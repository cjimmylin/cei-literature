---
title: "2025-Brito-ToxSyn Reducing Bias in Hate Speech Detection via Synthetic Minority - PDF Extract"
source_pdf: "2025-Brito-ToxSyn Reducing Bias in Hate Speech Detection via Synthetic Minority.pdf"
pages: 10
extracted_at: "2026-02-13T09:50:30.549138"
---

# PDF Extract: 2025-Brito-ToxSyn Reducing Bias in Hate Speech Detection via Synthetic Minority

**Source PDF:** 2025-Brito-ToxSyn Reducing Bias in Hate Speech Detection via Synthetic Minority.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

ToxSyn: Reducing Bias in Hate Speech Detection via Synthetic
Minority Data in Brazilian Portuguese
Iago A. Brito, Julia S. Dollis, Fernanda B. Färber, Diogo F. C. Silva
Arlindo R. Galvão Filho
Advanced Knowledge Center for Immersive Technologies (AKCIT), Federal University of Goiás
{iagoalves, juliadollis, fernandabufon, diogo_fernandes}@discente.ufg.br
arlindogalvao@ufg.br
Abstract
The development of robust hate speech detection systems remains limited by the lack of large-scale, fine-grained
training data, especially for languages beyond English. Existing corpora typically rely on coarse toxic/non-toxic labels,
and the few that capture hate directed at specific minority groups critically lack the non-toxic counterexamples (i.e.,
benign text about minorities) required to distinguish genuine hate from mere discussion. We introduce ToxSyn, the
first Portuguese large-scale corpus explicitly designed for multi-label hate speech detection across nine protected
minority groups. Generated via a controllable four-stage pipeline, ToxSyn includes discourse-type annotations to
capture rhetorical strategies of toxic language, such as sarcasm or dehumanization. Crucially, it systematically
includes the non-toxic counterexamples absent in all other public datasets. Our experiments reveal a catastrophic,
mutual generalization failure between social-media domains and ToxSyn: models trained on social media struggle to
generalize to minority-specific contexts, and vice-versa. This finding indicates they are distinct tasks and exposes
summary metrics like Macro F1 can be unreliable indicators of true model behavior, as they completely mask model
failure. We publicly release ToxSyn at HuggingFace to foster reproducible research on synthetic data generation and
benchmark progress in hate-speech detection for low- and mid-resource languages.
Keywords: Hate speech detection, synthetic data generation, low-resource NLP
1.
Introduction
The task of identifying and mitigating online hate
speech is a critical challenge for building safe and
inclusive digital spaces, from social media plat-
forms to nascent virtual reality ecosystems (Albladi
et al., 2025; Weerasinghe et al., 2025). However,
progress is limited by severe limitations in available
training corpora. Most datasets rely on a coarse
toxic/non-toxic dichotomy, lacking the multi-label
annotations needed to identify specific protected
classes, such as racial, religious, or gender groups
(Vargas et al., 2022). Furthermore, while some
English datasets have begun to include both ex-
plicit and implicit toxicity, the fundamental aspect of
discourse type remains unaddressed in existing cor-
pora, failing to capture crucial contextual features.
Consequently, the field is constrained to develop-
ing models that may achieve high performance on
coarse-grained benchmarks, but lack the neces-
sary robustness and contextual understanding to
address the nuanced ways hate speech targets
vulnerable communities.
Furthermore,
this data-centric challenge is
severely compounded by a linguistic bias that per-
meates the field. Despite the global nature of this
problem, the vast majority of research and techno-
logical progress remains overwhelmingly Anglocen-
tric, relying on models trained with informal English
data scraped from a handful of platforms (Jahan
and Oussalah, 2023). This imbalance creates a
significant performance gap, as these models fail
to generalize across different linguistic and cultural
contexts, not only restricting the development of uni-
versally effective moderation tools but also leaves
speakers of most languages, particularly those in
low-resource settings, disproportionately vulnera-
ble to online toxicity (Kargaran et al., 2024).
These interconnected issues of data granularity
and linguistic focus are particularly pronounced in
the Portuguese context. Most existing datasets
provide only only binary toxic or non-toxic annota-
tions, while the few works that attempt to identify
protected groups are often limited to dozens or
hundreds of such labeled samples (De Pelle and
Moreira, 2017; Leite et al., 2020). Critically, these
datasets focus exclusively on negative samples tar-
geting minority groups, failing to include sufficient
non-toxic counterexamples (i.e., benign text about
these groups). This omission fundamentally limits
a model’s ability to distinguish genuine hate from
mere discussion.
In addition, current existing datasets suffers from
a severe domain confinement. The vast majority
of available Portuguese data is drawn from social
media, a domain whose linguistic patterns (e.g.,
brevity, slang) differ markedly from other contexts
where toxicity manifests, such as news commen-
tary or transcribed dialogues. This reliance on a
single, informal domain, combined with the afore-
mentioned lack of label granularity, severely limits
the ability of current Portuguese classifiers and
arXiv:2506.10245v2  [cs.CL]  14 Nov 2025

--- Page 2 ---

