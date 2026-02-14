---\ntitle: "2025-[[Unknown]]-Benchmarking Hindi LLMs A New Suite - PDF Extract"\nsource_pdf: "2025/2025-[[Unknown]]-Benchmarking Hindi LLMs A New Suite.pdf"\npages: 17\nextracted_at: "2026-02-14T02:17:31.025460"\n---\n\n# PDF Extract: 2025-[[Unknown]]-Benchmarking Hindi LLMs A New Suite\n\n**Source PDF:** 2025/2025-[[Unknown]]-Benchmarking Hindi LLMs A New Suite.pdf\n**Total Pages:** 17\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nBenchmarking Hindi LLMs: A New Suite of Datasets and a Comparative
Analysis
Anusha Kamath, Kanishk Singla, Rakesh Paul, Raviraj Joshi,
Utkarsh Vaidya, Sanjay Singh Chauhan, Niranjan Wartikar
NVIDIA
{anushak, kanishks, rapaul, ravirajj, uvaidya,
schauhan, nwartikar}@nvidia.com
Abstract
Evaluating instruction-tuned Large Language
Models (LLMs) in Hindi is challenging due to a
lack of high-quality benchmarks, as direct trans-
lation of English datasets fails to capture cru-
cial linguistic and cultural nuances. To address
this, we introduce a suite of five Hindi LLM
evaluation datasets: IFEval-Hi, MT-Bench-
Hi, GSM8K-Hi, ChatRAG-Hi, and BFCL-Hi.
These were created using a methodology that
combines from-scratch human annotation with
a translate-and-verify process. We leverage this
suite to conduct an extensive benchmarking of
open-source LLMs supporting Hindi, providing
a detailed comparative analysis of their current
capabilities. Our curation process also serves as
a replicable methodology for developing bench-
marks in other low-resource languages.
1
Introduction
The rapid expansion of Large Language Models
(LLMs) necessitates the development of robust and
reliable evaluation methodologies (Liang et al.,
2022; Srivastava et al., 2023). As these models
are integrated into a wide range of applications,
a rigorous assessment of their capabilities, limi-
tations, and safety is paramount (Achiam et al.,
2023; Wang et al., 2023). Although the initial fo-
cus of evaluation has been predominantly on En-
glish, a model’s global utility is contingent upon its
performance across diverse linguistic and cultural
contexts (Singh et al., 2024c). The evaluation of
non-English LLMs is therefore essential, not only
for ensuring equitable technological access but also
for understanding the extent to which these models
capture the distinct complexities inherent in dif-
ferent languages, an undertaking that goes beyond
mere translation (Bender et al., 2021).
The evaluation landscape for English LLMs is
well-established, featuring a comprehensive suite
of benchmarks targeting a spectrum of model ca-
pabilities. For foundational "base" models, bench-
marks assess commonsense reasoning, such as Hel-
laSwag (Zellers et al., 2019) and Winogrande (Sak-
aguchi et al., 2021), factual accuracy with Truth-
fulQA (Lin et al., 2022), and broad multi-task
knowledge with MMLU (Hendrycks et al., 2020;
Wang et al., 2024; Singh et al., 2024b). Specialized
datasets evaluate capabilities like mathematical rea-
soning on GSM8K(Cobbe et al., 2021) and code
generation with HumanEval (Chen et al., 2021) and
MBPP (Austin et al., 2021). Furthermore, the ad-
vent of interactive, instruction-following models
has spurred the creation of benchmarks to assess
conversational quality on MT-Bench (Zheng et al.,
2023), fidelity to complex instructions with IFEval
(Zhou et al., 2023), and the ability to execute tool
or function calls correctly on BFCL (Patil et al.).
These datasets have collectively become the stan-
dard for evaluating the performance of state-of-the-
art models in English.
In recent years, significant progress has been
made in developing evaluation resources for In-
dic languages, typified by benchmarks such as In-
dicGLUE (Kakwani et al., 2020), MILU (Verma
et al., 2025), IndicMMLU-Pro (Sankalp et al.), and
IndicGenBench (Singh et al., 2024a). These re-
sources have been instrumental in assessing the
core capabilities of pre-trained base models across
numerous languages of the Indian subcontinent
(Joshi et al., 2024). Despite this progress, the exist-
ing benchmarks primarily target pre-trained base
models, leaving a noticeable gap in resources for
assessing the capabilities of instruction-tuned mod-
els. Consequently, benchmarks for critical skills
like instruction following, conversational ability,
and function calling, such as Hindi versions of IFE-
val, MT-Bench, and BFCL, are largely unavailable
publicly.
A common methodology to address this gap in-
volves the direct translation of existing English
benchmarks. This approach, however, presents
considerable challenges, as automated translation
arXiv:2508.19831v2  [cs.CL]  15 Oct 2025

