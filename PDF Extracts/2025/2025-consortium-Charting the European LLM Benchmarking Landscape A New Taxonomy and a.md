---
title: "2025-consortium-Charting the European LLM Benchmarking Landscape A New Taxonomy and a - PDF Extract"
source_pdf: "2025-consortium-Charting the European LLM Benchmarking Landscape A New Taxonomy and a.pdf"
pages: 17
extracted_at: "2026-02-13T09:50:30.066238"
---

# PDF Extract: 2025-consortium-Charting the European LLM Benchmarking Landscape A New Taxonomy and a

**Source PDF:** 2025-consortium-Charting the European LLM Benchmarking Landscape A New Taxonomy and a.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

Charting the European LLM Benchmarking Landscape:
A New Taxonomy and a Set of Best Practices
Špela Vintar∗†, Taja Kuzman Pungeršek∗, Mojca Brglez∗†, Nikola Ljubešić∗•‡
∗Jožef Stefan Institute, Jamova 39, Ljubljana, Slovenia
{spela.vintar, taja.kuzman, mojca.brglez, nikola.ljubesic}@ijs.si
†Faculty of Arts, University of Ljubljana, Aškerčeva 2, Ljubljana, Slovenia
• Faculty of Computer and Information Science, University of Ljubljana
Večna pot 113, Ljubljana, Slovenia
‡ Institute of Contemporary History, Privoz 11, Ljubljana, Slovenia
Abstract
While new benchmarks for large language models (LLMs) are being developed continuously to catch up with the
growing capabilities of new models and AI in general, using and evaluating LLMs in non-English languages remains
a little-charted landscape. We give a concise overview of recent developments in LLM benchmarking, and then
propose a new taxonomy for the categorization of benchmarks that is tailored to multilingual or non-English use
scenarios. We further propose a set of best practices and quality standards that could lead to a more coordinated
development of benchmarks for European languages. Among other recommendations, we advocate for a higher
language and culture sensitivity of evaluation methods.
Keywords: large language models, benchmarking, taxonomy, cultural competence, quality recommenda-
tions
1.
Introduction
The rapid advancement of large language mod-
els (LLMs) has brought unprecedented capabili-
ties in natural language understanding and gen-
eration, reasoning, coding, and more. With the
global race in raising the bar, commercial models
are approaching artificial general intelligence (AGI)
and exhibit more and more agency as they engage
in strategic planning, independently interact with
other applications, and carry out larger tasks. While
open-source models generally score lower on most
leaderboards, they too grow larger and smarter.
In the brief history of LLMs, many evaluation
frameworks have been set up – both human and
automatic – to assess their evolving performance
across different linguistic and non-linguistic tasks
of growing complexity.
While new benchmarks
emerge almost on a daily basis in order to measure
these expanding abilities, the overwhelming major-
ity of evaluation datasets are developed primarily
for English, creating a significant evaluation gap for
other languages and varieties.
To evaluate the performance of LLMs in non-
English contexts, a widely used approach so far
has been to translate existing English benchmarks
using machine translation, with or without human
revision. This might seem reasonable: several
major international benchmarks or benchmark col-
lections (e.g., SuperGLUE (Wang et al., 2019),
MMLU (Hendrycks et al., 2021), Hellaswag (Zellers
et al., 2019) exist together with their parallel (trans-
lated) versions, and this allows for a direct com-
parison of LLMs across a wide range of tasks and
languages. However, Global-MMLU (Singh et al.,
2024) revealed that success in MMLU depends
heavily on learning Western-centric concepts, with
28% of all questions requiring culturally sensitive
knowledge. Moreover, for questions requiring geo-
graphic knowledge, an astounding 84.9% focus on
either North American or European regions. Such
cultural biases are not uncommon in other widely
used benchmarks, and their machine-translated
versions potentially overlook language- and culture-
specific phenomena, exhibit skewed performance
which does not accurately reflect true multilingual
capabilities, or simply fail to address issues which
may be critical for users of an LLM in a particular
language.
On the other spectrum of multilingual evaluation,
there are several cases of language- and culture-
specific benchmarks, such as those included in the
Hungarian HuLu (Ligeti-Nagy et al., 2024) evalua-
tion framework, BenCzechMark (Fajcik et al., 2025),
PLCC (Dadas et al., 2025), or BertaQA (Etxaniz
et al., 2024), which have been developed specif-
ically for a particular language or community of
speakers. Such benchmarks provide a deeper in-
sight into a model’s performance for that language,
but typically do not allow us to assess the model’s
multilingual capacities.
Despite the proliferation of evaluation platforms,
research projects, and benchmarking initiatives
across the multilingual landscape, the field lacks
a comprehensive overview that synthesizes cur-
rent practices, identifies critical gaps, and provides
arXiv:2510.24450v2  [cs.CL]  4 Nov 2025

--- Page 2 ---

clear guidance for developing more inclusive and
effective evaluation methodologies for LLMs in non-
English contexts. We thus make a case for the
creation of a European benchmarking registry that
collects structured benchmark data according to a
universal and inclusive taxonomy of benchmarks.
The proposed registry would include rich descrip-
tive metadata and provide a clear overview of both
existing benchmarks and the gaps in the current
European benchmarking landscape.
The remainder of this paper is structured as fol-
lows: In Section 2, we present some recent devel-
opments in LLM benchmarking, focusing on eval-
uations of linguistic and cultural competence in a
multilingual context and on emerging trends. In
Section 3, we proceed with a proposal for a cat-
egorization of benchmarks that could serve as a
foundation for charting ongoing and future LLM
evaluation activities in Europe and beyond. We
finally propose some recommendations as to how
existing benchmarks can be documented, and how
future benchmarks can be made both more culture-
aware and more in tune with the needs of different
language communities.
2.
Recent Developments in LLM
Benchmarking
Several comprehensive overviews of LLM bench-
marking have recently been published, including
Chang et al. (2023) and Ni et al. (2025). Both sur-
veys clearly show trends in both the development
of datasets and the evolution of evaluation metrics.
However, they lack a focus on non-English and mul-
tilingual scenarios, which is the main motivation for
this work.
2.1.
Major Benchmarks
By major or global, we refer to benchmarks most
frequently used in current evaluation platforms and
leaderboards. These benchmarks are without ex-
ception in English. The ones that evaluate generic
language understanding and commonsense rea-
soning have their origins in the 2018–2022 period,
when the challenges still roughly corresponded to
natural language processing (NLP) research areas.
Some of these benchmarks have seen multiple re-
visions, extensions and updates, and can be seen
as “parent” datasets on which many adaptations,
translations, or local versions are based.
Some of the most prominent for language under-
standing and reasoning include MMLU (Hendrycks
et al., 2021) and its derivatives MMLU-Pro (Wang
et al., 2024), MMLU-Prox (Xuan et al., 2025) and
Global MMLU (Singh et al., 2024); the Super-
GLUE benchmark collection comprising BoolQ
(yes/no questions, Clark et al., 2019), Commit-
mentBank (textual entailment, De Marneffe et al.,
2019), COPA (Choice of Plausible Alternatives for
causal reasoning, Roemmele et al., 2011), MultiRC
(multi-sentence reading comprehension, Khashabi
et al., 2018), ReCoRD (reading comprehension
with commonsense reasoning, Zhang et al., 2018),
RTE (Recognizing Textual Entailment, Giampiccolo
et al., 2007), WiC (Words in Context, Pilehvar and
Camacho-Collados, 2019), and WSC (Winograd
Schema Challenge, Levesque et al., 2012); ARC
(Clark et al., 2018) with multiple-grade science
questions; Hellaswag (Zellers et al., 2019) and
its recent derivative GoldenSwag (Chizhov et al.,
2025). An attempt to create a more challenging
benchmark collection is BIG-bench (Beyond the Im-
itation Game Benchmark, Srivastava et al., 2023),
a massive collaborative benchmark consisting of
204 tasks contributed by more than 450 authors
across 132 institutions, designed to probe large lan-
guage models on tasks believed to be beyond their
current capabilities. Finally, SUPERB (Speech pro-
cessing Universal PERformance Benchmark, Yang
et al., 2021) is a unified speech-focused benchmark
for evaluating self-supervised and general-purpose
speech representations across a wide spectrum
of speech processing tasks. It organizes 10 core
tasks – including automatic speech recognition,
speaker identification, keyword spotting, emotion
recognition, and intent classification – spanning
content, speaker, semantics, and paralinguistics.
2.2.
Multilingual Benchmarks
Most state-of-the art models have multilingual ca-
pabilities, but since the precise amounts of non-
English data used in their pre-training are usually
obscure, it is hard to say to what extent the lan-
guage competence of a model in a particular lan-
guage is in correlation with the amount of language-
specific data it has seen. In addition to this, models
differ in their representations of intermediate layers,
which may result in cultural conflicts between latent
internal and target output language (Zhong et al.,
2024).
Since many authors observe a marked decline
in performance for low-resource languages, bench-
marks are now being developed both as parallel
evaluation sets based on existing “parent” datasets
to allow for direct comparison of LLM capabilities
across a number of languages, and as language-
specific benchmarks, usually aimed at assessing
LLM performance in a particular linguistic commu-
nity and/or culture (see Section 2.4 for the latter).
Although the datasets in the first category are
parallel, they may differ considerably in the meth-
ods used for their creation. Some were translated
using machine translation or LLMs, for example,
EU20-MMLU, EU20-HellaSwag, EU20-ARC, EU20-
TruthfulQA, and EU20-GSM8K (Thellmann et al.,

--- Page 3 ---

2024); or MMLU-Prox (Xuan et al., 2025). Other
multilingual benchmarks were created with a spe-
cial focus on cultural sensitivity by dividing the orig-
inal subsets into culturally sensitive and culturally
agnostic ones (Global MMLU, Singh et al., 2024), or
by using professional translators or multiple rounds
of revision to raise the quality of the dataset, e.g.,
BenchMax (Huang et al., 2025), Flores-101 and
FLORES-200 (Goyal et al., 2022) and Belebele
(Bandarkar et al., 2024).
For speech, ML-SUPERB (Multilingual Speech
processing Universal PERformance Benchmark,
Shi et al., 2023) extends the English SUPERB
speech benchmark to 143 languages, evaluating
self-supervised speech representations on auto-
matic speech recognition and language identifica-
tion. FLEURS (Conneau et al., 2022) is a speech-
based extension of the FLORES multilingual bench-
mark, with focus on language identification, auto-
matic speech recognition, and retrieval evaluation.
DIALECTBENCH (Faisal et al., 2024) is the first
large-scale benchmark for language variety under-
standing, aggregating 10 text-level tasks for 281
varieties.
2.3.
Dynamic Benchmarks
Recent developments emphasize dynamic and
contamination-resistant evaluation.
The period
2022–2025 has witnessed fundamental shifts to-
ward more sophisticated evaluation approaches.
One such attempt is LiveBench (White et al., 2024),
the first benchmark designed to resist training data
contamination through frequently updated ques-
tions from recent sources, automatic scoring, and
monthly updates. This dynamic approach remains
challenging, with the top models achieving accu-
racy below 80%.
2.4.
Language- and Culture-Specific
Benchmarks
Focusing on different approaches to the evaluation
of LLM performance in non-English European lan-
guages, we find a broad array of language- and
culture-specific benchmarks developed with vari-
ous methodologies and serving different purposes,
of which we present the ones we find most interest-
ing.
Many European languages have established
evaluation frameworks dedicated to language-
specific benchmarks, and in most cases such
frameworks combine traditional datasets translated
from English, and native more culture-aware bench-
marks. Examples include HuLu1 for Hungarian
(Ligeti-Nagy et al., 2024), which covers a number of
1https://hulu.nytud.hu
well-known tasks such as plausible alternatives (Hu-
CoPa), textual entailment (HuRTE) and linguistic
acceptability (HuCoLa), of which the latter was orig-
inally constructed using sentences from selected
Hungarian linguistics books. BenCzechMark for
Czech (Fajcik et al., 2025) is a complex bench-
mark collection comprising 50 tasks, of which 14
were newly created and only 10% of the collective
instances were machine-translated. The authors
also employ multiple evaluation metrics including
duel scoring. Another recent benchmark for Czech,
Ukrainian and Slovak called CUS-QA (Libovick`y
et al., 2025) focuses specifically on cultural compe-
tence and crafts questions, both textual and visual,
from Wikipedia articles which exist in only one of
the languages.
For Iberian languages, a comprehensive and ex-
tensible framework has been established under
IberBench (González et al., 2025), spanning 22
task categories and addressing both generic and
industry-relevant tasks. In parallel and under a sim-
ilar name, IberoBench (Baucells et al., 2025) offers
62 tasks of which several were created from scratch
from native data, and others were included only if
they satisfied rather strict quality criteria.
For Slovenian, the SloBENCH2 evaluation frame-
work offers natural language inference (SI-NLI),
machine translation, speech recognition, Slovene
SuperGLUE, and two pragmatics benchmarks: Slo-
PragMega and SloPragEval. To create the latter,
full localization of the originally English dataset was
performed, by adapting cultural references and oc-
casionally completely rewriting examples to better
match the linguistic and cultural context. A simi-
lar approach has been taken while translating and
adapting the COPA benchmark (Roemmele et al.,
2011) to four standard languages and three dialects
of the South Slavic language group, resulting in
the DIALECT-COPA (Ljubešić et al., 2024) bench-
mark collection. While proper cultural adaptation
did take place, the overall popularity and age of
the parent COPA benchmark surely makes it prone
to LLM contamination. Regardless of that, today’s
best-performing proprietary models still score only
halfway between random and optimal on dialectal
data (Chifu et al., 2024).
A fully native benchmark is ITALIC for Italian
(Seveso et al., 2025), which comprises 10,000 in-
stances from 12 domains and was built entirely from
exam materials offered by various public institutions
or government bodies.
An exceptionally active approach to language-
and culture-specific benchmarking can be ob-
served for Polish3, with a range of generic and
domain-specific evaluations for Polish including
2https://slobench.cjvt.si
3https://huggingface.co/spaces/
speakleash/polish-llm-benchmarks

--- Page 4 ---

multi-turn conversation (MT-Bench), emotional in-
telligence (EQ-Bench), comprehensive text under-
standing (CPTUB4), medical domain benchmark,
linguistic and cultural competency (PLCC, Dadas
et al., 2025), educational (LLMs Behind the School
Desk), cultural vision benchmark, and legal QA
tasks. Most of these benchmarks were developed
anew, by carefully selecting tasks and examples,
verifying them by experts and collecting human an-
notations. The CPTUB is composed of two parts,
the first evaluating implicatures (implied meaning,
sarcasm, idiomatic expressions) and the second
testing on tricky questions (logical puzzles, seman-
tic ambiguity, logical inconsistencies, absurdity, hu-
mor). Similarly, the PLCC consists of 600 manually
crafted questions and is divided into six categories:
history, geography, culture and tradition, art and en-
tertainment, grammar, and vocabulary. The leader-
board results5 indicate that even the largest models
still reach mediocre performance in Polish gram-
mar and vocabulary, thus justifying the need for
detailed assessment of linguistic competence for
other European languages as well. A final exam-
ple of a culturally specific benchmark is the Polish
Cultural Vision Benchmark6, a collection of images
with text descriptions to evaluate the cultural com-
petence of multimodal models. The dataset is part
of a citizen science project aimed at collecting 1 mil-
lion culturally specific images7 and recruiting user
donations under the slogan of “technopatriotism.”
While similar platforms have been established be-
fore to collect text data, this is a positive example of
a contemporary and at the same time participatory
benchmark.
3.
Categorization of Benchmarks
Since this paper makes a case for a European
database of LLM benchmarks, we propose a new
taxonomy which would allow a better categoriza-
tion and labeling of benchmarks for non-English
languages. This would allow us to better compare
LLMs across languages; gain deeper insight into
the strengths and weaknesses of current and future
LLMs in a specific language, use case, modality or
domain; set common priorities and work towards
filling the evaluation and performance gaps.
The proposed taxonomy should serve as a (ten-
tative) hierarchy of labels to organize or classify
benchmarks; many (or indeed most) belong to more
4https://huggingface.co/spaces/
speakleash/cptu_bench
5https://huggingface.co/spaces/sdadas/
plcc
6https://huggingface.co/spaces/
speakleash/Polish_Cultural_Vision_
Benchmark
7https://obywatel.bielik.ai
than a single category. For this reason, a natural
choice to store and query the European benchmark-
ing activities is a database, in which benchmarks
are described according to this proposal. Thus, the
benchmarks are assigned non-exclusive categories
and are richly described with metadescriptions.
While alignment, including trustworthiness, truth-
fulness and safety of LLMs, are central topics to
the development of LLMs, they constitute another
level of evaluation. Many elements of AI ethics
partly overlap, or are entailed, in other benchmarks
(e.g., bias is revealed in translation or language
generation; trustworthiness is related to reasoning
performance, etc.). This is another reason why
multiple categories per benchmark are considered
typical and expected.
Since LLMs tend to perform worse in non-English
languages, and especially non-standard varieties,
over a spectrum of tasks, we propose that the
language- and culture-related abilities receive more
attention, and therefore a more fine-grained taxon-
omy than they do in existing taxonomies. The list
can be expanded as needed.
3.1.
Existing Taxonomies
As new benchmarks are continuously presented to
evaluate the emerging capabilities of LLMs, many
attempts have been made to organize them in a
structured and logical way.
The AI Verify Foundation has established one
of the most systematic approaches to LLM bench-
mark categorization globally. In their October 2023
publication “Cataloguing LLM Evaluations” (AI Ver-
ify Foundation, 2023), LLM benchmarks are orga-
nized into 5 top categories (further divided into
subcategories). These are General Capabilities
(natural language understanding, natural language
generation, reasoning, knowledge and factuality,
tool use effectiveness, multilingualism, and con-
text length handling); Domain Specific Capabilities
(specialized industry performance across various
domains); Safety and Trustworthiness; Extreme
Risks; and Undesirable Use Cases.
The catalogue represents a comprehensive and
valuable contribution to the field, and has many
positive features: The taxonomy is based on LLM
capabilities, occasionally also referred to as tasks,
which seems intuitively most pragmatic as this is
usually the way we think about (and evaluate) hu-
man performance too. Complex benchmarks can
appear in several categories simultaneously (e.g.,
BigBench as a massive collaborative benchmark
appears in almost all taxonomy categories), and the
recommendations for future LLM evaluations are
a solid starting point to reinforce minimum quality
standards for fair and trustworthy LLM assessment.
However, the catalogue also has some draw-
backs which render it unsuitable for our purposes.

--- Page 5 ---

Firstly, to no fault of its authors, it has not been
updated since 2023 and hence does not include
many benchmarks which have since become main-
stream, nor does it address recent developments
in LLMs and AI in general. Secondly, although it
includes Multilinguality as a separate category, it
falls short in capturing some aspects of LLM perfor-
mance which may be critical for the evaluation of
European models; i.e., models specifically devel-
oped to be used in region-, language-, culture- or
domain-specific contexts. Thirdly, and this is less
of a drawback but simply an observation, the taxon-
omy and the quality recommendations are primarily
focused on the safety and trustworthiness of LLMs,
in the context of AI governance and alignment re-
search. While these are indeed crucial priorities
especially for the so-called ”frontier models” and
capabilities, the European landscape of LLM de-
velopment and evaluation is – at least for now –
gyrating around a different set of goals, such as
how to reach state-of-the-art levels of understand-
ing and generation in non-English languages, or
how to de-bias English-centric models.
Other approaches to taxonomization include
HELM (Holistic Evaluation of Language Models),
also referred to as the Stanford approach (Liang
et al., 2022). The authors introduce the concept of
scenarios (what we want to evaluate) and metrics
(which performance aspects are measured, and
how), then propose a taxonomy of scenarios and
desiderata. Today, the framework8 includes a num-
ber of leaderboards with support for multimodality
and model-graded evaluation. While the scenarios
proposed in HELM and the framework itself leave
room for continuous extension, they do not in fact
offer a hierarchical structure with sufficient focus
on multilinguality and issues related to the use of
LLMs in non-English contexts.
Similarly, Chang et al. (2023) provide an overview
of existing LLM evaluations, which they examine
from three aspects: what, where, and how to eval-
uate. They divide the evaluations tasks into eight
top-level non-exclusive categories, namely Natural
language processing; Robustness, ethics, biases
and trustworthiness; Social sciences; Natural sci-
ence and engineering; Medical applications; Agent
applications; and Other applications.
Huber and Niklaus (2025) present a cognitive-
based view on benchmarking by mapping the well-
known Bloom’s taxonomy of cognitive abilities to
LLM capabilities across six hierarchical cognitive
levels: Remember, Understand, Apply, Analyze,
Evaluate, and Create, revealing significant gaps in
the coverage of higher-order thinking skills.
Another comprehensive attempt at taxonomizing
benchmarks is by Guo et al. (2023) who introduce
a three-pillar framework that categorizes LLM eval-
8https://crfm.stanford.edu/helm/
uation into three major groups: Knowledge and
capability evaluation, Alignment evaluation, and
Safety evaluation.
3.2.
New Taxonomy Proposal
As already outlined in the sections above, the pro-
posed taxonomy, provided in Appendix A, is in-
tended for the categorization of (mainly) European
LLM benchmarks and is based on AI Verify Foun-
dation’s catalogue, but with the following modifica-
tions:
• We merge all language-related tasks and
scenarios under a single top-level category
called Language capabilities (see Table 1 in
Appendix).
• We further merge the traditional NLP divide
between natural language understanding
and natural language generation into a sin-
gle subcategory. The fact is that state-of-the-
art LLMs more often than not combine these
two capabilities, and even straight-forward
tasks such as question answering or text sum-
marization involve both.
• We expand the category for general linguis-
tic competence with further subcategories
for style, conversation and pragmatics, and
allow for other more fine-grained aspects of
measuring the grammaticality, stylistic appro-
priateness or coherence of generated outputs
(see Tables 1 and 2 in Appendix).
• We expand the category of specific linguis-
tic competence to include creativity, atypical
communication, the use of domain-specific lan-
guage etc. (see Table 2).
• We also expand and redefine the category
of multilinguality to include code-switching,
multilingual interaction, and dialectal flexibility
(see Table 2).
• We introduce cultural competence as a sep-
arate category.
• We introduce speech as a separate category
to include benchmarks specifically aimed at
performing tasks unique to spoken language
as input or output (see Table 2).9
• We add agency as a form of long-term, con-
sistent or strategic reasoning (see Table 3).
9We propose Modality as one of the metadescriptors,
allowing for any benchmark to be implemented in any of
the modes. The Speech category refers to evaluations
targeted at speech-related activities.

--- Page 6 ---

Figure 1 shows the four top-level taxonomy cate-
gories with subcategories. The full taxonomy along
with fine-grained third-level categories is provided
in Tables 1, 2, 3 and 4 in Appendix A.
Figure 1: Top-level categories with subcategories.
4.
Quality Standards and Metadata
If we conceive of a European benchmarking reg-
istry as a searchable database which may help the
LLM development community in setting priorities,
exchanging knowledge and standardizing evalua-
tion practices, we should be able to define some
desiderata around how a particular benchmark is
presented, described and distributed. Below we
discuss some of these aspects.
4.1.
Provenance
While it is clear that the development of original
and sufficiently complex benchmarking datasets is
highly time-consuming and costly, the drawbacks of
automatically translated and culturally maladapted
benchmarks have been clearly pointed out (Singh
et al., 2024; Xuan et al., 2025). We should thus
strive towards clearer – even if more complex –
descriptors which indicate how a dataset or bench-
mark was created. We propose the following de-
scriptors:
• Original Applies to datasets which have been
originally created in the language they appear
in, by any method other than translation (e.g.,
collecting original exam questions, employ-
ing experts to provide domain-specific tasks,
adapting authentic texts in a particular lan-
guage to create tasks in that language).
• Machine translation Applies to datasets cre-
ated by any automated translation service, in-
cluding those created by LLMs using any kind
of prompt scenario, and workflows with ma-
chine revision. The tools and workflows must
be specified.
• Machine translation and Human revision
Applies to datasets where the result of auto-
mated translation was revised by a human pro-
fessional or non-professional translator or re-
viewer. Since many non-English benchmarks
are created by machine translating the – usu-
ally – English original, followed by human re-
vision of only a small portion of the dataset,
the recommendation would be to use all labels
that apply.
• Human translation Used only for datasets
which have been fully translated and revised
by humans. Only a few European non-English
datasets satisfy this criterion.
• Full localization Used for datasets which have
not only been translated professionally, but
for which a full linguistic and cultural adap-
tation was performed. This might mean the
replacement of culturally-specific or untrans-
latable tasks with new ones, or removing parts
of the dataset deemed culturally unsuitable.
• Other If several of the above scenarios were
used, the dataset should be labeled with all
that apply. Other methods and scenarios used
in the creation of a dataset should be specified
here.
4.2.
Accessibility
The tension between open benchmarking and data
contamination poses a significant challenge for AI
evaluation. While public datasets enable repro-
ducible research and fair comparisons, they risk
contamination when models train on test data, inflat-
ing performance scores and undermining bench-
mark validity. Private evaluation sets offer a po-
tential solution by keeping data hidden from train-
ing processes, ensuring cleaner performance mea-
surements.
• Public Applies to fully open datasets shared
with labels through common platforms.
• Public without labels Applies to datasets
where labels are not distributed to prevent di-
rect training.

--- Page 7 ---

• Private (academic/research access) Where
authors encourage reproducibility but wish to
prevent contamination.
• Private (closed/proprietary) Where datasets
are typically not shared as they are used for
internal or industry-specific evaluation.
• Other This may include dynamic benchmarks
where tasks are continually updated (such as
White et al., 2024).
4.3.
Language Coverage
This category indicates the prominence, reach or
scale of a benchmark in terms of its presence on
major leaderboards, coverage, global spread, but
also purpose. We are aware that the boundaries
between the proposed buckets may be fuzzy.
• Major global benchmark See section 2.1 for
examples.
• Multilingual benchmark This category can be
used for benchmarks derived from the above,
for instance by developing a multilingual vari-
ant of a well-known benchmark for a set of new
languages. Examples include XCOPA (Ponti
et al., 2020), MMLU-Prox (Xuan et al., 2025)
or xHumanEval (Raihan et al., 2025).
• Language-group or region-specific bench-
mark This category is used for language-
specific benchmarks as well as benchmarks
that cover multiple languages from a simi-
lar language group or target a certain ge-
ographical region.
Examples include Iber-
oBENCH (Baucells et al., 2025) and DIALECT-
COPA (Ljubešić et al., 2024).
• Other
4.4.
Evaluation Type
An important factor for present and future bench-
marks is the divide between closed-ended types of
tasks, most prominently multiple-choice questions,
but also other types of tasks where the solution is in-
cluded in the task, and open-ended tasks, typically
generation of text, speech, image, or multimodal
output. Few benchmarks to date address the lat-
ter, despite the fact that generative LLMs are now
mainstream and the vast majority of application
scenarios exploit generative abilities.
4.5.
Evaluation Metrics and Frameworks
The performance of an LLM can be evaluated in
several ways, depending on the type of task. For
multiple choice questions, text classification tasks
or cloze tests, where the correct answer is deter-
ministic, accuracy or F1 can be used. However, to
evaluate longer, more complex responses resulting
from generative tasks, many other methods were
proposed. In reference-based evaluation, the LLM
response is compared to a reference using various
distance measures (e.g., BERTScore, Rouge-1,
METEOR), while in reference-less contexts, the
quality of the response is directly assessed (e.g.,
by an LLM-as-a-judge). As we have seen, re-
cently developed benchmarks employ more com-
plex evaluation methodologies, and a common al-
ternative to algorithmic benchmarks is human pref-
erence voting (in so-called chatbot arenas, e.g.,
https://lmarena.ai/).
Another important element is the existence of
a human baseline, and its quality. Important fac-
tors to consider are participant selection (demo-
graphic sampling, expertise), participant training,
task design and instructions (to ensure fair com-
parison between humans and LLMs), control for
attention, bias or fatigue, and the collection of par-
ticipant demographics to facilitate reproducibility
and interpretation of results. Human annotators or
participants can also provide relevant insight into
the overall quality of the benchmark, thus some
campaigns actively collect human feedback to be
used in revised versions of the evaluation dataset.
If the benchmark or dataset is integrated into
an evaluation framework, this should be indicated
together with a link or other reference to the evalu-
ation site.
4.6.
Metadescriptors
We propose collecting rich metadata for each
benchmark that allows researchers to quickly under-
stand its content, characteristics, and provenance.
Such metadescriptors facilitate dataset discovery,
comparison, and reuse. Below, we summarize the
metadata fields currently envisaged in the proposed
registry:
• Description: A short summary of the dataset’s
content and purpose.
• Benchmark family: The broader benchmark
initiative or collection to which the dataset
belongs.
For example, the COPA bench-
mark family would include the English COPA
(Roemmele et al., 2011) and its many par-
allel variants such as the COPA datasets in
Hungarian (Ligeti-Nagy et al., 2024), Croat-
ian (Ljubešić and Lauc, 2021), South Slavic
dialects (Ljubešić et al., 2024) etc.
• Number of test instances: The total num-
ber of instances in the test set, enabling quick
comparison of dataset scale.

--- Page 8 ---

• Language:
The language(s) in which the
dataset is provided.
• Language type:
Specification of whether
the language of the dataset is standard, non-
standard, or a dialect.
• Modality: The input modality of the dataset,
such as text, speech, sign language, or audio-
visual signal.
• Authors:
The creators or curators of the
dataset.
• Paper link: Reference to the main publication
describing the dataset.
• Access info: Information on how to obtain the
dataset, e.g., a link to a website from where the
dataset can be acquired, or an e-mail of the
dataset owner if the dataset is not published
online.
• Last revised: The date of the most recent
update or revision of the dataset.
• More information: Additional notes, links, or
resources relevant to the dataset.
5.
Recommendations and Future
Directions
Several challenges of LLM evaluation have been
pointed out by a number of studies (e.g., Laskar
et al., 2024 or AI Verify Foundation, 2023: p. 16–
22), most notably reproducibility, reliability (includ-
ing contamination, obscure evaluation methods
and unfair comparisons), and robustness. There
are numerous parallel activities in progress to set
the course of the European LLM evaluation land-
scape, agree on common principles and establish
a dialogue between different stakeholders. While a
full review of the above-mentioned challenges is be-
yond the scope of this paper, we list some priorities
which apply in particular for the European bench-
marking landscape and evaluations in non-English
settings.
1. Cultural sensitivity The prevalent framing of
toxicity, bias, but also factual knowledge and
reasoning, tends to be Western-centric. Evalu-
ation concepts should be expanded to include
diverse global perspectives and values.
2. Language sensitivity Under this term, we re-
fer to the fact that LLMs find applications in
multilingual and multicultural settings, and that
the performance of an LLM may depend heav-
ily on the language it is used in. Benchmarks
for bias and toxicity, but also some common
benchmarks for language understanding and
inference, are not trivial to transfer across lan-
guages and linguistic structures.
3. Comparability vs. specificity Many Euro-
pean and other non-English languages still
have a limited number of benchmark datasets.
To provide a common ground for the evalua-
tion of LLMs across languages, major global
benchmarks are still being translated to facil-
itate international comparability. It is recom-
mended that such translation and adaptation
procedures acknowledge the complexity of the
task and, even if performed automatically, con-
sider employing different tools, prompt strate-
gies, LLM revision techniques and human eval-
uation of random samples.
4. Additional modalities Many benchmarks
have been developed recently to include differ-
ent modalities, but there is still a gap in bench-
marks for speech, sign language, audiovisual
communication, and combinations thereof.
5. Human baseline While frontier LLMs already
surpass humans in many areas, it is of
paramount importance, especially in high-risk
domains, to have a solid foundation for the
evaluation of LLMs by comparing the results
to human performance on a specific task, ac-
knowledging that every benchmark is a limited
representation of a task.
6. Transparent implementation The details of
the evaluation process should be published
in a transparent manner, including the exact
specification of prompting strategies and hyper-
parameters used, such as temperature. If pos-
sible, evaluation scripts should also be made
public, and results validated through multiple
runs in the case of smaller datasets.
7. Context-specific evaluation There is a lack
of nuanced, context-specific evaluations that
address the multi-faceted nature of real-world
LLM deployments.
This includes domain-
specificity, but also other elements of attuning
evaluation to the users it serves.
We believe that the rapidly evolving benchmark-
ing landscape for European languages would ben-
efit from a catalogue where each benchmark is cat-
egorized and documented according to the above
principles. We conceive of such a catalogue in the
form of a database, accommodating the fact that
the proposed taxonomy categories and metade-
scriptors may overlap, so that each entry can be
labeled with all which apply.

--- Page 9 ---

6.
Conclusion
We have presented recent trends in LLM bench-
marking for European languages and proposed a
new taxonomy for their categorization, intended to
be implemented alongside a range of metadescrip-
tors in the context of a European catalogue of LLM
benchmarks. Our taxonomization strategy focuses
on the linguistic, cultural, factual and reasoning ca-
pabilities of models and also incorporates emerging
abilities. The proposed considerations follow the
wide-spread belief amongst European researchers
and developers that the traditional Western-centric,
likely contaminated and linguistically inappropriate
datasets no longer satisfy our needs, and that tar-
geted efforts should be invested in filling the evalu-
ation gaps for all European languages.
The initiative presented in this paper is the result
of a series of discussions and reflections within the
framework of several international research com-
munities, collecting and integrating feedback from
a number of researchers, developers and bench-
mark creators. With the rapid advancement of the
field, we envisage continuous extensions and revi-
sions both of the taxonomy and the associated set
of metadescriptors and recommendations.
Acknowledgements
This work is supported by the LLM4DH project,
funded by the Slovenian Research and Innovation
Agency (ARIS) under the grant agreement GC-
0002.
7.
Bibliographical References
AI Verify Foundation. 2023. Catalogue of LLM Eval-
uations.
Lucas Bandarkar, Davis Liang, Benjamin Muller,
Mikel Artetxe, Satya Narayan Shukla, Donald
Husa, Naman Goyal, Abhinandan Krishnan,
Luke Zettlemoyer, and Madian Khabsa. 2024.
The Belebele Benchmark: a Parallel Reading
Comprehension Dataset in 122 Language Vari-
ants. In Proceedings of the 62nd Annual Meet-
ing of the Association for Computational Linguis-
tics (Volume 1: Long Papers), pages 749–775,
Bangkok, Thailand. Association for Computa-
tional Linguistics.
Irene Baucells, Javier Aula-Blasco, Iria de Dios-
Flores, Silvia Paniagua Suárez, Naiara Perez,
Anna Salles, Susana Sotelo Docio, Júlia Fal-
cão, Jose Javier Saiz, Robiert Sepulveda Torres,
Jeremy Barnes, Pablo Gamallo, Aitor Gonzalez-
Agirre, German Rigau, and Marta Villegas. 2025.
IberoBench: A benchmark for LLM evaluation in
Iberian languages. In Proceedings of the 31st
International Conference on Computational Lin-
guistics, pages 10491–10519, Abu Dhabi, UAE.
Association for Computational Linguistics.
Daniel Borkan, Lucas Dixon, Jeffrey Sorensen,
Nithum Thain, and Lucy Vasserman. 2019. Nu-
anced metrics for measuring unintended bias
with real data for text classification. In Compan-
ion proceedings of the 2019 world wide web con-
ference, pages 491–500.
Yupeng Chang, Xu Wang, Jindong Wang, Yuan
Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xi-
aoyuan Yi, Cunxiang Wang, Yidong Wang, Wei
Ye, Yue Zhang, Yi Chang, Philip S. Yu, Qiang
Yang, and Xing Xie. 2023. A survey on evalu-
ation of large language models. arXiv preprint
arXiv:2307.03109.
Adrian-Gabriel Chifu, Goran Glavaš, Radu Tudor
Ionescu, Nikola Ljubešić, Aleksandra Miletić,
Filip Miletić, Yves Scherrer, and Ivan Vulić. 2024.
VarDial evaluation campaign 2024: Common-
sense reasoning in dialects and multi-label sim-
ilar language identification. In Proceedings of
the Eleventh Workshop on NLP for Similar Lan-
guages, Varieties, and Dialects (VarDial 2024),
pages 1–15, Mexico City, Mexico. Association
for Computational Linguistics.
Pavel Chizhov, Mattia Nee, Pierre-Carl Langlais,
and Ivan P Yamshchikov. 2025.
What the
HellaSwag?
On the Validity of Common-
Sense Reasoning Benchmarks. arXiv preprint
arXiv:2504.07825.
Christopher Clark, Kenton Lee, Ming-Wei Chang,
Tom Kwiatkowski, Michael Collins, and Kristina
Toutanova. 2019. BoolQ: Exploring the Surpris-
ing Difficulty of Natural Yes/No Questions. In
Proceedings of the 2019 Conference of the North
American Chapter of the Association for Compu-
tational Linguistics: Human Language Technolo-
gies, Volume 1 (Long and Short Papers), pages
2924–2936, Minneapolis, Minnesota. Associa-
tion for Computational Linguistics.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar
Khot, Ashish Sabharwal, Carissa Schoenick, and
Oyvind Tafjord. 2018. Think you have Solved
Question Answering? Try ARC, the AI2 Reason-
ing Challenge. arXiv preprint arXiv:1803.05457.
Alexis
Conneau,
Min
Ma,
Simran
Khanuja,
Yu Zhang, Vera Axelrod, Siddharth Dalmia, Ja-
son Riesa, Clara Rivera, and Ankur Bapna. 2022.
Fleurs: Few-shot learning evaluation of univer-
sal representations of speech. arXiv preprint
arXiv:2205.12446.

--- Page 10 ---

Sławomir Dadas, Małgorzata Grębowiec, Michał
Perełkiewicz, and Rafał Poświata. 2025. Eval-
uating Polish linguistic and cultural compe-
tency in large language models. arXiv preprint
arXiv:2503.00995.
Cristian Danescu-Niculescu-Mizil, Moritz Sudhof,
Dan Jurafsky, Jure Leskovec, and Christopher
Potts. 2013. A computational approach to polite-
ness with application to social factors. In Pro-
ceedings of the 51st Annual Meeting of the As-
sociation for Computational Linguistics (Volume
1: Long Papers), pages 250–259.
Marie-Catherine De Marneffe, Mandy Simons, and
Judith Tonhauser. 2019. The CommitmentBank:
Investigating projection in naturally occurring dis-
course. In Proceedings of Sinn und Bedeutung,
volume 23, pages 107–124.
Julen Etxaniz, Gorka Azkune, Aitor Soroa, Oier La-
calle, and Mikel Artetxe. 2024. BertaQA: How
Much Do Language Models Know About Local
Culture? Advances in Neural Information Pro-
cessing Systems, 37:34077–34097.
Fahim Faisal, Orevaoghene Ahia, Aarohi Srivas-
tava, Kabir Ahuja, David Chiang, Yulia Tsvetkov,
and Antonios Anastasopoulos. 2024. DIALECT-
BENCH: An NLP benchmark for dialects, vari-
eties, and closely-related languages. In Proceed-
ings of the 62nd Annual Meeting of the Associ-
ation for Computational Linguistics (Volume 1:
Long Papers), pages 14412–14454, Bangkok,
Thailand. Association for Computational Linguis-
tics.
Martin Fajcik, Martin Docekal, Jan Dolezal, Karel
Ondrej, Karel Beneš, Jan Kapsa, Pavel Smrz,
Alexander Polok, Michal Hradis, Zuzana Never-
ilova, et al. 2025. BenCzechMark : A Czech-
centric Multitask and Multimetric Benchmark for
Large Language Models with Duel Scoring Mech-
anism. Transactions of the Association for Com-
putational Linguistics, 13:1068–1095.
Bofei Gao, Feifan Song, Zhe Yang, Zefan Cai,
Yibo Miao, Qingxiu Dong, Lei Li, Chenghao Ma,
Liang Chen, Runxin Xu, et al. 2024. Omni-math:
A universal olympiad level mathematic bench-
mark for large language models. arXiv preprint
arXiv:2410.07985.
Danilo Giampiccolo, Bernardo Magnini, Ido Dagan,
and William B Dolan. 2007. The third pascal
recognizing textual entailment challenge. In Pro-
ceedings of the ACL-PASCAL workshop on tex-
tual entailment and paraphrasing, pages 1–9.
José Ángel González, Ian Borrego Obrador, Ál-
varo Romo Herrero, Areg Mikael Sarvazyan,
Mara Chinea-Ríos, Angelo Basile, and Marc
Franco-Salvador. 2025. IberBench: LLM Eval-
uation on Iberian Languages.
arXiv preprint
arXiv:2504.16921.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary,
Peng-Jen Chen, Guillaume Wenzek, Da Ju, San-
jana Krishnan, Marc’Aurelio Ranzato, Francisco
Guzmán, and Angela Fan. 2022. The Flores-
101 evaluation benchmark for low-resource and
multilingual machine translation. Transactions
of the Association for Computational Linguistics,
10:522–538.
Neel Guha, Julian Nyarko, Daniel Ho, Christo-
pher Ré, Adam Chilton, Alex Chohlas-Wood,
Austin Peters, Brandon Waldon, Daniel Rock-
more, Diego Zambrano, et al. 2023. Legalbench:
A collaboratively built benchmark for measuring
legal reasoning in large language models. Ad-
vances in neural information processing systems,
36:44123–44279.
Zishan Guo, Renren Jin, Chuang Liu, Yufei Huang,
Dan Shi, Linhao Yu, Yan Liu, Jiaxuan Li, Bojian
Xiong, Deyi Xiong, et al. 2023. Evaluating Large
Language Models: A Comprehensive Survey.
arXiv preprint arXiv:2310.19736.
Dan Hendrycks, Collin Burns, Steven Basart, Andy
Zou, Mantas Mazeika, Dawn Song, and Jacob
Steinhardt. 2021. Measuring Massive Multitask
Language Understanding. Proceedings of the
International Conference on Learning Represen-
tations (ICLR).
Xu Huang, Wenhao Zhu, Hanxu Hu, Conghui
He, Lei Li, Shujian Huang, and Fei Yuan. 2025.
BenchMAX: A Comprehensive Multilingual Eval-
uation Suite for Large Language Models. arXiv
preprint arXiv:2502.07346.
Thomas Huber and Christina Niklaus. 2025. LLMs
Meet Bloom’s Taxonomy: A Cognitive View on
Large Language Model Evaluations. In Proceed-
ings of the 31st International Conference on Com-
putational Linguistics, pages 5211–5246.
Di Jin, Eileen Pan, Nassim Oufattole, Wei-Hung
Weng, Hanyi Fang, and Peter Szolovits. 2021.
What disease does this patient have?
a
large-scale open domain question answering
dataset from medical exams. Applied Sciences,
11(14):6421.
Daniel Khashabi, Snigdha Chaturvedi, Michael
Roth, Shyam Upadhyay, and Dan Roth. 2018.
Looking Beyond the Surface: A Challenge Set
for Reading Comprehension over Multiple Sen-
tences. In Proceedings of North American Chap-
ter of the Association for Computational Linguis-
tics (NAACL).

--- Page 11 ---

Matej Klemen, Aleš Žagar, Jaka Čibej, and Marko
Robnik-Šikonja. 2022. Slovene natural language
inference dataset SI-NLI. Slovenian language
resource repository CLARIN.SI.
Anastassia Kornilova and Vladimir Eidelman. 2019.
BillSum: A corpus for automatic summarization
of US legislation. In Proceedings of the 2nd Work-
shop on New Frontiers in Summarization, pages
48–56, Hong Kong, China. Association for Com-
putational Linguistics.
Taja Kuzman, Mojca Brglez, Peter Rupnik, and
Nikola Ljubešić. 2021. Slovene web genre identi-
fication corpus GINCO 1.0. Slovenian language
resource repository CLARIN.SI.
Taja Kuzman, Igor Mozetič, and Nikola Ljubešić.
2023. Automatic genre identification for robust
enrichment of massive text collections: Inves-
tigation of classification methods in the era of
large language models. Machine Learning and
Knowledge Extraction, 5(3):1149–1175.
Md Tahmid Rahman Laskar, Sawsan Alqahtani,
M Saiful Bari, Mizanur Rahman, Mohammad
Abdullah Matin Khan, Haidar Khan, Israt Ja-
han, Amran Bhuiyan, Chee Wei Tan, Md Rizwan
Parvez, Enamul Hoque, Shafiq Joty, and Jimmy
Huang. 2024. A systematic survey and critical re-
view on evaluating large language models: Chal-
lenges, limitations, and recommendations. In
Proceedings of the 2024 Conference on Empir-
ical Methods in Natural Language Processing,
pages 13785–13816, Miami, Florida, USA. As-
sociation for Computational Linguistics.
Hector J Levesque, Ernest Davis, and Leora Mor-
genstern. 2012. The Winograd Schema Chal-
lenge. In 13th International Conference on the
Principles of Knowledge Representation and
Reasoning, KR 2012, pages 552–561. Institute
of Electrical and Electronics Engineers Inc.
Percy Liang, Rishi Bommasani, Tony Lee, Dimitris
Tsipras, Dilara Soylu, Michihiro Yasunaga, Yian
Zhang, Deepak Narayanan, Yuhuai Wu, Ananya
Kumar, et al. 2022. Holistic Evaluation of Lan-
guage Models. arXiv preprint arXiv:2211.09110.
Jindřich Libovick`y, Jindřich Helcl, Andrei Manea,
and Gianluca Vico. 2025.
CUS-QA: Local-
Knowledge-Oriented
Open-Ended
Ques-
tion
Answering
Dataset.
arXiv
preprint
arXiv:2507.22752.
Noémi Ligeti-Nagy, Gergő Ferenczi, Enikő Héja,
László János Laki, Noémi Vadász, Zijian Győző
Yang, and Tamás Váradi. 2024.
HuLU: Hun-
garian language understanding benchmark kit.
In Proceedings of the 2024 Joint Interna-
tional Conference on Computational Linguistics,
Language Resources and Evaluation (LREC-
COLING 2024), pages 8360–8371.
Stephanie Lin, Jacob Hilton, and Owain Evans.
2022. TruthfulQA: Measuring How Models Mimic
Human Falsehoods. In Proceedings of the 60th
Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers),
pages 3214–3252.
Nikola Ljubešić. 2021. Choice of plausible alterna-
tives dataset in Croatian COPA-HR. Slovenian
language resource repository CLARIN.SI.
Nikola Ljubešić, Nada Galant, Sonja Benčina, Jaka
Čibej, Stefan Milosavljević, Peter Rupnik, and
Taja Kuzman. 2024. DIALECT-COPA: Extend-
ing the standard translations of the COPA causal
commonsense reasoning dataset to South Slavic
dialects. In Proceedings of the Eleventh Work-
shop on NLP for Similar Languages, Varieties,
and Dialects (VarDial 2024), pages 89–98, Mex-
ico City, Mexico. Association for Computational
Linguistics.
Nikola Ljubešić and Davor Lauc. 2021. BERTić-
The Transformer Language Model for Bosnian,
Croatian, Montenegrin and Serbian. In Proceed-
ings of the 8th Workshop on Balto-Slavic Natural
Language Processing, pages 37–42.
Andrew L. Maas, Raymond E. Daly, Peter T. Pham,
Dan Huang, Andrew Y. Ng, and Christopher Potts.
2011. Learning word vectors for sentiment anal-
ysis. In Proceedings of the 49th Annual Meeting
of the Association for Computational Linguistics:
Human Language Technologies, pages 142–150,
Portland, Oregon, USA. Association for Compu-
tational Linguistics.
Michal Mochtak, Peter Rupnik, and Nikola Ljubešić.
2024. The parlasent multilingual training dataset
for sentiment identification in parliamentary pro-
ceedings. In Proceedings of the 2024 Joint In-
ternational Conference on Computational Lin-
guistics, Language Resources and Evaluation
(LREC-COLING 2024), pages 16024–16036.
Michal Mochtak, Peter Rupnik, Katja Meden, and
Nikola Ljubešić. 2023. The multilingual senti-
ment dataset of parliamentary debates ParlaSent
1.0.
Slovenian language resource repository
CLARIN.SI.
Ramesh Nallapati, Bowen Zhou, Cicero dos San-
tos, Çağlar Gu˙lçehre, and Bing Xiang. 2016. Ab-
stractive text summarization using sequence-to-
sequence RNNs and beyond. In Proceedings
of the 20th SIGNLL Conference on Computa-
tional Natural Language Learning, pages 280–
290, Berlin, Germany. Association for Computa-
tional Linguistics.

--- Page 12 ---

Shiwen Ni, Guhong Chen, Shuaimin Li, Xuanang
Chen, Siyi Li, Bingli Wang, Qiyao Wang, Xingjian
Wang, Yifan Zhang, Liyang Fan, et al. 2025. A
Survey on Large Language Model Benchmarks.
arXiv preprint arXiv:2508.15361.
Dojun Park, Jiwoo Lee, Hyeyun Jeong, Seohyun
Park, Youngeun Koo, Soonha Hwang, Seonwoo
Park, and Sungeun Lee. 2024. MultiPragEval:
Multilingual Pragmatic Evaluation of Large Lan-
guage Models. In 2nd Workshop on Generali-
sation (Benchmarking) in NLP, GenBench 2024,
pages 96–119. Association for Computational
Linguistics (ACL).
Fabio Petroni, Tim Rocktäschel, Sebastian Riedel,
Patrick Lewis, Anton Bakhtin, Yuxiang Wu, and
Alexander Miller. 2019. Language Models as
Knowledge Bases? In Proceedings of the 2019
Conference on Empirical Methods in Natural
Language Processing and the 9th International
Joint Conference on Natural Language Process-
ing (EMNLP-IJCNLP), pages 2463–2473, Hong
Kong, China. Association for Computational Lin-
guistics.
Mohammad Taher Pilehvar and Jose Camacho-
Collados. 2019. WiC: the word-in-context dataset
for evaluating context-sensitive meaning repre-
sentations. In Proceedings of the 2019 Confer-
ence of the North American Chapter of the As-
sociation for Computational Linguistics: Human
Language Technologies, Volume 1 (Long and
Short Papers), pages 1267–1273, Minneapolis,
Minnesota. Association for Computational Lin-
guistics.
Edoardo Maria Ponti, Goran Glavaš, Olga Majew-
ska, Qianchu Liu, Ivan Vulić, and Anna Korho-
nen. 2020. XCOPA: A multilingual dataset for
causal commonsense reasoning. In Proceed-
ings of the 2020 Conference on Empirical Meth-
ods in Natural Language Processing (EMNLP),
pages 2362–2376, Online. Association for Com-
putational Linguistics.
Nishat Raihan, Antonios Anastasopoulos, and Mar-
cos Zampieri. 2025. mHumanEval - a multilin-
gual benchmark to evaluate large language mod-
els for code generation. In Proceedings of the
2025 Conference of the Nations of the Americas
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Vol-
ume 1: Long Papers), pages 11432–11461, Al-
buquerque, New Mexico. Association for Com-
putational Linguistics.
Sudha Rao and Joel Tetreault. 2018. Dear Sir or
Madam, May I Introduce the GYAFC Dataset:
Corpus, Benchmarks and Metrics for Formality
Style Transfer. In Proceedings of the 2018 Con-
ference of the North American Chapter of the
Association for Computational Linguistics: Hu-
man Language Technologies, Volume 1 (Long
Papers), pages 129–140.
Melissa Roemmele, Cosmin Adrian Bejan, and An-
drew S. Gordon. 2011. Choice of Plausible Alter-
natives: An Evaluation of Commonsense Causal
Reasoning. In Proceedings of the 2011 AAAI
Spring Symposium on Logical Formalizations of
Commonsense Reasoning.
Rachel
Rudinger,
Jason
Naradowsky,
Brian
Leonard, and Benjamin Van Durme. 2018. Gen-
der bias in coreference resolution. In Proceed-
ings of the 2018 Conference of the North Amer-
ican Chapter of the Association for Computa-
tional Linguistics: Human Language Technolo-
gies, New Orleans, Louisiana. Association for
Computational Linguistics.
Andrea Seveso, Daniele Potertì, Edoardo Federici,
Mario Mezzanzanica, and Fabio Mercorio. 2025.
ITALIC: An Italian culture-aware natural language
benchmark. In Proceedings of the 2025 Con-
ference of the Nations of the Americas Chapter
of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long
Papers), pages 1469–1478, Albuquerque, New
Mexico. Association for Computational Linguis-
tics.
Jiatong Shi, Dan Berrebbi, William Chen, Ho-Lam
Chung, En-Pei Hu, Wei-Ping Huang, Xuankai
Chang, Shang-Wen Li, Abdelrahman Mohamed,
Hung yi Lee, and Shinji Watanabe. 2023. Ml-
superb: Multilingual speech universal perfor-
mance benchmark. In Proceedings of the Annual
Conference of the International Speech Com-
munication Association, INTERSPEECH 2023,
pages 884–888.
Shivalika Singh, Angelika Romanou, Clémen-
tine Fourrier, David I Adelani, Jian Gang Ngui,
Daniel Vila-Suero, Peerat Limkonchotiwat, Kelly
Marchisio, Wei Qi Leong, Yosephine Susanto,
et al. 2024.
Global MMLU: Understanding
and Addressing Cultural and Linguistic Bi-
ases in Multilingual Evaluation. arXiv preprint
arXiv:2412.03304.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam
Fisch, Adam R. Brown, Adam Santoro, Aditya
Gupta, Adrià Garriga-Alonso, Agnieszka Kluska,
Aitor Lewkowycz, Akshat Agarwal, Alethea
Power, Alex Ray, Alex Warstadt, et al. 2023. Be-
yond the imitation game: Quantifying and ex-
trapolating the capabilities of language models.
Transactions on Machine Learning Research.