benchmarks.
To address this gap, we introduce ToxSyn, a
large-scale synthetic dataset for Portuguese hate
speech detection, allowing train and evaluate lan-
guage models on both binary and targeted-group fo-
cused toxicity. Comprising 53,274 LLM-generated
samples annotated for toxicity, discourse type, and
target group, ToxSyn covers nine protected com-
munities, including racial, religious, gender, and
ability-based categories, all underrepresented in
existing datasets. To the best of our knowledge, it
is the first corpus in Portuguese explicitly designed
to support hate-speech detection across multiple
protected groups. As illustrated in Figure 1, the
dataset is produced through a controlled four-stage
generation pipeline that ensures broad coverage of
both overt and subtle hate expressions while bal-
ancing label frequencies and rhetorical variation.
We assess the effectiveness of ToxSyn by fine-
tuning toxicity classifiers and testing them on both
general and group-specific detection tasks. The
results show that Portuguese toxicity detection mod-
els are strongly domain-dependent, performing well
within their training domain but showing substantial
degradation in out-of-domain settings. This find-
ing highlights the need for robust, balanced, and
minority-aware datasets to achieve reliable gen-
eralization across diverse linguistic domains and
demographic targets.
The main contributions of this work are:
1. We introduce ToxSyn, the first Portuguese pub-
licly available corpus designed to support hate-
speech classification across multiple minor-
ity targets, comprising over 50K synthetic in-
stances annotated with toxicity, target group,
and discourse-type labels
2. We present a controllable LLM-based data
generation pipeline that allows for balancing
class distributions, injecting low-frequency ex-
pressions, and applying safety constraints.
3. We demonstrate that toxicity detection in Por-
tuguese is strongly domain-dependent, with
model performance degrading sharply when
applied to out-of-distribution contexts.
2.
Related Works
Synthetic corpora have been explored as a means
to augment limited hate speech datasets. ToxiGen
(Hartvigsen et al., 2022) combines a classifier-in-
the-loop framework with GPT-3 (Brown et al., 2020)
to adversarially generate over 250,000 examples
across 13 demographic targets, yielding measur-
able improvements in classification performance.
ToxiCraft (Hui et al., 2024) extends this line of work
by using GPT-4 (Achiam et al., 2023) with struc-
tured prompting and self-evaluation to generate text
with greater controllability. Despite their technical
sophistication, both approaches are constrained to
English, which limits their applicability to languages
that differ in sociolinguistic norms and expressions
of toxicity.
In the context of Portuguese, HateBR (Vargas
et al., 2022) provides a multilabel dataset of 7,000
Instagram comments, annotated for binary of-
fensiveness, severity (in three levels), and nine
hate speech categories. Although the annotation
schema is comprehensive, the category distribu-
tion is highly uneven: only 727 category labels are
assigned in total, with 496 corresponding to party-
ism and fewer than 100 for any other class (e.g.,
just two antisemitic samples and a single exam-
ple of xenophobic text). This imbalance limits the
dataset’s utility for training models with generaliza-
tion capacity.
Several additional Portuguese-language corpora
have been proposed, but often suffer from limited
scale and class coverage. OFFCOMBR-3 (De Pelle
and Moreira, 2017) includes 1,250 comments anno-
tated across six categories by three annotators, but
only 19.5% of the samples are toxic and most cat-
egories have very few labeled instances marking
harmful content against a minority group. ToLD-BR
(Leite et al., 2020) provides annotations for four mi-
nority classes but includes less than 30 examples
per class. OLID-BR (Trajano et al., 2024) improves
on label balance by annotating between 92 and 461
samples per category across five target classes.
Still, the dataset size remains limited for training
deep learning models without additional data aug-
mentation.
TuPy-E (Oliveira et al., 2023) merges three an-
notated Portuguese corpora (Fortuna et al., 2019;
Leite et al., 2020; Vargas et al., 2022) with the TuPy
dataset into a unified collection of 43,668 social-
media comments. Of these, 11,547 are labeled as
toxic, and only 3,327 carry annotations indicating of-
fense toward a protected minority1. Although TuPy-
E’s multilabel schema spans nine categories (e.g.,
ageism, aporophobia, capacitism, LGBT-phobia),
its utility is undermined by severe class imbalance:
some categories are represented by fewer than one
hundred instances (e.g. ageism and aporophobia
has 57 and 66 examples, respectively), whereas
there is categories such as misogyny that com-
prises 1,675 samples. This extreme sparsity de-
grades the performance of encoder-based multi-
label classifiers in the original study, highlighting
the urgent need for larger, more evenly distributed
resources to train and evaluate robust hate-speech
detection models in Portuguese.
Additionally, existing Portuguese corpora exhibit
1Although TuPy-E contains Political hate category, we
disconsider it since this class do not offend any minority
group.

--- Page 3 ---

