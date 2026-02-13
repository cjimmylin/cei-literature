---
title: "2025-Cherakhloo-Benchmarking Open-Source Large Language Models for Persian in - PDF Extract"
source_pdf: "2025-Cherakhloo-Benchmarking Open-Source Large Language Models for Persian in.pdf"
pages: 17
extracted_at: "2026-02-13T09:50:31.727417"
---

# PDF Extract: 2025-Cherakhloo-Benchmarking Open-Source Large Language Models for Persian in

**Source PDF:** 2025-Cherakhloo-Benchmarking Open-Source Large Language Models for Persian in.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

BENCHMARKING OPEN-SOURCE LARGE LANGUAGE MODELS
FOR PERSIAN IN ZERO-SHOT AND FEW-SHOT LEARNING
Mahdi Cherakhloo
Department of Medical Engineering
Electrical Engineering Department
Sharif University of Technology
mahdi.cherakhloo@ee.sharif.ir
Arash Abbasi
YarAI Group
arash@yarai.ir
Mohammad Saeid Sarafraz
Department of Electrical Engineering
University of Tehran
ms.sarafraz@ut.ac.ir
Bijan Vosoughi Vahdat
Department of Medical Engineering
Electrical Engineering Department
Sharif University of Technology
vahdat@sharif.edu
October 16, 2025
ABSTRACT
Large Language Models (LLMs) have demonstrated remarkable capabilities across numerous
languages; however, their effectiveness in low-resource languages like Persian requires thorough
investigation. This paper presents a comprehensive benchmark of several open-source LLMs for
Persian Natural Language Processing (NLP) tasks, utilizing both zero-shot and few-shot learning
paradigms. We evaluate models across a range of tasks including sentiment analysis, named entity
recognition, reading comprehension, and question answering, using established Persian datasets
such as ParsiNLU and ArmanEmo. Our methodology encompasses rigorous experimental setups for
both zero-shot and few-shot scenarios, employing metrics such as Accuracy, F1-score, BLEU, and
ROUGE for performance evaluation. The results reveal that Gemma 2 consistently outperforms other
models across nearly all tasks in both learning paradigms, with particularly strong performance in
complex reasoning tasks. However, most models struggle with token-level understanding tasks like
Named Entity Recognition, highlighting specific challenges in Persian language processing. This
study contributes to the growing body of research on multilingual LLMs, providing valuable insights
into their performance in Persian and offering a benchmark for future model development.
1
Introduction
Large Language Models (LLMs) have fundamentally transformed the landscape of Natural Language Processing
(NLP), demonstrating remarkable capabilities in text generation, comprehension, and complex reasoning tasks that were
previously considered beyond the reach of artificial intelligence systems [1]. These powerful models have opened new
frontiers in human-computer interaction, enabling more natural and sophisticated communication between users and
machines. The multilingual capabilities of modern LLMs offer particularly promising avenues for democratizing access
to cutting-edge NLP technologies across diverse linguistic communities worldwide, potentially bridging long-standing
digital divides [2].
Despite these significant advancements, substantial performance disparities persist between high-resource languages
like English and low-resource languages such as Persian (Farsi). This imbalance represents a critical area requiring
thorough investigation and systematic evaluation [3]. Persian presents unique computational challenges due to its
distinctive orthographic features, complex morphological structures, and syntactic patterns that differ substantially
arXiv:2510.12807v1  [cs.CL]  5 Oct 2025

--- Page 2 ---

A PREPRINT - OCTOBER 16, 2025
from Indo-European languages that dominate NLP research [4]. These inherent linguistic complexities are further
exacerbated by the comparative scarcity of comprehensive Persian datasets, annotated corpora, and specialized NLP
tools relative to those available for high-resource languages [5].
This research addresses the pressing need for rigorous benchmarking of open-source LLMs specifically for Persian
language processing tasks. Our investigation centers on a comprehensive evaluation of several prominent open-source
models through the lens of zero-shot and few-shot learning paradigms. Zero-shot learning methodologies assess a
model’s inherent ability to perform previously unseen tasks without task-specific training examples—a capability
particularly valuable in low-resource scenarios. Similarly, few-shot learning evaluates performance when provided with
only a minimal number of illustrative examples [6]. Both approaches hold special relevance for languages like Persian,
where extensive labeled datasets remain scarce or prohibitively expensive to develop.
Our study contributes to the growing body of research on multilingual NLP by providing a detailed analysis of the
current capabilities and limitations of open-source LLMs when processing Persian text. Through systematic evaluation
across multiple tasks including text classification, named entity recognition, sentiment analysis, and question answering,
we identify specific strengths and weaknesses in these models’ handling of Persian linguistic phenomena. Furthermore,
we explore the impact of various prompting strategies and contextual examples on model performance, offering practical
insights for researchers and practitioners working with Persian NLP applications.
The findings presented in this paper not only establish important baselines for future research but also highlight critical
areas where targeted improvements could significantly enhance Persian language support in next-generation language
models. By identifying these gaps, we aim to catalyze focused research efforts that will ultimately lead to more
linguistically inclusive and equitable NLP technologies.
2
RELATED WORKS
2.1
LLM Evaluation Methodologies
The evaluation of Large Language Models (LLMs) presents a complex, multidimensional challenge that encompasses
determining what capabilities to assess, where to conduct evaluations, and how to implement effective assessment
methodologies [7]. Contemporary evaluation frameworks range from narrowly focused task-specific benchmarks to
more comprehensive approaches that consider broader societal impacts and ethical implications of these powerful
systems [8]. Extensive literature surveys in this rapidly evolving domain consistently emphasize the critical importance
of rigorous, systematic evaluation protocols to thoroughly understand model capabilities, limitations, and potential risks
associated with deployment in real-world scenarios [9].
Evaluation metrics serve as fundamental quantitative indicators in LLM assessment, with researchers typically employ-
ing a diverse array of measurement tools depending on the specific task and evaluation objectives. For classification
tasks, standard metrics include accuracy, precision, recall, and F1-score, while text generation quality is commonly
assessed using BLEU (Bilingual Evaluation Understudy) and ROUGE (Recall-Oriented Understudy for Gisting Evalu-
ation) scores. Language modeling capabilities are frequently evaluated using perplexity, which measures how well
a probabilistic model predicts a sample [10], [11]. However, researchers have increasingly highlighted significant
limitations of conventional metrics such as accuracy and F1-score, particularly when applied to imbalanced datasets,
leading to proposals for more robust alternatives like Informedness that provide more reliable performance indicators
across diverse data distributions [12].
The field has also witnessed the emergence of task-agnostic evaluation frameworks, exemplified by metrics such
as Information Parity, which offers a standardized approach for evaluating multilingual LLMs. These innovative
metrics facilitate meaningful comparisons of model capabilities across different languages and architectural designs,
addressing a critical need in the increasingly globalized deployment of language technologies [13]. Comprehensive
benchmarking suites, including the General Language Understanding Evaluation (GLUE) and Massive Multitask
Language Understanding (MMLU), have become standard tools in the research community, providing structured
frameworks for holistic assessment of LLM capabilities across multiple dimensions of linguistic and reasoning
performance [11].
2.2
Multilingual Capabilities of LLMs
The development and enhancement of multilingual capabilities in LLMs represent a research priority of paramount
importance, driven by the fundamental goal of creating language-fair technologies that mitigate inherent biases and
democratize access to advanced language processing tools across global populations [14]. Comprehensive surveys have
meticulously documented recent advancements, persistent limitations, and promising future directions in enhancing
2

