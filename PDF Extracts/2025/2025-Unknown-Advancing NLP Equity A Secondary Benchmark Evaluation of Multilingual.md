---
title: "2025-Unknown-Advancing NLP Equity A Secondary Benchmark Evaluation of Multilingual - PDF Extract"
source_pdf: "2025-Unknown-Advancing NLP Equity A Secondary Benchmark Evaluation of Multilingual.pdf"
pages: 9
extracted_at: "2026-02-14T01:57:25.851079"
---

# PDF Extract: 2025-Unknown-Advancing NLP Equity A Secondary Benchmark Evaluation of Multilingual

**Source PDF:** 2025-Unknown-Advancing NLP Equity A Secondary Benchmark Evaluation of Multilingual.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Advancing NLP Equity: A Secondary Benchmark Evaluation of
Multilingual Language Models for Underrepresented Languages
Md Muntaqim Meherab*1, Salman*1, Md. Maruf Billah†2, Kazi Shakkhar Rahman†3, Liza
Sharmin†4, Tanvirul Islam†1, Z N M Zarif Mahmud†1, Nuruzzaman Faruqui‡5, Sheak Rashed
Haider Noori‡1, Touhid Bhuiyan‡6
1Department of Computer Science and Engineering, Daffodil International University
2Dept. of Electrical and Computer Engineering, North South University
3Dept. of Computer Science and Engineering, Islamic University of Technology
4Faculty of Humanities & Social Sciences, Daffodil International University
5Dept. of Software Engineering, Daffodil International University
6Washington University of Science and Technology
meherab2305101354@diu.edu.bd, salman2305101404@diu.edu.bd, maruf.billah.232@northsouth.edu,
shakkharrahman@iut-dhaka.edu, deanfhss@daffodilvarsity.edu.bd, tanvirulislam.cse@diu.edu.bd, zarif.cse@diu.edu.bd,
faruqui.swe@diu.edu.bd, headcse@daffodilvarsity.edu.bd, touhid.bhuiyan@wust.edu
Abstract
Recent multilingual language models promise support for
“100+ languages,” yet speakers of Indigenous and other un-
derrepresented languages still often do not see themselves
in these advances. In this work, we take a deliberately sim-
ple, secondary-benchmark perspective: rather than propos-
ing a new model or dataset, we re-evaluate an off-the-
shelf multilingual natural language inference (NLI) model
on public benchmarks that explicitly include Indigenous lan-
guages of the Americas. Concretely, we use the Americ-
asNLI benchmark for ten Indigenous languages and XNLI
for English and Spanish, and we evaluate the widely used
joeddav/xlm-roberta-large-xnli model under a
fixed, zero-shot protocol. Our goal is to answer three ques-
tions: (i) How large is the performance gap between high-
resource and underrepresented languages under the same
model and task? (ii) Are these gaps consistent across lan-
guages, or do some communities fare systematically worse
than others? (iii) What kinds of qualitative errors arise, and
what do they suggest about cultural and linguistic mismatch?
Our experiments reveal a striking discrepancy: while English
and Spanish reach almost perfect accuracy on XNLI (around
99.8% on our runs), the same model averages only about 43%
accuracy across ten Indigenous languages in AmericasNLI,
with none exceeding 47%. We also show qualitative NLI fail-
ures in Quechua that point to difficulties with morphology, id-
ioms, and discourse-level inference. We argue that even such
a simple re-analysis can serve as a low-cost yet high-impact
tool for making inequities in multilingual NLP visible, espe-
cially for communities that rarely appear in headline bench-
marks.
*These authors contributed equally.
†These authors contributed equally.
‡These authors contributed equally.
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
Introduction
Large pretrained language models have reshaped natural lan-
guage processing (NLP) in just a few years. Transformer ar-
chitectures (Vaswani et al. 2017) and multilingual pretrain-
ing (Devlin et al. 2019; Conneau et al. 2020) have led to im-
pressive gains across tasks and languages, and many models
now advertise support for “100+ languages” out of the box.
From a distance, this can give the impression that the field is
on track to serve a linguistically diverse world.
A closer look, however, tells a more uneven story. A grow-
ing body of work shows that most of the benefits of mod-
ern NLP are concentrated in a small set of high-resource
languages, typically major European and East Asian lan-
guages (Joshi et al. 2020; Blasi et al. 2022). Speakers of In-
digenous and minoritized languages often see little or no im-
provement in everyday tools—if such tools exist at all. This
is not just a technical detail; it is part of a broader pattern in
which linguistic communities already marginalized in edu-
cation, media, and governance are left behind in the digital
sphere as well.
In this paper, we focus on this gap from a pragmatic an-
gle. Rather than introducing a new model, we ask a simpler
question: If we take a widely used multilingual model exactly
as it is, and we evaluate it carefully on a benchmark that
explicitly includes underrepresented languages, what story
do the numbers tell? This type of secondary benchmarking
is not glamorous. However, it can be done quickly, it is re-
producible, and it can provide clear evidence that is easy to
communicate both inside and outside the research commu-
nity.
We centre our study on Natural Language Inference
(NLI), a standard testbed for higher-level semantic under-
standing. We treat NLI as a proxy for whether a language

--- Page 2 ---