Obtain a seed dataset that
comprises the core to
generation process.
1) Seed Dataset
2) Prompt-Based Expansion
3) Paraphrase Augmentation
4) Enrichment
Few‑shot prompting
creates minority‑focused
sentences based on
predefined strategies.
Dual paraphrase
augmentation triples
corpus size and stylistic
variety.
Enrich with implicit‑hate
variants using the
generated dataset.
Figure 1: Overview of ToxSyn generation pipeline, comprising seed dataset, prompt-based expansion,
paraphrase augmentation, and enrichment.
an additional blind spot: they annotate only hostile
mentions of protected groups and omit neutral or
supportive references. Consequently, a sentence
that praises Black resilience or affirms LGBTQIA+
rights is either absent or, at best, indistinguishable
from non-minority content. This omission prevents
classifiers from learning the difference between the
absence of hate and the presence of endorsement,
limiting applications such as allyship detection and
fine-grained content moderation in both formal and
informal domains. Filling this gap is essential for
building context-aware systems that recognise not
just toxicity, but also positive engagement with mi-
nority communities.
3.
ToxSyn
This section describes the construction of ToxSyn,
a large-scale dataset designed to provide compre-
hensive coverage of minority-targeted hate speech
in Portuguese. Our approach emphasizes con-
trolled representation of protected groups and lin-
guistic diversity across both toxic and non-toxic
expressions. The dataset is produced through a
structured four-stage generation pipeline, designed
to ensure broad coverage of different target commu-
nities while capturing a range of implicit and explicit
toxic language. To further enhance generalization
and reduce potential overfitting to specific groups,
we also incorporate neutral content unrelated to mi-
nority identity, increasing topical variety across the
dataset. Detailed descriptions of each stage of the
pipeline are provided in the following subsections.
3.1.
Seed Dataset
We hypothesize that exposing a language model to
a rich spectrum of perspectives and expressions of
toxicity for a compact set of minority targets enables
better generalization to additional, unseen commu-
nities. Guided by this principle, we constructed a fo-
cused seed dataset centered on two targets: Black
people and women. Selecting a small set of groups
allowed us to pursue depth over breadth, systemat-
ically exploring intra-group variation in how hostility,
positivity and neutrality are expressed while keep-
ing the seed compact and semantically coherent
for use as in-context demonstrations during later
prompt-based expansion.
Concretely, the seed comprises 40 toxic and 40
non-toxic examples for each target, finalizing with
160 sentences in total. Examples were crafted to
vary across multiple axes (i.e. tone, topical content,
and syntactic structure), maximizing intra-group
diversity and providing clear positive and counter-
factual instances that help the model distinguish
targeted hostility from benign references. These
high-quality seed examples form the foundation
for our subsequent controlled LLM generation and
augmentation stages.
3.2.
Prompt-Based Expansion
In this stage, we employ GPT-4o Mini (Achiam et al.,
2023) in a few-shot prompting configuration to gen-
erate new samples conditioned on minority identity.
The model is prompted with representative seed
examples and instructed to produce linguistically
diverse toxic and non-toxic statements for one of
nine target communities: Black people, Jews, Mus-
lims, Indigenous Brazilians, women, LGBTQIA+
individuals, elderly people, and people with disabil-
ities. These categories were selected to achieve
both broad demographic coverage and equitable
representation of groups that are typically under-
sampled or totally absent from existing Portuguese
hate-speech datasets.
To ensure wide topical and stylistic coverage
across all minorities, we developed 26 distinct gen-
eration templates (14 non-toxic, 12 toxic) that sys-
tematically vary the ideological frame and tone of
the outputs. For example, applying Real Problems
Minimization toxic template guides the model to
downplay the hardships of marginalized communi-
ties, whereas the non-toxic template Problem Ac-
knowledgment promotes constructive framing of
societal challenges. To further enhance textual
diversity, each generation prompt also includes a
randomized length constraint (short, medium, or
long).
To guarantee both representational balance and
conceptual robustness, we ensured that the final
dataset was evenly distributed across the binary
toxicity labels (toxic vs. non-toxic) and all nine de-
mographic groups. This deliberate sampling design
not only prevents asymmetric group representation
but also supports fairer evaluation of language mod-
els across demographic dimensions. The resulting

--- Page 4 ---

