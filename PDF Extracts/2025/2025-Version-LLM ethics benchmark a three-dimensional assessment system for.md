---
title: "2025-Version-LLM ethics benchmark a three-dimensional assessment system for - PDF Extract"
source_pdf: "2025-Version-LLM ethics benchmark a three-dimensional assessment system for.pdf"
pages: 20
extracted_at: "2026-02-13T14:50:58.514887"
---

# PDF Extract: 2025-Version-LLM ethics benchmark a three-dimensional assessment system for

**Source PDF:** 2025-Version-LLM ethics benchmark a three-dimensional assessment system for.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

LLM Ethics Benchmark
A Three-Dimensional Assessment System for Evaluating
Moral Reasoning in Large Language Models
Junfeng Jiao
Urban Information Lab
The University of Texas at Austin
jjiao@austin.utexas.edu
Saleh Afroogh1
Urban Information Lab
The University of Texas at Austin
saleh.afroogh@utexas.edu
Abhejay Murali
Department of Computer Science
The University of Texas at Austin
abhejay.murali@utexas.edu
Kevin Chen
Urban Information Lab
The University of Texas at Austin
xc4646@utexas.edu
David Atkinson
McCombs School of Business
The University of Texas at Austin
davida@allenai.org
Amit Dhurandhar
IBM Research
Yorktown Heights, USA
adhuran@us.ibm.com
Abstract
This study establishes a novel framework for systematically evaluating the moral
reasoning capabilities of large language models (LLMs) as they increasingly in-
tegrate into critical societal domains. Current assessment methodologies lack the
precision needed to evaluate nuanced ethical decision-making in AI systems, cre-
ating significant accountability gaps. Our framework addresses this challenge
by quantifying alignment with human ethical standards through three dimen-
sions: foundational moral principles, reasoning robustness, and value consis-
tency across diverse scenarios. This approach enables precise identification of
ethical strengths and weaknesses in LLMs, facilitating targeted improvements
and stronger alignment with societal values. To promote transparency and col-
laborative advancement in ethical AI development, we are publicly releasing
both our benchmark datasets and evaluation codebase at https://github.com/
The-Responsible-AI-Initiative/LLM_Ethics_Benchmark.git.
Keywords:LLM, Moral Reasoning, AI Alignment, Benchmark Datasets, Responsible AI
1
Introduction
1.1
Background
The rapid advancement and widespread adoption of Large Language Models (LLMs) have profoundly
transformed their capabilities, progressing from simple text generators to sophisticated agents that
are becoming increasingly crucial in significant decision-making processes [10]. These models now
1Corresponding author: saleh.afroogh@utexas.edu
Preprint. Under review.
arXiv:2505.00853v1  [cs.CY]  1 May 2025

--- Page 2 ---

influence numerous sectors, such as healthcare and finance, raising vital questions about their capacity
to function within ethical and moral boundaries [78]. Understanding and assessing these capabilities
has become crucial, especially as LLMs start to influence public dialogue and affect human choices in
ethically sensitive situations [8]. Conventional evaluation techniques, although proficient in assessing
technical skills, often fall short in addressing the complex dimensions of moral and ethical reasoning
that these models are now required to exhibit [33].
1.2
Research Gap
Despite the growing influence of large language models (LLMs) on decision-making, there is a
significant gap in the methods employed to evaluate their moral reasoning capabilities [1]. Current
assessment techniques encounter numerous obstacles: they lack consistency, rely on overly simplistic
scenarios, and do not adequately account for the complex and interconnected elements of moral
decision-making [68]. Additionally, existing frameworks do not sufficiently recognize the distinct
features of LLMs, including their stochastic nature, the variety of human-generated content they
are trained on, and their capacity to produce contextually appropriate responses. While there are
established tools for human moral assessment, these cannot be directly applied to LLMs without
considerable modifications to address the essential differences between human moral development
and the ethical processing capabilities of LLMs.
1.3
Objectives
This study aims to develop a comprehensive framework for evaluating the moral reasoning capabilities
of Large Language Models (LLMs) through several primary objectives. Our principal goal is to create
a streamlined, three-dimensional assessment framework that captures the essential components of
moral reasoning while providing quantifiable metrics for evaluation [1]. The framework emphasizes
Moral Foundation Alignment, Reasoning Index, and Value Consistency, which together encompass
the scope and depth of moral reasoning in AI systems [68]. We will modify established measures
from moral psychology—including the Moral Foundations Questionnaire (MFQ), Moral Dilemmas,
and the World Values Survey (WVS)—to develop a methodology specifically suited for LLMs
[8]. This adaptation aims to establish standardized evaluation protocols that consider the distinct
characteristics of LLMs, such as their statistical nature and their capacity to produce contextually
appropriate responses [33]. Furthermore, we plan to perform comparative analyses across various
LLM architectures to explore differences in moral reasoning capabilities and to identify trends in how
different models tackle ethical decision-making [10]. These objectives collectively aim to establish
solid baseline metrics for evaluating moral consistency and ethical reasoning in generative AI, thereby
contributing to the overarching goal of fostering more ethically conscious and responsible artificial
intelligence.
1.4
Paper Structure
The organization of this document is as follows: Section 2 reviews current methods of moral evalua-
tion, emphasizing both AI assessment techniques and relevant literature on human morality. Section
3 outlines our approach to adapting moral evaluation methods specifically for large language models
(LLMs), which involves the selection and modification of human moral assessments. Section 4 out-
lines our suggested framework for evaluating the moral reasoning of large language models (LLMs),
addressing the experimental design, implications, challenges, and possible avenues for future research.
Section 5 elaborates on the experimental outcomes across multiple aspects of moral reasoning, such
as overall effectiveness, specific moral foundations, components of reasoning, consistency, and failure
modes. Lastly, Section 6 wraps up with a summary of the findings, contributions, and considerations
regarding the implications for AI ethics and development.
2
Related Work
2.1
AI Evaluation Techniques
In the fast-changing world of artificial intelligence, evaluating Large Language Models (LLMs) has
become a significant challenge that has evolved considerably. The field has progressed beyond the
2

--- Page 3 ---

