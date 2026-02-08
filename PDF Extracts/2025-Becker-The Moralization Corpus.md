---
title: "2025-Becker-The Moralization Corpus - PDF Extract"
source_pdf: "2025-Becker-The Moralization Corpus.pdf"
pages: 11
extracted_at: "2026-02-07T17:00:46.194259"
---

# PDF Extract: 2025-Becker-The Moralization Corpus

**Source PDF:** 2025-Becker-The Moralization Corpus.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

The Moralization Corpus: Frame-Based Annotation and Analysis of
Moralizing Speech Acts across Diverse Text Genres
Maria Becker, Mirko Sommer, Lars Tapken, Yi Wan Teh, Bruno Brocai
Department of German Linguistics, Heidelberg University
Department of Computational Linguistics, Heidelberg University
{maria.becker, bruno.brocai}@gs.uni-heidelberg.de
{sommer, tapken, teh}@cl.uni-heidelberg.de
Abstract
Moralizations – arguments that invoke moral values to justify demands or positions – are a yet underexplored form of
persuasive communication. We present the Moralization Corpus, a novel multi-genre dataset designed to analyze
how moral values are strategically used in argumentative discourse. Moralizations are pragmatically complex and
often implicit, posing significant challenges for both human annotators and NLP systems. We develop a frame-based
annotation scheme that captures the constitutive elements of moralizations – moral values, demands, and discourse
protagonists – and apply it to a diverse set of German texts, including political debates, news articles, and online
discussions. The corpus enables fine-grained analysis of moralizing language across communicative formats and
domains. We further evaluate several large language models (LLMs) under varied prompting conditions for the task
of moralization detection and moralization component extraction and compare it to human annotations in order to
investigate the challenges of automatic and manual analysis of moralizations. Results show that detailed prompt
instructions has a greater effect than few-shot or explanation-based prompting, and that moralization remains a
highly subjective and context-sensitive task. We release all data, annotation guidelines, and code to foster future
interdisciplinary research on moral discourse and moral reasoning in NLP.
Keywords: moralization, moral values, moral frames, corpus creation, annotation, LLMs, evaluation
1.
Introduction
Recently, an increasing number of studies at the in-
terface of Natural Language Processing (NLP) and
Computational Social Science have addressed the
task of modeling morality in text, reflecting the grow-
ing interest in exploring moral phenomena through
computational means. Most of this work has ei-
ther focused on predicting moral values from text
(e.g., Morteza Dehghani and Gratch (2014); Zhang
and Counts (2016); Diakopoulos et al. (2014)), or
on analyzing moral biases in large language mod-
els (LLMs) (Schramowski et al. (2022); Hendrycks
et al. (2021); Hämmerl et al. (2023); Jiang et al.
(2021); Fraser et al. (2022), among others). How-
ever, the pragmatic patterns of moralizations – that
is, how moral values are strategically used in argu-
mentative contexts to justify demands or stances –
have not yet been systematically modeled in NLP
research.
We understand moralizations as persuasive
strategies in which moral values are invoked to
describe controversial topics and to demand spe-
cific actions or judgments. Three examples appear
in Table 1. In moralizing practices, vocabulary as-
sociated with moral values (e.g., freedom, justice,
security, inequality) serves to reinforce a demand
by linking it to widely shared moral norms (Haidt
et al., 2009; Graham et al., 2013). For instance, in
the sentence We should introduce a refugee cap
in order to ensure the safety of Germans, the term
(1) We should all stop eating meat because it causes
unnecessary suffering to animals.
(2) Women still earn less than men, even though equality
between men and women is enshrined in the Basic Law.
(3) Immigrants are taking jobs from hardworking citizens
and undermining our values.
Table 1:
Examples of moralizations from our
dataset (moral phrases in bold) illustrate how moral
values support explicit (Ex. 1) or implicit (Ex. 2–3)
demands and occur in both populistic (Ex. 3) and
non-populistic (Ex. 1–2) contexts.
safety functions as a moral justification for a politi-
cal demand. As the examples in Table 1 illustrate,
moralizations can take many forms and occur in a
broad range of contexts – political, social, religious,
and even scientific – beyond explicitly populist or
manipulative discourse. That said, our goal is not
to assess moralizations in terms of being “good” or
“bad,” but rather to examine their linguistic realiza-
tion and discourse functions.
While previous computational studies have pri-
marily modeled morality through simplified categor-
ical frameworks (e.g., one moral value per tweet
or sentence), the complexity and heterogeneity of
moralizations as a pragmatic phenomenon call for
a more nuanced and structured approach. In this
paper, we therefore propose a novel annotation
arXiv:2512.15248v1  [cs.CL]  17 Dec 2025

--- Page 2 ---

