---
title: "2026-Unknown-Cross-Lingual Probing and Community-Grounded Analysis of Gender Bias - PDF Extract"
source_pdf: "2026-Unknown-Cross-Lingual Probing and Community-Grounded Analysis of Gender Bias.pdf"
pages: 8
extracted_at: "2026-02-13T09:50:30.886162"
---

# PDF Extract: 2026-Unknown-Cross-Lingual Probing and Community-Grounded Analysis of Gender Bias

**Source PDF:** 2026-Unknown-Cross-Lingual Probing and Community-Grounded Analysis of Gender Bias.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Cross-Lingual Probing and
Community-Grounded Analysis of Gender
Bias in Low-Resource Bengali
Md Asgor Hossain Reaj
Department of Computer Science
AIUB, Dhaka, Bangladesh
20-43999-2@student.aiub.edu
Rajan Das Gupta
Department of Computer Science
AIUB, Dhaka, Bangladesh
18-36304-1@student.aiub.edu
Jui Saha Pritha
Department of Computer Science
AIUB, Dhaka, Bangladesh
17-35507-3@student.aiub.edu
Abdullah Al Noman
Department of Information Technology
Wilmington University, Delaware, USA
anoman001@my.wilmu.edu
Abir Ahmed
Department of Information Technology
WUST, Virginia, USA
abira.student@wust.edu
Golam Md Mohiuddin
Faculty of Information Science and Technology
Multimedia University, Melaka, Malaysia
golam.md.mohiuddin@student.mmu.edu.my
Tze Hui Liew
Centre for Intelligent Cloud Computing
Multimedia University, Melaka, Malaysia
thliew@mmu.edu.my
Abstract—Large Language Models (LLMs) have
achieved significant success in recent years; yet, issues
of intrinsic gender bias persist, especially in non-
English languages. Although current research mostly
emphasizes English, the linguistic and cultural biases
inherent in Global South languages, like Bengali,
are little examined. This research seeks to examine
the characteristics and magnitude of gender bias in
Bengali, evaluating the efficacy of current approaches
in identifying and alleviating Bias. We use several
methods to extract gender-biased utterances, includ-
ing lexicon-based mining, computational classification
models, translation-based comparison analysis, and
GPT-based bias creation. Our research indicates that
the straight application of English-centric bias detec-
tion frameworks to Bengali is severely constrained
by language disparities and socio-cultural factors that
impact implicit biases. To tackle these difficulties, we
executed two field investigations inside rural and low-
income areas, gathering authentic insights on gender
Bias. The findings demonstrate that gender Bias in
Bengali presents distinct characteristics relative to En-
glish, requiring a more localized and context-sensitive
methodology. Additionally, our research emphasizes
the need of integrating community-driven research
approaches to identify culturally relevant biases of-
ten neglected by automated systems. Our research
enhances the ongoing discussion around gender bias
in AI by illustrating the need to create linguistic tools
specifically designed for underrepresented languages.
This study establishes a foundation for further in-
vestigations into bias reduction in Bengali and other
Indic languages, promoting the development of more
inclusive and fair NLP systems.
Index Terms—Gender Bias, Natural Language Pro-
cessing, Language Bias, Large Language Models
I. INTRODUCTION
Natural Language Processing (NLP) has come
a long way thanks to Large Language Models
(LLMs), which do very well at tasks like translation,
sentiment analysis, and answering questions. Even
though these models are used a lot, they often show
bias, which may make social inequalities worse,
particularly for disadvantaged groups [1], [2]. There
is a lot of study on gender bias in English NLP, but
not much on low-resource languages like Bengali.
arXiv:2601.17764v1  [cs.CL]  25 Jan 2026

--- Page 2 ---

