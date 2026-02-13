---
title: "2025-Ghaly-Assessing Large Language Models on Islamic - PDF Extract"
source_pdf: "2025-Ghaly-Assessing Large Language Models on Islamic.pdf"
pages: 10
extracted_at: "2026-02-13T09:15:44.249872"
---

# PDF Extract: 2025-Ghaly-Assessing Large Language Models on Islamic

**Source PDF:** 2025-Ghaly-Assessing Large Language Models on Islamic.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Assessing Large Language Models on Islamic Legal Reasoning:
Evidence from Inheritance Law Evaluation
Abdessalam BOUCHEKIF1
Samer RASHWANI1
Heba Sbahi1
Shahd Gaben1
Mutaz AL-KHATIB1
Mohammed GHALY1
1Hamad Bin Khalifa University, Qatar
{abouchekif, srashwani, mghaly, malkhatib, sgaben, hsbahi}@hbku.edu.qa
Abstract
This paper evaluates the knowledge and
reasoning capabilities of Large Language
Models in Islamic inheritance law, known
as 'ilm al-maw¯ar¯ıth. We assess the perfor-
mance of seven LLMs using a benchmark
of 1,000 multiple-choice questions covering
diverse inheritance scenarios, designed to
test each model’s ability, from understand-
ing the inheritance context to computing
the distribution of shares prescribed by Is-
lamic jurisprudence. The results reveal a
significant performance gap: o3 and Gemini
2.5 achieved accuracies above 90%, whereas
ALLaM, Fanar, LLaMA, and Mistral scored
below 50%. These disparities reflect impor-
tant differences in reasoning ability and
domain adaptation. We conduct a detailed
error analysis to identify recurring failure
patterns across models, including misunder-
standings of inheritance scenarios, incorrect
application of legal rules, and insufficient
domain knowledge. Our findings highlight
the limitations of current models in han-
dling structured legal reasoning and suggest
directions for improving their performance
in Islamic legal reasoning. Our code is avail-
able at https://github.com/bouchekif/
inheritance_evaluation
1
Introduction
In recent years, the application of Large Lan-
guage Models (LLMs) to Islamic domains has
attracted growing interest in the NLP com-
munity.
This progress has been driven by
the emergence of open-source Arabic LLMs
and the development of shared tasks target-
ing Islamic NLP. Models such as Falcon (Al-
mazrouei et al., 2023), Jais (Sengupta et al.,
2023), AceGPT (Huang et al., 2023), Arabi-
anGPT (Koubaa et al., 2024), ALLaM (Bari
et al., 2024), and Fanar (Abbas et al., 2025)
have been pretrained on large-scale Arabic cor-
pora including Quranic verses, Hadith, and
fatwa archives, enabling new capabilities in re-
ligious text understanding.
Several shared tasks have been proposed to
benchmark LLMs on Islamic texts, such as
Quranic QA (Malhas et al., 2022, 2023) and
general Islamic knowledge retrieval (Qamar
et al., 2023). More recently, the QIAS 2025
shared task (Bouchekif et al., 2025) was intro-
duced to evaluate LLMs on religious and legal
reasoning through two subtasks: (1) Islamic
Inheritance Reasoning, which involves comput-
ing inheritance shares based on Islamic ju-
risprudence; and (2) Islamic Knowledge Assess-
ment, which covers core disciplines such as fiqh,
Hadith, and tafsir. (Sayeed et al., 2025) ex-
plored QA systems for t.ibb nabaw¯ı (Prophetic
medicine) using LLaMA-3, Mistral-7B, and
Qwen-2 combined with Retrieval-Augmented
Generation (RAG), while (Alan et al., 2024)
proposed MufassirQAS, a RAG-based system
trained on Turkish Islamic texts to improve
transparency and reduce hallucinations in reli-
gious QA. (Rizqullah et al., 2023) introduced
the QASiNa QA dataset, derived from Sirah
Nabawiyah texts in Indonesian, comparing tra-
ditional multilingual transformers (XLM-R,
mBERT, IndoBERT) with GPT-3.5 and GPT-
4. (Qamar et al., 2024) introduced a dataset of
73,000 non-factoid QA pairs covering Quranic
Tafsir and Hadith. The study revealed a crit-
ical gap between automatic evaluation met-
rics (such as ROUGE) and human judgments.
These results show that automatic evaluation
metrics alone are not sufficient, and highlight
the need for more robust evaluation methods
that can better reflect the complexity and in-
terpretive nature of Islamic religious texts. In
Aleid and Azmi (2025), the authors released
Hajj-FQA, a benchmark of 2,826 QA pairs
extracted from 800 expert-annotated fatwas
concerning the Hajj pilgrimage. Despite these
arXiv:2509.01081v2  [cs.CL]  17 Sep 2025

--- Page 2 ---

