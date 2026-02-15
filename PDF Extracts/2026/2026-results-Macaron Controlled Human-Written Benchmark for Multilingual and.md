---
title: "2026-results-Macaron Controlled Human-Written Benchmark for Multilingual and - PDF Extract"
source_pdf: "2026-results-Macaron Controlled Human-Written Benchmark for Multilingual and.pdf"
pages: 19
extracted_at: "2026-02-15T17:54:30.239512"
---

# PDF Extract: 2026-results-Macaron Controlled Human-Written Benchmark for Multilingual and

**Source PDF:** 2026-results-Macaron Controlled Human-Written Benchmark for Multilingual and.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Macaron: Controlled, Human-Written Benchmark for Multilingual and
Multicultural Reasoning via Template-Filling
Alaa Elsetohy1,∗, Sama Hadhoud1, Haryo Akbarianto Wibowo1, Chenxi Whitehouse2,
Genta Indra Winata3, Fajri Koto1, Alham Fikri Aji1,∗
1MBZUAI
2Meta
3Capital One
{alaa.elsetohy,alham.fikri}@mbzuai.ac.ae
∗Corresponding authors
Abstract
Multilingual benchmarks rarely test reasoning
over culturally grounded premises: translated
datasets keep English-centric scenarios, while
culture-first datasets often lack control over the
reasoning required. We propose Macaron, a
template-first benchmark that factorizes rea-
soning type and cultural aspect across ques-
tion languages. Using 100 language-agnostic
templates that cover 7 reasoning types, 22 cul-
tural aspects, native annotators create scenario-
aligned English and local-language multiple-
choice questions and systematically derived
True/False questions. Macaron contains 11,862
instances spanning 20 countries/cultural con-
texts, 10 scripts, and 20 languages (includ-
ing low-resource ones like Amharic, Yoruba,
Zulu, Kyrgyz, and some Arabic dialects). In
zero-shot evaluation of 21 multilingual LLMs,
reasoning-mode models achieve the strongest
performance and near-parity between English
and local languages, while open-weight mod-
els degrade substantially in local languages and
often approach chance on T/F tasks. Culture-
grounded mathematical and counting templates
are consistently the hardest.
The data can
be accessed here https://huggingface.co/
datasets/AlaaAhmed2444/Macaron.
1
Introduction
With the growing progress of multilingual LLMs,
benchmarking them across languages and cultures
is equally important. Prior work has created sev-
eral benchmarks. In one aspect, translation-parallel
benchmarks enable controlled cross-lingual com-
parison but frequently preserve English-centric sce-
narios and assumptions (Conneau et al., 2018; Ponti
et al., 2020; Artetxe et al., 2019; Lin et al., 2021;
Singh et al., 2025; Xuan et al., 2025). Alterna-
tively, some benchmarks feature examples written
independently for each language or region, pro-
viding locally salient content (Chiu et al., 2025;
Myung et al., 2024; Sadallah et al., 2025; Hasan
et al., 2025; Wibowo et al., 2024), but they often do
not explicitly control which reasoning skills items
require, and independently authored regional sub-
sets can drift in scope and difficulty (Romero et al.,
2024). Moreover, scaling such datasets to many
cultures typically requires creating new questions
from scratch for each language; hence, writing chal-
lenging benchmarks will be time-consuming each
time and might lead some annotators to go for the
simpler questions.
We propose Macaron, a template-first bench-
mark for multilingual multicultural reasoning. We
design 100 language-agnostic templates tagged
with 7 reasoning types and 22 cultural aspects, and
recruit native annotators to instantiate them with
culturally grounded content and produce scenario-
aligned English–local versions. Because templates
are reusable, extending Macaron to new cultural
contexts primarily requires instantiation and trans-
lation of the same template set, keeping structure
and targeted reasoning stable.
From 1,977 bilingual MC scenarios spanning 20
languages and cultural contexts, we derive aligned
True/False variants in both English and the lo-
cal language, yielding 11,862 evaluation instances.
Evaluations across model families show clear capa-
bility and robustness gaps: reasoning-mode models
are strongest (79.3% overall) and nearly language-
robust (Avg. ∆MC = −1.1), while open-weight
models lag (55.2%) and degrade more in local lan-
guages (Avg. ∆MC = −7.5). Some reasoning
types, cultural aspects, and question formats are
consistently harder, especially culture-grounded
mathematical and counting questions.
Our contributions are:
1. A template-first framework that factorizes rea-
soning type and cultural aspect for controlled
multilingual cultural reasoning.
2. Macaron: a scenario-aligned bilingual bench-
mark with MCQ and derived T/F variants
1
arXiv:2602.10732v1  [cs.CL]  11 Feb 2026

--- Page 2 ---

Q: 我大一的时候，歌曲告白气球发行了。
基于这点，我最可能出生于哪一年？
Reasoning: Mathematical, Multi-hop, Temporal
Cultural Aspects: Music and Art, Education
A: 1998
B: 1992
C: 2005
D: 1988 
Q: 如果你出生于1998年，告白气球会在你
大一的时候发行吗？
Q: 如果你出生于1992年，告白气球会在你
大一的时候发行吗？
True
False
China
Reasoning: Multi-hop, Commonsense
Cultural Aspects: Music and Art, Famous People
A: Isigubhu B: Icilongo
C: Isiginci
D: Impempe 
Q: U-Hugh Masekela wayengezwa isigubhu kumemulo
kubo kwelakhe?
Q: U-Hugh Masekela wayengezwa icilongo kumemulo
kubo kwelakhe?
True
False
South Africa (Zulu)
Q: Iyiphi into yokwenza umculo uHugh Masekela
abengayizwa kumemulo kubo kwelakhe?
Reasoning: Spatial, Mathematical, Commonsense
Cultural Aspects: Cities and Landmarks, Education
A: ศาลายาB: พญาไท
C: ปทุมวัน
D: พุทธมณฑลสาย 1 
Q: ถ้าฉันเรียนวิศวกรรมศาสตร์ที่มหาวิทยาลัยมหิดล การเช่า
ที่พักในศาลายาจะช่วยลดระยะเวลาการเดินทางของฉันใช่หรือ
ไม่?
Q: ถ้าฉันเรียนวิศวกรรมศาสตร์ที่มหาวิทยาลัยมหิดล การเช่าที่พัก
ในพญาไทจะช่วยลดระยะเวลาการเดินทางของฉันใช่หรือไม่?
True
False
Thailand (Thai)
Q: ถ้าฉันเรียนวิศวกรรมศาสตร์ที่มหาวิทยาลัย
มหิดล ฉันควรเช่าอพาร์ตเมนต์ในพื้นที่ใดต่อไป
นี้ เพื่อจะได้ไม่ต้องเดินทางไกลเกินไป?
Reasoning: Logical, Multi-hop
Cultural Aspects: Food and Cuisine , Music and Art
A: Πιροσκί
B: Μπατζίνα
D: Λαχανοντολμάδες
αυγολέμονο
C: Κοκορέτσι 
Q: Ακολουθώντας το μοτίβο Τσάμικος →
Κοντοσούβλι, μπορούμε να πούμε ότι
Σέρρα → Πιροσκί;
Q: Ακολουθώντας το μοτίβο Τσάμικος →
Κοντοσούβλι, μπορούμε να πούμε ότι
Σέρρα → Μπατζίνα;
True
False
Greece
Q: Τσάμικος (Ήπειρος) → Κοντοσούβλι Ηπείρου
     Σέρρα (ποντιακός χορός) → ?