model can handle non-trivial semantics in languages that are
rarely represented in its training data. For languages with
very limited NLP resources, even basic NLI competence is
far from guaranteed.
Concretely, we evaluate the following setup:
• Model: joeddav/xlm-roberta-large-xnli, an
XLM-R large model fine-tuned on XNLI for NLI in 15
languages.
• Low-resource
benchmark:
AmericasNLI,
an
NLI
dataset in ten Indigenous languages of the Americas,
designed for zero-shot evaluation of large multilingual
models.
• High-resource reference: XNLI test sets for English
and Spanish, two languages explicitly included during
fine-tuning.
We deliberately do not fine-tune or adapt the model. In-
stead, we use a uniform, zero-shot inference protocol across
all languages. This allows us to ask: under the same task, ar-
chitecture, and label space, how differently does the model
behave depending on which community’s language it is ex-
posed to?
We structure our analysis around three research questions:
RQ1: How well does a widely used multilingual NLI model
perform on truly low-resource Indigenous languages
compared with high-resource languages?
RQ2: Are performance gaps consistent across Indigenous
languages, or do some communities experience system-
atically worse performance than others?
RQ3: What qualitative error patterns emerge, and what do
they suggest about the model’s handling of morphology,
idioms, and discourse in these languages?
Our experimental design is intentionally modest, both in
scope and in resource demands. We use only public datasets
and a single off-the-shelf model. The entire evaluation can
be reproduced on a single GPU within roughly a day, making
it accessible to students, small labs, and community-based
researchers who may not have access to large compute clus-
ters.
Despite its simplicity, the results are sobering. In our runs,
the XNLI-fine-tuned model reaches nearly perfect accuracy
on English and Spanish (around 99.9% and 99.6%, respec-
tively), but averages only about 43% accuracy across the ten
AmericasNLI languages. Accuracy for individual Indige-
nous languages hovers in the low-40% range, with no lan-
guage above 47%. In other words, a model that is effectively
“solving” NLI in high-resource settings behaves more like a
weak baseline when asked to support Indigenous communi-
ties.
Beyond the headline numbers, qualitative error analysis
for Quechua reveals systematic confusions between contra-
diction and neutral, as well as a tendency to over-predict
entailment in the presence of complex morphology and
discourse markers. These errors align with broader con-
cerns that current multilingual models often underrepre-
sent the structural and cultural diversity of the world’s lan-
guages (Joshi et al. 2020; Bird 2022).
Our contributions are:
• A simple but rigorous secondary-benchmark evaluation
of a widely used multilingual NLI model on Americ-
asNLI and XNLI, quantifying the performance gap be-
tween high-resource and Indigenous languages.
• A set of language-level and aggregate metrics that make
these gaps easy to communicate and compare.
• A small but concrete qualitative analysis of NLI failures
in Quechua, illustrating how errors connect to morphol-
ogy, idioms, and discourse.
• A reproducible, low-cost evaluation pipeline that can
serve as a template for similar audits of other multilin-
gual models and tasks.
Our results do not claim to be the final word on fair-
ness in multilingual NLI. They are, however, a reminder that
even small, focused re-evaluations can surface inequities
that might otherwise be hidden behind impressive average
scores.
Background and Related Work
Multilingual Pretrained Language Models
Transformer-based pretrained language models such as
BERT (Devlin et al. 2019) and its multilingual variants have
become the backbone of modern NLP. Multilingual BERT
(mBERT) and XLM-R (Conneau et al. 2020) extend this
paradigm by jointly pretraining on large corpora spanning
dozens or hundreds of languages. These models have de-
livered strong cross-lingual transfer on tasks such as part-
of-speech tagging, question answering, and NLI, especially
for languages with reasonable amounts of text in pretraining
corpora.
However, pretraining coverage is not synonymous with
equitable performance. Even when a language is technically
present in the pretraining mix, it may be represented by or-
ders of magnitude fewer tokens than English or other high-
resource languages. Recent studies have shown that, in prac-
tice, performance tends to track data availability and socio-
economic status of language communities rather than any
intrinsic linguistic property (Blasi et al. 2022).
Cross-Lingual NLI Benchmarks
Natural
Language
Inference
has
become
a
standard
testbed for semantic understanding across languages.
XNLI (Conneau et al. 2018) extends the English MultiNLI
dataset to 15 languages via translation, providing a bench-
mark for evaluating multilingual sentence representations
and cross-lingual transfer. Models like XLM-R are often
fine-tuned on XNLI for these languages and then reused for
zero-shot classification in other settings.
While XNLI has driven substantial progress, its language
coverage remains skewed toward high-resource languages.
To address this gap, AmericasNLI introduces NLI test and
validation sets for ten Indigenous languages of the Ameri-
cas, including Ash´aninka, Aymara, Bribri, Guaran´ı, Nahuatl,
Otom´ı, Quechua, Rar´amuri, Shipibo-Konibo, and Wixarika.
AmericasNLI is explicitly designed to stress-test zero-shot
transfer from high-resource languages to truly low-resource

--- Page 3 ---