--- Page 2 ---\n\nDataset Name
Count
Method
IFEval-Hi
848
In-house
MT-Bench-Hi
200
Translated and human evaluated (4 categories); In-house (4 categories)
GSM8K-Hi
1319
Translated and human evaluated (100%)
ChatRAG-Hi
5948
Translated, filtered, and human-evaluated (5%). Includes: INSCIT (450), Doc2Dial (498), QuAC, QReCC,
TopiocQA, CoQA, HybriDial, SQA, DoQA (Cooking, Travel, Movies), ConvFinQA (500 each).
Context: GCP translated, no filtering.
Answers and conversation turns:
- Used GCP translated data when the back-translated version matched the original (CHRF++ ≥90).
- Else, used LLM translated data with heuristic filtering to remove poor translations.
BFCL-Hi
2251
Translated (not human evaluated)
Table 1: Overview of the Hindi evaluation datasets. The test suite consists of Hindi versions of IFEval, MT-Bench,
GSM8K, ChatRAG, and BFCL.
frequently fails to preserve the linguistic subtleties
and cultural context integral to the target language.
This process can yield datasets that are linguisti-
cally incongruous or culturally irrelevant, thereby
diminishing the validity and reliability of the evalu-
ation. Such benchmarks often test a model’s ability
to comprehend translated English rather than its
native fluency and instruction fidelity.
To address these deficiencies, this paper intro-
duces Hindi versions of five widely-used and com-
prehensive benchmarks: IFEval-Hi, MT-Bench-Hi,
GSM8K-Hi, ChatRAG-Hi, and BFCL-Hi. We de-
veloped these datasets using a process that com-
bined direct human creation with a translate-and-
verify workflow, ensuring high linguistic and cul-
tural relevance. A summary of the final dataset
sizes and curation methods is presented in Table 1.
Furthermore, we utilize this new suite to conduct a
comprehensive benchmarking of several prominent,
publicly available LLMs based on foundational
models, including Llama, Gemma, and Nemotron.
This work contributes a valuable, high-quality eval-
uation suite for Hindi to the research community
and presents a comparative analysis that offers crit-
ical insights into the current capabilities of Hindi
language models.
The main contributions of our work are as fol-
lows:
• We introduce a suite of five new, high-
quality benchmarks (IFEval-Hi1, MT-Bench-
Hi2, GSM8K-Hi3, ChatRAG-Hi4, and BFCL-
Hi5) for evaluating instruction-tuned LLMs in
Hindi and detail the curation process devel-
oped for their creation.
1https://huggingface.co/datasets/nvidia/IFEval-Hi
2https://huggingface.co/datasets/nvidia/MT-Bench-Hi
3https://huggingface.co/datasets/nvidia/GSM8K-Hi
4https://huggingface.co/datasets/nvidia/ChatRAG-Hi
5https://huggingface.co/datasets/nvidia/BFCL-Hi
• We present a comprehensive benchmark of
prominent, publicly available LLMs on this
new suite, providing the first robust compara-
tive analysis of their capabilities in Hindi. Our
findings show that while specialized models
exhibit strength in specific tasks, Gemma-2-
9b-it in the SLM class and GPT-OSS-120B
in the LLM class emerge as the most capable
general-purpose models.
2
Related Work
Recent years have witnessed notable progress in
the evaluation of multilingual and low-resource lan-
guage models, with a particular focus on Indic lan-
guages. Foundational efforts, such as IndicGLUE
(Kakwani et al., 2020) and IndicXTREME (Dodda-
paneni et al., 2023), established the initial ground-
work by adapting the GLUE paradigm for major
Indic languages. These benchmarks provided a
broad suite of Natural Language Understanding
(NLU) tasks, including classification, entailment,
and named entity recognition, which proved instru-
mental in assessing the foundational capabilities of
models across multiple Indic languages, including
Hindi.
Building upon these foundations, subsequent
benchmarks like MILU (Verma et al., 2025) in-
troduced more challenging and culturally grounded
tasks. MILU, is a large-scale benchmark compris-
ing approximately 80,000 multiple-choice ques-
tions derived from Indian competitive examina-
tions. By emphasizing India-specific domains such
as local governance, arts, and history, MILU under-
scores the importance of cultural context in evalua-
tion, an element often diluted in directly translated
datasets. Specialized datasets like IndicQuest (Ro-
hera et al., 2024) have been developed to evaluate
the factual knowledge of Indic LLMs. In parallel,

--- Page 3 ---\n\nFigure 1: Distribution of samples by Indian cultural
themes in the IFEval-Hi dataset.
Figure 2: Distribution of verifiable instruction types
within the IFEval-Hi dataset.
benchmarks such as IndicSQuAD (Endait et al.,
2025) and IndicQA (Singh et al., 2025) have ad-
dressed extractive and abstractive question answer-
ing.
More recently, the field has shifted toward multi-
task and generative evaluation. Benchmarks like
the IndicGenBench suite (Singh et al., 2024a)
and IndicMMLU-Pro (Sankalp et al.) now assess
complex reasoning, creative understanding, and
instruction-following, demonstrating a move be-
yond traditional NLU paradigms. This trend is fur-
ther reflected in the Okapi (Lai et al., 2023), which
translated key English benchmarks into numerous
languages, and the development of Global MMLU
(Singh et al., 2024b), which extends evaluation to
more diverse cultural contexts.
Figure 3:
Category distribution in MT-Bench-Hi,
adapted with Indian cultural themes to increase focus
on culturally relevant instructions.
3
Dataset Curation
This section describes the process used to curate
the Hindi versions of popular English benchmark
datasets. Sample examples from each dataset are
shown in Figure 4.
3.1
IFEval-Hi
The creation of IFEval-Hi is based on the English
Instruction Following Evaluation (IFEval) bench-
mark, which is designed to rigorously assess an
LLM’s ability to adhere to precise instructions. The
original English IFEval is structured around 25 dis-
tinct and objectively verifiable instruction types,
such as "insert a word at a specific position" or
"reverse the first paragraph". This structure en-
sures a reliable and scalable evaluation process. To
test models with increasing difficulty, the prompts
are organized into three complexity levels: Sin-
gle, Double, and Triple Instructions, requiring the
model to execute one, two, or three distinct com-
mands within the same prompt, respectively.
Our curation process for IFEval-Hi was a sys-
tematic adaptation of this framework to an Indian
cultural and linguistic context. The core of this pro-
cess involved retaining the 22 verifiable instruction
types as a structural framework while replacing
the generic content of the English prompts with
themes relevant to India. Some categories that are
not relevant to Hindi, such as "Change Cases," were
dropped. The thematic content was sourced from
comprehensive categories on Wikipedia related to
India, covering a wide range of topics including
Indian history, philosophy, festivals, art forms, and
social norms. The distribution of cultural themes