Reasoning: Commonsense, Multi-hop, Temporal
Cultural Aspects: Agriculture
A: Naranja
B: Mango
C: Huaya
D: Mamey
Q: En Yucatán, ¿encontrarías naranjas abundantemente
en octubre?
Q: En Yucatán, ¿encontrarías mangos abundantemente
en octubre?
True
False
Mexico
Q: En Yucatán, ¿cuál de los siguiente frutos /
vegetales encontrarías abundantemente en
Octubre?
Morocco
٠١ ذو الحجة، شمن ماكلة اللي إال زرتي للمغرب نهار :س
كتشوفها موجودة كثر من أي نهار آخر؟ 
Cultural Aspects: Food and Cuisine, Events and Festivals
Reasoning: Mathematical, Multi-hop, Temporal
A: بولفافB: حريرة
C: أملوD: دجاج محمر 
٠١ واش الناس فالمغرب غالبا كياكلو بولفاف كثر نهار
ذو الحجة؟
٠١ واش الناس فالمغرب غالبا كياكلو الحريرة كثر نهار
ذو الحجة؟
True
False
Japan
Reasoning: Causal, Multi-hop, Commonsense
Cultural Aspects: Events and Festivals, Social Customs
Q: 次のうち、日本の引っ越し祝いとして
最もふさわしくない贈り物はどれですか？
A: はさみB: ハンドタオル
C: 家具
D: お菓子やおつまみ
Q: はさみは、日本の引っ越し祝いとして最も不適切な
贈り物ですか？
Q: タオルは、日本の引っ越し祝いとして最も不適切な
贈り物ですか？
True
False
Figure 1: Macaron Coverage. Our benchmark spans 20 countries, 20 languages, 10 scripts; each mapped country
(colored in blue) contributes scenario-aligned English and local-language items based on the predesigned set of
templates.
across 20 languages and 20 cultural contexts.
3. An evaluation of 21 multilingual LLMs with
analyses across languages, reasoning cate-
gories, and cultural aspects.
2
Related Work
Reasoning and diagnostic evaluation.
English-
first benchmarks cover commonsense and plausi-
bility reasoning (HellaSwag, WinoGrande, ARC,
CROW) (Zellers et al., 2019; Sakaguchi et al.,
2019; Clark et al., 2018; Ismayilzada et al., 2023)
and exam-style reasoning (BIG-bench, MMLU,
MMLU-Pro) (Srivastava et al., 2023; Hendrycks
et al., 2021; Wang et al., 2024), with harder diag-
nostic subsets such as BBH (Suzgun et al., 2023).
Controlled-structure datasets such as bAbI and
CLUTRR (Weston et al., 2015; Sinha et al., 2019)
motivate template-controlled evaluation. While
these resources provide strong reasoning diagnos-
tics, they are not designed to evaluate reasoning
under culturally grounded premises.
Translation-parallel multilingual evaluation.
A common multilingual strategy is to translate
English-source datasets to many languages, en-
abling controlled cross-lingual comparison but in-
heriting source framing and assumptions. Exam-
ples include XNLI (Conneau et al., 2018), XCOPA
(Ponti et al., 2020), XQuAD (Artetxe et al., 2019),
and X–CSR (Lin et al., 2021). Global-MMLU and
MMLU-ProX expand exam-style evaluation across
languages and scripts while keeping instances par-
allel (Singh et al., 2025; Xuan et al., 2025).
Culture-grounded and regional benchmarks.
Regional-sourcing benchmarks such as INCLUDE
and MILU draw from local exams or region-
specific materials (Romanou et al., 2025; Verma
et al., 2025). Culture-first and native-query re-
sources such as CulturalBench, BLEnD, ArabCul-
ture, and NativQA/MultiNativQA emphasize lo-
cally salient content (Chiu et al., 2025; Myung
et al., 2024; Sadallah et al., 2025; Hasan et al.,
2025). NormAd is complementary for norm and eti-
quette judgments, but it is not a bilingual, scenario-
aligned reasoning test (Rao et al., 2025). Multi-
NRC adds explicit reasoning categories alongside
native-authored questions, but covers fewer lan-
guages and does not systematically cross reasoning
types with cultural domains at scale (Fabbri et al.,
2025).
Table 1 compares our benchmark with previous
work. Our work differs by providing a reasoning-
based benchmark that requires reasoning capabili-
ties in addition to cultural knowledge. Additionally,
we carefully hand-craft templates to ensure stan-
dardized questions and more controlled difficulty.
3
Data Curation
Our goal is to evaluate multilingual, multicultural
reasoning in a controlled setting. We operational-
ize this as (i) multiple-choice question answering
and (ii) binary True/False verification over the same
2

--- Page 3 ---

Benchmark
Modality
#Eval
#Lang
#Scripts
Culture-
EN–Local
Template
Reasoning
Culture meta/
items
grounded
aligned
based
taxonomy
taxonomy
Global-MMLU (Singh et al., 2025)
MCQ
14k/langa
42
13⋄
✗
✓
✗
✗
✓
MMLU-ProX (Xuan et al., 2025)
MCQ (10)
11.8k/langa
29
10⋄
✗
✓
✗
✗
✗
INCLUDE (Romanou et al., 2025)
MCQ
197.2k
44 (52 countries)
15
✓
✗
✗
✗
✗
MILU (Verma et al., 2025)
MCQ
79.6K
11
10⋄
✓
✗
✗
✗
✗
BLEnDK (Myung et al., 2024)
SAQ+MCQ
52.6k
13
7⋄
✓
✓
✗
✗
✓
CulturalBenchK (Chiu et al., 2025)
MCQ+T/F∥
6.7k
1 (45 regions)
1
✓
✗
✗
✗
✓
ArabCultureK (Sadallah et al., 2025)
MCQ (3)
3.5K
1 (13 countries)
1
✓
✗
✗
✗
✓
NativQAK (Hasan et al., 2025)
QA
64K
7
4⋄
✓
✗
✗
✗
✓
MultiNRC (Fabbri et al., 2025)
SAQ
1k
3
2⋄
✓
✓
✗
✓g
✗
WorldCuisines (Winata et al., 2025)
MCQ, QA
1M
30
14
✓
✓
✓
✗
✗
Ours
MCQ+T/F∥
~12k
20
10
✓
✓
✓
✓
✓
Table 1: Benchmark comparison with coverage statistics and design axes. Modality denotes the evaluation
format (MCQ, SAQ, QA, and/or T/F); T/F∥indicates binary instances systematically derived from MCQ options
(scenario-aligned). #Eval items reports test size when available; translation-parallel benchmarks report per-language
test size (a). #Scripts counts distinct writing scripts; ⋄computed from the language list using dominant scripts.
K marks benchmarks primarily framed as cultural knowledge or information-seeking QA rather than explicitly
reasoning-targeted evaluation. gMultiNRC defines four reasoning categories.
culturally grounded scenarios as shown in Figure
2. The benchmark is designed to help disentangle
three factors that are often confounded in multilin-
gual evaluation: language (English vs. local input),
cultural grounding, and reasoning (the inference
required to answer).
3.1
Task Definition
Let L denote the set of local languages in the bench-
mark and Cctx the set of cultural contexts (countries
or regions). We construct base annotations as bilin-
gual, culturally aligned multiple-choice items. A
base annotation is a tuple
a =
 qen, Aen, qℓ, Aℓ, Ra, Ca

,
where qen and qℓare the English and local-language
question texts, Aen and Aℓare the corresponding
sets of four answer options with exactly one correct
choice, and ℓ∈L is the local language. We treat
both reasoning and culture as explicit (potentially
multi-label) metadata: Ra ⊆R is the set of reason-
ing types targeted by the item, and Ca ⊆Caspect is
the set of cultural aspects it probes.
From each base annotation, we derive four addi-
tional binary instances (True/False in English and
in local language; Section 3.5), yielding six aligned
evaluation instances per cultural scenario.
3.2
Reasoning and Cultural Taxonomies
Reasoning types.
We define a taxonomy of seven
reasoning types that commonly arise in culturally
grounded questions: mathematical (numerical com-
putation and comparison), commonsense (everyday
plausibility and typical situations), causal (cause–
effect relations), temporal (time, order, calendars),
logical (deduction, implication, and analogy), spa-
tial (geographic and spatial relations), and multi-
hop (composition of two or more inference steps,
e.g., symbol →religion →practice). Templates
may be tagged with multiple reasoning types when
solving requires more than one skill.
Cultural aspects.
We complement the reason-
ing taxonomy with 22 cultural aspects that cap-
ture the domains of everyday life represented by
our templates: Agriculture, Brands and Commerce,
Cities and Landmarks, Death and Funerals, Edu-
cation, Events and Festivals, Famous People, Fash-
ion and Media, Folklore and Folktales, Food and
Cuisine, Language and Communication, Litera-
ture and Written works, Music and Art, Naming,
Objects and Units, Politics and Governance, Re-
lationships, Social Customs, Sports, Time, Trans-
portation, and socio-religious aspects of life. Each
template is associated with at least one aspect, and
some span multiple aspects. We provide an exam-
ple for each aspect in Appendix Table 6.
3.3
Template Framework
To systematically cover the reasoning×culture
space, we design a set of 100 language-agnostic
templates. Each template specifies:
• a question skeleton with typed slots (e.g.,
[COUNTRY], [PERSON], [FOOD1]), including
constraints on valid slot values;
• metadata tags indicating the targeted reason-
ing type(s) and cultural aspect(s);
3

--- Page 4 ---