ones, focusing on languages with minimal or no presence in
mainstream NLP benchmarks.
Our work builds directly on this line of research. Rather
than training new models, we use AmericasNLI as a lens
to examine how an off-the-shelf XNLI-fine-tuned model be-
haves when evaluated on these languages alongside its orig-
inal high-resource targets.
Inequalities in Language Technology
Several studies have documented systematic inequalities in
language technology. Joshi et al. (Joshi et al. 2020) quantify
how a small set of languages dominate NLP research and re-
sources, while most of the world’s languages receive little or
no attention. Blasi et al. (Blasi et al. 2022) provide a global
perspective on disparities in performance across languages,
linking them to a combination of resource availability, eco-
nomic indicators, and colonial history.
Other work has argued that resource labels such as “low-
resource” can obscure important distinctions between stan-
dardised, local, and contact languages, and can carry their
own power dynamics (Bird 2022). From a governance per-
spective, these disparities have implications for who gets to
shape the development and deployment of language tech-
nologies, and whose values and communicative practices are
encoded in them.
Our study sits within this broader conversation but with a
narrower empirical focus. We ask a concrete question about
one widely used multilingual NLI model and two well-
defined benchmarks, with the aim of providing clear, repro-
ducible evidence that can be situated within a larger body of
work on linguistic equity in NLP.
Secondary Benchmarking and Model Audits
There is a growing recognition that evaluating existing mod-
els under new conditions can be as valuable as building new
models, especially for fairness and governance. Secondary
benchmarking—reusing public models and datasets to an-
swer new questions—offers an accessible way to conduct
such audits. It lowers the entry barrier for researchers and
community members who may not have resources to train
large models but do have important questions about how
those models behave.
In the multilingual setting, secondary benchmarking has
been used to examine gender bias, toxicity, and domain
shifts across languages. Our work follows this spirit: we
use standard tools (Hugging Face Transformers), public
benchmarks (AmericasNLI, XNLI), and a simple evalua-
tion pipeline to highlight how much performance can change
when moving from well-served to underrepresented lan-
guages.
Table 1 summarizes how our study sits in relation to key
strands of prior work on multilingual models, low-resource
NLI, and linguistic equity.
Task and Problem Setting
Natural Language Inference as a Probe
We frame our study around Natural Language Inference
(NLI). Given a premise sentence and a hypothesis sentence,
the task is to predict whether the hypothesis is entailed by
the premise, contradicted by it, or neutral. Even though NLI
is an idealised task, it requires models to engage with se-
mantic phenomena such as negation, quantification, lexical
relations, and basic world knowledge.
For high-resource languages like English, NLI bench-
marks have become mature enough that large pretrained
models approach human-level performance. This makes
NLI a useful probe: if a model that “solves” NLI in English
performs poorly on the same task in an Indigenous language,
this suggests that the underlying semantic capabilities have
not transferred equitably.
Formally, let L denote the set of sentences in a given lan-
guage, and let Y = {entailment, neutral, contradiction} be
the label space. Each NLI example is a pair (p, h) ∈L × L
consisting of a premise p and a hypothesis h, together with a
gold label y ∈Y. A classifier fθ (here, our fine-tuned mul-
tilingual model) implements a mapping
fθ : L × L →Y,
fθ(p, h) = ˆy,
(1)
where ˆy is the predicted NLI label. In this work, we do not
update θ; we evaluate a fixed pretrained fθ in a zero-shot
setting across languages.
Underserved Communities and Indigenous
Languages
We follow prior work in treating speakers of Indigenous lan-
guages of the Americas as a concrete example of under-
served communities in NLP. These languages are often un-
derrepresented in educational systems, under-resourced in
terms of digital tools, and sometimes endangered in terms of
intergenerational transmission. For many of them, even ba-
sic NLP infrastructure—tokenizers, morphological analyz-
ers, or spell-checkers—is still in early stages or entirely ab-
sent.
Importantly, these languages are not just data points or
test cases. They encode rich cultural histories, oral tradi-
tions, and epistemologies that have developed over cen-
turies. When language technologies fail to support these lan-
guages, they risk reinforcing existing patterns of exclusion
from digital spaces. Our goal in this paper is not to “fix”
these issues, but to help document them in a way that is con-
crete, reproducible, and legible to the broader NLP commu-
nity.
Research Questions
Given this context, our study is guided by three research
questions (RQ1–RQ3), which we restate here with slightly
more operational detail:
RQ1: How large is the performance gap between high-
resource and Indigenous languages on NLI under a fixed
multilingual model and evaluation protocol?
We measure language-wise accuracy and macro-F1, and
compare the mean performance of English and Spanish
(high-resource languages included in XNLI fine-tuning)
against that of the ten AmericasNLI languages.
RQ2: Do performance gaps vary substantially across In-
digenous languages?

--- Page 4 ---

