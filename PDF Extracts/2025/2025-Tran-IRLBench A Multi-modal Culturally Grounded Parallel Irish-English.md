---
title: "2025-Tran-IRLBench A Multi-modal Culturally Grounded Parallel Irish-English - PDF Extract"
source_pdf: "2025-Tran-IRLBench A Multi-modal Culturally Grounded Parallel Irish-English.pdf"
pages: 12
extracted_at: "2026-02-15T17:54:28.561540"
---

# PDF Extract: 2025-Tran-IRLBench A Multi-modal Culturally Grounded Parallel Irish-English

**Source PDF:** 2025-Tran-IRLBench A Multi-modal Culturally Grounded Parallel Irish-English.pdf
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

arXiv:2505.13498v1  [cs.CL]  16 May 2025
IRLBench: A Multi-modal, Culturally Grounded,
Parallel Irish-English Benchmark for Open-Ended
LLM Reasoning Evaluation
Khanh-Tung Tran
University College Cork
Cork, Ireland
123128577@umail.ucc.ie
Barry O’Sullivan
University College Cork
Cork, Ireland
b.osullivan@cs.ucc.ie
Hoang D. Nguyen
University College Cork
Cork, Ireland
hn@cs.ucc.ie
Abstract
Recent advances in Large Language Models (LLMs) have demonstrated promis-
ing knowledge and reasoning abilities, yet their performance in multilingual and
low-resource settings remains underexplored. Existing benchmarks often exhibit
cultural bias, restrict evaluation to text-only, rely on multiple-choice formats, and,
more importantly, are limited for extremely low-resource languages. To address
these gaps, we introduce IRLBench, presented in parallel English and Irish, which
is considered definitely endangered by UNESCO. Our benchmark consists of 12
representative subjects developed from the 2024 Irish Leaving Certificate exams,
enabling fine-grained analysis of model capabilities across domains. By framing
the task as long-form generation and leveraging the official marking scheme, it does
not only support a comprehensive evaluation of correctness but also language fi-
delity. Our extensive experiments of leading closed-source and open-source LLMs
reveal a persistent performance gap between English and Irish, in which models
produce valid Irish responses less than 80% of the time, and answer correctly
55.8% of the time compared to 76.2% in English for the best-performing model.
We release IRLBench1 and an accompanying evaluation codebase2 to enable future
research on robust, culturally aware multilingual AI development.
1
Introduction
Large Language Models (LLMs) and their variants, including Vision–Language Models (VLMs) and
Large Reasoning Models (LRMs), have recently achieved remarkable reasoning performance [1, 2],
reshaping the field of natural language processing and rapidly overtaking traditional benchmarks
[3]. As capabilities have advanced, existing reasoning benchmarks, such as mathematical and STEM
reasoning, once considered challenging, have become saturated, prompting the community to develop
more rigorous and advanced evaluations to probe the limits of current models [4, 5]. However, these
benchmarking efforts predominantly focus on resource-rich and dominant languages such as English.
Consequently, performance in other languages remains poorly understood, and the unique challenges
of low-resource settings remain under-explored [6, 7].
Multilingual benchmarks that do exist often suffer from several shortcomings. They may embed
cultural bias, limit themselves to text-only questions, rely on multiple-choice formats, or omit ex-
tremely low-resourced languages. This leads to known-limitations such as memorization problem and
unable to test language generation capability in multi-choice benchmark. Moreover, the translation of
English-centric benchmarks into other languages often proves insufficient, as the resulting tasks may
1https://huggingface.co/datasets/ReliableAI/IRLBench
2https://github.com/ReML-AI/IRLBench
Preprint. Under review.

--- Page 2 ---