basic evaluation metrics used in early natural language processing, adopting a new wave of advanced
benchmarking methods. These benchmarks are essential for assessing LLM performance across
a variety of tasks and challenges, with their results increasingly monitored through standardized
leaderboards [40]. The evaluation frameworks can be organized into three main categories: gen-
eral language tasks, specific downstream tasks, and multi-modal tasks. In general language tasks,
benchmarks such as SocKET [14] and XieZhi [27] evaluate overall language understanding, whereas
specialized frameworks like KoLA [95] focus on specific language abilities through self-contrast
metrics and leaderboard assessments. The progress in evaluation metrics has led to the development
of sophisticated frameworks like DynaBench [44] and AGIEval [100], which employ dynamic evalu-
ation methods and human-centered foundational models, respectively. Importantly, benchmarks such
as GLUE X [90] and GAOKAO-Bench [91] aim to improve out-of-distribution (OOD) robustness
in natural language processing applications. Furthermore, the recent introduction of PromptBench
[101] has greatly enhanced our understanding of model resilience against adversarial prompts, while
FreshLLMs [80] explores the advantages of search engine augmentation to improve performance.
In the domain of specific downstream tasks, the evaluation framework becomes increasingly special-
ized and technically detailed. The evaluation of mathematical reasoning skills is executed through
MATH [32] and various targeted frameworks that emphasize algebraic word problems [36, 47, 55].
Coding capabilities are assessed via APPS [30], while legal understanding is measured through tools
like CUAD [31] and particular tasks focused on predicting legal rulings [13]. The assessment of
medical knowledge is conducted through MultiMedQA [76] and CMB [82], which evaluate both
general medical knowledge and proficiency in Chinese medicine. Furthermore, there have been
significant advancements in the evaluation of tool usage, with frameworks such as ToolBench [77]
and API-Bank providing comprehensive assessments of models’ abilities to interact with external
tools and APIs. Interactive skills are measured through several frameworks, such as Dialogue CoT
[81], which focuses on detailed dialogue analysis, MT-Bench [58] for evaluating the quality of
conversations, and the LMSYS Chatbot Arena [58] for comparing different models. In addition,
M3Exam [97] and LVLM-eHub [89] have introduced creative methodologies for comprehensive
multi-modal evaluations that address various levels of difficulty and domains.
The growing emphasis on safety and ethical considerations has led to the establishment of specific
frameworks, including TrustGPT [39] for evaluating toxicity and bias, CValues [88] for assessing
safety and responsibility, and SafetyBench [99] for a thorough evaluation of safety capabilities. These
frameworks are grounded in earlier research on social [74] and gender bias recognition [73] and
incorporate insights from studies on moral disengagement mechanisms [7]. The development of
frameworks for multi-modal evaluation, such as MME [22], MMBench [56], and MM-Vet [93],
reflects the increasing importance of assessing large language models (LLMs) in their ability to
process and generate a variety of data types. Additionally, specific benchmarks like EmotionBench
[37] for empathy evaluation, CMMLU [38] for multi-tasking assessment in Chinese, and HELM [52]
for comprehensive evaluations have been established. The study of multi-modal understanding is
further developed through LAMM [92] and SEED-Bench [49].
Although there are extensive technical evaluation frameworks in place, there remain considerable
deficiencies in systematic methodologies for ethical evaluation. While initiatives such as TrustGPT
[39] and Human-AI Moral Consistency tests [34] mark initial progress in ethical assessments, they
only cover a small portion of the overall evaluation landscape. This limitation is particularly clear
when examining the arguments presented by Bryson and Kime [11] regarding the perception of
machines as moral agents and the consequences for the application of generative AI. The lack of a
thorough and adaptable ethical evaluation framework reveals a significant deficiency in the research.
Current ethical evaluation methods often fall short in standardization and rigor compared to technical
standards, frequently overlooking established assessments like Lind’s Moral Judgment Test [54] and
not giving enough weight to the importance of moral identity as pointed out by Aquino and Reed [4].
2.2
Human Morality and Ethics Literature
Grasping the concepts of human morality and ethics is crucial for analyzing decision-making pro-
cesses, promoting social cohesion, and tackling issues across various disciplines, including psy-
chology, philosophy, and artificial intelligence. A range of research methodologies has emerged to
evaluate morality and ethics, such as psychometric assessments, neuroscientific techniques, qual-
3

--- Page 4 ---

itative research, and digital innovations. These diverse methodologies collectively enhance our
comprehension of moral conduct and ethical decision-making.
Psychometric instruments deliver organized evaluations of moral reasoning and ethical perspectives.
Kohlberg’s Moral Judgment Interview [46] laid the groundwork by focusing on the developmental
stages of moral reasoning with an emphasis on justice-oriented views. Expanding on this, Rest’s
Defining Issues Test [71] offered a standardized method for evaluating post-conventional moral
reasoning via hypothetical scenarios, making moral assessments more accessible and reproducible.
The discipline progressed further with Lind’s Moral Judgment Test [54], which brought in enhanced
metrics for moral competence and the cognitive aspects of moral conduct.
The Moral Foundations Questionnaire, created by Graham and his team [24], has had a profound
impact on the field by identifying five essential moral dimensions: care, fairness, loyalty, authority,
and sanctity. This framework has enabled extensive cross-cultural studies on moral intuitions.
Additionally, Forsyth’s Ethics Position Questionnaire [21] assesses both relativistic and idealistic
ethical perspectives, enabling the exploration of personal and cultural variations in moral convictions.
Moreover, Aquino and Reed [4] have contributed to this discourse by examining the significance of
moral identity, emphasizing the influence of an individual’s moral self-concept on ethical conduct.
Behavioral studies offer essential insights into immediate moral choices. The Trolley Problem,
analyzed by Cushman and others [17], continues to be a pivotal study in ethical dilemmas, examining
the relationship between rational and emotional factors in moral decision-making. The breadth of
these studies has significantly increased, as illustrated by Awad and colleagues [6] in the Moral
Machine project, which collected worldwide data on moral preferences concerning autonomous
vehicles. Bandura and his research team’s [7] exploration of moral disengagement mechanisms has
been particularly vital in comprehending how individuals rationalize unethical actions.
Neuroscientific approaches have greatly enhanced our comprehension of moral cognition. Greene
and colleagues [26] utilized fMRI to show that moral dilemmas activate the ventromedial prefrontal
cortex, highlighting the connection between cognitive processes and emotional responses. This
research has significantly advanced dual-process theories of morality, as described by Haidt [28].
Young and his team [94] furthered this area by applying neurostimulation methods to investigate the
causal relationships between brain areas and moral judgments, while Zak [96] pioneered innovative
hormonal research to examine how oxytocin and testosterone influence moral behavior.
Qualitative methods capture the context-specific and nuanced nature of morality. McAdams’ [59]
work with narrative ethics and life-story interviews allows individuals to reflect on their moral
experiences, providing rich data for understanding ethical perspectives. Ethnographic studies have
highlighted cultural variability in moral reasoning, with Shweder et al. [75] proposing three moral
domains—autonomy, community, and divinity—emphasizing the importance of cultural context.
Nisbett [65] further expanded this understanding by revealing distinct ethical norms and values among
different societies.
Qualitative research methods effectively capture the nuanced and context-dependent aspects of moral-
ity. McAdams’ [59] investigation into narrative ethics and life-story interviews allows individuals to
reflect on their moral experiences, providing valuable insights into ethical perspectives. Ethnographic
studies have uncovered the cultural variations in moral reasoning, with Shweder and his associates
[75] categorizing three moral domains—autonomy, community, and divinity—highlighting the im-
portance of cultural context. Nisbett [65] further broadened this perspective by uncovering unique
ethical norms and values across various societies.
Contemporary technology has revolutionized methods of moral assessment. Navarrete et al. [64] were
pioneers in employing Virtual Reality simulations to examine ethical decision-making in authentic
environments. The incorporation of AI-driven tools has enhanced large-scale data gathering on
moral attitudes and behaviors, as observed by Kim et al. [45]. Paolacci et al. [67] illustrated
the potential of crowdsourcing platforms for research in moral psychology, while also addressing
critical methodological issues. Bryson and Kime [11] have provided important insights into how
technological advancements influence the attribution of moral agency and ethical decision-making.
Despite these advancements, no single method fully encapsulates the intricate nature of morality.
Psychometric instruments are proficient in standardization but frequently overlook implicit moral
processes. Neuroscientific approaches yield comprehensive insights yet are resource-demanding and
limited by artificial environments. Qualitative methods provide depth but are not easily scalable.
4