1) Templates
Design
2) Templates
Instantiation and
Questions
Translation by
Annotators
4) True / False
Generation and
Translation
5) LLM-Correction
Pass
[The neighborhood or residential area that's closer to                                         ]
[A neighborhood or residential area that's further to                                         ]
OPTION A:
OPTION B,C,D:
Reasoning: Spatial, Mathematical, Commonsense
Cultural Aspects: Cities and Landmarks, Education
If I study Music at East China Normal University, which of the following
areas should I rent an apartment in so that I don’t have to commute too far?
Q:
A: Jiangchuan Road Subdistrict
B: Xujiahui
C: Lujiazui
D: Chongming Island
如果我在华东师范大学学习音乐，为了避免太远的通勤，我应该在以下哪一
个区域租房？
Q:
A: 江川路街道
B: 徐家汇
C: 陆家嘴
D: 崇明岛
If I study                at                           , would renting in                  keep my commute short?
[SUBJECT]
[UNIVERSITY NAME]
[OPTION A]
If I study                at                           , would renting in                  keep my commute
short?
[SUBJECT]
[UNIVERSITY NAME]
[OPTION B]
If I study Music at East China Normal University, would renting
in Xujiahui keep my commute short?
If I study Music at East China Normal University, would renting
in Jiangchuan Road Subdistrict keep my commute short?
True Q:
False Q:
True Q:
False Q:
True Q:
False Q:
如果我在华东师范大学学习音乐，租房租在江川路街道，通勤距
离会近吗？
如果我在华东师范大学学习音乐，租房租在徐家汇，通勤距离会
近吗？
If I study                at                            , which of the following areas should I rent an apartment in so that I don’t have to commute too
far?
[SUBJECT]
[UNIVERSITY NAME]
openai/gpt-5.2-chat
English
Questions
Correct minor
grammar mistakes
and spelling if
there are any
Does this list contain exactly              that        Ye Tsom: Tire Siga, Shiro, Beyaynet, Kikil?
Does this list contain exactly             that      Ye Tsom: Tire Siga, Shiro, Beyaynet, Kikil?
Does Talas meet both criteria: being adjacent to Naryn and         the Burana Tower?
Does Talas meet both criteria: being adjacent to Naryn and             the Burana Tower?
 1 foods 
are
 1 food 
is
has
having
[UNIVERSITY NAME]
[UNIVERSITY NAME]
3) True / False
Templates Design
Figure 2: Macaron Curation Pipeline. We first design language-agnostic templates tagged with reasoning categories
and cultural aspects. Native annotators instantiate each template with culturally grounded content to produce
scenario-aligned English MCQs and translate them into local languages. From each MCQ, we derive aligned
True/False statements by instantiating the template’s binary child forms with the correct option (True) and a distractor
(False), and translate these statements into the local language. Finally, we run an LLM proofreading pass to correct
minor spelling/grammar issues while preserving the original meaning and leaving all local-language text unchanged.
• an expected output format (four-option multi-
ple choice with exactly one correct answer).
Templates are authored and iteratively refined
by the dataset creators. During refinement, we
remove culturally insensitive or non-portable de-
signs, tighten slot constraints to prevent ambiguity,
and ensure that the intended reasoning path is sta-
ble across cultural contexts. Each template also
includes a True/False variant (Section 3.5).
3.4
Bilingual Annotation Pipeline
Annotators and onboarding
For each cultural
context, we recruit two annotators via the Upwork
freelancing platform. Annotators are native speak-
ers of the target local language and have substantial
lived experience in the target context (e.g., having
grown up and/or currently residing there). During
onboarding, annotators receive some guidelines
and complete a small pilot set of templates with
feedback from the dataset creators.
The guidelines emphasize:
1. Cultural representativeness within tem-
plates.
Instantiate each assigned template
with content that is locally appropriate and
commonly recognizable to members of the
target culture, aiming for diversity across ev-
eryday institutions and practices.
2. Avoiding both stereotypes and obscure
trivia.
Prefer culturally salient, everyday
knowledge rather than tourist facts or internet
stereotypes, while avoiding niche or hard-to-
verify trivia that most locals would not know.
3. Plausible within-context distractors. Write
distractors that are plausible within the same
cultural sphere so items cannot be solved by
eliminating obviously foreign options; ensure
exactly one correct answer.
4. Non-applicability and ambiguity flags. Flag
and skip templates that do not meaningfully
apply to your cultural context.
Step 1: English multiple-choice instantiation
Annotators are assigned a subset of templates. For
each template, they:
1. fill required slots with culturally appropriate
content based on lived experience and com-
monly shared local knowledge;
2. provide one correct option and three plausi-
4

--- Page 5 ---

ble distractors, ensuring exactly one option is
correct for the target context.
Step 2: local-language translation
After com-
pleting the English version, the same annotator
translates the question and its options into their na-
tive language. For each base item, they produce
local-language text qℓand Aℓunder the constraints
that the translation must:
• preserve the underlying cultural content (same
dish, institution, practice, person, etc.);
• preserve the reasoning structure and difficulty;
• allow only light adaptations for naturalness
when needed, as long as the English and local
versions still align.
Each
item
inherits
the
reasoning
and
cultural-aspect tags from the template meta-
data,
yielding
a
bilingual
base
annotation
a =
 qen, Aen, qℓ, Aℓ, Ra, Ca

.
3.5
True/False Variant Generation
Starting from each base annotation, we construct
four additional binary instances: True and False in
English and in the local language. Concretely, for
each base item we instantiate the template’s binary
child forms: a True variant by inserting the correct
option, yielding a statement whose correct label
is True; and a False variant by inserting a care-
fully chosen distractor option, yielding a statement
whose correct label is False.
We generate these binary instances in both En-
glish and the local language, maintaining scenario-
level alignment. The True and False variants share
the same cultural scenario and reasoning require-
ments as the parent multiple-choice item. Thus,
each base annotation yields six aligned instances:
MC–EN, MC–L, T–EN, T–L, F–EN, and F–L.
3.6
Quality Control
To ensure cultural correctness, linguistic clarity,
and consistency across annotators and cultural con-
texts, we apply a combination of human review and
automated quality-control procedures.
Manual cultural review.
For each cultural con-
text, a reviewer from that culture manually samples
and reviews the annotated items for cultural cor-
rectness and local-language clarity. Items flagged
as confusing, ambiguous, or culturally inaccurate
are revised and, when necessary, removed.
Automated validation and English proofread-
ing.
Because questions are produced by instan-
Country
Language
Script
#Q
Egypt
Egyptian Arabic
Arabic
594
Philippines
Tagalog
Latin
594
India
Hindi
Devanagari
600
Ethiopia
Amharic
Ge’ez
588
Mexico
Mexican Spanish
Latin
594
Tunisia
Tunisian Arabic
Arabic
600
Greece
Greek
Greek
600
Brazil
Portuguese
Latin
600
Kyrgyzstan
Kyrgyz
Cyrillic
600
South Africa
Zulu
Latin
600
Italy
Italian
Latin
588
Thailand
Thai
Thai
594
Turkey
Turkish
Latin
600
Georgia
Georgian
Mkhedruli
594
China
Chinese
Han (Hans)
582
Indonesia
Indonesian
Latin
570
Yemen
Yemeni Arabic
Arabic
600
Nigeria
Yoruba
Latin
570
Morocco
Moroccan Arabic
Arabic
600
Japan
Japanese
Japanese
594
Total
11,862
Table 2: Dataset statistics and language coverage. Small
deviations across contexts reflect items removed during
quality control.
tiating shared templates with culture-specific con-
tent, small surface-level inconsistencies can arise
in the English text across annotators and contexts
(e.g., tense mismatches introduced by adapting a
template from a generic present-tense form to a
past event). To mitigate this template-instantiation
noise without altering cultural content or reason-
ing difficulty, we run a deterministic LLM-assisted
proofreading pass on English fields only (multiple-
choice questions and options, and the English True/-
False statements). For each English field, we query
openai/gpt-5.2-chat to correct only spelling
and grammatical errors (including agreement, tense
consistency, and capitalization), while preserving
the original writing style and word choices and
keeping all cultural references and proper nouns
unchanged; rephrasing or stylistic improvement is
explicitly disallowed. All local-language text is left
exactly as written by annotators.
3.7
Dataset Statistics
After quality control and expansion, the benchmark
contains 11,862 total evaluation instances. Table 2
summarizes the distribution by cultural context
(country), along with the associated local language
and script. Appendix A provides additional break-
downs of template coverage across cultural aspects
(Figure 6) and reasoning categories (Figure 7).
4
Experimental Setup
We evaluate a total of 21 multilingual LLMs in
both multiple-choice (MC) and binary (True/False)
5

--- Page 6 ---

Category
Model
MC-EN
MC-L
∆MC
TF-EN
TF-L
∆TF
Overall
Closed (thinking)
google-gemini-3-flash-preview-thinking
89.5%
89.1%
-0.4%
84.5%
82.7%
-1.8%
86.5%
google-gemini-2.5-pro-thinking
87.5%
88.3%
+0.8%
81.6%
81.2%
-0.4%
84.7%
deepseek-deepseek-chat-v3.1-thinking
76.2%
75.6%
-0.6%
76.7%
71.7%
-5.0%
75.1%
google-gemini-2.5-flash-thinking
70.1%
65.9%
-4.2%
74.6%
74.1%
-0.5%
71.2%
Average (Closed (thinking))
80.8%
79.7%
-1.1%
79.3%
77.4%
-1.9%
79.3%
Closed (standard)
google-gemini-3-flash-preview
86.8%
87.0%
+0.2%
81.9%
79.7%
-2.2%
83.9%
anthropic-claude-opus-4.5
81.3%
80.2%
-1.1%
76.9%
75.2%
-1.7%
78.4%
openai-gpt-5-chat
79.0%
78.2%
-0.8%
77.1%
73.5%
-3.6%
77.0%
google-gemini-2.5-flash
80.2%
80.2%
+0.0%
71.9%
70.5%
-1.4%
75.7%
deepseek-deepseek-chat-v3.1
74.0%
68.4%
-5.6%
67.9%
64.1%
-3.8%
68.6%
anthropic-claude-haiku-4.5
70.5%
63.8%
-6.7%
68.5%
64.8%
-3.7%
66.9%
openai-gpt-4o-mini
70.6%
65.3%
-5.3%
67.0%
64.2%
-2.8%
66.8%
Average (Closed (standard))
77.5%
74.7%
-2.8%
73.0%
70.3%
-2.7%
73.9%
Open-weight
qwen-qwen3-235b-a22b-2507
73.3%
68.3%
-5.0%
67.3%
65.9%
-1.4%
68.7%
meta-llama-llama-3.3-70b-instruct
70.2%
62.6%
-7.6%
67.5%
62.0%
-5.5%
65.6%
meta-llama-llama-4-maverick
68.7%
67.5%
-1.2%
64.1%
62.1%
-2.0%
65.6%
meta-llama-llama-3.1-8b-instruct
54.2%
43.4%
-10.8%
56.7%
53.4%
-3.3%
51.9%
qwen-qwen3-4b-instruct-2507
52.6%
45.6%
-7.0%
55.2%
53.7%
-1.5%
51.8%
internlm-internlm3-8b-instruct
54.8%
40.9%
-13.9%
55.8%
52.2%
-3.6%
50.9%
qwen-qwen2.5-7b-instruct
57.0%
46.9%
-10.1%
52.6%
52.6%
+0.0%
52.3%
coherelabs-aya-expanse-8b
52.7%
48.7%
-4.0%
51.7%
52.5%
+0.8%
51.4%
meta-llama-llama-3.2-3b-instruct
47.4%
36.3%
-11.1%
54.9%
51.6%
-3.3%
47.6%
coherelabs-aya-23-8b
43.8%
39.2%
-4.6%
50.4%
50.5%
+0.1%
46.0%
Average (Open-weight)
57.5%
49.9%
-7.5%
57.6%
55.6%
-2.0%
55.2%
Average (All)
68.6%
63.9%
-4.7%
66.9%
64.7%
-2.2%
66.0%
Table 3: Overall model comparison on our benchmark (accuracy, %). Deltas are computed as (Local −English).
formats, using paired English and local-language
versions of each culturally grounded scenario to
isolate the effects of language, cultural grounding,
and reasoning type.
All models are tested in a zero-shot setting.
For open-weight models and API models that ex-
pose token-level log-probabilities, we compute the
log-likelihood of each candidate answer (A–D for
multiple-choice, T/F for True/False) and select the
highest-probability option. For API models that
do not provide log-probabilities, including “think-
ing” models that produce explicit chain-of-thought,
models are allowed to reason freely but are in-
structed to output their final answer in a structured
format (a JSON object {"answer": "A"} on the
last line). We extract the answer field and compute
accuracy with respect to the gold label.
Models.
The evaluated models span both closed-
source models and open-weight instruction-tuned
LLMs. Specifically, we include Google Gemini
3
Flash
Preview (standard and “thinking”)1;
Google Gemini 2.5 Pro (thinking) and Gemini
2.5
Flash (standard and thinking) (Comanici
et al., 2025); DeepSeek-Chat
v3.1 (standard
and “thinking”) (DeepSeek-AI et al., 2025); An-
thropic Claude models (Opus 4.5 and Haiku
1https://blog.google/products-and-platforms/
products/gemini/gemini-3-flash/
4.5)2; OpenAI GPT-5 Chat3 and GPT-4o-mini
(OpenAI et al., 2024); as well as open-weight
models including Qwen3 (235B-A22B and 4B)
(Yang et al., 2025), Qwen2.5-7B (Qwen et al.,
2025), Meta Llama 4 Maverick4 and Llama 3.x
(3.3-70B, 3.1-8B, 3.2-3B) (Grattafiori et al.,
2024), InternLM3-8B5, and Cohere Aya models
(Aya-23-8B and Aya-Expanse-8B) (Aryabumi
et al., 2024; Dang et al., 2024).
5
Results and Discussion
Table 3 reports overall performance on scenario-
aligned English and local-language instances in
both multiple-choice (MC) and True/False formats,
grouped by model category. We additionally report
cross-lingual gaps ∆MC and ∆TF, computed as
(Local −English), where negative values indicate
degraded performance in the local language.
Open-weight models show larger English–local
gaps and reduced reliability on True/False.
Closed-source thinking models achieve the high-
est overall accuracy (79.3% on average), outper-
forming closed (standard) models (73.9%) and
open-weight models (55.2%). The English–local
gap widens as model capacity decreases: think-
2https://platform.claude.com/docs/en/
about-claude/models/whats-new-claude-4-5
3https://cdn.openai.com/gpt-5-system-card.pdf
4https://www.llama.com/models/llama-4/
5https://internlm.readthedocs.io/en/latest/
model_card/InternLM3.html
6

--- Page 7 ---

Top-5 Easiest Templates (avg. over models)
Top-5 Hardest Templates (avg. over models)
Acc
Template prompt
Acc
Template prompt
92.51%
If my friend has the last name [LAST NAME], which
country is most likely their birthplace?
35.76%
Among all the provinces in [SET OF PROVINCES/LOCATION],
how
many
provinces
have
an
area
smaller
than
[PROVINCE]?
85.66%
Which
of
the
following
authors
is
traditionally
associated with [CULTURE/REGION]’s literature?
37.52%
[GIFT 1], [GIFT 2], [GIFT 3], and [GIFT 4]. How many
of these are suitable gifts to give when attending a
[NATIONALITY] friend’s wedding?
85.44%
If I am visiting [PLACE] in [MONTH], what kind of
clothes should I pack?
38.31%
[MATERIAL 1], [MATERIAL 2], [MATERIAL 3], [MATERIAL 4].
How many of these are not typically used when making
[TRADITIONAL ITEM]?
84.98%
In [NATIONALITY OR CULTURE] attire, what determines
the [GARMENT FEATURE]?
39.61%
Among all [POLITICAL POSITION] in [COUNTRY] up until
[YEAR], how many of them are [CONDITION]?
84.36%
Which of these political systems was/is traditionally
practiced in [REGION] during the [TIME PERIOD]?
42.30%
[FOOD 1], [FOOD 2], [FOOD 3], [FOOD 4], how many of
these are [SOME CLASSIFICATION]?
Table 4: Template difficulty extremes: easiest prompts are simple cultural associations, while hardest prompts are
constraint-heavy exact-count questions.
China
India
Italy
Japan
Brazil
Mexico
Turkey
Indonesia
Greece
Philippines
Thailand
Yemen
Morocco
Georgia
Egypt
Kyrgyzstan
Tunisia
Nigeria
South Africa
Ethiopia
0
20
40
60
80
Accuracy
Local
English
Figure 3: Average performance in English vs. local
language across cultural contexts.
Causal Reasoning
Commonsense Reasoning
Logical Reasoning
Mathematical Reasoning
Multi-hop Reasoning
Spatial Reasoning
Temporal Reasoning
Reasoning Category
Gemini 3 Flash Preview (Thinking)
Gemini 2.5 Pro (Thinking)
Gemini 3 Flash Preview
Claude Opus 4.5
Gemini 2.5 Flash
GPT-5 Chat
DeepSeek Chat v3.1 (Thinking)
DeepSeek Chat v3.1
Qwen3-235B-A22B-2507
Llama 4 Maverick
GPT-4o Mini
Claude Haiku 4.5
Gemini 2.5 Flash (Thinking)
Llama 3.3 70B Instruct
Qwen2.5-7B-Instruct
Aya Expanse 8B
Qwen3-4B-Instruct-2507
Llama 3.1 8B Instruct
InternLM3-8B-Instruct
Llama 3.2 3B Instruct
Aya 23 8B
Model
91.3%
90.3%
88.3%
84.7%
89.4%
90.3%
88.5%
89.9%
88.7%
88.0%
82.9%
87.9%
87.1%
86.5%
90.5%
88.8%
87.2%
80.8%
86.4%
87.6%
85.2%
85.1%
83.0%
80.4%
75.2%
80.5%
82.2%
79.4%
84.0%
82.9%
79.2%
72.6%
80.1%
81.8%
80.2%
86.3%
83.1%
77.6%
68.6%
78.7%
81.4%
75.2%
75.4%
75.7%
71.8%
75.6%
76.9%
78.7%
77.4%
78.5%
74.7%
70.4%
64.2%
71.1%
70.1%
71.4%
82.1%
73.9%
69.9%
62.1%
70.3%
71.7%
69.3%
78.1%
71.2%
67.9%
59.3%
67.1%
68.1%
67.3%
74.9%
71.5%
66.2%
56.7%
68.6%
72.2%
66.1%
77.0%
70.8%
65.4%
58.5%
67.1%
69.3%
65.3%
76.3%
74.8%
75.9%
56.3%
64.9%
64.5%
58.3%
74.6%
68.9%
65.7%
57.5%
66.4%
70.8%
64.9%
60.1%
55.0%
52.5%
41.8%
52.0%
50.9%
51.7%
58.9%
52.7%
50.9%
42.9%
51.1%
50.5%
49.2%
56.1%
51.3%
49.2%
41.8%
49.9%
49.5%
47.5%
53.1%
50.8%
49.6%
42.4%
49.0%
52.5%
47.5%
54.2%
49.7%
46.2%
42.6%
48.4%
46.2%
49.8%
47.2%
42.7%
42.3%
38.9%
41.7%
43.7%
40.6%
49.7%
44.6%
40.3%
36.2%
41.7%
45.2%
39.3%
0
20
40
60
80
100
Accuracy %
Figure 4: Accuracy by reasoning type across models.
ing models are near-parity (Avg. ∆MC = −1.1),
whereas open-weight models exhibit much larger
drops (Avg. ∆MC = −7.5), particularly at 3B–
8B scale. While most models are above random
baseline in MC, many open-weight models cluster
around ∼50–55% on True/False, close to the 50%
random baseline, indicating limited reliability in bi-
nary verification of culturally grounded statements.
Paired True/False accuracy exposes scenario-
level verification.
Each MC scenario yields a
True/False question pair (True uses the correct op-
Category
T/F (avg. EN/L)
Paired T/F
Drop (pp)
Closed (thinking)
78.4%
62.1%
16.3
Closed (standard)
71.7%
48.4%
23.3
Open-weight
56.6%
18.2%
38.4
Average (All)
65.8%
36.6%
29.2
Table 5: True/False accuracy (averaged over English and
local vs. paired True/False accuracy by model category.
Drop is the difference in percentage points.
tion; False uses a distractor; Section 3.5). In the
paired true/false accuracy calculation, we count a
scenario correct only if the model answers both
questions correctly, to test whether models gen-
uinely verify the underlying cultural fact rather than
succeeding by chance. As shown in Table 5, paired
accuracy is substantially lower than per-question
T/F accuracy across all model categories. This
gap suggests that performance on single T/F items
can be inflated by shallow response tendencies, not
actual cultural knowledge.
English outperforms local except for China,
while the largest gaps concentrate in lower-
resource languages. Figure 3 shows China as
nearly the only case where local slightly exceeds
English, plausibly influenced by the strong pres-
ence of Chinese-focused models (e.g., multiple
Qwen variants) in our evaluation.
In contrast,
the English–local gap is substantially larger for
Amharic, Yoruba, Zulu, and Arabic dialects, high-
lighting that cross-lingual brittleness concentrates
in lower-coverage languages and dialects. Math-
ematical reasoning is hardest in cultural con-
texts; causal and temporal reasoning are easier.
In Figure 4, Mathematical Reasoning is the lowest-
accuracy category for 20/21 models, while Causal
(often alongside Commonsense) is typically high-
est. We attribute this to a double burden: culture-
7

--- Page 8 ---

Objects and Units
Music and Art
Folklore and Folktales
Death and Funerals
Agriculture
Time
Food and Cuisine
Famous People
Events and Festivals
Transportation
Education
Social Customs
Brands and Commerce
Politics and Governance
Cities and Landmarks
Fashion and Media
socio-religious aspects of life
Sports
Literature and Written works
Relationships
Language and Communication
Naming
Cultural Aspect
Gemini-3-Flash
Claude-Opus-4.5
Gemini-2.5-Flash
GPT-5 Chat
DeepSeek-v3.1
Qwen3-235B
GPT-4o Mini
Llama-4-Maverick
Claude-Haiku-4.5
Llama-3.3-70B
Qwen/Qwen2.5-7B-Instruct
Coherelabs/Aya-expanse-8b
Qwen/Qwen3-4B-Instruct-2507
Meta-llama/Llama-3.1-8B-Instruct
InternLM3-8B
Coherelabs/Aya-23-8B
Meta-llama/Llama-3.2-3B-Instruct
Model
78% 81% 89% 82% 90% 91% 88% 89% 86% 81% 92% 84% 92% 83% 91% 87% 91% 90% 92% 98% 97% 100%
76% 74% 82% 81% 76% 86% 80% 84% 80% 74% 79% 77% 85% 78% 84% 81% 89% 88% 81% 93% 88% 100%
69% 71% 85% 77% 84% 84% 81% 81% 79% 76% 81% 69% 86% 82% 84% 81% 84% 83% 86% 95% 96% 97%
63% 68% 78% 74% 84% 75% 82% 79% 77% 81% 80% 82% 88% 75% 83% 82% 82% 81% 87% 90% 94% 98%
63% 63% 70% 71% 69% 76% 67% 72% 72% 76% 74% 75% 76% 74% 73% 72% 77% 85% 84% 80% 81% 98%
63% 60% 65% 64% 69% 72% 68% 72% 71% 70% 66% 73% 69% 74% 73% 74% 79% 75% 80% 88% 90% 100%
51% 58% 61% 59% 75% 59% 69% 66% 68% 68% 72% 68% 69% 66% 72% 74% 78% 79% 84% 82% 88% 95%
54% 57% 53% 65% 62% 61% 64% 69% 67% 58% 70% 71% 73% 71% 73% 73% 84% 78% 78% 92% 88% 95%
59% 51% 66% 70% 67% 63% 63% 64% 68% 66% 67% 69% 69% 75% 68% 69% 80% 69% 80% 77% 94% 93%
49% 58% 65% 62% 56% 67% 62% 66% 64% 68% 68% 63% 72% 71% 71% 71% 78% 72% 81% 82% 83% 95%
40% 43% 50% 47% 54% 45% 48% 47% 53% 58% 54% 63% 54% 58% 54% 56% 57% 60% 66% 55% 75% 90%
41% 40% 45% 40% 38% 45% 44% 48% 50% 50% 54% 56% 52% 60% 53% 58% 57% 65% 68% 48% 79% 90%
40% 41% 50% 44% 34% 41% 42% 48% 51% 50% 50% 56% 49% 52% 47% 56% 52% 58% 61% 60% 83% 88%
42% 42% 38% 42% 39% 29% 44% 50% 44% 50% 60% 53% 44% 54% 52% 56% 57% 64% 58% 62% 50% 85%
38% 42% 41% 42% 46% 44% 43% 45% 48% 54% 52% 55% 51% 51% 48% 52% 51% 48% 52% 58% 68% 82%
38% 32% 30% 49% 34% 40% 37% 35% 43% 52% 41% 48% 43% 43% 43% 45% 44% 45% 52% 42% 60% 88%
36% 37% 30% 37% 34% 38% 36% 39% 39% 38% 42% 44% 40% 46% 46% 48% 43% 54% 49% 48% 56% 78%
0
20
40
60
80
100
Accuracy %
Figure 5: Accuracy (%) by cultural aspect across models. Each cell aggregates over evaluation instances whose
templates are tagged with the corresponding aspect (multi-label; a single instance may contribute to multiple
aspects). Aspects are ordered by mean accuracy (hard →easy).
grounded math questions require both retrieving
long-tail, locale-specific numeric facts and perform-
ing exact composition (e.g., counting or aggrega-
tion), so either retrieval or calculation errors can
flip the answer. Moreover, such numeric facts are
often sparse in training data and region-specific,
raising the risk of confident but incorrect answers.
In contrast, causal and commonsense questions are
often supported by broadly shared everyday knowl-
edge that is better covered in pretraining corpora.
Cultural aspect difficulty is consistent across
models. Figure 5 reports a model×aspect heatmap
and reveals a stable hard →easy ordering across
model families. Averaged over models, Naming is
the easiest aspect (92.5%), followed by Language
and Communication (80.6%), whereas Objects and
Units (52.9%) and Music and Art (54.0%) are the
hardest, yielding a ∼40-point spread. Most remain-
ing aspects form a broad middle band (roughly
64–70% mean accuracy). Beyond mean difficulty,
the heatmap highlights where robustness gaps are
largest: Time varies from 91% (strongest model)
down to 29% (smaller open-weight models), with
similarly large spreads for Folklore and Folktales
(89% →30%), Agriculture (90% →34%), and
Relationships (98% →42%). In contrast, Naming
remains high across all models (78–100%), sug-
gesting it is less discriminative of model capability
than domains involving long-tail artifacts and cul-
turally specific narratives.
“How many” templates are the main failure
mode. Table 4 shows that the easiest templates
are mostly single-step cultural associations (e.g.,
last name →likely birthplace at 92.51%), while
the hardest are uniformly “How many. . . ” prompts
that require enumerating a culturally grounded set,
applying a constraint (often with negation/com-
parison), and producing an exact count (down to
35.76%). This pattern is consistent with our earlier
finding that mathematical reasoning remains the
weakest capability in culturally situated scenarios.
6
Conclusion
We introduce a template-first benchmark for mul-
tilingual, multicultural reasoning across 20 cul-
tural contexts, languages, and 10 scripts (11,862
total instances). Our dataset separates language,
cultural grounding, and reasoning type using
scenario-aligned multiple-choice and True/False
items. Zero-shot evaluations show that closed rea-
soning models achieve near-parity between English
and local inputs, while open-weight models lag
with significant performance drops. This bench-
mark supports diagnostic evaluation to motivate
more culturally robust model development.
8

--- Page 9 ---

Limitations
Despite its breadth, the benchmark has several lim-
itations. First, coverage is necessarily coarse: we
include 20 cultural contexts with one primary lo-
cal language each, which cannot capture within-
country cultural diversity, minority languages, or
finer-grained dialect continua. As a result, perfor-
mance within a single country or language should
not be interpreted as representative of all local va-
rieties or communities. Second, the task format
is intentionally controlled: while multiple-choice
and binary verification enable precise alignment
and diagnostic evaluation, they do not reflect open-
ended dialogue, interactive reasoning, tool use, or
real-world information access. Consequently, the
benchmark measures culturally grounded reason-
ing under constrained conditions rather than end-to-
end performance in realistic deployment settings.
Ethical Considerations
Macaron is a human-written benchmark designed
to evaluate multilingual reasoning over culturally
grounded premises in a controlled, template-first
setting.
Annotator compensation.
We recruited two an-
notators per cultural context via Upwork and com-
pensated them at a fixed rate of US$9 per 10 com-
pleted template instantiations, where a completion
consists of writing the English multiple-choice item
and translating the question, options, and T/F vari-
ants into the local language.
Cultural sensitivity and representational harms.
Because items are cultural-based, there is a risk
of stereotyping, oversimplifying a country/region
into a single culture, or encoding contested prac-
tices as universal. We mitigate this through (i)
iterative template refinement to remove cultur-
ally insensitive/non-portable designs and reduce
ambiguity, (ii) annotator guidelines that empha-
size culturally representative everyday knowledge
while avoiding stereotypes and obscure trivia, and
(iii) plausible within-context distractors to reduce
“foreign-option elimination.” Annotators may also
flag templates as non-applicable when they do not
meaningfully transfer.
Coverage is coarse (one primary local language
per cultural context), so results should not be in-
terpreted as measuring within-country diversity or
dialect variation. As with any benchmark, Macaron
can be misused for overfitting or for simplistic
“ranking” of languages/cultures; we recommend
using it as a diagnostic tool and reporting results
with the above coverage and format constraints in
mind.
LLM assistance in writing.
We used an LLM as
a writing aid (e.g., to improve clarity and correct mi-
nor grammar issues) while drafting this manuscript.
All technical content, experimental design, analy-
ses, and conclusions were produced and verified
by the authors, who take full responsibility for the
final paper. We did not provide any sensitive or
personally identifying information to the model.
References
Mikel Artetxe, Sebastian Ruder, and Dani Yogatama.
2019. On the cross-lingual transferability of mono-
lingual representations. In Proceedings of the 57th
Annual Meeting of the Association for Computational
Linguistics. Association for Computational Linguis-
tics. Introduces the XQuAD dataset.
Viraat Aryabumi, John Dang, Dwarak Talupuru,
Saurabh Dash, David Cairuz, Hangyu Lin, Bharat
Venkitesh, Madeline Smith, Jon Ander Campos,
Yi Chern Tan, Kelly Marchisio, Max Bartolo, Se-
bastian Ruder, Acyr Locatelli, Julia Kreutzer, Nick
Frosst, Aidan Gomez, Phil Blunsom, Marzieh Fadaee,
and 2 others. 2024.
Aya 23: Open weight re-
leases to further multilingual progress.
Preprint,
arXiv:2405.15032.
Yu Ying Chiu,
Liwei Jiang,
Bill Yuchen Lin,
Chan Young Park, Shuyue Stella Li, and 1 others.
2025. Culturalbench: A robust, diverse and challeng-
ing benchmark for measuring lms’ cultural knowl-
edge through human–ai red-teaming. In Proceedings
of the 63rd Annual Meeting of the Association for
Computational Linguistics, Vienna, Austria. Associa-
tion for Computational Linguistics.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018.
Think you have solved question
answering?
try arc, the ai2 reasoning challenge.
Preprint, arXiv:1803.05457.
Gheorghe Comanici, Eric Bieber, Mike Schaekermann,
Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Mar-
cel Blistein, Ori Ram, Dan Zhang, Evan Rosen, Luke
Marris, Sam Petulla, Colin Gaffney, Asaf Aharoni,
Nathan Lintz, Tiago Cardal Pais, Henrik Jacobs-
son, Idan Szpektor, Nan-Jiang Jiang, and 3416 oth-
ers. 2025. Gemini 2.5: Pushing the frontier with
advanced reasoning, multimodality, long context,
and next generation agentic capabilities. Preprint,
arXiv:2507.06261.
Alexis Conneau, Guillaume Lample, Marc’Aurelio Ran-
zato, Ludovic Denoyer, and Hervé Jégou. 2018. Xnli:
Evaluating cross-lingual sentence representations. In
9

--- Page 10 ---

Proceedings of the 2018 Conference on Empirical
Methods in Natural Language Processing, Brussels,
Belgium. Association for Computational Linguistics.
John Dang, Shivalika Singh, Daniel D’souza, Arash
Ahmadian, Alejandro Salamanca, Madeline Smith,
Aidan Peppin, Sungjin Hong, Manoj Govindassamy,
Terrence Zhao, Sandra Kublik, Meor Amer, Viraat
Aryabumi, Jon Ander Campos, Yi-Chern Tan, Tom
Kocmi, Florian Strub, Nathan Grinsztajn, Yannis Flet-
Berliac, and 26 others. 2024. Aya expanse: Combin-
ing research breakthroughs for a new multilingual
frontier. Preprint, arXiv:2412.04261.
DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingx-
uan Wang, Bochao Wu, Chengda Lu, Chenggang
Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan,
Damai Dai, Daya Guo, Dejian Yang, Deli Chen,
Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai,
and 181 others. 2025. Deepseek-v3 technical report.
Preprint, arXiv:2412.19437.
Alexander R. Fabbri, Diego Mares, Jorge Flores, Meher
Mankikar, Ernesto Hernandez, Dean Lee, Bing Liu,
and Chen Xing. 2025. Multinrc: A challenging and
native multilingual reasoning evaluation benchmark
for llms. Preprint, arXiv:2507.17476.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schel-
ten, Alex Vaughan, Amy Yang, Angela Fan, Anirudh
Goyal, Anthony Hartshorn, Aobo Yang, Archi Mi-
tra, Archie Sravankumar, Artem Korenev, Arthur
Hinsvark, and 542 others. 2024. The llama 3 herd of
models. Preprint, arXiv:2407.21783.
Md. Arid Hasan, Maram Hasanain, Fatema Ahmad,
Sahinur Rahman Laskar, Sunaya Upadhyay, and
1 others. 2025.
Nativqa: Multilingual culturally-
aligned natural query for llms. In Findings of the As-
sociation for Computational Linguistics: ACL 2025,
Vienna, Austria. Association for Computational Lin-
guistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring massive multitask language under-
standing. Preprint, arXiv:2009.03300.
Mete Ismayilzada, Debjit Paul, Syrielle Montariol, Mor
Geva, and Antoine Bosselut. 2023. Crow: Bench-
marking commonsense reasoning in real-world tasks.
Preprint, arXiv:2310.15239.
Bill Yuchen Lin, Seyeon Lee, Xiaoyang Qiao, and Xi-
ang Ren. 2021. Common sense beyond english: Eval-
uating and improving multilingual language models
for commonsense reasoning. In Proceedings of the
59th Annual Meeting of the Association for Compu-
tational Linguistics, Online. Association for Compu-
tational Linguistics.
Junho Myung and 1 others. 2024. Blend: A bench-
mark for llms on everyday knowledge in diverse cul-
tures and languages. In Advances in Neural Informa-
tion Processing Systems (Datasets and Benchmarks
Track).
OpenAI, Josh Achiam, Steven Adler, Sandhini Agarwal,
Lama Ahmad, Ilge Akkaya, Florencia Leoni Ale-
man, Diogo Almeida, Janko Altenschmidt, Sam Alt-
man, Shyamal Anadkat, Red Avila, Igor Babuschkin,
Suchir Balaji, Valerie Balcom, Paul Baltescu, Haim-
ing Bao, Mohammad Bavarian, Jeff Belgum, and
262 others. 2024. Gpt-4 technical report. Preprint,
arXiv:2303.08774.
Edoardo Maria Ponti, Goran Glavaš, Olga Majewska,
Qianchu Liu, Ivan Vuli´c, and Anna Korhonen. 2020.
Xcopa: A multilingual dataset for causal common-
sense reasoning. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing, Online. Association for Computational
Linguistics.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan
Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin
Yang, Jiaxi Yang, Jingren Zhou, and 25 oth-
ers. 2025.
Qwen2.5 technical report.
Preprint,
arXiv:2412.15115.
Abhinav Sukumar Rao, Akhila Yerukola, Vishwa Shah,
Katharina Reinecke, and Maarten Sap. 2025. Nor-
mad: A framework for measuring the cultural adapt-
ability of large language models. In Proceedings
of the 2025 Conference of the Nations of the Amer-
icas Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume
1: Long Papers), page 2373–2403. Association for
Computational Linguistics.
Angelika Romanou, Negar Foroutan, Anna Sotnikova,
Sree Harsha Nelaturu, Shivalika Singh, Rishabh
Maheshwary, Micol Altomare, Zeming Chen, Mo-
hamed A. Haggag, Snegha A, Alfonso Amayue-
las, Azril Hafizi Amirudin, Danylo Boiko, Michael
Chang, Jenny Chim, Gal Cohen, Aditya Kumar
Dalmia, Abraham Diress, Sharad Duwal, and 38
others. 2025. INCLUDE: Evaluating multilingual
language understanding with regional knowledge. In
The Thirteenth International Conference on Learning
Representations.
David Romero, Chenyang Lyu, Haryo Akbarianto Wi-
bowo, Teresa Lynn, Injy Hamed, Aditya Nanda
Kishore, Aishik Mandal, Alina Dragonetti, Artem
Abzaliev, Atnafu Lambebo Tonja, Bontu Fufa Balcha,
Chenxi Whitehouse, Christian Salamea, Dan John
Velasco, David Ifeoluwa Adelani, David Le Meur,
Emilio Villa-Cueva, Fajri Koto, Fauzan Farooqui, and
57 others. 2024. Cvqa: Culturally-diverse multilin-
gual visual question answering benchmark. Preprint,
arXiv:2406.05967.
Abdelrahman Sadallah, Junior Cedric Tonga, Khalid
Almubarak, Saeed Almheiri, Farah Atif, and 1 oth-
ers. 2025. Commonsense reasoning in arab culture.
arXiv preprint, arXiv:2502.12788.
10

--- Page 11 ---

Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhagavat-
ula, and Yejin Choi. 2019. Winogrande: An adver-
sarial winograd schema challenge at scale. Preprint,
arXiv:1907.10641.
Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David I. Adelani, Jian Gang Ngui, Daniel
Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
sio, Wei Qi Leong, Yosephine Susanto, Raymond
Ng, Shayne Longpre, Wei-Yin Ko, Sebastian Ruder,
Madeline Smith, Antoine Bosselut, Alice Oh, Andre
F. T. Martins, Leshem Choshen, and 5 others. 2025.
Global mmlu: Understanding and addressing cul-
tural and linguistic biases in multilingual evaluation.
Preprint, arXiv:2412.03304.
Koustuv Sinha, Shagun Sodhani, Jin Dong, Joelle
Pineau, and William L. Hamilton. 2019. CLUTRR:
A diagnostic benchmark for inductive reasoning from
text.
In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
4506–4515, Hong Kong, China. Association for Com-
putational Linguistics.
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam Fisch,
Adam R. Brown, Adam Santoro, Aditya Gupta,
Adrià Garriga-Alonso, Agnieszka Kluska, Aitor
Lewkowycz, Akshat Agarwal, Alethea Power, Alex
Ray, Alex Warstadt, Alexander W. Kocurek, Ali
Safaya, Ali Tazarv, and 432 others. 2023.
Be-
yond the imitation game: Quantifying and extrap-
olating the capabilities of language models. Preprint,
arXiv:2206.04615.
Mirac Suzgun, Nathan Scales, Nathanael Schärli, Se-
bastian Gehrmann, Yi Tay, Hyung Won Chung,
Aakanksha Chowdhery, Quoc V. Le, Ed H. Chi,
Denny Zhou, and Jason Wei. 2023.
Challenging
big-bench tasks and whether chain-of-thought can
solve them. In ACL (Findings), pages 13003–13051.
Sshubam Verma, Mohammed Safi Ur Rahman Khan,
Vishwajeet Kumar, Rudra Murthy, and Jaydeep Sen.
2025. MILU: A multi-task Indic language under-
standing benchmark. In Proceedings of the 2025
Conference of the Nations of the Americas Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Pa-
pers), pages 10076–10132, Albuquerque, New Mex-
ico. Association for Computational Linguistics.
Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni,
Abhranil Chandra, Shiguang Guo, Weiming Ren,
Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max
Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue,
and Wenhu Chen. 2024. Mmlu-pro: A more robust
and challenging multi-task language understanding
benchmark. Preprint, arXiv:2406.01574.
Jason Weston, Antoine Bordes, Sumit Chopra, Alexan-
der M. Rush, Bart van Merriënboer, Armand Joulin,
and Tomas Mikolov. 2015.
Towards ai-complete
question answering: A set of prerequisite toy tasks.
Preprint, arXiv:1502.05698.
Haryo Wibowo, Erland Fuadi, Made Nityasya, Radi-
tyo Eko Prasojo, and Alham Aji. 2024. COPAL-ID:
Indonesian language reasoning with local culture and
nuances. In Proceedings of the 2024 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), pages 1404–1422,
Mexico City, Mexico. Association for Computational
Linguistics.
Genta Indra Winata, Frederikus Hudi, Patrick Amadeus
Irawan, David Anugraha, Rifki Afina Putri, Wang Yu-
tong, Adam Nohejl, Ubaidillah Ariq Prathama, Ned-
jma Ousidhoum, Afifa Amriani, and 1 others. 2025.
Worldcuisines: A massive-scale benchmark for mul-
tilingual and multicultural visual question answering
on global cuisines. In Proceedings of the 2025 Con-
ference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers),
pages 3242–3264.
Weihao Xuan, Rui Yang, Heli Qi, Qingcheng Zeng,
Yunze Xiao, Aosong Feng, Dairui Liu, Yun Xing, Jun-
jue Wang, Fan Gao, Jinghui Lu, Yuang Jiang, Huitao
Li, Xin Li, Kunyu Yu, Ruihai Dong, Shangding
Gu, Yuekang Li, Xiaofei Xie, and 13 others. 2025.
Mmlu-prox:
A multilingual benchmark for ad-
vanced large language model evaluation. Preprint,
arXiv:2503.10497.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, Chujie Zheng, Day-
iheng Liu, Fan Zhou, Fei Huang, Feng Hu, Hao
Ge, Haoran Wei, Huan Lin, Jialong Tang, and 41
others. 2025.
Qwen3 technical report.
Preprint,
arXiv:2505.09388.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019.
Hellaswag: Can
a machine really finish your sentence?
Preprint,
arXiv:1905.07830.
A
Data Statistics in More Detail
This appendix provides (i) additional dataset statis-
tics, (ii) full benchmark breakdowns by script and
by language/cultural context, (iii) the exact evalu-
ation prompts used for all model settings, and (iv)
screenshots of the annotation platform.
11