Table 1: Positioning Our Work Within Prior Research
Area
What Existing Work Shows
What Our Study Adds
Multilingual
pre-
trained
language
models
Large models like mBERT and XLM-R deliver
strong results for well-represented languages,
but performance tends to follow data availabil-
ity and global socio-economic patterns.
We provide a concrete, task-specific demon-
stration
of
this
imbalance
by
quantifying
how sharply performance drops for Indigenous
American languages under identical evaluation
conditions.
Cross-lingual
NLI
benchmarks
XNLI has become a standard benchmark but is
skewed toward high-resource languages; Amer-
icasNLI was created to fill this gap by providing
truly low-resource test sets.
Instead of proposing new data or models, we
treat AmericasNLI as a diagnostic tool, using
it to reveal how a commonly deployed XNLI-
tuned model behaves when confronted with lan-
guages outside its design scope.
Inequalities in
lan-
guage technology
Prior studies document global disparities in NLP
performance, resource availability, and histori-
cal factors shaping linguistic representation.
We offer a focused, reproducible case study
showing how these systemic patterns manifest in
a familiar task (NLI), turning abstract inequality
findings into specific, measurable outcomes.
Secondary
bench-
marking and model
audits
Auditing models under new conditions has be-
come increasingly recognized as a lightweight
but meaningful fairness practice.
We contribute a straightforward audit procedure
that others can reuse, emphasizing accessibility
for researchers without large computational bud-
gets.
Evaluation
of
un-
derrepresented
languages
Much prior work focuses on building mod-
els, datasets, or adaptation strategies for low-
resource languages.
Our role is complementary: we highlight the
baseline reality of out-of-the-box model behav-
ior, establishing a reference point that any future
improvements should exceed.
We examine per-language metrics to see whether all lan-
guages are equally disadvantaged, or whether some lan-
guages consistently receive better or worse support from
the model.
RQ3: What kinds of qualitative errors does the model make
in an Indigenous language, and what do these errors sug-
gest about its handling of morphology, idioms, and dis-
course?
We focus on Quechua as a case study, collecting a small
sample of misclassified NLI pairs and analysing where
the model tends to over-predict entailment or confuse
contradiction with neutral.
These questions are intentionally narrow. They do not ad-
dress all dimensions of fairness or usability, but they provide
a concrete starting point that others can extend with more so-
phisticated analyses or additional models.
Methodology
Our methodology is designed around a few principles: use
only public resources; keep the evaluation protocol sim-
ple and transparent; and separate high-resource and low-
resource settings as clearly as possible.
Datasets
AmericasNLI
is an NLI benchmark that extends the
XNLI framework to ten Indigenous languages of the Amer-
icas. For each language, it provides development and test
splits with a few hundred examples each, derived from par-
allel annotations aligned with English NLI data. The target
languages include:
Ash´aninka (cni), Aymara (aym), Bribri (bzd), Guaran´ı
(gn), Nahuatl (nah), Otom´ı (oto), Quechua (quy),
Rar´amuri (tar), Shipibo-Konibo (shp), and Wixarika
(hch).
In our experiments, we use the test split for each lan-
guage. The number of test examples per language ranges
from roughly 738 to 750, following the statistics provided
with the dataset. We treat these languages as representa-
tive examples of underrepresented communities in current
NLP practice: they are typologically diverse, historically
marginalized, and largely absent from mainstream training
corpora.
XNLI
For a high-resource reference point, we use the
XNLI test sets for English and Spanish. XNLI extends
MultiNLI to 15 languages via translation and serves as
a standard benchmark for cross-lingual NLI. Crucially,
the joeddav/xlm-roberta-large-xnli model we
evaluate has been fine-tuned on XNLI for a subset of these
languages, including English and Spanish. We treat perfor-
mance on these two languages as an approximate upper
bound for what the model can achieve under our evaluation
protocol.
Model
We evaluate a single off-the-shelf model:
• Model: joeddav/xlm-roberta-large-xnli
• Base architecture: XLM-R large (Conneau et al. 2020)
• Fine-tuning: Trained on XNLI for NLI in 15 languages

--- Page 5 ---

XLM-R itself is a multilingual masked language model
pretrained on over 100 languages with the RoBERTa-style
objective. The joeddav/xlm-roberta-large-xnli
checkpoint adds a classification head and fine-tuning on
XNLI, making it a widely used backbone for zero-shot
cross-lingual NLI and text classification.
This model is a natural choice for our study for two rea-
sons. First, it is popular in practice; many applied systems
rely on it, often under the assumption that it “supports” a
wide range of languages out of the box. Second, its fine-
tuning data explicitly excludes the Indigenous languages in
AmericasNLI, making it a realistic example of a model that
is powerful in high-resource contexts but not intentionally
designed for the underrepresented languages we care about.
Evaluation Protocol
We adopt a uniform, zero-shot evaluation protocol across all
languages and datasets. There is no fine-tuning or adaptation
on AmericasNLI.
Input encoding.
For each (premise, hypothesis) pair, we
use the Hugging Face XLM-R tokenizer to encode the sen-
tence pair with a maximum sequence length of 128 tokens.
We rely on the standard sentence-pair encoding format used
in transformers, which internally handles segment em-
beddings as appropriate for XLM-R.
Model inference.
We run batched inference using a batch
size of 32 and single-GPU acceleration. For each batch, we
obtain the model’s logits over the three NLI labels (entail-
ment, neutral, contradiction). We then take the argmax to
obtain the predicted class for each example.
Metrics.
For each language and dataset, we report two
standard classification metrics:
• Accuracy: the proportion of test examples for which the
predicted label matches the gold label.
• Macro-F1: the unweighted average F1 score across the
three classes, which helps reduce the impact of any label
imbalance.
To support RQ1 and RQ2, we also compute aggregate
mean accuracy for two groups:
• High-resource group: the English and Spanish XNLI
test sets.
• Low-resource group: the ten AmericasNLI languages.
Formally, given a test set {(pi, hi, yi)}N
i=1 for a particular
language, with gold labels yi ∈Y and model predictions
ˆyi = fθ(pi, hi), the accuracy is
Acc = 1
N
N
X
i=1
1{ˆyi = yi},
(2)
where 1{·} is the usual indicator function.
Let C = {entailment, neutral, contradiction} denote the
set of classes. For each class c ∈C, we define precision Pc
and recall Rc in the standard way from true positives, false
positives, and false negatives. The macro-averaged F1 score
is then
Macro-F1 = 1
|C|
X
c∈C
2PcRc
Pc + Rc + ε,
(3)
where ε is a small constant to avoid division by zero.
Error analysis.
For RQ3, we focus on Quechua (quy) as
a case study. We run the same inference procedure and then
collect a small sample of misclassified examples. For each,
we record the premise, hypothesis, gold label, and predicted
label, and we manually inspect them to identify recurring
patterns such as:
• Confusions between contradiction and neutral.
• Systematic over-prediction of entailment.
• Apparent difficulties with morphology or idiomatic ex-
pressions.
Implementation Details
All experiments are implemented in Python using the
Hugging Face datasets and transformers libraries.
We load AmericasNLI and XNLI directly from Hug-
ging Face, and we rely on the model hub to fetch the
joeddav/xlm-roberta-large-xnli
checkpoint.
We fix a random seed for data loading to ensure repro-
ducibility, although the evaluation itself is deterministic
given the trained model.
The
entire
pipeline—from
data
loading
to
metric
computation—can be run in a single Colab notebook with
GPU support.
Experiments and Results
In this section, we report our zero-shot evaluation of XLM-
Rlarge (fine-tuned on XNLI) on the AmericasNLI benchmark
and the XNLI test sets for English and Spanish. We focus on
three aspects: (i) the overall performance gap between high-
and low-resource languages, (ii) variation across Indigenous
languages, and (iii) qualitative error patterns that shed light
on cultural and morpho-syntactic mismatches.
Experimental Setup
We follow the protocol outlined in Section method-
ology.
For
each
language
in
AmericasNLI,
we
use
the
official
test
split
and
run
the
pretrained
joeddav/xlm-roberta-large-xnli
model
in
a pure zero-shot setting, without any further fine-tuning
or adaptation. For XNLI, we evaluate on the English
and Spanish test sets to approximate an upper bound for
high-resource, in-distribution languages.
Unless otherwise noted, we use a maximum sequence
length of 128 subword tokens and a batch size of 32. Longer
sequences are truncated from the end. We compute accuracy
and macro-averaged F1 (macro-F1) over the three NLI la-
bels (entailment, neutral, contradiction). All predictions are
obtained with a single forward pass per example.

