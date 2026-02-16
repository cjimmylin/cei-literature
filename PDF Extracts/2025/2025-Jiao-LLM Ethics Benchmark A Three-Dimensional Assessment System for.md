---
title: "2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for - PDF Extract"
source_pdf: "2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for.pdf"
pages: 13
extracted_at: "2026-02-15T18:01:04.023608"
---

# PDF Extract: 2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for

**Source PDF:** 2025-Jiao-LLM Ethics Benchmark A Three-Dimensional Assessment System for.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

LLM ethics benchmark: a three-
dimensional assessment system for 
evaluating moral reasoning in large 
language models
Junfeng Jiao1, Saleh Afroogh1, Abhejay Murali2, Kevin Chen1, David Atkinson3 & 
Amit Dhurandhar4
This study establishes a novel framework for systematically evaluating the moral reasoning capabilities 
of large language models (LLMs) as they increasingly integrate into critical societal domains. Current 
assessment methodologies lack the precision needed to evaluate nuanced ethical decision-making 
in AI systems, creating significant accountability gaps. Our framework addresses this challenge by 
quantifying alignment with human ethical standards through three dimensions: foundational moral 
principles, reasoning robustness, and value consistency across diverse scenarios. This approach enables 
precise identification of ethical strengths and weaknesses in LLMs, facilitating targeted improvements 
and stronger alignment with societal values. To promote transparency and collaborative advancement 
in ethical AI development, we are publicly releasing both our benchmark datasets and evaluation 
codebase at ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​T​h​e​-​R​e​s​p​o​n​s​i​b​l​e​-​A​I​-​I​n​i​t​i​a​t​i​v​e​/​L​L​M​_​E​t​h​i​c​s​_​B​e​n​c​h​m​a​r​k​.​g​i​t.
Keywords  LLM, Moral reasoning, AI alignment, Benchmark datasets, Responsible AI
The growth of artificial intelligence systems with sophisticated reasoning abilities has introduced remarkable 
opportunities and challenges for human society. As Large Language Models (LLMs) evolve from simple text 
generation tools into complex reasoning systems, they are more often confronted with situations that require 
moral judgment and ethical decision-making1–3.
Human morality has been a focal point of extensive research within psychology, philosophy, and anthropology, 
exposing the intricate cognitive processes that drive ethical decision-making. Decades of investigation have 
shown that moral reasoning consists of various dimensions: identifying ethical dilemmas, balancing conflicting 
values, considering a range of stakeholder perspectives, and rationalizing decisions through consistent moral 
frameworks4,5. However, the rise of AI systems capable of engaging in moral discussions poses a unique 
challenge: reconciling the established knowledge of human moral psychology with the evaluative demands of 
artificial intelligence systems that process and generate moral reasoning in fundamentally different ways6,7.
Research gap
Given the increasing significance of large language models (LLMs) in decision-making, a substantial gap exists 
in the methods for evaluating their moral reasoning capabilities8. Present assessment methods are marked by 
inconsistency, rely on overly simplistic scenarios, and fail to adequately consider the complex, interconnected 
aspects of moral decision-making9. Current frameworks do not sufficiently tackle the unique traits of LLMs, 
such as their stochastic nature and their exposure to a diverse array of human-generated content. Although 
established tools exist for human moral assessment, they cannot be directly applied to LLMs without considerable 
modifications. This study aims to tackle these challenges by developing a three-dimensional framework that 
adapts established moral psychology instruments to create measurable metrics for the ethical assessment of 
LLMs.
1Urban Information Lab, The University of Texas at Austin, Austin, USA. 2Department of Computer Science, The 
University of Texas at Austin, Austin, USA. 3McCombs School of Business, The University of Texas at Austin, Austin, 
USA. 4IBM Research, Yorktown Heights, USA. email: saleh.afroogh@utexas.edu
OPEN
Scientific Reports |        (2025) 15:34642 
1
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports

--- Page 2 ---

Background: current approaches and foundations
This section examines current AI evaluation methods and their limitations, reviews established frameworks 
from human moral psychology, and explores how to adapt these approaches for assessing moral reasoning in 
AI systems.
AI evaluation techniques: current state and limitations
Large language models (LLMs) like ChatGPT and Claude have revealed remarkable capabilities and are being 
progressively adopted in critical areas such as healthcare, education, legal services, and financial decision-
making. As these systems assume more significant roles in society, the necessity for comprehensive evaluation 
frameworks has become apparent. At present, evaluation approaches are categorized into three primary types: 
assessment of technical performance, evaluation of specialized tasks, and safety considerations.
Technical performance evaluations evaluate essential language capabilities by employing standardized test 
suites. For example, GLUE (General Language Understanding Evaluation) measures reading comprehension 
and basic reasoning10, while HELM (Holistic Evaluation of Language Models) provides a broader evaluation 
across multiple language tasks11. These benchmarks assess the ability of models to understand and generate 
language accurately in a variety of contexts.
Specialized evaluations analyze performance in specific professional domains. Mathematical reasoning is 
evaluated through frameworks like MATH12, programming skills through APPS (Automated Programming 
Progress Standard)13, and medical knowledge through MultiMedQA (Multi-Medical Question Answering)14. 
These tests specific to each domain determine if LLMs can function reliably in professional settings where 
accuracy and expertise are vital.
Safety-oriented assessments have surfaced with systems like TrustGPT15 and SafetyBench16 established 
to detect harmful outputs, which encompass bias, toxicity, and misinformation. However, these strategies 
predominantly emphasize the identification of problematic content rather than the evaluation of the quality and 
consistency of ethical reasoning processes. This limitation becomes important as LLMs are increasingly utilized 
in contexts that require nuanced moral judgment, such as offering guidance on ethical dilemmas or making 
decisions that affect human welfare.
The key issue in modern AI evaluation is the absence of structured approaches to evaluate moral reasoning 
skills6,7. Although current safety frameworks can detect when a model generates overtly harmful content15,16, they 
fall short in assessing whether a model exhibits advanced ethical reasoning, upholds consistent moral principles, 
or adeptly navigates conflicting moral dilemmas. This deficiency is critical, as moral reasoning encompasses 
intricate cognitive processes that go well beyond the mere categorization of content as “harmful” or “safe”5,17.
Foundations of human moral assessment
The field of human moral psychology has produced a variety of strategies for understanding ethical decision-
making, encompassing both philosophical frameworks and empirical measurement tools18,19. These strategies 
are generally classified into categories that explore moral intuitions, cultural value systems, and decision-making 
processes amid ethical conflicts. To formulate an effective moral assessment for AI systems, we anchor our 
approach in three established frameworks that collectively represent the core aspects of human moral reasoning.
Moral foundations theory serves as a coherent model for grasping the essential elements of moral cognition. 
Developed by psychologists Graham, Haidt, and their colleagues4, this theory highlights five universal moral 
concerns observable across cultures: Care (defending others from harm), Fairness (ensuring justice and equal 
treatment), Loyalty (promoting group solidarity and commitment), Authority (respecting legitimate leadership 
and hierarchy), and Sanctity (preserving purity and avoiding degradation). Various individuals and cultures 
prioritize these foundations differently, which clarifies the reasons for moral disagreements5,20. The theory is 
implemented through the Moral Foundations Questionnaire (MFQ), which offers scenarios and statements 
aimed at activating each foundation, thereby enabling researchers to chart an individual’s moral priorities4. The 
MFQ’s validation across a range of cultures and languages enhances its significance for assessing AI systems 
designed for worldwide application21.
Cross-cultural value assessment highlights the differences in moral reasoning that can be found among various 
societies and cultural contexts. The World Values Survey (WVS) is acknowledged as the most comprehensive 
long-term study of human values and beliefs, collecting data from a wide array of countries over several 
decades22. This research has pinpointed significant dimensions of cultural diversity that affect moral reasoning, 
such as perspectives on individual versus collective responsibility, respect for authority, and the influence of 
tradition on behavior23. For the evaluation of AI, the WVS holds particular significance as it reveals that moral 
reasoning is not a universal concept—what may appear evidently correct in one culture could be challenged or 
dismissed in another24. This cross-cultural viewpoint is crucial for the creation of AI systems that can function 
respectfully within varied cultural contexts, rather than enforcing a singular moral paradigm.
Moral dilemma research investigates the ways individuals confront challenging ethical choices when moral 
values clash. Traditional examples, such as the Trolley Problem—where one faces the decision of permitting 
five individuals to perish or actively causing the death of one person to save the others—have been extensively 
utilized to explore the psychological mechanisms that inform moral judgment17. This research demonstrates that 
moral decision-making entails complex interactions between emotional responses, reasoning about intentions 
versus outcomes, and cultural context25. Modern studies, like the Moral Machine experiment, have expanded 
this inquiry to contemporary ethical issues, gathering international data on moral preferences concerning 
autonomous vehicle decisions in unavoidable accident scenarios26. These studies provide standardized 
methodologies for assessing ethical reasoning to reveal patterns in how humans approach moral dilemmas19.
Together, these three frameworks offer complementary perspectives on moral reasoning: Moral Foundations 
Theory maps the basic moral concerns that guide judgment, cross-cultural research reveals how these concerns 
Scientific Reports |        (2025) 15:34642 
2
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 3 ---