Figure 1: Performance of State-of-the-Art models on recent Irish benchmarks compared to IRLBench.
We benchmark more models on IRLBench in Section 4.
not correlate effectively with local human preferences and knowledge contexts [8, 3]. A key example
of such a gap is Irish, classified as definitely endangered by UNESCO [9]. Irish currently lacks
detailed, open-ended evaluation datasets. Existing Irish datasets (e.g., SIB200 [10], Belebele [11],
IrishQA [12]) focus on more traditional tasks (e.g., topic classification), and are quickly saturated
by state-of-the-art models, with accuracy rates approaching 90%, leaving little room for meaningful
comparison or deeper analysis of multilingual transfer, as shown in Figure 1.
To address these issues, we introduce IRLBench, a novel multimodal, culturally grounded, parallel
English–Irish benchmark for open-ended evaluation. Inspired by recent studies leveraging educational
materials as benchmarks [13], IRLBench is derived directly from the 2024 Irish Leaving Certificate
exams. It comprises twelve representative subjects grouped into four key domains: Science, Applied
Science, Business Studies, and Social Studies. To construct the dataset, we collected official exam
papers and corresponding marking schemes in PDF format, employing an automated vision-language
pipeline to extract and format content efficiently. A final human verification step ensures high data
quality and accuracy. Because each exam is available in parallel English and Irish versions, with
identical content, IRLBench naturally supports direct multilingual comparisons. By formulating
each question as a long-form, open-ended generation task aligned with official marking criteria,
the benchmark enables comprehensive evaluation of factual correctness, domain-specific academic
knowledge, linguistic fidelity, and depth of reasoning simultaneously in both languages (Figure 2).
Furthermore, IRLBench includes multimodal questions, requiring models to interpret figures, tables,
and diagrams alongside textual descriptions, as shown in Figure 2, where a Chemistry question
necessitates understanding of an associated diagram depicting a chemical process.
We conduct extensive experiments on leading closed-source (e.g., gpt-4.1, gemini-2.0-flash) and
open-source (e.g., Llama-4-Scout-Instruct) models. Using LLM-as-a-judge for automatic evaluation
[14, 15], our results reveal a persistent performance gap between English and Irish: the best model
achieves 76.2% accuracy in English but only 55.8% in Irish, and produces responses in Irish less than
80% of the time. These findings underscore both the challenge of open-ended academic reasoning in
low- and extremely low-resource languages, and the importance of multimodal, culturally grounded
evaluation.
Our key contributions are as follows:
• IRLBench. We introduce IRLBench, a parallel Irish-English, multimodal, open-ended
academic reasoning dataset drawn from the 2024 Irish Leaving Certificate,
• Comprehensive Evaluation. We systematically evaluate a range of closed- and open-source
LLMs, analyzing their performance across language (English vs. Irish) and domain (Science,
Applied Science, Business Studies, and Social Studies).
• Insights on Multilingual Transfer. Our experiments reveal a significant English-Irish
performance gap (upto 20% for SoTA models), quantify models’ language fidelity (where
models struggling to generate output in target language), and identify subject areas where
2

--- Page 3 ---

Physics & Chemistry
History
Irish
English
Either of the following answers is acceptable.
- calcium dicarbide
- 
Taispeántar sa léaráid gaireas a
úsáidtear chun gás eitín a ullmhú trí
uisce a dhoirteadh ar sholad Q.
Sainaithin solad Q. 
The diagram shows an apparatus
used to  prepare ethyne gas by
dropping water onto a solid Q.
Identify solid Q. 
Tá ceachtar de na freagraí seo inghlactha.
- déchairbíd chailciam
- 
Irish
English
TWO elements: Coleraine + Civil Rights.
To mark the answer, the examiner will divide the answer into
paragraphs or paragraph equivalents:
(i) A relevant introduction giving the background situation
and/or defining the terms and explaining the approach;
(ii) An episode, phase or stage in a sequence of events;
...
Cén tionchar a bhí ag conspóid Ollscoil Chúil Raithin agus ag
an ngluaiseacht Cearta Sibhialta ar Dhoire ó lár go deireadh
na 1960idí?
How did the Coleraine University controversy and the Civil
Rights movement affect Derry in the mid-to-late 1960s?
DHÁ ghné: Cúil Raithin + Cearta Sibhialta
Chun an freagra a mharcáil,  roinnfidh an scrúdaitheoir an
freagra ina ailt nó a chomhionannas:
(i) Réamhrá ábhartha ina dtráchtar ar chúlra an cháis agus/nó
ina leagtar síos na téarmaí agus ina mínítear an cur chuige;
(ii) Eachtra, ré nó céim in ord na n-imeachtaí;
...
Figure 2: Illustrative examples showcasing the Irish-English parallel nature and the diverse tasks of
IRLBench dataset.
Dataset
Multilingual
Parallel
Culture aware
Multi-task
Multi-modal
Evaluation
MGSM [16]
✓
✓
✗
✗
✗
multi-choice
Global_MMLU [17]
✓
✓
✓
✓
✗
multi-choice
MMMLU
✓
✓
✗
✓
✗
multi-choice
M3Exam [18]
✓
✗
✓
✓
✓
multi-choice
HLE [5]
✗
✗
✗
✓
✓
open-ended
IRLBench (OURs)
✓
✓
✓
✓
✓
open-ended
Table 1: Comparison of IRLBench and other related low-resource scenario benchmarks.
multilingual transfer is particularly weak, providing potential directions for future research
on low-resource, open-ended reasoning.
2
Related Works
Multilingual Reasoning benchmark. Recent multilingual reasoning datasets have attempted to
evaluate LLMs across multiple languages. For instance, MGSM [16], a multilingual variant of
GSM8K [19], provides human-translated arithmetic word problems in 10 languages, including two
extremely low-resource languages. However, these problems predominantly reflect U.S.-centric con-
texts, introducing potential cultural biases. Another notable benchmark, MMLU (Massive Multitask
Language Understanding) [20], has inspired multilingual derivatives: MMMLU3, a professionally
translated set of MMLU questions across 14 languages, and Global_MMLU [17], which highlights
cultural biases by identifying that approximately 28% of original MMLU questions heavily rely on
Western-centric concepts. To mitigate this, Global_MMLU categorizes its dataset into culturally
sensitive and culturally agnostic subsets across 42 languages. Further, there have been efforts to create
language-specific variants of MMLU using local exam questions and educational materials. Examples
include CMMLU (Chinese)[21], KMMLU (Korean)[22], and ArabicMMLU (Arabic)[23]. Recently,
M3Exam addressed cultural bias by collecting real-world exam questions from various countries,
but its non-parallel structure across languages limits fair cross-lingual comparisons. Moreover, all
these aforementioned benchmarks primarily use multiple-choice or short-answer questions, testing
factual recall rather than in-depth generative reasoning. Such tasks risk memorization biases and fail
to rigorously assess the language generation capabilities of models[24].
3https://huggingface.co/datasets/openai/MMMLU
3