--- Page 6 ---

Language
Code
# Test
Acc.
Macro-F1
Aymara
aym
750
0.421
0.378
Bribri
bzd
750
0.443
0.419
Ash´aninka
cni
750
0.416
0.390
Guaran´ı
gn
750
0.460
0.428
Wixarika
hch
750
0.407
0.362
Nahuatl
nah
738
0.463
0.446
Otom´ı
oto
748
0.434
0.407
Quechua
quy
750
0.417
0.388
Shipibo-Konibo
shp
750
0.467
0.456
Rar´amuri
tar
750
0.403
0.352
Table 2: Zero-shot NLI performance of XLM-Rlarge on
AmericasNLI. Accuracy and macro-F1 are computed over
three labels: entailment, neutral, and contradiction.
Group
Languages
Mean Acc.
High-resource (XNLI)
en, es
0.998
Low-resource (AmericasNLI)
10 langs
0.433
Table 3: Aggregate zero-shot accuracy of XLM-Rlarge on
XNLI (English, Spanish) and AmericasNLI (10 Indigenous
languages).
Per-language Performance on AmericasNLI
Table 2 shows per-language performance on AmericasNLI.
Accuracy ranges from roughly 40% to 47% across the
ten Indigenous languages, with macro-F1 tracking accuracy
closely. In other words, even the best-performing languages
are just a bit above the random baseline of 33.3% for a bal-
anced three-way classification task.
The model does slightly better on Shipibo-Konibo (0.467
accuracy, 0.456 macro-F1) and Nahuatl (0.463 / 0.446), and
slightly worse on Rar´amuri (0.403 / 0.352) and Wixarika
(0.407 / 0.362). Overall, the spread between the best and
worst Indigenous languages is modest (about six percent-
age points of accuracy), and the entire band is far from
what would normally be considered “usable” performance
in high-stakes applications.
Figure 1 visualizes this distribution. The bar plot makes
the story easy to see at a glance: all Indigenous languages
cluster just above chance level, with none approaching high-
resource performance.
High- vs. Low-resource Comparison
To understand how large the gap is between high- and low-
resource languages for the same model and same task, we
compare AmericasNLI results with XNLI results for English
and Spanish (Table 3). On XNLI, the model achieves almost
perfect accuracy: 0.999 for English and 0.996 for Spanish.
Averaged over these two languages, the mean accuracy is
approximately 0.998.
For the ten AmericasNLI languages, the mean accuracy
is 0.4331. The difference between high- and low-resource
groups is therefore about 56.4 percentage points. That is,
the same widely deployed model behaves almost like a reli-
able semantic reasoner for English and Spanish, and like a
barely-above-chance classifier for Indigenous languages of
the Americas.
We can make the high- vs. low-resource comparison a
bit more explicit. Let Lhigh be the set of high-resource lan-
guages (in our case, English and Spanish from XNLI), and
let Llow be the set of low-resource languages (the ten Amer-
icasNLI languages). For each language ℓ, let Acc(ℓ) denote
the test accuracy of fθ on that language. We define group-
wise mean accuracies as
Acchigh =
1
|Lhigh|
X
ℓ∈Lhigh
Acc(ℓ),
Acclow =
1
|Llow|
X
ℓ∈Llow
Acc(ℓ).
(4)
The performance gap we highlight can then be written as
∆Acc = Acchigh −Acclow.
(5)
In our runs, Acchigh ≈0.998 and Acclow ≈0.433, so
∆Acc ≈0.564.
We also plot this contrast directly in Figure 2. The visual
gap between the two bars is a concrete reminder that current
multilingual models are far from offering a fair distribution
of semantic understanding across languages.
Qualitative Error Analysis
To understand model failures beyond aggregate metrics, we
manually inspect a small sample of misclassified Quechua
examples (quy) from the AmericasNLI test set (five cases,
sampled from our evaluation outputs). A consistent pat-
tern is over-predicting entailment under high lexical over-
lap, even when the hypothesis adds unsupported details
(gold: neutral) or reverses polarity (gold: contradiction). We
also observe confusion between contradiction and neutral
when negation or evidential markers shift commitment in
ways that are not captured by shallow lexical cues. Overall,
these errors suggest the model often relies on surface over-
lap rather than tracking the underlying entailment relation,
consistent with limited task-specific exposure to Indigenous
morpho-syntax and discourse markers during fine-tuning.
Discussion
We now return to our three research questions and ask what
the numbers mean for equity and fairness in multilingual
NLP.
RQ1: How Well Does the Model Perform on
Low-resource Languages?
On XNLI, XLM-Rlarge essentially solves the task: near-
perfect accuracy and macro-F1 for English and Spanish.
On AmericasNLI, by contrast, the average accuracy is only
43.3%, with all languages tightly clustered between roughly
40% and 47%.
From a purely machine learning perspective, one might
say the model is “above chance” and move on. From a user-
centered perspective, however, these numbers mean that for
speakers of Indigenous American languages, a model that
appears state-of-the-art in English behaves more like a rough
heuristic than a dependable tool.