--- Page 13 ---

Klaudia Thellmann, Bernhard Stadler, Michael
Fromm, Jasper Schulze Buschhoff, Alex Jude,
Fabio Barth, Johannes Leveling, Nicolas Flores-
Herr, Joachim Köhler, René Jäkel, et al. 2024. To-
wards Multilingual LLM Evaluation for European
Languages. arXiv preprint arXiv:2410.08928.
Noémi Vadász and Noémi Ligeti-Nagy. 2022. Wino-
grad schemata and other datasets for anaphora
resolution in Hungarian. Acta Linguistica Aca-
demica, 69(4):564–580.
Alex Wang, Yada Pruksachatkun, Nikita Nangia,
Amanpreet Singh, Julian Michael, Felix Hill,
Omer Levy, and Samuel Bowman. 2019. Su-
perGLUE: A Stickier Benchmark for General-
Purpose Language Understanding Systems. Ad-
vances in neural information processing systems,
32.
Boxin Wang, Weixin Chen, Hengzhi Pei, Chulin Xie,
Mintong Kang, Chenhui Zhang, Chejian Xu, Zidi
Xiong, Ritik Dutta, Rylan Schaeffer, et al. 2023.
DecodingTrust: A Comprehensive Assessment
of Trustworthiness in GPT Models. In NeurIPS.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng
Ni, Abhranil Chandra, Shiguang Guo, Weiming
Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, et al.
2024. MMLU-Pro: A More Robust and Challeng-
ing Multi-Task Language Understanding Bench-
mark. Advances in Neural Information Process-
ing Systems, 37:95266–95290.
Alex Warstadt, Alicia Parrish, Haokun Liu, Anhad
Mohananey, Wei Peng, Sheng-Fu Wang, and
Samuel R. Bowman. 2020. BLiMP: The bench-
mark of linguistic minimal pairs for English. Trans-
actions of the Association for Computational Lin-
guistics, 8:377–392.
Alex Warstadt, Amanpreet Singh, and Samuel R
Bowman. 2019. Neural network acceptability
judgments. Transactions of the Association for
Computational Linguistics, 7:625–641.
Colin White, Samuel Dooley, Manley Roberts,
Arka Pal, Ben Feuer, Siddhartha Jain, Ravid
Shwartz-Ziv, Neel Jain, Khalid Saifullah, Sree-
manti Dey, et al. 2024. LiveBench: A Challenging,
Contamination-Limited LLM Benchmark. arXiv
preprint arXiv:2406.19314.
Krzysztof Wróbel, SpeakLeash Team, and Cyfronet
Team. 2024.
Polish medical leaderboard.
https://huggingface.co/spaces/speakleash/
polish_medical_leaderboard.
Weihao Xuan, Rui Yang, Heli Qi, Qingcheng Zeng,
Yunze Xiao, Aosong Feng, Dairui Liu, Yun Xing,
Junjue Wang, Fan Gao, et al. 2025.
MMLU-
ProX: A Multilingual Benchmark for Advanced
Large Language Model Evaluation. arXiv preprint
arXiv:2503.10497.
Shu-wen Yang, Po-Han Chi, Yung-Sung Chuang,
Cheng-I Jeff Lai, Kushal Lakhotia, Yist Y. Lin,
Andy T. Liu, Jiatong Shi, Xuankai Chang, Guan-
Ting Lin, Wei-Cheng Huang, Wei-Cheng Tseng,
Da-Rong Liu, Zili Huang, Shuyan Dong, Shang-
Wen Li Wang, Zhaoheng Ni Ma, Benjamin Chen,
Chih-Liang Chang, Kevin Lin, Wen-Chin Huang,
Andy T. Wu, Po-Chun Hsu, Chun-Lin Chen,
Han Lu Cheng, Yu Tsao, Hung-Yi Hsieh, and
Hung-Yi Lee. 2021. Superb: Speech processing
universal performance benchmark. In Proceed-
ings of Interspeech.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. HellaSwag: Can
a Machine Really Finish Your Sentence?
In
Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics, pages
4791–4800.
Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng
Gao, Kevin Duh, and Benjamin Van Durme. 2018.
Record: Bridging the gap between human and
machine commonsense reading comprehension.
arXiv preprint arXiv:1810.12885.
Chengzhi Zhong, Fei Cheng, Qianying Liu, Jun-
feng Jiang, Zhen Wan, Chenhui Chu, Yugo Mu-
rawaki, and Sadao Kurohashi. 2024. Beyond
English-centric LLMs: What language do multi-
lingual language models think in? arXiv preprint
arXiv:2408.10811.
A.
Appendix
In Tables 1, 2, 3 and 4, we provide the full proposed
taxonomy for LLM benchmarks along with category
descriptions and examples.