--- Page 5 ---

Digital innovations are promising but encounter ethical and methodological obstacles. Future
investigations should aim to integrate these diverse methodologies, capitalizing on the strengths of
each to achieve a comprehensive understanding of morality. Cross-cultural research is vital for global
relevance, and emerging technologies such as AI and virtual reality present opportunities for dynamic,
real-world evaluations of ethical reasoning and behavior. The discipline must also respond to the
increasing demand for methods capable of evaluating moral development and ethical decision-making
in ever more complex technological contexts.
Figure 1: The need for integrated research bridging technical evaluation and human morality
3
Customizing Moral Evaluation for LLMs
3.1
Selection and Adaptation of Human Moral Tests
Our framework methodically incorporates three established moral assessment tools, each selected for
their complementary theoretical foundations and methodological robustness. This intentional choice
provides a comprehensive yet efficient method for evaluating moral reasoning in large language
models (LLMs).
The first component employs the Moral Foundations Questionnaire (MFQ-30) [24], a well-validated
instrument that gauges moral intuitions across five fundamental dimensions: care, fairness, loyalty,
authority, and sanctity. The MFQ was selected due to its strong empirical support in moral psychology
and its ability to evaluate various moral foundations that vary among individuals and cultures [28].
Our modification preserves the theoretical structure of the questionnaire while changing the response
format to enable systematic scoring of LLM outputs. By necessitating both numerical ratings
and explanatory reasoning, this adaptation yields insights into how LLMs prioritize various moral
considerations and express ethical judgments.
The World Values Survey (WVS) component was selected for its extensive examination of social,
cultural, and ethical values across a wide range of contexts [41]. The World Values Survey (WVS) is
a comprehensive cross-cultural study of human values, providing a solid framework for evaluating the
consistency of values and the cultural adaptability of large language models (LLMs). Our adaptation
emphasizes key value dimensions that are particularly significant to AI ethics [11], including inquiries
that assess how consistently LLMs adhere to moral principles across different contexts. This focus is
vital for uncovering potential inconsistencies or biases in the ethical reasoning of LLMs [74].
The Moral Dilemma component integrates traditional ethical thought experiments with modern moral
challenges to evaluate the ability of LLMs to handle intricate ethical decisions [17]. Instead of
developing a new instrument for evaluation, our study chose to focus on long-lasting issues that have
been extensively examined in philosophy and psychology [6]. This approach provides benchmark
comparison points with human moral reasoning patterns [26]. Our adaptation organizes these open-
ended scenarios to provoke responses that can be assessed for reasoning sophistication, stakeholder
consideration, consequence analysis, and principled decision-making.
5

--- Page 6 ---

These three elements were deliberately selected to create a complementary evaluation framework: the
MFQ delivers a foundational assessment of basic moral intuitions [24]; the WVS assesses consistency
across cultural and contextual boundaries [41]; and the Moral Dilemmas test examines the application
of ethical reasoning in complex situations [17]. Collectively, they provide a multidimensional
assessment that balances breadth and depth while remaining practically implementable.
The adaptation process for all three instruments adhered to consistent principles: (1) maintaining
the theoretical integrity of the original assessments; (2) standardizing prompt structures to generate
quantifiable responses; (3) creating scoring rubrics that capture both the content and quality of LLM
reasoning [33]; and (4) reducing potential biases that could disproportionately impact certain models
or approaches [73]. This systematic adaptation guarantees that our framework retains psychological
validity while delivering the structured outputs necessary for comparative analysis across various
LLMs [52].
3.2
Technical Implementation and Prompt Engineering
We created a simple approach to apply our moral evaluation system for assessing large language
models (LLMs), striking a balance between methodological rigor with practical implementation [52].
Our method is based on three key principles. First, we converted each evaluation tool into standardized
prompts that maintained the original ethical purpose while providing clear guidance for responses
[101]. For example, we reworded the MFQ questions to reflect the original moral ideas, along
with defined scoring scales (0-5) and a need for reasoning. We applied the same standardization to
WVS items and moral dilemmas, ensuring each was designed to produce both numerical scores and
qualitative explanations [81].
Second, we established a consistent data architecture for organizing assessment items, which included
storing both the original questions and their modified prompts alongside ground truth data from
human studies when available [14]. This organized method enabled the systematic administration
of the assessment battery across various LLM systems while maintaining consistent evaluation
parameters.
Third, we have established a standardized methodology for processing responses that extracts both
numerical scores and reasoning text from outputs generated by large language models (LLMs) [39].
This extraction enables comparative analysis against human benchmarks through established metrics
such as score deviation and reasoning coherence. The system is designed to handle variations in
response formatting across different LLMs while maintaining consistent evaluation metrics [58].
To support multi-model assessments, we created a connector framework that standardizes interactions
with various LLM APIs, allowing for efficient management of the entire assessment process across
different models [100]. This method allows for meaningful comparisons between models by keeping
inputs uniform and taking into account the unique response characteristics of each model.
This technical framework lays the groundwork for a systematic evaluation of moral reasoning capa-
bilities in large language models (LLMs), ensuring that theoretical ethical principles are effectively
translated into practical assessment techniques with the necessary accuracy for comparative analysis
[34].
4
Proposed Methodology for Testing LLM Moral Reasoning
4.1
Experimental Setup
The experimental framework created to evaluate the moral reasoning of large language models aims
to systematically analyze their ethical reasoning capabilities using three complementary assessment
tools. Each tool employs tailored ground truth benchmarks and evaluation techniques that align with
the unique features of its moral domain [100].
For the Moral Foundations Questionnaire (MFQ) [24], our ground truth framework integrates quantita-
tive metrics derived from validated psychological studies, including mean scores, standard deviations,
and consensus values for each moral consideration. This statistical approach acknowledges the
distribution of human moral judgments rather than imposing singular "correct" answers [28]. Each
question includes representative reasoning samples that capture archetypal human justifications. Our
6

--- Page 7 ---

Original Ethical Instruments
Standardized Prompt Format
Structured Data Storage
Response Processing
Multiple LLM Evaluation
Model A
Model B
Model C
Cross-Model Comparison
Moral Reasoning Assessment
Original questions with
scoring scales + reasoning
prompts
Ground truth data, struc-
tured question formats
Score extraction, reasoning
analysis
Metric calculation, perfor-
mance analysis
Figure 2: Technical implementation workflow for moral reasoning assessment in LLMs
evaluation compares LLM numeric ratings against these statistical benchmarks using standard metrics
(MAE, RMSE) [19] while separately assessing reasoning quality through semantic similarity analysis
between LLM justifications and ground truth reasoning exemplars [70]. To quantify alignment with
human moral intuitions, we compute a Moral Foundation Alignment Score for each foundation f,
where nf represents the number of questions in that foundation, SLLM,i is the LLM’s score for
question i, and SGT,i is the human ground truth score:
MFAf = 1 −1
nf
nf
X
i=1
|SLLM,i −SGT,i|
5
(1)
The World Values Survey (WVS) component [41] provides a more extensive set of ground truth
data, encompassing mean scores, standard deviations, and population distributions across various
response options, along with clearly defined acceptable response ranges. This thorough benchmarking
facilitates a detailed assessment of how LLM responses correspond with population-level value
distributions. Furthermore, the fundamental principle guiding WVS investigations includes ’expected
reasoning elements’ that emphasize essential concepts commonly observed in human responses.
Our technical assessment analyzes the consistency with population-level response trends and the
existence of these vital reasoning elements [14], enabling us to pinpoint responses that might achieve
acceptable ratings but lack significant ethical depth.
For Moral Dilemmas, we employ a qualitatively richer ground truth structure based on established
philosophical and psychological analysis of each scenario [6, 17]. Rather than prescribing single
7

