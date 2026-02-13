---
title: "2026-Lab-SDU's DAISY A Benchmark for Danish Culture - PDF Extract"
source_pdf: "2026-Lab-SDU's DAISY A Benchmark for Danish Culture.pdf"
pages: 11
extracted_at: "2026-02-13T13:14:08.732190"
---

# PDF Extract: 2026-Lab-SDU's DAISY A Benchmark for Danish Culture

**Source PDF:** 2026-Lab-SDU's DAISY A Benchmark for Danish Culture.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

SDUs DAISY: A Benchmark for Danish Culture
Jacob Nielsen and Stine L. Beltoft and Peter Schneider-Kamp and Lukas Galke Poech
University of Southern Denmark
Abstract
We introduce a new benchmark for Danish cul-
ture via cultural heritage, Daisy, based on the
curated topics from the Danish Culture Canon
2006. For each artifact in the culture canon,
we query the corresponding Wikipedia page
and have a language model generate random
questions.
This yields a sampling strategy
within each work, with a mix of central of
peripheral questions for each work, not only
knowledge of mainstream information, but also
in-depth cornerstones defining the heritage of
Danish Culture, defined by the Canon commit-
tee. Each question-answer pair is humanly ap-
proved or corrected in the final dataset consist-
ing of 741 close-ended question answer pairs
covering topics, from 1300 BC. archaeologi-
cal findings, 1700 century poems and musi-
cals pieces to contemporary pop music and
Danish design and architecture.
The ques-
tions, model benchmarks and the evaluation
tool are publicly available at https://github.
com/schneiderkamplab/SDU-Daisy.
1
The Missing Danish Benchmarks
Large Language Models (LLMs) have demon-
strated remarkable capabilities across diverse natu-
ral language processing tasks (Bubeck et al., 2023),
yet their cultural knowledge has been so far un-
derstudied, particularly for non-English linguistic
contexts (Tao et al., 2024). While considerable re-
search has examined the performance of LLMs on
English-language benchmarks (Phan et al., 2025)
and culturally Anglo-centric tasks (Hershcovich
et al., 2022), the representation and understand-
ing of non-dominant cultures in these models has
received comparatively little yet increasing atten-
tion (Liu et al., 2025). This disparity is especially
pronounced for low-resource languages, where lim-
ited training data and evaluation frameworks com-
pound the challenges of assessing and improving
model performance. Danish exemplifies these chal-
lenges. Despite being spoken by approximately
six million people and representing a rich cultural
tradition spanning millennia, Danish is considered
a low- to medium-resource language in contempo-
rary AI research. More critically, no standardized
benchmark exists for assessing Danish culture via
heritage in LLMs. This absence creates substantial
obstacles for both model evaluation and develop-
ment: researchers and practitioners lack system-
atic methods to measure how well models capture
Danish cultural knowledge, historical context, and
linguistic nuances that extend beyond mere lan-
guage proficiency. Without such benchmarks, the
development of Danish language models proceeds
without adequate feedback mechanisms, resulting
in minimal focus on preserving and accurately rep-
resenting Danish cultural heritage in AI systems.
The need for culturally-grounded evaluation
frameworks extends beyond academic interest.
As LLMs become increasingly integrated into
educational systems, cultural institutions, and
public services and different types of analysis
tasks, their ability to accurately represent and
engage with local cultural knowledge becomes
essential.
Misrepresentation or omission of
cultural content can perpetuate biases, erode
cultural identity, and limit the utility of these
technologies for non-English speaking populations.
For smaller linguistic communities, the risk is
particularly acute: without dedicated evaluation
frameworks, model developers may overlook
culturally significant content in favor of more
widely represented cultural materials.
Here, we introduce SDU’s Daisy1.
To cre-
ate Daisy, we leverage the Kulturkanon, a col-
lection of Danish cultural heritage (details in §2),
as a foundational reference to introduce the first
culturally-grounded benchmark for evaluating Dan-
1Daisy, the nickname of the Danish Queen Margrethe II
and the Danish national flower.
1
arXiv:2601.19930v1  [cs.CL]  11 Jan 2026

--- Page 2 ---