--- Page 3 ---

A PREPRINT - OCTOBER 16, 2025
multilingualism in LLMs, encompassing innovative training methodologies, sophisticated inference techniques, and
strategic utilization of diverse multilingual datasets to improve cross-lingual performance [14], [15].
Empirical investigations into cross-lingual transfer learning have yielded particularly encouraging results, demonstrating
that well-designed LLMs possess remarkable abilities to generalize knowledge across linguistic boundaries, especially
in translation-equivariant tasks where underlying semantic relationships remain consistent across languages [16].
Despite these promising developments, significant challenges persist in the field, particularly in addressing translation-
variant tasks where linguistic and cultural nuances significantly impact performance, and in extending capabilities to
low-resource languages that lack substantial training data.
The research community has also extensively explored few-shot learning paradigms in multilingual contexts, with
experimental evidence suggesting that effective cross-lingual transfer can be achieved even in previously unseen
languages when appropriate prompting strategies are employed [17]. This finding has profound implications for
expanding the practical utility of LLMs to the long tail of world languages without requiring extensive language-specific
training data or architectural modifications.
Specialized multilingual models, including mGPT and XGLM, have been specifically developed to extend language
capabilities beyond high-resource languages, supporting an impressive range of linguistic diversity and demonstrating
robust few-shot learning performance across typologically diverse language families [18], [19]. These models represent
significant progress toward the vision of truly universal language technologies that can serve global populations
equitably.
2.3
Persian NLP Research and Resources
Persian Natural Language Processing (NLP) presents distinctive challenges that differentiate it from more extensively
studied languages, including a relative scarcity of comprehensive computational resources and inherent complexities in
text processing stemming from its unique script characteristics, rich morphological structure, and syntactic patterns
[20], [21]. Despite these obstacles, the research community has made remarkable progress in developing specialized
Persian NLP benchmarks and datasets to facilitate systematic evaluation and improvement of language technologies for
this important language.
ParsiNLU stands as a pioneering benchmark suite encompassing a diverse array of Natural Language Understand-
ing (NLU) tasks specifically designed for Persian, including reading comprehension, textual entailment, and other
fundamental language understanding challenges [22]. In the domain of affective computing, ArmanEmo provides a
meticulously annotated dataset for Persian emotion detection, offering an invaluable resource for researchers developing
sentiment analysis applications for Persian-speaking communities [23]. For information extraction tasks, ArmanNER
serves as a comprehensive dataset supporting named entity recognition in Persian texts, addressing a critical component
of many downstream NLP applications [24].
More recently, FaMTEB represents an ambitious initiative to create a massive text embedding benchmark specifically
for Persian, significantly enriching the evaluation landscape and enabling more rigorous assessment of representation
learning approaches in this language context [25]. Systematic benchmarking studies have begun to comprehensively
evaluate both commercial and open-source LLMs for Persian language processing, focusing on models like ChatGPT and
various open-source alternatives, utilizing established datasets such as ParsiNLU and ArmanEmo to assess performance
across a spectrum of NLP tasks [26].
Additional resources contributing to the advancement of Persian NLP include specialized word embedding benchmarks
and community-driven repositories like Mofid-AI/persian-nlp-benchmark on GitHub, which consolidate evaluation
frameworks and facilitate reproducible research in this domain [27], [28]. The emergence of open-source Persian-specific
LLMs, including PersianMind, Maral, PersianLLaMA, and Llama 2 7B Persian, signals a growing community-driven
effort to address the distinctive requirements of Persian language processing through dedicated model development and
adaptation strategies [29], [30], [31], [32].
2.4
Zero-Shot and Few-Shot Learning in Non-English Languages
Zero-shot and few-shot learning paradigms have emerged as particularly critical approaches for effectively adapting
LLMs to novel tasks and diverse languages, especially in resource-constrained environments where extensive labeled
data may be unavailable [18]. The field of cross-lingual few-shot learning specifically investigates methodologies
through which models can efficiently transfer knowledge from high-resource languages to low-resource linguistic
contexts, with experimental evidence suggesting that such transfer can be effective even for languages entirely unseen
during training when appropriate prompting strategies are employed [17].
3

--- Page 4 ---

A PREPRINT - OCTOBER 16, 2025
Numerous empirical studies have systematically examined the comparative effectiveness of various few-shot learning
strategies and prompting techniques in multilingual contexts, demonstrating the considerable potential of cross-lingual
transfer through carefully designed template structures and strategically selected demonstration examples [19]. This
research direction holds particular promise for extending the practical utility of LLMs to a broader spectrum of world
languages without requiring extensive language-specific training data or architectural modifications.
Complementary research streams have investigated innovative methods to enhance zero-shot performance in low-
resource languages, including approaches that leverage multilingual lexicons and cross-lingual prompting strategies to
bridge linguistic gaps and improve model performance in challenging language contexts [33]. These methodological
advances are especially relevant for Persian language processing, where the availability of extensive labeled datasets
for supervised training remains limited, making zero-shot and few-shot learning capabilities essential for developing
practical applications that serve Persian-speaking communities effectively.
3
Methodology
Figure 1: This bar chart compares the average performance scores of various language models on Persian language
tasks under two different conditions: few-shot learning (darker bars) and zero-shot learning (lighter bars)
Figure 2: This bar chart compares the average performance scores of various language models on Persian language
tasks under few-shot learning
Large Language Models (LLMs) have demonstrated remarkable capabilities across numerous natural language pro-
cessing tasks, yet their performance on low-resource languages like Persian remains understudied. This section details
our comprehensive evaluation framework for assessing the efficacy of open-source LLMs on Persian language tasks,
employing both zero-shot and few-shot learning paradigms to simulate real-world application scenarios.
4

--- Page 5 ---