framework for modeling moralization frames in text,
which captures the interplay between moral val-
ues, demands, and discourse protagonists across
multiple text genres. Annotating moral values and
demands links values to concrete prescriptions,
revealing how moral arguments serve as legitima-
tion strategies. Identifying protagonists as moral
agents, beneficiaries, or culprits uncovers the so-
cial dynamics behind such arguments. Thus, being
able to identify and analyze moralizations in differ-
ent text genres provides a valuable foundation for
interesting research e.g. in linguistics, social and
political sciences.1
Our framework is designed to operationalize mor-
alizations in a way that makes their linguistic and
pragmatic properties empirically accessible. It is
holistic, in that it integrates moral, rhetorical, and
argumentative dimensions within a unified frame
structure; and flexible, in that it can be applied
to various languages, genres, and segment sizes.
The annotation process involves iterative refine-
ment, combining qualitative and quantitative vali-
dation steps to ensure coherence and reliability.
By applying this framework to a German dataset
comprising political debates, media reports, and
online discussions, we show that certain types of
moralizations and discourse roles become ana-
lytically visible only through our multidimensional
annotation. In addition, our annotation studies high-
light the inherent subjectivity of the task, revealing
how differing conceptual understandings of moral-
ization influence annotation consistency. We also
probe several LLMs for their ability to detect moral-
izations automatically, providing both a feasibility
study and a detailed error analysis that sheds light
on which linguistic and contextual factors are deci-
sive for successful moralization detection.
Our contributions are threefold: (1) We pro-
pose a novel, frame-based annotation framework
for moralizations that captures moral values, de-
mands, and protagonists and allows for a fine-
grained analysis of moralizations; (2) We apply
and refine this framework across diverse genres of
German texts, demonstrating its analytical poten-
tial for investigating moral rhetoric and framing, e.g.
in political and social discourse; and (3) We con-
duct and compare several manual annotation and
LLM-based detection experiments together with
extensive evaluations to explore the challenges of
identifying moralizations. All resources developed
in this work – including the annotated dataset, an-
notation manual, and code – are released publicly
1Similar to Rehbein et al. (2025), our focus is not on
aligning LLMs with human values or investigating moral
biases in LLMs, but instead to use NLP approaches to
analyze moralizations in different texts, thereby contribut-
ing to research on value-based reasoning.
to support further research in this area.2 In sum,
our goal is to provide a methodological foundation
for analyzing how moral rhetoric operates across
discourses – a foundation that, we argue, enables
new insights into moral communication that previ-
ous modeling approaches could not reveal.
The remainder of the paper is structured as fol-
lows: §2 provides an overview of prior work on
(computational) modeling of morality. §3 and 4 in-
troduce our annotation framework and dataset. §5
and §6 report our experiments and evaluation for
moralization detection, and §7 discusses implica-
tions and future directions.
2.
Related Work
Morality has been extensively studied both within
NLP and in related disciplines; however, the spe-
cific phenomenon of moralization and its computa-
tional modeling have so far received little attention.
Morality in Computational Social Science.
As
pointed out by Reinig et al. (2024), many ap-
proaches computationally model morality in order
to investigate research questions from the political
or social sciences. These studies predict moral at-
titudes or sentiments from newspaper or social me-
dia text, e.g. on discourses about abortion policies
(Zhang and Counts, 2016), vaccine campaigns (Is-
lam and Goldwasser, 2022) or climate change (Di-
akopoulos et al., 2014). For all studies of morality
in the field of CSS, Twitter is by far the most promi-
nent empirical basis (cf. Reinig et al. 2024). In
contrast, our dataset captures moralizations across
heterogeneous genres and communicative formats,
including more subtle contexts such as non-fiction.
Interdisciplinary Perspectives.
Outside NLP,
moralization has been studied in linguistics (Felder
and Müller, 2022; Becker et al., 2023), communica-
tion studies (Kampf and Katriel, 2016), psychology
(Rhee et al., 2019), and political science (Mooijman
et al., 2018). These works emphasize moralization
as a persuasive strategy – a phenomenon largely
unexplored computationally. Our study addresses
this gap by analyzing the potential of computation-
ally modeling moralizations.
Morality and Argumentation.
We examine
moral values in argumentative contexts. Work at
this intersection (e.g., Kobbe et al., 2020; Kiesel
et al., 2023) shows that moral values contribute to
argumentative quality and persuasion. The goal
of the SemEval shared task ValueEval’23 (Kiesel
2https://anonymous.4open.science/r/
Moralisierungsdetektion

--- Page 3 ---

Figure 1: Fully annotated example of a moralization frame, labeled with the demand, the supporting moral
value and the protagonists (translation from German by the authors).
et al., 2023) is to explore if it is possible to automati-
cally uncover the values on which arguments draw;
and Landowska et al. (2024) label political texts
preannotated for argument structures with moral
foundations in order to explain the strategies in the
use of moral arguments.
Frame-Based Approaches.
Few studies model
morality in relation to entities or events. Roy et al.
(2022, 2021) define morality frames as the moral
foundation(s) invoked by a text, along with the senti-
ment toward mentioned entities. Similarly, Lei et al.
(2024) and Zhang et al. (2024) combine moral foun-
dations with entity and event information in order
to learn morality-relevant text representations. The
approach by Rehbein et al. (2025), most related
to ours, provides fine-grained moral frame anno-
tations including moral frame types, moral founda-
tions, and narrative roles in parliamentary debates.
We extend this line toward broader genres and
pragmatic functions.
3.
Dataset and Annotation
Our dataset of moralizing text passages was cre-
ated in four steps: (1) development of a dictio-
nary of morality-indicating words; (2) retrieval of
text snippets from large corpora and web sources
based on the dictionary entries; (3) creation of an
annotation scheme capturing key components of
moralizations; and (4) a multi-step annotation pro-
cess ensuring data quality.
Dictionary Creation.
To identify moralizing pas-
sages, we developed DIMI, a multilingual dictio-
nary of morality-indicating words. Starting from a
manually curated German seed list of 130 words
(e.g., freedom, fairness, guilt) (Felder and Müller,
2022), we expanded it using co-occurrence pro-
files from the CCDB database (Belica, 2011). After
manual cleaning, the dictionary comprised 3,000
entries, which we automatically translated into En-
glish, French, and Italian and manually verified.3
Data Collection.
Next, we used DIMI to query
large corpora and online sources for text pas-
sages containing at least one dictionary entry. For
3Unlike existing moral dictionaries, our resource in-
cludes not only explicitly moral terms but also contextu-
ally moralizing words such as guise.
each language (German, English, French, Ital-
ian), we retrieved 2,000 five-sentence snippets
from seven genres: letters to the editor, interviews
(both from various newspapers), parliamentary de-
bates (plenary minutes), commentaries (opinion
articles), court reports (newspaper articles about
legal cases), Wikipedia discussions (where users
discuss how to improve an article), and non-fiction
books (on history, parenting, cultural studies, etc.).
The German data were drawn from DEREKO (IDS,
2022), while other languages were collected from
publicly available web texts. Each dataset was split
into training (70%), development (15%), and test
(15%) sets, balanced across genres.
Category Development.
Our annotation cap-
tures three interrelated layers, designed to capture
the key pragmalinguistic features of moralizations
and to enable consistent corpus-based analysis
across different genres and contexts:
(1) Moral values (phrase level), mapped to
the six Moral Foundations CARE/HARM, FAIR-
NESS/CHEATING, LOYALTY/BETRAYAL, AUTHOR-
ITY/SUBVERSION, PURITY/DEGRADATION, and LIB-
ERTY/OPPRESSION according to the Moral Founda-
tions Theory (MFT) (Graham et al., 2009, 2013)4
Multi-label assignments are allowed, and multiple
values in the same instance are annotated sep-
arately; (2) Demands (clause or sentence level),
here annotators mark all explicit demands (e.g.
We should all stop eating meat) in the texts. For
implicit demands, annotators rephrase the claim
in a simple sentence (e.g. Women still earn less
than men is explicated as Women should be paid
equally); and (3) Protagonists (phrase level),
labeled by group type: INDIVIDUALS (e.g.
An-
gela Merkel), GENERIC (references to humans,
such as the people, men and women), INSTITU-
TIONS/ORGANIZATIONS (e.g. the democrats, the
stakeholders), and SOCIAL GROUPS (e.g.
par-
ents, homeless people); and discourse role (role
within the moralization): person who is moralizing
(DEMANDER), target of the demand (ADRESSEE),
person who would benefit (BENEFICIARY) or being
disadvantaged (MALEFICIARY) from the demand.
Together, these layers form a moralization
frame, which we define as the text span that links
4The MFT assumes that moral reasoning is driven by
a set of intuitive emotional responses, or “gut feelings”,
that underlie and rationalize moral judgment.