--- Page 4 ---\n\nIFEval-Hi
भारतकीशिक्षाप्रणालीकेसुधारकेबारेमेंअपनीरायरखें।आपकापूराउत्तरहिन्दीमेंहोना
चाहिएऔरउसमें"श" अक्षरकमसेकम६बारआनाचाहिए।
MT-Bench-Hi
खुदकोरत्नटाटाकेरूपमेंप्रस्तुतकरेंऔरअगलेसंवादमेंउनकेजैसाबोलनेकीकोशिश
करें।भारतमेंसौरऊर्जामेंनिवेशक्योंकरनाचाहिए, औरक्यायहदेशकेभविष्यकेलिए
महत्वपूर्णहै?
Follow up: भारतमेंसौरऊर्जाकेक्षेत्रमेंनिजीक्षेत्रऔरसरकारकोमिलकरकिसप्रकार
कीनीतियाँअपनानीचाहिए, ताकियहक्षेत्रऔरभीतेजीसेविकसितहोसके?
GSM8K-Hi
एकटोकरीमें25 संतरेहैं, जिनमेंसे1 खराबहै, 20% कच्चेहैं, 2 खट्टेहैंऔरबाकीअच्छे
हैं।कितनेसंतरेअच्छेहैं?
ChatRAG-Hi
Question: जापानीट्रेनशिष्टाचार: क्याशिंकान्सेनग्रीनकारमेंशिशुलेजानास्वीकार्यहै?
Answer: यहस्वीकार्यहै।हालांकि, यहशिष्टाचारहैकियदिबच्चाशोरमचानाशुरूकरदे
तोआपउसेदरवाजेकेबाहर"डेक" क्षेत्रमेंलेजाएं।
Context: हां, यहस्वीकार्यहै।हालांकि, यहशिष्टाचारहैकियदिबच्चाशोरमचानाशुरू
करदेतोआपउसेदरवाजेकेबाहर"डेक" क्षेत्रमेंलेजाएं(जहांबाथरूम, टेलीफोन, वेंडिंग
मशीनआदिहैं)।...
BFCL-Hi
Prompt: इसे20 डिग्रीघुमाएंऔरक्षैतिजरूपसेपलटें
Function Names:
flipImageAction, rotateImageAction, removeBack-
groundAction, getRecommendationsAction, resizeImageAction
Figure 4: Representative examples from five Hindi evaluation datasets curated in this study.
is detailed in Figure 1, while the breakdown across
verifiable instruction categories is presented in Fig-
ure 2.
New prompts were carefully created by a team
of five annotators over a ten-week period. To en-
sure that the newly created Indian-themed prompts
were both culturally relevant and objectively ver-
ifiable, annotators were provided with examples
for each instruction type. For instance, when the
instruction theme is "Geography of India" and the
instruction category is a letter frequency constraint,
such as requiring a certain Hindi letter to appear at
least three times, the annotator crafts an instruction
that incorporates both the theme and the explicit
constraint. Specific sample is shown in Figure 4.
To ensure that IFEval-Hi could be used as a direct
benchmark against its English counterpart, the eval-
uation metrics and constraints for each of the 22
instruction categories were directly mirrored, along
with the three levels of complexity. This significant
human-in-the-loop effort resulted in a final dataset
comprising 848 high-quality, culturally resonant
samples. The annotation process is described in
further detail in Appendix A.2.
3.2
MT-Bench-Hi
MT-Bench-Hi is the Hindi adaptation of the En-
glish Multi-Turn Benchmark (MT-Bench), a stan-
dard for evaluating the conversational and reason-
ing abilities of LLMs in extended dialogues. The
original benchmark consists of 80 high-quality,
multi-turn questions designed to test key capabili-
ties such as maintaining context, response accuracy,
and instruction following. It employs an "LLM-as-
a-Judge" approach, where a powerful model like
GPT-4o scores all responses on a 1-10 scale using
two distinct methods: for reference-free categories
(STEM, Writing, Roleplay, Humanities, Extrac-
tion), responses are scored directly, while for cat-
egories with reference answers (Reasoning, Math,
Coding), they are evaluated via pairwise compari-
son against the reference answer.
The curation of MT-Bench-Hi was a detailed
adaptation process designed to make the bench-
mark culturally and contextually relevant for India.
We adopted a hybrid approach to content creation.
For universal technical categories (STEM, math,
reasoning, coding), questions were translated from
English to Hindi using GCP and subsequently un-
derwent thorough human evaluation to verify ac-
curacy and intent. For categories requiring deep
cultural contextualization (Writing, Roleplay, Hu-
manities, Extraction), questions were created from
scratch by human specialists to ensure the prompts
were authentically Indian. Figure 3 illustrates the fi-
nal distribution of samples across these categories.
To maintain high standards, annotators were pro-
vided with reference examples from the English
MT-Bench and guided through a specialized in-
terface. A key quality assurance step involved
showing annotators sample responses from a high-
performing model (e.g., GPT-4o) to help them craft
prompts that could effectively test advanced capa-
bilities in an Indian context. The evaluation frame-
work was aligned with the original’s "LLM-as-a-
Judge" methodology. To ensure consistency, we
maintain the same format as the original dataset;
for categories that include a reference answer, we

--- Page 5 ---\n\nFigure 5: A sample GSM8K question highlighting a translation mistake in Hindi (red), the corrected version (green),
and the corresponding English line (yellow), showcasing the process of identifying and fixing language conversion
errors manually.
retain the original English reference answer during
evaluation. Aligning with the original MT-Bench
setup, we employ direct, single-answer evaluation
for reference-free, subjective categories (e.g., Writ-
ing, Roleplay) and pairwise comparison against
a reference answer for categories with objective
solutions (e.g., Math, Coding, Reasoning). The
annotation process is described in further detail in
Appendix A.3.
3.3
GSM8K-Hi
The foundation for this dataset is the English
GSM8K (Grade School Math 8K), a prominent
benchmark for assessing the mathematical reason-
ing of LLMs. Directly translating the dataset into
Hindi risks altering the underlying mathematical
logic, particularly in problems with comparative
constructs such as ‘twice that amount’ or ‘10 less
than half the age of’. However, crafting linguis-
tically diverse math problems that require multi-
step solutions demands significant expertise in both
mathematics and language structure.
This pro-
cess involves considerable time and effort from hu-
man annotators with domain expertise, making it a
resource-intensive endeavor. Therefore, to balance
quality with feasibility, we opted for a two-step
"translate-then-verify" methodology.
The process began with machine translation of
the original English problems (including GSM8K
system prompt) into Hindi using GCP. Human an-
notators were then provided with both the Hindi
translation and the original English text for refer-
ence. Their primary task was to evaluate the Hindi
translation for correctness and suggest modifica-
tions to ensure linguistic accuracy and contextual
appropriateness. This verification stage proved to
be essential, as annotators flagged approximately
10% of the machine-translated data for inaccura-
cies. These instances were subsequently reviewed
and corrected through close collaboration between
our development team and the annotators, ensur-
ing the final dataset maintained high quality. To
illustrate this process, Figure 5 shows a sample er-
ror alongside its correction. To ensure consistent
benchmarking, GSM8K-Hi is evaluated using the
LM-Eval-Harness, the same framework employed
for the original English dataset. The annotation
process is described in further detail in Appendix
A.4.
3.4
ChatRAG-Hi
ChatRAG-Hi is the Hindi version of ChatRAG
Bench, a benchmark for evaluating conversational
question-answering using documents and retrieved
context.
The original incorporates ten diverse
datasets, including Doc2Dial, QuAC, and Con-
vFinQA. Adapting this composite dataset posed
challenges due to the varied structures of its subsets,
which range from extensive contexts to single-word
answers.
Our curation process involved a differential trans-
lation strategy. The extensive context passages
were translated using GCP without subsequent fil-
tering. For the more sensitive answers and conver-
sation turns, we adopted a two-tiered approach. We
first used GCP and validated the output by back-