--- Page 14 ---

Level
Category
Explanation
1
Language capabilities
Language-related tasks and scenarios that evaluate core
linguistic skills of large language models (LLMs), including
natural language understanding, generation, and interaction
in human language.
1.1
Natural language understand-
ing and generation
Ability to interpret, process, and produce grammatically cor-
rect, coherent and contextually appropriate text.
1.1.1
Comprehension
Understanding text meaning, intent, and details in written or
spoken input. E.g., the English question-answering BoolQ
(Clark et al., 2019) dataset, ReCoRD (Reading Comprehen-
sion with Commonsense Reasoning, Zhang et al., 2018)
dataset, and Multi-Sentence Reading Comprehension (Mul-
tiRC, Khashabi et al., 2018) dataset, the English RTE (Rec-
ognizing Textual Entailment, Giampiccolo et al., 2007) and
Hungarian HuRTE (Ligeti-Nagy et al., 2024) datasets, and
others.
1.1.2
Context sensitivity
Identifying meaning, tone or style from contextual clues
and responding accordingly; maintaining consistency across
longer discourse. E.g., the English WiC (Words in Context,
Pilehvar and Camacho-Collados, 2019) dataset.
1.1.3
Natural language inference
Determining a relationship between sentences, e.g., whether
they contradict, entail, or are neutral to each other. E.g., the
English CommitmentBank (De Marneffe et al., 2019) dataset
and the Hungarian CommitmentBank Corpus (HuCB, Ligeti-
Nagy et al., 2024), the Slovene Natural Language Inference
Dataset SI-NLI (Klemen et al., 2022) and the Hungarian
anaphora resolution datasets (HuWNLI, Vadász and Ligeti-
Nagy, 2022).
1.1.4
Summarization
Condensing text while preserving key information and in-
tent. E.g., the English CNN/DailyMail text summarization
benchmark (Nallapati et al., 2016), and the English BillSum
benchmark for legal text summarization (Kornilova and Ei-
delman, 2019).
1.2
General linguistic competence
Mastering grammar, style, and pragmatic use of language.
1.2.1
Grammar
Producing text that is grammatically correct in terms of
syntax, identifying grammatical errors or correcting them.
E.g., the Benchmark of Linguistic Minimal Pairs for English
(BLiMP, Warstadt et al., 2020), the English Corpus of Linguis-
tic Acceptability (CoLA, Warstadt et al., 2019) and Hungar-
ian Corpus of Linguistic Acceptability (HuCOLA, Ligeti-Nagy
et al., 2024), and the Polish linguistic and cultural compe-
tency benchmark (PLCC, Dadas et al., 2025) dataset.
1.2.2
Style
Identifying the tone, register, or rhetorical style in an input
or generating the output in the appropriate tone, register or
rhetorical style. E.g., the English Grammarly’s Yahoo An-
swers Formality Corpus (GYAFC) for benchmarking formality
style transfer (Rao and Tetreault, 2018).
1.2.3
Conversation & pragmatics
Identifying the intent of the written and spoken output and
other social aspects of communication, such as politeness,
sarcasm, emotions, implicit and figurative meaning. E.g., the
multilingual MultiPragEval (Park et al., 2024) and the Slove-
nian SloPragEval pragmatics understanding benchmarks,
the English IMDB (Maas et al., 2011) and multilingual Par-
laSent (Mochtak et al., 2023; Mochtak et al., 2024) sentiment
identification datasets, English EN-GINCO and Slovenian
GINCO automatic genre identification benchmark (Kuzman
et al., 2023; Kuzman et al., 2021), and the English Stanford
Politeness Corpus (Danescu-Niculescu-Mizil et al., 2013).
Table 1: Hierarchy of LLM Benchmark Categories (part 1).