--- Page 12 ---

A.1
Cultural-aspect coverage
0
100
200
300
400
Number of Templates
Cities and Landmarks
Events and Festivals
Food and Cuisine
Famous People
Music and Art
Politics and Governance
Fashion and Media
Objects and Units
Education
Social Customs
Brands and Commerce
socio-religious aspects of life
Literature and Written works
Time
Folklore and Folktales
Sports
Transportation
Agriculture
Death and Funerals
Language and Communication
Relationships
Naming
Cultural Aspect
Figure 6: Distribution of cultural-aspect tags in the
benchmark. Bars report the number of template in-
stantiations tagged with each of the 22 cultural aspects.
Aspects are not mutually exclusive, so a single item may
contribute to multiple bars.
A.2
Reasoning-category coverage
Multi-hop Reasoning
32.7%
Commonsense Reasoning
19.9%
Logical Reasoning
14.7%
Temporal Reasoning
13.9%
Mathematical Reasoning
10.2%
Spatial Reasoning
4.7%
Causal Reasoning
3.8%
Figure 7: Distribution of reasoning-category tags in
the template set. Percentages are normalized over tag
assignments (multi-label items contribute multiple as-
signments).
B
Detailed Benchmark Results
This section reports accuracy on local-language
evaluation instances (MC–L, T–L, F–L), aggre-
gated either (i) by writing system (macro-averaging
across languages that share a script) or (ii) by
benchmark language/cultural context.
C
Evaluation Prompts
We evaluate each model under two prompting
regimes. For standard (non-thinking) models,
we request a direct answer without eliciting expla-
nations. For thinking-capable models, we allow
step-by-step reasoning but enforce a strict final-line
JSON output format for automatic parsing.
C.1
Non-thinking models: Multiple-choice
prompt
Non-Thinking Models: MCQ Prompt
Question: {question}
A) {option1}
B) {option2}
C) {option3}
D) {option4}
Answer directly without any explanation or
reasoning.
Output a single line containing only a JSON
object of the form:
{"answer": "X"}
Replace X with the correct letter (A, B, C,
or D).
Do not include anything else.
C.2
Non-thinking models: True/False prompt
Non-Thinking Models: True/False Prompt
Statement: {question}
Answer directly without any explanation or
reasoning.
Output a single line containing only a JSON
object of the form:
{"answer": "ANSWER"}
Replace ANSWER with either "T" for True or
"F" for False.
Do not include anything else.
C.3
Thinking models: Multiple-choice
prompt
Thinking Models: MCQ Prompt
Question: {question}
A) {option1}
B) {option2}
C) {option3}
D) {option4}
First, you may think step by step to solve
the question.
12