--- Page 4 ---

Data
Extraction
Data
Verification
Data
Collection
Exam-Marking Scheme
Image Pair
Question-Marking
Scheme Dataset
Official Grouping
Science
1. Math
2. Physics
3. Chemistry
1. Phys.&Chem.
2. Comp. Science
3. Technology
1. Accounting
2. Business
3. Economics
1. Art
2. Politics&Society
3. History
Irish Leaving Certificate
Examination 2024
Applied
Science
Business
Studies
Social
Studies
Selected Representatives Subjects
Vision-Language
Model
Extract and Match
Vision-Language
Model
Q1-MS1
Qn-MSn
...
- Correct pairs
- Missing questions/
marking schemes
- Format consistent
Refined Dataset
Q1-MS1
Qn-MSn
...
Human
Annotators
Common Errors:
- Repetition errors
- Typo errors
- Missing pairs
IRLBench
Multi-modal,
Culturally Grounded,
Parallel Irish-English
Benchmark
Figure 3: Pipeline.
Recent English-centric datasets, including SPIQA [25] and Humanity’s Exam [5], have transitioned
towards open-ended, free-form generative evaluation. However, there is still a need for such datasets
for extremely low-resource languages. Our work extends this direction by introducing IRLBench,
the first multilingual, culturally grounded, parallel benchmark specifically designed for open-ended
generative evaluation in an extremely low-resource language scenario, Irish. Table 1 provides a
comparative summary highlighting IRLBench’s unique features relative to existing multilingual
benchmarks.
Benchmarks for the Irish Language. Irish, classified as definitely endangered by UNESCO,
significantly lacks resources for AI and natural language processing development. Current datasets,
such as IrishQA [12] or multilingual benchmarks including SIB200 [10] and Belebele [10], primarily
target language understanding tasks such as topic classification. These datasets have been rapidly
saturated by SoTA LLMs, achieving accuracies approaching 90% (as shown in Figure 1), which limits
their effectiveness in differentiating model capabilities and analyzing deeper aspects of multilingual
reasoning and transfer. IRLBench aims to fill this critical gap by providing challenging, multimodal,
open-ended tasks that comprehensively evaluate the generative reasoning abilities of models in both
Irish and English.
3
IRLBench
In this section, we provide a detailed description of IRLBench, covering our data collection method-
ology, dataset composition, and benchmarking task designed to evaluate SoTA LLMs. First, we
outline our automated extraction pipeline and subsequent human verification process. Next, we
present the dataset’s composition, organized by subjects and subject groups. Finally, we discuss our
4

--- Page 5 ---

