---
title: "2025-Unknown-MUDT A Dependency Annotation Framework for Low-Resource Uyghur - PDF Extract"
source_pdf: "2025-Unknown-MUDT A Dependency Annotation Framework for Low-Resource Uyghur.pdf"
pages: 20
extracted_at: "2026-02-13T13:57:14.915219"
---

# PDF Extract: 2025-Unknown-MUDT A Dependency Annotation Framework for Low-Resource Uyghur

**Source PDF:** 2025-Unknown-MUDT A Dependency Annotation Framework for Low-Resource Uyghur.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Construction and educational application of a linguistically
grounded dependency treebank for Uyghur
Jiaxin Zuo1,*, Yiquan Wang2, Yuan Pan3, and Xiadiya Yibulayin1,*
1College of Chinese Language and Literature, Xinjiang University, Urumqi, Xinjiang 830046, China
2College of Mathematics and System Science, Xinjiang University, Urumqi, Xinjiang 830046, China
3College of Computer Science and Technology, Xinjiang University, Urumqi, Xinjiang 830046, China
*Corresponding author: Jiaxin Zuo (zuojiaxin@stu.xju.edu.cn), Xiadiya Yibulayin (xadiya49@sina.cn)
Abstract
Developing effective educational technologies for low-resource agglutinative languages like Uyghur is often
hindered by the mismatch between existing annotation frameworks and specific grammatical structures. To ad-
dress this challenge, this study introduces the Modern Uyghur Dependency Treebank (MUDT), a linguistically
grounded annotation framework specifically designed to capture the agglutinative complexity of Uyghur, includ-
ing zero copula constructions and fine-grained case marking. Utilizing a hybrid pipeline that combines Large
Language Model pre-annotation with rigorous human correction, a high-quality treebank consisting of 3,456
sentences was constructed. Intrinsic structural evaluation reveals that MUDT significantly improves dependency
projectivity by reducing the crossing-arc rate from 7.35% in the Universal Dependencies standard to 0.06%.
Extrinsic parsing experiments using UDPipe and Stanza further demonstrate that models trained on MUDT
achieve superior in-domain accuracy and cross-domain generalization compared to UD-based baselines. To val-
idate the practical utility of this computational resource, an AI-assisted grammar tutoring system was developed
to translate MUDT-based syntactic analyses into interpretable pedagogical feedback. A controlled experiment
involving 35 second-language learners indicated that students receiving syntax-aware feedback achieved signif-
icantly higher learning gains compared to those in a control group. These findings establish MUDT as a robust
foundation for syntactic analysis and underscore the critical role of linguistically informed natural language pro-
cessing resources in bridging the gap between computational models and the cognitive needs of second-language
learners.
Keywords: Uyghur Language; Dependency Treebank; Intelligent Computer-Assisted Language Learning; Syn-
tactic Annotation; Low-Resource Languages.
1
Introduction
Mastering the rich agglutinative morphology of Uyghur presents a formidable challenge for second language
(L2) learners. Unlike analytic languages, Uyghur encodes complex grammatical relations—such as mood, voice,
and case—within dense suffix chains (Gulinigeer et al., 2021). Learners often struggle with opaque syntactic
structures, particularly zero copula constructions where the predicative link is implicit, and the nuanced logical
dependencies governing postpositional phrases (Little, 2001). While Intelligent Computer-Assisted Language
Learning (ICALL) systems offer a promising avenue for providing personalized, immediate feedback, their effi-
cacy is strictly bound by the accuracy of the underlying Natural Language Processing (NLP) models (Arnett and
Bergen, 2025; Settles et al., 2020). Unfortunately, for low-resource languages like Uyghur, a significant disconnect
remains between the linguistic reality of the language and its computational representation, creating a bottleneck
1
arXiv:2507.21536v2  [cs.CL]  20 Jan 2026

--- Page 2 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
that hinders the development of effective educational technology (Akhundjanova et al., 2025; Taguchi et al., 2022;
Hedderich et al., 2021).
Currently, the Universal Dependencies (UD) framework serves as the de facto standard for syntactic annota-
tion due to its cross-linguistic consistency (de Marneffe et al., 2021; Nivre et al., 2020). However, this universalist
approach often necessitates a trade-off: to maintain typological comparability, it abstracts away language-specific
details that are critical for precise grammatical analysis (Osborne and Gerdes, 2019). In the context of Uyghur,
the UD framework frequently collapses distinct semantic functions into generic labels and lacks explicit modeling
for phenomena such as zero copulas (Taguchi et al., 2022). For a learner seeking to understand why a sentence is
ungrammatical, a parser based on such simplified standards is insufficient; it leads to structural ambiguities and
parsing errors that effectively impose a performance ceiling on downstream applications. Consequently, advanc-
ing educational technology for Uyghur requires more than simply accumulating data; it demands a fundamental
paradigm shift toward an annotation framework that is grounded in linguistic reality (Mukherjee, 2006; Dash,
2024).
To bridge this gap between linguistic theory and educational practice, this study introduces the Modern Uyghur
Dependency Treebank (MUDT), a linguistically grounded annotation framework specifically engineered to cap-
ture the agglutinative complexity of Uyghur. Diverging from the generic principles of UD, MUDT incorporates a
multi-layered morphological decomposition and a tailored dependency taxonomy that explicitly handles zero cop-
ulas and fine-grained case marking. We constructed a high-quality treebank of 3,456 sentences through a rigorous
hybrid pipeline, combining pre-annotation by Large Language Models with extensive human correction (Gilardi
et al., 2023; Alizadeh et al., 2023; Bender et al., 2021).
Our evaluation confirms that this language-specific design translates into substantial computational and ped-
agogical benefits. Intrinsic structural analysis reveals that MUDT significantly simplifies dependency structures,
reducing the crossing-arc rate from 7.35% in the existing UD standard to a negligible 0.06%, thereby creating a
representation that is far more consistent and learnable for algorithms (Futrell et al., 2015; Yadav et al., 2021b). Ex-
trinsic parsing experiments using UDPipe and Stanza further demonstrate that models trained on MUDT achieve
superior in-domain accuracy and cross-domain generalization. Crucially, to validate the practical utility of this
resource, we developed an AI-assisted grammar tutoring system driven by the MUDT parser (Dada et al., 2024).
In a controlled experiment with 35 L2 learners, the system translated syntactic analyses into interpretable peda-
gogical feedback (Alharbi, 2023). Results indicated that students receiving this syntax-aware feedback achieved
significantly higher learning gains (13.73 points) compared to the control group (7.88 points). These findings
establish MUDT not only as a robust foundation for syntactic analysis but also as a critical enabler for the next
generation of intelligent language learning tools.
2
Related Work
2.1
Computational Challenges in the Morphology-Syntax Interface
The defining characteristic of agglutinative languages like Uyghur is the dense encoding of grammatical cate-
gories—such as case, mood, and person—within recursively attached suffixes. Consequently, words in Uyghur
function as complete syntactic units that would otherwise require full phrases in analytic languages (Tömür and
Lee, 2003; Seddah et al., 2013; Tsarfaty et al., 2013). From a dependency parsing perspective, this shifts the
computational burden from linear word order to the internal morphology-syntax interface. However, the lack
of explicit boundaries for argument roles, combined with the prevalence of implicit structures like zero copulas,
creates systematic ambiguities. Without fine-grained morphosyntactic modeling, parsers struggle to reconstruct
predicate-argument structures accurately, often failing to identify the correct head of a phrase (Eryi˘git et al., 2008;
Tusun and Hendriks, 2022).
These linguistic features introduce dual computational bottlenecks: the infinite productivity of word forms
2