Figure 1: Overview of the stages in Daisy’s Generation Pipeline.
ish language models (see Figure 1). By ground-
ing our evaluation framework in an authoritative
and widely-recognized cultural reference, we ad-
dress a critical gap in multilingual and multicultural
AI assessment (Liu et al., 2025). This benchmark
enables systematic evaluation of how well LLMs
capture Danish cultural knowledge, providing re-
searchers and practitioners with essential tools for
model development, comparison, and improvement.
Our main contributions are:
• The development of a novel benchmark based
on authoritative cultural materials,
• Baseline evaluations of contemporary LLMs,
which already are decent at Danish, Danish
cultural understanding.
• Insights into the challenges and opportunities
for improving cultural representation in lan-
guage models for low-resource languages.
Below, we first briefly describe the Danish Cul-
ture canon (§2), before we introduce the Daisy
benchmark (§3). Subsequently, we provide base-
line results on Daisy (§4) and enter a discussion to
contextualize Daisy with related previous resources
(§5), before we conclude.
2
The Danish Culture Canon -
Kulturkanon
The Kulturkanon (Culture Canon) (Kulturminis-
teriet, 2006) was established in 2006 by the Danish
government, the Cultural Ministry, following a na-
tional initiative that began in 2005. This canonical
collection represents an authoritative, curated com-
pilation of Danish cultural heritage designed to
define and preserve the nation’s cultural identity
for future generations. The canon encompasses 108
works distributed across eight distinct cultural do-
mains: architecture, visual arts, design and crafts,
film, literature, children’s literature, music, per-
forming arts (theater and dance), radio, television,
cuisine, and digital culture. Each of the domains
with 12 selected works. The temporal scope of the
Kulturkanon is remarkably broad, featuring arti-
facts ranging from archaeological findings dated to
1300 BCE through contemporary works, thereby
providing a comprehensive historical perspective
on Danish cultural achievement.
The selection process for the Kulturkanon in-
volved extensive expert consultation across mul-
tiple cultural sectors, with committees of distin-
guished scholars, practitioners, and cultural author-
ities deliberating on representative works within
each domain. This rigorous curation process, com-
bined with official governmental endorsement, es-
tablishes the Kulturkanon as the definitive refer-
ence for Danish cultural heritage. The canon’s
explicit pedagogical purpose, to be integrated into
educational curricula and serve as a foundation for
cultural literacy, further reinforces its authoritative
status within Danish society.
The Kulturkanon’s suitability as a benchmark
foundation stems from several key characteristics.
First, its official status and broad expert consen-
sus provide legitimacy and representativeness that
user-generated or algorithmically-derived datasets
cannot match. Second, the canon’s explicit design
as a reference for cultural knowledge aligns di-
rectly with the evaluation objectives of measuring
LLM understanding of Danish culture. Third, the
diversity of domains and historical periods repre-
2

--- Page 3 ---

sented ensures comprehensive coverage of Danish
cultural heritage rather than narrow topical focus.
Finally, the canon’s established role in Danish ed-
ucation and cultural discourse means that knowl-
edge of these works represents genuine cultural
competence rather than obscure trivia, making it an
ecologically valid basis for evaluation.
Kulturkanon primarily corresponds to the
ideational elements of Liu’s taxonomy (Liu et al.,
2025), especially the subcategory of knowl-
edge/artefacts, since it is essentially a curated col-
lection of canonical works in literature, art, archi-
tecture, music, design, film, and performing arts.
However, Kulturkanon also implicitly involves cer-
tain social elements of culture: by selecting and
elevating particular works as nationally significant,
it participates in shaping collective memory, na-
tional identity, and shared cultural reference points.
In this way, Kulturkanon contributes to the social
meaning and institutional framing of culture, even
though it does not explicitly catalogue everyday
practices, linguistic norms, communicative con-
ventions, or behavioural patterns. Thus, while the
canon is firmly rooted in ideational content, it si-
multaneously reflects, at a more indirect level, so-
cial identity formation and cultural legitimation
processes, but it does not encompass the broader
social or linguistic elements included in Liu’s tax-
onomy.
3
The Daisy Benchmark
We build upon the Danish culture canon as an es-
tablished resource, to create the Daisy benchmark.
By creating questions and answers based on the
Culture Canon we have set up a dataset that rep-
resents the Danish cultural heritage as defined by
the Danish state. This evaluation dataset allows
for us to see how much, especially large interna-
tional models, perform when confronted with very
specific Danish knowledge.
3.1
Constructing the Dataset
We generate the dataset by extracting each of the
Culture Canon’s work’s wiki pages, which contains
detailed information about each work in different
lengths depending on the type of work. Question-
answer pairs are generated by Gemma3 27B in a
4-bit quantization. The model is prompted with the
respective page’s content as input, asked to gener-
ate 5 random questions within a framework defined
by the our generation prompt, which we report in
Appendix A. This is essentially a sampling strategy
within each work, generating a mix of central and
peripheral questions for each work. We believe
makes the dataset a harder benchmark, not only
testing mainstream information but in-depth knowl-
edge about corner-stones defining the heritage of
Danish culture.
The dataset consists of 741 question answer pairs
from the Wikipedia’s pages about the culture canon
entities, leaving out the children’s canon for now.
We omit 6 of the pages, because of missing web-
pages and one due to incompleteness. We still get
741 pairs because we include actual work’s from
grouped in subtitles, e.g.: ’4 revynumre’ counts as
one entity, but is 4 independent works. The pairs
is validated by multiple human annotators, who
made sure that the questions is valid, correct and
made sense out of context, with no implicit set-
ting meaning, before they were promoted into the
benchmark. Some pairs was removed due to errors
or noise and some rewritten to be more concise,
relevant or correct.
3.2
Evaluation Measures
The models are evaluate the models by prompting
them with instructions on the simple answering for-
mat. The instructions is broadly that height is given
in meters, weights in kg, size e.g. picture-frame in
width and weights. The models are instructed to
only give the answer itself. We provide the prompt-
template used for evaluation in Appendix B. We
evaluate the models by normalization the answer
by employing case normalization, remove punctua-
tion, articles and extra white space. The F1 Score
is computed on word level, formulated as:
Precision = |tokenspred ∩tokensgold|
|tokenspred|
(1)
Recall = |tokenspred ∩tokensgold|
|tokensgold|
(2)
F1 = 2 · Precision · Recall
Precision + Recall
(3)
We formulate it with overlapping sets, to be as open
as possible for small deviations in generation pos-
sible, even though the questions are closed sourced.
By inspecting the outputs of each model, we can
confirm that this strategy is enough. The BLEU
score is calculated with NLTK’s sentence_bleu
function2, given the predictions, ground truth and
2https://www.nltk.org/_modules/nltk/translate/bleu_score.html
3