proposed evaluation procedure, highlighting how IRLBench effectively assesses models’ open-ended
generative abilities in extremely low-resource multilingual scenarios.
3.1
Data Collection
The Irish Leaving Certificate is Ireland’s final secondary-school system examination, which also
serves as the standard university matriculation examination, typically requiring students at least two
years of preparation4. Exams are available in parallel Irish and English versions, accompanied by
standardized marking schemes, and cover five broad subject groups: Languages, Natural Sciences,
Applied Sciences, Social Sciences, and Business Studies. Each subject can be examined at one of three
difficulty levels: Higher (informally called Honours), Ordinary (Pass), or Foundation, with Higher
Level exams posing the most difficult challenge. To rigorously evaluate SoTA LLMs, IRLBench
exclusively includes Higher Level exams. Additionally, to facilitate direct performance comparisons
between English and Irish and to avoid confounding effects from language-specific content, we
exclude the Languages subject group, which is only available in one language. From each remaining
group, we select three representative subjects, forming a diverse set of 12 subjects. Each subject’s
official marking scheme enables precise and structured evaluation. The structure and characteristics
of the selected exams are illustrated in the upper portion of Figure 3, and example question-marking
scheme pairs are provided in Figure 2, demonstrating the multi-modal, parallel, and diverse nature of
IRLBench.
The original exam papers and marking schemes are publicly available as PDFs containing complex
layouts with embedded tables, figures, and equations5. Given the challenges in accurately converting
these documents into editable formats (e.g., Markdown or Word), we process them directly as images.
To achieve efficient and accurate extraction, we leverage the frontier VLM gemini-2.0-flash, chosen
for its strong performance in agentic tasks and cost-effectiveness [26, 27]. Specifically, the model
extracts pairs of exam questions and corresponding marking schemes from the PDF images, aligning
textual and graphical elements, as illustrated in the lower part of Figure 3.
The initial extraction result reveal several systematic issues, including incorrect question-marking
scheme pairings, incomplete graphic extraction, and inconsistent formatting (in table and equations).
To address these challenges before human annotation, we implement an automated verification step
using the same VLM. This step significantly reduce systemic errors by detecting misalignments
and extraction inaccuracies. Then, human annotators is only involved in a final verification phase,
manually resolving the three most common remaining issues: duplicated outputs (primarily from
lengthy Irish text segments), typographical mistakes, and missing question-scheme pairs. The
resulting benchmark, IRLBench, is a multimodal, culturally grounded dataset with parallel Irish-
English samples, enabling detailed evaluation of multilingual academic reasoning capabilities.
3.2
Data Statistics
IRLBench consists of 1700 samples, each containing a pair of question and marking scheme developed
from the 2024 Irish Leaving Certificate exams. Samples are equally distributed between English and
Irish, with parallel content for comparative evaluation. Additionally, 18.11% of these samples contain
graphical illustrations, enabling multi-modal assessment.
Table 2 summarizes the dataset distribution across four subject groups: Science, Applied Science,
Business Studies, and Social Studies. The Applied Science group has the highest number of samples
(590), primarily from Physics and Chemistry (370). Science follows closely with 5982 samples,
with Chemistry (256) and Physics (216) comprising the majority. Business Studies contains 326
samples, evenly split between Business and Economics, but with fewer samples from Accounting.
Social Studies is the smallest group, but still consists of 202 samples, distributed among History
(106), Politics and Society (56), and Art (40).
Figure 4 visualizes the proportional distribution of these samples, showing the dominance of Applied
Science and Science, highlighting their substantial representation within IRLBench. This structured
diversity allows fine-grained analyses across subjects and language modalities, providing a robust
foundation for evaluating multilingual and multimodal generative capabilities.
4https://en.wikipedia.org/wiki/Leaving_Certificate_%28Ireland%29
5https://www.studyclix.ie
5

--- Page 6 ---

Table 2: Amount of samples collected
for IRLBench. Each sample is a pair of
question and marking scheme, including
both text and illustrations in the original
Leaving Certificate exam. 18.11% of the
samples include graphical illustrations,
and the amount of samples are equally
split between English and Irish, with the
same task contents.
Group
Subject
Samples Group
Subject
Samples
Science
Math
110
Business
Studies
Business
132
Physics
216
Accounting
62
Chemistry
256
Economics
132
Total
582
Total
326
Applied
Science
Physics and
Chemistry
370
Social
Studies
Art
40
Computer
Science
100
Politics and
Society
56
Technology
120
History
106
Total
590
Total
202
Total samples across all groups: 1700
Figure 4: Distributions of subject groups
and subjects as percentages of total
amount of samples in IRLBench.
3.3
Benchmarking Task
Evaluating open-ended generation tasks poses significant challenges, as answers that are correct often
vary widely in wording and detail, making traditional metrics like BLEU [28] and ROUGE [29]
inadequate. Recent works [30, 14, 15] address these limitations by leveraging instruction-tuned LLMs
as automated evaluators, utilizing their inherent ability to assess natural language outputs in context.
Following this approach of LLM-as-a-judge, we employ an evaluation strategy combined with official
marking schemes to reliably assess performance on IRLBench. We select gemini-2.5-flash [26] as
our evaluation model due to its strong performance in instruction-following and reasoning tasks. For
each evaluation, the judge model receives a prompt containing the original exam question, its official
marking scheme, and the candidate model’s generated response. The judge then assigns a binary label:
correct or incorrect, simplifying the evaluation task and reducing the inherent variability associated
with LLM-based evaluation. Although this binary judgement deviates somewhat from the granular
scoring outlined in official marking schemes, it ensures consistent and comparable performance
metrics across benchmarked models.
In addition to evaluating correctness, we assess the capability of models to generate text in Irish,
an extremely low-resource language. To this end, we use a FastText-based language identification
model [31, 32] to determine the language of responses generated for Irish-language questions. As the
language detection model operates at the sentence level, we split generated answers into individual
sentences. If more than 50% of sentences are detected as English rather than Irish, we classify the
entire response as non-Irish. This criterion provides an estimate of language fidelity, emphasizing
models’ practical ability to handle extremely low-resource multilingual generation tasks.
Finally, we benchmark and compare prominent SoTA VLMs. This includes leading closed-source
commercial models such as o4-mini [33], gpt-4.1 [34], and gemini-2.0-flash, known for their superior
performance across various reasoning tasks, as well as open-source models, notably Llama-4-Scout-
Instruct [35] and the aya-vision series (32B and 8B parameters) [36].
4
Results and Analysis
4.1
Performance Gap Between Irish and English
Figure 5 compares the accuracy scores of various models evaluated on IRLBench, segmented by
language (English vs. Irish). Our results highlight that open-ended reasoning remains substantially
more challenging in extremely low-resource languages such as Irish. On the English split, the
top-performing model, o4-mini, achieves a strong average accuracy of 76.2%, closely followed by
gpt-4.1 at 71.3%. In contrast, all evaluated models demonstrate considerably lower accuracy on the
6

