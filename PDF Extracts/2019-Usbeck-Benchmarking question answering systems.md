---
title: "2019-Usbeck-Benchmarking question answering systems - PDF Extract"
source_pdf: "2019-Usbeck-Benchmarking question answering systems.pdf"
pages: 11
extracted_at: "2026-01-29T13:51:05.693511"
---

# PDF Extract: 2019-Usbeck-Benchmarking question answering systems

**Source PDF:** 2019-Usbeck-Benchmarking question answering systems.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

Semantic Web 1 (2016) 1–5
1
IOS Press
Benchmarking Question Answering Systems
Editor(s): Name Surname, University, Country
Solicited review(s): Name Surname, University, Country
Open review(s): Name Surname, University, Country
Ricardo Usbeck a,∗, Michael Röder a, Michael Hoffmann a, Felix Conrads a, Jonathan Huthmann a,
Axel-Cyrille Ngonga-Ngomo a, Christian Demmler a, and Christina Unger b
a AKSW Group, University of Leipzig, Germany
b CITEC, University of Bielefeld, Germany
Abstract. The need for making the Semantic Web better accessible for lay users and the uptake of interactive systems and smart
assistants for the Web have spawned a new generation of RDF-based question answering systems. However, the fair evaluation
of these systems remains a challenge due to the different type of answers that they provide. Hence, repeating current published
experiments or even benchmarking on the same datasets remains a complex and time-consuming task.
We present a novel online benchmarking platform for question answering (QA) that relies on the FAIR principles to support the
ﬁne-grained evaluation of question answering systems. We present how the platform addresses the fair benchmarking platform
of question answering systems through the rewriting of URIs and URLs. In addition, we implement different evaluation metrics,
measures, datasets and pre-implemented systems as well as possibilities to work with novel formats for interactive and non-
interactive benchmarking of question answering systems. Our analysis of current frameworks show that most of the current
frameworks are tailored towards particular datasets and challenges but do not provide generic models. In addition, while most
framework perform well in the annotation of entities and properties, the generation of SPARQL queries from annotated text
remains a challenge.
Keywords: Factoid Question Answering, Benchmarking, Repeatable Open Research
1. Introduction
The Web of Data has grown to contain billions of
facts pertaining to a large variety of domains. While
this wealth of data can be easily accessed by experts,
it remains difﬁcult to use for non-experts [7,37]. This
need has led to the development of a large number
of question answering (QA) and keyword search tools
for the Web of Data [33,34,35,36,40]. As benchmark-
ing has been credited with the more rapid advance-
ment of research, many campaigns and challenges
(e.g., Question Answering on Linked Data [34,35,36],
BioASQ [33]) have evolved around the QA research
ﬁeld (see Section 2) since the ﬁrst question answering
system [15]. A signiﬁcant improvement in F-measure
was measured for question answering frameworks over
*usbeck@informatik.uni-leipzig.de
the last years, an increase which is partly due to the
existence of such campaigns [18]. However, evalu-
ation datasets, measures and QA system processes
are hardly documented. In addition, the few existing
testbeds are commonly tailored toward a particular
challenge and cannot be used universally. Hence, there
is no overview of the performance of frameworks out-
side of the challenges, making the evaluation of (1) the
state of the art and (2) the weaknesses and strengths of
existing systems tedious if not impossible.
Motivated by the more than 17,000 experiments that
have already been ran on GERBIL [39] and the im-
provement of named entity recognition (NER) and en-
tity linking (EL) systems by over 12% F-measure since
the deployment of GERBIL, we address the drawbacks
aforementioned by presenting a novel benchmark-
ing platform for question answering systems dubbed
GERBIL QA. Our platform relies on the foundations
1570-0844/16/$35.00 c⃝2016 – IOS Press and the authors. All rights reserved

--- Page 2 ---