Bengali is quite different from Western languages
in terms of its language and culture, which makes
it harder to find and fix prejudice.
Sadhu et al.’s 2024 study and other research have
started to look at gender stereotypes in multilingual
models for Bengali [3], but there hasn’t been a full
investigation yet. This study fills up the gaps by
looking particularly at gender prejudice in Bengali
LLMs, taking into account the language’s unique
syntax, gender-neutral pronouns, and cultural dif-
ferences. Our work includes creating custom ways
to find gender-biased patterns in Bengali, taking
into account its unique language features; testing
machine learning models to consistently find gender
bias in Bengali texts; and using generative models
to look at how gender bias shows up in synthetic
Bengali text.
We look at a lot of different types of data [4],
such as social media, news stories, and translated
statistics on gender prejudice. The results show that
unconscious biases exist and that it is not always
possible to simply adapt English-based frameworks
to Bengali. The goal of this endeavor is to improve
fair NLP technologies that operate well for the large
number of people who speak Bengali.
II. RELATED WORK
A. Bias Detection
Detecting bias in datasets and language models is
a prerequisite for building equitable NLP systems.
Several evaluation protocols, such as CrowS-Pairs
[5] and StereoSet [6], benchmark English text for
gender and societal biases. However, these tools
transfer poorly to Bengali due to its distinct lin-
guistic structure and sociocultural context. Most
prior research focuses on English and other Indo-
European languages with grammatical gender cat-
egories [7]. Although Bengali lacks grammatical
gender, it still encodes implicit and explicit biases
shaped by cultural norms. This motivates the design
of methods specifically adapted to Bengali.
We propose a framework integrating generative,
heuristic, and lexical analyses to detect biases across
semantics, syntax, and morphology. This ensures
more comprehensive diagnostic coverage than di-
rectly applying English-centric tools.
B. Debiasing Methods for Bengali Language Mod-
els
Bias detection and mitigation are interdependent
tasks for deploying LMs in practice. While Bengali
lacks explicit gender categories, implicit cultural
biases remain pervasive. Addressing these requires
targeted strategies. Kaneko et al. [8], [9] distin-
guished between intrinsic and extrinsic bias evalua-
tions, noting weak correlations [10], [11]. Lauscher
et al. [12] mitigated bias using adapter modules
trained on counterfactually augmented data. Barikeri
et al. [13] introduced REDDITBIAS for dialogue-
based bias detection, and Pujari et al. [14] projected
embeddings away from a gendered subspace. These
methods, while effective in English, require adapta-
tion for Bengali. Building on linguistic analyses of
Bengali [15], we propose counterfactual augmenta-
tion and modified lexical analysis to capture implicit
biases in cultural discourse. Chakraborty et al. [16]
highlighted abusive Bengali social media language,
underscoring the need for curated resources. Our
approach incorporates such insights, extending prior
datasets such as Bengali & Banglish [17] for more
inclusive LM development.
C. Challenges
Bias mitigation remains difficult due to dataset
artifacts, annotation practices, and entrenched so-
ciocultural norms. Orgad and Belinkov [18] empha-
sized entangled metrics; Draws et al. [19] and Shar-
ifi Noorian et al. [20]–[22] showed that annotator
assumptions introduce bias. Zhou et al. [23], [24]
demonstrated that dataset re-labeling can outperform
model-level debiasing. Gender bias is particularly
persistent. Studies [25]–[31] confirm that social bi-
ases embedded in corpora propagate into models,
affecting fairness [32]. Reviews such as Stanczak
and Augenstein [33], [34] and Devinney et al. [35]
document these issues, though largely in English
and Global North contexts. This leaves critical blind
spots for Global South languages. We conducted ex-
periments adapting English-based detection methods
to Bengali, revealing clear limitations. To address
this, we adopted a community-driven approach,
engaging Bengali speakers in data collection and
validation. Diverse annotators are essential, since
perceptions of bias depend on social and cultural
background.

--- Page 3 ---