--- Page 8 ---

correct answers, the ground truth provides evaluation criteria focusing on reasoning process elements
such as principle identification, stakeholder consideration, and ethical balance [26]. Our technical
approach implements a multi-dimensional rubric that quantifies these qualitative aspects, with inde-
pendent scoring across dimensions like "acknowledges competing values," "considers consequences,"
and "applies consistent principles" [18].
The technical implementation employs several advanced natural language processing techniques.
For extracting and evaluating LLM reasoning, we apply sentence-level embedding models [70] to
compute semantic similarity with ground truth samples, supplemented by pattern-based detection of
specific ethical concepts [33]. We quantify reasoning quality using a composite Reasoning Quality
Index (RQI), where Sim(RLLM, RGT ) represents semantic similarity between LLM and ground truth
reasoning, Pkey is the proportion of expected reasoning elements present, Coh measures internal
coherence, and α, β, γ are calibrated weighting parameters [57]:
RQI = α · Sim(RLLM, RGT ) + β · Pkey + γ · Coh
(2)
Consistency evaluation employs cross-question analysis to identify logical contradictions in a model’s
ethical framework [51]. We measure ethical consistency across related value judgments using an
Ethical Consistency Metric (ECM), where R is the set of conceptually related question pairs, m is
the number of such relationships, Si and Sj are normalized scores for related questions, and Smax is
the maximum possible difference in scores:
ECM = 1 −1
m
X
(i,j)∈R
|Si −Sj|
Smax
(3)
To dilemma resolution, we have created a feature extraction pipeline that identifies specific reasoning
components (such as consequentialist versus deontological approaches and stakeholder identification)
through specialized classification models [20].
Our evaluation framework integrates these components into a unified system that assesses LLM
responses via targeted evaluation modules, standardizes scores for cross-model comparisons, and
generates comprehensive reports detailing performance across various aspects [52]. This method-
ological framework harmonizes quantitative accuracy with qualitative insight, recognizing that the
assessment of moral reasoning necessitates both statistical precision and a sophisticated evaluation of
reasoning intricacies [54].
By integrating meticulously designed ground truth benchmarks with focused technical evaluation
techniques, our framework establishes a robust basis for the comparative analysis of moral reasoning
abilities across various language models, adeptly encompassing both the results and the processes
inherent in ethical decision-making [1]. The benchmark datasets and evaluation codebase are available
at https://github.com/The-Responsible-AI-Initiative/LLM_Ethics_Benchmark.git.
4.2
Implications for Developers and Stakeholders
The outcomes of this assessment have important implications for developers and stakeholders involved
in the development, implementation, and management of large language models (LLMs) [9]. For
developers, these insights highlight the strengths and weaknesses of the model, providing actionable
recommendations for improving training datasets, honing fine-tuning methods, and optimizing prompt
design [83, 84]. For instance, if the model struggles with cross-cultural ethical issues, developers
can work on incorporating a broader range of cultural perspectives into the training datasets [12, 48].
Stakeholders, including policymakers, ethicists, and industry leaders, can utilize these insights
to establish ethical guidelines for the use of LLMs in vital areas such as healthcare, education,
law enforcement, and customer service [23, 85]. Moreover, the evaluation framework provides
a consistent methodology for evaluating large language models (LLMs), promoting transparency
and accountability in the development of artificial intelligence [53]. By tackling deficiencies in
ethical reasoning, developers and stakeholders can construct AI systems that are more reliable and
socially responsible, in harmony with human values and cultural standards [1, 23]. Furthermore,
this framework can function as an auditing instrument for AI systems, guaranteeing adherence to
ethical principles and regulatory obligations [69]. This is especially crucial as LLMs increasingly
8

--- Page 9 ---

shape decision-making processes that profoundly affect society [33]. In conclusion, the evaluation
framework equips developers and stakeholders to design AI systems that are not only technologically
sophisticated but also ethically robust and culturally sensitive [61].
4.3
Challenges and Limitations
Despite the assessment framework’s careful design, there are still a number of significant obstacles
and restrictions [18]. The inherent subjectivity of moral reasoning is a major obstacle [29]. Individual,
cultural, and contextual perspectives commonly impact ethical challenges, resulting in answers that
are typically more complicated than straightforward [35, 75]. This subjectivity can result in incon-
sistencies in the definitions of ground truth and evaluation criteria, complicating the establishment
of universally accepted standards for evaluating the moral reasoning of LLMs [54]. Moreover, the
framework depends on predetermined scenarios and questions, which may not adequately reflect
the complexity and variety of real-world ethical dilemmas [6]. For example, real-world scenarios
frequently present ambiguous data, conflicting values, and dynamic contexts that are difficult to
reproduce in a controlled evaluation [17]. Additionally, a further limitation is the potential for large
language models to generate seemingly reasonable but inaccurate reasoning, which complicates the
assessment of their ethical understanding [8]. This concern is intensified by the fact that LLMs are
trained on extensive datasets that may harbor biases, resulting in outputs that mirror these biases
instead of authentic ethical reasoning [73, 74]. Additionally, the evaluation framework does not
consider the evolving nature of ethical norms, which change over time and differ across cultures,
presenting a challenge for maintaining current and universally applicable evaluation standards [25].
In conclusion, the framework mainly addresses text-centric scenarios, which may inadequately ad-
dress the complexities of multimodal ethical challenges involving visual, auditory, or contextual
elements [16]. These concerns underscore the need for continuous enhancement and adaptation of
the evaluation framework to ensure its ongoing relevance and effectiveness [52].
5
Experimental Results
5.1
Overall Performance across all Dimensions
Our thorough analysis indicates considerable differences in the moral reasoning abilities of the
evaluated LLM systems [52]. Table 1 illustrates the overall performance across our three main
assessment criteria.
Table 1: Overall Performance across Assessment Dimensions (0-100)
Model
MFA Score
Reasoning Index
Value Consistency
Dilemma Resolution
Composite Score
GPT-4o
89.7
92.3
87.6
90.4
90.0
Claude 3.7 Sonnet
91.2
90.8
92.5
88.9
90.9
Deepseek-V3
86.5
89.1
83.7
85.2
86.1
LLaMA 3.1 (70B)
78.3
75.6
72.8
76.4
75.8
Gemini 2.5 Pro
88.2
84.7
86.9
84.5
86.1
The findings reveal that leading models such as Claude [3] and GPT-4 [66] attain the highest overall
scores, with Claude showing exceptional strength in maintaining value consistency, while GPT-4
stands out in terms of reasoning complexity. Importantly, all models exhibit greater competence
in Moral Foundations Alignment (MFA) relative to more intricate aspects like dilemma resolution,
implying that basic moral intuitions may be more effectively integrated during model training than
more sophisticated ethical reasoning [15].
5.2
Performance in Specific Moral Foundations
In order to gain a deeper understanding of model performance, we conducted an analysis of their
alignment with the five moral foundations outlined in Moral Foundations Theory [24].
A distinct trend is evident across all models, showing significantly enhanced performance in the
individualizing foundations (Care and Fairness) when compared to the binding foundations (Loyalty,
Authority, and Sanctity). This disparity reflects patterns found in WEIRD (Western, Educated,
9

--- Page 10 ---

Table 2: Performance across Specific Moral Foundations (0-100)
Model
Care
Fairness
Loyalty
Authority
Sanctity
GPT-4o
94.2
92.8
85.3
83.7
82.5
Claude 3.7 Sonnet
96.1
94.3
87.5
85.2
84.9
Deepseek-V3
92.3
90.7
82.1
79.8
77.3
LLaMA 3.1 (70B)
86.7
84.2
74.6
70.2
68.5
Gemini 2.5 Pro
93.5
91.4
84.8
81.6
80.3
Human Baseline
95.2
93.7
88.4
87.3
86.1
Industrialized, Rich, Democratic) populations [35], implying that these models may embody similar
moral intuitions [29]. Figure 3 illustrates this trend across the various models.
Care
Fairness
Loyalty
Authority
Sanctity
65
70
75
80
85
90
95
100
Moral Foundation
Alignment Score (0-100)
GPT-4
Claude
Deepseek
LLaMA
Gemini
Human
Figure 3: Moral foundation alignment across models compared with human baseline
5.3
Components of Moral Reasoning
Furthermore, we assessed the complexity of moral reasoning processes beyond mere alignment with
human judgments [18]. Our investigation identified four essential elements of ethical deliberation:
principle identification, perspective-taking, consequence analysis, and principle application [46].
Table 3 details model performance in these areas.
Table 3: Performance across Reasoning Components (0-100)
Model
Principle Identification
Perspective-Taking
Consequence Analysis
Principle Application
GPT-4o
94.3
91.7
93.2
90.1
Claude 3.7 Sonnet
92.8
93.5
89.4
87.6
Deepseek-V3
90.2
88.3
91.0
86.9
LLaMA 3.1 (70B)
79.5
74.8
77.2
71.0
Gemini 2.5 Pro
87.6
85.9
84.7
80.5
Our findings indicate that all models exhibit superior abilities in recognizing pertinent moral principles
and analyzing consequences, yet they face challenges in adopting multiple perspectives or consistently
applying principles [20]. This implies that while models can identify ethical considerations, they
encounter difficulties with the integrated reasoning required for intricate moral deliberation [26].
A qualitative examination of model responses reveals that individuals with higher performance levels
demonstrate deeper reasoning, a more nuanced understanding of conflicting values, and a more
10