--- Page 6 ---\n\nModel
Size
MT-Bench-Hi
BFCL-Hi
GSM8K-Hi
IFEval-Hi
ChatRAG-Hi
SLMs
Gemma-2-2b-it
2B
4.37
32.96
26.99
38.92
29.89
Llama-3.2-3B-Instruct
3B
5.14
33.81
40.11
40.80
32.60
Nemotron-Mini-4B-Instruct
4B
3.44
-
32.22
36.08
27.32
Nemotron-4-Mini-Hindi-4B-Instruct
4B
6.01
52.82
47.31
51.65
36.07
Llama-3.1-8B-Instruct
8B
6.44
31.23
61.33
48.82
38.03
Aya-expanse-8b
8B
6.58
36.56
64.52
42.92
30.15
Gemma-2-9b-it
9B
7.37
50.51
64.44
61.79
40.97
Krutrim-2-instruct
12B
6.31
26.88
56.56
59.32
37.48
LLMs
GPT-OSS-20B (reasoning low)
21B
8.51
54.60
80.64
69.04
26.16
Mistral-Small-3.2-24B-Instruct-2506
24B
7.83
41.45
77.55
66.89
37.92
Sarvam-M (reasoning off)
24B
8.25
48.60
82.30
71.64
40.14
Gemma-3-27b-it
27B
8.31
62.42
78.12
67.72
45.23
GPT-OSS-120B (reasoning low)
117B
8.70
61.26
93.41
73.86
29.85
Qwen3-235B-A22B-FP8 (reasoning off)
235B
8.10
59.88
89.69
68.11
32.47
Llama-3.1-405B
405B
7.17
49.53
86.27
68.66
47.46
LLMs (Reasoning)
GPT-OSS-20B (reasoning medium)
21B
8.43
63.26
83.41
72.01
29.16
GPT-OSS-20B (reasoning high)
21B
8.23
64.77
83.44
72.11
32.39
Sarvam-M (reasoning on)
24B
8.60
59.53
84.40
74.06
37.13
GPT-OSS-120B (reasoning medium)
117B
8.79
66.19
95.93
76.69
30.80
GPT-OSS-120B (reasoning high)
117B
8.70
64.90
96.27
76.80
31.82
Table 2: Performance of various LLMs on Hindi benchmarks. MT-Bench-Hi is scored on a scale of 1-10 using
an LLM-as-a-judge approach. BFCL-Hi, GSM8K-Hi, and IFEval-Hi report accuracy on a 1-100 scale, while
ChatRAG-Hi reports the F1-Score. The highest score in each column is highlighted in bold.
translating it to English. If the back-translated
text matched the original with a high degree of
fidelity (CHRF++ score >= 90), the GCP transla-
tion was retained. In cases where the CHRF++
score was low, which often occurred with very
short text segments (1–3 words) where GCP lacks
sufficient contextual cues, the GCP translation was
discarded. To overcome this, we employed an LLM
for these segments, providing it with the broader
GCP-translated Hindi context alongside the origi-
nal short English answer to generate a more accu-
rate and contextually appropriate Hindi equivalent.
This LLM-generated (Llama-3.1-405B) data was
then subjected to heuristic filtering to remove poor-
quality outputs. This hybrid methodology was de-
signed to maximize accuracy across different text
types. To ensure overall quality, approximately
10% of the final Hindi data underwent human ver-
ification, which confirmed the high fidelity of the
translations, with the error rate across subsets re-
maining within 1-5%.
3.5
BFCL-Hi
BFCL-Hi is the Hindi adaptation of the Berke-
ley Function-Calling Leaderboard (BFCL V2), a
benchmark designed to evaluate the ability of
LLMs to call functions or tools.
The original
dataset comprises diverse function-calling scenar-
ios, including simple, multiple, and parallel calls. It
also includes relevance and irrelevance categories
to assess a model’s ability to determine if the pro-
vided tools are appropriate for a given query.
The dataset is structured in a JSON format where
each entry contains a conversation history and an
array of available functions, defined with names,
descriptions, and parameter schemas. To create
BFCL-Hi, we translated the conversational history
into Hindi using the GCP translation service. Cru-
cially, the function calls themselves, including their
names, descriptions, and parameter details, were re-
tained in their original English format. This hybrid
approach tests the model’s ability to understand a
Hindi query and map it to a predefined English-
language tool. However, to make the dataset more
relevant for fully localized use cases, the function
parameters should also be translated into Hindi,
which we leave as a task for future work. The
ground truth for simple, multiple, and parallel cate-
gories remained unchanged from the English ver-
sion. The relevance and irrelevance categories do
not include ground truth, as they are designed to
verify whether the model correctly attempts a func-
tion call. Evaluation is performed using the BFCL
Abstract Syntax Tree (AST) methodology to ensure
a thorough and accurate analysis.

--- Page 7 ---\n\n4
Results and Discussion
This section presents and analyzes the performance
of a diverse set of publicly available, instruction-
tuned Small Language Models (SLMs) and Large
Language Models (LLMs) on our newly developed
Hindi benchmark suite, with detailed results pre-
sented in Table 2. The models evaluated include
representatives from prominent families such as
Google’s Gemma, Meta’s Llama, OpenAI’s GPT-
OSS, NVIDIA’s Nemotron, Qwen, and Sarvam,
alongside other notable multilingual models.
Among the SLMs, the results reveal a competi-
tive landscape. Gemma-2-9b-it provides the best
all-around performance, securing the highest scores
on MT-Bench-Hi, IFEval-Hi, and ChatRAG-Hi.
Aya-expanse-8b secures the best score on GSM8K-
Hi. The value of targeted, language-specific train-
ing is highlighted by Nemotron-4-Mini-Hindi-4B-
Instruct, which leads significantly on BFCL-Hi.
In the LLM category (models with > 20B pa-
rameters), GPT-OSS-120B demonstrates standout
performance by achieving the best scores on MT-
Bench-Hi, GSM8K-Hi, and IFEval-Hi.
Other
models show specialized strengths: Gemma-3-
27b-it achieves the highest score on BFCL-Hi,
while the largest model, Llama-3.1-405B, excels
on ChatRAG-Hi. However, it is worth noting that
GPT-OSS may have an inherent advantage due to
its reasoning mode, even though we set it to a low
level for a fairer comparison, and the potential for
the GPT-4o judge to be biased towards a sibling
OpenAI model also warrants further investigation.
Furthermore, activating the dedicated reasoning
modes in models like GPT-OSS and Sarvam-M pro-
vides a substantial performance uplift on complex
tasks like BFCL, GSM8K, and IFEval. With these
capabilities enabled, GPT-OSS-120B achieves the
top scores across multiple benchmarks, highlight-
ing the value of reasoning models for Hindi.
In summary, while specialized models show
strength in specific tasks, Gemma-2-9b-it in the
SLM class and GPT-OSS-120B in the LLM class
emerge as the most capable general-purpose mod-
els. The distribution of top scores across different
models highlights that no single model is best for
all tasks. This analysis also indicates that model
size is not the sole determinant of performance, a
point reinforced by both the 8B Aya model out-
performing larger SLMs on GSM8K-Hi and the
competitive results of Sarvam-M, which was post-
trained on Indic languages. These findings suggest
that architectural choices and targeted training data
are crucial for developing specialized capabilities
for the Hindi language.
5
Conclusion
In this work, we addressed the critical gap in evalu-
ation resources for instruction-tuned Hindi LLMs
by introducing a new suite of five culturally and lin-
guistically robust benchmarks. Our hybrid curation
methodology, combining careful human-centric
creation with a translate-and-verify process, pro-
vides a valuable framework for developing similar
resources in other languages. Our evaluation of var-
ious public LLMs supporting the Hindi language
revealed a competitive landscape where different
models exhibit specialized strengths in reasoning,
conversation, and function calling. This suite en-
ables a more nuanced assessment of Hindi LLMs,
supporting the broader goal of fostering more equi-
table and capable multilingual AI systems.
Limitations
We acknowledge certain limitations in our work.
While our benchmark suite is comprehensive, it
does not encompass every possible instruction type
or conversational scenario. The use of an "LLM-
as-a-Judge" for MT-Bench-Hi carries inherent bi-
ases, particularly as the judge model’s proficiency
in evaluating nuanced Hindi content is not guar-
anteed. Furthermore, datasets developed through
translation, despite human verification, could be
improved with full human curation to better cap-
ture cultural and linguistic subtleties. Future work
could expand the scope of these benchmarks and
explore alternative evaluation methodologies.
Acknowledgements
This work would not have been possible without
contributions from many people at NVIDIA. To
mention a few: Priyanka Chavan, Shweta Dash,
Asmita Kadwe, Nilesh Chauhan, Saloni Pipada,
Shrutika Marke, Priyanka Patil, Ninad Nemade,
Muskan Grewal, Aditya Patil, and Noopur Mishra.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.