--- Page 4 ---

(a)
The
mayor
remains
silent on topics such as
child poverty, while pub-
licly championing prestige
projects. Millions are being
wasted on the mistakes of
the senators. It is time that
politicians, too, are held ac-
countable. →Moralization
(b) Researchers collected
data on child poverty and
other broader social issues,
and how politicians respond
to them in public discourse.
The material was analyzed
to identify recurring themes
across different text types.
→No Moralization/ NVI
Table 2: Passages retrieved with DIMI, where (a)
constitutes a moralization while (b) neutrally de-
scribes a research activity about child poverty.
moral values, demands, and protagonists. These
elements are constitutive of moralizations and en-
compass all central components necessary for the
systematic analysis and interpretation of moraliza-
tions in discourse.5
Annotation Procedure.
The annotation of mor-
alizations is not only complex but also inherently
subjective. To address this, we designed a multi-
step annotation procedure that captures nuanced
judgments without compromising the operational-
ization required for computational modeling. As
outlined above, annotations (and analysis) were
conducted only for the German dataset; extending
the annotation framework to the English, French,
and Italian data is currently in progress. The anno-
tation proceeded in six stages:
(1) Identification: The mere occurrence of a
moral word or phrase does not in itself constitute a
moralization (cf. Table 2). In fact, we observe that
in many contexts, moral terms may also appear in
neutral or reportive texts without carrying any per-
suasive or argumentative intention (referred to as
Neutral Value Referring Instances, NVIs). Distin-
guishing between NVIs and moralizations was thus
a crucial first step in our annotations. We therefore
prepared a check list for moralizations together
with positive and negative examples. Then, each
retrieved text passage is annotated independently
by two annotators (binary classification), both with
a background in linguistics, yielding a high agree-
ment of 0.71 (Cohen’s Kappa). Passages with dis-
agreement are adjudicated by an expert annotator
(one of the authors).
(2) Pilot phase: We then conducted an initial ex-
ercise using a subset of 200 moralizations to train
six annotators (all with a background in linguistics)
for the task of moral value component detection
and classification (values, demands and protago-
nists). The goal was to optimize the annotation
5We acknowledge that retrieval may yield incomplete
frames; this limitation is addressed in our evaluation,
and future work will focus on methods for extracting and
segmenting complete frames.
manual by identifying sources of annotation vari-
ance, problematic categories, and ambiguous ex-
amples. We iteratively refined the manual through
additional examples and special-case rules, before
proceeding to the annotation of the full dataset.
(3) Full annotation: All instances that have
been identified as moralizations in the identification
step were then distributed across the six trained
annotators who labeled moral values, demands,
and protagonists based on our codebook using the
INCEpTION platform (Klie et al., 2018).
(4) Review: Each file was secondarily reviewed
by another annotator, allowing for corrections and
additions, and generating a further set of discus-
sion items.6 Open questions or ambiguous cases
were discussed and resolved with the team.
(5) Re-annotation of NVIs: While the review
focused on moralizing instances, some entries la-
beled as NVI qualify, upon closer inspection, as
moralizations. These NVIs were re-reviewed by
three expert annotators, limited to the test set
due to the time-intensive process.7 Instances con-
firmed as moralizations were retroactively anno-
tated with all moralization components, resulting in
278 additional annotated moralization instances.
(6) Formal validation: Final consistency checks
ensured that the formal annotation rules had been
respected (e.g., that each moralization contains
a demand or spans were marked correctly). We
correct and supplement the data accordingly and
remove irrecoverable instances.
The resulting Moralization Corpus provides a
rich, pragmatically grounded resource for study-
ing moralizations across genres and serves as a
benchmark for computational modeling of moraliz-
ing discourses.
4.
Data Statistics
The final dataset contains 11,503 instances with
an average length of 83 tokens, evenly distributed
across seven genres. The proportion of moraliza-
tions varies, mainly due to the particular considera-
tion of the test set within our multi-step annotation
process (18% in Dev and Train, and 45% in Test).
Across all genres, however, NVIs clearly outnum-
ber moralizations, confirming that moral terms are
often used descriptively rather than strategically.
6This approach has been inspired by similar ap-
proaches such as Weber-Genzel et al. (2024) or Becker
et al. (2024).
Since moralization feature annotation
is highly time-intensive, full parallel annotation of the
dataset was not feasible.
7A refined test set suffices for the prompting exper-
iments and evaluations in this paper, while automated
re-annotation of the full dataset is underway for future
finetuning experiments.

--- Page 5 ---