--- Page 7 ---

Figure 5: Accuracy scores on IRLBench per model and language.
Irish version, scoring below 60% despite being presented with the same questions but written in Irish.
This indicates a persistent performance gap exceeding 10% between the two languages across all
models.
Generally, models with superior performance on English also perform relatively better on Irish.
However, reasoning-adapted models (e.g., through reinforcement learning with test-time scaling),
such as o4-mini, exhibit a notably larger gap (20.4%) compared to more general models like gpt-4.1
(12.9%) and gemini-2.0-flash (17.9%). This suggests that current SoTA models, particularly those
optimized explicitly for reasoning, have not adequately addressed multilingual transfer, resulting in
pronounced performance disparities in low-resource language contexts.
4.2
Performance Across Subject Groups
Table 3 summarizes model accuracy across IRLBench’s subject groups, providing detailed compar-
isons between English and Irish performance. On the English subset, o4-mini achieves the highest
overall accuracy (76.17%), followed by gpt-4.1 (71.29%). In general, open-source models lag behind
their closed-source counterparts, particularly in science-focused categories (Science and Applied
Science). However, an interesting exception occurs in the Social Studies group, where the open-
source model Llama-4-Scout-Instruct outperforms the closed-source Gemini-2.0-Flash by a margin
of 1.98%.
Noteably, performance gaps are even more significant in Irish, with smaller open-source models
(aya-vision-32b and aya-vision-8b) failing almost entirely. Additionally, a consistent trend emerges:
models excelling in English tend to perform better in Irish as well, underscoring that underlying
reasoning proficiency strongly influences multilingual transfer. This result emphasizes the importance
of robust linguistic and reasoning abilities in achieving strong multilingual generalization.
4.3
Error Analysis: Correctness vs. Language Fidelity
Beyond correctness, we also evaluate the ability of models to generate text in Irish, an extremely
low-resource language. We employ a FastText-based language identification model [32] trained
7

--- Page 8 ---

Model
Split
Science
Applied
Science
Business
Studies
Social
Studies
Average
aya-vision-8b
English
32.31
36.77
37.43
63.37
38.55
aya-vision-32b
42.76
47.11
44.17
71.29
48.36
Llama-4-Scout-Instruct
61.26
57.91
60.73
78.22
62.99
gemini-2.0-flash
62.77
61.83
60.12
76.24
64.41
o4-mini
77.06
73.35
71.16
81.19
76.17
gpt-4.1
72.21
68.44
68.10
72.28
71.29
aya-vision-8b
Irish
0.22
0.00
0.62
1.00
0.36
aya-vision-32b
1.77
1.00
0.62
7.92
2.27
Llama-4-Scout-Instruct
34.10
39.31
44.98
49.50
39.67
gemini-2.0-flash
45.35
38.08
47.85
67.32
46.54
o4-mini
51.58
49.87
53.99
72.28
55.82
gpt-4.1
54.12
54.31
60.12
73.27
58.43
Table 3: Model performances per subject group and language of IRLBench.
Figure 6: Percentage of responses generated by models that are in Irish (on Irish split of IRLBench).
specifically for language detection to classify each response at the sentence level. Responses
containing more than 50% English sentences are considered non-Irish, representing a lower bound
for language fidelity.
Figure 6 illustrates the proportion of responses produced in Irish, split by categories: for all responses,
in correct responses only, or in incorrect responses only. We exclude models with extremely low
accuracy (shown in previous results) due to insufficient valid samples for analysis. The analysis
reveals that most evaluated models (with the exception of gpt-4.1) produce valid Irish responses less
than 80% of the time, underscoring significant gaps in generative proficiency. Moreover, there is a
clear correlation between correctness and the capability to generate outputs in Irish (The percentage
in Correct responses compared to the percentage in Incorrect responses), a gap of at least 6.3% in
gpt-4.1, suggesting interdependence between reasoning and language-generation skills. This result
also highlights a notable limitation of previous benchmarks, which often rely on multiple-choice
formats and thus do not adequately measure generative language capabilities.
4.4
Confidence Analysis
Finally, following the methodology proposed in [37], we analyze models’ self-reported confidence
alongside their responses, by directly prompting them to output their confidence, alongside their
response to the task. Figure 7 compares actual model accuracy against their self-assessed confidence
8