Finally, perspectives from rural Bangladesh re-
main underrepresented despite increasing digital
adoption. Incorporating such viewpoints through
crowdwork offers a promising pathway toward fairer
Bengali NLP systems.
III. SOURCING BENGALI DATA FOR GENDER
BIAS IDENTIFICATION
A. Datasets
To identify gender bias in Bengali, we draw
on four complementary sources that jointly pro-
vide controlled supervision, cross-lingual transfer
signals, and ecologically valid in-the-wild text, as
summarized in Figure 1.
Gender Bias
Bangla
Language
Technology
Crowd
Sourcing
Data
Mining
Analysis
Learning
Annotation
Study
Gender Bias
Awareness
Workshop
YouTube
Comments
FSB
BUG
CORGI-PM
Datasets
YouTube
Comments
GPT
Generations
BUG
CORGI-PM
Methods
Fig. 1. Gender Bias Analysis Pipeline
CORGI-PM is a Chinese corpus of 32.9K sen-
tences, including 5.2K labeled as gender-biased,
constructed via keyword-based filtering and sen-
tence re-ranking; in our setting, it supplies bias-
bearing material for translation-based transfer into
Bengali and supervision for binary classification.
BUG is a large-scale English resource (108K sen-
tences; 54K stereotypical, 30K anti-stereotypical,
24.5K neutral) extracted through lexical–syntactic
pattern matching from sources such as Wikipedia
and PubMed; we translate a stratified subset to
test whether stereotype signals persist after cross-
lingual transfer and remain meaningful in Bengali
contexts. To capture organically produced discourse,
we collect 7,340 Bengali YouTube comments using
targeted queries about gender-related controversies;
this corpus serves as a real-world evaluation bed
for both classification and scoring models. Finally,
FSB comprises 1,000 GPT-generated Bengali texts
annotated for gender bias via systematic prompting
of GPT-3.5-Turbo; it provides label-rich supervision
for training a continuous bias scorer and a seeded
pool for retrieval and filtering. Taken together, these
datasets enable a principled assessment of gender
bias in Bengali across semantics, syntax, and prag-
matics, while balancing controlled experimentation
with cultural and platform-specific realism.
IV. EXPERIMENTS
To evaluate multiple strategies for sourcing and
detecting gender-biased Bengali text, we imple-
mented six complementary approaches. For each
method, we report the yield of biased sentences, as
determined through manual validation.
LaBSE Mining Following Albalak et al. [36],
we sampled 10M Bengali sentences from a large
corpus. Using LaBSE embeddings [37], we built a
FAISS index of all sentences and queried it with
embeddings of the top 100 most-biased English
seed sentences from FSB [38]. For each query, we
retrieved the five most similar Bengali sentences by
cosine similarity, yielding 500 candidates. From 200
randomly sampled candidates, manual annotation
indicated ∼10% were biased. This demonstrates that
cross-lingual retrieval surfaces some biased content,
though yield remains limited due to domain and
cultural mismatch between English FSB seeds and
Bengali corpora.
Translation into Bengali We sampled 100 biased
sentences each from CORGI-PM [39] and BUG
[40], translating them into Bengali using Azure
Translate. One author annotated the results for bias
retention and cultural relevance. We found that
24% (BUG) and 33% (CORGI-PM) retained gender
bias post-translation and were contextually valid
in Bengali, indicating partial transferability of En-
glish/Chinese bias corpora.
CORGI Classifier We fine-tuned mBERT [41]
on CORGI-PM [39] using the provided splits. The
model achieved 0.81 accuracy on the test set. Apply-
ing it to 7,340 YouTube comments flagged 4.67%

--- Page 4 ---

(343) as biased. Manual verification of 100 flagged
comments confirmed 36% as biased, highlighting
domain-shift limitations when transferring from cu-
rated corpora to colloquial social media.
TABLE I
HYPERPARAMETERS FOR CORGI CLASSIFIER FINE-TUNING
Epochs
Batch Size
Learning Rate
Optimizer
Patience
4
128
0.00001
AdamW
3
FSB Scorer We optimized BanglaBERT using
LoRA [42] on 1,000 FSB sentences [38], incor-
porating a regression head to forecast bias scores
within the range of [−1, 1]. The model attained a
mean squared error (MSE) of 0.057 and a Pearson
correlation coefficient (r) of 0.85 during validation,
comparable to the findings of [38]. We manually
validated the top 100 scored YouTube comments,
finding that 21% exhibited bias.
TABLE II
HYPERPARAMETERS FOR TRAINING THE FSB SCORER
Epochs
lr
Scheduler
Optimizer
Batch Size
25
0.0008
cosine
Adam
32
Warmup Steps LoRA r
LoRA α
LoRA Dropout
LoRA Modules
50
8
16
0.1
[”query”, ”output”]
CORGI-style Mining We collected 684 Bengali
adjectives and computed an association score with
gender by comparing embeddings of each adjective
to Bengali words for “man” and “woman” using
mBERT and BanglaBERT. Specifically, we defined:
s(a) = cos(e(a), e(woman)) −cos(e(a), e(man)).
After z-normalization, we selected top female-
leaning adjectives and retrieved sentences from
Kathbath and LOIT corpora. Thresholds were tuned
to yield ∼100 sentences per corpus per model.
Manual inspection revealed 3% of mBERT-retrieved
sentences were biased, while none retrieved via
BanglaBERT were biased, showing the limited util-
ity of purely lexicon-driven heuristics in Bengali.
GPT Generation Using FSB prompts [38], we
generated 1,800 English sentences. Six annotators
reviewed 300 samples, discarding 8% as cultur-
ally irrelevant to Bangladesh. The remainder were
usable, with varying degrees of bias, highlighting
generation as a high-yield but low-diversity data
source.
A. Results and Analysis
The yield of potentially gender-biased Ben-
gali text varied substantially across methods and
datasets. As shown in Table III, GPT-based gener-
ation achieved the highest precision, while cross-
lingual and heuristic approaches produced relatively
lower yields. Below we analyze the key limitations
behind these outcomes.
TABLE III
YIELD OF POTENTIALLY GENDER-BIASED TEXT FROM
DIFFERENT DATA SOURCES AND METHODS.
Dataset
Method
# of Samples
Yield (%)
Bengali text corpora
LaBSE mining
250
18
BUG
Azure Translate
120
27
CORGI-PM
Azure Translate
110
31
YouTube comments
CORGI classifier
90
38
YouTube comments
FSB scorer
120
19
GPT generations
FSB
1750
90
Internet data is Anglocentric. Bengali gender-
prejudiced text is difficult to extract from large-scale
online corpora, since most web content aligns with
mainstream English discourse [43]–[45]. Although
we collected 10M Bengali sentences and applied
LaBSE retrieval with highly biased English seeds,
only ∼20% of sampled candidates contained bias.
This suggests structural and stylistic differences
between curated English bias corpora and cleaned
Bengali corpora suppress retrieval yield.
Translation is a bottleneck. Many bias-bearing
terms fail to transfer naturally across languages. For
example, Bengali equivalents such as “shikkhok”
(teacher) or “grihini” (housewife) differ from col-
loquial terms like “teacher” or “bou”. As prior
work notes [46], [47], such mismatches reduce the
ability to faithfully preserve gender stereotypes. In
our setting, only 24–33% of translated sentences
retained bias in a Bangladeshi context.
Social media data limitations. Social platforms
are valuable for organic bias signals but are domi-
nated by English discourse [48]–[51]. From 7,340
YouTube comments, only 4.7% were flagged as
biased by classifiers, with even fewer validated
as true positives. Platform restrictions and code-