--- Page 8 ---\n\nJacob Austin, Augustus Odena, Maxwell Nye, Maarten
Bosma, Henryk Michalewski, David Dohan, Ellen
Jiang, Carrie Cai, Michael Terry, Quoc Le, et al. 2021.
Program synthesis with large language models. arXiv
preprint arXiv:2108.07732.
Emily M Bender, Timnit Gebru, Angelina McMillan-
Major, and Shmargaret Shmitchell. 2021. On the
dangers of stochastic parrots: Can language models
be too big? In Proceedings of the 2021 ACM confer-
ence on fairness, accountability, and transparency,
pages 610–623.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan, Henrique Ponde De Oliveira Pinto, Jared Ka-
plan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, et al. 2021.
Evaluating large
language models trained on code. arXiv preprint
arXiv:2107.03374.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, et al. 2021. Training verifiers to solve math
word problems. arXiv preprint arXiv:2110.14168.
Sumanth Doddapaneni, Rahul Aralikatte, Gowtham
Ramesh, Shreya Goyal, Mitesh M Khapra, Anoop
Kunchukuttan, and Pratyush Kumar. 2023. Towards
leaving no indic language behind: Building mono-
lingual corpora, benchmark and models for indic
languages. In Proceedings of the 61st Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 12402–12426.
Sharvi Endait, Ruturaj Ghatage, Aditya Kulkarni,
Rajlaxmi Patil, and Raviraj Joshi. 2025.
Indic-
squad: A comprehensive multilingual question an-
swering dataset for indic languages. arXiv preprint
arXiv:2505.03688.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Raviraj Joshi, Kanishk Singla, Anusha Kamath, Rau-
nak Kalani, Rakesh Paul, Utkarsh Vaidya, San-
jay Singh Chauhan, Niranjan Wartikar, and Eileen
Long. 2024.
Adapting multilingual llms to low-
resource languages using continued pre-training and
synthetic corpus. arXiv preprint arXiv:2410.14815.
Divyanshu Kakwani, Anoop Kunchukuttan, Satish
Golla, Gokul NC, Avik Bhattacharyya, Mitesh M
Khapra, and Pratyush Kumar. 2020. Indicnlpsuite:
Monolingual corpora, evaluation benchmarks and
pre-trained multilingual language models for indian
languages. In Findings of the association for compu-
tational linguistics: EMNLP 2020, pages 4948–4961.
Viet Lai, Chien Nguyen, Nghia Ngo, Thuat Nguyen,
Franck Dernoncourt, Ryan Rossi, and Thien Nguyen.
2023. Okapi: Instruction-tuned large language mod-
els in multiple languages with reinforcement learning
from human feedback. In Proceedings of the 2023
Conference on Empirical Methods in Natural Lan-
guage Processing: System Demonstrations, pages
318–327.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Ku-
mar, et al. 2022. Holistic evaluation of language
models. arXiv preprint arXiv:2211.09110.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
Truthfulqa: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252.
Shishir G Patil, Huanzhi Mao, Fanjia Yan, Charlie
Cheng-Jie Ji, Vishnu Suresh, Ion Stoica, and Joseph E
Gonzalez. The berkeley function calling leaderboard
(bfcl): From tool use to agentic evaluation of large
language models. In Forty-second International Con-
ference on Machine Learning.
Pritika Rohera, Chaitrali Ginimav, Akanksha Salunke,
Gayatri Sawant, and Raviraj Joshi. 2024. L3cube-
indicquest: A benchmark question answering dataset
for evaluating knowledge of llms in indic context.
In Proceedings of the 38th Pacific Asia Conference
on Language, Information and Computation, pages
982–988.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavat-
ula, and Yejin Choi. 2021. Winogrande: An adver-
sarial winograd schema challenge at scale. Commu-
nications of the ACM, 64(9):99–106.
KJ Sankalp, Ashutosh Kumar, Laxmaan Balaji, Nikunj
Kotecha, Vinija Jain, Aman Chadha, and Sreyoshi
Bhaduri. Indicmmlu-pro: Benchmarking indic large
language models on multi-task language understand-
ing.
Abhishek Kumar Singh, Vishwajeet Kumar, Rudra
Murthy, Jaydeep Sen, Ashish Mittal, and Ganesh Ra-
makrishnan. 2025. Indic qa benchmark: A multilin-
gual benchmark to evaluate question answering capa-
bility of llms for indic languages. In Findings of the
Association for Computational Linguistics: NAACL
2025, pages 2607–2626.
Harman Singh, Nitish Gupta, Shikhar Bharadwaj, Di-
nesh Tewari, and Partha Talukdar. 2024a. Indicgen-
bench: A multilingual benchmark to evaluate gen-
eration capabilities of llms on indic languages. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 11047–11073.
Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David I Adelani, Jian Gang Ngui, Daniel Vila-
Suero, Peerat Limkonchotiwat, Kelly Marchisio,
Wei Qi Leong, Yosephine Susanto, et al. 2024b.
Global mmlu: Understanding and addressing cul-
tural and linguistic biases in multilingual evaluation.
arXiv preprint arXiv:2412.03304.