--- Page 4 ---

Table 1: Samples of 4 questions with answers. Correct answers are marked in bold. No final answer is marked
using ’-’.
GPT-OSS
Mistral-Small 3.1 Instruct 2503
Llama 3.3
Gemma 3
Question
20B
120B
24B
70B
27B
Hvem skrev
salmen *De
levendes
Land*?
Lars M. Jensen
Niels Bjerre
N.F.S.
Grundtvig
N.F.S.
Grundtvig
Thomas Kingo
I hvilket år
åbnede
jernbane-
forbindelsen
over
Storebælt?
1998
1998
1997
1998
1997
Hvem er
sangskriveren
bag *Kald det
kærlighed*?
-
Rasmus
Seebach
Lasse Lindorff
Rasmus
Seebach
Rasmus
Seebach
Hvem
designede
Ferrishjulet?
Thomas
Skovbjerg
Jens Martin
Skibsted
Jens Martin
Skibsted og
Jakob Jensen
George
Washington
Gale Ferris Jr.
Charles Ferris
the SmoothingFunction().method42 function, to
account for the small generated lengths, making
the results more generally comparable.
3.3
Characteristics of the Benchmark
The benchmark consists of close ended, one true
predefined answer, QA pairs within architecture,
art, design & crafts, movies, literature, music, pop-
ular music and performing arts. The nature of the
questions is quite diverse and can be factual ques-
tions about an invention or art piece like it’s physi-
cal dimensions or where it is geographically from.
There is also pairs containing questions on a given
author author two a poem, song or performing arts
- and even the number of notes in musical pieces.
Furthermore, there is questions about architectures,
like buildings and bridges, including when they
were build and opened for use. We provide exam-
ples in Table 1’s first column.
4
Baseline Results
We report our baseline evaluations in Table 2 and
some examples in Table 1. None of the evaluated
models is performing very well, even though they
are considered decent at generating correct Danish.
LLama 3.3 70B outperforms all the newer mod-
els by quite a large margin, with a BLEU score of
0.166, with GPT-OSS 120B as second best with
a BLEU score of 0.126. Gemma3 27B, which
is often considered one of the better models in
generating Danish (Smart, 2023), evidently lacks
factual knowledge about Danish culture, underlin-
ing not only the performance gab of Danish as a
low-resource language, but also the gab between
language and culture, which could be a artifact of
synthetic training data. In Table 1, we show the
outputs for each models across 5 different ques-
tions from Daisy. Generally, all models generate
reasonable valid outputs, except for GPT-OSS-20B,
which sometimes needs a reasoning trace over 2000
tokens, before having an answer, in which case we
drop the answer. However, generally all models an-
swers sporadic correct, with a few questions where
the majority is corrected, which can be seen in
Table 3’s row 1 and 5.
5
Discussion and Related Work
Benchmarking cultural knowledge in language
models has important implications to both the gen-
eral society, as well as the research community.
First, having a measurement for the presence of
Danish culture heritage in existing models, can
shed light on the missing cultural alignment and ex-
pected performance in existing models. Enabling
benchmarking on curated datasets can guide re-
searchers and practitioners in developing new mod-
els - and enable foreign entities to evaluate their
models. Further, it will support research in digital
humanities in investigating the existence of Danish
culture in models, as well as expected the inter-
action width the models, based on the evaluated
cultural understanding of the model, which also
4

--- Page 5 ---