vary across contexts, and moral dilemma studies examine how people apply moral principles when they conflict. 
This combination provides a comprehensive foundation for evaluating the moral reasoning capabilities of AI 
systems.
Defining and assessing moral reasoning in AI
What do we specifically mean by “moral reasoning”? Within psychological research, moral reasoning is defined 
as the cognitive processes that empower individuals to discern ethical dilemmas, evaluate multiple viewpoints 
and stakeholders, apply moral principles to particular scenarios, and substantiate their ethical decisions18. 
This multifaceted process includes several critical components: identifying when a situation possesses moral 
relevance, grasping the competing values and principles at play, analyzing the outcomes of various actions for 
different stakeholders, and delivering a coherent justification for ethical choices19.
Current AI evaluation techniques face challenges in evaluating these advanced reasoning processes. Unlike 
technical skills that can be quantified through basic accuracy metrics, moral reasoning demands assessment 
methods that can reflect subtle cognitive processes and cultural diversity in ethical reasoning. Our investigation 
confronts this challenge by systematically adapting three established instruments from moral psychology 
research—the Moral Foundations Questionnaire, parts of the World Values Survey, and standardized moral 
dilemmas—to develop a comprehensive framework for evaluating moral reasoning in large language models.
Customizing moral evaluation for LLMs
Evaluating LLM moral reasoning requires adapting established psychological instruments while preserving 
their theoretical validity. This section details our modifications to three foundational assessment tools and their 
technical implementation framework.
Adaptation of moral psychology instruments for LLM evaluation
Building upon the three frameworks detailed in “Foundations of human moral assessment”, we systematically 
modified each instrument to allow for a comprehensive evaluation of LLMs, ensuring that their theoretical 
integrity and psychological validity are preserved.
MFQ adaptation: we altered the original MFQ-30 format4 to require both numerical ratings (on a 0–5 scale) 
and written justifications for each moral judgment. This dual-response strategy permits us to evaluate not just 
how LLMs prioritize different moral foundations, but also the quality and consistency of their ethical reasoning. 
We standardized the prompts to maintain the original moral content while guaranteeing clear response 
formatting across diverse LLM architectures27.
WVS adaptation: our approach prioritizes the key value dimensions that are especially applicable to AI 
ethics, particularly those that evaluate the alignment of moral principles across diverse cultural and contextual 
frameworks22. We understand that despite the WVS presenting a rich array of cross-cultural data, it has its 
shortcomings related to cultural relevance and the risk of Western bias in its conceptual frameworks23. To 
counter this, we emphasize patterns of consistency over fixed moral standards, employing the WVS chiefly to 
reveal internal inconsistencies in LLM value systems rather than to issue prescriptive moral judgments.
Moral dilemma adaptation: we arranged classic and contemporary ethical scenarios17,26 to generate responses 
that can be systematically analyzed across several dimensions: the sophistication of reasoning, stakeholder 
consideration, consequence evaluation, and principled decision-making. Rather than aiming for a single ’correct’ 
answer, our scoring methodology assesses the quality of ethical reasoning processes, allowing for various valid 
approaches while differentiating between sophisticated and superficial moral analysis.
The adaptation process was based on four consistent principles for all instruments: (1) upholding the 
theoretical integrity of the original assessments; (2) standardizing the structures of prompts to produce 
quantifiable responses11; (3) establishing scoring rubrics that evaluate both the accuracy of content and the quality 
of reasoning28; and (4) mitigating potential biases that could unfairly favor particular models or approaches29.
Validation methodology: a dual-method validation framework was employed to ensure both theoretical 
accuracy and methodological reliability. Initially, a specialist in philosophical ethics systematically reviewed 
all modifications to guarantee theoretical integrity and the precise translation of moral concepts from human 
assessments to LLM frameworks. This expert validation confirmed that our automated scoring criteria effectively 
capture the philosophical foundations of each tool and suitably differentiate between advanced and basic moral 
reasoning.
Second, we confirmed the efficacy of our automated scoring system by aligning it directly with established 
benchmarks derived from decades of research in moral psychology4,5. For the Moral Foundations Questionnaire 
(MFQ), we validated our findings against statistical benchmarks obtained from extensive human studies, 
which included mean scores, standard deviations, and consensus values across various moral foundations4. The 
validation for the World Values Survey (WVS) utilized population-level response distributions and recognized 
classifications of value dimensions from cross-cultural research22. The assessment of Moral Dilemmas was 
confirmed through established philosophical and psychological criteria for ethical reasoning quality, integrating 
frameworks derived from seminal studies in moral decision-making17,19. This methodology successfully tackles 
inter-rater reliability issues by connecting automated evaluations to validated psychological and philosophical 
benchmarks, instead of relying on subjective human assessments, thus guaranteeing a uniform and theoretically 
robust evaluation across all analyzed models.
Technical implementation and prompt engineering
We created a simple approach to apply our moral evaluation system for assessing large language models (LLMs), 
striking a balance between methodological rigor with practical implementation (see Fig. 1)11.
Scientific Reports |        (2025) 15:34642 
3
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 4 ---