corpus comprises 10,790 unique sentences that
combine linguistic richness with demographic di-
versity, forming a solid foundation for subsequent
stages of large-scale synthetic expansion.
3.3.
Paraphrase Augmentation
To further enrich lexical and pragmatic variation,
each sentence produced in the expansion stage
was paraphrased twice: once through a toxic and
once through a non-toxic transformation. These
transformations, randomly sampled from prede-
fined strategy pools, introduce diverse rhetorical
and stylistic shifts that reflect how toxicity and neu-
trality manifest in natural discourse. Toxic trans-
formations simulate linguistic mechanisms such
as victim-blaming, ambiguous framing, appeal to
authority, and hyperbolic exaggeration, while non-
toxic transformations leverage strategies like ques-
tioning, contrastive emphasis, nuanced ambiguity,
and positive negation. This procedure enhances
linguistic heterogeneity and pragmatic realism, pro-
viding the model with broader exposure to the sub-
tle ways toxicity and neutrality are expressed.
Because our transformations are applied sym-
metrically (i.e., non-toxic rewriting patterns are ap-
plied to originally toxic inputs and toxic patterns to
originally non-toxic inputs), we frequently obtain
instances that are effectively detoxified yet retain
residual pragmatic or referential ambiguity regard-
ing intent and target. These ambiguous examples
increase the corpus realism by reflecting positive
text but with terms usually associated with natu-
ral hostility discourse. Consequently, they serve
as valuable edge cases: they reduce reliance on
lexical heuristics, encourage models to exploit con-
textual and pragmatic cues, and provide hard nega-
tives/positives useful for robustness and calibration
analyses.
Furthermore, our paraphrasing process enabled
systematic swapping of the original minority tar-
get across the nine predefined groups.
How-
ever, LLMs outputs occasionally hallucinated un-
supported targets or produced non-standard sur-
face forms. To enforce consistency, we applied a
regular-expression based normalization that maps
variant forms to our nine canonical labels (e.g., all
“immigrant from *” variants were mapped to “immi-
grant”). This normalization resulted in the discard-
ing of approximately 8% of generated sentences
that lacked a valid mapping.
After normalization and filtering, the stage
yielded 20,799 additional paraphrases.
When
these paraphrases are combined with the original
samples, the corpus achieves 14,521 toxic and
17,068 non-toxic instances, a total of 31,589 ex-
emplars. These procedures substantially broaden
ToxSyn’s stylistic and rhetorical diversity while pre-
serving precise minority-target annotations.
3.4.
Enrichment
In the final generation round we repeat the few-
shot procedure from Section 3.2, but draw our
in-context examples from the 31,589 sentences
produced rather than the 160 examples from the
original seed dataset. By exposing GPT-4o Mini
(Achiam et al., 2023) to this richer demonstration
pool, already populated with a spectrum of explicit
and implicit rhetoric, we encourage the model to
imitate a broader range of discourse styles while
preserving the label fidelity established earlier.
To further broaden the corpus’s coverage of im-
plicit hate speech, we extend the template cata-
logue from 26 to 28 by adding two new toxic pat-
terns: Ambiguous Prejudice (double-meaning lan-
guage to convey prejudice in an implicit but percepti-
ble way) and Justification Prejudice (frames discrim-
inatory attitudes as ostensibly reasonable, present-
ing bias as a matter of common sense, economic
necessity, or cultural tradition). Although earlier
stages included implicit hate, these two templates
diversify the rhetorical tactics used to conceal prej-
udice, producing harder-to-classify examples that
increase the dataset’s linguistic complexity.
Applying all 28 generation templates to the en-
riched prompt pool yields a final minority-targeted
corpus of 50,074 sentences, in which 24,707 are
toxic and 25,367 are non-toxic examples. This com-
prehensive collection captures a continuum of hate-
ful expression, from overt slurs to subtle and covert
prejudice, providing a richly annotated dataset for
Portuguese hate-speech research.
3.5.
Neutral Samples
To improve generalization to content where demo-
graphic cues are absent, we design a two-phase
neutral-text augmentation module.
In Phase 1,
we curate 60 fully neutral seed sentences and ex-
pand each via a five-shot prompting routine using
four randomly chosen domain templates (conversa-
tional, news, policy, and academic). Each five-shot
input return five new samples as output, resulting
in 300 domain-varied variants.
In Phase 2, we further diversify those 300 sen-
tences through 20 distinct style-transformation
prompts, ranging from social-media vernacular to
formal editorials, resulting on 6,000 neutral candi-
dates. To maintain emphasis on minority-targeted
hate speech, we stratify this pool by seed, domain,
and style, then uniformly sample 3,200 sentences
for integration. This procedure injects rich topical
and stylistic diversity while preserving the dataset’s
core focus on protected-group samples.

--- Page 5 ---

Group
Train Count
Test Count
Total
Black
Toxic
2,688
302
2,990
Non-toxic
2,714
304
3,018
Count
5,402
606
6,008
Women
Toxic
2,703
304
3,007
Non-toxic
2,307
256
2,563
Count
5,010
560
5,570
LGBTQIA+
Toxic
2,653
294
2,947
Non-toxic
2,668
299
2,967
Count
5,321
593
5,914
Native Brazilian
Toxic
2,615
290
2,905
Non-toxic
2,659
295
2,954
Count
5,274
585
5,859
Muslim
Toxic
2,601
288
2,889
Non-toxic
2,592
286
2,878
Count
5193
574
5,767
Jewish
Toxic
2,514
278
2,792
Non-toxic
2,569
284
2,853
Count
5,083
562
5,645
Elderly
Toxic
2,039
226
2,265
Non-toxic
2,433
269
2,702
Count
4,472
495
4,967
Disable People
Toxic
2,400
266
2,666
Non-toxic
2,489
275
2,764
Count
4,889
541
5,430
Immigrants
Toxic
2,022
224
2,246
Non-toxic
2,400
268
2,668
Count
4,422
492
4,914
Neutral
Toxic
0
0
0
Non-toxic
3,000
200
3,200
Total
48,066
5,208
53.274
Table 1: Final ToxSyn distribution per group.
3.6.
Human Annotation
To create a high-quality, human-verified benchmark,
we constructed a test set of 5,208 examples. This
set was composed of 200 neutral samples and
a 10% sample of the generated minority-targeted
data (5,008 examples). To ensure comprehensive
representation of our fine-grained categories, this
sample was stratified across the Toxic Label, Mi-
nority, and Discourse Type features.
We employed a red team of four native
Portuguese-speaking annotators. To ensure an un-
biased gold standard and prevent the cognitive bias
introduced by pre-annotation (Beck et al., 2025),
annotators were kept blind to the machine labels,
annotating from scratch all 5,208 samples from the
raw text. This approach served a dual purpose: 1)
to efficiently produce a gold-standard test set and
2) to directly quantify the quality of our synthetic
generation pipeline.
The results of this validation strongly affirm the
high fidelity of our synthetic data. The human an-
notators modified around 7% of the primary toxi-
city labels and fewer than 1% of the specific mi-
nority target labels. This high level of agreement
between the generated labels and the final human-
adjudicated data demonstrates the robustness and
accuracy of our controllable pipeline.
3.7.
Final Dataset
The final ToxSyn corpus distribution is shown in
Table 1. It comprises 53,274 synthetic sentences,
including 24,707 toxic examples and 25,367 non-
toxic sentences referencing minority groups, and
3,200 non-toxic neutral samples, resulting in a near-
balanced split (46% toxic vs. 54% non-toxic), with
each of the nine protected groups represented by at
least 4,914 instances and at most 6,008 samples.
Every entry is annotated for Toxic Label, Minority,
and Discourse Type, supporting both supervised
model training and corpus-level analyses. In Ta-
ble 2, we contrast ToxSyn’s source, group cover-
age, and sample counts with existing Portuguese
datasets. Representative examples illustrating di-
versity in target, toxicity, and discourse style are
provided in Table 3.
4.
Experiments
We evaluate the effectiveness of the ToxSyn
dataset under two classification settings: (1) multi-
domain classification, which determines whether
a given text is toxic or non-toxic in both general
and minority targeted benchmarks, and (2) group-
specific classification, in which we assess each
protected group separately by considering a text as
belonging to the target group only when its toxicity
is directed toward that group, while texts that are
non-toxic or toxic toward other groups are treated
as not belonging to it.
Given the lack of Portuguese benchmarks with
detailed multi-label annotations, we translated the
human-annotated portion of ToxiGen (Hartvigsen
et al., 2022) into Portuguese using GPT-4 (Achiam
et al., 2023). These experiments aim to assess the
impact of synthetic data generated by our pipeline
across multiple evaluation settings and model ca-
pacities.
4.1.
Experimental Setup
Implementation.
All experiments were con-
ducted on a single NVIDIA RTX 4090 GPU using
the Hugging Face Transformers library2. We used
a batch size of 32, a learning rate of 5e-5 with linear
2https://huggingface.co/

