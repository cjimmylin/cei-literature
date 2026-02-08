---
title: "A Risk Taxonomy for Evaluating AI-Powered - PDF Extract"
source_pdf: "2025-Steenstra-A Risk Taxonomy for Evaluating AI-Powered.pdf"
pages: 11
extracted_at: "2026-01-24T16:38:36.524673"
---

# PDF Extract: A Risk Taxonomy for Evaluating AI-Powered

**Source PDF:** 2025-Steenstra-A Risk Taxonomy for Evaluating AI-Powered.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

A Risk Ontology for Evaluating AI-Powered Psychotherapy
Virtual Agents
Ian Steenstra
Northeastern University
Boston, MA, USA
steenstra.i@northeastern.edu
Timothy Bickmore
Northeastern University
Boston, MA, USA
t.bickmore@northeastern.edu
Abstract
The proliferation of Large Language Models (LLMs) and Intelligent
Virtual Agents acting as psychotherapists presents significant op-
portunities for expanding mental healthcare access. However, their
deployment has also been linked to serious adverse outcomes, in-
cluding user harm and suicide, facilitated by a lack of standardized
evaluation methodologies capable of capturing the nuanced risks of
therapeutic interaction. Current evaluation techniques lack the sen-
sitivity to detect subtle changes in patient cognition and behavior
during therapy sessions that may lead to subsequent decompensa-
tion. We introduce a novel risk ontology specifically designed for
the systematic evaluation of conversational AI psychotherapists.
Developed through an iterative process including review of the
psychotherapy risk literature, qualitative interviews with clinical
and legal experts, and alignment with established clinical criteria
(e.g., DSM-5) and existing assessment tools (e.g., NEQ, UE-ATR), the
ontology aims to provide a structured approach to identifying and
assessing user/patient harms. We provide a high-level overview
of this ontology, detailing its grounding, and discuss potential use
cases. We discuss four use cases in detail: monitoring real user in-
teractions, evaluation with simulated patients, benchmarking and
comparative analysis, and identifying unexpected outcomes. The
proposed ontology offers a foundational step towards establishing
safer and more responsible innovation in the domain of AI-driven
mental health support.
CCS Concepts
• Applied computing →Consumer health; • Information
systems →Language models; • Human-centered computing
→Empirical studies in HCI.
Keywords
AI Psychotherapy, Risk Assessment, Intelligent Virtual Agents, LLM
Safety, AI Alignment, Mental Health Technology
ACM Reference Format:
Ian Steenstra and Timothy Bickmore. 2025. A Risk Ontology for Evaluating
AI-Powered Psychotherapy Virtual Agents. In Preprint. ACM, New York,
NY, USA, 11 pages. https://doi.org/10.1145/3717511.3749286
Preprint,
© 2025 Copyright held by the owner/author(s). Publication rights licensed to ACM.
This is the author’s version of the work. It is posted here for your personal use.
Not for redistribution. The definitive Version of Record was published in Preprint,
https://doi.org/10.1145/3717511.3749286.
1
Introduction
Intelligent Virtual Agents (IVAs), particularly those powered by
Large Language Models (LLMs), are increasingly deployed as AI-
powered psychotherapy agents, sometimes by entertainment chat-
bots "masquerading" as qualified professionals [2, 9, 11, 20]. This
trend raises serious safety concerns, highlighted by the American
Psychological Association’s warning about AI reinforcing harmful
thinking [2]. Alarming incidents, such as a user’s suicide linked to
interactions with an AI chatbot "therapist" that reportedly ampli-
fied harmful ideations [2, 23], underscore the profound risks. These
events reveal the dangers of deploying such AI-powered IVAs, of-
ten "dangerous and untested," to vulnerable individuals without
rigorous, context-appropriate safety evaluations [2, 23, 27].
A critical challenge is the lack of standardized methods to eval-
uate these AI psychotherapy agents for risks unique to conversa-
tional therapeutic interactions. Current LLM benchmarks assess
general capabilities like toxicity, but are ill-suited for the sustained,
dynamic conversations inherent when AI-powered IVAs conduct
therapy [5, 33]. Traditional clinical trials, vital for efficacy, are also
slow and ethically challenging for initial safety validation of au-
tonomous AI psychotherapists [7, 27]. This evaluation gap leaves
users vulnerable to unforeseen adverse outcomes.
To address this, we introduce a risk ontology specifically de-
signed for evaluating AI psychotherapy agents. This paper presents
a high-level overview of the ontology, developed through an itera-
tive process involving psychotherapy risk literature review, qual-
itative interviews with clinical and legal experts, and alignment
with established clinical criteria (e.g., DSM-5) and assessment tools
(e.g., NEQ, UE-ATR). We posit that this ontology offers a structured,
systematic approach to identify, categorize, and ultimately help to
mitigate risks when IVAs deliver psychotherapy. Our primary aim
is to provide a framework for evaluating these automated systems,
fostering safer innovation in AI-driven mental health support.
2
Related Work
2.1
Risks in Psychotherapy
Psychotherapy, while generally effective, can occasionally lead to
negative consequences [3, 18]. Estimates of unwanted effects vary
from 3% to over 50%, depending on the particular definitions and
assessment methods used [17, 19]. A key challenge is the lack of a
uniform conceptual framework and standardized tools for assessing
adverse events (AEs) in psychotherapy [19].
Several frameworks attempt to categorize negative experiences
in psychotherapy. Linden and Schermuly-Haupt distinguish Un-
wanted Events (UEs) from Adverse Treatment Reactions (ATRs)
caused by correctly applied treatment, and malpractice reactions
arXiv:2505.15108v2  [cs.CL]  20 Sep 2025