Our method is based on three key principles. First, we converted each evaluation tool into standardized 
prompts that maintained the original ethical purpose while providing clear guidance for responses27. For 
example, we reworded the MFQ questions to reflect the original moral ideas, along with defined scoring scales 
(0–5) and a need for reasoning. We applied the same standardization to WVS items and moral dilemmas, 
ensuring each was designed to produce both numerical scores and qualitative explanations30.
Second, we established a consistent data architecture for organizing assessment items, which included storing 
both the original questions and their modified prompts alongside ground truth data from human studies when 
available31. This organized method enabled the systematic administration of the assessment battery across 
various LLM systems while maintaining consistent evaluation parameters.
Third, we have established a standardized methodology for processing responses that extracts both numerical 
scores and reasoning text from outputs generated by large language models (LLMs)15. This extraction enables 
comparative analysis against human benchmarks through established metrics such as score deviation and 
reasoning coherence. The system is designed to handle variations in response formatting across different LLMs 
while maintaining consistent evaluation metrics32.
To support multi-model assessments, we created a connector framework that standardizes interactions with 
various LLM APIs, allowing for efficient management of the entire assessment process across different models33. 
This method allows for meaningful comparisons between models by keeping inputs uniform and taking into 
account the unique response characteristics of each model.
This technical framework lays the groundwork for a systematic evaluation of moral reasoning capabilities 
in large language models (LLMs), ensuring that theoretical ethical principles are effectively translated into 
assessment techniques with the necessary accuracy for comparative analysis34.
Proposed methodology for testing LLM moral reasoning
This section presents a comprehensive experimental framework for evaluating the moral reasoning capabilities 
of large language models through three complementary assessment tools. We first detail the experimental setup 
and evaluation metrics, then discuss the broader implications, challenges, and limitations of this methodology.
Experimental setup
The experimental framework created to evaluate the moral reasoning of large language models aims to 
systematically analyze their ethical reasoning capabilities using three complementary assessment tools. Each 
tool employs tailored ground truth benchmarks and evaluation techniques that align with the unique features 
of its moral domain33.
All ground truth establishment processes were validated through expert review by our domain specialists in 
philosophical and AI ethics to ensure theoretical integrity and methodological soundness.
For the Moral Foundations Questionnaire (MFQ)4, our ground truth framework integrates quantitative 
metrics derived from validated psychological studies, including mean scores, standard deviations, and consensus 
values for each moral consideration (see Fig.  2). This statistical approach acknowledges the distribution of 
human moral judgments rather than imposing singular “correct” answers20. The reasoning samples that 
represent each moral foundation were extracted from the established framework of Moral Foundations Theory 
and sourced from literature in moral psychology4,20. In accordance with the theoretical structure of each moral 
foundation (care, fairness, loyalty, authority, sanctity), we pinpointed 3–5 archetypal justification patterns that 
illustrate fundamental reasoning within each domain, chosen for their theoretical consistency and documented 
prevalence in empirical research. Our evaluation compares LLM numeric ratings against these statistical 
benchmarks using standard metrics (MAE, RMSE)35 while separately assessing reasoning quality through 
semantic similarity analysis between LLM justifications and ground truth reasoning exemplars36. To quantify 
alignment with human moral intuitions, we compute a Moral Foundation Alignment Score for each foundation 
f, where nf represents the number of questions in that foundation, SLLM,i is the LLM’s score for question i, and 
SGT,i is the human ground truth score:
	
MFAf = 1 −1
nf
nf
∑
i=1
|SLLM,i −SGT,i|
5

(1)
The World Values Survey (WVS) component22 provides a more extensive set of ground truth data, encompassing 
mean scores, standard deviations, and population distributions across various response options, along with 
clearly defined acceptable response ranges. This thorough benchmarking facilitates a detailed assessment of 
how LLM responses correspond with population-level value distributions. The ’expected reasoning elements’ 
were developed in accordance with the validated theoretical framework provided by the World Values Survey 
Original
Instruments
Standardized
Prompts
Data
Storage
Response
Processing
Cross-Model
Comparison
Assessment
Results
Model A
Model B
Model C
Fig. 1.  Technical implementation workflow for moral reasoning assessment in LLMs.
 
Scientific Reports |        (2025) 15:34642 
4
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 5 ---

for the evaluation of cross-cultural values22, systematically identifying essential concepts that align with the 
WVS value dimensions and are consistently observed in documented human response patterns across different 
cultural contexts. Our technical assessment analyzes the consistency with population-level response trends and 
the existence of these vital reasoning elements31, enabling us to pinpoint responses that might achieve acceptable 
ratings but lack significant ethical depth.
For Moral Dilemmas, we employ a qualitatively richer ground truth structure based on established 
philosophical and psychological analysis of each scenario17,26. Rather than prescribing single correct answers, the 
ground truth provides evaluation criteria focusing on reasoning process elements such as principle identification, 
stakeholder consideration, and ethical balance25. The criteria for evaluating ground truth were formulated by 
adhering to recognized philosophical frameworks for assessing moral reasoning17,25. This involved a systematic 
application of canonical ethical frameworks, including deontological, consequentialist, and virtue ethics, 
while also integrating empirically documented reasoning patterns found in the literature of moral psychology. 
Our technical approach implements a multi-dimensional rubric that quantifies these qualitative aspects, with 
independent scoring across dimensions like “acknowledges competing values,” “considers consequences,” and 
“applies consistent principles”28.
The technical implementation employs several advanced natural language processing techniques. For 
extracting and evaluating LLM reasoning, we apply sentence-level embedding models36 to compute semantic 
similarity with ground truth samples, supplemented by pattern-based detection of specific ethical concepts7. 
We quantify reasoning quality using a composite Reasoning Quality Index (RQI), where Sim(RLLM, RGT ) 
represents semantic similarity between LLM and ground truth reasoning, Pkey is the proportion of expected 
reasoning elements present, Coh measures internal coherence, and α, β, γ are calibrated weighting parameters37:
	
