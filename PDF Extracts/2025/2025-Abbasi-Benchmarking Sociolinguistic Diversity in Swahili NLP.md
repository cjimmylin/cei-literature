---
title: "2025-Abbasi-Benchmarking Sociolinguistic Diversity in Swahili NLP - PDF Extract"
source_pdf: "2025-Abbasi-Benchmarking Sociolinguistic Diversity in Swahili NLP.pdf"
pages: 16
extracted_at: "2026-02-13T09:15:42.604686"
---

# PDF Extract: 2025-Abbasi-Benchmarking Sociolinguistic Diversity in Swahili NLP

**Source PDF:** 2025-Abbasi-Benchmarking Sociolinguistic Diversity in Swahili NLP.pdf
**Total Pages:** 16

---

## Content

```
--- Page 1 ---

BENCHMARKING SOCIOLINGUISTIC DIVERSITY IN SWAHILI
NLP: A TAXONOMY-GUIDED APPROACH
Kezia Oketch, John P. Lalor, Ahmed Abbasi
Department of IT, Analytics, and Operations
University of Notre Dame
{koketch, john.lalor, aabbasi}@nd.edu
ABSTRACT
We introduce the first taxonomy-guided evaluation of Swahili NLP, addressing gaps in sociolinguistic
diversity. Drawing on health-related psychometric tasks, we collect a dataset of 2,170 free-text
responses from Kenyan speakers. The data exhibits tribal influences, urban vernacular, code-mixing,
and loanwords. We develop a structured taxonomy and use it as a lens for examining model prediction
errors across pre-trained and instruction-tuned language models. Our findings advance culturally
grounded evaluation frameworks and highlight the role of sociolinguistic variation in shaping model
performance.
1
Introduction
Natural language processing (NLP) has advanced key sectors such as healthcare (de Las Heras-Pedrosa et al. 2020),
education (Obiria et al. 2018), and public policy. These gains are largely confined to high-resource languages such
as English, Mandarin, and French; low-resource languages have been severely underrepresented in training data and
model development (Mohamed et al. 2023, Alabi et al. 2022, Akera et al. 2022). As a result, NLP systems often do not
reflect the linguistic and cultural realities of the communities they are deployed in (Magueresse et al. 2020), especially
in multilingual, culturally diverse regions.
Swahili, spoken by over 200 million people across East and Central Africa (Merritt and Abdulaziz 1985, Muna
and Okombo 2017), exemplifies this disparity. Despite its widespread use as a lingua franca connecting over 40
ethnolinguistic communities in Kenya alone (Petzell 2012, Murindanyi et al. 2023, Lodhi 1993, Amidu 1995), Swahili
remains marginalized in NLP research and benchmark datasets (Martin et al. 2021, Gelas et al. 2012, Obiria et al. 2018).
Existing datasets, such as MasakhaNER (Adelani et al. 2021), have made strides in curating resources for African
languages. However, these datasets are mostly designed for structured tasks using formal language corpora, leaving
gaps in their ability to capture the dynamic linguistic features present in real-world usage.
Swahili’s real-world usage is shaped by rich sociolinguistic variation, which poses challenges for NLP models trained
on standardized corpora. Speakers routinely switch between dialects, borrow from tribal lexicons, blend English with
Swahili in urban vernaculars like Sheng, and use loanwords from Arabic and other regional languages (Mazrui 1998).
These variations are not random; they reflect underlying social dimensions such as tribal identity, education, and
socio-economic status, all of which influence lexical choices and discourse styles. For NLP models, this variation
complicates semantic disambiguation, contextual inference, and syntactic parsing (van Boven et al. 2022, Perera
et al., Kumar et al. 2024). For instance, the word Panda in Swahili can mean “climb,” “plant,” or “board” depending
on context; the Sheng expression Dawa za kutesa (“serious medication”) is used to describe something “tough” or
“powerful.” We address these gaps by introducing a new Swahili NLP dataset designed to capture this full spectrum of
variation. Focused on health-related perceptions, it comprises 2,170 free-text responses from Kenyan speakers, each
paired with demographic metadata such as tribe, gender, income, and education, enabling sociolinguistic modeling and
fairness evaluation. The dataset includes examples of Sheng, dialectal Swahili, code-mixing, and loan words, as well as
instances of polysemy and informal usage.
Our contributions are as follows. First, we collect a dataset of health psychometrics in Swahili, the first to the best
of our knowledge, by following the procedure of Abbasi et al. (2021). Second, we benchmark target-language and
arXiv:2508.14051v1  [cs.CL]  6 Aug 2025

--- Page 2 ---

A PREPRINT
multi-lingual NLP models on the dataset to determine how they perform. Third, we conduct a detailed analysis of
the data and develop a taxonomy of Swahili sociolinguistic features. Fourth, we use regression analysis to model
prediction error as a function of taxonomy-guided features to analyze how sociolinguistic variation contributes to model
performance.1
2
Related Work
2.1
African Languages in NLP
The linguistic diversity of Africa presents distinct challenges for NLP. Over 2,000 languages are spoken on the continent,
many of which lack digitized resources and annotated corpora (Joshi et al. 2020). Swahili is the most widely spoken
African language and as such has received more attention in the NLP community; however, existing models still struggle
with its dialectal variation and tribal lexicon (Alabi et al. 2022, Adelani et al. 2021). While initiatives like AfriBERTa
and Masakhane have advanced representation for African languages (Nekoto et al. 2020, Adelani et al. 2021), they
remain limited in modeling sociolinguistic variation such as code-mixing, urban youth vernacular, and tribal influence.
In Swahili specifically, tribal affiliation has been shown to shape vocabulary and discourse patterns (Mazrui 1998). We
extend this work by curating a dataset that captures context-rich, non-standard variation and benchmarking NLP/LLM
model performance.
2.2
Sociolinguistic Variations
Linguistic variations such as code-mixing, dialectal shifts, and urban vernaculars are often treated as noise in mainstream
NLP workflows, where preprocessing favors standardized forms and disregards heterogeneity (Blodgett et al. 2020,
Joshi et al. 2020, Kantharuban et al. 2023). This approach marginalizes communities whose speech deviates from
dominant norms. However, a growing body of work challenges this premise. Studies on code-switching (Khanuja et al.
2020, Piergallini et al. 2016), dialectal NLP (Blodgett et al. 2016, Faisal et al. 2024), and low-resource benchmarks (Tan
and Celis 2019), argue for treating variation as a meaningful signal. (Ponti et al. 2019) note that variation is governed by
typological, cognitive, and social factors and should be explicitly modeled. Likewise, (Bafna et al. 2024) treat linguistic
perturbations not as noise but as systematic deviations along morphological, phonological, and lexical dimensions. We
build on this argument by creating a taxonomy of sociolinguistic features in Swahili and modeling their influence on
prediction error.
3
Dataset Construction
NLP has the potential to elucidate how language mediates healthcare access, comprehension, and trust, including
among linguistically marginalized populations (Aracena and Dunstan 2023). Accordingly, we develop a dataset of
healthcare related text data in Swahili. We adapt the framework of Abbasi et al. (2021) by translating and reproducing
their annotation task. Specifically, we adapted established English-language survey items originally measuring four
health-related attitudes: Anxiety Visiting a Doctor, Subjective Health Literacy, Health Numeracy, and Trust in Doctor
(Abbasi et al. 2021, Netemeyer et al. 2020).2 A certified translator produced Swahili versions, which were reviewed by
two experts for fluency and cultural fit. Discrepancies were resolved by consensus.
For data collection, we utilized GeoPoll, a leading crowdsourcing platform in Kenya. GeoPoll’s robust network of
participants in the region allowed us to access a diverse demographic pool, capturing variations in Swahili usage
influenced by tribe and urban-rural divides. GeoPoll’s mobile-first approach was crucial for engaging participants in
rural and urban areas, ensuring inclusivity in a region where internet access can be limited.
Participants completed open-ended textual prompts (Table 1) in addition to survey items corresponding to the four
dimensions (Abbasi et al. 2021). These included both self-reported behavior (e.g., frequency of doctor visits, smoking
and drinking habits) and standard demographic questions (gender, age, tribe, education, income, and race). To ensure
response quality, we applied standard reliability practices (e.g., incentives, validation, review, Abbasi et al. 2021,
Buechel et al. 2018, Buhrmester et al. 2011). Participants received monetary compensation upon completion, consistent
with local-fair wage guidelines. All study procedures were reviewed and approved by the University’s Institutional
Review Board, and informed consent was obtained from all participants.
To refine our survey design and validate the GeoPoll platform we conducted a pilot study of 125 participants. Following
the pilot, we conducted our full study. The final corpus comprises 2,170 free-text entries from native speakers across
1Our code and data is available at https://github.com/nd-hal/swahili_psych_taxonomy.
2Henceforth, we refer to these dimensions as Anxiety, Literacy, Numeracy, and Trust, respectively.
2

--- Page 3 ---

A PREPRINT
Task
English Prompt
Swahili Translation
Literacy
Regarding all the questions you just answered, to what
degree do you feel you have the capacity to obtain,
process, and understand basic health information and
services needed to make appropriate health decisions?
Please explain your answer in a few sentences.
Kuhusiana na maswali uliyojibu hapo juu, kwa ki-
wango gani unahisi una uwezo wa kupata, kuchakata,
na kuelewa taarifa za msingi za afya na huduma zina-
zohitajika kufanya maamuzi sahihi ya afya? Tafad-
hali eleza jibu lako kwa sentensi chache.
Trust
In a few sentences, please explain the reasons why you
trust or distrust your primary care physician. If you do
not have a primary care physician, please answer in
regard to doctors in general.
Katika sentensi chache, tafadhali eleza sababu kwa
nini unamwamini au humwamini daktari wako wa
matibabu ya kawaida. Ikiwa huna daktari wa mat-
ibabu ya kawaida, tafadhali jibu kuhusu madaktari
kwa ujumla.
Anxiety
In a few sentences, please describe what makes you
most anxious or worried when visiting the doctor’s
office.
Katika sentensi chache, tafadhali eleza kinachoku-
fanya uhisi wasiwasi au hofu zaidi unapotembelea
ofisi ya daktari.
Numeracy
In a few sentences, please describe an experience in
your life that demonstrated your knowledge of health
or medical issues.
Kwa sentensi chache, tafadhali eleza tukio ambalo
lilionyesha ujuzi wako wa masuala ya afya au mati-
babu.
Table 1: English prompts and their corresponding Swahili translations for the four psychometric survey tasks
(a) Distribution of tribes by language group.
(b) Distribution of psychometric task response scores.
Figure 1: Summary statistics of our collected dataset.
Kenya.3 Since race is homogeneous (>95% Black) in our testbed, tribe serves as a more salient demographic dimension,
correlating with lexical choices. Figure 1a depicts the distribution of tribes in our dataset grouped by their ethnolinguistic
category. To quantify each construct, we aggregated item-level responses into a unified score scaled on a 0-1 range
across tasks. Figure 1b visualizes the distribution of user patterns across the four dimensions. We can see that numeracy
and anxiety responses exhibit characteristics closer to normality, while trust and literacy deviate significantly due to
skewness. Table 2 presents sample anxiety-related responses in Swahili, accompanied by their English translations and
associated scores. The text was translated directly to English by a member of the research team to maintain the original
respondent’s intention.
4
Benchmarking Swahili NLP Models
4.1
Experimental Setup
To evaluate our Swahili dataset, we conducted regression and classification tasks to see how well various multilingual
NLP models could predict survey-based “ground-truth” scores using the user-generated text responses (Abbasi et al.
2021). In the regression setting, the target variable consisted of continuous scores normalized on a 0-1 range. For
classification, we discretized across the median values, resulting in high versus low class labels (Gibson et al. 2015,
Abbasi et al. 2021).
3Full summary statistics are provided in Appendix A.1.
3

--- Page 4 ---

A PREPRINT
Anxiety
Score
Swahili Text Response
English Translation
0.9524
Pesa kwa matibabu hunifanya niwe na wasiwasi.
Ripoti ya daktari hunipa wasiwasi mwingi maanake
sijui atasema naugua ugonjwa upi.
Money for treatment makes me anxious. A doctor’s
report gives me a lot of worry because I don’t know
which illness they will say I have.
0.3095
Wasiwasi hutokea wakati usipojua shida au tatizo
la afya nililonalo au kutojua gharama ya matibabu
pamoja na dawa kwa ujumla baada ya vipimo.
Anxiety arises when you don’t know the health prob-
lem or condition I have or not knowing the overall
cost of treatment and medication after tests.
Table 2: Sample participant responses to the Anxiety task, presented with corresponding Swahili text, English translation,
and normalized psychometric scores.
We ran our experiments with nine NLP models: linear/logistic regression, mBERT (Devlin et al. 2019), XLM-RoBERTa
(Conneau et al. 2020), AfriBERTa (Ogueji et al. 2021), SwahBERT (Martin et al. 2022), Qwen2.5-72B-Instruct
and Qwen2.5-7B-Instruct (Yang et al. 2024), and Llama-3.1-405B-Instruct and Llama-3.1-8B-Instruct (Grattafiori
et al. 2024). The linear and logistic baselines were trained using TF-IDF features with 1-3-gram windows, and
capped at 30,000 and 10,000 features, respectively. For PLMs, we fine-tuned each model for each task with five-fold
cross validation using weighted cross-entropy loss for classification and mean squared error loss for regression. For
instruction-tuned LLMs, we used few-shot prompting with three in-context examples sampled from the training fold.
Prompts were structured to elicit either a numeric score between 0 and 1 for regression tasks, or a binary “Yes” or “No”
for classification tasks. Additional experimental details, including hyperparameters and prompting templates, are in
Appendix C.
4.2
Evaluation Metrics
For regression tasks, we computed mean squared error (MSE) to quantify average prediction error and Pearson’s r to
capture the linear correlation between predicted and actual scores. For classification, we used the F1 score to balance
precision and recall, and area under the ROC curve (AUC) to measure the model’s ability to distinguish between classes
across different thresholds.
To evaluate tribal fairness, we selected a mix of multilingual (mBERT, XLM-RoBERTa), regional (AfriBERTa), and
Swahili-specific (SwahBERT) models commonly used in African NLP tasks.4 We binarized the tribe variable such that
the top two tribes (Kikuyu and Kamba) were the privileged class; all others were the protected class.
We quantify fairness via three measures: xAUC, Disparate Impact (DI), and Fairness Violation (FV). xAUC (Kallus
and Zhou 2019) measures disparities in the ranked ordering of predicted scores across groups: ∆xAUC = p(Rb
1 ≤
Ra
0) −p(Ra
1 ≤Rb
0). A positive ∆xAUC indicates that individuals from group a in the privileged class T = 1 are
ranked higher by the model than those from group b in the protected class T = 0. DI quantifies the relative rate at which
two groups, privileged and non-privileged, receive predicted positive outcomes, serving as a proxy for group-level
equity (Lalor et al. 2022, Friedler et al. 2019, Barocas and Selbst 2016) DI = p(ˆy=1|T =0)
p(ˆy=1|T =1). A DI value below 1 indicates
that the protected group receives positive predictions at a lower rate than the privileged group, signaling potential
group-level disparity. FV measures the largest absolute difference between the TPR of any intersectional subgroup and
the global TPR, and quantifies the maximum discrepancy between the behavior of any subgroup and that of the overall
population (Yang et al. 2020).
We also evaluated intersectional fairness across combinations of demographic attributes. Here, we binarized tribe
into two ethnolinguistic groups, Bantu and Non-Bantu, to reflect established East African linguistic family structures
and capture meaningful sociolinguistic variation (Mazrui et al. 1998, Heine and Nurse 2000). We computed DI and
FV for all possible combinations of demographic attributes across increasing levels of complexity (e.g., two-way,
three-way, and higher-order intersections). In the two-dimensional case, for example, protected groups include older
women, women with lower income, and non-Bantu women; corresponding privileged groups are their complements,
e.g., younger men, higher-income men, and Bantu men (Lalor et al. 2022). As in prior work, we set gender as the
base demographic (Bolukbasi et al. 2016, Lalor et al. 2022). We excluded 102 responses that contained ambiguous
demographics (e.g., cases where income was marked as “not sure” or tribe listed as “I choose not to answer”).
4While prior research have evaluated NLP models with regards to race (Guo et al. 2022), in our dataset, race is homogeneous
(>95% Black) and hence not a salient demographic variable for such analysis.
4

--- Page 5 ---

A PREPRINT
4.3
Results
4.3.1
Performance on Healthcare NLP Tasks
Model
Continuous Classification
Binary Classification
Literacy
Trust
Anxiety
Numeracy
Literacy
Trust
Anxiety
Numeracy
r
RMSE
r
RMSE
r
RMSE
r
RMSE AUC F 1 AUC F 1 AUC F 1 AUC F 1
Regression
.098
.388
.288
.157
.123
.261
.022
.297
.603 .589 .711 .784 .558 .570 .563 .686
AfriBERTa
.202
.174
.436
.133
.156
.234
.129
.242
.604 .655 .650 .635 .585 .647 .570 .648
SwahBERT
.181
.180
.392
.136
.089
.249
.103
.234
.578 .657 .636 .652 .567 .648 .536 .640
XLM-RoBERTa .145
.172
.398
.133
.103
.229
.129
.207
.572 .659 .647 .669 .557 .652 .525 .636
mBERT
.180
.174
.427
.133
.138
.228
.133
.220
.559 .659 .649 .652 .543 .652 .585 .644
Qwen2.5-7B
.121
.215
.337
.250
.084
.266
.031
.294
.538 .565 .566 .496 .483 .386 .527 .572
Qwen2.5-72B
.169
.209
.471
.225
.134
.247
.023
.257
.546 .629 .639 .735 .503 .626 .522 .532
Llama3.1-8B
.125
.118
.163
.187
.039
.255
.019
.212
.533 .526 .563 .665 .503 .607 .523 .591
Llama3.1-405B
.255
.165
.541
.215
.204
.288
.039
.284
.539 .675 .608 .712 .517 .670 .502 .653
Table 3: Performance of all evaluated models on regression and binary classification tasks across the four psychometric
dimensions. The best-performing scores per column are highlighted in bold.
Table 3 summarizes performance on both regression and classification tasks. Our findings reveal two key insights. First,
there is no clear consensus model (or category of models) that outperforms others. On certain tasks, such as Trust,
domain-adapted PLMs consistently outperformed general-purpose LLMs (e.g., in terms of AUC, RMSE). For instance,
AfriBERTa, XLM-RoBERTa, and mBERT all achieved the lowest RMSE on Trust (.133). AfriBERTa had the highest
AUC on Literacy (.604) and Anxiety (.585), while mBERT led on Numeracy (.585), underscoring the advantage of
multilingual models trained on regionally relevant data. Conversely, the two Llama LLMs had the best F1 scores for
Anxiety and Literacy, and the highest correlation scores on Literacy (r = .255), Trust (r = .541), and Anxiety (r = .204).
Second, when comparing the results against those attained by Abbasi et al. (2021) on the English testbed, all PLM
and LLM models in this study yielded AUCs for binary classification that were at least 20%-30% lower than those
attained by their English-language BERT model (Literacy= .798, Trust= .845, Anxiety= .723, Numeracy= .776).
This point is further underscored by the fact that in their study, the Regression models performed as weak baselines
whereas in our results they were at or near the top for all four binary classification tasks. Although the two testbeds are
obviously different (English versus Swahili), given the commonalities in the construction process, the results suggest
that the state-of-the-art in regards to text classification predictive power for Swahili may be markedly behind that in
high-resource languages such as English.
4.3.2
LLMs and Domain-specific PLMs Encode Tribal Biases
We first evaluated model fairness using the aforementioned xAUC metric, which is particularly appropriate for allocation-
sensitive contexts such as triaging patients under limited healthcare resources, where ranking quality matters more than
binary decisions (Kallus and Zhou 2019). For this analysis, in order to capture a mix of domain-specific PLMs and
LLMs of different sizes, we included SwahBERT, Llama-3.1-405B, and Qwen2.5-72B.
Figure 2 plots model performance (AUC) against ∆xAUC, comparing Kamba vs All (left) and Kikuyu vs All (right).
The results reveal some strong tribal disparities. For instance, on the Kamba panel (left), the highest Trust AUC
model, SwahBERT, exhibits the highest ∆xAUC value (≈0.3). This is a strong signal of ranking bias, indicating that
the difference between Kamba individuals labeled as “trusting” over non-Kamba labeled as "distrusting," relative to
non-Kamba "distrusting" over Kamba "trusting", is 30%. Crucially, SwahBERT was also the only domain-specific
PLM included in the analysis, and yet garnered markedley higher bias on the Trust classification task than its Llama
and Qwen counterparts. In this case, SwahBERT may be overfitting to lexical or syntactic features resulting in potential
overgeneralizations about trust-related language used by Kamba speakers. We observe a similar trend on Literacy. This
finding highlights that domain-adapted models can still entrench subgroup privilege when they mirror the linguistic
norms of dominant communities.
In the Kikuyu panel, we do not observe large ∆xAUC deviations from 0 for the highest AUC models. However, the
lower-performing models tend to exhibit large deltas on tasks such as Literacy indicating possible tribal disparities. For
instance, SwahBERT on Literacy reaches a ∆xAUC of -0.24. While not all models exhibit this behavior, Qwen2.5-72B,
for example, achieves a positive ∆xAUC on Literacy (≈+0.14). The fairness results using xAUC suggest that both
5

--- Page 6 ---

A PREPRINT
domain-specific PLMs and LLM models are encoding sociolinguistic patterns that systematically favor or disfavor
certain tribal subgroups. In the ensuing subsection, we examine disparate impact across multiple demographics.
Figure 2: Relationship between model performance (AUC) and fairness ∆xAUC for two tribal groups: (left) Kamba
versus all others, and (right) Kikuyu versus all others.
4.3.3
Intersections Exacerbate Biases
Figure 3 shows results for disparate impact, moving from single-group fairness to intersectional subgroup analysis. The
figure reveals that disparities intensify, and the apparent fairness of several models quickly erodes as the set of groups
increases. On the Anxiety task, mBERT’s disparate impact (DI) drops from ≈0.83 at the group level to below 0.72 at
five-way intersections, signaling that individuals belonging to multiple marginalized categories (e.g., old, non-Kamba,
low-education, female, low-income) are systematically de-prioritized. XLM-RoBERTa and SwahBERT follow similar
declines.
In Literacy, XLM-RoBERTa’s DI plummets below 0.80, revealing stark underprediction for complex identity configura-
tions. These show that the more a person diverges from dominant demographic norms, the worse the model treats them.
Numeracy appears more balanced (DI≈1) for most model-intersection combinations. On the Trust task, the impact
of the range of intersectional bias is most pronounced as evidenced by the growing intervals observed across all four
PLMs. This trend is also observed on the Literacy task. Moreover, there, XLM-RoBERTa exhibits DI consistently<1
and below 0.8 when examining low-income, low-education, older females from select tribes. The results highlight key
intersectional biases at the confluence of tribal affiliations and gender, age, education, and income.
Figure 3: Impact of increasing demographic intersectionality on disparate impact (DI) across the four psychometric
tasks. DI values are computed across 1-way to 5-way demographic intersections.
6

--- Page 7 ---

A PREPRINT
5
Taxonomy of Linguistic Variation
Having collected and evaluated our dataset with a benchmark suite of models, we next conduct a thorough analysis
of the dataset to develop a taxonomy of linguistic variations in Swahili and conduct an error analysis based on the
taxonomy.
5.1
Taxonomy Construction
As demonstrated by our benchmarking, PLMs and LLMs often struggle in culturally and linguistically rich contexts like
Swahili, in particular when these models are deployed in region-specific applications (Grieve et al. 2024, Amol et al.
2024). These failures stem not only from data scarcity but also from the inability of PLMs to model sociolinguistic
variations such as code-mixing, Sheng, tribal lexical influence, and loanwords. These language patterns – prevalent in
everyday Swahili communication – represent identity, region, and social contexts.
To capture these linguistic patterns, we constructed a taxonomy through a bottom-up analysis of our data. We inspected
all 2,170 responses from our survey across all four psychometric tasks. Each response was annotated by a member of
the research team fluent in Swahili for the presence of sociolinguistic features such as borrowed words, code-switched
segments, and dialect-specific expressions. We grouped the most frequently observed patterns that commonly lead to
errors in language modeling into four core categories: code-mixing, sheng, tribal lexicon, and loanwords.5
The final taxonomy (Figure 4) reveals specific representational gaps in current PLMs that have not been widely
documented in prior literature. Through our error analysis of model predictions, we observed that the responses
containing sheng or tribal lexical terms were disproportionately affected. Some were consistently underpredicted,
while others were overpredicted, depending on model and task. These inconsistencies suggest that PLMs lack robust
representations for culturally embedded linguistic forms. By organizing these phenomena into a structured taxonomy,
we offer a framework for identifying such weaknesses and improving model performance in linguistically diverse,
underrepresented settings.
Figure 4: Proposed taxonomy of sociolinguistic variation in Swahili, capturing linguistic categories observed in the
dataset: Loan Words (Kang 2011), Sheng (Githiora 2002), Tribal Lexicons (Amol et al. 2024), Code-Mixing (Piergallini
et al. 2016)
5These four categories form the core of our analysis; they are not exhaustive. We also found other variations such as discourse
markers, reduplication, and verbal morphology, that we do not model here (see Table 8). Here, we focus on the four categories most
associated with model prediction errors.
7

--- Page 8 ---

A PREPRINT
5.2
Linguistic Features Like Sheng and Tribal Terms Drive Mispredictions
Building on this taxonomy, we conducted a systematic error analysis to quantify how these linguistic features contribute
to prediction errors made by the PLMs. Specifically, we shift focus from aggregate performance metrics to model
behavior by analyzing prediction errors at the response level (Lalor et al. 2024). Here we define error as the difference
between the human-assigned and model-generated score (∆i = Humani −Modeli) and examine its variation by
sociolinguistic feature. This enables empirical error analysis beyond anecdotal cases. As stated in 5.1, we annotated
four sociolinguistic feature categories; code-mixing, sheng, tribal lexicon, and loanwords.
We used the features to fit two ordinary least squares (OLS) regression models for each PLM-task pair. In the first model
we consider main effects only: ∆i = β0 + P4
j=1 βjXij + εi, where Xij is a binary indicator for whether linguistic
feature j is present in response i. This model estimates the average marginal effect of each feature on the model error.
The second model includes all pairwise interactions among the four feature categories:
∆i = β0 +
4
X
j=1
βjXij +
X
k>j
βjk(Xij × Xik) + εi
(3)
where Xij ×Xik represents the co-occurrence of features j and k in the same response. This captures interaction effects
where feature combinations may influence model error. In both models, positive coefficients indicate underprediction
by the model when a feature is present; negative values indicate overprediction.
The resulting coefficients ˆβj are visualized in Figure 5. Our findings show that model errors are not random but
systematic. For instance, sheng usage is consistently associated with errors; whether it is over-prediction or under-
prediction is task-dependent. The interactions between sheng usage, tribal lexicon, and loanwords are particularly
strong indicators of under-prediction, especially in Numeracy and Anxiety (see area under red box). These results
reflect broader trends in the literature: PLMs tend to struggle with code-mixed and dialectically marked language
(Khanuja et al. 2020, Blodgett et al. 2016), and such linguistic complexity often corresponds with higher error variance
(Tan and Celis 2019).
Figure 5: Ordinary least squares regression coefficients ˆ∆for main effects (left) and interaction effects (right) of
sociolinguistic features on model prediction error across tasks.
8

--- Page 9 ---

A PREPRINT
Model
Feature
Anxiety
Literacy
Numeracy
Trust
AfriBERTa
Sheng
-0.130 (0.422)
-0.269 (0.360)
0.017 (0.024)
0.397 (0.383)
Tribal
0.075*** (0.022)
0.009 (0.019)
0.001 (0.001)
0.061** (0.020)
Loan
0.339*** (0.018)
0.113*** (0.016)
-0.007*** (0.001)
0.288*** (0.016)
CodeMixed
0.124** (0.040)
0.166*** (0.034)
-0.004 (0.002)
0.010 (0.037)
mBERT
Sheng
-1.414** (0.433)
-0.068 (0.432)
-0.032 (0.526)
0.162 (0.478)
Tribal
-0.262*** (0.022)
-0.145*** (0.023)
-0.164*** (0.028)
-0.497*** (0.023)
Loan
0.261*** (0.019)
0.085*** (0.020)
0.218*** (0.024)
0.300*** (0.021)
CodeMixed
0.123** (0.042)
0.207*** (0.041)
0.148** (0.050)
0.112* (0.046)
SwahBERT
Sheng
-1.372** (0.418)
0.003 (0.425)
0.065 (0.495)
-0.102 (0.465)
Tribal
-0.234*** (0.022)
-0.135*** (0.022)
-0.153*** (0.026)
-0.470*** (0.023)
Loan
0.060** (0.019)
0.014 (0.020)
0.105*** (0.023)
0.104*** (0.021)
CodeMixed
0.140*** (0.040)
0.174*** (0.041)
0.145** (0.047)
0.108* (0.044)
XLM-RoBERTa
Sheng
0.096 (0.540)
-0.352 (0.488)
-0.461 (0.636)
0.448 (0.509)
Tribal
0.141*** (0.029)
0.040 (0.026)
0.066 (0.034)
0.168*** (0.027)
Loan
0.458*** (0.023)
0.151*** (0.022)
0.338*** (0.028)
0.375*** (0.022)
CodeMixed
0.160** (0.052)
0.238*** (0.046)
0.180** (0.061)
0.016 (0.049)
Table 4: Main effect regression coefficients of sociolinguistic features on model prediction error, with standard errors
shown in parentheses. Asterisks denote levels of statistical significance (* p < 0.05, ** p < 0.01, *** p < 0.001).
Importantly, these patterns have fairness implications. When models systematically mispredict responses that reflect
certain linguistic identities, they contribute to epistemic injustice (Helm et al. 2024). By modeling ∆scores and
surfacing linguistic conditions under which models deviate from human judgment, our analysis provides an interpretable
framework for diagnosing model failure in low-resource languages.
6
Conclusion
This paper introduces a culturally grounded benchmark for evaluating fairness and performance for Swahili NLP.
Based on the framework of Abbasi et al. (2021), we curated a novel dataset enriched with sociolinguistic variation
and demographic metadata, and we developed a structural taxonomy to guide error analysis. Our experiments reveal
that linguistic features such as sheng, loanwords, and tribal lexicons systematically contribute to prediction errors.
Furthermore, intersectional fairness metrics demonstrate that disparities compound across demographic dimensions
such as tribe, gender, and education.
Together, these findings underscore that fairness in NLP cannot be decoupled from sociolinguistic context. Our work
offers not only a diagnostic tool for evaluating models in low-resource settings, but also a call to center linguistic
diversity in the design of equitable language technologies. In the context of African NLP, intersectional bias remains
underexplored. While multilingual models like mBERT (Devlin et al. 2019) and XML-RoBERTa (Conneau et al.
2020) claim to generalize across languages, these models fail to capture intersectional patterns in African languages,
particularly when tasked with representing tribal or gendered subgroups (Joshi et al. 2020, Nekoto et al. 2020),
highlighting the need for culturally grounded datasets.
Limitations
While this study makes significant strides in advancing NLP research for low-resource languages, particularly Swahili,
it is important to acknowledge the limitations that constrain its broader applicability. First, the dataset, although rich in
linguistic diversity, is primarily focused on Kenyan Swahili speakers. This focus may limit the generalizability of the
findings to other regions where Swahili usage exhibits notable variations, such as Tanzania, Uganda, and the Democratic
Republic of Congo. Another challenge lies in the dataset’s representation of language phenomena. Despite the inclusion
of sheng, dialectal variations, and code-mixing, certain linguistic features, such as rare idiomatic expressions and
phonetic variations, are not comprehensively captured. Moreover, the study underexplores code-switching involving
Swahili and other regional languages, such as Kikuyu or Luo, which are common in everyday communication. These
limitations highlight the inherent challenges in developing NLP systems for low-resource languages like Swahili. They
underscore the need for future research to expand datasets, refine fairness evaluation methods, and develop models
optimized for deployment in resource-constrained environments. Additionally, although the cross-validation splits were
9

--- Page 10 ---

A PREPRINT
stratified by task label, they were not demographically balanced by protected attributes (e.g., gender, tribe), which may
have introduced representational bias during training. We highlight this as an important direction for future work.
References
Ahmed Abbasi, David Dobolyi, John P. Lalor, Richard G. Netemeyer, Kendall Smith, and Yi Yang. 2021. Constructing a psychometric
testbed for fair natural language processing. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing, pages 3748–3758, Online and Punta Cana, Dominican Republic. Association for Computational Linguistics.
David Ifeoluwa Adelani, Jade Abbott, Graham Neubig, Daniel D’souza, Julia Kreutzer, Constantine Lignos, Chester Palen-Michel,
Happy Buzaaba, Shruti Rijhwani, Sebastian Ruder, et al. 2021. Masakhaner: Named entity recognition for african languages.
Transactions of the Association for Computational Linguistics, 9:1116–1131.
Benjamin Akera, Jonathan Mukiibi, Lydia Sanyu Naggayi, Claire Babirye, Isaac Owomugisha, Solomon Nsumba, Joyce Nakatumba-
Nabende, Engineer Bainomugisha, Ernest Mwebaze, and John Quinn. 2022. Machine translation for african languages:
Community creation of datasets and models in uganda.
Jesujoba O. Alabi, David Ifeoluwa Adelani, Marius Mosbach, and Dietrich Klakow. 2022. Adapting pre-trained language models to
African languages via multilingual adaptive fine-tuning. In Proceedings of the 29th International Conference on Computational
Linguistics, pages 4336–4349, Gyeongju, Republic of Korea. International Committee on Computational Linguistics.
Assibi Apatewon Amidu. 1995. Kiswahili: People, language, literature and lingua franca. Nordic Journal of African Studies,
4(1):20–20.
Cynthia Jayne Amol, Everlyn Asiko Chimoto, Rose Delilah Gesicho, Antony M Gitau, Naome A Etori, Caringtone Kinyanjui,
Steven Ndung’u, Lawrence Moruye, Samson Otieno Ooko, Kavengi Kitonga, et al. 2024. State of nlp in kenya: A survey.
arXiv preprint arXiv:2410.09948.
Claudio Aracena and Jocelyn Dunstan. 2023. Development of pre-trained language models for clinical nlp in spanish. In Proceedings
of the 17th Conference of the European Chapter of the Association for Computational Linguistics: Student Research Workshop,
pages 52–60.
Niyati Bafna, Kenton Murray, and David Yarowsky. 2024. Evaluating large language models along dimensions of language variation:
A systematik invesdigatiom uv cross-lingual generalization. In Proceedings of the 2024 Conference on Empirical Methods in
Natural Language Processing, pages 18742–18762, Miami, Florida, USA. Association for Computational Linguistics.
Solon Barocas and Andrew D Selbst. 2016. Big data’s disparate impact. Calif. L. Rev., 104:671.
Su Lin Blodgett, Solon Barocas, Hal Daumé III, and Hanna Wallach. 2020. Language (technology) is power: A critical survey of
“bias” in NLP. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 5454–5476,
Online. Association for Computational Linguistics.
Su Lin Blodgett, Lisa Green, and Brendan O’Connor. 2016. Demographic dialectal variation in social media: A case study of
African-American English. In Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing,
pages 1119–1130, Austin, Texas. Association for Computational Linguistics.
Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T Kalai. 2016. Man is to computer programmer as
woman is to homemaker? debiasing word embeddings. Advances in neural information processing systems, 29.
Sven Buechel, Anneke Buffone, Barry Slaff, Lyle Ungar, and João Sedoc. 2018. Modeling empathy and distress in reaction to news
stories. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing, pages 4758–4765,
Brussels, Belgium. Association for Computational Linguistics.
Michael Buhrmester, Tracy Kwang, and Samuel D Gosling. 2011. Amazon’s mechanical turk: A new source of inexpensive, yet
high-quality, data? Perspectives on psychological science, 6(1):3–5.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave,
Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov. 2020. Unsupervised cross-lingual representation learning at scale.
In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 8440–8451, Online.
Association for Computational Linguistics.
Carlos de Las Heras-Pedrosa, Pablo Sánchez-Núñez, and José Ignacio Peláez. 2020. Sentiment analysis and emotion understanding
during the covid-19 pandemic in spain and its impact on digital ecosystems. International journal of environmental research
and public health, 17(15):5542.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of deep bidirectional transformers
for language understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers), pages 4171–4186,
Minneapolis, Minnesota. Association for Computational Linguistics.
Fahim Faisal, Orevaoghene Ahia, Aarohi Srivastava, Kabir Ahuja, David Chiang, Yulia Tsvetkov, and Antonios Anastasopoulos.
2024. Dialectbench: A nlp benchmark for dialects, varieties, and closely-related languages. arXiv preprint arXiv:2403.11009.
Sorelle A Friedler, Carlos Scheidegger, Suresh Venkatasubramanian, Sonam Choudhary, Evan P Hamilton, and Derek Roth. 2019. A
comparative study of fairness-enhancing interventions in machine learning. In Proceedings of the conference on fairness,
accountability, and transparency, pages 329–338.
10

--- Page 11 ---

A PREPRINT
Hadrien Gelas, Laurent Besacier, and François Pellegrino. 2012. Developments of swahili resources for an automatic speech
recognition system. In SLTU, pages 94–101.
James Gibson, Nikolaos Malandrakis, Francisco Romero, David C Atkins, and Shrikanth S Narayanan. 2015. Predicting therapist
empathy in motivational interviews using language features inspired by psycholinguistic norms. In Interspeech, pages
1947–1951.
Chege Githiora. 2002. Sheng: peer language, swahili dialect or emerging creole? Journal of African cultural studies, 15(2):159–181.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman, Akhil
Mathur, Alan Schelten, Alex Vaughan, et al. 2024. The llama 3 herd of models. arXiv preprint arXiv:2407.21783.
Jack Grieve, Sara Bartl, Matteo Fuoli, Jason Grafmiller, Weihang Huang, Alejandro Jawerbaum, Akira Murakami, Marcus
Perlman, Dana Roemling, and Bodo Winter. 2024. The sociolinguistic foundations of language modeling. arXiv preprint
arXiv:2407.09241.
Yue Guo, Yi Yang, and Ahmed Abbasi. 2022. Auto-debias: Debiasing masked language models with automated biased prompts. In
Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages
1012–1023.
Bernd Heine and Derek Nurse. 2000. African languages: An introduction. Cambridge University Press.
Paula Helm, Gábor Bella, Gertraud Koch, and Fausto Giunchiglia. 2024. Diversity and language technology: how language modeling
bias causes epistemic injustice. Ethics and Information Technology, 26(1):8.
Pratik Joshi, Sebastin Santy, Amar Budhiraja, Kalika Bali, and Monojit Choudhury. 2020. The state and fate of linguistic diversity
and inclusion in the NLP world. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,
pages 6282–6293, Online. Association for Computational Linguistics.
Nathan Kallus and Angela Zhou. 2019. The fairness of risk scores beyond classification: Bipartite ranking and the xauc metric.
Advances in neural information processing systems, 32.
Yoonjung Kang. 2011. Loanword phonology. The Blackwell companion to phonology, 4:1003–1026.
Anjali Kantharuban, Ivan Vuli´c, and Anna Korhonen. 2023. Quantifying the dialect gap and its correlates across languages. In
Findings of the Association for Computational Linguistics: EMNLP 2023, pages 7226–7245, Singapore. Association for
Computational Linguistics.
Simran Khanuja, Sandipan Dandapat, Anirudh Srinivasan, Sunayana Sitaram, and Monojit Choudhury. 2020. GLUECoS: An
evaluation benchmark for code-switched NLP. In Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, pages 3575–3585, Online. Association for Computational Linguistics.
Ritesh Kumar, Shyam Ratan, Siddharth Singh, Enakshi Nandi, Laishram Niranjana Devi, Akash Bhagat, Yogesh Dawer, Bornini
Lahiri, and Akanksha Bansal. 2024. A multilingual, multimodal dataset of aggression and bias: the comma dataset. Language
Resources and Evaluation, 58(2):757–837.
John Lalor, Yi Yang, Kendall Smith, Nicole Forsgren, and Ahmed Abbasi. 2022. Benchmarking intersectional biases in NLP. In
Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, pages 3598–3609, Seattle, United States. Association for Computational Linguistics.
John P Lalor, Ahmed Abbasi, Kezia Oketch, Yi Yang, and Nicole Forsgren. 2024. Should fairness be a metric or a model?
a model-based framework for assessing bias in machine learning pipelines. ACM Transactions on Information Systems,
42(4):1–41.
Abdulaziz Y Lodhi. 1993. The language situation in africa today. Nordic Journal of African Studies, 2(1):11–11.
Alexandre Magueresse, Vincent Carles, and Evan Heetderks. 2020. Low-resource languages: A review of past work and future
challenges. ArXiv, abs/2006.07264.
Gati Martin, Medard Edmund Mswahili, Young-Seob Jeong, and Jiyoung Woo. 2022. SwahBERT: Language model of Swahili. In
Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, pages 303–313, Seattle, United States. Association for Computational Linguistics.
Gati L Martin, Medard E Mswahili, and Young-Seob Jeong. 2021. Sentiment classification in swahili language using multilingual
bert. arXiv preprint arXiv:2104.09006.
Ali A Mazrui. 1998. Neo-dependency and africa’s fragmentation.
Ali Al’Amin Mazrui, Alamin M Mazrui, and Alamin Mazrui. 1998. The Power of Babel: language and governance in the African
experience. University of Chicago Press.
Marilyn Merritt and Mohamed H Abdulaziz. 1985. Swahili as a national language in east africa.
Naira Abdou Mohamed, Imade Benelallam, Abdessalam Bahafid, and Zakarya Erraji. 2023. Bantulm: Enhancing cross-lingual
learning in the bantu language family.
Edwin Muna and Patrick Lugwiri Okombo. 2017. The international status of kiswahili: The parameters of braj kachru’s model of
world englishes.
Sudi Murindanyi, Brian Afedra Yiiki, Andrew Katumba, and Joyce Nakatumba-Nabende. 2023. Explainable machine learning
models for swahili news classification. In Proceedings of the 2023 7th International Conference on Natural Language
Processing and Information Retrieval, pages 12–18.
11

--- Page 12 ---

A PREPRINT
Wilhelmina Nekoto, Vukosi Marivate, Tshinondiwa Matsila, Timi Fasubaa, Taiwo Fagbohungbe, Solomon Oluwole Akinola,
Shamsuddeen Muhammad, Salomon Kabongo Kabenamualu, Salomey Osei, Freshia Sackey, Rubungo Andre Niyongabo,
Ricky Macharm, Perez Ogayo, Orevaoghene Ahia, Musie Meressa Berhe, Mofetoluwa Adeyemi, Masabata Mokgesi-Selinga,
Lawrence Okegbemi, Laura Martinus, Kolawole Tajudeen, Kevin Degila, Kelechi Ogueji, Kathleen Siminyu, Julia Kreutzer,
Jason Webster, Jamiil Toure Ali, Jade Abbott, Iroro Orife, Ignatius Ezeani, Idris Abdulkadir Dangana, Herman Kamper, Hady
Elsahar, Goodness Duru, Ghollah Kioko, Murhabazi Espoir, Elan van Biljon, Daniel Whitenack, Christopher Onyefuluchi,
Chris Chinenye Emezue, Bonaventure F. P. Dossou, Blessing Sibanda, Blessing Bassey, Ayodele Olabiyi, Arshath Ramkilowan,
Alp Öktem, Adewale Akinfaderin, and Abdallah Bashir. 2020. Participatory research for low-resourced machine translation:
A case study in African languages. In Findings of the Association for Computational Linguistics: EMNLP 2020, pages
2144–2160, Online. Association for Computational Linguistics.
Richard G Netemeyer, David G Dobolyi, Ahmed Abbasi, Gari Clifford, and Herman Taylor. 2020. Health literacy, health numeracy,
and trust in doctor: effects on key patient health outcomes. Journal of Consumer Affairs, 54(1):3–42.
Peter B. Obiria, Phyllis Ngigi, and Grace Machuke. 2018. Swahili text classification using support vector machine and feature
selection to enhance opinion analysis in kenyan universities.
Kelechi Ogueji, Yuxin Zhu, and Jimmy Lin. 2021. Small data? no problem! exploring the viability of pretrained multilingual
language models for low-resourced languages. In Proceedings of the 1st Workshop on Multilingual Representation Learning,
pages 116–126, Punta Cana, Dominican Republic. Association for Computational Linguistics.
Maneesha Perera, Rajith Vidanaarachchi, Sangeetha Chandrashekeran, Melissa Kennedy, Brendan Kennedy, and Saman Halgamuge.
Exploring the intersection of indigenous knowledge and ai: A systematic review and future directions.
Malin Petzell. 2012. The linguistic situation in tanzania. Moderna språk, 106(1):136–144.
Mario Piergallini, Rouzbeh Shirvani, Gauri Shankar Gautam, and Mohamed Chouikha. 2016. Word-level language identification and
predicting codeswitching points in swahili-english language data. In Proceedings of the second workshop on computational
approaches to code switching, pages 21–29.
Edoardo Maria Ponti, Helen O’horan, Yevgeni Berzak, Ivan Vuli´c, Roi Reichart, Thierry Poibeau, Ekaterina Shutova, and Anna
Korhonen. 2019. Modeling language variation and universals: A survey on typological linguistics for natural language
processing. Computational Linguistics, 45(3):559–601.
Yi Chern Tan and L Elisa Celis. 2019. Assessing social and intersectional biases in contextualized word representations. Advances in
neural information processing systems, 32.
Goya van Boven, Stephanie Hirmer, and Costanza Conforti. 2022. At the intersection of nlp and sustainable development: exploring
the impact of demographic-aware text representations in modeling value on a corpus of interviews. In Proceedings of the
Thirteenth Language Resources and Evaluation Conference, pages 2007–2021.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan Li, Dayiheng Liu, Fei Huang,
et al. 2024. Qwen2 technical report. arXiv preprint arXiv:2407.10671.
Forest Yang, Mouhamadou Cisse, and Sanmi Koyejo. 2020. Fairness with overlapping groups; a probabilistic perspective. Advances
in neural information processing systems, 33:4067–4078.
12

--- Page 13 ---

A PREPRINT
A
Appendix
A.1
Dataset Summary Statistics
Characteristic
Description
Unique users
2170
Text fields (per user)
Literacy, Numeracy, Trust, Anxiety
Age
Mean: 30.3, Over 50: 2.5%
Race
95.3% black, 3.46% multi-/bi-racial, 1.24% other
Sex (Male)
52.72%
Income (KES)
75.94% < 2.8 M
Education
72.73% college grad or higher
Tribe (top 5)
29.59% Kikuyu, 15.3% Luhya, 13.82% Luo, 11.15%
Kamba, 8.29% Kalenjin
Examples of other
behavior/psychometric
dimensions
Usage of prescription drugs, Presence of primary care
physician, Frequency of doctor visits, Smoking and drink-
ing frequency
Response times
42 minutes (mean), 39 minutes (median)
Mean response lengths
(chars)
128 (Literacy), 121 (Numeracy), 128 (Trust), 127 (Anxi-
ety)
Table 5: Summary statistics of the Swahili dataset, including participant demographics, text length, and survey
completion details.
B
Appendix: Other Evaluation and Fairness Results
B.1
Model Evaluation
Table 6 provides an expanded version of Table 3 that includes standard deviations calculated over five fold cross-
validations. These results offer additional visibility into the stability of each model.
Model
Continuous Classification
Binary Classification
Literacy
Trust
Anxiety
Numeracy
Literacy
Trust
Anxiety
Numeracy
r
RMSE
r
RMSE
r
RMSE
r
RMSE
AUC
F 1
AUC
F 1
AUC
F 1
AUC
F 1
Regression
.098±.074 .388±.298 .288±.054 .157±.008 .123±.019 .261±.006 .022±.041 .297±.011 .603±.015 .589±.025 .711±.022 .784±.015 .558±.017 .570±.019 .563±.021 .686±.022
AfriBERTa
.202±.049 .174±.003 .436±.029 .133±.003 .156±.043 .234±.008 .129±.033 .242±.016 .604±.028 .655±.019 .650±.022 .635±.025 .585±.017 .647±.029 .570±.029 .648±.017
SwahBERT
.181±.023 .180±.012 .392±.026 .136±.004 .089±.024 .249±.009 .103±.022 .234±.004 .578±.025 .657±.005 .636±.035 .652±.025 .567±.011 .648±.016 .536±.030 .640±.024
XLM-RoBERTa .145±.035 .172±.009 .398±.011 .133±.003 .103±.042 .229±.002 .129±.064 .207±.007 .572±.021 .659±.018 .647±.024 .669±.021 .557±.013 .652±.013 .525±.048 .636±.028
mBERT
.180±.034 .174±.009 .427±.015 .133±.002 .138±.026 .228±.004 .133±.021 .220±.012 .559±.028 .659±.011 .649±.019 .652±.022 .543±.029 .652±.013 .585±.029 .644±.029
Qwen2.5-7B
.121±.033 .215±.013 .337±.027 .250±.027 .084±.033 .266±.009 .031±.058 .294±.023 .538±.022 .565±.015 .566±.023 .496±.114 .483±.013 .386±.079 .527±.009 .572±.105
Qwen2.5-72B
.169±.039 .209±.012 .471±.017 .225±.014 .134±.028 .247±.008 .023±.037 .257±.024 .546±.021 .629±.012 .639±.036 .735±.059 .503±.016 .626±.029 .522±.013 .532±.093
Llama3.1-8B
.125±.052 .118±.014 .163±.003 .187±.003 .039±.009 .255±.023 .019±.054 .212±.019 .533±.025 .526±.041 .563±.036 .665±.019 .503±.038 .607±.077 .523±.023 .591±.129
Llama3.1-405B
.255±.063 .165±.013 .541±.042 .215±.012 .204±.025 .288±.030 .039±.059 .284±.036 .539±.023 .675±.013 .608±.053 .712±.118 .517±.016 .670±.018 .502±.006 .653±.020
Table 6: Expanded model performance metrics including standard deviations across five-fold cross-validation for both
regression and binary classification tasks.
B.2
Model Fairness
We also assessed group-level fairness using DI, focusing on two tribes with high representation in our dataset: Kikuyu
and Kamba. We computed DI for each task by comparing the positive prediction rates for these groups against the rest
of the population (i.e., Kikuyu or Kamba as the privileged classes versus All other as the protected class). As shown in
Figure 6, the DI values for most tasks are close to 1, suggesting minimal disparity. However, in the Numeracy task for
Kamba group, DI exceeds the 1.2 threshold when evaluated using Llama 3.1-405b and Qwen2.5-72B.
13

--- Page 14 ---

A PREPRINT
This indicates that participants outside the Kamba group (i.e., the protected group) are more likely to receive positive
predictions for Numeracy compared to Kamba participants. This disparity may stem from variation in how numeracy-
related concepts are linguistically expressed across groups, with non-Kamba participants using phrasing that better
aligns with the model’s learned patterns and trigger positive classifications.
Figure 6: Relationship between model performance (AUC) and group fairness, measured by Disparate Impact (DI), for
the Kamba and Kikuyu groups compared against all other tribal subgroups.
C
Appendix: Experiments and Model Parameters
As mentioned in section 4, we conducted both regression and classification experiments across four psychometric
tasks: Subjective Literacy, Trust in Physicians, Anxiety visiting the Doctor, and Health Numeracy. Each task involved
predicting either a continuous score or a binarized label derived from human-annotated data. Our goal was to compare
model performance and fairness across baseline models, PLMs, and LLMs in both zero-shot and few-shot settings.
C.1
TF-IDF Baseline Models
We implemented two classical baselines using scikit-learn: a linear regression model for continuous score prediction,
and a logistic regression model for binary classification. For both, free-text responses were vectorized using TF-IDF
with an n-gram range of 1 to 3. The logistic model used up to 30,000 features, while the linear model used up to 10,000
features to reduce dimensionality. Logistic regression was evaluated using Accuracy, F1, AUC, Precision, and Recall.
Linear regression was evaluated using Root Mean Squared Error (RMSE) and Pearson correlation (r). All experiments
used 5-fold cross-validation. We report the average F1, AUC, r, and RMSE across all five folds.
C.2
Pretrained Language Models
We fine-tuned four transformer-based PLMs: mBERT, XLM-RoBERTa, AfriBERTa, and SwahBERT, using the Hugging
Face Transformers library. For classification, we discretized continuous scores using the median and fine-tuned models
with a batch size of 16, a learning rate of 1e-5, and 5 epochs. Weighted cross-entropy loss was used to mitigate class
imbalance. For regression, we predicted the continuous scores directly using mean squared error loss, a batch size of 8,
and otherwise similar hyperparameters. All PLMs were evaluated using 5-fold cross-validation on an NVIDIA A100
GPU. We report AUC and F1 scores for classification, and RMSE and Pearson r for regression.
C.3
Large Language Models
We evaluated four multilingual LLMs—Qwen2.5-72B-Instruct, Qwen2.5-7B-Instruct, Llama3.1-405B-Instruct, and
Llama3.1-8B-Instruct—using few-shot prompting via the Replicate and DeepInfra APIs. For the regression task,
14

--- Page 15 ---

A PREPRINT
each prompt included three few-shot examples (low, medium, high) from the training fold, followed by a test text,
and instructed the model to return a numeric score between 0 and 1. For classification, prompts consisted of three
binary-labeled examples and a test text, with the model instructed to respond with “Yes” or “No.” Predictions were
parsed using basic string-matching logic.
All API calls used consistent decoding parameters across models: temperature=0.3, max_tokens=100, top_p=1.0,
and no specified stop sequence. Each model received the same prompt format across folds. Evaluation was conducted
per task using AUC and F1 for classification, and RMSE and Pearson’s r for regression.
(a) Few-shot Prompt
(b) Binary Prompt
Figure 7: Examples of prompt formats used in our experiments.
C.4
Intersectional Fairness Evaluation
We evaluated intersectional fairness by computing two complementary group-level metrics: Disparate Impact (DI)
and Fairness Violations (FV). Our analysis focused on five binary demographic attributes: age (≤30), gender (male),
tribal identity (Bantu vs. Non-Bantu), education (≥some college), and income (≤2.58M KES). Each attribute was
binarized to distinguish between a protected group (coded as 0) and a privileged group (coded as 1). To capture
compounded disadvantage, we generated all 1-way to 3-way combinations of these attributes, resulting in 1, 2, and
3-way intersectional subgroups. Each combination was encoded as a binary indicator representing whether a participant
belonged to all constituent protected categories. This allowed us to examine model performance disparities not only
across individual demographic groups but also across their intersections. We excluded subgroups with fewer than two
members in either protected or privileged categories to ensure statistical robustness. DI and FV metrics were aggregated
across 1-way (DI), 2-way (DI+, FV+), and 3-way (DI++, FV++) levels and are summarized in Table 7.
While group-level fairness scores indicate relatively limited disparities, the intersectional analysis reveals that combining
multiple demographic attributes surfaces more complex patterns of bias (Table 7). A clear compounding effect emerges
in the Anxiety task for mBERT, where DI decreases from 0.90 at the group level to 0.86 (DI+) and further to 0.83
(DI++). This pattern suggests that as more identity dimensions are layered, the model increasingly underpredicts for
certain subgroups. Fairness Violation (FV) scores further confirm this trend. In the Trust task, XLM-RoBERTa’s score
increases from 0.60 at the group level (FV) to 0.80 at the three-way intersection level (FV++), reflecting a sharp rise in
disparity as more demographic attributes are considered. These findings demonstrate that fairness deteriorates when
multiple identity dimensions are considered jointly.
Note on Tribe Binarization: Tribal identity was binarized as Bantu vs. Non-Bantu to reflect East African linguistic
family structures (Mazrui 1998, Heine and Nurse 2000). Bantu languages, such as Kikuyu and Kamba, share
agglutinative morphology and phonological structures, while Non-Bantu groups, such as Luo and Somali, come from
15

--- Page 16 ---

A PREPRINT
Task
Model
DI
DI+
DI++
FV
FV+
FV++
Literacy
mBERT
0.94
0.98
0.99
0.20
-
-
XLM-RoBERTa
0.81
0.88
0.86
0.20
0.10
0.20
AfriBERTa
0.93
0.94
0.93
-
-
-
SwahBERT
0.93
0.95
0.94
0.40
0.10
-
Trust
mBERT
1.05
1.04
1.05
0.60
0.40
0.30
XLM-RoBERTa
1.19
1.15
1.16
0.60
0.70
0.80
AfriBERTa
1.05
1.02
1.01
0.20
0.20
0.20
SwahBERT
1.03
1.00
0.99
0.40
0.20
0.30
Anxiety
mBERT
0.90
0.86
0.83
-
-
0.30
XLM-RoBERTa
1.09
1.07
1.06
0.20
0.20
0.10
AfriBERTa
0.96
0.97
0.99
-
-
-
SwahBERT
0.95
0.96
0.94
-
-
-
Numeracy
mBERT
1.07
1.02
1.00
0.40
0.20
0.10
XLM-RoBERTa
0.94
0.96
0.98
-
-
-
AfriBERTa
0.96
0.95
0.95
-
-
-
SwahBERT
1.03
1.02
1.02
0.20
-
-
Table 7: Disparate Impact (DI) and Fairness Violation (FV) scores for one-way (DI, FV), two-way (DI+, FV+), and
three-way (DI++, FV++) intersectional subgroup analyses. Bolded values indicate the greatest observed disparity.
Dashes indicate zero values.
Nilotic and Cushitic families with distinct syntactic and lexical properties. This binarization captures meaningful
sociolinguistic variation while preserving statistical power and interpretability in fairness evaluations.
D
Appendix: Additional Dataset Information
The table below summarizes the frequency of linguistic features identified in the Swahili dataset. The counts represent
the total number of instances each feature type appeared across all text responses. This taxonomy guided our fairness
analysis by enabling targeted evaluation of model performance across diverse linguistic phenomena.
Feature Group
Category
Count
Lexical
Vocabulary Richness (Hapax Legom-
ena)
145,628
Word Length Variation
360
Loan Words
2,819
Code-Mixing
245
Sheng
17
Function Word Usage
347,448
Structural
Word Count & Distribution
175,269
Reduplication
245
Absence of Phonetic Markers
11
Punctuation Frequency
10,938
Question/Exclamation Usage
31
Syntactic
Verb Morphology
9,230
Discourse Markers
2,755
Content-Specific
Medical Terminology
8,274
Tribal Lexicon
2,323
Table 8: Frequency of Linguistic Features in the Dataset
16

```
