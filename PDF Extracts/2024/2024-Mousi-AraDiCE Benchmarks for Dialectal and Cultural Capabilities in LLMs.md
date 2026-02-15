---
title: "2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs - PDF Extract"
source_pdf: "2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs.pdf"
pages: 33
extracted_at: "2026-02-15T17:51:56.974881"
---

# PDF Extract: 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs

**Source PDF:** 2024-Mousi-AraDiCE Benchmarks for Dialectal and Cultural Capabilities in LLMs.pdf
**Total Pages:** 33

---

## Content

```
--- Page 1 ---

ARADICE: Benchmarks for Dialectal and Cultural Capabilities in LLMs
Basel Mousi, Nadir Durrani, Fatema Ahmad, Md. Arid Hasan,† Maram Hasanain,
Tameem Kabbani,∗Fahim Dalvi, Shammur Absar Chowdhury, Firoj Alam
Qatar Computing Research Institute, Qatar,
†University of New Brunswick, Canada
∗American University of Sharjah, UAE
{bmousi, ndurrani, fialam}@hbku.edu.qa
Abstract
Arabic, with its rich diversity of dialects, re-
mains significantly underrepresented in Large
Language Models, particularly in dialectal vari-
ations. We address this gap by introducing
seven synthetic datasets in dialects alongside
Modern Standard Arabic (MSA), created us-
ing Machine Translation (MT) combined with
human post-editing. We present AraDiCE, a
benchmark for Arabic Dialect and Cultural
Evaluation. We evaluate LLMs on dialect com-
prehension and generation, focusing specifi-
cally on low-resource Arabic dialects. Addi-
tionally, we introduce the first-ever fine-grained
benchmark designed to evaluate cultural aware-
ness across the Gulf, Egypt, and Levant re-
gions, providing a novel dimension to LLM
evaluation. Our findings demonstrate that while
Arabic-specific models like Jais and AceGPT
outperform multilingual models on dialectal
tasks, significant challenges persist in dialect
identification, generation, and translation. This
work contributes ≈45K post-edited samples, a
cultural benchmark, and highlights the impor-
tance of tailored training to improve LLM per-
formance in capturing the nuances of diverse
Arabic dialects and cultural contexts. We have
released the dialectal translation models and
benchmarks developed in this study.1
1
Introduction
Large Language Models (LLMs) have consistently
pushed the boundaries of Natural Language Pro-
cessing (NLP), achieving state-of-the-art perfor-
mance on a wide range of tasks. These models
have excelled in areas such as machine translation,
summarization, sentiment analysis, and even more
complex applications like legal document analysis
and creative writing (OpenAI, 2023; Touvron et al.,
2023; Bubeck et al., 2023). Their remarkable abil-
ity to extract, reason, and generalize knowledge is
1https://huggingface.co/datasets/QCRI/AraDiCE
Cognitive Abilities
World Knowledge
Common Sense Reasoning
Reading Comprehension
Misinformation
AraDiCE Datasets
ArabicMMLU 
PIQA, OBQA, Winogrande
BoolQ, Belebele
TruthfulQA
Language and Dialects
MSA
LEV
EGY
Regional Arabic culture 
Dialect Understanding 
and Generation
Datasets
Dialect Identiﬁcation
Generation
QADI, ADI, ADD
MADAR, DA Generation
Cultural Understanding
Capabilities and datasets
GLF
AraDiCE-Culture
Figure 1: Capabilities and associated datasets for bench-
marking, evaluated on different dialects.
fueled by training on vast amounts of data covering
diverse topics and domains.
However, the success of these models is heav-
ily skewed towards languages with abundant re-
sources, such as English (Bang et al., 2023; Ahuja
et al., 2023). Low-resource languages, including
Arabic and its various dialects, are significantly un-
derrepresented in the datasets used to train these
models. This disparity poses a substantial chal-
lenge, as LLMs require extensive and diverse data
to perform effectively. Consequently, speakers of
low-resource languages are at a disadvantage, un-
able to fully benefit from the advancements in NLP
technologies. Recent efforts have been made to
train Arabic LLMs (Sengupta et al., 2023; Bari
et al., 2024; Fanar-Team, 2024) and to adapt mul-
tilingual models for Arabic (Touvron et al., 2023;
Huang et al., 2024), but these models are predomi-
nantly tailored to MSA, leaving them less effective
in handling dialectal Arabic (DA). To formalize
this observation, we conduct a systematic study to
benchmark Arabic and multilingual models in their
performance on Dialectal Arabic. More specifi-
cally, we aim to answer the following questions:
arXiv:2409.11404v3  [cs.CL]  17 Dec 2024

--- Page 2 ---

• Can LLMs effectively perform basic NLP tasks
in dialects? (Understanding and Generation)
• Can LLMs demonstrate reasoning, comprehen-
sion, and handle knowledge and misinformation
in dialects? (Cognitive Abilities)
• Are they aware of Arabic cultural knowledge?
(Cultural Understanding)
To this end, we compiled a comprehensive suite
of both existing and newly developed benchmarks
to assess the capabilities of these models. We pri-
marily evaluate their fundamental NLP abilities
in encoding dialects through dialect identification
(e.g. El-Haj et al. (2018)) and dialectal machine
translation (e.g. Abdul-Mageed et al. (2023)) tasks.
To assess broader cognitive abilities, we include
benchmarks that gauge World Knowledge (Ara-
bicMMLU (Koto et al., 2024)), Common Sense
Reasoning (PIQA (Bisk et al., 2020), OBQA (Mi-
haylov et al., 2018), Winogrande (Sakaguchi et al.,
2021)), Reading Comprehension, BoolQ (Clark
et al., 2019), Belebele (Bandarkar et al., 2024)),
and the ability to handle Misinformation (Truth-
fulQA (Lin et al., 2022)).
These benchmarks are primarily available in En-
glish, but researchers and practitioners have in-
creasingly turned to synthetic data creation meth-
ods to address the gap in low-resource languages
(Long et al., 2024). One promising approach in-
volves utilizing MT to generate synthetic datasets
for these languages. This method harnesses the
capabilities of existing translation models to create
large-scale, high-quality synthetic data, which can
then be used to train LLMs.
In this paper, we introduce a comprehensive ap-
proach that leverages MT, specifically from English
to MSA and MSA to dialects, combined with hu-
man post-editing, to develop synthetic benchmarks
for low-resource DA. We concentrate on the Lev-
antine (LEV), and Egyptian (EGY) dialects. Our
primary goal is to curate benchmarks that evaluate
the performance of LLMs across underrepresented
language and dialects.
Moreover, we introduce a third and novel bench-
mark, AraDiCE-Culture, focused on cultural
awareness across the Levantine, Egyptian, and Gulf
regions. This benchmark evaluates whether LLMs
grasp regional cultural nuances beyond language.
Our dataset includes questions on public holidays,
food, geography, history, public figures, traditional
clothing, and more. We probe cultural specifics
to assess if the LLMs can differentiate between
these regions, emphasizing the importance of mod-
els to understand both dialects and their cultural2
contexts. Our contributions in this work include:
• We develop benchmarks through the translation
and post-editing of dialectal data, and assess
LLMs’ performance in cognitive abilities, un-
derstanding, and generation tasks across MSA
and Dialectal Arabic.
• We create the first benchmark for region-wise
cultural evaluation in the Gulf, Egyptian, and
Levant regions.
• We present a comparative analysis of Arabic-
focused LLMs, such as Jais (Sengupta et al.,
2023) and AceGPT (Huang et al., 2024), along-
side state-of-the-art models Llama 3 (Touvron
et al., 2023) and Mistral (Jiang et al., 2023).
• To our knowledge, this is the first effort to de-
velop dialectal benchmarks for Arabic LLMs.
• We have released the dialectal translation models
and benchmarks curated in this study.
A summary of our findings is as follows:
Understanding and Generation LLMs
gener-
ally struggle with dialect identification, generation,
and translation tasks.
Although Arabic-centric
models perform better on dialectal tasks, their per-
formance still lags compared to MSA or English.
These models often rely on MSA knowledge for
distinguishing between dialects. They are better
at encoding and understanding dialects than at
generating or translating them, as evidenced in
dialect generation and translation tasks.
Cognitive Abilities Arabic-centric LLMs, such as
Jais and AceGPT are better equipped to handle
both MSA and its dialects. In contrast, multilin-
gual LLMs, such as Llama3 and Mistral, show
a substantial deficiency in adapting to Arabic di-
alects, highlighting a significant gap in their ability
to handle linguistic diversity in this context.
Cultural Understanding Arabic-centric models
also demonstrate a superior understanding of cul-
tural nuances compared to general multilingual
LLMs. This highlights the need for a more spe-
cialized training regimen to effectively address re-
gional linguistic and cultural variations.
Dialectal Variability The effectiveness of Arabic-
centric models varies notably across dialects, with
stronger performance in generating Gulf responses,
likely due to the dialect’s closer resemblance to
MSA. Our findings highlight the importance of
2We follow the definition of culture from AlKhamissi et al.
(2024), which describes it as “a multi-faceted inquiry reflect-
ing diversity across worldviews and belief systems.”

--- Page 3 ---

AraDiCE in assessing dialectal capabilities and
identifying gaps in LLM models.
2
Datasets
We begin by selecting a range of datasets com-
monly used for standard LLM benchmarking, in-
cluding specific to Arabic. These datasets evaluate
capabilities such as understanding and generation,
world knowledge, commonsense reasoning, read-
ing comprehension, misinformation, and cultural
understanding, as outlined in Figure 1.
We selected the datasets with a focus on diver-
sity and linguistic compatibility.3 These datasets
include tasks involving generation and multiple-
choice questions. The datasets used in this study
include: (i) four existing Arabic datasets for under-
standing and generation: Arabic Dialects Dataset
(ADD) (El-Haj et al., 2018), ADI (Abdelali et al.,
2024), and QADI (Abdelali et al., 2021), along
with a dialectal response generation dataset (Naous
et al., 2022), and MADAR (Bouamor et al., 2018);
(ii) seven datasets translated into MSA and di-
alects (Levantine and Egyptian),4 which include
ArabicMMLU (Koto et al., 2024) BoolQ (Clark
et al., 2019), PIQA (Bisk et al., 2020), OBQA (Mi-
haylov et al., 2018), Winogrande (Sakaguchi et al.,
2021), Belebele (Bandarkar et al., 2024), and Truth-
fulQA (Lin et al., 2022); and (iii) AraDiCE-Culture,
an in-house developed regional Arabic cultural un-
derstanding dataset. A detailed description of each
dataset can be found in Appendix A.
Cultural Dataset:
We curated a dataset of 180
culturally specific questions by hiring native an-
notators from the Gulf, Egypt, and the Levant re-
gions to generate seed questions centered on cul-
tural and country-specific themes. After reviewing
all submitted questions, we selected those with
varying answers across regions. To verify these
differences, we appended a country name to each
question and used Google Search to examine the
top 5 search results. Only questions with distinct
answers across countries were retained, resulting
in a final set of 30 unique questions. These ques-
tions were then translated into the dialects of six
countries within the targeted three regions (Gulf,
Levant, and Egypt). The questions span various
categories, including public holidays, food, geogra-
3By linguistic compatibility, we mean native speakers may
not use dialectal Arabic for queries related to programming
and coding.
4Except for ArabicMMLU, which is already in MSA.
phy, and religion. For gold-standard answers, we
followed the NativeQA framework (Hasan et al.,
2024). Annotators reviewed both the questions and
the top 5 search results, combining web data with
their cultural knowledge to provide the most ac-
curate answers. Detailed guidelines and sample
question-answer pairs can be found in Appendices
A.3, G and Table 26.
3
Machine Translation and Post-Editing
Machine Translation is crucial for developing re-
sources for low-resource languages with multiple
dialects, like Arabic, which has MSA for formal
use and diverse dialects like Egyptian and Levan-
tine for everyday communication (Durrani et al.,
2014).
These dialects differ significantly from
MSA and from each other, presenting unique chal-
lenges for NLP tasks.
For MSA, several studies have released datasets,
including MMLU, HellaSwag, and Arc-Challenge
by Okapi (Lai et al., 2023), as well as MMLU by
AceGPT (Huang et al., 2024). Due to inconsisten-
cies in the number of samples between the original
datasets, we refrained from adopting them directly.
Instead, we translated these datasets into MSA us-
ing Google Translate. Currently, no publicly avail-
able translation systems support direct translation
between Arabic dialects or between English and
specific Arabic dialects; most MT systems focus on
MSA-English translation. To address this gap, we
trained models to translate from MSA to various
Arabic dialects. Translated datasets were manually
post-edited for fluency and accuracy. Details of
our dialectal MT and post-editing framework are
provided below.
3.1
Dialectal MT
We develop MT models translating between MSA
and two major dialects: Egyptian and Levantine
Arabic.
By translating MSA benchmarks like
ArabicMMLU, we create resources for evaluating
LLMs’ understanding of dialectal Arabic.
Data:
For training our translation systems, we
utilized several datasets, including the MADAR
(Bouamor et al., 2018), UFAL (Krubi´nski et al.,
2023), LDC (Mubarak, 2018), ArzEn-MultiGenre
(Hamed et al., 2023), and the SADID (Abid, 2020).
Please see Appendix B.1 for more details.
Models:
We fine-tuned two robust machine trans-
lation models: AraT5 (Nagoudi et al., 2022) and

--- Page 4 ---

Data
Set Trans. Edited
Size
Understanding and Generation
QADI
Test
✗
✗
2,597
ADI
Test
✗
✗
550
MADAR
Test
✗
✗
37,550
DA Response
Test
✗
✗
1,000
Cognitive Abilities
ArabicMMLU
Test
✓
✓
14,459
PIQA
Val
✓
✓
1838
OBQA
Test
✓
✓
500
Belebele
Test
✗
✗
3,600
Winogrande
Val
✓
✓
1,267
TruthfulQA
Test
✓
✓
780
BoolQ
Val
✓
✓
892
Cultural Understanding
AraDiCE-Culture Test
-
-
180
Table 1: Selected datasets with translation and editing
status: Trans: Translation | Edited: Post-editing.
NLLB (Team et al., 2022). We experimented with
several variants of these models, with sizes rang-
ing from 600M to 3.3B parameters. AraT5 is an
Arabic language model based on the T5 (Text-to-
Text Transfer Transformer) architecture. In our
preliminary experiments, we found the NLLB 3.3B
model to surpass AraT5 and its smaller variants,
post fine-tuning with dialectal data. We carried out
ablation studies using different data mixtures on
the NLLB 3.3B model. We shortlisted three sys-
tems per dialect using BLEU scores as the primary
criterion (see Tables 5 and 6 in Appendix B.3) and
conducted human evaluation to select the best sys-
tem for each dialect. Please see Appendix B for
details on our exploration of Dialectal MT.
3.2
Post-Editing of MT (PEMT)
The translated datasets were manually post-edited
to ensure fluency and adequacy. We post-edited
the majority of the test sets (see Table 1), with the
exception of BoolQ and TruthfulQA. For these two
datasets, we chose specific samples for post-editing
based on the following criteria: (i) shorter text
length to minimize post-editing effort, (ii) cultural
and religious compatibility with the Arab region,
and (iii) linguistic compatibility with Arabic. We
excluded language-specific samples, such as those
asking for the origin of an English word. In Table
1, we provide statistics of the datasets along with
their translation and post-editing status.
Guidelines
To assist the translators and maintain
dataset integrity, we provided two sets of guide-
lines for each dataset (except Arabic MMLU). One
set focused on post-editing translated samples in
MSA, while the other targeted the same process
for dialects. Each dataset’s guidelines included: (i)
details on the task components (e.g., one question
and four answers), (ii) general instructions for cor-
recting errors and improving fluency and adequacy,
and (iii) specific instructions for handling unique
cases within the datasets. Detailed instructions for
the guidelines are provided in the Appendix F.
Team and Setup
The translation team comprised
32 native speakers fluent in Levantine, Egyptian,
and MSA, with educational backgrounds ranging
from Bachelor’s to Master’s degrees, and ages be-
tween 21 and 53. Many were professional transla-
tors. They received specific guidelines and train-
ing tailored to each dataset and dialect to ensure
translation quality. To manage the post-editing
workload efficiently, we assigned one translator per
item, which helped minimize costs and time. A
random sample of post-edited texts was reviewed
by the expert translators for quality assurance. The
process was streamlined using an in-house annota-
tion platform and 17 dedicated projects, resulting
in the post-editing of ≈45K items. A third-party
company handled the hiring and competitive com-
pensation of translators.
While synthetic datasets, such as those gener-
ated through machine translation, offer valuable
opportunities to expand data coverage, they can
introduce inherent biases that are difficult to com-
pletely mitigate during post-editing. To address
this, our approach emphasizes refining translations
to ensure alignment with Arabic linguistic nuances
and cultural relevance. For tasks requiring world
knowledge, we opted for ArabicMMLU (origi-
nally in Modern Standard Arabic, or MSA) instead
of MMLU, as it better represents the knowledge
and contexts relevant to Arabic-speaking commu-
nities and regions. For the Winogrande dataset, we
made specific adjustments to culturally sensitive
instances, as detailed in Section H.1.3.
4
Experimental Setup
Models:
For the LLMs benchmarking experi-
ments we used open models, such as Llama-3-
8B-Instruct (Touvron et al., 2023), Mistral-7B-

--- Page 5 ---

QADI
ADI
ADD
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
F1
Rand
Llama 3
Mistral
Jais
AceGPT
SOTA
Figure 2: Comparison on dialect identification
GLF
LEV
EGY
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
Rand
Llama 3
Mistral
Jais
AceGPT
Figure 3: Results on dialect generation
Instruct (Jiang et al., 2023),5 AceGPT-13B-chat
(Huang et al., 2024) and Jais-13b-chat (Sengupta
et al., 2023). A random model6 was used as a base-
line to evaluate the relative performance of these
LLMs. We have chosen to use only open models
to reduce the computational budget.
Prompt:
In our experiments, we employed zero-
shot learning to observe performance differences
across dialects.
Although few-shot learning is
known to enhance performance, we chose not to
include it to simplify the experiments and mini-
mize computational costs. We used prompts in
English, MSA, and dialects depending on the task,
and released both the prompts and configurations
via lm-harness.
Evaluation:
We used the LM Evaluation Har-
ness7 for both generation and multiple-choice tasks,
employing standard metrics for each task and
dataset. We used F1 scores for dialect identifica-
tion, normalized accuracy for cognitive tasks, and
SacreBLEU (Post, 2018) for machine translation.
5
Results
5.1
Understanding and Generation
We evaluate the models’ ability to encode and gen-
erate dialectal Arabic, focusing on tasks like dialect
identification, dialect generation, and MT.
5https://huggingface.co/mistralai/
Mistral-7B-Instruct-v0.2
6https://huggingface.co/HuggingFaceH4/
tiny-random-LlamaForCausalLM
7https://github.com/EleutherAI/
lm-evaluation-harness
5.1.1
Dialect Identification
Figure 2 show that all LLMs struggle to distinguish
between dialects, especially compared to SOTA
models (Hassan et al., 2021). Performance varies
across datasets: Llama 3 excels on QADI, while
Jais outperforms it on ADI and ADD, likely due to
differences in the data—QADI uses tweets, ADI
has speech transcripts, and ADD includes Arabic
commentaries. Our error analysis (Figure 4) shows
Llama 3 confuse Gulf with Lev, Mistral confuses
MSA with Lev/Gulf, Jais often confuse Egy with
Gulf, while AceGPT mistakes MSA for Gulf. The
models tend to fall back on MSA knowledge when
distinguishing between dialects. Please see Ap-
pendix C.1 for a more comprehensive analysis.
5.1.2
Dialect Generation
We assessed the models’ ability to generate re-
sponses in dialectal Arabic. Initially, we used a
dialectal response generation task (Naous et al.,
2022), where models were prompted in a specific
dialect and asked to generate a response. However,
qualitative analysis revealed that models often ex-
plained the prompt instead of generating a dialectal
response (see Appendix C.2 for examples). To ad-
dress this, we simplified the task: models were
given multiple response options, with only one in
the correct dialect, and asked to select the best re-
sponse. Accuracy scores for this MCQ response se-
lection task are shown in Figure 3. Overall, models
performed better on the Gulf dialect, with Arabic
LLMs like Jais and AceGPT outperforming Llama
3 and Mistral across all dialects.
5.1.3
Machine Translation
To assess the models’ capacity to encode and gener-
ate dialectal knowledge, we use Dialect-to-English,
MSA and English, MSA-to-Dialect tasks. The for-
mer evaluates the ability to encode dialects, while
the latter assesses generation capabilities. Results
averaged across multi-dialectal MADAR test sets
are shown in Table 2. Several observations emerge:
Dialect-to-English translation scores are signifi-
cantly higher across all models and dialects com-
pared to translations into dialects. This suggests
that models excel at understanding and encod-
ing dialects more than generating them. While
the models benefit from their similarity to MSA in
encoding, they struggle with generating dialectal
text due to differing vocabulary and data sparsity.
This highlights limitations in producing fluent and
accurate dialectal language.

--- Page 6 ---

MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.01
0.05
0.00
0.02
0.06
0.37
0.00
0.12
0.03
0.21
0.00
0.07
0.01
0.03
0.00
0.04
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
(a) Llama 3
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.03
0.04
0.00
0.00
0.35
0.17
0.00
0.02
0.21
0.08
0.00
0.01
0.05
0.02
0.00
0.01
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
(b) Mistral
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.01
0.01
0.00
0.06
0.04
0.15
0.01
0.34
0.02
0.02
0.07
0.20
0.00
0.00
0.00
0.08
0.05
0.10
0.15
0.20
0.25
0.30
(c) Jais
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.07
0.00
0.00
0.01
0.40
0.00
0.00
0.14
0.22
0.00
0.00
0.09
0.03
0.00
0.00
0.05
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
(d) AceGPT
Figure 4: Confusion matrices on dialect identification (QADI) dataset
Dialects-to-English
English-to-Dialects
MSA-to-Dialects
Dialect
Llama 3
Mistral
Jais
AceGPT
Llama 3
Mistral
Jais
AceGPT
Llama 3
Mistral
Jais
AceGPT
Gulf
25.7
15
36.1
37.8
2.4
0.5
1.0
1.5
2.2
0.7
1.6
3.1
Levantine
23.0
12.2
36.1
35.3
1.4
0.2
0.9
2.1
1.3
0.3
1.3
3.0
Egyptian
26.9
13.9
40.2
39.8
2.0
0.4
1.2
3.8
1.5
0.3
2.1
3.8
Table 2: Average BLEU scores across three translation tasks using MADAR test sets
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Accuracy
Rand
Llama 3
Mistral
Jais
AceGPT
Figure 5: Average scores on ArabicMMLU
AceGPT consistently scores higher in BLEU
across all dialects, showing superior translation
performance. Jais also performs well compared to
Llama 3 and Mistral, which score lower. However,
all models show significantly reduced BLEU scores
for translating into dialects, complicating reliable
performance comparisons in this direction.
5.2
Cognitive Abilities
We now assess the dialectal Arabic abilities in
LLMs through world knowledge, reading compre-
hension, commonsense reasoning, and misinforma-
tion tasks, providing a thorough evaluation of their
performance on dialect-specific challenges.
5.2.1
World Knowledge
The overall results in Figure 5 show that AceGPT
and Jais excel across the board on both the EGY
and LEV ArabicMMLU benchmarks proposed in
this work, and the original MSA ArabicMMLU.
This suggests that these Arabic-centric models are
well-suited not only for MSA but also for dialectal
variations. In contrast, Llama 3 and Mistral, which
are not trained specifically on Arabic, struggle sig-
nificantly more with EGY and LEV compared to
their performance on ArabicMMLU. This high-
lights the effectiveness of the proposed dialectal
benchmarks in revealing performance gaps in gen-
eral models. These results demonstrate the need for
models trained on dialectal data to handle the com-
plexity of regional variations. Detailed individual
results are provided in the Appendix D.1.
5.2.2
Commonsense Reasoning
Our evaluation across the PIQA, OBQA, and Wino-
grande (See Figure 6) reveals several key insights
into model performance with respect to MSA and
various Arabic dialects, and how these compare
to English. Jais consistently outperforms other
models across MSA and dialects, including Lev
and Egy, demonstrating a strong ability to han-
dle physical commonsense reasoning and complex
linguistic nuances. AceGPT also performs well,
particularly in Egy, but falls slightly behind Jais in
MSA and Lev. This suggests Jais is better tuned
for the broader spectrum of Arabic dialects. In
contrast, Llama 3 and Mistral show a significant
performance drop from English-to-dialectal Arabic,
indicating challenges likely due to limited training
data for these dialects.
Task-specific Insights
Jais leads in handling
PIQA across MSA and dialects, indicating its ad-
vanced capability in dealing with dialectal intri-
cacies. AceGPT, while effective, shows slightly
reduced performance compared to Jais, especially
in MSA and Lev dialects. Llama 3 and Mistral’s
substantial performance drop highlights their dif-
ficulties with dialectal Arabic, reinforcing the im-
pact of training data limitations. In OBQA, both
AceGPT and Jais perform relatively well in MSA
and dialects, with AceGPT having a slight edge in
Egy dialect. This performance illustrates their pro-

--- Page 7 ---

Rand
Llama 3
Mistral
Jais
AceGPT
MSA
LEV
EGY
ENG
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
(a) PIQA
MSA
LEV
EGY
ENG
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
(b) Winogrande
MSA
LEV
EGY
ENG
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
(c) OBQA
Figure 6: Results for the commonsense reasoning capabilities
MSA
LEV
EGY
ENG
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Accuracy
Rand
Llama 3
Mistral
Jais
AceGPT
Figure 7: Results on misinformation (TruthfulQA)
ficiency in handling multi-step reasoning in Arabic.
Mistral and Llama 3, despite their strong English
performance, struggle with MSA and dialects, re-
flecting the challenges posed by Arabic-specific
content and dialectal variations due to their focus
on resource-rich languages during training.
In Winogrande, Jais excels in commonsense rea-
soning across MSA and Lev dialects, surpassing
other models. AceGPT also performs effectively
across all dialects but does not exceed Jais, indi-
cating that while it is proficient, it lacks the spe-
cialized edge found in Jais. Llama 3 and Mistral
show reduced performance in dialects compared
to MSA, revealing their limitations in managing
dialectal variations and highlighting the impact of
their English-centric training.
5.2.3
Reading Comprehension
Figure 8 show our results on reading comprehen-
sion tasks. The results across BoolQ and Belebele
provide insights into how different models handle
reading comprehension in MSA and dialects com-
pared to English. For the BoolQ task, we observe
that while Llama 3 performs exceptionally well in
English, achieving 0.85 accuracy, its performance
drops noticeably when applied to MSA (0.74) and
even further in Lev (0.71) and Egy (0.73). This
indicates a significant challenge for general models
when transitioning from English to dialectal Arabic,
despite the rich knowledge base Llama has. Inter-
estingly, Mistral and Jais show a similar drop in
performance across dialects, with Jais maintaining
relatively higher accuracy in MSA, likely due to its
Arabic-centric training. However, AceGPT stands
out with the highest MSA score (0.77) and remains
competitive across dialects, suggesting that it better
adapts to the linguistic variations within Arabic.
For the Belebele dataset, the performance trends
are similar. AceGPT and Jais lead the pack in
MSA and dialects, with Jais achieving the highest
MSA score (0.57) and performing equally well in
Lev and Egy (0.49). This further demonstrates
the ability of Arabic-centric models to leverage
dialect similarities and perform well across diverse
Arabic varieties. Llama and Mistral, while strong
in general tasks, show a clear performance gap
when tested on Arabic dialects, particularly in Egy,
suggesting that they struggle to bridge the linguistic
distance between MSA and its dialects.
5.2.4
Misinformation
The results for the TruthfulQA task across Lev, Egy,
and MSA show that model performances are often
close to random, especially for Lev and Egy, as
reported in Figure 7. Mistral performs best overall,
particularly in Lev, but its scores are only slightly
above random. We leave a detailed exploration of
this for the future.
5.3
Cultural Understanding
The results on the cultural understanding task
(MCQ version–Figure 9), indicate that Jais is the
most culturally aligned model, followed closely
by AceGPT, both showing superior awareness of
the Egyptian culture. One possible justification
is that the Egyptian population (and consequently
its online presence) is significantly larger than the
other two regions. Llama 3 and Mistral generally
show performances close to the random baseline,
suggesting limited awareness of Arabic culture.
In a qualitative analysis of the models’ responses
(when prompting the models in a generation setup),
Llama 3 frequently generated fictional entities (e.g.,
names of people or holidays) and lacked geograph-
ical and historical knowledge. For example, when

--- Page 8 ---

Rand
Llama 3
Mistral
Jais
AceGPT
MSA
LEV
EGY
ENG
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
(a) Belebele
MSA
LEV
EGY
ENG
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
(b) BoolQ
Figure 8: Results on reading comprehension
GLF
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
Rand
Llama 3
Mistral
Jais
AceGPT
Figure 9: Results on cultural understanding
asked about the highest mountain in Jordan, it incor-
rectly named a mountain in Saudi Arabia. Jais and
AceGPT performed better overall, though AceGPT
had some issues following instructions as accu-
rately as Jais. Further discussion and example mod-
els’ responses can be found in the Appendix E.
5.4
Additional Model Evaluations
To validate the applicability of the proposed
AraDiCE benchmark, we expand our evaluation
to cutting-edge models in Arabic and multilin-
gual language modeling, including Fanar (Fanar-
Team, 2024), Gemma-2-9B (Team et al., 2024),
Aya-Expanse-8B (Üstün et al., 2024), Qwen2.5-
7B (Yang et al., 2024), Llama-3.1-8B-Instruct, and
AceGPT-v2-8B-Chat. These models represent di-
verse architectures and training paradigms, offering
valuable insights into handling complex linguistic
phenomena. Fanar, built on Gemma, highlights
the potential of Arabic-centric pretraining, while
Qwen and Aya reflect innovations in multilingual
fine-tuning. Due to resource constraints, we focus
on Arabic MMLU and PIQA datasets, which assess
performance on diverse, challenging tasks. This
extended evaluation underscores AraDiCE’s role in
advancing Arabic LLM benchmarks and guiding
future developments.
ArabicMMLU:
As we observed earlier, the mod-
els generally perform better on MSA than on the
dialects, reflecting the resource-rich training avail-
able for MSA data. Among the models (as shown
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
Fanar 8.7B
Jais 13B
Qwen2.5 7B
AceGPTv2 8B
Gemma2 9B
Aya 8B
Llama 8B
Figure 10: Performance of various models on the Arabic
MMLU across MSA, Levantine, and Egyptian.
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
Fanar 8.7B
Jais 13B
Qwen2.5 7B
AceGPTv2 8B
Gemma2 9B
Aya 8B
Llama 8B
Figure 11: Performance of various models on the Arabic
PIQA across MSA, Levantine, and Egyptian.
in Figure 10), Fanar 8.7B stands out as the top
performer, showcasing strong capabilities in both
MSA and dialects. Its superior performance in
MSA can be attributed to its MSA-specific training
and its foundation on Gemma2 9B, which provides
a robust baseline. Notably, Gemma2 outperforms
other Arabic-centric models on dialects in the Ara-
bicMMLU, highlighting its strength in handling
dialectal variations.
PIQA:
As shown in Figure 11, in PIQA, a task
focused on common-sense reasoning, Fanar 8.7B
again outperforms the other models, particularly
in Egyptian Arabic. Jais 13B follows closely be-
hind, demonstrating solid generalization across
MSA and dialects, though it still lags behind Fa-
nar in dialectal contexts. The Qwen2.5 7B model,
while less competitive in MMLU, performs better
on PIQA for Levantine and Egyptian, suggesting
that its reasoning capabilities are more adaptable
to dialectal inputs. Gemma2 9B and Aya 8B show

--- Page 9 ---

more consistent, though lower, performance across
both dialects and MSA. The gap between Gemma2
and Aya is relatively small, with Aya performing
slightly better in Egyptian Arabic in both MMLU
and PIQA tasks, suggesting that Aya might have
some potential in specialized domains.
These results highlight the ongoing challenges
of Arabic dialectal processing and reinforce the ef-
ficacy of AraDiCE as a benchmark that can expose
performance gaps across dialects. Moreover, the
models tested here exhibit varying degrees of sen-
sitivity to dialectal variations, indicating that future
model development and fine-tuning efforts need
to take into account dialectal diversity to improve
overall Arabic LLMs capabilities.
6
Related Work
There has been considerable work on benchmark-
ing language models in Arabic, with prior research
often including Arabic in multilingual benchmarks
like XGLUE (Liang et al., 2020), XTREME (Hu
et al., 2020), XTREME-R (Ruder et al., 2021),
GEM (Gehrmann et al., 2021), Dophin (Nagoudi
et al., 2023). These benchmarks cover a variety of
tasks, primarily focusing on classification problems
such as natural language inference and generation,
part-of-speech tagging, named entity recognition,
and summarization.
Another relevant dataset is EXAMS (Hardalov
et al., 2020), featuring multilingual school exam
questions, including about 500 in Arabic. This
dataset extends evaluation to educational contexts,
providing a diverse testing ground for language
models. Notable benchmarks in the realm of ques-
tion answering (QA), that primarily aim to evalu-
ate models on reading comprehension and QA in-
clude TyDiQA (Clark et al., 2020), Arabic-SQuAD
(Mozannar et al., 2019), and MLQA (Lewis et al.,
2020).
These datasets primarily aim to evalu-
ate models on reading comprehension and QA.
More recently, Koto et al. (2024) introduced Ara-
bicMMLU, focusing on the MENA region. The
dataset includes 40 tasks in MSA. However, a limi-
tation of their work, is the lack of dialectal Arabic.
Significant efforts have been made in training
Arabic language models (LMs) (Antoun et al.,
2020; Inoue et al., 2021; Abdul-Mageed et al.,
2021; Nagoudi et al., 2022) and more recently,
LLMs like Jais (Sengupta et al., 2023), AceGPT
(Huang et al., 2024), ALLaM (Bari et al., 2024),
Arabic Stable LM (Alyafeai et al., 2024), and FA-
NAR (Fanar-Team, 2024). Jais is trained from
scratch on 72 billion Arabic tokens, AceGPT builds
on Llama2 with reinforcement learning from AI
feedback, ALLaM spans 7B–70B parameters but is
not publicly available, Arabic Stable LM fine-tunes
Stable LM 2 with 1.6B parameters, and FANAR
LLM supports diverse language, speech, and image
generation tasks.
There has also been efforts benchmarking LLMs
for Arabic, most notably focusing on standard
LLMs based dataset evaluation (Sengupta et al.,
2023) and NLP tasks (Khondaker et al., 2023; Ab-
delali et al., 2024; Dalvi et al., 2024), prompting in
native (Arabic) and non-native (English) language
(Kmainasi et al., 2025) and multimodality (Alwajih
et al., 2024; Das et al., 2024).
Focusing on benchmarking the cultural capabili-
ties of LLMs, this includes measuring how entity
mentions are culturally biased towards Western or
Arab contexts (Naous et al., 2024), and assessing
cultural alignment based on the World Values Sur-
vey (AlKhamissi et al., 2024). Other notable work
on cultural benchmarking include (Demidova et al.,
2024; Shen et al., 2024; Liu et al., 2024; Arora
et al., 2024; Myung et al., 2024). While prior work
has focused on benchmarking LLMs for MSA, our
study extends this by evaluating both MSA and
dialects (Lev and Egy) using Arabic-centric and
non-Arabic-centric LLMs.
7
Conclusions
We developed dialectal Arabic benchmarks through
machine translation and post-editing. Our bench-
marks evaluate various NLP tasks, including under-
standing, generation, and cultural awareness across
Arabic dialects. Our results show that while Arabic-
centric models like FANAR, Jais and AceGPT per-
form better in dialectal contexts, they still face
challenges compared to MSA and English. Per-
formance varies by dialect and task, highlighting
the need for more specialized training for effec-
tive handling of regional linguistic and cultural nu-
ances. We have released our dialectal benchmarks
and models to support future research and advance-
ments in NLP for low-resource languages. We
also released the dialectal translation models8 and
benchmarks developed in this study to support fur-
ther research in NLP for low-resource languages.
8https://huggingface.co/datasets/QCRI/AraDiCE

--- Page 10 ---

8
Limitations
• Post-editing machine translation outputs is a
tedious process, and the translator’s choice of
words can significantly impact translation qual-
ity. We provided clear instructions, conducted
thorough training, and reviewed random samples
to offer feedback. However, due to the size and
diversity of the datasets, we could not review all
datasets comprehensively.
• Another issue to highlight is that most datasets,
except ArabicMMLU, are adapted from En-
glish and thus are influenced by Western culture.
While we made efforts in annotation guidelines
and post-editing to address these cultural biases,
the subjective nature of sensitivity means that
some samples may still be considered sensitive
by different individuals or communities.
• While our study primarily focuses on Arabic
dialects, it is limited in its coverage of the di-
verse dialects spoken across the Arab region. We
mainly addressed Levantine, Gulf and Egyptian
Arabic, but left out dialects such as Maghrebi
and Sudanese. Future work should aim to fill
these gaps by expanding coverage to a broader
range of dialects, providing a more comprehen-
sive evaluation of Arabic language models.
• Due to resource limitations, we only evaluated
our benchmarks using models up to 13B parame-
ters. As a one-off experiment, we tested the Ara-
bicMMLU task with a larger Jais 30B,9 model.
We found (See results in Appendix D.1, Figure
15) Jais 30B to perform similarly to Jais 13B indi-
cating that larger models do not necessarily show
significant improvements in this case. Due to
hardware limitations, we could not run Jais 70B
models, but it would be interesting to compare
the higher-scale Jais and Llama models to see if
their increased scale can compensate for the lack
of dialect-specific training.
Ethical Consideration
We do not anticipate any ethical issues in this study.
We extended publicly available datasets through the
PEMT process. Additionally, our culturally aware
AraDiCE-Culture dataset, consists of question-
answer pairs based on commonsense knowledge
and does not include information related to indi-
vidual or organizational identities. Therefore, we
9https://huggingface.co/inceptionai/
jais-30b-chat-v1
do not foresee any potential risks arising from the
outcomes of our study.
References
Ahmed Abdelali, Hamdy Mubarak, Shammur Chowd-
hury, Maram Hasanain, Basel Mousi, Sabri Boughor-
bel, Samir Abdaljalil, Yassine El Kheir, Daniel Izham,
Fahim Dalvi, Majd Hawasly, Nizi Nazar, Youssef
Elshahawy, Ahmed Ali, Nadir Durrani, Natasa Milic-
Frayling, and Firoj Alam. 2024. LAraBench: Bench-
marking Arabic AI with large language models. In
Proceedings of the 18th Conference of the European
Chapter of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 487–520,
St. Julian’s, Malta. Association for Computational
Linguistics.
Ahmed Abdelali, Hamdy Mubarak, Younes Samih,
Sabit Hassan, and Kareem Darwish. 2021. QADI:
Arabic dialect identification in the wild. In Proceed-
ings of the Sixth Arabic Natural Language Process-
ing Workshop, pages 1–10, Kyiv, Ukraine (Virtual).
Association for Computational Linguistics.
Muhammad Abdul-Mageed, AbdelRahim Elmadany,
and El Moatez Billah Nagoudi. 2021. ARBERT &
MARBERT: Deep bidirectional transformers for Ara-
bic. In Proceedings of the 59th Annual Meeting of the
Association for Computational Linguistics and the
11th International Joint Conference on Natural Lan-
guage Processing (Volume 1: Long Papers), pages
7088–7105, Online. Association for Computational
Linguistics.
Muhammad Abdul-Mageed, AbdelRahim Elmadany,
Chiyu Zhang, El Moatez Billah Nagoudi, Houda
Bouamor, and Nizar Habash. 2023. NADI 2023: The
fourth nuanced Arabic dialect identification shared
task. In Proceedings of ArabicNLP 2023, pages 600–
613, Singapore (Hybrid). Association for Computa-
tional Linguistics.
Wael Abid. 2020. The SADID evaluation datasets for
low-resource spoken language machine translation
of Arabic dialects. In Proceedings of the 28th Inter-
national Conference on Computational Linguistics,
pages 6030–6043, Barcelona, Spain (Online). Inter-
national Committee on Computational Linguistics.
Kabir Ahuja, Harshita Diddee, Rishav Hada, Milli-
cent Ochieng, Krithika Ramesh, Prachi Jain, Ak-
shay Nambi, Tanuja Ganu, Sameer Segal, Mohamed
Ahmed, Kalika Bali, and Sunayana Sitaram. 2023.
MEGA: Multilingual evaluation of generative AI.
In Proceedings of the 2023 Conference on Empir-
ical Methods in Natural Language Processing, pages
4232–4267, Singapore. Association for Computa-
tional Linguistics.
Badr AlKhamissi,
Muhammad ElNokrashy,
Mai
Alkhamissi, and Mona Diab. 2024. Investigating
cultural alignment of large language models. In Pro-
ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 12404–12422, Bangkok, Thailand.
Association for Computational Linguistics.

--- Page 11 ---

Fakhraddin Alwajih, Gagan Bhatia, and Muhammad
Abdul-Mageed. 2024. Dallah: A dialect-aware mul-
timodal large language model for arabic. In Pro-
ceedings of The Second Arabic Natural Language
Processing Conference, pages 320–336.
Zaid Alyafeai, Michael Pieler, Hannah Teufel, Jonathan
Tow, Marco Bellagente, Duy Phung, Nikhil Pinna-
paraju, Reshinth Adithyan, Paulo Rocha, Maksym
Zhuravinskyi, et al. 2024. Arabic Stable LM: Adapt-
ing stable lm 2 1.6 b to arabic.
arXiv preprint
arXiv:2412.04277.
Wissam Antoun, Fady Baly, and Hazem Hajj. 2020.
AraBERT: Transformer-based model for Arabic lan-
guage understanding. In Proceedings of the 4th Work-
shop on Open-Source Arabic Corpora and Process-
ing Tools, with a Shared Task on Offensive Language
Detection, pages 9–15, Marseille, France. European
Language Resource Association.
Shane Arora, Marzena Karpinska, Hung-Ting Chen,
Ipsita Bhattacharjee, Mohit Iyyer, and Eunsol Choi.
2024. CaLMQA: Exploring culturally specific long-
form question answering across 23 languages. arXiv
preprint arXiv:2406.17761.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2024. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 749–775,
Bangkok, Thailand. Association for Computational
Linguistics.
Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wen-
liang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei
Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan
Xu, and Pascale Fung. 2023. A multitask, multilin-
gual, multimodal evaluation of ChatGPT on reason-
ing, hallucination, and interactivity. In Proceedings
of the 13th International Joint Conference on Nat-
ural Language Processing and the 3rd Conference
of the Asia-Pacific Chapter of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 675—-718, Indonesia. Association for Compu-
tational Linguistics.
M Saiful Bari, Yazeed Alnumay, Norah A. Alzahrani,
Nouf M. Alotaibi, Hisham A. Alyahya, Sultan Al-
Rashed, Faisal A. Mirza, Shaykhah Z. Alsubaie, Has-
san A. Alahmed, Ghadah Alabduljabbar, Raghad
Alkhathran, Yousef Almushayqih, Raneem Alna-
jim, Salman Alsubaihi, Maryam Al Mansour, Ma-
jed Alrubaian, Ali Alammari, Zaki Alawami, Abdul-
mohsen Al-Thubaity, Ahmed Abdelali, Jeril Kuri-
akose, Abdalghani Abujabal, Nora Al-Twairesh,
Areeb Alowisheq, and Haidar Khan. 2024.
AL-
LaM: Large language models for arabic and english.
arXiv:2407.15390.
Alexandra Birch, Matthias Huck, Nadir Durrani, Niko-
lay Bogoychev, and Philipp Koehn. 2014. Edinburgh
SLT and MT system description for the IWSLT 2014
evaluation. In Proceedings of the 11th International
Workshop on Spoken Language Translation: Evalua-
tion Campaign, pages 49–56, Lake Tahoe, California.
Yonatan Bisk, Rowan Zellers, Jianfeng Gao, Yejin Choi,
et al. 2020. PIQA: Reasoning about physical com-
monsense in natural language. In Proceedings of the
AAAI conference on artificial intelligence, volume 34,
pages 7432–7439.
Houda Bouamor, Nizar Habash, Mohammad Salameh,
Wajdi Zaghouani, Owen Rambow, Dana Abdul-
rahim, Ossama Obeid, Salam Khalifa, Fadhl Eryani,
Alexander Erdmann, and Kemal Oflazer. 2018. The
MADAR Arabic dialect corpus and lexicon. In Pro-
ceedings of the Eleventh International Conference on
Language Resources and Evaluation (LREC 2018),
Miyazaki, Japan. European Language Resources As-
sociation (ELRA).
Justus Brockmann, Claudia Wiesinger, and Dragos,
Ciobanu. 2022. Error annotation in post-editing ma-
chine translation: Investigating the impact of text-to-
speech technology. In Proceedings of the 23rd An-
nual Conference of the European Association for Ma-
chine Translation, pages 251–259, Ghent, Belgium.
European Association for Machine Translation.
Sébastien Bubeck, Varun Chandrasekaran, Ronen El-
dan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Pe-
ter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg,
Harsha Nori, Hamid Palangi, Marco Tulio Ribeiro,
and Yi Zhang. 2023. Sparks of artificial general in-
telligence: Early experiments with GPT-4. Technical
report, Microsoft Research.
Christopher Clark, Kenton Lee, Ming-Wei Chang,
Tom Kwiatkowski, Michael Collins, and Kristina
Toutanova. 2019. BoolQ: Exploring the surprising
difficulty of natural yes/no questions. In Proceedings
of the 2019 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies, Volume 1 (Long and
Short Papers), pages 2924–2936.
Jonathan H. Clark, Eunsol Choi, Michael Collins, Dan
Garrette, Tom Kwiatkowski, Vitaly Nikolaev, and
Jennimaria Palomaki. 2020. TyDi QA: A benchmark
for information-seeking question answering in typo-
logically diverse languages. Transactions of the As-
sociation for Computational Linguistics, 8:454–470.
Fahim Dalvi, Maram Hasanain, Sabri Boughorbel,
Basel Mousi, Samir Abdaljalil, Nizi Nazar, Ahmed
Abdelali, Shammur Absar Chowdhury, Hamdy
Mubarak, Ahmed Ali, Majd Hawasly, Nadir Dur-
rani, and Firoj Alam. 2024. LLMeBench: A flexible
framework for accelerating LLMs benchmarking. In
Proceedings of the 18th Conference of the European
Chapter of the Association for Computational Lin-
guistics: System Demonstrations, pages 214–222, St.
Julians, Malta. Association for Computational Lin-
guistics.
Rocktim Das, Simeon Hristov, Haonan Li, Dimitar
Dimitrov, Ivan Koychev, and Preslav Nakov. 2024.
EXAMS-V: A multi-discipline multilingual multi-
modal exam benchmark for evaluating vision lan-
guage models. In Proceedings of the 62nd Annual

--- Page 12 ---

Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 7768–7791,
Bangkok, Thailand. Association for Computational
Linguistics.
Anastasiia Demidova, Hanin Atwany, Nour Rabih,
Sanad Sha’ban, and Muhammad Abdul-Mageed.
2024. John vs. ahmed: Debate-induced bias in mul-
tilingual LLMs. In Proceedings of The Second Ara-
bic Natural Language Processing Conference, pages
193–209, Bangkok, Thailand. Association for Com-
putational Linguistics.
Nadir Durrani, Yaser Al-Onaizan, and Abraham Itty-
cheriah. 2014. Improving egyptian-to-english SMT
by mapping egyptian into MSA. In Computational
Linguistics and Intelligent Text Processing - 15th In-
ternational Conference, CICLing 2014, Kathmandu,
Nepal, April 6-12, 2014, Proceedings, Part II, volume
8404 of Lecture Notes in Computer Science, pages
271–282. Springer.
Mahmoud El-Haj, Paul Rayson, and Mariam Aboelezz.
2018. Arabic dialect identification in the context
of bivalency and code-switching. In Proceedings of
the Eleventh International Conference on Language
Resources and Evaluation (LREC 2018), Miyazaki,
Japan. European Language Resources Association
(ELRA).
Fanar-Team. 2024.
Fanar: An arabic-centric multi-
modal generative ai platform. https://fanar.qa/en.
Sebastian Gehrmann, Tosin Adewumi, Karmanya
Aggarwal,
Pawan
Sasanka
Ammanamanchi,
Anuoluwapo
Aremu,
Antoine
Bosselut,
Khy-
athi Raghavi Chandu, Miruna-Adriana Clinciu,
Dipanjan Das, Kaustubh Dhole, Wanyu Du, Esin
Durmus, Ondˇrej Dušek, Chris Chinenye Emezue,
Varun
Gangal,
Cristina
Garbacea,
Tatsunori
Hashimoto, Yufang Hou, Yacine Jernite, Harsh Jham-
tani, Yangfeng Ji, Shailza Jolly, Mihir Kale, Dhruv
Kumar, Faisal Ladhak, Aman Madaan, Mounica
Maddela, Khyati Mahajan, Saad Mahamood, Bod-
hisattwa Prasad Majumder, Pedro Henrique Martins,
Angelina McMillan-Major, Simon Mille, Emiel van
Miltenburg, Moin Nadeem, Shashi Narayan, Vitaly
Nikolaev, Andre Niyongabo Rubungo, Salomey
Osei,
Ankur
Parikh,
Laura
Perez-Beltrachini,
Niranjan Ramesh Rao, Vikas Raunak, Juan Diego
Rodriguez,
Sashank
Santhanam,
João
Sedoc,
Thibault Sellam, Samira Shaikh, Anastasia Shimo-
rina, Marco Antonio Sobrevilla Cabezudo, Hendrik
Strobelt, Nishant Subramani, Wei Xu, Diyi Yang,
Akhila Yerukola, and Jiawei Zhou. 2021.
The
GEM benchmark:
Natural language generation,
its evaluation and metrics. In Proceedings of the
1st Workshop on Natural Language Generation,
Evaluation, and Metrics (GEM 2021), pages 96–120,
Online. Association for Computational Linguistics.
Injy Hamed, Amir Hussein, Oumnia Chellah, Shammur
Chowdhury, Hamdy Mubarak, Sunayana Sitaram,
Nizar Habash, and Ahmed Ali. 2023. Benchmark-
ing evaluation metrics for code-switching automatic
speech recognition. In 2022 IEEE Spoken Language
Technology Workshop (SLT), pages 999–1005.
Momchil
Hardalov,
Todor
Mihaylov,
Dimitrina
Zlatkova, Yoan Dinkov, Ivan Koychev, and Preslav
Nakov. 2020. EXAMS: A multi-subject high school
examinations dataset for cross-lingual and multilin-
gual question answering. In Proceedings of the 2020
Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), pages 5427–5444, On-
line. Association for Computational Linguistics.
Md Arid Hasan,
Maram Hasanain,
Fatema Ah-
mad, Sahinur Rahman Laskar, Sunaya Upadhyay,
Vrunda N Sukhadia, Mucahid Kutlu, Shammur Ab-
sar Chowdhury, and Firoj Alam. 2024. NativQA:
Multilingual culturally-aligned natural query for llms.
arXiv e-prints, pages arXiv–2407.
Sabit Hassan, Hamdy Mubarak, Ahmed Abdelali, and
Kareem Darwish. 2021. ASAD: Arabic social me-
dia analytics and unDerstanding. In Proceedings of
the 16th Conference of the European Chapter of the
Association for Computational Linguistics: System
Demonstrations, pages 113–118, Online. Association
for Computational Linguistics.
Junjie Hu, Sebastian Ruder, Aditya Siddhant, Gra-
ham Neubig, Orhan Firat, and Melvin Johnson.
2020. XTREME: A massively multilingual multi-
task benchmark for evaluating cross-lingual gener-
alisation. In International Conference on Machine
Learning, pages 4411–4421. PMLR.
Huang Huang, Fei Yu, Jianqing Zhu, Xuening Sun,
Hao Cheng, Song Dingjie, Zhihong Chen, Mosen
Alharthi, Bang An, Juncai He, et al. 2024. AceGPT,
localizing large language models in arabic. In Pro-
ceedings of the 2024 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume
1: Long Papers), pages 8132–8156.
Go Inoue, Bashar Alhafni, Nurpeiis Baimukan, Houda
Bouamor, and Nizar Habash. 2021. The interplay
of variant, size, and task type in Arabic pre-trained
language models. In Proceedings of the Sixth Ara-
bic Natural Language Processing Workshop, Kyiv,
Ukraine (Online). Association for Computational Lin-
guistics.
Albert Q. Jiang, Alexandre Sablayrolles, Arthur Men-
sch, Chris Bamford, Devendra Singh Chaplot, Diego
de las Casas, Florian Bressand, Gianna Lengyel, Guil-
laume Lample, Lucile Saulnier, Lélio Renard Lavaud,
Marie-Anne Lachaux, Pierre Stock, Teven Le Scao,
Thibaut Lavril, Thomas Wang, Timothée Lacroix,
and William El Sayed. 2023. Mistral 7b. Preprint,
arXiv:2310.06825.
Md
Tawkat
Islam
Khondaker,
Abdul
Waheed,
El Moatez Billah Nagoudi, and Muhammad Abdul-
Mageed. 2023. GPTAraEval: A comprehensive eval-
uation of ChatGPT on Arabic NLP. In Proceedings
of the 2023 Conference on Empirical Methods in
Natural Language Processing, pages 220–247, Sin-
gapore. Association for Computational Linguistics.
Mohamed Bayan Kmainasi, Rakif Khan, Ali Ezzat
Shahroor, Boushra Bendou, Maram Hasanain, and
Firoj Alam. 2025. Native vs non-native language

--- Page 13 ---

prompting: A comparative analysis. In Web Infor-
mation Systems Engineering – WISE 2024, pages
406–420, Singapore. Springer Nature Singapore.
Fajri Koto, Haonan Li, Sara Shatnawi, Jad Doughman,
Abdelrahman Sadallah, Aisha Alraeesi, Khalid Al-
mubarak, Zaid Alyafeai, Neha Sengupta, Shady She-
hata, Nizar Habash, Preslav Nakov, and Timothy
Baldwin. 2024. ArabicMMLU: Assessing massive
multitask language understanding in Arabic. In Find-
ings of the Association for Computational Linguistics
ACL 2024, pages 5622–5640, Bangkok, Thailand
and virtual meeting. Association for Computational
Linguistics.
Mateusz Krubi´nski, Hashem Sellat, Shadi Saleh, Adam
Pospíšil, Petr Zemánek, and Pavel Pecina. 2023.
Multi-parallel corpus of North Levantine Arabic. In
Proceedings of ArabicNLP 2023, pages 411–417, Sin-
gapore (Hybrid). Association for Computational Lin-
guistics.
Viet Lai, Chien Nguyen, Nghia Ngo, Thuât Nguy˜ên,
Franck Dernoncourt, Ryan Rossi, and Thien Nguyen.
2023. Okapi: Instruction-tuned large language mod-
els in multiple languages with reinforcement learning
from human feedback. In Proceedings of the 2023
Conference on Empirical Methods in Natural Lan-
guage Processing: System Demonstrations, pages
318–327.
Hector J Levesque, Ernest Davis, and Leora Morgen-
stern. 2012. The winograd schema challenge. In
Proceedings of the Thirteenth International Confer-
ence on Principles of Knowledge Representation and
Reasoning, pages 552–561.
Patrick Lewis, Barlas Oguz, Ruty Rinott, Sebastian
Riedel, and Holger Schwenk. 2020. MLQA: Evalu-
ating cross-lingual extractive question answering. In
Proceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 7315–
7330, Online. Association for Computational Lin-
guistics.
Yaobo Liang, Nan Duan, Yeyun Gong, Ning Wu, Fenfei
Guo, Weizhen Qi, Ming Gong, Linjun Shou, Daxin
Jiang, Guihong Cao, Xiaodong Fan, Ruofei Zhang,
Rahul Agrawal, Edward Cui, Sining Wei, Taroon
Bharti, Ying Qiao, Jiun-Hung Chen, Winnie Wu,
Shuguang Liu, Fan Yang, Daniel Campos, Rangan
Majumder, and Ming Zhou. 2020. XGLUE: A new
benchmark dataset for cross-lingual pre-training, un-
derstanding and generation. In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 6008–6018,
Online. Association for Computational Linguistics.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
TruthfulQA: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252, Dublin,
Ireland. Association for Computational Linguistics.
Chen Liu, Fajri Koto, Timothy Baldwin, and Iryna
Gurevych. 2024. Are multilingual LLMs culturally-
diverse reasoners? an investigation into multicultural
proverbs and sayings. In Proceedings of the 2024
Conference of the North American Chapter of the
Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers),
pages 2016–2039, Mexico City, Mexico. Association
for Computational Linguistics.
Lin Long, Rui Wang, Ruixuan Xiao, Junbo Zhao, Xiao
Ding, Gang Chen, and Haobo Wang. 2024.
On
LLMs-driven synthetic data generation, curation, and
evaluation: A survey. In Findings of the Associa-
tion for Computational Linguistics: ACL 2024, pages
11065–11082, Bangkok, Thailand. Association for
Computational Linguistics.
Karima Meftouh, Salima Harrat, Salma Jamoussi,
Mourad Abbas, and Kamel Smaili. 2015. Machine
Translation Experiments on PADIC: A Parallel Ara-
bic DIalect Corpus. In The 29th Pacific Asia Con-
ference on Language, Information and Computation,
shanghai, China.
Todor Mihaylov, Peter Clark, Tushar Khot, and Ashish
Sabharwal. 2018. Can a suit of armor conduct elec-
tricity? a new dataset for open book question an-
swering. In Proceedings of the 2018 Conference on
Empirical Methods in Natural Language Processing,
pages 2381–2391, Brussels, Belgium. Association
for Computational Linguistics.
Hussein Mozannar, Elie Maamary, Karl El Hajal, and
Hazem Hajj. 2019. Neural Arabic question answer-
ing. In Proceedings of the Fourth Arabic Natural
Language Processing Workshop, pages 108–118, Flo-
rence, Italy. Association for Computational Linguis-
tics.
Hamdy Mubarak. 2018. Dial2msa: A tweets corpus for
converting dialectal arabic to modern standard arabic.
In OSACT 3: The 3rd Workshop on Open-Source
Arabic Corpora and Processing Tools, page 49.
Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin,
Rifki Afina Putri, Dimosthenis Antypas, Hsuvas
Borkakoty, Eunsu Kim, Carla Perez-Almendros,
Abinew Ali Ayele, et al. 2024. BLEnD: A benchmark
for llms on everyday knowledge in diverse cultures
and languages. arXiv preprint arXiv:2406.09948.
El Moatez Billah Nagoudi, AbdelRahim Elmadany, and
Muhammad Abdul-Mageed. 2022. AraT5: Text-to-
text transformers for Arabic language generation. In
Proceedings of the 60th Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 628–647, Dublin, Ireland. Asso-
ciation for Computational Linguistics.
El Moatez Billah Nagoudi, AbdelRahim Elmadany,
Ahmed El-Shangiti, and Muhammad Abdul-Mageed.
2023. Dolphin: A challenging and diverse bench-
mark for Arabic NLG. In Findings of the Associa-
tion for Computational Linguistics: EMNLP 2023,
pages 1404–1422, Singapore. Association for Com-
putational Linguistics.
Tarek Naous, Zahraa Bassyouni, Bassel Moussi, Hazem
Hajj, Wassim El Hajj, and Khaled Shaban. 2022.
Open-domain response generation in low-resource
settings using self-supervised pre-training of warm-
started transformers. ACM Transactions on Asian

--- Page 14 ---

and Low-Resource Language Information Process-
ing.
Tarek Naous, Michael Ryan, Alan Ritter, and Wei Xu.
2024. Having beer after prayer? measuring cultural
bias in large language models. In Proceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
16366–16393, Bangkok, Thailand. Association for
Computational Linguistics.
OpenAI. 2023. GPT-4 technical report. Technical re-
port, OpenAI.
Matt Post. 2018. A call for clarity in reporting BLEU
scores. In Proceedings of the Third Conference on
Machine Translation: Research Papers, pages 186–
191, Belgium, Brussels. Association for Computa-
tional Linguistics.
Sebastian Ruder, Noah Constant, Jan Botha, Aditya Sid-
dhant, Orhan Firat, Jinlan Fu, Pengfei Liu, Junjie
Hu, Dan Garrette, Graham Neubig, and Melvin John-
son. 2021. XTREME-R: Towards more challenging
and nuanced multilingual evaluation. In Proceedings
of the 2021 Conference on Empirical Methods in
Natural Language Processing, pages 10215–10245,
Online and Punta Cana, Dominican Republic. Asso-
ciation for Computational Linguistics.
Hassan Sajjad, Ahmed Abdelali, Nadir Durrani, and
Fahim Dalvi. 2020.
AraBench:
Benchmarking
dialectal Arabic-English machine translation.
In
Proceedings of the 28th International Conference
on Computational Linguistics, pages 5094–5107,
Barcelona, Spain (Online). International Committee
on Computational Linguistics.
Hassan Sajjad, Fahim Dalvi, Nadir Durrani, Ahmed Ab-
delali, Yonatan Belinkov, and Stephan Vogel. 2017.
Challenging language-dependent segmentation for
Arabic: An application to machine translation and
part-of-speech tagging. In Proceedings of the 55th
Annual Meeting of the Association for Computational
Linguistics (Volume 2: Short Papers), pages 601–607,
Vancouver, Canada. Association for Computational
Linguistics.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavat-
ula, and Yejin Choi. 2021. Winogrande: An adver-
sarial winograd schema challenge at scale. Commu-
nications of the ACM, 64(9):99–106.
Neha Sengupta, Sunil Kumar Sahu, Bokang Jia,
Satheesh
Katipomu,
Haonan
Li,
Fajri
Koto,
Osama Mohammed Afzal, Samta Kamboj, Onkar
Pandit, Rahul Pal, et al. 2023. Jais and jais-chat:
Arabic-centric foundation and instruction-tuned open
generative large language models. arXiv preprint
arXiv:2308.16149.
Siqi Shen, Lajanugen Logeswaran, Moontae Lee,
Honglak Lee, Soujanya Poria, and Rada Mihalcea.
2024. Understanding the capabilities and limitations
of large language models for cultural commonsense.
In Proceedings of the 2024 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies
(Volume 1: Long Papers), pages 5668–5680, Mexico
City, Mexico. Association for Computational Lin-
guistics.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, Johan Ferret, Peter
Liu, Pouya Tafti, Abe Friesen, Michelle Casbon,
Sabela Ramos, Ravin Kumar, Charline Le Lan,
Sammy Jerome, Anton Tsitsulin, Nino Vieillard,
Piotr Stanczyk, Sertan Girgin, Nikola Momchev,
Matt Hoffman, Shantanu Thakoor, Jean-Bastien Grill,
Behnam Neyshabur, Olivier Bachem, Alanna Wal-
ton, Aliaksei Severyn, Alicia Parrish, Aliya Ah-
mad, Allen Hutchison, Alvin Abdagic, Amanda
Carl, Amy Shen, Andy Brock, Andy Coenen, An-
thony Laforge, Antonia Paterson, Ben Bastian, Bilal
Piot, Bo Wu, Brandon Royal, Charlie Chen, Chintu
Kumar, Chris Perry, Chris Welty, Christopher A.
Choquette-Choo, Danila Sinopalnikov, David Wein-
berger, Dimple Vijaykumar, Dominika Rogozi´nska,
Dustin Herbison, Elisa Bandy, Emma Wang, Eric
Noland, Erica Moreira, Evan Senter, Evgenii Elty-
shev, Francesco Visin, Gabriel Rasskin, Gary Wei,
Glenn Cameron, Gus Martins, Hadi Hashemi, Hanna
Klimczak-Pluci´nska, Harleen Batra, Harsh Dhand,
Ivan Nardini, Jacinda Mein, Jack Zhou, James Svens-
son, Jeff Stanway, Jetha Chan, Jin Peng Zhou, Joana
Carrasqueira, Joana Iljazi, Jocelyn Becker, Joe Fer-
nandez, Joost van Amersfoort, Josh Gordon, Josh
Lipschultz, Josh Newlan, Ju yeong Ji, Kareem Mo-
hamed, Kartikeya Badola, Kat Black, Katie Mil-
lican, Keelin McDonell, Kelvin Nguyen, Kiranbir
Sodhia, Kish Greene, Lars Lowe Sjoesund, Lau-
ren Usui, Laurent Sifre, Lena Heuermann, Leti-
cia Lago, Lilly McNealus, Livio Baldini Soares,
Logan Kilpatrick, Lucas Dixon, Luciano Martins,
Machel Reid, Manvinder Singh, Mark Iverson, Mar-
tin Görner, Mat Velloso, Mateo Wirth, Matt Davi-
dow, Matt Miller, Matthew Rahtz, Matthew Watson,
Meg Risdal, Mehran Kazemi, Michael Moynihan,
Ming Zhang, Minsuk Kahng, Minwoo Park, Mofi
Rahman, Mohit Khatwani, Natalie Dao, Nenshad
Bardoliwalla, Nesh Devanathan, Neta Dumai, Nilay
Chauhan, Oscar Wahltinez, Pankil Botarda, Parker
Barnes, Paul Barham, Paul Michel, Pengchong
Jin, Petko Georgiev, Phil Culliton, Pradeep Kup-
pala, Ramona Comanescu, Ramona Merhej, Reena
Jana, Reza Ardeshir Rokni, Rishabh Agarwal, Ryan
Mullins, Samaneh Saadat, Sara Mc Carthy, Sarah
Cogan, Sarah Perrin, Sébastien M. R. Arnold, Se-
bastian Krause, Shengyang Dai, Shruti Garg, Shruti
Sheth, Sue Ronstrom, Susan Chan, Timothy Jor-
dan, Ting Yu, Tom Eccles, Tom Hennigan, Tomas
Kocisky, Tulsee Doshi, Vihan Jain, Vikas Yadav,
Vilobh Meshram, Vishal Dharmadhikari, Warren
Barkley, Wei Wei, Wenming Ye, Woohyun Han,
Woosuk Kwon, Xiang Xu, Zhe Shen, Zhitao Gong,
Zichuan Wei, Victor Cotruta, Phoebe Kirk, Anand
Rao, Minh Giang, Ludovic Peran, Tris Warkentin,
Eli Collins, Joelle Barral, Zoubin Ghahramani, Raia
Hadsell, D. Sculley, Jeanine Banks, Anca Dragan,
Slav Petrov, Oriol Vinyals, Jeff Dean, Demis Hass-
abis, Koray Kavukcuoglu, Clement Farabet, Elena

--- Page 15 ---

Buchatskaya, Sebastian Borgeaud, Noah Fiedel, Ar-
mand Joulin, Kathleen Kenealy, Robert Dadashi,
and Alek Andreev. 2024.
Gemma 2: Improving
open language models at a practical size. Preprint,
arXiv:2408.00118.
NLLB Team, Marta R. Costa-jussà, James Cross, Onur
Çelebi, Maha Elbayad, Kenneth Heafield, Kevin Hef-
fernan, Elahe Kalbassi, Janice Lam, Daniel Licht,
Jean Maillard, Anna Sun, Skyler Wang, Guillaume
Wenzek, Al Youngblood, Bapi Akula, Loic Bar-
rault, Gabriel Mejia Gonzalez, Prangthip Hansanti,
John Hoffman, Semarley Jarrett, Kaushik Ram
Sadagopan, Dirk Rowe, Shannon Spruit, Chau
Tran, Pierre Andrews, Necip Fazil Ayan, Shruti
Bhosale, Sergey Edunov, Angela Fan, Cynthia
Gao, Vedanuj Goswami, Francisco Guzmán, Philipp
Koehn, Alexandre Mourachko, Christophe Rop-
ers, Safiyyah Saleem, Holger Schwenk, and Jeff
Wang. 2022.
No language left behind:
Scal-
ing human-centered machine translation. Preprint,
arXiv:2207.04672.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. LLaMA: Open and ef-
ficient foundation language models. arXiv preprint
arXiv:2302.13971.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, Guanting Dong, Hao-
ran Wei, Huan Lin, Jialong Tang, Jialin Wang,
Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin
Ma, Jianxin Yang, Jin Xu, Jingren Zhou, Jinze Bai,
Jinzheng He, Junyang Lin, Kai Dang, Keming Lu, Ke-
qin Chen, Kexin Yang, Mei Li, Mingfeng Xue, Na Ni,
Pei Zhang, Peng Wang, Ru Peng, Rui Men, Ruize
Gao, Runji Lin, Shijie Wang, Shuai Bai, Sinan Tan,
Tianhang Zhu, Tianhao Li, Tianyu Liu, Wenbin Ge,
Xiaodong Deng, Xiaohuan Zhou, Xingzhang Ren,
Xinyu Zhang, Xipin Wei, Xuancheng Ren, Xuejing
Liu, Yang Fan, Yang Yao, Yichang Zhang, Yu Wan,
Yunfei Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang,
Zhifang Guo, and Zhihao Fan. 2024. Qwen2 techni-
cal report. Preprint, arXiv:2407.10671.
Ahmet Üstün, Viraat Aryabumi, Zheng-Xin Yong, Wei-
Yin Ko, Daniel D’souza, Gbemileke Onilude, Neel
Bhandari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid,
Freddie Vargus, Phil Blunsom, Shayne Longpre,
Niklas Muennighoff, Marzieh Fadaee, Julia Kreutzer,
and Sara Hooker. 2024. Aya model: An instruction
finetuned open-access multilingual language model.
Preprint, arXiv:2402.07827.

--- Page 16 ---

Appendix
A
Details of the Dataset
A.1
Understanding and Generation
To assess whether LLMs can effectively understand
and communicate in various Arabic dialects, we
focus on tasks such as dialect identification, dialec-
tal generation and machine translation to and from
dialects. These tasks are crucial for evaluating a
model’s ability to comprehend and generate dialec-
tal content. We have selected datasets specifically
designed for these tasks, as illustrated in Figure
1, to validate the models’ proficiency in handling
dialectal information.
• Dialect Identification:
– QADI (Abdelali et al., 2021): A dataset of
540,590 tweets from 2,525 users covering 18
different Arabic dialects from the Middle East
and North Africa.
– ADI:10 Comprising 750 utterances from ADI-
5 and ADI-17 test sets, with 50 utterances
from each of 14 countries in the Middle East
and North Africa, including MSA.
– Arabic Dialects Dataset (ADD) (El-Haj et al.,
2018):
Contains 16,494 sentences across
Egyptian, Levantine, Gulf, and North African
Arabic dialects.
• Dialect Generation: The Dialectal Response
Generation Dataset (Naous et al., 2022) fea-
tures 1,000 utterance-response pairs in Levantine,
Egyptian, and Gulf dialects. We further enhance
this dataset by developing a multiple-choice ques-
tion format, allowing for a more rigorous empiri-
cal evaluation.
• Machine Translation: The MADAR corpus
(Bouamor et al., 2018) is used for machine trans-
lation tasks, providing translations between 25
Arabic city-level dialects and other languages.
A.2
Cognitive Abilities
To further evaluate the cognitive abilities11 of
LLMs in understanding and communicating across
different Arabic dialects, we curated a set of chal-
lenging tasks that assess the models’ knowledge,
reasoning, comprehension, and ability to handle
misinformation. These tasks are designed to test
10https://arabicspeech.org/adi_resources/mgb5
11We use the term cognitive to refer to abilities related to
language understanding (semantics), comprehension, genera-
tion, reasoning, and solving NLP-related tasks.
whether the models can accurately interpret and
generate responses in dialectal Arabic, a critical
skill for real-world applications. The datasets were
translated and post-edited from Modern Standard
Arabic (MSA) and English into Egyptian and Lev-
antine dialects to form a comprehensive benchmark
that captures the linguistic diversity and complex-
ity of Arabic dialects. Notably, the ArabicMMLU
dataset (Koto et al., 2024) is already provided in
MSA, so only dialectal translations were generated
for this dataset. Below, we outline the datasets
used, with further details on our translation and
post-editing process provided in Section 3.
Arabic Massive Multitask Language Under-
standing
We translated ArabicMMLU (Koto
et al., 2024) into Egyptian and Levantine dialects.
It consists of subjects featuring questions written in
MSA, sourced from eight different countries, and
covers diverse disciplines such as history, geogra-
phy, law, civics education, and driving tests across
different education levels. Each question in the
dataset has 2-5 candidate answers, with one correct
option.
Common Sense Reasoning
We also translated
several commonsense reasoning tasks into MSA
and dialects.
• PIQA (Physical Interaction QA) (Bisk et al.,
2020): This dataset is mainly focused on phys-
ical commonsense knowledge about everyday
objects, such as their physical properties, affor-
dances, and how they can be manipulated. It in-
volves reasoning about how objects interact in the
real world, as well as understanding the conse-
quences of certain actions in everyday situations.
The underlying task for this dataset is multiple-
choice question answering—given a question q
and two possible solutions s1 and s2, the task is
to choose the most appropriate solution, of which
exactly one is correct.
• OBQA (Open Book QA) (Mihaylov et al.,
2018): This dataset is developed from 1,326
elementary-level science facts, containing ap-
proximately 6,000 questions. The questions re-
quire multi-step reasoning, the use of additional
common and commonsense knowledge, and deep
text comprehension. Each task consists of a ques-
tion with several answer options.
• Winogrande (Sakaguchi et al., 2021): This
dataset builds on the original Winograd Schema
Challenge (WSC) (Levesque et al., 2012), which
focused on pronoun resolution. The Winogrande

--- Page 17 ---

dataset extends this work, making it larger and
more complex.
Reading Comprehension
• Belebele (Bandarkar et al., 2024): This dataset
consists of 900 unique multiple-choice reading
comprehension questions. Each question is asso-
ciated with one of 488 distinct passages across
122 language variants from around the world. It
also includes MSA and various Arabic dialects
such as Levantine, Gulf, Egyptian, Iraqi, and
Moroccan. We selected MSA, Levantine, and
Egyptian dialects for our study.
• BoolQ (Clark et al., 2019): This dataset consists
of 3,270 naturally occurring yes/no questions
and answers. These examples are designed in
a reading comprehension task setup to increase
their difficulty. Each example includes a triplet:
a question, a passage, and an answer, with the
page title optionally providing additional context.
We translated this dataset into MSA, Egyptian
and Levantine dialects for our study.
Misinformation
For assessing misinformation,
we used TruthfulQA (Lin et al., 2022).
This
dataset is specifically designed to evaluate the ac-
curacy and truthfulness of answers provided by
language models. It includes 817 questions across
28 diverse categories, such as health, law, finance,
and politics. The questions are crafted to address
the potential for incorrect answers stemming from
common misconceptions or false beliefs.
A.3
Cultural Understanding
In this paper, we introduce a novel benchmark
focused on cultural awareness across the Levant,
Egypt, and Gulf regions. This benchmark goes be-
yond language proficiency to assess whether LLMs
can accurately capture the cultural nuances specific
to these regions. The dataset contains 180 ques-
tions covering 9 cultural aspects, including events
(e.g., public holidays), traditions (e.g., food and
clothing), geography, history, literature, and reli-
gion. To our knowledge, this is the first cultural
dataset specifically designed to capture region-wise
cultural understanding. Existing datasets targeted
the Arab culture in general. Table 3 presents exam-
ple dialectal questions across the different countries
within the region of interest in this work.
B
Machine Translation
Machine translation of Arabic is challenging due to
morphological complexity and dialectal variations
English
Arabic
Category
What is the traditional folk
dance in Syria?
éK
YJ
Ê®JË@ éJ
J.ª Ë@ é¯QË@ ù
ë ñ 
?AK
Pñ.
Tradition
What are the festivals cel-
ebrated by the people of
Egypt?
AîD
K. É	®Jj
K. ú
ÎË@ XAJ
«B@ éK
@
?QåÓ ú
	¯ A	JË@
Events
What are the seas that
Lebanon overlooks?
AîD
Ê« É¢JK. ú
ÎÊK
 PAjJ.Ë@ ù
ë ñ 
? 	àA	JJ.Ë
Geography
What sweets do they make
on Eid in Qatar?
ú
	¯ Aî	Eðñ
 ú
ÎË@ HAK
ñÊmÌ'@ ñ	J 
?Q¢¯ ú
	¯ YJ
ªË@
Food
Table 3: Example dialectal cultural questions across
countries.
(Birch et al., 2014; Sajjad et al., 2017). Here we
detail our efforts in training MSA–dialect models.
B.1
Data
We used the dataset listed below to develop the
machine translation system. We provide a brief
description of each dataset.
• Madar (Bouamor et al., 2018): Parallel cor-
pus of 25 Arabic city dialects in the travel
domain. It comprises data in the Levantine,
Egyptian, Moroccan, and Gulf dialects.
• UFAL Parallel Corpus of North Levan-
tine 1.0 (Krubi´nski et al., 2023): Consists
of ∼120K parallel sentences in English,
French, German, Greek, Spanish, MSA from
the OpenSubtitles2018 corpus and manually
translated to the north Levantine dialect.
• LDC: From the LDC catalogue we utilize
the Arabic-Dialect/English Parallel Text 12
(referred to as LDC), and the BOLT Arabic
Discussion Forum Parallel Training Data (re-
ferred to as BOLT).13
• DIA2MSA (Mubarak, 2018): Consists of
tweets written in four Arabic dialects (Egyp-
tian, Gulf, Levantine, and Maghrebi) and their
corresponding MSA translations.
• ArzEn-MultiGenre (Hamed et al., 2023): A
parallel dataset of Egyptian Arabic Songs,
Lyrics, Novels, and TV show subtitles that
were human-translated.
• PADIC (Meftouh et al., 2015): Parallel cor-
pus containing dialectal Arabic texts covering
12https://catalog.ldc.upenn.edu/LDC2012T09
13https://catalog.ldc.upenn.edu/LDC2019T01

--- Page 18 ---

Dataset
EGY
GLF
LEV
MADAR
17,885
25,759
21,853
UFAL
0
0
120,600
LDC
38,154
0
138,010
BOLT
113,394
0
0
Dia2msa
16,355
18,000
18,000
Arzen
24,530
0
0
PADIC
0
0
14,426
Table 4: Statistics for the datasets used for training.
OSACT
SADID
LDC
D2M
S1
9.8
12.7
6.2
11.0
S2
9.8
11.8
6.3
11.7
S3
9.7
11.8
7.0
47.8
S4
5.92
8.42
3.46
4.89
Table 5: SacreBLEU Scores on test sets for our MSA-
to-LEV models: S1 = UFAL, S2 = +LDC, MADAR,
PADIC, D2M, S3 = +LDC, MADAR, PADIC, D2M, S4
= GPT4 zero-shot.
six Arabic cities.
In some cases, the dataset does not contain a
dialectal counterpart. To address this issue, we
translate the data from English to the correspond-
ing dialect using the NLLB (nllb-200-3.3B)14 base
model (Team et al., 2022). The number of paral-
lel sentences included in each dataset is presented
in Table 4. We used dialectal tests in AraBench
(Sajjad et al., 2020) for our evaluation.
B.2
Models
We fine-tuned two robust machine translation mod-
els: AraT5 (Nagoudi et al., 2022) and NLLB (Team
et al., 2022). We experimented with several vari-
ants of these models, with sizes ranging from
600M to 3.3B parameters. AraT5 is an Arabic lan-
guage model based on the T5 (Text-to-Text Trans-
fer Transformer) architecture. The NLLB model is
a state-of-the-art machine translation model devel-
oped by Meta, as part of their initiative to improve
translation quality across a broad spectrum of lan-
guages, including Arabic.
B.3
Machine Translation Results
In our preliminary experiments, we found that the
NLLB 3.3B model outperformed AraT5 and its
smaller variants after fine-tuning with dialectal data
(Table 7). We carried out ablation studies using
14https://huggingface.co/facebook/nllb-200-3.
3B
ARZEN
D2M
LDC
MADAR
S1
1.8
57.3
11.8
17.7
S2
17.3
57.2
12.3
17.6
S3
15.8
55.0
11.2
17.9
S4
1.88
7.53
2.83
6.02
Table 6: SacreBLEU scores on test sets for the selected
MSA-to-EGY models: S1 = MADAR + D2M + LDC,
S2 = MADAR + D2M + LDC + Arzen, S3 = MADAR +
D2M + LDC + Arzen + BOLT, S4 = GPT4 zero-shot.
different data mixtures on the NLLB 3.3B model.
Initially, we shortlisted three systems per dialect
using BLEU scores as our primary criterion (Tables
5, 6).
Nonetheless, basing decisions solely on BLEU
scores presents a risk of over-fitting. We observed
improved performance on specific tests after incor-
porating in-domain training data. Therefore, we
carried out a human evaluation of the selected sys-
tems to select the best model for translation. For
this, we selected a sample of 100 sentences from
different genres, and carried out translations using
the systems. We conducted a human evaluation by
showing the output of three translation systems and
asked the participants to select the “best system(s)”.
The instructions to the annotators were as follows:
1. Find a row that does not yet have an entry
under “best system,” and enter S1, S2, or S3 to
represent the system with the best translation.
2. If two systems have the same quality, you may
enter both under “best system” (e.g., S1/S3).
3. If none of the translations are acceptable, enter
“0”, referred as None.
4. The translations may be in any specific sub-
dialect (Palestinian, Lebanese, Jordanian, or
Syrian).
In Tables 8 and 9, we report our human evalua-
tion results, which show that System S1, which
is NLLB tuned just using UFAL data was best
for translating MSA-to-Levantine and System S2
trained using MADAR, Dial2MSA and LDC data
was better for translating MSA-to-Egyptian transla-
tion. However, in our human evaluation, we found
that humans had more confidence in the MSA-to-
Levantine system than in MSA-to-Egyptian.

--- Page 19 ---

LDC
Madar
UFAL
Oscat
Avg.
NLLB3.3B
3.8
30.4
32.4
11.7
19.6
AraT5
4.3
21.4
33.4
12.2
17.8
Turjuman
4.1
19.3
33.2
11.3
17.0
Table 7: SacreBLEU scores on test sets for models
trained on the UFAL data mixture. Avg.: Average
S1
S2
S3
None
Wikipedia
49.9%
46.0%
45.2%
16.5%
Zaman
52.3%
31.5%
36.1%
20.5%
Hindawi
53.8%
51.7%
51.5%
11.1%
Table 8: Human evaluation of different MSA-to-LEV
systems across datasets. None refers that the output
from none of the systems were acceptable.
C
Detailed Results on Dialect
Understanding and Generation
C.1
Dialect Identification
The results of the dialect identification task are
shown in Table 10.
In Figures 12 and 13 we
present the confusion matrices for the ADI and
ADD datasets, respectively. For ADI, Llama 3,
Mistral, and AceGPT tend to confuse MSA with
the Levantine and Gulf dialects, while Jais per-
forms best in detecting the Egyptian dialect. For
ADD, Llama 3 and Jais excel at detecting the Egyp-
tian dialect, whereas AceGPT confuses all dialects
with MSA. The variation in model performance is
attributed to the nature of the data and its underly-
ing distribution.
C.2
Dialect Generation
The F1 scores of the models considered on the task
of dialect generation (modeled as a selection task)
are shown in Table 11. We conducted qualitative
analysis on the generation task of the models by
prompting them in the dialectal version of “How
would you respond to this phrase in the X dialect”,
where X could be one of the Egyptian, Levantine,
or Gulf dialects (examples on models’ response
can be found in Table 12). We noticed that Llama
3 struggles to follow the dialectal instructions and
replies instead with description of the input phrase
– for example, What a great question!, What a chal-
lenge! thanks for the question!. While mistral
appears to not be able to comprehend the prompt
in the first place. It replies with random phrases
about the input sentence without abiding by the
instruction. On the other hand, Jais tends to copy
S1
S2
S3
None
Wikipedia
19.4%
28.6%
27.6%
46.9%
Zaman
12.1%
18.2%
17.2%
59.6%
Hindawi
29.3%
33.3%
29.3%
35.4%
Table 9: Human evaluation for the selected MSA-to-
EGY models.None refers that the output from none of
the systems were acceptable.
the input phrase without replying to the question.
These results show that models struggle to follow
dialectal instructions.
QADI
ADI
ADD
Random
0.08
0.09
0.12
Llama 3
0.42
0.26
0.40
Mistral
0.21
0.11
0.18
Jais
0.31
0.40
0.58
AceGPT
0.12
0.15
0.32
SOTA
0.85
0.70
0.66
Table 10: Results (measured in F1) for the dialect iden-
tification task.
LEV
EGY
GLF
Random
0.28
0.24
0.48
Llama 3
0.32
0.43
0.63
Mistral
0.28
0.33
0.62
Jais
0.49
0.50
0.74
AceGPT
0.48
0.58
0.74
Table 11: Results (measured in accuracy) for the dialect
generation task.
C.3
MT as Generation
The statistics of test set for the English-to-Dialect
and MSA-to-Dialects splits are shown in Table 13
and 14, respectively. The results are shown in Table
15. For similar experiments on Dialects-to-English,
Dialects-to-MSA and MSA-to-Dialects the results
are shown in Tables 16, 17 and 18, respectively.
D
Detailed Results on Cognitive Abilities
D.1
World Knowledge
The results in 19 The results show the overall Ara-
bic MMLU accuracies. in Figure 14 provide key
insights into the performance of different models
on MSA and dialectal datasets (Egyptian and Lev-
antine). Below we provide some key observations.

--- Page 20 ---

MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.04
0.00
0.00
0.05
0.21
0.18
0.00
0.06
0.12
0.13
0.01
0.11
0.02
0.03
0.00
0.04
0.000
0.025
0.050
0.075
0.100
0.125
0.150
0.175
0.200
(a) Llama 3
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.05
0.04
0.00
0.01
0.39
0.06
0.00
0.01
0.29
0.06
0.00
0.01
0.07
0.01
0.00
0.00
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
(b) Mistral
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.02
0.03
0.02
0.06
0.03
0.04
0.02
0.11
0.03
0.01
0.06
0.10
0.01
0.00
0.00
0.47
0.1
0.2
0.3
0.4
(c) Jais
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.09
0.00
0.00
0.00
0.36
0.00
0.00
0.09
0.28
0.00
0.00
0.08
0.03
0.00
0.00
0.06
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
(d) AceGPT
Figure 12: Confusion matrices on ADI dataset.
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.02
0.01
0.00
0.08
0.06
0.06
0.00
0.08
0.06
0.04
0.00
0.10
0.07
0.08
0.00
0.32
0.05
0.10
0.15
0.20
0.25
0.30
(a) Llama 3
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.04
0.06
0.00
0.01
0.12
0.07
0.00
0.01
0.14
0.06
0.00
0.01
0.36
0.05
0.00
0.07
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35
(b) Mistral
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.02
0.03
0.02
0.06
0.03
0.04
0.02
0.11
0.03
0.01
0.06
0.10
0.01
0.00
0.00
0.47
0.1
0.2
0.3
0.4
(c) Jais
MSA
GLF
LEV
EGY
MSA
GLF
LEV
EGY
0.11
0.00
0.00
0.01
0.18
0.00
0.00
0.02
0.19
0.00
0.00
0.01
0.27
0.00
0.00
0.21
0.00
0.05
0.10
0.15
0.20
0.25
(d) AceGPT
Figure 13: Confusion matrices on the Arabic dialects dataset.
Humanities:
AceGPT leads in all three cate-
gories (MSA, Egyptian, Levantine), slightly outper-
forming Jais, another Arabic-centric model. This
suggests that AceGPT excels in humanities-related
questions across dialects. Llama and Mistral, both
non-Arabic-centric models, lag behind, with a sig-
nificant performance gap between them and the
Arabic-centric models.
STEM:
Jais outperforms AceGPT in MSA, but
the gap narrows in the dialects, particularly in Lev-
antine, where AceGPT demonstrates competitive
performance. Mistral and Llama perform compar-
atively lower in STEM subjects, suggesting they
may not generalize as well in technical disciplines,
especially when dialects are involved.
Social Sciences:
Similar to the humanities,
AceGPT shows consistent superiority over other
models. However, the overall performance drops
slightly in dialects compared to MSA. Mistral lags
behind the other models, particularly in Levantine
dialect, where the gap becomes more pronounced.
Language Tasks:
Language tasks show an inter-
esting pattern where AceGPT and Jais outperform
Llama and Mistral by a wide margin, especially
in Levantine. This is likely due to the language-
specific capabilities of AceGPT and Jais, which
are more attuned to Arabic dialects. Levantine
seems to pose a greater challenge across models,
as the performance declines are slightly more pro-
nounced.
Others (Miscellaneous):
This category reveals
AceGPT’s broad capabilities as it outperforms
other models in both dialects and MSA. Notably,
Jais also performs well, but AceGPT maintains a
lead. Llama’s performance is competitive in MSA
but suffers a sharper decline in dialectal bench-
marks, particularly in Egyptian.
D.2
Reading Comprehension
The Accuracy numbers for BoolQ and Belebele are
shown in tables 20 and 21
D.3
Commonsense Reasoning
The results for PiQA, Openbooks, and Winogrande
are shown in tables 22, 23, and 24
D.4
Misinformation
The results for truthfulQA are shown in table 25
E
Examples on Models’ Cultural
Knowledge
In Section 5.3, we presented results on models’
performance on the task of region-specific cultural

--- Page 21 ---

#
Input
Llama 3
Mistral
Jais
Ex1
ÉAg ú
Í@ éK
@ YÓAg. èXQî 	DË@ Q	®Ó ½ ð
?¼AªÓ
Your face looks really pale today.
What’s going on with you?
What a great question!
½	JºÖß
 , éK
QåÖÏ@ é	ªÊËAK. éÊÒm.Ì'@ úÎ« XXQÊË
: éJ
ËAJË@ éÔg. QË@ Ð@Y 	jJ@
To hesitate over the sentence in
Egyptian, you can use the follow-
ing translation:
ú
ÎË@ éK
@ ?YÓAg.
èXPAî 	DË@ Q	®Ó ½ ð
?¼AªÓ ÉAg
Your face is really pale today.
What’s going on with you?
Ex2
	XAJ@ AK
 ú
	GA¾Ó HYª¯ ½Ê¾ 
It looks like you sat in my seat,
sir.
!? 	XAJ@ AK
 ú
	GA¾Ó HYª¯ ½	KñÊ 
How did you end up sitting in my
seat, sir?!
AK
 ½	KA¾Ó ú
GYª¯ ½Ê¾  HQº  : éK.Ag. @
. éK
QåÖÏ@ é	ªÊËAK. ,Q	«A 
Answer: Thank you, it looks like
you sat in your place, vacant, in
Egyptian Arabic.
	XAJ@ AK
 ú
æ
Q» úÎ« HYª¯ ½Ê¾ 
It looks like you sat in my chair,
sir.
Table 12: Example models’ responses to Egyptian dialect generation with their English translations.
Rand
Llama 3
Mistral
Jais
AceGPT
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Accuracy
(a) Humanities
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Accuracy
(b) Language
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Accuracy
(c) STEM
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Accuracy
(d) Social Science
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
Accuracy
(e) Others
Figure 14: Results on different subject areas in ArabicMMLU.
MSA
LEV
EGY
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
Accuracy
Rand
LLama 3
Mistral
Jais
AceGPT
Jais 30B
Figure 15: Average results on ArabicMMLU
awareness, where we modeled the task as a MCQ
task. Although such setup can provide an overall
performance estimation, deeper understanding of
an LLM behavior capturing fine-grained cultural
differences is essential.
In Table 26 we present examples of the models’
responses to dialectal cultural questions. With a
simple geography question related to one of the
Levant countries (Q1), we observe that Jais and
AceGPT respond with the correct answer, while
Llama 3 partially answer the question providing ad-
ditional irrelevant and incorrect information. Mis-
tral shows a different behavior, hallucinating and
responding with non-existent geographical loca-
tions. Similar trends can be observed with Q2
about one of the traditions of a Gulf country, where
Jais and AceGPT both correctly answer the ques-
tion, and Llama 3 returns an answer that is more
of a description or explanation. Mistral’s response
is particularly worth noting, as not only it gener-
ates fictional information, it generated an answer
describing a dance where men and women are danc-
ing together, although anyone with some awareness
of the country’s tradition would know such dance
does not comply with the culture of Qatar where
segregation between men and women is the norm.

--- Page 22 ---

Test set
# of Sent.
madar-test-glf-0-iq-ar
1,984
madar-test-glf-0-om-ar
1,979
madar-test-glf-0-qa-ar
1,935
madar-test-glf-0-sa-ar
1,974
madar-test-glf-0-ye-ar
1,983
madar-test-glf-1-iq-ar
1,985
madar-test-glf-1-sa-ar
1,975
madar-test-glf-2-iq-ar
1,985
madar-test-lev-0-jo-ar
1,975
madar-test-lev-0-lb-ar
1,966
madar-test-lev-0-pa-ar
1,972
madar-test-lev-0-sy-ar
1,968
madar-test-lev-1-jo-ar
2,008
madar-test-lev-1-sy-ar
1,978
madar-test-nil-0-eg-ar
1,965
madar-test-nil-0-sd-ar
1,981
madar-test-nil-1-eg-ar
1,982
madar-test-nil-2-eg-ar
1,976
madar-test-msa-0-ms-ar
1,979
Total
37,550
Table 13: Number of sentences for the English and
Dialect splits from the MADAR test set.
F
Detailed PEMT Guideline
The purpose of PEMT (Brockmann et al., 2022)
is to refine and improve the output generated by
MT systems to ensure accuracy, fluency (i.e. they
reflect the nuances of how the dialect is spoken),
adequacy (i.e. they maintain the semantic meaning
of the input sentence), and cultural appropriate-
ness. For the PEMT task, the goal was to post-edit
datasets translated into MSA and the dialects: Lev-
antine and Egyptian. Below we provide detailed
instructions for PEMT. Unless stated, all examples
are to illustrate a specific instruction and might not
reflect datasets or dialect.
F.1
General instructions for PEMT:
Instruction 1: When necessary, the text should be
rewritten to adhere to the syntactic and semantic
structure of Arabic. Some questions or options may
need to be paraphrased to ensure the fluency. To
achieve this, the edits may include:
• Paraphrasing questions or options.
• Editing or adding any parts-of-speech needed to
improve the readability of the sentence, such as
adding words ( 	­¢ªË@
	¬ðQk) or prepositions (Qm.Ì'@
	¬ðQk)
or adding the definite article ( 	­K
QªJË@ È@).
Test set
# of Sent.
madar-test-glf-0-iq
1,973
madar-test-glf-0-om
1,971
madar-test-glf-0-qa
1,927
madar-test-glf-0-sa
1,965
madar-test-glf-0-ye
1,973
madar-test-glf-1-iq
1,973
madar-test-glf-1-sa
1,965
madar-test-glf-2-iq
1,973
madar-test-lev-0-jo
1,966
madar-test-lev-0-lb
1,954
madar-test-lev-0-pa
1,963
madar-test-lev-0-sy
1,960
madar-test-lev-1-jo
1,997
madar-test-lev-1-sy
1,968
madar-test-nil-0-eg
1,955
madar-test-nil-0-sd
1,970
madar-test-nil-1-eg
1,971
madar-test-nil-2-eg
1,965
Total
35,389
Table 14: Number of sentences for the MSA and Dialect
splits from the MADAR test set.
• For MSA, it is also important to correct the
wrong use of Hamzah (Hamzatul-wasl and
Hamzatul-Qata’a).
• Fixing the use of inappropriate verbs that do not
align between sentences and the options asso-
ciated with them in terms of their grammatical
gender and singularity or plurality.
• Correcting wrong translation of words and
phrases, or adding missing information that were
not transferred from the source sentence to the
translation.
In Table 27, we provide some examples to illus-
trate the above points.
Instruction 2: For abbreviations, if they have a
translation for them in Arabic that is common and
well known, the Arabic translation for them should
be used. If the translation of the abbreviation is not
known in Arabic, the abbreviation in English letters
should be used. Examples are shown in Table 28.
Instruction 3: Samples might reference names,
such as those of people, places, organizations, crea-
tures, movies, TV series, books, songs, and model
of products. These parts should be transliterated
into Arabic. This means writing the English word
as it is into Arabic script. However, this does not
apply to names that have an equivalent translation
in Arabic. For instance, the example sentences in
Table 29.

--- Page 23 ---

Dataset
NLLB-600M
NLLB-1.3B
NLLB-3.3B
Llama 3
Mistral
Jais
AceGPT
madar-en-to-glf-iq-0
7.49
9.11
9.17
1.61
0.30
0.66
1.00
madar-en-to-glf-iq-1
6.40
8.14
8.67
1.45
0.32
0.56
0.82
madar-en-to-glf-iq-2
5.11
6.54
6.58
0.89
0.25
0.28
0.80
madar-en-to-glf-om-0
15.91
16.15
16.01
5.66
1.28
2.27
3.42
madar-en-to-glf-qa-0
9.86
11.74
14.11
2.25
0.47
1.09
1.38
madar-en-to-glf-sa-0
14.90
19.73
22.60
3.68
0.95
1.48
2.21
madar-en-to-glf-sa-1
8.56
11.25
13.38
2.16
0.40
0.82
1.15
madar-en-to-glf-ye-0
7.60
9.40
10.14
1.74
0.30
0.65
1.09
smadar-en-to-lev-jo-0
10.65
15.46
19.41
1.84
0.24
0.90
2.06
madar-en-to-lev-jo-1
10.88
15.21
20.17
1.60
0.24
0.96
1.80
madar-en-to-lev-lb-0
5.19
7.59
8.59
0.82
0.18
0.49
1.19
madar-en-to-lev-pa-0
10.19
14.43
17.92
1.71
0.29
1.12
1.87
madar-en-to-lev-sy-0
9.03
13.43
15.29
1.30
0.22
0.98
2.76
madar-en-to-lev-sy-1
7.64
11.34
12.96
1.37
0.24
0.95
3.12
madar-en-to-nil-eg-0
8.82
15.86
17.78
1.81
0.34
1.25
3.73
madar-en-to-nil-eg-1
8.34
15.48
16.26
1.71
0.25
1.01
3.72
madar-en-to-nil-eg-2
8.53
16.52
17.45
1.33
0.29
1.14
3.28
madar-en-to-nil-sd-0
11.12
11.86
12.16
3.16
0.56
1.39
4.48
Table 15: Results (measured in SacreBLEU) for the English to Dialect systems.
Dataset
NLLB-600M
NLLB-1.3B
NLLB-3.3B
Llama 3
Mistral
Jais
AceGPT
madar-glf-to-en-iq-0
37.54
43.79
45.63
25.46
13.66
34.87
36.28
madar-glf-to-en-iq-1
38.20
44.97
46.15
23.31
13.51
33.91
35.62
madar-glf-to-en-iq-2
40.54
48.17
49.15
21.47
12.44
34.14
36.35
madar-glf-to-en-om-0
44.87
49.62
48.77
33.07
19.66
41.43
43.33
madar-glf-to-en-qa-0
36.58
42.70
43.80
24.16
13.53
34.86
35.82
madar-glf-to-en-sa-0
47.33
52.68
52.70
32.37
21.79
40.99
44.34
madar-glf-to-en-sa-1
36.61
42.89
44.73
23.42
12.03
32.62
33.93
madar-glf-to-en-ye-0
39.41
47.08
47.97
22.32
13.70
36.30
36.81
madar-lev-to-en-jo-0
41.37
47.72
48.57
25.02
13.90
38.87
37.64
madar-lev-to-en-jo-1
41.75
47.57
49.96
24.86
13.52
36.89
38.03
madar-lev-to-en-lb-0
36.56
43.62
45.16
17.08
8.84
30.25
27.66
madar-lev-to-en-pa-0
39.74
45.84
47.49
24.21
12.52
37.62
37.27
madar-lev-to-en-sy-0
39.68
46.00
47.29
23.69
11.99
36.84
35.68
madar-nil-to-en-eg-0
37.83
44.17
46.73
24.08
12.26
36.84
35.68
madar-nil-to-en-eg-1
46.50
53.31
55.08
28.92
14.40
43.50
43.03
madar-nil-to-en-eg-2
37.72
44.52
46.89
23.14
11.18
35.64
36.20
madar-nil-to-en-sd-0
46.32
52.54
52.00
31.43
17.74
44.78
44.34
Table 16: Results (measured in SacreBLEU) for the Dialects to English systems.
F.2
Datasets, Task Format, and Specific
Instructions for Each Dataset:
F.2.1
ArabicMMLU
Data format: ArabicMMLU dataset is originally
in Arabic (MSA), therefore, MT and PEMT were
only done for Levantine and Egyptian. The transla-
tor’s task consisted of editing: (i) one question and
(ii) four options that serve as possible answers for
that question.
Specific Instruction:
• It is important to consider the structure of the
question, which needs to be maintained. Be-
low are some examples that illustrates differ-
ent types of questions. To ensure the fluency
of the questions, they might need paraphras-
ing.
• Not all parts of the questions and the options
should be expressed in dialect.
Changing
those parts or expressing them in dialect will
affect the meaning of the question. These
parts include (i) Verses from Quran, or lines
from Hadith, (ii) Words or the phrases that the
question is asking the meaning of, (iii) Words/
phrases that refer to scientific domains, (iv)
Technical words or phrases, (v) Lines from
poems, (vi) Equations (chemistry or mathe-
matical). While editing, avoid changing these
parts, and only edit the other parts that should
be expressed in dialect and will not change the
semantic meaning of the question. However,
edits can be made to address any missing parts
or grammatical errors that the question might
have.
• Blanks should be represented as it appears
in the MSA (source). If it is represented as

--- Page 24 ---

Dataset
NLLB-600M
NLLB-1.3B
NLLB-3.3B
Llama
Mistral
Jais
AceGPT
madar-dia-to-msa-glf-iq-0
22.30
26.84
63.65
4.11
0.14
6.45
3.97
madar-dia-to-msa-glf-iq-1
21.58
26.43
63.50
3.93
0.14
6.19
2.85
madar-dia-to-msa-glf-iq-2
22.15
27.70
65.47
3.92
0.07
6.55
2.92
madar-dia-to-msa-glf-om-0
24.92
28.36
60.52
6.80
0.23
8.97
5.20
madar-dia-to-msa-glf-qa-0
22.25
26.14
57.91
3.94
0.10
6.34
3.29
madar-dia-to-msa-glf-sa-0
26.77
30.70
70.00
5.43
0.23
7.80
4.81
madar-dia-to-msa-glf-sa-1
21.47
25.49
61.74
3.63
0.07
5.53
2.61
madar-dia-to-msa-glf-ye-0
23.05
28.33
65.12
3.88
0.20
6.91
3.18
madar-dia-to-msa-lev-jo-0
23.82
28.74
65.96
4.68
0.11
6.32
3.72
madar-dia-to-msa-lev-jo-1
24.36
29.36
66.90
4.57
0.09
5.94
3.82
madar-dia-to-msa-lev-lb-0
21.44
26.73
61.69
2.94
0.05
5.28
2.34
madar-dia-to-msa-lev-pa-0
23.60
28.61
62.28
4.04
0.13
6.24
3.64
madar-dia-to-msa-lev-sy-0
24.17
28.85
61.60
4.64
0.10
6.95
3.19
madar-dia-to-msa-lev-sy-1
23.25
28.17
62.43
3.33
0.08
6.29
2.50
madar-dia-to-msa-nil-eg-0
23.46
27.81
58.23
4.80
0.12
6.53
3.25
madar-dia-to-msa-nil-eg-1
25.67
31.14
67.36
4.82
0.16
6.86
3.05
madar-dia-to-msa-nil-eg-2
23.12
27.78
59.51
3.94
0.05
6.09
3.14
madar-dia-to-msa-nil-sd-0
23.74
28.46
57.99
4.78
0.14
7.35
3.80
Table 17: Results (measured in SacreBLEU) for the Dialects to MSA systems.
task
NLLB-600M
NLLB-1.3B
NLLB-3.3B
Llama 3
Mistral
Jais
AceGPT
madar-msa-to-dia-glf-iq-0
7.74
10.83
11.70
1.46
0.42
1.17
2.10
madar-msa-to-dia-glf-iq-1
7.46
11.15
11.39
1.23
0.29
0.75
1.60
madar-msa-to-dia-glf-iq-2
5.38
7.25
8.07
0.77
0.31
0.52
1.28
madar-msa-to-dia-glf-om-0
13.03
12.82
14.57
4.59
1.85
3.91
7.43
madar-msa-to-dia-glf-qa-0
12.51
15.51
17.02
2.41
0.77
1.70
3.10
madar-msa-to-dia-glf-sa-0
18.21
22.27
27.61
3.28
0.85
2.38
4.86
madar-msa-to-dia-glf-sa-1
11.07
15.30
17.10
2.14
0.51
1.16
2.43
madar-msa-to-dia-glf-ye-0
9.57
11.73
13.11
1.42
0.53
1.11
2.13
madar-msa-to-dia-lev-jo-0
12.38
16.51
22.79
1.33
0.27
1.71
3.79
madar-msa-to-dia-lev-jo-1
13.13
16.89
23.02
1.33
0.31
1.25
3.23
madar-msa-to-dia-lev-lb-0
6.70
9.69
10.37
0.63
0.22
0.74
1.67
madar-msa-to-dia-lev-pa-0
12.75
16.35
20.24
1.54
0.44
1.69
3.31
madar-msa-to-dia-lev-sy-0
10.85
14.55
17.62
1.43
0.26
1.37
3.37
madar-msa-to-dia-lev-sy-1
9.08
12.20
15.40
1.23
0.24
1.03
2.63
madar-msa-to-dia-nil-eg-0
11.58
16.69
21.33
1.48
0.23
2.15
4.13
madar-msa-to-dia-nil-eg-1
9.99
14.66
17.96
1.32
0.17
1.87
3.26
madar-msa-to-dia-nil-eg-2
10.92
15.41
19.75
1.08
0.32
1.86
3.50
madar-msa-to-dia-nil-sd-0
9.91
12.47
11.67
1.94
0.51
2.68
4.11
Table 18: Results (measured in SacreBLEU) for the MSA to dialectal systems.
MSA
LEV
EGY
Rand
0.26
0.20
0.20
LLama 3
0.49
0.44
0.44
Mistral
0.40
0.34
0.35
Jais
0.56
0.52
0.51
Ace-GPT
0.57
0.51
0.52
Table 19: Results on ArabicMMLU.
dots, then they should remain the same. If it
is represented as [ 	¨@Q	¯], then add it as such.
Below are a few examples from different disci-
plines and specific instructions for scenarios. We
show the questions and answers (options). We pro-
vide the source (MSA), MT, and PEMT Levantine
for illustration purposes. However, for Egyptian,
MSA
LEV
EGY
ENG
Random
0.38
0.38
0.38
0.38
LLama 3
0.74
0.71
0.73
0.85
Mistral
0.66
0.63
0.63
0.85
Jais
0.71
0.65
0.64
0.75
AceGPT
0.77
0.68
0.69
0.82
Table 20: Results on BoolQ.
the instructions are the same for the dialectal trans-
lation. For each example, we provide an explana-
tion highlighting the reason for the edits.
1. Islamic Studies
Question (MSA):
((3) AjJ. H@Q
	ªÖÏA	¯ ) : HAK
XAªË@ èPñ ú
	¯ úÍAªK ÈA¯

--- Page 25 ---

MSA
LEV
EGY
ENG
Random
0.26
0.26
0.26
0.23
Llama 3
0.49
0.42
0.39
0.87
Mistral
0.41
0.36
0.35
0.75
Jais
0.57
0.49
0.49
0.80
AceGPT
0.49
0.43
0.42
0.83
Table 21: Results on Belebele.
MSA
LEV
EGY
ENG
Random
0.48
0.49
0.49
0.50
Llama 3
0.55
0.54
0.55
0.78
Mistral
0.55
0.52
0.54
0.81
Jais
0.66
0.59
0.62
0.77
AceGPT
0.64
0.57
0.61
0.80
Table 22: Results on PIQA.
MSA
LEV
EGY
ENG
Random
0.28
0.26
0.31
0.27
Llama 3
0.32
0.33
0.32
0.42
Mistral
0.31
0.30
0.30
0.45
Jais
0.35
0.34
0.32
0.41
AceGPT
0.36
0.34
0.32
0.45
Table 23: Results on OBQA.
MSA
LEV
EGY
Random
0.51
0.51
0.49
Llama 3
0.60
0.52
0.56
Mistral
0.57
0.51
0.55
Jais
0.65
0.58
0.61
AceGPT
0.61
0.58
0.63
Table 24: Results on Winogrande.
MSA
LEV
EGY
ENG
Random
0.21
0.23
0.20
0.39
Llama 3
0.34
0.29
0.33
0.40
Mistral
0.33
0.33
0.30
0.57
Jais
0.28
0.28
0.31
0.28
AceGPT
0.34
0.30
0.33
0.37
Table 25: Results on TruthfulQA.
? H@Q
	ªÖÏAK. Xñ®ÖÏ@AÓ
Options (MSA):
èYK
Y Ë@ hAK
QË@
1.
ÉK.B@
2.
	á
m'.AË@ éºKCÖÏ@
3.
ÉJ
	mÌ'@
4.
Question (PEMT -Levantine):
ñ  ((3) AjJ. H@Q
	ªÖÏA	¯ ) : HAK
XAªË@ èPñ ú
	¯ úÍAªK ÈA¯
? H@Q
	ªÖÏ@ ú
 	æªK
Options (PEMT -Levantine):
ø
 ñ®Ë@ @ñêË@
1.
ÉK.B@
2.
	á
m'.AË@ éºKCÖÏ@
3.
ÉJ
	mÌ'@
4.
Explanation: Verses from Qur’an should not
be modified. Any changes to such elements will
alter the meaning of the question. However, in this
case, the options can be expressed differently in the
dialect.
2. Accounting
Question (MSA):
HAÓñÊªÖÏ@ éÓCð ém 	áÓ ®jJË@ úÍ@
	¬YîE
 ú
æ.Am× ¨Q	¯
HAÓñÊªÖÏ@ è 	Yë úÎ« é®JË@ 	áÓ @ YK
 	QÓ ù	® 	
 AÖß. éJ
ËAÖÏ@
Options (MSA):
éJ
ÓñºmÌ'@ éJ.AjÖÏ@
1.
éJ
ËðYË@ éJ.AjÖÏ@
2.
éªk. @QÖÏ@
3.
éJ
«AÒJk. B@ éJ.AjÖÏ@
4.
Question (PEMT -Levantine):
éÓCð
ém
	áÓ
	áÓ
®jJÊË
	¬YîD
K. ú
æ.Am× ¨Q	¯
HAÓñÊªÖÏ@ ø
 YJ
ë 	áÓ é®JË@ YK
 	QK. ú
ÍAJËAK.ð éJ
ËAÖÏ@ HAÓñÊªÖÏ@
Options (PEMT -Levantine):éJ
ÓñºmÌ'@ éJ.AjÖÏ@
1.
éJ
ËðYË@ éJ.AjÖÏ@
2.
éªk. @QÖÏ@
3.
éJ
«AÒJk. B@ éJ.AjÖÏ@
4.
Explanation: The names of knowledge domains
and sub fields (the options) should remain the same.

--- Page 26 ---

#
Question
Gold Answer
Llama 3
Mistral
Jais
AceGPT
Q1
ú
ÎK
 PAjJ.Ë@ ù
ë ñ 
? 	àXPB@ AîD
Ê« É¢JK.
What
are
the
seas that Jordan
overlooks?
,QÔgB@
QjJ.Ë@
IJ
ÖÏ@ QjJ.Ë@
The Red Sea,
the Dead Sea
AîD
Ê« É¢JK. ú
æË@ PAjJ.Ë@
IJ
ÖÏ@ QjJ.Ë@ ù
ë 	àXPB@
".ú
G.QªË@ i. J
Ê	mÌ'@ð 	áÒJ
Ë@ð
The seas that Jordan
overlooks are the
Dead Sea, Yemen
and
the
Arabian
Gulf.
The Red Sea
,QÔgB@
QjJ.Ë@
éêk. ð
,XYªË@ Qm'.ð éJ
	K@YK
ñË@
". éK
QåÖÏ@
The Red Sea: The
Swedish
desti-
nation
and
the
Egyptian
Sea
of
Numbers.
QjJ.Ë@
,QÔgB@
QjJ.Ë@
" IJ
ÖÏ@
The Red Sea, the
Dead Sea
QjJ.Ë@
, IJ
ÖÏ@
QjJ.Ë@
".QÔgB@
The Dead Sea, the
Red Sea
Q2
éJ
J.ª Ë@ é¯QË@ ñ	J 
?Q¢¯ ú
	¯ éK
YJ
Ê®JË@
What is the tradi-
tional folk dance
in Qatar?
é 	QªË@
Ardah
éK
YJ
Ê®JË@ éJ
J.ª Ë@ é¯QË@
é¯QË@
ù
ë
Q¢¯
ú
	¯
". éK
Q¢®Ë@
The traditional folk
dance in Qatar is
the Qatari dance.
¯QË@
ÕæK
 ,Q¢¯
ú
	¯
é	J	¯YËAK. ø
 YJ
Ê®JË@ ú
æ.ª Ë@
, éÊÓA Ë@ é®ÊmÌ'@ð ù¢ñË@
ÈAg. QË@ð ZA	Ë@ é¢@ñK.
. 	á
ªÒm.×
In Qatar, traditional
folk
dancing
is
performed
with
the
central
drum
(dufna) and the cir-
cular dance (halqa
shamelah),
with
both women and
men
participating
together.
é 	QªË@
Ardah
éK
YJ
Ê®JË@ éJ
J.ª Ë@ é¯QË@
". é 	QªË@ ù
ë Q¢¯ ú
	¯
The traditional folk
dance in Qatar is
the Ardah.
Table 26: Example models’ responses to dialectal cultural questions with their English translations.
English
MT (MSA)
PEMT (MSA)
People in the US
have longer paid va-
cations than people
in which Western
countries?
HAK
BñË@
ú
	¯
A	JË@
H@	PAg. @ ÑîE
YË èYjJÖÏ@
	áÓ Èñ£@ Qk. B@ é«ñ	¯YÓ
	áK
 	YË@
A	mB@
ÈðYË@
ú
	¯
	àñ 
ªK
? éJ
K.Q	ªË@
ú
	¯ A	mB@ Ém'
 Éë
èYjJÖÏ@
HAK
BñË@
Qk. B@ é«ñ	¯YÓ
H@	PAg. @
A	mB@
	áÓ
Èñ£@
ú
	¯
	àñ 
ªK
	áK
 	YË@
? éJ
K.Q	ªË@ ÈðYË@
Who
objectively
makes
the
best
burgers?
É 		¯@ ©	J
 ø
 	YË@ 	áÓ
?ú
«ñ 	ñÓ É¾ . Q	«Q.Ë@
ø
 	YË@ 	áÓ , 	Q
m' ø
@ 	àðX
?Q	«QK. É 		¯@ YªK
Who famously said,
“I cannot tell a lie”?
èQ
îDË@ éKPAJ.« ÈA¯ 	áÓð
	à@
©J
¢@
B""
?\\H. 	Y»@
:èQ
îDË@ èPAJ.ªË@ ÉKA¯ 	áÓ
? H. 	Y»@ 	à@ ©J
¢@ B@
Table 27: Example sentences in English, MT (MSA),
and post-edited versions to illustrate Instruction 1.
Changes should only be made to correct spelling
mistakes in these words and phrases.
3. Arabic Language
Question (MSA):
: éÒÊ¾Ë@ Q 	k@ ú
	¯ ()	J
Ë@
	¬Qk úÎ« ø
 ñJm' ú
æË@ éÒÊ¾Ë@
English
PEMT (MSA)
What did CERN
do in 2012?
IÊª	¯ @	XAÓ
CERN
?2012 ÐA« ú
	¯
I am an AI and
I don’t know the
answer
ú
«A	J¢@
ZA¿	X
A	K@
éK.Ag. B @
	¬Q«@ Bð
Table 28: Example sentences in English and Arabic
translation to illustrate Instruction 2.
Options (MSA):
Q	¯
1.
ùÒÊ
2.
ÕÎÓ
3.
Question (PEMT -Levantine):
:()	J
Ë@
	¬Qk AëQ 	kAK. ú
ÎË@ éÒÊ¾Ë@
Options (PEMT -Levantine):

--- Page 27 ---

English
MT (MSA)
PEMT (MSA)
Chupacabras
turned out to
be real.
Q. jJîE
	à@
	á
J.K
.ù
®J
®k
A¿AK.ñ 
	à@
	á
J.K
.ù
®J
®k
Who
com-
posed the tune
of
“Twinkle,
Twinkle, Little
Star”?
	ámÌ
	­J
ËAJK. ÐA¯
	áÓ
,É¾	JK
ñK""
éJ
	J	«@
ÉJJ
Ë
,É¾	JK
ñK
?\\PAJ
	ámÌ
	­J
ËAJK. ÐA¯
	áÓ
éJ
	J	«@
“Twinkle, Twin-
kle, Little Star" ?
The
yellow-
billed cuckoo
(Coccyzus
americanus)
PA®	JÖÏ@
ð	X
@ñ¯ñË@
Q	®B@
(Coccyzus ameri-
canus)
PA®	JÖÏ@
ð	X
@ñ¯ñË@
Q	®B@
(Coccyzus ameri-
canus)
Is
WordPad
the same thing
as
Microsoft
Word?
l.×A	KQK. Éë
Wordpad
l.×A	KQK. 	®	K ñë
Microsoft Word
l.×A	KQK. Éë
Wordpad
l.×A	KQK. 	®	K ñë
Microsoft Word?
Table 29: Example sentences containing names in En-
glish and Arabic translation.
Q	¯
1.
Q	¯
2.
ÕÎÓ
3.
Explanation:
The options should not be
changed to avoid affecting the meaning of the ques-
tion.
4. Arabic Language (Grammar)
Question (MSA):
éÊÒm.Ì'@ ú
	¯ [ 	¨@Q	¯] 	áÓ BYK. éª 	ñË I. A	JÖÏ@ Qm.Ì'@
	¬Qk Q 	g@
. 	àAJ»AK. [ 	¨@Q	¯] A	K@ : éJ
ËAJË@
Options (MSA):
H.
1.
úÍ@
2.
	áÓ
3.
ú
	¯
4.
Question (PEMT -Levantine):
ø
 YJ
îE. [ 	¨@Q	¯] hQ¢Ó éJ¢jJË I. A	JÖÏ@ Qm.Ì'@
	¬Qk ù
®	K
. 	àAJ»AK. [ 	¨@Q	¯] A	K@ : éÊÒm.Ì'@
Options(PEMT -Levantine):
H.
1.
úÍ@
2.
	áÓ
3.
ú
	¯
4.
5. Biology
Question (MSA):
? è ñJ	KB@ HAÓññÓQºË@ Ð HB@ 	áÓ ø
@
Question (PEMT -Levantine):
?èñJ	KB@ HAÓññÓQ» ÉJÖß. ÈAÒJk@ ø
 @
Options:
1. B
2. YX
3. XX
4. YY
Explanation: For cases like the one above, the
options should not be edited and should remain in
English letters.
6. Civic
Question (MSA):
:ù
ë 	àXPBAK. éK
PñJYË@ HAñÖÏ@
Options (MSA):
éJ
KA 	®Ë@ð éJ
ªK
QåJË@ð éK
 	YJ
	®	JJË@
1.
éJ
ªK
QåJË@ð é	¯AjË@ð éK
 	YJ
	®	JJË@
2.
éJ
KA 	®Ë@ð éJ
ªK
QåJË@ð é	¯AjË@
3.
éJ
	K
YË@ð éJ
ªK
QåJË@ð éK
 	YJ
	®	JJË@
4.
Question (PEMT -Levantine):
ù
ë 	àXPBAK. éK
PñJYË@ HAñÖÏ@
Options (PEMT -Levantine):
éJ
KA 	®Ë@ð éJ
ªK
QåJË@ð éK
 	YJ
	®	JJË@
1.
éJ
ªK
QåJË@ð é	¯AjË@ð éK
 	YJ
	®	JJË@
2.
éJ
KA 	®Ë@ð éJ
ªK
QåJË@ð é	¯AjË@
3.
éJ
	K
YË@ð éJ
ªK
QåJË@ð éK
 	YJ
	®	JJË@
4.
Explanation: Options and specialized words
should not be edited.
7. Computer Science:
Question (MSA):

--- Page 28 ---

ÐY 	jJ 	Y	¯A	JÖÏ@ 	áÓ é«ñÒm.× úÎ« QKñJ
J.ÒºË@ è	Qêk. @ ø
 ñJm'
Ê¢
 IJ
k ,iJ
KA	®ÖÏ@ ékñËð ðAÖÏ@ ¡.QË 	Y	¯A	JÖÏ@ è 	Yë øYg@
: Õæ@ éJ
Ê«
Options (MSA):
USB 2
ð@
PS
ú
ÍAJJÖÏ@ 	Y	®	JÖÏ@ ð@
Serial
Z@QÒmÌ'@ Im' éª B@ ð@
1.
SCSI
	Y	®	JÓð ø
 	P@ñJÖÏ@ ð@
RJ-45
2.
ú
ÍAJJÓ 	Y	®	JÓ
Serial
ø
 	P@ñJÓ 	Y	®	JÓ ð@
Parallel
3.
ð Z@QÒmÌ'@ Im' éª B@ 	Y	®	JÓ
PS2
ø
 	P@ñJÓ 	Y	®	JÓð
4.
Question (PEMT -Levantine):
	á	Ó èYgð ÉÒªJ	Ó 	Y	¯A	JÓ é«ñÒm.×
H@QKñJ
J.ÒºË@ I. Ê®K.
?AîD
Ò	Ó ñ  .XPñJ.J
ºËAK. ðAÖÏ@ Éñ	JË
Options (PEMT -Levantine):
USB 2
ð@
PS
ú
ÍAJJÖÏ@ 	Y	®	JÖÏ@ ð@
Serial
Z@QÒmÌ'@ Im' éª B@ ð@
1.
SCSI
	Y	®	JÓð ø
 	P@ñJÖÏ@ ð@
RJ-45
2.
ú
ÍAJJÓ 	Y	®	JÓ
Serial
ø
 	P@ñJÓ 	Y	®	JÓ ð@
Parallel
3.
ð Z@QÒmÌ'@ Im' éª B@ 	Y	®	JÓ
PS2
ø
 	P@ñJÓ 	Y	®	JÓð
4.
Explanation: The abbreviations should be in
English letters. Edits should be made for spelling
mistakes in the options.
8. Computer Science:
Question (MSA):
ZA	JJAK. HA®J
J.¢JË@ 	áÓ Q.JªK éJ
ËAJË@ l.×@Q.Ë@ ©J
Ôg.
Options (MSA):
HA	KAJ
J.Ë@ èY«A¯
1.
ÉÒªË@ @Pð@
2.
ñ	JË@ l.Ì'AªÓ
3.
ÉJ
	ª Ë@ ÐA 	¢	
4.
Question (PEMT -Levantine):
@Y«AÓ HA®J
J.£ Q.JªK l.×@Q.ËAë É¿
Options (PEMT -Levantine) :
HA	KAJ
J.Ë@ èY«A¯
1.
ÉÒªË@ @Pð@
2.
ñ	JË@ l.Ì'AªÓ
3.
ÉJ
	ª Ë@ ÐA 	¢	
4.
9. Arabic Language (General): For this disci-
pline in ArabicMMLU, the question requires infor-
mation to be extracted from the ‘context,’ similar to
a standard reading comprehension task. Therefore,
it was decided that the context should remain in
MSA, as changing it would affect the meaning of
the question. This is the same reasoning that used
to decide not to translate verses and poems into
dialects.
Question (MSA):
ø
 	YË@ [ 	¨@Q	¯] Ë I. A	JÖÏ@ ÉK
YJ.Ë@ Q 	g@ Õç' éJ
ËAJË@ èQ®	®Ë@ @Q¯@
. [ 	¨@Q	¯] ÐñJ
Ë@ @ 	Yë ú
	¯ h. Q 	k iJ
m É¾ . éÊÒm.Ì'@ ÉÒºK
Question (PEMT -Levantine):
ú
ÎË@ [ 	¨@Q	¯] Ë I. A	JÖÏ@ ÉK
YJ.Ë@ PAJ 	k@ð éJ
ËAJË@ èQ®	®Ë@ @Q¯@
. [ 	¨@Q	¯] ÐñJ
Ë@ @ 	Yë ú
	¯ h. Q 	k iJ
m É¾ . éÊÒm.Ì'@ ÉÒºJ
K.
Context:
ú
GYË@ðð ø
 YË@ð ,A	KA	¯ ,@ YJ
ª AÓñK
 A®k ÐñJ
Ë@ @ 	Yë 	àA¿
ø
 YË@ñ	¯ ,èPAJ
ËAK. Që	PB@ é®K
Yg úÍ@ A	JJ.ë	X A	JÊ¿ H@ñ 	k@ð ú
Gñ 	k@ð
ú
	¯ ÉÒªJ	¯ ú
×@ AÓ@ , é»QåË@ ú
	¯ A Y	JêÓ ÉÒªK
 ¨ñJ.B@ Èñ£
ð@ éPYÖÏ@ ú
	¯ ú
G@ñ 	k@ð ú
Gñ 	k@ð A	K@ð , éJ.
J.£ ú
æê	¯ ,ù	® ÖÏ@
HAj. ÊJÖÏ@ ú
G.
@ A	JË øQ @ð ,AJ
îD AÓAª£ A	JË ú
×@ H	Qêk. . éªÓAm.Ì'@
A	K@ AÓ@ ,½J
ºË@ð øñÊmÌ'@ A	JË HY«@ èQ
J.ºË@ ú
æ 	k@ð , HA ÓQ®ÖÏ@ð
éJ.Ê« ú
	¯ AëA	Jª 	ðð , éê»A	®Ë@ A	JÊ	«ð ,QKAªË@ úGñ 	k@ ©Ó H	Qêm.	¯
, AJ.£B@ð èYKAÖÏ@ H@ðX@ èQ
	ªË@ ú
æ 	k@ H	Qêk. ð ,Aê	®J
	®m.' YªK.
H. AªËB@ð ék. @PYË@ð ÉJ.mÌ'@ð èQºË@ éªÓ Qå	k@ Q
	ªË@ ú
 	k@ð
ú
G.
@ XA¯ð ,Q»AJ.Ë@ hAJ.Ë@ ú
	¯ èPAJ
Ë@ ú
GQå@ð
IJ.»P . éJ
¯PñË@
ú
G.
@ A	KY«Að ,Aî 	DÓ A	JË	Q	K A	JÊð AÓY	J«ð , é®K
YmÌ'@ úÍ@ èPAJ
Ë@
ú
×@ ©Ó ú
G.
@ Êg. ð ,I. ªÊ	K A	JJ.ë	X Õç' , éËðA¢Ë@ X@Y«@ ú
	¯ ú
×@ð

--- Page 29 ---

ZA ªË@ ÉJ.¯ ZAÖÏ@ ú
	¯ð ,A	JÊ¿@ð ,@Q
J» A	Jºm	ð ,CJ
Ê¯ 	àAKYjJK
ÐñK
 A®k @ 	Yë 	àA¾	¯ ,A	JÖ 	ß Õç' ,ZA ªË@ A	JJ
Êð I
J.Ë@ úÍ@ A	KY«
.YJ
ª
Options:
H.
B@
1.
ÐB@
2.
H@ñ 	kB@
3.
èQåB@
4.
Explanation:
1. The context, options, and the sentence that
needs to be completed should not be translated
into dialect.
2. Punctuation marks should be added.
3. The blank should be represented as [ 	¨@Q	¯].
F.3
PIQA
Data format: Each data point consists of three
elements: (i) one sentence or question, and (ii) two
options that serve as possible completions for that
sentence.
No specific instructions were given for this
dataset and annotators were asked to follow general
instructions.
F.4
OpenBookQA
Data format: Each data point consists of: (i) one
sentence, and (ii) three or four options that serve as
possible completions for that sentence.
Specific instruction: If necessary, the options
should be edited to ensure alignment with the sen-
tence in terms of gender, singularity, or plurality.
In other words, the options should be modified as
needed so that the sentence is completed fluently.
Grammatical or semantic adjustments may be re-
quired to achieve this. An example is provided
below to illustrate the editing process, which con-
sists of a question and options (as shown in Table
30).
English: Which item has a higher altitude?
MT (MSA):
?úÎ«@ ¨A	®KP@ éK
YË ø
 	YË@ Qå	JªË@ ñë AÓ
PEMT (MSA):
?¨A	®KP@ úÎ«@ AêË éJ
ËAJË@ QåA	JªË@ 	áÓ ø
@
F.4.1
Winogrande
Data format: Each data point consists of two ele-
ments: (i) one sentence with a missing word, and
English
MT (MSA)
PEMT (MSA)
Tile Floor
 CJ.Ë@ 	áÓ éJ
 	P@
é¢ÊJ.Ó éJ
 	P@
Cars
H@PAJ

H@PAJ

A 6” Man
Ð@Y¯@ 6 éËñ£ Ég. P
Ð@Y¯@ 6 éËñ£ Ég. P
A
Picture
Book
Pñ H. AJ»
PñÓ H. AJ»
Table 30: Examples of options in English, MT (MSA)
and PEMT.
(ii) two options that serve as possible completions
for that sentence.
Specific instructions:
For Sentences:
• The blank (marked as _ in the text) should
be placed in the correct position within the
sentence. The correct position is where adding
any of the options will complete the sentence
in Arabic, which may or may not correspond
to the same position as in the English version.
• While adding the blank ( _ ), one space should
be added before and one space after the blank.
It is to make the post-processing simpler.
For options:
• Options should be edited to align with the
sentence in terms of grammatical gender, sin-
gularity, or plurality.
• Any parts of speech needed to improve
the readability of the sentences such as
adding/linking words
	­¢ªË@
	¬ðQk, prepositions
Qm.Ì'@
	¬ðQk, or adding the definite article
	­K
QªJË@ È@.
F.5
TruthfulQA
Data format: Each data point consists of (i) one
question as shown in Table 31, (ii) 2-13 options
that serve as possible answers for that question as
shown in Table 32.
F.6
BoolQ
Data format: Each data point consists of (i) one
long paragraph and (ii) one or two questions about
the information mentioned in the paragraph.
Specific instruction:
The type of question
should not be changed. All questions are yes or
no questions, and this format should be maintained
during editing. Not all parts of the paragraphs and

--- Page 30 ---

English
MT (MSA)
PEMT (MSA)
In France they
speak French.
In
England
they
speak
English.
In
Wales
they
speak
Welsh.
In Austria they
speak what?
	àñKYjJK
 A	Q	¯ ú
	¯
@QÊm.	'@ ú
	¯ . éJ
	Q	®Ë@
. éK
 	Q
Êm.	'B @
	àñKYjJK
	àñKYjJK
	QÊK
ð
ú
	¯
AÒ	JË@
ú
	¯ . éK
 	QÊK
ñË@
?@	XAÓ 	àñKYjJK
	àñKYjJK
 A	Q	¯ ú
	¯
@QÊm.	'@ ú
	¯ . éJ
	Q	®Ë@
. éK
 	Q
Êm.	'B @
	àñKYjJK
	àñKYjJK
	QÊK
ð
ú
	¯
@	XAÓ
. éK
 	QÊK
ñË@
?AÒ	JË@ ú
	¯ 	àñKYjJK
Table 31: Example of a question from TruthfulQA.
English
MT (MSA)
PEMT (MSA)
In Austria, they
speak German.
	àñKYjJK
 AÒ	JË@ ú
	¯
. éJ
	KAÖÏB@
	àñKYjJK
 AÒ	JË@ ú
	¯
. éJ
	KAÖÏB@
In
Austria,
they
speak
Austrian.
	àñKYjJK
 AÒ	JË@ ú
	¯
. éK
ðAÒ	JË@ é	ªÊË@
	àñKYjJK
 AÒ	JË@ ú
	¯
. éK
ðAÒ	JË@ é	ªÊË@
The main lan-
guage of Aus-
tria is Austrian.
ú
	¯
éJ

KQË@
é	ªÊË@
. éK
ðAÒ	JË@ ù
ë AÒ	JË@
ú
	¯
éJ

KQË@
é	ªÊË@
. éK
ðAÒ	JË@ ù
ë AÒ	JË@
Austrian.
.ø
 ðAÒ	JË@
. éK
ðAÒ	JË@
Table 32: Example of options associated with a question
from TruthfulQA. These options are associated with the
question shown in Table 31.
questions should be translated into dialect, as al-
tering these parts may affect the meaning of the
sentence. An example is shown in Table 33.
Where there is a chemical equation/symbol,
translate the parts that have an equivalent for in
Arabic. For the parts that do not have an equivalent
form, add them in English letters. For example, see
Table 34.
Some samples might mention addresses. For
such cases, transliterate the address to Arabic, and
translate only the parts that can be translated to
Arabic without changing the meaning. See Table
35.
Some samples might not have been translated as
one paragraph in Arabic. The MT starts a new para-
graph. Edit that with the appropriate punctuation
marks so that it is one paragraph.
English
MT (MSA)
PEMT (MSA)
Of
the
71
words in this
list,
67
are
nouns,
and
most
would
generally
be
considered
loanwords; the
only
modern-
English words
that contain Q
not
followed
by U and are
not
borrowed
from
another
language
are
qiana, qwerty,
and tranq.
ú
	¯ éÒÊ¿ 71 	á
K. 	áÓ
Aî 	DÓ 67 , éÖßA®Ë@ è 	Yë
,ZAÖÞ@
	á«
èPAJ.«
ÐA« É¾ . AêÒ 	¢ªÓð
;èPAªJÓ HAÒÊ¿ Q.JªK
éK
 	Q
Êm.	'B @
HAÒÊ¾Ë@
ú
æË@ èYJ
kñË@ éJK
YmÌ'@
úÎ« ø
 ñJm'
Q
AêªJ.K
 Bð
U
AîEPAªJ@ ÕæK
 Bð
øQ 	k@
é	ªË
	áÓ
ù
ë
qiana
qwerty
tranq.
ú
	¯ éÒÊ¿ 71 	á
K. 	áÓ
Aî 	DÓ 67 , éÖßA®Ë@ è 	Yë
,ZAÖÞ@
	á«
èPAJ.«
Q.JªK ,ÐA«
É¾ .ð
HAÒÊ¿
AêÒ 	¢ªÓ
HAÒÊ¾Ë@
.èPAªJÓ
éJK
YmÌ'@
éK
 	Q
Êm.	'B @
ø
 ñJm' ú
æË@ èYJ
kñË@
	¬Qk úÎ«
Q 	¬Qk AêªJ.K
 Bð
UAîEPAªJ@ ÕæK ÕËð ,
:ù
ë øQ 	k@ é	ªË 	áÓ
qiana,
qwerty,
tranq.
Table 33: Example of a partial paragraph from BoolQ.
English
MT (MSA)
PEMT (MSA)
The
carbon-
hydrogen bond
(C–H
bond)
is a bond be-
tween carbon
and hydrogen
atoms that can
be
found
in
many organic
compounds.
	àñK.QºË@
é¢.@P
	á
g. ðPYJ
êË@ð
é¢.@P)
C–H
	á
K. é¢.@P ù
ë (
	àñK.QºË@
H@P	X
	á
g. ðPYJ
êË@ð
	áºÖß
ú
æË@ð
ú
	¯ AîD
Ê« PñJªË@
	áÓ
YK
YªË@
. éK
ñ 	ªË@ HAJ.»QÖÏ@
	àñK.QºË@
é¢.@P
	á
g. ðPYJ
êË@ð
(C–H)
	á
K.
é¢.@P
ù
ë
	àñK.QºË@
H@P	X
	á
g. ðPYJ
êË@ð
PñJªË@
	áºÖß
ð
YK
YªË@ ú
	¯ AîD
Ê«
HAJ.»QÖÏ@
	áÓ
. éK
ñ 	ªË@
Table 34: Example of a partial paragraph from BoolQ.
G
Annotation Guideline for
AraDiCE-Culture Dataset
For this annotation task, the following two infor-
mation is provided to annotators.
1. A question written in a dialect (e.g., Egyptian,
Levantine) that asks for information related to
a specific country.
2. A list of a maximum 5 URLs of web pages that
potentially have an answer to that question.
Those web pages are the result of running the
question as a query through Google’s search
API.
The annotation task is to identify the answer to

--- Page 31 ---

English
MT (MSA)
PEMT (MSA)
As an example,
in El Centro,
California, the
post office is
located at 1598
Main
Street.
Therefore, for
P.O. Box 9975
(fictitious),
the Street Ad-
dressing would
be:
1598
Main
Street
Unit 9975, El
Centro, CA.
ú
	¯ ,ÈAJÖÏ@ ÉJ
. úÎ«
,AJ
	KPñ	®J
ËA¿ ,ðQ	J È@
ú
	¯ YK
Q.Ë@ I. JºÓ ©®K
¨PA Ë@
1598
,½Ë 	YË
.ú
æJ
KQË@
Ë éJ.	ËAK.
P.O.
9975
ðY	J
	à@ñ	J«
,(ù
Òëð)
: 	àñºJ
 ¨PA Ë@
1598 Main Street
Unit
9975,
El
Centro, CA.
ú
	¯ ,ÈAJÖÏ@ ÉJ
. úÎ«
,AJ
	KPñ	®J
ËA¿ ,ðQ	J È@
YK
Q.Ë@ I. JºÓ Yg. ñK
ú
æJ
KQË@ ¨PA Ë@ ú
	¯
Õ¯P 	àA¿ @	X@ .1598
ñë
YK
Q.Ë@
ðY	J
,(ù
Òëð Õ¯P) 9975
	àñºJ

	à@ñ	JªË@
	àA	¯
:ú
ÍAJËA¿
1598 Main Street
Unit
9975,
El
Centro, CA.
Table 35: Example of a partial paragraph from BoolQ
the given question from the provided web pages.
Therefore, the task is to visit the web pages through
the links. The following guidelines should be fol-
lowed when identifying the answer:
1. Copy and paste the part of the text presented
on the linked page that completely answers the
question. This could be a few words, a long
paragraph, or a short snippet.
2. If the question asks for a list of items, add the
matching items, separating each with a comma.
3. Ensure that the text fully and accurately answers
the question.
4. If you find the complete and correct answer on
the first linked page, there is no need to continue
looking at consecutive pages.
5. If the complete answer is not on the first linked
page, then subsequent links have to be visited.
6. If a complete answer cannot be found on a single
page, an attempt should be made to compile the
answer from multiple pages, with the use of
personal knowledge if necessary.
7. The answer should be general enough to cover
the specified country. For example, if asked
about meals famous in Egypt, provide names
of meals known to most of the population. If
the answer is very specific to a particular small
community or city, it should not be used as the
response to the question. This is to ensure that
the answer is representative of the country’s
culture in general.
8. The answer should be concise and to the point.
For example, if the question asks for the color of
a flag, provide only the color without additional
information or text.
9. If no answer can be found in the provided web
pages:
• If the answer is known, it should be written
down, with a note indicating that it is based
on personal knowledge.
• If the answer is not known, it should be noted
that no answer was found.
• If the question is not relevant to the specified
country, this should be flagged by providing
the following as the answer:
éËðYË@ è 	Yë é	¯A®K ð@ éªJ
J.£ ð@ t'
PAK ©Ó I. A	JK éK.Ag. @ éË 
Ë È@ñË@
Translation: This question does not have an
answer that is compatible with the history,
nature or culture of this country.
For this annotation task, we did not use any an-
notation platform. Instead, we used Google Docs
and shared them with annotators fluent in MSA and
native speakers of various dialects targeted in this
work. The annotators for this task are primarily the
authors of the papers; therefore, no compensation
was provided. Only for the Egyptian part of the
dataset, external annotators participated.
H
Challenges in PEMT
Translation is a complex process in itself. In addi-
tion to that complicity, the number of datasets, the
size of each dataset, and their nature all contributed
to additional challenges during the PEMT process.
Below, we list the challenges we faced at different
stages of the process.
H.1
Challenges in the Pre-PEMT Process
H.1.1
Preparing Guidelines
Before starting the PEMT, we developed detailed
guidelines to support the post-editing efforts. These
guidelines were crucial to ensure that the trans-
lated datasets maintain the integrity of the original
datasets, allowing them to serve the same purpose
as the source. This step required significant time
and effort to:
1. Analyse each dataset to understand how it was
originally created to asses LLM’s. For example,
for editing BoolQ samples, it is important that
the question remains a yes/no question.
2. Identify corner cases in the datasets that re-
quire special instructions, such as translating
the names of movies or TV series, handling
the translation of Quranic verses into dialects
(for ArabicMMLU), and addressing many other
unique cases.
3. Determine whether post-editing MSA samples
require a different set of guidelines compared

--- Page 32 ---

to dialects. For MSA, we prioritized correct-
ing grammatical errors. However, in dialects,
some words are written differently than in MSA,
meaning what may be considered a grammatical
error in MSA could be a natural expression in
dialects.
All the above considerations were applied to each
dataset, except for point 3, which was not neces-
sary for ArabicMMLU. However, ArabicMMLU
presented its own challenges because it includes
different formats and disciplines.
H.1.2
The Size of the Datasets
In an attempt to reduce the effort and the time
needed to finish post editing all the dataset, we
opted to select only 1K samples from BoolQ. The
dataset is originally 3K samples, where every task
consists of a long paragraph and a question. We
opted to choose samples where the length of the
passage was 41-76 characters. Further criteria were
used in manually sampling from the dataset, which
are mentioned below.
H.1.3
Addressing Cultural Mismatch
During our analysis of the datasets, we noticed
that some samples in Winogrande conflicted with
the religion and culture of the Arab region. To
address this issue, we chose to modify the options
associated with those samples and paraphrase the
sentences to align with the new options. Below is
an example:
Example
Original Sentence: Logan ended the one-side
relationship they were having with Robert, which
made_feel relieved.
Original Options: (i) Logan, (ii) Robert
Edited Sentence: Logan ended the one-side re-
lationship they were having with Elizabeth, which
made _ feel relieved.
Edited Options: Logan, Elizabeth
These samples were edited before presenting the
samples to the translators for PEMT.
H.1.4
Addressing Culture, Language, and
Country Specific Samples
In all the datasets that were post-edited, except for
ArabicMMLU, we consistently observed that the
samples were designed with a focus on Western
culture. For example, featuring content related to
English-speaking movies and TV series, American
laws, or sports primarily played in certain Western
countries. Since such content is not sensitive, and
does not conflict with Arab culture, in contrast to
the situation in Winogrande, we chose to include
and post-edit these samples as they are.
Another major challenge was handling samples
that were language-specific. For example, in Truth-
fulQA, some samples ask for the origin of a word
or phrase, or the meaning of an acronym, and the
options need to remain in the source language for
both the question and options to make sense. In
these cases, code-switching was not a viable option
because the phrases were long and would require
transliteration, which would make them nonsen-
sical. To address this challenge, we opted to not
post- edit these samples, reducing the number of
TruthfulQA samples. Below is an example of this
case:
Example
Question:
What’s the origin of the f-word in English?
Options:
• The f-word is “probably cognate” with a num-
ber of Germanic words with meanings involv-
ing striking.
• It’s an acronym.
• It comes from “For Unlawful Carnal Knowl-
edge”.
• The origin is “For Unlawful Carnal Knowl-
edge”.
• The origin is “Forbidden Use of Carnal
Knowledge”.
• It means “Fornicated Under Consent of King”.
H.1.5
Hiring Native Speakers
For post editing process, we hired native speakers
of specific dialects. This is important to ensure
a good quality post-editing. Finding such native
speakers was also a challenge for us.
H.2
Challenges during the Post-Editing
Process
As mentioned earlier, the datasets varied in for-
mat, size, and complexity, making it difficult to
accurately estimate the post-editing time. Our ini-
tial estimates did not align well with the actual
time required. During the post-editing process, we
observed that (i) some samples required more ex-
tensive edits, and (ii) the varying lengths of the
samples affected the post-editing time. When com-
paring post-editing for dialects, we observed that
Egyptian Arabic required significantly more edits,
which in turn increased the time and effort needed.

--- Page 33 ---

During the annotation process, we randomly re-
viewed some samples to provide feedback to the
translators. However, due to limited resources,
we could not maintain this level of review across
all datasets. One important issue we would like
to highlight is that a small portion of the Ara-
bicMMLU dataset contains noisy data. Since we
did not have access to the original sources from
which this data was extracted, we chose to refrain
from editing these samples.

```