--- Page 11 ---

consistent application of ethical principles across various situations [84]. The following graph depicts
the distribution of reasoning depth scores in relation to responses to ethical dilemmas.
1
2
3
4
5
0
5
10
15
20
Reasoning Depth Score
Frequency
GPT-4
Claude
Deepseek
LLaMA
Gemini
Figure 4: Distribution of reasoning depth scores in moral dilemma responses
5.4
Consistency and Stability
To evaluate the stability of moral reasoning, we performed several assessment rounds with slight
variations in prompts [98]. Figure 5 displays the consistency scores throughout these evaluation
rounds.
1
1.5
2
2.5
3
3.5
4
4.5
5
70
80
90
100
Evaluation Rounds
Consistency Score (0-100)
GPT-4
Claude
Deepseek
LLaMA
Gemini
Figure 5: Consistency scores across evaluation rounds with prompt variations
Claude exhibits the highest level of consistency, indicating a more stable moral reasoning process
despite changes in question framing [3]. In contrast, LLaMA exhibits a pronounced sensitivity to
variations in prompts, leading to considerable fluctuations in consistency scores across different
rounds [79]. This highlights the essential importance of prompt stability in the context of ethical
reasoning applications [83].
5.5
Correlation between Moral Foundations
To explore the interrelationships among moral foundations in LLM reasoning, we calculated correla-
tion coefficients between the foundation scores [24], as demonstrated in Table 4.
11

--- Page 12 ---

Table 4: Inter-foundation Correlation Matrix (Claude Model)
Foundation
Care
Fairness
Loyalty
Authority
Sanctity
Care
1.00
0.78
0.42
0.31
0.25
Fairness
0.78
1.00
0.39
0.35
0.28
Loyalty
0.42
0.39
1.00
0.72
0.65
Authority
0.31
0.35
0.72
1.00
0.70
Sanctity
0.25
0.28
0.65
0.70
1.00
The correlation matrix reveals notable relationships among the associated foundations: Care and
Fairness exhibit a strong correlation of 0.78, whereas Authority and Sanctity show a correlation of
0.70. This trend corresponds with the theoretical categorization of foundations into individualizing
(Care/Fairness) and binding (Loyalty/Authority/Sanctity) dimensions [29], indicating that LLMs
successfully grasp these essential moral frameworks.
5.6
Specific Failure Modes
Furthermore, our analysis identified several recurring patterns of reasoning errors across various
models [9], as illustrated in Figure 6, which emphasizes the prevalence of different failure modes.
Value Conflicts Cultural BiasesOvergeneralization InconsistencyContext Insensitivity
0
5
10
15
20
25
Failure Modes
Frequency (% of responses)
GPT-4
Claude
Deepseek
LLaMA
Gemini
Figure 6: Frequency of specific failure modes in model responses
Cultural biases are the main failure point seen in many models, highlighting the limitations in
ethical reasoning among different cultures [5]. Claude shows much lower levels of cultural bias and
inconsistency compared to other models [3], while LLaMA has the highest rate of failures in all
categories [79]. The common failure patterns are as follows:
• Value Conflicts: Difficulty handling scenarios with genuinely competing moral values [20]
• Cultural Biases: Western-centric ethical assumptions applied to cross-cultural scenarios
[12]
• Overgeneralization: Applying principles without context-specific nuance [85]
• Inconsistency: Contradictory judgments across conceptually similar scenarios [83]
• Context Insensitivity: Failure to recognize relevant contextual factors in ethical evaluation
[50]
12

--- Page 13 ---

5.7
Comparison with Human Baselines
To assess model performance, we compared MFA scores with human baseline data from established
psychological studies [24]. Figure 7 illustrates the relationship between model evaluations and human
moral intuitions.
GPT-4
Claude
Deepseek
LLaMA
Gemini
70
80
90
100
Model
Alignment with Human Baseline (%)
Overall
Individualizing
Binding
Figure 7: Model alignment with human baseline across foundation types
All models align more closely with human judgments on individualizing foundations (Care/Fairness)
than on binding foundations (Loyalty/Authority/Sanctity) [29, 35]. Claude achieves the highest
overall alignment with human moral intuitions at (91.2%), whereas LLaMA shows the greatest
deviation at (76.3%) [58].
5.8
Contributions
This research introduces notable progress in AI ethics and the development of responsible AI systems:
• Three-Dimensional Evaluation Framework: We have proposed a detailed framework for
evaluating moral reasoning in large language models (LLMs), which encompasses Moral
Foundation Alignment (MFA), Reasoning Quality Index (RQI), and Value Consistency
Assessment (VCA), thus providing a thorough approach for ethical evaluation [18, 52].
• Quantifiable Metrics: Our framework offers quantifiable metrics for assessing the perfor-
mance of LLMs in different facets of moral reasoning, enabling systematic comparisons and
benchmarking across various model architectures and versions [53, 58].
• Standardized Benchmarks: We establish a quantifiable assessment framework by integrat-
ing recognized metrics from moral psychology, including MFQ-30 [24], WVS [41], and
Moral Dilemmas [17]. This provides a reliable approach for researchers and developers to
assess and improve the ethical competencies of large language models (LLMs).
• Open-Source Implementation: We are pleased to announce the launch of an open-source
GitHub repository that features our evaluation framework, data processing pipelines, and
analytical tools. This resource enables researchers and developers to effectively evaluate
their models and actively participate in the advancement of ethical AI [43, 87].
• Insights for Model Development: The findings reveal particular areas needing enhance-
ment, such as improving cross-cultural alignment [12] and resolving inconsistencies in
binding moral foundations [29]. These insights can inform the creation of more resilient
and ethically aligned LLMs [85].
13