--- Page 15 ---

Level
Category
Explanation
1.3
Specific linguistic competence
Mastering specific uses of language, such as creative or
specialized language.
1.3.1
Creativity
Producing original, novel, or imaginative language (e.g.,
storytelling, poetry, jokes).
1.3.2
Terminology & specialized
language
Correct use and understanding of domain-specific vocabu-
lary and professional jargon.
1.3.3
Language varieties
Benchmarks evaluating diverse forms of language use, in-
cluding child language, second-language learners, and atyp-
ical communication.
1.4
Multilinguality
Ability to operate across languages and dialects.
1.4.1
Translation
Rendering meaning from one language to another with
fidelity. E.g., the Flores-101 and FLORES-200 datasets
(Goyal et al., 2022), the translation tasks in the BenchMax
(Huang et al., 2025) dataset, and the machine translation
benchmarks in the Slovenian SloBENCH evaluation frame-
work (https://slobench.cjvt.si).
1.4.2
Code-switching / multilingual
interaction
Ability to detect the use of multiple languages, identify which
language is being used, and to mix languages fluidly within
discourse.
1.4.3
Dialectal capabilities
Understanding or generating dialectal or regional variations.
E.g., the DIALECTBENCH (Faisal et al., 2024) dataset.
1.5
Speech
Understanding and generation of spoken language, mastery
of intonation, prosody, and other features unique to speech.
E.g., tasks in the English Speech processing Universal PER-
formance Benchmark (SUPERB, Yang et al., 2021) and
its multilingual extension, the Multilingual Speech process-
ing Universal PERformance Benchmark (ML-SUPERB, Shi
et al., 2023).
1.5.1
Speech understanding
The ability to transcribe speech and extract meaning, intent,
and emotion from spoken input. E.g., the Slovenian Speech
Recognition benchmark in the SloBENCH evaluation frame-
work (https://slobench.cjvt.si).
1.5.2
Speech generation
Generating natural-sounding speech with control over
prosody, emotion, and speaker features.
1.5.3
Speech-specific interaction
Managing multi-turn spoken dialogue, maintaining conver-
sational grounding, and understanding paralinguistic cues.
1.6
Cultural competence
Understanding culturally-specific concepts and awareness of
cultural context, norms, and values in communication. E.g.,
the Polish linguistic and cultural competency benchmark
(PLCC, Dadas et al., 2025).
1.7
Multimodality
Mastering tasks across multiple input/output formats
(e.g.,
text,
speech,
sign language,
audiovisual sig-
nal).
E.g.,
the
Polish
Cultural
Vision
Benchmark
(PCVB, https://huggingface.co/spaces/speakleash/Polish_
Cultural_Vision_Benchmark).
Table 2: Hierarchy of LLM Benchmark Categories (part 2).

--- Page 16 ---

Level
Category
Explanation
2
Knowledge and reasoning
Generating output that is consistent with established facts
and real-world knowledge, logical reasoning and problem
solving.
2.1
General knowledge
Broad world knowledge across common domains and estab-
lished facts. E.g., the English Massive Multitask Language
Understanding (MMLU, Hendrycks et al., 2021) and its trans-
lations into European languages (Thellmann et al., 2024)
and other languages (Singh et al., 2024), the English Wino-
grad Schema Challenge (WSC, Levesque et al., 2012), the
English WikiFact benchmark (Petroni et al., 2019), and oth-
ers.
2.2
Domain-specific knowledge
Specialized knowledge in professional or technical areas.
2.2.1
Math
Numerical reasoning, problem solving, and formal proofs.
E.g., the English Omni-MATH (Mathematical Reasoning)
dataset (Gao et al., 2024), certain tasks in the English BIG-
bench (Beyond the Imitation Game Benchmark, Srivastava
et al., 2023) and LiveBench (White et al., 2024) benchmarks.
2.2.2
Law
Generating output that is consistent with relevant laws,
cases, and regulations, and performing various forms of
legal reasoning, including issue-spotting and interpretation.
E.g., the English BillSum benchmark (Kornilova and Eidel-
man, 2019) for legal text summarization and the English
LegalBench benchmark of legal reasoning tasks (Guha et al.,
2023).
2.2.3
Finance
Knowledge of economic principles, financial systems, and
reasoning over markets, investments, and accounting.
2.2.4
Medicine
Knowledge of biomedical concepts and interpretation of med-
ical information for diagnostics and treatment. E.g., the En-
glish MedQA benchmark (Jin et al., 2021) and the Polish
medical leaderboard (Wróbel et al., 2024).
2.3
Reasoning
Processing and reasoning about information logically, draw-
ing inferences and problem-solving. This includes under-
standing cause-and-effect scenarios.
E.g., the English
ReCoRD (Reading Comprehension with Commonsense
Reasoning, Zhang et al., 2018) dataset, the English Hel-
laswag (Zellers et al., 2019) dataset and its translation into
20 other European languages EU20-HellaSwag (Thellmann
et al., 2024), the English COPA (Roemmele et al., 2011)
dataset and its translations into Hungarian (Ligeti-Nagy et al.,
2024), Croatian (Ljubešić and Lauc, 2021; Ljubešić, 2021),
a Slovenian Cerkno dialect (Ljubešić et al., 2024) and other
languages and dialects.
2.4
Agency
Sustained long-term planning, strategic reasoning and con-
sistent decision-making over extended interactions. E.g.,
certain tasks from the English LiveBench (White et al., 2024)
benchmark.
Table 3: Hierarchy of LLM Benchmark Categories (part 3).

--- Page 17 ---

Level
Category
Explanation
3
Safety
and
trustworthi-
ness
Benchmarks that evaluate the model’s reliability and its risks,
that is, whether it behaves reliably, predictably, ethically, and
without harm.
3.1
Misinformation
Detecting or generating false or misleading information. E.g.,
the English TruthfulQA dataset (Lin et al., 2022) and its trans-
lation into 20 other European languages EU20-TruthfulQA
(Thellmann et al., 2024).
3.2
Toxicity
Identifying offensive, abusive, or harmful language, and
avoiding its use. Includes tasks such as hate speech detec-
tion. E.g., the English CivilComments benchmark (Borkan
et al., 2019), and the Toxicity benchmark in the English De-
codingTrust benchmark collection (Wang et al., 2023).
3.3
Bias
Detection and mitigation of stereotypes or unfair treatment
across groups. Includes benchmarks that assess whether
a model’s performance on a task is unjustifiably different
across different groups and attributes. E.g., the English
Winogender Schema Diagnostics dataset (Rudinger et al.,
2018) and the Fairness and Stereotype benchmarks in the
English DecodingTrust benchmark collection (Wang et al.,
2023).
3.4
Machine ethics
Adherence to ethical principles and moral reasoning in re-
sponses, ability to distinguish between moral and immoral
actions. E.g., the Machine Ethics benchmark in the English
DecodingTrust benchmark collection (Wang et al., 2023).
3.5
Psychological traits
Assessing model’s characteristics that are typically associ-
ated with human personalities.
3.6
Robustness
Reliability under adversarial input, noise, or perturbations.
E.g., the Adversarial Robustness, Out-of-Distribution Ro-
bustness, and Robustness against Adversarial Demonstra-
tions benchmarks in the English DecodingTrust benchmark
collection (Wang et al., 2023).
3.7
Data governance
Benchmarks that assess whether models leak their training
data in their responses. E.g., the Privacy benchmark in the
English DecodingTrust benchmark collection (Wang et al.,
2023).
4
Alignment and dangerous
capabilities
Benchmarks that evaluate model capabilities that could have
catastrophic consequences, including dangerous capabil-
ities (cyber operations, weapons acquisition, autonomous
replication) and alignment risks (power-seeking behavior,
shutdown resistance). This category includes tasks that
assess whether the model is able to detect and exploit vul-
nerabilities in hardware, software and data, whether the
model can contribute to the development of weapon tech-
nologies, whether the model possesses information about
itself and its creators, whether it can break free from its oper-
ational confines, or whether it is capable of persuasion and
manipulation.
Table 4: Hierarchy of LLM Benchmark Categories (part 4).

```