Moral Values.
Within moralizations, an aver-
age of 1.6 moral values were annotated per
instance, most often in Wikipedia discussions
(1.7) and least frequently in online comments
(1.4).
Across the dataset, the CARE–HARM
pair dominates (CARE 16%, HARM 22%), fol-
lowed by FAIRNESS–CHEATING (16%/13%). AU-
THORITY (3%) and SUBVERSION (2%) are rare.
Genre variation aligns with communicative con-
text: FAIRNESS–CHEATING is especially frequent
in Wikipedia discussions (28%/19%), reflecting
norms of equality and rule compliance in the meta-
discourses about the editing of articles. In court
reports, FAIRNESS and LIBERTY as foundational
principles of law prevail, while non-fiction books
show more OPPRESSION due to historical topics
and war narratives.
Demands.
Explicit and implicit demands are bal-
anced overall (53% vs. 47%), but differ by genre.
Explicit demands dominate in parliamentary de-
bates (66%), while implicit ones prevail in com-
mentaries (48%) and letters to the editor (26%),
where addressees are diffuse publics rather than
interlocutors. In such cases, moralizations serve
less to direct action than to express evaluation or
positioning, and accordingly, moral appeals often
stay implicit, as in the following example from an
letter to the editor:
It is outrageous how arrogantly our politicians
ignore the needs of our children. From a political
perspective, children do not pay off, but for society
they certainly do. Yet recognizing that requires a
certain degree of foresight.
Protagonists.
Across all instances, BENEFICIA-
RIES (which appear avg. 0.65 times within a mor-
alization) and ADDRESSEES (0.64) occur most fre-
quently, followed by demanders (0.42); MALEFICIA-
RIES are rare (0.10). Moralizations therefore tend
to emphasize positive outcomes rather than blame.
In most cases, not all protagonist slots within the
moralization frame are explicitly filled and must
be inferred from context or world knowledge, as
in the following example from q parliamentary de-
bate where the beneficiary stays implicit: We need
stricter laws to prevent racially motivated violence.
INSTITUTIONS (32%) and SOCIAL GROUPS (30%)
are the most frequent protagonist types, followed
by INDIVIDUALS (20%) and GENERIC HUMAN refer-
ences (15%). This suggests that moral demands
often invoke collective actors, as group-level out-
comes appear more socially relevant and persua-
sive than individual ones, consistent with previous
findings on the social function of moralization (see
Becker (2025): 252). Typical role–group config-
urations show that individuals act as demanders,
institutions as addressees, and social groups as
beneficiaries. Moralizations thus reflect a char-
acteristic pattern linking individual agency, institu-
tional responsibility, and collective good.
5.
Experiments
We evaluate several LLMs using different prompt
designs to assess their ability to detect moraliza-
tions and to compare their prediction to human
annotations. We evaluate results on the main test
set and the reduced Test-150 subset (see §6).
Prompt Engineering.
Our prompts8 are derived
from the annotation manual and follow its struc-
ture. Each defines moralization by three criteria:
(1) the presence of moral values, (2) an explicit
or implicit demand, and (3) an argumentative link
between both. The prompts further guide the ex-
traction and classification of moral values and pro-
tagonists. Output is generated in a standardized
JSON format including all components and a short
explanation: Moral phrases and their classification
according to MFT, extracted or reconstructed de-
mands, protagonists together with their assigned
roles and group affiliations, the binary decision on
whether the passage constitutes a moralization,
and a short explanatory rationale. The underlying
chain of thought requires the model to proceed
step by step: first identifying the core components
of moralizations, and then deciding whether the
text qualifies as a moralization.
Prompt versions were refined through iterative
evaluations. Key adjustments improved recall and
precision: (a) clearer definition of positive and neg-
ative values, (b) stricter rules for identifying implicit
demands, (c) stronger emphasis on the argumen-
tative link, (d) explicit description of NVIs, and (e)
integration of borderline cases into the examples.
Prompt Configurations.
We experimented with
seven configurations varying in level of detail, rea-
soning requirement, and example inclusion: (1)
basic-0shot: minimal instruction; (2) cot-0shot:
stepwise reasoning with detailed instructions but
without examples; (3) cot-10shot: same, plus ten
examples; (4) cot-explain-0shot: here the model
must explicitly verbalize its reasoning (an explana-
tory step), no examples; (5) cot-explain-10shot:
explanation plus examples; (6) manual-0shot: a de-
tailed configuration based on our annotation man-
ual; and (7) manual-explain-0shot: manual plus
explanatory step. Each of the five models was
tested with all seven configurations, resulting in 35
outputs per instance.
8The prompts are included in our project repository.

--- Page 6 ---

Models.
We tested five instruction-tuned LLMs
differing in architecture, scale, and context ca-
pacity: LLaMA-4-Scout-17B-16E-Instruct (109B),
C4AI-Command-a-03-2025 (111B), Mistral-Small-
3.2-24B-Instruct-2506 (24B), GPT-5-mini-2025-08-
07, and Claude-3.5-Haiku-20241022.
6.
Evaluation and Analysis
We evaluate annotation quality and model perfor-
mance for binary moralization detection and com-
ponent extraction and classification (values, de-
mands, and protagonists).
6.1.
Binary Moralization Classification
Fig. 2 summarizes results on the test set across
all prompting conditions for the binary moralization
classification task. Performance differences are
generally small; detailed prompts yield the most
consistent gains above the basic version, under-
scoring that a clear, structured definition of mor-
alization is crucial.
Among models, Cohere at-
tains the best F1 scores, followed by the ensemble
model (majority vote of all five models); Claude
and Mistral lag behind. Notably, few-shot exam-
ples and forced explanations do not consistently
improve accuracy, suggesting that moralization
requires deeper pragmatic reasoning than these
techniques capture. Error analysis shows a pre-
cision–recall trade-off: detailed prompts reduce
false positives (↑precision, ↓recall), while example-
enriched prompts reduce false negatives (↑recall,
↓precision). No single configuration dominates;
the choice depends on whether recall (e.g. for
monitoring or detection systems) or precision (e.g.
for analytical research tasks) is prioritized.
6.2.
Moralization Component Detection
and Classification
Moral values & Protagonists.
Automatically
evaluating whether a model has identified and clas-
sified all relevant moral values and protagonists
within a moralization is particularly challenging,
since precise boundary detection and overlapping
labels, among others, limit automatic agreement
with gold annotations.
We evaluate moral value and protagonist spans
with the SemEval-2013 NER-style setup (Segura-
Bedmar et al., 2013) using strict and partial match-
ing. Moral values achieve low F1 scores (strict
≤0.20; partial up to 0.22), indicating difficulties
with span boundaries and context-sensitive, often
implicit value expressions. Detailed prompts (op-
posed to basic descriptions) boost performance
most, while examples and explanation generation
yield small but consistent gains.
Protagonists
perform
higher
(strict
F1
of
0.20–0.28; +0.03–0.05 pp under partial). Cohere
and Mistral lead for values; GPT leads for protago-
nists. Detailed prompts and examples help recall
while precision remains limited, reflecting overgen-
eration and multi-label ambiguity. Methodologically,
results are constrained by our selective annotation
scheme (focus on morally relevant values/actors)
and the task’s subjectivity, so metrics should be
read as indicative rather than definitive. Neverthe-
less, the consistent relative ranking across models
and strategies provides a first indication of sys-
tem behavior and points to directions for targeted
fine-tuning and nuanced evaluation.
Demands.
Next, we evaluate the models’ ability
to extract or generate demand formulations. We
employ a combination of BLEU (Papineni et al.,
2002), ROUGE (Lin, 2004), measuring lexical over-
lap; and BERTScore (Zhang et al., 2020) which
leverages embeddings to estimate semantic simi-
larity.
The results show only minimal variation between
models and prompt configurations. BERTScore
ranges from 73 (Mistral, manual-explain) to 78
(Cohere, cot-0shot).
As expected, explicit de-
mands yield substantially higher performance (up
to 82) compared to implicit ones (maximum 75).
Overlap metrics are lower, as expected for free text
generation tasks.
Given the limitations of reference-based eval-
uation of text generation tasks (cf. Becker et al.
(2021)), we additionally conducted a manual eval-
uation of generated and extracted demands. Two
team annotators assessed all Test-150 instances
labeled as moralizations by majority vote. For each,
demands produced by the three best-performing
configurations (§6.1) of each model were rated on
a five-point Likert scale for semantic correctness,
i.e., how accurately the demand conveyed the in-
tended moral claim. In total, 73 moralizations and
1,095 generated demands were evaluated in paral-
lel, yielding substantial agreement of 0.63 (Cohen’s
Kappa), with disagreements resolved by an expert
adjudicator.
Models achieved high average ratings of 4.27, in-
dicating that generated demands largely captured
the intended moral argumentation. Differences
across configurations were minimal, and no no-
table differences appeared between implicit and
explicit prompts. GPT performed best (4.6), while
Mistral scored lowest (3.8).
Overall, these results confirm that moralization is
a complex linguistic and conceptual phenomenon
challenging for automated detection and interpre-
tation. Although detailed prompts and strong mod-
els improve performance slightly, overall scores
remain moderate, highlighting the need for refined