--- Page 9 ---\n\nShivalika Singh, Freddie Vargus, Daniel Dsouza,
Börje F Karlsson, Abinaya Mahendiran, Wei-Yin
Ko, Herumb Shandilya, Jay Patel, Deividas Mataciu-
nas, Laura OMahony, et al. 2024c. Aya dataset: An
open-access collection for multilingual instruction
tuning. arXiv preprint arXiv:2402.06619.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Shoeb, Abubakar Abid, Adam Fisch,
Adam R Brown, Adam Santoro, Aditya Gupta, Adri
Garriga-Alonso, et al. 2023. Beyond the imitation
game: Quantifying and extrapolating the capabili-
ties of language models. Transactions on machine
learning research.
Sshubam Verma, Mohammed Safi Ur Rahman Khan,
Vishwajeet Kumar, Rudra Murthy, and Jaydeep Sen.
2025. Milu: A multi-task indic language understand-
ing benchmark. In Proceedings of the 2025 Confer-
ence of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers),
pages 10076–10132.
Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie,
Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi
Xiong, Ritik Dutta, Rylan Schaeffer, et al. 2023. De-
codingtrust: A comprehensive assessment of trust-
worthiness in gpt models. In NeurIPS.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni,
Abhranil Chandra, Shiguang Guo, Weiming Ren,
Aaran Arulraj, Xuan He, Ziyan Jiang, et al. 2024.
Mmlu-pro: A more robust and challenging multi-task
language understanding benchmark. Advances in
Neural Information Processing Systems, 37:95266–
95290.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can a
machine really finish your sentence? In Proceedings
of the 57th Annual Meeting of the Association for
Computational Linguistics, pages 4791–4800.
Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan
Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin,
Zhuohan Li, Dacheng Li, Eric Xing, et al. 2023.
Judging llm-as-a-judge with mt-bench and chatbot
arena. Advances in Neural Information Processing
Systems, 36:46595–46623.
Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Sid-
dhartha Brahma, Sujoy Basu, Yi Luan, Denny Zhou,
and Le Hou. 2023.
Instruction-following evalu-
ation for large language models.
arXiv preprint
arXiv:2311.07911.
A
Appendix
A.1
Annotator Team and Process
The human-centric curation and verification tasks
were conducted by a team of five specialists. These
individuals were employees of our organization,
compensated fairly for their work, and were se-
lected for their proficiency in Hindi as either a first
or second language. Representing various regions
across India, they possessed strong reading and
writing skills and a solid understanding of cultural
nuances.
The primary tool used for annotation was Su-
perAnnotate, which provided an intuitive interface
for our workflow. This platform allowed for the
efficient sharing of examples, processing of results
using Python scripts, and performance of quality
assurance (QA). The data underwent periodic QA
and development checks to ensure alignment with
project requirements. To maintain high levels of
creativity and productivity, the specialists worked
in focused sessions of 2–3 hours per day.
A.2
IFEval-Hi Curation Process
The annotation procedure for IFEval-Hi was highly
structured and communicated to annotators through
a comprehensive guidelines document. The process
was organized into sequential stages of increasing
complexity, beginning with cases that contained
a single verifiable instruction, followed by stages
with two and then three instructions. Each test case
was assigned a predefined Indian theme and instruc-
tion category to ensure a balanced distribution of
scenarios.
The annotation workflow for each case involved
several key components:
• Reference Sample: Annotators were provided
with a developer-generated sample in Hindi
that incorporated the verifiable instruction,
serving as a clear reference for the task re-
quirements.
• Annotation Interface: A dedicated text box
was provided for annotators to formulate their
questions based on the assigned theme and in-
struction category, with a separate comments
box for any necessary clarifications with the
quality control developer.
• Evaluation Parameters: The parameters re-
quired for automatic evaluation were also sys-
tematically recorded, aligning with the stan-
dards of the English dataset. Annotators re-
ceived detailed guidelines for these parame-
ters, with the Hindi reference sample serving
as a practical model.
• Review and Feedback Loop: A weekly review
of approximately 50% of submitted samples

--- Page 10 ---\n\nFigure 6: Illustration of the annotation interface used to curate the IFEval dataset, displaying the guidelines and
example instructions provided to annotators.
was conducted by developers. Any cases re-
quiring revision were returned to annotators
with specific feedback in the comments sec-
tion, ensuring a consistent feedback loop and
high-quality output.
Sample annotation UI screens are shown in Figures
6 and 7. Some examples from the dataset are shown
in Figure 8.
A.3
MT-Bench-Hi Curation Process
The curation of the MT-Bench-Hi dataset, while
presenting distinct challenges, benefited from the
procedural learnings established during the IFEval-
Hi creation. Specialists were guided by supplemen-
tary instructions tailored to the specific demands
of creating multi-turn conversational benchmarks.
This process was designed to help annotators under-
stand the evaluation procedure and produce high-
quality, contextually relevant samples.
The workflow for each test case provided anno-
tators with a comprehensive view of the task:
• Original English Sample: Annotators were
given an original question and follow-up from
the MT-Bench dataset as a reference.
• Model Response Example: The correspond-
ing model-generated response for the English
sample was included.
• Evaluation Insight: The AI judge’s rating and
judgment for that response were also provided,

--- Page 11 ---\n\nFigure 7: Example entry from the Hindi IFEval, curated at three levels of complexity: Single Instruction, Double
Instruction, and Triple Instruction.
IFEval-Hi
भारतकीशिक्षाप्रणालीकेसुधारकेबारेमेंअपनीरायरखें।आपकापूराउत्तरहिन्दीमेंहोनाचाहिएऔरउसमें
"श" अक्षरकमसेकम६बारआनाचाहिए।
भारतकेप्रसिद्धनृत्योंपरदोलेखलिखेंऔरदोनोंलेखोंको****** सेअलगकरें।
भारतकेप्रमुखवन्यजीवअभयारण्यों, राष्ट्रीयउद्यानोंतथासंरक्षणमेंउनकीभूमिकाकेबारेमेंबताइए।ध्यान
रखेंकिआपइसमेंअल्पविरामकाप्रयोगनकरेंऔरप्रजातिएवंसंरक्षणजैसेशब्दोंकोशामिलकरनानभूलें।
भारतमेंअंग्रेज़ोंनेकितनेवर्षोंतकराजकिया, इसपरएकबड़ालेखलिखें।इसलेखकाशीर्षकदोहरेकोणीय
कोष्ठकमेंहोनाचाहिए, जैसे<<ब्रिटिशराज>>।
केंद्रीयप्रदूषणनियंत्रणबोर्डकागठनकबहुआथाऔरइसकेकार्यक्याहैं, इसविषयपर२०सेज़्यादावाक्यों
औरन्यूनतम२००शब्दोंमेंएकलेखलिखें।आपकेलेखकाशीर्षकदोहरेकोणीयकोष्ठकमेंहोनाचाहिए, जैसे
<<प्रदूषणनियंत्रण>>।
Figure 8: Examples from the IFEval-Hi benchmark.
offering annotators direct insight into the eval-
uation criteria and performance expectations.
Using this framework, annotators reviewed the ini-
tial English question and its follow-up, then crafted
analogous questions contextualized for Indian set-
tings. To ensure quality and adherence to guide-
lines, 50% of the newly created samples were sub-
ject to a weekly review by a developer. This struc-
tured approach equipped annotators to produce
high-quality, contextually appropriate samples for
the MT-Bench-Hi dataset. The sample annotation
UI screen is shown in Figure 9. Some examples
from the dataset are shown in Figure 10.
A.4
GSM8K-Hi Curation Process
By the GSM8K annotation stage, annotators were
proficient with the annotation interface. The math-
ematical nature of this dataset required sustained
attention to detail during the verification process.
The workflow for each sample test case included
the following elements:
• Translated Content: Annotators received the
translated Hindi version of the instruction and
the corresponding translated output.
• Final Answer: The final numerical answer
was clearly indicated for verification.
Annotators were instructed to carefully read and
comprehend the question to assess its clarity and