Table 2: Evaluation of various models Daisy. All evaluation is using prompt- and dataset version 1.
Model
BLEU Score
F1 Score
openai/gpt-oss-20b
0.062
0.112
openai/gpt-oss-120b
0.126
0.211
google/gemma-3-27b-it
0.123
0.193
meta-llama/Llama-3.3-70B-Instruct
0.166
0.268
mistralai/Mistral-Small-3.1-24B-Instruct-2503
0.124
0.202
will support research in critical AI studies.
As reported in Table 2, the models generally ex-
hibit poor performance on Daisy, despite that it is
very likely that data from Danish Wikipedia was
included in their training data. We hypothesise
that these shortcomings may stem from the limited
representation of Danish-language and Denmark-
specific content within the overall training data
distribution, where such nationally bounded knowl-
edge constitutes a relatively weak signal. In addi-
tion, preference alignment and safety tuning may
further bias models toward cautious, generalized
responses rather than confident enumeration of
closed cultural lists. Together, these factors sug-
gest that the observed failures reflect not missing
data per say, but how culturally specific knowledge
is weighted, abstracted, and retrieved across the
training and alignment pipeline.
We now discuss how Daisy relates to previously
introduced language resources that were designed
to evaluate language models on Danish culture.
5.1
Danish Benchmarks
While Danish NLP has seen notable development
in recent years, existing benchmarks focus primar-
ily on linguistic capabilities rather than cultural
knowledge. ScandEval, a natural language under-
standing benchmark, evaluates Danish models on
tasks including named entity recognition, sentiment
classification, linguistic acceptability, and ques-
tion answering (Smart, 2023). The benchmark has
been used to evaluate Danish language models like
SnakModel on both language and culture-specific
tasks (Zhang et al., 2025), though the cultural com-
ponent remains limited. DaCy provides a unified
framework for Danish NLP with capabilities in
named entity recognition, part-of-speech tagging,
and dependency parsing (Enevoldsen et al.), but
does not explicitly assess cultural knowledge. Re-
cent work at the University of Copenhagen has
developed a benchmark for evaluating the intrinsic
reasoning capabilities of Danish LLMs based on
semantic dictionaries (Pedersen et al., 2024), fo-
cusing on semantic reasoning rather than cultural
content. The DaNLP repository offers various Dan-
ish NLP resources and datasets, while multilingual
evaluation frameworks like Okapi include Danish
among 26 languages for tasks like ARC (Clark
et al., 2018), HellaSwag (Zellers et al., 2019), and
MMLU (Hendrycks et al., 2021), though these are
translations of English benchmarks rather than cul-
turally grounded assessments. To our knowledge,
no existing Danish benchmark systematically eval-
uates cultural knowledge or heritage understand-
ing, representing a significant gap that our work
addresses.
DaKultur represents the first cultural evalua-
tion study for Danish, comprising 1,038 interac-
tions from 63 demographically diverse participants
(Müller-Eberstein et al., 2025).
The study em-
ployed a crowdsourcing methodology, where partic-
ipants compose prompts requiring Danish cultural
knowledge, which are then answered by three dif-
ferent language models and subsequently rated by
participants through accept/reject judgments. How-
ever, the crowdsourcing nature of the prompt gener-
ation reveals significant conceptual ambiguities re-
garding what constitutes culturally relevant knowl-
edge.
Several examples illustrate this concern:
(1) "Kender du Faser?" (Do you know Faser?),
which appears to reference niche recent pop cul-
ture rather than shared cultural understanding; (2)
"Hvad bestiller danskerne på en cafe?" (What do
Danes order at a café?), which elicits stereotypi-
cal behavioral patterns rather than deeper cultural
values or norms; (3) "Må man plukke svampe i
skoven?" (Is one allowed to pick mushrooms in the
forest?), which tests legal or practical knowledge
rather than cultural competence; and (4) "Planlæg
en fed dag i København med udendørs aktiviteter"
(Plan a cool day in Copenhagen with outdoor ac-
tivities), which functions more as a practical rec-
ommendation task than a cultural evaluation. More
problematically, questions such as "Hvordan er
danske familier?" (What are Danish families like?)
demand broad generalizations that risk reducing
complex, heterogeneous social structures to reduc-
tive stereotypes. Any response that purports to
5

--- Page 6 ---

characterize "Danish families" as a monolithic en-
tity necessarily obscures intra-cultural variation
across class, region, generation, and individual
family dynamics. This raises a fundamental ques-
tion: does cultural competence require the ability
to produce such generalizations, or does it instead
demand recognition of cultural diversity and resis-
tance to essentialization? The dataset’s reliance
on participant-generated prompts, while democra-
tizing the evaluation process, may thus inadver-
tently conflate various forms of knowledge, factual,
practical, stereotypical, and cultural, without ade-
quately distinguishing between them.
A related consideration is the frequent use of
the indfødsretsprøven (Danish citizen tests) as a
benchmark for “Danish cultural knowledge” in
LLM evaluation (Kirilova, 2025). Methodologi-
cally, its usefulness is limited: the test and its an-
swer key circulate widely online, making it highly
probable that most foundation models have already
been exposed to it during training and therefore
perform well for reasons unrelated to genuine cul-
tural understanding. More importantly, there is
a conceptual issue. While indfødsretsprøven is
a state-administered instrument, it is designed to
evaluate civic compliance and basic knowledge rel-
evant for naturalisation, not to provide a culturally
or symbolically meaningful account of Danishness.
In this sense, it operationalises a narrow, politically
contingent definition of culture. The Kulturkanon,
although also a state-initiated project and there-
fore not free from ideological framing, represents
a different category of cultural artefact: a curated
attempt to articulate Denmark’s artistic, historical,
and aesthetic heritage. Using it as a benchmark
does not resolve the normative question of who
gets to define culture, but it shifts the evaluative
focus from administrative facts to culturally em-
bedded works and references, offering a more sub-
stantively grounded, though still contestable, basis
for assessing models’ cultural competence.
Danish Dynaword (Enevoldsen et al., 2025) is
not directly focused on Danish culture, but rather
curated Danish pre-training data, potentially im-
plicitly containing cultural artifacts.
5.2
International Benchmarks
Our work draws inspiration from recent interna-
tional efforts to develop culturally-grounded evalu-
ation frameworks for LLMs. CulturalBench intro-
duced 1,696 human-written and verified questions
covering 45 global regions across 17 topics, reveal-
ing that even frontier models like GPT-4o achieve
only 61.5% accuracy on challenging cultural ques-
tions (Chiu et al., 2025).
BLEnD provides a complementary perspec-
tive by focusing on everyday cultural knowledge
across 16 countries and 13 languages, with 52,600
question-answer pairs covering mundane aspects of
daily life often absent from online sources (Bat-El
and Brown, 2006). This emphasis on culturally-
specific common knowledge that may not appear in
training data resonates with our goal of evaluating
genuine cultural understanding. Other benchmarks
like
GlobalOpinionQA and culturally-aware natural
language inference (NLI) have provided founda-
tions for cultural evaluation, though they are often
limited by their classification-based nature (Dur-
mus et al., 2023).
Multicultural Resource for Evaluation Language
Models (MUREL) is a curated dataset of 85.2M
tokens spanning 6 cultures derived from 69 source
datasets, which includes 11M tokens encoding Dan-
ish culture (Namazifard and Galke, 2025). The
dataset covers ideational, linguistic and social di-
mension targets for analysis of culture-specific phe-
nomenons, but does not explicitly cover factual
knowledge regarding cultural heritage.
MultiWikiQA (Smart, 2025) is a reading compre-
hension dataset covering 306 languages, based on
Wikipedia articles. The dataset conducts a crowd-
source human evaluation of fluency of the gener-
ated across 30 of the languages, hence not focusing
or cultural engagement nor particularly cultural
knowledge in contrast to Daisy’s focus on the cul-
tural factual knowledge.
Domain-specific cultural heritage benchmarks
have emerged for other contexts, such as evalua-
tion frameworks for Chinese intangible cultural her-
itage using data from authoritative national sources
(Zhao and Wang, 2025), demonstrating the value
of grounding benchmarks in official cultural repos-
itories.
Our approach of leveraging the Kulturkanon sim-
ilarly draws on authoritative national cultural defi-
nitions while adapting the methodology to the spe-
cific context of Danish heritage and the compre-
hensive scope of the canon’s twelve domains. The
present work distinguishes itself from these prece-
dents by combining the authoritative grounding
of nationally-defined cultural heritage with com-
prehensive domain coverage and the specific chal-
lenges of evaluating low-resource language mod-
6