--- Page 5 ---

switching practices (mix of Bengali and English)
further complicate reliable retrieval [52].
Cross-lingual and domain transfer loss. Recent
studies [53]–[57] highlight limited generalizability
of multilingual embeddings. We observed similar
effects: CORGI classifiers fine-tuned on curated cor-
pora transferred poorly to noisy YouTube comments,
while the FSB scorer trained on GPT-generated
sentences struggled on colloquial text. These mis-
matches underscore the risks of applying models
trained on narrow domains to real-world social
discourse.
Heuristic retrieval challenges. Adjective-based
mining produced extremely low yields (3% with
mBERT and 0% with BanglaBERT). Topic-based
retrieval from YouTube also led to many false pos-
itives. This reflects both the brittleness of lexical
heuristics in Bengali and the limited cultural ground-
ing of LLMs, which remain insensitive to nuanced
stereotypes in Bangladeshi communities [58].
Data diversity constraints. Finally, our experi-
ments showed that GPT-based generations yield the
highest proportion of biased sentences (90%), but
lack topical and idiomatic diversity. Generated sen-
tences often appeared repetitive, simplistic, and cul-
turally shallow. As prior work emphasizes [59]–[61],
achieving representative coverage of bias requires
diverse data sources and contextually grounded
seeds, which remain scarce for Bengali.
V. DISCUSSION AND LIMITATIONS
This study provides a systematic investigation of
gender bias in Bengali, revealing both methodolog-
ical and sociocultural challenges in low-resource
contexts. Computational approaches such as LaBSE
mining, translation-based transfer, and keyword-
driven retrieval showed limited effectiveness due
to contextual misalignment and high false-positive
rates, while GPT-based generation achieved the
highest yield (90%) but lacked linguistic and cultural
diversity. Data mining was further constrained by
the Anglocentric dominance of online corpora, code-
switching, and restricted access to social platforms,
which limit the availability of culturally relevant
Bengali data [43]–[45], [52]. The low prevalence
of validated bias and the fragility of cross-domain
transfer align with documented limitations of multi-
lingual embeddings [53]–[57]. Translation pipelines
also frequently failed to capture colloquial nuance,
with transliteration inconsistencies and idiomatic
gaps further reducing quality [46], [47].
To complement automated methods, we con-
ducted field studies to elicit community-grounded
examples. Participants often conflated gender bias
with biological sex; interactive activities (e.g., skits,
role-play) helped clarify stereotypes. Yet, annotation
with rural and low-income participants was hindered
by digital barriers, formal language instructions,
and task complexity; manual review showed that
about 30% of collected data was culturally mis-
aligned. These findings underscore the need for
participatory, simplified, and context-sensitive an-
notation frameworks. Addressing current limitations
will require richer prompts and culturally grounded
lexical resources for generation [59]–[61], improved
translation and preprocessing systems, and tighter
integration of computational and community-driven
methods. Finally, adopting intersectional perspec-
tives that account for caste, religion, geography, and
socioeconomic status is essential to capture the full
scope of systemic bias and to build equitable NLP
systems for Bengali and related underrepresented
languages.
VI. CONCLUSION
This paper presented one of the first systematic
studies of gender bias in Bengali, evaluating cross-
lingual retrieval, translation-based transfer, classi-
fier training, continuous scoring, heuristic adjective
mining, and GPT-based generation. Our findings
reveal that while generative methods yield large
quantities of biased text, they lack cultural and lin-
guistic diversity, whereas cross-lingual and heuristic
methods produce lower precision due to structural
mismatches. Translation pipelines preserve bias only
partially, and classifiers trained on curated datasets
transfer poorly to colloquial Bangladeshi social me-
dia, underscoring the limitations of directly adapting
English-centric frameworks.
These results highlight the need for culturally
aware design, including improved translation sys-
tems, context-sensitive lexicons, and participatory
data collection to surface stereotypes invisible to
automated methods. Moreover, future NLP systems
for Bengali should integrate community-informed
annotation and adopt intersectional perspectives that