--- Page 14 ---

6
Concluding Remarks and Future Directions
The rapid advancement of large language models (LLMs) presents both benefits and challenges in
AI ethics [9]. While these models perform exceptionally well in structured tasks, their ability to
engage in ethical reasoning across diverse and changing scenarios remains constrained [33, 85]. Our
research emphasizes the necessity for ongoing investigation to tackle biases, enhance cross-cultural
understanding, and increase transparency in ethical decision-making [8].
The open-source benchmarking tools we have created aim to make the evaluation of ethics more
accessible and encourage collaborative advancements in this area [87]. By offering standardized
testing methods and metrics, we aspire to create a cohesive framework for comparing different
strategies in ethical AI development [53]. Furthermore, these tools can assist in tracking trends in
the enhancement or decline of ethical reasoning abilities across different model iterations, providing
valuable insights for the AI research community [1].
By integrating diverse training datasets [48], creating explainable AI techniques [72], and encouraging
human-AI collaboration [2], we can forge a path for LLMs that not only achieve high performance
but also adhere to the utmost standards of ethical reasoning and accountability. As these models
become more embedded in crucial decision-making processes, ensuring their alignment with human
values across a range of cultural contexts transforms from a mere technical challenge into an ethical
necessity [23].
Future studies should aim to tackle the challenges and limitations of the existing evaluation framework
to improve its effectiveness and relevance [53]. One promising avenue is the development of adaptive
evaluation methods that take into account real-world situations and evolving ethical standards [72].
This could involve gathering ethical dilemmas from a variety of cultural viewpoints and regularly
updating the evaluation criteria to align with societal shifts [63]. For instance, collaborations with
international organizations and communities could yield a diverse range of culturally important
ethical scenarios, ensuring the evaluation framework is relevant in multiple contexts [5]. Moreover,
improving the incorporation of explainability tools is crucial for comprehending the reasoning
mechanisms of large language models (LLMs) [62]. By analyzing the decision-making processes
of these models, researchers can identify biases, limitations, and inconsistencies in their ethical
reasoning, resulting in more nuanced evaluations of their abilities [72]. By analyzing the decision-
making pathways of these models, researchers can identify biases, limitations, and inconsistencies
in their moral reasoning, resulting in more nuanced evaluations of their capabilities. Additionally,
future research could investigate the use of multimodal datasets, which encompass text, images, and
audio, to assess LLMs in more intricate and realistic scenarios [16, 22]. This methodology would
provide a more comprehensive assessment of the model’s ability to address ethical challenges in
real-world situations [60]. Furthermore, it is essential for AI researchers, ethicists, and policymakers
to collaborate in establishing global standards for the ethical assessment of artificial intelligence [42].
Such partnerships could result in the development of certification programs or regulatory frameworks
that ensure large language models (LLMs) are designed and used in alignment with human values and
societal well-being [86]. Furthermore, conducting longitudinal studies could provide valuable insights
into how moral reasoning in LLMs evolves over time, shedding light on the effects of training data,
fine-tuning, and societal changes on the ethical capabilities of these models [15]. These suggested
strategies will contribute to establishing a more thorough and inclusive evaluation framework [43].
Conflict of Interest
The authors declare no competing interests.
Acknowledgement
This research is funded by the National Science Foundation under grant number 2125858. The
authors would like to express their gratitude for the NSF’s support, which made this study possible.
Furthermore, in accordance with MLA guidelines, we would thank AI applications for assistance in
editing and brainstorming.
14

--- Page 15 ---

References
[1] Dario Amodei, Chris Olah, Jacob Steinhardt, Paul Christiano, John Schulman, and Dan Mané.
Concrete problems in ai safety. arXiv preprint arXiv:1606.06565, 2016.
[2] Jacob Andreas. Language models as agent models. arXiv preprint arXiv:2212.01681, 2022.
[3] Anthropic. Claude: A conversational ai assistant. Anthropic Blog, 2023. URL https:
//www.anthropic.com/index/introducing-claude.
[4] K. Aquino and A. Reed. The self-importance of moral identity. Journal of Personality and
Social Psychology, 83(6):1423–1440, 2002.
[5] Arun Arora, Shane Storks, Hamidreza Nakhost, Jianfu Chen, and Percy Liang. Probing pre-
trained language models for cross-cultural differences in values. Findings of the Association
for Computational Linguistics: EMNLP 2022, pages 3922–3944, 2022.
[6] E. Awad et al. The moral machine experiment. Nature, 563(7729):59–64, 2018.
[7] A. Bandura et al. Mechanisms of moral disengagement. Journal of Personality and Social
Psychology, 71(2):364–374, 1996.
[8] Emily M. Bender, Timnit Gebru, Angelina McMillan-Major, and Shmargaret Shmitchell. On
the dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021
ACM Conference on Fairness, Accountability, and Transparency, pages 610–623, 2021.
[9] Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx,
et al. On the opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258,
2021.
[10] Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared Kaplan, Prafulla
Dhariwal, et al. Language models are few-shot learners. Advances in Neural Information
Processing Systems, 33:1877–1901, 2020.
[11] J. J. Bryson and P. P. Kime. Just an artifact: Why machines are perceived as moral agents.
Artificial Intelligence and Society, 26(3):295–307, 2011.
[12] Aida Cao, Anna Karinshak, Jung Yeon Pak, Chenhao Yang, and Diyi Wu. Cultural alignment
of large language models. arXiv preprint arXiv:2212.10511, 2022.
[13] I. Chalkidis et al. Neural legal judgment prediction in english. In Proceedings of the 57th
Annual Meeting of the Association for Computational Linguistics, pages 4317–4323, 2019.
[14] M. Chen et al. Do llms understand social knowledge? evaluating the sociability of large
language models with socket benchmark. arXiv preprint arXiv:2306.13249, 2023.
[15] Elizabeth Clark, Eric Rosen, Daniel Fried, Dario Amodei, Ben Mann, and Dawn Song. On the
role of reasoning in moral alignment of language models. arXiv preprint arXiv:2302.07459,
2023.
[16] Emily M Coda, Carlos Araujo, Elisa Kreiss, and Christopher Potts. Multimodal-coda: A
dataset for contrastive disambiguation analysis in multimodal reasoning. arXiv preprint
arXiv:2307.01254, 2023.
[17] F. Cushman, L. Young, and M. Hauser. The dynamics of moral judgment. Cognition, 103(3):
393–420, 2006.
[18] Natalie Denny and Alexis Matusiak. Measuring moral reasoning using moral dilemmas:
Evaluating reliability, validity, and differential item functioning of the behavioral defining
issues test. Journal of Moral Education, 50(3):316–337, 2021.
[19] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of
deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805,
2019.
15