efforts, multiple studies have reported critical
limitations in the performance of LLMs on Is-
lamic content. For instance, (Mohammed et al.,
2025) shows that even advanced models like
GPT-4 tend to produce factually incorrect or
misleading answers when applied to Islamic
content. They identify three main issues: (i)
misinterpretation of religious context, (ii) gen-
eration of unclear or unreliable answers not
grounded in authoritative Islamic sources, and
(iii) sensitivity to minor variations in question
phrasing, often resulting in inconsistent out-
puts. Similarly, (Alnefaie et al., 2023) observed
that GPT-4 has difficulty answering Quranic
questions accurately, due to difficulties with
classical Arabic, semantic ambiguity, and mis-
interpretation of contextual meaning.
Early research on automating Islamic inher-
itance (hereafter IRTH) began with expert
systems focused on calculating basic inheri-
tance shares (Akkila and Naser, 2016). Later
works incorporated intricate adjustments such
as h.ajb, 'awl, and radd (Tabassum et al., 2019).
(Zouaoui and Rezeg, 2021) introduced an Ara-
bic ontology for identifying heirs and calculat-
ing their inheritance shares (Tabassum et al.,
2019). In this work, we evaluate seven LLMs
on their ability to reason over inheritance prob-
lems, reporting both quantitative performance
metrics and qualitative analyses, revealing spe-
cific reasoning failures as well as broader model
limitations. This paper is organized as follows:
Section 2 introduces the foundations of IRTH.
Section 3 describes the dataset, while Section
4 details the experimental setup and results.
In Section 5, we analyze the justifications that
models provide for their answers. Finally, Sec-
tion 6 concludes the paper with a discussion of
future work.
2
Background on Islamic
Inheritance Law
Islamic inheritance law involves intricate tex-
tual interpretation and structured legal reason-
ing grounded in the Quran, Prophetic tradi-
tion (Sunnah), and Islamic jurisprudence. It
governs the distribution of the estate of a de-
ceased person through a fixed legal framework
that combines normative principles with pre-
cise arithmetic calculations.
Solving inheritance problems requires a combi-
nation of cognitive, legal, and computational
skills, including:
• Identifying familial relationships and con-
sidering legal conditions such as debts, be-
quests, and the sequence of deaths among
relatives.
• Determining eligible heirs, including fixed-
share heirs (as.h. ¯ab al-fur¯ud. ) and residuaries
('as.ab¯at), and correctly applying exclusion
rules (h. ajb) based on valid justifications
and authentic scriptural evidence.
• Computing shares by deriving a common
denominator and adjusting the distribu-
tion when necessary:
– Radd (redistribution) is used when a
surplus remains after initial allocation.
This surplus is proportionally redis-
tributed among the heirs, excluding
spouses.
Example: Wife (1/4) and full sister
(1/2), leaving a surplus of 1/4; after
redistribution, the wife receives (1/4)
and the sister receives (3/4).
– 'Awl (proportional reduction) is ap-
plied when the sum of assigned shares
exceeds the estate.
All shares are
scaled down proportionally.
Exam-
ple: Father (1/6), mother (1/6), wife
(1/8), and four daughters (2/3); the
total exceeds 1. The denominator is
adjusted to 27, and then the wife re-
ceives 3/27 = 1/9.
• Addressing complex and exceptional sce-
narios, such as consecutive death scenarios
(mun¯asakha) or juristic disputes like the
Akdariyya case involving grandparents and
siblings.
• Numerical precision in the final distribu-
tion, including the correct adjustment and
fractional allocation 1.
Given its structured rules, mathematical
computations, and reliance on Arabic jurispru-
dential sources, IRTH presents a real-world
scenario for evaluating the reasoning abilities
of LLMs.
1For more details about the terminology and rules
of Islamic inheritance law, see “Irth,” in Al-Maws¯u'a al-
Fiqhiyya (The Kuwaitan Encyclopedia of Fiqh). Kuwait:
Waz¯arat al-Awq¯af wa-al-Shu'¯un al-Islamiyya. 45 Vols.
1984-2007. Vol. 3, Pp. 17-79.

--- Page 3 ---

3
Dataset Description
Our evaluation is based on the validation set of
the QIAS 2025 Shared Task2(Bouchekif et al.,
2025). The dataset was constructed from Is-
lamic religio-ethical advices (fatwas) collected
from IslamWeb3. Each fatwa was automati-
cally converted into multiple-choice questions
(MCQ) using Gemini 2.5 Pro, then reviewed
by four experts in Islamic studies to ensure
both legal soundness and linguistic clarity. As
part of the preprocessing phase, ambiguous
questions were rephrased to guarantee a sin-
gle, unambiguous interpretation. The answer
choices were also revised to eliminate semantic
and numerical redundancies, such as equivalent
options (e.g 1/2 and 2/4). Each MCQ presents
six answer choices, with a single correct an-
swer. These questions assess a model’s ability
to identify eligible heirs, apply fixed-share rules,
and reason through complex inheritance logic.
The dataset has two levels of difficulty: 500
MCQs labelled as Beginner and 500 Advanced,
reflecting increasing complexity in both legal
reasoning and mathematical computation.
• Beginner: identifying eligible heirs, their
basic shares, and non-eligible heirs.
• Advanced: handling multiple heirs, resid-
uary shares, partial exclusions, multi-
generational cases, fixed estate constraints,
and intricate fractional distributions.
Each example is evaluated based on its level
of difficulty—either beginner or advanced. This
approach allows us to distinguish between mod-
els lacking foundational knowledge and those
capable of solving complex cases that require
deeper legal reasoning. It enables a more pre-
cise analysis of limitations in legal reasoning
capacity across evaluated models.
4
Experiments and Results
4.1
Experimental Setup
We evaluate seven LLMs in a zero-shot set-
ting using Arabic prompts, without any task-
specific fine-tuning. The prompt clearly defines
the task, presents a multiple-choice question
with its options, and instructs the model to
select the correct answer and provide a justifi-
cation. This enables us to assess reasoning and
2https://sites.google.com/view/qias2025
3https://www.islamweb.net/
verify that its conclusions are based on logical
inferences rather than stochastic guesses. The
evaluated models include Arabic-specialized
LLMs optimized for Arabic language tasks,
open-source multilingual models, and commer-
cial multilingual models, with sizes ranging
from 7 to over 100 billion parameters (exact
sizes of the commercial models are not pub-
licly disclosed). The Arabic-focused models in-
clude Fanar (Islamic-RAG4), ALLaM-7B5, and
Mistral-Saba-24B6, a model that has achieved
competitive performance on standard Arabic
benchmarks. We also include LLaMA 3 70B7,
a powerful open-source multilingual model de-
veloped by Meta. As for commercial LLMs,
we evaluate three LLMs: Gemini 2.5 (flash-
preview), OpenAI’s o3 and GPT-4.5. Gemini
and o3 represent the state of the art in rea-
soning capabilities, while GPT-4.5 is widely
regarded as one of the most advanced models
in the GPT series.
4.2
Overall Performance
Table 1 summarizes model accuracy across the
three difficulty levels. The o3 model achieved
the highest overall accuracy (93.4%), followed
closely by Gemini (90.6%). GPT-4.5 achieved
74.0% accuracy, positioning it between models
with advanced reasoning capabilities and those
relying on heuristic inference. Fanar, ALLaM,
and LLaMA scored below 50%, revealing a
significant performance gap. The underperfor-
mance of ALLaM and Fanar may be partly due
to currently available smaller configurations
(e.g., 7B and 9B). Since no larger versions of
these models are publicly available, we evaluate
them in their current smaller versions, with a
focus on end-task performance and reasoning.
All models performed better on beginner-level
questions, which typically involve fewer heirs
and simpler distribution rules.
The perfor-
mance degradation at the Advanced level was
particularly evident for Arabic-focused models.
For example, ALLaM achieved 58.0% accuracy
4Accessible via a free public API: https://api.
fanar.qa/request/en
5An open-source Arabic model hosted on Hugging
Face:
https://huggingface.co/Abdelaali-models/
ALLaM-7B-Instruct-preview
6Available via the Groq platform: https://console.
groq.com/keys or Mistral’s official website: https://
admin.mistral.ai/organization/api-keys
7We access LLaMA 3 70B via the Groq API: https:
//console.groq.com/keys.

--- Page 4 ---

on Beginner cases but dropped to just 27.8%
on Advanced ones.
This highlights limited
capabilities in handling complex inheritance
scenarios. In contrast, reasoning models (i.e,
o3 and Gemini 2.5) maintained high perfor-
mance across both levels, suggesting superior
reasoning capabilities when handling complex
cases.
Model
Overall
Beginner
Advanced
o3
93.4
94.4
92.4
Gemini 2.5
90.6
91.6
89.6
GPT-4.5
74.0
86.8
61.2
LLaMA 3
48.8
57.8
39.8
Fanar 7B
48.1
60.4
35.8
Mistral
44.5
58.6
30.4
ALLaM 7B
42.9
58.0
27.8
Table 1: Accuracy (%) for each model across diffi-
culty levels.
4.3
Evaluation Criteria
To better understand model limitations, we
conducted a targeted error analysis on a subset
of 142 multiple-choice questions. This subset
consists of questions that were incorrectly an-
swered by all low-performing models (i.e., those
scoring below 50%). To guide this evaluation,
we categorize errors into two main types: foun-
dational and complex, based on an expert in
the IRTH domain. This structure allows for a
more precise distinction between errors caused
by legal misunderstanding and those requir-
ing advanced reasoning and computation. Our
analysis focused on three open-source models:
ALLaM, LLaMA, and Fanar8. For comparison,
we also included Gemini, which answered only
13 out of the 142 questions incorrectly. This
subset was reviewed by Islamic studies experts
who analyzed the justifications and annotated
the corresponding error types.
4.3.1
Foundational Errors (FD)
• Comprehension Error (CE): Misin-
terpretation of the problem statement,
such as misidentifying family relationships
or neglecting legally relevant information
8The Fanar model is publicly available on Hugging
Face
https://huggingface.co/QCRI/Fanar-1-9B.
We used the Islamic-RAG version, which is specifically
adapted to the Islamic domain and accessible via a free
public API.
(e.g., debts, bequests (was.¯ay¯a), or se-
quence of deaths).
• Error in Applying Normative Rules
(ENR): Incorrect legal analysis, including
heir misclassifications (e.g., as.h. ¯ab al-fur¯ud. ,
'as.ab¯at), misapplication of exclusion rules
(h. ajb), or incorrect scriptural citation.
• Basic Computational Error (BCE):
Simple arithmetic mistakes or hallucinated
numerical values in the final distribution.
4.3.2
Complex Errors (CPLX)
• Error in Calculatory Adjustment
(ECA): Failure to perform advanced
mathematical operations required for es-
tate division, including:
– Adjustment (Tas.h.¯ıh. ):
Incorrect
modification of the base denomina-
tor.
– Redistribution (Radd): Misalloca-
tion of estate surplus.
– Proportionate Reduction ('Awl):
Failure to proportionally reduce all
shares when total claims exceed the
estate.
• Error in Resolving Exceptional and
Disputed Cases (ERE): Inability to re-
solve non-standard or disputed cases (e.g.,
involving grandfather and siblings, or suc-
cessive deaths (mun¯asakha)).
Type
ALLaM
Fanar
LLaMA
Gemini
ENR
38.0
47.9
44.4
4.9
CE
4.2
4.9
0.7
0.0
BCE
3.5
3.5
4.2
0.7
FD Total
45.8
56.3
49.3
5.6
ECA
54.2
43.7
50.7
9.2
CPLX Total
54.2
43.7
50.7
9.2
Table 2: Distribution of error types across models
(expressed as percentages) based on 142 jointly in-
correct answer selections. FD: Foundational Errors.
CPLX: Complex Errors.
4.4
Results analysis
As shown in Table 2, open-source models fail
in the foundational elements of IRTH, such
errors represent 45.8% of the wrong answers
selected by ALLaM, 56.3% by Fanar, and 49.3%
by LLaMA, mainly due to ENR-related issues.
This finding is particularly noteworthy given

--- Page 5 ---

#
Question
Answer
Model
1
:ytn¤ yn ¤ ¤E  yw
 ­d w  nb  hF  d 
?Trt  hF wm
 d ¤ hF Yl O ­d w  nb A O Yl Anb  O Amny ,Trt Am ,Trt  O ¤z  ºAW d` Yqbt§
Ánbasat  A Â`uÂC ÄanuhaÁ¤〉:§rk   rq ¨ ºA
  ¨AtA¤ ,(23 :ºAsn ) 〈Åmut"basat  A ÅmukaÁ¤
ynb ¤ ,d ¤ hF Yl O ­d w  nb .¨Ab   AmFAqt§
LLaMA
2
n ,1  d yqJ   ¨w
 1  d TqyqJ  ,2  d
?n  hF  d
Anb    Atn ¤ yqJ  An¡  A  Ð
yqK  °  wk§ |rfA ,TqyqK  ± ¤
Am .©¤AstA Anbl ¨Ab ¤ Trt  O
Onl Yqbt§ ,Trt  O @§ ±   
­d ¤ k Trt  C  A`§ A © rµ Yl n  O§ ,@ .ytnb  
Tyrq  T§µ  Y dnts  @¡¤
. AmhF
11 :ºAsn  〈ÂFÂduÌs  ÃhiÌÂila ¿­Áw"Ã Âha ÁAa ÅÃa〉
Trt  ¨A ysq Y ¾AynmR ryK ¨t ¤
Ak 	s A³ ¤ Cw@  
CA±  y
Yl ¾ºAn k¤ .T¤r`m  Ty®F³  §C wm ,Anb ¤ yqK  ¯ ¤ TqyqK  ±   w¤
¯  @§ y ÅyAbA" ­dA ybW t§
y ¨Ab  sq§¤ Trt  O yqK .©¤AstA Anb Fanar
3
¤ ,¢¤ ,dyw  ¢n   ¨w
.C¯¤ 0007 lb r¤ ,£d ¤
? lbm   ¢ 	yO 
A¾An  ym  r  Ð ,§rk   rql ¾Aq¤
¢l  wq§ y ,£ry d r§ ® ,A¾dy¤
 A  〉:11 T§µ  ºAsn  ­CwF ¨ YA`
© ±  r  ,@ .〈On  ¢l d¤ ¢
  ¢§wnt  	§ k .TA  £@¡ ¨ º¨J
Tmsq  Hy¤ ¨rK  	yOnA l`t§  @¡
¨ AhrÐ ¨t   w° Tyr  TyAm y w Yl ¾ºAn ryt d ¨t ¤  ¥s 	s k¤ .Trt  §Ewt T}A  T¤d Adn ±  r ¯ ,Ty®F³  TyrK  Ak± .¨ rÐ   An¡  wk§
Fanar
4
3 ,yqJ  4 , ,¤E  yw
?° ­w³  	yO A .±   
,rÐ  ¯ TCw   ym  rt§   Ð
 m  ww A¾ARr xds  ¢±  
¿­Áw"Ã Âha ÁAa ÅÃa :YA` ¢l  A ,­w³ ,TA  £@¡ ¨¤
.11:ºAsn  ÂFÂduÌs  ÃhiÌÂila
  3¤ yqJ  4) ­w³   m dw§
.xds  ±  	yO  wk§  @ ,(± Fanar
5
n ,(2  d` ) yqJ  : ¨w
.(1  d` ) TqyqJ  ,(4  d` )
?Anb   ­d ¤ k ¾AmhF 
TqyqJ ¤ ­d ¤ n  w¤ TA ¨
O @ TqyqK  ±    ,­d ¤
 Ð
.rµ  On  @ nb ¤ ,Trt rtK§ h ,n  r An¡  A
 wk§ ,TA  £@¡ ¨ .©¤AstA On  ¨
k   © ,On   d ¤ hF n k
.TlAk  Trt   ymhF n
ALLaM
6
3 ,yqJ  4 , ,¤E  yw
?° ­w³  	yO A .±   
ÃÌluki Ãh"§ÁwaÁiÁ¤〉:ºAsn  ­CwF ¨ YA` ¢l  A
〈¿daÁ¤ Âha ÁAa  Ã ÁÁra AaÌmi ÂFÂduÌs  Aamuh"niÌ ¿diAÁ¤
 Ar§ 
± ¤ ±  ,TA  £@¡ ¨ .(11 :ºAsn )
.A¾AS§ xds   wr§ ° ­w³ ¤ ,xds ALLaM
7
¤
n¤
T¤E

¨w
T`C r¤ ,TqyqJ¤ yqyqJ¤
T¤z  @  .¾Af §rK¤
?lbm   @¡ 
,d¤ yml k§   Ð m  @ T¤z  Ã ÅmukuAÁ¤ÅEÁ ÁÁra Aa Âf"Oi ÅmukaÁw" :YA` ¢wq
T¤z    Am¤ .(21 :ºAsn ) Å¿daÁ¤ ÄanuhÌa uka§ ÅmÌa
¯ TtF w¡ m    ,d¤ Ah k§ 
ALLaM
Table 3: Examples of open-source models’ errors

--- Page 6 ---

that the questions were derived from fatwas on
IslamWeb, a data source presumably included
in the training corpora of the evaluated models.
4.4.1
Foundational Errors
Given the significant gap between commercial
and open-source models in handling founda-
tional errors, we analyze them separately. This
distinction allows us to better understand the
recurrent weaknesses specific to each model cat-
egory, particularly in tasks that require accu-
rate identification of heirs, correct application
of fixed-share rules, and adherence to norma-
tive principles of Islamic jurisprudence.
In Open-Source Models
• Errors in jus-
tification and scriptural citation: Some
models base their reasoning on fabricated
Quranic verses or prophetic narrations that do
not appear in any canonical collection, often re-
sulting in incorrect distribution of inheritance
shares. As illustrated in the first example of
Table 3, the model incorrectly assigned the
wife’s share as one-fourth, referencing the verse
”Åmut"basat  A ÅmukaÁ¤ Ánbasat  A Â`uÂC ÄanuhaÁ¤“ (“To
them belongs a quarter of what they earned,
and to you what you earned”) and attribut-
ing it to S¯urat al-Nis¯a' (4:32). This verse is
entirely fabricated and does not exist in the
Quran. Such hallucinations were frequently ob-
served across open-source models, representing
a serious issue in the Islamic context.
• Errors in Identifying Fixed Shares: Se-
lected open-source Arabic models misapplied
fixed-share rules for primary heirs (e.g., par-
ents, spouses, daughters).
For instance, in
Example 2, Fanar failed to allocate two-thirds
of the estate to the two daughters, even though
this share is explicitly prescribed in the Quranic
verse: Âl"i ÃrakaÄ@li ,"muÃ AaÅ¤Á ¨i ÂhaÌl  Âmukyi}wu§〉
Aaulu ÁÌnuhala Ãn"yatan"  ÁÅwa ¾ºAasi ÁÌnu ÅÃa ,in"yaya"Â"  ÃÌ\a
(4:11) 〈Âf"OiÌn  Aahala ¾­ÁdiAÁ¤ ÅtaAa ÅÃÁ¤ ,aÁra Aa.
Similarly, as shown in Example 3, Fanar er-
roneously denied the mother her fixed share,
based on the incorrect premise that the son’s
presence excludes all other heirs. This reason-
ing directly contravenes the explicit Quranic
stipulation that a mother receives one-sixth
of the estate if the deceased has offspring, as
stated in: (4:11) 〈ÂFÂduÌs  ÃhiÌÂila ¿daÁ¤ Âha ÁAa  Ãa〉.
• Comprehension Error: This type of error
occurs when models fail to correctly determine
which heir the question is referring to.
As
shown in Example 4, the model interpreted
the query as concerning the mother’s share,
whereas it explicitly asked about the maternal
brothers. Consequently, the model produced a
justification that was irrelevant to the question,
ultimately resulting in a wrong answer.
• Identifying eligible Heirs: Open-source
LLMs often make errors at the initial step of
inheritance distribution—identifying the eligi-
ble heirs—which subsequently leads to incor-
rect share assignments. These errors typically
take two forms: the omission of rightful heirs
and the inclusion of individuals not mentioned
in the scenario. For instance, in Example 5,
the model failed to recognize the brother as a
residuary heir, excluding him entirely from the
estate. Conversely, in Example 6, ALLaM erro-
neously included the father as an heir, despite
his absence from the question. This resulted in
an unjustified reallocation of shares, reducing
the portions assigned to the rightful heirs.
• Basic Computational Error: In some
cases, models correctly identify the eligible
heirs and apply the relevant inheritance rules,
yet still produce incorrect results due to basic
computational errors. For example, in ques-
tion 7, ALLaM correctly stated that the wife
is entitled to one-eighth of the estate, as the
deceased left behind a child. However, they
miscalculated one-eighth of 24,000 as 6,000,
whereas of the correct value of 3,000.
In Commercial Models
Gemini demon-
strates strong capabilities in understanding
inheritance questions, accurately interpreting
familial relationships, identifying eligible heirs,
and correctly applying fixed-share rules in ac-
cordance with Islamic jurisprudence. Its re-
sponses are generally well-structured, legally
sound, and supported by appropriate scrip-
tural references. However, Gemini occasionally
fails on questions that require a nuanced un-
derstanding of intra-madhhab distinctions. For
instance, as shown in Example 8, the model
was asked to apply the M¯alik¯ı position regard-
ing the inheritance of a khunth¯a mushkil—an
intersex individual whose gender cannot be

--- Page 7 ---

#
Question
Answer
8
kKm  Yn   ry k ¨
£r§dq ®tA ¢C lt§ ©@ TykAm  	¡@ w¡ A :Y ¤ ¾ rÐ
£@¡ ¨ kKm  Yn  §Cw ¨
?¾®RAft Amh C¤  Ð TA ¢C lt§ ©@  kKm  Yn  TA ¨ TykAm  «r§
¢`  C¤ ¢C RAf¤ ,Y ¤ ¾ rÐ £r§dq ®tA
± ) rR±A ¢` ¤ Yn    A`§   ,TCw  
¾ºAn Ð¤ ,C ¤ k qytm    E¤A d  AmS (¾AbyO
.KA Am  r} d db Yl
9
 ry k A ­w¤    ¨w
 Ð ¨ rOn  ¢y  lsm  ¯ ?¯  ®F b 
±  A
±    ,­d ¤ TqyqJ ¤ ­d ¤ n  w¤ TA ¨
 Ð .rµ  On  @ nb ¤ ,Trt  O @ TqyqK .©¤AstA On  ¨ rtK§ h ,n  r An¡  A
k   © ,On   d ¤ hF n k  wk§ ,TA  £@¡ ¨
.TlAk  Trt   ymhF n
Table 4: Examples of Gemini errors
definitively identified. In this case, inheritance
shares vary depending on the gender designa-
tion. Instead of referencing the M¯alik¯ı view,
Gemini erroneously justified its answer using
Sh¯afi'¯ı jurisprudence. This highlights a broader
limitation in the model’s ability to accurately
distinguish between the rulings of different Is-
lamic legal schools when such distinctions are
legally consequential.
Despite its overall competence, Gemini occa-
sionally showed weaknesses in nuanced scenar-
ios. For instance, it failed to correctly differen-
tiate between inheritance scenarios involving
conversion to Islam before or after death, as
illustrated in Example 9. In this case, since
both the father and the son were non-Muslims
before the father’s death, the son is deemed a
legitimate heir according to all scholars.
4.4.2
Complex Errors
Even when models accurately apply the
inheritance rules and identify eligible heirs,
they may still fail at later stages when faced
with complex scenarios, such as those requiring
the application of complex rules such as
proportional reduction ('awl) and residual
reallocation (radd).
• Distribution Denominator: Most errors
( 50%) committed by models involved miscal-
culations related to correcting the distribution
denominator according to the number of heirs.
This issue likely arises from their failure to
appreciate the mathematical necessity of such
corrections, a process historically used to avoid
fractions and ambiguity before calculators were
commonplace. While Gemini appeared to rec-
ognize the principle, but applied it inconsis-
tently, as illustrated in Example 10.
Open-source models encountered significant dif-
ficulties with distribution denominator correc-
tions, frequently becoming confused or trapped
in calculation loops. They often attempted to
calculate denominators prematurely, as shown
in Example 11, revealing poor understanding
of the sequential calculation steps required in
inheritance law.
• Redistribution (radd): Gemini occasion-
ally failed to redistribute leftover shares after
the initial allocation, as illustrated in Exam-
ple 12. In that case, the full sister initially
received 50% of the shares, with 25% of the
estate remaining. This should go to the heirs
other than spouses—in this case, the full sis-
ter—bringing her total share to 75%. Open-
source models consistently failed in such cases,
largely because initial distribution errors made
it impossible to identify residual shares requir-
ing redistribution.
• Proportionate Reduction ('awl): Gem-
ini consistently handled proportionate reduc-
tion scenarios accurately, clearly explaining
the underlying principle. Conversely, smaller
models consistently failed in proportionate re-
duction calculations, indicating a fundamental
misunderstanding of this critical inheritance
concept, even when the need for 'Awl was ex-
plicitly stated in the question. ALLaM in Ex-
ample 13, arbitrarily defined the 'Awl denom-
inator without first computing the individual
shares and their common denominator, leading
to an invalid final distribution.
• Resolving Exceptional and Disputed
Cases:
In cases involving juristic disagreement, all

--- Page 8 ---

#
Question
Answer
10
 ) ,3  d`  (yqJ ) : ¨w
 d`  (n) ,3  d`  (yqJ 
(TqyqJ ) ,1  d`  (T¤E) ,4
 T¤z  hF  d  .5  d` ?Om  Trt  }
 Ãa〉:YA` ¢wq ,(Anb ) C w  rf   ww m  T¤zl
(yOt  b) Tsm  } .〈ut"Ára AaÌmi ÂnumuÌ  ÁÌnuhala ¿daÁ¤ Åmuka ÁAa
,(3) Anb  	yO¤ (8) T¤z  	yO ¨Aq AS   wk§
©¤As§ 24  1
8 © ,m  w¡ }±   @¡  T¤z  hF .24 w¡¤
sqn§ ¯ TbO`l ¿A  ww ¾AyO At Tsm  :T\®) .3
d Y w}w  Tyfy Rw§ yl`t   @¡ k¤ ,hF¤¦C Yl
.(yOt  b T¤z  hF w¡¤ ­AW`m   CAy 11
,3  d`  (yqJ )
: ¨w
(n) ,3  d`  (yqJ   )
) ,1  d`  (T¤E) ,4  d`  d wm  .5  d`  (TqyqJ
Trt }C± Anb hF
?Om w¡ Om  Trt  }  C±  Anb  hF  d wm
ÅmuhuS"`a ÃAaÅCÁ"   wu¤ÂÁ¤〉:ºAsn  ­CwF ¨ YA` ¢l  A .A¾AmhF 30
YaÃ  wula`"fa ÅÁ AaÌÃ Án§ÃriAahum"AÁ¤ ÁnyiniÅ¥um"  Áni ÃhaÌl  ÃAati ¨i ¿{"`abi YaÅ¤Á
(7 T§µ ) 〈A¾CwuW"sa ÃAatik"  ¨i ÁkiÁÐ ÁAa A¾A¤Âr"`a Åmuki¶AayiÅ¤Á
12
¤ ­d ¤ T¤E  ¨w
	yOn  w¡ A ,­d ¤ TqyqJ