--- Page 6 ---

consider not only gender but also caste, religion,
geography, and socioeconomic class. Such efforts
are essential to advance equitable and inclusive
language technologies for underrepresented commu-
nities in the Global South.
ACKNOWLEDGMENT
The authors would like to thank the ELITE Re-
search Lab for their support and valuable contribu-
tions to this research.
REFERENCES
[1] T. Hagendorff, S. Fabi, and M. Kosinski, “Human-like
intuitive behavior and reasoning biases emerged in large
language models but disappeared in ChatGPT,” Nature
Computational Science, vol. 3, no. 10, pp. 833–838, 2023.
[2] M. Kabir, M. S. Islam, M. T. R. Laskar, M. T. Nayeem,
M. S. Bari, and E. Hoque, “Benllmeval: A comprehensive
evaluation into the potentials and pitfalls of large language
models on bengali nlp,” arXiv preprint arXiv:2309.13173,
2023.
[3] J. Sadhu, M. R. Saha, and R. Shahriyar, “An empirical study
of gendered stereotypes in emotional attributes for bangla
in multilingual large language models,” arXiv preprint
arXiv:2407.06432, 2024.
[4] M. T. Hosain, M. K. Morol, and M. J. Hossen, “A hybrid
self attentive linearized phrase structured transformer based
rnn for financial sentence analysis with sentence level
explainability,” Scientific Reports, vol. 15, no. 1, p. 23893,
2025.
[5] R. Zalkikar and K. Chandra, “Measuring social biases in
masked language models by proxy of prediction quality,”
arXiv preprint arXiv:2402.13954, 2024.
[6] M. Nadeem, A. Bethke, and S. Reddy, “Stereoset: Measur-
ing stereotypical bias in pretrained language models,” arXiv
preprint arXiv:2004.09456, 2020.
[7] J. Vig, S. Gehrmann, Y. Belinkov, S. Qian, D. Nevo,
Y. Singer, and S. Shieber, “Investigating gender bias in lan-
guage models using causal mediation analysis,” Advances in
neural information processing systems, vol. 33, pp. 12 388–
12 401, 2020.
[8] M. Kaneko, D. Bollegala, and N. Okazaki, “Debiasing
isn’t enough!–on the effectiveness of debiasing mlms and
their social biases in downstream tasks,” arXiv preprint
arXiv:2210.02938, 2022.
[9] I. Zerine, M. M. Islam, M. S. Islam, M. Y. Ahmad, and
M. A. Rahman, “Climate risk analytics for us agriculture
sustainability: Modeling climate impact on crop yields and
supply chain to support federal policies food security and
renewable anergy adoption,” Cuestiones de Fisioterapia,
vol. 49, no. 3, pp. 241–258, 2020.
[10] A. Salam, I. M. Chowdhury, M. M. Sadeque, and
B. Taslimul, “Save time for public transport users in a
developing country,” International Journal of Education
and Management Engineering, vol. 11, no. 8, pp. 27–33,
2016.
[11] M. M. Islam, I. Zerine, M. A. Rahman, M. S. Islam,
and M. Y. Ahmed, “Ai-driven fraud detection in financial
transactions-using machine learning and deep learning to
detect anomalies and fraudulent activities in banking and e-
commerce transactions,” Available at SSRN 5287281, 2024.
[12] A. Lauscher, T. Lueken, and G. Glavaˇs, “Sustainable
modular debiasing of language models,” arXiv preprint
arXiv:2109.03646, 2021.
[13] S. Barikeri, A. Lauscher, I. Vuli´c, and G. Glavaˇs, “Red-
ditbias: A real-world resource for bias evaluation and de-
biasing of conversational language models,” arXiv preprint
arXiv:2106.03521, 2021.
[14] A. K. Pujari, A. Mittal, A. Padhi, A. Jain, M. Jadon,
and V. Kumar, “Debiasing gender biased hindi words with
word-embedding,” in Proceedings of the 2019 2nd Interna-
tional Conference on Algorithms, Computing and Artificial
Intelligence, 2019, pp. 450–456.
[15] N. S. Dash, “Linguistic divergences in english to bengali
translation,” International Journal of English Linguistics,
vol. 3, no. 1, p. 31, 2013.
[16] P. Chakraborty and M. H. Seddiqui, “Threat and abusive
language detection on social media in bengali language,” in
2019 1st International Conference on Advances in Science,
Engineering and Robotics Technology (ICASERT).
IEEE,
2019, pp. 1–6.
[17] M. R. Faisal, A. M. Shifa, M. H. Rahman, M. A. Uddin, and
R. M. Rahman, “Bengali & banglish: A monolingual dataset
for emotion detection in linguistically diverse contexts,”
Data in Brief, vol. 55, p. 110760, 2024.
[18] H. Orgad and Y. Belinkov, “Choose your lenses: Flaws
in gender bias evaluation,” in Proceedings of the 4th
Workshop on Gender Bias in Natural Language Processing
(GeBNLP).
Association for Computational Linguistics,
2022, pp. 151–167.
[19] T. Draws, A. Rieger, O. Inel, U. Gadiraju, and N. Tintarev,
“A checklist to combat cognitive biases in crowdsourcing,”
in Proceedings of the AAAI Conference on Human Compu-
tation and Crowdsourcing, vol. 9, 2021, pp. 48–59.
[20] S. S. Noorian, S. Qiu, B. Sayin, A. Balayn, U. Gadi-
raju, J. Yang, and A. Bozzon, “Perspective: Leveraging
human understanding for identifying and characterizing
image atypicality,” in Proceedings of the 28th International
Conference on Intelligent User Interfaces, 2023, pp. 650–
663.
[21] M. R. Abir, M. T. Hosain, M. Abdullah-Al-Jubair, and
M. Mridha, “Imvb7t: A multi-modal model for food prefer-
ences based on artificially produced traits,” arXiv preprint
arXiv:2412.16807, 2024.
[22] N. Vasker, A. T. Nafisa, M. A. Rahman, and M. Hasan,
“Heart disease classification with xai and kernel shap,”
in 2024 IEEE 3rd International Conference on Robotics,
Automation, Artificial-Intelligence and Internet-of-Things
(RAAICON).
IEEE, 2024, pp. 82–85.
[23] X. Zhou, M. Sap, S. Swayamdipta, Y. Choi, and N. Smith,
“Challenges in automated debiasing for toxic language
detection,” in Proceedings of the 16th Conference of the
European Chapter of the Association for Computational
Linguistics: Main Volume.
Association for Computational
Linguistics, 2021, pp. 3143–3155.
[24] M. T. Hosain, S. Rahman, M. K. Morol, and M. R.
Parvez, “Xolver: Multi-agent reasoning with holistic expe-
rience learning just like an olympiad team,” arXiv preprint
arXiv:2506.14234, 2025.
[25] T. Bolukbasi, K.-W. Chang, J. Y. Zou, V. Saligrama, and
A. T. Kalai, “Man is to computer programmer as woman is
to homemaker? debiasing word embeddings,” in Advances
in Neural Information Processing Systems 29, 2016, pp.
4349–4357.

