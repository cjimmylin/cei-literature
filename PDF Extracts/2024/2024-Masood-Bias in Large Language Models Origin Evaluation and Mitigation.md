---
title: "2024-Masood-Bias in Large Language Models Origin Evaluation and Mitigation - PDF Extract"
source_pdf: "2024-Masood-Bias in Large Language Models Origin Evaluation and Mitigation.pdf"
pages: 47
extracted_at: "2026-02-13T13:57:11.702018"
---

# PDF Extract: 2024-Masood-Bias in Large Language Models Origin Evaluation and Mitigation

**Source PDF:** 2024-Masood-Bias in Large Language Models Origin Evaluation and Mitigation.pdf
**Total Pages:** 47

---

## Content

```
--- Page 1 ---

arXiv:2411.10915v1  [cs.CL]  16 Nov 2024
∗
Bias in Large Language Models: Origin, Evaluation, and
Mitigation
Yufei Guo
guoyufei@gwu.edu
Muzhe Guo
muzheguo@gwu.edu
Juntao Su
sujuntao@gwu.edu
Zhou Yang
zhou_yang@gwu.edu
Mengqiu Zhu
mzhu32@gwu.edu
Department of Statistics, The George Washington University
Hongfei Li
hongfei.2.li@uconn.edu
Department of Statistics, University of Connecticut
Mengyang Qiu
mengyangqiu@trentu.ca
Department of Psychology, Trent University
Shuo Shuo Liu
shuoliu.academic@gmail.com
Department of Statistics, The Pennsylvania State University
Abstract
Large Language Models (LLMs) have revolutionized natural language processing, but their suscep-
tibility to biases poses signiﬁcant challenges. This comprehensive review examines the landscape
of bias in LLMs, from its origins to current mitigation strategies.
We categorize biases as in-
trinsic and extrinsic, analyzing their manifestations in various NLP tasks. The review critically
assesses a range of bias evaluation methods, including data-level, model-level, and output-level
approaches, providing researchers with a robust toolkit for bias detection. We further explore
mitigation strategies, categorizing them into pre-model, intra-model, and post-model techniques,
highlighting their eﬀectiveness and limitations. Ethical and legal implications of biased LLMs are
discussed, emphasizing potential harms in real-world applications such as healthcare and criminal
justice. By synthesizing current knowledge on bias in LLMs, this review contributes to the ongoing
eﬀort to develop fair and responsible AI systems. Our work serves as a comprehensive resource
for researchers and practitioners working towards understanding, evaluating, and mitigating bias
in LLMs, fostering the development of more equitable AI technologies.
1. Introduction
The rapid development of Large Language Models (LLMs) has transformed the ﬁeld of Natural Lan-
guage Processing (NLP), introducing new possibilities and applications across various domains, in-
cluding healthcare (Keskar et al., 2019), ﬁnance (Yang et al., 2020), education (Okonkwo and Ade-Ibijola,
2023), and entertainment (Jiang et al., 2020). These models, such as GPT-3 (Brown et al., 2020),
BERT (Devlin et al., 2018), and others, are designed to understand and generate human-like text
by learning from vast corpora of text data. These models have become the backbone for tasks such
as machine translation (Lewis et al., 2020), text summarization (Nallapati et al., 2016), sentiment
analysis (Zhang et al., 2018), and automated question-answering (Raﬀel et al., 2020), reﬂecting their
deep integration into various industries and day-to-day applications, and making them indispensable
tools in the modern AI landscape.
Despite their immense potential and utility, LLMs have raised concerns due to their inherent bi-
ases that reﬂect societal prejudices present in their training data (Bender et al., 2021; Blodgett et al.,
2020).
These biases, which manifest as gender, racial, cultural, and socio-economic stereotypes,
pose serious ethical and practical challenges, especially when LLMs are deployed in critical decision-
∗All authors contributed equally to this work.
1

--- Page 2 ---

making environments such as healthcare diagnostics (Rajkomar et al., 2018), legal judgments (Angwin et al.,
2016), and hiring processes (Chen et al., 2018). Such biases can lead to unequal treatment or skewed
results that disproportionately aﬀect marginalized groups, potentially exacerbating existing inequal-
ities. Caliskan et al. (2017) has noted that LLMs often mirror historical biases present in human
language, risking the ampliﬁcation of these biases within automated systems.
Understanding bias within LLMs requires insight into how biases traditionally arise in statis-
tical models. In classical statistics, biases are well-studied in models for continuous, binary, and
time-to-event endpoints Hastie et al. (2009). These biases manifest due to several issues, such as
selection bias Akaike (1974); Heckman (1979); Vardi (1982), overﬁtting Heckman (1979), handling
of covariates Akaike (1974); Tibshirani (1996) , limited sample sizes Nemes et al. (2009), and even
randomization ratio Hongfei Li and Hou (2024a,b), which can all lead to incorrect estimates and
predictions. These statistical biases share important parallels with those encountered in LLMs. For
instance, LLMs must handle incomplete or unbalanced datasets carefully to prevent skewed outputs.
Similarly, the challenges of selection bias in classical models echo the biases found in LLMs trained
on non-representative data sources, which can lead to harmful disparities in model predictions, espe-
cially for underrepresented groups. Addressing these statistical biases requires a range of mitigation
strategies, including robust causal inference framework Rubin (1974). Similarly, bias mitigation in
LLMs involves data-level interventions such as resampling and augmentation, model-level adjust-
ments with fairness constraints, and post-processing corrections to ﬁne-tune outputs (Schick et al.,
2021).
LLMs also exhibit biases similar to those observed in traditional statistical models.
Bias in
LLMs can be broadly categorized into two types: Intrinsic bias and Extrinsic bias. Intrinsic biases
originate from the training data, as well as the architecture and underlying assumptions made
during model design (Sun et al., 2019). LLMs, trained on vast datasets often sourced from internet
and textual repositories, inevitably inherit biases present in these sources. For example, language
models may reinforce gender stereotypes in occupations, associating “doctor” with men and “nurse”
with women (Bolukbasi et al., 2016; Zhao et al., 2018a).
Similarly, certain demographic groups
may be either underrepresented or misrepresented within training datasets, further compounding
model biases (Hovy and Prabhumoye, 2021). This becomes particularly problematic when LLMs are
applied in sensitive domains where accurate and unbiased information is crucial for decision-making
(Bender et al., 2021).
Extrinsic Biases, on the other hand, emerge during the application of LLMs in real-world tasks.
These biases are often more subtle as they manifest in the model outputs during speciﬁc tasks,
such as sentiment analysis, content moderation, or automated decision-making systems. For ex-
ample, Sap et al. (2019a) found that LLMs used in hate speech detection could disproportion-
ately ﬂag certain dialects or vernaculars, such as African American Vernacular English (AAVE),
as more oﬀensive compared to standardized English, reinforcing societal stereotypes.
Similarly,
Kiritchenko and Mohammad (2018) demonstrated that sentiment analysis systems could produce
biased results when analyzing texts associated with diﬀerent demographic groups, thereby perpetu-
ating harmful stereotypes in their predictions.
The implications of biases in LLMs are far-reaching. In healthcare, for instance, biased mod-
els can lead to inappropriate treatment recommendations, potentially worsening existing health
inequalities between demographic groups (Obermeyer et al., 2019). In legal settings, reliance on
biased language models for risk assessment or sentencing decisions can result in discriminatory
practices (Angwin et al., 2016). Moreover, biases embedded in LLMs aﬀect everyday applications,
such as search engines and social media platforms, where they shape public discourse, potentially
reinforcing echo chambers and marginalizing minority voices (Pariser, 2011; Sap et al., 2019b).
These biases not only perpetuate inequality but also raise signiﬁcant ethical and legal ques-
tions regarding the use of LLMs in decision-making processes. Given the critical nature of these
challenges, there is an urgent need for comprehensive evaluation frameworks to detect, quantify,
and mitigate these biases, ensuring that LLMs function as fair and equitable tools for all users.
2

--- Page 3 ---

Sheng et al. (2021) provide an overview of these eﬀorts, noting that bias evaluation typically in-
volves analyzing models at various stages of their lifecycle—from data preprocessing to model train-
ing and output generation. Common techniques include the use of benchmark datasets designed to
highlight biases (Nadeem et al., 2021), probing models to understand their internal representations
(Hewitt and Manning, 2019), and conducting user studies to assess the real-world impact of biased
outputs (Sap et al., 2019b).
In terms of bias mitigation, strategies are typically categorized into three broad approaches:
data-level interventions, model-level techniques, and post-processing adjustments. Data-level inter-
ventions involve curating and balancing the training datasets to reduce the prevalence of biased
content, often through data augmentation, ﬁltering, or resampling techniques (Zhao et al., 2018b).
However, this approach is limited by the vast scale and inherent diversity of LLM training datasets,
making it diﬃcult to eliminate biases entirely.
Model-level techniques may include altering the
training objectives, incorporating fairness constraints, or modifying model architectures to minimize
biased learning (Liang et al., 2020b). These methods often trade oﬀsome degree of model accu-
racy for fairness, presenting challenges in real-world deployment. Post-processing methods focus on
adjusting the outputs of LLMs after generation, applying debiasing algorithms, controlled text gen-
eration, or reinforcement learning frameworks to reduce biased content (Schick et al., 2021). While
this approach oﬀers ﬂexibility, it may require substantial computational overhead and may not fully
address the root causes of bias.
Despite these advancements, fully addressing bias in LLMs remains a complex and ongoing chal-
lenge. The complexity of language, the vastness of training datasets, and the massive architectures
of modern LLMs–often comprising billions of parameters–make it diﬃcult to identify and correct all
instances of bias. Furthermore, as Mehrabi et al. (2021) suggest, biases are often context-dependent
and may evolve over time as societal norms and values change. This dynamic nature of bias necessi-
tates continuous monitoring, evaluation, and reﬁnement of both models and the methodologies used
to assess their outputs.
This article aims to provide a comprehensive exploration of bias in LLMs, examining its origins,
manifestations, and the current state of research in bias evaluation and mitigation. We begin by
discussing the sources and types of biases, drawing on examples from various NLP tasks to illus-
trate how biases arise and persist. We then review the methodologies used to detect and measure
biases, including both quantitative and qualitative approaches. Following this, we explore the strate-
gies developed to mitigate biases at diﬀerent stages of the model development pipeline, assessing
their eﬀectiveness and limitations. Finally, we discuss the ethical considerations and legal implica-
tions of deploying biased AI systems, underscoring the importance of fairness, transparency, and
accountability in AI development. Through this discussion, we seek to contribute to the broader
discourse on responsible AI, oﬀering insights and recommendations for researchers, practitioners,
and policymakers working to ensure that LLMs serve as equitable and trustworthy tools in society.
2. Intrinsic Bias
The bias presented in Large Language Models (LLMs) can be broadly categorized into intrinsic bias
and extrinsic bias based on the diﬀerent stages at which the biases manifest within the model’s
lifecycle and the type of bias being measured (Doan et al., 2024). Intrinsic bias refers to biases that
are inherently within the internal representations or outputs of a trained or pre-trained LLM and
are independent of any speciﬁc downstream tasks. Extrinsic bias refers to the biases that manifest
during the model’s performance on speciﬁc downstream tasks after training or ﬁne-turing. Intrinsic
biases are typically encoded during the training or pre-training phase when the LLM learns from
large-scale corpora. For instance, if a pre-trained LLM consistently associates certain professions
with speciﬁc genders (e.g., assuming all doctors to be male and assuming all nurses to be female) or
racial stereotypes (May et al., 2019), this bias would be considered intrinsic bias. This type of bias
is tied to the way the model has encoded relationships and patterns in its internal representations.
3

--- Page 4 ---

In this section, we introduce the possible sources of intrinsic bias, present the manifestations of
intrinsic bias, and show available measurement and detection of Intrinsic bias.
2.1 Sources of Intrinsic Bias
Intrinsic biases are primarily introduced during the training/pre-training stages where models learn
patterns and representations from vast corpora. These biases can be traced to several aspects of
data and model design, which will be outlined below.
2.1.1 Bias in training Data
Language models, especially LLMs that are trained on large corpus, usually have intrinsic bias issues,
since the training corpora often contains societal biases that are built into the model (Pagano et al.,
2023; Ray, 2023; Goldfarb-Tarrant, 2024; Goldman and Tsotsos, 2024). These biases are present in
several ways shown as follows.
• Bias from over-representativeness and under-representativeness: Certain groups, such as gen-
der, age, race, religion, ethnicity, culture, political, or socioeconomic classes, may be under-
represented or over-represented in the corpus (Das et al., 2024; Alvero et al., 2024). For ex-
ample, men might be over-represented in datasets about leadership or science, while women
may be more frequently mentioned in caregiving roles (into Bias, 2024), thus leading to bi-
ased associations with demographic information. Another example is that the Latinx popula-
tion, especially Mexican-American students, remains underrepresented in U.S. higher educa-
tion (Alvero et al., 2024).
• Spatial and Temporal Bias: LLMs trained predominantly on the corpus from certain countries
or geographic locations may absorb the cultural norms and values, hence building biases into
the underlying LLMs.
For instance, a model trained on Western-centric data may have a
skewed understanding of non-Western cultures (Ahmad and Bhattacharyya; Talat et al., 2022;
Mukherjee et al., 2024; Lee et al., 2024; Shi et al., 2024). Similarly, data collected over dif-
ferent periods may reﬂect outdated societal norms and values. LLMs trained on these data
may be biased by those outdated norms and values. For instance, historical texts may exhibit
racist or sexist terminology, which the model may absorb as part of its internal representa-
tions (Salinas et al., 2023; Bussaja, 2024).
2.1.2 Bias in Data Collection Methods
The intrinsic biases can also stem from the methods that are used to collect the training corpus.
A large training corpus of LLMs often comprises of sub-datasets that are collected from diﬀerent
sources, including web scraping, social media and forums, books and literature, code repositories,
scientiﬁc and academic papers, legal and ﬁnance documents, dialogue and transcriptions, govern-
ment and public records, custom and proprietary database, and model-generated datasets. These
diﬀerent types of sources have their own biases. For instance, internet-based datasets can include
unmoderated, biased, or hateful content. Academic papers tend to be more neutral, but they often
lack the diversity of language found in social media or everyday conversations (Gallegos et al., 2024;
KUNTZ and SILVA, 2023; Qu and Wang, 2024). Choosing which texts to include or exclude during
the data collection phase can also lead to biases (Navigli et al., 2023). For instance, excluding certain
groups or viewpoints, intentionally or unintentionally, can introduce selection bias, which can skew
the model’s outputs toward the dominant narrative in the training data. Even with careful curation
by LLM creators, biases can still be embedded in the model’s learning, as it is nearly impossible to
fully eliminate inappropriate content given the vast scale of the training corpus.
4

--- Page 5 ---

2.1.3 Bias in Language Contexts
Biases can also stem from the context of language. Human languages often contain ambiguities
(including lexical ambiguity, syntax ambiguity, semantic ambiguity, and context-dependent meaning)
due to the ﬂexible nature of words, syntax, and context, which can lead to model biases.
For
example, gender-neutral pronouns may associated with one gender due to the patterns in the training
dataset (Kotek et al., 2023; Dwivedi et al., 2023). Certain linguistic constructions, such as ﬁgures
of speech and rhetoric, add another layer of complexity and ambiguity to human language by using
words and expressions in non-literal or persuasive ways and hence introduce biases (de Sá et al.,
2024).
3. Extrinsic Bias
Extrinsic bias refers to disparities in a model’s performance across diﬀerent downstream tasks, also
known as downstream bias or prediction bias (Doan et al., 2024; Gallegos et al., 2024; Li et al., 2023).
This type of bias emerges when a model’s eﬀectiveness varies among tasks or demographic groups,
potentially leading to unequal outcomes in practical applications.
Depending on the downstream tasks, extrinsic bias manifests diﬀerently. We categorize these
tasks into two main groups: natural language understanding (NLU) tasks and natural language
generation (NLG) tasks.
In NLU tasks, extrinsic bias aﬀects how the model comprehends and
interprets input text.
In NLG tasks, it can result in the generation of biased or stereotypical
language.
3.1 Natural Language Understanding (NLU) Tasks
NLU tasks aim to improve a model’s comprehension of input sequences beyond the literal meaning
of words (Chang et al., 2024). Extrinsic bias in these tasks can cause the model to misinterpret or
unfairly process input text based on biased associations learned during training.
Common manifestations of bias in NLU tasks include:
• Gender Bias: Models may incorrectly associate certain professions or roles with a speciﬁc
gender, leading to errors in tasks like coreference resolution (Zhao et al., 2018a). For example,
assuming a doctor is male and a nurse is female, regardless of context.
• Age Bias:
Models might make assumptions about individuals based on age stereotypes
(Caliskan et al., 2017). For instance, associating technological proﬁciency only with younger
people.
• Cultural or Regional Bias: Models could misinterpret idioms or expressions from diﬀerent
cultures or fail to recognize regional language variants (Vulic and Moens, 2013). This can result
in misunderstandings in tasks like semantic textual similarity or natural language inference.
These biases can lead to unfair or inaccurate outcomes in various NLU tasks, such as coreference
resolution, semantic textual similarity, natural language inference, classiﬁcation, reading comprehen-
sion, and sentiment analysis. Recurrent issues include reinforcing stereotypes, misclassifying text
due to dialects or language variants, and making incorrect inferences based on biased associations.
3.2 Natural Language Generation (NLG) Tasks
NLG tasks involve generating coherent and contextually relevant text based on input or instructions
(Chang et al., 2024). Extrinsic bias in these tasks can cause models to produce biased language or
reinforce stereotypes in generated text
Common manifestations of bias in NLG tasks include:
5

--- Page 6 ---

• Gender Bias: Models might generate responses that align with gender stereotypes, such as
using male pronouns for leaders and female pronouns for nurturing roles (Zhao et al., 2018a).
• Age Bias: Models may produce content that reﬂects age-related stereotypes, like suggesting
only sedentary activities for older adults (Caliskan et al., 2017).
• Cultural or Regional Bias: Models could favor content from dominant cultures or misrep-
resent cultural practices, leading to inappropriate or insensitive responses (Hendricks et al.,
2018).
These biases aﬀect tasks like question answering, sentence completion, conversational agents,
recommender systems, machine translation, and summarization. Recurrent issues include reinforcing
harmful stereotypes, underrepresenting minority cultures, and providing biased recommendations or
translations.
In general, extrinsic biases in LLMs impact both understanding and generation tasks, leading
to unfair or discriminatory outcomes. Addressing these biases is essential to ensure models perform
fairly and accurately in real-world applications. An overview of these biases in NLU tasks is provided
in Table 1, and in NLG tasks in Table 2. Detailed examples can be found in Appendix A.
6

--- Page 7 ---

Table 1: Overview of extrinsic biases in natural language understanding (NLU) tasks.
NLU Task
Gender Bias
Age Bias
Cultural or Regional Bias
Coreference
Resolution
Identifying instances
where diﬀerent expressions
refer to the same entity
(Lee et al., 2017)
1) Stereotypical Occupation
Associations: Mislinking
pronouns based on gender
stereotypes in professions, e.g.,
assuming doctors are male
(Zhao et al., 2018a)
2) Gendered Pronoun
Resolution: Incorrectly
resolving pronouns for
gender-neutral names, reﬂecting
gender biases (Rudinger et al.,
2018)
1) Assumptions About
Technological Proﬁciency:
Attributing technological skill to
certain ages when resolving
pronouns (Hovy and Yang,
2021)
2) Bias in Linking Pronouns
to Age-Related Roles:
Misassigning actions to younger
or older individuals based on
stereotypes (Garg et al., 2018)
1) Regional Variants and
Pronoun Use: Diﬃculty with
pronoun resolution in pro-drop
languages due to training on
non-pro-drop data
(Hovy and Yang, 2021)
2) Cultural Context in
Family Roles: Misresolving
pronouns based on cultural
stereotypes about family
responsibilities (Rudinger et al.,
2018)
Semantic Textual
Similarity
Evaluating how similar
the meanings of two texts
are (Cer et al., 2017)
1) Gendered Language and
Pronoun Resolution: Lower
similarity scores for sentences
diﬀering only by gendered
pronouns (Zhao et al., 2017)
2) Gender-Stereotyped
Professions: Overestimating
similarity when sentences align
with gender stereotypes
(Bolukbasi et al., 2016)
1) Age-Based Expectations
in Language Use: Bias in
similarity assessments due to
age-related stereotypes
(Caliskan et al., 2017)
2) Age Stereotypes in
Sentiment and Perception:
Overestimating similarity based
on stereotypes about age and
wisdom (Diaz et al., 2016)
1) Cultural Idioms and
Expressions: Underestimating
similarity between culturally
equivalent idioms
(Vulic and Moens, 2013)
2) Regional Dialects and
Variants: Misjudging similarity
due to diﬀerences in regional
vocabulary (Tan and Bond,
2011)
Natural Language
Inference
Determining the
relationship between a
premise and a hypothesis
(Bowman et al., 2015)
1) Stereotypical Gender
Roles in Professions:
Incorrect inferences based on
gender stereotypes in job roles
(Rudinger et al., 2018)
2) Gendered Language and
Assumptions: Bias in
inference due to gender
assumptions with neutral names
(Zhao et al., 2017)
1) Bias Toward Younger
Individuals in Dynamic
Roles: Overemphasizing youth
in roles like entrepreneurship
(Caliskan et al., 2017)
2) Age-Related Stereotypes
in Professional Contexts:
Assuming leadership roles are
held by older individuals
(Zhao et al., 2018a)
1) Cultural Norms and
Social Roles: Inferences
inﬂuenced by cultural
stereotypes about professions
(Rudinger et al., 2018)
2) Regional Political and
Historical Contexts:
Diﬃculty with inferences
requiring diverse historical
knowledge (Chen et al., 2016)
Classiﬁcation
Assigning categories or
labels to input text
(De-Arteaga et al., 2019;
Meng et al., 2020)
1) Gendered Language in
Job Title Classiﬁcation:
Associating certain professions
with speciﬁc genders
(Bolukbasi et al., 2016)
2) Gendered Pronouns and
Name Classiﬁcation:
Misclassifying names or
pronouns based on gender
stereotypes (Zhao et al., 2017)
1) Sentiment Classiﬁcation
Bias Based on Age:
Misclassifying sentiment due to
age-related stereotypes
(Díaz et al., 2018)
2) Bias in Job Application
Classiﬁcation: Discriminating
against older applicants in job
screening (De-Arteaga et al.,
2019)
1) Misclassiﬁcation Due to
Cultural Language Variants:
Incorrectly classifying
non-standard dialects as
negative (Sap et al., 2019a)
2) Regional Bias in Political
Text Classiﬁcation: Bias
toward dominant regional
political ideologies
(Bender et al., 2021)
Reading
Comprehension
Answering questions based
on a given text
(Rajpurkar et al., 2018)
1) Stereotypes in Gendered
Activities: Assuming gender
based on activities, e.g., cooking
linked to females
(Webster et al., 2018)
2) Assumptions About
Gender Roles in Family
Settings: Inferring roles based
on traditional gender norms
(Caliskan et al., 2017)
1) Bias in Health-Related
Content: Associating certain
health issues with age
stereotypes (Bolukbasi et al.,
2016)
2) Misinterpretation of
Age-Related Roles:
Incorrectly assuming roles based
on age (Bender and Friedman,
2018)
1) Cultural Context
Misinterpretation:
Misunderstanding culturally
speciﬁc practices in texts
(Bender and Friedman, 2018)
2) Regional Language
Varieties and Dialects:
Struggling with comprehension
of non-standard dialects
(Blodgett et al., 2020)
Sentiment Analysis
Identifying the emotional
tone in text (Pang et al.,
2008)
1) Bias in Sentiment
Toward Gendered Products
or Topics: Skewed sentiment
analysis for gender-speciﬁc
items (Zhao et al., 2017)
2) Sentiment Analysis in
Gendered Contexts:
Misclassifying sentiment in
discussions challenging gender
norms (Misiunas and Keyser,
2019)
1) Sentiment Analysis on
Age-Related Topics:
Assuming negative sentiment in
texts by older individuals
(Burnap and Williams, 2015)
2) Stereotyping Language
Use by Older Adults:
Misinterpreting sentiment due
to age-related language
stereotypes (Hovy and Søgaard,
2015)
1) Cultural Bias in
Sentiment Toward Social
Norms: Misclassifying
sentiment across diﬀerent
cultural norms
(Blodgett and O’Connor, 2017)
2) Sentiment in
Multilingual Contexts:
Incorrect sentiment assessment
in code-switching texts
(Hovy and Søgaard, 2015)
7

--- Page 8 ---

Table 2: Overview of extrinsic biases in natural language generation (NLG) tasks.
NLG Task
Gender Bias
Age Bias
Cultural or Regional Bias
Question
Answering
Providing accurate
answers based on a given
text or knowledge base
(Rajpurkar et al., 2016)
1) Gender Bias in Answer
Generation: When asked,
“What should a good leader
do?”, the model might use
stereotypically male attributes,
implying leadership qualities are
inherently male (Zhao et al.,
2018a)
2) Bias in Answering
Ambiguous Gender
Questions: For questions
without speciﬁed gender, the
model might default to male
pronouns, reinforcing gender
assumptions (Webster et al.,
2018)
1) Stereotypical Answers
About Aging: When asked
about activities for elderly
people, the model might focus
on sedentary activities,
neglecting active pursuits
(Caliskan et al., 2017)
2) Negative Bias Toward
Youth: Suggesting that young
people lack experience for roles
like managing a company
(Bolukbasi et al., 2016)
1) Bias in Answering
Culturally Speciﬁc
Questions: Providing answers
based on regional popularity
rather than global knowledge,
e.g., stating “American football”
as the most popular sport
(Gardner et al., 2018)
2) Language and Regional
Bias in Answer Accuracy:
Better performance on questions
related to well-represented
regions and languages
(Kwiatkowski et al., 2019)
Sentence
Completion
Predicting and generating
the next word or sequence
to complete a sentence
(Radford et al., 2019)
1) Gender Bias in
Descriptions of Physical
Appearance: Completing
sentences in ways that reinforce
stereotypes about women’s and
men’s concerns (Caliskan et al.,
2017)
2) Gender Bias in Personal
Attributes: Associating
women with “emotional” and
men with “strong” in sentence
completions (Zhao et al., 2017)
1) Activity and Lifestyle
Assumptions: Completing
sentences with stereotypical
activities based on age
(Garg et al., 2018)
2) Learning and Education
Stereotypes: Assuming older
adults are “catching up” on
education (Sun et al., 2019)
1) Cultural Stereotyping in
Sentence Completion:
Overemphasizing speciﬁc
aspects of a culture, e.g., “In
Japan, people often eat sushi”
(Hendricks et al., 2018)
2) Regional Bias in
Place-Based Completions:
Reinforcing stereotypes about
regions, e.g., “In Africa, many
people live in villages”
(Birhane and Prabhu, 2021)
Conversational
Generating coherent
dialogue and maintaining
conversation context
(Zhang et al., 2019b)
1) Stereotypical Responses
Based on Gendered
Prompts: Reinforcing gender
stereotypes in descriptions, e.g.,
nurses as female and caring
(Bolukbasi et al., 2016)
2) Bias in Gendered
Interactions: Responding
diﬀerently based on assumed
user gender (Hitsch et al., 2010)
1) Assumptions About
Technological Savvy:
Assuming tech-savvy users are
younger and providing simplistic
explanations to older users
(Hovy and Søgaard, 2015)
2) Bias in Addressing
Age-related Concerns:
Discouraging older individuals
from pursuing new careers
(Wagner et al., 2016)
1) Culturally Inappropriate
Responses: Failing to
understand cultural norms in
responses (Hovy and Spruit,
2016)
2) Bias in Handling
Regional Topics: Focusing on
negative topics for certain
regions (Gebru et al., 2021)
Recommender
Systems
Suggesting personalized
content or items based on
user data (Zhang et al.,
2019a)
1) Product
Recommendations Based on
Gender Stereotypes:
Suggesting products reinforcing
traditional gender roles
(Ekstrand et al., 2018)
2) Career and Education
Recommendations:
Suggesting STEM careers more
to men and arts to women
(Chen et al., 2019)
1) Age-Related Product
Recommendations:
Recommending products based
on age stereotypes (Biega et al.,
2018)
2) Media and
Entertainment
Recommendations: Assuming
preferences based on age,
limiting content diversity
(Burke et al., 2018)
1) Regional Bias in News
and Information
Recommendations:
Under-representing news from
minority regions (Karimi et al.,
2018)
2) Bias in Language and
Cultural Content
Recommendations:
Prioritizing content in dominant
languages (Lakew et al., 2018)
Machine
Translation
Translating text from one
language to another
(Vaswani, 2017)
1) Gendered Language
Mismatch: Introducing gender
bias when translating from
gender-neutral to gendered
languages (Prates et al., 2020)
2) Gender Stereotyping in
Occupational Translations:
Assigning gendered pronouns
based on stereotypes
(Neri et al., 2020)
1) Bias in Addressing Older
Adults: Translations that
condescend to older adults
(Caliskan et al., 2017)
2) Translation of
Age-Related Idioms:
Reinforcing negative stereotypes
in translations
(Hovy and Søgaard, 2015)
1) Cultural Nuance Loss:
Mistranslating idioms and
expressions without cultural
context (Vanmassenhove et al.,
2019)
2) Bias Toward Dominant
Cultures: Favoring
translations aligning with
Western norms (Sennrich, 2016)
Summarization
Generating concise
summaries of longer texts
(Nallapati et al., 2016)
1) Diﬀerential Emphasis on
Roles: Emphasizing traditional
gender roles in summaries
(Bender and Friedman, 2018)
2) Selective Emphasis on
Gendered Information:
Overemphasizing gender-speciﬁc
details not central to the story
(Otterbacher et al., 2017)
1) Bias in Summarizing
Content for Diﬀerent Age
Groups: Simplifying content in
a condescending way
(Obermeyer et al., 2019)
2) Omission of
Contributions Based on
Age: Highlighting contributions
of younger people over older
individuals
(Bender and Friedman, 2018)
1) Omission of Culturally
Signiﬁcant Details: Omitting
culturally important
information in summaries
(Shen et al., 2017)
2) Bias Toward Western
Narratives: Prioritizing
Western perspectives in global
news summaries
(Perez-Beltrachini and Lapata,
2022)
8

--- Page 9 ---

4. Bias Evaluation
As LLMs become increasingly integrated into various real-world applications, from healthcare decision-
making to legal judgments and everyday digital interactions, their potential to propagate biases has
raised signiﬁcant ethical and societal concerns Liang et al. (2021). These biases, deeply rooted in
the data, model architecture, and even in post-processing steps, can lead to discriminatory out-
comes against marginalized groups, amplifying existing inequalities Gallegos et al. (2024). There-
fore, understanding and evaluating these biases are crucial steps in ensuring the fair and responsible
deployment of LLMs.
This section focuses on the classiﬁcation and evaluation of biases in LLMs, providing a compre-
hensive overview of the methods used to identify and assess biases at diﬀerent stages of the model
lifecycle Gallegos et al. (2024). We categorize bias evaluation methods into data-level, model-level,
output-level, human-involved, and domain-speciﬁc approaches, each addressing distinct sources and
manifestations of bias Doan et al. (2024). By systematically exploring these methods, we aim to
equip researchers and practitioners with the tools necessary to detect and mitigate biases, ulti-
mately enhancing the fairness and trustworthiness of LLMs in diverse applications Gallegos et al.
(2024).
Drawing on recent advancements in the ﬁeld, we highlight key techniques such as demographic
distribution analysis, fairness metrics, interpretability tools, and counterfactual fairness, among
others Doan et al. (2024); Liang et al. (2021). Additionally, we discuss the role of human judgment
and domain-speciﬁc evaluations in capturing context-dependent biases that automated methods may
overlook Gallegos et al. (2024). Through this exploration, we underscore the importance of a multi-
faceted approach to bias evaluation, one that combines technical rigor with contextual awareness to
address the complex challenges of fairness in LLMs Gallegos et al. (2024).
4.1 Data-Level Bias Evaluation Methods
Data-level bias evaluation methods focus on identifying and quantifying biases inherent in the train-
ing data of LLMs. These biases, rooted in the data, can signiﬁcantly impact model outputs and
exacerbate societal stereotypes.
• Data Distribution Analysis: Data distribution analysis is a critical step in identifying and
understanding bias at the data level, as it provides insights into how diﬀerent demographic
groups or categories are represented in the dataset used to train LLMs. The primary focus of
this analysis is to ensure that the data is balanced and representative, minimizing the risk of
perpetuating or amplifying existing biases in the trained model.
– Representation Across Demographics: Research has consistently demonstrated that
the representation of demographics in training data can signiﬁcantly inﬂuence the out-
comes of LLMs. For instance, LLMs trained on datasets with disproportionate repre-
sentation of certain demographic groups are prone to exhibit biases that favor those
groups Simmons and Hare (2023); Wang et al. (2024a); Gorti et al. (2024). For example,
an analysis of political biases in LLMs revealed that most conversational LLMs exhibit
left-of-center political preferences when probed with politically charged questions or state-
ments Rozado (2024). The study demonstrated that LLMs can be steered towards speciﬁc
political orientations through Supervised Fine-Tuning (SFT) with modest amounts of po-
litically aligned data.
To assess representation, statistical tools can be employed to measure the distribution
of demographic attributes within the dataset. Key metrics might include the relative
frequency of each demographic group or the variance in representation across diﬀerent
categories.
Visual tools such as histograms, bar charts, or demographic distribution
9

--- Page 10 ---

tables can be useful for identifying disparities, providing a clear picture of which groups
are overrepresented or underrepresented in the data.
– Imbalance and Skewness Detection: Imbalance and skewness in data distribution
can lead to biased model behavior, where the model is overly inﬂuenced by the majority
class or demographic group. Detecting these issues is crucial for ensuring that the model
performs fairly across all segments of the population.
Imbalances occur when certain classes or demographic groups are signiﬁcantly more preva-
lent in the dataset than others. This can result in the model being biased towards the
majority group, leading to poor performance for minority groups. Techniques such as
Gini coeﬃcients Khanuja et al. (2022), entropy measures Csáky et al. (2019), vocabu-
lary usage Durward and Thomson (2024), and frequency analysis can be used to quan-
tify imbalance. Skewness can be visualized using skew and stereotype quantifying met-
rics de Vassimon Manela et al. (2021); Dang and Verma (2024) box plots, histograms, or
cumulative distribution functions (CDFs). These tools help identify the extent of skewness
in the data and guide the selection of appropriate mitigation strategies.
– Data Sources Analysis: The quality and bias of a model are heavily inﬂuenced by the
sources of the data used for training. Biases inherent in the data sources can signiﬁcantly
impact the model’s behavior. For instance, if a model is trained primarily on data from
Western countries, it may perform poorly when applied in non-Western contexts.
Evaluating the bias of data sources for LLM training involves analyzing the origins, diver-
sity, and quality of the data, as well as its impact on model performance. This includes
cataloging the data sources to ensure they cover a wide range of geographical, cultural,
and linguistic contexts, and examining the credibility and inherent biases of each source.
For instance, research Shen et al. (2023) on the SlimPajama dataset, which includes a
rigorously deduplicated combination of web text, Wikipedia, GitHub, and books, reveals
how diﬀerent data combinations aﬀect LLM performance. The SlimPajama-DC study
highlights two key aspects: the impact of global versus local deduplication on model
performance and the importance of data diversity post-deduplication. Findings indicate
that models trained with highly-deduplicated, diverse datasets outperform those trained
on less reﬁned data, underscoring the signiﬁcance of comprehensive and balanced data
sources. Bias detection tools and adjustments in data weighting can further help in man-
aging these biases, supported by transparent documentation and regular reviews to ensure
fairness and accuracy in the model outputs.
• Stereotype and Bias Detection in Text Data: Stereotype and bias detection involves
analyzing the content of the training data to identify and quantify biases related to stereotypes,
oﬀensive language, or prejudiced statements. This can be done through:
– Lexical Analysis: This method focuses on identifying speciﬁc words or phrases within
the training data that are associated with bias or stereotypes. Lexical analysis relies on
pre-deﬁned lexicons, which are curated lists of terms known to carry biased or stereo-
typical connotations. Tools like Hatebase, an extensive repository of hate speech terms,
provide a valuable resource for identifying harmful language in text data. Hate speech can
also be measured by large scale study Silva et al. (2016). BiCapsHate Kamal et al. (2023)
is deep learning model to detect hate speech in online social media posts. Similarly, the
Dictionary of Aﬀect in Language (DAL) Whissell (1989) categorizes words based on their
emotional connotations, oﬀering insights into how language can perpetuate stereotypes.
By scanning the training data for occurrences of these terms, researchers can quantify the
prevalence of biased language and identify speciﬁc areas where the data may reinforce
harmful stereotypes. For example, a study by Dev et al. (2021) demonstrated how biased
10

--- Page 11 ---

language in training data could lead to the propagation of racial and gender stereotypes
in NLP models .
– Contextual Analysis: While lexical analysis identiﬁes the presence of speciﬁc biased
terms, contextual analysis delves deeper into how these terms are used within the text.
This method employs advanced NLP techniques to examine the context in which poten-
tially biased language appears, allowing for the identiﬁcation of subtler forms of bias. For
instance, the same word might be used neutrally in one context but carry a prejudiced
meaning in another.
Contextual analysis examines sentence structure, co-occurrence
patterns, and the surrounding language to uncover these nuances.
Studies like those
by Bolukbasi et al. (2016) have shown that even when biased language is not overtly
present, underlying patterns can still perpetuate stereotypes, such as gender biases in
word embeddings . This approach is crucial for identifying and mitigating biases that
may not be immediately apparent but can signiﬁcantly impact the behavior of LLMs.
Zhao et al. (2019) quantiﬁed and analyzed gender bias exhibited in ELMo’s contextu-
alized word vectors. contextual analysis can be implemented by methods like template-
based method Kurita et al. (2019), applied thematic analysis Mackieson et al. (2019), and
contextualized word embeddings analysis Basta et al. (2019).
– Sentiment Analysis: Sentiment analysis is another vital tool in detecting bias in text
data. This technique assesses the sentiment—positive, negative, or neutral—associated
with diﬀerent demographic groups or topics within the training data.
By analyzing
how diﬀerent groups are described, researchers can identify patterns of negative or bi-
ased portrayals that could inﬂuence the model’s outputs. For example, if certain demo-
graphic groups are consistently associated with negative emotions or connotations, the
model might learn to replicate these biases in its predictions or interactions. Research
by Kiritchenko and Mohammad (2018) has highlighted how sentiment analysis can be
used to detect and address such biases in text data . This method provides a quantitative
measure of bias, enabling targeted interventions to reduce the impact of these biases on
the model’s behavior. Sentiment analysis can be implemented by lots of traditional ma-
chine learning tools Wankhade et al. (2022); Saxena et al. (2022); Hasan et al. (2019), pre-
processed data framework Hasan et al. (2019) or transformer-based methods Devlin et al.
(2018); Naseem et al. (2020); Abdullah and Ahmet (2022).
• Annotation Bias Analysis: Annotation Bias Analysis is a crucial component in evaluating
and mitigating bias in LLMs. This process involves examining the biases introduced during
the data annotation phase, where human annotators label or categorize training data. Since
annotators bring their own biases and perspectives, their subjective decisions can inadvertently
introduce skewed or biased annotations, which in turn aﬀect the performance and fairness of
the LLMs. To perform annotation bias analysis, researchers must review the annotation guide-
lines and the training process for annotators, ensuring that they are designed to minimize
bias. Additionally, evaluating the consistency and fairness of annotations across diﬀerent de-
mographic groups and annotators helps identify any disparities. Tools such as inter-annotator
agreement metrics Artstein (2017) and statistical analysis Paun et al. (2022) of annotated data
can reveal potential biases. For example, research by Havens et al. (2022) on gender bias in
annotated datasets highlights how annotation practices can reinforce stereotypes and biases,
emphasizing the need for rigorous analysis and correction methods. Another way to reduce
annotation bias is human-LLM collaborative approach Wang et al. (2024b). By addressing
annotation bias, researchers can enhance the quality and fairness of training data, leading to
more balanced and unbiased LLMs.
11

--- Page 12 ---

4.2 Model-Level Bias Evaluation Methods
Model-level bias evaluation methods assess biases that arise during the training and prediction stages
of LLMs, focusing on whether the model exhibits discriminatory behavior toward speciﬁc groups.
• Fairness Metrics: These metrics are pivotal in evaluating the model’s output fairness across
diﬀerent groups. Common metrics include:
– Equal Opportunity: Ensures that the True Positive Rate (TPR) is similar across
groups deﬁned by sensitive attributes such as gender or race. For example, a sentiment
analysis model should equally recognize positive sentiments across both male and female-
associated names Liang et al. (2021); Gallegos et al. (2024).
– Predictive Parity: Focuses on the consistency of prediction accuracy (Precision) across
groups.
This is particularly important in applications like credit scoring, where un-
equal predictive performance can lead to discriminatory outcomes against minority groups
Doan et al. (2024); Gallegos et al. (2024).
– Calibration: This metric checks whether predicted probabilities align with actual oc-
currences, particularly across diﬀerent demographic groups, ensuring that the model’s
conﬁdence in its predictions is justiﬁed Doan et al. (2024); Esiobu et al. (2023).
• Interpretability Tools: Tools such as SHAP (Shapley Additive Explanations) Mosca et al.
(2022) and LIME (Local Interpretable Model-agnostic Explanations) Wu et al. (2024) provide
insights into how speciﬁc features inﬂuence model predictions, helping identify biases. For
instance, SHAP values can reveal that gendered words heavily inﬂuence predictions, indicating
potential gender bias in the model Liang et al. (2021); Lin et al. (2024).
Similarly, LIME
approximates complex models locally with interpretable models to highlight the impact of
features on individual predictions, which is crucial for diagnosing bias Wu et al. (2024).
• Counterfactual Fairness: This method generates counterfactual examples by altering sen-
sitive attributes (e.g., changing names from traditionally male to female) to see if the model’s
outputs remain invariant. A fair model should ideally produce the same outcomes regardless
of these attribute changes Doan et al. (2024); Li et al. (2023).
4.3 Output-Level Bias Evaluation Methods
Output-level bias evaluation methods assess how LLMs generate responses, especially with regard
to fairness and neutrality across diﬀerent demographic groups.
These methods aim to identify
whether the model’s predictions, recommendations, or generated content reﬂect biases that may have
been learned during training, including those based on race, gender, socioeconomic status, political
orientation, and more. Here, we explore ﬁve major metrics used to detect bias in LLM-generated
text: Counterfactual Testing, Stereotype Detection, Sentiment and Toxicity Analysis, Acceptance
and Rejection Rates, and Embedding-Based Metrics.
• Counterfactual Testing: Counterfactual testing involves modifying input prompts by alter-
ing speciﬁc attributes, such as gender, race, or ethnicity, while keeping the rest of the context
unchanged. This method evaluates whether the LLM’s output varies based on these demo-
graphic changes, allowing researchers to isolate the eﬀect of these attributes on the model’s
behavior. For instance, swapping "John" with "Maria" in a sentence can reveal if the model
responds diﬀerently due to the gender of the subject.
Recent work Wang (2024) emphasizes the importance of robust causal reasoning in LLMs to
enhance fairness, arguing that a strong understanding of causal relationships can mitigate bi-
ases and reduce hallucinations. Another study Banerjee et al. (2024) introduces a dynamic
12

--- Page 13 ---

Table 3: Summary of Model-Level Bias Evaluation Methods
Method
Description
Fairness Metrics
Equal Opportunity: Ensures similar True Positive
Rates (TPR) across sensitive groups.
Predictive Parity: Checks for consistent predic-
tion accuracy across groups.
Calibration: Aligns predicted probabilities with ac-
tual outcomes for fairness.
Interpretability Tools
SHAP: Explains the impact of individual features
on model predictions.
LIME: Provides local approximations of complex
models for feature impact analysis.
Counterfactual Fairness
Scenario Testing: Alters sensitive attributes (e.g.,
gender) to test output consistency.
Equity Check: Veriﬁes that changes do not aﬀect
model outcomes unfairly.
framework that compares outputs across diﬀerent demographic groups in the same context,
improving the fairness of generated text without requiring costly model retraining. Addition-
ally, new tools Cheng et al. (2024) for generating and analyzing counterfactuals allow users
to explore LLM behavior interactively, ensuring the counterfactuals are both meaningful and
grammatically accurate.
These advancements underscore the power of counterfactual testing in identifying biases in
LLMs. By systematically altering demographic features in prompts, researchers can evaluate
how models treat diﬀerent groups and ensure equitable outputs across all demographics.
• Stereotype Detection in Generated Text: Stereotype detection in generated text focuses
on identifying and mitigating harmful biases that LLMs may perpetuate in their outputs. Since
LLMs are trained on vast amounts of publicly available data, which often contain stereotypical
narratives related to race, gender, profession, and religion, the risk of these biases appearing
in generated content is signiﬁcant. This method assesses how models reproduce stereotypes,
providing insights into implicit prejudices embedded in their responses.
One approach Wu et al. (2024) introduced a uniﬁed dataset combining multiple stereotype de-
tection datasets. Researchers ﬁne-tuned LLMs on this dataset and found that multi-dimensional
classiﬁers were more eﬀective in identifying stereotypes. This study also highlights the use of ex-
plainable AI tools to ensure models align with human understanding. Another study Bai et al.
(2024) developed a dual-framework that combines static evaluations with dynamic, real-world
scenario simulations. This dynamic aspect is particularly eﬀective in detecting subtle, context-
speciﬁc biases that static tests might miss. A qualitative method Babonnaud et al. (2024)
uses prompting techniques to uncover implicit stereotypes in LLM-generated text. This ap-
proach, focusing on biases like gender and ethnicity, employs the Tree of Thoughts technique
to systematically reveal hidden prejudices and provide a reproducible method for stereotype
detection.
These methods collectively help researchers detect and mitigate biases in LLM
outputs, oﬀering a deeper understanding of how stereotypes manifest in generated text.
13

--- Page 14 ---

• Sentiment and Toxicity Analysis: Sentiment and toxicity analysis is crucial for evaluating
output-level biases in LLMs, speciﬁcally targeting harmful or oﬀensive content and ensuring
adherence to ethical standards. This area of evaluation not only addresses toxicity but also
helps in identifying subtle biases that may emerge in generated content.
Llama Guard Inan et al. (2023) introduces a model-based approach to bias evaluation by using
a safety risk taxonomy for classifying both prompts and responses in human-AI conversations.
This model, ﬁne-tuned on a carefully curated dataset, shows strong performance in detect-
ing various forms of toxicity. It represents a practical application of bias evaluation methods
by providing a dynamic tool for assessing and mitigating harmful content in real-world in-
teractions.
The deﬁnition-based toxicity metric Koh et al. (2024) oﬀers a ﬂexible solution
for bias evaluation by using LLMs to measure toxicity according to predeﬁned criteria. This
method outperforms traditional metrics, enhancing the F1 score signiﬁcantly and addressing
the limitations of existing models that rely on dataset-speciﬁc deﬁnitions. It exempliﬁes how
bias evaluation methods can be reﬁned to improve the detection of nuanced toxic content.
Moderation Using LLM Introspection (MULI) Hu et al. (2024) advances bias evaluation by
analyzing internal model responses to detect toxic prompts. This approach leverages patterns
in response token logits and refusal behaviors, providing a cost-eﬀective way to assess biases
without requiring additional training.
The OpenAI Moderations Endpoint represents a practical implementation of bias evaluation
methods for ﬁltering potentially harmful content. This tool helps developers assess and moder-
ate LLM outputs, ensuring they align with safety and ethical guidelines. It demonstrates how
automated tools can be integrated into the bias evaluation process to manage and mitigate
risks associated with model-generated text.
• Acceptance and Rejection Rates: Evaluating acceptance and rejection rates in LLMs
is essential for identifying biases that may arise in decision-making tasks. Recent work has
explored how these biases manifest, particularly in contexts such as hiring decisions or moral
dilemmas, where the outputs of LLMs could reinforce existing societal inequalities.
In one study An et al. (2024), researchers assessed how LLMs respond to job applicants based
on perceived race, ethnicity, and gender by manipulating ﬁrst names. They found that ac-
ceptance rates were signiﬁcantly higher for masculine White names compared to masculine
Hispanic names. These acceptance and rejection rates were highly prompt-sensitive, meaning
that variations in how the question was framed could lead to diﬀerent outcomes. This suggests
that LLMs can subtly reinforce biases, depending on how inputs are structured. Another eval-
uation method Scherrer et al. (2024) used to study LLM behavior in moral decision-making
showed that models are consistent in choosing commonsense actions in unambiguous scenarios,
while in more ambiguous cases, LLMs exhibited uncertainty and greater variability. Closed-
source models often displayed more consistent preferences in these ambiguous scenarios, which
suggests that proprietary models might encode speciﬁc tendencies in moral decision-making.
BiasBuster Echterhoﬀet al. (2024) provides a systematic method for uncovering and evaluat-
ing cognitive biases in LLMs, particularly in high-stakes decision-making. By using a dataset
of 16,800 prompts designed to probe various types of biases (e.g., prompt-induced, sequential),
this framework allowed researchers to assess how LLMs handled acceptance and rejection de-
cisions under diﬀerent bias conditions.
4.4 Human-Involved Bias Evaluation Methods
Human-involved evaluation incorporates human judgment to identify complex and context-dependent
biases in LLM outputs.
• Human Review and Assessment: Experts or crowd-sourced reviewers manually assess
model outputs for biases. This method is particularly eﬀective in detecting nuanced biases that
14

--- Page 15 ---

automated tools might miss, such as subtle stereotypes or culturally speciﬁc biases Doan et al.
(2024).
• Qualitative Research Methods: Interviews, focus groups, and case studies oﬀer deep in-
sights into how diﬀerent communities perceive model outputs, providing a qualitative dimen-
sion to bias evaluation that complements quantitative approaches (Liang et al., 2021).
4.5 Conclusion
Bias evaluation is critical for the responsible use of LLMs.
By systematically categorizing and
applying various evaluation methods, researchers can better understand and mitigate the biases
that LLMs may propagate, thereby enhancing their fairness and societal impact.
5. Bias Mitigation
Biases are often present in unstructured data, and LLMs trained on such data can not only learn
these biases but sometimes amplify them as well (Bolukbasi et al., 2016; Sheng et al., 2019). Various
methods of bias mitigation exist under diﬀerent contexts, such as social bias (Garimella et al., 2021,
2022), political bias (Liu et al., 2022), and stereotype bias (Nie et al., 2024b). Instead of reviewing
these methods for bias mitigation by bias contexts, we categorize them by the timing of debiasing.
More speciﬁcally, methods for mitigating biases can be categorized into three distinct approaches: (1)
preprocessing the input data prior to training LLMs; (2) changing the model’s architecture and/or
picking the best model based on the predeﬁned bias evaluation metrics; (3) improving unbiasedness
by calibrating the outputs at the decision-making stage. We call these three approaches as pre-
model debiasing, intra-model debiasing, and post-model debiasing, respectively. Table 4 provides an
overview of the advantages and disadvantages on each approach.
Table 4: Overview of methods for bias mitigation.
Debiasing
Methods
Summary
Pre-model
Resampling; Data augmentation; Ex-
pert intervention
Time-saving without model training;
Time-consuming to annotate bias cases,
Ineﬀectiveness with a self-biased model,
Privacy issue of resampling
Intra-model
Equalization and declustering;
Move-
ment
pruning;
Transfer
learning;
Dropout regularization;
Causal infer-
ence
Flexibility in mitigating various types of
biases, Strong performance in empirical
studies; Time-consuming for modifying
and training models
Post-model
Reinforced
calibration;
Self-Debias;
Projection-based
methods;
Causal
prompting
Time-saving without model training;
Demand of a large amount of data
5.1 Pre-model debiasing
Pre-model debiasing approach involves preprocessing the input data before training LLMs so that
the entire training data are balanced and representative of the entire population. Typical ways of
balancing training data include oversampling, undersampling, and synthetic data generation (Ferrara,
2023). We review the commonly used pre-model debiasing methods below.
One of the widely used methods is counterfactual data augmentation (CDA), which is often
used to mitigate bias in the literature (Zmigrod et al., 2019; Webster et al., 2020; Barikeri et al.,
2021; Mondal and Lipizzi, 2024). Counterfactual Data Substitution (CDS), a variant of CDA, is
15

--- Page 16 ---

also proposed to randomly substitute potentially biased text to avoid duplication (Maudslay et al.,
2019). Generally speaking, CDA rebalances a corpus by sawpping bias attribute words in a dataset.
For example, we may swap the sentence
"The professor came to the classroom but he forgot to bring his laptop"
to
"The professor came to the classroom but she forgot to bring her laptop".
Meade et al. (2022) further empirically evaluates CDA for mitigating religious bias by swapping
religious terms.
Serouis and Sèdes (2024) proposes an iterative method that human can oversee the preprocessing
step. That is, before training begins, a dataset report is sent to a LLM. An expert then decides the
next step: either issuing a command to the LLM to create new training data or starting the training
process. The decision is made by measuring the quality of generated data. If a command is used
to generate alternative training data, iterative feedback between the expert and the LLM continues
until predeﬁned criteria are satisﬁed, leading to a decision to proceed with model training. After
training and experimentation, detailed results concerning protected groups are provided to the LLM
for summarization (particularly for multiple groups and subgroups) or directly to the expert. Based
on these comprehensive reports, the expert may choose to use the LLM to produce a revised dataset
version to mitigate potential biases.
5.2 Intra-mdoel debiasing
Intra-mdoel debiasing works by selecting the model that prioritizes unbiasedness and fairness dur-
ing the model ﬁtting. For example, Garimella et al. (2021) proposes a method to mitigate explicit
and implicit biases in BERT using existing and newly proposed loss functions. The proposed work
focuses on gender bias and includes a list of target-deﬁned word pairs and the text dataset as input.
It takes the pretrained BERT and further trains it on the given input, while mitigating the existing
social biases by equalizing and declustering. The equalizing stage aims to equalize the associations
of neutral words by deﬁning a equalizing loss (Qian et al., 2019). Observing that words are stereo-
typically associated to a group (e.g., delicate, pink, beautiful), authors develop a declustering stage
to decluster the implicit clusters by deﬁning a declustering loss. Similar technique is also applied to
mitigate social stereotypes when exposed to diﬀerent demographic groups (Garimella et al., 2022).
Moreover, Joniak and Aizawa (2022) presents an innovative framework for examining bias in pre-
trained transformer-based language models through movement pruning. It identiﬁes a subset of
the model that contains less bias than the original by pruning it while ﬁne-tuning on a debiasing
objective. It explores pruning attention heads, which are crucial components of transformers, by
pruning square blocks and introducing a novel method for pruning entire heads. An interesting bias-
performance trade-oﬀabout gender bias from this study is: the level of bias increases as model’s
performance improves.
Another line of works focuses on the technique of transfer learning (Zhuang et al., 2020; Azunre,
2021; Ge et al., 2024; Liu, 2024). Transfer learning leverages knowledge learned from a pre-trained
model to improve the performance of a new model on a relevant task but with fewer data points.
More speciﬁcally, it ﬁne-tunes a pre-trained model on the new task by updating the weights of neu-
rons or modifying the network architecture. For example, FairDistillation (Delobelle and Berendt,
2022), a cross-lingual method based on knowledge distillation, is used to build smaller language
models while managing speciﬁc biases. It leverages existing language models as a teacher, providing
a richer training signal without the need for retraining from scratch. To avoid transferring learned
correlations to new language models, it further substitutes CDA’s augmentation strategy with prob-
abilistic rules between tokens. Furthermore, we notice that a few works utilize multilinguality as bias
mitigation (Ahn and Oh, 2021; Levy et al., 2023; Nie et al., 2024a). These works advocate multilin-
16

--- Page 17 ---

gual training to mitigate biases. They demonstrate the eﬀectiveness of multilinguality in reducing
bias and boosting prediction accuracy (Nie et al., 2024a).
Another useful method is dropout regularization (Srivastava et al., 2014; Webster et al., 2020).
Brieﬂy, they explore the impact of increasing dropout parameters for BERT and ALBERT’s attention
weights and hidden activations, followed by an additional phase of pre-training. Experiments reveal
that dropout regularization reduces gender bias in these models. They propose that dropout disrupts
the attention mechanisms in BERT and ALBERT, thereby preventing the models from learning
undesirable word associations.
Grounded in the theory of causal inference, causality-guided methods are investigated due to
the theoretical guarantees and good generalization (Da et al., 2024; Cai et al., 2024). For instance,
researchers propose a bias reduction method for sentiment classiﬁcation (Da et al., 2024).
This
framework treats the neural network as a causal Directed Acyclic Graph (DAG). Borrowing the
concept of causal mediation analysis for neural network (Vig et al., 2020), authors study the direct
and indirect eﬀects of individual neurons to identify parts of a model where gender bias is causally
implicated. Finally, authors apply counterfactual training to only ﬁne-tune the BERT target layers.
Moreover, Cai et al. (2024) uses causal mediation analysis to trace the causal eﬀects of diﬀerent
components’ activation within a LLM. In this way, we are able to investigate the storage locations
and generation mechanisms of gender bias in LLMs.
Least Square Debias Method (LSDM) is
proposed to modify parameters to mitigate gender bias in models.
5.3 Post-model debiasing
Post-model debiasing mitigates bias by adjusting the output of LLMs. The beneﬁts of post-model
debiasing are no changes in the training data and no changes in the architecture of LLMs. For
example, reinforced calibration can be used to mitigates political bias in GPT-2 (Liu et al., 2021,
2022).
It keeps the architecture of GPT-2 unchanged but calibrates bias during the generation.
More speciﬁcally, authors present a reinforcement learning based framework for political biases in two
modes: word embedding debias and classiﬁer guided debias. For the word embedding debias, authors
pick the unbiased token at each generation step by forcing neutral words to maintain equal distances
from groups of sensitive words (e.g., male and female) in the embedding space (Bolukbasi et al.,
2016; Park et al., 2018; Zhao et al., 2018c). The classiﬁer guided debiasing works when the bias is
not purely word level (Bordia and Bowman, 2019).
Self-Debias is another work that leverages model’s internal knowledge to generate unbiased
prompts (Schick et al., 2021). The necessary condition for this approach is that if a model is able to
discern the presence of undesired biases, it should be able to avoid them at test time. Self-Ddebias
ﬁrst detects when the models output undesirable attributes based on internal knowledge. It then
reduces the probability of producing biased test (such as sexist, racist, and violent) by a decoding
algorithm. This has been empirically evaluated as a strong debiasing technique (Meade et al., 2022).
Projection-based methods are also shown to be useful for mitigating biases. Notable methods
such as SENT-DEBIAS (Liang et al., 2020a) and INLP (Ravfogel et al., 2020) work by projecting
model’s representations onto a subspace.
More speciﬁcally, SENT-DEBIAS involves four steps:
(1) identifying words that display biased attributes (e.g., he and she); (2) embedding these words
within biased attribute sentences to generate their sentence representations by CDA; (3) estimating
the bias subspace within these sentence representations by principle component analysis (PCA); (4)
debiasing general sentences by removing their projection onto this bias subspace. INLP roughly
debiases a model’s representations by training a linear classiﬁer to predict the protected attribute
we want to remove (e.g., gender) from the representations. The representations are then debiased by
projecting them into the nullspace of the trained classiﬁer’s weight matrix, eﬀectively eliminating all
the information the classiﬁer used to predict the protected attribute from the representation. This
process can be applied iteratively to further debias the representation.
17

--- Page 18 ---

In alignment with causal methods in intra-model debiasing, researchers also develop methods
based on causal prompting (Li et al., 2024a; Zhang et al., 2024).
Prompting methods gain pop-
ularity since the general public has no access to the model’s internal structure due to business
interest. Speciﬁcally, Li et al. (2024a) proposes causal prompting based on front-door adjustment
(Pearl et al., 2016). The proposed method modiﬁes prompts without access to the parameters and
logits of LLMs. First, it queries LLMs to generate chain-of-thoughts (CoTs) m times with the input
prompt (demonstration examples and a question of the test example). An encoder-based clustering
algorithm is applied to these CoTs and top K representative CoTs are selected. Next, it retrieves
the optimal demonstration examples for each representative. Finally, LLMs are queried T times to
obtain T answers for each representative CoT, and the ﬁnal answer is obtained by a weighted vot-
ing. Zhang et al. (2024) constructs detailed causal models for both the underlying data-generating
process of the training corpus and the LLM’s reasoning process. They recognize that selection mech-
anisms are crucial in determining how the LLM’s output can be inﬂuenced by diﬀerent prompts.
Additionally, they propose a causality-guided debiasing framework. By gaining causal insights into
the data-generating processes, the necessary conditions that prompt-design strategies must meet to
achieve principled and eﬀective debiasing are identiﬁed.
6. Ethical Concerns and Legal Challenges
Due to rapid advancements and successful integration of LLMs into systems that are widespread
throughout our society, more and more are raising concerns that LLMs can learn and amplify societal
biases (gender, race, religion, age, etc.) embedded in the enormous Internet data they are trained on
(Gallegos et al., 2024). As a result, LLMs can potentially generate biased outputs among diﬀerent
social groups, which falls under the ethical concerns of AI. Furthermore, disparate treatments led by
biased outputs in decision-making processes can result in legal challenges under anti-discrimination
laws.
We categorize biased outputs and disparate treatments according to a pre-established taxonomy:
representational harms and allocational harms (Blodgett et al., 2020). Representational harms refers
to when an automated system exhibits negative altitudes or misrepresents, even ignores existence of
certain social groups. Allocational harms refers to when an automated system allocate resources in
favor of some social groups over the others.
After reviewing many types of representational harms described in the literature, we constrained
our discussion to four categories that can cover most representational harms / ethical concerns:
• Stereotyping.
– Deﬁnition: Negative abstractions about a labeled social group.
– Result 1: Reinforced social bias against certain social groups,
– Result 2: Toxic language towards certain social groups.
• Misrepresentation.
– Deﬁnition: An incomplete sample generalized to a social group.
– Result 1: Reinforced normativity of the dominant social group and implicit exclusion or
devaluation or other groups.
– Result 2: Biased outputs that mischaracterize certain social groups.
• Disparate system performance.
– Deﬁnition: Degraded understanding or model performance in LLM language processing
or generation between social groups.
– Result 1: Allocational harms
18

--- Page 19 ---

Stereotyping.
LLMs can reinforce over-simpliﬁed and often negative labels on certain social
groups. Abid et al. (2021) demonstrate that LLMs captures Muslim-violence bias in various uses
cases and the Muslin-violence bias is more severe than commonly-seen biases of other religious groups.
Bender et al. (2021) describe how LLMs like referring to "women doctors" since even in today’s world,
doctor is a male-dominant occupation. Stereotypes perpetuated and even exacerbated by LLMs can
further translate into oﬀensive languages that target a social group. Gehman et al. (2020) evaluate
ﬁve language models (including GPT-1 to 3) using a "REALTOXICITYPROMPTS" machine and
show that all ﬁve model degenerates into toxicity over 0.5 (assigned by a widely-accepted toxicity
classiﬁer) within less than 100 generations from non-toxic prompts. Toxic generations from language
models can range from the like of "Islamic slaughtering" to "lying white media".
Misrepresentation. The disproportionate representation of marginalized or minority social groups
in LLM training data can lead to implicit exclusion of marginalized groups and mischaracterization
of certain groups. Bender et al. (2021) raise an example of ‘both genders’ that exclude non-binary
identities from the context.
Navigli et al. (2023) provide several examples of misrepresentation
across gender, age, nationality, ethnicity, etc. For example, "they are not very good at English" as
a response to "they are Chinese" or "she is ignorant" as a response to "she is White".
Disparate system performance. Koenecke et al. (2020) reveal that all of the ﬁve state-of-the-art
LLM-based automated speech recognition (ASR) systems show higher word error rates for black
speakers than white speakers. Saunders and Byrne (2020) demonstrate that the over-prevalence of
male-centric forms in Machine Translation training data result in better translations for male-centric
sentences and for sentences that contains male-dominant roles such as doctors and developers. Next,
we discuss disparate system performance in LLM-automated hiring and healthcare tools, which often
lead to allocational harms that raise anti-discrimination legal challenges.
• Allocational Harms.
– Deﬁnition: Disparate treatment due to membership of a social group or due to proxies
associated with a social group.
– LLM-based Hiring Tools: Resume and Cover Letter Screening
– LLM-based Health Care Tools: AI Diagnostics
Allocational harms.
Social biases preserved by LLMs would likely lead to direct or indirect
discrimination actions from LLMs.
Ferrara (2023) argues that AI-automated tools may reserve
and exacerbate societal biases embedded in the training data. LLM-aided resume analyzing tools
may disqualify people based on non-traditional backgrounds instead of job-related qualiﬁcations. In
2018, Amazon reportedly took an internal AI recruiting tool oﬀthe shelf after being accused of bias
against women since the resumes in the training data are predominantly from white males. Another
example is that LLM-aided healthcare tools may generate inaccurate predictions and treatment
recommendations for under-represented groups, potentially inﬂuencing healthcare decision-making
and resulting in unfair medical resource allocation. Zack et al. (2024) discovered that GPT-4 is less
likely to recommend more expensive diagnostician procedures to Black people and more likely to
predict Hispanic women are more likely to hide alcohol abusing history than Asian women.
7. Conclusion
This review has provided a comprehensive analysis of bias in LLMs, examining their sources, manifes-
tations, evaluation methods, and mitigation strategies. Our categorization of intrinsic and extrinsic
biases oﬀers a structured approach to understanding their impact on various NLP tasks (Doan et al.,
2024; Gallegos et al., 2024). We have evaluated a range of bias assessment techniques, from data-level
analysis to human-involved methods, providing researchers with a diverse toolkit for bias evaluation
(Liang et al., 2021). Our examination of mitigation strategies, encompassing pre-model, intra-model,
19

--- Page 20 ---

and post-model approaches, highlights both promising developments and areas that require further
research (Ferrara, 2023; Liu et al., 2022).
The ethical and legal implications of biased LLMs are substantial. The potential for both repre-
sentational and allocational harms in real-world applications emphasizes the need for responsible AI
development (Blodgett et al., 2020; Zack et al., 2024). As LLMs become increasingly integrated into
diverse facets of society–from personal assistants to decision-making systems in critical sectors-—it
is imperative to address these biases to prevent unintended negative consequences.
Looking forward, key research directions include developing context-sensitive bias evaluation
metrics that can identify subtle biases across diverse cultural settings (Wu et al., 2024), advancing
causal inference techniques for more eﬀective debiasing methods (Li et al., 2024a), and investigating
the long-term societal impacts of biased LLMs in critical domains such as healthcare and criminal
justice (Obermeyer et al., 2019). Additionally, fostering interdisciplinary collaborations to address
ethical challenges and develop adaptive regulatory frameworks (Gebru et al., 2021), while optimizing
the balance between model performance and fairness (Joniak and Aizawa, 2022), remains crucial.
By thoroughly examining the complexities of bias in LLMs and highlighting avenues for ongoing
research and collaboration, we aim to contribute to the development of AI systems that are both
technologically advanced and socially responsible. Addressing these challenges is essential to har-
ness the full potential of LLMs, fostering innovations that advance technology while upholding the
principles of fairness and equality.
Acknowledgments
References
Tariq Abdullah and Ahmed Ahmet. Deep learning in sentiment analysis: Recent architectures. ACM
Computing Surveys, 55(8):1–37, 2022.
Abubakar Abid, Maheen Farooqi, and James Zou. Persistent anti-muslim bias in large language
models. In Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society, page
298–306, New York, NY, USA, 2021. Association for Computing Machinery.
Arif Ahmad and Pushpak Bhattacharyya. Bias in language models: A survey.
Jaimeen Ahn and Alice Oh. Mitigating language-dependent ethnic bias in BERT. In Proceedings
of the 2021 Conference on Empirical Methods in Natural Language Processing, Online and Punta
Cana, Dominican Republic, November 2021. Association for Computational Linguistics.
Hirotugu Akaike. A new look at the statistical model identiﬁcation. IEEE Transactions on Automatic
Control, 19(6):716–723, 1974. doi: 10.1109/TAC.1974.1100705.
AJ Alvero, Jinsook Lee, Alejandra Regla-Vargas, Rene Kizilec, Thorsten Joachims, and Anthony Lis-
ing Antonio. Large language models, social demography, and hegemony: Comparing authorship
in human and synthetic text. Preprint, pages 1–25, 2024.
Haozhe An, Christabel Acquaye, Colin Wang, Zongxia Li, and Rachel Rudinger. Do large language
models discriminate in hiring decisions on the basis of race, ethnicity, and gender? arXiv preprint
arXiv:2406.10486, 2024.
Julia Angwin, JeﬀLarson, Surya Mattu, and Lauren Kirchner. Machine bias. ProPublica, 23(2016):
139–159, 2016.
Ron Artstein. Inter-annotator agreement. Handbook of linguistic annotation, pages 297–313, 2017.
Paul Azunre. Transfer learning for natural language processing. Simon and Schuster, 2021.
20

--- Page 21 ---

William Babonnaud, Estelle Delouche, and Mounir Lahlouh. The bias that lies beneath: Qualitative
uncovering of stereotypes in large language models. Swedish Artiﬁcial Intelligence Society, pages
195–203, 2024.
Yanhong Bai, Jiabao Zhao, Jinxin Shi, Zhentao Xie, Xingjiao Wu, and Liang He. Fairmonitor: A
dual-framework for detecting stereotypes and biases in large language models. arXiv preprint
arXiv:2405.03098, 2024.
Pragyan Banerjee, Abhinav Java, Surgan Jandial, Simra Shahid, Shaz Furniturewala, Balaji Krish-
namurthy, and Sumit Bhatia. All should be equal in the eyes of lms: Counterfactually aware
fair text generation. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence, volume 38,
pages 17673–17681, 2024.
Soumya Barikeri, Anne Lauscher, Ivan Vulić, and Goran Glavaš. RedditBias: A real-world resource
for bias evaluation and debiasing of conversational language models. In Proceedings of the 59th
Annual Meeting of the Association for Computational Linguistics and the 11th International Joint
Conference on Natural Language Processing (Volume 1: Long Papers), Online, August 2021. As-
sociation for Computational Linguistics.
Christine Basta, Marta R Costa-Jussà, and Noe Casas. Evaluating the underlying gender bias in
contextualized word embeddings. arXiv preprint arXiv:1904.08783, 2019.
Emily M Bender and Batya Friedman. Data statements for natural language processing: Toward
mitigating system bias and enabling better science. Transactions of the Association for Compu-
tational Linguistics, 6:587–604, 2018.
Emily M Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On the
dangers of stochastic parrots: Can language models be too big. In Proceedings of the 2021 ACM
conference on fairness, accountability, and transparency, pages 610–623, 2021.
Asia J Biega, Krishna P Gummadi, and Gerhard Weikum. Equity of attention: Amortizing individ-
ual fairness in rankings. In The 41st international acm sigir conference on research & development
in information retrieval, pages 405–414, 2018.
Abeba Birhane and Vinay Uday Prabhu. Large image datasets: A pyrrhic win for computer vision?
In 2021 IEEE Winter Conference on Applications of Computer Vision (WACV), pages 1536–1546.
IEEE, 2021.
Su Lin Blodgett and Brendan O’Connor. Racial disparity in natural language processing: A case
study of social media african-american english. arXiv preprint arXiv:1707.00061, 2017.
Su Lin Blodgett, Solon Barocas, Hal Daumé III, and Hanna Wallach. Language (technology) is
power: A critical survey of “bias” in NLP. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel
Tetreault, editors, Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, pages 5454–5476. Association for Computational Linguistics, 2020.
Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T Kalai. Man is
to computer programmer as woman is to homemaker? debiasing word embeddings. Advances in
neural information processing systems, 29, 2016.
Shikha Bordia and Samuel R. Bowman. Identifying and reducing gender bias in word-level language
models. In North American Chapter of the Association for Computational Linguistics, 2019.
Samuel R Bowman, Gabor Angeli, Christopher Potts, and Christopher D Manning. A large anno-
tated corpus for learning natural language inference. arXiv preprint arXiv:1508.05326, 2015.
21

--- Page 22 ---

Tom B Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla Dhariwal,
Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language models are
few-shot learners. Advances in Neural Information Processing Systems, 33:1877–1901, 2020.
Robin Burke, Nasim Sonboli, and Aldo Ordonez-Gauger. Balanced neighborhoods for multi-sided
fairness in recommendation. In Conference on fairness, accountability and transparency, pages
202–214. PMLR, 2018.
Pete Burnap and Matthew L Williams. Cyber hate speech on twitter: An application of machine
classiﬁcation and statistical modeling for policy and decision making. Policy & internet, 7(2):
223–242, 2015.
Janga Bussaja. Evaluating racial bias in large language models: The necessity for. Available at
SSRN 4880025, 2024.
Yuchen Cai, Ding Cao, Rongxi Guo, Yaqin Wen, Guiquan Liu, and Enhong Chen. Locating and
mitigating gender bias in large language models. In International Conference on Intelligent Com-
puting, pages 471–482. Springer, 2024.
Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. Semantics derived automatically from
language corpora contain human-like biases. Science, 356(6334):183–186, 2017.
Daniel Cer, Mona Diab, Eneko Agirre, Inigo Lopez-Gazpio, and Lucia Specia. Semeval-2017 task
1: Semantic textual similarity-multilingual and cross-lingual focused evaluation. arXiv preprint
arXiv:1708.00055, 2017.
Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan
Yi, Cunxiang Wang, Yidong Wang, et al. A survey on evaluation of large language models. ACM
Transactions on Intelligent Systems and Technology, 15(3):1–45, 2024.
Michelle Chen, Zhu Ma, Aniko Hannak, and Christo Wilson. My fair lady: Detecting and mitigating
bias in job advertisements. Proceedings of the 2018 World Wide Web Conference, pages 991–1000,
2018.
Qian Chen, Xiaodan Zhu, Zhenhua Ling, Si Wei, Hui Jiang, and Diana Inkpen. Enhanced lstm for
natural language inference. arXiv preprint arXiv:1609.06038, 2016.
Ruey-Cheng Chen, Qingyao Ai, Gaya Jayasinghe, and W Bruce Croft. Correcting for recency bias
in job recommendation. In Proceedings of the 28th ACM international conference on information
and knowledge management, pages 2185–2188, 2019.
Furui Cheng, Vilém Zouhar, Robin Shing Moon Chan, Daniel Fürst, Hendrik Strobelt, and Men-
natallah El-Assady. Interactive analysis of llms using meaningful counterfactuals. arXiv preprint
arXiv:2405.00708, 2024.
Richárd Csáky, Patrik Purgai, and Gábor Recski. Improving neural conversational models with
entropy-based data ﬁltering. arXiv preprint arXiv:1905.05471, 2019.
Yifei Da, Matías Nicolás Bossa, Abel Díaz Berenguer, and Hichem Sahli. Reducing bias in sentiment
analysis models through causal mediation analysis and targeted counterfactual training. IEEE
Access, 2024.
Vu Minh Hoang Dang and Rakesh M Verma. Data quality in nlp: Metrics and a comprehensive
taxonomy. In International Symposium on Intelligent Data Analysis, pages 217–229. Springer,
2024.
22

--- Page 23 ---

Debarati Das, Karin De Langis, Anna Martin, Jaehyung Kim, Minhwa Lee, Zae Myung Kim, Shirley
Hayati, Risako Owan, Bin Hu, Ritik Parkar, et al. Under the surface: Tracking the artifactuality
of llm-generated data. arXiv preprint arXiv:2401.14698, 2024.
Maria De-Arteaga, Alexey Romanov, Hanna Wallach, Jennifer Chayes, Christian Borgs, Alexandra
Chouldechova, Sahin Geyik, Krishnaram Kenthapadi, and Adam Tauman Kalai. Bias in bios: A
case study of semantic representation bias in a high-stakes setting. In proceedings of the Conference
on Fairness, Accountability, and Transparency, pages 120–128, 2019.
Jader Martins Camboim de Sá, Marcos Da Silveira, and Cédric Pruski. Semantic change character-
ization with llms using rhetorics. arXiv preprint arXiv:2407.16624, 2024.
Daniel de Vassimon Manela, David Errington, Thomas Fisher, Boris van Breugel, and Pasquale
Minervini. Stereotype and skew: Quantifying gender bias in pre-trained and ﬁne-tuned language
models. In Proceedings of the 16th Conference of the European Chapter of the Association for
Computational Linguistics: Main Volume, pages 2232–2242, 2021.
Pieter Delobelle and Bettina Berendt. Fairdistillation: mitigating stereotyping in language models.
In Joint European Conference on Machine Learning and Knowledge Discovery in Databases, pages
638–654. Springer, 2022.
Sunipa Dev, Tao Li, JeﬀM Phillips, and Vivek Srikumar. On measuring and mitigating biased
inferences of word embeddings. In Proceedings of the AAAI Conference on Artiﬁcial Intelligence,
volume 34, pages 7659–7666, 2020.
Sunipa Dev, Emily Sheng, Jieyu Zhao, Aubrie Amstutz, Jiao Sun, Yu Hou, Mattie Sanseverino, Jiin
Kim, Akihiro Nishi, Nanyun Peng, et al. On measures of biases and harms in nlp. arXiv preprint
arXiv:2108.03362, 2021.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of deep
bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805, 2018.
Fernando Diaz, Bhaskar Mitra, and Nick Craswell.
Query expansion with locally-trained word
embeddings. arXiv preprint arXiv:1605.07891, 2016.
Mark Díaz, Isaac Johnson, Amanda Lazar, Anne Marie Piper, and Darren Gergle. Addressing age-
related bias in sentiment analysis. In Proceedings of the 2018 chi conference on human factors in
computing systems, pages 1–14, 2018.
Thang Viet Doan, Zichong Wang, Minh Nhat Nguyen, and Wenbin Zhang. Fairness in large language
models in three hours. In Proceedings of the 33rd ACM International Conference on Information
& Knowledge Management (Boise, USA), 2024.
Matthew Durward and Christopher Thomson. Evaluating vocabulary usage in llms. In Proceedings
of the 19th Workshop on Innovative Use of NLP for Building Educational Applications (BEA
2024), pages 266–282, 2024.
Satyam Dwivedi, Sanjukta Ghosh, and Shivam Dwivedi. Breaking the bias: Gender fairness in llms
using prompt engineering and in-context learning. Rupkatha Journal on Interdisciplinary Studies
in Humanities, 15(4), 2023.
Jessica Echterhoﬀ, Yao Liu, Abeer Alessa, Julian McAuley, and Zexue He. Cognitive bias in high-
stakes decision-making with llms. arXiv preprint arXiv:2403.00811, 2024.
23

--- Page 24 ---

Michael D Ekstrand, Mucun Tian, Ion Madrazo Azpiazu, Jennifer D Ekstrand, Oghenemaro Anuyah,
David McNeill, and Maria Soledad Pera.
All the cool kids, how do they ﬁt in?: Popularity
and demographic biases in recommender evaluation and eﬀectiveness. In Conference on fairness,
accountability and transparency, pages 172–186. PMLR, 2018.
David Esiobu, Xiaoqing Tan, Saghar Hosseini, Megan Ung, Yuchen Zhang, Jude Fernandes, Jane
Dwivedi-Yu, Eleonora Presani, Adina Williams, and Eric Smith. Robbie: Robust bias evaluation
of large generative language models. In Proceedings of the 2023 Conference on Empirical Methods
in Natural Language Processing, pages 3764–3814, 2023.
Emilio Ferrara. Should chatgpt be biased? challenges and risks of bias in large language models.
First Mondy, 28(11), 2023.
Isabel O Gallegos, Ryan A Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernon-
court, Tong Yu, Ruiyi Zhang, and Nesreen K Ahmed. Bias and fairness in large language models:
A survey. Computational Linguistics, pages 1–79, 2024.
Matt Gardner, Joel Grus, Mark Neumann, Oyvind Tafjord, Pradeep Dasigi, Nelson Liu, Matthew
Peters, Michael Schmitz, and Luke Zettlemoyer. Allennlp: A deep semantic natural language
processing platform. arXiv preprint arXiv:1803.07640, 2018.
Nikhil Garg, Londa Schiebinger, Dan Jurafsky, and James Zou. Word embeddings quantify 100
years of gender and ethnic stereotypes. Proceedings of the National Academy of Sciences, 115(16):
E3635–E3644, 2018.
Aparna Garimella, Akhash Amarnath, Kiran Kumar, Akash Pramod Yalla, N Anandhavelu, Niyati
Chhaya, and Balaji Vasan Srinivasan. He is very intelligent, she is very beautiful? on mitigating
social biases in language modelling and generation. In Findings of the Association for Computa-
tional Linguistics: ACL-IJCNLP 2021, pages 4534–4545, 2021.
Aparna Garimella, Rada Mihalcea, and Akhash Amarnath. Demographic-aware language model
ﬁne-tuning as a bias mitigation technique.
In Proceedings of the 2nd Conference of the Asia-
Paciﬁc Chapter of the Association for Computational Linguistics and the 12th International Joint
Conference on Natural Language Processing (Volume 2: Short Papers), pages 311–319, 2022.
Yingqiang Ge, Wenyue Hua, Kai Mei, Juntao Tan, Shuyuan Xu, Zelong Li, Yongfeng Zhang, et al.
Openagi: When llm meets domain experts. Advances in Neural Information Processing Systems,
36, 2024.
Timnit Gebru, Jamie Morgenstern, Briana Vecchione, Jennifer Wortman Vaughan, Hanna Wallach,
Hal Daumé Iii, and Kate Crawford. Datasheets for datasets. Communications of the ACM, 64
(12):86–92, 2021.
Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A. Smith. RealToxici-
tyPrompts: Evaluating neural toxic degeneration in language models. In Trevor Cohn, Yulan He,
and Yang Liu, editors, Findings of the Association for Computational Linguistics: EMNLP 2020,
pages 3356–3369. Association for Computational Linguistics, 2020.
Seraphina Goldfarb-Tarrant. Fairness in transfer learning for natural language processing. 2024.
Josh Goldman and John K Tsotsos. Statistical challenges with dataset construction: Why you will
never have enough images. arXiv preprint arXiv:2408.11160, 2024.
Atmika Gorti, Manas Gaur, and Aman Chadha. Unboxing occupational bias: Grounded debiasing
llms with us labor data. arXiv preprint arXiv:2408.11247, 2024.
24

--- Page 25 ---

Md Rakibul Hasan, Maisha Maliha, and M Arifuzzaman. Sentiment analysis with nlp on twitter
data. In 2019 international conference on computer, communication, chemical, materials and
electronic engineering (IC4ME2), pages 1–4. IEEE, 2019.
Trevor Hastie, Robert Tibshirani, and Jerome Friedman. The Elements of Statistical Learning: Data
Mining, Inference, and Prediction. Springer Science & Business Media, 2nd edition, 2009. URL
https://doi.org/10.1007/978-0-387-84858-7.
Lucy Havens, Melissa Terras, Benjamin Bach, and Beatrice Alex. Uncertainty and inclusivity in
gender bias annotation: An annotation taxonomy and annotated datasets of british english text.
In 4th Workshop on Gender Bias in Natural Language Processing at NAACL, pages 30–57. ACL
Anthology, 2022.
James J. Heckman. Sample selection bias as a speciﬁcation error. Econometrica, 47(1):153–161,
1979. doi: 10.2307/1912352. URL https://www.jstor.org/stable/1912352.
Lisa Anne Hendricks, Kaylee Burns, Kate Saenko, Trevor Darrell, and Anna Rohrbach. Women also
snowboard: Overcoming bias in captioning models. In Proceedings of the European conference on
computer vision (ECCV), pages 771–787, 2018.
John Hewitt and Christopher D Manning. A structural probe for ﬁnding syntax in word representa-
tions. In Proceedings of the 2019 Conference of the North American Chapter of the Association
for Computational Linguistics, pages 4129–4138, 2019.
Günter J Hitsch, Ali Hortaçsu, and Dan Ariely. Matching and sorting in online dating. American
Economic Review, 100(1):130–163, 2010.
Chuan Tian Hongfei Li, Qian H. Li and Kevin Hou. Issues in cox proportional hazards model with
unequal randomization. Journal of Biopharmaceutical Statistics, 0(0):1–6, 2024a. doi: 10.1080/
10543406.2024.2418139.
URL https://doi.org/10.1080/10543406.2024.2418139.
PMID:
39445665.
Chuan Tian Hongfei Li, Qian H. Li and Kevin Hou. Issues in cox proportional hazards model with
unequal randomization. Journal of Biopharmaceutical Statistics, 0(0):1–6, 2024b. doi: 10.1080/
10543406.2024.2418139.
URL https://doi.org/10.1080/10543406.2024.2418139.
PMID:
39445665.
Dirk Hovy and Shrimai Prabhumoye.
Five sources of bias in natural language processing.
In
Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics, pages
878–888, 2021.
Dirk Hovy and Anders Søgaard. Tagging performance correlates with author age. In Proceedings of
the 53rd annual meeting of the Association for Computational Linguistics and the 7th international
joint conference on natural language processing (volume 2: Short papers), pages 483–488, 2015.
Dirk Hovy and Shannon L Spruit. The social impact of natural language processing. In Proceedings
of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short
Papers), pages 591–598, 2016.
Dirk Hovy and Diyi Yang. The importance of modeling social factors of language: Theory and
practice. In Proceedings of the 2021 Conference of the North American Chapter of the Association
for Computational Linguistics: Human language technologies, pages 588–602, 2021.
Zhanhao Hu, Julien Piet, Geng Zhao, Jiantao Jiao, and David Wagner. Toxicity detection for free.
arXiv preprint arXiv:2405.18822, 2024.
25

--- Page 26 ---

Wenyue Hua, Yingqiang Ge, Shuyuan Xu, Jianchao Ji, and Yongfeng Zhang. Up5: Unbiased foun-
dation model for fairness-aware recommendation. arXiv preprint arXiv:2305.12090, 2023.
Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning Mao, Michael
Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, et al. Llama guard: Llm-based input-output
safeguard for human-ai conversations. arXiv preprint arXiv:2312.06674, 2023.
An Investigation into Bias. Systematic prejudices. 2024.
Liying Jiang, Ming Yang, and Xiang Li. Smart music player: User-adaptive music recommendation
system. IEEE Transactions on Multimedia, 22(3):666–675, 2020.
Przemyslaw Joniak and Akiko Aizawa. Gender biases and where to ﬁnd them: Exploring gender bias
in pre-trained transformer-based language models using movement pruning. In Proceedings of the
4th Workshop on Gender Bias in Natural Language Processing (GeBNLP), Seattle, Washington,
July 2022. Association for Computational Linguistics.
Ashraf Kamal, Tarique Anwar, Vineet Kumar Sejwal, and Mohd Fazil. Bicapshate: attention to
the linguistic context of hate via bidirectional capsules and hatebase.
IEEE Transactions on
Computational Social Systems, 11(2):1781–1792, 2023.
Mozhgan Karimi, Dietmar Jannach, and Michael Jugovac. News recommender systems–survey and
roads ahead. Information Processing & Management, 54(6):1203–1227, 2018.
Nitish Shirish Keskar, Bryan McCann, Lav R Varshney, Caiming Xiong, and Richard Socher. Ctrl:
A conditional transformer language model for controllable generation. In Proceedings of the 2019
Conference on Empirical Methods in Natural Language Processing, pages 111–129, 2019.
Simran Khanuja, Sebastian Ruder, and Partha Talukdar.
Evaluating the diversity, equity and
inclusion of nlp technology: A case study for indian languages. arXiv preprint arXiv:2205.12676,
2022.
Svetlana Kiritchenko and Saif M Mohammad. Examining gender and race bias in two hundred
sentiment analysis systems. arXiv preprint arXiv:1805.04508, 2018.
Allison Koenecke, Andrew Nam, Emily Lake, Joe Nudell, Minnie Quartey, Zion Mengesha, Connor
Toups, John R Rickford, Dan Jurafsky, and Sharad Goel. Racial disparities in automated speech
recognition. Proceedings of the national academy of sciences, 117(14):7684–7689, 2020.
Hyukhun Koh, Dohyung Kim, Minwoo Lee, and Kyomin Jung.
Can llms recognize toxic-
ity?
structured toxicity investigation framework and semantic-based metric.
arXiv preprint
arXiv:2402.06900, 2024.
Hadas Kotek, Rikker Dockum, and David Sun. Gender bias and stereotypes in large language models.
In Proceedings of the ACM collective intelligence conference, pages 12–24, 2023.
JESSICA B KUNTZ and ELISE C SILVA. Who authors the internet? Analyzing Gender Diversity
in ChatGPT-3 Training Data. Pitt Cyber: University of Pittsburgh, 2023.
Keita Kurita, Nidhi Vyas, Ayush Pareek, Alan W Black, and Yulia Tsvetkov. Measuring bias in
contextualized word representations. arXiv preprint arXiv:1906.07337, 2019.
Tom Kwiatkowski, Jennimaria Palomaki, Olivia Redﬁeld, Michael Collins, Ankur Parikh, Chris
Alberti, Danielle Epstein, Illia Polosukhin, Jacob Devlin, Kenton Lee, et al. Natural questions: a
benchmark for question answering research. Transactions of the Association for Computational
Linguistics, 7:453–466, 2019.
26

--- Page 27 ---

Surafel M Lakew, Marcello Federico, Matteo Negri, and Marco Turchi. Multilingual neural machine
translation for low-resource languages. IJCoL. Italian Journal of Computational Linguistics, 4
(4-1):11–25, 2018.
Byunghwee Lee, Rachith Aiyappa, Yong-Yeol Ahn, Haewoon Kwak, and Jisun An. Neural embed-
ding of beliefs reveals the role of relative dissonance in human decision-making. arXiv preprint
arXiv:2408.07237, 2024.
Kenton Lee, Luheng He, Mike Lewis, and Luke Zettlemoyer. End-to-end neural coreference resolution.
arXiv preprint arXiv:1707.07045, 2017.
Sharon Levy, Neha John, Ling Liu, Yogarshi Vyas, Jie Ma, Yoshinari Fujinuma, Miguel Ballesteros,
Vittorio Castelli, and Dan Roth. Comparing biases and the impact of multilingual training across
multiple languages.
In Proceedings of the 2023 Conference on Empirical Methods in Natural
Language Processing, Singapore, December 2023. Association for Computational Linguistics.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan Ghazvininejad, Abdelrahman Mohamed, Omer Levy,
Veselin Stoyanov, and Luke Zettlemoyer. Bart: Denoising sequence-to-sequence pre-training for
natural language generation, translation, and comprehension. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pages 7871–7880, 2020.
Jingling Li, Zeyu Tang, Xiaoyu Liu, Peter Spirtes, Kun Zhang, Liu Leqi, and Yang Liu. Steer-
ing llms towards unbiased responses: A causality-guided debiasing framework. arXiv preprint
arXiv:2403.08743, 2024a.
Weitao Li, Junkai Li, Weizhi Ma, and Yang Liu. Citation-enhanced generation for llm-based chatbot.
arXiv preprint arXiv:2402.16063, 2024b.
Yingji Li, Mengnan Du, Rui Song, Xin Wang, and Ying Wang. A survey on fairness in large language
models. arXiv preprint arXiv:2308.10149, 2023.
Paul Pu Liang, Irene Mengze Li, Emily Zheng, Yao Chong Lim, Ruslan Salakhutdinov, and Louis-
Philippe Morency. Towards debiasing sentence representations. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, Online, July 2020a. Association for
Computational Linguistics.
Paul Pu Liang, Liang Zheng, Ruslan Salakhutdinov, and Louis-Philippe Morency. Towards debias-
ing sentence representations. In Proceedings of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 5502–5515, 2020b.
Paul Pu Liang, Chiyu Wu, Louis-Philippe Morency, and Ruslan Salakhutdinov. Towards under-
standing and mitigating social biases in language models. In International Conference on Machine
Learning, pages 6565–6576. PMLR, 2021.
Zichao Lin, Shuyan Guan, Wending Zhang, Huiyan Zhang, Yugang Li, and Huaping Zhang. Towards
trustworthy llms: a review on debiasing and dehallucinating in large language models. Artiﬁcial
Intelligence Review, 57(9):1–50, 2024.
Ruibo Liu, Chenyan Jia, Jason Wei, Guangxuan Xu, Lili Wang, and Soroush Vosoughi. Mitigating
political bias in language models through reinforced calibration.
In Proceedings of the AAAI
Conference on Artiﬁcial Intelligence, volume 35, pages 14857–14866, 2021.
Ruibo Liu, Chenyan Jia, Jason Wei, Guangxuan Xu, and Soroush Vosoughi.
Quantifying and
alleviating political bias in language models. Artiﬁcial Intelligence, 304:103654, 2022.
27

--- Page 28 ---

Shuo Shuo Liu. Uniﬁed transfer learning in high-dimensional linear regression. In International
Conference on Artiﬁcial Intelligence and Statistics, pages 1036–1044. PMLR, 2024.
Bill MacCartney. Natural language inference. Stanford University, 2009.
Penny Mackieson, Aron Shlonsky, and Marie Connolly. Increasing rigor and reducing bias in qual-
itative research: A document analysis of parliamentary debates using applied thematic analysis.
Qualitative social work, 18(6):965–980, 2019.
Rowan
Hall
Maudslay,
Hila
Gonen,
Ryan
Cotterell,
and
Simone
Teufel.
It’s
all
in
the
name:
Mitigating
gender
bias
with
name-based
counterfactual
data
substitution.
In
Conference
on
Empirical
Methods
in
Natural
Language
Processing,
2019.
URL
https://api.semanticscholar.org/CorpusID:202541569.
Chandler May, Alex Wang, Shikha Bordia, Samuel R Bowman, and Rachel Rudinger. On measuring
social biases in sentence encoders. arXiv preprint arXiv:1903.10561, 2019.
Nicholas Meade, Elinor Poole-Dayan, and Siva Reddy. An empirical survey of the eﬀectiveness of
debiasing techniques for pre-trained language models. In Proceedings of the 60th Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers), pages 1878–1898,
Dublin, Ireland, May 2022. Association for Computational Linguistics.
Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena, Kristina Lerman, and Aram Galstyan.
A
survey on bias and fairness in machine learning. ACM Computing Surveys, 54(6):1–35, 2021.
Yu Meng, Yunyi Zhang, Jiaxin Huang, Chenyan Xiong, Heng Ji, Chao Zhang, and Jiawei Han. Text
classiﬁcation using label names only: A language model self-training approach. arXiv preprint
arXiv:2010.07245, 2020.
Karolis Misiunas and Ulrich F Keyser. Density-dependent speed-up of particle transport in channels.
Physical Review Letters, 122(21):214501, 2019.
Devam Mondal and Carlo Lipizzi. Mitigating large language model bias: Automated dataset aug-
mentation and prejudice quantiﬁcation. Computers, 13(6):141, 2024.
Edoardo Mosca, Ferenc Szigeti, Stella Tragianni, Daniel Gallagher, and Georg Groh. Shap-based
explanation methods: a review for nlp interpretability. In Proceedings of the 29th international
conference on computational linguistics, pages 4593–4603, 2022.
Anjishnu Mukherjee, Aylin Caliskan, Ziwei Zhu, and Antonios Anastasopoulos. Global gallery: The
ﬁne art of painting culture portraits through multilingual instruction tuning. In Proceedings of the
2024 Conference of the North American Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers), pages 6398–6415, 2024.
Moin Nadeem, Anna Bethke, and Siva Reddy. Stereoset: Measuring stereotypical bias in pretrained
language models. In Proceedings of the 59th Annual Meeting of the Association for Computational
Linguistics, pages 5356–5371, 2021.
Ramesh Nallapati, Bowen Zhou, Caglar Gulcehre, Bing Xiang, et al. Abstractive text summarization
using sequence-to-sequence rnns and beyond. arXiv preprint arXiv:1602.06023, 2016.
Usman Naseem, Imran Razzak, Katarzyna Musial, and Muhammad Imran. Transformer based deep
intelligent contextual embedding for twitter sentiment analysis.
Future Generation Computer
Systems, 113:58–69, 2020.
Roberto Navigli, Simone Conia, and Björn Ross. Biases in large language models: Origins, inventory,
and discussion. J. Data and Information Quality, 15(2), 2023.
28

--- Page 29 ---

Szilard
Nemes,
Junmei
M.
Jonasson,
Anna
Genell,
and
Gunnar
Steineck.
Bias
in
odds
ratios
by
logistic
regression
modelling
and
sample
size.
BMC
Med-
ical
Research
Methodology,
9:56,
2009.
doi:
10.1186/1471-2288-9-56.
URL
https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/1471-2288-9-56.
Davide Neri, Jacopo Soldani, Olaf Zimmermann, and Antonio Brogi. Design principles, architectural
smells and refactorings for microservices: a multivocal review. SICS Software-Intensive Cyber-
Physical Systems, 35:3–15, 2020.
Shangrui Nie, Michael Fromm, Charles Welch, Rebekka Görge, Akbar Karimi, Joan Plepi, Nazia
Mowmita, Nicolas Flores-Herr, Mehdi Ali, and Lucie Flek. Do multilingual large language models
mitigate stereotype bias? In Proceedings of the 2nd Workshop on Cross-Cultural Considerations
in NLP, Bangkok, Thailand, August 2024a. Association for Computational Linguistics.
Shangrui Nie, Michael Fromm, Charles Welch, Rebekka Görge, Akbar Karimi, Joan Plepi, Nazia Af-
san Mowmita, Nicolas Flores-Herr, Mehdi Ali, and Lucie Flek. Do multilingual large language
models mitigate stereotype bias? arXiv preprint arXiv:2407.05740, 2024b.
Ziad Obermeyer, Brian Powers, Christine Vogeli, and Sendhil Mullainathan. Dissecting racial bias
in an algorithm used to manage the health of populations. Science, 366(6464):447–453, 2019.
Collins W Okonkwo and Abejide Ade-Ibijola.
The role of artiﬁcial intelligence in education:
Prospects and challenges. Journal of Educational Technology & Society, 26(1):1–12, 2023.
Jahna Otterbacher, Jo Bates, and Paul Clough. Competent men and warm women: Gender stereo-
types and backlash in image search results. In Proceedings of the 2017 chi conference on human
factors in computing systems, pages 6620–6631, 2017.
Tiago P Pagano, Rafael B Loureiro, Fernanda VN Lisboa, Rodrigo M Peixoto, Guilherme AS
Guimarães, Gustavo OR Cruz, Maira M Araujo, Lucas L Santos, Marco AS Cruz, Ewerton LS
Oliveira, et al. Bias and unfairness in machine learning models: a systematic review on datasets,
tools, fairness metrics, and identiﬁcation and mitigation methods. Big data and cognitive comput-
ing, 7(1):15, 2023.
Bo Pang, Lillian Lee, et al. Opinion mining and sentiment analysis. Foundations and Trends® in
information retrieval, 2(1–2):1–135, 2008.
Eli Pariser. The Filter Bubble: How the New Personalized Web is Changing What We Read and
How We Think. Penguin, 2011.
Ji Ho Park, Jamin Shin, and Pascale Fung. Reducing gender bias in abusive language detection.
In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing,
Brussels, Belgium, October-November 2018. Association for Computational Linguistics.
Silviu Paun, Ron Artstein, and Massimo Poesio. Statistical methods for annotation analysis. Springer
Nature, 2022.
Judea Pearl, Madelyn Glymour, and Nicholas P Jewell. Causal inference in statistics: A primer.
John Wiley & Sons, 2016.
Laura Perez-Beltrachini and Mirella Lapata. Models and datasets for cross-lingual summarisation.
arXiv preprint arXiv:2202.09583, 2022.
Marcelo OR Prates, Pedro H Avelar, and Luís C Lamb. Assessing gender bias in machine translation:
a case study with google translate. Neural Computing and Applications, 32:6363–6381, 2020.
29

--- Page 30 ---

Yusu Qian, Urwa Muaz, Ben Zhang, and Jae Won Hyun. Reducing gender bias in word-level language
models with a gender-equalizing loss function. In Proceedings of the 57th Annual Meeting of the
Association for Computational Linguistics: Student Research Workshop, Florence, Italy, July 2019.
Association for Computational Linguistics.
Yao Qu and Jue Wang. Performance and biases of large language models in public opinion simulation.
Humanities and Social Sciences Communications, 11(1):1–13, 2024.
Alec Radford, Jeﬀrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al. Language
models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
Colin Raﬀel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a uniﬁed text-to-text
transformer. Journal of Machine Learning Research, 21:1–67, 2020.
Alvin Rajkomar, Moritz Hardt, Michael D Howell, Greg Corrado, and Michael H Chin. Ensuring
fairness in machine learning to advance health equity.
Annals of Internal Medicine, 169(12):
866–872, 2018.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. Squad: 100,000+ questions
for machine comprehension of text. arXiv preprint arXiv:1606.05250, 2016.
Pranav Rajpurkar, Robin Jia, and Percy Liang. Know what you don’t know: Unanswerable questions
for squad. arXiv preprint arXiv:1806.03822, 2018.
Shauli Ravfogel, Yanai Elazar, Hila Gonen, Michael Twiton, and Yoav Goldberg. Null it out: Guard-
ing protected attributes by iterative nullspace projection. In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics, Online, July 2020. Association for Compu-
tational Linguistics.
Partha Pratim Ray. Chatgpt: A comprehensive review on background, applications, key challenges,
bias, ethics, limitations and future scope.
Internet of Things and Cyber-Physical Systems, 3:
121–154, 2023.
David Rozado. The political preferences of llms. PloS one, 19(7):e0306621, 2024.
Donald B. Rubin. Estimating causal eﬀects of treatments in randomized and nonrandomized studies.
Journal of Educational Psychology, 66(5):688–701, 1974. doi: 10.1037/h0037350.
Rachel Rudinger, Jason Naradowsky, Brian Leonard, and Benjamin Van Durme. Gender bias in
coreference resolution. arXiv preprint arXiv:1804.09301, 2018.
Abel Salinas, Louis Penaﬁel, Robert McCormack, and Fred Morstatter. " im not racist but...": Dis-
covering bias in the internal knowledge of large language models. arXiv preprint arXiv:2310.08780,
2023.
Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi, and Noah A Smith.
The risk of racial
bias in hate speech detection. In Proceedings of the 57th Annual Meeting of the Association for
Computational Linguistics, pages 1668–1678, 2019a.
Maarten Sap, Saadia Gabriel, Lianhui Qin, Dan Jurafsky, Noah A Smith, and Yejin Choi. Social
bias frames: Reasoning about social and power implications of language. In Proceedings of the
57th Annual Meeting of the Association for Computational Linguistics, pages 5477–5483, 2019b.
30

--- Page 31 ---

Danielle Saunders and Bill Byrne. Reducing gender bias in neural machine translation as a domain
adaptation problem. In Dan Jurafsky, Joyce Chai, Natalie Schluter, and Joel Tetreault, editors,
Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages
7724–7736. Association for Computational Linguistics, 2020.
Akrati Saxena, Harita Reddy, and Pratishtha Saxena. Introduction to sentiment analysis covering
basics, tools, evaluation metrics, challenges, and applications. Principles of social networking: the
new horizon and emerging challenges, pages 249–277, 2022.
Nino Scherrer, Claudia Shi, Amir Feder, and David Blei. Evaluating the moral beliefs encoded in
llms. Advances in Neural Information Processing Systems, 36, 2024.
Timo Schick, Sahana Udupa, and Hinrich Schütze. Self-diagnosis and self-debiasing: A proposal for
reducing corpus-based bias in nlp. Transactions of the Association for Computational Linguistics,
9:1408–1424, 2021.
Rico Sennrich. Neural machine translation. Institute for Language, Cognition and Computation
University of Edinburgh, 18, 2016.
Ibrahim Mohamed Serouis and Florence Sèdes. Exploring large language models for bias mitigation
and fairness. In 1st International Workshop on AI Governance (AIGOV) in conjunction with the
Thirty-Third International Joint Conference on Artiﬁcial Intelligence, 2024.
Tianxiao Shen, Tao Lei, Regina Barzilay, and Tommi Jaakkola. Style transfer from non-parallel text
by cross-alignment. Advances in neural information processing systems, 30, 2017.
Zhiqiang Shen, Tianhua Tao, Liqun Ma, Willie Neiswanger, Joel Hestness, Natalia Vassilieva, Daria
Soboleva, and Eric Xing.
Slimpajama-dc: Understanding data combinations for llm training.
arXiv preprint arXiv:2309.10818, 2023.
Emily Sheng, Kai-Wei Chang, Prem Natarajan, and Nanyun Peng. The woman worked as a babysit-
ter: On biases in language generation. In Proceedings of the 2019 Conference on Empirical Methods
in Natural Language Processing and the 9th International Joint Conference on Natural Language
Processing (EMNLP-IJCNLP), pages 3407–3412, 2019.
Emily Sheng, Kai-Wei Chang, Premkumar Natarajan, and Nanyun Peng. Societal biases in language
generation: Progress and challenges. In Proceedings of the 59th Annual Meeting of the Association
for Computational Linguistics, pages 4275–4293, 2021.
Weiyan Shi, Ryan Li, Yutong Zhang, Caleb Ziems, Raya Horesh, Rogério Abreu de Paula, Diyi
Yang, et al. Culturebank: An online community-driven knowledge base towards culturally aware
language technologies. arXiv preprint arXiv:2404.15238, 2024.
Leandro Silva, Mainack Mondal, Denzil Correa, Fabrício Benevenuto, and Ingmar Weber. Analyzing
the targets of hate in online social media. In Proceedings of the International AAAI Conference
on Web and Social Media, volume 10, pages 687–690, 2016.
Gabriel Simmons and Christopher Hare. Large language models as subpopulation representative
models: A review. arXiv preprint arXiv:2310.17888, 2023.
Nitish Srivastava, Geoﬀrey Hinton, Alex Krizhevsky, Ilya Sutskever, and Ruslan Salakhutdinov.
Dropout: a simple way to prevent neural networks from overﬁtting. The Journal of Machine
Learning Research, 15(1):1929–1958, 2014.
Tony Sun, Andrew Gaut, Shirlyn Tang, Yuxin Huang, Mai ElSherief, Jieyu Zhao, Diba Mirza,
Elizabeth Belding, Kai-Wei Chang, and William Yang Wang. Mitigating gender bias in natural
language processing: Literature review. arXiv preprint arXiv:1906.08976, 2019.
31

--- Page 32 ---

Zeerak Talat, Aurélie Névéol, Stella Biderman, Miruna Clinciu, Manan Dey, Shayne Longpre, Sasha
Luccioni, Maraim Masoud, Margaret Mitchell, Dragomir Radev, et al. You reap what you sow:
On the challenges of bias evaluation under multilingual settings. In Proceedings of BigScience
Episode# 5–Workshop on Challenges & Perspectives in Creating Large Language Models, pages
26–41, 2022.
Liling Tan and Francis Bond.
Building and annotating the linguistically diverse ntu-mc (ntu-
multilingual corpus). In Proceedings of the 25th Paciﬁc Asia Conference on Language, Information
and Computation, pages 362–371. Waseda University, 2011.
Robert Tibshirani. Regression shrinkage and selection via the lasso. Journal of the Royal Statistical
Society: Series B (Methodological), 58(1):267–288, 1996.
Eva Vanmassenhove, Dimitar Shterionov, and Andy Way. Lost in translation: Loss and decay of
linguistic richness in machine translation. arXiv preprint arXiv:1906.12068, 2019.
Yehuda
Vardi.
Nonparametric
estimation
in
the
presence
of
length
bias.
The
Annals
of
Statistics,
10(2):616–620,
1982.
doi:
10.1214/aos/1176345802.
URL
https://projecteuclid.org/euclid.aos/1176345802.
A Vaswani. Attention is all you need. Advances in Neural Information Processing Systems, 2017.
Jesse Vig, Sebastian Gehrmann, Yonatan Belinkov, Sharon Qian, Daniel Nevo, Yaron Singer, and
Stuart Shieber.
Investigating gender bias in language models using causal mediation analysis.
Advances in Neural Information Processing Systems, 33:12388–12401, 2020.
Ivan Vulic and Marie-Francine Moens. Cross-lingual semantic similarity of words as the similarity
of their semantic word responses.
In Proceedings of the 2013 Conference of the North Amer-
ican Chapter of the Association for Computational Linguistics: Human Language Technologies
(NAACL-HLT 2013), pages 106–116. ACL; East Stroudsburg, PA, 2013.
Claudia Wagner, Eduardo Graells-Garrido, David Garcia, and Filippo Menczer. Women through
the glass ceiling: gender asymmetries in wikipedia. EPJ data science, 5:1–24, 2016.
Angelina Wang, Jamie Morgenstern, and John P Dickerson. Large language models cannot replace
human participants because they cannot portray identity groups. arXiv preprint arXiv:2402.01908,
2024a.
Xinru Wang, Hannah Kim, Sajjadur Rahman, Kushan Mitra, and Zhengjie Miao.
Human-llm
collaborative annotation through eﬀective veriﬁcation of llm labels. In Proceedings of the CHI
Conference on Human Factors in Computing Systems, pages 1–21, 2024b.
Zeyu Wang. Causalbench: A comprehensive benchmark for evaluating causal reasoning capabilities
of large language models. In Proceedings of the 10th SIGHAN Workshop on Chinese Language
Processing (SIGHAN-10), pages 143–151, 2024.
Mayur Wankhade, Annavarapu Chandra Sekhara Rao, and Chaitanya Kulkarni. A survey on sen-
timent analysis methods, applications, and challenges. Artiﬁcial Intelligence Review, 55(7):5731–
5780, 2022.
Kellie Webster, Marta Recasens, Vera Axelrod, and Jason Baldridge. Mind the gap: A balanced
corpus of gendered ambiguous pronouns. Transactions of the Association for Computational Lin-
guistics, 6:605–617, 2018.
Kellie Webster, Xuezhi Wang, Ian Tenney, Alex Beutel, Emily Pitler, Ellie Pavlick, Jilin Chen,
Ed Chi, and Slav Petrov. Measuring and reducing gendered correlations in pre-trained models.
arXiv preprint arXiv:2010.06032, 2020.
32

--- Page 33 ---

Cynthia M Whissell. The dictionary of aﬀect in language. In The measurement of emotions, pages
113–131. Elsevier, 1989.
Zekun Wu, Sahan Bulathwela, Maria Perez-Ortiz, and Adriano Soares Koshiyama. Auditing large
language models for enhanced text-based stereotype detection and probing-based bias evaluation.
arXiv preprint arXiv:2404.01768, 2024.
Yuqi Yang, Yuan Yuan, and Lei Liu. Finbert: A pretrained language model for ﬁnancial communi-
cations. arXiv preprint arXiv:2006.08097, 2020.
Travis Zack, Eric Lehman, Mirac Suzgun, and Jorge A Rodriguez. Assessing the potential of gpt-4 to
perpetuate racial and gender biases in health care: a model evaluation study. The Lancet Digital
Health, 6(1):E12–E22, 2024.
LotﬁA Zadeh. From search engines to question answering systems—the problems of world knowledge,
relevance, deduction and precisiation. In Capturing intelligence, volume 1, pages 163–210. Elsevier,
2006.
Congzhi Zhang, Linhai Zhang, Deyu Zhou, and Guoqiang Xu. Causal prompting: Debiasing large
language model prompting based on front-door adjustment.
arXiv preprint arXiv:2403.02738,
2024.
Lei Zhang, Shuai Wang, and Bing Liu.
Deep learning for sentiment analysis: A survey. IEEE
Transactions on Aﬀective Computing, 10(3):235–255, 2018.
Shuai Zhang, Lina Yao, Aixin Sun, and Yi Tay. Deep learning based recommender system: A survey
and new perspectives. ACM computing surveys (CSUR), 52(1):1–38, 2019a.
Yizhe Zhang, Siqi Sun, Michel Galley, Yen-Chun Chen, Chris Brockett, Xiang Gao, Jianfeng Gao,
Jingjing Liu, and Bill Dolan.
Dialogpt: Large-scale generative pre-training for conversational
response generation. arXiv preprint arXiv:1911.00536, 2019b.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Ordonez, and Kai-Wei Chang.
Men also like
shopping:
Reducing gender bias ampliﬁcation using corpus-level constraints.
arXiv preprint
arXiv:1707.09457, 2017.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Ordonez, and Kai-Wei Chang. Gender bias in
coreference resolution: Evaluation and debiasing methods. In Proceedings of the 2018 Conference
of the North American Chapter of the Association for Computational Linguistics, pages 15–20,
2018a.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Vicente Ordonez, and Kai-Wei Chang. Learning gender-
neutral word embeddings. In Proceedings of the 2018 Conference on Empirical Methods in Natural
Language Processing, pages 4847–4853, 2018b.
Jieyu Zhao, Yichao Zhou, Zeyu Li, Wei Wang, and Kai-Wei Chang. Learning gender-neutral word
embeddings. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language
Processing, Brussels, Belgium, October-November 2018c. Association for Computational Linguis-
tics.
Jieyu Zhao, Tianlu Wang, Mark Yatskar, Ryan Cotterell, Vicente Ordonez, and Kai-Wei Chang.
Gender bias in contextualized word embeddings. arXiv preprint arXiv:1904.03310, 2019.
Fuzhen Zhuang, Zhiyuan Qi, Keyu Duan, Dongbo Xi, Yongchun Zhu, Hengshu Zhu, Hui Xiong, and
Qing He. A comprehensive survey on transfer learning. Proceedings of the IEEE, 109(1):43–76,
2020.
33

--- Page 34 ---

Ran Zmigrod, Sabrina J. Mielke, Hanna Wallach, and Ryan Cotterell. Counterfactual data augmen-
tation for mitigating gender stereotypes in languages with rich morphology. In Proceedings of the
57th Annual Meeting of the Association for Computational Linguistics, Florence, Italy, July 2019.
Association for Computational Linguistics.
34

--- Page 35 ---

Appendix A. Examples of Extrinsic Biases
A.1 Natural Language Understanding (NLU) tasks
NLU encompasses a broad range of tasks that aim to improve comprehension of input sequences
(Chang et al., 2024). It seeks to grasp the deeper connotations and implications inherent in human
communication, focusing on what human language signiﬁes beyond the literal interpretation of
individual words.
A.1.1 Coreference Resolution
Coreference Resolution in the context of LLMs involves identifying instances where diﬀerent expres-
sions within a text refer to the same entity (Lee et al., 2017). This task is crucial for accurately
interpreting the meaning of sentences, especially in cases where pronouns, names, or other referen-
tial expressions are used. The primary goal of coreference resolution is to correctly link pronouns
like “he,” “she,” or “it” and deﬁnite descriptions like “the CEO” to the appropriate entity mentioned
earlier in the text.
In coreference resolution tasks, extrinsic bias frequently arises when the model’s ability to cor-
rectly identify and link references (such as pronouns or entity names) to the appropriate entities is
aﬀected by external factors unrelated to the intrinsic nature of the text itself.
• Gender Bias
– Stereotypical Occupation Associations: In a sentence like “The doctor ﬁnished the
surgery, and she went to check on the patient,” a biased model might mistakenly link
“she” to a nurse or another female ﬁgure, based on the stereotype that doctors are more
likely to be male. Similarly, in “The nurse ﬁnished the shift, and he went home,” the
model might incorrectly associate “he” with a doctor or a male ﬁgure rather than the
nurse, reﬂecting a bias that nurses are more likely to be female (Zhao et al., 2018a).
– Gendered Pronoun Resolution: In a sentence like “Sam loves cooking. He is very tal-
ented in the kitchen,” a biased model might incorrectly resolve “he” to assume that Sam is
male, even though the name “Sam” can be gender-neutral. This reﬂects a bias that cook-
ing, when associated with talent or professionalism, is more likely to be linked to males,
while in other contexts, the same task might be associated with females (Rudinger et al.,
2018).
• Age Bias
– Assumptions about Technological Proﬁciency: In a sentence like “The senior pro-
grammer and the young intern were debugging the code. He quickly found the bug,” a
biased model might incorrectly resolve “He” to refer to the senior programmer, based on
the stereotype that senior individuals are more skilled with technology, even though both
the senior programmer and the young intern are equally likely candidates (Hovy and Yang,
2021).
– Bias in Linking Pronouns to Age-related Roles: In a sentence like “The retiree
and the young employee discussed the new policies.
He suggested some changes,” a
biased model might incorrectly resolve “he” to refer to the young employee, based on
the stereotype that younger individuals are more likely to suggest changes or new ideas,
whereas retirees might be stereotypically viewed as less active in professional settings
(Garg et al., 2018).
• Cultural or Regional Bias
35

--- Page 36 ---

– Regional Variants and Pronoun Use: In diﬀerent cultural or regional contexts, the
use of pronouns can vary signiﬁcantly. For instance, in some languages, pronouns might
be omitted altogether (pro-drop languages), while in others, they are used extensively.
A coreference resolution system trained predominantly on non-pro-drop language data
might struggle with correctly resolving entities in pro-drop languages, where subjects are
often implied rather than explicitly mentioned (Hovy and Yang, 2021).
– Cultural Context in Family Roles: In some cultures, family roles are strictly deﬁned,
with certain responsibilities typically assigned to speciﬁc genders or ages. A coreference
resolution model might incorrectly resolve pronouns based on these cultural stereotypes.
For example, in a sentence like “The eldest son took care of his siblings. She prepared
dinner,” a biased model might incorrectly resolve “She” to the mother rather than the
eldest daughter, based on cultural assumptions about family roles (Rudinger et al., 2018).
A.1.2 Semantic Textual Similarity (STS)
Semantic Textual Similarity (STS) tasks in LLMs focus on evaluating how similar the meanings
of two pieces of text are. The purpose of STS is to determine how closely related the meanings
of two text snippets are, which can vary from complete equivalence in meaning to being entirely
unrelated. STS tasks are crucial for various applications where understanding the nuanced diﬀerences
or similarities between texts is essential (Cer et al., 2017).
Extrinsic biases in STS tasks refer to biases that cause the model to inaccurately assess the
similarity between two pieces of text. These biases can lead to skewed results, where the model
might overestimate or underestimate the similarity between texts based on these biases rather than
their actual semantic content.
• Gender Bias
– Gendered Language and Pronoun Resolution: When comparing the similarity be-
tween sentences with gendered pronouns, such as: Sentence A: “She is a leader.”; Sentence
B: “He is a leader.” A biased model might incorrectly rate the similarity between these
sentences lower than it should, due to underlying gender associations, despite the fact
that the sentences are nearly identical except for the pronoun (Zhao et al., 2017).
– Gender-Stereotyped Professions: Consider two sentences: Sentence A: “The nurse
administered the medication.”; Sentence B: “She took care of the patient.” If an LLM
trained with gender biases in its data associates nursing primarily with women, it might
assess a higher similarity between these sentences compared to another pair where the
nurse is referred to as “he,” even though the gender of the nurse should not aﬀect the
similarity score (Bolukbasi et al., 2016).
• Age Bias
– Age-Based Expectations in Language Use: The sentences “She is full of energy
and enthusiasm” and “She is calm and experienced” might be rated as less similar if the
ﬁrst sentence is associated with a young person and the second with an older person,
despite both sentences describing positive qualities. A biased model might reinforce the
stereotype that energy is associated with youth and calmness with older age, skewing the
similarity score (Caliskan et al., 2017).
– Age Stereotypes in Sentiment and Perception: Sentences like “She is wise” and “She
is elderly” might be rated as similar by a biased model due to the stereotype that elderly
people are wise. This could lead to an overestimation of the similarity between texts that
describe older individuals, even if the context suggests diﬀerent meanings (Diaz et al.,
2016).
36

--- Page 37 ---

• Cultural or Regional Bias
– Cultural Idioms and Expressions: Consider the sentences “It’s raining cats and dogs”
(an English idiom meaning heavy rain) and “Il pleut des cordes” (a French idiom meaning
the same). A culturally biased model trained predominantly on English data might rate
these sentences as less similar because the literal words are diﬀerent, even though they
convey the same meaning in their respective cultures (Vulic and Moens, 2013).
– Regional Dialects and Variants:
In English, the word "apartment" is commonly
used in American English, while “ﬂat” is used in British English. A model trained pre-
dominantly on one variant might incorrectly assess the similarity between “I live in an
apartment” and “I live in a ﬂat” as low, due to not recognizing the regional synonymy
(Tan and Bond, 2011).
A.1.3 Natural Language Inference
Natural Language Inference (NLI) is a task where the goal is to determine the relationship between
a pair of sentences, typically referred to as the “premise” and the “hypothesis.” The task involves
classifying the relationship between these sentences into one of three categories: entailment (the
hypothesis logically follows from the premise), contradiction (the hypothesis contradicts the premise),
or neutral(the hypothesis is neither supported nor contradicted by the premise; it could be true or
false based on the premise alone) (Bowman et al., 2015). It is a fundamental task in understanding
and reasoning with natural language and is often used to evaluate the reasoning capabilities of LLMs.
Extrinsic bias in the NLI task using LLMs refers to biases introduced from external factors
that aﬀect the model’s ability to accurately determine the relationship between a premise and a
hypothesis. In NLI, the task is to decide whether a given hypothesis is entailed by, contradicted by,
or neutral with respect to the premise. External biases can inﬂuence how well the model performs
this task, leading to skewed or unfair results (MacCartney, 2009; Dev et al., 2020).
• Gender Bias
– Stereotypical Gender Roles in Professions: Given a premise like “The person is a
doctor,” and a hypothesis “She is caring,” a biased model might be more likely to infer that
the hypothesis is true because of the stereotype associating women with caring professions.
Conversely, if the premise is “The person is an engineer,” and the hypothesis is “She is
analytical,” the model might incorrectly infer this as less likely due to the stereotype that
engineering is male-dominated (Rudinger et al., 2018).
– Gendered Language and Assumptions: In a scenario where the premise is “Alex
received a promotion,” and the hypothesis is “She worked very hard,” a biased model
might rate this inference as less likely due to the name “Alex,” which can be gender-
neutral but may be more commonly associated with males. The model may incorrectly
prefer “He worked very hard” based on gender assumptions (Zhao et al., 2017).
• Age Bias
– Bias Toward Younger Individuals in Dynamic Roles: Given the premise “The
person is a dynamic entrepreneur,” and the hypothesis “The person is young,” a biased
model might overly favor the hypothesis due to the stereotype that entrepreneurship and
dynamism are traits associated with younger people, disregarding the possibility that
older individuals can also embody these characteristics (Caliskan et al., 2017).
– Age-Related Stereotypes in Professional Contexts: If the premise is “The CEO
announced the company’s new strategic direction,” a biased model might infer that “The
CEO is in their 50s” is more likely to be true (entailment), reﬂecting the stereotype that
37

--- Page 38 ---

leadership roles are typically held by older individuals.
On the other hand, it might
incorrectly classify “The CEO is in their 20s” as a contradiction (Zhao et al., 2018a).
• Cultural or Regional Bias
– Cultural Norms and Social Roles: Consider the premise “She is a nurse” and the
hypothesis “She is caring.” A model inﬂuenced by cultural stereotypes might incorrectly
infer that the hypothesis is true based on the cultural assumption that nurses are in-
herently caring, which reﬂects a bias rather than a logical inference based on the text
(Rudinger et al., 2018).
– Regional Political and Historical Contexts: A premise might state, “The Berlin
Wall fell in 1989,” with a hypothesis, “Germany was reuniﬁed shortly after.” A model
trained predominantly on Western narratives might correctly infer entailment, but could
struggle with similar inferences in diﬀerent cultural or geopolitical contexts where regional
historical knowledge is less emphasized (Chen et al., 2016).
A.1.4 Classification
A classiﬁcation task in the context of LLMs refers to the process of assigning predeﬁned categories
or labels to a given input text based on its content.
The objective is to automatically identify
the appropriate class or category to which the text belongs, leveraging the patterns and knowledge
learned by the language model (De-Arteaga et al., 2019; Meng et al., 2020).
Bias can be understood as the variation in classiﬁcation outcomes for texts involving diﬀerent
values of sensitive attributes (e.g., gender). An unbiased model should have similar classiﬁcation
outcomes between diﬀerent social groups.
• Gender Bias
– Gendered Language in Job Title Classiﬁcation: When classifying job-related text,
an LLM might associate certain professions with speciﬁc genders based on stereotypical
norms. For instance, “nurse” might be more frequently classiﬁed as female, while “engineer”
might be classiﬁed as male, even when the text does not explicitly mention gender. This
bias can lead to skewed recommendations in hiring algorithms or job description parsing
(Bolukbasi et al., 2016).
– Gendered Pronouns and Name Classiﬁcation: When classifying names or pronouns,
LLMs may exhibit bias by associating certain names or pronouns with speciﬁc gendered
stereotypes. For instance, names like “Alex” or “Jordan” might be classiﬁed with a gen-
dered label (male or female) based on historical or cultural associations rather than the
context provided (Zhao et al., 2017).
• Age Bias
– Sentiment Classiﬁcation Bias Based on Age: A model might classify text written by
older individuals as more negative or less enthusiastic compared to text written by younger
individuals. For instance, if an older person discusses new technology, the model might
incorrectly classify the sentiment as negative or apprehensive, based on the stereotype
that older people are less tech-savvy or more resistant to change (Díaz et al., 2018).
– Bias in Job Application Classiﬁcation: In job application screening, an LLM might
classify older applicants as less suitable for certain roles based on age-related stereotypes.
For example, the model might down-rank resumes of older applicants for tech-related jobs
due to biases that associate youth with innovation and adaptability, while assuming older
candidates are less capable of learning new skills (De-Arteaga et al., 2019).
38

--- Page 39 ---

• Cultural or Regional Bias
– Misclassiﬁcation Due to Cultural Language Variants: A text classiﬁcation model
might incorrectly classify content written in African American Vernacular English (AAVE)
as informal, unprofessional, or even toxic, due to biases against non-standard English
dialects. This can result in discriminatory outcomes, such as the unfair ﬂagging of social
media posts by Black users (Sap et al., 2019a).
– Regional Bias in Political Text Classiﬁcation: A political text classiﬁer might be
biased toward the dominant political ideology of the region where the training data was
sourced. For instance, texts supporting socialist policies might be classiﬁed as “radical”
or “extreme” if the training data predominantly reﬂects a region where socialism is less
accepted (Bender et al., 2021).
A.1.5 Reading comprehension
Reading comprehension in the context of LLMs involves providing the model with a passage of text
and asking it to answer questions about that passage. The objective is to evaluate the model’s
ability to understand and interpret the content of the passage, including facts, concepts, and in-
ferred meanings. The task evaluates the model’s capability to extract relevant information, make
inferences, and provide accurate and contextually appropriate answers based on the text provided
(Rajpurkar et al., 2018).
Extrinsic biases in reading comprehension tasks within LLMs arise when the model’s ability to
understand and answer questions based on a given text is inﬂuenced by external biases embedded in
the training data. These biases can lead to incorrect or biased models favoring certain interpretations
of the text, making incorrect assumptions, or resulting in skewed answers that reﬂect prejudiced
views, rather than a neutral understanding of the text.
• Gender Bias
– Stereotypes in Gendered Activities: In a scenario where the passage mentions, “Alex
is an excellent cook,” a biased model might assume that Alex is female and reﬂect this
in its answers to questions about the passage.
For example, when asked, "What are
her skills?" the model might incorrectly use a gendered pronoun, despite "Alex" being
a gender-neutral name, thereby reﬂecting gender stereotypes associated with cooking
(Webster et al., 2018).
– Assumptions About Gender Roles in Family Settings: A passage might describe
both a mother and a father taking care of children, but when asked, “Who is responsible for
preparing dinner?” a biased model might infer that the mother is responsible, reﬂecting
traditional gender roles (Caliskan et al., 2017).
• Age Bias
– Bias in Health-Related Content: In passages discussing health, a model might in-
correctly infer that certain conditions or concerns (e.g., memory loss, frailty) are more
likely associated with older characters, even when the text is neutral or unrelated to age.
For instance, a passage about a character feeling tired might lead the model to infer an
age-related cause if the character is older (Bolukbasi et al., 2016).
– Misinterpretation of Age-Related Roles: In a passage describing a family scenario,
a reading comprehension model might incorrectly assume that the younger character is
less responsible or that the older character is in a caregiving role, even if the text does
not support these assumptions. This could lead to biased answers to questions about the
characters’ roles or behaviors (Bender and Friedman, 2018).
39

--- Page 40 ---

• Cultural or Regional Bias
– Cultural Context Misinterpretation: A reading comprehension model might misin-
terpret a text that involves culturally speciﬁc practices or norms. For example, if a passage
describes a traditional Japanese tea ceremony, a model trained predominantly on Western
texts might misunderstand the signiﬁcance of the ceremony, interpreting it as a simple
social gathering rather than a ritual with deep cultural meaning (Bender and Friedman,
2018).
– Regional Language Varieties and Dialects: A reading comprehension model might
struggle with understanding regional dialects or non-standard language varieties.
For
instance, a passage written in African American Vernacular English (AAVE) might be
misinterpreted or considered less coherent by the model, leading to incorrect or biased
responses to comprehension questions (Blodgett et al., 2020).
A.1.6 Sentiment Analysis
Sentiment Analysis in the context of LLMs involves identifying the sentiment or emotional tone
expressed in a piece of text. This task typically categorizes text as having a positive, negative, or
neutral sentiment, although more nuanced categorizations (such as speciﬁc emotions like happiness,
anger, or sadness) can also be used. Sentiment analysis is widely applied in areas such as social
media monitoring, customer feedback analysis, and product reviews (Pang et al., 2008).
Extrinsic biases in sentiment analysis tasks within LLMs refer to the unintended and often unfair
inﬂuences that external biases embedded in the training data have on the model’s ability to accurately
interpret the sentiment (whether positive, negative, or neutral) expressed in text. These biases can
cause the model to systematically misclassify sentiment based on factors like the writer’s gender,
race, age, or other demographic characteristics, leading to skewed or unfair sentiment assessments.
• Gender Bias
– Bias in Sentiment Toward Gendered Products or Topics: Sentiment analysis
models might exhibit bias when analyzing reviews or discussions about gendered products.
For example, reviews of products marketed toward women, such as beauty products, might
be categorized with more extreme sentiment (either overly positive or negative) compared
to neutral categorizations for products marketed toward men (Zhao et al., 2017).
– Sentiment Analysis in Gendered Contexts: Sentiment analysis models may misin-
terpret the sentiment of sentences involving gendered contexts. For example, statements
about women’s rights or feminism might be more likely to be categorized as negative, re-
ﬂecting a bias against topics that challenge traditional gender norms (Misiunas and Keyser,
2019).
• Age Bias
– Sentiment Analysis on Age-Related Topics: When analyzing sentiment on topics
related to aging, retirement, or health, sentiment analysis models might display bias by
assuming a more negative sentiment in texts written by older individuals. For example,
discussions about retirement might be categorized as negative due to societal biases about
aging, even if the text is neutral or positive in tone (Burnap and Williams, 2015).
– Stereotyping Language Use by Older Adults: Sentiment analysis models might
misinterpret text written by older adults as more negative or less enthusiastic due to
stereotypical views that older individuals are more conservative or less expressive. For
instance, a review from an older person saying “The movie was good” might be rated as
less positive compared to a more exuberant review from a younger person, even though
both reviews express positive sentiment (Hovy and Søgaard, 2015).
40

--- Page 41 ---

• Cultural or Regional Bias
– Cultural Bias in Sentiment Toward Social Norms: Sentiment analysis might mis-
interpret text related to social norms diﬀerently across cultures. For instance, in some
cultures, discussing money openly is seen as positive and associated with success, while
in others, it might be considered impolite or negative.
A model trained on Western
data might categorize open discussions about money in a non-Western text as negative
(Blodgett and O’Connor, 2017).
– Sentiment in Multilingual Contexts:
In multilingual regions, a sentiment analy-
sis model might incorrectly categorize sentiment when it encounters code-switching (the
practice of alternating between two or more languages or dialects). For instance, in Latin
America, code-switching between Spanish and indigenous languages might lead to incor-
rect sentiment assessments if the model is biased towards Spanish and fails to interpret
the sentiment conveyed in the indigenous language correctly (Hovy and Søgaard, 2015).
A.2 Natural Language Generation (NLG) tasks
NLG tasks refer to downstream tasks in which the model generates coherent, contextually relevant,
and human-like text based on a given input or set of instructions (Chang et al., 2024). The objective
of NLG is to produce text that is not only grammatically correct but also semantically meaningful
and appropriate for the context in which it is generated.
A.2.1 Question Answering
Question Answering (QA) tasks in the context of LLMs focus on the model’s ability to provide
accurate and relevant answers to questions based on a given text or knowledge base.
It is an
essential task in the domain of human-computer interaction, and it has been extensively used in
various situations such as search engines and chatbots (Zadeh, 2006; Li et al., 2024b). The goal of
QA is to extract, infer, or generate responses that directly address the query, leveraging the model’s
understanding of language, context, and content (Rajpurkar et al., 2016).
Extrinsic biases in QA tasks occur when the model’s responses are inﬂuenced by external biases
embedded in the training data on the model’s ability to provide accurate and fair answers to questions.
These biases can lead to skewed, misleading, unfair, inaccurate, or discriminatory answers based
on gender, race, age, culture, or other demographic factors, rather than providing a neutral and
contextually appropriate response.
• Gender Bias
– Gender Bias in Answer Generation:
When asked, “What should a good leader
do?”, the model might provide examples or language that align with stereotypically male
attributes (e.g., “He should be assertive and decisive”), thereby implying that leadership
qualities are inherently male. If asked about nurturing roles, the model might default to
female pronouns and qualities, reinforcing gendered stereotypes (Zhao et al., 2018a).
– Bias in Answering Ambiguous Gender Questions: For a question like “What does
a typical manager do?” where gender is not speciﬁed, a biased model might generate an
answer using male pronouns (“He manages the team...”), reﬂecting an assumption that
managers are typically male. This bias can also appear in reverse, where certain roles like
teaching or nursing might default to female pronouns (Webster et al., 2018).
• Age Bias
– Stereotypical Answers About Aging: If asked, “What are the best activities for
elderly people?” a model might focus on sedentary activities like knitting or watching
41

--- Page 42 ---

TV, neglecting more active pursuits like hiking, traveling, or volunteering. This reﬂects a
bias that older adults are less capable of engaging in physically demanding or adventurous
activities (Caliskan et al., 2017).
– Negative Bias Toward Youth: If a question is posed like, “Are young people capable
of managing a company?” a biased model might respond with, “They may lack the experi-
ence needed for such a role,” reﬂecting stereotypes that associate youth with inexperience,
despite many young people successfully managing companies (Bolukbasi et al., 2016).
• Cultural or Regional Bias
– Bias in Answering Culturally Speciﬁc Questions: When asked, “What is the most
popular sport in the world?” a biased QA system might answer “American football” if
trained predominantly on data from the United States, ignoring that globally, soccer
(football) is more widely popular. This reﬂects a bias toward regional popularity rather
than global knowledge (Gardner et al., 2018).
– Language and Regional Bias in Answer Accuracy:
A QA system might per-
form better when answering questions in or about regions and languages that are well-
represented in its training data. For example, questions about European history or in
English might be answered more accurately than questions about African history or in
less commonly spoken languages (Kwiatkowski et al., 2019).
A.2.2 Sentence Completions
Sentence Completion tasks in the context of LLMs involve predicting and generating the next word or
sequence of words to complete a partially provided sentence. The goal of these tasks is to produce a
grammatically correct and contextually appropriate continuation that aligns with the preceding text.
Sentence completion is a fundamental capability in many NLP applications, such as autocomplete
features and writing assistants (Radford et al., 2019).
Extrinsic biases in sentence completion tasks within LLMs occur when the model’s predictions for
completing a sentence are inﬂuenced by external biases embedded in the training data on the model’s
ability to generate appropriate and unbiased sentence continuations. This type of bias can cause
the model to complete sentences in ways that reinforce harmful stereotypes, perpetuate prejudice,
or reﬂect biased assumptions about gender, race, age, culture, or other demographic factors.
• Gender Bias
– Gender Bias in Descriptions of Physical Appearance: If the sentence starts with
“She looked at herself in the mirror and...” a biased model might complete it with “...ad-
justed her makeup,” whereas “He looked at himself in the mirror and...” might be com-
pleted with “...straightened his tie.” This reﬂects the stereotype that women are more
concerned with appearance and men with professionalism (Caliskan et al., 2017).
– Gender Bias in Personal Attributes: If prompted with “She is very...” a model might
complete the sentence with adjectives like “emotional,” “beautiful,” or “caring,” while
“He is very...”
might be completed with “strong,” “intelligent,” or “ambitious.”
These
completions reﬂect stereotypical views of women as being more emotional and men as
being more rational or powerful (Zhao et al., 2017).
• Age Bias
– Activity and Lifestyle Assumptions: For a prompt like “At 25, Jenny enjoys,” a bi-
ased model might complete the sentence with “partying and going out every night,” based
on the stereotype that young adults are primarily interested in nightlife and socializing,
ignoring the diversity of interests in this age group (Garg et al., 2018).
42

--- Page 43 ---

– Learning and Education Stereotypes: Given the prompt “At 50, Mark decided to,” a
biased model might complete it with “go back to school to ﬁnally get his degree,” assuming
that older adults are “catching up” on education rather than pursuing lifelong learning or
new academic challenges (Sun et al., 2019).
• Cultural or Regional Bias
– Cultural Stereotyping in Sentence Completion: If the model is given a sentence
like “In Japan, people often eat,” it might complete with “sushi,” reﬂecting a cultural
stereotype that overemphasizes a speciﬁc aspect of Japanese cuisine, while ignoring the
diversity of food in Japanese culture. Similarly, completing “In Mexico, people celebrate”
with “Cinco de Mayo” might reinforce a limited and stereotypical understanding of Mexi-
can culture (Hendricks et al., 2018).
– Regional Bias in Place-Based Completions:
For the sentence “In Africa, many
people live in,” the model might complete with “villages,” reﬂecting a regional bias that
assumes rural living conditions are more common across an entire continent, despite the
presence of large urban areas. This completion overlooks the diversity of living environ-
ments in diﬀerent African countries and regions (Birhane and Prabhu, 2021).
A.2.3 Conversational
Conversational tasks in the context of LLMs involve generating, understanding, and maintaining
coherent dialogue with users. These tasks are crucial for applications like chatbots, virtual assis-
tants, and customer service automation. Conversational tasks typically require the model to not
only generate contextually appropriate responses but also to track the context of the conversation,
understand user intent, manage the dialogue ﬂow, and sometimes incorporate external knowledge
or personalized information (Zhang et al., 2019b).
Extrinsic biases in conversational tasks within LLMs refer to the unintended inﬂuence of ex-
ternal biases on the model’s responses during a conversation. These biases can cause the model
to generate responses that reﬂect prejudiced views, reinforce stereotypes, or unfairly favor certain
perspectives, leading to skewed, insensitive, or inappropriate conversational outcomes, which may
negatively impact user experience.
• Gender Bias
– Stereotypical Responses Based on Gendered Prompts: When given a prompt
like “Describe a nurse” versus “Describe a doctor,” an LLM might generate responses
that reinforce gender stereotypes.
For example, it might describe a nurse as “caring,
nurturing, and female,” while describing a doctor as “authoritative, knowledgeable, and
male,” despite no gender being speciﬁed in the prompts (Bolukbasi et al., 2016).
– Bias in Gendered Interactions:
In a customer service chatbot, the model might
respond more politely or deferentially to queries assumed to be from female users based
on gender cues in the text (like names or pronouns), while responding more assertively
or formally to male users. This reﬂects gendered expectations of communication styles
(Hitsch et al., 2010).
• Age Bias
– Assumptions About Technological Savvy: In a conversation where the user is dis-
cussing technology, a biased model might assume the user is younger if they express
familiarity with tech jargon or concepts. Conversely, if the user asks for help with ba-
sic technology, the model might assume the user is older and potentially provide overly
simplistic explanations, which could be patronizing (Hovy and Søgaard, 2015).
43

--- Page 44 ---

– Bias in Addressing Age-related Concerns:
In a scenario where a user asks for
advice on starting a new career later in life, a biased model might discourage them by
emphasizing the challenges of changing careers at an older age. For instance, if the user
says, “I’m thinking of switching careers at 50,” the model might respond with comments
like, “It might be diﬃcult at your age,” reﬂecting a bias that older individuals face more
barriers in the job market (Wagner et al., 2016).
• Cultural or Regional Bias
– Culturally Inappropriate Responses: A conversational LLM might provide responses
that are culturally inappropriate or insensitive due to a lack of understanding of cultural
norms.
For example, if a user from Japan mentions “visiting a shrine,” a culturally
biased model might respond with a suggestion that is more aligned with Western religious
practices, failing to acknowledge the cultural signiﬁcance of shrines in Japanese culture
(Hovy and Spruit, 2016).
– Bias in Handling Regional Topics: A conversational AI might be biased in how it
handles topics related to certain regions. For instance, if asked about news in Africa, the
model might focus disproportionately on negative topics like conﬂict or poverty, reﬂecting
a bias in the training data, while similar questions about Europe might elicit more varied
and positive topics (Gebru et al., 2021).
A.2.4 Recommender Systems
Recommender Systems in the context of LLMs are designed to predict and suggest personalized
content or items of interest to users based on their preferences, behavior, or contextual information.
These systems analyze patterns in user data, such as past interactions, preferences, or demographic
information, to provide personalized recommendations, such as suggesting movies, products, books,
or articles that the user might enjoy or ﬁnd useful (Zhang et al., 2019a; Hua et al., 2023).
Extrinsic biases in recommender systems within LLMs occur when the model’s recommendations
are inﬂuenced by external biases present in the training data. This bias can result in the model
making recommendations that disproportionately favor certain groups, products, or content types
over others based on factors like gender, race, age, culture, or other demographic characteristics,
rather than providing neutral and personalized suggestions.
• Gender Bias
– Product Recommendations Based on Gender Stereotypes: A recommender sys-
tem might suggest beauty products, fashion items, or household goods primarily to women
while recommending electronics, tools, or sports equipment predominantly to men. This
bias reinforces traditional gender roles and can lead to irrelevant or unappealing recom-
mendations for users whose interests do not align with these stereotypes (Ekstrand et al.,
2018).
– Career and Education Recommendations: A job or education recommender system
might suggest STEM (Science, Technology, Engineering, and Mathematics) careers more
often to male users while recommending roles in healthcare, education, or the arts more
frequently to female users. This bias can perpetuate gender disparities in career choices
and educational opportunities (Chen et al., 2019).
• Age Bias
– Age-Related Product Recommendations: A recommender system might automati-
cally suggest health-related products, such as supplements or exercise equipment, to older
users while recommending tech gadgets or trendy fashion items to younger users. These
44

--- Page 45 ---

recommendations may not accurately reﬂect the individual’s interests but are based on
age-related stereotypes (Biega et al., 2018).
– Media and Entertainment Recommendations: A recommender system might as-
sume that older users prefer classic movies or oldies music, while younger users prefer
contemporary pop culture content. This can result in older users being recommended
content that does not reﬂect their actual tastes if they have a preference for contempo-
rary media, and younger users missing out on discovering older, classic content they might
enjoy (Burke et al., 2018).
• Cultural or Regional Bias
– Regional Bias in News and Information Recommendations: A news recommender
system might prioritize local or regional news from dominant cultures, under-representing
or completely ignoring news from minority regions or less dominant cultures. For instance,
users in a country might predominantly receive news recommendations about urban cen-
ters and mainstream political issues, while rural or indigenous issues are marginalized
(Karimi et al., 2018).
– Bias in Language and Cultural Content Recommendations:
A recommender
system might prioritize content in the dominant language of a region, leading to a lack
of recommendations for content in minority languages. For example, in a multilingual
country, the system might recommend mostly English-language content, marginalizing
content in local languages like Tamil, Welsh, or Basque (Lakew et al., 2018).
A.2.5 Machine Translation
Machine Translation (MT) tasks in the context of LLMs involve the automatic translation of text
from one language to another. The aim is to produce a translation that accurately conveys the
meaning of the original text while maintaining grammatical correctness, ﬂuency, and cultural appro-
priateness in the target language. Machine Translation systems are trained on large parallel corpora,
which contain pairs of sentences in diﬀerent languages that correspond to each other. These models
learn patterns and structures in both languages to generate translations (Vaswani, 2017).
Extrinsic biases in Machine Translation (MT) tasks within LLMs occur when the model’s trans-
lations are inﬂuenced by external biases embedded in the training data. Such biases can lead to
translations that reﬂect cultural, gender, racial, or regional stereotypes, resulting in unfair or inac-
curate translations that either misrepresent the original text’s meaning or that reinforce harmful
stereotypes.
• Gender Bias
– Gendered Language Mismatch: When translating from a gender-neutral language
like Turkish or Finnish into a gendered language like English or Spanish, the model might
introduce gender bias by assigning gendered pronouns or roles based on stereotypes. For
example, the Turkish sentence “O bir doktor” (which means “He/She is a doctor”) might
be translated into English as “He is a doctor,” reﬂecting the stereotype that doctors are
male (Prates et al., 2020).
– Gender Stereotyping in Occupational Translations: When translating sentences
that involve professions, the model might incorrectly assign gendered pronouns based
on stereotypes. For instance, translating the phrase “The nurse” from a gender-neutral
language might result in “La enfermera” (female nurse) in Spanish, while “The engineer”
might be translated as “El ingeniero” (male engineer), even if the original language did
not specify gender (Neri et al., 2020).
• Age Bias
45

--- Page 46 ---

– Bias in Addressing Older Adults: A machine translation system might translate
sentences in a way that condescends to older adults, reﬂecting societal biases. For example,
translating “The elderly person learned to use a smartphone” might introduce a tone or
wording in the target language that implies surprise or patronization, even if the original
sentence was neutral (Caliskan et al., 2017).
– Translation of Age-Related Idioms: When translating age-related idioms or expres-
sions, a biased translation system might reinforce negative stereotypes.
For instance,
translating a phrase like “old people are slow” into another language might retain the
negative connotation or even intensify it if the target language has a stronger cultural
bias against the elderly. (Hovy and Søgaard, 2015).
• Cultural or Regional Bias
– Cultural Nuance Loss: Cultural idioms, proverbs, or colloquial phrases often lose their
meaning or are mistranslated when a model does not consider the cultural context. For
example, the English idiom “It’s raining cats and dogs” could be literally translated into
another language, resulting in a confusing or meaningless phrase in that target culture.
A culturally aware model would translate it into a local equivalent, such as “Il pleut des
cordes” (It’s raining ropes) in French (Vanmassenhove et al., 2019).
– Bias Toward Dominant Cultures: A machine translation system might favor trans-
lations that align with Western cultural norms over those of less dominant cultures. For
instance, translating phrases related to food, clothing, or customs might reﬂect West-
ern standards, even when the source text belongs to a non-Western culture. An example
could be translating a traditional Chinese clothing item, “Qipao,” simply as “dress,” which
dilutes the cultural signiﬁcance (Sennrich, 2016).
A.2.6 Summarization
Summarization in the context of LLMs involves generating a concise and coherent summary of a
longer text while preserving the key information and main points. The goal of summarization is to
shorten the text while preserving its essential meaning and context (Nallapati et al., 2016).
Extrinsic biases in summarization tasks within LLMs refer to biases that stem from external
inﬂuences present in the training data on the way a model generates summaries.
These biases
can aﬀect how the model selects and condenses information, potentially leading to skewed, unfair,
or incomplete summaries that disproportionately emphasize or omit certain information based on
gender, race, age, or other characteristics, rather than providing a neutral summary of the content.
• Gender Bias
– Diﬀerential Emphasis on Roles: In summarizing biographies or obituaries, a model
might emphasize traditional gender roles. For example, summaries of women’s lives might
focus more on their roles as wives and mothers, while summaries of men’s lives might
emphasize their careers or public achievements, even if the original text gave equal im-
portance to both aspects (Bender and Friedman, 2018).
– Selective Emphasis on Gendered Information: In summarizing a news article, a bi-
ased model might disproportionately emphasize gender-speciﬁc details that are not central
to the story. For instance, when summarizing an article about a successful entrepreneur,
the model might overemphasize details about the entrepreneur’s gender or appearance if
the subject is female while focusing on achievements and business strategies if the sub-
ject is male. This kind of bias reinforces gender stereotypes and can skew the perceived
importance of certain information (Otterbacher et al., 2017).
• Age Bias
46

--- Page 47 ---

– Bias in Summarizing Content for Diﬀerent Age Groups: When summarizing
content aimed at diﬀerent age groups, a model might simplify or alter the tone of content
intended for younger audiences in a way that reﬂects condescension or a lack of complexity.
For instance, a model might overly simplify a summary of educational content intended for
teenagers, assuming they cannot handle complex information (Obermeyer et al., 2019).
– Omission of Contributions Based on Age: When summarizing a report or article
that includes contributions from both younger and older individuals, a biased summariza-
tion model might disproportionately highlight the contributions of younger people while
downplaying or omitting the contributions of older individuals. For example, in summa-
rizing a collaborative project, the model might emphasize the innovative ideas of younger
team members while neglecting the experience and insights provided by older members
(Bender and Friedman, 2018).
• Cultural or Regional Bias
– Omission of Culturally Signiﬁcant Details: A summarization model might omit
culturally signiﬁcant details that are not widely understood in the model’s primary train-
ing data. For instance, if summarizing a text about a traditional festival like Diwali, the
model might focus on generic elements like “a festival with lights” while omitting impor-
tant cultural and religious aspects such as the signiﬁcance of the festival in Hinduism
(Shen et al., 2017).
– Bias Toward Western Narratives: When summarizing global news articles, a model
might prioritize Western perspectives or narratives, underplaying or omitting the view-
points from non-Western cultures. For example, in summarizing an article about a politi-
cal conﬂict in the Middle East, the model might focus on the perspectives of Western gov-
ernments and omit the perspectives of local populations (Perez-Beltrachini and Lapata,
2022).
These examples illustrate how extrinsic biases in LLMs can impact the accuracy, fairness, and
potential for discrimination, often reinforcing harmful stereotypes and societal biases. Extrinsic bias
is a signiﬁcant concern because it can lead to unfair and discriminatory outcomes in applications like
hiring, lending, and content moderation. Mitigating extrinsic biases in LLMs requires a comprehen-
sive strategy that includes the use of diverse, representative, and balanced training data, inclusive
labeling practices, the implementation of debiasing techniques, and continuous evaluation to ensure
fair and accurate language processing.
47

```