?Trt   C ¤ k ¨¶Ahn ÅmÌa  Ãaf" :YA` ¢wq C w  rf   w¤ d` r  r T¤z r ­d w  TqyqK  ± ¤ ."mut"Ára AÌami Â`ubÌÂr  Äanuhala ¿daÁ¤ ÅmukÌa uka§
,C ¤ r ¯¤ rÐ C ¤ } An¡ k§ ¤  rf   Ð On ."aÁra Aa Âf"Oi Aahala ¿"Â ÂhaÁ¤ ¿daÁ¤ Âha Ás"ya Ákala¡ ¿¦Âr"  ÃÃ" :YA` ¢wq
13
Y ,n¤ ¤ 
¤ ¤E  yw
?Trt  £@¡ w` 
Y A`u Tsm   ± Ð¤ ,12 Y A`u Tsm  ,Tsm  £@¡ ¨
Y ¤z  ASu§ y ,nb ¤ ± ¤ 
± ¤ ¤z   w¤ A ¨ 12
.5 Yl Trt  squ¤ (1 " 1 " 3) 5 x¤¦r   d bOy ,Tsm A¾Amyila ÁAa ÁhaÌl  ÁÌÃ ÃhaÌl  ÁniÌ ¾TaS§Ãraf" :ºAsn  ­CwF ¨ YA` ¢l  A
(11 :ºAsn ) ÅA¾Amyika
14
¡ An¤ ºAn¤ ¤E  yw
¨ A¡ ¯¤ d ySf ° Ew§
? rym QwOn YA`¤ ¢AbF ¢l   ­Cdq TS§r  rym  Tms  ±
¤ Tmsq  £@¡ ryy d± Ew§ ¯¤ ,§rk   rq  ¨ Ty`W
A§ At ¨ YA` A .Ahy {` Yl TCw  {` ySf
.]11 :ºAsn [ (¾Amyk ¾Amyl  A ¢l    ¢l   TS§r) :§C wm Table 5: Examples of Gemini’s Complex Errors.
models consistently defaulted to the majority
opinion, likely due to a training data bias that
favors definitive answers over nuanced scholarly
disagreement (ikhtil¯af ).
Consequently, they
failed to acknowledge valid minority views, as
shown in Example 14. The optimal response
would be to note Imam Ahmad’s less common
but valid view: parents may give more to cer-
tain heirs during their lifetime—such as those
who are very poor or ill—even though this will
ultimately impact the total estate.
5
Analysis of Correct Answers
While standard evaluation focuses on answer
accuracy, this is insufficient in religious legal
contexts, particularly in inheritance law, where
the validity of the underlying reasoning is im-
portant. A correct prediction alone may mask
significant reasoning flaws if the accompanying
explanation is inadequate, irrelevant, or fabri-
cated. To further investigate the robustness of
the models’ reasoning, we manually analyzed
the justifications of 40 instances where mod-
els produced correct answers. Our analysis re-
vealed that even when lower-performing models
arrived at the correct answer, their justifica-
tions often reflected the same errors discussed
in section 4.4.1. In terms of comprehension,
Fanar presumed the presence of offspring, al-
though none were mentioned in the question,
as shown in Example 15. Justification errors
were also common; models cited irrelevant or
fabricated Quranic verses and hadiths, such
as LLaMA referencing a non-existent Hadith,
see Example 16. Moreover, we observed mis-
takes in the application of normative rules. In
Example 17, LLaMA split half the shares be-
tween brothers and sisters and gave two-thirds
to daughters, while the correct approach is to
grant daughters a fixed two-thirds share and
allocate the remainder to brothers and sisters.
As shown in Table 7, foundational errors
in comprehension and rule application were
present in 27.5% of ALLaM’s justifications,

--- Page 9 ---

#
Question
Answer
Model
15
§w ,T¤E ,
: ¨w
,AqyqJ  w Hm ,yqyqJ
 ¤ ,
±   ­w T®
?±  	yO A .
± ,C w  rf   ww ¾ARr xds  °   ,¨Awl`m ¾Aq¤
ÅÃ ÁÁra AÌami ÂFÂduÌs  Aamuh"ni ¿diAÁ¤ ÃÌluki Ãh"§ÁwaÁiÁ¤〉:YA` A Am
£@¡ ¨ ±  	yO  wk§ ,¨AtA¤ .]11 :ºAsn [ 〈¿daÁ¤ Âha ÁAa
.xds  w¡ TA Fanar
16
  1 ,yqJ  4  ¨w
 2 ,T¤E 1 ,n 4 , 1 ,± ?yqK  ±  C w A .TqyqJ
C ¤ An¡ k§   Ð 	yO`tA yqK  ±  r§ :yl`t r§ yqK  ±A" :©wbn  §d  ¨ ºA Am ,¢n 
r rÐ
  Ð 	yO`tA yqK  ±  r§ ¨AtA¤ ,"qyqK  ±   ry
.¢n 
r rÐ C ¤ An¡ k§
LLaMA
17
,(2  d` ) yqJ  : ¨w
 d` ) TqyqJ  ,(4  d` ) n
?C±  Anb  	yO w¡ A .(1
@§ yqK  ±A ,ºAn± ¤ TqyqK  ± ¤ yqK  ±  r§
Yqb§ ¨AtA¤ ,On  @ TqyqK  ± ¤ (On ) 
±  hF
± ¤ ,TCw  w¡ 
AOn   ± (¨Ab  On )  Al  Anbl
Yl Anb  Yqb¤ ,AmhbyO  ¤@§ TqyqK  ± ¤ yqK .¨Ab LLaMA
Table 6: Examples of correct answers accompanied by incorrect justifications.
32.5% of Fanar’s, and 47% of LlaMA’s.
In
stark contrast, Gemini consistently produced
sound justifications, demonstrating accurate
calculations, valid legal reasoning, and correct
citations. This disparity underscores that per-
formance evaluations must account for reason-
ing quality, as accuracy alone provides an in-
complete and potentially misleading assessment
of a model’s capabilities in this domain.
Type
ALLaM
Fanar
LLaMA
ENR
22.5 %
22.5%
44.5%
CE
5%
10%
2.5%
BCE
-
-
-
FD Total
27.5%
32.5%
47%
ECA
-
-
-
CPLX Total
-
-
-
Table 7: Distribution of error types in model justi-
fications for correct answers.
6
Conclusion
This paper addresses estate distribution ac-
cording to Islamic inheritance law using seven
distinct LLMs.
Due to the task’s complex-
ity, models with reasoning capabilities, such
as Gemini 2.5 and o3, demonstrated high per-
formance, achieving accuracy rates of 90.6%
and 93.4%, respectively. Models without rea-
soning capability, such as GPT-4.5—which
is considered one of the most powerful com-
mercial OpenAI models—achieved moderate
results (74%). Conversely, models like Jais,
Mistral, and LLaMA, despite strong perfor-
mance on several Arabic language benchmarks,
showed significantly lower accuracy, scoring be-
low 50%, reflecting their limitations in legal
reasoning. Our evaluations highlighted a clear
gap between models with reasoning abilities
and those without. This gap was particularly
evident among ALLaM, Fanar, LLaMA, and
Mistral, which consistently struggled with iden-
tifying complex familial relationships, evaluat-
ing diverse inheritance scenarios, and correctly
executing corrective calculations such as redis-
tribution (Radd) and proportionate reduction
('Awl). Future research should focus on de-
veloping agentic AI systems that can reason
step by step, follow legal rules precisely, and
adapt to complex inheritance cases. This in-
cludes creating high-quality datasets designed
to support legal reasoning, developed with the
guidance of experts in Islamic law.
References
Ummar Abbas, Mohammad Shahmeer Ahmad,
Firoj Alam, Enes Altinisik, Ehsannedin As-
gari, Yazan Boshmaf, Sabri Boughorbel, San-
jay Chawla, Shammur A. Chowdhury, Fahim
Dalvi, Kareem Darwish, Nadir Durrani, Mo-
hamed Elfeky, Ahmed K. Elmagarmid, Mo-
hamed Y. Eltabakh, Masoomali Fatehkia, Anas-
tasios Fragkopoulos, Maram Hasanain, Majd
Hawasly, and 22 others. 2025.
Fanar:
An
arabic-centric multimodal generative AI platform.
arXiv preprint, arXiv:2501.13944.
Alaa N Akkila and Samy S Abu Naser. 2016. Pro-
posed expert system for calculating inheritance
in islam. Technical report.
Ahmet Yusuf Alan, Enis Karaarslan, and Ömer
Aydin. 2024. A rag-based question answering

--- Page 10 ---

system proposal for understanding islam: Mufas-
sirqas llm. arXiv preprint arXiv:2401.15378.
Hayfa A Aleid and Aqil M Azmi. 2025.
Hajj-
fqa: A benchmark arabic dataset for develop-
ing question-answering systems on hajj fatwas:
H. aleid and a. azmi.
Journal of King Saud
University Computer and Information Sciences,
37(6):135.
Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz
Alshamsi, Alessandro Cappelli, Ruxandra Co-
jocaru, Mérouane Debbah, Étienne Goffinet,
Daniel Hesslow, Julien Launay, Quentin Malartic,
and 1 others. 2023. The falcon series of open lan-
guage models. arXiv preprint arXiv:2311.16867.
Sarah Alnefaie, Eric Atwell, and Mohammad Am-
mar Alsalka. 2023. Is gpt-4 a good islamic expert
for answering quran questions? In Proceedings
of the 35th Conference on Computational Lin-
guistics and Speech Processing (ROCLING 2023),
pages 124–133.
M. Saiful Bari,
Yazeed Alnumay,
Norah A.
Alzahrani, Nouf M. Alotaibi, Hisham A. Alyahya,
Sultan Alrashed, Faisal Mirza, Shaykhah Alsub-
aie, Hassan A. Alahmed, Ghadah Alabduljab-
bar, Raghad Alkhathran, Yousef Almushayqih,
Raneem Alnajim, Salman Alsubaihi, Maryam
Al Mansour, Majed Alrubaian, Ali Alammari,
Zaki Alawami, Abdulmohsen Al-Thubaity, and
6 others. 2024.
Allam: Large language mod-
els for arabic and english.
arXiv preprint
arXiv:2407.15390.
Abdessalam Bouchekif, Samer Rashwani, Mo-
hammed Ghaly, Mutez Al-Khatib, Emad Mo-
hamed, Wajdi Zaghouani, Heba Sbahi, Shahd
Gaben, and Aiman Erbad. 2025.
Qias 2025:
Overview of the shared task on islamic inheri-
tance reasoning and knowledge assessment. In
Proceedings of The Second Arabic Natural Lan-
guage Processing Conference, ArabicNLP 2025,
Suzhou, China, November 5–9, 2025. Association
for Computational Linguistics.
Huang Huang, Fei Yu, Jianqing Zhu, Xuening Sun,
Hao Cheng, Dingjie Song, Zhihong Chen, Abdul-
mohsen Alharthi, Bang An, Juncai He, and 1 oth-
ers. 2023. Acegpt, localizing large language mod-
els in arabic. arXiv preprint arXiv:2309.12053.
Anis Koubaa, Adel Ammar, Lahouari Ghouti,
Omar Najar, and Serry Sibaee. 2024.
Arabi-
angpt: Native arabic gpt-based large language
model. arXiv preprint arXiv:2402.15313.
Rana Malhas, Watheq Mansour, and Tamer El-
sayed. 2022. Qur’an QA 2022: Overview of the
first shared task on question answering over the
holy qur’an. In Proceedings of the 5th Workshop
on Open-Source Arabic Corpora and Processing
Tools, pages 79–87, Marseille, France. European
Language Resources Association.
Rana Malhas, Watheq Mansour, and Tamer El-
sayed. 2023.
Qur’an qa 2023 shared task:
Overview of passage retrieval and reading com-
prehension tasks over the holy qur’an. In Pro-
ceedings of ArabicNLP 2023, pages 690–701, Sin-
gapore.
Marryam Yahya Mohammed, Sama Ayman Ali,
Salma Khaled Ali, Ayad Abdul Majeed, and En-
saf Hussein Mohamed. 2025. Aftina: enhancing
stability and preventing hallucination in ai-based
islamic fatwa generation using llms and rag. Neu-
ral Computing and Applications, pages 1–26.
Faiza Qamar, Seemab Latif, and Rabia Latif. 2024.
A benchmark dataset with larger context for
non-factoid question answering over islamic text.
arXiv preprint arXiv:2409.09844.
Syed Qamar and 1 others. 2023.
A benchmark
dataset with larger context for qa over islamic
text. arXiv preprint.
Muhammad Razif Rizqullah, Ayu Purwarianti, and
Alham Fikri Aji. 2023. Qasina: Religious domain
question answering using sirah nabawiyah. In
2023 10th International Conference on Advanced
Informatics: Concept, Theory and Application
(ICAICTA), pages 1–6.
Mohammad Amaan Sayeed, Mohammed Talha
Alam, Raza Imam, Shahab Saquib Sohail, and
Amir Hussain. 2025.
From rag to agentic:
Validating islamic-medicine responses with llm
agents. arXiv preprint arXiv:2506.15911.
Neha Sengupta, Sunil Kumar Sahu, Bokang Jia,
Satheesh Katipomu, Haonan Li, Fajri Koto,
William Marshall, Gurpreet Gosal, Cynthia Liu,
Zhiming Chen, and 1 others. 2023. Jais and jais-
chat: Arabic-centric foundation and instruction-
tuned open generative large language models.
arXiv preprint arXiv:2308.16149.
Sadia Tabassum, AHM Hoque, Sharaban Twahura,
and Mohammad Osiur Rahman. 2019. Develop-
ing an islamic farayez system applying software
engineering. Jurnal Kejuruteraan, 31(1):25–38.
Samia Zouaoui and Khaled Rezeg. 2021. Islamic
inheritance calculation system based on arabic
ontology (arafamonto). Journal of King Saud
University-Computer and Information Sciences,
33(1):68–76.

```