--- Page 3 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
leads to severe data sparsity, while the complex many-to-many mapping between morphology and syntax often
traps statistical models in local optima (Seddah et al., 2013; Tsarfaty et al., 2010). In the context of ICALL, these
parsing deficiencies are particularly detrimental. If a model fails to decode the morphological cues governing
argument relations, it cannot distinguish between a learner’s error and a valid complex structure. This results in
feedback that is either generic or misleading, rather than pedagogically supportive (Ragheb and Dickinson, 2012;
Volodina et al., 2014). Therefore, explicit and accurate modeling of morphological complexity is a prerequisite
for any interpretable educational application (Meurers, 2021).
2.2
Limitations of Universal Dependencies for Educational Purposes
While the Universal Dependencies (UD) framework has successfully facilitated cross-lingual research (Nivre,
2016; de Marneffe et al., 2021; Croft et al., 2017), its design philosophy prioritizes typological parallelism over
language-specific granularity. To maintain compatibility across diverse languages, the UD standard for Turkic
languages often collapses specific case functions into generic labels (e.g., obl), effectively obscuring the semantic
distinctions carried by functional morphemes (Tyers et al., 2017; Osborne and Gerdes, 2019).
Furthermore, the lack of standardized guidelines for specific agglutinative phenomena has led to inconsisten-
cies across existing treebanks. Variations in annotating complex constructions, such as post-verbal auxiliaries and
pronominalized locatives, hinder the effectiveness of cross-lingual transfer and the development of reliable tools
(Akhundjanova, 2025; Washington et al., 2024). For educational applications, where the goal is to explain why a
sentence is constructed in a certain way, this loss of information is critical. A syntax tree that simplifies a com-
plex postpositional phrase into a generic dependent cannot support a tutoring system intended to diagnose learner
errors within that very phrase. Thus, while UD provides a structural foundation, a more linguistically grounded
annotation scheme is required to meet the precision and interpretability standards of grammar instruction.
2.3
The Gap in ICALL for Low-Resource Languages
Intelligent Computer-Assisted Language Learning (ICALL) systems have demonstrated significant potential in
promoting language internalization by focusing learner attention on linguistic forms (Amaral and Meurers, 2011;
Norris and Ortega, 2000). However, the distribution of these technologies is structurally unbalanced. Advanced
tools capable of deep syntactic analysis are predominantly concentrated in high-resource languages, while low-
resource languages face systematic inequalities in both model performance and application coverage (Weng and
Chiu, 2023; Blasi et al., 2022a; Pakray et al., 2025).
Current applications for under-resourced languages typically rely on shallow processing techniques, such as
vocabulary drills or simple pattern matching. While useful for rote memorization, these methods lack the depth to
explain systematic syntactic errors or provide corrective feedback on complex sentence structures (Bontogon et al.,
2018; Ward et al., 2022). From a pedagogical standpoint, effective grammar learning requires “Focus on Form,"
where learners can perceive the direct mapping between structure and function. Shallow systems that cannot
differentiate argument roles or case functions fail to provide this diagnostic guidance (Ragheb and Dickinson,
2012; Volodina et al., 2014). To bridge this gap, educational technologies must be grounded in deep syntactic
analysis. Dependency parsing offers an ideal mechanism for visualizing abstract grammatical relations, but only
if it is built upon an annotation scheme that accurately reflects the morphosyntactic logic of the target language
(Meurers, 2021; Hellman, 2019).
3
The MUDT Framework: Bridging Theory and Computation
The primary bottleneck in developing intelligent tutoring systems for Uyghur is not merely the scarcity of data,
but the lack of a computational representation that aligns with the linguistic reality faced by learners. Existing
3

--- Page 4 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
universal frameworks, such as Universal Dependencies (UD), often prioritize cross-linguistic consistency over
language-specific precision. While valuable for typology, this approach obscures critical grammatical details
essential for error diagnosis in an educational setting.
Figure 1: Schematic representation of the full-stack research framework. The framework integrates linguistic
theory, resource construction, model training, and educational application through four logical layers. Layer 1
establishes the linguistic foundation by adapting the Universal Dependencies framework to accommodate Uyghur
agglutinative features through the MUDT design. Layer 2 details the treebank construction process using a hybrid
human-AI loop to produce the gold standard corpus. Layer 3 illustrates the computational modeling phase where
various parsers are evaluated to validate the structural fidelity of MUDT. Layer 4 demonstrates the educational
application workflow where the system generates interpretable feedback to enhance learner outcomes.
To address this, we introduce the Modern Uyghur Dependency Treebank (MUDT) framework, the overall
research architecture of which is illustrated in Figure 1. Unlike generic approaches, MUDT is designed with a
pedagogical mandate: the annotation structure must explicitly reflect the morphosyntactic logic that learners are
struggling to master.
3.1
Design Philosophy: Fidelity over Universality
Our design philosophy balances computational feasibility with linguistic fidelity (Volodina et al., 2014; Gerdes
et al., 2018). In an educational context, occasional statistical noise in parsing is tolerable, but a systematic con-
ceptual flaw in the annotation scheme is fatal. If the annotation scheme incorrectly identifies the head of a phrase
(e.g., marking a noun as the head of a postposition), the feedback generated by any downstream AI tool will be
pedagogically misleading (Boulton and Cobb, 2017). Therefore, MUDT deviates from UD guidelines specifically
where the universal standard fails to capture the agglutinative and head-final nature of Uyghur (Blasi et al., 2022b;
Tyers et al., 2017).
3.2
Morphological Layer: The Foundation of Syntax
Uyghur morphology is the gateway to its syntax (Gulinigeer et al., 2021). A single word form often encodes
information that would require a full phrase in English (e.g., kel-El-mi-gEn-lik-im-din means “because of my
inability to come”).
4