2
Usbeck et al. / Benchmarking Question Answering Systems
provided by community-approved GERBIL frame-
work for benchmarking Named Entity Recognition
and Entity Linking systems [39] (see Figure 1). While
we reused the mechanisms provided by GERBIL to
store experiments and generate corresponding URIs,
we replaced the core components of semantic anno-
tation systems, datasets, metrics and matching proce-
dures since they are not usable for the QA benchmark-
ing task. In particular, we addressed the crucial prob-
lem of benchmarking systems which return equiva-
lent URIs, URLs and strings, in a fair manner. There-
with, we provide the QA community with the means
to perform citable, comparable and extensible in-depth
benchmarking of QA systems.
GERBIL QA follows the FAIR principles [44]:
– Findable: All experimental (meta)data is avail-
able in persistent RDF as JSON-LD and in a
SPARQL endpoint1 using the rich DataID [6] and
DataCube [9] vocabularies.
– Accesible: Experiments can be linked via W3ID2
URIs using the HTTP protocol for a human- or
machine-readable version.
– Interoperatable: All (meta)data and its respec-
tive identiﬁers uses RDF as formal, accessi-
ble, shared, and broadly applicable language for
knowledge representation.
– Re-Usable: Every captured evaluation metric is
described via an RDF model and released without
any license restrictions. The metadata describes
further the provenance of the used system and
dataset.
Our approaches differs from the state of the art (in-
cluding GERBIL) and addresses the following draw-
backs of existing challenges and systems for evaluat-
ing question answering:
– Datasets: Current evaluation campaigns and chal-
lenges offer a dataset (mostly by mere reference)
and a set of questions without any extensibility.
We address this drawback by allowing for the
user-driven addition of datasets.
– Reference implementations: The development of
QA systems driven by the objective assessment
of the weaknesses of one’s own system in com-
parison to existing solutions was quasi impossi-
ble. With GERBIL QA, users can continuously
1http://gerbil-qa.aksw.org/sparql
2https://w3id.org/
benchmark their systems against the solutions in-
cluded in the platform.
– Evaluation: The fair evaluation of knowledge
base-based QA systems across different URLs
and URIs (e.g. Wikipedia vs. Freebase) used to
refer to the same real-world object, which has re-
main non-investigated so far, is now an integral
part of GERBIL QA.
To address these challenges, GERBIL QA provides
the following novel contributions:
– We offer 7 metrics for benchmarking QA systems
as well as 6 novel QA (sub-)experiment types to
(1) allow for a ﬁne-grained evaluation of QA sys-
tems and therewith (2) improvement of the diag-
nostic process.
– While we reuse the existing GERBIL core, we
provide novel matching and metric calculations
for QA since existing evaluation platforms do not
offer these functionality.
– We integrate 6 existing QA systems into the plat-
form and provide an unprecedented bundle of 22
question answering datasets (QALD-1 to QALD-
6 and NLQ) to evaluate these systems. We hence
present the ﬁrst integral comparison of QA sys-
tems for Linked Data across challenges.
– Our framework supports both online systems and
ﬁle-based evaluation campaigns over a large va-
riety of datasets. That is, we allow for the upload
of system results as well as datasets on the ﬂy as
well as webservices for systems.
– In addition, we support three widely used formats
for the interactive communication of QA systems
via webservices.
Note that GERBIL QA reuses the mechanisms pro-
vided by GERBIL to offer citable, stable experiment
URIs and descriptions, which are both human and
machine-readable. To this end, GERBIL QA uses the
recently proposed DataID [6] ontology which is based
on a combination of VoID [2] and DCAT [23] meta-
data with Prov-O [21] provenance information and
ODRL [25] licenses to describe datasets.
A demo of the system is available at http://
gerbil-qa.aksw.org/gerbil/. Furthermore,
we made the datasets, utilities and the source code
openly available and extensible.3 A general overview
over the GERBIL framework can be found at the
3https://github.com/AKSW/NLIWOD and https://
github.com/AKSW/gerbil/tree/QuestionAnswering

--- Page 3 ---

Usbeck et al. / Benchmarking Question Answering Systems
3
Open 
Datasets
Web service calls
Interface
Interface
Systems
Configuration
GERBIL
...
Benchmark Core
Your QA 
System
Your (Private) 
Dataset
Fig. 1. Overview of the Question Answering Benchmarking platform based on the GERBIL core.
project website4. Note, that while our platform focuses
on RDF-based systems, i.e., question answering sys-
tems based on Linked Data and other resources pro-
viding RDF resources or literals as answers, it can be
easily extended to non-RDF systems.
2. Question Answering Benchmarking Campaigns
Like in other disciplines, QA researchers and practi-
tioners require reliable test environments and compar-
ison methods to step-up their development speed and
lower entrance barriers. There has thus been a number
of challenges and campaigns attracting researchers as
well as industry practitioners to QA. Since 1998, the
TREC conference, especially the QA track [42], aims
at providing domain-independent evaluations over
large, unstructured corpora. This seminal campaign
pushed research projects forwards over the course of
its more than ten implementations. The latest TREC-
QA tackles the ﬁeld of live QA5 where systems an-
swer real-life, real-time questions of users submitted
to a popular community-based Question and Answer
sites. The CLEF campaigns on information retrieval
have a more than 10 year tradition in evaluation IR
4https://gerbil.aksw.org
5https://sites.google.com/site/
trecliveqa2016/
systems [1]. However, here we focus on benchmark-
ing QA systems which are able to return a concise set
of answers rather than snippets from documents to a
particular keyword query.
Next to that, the BioASQ series [33] challenges se-
mantic indexing as well as QA systems on biomedi-
cal data and is currently at its ﬁfth installment. Here,
systems have to work on RDF as well as textual data
to present matching triples as well as text snippets.
Moreover, the OKBQA6 is primarily an open QA plat-
form powered by several Korean research institutes
but they also released the NLQ datasets within their
3rd hackathon7. This dataset is answerable purely by
Wikipedia respectively by DBpedia using SPARQL.
The well-known QALD (Question Answering over
Linked Data) [36] campaign, currently running in its
6th instantiation, is a diverse evaluation series includ-
ing 1) RDF-based, 2) hybrid, i.e., RDF and textual
data, 3) statistical as well as 4) multi-knowledge base
and 5) music-domain-based benchmarks.
In the following, we will use the datasets and for-
mats (QALD-XML, QALD-JSON) as a base for our
benchmarking suite, since they have been adopted by
more than 20 QA systems since 2011 (see [18] and Ta-
ble 2). So far, yearly QALD events enable participants
6http://www.okbqa.org
7http://2015.okbqa.org/nlq

--- Page 4 ---