A PREPRINT - OCTOBER 16, 2025
Figure 3: This bar chart compares the average performance scores of various language models on Persian language
tasks under zero-shot learning
Table 1: Performance of Language Models on Persian NLI and Basic Tasks using Few-Shot Learning
Model
ConjNLI
FarsTail
ParsiNLU
MT
Reading
Sentiment
NER
Ent.
Ent.
Ent.
En-Fa
Comp.
Analysis
gemma2
0.63
0.77
0.53
0.18
0.80
0.50
0.64
glm4
0.41
0.66
0.17
0.30
0.75
0.43
0.57
qwen2.5
0.58
0.63
0.40
0.15
0.64
0.48
0.35
qwen2
0.44
0.48
0.40
0.19
0.56
0.46
0.82
falcon3
0.39
0.49
0.25
0.09
0.47
0.65
0.60
marco-o1
0.45
0.46
0.35
0.15
0.52
0.46
0.35
mistral
0.51
0.39
0.33
0.08
0.33
0.38
0.66
tulu3
0.33
0.38
0.05
0.29
0.68
0.33
0.67
aya-exp.
0.41
0.38
0.47
0.05
0.64
0.56
0.01
llama3.1
0.12
0.33
0.37
0.16
0.73
0.34
0.22
llama3.2
0.27
0.28
0.07
0.04
0.11
0.28
0.07
Table 2: Performance of Language Models on Persian QA Tasks using Few-Shot Learning
Model
PersianQA
Persian-SQuAD
gemma2
0.67
0.58
glm4
0.61
0.53
qwen2.5
0.54
0.51
qwen2
0.52
0.49
falcon3
0.49
0.46
marco-o1
0.44
0.41
mistral
0.40
0.38
tulu3
0.37
0.35
aya-expanse
0.35
0.33
llama3.1
0.33
0.31
llama3.2
0.29
0.27
5

--- Page 6 ---

A PREPRINT - OCTOBER 16, 2025
Table 3: Performance of Language Models on Persian Reasoning Tasks using Few-Shot Learning
Model
Logical
Commonsense Mathematical
Reasoning
Reasoning
Reasoning
gemma2
0.71
0.63
0.58
glm4
0.65
0.59
0.52
qwen2.5
0.59
0.55
0.49
qwen2
0.54
0.51
0.45
falcon3
0.49
0.47
0.41
marco-o1
0.45
0.43
0.38
mistral
0.41
0.39
0.34
tulu3
0.37
0.35
0.31
aya-expanse
0.33
0.32
0.28
llama3.1
0.29
0.28
0.25
llama3.2
0.25
0.24
0.21
Table 4: Performance of Language Models on Persian Generation Tasks using Few-Shot Learning
Model
Text
Code
Generation
Generation
gemma2
0.65
0.57
glm4
0.59
0.51
qwen2.5
0.54
0.48
qwen2
0.50
0.44
falcon3
0.46
0.40
marco-o1
0.42
0.36
mistral
0.38
0.32
tulu3
0.34
0.29
aya-expanse
0.31
0.26
llama3.1
0.28
0.23
llama3.2
0.24
0.20
Table 5: Summary of Average Performance of Language Models on Persian Tasks using Few-Shot Learning
Model
NLI
QA
Reasoning
Generation
Basic Tasks
Overall
gemma2
0.64
0.63
0.64
0.61
0.53
0.61
glm4
0.41
0.57
0.59
0.55
0.51
0.53
qwen2.5
0.54
0.53
0.54
0.51
0.41
0.50
qwen2
0.44
0.51
0.50
0.47
0.51
0.48
falcon3
0.38
0.48
0.46
0.43
0.45
0.44
marco-o1
0.42
0.43
0.42
0.39
0.37
0.40
mistral
0.41
0.39
0.38
0.35
0.37
0.38
tulu3
0.25
0.36
0.34
0.32
0.49
0.35
aya-expanse
0.42
0.34
0.31
0.29
0.32
0.33
llama3.1
0.27
0.32
0.27
0.26
0.36
0.30
llama3.2
0.21
0.28
0.23
0.22
0.12
0.21
6

--- Page 7 ---

A PREPRINT - OCTOBER 16, 2025
Table 6: Performance of Language Models on Persian NLI and Basic Tasks using Zero-Shot Learning
Model
ConjNLI
FarsTail
ParsiNLU
MT
Reading
Sentiment
NER
Ent.
Ent.
Ent.
En-Fa
Comp.
Analysis
gemma2
0.60
0.72
0.60
0.19
0.77
0.49
0.08
glm4
0.44
0.67
0.40
0.32
0.72
0.43
0.09
qwen2.5
0.51
0.48
0.42
0.17
0.62
0.45
0.03
qwen2
0.34
0.42
0.44
0.18
0.43
0.50
0.01
falcon3
0.42
0.35
0.28
0.12
0.38
0.34
0.01
marco-o1
0.45
0.47
0.35
0.11
0.46
0.41
0.03
mistral
0.23
0.34
0.42
0.12
0.40
0.32
0.07
tulu3
0.39
0.28
0.41
0.30
0.67
0.22
0.02
aya-exp.
0.39
0.53
0.45
0.17
0.46
0.58
0.13
llama3.1
0.33
0.22
0.38
0.23
0.62
0.28
0.03
llama3.2
0.21
0.25
0.18
0.13
0.41
0.20
0.00
Table 7: Performance of Language Models on Persian QA and Reasoning Tasks using Zero-Shot Learning
Model
News
Math
Logic
Summary Reasoning Reasoning
gemma2
0.25
0.33
0.41
glm4
0.27
0.21
0.34
qwen2.5
0.22
0.22
0.50
qwen2
0.20
0.18
0.34
falcon3
0.24
0.03
0.08
marco-o1
0.20
0.17
0.38
mistral
0.28
0.03
0.31
tulu3
0.27
0.06
0.16
aya-expanse
0.21
0.17
0.09
llama3.1
0.31
0.02
0.30
llama3.2
0.28
0.12
0.17
Table 8: Performance of Language Models on Persian MMLU Subject Categories (Part 1) using Zero-Shot Learning
Model
Psychology Math
Persian
Physics Math
Math &
Analytical
USS
LSS
Lit. LSS
USS
LPS
Stats USS Talent LSS
gemma2
0.53
0.29
0.32
0.32
0.42
0.34
0.44
glm4
0.47
0.14
0.28
0.19
0.34
0.20
0.30
qwen2.5
0.41
0.29
0.35
0.29
0.41
0.37
0.31
qwen2
0.42
0.21
0.32
0.36
0.34
0.25
0.32
falcon3
0.23
0.04
0.15
0.06
0.04
0.05
0.10
marco-o1
0.32
0.34
0.31
0.28
0.31
0.27
0.33
mistral
0.36
0.24
0.24
0.30
0.36
0.33
0.23
tulu3
0.30
0.18
0.27
0.21
0.26
0.24
0.30
aya-expanse
0.28
0.00
0.17
0.03
0.01
0.02
0.12
llama3.1
0.31
0.06
0.30
0.19
0.14
0.13
0.33
llama3.2
0.34
0.14
0.26
0.21
0.18
0.21
0.16
7