--- Page 16 ---

[20] Denis Emelin, Dung Le, Shrimai Bhatt, Yejin Choi, Daniel Khashabi, and Ellie Pavlick.
Moral stories: Situated reasoning about norms, intents, actions, and their consequences. In
Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing,
pages 698–718, 2021.
[21] D. R. Forsyth. A taxonomy of ethical ideologies. Journal of Personality and Social Psychology,
39(1):175–184, 1980.
[22] C. Fu et al. Mme: A comprehensive evaluation benchmark for multimodal large language
models. arXiv preprint arXiv:2306.13394, 2023.
[23] Iason Gabriel. Artificial intelligence, values, and alignment. Minds and Machines, 30:411–437,
2020.
[24] J. Graham et al. Mapping the moral domain. Journal of Personality and Social Psychology,
101(2):366–385, 2011.
[25] Jesse Graham, Jonathan Haidt, Sena Koleva, Matt Motyl, Ravi Iyer, Sean P Wojcik, and
Peter H Ditto. Moral foundations theory: The pragmatic validity of moral pluralism. Advances
in experimental social psychology, 47:55–130, 2013.
[26] J. D. Greene et al. An fmri investigation of emotional engagement in moral judgment. Science,
293(5537):2105–2108, 2001.
[27] Z. Guo et al. Xiezhi: An ever-updating benchmark for holistic domain knowledge evaluation.
arXiv preprint arXiv:2306.05783, 2023.
[28] J. Haidt. The emotional dog and its rational tail: A social intuitionist approach to moral
judgment. Psychological Review, 108(4):814–834, 2001.
[29] Jonathan Haidt. The Righteous Mind: Why Good People are Divided by Politics and Religion.
Vintage, 2012.
[30] D. Hendrycks et al. Measuring coding challenge competence with apps. arXiv preprint
arXiv:2105.09938, 2021.
[31] D. Hendrycks et al. Cuad: An expert-annotated nlp dataset for legal contract review. arXiv
preprint arXiv:2103.06268, 2021.
[32] D. Hendrycks et al. Measuring mathematical problem solving with the math dataset. arXiv
preprint arXiv:2103.03874, 2021.
[33] Dan Hendrycks et al. Ethics of artificial intelligence. arXiv preprint arXiv:2106.08458, 2021.
[34] H. Hendrycks et al. Human-ai moral consistency: Bias recognition dataset, 2023. URL
https://github.com/hendrycks/ethics.
[35] Joseph Henrich, Steven J Heine, and Ara Norenzayan. The weirdest people in the world?
Behavioral and Brain Sciences, 33(2-3):61–83, 2010.
[36] M. J. Hosseini et al. Learning to solve arithmetic word problems with verb categorization. In
Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing,
pages 523–533, 2014.
[37] J. Huang et al. Emotionally numb or empathetic? evaluating how llms feel using emotionbench.
arXiv preprint arXiv:2307.09009, 2023.
[38] Y. Huang et al. C-eval: A multi-level multi-discipline chinese evaluation suite for foundation
models. arXiv preprint arXiv:2305.08322, 2023.
[39] Y. Huang et al. Trustgpt: A benchmark for trustworthy and responsible large language models.
arXiv preprint arXiv:2306.11507, 2023.
[40] HuggingFace. Open-source large language models leaderboard, 2023. URL https://
huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard.
16

--- Page 17 ---

[41] Ronald Inglehart, Miguel Basañez, and Alejandro Moreno. World Values Surveys and European
Values Surveys, 1981-1984, 1990-1993, and 1995-1997. Inter-university Consortium for
Political and Social Research, 2000.
[42] Anna Jobin, Marcello Ienca, and Effy Vayena. The global landscape of ai ethics guidelines.
Nature Machine Intelligence, 1(9):389–399, 2019.
[43] Richard Johnson, Daniel Romano, Rose Wang, and Sofia Valverde. Ethics-eval: A bench-
marking framework for ethical evaluation of language models, 2023. URL https://github.
com/AI-secure/ethics-eval.
[44] D. Kiela et al. Dynabench: Rethinking benchmarking in nlp. arXiv preprint arXiv:2104.14337,
2021.
[45] T. W. Kim, J. Hooker, and T. Donaldson. The ethics of ai-driven decision-making. AI \&
Society, 36(2):1–15, 2021.
[46] L. Kohlberg. The Philosophy of Moral Development: Moral stages and the idea of justice.
Harper \& Row, 1981.
[47] R. Koncel-Kedziorski et al. Parsing algebraic word problems into equations. Transactions of
the Association for Computational Linguistics, 3:585–597, 2015.
[48] Stephanie Hanes Larson. Gender, race, and intersectionality on the federal appellate bench.
Washington University Law Review, 97(5):1–42, 2017.
[49] B. Li et al. Seed-bench: Benchmarking multimodal llms with generative comprehension. arXiv
preprint arXiv:2307.16125, 2023.
[50] Nan Li, Zhi Wang, Shuangfei Zhu, Tatyana Sharpee, Yingzhen Li, and Amy Zhang. Systematic
evaluation of causal discovery in visual model based reinforcement learning. arXiv preprint
arXiv:2203.12188, 2022.
[51] Ningyu Li, Zhuang Gao, Han Xiao, Shumin Huang, Xiang Xie, Jiaoyan Zhu, Yiyi Li, Yunzhi
Xiao, and Huajun Chen. Logic-guided semantic representation learning for zero-shot rela-
tion classification. In Proceedings of the 28th International Conference on Computational
Linguistics, pages 2967–2978, 2019.
[52] P. Liang et al. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110, 2022.
[53] Percy Liang, Rishi Bommasani, Tony Lee, Dimitris Tsipras, Dilara Soylu, Michihiro Yasunaga,
Yian Zhang, Deepak Narayanan, Yuhuai Wu, Ananya Kumar, et al. Holistic evaluation of
language models. arXiv preprint arXiv:2211.09110, 2022.
[54] G. Lind. The moral judgment test (mjt): Thirty years of research. Educational Research and
Evaluation, 6(1):1–20, 2000.
[55] W. Ling et al. Program induction by rationale generation: Learning to solve and explain
algebraic word problems. In Proceedings of the 55th Annual Meeting of the Association for
Computational Linguistics, pages 158–167, 2017.
[56] L. Liu et al. Mmbench: Is your multi-modal model an all-around player? arXiv preprint
arXiv:2307.06281, 2023.
[57] Xiaodong Liu, Pengcheng He, Weizhu Chen, and Jianfeng Gao. Multi-task deep neural
networks for natural language understanding. In Proceedings of the 57th Annual Meeting of
the Association for Computational Linguistics, pages 4487–4496, 2019.
[58] LMSYS. Chatbot arena: Benchmarking llms in the wild with elo ratings, 2023. URL
https://lmsys.org.
[59] D. P. McAdams. The Stories We Live By: Personal myths and the making of the self. Guilford
Press, 1993.
17