--- Page 7 ---

Aymara
(aym)
Bribri
(bzd)
Asháninka
(cni)
Guaraní
(gn)
Wixarika
(hch)
Nahuatl
(nah)
Otomí
(oto)
Quechua
(quy)
Shipibo­Konibo
(shp)
Rarámuri
(tar)
English
(en)
Spanish
(es)
0.0
0.2
0.4
0.6
0.8
1.0
Score
0.421
0.443
0.416
0.460
0.407
0.463
0.434
0.417
0.467
0.403
0.998
0.998
0.378
0.419
0.390
0.428
0.362
0.446
0.407
0.388
0.456
0.352
0.998
0.998
High­resource baseline
(English & Spanish, Mean Acc. 0.998)
Zero­shot NLI accuracy and macro­F1 of XLM­Rlarge by language
Test Accuracy
Macro­F1
English & Spanish (Mean Acc. 0.998)
Figure 1: Zero-shot accuracy of XLM-Rlarge on each AmericasNLI language. All languages sit in a narrow band around 43%
accuracy, only slightly above the random baseline of 33.3%.
High­resource (XNLI)
(en, es)
Low­resource (AmericasNLI)
(10 langs)
0.0
0.2
0.4
0.6
0.8
1.0
Mean Accuracy
0.998
0.433
Large performance gap
between high­ and low­resource
Mean Accuracy by Resource Setting
High­resource (en, es)
Low­resource (10 AmericasNLI langs)
Figure 2: Mean zero-shot accuracy of XLM-Rlarge for high-
resource languages (English (en), Spanish (es)) vs. low-
resource AmericasNLI languages.
RQ2: Are There Systematic Performance Gaps
Across Languages?
The group-level gap of around 56 percentage points between
high- and low-resource languages is hard to ignore. It mir-
rors, in a concrete NLI setting, what prior work has reported
at scale: language technologies work best for languages with
large digital footprints and leave many other communities
behind.
Within the AmericasNLI group, variation is relatively
small. Shipibo-Konibo and Nahuatl sit at the high end,
Rar´amuri and Wixarika at the low end, but the spread is only
about six percentage points. This suggests that the main is-
sue is not fine-grained linguistic typology, but the fact that
none of these languages were treated as first-class targets
during model development.
RQ3: What Do Error Patterns Tell Us About
Cultural and Linguistic Mismatch?
The Quechua examples show that the model struggles pre-
cisely where local morpho-syntax and pragmatics carry
much of the meaning: negation, evidentiality, and subtle
shifts in commitment or stance. It tends to over-predict en-
tailment when there is high lexical overlap, even when the
hypothesis is neutral or contradictory, and to over-predict
contradiction when it encounters explicit negation without
tracking what is actually being negated.
For speakers, this is more than an abstract optimization
issue. Misclassifying contradictions as entailments effec-
tively asserts that two statements agree when they in fact
conflict. Collapsing neutral into contradiction can create an
impression of disagreement where none exists. When such
behaviours systematically affect already underserved com-
munities, they become fairness concerns rather than mere
model quirks.
Implications for Evaluation and Model Selection
Our results also speak to how we evaluate and select mul-
tilingual models. If we only look at averages over high-

--- Page 8 ---