--- Page 6 ---

Datasets
Source
Groups
Target
OffcomBR-3
News comments
6
19
ToLD-BR
Twitter
4
124
HateBR
Instagram
9
727
OlidBR
Social media
5
1,390
Tupy-E
Social media
9
3,742
ToxSyn (ours)
Controlled generation
9
50,074
Table 2: Comparison of hate-speech datasets in
Portuguese by source, number of target groups,
and number of samples targeting a minority group.
scheduling, and no weight decay. All runs were per-
formed with fixed random seed 42. Models were
trained for 3 epochs.
Model.
For both multi-domain and group-specifi
tasks, we fine-tuned the BERTimbau base model
(Souza et al., 2020), which has demonstrated
strong performance in prior Portuguese NLP bench-
marks (da Silva Oliveira et al., 2024).
Classification.
In the multi-domain classification
setup, the model was trained using all training ex-
amples considering only if the sample was toxic or
non-toxic, discarding group labels. For the group-
specific classification setting, we constructed train-
ing sets: for each group, we retained all toxic sam-
ples targeting that group and sampled 3,000 coun-
terexamples: 1,000 non-toxic samples from the
same group, 1,000 toxic samples from other groups,
and 1,000 non-toxic samples from other groups or
neutral content.
4.2.
Evaluation Benchmarks
Existing Portuguese hate-speech corpora are in-
sufficient for robust target-group evaluation: each
individual dataset contains only tens to hundreds
of examples per protected class, far too few to sup-
port reliable performance assessment. To mitigate
this, we concatenate the principal public datasets
that contain group annotations (HateBR (Vargas
et al., 2022), OFFCOMBR-3 (De Pelle and Moreira,
2017), OLID-BR (Trajano et al., 2024), and TuPy-E
(Oliveira et al., 2023)) and merging related groups
to increase the number of test samples (for ex-
ample, all nationality-based groups were grouped
under immigrants; Antisemitic and Islamophobic
references were subsumed into religious intoler-
ance). This results in 6,002 total samples, of which
2,318 share at least one protected-group label with
ToxSyn. For simplicity, we mention this set as Por-
tuguese Merged in the rest of the paper.
To improve minority coverage for evaluation, we
translate the human-annotated portion of ToxiGen
(Hartvigsen et al., 2022). This set contains multi-
label examples for six protected groups that are
also present in ToxSyn. The resulting dataset con-
tains 8,960 samples of both toxic and non-toxic text
mentioning specific groups, of which 6,166 sam-
ples contains minority groups label that intersects
with ToxSyn.
Although Portuguese Merged set constitutes
the largest multi-label test set for hate speech
in Portuguese, it is constrained by its informal
social-media register and by only marking protected
groups when content is toxic; neutral or supportive
references remain unlabeled, and no existing cor-
pus covers enough minority-targeted examples for
training. The translated ToxiGen dataset mitigates
some of these gaps by supplying formal, multi-label
examples, but it introduces unnaturalized phrasing
and culturally mismatched slurs (for instance, the
English “watermelon” stereotype against Black peo-
ple does not translate meaningfully in Portuguese).
4.3.
Multi-Domain Classification
To assess cross-domain generalization, we fine-
tuned BERTimbau on the full training sets of ToLD-
BR, HateBR, OLID-BR, and our ToxSyn. We then
evaluated each model on the test sets of all other
benchmarks, including the minority-focused Toxi-
Gen dataset.
We report two key metrics (Table 4): Macro
F1-score (to balance precision and recall across
classes) and Toxic-Class Recall (to measure the
model’s core ability to identify harmful content). The
results reveal a strong, mutual generalization fail-
ure between general social media domains and
minority-focused domains.
This failure is most evident in the Toxic-Class
Recall scores. Models trained on general social
media fail catastrophically when tested on minority-
focused data. For instance, the model trained on
ToLD-BR predicts almost all inputs as non-toxic,
identifying only 10 from a total of 2,472 toxic sam-
ples present in the test set. The best-performing
social media model (OLID-BR) still only identified
20% of toxic samples in ToxSyn and 19% in Toxi-
Gen. This finding demonstrates that these models
overfit to their source domains and are incapable
of identifying hate speech when it appears in a dif-
ferent context (e.g., more formal text or different
rhetorical styles).
Crucially, this failure is reciprocal. The model
trained on ToxSyn also struggles to detect toxicity
in the general-domain corpora, achieving a toxic-
class recall of only 0.17 on ToLD-BR and 0.51 on
HateBR. This indicates that the stylistic and lin-
guistic patterns of toxicity differ significantly across
domains.
However, the ToxSyn-trained model generalizes
effectively to other minority-focused dataset, achiev-
ing a strong 0.69 F1-score and 0.77 Toxic-Class Re-
call on ToxiGen. This suggests that while it does not