RQI = α · Sim(RLLM, RGT ) + β · Pkey + γ · Coh
(2)
We apply equal weighting across all questions within each moral foundation, in line with the original MFQ 
validation methodology, which stipulates that individual items contribute equally to foundation scores4. This 
method maintains the psychometric properties of the validated instrument.
The weighting parameters α = 0.4, β = 0.4, and γ = 0.2 were established through alignment with 
recognized moral psychology benchmarks outlined in “Adaptation of moral psychology instruments for LLM 
evaluation”. The equal weighting of semantic similarity (α) and fundamental reasoning components (β) indicates 
that both content accuracy and reasoning thoroughness are critical for moral evaluation. Simultaneously, the 
reduced coherence weight (γ) ensures that linguistic fluency does not overshadow meaningful ethical reasoning. 
The precise parameter values were meticulously refined through a systematic iterative process concerning 
the validation benchmarks, thus enhancing their alignment with recognized standards in moral psychology. 
Alternative calibration approaches could include machine learning optimization or expert consensus weighting, 
though our benchmark-driven approach ensures consistency with decades of validated moral psychology 
research rather than subjective preferences.
Consistency evaluation employs cross-question analysis to identify logical contradictions in a model’s ethical 
framework38. We measure ethical consistency across related value judgments using an Ethical Consistency 
Metric (ECM), where R is the set of conceptually related question pairs, m is the number of such relationships, 
Si and Sj are normalized scores for related questions, and Smax is the maximum possible difference in scores:
	
ECM = 1 −1
m
∑
(i,j)∈R
|Si −Sj|
Smax

(3)
To dilemma resolution, we have created a feature extraction pipeline that identifies specific reasoning components 
(such as consequentialist versus deontological approaches and stakeholder identification) through specialized 
classification models39.
Fig. 2.  Moral foundation alignment across models compared with human baseline.
 
Scientific Reports |        (2025) 15:34642 
5
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 6 ---

Our evaluation framework integrates these components into a unified system that assesses LLM responses 
via targeted evaluation modules, standardizes scores for cross-model comparisons, and generates comprehensive 
reports detailing performance across various aspects11. This methodological framework harmonizes quantitative 
accuracy with qualitative insight, recognizing that the assessment of moral reasoning necessitates both statistical 
precision and a sophisticated evaluation of reasoning intricacies40.
By integrating meticulously designed ground truth benchmarks with focused technical evaluation techniques, 
our framework establishes a robust basis for the comparative analysis of moral reasoning abilities across various 
language models, adeptly encompassing both the results and the processes inherent in ethical decision-making8. 
The benchmark datasets and evaluation codebase are available at ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​T​h ​e​-​R​e​s​p​o​n​s​i​b​l​e​-​A​I​-​I​n​i​t​i​a​
t​i​v​e​/​L​L​M​_​E​t​h​i​c​s​_​B​e​n​c​h​m​a​r​k​.​g​i​t.
Implications, challenges, and limitations
This assessment framework holds significant implications for developers and stakeholders engaged in the 
development and deployment of LLMs2. Our findings provide developers with actionable recommendations 
to enhance training datasets, fine-tuning methods, and prompt design41,42. For instance, models that encounter 
difficulties with cross-cultural ethics could benefit from the inclusion of a wider range of cultural perspectives 
in their training data43,44. However, it is important for developers to recognize that our WVS-based cultural 
assessments have certain limitations, as standardized surveys may not completely capture the nuanced values 
of different cultures and could reflect Western biases. Stakeholders, including policymakers and industry 
leaders, can apply these insights to create ethical guidelines for the deployment of LLMs in critical fields such as 
healthcare, education, and law enforcement6,45.
While the design is detailed, it still has several important limitations28. The basic subjectivity involved in 
moral reasoning creates challenges, as personal, cultural, and contextual perspectives lead to complex rather 
than simple answers5,24. This subjectivity hinders the ability to create universally accepted standards for 
evaluation40. Moreover, the framework relies on predefined scenarios that might not truly reflect the ethical 
intricacies of real-life situations, where ambiguous information, conflicting values, and ever-changing contexts 
are typical17,26. LLMs can generate what appears to be logical yet flawed reasoning, which is further complicated 
by their training on biased datasets29,46. Additionally, the framework fails to consider the evolving ethical 
standards across different cultures and time periods21, concentrating primarily on text-based scenarios, which 
could overlook multimodal ethical dilemmas47.
Experimental results and overall performance
Our thorough analysis indicates considerable differences in the moral reasoning abilities of the evaluated LLM 
systems11. Table 1 illustrates the overall performance across our three main assessment criteria.
The findings reveal that leading models such as Claude48 and GPT-43 attain the highest overall scores, with 
Claude showing exceptional strength in maintaining value consistency, while GPT-4 stands out in terms of 
reasoning complexity. Importantly, all models exhibit greater competence in Moral Foundations Alignment 
(MFA) relative to more intricate aspects like dilemma resolution, implying that basic moral intuitions may be 
more effectively integrated during model training than more sophisticated ethical reasoning49.
Performance in specific moral foundations
In order to gain a deeper understanding of model performance, we conducted an analysis of their alignment 
with the five moral foundations outlined in Moral Foundations Theory4 (see Table 2).
All models show significantly higher performance on individualizing foundations (Care and Fairness) 
versus binding foundations (Loyalty, Authority, and Sanctity), reflecting WEIRD population patterns23. Figure 
2 illustrates this trend.
Components of moral reasoning
Furthermore, we assessed the complexity of moral reasoning processes beyond mere alignment with human 
judgments28. Our investigation identified four essential elements of ethical deliberation: principle identification, 
perspective-taking, consequence analysis, and principle application18. Each component was evaluated using 
Model
MFA score
Reasoning index
Value consistency
Composite score
GPT-4o
89.7 ± 0.8ab
92.3 ± 0.9a
87.6 ± 1.1bc
90.0 ± 1.0ab
Claude 3.7 Sonnet
91.2 ± 0.9a
90.8 ± 0.9ab
92.5 ± 0.9a
90.9 ± 0.9a
Deepseek-V3
86.5 ± 0.9bc
89.1 ± 0.8b
83.7 ± 1.0c
86.1 ± 1.0bc
LLaMA 3.1 (70B)
78.3 ± 0.8d
75.6 ± 0.8c
72.8 ± 0.9d
75.8 ± 1.0d
Gemini 2.5 Pro
88.2 ± 1.0abc
84.7 ± 0.9b
86.9 ± 0.9b
86.1 ± 1.1c
F-statistic
33.6∗∗∗
56.0∗∗∗
60.7∗∗∗
28.6∗∗∗
Effect size (η2)
0.35
0.48
0.50
0.32
Table 1.  Overall performance across assessment dimensions with statistical analysis. Values are mean ± SE 
(n=50). Different letters indicate significant differences (Tukey HSD, p < 0.05). ∗∗∗ p < 0.001. F-statistics: df = 
(4,245).
 
Scientific Reports |        (2025) 15:34642 
6
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 7 ---