--- Page 13 ---

At the very end, output a single line
containing only a JSON object of the
form:
{"answer": "X"}
Replace X with the correct letter (A, B, C,
or D).
Do not include anything else on that final
line.
C.4
Thinking models: True/False prompt
Thinking Models: True/False Prompt
Statement: {question}
First, you may think step by step.
At the very end, output a single line
containing only a JSON object of the
form:
{"answer": "ANSWER"}
Replace ANSWER with either "T" for True or
"F" for False.
Do not include anything else on that final
line.
C.5
Data verification prompt (GPT-5.2-chat)
To improve linguistic quality while preserving
meaning, we run an automated proofreading pass
using GPT-5.2-chat that is restricted to spelling and
grammar fixes only:
Data Verification Prompt (GPT-5.2-chat)
You are a careful proofreader. Your task is
to check this {context} for ONLY
grammatical and spelling mistakes.
**Instructions:**
1. Fix ONLY spelling errors and grammatical
mistakes
2. Preserve the exact writing style, tone,
and word choices
3. Keep all cultural references and proper
nouns exactly as they are
4. Do NOT rephrase or improve the writing -
only correct errors
5. If there are no errors, return the text
exactly as-is
**Common errors to check for:**
- **Spelling mistakes**: "recieve" ->
"receive", "occured" -> "occurred"
- **Plural/singular agreement**: "1 foods"
-> "1 food", "2 dish" -> "2 dishes"
- **Subject-verb agreement**: "they was" ->
"they were", "he don't" -> "he
doesn't", "that are" with singular ->
"that is"
- **Verb tense for past events**: "Is X
established in 1950?" -> "Was X
established in 1950?" (BE CONSISTENT
across similar questions)
- **Pronoun agreement**: Singular "their"
is acceptable as gender-neutral. Keep
it unless clearly wrong. Be CONSISTENT
within the same question set.
- **Unnecessary apostrophes**: "apple's"
(plural) -> "apples"
- **Capitalization**: Only fix clear errors
like "i" -> "I" or well-known proper
nouns (countries, famous people). DO
NOT automatically capitalize cultural
terms, food names, or words that might
be intentionally lowercase.
- **Article errors**: "a apple" -> "an
apple", "an hour" not "a hour"
**Text to check:**
{text}
**Response format:**
If there are errors:
{
"has_errors": true,
"corrected": "the corrected text here",
"explanation": "brief explanation of what
was fixed (e.g., 'Fixed plural/singular
agreement')"
}
If no errors:
{
"has_errors": false,
"corrected": "{text}",
"explanation": "No errors found"
}
Respond ONLY with valid JSON, nothing else.
C.6
Example templates by cultural aspect
D
Annotation Platform
Figure 8 shows the onboarding flow presented to
annotators, including requirements for cultural au-
thenticity and guidance for handling culturally spe-
cific items. Figure 9 and Figure 10 show the main
annotation interface used to instantiate templates
in English, translate them into the local language,
and generate verification statements.
13

--- Page 14 ---

Cultural Aspect: Example Templates (I)
Cultural Aspect: Example Templates (II)
Aspect
Template prompt
Aspect
Template prompt
Food and Cuisine
Which dish would [FAMOUS PERSON] probably
not recognize from their childhood?
Sports
In [CULTURE SPORT] tradition, what happens
when [CONDITION]?
Music and Art
Which traditional musical instrument from
[COUNTRY/REGION] has the earliest recorded
history?
Fashion and Media
I
couldn’t
stop
laughing
watching
a/an
[CULTURE/REGION] series with [ACTOR NAME].
Which of the following is most likely the
name of the series?
Cities and Landmarks
Among
all
the
provinces
in
[SET
OF
PROVINCES/LOCATION],
how
many
provinces
have an area smaller than [PROVINCE]?
Transportation
If I live in [LOCATION 1/RESIDENTIAL AREA 1]
and I want to go to [LOCATION 2/RESIDENTIAL
AREA 2], how much time would it take on
average if I traveled by [TRANSPORTATION
METHOD]?
Famous People
Who
among
these
[NATIONALITY]
[FAMOUS
PEOPLE TYPE] does NOT share the key trait
of [COMMON TRAIT]?
Education
Which
[ACADEMIC
PERIOD]
would
a
[AGE]-year-old typically be in according
to [COUNTRY]’s education system?
Politics and Governance
What is the name of the first child of the
[Nth] president/leader of [COUNTRY]?
Agriculture
In [REGION] during [MONTH], which crop is
typically being [AGRICULTURAL ACTIVITY]?
Events and Festivals
Which of the following special days is the
closest to [EVENT]?
Naming
If
my
friend
has
the
last
name
"[LAST
NAME]", which country is most likely their
birthplace?
Objects and Units
In [CULTURE] traditional measurements, how
many [UNIT] equal one [LARGER UNIT]?
Folklore and Folktales
In [CULTURE]’s folk tales, which character
would
be
considered
out
of
place
if
it
appears alongside [CHARACTER]?
Socio-religious Aspects of
Life
According
to
[NATIONALITY]
cultural
superstition,
what
should
one
do
after
[ACTION] to avoid bad luck?
Brands and Commerce
Among
these
local
brands
in
[CULTURE/REGION],
which
one
would
a
typical middle-income person be most likely
to use?
Language and Communi-
cation
In [COUNTRY], which age group or social
category
is
LEAST
likely
to
use
the
expression "[COMMON PHRASE]" to describe
[MEANING OF EXPRESSION TO THEM]?
Death and Funerals
In [CULTURE/REGION], how many days after
death
is
[RITUAL/EVENT]
traditionally
performed?
Social Customs
In
[COUNTRY/REGION],
when
[CONDITION/ACTIVITIES],
which
of
the
following actions is considered a taboo?
Time
If
you
convert
[DATE]
in
the
[CALENDAR
SYSTEM] calendar to the Gregorian calendar
in [YEAR], which month would it fall in?
Relationships
If I call my [NATIONALITY] father [TERM],
would my children call him [OPTION A]?
Literature
and
Written
works
What age-appropriate book can I buy for my
[AGE]-year-old son?
Table 6: Cultural aspects covered in the benchmark, with one example template per aspect.
14

--- Page 15 ---

Figure 8: Onboarding landing page (Part 1 of 3).
15

--- Page 16 ---

Figure 8: Onboarding landing page (Part 2 of 3).
16

--- Page 17 ---

Figure 8: Onboarding landing page (Part 3 of 3).
17

--- Page 18 ---

Figure 9: Annotation interface (Part 1 of 2): Contextualization.
18

--- Page 19 ---

Figure 10: Annotation interface (Part 2 of 2): Instantiation and translation.
19

```