4
Usbeck et al. / Benchmarking Question Answering Systems
to upload XML or JSON-based system answers to pre-
viously uploaded ﬁles on the QALD website.
In contrast to existing challenges and campaigns,
our platform
1. allows using curated, updated benchmark datasets
(e.g., via Github) instead of once-uploaded-static
ﬁles and
2. referring speciﬁc experiments to speciﬁc ver-
sions of datasets. This is a major issue when
aiming to run benchmarks developed on previ-
ous versions of a dataset whose SPARQL end-
point has been updated over the years (e.g., run-
ning QALD-3 on the 2016 DBpedia endpoint) as
the results achieved differ completely from those
speciﬁed in the benchmark with some queries not
even being executable.
3. In addition, GERBIL QA allows implement-
ing wrappers for QA systems respectively us-
ing REST interfaces in an interactive manner to
benchmark QA systems online and in real-time,
see Section 4.
We refer the interested reader to our dataset project
homepage8 to read up more or add novel datasets.
3. Datasets
In its current version, our framework supports 21
QALD campaign datasets10 as well as the OKBQA
NLQ shared task 1 dataset11 listed in Table 1. The
versions of the datasets used here are curated ver-
sions of the original datasets with respect to correct-
ness of answers, quality of questions and complete-
ness of metadata. It is important to note that no eval-
uation campaign, especially QALD and OKBQA, of-
fers endpoints for all knowledge bases, i.e., develop-
ers and end users have to setup their own knowledge
base (KB) endpoint for the respective version. In Ta-
ble 1, the Knowledge Base version is the dataset which
served as a background for the provided answersets
for questions. That is, a certain benchmark dataset was
created to work on a certain version of the KB and thus
the answers could look different with another version
of the KB. Curating these datasets to the most current
KB is an open, future task. However, our platform al-
8https://github.com/AKSW/NLIWOD/tree/
master/qa.datasets
10http://qald.sebastianwalter.org/
11http://3.okbqa.org/nlq
ready checks basic assertions to these datasets such as
existence of answers in the gold standard or syntactical
correctness of gold standard SPARQL queries.
In contrast to the existing benchmarking campaigns,
GERBIL QA allows adding supplementary datasets.
Users can (1) add them to the project repository and
write a dataset wrapper in Java or (2) upload a dataset
as a ﬁle via our Web-interface for only one particu-
lar experiment. The ﬁrst option enables other users to
benchmark with this dataset and can thus spark the
generation of new datasets. The second option allows
to benchmark not yet ready or non-disclosed datasets.
In addition to supporting JSON and XML ﬁles in the
QALD format, GERBIL QA supports the extension
dubbed eQALD-JSON, which we developed to ad-
dress some of the drawbacks of the QALD format.
Existing formats lack the possibility to measure a
system’s ability measure metrics such as recognizing
entities, classes or properties. Moreover, the QALD
XML and JSON do not allow to benchmark systems
with respect to their conﬁdence in the computed an-
swer. Thus, the main advantage of eQALD-JSON is
that it represents the answers of a QA system so as
to support the full set of benchmark types provided
by GERBIL QA by explicating annotations, underly-
ing SPARQL queries and more, see Section 5. In par-
ticular, it includes 1) a knowledge base version, 2)
questions in multiple languages as well as equivalent
keyword queries, 3) annotations of the question w.r.t.
RDF resources and properties, 4) meta-information
like answer type and answer item type, 5) a schema-
less query12 as well as a SPARQL query and 6) an-
swers from the KB formatted in a manner compliant
with the W3C JSON-RDF standard13 as well as con-
ﬁdence scores for further evaluations. This format is
currently being standardized for the evaluation of nat-
ural language interfaces (see Section 7) and depicted
below:
{
"dataset": {
"id": "the dataset id",
"metadata": "some metadata..."
},
"questions": [{
"id": "the question id",
"metadata": {
"answertype": "Date|Number|String|
12https://sites.google.com/site/eswcsaq2015/
documents
13https://www.w3.org/TR/
sparql11-results-json/

--- Page 5 ---

Usbeck et al. / Benchmarking Question Answering Systems
5
Table 1
Build-in datasets and their features.
Dataset
#Questions
Knowledge Base
NLQ shared task 1
39
DBpedia 2015-04
QALD1_Test_dbpedia
50
DBpedia 3.6
QALD1_Train_dbpedia
50
DBpedia 3.6
QALD1_Test_musicbrainz
50
MusicBrainz9 (dump 2011)
QALD1_Train_musicbrainz
50
MusicBrainz (dump 2011)
QALD2_Test_dbpedia
99
DBpedia 3.7
QALD2_Train_dbpedia
100
DBpedia 3.7
QALD3_Test_dbpedia
99
DBpedia 3.8
QALD3_Train_dbpedia
100
DBpedia 3.8
QALD3_Test_esdbpedia
50
DBpedia 3.8 es
QALD3_Train_esdbpedia
50
DBpedia 3.8 es
QALD4_Test_Hybrid
10
DBpedia 3.9 + long abstracts
QALD4_Train_Hybrid
25
DBpedia 3.9 + long abstracts
QALD4_Test_Multilingual
50
DBpedia 3.9
QALD4_Train_Multilingual
200
DBpedia 3.9
QALD5_Test_Hybrid
10
DBpedia 2014 + long abstracts
QALD5_Train_Hybrid
40
DBpedia 2014 + long abstracts
QALD5_Test_Multilingual
49
DBpedia 2014
QALD5_Train_Multilingual
300
DBpedia 2014
QALD6_Train_Hybrid
49
DBpedia 2015-10 + long abstracts
QALD6_Train_Multilingual
333
DBpedia 2015-10
Total
1431
ListOfResource",
"hybrid": "TRUE|FALSE",
"aggregation" : "TRUE|FALSE",
"answeritemtype": [
"e.g., dbo:Person"
]
},
"question": [{
"language": "e.g. en or de",
"string": "The question in that
particular language...",
"keywords": "question as keywords",
"annotations": [{
"char_begin": "5...",
"char_end": "11...",
"URI": "e.g. dbr:Berlin...",
"type": "CLASS|PROPERTY|ENTITY"
}]
}],
"query": {
"SPARQL": "Question as SPARQL"
"schemaless ": "Schema-less SPARQL",
},
"answers": {
"bindings": [{
"result": {
"type": "...",
"value": "..."
}
}],
"confidence": "e.g. 0.9..."
}
}]
}
4. Systems
Table 2 shows that many systems of previous chal-
lenges and campaigns do not offer webservices, hence
increasing the difﬁculty to benchmark them with novel
datasets. Some offer webservice interfaces but they are
either not open or demand human input. Other systems
do not provide comprehensive answerset representa-
tions, e.g., showing whole paragraphs containing the
answer to a question instead of a Linked Data URI.
Another kind of system participating in past challenges
did not leave any trace of ﬁne granular quality assess-
ment as they miss publications and webservices. Thus,
the ﬁrst release of GERBIL QA contains only 6 im-
plemented system webservice clients. These are capa-
ble of answering hybrid, multilingual questions or key-
word queries. These systems are:

--- Page 6 ---

6
Usbeck et al. / Benchmarking Question Answering Systems
1. HAWK [38], the ﬁrst hybrid source QA system
which processes RDF as well as textual informa-
tion to answer one input query. HAWK is based
on a mix of computational linguistics and seman-
tic annotations to build SPARQL queries.
2. SINA [31], a keyword and natural language
query search engine which exploits the struc-
ture of RDF graphs to implement an explorative
search approach. The system is based on Hidden
Markov Models for choosing the correct dataset
to query based on a SPARQL generation process.
3. YodaQA [3], a modular, open-source, hybrid ap-
proach built on top of the Apache UIMA frame-
work14. YodaQA allows easy parallelization and
leverages pre-existing NLP UIMA components
by representing each artifact (question, search re-
sult, passage, candidate answer) as standalone
module.
4. QAKIS [7], an language-agnostic QA system
grounded in ontology-relation matches. Here, the
relation matches are based on surface forms ex-
tracted from Wikipedia to enforce a wide vari-
ety of context matches. QAKiS matches only one
relation per query and moreover relies on basic
heuristics which do not account for the variety of
natural language in general.
5. QANARY [5] follows the urge to reuse as many
as possible components to enable a best-of-
breed QA system following a new methodology
for combining preexisting modules. Thus, QA-
NARY itself is a rapid development environment
for new QA systems and a QA system itself.
6. OKBQA [20] was recently introduced by Kim et
al. also to facilitate a strong collaboration among
experts. The Open Knowledge Base Question
Answering system is thus supports developing a
new QA system reusing collaborative and intu-
itive ways.
Currently, GERBIL QA supports the addition of 3
types of systems: (1) services implemented as Java-
based wrapper (see above), (2) services conﬁgured via
the Web-interface as webservice or (3) ﬁle uploads.
Option (2) demands responses as either QALD-JSON
or eQALD-JSON while (3) support QALD-XML ﬁles
as well.For option (1), we implemented the 4 sys-
tems which were available as webservice and returned
Linked Data. We tested option (2) using the recent QA-
NARY [32] framework. Option (3) was tested with the
14https://uima.apache.org/
Table 2
Systems that participated in past QALD challenges. Note, having a
publication is optional with QALD. U means unreliable webservice,
N not yet implemented due to non-open API, M human interaction
needed.
Engine
Reference
Webservice?
Reason for Exclusion
QALD-1
FREyA
[10]
—
—
PowerAqua
[22]

U
SWIP
[8]
—
—
QALD-2
SemSeK
—
—
—
Alexandria
[43]

N
MHE
—
—
—
QAKiS
[7]

—
QALD-3
squal2sparql
[13]
—
—
CASIA
[16]
—
—
Scalewelis
[19]
—
—
RTV
[14]
—
—
Intui2
[11]
—
—
SWIP
[27]
—
—
QALD-4
Xser
[45]
—
—
gAnswer
[46]

N
CASIA
[17]
—
—
Intui3
[12]
—
—
ISOFT
[26]
—
—
RO_FII
—
—
—
QALD-5
Xser
[45]
—
—
APEQ
—
—
—
QAnswer
[30]
—
—
SemGraphQA
[4]
—
—
YodaQA
[3]

—
ISOFT
[26]
—
—
HAWK
[37]

—
QALD-6
CANaLI
[24]

M
PersianQA
—
—
—
UTQA
[41]
—
—
KWGAnswer
—
—
—
NbFramework
—
—
—
SemGraphQA
[4]
—
—
UIQA
—
—
—

--- Page 7 ---

Usbeck et al. / Benchmarking Question Answering Systems
7
QALD-6 data and will be used for the 7th instantia-
tion of the QALD challenge. This option enables de-
velopers to benchmark their system without setting up
a webservice endpoint under a public address. Within
the main GERBIL platform, experiments and log ﬁles
remain private until published, i.e., companies and in-
terested parties can test their systems online without
fearing premature publication.
5. Experiment Evaluation
In this section, we will explain the different experi-
ment types to evaluate a QA system as well as how the
evaluation metrics are computed and the system an-
swers compared. Throughout this section, we will use
the question "Who are the children of Ann Dunham?"
as running example.
5.1. Experiment Types
GERBIL QA allows measuring the performance
of common components of QA systems (named en-
tity recognition, entity linking, etc.) in addition to be-
ing able to benchmark whole QA systems. We use
the term sub-experiments to denote experiments for
benchmarking such sub-components. We designed and
implemented 5 sub-experiments inspired by past eval-
uation campaigns. The goal is to provide system de-
signers, researchers and decision makers with the op-
portunity to spot particular ﬂaws in a QA pipeline and
gain in-depth insights about the performance on differ-
ent aspects of systems on diverse datasets.
Table 3
Availability of (Sub)-experiments if the data has the QALD format
without a SPARQL query, including a SPARQL query (i.S.q.) and
for the eQALD-JSON format.
QALD
QALD i.S.q.
eQALD-JSON
QA



C2KB


P2KB


RE2KB


AT

AIT2KB


