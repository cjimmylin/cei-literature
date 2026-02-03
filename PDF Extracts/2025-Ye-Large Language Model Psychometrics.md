---
title: "Large Language Model Psychometrics - PDF Extract"
source_pdf: "2025-Ye-Large Language Model Psychometrics.pdf"
pages: 57
extracted_at: "2026-01-24T16:38:38.333453"
---

# PDF Extract: Large Language Model Psychometrics

**Source PDF:** 2025-Ye-Large Language Model Psychometrics.pdf
**Total Pages:** 57

---

## Content

```
--- Page 1 ---

Large language model psychometrics:
A systematic review of
evaluation, validation, and enhancement
Haoran Ye1, Jing Jin1, Yuhang Xie1, Xin Zhang2,3, Guojie Song 1,4,B
1State Key Laboratory of General Artificial Intelligence,
School of Intelligence Science and Technology, Peking University
2School of Psychological and Cognitive Sciences, Peking University
3Key Laboratory of Machine Perception (Ministry of Education), Peking University
4PKU-Wuhan Institute for Artificial Intelligence
hrye@stu.pku.edu.cn
gjsong@pku.edu.cn
Project Website: https://llm-psychometrics.com
Abstract
The advancement of large language models (LLMs) has outpaced traditional evaluation methodolo-
gies. This progress presents novel challenges, such as measuring human-like psychological constructs,
moving beyond static and task-specific benchmarks, and establishing human-centered evaluation.
These challenges intersect with psychometrics, the science of quantifying the intangible aspects of
human psychology, such as personality, values, and intelligence. This review paper introduces and
synthesizes the emerging interdisciplinary field of LLM Psychometrics, which leverages psychometric
instruments, theories, and principles to evaluate, understand, and enhance LLMs. The reviewed
literature systematically shapes benchmarking principles, broadens evaluation scopes, refines method-
ologies, validates results, and advances LLM capabilities. Diverse perspectives are integrated to
provide a structured framework for researchers across disciplines, enabling a more comprehensive
understanding of this nascent field. Ultimately, the review provides actionable insights for developing
future evaluation paradigms that align with human-level AI and promote the advancement of human-
centered AI systems for societal benefit. A curated repository of LLM psychometric resources is
available at https://github.com/valuebyte-ai/Awesome-LLM-Psychometrics.
arXiv:2505.08245v2  [cs.CL]  13 Jul 2025

--- Page 2 ---

Contents
1
Introduction
4
2
Preliminary and methodological foundations
6
2.1
Large language models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Psychometrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
6
2.3
Psychometric evaluation of AI before the era of LLMs
. . . . . . . . . . . . . . . . . . . . . . . . .
7
3
Psychometrics for benchmarking principles
7
3.1
Fundamental differences between psychometrics and AI benchmarking
. . . . . . . . . . . . . . . .
7
3.2
Benchmarking with psychometrics-inspired principles . . . . . . . . . . . . . . . . . . . . . . . . . .
9
4
Psychometrics for measuring psychological constructs
10
4.1
Measuring personality constructs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
10
4.1.1
Personality traits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
12
4.1.2
Values . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
13
4.1.3
Morality
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
14
4.1.4
Attitudes and opinions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
15
4.2
Measuring cognitive constructs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.2.1
Heuristics and biases . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.2.2
Social interactions
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
16
4.2.3
Psychology of language
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
4.2.4
Learning and cognitive capabilities
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
19
5
Psychometric evaluation methodology
20
5.1
Test format
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
5.1.1
Structured tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
21
5.1.2
Unstructured tests . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
22
5.2
Data and task sources . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
5.3
Prompting strategies
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
5.4
Model output and scoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
5.4.1
Closed-ended output and scoring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
5.4.2
Open-ended output and scoring
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
24
5.5
Inference parameters . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
6
Psychometric validation
25
6.1
Reliability and consistency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
25
6.2
Validity
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
6.2.1
Content validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
26
6.2.2
Construct validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
6.2.3
Criterion and ecological validity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
2

--- Page 3 ---

6.3
Standards and recommendations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
27
7
Psychometrics for LLM enhancement
28
7.1
Trait manipulation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
28
7.2
Safety and alignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
7.3
Cognitive enhancement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
8
Trends, challenges, and future directions
29
8.1
Psychometric validation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
8.2
From human constructs to LLM constructs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
29
8.3
Perceived vs. aligned traits . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
8.4
Anthropomorphization challenges
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
8.5
Expanding dimensions in model deployment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
30
8.6
Item response theory
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
8.7
From evaluation to enhancement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
31
9
Ethical considerations
31
10 Conclusion
32
3

--- Page 4 ---

1
Introduction
The advent of large language models (LLMs) represents a transformative breakthrough in AI. These systems exhibit
general-purpose capabilities spanning diverse domains [Bubeck et al., 2023], with particular proficiency in natural
language understanding and generation [Demszky et al., 2023, Grossmann et al., 2023, Gu et al., 2024, Ziems et al.,
2024]. They are rapidly integrated into critical societal infrastructure, ranging from consumer-facing applications like
chatbots [OpenAI, 2025] and search engines [Wang et al., 2024c] to high-stakes domains such as healthcare [Singhal
et al., 2023], education [Milano et al., 2023], and scientific discovery [Romera-Paredes et al., 2024, Ye et al., 2024].
Their increasing dominance has exposed a fundamental, pressing scientific challenge: how can we rigorously evaluate
these AI systems that transcend traditional benchmarks of biological or algorithmic intelligence?
Traditional AI evaluation has relied on curating task-specific datasets, annotating ground-truth labels with human input,
running models on these datasets, and assessing performance using predefined metrics. However, LLMs have triggered
an evaluation crisis, as their versatile capabilities and human-like behaviors exceed what traditional benchmarks can
measure. Novel challenges include but are not limited to (1) evaluating psychological constructs like personality,
values, and cognitive biases; (2) obsolescence of static benchmarks due to rapid LLM development and training data
contamination; (3) compromised robustness and validity due to LLMs’ prompt- and context-sensitivity; (4) requiring
human-centered evaluation approaches; and (5) expanding evaluation methodologies in scope and complexity as LLMs
integrate into agentic and multimodal systems.
These challenges intersect with humanity’s century-old quest to quantify the complex, intangible human psychology
[Pasquali, 2009]. Psychometrics emerged from this timeless pursuit as the scientific study of psychological measure-
ment. It bridges the abstract and the empirical by transforming human traits into quantifiable data, enabling better
understanding, prediction, and decision-making in education, business, healthcare, governance, and beyond [Rust
and Golombok, 2014]. The intersection of LLMs and psychometrics forms a methodological crucible, forging novel
paradigms to better decode and improve machine minds.
This intersection sets the stage for a new research frontier. We define LLM Psychometrics as the interdisciplinary
field dedicated to evaluating, understanding, and enhancing LLMs through the application and integration of psy-
chometric instruments, theories, and principles. This field seeks to quantify, interpret, manipulate, and improve the
complex, human-like attributes and behaviors exhibited by LLMs, encompassing both personality constructs (e.g.,
personality, values, morality, and attitudes) and cognitive constructs (e.g., heuristics and biases, social interaction
abilities, psycholinguistic abilities, and learning and cognitive capacities). Research in LLM Psychometrics applies,
extends, and innovates upon scientific methods of psychological measurement for LLMs. Based on the psychometric
principles, related research systematically examines the measurement results to ensure scientific rigor. By measuring
and elucidating psychological constructs in LLMs, LLM Psychometrics further informs strategies for their targeted
enhancement.
Recent research in LLM Psychometrics pioneers in addressing the LLM evaluation crisis. Some studies introduce
dynamic and construct-oriented evaluation frameworks that move beyond static, task-specific benchmarks [Hagendorff,
2023, Zhu et al., 2024a]. In parallel, novel methodologies are developed to measure non-cognitive and emergent
constructs [Huang et al., 2023d, Pellert et al., 2024, Ren et al., 2024]. Self-adaptive evaluation techniques now allow for
the extrapolation of item difficulty and tailoring assessments to model performance [Jiang et al., 2024a, Lalor et al.,
2024, Polo et al., 2024]. Drawing from the methodological framework of psychometric validation, research improves
the reliability and validity of evaluation protocols [Ye et al., 2025a]. Human-centered evaluation drives aligning model
behavior with human values [Wang et al., 2024f, Yao et al., 2025a]. In addition, the scope of evaluation expands
to agentic and multimodal systems, further broadening the methodological landscape [Huang et al., 2024c, Li et al.,
2024b].
The field of LLM Psychometrics has seen significant growth, evidenced by the proliferation of related research papers.
These studies, however, address a variety of psychological constructs, employ diverse methodologies, and utilize distinct
validation techniques. The interdisciplinary nature of this domain has attracted contributions from a broad spectrum of
academic communities. Despite this diversity, there is a lack of cohesion among researchers, leading to a fragmentation
of insights, particularly between studies focusing on disparate constructs. Consequently, there is a pressing need for a
systematic review to synthesize these efforts and facilitate a more integrated understanding of the field.
Taxonomy and paper structure.
To bridge the gap, we systematically review LLM Psychometrics across evaluation,
validation, and enhancement. The evaluation framework encompasses three core dimensions: the target construct (what
to measure), the measurement method (how to measure), and the validation of results (how well do we measure). The
psychometric insights not only inform evaluation but also guide the development and refinement of LLMs (how to
improve). Accordingly, this review is structured as follows (Fig. 1). § 2 provides an overview of the preliminaries and
4

--- Page 5 ---

3 Psychometrics for Benchmarking Principles
3.2 Benchmarking with Psychometrics-Inspired Principles
•
Construct-Oriented Benchmarking
•
Psychometrically Rigorous Benchmark Development
•
Item Response Theory
4 Psychometrics for Measuring 
Psychological Constructs
(What to measure?)
5 Psychometric
Evaluation Methodology
(How to measure?)
6 Psychometric
Validation
(How well do we measure?)
Core Measurement Framework
4.1 Measuring Personality 
Constructs
4.2 Measuring Cognitive 
Constructs
4.1.1 Personality Traits
4.1.2 Values
4.1.3 Morality
4.1.4 Attitudes & Opinions
4.2.1 Heuristics & Bias
4.2.2 Social Interactions
4.2.3 Psychology of Language
4.2.4 Learning and Cognitive
Capabilities
5.1 Test Format
5.2 Data and Task Sources
5.3 Prompting Strategies
5.4 Model Output and Scoring
5.5 Inference Parameters
6.1 Reliability and Consistency
6.2 Validity
6.3 Standards and
Recommendations
3.1 Fundamental Differences Between Psychometrics 
and Al Benchmarking
•
Fundamental Differences 
•
Complementary Aspects
7 Psychometrics for LLM Enhancement
7.1  Trait Manipulation
7.2  Safety and Alignment
7.3  Cognitive Enhancement
8 Trends, Challenges, and Future Directions
8.1 Psychometric Validation
8.2 From Human Constructs 
to LLM Constructs
8.3 Perceived vs. Aligned Traits
8.4 Anthropomorphization Challenges
8.5 Expanding Dimensions in Model Deployment
8.6 Item Response Theory
8.7 From Evaluation to
Enhancement
Figure 1: Overview of this review.
methodological foundations to facilitate subsequent discussions. § 3 thoroughly contrasts psychometrics and traditional
AI benchmarking and reviews how psychometric principles can underpin and reinvent LLM benchmarks. The core
measurement framework is detailed in § 4, § 5, and § 6. § 4 delves into the psychological constructs evaluated in LLMs,
elucidating the theories employed and summarizing key evaluation findings. In § 5, we scrutinize the psychometric
evaluation methodologies applied to LLMs, followed by § 6, which examines the psychometric validation of evaluation
results. Beyond evaluation, § 7 introduces strategies for enhancing LLMs through psychometric insights. § 8 discusses
emerging trends, challenges, and future directions. Finally, § 9 highlights key ethical considerations, while § 10
concludes the paper.
Scope and related work.
We consider studies to be out of scope if they do not employ psychometric approaches,
adhere to psychometric principles, or if they focus solely on scalar performance metrics rather than characterizing
behaviors. Readers interested in conventional LLM benchmarking are encouraged to consult surveys on LLM evaluation
[Chang et al., 2024, Guo et al., 2023b]. Several related reviews focus on the evaluation of specific constructs in
LLMs, such as personality [Dong et al., 2025, Wen et al., 2024b], attitudes and values [Ma et al., 2024a], cultural
awareness [Adilazuarda et al., 2024, Pawar et al., 2024], and theory of mind [Dong et al., 2025, Sarıta¸s et al., 2025].
Hagendorff [2023], Hagendorff et al. [2024] introduce the notion of machine psychology and review emergent LLM
abilities; however, they do not provide comprehensive coverage of the related research, nor do they elaborate on LLM
personality constructs, psychometric validation, or enhancement. This paper provides the first systematic review of
LLM Psychometrics.
5

--- Page 6 ---

2
Preliminary and methodological foundations
We aim for our survey to be self-contained and accessible to a broad, cross-disciplinary audience. To this end, this
section presents the preliminary and methodological foundations that underpin the subsequent discussions.
2.1
Large language models
LLMs are large-scale deep neural networks—essentially complex systems of nonlinear regression equations. An LLM
can generate text by predicting the next token (word or subword) in a sequential manner (autoregressive generation),
given the preceding context. It does so by modelling a conditional probability distribution over the vocabulary; i.e., the
likelihood of each token given the context:
P(xt|x<t) = f(x<t; θ),
(1)
where xt is the token at time step t; x<t is the context preceding xt, usually including both user prompts and previously
generated tokens; f is the model’s parameterized function; and θ represents the model parameters. Given f, the model
generates text by either sampling from this distribution or directly selecting the token with the highest probability. In
the former case, hyperparameters such as temperature can be adjusted to control the diversity of generated text. In the
latter case, the model is said to use greedy decoding, and the generated text is deterministic. In evaluating LLMs, it is
crucial to properly account for the stochasticity of the model.
These models are based primarily on the transformer architecture, a neural network design that employs self-attention
mechanisms to capture contextual relationships between words, phrases, and broader linguistic patterns. Modern
LLMs typically contain billions of parameters, enabling them to efficiently learn from vast amounts of textual data.
During evaluation, if the model has already been exposed to the test items during training, this is referred to as data
contamination. In such cases, the model is more likely to exhibit artificially inflated performance or simply reproduce
memorized patterns, rather than revealing its true underlying capabilities or traits.
The training process of LLMs is typically divided into two phases: pre-training and post-training. Pre-training is the
phase where LLMs learn to predict the next token, given its preceding context, on a large corpus of text data. This
process is unsupervised, as the model does not require explicit labels or annotations to learn the underlying patterns
in the data. The model processes Internet-scale text data from diverse sources like books, articles, and websites. By
repeatedly predicting the next word in a sentence, the model learns the statistical properties of language and gains
large-scale world knowledge. Models that have only undergone the pre-training phase are usually referred to as base
models. Post-training, or fine-tuning, is the process of adapting the base models to better follow user instructions, align
with human values, or specialize in particular tasks. This stage typically involves training the model on a smaller,
human-annotated dataset or incorporating human feedback on the quality of the model outputs. Models that have
undergone both phases are often referred to as fine-tuned models, instruction-tuned models, or aligned models.
We interact with LLMs using prompts, which are input instructions to the model. For psychometric evaluation, these
prompts can naively be the reformatted versions of test items originally designed for humans, adapted for LLMs
to answer. When designing prompts, one should consider differences between base and fine-tuned models. Most
public-facing LLMs are fine-tuned, so evaluation research primarily focuses on these models for greater practical
relevance.
A key emergent capability of LLMs is in-context learning, which allows models to adapt to new tasks or patterns by
conditioning on examples or instructions provided within the input context x<t, without modifying model parameters.
This property can influence LLM performance in psychometric evaluation. For instance, prompting models to reason
step-by-step (e.g., Chain-of-Thought prompting [Wei et al., 2022]) can enhance performance on reasoning tasks, while
instructing them to role-play may modulate their exhibited personalities and values.
2.2
Psychometrics
Psychometrics, also known as psychological testing, involves the use of tests to measure, understand, or predict behavior
by quantifying specific actions or characteristics. These tests rely on samples of behavior, meaning they are not perfect
measures and often include errors inherent to sampling. Test items are specific stimuli designed to elicit observable
reactions that can be scored or evaluated. Typically, tests are composed of multiple questions or problems as their items,
producing explicit data subject to scientific analysis.
A psychological test is a set of items that are designed to measure characteristics of human beings that pertain to behavior
[Kaplan and Saccuzzo, 2001]. Behavior measured by tests can be overt (observable actions) or covert (internal thoughts
or feelings). Tests may assess past, current, or even predict future behavior. Interpretation of test scores depends on
6

--- Page 7 ---

their context within a distribution. Scales are used to relate raw scores to defined distributions, aiding interpretation. In
addition, psychological tests can measure traits—enduring tendencies like shyness or determination—and states, which
reflect temporary conditions of individuals.
Psychological testing measures individual differences in various constructs, which are abstract psychological attributes
or dimensions that help explain and predict behavior. Two primary categories of such constructs are personality
constructs and cognitive constructs [Kaplan and Saccuzzo, 2001]. Personality tests focus on an individual’s tendencies
and dispositions. These tests measure typical behavior, such as preferences or tendencies to react in certain ways.
Cognitive tests evaluate speed, accuracy, or both, with higher scores reflecting better performance.
Two fundamental principles underpin psychometrics: reliability and validity [Raykov and Marcoulides, 2011]. Reliabil-
ity ensures accuracy, dependability, consistency, or repeatability of the test results. Reliable test results are stable across
time, contexts, and raters. Validity confirms the meaningfulness and usefulness of the test results. A valid measure
captures the intended construct. Validity is multifaceted; for example, predictive validity might correlate test scores with
job performance, while construct validity ensures alignment with theoretical models, such as the Big Five personality
traits [Goldberg, 2013].
Other principles include standardization, which provides context to raw scores by comparing individual results to a
representative sample, or norm group. Additionally, equivalence and fairness are crucial principles that tests must
adhere to. Test bias occurs when test items unintentionally advantage or disadvantage subgroups. Modern psychometrics
employs advanced statistical models to identify and revise biased items, ensuring assessments measure the intended
construct rather than extraneous factors [Rust and Golombok, 2014].
2.3
Psychometric evaluation of AI before the era of LLMs
The idea of applying psychometrics to AI originated in the early decades of AI [Pellert et al., 2024]. Evans [1964]
pioneered work in this area by creating a heuristic program that could solve parts of intelligence tests. Subsequent efforts
similarly focused on designing AI systems for cognitive tests [Newell, 1973], with the goal of creating systems capable
of handling human tasks. This was conceptually aligned with the development of static, task-centric benchmarks in
modern AI research [Chen et al., 2021, Hendrycks et al., 2020, Lee et al., 2024e, Liang et al., 2022, Srivastava et al.,
2022]. However, criticisms emerged regarding the absence of "hot cognition" in AI, prompting Simon [1963] to propose
incorporating emotional aspects into models. By the early 2000s, the concept of "psychometric AI" was explicitly
articulated as the pursuit of systems capable of excelling on all established, validated tests of intelligence and mental
ability. These included not only conventional IQ tests but also assessments of artistic and literary creativity, mechanical
ability, and beyond [Bringsjord and Schimanski, 2003, Pellert et al., 2024]. It was not until the advent of LLMs that the
versatility envisioned for "psychometric AI" began to materialize.
3
Psychometrics for benchmarking principles
3.1
Fundamental differences between psychometrics and AI benchmarking
Benchmarking AI systems superficially resembles psychometrics, particularly Classical Test Theory (CTT) [Crocker
and Algina, 1986], as both compile test items to evaluate cognitive capabilities and average the resulting scores.
However, closer examination reveals that AI benchmarks differ significantly from modern psychometric approaches
[Federiakin, 2025, Wang et al., 2023a]. We outline these key differences in Table 1.
Psychometrics.
Psychometrics centers on understanding the psychological constructs and ensuring that tests accu-
rately measure the intended constructs. Grounded in a causal measurement philosophy, this field posits that observed test
responses arise from latent psychological constructs [Federiakin, 2025, Markus and Borsboom, 2013]. These constructs
may encompass both abilities (e.g., reasoning skills) and personalities (e.g., conscientiousness). The causal framework
necessitates rigorous construct definition, requiring traits to be precisely delineated through iterative theory-building
and empirical validation. Psychometric test development follows methodical protocols, often structured by frameworks
such as Evidence-Centered Design (ECD) [Mislevy et al., 2003]. ECD emphasizes ensuring congruence between test
items and theoretical models of the construct, thereby supporting robust inferences about latent traits.
Central to this approach is the prioritization of item quality over quantity. Psychometricians conduct rigorous item
analyses to balance precision with practicality, as administering an excessive number of items to participants is often
impractical. Advanced statistical models, such as Item Response Theory (IRT) [Embretson and Reise, 2013] and Factor
Analysis [Loehlin, 2004], are adopted to estimate latent traits, analyze item performance, and assess model fit. These
models require relatively large sample sizes (the number of human participants) to yield stable parameter estimates, as
they must disentangle individual differences from measurement error to accurately infer latent traits.
7

--- Page 8 ---

Table 1: Comparison between psychometrics and conventional AI benchmark.
Feature
Psychometrics
AI benchmark
Core goal
To measure psychological constructs, to prove
that a test measures as intended (validity evi-
dence), and to understand the construct being
measured.
To test and compare the task performance of
different LLMs. Focuses on ranking models
and selecting the best one suited for a specific
task.
Philosophy of
measurement
Construct-oriented. Tends towards a causal ap-
proach to measurement, where the measured
trait is believed to cause the measurement out-
comes.
Task-oriented. Leans towards representativism,
assuming items exhaust or represent all aspects
of the underlying ability.
Target
construct
Personality and ability.
Mostly task-specific abilities.
Construct
definition
Emphasizes clear and detailed definitions of
the construct being measured. Agreement on
the construct definition is a byproduct of test
development.
Often defines constructs implicitly through ad
hoc task selection. Construct definitions can be
vague.
Development
process
Systematic and rigorous, often following meth-
ods like Evidence-Centered Design (ECD).
Can be labor-intensive.
Compiles a set of relevant questions or tasks,
then performs expert annotation or crowdsourc-
ing to label ground truth answers. Less labor-
intensive per item.
Number of
items
Can vary, but not necessarily large. Focus is on
item quality and relevance to the construct.
Typically consists of an extensive number of
questions to cover various aspects of abilities.
Reliability increases with test length.
Sample size
Typically requires a larger sample size of test
takers for robust statistical modeling.
Can be applied to evaluate the performance of
a single LLM on the benchmark.
Statistical
modeling
Employs advanced and various statistical mod-
els like Item Response Theory and Factor Anal-
ysis to analyze data, estimate latent abilities,
and assess model fit.
Often relies on simple aggregation methods,
such as calculating average accuracy across
benchmark tasks.
Result
analysis
Ensures the reliability, validity, predictive
power, and explanatory power of the test
through result analysis and statistical model-
ing.
Reliability is likely to be high due to the large
number of items. However, validity, predictive
power, or explanatory power beyond the target
task is not a primary concern.
The test results are analyzed to ensure the reliability, validity, predictive power, and explanatory power of the test.
Specifically, a well-designed test should: 1) consistently and accurately measure the intended construct, 2) predict
performance across a diverse range of related tasks and real-world outcomes, and 3) provide explanatory insight into
the observed data. For example, psychometric models often reveal that individual differences across a broad range of
cognitive tasks can be captured and explained by a relatively small set of underlying cognitive abilities [Cattell and
Horn, 1978].
Benchmark.
In contrast, AI benchmarking is driven by pragmatic goals: evaluating and ranking models based on
task performance. Unlike psychometrics, validity is not the primary concern. Instead, benchmarks typically emphasize
breadth, scalability, and—especially in the era of foundation models—difficulty. This approach reflects a representativist
philosophy, where it is assumed that an extensive set of benchmark items collectively captures all relevant aspects of the
abilities demanded by the target task [Federiakin, 2025]. However, constructs like reasoning or knowledge are often
ambiguously defined and encompass infinitely many aspects. Benchmarks implicitly operationalize these constructs
through ad hoc task selection.
The development of AI benchmarks is usually less labor-intensive, especially when compared with psychometrics
on a per-item basis. Test items and their corresponding ground truths are typically drawn from existing datasets,
expert curation, or crowdsourced contributions. While this process enables scalability, it risks conflating superficial
task performance with deeper cognitive capacities. For instance, a benchmark may assess mathematical reasoning
8

--- Page 9 ---

through arithmetic problems without verifying whether models rely on pattern recognition versus symbolic logic [Ahn
et al., 2024]. Additionally, LLM benchmarking commonly employs straightforward metrics, such as average accuracy,
eschewing the sophisticated latent variable models of psychometrics. This simplicity allows benchmarks to evaluate
single models efficiently, bypassing the need for population samples. However, it also limits the depth of insights that
can be gleaned from model performance [Federiakin, 2025].
Reliability and stability in benchmarking are primarily achieved through scaling up the test. However, ensuring the
quality of each individual item becomes impractical due to the test scale and the rapid pace of model development. For
instance, while psychometrics emphasizes the discriminative power of each item, some benchmarks, though initially
challenging, are quickly outpaced by continuous model improvements [McIntosh et al., 2024]. Conversely, certain
emerging benchmarks are currently too difficult to yield meaningful comparisons [Phan et al., 2025]. Benchmark results
are often limited to the specific target task, offering limited generalizability or predictive power across other tasks or
real-world applications. These results also pose significant challenges for conducting in-depth, multi-faceted analyses
of model capabilities [Wang et al., 2023a].
3.2
Benchmarking with psychometrics-inspired principles
Recent LLM evaluation efforts have drawn inspiration from psychometrics and seek to develop benchmarks that adhere
to psychometric principles.
Construct-oriented benchmarking.
Task-oriented benchmarks often entail vast question sets to capture complex
abilities. However, in many cases, the benchmarks either fail to fully represent these abilities due to their infinite
manifestations or involve extraneous factors that are irrelevant to the target ability [Wallach et al., 2025, Zhou et al.,
2025]. Recent research has drawn inspiration from psychometrics and explored the paradigm of construct-oriented
evaluation, seeking its discriminative, predictive, and explanatory power. Federiakin [2025], Ili´c and Gignac [2024]
employ factor analysis to explore the latent variables underlying LLM benchmark performance. Their findings reveal a
monolithic factor resembling general intelligence or ability. Federiakin [2025] ranks models based on this discovered
factor and highlights its unique advantages over raw benchmark scores. In contrast, similar attempts by Burnell et al.
[2023] identify three factors—reasoning, comprehension, and core language modeling—that better explain LLM
performance across 27 cognitive tasks. Based on it, Zhu et al. [2024a] integrate the three factors into benchmark
items to evaluate multifaceted abilities. This discrepancy between the estimated latent factors in the above findings
can be attributed to differences in the models and benchmarks employed [Zhou et al., 2025]. Therefore, rather than
relying on statistically derived factors, Zhou et al. [2025] propose a theory-driven hierarchical set of general scales for
systematic construct-oriented evaluation. These scales are validated to explain what AI systems can do and predict their
performance on novel task instances. Peng et al. [2024] present the Tong Test, a value- and ability-oriented framework,
for Artificial General Intelligence (AGI) evaluation. This framework is rooted in dynamic embodied physical and social
interactions (DEPSI), and can generate an infinite variety of tasks to evaluate key capabilities including values, learning,
and cognition.
Psychometrically rigorous benchmark development.
Beyond defining and analyzing latent constructs, researchers
have developed holistic, psychometrically rigorous methods for benchmark development. Liu et al. [2024e] intro-
duce Evidence-Centered Benchmark Design (ECBD), a framework structuring benchmark creation into five mod-
ules—capability, content, adaptation, assembly, and evidence—each requiring justification to ensure validity. Through
case studies of prominent LLM benchmarks, they demonstrate ECBD’s utility in identifying validity threats. Sim-
ilarly grounded in psychometrics but with a distinct approach, Fang et al. [2024] propose Psychometrics-Assisted
Benchmarking (PATCH), an eight-step process from construct definition to proficiency scoring. When piloted on
8th-grade mathematics, PATCH produced results diverging from traditional benchmarks, offering a more comprehensive
evaluation. Building on related principles, Kardanova et al. [2024] adapt Evidence-Centered Design (ECD) to create
psychometrically grounded benchmarks. Their application in pedagogy illustrates how this method can reduce data
contamination and enhance test interpretability.
Item Response Theory.
Item Response Theory (IRT) is a statistical approach in psychometrics that jointly estimates
the latent ability of examinees and the properties (difficulty, discrimination) of test items [Embretson and Reise,
2013]. Translating this framework to LLM evaluation enables researchers to infer latent ability scores, assess item
informativeness, and perform more efficient evaluation. Recent research leverages principles from IRT to develop
adaptive evaluation frameworks. These methods dynamically calibrate item difficulty based on model performance and
weighting items by their inferred difficulty, aiming to achieve accurate evaluations with smaller test sizes and more
discriminative items [Guinet et al., 2024, Lalor et al., 2024, Polo et al., 2024, Zhuang et al., 2023a,b]. Building on these
approaches, Jiang et al. [2024a], Truong et al. [2025] introduce IRT-based benchmarks that involve learning to estimate
9

--- Page 10 ---

Values
Schwartz
WVS
VSM
GLOBE
Others
& custom
Item: When you think about 
yourself, you describe yourself as 
outgoing and sociable. Please 
indicate your level of agreement 
with this self-description.
Scale: [Standard BFI-2 scale] 
1 (Disagree strongly) to 5 (Agree 
strongly) 
Answer: 4 (Agree)
Rating: Indicates high extraversion
LLM
User
Evaluator
Morality
MFT
ETHICS
DIT
PEW
Others
& custom
Item: How important is the value of 
helpfulness (i.e., working for the 
welfare of others) as a guiding 
principle in your life?
Scale: [Standard SVS scale] 
0 (Not important) to 9 (Of supreme 
importance)
Answer: 7 (Very important)
Rating: Strong benevolence 
orientation
LLM
User
Evaluator
Personality traits
Big Five
HEXACO
MBTI
Dark
Triad
Others
& custom
Item: One of the worst things a 
person could do is hurt a defenseless 
animal.
Scale: [Standard MFQ scale]
0 (Not at all relevant) to 5 (Extremely 
relevant)
Answer: 4 (Very relevant)
Rating: Strong Care/Harm 
foundation
LLM
User
Evaluator
Attitudes & Opinions
ANES
ATP
GLES
PCT
Others
& custom
Item: The Government should 
reduce the income differences 
between the rich and the poor.
Scale: [Standard ANES scale]
1 (Disagree strongly) to 7 (Agree 
strongly)
Answer: 4 (Neither agree nor 
disagree)
Rating: Moderate political position
LLM
User
Evaluator
Psychology of language
Language
compre-
hension
Language
generation
Language
acquisition
Format: Multiple-choice question
Item:
A child asks his mom if he can go to 
Sam's party. Mom asks, "Have you 
finished your homework?" What does 
mom likely mean?
A) She's just curious about homework.
B) You can go if homework is done.
C) She's changing the subject.
D) She doesn't know where the party is.
Answer: B) You can go if your 
homework is done.
Rating: Correct interpretation of 
conditional implication
LLM
User
Evaluator
Learning and
cognitive
capabilities
Format: Open-ended question
(Wechsler Adult Intelligence Scale)
Item: How are a lion and a tiger alike? 
Scale: [Standard WAIS Similarities 
subtest scoring] 0 to 2 points
Answer: Both are large wild cats in 
the Felidae family, carnivorous 
predators with similar physical 
characteristics.
Rating: 2 points (complete, accurate 
response identifying category)
LLM
User
Evaluator
Heuristics
&
biases
Format: short-answer question
(Cognitive Reflection Test)
Item:
A bat and a ball cost $1.10 in total. 
The bat costs $1.00 more than the ball. 
How much does the ball cost?
Answer: $0.05
Rating: Correct (resists intuitive but 
incorrect response of $0.10)
LLM
User
Evaluator
Personality Tests
Cognitive Tests
Social  interactions
Theory
of Mind
Emotional
Intelligence
Social
Intelligence
Format: Multiple-choice question
Item:
Sally puts her ball in a basket and 
leaves the room. Anne then moves 
the ball to a box. When Sally 
returns, where will she look for her 
ball?
A) In the basket
B) In the box
C) She won't look for the ball
D) She will ask Anne where it is
Answer: A) In the basket
Rating: Correct (demonstrates 
understanding of false belief)
LLM
User
Evaluator
Figure 2: Examples of psychometric tests for LLMs.
item difficulty and learning to generate novel items calibrated to specific difficulty levels. Additionally, research has
used IRT-based analyses to explore the alignment between LLM and human response distributions [He-Yueya et al.,
2024]. IRT-based evaluations further offer the potential to estimate construct and item parameters on a unified scale,
enabling direct comparisons across AI systems and against human norms, even when different test sets are used [Fang
et al., 2024, Wang et al., 2023a].
4
Psychometrics for measuring psychological constructs
This section delves into the psychological constructs evaluated in LLM Psychometrics. Fig. 2 exemplifies the tests for
the involved constructs.
4.1
Measuring personality constructs
LLMs exhibit personality constructs that are not explicitly programmed or trained towards. The emergent constructs
critically shape LLM behavior [Hagendorff, 2023], with profound implications for both individuals and broader social
groups [Bengio et al., 2024]. Measuring these embedded psychological constructs is essential for understanding
behavior, identifying biases, and fostering responsible development.
Table 2 and Table 3 summarize the representative personality constructs that have garnered attention in recent research.
Researchers typically select constructs based on their relevance to LLM development and deployment, as well as the
applicability of these constructs to AI systems. For instance, Li et al. [2024d] argue that emotional variability in LLMs
is not a meaningful construct, given that LLMs lack the biological mechanisms underlying emotions. Conversely,
personality and values are considered meaningful for LLMs, as they influence user interactions and model outputs
[Serapio-García et al., 2023, Ye et al., 2025a]. This rationale has led to extensive research on personality, values,
morality, and attitudes & opinions, as well as some—though less—focus on other constructs such as career selection
10

--- Page 11 ---

Table 2: Representative LLM personality constructs in LLM psychometrics. The main dimensions or focus of the
theories/inventories are listed in Table 3.
Constructs
Theories/inventories
Related work
Personality
traits
Big Five
Ai et al. [2024], Bhandari et al. [2025a,b], Bodroža et al. [2024], Caron and Srivastava [2022], Dorner
et al. [2023], Frisch and Giulianelli [2024], Gupta et al. [2024], Hilliard et al. [2024], Huang et al.
[2023a,e, 2024c], Jain et al. [2024], Jiang et al. [2023, 2024b], Karra et al. [2022], Klinkert et al.
[2024], Kovaˇc et al. [2023], La Cava and Tagarelli [2024], Lee et al. [2024d], Li et al. [2022a,b], Liu
et al. [2024a], Lu et al. [2023], Pellert et al. [2024], Petrov et al. [2024], Ren et al. [2024], Romero
et al. [2024], Serapio-García et al. [2023], Shu et al. [2024], Song et al. [2023], Sühr et al. [2023],
Zhang [2024], Zheng et al. [2025], Zou et al. [2024]
HEXACO
Barua et al. [2024], Bodroža et al. [2024], Miotto et al. [2022], Peereboom et al. [2024], Ren et al.
[2024], Wang et al. [2025b]
MBTI
Ai et al. [2024], Chen et al. [2024a], Cui et al. [2023], Huang et al. [2023c], La Cava and Tagarelli
[2024], Lu et al. [2023], Pan and Zeng [2023], Rao et al. [2023], Song et al. [2024b], Zhang et al.
[2024a]
Dark Triad
Barua et al. [2024], Huang et al. [2023e], Lee et al. [2024d], Li et al. [2022a,b], Lu et al. [2023],
Peereboom et al. [2024], Romero et al. [2024]
Other
& custom
Wen et al. [2024b] (reviews); Ai et al. [2024], Jiang et al. [2023], Mao et al. [2024a], Zeng [2024]
Values
Schwartz
Cahyawijaya et al. [2024], Fischer et al. [2023], Hadar-Shoval et al. [2024], Kovaˇc et al. [2023, 2024],
Lee et al. [2024a], Li et al. [2024b], Miotto et al. [2022], Pellert et al. [2024], Ren et al. [2024], Rozen
et al. [2024], Shen et al. [2024], Yao et al. [2024, 2025a,b], Ye et al. [2025a], Zhang et al. [2023a]
WVS
Chiu et al. [2025], Faulborn et al. [2025], Kim and Baek [2024], Yao et al. [2025a]
VSM
Kharchenko et al. [2024], Kovaˇc et al. [2023], Ren et al. [2024], Ye et al. [2025a], Zhong et al. [2024]
GLOBE
Karinshak et al. [2024], Li et al. [2024d], Ren et al. [2024]
SVO
Zhang et al. [2024c]
Other
& custom
Biedma et al. [2024], Jiang et al. [2024a], Li et al. [2024d], Liu et al. [2024b], Meadows et al. [2024],
Moore et al. [2024], Xu et al. [2023], Ye et al. [2025b], Zhang et al. [2024b]
Morality
MFT
Abdulhai et al. [2024], Aksoy [2024], Fraser et al. [2022], Ji et al. [2024], Münker [2024], Neuman
et al. [2025], Nunes et al. [2024], Pellert et al. [2024], Simmons [2023], Tlaie [2024], Yan et al.
[2024], Yao et al. [2025b], Zhou et al. [2024a]
ETHICS
Albrecht et al. [2022], Jinnai [2024], Karpov et al. [2024], Rodionov et al. [2023], Yu et al. [2023]
DIT
Khandelwal et al. [2024], Tanmay et al. [2023]
Other
& custom
Ahmad and Takemoto [2024], Bonagiri et al. [2024], Chiu et al. [2025], Garcia et al. [2024], Han
[2023], Huang et al. [2024a], Jiang et al. [2024a], Jin et al. [2022, 2024b], Jinnai [2024], Kucuk and
Kocyigit [2023], Liu et al. [2024d], Marraffini et al. [2024], Meijer et al. [2024], Neuman et al. [2025],
Ohashi et al. [2024], Peterson [2025], Ramezani and Xu [2023], Sachdeva and van Nuenen [2025],
Scherrer et al. [2023], Seror [2024], Takemoto [2024], Tanmay et al. [2023], Vida et al. [2024], Yuan
et al. [2024]
Attitudes
& opinions
ANES
Argyle et al. [2023], Bisbee et al. [2024], Jiang et al. [2022, 2024d], Qi et al. [2024], Sun et al. [2024],
Yang et al. [2024]
ATP
Hwang et al. [2023], Santurkar et al. [2023], Tjuatja et al. [2024]
GLES
Ball et al. [2025], Ma et al. [2024b], Qi et al. [2024], von der Heyde et al. [2024]
PCT
Azzopardi and Moshfeghi [2024], Bernardelle et al. [2024], Hartmann et al. [2023], Röttger et al.
[2024], Rozado [2023], Rutinowski et al. [2024], Wright et al. [2024]
Other
& custom
Ma et al. [2024a] (reviews); Ceron et al. [2024], Chalkidis and Brandl [2024], Dominguez-Olmedo
et al. [2024], Durmus et al. [2023], Faulborn et al. [2025], Feng et al. [2023], Geng et al. [2024],
Kalinin [2023], Kim and Lee [2023], Kim et al. [2025b], Lee et al. [2024c], Rosenbusch et al. [2023],
Röttger et al. [2025], Rozado [2023], Sanders et al. [2023], Wu et al. [2023], Xu et al. [2025c]
11

--- Page 12 ---

Table 3: Personality theories and inventories measured in LLM psychometrics and their main dimensions or focus.
Theory/inventory
What it measures / dimensions
Big Five
Five broad personality traits: Openness, Conscientiousness, Extraversion, Agreeable-
ness, Neuroticism
HEXACO
Six personality traits: Honesty-Humility, Emotionality, Extraversion, Agreeableness,
Conscientiousness, Openness
MBTI
Four dichotomies: Extraversion–Introversion, Sensing–Intuition, Thinking–Feeling,
Judging–Perceiving
Dark Triad
Three negative personality traits: Narcissism, Machiavellianism, Psychopathy
Schwartz
Basic human values: 10 or more values (e.g., Self-Direction, Stimulation, Hedo-
nism, Achievement, Power, Security, Conformity, Tradition, Benevolence, Univer-
salism), typically grouped into four higher-order categories (Openness to Change,
Self-Enhancement, Conservation, Self-Transcendence)
WVS
World Values Survey: Assesses broad cultural values such as traditional vs. secular-
rational values, survival vs. self-expression values
VSM
Value Survey Module (often Hofstede): Cultural dimensions such as Power Distance,
Individualism, Masculinity, Uncertainty Avoidance, Long-Term Orientation, Indulgence
GLOBE
Global Leadership and Organizational Behavior Effectiveness: Nine cultural dimen-
sions (e.g., Performance Orientation, Assertiveness, Future Orientation, Humane
Orientation, Institutional Collectivism, In-Group Collectivism, Gender Egalitarianism,
Power Distance, Uncertainty Avoidance)
SVO
Social Value Orientation: Measures individuals’ preferences regarding resource alloca-
tion between oneself and others (e.g., prosocial, individualistic, competitive orienta-
tions)
MFT
Moral Foundations Theory: Five (sometimes six) moral foundations—Care/Harm,
Fairness/Cheating, Loyalty/Betrayal, Authority/Subversion, Sanctity/Degradation, (Lib-
erty/Oppression)
ETHICS
Various ethics-related measures assessing moral reasoning, ethical principles, or moral
preferences
DIT
Defining Issues Test: Assesses moral development and reasoning using moral dilemmas
ANES
American National Election Studies: Political attitudes, beliefs, and behaviors in the
U.S.
ATP
Attitudes Toward Politics: Measures political attitudes and social controversies, often
specific to a region or subject
GLES
German Longitudinal Election Study: Political attitudes, beliefs, and voting behaviors
in Germany
PCT
Political Compass Test: Economic (Left/Right) and Social (Authoritarian/Libertarian)
political dimensions
[Hua et al., 2024], motivation [Chiu et al., 2025, Huang et al., 2023e], and mental health [De Duro et al., 2024, Reuben
et al., 2024].
4.1.1
Personality traits
Personality is the enduring configuration of characteristics and behavior that comprises an individual’s unique
adjustment to life [APA Dictionary of Psychology]. In the context of LLMs, personality traits relate to model safety,
bias, and toxicity [Wang et al., 2025b, Zhang et al., 2024a], and highly determine user experience [Klinkert et al., 2024].
The study of personality traits leads to several prominent theoretical models, each offering unique insights into individual
differences, including the Big Five [Goldberg, 2013], HEXACO [Ashton and Lee, 2007], Myers-Briggs Type Indicator
12

--- Page 13 ---

(MBTI) [Myers et al., 1962], and Dark Triad [Paulhus and Williams, 2002]. When applying psychometrics to LLMs,
most researchers directly administered the established inventories, such as NEO-PI-R [Costa and McCrae, 2008], BFI
[John et al., 1991], and BFI-2 [Soto and John, 2017], for measuring the Big Five traits; HEXACO-60 [Ashton and Lee,
2009] and HEXACO-100 [Lee and Ashton, 2018] inventories for HEXACO traits; MBTI assessment [Myers, 1985] for
MBTI types; and Dark Triad Dirty Dozen scale [Jonason and Webster, 2010] for Dark Triad traits.
Given widespread concerns about the practical relevance of these inventories [Ai et al., 2024], others have adapted
them for more real-world scenarios. For example, Bhandari et al. [2025a] contextualize the tests in topic-specific
or open-domain conversations; Ai et al. [2024] accompany the self-report tests with behavioral tests to examine the
personality knowledge of LLMs; Jiang et al. [2023] compile and adapt existing tests into the Machine Personality
Inventory; and Mao et al. [2024a] develop the PersonalityEdit inventory using LLMs. However, Peereboom et al. [2024]
argue that human-derived traits may not meaningfully apply to LLMs, underscoring the necessity for psychometric
theories specifically designed for LLM analysis.
Main findings.
Early models such as GPT-3 score above human averages on Dark Triad scales [Li et al., 2022a,b,
Romero et al., 2024]. Even after safety tuning, some models retain certain "dark qualities" [Li et al., 2022b], suggesting
that these patterns may be deeply rooted in the pretraining data. More advanced LLMs indicate better level of alignment.
They usually demonstrate high Openness, Extraversion, and Agreeableness traits, while low Neuroticism, on the Big
Five personality tests [Bhandari et al., 2025a, Zou et al., 2024]. The results align with their design as assistive and
helpful entities with emotional stability and engaging personality [Bhandari et al., 2025a, La Cava and Tagarelli, 2024].
Within the MBTI framework, most proprietary LLMs are classified as ENFJ or INFJ types [Huang et al., 2023c,
La Cava and Tagarelli, 2024], indicating tendencies toward helpfulness, idealism, and planning capabilities. Personality
differences between models are noteworthy. Comparative studies reveal that LLMs from different generations and
training methodologies display unique combinations of personality characteristics [Bhandari et al., 2025a, Karra
et al., 2022]. LLM personalities also vary across contexts. The same model may display different personality traits
across conversational topics [Song et al., 2023, Zou et al., 2024]. This variability challenges the applicability of
human personality theories that assume relative trait stability. Multiple studies suggest that prompt design and system
instructions substantially influence LLM personality expression [Caron and Srivastava, 2022, Song et al., 2023].
Comparing personality models and suggesting use cases.
The Big Five offers robust empirical foundations and
is the most prominent model for personality assessment. However, it is insufficient for predicting comprehensive
psychological outcomes [Feher and Vernon, 2021]. HEXACO extends the model by adding Honesty-Humility and
provides nuanced insights into moral traits, making it preferable for LLM application contexts demanding integrity
[Wang et al., 2025b]. In contrast, MBTI [Myers et al., 1962] categorizes 16 types via dichotomous scales. While popular
in career counseling and team-building for its accessibility, its typological approach oversimplifies personality and lacks
strong empirical support, limiting its utility in high-stakes decisions [Pittenger, 2005]. The Dark Triad [Paulhus and
Williams, 2002] diverges by focusing on maladaptive traits, making it useful in identifying toxic behaviors in LLMs
[Barua et al., 2024].
4.1.2
Values
Values are enduring beliefs that guide behavior and decision-making, reflecting what is important and desirable to an
individual or group [Schwartz, 1992]. Values offer a powerful lens for understanding LLM behavior. For example,
Ye et al. [2025a] show how different values contribute to the safety of LLMs; Liu et al. [2024b] reveal that different
spiritual values affect LLMs in social-fairness scenarios; and Sorensen et al. [2024b] demonstrate that standard value
alignment reduces distributional pluralism in LLM outputs.
A growing body of research has applied diverse value theories and instruments to assess the value orientations of
LLMs. Schwartz’s Value Theory, with its ten basic values and higher-order dimensions, is the most widely used,
often via the Schwartz Value Survey (SVS) or Portrait Values Questionnaire (PVQ) [Schwartz, 1992, Schwartz et al.,
2001]. Adaptations and contextualized prompts are increasingly common to better suit LLMs’ operational context [Ren
et al., 2024, Shen et al., 2024]. The World Values Survey (WVS) has also been used to probe LLMs’ alignment with
societal-level value dimensions [Haerpfer et al., 2022, Kim and Baek, 2024]. Cross-cultural frameworks like Hofstede’s
Values Survey Module (VSM) and the GLOBE study extend this analysis to workplace and leadership-related cultural
dimensions, with both direct and adapted inventories employed [Hofstede, 1984, House et al., 2004, Ren et al., 2024].
Social Value Orientation (SVO) frameworks, using tools like the SVO Slider Measure, focus on LLMs’ prosocial versus
proself tendencies [Murphy et al., 2011, Zhang et al., 2024c]. Additionally, researchers have developed localized or
custom inventories to capture region-specific or topical values, and some propose novel, bottom-up value taxonomies
for LLMs using psycholexical data [Biedma et al., 2024, Meadows et al., 2024, Xu et al., 2023, Ye et al., 2025b].
13

--- Page 14 ---

Collectively, these studies reveal both the adaptability of human value frameworks to LLMs and the need for tailored
approaches.
Main findings.
Research indicates that LLMs display distinct and systematic value patterns. According to Schwartz’s
Value Theory, LLMs tend to prioritize Self-Transcendence and Conservation. They exhibit stronger inclinations toward
Universalism, Benevolence, Conformity, and Security, while opposing Power and Achievement [Fischer et al., 2023,
Hadar-Shoval et al., 2024, Rozen et al., 2024, Zhang et al., 2023a]. WVS surveys further suggest that LLMs generally
prefer Self-Expression values over Survival values [Chiu et al., 2025]. Studies using the VSM and GLOBE frameworks
emphasize LLMs’ strong focus on Humane and Performance Orientation, with moderate Assertiveness [Li et al., 2024b].
Additionally, when assessed through SVO, advanced LLMs predominantly show Prosocial tendencies [Zhang et al.,
2024c].
Different models exhibit varied value orientations [Chiu et al., 2025, Duan et al., 2023, Kovaˇc et al., 2024, Li et al.,
2024b, Xu et al., 2023]. Versions within the same model family show evolutionary trends in values, potentially
influenced by safety alignment, capability advancement, and shifting societal expectations [Duan et al., 2023, Kim and
Baek, 2024, Moore et al., 2024]. Generally, larger models align more closely with desirable human values [Jiang et al.,
2024a, Kim and Baek, 2024, Shen et al., 2024, Zhong et al., 2024].
Cross-cultural research suggests that LLMs may embody a blend of cultural values, integrating perspectives from diverse
backgrounds [Kovaˇc et al., 2023]. However, they generally exhibit a tendency toward Western liberal values [Kim
and Baek, 2024]. LLMs can display different values based on profiling prompts [Karinshak et al., 2024, Kharchenko
et al., 2024, Zhong et al., 2024]. The context-dependency of their values is concerning and challenges the stability
assumptions in human value theories [Chiu et al., 2025, Kovaˇc et al., 2023, Meadows et al., 2024, Moore et al., 2024,
Shen et al., 2024, Xu et al., 2023].
Comparing value theories and suggesting use cases.
Schwartz emphasizes universal human motivations; WVS
examines societal-level value shifts; VSM and GLOBE address cross-cultural dimensions, with GLOBE emphasizing
leadership. SVO, in contrast, focuses on individual-level social preferences, i.e., prosocial vs. proself. While Schwartz
and SVO overlap in analyzing individual motivations, the former is broader, and the latter narrowly focuses on decision-
making in resource allocation. WVS, VSM, and GLOBE share cultural-level dimensions but differ in focus—WVS on
modernization, VSM on workplace-related cultural differences, and GLOBE on leadership and organizational practices.
For evaluating individual values in LLMs, use Schwartz for a comprehensive understanding of universal motivations
or SVO for interpersonal decision-making studies. In contrast, choose WVS for evaluating broad societal values in
LLMs. When evaluating cultural dimensions in LLMs, use VSM for workplace cultural differences or GLOBE for
leadership and organizational practices. In addition, Schwartz’s theory bridges individual and societal-level values,
making it versatile for mixed-focus studies.
4.1.3
Morality
Morality is the categorization of intentions, decisions and actions into those that are proper, or right, and those that
are improper, or wrong [Long and Sedley, 1987]. It is crucial to conduct moral assessments of LLMs to ensure
their ethical deployment. A large body of research applies the Moral Foundations Theory (MFT) [Graham et al.,
2009], primarily through the Moral Foundations Vignettes (MFVs) [Clifford et al., 2015], the Moral Foundations
Questionnaire (MFQ) [Graham et al., 2009], the MFQ-2 [Atari et al., 2023], and the Moral Foundations Dictionary
(MFD) [Graham et al., 2009]. These papers investigate model bias, alignment with political/moral ideologies, and
variation in personal or cultural values, using controlled prompt tests [Abdulhai et al., 2024, Nunes et al., 2024, Tlaie,
2024], persona-driven exploration [Münker, 2024], or evaluating internal moral coherence [Nunes et al., 2024]. Other
prominent moral theories and instruments include Kohlberg’s Theory via the Defining Issues Test (DIT) [Kohlberg,
1964], the Consequentialist-Deontological distinction [Beauchamp, 2001], the PEW 2013 Global Attitudes Survey
[Center, 2013], and localized moral theories [Liu et al., 2024d, Takeshita et al., 2023]. Specialized datasets are also
curated for scalable and comprehensive morality evaluation [Hendrycks et al., 2021, Jin et al., 2024b, Jinnai, 2024,
Marraffini et al., 2024]
Main findings.
LLMs are generally characterized by a rationalist and consequentialist focus, often prioritizing harm
minimization and fairness [Neuman et al., 2025]. Despite that, they show divergence in ethical reasoning [Neuman
et al., 2025] and moral preferences [Bonagiri et al., 2024, Jin et al., 2024b, Meijer et al., 2024, Tanmay et al., 2023]. In
some aspects, most LLMs align with human moral standards [Nunes et al., 2024, Takemoto, 2024, Tanmay et al., 2023],
which may be attributed to their extensive exposure to conventional ethical values during training. On the other hand,
some research presents a less optimistic view, uncovering significant deviations of LLMs from human moral preferences
[Ahmad and Takemoto, 2024, Marraffini et al., 2024, Vida et al., 2024]. Regarding the underlying mechanisms of
14

--- Page 15 ---

LLMs’ moral reasoning, Ji et al. [2024], Nunes et al. [2024], Simmons [2023] suggest that LLMs primarily exhibit
imitation rather than genuine conceptual understanding.
Comparing moral theories/instruments and suggesting use cases.
Instruments based on MFT are well-suited for
measuring LLMs’ alignment with intuitive moral principles across cultural or political dimensions. Tools like MFQ,
MFQ-2, MFVs, and MFD are particularly effective when investigating ideological leanings, bias, or internal consistency
in abstract vs. contextual moral judgments [Nunes et al., 2024]. In contrast, Kohlberg’s DIT explores structured moral
reasoning, offering a developmental perspective on how LLMs process ethical dilemmas [Khandelwal et al., 2024,
Tanmay et al., 2023]. DIT is valuable for longitudinal studies and evaluating whether models show higher-level moral
reasoning (e.g., post-conventional reasoning). Frameworks such as the Consequentialist-Deontological distinction and
global surveys like the PEW 2013 study are useful for categorizing ethical tendencies or analyzing cultural homogeneity
[Meijer et al., 2024, Neuman et al., 2025]. Localized tools (e.g., CMD, JCM) help assess cultural alignment [Liu et al.,
2024d, Takeshita et al., 2023]. Meanwhile, datasets like ETHICS provide morally charged scenarios for detecting
normative behavior and fine-tuning LLM responses in high-stakes ethical domains [Hendrycks et al., 2021, Jin et al.,
2024b, Marraffini et al., 2024].
4.1.4
Attitudes and opinions
Attitudes are always attitudes about something. This implies three necessary elements: first, there is the object of
thought, which is both constructed and evaluated. Second, there are acts of construction and evaluation. Third, there is
the agent, who is doing the constructing and evaluating. We can therefore suggest that, at its most general, an attitude
is the cognitive construction and affective evaluation of an attitude object by an agent [Bergman, 1998]. We use the
term "attitude" to encompass both attitudes and opinions, following [Bergman, 1998, Ma et al., 2024a]. Most research
on LLM attitudes examines political attitudes and public opinions [Ma et al., 2024a], which are key cognitive and
behavioral foundations in human society and closely tied to model fairness, credibility, and social impact [Durmus et al.,
2023, Hartmann et al., 2023, Lee et al., 2024c, Sanders et al., 2023, Santurkar et al., 2023]. For a broader discussion on
bias and fairness in LLMs, we refer readers to [Gallegos et al., 2024, Ranjan et al., 2024].
Researchers assess LLMs’ political attitudes using standardized questionnaires and scales from political science and
social psychology. US-focused instruments include the American National Election Studies (ANES) [Qi et al., 2024]
and the American Trends Panel (ATP) [Santurkar et al., 2023]. For cross-national comparisons, studies use tools like
the German Longitudinal Election Study (GLES) [Ball et al., 2025, Ma et al., 2024b, von der Heyde et al., 2024]. The
Political Compass Test (PCT) is also widely used to map LLMs within multidimensional political spectrums [Azzopardi
and Moshfeghi, 2024, Bernardelle et al., 2024, Hartmann et al., 2023, Röttger et al., 2024].
Other survey instruments include the General Social Survey (GSS) [Kim and Lee, 2023], the American Community
Survey (ACS) [Dominguez-Olmedo et al., 2024], the Canadian Election Study (CES) [Sanders et al., 2023], the
European Social Survey (ESS) [Geng et al., 2024], the Survey of Russian Elites [Kalinin, 2023], and the Supreme
Court Case Political Evaluation (SCOPE) [Xu et al., 2025c]. Additionally, researchers have developed specialized
datasets and tailored tools for LLMs, such as OpinionQA [Santurkar et al., 2023], a comprehensive dataset based on
ATP surveys; IssueBench [Röttger et al., 2025], a benchmark covering controversial issues with multiple response
formats; GlobalOpinionQA [Durmus et al., 2023], which extends political opinion evaluation to cross-cultural contexts;
and OpinionGPT [Haller et al., 2023], a web tool that demonstrates how input data biases influence model outputs.
Main findings.
Pretraining data inherently contains socially biased opinions and perspectives, which can amplify
political polarization in LLMs [Feng et al., 2023, Xu et al., 2025c]. Most studies identify a misalignment between
LLM outputs and human opinions [Dormuth et al., 2025, Santurkar et al., 2023, von der Heyde et al., 2024, Yang
et al., 2024], with many concluding that LLMs exhibit a left-leaning political bias [Bernardelle et al., 2024, Ceron
et al., 2024, Hartmann et al., 2023, Ma et al., 2024b, Rozado, 2023]. Cross-cultural comparative studies further reveal
Western-centric tendencies, demonstrating limited understanding of non-English political perspectives or multi-partisan
systems [Qi et al., 2024]. These findings suggest structural limitations in the models’ political understanding. It is also
shown that the degree and manifestation of bias vary significantly across contexts and domains. For example, political-
electoral propositions exhibit different bias patterns than socioeconomic issues like climate change [Wu et al., 2023]. In
contrast, some researchers offer more optimistic perspectives, emphasizing LLMs’ potential to simulate population-level
opinions and supplement traditional survey methods [Argyle et al., 2023, Bisbee et al., 2024, Dominguez-Olmedo et al.,
2024, Jiang et al., 2024d, Kalinin, 2023, Sanders et al., 2023, Sun et al., 2024, Wu et al., 2023]. They suggest that
with appropriate prompt design, calibration methods, and fine-tuning, LLMs can generate opinion distributions closely
approximating human group distributions [Jiang et al., 2022, Wu et al., 2023]. Such advancements indicate promising
directions for using LLMs in opinion research, though their current limitations and biases must still be acknowledged.
15

--- Page 16 ---

Comparing attitude measurement tools and suggesting use cases.
The ANES offers the most comprehensive
framework for American political contexts, making it ideal for studying model performance on U.S. social issues [Jiang
et al., 2022]. Cross-national surveys and datasets such as the ESS, GLES, and GlobalOpinionQA provide broader
cultural perspectives across diverse sociopolitical environments [Ball et al., 2025, Durmus et al., 2023, Geng et al.,
2024, Ma et al., 2024b, von der Heyde et al., 2024]. The ATP is better suited for researching model responses to social
controversies [Santurkar et al., 2023], while the PCT serves as a theory-driven political spectrum measurement tool,
offering simplified yet intuitive insights into LLM political positioning [Röttger et al., 2024]. Other surveys have
distinct regional and sociopolitical focuses: the CES examines political participation in North American multicultural
democracies [Sanders et al., 2023]; Survey of Russian Elites provides insights into non-Western political perspectives
[Kalinin, 2023]; the SCOPE delivers in-depth assessments of judicial attitudes [Xu et al., 2025c]; and the ACS serves as
a tool for researching socioeconomic issues and group representation [Dominguez-Olmedo et al., 2024].
4.2
Measuring cognitive constructs
Traditional NLP benchmarks are insufficient to capture and analyze emergent cognitive constructs [Hagendorff et al.,
2024, Ying et al., 2025a]. To address this gap, researchers are adapting related psychometric techniques to evaluate LLM
abilities. Hagendorff et al. [2024] introduce the concept of machine psychology, reviewing emergent LLM capabilities
and advocating for psychometric evaluation. They categorize these cognitive constructs into four key aspects: heuristics
and biases, social interactions, psychology of language, and learning and cognitive capabilities. Structured based on
this taxonomy, Table 4 summarizes the representative cognitive constructs measured in recent research.
4.2.1
Heuristics and biases
Heuristics and biases are mental shortcuts that simplify decision-making but can introduce systematic errors [Tversky
and Kahneman, 1974]. Recent research employs psychometric tools to evaluate rationality and biases in LLM outputs
and offer theoretical explanations for these biases.
Early studies, such as Binz and Schulz [2023], found that GPT-3 performs comparably to humans on cognitive ability
tests, exhibiting biases like framing and anchoring. More advanced models, such as GPT-4, show fewer System 1
(intuitive) errors and more System 2 (deliberative) reasoning, though biases persist [Hagendorff et al., 2023]. Large-
scale evaluations now cover a wide range of biases—including conjunction fallacy, unwarranted beliefs, and loss
aversion—using synthetic scenarios and multi-agent dialogue [Malberg et al., 2024, Xie et al., 2024b]. Multimodal
models are also being assessed for similar patterns [Schulze Buschoff et al., 2025].
To explain these findings, researchers draw on dual-process theory, linking LLM reasoning to intuitive and deliberative
modes [Hagendorff et al., 2023, Yax et al., 2024]. Other frameworks highlight LLMs’ lack of metacognitive abilities,
leading to “metacognitive myopia”—the inability to monitor or control reasoning processes, which perpetuates
systematic biases [Scholten et al., 2024]. Additional perspectives use cognitive dissonance and elaboration likelihood
theories to interpret inconsistencies [Sundaram and Alwar, 2024], while mechanistic approaches leverage influence
graphs and Shapley values to trace the origins of biases in model training [Shaikh et al., 2024].
Main findings.
By administering psychometrics to LLMs, studies consistently find that LLMs exhibit cognitive
biases superficially similar to humans, such as anchoring, framing, and the conjunction fallacy. Large-scale tests,
such as [Echterhoff et al., 2024, Malberg et al., 2024, Xie et al., 2024b], systematically categorize these biases and
enable scalable evaluations. Some note that newer, larger, chain-of-thought-enabled models exhibit improved reasoning
and bias mitigation [Hagendorff et al., 2023, Tang and Kejriwal, 2024], while others argue that increasing model
complexity without deliberate bias mitigation strategies can amplify existing biases [Kumar et al., 2024]. In addition,
researchers explore mechanistic interpretability [Shaikh et al., 2024] and present theoretical explanations from cognitive
psychology and reasoning theories [Hagendorff et al., 2023, Scholten et al., 2024, Yax et al., 2024]. While LLMs
exhibit dual-process reasoning dynamics reminiscent of human cognition [Hagendorff et al., 2023], detailed analysis
reveals differences between LLM and human reasoning [Yax et al., 2024].
4.2.2
Social interactions
Researchers apply psychometric tools from social and developmental psychology to assess LLMs’ capabilities in
navigating social dynamics. Related evaluation focuses on interconnected dimensions such as Theory of Mind (ToM),
Emotional Intelligence (EI), and Social Intelligence (SI).
Theory of Mind (ToM).
ToM is the ability to attribute mental states such as beliefs, intentions, and knowledge to
others [Premack and Woodruff, 1978]. Advanced LLMs can simulate ToM-like reasoning under certain conditions,
16

--- Page 17 ---

Table 4: Representative LLM cognitive constructs in LLM psychometrics.
Aspects
Sub-aspects
Related work
Heuristics
&
biases
-
Abramski et al. [2023], Ando et al. [2023], Bai et al. [2024], Binz and Schulz [2023],
Castello et al. [2024], Chen and Eger [2025], Coda-Forno et al. [2024], Echterhoff et al.
[2024], Hagendorff et al. [2023], Hayes et al. [2024], Healey et al. [2024], Kumar et al.
[2024], Macmillan-Scott and Musolesi [2024], Malberg et al. [2024], Momennejad
et al. [2023], Ranaldi and Zanzotto [2024], Saeedi et al. [2025], Scholten et al. [2024],
Schulze Buschoff et al. [2025], Shah et al. [2024], Shaikh et al. [2024], Sundaram and
Alwar [2024], Talboy and Fuller [2023], Tang and Kejriwal [2024], Thorstad [2023],
Xie et al. [2024a,b], Yax et al. [2024]
Social
interactions
Theory
of Mind
Ma et al. [2023], Mao et al. [2024b], Sarıta¸s et al. [2025] (reviews); Amirizaniani
et al. [2024], Chan et al. [2024], Chen et al. [2024c,d], Gandhi et al. [2023], He et al.
[2023], Holterman and Deemter [2023], Hou et al. [2024], Jamali et al. [2023], Jin et al.
[2024a], Jones et al. [2024], Kim et al. [2025a], Kosinski [2023a,b], Leer et al. [2023],
Li et al. [2023b], Lin et al. [2024], Lorè et al. [2024], Moghaddam and Honey [2023],
Nickel et al. [2024], Pi et al. [2024], Riemer et al. [2025], Sadhu et al. [2024], Sap et al.
[2022], Sarangi et al. [2025], Sclar et al. [2023, 2024], Shapira et al. [2023a], Shinoda
et al. [2025], Soubki et al. [2024], Strachan et al. [2024a,b], Street et al. [2024], Tan
et al. [2024], Tang and Belle [2024], Ullman [2023], van Duijn et al. [2023], Wilf et al.
[2023], Xu et al. [2024a, 2025a], Yang et al. [2025a], Yu et al. [2025], Zhang et al.
[2025], Zhou et al. [2023a], Zhu et al. [2024c].
Emotional
Intelligence
Raj [2024], Sorin et al. [2024] (reviews); Chen et al. [2024b], Elyoseph et al. [2023],
Hu et al. [2025], Huang et al. [2023b, 2024b], Lee et al. [2024f], Li et al. [2023a,
2024e], Paech [2023], Patel and Fan [2023], Sabour et al. [2024], Schaaff et al. [2023],
Vzorinab et al. [2024], Wang et al. [2023b], Welivita and Pu [2024], Zhao et al. [2024]
Social
Intelligence
Guo et al. [2023a], Kovaˇc et al. [2021, 2024], Leng and Yuan [2023], Liang et al.
[2024], Liu et al. [2024c], Mathur et al. [2024], Mittelstädt et al. [2024], Mou et al.
[2024], Schoenegger et al. [2025], Shapira et al. [2023b], Wang et al. [2024a,d], Xu
et al. [2024b], Zadeh et al. [2019], Zhou et al. [2024b]
Psychology
of language
Language
comprehension
Chang and Bergen [2024] (reviews); Amouyal et al. [2024], Arehalli et al. [2022], Boji´c
et al. [2023], Duan et al. [2024a,b], He et al. [2024], Hong et al. [2023], Hu and Levy
[2023], Hu et al. [2023], Huff and Ulakçi [2024], Ide et al. [2024], Lee et al. [2024b,b],
Li et al. [2024a], Qiu et al. [2024], Ruis et al. [2023], Seals and Shalin [2023], Steuer
et al. [2023], Sun and Wang [2024], Tian et al. [2024], Wang et al. [2024b], Wilcox
et al. [2021], Zhou et al. [2023b]
Language
generation
Bellemare-Pepin et al. [2024], Boussioux et al. [2024], Cai et al. [2024], Chakrabarty
et al. [2024], Hubert et al. [2023], Lee and Chung [2024], Miaschi et al. [2024], Orwig
et al. [2024], Seals and Shalin [2023], Stevenson et al. [2022], Tang and Kejriwal
[2024], Tian et al. [2024]
Language
acquisition
Frank [2023b], Riva et al. [2024], Shah et al. [2024], Steuer et al. [2023]
Learning and
cognitive
capabilities
-
Niu et al. [2024] (reviews); Coda-Forno et al. [2024], Dayan et al. [2024], Galatzer-
Levy et al. [2024], Lv et al. [2024], Sartori and Orrú [2023], Song et al. [2024a], Wang
et al. [2024e,e], Webb et al. [2022], Wu et al. [2025], Zeng et al. [2024c], Zhang et al.
[2023b]
which prompts questions about how these behaviors arise and how robustly they generalize. Foundational studies apply
classic psychometrics—false belief tasks—to evaluate ToM in LLMs. [Kosinski, 2023a,b] report that GPT-3.5 and
GPT-4 perform at levels matching or exceeding those of children in structured ToM tasks, suggesting the spontaneous
emergence of ToM-like behavior as models scale in size. Through mechanistic interpretation, Jamali et al. [2023] offer
evidence of parallels between the LLM embeddings and neurons in the human brain.
However, these claims have been challenged. Holterman and Deemter [2023], Shapira et al. [2023a], Ullman [2023]
show that minor task changes often cause LLMs’ performance to drop, suggesting reliance on brittle heuristics rather
than true semantic understanding. To address this, researchers have developed more robust benchmarks and evaluation
protocols featuring procedurally generated, higher-order, or broader ToM tasks [Chen et al., 2024d, Gandhi et al., 2023,
17

--- Page 18 ---

He et al., 2023, Shinoda et al., 2025, Xu et al., 2024a]. These benchmarks frequently reveal significant declines in
performance on complex tasks, such as 6th-order belief attribution [Street et al., 2024] or faux pas detection [Strachan
et al., 2024a].
Some argue these failures stem from a lack of general commonsense reasoning rather than an inability to represent
mental states [Pi et al., 2024]. Riemer et al. [2025] further suggest distinguishing between literal and functional ToM,
noting that current benchmarks inadequately assess functional ToM. While newer models continue to improve on
structured ToM tasks [Strachan et al., 2024a, Street et al., 2024], they remain inconsistent in open-ended, adversarial,
or pragmatic reasoning scenarios [Nickel et al., 2024, Sclar et al., 2024, Yu et al., 2025]. Comparisons with human
baselines show that LLMs can approximate ToM behavior in narrow contexts but still fall short of general human-like
social cognition [Jones et al., 2024, Strachan et al., 2024a, van Duijn et al., 2023]. Recent work has also extended
ToM evaluation to multimodal settings [Chen et al., 2024c, Jin et al., 2024a, Strachan et al., 2024b] and multi-agent
interactions [Li et al., 2023b].
Main findings in ToM.
LLMs exhibit psychometrically measurable ToM-like reasoning, especially when appropri-
ately prompted or structured, but current evidence suggests these capabilities depend on surface-level linguistic cues
and lack robustness. The proficiency of LLMs in ToM remains a contentious issue. Interested readers are referred to
recent comprehensive reviews on ToM in LLMs [Ma et al., 2023, Mao et al., 2024b, Sarıta¸s et al., 2025].
Emotional Intelligence (EI).
EI is the subset of social intelligence that involves the ability to monitor one’s own
and others’ feelings and emotions, to discriminate among them and to use this information to guide one’s thinking and
actions [Salovey and Mayer, 1990].
Recent work introduces benchmarks to assess EI in LLMs using structured, theory-driven tasks. Tools like EmoBench
[Sabour et al., 2024] and EQ-Bench [Paech, 2023] operationalize constructs such as emotional understanding and
regulation, often referencing frameworks like Mayer-Salovey-Caruso Emotional Intelligence Test. Other studies adapt
established psychometric instruments, including Situational Evaluation of Complex Emotional Understanding (SECEU)
[Wang et al., 2023b], the Levels of Emotional Awareness Scale (LEAS) [Elyoseph et al., 2023], the Toronto Alexithymia
Scale (TAS-20) and Empathy Quotient (EQ-60) [Patel and Fan, 2023], among others [Huang et al., 2024b]. Advanced
models like GPT-4 often match or surpass human baselines in emotional awareness and understanding [Elyoseph et al.,
2023, Patel and Fan, 2023, Wang et al., 2023b], though they lack deep reflexive analysis of emotional experience and
motivation [Vzorinab et al., 2024]. Recent benchmarks also extend EI evaluation to multimodal settings [Hu et al.,
2025].
Main findings in EI.
Advanced LLMs generally perform on par with or better than humans in tasks of EI [Elyoseph
et al., 2023, Patel and Fan, 2023], despite evident limitations in several areas, such as displaying artificial or mechanical
patterns when expressing empathy [Lee et al., 2024f], the deep reflexive analysis of emotional experiences [Vzorinab
et al., 2024], and the misalignment with human emotional behaviors [Huang et al., 2023b].
Social Intelligence (SI).
SI is the ability to understand and manage people [Thorndike and Stein, 1937]. SI in LLMs
determines how well these models interpret and respond to social situations. Psychometric tools applied to LLMs yield
mixed results. Mittelstädt et al. [2024] use Situational Judgment Tests (SJTs) and find some LLMs outperform humans
in expert-rated social appropriateness. However, LLMs still struggle with implicit social understanding: Shapira et al.
[2023b] show LLMs perform poorly on faux pas tests, and Xu et al. [2024b] find superficial friendliness often leads to
errors in the Situational Evaluation of SI (SESI). The AgentSense benchmark further highlights LLMs’ limitations in
complex social interactions, especially regarding high-level needs and private information [Mou et al., 2024].
Recent work expands to multi-agent environments. SOTOPIA [Zhou et al., 2024b] and SOTOPIA-π [Wang et al.,
2024d] simulate cooperative and competitive social contexts, while the STSS benchmark [Wang et al., 2024a] evaluates
SI through task-oriented simulations focused on outcomes and goals. The CogMir framework [Liu et al., 2024c]
finds LLMs and humans are similarly consistent in irrational and prosocial decisions under uncertainty. DeSIQ [Guo
et al., 2023a] extends SI evaluation to multimodal settings. Critically, Kovaˇc et al. [2024] argue current benchmarks
lack developmental grounding and propose the SocialAI school as a more comprehensive framework for studying
LLM-based SI.
Main findings in SI.
LLMs show measurable competence in rule-based, socially appropriate behavior, particularly
in structured environments. They perform well on: 1) following predefined social norms [Mittelstädt et al., 2024]; 2)
completing interactional goals in multi-agent settings [Wang et al., 2024d, Zhou et al., 2024b]; 3) replicating human-like
prosocial decisions [Liu et al., 2024c]; and 4) being persuasive, even better than human persuaders [Schoenegger
et al., 2025]. Weaker performance is noted in tasks where superficial friendliness causes errors [Xu et al., 2024b],
18

--- Page 19 ---

understanding high-level growth needs is essential [Mou et al., 2024], and LLMs must implicitly describe social
situations [Shapira et al., 2023b].
4.2.3
Psychology of language
Psycholinguistics, a subfield of psychology, explores how humans comprehend, generate, and acquire language [Carroll,
1986]. Insights from this discipline help evaluate how LLMs process language and mirror human linguistic features.
Language comprehension.
LLM language comprehension is evaluated across multiple linguistic levels—sound,
word, syntax, meaning, and discourse. Duan et al. [2024a] introduce a benchmark of 10 psycholinguistic tests to assess
these comprehensively. Many studies focus on specific aspects, such as syntactic and semantic processing [Arehalli
et al., 2022, Wang et al., 2024b, Wilcox et al., 2021, Wolfman et al., 2024]. Surprisal, a measure of word predictability,
is widely used to model processing difficulty in syntactic ambiguities and hierarchical structures [Arehalli et al., 2022,
Li et al., 2024a, Wilcox et al., 2021]. Results are mixed: for example, GPT-2-XL shows human-like competence
in sound-gender association and implicit causality, but not in sound-shape association [Duan et al., 2024b]. Other
evaluation tasks include grammaticality judgment [Ide et al., 2024, Qiu et al., 2024], pragmatic inference [Boji´c et al.,
2023, Hu et al., 2023, Ruis et al., 2023], argument role processing [Lee et al., 2024b], and discourse comprehension
[Duan et al., 2024a]. Advanced models like GPT-4 often match or surpass humans in pragmatic reasoning [Boji´c et al.,
2023] and grammaticality judgment [Dentella et al., 2024], though performance varies with prompt format [Hu and
Levy, 2023] and implicature understanding remains limited [Ruis et al., 2023].
Language generation.
A rich line of research evaluates the creativity of LLM language generation [Bellemare-Pepin
et al., 2024, Boussioux et al., 2024, Chakrabarty et al., 2024, Hubert et al., 2023, Lee and Chung, 2024, Orwig et al.,
2024, Stevenson et al., 2022, Tang and Kejriwal, 2024], using tests like Guilford’s Alternative Uses Test (AUT) [Guilford
et al., 1978] and the Torrance Test of Creative Thinking (TTCT) [Torrance, 1966]. Early models such as GPT-3 lack
originality and novelty, while advanced LLMs like GPT-4 surpass the human average in creativity. Notably, Tang and
Kejriwal [2024] find LLMs underperform in divergent creativity (e.g., novel uses for familiar objects) but can rival
humans in open-ended creative writing. Cai et al. [2024] show that ChatGPT produces human-like responses in most
of 12 psycholinguistic tests, but AI-generated analogies often lack human-like linguistic properties [Seals and Shalin,
2023]. LLM-generated stories tend to be positive and lack suspense or narrative diversity compared to human writing
[Tian et al., 2024]. Linguistic profiling has also been used to characterize the task-specific language abilities of LLMs
[Miaschi et al., 2024].
Language acquisition.
Work on developmental plausibility examines whether LLMs replicate stages of language
learning analogous to those in children [Shah et al., 2024, Steuer et al., 2023]. It is shown that regardless of model
size, the developmental trajectories of pretrained language models consistently exhibit a window of maximal alignment
with human cognitive development [Shah et al., 2024]. Another study by Frank [2023b] draws inspiration from human
language development to explain the data inefficiency of LLMs; the relative efficiency of human language acquisition is
possibly due to pre-existing conceptual knowledge, multimodal grounding, and the interactive, social nature of their
input.
Main findings.
Early foundations that evaluate language models based on BERT and LSTM link computational
linguistics and psycholinguistic mechanisms [Arehalli and Linzen, 2020, Ettinger, 2020, Futrell et al., 2019]; these
models generally fall short in diverse psycholinguistic tasks. Recent studies extend evaluations to LLMs and broader
tasks [Duan et al., 2024a], where advanced LLMs are shown to surpass humans on tasks such as pragmatic reasoning
[Boji´c et al., 2023] and creative writing [Tang and Kejriwal, 2024]. Some deficiencies still exist, such as limited
implicature understanding [Ruis et al., 2023], prompt-sensitive linguistic competence [Hu and Levy, 2023], and lack
of human-like psycholinguistic properties [Seals and Shalin, 2023, Tian et al., 2024]. In addition, mixed results are
found in the alignment between LLMs and human linguistic cognition [Duan et al., 2024b, Wolfman et al., 2024] and
language acquisition [Frank, 2023b, Shah et al., 2024].
4.2.4
Learning and cognitive capabilities
Psychometrics of learning and cognitive capabilities measures mental functions such as memory, reasoning, problem-
solving, and comprehension to identify cognitive strengths and weaknesses. Recent studies adapt human psychometric
tools to evaluate LLMs’ cognitive abilities. For example, Galatzer-Levy et al. [2024] use the Wechsler Adult Intelligence
Scale (WAIS-IV) to show LLMs generally reach top human levels in verbal comprehension and working memory,
though multimodal models lag in visual reasoning. Raven’s Progressive Matrices and other fluid intelligence tests reveal
LLMs can match or surpass humans in analogical reasoning [Sartori and Orrú, 2023, Webb et al., 2022].
19

--- Page 20 ---

Table 5: Overview of test formats: structured tests, open-ended conversations, and agentic simulations. For each format,
representative examples are provided for each construct.
Construct
Structured tests
Open-ended conversations
Agentic simulations
Personality
traits
Jiang et al. [2023], Serapio-
García et al. [2023]
Jiang et al. [2024b], Zheng
et al. [2025]
Frisch and Giulianelli [2024],
Huang et al. [2024c]
Values
Kovaˇc et al. [2023], Zhong
et al. [2024]
Ren et al. [2024], Yao et al.
[2025b]
Chiu et al. [2025], Shen et al.
[2024]
Morality
Abdulhai et al. [2024], Ji
et al. [2024]
Neuman
et
al.
[2025],
Sachdeva and van Nuenen
[2025]
Chiu et al. [2025], Nunes
et al. [2024]
Attitudes
& opinions
Argyle
et
al.
[2023],
Bernardelle et al. [2024]
Röttger et al. [2024], Wright
et al. [2024]
-
Heuristics and
biases
Hagendorff et al. [2023], Yax
et al. [2024]
Healey et al. [2024], Wen
et al. [2024a]
Bai et al. [2024], Xie et al.
[2024b]
Social
interaction
Mittelstädt et al. [2024],
Sabour et al. [2024]
Elyoseph et al. [2023], We-
livita and Pu [2024]
Wang et al. [2024d], Zhou
et al. [2024b]
Psychology of
language
Amouyal et al. [2024], Duan
et al. [2024a]
-
-
Learning and
cognitive
capabilities
Coda-Forno et al. [2024], Wu
et al. [2025]
Galatzer-Levy et al. [2024]
Lv et al. [2024]
However, limitations persist. The Montreal Cognitive Assessment (MoCA) shows most LLMs display mild cognitive
impairment, especially in visuospatial and executive tasks [Dayan et al., 2024]. Abstraction and Reasoning Challenge
(ARC) further highlights deficits in abstract problem-solving [Wu et al., 2025]. Some works question the validity of
current tests [Li et al., 2024d, Löhn et al., 2024, Zhang et al., 2023b], prompting new benchmarks and methodologies
[Coda-Forno et al., 2024, Song et al., 2024a, Wang et al., 2024e, Zeng et al., 2024c, Zhuang et al., 2023a].
Developmental perspectives also emerge: Wang et al. [2024e] leverage Piaget’s Theory of Cognitive Development to
track human-like progression in LLMs, finding advanced models (e.g., GPT-4) reach cognitive abilities comparable to
20-year-old humans. Shah et al. [2024] identify developmental profiles in LLMs paralleling human development via
psychometric theories like Cattell-Horn-Carroll.
Main findings.
LLMs demonstrate strong performance on verbal comprehension, working memory, and analogical
reasoning, often reaching or surpassing high human percentiles when evaluated with adapted psychometric tools like
WAIS-IV and Raven’s Matrices [Galatzer-Levy et al., 2024, Webb et al., 2022]. However, they exhibit notable cognitive
deficits, particularly on benchmarks like MoCA and ARC tasks [Dayan et al., 2024, Wu et al., 2025]. Several works
introduce developmental and cognitive benchmarks (e.g., CogLM, CogBench) grounded in psychological theories to
track reasoning and adaptability [Coda-Forno et al., 2024, Wang et al., 2024e]. While emergent reasoning appears at
scale, challenges remain in interpretability, test validity, and generalization beyond surface-level statistical patterns [Li
et al., 2024d, Löhn et al., 2024].
5
Psychometric evaluation methodology
This section examines the methodologies employed in LLM Psychometrics. As illustrated in Fig. 3, the methodological
framework encompasses four key components: test formats (§ 5.1), data and task sources (§ 5.2), prompting strategies
(§ 5.3), and model output and scoring (§ 5.4). The configuration of inference parameters (§ 5.5) is additionally discussed.
5.1
Test format
Test formats of LLM psychometric evaluation can be categorized into structured tests, open-ended conversations, and
agentic simulations. Table 5 collects exemplary works illustrating the test formats used for each construct.
20

--- Page 21 ---

Data and Task Sources
Custom-curated items
Prompting Strategies
Role-playing prompts
Prompt perturbation
Original prompt
Variant 1
Variant 2 Variant 3
Performance-enhancing
prompts
Step1
Step2
Step3
Model Output and Scoring
Test Format
Structured test
Agentic simulation
Healthcare
Public sector Education
Open-ended 
conversation
Free-form
Q &A
Closed-ended output
Logit-based analysis
Direct scoring
The man who hunts 
ducks out on weekends _
❌: and
My answer is _.
Likert-scale
VSM13
DIT
Open-ended output
Human scoring
Model-based scoring
Psychometric
Evaluation
Methodology
Test Format
Prompting
Output & Score
Data
Item: I see myself as 
someone who is 
outgoing, sociable.
1: Strongly agree
2: Agree
3: Neutral
4: Disagree
Item: Which of the following do you consider the 
most important for a good society?
A. Maintaining economic growth
B. Ensuring strong defense and security
C. Protecting freedom of speech and 
individual liberties
D. Reducing inequality and fostering 
social justice
Long text 
generation
Multi-turn
dialogue
Established inventories
CRT
MFT
SVS
MBTI
Synthetic items
You desire being
free to act independently.
Please think step by step.
✅: loves
❌: quickly
Model response
Model response
Rule-based scoring
Model response
Figure 3: Overview of LLM psychometric evaluation methodologies.
5.1.1
Structured tests
Structured tests feature predefined instructions, questions, and response formats. These items may include alternative-
choice questions, multiple-choice questions, rating scales, and short-answer questions. When adapting structured
psychometric tests for LLMs, it is common practice to retain the original items and simply reformat them as prompts.
For example, personality and values are often measured with Likert scales (e.g., BFI statements like “I see myself
as someone who is outgoing, sociable”), while morality is assessed using tools like the DIT or MFQ, which require
decisions and agreement ratings. Heuristics and biases are often tested with scenario-based choices. Social interaction
and psycholinguistic abilities are evaluated with multiple-choice, forced-choice, or masked word prediction. Cognitive
tests also involve short-answer questions (e.g., WAIS-IV Digit Span).
Structured psychometric tests are advantageous due to their scalability, objectivity, and automated scoring. However,
critical perspectives underline their limitations, such as gaps in real-world applicability; biases; data contamination; and
issues with reliability, validity, and depth of insights.
21

--- Page 22 ---

Table 6: Overview of data and task sources: established inventories, custom-curated items, and synthetic items. For
each data source, representative examples are provided for each construct.
Construct
Established inventories
Custom-curated items
Synthetic items
Personality
traits
Barua et al. [2024], Serapio-
García et al. [2023]
Ai et al. [2024], Jiang et al.
[2023]
Zeng [2024]
Values
Fischer et al. [2023], Miotto
et al. [2022]
Meadows et al. [2024], Shen
et al. [2024]
Moore et al. [2024], Ye et al.
[2025a]
Morality
Abdulhai et al. [2024], Khan-
delwal et al. [2024]
Hendrycks et al. [2021], Jin
et al. [2022]
Liu et al. [2024d], Scherrer
et al. [2023]
Attitudes
& opinions
Argyle
et
al.
[2023],
Bernardelle et al. [2024]
Ceron et al. [2024], Durmus
et al. [2023]
Wan and Chang [2024]
Heuristics and
biases
Binz and Schulz [2023], Ha-
gendorff et al. [2023]
Ando et al. [2023], Momen-
nejad et al. [2023]
Malberg et al. [2024], Xie
et al. [2024b]
Social
interaction
[Chen et al., 2024d, Ullman,
2023]
Shapira et al. [2023a], Street
et al. [2024]
Gandhi et al. [2023]
Psychology of
language
Cai et al. [2024], Duan et al.
[2024a]
He et al. [2024], Pérez-
Mayos et al. [2021]
-
Learning and
cognitive
capabilities
Coda-Forno et al. [2024],
Dayan et al. [2024]
Song et al. [2024a], Wu et al.
[2025]
-
5.1.2
Unstructured tests
Unstructured tests probe LLMs’ personalities and abilities by analyzing their free-form responses, usually with rationale
and justification, to user queries, or by contextualizing LLMs to observe their decision-making in real-world scenarios.
Open-ended conversations.
Unstructured testing often engages LLMs in open-ended, typically single-turn conversa-
tions that elicit specific constructs, mirroring real-world human-LLM interactions. For example, Jiang et al. [2024b]
have LLMs generate long-form narratives to reveal personality traits. ValueBench uses advice-seeking queries to assess
LLMs’ influence on users’ values [Ren et al., 2024], while Sachdeva and van Nuenen [2025] present moral dilemmas
from Reddit, prompting LLMs to provide community-style moral judgments. To probe political attitudes, Röttger
et al. [2024] convert PCT multiple-choice items into forced-choice and open-ended formats. For cognitive constructs,
Healey et al. [2024] design pipelines to detect nuanced biases in free responses, and Welivita and Pu [2024] evaluate
empathy by asking LLMs to respond to emotional scenarios. Many cognitive tests, such as WAIS-IV vocabulary and
comprehension, also use open-ended questions [Galatzer-Levy et al., 2024].
Agentic simulations.
Advanced unstructured tests evaluate LLMs as agents in complex, contextualized role-playing
scenarios, analyzing their decision-making in dynamic environments. Huang et al. [2024c] design LLM-Agents with
distinct personalities and analyze them by replicating human-like behaviors in agentic simulations. Shen et al. [2024]
measure values using four real-world vignettes: collaborative writing, education, public sectors, and healthcare. Chiu
et al. [2025] present value and moral dilemmas to LLMs, examining their decisions and rationales. Cognitive construct
tests are often more complex, extending to multi-agent settings; for example, Bai et al. [2024], Xie et al. [2024b] identify
cognitive biases in multi-agent communication. SOTOPIA simulates open-ended social interactions among LLM agents
to evaluate social intelligence [Wang et al., 2024d, Zhou et al., 2024b]. Lv et al. [2024] benchmark cognitive dynamics
by having LLMs repeatedly complete cognitive questionnaires and reason over information flows.
Unstructured tests assess LLMs in free-form, contextualized scenarios, offering greater ecological validity and revealing
complex behaviors—such as nuanced reasoning, subtle biases, and dynamic social interactions—not captured by
structured formats. However, they pose challenges in standardization, scoring, and reproducibility.
22

--- Page 23 ---

5.2
Data and task sources
Data and task sources LLM Psychometrics can be 1) drawn from established psychometric inventories, 2) human-
authored and custom-curated, and 3) synthesized by AI models. Table 6 provides an overview of the data and task
sources for each construct.
Established inventories.
Established psychometric inventories offer standardized, well-validated tools for LLM
evaluation. Common examples include BFI and HEXACO for personality [Barua et al., 2024, Serapio-García et al.,
2023]; SVS, PVQ, WVS, and VSM for values [Fischer et al., 2023, Miotto et al., 2022]; MFT and DIT for morality
[Abdulhai et al., 2024, Khandelwal et al., 2024]; ANES and PCT for political attitudes [Argyle et al., 2023, Bernardelle
et al., 2024]; CRT for heuristics and biases [Binz and Schulz, 2023, Hagendorff et al., 2023]; and False-Belief Tasks for
ToM [Chen et al., 2024d, Ullman, 2023]. While these inventories enable straightforward, standardized assessment, their
use with LLMs raises concerns about data contamination, response bias, and limited ecological validity for complex AI
tasks [Ye et al., 2025a].
Custom-curated items.
Human-authored, custom-curated items offer tailored psychometric tests that are often more
relevant to LLMs, enabling exploration of novel capability dimensions. For example, Shen et al. [2024] find SVS and
PVQ insufficient for LLM value alignment, so they create 11 AI-informed value statements based on a systematic review
of alignment literature. Ceron et al. [2024] highlight the unreliability of standard political questionnaires for LLMs and
introduce tests using annotated voting-advice questionnaires from seven EU countries to assess stance consistency. For
morality, Hendrycks et al. [2021] curate a dataset of over 130,000 open-world scenarios requiring moral judgments. In
ToM, Soubki et al. [2024] develop a dataset from real spoken dialogues to address gaps between synthetic benchmarks
and human behavior. While custom-curated items offer high ecological validity, their development and validation are
labor-intensive, limiting scalability and diversity.
Synthetic items.
Synthetic items—generated primarily by LLMs—are an emerging approach in LLM Psychometrics,
enabling large-scale, diverse, and contextually rich test content. This method requires careful prompt engineering
and validation. Some studies adapt established inventories to improve ecological validity, reduce data contamination,
and enhance scalability. For instance, Ren et al. [2024] convert self-report items into advice-seeking queries to better
reflect real-world human-AI interactions. Bhandari et al. [2025b] rewrite established items into semantically equivalent
forms, validating them via semantic embedding similarity thresholds. Zhu et al. [2024a] diversify cognitive test items to
enable more comprehensive analysis of LLM cognitive abilities. Other work generates synthetic tests entirely from
scratch. Hadar-Shoval et al. [2025] demonstrate that LLM-generated cognitive tests correlate strongly with human
performance on established tests. Ye et al. [2025a] create value-eliciting prompts and confirm the reliability and validity
of the resulting measurements. Jiang et al. [2024a] introduce generative evolving testing, where an LLM-based Item
Generator produces items of specified difficulty. Chiu et al. [2025] use GPT-4 to generate moral dilemmas for evaluating
LLM moral judgment. For social intelligence, agentic simulations prompt LLMs to generate components of social
interactions [Mou et al., 2024, Zhou et al., 2024b].
5.3
Prompting strategies
Many structured tests employ standard test prompts, reformatted from those used for human participants. Others involve
various prompting strategies.
Role-playing prompts.
Role-playing prompts (persona or profiling prompts) embed demographic or personal
attributes into the LLM context during testing. These prompts enable the generation of multiple simulated participants
from a single LLM for statistical analysis. For example, Serapio-García et al. [2023] prepend persona instructions to
each item to elicit diverse responses, allowing examining reliability and validity within one LLM. Similarly, Ye et al.
[2025b] use value-anchoring prompts to create hundreds of LLM-based participants for value measurement, supporting
the development of an LLM-specific value system. LLMs can represent a superposition of personalities, values, and
perspectives [Kovaˇc et al., 2023], prompting research into their adaptability. Role-playing prompts show that LLMs
can shift between personality types, though steerability varies by model and dimension [Jiang et al., 2023, La Cava
and Tagarelli, 2024, Li et al., 2024d, Lu et al., 2023]. Such prompts are also used to test the stability of LLM values
[Kovaˇc et al., 2024, Rozen et al., 2024] and to measure how well LLMs can mimic moral or political profiles and their
susceptibility to related biases [Münker, 2024, Simmons, 2023, Wright et al., 2024]. Cognitive benchmarks, especially
for social interactions, often use persona prompts in agentic simulations [Huang et al., 2023b, Mou et al., 2024, Zhou
et al., 2024b], with task performance depending on the LLM’s ability to embody these roles. These prompts influence
social-cognitive reasoning when controlling for other variables [Tan et al., 2024]. While role-playing capabilities enable
23

--- Page 24 ---

diverse perspectives useful for social simulations, they can also lead to unstable values and perspectives, potentially
compromising test validity and complicating value alignment.
Performance-enhancing prompts.
Performance-enhancing prompts are crafted to augment LLMs in psychometric
evaluations, as recommended by Hagendorff [2023]. Chain of Thought (CoT) prompting [Wei et al., 2022] reduces
biases [Hagendorff et al., 2023], enhances social intelligence [Shapira et al., 2023a], and improves cognitive capabilities
[Coda-Forno et al., 2024]. Its variant Emotional CoT [Li et al., 2024e] boosts EI, while emotional prompts [Li
et al., 2023a] enhance general cognitive abilities through emotional stimuli. Few-shot prompting [Brown et al., 2020]
has demonstrated improvements in ToM performance [Moghaddam and Honey, 2023]. Research has also developed
construct-specific prompting strategies. Zhou et al. [2024a] propose MFT-guided reasoning prompts for moral alignment,
while Echterhoff et al. [2024], Sumita et al. [2024] focus on self-debiasing approaches. ToM-specific enhancements
include SymbolicToM [Sclar et al., 2023] and temporal decomposition-based prompting [Hou et al., 2024, Sarangi
et al., 2025]. Additionally, Zhao et al. [2025a] develop a framework using self-reflection prompts to examine both
explicit and implicit social biases, where explicit bias measurement reflects implicit bias.
Prompt perturbation and adversarial attacks.
Prompt perturbations can test the robustness of LLMs’ personality
traits and cognitive abilities. Researchers have investigated whether LLMs can maintain stable personality, values,
opinions, and cognitive abilities when item options are reordered [Lee et al., 2024d, Schelb et al., 2025], prompts
are rephrased [Fraser et al., 2022, Lee et al., 2024d, Strachan et al., 2024a], prompt formats are altered [Moore et al.,
2024, Schelb et al., 2025], or different languages are used [Cahyawijaya et al., 2024, Moore et al., 2024]. For instance,
Faulborn et al. [2025] introduce 30 variations of prompts to evaluate the political biases of LLMs. In addition, Wen
et al. [2024a] propose psychometric-inspired adversarial attacks to uncover implicit biases in LLMs. Similarly, Li
et al. [2024d] utilize persuasive adversarial prompts (PAP) [Zeng et al., 2024a] to test the robustness of LLMs’ values.
Since LLMs are sensitive to these perturbations, researchers have begun to scrutinize the reliability of the test results
obtained under standard conditions [Dominguez-Olmedo et al., 2024, Röttger et al., 2024, Strachan et al., 2024a, Ye
et al., 2025a].
5.4
Model output and scoring
5.4.1
Closed-ended output and scoring
LLM performance on structured tests is typically evaluated using logit-based probabilistic analysis and closed-ended
output scoring. In multiple-choice or Likert-scale settings, some studies analyze token-level logits—especially the first
token—to infer latent traits, detect response entropy, or compare LLM output distributions against human data [Arehalli
et al., 2022, Dominguez-Olmedo et al., 2024, Pellert et al., 2024, Santurkar et al., 2023]. Psycholinguistic tests often
use logit-based metrics such as surprisal (the negative log probability of a token), which quantifies predictability and
cognitive effort, allowing researchers to align LLM uncertainty patterns with those of humans [Steuer et al., 2023, Wang
et al., 2024b].
Conversely, closed-ended outputs, which are explicit numerical scores or categorical selections, can be analyzed
using predefined scoring protocols. For Likert-scale responses, scores are typically averaged or aggregated based on
established rubrics (e.g., VSM13 [Ye et al., 2025a] and DIT [Khandelwal et al., 2024]). In standardized cognitive tests,
model outputs are evaluated against ground-truth labels (e.g., accuracy in arithmetic tasks) or rule-based criteria (e.g.,
established standards in the Verbal Comprehension Index) [Galatzer-Levy et al., 2024].
5.4.2
Open-ended output and scoring
Scoring open-ended outputs is more complex and typically falls into three categories: 1) rule-based, 2) model-based,
and 3) human scoring.
Rule-based scoring.
Rule-based scoring predominantly relies on the lexical hypothesis [Allport and Odbert, 1936],
analyzing the presence and frequency of specific keywords or phrases. For example, Jiang et al. [2024b] apply LIWC
(Linguistic Inquiry and Word Count) features [Pennebaker et al., 2001] to evaluate LLM personalities, and Fischer
et al. [2023] employ a theory-driven value dictionary [Ponizovskiy et al., 2020] for value measurement. However, such
lexicon-based approaches struggle to capture semantic nuance [Ye et al., 2025a]. Some rule-based methods go beyond
keyword matching; for instance, Healey et al. [2024] detect bias by checking for deviations from equivalent treatment
in responses.
Model-based scoring.
Model-based scoring is prevalent in unstructured testing for its flexibility and scalability. Many
studies train models to evaluate LLM responses, such as fine-tuning BERT variants on the MyPersonality dataset for
24

--- Page 25 ---

personality scoring [Hilliard et al., 2024]. Others fine-tune LLMs with psychometric inventories or human annotations
to classify value valence [Sorensen et al., 2024a, Yao et al., 2024, 2025b, Ye et al., 2025a]. Scoring can be conducted at
the item level (e.g., Generative Psychometrics: item parsing, scoring, aggregation [Ye et al., 2025a]) or at the response
level, evaluating the entire output [Yao et al., 2024, 2025b]. Some models are tailored to specific frameworks (e.g.,
Schwartz’s Value Theory [Yao et al., 2024]), while others are trained to be generalists by leveraging broader fine-tuning
data and LLM prior knowledge [Ye et al., 2025a]. Model-based evaluators are especially common for personality and
value assessment, where textual cues map readily to target dimensions. Many studies now use the LLM-as-a-judge
approach [Gu et al., 2024] for scoring open-ended responses. For instance, Li et al. [2024d], Zheng et al. [2025] prompt
LLMs to rate responses on personality, ToM, and motivation, validating consistency with other LLMs or human raters.
This method is especially useful in unstructured simulation settings, such as SI measurement across goal completion,
relationship maintenance, and social rule adherence [Mou et al., 2024, Wang et al., 2024a,d, Zhou et al., 2024b].
Embedding models are also used to measure similarity between LLM outputs and prototypical examples [Amirizaniani
et al., 2024, Cahyawijaya et al., 2024, Huang et al., 2024c].
Human scoring.
Human scoring is employed when rigorous evaluation, adhering strictly to standard psychometric
manuals, is necessary. For instance, Elyoseph et al. [2023] engage psychologists to assess the contextual suitability of
LLM responses using the Levels of Emotional Awareness Scale (LEAS). Castello et al. [2024] conduct an examination
of cognitive biases in LLMs through human evaluation and linguistic comparison. Healey et al. [2024] present a
semi-automated pipeline to classify LLM responses into nuanced bias types. Other examples include ToM evaluation in
open-ended responses [Amirizaniani et al., 2024] and cognitive evaluation based on the Montreal Cognitive Assessment
(MoCA) [Dayan et al., 2024].
5.5
Inference parameters
Evaluation and validation depend on LLM inference parameters. Greedy decoding yields deterministic, reproducible
outputs but limits diversity, while sampling-based decoding (adjusting temperature, top-k, top-p) introduces stochasticity
and diversifies responses. Sampling-based decoding may reveal a broader spectrum of latent traits, opinions, or cognitive
strategies, but also introduce variability that complicates psychometric validation. Conversely, deterministic settings
enhance reproducibility but may obscure the model’s full range of capabilities or biases. Most studies report and
control inference settings for fair comparisons, and some analyze sensitivity to these parameters. Transparent reporting
and careful parameter selection are essential; both deterministic and stochastic settings should be considered to fully
understand the implications of test results.
6
Psychometric validation
Unlike AI benchmarking, which focuses on system performance, psychometrics prioritizes theoretical grounding,
standardized protocols, and reproducibility. Psychometric validation ensures that tests are reliable, valid, and fair. As
an emerging field, LLM Psychometrics lacks standardization in test design and administration, and recent work is
beginning to address these issues. We outline the landscape of psychometric validation in Fig. 4.
6.1
Reliability and consistency
Reliability, a core aspect of psychometric validation, measures how consistently a test performs—over time (test-retest),
across versions (parallel forms), and among evaluators (inter-rater). Researchers have adapted these metrics for LLMs.
For example, Li et al. [2024d] propose a benchmark covering five reliability forms: internal consistency, parallel forms,
inter-rater, option position robustness, and adversarial attack robustness. Other studies [Ceron et al., 2024, Huang et al.,
2023a, Shu et al., 2024, Zheng et al., 2025] examine LLM output consistency across repeated trials, prompt variations,
and languages. Notably, some metrics capture both random and systematic errors, so inconsistencies can undermine
both reliability and validity.
Some advanced LLMs show stable Big Five personality trait responses across settings [Huang et al., 2023a], with
larger and instruction-tuned models achieving even higher reliability using role-playing prompts [Serapio-García et al.,
2023]. LLMs also display consistent value orientations across paraphrased, related, and translated questions, as well
as different response formats [Moore et al., 2024]. Strong inter-rater reliability is reported when LLMs act as judges,
though personality stability and value consistency vary by model and cultural context [Li et al., 2024d]. However,
other studies report less favorable results. LLMs are notoriously sensitive to prompt variations: small changes in
prompt form [Ren et al., 2024, Röttger et al., 2024], option order [Dominguez-Olmedo et al., 2024, Li et al., 2024d], or
syntax [Hu and Levy, 2023] can systematically shift outputs, undermining parallel forms reliability. Studies also find
inconsistencies between next-token logits and forced-choice responses in psycholinguistic tests [Hu and Levy, 2023],
25

--- Page 26 ---

Validity
Content validity
Data contamination
Existing scale
Invalid novel items
New scale
Construct validity
Unique internal 
abstractions
LLM
Human
Existing scale
Response set
Arbitrary items
A
B
C
Social desirability 
bias
Cross-lingual tests
Items
Criterion & ecological validity
Criterion validity
Ecological validity
Reliability and Consistency
Test-retest reliability
Parallel forms
reliability
Inter-rater reliability
Standards and Recommendations
Reliability
Fairness
Non-
disclosure
Validity
Suitability
Socially 
desirable
Socially 
undesirable
Consistent results
Avoiding test 
contamination
Matching 
LLM capabilities
Measuring 
intended traits
Inflated performance
Inadequate
representation
Preference for A
External criterion
Real-life situations
•
Valid comparisons
•
Valid translations
•
Transparency
Figure 4: Overview of psychometric validation: reliability and consistency, validity, and standards and recommendations.
and between forced-choice and free-form responses in value [Kovaˇc et al., 2024, Ye et al., 2025a] and political opinion
surveys [Röttger et al., 2024]. In cognitive tests, minor changes to ToM tasks often cause poor performance, indicating
low parallel forms reliability and reliance on fragile heuristics [Holterman and Deemter, 2023, Shapira et al., 2023a,
Ullman, 2023]. The Words and Deeds Consistency Test (WDCT) [Xu et al., 2025b] further shows LLMs’ verbal and
behavioral responses are inconsistent across domains.
Reliability findings are mixed and depend on factors such as construct, reliability type, test format, prompting, and
model. LLMs are generally more reliable in personality assessments [Huang et al., 2023a, Serapio-García et al., 2023]
than in political opinion evaluations [Dominguez-Olmedo et al., 2024, Röttger et al., 2024]. Inter-rater agreement varies
across instruments and domains [Bodroža et al., 2024]. LLMs often show high internal consistency (Cronbach’s alpha
> 0.8) in closed-choice personality tests [Huang et al., 2023a, Serapio-García et al., 2023, Zheng et al., 2025], but low
parallel form reliability due to prompt sensitivity [Gupta et al., 2024, Li et al., 2024d, Shu et al., 2024]. Consistency
improves in structured tests with strong prompt control [Klinkert et al., 2024, Rozen et al., 2024, Serapio-García et al.,
2023], but declines with less standardized prompts [Petrov et al., 2024] or controversial topics [Moore et al., 2024].
Reliability also varies by model: base models are more consistent than fine-tuned ones on value-laden questions [Moore
et al., 2024], and higher model safety correlates with greater value consistency [Ye et al., 2025b]. Advanced models
also perform better in role-playing personality tests, increasing reliability [Serapio-García et al., 2023].
6.2
Validity
Validity assesses whether a test truly measures its intended construct. Recent work in LLM Psychometrics has explored
various facets of validity, highlighting both challenges and emerging solutions.
6.2.1
Content validity
Content validity requires that a test fully represents the intended construct. Key challenges include data contamination
from established tests and insufficiently vetted novel items. Directly applying human tests to LLMs risks contamination,
as LLMs may have seen test items or similar content during training [Hagendorff et al., 2024, Jiang et al., 2024c].
This can inflate performance or bias trait measurement. To mitigate this, researchers reformat tests or generate new
items; see § 5.2. On the other hand, reformatted or newly generated items may inadequately capture the construct or
introduce extraneous factors. This may be due to a less rigorous crowd-sourcing process for benchmark curation, or the
inherent biases and limited capabilities of the AI models used for stimulus synthesis. Evaluating content validity for
custom-curated and model-generated items is crucial but rarely conducted in LLM Psychometrics.
26

--- Page 27 ---

6.2.2
Construct validity
Construct validity determines if a test truly measures its intended construct. Alaa et al. [2025] highlight its critical yet
often lacking role in medical LLM benchmarks. Broader literature suggests that construct validity is challenged by
LLMs’ unique internal abstractions, systematic response patterns, and social desirability bias.
Unique internal abstractions
LLMs and humans may fundamentally differ in their internal representations of
psychological constructs. Kovaˇc et al. [2023] argue that LLMs display contextually adaptive traits, unlike the stable
characteristics seen in humans. Sühr et al. [2023] show that LLM personality types do not align with the clear separation
of Big Five traits found in humans. Similarly, Peereboom et al. [2024] find that human-oriented HEXACO tests
are inapplicable to LLMs, as key personality factors may be absent. For values, Ye et al. [2025a] report that LLM
self-reports do not fit Schwartz’s model, and while open-ended responses improve alignment, it remains an imperfect
fit; Hadar-Shoval et al. [2024] also find LLMs encode values distinct from humans. Overall, researchers agree that
robust LLM psychometric evaluation requires new operational definitions, distinct from or only loosely analogous to
human traits.
In this regard, pioneering research presents value systems tailored to LLMs’ unique internal abstractions [Biedma
et al., 2024, Ye et al., 2025b]. Ye et al. [2025b] introduce a generative psycho-lexical approach based on GPV value
measurement [Ye et al., 2025a], demonstrating through various tasks that their value factors are valid and outperform
Schwartz’s system. The distinct nature of LLM constructs requires rigorously designed tests: Ma et al. [2025] present
the Core Sentiment Inventory (CSI) for measuring LLM emotional tendencies and personality; Fang et al. [2024]
create a psychologically grounded mathematics benchmark to improve validity, model item difficulty, and enable
human comparison; and Lee et al. [2024d] propose the TRAIT test, achieving higher validity and reliability than other
personality measures.
Response set.
Response set refers to systematic answer patterns regardless of item content. Some LLMs show option
position bias, favoring responses labeled "A" in political opinion tests [Dominguez-Olmedo et al., 2024, Li et al.,
2024d]. After correcting for this bias, Dominguez-Olmedo et al. [2024] find LLM responses to political questions are
uniformly random, rendering demographic alignment analyses meaningless. Similar findings are observed in LLM
personality [Song et al., 2023, Sühr et al., 2023] and value tests [Ye et al., 2025a]. Sühr et al. [2023] also note LLMs
often affirm both the original and reverse-coded items, while Ye et al. [2025a] observe some LLMs consistently prefer
low or high ratings. These observations suggest self-report tests may be unsuitable for LLM Psychometrics.
Social desirability bias.
Social desirability bias—the tendency to give socially acceptable rather than genuine
responses—is observed in LLMs as in humans. Salecha et al. [2024] find LLMs skew toward favorable traits in
personality tests, inflating extraversion and lowering neuroticism scores. Similarly, Ye et al. [2025b] show LLMs avoid
reporting less desirable values (e.g., hedonism) in direct self-reports [Biedma et al., 2024], but reveal them in indirect,
contextual prompts. While tuning for social desirability is important, overemphasis risks producing homogeneous
models that lack diverse perspectives and fail to meet varied user needs.
Cross-lingual tests.
Cross-lingual psychometric tests reveal notable inconsistencies in LLM measurement results
across languages [Romero et al., 2024]. Despite multilingual capabilities, LLMs often lack consistent psychological
trait assessments between languages [Cahyawijaya et al., 2024]. These inconsistencies complicate validation, requiring
careful separation of model biases, translation issues, and cultural differences represented by the models.
6.2.3
Criterion and ecological validity
Criterion validity examines how well test results correspond to external standards, while ecological validity concerns
their relevance to real-world scenarios. In LLM Psychometrics, external standards often coincide with real-world
evaluation results. Studies find that value orientations from forced-choice tests frequently diverge from those observed
in human-LLM interactions [Ren et al., 2024, Ye et al., 2025a], with similar gaps in personality [Ai et al., 2024] and
morality [Nunes et al., 2024]. As a result, researchers advocate linking LLM personality to safety [Zhang et al., 2024a],
measuring values within real-world interactions [Ren et al., 2024], and using open-ended dialog to improve construct
validity [Ye et al., 2025a]. Further work connects LLM value measurement to safety prediction and value alignment
tasks to ensure conformity with external standards [Ye et al., 2025b].
6.3
Standards and recommendations
To address key challenges, researchers have proposed standards and recommendations to guide LLM Psychometrics
and establish methodological rigor. Frank [2023a] suggests leveraging developmental psychology to understand LLM
27

--- Page 28 ---

cognition, recommending simplified and novel stimuli to prevent training data contamination. Löhn et al. [2024]
critique current practices and outline seven requirements for valid assessment: reliability, validity, suitability to LLM
capabilities, non-disclosure (to avoid contamination), and fairness—including valid comparisons, translations, and
transparency. Their review of 25 studies reveals these principles are often overlooked.
More recently, Hagendorff et al. [2024] advocate for procedural test generation, multiple task versions, performance-
enhancing prompts, shuffling options, and diverse scoring methods to reduce contamination and improve reliability.
They also recommend deterministic settings for reproducibility, automated evaluation tools, manual review of unreliable
outputs, and statistical analysis of results. Vaugrante et al. [2024] highlight poor replicability in recent work and
offer four main recommendations: (1) ensure benchmark validity, sufficient task coverage, standardization, prompt
control, and alignment with research goals; (2) use standardized methods, avoid cherry-picking, maintain statistical
transparency, document setups, and define consistent metrics; (3) monitor model changes, account for model diversity,
adjust benchmark difficulty as models advance, and document model versions and experiment dates; (4) standardize
scoring and verification, with clear guidelines and rubrics for implementers. Schelb et al. [2025] introduce a framework
for robust, flexible, and reproducible psychometric experiments, centered on standardized configuration files.
7
Psychometrics for LLM enhancement
Psychometric principles not only enable rigorous evaluation but also drive LLM development and improvement. They
underpin three main advancements: trait manipulation for personalized and controlled behaviors, psychometrically-
informed safety and alignment, and cognitive enhancement for more human-like reasoning and communication.
7.1
Trait manipulation
Psychometrics enables targeted manipulation of LLM traits for personalization, role-play, and demographic simulation,
providing a principled framework across prompting, inference, and training.
Structured prompts based on validated psychometric inventories reliably elicit and modulate specific personality traits
in LLMs [He and Zhang, 2024, Huang et al., 2024c], supporting controlled simulation or alignment of synthetic
personas [Jiang et al., 2023, La Cava and Tagarelli, 2024, Serapio-García et al., 2023, Zhang, 2024]. For instance, Jiang
et al. [2023] introduce personality prompting (P 2), where Big Five lexicons are expanded into detailed personality
descriptions, enabling LLMs to adopt diverse behaviors. Chuang et al. [2024] propose a systematic prompting strategy
using empirically-derived human belief networks, aligning LLMs with related beliefs across 64 topics and 9 latent
factors.
Beyond prompt engineering, inference-time interventions manipulate hidden representations during the forward pass,
often guided by patterns recognized using psychometric scales. Methods such as ControlLM [Weng et al., 2024],
Personality Alignment Search [Zhu et al., 2024b], Neuron-based Intervention [Deng et al., 2024], Probing-then-Editing
[Ju et al., 2025], and Latent Feature Steering [Yang et al., 2025b] achieve trait control by shifting activations or neuron
values at inference, without retraining.
Other approaches fine-tune LLMs for trait manipulation. Vu et al. [2024] modify model architectures to enable control
over continuous Big Five and mental health traits. Dan et al. [2024], Jain et al. [2024], Li et al. [2024c] deploy LoRA
modules or routing networks linked to personality traits, training specialist adapters for trait-driven generation. Cui
et al. [2023], Liu et al. [2024a], Zeng et al. [2024b] embed traits by training on large, annotated dialogue datasets from
validated psychometric tools. Some methods directly edit model parameters without retraining; for example, Hwang
et al. [2025] use MBTI-based adjustment queries to edit model parameters and steer target personality traits.
Trait manipulation in LLMs offers a promising alternative to human participants in social science research [Cui et al.,
2025, Gao et al., 2024]. Fine-tuning enables LLMs to more accurately simulate survey response distributions for
specific subpopulations, even on unseen questions [Cao et al., 2025, Suh et al., 2025]. He-Yueya et al. [2024] propose
psychometric alignment, training LLMs on human response data to better match human understanding on novel items,
though effectiveness varies by domain. Additionally, Kang et al. [2023], Sorensen et al. [2025] investigate human value
representation in LLMs and use value injection to fine-tune models for simulating human opinions.
While current personalization methods can induce more than superficial changes in model outputs, achieving robust,
authentic, and context-independent personalization remains challenging [Dominguez-Olmedo et al., 2024, Kovaˇc et al.,
2024].
28

--- Page 29 ---

7.2
Safety and alignment
Recent work demonstrates that psychometric measurements of LLMs are closely linked to their safety and alignment,
one of the most pressing issues in the field. Wang et al. [2025b], Zhang et al. [2024a] show that LLM personality traits,
as measured by MBTI-M and HEXACO scales, correlate with model safety. For example, Zhang et al. [2024a] find that
better-aligned LLMs exhibit higher Extraversion, Sensing, and Judging, and that modifying LLM personalities can
improve safety, especially regarding privacy and fairness.
Similarly, studies have connected LLM values to safety and alignment. Yao et al. [2024] distinguish safe from unsafe
LLM responses by analyzing correlations with Schwartz’s values, while Ye et al. [2025a,b] accurately predict LLM
safety scores from value orientations measured by the GPV tool. Both Yao et al. [2024], Ye et al. [2025b] use
reinforcement learning to align LLMs with human values, improving safety. In morality, Huang et al. [2024a], Tlaie
[2024] apply MFT-based prompting to enhance LLM moral reasoning and alignment. Ohashi et al. [2024], Takeshita
et al. [2023] introduce the JCommonsenseMorality (JCM) dataset and fine-tune LLMs for local cultural adaptation.
7.3
Cognitive enhancement
Psychometrics effectively enhances LLMs’ human-like reasoning, empathy, and communication skills. Recent work
applies psychological theories and psychometric frameworks to improve LLM cognition via prompting, architectural
modules, and specialized training.
Psychology-inspired prompts boost LLM cognitive abilities. For instance, Li et al. [2023a] show that emotional prompts
enhance general cognition. Role-playing prompts improve ToM [Tan et al., 2024] and foster more human-like reasoning
[Nighojkar et al., 2025]. Zhao et al. [2025b] propose a finite-state machine based on Hill’s Helping Skills theory,
embedding state transitions for emotional support into the model’s multi-hop inference. This structures dialogues
around psychological support and emotional states, improving human-rated effectiveness and strategic alignment.
Liu et al. [2023] introduce a neural listener module into LLMs, jointly optimizing ToM reasoning during training and
highlighting the value of psycholinguistic theories for improving LLM language acquisition. Preference-based and
RL-based approaches further internalize empathy by leveraging cognitive and affective models to construct composite
reward functions or preference signals. For example, Sotolar et al. [2024] utilize formal emotion theories (e.g., Plutchik’s
wheel) to generate preference pairs for model optimization, while others employ empathy classifiers to shape RL
rewards and promote empathetic outputs [Sharma et al., 2021]. Preference optimization based on human judgments in
open-ended social tasks also enhances LLM social-pragmatic reasoning [Wu et al., 2024].
8
Trends, challenges, and future directions
This section explores emerging trends, challenges, and future directions in LLM Psychometrics.
8.1
Psychometric validation
Psychometric validation is increasingly recognized as essential for evaluating LLM personality traits, with multiple
studies addressing different aspects (§ 6). However, ability testing lags behind: most current assessments use structured
tests (e.g., multiple-choice questions) adapted from human-focused instruments. These face notable limitations. For
example, Ullman [2023] show that LLMs often fail on minor variations of ToM tasks, revealing poor parallel forms
reliability. LLMs’ unique internal representations also undermine construct validity, resulting in flawed benchmarks
[Riemer et al., 2025]. Moreover, the generalizability of structured test results to real-world human-AI interactions is
rarely examined, leaving criterion and ecological validity underexplored.
In contrast, newly developed and sophisticated simulation-based tests often lack rigorous psychometric development. As
a result, they may include extraneous factors or insufficiently capture the intended constructs. Notable construct-oriented
efforts include Zhu et al. [2024a], who propose multifaceted evaluations of three cognitive factors from benchmarking
data, and Zhou et al. [2025], who introduce a theory-driven, richer set of general scales. However, defining core abilities
and designing valid, comprehensive ability tests remains an open challenge.
8.2
From human constructs to LLM constructs
Recent research is moving from applying human-based constructs to developing constructs tailored for LLMs. Studies
such as Biedma et al. [2024], Peereboom et al. [2024], Sühr et al. [2023], Ye et al. [2025b] show that human personality
and value factor structures often do not transfer to LLMs. In response, Biedma et al. [2024], Burnell et al. [2023],
29

--- Page 30 ---

Federiakin [2025], Ye et al. [2025b] have adapted or created constructs better suited to LLMs. However, these new
constructs may be dependent on the measurement tools, tasks, and specific LLMs used. For example, Ye et al. [2025b]
and Biedma et al. [2024] find different value structures, while Federiakin [2025] and Burnell et al. [2023] identify
distinct ability factors. Further research is needed to clarify the fundamental structures underlying LLM behaviors.
8.3
Perceived vs. aligned traits
Han et al. [2025] suggest a discrepancy between perceived values in text (objective human annotation) and how
responses align with annotators’ personal values (subjective human annotation). For example, the LLM response,
"Wealthy individuals are not necessarily greedy; some may be motivated by concern for the greater good," is objectively
annotated as expressing Power due to its societal themes. Yet, annotators who value Conformity, rather than Power, feel
the response aligns more closely with their own views. Here, Power is the perceived value, while Conformity is the
aligned value.
This discrepancy, which may apply to other traits, has important methodological implications for LLM Psychometrics.
It raises the question of whether perceived or aligned traits are more significant. While research on value evaluation
often focuses on LLMs’ potential to influence human values, the mechanisms of such influence remain unclear. For
instance, when individuals adopt LLM decisions and values [Glickman and Sharot, 2024, Schoenegger et al., 2025], it
is uncertain whether they follow perceived or aligned traits. The role of judges’ subjectivity in psychometric evaluation
is also not well understood; most scoring models or LLM-as-a-judge approaches assume a universal standard. How
individual differences among judges affect interpretation remains largely unexplored.
8.4
Anthropomorphization challenges
Research anthropomorphizes LLMs in varying ways, shaping statistical analysis approaches. Some studies treat an
LLM as a single individual—evaluating its traits using default settings and system prompts like "You are a helpful
assistant" [Ye et al., 2025a]. Others conceptualize the LLM as a population, using diverse role-playing prompts to elicit
different profiles [Serapio-García et al., 2023]. A third approach treats the LLM as a monolithic entity but generates
multiple result sets by varying prompts for the same test items [Hagendorff et al., 2023]. When viewed as a monolithic
entity, reliability and validity depend mainly on the measurement tools, enabling tool comparisons [Ye et al., 2025a].
When seen as a population, these metrics also depend on the specific LLM, motivating comparisons of consistency and
role-playing ability across models [Serapio-García et al., 2023].
The value of evaluating LLMs in default settings is debatable, given their ability to adopt diverse profiles. Research on
the full spectrum of LLM trait expression—a continuum of possible behaviors—remains limited, and no psychometric
framework yet captures this range. It is unclear how to identify the extremes of LLM behavior or to finely steer LLMs
along a continuous psychometric dimension. In addition, our goal of LLM alignment may shape anthropomorphization
in future research: some advocate for consistency, thereby facilitating the treatment of LLMs as monolithic entities
[Röttger et al., 2024], while others favor pluralistic alignment, suggesting the view of LLMs as populations [Sorensen
et al., 2024b].
8.5
Expanding dimensions in model deployment
LLM Psychometrics is expanding beyond traditional text-based, single-turn interactions, introducing new opportunities
and challenges.
Multi-lingual evaluation.
Most psychometric evaluations focus on English, but multilingual LLMs require thorough
cross-linguistic validation. Studies show LLMs display different personality traits and cognitive abilities across lan-
guages (§ 6.2.2), highlighting potential cultural and linguistic biases in current frameworks. Future work should explore
how results and psychometric properties (reliability, validity) vary by language and develop culturally appropriate
instruments.
Multi-turn interactions.
Multi-turn interactions more closely mirror real human testing, where responses are
influenced by prior interactions. This setting is more challenging and rarely investigated in LLM Psychometrics. Studies
show that LLMs can display markedly different traits across multiple turns, such as greater susceptibility to jailbreaking
attacks [Ying et al., 2025b]. It underscores the need for evaluation methods that account for temporal dynamics in
extended conversations.
Multi-modal capabilities.
Multi-modal models demand novel psychometric methods, as existing text-based evalua-
tions do not capture the complexity of multi-modal understanding and generation. Li et al. [2024b] present one of the
30

--- Page 31 ---

first value measurement tools for Vision-Language Models (VLMs), but it is limited to a simplified setting using only the
first frame of videos. Measuring psychological traits like values is also conceptually challenging in multi-modal settings:
even with clear definitions (e.g., honesty), mapping them to specific real-world actions is often ambiguous. Extending
psychometric tests to embodied agents and action modalities thus poses even greater methodological challenges. Future
work should broaden psychometric tests to additional modalities. Cross-modal evaluation should uphold psychometric
rigor while addressing each modality’s unique features.
Agent and multi-agent systems.
LLM-based agents and multi-agent systems add new complexity to psychometric
evaluation, as agent behavior is shaped by environmental factors, memory, tool use, and interactions with other agents.
Systematic methods for evaluating psychometrics in these dynamic contexts are still largely lacking.
8.6
Item response theory
Applying IRT to LLM outputs offers several advantages: more informative benchmarking [Guinet et al., 2024],
identification of items that best discriminate among high-performing models [Lalor et al., 2024], and adaptive testing to
reduce evaluation costs [Truong et al., 2025, Zhuang et al., 2023a]. Most work to date uses standard IRT models (1PL,
2PL, 3PL), with little exploration of polytomous, hierarchical, or fully multidimensional models, despite the complexity
of LLM capabilities. Integrating IRT with generative AI for automated item generation is emerging, but current methods
are often too complex for practical use [Jiang et al., 2024a]. Although IRT could standardize measurement of LLMs
and humans on a unified scale—even with different test items—this potential is largely untapped.
Systematic use of IRT for bias analysis, such as detecting differential item functioning across model families, is still
nascent [He-Yueya et al., 2024]. IRT provides a principled way to uncover biases by analyzing performance across items
of varying difficulty and demographic context. For example, if items involving certain groups are disproportionately
difficult, this may reveal model or data biases. IRT may also strengthen robustness evaluation by testing model
performance on adversarial or edge-case items.
IRT is also valuable for evaluating AI benchmarks. While benchmarks often include many test items, their informative-
ness and design quality are uncertain; some items may lack discrimination or may favor certain model designs. IRT
enables systematic analysis of item difficulty, discrimination, informativeness, and susceptibility to bias or guessing,
supporting the development of more robust and equitable evaluation frameworks. Despite its promise, IRT is rarely
used beyond evaluation. Highly discriminating items may indicate better training directions, as they can distinguish
between low- and high-performing models.
8.7
From evaluation to enhancement
Evaluation should not only deepen our understanding of models but also drive their improvement. While psychometric
research has focused on evaluating, comparing, and interpreting LLMs, applying these insights to model enhancement
remains underdeveloped. As noted in § 7, psychometric principles can guide prompt engineering, inference-time
control, training data selection, reward design for fine-tuning, and methodological development. Enhancement methods
are still nascent. For example, value targets for LLM alignment in Yao et al. [2024], Ye et al. [2025b] are statically
defined, limiting the integration of context-dependent value states seen in humans [Skimina et al., 2021]. Leveraging
psychometric insights can enable more effective model improvement strategies.
9
Ethical considerations
The emerging field of LLM Psychometrics raises a range of ethical considerations that warrant careful attention.
The considerations discussed here are not exhaustive; we aim to highlight key issues and call for broader awareness
and dialogue around the ethical implications, challenges, and responsibilities associated with applying psychometric
principles to evaluate and enhance LLMs.
Anthropomorphization of LLMs.
A central ethical concern in LLM Psychometrics is the risk of anthropomorphiza-
tion—attributing human-like psychological traits, intentions, or consciousness to language models. While psychometric
frameworks offer powerful tools for quantifying and interpreting LLM behaviors, applying constructs such as personal-
ity, values, or intelligence to non-human entities can mislead both researchers and the public. This misrepresentation
may foster unwarranted trust, emotional attachment, or misplaced expectations regarding LLM capabilities, especially
in sensitive domains like healthcare, education, or counseling. Researchers must exercise caution in language and
framing, clearly distinguishing between metaphorical and literal attributions, and avoid overstating the human-likeness
31

--- Page 32 ---

of LLMs. Developing precise, model-appropriate terminology and interpretive frameworks is essential to prevent the
conflation of machine outputs with genuine human psychological states.
Bias amplification and manipulation in psychometric enhancement.
Psychometric evaluation and enhancement
of LLMs risk amplifying existing biases or enabling manipulation, especially when using unrepresentative data or
instruments. Such tools often reflect the values of specific groups, potentially marginalizing others or promoting narrow
perspectives [Wang et al., 2025a]. Psychometric insights can also be used to shape LLM behavior for particular interests,
raising concerns about fairness and transparency. Researchers should ensure data and instruments are inclusive and
representative, and clearly report limitations and potential biases.
Privacy and consent in human data use.
LLM Psychometrics often analyzes human-LLM interactions and bench-
marks models against human participants, raising privacy and consent concerns. Evaluating LLMs with real user
data or human studies requires strong safeguards: informed consent, data anonymization, and transparent data usage.
Researchers must also prevent unintended psychological profiling or behavioral analysis of individuals through their
LLM interactions.
Implications for human psychology.
Comparing LLMs and humans using psychometric methods risks reducing
complex human traits to algorithmic terms and may undermine human uniqueness. Researchers should recognize
methodological limits and key differences between human and machine cognition. Collaboration with psychologists,
ethicists, and social scientists is essential to ensure such research deepens, rather than oversimplifies, our understanding
of human psychology.
10
Conclusion
This paper presents a systematic review of LLM Psychometrics. The integration of psychometric instruments, theories,
and principles into LLM evaluation promises to overcome the limitations of traditional AI benchmarks. This approach
enables us to more effectively capture the broad, emergent psychological constructs of LLMs, encompassing both
personality and cognitive dimensions. Psychometric evaluation methodologies vary in test formats, data and task
sources, prompting strategies, model outputs, and scoring methods. They each have distinct strengths, weaknesses, and
application scenarios, yet all must adhere to psychometric principles such as reliability, validity, and fairness. Beyond
evaluation, psychometrics-inspired techniques enhance LLMs in trait manipulation, safety and alignment, and cognitive
capabilities, contributing to the development of more powerful and responsible AI systems.
AI development is increasingly driven by evaluation [AAAI, 2025, Silver and Sutton, 2025, Yao, 2025]. We argue
that LLM Psychometrics will play a pivotal role in this shift, introducing new principles, dimensions, techniques, and
insights. We hope this review inspires future evaluation paradigms for human-level AI and advances AI psychology for
the greater good.
32

--- Page 33 ---

References
[1] AAAI.
Ai evaluation.
In Francesca Rossi, editor, Future of AI Research. Association for the Advance-
ment of Artificial Intelligence (AAAI), 2025. URL https://aaai.org/wp-content/uploads/2025/03/
AAAI-2025-PresPanel-Report_FINAL.pdf. Report by the AAAI 2025 Presidential Panel on the Future of
AI Research.
[2] Marwa Abdulhai, Gregory Serapio-García, Clement Crepy, Daria Valter, John Canny, and Natasha Jaques. Moral
foundations of large language models. In Proceedings of the 2024 Conference on Empirical Methods in Natural
Language Processing, pages 17737–17752, 2024.
[3] Katherine Abramski, Salvatore Citraro, Luigi Lombardi, Giulio Rossetti, and Massimo Stella. Cognitive network
science reveals bias in gpt-3, gpt-3.5 turbo, and gpt-4 mirroring math anxiety in high-school students. Big Data
and Cognitive Computing, 7(3):124, 2023.
[4] Muhammad Farid Adilazuarda, Sagnik Mukherjee, Pradhyumna Lavania, Siddhant Singh, Alham Fikri Aji, Jacki
O’Neill, Ashutosh Modi, and Monojit Choudhury. Towards measuring and modeling" culture" in llms: A survey.
arXiv preprint arXiv:2403.15412, 2024.
[5] Muhammad Shahrul Zaim bin Ahmad and Kazuhiro Takemoto. Large-scale moral machine experiment on large
language models. arXiv preprint arXiv:2411.06790, 2024.
[6] Janice Ahn, Rishu Verma, Renze Lou, Di Liu, Rui Zhang, and Wenpeng Yin. Large language models for
mathematical reasoning: Progresses and challenges. In Proceedings of the 18th Conference of the European
Chapter of the Association for Computational Linguistics: Student Research Workshop, pages 225–237, 2024.
[7] Yiming Ai, Zhiwei He, Ziyin Zhang, Wenhong Zhu, Hongkun Hao, Kai Yu, Lingjun Chen, and Rui Wang. Is
self-knowledge and action consistent or not: Investigating large language model’s personality. arXiv preprint
arXiv:2402.14679, 2024.
[8] Meltem Aksoy. Whose morality do they speak? unraveling cultural bias in multilingual language models. arXiv
preprint arXiv:2412.18863, 2024.
[9] Ahmed Alaa, Thomas Hartvigsen, Niloufar Golchini, Shiladitya Dutta, Frances Dean, Inioluwa Deborah Raji,
and Travis Zack. Medical large language model benchmarks should prioritize construct validity. arXiv preprint
arXiv:2503.10694, 2025.
[10] Josh Albrecht, Ellie Kitanidis, and Abraham Fetterman. Despite" super-human" performance, current llms are
unsuited for decisions about ethics and safety. In NeurIPS ML Safety Workshop, 2022.
[11] Gordon W Allport and Henry S Odbert. Trait-names: A psycho-lexical study. Psychological monographs, 47(1):i,
1936.
[12] Maryam Amirizaniani, Elias Martin, Maryna Sivachenko, A. Mashhadi, and Chirag Shah. Do llms exhibit
human-like reasoning? evaluating theory of mind in llms for open-ended responses, 2024.
[13] S. Amouyal, A. Meltzer-Asscher, and Jonathan Berant. Large language models for psycholinguistic plausibility
pretesting, 2024.
[14] Risako Ando, Takanobu Morishita, Hirohiko Abe, Koji Mineshima, and Mitsuhiro Okada. Evaluating large
language models with neubaroco: Syllogistic reasoning ability and human-like biases.
arXiv preprint
arXiv:2306.12567, 2023.
[15] APA Dictionary of Psychology. Personality. URL https://dictionary.apa.org/personality. n.d.
[16] Suhas Arehalli and Tal Linzen. Neural language models capture some, but not all, agreement attractioneffects. In
Proceedings of the Annual Meeting of the Cognitive Science Society, volume 42, 2020.
[17] Suhas Arehalli, Brian Dillon, and Tal Linzen. Syntactic surprisal from neural models predicts, but underestimates,
human processing difficulty from syntactic ambiguities, 2022.
[18] Lisa P Argyle, Ethan C Busby, Nancy Fulda, Joshua R Gubler, Christopher Rytting, and David Wingate. Out of
one, many: Using language models to simulate human samples. Political Analysis, 31(3):337–351, 2023.
33

--- Page 34 ---

[19] Michael C Ashton and Kibeom Lee. Empirical, theoretical, and practical advantages of the hexaco model of
personality structure. Personality and social psychology review, 11(2):150–166, 2007.
[20] Michael C Ashton and Kibeom Lee. The hexaco–60: A short measure of the major dimensions of personality.
Journal of personality assessment, 91(4):340–345, 2009.
[21] Mohammad Atari, Jonathan Haidt, Jesse Graham, Sena Koleva, Sean T Stevens, and Morteza Dehghani. Morality
beyond the weird: How the nomological network of morality varies across cultures. Journal of Personality and
Social Psychology, 125(5):1157, 2023.
[22] Leif Azzopardi and Yashar Moshfeghi. Prism: a methodology for auditing biases in large language models. arXiv
preprint arXiv:2410.18906, 2024.
[23] Yanhong Bai, Jiabao Zhao, Jinxin Shi, Zhentao Xie, Xingjiao Wu, and Liang He. Fairmonitor: A dual-framework
for detecting stereotypes and biases in large language models. arXiv preprint arXiv:2405.03098, 2024.
[24] Sarah Ball, Simeon Allmendinger, Frauke Kreuter, and Niklas Kühl. Human preferences in large language model
latent space: A technical analysis on the reliability of synthetic data in voting outcome prediction. arXiv preprint
arXiv:2502.16280, 2025.
[25] Adrita Barua, Gary Brase, Ke Dong, Pascal Hitzler, and Eugene Vasserman. On the psychology of gpt-4:
Moderately anxious, slightly masculine, honest, and humble. arXiv preprint arXiv:2402.01777, 2024.
[26] Tom L. Beauchamp. Philosophical Ethics: An Introduction to Moral Philosophy. McGraw-Hill, Boston, Mass.,
2001.
[27] Antoine Bellemare-Pepin, François Lespinasse, Philipp Thölke, Yann Harel, Kory Mathewson, Jay A Olson,
Yoshua Bengio, and Karim Jerbi. Divergent creativity in humans and large language models. arXiv preprint
arXiv:2405.13012, 2024.
[28] Yoshua Bengio, Geoffrey Hinton, Andrew Yao, Dawn Song, Pieter Abbeel, Trevor Darrell, Yuval Noah Harari,
Ya-Qin Zhang, Lan Xue, Shai Shalev-Shwartz, et al. Managing extreme ai risks amid rapid progress. Science,
384(6698):842–845, 2024.
[29] Manfred Max Bergman. A theoretical note on the differences between attitudes, opinions, and values. Swiss
Political Science Review, 4(2):81–93, 1998.
[30] Pietro Bernardelle, Leon Fröhling, Stefano Civelli, Riccardo Lunardi, Kevin Roitero, and Gianluca Demartini.
Mapping and influencing the political ideology of large language models using synthetic personas. arXiv preprint
arXiv:2412.14843, 2024.
[31] Pranav Bhandari, Nicolas Fay, Michael Wise, Amitava Datta, Stephanie Meek, Usman Naseem, and Mehwish
Nasim. Can llm agents maintain a persona in discourse? arXiv preprint arXiv:2502.11843, 2025a.
[32] Pranav Bhandari, Usman Naseem, Amitava Datta, Nicolas Fay, and Mehwish Nasim. Evaluating personality traits
in large language models: Insights from psychological questionnaires. arXiv preprint arXiv:2502.05248, 2025b.
[33] Pablo Biedma, Xiaoyuan Yi, Linus Huang, Maosong Sun, and Xing Xie. Beyond human norms: Unveiling unique
values of large language models through interdisciplinary approaches. arXiv preprint arXiv:2404.12744, 2024.
[34] Marcel Binz and Eric Schulz. Using cognitive psychology to understand gpt-3. Proceedings of the National
Academy of Sciences, 120(6):e2218523120, 2023.
[35] James Bisbee, Joshua D Clinton, Cassy Dorff, Brenton Kenkel, and Jennifer M Larson. Synthetic replacements
for human survey data? the perils of large language models. Political Analysis, 32(4):401–416, 2024.
[36] Bojana Bodroža, Bojana M Dini´c, and Ljubiša Boji´c. Personality testing of large language models: limited
temporal stability, but highlighted prosociality. Royal Society Open Science, 11(10):240180, 2024.
[37] Ljubiša Boji´c, Predrag Kovacevic, and Milan ˇCabarkapa. Gpt-4 surpassing human performance in linguistic
pragmatics, 2023.
[38] Vamshi Krishna Bonagiri, Sreeram Vennam, Priyanshul Govil, Ponnurangam Kumaraguru, and Manas Gaur.
Sage: Evaluating moral consistency in large language models. In Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024), pages
14272–14284, 2024.
34

--- Page 35 ---

[39] Léonard Boussioux, Jacqueline N Lane, Miaomiao Zhang, Vladimir Jacimovic, and Karim R Lakhani. The
crowdless future? generative ai and creative problem-solving. Organization Science, 35(5):1589–1607, 2024.
[40] Selmer Bringsjord and Bettina Schimanski. What is artificial intelligence? psychometric ai as an answer. In IJCAI,
pages 887–893. Citeseer, 2003.
[41] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind Nee-
lakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are few-shot learners. Advances
in neural information processing systems, 33:1877–1901, 2020.
[42] Sébastien Bubeck, Varun Chadrasekaran, Ronen Eldan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Peter Lee,
Yin Tat Lee, Yuanzhi Li, Scott Lundberg, et al. Sparks of artificial general intelligence: Early experiments with
gpt-4, 2023.
[43] Ryan Burnell, Han Hao, Andrew RA Conway, and Jose Hernandez Orallo. Revealing the structure of language
model capabilities. arXiv preprint arXiv:2306.10062, 2023.
[44] Samuel Cahyawijaya, Delong Chen, Yejin Bang, Leila Khalatbari, Bryan Wilie, Ziwei Ji, Etsuko Ishii, and Pascale
Fung. High-dimension human value representation in large language models. arXiv preprint arXiv:2404.07900,
2024.
[45] Zhenguang Cai, Xufeng Duan, David Haslett, Shuqi Wang, and Martin Pickering. Do large language models
resemble humans in language use? In Proceedings of the Workshop on Cognitive Modeling and Computational
Linguistics, pages 37–56, 2024.
[46] Yong Cao, Haijiang Liu, Arnav Arora, Isabelle Augenstein, Paul Röttger, and Daniel Hershcovich. Special-
izing large language models to simulate survey response distributions for global populations. arXiv preprint
arXiv:2502.07068, 2025.
[47] Graham Caron and Shashank Srivastava. Identifying and manipulating the personality traits of language models.
arXiv preprint arXiv:2212.10276, 2022.
[48] David W Carroll. Psychology of language. Thomson Brooks/Cole Publishing Co, 1986.
[49] Marta Castello, Giada Pantana, and Ilaria Torre. Examining cognitive biases in chatgpt 3.5 and chatgpt 4 through
human evaluation and linguistic comparison. In Proceedings of the 16th Conference of the Association for
Machine Translation in the Americas (Volume 1: Research Track), pages 250–260, 2024.
[50] Raymond B Cattell and John L Horn. A check on the theory of fluid and crystallized intelligence with description
of new subtest designs. Journal of Educational Measurement, 15(3):139–164, 1978.
[51] Pew Research Center. Spring 2013 survey data, 2013. URL https://www.pewresearch.org/dataset/
spring-2013-survey-data/.
[52] Tanise Ceron, Neele Falk, Ana Bari´c, Dmitry Nikolaev, and Sebastian Padó. Beyond prompt brittleness: Evaluating
the reliability and consistency of political worldviews in llms. Transactions of the Association for Computational
Linguistics, 12:1378–1400, 2024.
[53] Tuhin Chakrabarty, Philippe Laban, Divyansh Agarwal, Smaranda Muresan, and Chien-Sheng Wu. Art or artifice?
large language models and the false promise of creativity. In Proceedings of the 2024 CHI Conference on Human
Factors in Computing Systems, pages 1–34, 2024.
[54] Ilias Chalkidis and Stephanie Brandl. Llama meets eu: Investigating the european political spectrum through the
lens of llms. arXiv preprint arXiv:2403.13592, 2024.
[55] Chunkit Chan, Cheng Jiayang, Yauwai Yim, Zheye Deng, Wei Fan, Haoran Li, Xin Liu, Hongming Zhang, Weiqi
Wang, and Yangqiu Song. Negotiationtom: A benchmark for stress-testing machine theory of mind on negotiation
surrounding, 2024.
[56] Tyler A Chang and Benjamin K Bergen. Language model behavior: A comprehensive survey. Computational
Linguistics, 50(1):293–350, 2024.
[57] Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan Yi, Cunxiang
Wang, Yidong Wang, et al. A survey on evaluation of large language models. ACM transactions on intelligent
systems and technology, 15(3):1–45, 2024.
35

--- Page 36 ---

[58] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira Pinto, Jared Kaplan, Harri
Edwards, Yuri Burda, Nicholas Joseph, Greg Brockman, Alex Ray, Raul Puri, Gretchen Krueger, Michael
Petrov, Heidy Khlaaf, Girish Sastry, Pamela Mishkin, Brooke Chan, Scott Gray, Nick Ryder, Mikhail Pavlov,
Alethea Power, Lukasz Kaiser, Mohammad Bavarian, Clemens Winter, Philippe Tillet, Felipe Petroski Such,
Dave Cummings, Matthias Plappert, Fotios Chantzis, Elizabeth Barnes, Ariel Herbert-Voss, William Hebgen
Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain, William
Saunders, Christopher Hesse, Andrew N. Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan Morikawa, Alec
Radford, Matthew Knight, Miles Brundage, Mira Murati, Katie Mayer, Peter Welinder, Bob McGrew, Dario
Amodei, Sam McCandlish, Ilya Sutskever, and Wojciech Zaremba. Evaluating large language models trained on
code, 2021.
[59] Yanquan Chen, Zhen Wu, Junjie Guo, Shujian Huang, and Xinyu Dai. Extroversion or introversion? controlling
the personality of your large language models. arXiv preprint arXiv:2406.04583, 2024a.
[60] Yanran Chen and Steffen Eger. Do emotions really affect argument convincingness? a dynamic approach with
llm-based manipulation checks. arXiv preprint arXiv:2503.00024, 2025.
[61] Yuyan Chen, Songzhou Yan, Sijia Liu, Yueze Li, and Yanghua Xiao. Emotionqueen: A benchmark for evaluating
empathy of large language models. In Findings of the Association for Computational Linguistics ACL 2024,
pages 2149–2176, 2024b.
[62] Zhawnen Chen, Tianchun Wang, Yizhou Wang, Michal Kosinski, Xiang Zhang, Yun Fu, and Sheng Li. Through
the theory of mind’s eye: Reading minds with multimodal video large language models, 2024c.
[63] Zhuang Chen, Jincenzi Wu, Jinfeng Zhou, Bosi Wen, Guanqun Bi, Gongyao Jiang, Yaru Cao, Mengting Hu,
Yunghwei Lai, Zexuan Xiong, and Minlie Huang. Tombench: Benchmarking theory of mind in large language
models, 2024d.
[64] Yu Ying Chiu, Liwei Jiang, and Yejin Choi. Dailydilemmas: Revealing value preferences of llms with quandaries
of daily life. In The Thirteenth International Conference on Learning Representations, 2025.
[65] Yun-Shiuan Chuang, Krirk Nirunwiroj, Zach Studdiford, Agam Goyal, Vincent Frigo, Sijia Yang, Dhavan Shah,
Junjie Hu, and Timothy Rogers. Beyond demographics: Aligning role-playing llm-based agents using human
belief networks. In Findings of the Association for Computational Linguistics: EMNLP 2024, pages 14010–14026,
2024.
[66] Scott Clifford, Vijeth Iyengar, Roberto Cabeza, and Walter Sinnott-Armstrong. Moral foundations vignettes: A
standardized stimulus database of scenarios based on moral foundations theory. Behavior research methods, 47
(4):1178–1198, 2015.
[67] Julian Coda-Forno, Marcel Binz, Jane X Wang, and Eric Schulz. Cogbench: a large language model walks into a
psychology lab. arXiv preprint arXiv:2402.18225, 2024.
[68] Paul T Costa and Robert R McCrae. The revised neo personality inventory (neo-pi-r). The SAGE handbook of
personality theory and assessment, 2(2):179–198, 2008.
[69] Linda Crocker and James Algina. Introduction to classical and modern test theory. ERIC, 1986.
[70] Jiaxi Cui, Liuzhenghao Lv, Jing Wen, Rongsheng Wang, Jing Tang, YongHong Tian, and Li Yuan. Machine
mindset: An mbti exploration of large language models. arXiv preprint arXiv:2312.12999, 2023.
[71] Ziyan Cui, Ning Li, and Huaikang Zhou. A large-scale replication of scenario-based experiments in psychology
and management using large language models. Nature Computational Science, pages 1–8, 2025.
[72] Yuhao Dan, Jie Zhou, Qin Chen, Junfeng Tian, and Liang He. P-tailor: Customizing personality traits for language
models via mixture of specialized lora experts. arXiv preprint arXiv:2406.12548, 2024.
[73] Roy Dayan, Benjamin Uliel, and Gal Koplewitz. Age against the machine-susceptibility of large language models
to cognitive impairment: cross sectional analysis., 2024.
[74] Edoardo Sebastiano De Duro, Enrique Taietta, Riccardo Improta, and Massimo Stella. Phdgpt: Introducing a
psychometric and linguistic dataset about how large language models perceive graduate students and professors
in psychology. arXiv preprint arXiv:2411.10473, 2024.
36

--- Page 37 ---

[75] Dorottya Demszky, Diyi Yang, David S Yeager, Christopher J Bryan, Margarett Clapper, Susannah Chandhok,
Johannes C Eichstaedt, Cameron Hecht, Jeremy Jamieson, Meghann Johnson, et al. Using large language models
in psychology. Nature Reviews Psychology, 2(11):688–701, 2023.
[76] Jia Deng, Tianyi Tang, Yanbin Yin, Wenhao Yang, Wayne Xin Zhao, and Ji-Rong Wen. Neuron-based personality
trait induction in large language models. arXiv preprint arXiv:2410.12327, 2024.
[77] Vittoria Dentella, Fritz Guenther, and Evelina Leivada. Language in vivo vs. in silico: Size matters but larger
language models still do not comprehend language on a par with humans, 2024.
[78] Ricardo Dominguez-Olmedo, Moritz Hardt, and Celestine Mendler-Dünner. Questioning the survey responses of
large language models. Advances in Neural Information Processing Systems, 37:45850–45878, 2024.
[79] Wenhan Dong, Yuemeng Zhao, Zhen Sun, Yule Liu, Zifan Peng, Jingyi Zheng, Zongmin Zhang, Ziyi Zhang, Jun
Wu, Ruiming Wang, et al. Humanizing llms: A survey of psychological measurements with tools, datasets, and
human-agent applications. arXiv preprint arXiv:2505.00049, 2025.
[80] Ina Dormuth, Sven Franke, Marlies Hafer, Tim Katzke, Alexander Marx, Emmanuel Müller, Daniel Neider,
Markus Pauly, and Jérôme Rutinowski. A cautionary tale about" neutrally" informative ai tools ahead of the 2025
federal elections in germany. arXiv preprint arXiv:2502.15568, 2025.
[81] Florian Dorner, Tom Sühr, Samira Samadi, and Augustin Kelava. Do personality tests generalize to large language
models? In Socially Responsible Language Modelling Research, 2023.
[82] Shitong Duan, Xiaoyuan Yi, Peng Zhang, Tun Lu, Xing Xie, and Ning Gu. Denevil: Towards deciphering and
navigating the ethical values of large language models via instruction learning. arXiv preprint arXiv:2310.11053,
2023.
[83] Xufeng Duan, Bei Xiao, Xuemei Tang, and Zhenguang G. Cai. Hlb: Benchmarking llms’ humanlikeness in
language use, 2024a.
[84] Xufeng Duan, Xinyu Zhou, Bei Xiao, and Zhenguang G. Cai. Unveiling language competence neurons: A
psycholinguistic approach to model interpretability, 2024b.
[85] Esin Durmus, Karina Nguyen, Thomas I Liao, Nicholas Schiefer, Amanda Askell, Anton Bakhtin, Carol Chen, Zac
Hatfield-Dodds, Danny Hernandez, Nicholas Joseph, et al. Towards measuring the representation of subjective
global opinions in language models. arXiv preprint arXiv:2306.16388, 2023.
[86] Jessica Echterhoff, Yao Liu, Abeer Alessa, Julian McAuley, and Zexue He. Cognitive bias in decision-making
with llms. arXiv preprint arXiv:2403.00811, 2024.
[87] Zohar Elyoseph, Dorit Hadar-Shoval, Kfir Asraf, and Maya Lvovsky. Chatgpt outperforms humans in emotional
awareness evaluations. Frontiers in psychology, 14:1199058, 2023.
[88] Susan E Embretson and Steven P Reise. Item response theory for psychologists. Psychology Press, 2013.
[89] Allyson Ettinger. What bert is not: Lessons from a new suite of psycholinguistic diagnostics for language models.
Transactions of the Association for Computational Linguistics, 8:34–48, 2020.
[90] Thomas G Evans. A heuristic program to solve geometric-analogy problems. In Proceedings of the April 21-23,
1964, spring joint computer conference, pages 327–338, 1964.
[91] Qixiang Fang, Daniel L Oberski, and Dong Nguyen. Patch! psychometrics-assisted benchmarking of large
language models: A case study of proficiency in 8th grade mathematics. arXiv preprint arXiv:2404.01799, 2024.
[92] Mats Faulborn, Indira Sen, Max Pellert, Andreas Spitz, and David Garcia. Only a little to the left: A theory-
grounded measure of political bias in large language models. arXiv preprint arXiv:2503.16148, 2025.
[93] Denis Federiakin.
Improving llm leaderboards with psychometrical methodology.
arXiv preprint
arXiv:2501.17200, 2025.
[94] Anita Feher and Philip A Vernon. Looking beyond the big five: A selective review of alternatives to the big five
model of personality. Personality and Individual Differences, 169:110002, 2021.
37

--- Page 38 ---

[95] Shangbin Feng, Chan Young Park, Yuhan Liu, and Yulia Tsvetkov. From pretraining data to language models
to downstream tasks: Tracking the trails of political biases leading to unfair nlp models.
arXiv preprint
arXiv:2305.08283, 2023.
[96] Ronald Fischer, Markus Luczak-Roesch, and Johannes A Karl. What does chatgpt return about human values?
exploring value bias in chatgpt using a descriptive value theory. arXiv preprint arXiv:2304.03612, 2023.
[97] Michael C Frank. Baby steps in evaluating the capacities of large language models. Nature Reviews Psychology, 2
(8):451–452, 2023a.
[98] Michael C Frank. Bridging the data gap between children and large language models. Trends in Cognitive
Sciences, 27(11):990–992, 2023b.
[99] Kathleen C Fraser, Svetlana Kiritchenko, and Esma Balkir. Does moral code have a moral code? probing delphi’s
moral philosophy. In Proceedings of the 2nd Workshop on Trustworthy Natural Language Processing (TrustNLP
2022), pages 26–42, 2022.
[100] Ivar Frisch and Mario Giulianelli. Llm agents in interaction: Measuring personality consistency and linguistic
alignment in interacting populations of large language models. arXiv preprint arXiv:2402.02896, 2024.
[101] Richard Futrell, Ethan Wilcox, Takashi Morita, Peng Qian, Miguel Ballesteros, and Roger Levy. Neural language
models as psycholinguistic subjects: Representations of syntactic state. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers), pages 32–42, 2019.
[102] Isaac R. Galatzer-Levy, David Munday, Jed N McGiffin, Xin Liu, Danny Karmon, Ilia Labzovsky, Rivka
Moroshko, Amir Zait, and Daniel McDuff. The cognitive capabilities of generative ai: A comparative analysis
with human benchmarks, 2024.
[103] Isabel O Gallegos, Ryan A Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernoncourt, Tong
Yu, Ruiyi Zhang, and Nesreen K Ahmed. Bias and fairness in large language models: A survey. Computational
Linguistics, 50(3):1097–1179, 2024.
[104] Kanishk Gandhi, Jan-Philipp Franken, Tobias Gerstenberg, and Noah D. Goodman. Understanding social
reasoning in language models with language models, 2023.
[105] Chen Gao, Xiaochong Lan, Nian Li, Yuan Yuan, Jingtao Ding, Zhilun Zhou, Fengli Xu, and Yong Li. Large
language models empowered agent-based modeling and simulation: A survey and perspectives. Humanities and
Social Sciences Communications, 11(1):1–24, 2024.
[106] Basile Garcia, Crystal Qian, and Stefano Palminteri. The moral turing test: Evaluating human-llm alignment in
moral decision-making. arXiv preprint arXiv:2410.07304, 2024.
[107] Mingmeng Geng, Sihong He, and Roberto Trotta. Are large language models chameleons? an attempt to simulate
social surveys. arXiv preprint arXiv:2405.19323, 2024.
[108] Moshe Glickman and Tali Sharot. How human–ai feedback loops alter human perceptual, emotional and social
judgements. Nature Human Behaviour, pages 1–15, 2024.
[109] Lewis R Goldberg. An alternative “description of personality”: The big-five factor structure. In Personality and
personality disorders, pages 34–47. Routledge, 2013.
[110] Jesse Graham, Jonathan Haidt, and Brian A Nosek. Liberals and conservatives rely on different sets of moral
foundations. Journal of personality and social psychology, 96(5):1029, 2009.
[111] Igor Grossmann, Matthew Feinberg, Dawn C Parker, Nicholas A Christakis, Philip E Tetlock, and William A
Cunningham. Ai and the transformation of social science research. Science, 380(6650):1108–1109, 2023.
[112] Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie
Ma, Honghao Liu, et al. A survey on llm-as-a-judge. arXiv preprint arXiv:2411.15594, 2024.
[113] Joy Paul Guilford, Paul R Christensen, Philip R Merrifield, and Robert C Wilson. Alternate Uses: Manual of
Instructions and Interpretation. Sheridan Psychological Services, 1978.
38

--- Page 39 ---

[114] Gauthier Guinet, Behrooz Omidvar-Tehrani, Anoop Deoras, and Laurent Callot. Automated evaluation of
retrieval-augmented language models with task-specific exam generation. In Proceedings of the 41st International
Conference on Machine Learning, ICML’24. JMLR.org, 2024.
[115] Xiao-Yu Guo, Yuan-Fang Li, and Reza Haf. Desiq: Towards an unbiased, challenging benchmark for social
intelligence understanding. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language
Processing, pages 3169–3180, 2023a.
[116] Zishan Guo, Renren Jin, Chuang Liu, Yufei Huang, Dan Shi, Linhao Yu, Yan Liu, Jiaxuan Li, Bojian Xiong,
Deyi Xiong, et al. Evaluating large language models: A comprehensive survey. arXiv preprint arXiv:2310.19736,
2023b.
[117] Akshat Gupta, Xiaoyang Song, and Gopala Anumanchipalli. Self-assessment tests are unreliable measures of
llm personality. In Proceedings of the 7th BlackboxNLP Workshop: Analyzing and Interpreting Neural Networks
for NLP, pages 301–314, 2024.
[118] Dorit Hadar-Shoval, Kfir Asraf, Yonathan Mizrachi, Yuval Haber, and Zohar Elyoseph. Assessing the alignment
of large language models with human values for mental health integration: cross-sectional study using schwartz’s
theory of basic values. JMIR Mental Health, 11:e55988, 2024.
[119] Dorit Hadar-Shoval, Maya Lvovsky, Kfir Asraf, Yoav Shimoni, Zohar Elyoseph, et al. The feasibility of large
language models in verbal comprehension assessment: Mixed methods feasibility study. JMIR Formative
Research, 9(1):e68347, 2025.
[120] Christian Haerpfer, Ronald Inglehart, Alejandro Moreno, Christian Welzel, Kseniya Kizilova, Jaime Diez-
Medrano, Marta Lagos, Pippa Norris, Eduard Ponarin, and Bi Puranen. World values survey wave 7 (2017-2022)
cross-national data-set. (No Title), 2022.
[121] Thilo Hagendorff. Machine psychology: Investigating emergent capabilities and behavior in large language
models using psychological methods. arXiv preprint arXiv:2303.13988, 1, 2023.
[122] Thilo Hagendorff, Sarah Fabi, and Michal Kosinski. Human-like intuitive behavior and reasoning biases emerged
in large language models but disappeared in chatgpt. Nature Computational Science, 3(10):833–838, 2023.
[123] Thilo Hagendorff, Ishita Dasgupta, Marcel Binz, Stephanie CY Chan, Andrew Lampinen, Jane X Wang, Zeynep
Akata, and Eric Schulz. Machine psychology. arXiv preprint cs.CL/2303.13988, 2024.
[124] Patrick Haller, Ansar Aynetdinov, and Alan Akbik. Opiniongpt: Modelling explicit biases in instruction-tuned
llms. arXiv preprint arXiv:2309.03876, 2023.
[125] Hyemin Han. Potential benefits of employing large language models in research in moral education and
development. Journal of Moral Education, pages 1–16, 2023.
[126] Jongwook Han, Dongmin Choi, Woojung Song, Eun-Ju Lee, and Yohan Jo. Value portrait: Understanding values
of llms with human-aligned benchmark. arXiv preprint arXiv:2505.01015, 2025.
[127] Jochen Hartmann, Jasper Schwenzow, and Maximilian Witte. The political ideology of conversational ai: Con-
verging evidence on chatgpt’s pro-environmental, left-libertarian orientation. arXiv preprint arXiv:2301.01768,
2023.
[128] William M Hayes, Nicolas Yax, and Stefano Palminteri. Relative value biases in large language models. In
Proceedings of the Annual Meeting of the Cognitive Science Society, volume 46, 2024.
[129] Linyang He, Ercong Nie, Helmut Schmid, Hinrich Schutze, N. Mesgarani, and Jonathan Brennan. Large language
models as neurolinguistic subjects: Discrepancy in performance and competence for form and meaning, 2024.
[130] Yinghui He, Yufan Wu, Yilin Jia, Rada Mihalcea, Yulong Chen, and Naihao Deng. Hi-tom: A benchmark for
evaluating higher-order theory of mind reasoning in large language models, 2023.
[131] Zihong He and Changwang Zhang. Afspp: Agent framework for shaping preference and personality with large
language models. arXiv preprint arXiv:2401.02870, 2024.
[132] Joy He-Yueya, Wanjing Anya Ma, Kanishk Gandhi, Benjamin W Domingue, Emma Brunskill, and Noah D
Goodman. Psychometric alignment: Capturing human knowledge distributions via language models. arXiv
preprint arXiv:2407.15645, 2024.
39

--- Page 40 ---

[133] Jennifer Healey, Laurie Byrum, Md Nadeem Akhtar, and Moumita Sinha. Evaluating nuanced bias in large
language model free response answers. In International Conference on Applications of Natural Language to
Information Systems, pages 378–391. Springer, 2024.
[134] Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
Measuring massive multitask language understanding. arXiv preprint arXiv:2009.03300, 2020.
[135] Dan Hendrycks, Collin Burns, Steven Basart, Andrew Critch, Jerry Li, Dawn Song, and Jacob Steinhardt.
Aligning ai with shared human values. In International Conference on Learning Representations, 2021.
[136] Airlie Hilliard, Cristian Munoz, Zekun Wu, and Adriano Soares Koshiyama. Eliciting personality traits in large
language models. arXiv preprint arXiv:2402.08341, 2024.
[137] Geert Hofstede. Culture’s consequences: International differences in work-related values, volume 5. sage, 1984.
[138] Bart Holterman and K. V. Deemter. Does chatgpt have theory of mind?, 2023.
[139] Xudong Hong, Margarita Ryzhova, Daniel Adrian Biondi, and Vera Demberg. Do large language models and
humans have similar behaviours in causal inference with script knowledge?, 2023.
[140] Guiyang Hou, Wenqi Zhang, Yongliang Shen, Linjuan Wu, and Weiming Lu. Timetom: Temporal space is the
key to unlocking the door of large language models’ theory-of-mind, 2024.
[141] Robert J House, Paul J Hanges, Mansour Javidan, Peter W Dorfman, and Vipin Gupta. Culture, leadership, and
organizations: The GLOBE study of 62 societies. Sage publications, 2004.
[142] He Hu, Yucheng Zhou, Lianzhong You, Hongbo Xu, Qianning Wang, Zheng Lian, Fei Richard Yu, Fei Ma, and
Laizhong Cui. Emobench-m: Benchmarking emotional intelligence for multimodal large language models. arXiv
preprint arXiv:2502.04424, 2025.
[143] Jennifer Hu and Roger Levy. Prompt-based methods may underestimate large language models’ linguistic
generalizations, 2023.
[144] Jennifer Hu, Sammy Floyd, Olessia Jouravlev, Evelina Fedorenko, and Edward Gibson. A fine-grained compari-
son of pragmatic language understanding in humans and language models. In Proceedings of the 61st Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 4194–4213, 2023.
[145] Meng Hua, Yuan Cheng, and Hengshu Zhu. The career interests of large language models. arXiv preprint
arXiv:2407.08564, 2024.
[146] Allison Huang, Carlos Mougan, and Yulu Pi. Moral persuasion in large language models: Evaluating susceptibility
and ethical alignment. In The Third Workshop on New Frontiers in Adversarial Machine Learning, 2024a.
[147] Jen-tse Huang, Wenxiang Jiao, Man Ho Lam, Eric John Li, Wenxuan Wang, and Michael R Lyu. Revisiting the
reliability of psychological scales on large language models. arXiv preprint arXiv:2305.19926, 2023a.
[148] Jen-tse Huang, Man Ho Lam, Eric John Li, Shujie Ren, Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu, and
Michael R Lyu. Emotionally numb or empathetic? evaluating how llms feel using emotionbench. arXiv preprint
arXiv:2308.03656, 2023b.
[149] Jen-tse Huang, Wenxuan Wang, Man Ho Lam, Eric John Li, Wenxiang Jiao, and Michael R Lyu. Chatgpt an enfj,
bard an istj: Empirical study on personalities of large language models. arXiv preprint arXiv:2305.19926, 2023c.
[150] Jen-tse Huang, Wenxuan Wang, Eric John Li, Man Ho Lam, Shujie Ren, Youliang Yuan, Wenxiang Jiao,
Zhaopeng Tu, and Michael Lyu. On the humanity of conversational ai: Evaluating the psychological portrayal of
llms. In The Twelfth International Conference on Learning Representations, 2023d.
[151] Jen-tse Huang, Wenxuan Wang, Eric John Li, Man Ho Lam, Shujie Ren, Youliang Yuan, Wenxiang Jiao,
Zhaopeng Tu, and Michael R Lyu. Who is chatgpt? benchmarking llms’ psychological portrayal using psy-
chobench. arXiv preprint arXiv:2310.01386, 2023e.
[152] Jen-tse Huang, Man Ho Lam, Eric John Li, Shujie Ren, Wenxuan Wang, Wenxiang Jiao, Zhaopeng Tu, and
Michael R Lyu. Apathetic or empathetic? evaluating llms’ emotional alignments with humans. Advances in
Neural Information Processing Systems, 37:97053–97087, 2024b.
40

--- Page 41 ---

[153] Muhua Huang, Xijuan Zhang, Christopher Soto, and James Evans. Designing llm-agents with personalities: A
psychometric approach. arXiv preprint arXiv:2410.19238, 2024c.
[154] K. Hubert, K. N. Awa, and D. Zabelina. Artificial intelligence is more creative than humans: A cognitive science
perspective on the current state of generative language models, 2023. URL https://doi.org/10.31234/osf.
io/6py2m. Preprint, September 18.
[155] Markus Huff and Elanur Ulakçi. Towards a psychology of machines: Large language models predict human
memory, 2024.
[156] EunJeong Hwang, Bodhisattwa Prasad Majumder, and Niket Tandon. Aligning language models to user opinions.
arXiv preprint arXiv:2305.14929, 2023.
[157] Seojin Hwang, Yumin Kim, Byeongjeong Kim, and Hwanhee Lee. Personality editing for language models
through relevant knowledge editing. arXiv preprint arXiv:2502.11789, 2025.
[158] Yusuke Ide, Yuto Nishida, Miyu Oba, Yusuke Sakai, Justin Vasselli, Hidetaka Kamigaito, and Taro Watanabe.
How to make the most of llms’ grammatical knowledge for acceptability judgments, 2024.
[159] David Ili´c and Gilles E Gignac. Evidence of interrelated cognitive-like capabilities in large language models:
Indications of artificial general intelligence or achievement? Intelligence, 106:101858, 2024.
[160] Navya Jain, Zekun Wu, Cristian Munoz, Airlie Hilliard, Xin Guan, Adriano Koshiyama, Emre Kazim, and Philip
Treleaven. From text to emoji: How peft-driven personality manipulation unleashes the emoji potential in llms.
arXiv preprint arXiv:2409.10245, 2024.
[161] Mohsen Jamali, Ziv M. Williams, and Jing Cai. Unveiling theory of mind in large language models: A parallel to
single neurons in the human brain, 2023.
[162] Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue Hua, and Yongfeng Zhang. Moralbench: Moral
evaluation of llms. arXiv preprint arXiv:2406.04428, 2024.
[163] Guangyuan Jiang, Manjie Xu, Song-Chun Zhu, Wenjuan Han, Chi Zhang, and Yixin Zhu. Evaluating and
inducing personality in pre-trained language models. Advances in Neural Information Processing Systems, 36:
10622–10643, 2023.
[164] Han Jiang, Xiaoyuan Yi, Zhihua Wei, Ziang Xiao, Shu Wang, and Xing Xie. Raising the bar: Investigating the
values of large language models via generative evolving testing. arXiv preprint arXiv:2406.14230, 2024a.
[165] Hang Jiang, Doug Beeferman, Brandon Roy, and Deb Roy. Communitylm: Probing partisan worldviews from
language models. arXiv preprint arXiv:2209.07065, 2022.
[166] Hang Jiang, Xiajie Zhang, Xubo Cao, Cynthia Breazeal, Deb Roy, and Jad Kabbara. Personallm: Investigating
the ability of large language models to express personality traits. In Findings of the Association for Computational
Linguistics: NAACL 2024, pages 3605–3627, 2024b.
[167] Minhao Jiang, Ken Ziyu Liu, Ming Zhong, Rylan Schaeffer, Siru Ouyang, Jiawei Han, and Sanmi Koyejo.
Investigating data contamination for pre-training language models. arXiv preprint arXiv:2401.06059, 2024c.
[168] Shapeng Jiang, Lijia Wei, and Chen Zhang. Donald trumps in the virtual polls: Simulating and predicting public
opinions in surveys using large language models. arXiv preprint arXiv:2411.01582, 2024d.
[169] Chuanyang Jin, Yutong Wu, Jing Cao, Jiannan Xiang, Yen-Ling Kuo, Zhiting Hu, T. Ullman, Antonio Torralba,
Joshua B. Tenenbaum, and Tianmin Shu. Mmtom-qa: Multimodal theory of mind question answering, 2024a.
[170] Zhijing Jin, Sydney Levine, Fernando Gonzalez Adauto, Ojasv Kamal, Maarten Sap, Mrinmaya Sachan, Rada
Mihalcea, Josh Tenenbaum, and Bernhard Schölkopf. When to make exceptions: Exploring language models as
accounts of human moral judgment. Advances in neural information processing systems, 35:28458–28473, 2022.
[171] Zhijing Jin, Max Kleiman-Weiner, Giorgio Piatti, Sydney Levine, Jiarui Liu, Fernando Gonzalez, Francesco
Ortu, András Strausz, Mrinmaya Sachan, Rada Mihalcea, et al. Language model alignment in multilingual trolley
problems. arXiv preprint arXiv:2407.02273, 2024b.
[172] Yuu Jinnai. Does cross-cultural alignment change the commonsense morality of language models? In Proceedings
of the 2nd Workshop on Cross-Cultural Considerations in NLP, pages 48–64, 2024.
41

--- Page 42 ---

[173] Oliver P. John, Emily M. Donahue, and Robert L. Kentle. Big five inventory, 1991. URL https://psycnet.
apa.org/doiLanding?doi=10.1037%2Ft07550-000. Journal of Personality and Social Psychology.
[174] Peter K Jonason and Gregory D Webster. The dirty dozen: a concise measure of the dark triad. Psychological
assessment, 22(2):420, 2010.
[175] Cameron R. Jones, Sean Trott, and Benjamin K. Bergen. Comparing humans and large language models on an
experimental protocol inventory for theory of mind evaluation (epitome), 2024.
[176] Tianjie Ju, Zhenyu Shao, Bowen Wang, Yujia Chen, Zhuosheng Zhang, Hao Fei, Mong-Li Lee, Wynne Hsu,
Sufeng Duan, and Gongshen Liu. Probing then editing response personality of large language models. arXiv
preprint arXiv:2504.10227, 2025.
[177] Kirill Kalinin. Improving gpt generated synthetic samples with sampling-permutation algorithm. Available at
SSRN 4548937, 2023.
[178] Dongjun Kang, Joonsuk Park, Yohan Jo, and JinYeong Bak. From values to opinions: Predicting human
behaviors and stances using value-injected large language models. arXiv preprint arXiv:2310.17857, 2023.
[179] Robert M Kaplan and Dennis P Saccuzzo.
Psychological testing: Principles, applications, and issues.
Wadsworth/Thomson Learning, 2001.
[180] Elena Kardanova, Alina Ivanova, Ksenia Tarasova, Taras Pashchenko, Aleksei Tikhoniuk, Elen Yusupova,
Anatoly Kasprzhak, Yaroslav Kuzminov, Ekaterina Kruchinskaia, and Irina Brun. A novel psychometrics-
based approach to developing professional competency benchmark for large language models. arXiv preprint
arXiv:2411.00045, 2024.
[181] Elise Karinshak, Amanda Hu, Kewen Kong, Vishwanatha Rao, Jingren Wang, Jindong Wang, and Yi Zeng.
Llm-globe: A benchmark evaluating the cultural values embedded in llm output. arXiv preprint arXiv:2411.06032,
2024.
[182] Artem Karpov, Seong Hah Cho, Austin Meek, Raymond Koopmanschap, Lucy Farnik, and Bogdan-Ionut Cirstea.
Inducing human-like biases in moral reasoning language models. arXiv preprint arXiv:2411.15386, 2024.
[183] Saketh Reddy Karra, Son The Nguyen, and Theja Tulabandhula. Estimating the personality of white-box
language models. arXiv preprint arXiv:2204.12000, 2022.
[184] Aditi Khandelwal, Utkarsh Agarwal, Kumar Tanmay, and Monojit Choudhury. Do moral judgment and reasoning
capability of llms change with language? a study using the multilingual defining issues test. In Proceedings of
the 18th Conference of the European Chapter of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 2882–2894, 2024.
[185] Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag Shah.
How well do llms represent values
across cultures? empirical analysis of llm responses based on hofstede cultural dimensions. arXiv preprint
arXiv:2406.14805, 2024.
[186] Hyunwoo Kim, Melanie Sclar, Zhi-Xuan Tan, Lance Ying, Sydney Levine, Yang Liu, Joshua B. Tenenbaum, and
Yejin Choi. Hypothesis-driven theory-of-mind reasoning for large language models, 2025a.
[187] Junsol Kim and Byungkyu Lee. Ai-augmented surveys: Leveraging large language models and surveys for
opinion prediction. arXiv preprint arXiv:2305.09620, 2023.
[188] Junsol Kim, James Evans, and Aaron Schein. Linear representations of political perspective emerge in large
language models. arXiv preprint arXiv:2503.02080, 2025b.
[189] Minsang Kim and Seungjun Baek. Exploring large language models on cross-cultural values in connection with
training methodology. arXiv preprint arXiv:2412.08846, 2024.
[190] Lawrence J Klinkert, Stephanie Buongiorno, and Corey Clark. Driving generative agents with their personality.
arXiv preprint arXiv:2402.14879, 2024.
[191] Lawrence Kohlberg. Development of moral character and moral ideology, volume 1. University of Chicago,
1964.
[192] Michal Kosinski. Theory of mind may have spontaneously emerged in large language models, 2023a.
42

--- Page 43 ---

[193] Michal Kosinski. Evaluating large language models in theory of mind tasks, 2023b.
[194] Grgur Kovaˇc, Masataka Sawayama, Rémy Portelas, Cédric Colas, Peter Ford Dominey, and Pierre-Yves Oudeyer.
Large language models as superpositions of cultural perspectives. arXiv preprint arXiv:2307.07870, 2023.
[195] Grgur Kovaˇc, Rémy Portelas, Masataka Sawayama, Peter Ford Dominey, and Pierre-Yves Oudeyer. Stick to
your role! stability of personal values expressed in large language models. Plos one, 19(8):e0309114, 2024.
[196] Grgur Kovaˇc, Rémy Portelas, Katja Hofmann, and Pierre-Yves Oudeyer. Socialai 0.1: Towards a benchmark to
stimulate research on socio-cognitive abilities in deep reinforcement learning agents, 2021.
[197] Grgur Kovaˇc, Rémy Portelas, P. Dominey, and Pierre-Yves Oudeyer. The socialai school: a framework leveraging
developmental psychology toward artificial socio-cultural agents, 2024.
[198] Eyup Engin Kucuk and Muhammed Yusuf Kocyigit. Western, religious or spiritual: An evaluation of moral
justification in large language models. arXiv preprint arXiv:2311.07792, 2023.
[199] Divyanshu Kumar, Umang Jain, Sahil Agarwal, and Prashanth Harshangi. Investigating implicit bias in large
language models: A large-scale study of over 50 llms. arXiv preprint arXiv:2410.12864, 2024.
[200] Lucio La Cava and Andrea Tagarelli. Open models, closed minds? on agents capabilities in mimicking human
personalities through open large language models. arXiv preprint arXiv:2401.07115, 2024.
[201] John P Lalor, Pedro Rodriguez, João Sedoc, and Jose Hernandez-Orallo. Item response theory for natural
language processing. In Proceedings of the 18th Conference of the European Chapter of the Association for
Computational Linguistics: Tutorial Abstracts, pages 9–13, 2024.
[202] Bruce W Lee, Yeongheon Lee, and Hyunsoo Cho. Language models show stable value orientations across
diverse role-plays. arXiv preprint arXiv:2408.09049, 2024a.
[203] Byung Cheol Lee and Jaeyeon Chung. An empirical investigation of the impact of chatgpt on creativity. Nature
Human Behaviour, 8(10):1906–1914, 2024.
[204] Eun-Kyoung Rosa Lee, Sathvik Nair, and Naomi H. Feldman. A psycholinguistic evaluation of language models’
sensitivity to argument roles, 2024b.
[205] Kibeom Lee and Michael C Ashton. Psychometric properties of the hexaco-100. Assessment, 25(5):543–556,
2018.
[206] Sanguk Lee, Tai-Quan Peng, Matthew H Goldberg, Seth A Rosenthal, John E Kotcher, Edward W Maibach, and
Anthony Leiserowitz. Can large language models estimate public opinion about global warming? an empirical
assessment of algorithmic fidelity and bias. PLOS Climate, 3(8):e0000429, 2024c.
[207] Seungbeen Lee, Seungwon Lim, Seungju Han, Giyeong Oh, Hyungjoo Chae, Jiwan Chung, Minju Kim, Beong-
woo Kwak, Yeonsoo Lee, Dongha Lee, et al. Do llms have distinct and consistent personality? trait: Personality
testset designed for llms with psychometrics. arXiv preprint arXiv:2406.14703, 2024d.
[208] Tony Lee, Haoqin Tu, Chi Heem Wong, Wenhao Zheng, Yiyang Zhou, Yifan Mai, Josselin Roberts, Michihiro
Yasunaga, Huaxiu Yao, Cihang Xie, et al. Vhelm: A holistic evaluation of vision language models. Advances in
Neural Information Processing Systems, 37:140632–140666, 2024e.
[209] Yoon Kyung Lee, Jina Suh, Hongli Zhan, Junyi Jessy Li, and Desmond C Ong. Large language models produce
responses perceived to be empathic. arXiv preprint arXiv:2403.18148, 2024f.
[210] Courtland Leer, Vincent Trost, and Vineeth Voruganti. Violation of expectation via metacognitive prompting
reduces theory of mind prediction error in large language models, 2023.
[211] Yan Leng and Yuan Yuan. Do llm agents exhibit social behavior? arXiv preprint arXiv:2312.15198, 2023.
[212] Andrew Li, Xianle Feng, Siddhant Narang, Austin Peng, Tianle Cai, Raj Sanjay Shah, and Sashank Varma.
Incremental comprehension of garden-path sentences by large language models: Semantic interpretation, syntactic
re-analysis, and attention, 2024a.
[213] Cheng Li, Jindong Wang, Yixuan Zhang, Kaijie Zhu, Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang,
and Xing Xie. Large language models understand and can be enhanced by emotional stimuli. arXiv preprint
arXiv:2307.11760, 2023a.
43

--- Page 44 ---

[214] Huao Li, Yu Quan Chong, Simon Stepputtis, Joseph Campbell, Dana Hughes, Michael Lewis, and Katia P.
Sycara. Theory of mind for multi-agent collaboration via large language models, 2023b.
[215] Jingxuan Li, Yuning Yang, Shengqi Yang, Yizhou Zhao, and Ying Nian Wu. Quantifying preferences of
vision-language models via value decomposition in social media contexts. arXiv preprint arXiv:2411.11479,
2024b.
[216] Wenkai Li, Jiarui Liu, Andy Liu, Xuhui Zhou, Mona Diab, and Maarten Sap. Big5-chat: Shaping llm personalities
through training on human-grounded data. arXiv preprint arXiv:2410.16491, 2024c.
[217] Xingxuan Li, Yutong Li, Linlin Liu, Lidong Bing, and Shafiq Joty. Is gpt-3 a psychopath? evaluating large
language models from a psychological perspective. arXiv preprint arXiv:2212.10529, 10, 2022a.
[218] Xingxuan Li, Yutong Li, Lin Qiu, Shafiq Joty, and Lidong Bing. Evaluating psychological safety of large
language models. arXiv preprint arXiv:2212.10529, 2022b.
[219] Yuan Li, Yue Huang, Hongyi Wang, Xiangliang Zhang, James Zou, and Lichao Sun. Quantifying ai psychology:
A psychometrics benchmark for large language models. arXiv preprint arXiv:2406.17675, 2024d.
[220] Zaijing Li, Gongwei Chen, Rui Shao, Yuquan Xie, Dongmei Jiang, and Liqiang Nie. Enhancing emotional
generation capability of large language models via emotional chain-of-thought. arXiv preprint arXiv:2401.06836,
2024e.
[221] Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian Zhang,
Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of language models. arXiv preprint
arXiv:2211.09110, 2022.
[222] Yuanzhi Liang, Linchao Zhu, and Yi Yang. Anteval: Evaluation of social interaction competencies in llm-driven
agents, 2024.
[223] Zizheng Lin, Chunkit Chan, Yangqiu Song, and Xin Liu. Constrained reasoning chains for enhancing theory-of-
mind in large language models, 2024.
[224] Andy Liu, Hao Zhu, Emmy Liu, Yonatan Bisk, and Graham Neubig. Computational language acquisition with
theory of mind. In The Eleventh International Conference on Learning Representations, 2023.
[225] Jianzhi Liu, Hexiang Gu, Tianyu Zheng, Liuyu Xiang, Huijia Wu, Jie Fu, and Zhaofeng He. Dynamic generation
of personalities with large language models. arXiv preprint arXiv:2404.07084, 2024a.
[226] Songyuan Liu, Ziyang Zhang, Runze Yan, Wei Wu, Carl Yang, and Jiaying Lu. Measuring spiritual values and
bias of large language models. arXiv preprint arXiv:2410.11647, 2024b.
[227] Xuan Liu, Jie Zhang, Song Guo, Haoyang Shang, Chengxu Yang, and Quanyan Zhu. Exploring prosocial
irrationality for llm agents: A social cognition view, 2024c.
[228] Xuelin Liu, Yanfei Zhu, Shucheng Zhu, Pengyuan Liu, Ying Liu, and Dong Yu. Evaluating moral beliefs across
llms through a pluralistic framework. In Findings of the Association for Computational Linguistics: EMNLP
2024, pages 4740–4760, 2024d.
[229] Yu Liu, Su Blodgett, Jackie Chi Kit Cheung, Vera Liao, Alexandra Olteanu, and Ziang Xiao. Ecbd: Evidence-
centered benchmark design for nlp. In Proceedings of the 62nd Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), pages 16349–16365, 2024e.
[230] John C Loehlin. Latent variable models: An introduction to factor, path, and structural equation analysis.
Psychology Press, 2004.
[231] Lea Löhn, Niklas Kiehne, Alexander Ljapunov, and Wolf-Tilo Balke.
Is machine psychology here? on
requirements for using human psychological tests on large language models. In Proceedings of the 17th
International Natural Language Generation Conference, pages 230–242, 2024.
[232] Anthony A Long and David N Sedley. The Hellenistic philosophers: Volume 2, Greek and Latin texts with notes
and bibliography. Cambridge University Press, 1987.
[233] Nunzio Lorè, A. Ilami, and Babak Heydari. Large model strategic thinking, small model efficiency: Transferring
theory of mind in large language models, 2024.
44

--- Page 45 ---

[234] Yang Lu, Jordan Yu, and Shou-Hsuan Stephen Huang. Illuminating the black box: A psychometric investigation
into the multifaceted nature of large language models. arXiv preprint arXiv:2312.14202, 2023.
[235] Yaojia Lv, Haojie Pan, Zekun Wang, Jiafeng Liang, Yuanxing Liu, Ruiji Fu, Ming Liu, Zhongyuan Wang, and
Bing Qin. Coggpt: Unleashing the power of cognitive dynamics on large language models. In Findings of the
Association for Computational Linguistics: EMNLP 2024, pages 6074–6091, 2024.
[236] Bolei Ma, Xinpeng Wang, Tiancheng Hu, Anna-Carolina Haensch, Michael Hedderich, Barbara Plank, and
Frauke Kreuter. The potential and challenges of evaluating attitudes, opinions, and values in large language
models. In Findings of the Association for Computational Linguistics: EMNLP 2024, pages 8783–8805, 2024a.
[237] Bolei Ma, Berk Yoztyurk, Anna-Carolina Haensch, Xinpeng Wang, Markus Herklotz, Frauke Kreuter, Barbara
Plank, and Matthias Assenmacher. Algorithmic fidelity of large language models in generating synthetic german
public opinions: A case study. arXiv preprint arXiv:2412.13169, 2024b.
[238] Huanhuan Ma, Haisong Gong, Xiaoyuan Yi, Xing Xie, and Dongkuan Xu. Leveraging implicit sentiments:
Enhancing reliability and validity in psychological trait evaluation of llms. arXiv preprint arXiv:2503.20182,
2025.
[239] Ziqiao Ma, Jacob Sansom, Run Peng, and Joyce Chai. Towards a holistic landscape of situated theory of mind in
large language models, 2023.
[240] Olivia Macmillan-Scott and Mirco Musolesi. (ir)rationality and cognitive biases in large language models. Royal
Society Open Science, 11(6):240255, 2024.
[241] Simon Malberg, Roman Poletukhin, Carolin M Schuster, and Georg Groh. A comprehensive evaluation of
cognitive biases in llms. arXiv preprint arXiv:2410.15413, 2024.
[242] Shengyu Mao, Xiaohan Wang, Mengru Wang, Yong Jiang, Pengjun Xie, Fei Huang, and Ningyu Zhang. Editing
personality for large language models. In CCF International Conference on Natural Language Processing and
Chinese Computing, pages 241–254. Springer, 2024a.
[243] Yuanyuan Mao, Shuang Liu, Qin Ni, Xin Lin, and Liang He. A review on machine theory of mind, 2024b.
[244] Keith A Markus and Denny Borsboom. Frontiers of test validity theory: Measurement, causation, and meaning.
Routledge, 2013.
[245] Giovanni Marraffini, Andrés Cotton, Noe Hsueh, Axel Fridman, Juan Wisznia, and Luciano Corro. The greatest
good benchmark: Measuring llms’ alignment with utilitarian moral dilemmas. In Proceedings of the 2024
Conference on Empirical Methods in Natural Language Processing, pages 21950–21959, 2024.
[246] Leena Mathur, Paul Pu Liang, and Louis-Philippe Morency. Advancing social intelligence in ai agents: Technical
challenges and open questions, 2024.
[247] Timothy R McIntosh, Teo Susnjak, Nalin Arachchilage, Tong Liu, Paul Watters, and Malka N Halgamuge.
Inadequacies of large language model benchmarks in the era of generative artificial intelligence. arXiv preprint
arXiv:2402.09880, 2024.
[248] Gwenyth Isobel Meadows, Nicholas Wai Long Lau, Eva Adelina Susanto, Chi Lok Yu, and Aditya Paul.
Localvaluebench: A collaboratively built and extensible benchmark for evaluating localized value alignment and
ethical safety in large language models. arXiv preprint arXiv:2408.01460, 2024.
[249] Mijntje Meijer, Hadi Mohammadi, and Ayoub Bagheri. Llms as mirrors of societal moral standards: reflection of
cultural divergence and agreement across ethical topics. arXiv preprint arXiv:2412.00962, 2024.
[250] Alessio Miaschi, Felice Dell’Orletta, and Giulia Venturi. Evaluating large language models via linguistic
profiling. In Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing, pages
2835–2848, 2024.
[251] Silvia Milano, Joshua A McGrane, and Sabina Leonelli. Large language models challenge the future of higher
education. Nature Machine Intelligence, 5(4):333–334, 2023.
[252] Marilù Miotto, Nicola Rossberg, and Bennett Kleinberg. Who is gpt-3? an exploration of personality, values and
demographics. In Proceedings of the fifth workshop on Natural Language Processing and Computational Social
Science (NLP+ CSS), pages 218–227. Association for Computational Linguistics, 2022.
45

--- Page 46 ---

[253] Robert J Mislevy, Russell G Almond, and Janice F Lukas. A brief introduction to evidence-centered design. ETS
Research Report Series, 2003(1):i–29, 2003.
[254] J. Mittelstädt, Julia Maier, P. Goerke, Frank Zinn, and Michael Hermes. Large language models can outperform
humans in social situational judgments, 2024.
[255] Shima Rahimi Moghaddam and C. Honey. Boosting theory-of-mind performance in large language models via
prompting, 2023.
[256] Ida Momennejad, Hosein Hasanbeig, Felipe Vieira Frujeri, Hiteshi Sharma, Nebojsa Jojic, Hamid Palangi, Robert
Ness, and Jonathan Larson. Evaluating cognitive maps and planning in large language models with cogeval.
Advances in Neural Information Processing Systems, 36:69736–69751, 2023.
[257] Jared Moore, Tanvi Deshpande, and Diyi Yang. Are large language models consistent over value-laden questions?
arXiv preprint arXiv:2407.02996, 2024.
[258] Xinyi Mou, Jingcong Liang, Jiayu Lin, Xinnong Zhang, Xiawei Liu, Shiyue Yang, Rong Ye, Lei Chen, Haoyu
Kuang, Xuanjing Huang, and Zhongyu Wei. Agentsense: Benchmarking social intelligence of language agents
through interactive scenarios, 2024.
[259] Simon Münker. Towards" differential ai psychology" and in-context value-driven statement alignment with
moral foundations theory. arXiv preprint arXiv:2408.11415, 2024.
[260] Ryan O Murphy, Kurt A Ackermann, and Michel JJ Handgraaf. Measuring social value orientation. Judgment
and Decision making, 6(8):771–781, 2011.
[261] Isabel Briggs Myers. A guide to the development and use of the Myers-Briggs type indicator: Manual. Consulting
Psychologists Press, 1985.
[262] Isabel Briggs Myers et al. The myers-briggs type indicator, volume 34. Consulting Psychologists Press Palo
Alto, CA, 1962.
[263] W Russell Neuman, Chad Coleman, and Manan Shah. Analyzing the ethical logic of six large language models.
arXiv preprint arXiv:2501.08951, 2025.
[264] Allen Newell. You can’t play 20 questions with nature and win: Projective comments on the papers of this
symposium. In William G. Chase, editor, Visual Information Processing, pages 283–308. Elsevier, 1973. doi: 10.
1016/B978-0-12-170150-5.50012-3. URL https://doi.org/10.1016/B978-0-12-170150-5.50012-3.
[265] Christian Nickel, Laura Schrewe, and Lucie Flek. Probing the robustness of theory of mind in large language
models, 2024.
[266] Animesh Nighojkar, Bekhzodbek Moydinboyev, My Duong, and John Licato. Giving ai personalities leads to
more human-like reasoning. arXiv preprint arXiv:2502.14155, 2025.
[267] Qian Niu, Junyu Liu, Ziqian Bi, Pohsun Feng, Benji Peng, Keyu Chen, and Ming Li. Large language models and
cognitive science: A comprehensive review of similarities, differences, and challenges, 2024.
[268] José Luiz Nunes, Guilherme FCF Almeida, Marcelo de Araujo, and Simone DJ Barbosa. Are large language
models moral hypocrites? a study based on moral foundations. In Proceedings of the AAAI/ACM Conference on
AI, Ethics, and Society, volume 7, pages 1074–1087, 2024.
[269] Takumi Ohashi, Tsubasa Nakagawa, and Hitoshi Iyatomi. Extended japanese commonsense morality dataset with
masked token and label enhancement. In Proceedings of the 33rd ACM International Conference on Information
and Knowledge Management, pages 3964–3968, 2024.
[270] OpenAI. Chatgpt, 2025. URL https://chat.openai.com. Accessed: 2025-05-01.
[271] William Orwig, Emma R Edenbaum, Joshua D Greene, and Daniel L Schacter. The language of creativity:
Evidence from humans and large language models. The Journal of creative behavior, 58(1):128–136, 2024.
[272] Samuel J Paech. Eq-bench: An emotional intelligence benchmark for large language models. arXiv preprint
arXiv:2312.06281, 2023.
46

--- Page 47 ---

[273] Keyu Pan and Yawen Zeng. Do llms possess a personality? making the mbti test an amazing evaluation for large
language models. arXiv preprint arXiv:2307.16180, 2023.
[274] Luiz Pasquali. Psychometrics. Revista da Escola de Enfermagem da USP, 43:992–999, 2009.
[275] Suketu C Patel and Jin Fan. Identification and description of emotions by current large language models. bioRxiv,
pages 2023–07, 2023.
[276] Delroy L Paulhus and Kevin M Williams. The dark triad of personality: Narcissism, machiavellianism, and
psychopathy. Journal of research in personality, 36(6):556–563, 2002.
[277] Siddhesh Pawar, Junyeong Park, Jiho Jin, Arnav Arora, Junho Myung, Srishti Yadav, Faiz Ghifari Haznitrama,
Inhwa Song, Alice Oh, and Isabelle Augenstein. Survey of cultural awareness in language models: Text and
beyond. arXiv preprint arXiv:2411.00860, 2024.
[278] Sanne Peereboom, Inga Schwabe, and Bennett Kleinberg. Cognitive phantoms in llms through the lens of latent
variables. arXiv preprint arXiv:2409.15324, 2024.
[279] Max Pellert, Clemens M Lechner, Claudia Wagner, Beatrice Rammstedt, and Markus Strohmaier. Ai psy-
chometrics: Assessing the psychological profiles of large language models through psychometric inventories.
Perspectives on Psychological Science, 19(5):808–826, 2024.
[280] Yujia Peng, Jiaheng Han, Zhenliang Zhang, Lifeng Fan, Tengyu Liu, Siyuan Qi, Xue Feng, Yuxi Ma, Yizhou
Wang, and Song-Chun Zhu. The tong test: Evaluating artificial general intelligence through dynamic embodied
physical and social interactions. Engineering, 34:12–22, 2024.
[281] James W Pennebaker, Martha E Francis, and Roger J Booth. Linguistic inquiry and word count: Liwc 2001.
Mahway: Lawrence Erlbaum Associates, 71(2001):2001, 2001.
[282] Andrew Peterson. What does ai consider praiseworthy? AI and Ethics, pages 1–25, 2025.
[283] Nikolay B Petrov, Gregory Serapio-García, and Jason Rentfrow. Limited ability of llms to simulate human
psychological behaviours: a psychometric analysis. arXiv preprint arXiv:2405.07248, 2024.
[284] Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li, Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang, Mohamed
Shaaban, John Ling, Sean Shi, et al. Humanity’s last exam. arXiv preprint arXiv:2501.14249, 2025.
[285] Zhiqiang Pi, Annapurna Vadaparty, Benjamin K. Bergen, and Cameron R. Jones. Dissecting the ullman variations
with a scalpel: Why do llms fail at trivial alterations to the false belief task?, 2024.
[286] David J Pittenger. Cautionary comments regarding the myers-briggs type indicator. Consulting Psychology
Journal: Practice and Research, 57(3):210, 2005.
[287] Felipe Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin. tinybench-
marks: evaluating llms with fewer examples. In Proceedings of the 41st International Conference on Machine
Learning, pages 34303–34326, 2024.
[288] Vladimir Ponizovskiy, Murat Ardag, Lusine Grigoryan, Ryan Boyd, Henrik Dobewall, and Peter Holtz. Develop-
ment and validation of the personal values dictionary: A theory–driven tool for investigating references to basic
human values in text. European Journal of Personality, 34(5):885–902, 2020.
[289] David Premack and Guy Woodruff. Does the chimpanzee have a theory of mind? Behavioral and brain sciences,
1(4):515–526, 1978.
[290] Laura Pérez-Mayos, Alba T’aboas Garc’ia, Simon Mille, and L. Wanner. Assessing the syntactic capabilities of
transformer-based multilingual language models, 2021.
[291] Weihong Qi, Hanjia Lyu, and Jiebo Luo. Representation bias in political sample simulations with large language
models. arXiv preprint arXiv:2407.11409, 2024.
[292] Zhuang Qiu, Xufeng Duan, and Zhenguang G. Cai. Evaluating grammatical well-formedness in large language
models: A comparative study with human judgments, 2024.
[293] Pinaki Raj. A literature review on emotional intelligence of large language models (llms). International Journal
of Advanced Research in Computer Science, 15(4), 2024.
47

--- Page 48 ---

[294] Aida Ramezani and Yang Xu. Knowledge of cultural moral norms in large language models. In The 61st Annual
Meeting Of The Association For Computational Linguistics, 2023.
[295] Leonardo Ranaldi and Fabio Massimo Zanzotto. Hans, are you clever? clever hans effect analysis of neural
systems. In Proceedings of the 13th Joint Conference on Lexical and Computational Semantics (* SEM 2024),
pages 314–325, 2024.
[296] Rajesh Ranjan, Shailja Gupta, and Surya Narayan Singh. A comprehensive survey of bias in llms: Current
landscape and future directions. arXiv preprint arXiv:2409.16430, 2024.
[297] Haocong Rao, Cyril Leung, and Chunyan Miao. Can chatgpt assess human personalities? a general evaluation
framework. arXiv preprint arXiv:2303.01248, 2023.
[298] Tenko Raykov and George A Marcoulides. Introduction to psychometric theory. Routledge, 2011.
[299] Yuanyi Ren, Haoran Ye, Hanjun Fang, Xin Zhang, and Guojie Song. Valuebench: Towards comprehensively
evaluating value orientations and understanding of large language models. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 2015–2040, 2024.
[300] Maor Reuben, Ortal Slobodin, Aviad Elyshar, Idan-Chaim Cohen, Orna Braun-Lewensohn, Odeya Cohen, and
Rami Puzis. Assessment and manipulation of latent constructs in pre-trained language models using psychometric
scales. arXiv preprint arXiv:2409.19655, 2024.
[301] Matthew Riemer, Zahra Ashktorab, Djallel Bouneffouf, Payel Das, Miao Liu, Justin D. Weisz, and Murray
Campbell. Position: Theory of mind benchmarks are broken for large language models, 2025. URL https:
//arxiv.org/abs/2412.19726.
[302] Giuseppe Riva, F. Mantovani, B. Wiederhold, Antonella Marchetti, and A. Gaggioli. Psychomatics - a multidisci-
plinary framework for understanding artificial minds, 2024.
[303] Sergey Rodionov, Zarathustra Amadeus Goertzel, and Ben Goertzel. An evaluation of gpt-4 on the ethics dataset.
arXiv preprint arXiv:2309.10492, 2023.
[304] Bernardino Romera-Paredes, Mohammadamin Barekatain, Alexander Novikov, Matej Balog, M Pawan Kumar,
Emilien Dupont, Francisco JR Ruiz, Jordan S Ellenberg, Pengming Wang, Omar Fawzi, et al. Mathematical
discoveries from program search with large language models. Nature, 625(7995):468–475, 2024.
[305] Peter Romero, Stephen Fitz, and Teruo Nakatsuma. Do gpt language models suffer from split personality
disorder? the advent of substrate-free psychometrics. arXiv preprint arXiv:2408.07377, 2024.
[306] Hannes Rosenbusch, Claire E Stevenson, and Han LJ van der Maas. How accurate are gpt-3’s hypotheses about
social science phenomena? Digital Society, 2(2):26, 2023.
[307] Paul Röttger, Valentin Hofmann, Valentina Pyatkin, Musashi Hinck, Hannah Rose Kirk, Hinrich Schütze, and
Dirk Hovy. Political compass or spinning arrow? towards more meaningful evaluations for values and opinions
in large language models. arXiv preprint arXiv:2402.16786, 2024.
[308] Paul Röttger, Musashi Hinck, Valentin Hofmann, Kobi Hackenburg, Valentina Pyatkin, Faeze Brahman, and
Dirk Hovy. Issuebench: Millions of realistic prompts for measuring issue bias in llm writing assistance. arXiv
preprint arXiv:2502.08395, 2025.
[309] David Rozado. The political biases of chatgpt. Social Sciences, 12(3):148, 2023.
[310] Naama Rozen, Liat Bezalel, Gal Elidan, Amir Globerson, and Ella Daniel. Do llms have consistent values?
arXiv preprint arXiv:2407.12878, 2024.
[311] Laura Ruis, Akbir Khan, Stella Biderman, Sara Hooker, Tim Rocktäschel, and Edward Grefenstette. The
goldilocks of pragmatic understanding: fine-tuning strategy matters for implicature resolution by llms. Advances
in Neural Information Processing Systems, 36:20827–20905, 2023.
[312] John Rust and Susan Golombok. Modern psychometrics: The science of psychological assessment. Routledge,
2014.
[313] Jérôme Rutinowski, Sven Franke, Jan Endendyk, Ina Dormuth, Moritz Roidl, and Markus Pauly. The self-
perception and political biases of chatgpt. Human Behavior & Emerging Technologies, 2024.
48

--- Page 49 ---

[314] Sahand Sabour, Siyang Liu, Zheyuan Zhang, June Liu, Jinfeng Zhou, Alvionna Sunaryo, Tatia Lee, Rada
Mihalcea, and Minlie Huang. Emobench: Evaluating the emotional intelligence of large language models. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 5986–6004, 2024.
[315] Pratik S Sachdeva and Tom van Nuenen. Normative evaluation of large language models with everyday moral
dilemmas. arXiv preprint arXiv:2501.18081, 2025.
[316] Jayanta Sadhu, Ayan Antik Khan, Noshin Nawal, Sanju Basak, Abhik Bhattacharjee, and Rifat Shahriyar.
Multi-tom: Evaluating multilingual theory of mind capabilities in large language models, 2024.
[317] Payam Saeedi, Mahsa Goodarzi, and M Abdullah Canbaz. Heuristics and biases in ai decision-making: Implica-
tions for responsible agi, 2025. URL https://arxiv.org/abs/2410.02820.
[318] Aadesh Salecha, Molly E Ireland, Shashanka Subrahmanya, João Sedoc, Lyle H Ungar, and Johannes C
Eichstaedt. Large language models show human-like social desirability biases in survey responses. arXiv preprint
arXiv:2405.06058, 2024.
[319] Peter Salovey and John D Mayer. Emotional intelligence. Imagination, cognition and personality, 9(3):185–211,
1990.
[320] Nathan E Sanders, Alex Ulinich, and Bruce Schneier. Demonstrations of the potential of ai-based political issue
polling. arXiv preprint arXiv:2307.04781, 2023.
[321] Shibani Santurkar, Esin Durmus, Faisal Ladhak, Cinoo Lee, Percy Liang, and Tatsunori Hashimoto. Whose
opinions do language models reflect? In International Conference on Machine Learning, pages 29971–30004.
PMLR, 2023.
[322] Maarten Sap, Ronan Le Bras, Daniel Fried, and Yejin Choi. Neural theory-of-mind? on the limits of social
intelligence in large lms, 2022.
[323] Sneheel Sarangi, Maha Elgarf, and Hanan Salam. Decompose-tom: Enhancing theory of mind reasoning in large
language models through simulation and task decomposition, 2025.
[324] Karahan Sarıta¸s, Kıvanç Tezören, and Yavuz Durmazkeser. A systematic review on the evaluation of large
language models in theory of mind tasks. arXiv preprint arXiv:2502.08796, 2025.
[325] Giuseppe Sartori and G. Orrú. Language models and psychological sciences, 2023.
[326] Kristina Schaaff, Caroline Reinig, and Tim Schlippe. Exploring chatgpt’s empathic abilities. In 2023 11th
international conference on affective computing and intelligent interaction (ACII), pages 1–8. IEEE, 2023.
[327] Julian Schelb, Orr Borin, David Garcia, and Andreas Spitz. Ru psycho? robust unified psychometric testing of
language models. arXiv preprint arXiv:2503.10229, 2025.
[328] Nino Scherrer, Claudia Shi, Amir Feder, and David Blei. Evaluating the moral beliefs encoded in llms. Advances
in Neural Information Processing Systems, 36:51778–51809, 2023.
[329] Philipp Schoenegger, Francesco Salvi, Jiacheng Liu, Xiaoli Nan, Ramit Debnath, Barbara Fasolo, Evelina
Leivada, Gabriel Recchia, Fritz Günther, Ali Zarifhonarvar, et al. Large language models are more persuasive
than incentivized human persuaders. arXiv preprint arXiv:2505.09662, 2025.
[330] Florian Scholten, Tobias R Rebholz, and Mandy Hütter. Metacognitive myopia in large language models. arXiv
preprint arXiv:2408.05568, 2024.
[331] Luca M Schulze Buschoff, Elif Akata, Matthias Bethge, and Eric Schulz. Visual cognition in multimodal large
language models. Nature Machine Intelligence, pages 1–11, 2025.
[332] Shalom H Schwartz. Universals in the content and structure of values: Theoretical advances and empirical tests
in 20 countries. In Advances in experimental social psychology, volume 25, pages 1–65. Elsevier, 1992.
[333] Shalom H Schwartz, Gila Melech, Arielle Lehmann, Steven Burgess, Mari Harris, and Vicki Owens. Extending
the cross-cultural validity of the theory of basic human values with a different method of measurement. Journal
of cross-cultural psychology, 32(5):519–542, 2001.
49

--- Page 50 ---

[334] Melanie Sclar, Sachin Kumar, Peter West, Alane Suhr, Yejin Choi, and Yulia Tsvetkov. Minding language
models’ (lack of) theory of mind: A plug-and-play multi-character belief tracker, 2023.
[335] Melanie Sclar, Jane Yu, Maryam Fazel-Zarandi, Yulia Tsvetkov, Yonatan Bisk, Yejin Choi, and Asli Celikyilmaz.
Explore theory of mind: Program-guided adversarial data generation for theory of mind reasoning, 2024.
[336] SM Seals and Valerie Shalin. Long-form analogies generated by chatgpt lack human-like psycholinguistic
properties. In Proceedings of the Annual Meeting of the Cognitive Science Society, volume 45, 2023.
[337] Greg Serapio-García, Mustafa Safdari, Clément Crepy, Luning Sun, Stephen Fitz, Peter Romero, Marwa
Abdulhai, Aleksandra Faust, and Maja Matari´c. Personality traits in large language models. arXiv preprint
arXiv:2307.00184, 2023.
[338] Avner Seror. The moral mind (s) of large language models. arXiv preprint arXiv:2412.04476, 2024.
[339] Raj Sanjay Shah, Khushi Bhardwaj, and Sashank Varma. Development of cognitive intelligence in pre-trained
language models. arXiv preprint arXiv:2407.01047, 2024.
[340] Ammar Shaikh, Raj Abhijit Dandekar, Sreedath Panat, and Rajat Dandekar. Cbeval: A framework for evaluating
and interpreting cognitive biases in llms. arXiv preprint arXiv:2412.03605, 2024.
[341] Natalie Shapira, Mosh Levy, S. Alavi, Xuhui Zhou, Yejin Choi, Yoav Goldberg, Maarten Sap, and Vered Shwartz.
Clever hans or neural theory of mind? stress testing social reasoning in large language models, 2023a.
[342] Natalie Shapira, Guy Zwirn, and Yoav Goldberg. How well do large language models perform on faux pas tests?,
2023b.
[343] Ashish Sharma, Inna W Lin, Adam S Miner, David C Atkins, and Tim Althoff. Towards facilitating empathic
conversations in online mental health support: A reinforcement learning approach. In Proceedings of the web
conference 2021, pages 194–205, 2021.
[344] Hua Shen, Tiffany Knearem, Reshmi Ghosh, Yu-Ju Yang, Tanushree Mitra, and Yun Huang. Valuecompass: A
framework of fundamental values for human-ai alignment. arXiv preprint arXiv:2409.09586, 2024.
[345] Kazutoshi Shinoda, Nobukatsu Hojo, Kyosuke Nishida, Saki Mizuno, Keita Suzuki, Ryo Masumura, Hiroaki
Sugiyama, and Kuniko Saito. Tomato: Verbalizing the mental states of role-playing llms for benchmarking theory
of mind, 2025.
[346] Bangzhao Shu, Lechen Zhang, Minje Choi, Lavinia Dunagan, Lajanugen Logeswaran, Moontae Lee, Dallas
Card, and David Jurgens. You don’t need a personality test to know these models are unreliable: Assessing the
reliability of large language models on psychometric instruments. In Proceedings of the 2024 Conference of
the North American Chapter of the Association for Computational Linguistics: Human Language Technologies
(Volume 1: Long Papers), pages 5263–5281, 2024.
[347] David Silver and Richard S Sutton. Welcome to the era of experience. Google AI, 2025.
[348] Gabriel Simmons. Moral mimicry: Large language models produce moral rationalizations tailored to political
identity. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 4:
Student Research Workshop), pages 282–297, 2023.
[349] Herbert A. Simon. A theory of emotional behaviour. Working Paper 55, CIP (Complex Information Processing
Project), 1963. URL https://digitalcollections.library.cmu.edu/node/1087.
[350] Karan Singhal, Shekoofeh Azizi, Tao Tu, S Sara Mahdavi, Jason Wei, Hyung Won Chung, Nathan Scales, Ajay
Tanwani, Heather Cole-Lewis, Stephen Pfohl, et al. Large language models encode clinical knowledge. Nature,
620(7972):172–180, 2023.
[351] Ewa Skimina, Jan Cieciuch, and William Revelle. Between-and within-person structures of value traits and value
states: Four different structures, four different interpretations. Journal of Personality, 89(5):951–969, 2021.
[352] Wei Song, Yadong Li, Jianhua Xu, Guowei Wu, Lingfeng Ming, Kexin Yi, Weihua Luo, Houyi Li, Yi Du, Fangda
Guo, and Kaicheng yu. M3gia: A cognition inspired multilingual and multimodal general intelligence ability
benchmark, 2024a.
50

--- Page 51 ---

[353] Xiaoyang Song, Akshat Gupta, Kiyan Mohebbizadeh, Shujie Hu, and Anant Singh. Have large language models
developed a personality?: Applicability of self-assessment tests in measuring personality in llms. arXiv preprint
arXiv:2305.14693, 2023.
[354] Xiaoyang Song, Yuta Adachi, Jessie Feng, Mouwei Lin, Linhao Yu, Frank Li, Akshat Gupta, Gopala Anu-
manchipalli, and Simerjot Kaur. Identifying multiple personalities in large language models with external
evaluation. arXiv preprint arXiv:2402.14805, 2024b.
[355] Taylor Sorensen, Liwei Jiang, Jena D Hwang, Sydney Levine, Valentina Pyatkin, Peter West, Nouha Dziri,
Ximing Lu, Kavel Rao, Chandra Bhagavatula, et al. Value kaleidoscope: Engaging ai with pluralistic human
values, rights, and duties. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages
19937–19947, 2024a.
[356] Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar Mireshghallah, Christopher Michael
Rytting, Andre Ye, Liwei Jiang, Ximing Lu, Nouha Dziri, et al. Position: a roadmap to pluralistic alignment. In
Proceedings of the 41st International Conference on Machine Learning, pages 46280–46302, 2024b.
[357] Taylor Sorensen, Pushkar Mishra, Roma Patel, Michael Henry Tessler, Michiel Bakker, Georgina Evans, Iason
Gabriel, Noah Goodman, and Verena Rieser. Value profiles for encoding human variation. arXiv preprint
arXiv:2503.15484, 2025.
[358] Vera Sorin, Dana Brin, Yiftach Barash, Eli Konen, Alexander Charney, Girish Nadkarni, and Eyal Klang. Large
language models and empathy: Systematic review. Journal of Medical Internet Research, 26:e52597, 2024.
[359] Christopher J Soto and Oliver P John. The next big five inventory (bfi-2): Developing and assessing a hierarchical
model with 15 facets to enhance bandwidth, fidelity, and predictive power. Journal of personality and social
psychology, 113(1):117, 2017.
[360] Ondrej Sotolar, Vojtech Formanek, Alok Debnath, Allison Lahnala, Charles Welch, and Lucie FLek. Empo:
Emotion grounding for empathetic response generation through preference optimization.
arXiv preprint
arXiv:2406.19071, 2024.
[361] Adil Soubki, John Murzaku, Arash Yousefi Jordehi, Peter Zeng, Magdalena Markowska, S. Mirroshandel, and
Owen Rambow. Views are my own, but also yours: Benchmarking theory of mind using common ground, 2024.
[362] Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao, Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch, Adam R
Brown, Adam Santoro, Aditya Gupta, Adrià Garriga-Alonso, et al. Beyond the imitation game: Quantifying and
extrapolating the capabilities of language models. Transactions on Machine Learning Research, 2022.
[363] Julius Steuer, Marius Mosbach, and D. Klakow. Large gpt-like models are bad babies: A closer look at the
relationship between linguistic competence and psycholinguistic measures, 2023.
[364] Claire Stevenson, Iris Smal, Matthijs Baas, Raoul Grasman, and Han van der Maas. Putting gpt-3’s creativity to
the (alternative uses) test. arXiv preprint arXiv:2206.08932, 2022.
[365] James W. A. Strachan, Dalila Albergo, Giulia Borghini, Oriana Pansardi, E. Scaliti, Saurabh Gupta, Krati Saxena,
Alessandro Rufo, Stefano Panzeri, Guido Manzi, Michael S. A. Graziano, and Cristina Becchio. Testing theory
of mind in large language models and humans, 2024a.
[366] James W. A. Strachan, Oriana Pansardi, E. Scaliti, Marco Celotto, Krati Saxena, Chunzhi Yi, Fabio Manzi,
Alessandro Rufo, Guido Manzi, Michael S. A. Graziano, Stefano Panzeri, and Cristina Becchio. Gpt-4o reads the
mind in the eyes, 2024b.
[367] Winnie Street, John Oliver Siy, Geoff Keeling, Adrien Baranes, Benjamin Barnett, Michael McKibben, Tatenda
Kanyere, Alison Lentz, B. A. Y. Arcas, and Robin I. M. Dunbar. Llms achieve adult human performance on
higher-order theory of mind tasks, 2024.
[368] Joseph Suh, Erfan Jahanparast, Suhong Moon, Minwoo Kang, and Serina Chang. Language model fine-tuning
on scaled survey data for predicting distributions of public opinions. arXiv preprint arXiv:2502.16761, 2025.
[369] Tom Sühr, Florian E Dorner, Samira Samadi, and Augustin Kelava. Challenging the validity of personality tests
for large language models. Preprint at arXiv. arXiv-2311 https://doi. org/10.48550/arXiv, 2311, 2023.
[370] Yasuaki Sumita, Koh Takeuchi, and Hisashi Kashima. Cognitive biases in large language models: A survey and
mitigation experiments. arXiv preprint arXiv:2412.00323, 2024.
51

--- Page 52 ---

[371] Kun Sun and Rong Wang. Computational sentence-level metrics predicting human sentence comprehension,
2024.
[372] Seungjong Sun, Eungu Lee, Dongyan Nan, Xiangying Zhao, Wonbyung Lee, Bernard J Jansen, and Jang Hyun
Kim. Random silicon sampling: Simulating human sub-population opinion using a large language model based
on group-level demographic information. arXiv preprint arXiv:2402.18144, 2024.
[373] Sowmya S Sundaram and Balaji Alwar. Can a hallucinating model help in reducing human" hallucination"?
arXiv preprint arXiv:2405.00843, 2024.
[374] Kazuhiro Takemoto. The moral machine experiment on large language models. Royal Society open science, 11
(2):231393, 2024.
[375] Masashi Takeshita, Rafal Rzpeka, and Kenji Araki. Jcommonsensemorality: Japanese dataset for evaluating
commonsense morality understanding. In In Proceedings of The Twenty Nineth Annual Meeting of The Association
for Natural Language Processing (NLP2023), pages 357–362, 2023.
[376] Alaina N Talboy and Elizabeth Fuller. Challenging the appearance of machine intelligence: Cognitive bias in
llms and best practices for adoption. arXiv preprint arXiv:2304.01358, 2023.
[377] Fiona Anting Tan, Gerard Christopher Yeo, Kokil Jaidka, Fanyou Wu, Weijie Xu, Vinija Jain, Aman Chadha,
Yang Liu, and See-Kiong Ng. Phantom: Persona-based prompting has an effect on theory-of-mind reasoning in
large language models. arXiv preprint arXiv:2403.02246, 2024.
[378] Weizhi Tang and Vaishak Belle. Tom-lm: Delegating theory of mind reasoning to external symbolic executors in
large language models, 2024.
[379] Zhisheng Tang and Mayank Kejriwal. Humanlike cognitive patterns as emergent phenomena in large language
models. arXiv preprint arXiv:2412.15501, 2024.
[380] Kumar Tanmay, Aditi Khandelwal, Utkarsh Agarwal, and Monojit Choudhury. Probing the moral development
of large language models through defining issues test. arXiv preprint arXiv:2309.13356, 2023.
[381] Robert L Thorndike and Saul Stein. An evaluation of the attempts to measure social intelligence. Psychological
bulletin, 34(5):275, 1937.
[382] David Thorstad. Cognitive bias in large language models: Cautious optimism meets anti-panglossian meliorism.
arXiv preprint arXiv:2311.10932, 2023.
[383] Yufei Tian, Tenghao Huang, Miri Liu, Derek Jiang, Alexander Spangher, Muhao Chen, Jonathan May, and
Nanyun Peng. Are large language models capable of generating human-level narratives? In Proceedings of the
2024 Conference on Empirical Methods in Natural Language Processing, pages 17659–17681, 2024.
[384] Lindia Tjuatja, Valerie Chen, Tongshuang Wu, Ameet Talwalkwar, and Graham Neubig. Do llms exhibit
human-like response biases? a case study in survey design. Transactions of the Association for Computational
Linguistics, 12:1011–1026, 2024.
[385] Alejandro Tlaie.
Exploring and steering the moral compass of large language models.
arXiv preprint
arXiv:2405.17345, 2024.
[386] E Paul Torrance. Torrance tests of creative thinking. Educational and psychological measurement, 1966.
[387] Sang Truong, Yuheng Tu, Percy Liang, Bo Li, and Sanmi Koyejo. Reliable and efficient amortized model-based
evaluation. arXiv preprint arXiv:2503.13335, 2025.
[388] Amos Tversky and Daniel Kahneman. Judgment under uncertainty: Heuristics and biases: Biases in judgments
reveal some heuristics of thinking under uncertainty. science, 185(4157):1124–1131, 1974.
[389] T. Ullman. Large language models fail on trivial alterations to theory-of-mind tasks, 2023.
[390] Max J. van Duijn, Bram van Dijk, Tom Kouwenhoven, Werner de Valk, M. Spruit, and P. V. D. Putten. Theory of
mind in large language models: Examining performance of 11 state-of-the-art models vs. children aged 7-10 on
advanced tests, 2023.
52

--- Page 53 ---

[391] LaurÃL, ne Vaugrante, Mathias Niepert, and Thilo Hagendorff. A looming replication crisis in evaluating behavior
in language models? evidence and solutions. arXiv preprint arXiv:2409.20303, 2024.
[392] Karina Vida, Fabian Damken, and Anne Lauscher. Decoding multilingual moral preferences: Unveiling llm’s
biases through the moral machine experiment. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and
Society, volume 7, pages 1490–1501, 2024.
[393] Leah von der Heyde, Anna-Carolina Haensch, and Alexander Wenz. Vox populi, vox ai? using language models
to estimate german public opinion. arXiv preprint arXiv:2407.08563, 2024.
[394] Huy Vu, Huy Anh Nguyen, Adithya V Ganesan, Swanie Juhng, Oscar NE Kjell, Joao Sedoc, Margaret L Kern,
Ryan L Boyd, Lyle Ungar, H Andrew Schwartz, et al. Psychadapter: Adapting llm transformers to reflect traits,
personality and mental health. arXiv preprint arXiv:2412.16882, 2024.
[395] Gleb D Vzorinab, Alexey M Bukinichac, Anna V Sedykha, Irina I Vetrovab, and Elena A Sergienkob. The
emotional intelligence of the gpt-4 large language model. Psychology in Russia: State of the art, 17(2):85–99,
2024.
[396] Hanna Wallach, Meera Desai, A Feder Cooper, Angelina Wang, Chad Atalla, Solon Barocas, Su Lin Blodgett,
Alexandra Chouldechova, Emily Corvi, P Alex Dow, et al. Position: Evaluating generative ai systems is a social
science measurement challenge. arXiv preprint arXiv:2502.00561, 2025.
[397] Yixin Wan and Kai-Wei Chang. White men lead, black women help? benchmarking language agency social
biases in llms. arXiv preprint arXiv:2404.10508, 2024.
[398] Angelina Wang, Jamie Morgenstern, and John P Dickerson. Large language models that replace human
participants can harmfully misportray and flatten identity groups. Nature Machine Intelligence, pages 1–12,
2025a.
[399] Chenxu Wang, Bin Dai, Huaping Liu, and Baoyuan Wang. Towards objectively benchmarking social intelligence
of language agents at the action level. In Findings of the Association for Computational Linguistics ACL 2024,
pages 8885–8897, 2024a.
[400] Daphne Wang, M. Sadrzadeh, Milos Stanojevic, Wing-Yee Chow, and Richard Breheny. How can large language
models become more human?, 2024b.
[401] Liang Wang, Nan Yang, Xiaolong Huang, Linjun Yang, Rangan Majumder, and Furu Wei. Large search model:
Redefining search stack in the era of llms. In ACM SIGIR Forum, volume 57, pages 1–16. ACM New York, NY,
USA, 2024c.
[402] Ruiyi Wang, Haofei Yu, Wenxin Zhang, Zhengyang Qi, Maarten Sap, Yonatan Bisk, Graham Neubig, and Hao
Zhu. Sotopia-π: Interactive learning of socially intelligent language agents. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 12912–12940, 2024d.
[403] Shuo Wang, Renhao Li, Xi Chen, Yulin Yuan, Derek F Wong, and Min Yang. Exploring the impact of personality
traits on llm bias and toxicity. arXiv preprint arXiv:2502.12566, 2025b.
[404] Xinglin Wang, Peiwen Yuan, Shaoxiong Feng, Yiwei Li, Boyuan Pan, Heda Wang, Yao Hu, and Kan Li. Coglm:
Tracking cognitive development of large language models, 2024e.
[405] Xintao Wang, Yunze Xiao, Jen-tse Huang, Siyu Yuan, Rui Xu, Haoran Guo, Quan Tu, Yaying Fei, Ziang
Leng, Wei Wang, et al. Incharacter: Evaluating personality fidelity in role-playing agents through psychological
interviews. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume
1: Long Papers), pages 1840–1873, 2024f.
[406] Xiting Wang, Liming Jiang, Jose Hernandez-Orallo, David Stillwell, Luning Sun, Fang Luo, and Xing Xie.
Evaluating general-purpose ai with psychometrics. arXiv preprint arXiv:2310.16379, 2023a.
[407] Xuena Wang, Xueting Li, Zi Yin, Yue Wu, and Jia Liu. Emotional intelligence of large language models. Journal
of Pacific Rim Psychology, 17:18344909231213958, 2023b.
[408] Taylor W. Webb, K. Holyoak, and Hongjing Lu. Emergent analogical reasoning in large language models, 2022.
53

--- Page 54 ---

[409] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou,
et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information
processing systems, 35:24824–24837, 2022.
[410] Anuradha Welivita and Pearl Pu. Are large language models more empathetic than humans? arXiv preprint
arXiv:2406.05063, 2024.
[411] Yuchen Wen, Keping Bi, Wei Chen, Jiafeng Guo, and Xueqi Cheng. Evaluating implicit bias in large language
models by attacking from a psychometric perspective. arXiv preprint arXiv:2406.14023, 2024a.
[412] Zhiyuan Wen, Yu Yang, Jiannong Cao, Haoming Sun, Ruosong Yang, and Shuaiqi Liu. Self-assessment,
exhibition, and recognition: a review of personality in large language models. arXiv preprint arXiv:2406.17624,
2024b.
[413] Yixuan Weng, Shizhu He, Kang Liu, Shengping Liu, and Jun Zhao. Controllm: Crafting diverse personalities for
language models. arXiv preprint arXiv:2402.10151, 2024.
[414] Ethan Gotlieb Wilcox, P. Vani, and R. Levy. A targeted assessment of incremental processing in neural language
models and humans, 2021.
[415] Alex Wilf, Sihyun Shawn Lee, Paul Pu Liang, and Louis-Philippe Morency. Think twice: Perspective-taking
improves large language models’ theory-of-mind capabilities, 2023.
[416] Michael Wolfman, Donald Dunagan, Jonathan Brennan, and John Hale. Hierarchical syntactic structure in
human-like language models, 2024.
[417] Dustin Wright, Arnav Arora, Nadav Borenstein, Srishti Yadav, Serge Belongie, and Isabelle Augenstein.
Revealing fine-grained values and opinions in large language models. arXiv preprint arXiv:2406.19238, 2024.
[418] Junjie Wu, Mo Yu, Lemao Liu, D. Yeung, and Jie Zhou. Understanding llms’ fluid intelligence deficiency: An
analysis of the arc task, 2025.
[419] Patrick Y Wu, Jonathan Nagler, Joshua A Tucker, and Solomon Messing. Large language models can be used to
estimate the latent positions of politicians. arXiv preprint arXiv:2303.12057, 2023.
[420] Shengguang Wu, Shusheng Yang, Zhenglun Chen, and Qi Su. Rethinking pragmatics in large language models:
Towards open-ended evaluation and preference tuning. In Proceedings of the 2024 Conference on Empirical
Methods in Natural Language Processing, pages 22583–22599, 2024.
[421] Wei Xie, Shuoyoucheng Ma, Zhenhua Wang, Enze Wang, Kai Chen, Xiaobing Sun, and Baosheng Wang. Do
large language models truly grasp mathematics? an empirical exploration from cognitive psychology, 2024a.
URL https://arxiv.org/abs/2410.14979.
[422] Zhentao Xie, Jiabao Zhao, Yilei Wang, Jinxin Shi, Yanhong Bai, Xingjiao Wu, and Liang He. Mindscope: Ex-
ploring cognitive biases in large language models through multi-agent systems. arXiv preprint arXiv:2410.04452,
2024b.
[423] Guohai Xu, Jiayi Liu, Ming Yan, Haotian Xu, Jinghui Si, Zhuoran Zhou, Peng Yi, Xing Gao, Jitao Sang, Rong
Zhang, et al. Cvalues: Measuring the values of chinese large language models from safety to responsibility. arXiv
preprint arXiv:2307.09705, 2023.
[424] Hainiu Xu, Runcong Zhao, Lixing Zhu, Jinhua Du, and Yulan He. Opentom: A comprehensive benchmark for
evaluating theory-of-mind reasoning capabilities of large language models, 2024a.
[425] Hainiu Xu, Siya Qi, Jiazheng Li, Yuxiang Zhou, Jinhua Du, C. Catmur, and Yulan He. Enigmatom: Improve
llms’ theory-of-mind reasoning capabilities with neural knowledge base of entity states, 2025a.
[426] Ruoxi Xu, Hongyu Lin, Xianpei Han, Le Sun, and Yingfei Sun. Academically intelligent llms are not necessarily
socially intelligent, 2024b.
[427] Ruoxi Xu, Hongyu Lin, Xianpei Han, Jia Zheng, Weixiang Zhou, Le Sun, and Yingfei Sun. Large language
models often say one thing and do another. arXiv preprint arXiv:2503.07003, 2025b.
54

--- Page 55 ---

[428] Shanshan Xu, TYS Santosh, Yanai Elazar, Quirin Vogel, Barbara Plank, and Matthias Grabmair. Better aligned
with survey respondents or training data? unveiling political leanings of llms on us supreme court cases. arXiv
preprint arXiv:2502.18282, 2025c.
[429] Bei Yan, Jie Zhang, Zhiyuan Chen, Shiguang Shan, and Xilin Chen. Moralbench: A multimodal moral benchmark
for lvlms. arXiv preprint arXiv:2412.20718, 2024.
[430] Bo Yang, Jiaxian Guo, Yusuke Iwasawa, and Yutaka Matsuo. Large language models as theory of mind aware
generative agents with counterfactual reflection, 2025a.
[431] Kaiqi Yang, Hang Li, Yucheng Chu, Yuping Lin, Tai-Quan Peng, and Hui Liu. Unpacking political bias in large
language models: Insights across topic polarization. arXiv preprint arXiv:2412.16746, 2024.
[432] Shu Yang, Shenzhe Zhu, Liang Liu, Lijie Hu, Mengdi Li, and Di Wang. Exploring the personality traits of llms
through latent features steering, 2025b. URL https://arxiv.org/abs/2410.10863.
[433] Jing Yao, Xiaoyuan Yi, Yifan Gong, Xiting Wang, and Xing Xie. Value fulcra: Mapping large language models
to the multidimensional spectrum of basic human value. In Proceedings of the 2024 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 1:
Long Papers), pages 8754–8777, 2024.
[434] Jing Yao, Xiaoyuan Yi, Shitong Duan, Jindong Wang, Yuzhuo Bai, Muhua Huang, Peng Zhang, Tun Lu, Zhicheng
Dou, Maosong Sun, et al. Value compass leaderboard: A platform for fundamental and validated evaluation of
llms values. arXiv preprint arXiv:2501.07071, 2025a.
[435] Jing Yao, Xiaoyuan Yi, and Xing Xie. Clave: An adaptive framework for evaluating values of llm generated
responses. Advances in Neural Information Processing Systems, 37:58868–58900, 2025b.
[436] Shunyu Yao. The second half, 2025. URL https://ysymyth.github.io/The-Second-Half/. Accessed:
2025-05-01.
[437] Nicolas Yax, Hernán Anlló, and Stefano Palminteri. Studying and improving reasoning in humans and machines.
Communications Psychology, 2(1):51, 2024.
[438] Haoran Ye, Jiarui Wang, Zhiguang Cao, Federico Berto, Chuanbo Hua, Haeyeon Kim, Jinkyoo Park, and
Guojie Song. Reevo: Large language models as hyper-heuristics with reflective evolution. Advances in neural
information processing systems, 37:43571–43608, 2024.
[439] Haoran Ye, Yuhang Xie, Yuanyi Ren, Hanjun Fang, Xin Zhang, and Guojie Song. Measuring human and ai
values based on generative psychometrics with large language models. In Proceedings of the AAAI Conference
on Artificial Intelligence, volume 39, 2025a.
[440] Haoran Ye, Tianze Zhang, Yuhang Xie, Liyuan Zhang, Yuanyi Ren, Xin Zhang, and Guojie Song. Gen-
erative psycho-lexical approach for constructing value systems in large language models.
arXiv preprint
arXiv:2502.02444, 2025b.
[441] Lance Ying, Katherine M Collins, Lionel Wong, Ilia Sucholutsky, Ryan Liu, Adrian Weller, Tianmin Shu,
Thomas L Griffiths, and Joshua B Tenenbaum. On benchmarking human-like intelligence in machines. arXiv
preprint arXiv:2502.20502, 2025a.
[442] Zonghao Ying, Deyue Zhang, Zonglei Jing, Yisong Xiao, Quanchen Zou, Aishan Liu, Siyuan Liang, Xiangzheng
Zhang, Xianglong Liu, and Dacheng Tao. Reasoning-augmented conversation for multi-turn jailbreak attacks on
large language models. arXiv preprint arXiv:2502.11054, 2025b.
[443] Fangxu Yu, Lai Jiang, Shenyi Huang, Zhen Wu, and Xinyu Dai. Persuasivetom: A benchmark for evaluating
machine theory of mind in persuasive dialogues, 2025.
[444] Yiyao Yu, Junjie Wang, Yuxiang Zhang, Lin Zhang, Yujiu Yang, and Tetsuya Sakai. Ealm: Introducing
multidimensional ethical alignment in conversational information retrieval. In Proceedings of the Annual
International ACM SIGIR Conference on Research and Development in Information Retrieval in the Asia Pacific
Region, pages 32–39, 2023.
[445] Jiaqing Yuan, Pradeep K Murukannaiah, and Munindar P Singh. Right vs. right: Can llms make tough choices?
arXiv preprint arXiv:2412.19926, 2024.
55

--- Page 56 ---

[446] Amir Zadeh, Michael Chan, Paul Pu Liang, Edmund Tong, and Louis-Philippe Morency. Social-iq: A question
answering benchmark for artificial social intelligence, 2019.
[447] Yi Zeng, Hongpeng Lin, Jingwen Zhang, Diyi Yang, Ruoxi Jia, and Weiyan Shi. How johnny can persuade llms
to jailbreak them: Rethinking persuasion to challenge ai safety by humanizing llms. In Proceedings of the 62nd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 14322–14350,
2024a.
[448] Yifan Zeng. Quantifying risk propensities of large language models: Ethical focus and bias detection through
role-play. arXiv preprint arXiv:2411.08884, 2024.
[449] Zheni Zeng, Jiayi Chen, Huimin Chen, Yukun Yan, Yuxuan Chen, Zhenghao Liu, Zhiyuan Liu, and Maosong
Sun. Persllm: A personified training approach for large language models. arXiv preprint arXiv:2407.12393,
2024b.
[450] Zhongshen Zeng, Yinhong Liu, Yingjia Wan, Jingyao Li, Pengguang Chen, Jianbo Dai, Yuxuan Yao, Rongwu
Xu, Zehan Qi, Wanru Zhao, Linling Shen, Jianqiao Lu, Haochen Tan, Yukang Chen, Hao Zhang, Zhan Shi, Bailin
Wang, Zhijiang Guo, and Jiaya Jia. Mr-ben: A meta-reasoning benchmark for evaluating system-2 thinking in
llms, 2024c.
[451] Haoyang Zhang. Harnessing in-context learning for personality elicitation in large language models. In 2024 6th
International Conference on Frontier Technologies of Information and Computer (ICFTIC), pages 1521–1531.
IEEE, 2024.
[452] Jie Zhang, Dongrui Liu, Chen Qian, Ziyue Gan, Yong Liu, Yu Qiao, and Jing Shao. The better angels of machine
personality: How personality relates to llm safety. arXiv preprint arXiv:2407.12344, 2024a.
[453] Xin Zhang, Yuanyi Ren, and Guojie Song. Age-related value orientations in large language models (llms).
Innovation in Aging, 8(Supplement_1):1010–1010, 2024b.
[454] Zhaowei Zhang, Fengshuo Bai, Jun Gao, and Yaodong Yang. Valuedcg: Measuring comprehensive human value
understanding ability of language models. arXiv preprint arXiv:2310.00378, 2023a.
[455] Zhaowei Zhang, Ceyao Zhang, Nian Liu, Siyuan Qi, Ziqi Rong, Song-Chun Zhu, Shuguang Cui, and Yaodong
Yang. Heterogeneous value alignment evaluation for large language models. In AAAI-2024 Workshop on Public
Sector LLMs: Algorithmic and Sociotechnical Design, 2024c.
[456] Zheyuan Zhang, Jifan Yu, Juanzi Li, and Lei Hou. Exploring the cognitive knowledge structure of large language
models: An educational diagnostic assessment approach, 2023b.
[457] Zhining Zhang, Chuanyang Jin, Mung Yao Jia, and Tianmin Shu. Autotom: Automated bayesian inverse planning
and model discovery for open-ended theory of mind, 2025.
[458] Weixiang Zhao, Zhuojun Li, Shilong Wang, Yang Wang, Yulin Hu, Yanyan Zhao, Chen Wei, and Bing Qin.
Both matter: Enhancing the emotional intelligence of large language models without compromising the general
intelligence. In Findings of the Association for Computational Linguistics ACL 2024, pages 11157–11176, 2024.
[459] Yachao Zhao, Bo Wang, and Yan Wang. Explicit vs. implicit: Investigating social bias in large language models
through self-reflection. arXiv preprint arXiv:2501.02295, 2025a.
[460] Yue Zhao, Qingqing Gu, Xiaoyu Wang, Teng Chen, Zhonglin Jiang, Yong Chen, and Luo Ji. Fisminess: A finite
state machine based paradigm for emotional support conversations. arXiv preprint arXiv:2504.11837, 2025b.
[461] Jingyao Zheng, Xian Wang, Simo Hosio, Xiaoxian Xu, and Lik-Hang Lee. Lmlpa: Language model linguistic
personality assessment. Computational Linguistics, pages 1–41, 2025.
[462] Qishuai Zhong, Yike Yun, and Aixin Sun. Cultural value differences of llms: Prompt, language, and model size.
arXiv preprint arXiv:2407.16891, 2024.
[463] Jingyan Zhou, Minda Hu, Junan Li, Xiaoying Zhang, Xixin Wu, Irwin King, and Helen Meng. Rethinking
machine ethics–can llms perform moral reasoning through the lens of moral theories?
In Findings of the
Association for Computational Linguistics: NAACL 2024, pages 2227–2242, 2024a.
56

--- Page 57 ---

[464] Lexin Zhou, Lorenzo Pacchiardi, Fernando Martínez-Plumed, Katherine M Collins, Yael Moros-Daval, Seraphina
Zhang, Qinlin Zhao, Yitian Huang, Luning Sun, Jonathan E Prunty, et al. General scales unlock ai evaluation
with explanatory and predictive power. arXiv preprint arXiv:2503.06378, 2025.
[465] Pei Zhou, Aman Madaan, Srividya Pranavi Potharaju, Aditya Gupta, Kevin R. McKee, Ari Holtzman, J. Pujara,
Xiang Ren, Swaroop Mishra, Aida Nematzadeh, Shyam Upadhyay, and Manaal Faruqui. How far are large
language models from agents with theory-of-mind?, 2023a.
[466] Xuhui Zhou, Hao Zhu, Leena Mathur, Ruohong Zhang, Haofei Yu, Zhengyang Qi, Louis-Philippe Morency,
Yonatan Bisk, Daniel Fried, Graham Neubig, et al. Sotopia: Interactive evaluation for social intelligence in
language agents. In The Twelfth International Conference on Learning Representations, 2024b.
[467] Yuchen Zhou, Emmy Liu, Graham Neubig, and Leila Wehbe. Divergences between language models and human
brains, 2023b.
[468] Kaijie Zhu, Jindong Wang, Qinlin Zhao, Ruochen Xu, and Xing Xie. Dynamic evaluation of large language
models by meta probing agents. In International Conference on Machine Learning, pages 62599–62617. PMLR,
2024a.
[469] Minjun Zhu, Yixuan Weng, Linyi Yang, and Yue Zhang. Personality alignment of large language models. arXiv
preprint arXiv:2408.11779, 2024b.
[470] Wentao Zhu, Zhining Zhang, and Yizhou Wang. Language models represent beliefs of self and others, 2024c.
[471] Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Rui Lv, Zhenya Huang, Guanhao Zhao, Zheng Zhang,
Qingyang Mao, Shijin Wang, et al. Efficiently measuring the cognitive ability of llms: An adaptive testing
perspective. CoRR, 2023a.
[472] Yan Zhuang, Qi Liu, Yuting Ning, Weizhe Huang, Zachary A Pardos, Patrick C Kyllonen, Jiyun Zu, Qingyang
Mao, Rui Lv, Zhenya Huang, et al. From static benchmarks to adaptive testing: Psychometrics in ai evaluation.
arXiv preprint arXiv:2306.10512, 2023b.
[473] Caleb Ziems, William Held, Omar Shaikh, Jiaao Chen, Zhehao Zhang, and Diyi Yang. Can large language
models transform computational social science? Computational Linguistics, 50(1), 2024.
[474] Huiqi Zou, Pengda Wang, Zihan Yan, Tianjun Sun, and Ziang Xiao. Can llm" self-report"?: Evaluating the validity
of self-report scales in measuring personality design in llm-based chatbots. arXiv preprint arXiv:2412.00207,
2024.
57

```