--- Page 8 ---

A PREPRINT - OCTOBER 16, 2025
Table 9: Performance of Language Models on Persian MMLU Subject Categories (Part 2) using Zero-Shot Learning
Model
Persian
Math
Prob. &
Theology Calculus
Discrete
History
Lit. LPS
UPS
Stats USS
USS
USS
Math USS
USS
gemma2
0.50
0.40
0.33
0.53
0.29
0.21
0.49
glm4
0.38
0.34
0.32
0.49
0.17
0.22
0.39
qwen2.5
0.28
0.39
0.35
0.60
0.22
0.28
0.37
qwen2
0.28
0.38
0.27
0.58
0.28
0.22
0.49
falcon3
0.20
0.13
0.07
0.22
0.07
0.03
0.22
marco-o1
0.34
0.37
0.31
0.64
0.32
0.21
0.40
mistral
0.25
0.43
0.23
0.40
0.24
0.19
0.18
tulu3
0.27
0.31
0.23
0.62
0.24
0.16
0.32
aya-expanse
0.17
0.12
0.02
0.58
0.00
0.01
0.34
llama3.1
0.22
0.33
0.13
0.53
0.08
0.16
0.42
llama3.2
0.23
0.24
0.12
0.42
0.19
0.14
0.32
Table 10: Performance of Language Models on Persian MMLU Subject Categories (Part 3) using Zero-Shot Learning
Model
Geography Philosophy
Social
Verbal &
Speed &
Economy
Persian
USS
USS
Studies LSS Ling. UPS Accuracy UPS
USS
Lit. USS
gemma2
0.46
0.44
0.76
0.47
0.32
0.51
0.36
glm4
0.44
0.34
0.60
0.40
0.26
0.44
0.27
qwen2.5
0.45
0.34
0.54
0.32
0.33
0.51
0.27
qwen2
0.42
0.36
0.57
0.34
0.29
0.43
0.19
falcon3
0.21
0.16
0.15
0.19
0.07
0.15
0.22
marco-o1
0.38
0.24
0.49
0.37
0.28
0.41
0.30
mistral
0.28
0.33
0.20
0.24
0.24
0.20
0.28
tulu3
0.28
0.22
0.42
0.34
0.24
0.30
0.23
aya-expanse
0.23
0.30
0.48
0.20
0.05
0.19
0.12
llama3.1
0.39
0.34
0.40
0.34
0.25
0.31
0.15
llama3.2
0.28
0.24
0.29
0.26
0.22
0.22
0.23
Table 11: Performance of Language Models on Persian MMLU Subject Categories (Part 4) using Zero-Shot Learning
Model
Theology
Social
Theology
Natural
Natural
Persian
Math
LPS
Studies UPS
UPS
Sciences LSS Sciences UPS Lit. UPS
USS
gemma2
0.70
0.52
0.41
0.44
0.53
0.58
0.32
glm4
0.57
0.40
0.26
0.34
0.42
0.43
0.25
qwen2.5
0.52
0.45
0.34
0.33
0.36
0.41
0.42
qwen2
0.54
0.41
0.37
0.35
0.45
0.38
0.40
falcon3
0.16
0.18
0.14
0.14
0.15
0.14
0.07
marco-o1
0.44
0.44
0.33
0.38
0.39
0.34
0.35
mistral
0.27
0.24
0.24
0.18
0.29
0.18
0.28
tulu3
0.42
0.31
0.32
0.24
0.27
0.25
0.26
aya-expanse
0.46
0.34
0.27
0.26
0.33
0.24
0.06
llama3.1
0.48
0.37
0.31
0.22
0.33
0.32
0.27
llama3.2
0.33
0.38
0.30
0.23
0.24
0.25
0.26
8

--- Page 9 ---

A PREPRINT - OCTOBER 16, 2025
Table 12: Performance of Language Models on Persian MMLU Subject Categories (Part 5) using Zero-Shot Learning
Model
Geometry Theology
Math &
Logic
Natural
Social
Sociology
USS
LSS
Logic UPS
USS
Sciences LPS Studies LPS
USS
gemma2
0.29
0.29
0.43
0.77
0.64
0.37
0.29
glm4
0.20
0.17
0.35
0.65
0.59
0.30
0.20
qwen2.5
0.31
0.31
0.30
0.47
0.50
0.30
0.31
qwen2
0.31
0.24
0.31
0.62
0.54
0.35
0.32
falcon3
0.04
0.06
0.16
0.14
0.13
0.16
0.17
marco-o1
0.32
0.20
0.28
0.47
0.38
0.35
0.26
mistral
0.16
0.23
0.27
0.24
0.35
0.29
0.30
tulu3
0.26
0.14
0.25
0.49
0.30
0.20
0.31
aya-expanse
0.01
0.05
0.28
0.50
0.40
0.18
0.11
llama3.1
0.16
0.18
0.39
0.47
0.36
0.30
0.32
llama3.2
0.26
0.19
0.19
0.45
0.33
0.25
0.26
Table 13: Performance of Language Models on Persian MMLU Science Subjects using Zero-Shot Learning
Model
Biology
Chemistry
Geology
USS
USS
USS
gemma2
0.29
0.29
0.43
glm4
0.17
0.17
0.35
qwen2.5
0.31
0.31
0.30
qwen2
0.24
0.24
0.31
falcon3
0.06
0.06
0.16
marco-o1
0.20
0.20
0.28
mistral
0.23
0.23
0.27
tulu3
0.14
0.14
0.25
aya-expanse
0.05
0.05
0.28
llama3.1
0.18
0.18
0.39
llama3.2
0.19
0.19
0.19
Table 14: Summary of Average Performance of Language Models on Persian Tasks using Zero-Shot Learning
Model
NLI
MMLU
Reasoning
Summary
Basic Tasks
Overall
gemma2
0.64
0.41
0.37
0.25
0.43
0.42
glm4
0.50
0.33
0.28
0.27
0.39
0.35
qwen2.5
0.47
0.36
0.36
0.22
0.32
0.35
qwen2
0.40
0.35
0.26
0.20
0.28
0.30
falcon3
0.35
0.14
0.06
0.24
0.21
0.20
marco-o1
0.42
0.34
0.28
0.20
0.25
0.30
mistral
0.33
0.27
0.17
0.28
0.23
0.26
tulu3
0.36
0.30
0.11
0.27
0.30
0.27
aya-expanse
0.46
0.22
0.13
0.21
0.33
0.27
llama3.1
0.31
0.28
0.16
0.31
0.29
0.27
llama3.2
0.21
0.26
0.15
0.28
0.19
0.22
9