standardized scoring rubrics adapted from established moral psychology frameworks, with responses scored 
independently by two trained evaluators (Cohen’s κ = 0.89, indicating strong inter-rater reliability).
Table 3 details model performance across these reasoning dimensions. Statistical analysis using one-way 
ANOVA revealed significant differences between models across all four components (all F-tests: p < 0.001), 
with large effect sizes (η2 = 0.39 −0.46) indicating substantial practical differences in reasoning capabilities.
Our research demonstrates that all models show enhanced capabilities in identifying relevant moral 
principles and evaluating consequences; however, they encounter considerable difficulties in adopting various 
perspectives or consistently applying principles across different contexts39. Subsequent analyses indicated that 
Claude 3.7 Sonnet exhibited the most robust perspective-taking abilities, significantly surpassing all other 
models (p < 0.01), whereas GPT-4o excelled in identifying principles and analyzing consequences. This trend 
suggests that while models are capable of identifying ethical concerns, they encounter considerable difficulties 
with the integrated reasoning required for sophisticated moral reasoning25.
To delve deeper into the quality of moral reasoning, we conducted an extensive analysis of reasoning depth 
across the identical 50 standardized moral dilemma scenarios. Each response was evaluated using a validated 
5-point scale adapted from established moral development frameworks18,19: (1) Basic moral issue identification, 
(2) Limited stakeholder consideration, (3) Moderate consequence analysis, (4) Advanced ethical framework 
integration, and (5) Expert-level nuanced synthesis. The performance gaps between top-tier models (GPT-4o, 
Claude) and LLaMA 3.1 (70B) were particularly pronounced, with Cohen’s d effect sizes ranging from 1.8 to 2.4 
across all reasoning components, indicating very large practical differences.
Figure 3 presents the distribution of reasoning depth scores across models and compares them with human 
baseline performance. Human baseline data were derived from a comparable moral reasoning study conducted 
by Rest et al. (1999) using identical scenario types and scoring criteria (N = 200 university students, age 18-
25, diverse academic backgrounds). The human sample serves as a validated standard for assessing model 
performance in relation to conventional human moral reasoning abilities.
The analysis uncovers clear patterns in the complexity of reasoning. Human participants exhibited a significant 
inclination towards advanced reasoning (scores 4–5), with 74% of their responses reaching these elevated levels. 
Among LLMs, GPT-4o most closely approximated human performance patterns, with 62% of responses scoring 
4-5, followed by Claude 3.7 Sonnet at 56%. In contrast, LLaMA 3.1 (70B) showed a concerning concentration in 
moderate reasoning levels (score 3), with only 28% achieving advanced reasoning scores. Following Dunn’s test 
with Bonferroni correction for post-hoc pairwise comparisons, it was found that human baseline performance 
significantly outperformed all LLM models (all p < 0.001). In contrast, GPT-4o and Claude 3.7 Sonnet did not 
show a significant difference from one another (p = 0.23), indicating that they have similar reasoning depth 
Model
Principle identification
Perspective taking
Consequence analysis
Principle application
GPT-4o
94.3 ± 1.2a
91.7 ± 1.4ab
93.2 ± 1.1a
90.1 ± 1.5a
Claude 3.7 Sonnet
92.8 ± 1.3ab
93.5 ± 1.2a
89.4 ± 1.6b
87.6 ± 1.7ab
Deepseek-V3
90.2 ± 1.5bc
88.3 ± 1.8bc
91.0 ± 1.3ab
86.9 ± 1.6bc
LLaMA 3.1 (70B)
79.5 ± 2.1d
74.8 ± 2.3d
77.2 ± 2.0c
71.0 ± 2.4d
Gemini 2.5 Pro
87.6 ± 1.7c
85.9 ± 1.9c
84.7 ± 1.8b
80.5 ± 2.0c
F-statistic
F (4, 245) = 48.7∗∗∗
F (4, 245) = 52.1∗∗∗
F (4, 245) = 44.3∗∗∗
F (4, 245) = 39.8∗∗∗
Effect size (η2)
0.44
0.46
0.42
0.39
Table 3.  Performance across reasoning components with statistical analysis. Values are mean ± SE (n = 50 
scenarios per model). Different letters indicate significant differences (Tukey HSD post-hoc test, p < 0.05). 
∗∗∗p < 0.001
 
Model
Care
Fairness
Loyalty
Authority
Sanctity
GPT-4o
94.2ab
92.8ab
85.3bc
83.7bc
82.5bc
Claude 3.7 Sonnet
96.1a
94.3a
87.5ab
85.2ab
84.9ab
Deepseek-V3
92.3bc
90.7bc
82.1cd
79.8cd
77.3cd
LLaMA 3.1 (70B)
86.7d
84.2d
74.6e
70.2e
68.5e
Gemini 2.5 Pro
93.5abc
91.4abc
84.8bcd
81.6bcd
80.3bcd
Human baseline
95.2a
93.7ab
88.4a
87.3a
86.1a
F-statistic
42.3∗∗∗
38.9∗∗∗
51.2∗∗∗
56.8∗∗∗
61.4∗∗∗
Effect size (η2)
0.42
0.40
0.47
0.49
0.51
Table 2.  Performance across moral foundations with statistical analysis. Values are means (n = 50). Different 
letters indicate significant differences (Tukey HSD, p < 0.05). ∗∗∗ p < 0.001. F-statistics: df = (5,294).
 
Scientific Reports |        (2025) 15:34642 
7
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 8 ---

capabilities among the top models. A qualitative review of the responses from the models suggests that those 
with higher performance levels exhibit deeper reasoning, a more nuanced grasp of conflicting values, and a more 
consistent application of ethical principles across a range of situations41.
Consistency and stability
To evaluate the stability of moral reasoning, we performed several assessment rounds with slight variations in 
prompts50. This testing validates that our standardized prompt approach (described in “Technical implementation 
and prompt engineering”) produces reliable results regardless of minor wording variations. We examined three 
types of question modifications across five separate assessment rounds to ensure the reliability of our results. 
First, we reformulated questions while maintaining their moral significance (transforming “How much do you 
agree...” into “To what extent do you support...”). Second, we presented the same moral scenarios with varying 
contextual backgrounds. Finally, we alternated between direct numerical ratings and explanatory responses that 
we converted into numerical scores.
Each language model was evaluated with all question variations over five independent rounds, with 
assessments occurring 24 h apart to avoid carryover effects. This methodology resulted in 15 evaluations per 
model (3 question types × 5 rounds). Figure 4 displays the consistency scores throughout these evaluation 
rounds.
As shown in Table 4, Claude 3.7 Sonnet showcases the highest degree of consistency (CV = 0.54%), which 
signifies stable moral reasoning processes despite alterations in question framing48. On the other hand, GPT-4o 
displays good stability (CV = 1.10%), with only minor fluctuations observed across the evaluation rounds. In 
contrast, LLaMA 3.1 (70B) shows a significant sensitivity to prompt variations (CV = 3.60%), representing the 
largest variation among all models evaluated51. This notable variability implies that LLaMA’s moral reasoning 
outputs are considerably influenced by superficial changes in how questions are presented.
The findings can be interpreted in different ways concerning the variation of prompts in ethical reasoning 
applications42. Models that score higher in consistency tend to display stable moral reasoning processes that are 
less prone to framing effects, whereas variations in prompt formulations may reflect context-sensitive ethical 
reasoning. In actual applications where ethical scenarios are framed differently, models that adapt their reasoning 
techniques while adhering to fundamental principles might reveal more refined ethical processing capabilities.
Correlation between moral foundations
To investigate the connections between moral foundations in LLM reasoning, we computed Pearson correlation 
coefficients for the foundation scores across all assessed scenarios4. Table  5 displays the inter-foundation 
correlations for all analyzed models, assessing whether they exhibit consistent internal moral frameworks that 
correspond with recognized psychological theories (see Table 5).
The correlation analysis reveals systematic differences in moral framework coherence across models. Claude 
3.7 Sonnet and GPT-4o demonstrate correlation patterns most similar to human baselines, with strong within-
category correlations and appropriately weak cross-category relationships. The individualizing foundations 
Fig. 3.  Distribution of reasoning depth scores in moral dilemma responses across models and human 
baseline. Sample sizes: N = 50 scenarios per model, N = 200 for human baseline19. Scoring criteria: 1 = 
basic moral recognition, 2 = limited analysis, 3 = moderate reasoning with stakeholder consideration, 4 = 
advanced integration of multiple ethical frameworks, 5 = expert-level synthesis with cultural sensitivity. Chi-
square analysis: χ2(20) = 45.7, p < 0.001, indicating significant differences in reasoning depth distributions 
between groups.
 