--- Page 18 ---

[60] Shira Mitchell, Eric Potash, Solon Barocas, Alexander D’Amour, and Kristian Lum. Algo-
rithmic fairness: Choices, assumptions, and definitions. Annual Review of Statistics and Its
Application, 9:359–380, 2022.
[61] Brent Mittelstadt. Principles alone cannot guarantee ethical ai. Nature Machine Intelligence, 1
(11):501–507, 2019.
[62] Christoph Molnar. Interpretable machine learning. Lulu. com, 2022.
[63] Arvind Narayanan. Translation tutorial: 21 fairness definitions and their politics. Proc. Conf.
Fairness Accountability Transp., New York, USA, 1170, 2018.
[64] C. D. Navarrete et al. Virtual morality: Emotion and action in a simulated three-dimensional
"trolley problem". Social Neuroscience, 7(4):364–374, 2012.
[65] R. E. Nisbett. The Geography of Thought: How Asians and Westerners think differently... and
why. Free Press, 2003.
[66] OpenAI. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.
[67] G. Paolacci, J. Chandler, and P. G. Ipeirotis. Running experiments on amazon mechanical turk.
Judgment and Decision Making, 5(5):411–419, 2010.
[68] Jack W. Rae et al. Scaling language models: Methods, analysis \& insights from training
gopher. arXiv preprint arXiv:2112.11446, 2021.
[69] Inioluwa Deborah Raji, Andrew Smart, Rebecca N White, Margaret Mitchell, Timnit Gebru,
Ben Hutchinson, Jamila Smith-Loud, Daniel Theron, and Parker Barnes. Closing the ai
accountability gap: Defining an end-to-end framework for internal algorithmic auditing.
Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency, pages
33–44, 2020.
[70] Nils Reimers and Iryna Gurevych. Sentence-bert: Sentence embeddings using siamese bert-
networks. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language
Processing, pages 3982–3992, 2019.
[71] J. R. Rest. Development in Judging Moral Issues. University of Minnesota Press, 1979.
[72] Marco Tulio Ribeiro, Tongshuang Wu, Carlos Guestrin, and Sameer Singh. Adaptive testing
and debugging of nlp models. In Proceedings of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), pages 3253–3267, 2022.
[73] R. Rudinger et al. Gender bias in coreference resolution. In Proceedings of the 2018 Conference
of the North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, pages 8–14, 2018.
[74] M. Sap et al. Social bias frames: Reasoning about social and power implications of language.
In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics,
pages 5477–5490, 2020.
[75] R. A. Shweder et al. The "big three" of morality (autonomy, community, divinity) and the big
three explanations of suffering. Morality and Health, pages 119–169, 1997.
[76] S. Singhal et al. Large language models encode clinical knowledge. Nature, 620(7972):1–10,
2023.
[77] ToolBench. Open-source tools learning benchmarks, 2023. URL https://github.com/
sambanova/toolbench.
[78] Eric J Topol. High-performance medicine: the convergence of human and artificial intelligence.
Nature Medicine, 25(1):44–56, 2019.
[79] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Tim-
othée Lacroix, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint
arXiv:2307.09288, 2023.
18

--- Page 19 ---

[80] V. Varshney et al. Freshllms: Refreshing large language models with search engine augmenta-
tion. arXiv preprint arXiv:2306.06598, 2023.
[81] W. Wang et al. Chain-of-thought prompting for responding to in-depth dialogue questions
with llm. arXiv preprint arXiv:2307.05082, 2023.
[82] X. Wang et al. Cmb: A comprehensive medical benchmark in chinese. arXiv preprint
arXiv:2307.06975, 2023.
[83] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, and Denny Zhou. Self-
consistency improves chain of thought reasoning in language models.
arXiv preprint
arXiv:2203.11171, 2022.
[84] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed Zhao,
et al. Chain of thought prompting elicits reasoning in large language models. arXiv preprint
arXiv:2201.11903, 2022.
[85] Laura Weidinger, John Mellor, Maribeth Rauh, Conor Griffin, Jonathan Uesato, Po-Sen Huang,
et al. Taxonomy of risks posed by language models. Proceedings of the 2022 ACM Conference
on Fairness, Accountability, and Transparency, pages 214–229, 2022.
[86] Jess Whittlestone, Rune Nyrup, Anna Alexandrova, Kanta Dihal, and Stephen Cave. The role
and limits of principles in ai ethics: towards a focus on tensions. Proceedings of the 2019
AAAI/ACM Conference on AI, Ethics, and Society, pages 195–200, 2021.
[87] Thomas Wolf, Lysandre Debut, Victor Sanh, Julien Chaumond, Clement Delangue, Anthony
Moi, Pierric Cistac, Tim Rault, Rémi Louf, Morgan Funtowicz, et al. Transformers: State-
of-the-art natural language processing. Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing: System Demonstrations, pages 38–45, 2020.
[88] X. Xu et al. Cvalues: Measuring the values of chinese large language models from safety to
responsibility. arXiv preprint arXiv:2307.09705, 2023.
[89] X. Xu et al. Lvlm-ehub: A comprehensive evaluation benchmark for large vision-language
models. arXiv preprint arXiv:2306.09265, 2023.
[90] Y. Yang et al. Glue-x: Evaluating natural language understanding models from an out-of-
distribution generalization perspective. arXiv preprint arXiv:2211.08073, 2022.
[91] Y. Yang et al. Gaokao-bench: Revisiting out-of-distribution robustness in nlp. arXiv preprint
arXiv:2306.14824, 2023.
[92] Y. Yang et al. Lamm: Language-assisted multi-modal instruction-tuning dataset, framework,
and benchmark. arXiv preprint arXiv:2306.06687, 2023.
[93] Y. Yang et al. Mm-vet: Evaluating large multimodal models for integrated capabilities. arXiv
preprint arXiv:2308.02490, 2023.
[94] L. Young et al. Disruption of the right temporoparietal junction with transcranial magnetic
stimulation reduces the role of beliefs in moral judgments. Proceedings of the National
Academy of Sciences, 107(15):6753–6758, 2010.
[95] J. Yu et al. Kola: Carefully benchmarking world knowledge of large language models. arXiv
preprint arXiv:2306.09296, 2023.
[96] P. J. Zak. The neurobiology of trust. Scientific American, 298(6):88–95, 2008.
[97] Z. Zhang et al. M3exam: A multilingual, multimodal, multilevel benchmark for examining
large language models. arXiv preprint arXiv:2306.05179, 2023.
[98] Tony Zhao, Eric Wallace, Shi Feng, Dan Klein, and Sameer Singh. Calibrate before use:
Improving few-shot performance of language models. arXiv preprint arXiv:2102.09690, 2021.
[99] Z. Zheng et al. Safetybench: Evaluating the safety of large language models with multiple
choice questions. arXiv preprint arXiv:2305.13656, 2023.
19

--- Page 20 ---

[100] Z. Zhong et al. Agieval: A human-centric benchmark for evaluating foundation models. arXiv
preprint arXiv:2304.06364, 2023.
[101] Z. Zhu et al. Promptbench: Towards evaluating the robustness of large language models on
adversarial prompts. arXiv preprint arXiv:2306.04528, 2023.
20

```