--- Page 7 ---

Comment
Offensive
Minority
Discourse Type
Os muçulmanos frequentemente clamam por respeito, mas será que sua história de
conflitos não complica essa busca por aceitação?
Translation: Muslims often call for respect, but doesn’t their history of conflicts complicate
this quest for acceptance?
Yes
Muslims
Ambiguous Prejudice
Se as mulheres realmente quisessem ajudar, ao invés de criarem mais divisão, poderiam
ter contribuído positivamente para os movimentos sociais.
Translation: If women truly wanted to help, instead of creating more division, they could
have contributed positively to social movements.
Yes
Women
Victim Blaming
Não se pode ignorar que a comunidade judaica é frequentemente reconhecida por sua
resiliência, mesmo em situações desafiadoras.
Translation: It cannot be ignored that the Jewish community is often recognized for its
resilience, even in challenging situations.
No
Jewish
Positive Negation
Às vezes, dá até um nó na cabeça ver a rapidez que as fofocas rolam nas redes sociais,
mas é massa perceber como isso mexe com a cabeça da galera.
Translation: Sometimes it’s mind-boggling how fast gossip spreads on social media, but
it’s cool to see how it really messes with people’s minds.
No
Neutral
-
Table 3: Samples from ToxSyn labeled with Hate-Speech, Minority and Discourse Type. In regionalism
discourse, it is possible to see some Brazilian Portuguese slugs.
generalize to all domains, it successfully learned
the underlying patterns of group-targeted hate, al-
lowing it to transfer to another dataset with a similar
minority-focused objective.
Overall, these findings underscore that toxi-
city detection in Portuguese is highly domain-
dependent. While models trained on social me-
dia achieve adequate toxic-class recall in-domain
(at least 0.60), their performance collapses out-of-
domain (dropping to 0.20 or, in some cases, near-
zero). This massive reliability gap highlights the crit-
ical need for robust, balanced, and minority-aware
datasets to benchmark progress and build models
that can generalize beyond their narrow training
contexts.
Test Data
Finetune Data
ToLD-BR
HateBR
OLID-BR
ToxSyn (Ours)
F1-Score
ToLD-BR
0.79
0.69
0.80
0.46
HateBR
0.77
0.91
0.63
0.46
OLID-BR
0.60
0.62
0.69
0.42
ToxiGen*
0.41
0.46
0.48
0.69
ToxSyn (Ours)*
0.35
0.36
0.37
0.94
Recall
ToLD-BR
0.78
0.78
0.95
0.17
HateBR
0.60
0.89
0.91
0.51
OLID-BR
0.70
0.88
0.94
0.47
ToxiGen*
0.09
0.17
0.19
0.77
ToxSyn (Ours)*
0.00
0.18
0.20
0.94
Table 4: Cross-domain generalization results. We
report Macro F1-score and Recall for the Toxic
class. Datasets marked with * belong to the do-
main of group-targeted data.
4.4.
Group-Specific Classification
We next evaluated our ToxSyn-trained model’s abil-
ity to perform fine-grained, multi-label classification
of which protected group is being targeted. We
tested it on Portuguese Merged and the translated
subset of ToxiGen. A critical challenge in this eval-
uation is that existing Portuguese datasets contain
only toxic instances for each minority group, lack-
ing any neutral or benign counterexamples. This
data structure makes precision-based metrics like
F1-score mathematically unreliable, as there are
no true negatives for the group-specific task. We
therefore report Macro Recall, which properly mea-
sures the model’s sensitivity to detecting targeted
hate. This resource gap is a key finding: it was not
possible to train any comparable minority-aware
baselines from public Portuguese data, highlight-
ing the novelty of our work.
As shown in Table 5, the ToxSyn-trained model
achieves a strong average macro recall of 0.70
on the translated ToxiGen set, reflecting the close
conceptual alignment between the two minority-
focused resources. The model achieves a mod-
erate 0.64 macro recall on Portuguese Merged,
demonstrating a solid capability to transfer its knowl-
edge to the noisier, out-of-domain social media con-
text. However, the performance on this set varies
significantly across groups, often correlating with
data scarcity (e.g., 0.80 recall for "Religious" with
68 samples vs. 0.54 for "Elderly" with 44 samples).
These results confirm that ToxSyn can serve as a
foundational resource for training robust, minority-
aware models in Portuguese, while also highlight-
ing the need for more balanced, multi-group data
collection.
5.
Discussion
Our experiments reveal a profound domain de-
pendency in Portuguese toxicity detection. The
cross-domain evaluation demonstrates a mutual
and catastrophic generalization failure: models

--- Page 8 ---