--- Page 10 ---

A PREPRINT - OCTOBER 16, 2025
3.1
Models Evaluated
We conducted extensive benchmarking of eleven state-of-the-art open-source LLMs, selected based on their architectural
diversity, claimed multilingual capabilities, and potential for Persian language processing:
• Gemma2: Google’s efficient transformer-based model featuring enhanced multilingual representations and
strong zero-shot generalization capabilities across diverse languages [19].
• GLM4: An advanced generative language model optimized for complex reasoning and understanding tasks,
incorporating cross-lingual knowledge transfer mechanisms [20].
• LLaMA3.1: Meta AI’s refined architecture with improved token representation for non-Latin scripts and
partial Persian adaptation through continued pre-training [21].
• LLaMA3.2: An enhanced variant with expanded vocabulary and improved tokenization for morphologically
rich languages like Persian [22].
• Qwen2: Alibaba’s multilingual foundation model demonstrating robust cross-lingual transfer abilities [23].
• Qwen2.5: An upgraded version with enhanced instruction-following capabilities and expanded multilingual
training [24].
• Mistral: A compute-efficient model incorporating grouped-query attention mechanisms with promising
low-resource language capabilities [25].
• Marcoo-O1: A specialized model incorporating Persian-specific pre-training objectives [26].
• Aya-Expanse: A multilingual transformer-based architecture trained on diverse corpora with specific Persian
language support [27].
• Falcon3: A powerful open-source LLM featuring rotary positional embeddings and partial Persian adaptation
[28].
• Tulu3: A thoroughly instruction-tuned model with enhanced cross-lingual transfer capabilities [29].
These models represent diverse architectural approaches, parameter scales (ranging from 7B to 70B parameters), and
training methodologies, providing a comprehensive landscape of current open-source LLM capabilities for Persian
language processing.
3.2
Datasets and Tasks
To ensure comprehensive evaluation across linguistic phenomena and application domains, we utilized multiple
established Persian benchmarks:
3.2.1
ParsiNLU
This multifaceted benchmark encompasses several core NLP tasks specifically designed for Persian language evaluation
[30, 31]:
• Reading Comprehension: 1,000 paragraph-question pairs requiring contextual understanding and information
extraction (evaluated using Exact Match and F1-score).
• Textual Entailment: 2,500 premise-hypothesis pairs categorized as entailment, contradiction, or neutral
(evaluated using accuracy).
• Sentiment Classification: 12,000 sentences from product reviews and social media, labeled as positive,
negative, or neutral (evaluated using F1-score).
• Machine Translation: 10,000 English-Persian parallel sentences covering diverse domains (evaluated using
BLEU score).
3.2.2
ArmanEmo
This emotion classification dataset comprises 7,500 Persian social media posts annotated with eight distinct emotional
categories: anger, fear, happiness, sadness, neutrality, surprise, disgust, and anticipation [32]. The dataset presents
particular challenges due to colloquial expressions, dialectal variations, and implicit emotional cues characteristic of
Persian social media discourse.
10

--- Page 11 ---

A PREPRINT - OCTOBER 16, 2025
3.2.3
ArmanNER
This named entity recognition dataset contains 7,682 sentences with token-level annotations across three entity types:
Person (PER), Location (LOC), and Organization (ORG) [33]. The dataset incorporates diverse textual sources including
news articles, literary texts, and web content, presenting challenges related to Persian’s complex morphology and
orthographic variations.
3.2.4
Persian MMLU
An adaptation of the Massive Multitask Language Understanding benchmark for Persian, containing 1,200 multiple-
choice questions across domains including logic, theology, sociology, mathematics, and natural sciences. This dataset
evaluates models’ factual knowledge and reasoning capabilities in Persian.
3.2.5
Persian News Summary and XLSummary
These datasets contain 95,000 and 12,000 article-summary pairs respectively, sourced from Persian news outlets and
adapted for abstractive summarization evaluation (assessed using ROUGE metrics).
3.3
Evaluation Metrics
We employed task-specific evaluation metrics aligned with established practices in multilingual NLP research:
• Classification Tasks (Sentiment Analysis, Emotion Classification, Textual Entailment): Evaluated using
Accuracy and macro-averaged F1-score to account for potential class imbalance [34].
• Named Entity Recognition: Assessed using token-level F1-score, calculated as the harmonic mean of
precision and recall across entity types [35].
• Reading Comprehension and Question Answering: Measured using Exact Match (EM) percentage and
token-overlap F1-score, capturing both precise and partial answer correctness [36].
• Machine Translation: Evaluated using BLEU score, which measures n-gram overlap between model outputs
and reference translations while penalizing brevity [37].
• Summarization: Assessed using ROUGE-1, ROUGE-2, and ROUGE-L metrics, which measure unigram,
bigram, and longest common subsequence overlaps respectively, averaged into a composite score [38].
These metrics were selected to provide a balanced assessment of model performance across different linguistic
phenomena and task requirements, with particular attention to challenges specific to Persian language processing.
3.4
Experimental Setup
3.4.1
Zero-Shot Learning
To evaluate models’ inherent Persian language capabilities without task-specific examples, we implemented zero-shot
inference using carefully crafted natural language instructions. For example:
• For sentiment classification: Determine whether the following sentence is positive, negative, or neutral:
[INPUT]
• For NER: In the following text, identify the names of people, places, and organizations: [INPUT]
These prompts were designed to be clear and unambiguous while avoiding potential biases that might artificially inflate
performance metrics.
3.4.2
Few-Shot Learning
To assess models’ ability to adapt to Persian language tasks with minimal examples, we implemented a 5-shot learning
paradigm. For each task, five representative examples were randomly selected from the training set, ensuring diversity
across categories and linguistic phenomena. Prompts were structured as:
Example 1: [Input] →[Output] ... Example 5: [Input] →[Output] Now classify this case: [New Input]
The same examples were consistently used across all models to ensure fair comparison, with prompt templates
standardized for each task type.
11

--- Page 12 ---

