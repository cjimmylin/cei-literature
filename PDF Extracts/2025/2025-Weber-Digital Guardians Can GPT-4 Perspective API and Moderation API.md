---
title: "2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API - PDF Extract"
source_pdf: "2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API.pdf"
pages: 10
extracted_at: "2026-02-13T13:14:08.052603"
---

# PDF Extract: 2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API

**Source PDF:** 2025-Weber-Digital Guardians Can GPT-4 Perspective API and Moderation API.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Digital Guardians:
Can GPT-4, Perspective API, and Moderation API reliably detect
hate speech in reader comments of German online newspapers?
Manuel Weber, Moritz Huber, Maximilian Auch,
Alexander Döschl*, Max-Emanuel Keller, Peter Mandl
HM Hochschule München University of Applied Sciences
Lothstraße 64, 80335 München, Germany
*Corresponding author: alexander.doeschl@hm.edu
Abstract
In recent years, toxic content and hate speech have become widespread phenomena on the internet. Moderators
of online newspapers and forums are now required, partly due to legal regulations, to carefully review and,
if necessary, delete reader comments. This is a labor-intensive process. Some providers of large language
models already offer solutions for automated hate speech detection or the identification of toxic content. These
include GPT-4o from OpenAI, Jigsaw’s (Google) Perspective API, and OpenAI’s Moderation API. Based on
the selected German test dataset HOCON34k, which was specifically created for developing tools to detect
hate speech in reader comments of online newspapers, these solutions are compared with each other and
against the HOCON34k baseline. The test dataset contains 1,592 annotated text samples. For GPT-4o, three
different promptings are used, employing a Zero-Shot, One-Shot, and Few-Shot approach. The results of the
experiments demonstrate that GPT-4o outperforms both the Perspective API and the Moderation API, and exceeds the
HOCON34k baseline by approximately 5 percentage points, as measured by a combined metric of MCC and F2-score.
Keywords: Hate Speech Detection, Toxic Language, NLP, LLMs, GPT, BERT, German language, HOCON34k
1.
Introduction
Toxic content and hate speech are increasingly
spreading across social media and other online
platforms, including forums and comment sections
(Udanor and Anyanwu, 2019). The digital space,
which, according to Jaki and Steiger (2023), was
originally characterized by the advantages of un-
filtered communication, has since experienced a
negative shift. The dissemination of harmful con-
tent online poses a significant challenge to both so-
ciety and democracy. In response, legislators have
implemented measures to counteract the spread of
hate speech. As of February 2024, under the Digi-
tal Services Act (European Parliament, 2022), not
only large online companies but also smaller online
platforms operating within the EU are required to
take effective action against illegal content, includ-
ing hate speech. This calls for solutions that can
assist in detecting and removing harmful content
without infringing on freedom of expression.
Automated hate speech detection, powered by
artificial intelligence, is one approach to address-
ing this issue. While most of the research on hate
speech detection is concentrated on English, some
studies are beginning to address other languages.
Disclaimer:
This research aims to combat hate
speech and, therefore, contains examples of hate
speech or offensive language, for analysis and edu-
cational purposes.
Pretrained Large Language Models (LLMs) like
GPT-4 and available moderation APIs are potential
tools for this task.
This study compares the effectiveness of Ope-
nAI’s GPT-4 (OpenAI, 2023), Google’s Perspective
API (Perspective, 2024), and OpenAI’s Modera-
tion API (OpenAI, 2024) in detecting hate speech
in German online newspapers. The publicly ac-
cessible HOCON34k dataset (Keller et al., 2024),
containing annotated reader comments from Ger-
man online newspapers, serves as the basis for
evaluation. Each solution uses a pretrained model,
with no fine-tuning or additional training applied for
this study. The datasets and models underlying
these solutions, except for the baseline model, are
not publicly disclosed. However, the companies
usually provide paid API services for public use.
Various definitions of hate speech can be found
in the literature (see, for example, ERIC (2016) and
Meta (2024)). For this study, we use the compre-
hensive hate speech guidelines defined by Keller
et al. (2024), derived from the behavior codes of
online newspapers. This definition includes the
following types of content: racist and xenophobic
content, sexist and homophobic content such as
misogyny or misandry, hostility towards LGBTQ+
individuals, religious hatred, antisemitism, other
forms of hate against humanity, unconstitutional
or extremist slurs, vulgar, obscene, or offensive
language, insults, threats, and harassment.
arXiv:2501.01256v1  [cs.CL]  2 Jan 2025

--- Page 2 ---