The data necessary to carry out these sub-experiments
can be provided via eQALD-JSON. For four of the fol-
lowing ﬁve sub-experiments, the needed data can also
be derived from the SPARQL query that might be re-
turned by the QA system via QALD-XML or QALD-
JSON.
Question Answering (QA). The ﬁrst experiment
is the classic experiment as described by evalua-
tion campaigns like OKBQA and QALD. It aims
to measure the capability of a system to answer
questions correctly. A system’s answer and the cor-
responding gold standard answer are regarded as
set of URIs and literals and the traditional preci-
sion, recall and F-measure used for evaluation. For
our running example, GERBIL QA expects a set
of URIs containing dbr:Maya_Soetoro-Ng and
dbr:Barack_Obama.15
Note, that if a different set is returned, we refer to our
matching algorithm to try to match the answers, see
Section 5.3.
Resource to Knowledge Base (C2KB). This sub-
experiment aims at the identiﬁcation of all resources
that are relevant for the given question. It is known
from GERBIL [39] as Concept to Knowledge Base.
The evaluation calculates the measures precision, re-
call and F-measure based on the comparison of the ex-
pected resource URIs and the URIs returned by the QA
system. Instead of a simple string comparison we make
use of an advanced meaning matching implementation
offered by GERBIL and explained in the technical re-
port for GERBIL version 1.2.2 [29]. With respect to
our running example, GERBIL QA would expect a
system to annotate dbr:Ann_Dunham.
Properties to Knowledge Base (P2KB). For this
experiment, the system has to identify all properties
that are relevant for the given question. The experi-
ment is evaluated in a manner to that of the C2KB
experiment. In our case, the correct answer would be
dbo:children.
Relation to Knowledge Base (RE2KB). This sub-
experiment focuses on the triples that have to be ex-
tracted from the question and are needed to generate
the SPARQL query that would retrieve the correct an-
swers. These triples can contain resources, variables
and literals. The evaluation of this sub-experiment cal-
culates precision, recall and F-measure based on the
comparison of the expected triples from the gold stan-
dard SPARQL query and the triples or the SPARQL
query returned by the QA system. For achieving a true
positive, a returned triple has to match an expected
triple. Two triples are counted as matching if they con-
15The preﬁx dbr is used for http://dbpedia.org/
resource/ while dbo is used for http://dbpedia.org/
ontology/ throughout the paper.

--- Page 8 ---

8
Usbeck et al. / Benchmarking Question Answering Systems
tain the same resources at the same positions. If they
contain variables, the positions of the variables have to
be the same but the variable names are ignored. If they
contain a literal, the value of the literal has to be the
same. Regarding the running example, we would ex-
pect a system to build the triple dbr:Ann_Dunham
dbo:children ?uri.
Answer Type (AT). The identiﬁcation of the an-
swer type is an important part of a QA system. We
distinguish 4 different answer types extracted from the
QALD benchmarking campaign [36], i.e., date, num-
ber, string and list of resources. A single answer type
is expected for each question. This is the type for
which the F-measure is calculated. Note that this sub-
experiment can only generate meaningful results if the
eQALD-JSON is used. For the case of our running ex-
ample, we expect a list of resources as answer type.
Answer Item Type to Knowledge Base (AIT2KB).
The answer item types are the rdf:type informa-
tion of the returned resources. Precision, recall and F-
measure are calculated based on the set of expected
types. If the expected answer set of a question does
not contain resources the set of answer item types is
expected to be empty. Here, we would expect to see
dbo:Person as answer item type as both answers
are persons.
5.2. Metrics
GERBIL QA implements 7 evaluation metrics,
i.e., micro- as well as macro-precision, recall and F-
measure as well as the runtime of webservice-based
QA systems [39]. As a reminder, the F1-Score is de-
ﬁned as
F1-score = 2Precision × Recall
Precision + Recall
,
(1)
with
Precision =
TP
TP + FP
and
(2)
Recall =
TP
TP + FN
,
(3)
with respect to a set of provided answers.
However, GERBIL QA offers the implementation
of additional metrics [29]. Thus, it would be possible
to use a hierarchical F-measure, e.g., for the AIT2KB
sub-experiment [28].
5.3. Answer Matching
A general problem of benchmarking current QA
systems are the different answerset formats. The ex-
ample question might be answered with the resources
listed above or the names "Maya Soetoro-Ng" and
"Barack Obama".
Our approach chooses a matching strategy based on
the type of response that is expected by the benchmark.
In case, the gold standard answer set asks for a list
of resources, like in the running example above, our
approach can handle two types of answersets. First, if
the QA system returns a RDF resource, GERBIL QA
relies on the transitive closure of resource URIs that
are connected by owl:sameAs links [29]. One set is
generated for the gold standard answer and the other
set for the returned resource. If both sets intersect the
answer of the system is correct, i.e., counted as a true
positive for the normal precision and recall calculation.
This approach enables the benchmarking of QA sys-
tems with datasets even if both are not based on the
same KB as long as we can ﬁnd owl:sameAs rela-
tions between the KBs.
Second, if the answer type demanding a resource
is a plain string, GERBIL QA tries to use it as la-
bel for the resource. However, a returned label like
"Barack Obama" might be shared by several resources.
In this case, all resources are retrieved and used as in-
put for the resource-based strategy described before.
Note, that this might decrease the precision of the sys-
tem since not all retrieved resources sharing the given
label are matching the expected answers.
Strings, Dates and Numbers are currently matched
by exact string matches. In the future, we will extend
that by more sophisticated matching strategies such as
lexical mapping, e.g. towards XSD datatypes.
Besides these result-focused metrics, our system
measures the performance of live systems in two ways.
First, it computes the average time a system needs to
generate a response. Second, the number of errors the
system returns or that occur during the communication
with the system are counted.
5.4. Diagnostics
The implemented sub-experiments lead to detailed
insights about a system’s performance. For example,
this experiment16 describes a stable URI of an exper-
16http://w3id.org/gerbil/qa/experiment?id=
201605010001