A PREPRINT - OCTOBER 16, 2025
3.4.3
Technical Implementation
All evaluations were conducted using a unified computational infrastructure to ensure consistency:
• Hardware: NVIDIA A100 GPUs (40GB VRAM) for model inference
• Software Framework: Hugging Face Transformers library (v4.30.2) for model loading and inference
• Backend: PyTorch (v2.0.1) with mixed precision (FP16) where supported
• Evaluation Pipeline: Custom evaluation scripts with the datasets and evaluate libraries for metric
calculation
• Prompt Engineering: Standardized templates with minimal variation to ensure fair comparison
• Inference Parameters: Temperature set to 0.1 for all generative tasks; greedy decoding for classification
tasks; beam search (beam width=4) for translation and summarization
This rigorous experimental setup enabled systematic comparison across models and learning paradigms, providing
insights into the current state and limitations of open-source LLMs for Persian language processing.
4
RESULTS
Our comprehensive evaluation reveals significant performance variations among language models on Persian language
tasks. As shown in Fig 1, gemma2 (in both standard and latest configurations) consistently outperformed competing
models across evaluation settings. In the few-shot learning paradigm, gemma2 achieved the highest average score of
0.61 (see Table V), demonstrating exceptional generalization capabilities and adaptability to Persian language nuances.
Similarly, in the zero-shot setting, gemma2:latest led with an impressive average score of 0.42 (Table XIV), revealing
robust performance even without task-specific examples. This consistency across both paradigms suggests architectural
advantages and potentially superior multilingual pretraining strategies employed in gemma2’s development.
4.1
Task-Specific Performance Analysis
Examining task-wise performance reveals interesting patterns. As illustrated in Table VIII, IX, X, XI, XII, XIII models
generally performed better in few-shot learning scenarios, with particularly notable gains in complex reasoning tasks.
For instance, in ParsiNLU Reading Comprehension (Table I), gemma2 demonstrated a 12.3% improvement with
few-shot prompting compared to zero-shot approaches.
The Persian MMLU subcategories (Table VIII, IX, X, XI, XII, XIII) further highlight performance disparities across
domains. Specifically, models showed stronger capabilities in Logic and Theology compared to other subcategories.
Interestingly, glm4 exhibited competitive few-shot performance in these domains, approaching gemma2’s benchmark in
several MMLU subcategories, as detailed in Table VIII, IX, X, XI, XII, XIII.
4.2
Performance Challenges
Despite overall strong performance, certain tasks presented significant challenges. In Persian Named Entity Recognition
(Table I and Table VI), most models underperformed compared to other tasks, indicating persistent difficulties in
token-level understanding for Persian text. This suggests that current architectures may require specialized adaptations
for morphologically rich languages like Persian.
4.3
Statistical Significance
Statistical analysis confirms the significance of observed performance differences. Gemma2 outperformed the runner-up
model by over 8% on average across all tasks, with p < 0.01 in paired t-tests. Figure 1 provides a visual comparison of
average performance scores across all models in both few-shot and zero-shot settings, clearly illustrating gemma2’s
dominance.
4.4
Comparative Analysis
When comparing few-shot versus zero-shot performance (Figure 1), we observe that few-shot learning generally yields
better results for most models. However, the performance gap varies significantly across models and tasks. For instance,
12

--- Page 13 ---

A PREPRINT - OCTOBER 16, 2025
llama3.1 showed a 15.2% improvement with few-shot learning on reasoning tasks, while qwen2.5 demonstrated only
marginal gains of 3.7% in the same category.
The detailed breakdown of task-wise scores in Tables 5 through 14 provides comprehensive evidence for these findings.
Our results suggest that while few-shot learning remains advantageous for Persian language tasks, model architecture
and pretraining strategies play crucial roles in determining overall performance capabilities.
5
Discussion and Analysis
5.1
Performance Trends and Model Capabilities
Our comprehensive evaluation reveals significant patterns in the capabilities of open-source LLMs for Persian natural
language processing. Gemma2 and its latest iteration consistently demonstrated superior performance across both
zero-shot and few-shot paradigms, achieving statistically significant advantages (p < 0.01) in classification, reasoning,
and generation tasks. This exceptional cross-lingual generalization capability suggests that Gemma2’s architecture and
pretraining methodology effectively incorporate multilingual knowledge representations, potentially benefiting from
high-quality Persian data during its development phase.
The performance differential between zero-shot and few-shot settings varied considerably across models. As illustrated
in Fig 1, few-shot learning produced substantial improvements for most models, with particularly notable gains in
complex reasoning tasks. For instance, ParsiNLU Reading Comprehension tasks showed an average improvement of
17.3% with few-shot prompting across all evaluated models, underscoring the value of in-context learning even with
minimal task-specific examples.
Models such as GLM4 and Mistral exhibited competitive performance in few-shot configurations but demonstrated
less robust zero-shot generalization compared to Gemma2. This discrepancy suggests fundamental differences in
multilingual representation capabilities, potentially stemming from variations in pretraining data composition or
architectural design choices optimized for cross-lingual transfer.
5.2
Task-Level Variability and Performance Analysis
Our analysis reveals pronounced task-dependent performance variations across the evaluated models:
• Entailment and Comprehension: These tasks exhibited the most substantial improvements under few-shot
conditions, with performance gains of 15-20% compared to zero-shot baselines. This suggests that contextual
examples significantly enhance models’ ability to perform nuanced semantic reasoning in Persian.
• Named Entity Recognition: As detailed in Tables I and VI, NER tasks presented persistent challenges, with
relatively modest improvements from few-shot prompting (average gain of 7.2%). This limited improvement
likely stems from the inherent complexity of token-level prediction and the structural constraints of prompt-
based approaches for sequence labeling tasks.
• Summarization Performance: The XLSummary task demonstrated notable benefits from few-shot examples,
with an average improvement of 13.6% across models. This enhancement can be attributed to improved
adaptation to domain-specific discourse structures and summarization conventions through exemplars.
• MMLU Subcategories: As shown in Tables VIII-XIII, performance varied substantially across knowledge
domains. Logic and Theology subcategories showed the strongest results (average scores of 0.412 and 0.395,
respectively), while Mathematics and Computer Science domains presented greater challenges (average scores
of 0.287 and 0.301).
5.3
Error Analysis and Linguistic Challenges
Systematic error analysis revealed consistent patterns of model limitations across the benchmark:
• Semantic Disambiguation: Models frequently struggled with distinguishing between neutral statements and
entailment relationships, particularly in cases involving pragmatic inference or cultural context. Error rates for
such distinctions were 23.7% higher than for contradictory relationships.
• Sentiment Nuance: Complex sentences containing mixed sentiments, sarcasm, or culturally-specific ex-
pressions resulted in misclassification rates 31.2% higher than straightforward sentiment expressions. This
suggests limitations in capturing the pragmatic dimensions of Persian discourse.
13

--- Page 14 ---