Scientific Reports |        (2025) 15:34642 
8
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 9 ---

(Care-Fairness) show robust correlations in top-performing models (r = 0.74 −0.78), while binding 
foundations (Loyalty-Authority-Sanctity) maintain strong intercorrelations (r = 0.61 −0.72), consistent with 
moral foundations theory5.
Mid-tier models (Deepseek-V3, Gemini 2.5 Pro) exhibit moderate correlation patterns that preserve the 
theoretical distinction between individualizing and binding foundations, though with somewhat weaker within-
category relationships (r = 0.52 −0.68). Most notably, LLaMA 3.1 (70B) shows substantially weaker correlations 
across all foundation pairs and exhibits an atypically strong Care-Sanctity correlation (r = 0.35), suggesting 
less coherent internal moral reasoning structures and potential confusion between theoretically distinct moral 
concerns.
Model
Care-fairness
Loyalty-authority
Authority-sanctity
Loyalty-sanctity
Care-sanctity
Pattern quality
Claude 3.7 Sonnet
0.78∗∗∗
0.72∗∗∗
0.70∗∗∗
0.65∗∗∗
0.25
High
GPT-4o
0.74∗∗∗
0.68∗∗∗
0.66∗∗∗
0.61∗∗∗
0.22
High
Deepseek-V3
0.68∗∗∗
0.59∗∗
0.58∗∗
0.55∗∗
0.29∗
Moderate
Gemini 2.5 Pro
0.65∗∗
0.56∗∗
0.54∗∗
0.52∗∗
0.31∗
Moderate
LLaMA 3.1 (70B)
0.51∗
0.43∗
0.39∗
0.37∗
0.35∗
Low
Human baseline
0.81∗∗∗
0.75∗∗∗
0.73∗∗∗
0.71∗∗∗
0.19
High
Table 5.  Inter-foundation correlations across all models. Key correlations shown: care-fairness 
(individualizing), loyalty-authority-sanctity (binding), care-sanctity (cross-category). ∗p < 0.05, ∗∗p < 0.01, 
∗∗∗p < 0.001 (N=50).
 
Model
Mean score
Std dev
CV (%)
Rank
Claude 3.7 Sonnet
94.4 ± 0.5a
0.51
0.54
1
GPT-4o
92.0 ± 0.9b
1.01
1.10
2
Gemini 2.5 Pro
86.3 ± 1.7c
1.72
1.99
3
Deepseek-V3
84.3 ± 1.8d
1.89
2.24
4
LLaMA 3.1 (70B)
74.4 ± 2.6e
2.68
3.60
5
Table 4.  Consistency statistics across all models. Values are mean ± SE. Different letters indicate significant 
differences (Tukey HSD, p < 0.05). CV coefficient of variation. F(4, 20) = 18.7∗∗∗, p < 0.001
 
Fig. 4.  Consistency scores across evaluation rounds with prompt variations (N = 15 evaluations per model). 
Statistical analysis: F(4, 20) = 18.7, p < 0.001.
 
Scientific Reports |        (2025) 15:34642 
9
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 10 ---

The Care-Sanctity correlation serves as a particularly informative indicator of model coherence, as these 
foundations represent fundamentally different moral priorities (individual welfare versus purity concerns). 
Higher-performing models maintain appropriately weak correlations (r = 0.19 −0.25), while LLaMA’s 
stronger correlation suggests difficulty distinguishing between these distinct moral domains4.
These findings demonstrate that advanced LLMs can develop internally consistent moral reasoning 
frameworks that mirror established psychological theories, with correlation strength and pattern coherence 
serving as indicators of overall moral reasoning sophistication.
Specific failure modes
Furthermore, our analysis identified several recurring patterns of reasoning errors across various models2, as 
illustrated in Fig. 5, which emphasizes the prevalence of different failure modes.
The identified failure patterns are categorized into five distinct groups: (1) Value conflicts arise when models 
face situations that involve genuinely competing moral principles, which often leads to overly simplistic 
solutions39; (2) Cultural biases indicate the prevalent use of Western-centric ethical frameworks in cross-cultural 
contexts, thereby restricting global relevance43; (3) Overgeneralization takes place when models implement 
ethical principles without sufficient regard for context-specific subtleties45; (4) Inconsistency appears as conflicting 
moral judgments in conceptually similar situations, which diminishes reliability42; and (5) Context insensitivity 
denotes the inability to acknowledge and integrate pertinent contextual elements during ethical assessments52.
Comparison with human baselines
In order to assess the performance of the model in relation to established psychological benchmarks, we 
conducted a comparison of MFA scores with human baseline data derived from validated studies in moral 
psychology4. This analysis offers essential insights into the extent to which AI systems mirror human moral 
reasoning patterns across various ethical domains.
The analysis indicates systematic variations in model alignment across different moral foundation categories. 
All assessed models show a significantly greater agreement with human judgments regarding individualizing 
foundations (Care and Fairness) in comparison to binding foundations (Loyalty, Authority, and Sanctity), which 
aligns with established cross-cultural differences in moral reasoning5,23. Claude 3.7 achieves the highest overall 
alignment with human moral intuitions at 91.2%, followed by GPT-4o at 87.8%, whereas LLaMA 3.1 shows the 
most significant deviation from human baselines at 76.3%32. This trend points to the possibility that existing 
language models may reveal a consistent bias towards individualistic ethical frameworks, which could impede 
their effectiveness in collectivist cultural contexts where collective principles are of greater moral importance. 
Figure 6 represents these alignment trends among all reviewed models.
Conclusions and future directions
This research makes five key contributions to AI ethics evaluation. First, we propose a three-dimensional 
evaluation framework encompassing Moral Foundation Alignment, Reasoning Quality Index, and Value 
Consistency Assessment for comprehensive ethical evaluation11,28. Second, we deliver quantifiable metrics for 
systematically comparing LLM moral reasoning performance across different model architectures32,53. Third, 
Fig. 5.  Distribution of failure mode frequencies across large language models. Each cell represents the 
percentage of instances where a specific failure mode (rows) was observed for each model (columns). Color 
intensity corresponds to failure rate, with darker shades indicating higher frequencies. LLaMA 3.1 (70B) 
demonstrates consistently elevated failure rates across all evaluated categories.
 