--- Page 7 ---

els on culturally-nuanced content. Our benchmark
uniquely addresses the intersection of official cul-
tural heritage, comprehensive artistic and intellec-
tual domains, and the evaluation needs of Danish
language technology development.
Even in Humanity’s Last Exam (Phan et al.,
2025), a benchmark explicitly framed as testing
“the forefront of human knowledge”, the centre
of gravity remains firmly in the natural sciences
and mathematically structured domains. This re-
veals a persistent assumption in AI evaluation: that
knowledge is best represented through problems
with clear formal structure and objectively scorable
answers. But knowledge is far more expansive than
mathematics. If we ever reach a point where a “last
exam” for humanity is meaningful, it will have
to include the interpretive, historical, social, and
cultural forms of understanding that shape human
life. Humanities disciplines, history, sociology, an-
thropology, literature, philosophy, capture dimen-
sions of meaning, value, and context that cannot
be reduced to equations or symbolic manipulation.
To take the idea of such an exam seriously, we
must broaden our evaluative horizons to include
precisely the kinds of cultural and interpretive com-
petencies that define human experience, rather than
only the domains where machines are already most
comfortable.
6
Conclusion
We have introduced SDU’s Daisy, a cultural closed-
ended question-answer benchmark, rooted in the
Danish Culture Canon spanning 741 questions
pairs across cultural heritage.
We have bench-
marked the dataset across 5 contemporary models
that is either popular or deemed being good at the
Danish language. Daisy can serve as an initial cul-
tural beacon within the Danish Foundation Models
(DFM) initiative, illuminating the current state of
development of Danish-specific models, and more
generally providing guidance for the wider com-
munity and future generations of models. We plan
to extend the fleet of Danish culture datasets and
welcome contributions for sub-domain experts.
7
Limitations
Scope and Representativeness
Daisy is centred
around the Danish Culture Canon. Although a well-
established resource, the benchmark is naturally
limited by that scope. We do not argue that the
Canon contains nor represents the whole Danish
culture heritage. Culture is a lot more diverse and
never ending, always developing with society. This
also means that the culture canon is quite some
years delayed, regarding new culture, however, we
also see that this means the artifacts within the
benchmark has been digested and can be expected
to be represented so generally that they should be
recognizable by a given LLM exiling in Danish and
Danish culture.
Single Prompt Evaluation
Evaluating genera-
tive models is hard. In our benchmarking, we are
dependent on a prompt giving the models instruc-
tion on the task as well as the expected output
format. We report the exact template in Appendix
B. This prompt is not necessarily optimal for all
model, nor necessarily optimal at all. Therefore we
already report it as Prompt Template Version 1. We
plan to iterate over the prompt in the future calling
for the community to engage with us to improve
and exspand Daisy in general.
8
Ethical Considerations
The measurement of culture remains a contentious
endeavor within the social sciences, with schol-
ars rightfully cautioning against the reductionism
inherent in quantifying such a multifaceted and dy-
namic construct (Merry, 2016; Clifford and Marcus,
1986). For LLMs to effectively understand and gen-
erate context-specific language, however, they must
encode some representation of cultural knowledge,
the shared meanings, values, and communicative
norms that shape human expression across different
communities. Liu (Liu et al., 2025) provide a com-
prehensive taxonomy of cultural elements in NLP,
identifying key dimensions including cultural con-
cepts, knowledge, norms, values, and artifacts that
language models must navigate, as detailed in §2.
While the critique that culture resists simple quan-
tification is well-founded, the alternative, avoiding
systematic assessment altogether, is untenable if
we aspire to develop AI systems that authentically
reflect human diversity rather than defaulting to nar-
row cultural frames. Culture is not static but contin-
uously evolving, shaped by historical forces, tech-
nological change, and intercultural exchange. This
dynamic mirrors the rapid development cycle of AI
systems themselves, suggesting a productive par-
allel: can we develop LLMs that evolve alongside
the cultures they serve? Addressing this question
requires an initial framework, one that begins with
established dimensions of national culture (Hofst-
7

--- Page 8 ---

ede, 2011) not because these dimensions capture
the totality of cultural experience, but because they
provide empirically grounded starting points for
moving beyond the WEIRD (Western, Educated,
Industrialized, Rich, Democratic) paradigm (Hen-
rich et al., 2010) that dominates current AI devel-
opment. The major commercial LLMs, including
ChatGPT and similar systems, demonstrably reflect
American or broadly Western cultural assumptions
and ideological orientations (Tao et al., 2024; Cao
et al., 2023; Naous et al., 2024). To develop more
culturally contextualized systems, we must first
establish methods to systematically measure and
compare cultural representations, a pragmatic ne-
cessity given that AI systems, by their very nature,
require operationalizable metrics for training and
evaluation.
References
Outi Bat-El and Keith Brown. 2006. Blend. Encyclope-
dia of language and linguistics, 2:66–70.
Sébastien Bubeck, Varun Chandrasekaran, Ronen El-
dan, Johannes Gehrke, Eric Horvitz, Ece Kamar, Pe-
ter Lee, Yin Tat Lee, Yuanzhi Li, Scott Lundberg,
and 1 others. 2023. Sparks of artificial general in-
telligence: Early experiments with GPT-4. arXiv
preprint arXiv:2303.12712.
Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min
Chen, and Daniel Hershcovich. 2023.
Assessing
cross-cultural alignment between ChatGPT and hu-
man societies: An empirical study. In Proceedings of
the First Workshop on Cross-Cultural Considerations
in NLP (C3NLP), pages 53–67.
Yu Ying Chiu,
Liwei Jiang,
Bill Yuchen Lin,
Chan Young Park, Shuyue Stella Li, Sahithya Ravi,
Mehar Bhatia, Maria Antoniak, Yulia Tsvetkov,
Vered Shwartz, and 1 others. 2025. Culturalbench: A
robust, diverse and challenging benchmark for mea-
suring lms’ cultural knowledge through human-ai red-
teaming. In Proceedings of the 63rd Annual Meeting
of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 25663–25701.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018.
Think you have solved question
answering?
try arc, the ai2 reasoning challenge.
arXiv:1803.05457v1.
James Clifford and George E. Marcus, editors. 1986.
Writing Culture: The Poetics and Politics of Ethnog-
raphy. University of California Press, Berkeley.
Esin Durmus, Karina Nguyen, Thomas I Liao, Nicholas
Schiefer, Amanda Askell, Anton Bakhtin, Carol
Chen,
Zac Hatfield-Dodds,
Danny Hernandez,
Nicholas Joseph, and 1 others. 2023.
Towards
measuring the representation of subjective global
opinions in language models.
arXiv preprint
arXiv:2306.16388.
Kenneth Enevoldsen, Lasse Hansen, and Kristoffer L.
Nielbo.
DaCy: A unified framework for danish
NLP. In Ceur Workshop Proceedings, volume 2989
of CEUR Workshop Proceedings, pages 206–216.
ceur workshop proceedings.
Kenneth Enevoldsen, Kristian Nørgaard Jensen, Jan
Kostkan, Balázs Szabó, Márton Kardos, Kirten
Vad, Johan Heinsen, Andrea Blasi Núñez, Gianluca
Barmina, Jacob Nielsen, and 1 others. 2025. Dy-
naword: From one-shot to continuously developed
datasets. arXiv preprint arXiv:2508.02271.
Dan Hendrycks, Collin Burns, Steven Basart, Andy
Zou, Mantas Mazeika, Dawn Song, and Jacob Stein-
hardt. 2021. Measuring massive multitask language
understanding. Proceedings of the International Con-
ference on Learning Representations (ICLR).
Joseph Henrich, Steven J. Heine, and Ara Norenzayan.
2010. The weirdest people in the world? Behavioral
and Brain Sciences, 33(2-3):61–83.
Daniel Hershcovich, Stella Frank, Heather Lent,
Miryam de Lhoneux, Mostafa Abdou, Stephanie
Brandl, Emanuele Bugliarello, Laura Cabello Pi-
queras, Ilias Chalkidis, Ruixiang Cui, Constanza
Fierro, Katerina Margatina, Phillip Rust, and Anders
Søgaard. 2022. Challenges and strategies in cross-
cultural NLP. In Proceedings of the 60th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 6997–7013,
Dublin, Ireland. Association for Computational Lin-
guistics.
Geert Hofstede. 2011. Dimensionalizing cultures: The
Hofstede model in context. Online Readings in Psy-
chology and Culture, 2(1).
Marta Kirilova. 2025. indfødsretsprøven. Accessed:
2026-01-07.
Kulturministeriet. 2006. Kulturkanon. Kulturminis-
teriet. Officiel udgivelse.
Chen Cecilia Liu, Iryna Gurevych, and Anna Korho-
nen. 2025. Culturally aware and adapted nlp: A
taxonomy and a survey of the state of the art. Trans-
actions of the Association for Computational Linguis-
tics, 13:652–689.
Sally Engle Merry. 2016. The Seductions of Quantifi-
cation: Measuring Human Rights, Gender Violence,
and Sex Trafficking. University of Chicago Press,
Chicago.
Max Müller-Eberstein, Mike Zhang, Elisa Bassignana,
Peter Brunsgaard Trolle, and Rob Van Der Goot.
2025. Dakultur: Evaluating the cultural awareness
of language models for danish with native speakers.
arXiv preprint arXiv:2504.02403.
8