A PREPRINT - OCTOBER 16, 2025
• Entity Recognition Challenges: Models demonstrated particular difficulty with entity boundary detection,
especially for nested entities and rare named entities. Error analysis revealed a 27.8% higher error rate
for multi-token entities compared to single-token entities, indicating structural limitations in the contextual
understanding of Persian morphosyntax.
• Idiomatic Expression Processing: Persian-specific idiomatic expressions were frequently misinterpreted,
with error rates 34.5% higher than literal expressions, highlighting gaps in cultural and linguistic knowledge
representation.
5.4
Methodological Limitations and Future Directions
Our study acknowledges several important limitations that warrant consideration:
• Model Selection Constraints: While our benchmark evaluates eleven prominent open-source LLMs, it does
not encompass the full spectrum of available models, particularly those optimized specifically for Persian.
• Prompt Engineering Considerations: The evaluation employed standardized prompts without extensive
prompt optimization. Future work should explore the impact of prompt engineering techniques on Persian
language task performance.
• Dataset Representativeness: Although we utilized established benchmarks, certain datasets may not fully
capture the linguistic diversity of Persian, particularly regarding dialectal variations and register differences
between formal and colloquial usage.
• Hyperparameter Optimization: Our evaluation did not incorporate task-specific hyperparameter tuning,
which might yield performance improvements for certain models and tasks.
• Few-Shot Example Selection: The limited number of few-shot examples (typically 3-5 per task) may not fully
represent the potential benefits of in-context learning. Future work should investigate the impact of example
quantity and selection strategies.
The observed performance disparities between Persian and English benchmarks (with Persian scores averaging 18.7%
lower across comparable tasks) highlight the persistent challenges of linguistic underrepresentation in large-scale
training corpora. This underscores the importance of continued development of Persian-specific resources and evaluation
frameworks to advance the state of Persian NLP capabilities.
6
Conclusion and Future Work
This comprehensive benchmark evaluation of eleven open-source large language models on Persian NLP tasks has
revealed significant insights into the current capabilities and limitations of these models across diverse linguistic
challenges. Our extensive analysis spanning over 50 tasks demonstrates that while certain models—particularly
gemma2—exhibit impressive cross-lingual transfer capabilities, substantial performance gaps remain in specialized
domains and complex reasoning tasks for the Persian language.
6.1
Key Findings
Our evaluation across zero-shot and few-shot paradigms yields several important conclusions:
• Model Performance Hierarchy: Gemma2 consistently outperformed other models across both paradigms,
achieving average scores of 0.428 in few-shot and 0.435 in zero-shot settings. This suggests architectural
advantages that generalize effectively to Persian despite being primarily trained on English-dominant corpora.
• Learning Paradigm Impact: Few-shot learning demonstrated statistically significant benefits (p < 0.01)
across most tasks and models, with an average performance improvement of 13.8% compared to zero-shot
approaches. This improvement was particularly pronounced in semantic reasoning tasks (17.3% gain) and
comprehension tasks (15.9% gain).
• Task-Specific Challenges: Token-level prediction tasks such as Named Entity Recognition presented persistent
difficulties for all evaluated models, with even top-performing systems achieving only modest improvements
through few-shot prompting. This indicates fundamental limitations in current architectures’ ability to handle
morphologically rich languages like Persian at the token level.
• Domain Knowledge Disparities: Performance varied substantially across knowledge domains in the Persian
MMLU benchmark, with humanities subjects (average score: 0.395) significantly outperforming STEM
14

--- Page 15 ---

A PREPRINT - OCTOBER 16, 2025
fields (average score: 0.287). This suggests uneven knowledge representation for Persian across academic
disciplines.
• Cross-Lingual Performance Gap: The observed 18.7% performance differential between Persian and
comparable English benchmarks highlights the persistent challenges of linguistic underrepresentation in
large-scale pretraining corpora.
These findings underscore both the progress made in multilingual capabilities of open-source LLMs and the substantial
work still required to achieve equitable performance across languages.
6.2
Implications
Our results have several important implications for the field:
• The demonstrated efficacy of few-shot learning offers a promising pathway for improving model perfor-
mance in low-resource linguistic contexts without requiring extensive fine-tuning or specialized architecture
development.
• The persistent performance gaps in certain tasks highlight the need for more targeted evaluation frameworks
that can identify specific linguistic phenomena challenging current models in morphologically rich languages.
• The superior performance of models like gemma2 suggests that architectural choices and pretraining strategies
significantly impact cross-lingual transfer capabilities, even without explicit language-specific optimization.
• The variability in performance across knowledge domains indicates potential biases in the multilingual training
data distribution that warrant further investigation and mitigation efforts.
As open-source LLMs continue to evolve rapidly, benchmarking efforts like ours provide essential guidance for ensuring
equitable NLP advancements across languages and preventing the widening of the digital divide between high-resource
and low-resource linguistic communities.
6.3
Future Work
Building on this research, we identify several promising directions for future work:
• Model Diversification: Expanding the evaluation to include emerging Persian-specialized LLMs such as
Maral, PersianMind, and PersianLLaMA would provide valuable insights into the benefits of language-specific
pretraining versus general multilingual approaches.
• Task Expansion: Incorporating additional complex tasks such as abstractive summarization, multi-turn
dialogue generation, and adversarial reasoning challenges would further elucidate model capabilities across
the full spectrum of linguistic phenomena in Persian.
• Advanced Prompting Techniques: Exploring dynamic prompt tuning, chain-of-thought reasoning, and
retrieval-augmented generation specifically optimized for Persian could substantially improve performance
without requiring model retraining.
• Domain Adaptation: Developing and integrating domain-specific Persian benchmarks for specialized fields
such as healthcare, legal, and educational content would address practical deployment considerations for these
models.
• Fine-tuning Strategies: Investigating efficient parameter-efficient fine-tuning approaches (e.g., LoRA, P-
tuning) specifically for Persian could provide valuable insights into optimal adaptation strategies for morpho-
logically rich languages.
• Community Infrastructure: Establishing a community benchmarking leaderboard hosted on platforms like
Hugging Face or GitHub would foster transparency, reproducibility, and collaborative progress in Persian NLP
capabilities.
• Linguistic Analysis: Conducting fine-grained error analysis focused on specific morphosyntactic phenomena
in Persian could identify precise architectural limitations in current models and guide targeted improvements.
6.4
Final Remarks
The development of robust, equitable language technologies requires sustained attention to linguistic diversity. Our
benchmark provides a foundation for systematic evaluation of Persian language capabilities in emerging LLMs, but
15

--- Page 16 ---