--- Page 7 ---

0.3591
0.6772
0.7049
0.6695
0.6992
0.5542
0.5864
0.6113
0.7407
0.7296
0.7413
0.7454
0.7384
0.7357
0.5496
0.7719
0.7667
0.7431
0.7605
0.7612
0.7772
0.6278
0.6886
0.7494
0.7459
0.7426
0.7493
0.7338
0.5201
0.6851
0.6442
0.6166
0.5676
0.6593
0.6570
0.5404
0.7619
0.7537
0.7316
0.7539
0.7191
0.7224
basic
json
0shot
cot
json
0shot
cot
json-explain
0shot
cot
json
10shot
cot
json-explain
10shot
manual
json
0shot
manual
json-explain
0shot
0
0.2
0.4
0.6
0.8
1
claude-3-5-haiku-20241022
gpt-5-mini-2025-08-07
c4ai-command-a-03-2025 (111B)
Llama-4-Scout-17B-16E-Instruct (109B)
Mistral-Small-3.2-24B-Instruct-2506
ensemble (majority vote)
f1-score (macro)
Figure 2: Binary moralization classification across models and prompting conditions (macro F1).
evaluation methods and model adaptation.
6.3.
Agreement between Models and
Humans
Next, we take a closer look at these results to
explore moralization patterns across genres and to
interpret common deviations between human and
model-based annotation – with the ultimate goal of
informing linguistic and social-scientific analysis of
moralizations in discourse.
Annotation Setup.
To assess moralization de-
tection challenges for both humans and LLMs, we
selected a genre-balanced subset of 150 test in-
stances (Test-150), annotated by five annotators
with varying expertise: Expert 1 (project lead, >2
years), Experts 2 & 3 (doctoral researchers, >1
year), and Student Assistant 1 & 2 (few months of
experience). This setup enabled analysis of how
project familiarity – and thus understanding of our
definitions – affects annotation consistency. All an-
notators received the same detailed prompts as
the models and made binary yes/no moralization
judgments (on the instance level).
Findings.
Moralization rates rose with project
familiarity: Students labeled 23–24% as moraliza-
tions, while Experts averaged 38%. This suggests
that familiarity broadens detection, as everyday
notions are narrower than our operational defini-
tion. LLMs labeled 59%, indicating a more liberal
classification tendency (see §6.4, §6.5).
Next, human-human, model-model, and human-
model agreement were compared using Fleiss’
Kappa and PABAK (which adjusts Kappa for preva-
lence and bias). Results (cf. Fig. 3) show that
experts agree more with each other than students,
and student labels align more with LLMs than
experts do. Models agree with each other to a
degree comparable to human–human agreement,
but expert–expert consistency is highest. Inter-
estingly, the weakest models in binary classifica-
tion (Claude, Mistral) show the highest consistency
Figure 3: Mean PABAK Scores for different compar-
isons of agreement between and within human an-
notators and models. While Fleiss’ Kappa scores
are on average 1–2 percentage points lower, they
follow precisely the same tendencies as the other
measures.
across prompts. Explanation prompts increase
agreement between models, suggesting that they
foster more consistent interpretations, even if they
do not improve overall predictive accuracy, as
shown in §6.1.
6.4.
Analysis of (Dis)Agreement
To understand both the limits of model-based mor-
alization detection and the characteristic patterns
in human versus model reasoning, we analyzed
cases of agreement and disagreement within Test-
150 and collected the following statistics, focusing
on the most clearly classified cases: How often,
and in which cases, do (1) ...all annotators agree
(5/5) or at least 80% (≥80% 4/5)? (2) ...do all
models/configurations agree (35/35) or at least 80
80% (≥80% 29/35)? (3) ...do all models and hu-
mans agree (40 identical decisions), or at least
80% of each group coincide? (4) ...do models and
humans diverge fundamentally (i.e., ≥80%80% of
models vs. ≥80%80% of humans make opposite
decisions)?
Results show that models agree more on moral-
izations (43%) than on NVIs (24%); humans show
the opposite pattern (22% vs. (57%). Our hypoth-
esis is that models strongly rely on surface cues,
whereas humans capture subtle/implicit cases bet-
ter. We will pursue this hypothesis further by ex-
amining lexical cues in the data as explanatory

--- Page 8 ---

factors for human and model decisions in the next
subsection.
In total, only twelve cases can be identified in
which human and model decisions fundamentally
diverge. These cases will be examined in greater
detail in the next subsection.
6.5.
Linguistic Indicators of Moralization
To test the hypothesis that specific text features
function as the primary drivers for model (and hu-
man) decisions, a selected range of linguistic indi-
cators was examined which, according to a Becker
(2025), may serve as cues for the classification of
moralizations.
Categories.
(1) Text genre: Moralizations may
be easier to identify in certain genres (e.g., opinion-
ated texts); (2) Moral vocabulary: A high frequency
of moral words (≥5 per instance) may impel both
humans and models to label a text as a moral-
ization; (3) Explicit demands: are likely easier to
recognize than implicit ones; (4) Modal verbs: As
markers of deontic modality, they often co-occur
with explicit demands and thus can serve as lin-
guistic cues for moralization; (5) Subjunctive mood:
Since moralizations often describe future scenar-
ios, subjunctive forms can work as signals; and (6)
Instance length: Very short fragments might lack
sufficient context for clear classification and are
more likely labeled as NVIs.
Focusing on cases with ≥80% model–human
agreement, we found no genre effects, but other
indicators showed trends largely confirming our
hypotheses (cf. Table ??): We find high moral-
term density in 90% of agreed moralizations vs.
only 25% of agreed NVIs; modal verbs in 71% of
moralizations vs. 22% in NVIs; subjunctive is also
more frequent in moralizations (23% vs. 8%); and
explicit demands occur in 81% of unanimously mor-
alizations. Finally, the prevalence of short snippets
among agreed NVIs points to the need for dataset
refinement, as instance length stems from data
extraction artifacts rather than linguistic content.
6.6.
Deviation Analysis (Models Only)
Finally, we compared model predictions with the
human majority vote for Test-150 to identify typical
divergences. The analysis distinguishes between
False Positives (FP – where models predicted a
moralization whereas the majority vote of humans
was NVI) and False Negatives (FN – where models
predicted “overlooked” moralization according to
the majority vote of humans).
Our analysis and annotations reveal three main
sources for FPs: (i) neutral uses of moral vocab-
ulary (incl.
quotations, historical reporting), (ii)
(4) It is not enough to simply stand up and say: We reject
all forms of violence with disgust and indignation. We
must not only show that we do not tolerate racism and
violence, but also convey the democratic val- ues by
which we want to convince our children. Therefore, I
believe that under no circumstances should we restrict
civil rights. (Parliamentary debates)
(5) Attac should advocate for a Global Marshall Plan for
developing countries. Poverty reduction can only suc-
ceed if infrastructure problems are addressed: expanding
education systems, enforcing women’s rights, and ensur-
ing access to energy and water. In addition, international
institutions such as the IMF, WTO, and World Bank must
be democratized. (Letters to the editor)
(6) Politically, however, resistance from the left would not
only jeopardize the currency reform but also the constitu-
tional basis for the Solidarity Foundation. What is needed
now is a truly Swiss-style compromise. (Interviews)
Table 3: Examples for lexical cues of moralizations
(in bold): density of moral words (4), modal verbs
(5), and Subjunctives (6).
missing context, and (iii) borderline cases. Better-
performing models (LLaMA, Cohere, GPT) show
more borderline FPs, suggesting finer sensitivity,
while weaker models (Mistral, Claude) more often
mislabel neutral passages. Dominant cause for
FNs are missed demands, especially implicit ones.
Less frequent causes are missed moral terms and
missed value–demand link across sentences, as
well as figurative language, irony, and negated de-
mands.
Summary.
Overall, the analyses show that moral-
ization detection is inherently subjective, with mod-
els relying on explicit linguistic cues and humans
– especially experts – capturing more implicit mor-
alizations. Our findings highlight the challenges of
evaluating and modeling nuanced moral reason-
ing, shaped by subjectivity, context, and linguistic
variability.
7.
Conclusion
In this paper, we introduced the Moralization Cor-
pus, a novel, frame-based resource for analyzing
how moral values are strategically employed in
argumentative discourse. Our framework opera-
tionalizes moralization as the interplay between
moral values, demands, and discourse participants,
allowing for a fine-grained analysis of how moral
rhetoric functions across genres. The annotation
procedure and resulting data shed light on the
pragmatics of moralizing communication, demon-
strating that moralizations often rely on implicit
reasoning and contextual inference rather than
overt moral vocabulary. Experimental results with

--- Page 9 ---

several LLMs show that detailed task definitions
are essential for reliable moralization detection,
whereas few-shot examples and explanation gener-
ation do not consistently improve performance. Hu-
man–model comparisons further reveal that both
groups face similar challenges – particularly re-
garding implicitness, subjectivity, and the prag-
matic boundaries of moral speech acts. Taken to-
gether, this work provides an empirical and method-
ological foundation for future research on moral
communication, argumentation, and persuasion.
Beyond linguistic and social-scientific applications,
our results also inform computational modeling of
complex, subjective, and pragmatically grounded
language phenomena.
Limitations
While the Moralization Corpus constitutes a unique
resource for studying moralizing speech acts
across genres, several limitations remain. First,
both the automatic and manual evaluation of moral
value and protagonist classification can be fur-
ther improved. The current evaluation setup pro-
vides initial insights into model behavior, but more
fine-grained semantic and boundary-sensitive mea-
sures are needed to better capture the nuanced
character of moral references and role assign-
ments. Second, although our experiments included
configurations that prompted models to verbalize
explanations, we have not yet systematically ana-
lyzed the content, coherence, or validity of these
explanations. Future work will therefore include a
dedicated investigation into how explanation quality
correlates with model accuracy and human inter-
pretability.
Third, no model fine-tuning has yet been per-
formed on our dataset.
Since the annotation
scheme introduces new task-specific concepts
such as moral frames and pragmatic roles, fine-
tuned models might substantially improve the de-
tection and classification of moralizations. A fourth
limitation concerns the contextual scope of our
instances: the current dataset is based on five-
sentence snippets, which, while sufficient for lo-
cal pragmatic analysis, may not always capture
the full discursive context in which moralizations
unfold. Expanding the contextual window or in-
cluding paragraph-level annotations will thus be
an important step toward a more comprehensive
understanding of moral reasoning in discourse.
Furthermore, although our dataset is multilin-
gual in structure, detailed annotations have so far
only been carried out for the German data. Future
work will extend the annotation framework to En-
glish, French, and Italian, enabling cross-linguistic
comparisons and broader generalization. Finally,
due to the high complexity and time intensity of
the task, parallel double annotation was conducted
only for selected subsets rather than for the en-
tire corpus. While our multi-step adjudication en-
sured consistency and reliability, a fully parallel
annotation process would further strengthen inter-
annotator agreement and improve the overall ro-
bustness of the dataset.
Ethics Statement
The Moralization Corpus was constructed using
publicly available texts and copyright-compliant ma-
terial (e.g., parliamentary debates, news articles,
online discussions) and does not include private or
sensitive data. Given the inherently normative char-
acter of moral discourse, annotators were trained
to focus on linguistic and pragmatic aspects rather
than moral evaluation or agreement with the con-
tent. We acknowledge that subjectivity is an in-
tegral part of moral interpretation; our multi-step
annotation protocol and adjudication procedures
were designed to minimize bias while preserving
interpretive diversity. We further emphasize that
the goal of this research is analytical and descrip-
tive, not prescriptive: the dataset and models are
not intended for moral judgment or behavioral pre-
diction, but to support interdisciplinary research on
communication, argumentation, and moral framing.
8.
Bibliographical References
Maria Becker. 2025. Die rolle der diskursgram-
matik bei der detektion und analyse sprachlicher
praktiken. In M. Müller, M. Reisigl, M. Becker,
M. Bender, and E. Felder, editors, Diskursgram-
matik. De Gruyter, Berlin/Boston.
Maria Becker, Swetha Ananth, and Carina Kiemes.
2023.
The moral dimensions of health: pilot
study.
Maria Becker, Kanyao Han, Haejin Lee, Antonina
Werthmann, Rezvaneh Rezapour, Jana Diesner,
and Andreas Witt. 2024. Detecting impact rele-
vant sections in scientific research. In Proceed-
ings of the 2024 Joint International Conference
on Computational Linguistics, Language Re-
sources and Evaluation (LREC-COLING 2024),
pages 4744–4749, Torino, Italia. ELRA and
ICCL.
Maria Becker, Siting Liang, and Anette Frank. 2021.
Reconstructing implicit knowledge with language
models. In Proceedings of Deep Learning Inside
Out (DeeLIO): The 2nd Workshop on Knowledge

--- Page 10 ---

Extraction and Integration for Deep Learning Ar-
chitectures, pages 11–24, Online. Association
for Computational Linguistics.
Cyril Belica. 2011. Semantische Nähe als Ähn-
lichkeit von Kookkurrenzprofilen. Bozen Univer-
sity Press.
Nicholas A. Diakopoulos, Amy X. Zhang, Dag Elge-
sem, and Andrew Salway. 2014. Identifying and
analyzing moral evaluation frames in climate
change blog discourse. Proceedings of the In-
ternational AAAI Conference on Web and Social
Media.
Ekkehard Felder and Marcus Müller. 2022. Diskurs
korpuspragmatisch: Annotation, kollaboration,
deutung am beispiel von. Sprache in Politik und
Gesellschaft: Perspektiven und Zugänge, page
241.
Kathleen C. Fraser, Svetlana Kiritchenko, and
Esma Balkir. 2022. Does moral code have a
moral code? probing delphi’s moral philosophy.
In Proceedings of the 2nd Workshop on Trust-
worthy Natural Language Processing (TrustNLP
2022), pages 26–42, Seattle, U.S.A. Association
for Computational Linguistics.
Jesse Graham, Jonathan Haidt, Sena Koleva, Matt
Motyl, Ravi Iyer, Sean P. Wojcik, and Peter H.
Ditto. 2013. Chapter two - moral foundations
theory: The pragmatic validity of moral plural-
ism. In Patricia Devine and Ashby Plant, editors,
Advances in Experimental Social Psychology,
volume 47, pages 55–130. Academic Press.
Jesse Graham, Jonathan Haidt, and Brian A
Nosek. 2009. Liberals and conservatives rely
on different sets of moral foundations. Journal of
Personality and Social Psychology, 96(5):1029–
1046.
Jonathan Haidt, Jesse Graham, and Conrad
Joseph. 2009. Above and below left–right: Ide-
ological narratives and moral foundations. Psy-
chological Inquiry, 20(2-3):110–119.
Katharina Hämmerl, Bjoern Deiseroth, Patrick
Schramowski, Jindˇrich Libovický, Constantin
Rothkopf, Alexander Fraser, and Kristian Kerst-
ing. 2023. Speaking multiple languages affects
the moral bias of language models. In Findings
of the Association for Computational Linguistics:
ACL 2023, pages 2137–2156, Toronto, Canada.
Association for Computational Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, An-
drew Critch Critch, Jerry Li Li, Dawn Song, and
Jacob Steinhardt. 2021. Aligning ai with shared
human values. In International Conference on
Learning Representations.
IDS. 2022.
Deutsches referenzkorpus / archiv
der korpora geschriebener gegenwartssprache
2022-i (release vom 08.03.2022). PID: 00-04B6-
B898-AD1A-8101-4.
Tunazzina Islam and Dan Goldwasser. 2022. Un-
derstanding covid-19 vaccine campaign on face-
book using minimal supervision. In 2022 IEEE
International Conference on Big Data (Big Data),
pages 585–595.
Liwei Jiang, Jena D. Hwang, Chandra Bhagavat-
ula, Ronan Le Bras, Maxwell Forbes, Jon Bor-
chardt, Jenny T Liang, Oren Etzioni, Maarten
Sap, and Yejin Choi. 2021. Delphi: Towards ma-
chine ethics and norms. ArXiv, abs/2110.07574.
Zohar Kampf and Tamar Katriel. 2016. Political
condemnations. The Handbook of Communica-
tion in Cross-cultural Perspective, page 312.
Johannes Kiesel, Milad Alshomary, Nailia Mirza-
khmedova, Maximilian Heinrich, Nicolas Handke,
Henning Wachsmuth, and Benno Stein. 2023.
SemEval-2023 task 4: ValueEval: Identification
of human values behind arguments. In Proceed-
ings of the 17th International Workshop on Se-
mantic Evaluation (SemEval-2023), pages 2287–
2303, Toronto, Canada. Association for Compu-
tational Linguistics.
Jan-Christoph Klie, Michael Bugert, Beto Boullosa,
Richard Eckart de Castilho, and Iryna Gurevych.
2018. The inception platform: Machine-assisted
and knowledge-oriented interactive annotation.
In Proceedings of the 27th International Con-
ference on Computational Linguistics: System
Demonstrations, pages 5–9. Association for
Computational Linguistics. Veranstaltungstitel:
The 27th International Conference on Computa-
tional Linguistics (COLING 2018).
Jonathan Kobbe, Ines Rehbein, Ioana Hulpus, , and
Heiner Stuckenschmidt. 2020. Exploring moral-
ity in argumentation. In Proceedings of the 7th
Workshop on Argument Mining, pages 30–40,
Online. Association for Computational Linguis-
tics.
Alina Landowska, Katarzyna Budzynska, and
He Zhang. 2024. Quantitative and qualitative
analysis of moral foundations in argumentation -
argumentation.
Yuanyuan Lei, Md Messal Monem Miah, Ayesha
Qamar, Sai Ramana Reddy, Jonathan Tong,
Haotian Xu, and Ruihong Huang. 2024. EMONA:
Event-level moral opinions in news articles. In
Proceedings of the 2024 Conference of the
North American Chapter of the Association for
Computational Linguistics: Human Language

--- Page 11 ---

Technologies (Volume 1: Long Papers), pages
5239–5251, Mexico City, Mexico. Association for
Computational Linguistics.
Chin-Yew Lin. 2004. ROUGE: A package for auto-
matic evaluation of summaries. In Text Summa-
rization Branches Out, pages 74–81, Barcelona,
Spain. Association for Computational Linguistics.
Marlon Mooijman, Joe Hoover, Ying Lin, Heng Ji,
and Morteza Dehghani. 2018. Moralization in so-
cial networks and the emergence of violence dur-
ing protests. Nature human behaviour, 2(6):389–
396.
Sonya Sachdeva Morteza Dehghani, Kenji Sagae
and Jonathan Gratch. 2014. Analyzing politi-
cal rhetoric in conservative and liberal weblogs
related to the construction of the “ground zero
mosque”. Journal of Information Technology &
Politics, 11(1):1–14.
Kishore Papineni, Salim Roukos, Todd Ward, and
Wei-Jing Zhu. 2002.
Bleu: a method for au-
tomatic evaluation of machine translation.
In
Proceedings of the 40th Annual Meeting of the
Association for Computational Linguistics, pages
311–318, Philadelphia, Pennsylvania, USA. As-
sociation for Computational Linguistics.
Ines Rehbein, Lilly Brauner, Florian Ertz, Ines
Reinig, and Simone Ponzetto. 2025. Moral reck-
oning: How reliable are dictionary-based meth-
ods for examining morality in text? In Proceed-
ings of the 5th International Conference on Natu-
ral Language Processing for Digital Humanities,
pages 232–250, Albuquerque, USA. Association
for Computational Linguistics.
Ines Reinig, Maria Becker, Ines Rehbein, and Si-
mone Ponzetto. 2024. A survey on modelling
morality for text analysis. In Findings of the Asso-
ciation for Computational Linguistics ACL 2024,
pages 4136–4155, Bangkok, Thailand and vir-
tual meeting. Association for Computational Lin-
guistics.
Joshua J Rhee, Chelsea Schein, and Brock Bas-
tian. 2019. The what, how, and why of moral-
ization: A review of current definitions, meth-
ods, and evidence in moralization research.
Social and Personality Psychology Compass,
13(12):e12511.
Shamik Roy, Nishanth Sridhar Nakshatri, and Dan
Goldwasser. 2022. Towards few-shot identifica-
tion of morality frames using in-context learning.
In Proceedings of the Fifth Workshop on Natural
Language Processing and Computational So-
cial Science (NLP+CSS), pages 183–196, Abu
Dhabi, UAE. Association for Computational Lin-
guistics.
Shamik Roy, Maria Leonor Pacheco, and Dan Gold-
wasser. 2021. Identifying morality frames in po-
litical tweets using relational learning. In Pro-
ceedings of the 2021 Conference on Empirical
Methods in Natural Language Processing, pages
9939–9958, Online and Punta Cana, Dominican
Republic. Association for Computational Linguis-
tics.
Patrick Schramowski, Cigdem Turan, and Nico An-
dersen. 2022. Large pre-trained language mod-
els contain human-like biases of what is right
and wrong to do. Nature Machine Intelligence,
4:258–268.
Isabel Segura-Bedmar, Paloma Martínez, and
María Herrero-Zazo. 2013. SemEval-2013 task
9 : Extraction of drug-drug interactions from
biomedical texts (DDIExtraction 2013). In Sec-
ond Joint Conference on Lexical and Computa-
tional Semantics (*SEM), Volume 2: Proceed-
ings of the Seventh International Workshop on
Semantic Evaluation (SemEval 2013), pages
341–350, Atlanta, Georgia, USA. Association
for Computational Linguistics.
Leon
Weber-Genzel,
Siyao
Peng,
Marie-
Catherine De Marneffe, and Barbara Plank.
2024. Varierr nli: Separating annotation error
from human label variation. In Proceedings of
the 62nd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long
Papers), pages 2256–2269.
Amy X. Zhang and Scott Counts. 2016. Gender
and ideology in the spread of anti-abortion policy.
In Proceedings of the 2016 CHI Conference on
Human Factors in Computing Systems, CHI ’16,
page 3378–3389, New York, NY, USA. Associa-
tion for Computing Machinery.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q.
Weinberger, and Yoav Artzi. 2020. Bertscore:
Evaluating text generation with bert.
Xinliang Frederick Zhang, Winston Wu, Nick
Beauchamp, and Lu Wang. 2024. MOKA: Moral
knowledge augmentation for moral event extrac-
tion. In Proceedings of the 2024 Conference of
the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), pages
4481–4502, Mexico City, Mexico. Association for
Computational Linguistics.

```