resource languages, or macro-averages over mostly well-
supported languages, severe disparities can remain hidden.
A model may be “state-of-the-art” on a popular benchmark
and still perform at near-chance level for entire language
families.
In this sense, AmericasNLI serves as a useful stress test:
it exposes the limits of zero-shot transfer for languages that
have, until recently, been almost invisible in large-scale NLP
evaluation. For practitioners, the message is simple but im-
portant: whenever possible, we should inspect how a multi-
lingual model behaves on truly low-resource languages, not
just on those that dominate existing leaderboards.
Limitations and Future Work
This study is intentionally narrow. We focus on a single task
(natural language inference), a single benchmark (Americas-
NLI), and one widely used multilingual model (XLM-Rlarge
fine-tuned on XNLI). This makes the setup easy to repro-
duce and interpret, but also means our conclusions should
be read with caution.
First, we do not adapt or fine-tune the model on Indige-
nous languages. Prior work shows that continued pretraining
or translation-based approaches can substantially improve
performance on AmericasNLI. Our goal here is different:
to quantify out-of-the-box behavior in a realistic zero-shot
setting. Future work should compare a range of adaptation
strategies through the same fairness lens.
Second, we analyze only a small set of qualitative errors
for one language (Quechua). A fuller picture would require
systematic human analysis across all ten languages, ideally
involving fluent speakers and community members rather
than external annotators alone.
Third, our evaluation is purely text-based. Many real-
world uses of NLP in Indigenous communities involve
speech, code-switching, non-standard orthographies, or
multimodal input. The gap we observe on clean written NLI
data is therefore likely an optimistic estimate.
Finally, we do not attempt to model the social or historical
forces that produced the current distribution of resources and
benchmarks. Our work sits downstream of those structural
inequalities; addressing them will require collaboration well
beyond the technical NLP community.
Ethical Considerations
Working with Indigenous Languages
AmericasNLI was created with care, with documented data
collection and annotation. Even so, work with Indigenous
languages must attend to consent, representation, and benefit
sharing. In this study we rely only on the publicly released
splits and do not scrape additional data or train new models
from scratch.
Our analysis also remains at arm’s length from the com-
munities whose languages are represented. We do not claim
to speak for them or fully capture the social meaning of the
sentences. Any deployment of models for these languages
should involve collaboration with community members, lo-
cal experts, and relevant institutions.
Risks of Misuse and Misinterpretation
A first risk is that poor performance is misread as evidence
that Indigenous languages are “too hard” or “not worth sup-
porting.” The opposite is true: the gap we see reflects design
choices and resource allocation in the NLP ecosystem, not
properties of the languages themselves.
A second risk is over-confidence in models for high-
resource languages. Near-perfect accuracy on XNLI for En-
glish and Spanish does not mean these models are unbiased
or harmless. They can still encode and amplify stereotypes,
treat social groups unfairly, or fail in unexpected ways out-
side their original training domains.
Fairness and Responsibility
From a fairness perspective, the core message is simple: cur-
rent multilingual language models offer very different levels
of service depending on which language a person speaks.
This inequality is the outcome of choices about which lan-
guages to include in pretraining, which benchmarks to pri-
oritize, and which adaptation methods to develop.
As researchers and practitioners, we have a responsibil-
ity to make these disparities visible and to push for evalu-
ation practices that do not quietly ignore underserved com-
munities. Benchmarks like AmericasNLI are one part of that
work; building inclusive datasets, governance frameworks,
and community partnerships is the longer-term task.
Conclusion
We set out to answer a simple question: what happens when
a widely used multilingual NLI model, one that performs
nearly perfectly on English and Spanish, is asked to handle
truly low-resource Indigenous languages?
Using AmericasNLI as our testbed, we found that XLM-
Rlarge in a zero-shot setting hovers just above chance for
all ten Indigenous languages, with an average accuracy of
43.3%. In sharp contrast, the same model reaches almost
99.8% mean accuracy on XNLI for English and Spanish.
The resulting gap of about 56 percentage points is a clear
illustration of the linguistic digital divide.
Our qualitative analysis of Quechua error cases suggests
that the model especially struggles with morpho-syntactic
features and pragmatic nuances that were not part of its fine-
tuning regime. In those regions of the space, it falls back on
shallow lexical cues and produces label assignments that are
often at odds with human intuition.
From a technical point of view, these results are unsurpris-
ing: it is hard to do well on languages that receive little or no
explicit supervision. From a human point of view, however,
they are a reminder that talk of “multilingual” models can
easily obscure who actually benefits from the technology. If
we care about NLP equity, we need evaluation setups that
foreground underserved languages and make performance
gaps impossible to ignore.
We hope that this small, focused study can serve as a
compact, reproducible example for students and practition-
ers who want to engage seriously with fairness in multilin-
gual NLP, even when working under tight time or resource
constraints.

--- Page 9 ---