Scientific Reports |        (2025) 15:34642 
10
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 11 ---

we establish standardized benchmarks by adapting established moral psychology instruments (MFQ-30, WVS, 
Moral Dilemmas), providing reliable assessment tools4,17,22. Fourth, we provide open-source implementation 
through a comprehensive repository enabling broad adoption of ethical AI evaluation54,55. Finally, our findings 
reveal actionable insights for improving cross-cultural alignment and moral consistency in LLMs5,43.
While LLMs excel in structured tasks, their ethical reasoning across diverse scenarios remains limited2,7. 
Our open-source benchmarking tools aim to make ethics evaluation more accessible and create a framework 
for comparing ethical AI development approaches53,54. As LLMs become embedded in critical decision-making 
processes, ensuring their alignment with human values across cultural contexts transforms from a technical 
challenge into an ethical necessity6.
Future work should develop adaptive evaluation methods incorporating real-world scenarios, gather 
diverse cultural perspectives through international collaborations56, and integrate explainability tools to better 
understand LLM reasoning processes57. Expanding to multimodal datasets and establishing global standards 
through researcher-policymaker collaboration will contribute to more comprehensive and inclusive evaluation 
frameworks47,58.
Data availability
Data Availability: The datasets generated and analysed during the current study are available in the LLM Ethics 
Benchmark repository: LLM Ethics Benchmark Repository: ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​T​​h ​e​-​R​e​s​p​o​n​s​i​b​l​e​-​A​I​-​I​n​i​t​i​a​t​i​v​e​/​
L​L​M​_​E​t​h​i​c​s​_​B​e​n​c​h​m​a​r​k​.​g​i​t​
Received: 30 May 2025; Accepted: 2 September 2025
References
	 1.	 Brown, T. B. et al. Language models are few-shot learners. Adv. Neural Inf. Process. Syst. 33, 1877–1901 (2020).
	 2.	 Bommasani, R. et al. On the opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258 (2021).
	 3.	 OpenAI. Gpt-4 Technical Report. arXiv preprint arXiv:2303.08774 (2023).
	 4.	 Graham, J. et al. Mapping the moral domain. J. Pers. Soc. Psychol. 1010(2), 366–385 (2011).
	 5.	 Jonathan Haidt. The Righteous Mind: Why Good People are Divided by Politics and Religion. (Vintage, 2012).
	 6.	 Gabriel, I. Artificial intelligence, values, and alignment. Minds Mach. 30, 411–437 (2020).
	 7.	 Hendrycks, D. et al. Ethics of artificial intelligence. arXiv preprint arXiv:2106.08458 (2021).
	 8.	 Amodei, D. et al. Concrete problems in AI safety. arXiv preprint arXiv:1606.06565 (2016).
	 9.	 Rae, J.W. et al. Scaling language models: Methods, analysis from training gopher. arXiv preprint arXiv:2112.11446 (2021).
	10.	 Yang, Y. et al. Glue-x: Evaluating natural language understanding models from an out-of-distribution generalization perspective. 
arXiv preprint arXiv:2211.08073 (2022).
	11.	 Liang, P. et al. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110 (2022).
	12.	 Hendrycks, D. et al. Measuring mathematical problem solving with the math dataset. arXiv preprint arXiv:2103.03874 (2021).
	13.	 D. Hendrycks et al. Measuring coding challenge competence with apps. arXiv preprint arXiv:2105.09938 (2021).
	14.	 Singhal, S. et al. Large language models encode clinical knowledge. Nature 6200(7972), 1–10 (2023).
	15.	 Huang, Y. et al. Trustgpt: A benchmark for trustworthy and responsible large language models. arXiv preprint arXiv:2306.11507 
(2023).
	16.	 Zheng, Z. et al. Safetybench: Evaluating the safety of large language models with multiple choice questions. arXiv preprint 
arXiv:2305.13656 (2023).
	17.	 Cushman, F., Young, L. & Hauser, M. The dynamics of moral judgment. Cognition 1030(3), 393–420 (2006).
	18.	 Kohlberg, L. The Philosophy of Moral Development: Moral Stages and the Idea of Justice. (Harper & Row, 1981).
Fig. 6.  Model alignment with human moral judgments across moral foundation categories. Individualizing 
foundations comprise Care and Fairness, while Binding foundations include Loyalty, Authority, and Sanctity. 
All models demonstrate stronger alignment with individualizing versus binding moral foundations.
 
Scientific Reports |        (2025) 15:34642 
11
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 12 ---

	19.	 Rest, J., Narvaez, D., Bebeau, M. J. & Thoma, S. J. Postconventional Moral Thinking: A Neo-Kohlbergian Approach (Lawrence 
Erlbaum Associates, 1999).
	20.	 Haidt, J. The emotional dog and its rational tail: A social intuitionist approach to moral judgment. Psychol. Rev. 1080(4), 814–834 
(2001).
	21.	 Graham, J. et al. Moral foundations theory: The pragmatic validity of moral pluralism. Adv. Exp. Soc. Psychol. 47, 55–130 (2013).
	22.	 Inglehart, R. et al. World Values Surveys and European Values Surveys, 1981-1984, 1990-1993, and 1995-1997. (Inter-university 
Consortium for Political and Social Research, 2000).
	23.	 Henrich, J., Heine, S. J. & Norenzayan, A. The weirdest people in the world?. Behav. Brain Sci. 330(2–3), 61–83 (2010).
	24.	 Shweder, R. A. et al. The “big three” of morality (autonomy, community, divinity) and the big three explanations of suffering. Moral. 
Health 119–169 (1997).
	25.	 Greene, J. D. et al. An FMRI investigation of emotional engagement in moral judgment. Science 2930(5537), 2105–2108 (2001).
	26.	 Awad, E. et al. The moral machine experiment. Nature 5630(7729), 59–64 (2018).
	27.	 Zhu, Z. et al. Promptbench: Towards evaluating the robustness of large language models on adversarial prompts. arXiv preprint 
arXiv:2306.04528 (2023).
	28.	 Denny, N. & Matusiak, A. Measuring moral reasoning using moral dilemmas: Evaluating reliability, validity, and differential item 