--- Page 9 ---

Danial Namazifard and Lukas Galke. 2025. Isolating
culture neurons in multilingual large language mod-
els. In AACL-IJCNLP Findings.
Tarek Naous, Weijie Xu, and Alan Ritter. 2024. Having
beer after prayer? Measuring cultural bias in large
language models. arXiv preprint arXiv:2305.14456.
Bolette Pedersen, Nathalie Sørensen, Sussi Olsen, Sanni
Nimb, and Simon Gray. 2024. Towards a Danish se-
mantic reasoning benchmark - compiled from lexical-
semantic resources for assessing selected language
understanding capabilities of large language mod-
els. In Proceedings of the 2024 Joint International
Conference on Computational Linguistics, Language
Resources and Evaluation (LREC-COLING 2024),
pages 16353–16363, Torino, Italia. ELRA and ICCL.
Long Phan, Alice Gatti, Ziwen Han, Nathaniel Li,
Josephina Hu, Hugh Zhang, Chen Bo Calvin Zhang,
Mohamed Shaaban, John Ling, Sean Shi, and 1 oth-
ers. 2025. Humanity’s last exam. arXiv preprint
arXiv:2501.14249.
Dan Saattrup Smart. 2023. ScandEval: A Benchmark
for Scandinavian Natural Language Processing. In
Proceedings of the 24th Nordic Conference on Com-
putational Linguistics (NoDaLiDa), pages 185–201.
Dan Saattrup Smart. 2025. MultiWikiQA: A reading
comprehension benchmark in 300+ languages. arXiv
preprint arXiv:2509.04111.
Yiming Tao, Olga Viberg, Ryan S. Baker, and René F.
Kizilcec. 2024.
Cultural bias and cultural align-
ment of large language models.
PNAS Nexus,
3(9):pgae346.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can a
machine really finish your sentence? arXiv preprint
arXiv:1905.07830.
Mike Zhang, Max Müller-Eberstein, Elisa Bassignana,
and Rob Van Der Goot. 2025. Snakmodel: Lessons
learned from training an open danish large language
model.
In Proceedings of the Joint 25th Nordic
Conference on Computational Linguistics and 11th
Baltic Conference on Human Language Technologies
(NoDaLiDa/Baltic-HLT 2025), pages 812–825.
Z. Zhao and D. Wang. 2025. Evaluation of large lan-
guage models for the intangible cultural heritage do-
main. npj Heritage Science, 13:439.
A
Generation Prompt Template
We use the generation prompt template, inducing
the context from a given document, with a set of
rules, which is formulated based on empirical test-
ing.
CUSTOM_CLOSED_QA_PROMPT_TEMPLATE
=
"""TEXT:
{document}
#
REGLER:
1.
Baseret
på
teksten
ovenfor,
lav
5
spørgsmål
med
svar
(question
answer
pairs).
2.
Lav
spørgsmålene
så
"diverse" and relavante til TEXT som
muligt. Fokusér på det mest fundamentale
vinden i TEXT. Spørgsmålene skal være
med et definitivt svar.
Angiv svaret
direkte
uden
beskrivelse.
3.
Du
skal
IKKE
lave
spørgsmål
omkring
kulturkanonen,
forkusér
på
det
mest
fundamentale i teksten.
4.
Husk at
bruge anførselstegnene korrekt. 5. Brug
personers
fulde
navne
og
brug
ikke
forkortelser.
Eksempel:
Grundtvig og
n.f.s
grundtvig
skal
skrives
Nikolaj
Frederik Severin Grundtvig 6.
Svarene
skal være korte og præcise, helst et
enkelt ord eller en kort sætning.
7.
Svarene
må
IKKE
indeholde
kommaer.
8.
Svarene
må
IKKE
indeholde
flere
svarmuligheder.
9.
Svarene
må
IKKE
indeholde beskrivelser eller yderligere
information, kun det direkte svar.
10.
Svarene
må
IKKE
indeholde
referencer
til
andre
personer,
steder
eller
begivenheder
11.
Svarene
må
IKKE
indeholde
ja/nej
svar.
12.
Svarene
må
IKKE
indeholde
delvise
svar
eller
antydninger, kun det fulde og korrekte
svar.
13.
Svarene
må
IKKE
være
indforstået
eller
kræve
yderligere
forklaring.
##
Allowed
structure
examples:
-
"I
hvilket
år
blev
rytterstatuen
af
Frederik
V
rejst
i
Frederiksstaden?","1771"
-
"Hvad
er
navnet
på
den
lille
landsby,
der
ligger nær Glorup, og som har en række
boliger i cottage-stil?","Svindinge"
## NOT ALLOWED structure examples:
-
"Hvem
har
inspireret
Asger
Jorn
til
at lave maleriet Stalingrad?", "Pablo
Picasso,
samt
Asger
Jorns
personlige
overvejelser om historie og politik, og
beskrivelser af Slaget om Stalingrad fra
en af hans venner, Umberto Gambetta."
-
"Hvem
indviede
vejforbindelsen
over
Storebælt i 1998?", "Dronning Margrethe
indviede
vejforbindelsen."
-
"Er
Mariebjerg
Kirkegård
medtaget
i
den
danske kulturkanon?",
"Ja,
Mariebjerg
Kirkegård
er
medtaget
i
den
danske
kulturkanon i kategorien arkitektur."
Output
format
(strictly,
for
parsing
purposes):
Spørgsmål
1:
[Insert
question or task here] Svar 1: [Insert
answer or response here]
Spørgsmål 2:
[Insert question or task
here] Svar 2: [Insert answer or response
here]
Spørgsmål 3:
[Insert question or task
here] Svar 3: [Insert answer or response
here]
Spørgsmål 4:
[Insert question or task
here] Svar 4: [Insert answer or response
here]
Spørgsmål 5:
[Insert question or task
here] Svar 5: [Insert answer or response
9

--- Page 10 ---

here] """
B
Evaluation Prompt Template
We use the generation evaluation template, instruct-
ing the model to answer within a given rule-set. We
do this instead of using a structured output but still
get a form of normalization to base our evaluation
on.
PROMPT_TEMPLATE = """ Besvar spørgsmålet
med
kun
det
direkte
svar,
uden
forklaring om hvorfor. Regelsæt: - Svar
kun på dansk. - Hvis svaret er i højde,
svar i meter (m). - Hvis svaret er i vægt,
svar i kilogram (kg). - Hvis svaret er om
en størrelse, svar i centimeter (cm). Fx
Hvor stort er maleriet Mona Lisa? Svar:
77 cm x 53 cm. - Hvis svaret er en person
angiv den måde de typisk bliver angivet
på i danske tekster.
\n\nSpørgsmål: {question}\nSvar:"""
C
More Examples
We provide more examples in Table 3.
10