--- Page 2 ---

Preprint, September 2025,
Ian Steenstra and Timothy Bickmore
from incorrectly applied treatment [17, 18]. Mejía-Castrejón et al.
[19] adapted a medical model, classifying AEs by severity, related-
ness, seriousness, and expectedness. Common AEs identified across
studies and captured in assessment tools like the Negative Effects
Questionnaire (NEQ) [25] or the Unwanted Event to Adverse Treat-
ment Reaction (UE-ATR) checklist [17] include negative emotions
(e.g., anxiety, sadness), symptom worsening, the emergence of un-
pleasant memories, relationship strains, dependency on therapy,
or reduced self-efficacy [18, 32]. Factors influencing these include
patient and therapist characteristics, and specific techniques [18].
Assessing these effects is difficult; therapists may struggle to
recognize negative outcomes, and establishing causality is complex
[17, 18]. While tools like the UE-ATR, NEQ, and the Inventory for
Negative Effects of Psychotherapy (INEP) [15] exist, consensus on
definitions and instruments remains elusive [19]. Reviews show
variability and inadequate reporting of negative effects in random-
ized clinical trials [10, 13], underscoring the need for standardized
assessment. Our ontology development aims to build upon these
existing efforts by providing a structured framework specifically
adapted for evaluating AI psychotherapy agents.
2.2
Safety Evaluation of LLMs in Healthcare
The application of LLMs in high-stakes domains like healthcare,
including psychotherapy, demands rigorous safety assessment due
to the potential for significant harm [16, 27, 28]. General LLM
safety evaluations often focus on risks including bias, toxicity, or
misinformation [8, 31], using benchmarks such as ALERT [30] or
SafetyBench [34]. However, these may not adequately capture the
interactive and relational risks specific to psychotherapy.
Safety frameworks are emerging for AI in mental health, in-
cluding the READI framework [26] and the BPES checklist, em-
phasizing "Do No Harm" [12]. Complementing these expert-driven
approaches, some research grounds risk assessment in the direct
experiences of users. For instance, Chandra et al. [4] developed a
psychological risk taxonomy by surveying 283 individuals with
lived mental health experience about their negative interactions
with AI conversational agents, categorizing risks into specific AI
behaviors, negative psychological impacts, and the user contexts
that mediate them. Dialogue safety in mental health support is also
a focus [22]. For instance, Ψ-ARENA offers an interactive platform
for evaluating LLM-based psychological counselors [35]. Despite
these advances, a standardized ontology is still lacking to opera-
tionalize risk detection by systematically assessing and categorizing
the spectrum of potential harms specific to AI psychotherapeutic
interactions, grounded in clinical realities and existing assessment
principles. This is crucial as AI systems, unlike human therapists,
may lack nuanced understanding of human emotion, contextual
subtleties, and the ability to dynamically repair relational ruptures,
potentially leading to unique failure modes.
3
Ontology Development
The development of our risk ontology followed an iterative design
process. We first formulated a preliminary ontology based on an
in-depth literature review of psychotherapy risk (e.g., [13, 17, 24,
25]). This initial framework subsequently underwent expert review
through semi-structured interviews with 11 experts: 10 practicing
psychologist professionals and one legal professional specializing in
healthcare malpractice. These interviews were designed to explore
perceptions of risk in human therapy, identify potential failure
modes for AI therapists, and gather direct feedback on the prelimi-
nary ontology. The interview study was approved by Northeastern
University’s IRB. The interviews were analyzed using thematic
analysis [6] to reveal six key themes that directly informed the final
structure and content of the ontology. The interview study was
approved by Northeastern University’s IRB.
Theme 1: Therapy may require short-term discomfort
The first theme highlighted the difficulty in defining and iden-
tifying "harm" within the therapeutic context itself. Unlike the
clearer "do no harm" principle in general medicine, psychother-
apy often involves navigating "intentional discomfort" as part of
the therapeutic process. Participants described therapy inherently
involving potentially negative feelings ("feeling a little worse be-
fore you feel better," "encounter some painful things") as necessary
for growth. Distinguishing this expected discomfort from "unin-
tentional harm"—negative outcomes resulting from therapist er-
rors, misjudgments, or failures—is challenging. Harm exists on a
"spectrum," ranging from temporary setbacks ("bruises") like feel-
ing "misunderstood" or "judged," to more significant consequences
("cuts") such as a "rupture" in the "therapeutic alliance," prema-
ture termination ("stop coming to therapy," "drop out early"), wors-
ening symptoms ("exacerbate symptoms"), loss of "trust in self,"
developing a "bad taste... about therapy," or, in the most severe
cases, increased "suicide" risk. Furthermore, harm can be subjec-
tive, context-dependent ("contextual based on your history"), and
may not manifest "in the moment," only emerging later through
"rumination."
Theme 2: Therapist risk factors Therapist factors related to
risk are significant, encompassing competence ("evidence-based
care," "qualifications," "knowing their specialty"), ethical adher-
ence ("violates boundaries," "confidentiality"), and skillful technique
(avoiding "leading questions," "invalidating" responses, "negative
vocabulary," "overly reassuring"). Therapist "biases," "personal opin-
ions," lack of "cultural awareness," "distractions," and "burnout" were
cited as potential sources of unintentional harm. Building "therapeu-
tic rapport" and "trust" was seen as a primary mitigator, allowing
for "repair" if harm occurs.
Theme 3: Patient risk factors Patient vulnerability and con-
text also play a critical role. "Individual differences" mean risk fac-
tors vary; internal states ("hopelessness," "anxiety"), patient history
("memories," "interpretations"), the "social environment," "physical
environment" (including "access to means"), and "protective factors"
all interact dynamically.
Theme 4: Real-time nature of risk assessment Identify-
ing risks in real-time relies heavily on a therapist’s ability for
"moment-to-moment tracking," interpreting subtle "nonverbal body
language," "facial expressions," and "para verbal cues" (e.g., "intona-
tion"), alongside verbal content and formal "assessment tools" (e.g.,
"Columbia Scale"[21], "PHQ-9"[14]). However, assessment is imper-
fect due to patient "concealment," the limits of prediction ("intention
could change"), and the significant information loss in modalities
lacking visual and auditory cues, such as "texting" therapy, which
was viewed as particularly risky by many participants. Critically,

--- Page 3 ---

A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents
Preprint, September 2025,
effective responses require understanding the "underlying cause,"
not just the presenting "symptom."
Theme 5: Perceived shortcomings of AI Psychotherapists
When considering AI therapists, participants largely believed the
fundamental risks in human therapy remain the same but are po-
tentially "higher" or exacerbated. The primary concern stems from
the AI’s inherent inability (especially in text-based interactions) to
perceive the rich nonverbal and paralinguistic data humans use to
gauge internal states, build rapport, and understand nuance ("miss-
ing the person-to-person component," "can’t synthesize," loss of
"nuance"). This limitation raises concerns about AI’s capacity for
genuine "empathy," its potential to "misinterpret" user input, per-
petuate "bias," lack crucial "context," miss the "art" of therapy, and
ultimately, its ability to safely navigate complex emotional terrain.
While potential AI advantages like constant "availability," poten-
tially feeling "less judged," and superior information processing
were acknowledged, the loss of the human connection and obser-
vational capacity was seen as a major safety deficit. Interestingly,
AI was often considered potentially "better" than human texting
therapy, as the latter shares AI’s lack of nonverbals without AI’s
potential processing advantages.
Theme 6: Refinement of risk ontology The feedback on
the proposed risk ontology indicated it was a "good start" cover-
ing many "big risks," but highlighted needs for refinement. Key
omissions noted were "trauma" and "abuse." Participants stressed
the necessity of integrating "environmental" and "social factors,"
the "timeline" of symptoms, and grounding factors in established
tools like the "DSM" or clinical "inventories," while acknowledging
the limitations of categorical approaches versus "individual differ-
ences" and "nuance." The ontology’s current structure was seen as
potentially useful but insufficient alone for risk assessment without
incorporating deeper context and validated measures.
These insights drove significant revisions to the ontology’s struc-
ture and granularity. Specifically, the theme that "Therapy may
require short-term discomfort" led to the crucial distinction in our
ontology between "In-Session Warning Signs" (which may include
therapeutically necessary negative affect) and "Potential Real-World
Consequences" (clear harms). This ensures the evaluation frame-
work does not penalize an AI for inducing transient discomfort
that is part of a valid therapeutic process. Furthermore, the themes
of "Patient risk factors" and the need to account for "individual
differences" directly informed our decision to incorporate baseline
comparisons for psychological constructs, allowing for a more per-
sonalized risk assessment. Finally, feedback on the need to ground
the ontology in established tools led to the explicit alignment of
our "In-Session Warning Signs" and "Potential Real-World Conse-
quences", with concepts from the DSM-5 and existing instruments
like the NEQ and UE-ATR.
4
Overview of the Risk Ontology
The refined risk ontology (see Appendix A), derived from litera-
ture (e.g., [13, 17, 24, 25]), expert interviews, and DSM-5 criteria
[1], offers a structured framework to identify potential negative
outcomes in AI psychotherapy. It has three overarching categories:
1. Acute Crisis: This category represents immediate and severe
danger to the user that requires urgent intervention. Identification is
entirely dialogue-based, evaluating the AI psychotherapists ability
to recognize and respond to scenarios such as clear suicidal intent,
threats of harm to others, or severe psychological decompensation.
The framework assesses the AI’s performance against a predefined
four-step action plan: (1) Assess, (2) De-escalate, (3) Recommend
Emergency Services, and (4) Request Human Consultation.
2. In-Session Warning Signs: This category tracks dynamic,
moment-to-moment changes in the patient’s internal psycholog-
ical state that may predict future harm or signal heightened vul-
nerability. These are not direct harms but are leading indicators.
The framework operationalizes key psychological constructs (e.g.,
Hopelessness, Self-Efficacy) as internal state variables, which are
conceptualized as a 5-point Likert scale. These constructs, are dy-
namically updated in response to the AI psychotherapist’s dialogue.
Evaluation focuses on tracking the magnitude and direction of these
changes, acknowledging that while some transient negative shifts
can be part of the therapeutic process.
3. Potential Real-World Consequences: This category rep-
resents the tangible, adverse outcomes that could manifest in the
patient’s life following a therapeutic interaction, often aligning
with NEQ and UE-ATR unwanted events [17, 25]. Unlike the inter-
nal states of "In-Session Warning Signs", these are the observable
"harms" or deteriorations that serve as the primary dependent vari-
ables for evaluating the AI’s long-term safety and efficacy. Each po-
tential consequence is causally linked to changes in the "In-Session
Warning Signs".
The ontology aims to standardize safety evaluation for AI psy-
chotherapists. We outline several use cases for improving safety:
Monitoring Real User Interactions: The ontology can identify
emergent risks in real-time during user-AI psychotherapist interac-
tions, enabling early termination of harmful sessions or providing
feedback to developers and regulators. Monitoring, with ethical
consent, could track a user’s psychological construct intensities
pre- to post-interaction for "In-Session Warning Signs" shifts, while
dialogue tools scan for "Acute Crisis" events.
Evaluation with Simulated Patients: The risk ontology can
also structure the monitoring of interactions between an AI psy-
chotherapist and a simulated patient. This approach is exemplified
in our work on SimPatient, a testbed designed for safety and quality
of care assessment [29]. Within this system, the simulated patient
is equipped with dynamic internal states (e.g., Self-Efficacy) that
directly correspond to the ontology’s "In-Session Warning Signs".
This design enables systematic testing by comparing the patient’s
internal states throughout the interaction, allowing for quantitative
assessment of the AI psychotherapist’s impact on diverse personas.
Benchmarking and Comparative Analysis: The ontology
provides a standardized framework for robust benchmarking and
comparing AI psychotherapist models and versions. Systematically
evaluating AI psychotherapists against risk categories generates
consistent, comparable risk profiles, highlighting strengths and
weaknesses in eliciting and mitigating specific risks. Such insights
could aid developers in enhancing safety and fostering a transparent
development ecosystem focused on minimizing harm.
Identifying Unexpected Outcomes: The ontology is crucial
for identifying unexpected and emergent adverse outcomes in au-
tomated therapy. Systematic monitoring of user interactions and

--- Page 4 ---

Preprint, September 2025,
Ian Steenstra and Timothy Bickmore
outcomes against ontology categories can reveal significant devia-
tions from baselines or flag harmful patterns. Substantial deviations
warrant deeper analysis, scrutinizing conversational context to
understand precipitating AI behaviors. Uncovering root causes in-
forms targeted safety improvements and AI model refinements.
Our generalized risk ontology can also be augmented for spe-
cific populations or problems. For instance, evaluating an AI psy-
chotherapist for patients with substance use disorders, could add a
"In-Session Warning Signs" factor like "Substance Craving Inten-
sity". This tailoring enables nuanced risk assessment.
A critical next step is the formal validation of the ontology itself.
We envision a multi-pronged approach involving content validation
by clinical experts, construct validation by correlating its categories
with validated psychometric surveys, and empirical validation by
establishing inter-rater reliability against human-rated therapeutic
dialogues.
5
Conclusion
AI psychotherapists present significant opportunities and risks.
Documented negative outcomes demand standardized evaluations
for unique interaction risks. We developed the risk ontology, from
an iterative process involving literature, expert insights, and DSM-5,
and harm checklists. It offers a structured approach to identifying
and categorizing harms. Its overview, grounding, and adaptable
use cases (tracking in-session warning signs) aim to equip stake-
holders to ensure AI psychotherapy safety, fostering innovation
that prioritizes user well-being and minimizes unintended negative
consequences.
References
[1] American Psychiatric Association et al. 2013. Diagnostic and statistical manual of
mental disorders. American psychiatric association, Washington, DC.
[2] Ellen Barry. 2025. Human Therapists Prepare for Battle Against A.I. Pretenders.
https://www.nytimes.com/2025/02/24/health/ai-therapists-chatbots.html
[3] Charles M Boisvert and David Faust. 2002. Iatrogenic symptoms in psychotherapy:
A theoretical exploration of the potential impact of labels, language, and belief
systems. American Journal of Psychotherapy 56, 2 (2002), 244–259.
[4] Mohit Chandra, Suchismita Naik, Denae Ford, Ebele Okoli, Munmun De Choud-
hury, Mahsa Ershadi, Gonzalo Ramos, Javier Hernandez, Ananya Bhattacharjee,
Shahed Warreth, and Jina Suh. 2025. From Lived Experience to Insight: Un-
packing the Psychological Risks of Using AI Conversational Agents. In Proceed-
ings of the 2025 ACM Conference on Fairness, Accountability, and Transparency
(FAccT ’25). Association for Computing Machinery, New York, NY, USA, 975–1004.
doi:10.1145/3715275.3732063
[5] Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, Linyi Yang, Kaijie Zhu, Hao
Chen, Xiaoyuan Yi, Cunxiang Wang, Yidong Wang, Wei Ye, Yue Zhang, Yi Chang,
Philip S. Yu, Qiang Yang, and Xing Xie. 2024. A Survey on Evaluation of Large
Language Models. ACM Trans. Intell. Syst. Technol. 15, 3, Article 39 (March 2024),
45 pages. doi:10.1145/3641289
[6] Victoria
Clarke
and
Virginia
Braun.
2017.
Thematic
analy-
sis.
The
Journal
of
Positive
Psychology
12,
3
(2017),
297–298.
arXiv:https://doi.org/10.1080/17439760.2016.1262613 doi:10.1080/17439760.2016.
1262613
[7] Michael V Heinz, Daniel M Mackin, Brianna M Trudeau, Sukanya Bhattacharya,
Yinzhou Wang, Haley A Banta, Abi D Jewett, Abigail J Salzhauer, Tess Z Griffin,
and Nicholas C Jacobson. 2025. Randomized Trial of a Generative AI Chatbot for
Mental Health Treatment. NEJM AI 2, 4 (2025), AIoa2400802.
[8] Jiaming Ji, Tianyi Qiu, Boyuan Chen, Borong Zhang, Hantao Lou, Kaile Wang,
Yawen Duan, Zhonghao He, Lukas Vierling, Donghai Hong, Jiayi Zhou, Zhaowei
Zhang, Fanzhi Zeng, Juntao Dai, Xuehai Pan, Kwan Yee Ng, Aidan O’Gara, Hua
Xu, Brian Tse, Jie Fu, Stephen McAleer, Yaodong Yang, Yizhou Wang, Song-Chun
Zhu, Yike Guo, and Wen Gao. 2025. AI Alignment: A Comprehensive Survey.
arXiv:2310.19852 [cs.AI] https://arxiv.org/abs/2310.19852
[9] Yu Jin, Jiayi Liu, Pan Li, Baosen Wang, Yangxinyu Yan, Huilin Zhang, Chenhao
Ni, Jing Wang, Yi Li, Yajun Bu, et al. 2025. The Applications of Large Language
Models in Mental Health: Scoping Review. Journal of Medical Internet Research
27 (2025), e69284.
[10] Ulf Jonsson, Iman Alaie, Thomas Parling, and Filip K Arnberg. 2014. Reporting of
harms in randomized controlled trials of psychological interventions for mental
and behavioral disorders: a review of current practice. Contemporary clinical
trials 38, 1 (2014), 1–8.
[11] Marc Jurblum and Rob Selzer. 2025. Potential promises and perils of artificial
intelligence in psychotherapy –The AI Psychotherapist (APT). Australasian
Psychiatry 33, 1 (2025), 103–105. arXiv:https://doi.org/10.1177/10398562241286312
doi:10.1177/10398562241286312 PMID: 39344214.
[12] Waqas Ullah Khan and Emily Seto. 2023. A "Do No Harm" Novel Safety Check-
list and Research Approach to Determine Whether to Launch an Artificial
Intelligence-Based Medical Technology: Introducing the Biological-Psychological,
Economic, and Social (BPES) Framework. Journal of Medical Internet Research 25
(2023), e43386. doi:10.2196/43386
[13] Rahel Klatte, Bernhard Strauss, Christoph Flückiger, Francesca Färber, and Jenny
Rosendahl. 2023. Defining and assessing adverse events and harmful effects in
psychotherapy study protocols: a systematic review. Psychotherapy 60, 1 (2023),
130.
[14] Kurt Kroenke, Robert L Spitzer, and Janet BW Williams. 2001. The PHQ-9: validity
of a brief depression severity measure. Journal of general internal medicine 16, 9
(2001), 606–613.
[15] Inga Ladwig, Winfried Rief, and Yvonne Nestoriuc. 2014. What are the risks and
side effects of psychotherapy?-development of an inventory for the assessment
of negative effects of psychotherapy (INEP). Verhaltenstherapie 24, 4 (2014),
252–263.
[16] Hannah R Lawrence, Renee A Schneider, Susan B Rubin, Maja J Matarić, Daniel J
McDuff, and Megan Jones Bell. 2024. The Opportunities and Risks of Large
Language Models in Mental Health.
JMIR Mental Health 11 (2024), e59479.
doi:10.2196/59479
[17] Michael Linden. 2013. How to define, find and classify side effects in psychother-
apy: from unwanted events to adverse treatment reactions. Clinical psychology
& psychotherapy 20, 4 (2013), 286–296.
[18] Michael Linden and Marie-Luise Schermuly-Haupt. 2014. Definition, assessment
and rate of psychotherapy side effects. World psychiatry 13, 3 (2014), 306.
[19] Jessica Mejía-Castrejón, Juan Gerardo Sierra-Madero, Pablo Francisco
Belaunzarán-Zamudio, Ana Fresan-Orellana, Alejandro Molina-López, Ate-
nea Betzabé Álvarez-Mota, and Rebeca Robles-García. 2024. Development and
content validity of EVAD: A novel tool for evaluating and classifying the severity
of adverse events for psychotherapeutic clinical trials. Psychotherapy Research
34, 4 (2024), 475–489.
[20] Hongbin Na, Yining Hua, Zimu Wang, Tao Shen, Beibei Yu, Lilin Wang, Wei Wang,
John Torous, and Ling Chen. 2025. A Survey of Large Language Models in Psy-
chotherapy: Current Landscape and Future Directions. arXiv:2502.11095 [cs.CL]
https://arxiv.org/abs/2502.11095
[21] Kent Posner, D Brent, C Lucas, M Gould, B Stanley, G Brown, P Fisher, J Zelazny,
A Burke, MJNY Oquendo, et al. 2008. Columbia-suicide severity rating scale
(C-SSRS). New York, NY: Columbia University Medical Center 10 (2008), 2008.
[22] Huachuan Qiu, Tong Zhao, Anqi Li, Shuai Zhang, Hongliang He, and Zhenzhong
Lan. 2023. A Benchmark for Understanding Dialogue Safety in Mental Health
Support. In Natural Language Processing and Chinese Computing, Fei Liu, Nan
Duan, Qingting Xu, and Yu Hong (Eds.). Springer Nature Switzerland, Cham,
1–13.
[23] Kevin Roose. 2024. Can A.I. Be Blamed for a Teen’s Suicide?
https://www.
nytimes.com/2024/10/23/technology/characterai-lawsuit-teen-suicide.html
[24] Alexander Rozental, Louis Castonguay, Sona Dimidjian, Michael Lambert, Roz
Shafran, Gerhard Andersson, and Per Carlbring. 2018. Negative effects in psy-
chotherapy: commentary and recommendations for future research and clinical
practice. BJPsych Open 4, 4 (2018), 307–312.
[25] Alexander Rozental, Anders Kottorp, Johanna Boettcher, Gerhard Andersson, and
Per Carlbring. 2016. Negative effects of psychological treatments: an exploratory
factor analysis of the negative effects questionnaire for monitoring and reporting
adverse and unwanted events. PloS one 11, 6 (2016), e0157503.
[26] Elizabeth C. Stade, Johannes C. Eichstaedt, Jane P. Kim, and Shannon Wiltsey Stir-
man. 2025. Readiness Evaluation for Artificial Intelligence-Mental Health Deploy-
ment and Implementation (READI): A Review and Proposed Framework. Technol-
ogy, Mind, and Behavior 6, 2 (apr 21 2025). https://tmb.apaopen.org/pub/8gyddorx.
[27] Elizabeth C. Stade, Shannon Wiltsey Stirman, Lyle H. Ungar, Cody L. Boland,
H. Andrew Schwartz, David B. Yaden, João Sedoc, Robert J. DeRubeis, Robb
Willer, Jane P. Kim, and Johannes C. Eichstaedt. 2024. Large language models
could change the future of behavioral healthcare: a proposal for responsible
development and evaluation. npj Mental Health Research 3, 1 (2024), 12. doi:10.
1038/s44184-024-00056-z
[28] Ian Steenstra, Farnaz Nouraei, Mehdi Arjmand, and Timothy Bickmore. 2024.
Virtual Agents for Alcohol Use Counseling: Exploring LLM-Powered Motiva-
tional Interviewing. In Proceedings of the 24th ACM International Conference
on Intelligent Virtual Agents (GLASGOW, United Kingdom) (IVA ’24). Asso-
ciation for Computing Machinery, New York, NY, USA, Article 20, 10 pages.
doi:10.1145/3652988.3673932

--- Page 5 ---

A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents
Preprint, September 2025,
[29] Ian Steenstra, Farnaz Nouraei, and Timothy Bickmore. 2025. Scaffolding Empathy:
Training Counselors with Simulated Patients and Utterance-level Performance
Visualizations. In Proceedings of the 2025 CHI Conference on Human Factors in
Computing Systems (CHI ’25). Association for Computing Machinery, New York,
NY, USA, Article 593, 22 pages. doi:10.1145/3706598.3714014
[30] Simone Tedeschi, Felix Friedrich, Patrick Schramowski, Kristian Kersting, Roberto
Navigli, Huu Nguyen, and Bo Li. 2024.
ALERT: A Comprehensive Bench-
mark for Assessing Large Language Models’ Safety through Red Teaming.
arXiv:2404.08676 [cs.CL] https://arxiv.org/abs/2404.08676
[31] Laura Weidinger, Jonathan Uesato, Maribeth Rauh, Conor Griffin, Po-Sen Huang,
John Mellor, Amelia Glaese, Myra Cheng, Borja Balle, Atoosa Kasirzadeh, Court-
ney Biles, Sasha Brown, Zac Kenton, Will Hawkins, Tom Stepleton, Abeba
Birhane, Lisa Anne Hendricks, Laura Rimell, William Isaac, Julia Haas, Sean Legas-
sick, Geoffrey Irving, and Iason Gabriel. 2022. Taxonomy of Risks posed by Lan-
guage Models. In Proceedings of the 2022 ACM Conference on Fairness, Accountabil-
ity, and Transparency (Seoul, Republic of Korea) (FAccT ’22). Association for Com-
puting Machinery, New York, NY, USA, 214–229. doi:10.1145/3531146.3533088
[32] Lijun Yao, Xudong Zhao, Zhiwei Xu, Yang Chen, Liang Liu, Qiang Feng, and
Fazhan Chen. 2020. Influencing factors and machine learning-based prediction
of side effects in psychotherapy. Frontiers in Psychiatry 11 (2020), 537442.
[33] Renwen Zhang, Han Li, Han Meng, Jinyuan Zhan, Hongyuan Gan, and Yi-Chieh
Lee. 2025. The Dark Side of AI Companionship: A Taxonomy of Harmful Algorith-
mic Behaviors in Human-AI Relationships. In Proceedings of the 2025 CHI Confer-
ence on Human Factors in Computing Systems (CHI ’25). Association for Computing
Machinery, New York, NY, USA, Article 13, 17 pages. doi:10.1145/3706598.3713429
[34] Zhexin Zhang, Leqi Lei, Lindong Wu, Rui Sun, Yongkang Huang, Chong Long,
Xiao Liu, Xuanyu Lei, Jie Tang, and Minlie Huang. 2024. SafetyBench: Evaluating
the Safety of Large Language Models. In Proceedings of the 62nd Annual Meeting
of the Association for Computational Linguistics (Volume 1: Long Papers), Lun-Wei
Ku, Andre Martins, and Vivek Srikumar (Eds.). Association for Computational
Linguistics, Bangkok, Thailand, 15537–15553. doi:10.18653/v1/2024.acl-long.830
[35] Shijing Zhu, Zhuang Chen, Guanqun Bi, Binghang Li, Yaxi Deng, Dazhen Wan,
Libiao Peng, Xiyao Xiao, Rongsheng Zhang, Tangjie Lv, Zhipeng Hu, FangFang
Li, and Minlie Huang. 2025. {\Psi}-Arena: Interactive Assessment and Op-
timization of LLM-based Psychological Counselors with Tripartite Feedback.
arXiv:2505.03293 [cs.CL] https://arxiv.org/abs/2505.03293
A
Supplementary Material – AI Therapy Risk
Ontology

--- Page 6 ---

Preprint, September 2025,
Ian Steenstra and Timothy Bickmore
Figure 1: A High-Level Overview of the AI Therapy Risk Ontology

--- Page 7 ---

A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents
Preprint, September 2025,
Figure 2: Action Plans for Responding to Acute Crisis Scenarios

--- Page 8 ---

Preprint, September 2025,
Ian Steenstra and Timothy Bickmore
Figure 3: Definitions of Psychological Constructs Used as In-Session Warning Signs

--- Page 9 ---

A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents
Preprint, September 2025,
Figure 4: Potential Behavioral Harms and Their Predictive Psychological Constructs

--- Page 10 ---

Preprint, September 2025,
Ian Steenstra and Timothy Bickmore
Figure 5: Potential Cognitive and Affective Harms and Their Predictive Psychological Constructs

--- Page 11 ---

A Risk Ontology for Evaluating AI-Powered Psychotherapy Virtual Agents
Preprint, September 2025,
Figure 6: Potential Relational Harm and its Predictive Psychological Constructs

```