--- Page 9 ---

Figure 7: Model self-reported confidences compared to performances [37].
scores. Ideally, well-calibrated models should demonstrate a close alignment between confidence
and accuracy (e.g., 90% confidence corresponding to 90% accuracy). However, all models evaluated
on IRLBench display substantial discrepancies, exhibiting overly high confidence, all above 80%,
relative to actual performance where they all achieve less than 60% score on Irish split. For example,
aya-vision-32b maintains relatively high confidence, above 90%, and even increased for Irish tassk,
despite an accuracy rate of only 2.3%, a significant drop exceeding 40% from English to Irish. Such
miscalibration could mislead users who rely on confidence scores to assess response reliability. This
poor calibration likely arises from models’ intrinsic next-token prediction mechanisms, prone to
hallucinations and overly optimistic self-assessments.
5
Conclusion
We introduce IRLBench, the first multilingual, multi-modal benchmark specifically designed for open-
ended generative evaluation in extremely low-resource scenario. As we detail our extraction pipeline
from the 2024 Irish Leaving Certificate examination, IRLBench enables an in-depth assessment of
multilingual transferability and academic reasoning capabilities of SoTA LLMs in both Irish and
English. Our systematic evaluations reveal substantial performance gaps between the two languages
(more than 10% across all models), underscoring the significant challenges that persist in multilingual
reasoning tasks, particularly in resource-limited contexts.
Limitations and Societal Impact. Our benchmark currently addresses a single extremely low-
resource language scenario (Irish). Furthermore, the current evaluation methodology leverages an
LLM-as-a-judge paradigm, which may present challenges in scalability and robustness. Despite these
limitations, the clear performance disparities identified by IRLBench highlight critical gaps in current
LLMs, emphasizing the importance of developing robust multilingual generative capabilities. By
releasing IRLBench, we hope to foster future research towards improving model performance and
linguistic diversity in natural language processing.
Disclaimer. The data used throughout this research is based on the Regulations on Re-use of Public
Sector Information Regulations 2005 (SI 279 of 2005), and should be used for non-commercial
research and study only.
9

--- Page 10 ---