--- Page 7 ---

[26] R. D. Gupta, M. T. Hosain, M. F. Mridha, and S. U. Ahmed,
“Multimodal programming in computer science with inter-
active assistance powered by large language model,” in Pro-
ceedings of the Human-Computer Interaction Conference,
M. Kurosu and A. Hashizume, Eds. Cham: Springer Nature
Switzerland, 2025, pp. 59–69.
[27] A. Caliskan, J. J. Bryson, and A. Narayanan, “Semantics de-
rived automatically from language corpora contain human-
like biases,” Science, vol. 356, no. 6334, pp. 183–186, 2017.
[28] M. T. Hosain, A. Zaman, M. S. Sajid, S. S. Khan, and
S. Akter, “Privacy preserving machine learning model per-
sonalization through federated personalized learning,” arXiv
preprint arXiv:2505.01788, 2025.
[29] S. Dev, E. Sheng, J. Zhao et al., “On measures of biases
and harms in nlp,” Findings of the Association for Com-
putational Linguistics: AACL-IJCNLP 2022, pp. 246–267,
2022.
[30] M. F¨arber, V. Burkard, A. Jatowt, and S. Lim, “A multi-
dimensional dataset based on crowdsourcing for analyzing
and detecting news bias,” in Proceedings of the 29th ACM
International Conference on Information & Knowledge
Management.
Association for Computing Machinery,
2020, pp. 3007–3014.
[31] T. Spinde, M. Plank, J.-D. Krieger et al., “Neural media
bias detection using distant supervision with babe - bias
annotations by experts,” in Findings of the Association for
Computational Linguistics: EMNLP 2021. Association for
Computational Linguistics, 2021, pp. 1166–1177.
[32] S. Raza, M. Garg et al., “Nbias: A natural language
processing framework for bias identification in text,” Expert
Systems with Applications, vol. 237, 2024.
[33] K. Stanczak and I. Augenstein, “A survey on gender
bias in natural language processing,” arXiv preprint, 2021.
[Online]. Available: https://arxiv.org/abs/2112.14168
[34] M. T. Hosain, M. R. Abir, M. Y. Rahat, M. Mridha,
and S. H. Mukta, “Privacy preserving machine learning
with federated personalized learning in artificially generated
environment,” IEEE open journal of the computer society,
2024.
[35] H. Devinney, J. Bj¨orklund, and H. Bj¨orklund, “Theories
of “gender” in nlp bias research,” in Proceedings of the
2022 ACM Conference on Fairness, Accountability, and
Transparency.
Association for Computing Machinery,
2022, pp. 2083–2102.
[36] A. Albalak, S. Levy, and W. Y. Wang, “Addressing
issues of cross-linguality in open-retrieval question an-
swering systems for emergent domains,” arXiv preprint
arXiv:2201.11153, 2022.
[37] F. Feng, Y. Yang, D. Cer, N. Arivazhagan, and W. Wang,
“Language-agnostic
bert
sentence
embedding,”
arXiv
preprint arXiv:2007.01852, 2020.
[38] R. Hada, A. Seth, H. Diddee, and K. Bali, “”fifty shades
of bias”: Normative ratings of gender bias in gpt generated
english text,” arXiv preprint arXiv:2310.17428, 2023.
[39] G. Zhang, Y. Li, Y. Wu, L. Zhang, C. Lin, J. Geng, S. Wang,
and J. Fu, “Corgi-pm: A chinese corpus for gender bias
probing and mitigation,” arXiv preprint arXiv:2301.00395,
2023.
[40] S. Levy, K. Lazar, and G. Stanovsky, “Collecting a large-
scale gender bias dataset for coreference resolution and ma-
chine translation,” arXiv preprint arXiv:2109.03858, 2021.
[41] J. Devlin, “Bert: Pre-training of deep bidirectional trans-
formers
for
language
understanding,”
arXiv
preprint
arXiv:1810.04805, 2018.
[42] E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang,
L. Wang, and W. Chen, “Lora: Low-rank adaptation of large
language models,” arXiv preprint arXiv:2106.09685, 2021.
[43] E.
M.
Bender,
T.
Gebru,
A.
McMillan-Major,
and
S. Shmitchell, “On the dangers of stochastic parrots: Can
language models be too big?” in Proceedings of the 2021
ACM conference on fairness, accountability, and trans-
parency, 2021, pp. 610–623.
[44] M. T. Hosain and M. K. Morol, “Can multi-turn self-
refined single agent lms with retrieval solve hard coding
problems?” in Proceedings of the 63rd Annual Meeting of
the Association for Computational Linguistics (Volume 4:
Student Research Workshop), 2025, pp. 129–142.
[45] M. T. Hosain, R. D. Gupta, and M. K. Morol, “Multilingual
question answering in low-resource settings: A dzongkha-
english benchmark for foundation models,” arXiv preprint
arXiv:2505.18638, 2025.
[46] E. Vanmassenhove, D. Shterionov, and M. Gwilliam, “Ma-
chine translationese: Effects of algorithmic bias on lin-
guistic complexity in machine translation,” arXiv preprint
arXiv:2102.00287, 2021.
[47] M.
Zhang
and
A.
Toral,
“The
effect
of
transla-
tionese in machine translation test sets,” arXiv preprint
arXiv:1906.08069, 2019.
[48] A. Founta, C. Djouvas, D. Chatzakou, I. Leontiadis,
J. Blackburn, G. Stringhini, A. Vakali, M. Sirivianos, and
N. Kourtellis, “Large scale crowdsourcing and characteri-
zation of twitter abusive behavior,” in Proceedings of the
international AAAI conference on web and social media,
vol. 12, no. 1, 2018.
[49] R. Hada, S. Sudhir, P. Mishra, H. Yannakoudakis, S. M.
Mohammad, and E. Shutova, “Ruddit: Norms of offen-
siveness for english reddit comments,” arXiv preprint
arXiv:2106.05664, 2021.
[50] P. Mishra, H. Yannakoudakis, and E. Shutova, “Tackling
online abuse: A survey of automated abuse detection meth-
ods,” arXiv preprint arXiv:1908.06024, 2019.
[51] Z. Waseem and D. Hovy, “Hateful symbols or hateful
people? predictive features for hate speech detection on
twitter,” in Proceedings of the NAACL student research
workshop, 2016, pp. 88–93.
[52] B. I. Davidson, D. Wischerath, D. Racek, D. A. Parry,
E. Godwin, J. Hinds, D. van der Linden, J. F. Roscoe,
L. Ayravainen, and A. G. Cork, “Platform-controlled so-
cial media apis threaten open science,” Nature Human
Behaviour, vol. 7, no. 12, pp. 2054–2057, 2023.
[53] M. Artetxe, S. Ruder, and D. Yogatama, “On the cross-
lingual transferability of monolingual representations,”
arXiv preprint arXiv:1910.11856, 2019.
[54] S. Doddapaneni, R. Aralikatte, G. Ramesh, S. Goyal, M. M.
Khapra, A. Kunchukuttan, and P. Kumar, “Towards leaving
no indic language behind: Building monolingual corpora,
benchmark and models for indic languages,” arXiv preprint
arXiv:2212.05409, 2022.
[55] Y.-H. Lin, C.-Y. Chen, J. Lee, Z. Li, Y. Zhang, M. Xia,
S. Rijhwani, J. He, Z. Zhang, X. Ma et al., “Choosing trans-
fer languages for cross-lingual learning,” arXiv preprint
arXiv:1905.12688, 2019.
[56] M. M’hamdi, X. Ren, and J. May, “Cross-lingual continual
learning,” in Proceedings of the 61st Annual Meeting of the