References
[Blasi et al. 2022] Blasi, D. E.; Anastasopoulos, A.; and
Neubig, G. 2022. Systematic Inequalities in Lan-
guage Technology Performance across the World’s
Languages. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), 5486–5505. Dublin, Ireland:
Association for Computational Linguistics.
[Bird 2022] Bird, S. 2022. Local Languages, Third Spaces,
and other High-Resource Scenarios. In Proceedings of
the 60th Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers), 7817–
7829. Dublin, Ireland: Association for Computational
Linguistics.
[Choudhury and Deshpande 2021] Choudhury,
M.,
and
Deshpande, A. 2021. How Linguistically Fair Are
Multilingual Pre-Trained Language Models? Proceed-
ings of AAAI, 35(14):12710–12718.
[Conneau et al. 2018] Conneau, A.; Lample, G.; Rinott, R.;
Williams, A.; Bowman, S.; Schwenk, H.; and Stoy-
anov, V. 2018. XNLI: Evaluating Cross-lingual Sen-
tence Representations. Proceedings of EMNLP, 2475–
2485.
[Conneau et al. 2020] Conneau,
A.;
Khandelwal,
K.;
Goyal, N.; Chaudhary, V.; Wenzek, G.; Guzm´an, F.;
Grave, E.; Ott, M.; Zettlemoyer, L.; and Stoyanov,
V. 2020. Unsupervised Cross-lingual Representation
Learning at Scale. Proceedings of ACL, 8440–8451.
[Devlin et al. 2019] Devlin, J.; Chang, M.-W.; Lee, K.; and
Toutanova, K. 2019. BERT: Pre-training of Deep Bidi-
rectional Transformers for Language Understanding.
Proceedings of NAACL-HLT, 4171–4186.
[Doddapaneni et al. 2021] Doddapaneni, S.; Ramesh, G.;
Sahoo, S.; Jain, A.; Kunchukuttan, A.; and Khapra, M.
2021. A Primer on Pretrained Multilingual Language
Models. arXiv preprint arXiv:2107.00676.
[Ebrahimi et al. 2021] Ebrahimi, A.; Mager, M.; Oncevay,
A.; Chaudhary, V.; Chiruzzo, L.; Fan, A.; Ortega, J.;
Ramos, R.; Rios, A.; Meza-Ruiz, I.; Gim´enez-Lugo,
G.; Mager, E.; Neubig, G.; Palmer, A.; Coto-Solano,
R.; Vu, N. T.; and Kann, K. 2021. AmericasNLI: Eval-
uating Zero-shot Natural Language Understanding of
Pretrained Multilingual Models in Truly Low-resource
Languages. arXiv preprint arXiv:2104.08726.
[Ebrahimi et al. 2022] Ebrahimi, A.; Mager, M.; Oncevay,
A.; Chaudhary, V.; Chiruzzo, L.; Fan, A.; Ortega,
J.; Ramos, R.; Rios, A.; Meza-Ruiz, I.; et al. 2022.
AmericasNLI: Machine Translation and Natural Lan-
guage Inference Systems for Indigenous Languages
of the Americas. Frontiers in Artificial Intelligence,
5:995667.
[Hedderich et al. 2021] Hedderich, M. A.; Lange, L.; Adel,
H.; Str¨otgen, J.; and Klakow, D. 2021. A Survey on
Recent Approaches for Natural Language Processing
in Low-Resource Scenarios. Journal of Artificial Intel-
ligence Research, 72:781–887.
[Joshi et al. 2020] Joshi, P.; Santy, S.; Budhiraja, A.; Bali,
K.; and Choudhury, M. 2020. The State and Fate of
Linguistic Diversity and Inclusion in the NLP World.
Proceedings of ACL, 6282–6293.
[Lauscher et al. 2022] Lauscher, A.; Stojanovski, D.; Ponti,
E. M.; Vuli´c, I.; and Glavaˇs, G. 2022. Are Pretrained
Multilingual Models Equally Fair across Languages?
Proceedings of COLING, 3602–3621.
[Muller et al. 2020] Muller, B.; Ruder, S.; Ponti, E. M.;
Vuli´c, I.; and Søgaard, A. 2020. Unsupervised Cross-
Lingual
Representations
for
Low-Resource
Lan-
guages. Proceedings of ACL, 2877–2891.
[Pfeiffer et al. 2020a] Pfeiffer, J.; Vuli´c, I.; Gurevych, I.;
and Ruder, S. 2020a. MAD-X: An Adapter-based
Framework for Multi-task Cross-lingual Transfer. Pro-
ceedings of EMNLP, 7654–7673.
[Pfeiffer et al. 2020b] Pfeiffer, J.; Ruder, S.; Vuli´c, I.; and
Gurevych, I. 2020b. Unks Everywhere: Adapting Mul-
tilingual Language Models to New Scripts. Proceed-
ings of EMNLP, 3524–3536.
[Qian et al. 2018] Qian, Y.; Zhang, N.; Tan, T.; and Yu,
K. 2018. Deep Learning Based Speech Recognition
for Low-Resource Languages. IEEE/ACM Transac-
tions on Audio, Speech, and Language Processing,
26(1):211–224.
[Ruder 2021] Ruder, S. 2021. Challenges and Opportuni-
ties in Multilingual NLP. Communications of the ACM,
64(6):58–63.
[Vaswani et al. 2017] Vaswani, A.; Shazeer, N.; Parmar, N.;
Uszkoreit, J.; Jones, L.; Gomez, A. N.; Kaiser, Ł.;
and Polosukhin, I. 2017. Attention Is All You Need.
Advances in Neural Information Processing Systems,
30:5998–6008.
[Wang et al. 2022] Wang, J.; Liu, Y.; and Wang, X. 2022.
Assessing Multilingual Fairness in Pre-trained Multi-
modal Representations. Findings of ACL, 2681–2695.
[Williams et al. 2018] Williams, A.; Nangia, N.; and Bow-
man, S. 2018. A Broad-Coverage Challenge Corpus for
Sentence Understanding through Inference. Proceed-
ings of NAACL-HLT, 1112–1122.
[Wu and Dredze 2020] Wu, S., and Dredze, M. 2020. Are
All Languages Created Equal in Multilingual BERT?
Proceedings of ACL, 120–130.
[Zhao et al. 2020] Zhao, J.; Wang, T.; and Yatskar, M. 2020.
Gender Bias in Multilingual Word Embeddings. Pro-
ceedings of EMNLP, 2502–2513.

```