--- Page 5 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
To support granular feedback, MUDT adopts a four-layer morphological decomposition: (1) Surface Form, (2)
Lemma, (3) Morpheme Segmentation, and (4) Morphosyntactic Feature Bundle (FEATS). This layered approach
ensures that the parser can “see” the internal structure of words, which is a prerequisite for identifying errors in
suffix usage—a common stumbling block for learners (Senel et al., 2024).
3.3
Modeling Key Pedagogical Phenomena
The divergence of MUDT from standard UD is most critical in three areas that represent high-frequency error
zones for learners: Zero Copulas, Postpositional Phrases, and Compound Predicates. We summarize these struc-
tural differences in Table 1 and illustrate the structural contrasts in Figure 2.
Table 1: Contrastive Analysis: How MUDT addresses educational blind spots in UD.
Phenomenon
UD Approach (The Problem)
MUDT Approach (The Solu-
tion)
Educational Benefit
Zero Copula
Treats punctuation or the sub-
ject as the root; relation is im-
plicit or lost.
Explicitly marks the nominal
predicate as root and the sub-
ject link as cop:zero.
Enables
system
to
identify
“Noun Sentences" and provide
feedback on missing suffixes.
Postpositions
Noun →Postposition (case).
Noun is the head.
Postposition →Noun (obj).
Postposition is the head.
Reflects the true governing
logic: the postposition deter-
mines the case of the noun.
Compound Predicates
Auxiliary is the root; Lexical
verb is a dependent (advcl).
Lexical Verb is the root;
Auxiliary depends on it (aux).
Focuses analysis on the se-
mantic
core
(action)
rather
than grammatical tense mark-
ers.
3.3.1
Zero Copula Constructions
In Uyghur, the copula is frequently omitted in present tense (e.g., Bu kitab. “This [is] a book"). UD typically
struggles here, often attaching the subject to punctuation or leaving the structure fragmented (Bedir et al., 2021)
(Figure 2a). MUDT introduces the cop:zero relation (Figure 2d). By designating the nominal predicate (kitab)
as the root, we align the tree with the learner’s intuition that “book" is the core information. This allows an AI
tutor to explicitly detect valid verbless sentences.
3.3.2
Postpositional Logic
UD treats postpositions as functional leaves attached to nouns (Figure 2b). However, for a learner, the postposition
ytSyn (for) is the governor that demands a specific case from the noun (Osborne and Gerdes, 2019). MUDT inverts
this to Postposition →Noun (Figure 2e). This structure allows a tutoring system to trace the dependency
path upwards and generate feedback like: “The word ytSyn requires the preceding noun to be in the Nominative
case (Johanson, 2000)."
3.3.3
Compound Predicates: Reconstructing Argument Structure
Uyghur frequently employs the “Converb + Auxiliary" construction to form compound predicates. In the Uni-
versal Dependencies standard, the finite auxiliary is regarded as the root, while the lexical verb carrying the core
semantics is demoted to an adverbial clause modifier (advcl). The most critical issue is that UD typically attaches
the subject directly to the auxiliary, which severs the direct dependency link between the subject and the actual
action (Akhundjanova et al., 2025).
MUDT adopts a different strategy. While we still acknowledge the syntactic centrality of the auxiliary as the
Root, we mark the lexical verb as a direct complement of the auxiliary rather than a clause. More importantly,
5

--- Page 6 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
we attach core arguments such as the subject and object directly under the lexical verb (Semantic Head) rather
than the auxiliary. This “Auxiliary →Lexical Verb →Subject" chain structure successfully distinguishes the
Grammatical Head from the Semantic Head (Ivanova et al., 2012), enabling the pedagogical system to accurately
determine who performed what action rather than simply identifying who completed the grammatical aspect.
Bu kitab .
root
nsubj
parataxis
(a) UD: Zero Copula
Siz ytSyn
root
case
(b) UD: Noun-Head
Yezip boldi
root
advcl
(c) UD: Aux-Head
Bu kitab .
root
cop:zero
punct
(d) MUDT: Explicit Pred.
Siz ytSyn
root
obj
(e) MUDT: Post-Head
Yezip boldi
root
aux
(f) MUDT: Lexical-Head
Figure 2: Structural comparison of three critical linguistic phenomena. The top row (a-c) shows typical UD
structures (often semantically opaque). The bottom row (d-f) shows the proposed MUDT structures designed
for pedagogical clarity. Columns correspond to Zero Copula, Postpositional Phrases, and Compound Predicates
respectively.
The complete inventory of MUDT dependency relations is provided in Appendix A.
4
Treebank Construction and Technical Validation
To address the limitations of existing resources and support the development of intelligent educational applica-
tions, we constructed the Modern Uyghur Dependency Treebank. This section details the construction pipeline,
validates the reliability of the annotation scheme, and empirically demonstrates the superiority of the resulting
resource through intrinsic structural metrics, extrinsic parsing experiments, and qualitative error analysis.
4.1
Data Construction and Annotation Pipeline
To establish a robust foundation for educational applications while ensuring comparability with previous bench-
marks, we utilized the 3,456 sentences from the existing Universal Dependencies UD_Uyghur-UDT treebank (Eli
et al., 2016). This corpus represents standard written Uyghur and captures the core grammatical structures essen-
tial for language learning (Volodina et al., 2014). The construction of the treebank followed a hybrid human-AI
loop designed to balance computational efficiency with linguistic precision. We initially employed the Qwen3-
max Large Language Model via API to generate preliminary annotations based on the MUDT guidelines, but
the output exhibited characteristic low-resource processing errors such as hallucinations and inconsistencies in
fine-grained case marking (Kellert et al., 2025; Ding et al., 2023). Consequently, the pre-annotated data was im-
ported into the Brat annotation platform for a rigorous manual correction phase. A team of six annotators with
advanced degrees in linguistics, who underwent specialized training on the MUDT protocols to ensure conceptual
alignment, conducted a meticulous line-by-line review to resolve structural ambiguities and correct morphological
6

--- Page 7 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
features. The resulting high-quality corpus was subsequently partitioned into a training set of 1,656 sentences, a
development set of 900 sentences, and a test set of 900 sentences for experimental validation.
4.2
Reliability: Inter-Annotator Agreement
To ensure that the MUDT annotation scheme is scientifically reproducible and unambiguous, we conducted an
inter-annotator agreement study prior to the full-scale annotation (Braylan et al., 2022). We randomly sampled
200 sentences from the corpus, and independent linguists annotated them according to the proposed guidelines.
We evaluated agreement using Unlabeled Attachment Score, Labeled Attachment Score, and Cohen’s Kappa
coefficient (Zeman et al., 2018). The results indicated a high level of consensus, with an Unlabeled Attachment
Score of approximately 92.29 percent and a Labeled Attachment Score of 85.45 percent. Furthermore, the Cohen’s
Kappa coefficient for dependency relations reached 0.9890. These metrics confirm that the proposed annotation
scheme is defined with sufficient clarity to allow different human experts to apply it consistently, thereby validating
the reliability of the resulting treebank (Artstein, 2017; Bayerl and Paul, 2011; Warrens, 2015; McHugh, 2012).
4.3
Intrinsic Evaluation: Structural Quality and Linguistic Plausibility
Before training computational models, we performed an intrinsic quality assessment to quantify the structural
improvements of MUDT compared to the original UD standard (Yadav et al., 2021b). We hypothesize that a
linguistically grounded annotation should naturally result in a simpler, more projective graph structure that aligns
with the cognitive processing of the language (Gildea and Temperley, 2010; Yadav et al., 2022). Using identical
dataset splits, we compared the two treebanks across metrics including average dependency distance, crossing arc
ratios, and the explicit coverage of linguistic phenomena.
The evaluation results, presented in Table 2, indicate that MUDT achieves a fundamental structural opti-
mization. Most notably, the proportion of crossing arcs (non-projective dependencies) decreased drastically from
7.35% in the UD corpus to a negligible 0.06% in MUDT. From a linguistic perspective, this reduction is not
accidental but stems from resolving the conflict between Uyghur’s strict head-final typology and UD’s content-
head principle. In UD, attaching postpositions or auxiliary verbs as dependents to preceding nouns or verbs often
creates “back-and-forth” arcs that cross over other modifiers, artificially inflating syntactic complexity. MUDT
restores the linear projectivity of the dependency tree by re-assigning functional morphemes (postpositions and
light verbs) as syntactic heads, consistent with their roles as case-assigners and mood-markers.
Furthermore, the average dependency distance was reduced from 2.643 to 2.359. In dependency grammar
theory, shorter dependency distances correlate with lower cognitive load and higher parsing accuracy (Temperley,
2007; Temperley and Gildea, 2018). This reduction suggests that the MUDT structure is more local and computa-
tionally tractable, theoretically reducing the error propagation in downstream parsing models by keeping related
elements closer in the structural hierarchy.
Table 2: Comparison of Structural Quality Metrics between UDT and MUDT
Split
DepDist
Crossing%
Roots!=1%
Cycles%
InvalidHD%
DEV
2.64 →2.38
8.00 →0.11
0.00 →0.22
0.00 →0.67
0.00 →0.56
TEST
2.69 →2.37
8.67 →0.00
0.00 →0.00
0.00 →0.00
0.00 →0.00
TRAIN
2.62 →2.34
6.28 →0.06
0.00 →0.00
0.00 →0.00
0.00 →0.00
TOTAL
2.64 →2.36
7.35 →0.06
0.00 →0.06
0.00 →0.17
0.00 →0.14
Regarding the representation of specific linguistic phenomena, MUDT provides systematic annotation for
zero copula constructions. As shown in Table 3, we identified and labeled 142 instances of the zero copula
relation, whereas the UD corpus contained zero instances of this label. This explicit modeling provides necessary
supervision signals for educational applications that need to detect valid verbless sentences. Additionally, the
7

--- Page 8 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
cleaning process successfully eliminated structural violations such as multiple roots and cyclic dependencies in
the training and test sets, ensuring a normative standard for computational processing.
Table 3: Feature Coverage and Phenomenon Explicitation (UDT vs MUDT)
Split
FEATS Coverage %
FEATS Mean Count
cop:zero Count
DEV
44.19 / 44.20
0.975 / 0.975
0 / 57
TEST
45.02 / 45.02
1.032 / 1.032
0 / 22
TRAIN
46.04 / 46.04
1.019 / 1.019
0 / 63
TOTAL
45.29 / 45.29
1.010 / 1.010
0 / 142
4.4
Extrinsic Evaluation: Parser Performance and Generalization
To empirically verify the computational advantages of the framework, we conducted comparative parsing ex-
periments using three distinct parsers. We selected the transition-based UDPipe and the graph-based Stanza as
representative mainstream tools to demonstrate that the performance improvements of MUDT are robust across
widely used architectures. This comparison confirms the generalizability of the proposed framework over the
Universal Dependencies standard (Qi et al., 2020; Straka, 2018; Straka and Straková, 2020). Furthermore, we em-
ployed DiaParser as a state-of-the-art baseline to investigate the performance upper bound (Dozat and Manning,
2017; Glavaš and Vuli´c, 2021). Utilizing Deep Biaffine Attention, DiaParser achieved a UAS of 0.8050 and a LAS
of 0.6675, outperforming the best UDPipe baseline by margins of 7.09% and 14.05% respectively. These results
suggest that the graph-based Biaffine mechanism is particularly well-suited for modeling the long-distance depen-
dencies inherent in Uyghur’s head-final structure, offering improved resolution over transition-based approaches.
We subsequently evaluated performance in both in-domain and cross-domain settings to test learnability and gen-
eralization.
In the in-domain evaluation, where models were trained and tested on the same scheme, the MUDT-based
models consistently outperformed the UD-based baselines. As detailed in Table 4, the Stanza model trained on
MUDT achieved an Unlabeled Attachment Score of 0.655, significantly higher than the 0.572 achieved by the
model trained on UD. This performance gap indicates that the more regular and linguistically grounded structures
of MUDT are inherently easier for statistical models to learn.
Table 4: Parser Performance Comparison (UAS / LAS)
Model
Training / Evaluation Setup
UAS
LAS
UDPipe
Train MUDT / Eval MUDT
0.7341
0.5270
UDPipe
Train UDT / Eval UDT
0.7069
0.5284
UDPipe
Train MUDT / Eval UDT
0.6084
0.2991
UDPipe
Train UDT / Eval MUDT
0.6373
0.3252
Stanza
Train MUDT / Eval MUDT
0.6554
0.2607
Stanza
Train UDT / Eval UDT
0.5722
0.2534
Stanza
Train MUDT / Eval UDT
0.5198
0.1958
Stanza
Train UDT / Eval MUDT
0.5237
0.1585
DiaParser
Train MUDT / Eval MUDT
0.8050
0.6675
We further analyzed the asymmetric compatibility between the two schemes. When the model trained on
MUDT was applied to UD data, it maintained a relatively stable structural prediction capability. Conversely,
when the model trained on UD was applied to MUDT data, performance degraded sharply, with the Labeled
Attachment Score dropping to as low as 0.158 in the Stanza experiment. This asymmetry suggests that MUDT
functions as a superset of linguistic knowledge, containing fine-grained syntactic information that the UD model
8

--- Page 9 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
never encountered and therefore cannot predict. This confirms that MUDT captures essential grammatical nuances
required for advanced analysis while maintaining backward compatibility with the core structure of the language.
4.5
Qualitative Analysis of Divergence
To identify the source of the quantitative performance differences, we analyzed the specific structural divergences
between the UD baseline and the MUDT framework. The analysis reveals that the core difference lies in the
prioritization of semantic fidelity over formal universality.
Figure 3 illustrates a critical divergence in handling postpositional phrases. The UD-style analysis often inverts
the logical relationship to maintain direct arcs, attaching the postposition to the noun. In contrast, MUDT correctly
models the postposition as the functional head governing the noun object. This structural clarity allows the MUDT
parser to produce logically consistent modification chains, which is essential for error diagnosis in educational
settings.
Figure 3: Structural Comparison. (a) UDT-style analysis where the postposition incorrectly depends on the noun.
(b) MUDT analysis correctly modeling the postposition as the head.
NurGun
jillar
ilgiri
bu
jEr
byk-baraqsan
dErExlEr
bilEn
qaplanGan
quruqluq
ikEn
nummod
nmod
advmod
det
nmod
amod
obl
case
amod
nsubj
root
(a) UDT-style analysis
NurGun
jillar
ilgiri
bu
jEr
byk-baraqsan
dErExlEr
bilEn
qaplanGan
quruqluq
ikEn
nummod
obj
det
nsubj
amod
obj
instr:post
amod
post
cop
root
(b) MUDT analysis
Further qualitative examination, detailed in Table 5, highlights how MUDT explicitly captures phenomena that
are often collapsed in the UD standard. For instance, compound predicates are analyzed by identifying the lexical
verb as the root rather than the auxiliary, and distinct case relations such as the dative are explicitly labeled rather
than being grouped under generic oblique labels. These fine-grained distinctions are what enable the superior
performance of the MUDT-trained parsers and provide the necessary granularity for downstream pedagogical
feedback.
9

--- Page 10 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Table 5: Qualitative Comparison of Analyses for Key Divergent Phenomena
Uyghur Sentence
English Translation
UDT-style Analysis
MUDT Analysis (Gold)
Qajsar
geologniŋ
kørsεtkεn-
liriɣa qarap...
Looking at what the geologist
pointed to...
Label: obl
Arc: kørsεtkεnlirigε ←qarap
Label: case:dat
Arc: kørsεtkεnlirigε ←qarap
Mεn hεrgiz saqlap turalma-
jmεn!
I absolutely cannot wait any
longer!
Label: advcl
Arc: saqlap ←turalmiɣidεkmεn
Label: aux
Arc: saqlap ←turalmiɣidεkmεn
Sεn... sεwr qilip turalamsεn?
Can you wait patiently...?
Label: compound
Arc: sεwr ←qilip
Label: fixed
Arc: sεwr ←qilip
Buni... bildiŋiz? dεp soridi...
“How did you know this?”
...asked.
Label: advcl
Arc: bildiŋiz ←soridi
Label: obj
Arc: bildiŋiz ←dεp
...dεrεxlεr bilεn qaplanɣan...
...covered with trees...
Label: nmod (Logically inverted)
Arc: bilεn ←dεrεxlεr
Labels: obj and instr:post
Arcs: dεrεxlεr ←bilεn; bilεn ←
planɣan
5
Pedagogical Application: AI-Assisted Grammar Tutoring
The ultimate objective of refining the syntactic representation of Uyghur is to facilitate more effective language
acquisition. To demonstrate the practical utility of the MUDT framework, we developed an AI-assisted grammar
tutoring system and evaluated its effectiveness through a controlled classroom experiment. This section details the
system design, the experimental methodology involving L2 learners, and the empirical results regarding learning
gains.
5.1
System Design: From Parsing to Feedback
The MUDT-Tutor application functions as a comprehensive interactive learning environment rather than a static
parser. The operational workflow of the system is depicted in Figure 4. The user interface comprises an exercise
display area, a student input field, and an intelligent feedback panel. To evaluate morphosyntactic mastery, the
system utilizes a sentence correction format. Learners are presented with a Uyghur sentence containing specific
grammatical errors such as incorrect case marking or missing zero copula links. The students then type the
corrected version into the input field and initiate the analysis by clicking the submit button.
The submission of an answer triggers a backend pipeline consisting of parsing and diagnosis. The integrated
MUDT parser performs real-time syntactic analysis on the input to generate a dependency tree. Subsequently,
a rule engine compares this structure against a gold standard tree or a set of predefined error patterns. The
primary advantage of this approach lies in the decision authority of the parser. Instead of relying on simple
string matching, the system verifies the validity of syntactic relations. For instance, if a student corrects a spelling
error but maintains an incorrect dependency between a postposition and its governor, the resulting tree reveals
this deep structural flaw. The feedback panel then provides specific structural guidance such as instructions to
re-examine the governing object of the postposition instead of showing a generic error message.
The necessity of the MUDT framework becomes evident when considering specific feedback scenarios. For
instance, in zero copula sentences, a standard Universal Dependencies parser typically fails to identify the predica-
tive relationship or attaches the subject to punctuation, rendering the structure opaque to the feedback algorithm.
In contrast, the MUDT parser explicitly identifies the cop:zero relation. When the system detects a learner
attempting a nominal predicate sentence, it can verify if the subject and predicate are correctly linked and provide
positive reinforcement regarding the verbless structure. This allows the system to generate precise hints such as
identifying the postposition as the core of the phrase, a level of diagnostic clarity that would be impossible with
the generic oblique labels found in previous frameworks.
10

--- Page 11 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Figure 4: Operational flowchart of the syntactic diagnosis and explainable feedback mechanism in MUDT-Tutor.
The process is illustrated using a postposition correction task. (a) The Learner Input Interface presents the front-
end interaction where students submit corrections for ungrammatical sentences. (b) The Syntax-Aware Diagnosis
module performs parallel parsing of the input pair to extract dependency relations and verify structural validity
against the rule engine. (c) The Intelligent Scaffolding Feedback stage generates a dynamic response panel dis-
playing the correctness verdict, standard solution, error classification, and specific pedagogical guidance based on
the underlying syntactic analysis.
5.2
Experimental Design
To empirically validate the educational impact of the system, we employed a quasi-experimental pre-test and post-
test design. The study participants were 35 first-year undergraduate students majoring in Uyghur language at a
university in China. All participants were native Chinese speakers who had begun their study of Uyghur three
months prior to the experiment, placing them at a novice proficiency level where explicit grammar instruction is
most critical.
The experiment followed a four-day procedure designed to isolate the effect of intelligent feedback. On the
first day, all participants completed a paper-based pre-test to establish a baseline of their grammatical competence
regarding specific target structures, including case marking and complex predicates. Following the pre-test, par-
ticipants were randomly assigned to two groups: an experimental group (n=17) and a control group (n=18). On
the second day, both groups completed an identical digital exercise consisting of 20 sentence correction tasks. The
experimental condition involved the use of the MUDT-Tutor interface, which provided immediate, linguistically
grounded feedback upon error submission. This allowed students to engage in a cycle of hypothesis testing and re-
vision. The control condition involved a text-only interface where students completed the same tasks but received
no immediate system feedback. To differentiate between short-term memory retention and genuine learning, a
cooling-off period was observed on the third day. Finally, on the fourth day, a post-test was administered to mea-
sure learning gains. The assessment items on the pre-test and post-test were structurally equivalent but utilized
different lexical items to ensure the measurement of grammatical transfer rather than rote memorization (Zhai
et al., 2021; Alharbi, 2023).
11

--- Page 12 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
5.3
Results and Analysis
The quantitative analysis focused on the learning gains, defined as the difference between post-test and pre-test
scores. To ensure data quality, we performed a data cleaning process excluding participants who exhibited ab-
normal score regression (post-test score decreasing by more than 5 points compared to pre-test), resulting in a
final sample of N = 15 for the experimental group and N = 16 for the control group. Descriptive statistics indi-
cated a substantial difference in growth magnitude. The control group improved their average score from 60.75
(SD = 21.97) to 68.62 (SD = 23.76), resulting in a mean learning gain of 7.88. In contrast, the experimental
group utilizing the MUDT-Tutor improved from a baseline of 57.87 (SD = 20.77) to a post-test average of 71.60
(SD = 20.24), achieving a significantly higher mean learning gain of 13.73.
Table 6: Comparison of Learning Outcomes between Experimental and Control Groups (Post-cleaning)
Pre-test Mean
Post-test Mean
Group
N
Mean
SD
Mean
SD
Mean Gain
Experimental (MUDT-Tutor)
15
57.87
20.77
71.60
20.24
13.73
Control (No Feedback)
16
60.75
21.97
68.62
23.76
7.88
Note: Significant difference observed: t(29) = 2.51, p = 0.018,d = 0.90.
The data presented in Table 6 demonstrates that the provision of syntax-aware feedback resulted in superior
learning outcomes. To verify the statistical significance, we conducted an independent samples t-test on the
learning gains. The analysis revealed a significant difference between the two groups (t(29) = 2.51, p = 0.018).
Furthermore, the effect size was calculated as Cohen’s d = 0.90, indicating a large effect. These results confirm
that the interpretability of the feedback significantly helped students successfully restructure their interlanguage
knowledge compared to the control condition.
Beyond aggregate scores, an analysis of individual ranking changes revealed a positive shift in the relative
performance of students in the experimental group. Several students who ranked in the lower quartile during the
pre-test exhibited marked improvements in their class ranking during the post-test. For example, students who
initially scored below 40 points in the experimental group showed an average improvement that exceeded the
class average, suggesting that explicit structural cues are particularly beneficial for struggling learners who may
lack the intuition to self-correct. These findings indicate that the linguistic precision of the MUDT framework
does not merely serve theoretical completeness but translates directly into measurable pedagogical effectiveness,
validating the necessity of linguistically grounded computational resources for low-resource language education.
6
Discussion
The results presented in this study highlight the critical link between the quality of computational resources and
the effectiveness of educational technology for low-resource languages. Our findings suggest that the misalign-
ment between generic annotation frameworks and the specific agglutinative characteristics of Uyghur constitutes
a significant obstacle to developing reliable learning tools. By restructuring the dependency annotation scheme to
better align with the internal logic of the language, we observed consistent improvements spanning from intrinsic
structural clarity to pedagogical utility.
Intrinsic evaluation of the Modern Uyghur Dependency Treebank suggests that the proposed framework effec-
tively mitigates the structural ambiguities often encountered when applying universal standards to Uyghur syntax.
The substantial reduction in crossing arcs indicates that the new scheme aligns more closely with the projectivity
principle inherent in the language. This structural consistency appears to facilitate a more straightforward model-
ing of head-final dependencies. By explicitly annotating the internal structure of compound predicates and post-
positional phrases, the framework offers a more transparent hierarchy for these syntactic clusters. Furthermore,
12

--- Page 13 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
the systematic annotation of zero copula constructions provides a clearer representation of nominal sentences,
addressing the difficulty previous frameworks faced in assigning valid roots to such structures (Tyers et al., 2017;
Sulubacak et al., 2016; Türk et al., 2019).
These structural adjustments appear to contribute to improved computational performance. Parsing experi-
ments indicated that models trained on the linguistically grounded scheme generally outperformed those trained
on the universal standard, particularly within complex graph-based architectures. The asymmetry observed in
cross-domain tasks suggests that the Modern Uyghur Dependency Treebank may function as a superset of linguis-
tic knowledge, capturing fine-grained morphosyntactic distinctions that are often abstracted in broader universal
standards. This implies that preserving these granular details is beneficial for statistical models, as it allows for
advanced analysis while retaining the capability to process simpler structures. This observation aligns with prior
research demonstrating that preserving fine-grained morphological information enhances syntactic parsing per-
formance, particularly for morphologically rich and agglutinative languages (Seeker and Kuhn, 2013; Park et al.,
2025). Furthermore, studies have shown that the choice of segmentation granularity is critical for optimizing
performance across various NLP tasks (Park, 2025), suggesting that retaining morphological complexity aids in
capturing necessary syntactic dependencies.
The practical relevance of this computational precision was further supported by the pedagogical experiment.
The difference in learning gains between the experimental and control groups suggests a correlation between the
precision of syntactic analysis and the efficacy of grammar instruction. Students utilizing the intelligent tutoring
system demonstrated higher learning outcomes compared to peers who practiced without feedback. This obser-
vation indicates that for novice learners, the value of an educational tool is closely tied to the interpretability of
its guidance (Heift, 2022; Son et al., 2025; Katinskaia, 2025). While generic error detection provides a useful
baseline, its utility may be constrained when it cannot precisely differentiate between functional roles in complex
sentences. The ability of our system to provide specific structural diagnoses appeared to help learners test their
hypotheses and refine their interlanguage knowledge more effectively.
Beyond technical metrics, this study highlights broader implications for educational equity.
Learners of
low-resource languages often face challenges accessing the adaptive scaffolding available for dominant lan-
guages (Joshi et al., 2020; Pakray et al., 2025; Litman, 2016). By striving to align computational models with
the cognitive processing of the learner, specifically by clarifying how functional morphemes govern arguments,
the system serves as a supportive cognitive scaffold. This approach may help reduce the difficulty associated with
complex agglutinative morphology and encourage novice students to engage with the language more confidently.
The outcomes of this study suggest that bridging theoretical linguistics with engineering is a viable pathway for
enhancing language education, ensuring that technological tools are better adapted to the specific needs of diverse
learner communities.
7
Conclusion
By addressing the structural limitations of universal annotation standards, this study establishes a full-stack
methodology that bridges theoretical linguistics with practical educational technology for Uyghur. The construc-
tion and evaluation of the Modern Uyghur Dependency Treebank demonstrate that prioritizing linguistic fidelity
over typological universality yields a representation that is structurally more coherent and pedagogically trans-
formative. Beyond computational metrics, the true value of this resource lies in its capacity to explicate abstract
grammatical relations for the learner. For educators, it provides a reliable auxiliary for error analysis, while for
students, it offers a personalized guide through complex morphological structures. These findings confirm that
effective intelligent tutoring for low-resource languages relies on computational resources that respect the specific
logic of the target language, thereby supporting the preservation and acquisition of the Uyghur language in the
digital age.
13

--- Page 14 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Ethics declarations
Competing interests
The authors declare no competing interests.
Ethical approval
It will be updated after the article is accepted.
Informed consent
Written informed consent was obtained from all participants prior to data collection, which took place from De-
cember 15 to December 18, 2025. All participants were fully informed of the study’s objectives and anonymity
measures, and participation was entirely voluntary.
Data and code availability
The Modern Uyghur Dependency Treebank (MUDT) and the source code for the experiment are available at
https://github.com/wyqmath/MUDT.
Funding
This study was supported by the Xinjiang Social Science Foundation Project “Research on the Creative Transfor-
mation and Innovative Development of Outstanding Ethnic Minority Cultures in Xinjiang” (Grant No. 2025BYY142).
Author Contributions
Jiaxin Zuo: Conceptualization, Methodology, Data curation, Formal analysis, Software, Visualization, Writing –
original draft, Writing – review & editing.
Yiquan Wang: Software, Visualization, Writing – original draft, Writing – review & editing.
Yuan Pan: Software, Writing – original draft, Writing – review & editing.
Xiadiya Yibulayin: Supervision, Project administration, Resources, Funding acquisition, Writing – review &
editing.
References
Akhundjanova, A. (2025). Harmonizing annotation of turkic postverbial constructions: A comparative study of
UD treebanks. In Proceedings of the 18th Workshop on Building and Using Comparable Corpora (BUCC),
pages 10–17. Association for Computational Linguistics.
Akhundjanova, A., Akkurt, F., Chontaeva, B., Eslami, S., and Çöltekin, Ç. (2025). Parallel universal dependencies
treebanks for turkic languages. In Proceedings of the Eighth Workshop on Universal Dependencies (UDW,
SyntaxFest 2025), pages 129–136.
Alharbi, W. (2023). Ai in the foreign language classroom: A pedagogical overview of automated writing assistance
tools. Education Research International, 2023(1):4253331.
Alizadeh, M., Kubli, M., Samei, Z., Dehghani, S., Bermeo, J. D., Korobeynikova, M., and Gilardi, F. (2023).
Open-source large language models outperform crowd workers and approach chatgpt in text-annotation tasks.
arXiv preprint arXiv:2307.02179, page 101.
14

--- Page 15 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Amaral, L. and Meurers, D. (2011). On using intelligent computer-assisted language learning in real-life foreign
language teaching and learning. ReCALL, 23(1):4–24.
Arnett, C. and Bergen, B. (2025). Why do language models perform worse for morphologically complex lan-
guages? In Proceedings of the 31st International Conference on Computational Linguistics, pages 6607–6623.
Artstein, R. (2017). Inter-annotator agreement. In Handbook of linguistic annotation, pages 297–313. Springer
Netherlands, Dordrecht.
Bayerl, P. S. and Paul, K. I. (2011). What determines inter-coder agreement in manual annotations? a meta-
analytic investigation. Computational Linguistics, 37(4):699–725.
Bedir, T., ¸Sahin, K., Güngör, O., Üsküdarlı, S., Özgür, A., Güngör, T., and Ba¸saran, B. Ö. (2021). Overcoming
the challenges in morphological annotation of turkish in universal dependencies framework. In Proceedings
of The Joint 15th Linguistic Annotation Workshop (LAW) and 3rd Designing Meaning Representations (DMR)
Workshop, pages 112–122.
Bender, E. M., Gebru, T., McMillan-Major, A., and Shmitchell, S. (2021). On the dangers of stochastic parrots:
Can language models be too big? In Proceedings of the 2021 ACM conference on fairness, accountability, and
transparency, pages 610–623.
Blasi, D., Anastasopoulos, A., and Neubig, G. (2022a). Systematic inequalities in language technology perfor-
mance across the world’s languages. In Proceedings of the 60th Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages 5486–5505. Association for Computational Linguistics.
Blasi, D. E., Henrich, J., Adamou, E., Kemmerer, D., and Majid, A. (2022b). Over-reliance on English hinders
cognitive science. Trends in cognitive sciences, 26(12):1153–1170.
Bontogon, M., Arppe, A., Antonsen, L., Thunder, D., and Lachler, J. (2018). Intelligent computer assisted lan-
guage learning (ICALL) for nêhiyawêwin: An in-depth user-experience evaluation. The Canadian Modern
Language Review, 74(3):337–362.
Boulton, A. and Cobb, T. (2017).
Corpus use in language learning: A meta-analysis.
Language learning,
67(2):348–393.
Braylan, A., Alonso, O., and Lease, M. (2022). Measuring annotator agreement generally across complex struc-
tured, multi-object, and free-text annotation tasks. In Proceedings of the ACM Web Conference 2022, pages
1720–1730.
Croft, W., Nordquist, D., Looney, K., and Reagan, M. (2017). Linguistic typology meets universal dependencies.
In Proceedings of the 16th International Workshop on Treebanks and Linguistic Theories (TLT16), pages 63–75.
Dada, S., Flores, C., Bastable, K., Tönsing, K., Samuels, A., Mukhopadhyay, S., others, and Moore, R. (2024). Use
of an intelligent tutoring system for a curriculum on augmentative and alternative communication: Feasibility
for implementation. International Journal of Language & Communication Disorders, 59(6):2279–2293.
Dash, N. S. (2024). Corpus linguistics and language technology. In Routledge Encyclopedia of Technology and
the Humanities, pages 219–246. Routledge.
de Marneffe, M.-C., Manning, C. D., Nivre, J., and Zeman, D. (2021). Universal dependencies. Computational
Linguistics, 47(2):255–308.
Ding, B., Qin, C., Liu, L., Chia, Y. K., Li, B., Joty, S., and Bing, L. (2023). Is gpt-3 a good data annotator?
In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 11173–11195.
15

--- Page 16 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Dozat, T. and Manning, C. D. (2017). Deep biaffine attention for neural dependency parsing. In International
Conference on Learning Representations.
Eli, M., Mushajiang, W., Yibulayin, T., Abiderexiti, K., and Liu, Y. (2016).
Universal dependencies for
uyghur. In Proceedings of the Third International Workshop on Worldwide Language Service Infrastructure
and Second Workshop on Open Infrastructures and Analysis Frameworks for Human Language Technologies
(WLSI/OIAF4HLT2016), pages 44–50.
Eryi˘git, G., Nivre, J., and Oflazer, K. (2008).
Dependency parsing of turkish.
Computational Linguistics,
34(3):357–389.
Futrell, R., Mahowald, K., and Gibson, E. (2015). Large-scale evidence of dependency length minimization in 37
languages. Proceedings of the National Academy of Sciences, 112(33):10336–10341.
Gerdes, K., Guillaume, B., Kahane, S., and Perrier, G. (2018). SUD or Surface-Syntactic Universal Dependencies:
An annotation scheme near-isomorphic to UD. In Universal dependencies workshop 2018.
Gilardi, F., Alizadeh, M., and Kubli, M. (2023). Chatgpt outperforms crowd workers for text-annotation tasks.
Proceedings of the National Academy of Sciences, 120(30):e2305016120.
Gildea, D. and Temperley, D. (2010). Do grammars minimize dependency length? Cognitive Science, 34(2):286–
310.
Glavaš, G. and Vuli´c, I. (2021). Is supervised syntactic parsing beneficial for language understanding tasks? an
empirical investigation. In Proceedings of the 16th Conference of the European Chapter of the Association for
Computational Linguistics: Main Volume, pages 3090–3104.
Gulinigeer, A., Kahaerjiang, A., Jiamila, W., Yunfei, S., Turenisha, M., and Tuergen, Y. (2021). Morphological
analysis corpus construction of uyghur. In Proceedings of the 20th Chinese National Conference on Computa-
tional Linguistics, pages 1076–1086.
Hedderich, M. A., Lange, L., Adel, H., Strötgen, J., and Klakow, D. (2021). A survey on recent approaches for
natural language processing in low-resource scenarios. In Proceedings of the 2021 Conference of the North
American Chapter of the Association for Computational Linguistics: Human Language Technologies, pages
2545–2568.
Heift, T. (2022). Intelligent computer assisted language learning. In Research Questions in Language Education
and Applied Linguistics: A Reference Guide, pages 655–658. Springer International Publishing, Cham.
Hellman, A. B. (2019). Visualizing the structure of language: Dependency grammar for language teaching.
Springer.
Ivanova, A., Oepen, S., Øvrelid, L., and Flickinger, D. (2012). Who did what to whom? a contrastive study of
syntacto-semantic dependencies. In Proceedings of the sixth linguistic annotation workshop, pages 2–11.
Johanson, L. (2000). Turkic indirectives. Empirical approaches to language typology, pages 61–88.
Joshi, P., Santy, S., Budhiraja, A., Bali, K., and Choudhury, M. (2020). The state and fate of linguistic diversity
and inclusion in the nlp world. arXiv preprint arXiv:2004.09095.
Katinskaia, A. (2025). An overview of artificial intelligence in computer-assisted language learning. arXiv preprint
arXiv:2505.02032.
Kellert, O., Tyagi, N., Imran, M., Licona-Guevara, N., and Gómez-Rodríguez, C. (2025). Parsing the switch: Llm-
based ud annotation for complex code-switched and low-resource languages. arXiv preprint arXiv:2506.07274.
16

--- Page 17 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Litman, D. (2016). Natural language processing for enhancing teaching and learning. In Proceedings of the AAAI
conference on artificial intelligence, volume 30.
Little, D. (2001). Learner autonomy and the challenge of tandem language learning via the internet. ICT and
language learning: A European perspective, pages 29–38.
McHugh, M. L. (2012). Interrater reliability: the kappa statistic. Biochemia medica, 22(3):276–282.
Meurers, D. (2021). Natural language processing and language learning. In Chapelle, C. A., editor, The Encyclo-
pedia of Applied Linguistics, pages 1–16. Wiley.
Mukherjee, J. (2006). Corpus linguistics and language pedagogy: The state of the art–and beyond. Corpus
technology and language pedagogy: New resources, new tools, new methods, pages 5–24.
Nivre, J. (2016). Universal dependencies: A cross-linguistic perspective on grammar and lexicon. In Proceedings
of the Workshop on Grammar and Lexicon: Interactions and Interfaces (GramLex), pages 38–40. The COLING
2016 Organizing Committee.
Nivre, J., De Marneffe, M. C., Ginter, F., Hajic, J., Manning, C. D., Pyysalo, S., others, and Zeman, D. (2020).
Universal dependencies v2: An evergrowing multilingual treebank collection. In Proceedings of the twelfth
language resources and evaluation conference, pages 4034–4043.
Norris, J. M. and Ortega, L. (2000). Effectiveness of L2 instruction: A research synthesis and quantitative meta-
analysis. Language Learning, 50(3):417–528.
Osborne, T. and Gerdes, K. (2019). The status of function words in dependency grammar: A critique of universal
dependencies (UD). Glossa: a journal of general linguistics, 4(1):17.
Pakray, P., Gelbukh, A., and Bandyopadhyay, S. (2025). Natural language processing applications for low-resource
languages. Natural Language Processing, 31(2):183–197.
Park, J. (2025). Foundations and evaluations in nlp. arXiv preprint arXiv:2504.01342.
Park, J., Chen, Y., Kim, K., Lim, K., and Park, C. (2025). Enhancing korean dependency parsing with morphosyn-
tactic features. arXiv preprint arXiv:2503.21029.
Qi, P., Zhang, Y., Zhang, Y., Bolton, J., and Manning, C. D. (2020). Stanza: A python natural language processing
toolkit for many human languages. arXiv preprint arXiv:2003.07082.
Ragheb, M. and Dickinson, M. (2012). Defining syntax for learner language annotation. In Proceedings of
COLING 2012: Posters, pages 965–974. The COLING 2012 Organizing Committee.
Seddah, D., Tsarfaty, R., Kübler, S., Candito, M., Choi, J. D., Farkas, R., Foster, J., others, and Vincze, V. (2013).
Overview of the SPMRL 2013 shared task: A cross-framework evaluation of parsing morphologically rich
languages. In Proceedings of the Fourth Workshop on Statistical Parsing of Morphologically-Rich Languages,
pages 146–182. Association for Computational Linguistics.
Seeker, W. and Kuhn, J. (2013). Morphological and syntactic case in statistical dependency parsing. Computa-
tional Linguistics, 39(1):23–55.
Senel, L. K., Ebing, B., Baghirova, K., Schuetze, H., and Glavaš, G. (2024).
Karde¸s-nlu: Transfer to low-
resource languages with the help of a high-resource cousin–a benchmark and evaluation for turkic languages. In
Proceedings of the 18th Conference of the European Chapter of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 1672–1688.
17

--- Page 18 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Settles, B., T. LaFlair, G., and Hagiwara, M. (2020). Machine learning–driven language assessment. Transactions
of the Association for computational Linguistics, 8:247–263.
Son, J. B., Ruži´c, N. K., and Philpott, A. (2025). Artificial intelligence technologies and applications for language
learning and teaching. Journal of China Computer-Assisted Language Learning, 5(1):94–112.
Straka, M. (2018). Udpipe 2.0 prototype at conll 2018 ud shared task. In Proceedings of the CoNLL 2018 shared
task: Multilingual parsing from raw text to universal dependencies, pages 197–207.
Straka, M. and Straková, J. (2020). Udpipe at evalatin 2020: Contextualized embeddings and treebank embed-
dings. arXiv preprint arXiv:2006.03687.
Sulubacak, U., Gökırmak, M., Tyers, F., Çöltekin, Ç., Nivre, J., and Eryi˘git, G. (2016). Universal dependencies for
Turkish. In Proceedings of COLING 2016, the 26th International Conference on Computational Linguistics:
Technical Papers, pages 3444–3454.
Taguchi, C., Iwata, S., and Watanabe, T. (2022). Universal dependencies treebank for tatar: Incorporating intra-
word code-switching information. In Proceedings of the Workshop on Resources and Technologies for In-
digenous, Endangered and Lesser-resourced Languages in Eurasia within the 13th Language Resources and
Evaluation Conference, pages 95–104.
Temperley, D. (2007). Minimization of dependency length in written english. Cognition, 105(2):300–333.
Temperley, D. and Gildea, D. (2018). Minimizing syntactic dependency lengths: Typological/cognitive universal?
Annual Review of Linguistics, 4(1):67–80.
Tömür, K. and Lee, A. (2003). Modern Uyghur grammar (morphology). Yıldız.
Tsarfaty, R., Seddah, D., Goldberg, Y., Kübler, S., Versley, Y., Candito, M., Foster, J., others, and Tounsi, L.
(2010). Statistical parsing of morphologically rich languages (SPMRL) what, how and whither. In Proceedings
of the NAACL HLT 2010 First Workshop on Statistical Parsing of Morphologically-Rich Languages, pages
1–12. Association for Computational Linguistics.
Tsarfaty, R., Seddah, D., Kübler, S., and Nivre, J. (2013). Parsing morphologically rich languages: Introduction
to the special issue. Computational Linguistics, 39(1):15–22.
Türk, U., Atmaca, F., Özate¸s, ¸S. B., Ba¸saran, B. Ö., Güngör, T., and Özgür, A. (2019). Improving the annotations in
the Turkish universal Dependency Treebank. In Proceedings of the Third Workshop on Universal Dependencies
(UDW, SyntaxFest 2019), pages 108–115.
Tusun, A. and Hendriks, H. (2022). Caused motion events in modern uyghur: A typological perspective. Linguis-
tics, 60(5):1663–1705.
Tyers, F. M., Washington, J., Çöltekin, Ç., and Makazhanov, A. (2017). An assessment of universal dependency
annotation guidelines for turkic languages. Tatarstan Academy of Sciences, 10.
Volodina, E., Pilán, I., Rødven Eide, S., and Heidarsson, H. (2014). You get what you annotate: A pedagogically
annotated corpus of coursebooks for swedish as a second language. In Proceedings of the Ninth International
Conference on Language Resources and Evaluation (LREC’14), pages 3944–3951. European Language Re-
sources Association (ELRA).
Ward, M., Xu, L., and Uí Dhonnchadha, E. (2022). How NLP can strengthen digital game-based language learning
resources for less resourced languages. In Proceedings of the 9th Workshop on Games and Natural Language
Processing, pages 40–48. European Language Resources Association.
18

--- Page 19 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Warrens, M. J. (2015). Five ways to look at cohen’s kappa. Journal of Psychology & Psychotherapy, 5.
Washington, J., Çöltekin, Ç., Akkurt, F., Chontaeva, B., Eslami, S., Jumalieva, G., others, and Taguchi, C. (2024).
Strategies for the annotation of pronominalised locatives in turkic universal dependency treebanks. In Pro-
ceedings of the Joint Workshop on Multiword Expressions and Universal Dependencies (MWE-UD) @ LREC-
COLING 2024, pages 207–219. ELRA and ICCL.
Weng, X. and Chiu, T. K. (2023). Instructional design and learning outcomes of intelligent computer assisted
language learning: Systematic review in the field. Computers and Education: Artificial Intelligence, 4:100117.
Yadav, H., Husain, S., and Futrell, R. (2021b). Do dependency lengths explain constraints on crossing dependen-
cies? Linguistics Vanguard, 7(s3):20190070.
Yadav, H., Husain, S., and Futrell, R. (2022). Assessing corpus evidence for formal and psycholinguistic con-
straints on nonprojectivity. Computational Linguistics, 48(2):375–401.
Zeman, D., Hajic, J., Popel, M., Potthast, M., Straka, M., Ginter, F., et al. (2018). Conll 2018 shared task:
Multilingual parsing from raw text to universal dependencies. In Proceedings of the CoNLL 2018 Shared Task:
Multilingual parsing from raw text to universal dependencies, pages 1–21.
Zhai, X., Chu, X., Chai, C. S., Jong, M. S. Y., Istenic, A., Spector, M., and Li, Y. (2021). A review of artificial
intelligence (ai) in education from 2010 to 2020. Complexity, 2021(1):8812542.
A
The Complete MUDT Dependency Relation Inventory
Table 7: Dependency Relations in the Proposed Scheme for Modern Uyghur
Dependency Relation
Tag
Example (Uyghur)
Annotation Example
English Translation
Adverbial Clause
advcl
U kElgEndE, mEn
uni køryp qaldim.
advcl kElgEndE ←køryp
advcl(køryp, kElgEndE)
When he came, I saw him.
Apposition
appos
U oqutquÙi, jEni ustaz.
appos ustaz ←oqutquÙi
appos(oqutquÙi, ustaz)
He is a teacher, that is, a
mentor.
Auxiliary
aux
U oqup boldi.
aux oqup ←boldi
aux(boldi, oqup)
He finished reading.
Causal Relation
case:abl
U jErdin kEldi.
case:abl jErdin ←kEldi
case:abl(kEldi,
jErdin)
He came from that place.
Locative Relation
case:loc
U jErdE olturdi.
case:loc jErdE ←olturdi
case:loc(olturdi,
jErdE)
He sat in that place.
Dative Relation
case:dat
U jErgE kEtti.
case:dat jErgE ←kEtti
case:dat(kEtti, jErgE)
He went to that place.
Possessive Relation
case:poss
Uning kitabi.
case:poss uning ←kitabi
case:poss(kitabi,
uning)
His book.
Coordinating
Con-
junction
cc
U jaki mEn barmaymiz.
cc jaki ←mEn
cc(mEn, jaki)
Either he or I will not go.
Conjunct
conj
MEn alma, anar,
nESpyt jedim.
conj alma←anar←nESpyt
conj(anar, alma)
conj(nESpyt, anar)
I
ate
an
apple,
a
pomegranate, and a pear.
Copula Relation
cop
U jExSi ikEn.
cop jExSi ←ikEn
cop(ikEn, jExSi)
He is good.
Continued on next page
19

--- Page 20 ---

Construction and educational application of a linguistically grounded dependency treebank for Uyghur
Table 7 – continued from previous page
Dependency Relation
Tag
Example (Uyghur)
Annotation Example
English Translation
Zero Copula
cop:zero
U oqutquÙi.
cop:zero u ←oqutquÙi
cop:zero(oqutquÙi, u)
He is a teacher.
Determiner
det
Bu kitab.
det bu ←kitab
det(kitab, bu)
This book.
Discourse Element
discourse
HEE,u, kEldi.
discourse hEE ←kEldi
discourse(kEldi, hEE)
Yes, he came.
Fixed Expression
fixed
Men sizni jaxSi körimEn.
fixed jaxSi←kørimEn
fixed(kørimEn, jaxSi)
I like you.
Instrumental Relation
instr:case=loc
Aptobusda oltur.
instr:case=loc
aptobusda
←oltur
instr:case=loc(oltur,
aptobusda)
Sit on the bus.
instr:case=dat
QolGa eldi.
instr:case=dat
qolGE
←
eldi
instr:case=dat(eldi,
qolGE)
Took it by hand.
instr:case=post
Qol bilen jEziS.
instr:case=post bilen ←
jEziS
instr:case=post(jEziS,
bilen)
Write by hand.
Adverbial Modifier
advmod
U tez kEldi.
advmod tez ←kEldi
advmod(kEldi, tez)
He came quickly.
Adjectival Modifier
amod
JExSi kitab.
amod jExSi ←kitab
amod(kitab, jExSi)
A good book.
Nominal Modifier
nmod
EjnEk istakan.
nmod EjnEk ←istakan
nmod(istakan, EjnEk)
A glass cup.
Nominal Subject
nsubj
Biz kitab oquduq.
nsubj biz ←oquduq
nsubj(oquduq, biz)
We read a book.
Numeric Modifier
nummod
Bir kitab.
nummod bir ←kitab
nummod(kitab, bir)
One book.
Object
obj
Kitabni oquduq.
obj kitabni ←oquduq
obj(oquduq, kitabni)
We read the book.
Postposition
post
U kitab ytSyn kEldi.
post ytSyn ←kEldi
post(kEldi, ytSyn)
He came for the book.
Punctuation
punct
U kEldi.
punct . ←kEldi
punct(kEldi, .)
He came.
Root
root
U kEldi.
root root ←kEldi
root(ROOT, kEldi)
He came.
20

```