2.
Related Work
Hate speech detection using machine learning
methods has been extensively studied in numerous
research projects in recent years. Initially, tradi-
tional machine learning methods dominated; how-
ever, with the introduction of the transformer ar-
chitecture (Vaswani et al., 2017), deep learning
techniques have taken the forefront. Transformer-
based, pretrained language models, especially
Large Language Models (LLMs), have become in-
creasingly important, leading to notable progress
in hate speech detection for English texts, as well
as other languages (Istaiteh et al., 2020; Alkomah
and Ma, 2022; Jahan and Oussalah, 2023; Rawat
et al., 2024).
For instance, Chiu et al. (2021) utilized GPT-3 for
hate speech detection via Zero-, One-, and Few-
Shot learning. Their findings indicate that Few-
Shot learning improved performance by approxi-
mately 25 % compared to the Zero- and One-Shot
approaches (Chiu et al., 2021). Similarly, Guo et al.
(2024) used GPT-3.5 Turbo with different prompts
in a Few-Shot learning context. An F1-score of
0.82 was reported for hate speech recognition in
English texts. In comparison, the F1-score for Chi-
nese texts was only 0.55. Li et al. (2023) com-
pared ChatGPT with MTurker annotations and re-
port that ChatGPT achieves an accuracy of around
0.8 for malicious texts. Matter et al. (2024) eval-
uated the performance of GPT in recognizing vi-
olent speech on the platform incels.is, using GPT
to augment text examples. GPT-4 was found to
outperform GPT-3.5 in all metrics, with a weighted
F1-score of 0.88 and a macro F1-score of 0.78
reported as the best values.
Pan et al. (2024)
conducted a comparison between fine-tuning pre-
trained BERT-based models and several Large Lan-
guage Models (LLMs), including Mistral-7B-Instruct,
Zephyr-7b-beta, and Tulu-2, for detecting sexist and
misogynistic hate speech, as well as hate speech
against migrants, using two datasets in English lan-
guage. The LLMs were prompted using Zero- and
Few-Shot learning strategies. The best result was
achieved with 5-Shot learning and Zephyr, which
yielded a macro F1-score of 0.7094 in detecting
sexist speech. In comparison, the fine-tuned De-
BERTa model achieved a macro F1-score of 0.8681.
Glasebach et al. (2024) accomplished a macro-
average F1-Score up to 0.79 for hate speech and
0.75 for misogynistic hatespeech using a fine-tuned
GBERT-base model (Chan et al., 2020).
Google Jigsaw developed the publicly available
Perspective API (Google Jigsaw, 2024), which uti-
lizes a proprietary pretrained model designed to
detect harmful content, including sexist or racist
speech, and threats. OpenAI also provides a cur-
rently free API, the Moderation API, for detecting
harmful content across eleven categories (e.g., sex-
ist text, harassment, hate, threats, etc.) (OpenAI,
2024). The studies by Markov et al. (2022) evaluate
OpenAI’s Moderation API and Google’s Perspec-
tive API with different datasets and report better
performance of the Moderation API for all datasets
except Google’s Jigsaw dataset.
For example,
AUPRC values exceeding 0.9 were achieved us-
ing the Stormfront dataset, while the Perspective
API yielded an AUPRC value above 0.87. Addi-
tionally, experiments using GPT-2 showed better
results than with the Perspective API. Hosseini
et al. (2017) identified limitations in the Perspective
API when handling modified passages, while Nog-
ara et al. (2023) reported that the Perspective API
performed better for German content compared to
other tools. Previous studies have often not utilized
the latest versions of GPT models or APIs and have
primarily focused on hate speech detection in En-
glish. Our experiments aim to compare GPT-4o
with Google Jigsaw’s and OpenAI’s APIs, based on
their versions as of June 2024. The hate speech
detection will be tested using a recently released
German-language dataset specifically designed for
detecting hate speech in online newspapers (HO-
CON34k) (Keller et al., 2024). Metrics such as the
F2-score, Matthews correlation coefficient (MCC),
and a combined metric of both will be used for
comparison. A fine-tuned model based on Google
BERT (Devlin et al., 2019) developed by Keller et al.
(2024) for hate speech detection in the HOCON34k
dataset will serve as the baseline.
3.
Methodology
3.1.
Objective and Experimental Setup
The objective of our experiments was to compare
the performance of GPT-4o, Perspective API, and
Moderation API against the HOCON34k baseline
for hate speech detection in a binary classification
task:
• For GPT-4o, prompts were used for Zero-Shot,
One-Shot, and Few-Shot learning. The output
was mapped to a binary classification ("Hate
Speech" or "No Hate Speech" / "Yes" or "No").
• For the Moderation API, the overall score of
a query was used to derive the classifica-
tion (True = "Hate Speech", False = "No Hate
Speech").
• For the Perspective API, the output value rep-
resenting the probability of hate speech was
mapped to a binary classification based on
three different threshold values.
• The HOCON34k baseline utilizes a pre-trained
BERT model (Chan et al., 2020) fine-tuned

--- Page 3 ---

with the HOCON34k dataset. The HOCON34k
classifier outputs a probability score for hate
speech, which is evaluated using an optimized
threshold.
In total, seven individual tests were conducted:
three using GPT-4o, with varying learning ap-
proaches (abbreviated in Alg. 1 as GPT4-Z/O/F),
three using the Perspective API with varying thresh-
old values τ ∈{0.38, 0.5, 0.8} (denoted as PAPI-
038/05/08 in Alg. 1), and one test using the Mod-
eration API (MAPI). The results of the HOCON34k
baseline were taken from Keller et al. (2024) for
comparison.
The evaluation of detection performance was
based on a uniform test dataset designed for bi-
nary classification with the labels Hate Speech or
No Hate Speech. The test dataset was a selected
portion of the HOCON34k dataset (Keller et al.,
2024), annotated by twelve individuals, including
professional moderators from online newspapers.
The HOCON34k test dataset contains real-world
examples from reader comments on various on-
line newspaper platforms. For the GPT-4o tests,
the hate speech definition from HOCON34k was
inputted as a prompt. The Perspective API and
Moderation API used their own definitions of hate
speech.
Algorithm 1: Detection Experiment
begin
MAX_REPEATS := 3
SAMPLES := 1592
init api[] with {GPT4-Z, GPT4-O, GPT4-F,
PAPI-038, PAPI-05, PAPI-08, MAPI}
init result[api, MAX_REPEATS, SAMPLES]
init metrics[api, MAX_REPEATS]
init avgMetr[api]
for a in api do
for i from 1 to MAX_REPEATS do
for t from 1 to SAMPLES do
response = a.request(t.text)
result(a, i, t) = computeForecast(
threshold, response, t.label)
end for
compute metrics[a, i] ←result[a, i, *]
end for
compute avgMetr[a] = avg(metrics[a, i])
end for
print avgMetr
end
For the comparison of the approaches, each indi-
vidual test applied the 1,592 data samples to make
predictions. All tests were repeated three times.
Confusion matrices were generated, and the met-
rics Recall, Precision, F1-score, F2-score, MCC,
and the Champion-Challenger score S (Keller et al.,
2024) were computed. An average value for each
metric was calculated across the three runs. The
three runs were also used to verify the consistency
of the outputs. A Python script was developed to
automate the API requests for all runs. Algorithm 1
outlines its functionality in pseudocode. The re-
sult calculation was performed three times for each
considered API. The results for each request were
mapped to the confusion matrix using the com-
puteForecast function. Finally, the evaluation
metrics are computed for each run and API, fol-
lowed by calculating the average across the three
runs. The following subsections introduce the test
dataset (3.2), evaluation metrics (3.3), and give
further details on the experiments (3.4-3.6).
3.2.
Dataset HOCON34k
The basis of our experiments is the HOCON34k
dataset (Hatespeech in Online Comments from
German Newspapers, comprising approximately
34,000 comments) from Keller et al. (2024). The
dataset originates from the comment sections of
various German newspapers, including the TZ and
the Frankfurter Rundschau. The texts were labeled
as Hate Speech or No Hate Speech by profes-
sional moderators and other experts, including re-
searchers and IT specialists. In total, 29 individ-
uals participated in the annotation process. The
complete dataset contains 34,223 text examples,
of which 28,992 were labeled as not containing
hate speech (84.7 %) and 5,231 as hate speech
(15.3 %).
A subset of 15,248 texts, including 12,275 train-
ing samples, 2,492 validation samples, and 1,592
test samples, was selected for our comparison pur-
poses. This subset, annotated by 12 experts under
the supervision of a lead moderator, exhibited high
quality with an inter-rater agreement of κ = 0.6078
(Fleiss’ Kappa), indicating substantial agreement.
For our experiments, only the test dataset is re-
quired, consisting of 329 (20.67 %) hate speech
texts and 1,263 (79.33 %) non-hate speech texts.
These 1,592 texts, representing around 10 % of the
total dataset, were used for testing. In addition to
the text and binary annotation, the dataset includes
information such as post ID, annotator ID, whether
the context was sufficient for annotation, and the
source file name. However, for our experiments,
only texts and labels were used while context infor-
mation was not considered. Table 1 provides a few
example entries from the original dataset.
The texts are primarily in German. In addition,
some test data include foreign languages or inter-
net links. Individual texts in the dataset contain
spelling and grammar errors, colloquial and dialec-
tal expressions, or simply unintelligible character
strings. Symbols and self-censorship also appear
in some of the comments.

--- Page 4 ---

Post Id
Label
Text (Original and Translated)
4235999044
Hate Speech
(enough context)
Muslimischer Terrorismus. Wia immer hoid.
Translation: Muslim terrorism. As always.
3248014695
Not Hate Speech
(enough context)
Hkh vfkmfjhi
Translation: Hkh vfkmfjhi
3811968397
Hate Speech
(not enough context)
Wir werden nur verar...
Translation: We’re just being p...
4964167063
Not Hate Speech
(not enough context)
Nein Es sind doch nicht alle betrunken Obwohl ?
Translation: No, they’re not all drunk Although ?
Table 1: Example texts from the HOCON34k dataset (Keller et al., 2024)
3.3.
Evaluation Metrics
Accuracy, Precision, Recall, and F1-score are cal-
culated according to Powers (2020) based on the
confusion matrix using the four values: True Posi-
tive (TP), True Negative (TN), False Positive (FP),
and False Negative (FN). The moderators involved
in annotating the HOCON34k dataset primarily ex-
pect hate speech detection to minimize undetected
hate speech, meaning FN should be as low as
possible. A higher rate of false positives (FP) is
tolerable in this context, as all user-generated com-
ments undergo a manual review process. For this
reason, recall is more important than precision in
our use case. Consequently, in addition to the F1-
score, the F2-score is particularly relevant, as it
gives twice as much weight to recall compared to
precision, as shown in equation 1.
F2 =
(1 + 2)2 · TP
(1 + 2)2 · TP + FP + 22 · FN
(1)
However, an overly one-sided emphasis on recall
should be avoided, which is why the Matthews Cor-
relation Coefficient (MCC) is also considered. The
MCC is defined in equation 2 using P and N as
the total number of positives (P) and negatives (N).
The F2-score and a normalized MCC (eq. 3) are
combined into a single metric, referred to in Keller
et al. (2024) as the Champion Challenger score S
and shown in equation 4.
MCC =
TP · TN −FP · FN
p
P · N · (TP + FN)(TN + FP)
(2)
M norm = MCC + 1
2
(3)
S = M norm + F2
2
(4)
3.4.
Experiments with GPT-4o
For the experiments with GPT-4, the GPT-4o model
(exact designation: gpt-4o-2024-05-13) was used.
In all GPT-4o experiments, the prompt first included
the definition of hate speech as specified in Fig. 1.
This definition was taken from Keller et al. (2024).
Experiments are conducted with Zero-Shot, One-
Shot, and Few-Shot learning. The prompt is struc-
tured into three parts. In the first part, the hate
speech guidelines are explained. In the second
part, for One-Shot learning, one labeled example
text is provided, while for Few-Shot learning, four
labeled example texts are given. The first Few-
Shot learning example was also used for One-Shot
learning. This part is omitted for Zero-Shot learn-
ing. The labels are either Yes for hate speech or
No for no hate speech. The third part of the prompt
is included in all experiments and contains the spe-
cific instruction. Only Yes or No are allowed as
responses. Figure 1 shows the prompt used for
Few-Shot learning with four text examples, each la-
beled as Yes or No. The texts were taken from the
HOCON34k training dataset (not the test dataset)
and include original spelling errors.
API requests were made using the ope-
nai.Completion.create method from Ope-
nAI’s Python library (OpenAI, 2024). The temper-
ature parameter, ranging from 0.0 to 2.0, controls
response creativity, with higher values producing
more creative outputs.
At temperature=0.0, re-
sponses are intended to be almost deterministic.
For all experiments, the default value of 1.0 was
used. Preliminary tests showed no increase in de-
terminism with a temperature of 0.0. The method
output, either Yes or No, suggests that temperature
has no impact on short responses.
3.5.
Experiments with Moderation API
The OpenAI Moderation API provides an endpoint
to analyze input text to detect harmful content
(OpenAI, 2024). The underlying model is not pub-
licly available and cannot be modified, retrained,
or fine-tuned. In our experiments, we used the
API’s stable version from June 2024. The openai-
Moderation.create method allows client appli-
cations to check a text by passing it as an input pa-
rameter, along with a pre-generated API key. The
service is paid, but offers free usage credits (Ope-
nAI, 2024).

--- Page 5 ---

** Hassrede-Regelwerk**
Es handelt sich um Hassrede, wenn Texte folgende Punkte beinhalten: Rassistische und
fremdenfeindliche Inhalte, sexistische und homophobe Inhalte, wie z. B. Frauenfeindlichkeit
und Männerfeindlichkeit, Feindlichkeit gegen lesbische und schwule Personen etc., religiöser
Hass, antisemitische und andere menschenfeindliche Inhalte, verfassungsfeindliche oder
extremistische
Inhalte,
Schimpfwörter,
Vulgäre,
obszöne
und
anstößige
Sprachen,
Beleidigungen, Drohungen, Belästigung.
** Zwei positive und zwei negative Beispiele **
Zur Einordnung befinden sich Beispieltexte in Anführungszeichen und dahinter das Ergebnis, ob 
es sich um Hassrede handelt oder nicht:
1.
"Das finde ich auch. Je kleiner das Hirn, desto größer wird das Maulaufgerissen ;-)“ – Ja
2.
"Er wird sich nicht aendern sondern weiterhin Angriff um Angriff vergeigen.“ – Nein
3.
"Was wäre daran schlimm, diese Subjekte ins Gulag zu bringen?" – Ja
4.
"Ich denke Mal dass das die Antwort auf genau die selbe Aussage nur mit der linken und 
Kommunisten war.“ – Nein
** Konkrete Anweisung für die Bewertung **
Ist der folgende Text in Anführungszeichen Hassrede? Antworte ausschließlich mit Ja oder
Nein:
"Sie haben doch einen an der Palme."
** Hate Speech Guidelines **
A text is classified as hate speech if it includes any of the following: Racist and xenophobic
content, sexist and homophobic content, such as misogyny or misandry, hostility towards
lesbian and gay individuals, religious hate, antisemitic and other inhumane content,
unconstitutional or extremist content, vulgar, obscene, and offensive language, insults,
threats, or harassment.
** Two Positive and Two Negative Examples **
To assist with classification, example texts are provided in quotation marks, followed by 
the result indicating whether the text is considered hate speech:
1.
"I think so too. The smaller the brain, the bigger the mouth opens ;-)" – Yes
2.
"He won’t change but will continue to mess up attack after attack." – No
3.
"What would be wrong with sending these subjects to the Gulag?" – Yes
4.
"I think that was the response to exactly the same statement, just with leftists and 
communists." – No
** Specific Instruction for Evaluating ** 
Is the following text in quotation marks considered hate speech? Answer exclusively with
Yes or No:
"Sie haben doch einen an der Palme."
Figure 1: Prompt for GPT-4o Few-Shot Learning: Original Prompt (left) and Translation (right).
The API can process text up to 32,768 tokens
and checks for harmful content across eleven cate-
gories: Sexual, Hate, Harassment, Self-Harm, Sex-
ual/Minors, Hate/Threatening, Violence/Graphic,
Self-Harm/Intent, Self-Harm/Instructions, Harass-
ment/Threatening, and Violence (OpenAI, 2024).
This broad scope of content moderation aligns with,
and in some cases exceeds, our own definition
of hate speech, covering self-harm, instructions
for self-harm, and graphic content involving death,
violence, or injury. However, it does not explic-
itly cover unconstitutional or legal aspects, though
these might fall under certain categories. Legal
nuances specific to individual countries are not
considered by the API. The output of a create()
call is a moderation object, with each category
marked as True or False and a corresponding
score. Additionally, an overall flag (flagged) is
set to True if any category is marked as True. In
our experiments, we focused solely on this over-
all flag and interpreted it as a binary classification
for hate speech (flagged == True →1) or non-
hate speech (flagged == False →0). More
detailed classifications, such as sexism, were not
further analyzed in our experiments. The Modera-
tion API does not use the temperature parame-
ter for controlling randomness and creativity, and,
according to OpenAI (OpenAI, 2024), it provides
nearly deterministic outputs. However, our exper-
iments showed that the outputs were not always
repeatable and exhibited slight variations.
3.6.
Experiments with Perspective API
The current generation of the Perspective API is
implemented as a Charformer-based Transformer,
referred to as Unified Toxic Content Classification
(UTC) according to Lees et al. (2022).
A Charformer uses Gradient-Based Subword To-
kenization (GBST), enabling the model to learn
latent subwords from individual characters of a text,
as explained by Tay et al. (2021). The Perspective
API model is pretrained on multilingual texts and
comment sections (Lees et al., 2022; Tay et al.,
2021). The pretrained model is not specifically
focused on hate speech detection but rather on
identifying toxic content. Google Jigsaw defines
toxicity as “[...] a rude, disrespectful, or unreason-
able comment that is likely to make someone leave
a discussion” (Google Jigsaw, 2024). Similar to the
Moderation API, users cannot modify or fine-tune
the underlying language model in the Perspective
API. Unlike the Moderation API, the Perspective
API’s response provides probability scores between
0 and 1 for the categories Toxicity, Severe Toxic-
ity, Identity Attack, Insult, Profanity, and Threat.
Currently, no assessment for sexist texts is pro-
vided (Perspective, 2024), but except for this, the
definition is similar to the one used in Keller et al.
(2024). Legal or unconstitutional violations are not
considered, as these are country-specific issues,
and legal violations such as incitement to hatred
in Germany are also not accounted for. Legal in-
tricacies of individual countries are not part of the
Perspective API’s evaluation.
In our experiments, we mapped the output scores
to binary values, requiring the selection of a thresh-
old. For research purposes, a threshold of 0.7 to
0.9 is recommended for the Perspective API, with
adjustments based on the specific application (Per-
spective, 2024). A separate threshold can be set
for each category. In our experiments, we used
thresholds τ ∈{0.38, 0.5, 0.8} across all categories.
If the score for any category exceeds the threshold,
the text is classified as hate speech (1); otherwise,
it is classified as non-hate speech (0).

--- Page 6 ---

Table 2: Classification Results Across All Experiments and Comparison with Baseline
Metric
GPT-4o
Pers-API
ModAPI
HOCON34k
Zero-Shot
One-Shot
Few-Shot
τ = 0.38
τ = 0.5
τ = 0.8
τ = 0.523
Accuracy
0.8049
0.7701
0.7988
0.7726
0.8097
0.7965
0.6981
0.607
Precision
0.5212
0.4660
0.5097
0.4516
0.5883
0.8571
0.3766
0.327
Recall
0.6849
0.7700
0.6920
0.4680
0.2766
0.0182
0.7031
0.851
F1-score
0.5919
0.5806
0.5870
0.4597
0.3753
0.0357
0.4905
0.472
F2-score
0.6444
0.6811
0.6458
0.4646
0.3091
0.0227
0.5992
0.644
MCC
0.4743
0.4612
0.4674
0.3158
0.3066
0.1067
0.3326
0.320
S
0.6908
0.7059
0.6897
0.5613
0.4812
0.2880
0.6327
0.652
Higher is better for all metrics. Bold: best overall value for each metric. Underlined: best within the same model type.
We conducted three experiments with the Per-
spective API using the specified thresholds, incor-
porating waiting times between requests to avoid
exceeding the quota. For Python requests, we
used the Google API Client Library (google-api-
python-client). A request is made using the
execute method, with input parameters includ-
ing the text to be evaluated, the categories to be
checked, and the target language. The response
is returned as a JSON object, containing a score
for each category.
The highest score from the
response is used to determine the result, which
is then mapped to hate speech (1) or non-hate
speech (0) based on the selected threshold.
4.
Results and Limitations
4.1.
Results
The classification results of the experiments with
GPT-4o and the HOCON34k rule set show no sig-
nificant differences between Zero-Shot, One-Shot,
and Few-Shot learning. The approaches differ only
slightly. Zero-Shot learning, without any example
texts, achieved the best results in terms of Accuracy,
Precision, F1-score, and MCC. One-Shot learning
yielded the highest scores for Recall, F2-score, and
Champion-Challenger score (S). A comparison
with the baseline from the BERT-based HOCON34k
model (Keller et al., 2024) shows that GPT-4o in
One-Shot learning achieved an improved S score,
approximately 5 percentage points higher than the
baseline (S=0.7059). Contrary to our expectations,
Few-Shot learning (with four example texts) per-
formed slightly worse.
Table 2 presents the results of the experiments,
where the average of three runs was calculated for
each metric. For the Perspective API, a threshold
of 0.38 was the most effective for detecting hate
speech. A threshold of 0.5 produced better results
for Accuracy, while a threshold of 0.8 yielded the
best Precision. A comparison of Perspective and
Moderation API shows that the Moderation API
achieved superior overall performance on our test
dataset. The high Accuracy and Precision scores
of the Perspective API are due to mostly negative
predictions combined with the dataset’s imbalance.
With τ = 0.8, only 6 out of 1,592 samples were clas-
sified as hate speech, resulting in a high number of
323 False Negatives (see Tab. 3). For our applica-
tion scenario, we primarily compare quality using
the Champion-Challenger score (S). For the base-
line model, the threshold of 0.523 was optimized
for S, effectively balancing the F2-score, MCC, and
indirectly, Recall. This optimization is reflected in
the Recall value of the HOCON34k baseline, which
achieved the highest score of 0.851. The optimiza-
tion for S resulted in more True Positives being de-
tected, but also significantly more False Positives
(see Tab. 3).
However, there were considerably fewer False
Negatives. The baseline classification aimed to de-
tect as much hate speech as possible, even at the
cost of a higher number of False Positives, ensuring
that no hate speech remains undetected. It should
also be noted that the Perspective API, without lan-
guage selection, had greater difficulty with German
dialects, HTTP links, and uninterpretable character
strings. For example, texts like “Des häd a Depp
a gsogt!” (English translation: “That’s what a fool
said!”) or “mach mal den rand zu, du kleine braune
drecksau!!!” (English translation: “close the rim, you
little brown bastard!!!”) were classified as non-hate
speech due to error messages from the Perspec-
tive API. However, when the language was explicitly
set to German, no error messages were returned.
Table 3 also shows that deterministic output is not
guaranteed for identical queries with GPT-4o and
the Moderation API. There were slight variations be-
tween individual test runs, which was observed for
both One-Shot and Few-Shot Learning with GPT-
4o. In contrast, the output from the Perspective
API appears to be repeatable, as demonstrated in
Tab. 3 for the threshold of 0.8. This consistency
was also observed in test runs with the other two
thresholds.

--- Page 7 ---

Table 3: Confusion Matrices for 3 Repeated Runs
Experiment
TP
FN
FP
TN
GPT-4o, Few-Shot (1)
229
100
221
1042
GPT-4o, Few-Shot (2)
227
102
218
1045
GPT-4o, Few-Shot (3)
227
102
218
1045
Moderation API (1)
231
98
384
879
Moderation API (2)
231
98
382
881
Moderation API (3)
232
97
383
880
Pers-API, τ = 0.8 (1)
6
323
1
1262
Pers-API, τ = 0.8 (2)
6
323
1
1262
Pers-API, τ = 0.8 (3)
6
323
1
1262
HOCON34k τ = 0.523
280
49
577
686
4.2.
Limitations
The HOCON34k test dataset from Keller et al.
(2024), containing 1,592 text examples, has an
uneven distribution with a significantly higher pro-
portion of non-hate speech. The same applies to
the HOCON34k training dataset, which was used
to train the HOCON34k baseline. The underlying
models and training datasets for the other solutions
analyzed are not disclosed. During the analysis
of individual predictions, weaknesses in the test
dataset were identified. Upon closer inspection,
annotations were found that, in our opinion, do not
comply with the given HOCON34k guidelines. For
example, the text “stellt das schwein und macht
es wie die leute in bolivien !” (English translation:
“put the pig and make it like the people in bolivia
!”) was labeled as non hate speech, although it
is hate speech according to the HOCON34 rules.
Eliminating potentially erroneous data might lead
to different results.
Most
of
the
models
analyzed
are
non-
deterministic and can produce different predictions
for repeated runs of the classification. For the Per-
spective API, determinism is assumed. However,
this assumption is based solely on the consistent
classifications observed in the three repetitions
conducted in our experiments. The assumption
was not definitively proven in this study. In contrast,
the BERT-based HOCON34k classifier produces
consistent outputs for identical input texts on the
same hardware, exhibiting deterministic behavior.
The specific definition of hate speech in HO-
CON34k does not align with the definitions used in
the underlying models for the Perspective and Mod-
eration APIs. Different definitions of hate speech or
harmful speech for the various solutions limit their
comparability. The models of the APIs analyzed
were trained on harmful content using different def-
initions. However, aside from legal violations or
unconstitutional statements, a high degree of over-
lap between the models is assumed.
Table 4:
Overview of Adjustments to the Test
Dataset through Reannotation (HS = Hate Speech).
Reviewed labels
313
Unanimous decisions by annotators
155
in accordance with GPT-4o:
107
Decisions without unanimity
158
in accordance with GPT-4o:
94
Samples where the label was changed
201
From HS to Not HS:
64
From Not HS to HS:
137
Samples without change
112
5.
Dataset Analysis and Improvement
5.1.
Analysis of Testdata
Due to the assumption of optimization potential in
the dataset, a reannotation of a sample of 91 text ex-
amples from the test dataset was conducted by four
additional individuals who had previously worked
on the HOCON34k dataset and were therefore well-
versed in the guidelines. In the reannotation pro-
cess, between 16 and 26 text examples were an-
notated differently compared to the test dataset. In
some cases, it was not possible to make an ex-
act assessment based solely on the text. The four
annotators were thus asked to indicate whether
the context was sufficient for an accurate assess-
ment. Among the 91 text examples, 18, 21, 42,
and 45 texts were marked as "Insufficient Context"
by the four annotators. The annotators agreed on
the annotation of 51 texts. In 5 out of 91 text ex-
amples, all annotators agreed that the annotation
in the dataset was incorrect. A projection for the
entire test dataset of 1,592 samples estimated a
range of 78 to 96 samples with potentially incorrect
annotations (error range 10 %, confidence interval
90 %). The experiments with GPT-4o and Few-Shot
Learning yielded the same results as the annota-
tors in cases of unanimous agreement. For the 51
Figure 2: S-, F1-, and F2-scores of all models on
HOCON34k test compared to the reannotated data.

--- Page 8 ---

Table 5: Classification Results Across All Experiments after Reannotation
Metric
GPT-4o
Pers-API
ModAPI
HOCON34k
Zero-Shot
One-Shot
Few-Shot
τ = 0.38
τ = 0.5
τ = 0.8
τ = 0.523
Accuracy
0.8770
0.8102
0.8139
0.8290
0.8020
0.7517
0.7427
0.703
Precision
0.7592
0.5748
0.5817
0.7216
0.8258
1.0000
0.4932
0.453
Recall
0.7498
0.9493
0.9327
0.5237
0.2718
0.0150
0.7672
0.855
F1-score
0.7545
0.7160
0.7165
0.6069
0.4090
0.0295
0.6005
0.592
F2-score
0.7516
0.8398
0.8322
0.5541
0.3139
0.0186
0.6906
0.726
MCC
0.6725
0.6277
0.6252
0.5117
0.3974
0.1060
0.4461
0.440
S
0.7939
0.8268
0.8224
0.6550
0.5063
0.2858
0.7068
0.723
Higher is better for all metrics. Bold: best overall value for each metric. Underlined: best within the same model type.
Table 6: Confusion Matrices after Reannotation
Experiment
TP
FN
FP
TN
GPT-4o, Few-Shot (1)
376
25
279
911
GPT-4o, Few-Shot (2)
375
26
262
928
GPT-4o, Few-Shot (3)
371
30
266
924
Moderation API (1)
308
93
308
872
Moderation API (2)
308
93
315
875
Moderation API (3)
307
94
315
875
Pers-API, τ = 0.8 (1)
6
395
0
1190
Pers-API, τ = 0.8 (2)
6
395
0
1190
Pers-API, τ = 0.8 (3)
6
395
0
1190
HOCON34k τ = 0.557
343
58
415
775
unanimously confirmed texts, GPT-4o achieved an
accuracy of 100 %. Based on these results, it is as-
sumed that the imperfect classification is not solely
due to model limitations but also to inconsistent or
erroneous annotations.
5.2.
Reannotation of Testdata
A reannotation of the HOCON34k test dataset was
conducted according to the following procedure.
To keep the manual annotation effort within a mod-
erate scope, automated classifications based on
GPT-4o were used to identify potential misclassifi-
cations, which were then manually reviewed only
when necessary. For this, three classification runs
were performed for all test dataset samples using
the Zero-Shot version of GPT-4o, and a majority
decision was formed based on the mode value.
The majority decisions generated by GPT-4o
were then compared with the labels present in the
test dataset. If there was a discrepancy between
the comparison values, the corresponding sam-
ples were manually rechecked according to the
HOCON34k guidelines. Following this process,
314 labels requiring review were identified. These
were subsequently reannotated by three annota-
tors independently in a blind annotation process.
The labels in the test dataset were then adjusted,
with the majority decision of the three annotators
being adopted as the new label. In about 64% of
the cases, the label suggested by GPT was con-
firmed by the annotators and incorporated into the
dataset as the new label. In the remaining cases,
the majority of annotators disagreed with the GPT-
generated label, and the original label was retained.
Due to a missing annotation for one of the samples
under review, it was removed from the dataset.
This results in a new dataset size of 1,591 sam-
ples. Among these, 401 are labeled as hate speech
(previously 329), and 1,190 are labeled as non-hate
speech (previously 1,263). Compared to the orig-
inal dataset, the proportion of hate speech has
increased significantly from 20.7 % to 25.2 %. Ta-
ble 4 summarizes the reannotation process and
adjustments made to the test dataset.
5.3.
Improved Results
Following the reannotation described earlier, a
replication of all previously conducted experiments
was performed using the resulting optimized test
dataset. Additionally, the test of the HOCON34k
baseline classifier was repeated on the new test
data. The results of the repeated experiments are
presented in Tab. 5 and Fig. 2. Tab. 6 shows the
confusion matrices for the repeated experiments.
The test results improved for most experiments after
reannotation, often showing a significant increase
in performance.
Overall, the GPT-4o variants demonstrated the
best results on both the original and reannotated
test datasets. In contrast to the previous results,
GPT-4o also outperformed the other models in
terms of accuracy and recall. Based on the re-
annotated test dataset, with the exception of Zero-
Shot learning the GPT-based classification variants
achieved F2-scores and S-scores above 0.8, out-
performing the other models in these and most
other metrics. The best result was achieved by the
One-Shot variant with S = 0.8268. This variant al-
ready performed best in the original experiments

--- Page 9 ---

and experienced an increase in the S-score by
17.13 % due to the reannotation. The reannotation
also improved the test results for the HOCON34k
baseline classifier (Keller et al., 2024).
The S-
score increased from 0.652 to 0.723, a 10.89 % im-
provement. The GPT-based variants experienced
a stronger increase in the S-score. The One-Shot
variant nearly doubled its advantage over the base-
line, with performance increasing from 0.054 to
0.104. The improvement in recall was even more
significant. While the baseline classifier initially
demonstrated the highest recall, the One-Shot vari-
ant achieved a substantial improvement of 23.29 %,
increasing from 0.77 to 0.9493, thereby surpass-
ing the baseline also in recall performance. The
recall for the baseline classifier, on the other hand,
remained mostly unchanged. The Perspective API,
measured by S-score and F2-score, again pro-
duced the weakest results, in some cases even
showing a decline compared to the previous eval-
uation with the original dataset. The Moderation
API achieved better results than the Perspective
API but remained significantly behind GPT-4o and
slightly behind the HOCON34k baseline. Figure 2
provides a comparison of the test results before and
after the reannotation of the test data. The graph il-
lustrates the significant performance improvements
in nearly all experiments. The largest performance
gain was observed with GPT-4o. However, this
should be viewed critically, as the reannotation pro-
cess only considered samples that GPT identified
as misclassified. Given the near-deterministic clas-
sification, each adjustment results in a predictable
improvement in evaluation outcomes for GPT. Al-
though the final decision to adjust labels was made
by annotators, independent of GPT’s assessments,
the selective review may introduce a bias in favor
of GPT.
6.
Conclusions
In this study, we compared GPT-4o, OpenAI’s Mod-
eration API, and the Perspective API in detecting
hate speech in German online comments, using
the HOCON34k dataset and its baseline classifier
as a reference. GPT-4o, using various prompt-
ing strategies, outperformed other models, with
One-Shot Learning yielding better results than Few-
Shot Learning. The Moderation API performed well,
while the Perspective API struggled, showing high
precision but missing most hate comments due to
numerous false negatives.
Our findings highlight the critical role of high-
quality datasets in improving classification perfor-
mance. Correcting annotation errors resulted in
over 10% improvement across most models, in-
cluding the HOCON34k classifier.
Future research should focus on incorporating
contextual information into hate speech detection
models, as expressions often depend on previous
comments or the articles (Madhu et al., 2023). Ex-
panding datasets through data augmentation (Ja-
han et al., 2024) and developing systems capable
of continuous learning, which adapt to evolving lan-
guage using moderator feedback, are also essen-
tial. Specialized models for different sections of on-
line newspapers, like sports or politics, could further
improve detection accuracy. These advancements
are a key to enhancing real-world hate speech de-
tection systems.
References
Fatimah Alkomah and Xiaogang Ma. 2022. A Liter-
ature Review of Textual Hate Speech Detection
Methods and Datasets. Information, 13(6):273.
Branden Chan, Stefan Schweter, and Timo Möller.
2020. German’s Next Language Model.
Davide Chicco and Giuseppe Jurman. 2020. The
advantages of the Matthews correlation coeffi-
cient (MCC) over F1 score and accuracy in bi-
nary classification evaluation. BMC Genomics,
21(1):6.
Ke-Li Chiu, Annie Collins, and Rohan Alexander.
2021. Detecting Hate Speech with GPT-3.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
Deep Bidirectional Transformers for Language
Understanding.
ERIC. 2016.
Europäische Kommission gegen
Rassismus und Intoleranz Allgemeine Politik-
Empfehlung Nr. 15 der ECRI über die Bekämp-
fung von Hassrede.
European Parliament. 2022.
Verordnung -
2022/2065 - EN - EUR-Lex.
Jonas Glasebach, Max-Emanuel Keller, Alexander
Döschl, and Peter Mandl. 2024. GMHP7k: A Cor-
pus of German Misogynistic Hatespeech Posts.
Proceedings of the International AAAI Confer-
ence on Web and Social Media, 18:1946–1957.
Google Jigsaw. 2024. Perspective API. [Accessed:
2024-09-21].
Keyan Guo, Alexander Hu, Jaden Mu, Ziheng Shi,
Ziming Zhao, Nishant Vishwamitra, and Hongxin
Hu. 2024. An Investigation of Large Language
Models for Real-World Hate Speech Detection.

--- Page 10 ---

Hossein Hosseini, Sreeram Kannan, Baosen
Zhang, and Radha Poovendran. 2017. Deceiv-
ing Google’s Perspective API Built for Detecting
Toxic Comments.
Othman Istaiteh, Razan Al-Omoush, and Sara Ted-
mori. 2020. Racist and Sexist Hate Speech De-
tection: Literature Review. In 2020 International
Conference on Intelligent Data Science Tech-
nologies and Applications (IDSTA), pages 95–
99.
Md Saroar Jahan and Mourad Oussalah. 2023. A
systematic review of hate speech automatic de-
tection using natural language processing. Neu-
rocomputing, 546:126232.
Md Saroar Jahan, Mourad Oussalah, Djamila Ro-
maissa Beddia, Jhuma kabir Mim, and Nabil
Arhab. 2024. A Comprehensive Study on NLP
Data Augmentation for Hate Speech Detection:
Legacy Methods, BERT, and LLMs.
Sylvia Jaki and Stefan Steiger. 2023. Hate Speech
online: Hartknäckiges Phänomen und interdiszi-
plinärer Forschungsgegenstand. In Sylvia Jaki
and Stefan Steiger, editors, Digitale Hate Speech,
pages 1–14. Springer Berlin Heidelberg.
Justin M. Johnson and Taghi M. Khoshgoftaar.
2019. Survey on deep learning with class im-
balance. Journal of Big Data, 6(1):27.
Max-Emanuel Keller, Maximilian Auch, Alexander
Döschl, Fabian Vlk, Julian Quernheim, Mike Hart-
mann, Peter Mandl, Alexander Kaul, and Markus
Franz. 2024. HOCON34k: A Corpus of Hate
speech in Online Comments from German News-
papers. In Information Integration and Web Intel-
ligence, Bratislava, Slovakia.
Alyssa Lees, Vinh Q. Tran, Yi Tay, Jeffrey Sorensen,
Jai Gupta, Donald Metzler, and Lucy Vasserman.
2022. A New Generation of Perspective API: Ef-
ficient Multilingual Character-level Transformers.
Lingyao Li, Lizhou Fan, Shubham Atreja, and Libby
Hemphill. 2023. "HOT" ChatGPT: The promise of
ChatGPT in detecting and discriminating hateful,
offensive, and toxic comments on social media.
Hiren Madhu, Shrey Satapara, Sandip Modha,
Thomas Mandl, and Prasenjit Majumder. 2023.
Detecting offensive speech in conversational
code-mixed dialogue on social media: A contex-
tual dataset and benchmark experiments. Expert
Systems with Applications, 215:119342.
Thomas Mandl. 2023.
KI-Verfahren für die
Hate Speech Erkennung: Die Gestaltung von
Ressourcen für das maschinelle Lernen und ihre
Zuverlässigkeit. In Sylvia Jaki and Stefan Steiger,
editors, Digitale Hate Speech, pages 111–130.
Springer Berlin Heidelberg.
Todor Markov, Chong Zhang, Sandhini Agarwal,
Tyna Eloundou, Teddy Lee, Steven Adler, An-
gela Jiang, and Lilian Weng. 2022. A Holistic
Approach to Undesired Content Detection in the
Real World.
Daniel Matter, Miriam Schirmer, Nir Grinberg, and
Jürgen Pfeffer. 2024.
Close to Human-Level
Agreement: Tracing Journeys of Violent Speech
in Incel Posts with GPT-4-Enhanced Annota-
tions.
Meta. 2024. Hassrede | Transparency Center. [Ac-
cessed: 2024-09-21].
Gianluca Nogara, Francesco Pierri, Stefano Cresci,
Luca Luceri, Petter Törnberg, and Silvia Gior-
dano. 2023. Toxic Bias: Perspective API Mis-
reads German as More Toxic.
OpenAI. 2023.
GPT-4 Technical Report.
[Ac-
cessed: 2024-09-21].
OpenAI. 2024. OpenAI Platform. [Accessed: 2024-
09-21].
Ronghao Pan, José Antonio García-Díaz, and
Rafael Valencia-García. 2024. Comparing Fine-
Tuning, Zero and Few-Shot Strategies with Large
Language Models in Hate Speech Detection in
English. Computer Modeling in Engineering &
Sciences, 140(3):2849–2868.
Perspective. 2024. Perspective | Developers. [Ac-
cessed: 2024-09-21].
David MW Powers. 2020.
Evaluation:
from
precision,
recall
and
F-measure
to
ROC,
informedness,
markedness and correlation.
arXiv:2010.16061.
Anchal Rawat,
Santosh Kumar,
and Suren-
der Singh Samant. 2024. Hate speech detec-
tion in social media: Techniques, recent trends,
and future challenges. WIREs Computational
Statistics, 16(2):e1648.
Yi Tay, Vinh Q. Tran, Sebastian Ruder, Jai Gupta,
Hyung Won Chung, Dara Bahri, Zhen Qin, Si-
mon Baumgartner, Cong Yu, and Donald Metzler.
2021. Charformer: Fast Character Transformers
via Gradient-based Subword Tokenization.
Collins Udanor and Chinatu C. Anyanwu. 2019.
Combating the challenges of social media hate
speech in a polarized society: A Twitter ego lex-
alytics approach. Data Technologies and Appli-
cations, 53(4):501–527.
Ashish Vaswani, Noam Shazeer, Niki Parmar,
Jakob Uszkoreit, Llion Jones, Aidan N. Gomez,
Lukasz Kaiser, and Illia Polosukhin. 2017. Atten-
tion Is All You Need.

```