Group
Macro-Recall
Support
PT Merged
Black
0.63
230
Women
0.63
961
LGBTQIA+
0.64
734
Religious
0.80
68
Elderly
0.54
44
Immigrants
0.59
281
Average
0.64
-
ToxiGen
Black
0.72
713
Women
0.74
717
LGBTQIA+
0.67
714
Muslim
0.69
688
Jewish
0.76
688
Immigrants
0.60
2,646
Average
0.70
-
Table 5: Group-specific classification performance
per target group on ToxiGen Translated and Por-
tuguese Merged.
trained on general social media corpora are in-
capable of detecting minority-targeted hate and,
conversely, our ToxSyn-trained model, while highly
effective in its own domain, also fails to generalize
to general-domain datasets. This mutual failure
strongly suggests that toxicity is not a monolithic
concept. The rhetorical and contextual patterns of
minority-targeted hate are fundamentally different
from the lexical cues of social-media insults. This
finding exposes a critical methodological pitfall in
toxicity evaluation: Macro F1 scores are danger-
ously deceptive, as they completely mask a model’s
total failure to perform its primary task.
Given this domain-specificity, the primary con-
tribution of ToxSyn is not as a general-purpose
solver, but as the first resource to enable a pre-
viously impossible task in Portuguese: building
and evaluating fine-grained, minority-aware mod-
els. Our group-specific experiments underscored
this, as the lack of non-toxic counterexamples in
all other public corpora made it impossible to even
train comparable baselines.
ToxSyn’s success in this task, and its ability
to generalize to other minority-focused dataset,
is a direct result of our controllable generation
pipeline. By systematically creating fine-grained
annotations (discourse types, target groups) and,
crucially, their corresponding detoxified counterex-
amples, we compel the model to learn the deeper
contextual features that distinguish genuine harm
from benign discussion of identity, rather than brit-
tle, surface-level heuristics.
6.
Conclusion
In this paper, we introduced ToxSyn, a large-scale,
fine-grained synthetic dataset that fundamentally
addresses a critical resource gap in Portuguese.
It is the first Portuguese corpus to enable the fine-
grained classification of hate against specific mi-
nority groups, a task previously impossible due to
the critical absence of non-toxic counterexamples
in all other public data. Our controllable four-stage
pipeline was designed to systematically generate
these balanced and nuanced instances, providing
a unique resource for the community.
Our empirical investigation using ToxSyn re-
vealed that toxicity detection is not a monolithic
problem. We demonstrated a catastrophic, mutual
generalization failure between general-domain and
minority-targeted hate speech, proving that even
within the general toxicity domain, there are mul-
tiple manifests of harmful content and, therefore,
multiple sub-domains. This finding also serves as
a crucial methodological warning: our results show
that summary metrics like Macro F1 are danger-
ously deceptive, as they can completely mask a
model’s total failure to detect the target toxic class.
We thus argue that future benchmarks must in-
corporate more granular metrics. Our generation
pipeline provides a generalizable blueprint for cre-
ating such resources, and we release ToxSyn as
a new benchmark to foster more rigorous, context-
aware evaluation in the pursuit of genuinely equi-
table online safety.
7.
Future Work
Our work on ToxSyn opens several promising av-
enues for future research. First, our four-stage gen-
eration pipeline serves as a generalizable blueprint.
A clear next step is to adapt this methodology to
other low-resource languages that face similar data
scarcity, enabling the creation of fine-grained, bal-
anced hate speech corpora globally. Second, our
experiments confirmed a severe, mutual general-
ization failure between social-media and minority-
focused domains. Future work should focus on
bridging this domain gap. This could involve do-
main creating hybrid datasets that mix different do-
mains to train a single, robust classifier that oper-
ates effectively across diverse linguistic contexts.
Third, our dataset contains rich discourse-type la-
bels (e.g., Ambiguous Prejudice, Justification Prej-
udice). While we used these for generation and
stratification, they remain an untapped resource.
Training models to explicitly classify these rhetorical
strategies, moving beyond if a text is toxic to how
and why it is toxic, would enrich the research in the
field. Finally, while ToxSyn is validated against hu-
man annotation, it remains a synthetic resource. A
crucial next step is to address this gap by collecting
in-the-wild, human-authored data and annotating it
using ToxSyn’s detailed, multi-label schema.

--- Page 9 ---