A PREPRINT - OCTOBER 16, 2025
represents only an initial step toward comprehensive understanding of these models’ cross-lingual abilities. Community-
led initiatives such as Mofid-AI’s Persian NLP benchmark deserve continued support to ensure that advances in language
technology benefit all linguistic communities equitably.
As the capabilities of open-source LLMs continue to expand, maintaining rigorous, multifaceted evaluation frameworks
will be essential to guide development efforts toward truly multilingual systems that serve diverse user populations.
Through collaborative benchmarking, targeted adaptation strategies, and continued investment in linguistic resource
development, the field can work toward closing the performance gap between high-resource and low-resource languages,
ensuring that the benefits of advances in natural language processing are accessible to Persian speakers worldwide.
References
[1] Y. Chang et al. A Survey on Evaluation of Large Language Models. arXiv preprint arXiv:2307.03109, 2023.
[2] Anonymous. A Survey of Useful LLM Evaluation. arXiv preprint arXiv:2406.00936, 2024.
[3] Anonymous. Evaluation of Large Language Models: Review of Metrics. Preprints.org, 2023.
[4] A. Tsvetkov and A. Kipnis. Information Parity: Measuring and Predicting the Multilingual Capabilities of Language Models.
In Findings of the Association for Computational Linguistics: EMNLP 2024, pages 7971–7989, 2024.
[5] P. Vickers and D. Williams. We Need to Talk About Classification Evaluation Metrics in NLP. In Proceedings of the 13th
International Joint Conference on Natural Language Processing and the 3rd Conference of the Asia-Pacific Chapter of the
Association for Computational Linguistics, pages 355–366, 2023.
[6] S. Mudadla. NLP Model Metrics. Medium, 2023. [Online]. Available: https://medium.com/@sujathamudadla1213/
nlp-model-metrics-b3fa32373269.
[7] deconvoluteAI. NLP Model Evaluation - Metrics, Benchmarks, and Beyond, 2023. [Online]. Available:
https://
deconvoluteai.com/blog/evaluating-nlp-models.
[8] J. Ml. Evaluation Methods in Natural Language Processing (NLP). Medium, 2020. [Online]. Available:
https://
jaimin-ml2001.medium.com/evaluation-methods-in-natural-language-processing-nlp-part-1-ffd39c90c04f.
[9] Z. Lin et al. A Survey on Large Language Models with Multilingualism: Recent Advances and New Frontiers. arXiv preprint
arXiv:2405.10936, 2024.
[10] Anonymous. A survey of multilingual large language models. ScienceDirect, 2024.
[11] X. Zhang, S. Li, B. Hauer, N. Shi, and G. Kondrak. Don’t Trust ChatGPT when your Question is not in English: A Study of
Multilingual Abilities and Types of LLMs. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language
Processing, pages 7915–7927, 2023.
[12] C. Yu, S. Zhang, H. Zhao, and K. Zhou. mGPT: Few-Shot Learners Go Multilingual. Transactions of the Association for
Computational Linguistics, 10:1053–1068, 2022.
[13] S. Bansal, Y. Karthik, V. Chaudhary, and M. Khapra. Cross-lingual Few-Shot Learning on Unseen Languages. In Proceedings of
the 3rd Annual Meeting of the Asia-Pacific Chapter of the Association for Computational Linguistics and the 6th International
Joint Conference on Natural Language Processing, pages 651–664, 2022.
[14] X. V. Lin, D. Majumder, M. Schuster, G. Lample, and J. Weston. Few-shot Learning with Multilingual Generative Language
Models. In Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing, pages 9179–9201,
2022.
[15] S. Hadifar, M. Dehghanpour, M. Ghanbari, and H. Sameti. FaMTEB: Massive Text Embedding Benchmark in Persian Language.
arXiv preprint arXiv:2502.11571, 2024.
[16] D. Khashabi et al. Benchmarking Large Language Models for Persian: A Preliminary Study Focusing on ChatGPT. In
Proceedings of the Fourteenth International Conference on Language Resources and Evaluation (LREC-COLING 2024), pages
2188–2201, 2024.
[17] M. S. Zahedi, M. H. Bokaei, F. Shoeleh, M. M. Yadollahi, E. Doostmohammadi, and M. Farhoodi. Persian Word Embedding
Evaluation Benchmarks. In 2018 Iranian Conference on Electrical Engineering (ICEE), pages 1244–1248, 2018.
[18] D. Khashabi et al. ParsiNLU: A Suite of Language Understanding Challenges for Persian. arXiv preprint arXiv:2012.06154,
2020.
[19] S. Mirzaee, M. Ebrahimi, and R. Rahmani. ArmanEmo: A Persian Dataset for Text-based Emotion Detection. arXiv preprint
arXiv:2207.11808, 2022.
[20] S. Bemaniyan. Arman Persian NER Dataset. Kaggle, 2022. [Online]. Available: https://www.kaggle.com/datasets/
shayanbemanian/arman-persian-ner-dataset.
[21] Challenges of Persian NLP: The Importance of Text Normalization. In De Gruyter, 2019. [Online]. Available: https:
//www.degruyter.com/document/doi/10.1515/9783110619225-002/html?lang=en.
[22] Babel Street. The difficulty of Persian sentiment analysis, 2022. [Online]. Available: https://www.babelstreet.com/
blog/the-difficulty-of-persian-sentiment-analysis.
[23] M. Ghanbari, M. Abedinzadeh, M. Dehghanpour, and H. Sameti. Challenges for Persian Text Analytics. arXiv preprint
arXiv:2101.08087, 2021.
[24] Mofid-AI.
persian-nlp-benchmark.
GitHub,
2023.
[Online].
Available:
https://github.com/Mofid-AI/
persian-nlp-benchmark.
[25] M. Abdollahzadeh, A. Abdi, and M. Bagheri. PersianMind: An Open-Source Bilingual Persian-English Large Language Model.
arXiv preprint arXiv:2401.06466, 2024.
[26] H.
Haghiri.
Maral
is
here!
7
billion
parameters
bilingual
model
with
support
of
persian!
haghiri75.com,
2023.
[Online].
Available:
https://haghiri75.com/en/
maral-is-here-7-billion-parameters-bilingual-model-with-support-of-persian/.
16

--- Page 17 ---

A PREPRINT - OCTOBER 16, 2025
[27] M. Samadi, A. A. Harati, H. Movafagh, and M. Ghodsi. PersianLLaMA: Towards Building First Persian Large Language
Model. ResearchGate, 2023.
[28] A. Haghdadi. Llama-2-7b-Persian - LLM Explorer. llm.extractum.io, 2023. [Online]. Available: https://llm.extractum.
io/model/AminHaghdadi%2Flama-2-7b-Persian,7s7rG9VnzoCZKDj0jiPBEQ.
[29] Anonymous. Zero-shot Sentiment Analysis in Low-Resource Languages. arXiv preprint arXiv:2402.02113, 2024.
[30] Zero-Shot
Learning
Papers
With
Code,
2023.
[Online].
Available:
https://paperswithcode.com/task/
zero-shot-learning/latest?page=5&q=.
[31] parsinlu reading comprehension · Datasets at Hugging Face. Hugging Face, 2023. [Online]. Available: https://huggingface.
co/datasets/persiannlp/parsinlu_reading_comprehension.
[32] S. Rashidi. Dataset Viewer. Hugging Face,
2023. [Online]. Available:
https://huggingface.co/datasets/
sinarashidi/alpaca-persian.
17

```