--- Page 9 ---

Usbeck et al. / Benchmarking Question Answering Systems
9
iment with four QA systems, three pre-implemented
as well as an uploaded QALD XML answer ﬁle, on
two datasets, namely QALD-5-train multilingual and
hybrid. The uploaded HAWK ﬁle suggests an im-
provement over the pre-implemented HAWK system.
The pre-implemented HAWK system however per-
forms better on hybrid questions than on plain English
questions. Systems like YODA, which do only pro-
vide answers without a SPARQL query cannot be anal-
ysed sufﬁciently. However, systems that also provide a
SPARQL query, can be analysed towards their perfor-
mance in the sub-experiments.
6. Sustainability Plan and Community
To foster an open community of QA researchers,
we need a reliable platform for managing experimen-
tal data in a citable and comparable way, both read-
able for humans and machines. Thus, we published
the GERBIL QA platform under the permanent ID
http://w3id.org/gerbil/qa which has been
registered with W3ID17.
We presented this platform as a prototype for the
W3C community group for Natural Language Inter-
faces for the Web of Data18 which will build recom-
mendations for benchmarks based on it. All experi-
mental data and source code is open source, in partic-
ular underlies a dual-LGPL license or is without any
licence restrictions.19 The project itself is hosted by
the AKSW research group, already maintaining more
than 50 projects20. Furthermore, the research and de-
velopment unit of the University Leipzig Computation
Center keeps daily backups to ensure long-term quota-
bility. GERBIL is open-source software which can be
maintained and hosted by anybody.
Up to today, we have seen a tremendous interest
in the platform although it is not published yet in
any conference or journal. GERBIL QA has already
been used for 85 experiments including more than 940
sub-experiment executions. For example, the devel-
opers of HAWK use the system to measure the per-
formance of different conﬁgurations through uploads
in this experiment http://gerbil-qa.aksw.
org/gerbil/experiment?id=201610230001.
17https://w3id.org/
18https://www.w3.org/community/nli/
19https://github.com/AKSW/gerbil/blob/
master/LICENSE
20http://aksw.org/Projects.html
Although the HAWK optimal conﬁguration is overall
better than the HAWK feature conﬁguration, the fea-
ture conﬁguration is more able to detect the correct
Answer Item Type. Such insights enable researchers
and developers to steer the development process more
precisely.
7. Conclusion & Future work
We present the ﬁrst online benchmarking system
for question answering approaches over factoid ques-
tions. Our platform strives to speed up the develop-
ment process by offering diverse datasets, systems and
interfaces to generate repeatable and citable experi-
ments with in-depth analytics of a system’s perfor-
mance. A known limitation is our focus on RDF-based
systems (RDF resource matching, required SPARQL
query for sub-experiments) which we seek to circum-
vent in the future by using a standard to let interfaces
communicate the needed information with demanding
a SPARQL query within the result set.
In near-future developments, we will add additional
metrics such as hierarchical f-measure, novel datasets
and more systems. Moreover, we will unify the way of
matching system answers with gold standard answers
and thus pushing a fast-pace, open science movement.
We will look into evaluation campaigns such as TREC
LiveQA and CLEF to broaden our scope and include
also non-factoid QA. Therefore, we need to look into
enabling hybrid crowd-based evaluations within the
workﬂow of the yet automatic evaluation. Further-
more, we will add this benchmarking platform to the
H2020 HOBBIT project21 for a wider spread of our
activities. Also, we will bring this development to the
W3C community group of Natural Language Inter-
faces for the Web of Data to standardize system inter-
faces and allow for an even easier and concise bench-
marking. Finally, GERBIL QA will be used for the 7th
instantiation of the QALD challenge.
Acknowledgements This work has been supported
by Eurostars projects DIESEL (E!9367) and QAMEL
(E!9725) as well as the European Union’s H2020 re-
search and innovation action HOBBIT (GA 688227).
We thank the QANARY team for inspiring discus-
sions. Furthermore, we want to thank Jin-Dong Kim
for his thoughts on the novel QA format.
21http://project-hobbit.eu/

--- Page 10 ---

