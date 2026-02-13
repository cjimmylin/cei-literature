---
title: "2024-retrieved-Evaluation of AI Ethics Tools in Language Models A Developers' - PDF Extract"
source_pdf: "2024-retrieved-Evaluation of AI Ethics Tools in Language Models A Developers'.pdf"
pages: 56
extracted_at: "2026-02-13T09:50:31.164630"
---

# PDF Extract: 2024-retrieved-Evaluation of AI Ethics Tools in Language Models A Developers'

**Source PDF:** 2024-retrieved-Evaluation of AI Ethics Tools in Language Models A Developers'.pdf
**Total Pages:** 56

---

## Content

```
--- Page 1 ---

Evaluation of AI Ethics Tools in Language Models: A
Developers’ Perspective Case Study
Jhessica Silva1*, Diego A. B. Moreira1, Gabriel O. dos Santos1, Alef Ferreira2,
Helena Maia1, Sandra Avila1*, Helio Pedrini1*
1Instituto de Computa¸c˜ao, Universidade Estadual de Campinas (UNICAMP), Campinas,
S˜ao Paulo, Brazil.
2Instituto de Inform´atica, Universidade Federal de Goi´as (UFG), Goiˆania, Goi´as, Brazil.
*Corresponding author(s). E-mail(s): jhessica.silva@ic.unicamp.br; sandra@ic.unicamp.br;
helio@ic.unicamp.br;
Abstract
In Artificial Intelligence (AI), language models have gained significant importance due to the widespread
adoption of systems capable of simulating realistic conversations with humans through text generation.
Because of their impact on society, developing and deploying these language models must be done respon-
sibly, with attention to their negative impacts and possible harms. In this scenario, the number of AI
Ethics Tools (AIETs) publications has recently increased. These AIETs are designed to help developers,
companies, governments, and other stakeholders establish trust, transparency, and responsibility with
their technologies by bringing accepted values to guide AI’s design, development, and use stages. How-
ever, many AIETs lack good documentation, examples of use, and proof of their effectiveness in practice.
This paper presents a methodology for evaluating AIETs in language models. Our approach involved an
extensive literature survey on 213 AIETs, and after applying inclusion and exclusion criteria, we selected
four AIETs: Model Cards, ALTAI, FactSheets, and Harms Modeling. For evaluation, we applied AIETs
to language models developed for the Portuguese language, conducting 35 hours of interviews with their
developers. The evaluation considered the developers’ perspective on the AIETs’ use and quality in help-
ing to identify ethical considerations about their model. The results suggest that the applied AIETs serve
as a guide for formulating general ethical considerations about language models. However, we note that
they do not address unique aspects of these models, such as idiomatic expressions. Additionally, these
AIETs did not help to identify potential negative impacts of models for the Portuguese language.
Keywords: AI Ethics Tools, Language Models, Ethical Considerations, Portuguese Language.
1 Introduction
Language models have been reshaping how we interact with machines thanks to popularizing systems capable
of simulating realistic conversations. This popularization has occurred mainly with the launch of Chat-
GPT [1], which has a simple interface for user interaction. These models are trained “on the task of string
prediction, whether it operates over characters, words or sentences, and sequentially or not” [2], given a
previous context. Typically, language models take text as input to predict new strings.
Researchers from various fields have warned of the ethical threats these models pose. Hovy and Spruit [3]
show that the social impacts of language models range from the exclusion of people due to demographic biases
present in the data used for training to the generation of erroneous or false answers due to overgeneralization
of the models during training. Bender et al. [4] warn that large language models trained with large datasets
have a high environmental and financial cost and—yet—do not guarantee diversity, propagating worrying
1
arXiv:2512.15791v1  [cs.CY]  16 Dec 2025

--- Page 2 ---

biases such as stereotypical associations or negative feelings towards specific groups. Weidinger et al. [5]
conducted significant work investigating the ethical and social risks of harm caused by language models and
pointed out 21 potential risks.
In the context of the Portuguese, a language with medium-computational resources1, as it has little data
available for use in AI technologies, the most multilingual language models while lacking competitiveness [7],
also fail to adequately represent the cultural, historical, and social nuances of the population represented
by the language [4]. This deficiency is largely due to the predominant use of English-language data during
training, with minimal data from other languages incorporated [8]. Particularly, when it comes to Portuguese
expert models, although they perform better, the vast majority are trained with textual data translated from
English. Consequently, while these models target Portuguese speakers, they tend to replicate all aspects of
the global north. They may perpetuate errors and biases arising from automatic translation processes [7, 9].
These points show the importance of ethically evaluating language models and providing end users with
comprehensive documentation that explains the associated challenges of the technology. However, several
current models are only being advertised accompanied by “technical reports” that lack substantial infor-
mation about the model’s training processes, architecture, or ethical implications. One of the reasons for
this is that many of these models are being proposed by computer professionals without the support of
a multidisciplinary team. Unfortunately, many of these computer professionals finish their basic training
without a solid knowledge of subjects related to ethics and technologies [10, 11]. Consequently, they usually
do not have a basis for how to carry out ethical formulations about the technologies they propose. On the
other hand, specific conferences such as Conference on Fairness, Accountability, and Transparency (FAccT),
Empirical Methods in Natural Language Processing (EMNLP), and Conference on Neural Information Pro-
cessing Systems (NeurIPS) have begun to include dedicated sections for ethical considerations in their calls
for papers, showing the importance of reflecting on ethics in technology research. Due to the impacts and
potential risks that language models can generate for society, these models must be developed and deployed
responsibly to mitigate these threats.
In light of the presented challenges, this paper aims to contribute to the urgent open discussions in our
society about ethics and AI technologies. To this end, we conducted a case study on the use of AI Ethics
Tools (AIETs) [12–15] to assess the ethical considerations of language models developed in Portuguese. This
study was based on interviews with developers from four language models developed for the Portuguese
language using AIETs as a guide. The AIETs are practical methods that can be applied during the design,
development, and use of AI to identify potential ethical problems that the technology may generate and
propose ways to mitigate these problems. AIETs can be a starting point for designing and developing more
ethical AI technologies, especially language models, that aim to mitigate biases, avoid spreading inequalities,
and prevent the malicious use of their numerous capabilities.
The main contributions of our paper are as follows:
• We introduced a methodology to select and evaluate AIETs in language models carefully. For this, we
conducted an extensive literature survey of AIETs. We applied inclusion and exclusion criteria to filter
all 213 found AIETs, resulting in four selected AIETs;
• We conducted a case study where we applied the selected AIETs through interviews with the developers
of language models. To our knowledge, this is the first study to evaluate the use of AIETs in language
models;
• We introduced a process to assess AIETs from the developers’ perspective. We designed a question-
naire to extract developers’ perceptions of the analyzed AIETs to achieve this. We aimed to evaluate
the usability and effectiveness of AIETs in helping developers of language models to identify ethical
considerations about the developed model by comparing the results of each AIET with the others.
The remainder of this paper is structured as follows. Section 2 overviews AIETs and the works most
closely related to this paper. Section 3 presents the methodology adopted in this study. Section 4 presents
the results and discusses the developers’ perspectives and opinions on the AIETs applied in an interview
format. Section 5 presents the limitations and future work of this study. Finally, Section 6 presents the
conclusions and the ethical considerations of this study.
1Despite Portuguese being ranked among the top ten languages globally based on the number of native speakers, it is considered a
medium-resource language within the context of AI [6].
2

--- Page 3 ---

2 Background and Related Work
This section presents a brief overview of AIETs and the most closely works related to this paper. Section 2.1
provides the related concepts about AIETs, whereas Section 2.2 presents an overview of the works that
analyze AIETs as a whole. We adopt the term AI Ethics Tools (AIETs), as Ayling and Chapman [16], to
refer to all tools, toolkits, methods, frameworks, and research that aim to promote AI ethics throughout the
AI life cycle. In some works, other terms are also used to refer to AIETs, such as AI ethics toolkits [17],
Ethical AI frameworks [18], and AI ethics frameworks [19].
2.1 AIETs background
The AIETs are practical methods that can be utilized during the design, development, and use stages of AI
technologies to identify potential ethical issues that the technology may generate and, in some cases, propose
strategies for mitigating these problems. In recent years, researchers and companies in the public and private
sectors have proposed several AIETs to evaluate ethical principles. Several papers analyze these AIETs,
presenting an overview of their applications and impacts and the implications associated with translating
ethical principles into practical tools for use in AI technologies [16–18, 20–22].
The AIETs currently available are diverse, with different proposals and approaches, differing according
to the stage of the AI technology life-cycle where they can be applied (problem specification, design, testing,
and use stages) and according to their (i) categories, (ii) final objectives, (iii) topics and principles covered
by each one, and (iv) target audience [16, 18, 21]. In addition, AIETs can be applied to datasets and/or to
the developed models. Table 1 shows examples of Ethical Considerations and AIETs by AI life-cycle stages
and Table 2 shows examples of AIETs by each type of classification mentioned.
Table 1 Examples of ethical considerations and AIETs by stages in the AI life-cycle
Stage
Examples of Ethical Considerations
Examples of AIETs
Problem
specification
• Responsibility (Have the requirements
been clearly documented?)
• Non-maleficence (Who are the future users
and how will they be affected?)
• Sustainability (How might this AI impact
the environment?)
• IDEO’s AI Ethics Cards [23]
• Corporate Digital
Responsibility [24]
• Ethics for Designers [25]
Design
• Privacy (Has personal data been
anonymized?)
• Freedom and Autonomy (Was the data
collected with consent?)
• Beneficence (Is the AI development
process aimed at the well-being of users?)
• Datasheets for Datasets [26]
• Data statements for NLP [27]
• The Dataset Nutrition Label [28]
Testing
• Transparency (Are the results explainable
or interpretable?)
• Privacy (Can AI generate confidential
information?)
• Justice and Fairness (Did AI perform
differently for any groups?)
• Aequitas [29]
• AI Explainability 360 Toolkit [30]
• What-if Tool [31]
Use
• Security and Safety (Is the AI robust
against adversary attacks?)
• Trust (Can users trust AI results?)
• Dignity (Does AI respect users’ values?)
• Model Cards for Model
Reporting [12]
• Harms Modeling [14]
• ALTAI [13]
As mentioned earlier, AIETs aim to help developers, researchers, companies, governments, and other
stakeholders create more ethical AIs. However, although promising, many AIETs lack good documentation,
examples of use, evidence of their effectiveness, and are not yet well adopted by their target audience, as
well as being proposed for AIs in general [19, 20]. This paper practically investigates these issues, applying
AIETs to language models. It seeks to understand the effectiveness of AIETs in mapping ethical issues
already identified by the literature on these models. We assess interviews with the developers of language
models proposed for the Portuguese language, the usability of AIETs, their readability, whether they can
guide ethical thinking about technology, and the possible future adoption by those interviewed.
3

--- Page 4 ---

Table 2 Examples of AIETs by categories, final objectives, principles and target audience
AIET Type
Examples of AIETs
Categories
Checklists or
Questionnaires
• Datasheets for Datasets [26]
• FactSheets: Increasing Trust in AI Services through Supplier’s
Declarations of Conformity [15]
Frameworks
• AI-RFX Procurement Framework [32]
• Zeno: An Interactive Framework for Behavioral Evaluation of
Machine Learning [33]
Metrics
• LIME – Local Interpretable Model-Agnostic Explanations [34]
• SHAP – SHapley Additive exPlanations [35]
Codes and
Algorithm
• BOLD: Dataset and Metrics for Measuring Biases in Open-Ended
Language Generation [36]
• XAI – An eXplainability toolbox for machine learning [37]
Objectives
Audit
• Auditing LLMs: A Three-Layered Approach [38]
• Closing the AI Accountability Gap: Defining an end-to-end
framework for internal algorithmic auditing [39]
Requirements
assessment
and/or
Supervision
• ALTAI – The Assessment List for Trustworthy Artificial
Intelligence [13]
• A seven-layer model with checklists for standardising fairness
assessment throughout the AI lifecycle [40]
Risk
assessment
• Harms Modeling [14]
• PROBAST: A Tool to Assess the Risk of Bias and Applicability of
Prediction Model Studies [41]
Documentations
• Model Cards for Model Reporting [12]
• The Dataset Nutrition Label [28]
Case study or
Tutorial
• Judgment Call the Game: Using Value Sensitive Design and Design
Fiction to Surface Ethical Concerns Related to Technology [42]
• Community jury [43]
Technical
• TensorFlow Privacy [44]
• Adversarial Robustness Toolbox [45]
Principles
Transparency
• AI Explainability 360 Toolkit [30]
Responsibility
• Closing the AI accountability gap: Defining an end-to-end framework
for internal algorithmic auditing [39]
Beneficence
• Consequence Scanning: An Agile event for Responsible Innovators [46]
Dignity
• Equity Evaluation Corpus [47]
Privacy
• Should I disclose my dataset? Caveats between reproducibility and
individual data rights [48]
Audience
Data Scientist
• Aequitas: A Bias and Fairness Audit Toolkit [29]
Examiners
• TuringBox: An Experimental Platform for the Evaluation of AI
Systems [49]
Students
• AI Audit: A Card Game to Reflect on Everyday AI Systems [50]
Observations: Some AIETs can take on more than one classification; AIETs can have more than one
objective, ethical principle or target audience, although the table shows only one; Examples have not been
provided for all the existing principles and possible target audiences.
All AIETs analyzed in this research—Model Cards by Mitchell et al. [12], ALTAI by AI HLEG [13],
FactSheets by Arnold et al. [15], and Harms Modeling by Microsoft [14]—fall into the Checklists and Ques-
tionnaires category and are applied exclusively in the use stage of the AI life-cycle, as shown in Fig. 1. In
other words, these AIETs consist of lists of criteria, checks, or questions that guide the ethical analysis and
decision-making related to AI during the deployment and use stages. The primary objective of AIETs in this
category is to offer guidance on various ethical considerations associated with AI, including details about
datasets, the components of AI systems, requirements, system behaviors, potential biases, the impacts of
the technology, and raising ethical considerations.
2.2 Overview of AIETs
This section presents the most closely works related to this paper, providing an overview of the works that
analyze AIETs as a whole. Several AIETs have been proposed to evaluate ethical principles in practice. These
principles have been extensively discussed in the literature [51–55]. Jobin et al. [56] carried out a significant
4

--- Page 5 ---

Use Stage
Design Stage
Testing Stage
 
Problem
specification
Dataset
construction
Data
understanding
Data preparation
Modeling
Evaluation
Monitoring
Deployment
- Checklists
- Frameworks
- Metrics
- Codes
- Checklists
- Frameworks
- Metrics
- Checklists
- Frameworks
- Checklists
- Frameworks
- Audit
- Risk assessment
- Documentations
- Requirements
assessment
- Risk assessment
- Technical
- Requirements
assessment
- Case study
- Requirements
assessment
- Technical
Fig. 1 AIETs can be applied throughout the AI life-cycle, from problem specification to the use stage. Colored hexagons
indicate examples of AIETs types that can be applied in each of the stages. In purple, full border, the categories of AIETs.
In blue, dotted border, the objectives. The AIETs analyzed in this study are exclusively applied in the use stage of the AI
life-cycle, indicated by the solid red border
work with a comprehensive overview of 84 AI ethics guidelines2. The results indicate that the guidelines
converge on five ethical principles: transparency, justice and fairness, non-maleficence, responsibility, and
privacy. Other less recurrent principles are beneficence, freedom and autonomy, trust, sustainability, dignity,
and solidarity. Jobin et al. [56] also discussed that although there is convergence around some principles,
the analysis revealed significant semantic and conceptual divergences in how these ethical principles are
interpreted and in the specific recommendations or areas of concern derived from each one. Ryan and Stahl
[57] provided a compilation of the content of the normative requirements arising from these guidelines for a
better understanding of the codes of ethics included in each principle.
In recent years, some papers have significantly discussed about the implications of translating ethical
principles into viable AIETs for use in AI technologies and their impacts, and the following are the most
related to this paper.
Morley et al. [20] were among the first to present a typology of over 100 AIETs for applying ethics in AI,
discussing ways that ethical principles could be implemented in AI technologies. The authors categorized
the AIETs into five ethical AI principles: beneficence, non-maleficence, autonomy, justice, and explainability,
and by application stages in the AI life-cycle. They discuss “how efforts to date have been too focused on
the ‘what’ of ethical AI (i.e., debates about principles and codes of conduct) and not enough on the ‘how’
of applied ethics” and point out that AIETs offer little help on how to use them in practice, have limited
documentation and require a high level of skill to use.
Prem [18] extended the work of Morley et al. [20] by systematically analyzing AIETs from an operational
and implementation perspective. The author classified AIETs in terms of their categories (e.g., checklists,
declarations, audits, and metrics), their implementations (e.g., algorithms, libraries), and the ethical prob-
lems they aim to solve (general ethical aspects, privacy, fairness and bias, explainability, accountability,
transparency, correctness and accuracy, diversity, robustness, and reproducibility). Prem also discussed the
complexity involved in putting the principles into practice by developers since the principles are complex
2Here, as a way of presenting concepts related to this paper, one of the main works in the area was presented, carried out by Jobin
et al. [56]. However, the work by Jobin et al. has already been updated by other authors, such as Corrˆea et al. [55], who have added more
guidelines to the review (200–until 2023). However, the results are close and the discussions pointed out by Jobin et al. are still current.
5

--- Page 6 ---

and challenging to implement (“For example, it remains unclear what ‘interpretability’ means and how it
should be implemented.”).
Ayling and Chapman [16] presented a typology with 39 AIETs to apply ethics in AI, as does Morley
et al. [20], aiming to translate ethical principles into practice. What sets this work apart is the presentation
of AIETs’ analyses based on the sectors that develop and use them, the support for various stakeholders, and
the categories and stages of the AI life-cycle in which they can be applied. The authors also contrasted that
AIETs emerged in a scenario with no regulations for AI technologies, which could minimize their adoption
and application.
Wong et al. [17] qualitatively analyzed 27 AIETs to critically examine how the work of ethics is imagined
and how these AIETs support it. The authors’ analysis focused on the discourses that AIETs rely on when
talking about ethical issues and their implications, and finally, they presented three recommendations to
improve the way AIETs support AI ethics: “ (1) provide support for the non-technical dimensions of AI ethics
work; (2) support the work of engaging with stakeholders from non-technical backgrounds; (3) structure the
work of AI ethics as a problem for collective action.”.
The four papers presented previously discuss the gaps in putting principles into practice through the use
of AIETs and carry out a general assessment of these AIETs and their specifications, providing insights into
how ethics currently being applied in AI technologies. However, analyses were conducted only theoretically
and did not present practical research and comparisons.
Qiang et al. [19], as far as we know, were the first authors to assess AIETs practically in a comparative case
study. The authors compared four AIETs—Foresight into AI Ethics Toolkit [58], Guidelines for Trustworthy
AI [59], Ethics and Algorithms Toolkit [60], and Algorithmic Impact Assessment [61]—from the perspectives
of an auditor conducting an AI ethics risk assessment for a company and that of the company receiving the
AIETs’ final documentation. The authors discussed the lack of clarity and explanations of AIETs outcomes.
In addition, the authors pointed out the need for more standardization in the results of AIETs, which makes
their use more complicated. The authors applied the AIETs to an AI that was still being developed, and the
results suggest that each analyzed AIET provides a different benefit and that there is no unique solution
to address all AI ethical issues adequately. The authors also pointed out that, to better adopt AIETs, it is
necessary to specify the suitability and expected benefits of existing AIETs.
This paper is related to the work developed by Qiang et al. [19]. However, their studies focused on AIETs
that could be used in the development stage of the analyzed AI. In contrast, our work addresses the scenario
of AIETs applied to an already-developed AI. We focused on evaluating the effectiveness of existing AIETs
in helping developers of language models identify the risks and harms of their model while comparing the
AIETs analyzed. We chose language models as a case study because the literature has already mapped
several risks of these models, so we can compare whether the ethical considerations identified through AIETs
align with the literature.
3 Method
Our main goal is to understand how an AIET can help developers of language models to raise ethical
issues. In this section, we describe the methodology for achieving this goal, detailing the AIETs selected,
the language model selection, and how the AIETs were applied and evaluated. Fig. 2 shows an overview of
the methodology adopted in this paper.
3.1 AIET Selection
To evaluate AIETs in language models, we initially conducted an extensive literature survey. This survey
was carried out from January 2019 to July 20233 and aimed to identify the available AIETs up to that point.
We performed the searches using the search engines Web of Science, Scopus, and Google Scholar with the
following query:
(tool* OR framework* OR method*) AND ("artificial intelligence" OR "machine learning" OR
"natural language processing" OR "language model*") AND ethic*
3To keep this paper up to date, we provide the list of AIETs released until March 2025. In this way, we provide both the original list
of AIETs surveyed up to July 2023 (Appendix A) and the updated list from August 2023 to March 2025 (Appendix B). The selection
of the analyzed AIETs considered only the ones released up to July 2023.
6

--- Page 7 ---

Number of questions or fields to fill in
Multidisciplinary team
Examples of use
Quality of documentation
Questions about risks and harms of AI
Direct or reflective questions
AIET
Selection
AIET
Filter
Query
Jan/2019 to
Jul/2023
213
AIETs
Conferences
focused on
AI Ethics
8
AIETs
4
AIETs
Model Cards
ALTAI
FactSheets
Harms Modeling
Web of Science
Scopus
Google Scholar
Stage of application in the AI life cycle
Technical AIETs
Reflective AIETs
Feasibility of using in language models
Year of release
Target audience
Principles addressed
(a) AIET Selection
Query
Jan/2020 to
April/2024
21 Models
4 language models
selected for interviews
Google Scholar
Language
Model
Selection
(b) Language Model Selection
Present the
Consent
Form
Present and
explain the
AIET
Interview with the
developers using the
AIET as a guide for the
conversation
Generate the
documentation
based on the AIET
Developers assess
each AIET
according to their
perception
(c) Interviews: AIET Application and Evaluation
Fig. 2 Methodology overview. The initial stage of this project involved conducting a bibliographic survey of AIETs and
selecting the specific AIETs for evaluation (Fig. 2(a)). Following the selection, we assembled the interview scripts from the
AIETs questions and carried out an initial test. Once we defined the protocol, we submitted a project to the Research Ethics
Committee to obtain authorization to conduct the study, given that it involved interviews with human participants. After
securing the Ethics Committee’s approval, we carried out a bibliographic survey to select language models in Portuguese and
invite developers to participate in the study (Fig. 2(b)). Finally, we conducted the interviews and the AIETs were assessed by
the developers (Fig. 2(c))
We also searched the AIETs directly in journals and conferences focused on AI Ethics: FAccT (Conference
on Fairness, Accountability, and Transparency), AIES (Conference on AI, Ethics, and Society), AI and
Ethics, AI & Society, and Philosophy & Technology.
During the literature review, we found five articles that mapped other AIETs (more than 130 AIETs) [16–
18, 20, 21]. At the end of the search, we collected 213 AIETs4—including the AIETs indicated by the five
articles cited above. Due to the abundance of AIETs, we selected those that best suited the purpose of this
research using the following inclusion and exclusion criteria:
• Stage of application in the AI life-cycle: AIETs can be applied at different stages of the AI life-cycle.
In this paper, we evaluate the ethical considerations of a ready-for-use language model. Therefore, the
selected AIET must be applied in this final stage of the AI life-cycle, the use stage. We excluded all
4288 AIETs with the update made until March 2025.
7

--- Page 8 ---

AIETs that can only be applied to the previous stages (problem specification, design, and testing) such
as [26, 62, 63].
• Technical AIETs: Some AIETs were proposed for unique and specific objectives such as privacy [44],
explainability [37], and robustness [45], and required their application in the target model codes, thus
being technical AIETs. These AIETs did not meet the objective of this work and, therefore, were
excluded.
• Reflective AIETs: We kept all the AIETs that generated ethical considerations about the developed
model. Usually, these AIETs are questionnaires or checklists, where developers can produce documen-
tation of their AI developed focusing on the ethical considerations raised. In this way, we excluded
all the AIETs that did not help developers raise ethical issues, such as AIETs that were published to
serve as a guide on how to carry out an ethical audit on an AI without presenting questionnaires or
checklists [38, 39].
• Feasibility of using the AIET in language models: Some AIETs have specific focuses, such as only image
models [64, 65]. Since we focused on analyzing a language model, we excluded all AIETs that were not
feasible to use in our work.
• Year of release: We kept AIETs published from 2019 onwards to focus on tools developed during the
recent proliferation of language models and associated ethical guidelines.
• Target audience: Some AIETs were developed to be answered by companies through group tutorials
and company-wide workshops [43]. In this work, we selected AIETs that could be applied exclusively
to the model’s developers, and that could be applied in an interview format.
• Principle addressed: Some AIETs have been developed with a focus on just one ethical principle, such
as only on fairness [29, 66] or only on privacy [67, 68]. We kept the AIETs that had a combination
of at least three ethical principles. This analysis was carried out by checking the items contained in
the tools (e.g., questions, checklists) to identify the presence of the principles already discussed in the
literature [56].
Following these inclusion and exclusion criteria, we end up with eight AIETs [12–15, 40, 69–71]. Due to
the time required to apply all AIETs found through interviews with the developers, we decided to evaluate
four AIETs.
To select the final AIETs, we classified the AIETs found (see Table 3) by (i) the number of questions or
fields the AIET contained, (ii) whether the team proposing the AIET was multidisciplinary, (iii) whether
the AIET presented examples of use in its documentation, (iv) the quality of the documentation—whether
it was possible to understand how to use the AIET, (v) whether the AIET contained questions or fields to
fill in about risks and harms of the developed AI, and (vi) whether the AIET contained direct questions
(answered with yes or no) or had reflective questions, since the way the question is presented changes the way
developers can answer the question, (e.g., “During the development of the model, were there any concerns
about biases? [The answer to this question can be more direct, and can even be answered with just ‘yes’ or
‘no’]” and “What concerns related to bias were taken into account during the development of the model?
[The answer to this question will not be as direct as the previous question, because if the participant’s
answer was ‘yes’ in the previous question, in this one they will describe in more detail the concerns taken
into account]”).
The selection aimed to use different AIETs to assess developers’ perspectives of the different AIETs and
find their preferences for future use. The resulting collection of eight works appears in Table 3. The AIETs
selected are Model Cards [12], ALTAI [13], FactSheets [15], and Harms Modeling [14]. In the following, we
briefly describe the four AIETs selected.
Model Cards for Model Reporting [12], referred hereafter as Model Cards, are documents that
accompany an AI to provide transparent and accountable documentation about the technology, allowing
interested parties to be informed about all aspects of the AI in question, both in technical details and ethical
positions. To this end, Mitchell et al. proposed a structure with nine topics to comprise a Model Cards that
must be filled in by those responsible for the proposed AI: (1) model details, (2) intended use, (3) factors,
(4) metrics, (5) evaluation data, (6) training data, (7) quantitative analyses, (8) ethical considerations, and
(9) caveats and recommendations.
The Assessment List for Trustworthy Artificial Intelligence (ALTAI) [13] aims to help develop-
ers, companies, and/or organizations (self-)assess an AI through a questionnaire to create more trustworthy
technologies by identifying how AI can generate risks for society and the environment and what actions
to take to minimize these risks. ALTAI contains questions categorized into seven topics: (1) human agency
8

--- Page 9 ---

and oversight, (2) technical robustness and safety, (3) privacy and data governance, (4) transparency, (5)
diversity, non-discrimination, and fairness, (6) societal and environmental well-being, and (7) accountability.
FactSheets: Increasing Trust in AI Services through Supplier’s Declarations of Confor-
mity [15], referred hereafter as FactSheets, aims to create a documentation about an AI through a
questionnaire, which is designed to give stakeholders more trust in the technology. FactSheets helps to cre-
ate documentation on the developed AI to inform interested parties about how AI works, its applications,
limitations, and other information. FactSheets contains questions categorized into five topics: (1) statement
of purpose, (2) basic performance, (3) safety, (4) security, and (5) lineage.
Harms Modeling [14] aims to anticipate a technology’s potential for risks and identify deficiencies in the
technology that could put society and the environment at risk. Harms Modeling comprises stages where those
responsible for the technology define the purpose and use cases, analyze the impacts and their stakeholders,
and carry out a harm assessment of the technology. Harms Modeling addresses several types of harm that
should be assessed according to their severity, scale, probability, and frequency of occurring and affecting
personal and social well-being, and are grouped within the following types of risks: (1) risk of injury (physical
injury and emotional or psychological injury), (2) denial of consequential services (opportunity loss and
economic loss), (3) infringement on human rights (dignity loss, liberty loss, privacy loss, and environmental
impact), and (4) erosion of social and democratic structures (manipulation and social detriment).
3.2 Scripting and Testing the Interviews
All AIETs selected for this work fall within the Checklists and Questionnaires category, where the AIET
presents a set of questions that the participants must consider. In this way, the AIETs were used as a script
for each interview, using the AIET questions as a guide for the conversation.
To test the methodology proposed for the interviews, we conducted a pilot study with the developers of
the
CAPIVARA language model [7], a model developed by members of the Natural Language Processing
group of the Artificial Intelligence and Cognitive Architectures Hub (H.IAAC), the research group in which
this work was done.
CAPIVARA is an open source model proposed for low-resource languages focusing
on Portuguese. For the test, we invited and interviewed the three main developers of the model to fill in the
selected AIETs. Each interview session had a maximum duration of one hour, resulting in 11 interviews, all
of which every developer attended. We randomly selected the AIETs’ order and applied them as follows:
Model Cards, FactSheets, ALTAI, and Harms Modeling. The total time spent interviewing the developers
for each AIET was approximately two hours for Model Cards, two hours for FactSheets, three hours for
ALTAI, and four hours for Harms Modeling.
The AIETs best evaluated by the developers were Model Cards and Harms Modeling, as will be presented
in Section 4.1. Considering the duration necessary for conducting the interviews and the overall feasibility of
the study, the subsequent evaluations within this research will be exclusively focused on the AIETs’ Model
Cards and Harms Modeling.
3.3 Language Model Selection
Following the final AIET selection, we sought authorization from the Research Ethics Committee to conduct
the study, as it involves collecting data from human participants. Once the project received approval, we
invited the language model developers to participate in the study.
To select the language models developed with textual data in Portuguese5, a literature search was carried
out in February 2024 (updated in March 20256) with the following query in the search engine Google Scholar,
where we visited the first 20 pages, filtering the search from 20207 onwards:
"language model" AND "portuguese"
Fig. 3 presents the surveyed language models. Among these, we randomly selected four models to partici-
pate in the interviews8. Volunteer participants were recruited by the researcher responsible for this study via
e-mail. To preserve the confidentiality of the participants, we will not disclose the specific models interviewed
5In this paper, we focus only on language models developed exclusively for the Portuguese language, thus not considering multilingual
models.
6As with the AIETs, to keep this paper up to date, we provide the list of language models released until March 2025. However, the
selection of the interviewed models considered only the ones released up to March 2024.
7As far as we know, the first language models developed for the Portuguese language were published in 2020.
8We selected only four models due to the time required to conduct the study. As detailed in Section 5, carrying out a study on an
AIET requires a significant amount of time from both the researchers and the participants. In total, we conducted 35 interview sessions,
each lasting roughly one hour. Additionally, documenting each conversation required about two hours. For each group of participants,
the interviews were spread over 2 to 3 months.
9

--- Page 10 ---

Table 3 AIETs overview. Here, we compare the eight AIETs filtered according to the criteria (i) #Q: Number of questions or fields to fill, (ii)
IA: if it provides information about the authors, like name and affiliations, (iii) EG: if it provides examples of use, (iv) DQ: Documentation
quality (good, regular, and bad), (v) RH: if it evaluates risks and harms, (vi) D/R: if it has direct or reflective questions, and (vii) the
Differential about the AIETs. T: Application time (hours) in the testing interviews
AIET
Reference
T
#Q
IA
EG
DQ
RH
D/R
Differential
Model Cards
[12]
2h
25
✓
✓
good
✓
–
Only AIET for responsible
documentation in the format of a
fill-in form.
FactSheets
[15]
2h
119
✓
✓
good
✓
both
Best example of use. It has
questions that make references to
other AIETs [26, 27].
Machine Learning
Maturity Model
[71]
–
64
×
×
regular
×
direct
All topic sections aim to assess the
quality of the AI developed team.
AI Procurement in
a Box
[70]
–
119
✓
×
bad
✓
both
Provides case studies, but does not
show the use of the AIET.
ALTAI
[13]
3h
142
✓
×
regular
✓
direct
Provides a glossary of important
terms.
Harms
Modeling
[14]
4h
94
×
✓
regular
✓
reflective
Focuses exclusively at assessing risk
and harms and evaluate the
potential magnitude of them.
OECD framework
for the
classification of AI
systems
[69]
–
37
✓
✓
good
×
direct
Provides extensive documentation
about the AIET and AI topics.
Seven-Layer
Model with
Checklists
[40]
–
60
✓
✓
good
✓
both
Focuses exclusively on fairness
assessment.
10

--- Page 11 ---

in this paper. In addition, aspects of ethnicity, sexual orientation, gender identity, class, social group, and
physical size were not relevant to the selection of participants. Furthermore, we did not collect such informa-
tion because the study population was small, making the participants easily identifiable, and thus breaking
their confidentiality. A total of 11 developers participated in the interviews, which were organized into four
groups of 2, 2, 3, and 4 participants, corresponding to the group of developers from each model. Developers
from different models had no interaction during the interviews and their participation are anonymous9.
GPorTuguese-2
PTT5
BERTimbau
BioBERTpt
BERTaú
2020
GPT2-Bio-Pt
BERTikal
PetroBERT
Sabiá
2021
Albertina PT-*
CardioBERTpt
2022
JurisBERT
Cabrita
BERTabaporu
DeBERTinha
LegalBert-pt
2023
DeB3RTa
GovBERT-BR
GemBode
PhiBode
BERTweet.BR
Sabiá-3
MediAlbertina
Serafim PT*
PTT5-v2
Juru
Sabiá-2
RoBERTaLexPT
Gervásio PT*
GlórIA
PeLLE
TeenyTinyLlama
BODE
2024
Tucano
Carvalho pt-gl
V-Glória
2025
CAPIVARA
Fig. 3 Language models developed for the Portuguese language releases from 2020 to March 2025: GPorTuguese-2 [72],
PTT5 [73], BERTimbau [74], BioBERTpt [75], BERT´au [76], GPT2-Bio-Pt [77], BERTikal [78], PetroBERT [79], Sabi´a [80],
Albertina PT-* [81], CardioBERTpt [82], JurisBERT [83], Cabrita [84], BERTabaporu [85], DeBERTinha [86], CAPIVARA [7],
LegalBert-pt [87], BODE [88], TeenyTinyLlama [89], PeLLE [90], Gl´orIA [91], Gerv´asio PT* [92], RoBERTaLexPT [93], Sabi´a-
2 [94], Juru [95], PTT5-v2 [96], Serafim PT* [97], MediAlbertina [98], Sabi´a-3[99], Tucano [100], Carvalho pt-gl [101], V-
Gl´oria [102], GemBode e PhiBode [103], BERTweet.BR [104], GovBERT-BR [105], and DeB3RTa [106].
Brazilian Portuguese,
European Portuguese,
Both, Brazilian and European Portuguese
3.4 AIET Application and Evaluation
3.4.1 Interview and AIET Documentation
After selecting the AIETs and having the study approved by the Research Ethics Committee, we remotely
interviewed the language model developers who agreed to participate using the online meeting platform
Google Meet. We recorded all the interviews and later transcribed them with the appropriate authorizations
and consent from all the participants. Each interview session lasted a maximum of one hour and included
the participation of all developers from the same model.
At the first meeting, we presented to the participants a Consent Term setting out the objectives and
justifications of the study, the importance of the study, the procedures, and methodology that would be
adopted, how the data collected would be handled, the possible discomforts and risks of the study, the
benefits and the ethical guarantees for the participants. In addition, at the beginning of each interview, we
took a moment to answer any questions the participants might have and to help with whatever was necessary
for the progress of the research.
At the beginning of each interview with a new AIET, we took a moment to introduce the AIET to
the developers and answer any questions they had about it. The AIETs were answered verbally by the
developers during the interviews, and the interviews were conducted in Portuguese—we read all the questions
9Note that CAPIVARA model was a pilot case outside this anonymous group.
11

--- Page 12 ---

in Portuguese—we presented the English version for better understanding when a direct translation was not
possible—and the developers answered the questions in Portuguese.
After the interviews, we used audio recordings and transcriptions to create the final documentation for
each AIET. This documentation was prepared following the requirements of each AIET, that is, it is the
filled-in AIET. This documentation is confidential and only the developers had access to the final document
for their model.
3.4.2 Developers’ Feedback
Based on the final documentation—the filled-in AIETs—the participants were invited to individually com-
plete a questionnaire to identify their perspective of the AIETs and the ethical considerations raised by each
applied AIET.
For each applied AIET, we asked each developer their agreement with statements such as “The AIET
is easy to use/respond”, “The AIET is useful for identifying the risks of the language model”, “The AIET
is useful for generating responsible documentation about the language model”, and “It is complicated to
identify the ethical considerations of the language model using the AIET”. In addition, we asked whether
they would use a given AIET again in other projects, whether the developer had already thought about the
ethical considerations of their model before the interviews, which AIET raised the most ethical concerns
about their model, the documentation they consider most informative about ethical considerations, and
whether they already knew and used AIETs. We asked them to rate each AIET used between 1 and 5, with
5 being the most positive assessment of the AIET. Table 4 presents the complete questionnaire used for this
stage.
Following the risks listed by Weidinger et al. [5], and adding the following risks to the list: “Lack
of representation of cultural and social aspects of the Brazilian population”, “Lack of representation of
cultural and social aspects of the Portuguese-speaking population”, and “Low performance in the Portuguese
language”, we asked developers if they identified that risk as appearing in the language model they developed,
and if so, which AIET helped them to identify that risk. Table 5 presents the complete questionnaire used
for this stage.
This questionnaire took each developer around 30 minutes to complete, and they had 15 days after
receiving the final documentation to individually complete the questionnaire. We completed the interviews
in July 2024. Section 4 presents and discusses the results obtained in our study.
4 Results and Discussion
This section presents the results and discusses the developers’ perspectives and opinions on the AIETs
applied in an interview format. Section 4.1 presents the results obtained from the pilot interviews with the
three main developers of
CAPIVARA model with the application of the AIETs Model Cards, ALTAI,
FactSheets, and Harms Modeling. Section 4.2 describes the aggregated results of the interviews with the
developers of the four language models interviewed with the application of the AIETs Model Cards and
Harms Modeling.
We organized both subsections with the following topics that encompass the questions we asked the
developers through the AIETs final evaluation form:
Evaluation of the AIETs using agree/disagree responses: The first set of questions asks for
opinions on whether developers agree or disagree with certain affirmation about each analyzed AIET.
For each question (Fig. 4), the percentage of “Agree”, “Weakly agree”, “Weakly disagree” and “Dis-
agree” answers for each AIET is shown. These percentages exclude the “Neutral” responses when a
developer neither agreed nor disagreed with the affirmation (Fig. 4(b)). In addition, for each question,
the percentage of developers who agree with the affirmation is also highlighted in green. This figure
includes the percentage of “Agree” and “Weakly agree” answers (Fig. 4).
Classification of the AIETs using general questions: The second set of questions asks for gen-
eral opinions about the analyzed AIETs. We asked developers to choose the AIET that best answered
the question.
Ethical considerations identified using the AIETs: The third set of questions asks for opinions
on the risks, harms, and ethical considerations identified using the AIETs. We asked developers which
12

--- Page 13 ---

Table 4 Questionnaire to extract developers’ perceptions about the analyzed AIETs [Part 1]
Considering the AIET Harms Modeling, indicate your opinion on the following statements:
“The AIET is easy to use/answer”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
“The AIET is useful for identifying the risks of the language model”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
“The AIET is useful for generating responsible documentation about the language model”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
“It is complicated to identify the ethical considerations of the language model using the AIET”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
Considering the AIET Model Cards, indicate your opinion on the following statements:
“The AIET is easy to use/answer”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
“The AIET is useful for identifying the risks of the language model”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
“The AIET is useful for generating responsible documentation about the language model”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
“It is complicated to identify the ethical considerations of the language model using the AIET”
⃝Agree
⃝Weakly agree
⃝Neutral
⃝Weakly disagree
⃝Disagree
Which AIET would you prefer to use again if you were to propose/develop a new model?
⃝Harms Modeling
⃝Model Cards
Although you indicated a preference in the previous question, would you actually use the AIET again?
⃝Yes
⃝No
⃝Maybe
Which AIET helped you the most to identify the ethical considerations of your model?
⃝Harms Modeling
⃝Model Cards
Which AIET’s final documentation revealed the most ethical considerations about your model?
⃝Harms Modeling documentation
⃝Model Cards documentation
Which AIET’s final documentation would be more informative and better understood by your model’s
stakeholders?
⃝Harms Modeling documentation
⃝Model Cards documentation
How would you rate the AIETs, with 5 being the most positive and 1 the most negative?
Harms Modeling
Model Cards
⃝1
⃝2
⃝3
⃝4
⃝5
⃝1
⃝2
⃝3
⃝4
⃝5
Before applying the AIETs/interviews, did you assess the ethical issues related to your model?
⃝Yes
⃝No
Before applying the AIETs/interviews, did you already know about any AIET?
⃝Yes and I’ve used it
⃝Yes, but I’ve never used it
⃝No
If you answered “Yes” to the previous question, which AIET did you know?
[Open answer]
Would you like to make any additional comments about the AIETs or your previous answers?
[Open answer]
AIET best addressed or discussed the risks or harms of the model they developed. We presented 24
options of risks or harms that a language model can contain, where the developers had to answer as
an option either the four analyzed AIETs or the option “None”. The first 21 risks presented to the
developers were extracted from the risks mapped by Weidinger et al. [5]. As the models interviewed
were developed with a focus on the Portuguese language (PT-BR), we added three possible specific and
existing risks for these language models: “Lack of representation of cultural and social aspects of the
Brazilian population”, “Lack of representation of cultural and social aspects of the Portuguese-speaking
population”, and “Low performance in the Portuguese language”.
Scores of the analyzed AIETs by the developers: Finally, we asked developers to provide a score
for each analyzed AIET, following a 5-point scale, with 1 being the most negative perception of the AIET
and 5 being the most positive perception of the AIET.
13

--- Page 14 ---

Table 5 Questionnaire to extract developers’ perceptions about the analyzed AIETs [Part 2]
In which AIET do you think that the following risk/harm was best addressed? For each option, select the AIET
and select if your model has the risk (’Yes’ option) or not (’No’ option)
Social stereotypes and unfair discrimination
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Exclusionary norms
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Toxic language
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Lower performance by social group
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Compromise privacy by leaking private information
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Compromise privacy by correctly inferring private information
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Risks from leaking or correctly inferring sensitive information
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Disseminating false or misleading information
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Causing material harm by disseminating misinformation, e.g., in medicine or law
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Nudging or advising users to perform unethical or illegal actions
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Reducing the cost of disinformation campaigns
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Facilitating fraud and impersonation scams
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Assisting code generation for cyber attacks, weapons, or malicious use
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Illegitimate surveillance and censorship
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Anthropomorphizing systems can lead to overreliance or unsafe use
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Create avenues for exploiting user trust to obtain private information
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Promoting harmful stereotypes by implying gender or ethnic identity
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Environmental harms from operating language models
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Increasing inequality and negative effects on job quality
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Undermining creative economies
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Disparate access to benefits due to hardware, software, skill constraints
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Lack of representation of cultural and social aspects of the Brazilian population
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Lack of representation of cultural and social aspects of the Portuguese-speaking population
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
Low performance in the Portuguese language
⃝Harms Modeling
⃝Model Cards
⃝None
⃝Yes
⃝No
4.1 Results of the CAPIVARA Model
According to the perspectives of the three developers of the
CAPIVARA language model, the results of
this subsection show that:
Model Cards was considered an easy-to-use AIET, effective in identifying the risks associated with
language models and generating responsible documentation for these models. It was considered the AIET
that generated the most informative documentation. The tool obtained an average score of 4.33 points,
the developers’ second-best-rated score.
14

--- Page 15 ---

ALTAI was considered the least readable AIET, being the most complicated to use both for identifying
the risks of language models and for creating responsible and informative documentation. The tool
obtained an average score of 2 points, making it the worst rated by the developers.
FactSheets was an average AIET, being easy to use, and helpful for identifying language model risks
and generating responsible model documentation. The tool obtained an average score of 3.67 points.
Harms Modeling was considered an easy-to-use AIET and the best tool for identifying language model
risks, generating responsible and informative documentation about the models. The tool obtained an
average score of 4.67 points, being the best rated by the developers.
In the following, we present and discuss in detail these results following the structure presented in
Section 4.
4.1.1 Evaluation of the AIETs using Agree/Disagree Responses
Fig. 4 presents the results of evaluating the AIETs stage using agree/disagree responses. In the following,
we discuss each of the affirmations.
Model Cards
ALTAI
FactSheets
Harms Modeling
0%
20%
40%
60%
80%
100%
100%
33.3%
33.3%
66.7%
33.3%
66.7%
33.3%
33.3%
(a) “The AIET is easy to use/answer”
Model Cards
ALTAI
FactSheets
Harms Modeling
0%
20%
40%
60%
80%
100%
33.3%
33.3%
100%
66.7%
50%
66.6%
50%
(b) “The AIET is useful for identifying the risks of the language
model”
Model Cards
ALTAI
FactSheets
Harms Modeling
0%
20%
40%
60%
80%
100%
33.3%
33.3%
100%
66.6%
33.3%
33.3%
66.7%
33.3%
(c) “The AIET is useful for generating responsible documentation
about the language model”
Model Cards
ALTAI
FactSheets
Harms Modeling
0%
20%
40%
60%
80%
100%
33.3%
33.3%
66.7%
33.3%
33.3%
33.3%
33.3%
100%
33.3%
(d) “It is complicated to identify the ethical considerations of the
language model using the AIET”
Fig. 4 Evaluation of the AIETs from the perspective of the developers interviewed. Here, the graphs do not include the
“neutral” option.
: “Agree”,
: “Weakly agree”,
: “Weakly disagree”, and
: “Disagree”
15

--- Page 16 ---

“The AIET is easy to use/answer” (Fig. 4(a)). In this affirmation, Model Cards received 100% of
“Agree”answers, showing the developers’ agreement on the tool’s ease of use, followed by Harms Modeling,
with 100% agreeing with the affirmation, the majority vote being “Weakly agree”. The results make it
possible to understand the developers’ difficulty using ALTAI and FactSheets, respectively. An interesting
contrast is that the AIET that took the longest to apply was Harms Modeling (around 4 hours), showing
that the time taken to complete the AIET does not indicate difficulty in using it. During the application
of the ALTAI, the developers commented on the tool’s readability, with the questions being challenging to
understand with terms they did not know. ALTAI offers a glossary in its documentation describing keywords.
However, some developers did not understand some questions, even with the glossary. This result shows a
difficulty in using the tool and a possible impediment to its use in the daily lives of developers.
“The AIET is useful for identifying the risks of the language model” (Fig. 4(b)). Harms
Modeling received 100% “Agree”answers, showing agreement on the part of the developers as to the usability
of the tool in identifying risks in a language model. In fact, Harms Modeling presents an extensive list of
harms technology can generate. It offers a mechanism for evaluating these harms in terms of “severity”,
“scale”, “probability” and “frequency”, where for each option, the developers choose whether that harm is
“low”, “moderate” or “high”. Harms Modeling brought dynamism to the interviews, where the developers
could work together to analyze the harms in their model and indicate how harmful these risks could be to the
stakeholders. An interesting point is the fact that, at random, Harms Modeling was the last AIET applied
to the model. We therefore hypothesize that the order of the application interferes with how developers can
evaluate the AIETs. Thus, it is possible that if Harms Modeling had been applied first in the model, this
could have changed how Model Cards and FactSheets were answered, both with 100% agreement with the
affirmation, the majority vote being “Weakly agree”. In this affirmation, ALTAI was the worst-rated tool,
receiving 50% agreement with the “Weakly agree”option. Interestingly, at the same time as ALTAI was
rated worst when asked “Which AIET helped you the most to identify the ethical considerations of your
model?” (see Fig. 5), ALTAI was chosen by one out of three respondents, along with FactSheets and Harms
Modeling, showing that how a question is asked can interfere with the answer given.
“The AIET is useful for generating responsible documentation about the language model”
(Fig. 4(c)). Harms Modeling received 100% of “Agree”answers, showing agreement on the part of the devel-
opers as to the quality of the tool in generating responsible documentation about the model developed,
followed by Model Cards with 100% of agreement with the affirmation, the majority vote being “Weakly
agree”. Both AIETs were the ones that generated documentation with the most information and which will
possibly be better understood by the model’s stakeholders (see Fig. 5). FactSheets was the third best-rated
tool with 66.7%, followed by ALTAI with 33.3% of the votes. One contrast between the two AIETs is the
documentation that introduces them. FactSheets has usage examples, while ALTAI does not. In addition,
ALTAI presents “yes”/“no” questions, which makes it challenging to present a clear final documentation of
the model. The final documentation for both FactSheets and ALTAI was accompanied by questions, unlike
the proposal offered by Harms Modeling and Model Cards, making the final document more complicated
to read.
“It is complicated to identify the ethical considerations of the language model using the
AIET” (Fig. 4(d)). ALTAI and FactSheets, with 66.7% agreement, respectively, were considered the most
complicated to use as a guide for identifying ethical considerations about the model, reinforcing the results
achieved for the previous affirmation “The AIET is useful for generating responsible documentation about
the language model”. Harms Modeling, with 33.3% of the votes, was the third tool considered complicated
to use as a guide, showing a contrast with the responses obtained for the affirmation “The AIET is useful for
identifying the risks of the language model”, suggesting that although the tool can be helpful at the same
time, it can be complicated. Model Cards received 100% “Disagree”answers, showing total agreement among
developers on the ease of using the tool as a guide for identifying the ethical considerations of the model.
During the application, Model Cards was praised for offering examples of how to fulfill the requirements of
the card, which indicates that the way the tool is presented changes the perception of developers when using
it, and is in line with the results obtained in the affirmation “The AIET is easy to use/answer” (Fig. 4(a)).
16

--- Page 17 ---

4.1.2 Classification of the AIETs using General Questions
Fig. 5 shows the answers obtained from the four general questions asked at this stage. In the following, we
discuss each of the questions.
0%
20%
40%
60%
80%
100%
Which AIET would you prefer to use again if you were to
propose/develop a new model?
Which AIET helped you the most to identify the ethical
considerations of your model?
Which AIET’s final documentation revealed the most ethical
considerations about your model?
Which AIET’s final documentation would be more informative
and better understood by your model's stakeholders?
33.3%
66.7%
Fig. 5 Classification of AIETs through general questions.
: Model Cards,
: ALTAI,
: FactSheets, and
: Harms Modeling
“Which AIET would you prefer to use again if you were to propose/develop a new model?”.
We asked developers whether they would prefer to use an AIET again if they were to implement a new AI
model, regardless of the purpose of the model. The AIETs that were chosen, equally with 33.3% of the votes,
were FactSheets, Harms Modeling, and Model Cards, with no agreement among the developers. We also
asked developers whether, although they have a preference for an AIET, they really would use this AIET
in the future, and all answered “yes”, showing an acceptance on the part of the developers to make use
of AIETs to make the deployment of their models more ethical. However, at the same time, as the AIETs
analyzed were all for the final stage of the AI life-cycle (when the model is already ready), the developers
commented that it would be interesting to use intermediate AIETs alongside these AIETs for other stages of
the AI life-cycle. According to the developers, changing the finished model and maintaining the same result
the AI achieves is often not feasible, making it difficult to make the model “more ethical”. Using an AIET
earlier in the model development process makes it possible to anticipate and mitigate risks and negative
impacts before the model is ready. Once the model is ready, it will unlikely be changed to include ethical
adjustments.
“Which AIET helped you the most to identify the ethical considerations of your model?”.
This question asked which AIET best helped the developers identify their model’s ethical considerations. The
AIETs that were chosen, equally with 33.3% of the votes, were ALTAI, FactSheets, and Harms Modeling,
with no agreement between the developers, showing that for the same model, different AIETs can serve as
aids to help developers map the ethical considerations of a model. We also asked developers if they had
already ethically evaluated the model they had developed, and 66.7% answered “yes”, but the affirmative
respondents commented that they had only been concerned with two ethical considerations and that by
using AIETs it was possible to discover other critical considerations about the model they had developed.
“Which AIET’s final documentation revealed the most ethical considerations about your
model?”. This question asked which AIET’s final documentation contained and revealed more ethical
considerations about the model developed. The most voted AIET’s final documentation was Harms Modeling
with 66.7% of the votes, followed by FactSheets with 33.3%. This result is in line with the result obtained
17

--- Page 18 ---

in Section 4.1.1 through the affirmation “The AIET is useful for identifying the risks of the language
model”, where Harms Modeling received 100% of “agree” votes for the statement. During the interviews,
the developers praised how Harms Modeling presented several different harms. As it was the last AIET
interviewed, the developers even commented that it was possible to identify ethical considerations with the
help of Harms Modeling that had not yet been identified using any of the AIETs previously interviewed and
that if Harms Modeling had been the first analyzed AIET, the results obtained in the other AIETs would
probably have been different, for example, by raising more ethical considerations.
“Which AIET’s final documentation would be more informative and better understood
by your model’s stakeholders?”. This question asked which AIET’s final documentation could help
developers disseminate responsible, transparent, and reliable documentation in a clear and informative way
to their stakeholders, both direct and indirect. The most voted AIET’s final documentation was Model Cards
with 66.7% of the votes, followed by Harms Modeling with 33.3%. This result aligns with the result obtained
in Section 4.1.1 through the affirmation “The AIET is useful for generating responsible documentation about
the language model”, where Harms Modeling and Model Cards received 100% of the votes in agreement
with the affirmation. We also asked developers which AIET’s final documentation they would like to share
publicly with their stakeholders. Both Harms Modeling and Model Cards received 100% of votes, followed
by 33.3% of votes for FactSheets final documentation. No developer chose ALTAI final documentation as
an option, supporting the result obtained in Section 4.1.1 through the affirmation “The AIET is easy to
use/answer”, where it was argued that the AIET was not so readable for developers, so at the same time, it
would be complicated for such documentation to be shared to stakeholders in a clear and informative way.
4.1.3 Ethical Considerations Identified using the AIETs
In this stage, we asked developers to point out the ethical considerations identified using the analyzed AIETs
and Table 6 shows the results achieved. The results suggest that Harms Modeling was the tool that best
addressed or discussed the risks or harms of the model analyzed.
According to 66.7% of the developers, no AIET has led to the discussion of harms related to malicious
uses of the technology, such as encouraging unethical actions, reducing the cost of disinformation campaigns,
facilitating fraud and impersonation scams, and generating code for malicious or unethical use.
In addition, the specific risks for the Portuguese language model, “Lack of representation of cultural and
social aspects of the Brazilian population” and “Lack of representation of cultural and social aspects of the
Portuguese-speaking population” according to 66.7% of the developers, were not addressed by any AIET,
showing that generalist AIETs may not map specific risks in an AI.
4.1.4 Scores of the analyzed AIETs by the Developers
Finally, we asked developers to provide a score for each analyzed AIET and Table 7 shows the results
obtained. The best-rated AIET was Harms Modeling, with an average of 4.67 points, followed by Model
Cards, with 4.33 points. FactSheets scored 3.67 points, and ALTAI 2 points.
The results achieved are in line with the results presented and discussed earlier in this section, showing
a preference on the part of developers to use the AIETs Harms Modeling and Model Cards as aids for
identifying and disclosing ethical considerations about a developed model, with fewer difficulties in use
and better clarity of the results achieved. Because of all these results, as mentioned above, the following
evaluations of this paper are focused only on Harms Modeling and Model Cards.
4.2 Results of the Interviews
As mentioned in Section 3.3, 11 developers participated in the interviews, forming four groups:
• Group 1 (or language model 1) – 2 participants;
• Group 2 (or language model 2) – 2 participants;
• Group 3 (or language model 3) – 3 participants;
• Group 4 (or language model 4) – 4 participants.
However, one participant from Group 4 refrained from answering the final form. Therefore, the results
of this section will take into account the perspectives of 10 of the 11 interviewed developers. According to
their perspective, the results of this subsection show that:
18

--- Page 19 ---

Table 6
CAPIVARA developers’ choice of which AIET best addressed or discussed a risk to
their language model. The cells show the percentage of developers who chose an AIET as the one
that best addressed the risk under analysis. The table includes the option “None”, meaning that
any AIETs identified the analyzed risk, according to the developers’ opinion. The first 21 risks in
the table were extracted from the risks mapped by Weidinger et al. [5]
Analyzed Risk
Model
Cards
ALTAI
Fact-
Sheets
Harms
Modeling
None
Social stereotypes and unfair
discrimination
0%
33.3%
0%
66.7%
0%
Exclusionary norms
0%
0%
0%
100%
0%
Toxic language
0%
0%
0%
100%
0%
Lower performance by social group
33.3%
0%
33.3%
33.3%
0%
Compromise privacy by leaking
private information
0%
33.3%
0%
66.7%
0%
Compromise privacy by correctly
inferring private information
0%
33.3%
0%
66.7%
0%
Risks from leaking or correctly
inferring sensitive information
0%
0%
33.3%
66.7%
0%
Disseminating false or misleading
information
33.3%
0%
33.3%
33.3%
0%
Causing material harm by
disseminating misinformation, e.g.,
in medicine or law
0%
0%
33.3%
66.7%
0%
Nudging or advising users to perform
unethical or illegal actions
0%
0%
33.3%
0%
66.7%
Reducing the cost of disinformation
campaigns
33.3%
0%
0%
0%
66.7%
Facilitating fraud and impersonation
scams
0%
0%
0%
33.3%
66.7%
Assisting code generation for cyber
attacks, weapons, or malicious use
33.3%
0%
0%
0%
66.7%
Illegitimate surveillance and
censorship
0%
33.3%
0%
66.7%
0%
Anthropomorphizing systems can
lead to overreliance or unsafe use
0%
33.3%
0%
66.7%
0%
Create avenues for exploiting user
trust to obtain private information
0%
0%
0%
33.3%
66.7%
Promoting harmful stereotypes by
implying gender or ethnic identity
0%
0%
0%
100%
0%
Environmental harms from operating
language models
0%
33.3%
0%
66.7%
0%
Increasing inequality and negative
effects on job quality
0%
0%
0%
100%
0%
Undermining creative economies
0%
0%
0%
66.7%
33.3%
Disparate access to benefits due to
hardware, software, skill constraints
0%
0%
0%
100%
0%
Lack of representation of cultural
and social aspects of the Brazilian
population
0%
0%
0%
33.3%
66.7%
Lack of representation of cultural
and social aspects of the
Portuguese-speaking population
0%
0%
0%
33.3%
66.7%
Low performance in the Portuguese
language
0%
0%
33.3%
33.3%
33.3%
Model Cards was considered an objective AIET with the most tangible documentation. As in
Section 4.1, Model Cards was considered an easy-to-use AIET, effective in identifying the risks associated
with language models and generating responsible documentation for these models. The tool obtained an
average score of 4.1 points, being the best rated by the developers.
Harms Modeling was considered a more complete AIET. However, it is very general and broad, and
does not consider specific aspects of language models. Nevertheless, Harms Modeling was still considered
the best tool for identifying language model risks. The tool obtained an average score of 3.6 points.
19

--- Page 20 ---

Table 7 Rating given to AIETs by the developers. The last line shows the average rating for
each AIET
Model Cards
ALTAI
FactSheets
Harms Modeling
Developer 1
4
3
3
5
Developer 2
4
2
3
5
Developer 3
5
1
5
4
Average
4.33
2
3.67
4.67
The results also indicate that the applied AIETs effectively map general ethical considerations about
language models. However, it is important to note that they did not address the unique aspects of these
models and failed to identify potential negative impacts for the Portuguese language. Additionally, the
results suggest that it is still not common practice for developers to include an ethical analysis of their
models before publishing them. Furthermore, there was a lack of agreement among developers when it came
to identifying risks associated with their models individually. In the following section, we present and discuss
these results in detail.
4.2.1 Evaluation of the AIETs using Agree/Disagree Responses
Fig. 6 presents the results of evaluating the AIETs stage using agree/disagree responses. We discuss each of
the affirmations as follows.
“The AIET is easy to use/answer” (Fig. 6(a)). In this affirmation, Model Cards received 100% of
agreement, where the majority of votes were “Agree” demonstrating agreement on the part of the developers
regarding the tool’s ease of use. Harms Modeling, unlike Section 4.1.1, received 60% of agreement, where the
majority of votes were “Weakly agree”. During the interviews, some participants commented that Harms
Modeling was generalist, too broad, and not ideal for language models, and that this made it difficult to
answer the tool’s questions related to the model in question.
“The AIET is useful for identifying the risks of the language model” (Fig. 6(b)). In this
affirmation, both Model Cards and Harms Modeling received 100% agreement, showing that both AIETs
can be used to help identify the ethical considerations of language models. However, it was possible to notice
throughout the interviews that the analyzed AIETs do not have questions that would allow them to address
more unique considerations of language models, such as considerations related to multilingual performance,
accents, slang, and regional expressions.
“The AIET is useful for generating responsible documentation about the language model”
(Fig. 6(c)). In this affirmation, both Model Cards and Harms Modeling received 100% agreement, where
the majority of votes were “Agree” for both. This result shows that both AIETs can be used to help create
responsible documentation of language models. However, it is important to note that this documentation
was created by the research team of this paper, not by the developers. Harms Modeling does not explain
how documentation should be created/generated from the tool’s questions. Therefore, we followed a pattern
in creating these documentations that we felt would be more informative, given the characteristics of the
AIET. One comment we received from one of the participants was that he/she did not see how to create
documentation from the questions he/she answered. In this way, the usability of Harms Modeling to generate
good documentation will depend a lot on how that documentation is structured. In contrast, we can find
examples of documentation to follow in the paper introducing Model Cards.
“It is complicated to identify the ethical considerations of the language model using the
AIET” (Fig. 6(d)). In this affirmation, Model Cards and Harms Modeling received 87.5% and 90% agree-
ment, respectively, with the majority of votes being “Weakly agree” for both. This result significantly
diverged from the findings reported in Section 4.1.1, showing that in these interviews stage, the developers
had more difficulties in both AIETs. This classification may be attributed to the fact that the
CAPIVARA
model team used two other AIETs in addition to Model Cards (the first to be applied) and Harms Mod-
eling (the last to be applied). This contributed to the team arriving better prepared in Harms Modeling,
resulting in a good evaluation of the tool, while Model Cards was already a tool known to the interviewees,
although never used. Another factor is that they are part of the same H.IAAC team as the researchers of this
study, which introduces a high bias in the evaluation because they are in contact with the subject. In the
20

--- Page 21 ---

Model Cards
Harms Modeling
0%
20%
40%
60%
80%
100%
60%
20%
40%
40%
30%
10%
(a) “The AIET is easy to use/answer”
Model Cards
Harms Modeling
0%
20%
40%
60%
80%
100%
57.1%
50%
42.9%
50%
(b) “The AIET is useful for identifying the risks of the language
model”
Model Cards
Harms Modeling
0%
20%
40%
60%
80%
100%
87.5%
75%
12.5%
25%
(c) “The AIET is useful for generating responsible documentation
about the language model”
Model Cards
Harms Modeling
0%
20%
40%
60%
80%
100%
25%
30%
62.5%
60%
12.5%
10%
(d) “It is complicated to identify the ethical considerations of the
language model using the AIET”
Fig. 6 Evaluation of the AIETs from the perspective of the developers interviewed. Here, the graphs do not include the
“neutral” option.
: “Agree”,
: “Weakly agree”,
: “Weakly disagree”, and
: “Disagree”
general interviews, the other developers had no close contact with AIETs and had never used them—only 4
participants said they already knew about the existence of Model Cards. All these points contribute to the
evaluation received by both AIETs, where the developers voted that it was complicated to draw up ethical
considerations about language models using AIETs, even though they are useful for identifying the risks of
these models—the result of the affirmation “The AIET is useful for identifying the risks of the language
model” of the two (Fig. 6(b)).
4.2.2 Classification of the AIETs through General Questions
Fig. 7 shows the answers obtained to the four general questions asked at this stage. In the following, we
discuss each of the questions.
21

--- Page 22 ---

0%
20%
40%
60%
80%
100%
Which AIET would you prefer to use again if you were to
propose/develop a new model?
Which AIET helped you the most to identify the ethical
considerations of your model?
Which AIET’s final documentation revealed the most ethical
considerations about your model?
Which AIET’s final documentation would be more informative
and better understood by your model's stakeholders?
80%
60%
40%
20%
Fig. 7 Classification of AIETs through general questions.
: Model Cards and
: Harms Modeling
“Which AIET would you prefer to use again if you were to propose/develop a new model?”.
We asked developers whether they would prefer to use an AIET again if they were to implement a new
AI model, regardless of the purpose of the model. Model Cards received 80% of the votes against Harms
Modeling. We also asked developers whether, although they prefer an AIET, they would really use this AIET
in the future. 50% answered “maybe”, 30% “yes” and 20% “no”. This result shows that there is neither
significant resistance nor adherence on the part of developers to use the AIETs again.
“Which AIET helped you the most to identify the ethical considerations of your model?”.
This question asked which AIET best helped the developers identify their model’s ethical considerations.
Harms Modeling received 60% of the developers’ votes, indicating AIET’s potential to help developers map
the ethical considerations of a model. We also asked developers if they had already ethically evaluated the
model they had developed, with or without AIET, and they all answered “no”, although four had already
met Model Cards. This result indicates that it is not yet natural for developers to add a step to ethically
analyze their models before publishing them, showing the need for greater engagement and dissemination
in the area of AI ethics.
“Which AIET’s final documentation revealed the most ethical considerations about your
model?”. This question asked which AIET’s final documentation contained and revealed more ethical
considerations about the model developed. The most voted AIET’s final documentation was Harms Modeling
with 80% of the votes, in line with the result obtained in “Which AIET helped you the most to identify the
ethical considerations of your model?”. During application in the
CAPIVARA model, we raised the point
that the order in which the AIETs were applied could generate different results from the others. However,
this effect was not observed in the four groups interviewed, where the AIETs were applied in alternating
order. The results were similar in all application orders.
“Which AIET’s final documentation would be more informative and better understood
by your model’s stakeholders?”. This question asked which AIET’s final documentation could help
developers disseminate responsible, transparent, and reliable documentation in a clear and informative way
to their stakeholders, both direct and indirect. The most voted AIET’s final documentation was Model Cards
with 90% of the votes against Harms Modeling. We also asked developers which AIET’s final documentation
they would like to share publicly with their stakeholders. The developers chose only the Model Cards
documentation because it was clearer, more objective, and easier to read. Interestingly, in the statement
“Which AIET’s final documentation revealed the most ethical considerations about your model?” Harms
22

--- Page 23 ---

Modeling scored the highest. This shows that even if a documentation reveals more ethical considerations
about a model, it will not necessarily be more informative and better understood by stakeholders.
4.2.3 Ethical Considerations Identified using the AIETs
In this stage, we asked developers to point out the ethical considerations identified using the analyzed
AIETs and Table 8 shows the results achieved. The results suggest that Harms Modeling was the tool that
best addressed or discussed the risks or harms of the analyzed model. Unlike the results of Section 4.1.3,
the specific risks for Portuguese language models, “Lack of representation of cultural and social aspects
of the Brazilian population” and “Lack of representation of cultural and social aspects of the Portuguese-
speaking population”, according to 70% of the developers, were addressed either by Model Cards or by
Harms Modeling.
At this stage, we asked developers to indicate whether or not the language model presents the analyzed
risk. The developers’ opinions on the risks are shown in Table 9. In addition, we assessed the disagreement
of developers in the same group about the presence of risks in their language models. Table 10 shows these
disagreement results. An important point about these results is the fact that all the developers in the
same group took part in all the interviews together, in which they talked to each other about the ethical
considerations raised by the AIETs about the analyzed language model, to reach an agreement on the final
answer that would be given. However, even in this case, the results show disagreement about the impacts
of the model among the developers themselves.
These results show how important it is for everyone involved in the process of creating and developing
a language model to participate in the stages of identifying and documenting ethical considerations about
the technology.
4.2.4 Scores of the analyzed AIETs by the Developers
Finally, we asked developers to provide a score for each analyzed AIET and Table 11 shows the results
obtained. The best-rated AIET was Model Cards, with an average of 4.1 points. Harms Modeling had an
average score of 3.6 points. The results achieved are in line with those presented and discussed earlier in this
section, showing that part of developers prefer to use the Model Cards. In the final evaluation form, we left
a field open for developers to leave their comments on the AIETs if they wished. We received the following
comments from three participants about their preference for Model Cards:
“I found both AIETs very useful, but I preferred Model Cards because it is more objective; this makes it easier to
develop and consume by other people who will read its content.”.
“Harms Modeling, although more complete in terms of subject matter, always seemed very general to me, which
ended up being an evaluation of the technology rather than the models themselves, as well as being very extensive.
In this respect, Model Cards has my preference, as it is much more specific to the model itself, although it does not
cover as many factors.”.
“Overall, I came away with a feeling that Harms Modeling is a much more ‘nitpicky’ tool in the sense that it is
much more extensive and tries to cover as many considerations as possible, but this also means that in the case
of language models, it covers many aspects that do not apply. At various times we have commented on topics that
seemed very disconnected and I had to ‘struggle’ to find something that fit. Model Cards seemed more succinct.
Looking at the final documentation, I can say that the documentation resulting from Model Cards is much closer
to what I would write in a model/article of my own (if I were writing it without the aid of any AIET), than the
documentation resulting from Harms Modeling.”.
The comments summarize that Model Cards is an objective, specific tool with more tangible documen-
tation. On the other hand, Harms Modeling is a more complete tool, but it is very general and does not
consider specific aspects of language models in general.
5 Limitations and Future Directions
This paper presents the perspectives of language model developers about four distinct AIETs. However, we
evaluated them using a pre-defined form with closed and multiple-choice questions. Relying the evaluation
only on a quantitative questionnaire may not be the most suitable method for a comprehensive assessment
of AIETs, as such evaluations encompass various nuances. In future work, it would be beneficial to enhance
this analysis by incorporating more open-ended questions for the interviewees and gathering additional
qualitative data from the interviews.
23

--- Page 24 ---

Table 8 Developers’ choice of which AIET best addressed or discussed a risk to their language
model. The cells show the percentage of developers who chose an AIET as the one that best
addressed the risk under analysis. The table includes the option “None”, meaning that any AIETs
identified the analyzed risk, according to the developers’ opinion. The first 21 risks in the table
were extracted from the risks mapped by Weidinger et al. [5]
Analyzed Risk
Model
Cards
Harms
Modeling
None
Social stereotypes and unfair discrimination
0%
90%
10%
Exclusionary norms
0%
80%
20%
Toxic language
0%
100%
0%
Lower performance by social group
0%
90%
10%
Compromise privacy by leaking private information
10%
80%
10%
Compromise privacy by correctly inferring private
information
0%
80%
20%
Risks from leaking or correctly inferring sensitive
information
0%
80%
20%
Disseminating false or misleading information
0%
90%
10%
Causing material harm by disseminating misinformation,
e.g., in medicine or law
10%
70%
20%
Nudging or advising users to perform unethical or illegal
actions
0%
90%
10%
Reducing the cost of disinformation campaigns
0%
90%
10%
Facilitating fraud and impersonation scams
0%
90%
10%
Assisting code generation for cyber attacks, weapons, or
malicious use
0%
70%
30%
Illegitimate surveillance and censorship
0%
80%
20%
Anthropomorphizing systems can lead to overreliance or
unsafe use
0%
70%
30%
Create avenues for exploiting user trust to obtain private
information
0%
70%
30%
Promoting harmful stereotypes by implying gender or
ethnic identity
0%
90%
10%
Environmental harms from operating language models
0%
80%
20%
Increasing inequality and negative effects on job quality
0%
90%
10%
Undermining creative economies
10%
70%
20%
Disparate access to benefits due to hardware, software,
skill constraints
10%
80%
10%
Lack of representation of cultural and social aspects of the
Brazilian population
20%
50%
30%
Lack of representation of cultural and social aspects of the
Portuguese-speaking population
40%
30%
30%
Low performance in the Portuguese language
40%
30%
30%
Currently, this research does not offer deeper insights into participants’ reasoning and preferences for
AIETs. This insight could lead to richer results, not only about which AIETs participants prefer, but for
what reasons they prefer them. In addition, more in-depth analyses of the impacts of language models
developed for the Portuguese language and how developers deal with these impacts have not been carried
out. However, it would be essential to consider this aspect of the research, also taking into account the
nuances of the conversations during the interviews and the logic for mapping the risks of the model. In
future work, we intend to conduct a qualitative methodological analysis of the interviews.
In future research, it would be valuable to analyze the documentation produced by each AIET with
individuals—other than the developers themselves—, who are intended to interpret the results. However,
this analysis was not conducted in the current study, as a decision was made not to publicly disclose the
documentation generated by each AIET about the models interviewed. The documentation produced in this
study, particularly for the AIETs Harms Modeling and ALTAI, followed a specific format created by us
(the research team of this study), as neither AIET included examples of the expected final documentation.
Therefore, the findings of this study may be influenced by how we constructed these documentations.
An important point is that many of the interviewees expressed a desire to receive feedback or a score
regarding their model’s potential “damaging” effects based on the assessment of the researchers involved
24

--- Page 25 ---

Table 9 Opinions of developers in the same group about the presence of risks in the analyzed
model. This shows the percentage of developers in the same group who think the model has that
risk. In other words, 100% (darker color) means that all the developers in that group agree that the
analyzed model has that risk. 0% (lighter color) means that all the developers in that group agree
that the analyzed model does not have that risk. The first 21 risks in the table were extracted from
the risks mapped by Weidinger et al. [5]
Analyzed Risk
Group 1
(2)
Group 2
(2)
Group 3
(3)
Group 4
(3)
Social stereotypes and unfair discrimination
50%
0%
100%
100%
Exclusionary norms
50%
0%
33.3%
66.7%
Toxic language
50%
0%
100%
66.7%
Lower performance by social group
50%
0%
66.7%
66.7%
Compromise privacy by leaking private
information
0%
0%
100%
66.7%
Compromise privacy by correctly inferring
private information
50%
0%
100%
100%
Risks from leaking or correctly inferring sensitive
information
0%
0%
100%
100%
Disseminating false or misleading information
100%
0%
100%
100%
Causing material harm by disseminating
misinformation, e.g., in medicine or law
100%
0%
100%
66.7%
Nudging or advising users to perform unethical
or illegal actions
0%
0%
100%
100%
Reducing the cost of disinformation campaigns
50%
0%
100%
66.7%
Facilitating fraud and impersonation scams
50%
0%
100%
66.7%
Assisting code generation for cyber attacks,
weapons, or malicious use
0%
0%
0%
66.7%
Illegitimate surveillance and censorship
0%
0%
66.7%
66.7%
Anthropomorphizing systems can lead to
overreliance or unsafe use
0%
0%
100%
66.7%
Create avenues for exploiting user trust to obtain
private information
0%
0%
100%
66.7%
Promoting harmful stereotypes by implying
gender or ethnic identity
50%
0%
100%
100%
Environmental harms from operating language
models
0%
0%
0%
66.7%
Increasing inequality and negative effects on job
quality
100%
0%
100%
66.7%
Undermining creative economies
0%
0%
66.7%
66.7%
Disparate access to benefits due to hardware,
software, skill constraints
0%
0%
66.7%
66.7%
Lack of representation of cultural and social
aspects of the Brazilian population
50%
50%
66.7%
66.7%
Lack of representation of cultural and social
aspects of the Portuguese-speaking population
50%
50%
66.7%
66.7%
Low performance in the Portuguese language
0%
0%
66.7%
33.3%
in this study. However, due to the scope of this research and the team members’ backgrounds, we did not
address this aspect at this research stage.
The AIETs analyzed in this research are general and can be applied to various types of AIs. In future
work, it will be essential to map the best and worst aspects of each AIET analyzed and propose a new AIET
specifically tailored for language models. This is important as our interviews with developers highlighted
several considerations that were not relevant to language models. Therefore, a new AIET must have the
differential of filling the gap in the other AIETs, and, being specific to language models, it must have the
means to identify their risks. Additionally, it is crucial to consider language, cultural, and country-specific
aspects when assessing the language model’s context. We hypothesize that each AIET has its own differential
and that combining two or more could generate more significant results when evaluating a language model.
Identifying these points is crucial when proposing a new AIET that can be used as a single tool with the
best aspects of the others.
It is important to note that the results of this study currently only consider language models developed
exclusively for the Portuguese language within the Brazilian context. As future work, it would be interesting
25

--- Page 26 ---

Table 10 Disagreement between developers in the same group about the presence of risks in the
analyzed model. The colored cells mean there was disagreement between the developers of the same
language model regarding whether the model presents the analyzed risk. The first 21 risks in the
table were extracted from the risks mapped by Weidinger et al. [5]
Analyzed Risk
Group 1
(2)
Group 2
(2)
Group 3
(3)
Group 4
(3)
Social stereotypes and unfair discrimination
50%
0%
100%
100%
Exclusionary norms
50%
0%
33.3%
66.7%
Toxic language
50%
0%
100%
66.7%
Lower performance by social group
50%
0%
66.7%
66.7%
Compromise privacy by leaking private
information
0%
0%
100%
66.7%
Compromise privacy by correctly inferring
private information
50%
0%
100%
100%
Risks from leaking or correctly inferring sensitive
information
0%
0%
100%
100%
Disseminating false or misleading information
100%
0%
100%
100%
Causing material harm by disseminating
misinformation, e.g., in medicine or law
100%
0%
100%
66.7%
Nudging or advising users to perform unethical
or illegal actions
0%
0%
100%
100%
Reducing the cost of disinformation campaigns
50%
0%
100%
66.7%
Facilitating fraud and impersonation scams
50%
0%
100%
66.7%
Assisting code generation for cyber attacks,
weapons, or malicious use
0%
0%
0%
66.7%
Illegitimate surveillance and censorship
0%
0%
66.7%
66.7%
Anthropomorphizing systems can lead to
overreliance or unsafe use
0%
0%
100%
66.7%
Create avenues for exploiting user trust to obtain
private information
0%
0%
100%
66.7%
Promoting harmful stereotypes by implying
gender or ethnic identity
50%
0%
100%
100%
Environmental harms from operating language
models
0%
0%
0%
66.7%
Increasing inequality and negative effects on job
quality
100%
100%
100%
66.7%
Undermining creative economies
0%
0%
66.7%
66.7%
Disparate access to benefits due to hardware,
software, skill constraints
0%
0%
66.7%
66.7%
Lack of representation of cultural and social
aspects of the Brazilian population
50%
50%
66.7%
66.7%
Lack of representation of cultural and social
aspects of the Portuguese-speaking population
50%
50%
66.7%
66.7%
Low performance in the Portuguese language
0%
0%
66.7%
33.3%
How to interpret this table: This table presents two information. Percentage indicates the percentage
of developers in the same group who think the model has that risk. 100% means that all the developers in
that group agree that the analyzed model has that risk. 0% means that all the developers in that group
agree that the analyzed model does not have that risk. Colors indicates a disagreement among developers
within the same group about the presence of risk in the model. This disagreement (colored cells) occurs for
values that differ from 0% or 100% (white cells). For example, in a group of two developers, 50% means
that one developer believes the model has that risk, while the other developer does not; this disagreement
is reflected through the cell color.
to assess whether the results extend to (i) other Portuguese-speaking contexts, (ii) other linguistic contexts
beyond Portuguese, and (iii) multilingual contexts. Such investigations could bring additional results to
the research on the application of AIETs in language models, as we could understand whether the results
obtained are general for language models or unique to models focused exclusively on Portuguese.
Carrying out a study on an AIET requires significant time from both the researchers and the people
who participate voluntarily. Consequently, it was not possible to analyze all the AIETs found in the AIET
selection stage reported in Section 3.1. In total, we conducted 35 interview sessions, each lasting roughly
one hour. Additionally, documenting each conversation required about two hours. Overall, each participant
group dedicated approximately 2 to 3 months to the study.
26

--- Page 27 ---

Table 11 Rating given to AIETs by the developers. The last line
shows the average rating for each AIET
Model Cards
Harms Modeling
Developer 1
5
4
Developer 2
5
5
Developer 3
5
4
Developer 4
2
3
Developer 5
4
1
Developer 6
5
4
Developer 7
4
4
Developer 8
4
4
Developer 9
3
3
Developer 10
4
4
Average
4.1
3.6
This study primarily analyzes AIETs to assess their usability and effectiveness in aiding language model
developers in identifying, mapping, and documenting the ethical issues associated with their models. It is
important to highlight that the scope of this study is deliberately limited to these specific functions. However,
it should be noted that AIETs can serve additional purposes, such as evaluating datasets, assessing early
stages of AI development, and conducting quantitative analyses of models like fairness metrics, which were
not explored in this study.
As far as we know, there is no method in the literature for comparing AIETs [19], and we hope to
provoke the community’s interest in finding ways of standardizing AIET evaluations. A method for comparing
AIETs would allow for better adoption by researchers, developers, companies, and organizations since the
AI literature lacks papers with exclusive sections for ethical considerations, and such AIETs could be a guide
for the elaboration of this section. Having a tool to help these people identify the ethical considerations of
what is being proposed could make the future of AI more transparent, responsible, and reliable. However,
we understand that an AIET alone will not lead us down this path and will require from the AI (ethics)
research community efforts.
6 Conclusion
This paper introduced a methodology to carry out a systematically filter for selecting and evaluating AIETs
in language models. To this end, we conducted a case study where we applied four AIETs (Model Cards,
ALTAI, FactSheets, and Harms Modeling) through interviews with developers of language models developed
with a focus on Portuguese (PT-BR models). We performed the interviews using the items of each AIET
analyzed as a script. The total time to interview the developers was around two hours for Model Cards, three
hours for ALTAI, two hours for FactSheets, and four hours for Harms Modeling. The developers answered
the AIETs verbally during the interviews, and we conducted the interviews in Portuguese.
We evaluated the AIETs from the developers’ perspective, using a form each developer answered. The
results suggest that the AIETs applied are effective for use as a guide in drawing up general ethical consid-
erations about language models. However, we note that they are general and do not address unique aspects
of these models, such as idiomatic expressions. In addition, the AIETs did not help to identify potential
negative impacts of models for the Portuguese language, such as the lack of representation of social and
cultural aspects of Portuguese-speaking populations in the Brazilian context.
According to the developers’ perspective, the final AIET documentation presented the potential negative
impacts contained in the language models and is responsible and informative document for the stakeholders.
However, the results show that documentation presenting the risks in detail differs from being informative and
easy to understand. From the analyzed AIETs, the developers pointed Harms Modeling as the most helpful
AIET in identifying ethical considerations about their model and pointed Model Cards as the AIET with the
best usability and that generates the most responsible documentation for disclosing ethical considerations
to their stakeholders. Therefore, using multiple AIETs when raising ethical considerations about a model
would be interesting.
27

--- Page 28 ---

The developers interviewed so far said they had never ethically evaluated their models. This result
indicates that it is not yet natural for developers to add a step to ethically analyze their models during the
development stage before publishing them, showing the need for greater engagement and dissemination in
the area of AI ethics. During the interviews, all the developers of the same model participated together in
the interviews regarding the language model they had developed, where they discussed and raised thoughts
together. Even so, when it came to individually pointing out the risks and negative impacts of the developed
model, there was disagreement about the risks contained in the model. This shows us how important it is
that the ethical examination of a technology is carried out jointly by everyone involved in its life cycle.
The results showed that AIETs met their objectives of helping to map ethical issues in AI. However,
we noted that relying solely on AIETs is insufficient; developers must also possess a grounding in AI ethics
to effectively consider the implications of their technologies. In addition, some AIETs were exhausting to
complete due to the complexity of use and readability of the content.
Ethics Statement
This research evaluates AIETs through a case study involving the developers of a language model. The
developers participated in the study through remote interviews. We applied the AIETs to the developed
language model through an orally answered questionnaire. This study was approved by the Research Ethics
Committee of the Universidade Estadual de Campinas under CAAE number 74643023.8.0000.5404. To carry
out this work, we followed all the guidelines and protocols required by the Committee. We are committed
to not disclosing AIETs’ final documentation about the model. We offered the participants the option to
disclose the documentation to their stakeholders by their means. All results published in this paper have
been obtained and disclosed with the consent of the participants.
This research was carried out exclusively by computer science researchers. As such, this paper carries all
our biases in the field, influencing how each AIET was interpreted, how the interviews were conducted, how
the AIETs’ final documentations were drawn up, how the results were analyzed, and how the paper was
written. In the future, we intend to involve the participation of a multidisciplinary group of researchers so
that ethical considerations about the work could be raised at all stages. In addition, the contribution of a
multidisciplinary group would promote deeper discussions about the importance, use, and quality of existing
AIETs.
This paper may generate the adverse and unintended impact of one AIET being perceived better than
another, which was different from this paper’s intention. It was not our aim to provide a rank of the analyzed
AIETs or to discourage using a specific AIET because it has a low score from the developers’ perspective—
following the criteria adopted in this paper. Here, we showed a case study where the interviewed developers
of specific language models classified the AIETs. The result may differ if analyzed with another language
models—or even another type of AI—and with other developers. Since there are no methods for comparing
AIETs in the literature, we followed the criteria described in this paper. For this reason, we urge caution
when interpreting these results.
Declarations
• Funding: This project was supported by the Brazilian Ministry of Science, Technology and Inno-
vations, with resources from Law nº 8,248, of October 23, 1991, within the scope of PPI-SOFTEX,
coordinated by Softex and published Arquitetura Cognitiva (Phase 3), DOU 01245.003479/2024-10.
J.Silva was partially financed by the Coordination for the Improvement of Higher Education Per-
sonnel (CAPES)—Finance Code 001. J.Silva (2024/23118-1), D.Moreira (2023/05939-5), G.Santos
(2024/07969-1), and S.Avila (2023/12086-9, 2023/12865-8, 2020/09838-0, 2013/08293-7) are also par-
tially funded by FAPESP. S.Avila (316489/2023-9) and H.Pedrini (304836/2022-2) are also partially
funded by CNPq.
• Conflict of interest: The authors declare no competing interests.
• Ethics approval and consent to participate: This study was approved by the Research Ethics
Committee of the Universidade Estadual de Campinas under CAAE number 74643023.8.0000.5404. To
carry out this work, we followed all the guidelines and protocols required by the Committee.
• Consent for publication: All the participants signed an informed consent form accepting their
participation in the study and authorizing it to be carried out.
28

--- Page 29 ---

• Data availability: None of the data collected in the interviews will be made available, nor will the
AIETs’ final documentation about the model (sensitive data).
• Material availability: ‘Not applicable’.
• Code availability: ‘Not applicable’.
• Additional Acknowledgments: The authors would like to thank all the members (and former mem-
bers) of the Natural Language Processing research group at the Artificial Intelligence and Cognitive
Architectures Hub (H.IAAC). The authors also thank all participants in this study.
• Author contribution: J.Silva was responsible for writing the manuscript, conducting all steps of
this research and the interviews with the developers. G.Santos, D.Moreira, and A.Ferreira participated
in the initial interviews with the CAPIVARA model, helping to adapt the interview script. H.Maia
contributed to discussing about this research at all stages and with the Research Ethics Committee
project. S.Avila and H.Pedrini are the advisors of this research, providing guidance on all tasks and
contributing to the writing process. All authors reviewed the manuscript and provided critical feedback
to enhance its quality. All authors have approved the final version of this manuscript and agree to be
responsible for all aspects of the work, ensuring its accuracy and integrity.
References
[1] OpenAI.: Introducing ChatGPT.
2022.
https://openai.com/blog/chatgpt.
Available from: https:
//openai.com/blog/chatgpt.
[2] Bender EM, Koller A. Climbing towards NLU: On Meaning, Form, and Understanding in the Age of
Data. In: Jurafsky D, Chai J, Schluter N, Tetreault J, editors. Proceedings of the 58th Annual Meeting
of the Association for Computational Linguistics. Online: Association for Computational Linguistics;
2020. p. 5185–5198. Available from: https://aclanthology.org/2020.acl-main.463/.
[3] Hovy D, Spruit SL. The Social Impact of Natural Language Processing. In: Annual Meeting of the
Association for Computational Linguistics (Volume 2: Short Papers); 2016. p. 591–598.
[4] Bender EM, Gebru T, McMillan-Major A, Shmitchell S. On the Dangers of Stochastic Parrots: Can
Language Models Be Too Big? In: ACM Conference on Fairness, Accountability, and Transparency;
2021. p. 610–623.
[5] Weidinger L, Mellor J, Rauh M, Griffin C, Uesato J, Huang PS, et al. Ethical and Social Risks of
Harm from Language Models. arXiv:211204359. 2021 Dec;.
[6] Nicholas G, Bhatia A. Lost in Translation: Large Language Models in Non-English Content Analysis.
arXiv:230607377. 2023;[cs.CL].
[7] Santos GO, Moreira DAB, Ferreira AI, Silva J, Pereira L, Bueno P, et al. CAPIVARA: Cost-Efficient
Approach for Improving Multilingual CLIP Performance on Low-Resource Languages. In: Workshop on
Multi-lingual Representation Learning (MRL), Conference on Empirical Methods in Natural Language
Processing (EMNLP); 2023. p. 184–207.
[8] Johnson RL, Pistilli G, Men´edez-Gonz´alez N, Duran LDD, Panai E, Kalpokiene J, et al. The Ghost
in the Machine Has an American Accent: Value Conflict in GPT-3. arXiv:220307785. 2022 Mar;.
[9] Hovy D, Prabhumoye S. Five sources of bias in natural language processing. Language and Linguistics
Compass. 2021;15(8):e12432.
[10] Brown N, Xie B, Sarder E, Fiesler C, Wiese ES. Teaching ethics in computing: a systematic literature
review of ACM computer science education publications. ACM Transactions on Computing Education.
2024;24(1):1–36.
[11] Goetze TS. Integrating ethics into computer science education: Multi-, inter-, and transdisciplinary
approaches. In: 54th ACM Technical Symposium on Computer Science Education; 2023. p. 645–651.
29

--- Page 30 ---

[12] Mitchell M, Wu S, Zaldivar A, Barnes P, Vasserman L, Hutchinson B, et al. Model Cards for Model
Reporting. In: Conference on Fairness, Accountability, and Transparency; 2019. p. 220–229.
[13] High-Level Expert Group on Artificial Intelligence. The Assessment List for Trustworthy Artificial
Intelligence (ALTAI). Brussels: European Commission; 2020. Available from: https://digital-strategy.
ec.europa.eu/pt/node/806.
[14] Microsoft.: Harms Modeling - Azure Application Architecture Guide. 2022. Available from: https:
//learn.microsoft.com/en-us/azure/architecture/guide/responsible-innovation/harms-modeling/.
[15] Arnold M, Bellamy RKE, Hind M, Houde S, Mehta S, Mojsilovi´c A, et al. FactSheets: Increasing
trust in AI services through supplier’s declarations of conformity.
IBM Journal of Research and
Development. 2019;63(4/5):6:1–6:13. https://doi.org/10.1147/JRD.2019.2942288.
[16] Ayling J, Chapman A. Putting AI Ethics to Work: Are the Tools Fit for Purpose? AI and Ethics.
2022;2(3):405–429.
[17] Wong RY, Madaio MA, Merrill N. Seeing Like a Toolkit: How Toolkits Envision the Work of AI
Ethics. ACM on Human-Computer Interaction. 2023;7(CSCW1):1–27.
[18] Prem E. From Ethical AI Frameworks to Tools: A Review of Approaches. AI and Ethics. 2023;3:1–18.
[19] Qiang V, Rhim J, Moon Aj.
No Such Thing as One-Size-Fits-All in AI Ethics Frameworks: A
Comparative Case Study. AI & Society. 2023;6:1–20.
[20] Morley J, Floridi L, Kinsey L, Elhalal A. From What to How: An Initial Review of Publicly Available
AI Ethics Tools, Methods and Research to Translate Principles into Practices. Science and Engineering
Ethics. 2020;26(4):2141–2168.
[21] Palladino N. A ‘Biased’ Emerging Governance Regime for Artificial Intelligence? How AI Ethics Get
Skewed Moving from Principles to Practices. Telecommunications Policy. 2022;47(5):102479.
[22] Ortega-Bola˜nos R, Bernal-Salcedo J, Germ´an Ortiz M, Galeano Sarmiento J, Ruz GA, Tabares-Soto
R.
Applying the ethics of AI: a systematic review of tools for developing and assessing AI-based
systems.
Artificial Intelligence Review. 2024;57(5):110.
https://doi.org/https://doi.org/10.1007/
s10462-024-10740-3.
[23] IDEO.:
IDEO’s
AI
Ethics
Cards.
2019.
Available
from:
https://www.ideo.com/journal/
ai-needs-an-ethical-compass-this-tool-can-help.
[24] Lobschat L, Mueller B, Eggers F, Brandimarte L, Diefenbach S, Kroschke M, et al. Corporate digital
responsibility.
Journal of Business Research. 2021;122:875–888.
https://doi.org/10.1016/j.jbusres.
2019.10.006.
[25] for Designers E.: Ethics for Designers — The Toolkit.
2017.
Available from: https://www.
ethicsfordesigners.com/tools.
[26] Gebru T, Morgenstern J, Vecchione B, Vaughan JW, Wallach H, III HD, et al. Datasheets for datasets.
Communications of the ACM. 2021 Nov;64(12):86–92. https://doi.org/10.1145/3458723.
[27] Bender EM, Friedman B. Data statements for natural language processing: Toward mitigating system
bias and enabling better science.
Transactions of the Association for Computational Linguistics.
2018;6:587–604.
[28] Holland S, Hosny A, Newman S, Joseph J, Chmielinski K. The Dataset Nutrition Label: A Framework
To Drive Higher Data Quality Standards. arXiv:180503677. 2018 May;[cs].
[29] Saleiro P, Kuester B, Hinkson L, London J, Stevens A, Anisfeld A, et al. Aequitas: A Bias and Fairness
Audit Toolkit. arXiv:181105577. 2019;[cs.LG].
30

--- Page 31 ---

[30] Arya V, Bellamy RKE, Chen PY, Dhurandhar A, Hind M, Hoffman SC, et al. AI Explainability 360
Toolkit. In: 3rd ACM India Joint International Conference on Data Science & Management of Data
(8th ACM IKDD CODS & 26th COMAD). CODS-COMAD ’21. New York, NY, USA: Association
for Computing Machinery; 2021. p. 376–379.
[31] Research PA.: What-if Tool. 2018. Available from: https://pair-code.github.io/what-if-tool/.
[32] for Ethical AI & Machine Learning TI.: AI-RFX Procurement Framework. 2019. Available from:
https://ethical.institute/rfx.html.
[33] Cabrera AA, Fu E, Bertucci D, Holstein K, Talwalkar A, Hong JI, et al. Zeno: An Interactive Frame-
work for Behavioral Evaluation of Machine Learning.
In: CHI Conference on Human Factors in
Computing Systems. CHI ’23. New York, NY, USA: Association for Computing Machinery; 2023. .
[34] Ribeiro MT, Singh S, Guestrin C. “Why Should I Trust You?”: Explaining the Predictions of Any
Classifier. In: ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.
KDD ’16. New York, NY, USA: Association for Computing Machinery; 2016. p. 1135–1144.
[35] Lundberg SM, Lee SI. A Unified Approach to Interpreting Model Predictions. In: Advances in Neural
Information Processing Systems. vol. 30; 2017. .
[36] Dhamala J, Sun T, Kumar V, Krishna S, Pruksachatkun Y, Chang KW, et al. BOLD: Dataset and
Metrics for Measuring Biases in Open-Ended Language Generation. In: ACM Conference on Fair-
ness, Accountability, and Transparency. FAccT ’21. New York, NY, USA: Association for Computing
Machinery; 2021. p. 862–872.
[37] for Ethical AI & Machine Learning TI.: XAI - An eXplainability toolbox for machine learning. 2021.
Available from: https://github.com/EthicalML/xai.
[38] M¨okander J, Schuett J, Kirk HR, Floridi L. Auditing large language models: A three-layered approach.
AI and Ethics. 2024;4(4):1085–1115. https://doi.org/10.1007/s43681-023-00289-2.
[39] Raji ID, Smart A, White RN, Mitchell M, Gebru T, Hutchinson B, et al. Closing the AI accountability
gap: defining an end-to-end framework for internal algorithmic auditing.
In: Conference on Fair-
ness, Accountability, and Transparency. FAT* ’20. New York, NY, USA: Association for Computing
Machinery; 2020. p. 33–44.
[40] Agarwal A, Agarwal H.
A seven-layer model with checklists for standardising fairness assess-
ment throughout the AI lifecycle.
AI and Ethics. 2023;4(2):299–314.
https://doi.org/10.1007/
s43681-023-00266-9.
[41] Wolff RF, Moons KG, Riley RD, Whiting PF, Westwood M, Collins GS, et al. PROBAST: a tool
to assess the risk of bias and applicability of prediction model studies. Annals of Internal Medicine.
2019;170(1):51–58.
[42] Ballard S, Chappell KM, Kennedy K. Judgment Call the Game: Using Value Sensitive Design and
Design Fiction to Surface Ethical Concerns Related to Technology. In: Designing Interactive Systems
Conference; 2019. p. 421–433.
[43] Microsoft.: Community Jury - Azure Application Architecture Guide. 2022. Available from: https:
//learn.microsoft.com/en-us/azure/architecture/guide/responsible-innovation/community-jury/.
[44] Privacy T.: TensorFlow Privacy. 2019. Available from: https://github.com/tensorflow/privacy.
[45] Nicolae MI, Sinn M, Tran MN, Buesser B, Rawat A, Wistuba M, et al. Adversarial Robustness Toolbox
v1.0.0. arXiv180701069. 2019;[cs.LG].
[46] Doteveryone.:
Consequence
Scanning:
An
Agile
event
for
Responsible
Innova-
tors.
2019.
Available
from:
https://doteveryone.org.uk/wp-content/uploads/2021/02/
31

--- Page 32 ---

Consequence-Scanning-Agile-Event-Manual-TechTransformed-Doteveryone-2.pdf.
[47] Kiritchenko S, Mohammad SM. Examining Gender and Race Bias in Two Hundred Sentiment Analysis
Systems. NAACL HLT 2018. 2018;p. 43.
[48] Benatti RM, Villarroel CML, Avila S, Colombini EL, Severi F. Should I disclose my dataset? Caveats
between reproducibility and individual data rights. In: Natural Legal Language Processing Workshop.
Association for Computational Linguistics; 2022. p. 228–237.
[49] Epstein Z, Payne BH, Shen JH, Hong CJ, Felbo B, Dubey A, et al. TuringBox: An Experimental Plat-
form for the Evaluation of AI Systems. In: Twenty-Seventh International Joint Conference on Artificial
Intelligence, IJCAI-18. International Joint Conferences on Artificial Intelligence Organization; 2018.
p. 5826–5828.
[50] Ali S, Kumar V, Breazeal C. AI Audit: A Card Game to Reflect on Everyday AI Systems. AAAI Con-
ference on Artificial Intelligence. 2024 Jul;37(13):15981–15989. https://doi.org/10.1609/aaai.v37i13.
26897.
[51] Zhou J, Chen F, Berry A, Reed M, Zhang S, Savage S. A Survey on Ethical Principles of AI and
Implementations. In: IEEE Symposium Series on Computational Intelligence. Canberra, Australia:
IEEE; 2020. p. 3010–3017.
[52] Schiff D, Biddle J, Borenstein J, Laas K. What’s next for AI ethics, policy, and governance? a global
overview. In: AAAI/ACM Conference on AI, Ethics, and Society. New York City, NY, USA: ACM;
2020. p. 153–158.
[53] Floridi L. Translating principles into practices of digital ethics: Five risks of being unethical. Philosophy
& Technology. 2019;32(2):185–193.
[54] Khan AA, Badshah S, Liang P, Waseem M, Khan B, Ahmad A, et al. Ethics of AI: A systematic
literature review of principles and challenges. In: 26th International Conference on Evaluation and
Assessment in Software Engineering. Gothenburg, Sweden: ACM; 2022. p. 383–392.
[55] Corrˆea NK, Galv˜ao C, Santos JW, Del Pino C, Pinto EP, Barbosa C, et al. Worldwide AI ethics: A
review of 200 guidelines and recommendations for AI governance. Patterns. 2023;4(10).
[56] Jobin A, Ienca M, Vayena E. Artificial Intelligence: The Global Landscape of Ethics Guidelines. Nature
Machine Intelligence. 2019;1(9):389–399. [cs].
[57] Ryan M, Stahl BC. Artificial Intelligence Ethics Guidelines for Developers and Users: Clarifying Their
Content and Normative Implications. Journal of Information, Communication and Ethics in Society.
2020 Jan;19(1):61–86.
[58] Peters D, Vold K, Robinson D, Calvo RA.
Responsible AI: Two Frameworks for Ethical Design
Practice. IEEE Transactions on Technology and Society. 2020;1(1):34–47.
[59] High-Level Expert Group on Artificial Intelligence.: Ethics Guidelines for Trustworthy AI.
2019.
Available from: https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai.
[60] Anderson D, Bonaguro J, McKinney M, Nicklin A, Wiseman J.: Ethics & Algorithms Toolkit (beta).
2018. Available from: https://ethicstoolkit.ai/.
[61] Treasury Board of Canada.: Algorithmic Impact Assessment Tool.
2021.
Available from:
https://www.canada.ca/en/government/system/digital-government/digital-government-innovations/
responsible-use-ai/algorithmic-impact-assessment.html.
[62] Community TW.: The Turing Way: A Handbook for Reproducible, Ethical and Collaborative Research.
Zenodo. 2021.
32

--- Page 33 ---

[63] Reisman D, Schultz J, Crawford K, Whittaker M.
Algorithmic Impact Assessments: A Practical
Framework for Public Agency Accountability. AI Now Intitute. 2018;1(1):1–22.
[64] Dhurandhar A, Chen PY, Luss R, Tu CC, Ting P, Shanmugam K, et al. Explanations based on the
missing: Towards contrastive explanations with pertinent negatives. Advances in Neural Information
Processing Systems. 2018;31.
[65] Goodman D, Xin H, Yang W, Yuesheng W, Junfeng X, Huan Z. Advbox: A toolbox to generate
adversarial examples that fool neural networks. arXiv:200105574. 2020;[cs.LG].
[66] Zhang J, Shu Y, Yu H. Fairness in Design: A Framework for Facilitating Ethical Artificial Intelligence
Designs. International Journal of Crowd Science. 2023;7(1):32–39. https://doi.org/10.26599/IJCS.
2022.9100033.
[67] Goldsteen A, Saadi O, Shmelkin R, Shachor S, Razinkov N.
AI Privacy Toolkit.
SoftwareX.
2023;22:101352. https://doi.org/10.1016/j.softx.2023.101352.
[68] ICO.: Guide to the UK General Data Protection Regulation (UK GDPR). 2020.
[69] OECD Digital Economy Papers.: OECD Framework for the Classification of AI Systems. Paris: OECD
Publishing. 2022.
[70] Forum WE.: AI Procurement in a Box.
2020.
Available from: https://www3.weforum.org/docs/
WEF AI Procurement in a Box Project Overview 2020.pdf.
[71] for Ethical AI & Machine Learning TI.: Machine Learning Maturity Model, AI & Machine Learning
Solutions. 2019. Available from: https://ethical.institute/mlmm.
[72] Guillou P.: GPorTuguese-2 (Portuguese GPT-2 small): a Language Model for Portuguese text gen-
eration (and more NLP tasks...).
2020.
Available from: https://huggingface.co/pierreguillou/
gpt2-small-portuguese.
[73] Carmo D, Piau M, Campiotti I, Nogueira R, Lotufo R. PTT5: Pretraining and validating the T5
model on Brazilian Portuguese data. arXiv:200809144. 2020 Oct;.
[74] Souza F, Nogueira R, Lotufo R. BERTimbau: Pretrained BERT Models for Brazilian Portuguese.
In: Cerri R, Prati RC, editors. Intelligent Systems. Cham: Springer International Publishing; 2020. p.
403–417.
[75] Schneider ETR, de Souza JVA, Knafou J, Oliveira LESe, Copara J, Gumiel YB, et al. BioBERTpt - A
Portuguese Neural Language Model for Clinical Named Entity Recognition. In: 3rd Clinical Natural
Language Processing Workshop; 2020. p. 65–72.
[76] Finardi P, Viegas JD, Ferreira GT, Mansano AF, Carid´a VF.
BERTa´u: Ita´u BERT for Digital
Customer Service. arXiv:210112015. 2021 Jul;.
[77] Schneider ETR, de Souza JVA, Gumiel YB, Moro C, Paraiso EC. A GPT-2 Language Model for
Biomedical Texts in Portuguese. In: IEEE 34th International Symposium on Computer-Based Medical
Systems; 2021. p. 474–479.
[78] Polo FM, Mendon¸ca GCF, Parreira KCJ, Gianvechio L, Cordeiro P, Ferreira JB, et al. LegalNLP
– Natural Language Processing methods for the Brazilian Legal Language.
arXiv:211015709.
2021;[cs.CL].
[79] Rodrigues RBM, Privatto PIM, de Sousa GJ, Murari RP, Afonso LCS, Papa JP, et al. PetroBERT: A
Domain Adaptation Language Model for Oil and Gas Applications in Portuguese. In: Computational
Processing of the Portuguese Language; 2022. p. 101–109.
33

--- Page 34 ---

[80] Pires R, Abonizio H, Almeida TS, Nogueira R.
Sabi´a: Portuguese Large Language Models.
In:
Intelligent Systems; 2023. p. 226–240.
[81] Rodrigues J, Gomes L, Silva J, Branco A, Santos R, Cardoso HL, et al. Advancing Neural Encoding of
Portuguese with Transformer Albertina PT-*. In: Progress in Artificial Intelligence; 2023. p. 441–453.
[82] Schneider ETR, Gumiel YB, de Souza JVA, Mie Mukai L, Emanuel Silva e Oliveira L, de Sa Rebelo
M, et al. CardioBERTpt: Transformer-based Models for Cardiology Language Representation in Por-
tuguese.
In: IEEE 36th International Symposium on Computer-Based Medical Systems; 2023. p.
378–381.
[83] Viegas CFO, Costa BC, Ishii RP. JurisBERT: A New Approach that Converts a Classification Corpus
into an STS One. In: Gervasi O, Murgante B, Taniar D, Apduhan BO, Braga AC, Garau C, et al., edi-
tors. Computational Science and Its Applications – ICCSA 2023. Cham: Springer Nature Switzerland;
2023. p. 349–365.
[84] Larcher C, Piau M, Finardi P, Gengo P, Esposito P, Carid´a V. Cabrita: Closing the Gap for Foreign
Languages. arXiv:230811878. 2023;.
[85] Costa PB, Pavan MC, Santos WR, Silva SC, Paraboni I. BERTabaporu: Assessing a Genre-Specific
Language Model for Portuguese NLP. In: 14th International Conference on Recent Advances in Natural
Language Processing; 2023. p. 217–223.
[86] Campiotti I, Rodrigues M, Albuquerque Y, Azevedo R, Andrade A.
DeBERTinha: A Multistep
Approach to Adapt DebertaV3 XSmall for Brazilian Portuguese Natural Language Processing Task.
230916844. 2023;.
[87] Silveira R, Ponte C, Almeida V, Pinheiro V, Furtado V. LegalBert-pt: A Pretrained Language Model
for the Brazilian Portuguese Legal Domain. In: Intelligent Systems; 2023. p. 268–282.
[88] Garcia GL, Paiola PH, Morelli LH, Candido G, J´unior AC, Jodas DS, et al. Introducing Bode: A
Fine-Tuned Large Language Model for Portuguese Prompt-Based Task. CoRR. 2024;.
[89] Corrˆea NK, Falk S, Fatimah S, Sen A, De Oliveira N. TeenyTinyLlama: open-source tiny language
models trained in Brazilian Portuguese. Machine Learning with Applications. 2024;16:100558.
[90] de Mello GL, Finger M, , Serras F, de Mello Carpi M, Jose MM, et al. PeLLE: Encoder-based language
models for Brazilian Portuguese based on open data. arXiv:240219204. 2024;[cs.CL].
[91] Lopes R, Magalh˜aes J, Semedo D.
Gl´orIA: A Generative and Open Large Language Model for
Portuguese. PROPOR 2024. 2024;p. 441.
[92] Santos R, Silva J, Gomes L, Rodrigues J, Branco A. Advancing Generative AI for Portuguese with
Open Decoder Gerv´asio PT. In: 3rd Annual Meeting of the Special Interest Group on Under-resourced
Languages@ LREC-COLING 2024; 2024. p. 16–26.
[93] Garcia EAS, Silva NFF, Siqueira F, Albuquerque HO, Gomes JRS, Souza E, et al. RoBERTaLexPT: A
Legal RoBERTa Model pretrained with deduplication for Portuguese. In: 16th International Conference
on Computational Processing of Portuguese; 2024. p. 374–383.
[94] Almeida TS, Abonizio H, Nogueira R, Pires R.
Sabi´a-2: A New Generation of Portuguese Large
Language Models. arXiv:240309887. 2024;.
[95] Junior RM, Pires R, Romero R, Nogueira R.
Juru: Legal Brazilian Large Language Model from
Reputable Sources. arXiv:240318140. 2024;.
[96] Piau M, Lotufo R, Nogueira R. ptt5-v2: A Closer Look at Continued Pretraining of T5 Models for
the Portuguese Language. In: Paes A, Verri FAN, editors. Intelligent Systems. Cham: Springer Nature
Switzerland; 2025. p. 324–338.
34

--- Page 35 ---

[97] Gomes L, Branco A, Silva J, Rodrigues J, Santos R. Open Sentence Embeddings for Portuguese with
the Serafim PT* Encoders Family. In: Santos MF, Machado J, Novais P, Cortez P, Moreira PM,
editors. Progress in Artificial Intelligence. Cham: Springer Nature Switzerland; 2025. p. 267–279.
[98] Nunes M, Bon´e J, Ferreira JC, Chaves P, Elvas LB. MediAlbertina: An European Portuguese medical
language model. Computers in Biology and Medicine. 2024 Nov;182:109233. https://doi.org/10.1016/
j.compbiomed.2024.109233.
[99] Abonizio H, Almeida TS, Laitz T, Junior RM, Bon´as GK, Nogueira R, et al. Sabi´a-3 Technical Report.
arXiv:241012049. 2025 Feb;https://doi.org/10.48550/arXiv.2410.12049.
[100] Corrˆea NK, Sen A, Falk S, Fatimah S. Tucano: Advancing Neural Text Generation for Portuguese.
arXiv:241107854. 2024 Nov;https://doi.org/10.48550/arXiv.2411.07854.
[101] Gamallo P, Rodr´ıguez P, Santos D, Sotelo S, Miquelina N, Paniagua S, et al. A Galician-Portuguese
Generative Model. In: Santos MF, Machado J, Novais P, Cortez P, Moreira PM, editors. Progress in
Artificial Intelligence. Cham: Springer Nature Switzerland; 2025. p. 292–304.
[102] Simpl´ıcio A, Semedo D, Magalhaes J. V-Gl´orIA - Customizing Large Vision and Language Models
to European Portuguese. In: Kumar S, Balachandran V, Park CY, Shi W, Hayati SA, Tsvetkov Y,
et al., editors. 1st Workshop on Customizable NLP: Progress and Challenges in Customizing NLP for
a Domain, Application, Group, or Individual (CustomNLP4U). Miami, Florida, USA: Association for
Computational Linguistics; 2024. p. 317–326.
[103] Garcia GL, Paiola PH, Garcia E, Ribeiro Manesco JR, Papa JP. GemBode and PhiBode: Adapting
Small Language Models to Brazilian Portuguese. In: Hern´andez-Garc´ıa R, Barrientos RJ, Velastin SA,
editors. Progress in Pattern Recognition, Image Analysis, Computer Vision, and Applications. Cham:
Springer Nature Switzerland; 2025. p. 228–243.
[104] Carneiro F, Vianna D, Carvalho J, Plastino A, Paes A.
BERTweet.BR: A pre-trained language
model for tweets in Portuguese.
Neural Computing and Applications. 2025 Feb;37(6):4363–4385.
https://doi.org/10.1007/s00521-024-10711-3.
[105] Silva MO, Oliveira GP, Costa LGL, Pappa GL. GovBERT-BR: A BERT-Based Language Model for
Brazilian Portuguese Governmental Data. In: Paes A, Verri FAN, editors. Intelligent Systems. Cham:
Springer Nature Switzerland; 2025. p. 19–32.
[106] Pires H, Paucar L, Carvalho JP.
DeB3RTa: A Transformer-Based Model for the Portuguese
Financial Domain.
Big Data and Cognitive Computing. 2025 Mar;9(3):51.
Number: 3 Publisher:
Multidisciplinary Digital Publishing Institute. https://doi.org/10.3390/bdcc9030051.
[107] Fish B, Kun J, ´Ad´am D Lelkes. In: A Confidence-Based Approach for Balancing Fairness and Accuracy.
SIAM International Conference on Data Mining; 2016. p. 144–152.
[108] Ryffel T, Trask A, Dahl M, Wagner B, Mancuso J, Rueckert D, et al. A generic framework for privacy
preserving deep learning. CoRR. 2018;.
[109] Narayanan M, Schoeberl C. A Matrix for Selecting Responsible AI Frameworks. Center for Security
and Emerging Technology https://cset georgetown edu/wp-content/uploads/CSET-A-Matrix-for-
Selecting-Responsible-AI-Frameworks pdf. 2023;.
[110] IFTF.: A Playbook for Ethical Technology Governance. 2021. Available from: https://www.iftf.org/
projects/a-playbook-for-ethical-tech-governance/?
[111] Vyhmeister E, Castane G, ¨Ostberg PO, Thevenin S.
A responsible AI framework: pipeline
contextualisation. AI and Ethics. 2023;3(1):175–197. https://doi.org/10.1007/s43681-022-00154-8.
[112] Wachter S, Mittelstadt B. A right to reasonable inferences: Re-thinking data protection law in the
age of big data and AI. Colum Bus L Rev. 2019;p. 494.
35

--- Page 36 ---

[113] Guidotti R, Monreale A, Ruggieri S, Turini F, Giannotti F, Pedreschi D. A Survey of Methods for
Explaining Black Box Models. ACM Computing Surveys. 2018 Aug;51(5). https://doi.org/10.1145/
3236009.
[114] Friedman B, Hendry DG, Borning A. A Survey of Value Sensitive Design Methods. Foundations and
Trends® in Human–Computer Interaction. 2017;11(2):63–125. https://doi.org/10.1561/1100000015.
[115] Oetzel MC, and SS.
A systematic methodology for privacy impact assessments: A design science
approach. European Journal of Information Systems. 2014;23(2):126–150. https://doi.org/10.1057/
ejis.2013.18.
[116] Dom´ınguez Hern´andez A, Galanos V. A toolkit of dilemmas: Beyond debiasing and fairness formulas
for responsible AI/ML. In: IEEE International Symposium on Technology and Society (ISTAS). vol. 1;
2022. p. 1–4.
[117] Schmager S, Sousa S. A Toolkit to Enable the Design of Trustworthy AI. In: Stephanidis C, Kurosu M,
Chen JYC, Fragomeni G, Streitz N, Konomi S, et al., editors. HCI International 2021 - Late Breaking
Papers: Multimodality, eXtended Reality, and Artificial Intelligence. Cham: Springer International
Publishing; 2021. p. 536–555.
[118] ai A.: A3i the Trust in AI Framework. 2025. Available from: http://a3i.ai/trust-in-ai.
[119] Kolter Z, Madry A.: Adversarial Robustness - Theory and Practice. 2018. Available from: https:
//adversarial-ml-tutorial.org/.
[120] Accenture.: Accenture Fairness Evaluation Tool. 2019. Available from: https://www.nist.gov/system/
files/documents/2019/06/11/nist-ai-rfi-accenture-001.pdf.
[121] Kroll JA, Huey J, Barocas S, Felten EW, Reidenberg JR, Robinson DG, et al. Accountable Algorithms,
165 U. Pa L Rev. 2017;633:633.
[122] Butnaru C.: Agile Ethics for AI (HAI).
2018.
Available from: https://trello.com/b/SarLFYOd/
agile-ethics-for-ai-hai.
[123] Mantelero A. AI and Big Data: A blueprint for a human rights, social and ethical impact assessment.
Computer Law & Security Review. 2018;34(4):754–772. https://doi.org/10.1016/j.clsr.2018.05.017.
[124] Calderon A, Taber D, Qu H, Wen J.: AI Blindspots: A discovery process for spotting unconscious biases
and structural inequalities in AI systems. 2019. Available from: https://aiblindspot.media.mit.edu/.
[125] Commons A.: AI Commons. 2016. Available from: https://ai-commons.org/.
[126] Ortega E, Tran M, Bandeen G. AI Digital Tool Product Lifecycle Governance Framework through
Ethics and Compliance by Design†. In: IEEE Conference on Artificial Intelligence (CAI); 2023. p.
353–356.
[127] Bellamy RK, Dey K, Hind M, Hoffman SC, Houde S, Kannan K, et al. AI Fairness 360: An extensible
toolkit for detecting and mitigating algorithmic bias. IBM Journal of Research and Development.
2019;63(4/5):4–1.
[128] Database AI.: Welcome to the Artificial Intelligence Incident Database. 2025. Available from: https:
//incidentdatabase.ai/.
[129] Wahle JP, Ruas T, Mohammad SM, Meuschke N, Gipp B. AI Usage Cards: Responsibly Reporting AI-
Generated Content. In: ACM/IEEE Joint Conference on Digital Libraries (JCDL); 2023. p. 282–284.
[130] at Northwestern University CJL.: Algorithm Tips - Resources and leads for investigating algorithms
in society. 2019. Available from: http://algorithmtips.org/.
36

--- Page 37 ---

[131] Binns R. Algorithmic accountability and public reason. Philosophy & technology. 2018;31(4):543–556.
https://doi.org/10.1007/s13347-017-0263-5.
[132] Institute AN.: Algorithmic Accountability Policy Toolkit. 2018. Available from: https://ainowinstitute.
org/publication/algorithmic-accountability-policy-toolkit.
[133] and ND. Algorithmic Accountability. Digital Journalism. 2015;3(3):398–415. https://doi.org/10.1080/
21670811.2014.976411.
[134] of Canada G.: Algorithmic Impact Assessment tool.
2020.
Available from: https://www.canada.
ca/en/government/system/digital-government/digital-government-innovations/responsible-use-ai/
algorithmic-impact-assessment.html.
[135] Datta A, Sen S, Zick Y. Algorithmic Transparency via Quantitative Input Influence: Theory and
Experiments with Learning Systems. In: IEEE Symposium on Security and Privacy (SP); 2016. p.
598–617.
[136] Klaise J, Looveren AV, Vacanti G, Coca A. Alibi Explain: Algorithms for Explaining Machine Learning
Models. Journal of Machine Learning Research. 2021;22(181):1–7.
[137] Hardt M, Chen X, Cheng X, Donini M, Gelman J, Gollaprolu S, et al. Amazon SageMaker Clarify:
Machine Learning Bias Detection and Explainability in the Cloud. In: 27th ACM SIGKDD Conference
on Knowledge Discovery & Data Mining. KDD ’21. New York, NY, USA: Association for Computing
Machinery; 2021. p. 2974–2983.
[138] Van de Poel I. An ethical framework for evaluating experimental technology. Science and engineering
ethics. 2016;22(3):667–686. https://doi.org/10.1007/s11948-015-9724-3.
[139] Vallor S, Green B, Raicu I.: An Ethical Toolkit for Engineering/Design Practice – The Markkula
Center for Applied Ethics at Santa Clara University. 2018. Available from: https://www.scu.edu/
ethics-in-technology-practice/ethical-toolkit/.
[140] Bluemke DA, Moy L, Bredella MA, Ertl-Wagner BB, Fowler KJ, Goh VJ, et al.: Assessing radiology
research on artificial intelligence: A brief guide for authors, reviewers, and readers – from the radiology
editorial board. Radiological Society of North America. 2020.
[141] team at pymetrics DS.: Audit-AI: Open Sourced Bias Testing for Generalized Machine Learning
Applications. 2019. Available from: https://github.com/pymetrics/audit-ai.
[142] Group AAR, of Computer Sciences at Northeastern University KC.: Auditing Algorithms @ North-
eastern. 2025. Available from: https://personalization.ccs.neu.edu/.
[143] Sandvig C, Hamilton K, Karahalios K, Langbort C.
Auditing Algorithms: Research Methods for
Detecting Discrimination on Internet Platforms. Data and discrimination: converting critical concerns
into productive inquiry. 2014;22(2014):4349–4357.
[144] Papakyriakopoulos O, Choi ASG, Thong W, Zhao D, Andrews J, Bourke R, et al.
Augmented
Datasheets for Speech Datasets and Ethical Decision-Making.
In: ACM Conference on Fairness,
Accountability, and Transparency. FAccT ’23. New York, NY, USA: Association for Computing
Machinery; 2023. p. 881–904.
[145] Ribeiro MT, Wu T, Guestrin C, Singh S. Beyond Accuracy: Behavioral Testing of NLP Models with
CheckList.
In: Jurafsky D, Chai J, Schluter N, Tetreault J, editors. 58th Annual Meeting of the
Association for Computational Linguistics. Online: Association for Computational Linguistics; 2020.
p. 4902–4912.
[146] Sandler
R,
Basl
J,
Tiell
S.:
Building
Data
and
Artificial
Intelligence
Ethics
Commit-
tees
–
Accenture.
Accenture
and
Ethics
Institute
at
Northeastern
University.
2019.
Available
from:
https://cssh.northeastern.edu/ethics/wp-content/uploads/sites/31/2021/08/
37

--- Page 38 ---

Building Data and AI Ethics Committees.pdf.
[147] Captum.: Captum - Model Interpretability for PyTorch. 2019. Available from: https://github.com/
pymetrics/audit-ai.
[148] FROG.: Cards for Humanity. 2020. Available from: https://cardsforhumanity.frog.co/.
[149] Feldman M, Friedler SA, Moeller J, Scheidegger C, Venkatasubramanian S. Certifying and Removing
Disparate Impact. In: 21th ACM SIGKDD International Conference on Knowledge Discovery and
Data Mining. KDD ’15. New York, NY, USA: Association for Computing Machinery; 2015. p. 259–268.
[150] Ehsan U, Saha K, De Choudhury M, Riedl MO. Charting the Sociotechnical Gap in Explainable AI:
A Framework to Address the Gap in XAI. ACM Transactions on Computer-Human Interaction. 2023
Apr;7(CSCW1). https://doi.org/10.1145/3579467.
[151] Papernot N, Faghri F, Carlini N, Goodfellow I, Feinman R, Kurakin A, et al. Technical Report on
the CleverHans v2.1.0 Adversarial Examples Library. arXiv:161000768. 2018;.
[152] Madaio MA, Stark L, Wortman Vaughan J, Wallach H.
Co-Designing Checklists to Understand
Organizational Challenges and Opportunities around Fairness in AI. In: CHI Conference on Human
Factors in Computing Systems. CHI ’20. New York, NY, USA: Association for Computing Machinery;
2020. p. 1–14.
[153] Wachter S, Mittelstadt B, Russell C. Counterfactual Explanations without Opening the Black Box:
Automated Decisions and the GDPR. arXiv:171100399. 2018;https://doi.org/10.48550/arXiv.1711.
00399. [cs.AI].
[154] Kusner MJ, Loftus J, Russell C, Silva R. Counterfactual Fairness. In: Guyon I, Luxburg UV, Bengio
S, Wallach H, Fergus R, Vishwanathan S, et al., editors. Advances in Neural Information Processing
Systems. vol. 30. Curran Associates, Inc.; 2017. .
[155] CISA.: Cyber Resilience Review. 2025. Available from: https://www.cisa.gov/resources-tools/services/
cyber-resilience-review-crr.
[156] Pushkarna M, Zaldivar A, Kjartansson O. Data Cards: Purposeful and Transparent Dataset Docu-
mentation for Responsible AI. In: ACM Conference on Fairness, Accountability, and Transparency.
FAccT ’22. New York, NY, USA: Association for Computing Machinery; 2022. p. 1776–1826.
[157] Institute OD.: Data Ethics Canvas user guide V2. 2018. Available from: https://docs.google.com/
document/d/1MkvoAP86CwimbBD0dxySVCO0zeVOput bu1A6kHV73M/edit?tab=t.0#heading=h.
n0a7uoc7jz.
[158] UK
G.:
Data
Ethics
Framework:
Legislation
and
Codes
of
Practice
for
Use
of
Data.
2020.
Available
from:
https://www.gov.uk/government/publications/data-ethics-framework/
data-ethics-framework-legislation-and-codes-of-practice-for-use-of-data.
[159] Academy B, the Royal Society.: Data Management and Use: Governance in the 21st Century. The
British Academy and the Royal Society London. 2017. Available from: https://royalsociety.org/∼/
media/policy/projects/data-governance/data-management-governance.pdf.
[160] Antignac T, Sands D, Schneider G. Data Minimisation: A Language-Based Approach. In: De Cap-
itani di Vimercati S, Martinelli F, editors. ICT Systems Security and Privacy Protection. Cham:
Springer International Publishing; 2017. p. 442–456.
[161] McMillan-Major A, Bender EM, Friedman B.
Data Statements: From Technical Concept to
Community Practice. ACM J Responsib Comput. 2024 Mar;1(1). https://doi.org/10.1145/3594737.
[162] Data School UU.: Data Ethics Framework: legislation and codes of practice for use of data. 2017.
Available from: https://deda.dataschool.nl/.
38

--- Page 39 ---

[163] Simonyan K, Vedaldi A, Zisserman A. Deep Inside Convolutional Networks: Visualising Image Classi-
fication Models and Saliency Maps. arXiv:13126034. 2014;https://doi.org/https://doi.org/10.48550/
arXiv.1312.6034. [cs.CV].
[164] Li O, Liu H, Chen C, Rudin C. Deep learning for case-based reasoning through prototypes: A neural
network that explains its predictions. In: AAAI Conference on Artificial Intelligence. vol. 32; 2018. .
[165] DeepExplain.:
DeepExplain.
2017.
Available
from:
https://edwinwenink.github.io/
ai-ethics-tool-landscape/tools/deepexplain/.
[166] DeepLIFT.:
DeepLIFT.
2017.
Available
from:
https://edwinwenink.github.io/
ai-ethics-tool-landscape/tools/deeplift/.
[167] Deon.: An ethics checklist for data scientists. 2025. Available from: https://deon.drivendata.org/.
[168] Ethically D.: Design Ethically Toolkit. 2023. Available from: https://www.designethically.com/.
[169] Peters D, Calvo RA, Ryan RM.
Designing for Motivation, Engagement and Wellbeing in Digital
Experience. Frontiers in Psychology. 2018;Volume 9 - 2018. https://doi.org/10.3389/fpsyg.2018.00797.
[170] Suphakul T, Senivongse T. Development of privacy design patterns based on privacy principles and
UML. In: 18th IEEE/ACIS International Conference on Software Engineering, Artificial Intelligence,
Networking and Parallel/Distributed Computing (SNPD); 2017. p. 369–375.
[171] Shang X, Peng Z, Yuan Q, Khan S, Xie L, Fang Y, et al. DIANES: A DEI Audit Toolkit for News
Sources. In: 45th International ACM SIGIR Conference on Research and Development in Information
Retrieval. SIGIR ’22. New York, NY, USA: Association for Computing Machinery; 2022. p. 3312–3317.
[172] Mothilal RK, Sharma A, Tan C. Explaining machine learning classifiers through diverse counterfac-
tual explanations. In: Conference on Fairness, Accountability, and Transparency; 2020. p. 607–617.
Available from: https://github.com/interpretml/DiCE.
[173] Lab DCS.: Digital Impact Toolkit. 2025. Available from: https://digitalimpact.io/toolkit/.
[174] ELI5.: ELI5.
2016.
Available from: https://edwinwenink.github.io/ai-ethics-tool-landscape/tools/
eli5/.
[175] SAS E.: Ellpha. 2025. Available from: https://ellpha.ai/.
[176] Forum WE.: Empowering AI Leadership. 2025. Available from: https://new.express.adobe.com/page/
RsXNkZANwMLEf/.
[177] Forum WE.: Empowering AI Leadership: AI C-Suite Toolkit. 2022. Available from: https://www.
weforum.org/publications/empowering-ai-leadership-ai-c-suite-toolkit/.
[178] Shrobe H, Shrier DL, Pentland A. In: Enigma: Decentralized Computation Platform with Guaranteed
Privacy. MIT Press; 2018. p. 425–454.
[179] Ashok M, Madan R, Joha A, Sivarajah U. Ethical framework for Artificial Intelligence and Digital
technologies. International Journal of Information Management. 2022;62:102433. https://doi.org/10.
1016/j.ijinfomgt.2021.102433.
[180] Agbese M, Mohanani R, Khan AA, Abrahamsson P. Ethical Requirements Stack: A framework for
implementing ethical requirements of AI in software engineering practices.
In: 27th International
Conference on Evaluation and Assessment in Software Engineering. EASE ’23. New York, NY, USA:
Association for Computing Machinery; 2023. p. 326–328.
[181] Shahriari K, Shahriari M. IEEE standard review—Ethically aligned design: A vision for prioritizing
human wellbeing with artificial intelligence and autonomous systems. In: IEEE Canada International
39

--- Page 40 ---

Humanitarian Technology Conference (IHTC). IEEE; 2017. p. 197–201.
Available from: https://
standards.ieee.org/wp-content/uploads/import/documents/other/ead v2.pdf.
[182] Anderson D, Bonaguro J, McKinney M, Nicklin A, Wiseman J.: Ethics & Algorithms Toolkit. 2025.
Available from: https://ethicstoolkit.ai/.
[183] Stahl BC, Wright D. Ethics and Privacy in AI and Big Data: Implementing Responsible Research and
Innovation. IEEE Security & Privacy. 2018;16(3):26–33. https://doi.org/10.1109/MSP.2018.2701164.
[184] Hesketh P.: Ethics Cards. 2025. Available from: http://ethicskit.org/ethics-cards.html.
[185] Ethics Kit.: Ethics Kit Tools. 2025. Available from: http://ethicskit.org/tools.html.
[186] EthicsNet.: EthicsNet. 2025. Available from: https://www.ethicsnet.org/about.
[187] Sokol K, Flach P. Explainability fact sheets: a framework for systematic assessment of explainable
approaches. In: Conference on Fairness, Accountability, and Transparency. FAT* ’20. New York, NY,
USA: Association for Computing Machinery; 2020. p. 56–67.
[188] Oxborough C, Cameron E, Rao A, Birchall A, Townsend A, Westermann C. Explainable AI: Driving
business value through greater understanding. Retrieved from PWC website: https://www pwc co
uk/audit-assurance/assets/explainable-ai pdf. 2018;.
[189] Lepri B, Oliver N, Letouz´e E, Pentland A, Vinck P. Fair, transparent, and accountable algorithmic
decision-making processes: The premise, the proposed solutions, and the open challenges. Philosophy
& Technology. 2018;31(4):611–627. https://doi.org/https://doi.org/10.1007/s13347-017-0279-x.
[190] Bird S, Dud´ık M, Edgar R, Horn B, Lutz R, Milan V, et al. Fairlearn: A toolkit for assessing and
improving fairness in AI. Microsoft, Tech Rep MSR-TR-2020-32. 2020;.
[191] Zafar MB, Valera I, Rogriguez MG, Gummadi KP. Fairness Constraints: Mechanisms for Fair Clas-
sification. In: Singh A, Zhu J, editors. 20th International Conference on Artificial Intelligence and
Statistics. vol. 54 of Proceedings of Machine Learning Research. PMLR; 2017. p. 962–970.
[192] Zafar MB, Valera I, Rodriguez MG, Gummadi K, Weller A.: Fairness in Classification. 2016. Available
from: https://github.com/mbilalzafar/fair-classification.
[193] Agarwal A, Agarwal H, Agarwal N. Fairness Score and process standardization: Framework for fairness
certification in artificial intelligence systems. AI and Ethics. 2023;3(1):267–279. https://doi.org/https:
//doi.org/10.1007/s43681-022-00147-7.
[194] Rauber J, Brendel W, Bethge M. Foolbox: A Python toolbox to benchmark the robustness of machine
learning models. arXiv:170704131. 2018;https://doi.org/10.48550/arXiv.1707.04131. [cs.LG].
[195] Institute OR.: Foresight into AI Ethics (FAIE): A toolkit for creating an ethics roadmap for
your AI project.
2019.
Available from: https://openroboethics.org/wp-content/uploads/2021/07/
ORI-Foresight-into-Artificial-Intelligence-Ethics-Launch-V1.pdf.
[196] Sharma V, Mishra N, Kukreja V, Alkhayyat A, Elngar AA.
Framework for Evaluating Ethics in
AI. In: International Conference on Innovative Data Communication Technologies and Application
(ICIDCA); 2023. p. 307–312.
[197] Glenn J.: Futures Wheel. 2025. Available from: http://ethicskit.org/futures-wheel.html.
[198] Joshi C, Kaloskampis I, Nolan L. Generative Adversarial Networks (GANs) for Synthetic Dataset
Generation with Binary Classes. Data Science Campus, Feb. 2019;21.
40

--- Page 41 ---

[199] Sokol K, Flach P.
Glass-Box: Explaining AI Decisions With Counterfactual Statements Through
Conversation With a Voice-enabled Virtual Assistant. In: Twenty-Seventh International Joint Con-
ference on Artificial Intelligence, IJCAI-18. International Joint Conferences on Artificial Intelligence
Organization; 2018. p. 5868–5870.
[200] Officer I.: Guide to the UK general data protection regulation (UK GDPR). 2025. Available from:
https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/.
[201] H2O ai.: H2O.ai Machine Learning Interpretability Resources. 2017. Available from: https://github.
com/h2oai/mli-resources.
[202] Microsoft.: HAX Workbook.
2025.
Available from: https://www.microsoft.com/en-us/haxtoolkit/
workbook/.
[203] Hazy.: Hazy. 2025. Available from: https://hazy.com/.
[204] Adams L, Burall S.: How to stimulate effective public engagement on the ethics of artificial intelligence.
Involve: London.
2019.
Available from: https://www.involve.org.uk/sites/default/files/uploads/
docuemnt/How%20to%20stimulate%20effective%20public%20debate%20on%20the%20ethics%20of%
20artificial%20intelligence%20.pdf.
[205] Kleinberg J, Lakkaraju H, Leskovec J, Ludwig J, Mullainathan S. Human Decisions and Machine
Predictions. The Quarterly Journal of Economics. 2017 Aug;133(1):237–293. https://doi.org/10.1093/
qje/qjx032.
[206] Studio IW.: IBM Watson OpenScale.
2025.
Available from: https://www.ibm.com/uk-en/cloud/
watson-openscale.
[207] Graham C.
Anonymisation: Managing Data Protection Risk Code of Practice.
Information
Commissioner’s Office. 2012;.
[208] Office
IC.:
Guide
to
the
General
Data
Protection
Regulation
(GDPR).
2025.
Available
from:
https://ico.org.uk/for-organisations/guide-to-data-protection/
guide-to-the-general-data-protection-regulation-gdpr/.
[209] Olszewska JI, Systems, Committee SES, et al. IEEE standard model process for addressing ethical
concerns during system design: IEEE standard 7000-2021. IEEE. 2021;.
[210] IEEE.: IEEE Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems
on Human Well-Being.
2022.
Available from: https://standards.ieee.org/industry-connections/ec/
autonomous-systems.html.
[211] IEEE.: IEEE Ethics Certification Program for Autonomous and Intelligent Systems (ECPAIS). 2020.
Available from: https://standards.ieee.org/industry-connections/ecpais.html.
[212] Zhao WW. Improving Social Responsibility of Artificial Intelligence by Using ISO 26000. IOP Con-
ference Series: Materials Science and Engineering. 2018 Sep;428(1):012049. https://doi.org/10.1088/
1757-899X/428/1/012049.
[213] Crisan A, Drouhard M, Vig J, Rajani N. Interactive Model Cards: A Human-Centered Approach to
Model Documentation. In: ACM Conference on Fairness, Accountability, and Transparency. FAccT
’22. New York, NY, USA: Association for Computing Machinery; 2022. p. 427–439.
[214] Nori H, Jenkins S, Koch P, Caruana R. InterpretML: A Unified Framework for Machine Learning
Interpretability. arXiv preprint arXiv:190909223. 2019;.
[215] Madras D, Creager E, Pitassi T, Zemel R.
Learning Adversarially Fair and Transferable Rep-
resentations.
In: Dy J, Krause A, editors. 35th International Conference on Machine Learning.
vol. 80 of Proceedings of Machine Learning Research. PMLR; 2018. p. 3384–3393. Available from:
41

--- Page 42 ---

https://proceedings.mlr.press/v80/madras18a.html.
[216] Shrikumar A, Greenside P, Kundaje A. Learning Important Features Through Propagating Activation
Differences. In: Precup D, Teh YW, editors. 34th International Conference on Machine Learning.
vol. 70 of Proceedings of Machine Learning Research. PMLR; 2017. p. 3145–3153.
[217] Johansson F, Shalit U, Sontag D. Learning Representations for Counterfactual Inference. In: Balcan
MF, Weinberger KQ, editors. 33rd International Conference on Machine Learning. vol. 48 of Proceed-
ings of Machine Learning Research. New York, New York, USA: PMLR; 2016. p. 3020–3029. Available
from: https://proceedings.mlr.press/v48/johansson16.html.
[218] Bolukbasi T, Chang KW, Zou JY, Saligrama V, Kalai AT.
Man is to Computer Programmer as
Woman is to Homemaker? Debiasing Word Embeddings. Advances in neural information processing
systems. 2016;29.
[219] Hoffman RR, Mueller ST, Klein G, Litman J. Metrics for Explainable AI: Challenges and Prospects.
arXiv:181204608. 2019;https://doi.org/10.48550/arXiv.1812.04608. [cs.AI].
[220] Microsoft.:
Microsoft’s
framework
for
building
AI
systems
responsibly.
2022.
Available
from:
https://blogs.microsoft.com/on-the-issues/2022/06/21/
microsofts-framework-for-building-ai-systems-responsibly/?ref=blog.salesforceairesearch.com.
[221] Foundation IA.: Model Ethical Data Impact Assessment.
2019.
Available from: https://www.
informationaccountability.org/publications.
[222] Bassily R, Thakkar O, Thakurta A. Model-Agnostic Private Learning via Stability. arXiv:180305101.
2018;https://doi.org/https://doi.org/10.48550/arXiv.1803.05101. [cs.LG].
[223] Machine M.: Moral Machine. 2025. Available from: https://www.moralmachine.net/.
[224] Seedat N, Imrie F, Schaar Mvd.
Navigating Data-Centric Artificial Intelligence With DC-Check:
Advances, Challenges, and Opportunities.
IEEE Transactions on Artificial Intelligence. 2024
Jun;5(6):2589–2603. https://doi.org/10.1109/tai.2023.3345805.
[225] Group K.: Neural Network Exchange Format. 2025. Available from: https://www.khronos.org/nnef#:
%7E:text=Neural%20Network%20Exchange%20Format%20%20(NNEF,range%20of%20devices%
20and%20platforms.
[226] Kit E.: New Economy Impact Model.
2025.
Available from: http://ethicskit.org/downloads/
economy-impact-model.pdf.
[227] Bach S, Binder A, Montavon G, Klauschen F, M¨uller KR, Samek W. On Pixel-Wise Explanations for
Non-Linear Classifier Decisions by Layer-Wise Relevance Propagation. PLOS One. 2015 Jul;10(7):1–
46. https://doi.org/10.1371/journal.pone.0130140.
[228] ONNX.: Open Neural Network Exchange. 2017. Available from: https://github.com/onnx.
[229] Foundation O.: OpenMined. 2025. Available from: https://openmined.org/.
[230] The Open Machine Learning Foundation.: OpenML. 2025. Available from: https://www.openml.org/
about.
[231] Goldstein A, Kapelner A, Bleich J, and EP. Peeking Inside the Black Box: Visualizing Statistical
Learning With Plots of Individual Conditional Expectation. Journal of Computational and Graphical
Statistics. 2015;24(1):44–65. https://doi.org/10.1080/10618600.2014.907095.
[232] PAIR G.: People + AI Research Guidebook.
2019.
Available from: https://pair.withgoogle.com/
guidebook/.
42

--- Page 43 ---

[233] Orcutt
M.:
Personal
AI
privacy
watchdog
could
help
you
regain
control
of
your
data.
MIT Technology Review.
2017.
Available from: https://www.technologyreview.com/s/607830/
personal-ai-privacy-watchdog-could-help-you-regain-control-of-your-data/.
[234] Guazzelli A, Zeller M, Lin WC, Williams G. PMML: An open standard for sharing models. The R
Journal. 2009;.
[235] Dennis LA, Fisher M, Lincoln NK, Lisitsa A, Veres SM. Practical verification of decision-making in
agent-based autonomous systems. Automated Software Engineering. 2016;23:305–359. https://doi.
org/10.1007/s10515-014-0168-9.
[236] Diakopoulos N, Friedler S, Arenas M, Barocas S, Hay M, Howe B, et al.: Principles for Accountable
Algorithms and a Social Impact Statement for Algorithms. (2025). Available from: https://www.
fatml.org/resources/principles-for-accountable-algorithms.
[237] Cavoukian A, Taylor S, Abrams ME. Privacy by Design: essential for organizational accountability and
strong business practices. Identity in the Information Society. 2010;3:405–413. https://doi.org/https:
//doi.org/10.1007/s12394-010-0053-z.
[238] Makri EL, Lambrinoudakis C. Privacy Principles: Towards a Common Privacy Audit Methodology.
In: Fischer-H¨ubner S, Lambrinoudakis C, L´opez J, editors. Trust, Privacy and Security in Digital
Business. Cham: Springer International Publishing; 2015. p. 219–234.
[239] Souza R, Azevedo L, Louren¸co V, Soares E, Thiago R, Brand˜ao R, et al. Provenance Data in the
Machine Learning Lifecycle in Computational Science and Engineering. In: IEEE/ACM Workflows in
Support of Large-Scale Science (WORKS); 2019. p. 1–10.
[240] Overdorf R, Kulynych B, Balsa E, Troncoso C, G¨urses S. Questioning the assumptions behind fairness
solutions. arXiv:181111293. 2018;[cs.CY].
[241] RAIL.: Responsible AI Licenses (RAIL). (2025). Available from: https://www.licenses.ai/ai-licenses.
[242] AI MR.: Responsible AI Toolbox. 2022. Available from: https://responsibleaitoolbox.ai/.
[243] TensorFlow.: Responsible AI Toolkit. (2025). Available from: https://www.tensorflow.org/responsible
ai.
[244] Sandoval JCB, de Santana VF, Berger S, Quigley LT, Hobson S. Responsible and Inclusive Technology
Framework: A Formative Framework to Promote Societal Considerations in Information Technology
Contexts. arXiv:230211565. 2023;https://doi.org/10.48550/arXiv.2302.11565. [cs.CY].
[245] Behera RK, Bala PK, Rana NP, Irani Z.
Responsible natural language processing: A principlist
framework for social benefits. Technological Forecasting and Social Change. 2023;188:122306. https:
//doi.org/10.1016/j.techfore.2022.122306.
[246] Pulse UG.: Risks, Harms and Benefits Assessment Tool.
2018.
Available from: https://www.
unglobalpulse.org/document/risks-harms-and-benefits-assessment-tool/.
[247] Dinan E, Abercrombie G, Bergman SA, Spruit S, Hovy D, Boureau YL, et al. SafetyKit: First aid for
measuring safety in open-domain conversational systems. In: 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers). Association for Computational Linguistics;
2022. Available from: https://iris.unibocconi.it/bitstream/11565/4053224/1/2022.acl-long.284.pdf.
[248] Papernot N, Song S, Mironov I, Raghunathan A, Talwar K, Erlingsson U. Scalable Private Learning
with PATE. In: International Conference on Learning Representations; 2018. .
[249] Green N, Procope C, Cheema A, Adediji A. System Cards, a new resource for understanding how AI
systems work. Meta AI. 2021;.
43

--- Page 44 ---

[250] Zook M, Barocas S, boyd d, Crawford K, Keller E, Gangadharan SP, et al. Ten simple rules for
responsible big data research.
PLOS Computational Biology. Mar;13(3):1–10.
https://doi.org/10.
1371/journal.pcbi.1005399.
[251] Indicators TF.: Tensorflow’s Fairness Evaluation and Visualization Toolkit. 2020. Available from:
https://github.com/tensorflow/fairness-indicators.
[252] Simig D, Wang T, Dankers V, Henderson P, Batsuren K, Hupkes D, et al. Text Characterization
Toolkit (TCT).
In: Buntine W, Liakata M, editors. 2nd Conference of the Asia-Pacific Chapter
of the Association for Computational Linguistics and the 12th International Joint Conference on
Natural Language Processing: System Demonstrations. Taipei, Taiwan: Association for Computational
Linguistics; 2022. p. 72–87.
[253] Arnold T, Scheutz M. The “big red button”’ is too late: an alternative model for the ethical evaluation
of AI systems. Ethics and Information Technology. 2018;20:59–69. https://doi.org/https://doi.org/
10.1007/s10676-018-9447-7.
[254] Group CPS, the Tech Fairness Coalition, the ACLU of Washington.: The Algorithmic Equity Toolkit
(AEKit). 2020. Available from: https://www.aclu-wa.org/AEKit.
[255] Chmielinski KS, Newman S, Taylor M, Joseph J, Thomas K, Yurkofsky J, et al. The Dataset Nutrition
Label (2nd Gen): Leveraging Context to Mitigate Harms in Artificial Intelligence. arXiv:220103954.
2022;https://doi.org/10.48550/arXiv.2201.03954. [cs.LG].
[256] org I.: The Field Guide to Human-Centered Design - Design Kit. 2015. Available from: https://www.
designkit.org/resources/1.html.
[257] Butterworth M. The ICO and artificial intelligence: The role of fairness in the GDPR framework.
Computer Law & Security Review. 2018;34(2):257–268.
https://doi.org/https://doi.org/10.1016/j.
clsr.2018.01.004.
[258] Vasudevan S, Kenthapadi K. LiFT: A Scalable Framework for Measuring Fairness in ML Applications.
In: 29th ACM International Conference on Information and Knowledge Management (CIKM); 2020.
Available from: https://github.com/linkedin/lift.
[259] Pineau J.: The Machine Learning Reproducibility Checklist. 2020. Available from: https://www.cs.
mcgill.ca/∼jpineau/ReproducibilityChecklist.pdf.
[260] Shen H, Wang L, Deng WH, Brusse C, Velgersdijk R, Zhu H. The Model Card Authoring Toolkit:
Toward Community-centered, Deliberation-driven AI Design.
In: ACM Conference on Fairness,
Accountability, and Transparency. FAccT ’22. New York, NY, USA: Association for Computing
Machinery; 2022. p. 440–451.
[261] Bates AG, ˇSpakulov´a I, Dove I, Mealor A, for National Statistics O.: ONS Methodology Work-
ing paper series number 16 - Synthetic Data Pilot.
2025.
Available from: https://www.
ons.gov.uk/methodology/methodologicalpublications/generalmethodology/onsworkingpaperseries/
onsmethodologyworkingpaperseriesnumber16syntheticdatapilot#toc.
[262] Citron DK, Pasquale F. The scored society: Due process for automated predictions. Washington Law
Review. 2014;89:1.
[263] Lakkaraju H, Kleinberg J, Leskovec J, Ludwig J, Mullainathan S. The Selective Labels Problem:
Evaluating Algorithmic Predictions in the Presence of Unobservables. In: 23rd ACM SIGKDD Inter-
national Conference on Knowledge Discovery and Data Mining. New York, NY, USA: Association for
Computing Machinery; 2017. p. 275–284.
[264] Tale TW.: Whole Tale Project. 2025. Available from: https://wholetale.org/.
44

--- Page 45 ---

[265] Simbeck K. They shall be fair, transparent, and robust: Auditing learning analytics systems. AI and
Ethics. 2024;4(2):555–571. https://doi.org/https://doi.org/10.1007/s43681-023-00292-7.
[266] Calders T, Verwer S.
Three naive bayes approaches for discrimination-free classification.
Data mining and knowledge discovery. 2010;21:277–292.
https://doi.org/https://doi.org/10.1007/
s10618-010-0190-x.
[267] Katell M, Young M, Dailey D, Herman B, Guetler V, Tam A, et al.
Toward situated interven-
tions for algorithmic equity: Lessons from the field. In: Conference on Fairness, Accountability, and
Transparency. FAT* ’20. New York, NY, USA: Association for Computing Machinery; 2020. p. 45–55.
[268] Alshammari M, Simpson A.
Towards a Principled Approach for Engineering Privacy by Design.
In: Schweighofer E, Leitold H, Mitrakas A, Rannenberg K, editors. Privacy Technologies and Policy.
Cham: Springer International Publishing; 2017. p. 161–177.
[269] Ancona M, Ceolini E, ¨Oztireli C, Gross M. Towards better understanding of gradient-based attribution
methods for Deep Neural Networks. In: International Conference on Learning Representations; 2018. .
[270] Security
UP.:
Uber
Differential
Privacy.
2017.
Available
from:
https://medium.com/
uber-security-privacy/differential-privacy-open-source-7892c82c42b6.
[271] Lane G, Angus A, Murdoch A.: UnBias Fairness Toolkit. Zenodo. 2018.
[272] Leslie D. Understanding Artificial Intelligence Ethics and Safety: A Guide for the Responsible Design
and Implementation of AI Systems in the Public Sector. Zenodo; 2019.
[273] Spiekermann S, Winkler T.
Value-based Engineering for Ethics by Design.
arXiv:200413676.
2020;https://doi.org/10.48550/arXiv.2004.13676. [cs.CY].
[274] Biases W.: The AI developer platform to build AI agents, applications, and models with confidence.
2025. Available from: https://wandb.ai/site.
[275] Data W.: A new method for ethical data science.
2025.
Available from: https://medium.com/
wellcome-data/a-new-method-for-ethical-data-science-edb59e400ae9.
[276] Russell C, Kusner MJ, Loftus J, Silva R. When Worlds Collide: Integrating Different Counterfactual
Assumptions in Fairness. In: Guyon I, Luxburg UV, Bengio S, Wallach H, Fergus R, Vishwanathan S,
et al., editors. Advances in Neural Information Processing Systems. vol. 30. Curran Associates, Inc.;
2017. .
[277] Hasselbalch G, Olsen BK, Tranberg P.: White Paper on Data Ethics in Public Procurement of AI
based Services and Solutions. DataEthics, Dinamarca. 2020. Available from: https://dataethics.eu/
wp-content/uploads/dataethics-whitepaper-april-2020.pdf.
[278] Graves M, Ratti E.: A Capability Approach to Ethical Development and Internal Auditing of Ai
Technology [SSRN Scholarly Paper]. Rochester, NY: Social Science Research Network. 2024.
[279] Zlateva P, Steshina L, Petukhov I, Velev D. A Conceptual Framework for Solving Ethical Issues in
Generative Artificial Intelligence. Frontiers in Artificial Intelligence and Applications. 2024;381:110–
119. ISBN: 9781643684802. https://doi.org/10.3233/FAIA231182.
[280] van Kolfschooten H.: A Human Rights-Based Approach to Artificial Intelligence in Healthcare: A
Proposal for a Patients’ Rights Impact Assessment Tool [SSRN Scholarly Paper]. Rochester, NY:
Social Science Research Network. 2024.
[281] El-Haber N, Burnett D, Halford A, Stamp K, De Silva D, Manic M, et al. A Lifecycle Approach for
Artificial Intelligence Ethics in Energy Systems. Energies. 2024 Jul;17(14). https://doi.org/10.3390/
en17143572.
45

--- Page 46 ---

[282] Wang J, Pashmforoosh R.
A new framework for ethical artificial intelligence: keeping HRD in
the loop. Human Resource Development International. 2024;1:1–24. Publisher: Routledge eprint:
https://doi.org/10.1080/13678868.2024.2346492.
[283] Yurt E, Kasarci I. A Questionnaire of Artificial Intelligence Use Motives: A contribution to investi-
gating the connection between AI and motivation. International Journal of Technology in Education.
2024;7(2).
[284] Cappelli MA, Di Marzo Serugendo G.
A semi-automated software model to support AI ethics
compliance assessment of an AI system guided by ethical principles of AI.
AI and Ethics. 2024
May;https://doi.org/10.1007/s43681-024-00480-z.
[285] Hosobe H, Satoh K. A Soft Constraint-Based Framework for Ethical Reasoning. In: International
Conference on Agents and Artificial Intelligence; 2024. p. 1354–1361.
[286] Eindhoven University of Technology, the Netherlands, Faber I. A tangible toolkit to uncover clinician’s
ethical values about AI clinical decision support systems. In: DRS Conference Proceedings; 2024. .
[287] Ferrell OC, Harrison DE, Ferrell LK, Ajjan H, Hochstein BW. A theoretical framework to guide AI
ethical decision making. AMS Review. 2024 Apr;https://doi.org/10.1007/s13162-024-00275-9.
[288] McFadden Z. ACESOR: a critical engagement in systems of oppression AI assessment tool. AI and
Ethics. 2024 Apr;https://doi.org/10.1007/s43681-024-00478-7.
[289] Bogucka E, Constantinides M, ˇS´cepanovi´c S, Quercia D.
AI Design: A Responsible Artificial
Intelligence Framework for Prefilling Impact Assessment Reports.
IEEE Internet Computing.
2024;28(5):37–45. https://doi.org/10.1109/MIC.2024.3451351.
[290] Kon´e LA, Leonteva AO, Diallo MT, Haouba A, COLLET P. AI Ethical Framework: A Government-
Centric Tool Using Generative AI.
International Journal of Advanced Computer Science &
Applications. 2024;15(11).
[291] Radanliev P. AI Ethics: Integrating Transparency, Fairness, and Privacy in AI Development. Applied
Artificial Intelligence. 2025 Dec;39(1):2463722. https://doi.org/10.1080/08839514.2025.2463722.
[292] Han TA, Pandit D, Joneidy S, Hasan MM, Hossain J, Hoque Tania M, et al. An Explainable AI
Tool for Operational Risks Evaluation of AI Systems for SMEs. In: 15th International Conference on
Software, Knowledge, Information Management and Applications (SKIMA); 2023. p. 69–74. ISSN:
2573-3214.
[293] Iturbe E, Rios E, Rego A, Toledo N. Artificial Intelligence for next generation cybersecurity: The
AI4CYBER framework. In: 18th International Conference on Availability, Reliability and Security.
ARES ’23. New York, NY, USA: Association for Computing Machinery; 2023. .
[294] Ghosh A, Saini A, Barad H. Artificial intelligence in governance: Recent trends, risks, challenges,
innovative frameworks and future directions. AI & SOCIETY. 2025 Mar;https://doi.org/10.1007/
s00146-025-02312-y.
[295] Sallam M, Snygg J, Sallam M.
Assessment of Artificial Intelligence Credibility in Evidence-
Based Healthcare Management with “AERUS” Innovative Tool.
Journal of Artificial Intelligence,
Machine Learning and Data Science. 2024 Feb;2(1):9–18.
https://doi.org/10.51219/JAIMLD/
mohammed-sallam/20.
[296] G¨ollner S, Tropmann-Frick M. Bridging the Gap between Theory and Practice: Towards Responsible
AI Evaluation. In: CHAI@ KI; 2023. p. 68–76.
[297] Rossi de Borba JG, Dias Canedo E, Filho GPR.: Bridging Theory and Practice: A Tool for Translating
Ethical Ai Requirements into Ethical User Stories [SSRN Scholarly Paper]. Rochester, NY: Social
Science Research Network. 2024.
46

--- Page 47 ---

[298] Wang Z, Hao S, Carpendale S. Card-Based Approach to Engage Exploring Ethics in AI for Data Visu-
alization. In: Extended Abstracts of the CHI Conference on Human Factors in Computing Systems.
Honolulu HI USA: ACM; 2024. p. 1–7.
[299] Tejani AS, Klontzas ME, Gatti AA, Mongan JT, Moy L, Park SH, et al.
Checklist for Artifi-
cial Intelligence in Medical Imaging (CLAIM): 2024 Update. Radiology: Artificial Intelligence. 2024
Jul;6(4):e240300. https://doi.org/10.1148/ryai.240300.
[300] Bhat M. Creative Explainable AI Tools to Understand Algorithmic Decision-Making. In: 16th Con-
ference on Creativity & Cognition. C&amp;C ’24. New York, NY, USA: Association for Computing
Machinery; 2024. p. 10–16.
[301] Corrˆea NK, Santos JW, Galv˜ao C, Pasetti M, Schiavon D, Naqvi F, et al.
Crossing the princi-
ple–practice gap in AI ethics with ethical problem-solving. AI and Ethics. 2024 Apr;https://doi.org/
10.1007/s43681-024-00469-8.
[302] Hanschke VA, Rees D, Alanyali M, Hopkinson D, Marshall P. Data Ethics Emergency Drill: A Toolbox
for Discussing Responsible AI for Industry Teams. In: CHI Conference on Human Factors in Computing
Systems. CHI ’24. New York, NY, USA: Association for Computing Machinery; 2024. .
[303] Badawy W.
Data-driven framework for evaluating digitization and artificial intelligence risk: A
comprehensive analysis. AI and Ethics. 2023 Nov;https://doi.org/10.1007/s43681-023-00376-4.
[304] Stewart M, Warden P, Omri Y, Prakash S, Santos J, Hymel S, et al. Datasheets for Machine Learning
Sensors. arXiv:230608848 [cs]. 2023 Sep;.
[305] Waters G, Mapp W, Honenberger P. Decisional value scores: A new family of metrics for ethical
AI-ML. AI and Ethics. 2024 Jul;https://doi.org/10.1007/s43681-024-00504-8.
[306] Zhou J, Chen F. E-LENS: User Requirements-Oriented AI Ethics Assurance. arXiv:250304747 [cs].
2025 Feb;https://doi.org/10.48550/arXiv.2503.04747.
[307] Sieberichs C, Geerkens S, Braun A, Waschulzik T. ECS: an interactive tool for data quality assurance.
AI and Ethics. 2024 Feb;4(1):131–139. https://doi.org/10.1007/s43681-023-00393-3.
[308] Allen LK, Kendeou P. ED-AI Lit: An Interdisciplinary Framework for AI Literacy in Education. Policy
Insights from the Behavioral and Brain Sciences. 2023 Dec;p. 23727322231220339. Publisher: SAGE
Publications. https://doi.org/10.1177/23727322231220339.
[309] Afroogh S, Mostafavi A, Akbari A, Pouresmaeil Y, Goudarzi S, Hajhosseini F, et al.
Embedded
Ethics for Responsible Artificial Intelligence Systems (EE-RAIS) in disaster management: a concep-
tual model and its deployment. AI and Ethics. 2024 Nov;4(4):1117–1141. https://doi.org/10.1007/
s43681-023-00309-1.
[310] Casaburo D, Marsh I. Ensuring fundamental rights compliance and trustworthiness of law enforcement
AI systems: the ALIGNER Fundamental Rights Impact Assessment. AI and Ethics. 2024 Sep;https:
//doi.org/10.1007/s43681-024-00560-0.
[311] Tripathi A, Kumar V. Ethical practices of artificial intelligence: A management framework for responsi-
ble AI deployment in businesses. AI and Ethics. 2025 Feb;https://doi.org/10.1007/s43681-025-00670-3.
[312] van Hilten M, Ryan M, Blok V, de Roo N. Ethical, Legal and Social Aspects (ELSA) for AI: an
assessment tool for Agri-food. Smart Agricultural Technology. 2024 Dec;p. 100710. https://doi.org/
10.1016/j.atech.2024.100710.
[313] Brey P, Dainow B. Ethics by design for artifcial intelligence. AI and Ethics. 2023 Sep;https://doi.
org/10.1007/s43681-023-00330-4.
47

--- Page 48 ---

[314] Dagan N, Devons-Sberro S, Paz Z, Zoller L, Sommer A, Shaham G, et al. Evaluation of AI Solutions in
Health Care Organizations — The OPTICA Tool. NEJM AI. 2024 Aug;1(9):AIcs2300269. Publisher:
Massachusetts Medical Society. https://doi.org/10.1056/AIcs2300269.
[315] Dotan R, Blili-Hamelin B, Madhavan R, Matthews J, Scarpino J. Evolving AI Risk Management: A
Maturity Model based on the NIST AI Risk Management Framework. arXiv:240115229 [cs]. 2024 Jan;.
[316] O’Neil C, Sargeant H, Appel J.
Explainable Fairness in Regulatory Algorithmic Auditing.
West
Virginia Law Review. 2024;127:79.
[317] Raza S, Ghuge S, Ding C, Dolatabadi E, Pandya D. FAIR Enough: Develop and Assess a FAIR-
Compliant Dataset for Large Language Model Training? Data Intelligence. 2024 May;6(2):559–585.
https://doi.org/10.1162/dint a 00255.
[318] Sallami D, A¨ımeur E. Fairframe: A fairness framework for bias detection and mitigation in news. AI
and Ethics. 2024 Sep;https://doi.org/10.1007/s43681-024-00568-6.
[319] Moreira DAB, Ferreira AI, Silva J, dos Santos GO, Pereira L, Gondim JM, et al. FairPIVARA: Reduc-
ing and Assessing Biases in CLIP-Based Multimodal Models. In: British Machine Vision Conference;
2024. .
[320] Hoche M, Mineeva O, Burger M, Blasimme A, R¨atsch G.: FAMEWS: a Fairness Auditing tool for
Medical Early-Warning Systems. medRxiv. 2024. Pages: 2024.02.08.24302458.
[321] Rosado Gomez AA, Calder´on Benavides ML. Framework for Bias Detection in Machine Learning
Models: A Fairness Approach.
In: 17th ACM International Conference on Web Search and Data
Mining. WSDM ’24. New York, NY, USA: Association for Computing Machinery; 2024. p. 1152–1154.
[322] Ning Y, Teixayavong S, Shang Y, Savulescu J, Nagaraj V, Miao D, et al. Generative artificial intel-
ligence and ethical considerations in health care: a scoping review and ethics checklist. The Lancet
Digital Health. 2024;6(11):e848–e856. https://doi.org/10.1016/S2589-7500(24)00143-2.
[323] Lachenmaier J, Werling M, Morar D. Governance of Artificial Intelligence - A Framework Towards
Ethical AI Applications. Ethics and Information Technology. 2023 Oct;.
[324] Schuett J, Reuel AK, Carlier A. How to design an AI ethics board. AI and Ethics. 2024 Feb;https:
//doi.org/10.1007/s43681-023-00409-y.
[325] Adams J. Introducing the ethical-epistemic matrix: A principle-based tool for evaluating artificial
intelligence in medicine. AI and Ethics. 2024 Oct;https://doi.org/10.1007/s43681-024-00597-1.
[326] Morand C, Ligozat AL, N´ev´eol A. MLCA: A Tool for Machine Learning Life Cycle Assessment. In:
10th International Conference on ICT for Sustainability (ICT4S); 2024. p. 227–238.
[327] Jethwani H, Lewis ACF. Multi-Value Alignment for Ml/Ai Development ChoicesA Four-step Pro-
cess Including Approaches to Trade-offs. American Philosophical Quarterly. 2025 Apr;62(2):133–152.
Publisher: Duke University Press. https://doi.org/10.5406/21521123.62.2.03.
[328] Baldassarre MT, Gigante D, Kalinowski M, Ragone A.
POLARIS: A framework to guide the
development of Trustworthy AI systems.
In: IEEE/ACM 3rd International Conference on AI
Engineering-Software Engineering for AI; 2024. p. 200–210.
[329] Mart´ın-Moncunill D, Garc´ıa Laredo E, Carlos Nieves J. POTDAI: A Tool to Evaluate the Perceived
Operational Trust Degree in Artificial Intelligence Systems. IEEE Access. 2024;12:133097–133109.
Conference Name: IEEE Access. https://doi.org/10.1109/ACCESS.2024.3454061.
[330] Lee SU, Perera H, Liu Y, Xia B, Lu Q, Zhu L. Responsible AI Question Bank: A Comprehensive Tool
for AI Risk Assessment. CoRR. 2024;.
48

--- Page 49 ---

[331] Maathuis C, Chockalingam S. Risk Assessment of Large Language Models Beyond Apocalyptic Visions.
European Conference on Cyber Warfare and Security. 2024 Jun;23(1):279–286. Number: 1. https:
//doi.org/10.34190/eccws.23.1.2293.
[332] Li C, Liu C, Wu W. RuleGLM: An Ethics Evaluation Framework with Knowledge Vector Space. In:
Huang DS, Si Z, Zhang Q, editors. ADVANCED INTELLIGENT COMPUTING TECHNOLOGY
AND APPLICATIONS, PT III, ICIC 2024. vol. 14877. Singapore: Springer-Verlag Singapore Pte Ltd;
2024. p. 463–474. ISSN: 2945-9133, 1611-3349 Num Pages: 12 Series Title: Lecture Notes in Artificial
Intelligence Web of Science ID: WOS:001307345000038.
[333] Hsu CY, Tsai YL, Lin CH, Chen PY, Yu CM, Huang CY. Safe LoRA: The Silver Lining of Reducing
Safety Risks when Finetuning Large Language Models. Advances in Neural Information Processing
Systems. 2024 Dec;37:65072–65094.
[334] Banerjee S, Layek S, Tripathy S, Kumar S, Mukherjee A, Hazra R. Safeinfer: Context adaptive decod-
ing time safety alignment for large language models. In: AAAI Conference on Artificial Intelligence.
vol. 39; 2025. p. 27188–27196.
[335] Kodakandla N.
Scaling AI responsibly: Leveraging MLOps for sustainable machine learning
deployments. International Journal of Science and Research Archive. 2024;13(1):3447–3455.
[336] Xie T, Qi X, Zeng Y, Huang Y, Sehwag UM, Huang K, et al. SORRY-Bench: Systematically Evaluating
Large Language Model Safety Refusal.
In: The Thirteenth International Conference on Learning
Representations; 2025. .
[337] Wang Y, Lu E, Ruan Z, Liang Y, Zeng Y.
Stream: social data and knowledge collective intelli-
gence platform for TRaining Ethical AI Models. AI & SOCIETY. 2024 Jan;https://doi.org/10.1007/
s00146-023-01851-6.
[338] Bauroth M, Rath-Manakidis P, Langholf V, Wiskott L, Glasmachers T. tachAId—An interactive tool
supporting the design of human-centered AI solutions. Frontiers in Artificial Intelligence. 2024 Mar;7.
Publisher: Frontiers. https://doi.org/10.3389/frai.2024.1354114.
[339] Vyhmeister E, Castane GG. TAI-PRM: trustworthy AI—project risk management framework towards
Industry 5.0. AI and Ethics. 2024 Feb;https://doi.org/10.1007/s43681-023-00417-y.
[340] Perkins M, Furze L, Roe J, Macvaugh J.
The Artificial Intelligence Assessment Scale (AIAS): A
Framework for Ethical Integration of Generative AI in Educational Assessment. Journal of University
Teaching and Learning Practice. 2024;21(6). https://doi.org/10.53761/q3azde36.
[341] Habli I, Hawkins R, Paterson C, Ryan P, Jia Y, Sujan M, et al. The BIG Argument for AI Safety
Cases. arXiv:250311705 [cs]. 2025 Mar;https://doi.org/10.48550/arXiv.2503.11705.
[342] Nemat AT, Becker SJ, Lucas S, Thomas S, Gadea I, Charton JE. The Principle-at-Risk Analysis
(PaRA): Operationalising Digital Ethics by Bridging Principles and Operations of a Digital Ethics
Advisory Panel. Minds and Machines. 2023 Dec;https://doi.org/10.1007/s11023-023-09654-w.
[343] Getir Yaman S, Ribeiro P, Burholt C, Jones M, Cavalcanti A, Calinescu R. Toolkit for specification, val-
idation and verification of social, legal, ethical, empathetic and cultural requirements for autonomous
agents. Science of Computer Programming. 2024;236. https://doi.org/10.1016/j.scico.2024.103118.
[344] Trotsyuk AA, Waeiss Q, Bhatia RT, Aponte BJ, Heffernan IML, Madgavkar D, et al.
Toward a
framework for risk mitigation of potential misuse of artificial intelligence in biomedical research. Nature
Machine Intelligence. 2024 Nov;p. 1–8. Publisher: Nature Publishing Group. https://doi.org/10.1038/
s42256-024-00926-3.
[345] Vetter MA, Lucia B, Jiang J, Othman M. Towards a framework for local interrogation of AI ethics:
A case study on text generators, academic integrity, and composing with ChatGPT. Computers and
Composition. 2024 Mar;71:102831. https://doi.org/10.1016/j.compcom.2024.102831.
49

--- Page 50 ---

[346] Kioskli K, Bishop L, Polemi N, Ramfos A.
Towards a Human-Centric AI Trustworthiness Risk
Management Framework. Human Factors in Cybersecurity. 2024;127(127).
[347] Xia B, Lu Q, Zhu L, Lee SU, Liu Y, Xing Z. Towards a Responsible AI Metrics Catalogue: A Collection
of Metrics for AI Accountability. In: IEEE/ACM 3rd International Conference on AI Engineering -
Software Engineering for AI. Lisbon Portugal: ACM; 2024. p. 100–111.
[348] Berardinis Jd, Porcaro L, Mero˜no-Pe˜nuela A, Cangelosi A, Buckley T.
Towards Responsible AI
Music: an Investigation of Trustworthy Features for Creative Systems. arXiv:250318814 [cs]. 2025
Mar;https://doi.org/10.48550/arXiv.2503.18814.
[349] Collins GS, Moons KGM, Dhiman P, Riley RD, Beam AL, Calster BV, et al. TRIPOD+AI statement:
updated guidance for reporting clinical prediction models that use regression or machine learning
methods. BMJ. 2024 Apr;385:e078378. Publisher: British Medical Journal Publishing Group Section:
Research Methods &amp; Reporting. https://doi.org/10.1136/bmj-2023-078378.
[350] Sharma S. Trustworthy Artificial Intelligence: Design of AI Governance Framework. Strategic Analysis.
2023;0(0):1–22. Publisher: Routledge eprint: https://doi.org/10.1080/09700161.2023.2288994. https:
//doi.org/10.1080/09700161.2023.2288994.
[351] Teo W, Teoh Z, Arabi DA, Aboushadi M, Lai K, Ng Z, et al. What Would You do? An Ethical AI
Quiz. In: IEEE/ACM 45th International Conference on Software Engineering: Companion Proceedings
(ICSE-Companion); 2023. p. 112–116. ISSN: 2574-1934.
[352] Z¨oller MA, Titov W, Schlegel T, Huber MF. XAutoML: A Visual Analytics Tool for Understanding
and Validating Automated Machine Learning. ACM Transactions on Interactive Intelligent Systems.
2023 Dec;13(4):28:1–28:39. https://doi.org/10.1145/3625240.
50

--- Page 51 ---

Appendix A
AIETs list – until July 2023
1. A confidence-based approach for balancing fairness and accuracy [107]
2. A generic framework for privacy preserving deep learning [108]
3. A Matrix for Selecting Responsible AI Frameworks [109]
4. A Playbook for Ethical Technology Governance [110]
5. A responsible AI framework: pipeline contextualisation [111]
6. A Right to Reasonable Inferences: Re-Thinking Data Protection Law in the Age of Big Data and AI [112]
7. A seven-layer model with checklists for standardising fairness assessment throughout the AI lifecycle [40]
8. A survey of methods for explaining black box models [113]
9. A Survey of Value Sensitive Design Methods [114]
10. A systematic methodology for privacy impact assessments: a design science based approach [115]
11. A toolkit of dilemmas: Beyond debiasing and fairness formulas for responsible AI/ML [116]
12. A Toolkit to Enable the Design of Trustworthy AI [117]
13. A3i the Trust in AI Framework [118]
14. Adversarial Robustness - Theory and Practice [119]
15. Accenture Fairness Evaluation Tool [120]
16. Accountable Algorithms [121]
17. Advbox: a toolbox to generate adversarial examples that fool neural networks [65]
18. Adversarial Robustness Toolbox v1.0.0 [45]
19. Aequitas: A Bias and Fairness Audit Toolkit [29]
20. Agile Ethics for AI (HAI) [122]
21. AI Audit: A Card Game to Reflect on Everyday AI Systems [50]
22. AI and Big Data: A blueprint for a human rights, social and ethical impact assessment [123]
23. AI Blindspot: A discovery process for spotting unconscious biases and structural inequalities in AI systems [124]
24. AI Commons [125]
25. AI Digital Tool Product Lifecycle Governance Framework through Ethics and Compliance by Design [126]
26. AI Explainability 360 Toolkit [30]
27. AI Fairness 360 toolkit [127]
28. AI Incident Database [128]
29. AI Privacy Toolkit [67]
30. AI Procurement in a Box [70]
31. AI Usage Cards: Responsibly Reporting AI-Generated Content [129]
32. AI-RFX Procurement Framework [32]
33. Algorithm tips resources and leads for investigating algorithms in society [130]
34. Algorithmic Accountability and Public Reason [131]
35. Algorithmic Accountability Policy Toolkit [132]
36. Algorithmic Accountability: Journalistic investigation of computation power structures [133]
37. Algorithmic Impact Assessment (AIA) [134]
38. Algorithmic Impact Assessments: A Practical Framework for Public Agency Accountability [63]
39. Algorithmic Transparency via Quantitative Input Influence: Theory and Experiments with Learning Systems [135]
40. Alibi Explain: Algorithms for Explaining Machine Learning Models [136]
41. Amazon SageMaker Clarify: Machine Learning Bias Detection and Explainability in the Cloud [137]
42. An Ethical Framework for Evaluating Experimental Technology [138]
43. An Ethical Toolkit for Engineering/Design Practice [139]
44. Assessing Radiology Research on Artificial Intelligence: A Brief Guide for Authors, Reviewers, and Readers—From the Radiology
Editorial Board [140]
45. Assessment List for Trustworthy Artificial Intelligence (ALTAI) for self-assessment [13]
46. Audit-AI [141]
47. Auditing Algorithms @ Northeastern [142]
48. Auditing Algorithms: Research Methods for Detecting Discrimination on Internet Platforms [143]
49. Auditing large language models: a three-layered approach [38]
50. Augmented Datasheets for Speech Datasets and Ethical Decision-Making [144]
51. Beyond Accuracy: Behavioral Testing of NLP models with CheckList [145]
52. BOLD: Dataset and Metrics for Measuring Biases in Open-Ended Language Generation[36]
53. Building Data AI Ethics Committees [146]
54. Captum [147]
55. Cards for Humanity [148]
56. Certifying and Removing Disparate Impact [149]
51

--- Page 52 ---

57. Charting the Sociotechnical Gap in Explainable AI: A Framework to Address the Gap in XAI [150]
58. CleverHans [151]
59. Closing the AI Accountability Gap: Defining an End-toEnd Framework for Internal Algorithmic Auditing [39]
60. Co-Designing Checklists to Understand Organizational Challenges and Opportunities around Fairness in AI [152]
61. Community Jury [43]
62. Consequence Scanning [46]
63. Contrastive Explanation Method [64]
64. Corporate Digital Responsibility [24]
65. Counterfactual Explanations without Opening the Black Box: Automated Decisions and the GDPR [153]
66. Counterfactual Fairness [154]
67. Cyber Resilience Review (CRR) [155]
68. Data Cards: Purposeful and Transparent Dataset Documentation for Responsible AI [156]
69. Data Ethics Canvas: user guide [157]
70. Data Ethics Framework [158]
71. Data Management and Use: Governance in the 21st Century [159]
72. Data Minimisation: A Language-Based Approach [160]
73. Data Statements for Natural Language Processing: Toward Mitigating System Bias and Enabling Better Science [27]
74. Data Statements: From Technical Concept to Community Practice [161]
75. Datasheets for Datasets [26]
76. DEDA: De Ethische Data Assistent [162]
77. Deep Inside Convolutional Networks: Visualising Image Classification Models and Saliency Maps [163]
78. Deep Learning for Case-Based Reasoning Through Prototypes: A Neural Network That Explains Its Predictions [164]
79. DeepExplain [165]
80. DeepLIFT [166]
81. DEON - An ethics checklist for data scientists [167]
82. Design Ethically Toolkit [168]
83. Designing for Motivation, Engagement and Wellbeing in Digital Experience [169]
84. Development of privacy design patterns based on privacy principles and UML [170]
85. DIANES: A DEI Audit Toolkit for News Sources [171]
86. DiCE: Diverse Counterfactual Explanations for ML [172]
87. Digital Impact Toolkit [173]
88. ELI5 [174]
89. Ellpha [175]
90. Empowering AI Leadership [176]
91. Empowering AI Leadership: AI C-Suite Toolkit [177]
92. Enigma: Decentralized Computation Platform with Guaranteed Privacy [178]
93. Equity Evaluation Corpus (EEC) [47]
94. Ethical framework for Artificial Intelligence and Digital technologies [179]
95. Ethical Requirements Stack: A framework for implementing ethical requirements of AI in software engineering practices [180]
96. Ethically Aligned Design IEEE [181]
97. Ethics & Algorithms Toolkit [182]
98. Ethics and Privacy in AI and Big Data: Implementing Responsible Research and Innovation [183]
99. Ethics Cards [184]
100. Ethics for designers – the toolkit [25]
101. Ethics Kit [185]
102. EthicsNet [186]
103. Explainability fact sheets: a framework for systematic assessment of explainable approaches [187]
104. Explainable AI: Driving business value through greater understanding [188]
105. Explanations based on the Missing: Towards Contrastive Explanations with Pertinent Negatives [64]
106. FactSheets: Increasing trust in AI services through supplier’s declarations of conformity [15]
107. Fair, Transparent, and Accountable Algorithmic Decision-making Processes [189]
108. Fairlearn: A toolkit for assessing and improving fairness in AI [190]
109. Fairness Constraints: Mechanisms for Fair Classification [191]
110. Fairness in Classification [192]
111. Fairness in Design: A Framework for Facilitating Ethical Artificial Intelligence Designs [66]
112. Fairness Score and process standardization: framework for fairness certification in artificial intelligence systems [193]
113. Foolbox: A Python toolbox to benchmark the robustness of machine learning models [194]
114. Foresight into AI Ethics (FAIE) [195]
52

--- Page 53 ---

115. Framework for Evaluating Ethics in AI [196]
116. Futures Wheel [197]
117. Generative adversarial networks (GANs) for synthetic dataset generation with binary classes [198]
118. Glass-Box: Explaining AI Decisions With Counterfactual Statements Through Conversation With a Voice-enabled Virtual
Assistant [199]
119. Guide to the UK General Data Protection Regulation (UK GDPR) [200]
120. H20.ai Machine Learning Interpretability Resources [201]
121. Harms Modeling [14]
122. HAX Workbook [202]
123. Hazy [203]
124. How to stimulate effective public engagement on the ethics of artificial intelligence [204]
125. Human Decisions and Machine Predictions [205]
126. IBM Watson OpenScale [206]
127. ICO Anonymisation: managing data protection risk. Code of Practice [207]
128. ICO Guide to the General Data Protection Regulation [208]
129. IDEO’s AI Ethics Cards [23]
130. IEEE Draft Model Process for Addressing Ethical Concerns During System Design P7000/D3 [209]
131. IEEE Recommended Practice for Assessing the Impact of Autonomous and Intelligent Systems on Human WellBeing Std
7010 [210]
132. IEEE Ethics Certification Program for Autonomous and Intelligent Systems (ECPAIS) [211]
133. Improving Social Responsibility of Artificial Intelligence by Using ISO 26000 [212]
134. Interactive Model Cards: A Human-Centered Approach to Model Documentation [213]
135. InterpretML: A Unified Framework for Machine Learning Interpretability [214]
136. Judgment Call the Game: Using Value Sensitive Design and Design Fiction to Surface Ethical Concerns Related to Technology [42]
137. Learning Adversarially Fair and Transferable Representations [215]
138. Learning Important Features Through Propagating Activation Differences [216]
139. Learning Representation for Counterfactual Inference [217]
140. LIME – “Why Should I Trust You?”: Explaining the Predictions of Any Classifier [34]
141. Man is to Computer Programmer as Woman is to Homemaker? Debiasing Word Embeddings [218]
142. Metrics for explainable AI: Challenges and prospects [219]
143. Microsoft’s framework for building AI systems responsibly [220]
144. Model Cards for Model Reporting [12]
145. Model Ethical Data Impact Assessment [221]
146. Model-Agnostic Private Learning via Stability [222]
147. Moral Machine [223]
148. Navigating Data-Centric Artificial Intelligence With DC-Check: Advances, Challenges, and Opportunities [224]
149. Neural Network Exchange Format (NNEF) [225]
150. New Economy Impact Model [226]
151. OECD Framework for the Classification of AI systems [69]
152. On Pixel-Wise Explanations for Non-Linear Classifier Decisions by layer-wise relevance propagation [227]
153. ONNX Open Neural Network Exchange [228]
154. OpenMined [229]
155. OpenML [230]
156. Peeking Inside the Black Box: Visualizing Statistical Learning With Plots of Individual Conditional Expectation [231]
157. People + AI Research Guidebook [232]
158. Personal AI Privacy Watchdog Could Help You Regain Control of Your Data [233]
159. PMML: An Open Standard for Sharing Models [234]
160. Practical verification of decision-making in agent-based autonomous systems [235]
161. Principles for Accountable Algorithms and a Social Impact Statement for Algorithms [236]
162. Privacy by Design: essential for organizational accountability and strong business practices [237]
163. Privacy Principles: Towards a common privacy audit methodology [238]
164. PROBAST: A Tool to Assess the Risk of Bias and Applicability of Prediction Model Studies [41]
165. PROV-ML – Provenance Data in the Machine Learning Lifecycle in Computational Science and Engineering [239]
166. Questioning the assumptions behind fairness solutions [240]
167. Responsible AI Licenses (RAIL) [241]
168. Responsible AI Toolbox [242]
169. Responsible AI Toolkit [243]
170. Responsible and Inclusive Technology Framework: A Formative Framework to Promote Societal Considerations in Information
Technology Contexts [244]
53

--- Page 54 ---

171. Responsible natural language processing: A principlist framework for social benefits [245]
172. Risks, Harms and Benefits Assessment Tool [246]
173. SAFETYKIT: First Aid for Measuring Safety in Open-domain Conversational Systems [247]
174. Scalable Private Learning with PATE [248]
175. SHAP - A Unified Approach to Interpreting Model Predictions [35]
176. Should I disclose my dataset? Caveats between reproducibility and individual data rights [48]
177. System Cards, a new resource for understanding how AI systems work [249]
178. Ten simple rules for responsible big data research [250]
179. Tensorflow’s Fairness Evaluation and Visualization Toolkit [251]
180. TensorFlow Privacy [44]
181. Text Characterization Toolkit (TCT) [252]
182. The “big red button” is too late: an alternative model for the ethical evaluation of AI systems [253]
183. The Algorithmic Equity Toolkit (AEKit) [254]
184. The Dataset Nutrition Label: A Framework To Drive Higher Data Quality Standards [28]
185. The Dataset Nutrition Label (2nd Gen): Leveraging Context to Mitigate Harms in Artificial Intelligence [255]
186. The Field Guide to Human-Centred Design [256]
187. The ICO and artificial intelligence: the role of fairness in the GDPR framework [257]
188. The LinkedIn Fairness Toolkit (LiFT) [258]
189. The Machine Learning Reproducibility Checklist [259]
190. The Model Card Authoring Toolkit: Toward Community-centered, Deliberation-driven AI Design [260]
191. The ONS Methodology working paper on synthetic data [261]
192. The Scored Society: Due process for automated predictions [262]
193. The Selective Labels Problem: Evaluating Algorithmic Predictions in the Presence of Unobservables [263]
194. The Turing Way [62]
195. The Whole Tale [264]
196. They shall be fair, transparent, and robust: auditing learning analytics systems [265]
197. Three na¨ıve Bayes approaches for discrimination-free classification [266]
198. Toward situated interventions for algorithmic equity: lessons from the field [267]
199. Towards a Principled Approach for Engineering Privacy by Design [268]
200. Towards better understanding of gradient-based attribution methods for Deep Neural Networks [269]
201. TuringBox: An Experimental Platform for the Evaluation of AI Systems [49]
202. Uber Differential Privacy [270]
203. UnBias Fairness Toolkit [271]
204. Understanding artificial intelligence ethics and safety: A guide for the responsible design and implementation of AI systems in
the public sector [272]
205. Value-based Engineering for Ethics by Design [273]
206. Weights & Biases [274]
207. Wellcome Data – A new method for ethical data science [275]
208. What-If Tool [31]
209. When Worlds Collide: Integrating Different Counterfactual Assumptions in Fairness [276]
210. White Paper on Data Ethics in Public Procurement of AI-based Services and Solutions [277]
211. “Why Should I Trust You?”: Explaining the Predictions of Any Classifier [34]
212. XAI - An eXplainability toolbox for machine learning [37]
213. Zeno: An Interactive Framework for Behavioral Evaluation of Machine Learning [33]
Appendix B
AIETs list update – from August 2023 until March
2025
214. A Capability Approach to Ethical Development and Internal Auditing of AI Technology [278]
215. A Conceptual Framework for Solving Ethical Issues in Generative Artificial Intelligence [279]
216. A Human Rights-Based Approach to Artificial Intelligence in Healthcare: A Proposal for a Patients’ Rights Impact Assessment
Tool [280]
217. A Lifecycle Approach for Artificial Intelligence Ethics in Energy Systems [281]
218. A new framework for ethical artificial intelligence: keeping HRD in the loop [282]
219. A Questionnaire of Artificial Intelligence Use Motives: A Contribution to Investigating the Connection between AI and
Motivation [283]
220. A semi-automated software model to support AI ethics compliance assessment of an AI system guided by ethical principles of
AI [284]
221. A Soft Constraint-Based Framework for Ethical Reasoning [285]
54

--- Page 55 ---

222. A tangible toolkit to uncover clinician’s ethical values about AI clinical decision support systems [286]
223. A theoretical framework to guide AI ethical decision making [287]
224. ACESOR: a critical engagement in systems of oppression AI assessment tool [288]
225. AI Design: A Responsible AI Framework for Impact Assessment Reports [289]
226. AI Ethical Framework: A Government-Centric Tool Using Generative AI [290]
227. AI Ethics: Integrating Transparency Fairness and Privacy in AI Development [291]
228. An Explainable AI Tool for Operational Risks Evaluation of AI Systems for SMEs [292]
229. Artificial Intelligence for next generation cybersecurity: The AI4CYBER framework [293]
230. Artificial intelligence in governance: recent trends, risks, challenges, innovative frameworks and future directions [294]
231. Assessment of Artificial Intelligence Credibility in Evidence-Based Healthcare Management with “AERUS” Innovative Tool [295]
232. Bridging the Gap between Theory and Practice: Towards Responsible AI Evaluation [296]
233. Bridging Theory and Practice: A Tool for Translating Ethical AI Requirements into Ethical User Stories [297]
234. Card-Based Approach to Engage Exploring Ethics in AI for Data Visualization [298]
235. Checklist for Artificial Intelligence in Medical Imaging (CLAIM) [299]
236. Creative Explainable AI Tools to Understand Algorithmic Decision-Making [300]
237. Crossing the principle–practice gap in AI ethics with ethical problem-solving [301]
238. Data Ethics Emergency Drill: A Toolbox for Discussing Responsible AI for Industry Teams [302]
239. Data-driven framework for evaluating digitization and artificial intelligence risk: a comprehensive analysis [303]
240. Datasheets for Machine Learning Sensors [304]
241. Decisional value scores: A new family of metrics for ethical AI-ML [305]
242. E-LENS: User Requirements-Oriented AI Ethics Assurance [306]
243. ECS: an interactive tool for data quality assurance [307]
244. ED-AI Lit: An Interdisciplinary Framework for AI Literacy in Education [308]
245. Embedded Ethics for Responsible Artificial Intelligence Systems (EE-RAIS) in disaster management: a conceptual model and its
deployment [309]
246. Ensuring fundamental rights compliance and trustworthiness of law enforcement AI systems: the ALIGNER Fundamental Rights
Impact Assessment [310]
247. Ethical practices of artificial intelligence: a management framework for responsible AI deployment in businesses [311]
248. Ethical, Legal and Social Aspects (ELSA) for AI: an assessment tool for Agri-food [312]
249. Ethics by design for artifcial intelligence [313]
250. Evaluation of AI Solutions in Health Care Organizations — The OPTICA Tool [314]
251. Evolving AI Risk Management: A Maturity Model based on the NIST AI Risk Management Framework [315]
252. Explainable Fairness in Regulatory Algorithmic Auditing [316]
253. FAIR Enough: Develop and Assess a FAIR-Compliant Dataset for Large Language Model Training? [317]
254. Fairframe: a fairness framework for bias detection and mitigation in news [318]
255. FairPIVARA: Reducing and Assessing Biases in CLIP-Based Multimodal Models [319]
256. FAMEWS: a Fairness Auditing tool for Medical Early-Warning Systems [320]
257. Framework for Bias Detection in Machine Learning Models: A Fairness Approach [321]
258. Generative artificial intelligence and ethical considerations in health care: a scoping review and ethics checklist [322]
259. Governance of Artificial Intelligence – A Framework Towards Ethical AI Applications [323]
260. How to design an AI ethics board [324]
261. Introducing the ethical-epistemic matrix: a principle-based tool for evaluating artificial intelligence in medicine [325]
262. MLCA: A Tool for Machine Learning Life Cycle Assessment [326]
263. Multi-Value Alignment for Ml/AI Development Choices A Four-step Process Including Approaches to Trade-offs [327]
264. POLARIS: A framework to guide the development of Trustworthy AI systems [328]
265. POTDAI: A Tool to Evaluate the Perceived Operational Trust Degree in Artificial Intelligence Systems [329]
266. Responsible AI Question Bank: A Comprehensive Tool for AI Risk Assessment [330]
267. Risk Assessment of Large Language Models Beyond Apocalyptic Visions [331]
268. RuleGLM: An Ethics Evaluation Framework with Knowledge Vector Space [332]
269. Safe LoRA: The Silver Lining of Reducing Safety Risks when Finetuning Large Language Models [333]
270. SafeInfer: Context Adaptive Decoding Time Safety Alignment for Large Language Models [334]
271. Scaling AI responsibly: Leveraging MLOps for sustainable machine learning deployments [335]
272. SORRY-Bench: Systematically Evaluating Large Language Model Safety Refusal [336]
273. Stream: social data and knowledge collective intelligence platform for TRaining Ethical AI Models [337]
274. tachAId—An interactive tool supporting the design of human-centered AI solutions [338]
275. TAI-PRM: trustworthy AI—project risk management framework towards Industry 5.0 [339]
276. The Artificial Intelligence Assessment Scale (AIAS): A Framework for Ethical Integration of Generative AI in Educational
Assessment [340]
277. The BIG Argument for AI Safety Cases [341]
55

--- Page 56 ---

278. The Principle-at-Risk Analysis (PaRA): Operationalising Digital Ethics by Bridging Principles and Operations of a Digital Ethics
Advisory [342]
279. Toolkit for specification, validation and verification of social, legal, ethical, empathetic and cultural requirements for autonomous
agents [343]
280. Toward a framework for risk mitigation of potential misuse of artificial intelligence in biomedical research [344]
281. Towards a framework for local interrogation of AI ethics: A case study on text generators, academic integrity, and composing
with ChatGPT [345]
282. Towards a Human-Centric AI Trustworthiness Risk Management Framework [346]
283. Towards a Responsible AI Metrics Catalogue: A Collection of Metrics for AI Accountability [347]
284. Towards Responsible AI Music: an Investigation of Trustworthy Features for Creative Systems [348]
285. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning
methods [349]
286. Trustworthy Artificial Intelligence: Design of AI Governance Framework [350]
287. What Would You do? An Ethical AI Quiz [351]
288. XAutoML: A Visual Analytics Tool for Understanding and Validating Automated Machine Learning [352]
56

```