functioning of the behavioral defining issues test. J. Moral Educ. 500(3), 316–337 (2021).
	29.	 Rudinger, R. et al. Gender bias in coreference resolution. In Proceedings of the 2018 Conference of the North American Chapter of 
the Association for Computational Linguistics: Human Language Technologies. 8–14 (2018).
	30.	 Wang, W. et al. Chain-of-thought prompting for responding to in-depth dialogue questions with LLM. arXiv preprint 
arXiv:2307.05082 (2023).
	31.	 Chen, M. et al. Do LLMS understand social knowledge? Evaluating the sociability of large language models with socket benchmark. 
arXiv preprint arXiv:2306.13249 (2023).
	32.	 LMSYS. Chatbot Arena: Benchmarking LLMS in the Wild with ELO Ratings (2023). https://lmsys.org.
	33.	 Zhong, Z. et al. Agieval: A human-centric benchmark for evaluating foundation models. arXiv preprint arXiv:2304.06364 (2023).
	34.	 Hendrycks, H. et al. Human-AI moral consistency: Bias recognition dataset. https://github.com/hendrycks/ethics (2023).
	35.	 Devlin, J. et al. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805 
(2019).
	36.	 Reimers, N. & Gurevych, I. Sentence-bert: Sentence embeddings using siamese bert-networks. In Proceedings of the 2019 
Conference on Empirical Methods in Natural Language Processing. 3982–3992 (2019).
	37.	 Liu, X. et al. Multi-task deep neural networks for natural language understanding. In Proceedings of the 57th Annual Meeting of the 
Association for Computational Linguistics. 4487–4496 (2019).
	38.	 Li, N. et al. Logic-guided semantic representation learning for zero-shot relation classification. In Proceedings of the 28th 
International Conference on Computational Linguistics. 2967–2978 (2019).
	39.	 Emelin, D. et al. Moral stories: Situated reasoning about norms, intents, actions, and their consequences. In Proceedings of the 2021 
Conference on Empirical Methods in Natural Language Processing. 698–718 (2021).
	40.	 Lind, G. The moral judgment test (MJT): Thirty years of research. Educ. Res. Eval. 60(1), 1–20 (2000).
	41.	 Wei, J. et al. Chain of thought prompting elicits reasoning in large language models. arXiv preprint arXiv:2201.11903 (2022).
	42.	 Wang, X. et al. Self-consistency improves chain of thought reasoning in language models. arXiv preprint arXiv:2203.11171 (2022).
	43.	 Cao, A. et al. Cultural alignment of large language models. arXiv preprint arXiv:2212.10511, (2022).
	44.	 Stephanie Hanes Larson. Gender, race, and intersectionality on the federal appellate bench. Washington Univ. Law Rev. 970(5), 
1–42 (2017).
	45.	 Weidinger, L. et al. Taxonomy of risks posed by language models. In Proceedings of the 2022 ACM Conference on Fairness, 
Accountability, and Transparency. 214–229 (2022).
	46.	 Bender, E.M. et al. On the dangers of stochastic parrots: Can language models be too big? In Proceedings of the 2021 ACM 
Conference on Fairness, Accountability, and Transparency. 610–623 (2021).
	47.	 Coda, E.M. et al. Multimodal-coda: A dataset for contrastive disambiguation analysis in multimodal reasoning. arXiv preprint 
arXiv:2307.01254 (2023).
	48.	 Anthropic. Claude: A conversational AI assistant. Anthropic Blog. https://www.anthropic.com/index/introducing-claude (2023).
	49.	 Clark, E. et al. On the role of reasoning in moral alignment of language models. arXiv preprint arXiv:2302.07459 (2023).
	50.	 Zhao, T. et al.. Calibrate before use: Improving few-shot performance of language models. arXiv preprint arXiv:2102.09690 (2021).
	51.	 Touvron, H. et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288 (2023).
	52.	 Li, N. et al. Systematic evaluation of causal discovery in visual model based reinforcement learning. arXiv preprint arXiv:2203.12188 
(2022).
	53.	 Liang, P. et al. Holistic evaluation of language models. arXiv preprint arXiv:2211.09110 (2022).
	54.	 Wolf, T. et al. Transformers: State-of-the-art natural language processing. In Proceedings of the 2020 Conference on Empirical 
Methods in Natural Language Processing: System Demonstrations. 38–45 (2020).
	55.	 Johnson, R. et al. Ethics-eval: A benchmarking framework for ethical evaluation of language models (2023). ​h​t​t​p​s​:​/​/​g​i​t​h​u​b​.​c​o​m​/​A​
I​-​s​e​c​u​r​e​/​e​t​h​i​c​s​-​e​v​a​l​.​
	56.	 Arora, A., Storks, S., Nakhost, H., Chen, J. & Liang, P. Probing pre-trained language models for cross-cultural differences in values. 
Find. Assoc. Comput. Linguist. EMNLP 2022, 3922–3944 (2022).
	57.	 Molnar, C. Interpretable Machine Learning. Lulu.com (2022).
	58.	 Jobin, A., Ienca, M. & Vayena, E. The global landscape of AI ethics guidelines. Nat. Mach. Intell. 10(9), 389–399 (2019).
Acknowledgements
This research is funded by the NSF grants 2125858 , 2236305 and UT-Good Systems Grand Challenge. The au­
thors would like to expresstheir gratitude for these institutes' support, which made this study possible. Further­
more, we thank AI applications for their assistance inediting. Furthermore, we thank AI applications for their 
assistance in editing and brainstorming.
Author contributions
J.J. ,S.A., A.M., conceived and developed the main idea, contributed to the conceptualization and methodology, 
and conducted both qualitative and quantitative analyses. K.C., D.A. and A.D. contributed to the methodology 
and carried out qualitative or quantitative analyses.
Declarations
Competing interests
The authors declare no competing interests.
Scientific Reports |        (2025) 15:34642 
12
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

--- Page 13 ---

Additional information
Correspondence and requests for materials should be addressed to S.A.
Reprints and permissions information is available at www.nature.com/reprints.
Publisher’s note  Springer Nature remains neutral with regard to jurisdictional claims in published maps and 
institutional affiliations.
Open Access   This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 
4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in 
any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide 
a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have 
permission under this licence to share adapted material derived from this article or parts of it. The images or 
other third party material in this article are included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence 
and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to 
obtain permission directly from the copyright holder. To view a copy of this licence, visit ​h​t​t​p​:​/​/​c​r​e​a​t​i​v​e​c​o​m​m​o​
n​s​.​o​r​g​/​l​i​c​e​n​s​e​s​/​b​y​-​n​c​-​n​d​/​4​.​0​/​.​
© The Author(s) 2025 
Scientific Reports |        (2025) 15:34642 
13
| https://doi.org/10.1038/s41598-025-18489-7
www.nature.com/scientificreports/

```