10
Usbeck et al. / Benchmarking Question Answering Systems
References
[1] M. Agosti, G. M. D. Nunzio, M. Dussin, and N. Ferro. 10
years of CLEF data in DIRECT: where we are and where
we can go.
In T. Sakai, M. Sanderson, and W. Webber,
editors, Proceedings of the 3rd International Workshop on
Evaluating Information Access, EVIA 2010, National Center
of Sciences, Tokyo, Japan, June 15, 2010, pages 16–24.
National Institute of Informatics (NII), 2010.
ISBN 978-4-
86049-054-6.
URL http://research.nii.ac.jp/
ntcir/workshop/OnlineProceedings8/EVIA/
04-EVIA2010-AgostiM.pdf.
[2] K. Alexander, R. Cyganiak, M. Hausenblas, and J. Zhao.
Describing linked datasets with the void vocabulary, 2011.
http://www.w3.org/TR/void/.
[3] P. Baudiš and J. Šedivý. CLEF’15, chapter Modeling of the
Question Answering Task in the YodaQA System, pages 222–
228. Springer International Publishing, 2015.
[4] R. Beaumont, B. Grau, and A.-L. Ligozat. Semgraphqa at qald-
5: Limsi participation at qald-5 at clef.
In CLEF (Working
Notes), 2015.
[5] A. Both, D. Diefenbach, K. Singh, S. Shekarpour, D. Cherix,
and C. Lange. Qanary — a methodology for vocabulary-driven
open question answering systems. In Proceedings of the 13th
International Conference on The Semantic Web. Latest Ad-
vances and New Domains - Volume 9678, pages 625–641, New
York, NY, USA, 2016. Springer-Verlag New York, Inc. ISBN
978-3-319-34128-6.
.
URL http://dx.doi.org/10.
1007/978-3-319-34129-3_38.
[6] M. Brümmer, C. Baron, I. Ermilov, M. Freudenberg, D. Kon-
tokostas, and S. Hellmann. DataID: Towards semantically rich
metadata for complex datasets. In 10th International Confer-
ence on Semantic Systems 2014, 2014.
[7] E. Cabrio, J. Cojan, F. Gandon, and A. Hallili. Querying Multi-
lingual DBpedia with QAKiS. In ESWC, pages 194–198, 2013.
[8] C. Comparot, O. Haemmerlé, and N. Hernandez.
An easy
way of expressing conceptual graph queries from keywords
and query patterns. In International Conference on Conceptual
Structures, pages 84–96. Springer, 2010.
[9] R. Cyganiak, D. Reynolds, and J. Tennison. The RDF Data
Cube Vocabulary, 2014.
http://www.w3.org/TR/vocab-data-
cube/.
[10] D. Damljanovic, M. Agatonovic, and H. Cunningham. Natural
language interfaces to ontologies: Combining syntactic analy-
sis and ontology-based lookup through the user interaction. In
Extended Semantic Web Conference, pages 106–120. Springer,
2010.
[11] C. Dima. Intui2: A prototype system for question answering
over linked data. In CLEF (Working Notes), 2013.
[12] C. Dima. Answering natural language questions with intui3.
In CLEF (Working Notes), pages 1201–1211, 2014.
[13] S. Ferré. squall2sparql: a translator from controlled english to
full sparql 1.1. In Work. Multilingual Question Answering over
Linked Data (QALD-3), 2013.
[14] C. Giannone, V. Bellomaria, and R. Basili. A hmm-based ap-
proach to question answering against linked data. In CLEF
(Working Notes). Citeseer, 2013.
[15] B. F. Green Jr, A. K. Wolf, C. Chomsky, and K. Laughery.
Baseball: an automatic question-answerer. In Papers presented
at the May 9-11, 1961, western joint IRE-AIEE-ACM computer
conference, pages 219–224. ACM, 1961.
[16] S. He, S. Liu, Y. Chen, G. Zhou, K. Liu, and J. Zhao. Ca-
sia@ qald-3: A question answering system over linked data. In
CLEF (Working Notes), 2013.
[17] S. He, Y. Zhang, K. Liu, and J. Zhao. Casia@ v2: A mln-
based question answering system over linked data. In CLEF
(Working Notes), pages 1249–1259, 2014.
[18] K. Höffner, S. Walter, E. Marx, J. Lehmann, A.-C. Ngonga
Ngomo, and R. Usbeck. Overcoming Challenges of Seman-
tic Question Answering in the Semantic Web. Submitted to
Semantic Web Journal, 2016.
[19] G. Joris and S. Ferré.
Scalewelis: a scalable query-based
faceted search system on top of sparql endpoints. In Work.
Multilingual Question Answering over Linked Data (QALD-3),
2013.
[20] J. Kim, G. Choi, J. Kim, E. Kim, and K. Choi. The open frame-
work for developing knowledge base and question answering
system. In H. Watanabe, editor, COLING 2016, 26th Interna-
tional Conference on Computational Linguistics, Proceedings
of the Conference System Demonstrations, December 11-16,
2016, Osaka, Japan, pages 161–165. ACL, 2016. ISBN 978-4-
87974-703-7. URL http://aclweb.org/anthology/
C/C16/C16-2034.pdf.
[21] T. Lebo, S. Sahoo, D. McGuinness, K. Belhajjame, J. Ch-
eney, D. Corsar, D. Garijo, S. Soiland-Reyes, S. Zed-
nik, and J. Zhao.
PROV-O: The PROV Ontology, 2013.
http://www.w3.org/TR/prov-o/.
[22] V. Lopez, E. Motta, and V. Uren. Poweraqua: Fishing the se-
mantic web.
In European Semantic Web Conference, pages
393–410. Springer, 2006.
[23] F. Maali, J. Erickson, and P. Archer. Data Catalog Vocabulary
(DCAT), 2014. http://www.w3.org/TR/vocab-dcat/.
[24] G. M. Mazzeo and C. Zaniolo. Canali: A system for answering
controlled natural language questions on rdf knowledge bases,
2016.
[25] M.
McRoberts
and
V.
Rodríguez-Doncel.
Open
Digital
Rights
Language
(ODRL)
Ontology,
2014.
http://www.w3.org/ns/odrl/2/.
[26] S. Park, S. Kwon, B. Kim, and G. G. Lee.
Isoft at qald-5:
Hybrid question answering system over linked data and text
data. In CLEF (Working Notes), 2015.
[27] C. Pradel, G. Peyet, O. Haemmerlé, and N. Hernandez. Swip
at qald-3: results, criticisms and lesson learned. In Information
Access Evaluation. Multilinguality, Multimodality, and Visual-
ization. PROMISE Network of Excellence, 2013.
[28] M. Röder, R. Usbeck, and A.-C. Ngonga Ngomo.
Devel-
oping a Sustainable Platform for Entity Annotation Bench-
marks.
In ESWC Developers Workshop 2015, 2015.
URL http://svn.aksw.org/papers/2015/ESWC\
_GERBIL\_semdev/public.pdf.
[29] M. Röder, R. Usbeck, and A.-C. Ngonga Ngomo.
Ger-
bil’s new stunts: Semantic annotation benchmarking im-
proved.
Technical
report,
Leipzig
University,
2016.
URL http://svn.aksw.org/papers/2016/ISWC\
_Gerbil\_Update/public.pdf.
[30] S. Ruseti, A. Mirea, T. Rebedea, and S. Trausan-Matu.
Qanswer-enhanced entity matching for question answering
over linked data. In CLEF (Working Notes), 2015.
[31] S. Shekarpour, E. Marx, A.-C. N. Ngomo, and S. Auer. Sina:
Semantic interpretation of user queries for question answering
on interlinked data. Journal of Web Semantics, 2014.