References
[1] A. Cherian, K.-C. Peng, S. Lohit, J. Matthiesen, K. A. Smith, and J. B. Tenenbaum, “Evaluating
large vision-and-language models on children’s mathematical olympiads,” in The Thirty-eight
Conference on Neural Information Processing Systems Datasets and Benchmarks Track, 2024.
[2] J. Huang and K. C.-C. Chang, “Towards reasoning in large language models: A survey,” in Find-
ings of the Association for Computational Linguistics: ACL 2023 (A. Rogers, J. Boyd-Graber,
and N. Okazaki, eds.), (Toronto, Canada), pp. 1049–1065, Association for Computational
Linguistics, July 2023.
[3] M. Wu, W. Wang, S. Liu, H. Yin, X. Wang, Y. Zhao, C. Lyu, L. Wang, W. Luo, and K. Zhang,
“The bitter lesson learned from 2,000+ multilingual benchmarks,” 2025.
[4] H. Sun, Y. Min, Z. Chen, W. X. Zhao, Z. Liu, Z. Wang, L. Fang, and J.-R. Wen, “Challenging
the boundaries of reasoning: An olympiad-level math benchmark for large language models,”
2025.
[5] L. Phan et al., “Humanity’s last exam,” 2025.
[6] A. Ghosh, D. Datta, S. Saha, and C. Agarwal, “The multilingual mind : A survey of multilingual
reasoning in language models,” 2025.
[7] K.-T. Tran, B. O’Sullivan, and H. D. Nguyen, “Scaling test-time compute for low-resource
languages: Multilingual reasoning in llms,” 2025.
[8] M. F. Adilazuarda, S. Mukherjee, P. Lavania, S. S. Singh, A. F. Aji, J. O’Neill, A. Modi,
and M. Choudhury, “Towards measuring and modeling “culture” in LLMs: A survey,” in
Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing
(Y. Al-Onaizan, M. Bansal, and Y.-N. Chen, eds.), (Miami, Florida, USA), pp. 15763–15784,
Association for Computational Linguistics, Nov. 2024.
[9] UNESCO, ed., Atlas of the world’s languages in danger. Memory of Peoples Series, UNESCO,
3 ed., Feb. 2010.
[10] D. I. Adelani, H. Liu, X. Shen, N. Vassilyev, J. O. Alabi, Y. Mao, H. Gao, and E.-S. A. Lee, “SIB-
200: A simple, inclusive, and big evaluation dataset for topic classification in 200+ languages
and dialects,” in Proceedings of the 18th Conference of the European Chapter of the Association
for Computational Linguistics (Volume 1: Long Papers) (Y. Graham and M. Purver, eds.), (St.
Julian’s, Malta), pp. 226–245, Association for Computational Linguistics, Mar. 2024.
[11] L. Bandarkar, D. Liang, B. Muller, M. Artetxe, S. N. Shukla, D. Husa, N. Goyal, A. Krishnan,
L. Zettlemoyer, and M. Khabsa, “The belebele benchmark: a parallel reading comprehension
dataset in 122 language variants,” in Proceedings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), (Bangkok, Thailand and virtual
meeting), pp. 749–775, Association for Computational Linguistics, Aug. 2024.
[12] K.-T. Tran, B. O’Sullivan, and H. D. Nguyen, “Uccix: Irish-excellence large language model,”
ECAI 2024, 2024.
[13] S. Pawar, J. Park, J. Jin, A. Arora, J. Myung, S. Yadav, F. G. Haznitrama, I. Song, A. Oh, and
I. Augenstein, “Survey of cultural awareness in language models: Text and beyond,” 2024.
[14] L. Zheng, W.-L. Chiang, Y. Sheng, S. Zhuang, Z. Wu, Y. Zhuang, Z. Lin, Z. Li, D. Li, E. Xing,
H. Zhang, J. E. Gonzalez, and I. Stoica, “Judging LLM-as-a-judge with MT-bench and chatbot
arena,” in Thirty-seventh Conference on Neural Information Processing Systems Datasets and
Benchmarks Track, 2023.
[15] J. Ye, Y. Wang, Y. Huang, D. Chen, Q. Zhang, N. Moniz, T. Gao, W. Geyer, C. Huang, P.-Y.
Chen, N. V. Chawla, and X. Zhang, “Justice or prejudice? quantifying biases in LLM-as-a-judge,”
in The Thirteenth International Conference on Learning Representations, 2025.
[16] F. Shi, M. Suzgun, M. Freitag, X. Wang, S. Srivats, S. Vosoughi, H. W. Chung, Y. Tay, S. Ruder,
D. Zhou, D. Das, and J. Wei, “Language models are multilingual chain-of-thought reasoners,”
in The Eleventh International Conference on Learning Representations, 2023.
[17] S. Singh, A. Romanou, C. Fourrier, D. I. Adelani, J. G. Ngui, D. Vila-Suero, P. Limkonchotiwat,
K. Marchisio, W. Q. Leong, Y. Susanto, R. Ng, S. Longpre, W.-Y. Ko, S. Ruder, M. Smith,
A. Bosselut, A. Oh, A. F. T. Martins, L. Choshen, D. Ippolito, E. Ferrante, M. Fadaee, B. Ermis,
and S. Hooker, “Global mmlu: Understanding and addressing cultural and linguistic biases in
multilingual evaluation,” 2025.
10

--- Page 11 ---