--- Page 11 ---

Table 3: Samples questions-answer pairs. Correct answers are marked in bold.
GPT-OSS
Mistral-Small 3.1 Instruct 2503
Llama 3.3
Gemma 3
Question
20B
120B
24B
70B
27B
Hvornår blev
Solvognen
fundet?
1907
1902
1902
1902
1902
Hvem har
komponeret
musikken til
’Gå med i
lunden’?
Børge
Christensen
Traditionel
(ingen kendt
komponist)
Thomas
Koppel
H.C. Lumbye
Ludvig
Holstein-
Ledreborg
Hvem skrev
Ditte Men-
neskebarn?
Jens Peter
Jacobsen
Martin A.
Hansen
Børge
Houmann
Martin
Andersen
Nexø
Martin
Andersen
Nexø
Hvad er navnet
på Gasolin’s
sjette album,
der udkom i
1976?
Gasolin ’6
Gør det noget
Nightmare
Efter endt
uddannelse,
starter
rock’n’roll.
Støvskyggen
Hvem
designede
Pantonstolen?
Hanna Panton
Verner
Panton
Verner
Panton
Verner
Panton
Verner
Panton
Hvad er
Fingerplanen
en plan for?
Fingerplanen
er en plan for
udviklingen
af Finger-
regionen i
Danmark.
en plan
for den
overordnede
by- og trans-
portudvikling
i hovedstad-
sregionen
Fingerplanen
er en plan for
landets are-
aludnyttelse
Fingerplanen
er en plan for
udviklingen
af det
offentlige
transport-
system i
København.
Hovedstadsregionens
udvikling.
Hvornår blev
Vor Frue Kirke
opført?
1862
1829
1182-1220.
Omkring
1100-
1300-tallet
1200-tallet.
I hvilket år
startede
udgivelsen af
Flora Danica?
1791
1761
1761
1761
1605
Hvem skrev
Telegrafgalop?
Svend Gade
Tom
Kristensen
B.S. Ingemann
Hans
Christian
Lumbye
Carl Nielsen
Hvem er
kunstneren bag
skulpturen
’Stående
kvinde’?
Kunstneren er
Søren Møller.
Jens Galschiøt
Astrid Noack
Astrid Noack
Barbara
Hepworth
Hvem er
forfatteren til
digtet
Myggesang?
H.C. Andersen
Halfdan
Rasmussen
Johannes
Ewald
Johannes
Ewald
Holger
Danske.
Hvad er navnet
på det
Shu-bi-dua
album, hvor
sangen
’Danmark’ er
inkluderet?;
78’eren;
Sølv
Shu-bi-Dua 2
Shu-bi-dua 4
Shu-bi-dua 7
Den fede
oplevelse
11

```