8.
Limitations
While ToxSyn substantially advances Portuguese
hate-speech resources, it carries several impor-
tant caveats. First, each sentence is annotated
with a single target group, precluding the analysis
of intersectional or multi-target cases; overlapping
abuses (e.g., simultaneously sexist and racist lan-
guage) thus remain unmodeled. Second, the cor-
pus lacks severity tiers (e.g., mild versus severe
toxicity), which limits studies requiring fine-grained
harm assessment. Third, our four-stage genera-
tion pipeline relies on a fixed set of prompts and
normalization rules. Although this ensures control
and class balance, it may constrain the emergence
of novel or context-specific hate-speech patterns
not captured in our templates.
Moreover, as a fully synthetic dataset, ToxSyn
inherits potential biases from the underlying LLM,
including repetitive phrasing and distributional arti-
facts that may diverge from authentic human lan-
guage. Finally, while our human-in-the-loop vali-
dation of the 5,208 sample test set allowed us to
quantify the pipeline’s high fidelity, the remaining
training samples did not undergo this same rigor-
ous human review and may contain a similar level
of labeling noise.
9.
Ethics Statement
The use of generative models to create synthetic
toxic data must be approached with great caution
to prevent harmful applications, such as deliber-
ately offending minority groups or training language
models to produce hate speech. Nevertheless, re-
sponsible use of this methodology can significantly
enhance online communication by improving the
identification of toxic content and specifying the
particular minority groups being targeted. To en-
sure ethical deployment, applications that intend
to use ToxSyn should be validated by a under mul-
tidisciplinary team, providing critical guidance on
responsible usage and preventive measures for
potential misuse.
10.
Bibliographical References
Josh Achiam,
Steven Adler,
Sandhini Agar-
wal,
Lama
Ahmad,
Ilge
Akkaya,
Floren-
cia Leoni Aleman, Diogo Almeida, Janko Al-
tenschmidt, Sam Altman, Shyamal Anadkat, et al.
2023.
Gpt-4 technical report.
arXiv preprint
arXiv:2303.08774.
Aish Albladi, Minarul Islam, Amit Das, Maryam Big-
onah, Zheng Zhang, Fatemeh Jamshidi, Mostafa
Rahgouy, Nilanjana Raychawdhary, Daniela
Marghitu, and Cheryl Seals. 2025. Hate speech
detection using large language models: A com-
prehensive review. IEEE Access.
Jacob Beck, Stephanie Eckman, Christoph Kern,
and Frauke Kreuter. 2025.
Bias in the loop:
How humans evaluate ai-generated suggestions.
arXiv preprint arXiv:2509.08514.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sas-
try, Amanda Askell, et al. 2020. Language mod-
els are few-shot learners. Advances in neural
information processing systems, 33:1877–1901.
Amanda da Silva Oliveira, Thiago de Carvalho Ce-
cote, João Paulo Reis Alvarenga, Vander Luis
de Souza Freitas, and Eduardo José da Silva Luz.
2024.
Toxic speech detection in portuguese:
A comparative study of large language models.
In Proceedings of the 16th International Con-
ference on Computational Processing of Por-
tuguese, pages 108–116.
Thomas Hartvigsen,
Saadia Gabriel,
Hamid
Palangi, Maarten Sap, Dipankar Ray, and Ece
Kamar. 2022. ToxiGen: A large-scale machine-
generated dataset for adversarial and implicit
hate speech detection. In Proceedings of the
60th Annual Meeting of the Association for Com-
putational Linguistics (Volume 1: Long Papers),
pages 3309–3326, Dublin, Ireland. Association
for Computational Linguistics.
AH Kargaran, A Modarressi, N Nikeghbal, J Dies-
ner, F Yvon, and H Schutze. 2024. Mexa: Multilin-
gual evaluation of english-centric llms via cross-
lingual alignment. arxiv. Org, abs/2410.05873.
Fábio Souza, Rodrigo Nogueira, and Roberto
Lotufo. 2020. Bertimbau: pretrained bert models
for brazilian portuguese. In Brazilian conference
on intelligent systems, pages 403–417. Springer.
Maheshya
Weerasinghe,
Shaun
Macdonald,
Cristina
Fiani,
Joseph
O’Hagan,
Mathieu
Chollet, Mark McGill, and Mohamed Khamis.
2025. Beyond mute and block: adoption and
effectiveness of safety tools in social vr, from
ubiquitous harassment to social sculpting. IEEE
Transactions on Visualization and Computer
Graphics.

--- Page 10 ---

11.
Language Resource References
De Pelle, Rogers Prates and Moreira, Viviane P.
2017. Offensive comments in the brazilian web:
a dataset and baseline results. SBC.
Fortuna, Paula and Rocha da Silva, João and Soler-
Company, Juan and Wanner, Leo and Nunes,
Sérgio. 2019.
A Hierarchically-Labeled Por-
tuguese Hate Speech Dataset. Association for
Computational Linguistics.
Hartvigsen, Thomas and Gabriel, Saadia and
Palangi, Hamid and Sap, Maarten and Ray, Di-
pankar and Kamar, Ece. 2022. ToxiGen: A Large-
Scale Machine-Generated Dataset for Adversar-
ial and Implicit Hate Speech Detection. Associa-
tion for Computational Linguistics.
Hui, Zheng and Guo, Zhaoxiao and Zhao, Hang
and Duan, Juanyong and Huang, Congrui. 2024.
Toxicraft: A novel framework for synthetic gener-
ation of harmful information.
Jahan, Md Saroar and Oussalah, Mourad. 2023.
A systematic review of hate speech automatic
detection using natural language processing. El-
sevier.
Leite,
João Augusto and Silva,
Diego and
Bontcheva, Kalina and Scarton, Carolina. 2020.
Toxic Language Detection in Social Media for
Brazilian Portuguese: New Dataset and Multi-
lingual Analysis. Association for Computational
Linguistics.
Oliveira, Felipe and Reis, Victoria and Ebecken,
Nelson. 2023. TuPy-E: detecting hate speech in
Brazilian Portuguese social media with a novel
dataset and comprehensive analysis of models.
Trajano, Douglas and Bordini, Rafael H and Vieira,
Renata. 2024.
OLID-BR: offensive language
identification dataset for Brazilian Portuguese.
Springer.
Vargas, Francielle and Carvalho, Isabelle and Ro-
drigues de Góes, Fabiana and Pardo, Thiago
and Benevenuto, Fabrício. 2022.
HateBR: A
Large Expert Annotated Corpus of Brazilian In-
stagram Comments for Offensive Language and
Hate Speech Detection. European Language
Resources Association.

```