[18] W. Zhang, M. Aljunied, C. Gao, Y. K. Chia, and L. Bing, “M3exam: A multilingual, multimodal,
multilevel benchmark for examining large language models,” in Thirty-seventh Conference on
Neural Information Processing Systems Datasets and Benchmarks Track, 2023.
[19] K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek,
J. Hilton, R. Nakano, C. Hesse, and J. Schulman, “Training verifiers to solve math word
problems,” arXiv preprint arXiv:2110.14168, 2021.
[20] D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt, “Measuring
massive multitask language understanding,” Proceedings of the International Conference on
Learning Representations (ICLR), 2021.
[21] H. Li, Y. Zhang, F. Koto, Y. Yang, H. Zhao, Y. Gong, N. Duan, and T. Baldwin, “CMMLU:
Measuring massive multitask language understanding in Chinese,” in Findings of the Association
for Computational Linguistics: ACL 2024 (L.-W. Ku, A. Martins, and V. Srikumar, eds.),
(Bangkok, Thailand), pp. 11260–11285, Association for Computational Linguistics, Aug. 2024.
[22] G. Son, H. Lee, S. Kim, S. Kim, N. Muennighoff, T. Choi, C. Park, K. M. Yoo, and S. Biderman,
“KMMLU: Measuring massive multitask language understanding in Korean,” in Proceedings
of the 2025 Conference of the Nations of the Americas Chapter of the Association for Compu-
tational Linguistics: Human Language Technologies (Volume 1: Long Papers) (L. Chiruzzo,
A. Ritter, and L. Wang, eds.), (Albuquerque, New Mexico), pp. 4076–4104, Association for
Computational Linguistics, Apr. 2025.
[23] F. Koto, H. Li, S. Shatnawi, J. Doughman, A. Sadallah, A. Alraeesi, K. Almubarak, Z. Alyafeai,
N. Sengupta, S. Shehata, N. Habash, P. Nakov, and T. Baldwin, “ArabicMMLU: Assessing
massive multitask language understanding in Arabic,” in Findings of the Association for Com-
putational Linguistics: ACL 2024 (L.-W. Ku, A. Martins, and V. Srikumar, eds.), (Bangkok,
Thailand), pp. 5622–5640, Association for Computational Linguistics, Aug. 2024.
[24] E. S. Salido, J. Gonzalo, and G. Marco, “None of the others: a general technique to distinguish
reasoning from memorization in multiple-choice llm evaluation benchmarks,” 2025.
[25] S. Pramanick, R. Chellappa, and S. Venugopalan, “SPIQA: A dataset for multimodal ques-
tion answering on scientific papers,” in The Thirty-eight Conference on Neural Information
Processing Systems Datasets and Benchmarks Track, 2024.
[26] Google, “Introducing gemini 2.0: our new ai model for the agentic era,” 2024.
[27] Google, “Gemini 2.0: Flash, flash-lite and pro,” 2025.
[28] K. Papineni, S. Roukos, T. Ward, and W.-J. Zhu, “Bleu: a method for automatic evaluation of
machine translation,” in Proceedings of the 40th Annual Meeting of the Association for Compu-
tational Linguistics (P. Isabelle, E. Charniak, and D. Lin, eds.), (Philadelphia, Pennsylvania,
USA), pp. 311–318, Association for Computational Linguistics, July 2002.
[29] C.-Y. Lin, “ROUGE: A package for automatic evaluation of summaries,” in Text Summarization
Branches Out, (Barcelona, Spain), pp. 74–81, Association for Computational Linguistics, July
2004.
[30] C. Zhou, P. Liu, P. Xu, S. Iyer, J. Sun, Y. Mao, X. Ma, A. Efrat, P. Yu, L. YU, S. Zhang,
G. Ghosh, M. Lewis, L. Zettlemoyer, and O. Levy, “LIMA: Less is more for alignment,” in
Thirty-seventh Conference on Neural Information Processing Systems, 2023.
[31] A. Joulin, E. Grave, P. Bojanowski, and T. Mikolov, “Bag of tricks for efficient text classification,”
arXiv preprint arXiv:1607.01759, 2016.
[32] A. Joulin, E. Grave, P. Bojanowski, M. Douze, H. Jégou, and T. Mikolov, “Fasttext.zip: Com-
pressing text classification models,” arXiv preprint arXiv:1612.03651, 2016.
[33] OpenAI, “Introducing openai o3 and o4-mini,” 2025.
[34] OpenAI, “Introducing gpt-4.1 in the api,” 2025.
[35] M. AI, “The llama 4 herd: The beginning of a new era of natively multimodal ai innovation,”
2025.
[36] S. Dash, Y. Nan, J. Dang, A. Ahmadian, S. Singh, M. Smith, B. Venkitesh, V. Shmyhlo,
V. Aryabumi, W. Beller-Morales, J. Pekmez, J. Ozuzu, P. Richemond, A. Locatelli, N. Frosst,
P. Blunsom, A. Gomez, I. Zhang, M. Fadaee, M. Govindassamy, S. Roy, M. Gallé, B. Ermis,
A. Üstün, and S. Hooker, “Aya vision: Advancing the frontier of multilingual multimodality,”
2025.
11

--- Page 12 ---

[37] J. Wei, N. Karina, H. W. Chung, Y. J. Jiao, S. Papay, A. Glaese, J. Schulman, and W. Fedus,
“Measuring short-form factuality in large language models,” 2024.
12

```