--- Page 11 ---

Usbeck et al. / Benchmarking Question Answering Systems
11
[32] K. Singh, A. Both, D. Diefenbach, S. Shekarpour, D. Cherix,
and C. Lange15. Qanary–the fast track to creating a question
answering system with linked data technology. In ESWC, 2016.
[33] G. Tsatsaronis, G. Balikas, P. Malakasiotis, I. Partalas,
M. Zschunke, M. R. Alvers, D. Weissenborn, A. Krithara,
S. Petridis, D. Polychronopoulos, Y. Almirantis, J. Pavlopou-
los, N. Baskiotis, P. Gallinari, T. Artières, A. Ngonga,
N. Heino, É. Gaussier, L. Barrio-Alvers, M. Schroeder,
I. Androutsopoulos, and G. Paliouras.
An overview of
the BIOASQ large-scale biomedical semantic indexing and
question answering competition.
BMC Bioinformatics, 16:
138, 2015.
.
URL http://dx.doi.org/10.1186/
s12859-015-0564-6.
[34] C. Unger, C. Forascu, V. Lopez, A. N. Ngomo, E. Cabrio,
P. Cimiano, and S. Walter. Question answering over linked data
(QALD-4). In CLEF, pages 1172–1180, 2014.
[35] C. Unger, C. Forascu, V. Lopez, A. N. Ngomo, E. Cabrio,
P. Cimiano, and S. Walter. Question answering over linked data
(QALD-5). In CLEF, 2015. URL http://ceur-ws.org/
Vol-1391/173-CR.pdf.
[36] C. Unger, A.-C. N. Ngomo, and E. Cabrio. 6th Open Chal-
lenge on Question Answering over Linked Data (QALD-6),
pages 171–177.
Springer International Publishing, Cham,
2016. ISBN 978-3-319-46565-4.
[37] R. Usbeck and A.-C. Ngonga Ngomo.
HAWK@QALD5 –
Trying to answer hybrid questions with various simple ranking
techniques. In CLEF 2015 Labs and Workshops, Notebook Pa-
pers. CEUR Workshop Proceedings (CEUR-WS.org/Vol-1391),
2015.
URL http://svn.aksw.org/papers/2015/
CLEF\_HAWK/public.pdf.
[38] R. Usbeck, A. N. Ngomo, L. Bühmann, and C. tina Unger.
HAWK – Hybrid Question Answering Using Linked Data. In
The Semantic Web. Latest Advances and New Domains - 12th
European Semantic Web Conference, ESWC 2015, Portoroz,
Slovenia, May 31 - June 4, 2015. Proceedings, pages 353–368,
2015.
[39] R. Usbeck, M. Röder, A.-C. Ngonga Ngomo, C. Baron,
A. Both, M. Brümmer, D. Ceccarelli, M. Cornolti, D. Cherix,
B. Eickmann, P. Ferragina, C. Lemke, A. Moro, R. Navigli,
F. Piccinno, G. Rizzo, H. Sack, R. Speck, R. Troncy, J. Waitelo-
nis, and L. Wesemann. GERBIL – General Entity Annotation
Benchmark Framework. In 24th WWW conference, 2015.
[40] R. Usbeck, M. Röder, P. Haase, A. Kozlov, M. Saleem, and
A.-C. N. Ngomo. Requirements to modern semantic search
engines. In KESW, 2016.
[41] A. P. B. Veyseh. Cross-lingual question answering using com-
mon semantic space. In Proceedings of TextGraphs@NAACL-
HLT 2016: the 10th Workshop on Graph-based Methods for
Natural Language Processing, June 17, 2016, San Diego, Cal-
ifornia, USA, pages 15–19, 2016. URL http://aclweb.
org/anthology/W/W16/W16-1403.pdf.
[42] E. M. Voorhees et al. The trec-8 question answering track re-
port. In Trec, volume 99, pages 77–82, 1999.
[43] M. Wendt, M. Gerlach, and H. Düwiger. Linguistic modeling
of linked open data for question answering. In Extended Se-
mantic Web Conference, pages 102–116. Springer, 2012.
[44] M. D. Wilkinson, M. Dumontier, I. J. Aalbersberg, G. Apple-
ton, M. Axton, A. Baak, N. Blomberg, J.-W. Boiten, L. B.
da Silva Santos, P. E. Bourne, et al. The fair guiding princi-
ples for scientiﬁc data management and stewardship. Scientiﬁc
data, 3, 2016.
[45] K. Xu, Y. Feng, and D. Zhao. Xser@ QALD-4: Answering
Natural Language Questions via Phrasal Semantic Parsing.
QALD-4, 2014.
[46] L. Zou, R. Huang, H. Wang, J. X. Yu, W. He, and D. Zhao. Nat-
ural language question answering over rdf: a graph data driven
approach. In Proceedings of the 2014 ACM SIGMOD inter-
national conference on Management of data, pages 313–324.
ACM, 2014.

```