--- Page 12 ---\n\ncoherence, using the provided solution for addi-
tional context if necessary. They were tasked with
flagging any ambiguous or unclear questions for
review. On the quality control interface, develop-
ers reviewed the annotated samples, referencing
the original English versions to guide any neces-
sary corrections. The sample annotation UI screen
is shown in Figure 11. Some examples from the
dataset are shown in Figure 12.
A.5
ChatRAG-Hi and BFCL-Hi Curation
Process
The ChatRAG-Hi and BFCL-Hi datasets were cu-
rated through GCP translation and subsequent fil-
tering. Examples are provided in Figures 14 and
13, respectively.

--- Page 13 ---\n\nFigure 9: Illustration of the annotation interface used to curate the culturally adapted Indic version of the MT-Bench
dataset, displaying the guidelines and example instructions provided to annotators.

--- Page 14 ---\n\nMT-Bench-Hi
खुदकोरत्नटाटाकेरूपमेंप्रस्तुतकरेंऔरअगलेसंवादमेंउनकेजैसाबोलनेकीकोशिशकरें।भारतमेंसौर
ऊर्जामेंनिवेशक्योंकरनाचाहिए, औरक्यायहदेशकेभविष्यकेलिएमहत्वपूर्णहै?
Follow up: भारतमेंसौरऊर्जाकेक्षेत्रमेंनिजीक्षेत्रऔरसरकारकोमिलकरकिसप्रकारकीनीतियाँअपनानी
चाहिए, ताकियहक्षेत्रऔरभीतेजीसेविकसितहोसके?
अबआपएकभूगोलविशेषज्ञहैं।आपकाकार्यहैजटिलभौगोलिकअवधारणाओंकोसरलतरीकेसेसमझाना
ताकिआमलोगभीइसेसमझसकें।आइएशुरुआतकरतेहैंइससवालसे: भारतीयउपमहाद्वीपकाविस्तार
क्याहै? इसमेंकौन-कौनसीप्रमुखभौगोलिकविशेषताएँशामिलहैं?
Follow up: क्यायहसहीहै? मैंनेसुनाहैकिकुछविशेषज्ञइसे'हिमालयनबेल्ट' सेजोड़तेहैं, क्याइसका
कुछमतलबहै?
यदिभारतकेइतिहासकेकिसीमहत्वपूर्णचरण, जैसे१८५७कास्वतंत्रतासंग्रामकोड्रामा, माइमयाथिएटर
तकनीकोंकाउपयोगकरकेकक्षामेंप्रस्तुतकियाजाए, तोछात्रोंकोघटनाओंकीगहराईसमझनेमेंकैसेमदद
मिलेगी? उदाहरणकेलिएक्यासैनिकोंकेविद्रोहयाझांसीकीरानीकेसंघर्षकोमंचपरदर्शानाउनकीप्रेरणाओं
औरसामाजिकसंदर्भोंकोजीवंतरूपसेसमझासकताहै? ऐसेमेंक्यायहशिक्षणविधिछात्रोंकोभारतीय
स्वतंत्रतासंग्रामकेविभिन्नदृष्टिकोणोंकोअधिकप्रभावीढंगसेसमझनेमेंमददकरेगी?
Follow up: यदिझांसीकीरानीकेसंघर्षया१८५७केस्वतंत्रतासंग्रामकोथिएटरयामाइमकेमाध्यम
सेप्रस्तुतकियाजाताहै, तोक्याइसतरहकीप्रस्तुतिकेवलप्रमुखनायकोंपरकेंद्रितरहेगी, याइसमेंआम
नागरिकों, सैनिकोंऔरब्रिटिशअधिकारियोंकेदृष्टिकोणकोभीशामिलकियाजासकताहै? क्याइससेछात्रों
कोइतिहासकीघटनाओंकेविभिन्नसामाजिकऔरसांस्कृतिकप्रभावोंकोअधिकगहराईसेसमझनेकाअवसर
मिलेगा, औरयदिहाँ, तोकिसप्रकार?
भारतकेकिसीमहत्वपूर्णऐतिहासिकआंदोलन(जैसेस्वतंत्रतासंग्राम) कावर्णनकरतेहुएपाँचप्रमुखसिद्धांत
बताइए, जोकिसीऐतिहासिकघटनाकाविश्लेषणकरतेसमयध्यानमेंरखेजातेहैं।
Follow up: बताएगएसिद्धांतोंकाउपयोगकरतेहुएइसऐतिहासिकआंदोलनकीसफलतायाविफलता
कामूल्यांकनकरनेकेलिएकिनविशेषप्रमाणोंकीआवश्यकताहोगी? यहभीसमझाइएकियेप्रमाणइस
आंदोलनकोमजबूतयाकमजोरकैसेबनातेहैं।
क्याआपएकआकर्षककथालिखसकतेहैंजोइसवाक्यसेशुरूहो: मुंबईकेएकपुरानेमोहल्लेकीअटारी
मेंरखीएकपुरानीघड़ीसालोंसेचलनाबंदकरचुकीहै।
Follow up: अबवहीकार्यदोबाराकरेंलेकिनकेवलछहशब्दोंवालेवाक्योंकाउपयोगकरें।
Figure 10: Examples from the MT-Bench-Hi benchmark.

--- Page 15 ---\n\nFigure 11: Illustration of the annotation interface used to evaluate the translation quality of the GSM8K dataset,
displaying the guidelines and example instructions provided to annotators.

