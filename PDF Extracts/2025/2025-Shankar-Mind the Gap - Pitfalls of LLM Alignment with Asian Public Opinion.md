---
title: "2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion - PDF Extract"
source_pdf: "2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion.pdf"
pages: 15
extracted_at: "2026-02-08T06:31:11.194947"
---

# PDF Extract: 2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion

**Source PDF:** 2025-Shankar-Mind the Gap - Pitfalls of LLM Alignment with Asian Public Opinion.pdf
**Total Pages:** 15

---

## Content

```
--- Page 1 ---

Mind the Gap: Pitfalls of LLM Alignment with Asian Public Opinion
Warning: This paper contains content that may be potentially offensive or upsetting.
Hari Shankar1, Vedanta S P2, Sriharini Margapuri1, Debjani Mazumder1,
Ponnurangam Kumaraguru1, Abhijnan Chakraborthy3
1IIIT Hyderabad
2IIIT Kottayam
3IIT Kharagpur
Abstract
Large Language Models (LLMs) are increasingly de-
ployed in multilingual,
multicultural settings,
yet
their reliance on predominantly English-centric train-
ing data risks misalignment with the diverse cultural
values of different societies. In this paper, we present
a comprehensive, multilingual audit of alignment of
contemporary LLMs including GPT-4o-Mini, Gemini-
2.5-Flash, Llama 3.2, Mistral and Gemma 3 across In-
dia, East Asia and Southeast Asia. Our study specif-
ically focuses on the sensitive domain of religion as
the prism for broader cultural alignment.
To facili-
tate this, we conduct a multi-faceted analysis of every
LLM’s internal representations, using log-probs/logits,
to compare the model’s opinion distributions against
ground-truth public attitudes. We find that while the
popular models generally align with public opinion on
broad social issues, they consistently fail to accurately
represent religious viewpoints, especially those of mi-
nority groups, often amplifying negative stereotypes.
Lightweight interventions, such as demographic prim-
ing and native language prompting, partially mitigate
but do not eliminate these cultural gaps. We further
show that downstream evaluations on bias benchmarks
(such as CrowS-Pairs, IndiBias, ThaiCLI, KoBBQ) re-
veal persistent harms and under-representation in sen-
sitive contexts.
Our findings underscore the urgent
need for systematic, regionally grounded audits to en-
sure equitable global deployment of LLMs.
Introduction
Large language models (LLMs) have become essen-
tial tools for accessing information and generating
content, handling billions of prompts from a global
user base (Backlinko 2025; TechCrunch 2025).
How-
ever, this global reach comes with critical challenges.
Trained predominantly on English-centric Internet cor-
pora, LLMs often inherit the cultural biases of their
training data (Bender et al. 2021a; Seth et al. 2025;
Joshi et al. 2020).
This can lead to the marginali-
sation of non-Western viewpoints and, in some cases,
the reinforcement of harmful stereotypes, such as per-
sistent associations between specific religions and vio-
lence Abid, Farooqi, and Zou (2021). As these models
are integrated into education, research, and other ev-
eryday tasks, their potential to shape public discourse
in ways that reinforce existing prejudices becomes a sig-
nificant concern Weidinger, Mellor, and et al. (2021);
Bender et al. (2021b); Santurkar et al. (2023).
While efforts to mitigate such biases are ongoing, re-
search on cultural alignment has largely centred on the
American people and has been conducted almost exclu-
sively in English (Santurkar et al. 2023; Durmus et al.
2023).
This approach not only overlooks the major-
ity of the world’s population but also ignores the fact
that an LLM’s responses can vary significantly depend-
ing on the language of the prompt (Kang and Kim
2025). This linguistic disparity is especially problem-
atic for the vast multilingual user populations in Asia.
For instance, while religion’s role has declined in many
Western nations (Pew Research Center 2025, 2018; Aus-
tralian Bureau of Statistics 2022), it remains a central
and politically significant aspect of society across much
of Asia (The Print 2025; Elvia Muthiariny 2024; Pew
Research Center 2023). For billions of multilingual and
non-English speaking users, ensuring that LLMs are
culturally and linguistically representative is a critical
challenge that must be addressed (Santurkar et al. 2023;
Green et al. 2023).
Given the scale of LLM adoption, a lack of align-
ment risks profound social consequences – this is al-
ready evident on social media, where the proliferation of
AI-generated content has contributed to polarised dis-
course and marginalised certain communities, including
the LGBTQ+ community (Kerwin 2024; Bakshy, Mess-
ing, and Adamic 2015). In this work, we perform an
in-depth, multilingual analysis of LLM cultural align-
ment across several Asian nations, using religion as a
critical lens. We aim to answer the following research
questions:
1. How accurately do contemporary LLMs represent
public opinion on sensitive religious topics, relative
to their performance on broader social issues?
2. Does prompting in a local language mitigate or
worsen existing representational biases towards spe-
cific demographic groups within a country?
3. How do these high-level distributional gaps translate
to concrete representational harms on region-specific
bias benchmarks?

--- Page 2 ---

Figure 1: Evaluation framework for assessing LLMs,
where human opinion distributions from Pew surveys
(India, Sri Lanka, East Asia, and South East Asia) are
compared with model-generated distributions to mea-
sure representativeness across various categories.
To answer these questions, we adopt the Representa-
tiveness metric from (Santurkar et al. 2023) as our pri-
mary measure of alignment, which uses the Wasser-
stein Distance (Villani 2008) to compare a model’s
response distribution against nationally representative
survey data. This metric effectively accounts for the
ordinal structure of many survey answers (e.g., Likert
scales).
For a more robust, multi-faceted analysis, we sup-
plement this with two additional metrics: the Jensen-
Shannon Divergence (Lin 1991) and Hellinger Dis-
tance (Hellinger 1909). These offer a complementary
perspective by treating the answer options as distinct,
non-ordered categories. This allows us to specifically
measure the difference in probability mass a model as-
signs to each individual choice, regardless of its seman-
tic distance from other choices. Together, these met-
rics allow us to pinpoint specific linguistic and demo-
graphic biases from multiple viewpoints. By applying
this framework to evaluate responses in both English
and local languages across diverse Asian nations, we
provide a more nuanced evaluation of global cultural
alignment of language models. Figure 1 provides a sum-
mary of our methodology.
Next, to translate these high-level distributional gaps
into concrete representational harms, we evaluate the
models using a suite of culturally aware bias bench-
marks, to offer geographic and typological coverage:
CrowS-Pairs (Nangia et al. 2020), IndiBias (Sahoo et al.
2024), ThaiCLI (Kim et al. 2025), and KoBBQ (Jin
et al. 2024). Our evaluation reveals that the contempo-
rary models are representative of different Asian pop-
ulation on general topics. However, they consistently
struggle to generate representative opinions involving
religion and identity-related topics. At the same time,
in our bias benchmarks, the LLMs consistently rate neg-
ative framings of religious communities, such as Sunni
and Shia Muslims, as more plausible than positive ones.
This pattern likely reflects both uneven community rep-
resentation and the influence of negative stereotypes
embedded in online discourse.
Overall, our work underscores the need to systemat-
ically evaluate how AI models represent religious and
cultural identities worldwide before their widespread
adoption. To enable further research on this direction,
we have made our codebase and other resources publicly
available on GitHub1.
Related Work
Numerous studies demonstrate that Large Language
Models
(LLMs)
often
reflect
the
cultural
values
of English-speaking and Protestant European na-
tions (Tao et al. 2024; Huang et al. 2023). This has
led to models frequently aligning more closely with
United States-centric viewpoints and failing to capture
community-specific knowledge (Sukiennik et al. 2025;
Etxaniz et al. 2024). Recent comparative audits further
show that LLMs manifest regionally variable degrees of
alignment, with notable misrepresentations persisting
in Asian, African, and Latin American contexts (Bent-
ley, Evans, and Bull 2025; Alkhamissi and Ren 2024).
The lack of culturally representative data can lead to
large gaps in societal and religious viewpoints, a par-
ticularly critical issue in multilingual and plural soci-
eties (Qin et al. 2025; Gamboa, Feng, and Lee 2024).
A cross-lingual evaluation by (del Arco, Pelloni, and
Zampieri 2024) found persistent religious stereotyping
and refusals among LLMs, particularly for minority
faith groups, underscoring the scarcity of systematic
approaches to religion-focused NLP bias.
Measuring and mitigating cultural bias is a com-
plex task. (Khan, Casper, and Hadfield-Menell 2025)
highlights that alignment scores are highly sensitive
to methodological choices like prompt formatting and
question selection, which can even flip the results. Fur-
thermore, popular alignment pipelines like Reinforce-
ment Learning from Human Feedback (RLHF) can per-
petuate biases from the base model, such as those re-
lated to gender (Ovalle et al. 2024; Zhang et al. 2024).
The evaluation process itself can also be flawed, as
LLM-based judges sometimes favour reward style over
substantive accuracy (Feuer et al. 2025).
Various strategies have been proposed to improve
cultural alignment. Recent work on prompt engineer-
ing emphasises the effectiveness and limits of inter-
ventions such as local-language prompting and demo-
graphic priming in mitigating bias (Alkhamissi and Ren
2024; Bentley, Evans, and Bull 2025).
More funda-
mental approaches involve pre-training on targeted lo-
cal data to aid models in acquiring specific cultural
1https://github.com/HariShankar08/LLMOpinions/

--- Page 3 ---

knowledge (Etxaniz et al. 2024). Other techniques op-
erate at a deeper level, such as D2O (Distributional
Dispreference Optimisation), which uses human-labeled
negative examples during training (Duan et al. 2024),
or FairSteer, which applies corrective adjustments to
model activations at inference time without requiring
retraining (Li et al. 2025). While these methods show
promise, their limits for comprehensive cultural adap-
tation are still being explored (Liu, Korhonen, and
Gurevych 2025; Qin et al. 2025), and new metrics are
continuously being developed to enable more precise
measurement of representational harms
(Shin et al.
2024; Hida, Yamaguchi, and Hanawa 2024).
A synthesis of current approaches suggests that scal-
able, region-specific audits and the curation of native
survey data are necessary to ensure LLMs are deployed
equitably worldwide (Qin et al. 2025; del Arco, Pelloni,
and Zampieri 2024; Bentley, Evans, and Bull 2025).
Foundational work by (Santurkar et al. 2023) evaluates
whether model outputs reflect nationally representative
opinion data, providing a methodology for such au-
dits. Our research advances this paradigm by introduc-
ing multilinguality into existing datasets and extending
evaluation beyond Western-centric benchmarks. Specif-
ically, we augment standard resources with data in mul-
tiple languages and systematically test LLMs on tasks
that foreground both religion and multilingual align-
ment, with particular emphasis on India and East/-
Southeast Asia. Leveraging large-scale, nationally rep-
resentative Pew surveys and regionally salient cultural
datasets (Maguire 2017), we address a critical gap: eval-
uating how LLMs align with local public opinion on
religion across diverse linguistic contexts, especially in
societies where religion remains deeply intertwined with
social and political identity.
Establishing Ground Truth: Survey
Data and Bias Benchmarks
A key challenge in auditing LLMs for cultural alignment
is the scarcity of high-quality, large-scale data that re-
flects public opinion outside Western contexts. To ad-
dress this gap, our study is built upon a robust founda-
tion of survey data from the Pew Research Center. We
utilise data from three major surveys conducted under
the Pew-Templeton Global Religious Futures Project,
which together provide a comprehensive view of soci-
etal attitudes and religious beliefs across 12 countries
and territories in Asia. These surveys are: Religion in
India: Tolerance and Segregation (IND) (Sahgal and
Evans 2021), Religion and Views of an Afterlife in East
Asia (EA) (Evans 2024a), and Buddhism, Islam and
Religious Pluralism in South and Southeast Asia (SEA)
(Evans 2024b).
Figure 2 summarises the respondent
counts and regional coverage for each survey.
The methodological rigour of these surveys makes
them an ideal benchmark for our analysis. Data col-
lection for the IND survey was completed in 2021,
while the EA and SEA surveys were completed in
Figure 2: The treemap shows respondent counts from
12 countries/territories across India (green), East Asia
(blue), and Southeast Asia (orange), with block area
proportional to sample size.
These nationally repre-
sentative surveys (Pew Research Center 2021, 2024a,
2024b) form the empirical ground truth for measuring
LLM representativeness, enabling robust cross-country
comparisons on religion and social attitudes.
2024.
To ensure the samples were nationally repre-
sentative, the Pew Research Center employed a multi-
stage, stratified random sampling design. This involved
segmenting each country into primary sampling units
(e.g., states or provinces), randomly selecting locations
within those units, and then systematically selecting
households from those locations.
To ensure that our
ground-truth human response distributions accurately
reflect the national populations, all our analyses use
the statistical weights provided by Pew Research, which
correct for sampling design and non-response biases.
Translation of Survey Questionnaires
While the original surveys were administered in local
languages, the publicly available metadata provides the
survey questions and response options only in English.
To effectively test the multilingual capabilities of LLMs
and align our prompts with the original survey context,
a comprehensive translation of the survey instruments
was required. Due to the scale – 300 questions for Hindi
and 150+ questions for each of the ten other languages
– we need a fully automated translation and valida-
tion pipeline. To ensure accuracy and mitigate model-
specific biases, we first generated initial translations
using an ensemble of three distinct Machine Transla-
tion (MT) APIs: Google Cloud Translation, Microsoft
Translator, and Amazon Translator. For each survey
item, the majority consensus translation was selected as
done in (Macherey and Och 2007). To resolve instances
where all three translations diverged, the output from
Google Cloud Translation was selected, based on its
historically robust performance across a wide range of
languages.

--- Page 4 ---

We then validated each consensus translation for se-
mantic fidelity. For the nine languages supported by
the DeepL platform (DeepL GmbH 2025), its model
was used for back-translation. To ensure an unbiased
validation for the remaining languages (Khmer and
Sinhala), we selected the translation model for back-
translation that was held out from the original con-
sensus process. For instance, we used Microsoft Trans-
late to back-translate a text if the consensus translation
was derived from Google. Subsequently, we calculated
the cosine similarity between the Sentence-BERT em-
beddings of the original English source and the back-
translated text.
Translations achieving a similarity
score of 0.90 or higher were accepted, ensuring our
large-scale corpus meets a high, quantifiable standard
of translation quality (Naik 2024).
To further support this automated framework, we in-
corporated a hybrid validation strategy involving both
human experts and an LLM-as-a-judge. For Hindi and
Tamil, three native speakers for each language indepen-
dently assessed a random sample of 20% of the survey
items, rating them on a 4-point Likert scale for semantic
equivalence and fluency. The manual audit confirmed
a very high level of quality, with 97.2% of the reviewed
translations rated as acceptable or perfect. This pro-
cess yielded a strong inter-annotator agreement score
(Cohen’s κ = 0.84).
Finally, Claude Sonnet 4, acting as the judge model,
was prompted to score each translation on a 5-point
scale across semantic equivalence, fluency, and cultural
appropriateness, and was required to provide a concise
justification for its scores. This scalable approach al-
lowed for a comprehensive audit of all remaining trans-
lated items. The LLM judge assigned an average qual-
ity score of 4.6 out of 5.0 across these languages. This
hybrid validation process thus ensures our multilingual
dataset is both accurate at scale and sensitive to critical
linguistic nuance. The specific languages targeted for
each country are detailed in Table 1.
Country Prompt Languages
Country Prompt Languages
IND
en, hi
KHM
en, km
HKG
en, zh-Hant
IDN
en, id
JPN
en, ja
MYS
en, ms, zh-Hans
KOR
en, ko
SGP
en, ms, zh-Hans, ta
TWN
en, zh-Hant
LKA
en, si, ta
VNM
en, vi
THA
en, th
Table 1: Language coverage by country: for every coun-
try, prompts were issued in both English and one or
more local languages to facilitate a within-country anal-
ysis of language effects. Country names are represented
by ISO 3166-1 Alpha-3 codes, and languages by their
corresponding ISO 639-1 codes.
Bias Evaluation
To comprehensively evaluate the models’ representa-
tiveness and misrepresentation, we use four comple-
Dataset
Primary format
CrowS-Pairs
Pairwise Sentences
IndiBias
Pairwise / Judgment (English + Hindi)
ThaiCLI
Question / Chosen / rejected
KoBBQ
QA / templates (template-expanded)
Table 2: Cross-cultural benchmarks used to evaluate
bias and representational harms in LLMs. These cor-
pora span multiple regions and task formats—pair-
wise judgments (CrowS-Pairs,
IndiBias),
culturally
grounded question-answering (KoBBQ), and culturally
sensitive response scoring (ThaiCLI).
mentary, culturally-aware bias benchmarks:
CrowS-
Pairs
(Nangia et al. 2020), IndiBias
(Sahoo et al.
2024), ThaiCLI (UpstageAI 2025; Kim et al. 2025), and
KoBBQ (Jin et al. 2024). Together, these corpora allow
(i) measuring pairwise stereotyping tendencies in both
masked and generative language, (ii) targeted prob-
ing of representational harms in Indian contexts (En-
glish/Hindi), (iii) evaluating Thai cultural/pragmatic
alignment, and (iv) QA-style bias assessment in Korean.
These benchmarks provide broader geographic and ty-
pological coverage, and enable cross-cultural compari-
son of representational performance. We provide a sum-
mary of the same in Table 2.
CrowS-Pairs
We use CrowS-Pairs as a foundational benchmark to
measure general stereotyping preferences. Nangia et al.
(2020) consists of sentence pairs that contrast stereo-
typical and non-stereotypical statements. Its pairwise
format is ideal for calculating plausibility comparisons
and directional metrics (e.g., pairwise win rates or
ΔELO style plausibility differences), offering a clear,
language-neutral baseline for misrepresentation.
IndiBias
IndiBias is a benchmark designed specifically for the
South Asian context. Sahoo et al. (2024) is uniquely
designed to test for biases along India-relevant iden-
tity axes (e.g., religion, caste, region, gender, occupa-
tion) in both English and Hindi. While smaller than
some Western-centric corpora, IndiBias fills a crucial
gap by explicitly testing representational harms related
to South Asian identities and evaluating multilingual
model behaviour in this domain.
ThaiCLI
The ThaiCLI (Kim et al. 2025), benchmark evaluates
the alignment of large language models (LLMs) with
Thai cultural norms using a set of Question, Chosen,
Rejected triplets, where each question is paired with
both a culturally appropriate (Chosen) and inappropri-
ate (Rejected) answer. The benchmark presents seven
thematic domains, like royal family, religion, culture,

--- Page 5 ---

economy, humanity, lifestyle, and politics, in two dis-
tinct formats. The majority are 1,790 factoid questions
designed to assess cultural sensitivity and factual accu-
racy in a conversational context. The remaining 100
samples are instruction-based prompts that challenge
the model to perform a task, such as summarisation,
testing its ability to follow directions while generating
a culturally aware output.
KoBBQ
The Korean Bias Benchmark for QA (KoBBQ) adapts
the BBQ/BBQ-style methodology (Parrish et al. 2021)
to Korean QA settings using template expansions and
culturally localised target lists (Jin et al. 2024). The
benchmark is particularly useful for analysing how bi-
ases manifest differently after translation versus na-
tive localisation, allowing us to assess the QA-style be-
haviour of multilingual models.
Measuring Cultural Alignment and Bias
Following the methodology of (Santurkar et al. 2023),
we quantitatively measure how a model leans toward
different opinions. We frame each survey question as a
Multiple-Choice Question, and prompt the model to de-
rive a probability distribution over the answer options
(e.g.
‘A’, ‘B’, ‘C’). For models accessed via an API,
we construct this probability distribution using the top
twenty log-probabilities/log-probs. To ensure a deter-
ministic output, the model temperature is set to zero.
We call this the Model Opinion Distribution, denoted
as DM. For models that can be run locally2, we extract
DM distribution directly from the full next-token logit
vector, which encodes the probabilities of selecting each
of the tokens in the model’s vocabulary.
For comparison, we establish a Human Opinion Dis-
tribution from the survey data for each question, where
each respondent is associated with a weight. This dis-
tribution is calculated by summing the weights for each
answer choice across all respondents and then normal-
ising the resulting totals. Our analysis then compares
this human distribution to the model’s distribution to
measure the representativeness of each LLM.
Representativeness
Representativeness measures how well a Language
Model’s default opinion distribution matches that of a
human population. For each survey question, we com-
pare the model’s opinion distribution (DM) with the
human opinion distribution (DO). To quantify align-
ment, we employ three distance metrics, each converted
into an alignment score bounded between 0 and 1.
As our base metric, we use the formulation of Rep-
resentativeness as proposed by (Santurkar et al. 2023).
The metric employs Wasserstein Distance (WD), which
2Our local experiments were conducted on a server
equipped with three NVIDIA RTX 5000 GPUs.
effectively accounts for the ordinal structure of the an-
swer options. Alignment between two distributions D1
and D2 over a set of questions Q is defined as:
AW D(D1, D2; Q) =
1
|Q|
∑
q∈Q
(
1 −WD(D1(q), D2(q))
N −1
)
,
(1)
where N is the number of answer choices for each
question.
Based on this equation, the representativeness of a
language model M with respect to the population O
on a set of questions Q is therefore:
RO
M(Q) = AW D(DM, DO; Q),
(2)
We use the shorthand RM to refer to the representa-
tiveness of the model, as calculated by the above equa-
tion.
To further support the initial metric, we also measure
the Jensen-Shannon Divergence (JSD) and Hellinger
Distance (HD) to compare the model distribution DM
and human distribution (DO or DG). Their correspond-
ing alignment scores are as follows:
AJSD
(
DM, DG; Q
)
=
1
|Q|
∑
q∈Q
(
JSD
(
DM(q), DG(q)
))
,
(3)
AHD
(
DM, DG; Q
)
=
1
|Q|
∑
q∈Q
(
H
(
DM(q), DG(q)
))
.
(4)
Each metric discussed above is bounded between 0
and 1. For RM, which is formulated as an alignment
score, a higher value indicates better representative-
ness. Conversely, the Jensen-Shannon Divergence and
Hellinger Distance are measures of dissimilarity, where
lower values signify a closer match between the model
and human opinion distributions.
Evaluation on Bias Benchmarks
CrowS-Pairs
We evaluate bias using the religion
subset of CrowS-Pairs by converting each minimal pair
into a binary-choice prompt that asks the model to
“Choose the more socially acceptable sentence” and to
reply with only a single option code (1 or 2). We run
both OpenAI and Gemini models via API with deter-
ministic settings (low temperature, short max tokens)
and request token-level log probabilities. When a model
returns prose, we parse the first numeric choice; if ab-
sent, we fall back to the first step where the logprobs
indicate emission of ‘1’ or ‘2.’ Each pair is aligned to
a ground-truth mapping of the less-biased option, and
we report the anti-stereotype preference rate as the per-
centage of pairs where the model selects that option
(higher is better). We discard malformed responses that
do not yield a recoverable choice.

--- Page 6 ---

IndiBias
We
evaluated
large
language
models
(LLMs) on the IndiBias benchmark’s religion plausibil-
ity task, which presents pairs of positive (pro-identity)
and
negative
(anti-identity)
scenarios
for
Indian
religious identities and asks the model to select the
more plausible scenario.
Using the oﬀicial pipeline,
we generated prompts with GPT-4o-Mini and then
ran both GPT-4o-Mini (via the OpenAI API) and
Gemini-2.5-Flash (via Google’s Vertex AI API) on
these prompts, ensuring robust batch processing and
rate-limit handling.
For each model, we computed
ELO scores (Sahoo et al. 2024) for every identity
in both positive and negative splits, and defined a
misrepresentation score as the difference between neg-
ative and positive ELOs (ΔELO), where higher values
indicate a greater tendency to normalise negative
framings for that identity. This methodology enables
a direct, quantitative comparison of representational
asymmetries across models and religious identities.
ThaiCLI
To
assess
model
outputs,
an
LLM‑as‑a‑Judge paradigm has been used:
a strong
LLM (GPT‑4o,
stable version) is used to rate a
model’s generated answer for each question given the
Chosen/Rejected examples, on a scale from 1 to 10
along with an explanation.
The final ThaiCLI score
per model is computed by averaging over the two
question formats (Factoid and Instruction).
If score
extraction fails (via regular‐expression matching) in
the Judge’s response, the judgement is re-generated up
to a fixed number of attempts, with zero assigned only
if it still fails.
KoBBQ
We evaluate our models on the test split
of the KoBBQ benchmarking, constructing multiple-
choice prompts from the evaluation templates.
The
models are subsequently queried deterministically by
setting the temperature as zero. To extract the answer,
we parse the first instance of ‘A’, ‘B’, or ‘C’ from Ope-
nAI responses. For Gemini, we use structured output
constrained to the enum {A, B, C}.
We report over-
all accuracy and also break down performance by bbq-
category and by label-annotation (ambiguous vs disam-
biguated).
Experimental Evaluation
We
evaluate
GPT-4o-Mini
and
Gemini-2.5-Flash.
Gemini-2.5-Flash attains a high overall representative-
ness of 93% but falls to ≈87% on religion-related
prompts; GPT-4o-Mini shows a similar pattern (￿94%
overall vs ≈86% on religion). This decline is supported
by increases in Jensen–Shannon (JSD) and Hellinger
distance(HD) on the religion subset, with larger gaps
for GPT-4o-Mini (AJSD +0.20; AHD +0.18) than for
Gemini-2.5-Flash (AJSD +0.15; AHD +0.12), indicat-
ing greater relative degradation for religion items. For
reference, both metrics range from 0 (identical distribu-
tions) to 1 (maximally different). Notably, we find that
simple prompt-based steering – e.g., prefixing prompts
with demographic context such as “You are a citizen
Gemini-2.5-Flash
GPT-4o-Mini
0
50
100
93
94
87
86
96.57
98.41
Representativeness score (%)
Overall
Religion-related
Post-Steering
Figure 3: Representativeness scores ((RM) of GPT-4o-
Mini and Gemini-2.5-Flash on general versus religion-
related items. While both models achieve high overall
representativeness (>90%), their scores drop markedly
on religion-related prompts (≈7-8% lower).
KOR
VNM
IND
SGP
JPN
LKA
−6
−3
0
·10−2
∆H = Hlocal −HEN (negative = improvement)
Figure 4: Change in Hellinger distance (∆H = Hlocal −
HEN) when switching from English to local-language
prompts for Gemma-3-12B across multiple locales.
Negative values (bars below zero) indicate that local-
language prompting reduces the divergence between
model and human distributions.
of...” – can shift model outputs toward the target distri-
bution and reduce measured distributional divergence
on religion-related queries, as shown in Figure 3.
The
open-weight
models
selected
in
our
audit
(Gemma-3-12B-IT, Llama-3.2-1B-Instruct, Mistral-7B-
Instruct) (Google Research 2025; Meta AI 2024; Mis-
tral AI 2024) broadly mirror the pattern observed in
GPT-4o-Mini and Gemini-2.5-Flash:
achieving high
representativeness RM on non-religion prompts, yet
continue to display a distributional miscalibration on
prompts concerning religion and identity.
Gemma-3-
12B-IT keeps RM ≈0.96; struggling the most in coun-
tries of East Asia (AJSD ≈0.45; AHD ≈0.50). No-
tably, in Sri Lanka, switching from English to Sinhala
prompts yields a sharp improvement (AJSD : 0.465 →
0.320; ∆≈−0.15); AHD mirrors this with a decline in
divergence: (≈0.49→0.47). We visualize the variation
of AHD with language in Figure 4.

--- Page 7 ---

0.4
0.6
0.8
1
Gemma-3-12B
(SL: Sinhala vs EN)
Llama-3.2-1B
(Tw: ZH vs EN)
Mistral-7B
(Kr: KO vs EN)
Jensen–Shannon Distance (lower is better)
Local-language prompt
English prompt
Figure 5: Effect of prompt language on religion-related
items across distinct model–country pairs (Kr = Korea,
Tw = Taiwan, SL = Sri Lanka). Lower Jensen–Shan-
non distance indicates better alignment.
Llama-3.2-1B performs similarly, with RM ≈0.93 −
0.97. In Taiwan, replacing English prompts with Chi-
nese results in a modest but consistent reduction in di-
vergence (AJSD : 0.876 →0.808), while Hellinger Dis-
tance remains high and nearly unchanged (≈0.86).
Mistral-7B sustains RM > 0.91 overall but exhibits
the sharpest religion-related spikes in Southeast Asia
(AJSD ≈0.65 in Cambodia/Indonesia; AHD ≈0.52).
In Korea, however, local-language prompting reduces
divergence slightly (0.527 →0.477) while AHD remains
stable (≈0.48).
Figure 5 demonstrates these results, contrasting
Jensen–Shannon distances under local-language versus
English prompts for each model–country pair. Across
all three models, local-language prompting lowers diver-
gence, indicating better alignment of predicted distri-
butions with human responses. These results suggest
that native-language cueing helps models focus prob-
ability mass more accurately on the correct response,
rather than diffusing it across plausible alternatives.
Across models, the largest residual errors occur on
near-consensus items (e.g., QCURREL, QGOD, DE-
MONYM), where models reliably select the correct
mode but still assign residual probability to incor-
rect options, artificially inflating AJSD and AHD.
Lightweight, edge-friendly interventions—such as brief
demographic preambles and native-language prompts—
consistently narrow these gaps without degrading RM,
offering a practical pathway for improving alignment in
low-resource or multilingual contexts.
IndiBias:
Plausibility and Misrepresentation
Analysis
We find that GPT-4o-Mini exhibits clear
calibration gaps across identities.
The most mis-
represented groups, as indicated by high ∆ELO, are
Shia (+28.9), Sunni (+23.3), Jain (+16.8), and Parsi
(+16.5),
with smaller effects for Buddhist (+4.3)
and Bahai (+4.1).
Conversely, Hindu (−13.0), Sufi
(−10.1), Sikh (−9.3), Christian (−5.0), and Bohra
Muslim (−1.2) exhibit negative or minimal misrep-
−20
−10
0
10
20
30
Shia
Sunni
Jain
Parsi
Buddhist
Bahai
Hindu
Sufi
Sikh
Christian
Bohra Muslim
∆>0 (neg. > pos.)
∆<0 (pos. > neg.)
∆ELO (higher = more misrep.)
Figure 6: Misrepresentation of Indian religious identi-
ties on IndiBias using GPT-4o-Mini. The plot shows
∆ELO = ELOneg −ELOpos, where positive values in-
dicate that negative descriptions are judged more plau-
sible than positive ones.
Several minority identities
(Shia, Sunni, Jain, Parsi) show strong misrepresenta-
tion, while others (Hindu, Sikh, Sufi) show the oppo-
site trend, highlighting systematic group-specific cali-
bration gaps.
resentation, indicating higher plausibility for positive
framings.
This pattern suggests that negative de-
scriptions are disproportionately normalized for certain
identities, evidencing persistent group-specific miscal-
ibration.
Gemini-2.5-Flash shows broadly convergent
trends; for instance, Sunni also exhibits elevated nega-
tive plausibility (∆ELO > 0). These results (see Fig-
ure 6) highlight the need for careful evaluation of de-
mographic representativeness and fairness in LLM out-
puts.
KoBBQ: Disambiguation and Calibration on
Korean Identity Benchmarks
On GPT-4o-Mini,
we observe substantial gains in model calibration with
disambiguation: Overall accuracy rises from 0.611 (am-
biguous) to 0.961 (disambiguated). Religion-related ac-
curacy improves from 0.625 to 0.950. Differential bias
(religion) decreases sharply, from 0.275 (ambiguous)
to 0.100 (disambiguated). All other demographic axes
(e.g., race, gender, education) exhibit similar improve-
ments with disambiguation (see Figure 7). These re-
sults highlight the critical role of prompt specificity in
mitigating group-level calibration failures in LLM out-
puts.
CrowS-Pairs: Cross-Lingual Stereotype Probing
Our results (see Figure 8) reveal that GPT-4o-Mini is
consistently robust, selecting the anti-stereotype option
in ∼92% of cases (bias rate ∼8%), with zero invalids
across all languages. In contrast, Gemini-2.5-Flash ex-
hibits higher bias rates (∼16%), lower anti-stereotype
accuracy (∼68%), and a notable fraction of invalid re-
sponses (15–19/105), especially in Vietnamese. These
findings indicate that while GPT-4o-Mini robustly re-

--- Page 8 ---

Overall
Religion
Bias (Rel.)
0
0.5
1
Score
Ambiguous
Disambiguated
Figure 7: Effect of prompt disambiguation on GPT-
4o-Mini performance on the KoBBQ Korean identity
benchmark.
Disambiguating prompts improves over-
all accuracy (0.611→0.961) and religion-related ac-
curacy (0.625→0.950), while sharply reducing bias
(0.275→0.100).
en
hi
ja
ko
vi
zh
0
20
40
60
80
100
% (or count)
GPT-4o bias
Gemini bias
GPT-4o anti-stereo
Gemini anti-stereo
Figure 8:
Cross-lingual bias rates on the religion-
only subset of CrowS-Pairs across six languages (105
items/locale).
GPT-4o-Mini shows low bias (≈8%)
and high anti-stereotype accuracy (≈92%) consistently
across languages. Gemini-2.5-Flash exhibits higher bias
(≈16%), lower anti-stereotype accuracy (≈68%), and
more invalid responses, indicating weaker cross-lingual
stereotype resistance.
sists religious stereotyping across languages, Gemini-
2.5-Flash is both more prone to stereotype selections
and more likely to abstain or produce off-format out-
puts, raising concerns about cross-lingual consistency
and safety filtering.
ThaiCLI: Cultural Sensitivity in Thai
Results
show that GPT-4o-Mini highly aligned with Thai cul-
tural norms, achieving average scores above 8.3 across
both factoid and instruction prompts scoring 8.10 on 10,
and maintaining consistently high performance across
sensitive themes such as religion and royal family.
Gemini-2.5-Flash also demonstrates strong cultural sen-
sitivity, with a score of 7.52 on 10, but lags behind
OpenAI in both absolute score and consistency.
Discussion
This study reveals significant disparities in the cultural
alignment of open Large Language Models (LLMs)
across diverse Asian nations. While models like GPT-
4o-mini and Gemini-2.5-flash demonstrate high overall
representativeness on general social topics, they consis-
tently falter when representing public opinion on the
sensitive domain of religion. This observed misalign-
ment does not seem to be limited to interactions in
English.
The study indicates that these representa-
tional gaps persist, and in some cases are even ampli-
fied, when the models are prompted in various local
languages.
This pattern suggests that the challenge
may be deeply rooted in the models’ predominantly
English-centric training data and subsequent alignment
processes, rather than being a simple tool for transla-
tion.
The persistence of these gaps across multiple lan-
guages raises important considerations for the global
deployment of these technologies. It points to a poten-
tial risk of propagating a specific cultural viewpoint,
often one that is more aligned with Western contexts,
even when users are interacting in their native tongue.
This challenges the notion that multilingual capability
alone is suﬀicient for equitable performance across dif-
ferent cultural settings.
At the same time, this research introduces a layer
of complexity to this narrative.
It was found that
lightweight interventions, such as using a local language
or providing demographic context in the prompt, can
sometimes lead to partial improvements in alignment
scores. This may indicate that the models possess some
latent cultural knowledge that is not always activated
by default, hinting at potential avenues for developing
more effective steering and fine-tuning methods in the
future.
Limitations and Future Work
While this study provides a broad analysis, its method-
ology has certain constraints, which in turn high-
light opportunities for future work.
A key consider-
ation is the reliance on an extensive but largely au-
tomated translation pipeline for the survey questions.
Although a rigorous, multi-stage validation process in-
volving back-translation and human audits was imple-
mented, it is possible that subtle linguistic or cultural
nuances across the eleven target languages were not
fully captured, which could have influenced model re-
sponses. A foundational step would be the curation of
large-scale, diverse, and genuinely multilingual datasets
sourced directly from non-Western cultural contexts,
rather than relying on materials translated from En-
glish. Such resources would build a more globally rep-
resentative foundation for these models.

--- Page 9 ---

Furthermore, using religious opinion as a primary
lens for investigating cultural values offers a critical but
not exhaustive view. The cultural fabric of any society
is woven from many threads, and other dimensions such
as political ideologies, regional identities, and social hi-
erarchies are also important areas that would benefit
from similar in-depth, multilingual analysis.
Future research should also focus on developing and
evaluating more sophisticated steering techniques that
go beyond simple prompting.
The goal would be to
explore methods that help models adapt to diverse cul-
tural norms at a more fundamental level. This line of
inquiry could help foster the development of LLMs that
are not just multilingual in their textual output but are
more multicultural in their underlying understanding,
thereby addressing the kinds of representational gaps
that this audit has brought to light.
References
Abid, A.; Farooqi, M.; and Zou, J. 2021. Large lan-
guage models associate Muslims with violence. Nature
Machine Intelligence, 3(6): 461–463.
Alkhamissi, M.; and Ren, X. 2024. Investigating Cul-
tural Alignment of Large Language Models.
In Pro-
ceedings of the 62nd Annual Meeting of the Association
for Computational Linguistics. Association for Compu-
tational Linguistics. Long Paper.
Australian Bureau of Statistics. 2022. Census of Popu-
lation and Housing: Reflecting Australia—Stories from
the Census, 2021.
Backlinko. 2025.
ChatGPT Users: ChatGPT Usage
Statistics (2025). Accessed: 2025-08-21.
Bakshy, E.; Messing, S.; and Adamic, L. A. 2015. Expo-
sure to ideologically diverse news and opinion on Face-
book. Science, 348(6239): 1130–1132.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021a. On the dangers of stochastic par-
rots: Can language models be too big? In Proceedings
of the 2021 ACM conference on fairness, accountability,
and transparency, 610–623.
Bender, E. M.; Gebru, T.; McMillan-Major, A.; and
Shmitchell, S. 2021b.
On the Dangers of Stochastic
Parrots: Can Language Models Be Too Big?
In Pro-
ceedings of the ACM Conference on Fairness, Account-
ability, and Transparency (FAccT).
Bentley, S. V.; Evans, D.; and Bull, P. E. 2025. What
social stratifications in bias blind spot can tell us about
implicit social bias in both LLMs and humans. Scien-
tific Reports, 15: 14875.
DeepL GmbH. 2025.
DeepL API —Documentation.
https://developers.deepl.com/. Developer documenta-
tion for the DeepL API. Accessed 2025-09-01.
del Arco, F. P.; Pelloni, T.; and Zampieri, M. 2024. Di-
vine LLaMAs: Bias, Stereotypes, Stigmatization, and
Refusal Behaviors of Language Models for Judaism and
Islam. In Findings of the Association for Computational
Linguistics: EMNLP 2024, 12300–12313. Association
for Computational Linguistics.
Duan, S.; Yi, X.; Zhang, P.; Liu, Y.; Liu, Z.; Lu, T.;
Xie, X.; and Gu, N. 2024. Negating Negatives: Align-
ment with Human Negative Samples via Distributional
Dispreference Optimization. In Conference on Empiri-
cal Methods in Natural Language Processing (EMNLP).
Durmus, E.; Nyugen, K.; Liao, T. I.; Schiefer, N.;
Askell, A.; Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.;
Hernandez, D.; Joseph, N.; et al. 2023. Towards mea-
suring the representation of subjective global opinions
in language models. arXiv preprint arXiv:2306.16388.
Elvia Muthiariny, D. 2024. Indonesia Ranks Highest in
Global Religious Devotion. Tempo.co. Based on Pew
Research Center survey (2008–2023).
Etxaniz, J.; Azkune, G.; Soroa, A.; de Lacalle, O. L.;
and Artetxe, M. 2024. BertaQA: How Much Do Lan-
guage Models Know About Local Culture? In Proceed-
ings of the Annual Conference on Neural Information
Processing Systems (NeurIPS).
Evans, J. 2024a. East Asian Societies Survey Dataset.
Evans, J. 2024b.
South and Southeast Asia Survey
Dataset.
Feuer, B.; Goldblum, M.; Datta, T.; Nambiar, S.; Be-
saleli, R.; Dooley, S.; Cembalest, M.; and Dickerson,
J. P. 2025. Style Outweighs Substance: Failure Modes
of LLM Judges in Alignment Benchmarking. In The
Thirteenth International Conference on Learning Rep-
resentations (ICLR).
Gamboa, L. C. L.; Feng, Y.; and Lee, M. 2024. Social
Bias in Multilingual Language Models: A Survey. arXiv
preprint arXiv:2508.20201.
Gebru, T.; Morgenstern, J.; Vecchione, B.; Vaughan,
J. W.; Wallach, H.; III, H. D.; and Crawford, K. 2021.
Datasheets for Datasets. Communications of the ACM,
64(12): 86–92.
Google Research. 2025.
Gemma 3 12B-It.
https:
//huggingface.co/google/gemma-3-12b-it.
Green, J.; et al. 2023. ChatGPT Has Been Sucked Into
India’s Culture Wars. Wired. News account of pub-
lic controversy documenting asymmetric ChatGPT re-
sponses to jokes about religious figures. Accessed 2025-
09-01.
Hellinger,
E. 1909.
Neue Begründung der The-
orie
quadratischer
Formen
von
unendlichvielen
Veränderlichen. Journal für die reine und angewandte
Mathematik, 136: 210–271.
Hida, N.; Yamaguchi, K.; and Hanawa, K. 2024. Social
Bias Evaluation for Large Language Models Requires
Prompt Variations. arXiv preprint arXiv:2407.18376.
Huang, H.; Yu, F.; Zhu, J.; Sun, X.; Cheng, H.; Song,
D.; Chen, Z.; Alharthi, A.; An, B.; Liu, Z.; Zhang, Z.;
Chen, J.; Li, J.; Wang, B.; Zhang, L.; Sun, R.; Wan,
X.; Li, H.; and Xu, J. 2023. AceGPT, Localizing Large
Language Models in Arabic. In North American Chap-
ter of the Association for Computational Linguistics
(NAACL).

--- Page 10 ---

Jin, J.; Kim, J.; Lee, N.; Yoo, H.; Oh, A.; and Lee,
H. 2024. Kobbq: Korean bias benchmark for question
answering. Transactions of the Association for Compu-
tational Linguistics, vol. 12, pp. 507–524.
Joshi, P.; Santy, S.; Budhiraja, A.; Bali, K.; and
Choudhury, M. 2020. The State and Fate of Linguistic
Diversity and Inclusion in the NLP World. In Proceed-
ings of the 58th Annual Meeting of the Association for
Computational Linguistics, 6282–6293. Association for
Computational Linguistics. Highlights lack of represen-
tation for many languages in NLP resources.
Kang, E.; and Kim, J. 2025. LLMs Are Globally Mul-
tilingual Yet Locally Monolingual: Exploring Knowl-
edge Transfer via Language and Thought Theory. arXiv
preprint arXiv:2505.24409.
Kerwin, P. 2024. How Should AI Depict Marginalized
Communities? CMU Technologists Look to a More In-
clusive Future. Accessed September 12, 2025.
Khan, A.; Casper, S.; and Hadfield-Menell, D. 2025.
Randomness, Not Representation: The Unreliability of
Evaluating Cultural Alignment in LLMs. Proceedings of
the 2025 ACM Conference on Fairness, Accountability,
and Transparency (FAcct).
Kim, D.; Lee, S.; Kim, Y.; Rutherford, A.; and Park,
C. 2025.
Representing the Under-Represented: Cul-
tural and Core Capability Benchmarks for Developing
Thai Large Language Models. In Proceedings of the 31st
International Conference on Computational Linguis-
tics. International Committee on Computational Lin-
guistics.
Li, Y.; Fan, Z.; Chen, R.; Gai, X.; Gong, L.; Zhang, Y.;
and Liu, Z. 2025. FairSteer: Inference Time Debiasing
for LLMs with Dynamic Activation Steering.
Lin, J. 1991. Divergence measures based on the Shan-
non entropy. IEEE Transactions on Information The-
ory, 37(1): 145–151.
Liu, C. C.; Korhonen, A.; and Gurevych, I. 2025. Cul-
tural Learning-Based Culture Adaptation of Language
Models.
In Che, W.; Nabende, J.; Shutova, E.; and
Pilehvar, M. T., eds., Proceedings of the Association
for Computational Linguistics (ACL).
Macherey, W.; and Och, F. J. 2007. An Empirical Study
on Computing Consensus Translations from Multiple
Machine Translation Systems.
In Proceedings of the
2007 Joint Conference on Empirical Methods in Natural
Language Processing and Computational Natural Lan-
guage Learning (EMNLP–CoNLL), 986–995. Prague,
Czech Republic: Association for Computational Lin-
guistics. Consensus / system combination methods for
producing a single translation hypothesis from multiple
candidates.
Maguire, E. 2017. How East and West think in pro-
foundly different ways. BBC Future. BBC Future Se-
ries.
Meta AI. 2024.
Llama 3.2 1B Instruct.
https://
huggingface.co/meta-llama/Llama-3.2-1B-Instruct.
Mistral AI. 2024. Mistral 7B Instruct v0.3. https://
huggingface.co/mistralai/Mistral-7B-Instruct-v0.3.
Naik, N. 2024.
Probabilistic Consensus through En-
semble Validation: A Framework for LLM Reliability.
arXiv preprint.
Recent ensemble→validation frame-
work repurposing model ensembles as a consensus-
based validator for LLM outputs (improves precision
via inter-model agreement). Accessed 2025-09-01.
Nangia, N.; Vania, C.; Bhalerao, R.; and Bowman, S. R.
2020. CrowS-Pairs: A Challenge Dataset for Measuring
Social Biases in Masked Language Models. In Webber,
B.; Cohn, T.; He, Y.; and Liu, Y., eds., Proceedings of
the 2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP).
Ovalle, A.; Pavasovic, K. L.; Martin, L.; Zettlemoyer,
L.; Smith, E. M.; Chang, K.-W.; Williams, A.; and Sa-
gun, L. 2024. The Root Shapes the Fruit: On the Persis-
tence of Gender-Exclusive Harms in Aligned Language
Models. In Proceedings of the 2025 ACM Conference on
Fairness, Accountability, and Transparency (FAccT).
Parrish, A.; Chen, A.; Nangia, N.; Padmakumar, V.;
Phang, J.; Thompson, J.; Htut, P. M.; and Bowman,
S. R. 2021.
BBQ: A hand-built bias benchmark for
question answering. arXiv preprint arXiv:2110.08193.
Pew Research Center. 2018. Being Christian in Western
Europe.
Pew Research Center. 2023. 5 facts about religion in
South and Southeast Asia.
Pew Research Center. 2025.
Modeling the Future of
Religion in America: Recent Trends and Projections.
Qin, Y.; Wang, L.; Tan, Z.; and Li, H. 2025. A Survey
on Large Language Models with Multilingualism. arXiv
preprint arXiv:2405.10936.
Sahgal, N.; and Evans, J. 2021. India Survey Dataset.
Sahoo, N.;
Kulkarni, P.;
Ahmad, A.;
Goyal, T.;
Asad, N.; Garimella, A.; and Bhattacharyya, P. 2024.
IndiBias: A Benchmark Dataset to Measure Social Bi-
ases in Language Models for Indian Context. In Duh,
K.; Gomez, H.; and Bethard, S., eds., Proceedings of
the 2024 Conference of the North American Chapter of
the Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers).
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang,
P.; and Hashimoto, T. 2023. Whose opinions do lan-
guage models reflect? In International Conference on
Machine Learning, 29971–30004. PMLR.
Seth, A.; Choudhary, M.; Sitaram, S.; Toyama, K.;
Vashistha, A.; and Bali, K. 2025. How Deep Is Rep-
resentational Bias in LLMs? The Cases of Caste and
Religion. arXiv preprint arXiv:2508.03712.
Shin, J.; Song, H.; Lee, H.; Jeong, S.; and Park, J.
2024. Ask LLMs Directly, “What shapes your bias?”
: Measuring Social Bias in Large Language Models. In
Findings of the Association for Computational Linguis-
tics: ACL 2024, 16122–16143. Bangkok, Thailand: As-
sociation for Computational Linguistics.

--- Page 11 ---

Sukiennik, N.; Gao, C.; Xu, F.; and Li, Y. 2025.
An Evaluation of Cultural Value Alignment in LLM.
ArXiv.
Tao, Y.; Viberg, O.; Baker, R. S.; and Kizilcec, R. F.
2024. Cultural bias and cultural alignment of large lan-
guage models. PNAS nexus, 3(9): pgae346.
TechCrunch. 2025.
ChatGPT Users Send 2.5 Billion
Prompts a Day, OpenAI Tells Axios. Accessed: 2025-
08-21.
The Print. 2025. 24% Indians identify as religious na-
tionalists; 57% Hindus feel religious texts should shape
laws: Pew. The Print.
UpstageAI. 2025. ThaiCLI and Thai-H6 Benchmarks.
https://github.com/UpstageAI/ThaiCLI_H6. GitHub
repository.
Villani, C. 2008.
Optimal transport:
old and new.
Springer.
Weidinger, L.; Mellor, J. F. J.; and et al. 2021. Ethical
and social risks of harm from Language Models. arXiv
preprint arXiv:2112.04359.
Wilkinson, M. D.; Dumontier, M.; Aalbersberg, I. J.;
Appleton, G.; Axton, M.; Baak, A.; Blomberg, N.;
Boiten, J.-W.; da Silva Santos, L. B.; Bourne, P. E.;
Bouwman, J.; Brookes, A. J.; Clark, T.; Crosas, M.;
Dillo, I.; Dumon, O.; Edmunds, S.; Evelo, C. T.;
Finkers, R.; Gonzalez-Beltran, A.; Gray, A. J.; Groth,
P.; Goble, C.; Grethe, J. S.; Heringa, J.; ’t Hoen, P. A.;
Hooft, R.; Kuhn, T.; Kok, R.; Kok, J.; Lusher, S. J.;
Martone, M. E.; Mons, A.; Packer, A. L.; Persson, B.;
Rocca-Serra, P.; Roos, M.; van Schaik, R.; Sansone,
S.-A.; Schultes, E.; Sengstag, T.; Slater, T.; Strawn,
G.; Swertz, M. A.; Thompson, M.; van der Lei, J.; van
Mulligen, E.; Velterop, J.; Waagmeester, A.; Witten-
burg, P.; Wolstencroft, K.; Zhao, J.; and Mons, B. 2016.
The FAIR Guiding Principles for scientific data man-
agement and stewardship. Scientific Data, 3: 160018.
Zhang, D.; Yu, Y.; Li, C.; Dong, J.; Su, D.; Chu, C.;
and Yu, D. 2024. MM-LLMs: Recent Advances in Mul-
tiModal Large Language Models. In Annual Meeting of
the Association for Computational Linguistics (ACL).

--- Page 12 ---

Paper Checklist
1. For most authors...
(a) Would answering this research question advance
science without violating social contracts, such as
violating privacy norms, perpetuating unfair pro-
filing, exacerbating the socio-economic divide, or
implying disrespect to societies or cultures? Yes
(b) Do your main claims in the abstract and introduc-
tion accurately reflect the paper’s contributions
and scope? Yes
(c) Do you clarify how the proposed methodological
approach is appropriate for the claims made? Yes
(d) Do you clarify what are possible artifacts in the
data used, given population-specific distributions?
Yes
(e) Did you describe the limitations of your work? Yes
(f) Did you discuss any potential negative societal im-
pacts of your work? NA
(g) Did you discuss any potential misuse of your work?
Yes
(h) Did you describe steps taken to prevent or miti-
gate potential negative outcomes of the research,
such as data and model documentation, data
anonymization, responsible release, access control,
and the reproducibility of findings? Yes
(i) Have you read the ethics review guidelines and
ensured that your paper conforms to them? Yes
2. Additionally, if your study involves hypotheses test-
ing...
(a) Did you clearly state the assumptions underlying
all theoretical results? Yes
(b) Have you provided justifications for all theoretical
results? Yes
(c) Did you discuss competing hypotheses or theories
that might challenge or complement your theoret-
ical results? Yes
(d) Have you considered alternative mechanisms or
explanations that might account for the same out-
comes observed in your study? Yes
(e) Did you address potential biases or limitations in
your theoretical framework? Yes
(f) Have you related your theoretical results to the
existing literature in social science? Yes
(g) Did you discuss the implications of your theoreti-
cal results for policy, practice, or further research
in the social science domain? Yes
3. Additionally, if you are including theoretical proofs...
(a) Did you state the full set of assumptions of all
theoretical results? NA
(b) Did you include complete proofs of all theoretical
results? NA
4. Additionally, if you ran machine learning experi-
ments...
(a) Did you include the code, data, and instructions
needed to reproduce the main experimental results
(either in the supplemental material or as a URL)?
Yes
(b) Did you specify all the training details (e.g., data
splits, hyperparameters, how they were chosen)?
Yes
(c) Did you report error bars (e.g., with respect to the
random seed after running experiments multiple
times)? NA
(d) Did you include the total amount of compute and
the type of resources used (e.g., type of GPUs,
internal cluster, or cloud provider)? Yes
(e) Do you justify how the proposed evaluation is suf-
ficient and appropriate to the claims made? Yes
(f) Do you discuss what is “the cost” of misclassifica-
tion and fault (in)tolerance? NA
5. Additionally, if you are using existing assets (e.g.,
code, data, models) or curating/releasing new assets,
without compromising anonymity...
(a) If your work uses existing assets, did you cite the
creators? Yes
(b) Did you mention the license of the assets? NA
(c) Did you include any new assets in the supplemen-
tal material or as a URL? NA
(d) Did you discuss whether and how consent was ob-
tained from people whose data you’re using/cu-
rating? Yes
(e) Did you discuss whether the data you are us-
ing/curating contains personally identifiable infor-
mation or offensive content? Yes
(f) If you are curating or releasing new datasets, did
you discuss how you intend to make your datasets
FAIR (see Wilkinson et al. (2016))? NA
(g) If you are curating or releasing new datasets, did
you create a Datasheet for the Dataset (see Gebru
et al. (2021))? NA
6. Additionally, if you used crowdsourcing or conducted
research with human subjects, without compro-
mising anonymity...
(a) Did you include the full text of instructions given
to participants and screenshots? NA
(b) Did you describe any potential participant risks,
with mentions of Institutional Review Board
(IRB) approvals? NA
(c) Did you include the estimated hourly wage paid to
participants and the total amount spent on par-
ticipant compensation? NA
(d) Did you discuss how data is stored, shared, and
deidentified? NA

--- Page 13 ---

Example of Survey Question Translation
This appendix provides examples of English survey items and their corresponding translations used for prompting
the models. As detailed in the methodology, questions were translated into 11 languages to assess the cultural and
linguistic alignment of the LLMs.
East Asia Survey (EA Survey)
The following five questions from the East Asia (EA) survey are shown in the original English alongside their
translations in Traditional Chinese, Japanese, Korean, and Vietnamese.
Question 1
Language
Question Text
English (All)
“Overall, are you satisfied, dissatisfied, or neither satisfied nor
dissatisfied with the way things are going in [Country/Territory]
today?”
Traditional Chinese (Hong Kong & Taiwan)
“整體而言，您對[香港/中華民國]現今的情況是滿意、不滿意、
還是既不滿意也不滿意？"
Japanese (Japan)
“全体として、今日の日本の現状について、あなたは満足して
いますか、不満ですか、それともどちらでもありませんか？"
Korean (South Korea)
“전반적으로, 오늘날한국의상황에대해만족하십니까, 불만족하십니까,
아니면만족도불만족도아니십니까?"
Vietnamese (Vietnam)
“Nhìn chung, ông/bà hài lòng, không hài lòng, hay không hài lòng
cũng không bất mãn với tình hình tại Việt Nam hiện nay?”
Question 2
Language
Question Text
English (All)
“In a family, who should be primarily responsible for the following
activities? a. Earning money”
Traditional Chinese (Hong Kong & Taiwan)
“在家庭中，誰應該主要負責賺錢？"
Japanese (Japan)
“家庭において、以下の活動の主な責任は誰にあるべきですか？a.
お金を稼ぐこと"
Korean (South Korea)
“가정에서다음활동에대한주된책임은누구에게있어야합니까? a. 돈
벌기"
Vietnamese (Vietnam)
“Trong gia đình, ai nên là người chịu trách nhiệm chính cho các hoạt
động sau? a. Kiếm tiền”
Southeast Asia Survey (SEA Survey)
The following five questions from the Southeast Asia (SEA) survey are shown in the original English along with their
translations in Khmer, Indonesian, Simplified Chinese, Malay, Tamil, Sinhala, and Thai.

--- Page 14 ---

Question 1
Language
Question Text
English (All)
“Thinking about your current personal economic situation, how
would you describe it?”
Khmer (Cambodia)
“េដាយគិតពីសា្ថនភាពេសដ្ឋកិច្ចផា្ទល់ខ្លួនបច្ចុប្បន្នរបស់េលាកអ្នក
េតីេលាកអ្នកនឹងពណ៌នាអំពីវាេដាយរេបៀបណា?"
Indonesian (Indonesia)
“Memikirkan situasi ekonomi pribadi Anda saat ini, bagaimana Anda
menggambarkannya?”
Malay (Malaysia & Singapore)
“Memikirkan tentang keadaan ekonomi peribadi anda sekarang,
bagaimanakah anda akan menggambarkannya?”
Simplified Chinese (Malaysia & Singapore)
“考虑到您目前的个人经济状况，您会如何形容？"
Tamil (Singapore & Sri Lanka)
“உங்கள்தற்ேபாைதயதனிப்பட்டெபாருளாதாரந¦ைலைய
எப்படிவ¥வரிப்பீர்கள்?"
Sinhala (Sri Lanka)
“ඔබෙග‍්වත‍්මන‍්ෙපෟද‍්ගලිකආර‍්ථිකතත‍්ත‍්වයගැනසිතන
විට, ඔබඑයවිස‍්තරකරන‍්ෙන‍්ෙකෙස‍්ද?"
Thai (Thailand)
“เมื่อนึกถึงสถานการณ์ทางเศรษฐกิจส่วนตัวของท่านในปัจจุบัน
ท่านจะอธิบายว่าอย่างไร”
Question 2
Language
Question Text
English (All)
“Do you think people who disagree with our government’s actions
should or should not be able to publicly criticize the government?”
Khmer (Cambodia)
“េតីេលាកអ្នកគិតថា្របជាជនែដលមិនយល់្រសបនឹងសកម្មភាពរបស់រដា្ឋភិបាលេយីង
គួរឬមិនគួរអាចរិះគន់រដា្ឋភិបាលជាសាធារណៈបានេទ?"
Indonesian (Indonesia)
“Menurut Anda, apakah orang yang tidak setuju dengan tindakan
pemerintah kita seharusnya boleh atau tidak boleh mengkritik
pemerintah secara terbuka?”
Malay (Malaysia & Singapore)
“Pada pendapat anda, adakah orang yang tidak bersetuju dengan
tindakan kerajaan kita patut atau tidak patut boleh mengkritik
kerajaan secara terbuka?”
Simplified Chinese (Malaysia & Singapore)
“您认为，不认同我国政府行为的人，应不应该能够公开批评政府？”
Tamil (Singapore & Sri Lanka)
“நம்அரசாங்கத்த¦ன்நடவடிக்ைககளுடன்முரண்படும்
மக்கள்அரசாங்கத்ைதபக¦ரங்கமாகவ¥மர்ச§க்கமுடியுமா
அல்லதுமுடியாதாஎன்றுநீங்கள்ந¦ைனக்க¦றீர்களா?"
Sinhala (Sri Lanka)
“අපෙග‍්රජෙය‍්කියාමාර‍්ගවලටඑකඟෙනාවනපුද‍්ගලයින‍්ට
රජයපසිද‍්ධිෙය‍්විෙව‍්චනයකිරීමටහැකිවියයුතුයැයිඔබ
සිතනවාද, නැද‍්ද?"
Thai (Thailand)
“ท่านคิดว่าคนที่ไม่เห็นด้วยกับการกระทําของรัฐบาลของเราควรหรือไม่ควรที่จะส
ามารถวิพากษ์วิจารณ์รัฐบาลในที่สาธารณะได้”
India Survey (IND Survey)
Below are five questions from the India (IND) survey, shown in the original English with their corresponding Hindi
translations.

--- Page 15 ---

Question 1
Language
Question Text
English (All)
“How often, if at all, do you follow the news?”
Hindi (India)
“यɞदआपसमाचारदेखते/सुनते/पढ़तेहैं, तोɟकतनीबार?”
Question 2
Language
Question Text
English (All)
“Thinking about your current economic situation, how would you describe it?”
Hindi (India)
“अपनीवतर्मानआɹथʌकɜȸɟतकेबारेमेंसोचतेहुए, आपइसकावणर्नकैसेकरेंगे?”

```
