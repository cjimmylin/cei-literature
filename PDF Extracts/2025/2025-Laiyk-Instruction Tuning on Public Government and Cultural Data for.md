---
title: "2025-Laiyk-Instruction Tuning on Public Government and Cultural Data for - PDF Extract"
source_pdf: "2025-Laiyk-Instruction Tuning on Public Government and Cultural Data for.pdf"
pages: 29
extracted_at: "2026-02-13T09:50:28.980037"
---

# PDF Extract: 2025-Laiyk-Instruction Tuning on Public Government and Cultural Data for

**Source PDF:** 2025-Laiyk-Instruction Tuning on Public Government and Cultural Data for.pdf
**Total Pages:** 29

---

## Content

```
--- Page 1 ---

Instruction Tuning on Public Government and Cultural Data
for Low-Resource Language: a Case Study in Kazakh
Nurkhan Laiyk1∗
Daniil Orel1∗
Rituraj Joshi2
Maiya Goloburda1
Yuxia Wang1
Preslav Nakov1
Fajri Koto1
1Department of Natural Language Processing, MBZUAI
2Cerebras Systems
{nurkhan.laiyk,daniil.orel}@mbzuai.ac.ae
Abstract
Instruction tuning in low-resource languages
remains underexplored due to limited text data,
particularly in government and cultural do-
mains.
To address this, we introduce and
open-source a large-scale (10,600 samples)
instruction-following (IFT) dataset, covering
key institutional and cultural knowledge rel-
evant to Kazakhstan. Our dataset enhances
LLMs’ understanding of procedural, legal,
and structural governance topics. We employ
LLM-assisted data generation, comparing open-
weight and closed-weight models for dataset
construction, and select GPT-4o as the back-
bone. Each entity of our dataset undergoes
full manual verification to ensure high quality.
We also show that fine-tuning Qwen, Falcon,
and Gemma on our dataset leads to consistent
performance improvements in both multiple-
choice and generative tasks, demonstrating the
potential of LLM-assisted instruction tuning
for low-resource languages.
1
Introduction
Instruction tuning enhances large language models
(LLMs) by fine-tuning them on structured prompts,
improving their ability to follow human instructions
across various tasks such as question answering and
summarization (Ouyang et al., 2022). While extensive
instruction-tuning datasets exist for English, such as
FLAN (Longpre et al., 2023), P3 (Sanh et al., 2021),
and Dolly (Conover et al., 2023), efforts in low-resource
languages remain limited. This gap is particularly evi-
dent in domain-specific applications where multilingual
LLMs often provide generic or inaccurate responses due
to a lack of localized training data (Li et al., 2023).
A key challenge in adapting LLMs to underrepre-
sented languages is the scarcity of high-quality instruc-
tion data (Li et al., 2023). Multilingual models may pro-
cess low-resource languages at a technical level (Ope-
nAI, 2024), but their practical effectiveness is often
constrained by an incomplete understanding of region-
specific socio-political structures and cultural contexts.
For example, when asked about administrative proce-
dures like obtaining a passport in a particular country,
∗These authors contributed equally.
models tend to default to well-documented cases rather
than providing precise, localized information. Similarly,
cultural narratives—such as folklore, literature, and tra-
ditions—are often missing from instruction datasets
(Conover et al., 2023), limiting the models’ ability to
generate contextually appropriate responses.
While
prior work relied on translation (Sengupta et al., 2023)
or template-based techniques (Cahyawijaya et al., 2024)
to build instruction-tuning datasets, it does not fully
reflect the actual local context, as direct translations of-
ten fail to capture the nuances of regional governance,
customs, and linguistic variations.
Building instruction datasets from scratch is costly,
making large-scale manual data collection impractical
for many low-resource languages. To address this, we
adopt an LLM-assisted dataset generation approach (Liu
et al., 2022; Cahyawijaya et al., 2023; Zhang et al.,
2024), followed by full human validation. Specifically,
we use a single-prompt method where LLMs process
high-quality unlabeled text from public government and
cultural sources to extract both factual information and
corresponding instructions. These domains are highly
relevant for real-world applications, but remain underex-
plored for instruction-tuning, particularly in the context
of government data.
To demonstrate the effectiveness of this approach,
we introduce an instruction-tuning dataset for Kazakh
that integrates both institutional1 (GovSet) and cultural
(CultSet) domains. We choose Kazakh as our case
study because it remains underrepresented in NLP (Joshi
et al., 2020), despite having approximately 20 million
speakers. Prior research on Kazakh NLP has primarily
focused on classic tasks such as named entity recog-
nition (Yeshpanov et al., 2022) and sentiment analysis
(Yeshpanov and Varol, 2024), leaving more advanced
applications like instruction tuning, largely unexplored.
Our contributions are as follows:
• We create an open-source a high-quality manu-
ally verified large scale (10K samples) IFT dataset,
which covers both cultural, and institutional knowl-
edge, relevant to Kazakhstan.
• We contribute new domain knowledge on essen-
tial institutional topics, including procedural, legal,
structural, and other key aspects of public gover-
1Our study incorporates administrative, procedural, legal,
structural, and other government-related types of information.
arXiv:2502.13647v2  [cs.CL]  31 Aug 2025

--- Page 2 ---

 <kaz>
<instr>: Егер бала шетелде туса, ал ата-анасының бірі
шетелдік болса, онда қандай құжат қажет?
<eng>:
<instr>: If a child is born abroad and one of the parents is
a foreign citizen, what document is required?
<kaz>:  
<instr>: Егер бала шетелде туса, ал ата-анасының бірі шетелдік
болса, баланың паспортын ресімдеуге қандай құжат қажет?
Collected
text 
<eng>: 
<inst>: If a child is born abroad and one of the parents is a foreign
citizen, what document is required to issue the child's passport?
GPT-4o
generation
Generated instruction-response for CultSet
Manual
Validation
Validated instruction for GovSet
Data Collection
Data Creation
<resp>: If a child is born abroad and one of the parents is
a foreign citizen, then a notarized consent from that parent
is additionally required to issue a passport of the Republic
of Kazakhstan.
 <kaz>
<instr>: Киiз үйде түндiк дегенiмiз не екенiн түсiндiрiңiз.
<instr>: Explain what "tundik" means in a Kazakh yurt.
<resp>: Түндiк — киiз үйдiң шаңырағына жабы-латын киiз,
ол әрi жарық бередi, әрi түтiн шығуға мүмкiндiк бередi. 
<resp>: Tündik is a felt covering placed over
the shanyrak (the top part of a yurt), which provides both
light and ventilation for smoke to escape.
<resp>: Егер бала шетелде туса, ал ата-анасының бірі шетелдік
болса, онда Қазақстан Республикасы азаматының паспортын
ресімдеуге оның нотариалды келісімі қосымша қажет.
<resp>: If a child is born abroad and one of the parents is a foreign
citizen, what document is required to issue the child's passport?
<kaz>:  
<instr>: Қазақ халқының киiз үйiндегi түндiктiң не екенiн 
түсiндiрiңiз.
  
<inst>: Explain what "tundik" means in the Kazakh yurt.
<resp>: Түндiк — қазақтың баспанасы киiз үйдiң шаңырағына
жабылатын киiз. Ол әрi iшке жарық өткiзедi, әрi түтiн шығуына
мүмкiндiк бередi. 
<resp>: The "tundik" is the felt cover placed on the top of the Kazakh
yurt. It serves as insulation and allows smoke to escape. 
Collected
text 
KazWiki
Gov.kz
Validated instruction for CultSet
Generated instruction-response for GovSet
<resp>: Егер бала шетелде туса, ал ата-анасының бірі
шетелдің болса, онда ҚР азаматының паспортын
рәсімдеуге оның нотарилды келісімі қосымша қажет 
<eng>:
<eng>:
Figure 1: End-to-end process of dataset construction. The English translation is for illustrative purposes.
nance, enhancing LLMs’ understanding of these
critical areas.
• We compare the efficacy of open-weight and
closed-weight LLMs in LLM-assisted dataset con-
struction for low-resource languages and underrep-
resented cultures.
• We demonstrate that fine-tuning on our dataset, re-
sults in consistent improvements in both multiple-
choice and generative tasks. These results highlight
the impact of incorporating localized knowledge
into instruction tuning and demonstrate the poten-
tial of LLM-assisted approaches for expanding in-
struction datasets in other low-resource languages.
2
Related Work
2.1
Instruction-Tuning Datasets in English
There are three main strategies for creating English
instruction-tuning datasets: human-curated datasets,
templatized NLP tasks, and synthetic data generation
using LLMs.
Human-curated datasets, such as Open Assistant
(Köpf et al., 2023) and Dolly (Conover et al., 2023),
rely heavily on human annotation. While this approach
ensures high-quality data, it is expensive and difficult
to scale across multiple languages. To reduce costs,
datasets like the Public Pool of Prompts (P3) (Sanh
et al., 2021), SuperNatural Instructions (Wang et al.,
2022), and FLAN (Longpre et al., 2023) reformat exist-
ing NLP tasks into instruction-based formats. However,
these datasets primarily focus on specific NLU tasks
rather than general-purpose instruction following, limit-
ing their applicability.
Prior work on instruction dataset creation has largely
relied on generating data from existing language models
without incorporating external real-world knowledge.
Self-Instruct (Wang et al., 2023) expands an initial set
of human-written instructions by iteratively generating
new tasks using the model’s own outputs, while Hon-
ovich et al. (2023) created instruction-tuning datasets
by conditioning on a few example instructions. These
methods rely solely on sampling data from language
models or predefined topics, rather than grounding them
in external knowledge, making them less suitable for
capturing domain-specific or culturally relevant under-
standing. Unlike these approaches, our work focuses on
Kazakh, a low-resource language, and constructs an in-
struction dataset by leveraging external, factual sources
such as governmental and cultural texts, ensuring align-
ment with real-world contexts.
2.2
Instruction Tuning Datasets for Medium- to
Low-Resource Languages
While human-curated datasets are often expensive and
require native speakers, prior work has explored au-
tomatic dataset generation using machine translation
for medium- to low-resource languages. Sengupta et al.
(2023) applied this approach to develop JAIS, an Arabic-
centric language model, by translating various English
instruction datasets into Arabic. Similarly, Li et al.
(2023) translated Alpaca (Taori et al., 2023) into 52 lan-
guages. More recently, Alyafeai et al. (2024) introduced
an Arabic instruction dataset by translating Alpaca into
Arabic and performing manual edits and localization
to ensure relevance to the Arabic context. Although
this method is scalable, the quality of translation re-
mains inconsistent for low-resource languages, as noted
by Li et al. (2023). Additionally, machine-translated
datasets often introduce Anglocentric biases, limiting
their ability to capture culturally diverse perspectives.
Several frameworks have been proposed to improve
instruction tuning for low-resource languages. MURI
(Köksal et al., 2024) generates multilingual instruction
datasets using reverse instruction generation and trans-

--- Page 3 ---

lation, but none of its data have been validated by native
speakers. Li et al. (2024) improve upon translation-
based methods by prompting LLMs in English while
requiring responses in low-resource languages (e.g.,
Urdu), allowing models to leverage their internal knowl-
edge of the target language’s local context. However,
our approach differs in that we do not rely on the
model’s internal knowledge but instead use factual in-
formation from reliable sources such as government
data. Additionally, our dataset undergoes full human
validation to ensure accuracy and relevance. Meanwhile,
Cahyawijaya et al. (2023) focused on the linguistic as-
pects of instruction tuning by denoising low-resource
language text and prompting models to reconstruct com-
plete sentences. While this enhances fluency, it differs
from our approach, which prioritizes grounding instruc-
tions in externally verified, domain-specific knowledge
rather than refining linguistic quality alone.
2.3
Existing datasets in Kazakh
While there has been significant progress in developing
Kazakh datasets, the majority of high-quality Kazakh
datasets are related to speech (Mussakhojayeva et al.,
2024, 2022, 2021). In terms of textual data, existing re-
sources primarily focus on question answering and read-
ing comprehension rather than instruction tuning. For
instance, KazQAD (Yeshpanov et al., 2024) is a Kazakh
open-domain question answering (ODQA) dataset that
can be used in both reading comprehension and full
ODQA settings, as well as for information retrieval ex-
periments. Similarly, Belebele (Bandarkar et al., 2023)
is another dataset that, while useful for multilingual ma-
chine reading comprehension, is not explicitly designed
for instruction tuning. Belebele covers 122 languages,
including Kazakh, and comprises 900 multiple-choice
questions associated with 488 distinct passages from the
Flores-200 dataset.
Despite progress in Kazakh NLP resources, no ex-
isting instruction-tuning dataset incorporates cultural
or domain-specific knowledge, focuses on real-world
applications, and undergoes full human validation. This
limits the ability of LLMs to process Kazakh-language
instructions effectively in practical and locally relevant
contexts, which we aim to address in this work.
3
Background
Kazakh Cultural Heritage. Kazakhstan has a rich cul-
tural heritage that reflects a blend of nomadic traditions,
Soviet influences, and modern developments.
The country’s nomadic heritage is evident in many
aspects of daily life, from its architecture, with yurts (tra-
ditional felt tents) still used in rural areas, to its customs
of communal gatherings and feasts, such as the celebra-
tion of the Turkic New Year, Nauryz. Kazakh hospitality
is a source of pride for the nation, embodied in proverbs
like "Qonaq keldi — ırysın ala keldi" ("A guest arrives,
bringing fortune with them"). It is deeply important
that guests are never left hungry. They are always of-
fered a variety of traditional dishes, such as beshbarmak
(a hearty dish of boiled meat with pasta) and baursak
(deep-fried dough). Kazakhstan’s Soviet past has also
left a lasting imprint on its culture. Many cities still bear
the architectural marks of Soviet planning, while the era
also shaped the country’s education and scientific insti-
tutions, fostering a strong tradition in mathematics and
engineering—most notably reflected in the Baikonur
Cosmodrome, the world’s first and largest space launch
facility. Alongside all of this, modern developments
have transformed Kazakhstan. The capital, Astana, is
a prime example of this shift, with its futuristic skyline
and ambitious urban projects Investments in technology,
renewable energy, and digital infrastructure have pro-
pelled Kazakhstan onto the global stage, while cultural
revitalization efforts have fostered a renewed interest in
the Kazakh language, music, and art.
At it’s core, Kazakhstan’s culture is shaped by beliefs
and values, social practices, language, artistic expres-
sion, and material culture. Understanding these compo-
nents is crucial for ensuring accurate and meaningful
representation.
Kazakhstan’s Institutional Structure and the Pub-
lic Governance. Kazakhstan operates as a presidential
republic, and since gaining independence in 1991, the
country has focused on modernization, particularly in
governance and legal frameworks. The Constitution of
Kazakhstan, adopted in 1995, provides the foundation
for the country’s laws, establishing the rights and re-
sponsibilities of citizens, as well as the structure of the
government. A significant shift has been the digital-
ization of many governmental processes, making ser-
vices more accessible to the public. Kazakhstan ranks
among the top 25 countries in the UN E-Government
Development Index (EGDI) (Nations, n.d.). One of the
most notable achievements is the development of the
eGov platform, a centralized system providing citizens
with streamlined access to various government services.
eGov serves as a one-stop portal for activities such as
registering businesses, paying taxes, applying for social
benefits, and obtaining official documents like passports
and ID cards. It is a comprehensive source of govern-
mental services in Kazakhstan, simplifying processes
that previously required significant time and paperwork.
These various aspects of Kazakhstan—its rich cul-
tural heritage, nomadic traditions, modern gover-
nance, and the increasing digitalization of public ser-
vices—reflect the unique characteristics and dynamics
of the country. As Kazakhstan continues to modernize
and integrate technological advancements into everyday
life, it is crucial that these characteristics are properly
represented in tools like language models.

--- Page 4 ---

4
Data
4.1
Document Source
GovSet
We manually collected 1,376 texts from the
official Kazakhstan e-Government portal (gov.kz2), the
primary and most comprehensive platform for all pub-
lic services, governmental processes, and administra-
tive resources in the country. As the central hub for
Kazakhstan’s digital governance, gov.kz consolidates
a wide range of essential information into a single sys-
tem, covering diverse aspects of public administration,
legal frameworks, citizen services, and governmental
initiatives. By incorporating these texts, we ensure that
the dataset captures essential institutional aspects of life
in Kazakhstan, including its governmental structure and
public services. This enrichment enhances instruction-
tuning applications, making them more linguistically
appropriate and contextually informed.
CultSet
We automatically collected 4,400 texts from
Kazakh Wikidata,3 specifically focusing on pages re-
lated to Kazakh culture. These pages were identified
based on metadata that explicitly indicated their rele-
vance to Kazakh cultural topics. The parsed texts in-
clude various aspects of Kazakh traditions, heritage,
arts, and historical practices, providing a rich source of
culturally relevant content. This ensures that the dataset
reflects the depth and diversity of Kazakh culture, mak-
ing it suitable for instruction-tuning tasks that require a
culturally grounded perspective.
4.2
LLM-assisted Data Generation
We benchmark one open-weight LLM: LLaMA 3.1-
70B (Touvron et al., 2023), and three closed-weight
LLMs: GPT-4o (OpenAI, 2024), Gemini-1.5 (Deep-
Mind, 2024), and Claude-3.5-Sonnet (Anthropic, 2024),
to assess their effectiveness in assisting dataset creation.
These models were selected based on their strong per-
formance in multilingual benchmarks. However, their
capability in generating instruction datasets specific to
Kazakh government and cultural data remains uncertain.
We design a prompt (see Appendix A.3) that in-
structs LLMs to first extract factual information from a
given Kazakh document and then generate an instruc-
tion dataset based on the extracted content. Table 2
provides detailed statistics on the source documents and
the resulting instruction fine-tuning (IFT) dataset using
GPT-4o. Specifically, we use 4,400 Kazakh cultural
Wikipedia documents and 1,376 Kazakh government
data sources, generating a total of 10,600 IFT instances.
Of these, 58% belong to the government public data
category (GovSet), while the remaining samples are
derived from Wikipedia (CultSet). The example of
generated IFT data can be found in Table 15 and Ta-
ble 17.
2https://www.gov.kz
3kk.wikipedia.org
Model
Correctness
Completeness
Fluency
Llama 3.1 (70B)
3.54
3.45
3.07
Claude
3.74
3.48
3.09
Gemini 1.5
3.85
3.64
3.32
GPT-4o
4.38
4.29
4.04
MURI
3.87
3.52
3.41
Table 1: Human evaluation on LLM-generated instruc-
tion datasets.
Human Evaluation Across LLMs
For each LLM, we
sampled 100 generated IFT instances, drawn from 25
randomly selected GovSet and 25 CultSet documents.
Additionally, we randomly sampled 100 instances from
MURI (Köksal et al., 2024), which also includes Kazakh
IFT data, to provide a comparative quality assessment.
Two native Kazakh speakers were recruited to manu-
ally evaluate the generated data based on the following
criteria:
• Correctness: The factual accuracy and alignment
with the original text. A high score indicates that
the generated pair adheres closely to the source
material without introducing errors or inaccuracies.
• Fluency: The grammatical and stylistic quality of
the generated text. A higher score reflects well-
structured, natural, and polished language.
• Completeness:
The
degree
to
which
the
instruction-response pair is clear, contextually
grounded, and free from ambiguity. High scores
indicate that the pair is fully self-contained, with
enough context to make it understandable.
All criteria were rated on a Likert scale from 1 to 5, with
5 representing the highest quality. A detailed evaluation
rubric is provided in Table 8.
Table 1 presents the quality assessment of various
LLMs in generating IFT data for Kazakh. The inter-
annotator agreement, measured using Pearson correla-
tion, is high (ranging from 0.68 to 0.70) across cor-
rectness, completeness, and fluency, indicating strong
reliability in the evaluation process (see Appendix K.1
for further details).
Among the evaluated models, GPT-4o achieved the
highest performance across all three criteria. In contrast,
LLaMA-3.1 (70B) lagged significantly, scoring nearly
0.8–1 point lower in all aspects. Notably, MURI’s qual-
ity was lower than GPT-4o despite both relying on Ope-
nAI models. This discrepancy is likely due to MURI’s
reliance on machine translation, where Kazakh text is
first translated into English before generating instruc-
tions, followed by a final back-translation into Kazakh.
This multi-step translation process can introduce errors
due to cumulative translation inaccuracies. Addition-
ally, MURI is entirely LLM-generated without human
validation, further affecting its quality.
4.3
Manual Post-Editing
Given GPT-4o’s strong performance, we use it for large-
scale IFT data generation while ensuring quality through

--- Page 5 ---

CultSet
GovSet
Collected text
4,400
1,376
Avg. lengths (#char) of collected text
245
179
Generated IFT pairs
4,400
6,200
Avg. lengths (#char) of instruction
85
76
Avg. length (#) of output
453
215
# of unique tokens
62,449
24,304
Table 2: Overall statistics of GPT-4o generated IFT
dataset.
Error Type
% of Questions
CultSet
GovSet
No error
28.32%
19.47%
Wrong language
0.07%
0.14%
Structural
28.45%
33.58%
Grammatical
25.24%
28.73%
Lexical
17.92%
18.08%
Table 3: Distribution of error types in GPT-4o-generated
IFT data from CultSet and GovSet, identified during
manual post-editing.
full human verification. We employ 12 expert anno-
tators, all native Kazakh speakers with advanced de-
grees in World Languages, Literature, or Political Sci-
ence from top Kazakhstani universities. Their extensive
experience—having lived in Kazakhstan for over 25
years—equips them with the necessary linguistic and
cultural expertise.
To maintain consistency, annotators received detailed
guidelines outlining task objectives, evaluation criteria,
and examples of high-quality IFT pairs (see Appendix
F). They were responsible for manually reviewing and
correcting errors in the generated data. Before starting
the main annotation process, all candidates completed
a pilot task to assess their understanding of project re-
quirements and their ability to refine IFT pairs accu-
rately. Only those who met the evaluation criteria were
selected. Each annotator’s workload was equivalent to
five full working days, and they were compensated fairly
based on Kazakhstan’s monthly minimum wage. To ac-
commodate flexibility, annotators were given up to one
month to complete the task while working part-time.
Table 3 summarizes the error types identified during
manual post-editing of GPT-4o-generated data across
the two document sources.
Annotators found that
CultSet had a higher proportion of "No error" cases
(28.32%) compared to GovSet (19.47%), suggesting
variations in data quality.
Structural errors were the most common in both
datasets, accounting for over 28% in CultSet and 33%
in GovSet. These errors involve grammatically correct
but poorly structured responses, including issues with
logical flow, organization, and unnatural phrasing for a
Kazakh speaker. Additionally, grammatical and lexical
errors were frequently observed, with annotators noting
that GPT-4o occasionally replaces Kazakh words with
Russian equivalents, even when the correct Kazakh term
is explicitly provided in the original text. For a detailed
breakdown of annotator observations, see Appendix H.
4.4
Final Data Overview
As shown in Table 2, the final dataset consists of
4,400 CultSet and 6,200 GovSet IFT instances, total-
ing 10,600 high-quality samples. We split the dataset
into 90% training and 10% test, where the training data
is used for full fine-tuning of LLMs, and the test set is
used for generation evaluation in our experiments.
Since both CultSet and GovSet are topic-based, we
include their respective topics as metadata in the final
IFT dataset (see Table 13 and Table 14 for topic def-
initions). Figure 2 illustrates the topic distribution of
the dataset. The most common topics in CultSet in-
clude Kazakh literature, traditions, and media, while
GovSet primarily covers legal assistance, the healthcare
system, real estate laws, and education in Kazakhstan.
Examples of GPT-4o-generated IFT data can be found
in Table 15 and Table 17.
Table 2 further highlights a notable difference be-
tween the two subsets:
the average output length
in CultSet is significantly longer and contains more
unique tokens than GovSet. This difference stems from
the nature of GovSet responses, which are strictly fac-
tual and concise, whereas CultSet responses tend to be
more diverse and expressive.
5
Experiments
We conducted two experiments: multiple-choice ques-
tions (MCQ) and text generations evaluation. We will
detail each of the evaluation in the following sections.
Model Selection
For both MCQ and generation eval-
uations, we use three models: Gemma-2-9B (Gemma)
(Team et al., 2024), Qwen-2.5-7B (Qwen)(Qwen et al.,
2025), and Falcon-3-10B (Falcon) (Team, 2024). While
these LLMs have multilingual capabilities, they were
not specifically trained for Kazakh, allowing us to as-
sume that our IFT data is novel to them.
Fine-tuning
We
performed
full
fine-tuning
on
Gemma-2-9b, Qwen-2.5-7b, and Falcon-3-10b using
the AdamW optimizer with hyperparameters β1 = 0.9,
β2 = 0.95, ϵ = 1e−5, and a weight decay of 0.1. We
scaled the gradient norms using a maximum norm clip-
ping value of 1.0. The learning rate was kept constant
throughout the fine-tuning without any warm-up or de-
cay with a value of 1e−6 for Gemma-2 and Falcon-3,
and 1e−5 for Qwen-2.5. The batch size used was 16,
and we packed multiple documents until the maximum
sequence length was 8,192 tokens. Cross-document at-
tention is disabled by modifying attention masks so the
tokens of a document only attend to the tokens from the
same document in a causal way. No adjustment were
made to the original tokenizer for each model.

--- Page 6 ---

(a) CultSet
(b) GovSet
Figure 2: Topic distribution of GPT-4 generated IFT dataset in CultSet and GovSet.
(a) CultSet
(b) GovSet
Figure 3: Distribution of preferences for (a) CultSet and (b) GovSet datasets across models. The charts illustrate
the percentage of ’Tie’, ’Vanilla’, and ’After Fine-Tuning’ preferences in each dataset.
Baseline
As a baseline, we include the Kazakh Alpaca
dataset,4 which has been translated and localized into
Kazakh. For each model, we conduct full fine-tuning
with (1) our training dataset, (2) Alpaca, and (3) a com-
bination of Alpaca and our training dataset.
5.1
Multiple-choice Question Evaluation
Dataset
A dedicated open-source Kazakh NLP com-
munity5 has collaboratively developed and crowd-
sourced multiple hand-crafted benchmarks to assess the
factual knowledge of LLMs in Kazakh. We use three
multiple-choice question (MCQ) datasets: (1) Dastur-
MC (Sagyndyk et al., 2024b), which evaluates knowl-
edge of Kazakh traditions, (2) Kazakh Constitution-
MC (Sagyndyk et al., 2024a), which focuses on Kaza-
khstan’s legal system, and (3) Kazakh Unified Na-
tional (Sagyndyk et al., 2024c), which assesses citizen
rights, legal protections, and societal knowledge (re-
ferred to as the "Human Rights and Society" dataset).6
4https://huggingface.co/datasets/AmanMussa/
kazakh-instruction-v2
5https://huggingface.co/kz-transformers
6Examples of test questions are provided in Appendix L.
Model
Vanilla
RAG
Alpaca
Ours
Alpaca + Ours
Dastur
Gemma
0.498
0.533
0.513
0.543
0.566
Qwen
0.403
0.410
0.421
0.443
0.465
Falcon
0.450
0.460
0.458
0.464
0.471
Constitution
Gemma
0.600
0.655
0.627
0.640
0.650
Qwen
0.520
0.523
0.609
0.670
0.680
Falcon
0.430
0.386
0.450
0.490
0.520
Human Rights and Society
Gemma
0.405
0.450
0.430
0.465
0.480
Qwen
0.300
0.325
0.330
0.365
0.375
Falcon
0.215
0.220
0.234
0.250
0.275
Table 4: Zero-shot accuracies of language models in
different datasets: (1) Datasur, (2) Constitution, and (3)
Human Rights and Society
Each dataset consists of multiple-choice questions
with four answer options, only one of which is cor-
rect. We selected these evaluation benchmarks because
they align with the focus of our instruction fine-tuning

--- Page 7 ---

dataset and are not derived from our document sources
(CultSet and GovSet). These datasets cover cultur-
ally significant topics, legal frameworks, and citizen-
government interactions, reflecting real-world applica-
tions that our fine-tuned models aim to support.
Since no documented quality assurance process was
available for the three datasets, we conducted a manual
verification to ensure the accuracy of the questions. To
maintain a fair and valid comparison, only the manually
verified samples were used in our evaluation. For the
Dastur-MC dataset, we randomly sampled 300 ques-
tions and manually verified their correctness. The same
process was applied to the Kazakh Constitution-MC and
Human Rights and Society datasets, with 200 randomly
selected questions from each.
Setup
In addition to the fine-tuned models, we in-
clude retrieval-augmented generation (RAG) without
fine-tuning to estimate the upper bound of the origi-
nal models’ performance. For RAG, we use BM25
encoding, as no specialized Kazakh retrieval encoder
is available. For each question, we retrieve the top two
matching text chunks (each 256 symbols long) from the
training texts of our IFT corpus and provide them as
additional context.
To assess model capability, we use the LM Eval
Harness (Gao et al., 2024) framework in a zero-shot
setting. During evaluation, the answer is selected based
on the alphabetical option with the highest likelihood.
Result
Table 4 presents the zero-shot evaluation re-
sults across different models and techniques. Overall,
our fine-tuned dataset consistently outperforms other
approaches across datasets and models. The only excep-
tion is the Constitution dataset, where RAG performs
better with Gemma. Models fine-tuned on Kazakh Al-
paca show some improvement, though it remains lower
than that achieved with our instruction fine-tuning (IFT)
dataset.
Combining parts of our IFT dataset with the trans-
lated Alpaca dataset yields the highest performance
gains. This aligns with prior studies (Brief et al., 2024;
Wang et al., 2024), which suggest that incorporating gen-
eral chat instructions alongside domain-specific ones
enhances model performance.
For RAG-enhanced models, performance generally
exceeds that of the vanilla models, except for Falcon
on the Constitution dataset. However, fine-tuned mod-
els consistently achieve higher scores than their RAG-
enhanced counterparts. We hypothesize that this is due
to the models’ limited proficiency in Kazakh, which
may hinder their ability to fully understand the retrieved
context. As a result, despite the additional information
provided by RAG, the models may struggle to extract
the necessary details to select the correct answer in
MCQs.
CultSet
GovSet
After FT
Vanilla
After FT
Vanilla
Gemma
24.87
15.76
25.10
16.12
Falcon
27.98
25.96
28.70
26.17
Qwen
26.63
27.64
28.42
30.27
Table 5: Rouge-L comparison on CultSet and GovSet.
5.2
Generation Evaluation
We evaluate generation performance using our test set,
which consists of 500 questions from both CultSet and
GovSet (excluded from fine-tuning). We compare the
best models from Section 5.1 against their vanilla coun-
terparts. In this section, "After Fine-Tuning" refers
to models fine-tuned on Alpaca + Our Data, while
"Vanilla" refers to the original pre-trained models.
Automatic Evaluation with ROUGE and BERTScore
As shown in Table 5, fine-tuned models generally out-
perform their vanilla counterparts, except for Qwen,
where fine-tuning results in a lower ROUGE-L score
(Lin, 2004). However, a lower ROUGE-L does not nec-
essarily indicate worse performance—it may be due to
Qwen generating different phrasings compared to the
gold answers.
To further validate the quality of generated responses,
we also evaluate BERTScore (Zhang et al.). We use
Kaz-RoBERTa7 as the encoder model, as it is one of
the few open-source Kazakh-language transformers.
The BERTScore results in Table 6 align well with the
ROUGE-L scores. However, since Kazakh is a low-
resource language, BERTScore should be considered a
reference point rather than a definitive metric, as Kaz-
RoBERTa embeddings may not perfectly capture syn-
onym relationships.
Preference Evaluation with GPT-4o
We conducted
a 1-to-1 preference evaluation using the LLM-as-a-
judge approach. Specifically, we prompted GPT-4o
to compare responses from different models and deter-
mine whether each response wins, loses, or ties. The
prompt includes the instruction and the gold response
as context for GPT-4o.8 As shown in Figure 3, the
results align with ROUGE-L and BERTScore, confirm-
ing that fine-tuned models generally produce improved
outputs. Compared to Falcon, Qwen and Gemma ex-
hibit more significant improvements (63%–80% win-
ning rate), likely because their pre-trained versions were
less optimized for the task, making fine-tuning more
impactful.
Additionally, we analyze the win rate across topics
in CultSet and GovSet, as shown in Appendix B. The
results indicate that the impact of fine-tuning varies by
topic and is not always consistent. In CultSet, fine-
tuning Qwen with our IFT data yields the most improve-
ment in Cultural Institutions and Culture & Traditions,
7Huggingface model: kaz-roberta-conversational
8The prompt used for comparison is provided in Ap-
pendix A.2.

--- Page 8 ---

CultSet
GovSet
Precision
Recall
F1
Precision
Recall
F1
After Fine-Tuning
Gemma
41.94
46.36
43.62
40.27
44.90
42.00
Falcon
24.59
29.68
26.64
23.78
27.73
25.36
Qwen
39.64
45.40
41.82
36.28
40.20
37.59
Vanilla
Gemma
29.26
33.47
30.92
27.36
34.81
30.39
Falcon
23.29
28.17
25.20
20.38
24.68
22.11
Qwen
40.58
47.46
43.40
36.57
44.14
39.50
Table 6: BERTScore Precision, Recall, and F1 for CultSet and GovSet.
while the gains are smaller in Science & Humanities
and even lead to a decline in performance for Educa-
tion & Academia. In GovSet, fine-tuning Qwen with
our dataset significantly enhances performance in Legal
Assistance, though the improvement is less noticeable
in Employment-related topics.
While LLM-based evaluations provide scalable com-
parisons, they may not fully capture human judgment
nuances, making human evaluation essential for validat-
ing model preferences. Therefore, three human annota-
tors conducted a preference evaluation on a randomly
sampled 100 examples for each model (Gemma, Qwen,
and Falcon) across both CultSet and GovSet. Their
judgments were compared against the GPT-based pref-
erence evaluation to assess alignment. We computed
Cohen’s Kappa between GPT-4o and the annotators,
obtaining 0.63 for CultSet and 0.68 for GovSet, indi-
cating substantial agreement. We have also calculated
the agreement rate between annotators (detailed in Ap-
pendix K.2). The results show that GPT’s alignment
with human preferences is moderate, with better agree-
ment on GovSet than CultSet.
Conversational Evaluation.
As an extension of these
experiments, we generated a set of 100 conversations
for both CultSet and GovSet combined, covering top-
ics presented in Figure 2. These conversations were
intentionally left unfinished using a special prompt, as
detailed in Appendix A.2. Both the original and fine-
tuned models were tasked with generating the most ap-
propriate continuation for each conversation. Examples
of the resulting texts are showin in Table M. To evaluate
the quality of the responses, we employed an LLM-as-
a-judge framework. The results, presented in Figure 4,
indicate that models fine-tuned on domain-specific data
produced significantly more coherent and contextually
appropriate responses compared to their pre-fine-tuning
counterparts. We also see that in the conversational set-
tings there are less ties, compared to simple question
answering.
6
Conclusion and Future Work
We introduced a culturally and institutionally aligned
instruction-tuning dataset for Kazakh, aiming to en-
hance practical knowledge representation and address
the specific needs of public governmental data process-
ing in Kazakh. Through a carefully designed data collec-
tion pipeline, we generated instruction-tuning examples
Figure 4: Conversational data preference evaluation.
using GPT-4o and ensured their quality via a manual
correction and localization to capture Kazakh linguistic
and cultural nuances accurately.
The evaluation results show that this approach sub-
stantially improved the model’s factual knowledge, and
the understanding of low-resource languages. It also
shows that after such fine-tuning, the model’s responses
are much better in terms of correctness and soundness,
as assessed by native speakers and LLM as a judge.
In future work, we plan to apply this methodology to
other languages and dialects. We further aim to work to-
wards streamlining and automating the process as much
as possible. We will also focus more on the model-
ing part of the experiments, and open-source culturally
and institutionally relevant models for low-resource lan-
guages including Kazakh.
7
Limitations
We aim to establish a robust instruction-tuning dataset
for Kazakh, authentically reflecting the cultural and
linguistic richness of the language. Unlike many ex-
isting datasets, which rely on translated resources or
machine-generated responses, our dataset is entirely
crafted from Kazakh-specific content, ensuring greater
alignment with the cultural values and linguistic nu-
ances of the region. However, we recognize several
limitations in our work:
• Cultural Representation: The dataset emphasizes
topics deeply rooted in Kazakh culture, traditions,
and societal norms, ensuring relevance and cultural
authenticity. However, certain culturally sensitive
topics, such as those involving religious matters,

--- Page 9 ---

were intentionally omitted to avoid controversy and
maintain neutrality.
• Language Variations: Kazakh is a rich language
with significant regional variations in vocabulary
and usage. While our dataset primarily focuses on
standard Kazakh, it does not explicitly account for
regional dialects or variations, potentially limiting
its applicability to speakers outside the standard
dialect’s scope.
• Modeling Limitations: Our works is a proof of
concept, and it was not aimed at creation of SOTA
models for Kazakh. That is why we experiment
with smaller models and do not apply any training
tricks such as tokenizer adaptaion for Kazakh.
• Possible Data Drift: We also acknowledge that
despite of being very conservative by nature, some
institutional procedures can change over time, that
is why it is possible that the data provided in our
IFT dataset will get less actual. To handle this issue
we are planning updating the datasets annually.
8
Ethics
We adhered to the internal policies of web resources
while scraping data and included only publicly available
information verified by authorities.
While our method enhances LLMs’ understanding
of Kazakhstan’s institutional nuances, users should not
blindly trust generated responses. LLM outputs serve
as a starting point, and users remain responsible for
fact-checking due to potential hallucinations.
All human subjects in our study provided informed
consent, were fully aware of the study’s objectives, and
had the right to withdraw at any time. They were also
appropriately compensated as part of their job.
References
Zaid Alyafeai, Khalid Almubarak, Ahmed Ashraf,
Deema Alnuhait, Saied Alshahrani, Gubran Abdul-
rahman, Gamil Ahmed, Qais Gawah, Zead Saleh,
Mustafa Ghaleb, Yousef Ali, and Maged Al-shaibani.
2024. CIDAR: Culturally relevant instruction dataset
for arabic. In Findings of the Association for Compu-
tational Linguistics: ACL 2024, pages 12878–12901,
Bangkok, Thailand. Association for Computational
Linguistics.
Anthropic. 2024.
Claude ai: An overview.
https:
//www.anthropic.com.
Lucas Bandarkar, Davis Liang, Benjamin Muller, Mikel
Artetxe, Satya Narayan Shukla, Donald Husa, Naman
Goyal, Abhinandan Krishnan, Luke Zettlemoyer, and
Madian Khabsa. 2023. The belebele benchmark: a
parallel reading comprehension dataset in 122 lan-
guage variants.
Meni Brief, Oded Ovadia, Gil Shenderovitz, Noga Ben
Yoash, Rachel Lemberg, and Eitam Sheetrit. 2024.
Mixing it up: The cocktail effect of multi-task fine-
tuning on llm performance – a case study in finance.
Samuel Cahyawijaya, Holy Lovenia, Fajri Koto, Rifki
Putri, Wawan Cenggoro, Jhonson Lee, Salsabil Akbar,
Emmanuel Dave, Nuurshadieq Nuurshadieq, Muham-
mad Mahendra, Rr Putri, Bryan Wilie, Genta Winata,
Alham Aji, Ayu Purwarianti, and Pascale Fung. 2024.
Cendol: Open instruction-tuned generative large lan-
guage models for Indonesian languages. In Proceed-
ings of the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Pa-
pers), pages 14899–14914, Bangkok, Thailand. As-
sociation for Computational Linguistics.
Samuel Cahyawijaya, Holy Lovenia, Tiezheng Yu,
Willy Chung, and Pascale Fung. 2023. InstructAlign:
High-and-low resource language alignment via con-
tinual crosslingual instruction tuning. In Proceedings
of the First Workshop in South East Asian Language
Processing, pages 55–78, Nusa Dua, Bali, Indonesia.
Association for Computational Linguistics.
Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie,
Jun Wan, Sam Shah, Ali Ghodsi, Patrick Wendell,
Matei Zaharia, and Reynold Xin. 2023. Free dolly:
Introducing the world’s first truly open instruction-
tuned llm. Last accessed 2024-01-15.
Google DeepMind. 2024.
Gemini 1.5:
Scal-
ing multimodal ai.
https://deepmind.google/
technologies/gemini.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Biderman,
Sid Black, Anthony DiPofi, Charles Foster, Laurence
Golding, Jeffrey Hsu, Alain Le Noac’h, Haonan Li,
Kyle McDonell, Niklas Muennighoff, Chris Ociepa,
Jason Phang, Laria Reynolds, Hailey Schoelkopf,
Aviya Skowron, Lintang Sutawika, Eric Tang, An-
ish Thite, Ben Wang, Kevin Wang, and Andy Zou.
2024. A framework for few-shot language model
evaluation.
Or Honovich, Thomas Scialom, Omer Levy, and Timo
Schick. 2023. Unnatural instructions: Tuning lan-
guage models with (almost) no human labor.
In
Proceedings of the 61st Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 14409–14428, Toronto, Canada.
Association for Computational Linguistics.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika
Bali, and Monojit Choudhury. 2020. The state and
fate of linguistic diversity and inclusion in the NLP
world. In Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics, pages
6282–6293, Online. Association for Computational
Linguistics.
Andreas Köpf, Yannic Kilcher, Dimitri von Rütte,
Sotiris Anagnostidis, Zhi-Rui Tam, Keith Stevens,
Abdullah Barhoum, Arnav Dantuluri, et al. 2023.
Openassistant conversations – democratizing large
language
model
alignment.
arXiv
preprint
arXiv:2304.07327.
Abdullatif Köksal, Marion Thaler, Ayyoob Imani, Ah-
met Üstün, Anna Korhonen, and Hinrich Schütze.
2024. Muri: High-quality instruction tuning datasets
for low-resource languages via reverse instructions.

--- Page 10 ---

Chong Li, Wen Yang, Jiajun Zhang, Jinliang Lu, Shao-
nan Wang, and Chengqing Zong. 2024. X-instruction:
Aligning language model in low-resource languages
with self-curated cross-lingual instructions. In Find-
ings of the Association for Computational Linguistics:
ACL 2024, pages 546–566, Bangkok, Thailand. Asso-
ciation for Computational Linguistics.
Haonan Li, Fajri Koto, Minghao Wu, Alham Fikri
Aji, and Timothy Baldwin. 2023.
Bactrian-x:
Multilingual replicable instruction-following mod-
els with low-rank adaptation.
arXiv preprint
arXiv:2305.15011.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summariza-
tion Branches Out, pages 74–81, Barcelona, Spain.
Association for Computational Linguistics.
Alisa Liu, Swabha Swayamdipta, Noah A. Smith, and
Yejin Choi. 2022. WANLI: Worker and AI collabora-
tion for natural language inference dataset creation.
In Findings of the Association for Computational
Linguistics: EMNLP 2022, pages 6826–6847, Abu
Dhabi, United Arab Emirates. Association for Com-
putational Linguistics.
Shayne Longpre, Le Hou, Tu Vu, Albert Webson,
Hyung Won Chung, Yi Tay, Denny Zhou, Quoc V. Le,
Barret Zoph, Jason Wei, and Adam Roberts. 2023.
The flan collection: Designing data and methods for
effective instruction tuning. In Proceedings of the
40th International Conference on Machine Learning,
ICML’23. JMLR.org.
Saida Mussakhojayeva, Rinat Gilmullin, Bulat Khaki-
mov, Mansur Galimov, Daniil Orel, Adal Abilbekov,
and Huseyin Atakan Varol. 2024. Noise-robust multi-
lingual speech recognition and the tatar speech corpus.
In 2024 International Conference on Artificial Intelli-
gence in Information and Communication (ICAIIC),
pages 732–737.
Saida Mussakhojayeva,
Aigerim Janaliyeva,
Al-
mas Mirzakhmetov,
Yerbolat Khassanov,
and
Huseyin Atakan Varol. 2021. KazakhTTS: An Open-
Source Kazakh Text-to-Speech Synthesis Dataset. In
Proc. Interspeech 2021, pages 2786–2790.
Saida Mussakhojayeva, Yerbolat Khassanov, and
Huseyin Atakan Varol. 2022. Ksc2: An industrial-
scale open-source kazakh speech corpus. In Inter-
speech 2022, pages 1367–1371.
United Nations. n.d. Un e-government development in-
dex (egdi). https://publicadministration.un.
org/egovkb/Data-Center. Accessed: 2025-01-19.
OpenAI. 2024.
Gpt-4o technical report.
https://
openai.com/research/gpt-4o.
Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Car-
roll L Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022.
Training language models to follow in-
structions with human feedback.
arXiv preprint
arXiv:2203.02155.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan Li,
Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin,
Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin Yang,
Jiaxi Yang, Jingren Zhou, Junyang Lin, Kai Dang,
Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li,
Mingfeng Xue, Pei Zhang, Qin Zhu, Rui Men, Runji
Lin, Tianhao Li, Tianyi Tang, Tingyu Xia, Xingzhang
Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang
Zhang, Yu Wan, Yuqiong Liu, Zeyu Cui, Zhenru
Zhang, and Zihan Qiu. 2025. Qwen2.5 technical
report.
Beksultan Sagyndyk, Sanzhar Murzakhmetov, Sanzhar
Umbet, and Kirill Yakunin. 2024a. Kazakh consti-
tution: Multiple choice benchmark. Available on
Hugging Face.
Beksultan Sagyndyk, Sanzhar Murzakhmetov, Sanzhar
Umbet, and Kirill Yakunin. 2024b. Kazakh dastur:
Multiple choice benchmark. Available on Hugging
Face.
Beksultan Sagyndyk, Sanzhar Murzakhmetov, Sanzhar
Umbet, and Kirill Yakunin. 2024c. Kazakh unified
national testing: Multiple choice benchmark. Avail-
able on Hugging Face.
Victor Sanh, Albert Webson, Colin Raffel, Stephen H.
Bach, Lintang Sutawika, Zaid Alyafeai, Antoine
Chaffin, Arnaud Stiegler, Teven Le Scao, Arun Raja,
Manan Dey, M Saiful Bari, Canwen Xu, Urmish
Thakker, Shanya Sharma, Eliza Szczechla, Taewoon
Kim, Gunjan Chhablani, Nihal Nayak, Debajyoti
Datta, Jonathan Chang, Mike Tian-Jian Jiang, Han
Wang, Matteo Manica, Sheng Shen, Zheng Xin Yong,
Harshit Pandey, Rachel Bawden, Thomas Wang, Tr-
ishala Neeraj, Jos Rozen, Abheesht Sharma, Andrea
Santilli, Thibault Fevry, Jason Alan Fries, Ryan Tee-
han, Tali Bers, Stella Biderman, Leo Gao, Thomas
Wolf, and Alexander M. Rush. 2021.
Multitask
prompted training enables zero-shot task generaliza-
tion. arXiv preprint arXiv:2110.08207.
Neha Sengupta, Sunil Kumar Sahu, Bokang Jia,
Satheesh
Katipomu,
Haonan
Li,
Fajri
Koto,
Osama Mohammed Afzal, Samta Kamboj, Onkar
Pandit, Rahul Pal, Lalit Pradhan, Zain Muhammad
Mujahid, Massa Baali, Alham Fikri Aji, Zhengzhong
Liu, Andy Hock, Andrew Feldman, Jonathan Lee,
Andrew Jackson, Preslav Nakov, Timothy Baldwin,
and Eric Xing. 2023.
Jais and jais-chat: Arabic-
centric foundation and instruction-tuned open gen-
erative large language models.
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann
Dubois, Xuechen Li, Carlos Guestrin, Percy Liang,
and Tatsunori B. Hashimoto. 2023. Stanford alpaca:
An instruction-following llama model. Last accessed
2024-01-15.
Falcon-LLM Team. 2024. The falcon 3 family of open
models.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak

--- Page 11 ---

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
dow, Matt Miller, Matthew Rahtz, Matthew Wat-
son, Meg Risdal, Mehran Kazemi, Michael Moyni-
han, Ming Zhang, Minsuk Kahng, Minwoo Park,
Mofi Rahman, Mohit Khatwani, Natalie Dao, Nen-
shad Bardoliwalla, Nesh Devanathan, Neta Dumai,
Nilay Chauhan, Oscar Wahltinez, Pankil Botarda,
Parker Barnes, Paul Barham, Paul Michel, Pengchong
Jin, Petko Georgiev, Phil Culliton, Pradeep Kup-
pala, Ramona Comanescu, Ramona Merhej, Reena
Jana, Reza Ardeshir Rokni, Rishabh Agarwal, Ryan
Mullins, Samaneh Saadat, Sara Mc Carthy, Sarah
Cogan, Sarah Perrin, Sébastien M. R. Arnold, Se-
bastian Krause, Shengyang Dai, Shruti Garg, Shruti
Sheth, Sue Ronstrom, Susan Chan, Timothy Jordan,
Ting Yu, Tom Eccles, Tom Hennigan, Tomas Ko-
cisky, Tulsee Doshi, Vihan Jain, Vikas Yadav, Vilobh
Meshram, Vishal Dharmadhikari, Warren Barkley,
Wei Wei, Wenming Ye, Woohyun Han, Woosuk
Kwon, Xiang Xu, Zhe Shen, Zhitao Gong, Zichuan
Wei, Victor Cotruta, Phoebe Kirk, Anand Rao, Minh
Giang, Ludovic Peran, Tris Warkentin, Eli Collins,
Joelle Barral, Zoubin Ghahramani, Raia Hadsell,
D. Sculley, Jeanine Banks, Anca Dragan, Slav Petrov,
Oriol Vinyals, Jeff Dean, Demis Hassabis, Koray
Kavukcuoglu, Clement Farabet, Elena Buchatskaya,
Sebastian Borgeaud, Noah Fiedel, Armand Joulin,
Kathleen Kenealy, Robert Dadashi, and Alek An-
dreev. 2024. Gemma 2: Improving open language
models at a practical size.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, et al. 2023. Llama: Open and effi-
cient foundation language models. arXiv preprint
arXiv:2302.13971.
Renxi Wang, Haonan Li, Minghao Wu, Yuxia Wang,
Xudong Han, Chiyu Zhang, and Timothy Baldwin.
2024.
Demystifying instruction mixing for fine-
tuning large language models. In Proceedings of
the 62nd Annual Meeting of the Association for Com-
putational Linguistics (Volume 4: Student Research
Workshop), pages 68–75, Bangkok, Thailand. Associ-
ation for Computational Linguistics.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Al-
isa Liu, Noah A. Smith, Daniel Khashabi, and Han-
naneh Hajishirzi. 2023. Self-instruct: Aligning lan-
guage models with self-generated instructions. arXiv
preprint arXiv:2212.10560.
Yizhong Wang, Swaroop Mishra, Pegah Alipoormo-
labashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva
Naik, Arjun Ashok, Arut Selvan Dhanasekaran, An-
jana Arunkumar, David Stap, Eshaan Pathak, Gian-
nis Karamanolakis, Haizhi Lai, Ishan Purohit, Is-
hani Mondal, Jacob Anderson, Kirby Kuznia, Krima
Doshi, Kuntal Kumar Pal, and et al. 2022. Super-
naturalinstructions: Generalization via declarative
instructions on 1600+ nlp tasks. In Proceedings of
the 2022 Conference on Empirical Methods in Nat-
ural Language Processing, pages 5085–5109, Abu
Dhabi, United Arab Emirates. Association for Com-
putational Linguistics.
Rustem Yeshpanov, Pavel Efimov, Leonid Boytsov,
Ardak Shalkarbayuli, and Pavel Braslavski. 2024.
Kazqad: Kazakh open-domain question answering
dataset. In arXiv preprint arXiv:2404.04487.
Rustem
Yeshpanov,
Yerbolat
Khassanov,
and
Huseyin Atakan Varol. 2022. KazNERD: Kazakh
named entity recognition dataset. In Proceedings of
the Thirteenth Language Resources and Evaluation
Conference, pages 417–426, Marseille, France.
European Language Resources Association.
Rustem Yeshpanov and Huseyin Atakan Varol. 2024.
Kazsandra: Kazakh sentiment analysis dataset of re-
views and attitudes.
Meishan Zhang, Gongyao Jiang, Shuang Liu, Jing Chen,
and Min Zhang. 2024. LLM-assisted data augmenta-
tion for Chinese dialogue-level dependency parsing.
Computational Linguistics, 50(3):867–891.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q Wein-
berger, and Yoav Artzi. Bertscore: Evaluating text
generation with bert. In International Conference on
Learning Representations.
A
Prompts Details
A.1
Prompt for preference evaluation

--- Page 12 ---

You are given 2 responses , and a Golden Label.
Please , decide which of the responses is the
best (you have to take into account its factual
correctness , and readability)
Response 1: {pred1}
Response 2: {pred2}
Golden Label: {gold_label}
Return 1 if the first response is better , 2 if the
second one is better , 0 if they are equally
good. Return only the number
A.2
Prompt for creating conversational data
Prompt:
Instruction: {input_instruction}
Output: {output}
You are creating conversational data between two
people discussing {topic} in Kazakhstan. The
conversation should:
- Start with a general but relevant topic that
smoothly leads into the instruction ’s question.
- Be short and concise , where Person 1 initiates the
discussion and then asks a question with a
meaning similar to the instruction at the end.
- Person 2 should respond but not reveal the output
- the conversation ends with "Person 2 says: ...".
- Maintain natural , formal dialogue relevant to
government regulations in Kazakhstan.
Example Format:
Person 1 says: [General opening statement leading to
the topic]
Person 2 says: [Relevant response that naturally
progresses the discussion]
Person 1 says: [Rephrased instruction question]
Person 2 says: ...
A.3
Prompts for Generation Instruction Dataset
You are given a text: {TEXT}.
I want to extract all the facts from the given text.
Based on the extracted facts , I want you to
create instruction fine -tuning pairs in Kazakh.
The pairs may fall into the following categories ,
but you are free to use other relevant
categories if appropriate:
- Is it true that ...
- Explain ...
- Describe ...
- List the steps ...
For each category , provide a clear instruction.
The instructions MUST incorporate the provided
context where relevant to make the questions
more specific and meaningful.
Do not add anything else in the output.

--- Page 13 ---

B
Preference Evaluation Results
(a) CultSet
(b) GovSet
Figure 5: Category-wise comparison of preference evaluation across datasets: (a) CultSet and (b) GovSet.

--- Page 14 ---

C
MURI Dataset Samples
Instruction
Output
Issue
Morangis Франциядағы коммуна
туралы мәлiмет беру
Моренгем () — Франциядағы ком-
муна.
Нор-Па-де-Кале
аймағы-
на қарасты Па-де-Кале департа-
ментiнде орналасқан. Сент-Омер
округiнiң құрамына енедi. Алып
жатқан жер аумағы 9,98 км2 ша-
масында. Коммунаның INSEE ко-
ды — 62592, пошта индексi —
62910. Демографиясы 2009 жы-
лғы мәлiметтер бойынша тұрғын-
дарының саны 485 адамды құра-
ды. Халық тығыздығы — 48,6
адам/км2. Тұрғындарының жас
шамасы және жынысы бойынша
құрамы (2006)...
Inconsistent use of Kazakh trans-
literation, wrong verb’s tense
Бiрнеше
танымал
онлайн
құ-
мар ойындар веб-сайттарын көр-
сетiңiз.
***Құмар флеш покер ойындары
– Қасқырлар мен қой ақша шығару
ойын. | Онлайн покер 25. | Карьер
ойындары солитей шаяны | Ру-
летка казино ойындарын ойнаңыз
November 24, 2019 Қалай онлайн
казино алдау Ханшайым академи-
ясында ойнау 0 Comments 196 Ка-
зино флеш ойындар онлайн Ой-
ын Real steel Android көп ақша
жүктеп. VIP карталар казино Құ-
мар ойындар онлайн сайт web.
Казино бақылау Флорида. Кази-
но flash player <...> Ақша са-
тып алу Android үшiн ойындар.
Sandia casino. Покер ақша тiркеу
ойын. Покер-рум avi casino. Ама-
зинг рп казино ойын тактикасы.
Флорида-казино покер. Antiguo
casino ponce Пуэрто-Рико. ...
Inconsistent
usage
of
Kazakh
transliteration, markdown in the raw
text
Бердiбек Сапарбаев Ақтөбе облы-
сында «Жастар жылы» туралы не
дедi?
Бердiбек Сапарбаев Ақтөбе об-
лысы Жастар жылын қалай өткi-
зетiнiн айтты | BAQ.kz 28 Қаңтар
2019, 08:35 1857 | 1857 Астана,
BAQ.KZ. Ақтөбе облысының әкi-
мi Бердiбек Сапарбаев 25 қаңтар,
жұма күнi Мемлекет басшысы-
ның
Жастар
жылы
аясындағы
тапсырмаларының орындалу мә-
селелерiн талқылау үшiн облы-
стағы жастар қозғалысының бел-
сендiлерiмен кездестi. ...
Markdown and meta-data in the raw
text
Table 7: Samples from MURI dataset.

--- Page 15 ---

D
Distribution of instruction types
(a) GovSet train instruction types
(b) GovSet test instruction types
(c) CultSet train instruction types
(d) CultSet test instruction types
Figure 6: Instruction types distribution.

--- Page 16 ---

E
Preliminary Study
E.1
Human Evaluation for Preliminary Study Rubric
Score
Correctness
Fluency
Completeness
1
Highly inaccurate, incorrect, or
misleading information.
Very poor fluency, riddled with
errors, making it difficult to read.
Very incomplete, with critical
information missing, making it
unusable.
2
Significant factual or logical errors
that impact the correctness of the
instruction/question.
Multiple errors that hinder
readability or cause confusion.
Significant omissions that make the
instruction/question incomplete or
difficult to interpret.
3
Noticeable errors in facts or logical
flow, but the general meaning
remains clear.
Noticeable errors in grammar,
spelling, or structure, but the text is
still understandable.
Noticeable gaps in information or
coverage that leave the
instruction/question lacking.
4
Minor factual inaccuracies or
inconsistencies that do not affect
overall understanding.
Minor grammatical or stylistic
errors that do not significantly
affect readability.
Slightly incomplete, with minor
missing details that do not impact
overall understanding.
5
Fully correct and consistent with
Kazakh cultural and governmental
contexts, no factual or logical
errors.
Perfect fluency, no errors in
grammar, spelling, or sentence
structure. The text reads smoothly
and naturally.
Fully complete, no information is
missing, and the
instruction/question thoroughly
covers the context.
Table 8: Human annotation rubric for preliminary studies.

--- Page 17 ---

F
Annotation Guideline
To ensure a high-quality and standardized format for instruction-output annotations, we provide clear guidelines
throughout the annotation process. The annotators refine and edit the automatically generated instruction fine-tuning
(IFT) pairs using Google Spreadsheets, with each annotator assigned an individual worksheet.
A detailed
explanation of each field is provided below.
• ID: A unique identifier assigned to each data entry.
• Category: This column contain the category of each data
• Instruction: The automatically generated instruction from the original text.
• Output: The corresponding generated output.
• Updated Instruction: A revised version of the instruction that has been edited.
• Updated Output: The modified output.
• Comment: Additional notes from the annotator, including explanations of any modifications, uncertainties
about correctness, or suggestions for further improvements.
General Rules
• Annotators must verify the correctness of the generated IFT pairs by comparing them against the original text.
If an instruction-answer pair appears ambiguous, incorrect, or not supported by the original text, it should be
highlighted for further review. The author (either the project owner or designated reviewers) will assess and
remove it if necessary.
• Instructions must be complete and contextually accurate. If an instruction refers for example to a place,
governmental process, or any specific entity but does not explicitly name it, annotators must incorporate the
missing details from the original text.
• Questions must be fluent in Kazakh and maintain formal language for governmental data. No literary expres-
sions, dialectal variations, or informal language should be introduced into governmental instructions—formality
must be preserved.
• When processing biographical information, ensure clarity in numerical dates.
• If an instruction-answer pair is completely unrelated to the original text, annotators must review the original
text, verify the discrepancy, and highlight it for correction.
• Annotators are required to provide progress updates every two days, ensuring that issues are addressed promptly.

--- Page 18 ---

G
Annotation example
G.1
GovSet
Type
Instruction
Output
Updated Instruction
Updated Output
G
Неке қиғаннан кейiн құжаттарды
ауыстыру үдерiсiн түсiндiрiңiз.
Некеге тұрғаннан кейiн жұбайы,
егер ол жұбайының/зайыбының
тегiн
алса,
неке
қию
туралы
куәлiктi алған сәттен бастап 30
күн iшiнде жеке куәлiктi ауысты-
ру қажет.
Қазақстанда неке қиғаннан кейiн-
гi құжаттарды ауыстыру үдерiсiн
түсiндiрiңiз.
Ең алдымен, адам некеден кейiн
жұбайының тегiн қабылдаса, жеке
куәлiгiн 30 күн iшiнде ауыстыруы
қажет.
Explain the process of changing doc-
uments after marriage.
After marriage, if the spouse takes
the husband’s/wife’s last name, the
national ID must be changed within
30 days from the date the marriage
certificate is received.
Explain the process of changing
documents after marriage in Kaza-
khstan.
First of all, if a person adopts their
spouse’s surname after marriage,
they must change their ID within 30
days.
G
Қазақстанда халықаралық рейсте
жоғалған багаж үшiн өтемақы тө-
ленетiнi рас па?
Иә, халықаралық рейсте жоғалған
багаж үшiн өтемақы Қазақстан
қол қойған екi Конвенцияның –
Варшава мен Монреальдың ере-
желерiне, сондай-ақ компаниялар-
дың iшкi ережелерiне сәйкес төле-
недi.
Қазақстанда халықаралық рейсте
жоғалған багаж үшiн өтемақы
төлейтiнi қаншалықты рас?
Қазақстанда халықаралық рейсте
жоғалған багаж үшiн өтемақы
төлейтiнi толықтай рас. Өтемақы
Қазақстан қол қойған екi Конвен-
цияның (Варшава мен Монреаль-
дың ережелерiне) және компани-
ялардың iшкi ережелерi негiзiнде
есептелiнiп төленедi.
Is it true that compensation is paid
in Kazakhstan for lost baggage on
international flights?
Yes, compensation for lost baggage
on international flights is paid ac-
cording to the rules of the two Con-
ventions signed by Kazakhstan – the
Warsaw and Montreal Conventions
– as well as in accordance with the
internal rules of the companies.
Is it true that compensation is paid
in Kazakhstan for lost baggage on
international flights?
It is completely true that compen-
sation is paid in Kazakhstan for lost
baggage on international flights. The
compensation is calculated and paid
based on the two Conventions signed
by Kazakhstan (the rules of the War-
saw and Montreal Conventions) and
the internal regulations of the com-
panies.
G
Қазақстанда қандастарға азамат-
тық
алудың
шарттары
туралы
түсiндiрiңiз.
Қандастар
Қазақстан
аумағын-
да тұру мерзiмiне қарамастан
жеңiлдетiлген тәртiпте азаматты-
қты ала алады. Олар бұрынғы
азаматтықтан бас тарту туралы
нотариат
куәландырған
өтiнiш,
бекiтiлген нысандағы сауалнама-
өтiнiш, шарттарды сақтау тура-
лы мiндеттеме, өмiрбаян, жеке ба-
сын куәландыратын және адам-
ның басқа елдiң азаматтығына
жататындығын растайтын құжат-
тың көшiрмесi, қандастың куәлiгi
және төрт фотосурет секiлдi құ-
жаттарды тапсыруы керек.
Қандастар Қазақстан Республика-
сының азаматтығын алу үшiн не
iстеу керек?
Қандастардың Қазақстан Респуб-
ликасында тұрған мерзiмiне қара-
мастан олардың азаматтық алуы
жеңiлдетiлген тәртiппен жүзеге
асады. Қандастар Қазақстан Рес-
публикасының азаматтығын алу
үшiн бұрынғы азаматтықтан бас
тарту туралы нотариат куәлан-
дырған өтiнiш, бекiтiлген нысан-
дағы сауалнама-өтiнiш, шарттар-
ды
сақтау
туралы
мiндеттеме,
өмiрбаян, жеке басын куәландыра-
тын және адамның басқа елдiң аза-
маттығына жататындығын растай-
тын құжаттың көшiрмесi, қанда-
стың куәлiгi және төрт фотосурет
секiлдi құжаттарды тапсыруы ке-
рек.
Explain the conditions for obtain-
ing citizenship for oralmans (ethnic
Kazakhs) in Kazakhstan.
Oralmans (ethnic Kazakhs) can ob-
tain citizenship in a simplified man-
ner regardless of the duration of their
stay in Kazakhstan. They need to
submit a notarized application to re-
nounce their previous citizenship, a
completed application form in the
approved format, a commitment to
comply with the conditions, an au-
tobiography, a copy of a document
confirming their identity and lack of
foreign citizenship, a certificate of
oralman status, and four passport-
sized photos.
What should oralmans (ethnic Kaza-
khs) do to obtain citizenship of the
Republic of Kazakhstan?
Oralmans (ethnic Kazakhs) can ob-
tain citizenship in Kazakhstan re-
gardless of the duration of their stay
in a simplified manner. To obtain
Kazakhstani citizenship, they must
submit a notarized application to re-
nounce their previous citizenship, a
completed application form in the
approved format, a commitment to
comply with the conditions, an au-
tobiography, a copy of a document
confirming their identity and lack of
foreign citizenship, a certificate of
oralman status, and four passport-
sized photos.
Table 9: Example of annotation for GovSet.

--- Page 19 ---

G.2
CultSet
Type
Instruction
Output
Updated Instruction
Updated Output
C
Фильмнiң
қандай
жетiстiктерi
болды?
«Транссiбiр
экспресi»
фильмi
1978
жылы
Ереванда
өткен
Бүкiлодақтық
кинофестивальда
’ең
үздiк
шытырман
оқиғалы
фильм
үшiн’
сыйлығын
алды.
Сондай-ақ,
Карловы
Варыда
өткен 21-Халықаралық кинофе-
стивальда Азия, Африка және
Латын
Америкасы
елдерiнiң
симпозиумы
қазылар
алқасы-
ның сыйлығына ие болды. 1978
жылы
режиссер
Оразбаев
пен
суретшi Қарсақбаевқа Қазақстан
Мемлекеттiк сыйлығы берiлдi.
"Транссiбiр
экспресi"атты
қа-
зақстандық
фильмнiң
қандай
жетiстiктерi болды?
«Транссiбiр
экспресi»
фильмi
1977 жылы Қазақфильм студия-
сы тарабынан шықты. 1978 жылы
ол Ереванда өткен Бүкiлодақтық
кинофестивальда "Ең үздiк аван-
тюра фильмi үшiн"сыйлығын ал-
ды. Бұдан гөрi, Карловы Вары-
да өткен 21-Халықаралық кино-
фестивальда Азия, Африка және
Латын Америкасы елдерiнiң сим-
позиумы қазылар алқасының сый-
лығына да ие болды. 1978 жылы
фильм режиссерi Оразбаев пен су-
ретшiсi Қарсақбаевқа Қазақстан
Мемлекеттiк сыйлығы берiлдi.
What achievements did the film
have?
The film "Trans-Siberian Express"
received the award for "Best Adven-
ture Film" at the World Film Festival
held in Yerevan in 1978. Addition-
ally, it won a prize at the 21st In-
ternational Film Festival in Karlovy
Vary, as well as at the symposium
of Asia, Africa, and Latin American
countries. In 1978, the film’s direc-
tor, Orazbayev, and cinematographer
Karasbayev were awarded the State
Prize of Kazakhstan.
What achievements did the Kaza-
khstani film "Trans-Siberian Ex-
press" have?
The film "Trans-Siberian Express"
was released in 1977 by the Kaza-
khfilm studio. In 1978, it received
the award for "Best Adventure Film"
at the World Film Festival in Yere-
van. Later, it also won a prize at the
21st International Film Festival in
Karlovy Vary and at the symposium
of Asia, Africa, and Latin American
countries. In 1978, the film’s direc-
tor, Orazbayev, and cinematographer
Karasbayev were awarded the State
Prize of Kazakhstan.
C
Қазақ
халқының
музыкалық
мұрасы қалай дамыды?
Қазақ
халқының
музыкалық
мұрасы ғасырлар бойы ауыздан-
аузға,
ұстаздан-шәкiртке
жет-
кiзiлiп, көшпендi өмiр салтының
ықпалымен
дамыды.
Музыка-
лық дәстүрлер батырлық және
лирикалық жанрдағы эпостарды
қамтыды. Қазақ композиторлары
әлемдiк деңгейде танымал болып,
ұлттық
музыкалық
мәдениеттi
дамытуда үлкен үлес қосты.
Қазақ
халқының
музыкалық
мұрасы қалай дамыды?
Қазақ
халқының
музыкалық
мұрасы ғасырлар бойы ауыздан-
аузға,
ұстаздан-шәкiртке
жет-
кiзiлген. Негiзiнен көшпендi өмiр
салтының
ықпалымен
дамыды.
Қазақтың
музыкалық
дәстүрi
батырлық және лирикалық жанр-
дағы эпостарды қамтыды. Қазiргi
заманда қазақ композиторлары
әлемдiк деңгейде танымал болып,
ұлттық
музыкалық
мәдениеттi
одан әрi дамытуға үлкен үлес
қосып жүр.
How did the musical heritage of the
Kazakh people develop?
The musical heritage of the Kazakh
people developed over centuries
through oral transmission, from mas-
ter to apprentice, and was influenced
by the nomadic lifestyle. Musical
traditions included epic genres of
heroic and lyrical works. Kazakh
composers became renowned inter-
nationally and contributed signifi-
cantly to the development of national
musical culture.
How did the musical heritage of the
Kazakh people develop?
The musical heritage of the Kazakh
people developed over centuries
through oral transmission, from
master to apprentice, primarily in-
fluenced by the nomadic lifestyle.
Kazakh musical traditions encom-
passed genres of epic heroic and
lyrical works.
In modern times,
Kazakh composers have gained in-
ternational recognition and continue
to contribute greatly to the develop-
ment and advancement of national
musical culture.
C
Киiз үйде түндiк дегенiмiз не
екенiн түсiндiрiңiз.
Түндiк — киiз үйдiң шаңырағы-
на жабылатын киiз, ол әрi жарық
бередi, әрi түтiн шығуға мүмкiн-
дiк бередi. Төртбұрышты түрде пi-
шiлiп, шаңырақ диаметiрiнен 50-
60 сантиметрдей артық жасалады.
Қазақ халқының киiз үйiндегi
түндiктiң не екенiн түсiндiрiңiз.
Түндiк — қазақтың баспанасы
киiз үйдiң шаңырағына жабыла-
тын киiз. Ол әрi iшке жарық өт-
кiзедi, әрi түтiн шығуына мүмкiн-
дiк бередi. Төртбұрышты түрде пi-
шiлiп, шаңырақ диаметiрiнен 50-
60 сантиметрдей артық етiп жаса-
лады.
Explain what "tundik" means in a
Kazakh yurt.
The "tundik" is the felt cover placed
on the top of the yurt, which pro-
vides insulation and allows smoke
to escape. It is made slightly larger
than the circular roof opening, with
a diameter exceeding 50-60 centime-
ters. It is triangular in shape.
Explain what "tundik" means in the
Kazakh yurt.
The "tundik" is the felt cover placed
on the top of the Kazakh yurt.
It serves as insulation and allows
smoke to escape.
It is triangular
in shape and is made slightly larger
than the circular roof opening, with
a diameter exceeding 50-60 centime-
ters.
Table 10: Example of annotation for CultSet.

--- Page 20 ---

H
Annotator Comments
H.1
GovSet
Error Type
Annotator Comments
S
The generated data constantly uses an unnatural sentence structure that sounds like this: Сiз сәбиiңiздiң дүниеге келуiн күтудесiз және
онлайн режимiнде емханаға тiркелу үдерiсiн түсiндiрiңiзшi. Here the word және sounds extra and can be either eliminated or replaced
with бұл жағдайда. This example of a sentence with extra және is common.
G
Inconsistent verb forms in instructions. Like түсiндiру instead of түсiндiрiңiз.
G
The generated data has two verb forms like тану and танылу. If the first one is the action of subject, the second is an action that happens TO a
subject/object.
S
There is a frequent unnatural sentence structure that sounds like this: Бұл рас па: некеге тұрған адамдарға куәлiк электрондық нысанда
берiледi? Either the whole statement needs to be reconstructed or ме should be added at the end of the sentence.
G
The model frequently fails to change words to accusative case (add – н/- ын/-iн). For example, in the phrase тегi өзгертуге бола ма, the correct
form would be тегiн өзгертуге бола ма.
G
The translator often does not differentiate кезiнде and кезiндегi. For example, in the sentence Некенi бұзу кезiнде құжаттарды ресiмдеу
туралы түсiндiрiңiз, the correct word would be кезiндегi. The same happens with Қазақстанда and Қазақстандағы.
L
The model writes the word айырлуы several times. It must be either айырылуы or айырылғаны correctly.
S
The model frequently writes a phrase жүзеге асырылады, which sounds unnatural and must be жүзеге асады instead.
G
The model frequently used phrases like кiрмейдi екенiн, when the correct form for any verb there would be кiрмейтiнiн.
G
The model constantly uses this phrasing: дегенiмiз не екенiн түсiндiрiңiз. It sounds unnatural and must be replaced either with не екенiн
түсiндiрiңiз or just дегенiмiз не?
G
The model cannot differentiate question words like ма, ме etc. It can write мiндеттi ма?, which is used in verbal speech only. The correct form
would be мiндеттi ме?
G
The model can miss letters. For instance, мақсатары instead of мақсаттары; it is also not connected with the original text because the word is
not even used there.
S
There is a common sentence structure that sounds like this: Тұрмыстық зорлық-зомбылық жағдайында қандай медициналық көмек алу
жолдарын айтыңыз. Either the word қандай must be removed and -ғы added to жағдайында (жағдайындағы), or the statement must be a
question instead, like қандай медициналық көмек алуға болады?
G
Әр түрлi must be written as әртүрлi. Марапат must be used instead of награда.
S
There are many sentences like Шындық па, үйде арнайы әлеуметтiк қызметтердi көрсету тоқтатылады, егер қызмет алушының өзi
олардан бас тартса? The structure is wrong, шындық па must be placed at the end!! And егер etc. must be placed at the start. Any verb
before шындық па must end with -тыны/-тiнi.
G
The model often writes деп түсiндiрiңiз in instructions. In different occasions it must be written differently, like бола ма, түсiндiрiңiз or
болатынын түсiндiрiңiз.
G
Incorrect translation for процесс. It should be translated as үдерiс/үрдiс.
L
Sentences like Жеке куәлiктi алғаш алу үшiн қандай құжаттар қажет екенi рас па? are common in “Is it true that” instructions. Either
қандай must be removed or replaced with a list of documents.
L
The model generates a phrase өтiнiш жасау; the more common version would be өтiнiш беру or өтiнiш жазу.
G
The model sometimes has a hard time differentiating active and passive positions of subjects. For example, тiркеу куәлiгi немесе әскери билет
жоғалтқанда puts the verb as if the subject is passive, whereas the correct form would be жоғалғанда (because the subjects are in active form).
This happens with different verbs throughout the document.
G
Sometimes the answers that the model generates for instructions are not even connected to the question. For example, the answer for Өтiнiш
берушi ұсынылған ақпарат үшiн қашан жауап бередi деген айтылды ма? is Иә, өтiнiш берушiлер ұсынылған ақпарат үшiн өздерi
жауап бередi деп айтылды. The word өздерi as an answer is unrelated to the question қашан.
L
The model frequently generates phrases like осы мәтiн бойынша, бұл деректерге қарағанда, which implies that there is a certain text to rely
on.
L
The model sometimes pronounces Беларусь as Беларуссия, which is not correct even unofficially. For formal texts, Беларусь should be used,
or at least Белоруссия.
L
The model frequently uses the Russian word заем, even though there are Kazakh translations for it, such as несие or қарыз. This happens
because of the original text.
S
Sometimes the model generates sentence structures like Бұл рас па: Азамат 16 жасқа толғанда Қазақстанның әрбiр азаматы жеке
куәлiк алуға мiндеттi екенiн? Firstly, the word екенiн in all these sentences is grammatically incorrect here and must be екенi. Additionally,
since this sentence structure is very frequent, it must be reconstructed to place бұл рас па at the end. For example, it should sound like this: 16
жасқа толғанда Қазақстанның әрбiр азаматы жеке куәлiк алуға мiндеттi екенi рас па?
S
There are also sentences that start with шынайы ма екенiн анықтаңыз or шындық па анықтаңыз. These phrases must be rewritten as either
шындық па, соны анықтаңыз or just шын ба/шындық па without the анықтаңыз part.
G
The model cannot identify where it is better to not use табыс септiк. For example, пәтердi iздеу/пәтердi iздегенде is used frequently, but the
common and natural way must be without the -дi suffix.
Table 11: Selected annotator comments highlighting issues in GovSet. Error types are categorized as follows: L –
Lexical errors, S – Structural errors, G – Grammatical errors.

--- Page 21 ---

H.2
CultSet
Error Type
Annotator Comments
G
Inconsistent verb forms are present in the generated data. For example, түсiндiр is used instead of түсiндiрiңiз.
G
The generated data includes phrases such as "... туралы сипаттаңыз," which is grammatically incorrect because туралы is redundant.
S
Phrases like "... қалай сипатталады?" appear awkward and imply the presence of external text for context.
L
The word карьера is used instead of the correct Kazakh term мансап.
G
The word әртүрлi is written as әр түрлi, which is inconsistent with standard formatting.
G
There is confusion regarding whether -мен (-бен, -пен) should be attached to or separated from nouns.
G
The form of жылдары is inconsistent, alternating between жылы, жылдары, or abbreviated forms like ж. or жж..
L
Russian words, such as награда, карьера, and музей, are used even though Kazakh equivalents exist.
L
The word артис is used instead of the correct Kazakh term әртiс.
S
Words like бастап and берi are omitted when referring to years. For example, 1967 жылдан ол бұл атаққа ие болды.
G
The phrase туралы түсiндiрiңiз is unnatural and often incorrect. It should be replaced with туралы айтыңыз or айтып берiңiз.
G
The phrase жеңiл атлетшi is used correctly, but ауыр атлет is written without the suffix -шi. It should be standardized as атлетшi.
L
Shortened names and surnames are written without spaces. For example, Ы.Алтынсарин instead of Ы. Алтынсарин.
L
The phrase рөл ойнады is a direct translation from Russian and should be replaced with рөл орындады or рөл сомдады.
L
Years are written in abbreviated forms, such as 1973-78, omitting 19 in the second part.
L
Names of ру, tribes (тайпа), and жүз are written in lowercase, which is inconsistent with standard capitalization rules.
L
The word рөл is occasionally misspelled as рол or роль.
G
Verbs ending with -ып or -iп are used incorrectly, leading to unrelated sentences. For example, in the sentence Бұл ойын үлкен тойларда
арнайы жүлде тағайындалып өткiзiлiп, оның түрлерi көптеген, the part after өткiзiлiп is unrelated. The correct form would be Бұл
ойын үлкен тойларда арнайы жүлде тағайындалып өткiзiледi; оның түрлерi көп or Бұл ойын үлкен тойларда арнайы жүлде
тағайындалып өткiзiлiп, қазақ халқында әлi де жүргiзiлiп келедi.
S
Words occasionally appear in the Latin alphabet even though they are not written in Latin in the original text.
G
Sentences like Безендiрудiң көркемдеу құралдарын қандай өнер салалары пайдаланады деп түсiндiрiңiз are included. The common error
is the use of пайдаланады деп түсiндiрiңiз, which should be replaced with пайдаланатынын түсiндiрiңiз.
G
The phrase жер аударылды is used for referring to a person. If it describes someone moving places, it should be corrected to жер аударды.
S
The structure of the questions deviates from the natural structure of the Kazakh language. For example: Бұл рас па, АХҚО қатысушыларының
қызметiн реттеу Англия мен Уэльстiң жалпы құқық қағидаттары негiзiнде жүргiзiледi?
S
The questions ask for information not mentioned in the text, meaning the answer to the question is not present in the text.
S
The structure of the questions is entirely incorrect. For example: Астана Халықаралық Қаржы Орталығы қандай компаниялар үшiн реттеуге
икемдi тәсiл қолданады? The correct version: Астана Халықаралық Қаржы Орталығы қандай компанияларды реттеуге мүмкiндiк бередi?
L
The word ол is overused in the generated data.
Table 12: Selected annotator comments highlighting issues in CultSet. Error types are categorized as follows: L –
Lexical errors, S – Structural errors, G – Grammatical errors.
I
Categories Explained

--- Page 22 ---

Category
Description
Legal Assistance
Services related to providing legal advice, resolving disputes, or ensuring compliance with laws in areas such as
property rights, labor law, or civil matters.
Healthcare
Includes services for accessing healthcare facilities, obtaining health insurance, and managing public health
initiatives, including vaccinations and medical records.
Real Estate
Covers registration of property rights, encumbrances, and the legal transfer of property ownership.
Education
Involves services for school and university admissions, recognition of diplomas, and access to government scholar-
ships or grants.
Family
Services addressing marriage registration, child adoption, and other family-related matters like child welfare and
maternity benefits.
Taxes and Fines
Includes filing taxes, obtaining tax statements, and paying administrative fines or penalties.
Business Registration
Covers the process of starting, registering, or closing businesses, including obtaining licenses and permits.
Benefits, Allowances, and Pension
Government services related to social welfare benefits, pensions, and financial aid for citizens.
Employment and Job Placement
Services that facilitate job searches, vocational training, and unemployment benefits.
Driving and Transportation
Includes services for driver’s license issuance, vehicle registration, and public transportation systems.
ID Card, Passport, and Registration
Involves obtaining or renewing identity documents, passports, and residency registration.
Industry
Services supporting industrial development, including subsidies, licenses, and monitoring compliance with regula-
tions.
Financial Literacy
Government initiatives to improve citizens’ understanding of personal finance, savings, and investment.
Consular Services
Services provided to citizens abroad, such as visa issuance, document legalization, and emergency support.
Travel, Living Abroad, and Emigration
Addresses issues like emigration permits, citizenship renunciation, and support for expats.
Licensing and Accreditation
Involves issuing licenses for various professional or business activities and accrediting institutions.
Obtaining Citizenship
Covers processes for naturalization, renouncing, or restoring Kazakh citizenship.
Special Services
Includes unique or niche government-provided services that do not fall into other categories.
Military Registration
Services related to military service registration, deferments, and exemptions.
Population
Addresses population census activities, demographic statistics, and citizen registration systems.
Religion
Involves registration and oversight of religious organizations and facilitation of religious freedom policies.
Table 13: Category explanation for GovSet.
Category
Description
Literature and Writing
This category includes Kazakh literature, poetry, and contemporary works.
Culture and Traditions
Covers Kazakh cultural practices, including traditional music, dances, festivals, and customs.
Media and Communication
Includes Kazakhstan’s media landscape, featuring national TV channels, news outlets.
Arts and Entertainment
Encompasses visual arts, theater, film, and music.
Education and Academia
Covers the education system in Kazakhstan, including primary to higher education.
History and Archaeology
Includes the exploration of Kazakhstan’s ancient sites and the history of the Kazakh people.
Politics
Encompasses the political landscape of Kazakhstan, including its government, political parties, and international
relations, with a focus on its role in Central Asia.
Sciences and Humanities
Includes research and advancements in fields such as environmental science, economics, sociology, and the study of
Kazakh identity and history.
Historical Figures
This category celebrates important figures in Kazakhstan’s history.
Sports and Recreation
Covers popular sports in Kazakhstan like boxing, wrestling, football, traditional Kazakh sports and famous
Kazakhstani athletes.
Culinary and Food
This includes Kazakhstan’s traditional cuisine, such as "beshbarmak" and "kymyz".
Health and Medicine
Covers public health systems, advancements in medical care and renowned Kazakh doctors.
Business and Industry
This category encompasses Kazakhstan’s growing economy, with a focus on industries like oil and gas, agriculture,
and its expanding IT sector.
Cultural Institutions
Includes museums, galleries, theaters, and cultural centers in Kazakhstan, such as the National Museum of
Kazakhstan and the Astana Opera.
Transportation and Infrastructure
Covers the country’s infrastructure development, such as its extensive rail system, airports.
Nature and Environment
Focuses on Kazakhstan’s diverse landscapes, such as the steppes, mountains, and lakes.
Miscellaneous
A catch-all category that could include any other cultural, social, or historical aspects of Kazakhstan not covered by
other categories.
Table 14: Category explanation for CultSet.

--- Page 23 ---

J
Example of created data
Category
Instruction
Output
Benefits,
allowances,
and pensions
Қазақстанда зейнетақы төлем-
дерiн есептеудiң барлық қадам-
дарын тiзбектеңiз.
1. Табыс қатарынан 36 күнтiзбелiк ай iшiндегi жалпы соманы алыңыз. 2. Оны отыз алтыға бөлiңiз. 3. Жасына
байланысты зейнетақы төлемдерiн есептеуге арналған кiрiс, республикалық бюджет туралы заңда тиiстi
қаржы жылына белгiленген айлық есептiк көрсеткiштiң 55 еселенген мөлшерiнен аспауға тиiс.
List all the steps for calculating
pension payments in Kazakhstan.
1. Take the total amount of income for 36 calendar months in a row. 2. Divide it by thirty-six. 3. Income for
calculating pension payments by age should not exceed 55 times the monthly calculation index established for the
corresponding financial year by the Law on the Republican budget.
Business registration
Бұл
жоба
қандай
мақсатқа
бағытталғанын түсiндiрiңiз.
"Zhas Project бұл әлеуметтiк жобалар мен бизнес-идеяларды қаржыландыру арқылы осал топтарды, әсiресе
ауылдық жерлерде тұратын жас қазақстандықтарды қолдауға бағытталған бiрегей жоба. Жоба жастарды өз
қоғамының әлеуметтiк-экономикалық өмiрiне тартуға және нәтижелi жұмыспен қамтуға көмектеседi.
Explain the purpose of this
project.
"Zhas Project" is a unique project aimed at supporting vulnerable groups, especially young Kazakhstanians living in
rural areas, through the financing of social projects and business ideas. This project helps to involve young people
in the socio-economic life of their society and ensures productive employment.
Consular services
Қазақстанның шетелдегi заң-
дастыру процесiне жеке және
заңды
тұлғаларға
арналған
құжаттардың
ұқсастықтары
мен айырмашылықтарын си-
паттаңыз.
Ұқсастықтары: Екi жағдайда да еркiн нысандағы өтiнiш, заңдастыруға жататын құжат, және консулдық
алымның төленгенiн растайтын құжат талап етiледi. Айырмашылықтары: Жеке тұлға үшiн жеке басын
куәландыратын құжаттың көшiрмесi қажет, ал заңды тұлға үшiн уәкiлеттi тұлғаның куәландыратын құжаты
қажет. Заңды тұлға үшiн қосымша заңды тұлғаның мемлекеттiк тiркелгенiн (қайта тiркелгенiн) растайтын
құжат немесе заңды тұлғаның әрекет қабiлеттiлiгiн растайтын өзге де құжаттар талап етiледi.
Describe the similarities and dif-
ferences between documents for
natural persons and legal enti-
ties in the legalization process of
Kazakhstan abroad.
Similarities: in both cases, an application in any form, a document subject to legalization, and a document confirming
the payment of the consular fee are required. Differences: for a natural person, a copy of an identity document is
required, and for a legal entity, a certificate of an authorized person is required. For a legal entity, an additional
document confirming the state registration (re-registration) of a legal entity or other documents confirming the legal
capacity of a legal entity is required.
Driving and transporta-
tion
Транзиттiк декларация көшiр-
мелерiнiң талап етiлетiн жағ-
дайын түсiндiрiңiз.
Транзиттiк декларация ретiнде пайдаланылатын құжаттар, мысалы, көлiктiк (тасымалдау) құжат, негiзгi
құжат болып табылады, ал басқа құжаттар оның ажыратылмас бөлiгi ретiнде қарастырылады.
Explain the required status of the
transit declaration copies.
Documents used as a transit declaration, for example, a transport (transportation) document, is the main document,
while other documents are considered as its inalienable part.
Education
«Болашақ» бағдарламасы бой-
ынша оқуға түсерде қандай құ-
жаттарды алып келу керек?
1. Стипендиаттың жеке басын куәландыратын құжат. 2. Жұмыс берушi атынан оқу/тағылымдамадан өту
шартына қол қоятын адамның өкiлеттiгiн куәландыратын құжаттар. 3. Стипендиаттың ауылдық елдi мекен-
дерде тұрақты тұрғылықты жерi туралы мәлiметтер.
What
documents
should
be
brought when entering the Bo-
lashak program?
1. A document verifying the identity of the scholarship holder. 2. Documents certifying the authority of the person
signing the studying/internship agreement on behalf of the employer. 3. Infromation on the permanent place of
residence of the scholarship holder in rural settlements.
Employment
and
job
placement
«Бастау Бизнес» онлайн курсы-
ның ұзақтығы қанша күн бола-
тынын сипаттаңыз.
Оқу 14 күнтiзбелiк күннен аспайды.
Describe how many days the on-
line course "Bastau Business"
will last.
Training lasts no more than 14 calendar days.
Family
Алимент төлеу рәсiмi туралы
айтып берiңiз.
Алимент төлеу рәсiмi – бұл ата-аналардың баланы асырап-бағуға арналған төлемдер бойынша мiндеттеме-
лерiн орындауға байланысты процесс. Бұл ең көп таралған алимент жағдайы ретiнде белгiлi.
Tell about the procedure for pay-
ing alimony.
The alimony payment procedure is a process related to the fulfillment by parents of their child-support obligations.
This is known as the most common case of alimony.
Financial literacy
АХҚО-ның жасыл қаржыны да-
мыту бойынша жүргiзген жұ-
мыстарына нелер жатады?
АХҚО жасыл қаржыны дамыту үшiн әлеуеттi эмитенттерге, инвесторларға және нарық ойыншыларына
алғашқы көмек көрсетедi.
What is the work of the AIFC
on the development of green fi-
nance?
The AIFC provides first aid to potential issuers, investors and market players for the development of green finance.
Healthcare
Емханаға қалай жазылуға бола-
ды?
Жеке онлайн-сервистi пайдаланып немесе емхананың тiркеу бөлiмiне жүгiнiп, дәрiгердiң қабылдауына
жазылуға болады.
How can you make an appoint-
ment at the hospital?
You can make an appointment with a doctor using a personal online service or by contacting the registry office of
the hospital.
ID card, passport, and
registration
Жол жүру құжатын алу үшiн
қандай құжаттардың бiреуiн
көрсету қажет?
Жол жүру құжатын алу үшiн қажеттi құжаттардың бiреуiн көрсету қажет: туу туралы акт жазбасы, туу
туралы куәлiк, азаматтығы жоқ адамның куәлiгi, шетелдiк паспорт, босқын куәлiгi.
What documents do you need
to show to obrain a travel doc-
ument?
To obtain a travel document, it is necessary to show one of the necessary documents: a birth certificate record, a
birth certificate, a certificate of absence of citizenship, a foreign passport, a refugee certificate.
Table 15: Example of created instructions on GovSet.

--- Page 24 ---

Category
Instruction
Output
Industry
Жеңiл өнеркәсiптiң құрамын-
да қандай қосалқы салалар
бар?
Жеңiл өнеркәсiп 20-дан астам қосалқы салаларды қамтиды, олар тоқыма, тiгiн және былғары, терi, аяқ киiм
өндiрiстерi.
What sub-industries are part of
the light industry?
Light industry includes more than 20 sub-industries, these are textile, sewing and leather, shoe industries.
Legal assistance
Балалардың
интернетте
көп
уақыт өткiзуi рас па?
Иә, балалар мен жасөспiрiмдер интернетте көп уақыт өткiзедi.
Is it true that children spend a lot
of time on the internet?
Yes, children and teenagers spend a lot of time on the internet.
Licensing and accredita-
tion
Әуесқойлық аң аулауға куәлiк-
тi алу үшiн қандай құжаттар
қажет?
Келесi құжаттар ұсынылуы тиiс: жеке куәлiк, өлшемi 3х4см фотосурет (3 дана), аңшылық минимум курсын
аяқтау сертификаты, 2 АЕК мөлшерiнде мемлекеттiк бажды төлеу туралы түбiртектiң көшiрмесi.
What documents are needed to
obtain a certificate for amateur
hunting?
The following documents must be submitted: an identity card, a 3x4cm photo (3 pieces), a certificate of completion
of the hunting minimum course, a copy of the receipt for payment of the state duty in the amount of 2 MCI.
Military registration
2023 жылғы 16 қарашадан ба-
стап әскери есепке алу қағида-
ларына қандай өзгерiстер ен-
гiзiлдi?
2023 жылғы 16 қарашадан бастап бейбiт уақытта тiркеу туралы куәлiктер беру тоқтатылды, ал әскери билет-
тер әскери қызметтiң не құқық қорғау, арнаулы мемлекеттiк органдарда қызметтiң белгiленген мерзiмiнен
өткен адамдарға ғана берiледi.
What changes have been made to
the rules of military registration
since November 16, 2023?
Since November 16, 2023, the issuance of certificates of registration in peacetime has been suspended, and military
tickets are issued only to persons who have passed the established period of military service or service in law
enforcement, special state bodies.
Obtaining citizenship
Қазақстанның
ЖОО-да
оқи-
тын этникалық қазақтар аза-
маттықты жеңiлдетiлген тәр-
тiпте алады ма?
Иә, Қазақстанның ЖОО-да оқитын этникалық қазақтар азаматтықты жеңiлдетiлген тәртiпте алады.
Population
2023 жылы Қазақстанда қай
этникалық топ халықтың көп
бөлiгiн құрады?
2023 жылдың мәлiметтер бойынша, қазақтар халықтың көп бөлiгiн құрайды (70,6%).
Do ethnic Kazakhs studying at
universities in Kazakhstan re-
ceive citizenship in a simplified
prodecure?
Yes, ethnic Kazakhs studying at universities in Kazakhstan receive citizenship in a simplified prodecure.
Real estate
Кәмелетке толмаған адамның
өз мүлкiн басқара алуы шын-
дық па?
Жоқ, кәмелетке толмаған пәтер иесi 18 жасқа толғанға дейiн өз бетiнше мүлкiн басқара алмайды.
Is it true that a minor can manage
his/her property?
No, a minor apartment owner cannot independently manage his/her property until he/she reaches the age of 18.
Religion
Қазақстан
халқының
негiзгi
бөлiгi қандай дiндердi ұстана-
ды?
Елiмiзде халықтың негiзгi бөлiгi сунниттiк исламды ұстанатын мұсылмандар және орыс православтық
христиандықты ұстанушылар болып бөлiнедi.
What religions do the majority
of the population of Kazakhstan
practice?
In the country, the majority of the population is divided into Muslims professing Sunni Islam and adherents of
Russian Orthodox Christianity.
Special services
Мемлекеттiк органда қызмет-
тi алудағы қажеттi құжаттарды
түсiндiрiңiз.
Жеке басты куәландыратын, тұрақты тұрғылықты жерi бойынша тiркелгенiн растайтын құжаттар, мүгедек-
тiгi туралы және тиiстi мемлекеттiк ақпараттық жүйелерден мәлiметтер қажет. Аталған құжаттар Мемле-
кеттiк корпорацияның және жұмыспен қамту бөлiмдерiнiң бөлiмшелерi арқылы ЭЦҚ-мен куәландырылған
электрондық құжаттар нысанында алынады.
List the necessary documents in
receiving a service in a state
body.
Documents confirming registration at the place of permanent residence, disability information and information
from the relevant state data systems are required. These documents are obtained through the divisions of the State
Corporation and Employment Departments in the form of electronic documents certified by e-signature.
Taxes and fines
Eqonaq
жүйесiнде
шетелдiк
туристердiң келу мерзiмдерiн
сақтау үшiн қандай құрал ұсы-
нылады?
Шетелдiк туристердiң келу мерзiмдерiн сақтау үшiн Eqonaq жеке кабинетiнiң басты бетiнде көшi-қон
анықтамалығы ұсынылған.
What tool is offered in the
Eqonaq system to comply with
the deadlines for the arrival of for-
eign tourists?
To comply with the deadlines for the arrival of foreign tourists, a migration guide is provided on the main page of
the Eqonaq personal account.
Travel,
living abroad,
and emigration
Қазақстан
Республикасының
азамттығынан шығу үшiн та-
лап етiлетiн негiзгi шарттарды
түсiндiрiңiз.
Қазақстан Республикасының азамттығынан шығу үшiн негiзгi шарттар: азаматтың мемлекет алдында атқа-
рылмаған мiндеттерi, қылмыстық жауапкершiлiкке тартылмауы, және азаматтықтан шығудың мемлекеттiк
қауiпсiздiк мүдделерiне қайшы келмеуi тиiс. Егер осы шарттардың бiрi бұзылса, азаматтықтан шығуға
өтiнiш қабылданбайды.
Explain the basic conditions re-
quired to renounce citizenship of
the Republic of Kazakhstan.
The main conditions for renouncing the citizenship of the Republic of Kazakhstan are: unfulfilled duties of a citizen
to the state, non-involvement in criminal liability, and non-renouncing citizenship should not contradict the interests
of State Security. If one of these conditions is violated, the application for renunciation of citizenship will not be
accepted.
Table 16: Example of created instructions on GovSet.

--- Page 25 ---

Category
Instruction
Output
Arts and Entertainment
Қазақ композиторы мен этно-
музыканты Едiл Сейiлханұлы
Құсайыновтың қандай атқары-
лымды еңбектерi бар екенiн
түсiндiрiңiз.
Едiл Сейiлханұлы Құсайынов — «Қобыз» кафедрасының оқытушысы, түрлi ансамбльдер мен оркестрлерге
арналған музыкалық шығармалардың, сондай-ақ «Көкбөрi-Күлтегiн» балетiнiң, «Құрақ көрпе», «Келiн» ки-
нофильмдерiнiң музыкасының авторы. Ол «Алтай-Тарбағатай өңiрiнiң сыбызғы күйлерi» кiтабының авторы,
Қазақстан Республикасының Мәдениет Қайраткерi атанған.
Explain what are the works of
the Kazakh composer and eth-
nomusician Edil Seilkhanuly Ku-
sainov.
Edil Seilkhanuly Kusainov is an instructor at the "Kobyz" Department, the author of musical compositions for
various ensembles and orchestras, as well as music for the "Kokbori-Kultegin" ballet, and the "Kurak Korpe",
"Kelin" movies. He is the author of the book "Altai-Tarbagatai onirinin sybyzgy kuileri" (Sybyzgy Kuys of the
Altai-Tarbagatai region), and a cultural figure of the Republic of Kazakhstan.
Business and Industry
Қазақтың кен инженерi мен
бұрынғы Түпқараған ауданы-
ның әкiмi Әлiмғали Нұржанұ-
лы Қапуовтың қызмет жолын
сипаттаңыз.
Әлiмғали Нұржанұлы Қапуов – кен инженерi, бұрынғы Түпқараған ауданының әкiмi. 1948 жылы Форт-
Шевченко қаласында туған. ҚазПТИ-дi 1972 жылы бiтiрген. 1972-2005 жылдары әртүрлi қызметтер
атқарған: Жетiбай, «Ембiмұнай» карьерiнде, «Маңғыстау ұлутас» өндiрiстiк бiрлестiгiнде, «Маңғышлақ
ауылқұрылыс-12» тресiнде, «Маңғыстаумұнайқұрылыс» тресiнде, «Өзен» фирмасында және тағы басқа
орындарда қызметте болған. 2006 жылдан бастап «Құбыр» ЖШС-нiң директоры. «Өзен мұнай кен орнына
40 жыл», «Қазақстан мұнайына 100 жыл» белгiлерiнiң иегерi.
Describe the career path of the
Kazakh mining engineer and for-
mer Akim of Tupkaragan district
Alimgali Nurzhanuly Kapuov.
Alimgali Nurzhanuly Kapuov - mining engineer, former Akim of Tupkaragan district. He was born in 1948 in
Fort Shevchenko. He graduated from KazPTI in 1972. In 1972-2005, he worked on various positions: in Zhetybai,
Embimunay quarry, Mangistau Ulutas Production Association, Mangyshlak auylkurylys-12 trust, Mangistaumu-
naykurylys trust, Ozen firm and others. Since 2006, he has been the director of Kubyr LLP. He is the recipient of
badges like "40 years of Uzen oil field", "100 years of Kazakhstan oil".
Culinary and Food
Қазақтың
ұлттық
тағамы
төстiктi дайындау қадамдарын
сипаттап берiңiз.
Төстiктi дайындау үшiн алдымен қойдың төс етiн құйқасымен бiрге алып, екiге бөледi. Оны iстiкке шаншып,
сексеуiл шоғына қақтайды. Кейiн төстiктi терiсiмен бiрге үйiтiп, тұздайды. Бiрнеше күн бойы күн тигiзбей
кептiредi, тұз сiңгеннен кейiн отқа қақтап пiсiредi.
Describe the preparation steps of
the Kazakh national dish tostik
(brisket).
To prepare tostik, first take the lamb brisket with the skin and cut it in half. Poke it with a skewer and fry it on saxaul
coal. Then singe the brisket together with the skin and salt it. It has to dry for several days with no sun exposure,
and after the salt is absorbed, cook it on fire.
Cultural Institutions
Қазақстандағы Отырар руха-
нияты мұражай-кiтапханасына
енген көне заман кiтаптары қа-
лай жасалғанын түсiндiрiңiз.
Көне заман кiтаптары қолмен қауырсын қаламмен жазылып, Тараз ешкiсiнiң терiсiне түсiрiлген. Терiлер
қаттап, түйеге тиеп тасымалданған, әрiптер өшпей, жүздеген жылдарға жетiп тұрған.
Explain
how
ancient
books,
which
are
included
in
the
Museum-Library of Otrar spir-
ituality in Kazakhstan,
were
created.
Ancient books were written by hand with a quill pen and drawn on the skin of a Taraz goat. When the skins got
hard, they were loaded on camels, the letters were not erased, they stayed for hundreds of years.
Culture and Traditions
Қазақ
халқының
зооморф-
тық ою-өрнектерi мен олар
бейнелейтiн
элементтердi
сипаттаңыз.
Қазақтың зооморфтық ою-өрнектерi жануарлар әлемiн бейнелейдi. Олардың iшiндегi ең кең тарағаны –
мүйiздердi бейнелеу. Мүйiз тәрiздi доғалы «қошқар мүйiз», «мүйiз», «қос мүйiз», «сынық мүйiз» тәрiздi
өрнектер кездеседi. Сонымен қатар, «түйе мойын», «құс қанаты», «қаз мойны» сияқты жануарлардың басқа
да дене мүшелерi бейнеленедi. Бұл өрнектер үй заттарын, жиһаз бен қару-жарақ бұйымдарын сәндейдi.
Describe the zoomorphic orna-
ments of the Kazakh people and
the elements they represent.
Kazakh zoomorphic ornaments represent the animal world. The most common of them is the depiction of horns.
There are horn-shaped arched patterns such as "koshkar muyiz" (ram’s horn), "muyiz" (horn), "kos muyiz" (double
horn), "synyk muyiz" (broken horn). In addition, other body parts of animals are depicted, such as "tuye moiyn"
(camel neck),"kus kanaty" (bird wing),"kaz moiny" (goose neck). These patterns adorn household items, furniture
and weapons.
Education and Academia
Қазақстан тiлтанушы ғалымы
Ысқақов Ахмеди Ысқақұлы-
ның қазақ тiлiн дамытудағы
үлесiн түсiндiрiңiз.
Ысқақов Ахмеди Ысқақұлы қазақ тiлтануының тарихы мен грамматикасы, лексика және оқыту методикасы
саласындағы зерттеулерiмен танымал болды. Ол «Қазақ тiлiнiң сөздiгi» мен «Абай шығармаларының сөздiгi»
сияқты шығармаларды құрастырып, «Абай тiлi сөздiгiн» (1968) басқарды. 200-ден астам ғылыми еңбектiң
авторы.
Explain
the
contribution
of
Kazakh
linguist
Akhmedi
Iskakov to the development of
the Kazakh language.
Iskakov Akhmedi Iskakuly became famous for his research in the field of history and grammar of Kazakh linguistics,
vocabulary and teaching methods. He wrote such works as the "Dictionary of the Kazakh language" and the
"Dictionary of Abai’s works", and headed the writing of the "Dictionary of the Abai language" (1968). He is the
author of more than 200 scientific papers.
Health and Medicine
Қазақстандық
хирург
пен
медицина
ғылымдарының
докторы
Абдоллаев
Шәдi-
бай
Нұрғазыұлының
кәсiби
жетiстiктерiн сипаттаңыз.
Абдоллаев Шәдiбай Нұрғазыұлы хирург, медицина ғылымдарының докторы және профессор. Ол Қазақ
КСР-iнiң еңбек сiңiрген дәрiгерi атағын алды. Бұл ғалымның негiзгi ғылыми-зерттеулерi жедел хирургияның
мәселелерiне бағытталған, әсiресе, ерте кезеңдегi релапаротомия және жүктi әйелдерге хирургиялық көмек
көрсету.
Describe
the
professional
achievements of the Kazakh
surgeon and Doctor of Medical
Sciences Abdollayev Shadibay
Nurgazyuly.
Abdollayev Shadibay Nurgazyuly is a surgeon, Doctor of Medical Sciences and professor. He received the title of
honored doctor of the Kazakh SSR. The main research of this scientist is focused on the problems of emergency
surgery, especially relaparotomy at an early stage and surgical care for pregnant women.
Historical Figures
Қазақ күйшi-композиторы Ма-
хамбет Бөкейхановтың Қаза-
қстан музыкалық мәдениетiне
қосқан үлесiн түсiндiрiңiз.
Махамбет Бөкейханов қазақ күйлерiн жаздырушы, композитор. Ол Құрманғазы, Дәулеткерей, Әлiкей си-
яқты күйшiлердiң мұрасын бiздiң заманға жеткiзiп, өзi де күй шығарған. 1933 жылы студенттердiң халық
аспаптары оркестрiн ұйымдастырып, ұлттық музыка аспаптарын жетiлдiру үшiн шеберханада жұмыс iстедi.
Оның еңбегi арқылы көптеген қазақ күйлерi заманымызға жеттi.
Explain
the
contribution
of
the
Kazakh
kuishi-composer
Makhambet Bukeikhanov to the
musical culture of Kazakhstan.
Makhambet Bokeikhanov is a composer of Kazakh kuis. He brought the legacy of such kui performers as
Kurmangazy, Dauletkerey, Alikey to our time and wrote kui himself. In 1933 he organized a student orchestra of
folk instruments and worked in a workshop to improve national musical instruments. Thanks to his work, many
Kazakh kuis have reached our time.
Table 17: Example of created instructions on CultSet.

--- Page 26 ---

Category
Instruction
Output
History and Archaeol-
ogy
Қазақ халқының Албан тайпа-
сының тарихи мекендеген жер-
лерiн сипаттаңыз.
Қазақ халқының Албан тайпасы негiзiнен Жетiсу өңiрiнде, әсiресе қазiргi Алматы облысының Кеген мен
Нарынқол аудандарында мекендеген. Олар Iле өзенiнiң сол жағында, Қырғыз шекарасына дейiнгi аймақта
және Верный мен Жаркент уездерiнде шоғырланған. Бұл аймақ Iле Алатауының биiк жоталарына дейiнгi
жерлердi қамтиды.
Describe the historical habitats of
the Albanian tribe of the Kazakh
people.
The Albanian tribe of the Kazakh people lived mainly in the Zhetysu region, especially in the Kegen and Narynkol
districts of the modern Almaty region. They were concentrated on the left side of the Ili River, in the region up to
the Kyrgyz border and in the Verny and Zharkent counties. This region covers lands up to the high ridges of the
Trans-Ili Alatau.
Literature and Writing
Қазақ ақыны Абайдың қазақ
қоғамындағы терiс пиғылдар-
ды қалай сынға алғанын си-
паттаңыз.
Абай қазақ қоғамындағы әдiлетсiздiк, парақорлық, арамзалық және ерiншектiк сияқты терiс қылықтарды
ашық сынға алады. Ол халықтың бiр-бiрiн аңдып, ұрлық жасап, шын келiсiмге жете алмайтынына назар
аударады. Ақын өнер, әдебиет және ғылымға көңiл бөлiп, қоғамдық тәрбиеге баса мән бередi.
Describe how the Kazakh poet
Abai criticized the negative as-
pects of Kazakh society.
Abai openly criticizes such wrongdoings in Kazakh society as injustice, bribery, dishonesty and laziness. He draws
attention to the fact that the people follow each other, steal and do not reach a true agreement. The poet pays
attention to art, literature and science, and pays special attention to public education.
Media and Communica-
tion
Гүлмира Әлiбекқызы Қаракө-
зованың
қазақ
журналисти-
ка саласындағы жетiстiктерiн
түсiндiрiңiз.
Гүлмира Қаракөзова - тәжiрибелi журналист. Ол «Возвращенные имена» (1997) арнайы репортаждары топ-
тамасының, «Паритет» (2002-2004) тележобасының және «Жұлдызды Астана» (2005 жылдан) радиожобасы-
ның авторы. 2004 жылдан бастап «Астана» радиосын басқарады. «Мәдениет қайраткерi» құрмет белгiсiмен
(2006) және «Астана» медалiмен (2008) марапатталған.
Explain the achievements of Gul-
mira Alibekkyzy Karakozova in
the field of Kazakh journalism.
Gulmira Karakozova is an experienced journalist. She is the author of a series of special reports "Returning names"
(1997), the TV project "The Parity" (2002-2004) and the Radio Project "Starry Astana" (since 2005). Since 2004,
she has been leading Astana radio. She was awarded the Badge of Honor "Madeniyet kairatkeri" (2006) and the
medal "Astana" (2008).
Miscellaneous
Қазақстан заңгерi мен еңбек
сiңiрген
прокуроры
Қабдол-
ла Досбалаұлы Төлегеновтың
өмiрiндегi
маңызды
қызмет-
тердi сипаттаңыз.
Қабдолла Досбалаұлы Төлегенов 1952 жылы туған. Ол 1975 жылы Ташкент мемлекеттiк университетiнiң заң
факультетiн бiтiрген. Әр жылдарда түрлi қызметтердi атқарған, соның iшiнде Шымкент, Алматы облыста-
рының прокуроры, ҚР Қауiпсiздiк кеңесiнiң Хатшылығы меңгерушiсiнiң орынбасары және басқалары. 2008
жылдан берi Шығыс Қазақстан облысының прокуроры. Ол «Құрмет» орденiмен және басқа медальдармен
марапатталған.
Describe the most important
job positions in the life of the
lawyer and honored prosecutor
of Kazakhstan Kabdulla Dosbal-
auly Tulegenov.
Kabdolla Dosbalauly Tolegenov was born in 1952. He graduated from the faculty of law of Tashkent State University
in 1975. Over the years, he held various positions, including prosecutor of Shymkent, Almaty regions, deputy head
of the Secretariat of the Security Council of the Republic of Kazakhstan and others. He is the prosecutor of the East
Kazakhstan region since 2008. He was awarded the Order "Kurmet" and other medals.
Nature and Environment
Қазақстандағы
Көлсай
көл-
дерiнiң ұлттық табиғи паркiн-
де кездесетiн ерекше өсiмдiк-
тердi сипаттаңыз.
Көлсай көлдерiнiң ауданында ерекше сирек кездесетiн өсiмдiктерден өрiк, Iле барбарисi, долана, Альберт
құртқашашы бар. Аудан экологиялық тұрғыдан таза және жабайы өсiмдiктерге бай. Бұл өсiмдiктердiң көбi
дәрiлiк қасиетке ие.
Describe the unique plants found
in the Kolsai Lakes National Nat-
ural Park in Kazakhstan.
In the area of Kolsai lakes, especially rare plants can be found - apricot, Ili barbaris, hawthorn, Iris albertii. The area
is ecologically clean and rich in wild plants. Many of these plants have medicinal properties.
Politics
Қазақстандық қоғам қайрат-
керi Нұрлан Жылқышиевтiң
өмiрбаяндық фактiлерiн сурет-
теңiз.
Нұрлан Жылқышиев 1953 жылы 3 мамырда Тараз қаласында туған. Ол Шымкент педагогикалық институ-
тын және Алматы ауыл шаруашылығы институтын бiтiрген. 1998 жылы АҚШ-тың Тынық мұхиты жағалауы
университетiнде философия докторы дәрежесiн қорғаған. Қабыланбек агрошарап компаниясының бас ди-
ректоры болып қызмет атқарған және 2004 жылдан парламенттiң мәжiлiс депутаты. Ол әртүрлi марапаттарға
ие болған, соның iшiнде ’Тың және тыңайған жерлердi игерудiң 50 жылдығы’ төсбелгiсi.
Describe the biographical facts of
the Kazakh public figure Nurlan
Zhylkyshiev.
Nurlan Zhylkyshiev was born on May 3, 1953 in Taraz. He graduated from the Shymkent Pedagogical Institute
and the Almaty Agricultural Institute. In 1998, he defended his doctorate in philosophy at the University of the
Pacific coast of the United States. He worked as the head director of the agro-processing company Kabylanbek and
since 2004 has been a deputy of the Mazhilis of the Parliament. He has received various awards, including the "50th
anniversary of the development of Virgin and fallow lands" badge.
Sciences and Humanities
Едiл Ерғожаұлы Ерғожинның
химия саласында Қазақстан-
ның
мемлекеттiк
сыйлығын
алғаны рас па?
Иә, Едiл Ерғожаұлы Ерғожин химия ғылымының докторы, профессор, Қазақстанның мемлекеттiк сыйлығы-
ның иегерi.
Is it true that Edil Yergozhauly
Yerhozhin received the State
prize of Kazakhstan in the field
of chemistry?
Yes, Edil Yergozhauly Yergozhin is a doctor of chemical sciences, professor, winner of the State prize of Kazakhstan.
Sports and Recreation
Қазақстандық
пауэрлифтер-
паралимпиадшы
Давид
Дег-
тярев
2020
жылғы
жазғы
Паралимпиада
ойындарында
қандай жетiстiктерге жеттi?
Қазақ пауэрлифтерi Давид Дегтярев 2020 жылғы жазғы Паралимпиада ойындарында 54 кг дейiнгi салмақ
дәрежесiнде жарысқа қатысып, 170 кг, 172 кг және 174 кг салмақтарды көтеру арқылы алтын медаль иегерi
атанды.
What
did
Kazakhstani
powerlifter-paralympian David
Degtyarev achieve at the 2020
Summer Paralympic Games?
Kazakh powerlifter David Degtyarev competed at the 2020 Summer Paralympic Games in the weight category up to
54 kg and became the holder of a gold medal by lifting weights 170 kg, 172 kg and 174 kg.
Transportation and In-
frastructure
Қазақстандағы Ақтау Халықа-
ралық Әуежайының тарихын
қысқаша сипаттаңыз.
Ақтау Халықаралық Әуежайы 1983 жылы ашылған және көптеген iрi жүк тиейтiн әуе кемелерiн қабылдауға
жабдықталған. 1996 жылы акционерлiк қоғам ретiнде құрылды. 2007 жылы жаңа жолаушылар терминалын
салу мен басқаруға келiсiм жасалды. 2009 жылы жаңа терминал пайдалануға берiлдi, ол сағатына 450
жолаушыға қызмет көрсетедi. Әуежай жаңғыртулар нәтижесiнде ТМД елдерi арасында үздiк әуежай атағын
алды.
Briefly describe the history of
Aktau International Airport in
Kazakhstan.
Aktau International Airport was opened in 1983 and is equipped to receive many large cargo aircraft. It was
established in 1996 as a joint stock company. In 2007, an agreement was signed for the construction and management
of a new passenger terminal. In 2009, a new terminal was put into operation, serving 450 passengers per hour. As a
result of the modernization, the airport received the title of the best airport among the CIS countries.
Table 18: Example of created instructions on CultSet.

--- Page 27 ---

K
Inner-annotator agreement
K.1
Inner-Annotator Agreement for Preliminary Study
Figure 7: Inner annotator agreement across annotators for correctness, completeness, and fluency, measured using
Pearson correlation.
K.2
Inner-Annotator Agreement for Generation Evaluation
Figure 8: Inner-annotator agreement for generation evaluation, measured using Cohen’s Kappa.

--- Page 28 ---

L
MCQ Examples
Question Set
Kazakh
English translation
Correct
Answer
Dastur
Тыйым деген не?
A) Қазақ халқының той рәсiмi
B) Қазақ халқының тәрбиелiк құралы
C) Қазақ халқының музыкалық құралы
D) Қазақ халқының аспап-құралы
What is a tiyim?
A) A Kazakh wedding ceremony
B) A Kazakh educational tool
C) A Kazakh musical instrument
D) A Kazakh musical instrument
B
Dastur
Белкөтерер тағамы қандай адамдарға арнап дай-
ындалады?
A) Жас адамдарға
B) Тiсi болмаған, тамақ жей алмаған адамдарға
C) Спортшыларға
D) Бала-шағаларға
What kind of people is Belkoterer food prepared
for?
A) Young people
B) People who have no teeth and cannot eat
C) Athletes
D) Children
B
Constitution
Конституция АДАМ ЖӘНЕ АЗАМАТ II бөлi-
мiнiң негiзгi мәнi қандай?
A) Адамдың қадiр-қасиетiн қорлау
B) Адамдың қадiр-қасиетiне қол сұғу
C) Адамдың қадiр-қасиетiне қол сұғылмайды
D) Адамдың қадiр-қасиетiн жою
What is the main idea of the Constitution’s Section
II, chapter on rights of people and citizens?
A) Insulting human dignity
B) Infringement on human dignity
C) Human dignity is inviolable
D) Destruction of human dignity
C
Constitution
Қазақстан Республикасының басқару нысаны
қандай?
A) Парламенттiк басқару
B) Президенттiк басқару
C) Монархиялық басқару
D) Федерациялық басқару
What is the form of government of the Republic of
Kazakhstan?
A) Parliamentary government
B) Presidential government
C) Monarchical government
D) Federal government
B
Human Rights and
Society
ҚР Парламент Мәжiлiсi депутаты болу үшiн
қойылатын талаптарды атаңыз
A) он жыл еңбек өтiлi
B) елу жастан аспау
C) жоғары бiлiм
D) жиырма беске толу
What are the requirements for becoming a deputy
of the Mazhilis of the Parliament of the Republic of
Kazakhstan?
A) ten years of work experience
B) not older than fifty years
C) higher education
D) twenty-five years of age
D
Human Rights and
Society
Он алты жастан он сегiз жасқа дейiнгi қызмет-
керлер үшiн жұмыс уақытының ұзақтығы апта-
сына аспауы тиiс:
A) 36 сағаттан
B) 32 сағаттан
C) 24 сағаттан
D) 34 сағаттан
For employees aged sixteen to eighteen, the working
hours per week shall not exceed:
A) 36 hours
B) 32 hours
C) 24 hours
D) 34 hours
A
Table 19: Examples of MCQ.

--- Page 29 ---

M
Example of conversational data
Kazakh
English translation
Person 1 says: Қазақстанда жылжымайтын мүлiк алу және
сату кезiнде заңдық талаптар маңызды рөл атқарады. Бұл
процесс кейде ұзаққа созылуы мүмкiн, әсiресе, меншiк
иелерi бiрнешеу болған жағдайда.
Person 1 says: In Kazakhstan, legal requirements play an
important role when buying and selling real estate. This pro-
cess can sometimes be prolonged, especially when there are
multiple property owners.
Person 2 says: Иә, әсiресе, мүлiктi мұрагерлiк жолмен
алған жағдайда немесе кәмелетке толмаған бала иелiк ет-
кенде қосымша құжаттар талап етiледi.
Person 2 says: Yes, especially when the property is inherited
or owned by a minor, additional documents are required.
Person 1 says: Қазақстандағы жылжымайтын мүлiктiң са-
тып алу-сату үрдiсi өте маңызды болып табылады. Сiз
бiлесiз бе, кәмелетке толмаған баланың мүлкiн сату үшiн
қандай құжаттар қажет?
Person 1 says: The process of buying and selling real estate in
Kazakhstan is very important. Do you know what documents
are required to sell the property of a minor?
Person 2 says: ...
Person 2 says: ...
Gemma’s response: "...Кәмелетке толмаған баланың мүл-
кiн сату үшiн ата-анасының немесе олардың орынбасары-
ның қол қоюымен жасалған өтiнiш, баланың туу туралы
куәлiгi, мүлiктiң сатып алу-сату туралы құжаттар, мүлiк-
тiң құқықтық мәртебесiн анықтайтын құжаттар қажет."
Gemma’s response: "...To sell the property of a minor, an
application signed by the parents or their legal representatives,
the child’s birth certificate, documents regarding the purchase
and sale of the property, and documents confirming the legal
status of the property are required."
Table 20: Example of conversational data on GovSet.

```