--- Page 16 ---\n\nGSM8K-Hi
एकटोकरीमें25 संतरेहैं, जिनमेंसे1 खराबहै, 20% कच्चेहैं, 2 खट्टेहैंऔरबाकीअच्छेहैं।कितनेसंतरे
अच्छेहैं?
6 लोगोंकेएकपरिवार(2 वयस्कऔर4 बच्चे) कोएकतरबूजइसतरहसेबांटनाहैकिप्रत्येकवयस्कको
प्रत्येकबच्चेकेतरबूजकेटुकड़ेसेदोगुनाबड़ाटुकड़ामिले।प्रत्येकवयस्ककोतरबूजकाकितनाप्रतिशतहिस्सा
मिलेगा?
जॉर्डनअपनीमाँकोघरपरबनेजन्मदिनकेकेकसेसरप्राइजदेनाचाहतीथी।निर्देशोंकोपढ़करउसेपता
चलाकिकेककाघोलबनानेमें20 मिनटऔरकेककोबेककरनेमें30 मिनटलगेंगे।केककोठंडाहोनेमें2
घंटेऔरकेककोफ्रॉस्टकरनेमेंअतिरिक्त10 मिनटलगेंगे।अगरवहउसीदिनकेकबनानेकीयोजनाबना
रहीहै, तोउसेदेरसेदेरकिससमयकेकबनानाशुरूकरनाहोगाताकिवहशाम5:00 बजेपरोसनेकेलिए
तैयारहो?
लिसाऔरपीटरघर-घरजाकरचॉकलेटबारबेचरहेहैं।लिसानेसाढ़ेतीनडिब्बेचॉकलेटबारबेचे, औरपीटर
नेसाढ़ेचारडिब्बेबेचे।उन्होंनेमिलकर64 चॉकलेटबारबेचे।एकडिब्बेमेंकितनेचॉकलेटबारहैं?
डैनने3 गुलाबकीझाड़ियाँलगाईं।प्रत्येकगुलाबकीझाड़ीमें25 गुलाबहैं।प्रत्येकगुलाबमें8 कांटेहैं।कुल
कितनेकांटेहैं?
Figure 12: Examples from the GSM8K-Hi benchmark.
BFCL-Hi
Prompt
यदिमेरेपास100$ हैंऔरमैंने40$ दानकरदिएहैंतोअबमेरेपासकितनेडॉलरहैं?
Function Names
multiply, add, sub
Prompt
इसे20 डिग्रीघुमाएंऔरक्षैतिजरूपसेपलटें
Function Names
flipImageAction, rotateImageAction, removeBackgroundAction, ge-
tRecommendationsAction, resizeImageAction
Prompt
क्याआपजांचसकतेहैंकिसफेदiPhone 12 अभीभीउपलब्धहैयानहीं?
Function Names
inventory_management,
product_search,
order_status_check,
get_product_details
Prompt
बीजिंगमेंइससमयमौसमकीक्यास्थितिहै? शंघाईमेंभीमौसमकीक्यास्थितिहै?
Function Names
get_current_weather
Prompt
मैंमैकडोनाल्डजाकरपिज़्ज़ाखरीदनाचाहताहूँ।
Function Names
uber.ride
Figure 13: Examples from the BFCL-Hi dataset.

--- Page 17 ---\n\nChatRAG-Hi
Question
जापानीट्रेनशिष्टाचार: क्याशिंकान्सेनग्रीनकारमेंशिशुलेजानास्वीकार्यहै?
Answer
यहस्वीकार्यहै।हालांकि, यहशिष्टाचारहैकियदिबच्चाशोरमचानाशुरूकरदेतोआपउसे
दरवाजेकेबाहर"डेक" क्षेत्रमेंलेजाएं।
Context
हां, यहस्वीकार्यहै।हालांकि, यहशिष्टाचारहैकियदिबच्चाशोरमचानाशुरूकरदेतोआपउसे
दरवाजेकेबाहर"डेक" क्षेत्रमेंलेजाएं(जहांबाथरूम, टेलीफोन, वेंडिंगमशीनआदिहैं)।यदि
आपकोटेलीफोनकॉलकरनायाप्राप्तकरनाहै, अपनेसीटमेटकेसाथऊंचीआवाजमेंबात
करनाहै, याऐसाकुछभीकरनाहैजिससेअन्ययात्रियोंकोपरेशानीहोसकतीहै, तोयहवही
प्रोटोकॉलहै।...
Question
क्याजर्मनीमेंदुकानें२जनवरीकोखुलतीहैं?
Answer
क्षमाकरें, मैंसंदर्भकेआधारपरउत्तरनहींढूँढपारहाहूँ।
Context
2 जनवरीकोजर्मनीमेंसार्वजनिकअवकाशनहींहोताहै।चूंकियहशनिवारहै, इसलिएज़्यादातर
दुकानेंशनिवारकेखुलनेकेसमयकेअनुसारखुलीहोनीचाहिए।कुछस्थानीयदुकानोंकेलिए,
इसकामतलबयहहोसकताहैकिवेअपेक्षाकृतजल्दीबंदहोजातीहैं।ऐसाकहनेकेबाद, कुछ
दुकानेंवैसेभी"छुट्टियोंकेलिए" बंदहोसकतीहैं।...
Question
वेटिकनसिटीकीयात्राकरनेकेलिएक्यामुझेकैथोलिकहोनाआवश्यकहै?
Answer
वेटिकनसिटीनिश्चितरूपसेपर्यटकोंकेलिएखुलाहै।
Context
वेटिकनसिटीनिश्चितरूपसेपर्यटकोंकेलिएखुलाहै; जैसाकिआपशायदजानतेहैं, रोमऔर
वेटिकनसिटीकेबीचकोईवास्तविकसीमानहींहै, जिसकाअर्थहैकिकोईभीउनलोगोंके
कागजातकीजाँचनहींकरताहैजोएकसेदूसरेशहरमेंजातेहैं।...
Question
धन्यवाद।मैंइसेध्यानमेंरखूँगा।क्याऔरकुछहैजोमुझेजाननाचाहिए?
Answer
रोमऔरवेटिकनसिटीकेबीचकोईवास्तविकसीमानहींहै।
Context
वेटिकनसिटीनिश्चितरूपसेपर्यटकोंकेलिएखुलाहै; जैसाकिआपशायदजानतेहैं, रोमऔर
वेटिकनसिटीकेबीचकोईवास्तविकसीमानहींहै, जिसकाअर्थहैकिकोईभीउनलोगोंके
कागजातकीजाँचनहींकरताहैजोएकसेदूसरेशहरमेंजातेहैं।...
Question
क्याआपकोपताहैकिइरकुत्स्कमेंवीज़ाप्राप्तकरनाआसानहैयाअलमाटीमें?
Answer
अल्माटीमेंएकमंगोलियाईदूतावासहै, लेकिनयहशहरसेकाफीदूरहै, औरवहाँपहुँचना
परेशानीभराहै।
Context
अंतमें, मैंनेइरकुत्स्ककोचुना।मेरातर्क: अल्माटीमेंएकमंगोलियाईदूतावासहै, लेकिनयह
शहरसेकाफीदूरहै, औरवहाँपहुँचनापरेशानीभराहै।इसकेअलावा, कज़ाखपुलिसमुझे
थोड़ीचिंतितकरतीहै, औरजबवेआसपासहोतेहैंतोपासपोर्टकेबिनारहनातनावपूर्णहोता
है।इरकुत्स्कमें, आप1-4 कार्यदिवसोंकीप्रक्रियाकेलिएभुगतानकरसकतेहैं, औरयहशहर
केकेंद्रमेंहै।...
Figure 14: Examples from ChatRAG-Hi dataset. Each example contains a user question, a single answer, and partial
supporting context for illustration.
\n```\n