--- Page 8 ---

Association for Computational Linguistics (Volume 1: Long
Papers), 2023, pp. 3908–3943.
[57] F. Philippy, S. Guo, and S. Haddadan, “Towards a com-
mon understanding of contributing factors for cross-lingual
transfer in multilingual language models: A review,” arXiv
preprint arXiv:2305.16768, 2023.
[58] M. Choi, J. Pei, S. Kumar, C. Shu, and D. Jurgens, “Do llms
understand social knowledge? evaluating the sociability
of large language models with socket benchmark,” arXiv
preprint arXiv:2305.14938, 2023.
[59] L. Biester, V. Sharma, A. Kazemi, N. Deng, S. Wilson, and
R. Mihalcea, “Analyzing the effects of annotator gender
across nlp tasks,” in Proceedings of the 1st Workshop on
Perspectivist Approaches to NLP@ LREC2022, 2022, pp.
10–19.
[60] S. L. Blodgett, S. Barocas, H. Daum´e III, and H. Wallach,
“Language (technology) is power: A critical survey of”
bias” in nlp,” arXiv preprint arXiv:2005.14050, 2020.
[61] A. M. Davani, M. D´ıaz, and V. Prabhakaran, “Dealing
with disagreements: Looking beyond the majority vote in
subjective annotations,” Transactions of the Association for
Computational Linguistics, vol. 10, pp. 92–110, 2022.

```
