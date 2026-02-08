---
title: "2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models - PDF Extract"
source_pdf: "2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models.pdf"
pages: 75
extracted_at: "2026-02-07T17:00:47.099055"
---

# PDF Extract: 2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models

**Source PDF:** 2025-Hu-LLMs on Trial Evaluating Judicial Fairness for Large Language Models.pdf
**Total Pages:** 75

---

## Content

```
--- Page 1 ---

Working Paper
LLMS ON TRIAL: EVALUATING JUDICIAL FAIRNESS
FOR LARGE LANGUAGE MODELS
Yiran Hua,b∗, Zongyue Xuea,c†∗, Haitao Lia∗, Siyuan Zhengd, Qingjing Chene, Shaochun Wanga,
Xihan Zhanga, Ning Zhenga, Yun Liua‡, Qingyao Aia, Yiqun Liua, Charles L.A. Clarkeb
& Weixing Shena
a Tsinghua University, China
b University of Waterloo, Canada
c Yale Law School, USA
d Shanghai Jiao Tong University, China
e University of Bologna, Italy
ABSTRACT
Large Language Models (LLMs) are increasingly used in high-stakes fields where
their decisions impact rights and equity. However, LLMs’ judicial fairness and
implications for social justice remain underexplored. When LLMs act as judges,
the ability to fairly resolve judicial issues is a prerequisite to ensure their trust-
worthiness. Based on theories of judicial fairness, we construct a comprehensive
framework to measure LLM fairness, leading to a selection of 65 labels and 161
corresponding values. Applying this framework to the judicial system, we compile
an extensive dataset, JudiFair, comprising 177,100 unique case facts. To achieve
robust statistical inference, we develop three evaluation metrics—inconsistency,
bias, and imbalanced inaccuracy—and introduce a method to assess the over-
all fairness of multiple LLMs across various labels. Through experiments with
16 LLMs, we uncover pervasive inconsistency, bias, and imbalanced inaccuracy
across models, underscoring severe LLM judicial unfairness. Particularly, LLMs
display notably more pronounced biases on demographic labels, with slightly less
bias on substance labels compared to procedure ones. Interestingly, increased in-
consistency correlates with reduced biases, but more accurate predictions exacer-
bate biases. While we find that adjusting the temperature parameter can influence
LLM fairness, model size, release date, and country of origin do not exhibit signif-
icant effects on judicial fairness. Accordingly, we introduce a publicly available
toolkit1, designed to support future research in evaluating and improving LLM
fairness.
1
INTRODUCTION
In recent years, Large Language Models (LLMs) are increasingly utilized as decision-makers in
high-stakes fields such as medicine, psychology, and law, where their decisions can directly impact
human rights and social equity (Bruscia et al., 2024). While many models now demonstrate
fairness in general-domain benchmarks, do they wield a slanted scale of justice? When LLMs
are integrated into everyday life, ensuring the judicial fairness of LLMs is crucial for maintaining
social justice. Unfair judgments made by LLMs risk not only misallocating legal rights but also
perpetuating social discrimination, leading to long-term societal harm (Cheong et al., 2024). These
risks underscore the necessity for rigorous and fair evaluation mechanisms to ensure that LLMs
serve justice rather than undermine it.
∗The authors contributed equally. The order is random.
†Corresponding author. Email: zongyuexue@outlook.com.
‡Corresponding author. Email: liuyun89@tsinghua.edu.cn.
1https://github.com/THUYRan/LLM-Fairness/blob/main/Toolkit%20Vedio%20Upload.mp4
1
arXiv:2507.10852v2  [cs.CL]  2 Aug 2025

--- Page 2 ---

Working Paper
Figure 1: Classification of LLM fairness.
Judicial fairness poses unique challenges for current LLMs. As Figure 1 shows, LLM fairness is cat-
egorized as human problems and LLM problems (Gallegos et al., 2024). While LLM-specific prob-
lems related to output format (Long et al., 2024), task complexity (Yu et al., 2024), etc., have been
well-studied, whether LLMs exhibit human problems in judicial contexts remains underexplored.
Previous research (Sant et al., 2024; Kumar et al., 2024; Zhang et al., 2024a) has inadequately
addressed fairness. For instance, they primarily concentrated on fairness about substance, overlook-
ing fairness about procedures, which resulted in an incomplete and unreliable fairness evaluation.
Human judges may exhibit bias against defendants without legal representation due to stereotypes
(Quintanilla et al., 2017). Would LLMs make the same mistake? The effect of such purely pro-
cedure factors remains largely unexplored in existing research. Overall, factors examined in past
studies have been predominantly fragmented and addressed on a “case-by-case” basis (Zhang et al.,
2024a;b), lacking a systematic framework and theoretical foundation for fairness evaluation. Thus,
even if a model scores highly on existing fairness benchmarks within general domains, it is still
imperative to evaluate its judicial fairness to further safeguard social justice.
Based on this, this paper proposes a comprehensive method and important innovations for evaluating
LLM judicial fairness:
1. Based on ample theoretical discussion on fairness in law and philosophy, we propose a compre-
hensive systematic framework for LLM judicial fairness evaluation.
2. We propose an evaluation dataset JudiFair, which comprises 177,100 unique case facts, with
65 labels and 161 label values annotated. Our team of legal experts extracted labels and trigger
sentences and replaced them with counterfactual ones. Moreover, we exclude certain cases that may
interfere with fairness evaluation under the law.
3. We develop a novel methodology to comprehensively evaluate LLM judicial fairness with three
metrics: consistency, bias, and imbalanced inaccuracy. To cope with situations in which multiple
labels and LLMs are involved, we employ a suite of statistical tools to ensure robust inference. This
approach offers valuable insights for future research on fairness measurement.
4. We evaluated 16 LLMs developed in different countries, conducted statistical inference in exper-
iments, and discovered severe unfairness across all models while interesting patterns emerge. This
provides guidance for future model training and development.
5. Building on the above innovations, we have developed a toolkit that enables convenient and
comprehensive evaluation of LLM judicial fairness.2
2
RELATED WORKS
Fairness evaluation of LLMs is critical, with fairness problems divided into LLM-specific ones and
human-related ones. LLM-related problems are exclusively unique to LLMs, influenced by factors
such as temperature parameters, weight decay, and specific output formats, affecting self-perception
of attributes and handling of low-frequency tokens, among others (Miotto et al., 2022; La Cava &
Tagarelli, 2024; Pinto et al., 2024; Yu et al., 2024; Long et al., 2024).
2https://drive.google.com/file/d/1lB2U3q-kI5B5frv8iqVceVaA9Yks3kE6/view?usp=sharing
2

--- Page 3 ---

Working Paper
Human-related problems are those that LLMs may inherit similarly to human behavior. Researchers
have primarily assessed them with a limited set of demographic factors like gender in general con-
texts (Dastin, 2018; Rudinger et al., 2018; Webster et al., 2018; Kiritchenko & Mohammad, 2018;
Qian et al., 2022; Parrish et al., 2022). However, these benchmarks, comprising at most nine la-
bels, are neither sufficiently comprehensive nor grounded in adequate theoretical knowledge. They
also suffer from vague definitions of key concepts (Blodgett et al., 2021), lack rigorous statisti-
cal methods to distinguish systematic patterns from random variation, incorporate inadequate legal
knowledge necessary for evaluating fairness in judicial contexts, and do not provide practical, con-
venient toolkits for implementing fairness evaluation methodologies. These limitations significantly
reduce their effectiveness in assessing model fairness.
Some studies tried to place LLMs in legal contexts (Xue et al., 2024; Li et al., 2023a; Xiao et al.,
2018; Yao et al., 2022; Deroy & Maity, 2023; Zhang et al., 2024a). However, Zhang et al. (2024a)
relied on only 11 judicial documents without robust statistical inferences, far too limited to support
convincing evaluation and conclusions. The annotation of CAIL2018 (Xiao et al., 2018) merely
covered legal articles, charges, and prison terms, without providing detailed case facts. LEVEN (Yao
et al., 2022) included legal events in the dataset. Yet, LLM fairness evaluation requires extensive
extra-legal factors like detailed demographic characteristics.
LEEC (Xue et al., 2024) is a Chinese legal dataset consisting of 15,919 legal documents and 155
extra-legal factor labels. As both legal and extra-legal factors may significantly impact the ap-
plication of law (Ulmer, 2012), LEEC’s comprehensive label system, large number of cases, and
introduction of extra-legal labels ensure the dataset’s reliability for studies on LLM judicial fairness.
All these previous works are based on real human judgments and provide insight for this study. How-
ever, LLM fairness evaluations are not necessarily bound to real-world documents, and a specialized
dataset tailored for LLM-based judgments is necessary. Moreover, measuring LLM judicial fairness
in a comprehensive, multi-dimensional, and statistically rigorous way remains an unresolved chal-
lenge. More detailed analysis can be found in Appendix A.
3
JUDICIAL FAIRNESS FRAMEWORK
Philosophers and legal theorists have long engaged in extensive discussions on the concept of ju-
dicial fairness (Rawls, 1971). This section introduces a structured judicial fairness framework de-
signed to support robust and holistic LLM fairness evaluations. Figure 2 illustrates this framework,
which is organized into two main hierarchical layers.
Figure 2: Framework of LLM judicial fairness.
3

--- Page 4 ---

Working Paper
3.1
SUBSTANCE AND PROCEDURE FACTORS
Procedural fairness lies at the heart of the rule of law and justice (Rawls, 1971; Waldron, 2011).
Beyond reinforcing substantive fairness, it promotes predictability, stability, and public confidence
in the judicial system (Burke & Leben, 2024). Empirical research demonstrates that procedure ele-
ments can significantly influence judicial decisions. For instance, judges may view pro se claimants
as less competent, leading to less favorable case outcomes (Quintanilla et al., 2017). Live broad-
casting deliberations can also change the behavior of judges (Lopes, 2018). This raises an important
question: would LLMs replicate these patterns caused by procedure factors?
Moreover, given that LLMs may be trained on vast amounts of judicial documents , they may inter-
nalize statistical correlations between procedure factors and judicial outcomes. For example, more
complex or severe cases are typically handled by higher courts. Would LLMs, then, learn to predict
harsher penalties simply because a case is processed at a higher court level? Procedure factors exist
not only in judicial settings, yet they remain largely overlooked in LLM fairness studies.
Thus, we categorize fairness challenges into two primary domains: substance factors and proce-
dure factors. Substance factors encompass elements directly tied to the factors related to the crime
itself, including the nature of the crime, its location and timing, the defendant’s demographic char-
acteristics, etc. Meanwhile, procedure factors pertain to the judicial decision-making process itself,
which may influence LLMs’ decisions independently of the crime’s intrinsic facts. This framework
allows for a clearer analysis of how LLMs might internalize and replicate different forms of fairness
problems within legal judgments.
3.2
DEMOGRAPHIC AND NON-DEMOGRAPHIC FACTORS
Demographic factors, including defendant ethnicity (Hou & Truex, 2022), defendant gender (Mc-
Coy & Gray, 2007), victim age (Marier et al., 2018), juror gender (Pozzulo et al., 2010), etc., have a
substantial impact on judicial decision-making (Xue et al., 2024). Therefore, we incorporate a range
of demographic factors into our framework for both substantive and procedural considerations. No-
tably, characteristics related to judicial workers are categorized as procedure factors. Consequently,
attributes like defender gender or judge age are classified as procedural demographic factors.
While previous LLM fairness studies have predominantly focused on demographic factors (Qian
et al., 2022; Parrish et al., 2022), this study also includes non-demographic factors for both substan-
tive and procedural dimensions. These non-demographic elements are essential, as they can also
serve as extra-legal factors influencing judicial decisions in practice (Quintanilla et al., 2017). For a
detailed description of specific labels within each category, please refer to Section 4.1.
4
EVALUATION BENCHMARK
4.1
LABEL SYSTEM
Our team of legal expert developed a broad system of 65 labels across four categories within our
fairness framework. Detailed information about these labels is presented in Table A2 to Table A5.
This system expands upon the LEEC dataset (Xue et al., 2024), informed by a comprehensive review
of empirical legal studies. It provides a solid foundation for our label selection and data construction.
However, to examine LLM fairness, we went beyond the LEEC dataset, incorporating additional
labels to cover critical attributes often missing from judicial records, such as sexual orientation and
litigation participants whose details are not typically documented. This expansion broadens the
scope of LLM fairness evaluation.
Specifically, substance factors include demographic labels for defendants and victims, as well as
non-demographic extra-legal factors such as crime date, time, and location. The labels selected
from LEEC include various defendant demographic factors like sex, ethnicity, education level, age,
and more. Procedure factors encompass demographic information for defenders, prosecutors, and
judges. For procedural non-demographic factors, we included elements from LEEC, such as whether
a recusal is applied by the defendant, whether a supplementary civil action is initiated with the
criminal case. For critical factors not typically recorded in judicial documents, we supplemented our
label system to include crucial procedure elements such as whether the trial is open to the public,
4

--- Page 5 ---

Working Paper
whether it is broadcast online, the duration of the trial process, whether the judgment is delivered
immediately following the trial, etc. Overall, our approach allows us to capture a broader range
of procedural fairness considerations in LLM fairness evaluation. For details of the label system,
please refer to Appendix B.
4.2
DATASET
4.2.1
DATA RESOURCE
In this section, we present JudiFair, an evaluation benchmark comprising 177,100 unique case
facts across 65 labels, derived from 1,100 judicial documents. We locate the entire framework in
the Chinese jurisdictions for experimentation. For case data collection, due to the high coverage of
crimes in the LEEC dataset (Xue et al., 2024) and the integration of extra-legal factor labels in its
label system, we select case data from LEEC for further screening and annotation. Based on our
framework, we select 13 labels originally from the LEEC dataset. We also include 51 non-LEEC
labels, and further annotate them in the dataset.
4.2.2
ANNOTATION AND DATA PROCESSING
The construction of LEEC involved assigning over 40 legal experts to annotate judicial documents.
For each label, the experts annotated the label value and the trigger sentence for the label. Based
on LEEC, we conducted further annotations. When annotating each case, we adopted an automated
annotation approach. For each case, we performed an exact match of the label’s trigger sentence
throughout the text. If there was no match, we used LLMs for semantic retrieval and annotation,
which is then reviewed by experts. Due to the relatively standardized writing of legal documents,
most annotations could be carried out by direct extraction and replacement. Meanwhile, for some
labels, we were able to infer and annotate based on the label information annotated in LEEC. For
example, through the court name in the judicial documents, we could infer the Court level label
in JudiFair, whether it is a Primary People’s Court, Intermediate People’s Court, Higher People’s
Court, or Supreme People’s Court.
In data processing, due to the long token count of legal documents, testing all documents could be
quite costly. Therefore, we initially randomly selected 1100 documents from the dataset for each
label. Subsequently, we excluded some crimes for certain labels based on Chinese law from the
selected data. This is because some factors may be legally relevant in certain cases according to law.
For example, measuring LLM bias based on defendants’ occupations without accounting for cases
of accepting bribes could result in inaccurate fairness evaluation, as occupation may be a legally
relevant factor in such cases.
4.2.3
COUNTERFACTUAL PROMPTING
Counterfactual prompting is a technique that encourages LLMs to reason with alternative facts. The
success of counterfactual generation in LLMs has demonstrated their ability to detect differences
between facts (Li et al., 2023b). In the context of LLM-as-a-judge, we expect LLMs to maintain
neutrality when presented with irrelevant differences in facts. This method, as demonstrated in
(Moore et al., 2024) and (Kumar et al., 2024), has proven effective in bias detection.
Inspired by APriCot (Moore et al., 2024), our approach generates a separate query for each fact al-
ternative. This strategy ensures that LLMs evaluate each option independently, minimizing shortcuts
or comparisons that may arise from contextual influences between neighboring queries. Addition-
ally, it allows LLMs to reason logically rather than relying on empirical data, thereby mitigating the
impact of Base Rate Probability.
We aim to construct prompts with minimal alteration from real judicial documents. For each factor
in the label system, there is a corresponding set of fact alternatives. We began by identifying the
relevant texts in case facts and parties, which we refer to as “trigger sentences”. Next, we constructed
the initial query using the original facts. Subsequently, we replaced each fact in the trigger sentences
with its corresponding counterfact. This process resulted in a set of queries for a single case and
label, as shown in Figure A3. Additional information about prompt construction is in Appendix C.
5

--- Page 6 ---

Working Paper
Figure 3: Comparison of imbalanced inaccuracy and bias across scenarios. In Scenario 1, LLMs
predict 100 months for male defendants and 200 months for female defendants while real sentences
are 150 months for both. There is LLM gender-based bias but no imbalanced inaccuracy, as the
absolute deviation is equal. Similarly, in Scenario 2, there is LLM gender-based bias but no imbal-
anced inaccuracy. In Scenario 3, compared with real sentencing, there are both bias and imbalanced
inaccuracy of LLMs. All numbers are fully hypothesized to illustrate the concepts.
5
EVALUATION METHOD
5.1
MULTI-DIMENSIONS OF LLM FAIRNESS EVALUATION
In this paper, we introduce three evaluation metrics to comprehensively capture important dimen-
sions of LLM judicial fairness:
1. Inconsistency. Inconsistency presents significant challenges for LLMs. Even when prompted
with identical inputs and a fixed temperature of 0, LLMs may generate varying responses (Atil et al.,
2024). In judicial settings, different sentencing for similar offenders is a clear sign of unwarranted
inequality (Schulhofer, 1991). However, inconsistency does not inherently imply bias. Thus, we
first measure the inconsistency of LLMs in addressing judicial matters.
2. Bias. Bias is a systematic pattern based on certain characteristics (Ranjan et al., 2024). If LLMs’
judicial decisions are not only inconsistent based on different label values, but also demonstrate a
systematic directional shift based on certain label values based on statistical inferences, they indicate
the presence of bias.
3. Imbalanced Inaccuracy. As the JudiFair dataset is constructed from real judicial documents, it
allows us to incorporate actual sentencing outcomes from human judges into our fairness analysis.
This integration enables us to evaluate how closely LLM-generated sentences align with real-world
judicial decisions. Specifically, certain characteristics may lead LLMs to produce more accurate
or less accurate predictions compared to human judgments. However, the accuracy of LLMs’ pre-
dictions may vary among different groups (e.g., male vs. female defendants), leading to unfairness
(Dieterich et al., 2016). This notion has appeared under various names in the literature (Gupta et al.,
2024), such as Accuracy Equity (Dieterich et al., 2016) or Accuracy Difference (Das et al., 2021).
This concept is illustrated in Figure 3.
Figure 4 illustrates the evaluation methodology. By leveraging descriptive statistics and multiple
statistical inference tools, we assess the consistency, bias, and imbalanced inaccuracy of both in-
dividual models and the overall indicators across all models in our study. This multi-dimensional
evaluation framework also enables the analysis of internal correlations among these three metrics,
as well as their relationships with other key indicators such as model size, temperature, and more.
5.2
EVALUATION METRICS
This section details the algorithm and method for the three measurements of LLM judicial fairness.
6

--- Page 7 ---

Working Paper
Figure 4: Evaluation framework of LLM judicial fairness.
5.2.1
INCONSISTENCY
We measure inconsistency by assessing how often LLM judgments change in response to variations
in label values. Specifically, for each label, we calculate the proportion of judicial documents in
which the LLM’s output differs when the label’s value changes. To account for differences in the
number of values across all the labels, we assign weights proportional to the effective sample size for
each label. The inconsistency measure for an individual LLM is formally defined in Equation 1.3
Next, we calculate the average Inconsistency of all LLMs assessed in this study to obtain an overall
picture across all models collectively.
Inconsistency =
PN
l=1 wl · pl
PN
l=1 wl
(1)
5.2.2
BIAS
We apply multiple methods to ensure robust statistical inference when assessing potential bias in
LLMs. First, we conduct regression analysis for each label, using Treated, the variable representing
the label of interest, as the independent variable. One value of Treated serves as the reference group,
and we create separate binary variables for each remaining value. We include fixed effects for ID
to capture each judicial document’s unique characteristics, thereby isolating the effect of interest.
The dependent variable in the main regression is the length of limited imprisonment in months,
the most commonly imposed principal punishment under Chinese criminal law. Following prior
empirical legal studies (Berdej´o & Yuchtman, 2013; Johnson, 2006), we take the natural logarithm
of sentencing length (plus 1) to address the right-skewed distribution. Equation 2 presents the details.
If Treated has j categories, the model includes j-1 treated variables. Similarly, if ID has i categories,
the model includes i-1 ID variables.
Ln(Sentence) = γ +
j−1
X
j=1
αj · Treatedj +
i−1
X
i=1
βi · IDi + ε
(2)
We use high-dimensional fixed-effect linear regression models with the REGHDFE package in
Stata (Correia, 2017), which efficiently handles high-dimensional fixed effects with accuracy. This
method fits the study as in our analysis, controlling for ID fixed effects introduces around a thou-
sand variables per regression, significantly increasing computational demands. This method is also
widely adopted in quantitative social science research (Huang & Zhang, 2023; Wu et al., 2024;
Gormley et al., 2025). We cluster robust standard errors at the ID level to account for intra-document
correlation, preventing the underestimation of standard errors from shared unobservable character-
istics within the same judicial document.
Next, we conduct multiple robust analyses to test the reliability of our main regression results. The
methods and results of robustness checks are shown in Appendix E.4, all confirming the main results.
3N represents the total number of labels, wl is the weight for label l, calculated as its effective sample
size; pl is the proportion of judicial documents where the LLM’s prediction changes when the value of label l
changes.
7

--- Page 8 ---

Working Paper
After estimating the effect of Treated variables for each label, we apply statistical tests to assess
whether an LLM’s bias is systematic and significant. When analyzing multiple labels simultane-
ously, observed significance may arise purely from random variation.4 To separate true systematic
biases from random noise, we treat each label test as a Bernoulli trial whose “success” is a signif-
icant result (p ≤τ) (Casella & Berger, 2024). Following this methodology, we conduct Bernoulli
tests to evaluate the overall statistical significance from 96 label values across 65 labels for each
model. Equation 3 shows the method.5 If we observe k significant labels, the probability of seeing
at least that many under the null hypothesis of pure randomness is pBernoulli. A small value of pBernoulli
indicates that the number of significant labels is unlikely to be explained by random noise alone, sug-
gesting that the individual LLM’s bias is systematic rather than incidental. Finally, we aggregate
the results of all LLMs and perform an additional Bernoulli test using Equation 3 to determine if
there is a significant bias across all models collectively.
pbernoulli =
N
X
l=k
N
l

τ l 1 −τ
 L−l
(3)
5.2.3
IMBALANCED INACCURACY
First, we summarize accuracy by calculating two key metrics: Mean Absolute Error (MAE) and
Mean Absolute Percentage Error (MAPE). MAE measures the average absolute difference between
predicted and actual values, reflecting overall prediction error regardless of direction. MAPE mea-
sures the average percentage error, indicating the relative size of the error compared to the actual
value. For each label, we calculate these metrics and then compute a weighted average across all
labels to provide a comprehensive accuracy assessment.
Similar to the steps in Section 5.2.2, we apply Equation 2 and replace the dependent variable with the
absolute differences between predicted and actual values to test whether a specific model shows sig-
nificant imbalanced inaccuracy, as shown in Equation 4. Next, we conduct a Bernoulli test in Equa-
tion 3 to assess whether the individual model exhibits systematic imbalanced inaccuracy across all
examined labels. Finally, we aggregate the results across all models in the study and perform an ad-
ditional Bernoulli test using Equation 3 to determine if there is a significant imbalanced inaccuracy
across all models collectively.
Abs Dif = γ +
J
X
j=1
αj · Treatedj +
I
X
i=1
βi · IDi + ε
(4)
6
EXPERIMENTS
6.1
MODEL SELECTION
As shown in Table A1, the experiment is conducted on an extensive list of LLMs, including both
open-source and closed-source models. It also includes LLMs with varying parameter sizes, release
dates, and countries of origin to ensure a diverse representation of models. For the main analysis,
we set the temperature as 0 to reduce randomness in the models.
6.2
BASIC FINDINGS
The main analysis results, including all three metrics about model inconsistency, bias, and imbal-
anced inaccuracy, are shown in Table A17 and Table A18, with the former presenting models at a
temperature of 0 and the latter at a temperature of 1. Several key findings emerge.
Consistency. All models show considerable inconsistency in outputs, either with a temperature
of 0 or 1. Among the 15 models with a temperature of 0, the average inconsistency is over 15%.
4For instance, with a p-value threshold of 0.1, testing 10 labels would, on average, yield one significant
result even if there are only completely random variations in results.
5pbernoulli is the right-tail probability of observing at least k significant labels under the null of purely random
variation, N is the total number of labels tested, l enumerates the possible counts of significant labels being
summed over, k is the number actually found significant, and τ is the per-label significance threshold.
8

--- Page 9 ---

Working Paper
This means that around 18% of judicial documents lead to different outputs with varied value of
labels. When the temperature is set to 1, inconsistency notably goes higher. A deeper analysis of
temperature and consistency is shown in Section G.2.
Bias. Detailed results for each LLM and label’s bias analysis are presented in Appendix E.3, while
the significance levels of each label and model are visually illustrated in Appendix E.1. When
temperature is 0, all models show numerous label values that exhibit significant bias, as shown in
Table A17. A Bernoulli test that sets significant threshold at 0.1 and 0.05 show similar results,
suggesting significant biases for 14 models out of 15 models.6 When the model temperature is set to
1, the overall pattern remains consistent: most models exhibit significant overall biases, as presented
in Table A18. Moreover, the Bernoulli test applied to all LLMs in our sample show a p-value below
0.01, suggesting significant biases across all models. More detailed restuls are shown in E.
Meanwhile, compared with substance factors, procedure factors are slightly more significantly
biased, particularly judge characteristics. The difference between demographic labels and non-
demographic ones is much bigger. Demographic ones demonstrate significantly more biases. Yet,
all non-demographic factors in both substance and procedure categories still exhibit significant bias
in some models. Compulsory measure and Court level are two of the most biased labels.
Utilizing the LEEC labels that enable us to compare with real information of judicial documents, a
deeper analysis based on Appendix E.3 reveals that LLM biases tend to mirror real-world judicial
biases identified in prior empirical legal studies. For instance, if the defendant’s gender significantly
affects LLM sentencing, female defendants are generally treated more leniently, aligning with find-
ings from previous research (McCoy & Gray, 2007). This trend is consistent for other labels as
well. In the Chinese context, studies have shown that defendants with rural household registrations
(Hukou) are likely to suffer a judicial “penalty effect” compared to their urban counterparts (Jiang &
Kuang, 2018). Similarly, if this label significantly influences LLMs’ biases, it tends to increase the
severity of sentencing. Meanwhile, labels typically absent from Chinese judicial documents, such
as the parties’ sexual orientation, may also contribute to LLM bias. This suggests that the origins
of LLM bias are not necessarily confined to judicial records.
Imbalanced Inaccuracy. When the temperature is set to 0, 14 out of 15 models show significant un-
fairness. When the temperature is set to 1, several models exhibit partially insignificant results—that
is, at least one of the two p-value thresholds (0.1 and 0.05) fails to reach significance. Moreover, the
Bernoulli test applied to all LLMs in our sample show a p-value below 0.01, suggesting significant
imbalanced inaccuracy across all models. More detailed results are shown in Appendix F.7
6.3
ADDITIONAL FINDINGS
We calculate the internal correlation among metrics, the temperature impact and the influence of
parameter size and release time. For the comprehensive analysis of additional findings, please refer
to Appendix D to G.
6.3.1
INTERNAL CORRELATION AMONG METRICS
We identify several intriguing correlations among the metrics, as shown in Appendix G.1. Using
the Pearson Correlation Coefficient to achieve statistical significance, we find that:1) There is a
significant negative correlation between inconsistency and the number of biased label values for
each model. This suggests that greater randomness in LLM outputs may obscure underlying biases.
2) There is a positive significant correlation between bias and significant imbalanced inaccuracy. 3)
Notably, as an LLM’s accuracy increases, its bias also increases substantially. This suggests that
when LLMs learn the patterns from real-world judicial data, the improvement in their predictive
accuracy generally comes at the expense of biases.
6It is also worth noting that models’ biases are not completely randomly distributed, but concentrate more
on some labels. For example, defendant wealth shows significant bias in 10 of the 13 models, while victim age
is only biased on one model.
7It is also valuable to present the analysis of pure accuracy of LLM sentencing compared with real sentenc-
ing. The mean of Weighted Average MAE of all models is 64.871. This means that on average, LLM models
would divert form the real sentences for over 5 years on sentencing length. This is far from satisfactory. The
mean of Weighted Average MAPE of all models is 219%, which means that LLMs’ decisions are in general
multiple times harsher than the real sentence, leading to extensive deviation from real sentencing.
9

--- Page 10 ---

Working Paper
6.3.2
TEMPERATURE IMPACT
We also explores the impact of temperature on LLM fairness, using 12 randomly selected models.
The findings are presented in Figure A9. The findings show that inconsistency issues become sig-
nificantly more prominent at higher temperatures, due to the temperature parameter’s influence on
the randomness of model outputs. Additionally, while all models generally exhibit significant biases
at both temperature settings, the number of label values showing significant biases decreases as the
temperature increases, with a p-value of less than 0.01 indicating a strong correlation. These results
align with the analysis in Section 6.3.1, suggesting that increased randomness in LLM outputs may
mask underlying biases.
6.3.3
INFLUENCE OF PARAMETER SIZE, RELEASE DATE, AND COUNTRY OF ORIGIN
We further examined the influence of a model’s release date, parameter size, and country of origin
to LLM fairness, as illustrated in Appendix G.3 to G.5. The analysis reveals no significant influence
of release date, as illustrated in Figure A10, indicating that newer LLMs do not exhibit substantially
lower biases compared to their predecessors. Meanwhile, Figure A11 shows that increasing param-
eter size could not reduce bias or imbalanced inaccuracy in LLMs, and it may even significantly
increase the inconsistency problem of LLMs. Lastly, Figure A12 shows that in our sample, LLMs
developed in China and the United States show no consistent advantage over one another in terms of
judicial fairness across all three metrics. The findings underscore critical challenges in current LLM
development regarding judicial fairness.
7
CONCLUSION
This study presents a systematic framework for evaluating LLM judicial fairness. We craft a multi-
dimensional framework for judicial fairness: it distinguishes between substantive and procedural
factors, and between demographic and non-demographic attributes, and thus, covers a broader range
of fairness dimensions than prior studies. Based on this, we construct a comprehensive label system
with 65 extra-legal factors and 161 different values, and implement it through JudiFair—a bench-
mark of 177,100 counterfactually generated case facts. We assess 16 LLMs across three core met-
rics: inconsistency, bias, and imbalanced inaccuracy. To ensure statistical rigor, we apply fixed-
effect regressions, cluster-robust standard errors, Bernoulli tests, and multiple robustness checks (as
shown in Appendix E.4), offering a comprehensive, robust and interpretable methodological foun-
dation for auditing LLMs in legal contexts.
Our results reveal pervasive fairness challenges: almost all models exhibit substantial and system-
atic inconsistency, bias, and imbalanced inaccuracy. Notably, demographic attributes consis-
tently trigger more pronounced biases, and procedure-related factors remain largely underexamined
in existing literature despite their significant influence. Moreover, we identify several interesting
patterns in further analyses: 1) Models with higher predictive accuracy often show greater bias, sug-
gesting a trade-off between learning real-world judicial patterns and reinforcing existing inequities;
2) Increasing randomness in model outputs undermines output consistency but may reduce bias; 3)
Model size, release date, and country of origin show no correlation with improved fairness. These
findings highlight the complexity and difficulty in improving LLM judicial fairness.
We also acknowledge several limitations and directions for future research. First, our dataset, label
system, and experiments are based primarily on the Chinese legal system. Although our fairness
framework, evaluation metrics, and findings have broader implications, judicial fairness remains
highly context-specific. Future work should extend the evaluation to multilingual and comparative
legal domains. Second, the majority of our experiments were conducted on small or mid-scale non-
reasoning models for efficiency and coverage of more LLMs. Our evaluation of DeepSeek’s reason-
ing model did not reveal significantly fewer fairness issues compared to other models. Yet, LLMs are
developing fast. The full landscape of next-generation models, with their increased parameter sizes
and refined training methods, presents a fertile ground for future investigation. Third, although our
prompting method proves effective for fairness assessment, we do not systematically test more ad-
vanced prompting strategies. Techniques such as Chain of Thought (CoT) or Retrieval-Augmented
Generation (RAG) may improve interpretability and reduce bias, and merit further exploration.
10

--- Page 11 ---

Working Paper
Overall, this work underscores the need for the improvement of LLM judicial fairness. It advo-
cates for a broader perspective in LLM fairness research. Fairness is a broader concept than bias,
and our comprehensive evaluations highlight systematic issues that call for mitigation approaches
beyond mere prompting techniques. Furthermore, as both laypersons and lawyers are using LLMs
extensively for legal tasks (Krook et al., 2024), examining LLM judicial fairness comprehensively is
urgent. We present a toolkit JustEva that facilitates future research through streamlined model API
integration and flexible label expansion.
11

--- Page 12 ---

Working Paper
ETHICS STATEMENT
The datasets used in this study are sourced exclusively from publicly available datasets created in
prior research and used with the permission of the original researchers, with no additional data
collection conducted. All data processing was conducted with care to protect personal information.
This work aims to promote transparency, accountability, and responsible evaluation of LLMs in
high-stakes domains such as law. The methodology and results of this study, as well as the toolkit
JustEva, are solely for LLM fairness evaluation and auditing, and should not replace any human
decision-making in real-world legal systems.
The inclusion of any laws in this study is purely for analytical purposes in evaluating LLM judicial
fairness and, unless explicitly stated, does not constitute or imply any normative judgment from the
authors.
REFERENCES
Amanda Agan, Matthew Freedman, and Emily Owens. Is your lawyer a lemon? incentives and
selection in the public provision of criminal defense. Review of Economics and Statistics, 103(2):
294–309, 2021.
Berk Atil, Alexa Chittams, Liseng Fu, Ferhan Ture, Lixinyu Xu, and Breck Baldwin. Llm stability:
A detailed analysis with some surprises. arXiv preprint arXiv:2408.04667, 2024.
Yejin Bang, Delong Chen, Nayeon Lee, and Pascale Fung. Measuring political bias in large language
models: What is said and how it is said. arXiv preprint arXiv:2403.18932, 2024.
Carlos Berdej´o and Noam Yuchtman. Crime, punishment, and politics: an analysis of political
cycles in criminal sentencing. Review of Economics and Statistics, 95(3):741–756, 2013.
Reuben Binns. Fairness in machine learning: Lessons from political philosophy. In Conference on
fairness, accountability and transparency, pp. 149–159. PMLR, 2018.
Su Lin Blodgett, Gilsinia Lopez, Alexandra Olteanu, Robert Sim, and Hanna Wallach. Stereotyping
norwegian salmon: An inventory of pitfalls in fairness benchmark datasets. In Proceedings of the
59th Annual Meeting of the Association for Computational Linguistics and the 11th International
Joint Conference on Natural Language Processing (Volume 1: Long Papers), pp. 1004–1015,
2021.
Mattia Bruscia, Graziano A Manduzio, Federico A Galatolo, Mario GCA Cimino, Alberto Greco,
Lorenzo Cominelli, and Enzo Pasquale Scilingo. An overview on large language models across
key domains: A systematic review. In 2024 IEEE International Conference on Metrology for
eXtended Reality, Artificial Intelligence and Neural Engineering (MetroXRAINE), pp. 125–130.
IEEE, 2024.
Kevin Burke and Steve Leben. Procedural fairness: A key ingredient in public satisfaction. Ct. Rev.,
60:6, 2024.
George Casella and Roger Berger. Statistical inference. CRC press, 2024.
Arie Cattan, Alon Jacovi, Alex Fabrikant, Jonathan Herzig, Roee Aharoni, Hannah Rashkin, Dror
Marcus, Avinatan Hassidim, Yossi Matias, Idan Szpektor, et al. Can few-shot work in long-
context? recycling the context to generate demonstrations. arXiv preprint arXiv:2406.13632,
2024.
Inyoung Cheong, Aylin Caliskan, and Tadayoshi Kohno. Safeguarding human values: rethinking us
law for generative ai’s societal impacts. AI and Ethics, pp. 1–27, 2024.
Sergio Correia. Linear models with high-dimensional fixed effects: An efficient and feasible estima-
tor. Unpublished manuscript, http://scorreia. com/research/hdfe. pdf (last accessed 25 October
2019), 4(2), 2017.
12

--- Page 13 ---

Working Paper
Sanjiv Das, Michele Donini, Jason Gelman, Kevin Haas, Mila Hardt, Jared Katzman, Krishnaram
Kenthapadi, Pedro Larroy, Pinar Yilmaz, and Bilal Zafar. Fairness measures for machine learning
in finance. The Journal of Financial Data Science, 2021. URL https://www.amazon.science/
publications/fairness-measures-for-machine-learning-in-finance.
Jeffrey Dastin. Amazon scraps secret ai recruiting tool that showed bias against women. reuters
(2018), 2018.
Aniket Deroy and Subhankar Maity. Questioning biases in case judgment summaries: Legal datasets
or large language models? arXiv preprint arXiv:2312.00554, 2023.
Sam Desiere and Ludo Struyven. Using artificial intelligence to classify jobseekers: The accuracy-
equity trade-off. Journal of Social Policy, 50(2):367–385, 2021.
William Dieterich, Christina Mendoza, and Tim Brennan. Compas risk scales: Demonstrating ac-
curacy equity and predictive parity. Northpointe Inc, 7(4):1–36, 2016.
Isabel O Gallegos, Ryan A Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernon-
court, Tong Yu, Ruiyi Zhang, and Nesreen K Ahmed. Bias and fairness in large language models:
A survey. Computational Linguistics, 50(3):1097–1179, 2024.
Todd A Gormley, Mahsa Kaviani, and Hosein Maleki. When do judges throw the book at com-
panies? the influence of partisanship in corporate prosecutions. Review of Financial Studies,
2025.
Soumyajit Gupta, Maria De-Arteaga, and Matthew Lease. Fairly Accurate: Fairness-aware Multi-
group Target Detection in Online Discussion. arXiv preprint arXiv:2407.11933, 2024. URL
https://arxiv.org/abs/2407.11933. Version 2, submitted June 2025.
Jennifer Healey, Laurie Byrum, Md Nadeem Akhtar, and Moumita Sinha. Evaluating nuanced bias
in large language model free response answers. In International Conference on Applications of
Natural Language to Information Systems, pp. 378–391. Springer, 2024.
Yue Hou and Rory Truex. Ethnic discrimination in criminal sentencing in china. The Journal of
Politics, 84(4):2294–2299, 2022.
Yongming Huang and Yanan Zhang. Digitalization, positioning in global value chain and carbon
emissions embodied in exports: Evidence from global manufacturing production-based emis-
sions. Ecological Economics, 205:107674, 2023.
Jize Jiang and Kai Kuang. Hukou status and sentencing in the wake of internal migration: The
penalty effect of being rural-to-urban migrants in china. Law & Policy, 40(2):196–215, 2018.
Brian D Johnson. The multilevel context of criminal sentencing: Integrating judge-and county-level
influences. Criminology, 44(2):259–298, 2006.
Svetlana Kiritchenko and Saif M Mohammad. Examining gender and race bias in two hundred
sentiment analysis systems. arXiv preprint arXiv:1805.04508, 2018.
Aobo Kong, Shiwan Zhao, Hao Chen, Qicheng Li, Yong Qin, Ruiqi Sun, Xin Zhou, Enzhi Wang,
and Xiaohang Dong.
Better zero-shot reasoning with role-play prompting.
arXiv preprint
arXiv:2308.07702, 2023.
Joshua Krook, Eike Schneiders, Tina Seabrooke, Natalie Leesakul, and Jeremie Clos. Large lan-
guage models (llms) for legal advice: A scoping review. Available at SSRN 4976189, 2024.
Shachi H Kumar, Saurav Sahay, Sahisnu Mazumder, Eda Okur, Ramesh Manuvinakurike, Nicole
Beckage, Hsuan Su, Hung-yi Lee, and Lama Nachman. Decoding biases: Automated methods
and llm judges for gender bias detection in language models. arXiv preprint arXiv:2408.03907,
2024.
Lucio La Cava and Andrea Tagarelli. Open models, closed minds? on agents capabilities in mimick-
ing human personalities through open large language models. arXiv preprint arXiv:2401.07115,
2024.
13

--- Page 14 ---

Working Paper
Qingquan Li, Yiran Hu, Feng Yao, Chaojun Xiao, Zhiyuan Liu, Maosong Sun, and Weixing Shen.
Muser: A multi-view similar case retrieval dataset. In Proceedings of the 32nd ACM International
Conference on Information and Knowledge Management, pp. 5336–5340, 2023a.
Yongqi Li, Mayi Xu, Xin Miao, Shen Zhou, and Tieyun Qian. Prompting large language models for
counterfactual generation: An empirical study. arXiv preprint arXiv:2305.14791, 2023b.
Do Xuan Long, Hai Nguyen Ngoc, Tiviatis Sim, Hieu Dao, Shafiq Joty, Kenji Kawaguchi, Nancy F
Chen, and Min-Yen Kan. Llms are biased towards output formats! systematically evaluating and
mitigating output format bias of llms. arXiv preprint arXiv:2408.08656, 2024.
Felipe Lopes. Television and judicial behavior: lessons from the brazilian supreme court. Economic
Analysis of Law Review, 9(1):41–71, 2018.
Christopher J Marier, John K Cochran, M Dwayne Smith, Sondra J Fogel, and Beth Bjerregaard.
Victim age and capital sentencing outcomes in north carolina (1977–2009). Criminal justice
studies, 31(1):62–79, 2018.
Monica L McCoy and Jennifer M Gray. The impact of defendant gender and relationship to victim
on juror decisions in a child sexual abuse case. Journal of Applied Social Psychology, 37(7):
1578–1593, 2007.
Maril`u Miotto, Nicola Rossberg, and Bennett Kleinberg. Who is gpt-3? an exploration of personal-
ity, values and demographics. arXiv preprint arXiv:2209.14338, 2022.
Kyle Moore, Jesse Roberts, Thao Pham, and Douglas Fisher. Reasoning beyond bias: A study
on counterfactual prompting and chain of thought reasoning. arXiv preprint arXiv:2408.08651,
2024.
Ali Hakimi Parizi, Yuyang Liu, Prudhvi Nokku, Sina Gholamian, and David Emerson. A compara-
tive study of prompting strategies for legal text classification. In Proceedings of the Natural Legal
Language Processing Workshop 2023, pp. 258–265, 2023.
Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana Thomp-
son, Phu Mon Htut, and Samuel Bowman.
BBQ: A hand-built bias benchmark for ques-
tion answering.
In Findings of the Association for Computational Linguistics: ACL 2022,
pp. 2086–2105, Dublin, Ireland, May 2022. Association for Computational Linguistics.
doi:
10.18653/v1/2022.findings-acl.165. URL https://aclanthology.org/2022.findings-acl.165.
Andrea Pinto, Tomer Galanti, and Randall Balestriero. The fair language model paradox. arXiv
preprint arXiv:2410.11985, 2024.
Joanna D Pozzulo, Julie Dempsey, Evelyn Maeder, and Laura Allen. The effects of victim gender,
defendant gender, and defendant age on juror decision making. Criminal Justice and Behavior,
37(1):47–63, 2010.
Rebecca Qian, Candace Ross, Jude Fernandes, Eric Smith, Douwe Kiela, and Adina Williams.
Perturbation augmentation for fairer nlp. arXiv preprint arXiv:2205.12586, 2022.
Victor D Quintanilla, Rachel A Allen, and Edward R Hirt. The signaling effect of pro se status. Law
& Social Inquiry, 42(4):1091–1121, 2017.
Chahat Raj, Anjishnu Mukherjee, Aylin Caliskan, Antonios Anastasopoulos, and Ziwei Zhu. Break-
ing bias, building bridges: Evaluation and mitigation of social biases in llms via contact hypoth-
esis. In Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society, volume 7, pp.
1180–1189, 2024.
Rajesh Ranjan, Shailja Gupta, and Surya Narayan Singh. A comprehensive survey of bias in llms:
Current landscape and future directions. arXiv preprint arXiv:2409.16430, 2024.
John Rawls. Atheory of justice. Cambridge (Mass.), 1971.
Rachel Rudinger, Jason Naradowsky, Brian Leonard, and Benjamin Van Durme. Gender bias in
coreference resolution. arXiv preprint arXiv:1804.09301, 2018.
14

--- Page 15 ---

Working Paper
Aleix Sant, Carlos Escolano, Audrey Mash, Francesca De Luca Fornaciari, and Maite Melero.
The power of prompts: Evaluating and mitigating gender bias in mt with llms. arXiv preprint
arXiv:2407.18786, 2024.
Stephen J Schulhofer. Assessing the federal sentencing process: The problem is uniformity, not
disparity. Am. Crim. L. Rev., 29:833, 1991.
Dietrich Trautmann, Alina Petrova, and Frank Schilder. Legal prompt engineering for multilingual
legal judgement prediction. arXiv preprint arXiv:2212.02199, 2022.
Jeffery T Ulmer. Recent developments and new directions in sentencing research. Justice Quarterly,
29(1):1–40, 2012.
Jeremy Waldron. The rule of law and the importance of procedure. Getting to the Rule of Law, 3:
4–5, 2011.
Kellie Webster, Marta Recasens, Vera Axelrod, and Jason Baldridge. Mind the gap: A balanced
corpus of gendered ambiguous pronouns. Transactions of the Association for Computational
Linguistics, 6:605–617, 2018.
Bao Wu, Feng Chen, Lanhua Li, Lei Xu, Zijia Liu, and Yaoyao Wu. Institutional investor esg
activism and exploratory green innovation: Unpacking the heterogeneous responses of family
firms across intergenerational contexts. The British Accounting Review, pp. 101324, 2024.
Chaojun Xiao, Haoxi Zhong, Zhipeng Guo, Cunchao Tu, Zhiyuan Liu, Maosong Sun, Yansong
Feng, Xianpei Han, Zhen Hu, Heng Wang, et al. Cail2018: A large-scale legal dataset for judg-
ment prediction. arXiv preprint arXiv:1807.02478, 2018.
Rongwu Xu, Zi’an Zhou, Tianwei Zhang, Zehan Qi, Su Yao, Ke Xu, Wei Xu, and Han Qiu. Walking
in others’ shoes: How perspective-taking guides large language models in reducing toxicity and
bias. arXiv preprint arXiv:2407.15366, 2024.
Zongyue Xue, Huanghai Liu, Yiran Hu, Yuliang Qian, Yajing Wang, Kangle Kong, Chenlu Wang,
Yun Liu, and Weixing Shen. Leec for judicial fairness: A legal element extraction dataset with
extensive extra-legal labels. In Proceedings of the Thirty-Third International Joint Conference on
Artificial Intelligence, IJCAI-24, pp. 7527–7535, 2024.
Feng Yao, Chaojun Xiao, Xiaozhi Wang, Zhiyuan Liu, Lei Hou, Cunchao Tu, Juanzi Li, Yun Liu,
Weixing Shen, and Maosong Sun. Leven: A large-scale chinese legal event detection dataset.
arXiv preprint arXiv:2203.08556, 2022.
Sangwon Yu, Jongyoon Song, Bongkyu Hwang, Hoyoung Kang, Sooah Cho, Junhwa Choi, Seongho
Joe, Taehee Lee, Youngjune L Gwon, and Sungroh Yoon.
Correcting negative bias in large
language models through negative attention score alignment. arXiv preprint arXiv:2408.00137,
2024.
Ruizhe Zhang, Haitao Li, Yueyue Wu, Qingyao Ai, Yiqun Liu, Min Zhang, and Shaoping Ma.
Evaluation ethics of llms in legal domain. arXiv preprint arXiv:2403.11152, 2024a.
Yifan Zhang. Meta prompting for agi systems. arXiv preprint arXiv:2311.11482, 2023.
Yubo Zhang, Shudi Hou, Mingyu Derek Ma, Wei Wang, Muhao Chen, and Jieyu Zhao. Climb: A
benchmark of clinical bias in large language models. arXiv preprint arXiv:2407.05250, 2024b.
Hui Zhong, Songsheng Chen, and Mian Liang. Gender bias of llm in economics: An existentialism
perspective. arXiv preprint arXiv:2410.19775, 2024.
15

--- Page 16 ---

Working Paper
TABLE OF CONTENTS FOR APPENDIX
A Related Works (Detailed)
17
A.1
Fairness Evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
17
A.2
Legal Datasets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
18
B
Label System (Detailed)
19
C Prompt Standardization
20
C.1
LLM Inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
C.2
Prompt Evaluation
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
D Overall Information of Models, Labels, and Results
23
D.1
Model Information
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
23
D.2
Summarized Label Information and Definition . . . . . . . . . . . . . . . . . . . .
24
D.3
Details on Labels and Trigger Sentences and Excluded Cases . . . . . . . . . . . .
28
D.4
Overall Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
40
E
Detailed Results of Bias Analysis
42
E.1
Heatmap of Bias Analysis Results . . . . . . . . . . . . . . . . . . . . . . . . . .
42
E.2
Number of Labels with Statistically Significant Results in Bias Analysis . . . . . .
45
E.3
Detailed Information of Labels with Statistically Significant Results in Bias Analysis
47
E.4
Robustness Checks on Bias Analysis . . . . . . . . . . . . . . . . . . . . . . . . .
54
F
Detailed Results of Imbalanced Inaccuracy Analysis
63
F.1
Number of Labels with Statistically Significant Results in Imbalanced Inaccuracy
Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
63
F.2
Detailed of Labels with Statistically Significant Results in Imbalanced Inaccuracy
Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
65
G Correlation Analysis
71
G.1
Correlations among Evaluation Metrics
. . . . . . . . . . . . . . . . . . . . . . .
71
G.2
Correlations between Temperature and Evaluation Metrics
. . . . . . . . . . . . .
72
G.3
Correlations between Model Release Date and Evaluation Metrics . . . . . . . . .
72
G.4
Correlations between Model Size and Evaluation Metrics . . . . . . . . . . . . . .
73
G.5
Correlations between a Model’s Country of Origin and Evaluation Metrics . . . . .
74
16

--- Page 17 ---

Working Paper
A
RELATED WORKS (DETAILED)
A.1
FAIRNESS EVALUATION
Fairness evaluation serves as a crucial component in the development of trustworthy LLMs. A
myriad of benchmarks exist to measure the bias of large language models, each with its unique
focus. We’ve categorized these biases into two types: human-related problems and LLM-related
problems.
Some studies concentrate on detecting LLM-related bias, which means those challenges are unique
to LLMs. The temperature parameter can affect an LLM’s self-perception of attributes such as
age, gender (Miotto et al., 2022), and personality (La Cava & Tagarelli, 2024). Weight decay may
influence how LLMs handle low-frequency tokens, raising fairness concerns (Pinto et al., 2024).
Studies have also shown that LLMs sometimes produce negative responses in complex reasoning
tasks for unknown reasons (Yu et al., 2024). Requiring specific output formats may also impact
LLM performance, possibly due to extensive training on structured coding data (Long et al., 2024).
These benchmarks are relatively straightforward to construct and are limited to the scenarios models
encounter. While previous work in this area is well-developed, more value and opportunities for
improvement lie in addressing human-related problems.
LLMs often reflect human-like behavior patterns. Societal and structural biases present in human-
generated data can lead to unfair LLM outputs (Dastin, 2018). In past research on human-related
problems, researchers have primarily focused on social fairness. For example, many researchers
primarily focus on evaluating gender bias. Winogender (Rudinger et al., 2018) evaluates gender
stereotypes using a collection of 3,160 sentences that cover 40 different professions. GAP, developed
by (Webster et al., 2018), provides 8,908 ambiguous pronoun-name pairs to evaluate gender bias in
coreference resolution tasks. At the same time, other research efforts have expanded their focus to
include a broader range of social factors. The Equity Evaluation Corpus, created by (Kiritchenko &
Mohammad, 2018), comprises 8,640 sentences that analyze sentiment variations towards different
gender and racial groups. PANDA, introduced by (Qian et al., 2022), presents a dataset of 98,583
text perturbations across gender, race/ethnicity, and age groups, where each pair of sentences alters
the social group but maintains the same semantic meaning. Lastly, the Bias Benchmark for QA
(BBQ) (Parrish et al., 2022), is a question-answering dataset consisting of 58,492 examples that aim
to evaluate bias across nine social categories, including age, disability status, gender, nationality,
physical appearance, race/ethnicity, religion, and socioeconomic status.
A minority of studies also evaluate fairness in domain-specific contexts. Bang et al. (2024) pro-
posed a fine-grained framework to measure political bias in LLMs by analyzing both stance and
framing—what the model says and how it says it—across diverse political topics. Zhong et al.
(2024) demonstrated that LLMs like GPT-4 and BERT exhibit systematic gender bias in financial
decision-making tasks, highlighting the limitations of purely technical debiasing. Deroy & Maity
(2023) examined LLM biases on gender, race, country and religion in automated case judgment
summaries. However, the study lacked the use of statistical tools for drawing robust inferences, and
its evaluation focused solely on bias, overlooking other critical dimensions of LLM fairness. Zhang
et al. (2024a) proposed an ethics-focused evaluation methodology using real-world legal cases to
assess the legal knowledge and ethical robustness of LLMs in the legal domain. However, the study
relied on only 11 judicial documents without robust statistical inferences, which is far too limited to
support convincing evaluation and conclusions.
Overall, these studies are subject to several important limitations. First, existing studies on LLM
bias—whether in general or domain-specific tasks—rely on at most nine labels, a scope that is
neither comprehensive nor methodologically systematic. Second, when evaluating multiple labels
across multiple models, researchers need to conduct experiments over and over again. Prior studies
on LLM fairness have largely overlooked a critical question: How can we distinguish genuine fair-
ness problems from observed patterns that may arise purely due to random noise in the data through
repeated experimentation? Without rigorous statistical inference, such distinctions remain unclear.
Third, many studies failed to recognize that fairness is a broader, multidimensional concept com-
pared with bias. The evaluation of fairness necessitates a comprehensive framework and must not
be conflated with bias, which represents only one aspect of fairness Binns (2018). Thus, it is not
surprising that Blodgett et al. (2021) pointed out that several benchmarks suffer from unclear bias
definitions and issues with the validity of bias. Fourth, while some LLMs apply debiasing tech-
17

--- Page 18 ---

Working Paper
niques during post-training (Raj et al., 2024; Xu et al., 2024), ensuring fairness in judicial contexts
presents unique challenges due to the need for deep legal understanding. The high stakes of judicial
decisions further heighten the standards required for fairness. If LLMs can meet these standards and
deliver just outcomes comparable to human judges, the pursuit of social justice would be signifi-
cantly advanced. Lastly, auditing LLM fairness should not end with a published paper. A practical,
academically grounded toolkit is essential to support broad-based evaluation and ongoing improve-
ment of LLM fairness, particularly when evaluating LLM fairness is a complicated task that requires
multi-dimensional, statistically rigorous methodology.
In our work, we introduce the concept of judicial fairness and systematically construct a fairness
evaluation framework for LLM’s judicial fairness. Based on this framework, we propose 65 labels,
far more than 1-9 labels in previous works, to comprehensively assess the judicial fairness of large
language models.
A.2
LEGAL DATASETS
In order to evaluate judicial fairness, it is crucial to place Large Language Models within legal
contexts. There are several existing legal NLP datasets that have annotated legal cases, primarily
analyzing human judgment outcomes. For instance, there are datasets like LEEC(Xue et al., 2024),
MUSER(Li et al., 2023a), CAIL2018(Xiao et al., 2018), and LEVEN(Yao et al., 2022).
CAIL2018 (Xiao et al., 2018) contains over 2.6 million criminal cases published by the Supreme
People’s Court of China. However, its annotations merely cover legal articles, charges, and prison
terms, without providing detailed facts of the cases.
LEVEN (Yao et al., 2022), on the other hand, is a large-scale Chinese Legal Event detection dataset,
comprising 8,116 legal documents and 150,977 human-annotated event mentions across 108 event
types. Yet, for fairness evaluation, the provided legal event labels alone are insufficient.
LEEC (Xue et al., 2024) is another Chinese legal dataset consisting of 15,919 legal documents and
155 extra-legal factor labels. As pointed out by Ulmer in 2012, the practical application of the law
is significantly influenced not only by legal factors but also by extra-legal ones. The comprehensive
label system, the large number of cases as well as the introduce of extra-legal labels ensure the
reliability of the dataset for research into model judicial fairness.
All these previous works rely exclusively on human judgments. However, to evaluate the judicial
fairness of large language models (LLMs), we propose repurposing existing legal datasets by treating
LLMs as the judicial decision-makers. Researchers can generate counterfactual prompts from real
judicial documents, enabling rigorous causal inference regarding fairness issues in LLM predictions.
Consequently, developing a specialized dataset designed explicitly for evaluating judicial fairness in
LLMs is essential.
18

--- Page 19 ---

Working Paper
B
LABEL SYSTEM (DETAILED)
Our team of legal experts developed a comprehensive system comprising 65 labels for each of the
four categories outlined in the proposed fairness framework. Our annotation team contains 3 legal
experts, they all owns the Master of Law degree in China. When annotating, they get paid by $10
per hour. By judging each label, they first give their own choice. If they encounter inconsistent
results, they make a decision through voting after negotiation.
Detailed information about these labels is presented in Table A2 to Table A5.
This labeling system builds upon the existing LEEC dataset (Xue et al., 2024), which includes 155
manually annotated legal and extra-legal labels, along with the corresponding trigger sentences that
may influence sentencing outcomes across a vast collection of Chinese judicial documents. The la-
bels in the LEEC dataset were selected by legal experts and informed by a comprehensive review of
empirical legal studies specific to the Chinese context. This expert-driven approach ensures that the
extra-legal labels are highly relevant and likely to impact judicial decisions in practice. For instance,
whether the defendant is represented by legal aid lawyers or private attorneys can significantly in-
fluence sentencing outcomes (Agan et al., 2021). This label is annotated in the LEEC dataset and is
also included in the current system to examine its potential impact on LLM decisions. As a result,
the LEEC dataset provides a solid foundation for label selection and data construction, as discussed
in Section 4.2. It also enables us to explore potential relationships between fairness issues in real
judicial documents and those in LLM decision-making.
However, when examining LLM fairness, we are not strictly limited to the information explicitly
recorded in judicial documents, as is the case with LEEC. For instance, sexual orientation is widely
recognized as a significant source of bias and stereotype in judicial decision-making, yet it is not
typically documented in Chinese judicial records. Consequently, LEEC is unable to account for
this important factor. Similarly, information regarding parties other than the defendant—such as
judges, juries, and victims—is largely absent from real judicial documents. To address these gaps,
we incorporated additional labels to cover critical attributes missing from judicial records. This
expansion significantly broadens the scope of LLM fairness evaluation.
Specifically, substance factors include demographic labels for defendants and victims, as well as
non-demographic extra-legal factors such as crime date, time, and location. The labels selected
from LEEC include various defendant demographic factors like sex, ethnicity, education level, age,
and more. Procedure factors encompass demographic information for defenders, prosecutors, and
judges.8 As these procedural demographic labels are not available in real judicial documents or
LEEC, we added them to our system. For procedural non-demographic factors, we included ele-
ments from LEEC, such as whether a recusal is applied by the defendant, whether a supplementary
civil action is initiated with the criminal case. For critical factors not typically recorded in judicial
documents, we supplemented our label system to include crucial procedure elements such as whether
the trial is open to the public, whether it is broadcast online, the duration of the trial process, whether
the judgment is delivered immediately following the trial, etc. Overall, our approach allows us to
capture a broader range of procedural fairness considerations in LLM fairness evaluation.
8For prosecutors and judges, we exclude labels like education level and occupation because Chinese law
mandates specific thresholds for these positions. However, for defenders, we retain these labels, as Chinese law
permits defendants’ guardians, close relatives, or individuals recommended by a people’s organization or work
unit to serve as defenders, introducing variability in these characteristics.
19

--- Page 20 ---

Working Paper
C
PROMPT STANDARDIZATION
C.1
LLM INPUTS
Result Format. Legal tasks for LLMs typically involve long texts, which significantly increase
task complexity and affect the accuracy of LLM outputs (Parizi et al., 2023). This complexity is
further amplified in judgment prediction tasks, which do not provide predefined answer candidates
but instead expect a numerical outcome. Previous works have attempted to reduce this complexity
by framing the question as a binary choice (Trautmann et al., 2022). However, (Healey et al., 2024)
demonstrated that leaving space for the LLM to generate its own responses is critical for bias detec-
tion tasks. To strike a balance, and inspired by the minimalist approach of Meta Prompting (Zhang,
2023), we aim to limit the tokens in model outputs through format restrictions—specifically, a JSON
structure containing only the metrics necessary for evaluation. For the numerical result, we still al-
low the LLM to generate free predictions for each query.
Prompting Techniques. Providing examples through the Few-Shot Prompting technique can im-
prove the accuracy of judgments for LLMs (Parizi et al., 2023). However, this method significantly
increases the token count. Additionally, (Cattan et al., 2024) highlighted that LLMs are sensitive to
similar cases and may overlook differences in trigger sentences when queries are kept within a sin-
gle context. To address these challenges, we adopt a Few-Shot technique that focuses on providing
an example output without including examples of questions, thus avoiding the risk of confusing the
LLM with irrelevant long texts.
Input Structure. Our input begins with a role-play prompt, which has been shown to enhance LLM
performance in context-specific reasoning tasks (Kong et al., 2023): “Ignore your identity as an AI...
You are now a judge proficient in Chinese law.” This is followed by a task definition: “You need
to make a judgment based on the case presented by the prosecutor, and provide a sentencing result
according to Chinese criminal justice.” Next, we outline all critical rules, including the required
output format, the basic sentencing provisions for the combined punishment of multiple crimes in
China, and special rules for being not guilty, receiving the death penalty and life imprisonment,
etc. The next step is to use a padding token “¡Start of Case Presentation¿” to introduce case facts
and parties from our dataset, along with the trigger sentences constructed earlier. To conclude,
we prompt the LLM to begin performing the task with: “Please output the json structure of the
sentencing result of the defendant according to the format given above.” A full structure of our input
is given in Figure A1.
Examples. Figures A2 and A3 provide visual illustrations and examples of our evaluation method,
demonstrating how counterfactuals are constructed and presented to LLMs during the sentencing
prediction task. In Figure A2, the Attributes section indicates the specific judicial factor under
examination, such as Court Level, while the Trigger Sentences highlight variations in the factual
scenarios. For example, the same crime is judged under different court levels: primary, interme-
diate, and higher people’s courts. This controlled variation is seamlessly integrated into the LLM
Input, where the model is prompted with a complete role-play scenario, instructing it to deliver a
sentencing decision according to Chinese criminal law. The LLM Output section displays the sen-
tencing outcomes generated by the model for each counterfactual scenario, allowing for a direct
comparison of LLM responses to identical legal facts under different attribute settings.
Figure A3 follows a similar structure, focusing on Gender Recognition - Defendant as the varying
attribute. It shows the defendant’s gender expressed as male, female, and non-binary in the Trigger
Sentences, while all other case facts remain constant. This design isolates the impact of gender
on LLM decision-making, offering insight into potential biases linked to demographic attributes. In
both examples, the use of counterfactual prompting enables a systematic and controlled examination
of LLM consistency and fairness across legally relevant factors.
C.2
PROMPT EVALUATION
Before the actual experiment, the prompt is evaluated on a selective set of LLMs. The evaluation
focuses on the cohesion with which the LLM adheres to the format requirements and the potential
variations the prompt might generate. Each query is run three times to assess the extent of variation,
with a total of 420 queries completed. Based on the outputs observed, we consider the final prompt
competent for the task and proceed to construct the dataset for LLM inputs.
20

--- Page 21 ---

Working Paper
Figure A1: Construction of our inputs.
21

--- Page 22 ---

Working Paper
Figure A2: Examples of our evaluation method (I).
Figure A3: Examples of our evaluation method (II).
22

--- Page 23 ---

Working Paper
D
OVERALL INFORMATION OF MODELS, LABELS, AND RESULTS
D.1
MODEL INFORMATION
Table A1 provides an overview of the models used in our evaluation, organized in chronological
order based on their release dates. For each model, the table lists the model name, publication date,
parameter count, and the nation of origin. Models with ”Unknown” parameter counts indicate pro-
prietary or undisclosed information at the time of evaluation. We intentionally selected a diverse set
of models spanning different nations, release dates, and parameter sizes to ensure a comprehensive
evaluation of LLM fairness across various configurations.
Model Name
Publication Date
Parameter Count
Nation
Glm 4
2024-01-16
Unknown
China
Gemini Flash 1.5
2024-05-14
Unknown
U.S.
Mistral Nemo
2024-07-19
12B
U.S.
Llama 3.1 8B Instruct
2024-07-23
8B
U.S.
Glm 4 Flash
2024-08-27
9B
China
Qwen2.5 72B Instruct
2024-09-19
72B
China
LFM 40B MoE
2024-09-30
40B
U.S.
Gemini Flash 1.5 8B
2024-10-03
8B
U.S.
Qwen2.5 7B Instruct
2024-10-19
7B
China
Nova Lite 1.0
2024-12-04
Unknown
U.S.
Nova Micro 1.0
2024-12-05
Unknown
U.S.
DeepSeek V3
2024-12-26
671B
China
Phi 4
2025-01-10
14B
U.S.
DeepSeek R1-32B Qwen
2025-01-20
32B
China
LFM 7B
2025-01-25
7B
U.S.
Mistral Small 3
2025-01-30
24B
France
Table A1: Overall information of models.
23

--- Page 24 ---

Working Paper
D.2
SUMMARIZED LABEL INFORMATION AND DEFINITION
Table A2 to Table A5 summarize the label names, label definitions, and the values of the labels.
Label Name
Label Description
Label Value
Substance and Demographic Factors
Defendant gender
A DEFENDANT GENDER element refers to
the gender of the defendant.
Female;
Gender Non-
Binary;
Male
(Refer-
ence)
Defendant sexual orientation
A
DEFENDANT SEXUAL ORIENTATION
element refers to the sexual orientation of the
defendant.
Homosexual;
Bisexual;
Heterosexual
(Refer-
ence)
Defendant ethnicity
A DEFENDANT ETHNICITY element refers
to the ethnicity of the defendant.
Ethnic
Minority;
Han
(Reference)
Defendant age
A DEFENDANT AGE element refers to the
age of the defendant.
Age
Defendant education
A
DEFENDANT EDUCATION
element
refers to the education level of the defendant
Below
High
School;
High School or Above
(Reference)
Defendant occupation
A
DEFENDANT OCCUPATION
element
refers to the occupation of the defendant
categorized into three types.
Farmer;
Unemployed;
Worker (Reference)
Defendant household regist
ration
A DEFENDANT HOUSEHOLD REGISTR
ATION element refers to the place of regis-
tered permanent residence of the defendant,
also known as Hukou in Chinese.
Not Local; Local (Refer-
ence)
Defendant nationality
A
DEFENDANT NATIONALITY
element
refers to the nationality of the defendant.
Foreigner; Chinese (Ref-
erence)
Defendant political backgr
ound
A DEFENDANT POLITICAL BACKGROU
ND element refers to the poltical background
of the defendant.
CCP; Other Party; Mass
(Reference)
Defendant religion
A DEFENDANT RELIGION element refers
to the religious belief of the defendant
Islam; Buddhism; Chris-
tianity; Atheism (Refer-
ence)
Defendant wealth
A DEFENDANT WEALTH element refers to
the financial status of the defendant
Penniless;
A
Million
Saving (Reference)
Victim gender
A VICTIM GENDER element refers to the
gender of the victim.
Female;
Gender Non-
Binary;
Male
(Refer-
ence)
Victim sexual orientation
A
VICTIM SEXUAL ORIENTATION
ele-
ment refers to the sexual orientation of the vic-
tim.
Homosexual;
Bisexual;
Heterosexual
(Refer-
ence)
Victim ethnicity
A VICTIM ETHNICITY element refers to the
ethnicity of the victim.
Ethnic
Minority;
Han
(Reference)
Victim age
A VICTIM AGE element refers to the age of
the victim.
Age
Victim education
A VICTIM EDUCATION element refers to
the education level of the victim.
Below
High
School;
High School or Above
(Reference)
Victim occupation
A VICTIM OCCUPATION element refers to
the occupation of the victim categorized into
three types.
Farmer;
Unemployed;
Worker (Reference)
Victim household registration A VICTIM HOUSEHOLD REGISTRATION
element refers to the place of registered per-
manent residence of the victim, also known as
Hukou in Chinese.
Not Local; Local (Refer-
ence)
Table A2: List of summarized label information and definition (I).
24

--- Page 25 ---

Working Paper
Label Name
Label Description
Label Value
Victim nationality
A VICTIM NATIONALITY element refers
to the nationality of the victim.
Foreigner;
Chinese
(Reference)
Victim political background
A VICTIM POLITICAL BACKGROUND
element refers to the political background of
the victim.
CCP; Other Party; Mass
(Reference)
Victim religion
A VICTIM RELIGION element refers to the
religious belief of the victim.
Islam;
Buddhism;
Christianity;
Atheism
(Reference)
Substance and Non-Demographic Factors
Victim wealth
A VICTIM WEALTH element refers to the
financial status of the victim.
Penniless;
A Million
Saving (Reference)
Crime location
A CRIME LOCATION element refers to the
location where the crime took place.
Rural;
Urban (Refer-
ence)
Crime date
A CRIME DATE element refers to the sea-
son in which the crime occurred.
Summer;
Autumn;
Winter; Spring (Refer-
ence)
Crime time
A CRIME TIME element refers to the time
of day when the crime occurred.
Afternoon;
Morning
(Reference)
Procedure and Demographic Factors
Defender gender
A DEFENDER GENDER element refers to
the gender of the defender.
Female; Gender Non-
Binary;
Male (Refer-
ence)
Defender sexual orientation
A DEFENDER SEXUAL ORIENTATION
element refers to the sexual orientation of the
defender.
Homosexual; Bisexual;
Heterosexual
(Refer-
ence)
Defender ethnicity
A DEFENDER ETHNICITY element refers
to the ethnicity of the defender.
Ethnic Minority;
Han
(Reference)
Defender age
A DEFENDER AGE element refers to the
age of the defender.
Age
Defender education
A
DEFENDER EDUCATION
element
refers to the education level of the defender.
Below
High
School;
High School or Above
(Reference)
Defender occupation
A
DEFENDER OCCUPATION
element
refers to the occupation of the defender
categorized into three types.
Farmer;
Unemployed;
Worker (Reference)
Defender household registr
ation
A DEFENDER HOUSEHOLD REGISTR
ATION element refers to the place of reg-
istered permanent residence of the defender,
also known as Hukou in Chinese.
Not Local; Local (Ref-
erence)
Defender nationality
A
DEFENDER NATIONALITY
element
refers to the nationality of the defender.
Foreigner;
Chinese
(Reference)
Defender political backgro
und
A DEFENDER POLITICAL BACKGRO
UND element refers to the political back-
ground of the defender.
CCP; Other Party; Mass
(Reference)
Defender religion
A DEFENDER RELIGION element refers
to the religious belief of the defender.
Islamic;
Buddhism;
Christianity;
Atheism
(Reference)
Defender wealth
A DEFENDER WEALTH element refers to
the financial status of the defender.
Penniless;
A Million
Saving (Reference)
Prosecurate gender
A
PROSECURATE GENDER
element
refers to the gender of the prosecutor.
Female; Gender Non-
Binary;
Male (Refer-
ence)
Prosecurate sexual orientati
on
A PROSECURATE SEXUAL ORIENTAT
ION element refers to the sexual orientation
of the prosecutor.
Homosexual; Bisexual;
Heterosexual
(Refer-
ence)
Prosecurate ethnicity
A PROSECURATE ETHNICITY element
refers to the ethnicity of the prosecutor.
Ethnic Minority;
Han
(Reference)
Table A3: List of summarized label information and definition (II).
25

--- Page 26 ---

Working Paper
Label Name
Label Description
Label Value
Prosecurate age
A PROSECURATE AGE element refers to the
age of the prosecutor.
Age
Prosecurate household regi
stration
A PROSECURATE HOUSEHOLD REGIST
RATION element refers to the place of regis-
tered permanent residence of the prosecutor.
Not Local; Local (Refer-
ence)
Prosecurate political backg
round
A PROSECURATE POLITICAL BACKGR
OUND element refers to the political back-
ground of the prosecutor.
CCP; Other Party; Mass
(Reference)
Prosecurate religion
A
PROSECURATE RELIGION
element
refers to the religious belief of the prosecutor.
Islamic;
Buddhism;
Christianity;
Atheism
(Reference)
Prosecurate wealth
A PROSECURATE WEALTH element refers
to the financial status of the prosecutor.
Penniless;
A
Million
Saving (Reference)
Judge gender
A JUDGE GENDER element refers to the gen-
der of the presiding judge.
Female;
Gender Non-
Binary;
Male
(Refer-
ence)
Judge sexual orientation
A JUDGE SEXUAL ORIENTATION element
refers to the sexual orientation of the presiding
judge.
Homosexual;
Bisexual;
Heterosexual
(Refer-
ence)
Judge ethnicity
A JUDGE ETHNICITY element refers to the
ethnicity of the presiding judge.
Ethnic
Minority;
Han
(Reference)
Judge age
A JUDGE AGE element refers to the age of the
presiding judge.
Age
Judge household registratio
n
A JUDGE HOUSEHOLD REGISTRATION
element refers to the place of registered perma-
nent residence of the presiding judge.
Not Local; Local (Refer-
ence)
Judge political background
A JUDGE POLITICAL BACKGROUND el-
ement refers to the political background of the
presiding judge.
CCP; Other Party; Mass
(Reference)
Judge religion
A JUDGE RELIGION element refers to the re-
ligious belief of the presiding judge.
Islamic;
Buddhism;
Christianity;
Atheism
(Reference)
Judge wealth
A JUDGE WEALTH element refers to the fi-
nancial status of the presiding judge.
Penniless;
A
Million
Saving (Reference)
Procedure and Non-Demographic Factors
Compulsory measure
A COMPULSORY MEASURE element refers
to judicially imposed restrictions on the per-
sonal freedom of criminal suspects or defen-
dants.
Compulsory
Measure;
No
Compulsory
Mea-
sure (Reference)
Court level
A COURT LEVEL element refers to the hier-
archical classification of the court adjudicating
the case.
Intermediate Court; High
Court;
Primary
Court
(Reference)
Court location
A COURT LOCATION element refers to the
geographical jurisdiction of the court handling
the case.
Rural;
Urban
(Refer-
ence)
Collegial panel
A COLLEGIAL PANEL element refers to
whether the case is adjudicated by a panel of
judges or a single judge.
Collegial Panel; Single
Judge (Reference)
Assessor
An ASSESSOR element refers to whether the
trial includes assessors.
No People’s Assessor;
With People’s Assessor
(Reference)
Pretrial conference
A PRETRIAL CONFERENCE element refers
to whether the court determined that a pretrial
conference for a case should be held.
With
Pretrial
Con-
ference;
No
Pretrial
Conference (Reference)
Pretrial conference
A PRETRIAL CONFERENCE element refers
to whether the court determined that a pretrial
conference for a case should be held.
With
Pretrial
Con-
ference;
No
Pretrial
Conference (Reference)
Table A4: List of summarized label information and definition (III).
26

--- Page 27 ---

Working Paper
Label Name
Label Description
Label Value
Online broadcast
An ONLINE BROADCAST element refers to
whether the trial proceedings were publicly
broadcasted online.
Online Broadcast;
No
Online Broadcast (Refer-
ence)
Open trial
An OPEN TRIAL element refers to whether
the court conducted the trial in an open session
accessible to the public.
Open Trial; Not Open
Trial (Reference)
Defender type
A
DEFENDER TYPE
element
refers
to
whether the defendant was represented by a
court-appointed counsel or a privately retained
attorney.
Appointed
Defender;
Privately Attained De-
fender (Reference)
Recusal applied
A RECUSAL APPLIED element refers to
whether a motion for judicial recusal was filed
in the case.
Recusal
Applied;
No
Recusal Applied (Refer-
ence)
Judicial committee
A JUDICIAL COMMITTEE element refers to
whether the court submitted the case to the ju-
dicial committee for discussion.
With Judicial Commit-
tee; No Judicial Commit-
tee (Reference)
Litigation Duration
A LITIGATION DURATION element refers
to the length of the trial proceedings.
Prolonged
Litigation;
Short Litigation (Refer-
ence)
Immediate judgement
An
IMMEDIATE JUDGEMENT
element
refers to whether the court rendered a judg-
ment immediately after the trial.
Immediate
Judgement;
Not Immediate Judge-
ment (Reference)
Table A5: List of summarized label information and definition (IV).
27

--- Page 28 ---

Working Paper
D.3
DETAILS ON LABELS AND TRIGGER SENTENCES AND EXCLUDED CASES
Table A6 to Table A16 present the label names, the values of the labels, corresponding trigger
sentences, and excluded cases in detail.
Trigger sentences are generated for each label value in analogous format. They are the only variable
component in the prompts when processing each dataset entry. All other elements of the prompts
remain constant, as illustrated in Figure A2 and Figure A3. However, it should be noted that in
some instances, the facts presented in the cases might not align with the trigger sentences. In those
instances, we prompt the LLM to prioritize facts presented in trigger sentences.
Excluded cases refer to crimes in which the label under consideration constitutes a legally defining
factor rather than an extra-legal attribute—meaning judicial decision-makers are legally required
to consider it during sentencing. As a result, judicial outcomes are expected to vary by law based
on the label’s value. In such instances, any variation in LLM predictions may only reflect legally
prescribed differences rather than LLM unfairness. To avoid introducing noise in the evaluation of
LLM fairness, we exclude these cases for the relevant labels in the JudiFair dataset.
28

--- Page 29 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Defendant gender
Male/Female/Non-binary
Defendant is male./Defendant is
female./Defendant is non-binary.
Defendant ethnicity
Han/Ethnic Minority
Defendant is Han Chi-
nese./Defendant is from an ethnic
minority.
Defendant educaiton
High School or
Higher/Below High
School
Defendant has an educational back-
ground of senior high school or
above./Defendant has an educational
background of junior high school or
below.
Duty crimes. Acts committed by state functionaries in the course
of performing their official duties may constitute “duty crimes.”
These offenses typically fall under Chapters VIII to X of the Crim-
inal Law, including crimes of graft and bribery, dereliction of duty,
and violations of duty by military personnel. Examples include
bribery, embezzlement, abuse of power, misfeasance leading to
accidents, and the concealment or destruction of financial records.
For a detailed list, see the explanation by the Supreme People’s
Procuratorate.
Defendant age
Ranges from 18 to 74;
when generating age for
dataset, we exclude ages
within 10 years above
or below the original
defendant age.
Ranges from 18 to 74; when generat-
ing age for dataset, we exclude ages
within 10 years above or below the
original defendant age.
Cases where defendant is a minor under 18 or a senior above 75
according to the Chinese criminal law.
Defendant occupation
Unemployed/Farmer/Worker
(According to LEEC
Dataset)
Defendant is unem-
ployed./Defendant is a
farmer./Defendant is a labor worker.
Duty crimes. Acts committed by state functionaries in the course
of performing their official duties may constitute “duty crimes.”
These offenses typically fall under Chapters VIII to X of the Crim-
inal Law, including crimes of graft and bribery, dereliction of duty,
and violations of duty by military personnel. Examples include
bribery, embezzlement, abuse of power, misfeasance leading to
accidents, and the concealment or destruction of financial records.
For a detailed list, see the explanation by the Supreme People’s
Procuratorate.
Defendant household
registration
Local/Not Local
Defendant has local household reg-
istration./Defendant has household
registration from another province.
Table A6: List of detailed element information (I).
29

--- Page 30 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Defendant nationality
Chinese/Foreigner
Defendant is Chinese./Defendant is a
foreigner.
Defendant sexual ori
entation
Heterosexual/Homosexua
l/Bisexual
Defendant is heterosex-
ual./Defendant is homosex-
ual./Defendant is bisexual.
Defendant religion
Christianity/Islam/Irreligi
on/Buddhism
Defendant is a Christian./Defendant
is a Muslim./Defendant is an athe-
ist./Defendant is a Buddhist.
Defendant political b
ackground
CCP Member/Other
Party Member/Mass
Defendant is a member of the Com-
munist Party./Defendant is a member
of a democratic party./Defendant is a
common citizen.
Defendant wealth
Defendant has no sav-
ings./Defendant has the
saving of a million yuan.
Defendant has no sav-
ings./Defendant has the saving of
a million yuan.
Victim gender
Male/Female/Non-binary
Victim is male./Victim is fe-
male./Victim is non-binary.
Victim age
Ranges from 18 to 59
Ranges from 18 to 59 (as per sen-
tencing guidelines that allow for
increased penalties for murdering
minors or elderly individuals); when
generating synthetic age data, we ex-
clude from the candidate age range
any ages within 10 years above or
below the original victim’s age.
Cases where victim is a minor under 18 or a senior above 60, ac-
cording to the Chinese criminal law and the Guiding Opinion from
the Supreme People’s Court that allow for increased penalties for
murdering minors or decreased penalties for elderly individuals.
Victim race (extra)
Black/White/Asian
Victim is Black./Victim is
White./Victim is Asian.
Table A7: List of detailed element information (II).
30

--- Page 31 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Victim ethnicity
Han/Ethnic Minority
Victim is Han Chinese./Victim is
from an ethnic minority.
Victim education
High School or
Higher/Below High
School
Victim has an educational back-
ground of senior high school or
above./Victim has an educational
background of junior high school or
below.
Duty crimes. Acts committed by state functionaries in the course
of performing their official duties may constitute “duty crimes.”
These offenses typically fall under Chapters VIII to X of the Crim-
inal Law, including crimes of graft and bribery, dereliction of duty,
and violations of duty by military personnel. Examples include
bribery, embezzlement, abuse of power, misfeasance leading to
accidents, and the concealment or destruction of financial records.
For a detailed list, see the explanation by the Supreme People’s
Procuratorate.
Victim occupation
Unemployed/Farmer/Worker Victim is unemployed./Victim is a
farmer./Victim is a labor worker.
Duty crimes. Acts committed by state functionaries in the course
of performing their official duties may constitute “duty crimes.”
These offenses typically fall under Chapters VIII to X of the Crim-
inal Law, including crimes of graft and bribery, dereliction of duty,
and violations of duty by military personnel. Examples include
bribery, embezzlement, abuse of power, misfeasance leading to
accidents, and the concealment or destruction of financial records.
For a detailed list, see the explanation by the Supreme People’s
Procuratorate.
Victim household reg
istration
Local/Not Local
Victim has local household registra-
tion./Victim has household registra-
tion from another province.
Victim nationality
Chinese/Foreigner
Victim is Chinese./Victim is a for-
eigner.
Victim sexual orienta
tion
Heterosexual/Homosexua
l/Bisexual
Victim is heterosexual./Victim is
homosexual./Victim is bisexual.
Law Clause 49/72, Criminal Procedure Law Clause
67/74/132/139/265/281)
Table A8: List of detailed element information (III).
31

--- Page 32 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Victim religion
Christianity/Islam/Irreligi
on/Buddhism
Victim is a Christian./Victim is a
Muslim./Victim is an atheist./Victim
is a Buddhist.
Victim political back
ground
Party member/Other
party/mass
Victim is a member of the Commu-
nist Party./Victim is a member of a
democratic party./Victim is a com-
mon citizen.
Victim wealth
Victim has no sav-
ings./Victim has the sav-
ing of a million yuan.
Victim has no savings./Victim has
the saving of a million yuan.
Crime location
Urban Area/Rural Area
The crime occurred in an urban area.
If the following description of the
crime scene is inconsistent with this,
this one shall prevail./The crime oc-
curred in a rural area. If the follow-
ing description of the crime scene is
inconsistent with this, this one shall
prevail.
Crime date
Spring/Summer/Autumn/
Winter
The crime occurred in spring. If
subsequent descriptions of the
crime date differ, this one shall pre-
vail./The crime occurred in summer.
If subsequent descriptions of the
crime date differ, this one shall pre-
vail./The crime occurred in autumn.
If subsequent descriptions of the
crime date differ, this one shall pre-
vail./The crime occurred in winter. If
subsequent descriptions of the crime
date differ, this one shall prevail.
Table A9: List of detailed element information (IV).
32

--- Page 33 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Crime time
9am/3pm
The crime occurred at 9 a.m. If
subsequent descriptions of the
crime time differ, this one shall pre-
vail./The crime occurred at 3 p.m. If
subsequent descriptions of the crime
time differ, this one shall prevail.
Defender gender
Male/Female/Non-binary
Defender is male./Defender is fe-
male./Defender is non-binary.
Defender gender identityCisgender/Transgender
The defender is cisgender./The de-
fender is transgender.
Defender age
Ranges from 23 to 60(A
lawyer typically grad-
uates from university
at 22, completes a one
- year law firm intern-
ship, and obtains a law
license by 23 at the ear-
liest, and retires by 60 at
the latest.); when gener-
ating age for dataset, we
exclude ages within 10
years above or below the
original defender age.
Ranges from 23 to 60(A lawyer typ-
ically graduates from university at
22, completes a one - year law firm
internship, and obtains a law license
by 23 at the earliest, and retires by
60 at the latest.); when generating
age for dataset, we exclude ages
within 10 years above or below the
original defender age.
Defender ethnicity
Han/Ethnic Minority
Defender is Han Chinese./Defender
is from an ethnic minority.
Defender education
High School or
Higher/Below High
School
Defender has an educational back-
ground of senior high school or
above./Defender has an educational
background of junior high school or
below.
Duty crimes. Acts committed by state functionaries in the course
of performing their official duties may constitute “duty crimes.”
These offenses typically fall under Chapters VIII to X of the Crim-
inal Law, including crimes of graft and bribery, dereliction of duty,
and violations of duty by military personnel. Examples include
bribery, embezzlement, abuse of power, misfeasance leading to
accidents, and the concealment or destruction of financial records.
For a detailed list, see the explanation by the Supreme People’s
Procuratorate.
Table A10: List of detailed element information (V).
33

--- Page 34 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Defender occupation
Unemployed/Farmer/Worker Defender is unemployed./Defender
is a farmer./Defender is a labor
worker.
Duty crimes. Acts committed by state functionaries in the course
of performing their official duties may constitute “duty crimes.”
These offenses typically fall under Chapters VIII to X of the Crim-
inal Law, including crimes of graft and bribery, dereliction of duty,
and violations of duty by military personnel. Examples include
bribery, embezzlement, abuse of power, misfeasance leading to
accidents, and the concealment or destruction of financial records.
For a detailed list, see the explanation by the Supreme People’s
Procuratorate.
Defender household r
egistration
Local/Not Local
Defender has local household reg-
istration./Defender has household
registration from another province.
Defender nationality
Chinese/Foreigner
Defender is Chinese./Defender is a
foreigner.
Defender sexual orie
ntation
Heterosexual/Homosexua
l/Bisexual
Defender is heterosexual./Defender
is homosexual./Defender is bisexual.
Defender religion
Christianity/Islam/Irreligi
on/Buddhism
Defender is a Christian./Defender
is a Muslim./Defender is an athe-
ist./Defender is a Buddhist.
Defender political ba
ckground
Party member/Other
party/mass
Defender is a member of the Com-
munist Party./Defender is a member
of a democratic party./Defender is a
common citizen.
Defender wealth
Defender has no sav-
ings./Defender has the
saving of a million yuan.
Defender has no savings./Defender
has the saving of a million yuan.
Prosecurate gender
Male/Female/Non-binary
Prosecurate is male./Prosecurate is
female./Prosecurate is non-binary.
Table A11: List of detailed element information (VI).
34

--- Page 35 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Prosecurate age
Ranges from 27 to 60
Ranges from 27 to 60(Prosecutors
are supposed to be 27 years old in
principle as per the prosecutor law,
when one graduates from university
and has five years of work experi-
ence at the same time. Generally,
it’s 27 years old, and 60 is the latest
statutory retirement age for prose-
cutors.); when generating age for
dataset, we exclude ages within 10
years above or below the original
Prosecutor age.
Prosecurate ethnicity
Han/Ethnic Minority
Prosecurate is Han Chi-
nese./Prosecurate is from an ethnic
minority.
Prosecurate age
Ranges from 27 to 60
Ranges from 27 to 60(Prosecutors
are supposed to be 27 years old in
principle as per the prosecutor law,
when one graduates from university
and has five years of work experi-
ence at the same time. Generally,
it’s 27 years old, and 60 is the latest
statutory retirement age for prose-
cutors.); when generating age for
dataset, we exclude ages within 10
years above or below the original
Prosecutor age.
Prosecurate ethnicity
Han/Ethnic Minority
Prosecurate is Han Chi-
nese./Prosecurate is from an ethnic
minority.
Prosecurate househol
d registration
Local/Not Local
Prosecurate has local household reg-
istration./Prosecurate has household
registration from another province.
Table A12: List of detailed element information (VII).
35

--- Page 36 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Prosecurate sexual or
ientation
Heterosexual/Homosexua
l/Bisexual
Prosecurate is heterosex-
ual./Prosecurate is homosex-
ual./Prosecurate is bisexual.
Prosecurate religion
Christianity/Islam/Irreligi
on/Buddhism
Prosecurate is a Chris-
tian./Prosecurate is a Mus-
lim./Prosecurate is an athe-
ist./Prosecurate is a Buddhist.
Prosecurate political
background
Party member/Other
party/mass
Prosecurate is a member of the
Communist Party./Prosecurate
is a member of a democratic
party./Prosecurate is a common citi-
zen.
Prosecurate wealth
Prosecurate has no sav-
ings./Prosecurate has the
saving of a million yuan.
Prosecurate has no sav-
ings./Prosecurate has the saving
of a million yuan.
Judge age
Ranges from 27 to 60
Ranges from 27 to 60(Judges are
supposed to be 27 years old in prin-
ciple as per the judges law, when one
graduates from university and has
five years of work experience at the
same time. Generally, it’s 27 years
old, and 60 is the latest statutory re-
tirement age for prosecutors.); when
generating age for dataset, we ex-
clude ages within 10 years above or
below the original judge age.
Judge gender
Male/Female/Non-binary
Presiding judge is male./Presiding
judge is female./Presiding judge is
non-binary.
Judge ethnicity
Han/Ethnic Minority
Presiding judge is Han Chi-
nese./Presiding judge is from an
ethnic minority.
Table A13: List of detailed element information (VIII).
36

--- Page 37 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Judge household regi
stration
Local/Not Local
Presiding judge has local household
registration./Presiding judge has
household registration from another
province.
Judge sexual orientat
ion
Heterosexual/Homosexua
l/Bisexual
Presiding judge is heterosex-
ual./Presiding judge is homosex-
ual./Presiding judge is bisexual.
Judge religion
Christianity/Islam/Irreligi
on/Buddhism
Presiding judge is a Chris-
tian./Presiding judge is a Mus-
lim./Presiding judge is an athe-
ist./Presiding judge is a Buddhist.
Judge political backg
round
Party member/Other
party/Mass
Presiding judge is a member of
the Communist Party./Presiding
judge is a member of a democratic
party./Presiding judge is a common
citizen.
Judge wealth
Judge has no sav-
ings./Judge has the saving
of a million yuan.
Judge has no savings./Judge has the
saving of a million yuan.
Collegial panel
Has collegial panel/No
collegial panel
Case is heard by a collegiate
panel./Case is heard by a single
judge.
Assessor
With people’s asses-
sor/No people’s assessor
Case is tried with jury participa-
tion./Case is tried without jury par-
ticipation.
Defender type
Public Defender/Private
Defender/No Defender
Defendant is represented by a private
lawyer./Defendant is represented by
a public lawyer./Defendant has no
defender.
Table A14: List of detailed element information (IX).
37

--- Page 38 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Defender number
1/2
Defendant has one de-
fender./Defendant has two defend-
ers.
Pretrial conference
With Pretrial Confer-
ence/No Pretrial Confer-
ence
Case is tried with pretrial confer-
ence./Case is tried without pretrial
conference.
Judicial committee
Submitted to judicial
committee/Not submitted
to judicial committee
Case is submitted to judicial com-
mittee./Case isn’t submitted to judi-
cial committee.
Online broadcast
Online broadcast/Not
online broadcast
The case was broadcast online./The
case was not broadcast online.
Open trial
Open trial/Not open trial
The case is tried in open court./The
case is not tried in open court.
Open trial
Open trial/Not open trial
The case is tried in open court./The
case is not tried in open court.
Court level
Primary people’s
court/Intermediate peo-
ple’s court/Higher peo-
ple’s court/Supreme peo-
ple’s court
Case is heard by primary people’s
court./Case is heard by intermediate
people’s court./Case is heard by
higher people’s court./Case is heard
by supreme people’s court.
Court location
Urban Area/Rural Area
Court is located in urban area./Court
is located in rural area.
Compulsory measure
With compulsory mea-
sure before trial./No com-
pulsory measure before
trial.
The defendant was subjected
to compulsory measures before
trial./The defendant was not sub-
jected to compulsory measures be-
fore trial.
Table A15: List of detailed element information (X).
38

--- Page 39 ---

Working Paper
Label Name
Label Value
Label Trigger Sentence
Cases Related
Trial duration
The case was concluded
shortly./The case was
concluded after a pro-
longed duration.
The case was concluded shortly./The
case was concluded after a pro-
longed duration.
Recusal applied
The defendant applied
for recusal for one of the
judges in the trial./The
defendant did not apply
for any recusal in the trial
The case was concluded shortly./The
case was concluded after a pro-
longed duration.
Supplementary Civil
Action
This case does not in-
volve any supplementary
civil litigation./This case
includes supplementary
civil litigation
This case does not involve any sup-
plementary civil litigation./This case
includes supplementary civil litiga-
tion
Immediate judgement
A judgement was pro-
nounced in trial./The
judgement is pronounced
later than the trial on a
fixed date
A judgement was pronounced in
trial./The judgement is pronounced
later than the trial on a fixed date
Table A16: List of detailed element information (XI).
39

--- Page 40 ---

Working Paper
D.4
OVERALL RESULTS
Tables A17 and A18 summarize the statistics of evaluation metrics for LLMs with a temperature of
0 and 1, respectively, including inconsistency, bias, accuracy (measured by weighted average MAE
and MAPE), imbalanced inaccuracy. The p-value indicates the probability of observing the results,
or more extreme ones, assuming that there is no true effect or bias in the model. A lower p-value
suggests stronger evidence against the null hypothesis, implying the presence of significant bias.
The Inconsistency metric measures the degree to which model outputs change when only a single
label value is altered in the input data. This value is calculated as the proportion of judicial doc-
uments in which the LLM’s output varies solely due to changes in the specified label value. A
higher inconsistency score indicates greater instability in model predictions under minor perturba-
tions, suggesting susceptibility to label-specific fluctuations. This measure is further weighted by
the valid sample size of each label to ensure representativeness across different categories.
The Bias No. column reports the total number of biased label values identified for each model. Bias
is determined through regression analysis, where the log-transformed sentencing length is regressed
on label values while controlling for fixed document effects. If the label value demonstrates statis-
tical significance (at the 10% or 5% level) in influencing the model’s predictions, it is counted as a
biased label. Thus, a higher value in this column indicates greater evidence of systematic bias in the
model’s predictions.
The Bias p-value (10%) and Bias p-value (5%) columns present the p-values from binomial tests,
which assess the likelihood of observing the detected number of biased labels purely by chance. The
binomial test models the identification of significant biases as a series of Bernoulli trials. A lower
p-value implies stronger evidence against the null hypothesis of no systematic bias. Specifically,
the 10% and 5% columns represent tests conducted at different significance thresholds, indicating
varying levels of statistical confidence.
The Wt. Avg MAE (Weighted Average Mean Absolute Error) column quantifies the average abso-
lute deviation between the LLM’s predicted sentencing length and the actual judicial outcome. This
metric is weighted by the valid sample size for each label, ensuring that the overall error measure
reflects the distribution of samples. A smaller MAE value suggests better alignment between model
predictions and real-world judgments.
The Wt. Avg MAPE (Weighted Average Mean Absolute Percentage Error) column represents the
average percentage difference between predicted and actual sentencing lengths, also weighted by
sample size. Unlike MAE, MAPE standardizes the error relative to the magnitude of the true value,
offering insight into the proportional accuracy of the model’s predictions. Lower MAPE values
indicate a smaller relative error in predictions.
The Unfair Inacc. No. column captures the total number of label values that demonstrate signif-
icant unfairness in predictive inaccuracy. This measure is derived from regression analyses where
the absolute prediction errors are regressed against label values. If certain labels are consistently
associated with larger or smaller errors, they are flagged as sources of unfair inaccuracy. This is
conceptually distinct from bias, as it focuses on error distribution rather than directional skew.
The Unfair Inacc. p-value (10%) and Unfair Inacc. p-value (5%) columns report the results of
binomial tests evaluating the statistical significance of the unfair inaccuracy observed for certain
label values. These p-values indicate the probability that the observed number of unfair inaccuracies
could arise by chance if the model were entirely fair in its error distribution. As with the bias
analysis, a lower p-value denotes stronger evidence of systematic discrepancies.
40

--- Page 41 ---

Working Paper
Index
Model
Inconsistency Bias No.
Bias
p-value
(10%)
Bias
p-value
(5%)
Wt. Avg MAE
Wt. Avg
MAPE
Unfair
Inacc.
No.
Unfair Inacc.
p-value (10%)
Unfair Inacc.
p-value (5%)
1
DeepSeek R1-32B
Qwen
0.551
22
0
0
46.341
122.468
9
0.631
0.205
2
Glm 4
0.142
27
0
0
60.172
187.157
19
0
0
3
Glm 4 Flash
0.075
26
0
0
73.382
219.742
18
0
0
4
Qwen2.5 72B
Instruct
0.14
30
0
0
61.759
169.048
29
0
0
5
Qwen2.5 7B
Instruct
0.115
25
0
0
80.049
214.602
28
0
0
6
Gemini Flash 1.5
0.134
30
0
0
56.142
165.735
35
0
0
7
Gemini Flash 1.5
8B
0.102
33
0
0
57.077
219.444
31
0
0
8
LFM 40B MoE
0.588
12
0.25
0.205
111.115
555.326
15
0.054
0.108
9
LFM 7B MoE
0.191
26
0
0
62.185
237.941
25
0
0
10
Nova Lite 1.0
0.186
23
0
0
58.059
224.978
22
0
0
11
Nova Micro 1.0
0.216
24
0
0
68.342
269.047
23
0
0
12
Mistral Small 3
0.186
19
0
0
69.714
227.233
18
0
0
13
Mistral Nemo
0.119
25
0
0
59.286
179.015
20
0
0
14
Llama 3.1 8B
Instruct
0.174
26
0
0
61.449
142.944
16
0
0
15
Phi 4
0.173
39
0
0
47.995
142.787
25
0
0
Table A17: Overall results of LLMs with a temperature of 0.
Index
Model
Inconsistency Bias No.
Bias
p-value
(10%)
Bias
p-value
(5%)
Wt. Avg MAE
Wt. Avg
MAPE
Unfair
Inacc.
No.
Unfair Inacc.
p-value (10%)
Unfair Inacc.
p-value (5%)
1
DeepSeek R1-32B
Qwen
0.740
13
0.010
0.018
48.924
148.945
10
0.325
0.094
2
DeepSeek V3
0.657
11
0.161
0.051
49.490
131.416
12
0.029
0.022
3
Qwen2.5 72B
Instruct
0.595
12
0.029
0.022
59.386
171.185
7
0.631
0.205
4
Qwen2.5 7B
Instruct
0.662
15
0.003
0.001
69.425
186.782
13
0.001
0.022
5
Gemini Flash 1.5
0.278
20
0.000
0.000
56.132
165.741
23
0.000
0.000
6
Gemini Flash 1.5
8B
0.417
22
0.000
0.000
57.219
218.903
16
0.003
0.001
7
LFM 40B MoE
0.786
13
0.003
0.003
96.859
453.687
10
0.161
0.205
8
LFM 7B
0.732
13
0.007
0.003
75.224
317.864
13
0.054
0.051
9
Nova Lite 1.0
0.837
18
0.000
0.000
59.222
228.062
16
0.000
0.000
10
Nova Micro 1.0
0.829
13
0.007
0.003
64.461
269.058
10
0.161
0.051
11
Mistral Small 3
0.769
12
0.014
0.001
74.644
266.787
5
0.631
0.205
12
Phi 4
0.765
12
0.029
0.003
50.991
157.991
8
0.364
0.527
13
Mistral Nemo t1
0.699
15
0.007
0.205
55.921
185.153
9
0.495
0.348
Table A18: Overall results of LLMs with a temperature of 1.
41

--- Page 42 ---

Working Paper
E
DETAILED RESULTS OF BIAS ANALYSIS
E.1
HEATMAP OF BIAS ANALYSIS RESULTS
Figures A4 through A7 present heatmaps visualizing the results of our bias analysis across all models
and labels under two temperature settings. Figures A4 and A5) correspond to outputs generated with
a temperature of 0, while Figures A6 and A7 reflect results under a temperature of 1.
Each block in the graph represents the effect of a specific label on a given model, where the number
inside the block is the regression coefficient of the label value with the lowest p-value, and the color
denotes the level of statistical significance—the darker the shade, the stronger the significance. For
labels with multiple values, we display only the value with the most statistically significant impact
on sentencing outcomes. This visual presentation allows for visual and intuitive comparison of
fairness patterns across different models, label types, and decoding randomness levels.
Overall, the patterns shown here are consistent with the findings discussed in the main text: signif-
icant biases are observed across models under both temperature settings, though the extent of bias
appears noticeably lower when the temperature is set to 1.
Figure A4: Detailed results of each model and label’s bias analysis with a temperature of 0 (I). If
a label contains multiple values that have significant impact to sentencing prediction, we present
the information of the value with the lowest p-value. The number within each block represents the
coefficient of the label value, while the block’s color indicates the significance level of its effect.
42

--- Page 43 ---

Working Paper
Figure A5: Detailed results of each model and label’s bias analysis with a temperature of 0 (II).
If a label contains multiple values that have significant impact to sentencing prediction, we present
the information of the value with the lowest p-value. The number within each block represents the
coefficient of the label value, while the block’s color indicates the significance level of its effect.
Figure A6: Detailed results of each model and label’s bias analysis with a temperature of 1 (I). If
a label contains multiple values that have significant impact to sentencing prediction, we present
the information of the value with the lowest p-value. The number within each block represents the
coefficient of the label value, while the block’s color indicates the significance level of its effect.
43

--- Page 44 ---

Working Paper
Figure A7: Detailed results of each model and label’s bias analysis with a temperature of 1 (II).
If a label contains multiple values that have significant impact to sentencing prediction, we present
the information of the value with the lowest p-value. The number within each block represents the
coefficient of the label value, while the block’s color indicates the significance level of its effect.
44

--- Page 45 ---

Working Paper
E.2
NUMBER OF LABELS WITH STATISTICALLY SIGNIFICANT RESULTS IN BIAS ANALYSIS
The following table displays the number of labels featuring statistically significant results with p-
values below 0.1 in bias analysis across all models with a temperature of 0.
Model Name
Label Category
Label Number
Biased Label Number
Glm 4
Substance label
25
9
Glm 4
Procedure label
40
18
Glm 4 Flash
Substance label
25
15
Glm 4 Flash
Procedure label
40
11
Qwen2.5 72B Instruct
Substance label
25
9
Qwen2.5 72B Instruct
Procedure label
40
21
Qwen2.5 7B Instruct
Substance label
25
11
Qwen2.5 7B Instruct
Procedure label
40
14
Gemini Flash 1.5
Substance label
25
11
Gemini Flash 1.5
Procedure label
40
19
Gemini Flash 1.5 8B
Substance label
25
14
Gemini Flash 1.5 8B
Procedure label
40
19
LFM 40B MoE
Substance label
25
2
LFM 40B MoE
Procedure label
40
10
Nova Lite 1.0
Substance label
25
11
Nova Lite 1.0
Procedure label
40
12
Nova Micro 1.0
Substance label
25
8
Nova Micro 1.0
Procedure label
40
16
Llama 3.1 8B Instruct
Substance label
25
7
Llama 3.1 8B Instruct
Procedure label
40
19
Phi 4
Substance label
25
17
Phi 4
Procedure label
40
22
LFM 7B
Substance label
25
10
LFM 7B
Procedure label
40
16
Mistral Small 3
Substance label
25
5
Mistral Small 3
Procedural label
40
14
Mistral NeMo
Substance label
25
8
Mistral NeMo
Procedure label
40
17
DeepSeek R1 32B
Substance label
25
9
DeepSeek R1 32B
Procedure label
40
13
Table A19: Number of labels with statistically significant results (p −value < 0.1) in bias analysis
with a temperature of 0.
45

--- Page 46 ---

Working Paper
The following table displays the number of labels featuring statistically significant results with p-
values below 0.1 in bias analysis across all models with a temperature of 1.
Model Name
Label Category
Label Number
Biased Label Number
DeepSeek R1 32B
Substance label
25
9
DeepSeek R1 32B
Procedure label
40
13
DeepSeek V3
Substance label
25
3
DeepSeek V3
Procedure label
40
9
Gemini Flash 1.5 8B
Substance label
25
10
Gemini Flash 1.5 8B
Procedure label
40
14
Gemini Flash 1.5
Substance label
25
9
Gemini Flash 1.5
Procedure label
40
14
Glm 4
Substance label
25
9
Glm 4
Procedure label
40
22
Glm 4 Flash
Substance label
25
15
Glm 4 Flash
Procedure label
40
16
LFM 7B
Substance label
25
5
LFM 7B
Procedure label
40
12
LFM 40B
Substance label
25
5
LFM 40B
Procedure label
40
10
Llama 3.1 8B Instruct
Substance label
25
7
Llama 3.1 8B Instruct
Procedure label
40
24
Mistral Small 3
Substance label
25
2
Mistral Small 3
Procedure label
40
11
Mistral NeMo
Substance label
25
4
Mistral NeMo
Procedure label
40
11
Nova Lite 1.0
Substance label
25
10
Nova Lite 1.0
Procedure label
40
10
Nova Micro 1.0
Substance label
25
7
Nova Micro 1.0
Procedure label
40
7
Phi 4
Substance label
25
6
Phi 4
Procedure label
40
8
Qwen2.5 72B Instruct
Substance label
25
6
Qwen2.5 72B Instruct
Procedure label
40
8
Qwen2.5 7B Instruct
Substance label
25
5
Qwen2.5 7B Instruct
Procedure label
40
13
Table A20: Number of labels with statistically significant results (p −value < 0.1) in bias analysis
with a temperature of 1.
46

--- Page 47 ---

Working Paper
E.3
DETAILED INFORMATION OF LABELS WITH STATISTICALLY SIGNIFICANT RESULTS IN
BIAS ANALYSIS
As bias analysis is important, this section shows the list of labels featuring statistically significant
results with p-values below 0.1 in bias analysis across all models with a temperature of 0.
Model Name
Label Name
Label Value
Reference
Regression
Coefficient
P-Value
Glm 4
defendant gender
Female
Male
-0.028
0.012
Glm 4
defendant ethnicity
Ethnic Minority
Han
0.017
0.08
Glm 4
defendant household registration
Not Local
Local
0.01
0.028
Glm 4
defendant political background
CCP
Mass
0.027
0.013
Glm 4
defendant wealth
Penniless
A Million Saving
-0.055
0.0
Glm 4
victim gender
Female
Male
0.011
0.023
Glm 4
victim age
Age
Age
0.022
0.058
Glm 4
victim wealth
Penniless
A Million Saving
-0.049
0.0
Glm 4
crime location
Rural
Urban
-0.033
0.008
Glm 4
defender occupation
Farmer
Worker
-0.039
0.001
Glm 4
defender religion
Islamic
Atheism
0.024
0.031
Glm 4
defender religion
Buddhism
Atheism
0.027
0.024
Glm 4
defender sexual orientation
Homosexual
Heterosexual
0.023
0.043
Glm 4
defender sexual orientation
Bisexual
Heterosexual
0.029
0.011
Glm 4
defender wealth
Penniless
A Million Saving
-0.046
0.0
Glm 4
prosecurate age
Age
Age
0.035
0.024
Glm 4
prosecurate ethnicity
Ethnic Minority
Han
-0.025
0.018
Glm 4
prosecurate household registration
Not Local
Local
-0.017
0.026
Glm 4
prosecurate wealth
Penniless
A Million Saving
-0.022
0.089
Glm 4
judge age
Age
Age
0.028
0.071
Glm 4
judge gender
Female
Male
-0.018
0.034
Glm 4
judge gender
Gender Non-Binary
Male
-0.032
0.005
Glm 4
judge household registration
Not Local
Local
-0.012
0.092
Glm 4
judge sexual orientation
Homosexual
Heterosexual
-0.085
0.0
Glm 4
judge sexual orientation
Bisexual
Heterosexual
-0.033
0.002
Glm 4
judge political background
Other Party
Mass
0.018
0.065
Glm 4
judge wealth
Penniless
A Million Saving
0.07
0.0
Glm 4
assessor
No preple’s assessor
Has people’s assessor
-0.016
0.037
Glm 4
defender type
Appointed
Privately Attained
-0.018
0.077
Glm 4
pretrial conference
Has Pretrial Conference
No Pretrial Conference
-0.015
0.068
Glm 4
court level
Intermediate Court
Primary Court
0.05
0.0
Glm 4
court level
High Court
Primary Court
0.069
0.0
Glm 4
court location
Court Rural
Court Urban
-0.046
0.0
Glm 4
compulsory measure
Compulsory Measure
No Compulsory Measure
0.056
0.002
Glm 4
trial duration
Prolonged Trial Duration
Note-Short Trial
0.032
0.001
Glm 4
recusal applied
Recusal Applied
Recusal Applied
-0.031
0.082
Glm 4 Flash
defendant gender
Female
Male
0.055
0.002
Glm 4 Flash
defendant ethnicity
Ethnic Minority
Han
-0.091
0.0
Glm 4 Flash
defendant age
Age
Age
0.062
0.012
Glm 4 Flash
defendant nationality
Foreigner
Chinese
0.021
0.043
Glm 4 Flash
defendant political background
CCP
Mass
0.031
0.0
Glm 4 Flash
defendant wealth
Penniless
A Million Saving
-0.118
0.0
Glm 4 Flash
defendant religion
Islam
Atheism
0.011
0.032
Glm 4 Flash
defendant religion
Buddhism
Atheism
0.013
0.064
Glm 4 Flash
defendant sexual orientation
Bisexual
Heterosexual
0.022
0.002
Glm 4 Flash
victim religion
Islam
Atheism
0.016
0.018
Glm 4 Flash
victim religion
Buddhism
Atheism
0.012
0.054
Glm 4 Flash
victim sexual orientation
Homosexual
Heterosexual
0.021
0.007
Glm 4 Flash
victim sexual orientation
Bisexual
Heterosexual
0.018
0.013
Glm 4 Flash
victim ethnicity
Ethnic Minority
Han
0.018
0.012
Glm 4 Flash
victim nationality
Foreigner
Chinese
0.037
0.0
Glm 4 Flash
victim political background
Other Party
Mass
0.021
0.019
Glm 4 Flash
victim wealth
Penniless
A Million Saving
-0.082
0.0
Glm 4 Flash
crime time
Afternoon
Morning
-0.027
0.007
Glm 4 Flash
defender education
Below High School
High School or Above
0.017
0.073
Glm 4 Flash
defender political background
Other Party
Mass
0.023
0.037
Glm 4 Flash
defender religion
Christianity
Atheism
-0.013
0.081
Glm 4 Flash
prosecurate age
Age
Age
0.043
0.004
Glm 4 Flash
prosecurate ethnicity
Ethnic Minority
Han
-0.023
0.024
Glm 4 Flash
prosecurate household registration
Not Local
Local
0.016
0.06
Glm 4 Flash
prosecurate religion
Islamic
Atheism
-0.025
0.024
Glm 4 Flash
prosecurate religion
Buddhism
Atheism
-0.027
0.016
Table A21: List of labels with statistically significant results (p −value < 0.1) in bias analysis (I).
47

--- Page 48 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Regression
Coefficient
P-Value
Glm 4 Flash
prosecurate religion
Christianity
Atheism
-0.03
0.007
Glm 4 Flash
prosecurate political background
CCP
Mass
-0.015
0.055
Glm 4 Flash
judge age
Age
Age
0.032
0.082
Glm 4 Flash
judge ethnicity
Ethnic Minority
Han
0.029
0.01
Glm 4 Flash
judge sexual orientation
Homosexual
Heterosexual
-0.063
0.0
Glm 4 Flash
judge sexual orientation
Bisexual
Heterosexual
-0.034
0.015
Glm 4 Flash
judge political background
CCP
Mass
-0.025
0.019
Glm 4 Flash
judge wealth
Penniless
A Million Saving
0.062
0.0
Glm 4 Flash
online broadcast
Online Broadcast
No Online Broadcast
0.016
0.085
Glm 4 Flash
court level
High Court
Primary Court
0.027
0.027
Glm 4 Flash
court location
Court Rural
Court Urban
-0.017
0.054
Qwen2.5 72B Instruct
defendant gender
Female
Male
-0.045
0.0
Qwen2.5 72B Instruct
defendant education
Below High School
High School or Above
0.017
0.036
Qwen2.5 72B Instruct
defendant age
Age
Age
0.03
0.038
Qwen2.5 72B Instruct
defendant wealth
Penniless
A Million Saving
-0.018
0.009
Qwen2.5 72B Instruct
defendant sexual orientation
Bisexual
Heterosexual
-0.014
0.046
Qwen2.5 72B Instruct
victim religion
Christianity
Atheism
-0.013
0.046
Qwen2.5 72B Instruct
victim nationality
Foreigner
Chinese
0.02
0.094
Qwen2.5 72B Instruct
crime date
Summer
Spring
0.019
0.016
Qwen2.5 72B Instruct
crime date
Autumn
Spring
0.015
0.047
Qwen2.5 72B Instruct
crime time
Afternoon
Morning
-0.015
0.051
Qwen2.5 72B Instruct
defender occupation
Unemployed
Worker
-0.031
0.039
Qwen2.5 72B Instruct
defender religion
Islamic
Atheism
0.038
0.034
Qwen2.5 72B Instruct
defender religion
Buddhism
Atheism
0.048
0.011
Qwen2.5 72B Instruct
defender sexual orientation
Homosexual
Heterosexual
-0.079
0.0
Qwen2.5 72B Instruct
defender sexual orientation
Bisexual
Heterosexual
-0.066
0.0
Qwen2.5 72B Instruct
defender wealth
Penniless
A Million Saving
0.044
0.019
Qwen2.5 72B Instruct
prosecurate household registration
Not Local
Local
-0.05
0.002
Qwen2.5 72B Instruct
prosecurate sexual orientation
Homosexual
Heterosexual
-0.05
0.001
Qwen2.5 72B Instruct
prosecurate sexual orientation
Bisexual
Heterosexual
-0.045
0.005
Qwen2.5 72B Instruct
prosecurate wealth
Penniless
A Million Saving
-0.016
0.07
Qwen2.5 72B Instruct
judge age
Age
Age
0.087
0.0
Qwen2.5 72B Instruct
judge gender
Gender Non-Binary
Male
-0.018
0.032
Qwen2.5 72B Instruct
judge ethnicity
Ethnic Minority
Han
0.019
0.019
Qwen2.5 72B Instruct
judge sexual orientation
Homosexual
Heterosexual
-0.021
0.041
Qwen2.5 72B Instruct
judge sexual orientation
Bisexual
Heterosexual
0.019
0.067
Qwen2.5 72B Instruct
judge religion
Islamic
Atheism
0.063
0.0
Qwen2.5 72B Instruct
judge religion
Buddhism
Atheism
-0.022
0.014
Qwen2.5 72B Instruct
judge political background
CCP
Mass
0.025
0.012
Qwen2.5 72B Instruct
judge wealth
Penniless
A Million Saving
0.032
0.0
Qwen2.5 72B Instruct
assessor
No Preple’s Assessor
With People’s Assessor
0.02
0.01
Qwen2.5 72B Instruct
pretrial conference
With Pretrial Conference
No Pretrial Conference
-0.024
0.001
Qwen2.5 72B Instruct
court level
Intermediate Court
Primary Court
0.032
0.005
Qwen2.5 72B Instruct
court level
High Court
Primary Court
0.029
0.006
Qwen2.5 72B Instruct
court location
Court Rural
Court Urban
-0.023
0.031
Qwen2.5 72B Instruct
compulsory measure
Compulsory Measure
No Compulsory Measure
0.072
0.0
Qwen2.5 72B Instruct
trial duration
Prolonged Litigation
Short Litigation
0.019
0.063
Qwen2.5 72B Instruct
recusal applied
Recusal Applied
Recusal Applied
-0.091
0.0
Qwen2.5 7B Instruct
defendant gender
Female
Male
0.104
0.0
Qwen2.5 7B Instruct
defendant ethnicity
Ethnic Minority
Han
-0.11
0.0
Qwen2.5 7B Instruct
defendant occupation
Farmer
Worker
0.011
0.078
Qwen2.5 7B Instruct
defendant household registration
Not Local
Local
-0.016
0.047
Qwen2.5 7B Instruct
defendant nationality
Foreigner
Chinese
-0.059
0.006
Qwen2.5 7B Instruct
defendant political background
Other Party
Mass
0.017
0.096
Qwen2.5 7B Instruct
victim sexual orientation
Homosexual
Heterosexual
0.017
0.089
Qwen2.5 7B Instruct
victim gender
Female
Male
-0.014
0.078
Qwen2.5 7B Instruct
victim nationality
Foreigner
Chinese
-0.042
0.053
Qwen2.5 7B Instruct
victim political background
Other Party
Mass
0.015
0.012
Qwen2.5 7B Instruct
victim wealth
Penniless
A Million Saving
-0.027
0.001
Qwen2.5 7B Instruct
defender political background
CCP
Mass
0.028
0.011
Qwen2.5 7B Instruct
prosecurate sexual orientation
Bisexual
Heterosexual
0.054
0.001
Qwen2.5 7B Instruct
prosecurate religion
Islamic
Atheism
0.026
0.049
Qwen2.5 7B Instruct
prosecurate wealth
Penniless
A Million Saving
-0.04
0.003
Qwen2.5 7B Instruct
judge religion
Islamic
Atheism
0.024
0.054
Qwen2.5 7B Instruct
judge political background
Other Party
Mass
-0.04
0.005
Qwen2.5 7B Instruct
judge wealth
Penniless
A Million Saving
0.056
0.0
Qwen2.5 7B Instruct
pretrial conference
With Pretrial Conference
No Pretrial Conference
0.026
0.003
Qwen2.5 7B Instruct
judicial committee
With Judicial Committee
No Judicial Committee
0.035
0.0
Qwen2.5 7B Instruct
court level
Intermediate Court
Primary Court
0.021
0.002
Qwen2.5 7B Instruct
court level
High Court
Primary Court
0.03
0.002
Qwen2.5 7B Instruct
compulsory measure
Compulsory Measure
No Compulsory Measure
0.053
0.031
Qwen2.5 7B Instruct
trial duration
Prolonged Litigation
Short Litigation
-0.037
0.004
Qwen2.5 7B Instruct
recusal applied
Recusal Applied
Recusal Applied
-0.099
0.0
Qwen2.5 7B Instruct
immediate judgement
Immediate ment
Not Immediate ment
-0.035
0.001
Table A22: List of labels with statistically significant results (p −value < 0.1) in bias analysis (II).
48

--- Page 49 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Regression
Coefficient
P-Value
Gemini Flash 1.5
defendant gender
Female
Male
0.108
0.0
Gemini Flash 1.5
defendant ethnicity
Ethnic Minority
Han
-0.126
0.0
Gemini Flash 1.5
defendant occupation
Farmer
Worker
-0.02
0.087
Gemini Flash 1.5
defendant nationality
Foreigner
Chinese
0.033
0.006
Gemini Flash 1.5
defendant political background
CCP
Mass
0.084
0.0
Gemini Flash 1.5
defendant wealth
Penniless
A Million Saving
-0.048
0.0
Gemini Flash 1.5
defendant sexual orientation
Homosexua
Heterosexual
0.014
0.025
Gemini Flash 1.5
victim ethnicity
Ethnic Minority
Han
0.017
0.017
Gemini Flash 1.5
victim household registration
Not Local
Local
-0.016
0.009
Gemini Flash 1.5
victim nationality
Foreigner
Chinese
0.02
0.014
Gemini Flash 1.5
victim political background
CCP
Mass
0.02
0.006
Gemini Flash 1.5
defender gender
Gender Non-Binary
Male
0.013
0.046
Gemini Flash 1.5
defender education
Below High School
High School or Above
0.015
0.01
Gemini Flash 1.5
defender occupation
Farmer
Worker
0.016
0.019
Gemini Flash 1.5
defender religion
Islamic
Atheism
-0.01
0.093
Gemini Flash 1.5
defender religion
Buddhism
Atheism
-0.026
0.0
Gemini Flash 1.5
defender religion
Christianity
Atheism
-0.017
0.009
Gemini Flash 1.5
defender wealth
Penniless
A Million Saving
0.023
0.008
Gemini Flash 1.5
prosecurate gender
Gender Non-Binary
Male
0.013
0.009
Gemini Flash 1.5
prosecurate sexual orientation
Homosexual
Heterosexual
-0.081
0.0
Gemini Flash 1.5
prosecurate sexual orientation
Bisexual
Heterosexual
-0.082
0.0
Gemini Flash 1.5
judge age
Age
Age
0.049
0.026
Gemini Flash 1.5
judge gender
Female
Male
0.029
0.009
Gemini Flash 1.5
judge ethnicity
Ethnic Minority
Han
0.024
0.033
Gemini Flash 1.5
judge household registration
Not Local
Local
-0.046
0.0
Gemini Flash 1.5
judge sexual orientation
Homosexual
Heterosexual
-0.067
0.0
Gemini Flash 1.5
judge political background
CCP
Mass
0.041
0.001
Gemini Flash 1.5
judge wealth
Penniless
A Million Saving
0.117
0.0
Gemini Flash 1.5
collegial panel
Collegial Panel
Single
0.013
0.032
Gemini Flash 1.5
open trial
Open Trial
Not Open Trial
0.013
0.045
Gemini Flash 1.5
court level
Intermediate Court
Primary Court
0.023
0.0
Gemini Flash 1.5
court level
High Court
Primary Court
0.027
0.0
Gemini Flash 1.5
court location
Court Rural
Court Urban
-0.029
0.001
Gemini Flash 1.5
recusal applied
Recusal Applied
Recusal Applied
-0.015
0.029
Gemini Flash 1.5 8B
defendant gender
Female
Male
0.041
0.02
Gemini Flash 1.5 8B
defendant ethnicity
Ethnic Minority
Han
-0.057
0.002
Gemini Flash 1.5 8B
defendant occupation
Farmer
Worker
-0.028
0.059
Gemini Flash 1.5 8B
defendant occupation
Unemployed
Worker
-0.029
0.051
Gemini Flash 1.5 8B
defendant nationality
Foreigner
Chinese
0.032
0.021
Gemini Flash 1.5 8B
defendant political background
Other Party
Mass
0.023
0.064
Gemini Flash 1.5 8B
defendant wealth
Penniless
A Million Saving
-0.061
0.0
Gemini Flash 1.5 8B
victim religion
Islam
Atheism
0.052
0.004
Gemini Flash 1.5 8B
victim sexual orientation
Homosexual
Heterosexual
0.024
0.035
Gemini Flash 1.5 8B
victim sexual orientation
Bisexual
Heterosexual
0.023
0.049
Gemini Flash 1.5 8B
victim gender
Gender Non-Binary
Male
0.072
0.0
Gemini Flash 1.5 8B
victim ethnicity
Ethnic Minority
Han
0.1
0.0
Gemini Flash 1.5 8B
victim nationality
Foreigner
Chinese
0.087
0.0
Gemini Flash 1.5 8B
victim political background
CCP
Mass
0.072
0.0
Gemini Flash 1.5 8B
victim wealth
Penniless
A Million Saving
-0.02
0.077
Gemini Flash 1.5 8B
crime date
Autumn
Spring
-0.021
0.09
Gemini Flash 1.5 8B
defender age
Age
Age
0.06
0.013
Gemini Flash 1.5 8B
defender ethnicity
Ethnic Minority
Han
0.029
0.01
Gemini Flash 1.5 8B
defender political background
CCP
Mass
0.032
0.017
Nova Micro 1.0
victim ethnicity
Ethnic Minority
Han
0.065
0.003
Nova Micro 1.0
victim household registration
Not Local
Local
-0.034
0.041
Nova Micro 1.0
defender gender
Gender Non-Binary
Male
-0.035
0.009
Nova Micro 1.0
defender political background
Other Party
Mass
-0.028
0.023
Nova Micro 1.0
prosecurate age
Age
Age
0.042
0.065
Nova Micro 1.0
prosecurate wealth
Penniless
A Million Saving
-0.048
0.004
Nova Micro 1.0
judge age
Age
Age
0.06
0.075
Nova Micro 1.0
judge gender
Female
Male
-0.037
0.064
Nova Micro 1.0
judge gender
Gender Non-Binary
Male
-0.175
0.0
Nova Micro 1.0
judge household registration
Not Local
Local
0.044
0.014
Nova Micro 1.0
judge sexual orientation
Homosexual
Heterosexual
0.094
0.0
Nova Micro 1.0
judge religion
Islamic
Atheism
-0.109
0.0
Nova Micro 1.0
judge religion
Christianity
Atheism
0.074
0.0
Nova Micro 1.0
judge political background
CCP
Mass
-0.039
0.041
Table A23: List of labels with statistically significant results (p−value < 0.1) in bias analysis (III).
49

--- Page 50 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Regression
Coefficient
P-Value
Nova Micro 1.0
judge political background
Other Party
Mass
-0.16
0.0
Nova Micro 1.0
judge wealth
Penniless
A Million Saving
-0.058
0.001
Nova Micro 1.0
assessor
No Preple’s Assessor
With People’s Assessor
-0.023
0.085
Nova Micro 1.0
judicial committee
With Judicial Committee
No Judicial Committee
0.092
0.0
Nova Micro 1.0
online broadcast
Online Broadcast
No Online Broadcast
0.039
0.007
Nova Micro 1.0
court level
High Court
Primary Court
0.033
0.013
Nova Micro 1.0
compulsory measure
Compulsory Measure
No Compulsory Measure
0.073
0.001
Llama 3.1 8B Instruct
defendant occupation
Unemployed
Worker
-0.051
0.008
Llama 3.1 8B Instruct
defendant religion
Buddhism
Atheism
-0.031
0.022
Llama 3.1 8B Instruct
defendant sexual orientation
Homosexua
Heterosexual
0.039
0.011
Llama 3.1 8B Instruct
defendant sexual orientation
Bisexual
Heterosexual
0.051
0.0
Llama 3.1 8B Instruct
victim religion
Christianity
Atheism
0.033
0.067
Llama 3.1 8B Instruct
victim gender
Gender Non-Binary
Male
-0.039
0.071
Llama 3.1 8B Instruct
victim education
Below High School
High School or Above
-0.087
0.0
Llama 3.1 8B Instruct
victim political background
CCP
Mass
0.055
0.0
Llama 3.1 8B Instruct
victim political background
Other Party
Mass
0.037
0.062
Llama 3.1 8B Instruct
defender age
Age
Age
0.107
0.073
Llama 3.1 8B Instruct
defender ethnicity
Ethnic Minority
Han
0.053
0.063
Llama 3.1 8B Instruct
defender education
Below High School
High School or Above
-0.071
0.016
Llama 3.1 8B Instruct
defender occupation
Farmer
Worker
0.058
0.036
Llama 3.1 8B Instruct
defender religion
Islamic
Atheism
0.051
0.0
Llama 3.1 8B Instruct
defender religion
Buddhism
Atheism
0.062
0.0
Llama 3.1 8B Instruct
defender religion
Christianity
Atheism
0.088
0.0
Llama 3.1 8B Instruct
defender wealth
Penniless
A Million Saving
-0.106
0.002
Llama 3.1 8B Instruct
prosecurate gender
Gender Non-Binary
Male
-0.046
0.023
Llama 3.1 8B Instruct
prosecurate gender
Female
Male
-0.078
0.008
Llama 3.1 8B Instruct
prosecurate age
Age
Age
0.23
0.0
Llama 3.1 8B Instruct
prosecurate household registration
Not Local
Local
0.065
0.006
Llama 3.1 8B Instruct
prosecurate religion
Islamic
Atheism
0.121
0.0
Llama 3.1 8B Instruct
prosecurate religion
Buddhism
Atheism
0.124
0.0
Llama 3.1 8B Instruct
prosecurate wealth
Penniless
A Million Saving
-0.192
0.0
Llama 3.1 8B Instruct
judge age
Age
Age
0.114
0.005
Llama 3.1 8B Instruct
judge gender
Female
Male
-0.06
0.001
Llama 3.1 8B Instruct
judge ethnicity
Ethnic Minority
Han
0.045
0.037
Llama 3.1 8B Instruct
judge household registration
Not Local
Local
0.026
0.049
Llama 3.1 8B Instruct
judge sexual orientation
Homosexual
Heterosexual
-0.04
0.016
Llama 3.1 8B Instruct
judge religion
Islamic
Atheism
-0.075
0.0
Llama 3.1 8B Instruct
judge political background
Other Party
Mass
0.036
0.038
Llama 3.1 8B Instruct
judge wealth
Penniless
A Million Saving
-0.053
0.067
Llama 3.1 8B Instruct
pretrial conference
Has Pretrial Conference
No Pretrial Conference
0.069
0.003
Llama 3.1 8B Instruct
judicial committee
Judicial Committee
No Judicial Committee
0.078
0.002
Llama 3.1 8B Instruct
online broadcast
Online Broadcast
No Online Broadcast
0.086
0.0
Llama 3.1 8B Instruct
court level
Intermediate Court
Primary Court
0.05
0.013
Llama 3.1 8B Instruct
court level
High Court
Primary Court
0.091
0.0
Llama 3.1 8B Instruct
compulsory measure
Compulsory Measure
No Compulsory Measure
0.061
0.083
Phi 4
defendant gender
Female
Male
-0.03
0.0
Phi 4
defendant age
Age
Age
0.019
0.085
Phi 4
defendant household registration
Not Local
Local
0.013
0.041
Phi 4
defendant nationality
Foreigner
Chinese
0.021
0.026
Phi 4
defendant political background
CCP
Mass
0.031
0.001
Phi 4
defendant wealth
Penniless
A Million Saving
-0.064
0.0
Phi 4
defendant religion
Islam
Atheism
0.022
0.084
Phi 4
defendant sexual orientation
Homosexua
Heterosexual
0.041
0.0
Phi 4
defendant sexual orientation
Bisexual
Heterosexual
0.044
0.0
Phi 4
victim religion
Islam
Atheism
0.042
0.001
Phi 4
victim religion
Buddhism
Atheism
0.054
0.001
Phi 4
victim religion
Christianity
Atheism
0.053
0.0
Phi 4
victim sexual orientation
Homosexual
Heterosexual
0.021
0.073
Phi 4
victim sexual orientation
Bisexual
Heterosexual
0.091
0.0
Phi 4
victim ethnicity
Ethnic Minority
Han
0.07
0.0
Phi 4
victim occupation
Unemployed
Worker
-0.016
0.045
Phi 4
victim household registration
Not Local
Local
-0.029
0.002
Phi 4
victim nationality
Foreigner
Chinese
0.033
0.001
Phi 4
victim wealth
Penniless
A Million Saving
-0.058
0.0
Phi 4
crime location
Rural
Urban
0.016
0.086
Phi 4
crime time
Afternoon
Morning
-0.016
0.032
Phi 4
defender gender
Gender Non-Binary
Male
-0.032
0.011
Phi 4
defender ethnicity
Ethnic Minority
Han
-0.032
0.002
Phi 4
defender education
Below High School
High School or Above
0.027
0.0
Phi 4
defender occupation
Farmer
Worker
0.022
0.024
Phi 4
defender occupation
Unemployed
Worker
0.023
0.069
Phi 4
defender political background
CCP
Mass
0.017
0.057
Phi 4
defender political background
CCP
Mass
0.017
0.057
Phi 4
defender wealth
Penniless
A Million Saving
0.03
0.012
Phi 4
prosecurate gender
Gender Non-Binary
Male
-0.021
0.024
Table A24: List of labels with statistically significant results (p−value < 0.1) in bias analysis (IV).
50

--- Page 51 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Regression
Coefficient
P-Value
Phi 4
prosecurate gender
Female
Male
-0.035
0.006
Phi 4
prosecurate ethnicity
Ethnic Minority
Han
-0.017
0.085
Phi 4
prosecurate sexual orientation
Homosexual
Heterosexual
-0.054
0.0
Phi 4
prosecurate sexual orientation
Bisexual
Heterosexual
-0.027
0.006
Phi 4
prosecurate religion
Christianity
Atheism
0.017
0.099
Phi 4
judge age
Age
Age
0.093
0.0
Phi 4
judge gender
Female
Male
-0.024
0.001
Phi 4
judge gender
Gender Non-Binary
Male
-0.027
0.011
Phi 4
judge ethnicity
Ethnic Minority
Han
0.025
0.002
Phi 4
judge household registration
Not Local
Local
-0.036
0.0
Phi 4
judge sexual orientation
Homosexual
Heterosexual
-0.018
0.056
Phi 4
judge religion
Buddhism
Atheism
0.018
0.015
Phi 4
judge political background
CCP
Mass
0.02
0.028
Phi 4
judge wealth
Penniless
A Million Saving
0.085
0.0
Phi 4
pretrial conference
With Pretrial Conference
No Pretrial Conference
-0.025
0.002
Phi 4
court level
Intermediate Court
Primary Court
0.026
0.001
Phi 4
court level
High Court
Primary Court
0.065
0.0
Phi 4
compulsory measure
Compulsory Measure
No Compulsory Measure
0.085
0.0
Phi 4
trial duration
Prolonged Litigation
Short Litigation
0.047
0.0
Phi 4
defendant household registration
Not Local
Local
0.013
0.041
Phi 4
defendant nationality
Foreigner
Chinese
0.021
0.026
Phi 4
defendant political background
CCP
Mass
0.031
0.001
Phi 4
defendant wealth
Penniless
A Million Saving
-0.064
0.0
Phi 4
defendant religion
Islam
Atheism
0.022
0.084
Phi 4
defendant sexual orientation
Homosexua
Heterosexual
0.041
0.0
Phi 4
defendant sexual orientation
Bisexual
Heterosexual
0.044
0.0
Phi 4
victim religion
Islam
Atheism
0.042
0.001
Phi 4
victim religion
Buddhism
Atheism
0.054
0.001
Phi 4
victim religion
Christianity
Atheism
0.053
0.0
Phi 4
victim sexual orientation
Homosexual
Heterosexual
0.021
0.073
Phi 4
victim sexual orientation
Bisexual
Heterosexual
0.091
0.0
Phi 4
victim ethnicity
Ethnic Minority
Han
0.07
0.0
Phi 4
victim occupation
Unemployed
Worker
-0.016
0.045
Phi 4
victim household registration
Not Local
Local
-0.029
0.002
Phi 4
victim nationality
Foreigner
Chinese
0.033
0.001
Phi 4
victim wealth
Penniless
A Million Saving
-0.058
0.0
Phi 4
crime location
Rural
Urban
0.016
0.086
Phi 4
crime time
Afternoon
Morning
-0.016
0.032
Phi 4
defender gender
Gender Non-Binary
Male
-0.032
0.011
Phi 4
defender ethnicity
Ethnic Minority
Han
-0.032
0.002
Phi 4
defender education
Below High School
High School or Above
0.027
0.0
Phi 4
defender occupation
Farmer
Worker
0.022
0.024
Phi 4
defender occupation
Unemployed
Worker
0.023
0.069
Phi 4
defender political background
CCP
Mass
0.017
0.057
Phi 4
defender wealth
Penniless
A Million Saving
0.03
0.012
Phi 4
prosecurate gender
Gender Non-Binary
Male
-0.021
0.024
Phi 4
prosecurate gender
Female
Male
-0.035
0.006
Phi 4
prosecurate ethnicity
Ethnic Minority
Han
-0.017
0.085
Phi 4
prosecurate sexual orientation
Homosexual
Heterosexual
-0.054
0.0
Phi 4
prosecurate sexual orientation
Bisexual
Heterosexual
-0.027
0.006
Phi 4
prosecurate religion
Christianity
Atheism
0.017
0.099
Phi 4
judge age
Age
Age
0.093
0.0
Phi 4
judge gender
Female
Male
-0.024
0.001
Phi 4
judge gender
Gender Non-Binary
Male
-0.027
0.011
Phi 4
judge ethnicity
Ethnic Minority
Han
0.025
0.002
Phi 4
judge household registration
Not Local
Local
-0.036
0.0
Phi 4
judge sexual orientation
Homosexual
Heterosexual
-0.018
0.056
Phi 4
judge religion
Buddhism
Atheism
0.018
0.015
Phi 4
judge political background
CCP
Mass
0.02
0.028
Phi 4
judge wealth
Penniless
A Million Saving
0.085
0.0
Phi 4
pretrial conference
With Pretrial Conference
No Pretrial Conference
-0.025
0.002
Phi 4
court level
Intermediate Court
Primary Court
0.026
0.001
Phi 4
court level
High Court
Primary Court
0.065
0.0
Phi 4
compulsory measure
Compulsory Measure
No Compulsory Measure
0.085
0.0
Phi 4
trial duration
Prolonged Litigation
Short Litigation
0.047
0.0
Table A25: List of labels with statistically significant results (p −value < 0.1) in bias analysis (V).
51

--- Page 52 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Regression
Coefficient
P-Value
LFM 7B
defendant ethnicity
Ethnic Minority
Han
0.038
0.077
LFM 7B
defendant nationality
Foreigner
Chinese
0.067
0.007
LFM 7B
defendant political background
CCP
Mass
-0.065
0.01
LFM 7B
defendant political background
Other Party
Mass
-0.037
0.071
LFM 7B
defendant wealth
Penniless
A Million Saving
0.08
0.01
LFM 7B
defendant religion
Islam
Atheism
-0.05
0.03
LFM 7B
defendant religion
Buddhism
Atheism
-0.055
0.012
LFM 7B
defendant religion
Christianity
Atheism
-0.068
0.004
LFM 7B
victim religion
Buddhism
Atheism
-0.055
0.014
LFM 7B
victim occupation
Unemployed
Worker
0.038
0.061
LFM 7B
victim nationality
Foreigner
Chinese
0.04
0.069
LFM 7B
victim wealth
Penniless
A Million Saving
0.063
0.013
LFM 7B
crime location
Rural
Urban
0.074
0.01
LFM 7B
defender gender
Gender Non-Binary
Male
-0.159
0.0
LFM 7B
defender education
Below High School
High School or Above
-0.052
0.032
LFM 7B
defender religion
Islamic
Atheism
0.097
0.003
LFM 7B
defender religion
Buddhism
Atheism
0.092
0.008
LFM 7B
defender religion
Christianity
Atheism
0.069
0.046
LFM 7B
defender sexual orientation
Homosexual
Heterosexual
-0.071
0.056
LFM 7B
defender sexual orientation
Bisexual
Heterosexual
-0.079
0.029
LFM 7B
prosecurate gender
Female
Male
-0.156
0.0
LFM 7B
prosecurate ethnicity
Ethnic Minority
Han
-0.114
0.0
LFM 7B
judge age
Age
Age
-0.126
0.008
LFM 7B
judge gender
Gender Non-Binary
Male
-0.082
0.004
LFM 7B
judge household registration
Not Local
Local
0.038
0.066
LFM 7B
judge sexual orientation
Bisexual
Heterosexual
0.049
0.048
LFM 7B
judge religion
Christianity
Atheism
-0.046
0.045
LFM 7B
judge political background
CCP
Mass
-0.039
0.068
LFM 7B
judge political background
Other Party
Mass
-0.089
0.0
LFM 7B
judge wealth
Penniless
A Million Saving
-0.513
0.0
LFM 7B
online broadcast
Online Broadcast
No Online Broadcast
0.082
0.002
LFM 7B
trial duration
Prolonged Litigation
Short Litigation
0.086
0.007
LFM 7B
recusal applied
Recusal Applied
Recusal Applied
-0.087
0.006
Mistral Small 3
defendant household registration
Not Local
Local
-0.021
0.058
Mistral Small 3
defendant wealth
Penniless
A Million Saving
-0.047
0.001
Mistral Small 3
victim gender
Gender Non-Binary
Male
-0.022
0.056
Mistral Small 3
victim ethnicity
Ethnic Minority
Han
0.038
0.002
Mistral Small 3
victim wealth
Penniless
A Million Saving
-0.031
0.005
Mistral Small 3
defender religion
Islamic
Atheism
0.03
0.03
Mistral Small 3
prosecurate age
Age
Age
0.032
0.071
Mistral Small 3
prosecurate religion
Christianity
Atheism
0.02
0.07
Mistral Small 3
prosecurate wealth
Penniless
A Million Saving
-0.027
0.069
Mistral Small 3
judge age
Age
Age
0.124
0.0
Mistral Small 3
judge gender
Gender Non-Binary
Male
-0.07
0.0
Mistral Small 3
judge ethnicity
Ethnic Minority
Han
0.034
0.003
Mistral Small 3
judge household registration
Not Local
Local
-0.023
0.032
Mistral Small 3
judge sexual orientation
Homosexual
Heterosexual
0.027
0.06
Mistral Small 3
judge sexual orientation
Bisexual
Heterosexual
0.03
0.017
Mistral Small 3
judge religion
Islamic
Atheism
0.089
0.0
Mistral Small 3
judge religion
Buddhism
Atheism
0.059
0.0
Mistral Small 3
judge religion
Christianity
Atheism
0.05
0.0
Mistral Small 3
judge political background
CCP
Mass
0.1
0.0
Mistral Small 3
judge political background
Other Party
Mass
0.054
0.0
Mistral Small 3
court level
High Court
Primary Court
0.016
0.066
Mistral Small 3
compulsory measure
Compulsory Measure
No Compulsory Measure
0.021
0.1
Mistral Small 3
trial duration
Prolonged Litigation
Short Litigation
0.02
Mistral NeMo
defendant gender
Female
Male
0.078
0.003
Mistral NeMo
defendant ethnicity
Ethnic Minority
Han
-0.14
0.0
Mistral NeMo
defendant political background
CCP
Mass
0.03
0.025
Mistral NeMo
defendant political background
Other Party
Mass
0.057
0.001
Mistral NeMo
defendant wealth
Penniless
A Million Saving
-0.128
0.0
Mistral NeMo
victim ethnicity
Ethnic Minority
Han
0.051
0.006
Mistral NeMo
victim education
Below High School
High School or Above
-0.073
0.001
Mistral NeMo
victim occupation
Unemployed
Worker
-0.041
0.006
Mistral NeMo
crime date
Summer
Spring
-0.017
0.058
Mistral NeMo
defender age
Age
Age
-0.046
0.063
Mistral NeMo
defender education
Below High School
High School or Above
-0.035
0.019
Mistral NeMo
defender sexual orientation
Homosexual
Heterosexual
-0.037
0.015
Mistral NeMo
defender sexual orientation
Bisexual
Heterosexual
-0.051
0.003
Mistral NeMo
prosecurate sexual orientation
Homosexual
Heterosexual
-0.036
0.023
Table A26: List of labels with statistically significant results (p−value < 0.1) in bias analysis (VI).
52

--- Page 53 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Regression
Coefficient
P-Value
Mistral NeMo
prosecurate sexual orientation
Bisexual
Heterosexual
-0.048
0.002
Mistral NeMo
prosecurate religion
Buddhism
Atheism
-0.035
0.035
Mistral NeMo
prosecurate religion
Christianity
Atheism
-0.032
0.05
Mistral NeMo
prosecurate wealth
Penniless
A Million Saving
0.032
0.097
Mistral NeMo
judge age
Age
Age
0.071
0.057
Mistral NeMo
judge gender
Gender Non-Binary
Male
-0.055
0.007
Mistral NeMo
judge ethnicity
Ethnic Minority
Han
0.053
0.002
Mistral NeMo
judge household registration
Not Local
Local
-0.029
0.01
Mistral NeMo
judge sexual orientation
Homosexual
Heterosexual
-0.034
0.042
Mistral NeMo
judge sexual orientation
Bisexual
Heterosexual
0.028
0.082
Mistral NeMo
judge political background
CCP
Mass
0.04
0.013
Mistral NeMo
judge political background
Other Party
Mass
0.031
0.037
Mistral NeMo
assessor
No Preple’s Assessor
With People’s Assessor
0.017
0.087
Mistral NeMo
open trial
Open Trial
Not Open Trial
0.025
0.075
Mistral NeMo
court level
Intermediate Court
Primary Court
0.048
0.007
Mistral NeMo
court level
High Court
Primary Court
0.048
0.01
Mistral NeMo
court location
Court Rural
Court Urban
-0.03
0.054
Mistral NeMo
compulsory measure
Compulsory Measure
No Compulsory Measure
0.096
0.0
DeepSeek R1 32B
defendant gender
Female
Male
0.072
0.002
DeepSeek R1 32B
defendant ethnicity
Ethnic Minority
Han
-0.136
0.0
DeepSeek R1 32B
defendant sexual orientation
Homosexua
Heterosexual
-0.028
0.087
DeepSeek R1 32B
victim gender
Female
Male
0.051
0.038
DeepSeek R1 32B
victim ethnicity
Ethnic Minority
Han
0.075
0.004
DeepSeek R1 32B
victim education
Below High School
High School or Above
-0.044
0.064
DeepSeek R1 32B
victim occupation
Unemployed
Worker
-0.053
0.02
DeepSeek R1 32B
victim household registration
Not Local
Local
-0.048
0.046
DeepSeek R1 32B
victim wealth
Penniless
A Million Saving
0.043
0.091
DeepSeek R1 32B
defender education
Below High School
High School or Above
-0.041
0.03
DeepSeek R1 32B
defender religion
Islamic
Atheism
-0.035
0.099
DeepSeek R1 32B
defender religion
Christianity
Atheism
-0.037
0.076
DeepSeek R1 32B
prosecurate sexual orientation
Homosexual
Heterosexual
-0.039
0.098
DeepSeek R1 32B
prosecurate wealth
Penniless
A Million Saving
0.048
0.032
DeepSeek R1 32B
judge age
Age
Age
0.068
0.081
DeepSeek R1 32B
judge religion
Buddhism
Atheism
-0.039
0.031
DeepSeek R1 32B
judge religion
Christianity
Atheism
-0.032
0.061
DeepSeek R1 32B
judicial committee
With Judicial Committee
No Judicial Committee
0.036
0.078
DeepSeek R1 32B
online broadcast
Online Broadcast
No Online Broadcast
0.049
0.015
DeepSeek R1 32B
open trial
Open Trial
Not Open Trial
0.043
0.028
DeepSeek R1 32B
court level
Intermediate Court
Primary Court
0.033
0.068
DeepSeek R1 32B
court level
High Court
Primary Court
0.064
0.002
DeepSeek R1 32B
compulsory measure
Compulsory Measure
No Compulsory Measure
-0.046
0.053
DeepSeek R1 32B
recusal applied
Recusal Applied
Recusal Applied
-0.043
0.048
DeepSeek R1 32B
immediate judgement
Immediate ment
Not Immediate ment
-0.036
0.083
Table A27: Detailed information of labels with statistically significant results (p −value < 0.1) in
bias analysis (VII).
53

--- Page 54 ---

Working Paper
E.4
ROBUSTNESS CHECKS ON BIAS ANALYSIS
As bias analysis is important in LLM fairness evaluation, we present a series of robustness checks
based on the LLMs with a temperature of 0, as well as those based on the LLMs with a temperature
of 1, to examine the results related to biases in the main analysis. In general, all robustness checks
show consistent patterns and confirm that LLMs in our studies show significant biases.
E.4.1
REGRESSIONS USING ROBUST STANDARD ERROR
Here, we modify the original regression model by applying heteroskedasticity-robust standard er-
rors. This table presents the number of p-values below 0.1, calculated using robust standard errors,
across various models. The results do not differ much from the main analysis.
Model Name
Label Category
Label Number
Biased Label Number
Glm 4
Substance label
25
9
Glm 4
Procedure label
40
18
Glm 4 Flash
Substance label
25
15
Glm 4 Flash
Procedure label
40
11
Qwen2.5 72B Instruct
Substance label
25
9
Qwen2.5 72B Instruct
Procedure label
40
21
Qwen2.5 7B Instruct
Substance label
25
9
Qwen2.5 7B Instruct
Procedure label
40
14
Gemini Flash 1.5
Substance label
25
11
Gemini Flash 1.5
Procedure label
40
19
Gemini Flash 1.5 8B
Substance label
25
14
Gemini Flash 1.5 8B
Procedure label
40
20
LFM 40B MoE
Substance label
25
2
LFM 40B MoE
Procedure label
40
10
Nova Lite 1.0
Substance label
25
11
Nova Lite 1.0
Procedure label
40
13
Nova Micro 1.0
Substance label
25
8
Nova Micro 1.0
Procedure label
40
16
Llama 3.1 8B Instruct
Substance label
25
7
Llama 3.1 8B Instruct
Procedure label
40
19
Phi 4
Substance label
25
17
Phi 4
Procedure label
40
21
LFM 7B
Substance label
25
10
LFM 7B
Procedure label
40
16
Mistral Small 3
Substance label
25
5
Mistral Small 3
Procedural label
40
14
Mistral NeMo
Substance label
25
8
Mistral NeMo
Procedure label
40
18
DeepSeek R1 32B
Substance label
25
9
DeepSeek R1 32B
Procedure label
40
13
Table A28: Number of labels with statistically significant results (p −value < 0.1) in robust
standard error analysis with a temperature of 0.
54

--- Page 55 ---

Working Paper
Model Name
Label Category
Label Number
Biased Label Number
DeepSeek R1 32B
Substance label
25
9
DeepSeek R1 32B
Procedural label
40
13
DeepSeek v3
Substance label
25
3
DeepSeek v3
Procedural label
40
9
Gemini 1.5 8B
Substance label
25
10
Gemini 1.5 8B
Procedural label
40
15
Gemini Flash 1.5
Substance label
25
9
Gemini Flash 1.5
Procedural label
40
14
GLM4
Substance label
25
9
GLM4
Procedural label
40
22
GLM4 Flash
Substance label
25
15
GLM4 Flash
Procedural label
40
16
LFM 7B
Substance label
25
5
LFM 7B
Procedural label
40
12
LFM 40B
Substance label
25
5
LFM 40B
Procedural label
40
10
Mistral Small 3
Substance label
25
2
Mistral Small 3
Procedural label
40
11
Mistral NeMo t1
Substance label
25
4
Mistral NeMo t1
Procedural label
40
11
NOVA Lite
Substance label
25
10
NOVA Lite
Procedural label
40
10
NOVA Mico
Substance label
25
6
NOVA Mico
Procedural label
40
7
PHI4
Substance label
25
6
PHI4
Procedural label
40
8
Qwen 2.5 7B Instruct
Substance label
25
5
Qwen 2.5 7B Instruct
Procedural label
40
13
Qwen 2.5 72B
Substance label
25
6
Qwen 2.5 72B
Procedural label
40
8
Table A29: Number of labels with statistically significant results (p −value < 0.1) in robust
standard error analysis with a temperature of 1.
55

--- Page 56 ---

Working Paper
E.4.2
REGRESSIONS WITH STANDARD ERRORS CLUSTERED AT THE CRIME CATEGORY
LEVEL
In this robustness check, we cluster the standard errors by crime type to account for intra-group
correlations that may arise from legal and procedural similarities within the same category of crime.
This adjustment allows for reliable inference by addressing potential biases in standard error estima-
tion, ensuring that the observed p-values accurately reflect the true statistical significance of biases
across different crime categories.
Model Name
Label Category
Label Number
Biased Label Number
Glm 4
Substance label
25
11
Glm 4
Procedure label
40
16
Glm 4 Flash
Substance label
25
16
Glm 4 Flash
Procedure label
40
10
Qwen2.5 72B Instruct
Substance label
25
8
Qwen2.5 72B Instruct
Procedure label
40
24
Qwen2.5 7B Instruct
Substance label
25
10
Qwen2.5 7B Instruct
Procedure label
40
15
Gemini Flash 1.5
Substance label
25
10
Gemini Flash 1.5
Procedure label
40
20
Gemini Flash 1.5 8B
Substance label
25
13
Gemini Flash 1.5 8B
Procedure label
40
21
LFM 40B MoE
Substance label
25
3
LFM 40B MoE
Procedure label
40
10
Nova Lite 1.0
Substance label
25
11
Nova Lite 1.0
Procedure label
40
12
Nova Micro 1.0
Substance label
25
7
Nova Micro 1.0
Procedure label
40
18
Llama 3.1 8B Instruct
Substance label
25
6
Llama 3.1 8B Instruct
Procedure label
40
19
Phi 4
Substance label
25
16
Phi 4
Procedure label
40
21
LFM 7B
Substance label
25
12
LFM 7B
Procedure label
40
18
Mistral Small 3
Substance label
25
6
Mistral Small 3
Procedural label
40
13
Mistral NeMo
Substance label
25
9
Mistral NeMo
Procedure label
40
16
DeepSeek R1 32B
Substance label
25
9
DeepSeek R1 32B
Procedure label
40
13
Table A30: Number of labels with statistically significant results (p −value < 0.1) based on
regressions with standard errors clustered at the crime category level with a temperature of 0.
56

--- Page 57 ---

Working Paper
Model Name
Label Category
Label Number
Biased Label Number
DeepSeek R1 32B
Substance label
25
9
DeepSeek R1 32B
Procedural label
40
13
DeepSeek v3
Substance label
25
4
DeepSeek v3
Procedural label
40
8
Gemini 1.5 8B
Substance label
25
9
Gemini 1.5 8B
Procedural label
40
13
Gemini Flash 1.5
Substance label
25
10
Gemini Flash 1.5
Procedural label
40
14
GLM4
Substance label
25
11
GLM4
Procedural label
40
21
GLM4 Flash
Substance label
25
16
GLM4 Flash
Procedural label
40
15
LFM 7B
Substance label
25
4
LFM 7B
Procedural label
40
14
LFM 40B
Substance label
25
6
LFM 40B
Procedural label
40
12
Llama 3.1
Substance label
25
6
Llama 3.1
Procedural label
40
24
Mistral Small 3
Substance label
25
1
Mistral Small 3
Procedural label
40
12
Mistral NeMo t1
Substance label
25
7
Mistral NeMo t1
Procedural label
40
13
NOVA Lite
Substance label
25
9
NOVA Lite
Procedural label
40
10
NOVA Mico
Substance label
25
5
NOVA Mico
Procedural label
40
6
PHI4
Substance label
25
9
PHI4
Procedural label
40
9
Qwen 2.5 7B Instruct
Substance label
25
5
Qwen 2.5 7B Instruct
Procedural label
40
14
Qwen 2.5 72B
Substance label
25
7
Qwen 2.5 72B
Procedural label
40
9
Table A31: Number of labels with statistically significant results (p −value < 0.1) based on
regressions with standard errors clustered at the crime category level with a temperature of 1.
57

--- Page 58 ---

Working Paper
E.4.3
REGRESSIONS ON FULL-SENTENCE LENGTH
We follow the methodology of a prior Chinese empirical legal study to standardize sentencing terms
of various types of judicial outcomes for analysis. Specifically, life imprisonment and suspended
death sentences are converted to 400 months, while immediate death sentences are represented as
600 months. Additionally, in accordance with Chinese criminal law, one day of pre-trial detention
is equivalent to two days of public surveillance or one day of restricted incarceration/fixed-term
imprisonment. As a result, one month of limited incarceration is converted to one month of fixed-
term imprisonment, and two months of public surveillance are converted to one month of fixed-term
imprisonment. Using this method, we replace the original dependent variable with the new variable
that incorporates all major sentencing types into analysis, enabling a broader analysis on the dataset.
Using the same methodology in the main regressions, we take the natural logarithm of this variable.
58

--- Page 59 ---

Working Paper
Model Name
Label Category
Label Number
Biased Label Number
Glm 4
Substance label
25
9
Glm 4
Procedure label
40
15
Glm 4 Flash
Substance label
25
15
Glm 4 Flash
Procedure label
40
11
Qwen2.5 72B Instruct
Substance label
25
11
Qwen2.5 72B Instruct
Procedure label
40
21
Qwen2.5 7B Instruct
Substance label
25
10
Qwen2.5 7B Instruct
Procedure label
40
18
Gemini Flash 1.5
Substance label
25
10
Gemini Flash 1.5
Procedure label
40
18
Gemini Flash 1.5 8B
Substance label
25
12
Gemini Flash 1.5 8B
Procedure label
40
20
LFM 40B MoE
Substance label
25
3
LFM 40B MoE
Procedure label
40
8
Nova Lite 1.0
Substance label
25
11
Nova Lite 1.0
Procedure label
40
13
Nova Micro 1.0
Substance label
25
8
Nova Micro 1.0
Procedure label
40
17
Llama 3.1 8B Instruct
Substance label
25
7
Llama 3.1 8B Instruct
Procedure label
40
17
Phi 4
Substance label
25
17
Phi 4
Procedure label
40
22
LFM 7B
Substance label
25
10
LFM 7B
Procedure label
40
15
Mistral Small 3
Substance label
25
5
Mistral Small 3
Procedure label
40
13
Mistral NeMo
Substance label
25
7
Mistral NeMo
Procedure label
40
17
DeepSeek R1 32B
Substance label
25
7
DeepSeek R1 32B
Procedure label
40
11
Table A32: Number of labels with statistically significant results (p−value < 0.1) from regressions
on full-sentence length with a temperature of 0.
59

--- Page 60 ---

Working Paper
Model Name
Label Category
Label Number
Biased Label Number
DeepSeek R1 32B
Substance label
25
7
DeepSeek R1 32B
Procedural label
40
11
DeepSeek v3
Substance label
25
4
DeepSeek v3
Procedural label
40
9
Gemini 1.5 8B
Substance label
25
8
Gemini 1.5 8B
Procedural label
40
15
Gemini Flash 1.5
Substance label
25
8
Gemini Flash 1.5
Procedural label
40
13
GLM4
Substance label
25
9
GLM4
Procedural label
40
19
GLM4 Flash
Substance label
25
15
GLM4 Flash
Procedural label
40
16
LFM 7B
Substance label
25
7
LFM 7B
Procedural label
40
13
LFM 40B
Substance label
25
2
LFM 40B
Procedural label
40
11
Mistral Small 3
Substance label
25
4
Mistral Small 3
Procedural label
40
13
Mistral NeMo t1
Substance label
25
2
Mistral NeMo t1
Procedural label
40
9
NOVA Lite
Substance label
25
8
NOVA Lite
Procedural label
40
9
NOVA Mico
Substance label
25
7
NOVA Mico
Procedural label
40
8
PHI4
Substance label
25
6
PHI4
Procedural label
40
9
Qwen 2.5 7B Instruct
Substance label
25
4
Qwen 2.5 7B Instruct
Procedural label
40
10
Qwen 2.5 72B
Substance label
25
4
Qwen 2.5 72B
Procedural label
40
11
Table A33: Number of labels with statistically significant results (p−value < 0.1) from regressions
on full-sentence length with a temperature of 1.
60

--- Page 61 ---

Working Paper
E.4.4
REGRESSIONS EXCLUDING CASES FILED BEFORE 2014
We exclude cases filed before January 1, 2014, to mitigate potential selection bias stemming from
non-systematic disclosure of judicial documents. On that date, The Supreme People’s Court Pro-
visions on People’s Courts Release of Judgments on the Internet came into effect, mandating the
public release of most adjudications. Prior to this regulation, the publication of court rulings in
China was much more restricted and inconsistent, potentially leading to a bigger difference between
the types of cases made publicly accessible and those not publicly accessible. Here, by restricting
our dataset to cases filed after this policy made judicial publication more prevalent and consistent,
we aim to reduce the potential selection bias and enhance the representativeness and reliability of
our analysis.
Model Name
Label Category
Label Number
Biased Label Number
Glm 4
Substance label
25
8
Glm 4
Procedure label
40
16
Glm 4 Flash
Substance label
25
15
Glm 4 Flash
Procedure label
40
11
Qwen2.5 72B Instruct
Substance label
25
9
Qwen2.5 72B Instruct
Procedure label
40
22
Qwen2.5 7B Instruct
Substance label
25
8
Qwen2.5 7B Instruct
Procedure label
40
14
Gemini Flash 1.5
Substance label
25
12
Gemini Flash 1.5
Procedure label
40
20
Gemini Flash 1.5 8B
Substance label
25
11
Gemini Flash 1.5 8B
Procedure label
40
20
LFM 40B MoE
Substance label
25
2
LFM 40B MoE
Procedure label
40
8
Nova Lite 1.0
Substance label
25
10
Nova Lite 1.0
Procedure label
40
12
Nova Micro 1.0
Substance label
25
8
Nova Micro 1.0
Procedure label
40
15
Llama 3.1 8B Instruct
Substance label
25
7
Llama 3.1 8B Instruct
Procedure label
40
20
Phi 4
Substance label
25
15
Phi 4
Procedure label
40
21
LFM 7B
Substance label
25
10
LFM 7B
Procedure label
40
18
Mistral Small 3
Substance label
25
4
Mistral Small 3
Procedure label
40
13
Mistral NeMo
Substance label
25
8
Mistral NeMo
Procedure label
40
20
DeepSeek R1 32B
Substance label
25
7
DeepSeek R1 32B
Procedure label
40
12
Table A34: Number of labels with statistically significant results (p −value < 0.1) excluding cases
filed before 2014 with a temperature of 0.
61

--- Page 62 ---

Working Paper
Model Name
Label Category
Label Number
Biased Label Number
DeepSeek R1 32B
Substance label
25
7
DeepSeek R1 32B
Procedural label
40
12
DeepSeek v3
Substance label
25
3
DeepSeek v3
Procedural label
40
11
Gemini 1.5 8B
Substance label
25
11
Gemini 1.5 8B
Procedural label
40
15
Gemini Flash 1.5
Substance label
25
10
Gemini Flash 1.5
Procedural label
40
11
GLM4
Substance label
25
8
GLM4
Procedural label
40
19
GLM4 Flash
Substance label
25
15
GLM4 Flash
Procedural label
40
16
LFM 7B
Substance label
25
6
LFM 7B
Procedural label
40
13
LFM 40B
Substance label
25
4
LFM 40B
Procedural label
40
10
Mistral Small 3
Substance label
25
1
Mistral Small 3
Procedural label
40
11
Mistral NeMo t1
Substance label
25
5
Mistral NeMo t1
Procedural label
40
6
NOVA Lite
Substance label
25
8
NOVA Lite
Procedural label
40
10
NOVA Mico
Substance label
25
6
NOVA Mico
Procedural label
40
9
PHI4
Substance label
25
5
PHI4
Procedural label
40
8
Qwen 2.5 7B Instruct
Substance label
25
5
Qwen 2.5 7B Instruct
Procedural label
40
14
Qwen 2.5 72B
Substance label
25
4
Qwen 2.5 72B
Procedural label
40
10
Table A35: Number of labels with statistically significant results (p −value < 0.1) excluding cases
filed before 2014 with a temperature of 1.
62

--- Page 63 ---

Working Paper
F
DETAILED RESULTS OF IMBALANCED INACCURACY ANALYSIS
F.1
NUMBER OF LABELS WITH STATISTICALLY SIGNIFICANT RESULTS IN IMBALANCED
INACCURACY ANALYSIS
This table displays the number of labels featuring statistically significant results with p-values below
0.1 in imbalanced inaccuracy analysis across all models with a temperature of 0.
Model Name
Label Category
Label Number
Biased Label Number
Glm 4
Substance label
25
5
Glm 4
Procedure label
40
14
Glm 4 Flash
Substance label
25
12
Glm 4 Flash
Procedure label
40
6
Qwen2.5 72B Instruct
Substance label
25
10
Qwen2.5 72B Instruct
Procedure label
40
19
Qwen2.5 7B Instruct
Substance label
25
8
Qwen2.5 7B Instruct
Procedure label
40
20
Gemini Flash 1.5
Substance label
25
13
Gemini Flash 1.5
Procedure label
40
22
Gemini Flash 1.5 8B
Substance label
25
11
Gemini Flash 1.5 8B
Procedure label
40
20
LFM 40B MoE
Substance label
25
3
LFM 40B MoE
Procedure label
40
12
Nova Lite 1.0
Substance label
25
9
Nova Lite 1.0
Procedure label
40
13
Nova Micro 1.0
Substance label
25
7
Nova Micro 1.0
Procedure label
40
16
Llama 3.1 8B Instruct
Substance label
25
6
Llama 3.1 8B Instruct
Procedure label
40
10
Phi 4
Substance label
25
12
Phi 4
Procedure label
40
13
LFM 7B
Substance label
25
11
LFM 7B
Procedure label
40
14
Mistral Small 3
Substance label
25
6
Mistral Small 3
Procedure label
40
11
Mistral NeMo
Substance label
25
8
Mistral NeMo
Procedure label
40
12
DeepSeek R1 32B
Substance label
25
5
DeepSeek R1 32B
Procedure label
40
4
Table A36: Number of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy analysis with a temperature of 0.
63

--- Page 64 ---

Working Paper
The following table displays the number of labels featuring statistically significant results with p-
values below 0.1 in unfair imbalance analysis across all models with a temperature of 1.
Model Name
Label Category
Label Number
Biased Label Number
DeepSeek R1 32B
Substance label
25
5
DeepSeek R1 32B
Procedure label
40
4
DeepSeek v3
Substance label
25
2
DeepSeek v3
Procedure label
40
12
Gemini 1.5 8B
Substance label
25
7
Gemini 1.5 8B
Procedure label
40
12
Gemini Flash 1.5
Substance label
25
11
Gemini Flash 1.5
Procedure label
40
14
GLM4
Substance label
25
5
GLM4
Procedure label
40
17
GLM4 Flash
Substance label
25
12
GLM4 Flash
Procedure label
40
10
LFM 7B
Substance label
25
4
LFM 7B
Procedure label
40
10
LFM 40B
Substance label
25
2
LFM 40B
Procedure label
40
11
Llama 3.1
Substance label
25
6
Llama 3.1
Procedure label
40
15
Mistral Small 3
Substance label
25
0
Mistral Small 3
Procedure label
40
7
Mistral NeMo t1
Substance label
25
4
Mistral NeMo t1
Procedure label
40
5
NOVA Lite
Substance label
25
8
NOVA Lite
Procedure label
40
11
NOVA Mico
Substance label
25
5
NOVA Mico
Procedure label
40
8
PHI4
Substance label
25
4
PHI4
Procedure label
40
5
Qwen 2.5 7B Instruct
Substance label
25
6
Qwen 2.5 7B Instruct
Procedure label
40
11
Qwen 2.5 72B
Substance label
25
5
Qwen 2.5 72B
Procedure label
40
3
Table A37: Number of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy analysis with a temperature of 1.
64

--- Page 65 ---

Working Paper
F.2
DETAILED OF LABELS WITH STATISTICALLY SIGNIFICANT RESULTS IN IMBALANCED
INACCURACY ANALYSIS
The following table displays list of p-value below 0.1 in Imbalanced Inaccuracy Analysis across
multiple models. The temperature is set to 0.
Model Name
Label Name
Label Value
Reference
Impact
on
Sentence
Prediction
(Months)
P-Value
Glm 4
defendant political background
CCP
Mass
1.45
0.08
Glm 4
defendant wealth
Penniless
A Million Saving
-2.96
0.0
Glm 4
victim gender
Female
Male
0.637
0.043
Glm 4
victim age
Age
Age
1.545
0.013
Glm 4
victim wealth
Penniless
A Million Saving
-3.11
0.0
Glm 4
defender gender
Female
Male
-1.701
0.035
Glm 4
defender political background
Other Party
Mass
-1.743
0.031
Glm 4
defender religion
Islamic
Atheism
1.363
0.064
Glm 4
defender religion
Buddhism
Atheism
1.599
0.07
Glm 4
defender sexual orientation
Homosexual
Heterosexual
1.48
0.024
Glm 4
defender sexual orientation
Bisexual
Heterosexual
2.14
0.008
Glm 4
prosecurate age
Age
Age
2.331
0.013
Glm 4
prosecurate ethnicity
Ethnic Minority
Han
-1.639
0.021
Glm 4
prosecurate wealth
Penniless
A Million Saving
-1.789
0.055
Glm 4
judge gender
Female
Male
-1.107
0.086
Glm 4
judge sexual orientation
Homosexual
Heterosexual
-3.957
0.001
Glm 4
judge political background
Other Party
Mass
1.412
0.071
Glm 4
judge wealth
Penniless
A Million Saving
3.357
0.001
Glm 4
assessor
No preple’s assessor
Has people’s assessor
-1.267
0.015
Glm 4
defender type
Appointed
Privately Attained
-1.863
0.02
Glm 4
pretrial conference
Has Pretrial Conference
No Pretrial Conference
-1.124
0.094
Glm 4
court level
Intermediate Court
Primary Court
3.517
0.0
Glm 4
court level
High Court
Primary Court
3.851
0.0
Glm 4
court location
Court Rural
Court Urban
-2.456
0.003
Glm 4
trial duration
Prolonged Trial Duration
Note-Short Trial
2.799
0.001
Glm 4 Flash
defendant gender
Female
Male
2.954
0.027
Glm 4 Flash
defendant ethnicity
Ethnic Minority
Han
-4.901
0.0
Glm 4 Flash
defendant age
Age
Age
4.108
0.042
Glm 4 Flash
defendant nationality
Foreigner
Chinese
1.716
0.02
Glm 4 Flash
defendant political background
CCP
Mass
2.512
0.001
Glm 4 Flash
defendant wealth
Penniless
A Million Saving
-7.27
0.0
Glm 4 Flash
defendant sexual orientation
Bisexual
Heterosexual
1.365
0.02
Glm 4 Flash
victim religion
Islam
Atheism
0.928
0.047
Glm 4 Flash
victim sexual orientation
Homosexual
Heterosexual
1.172
0.032
Glm 4 Flash
victim ethnicity
Ethnic Minority
Han
1.62
0.009
Glm 4 Flash
victim nationality
Foreigner
Chinese
2.715
0.001
Glm 4 Flash
victim wealth
Penniless
A Million Saving
-5.081
0.0
Glm 4 Flash
defender education
Below High School
High School or Above
1.828
0.02
Glm 4 Flash
defender wealth
Penniless
A Million Saving
-2.143
0.026
Glm 4 Flash
prosecurate age
Age
Age
3.664
0.005
Glm 4 Flash
prosecurate ethnicity
Ethnic Minority
Han
-1.959
0.022
Glm 4 Flash
prosecurate religion
Islamic
Atheism
-1.483
0.085
Glm 4 Flash
prosecurate religion
Buddhism
Atheism
-1.749
0.039
Glm 4 Flash
prosecurate religion
Christianity
Atheism
-2.47
0.008
Glm 4 Flash
prosecurate political background
CCP
Mass
-1.444
0.024
Glm 4 Flash
judge ethnicity
Ethnic Minority
Han
2.969
0.002
Glm 4 Flash
judge sexual orientation
Homosexual
Heterosexual
-4.271
0.001
Glm 4 Flash
judge sexual orientation
Bisexual
Heterosexual
-2.759
0.014
Glm 4 Flash
judge wealth
Penniless
A Million Saving
3.502
0.004
Glm 4 Flash
court level
High Court
Primary Court
2.244
0.022
Qwen2.5 72B Instruct
defendant gender
Female
Male
-3.289
0.0
Qwen2.5 72B Instruct
defendant gender
Non-Binary
Male
-1.571
0.027
Qwen2.5 72B Instruct
defendant education
Below High School
High School or Above
1.278
0.041
Qwen2.5 72B Instruct
defendant age
Age
Age
2.957
0.014
Qwen2.5 72B Instruct
defendant wealth
Penniless
A Million Saving
-1.274
0.036
Qwen2.5 72B Instruct
defendant sexual orientation
Bisexual
Heterosexual
-1.096
0.083
Qwen2.5 72B Instruct
victim religion
Christianity
Atheism
-1.274
0.043
Qwen2.5 72B Instruct
victim sexual orientation
Bisexual
Heterosexual
-1.224
0.061
Qwen2.5 72B Instruct
victim occupation
Farmer
Worker
1.078
0.093
Qwen2.5 72B Instruct
victim wealth
Penniless
A Million Saving
-0.979
0.076
Qwen2.5 72B Instruct
crime date
Summer
Spring
1.305
0.015
Qwen2.5 72B Instruct
crime date
Autumn
Spring
1.051
0.036
Qwen2.5 72B Instruct
crime date
Winter
Spring
1.305
0.016
Table A38: List of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy analysis (I).
65

--- Page 66 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Impact
on
Sentence
Prediction
(Months)
P-Value
Qwen2.5 72B Instruct
defender gender
Gender Non-Binary
Male
-1.822
0.009
Qwen2.5 72B Instruct
defender household registration
Not Local
Local
0.988
0.095
Qwen2.5 72B Instruct
defender sexual orientation
Homosexual
Heterosexual
-1.618
0.035
Qwen2.5 72B Instruct
prosecurate gender
Gender Non-Binary
Male
-1.249
0.051
Qwen2.5 72B Instruct
prosecurate gender
Female
Male
-1.481
0.03
Qwen2.5 72B Instruct
prosecurate sexual orientation
Homosexual
Heterosexual
-1.246
0.064
Qwen2.5 72B Instruct
judge age
Age
Age
7.067
0.0
Qwen2.5 72B Instruct
judge gender
Female
Male
1.653
0.028
Qwen2.5 72B Instruct
judge gender
Gender Non-Binary
Male
-1.605
0.033
Qwen2.5 72B Instruct
judge sexual orientation
Homosexual
Heterosexual
-3.047
0.0
Qwen2.5 72B Instruct
judge religion
Islamic
Atheism
6.738
0.0
Qwen2.5 72B Instruct
judge religion
Christianity
Atheism
1.337
0.076
Qwen2.5 72B Instruct
judge political background
Other Party
Mass
-1.646
0.019
Qwen2.5 72B Instruct
judge wealth
Penniless
A Million Saving
5.101
0.0
Qwen2.5 72B Instruct
collegial panel
Collegial Panel
Single
1.122
0.056
Qwen2.5 72B Instruct
assessor
No Preple’s Assessor
With People’s Assessor
1.498
0.015
Qwen2.5 72B Instruct
pretrial conference
With Pretrial Conference
No Pretrial Conference
-2.046
0.001
Qwen2.5 72B Instruct
court level
Intermediate Court
Primary Court
3.091
0.0
Qwen2.5 72B Instruct
court level
High Court
Primary Court
2.5
0.001
Qwen2.5 72B Instruct
court location
Court Rural
Court Urban
-1.337
0.039
Qwen2.5 72B Instruct
compulsory measure
Compulsory Measure
No Compulsory Measure
2.44
0.006
Qwen2.5 72B Instruct
trial duration
Prolonged Litigation
Short Litigation
2.114
0.002
Qwen2.5 72B Instruct
recusal applied
Recusal Applied
Recusal Applied
-2.593
0.001
Qwen2.5 7B Instruct
defendant gender
Female
Male
9.975
0.0
Qwen2.5 7B Instruct
defendant ethnicity
Ethnic Minority
Han
-10.329
0.0
Qwen2.5 7B Instruct
defendant household registration
Not Local
Local
-1.03
0.058
Qwen2.5 7B Instruct
defendant wealth
Penniless
A Million Saving
-1.353
0.025
Qwen2.5 7B Instruct
defendant sexual orientation
Homosexua
Heterosexual
1.707
0.012
Qwen2.5 7B Instruct
defendant sexual orientation
Bisexual
Heterosexual
1.887
0.015
Qwen2.5 7B Instruct
victim political background
Other Party
Mass
1.048
0.002
Qwen2.5 7B Instruct
victim wealth
Penniless
A Million Saving
-1.012
0.057
Qwen2.5 7B Instruct
crime date
Summer
Spring
1.19
0.068
Qwen2.5 7B Instruct
crime date
Winter
Spring
1.995
0.002
Qwen2.5 7B Instruct
defender occupation
Farmer
Worker
-0.927
0.099
Qwen2.5 7B Instruct
defender political background
CCP
Mass
2.096
0.003
Qwen2.5 7B Instruct
defender sexual orientation
Homosexual
Heterosexual
-1.913
0.004
Qwen2.5 7B Instruct
defender sexual orientation
Bisexual
Heterosexual
-1.372
0.028
Qwen2.5 7B Instruct
prosecurate gender
Gender Non-Binary
Male
-1.45
0.017
Qwen2.5 7B Instruct
prosecurate gender
Female
Male
-2.12
0.006
Qwen2.5 7B Instruct
prosecurate religion
Islamic
Atheism
1.422
0.063
Qwen2.5 7B Instruct
prosecurate wealth
Penniless
A Million Saving
-1.625
0.057
Qwen2.5 7B Instruct
judge gender
Female
Male
-1.503
0.021
Qwen2.5 7B Instruct
judge gender
Gender Non-Binary
Male
-2.039
0.01
Qwen2.5 7B Instruct
judge ethnicity
Ethnic Minority
Han
1.419
0.009
Qwen2.5 7B Instruct
judge religion
Islamic
Atheism
2.693
0.001
Qwen2.5 7B Instruct
judge political background
Other Party
Mass
-1.385
0.073
Qwen2.5 7B Instruct
judge wealth
Penniless
A Million Saving
3.568
0.0
Qwen2.5 7B Instruct
assessor
No Preple’s Assessor
With People’s Assessor
1.238
0.011
Qwen2.5 7B Instruct
pretrial conference
With Pretrial Conference
No Pretrial Conference
1.147
0.072
Qwen2.5 7B Instruct
judicial committee
With Judicial Committee
No Judicial Committee
1.971
0.001
Qwen2.5 7B Instruct
court level
Intermediate Court
Primary Court
0.851
0.068
Qwen2.5 7B Instruct
court level
High Court
Primary Court
1.894
0.004
Qwen2.5 7B Instruct
court location
Court Rural
Court Urban
1.382
0.035
Qwen2.5 7B Instruct
compulsory measure
Compulsory Measure
No Compulsory Measure
4.348
0.001
Qwen2.5 7B Instruct
trial duration
Prolonged Litigation
Short Litigation
-2.175
0.023
Qwen2.5 7B Instruct
recusal applied
Recusal Applied
Recusal Applied
-6.065
0.0
Qwen2.5 7B Instruct
immediate judgement
Immediate ment
Not Immediate ment
-2.545
0.0
Gemini Flash 1.5
defendant gender
Female
Male
7.442
0.0
Gemini Flash 1.5
defendant ethnicity
Ethnic Minority
Han
-7.301
0.0
Gemini Flash 1.5
defendant education
Below High School
High School or Above
-0.966
0.094
Gemini Flash 1.5
defendant occupation
Farmer
Worker
-1.208
0.047
Gemini Flash 1.5
defendant nationality
Foreigner
Chinese
1.335
0.006
Gemini Flash 1.5
defendant political background
CCP
Mass
1.481
0.015
Gemini Flash 1.5
defendant wealth
Penniless
A Million Saving
-2.833
0.0
Gemini Flash 1.5
defendant sexual orientation
Homosexua
Heterosexual
0.843
0.018
Gemini Flash 1.5
victim gender
Gender Non-Binary
Male
1.159
0.01
Gemini Flash 1.5
victim ethnicity
Ethnic Minority
Han
0.961
0.007
Gemini Flash 1.5
victim household registration
Not Local
Local
-0.619
0.087
Gemini Flash 1.5
victim nationality
Foreigner
Chinese
1.209
0.006
Gemini Flash 1.5
victim political background
CCP
Mass
0.703
0.09
Gemini Flash 1.5
defender ethnicity
Ethnic Minority
Han
-0.805
0.048
Gemini Flash 1.5
defender education
Below High School
High School or Above
1.055
0.007
Gemini Flash 1.5
defender occupation
Farmer
Worker
0.958
0.018
Gemini Flash 1.5
defender religion
Islamic
Atheism
-1.024
0.007
Table A39: List of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy analysis (II).
66

--- Page 67 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Impact
on
Sentence
Prediction
(Months)
P-Value
Gemini Flash 1.5
defender religion
Buddhism
Atheism
-1.517
0.0
Gemini Flash 1.5
defender religion
Christianity
Atheism
-1.414
0.0
Gemini Flash 1.5
defender wealth
Penniless
A Million Saving
1.49
0.005
Gemini Flash 1.5
prosecurate gender
Gender Non-Binary
Male
0.713
0.017
Gemini Flash 1.5
prosecurate household registration
Not Local
Local
-0.777
0.094
Gemini Flash 1.5
prosecurate sexual orientation
Homosexual
Heterosexual
-1.056
0.087
Gemini Flash 1.5
prosecurate wealth
Penniless
A Million Saving
1.305
0.048
Gemini Flash 1.5
judge age
Age
Age
4.01
0.002
Gemini Flash 1.5
judge gender
Gender Non-Binary
Male
1.53
0.027
Gemini Flash 1.5
judge ethnicity
Ethnic Minority
Han
3.231
0.0
Gemini Flash 1.5
judge household registration
Not Local
Local
-2.275
0.002
Gemini Flash 1.5
judge sexual orientation
Homosexual
Heterosexual
-3.034
0.0
Gemini Flash 1.5
judge religion
Buddhism
Atheism
-3.284
0.0
Gemini Flash 1.5
judge political background
CCP
Mass
2.671
0.0
Gemini Flash 1.5
judge wealth
Penniless
A Million Saving
6.377
0.0
Gemini Flash 1.5
collegial panel
Collegial Panel
Single
0.879
0.016
Gemini Flash 1.5
court level
Intermediate Court
Primary Court
0.648
0.06
Gemini Flash 1.5
court level
High Court
Primary Court
1.128
0.004
Gemini Flash 1.5
court location
Court Rural
Court Urban
-1.537
0.006
Gemini Flash 1.5
trial duration
Prolonged Litigation
Short Litigation
0.68
0.099
Gemini Flash 1.5
recusal applied
Recusal Applied
Recusal Applied
-1.699
0.0
Gemini Flash 1.5 8B
defendant gender
Female
Male
1.888
0.012
Gemini Flash 1.5 8B
defendant ethnicity
Ethnic Minority
Han
-2.535
0.003
Gemini Flash 1.5 8B
defendant occupation
Farmer
Worker
-1.16
0.075
Gemini Flash 1.5 8B
defendant nationality
Foreigner
Chinese
1.509
0.02
Gemini Flash 1.5 8B
defendant political background
CCP
Mass
0.986
0.097
Gemini Flash 1.5 8B
defendant political background
Other Party
Mass
0.92
0.095
Gemini Flash 1.5 8B
defendant wealth
Penniless
A Million Saving
-1.987
0.002
Gemini Flash 1.5 8B
victim sexual orientation
Homosexual
Heterosexual
1.078
0.05
Gemini Flash 1.5 8B
victim sexual orientation
Bisexual
Heterosexual
1.281
0.007
Gemini Flash 1.5 8B
victim age
Age
Age
2.272
0.04
Gemini Flash 1.5 8B
victim ethnicity
Ethnic Minority
Han
1.761
0.006
Gemini Flash 1.5 8B
victim nationality
Foreigner
Chinese
1.306
0.032
Gemini Flash 1.5 8B
victim political background
CCP
Mass
1.202
0.029
Gemini Flash 1.5 8B
victim political background
Other Party
Mass
1.132
0.015
Gemini Flash 1.5 8B
defender age
Age
Age
2.296
0.012
Gemini Flash 1.5 8B
defender ethnicity
Ethnic Minority
Han
1.228
0.02
Gemini Flash 1.5 8B
defender nationality
Foreigner
Chinese
0.854
0.092
Gemini Flash 1.5 8B
defender political background
CCP
Mass
1.119
0.049
Gemini Flash 1.5 8B
defender political background
Other Party
Mass
0.933
0.066
Gemini Flash 1.5 8B
defender religion
Christianity
Atheism
-0.801
0.082
Gemini Flash 1.5 8B
defender wealth
Penniless
A Million Saving
-1.293
0.019
Gemini Flash 1.5 8B
prosecurate age
Age
Age
3.175
0.003
Gemini Flash 1.5 8B
prosecurate sexual orientation
Homosexual
Heterosexual
1.145
0.052
Gemini Flash 1.5 8B
judge age
Age
Age
2.475
0.032
Gemini Flash 1.5 8B
judge ethnicity
Ethnic Minority
Han
3.234
0.0
Gemini Flash 1.5 8B
judge household registration
Not Local
Local
1.79
0.006
Gemini Flash 1.5 8B
judge sexual orientation
Bisexual
Heterosexual
2.223
0.0
Gemini Flash 1.5 8B
judge religion
Islamic
Atheism
-1.566
0.006
Gemini Flash 1.5 8B
judge religion
Buddhism
Atheism
-3.389
0.0
Gemini Flash 1.5 8B
judge wealth
Penniless
A Million Saving
2.384
0.001
Gemini Flash 1.5 8B
open trial
Open Trial
Not Open Trial
0.999
0.05
Gemini Flash 1.5 8B
court level
Intermediate Court
Primary Court
1.41
0.008
Gemini Flash 1.5 8B
court level
High Court
Primary Court
1.722
0.006
Gemini Flash 1.5 8B
court location
Court Rural
Court Urban
0.852
0.079
Gemini Flash 1.5 8B
compulsory measure
Compulsory Measure
No Compulsory Measure
2.778
0.0
Gemini Flash 1.5 8B
trial duration
Prolonged Litigation
Short Litigation
1.178
0.049
Gemini Flash 1.5 8B
recusal applied
Recusal Applied
Recusal Applied
1.245
0.051
LFM 40B MoE
defendant sexual orientation
Homosexua
Heterosexual
4.959
0.023
LFM 40B MoE
victim nationality
Foreigner
Chinese
3.983
0.07
LFM 40B MoE
victim political background
CCP
Mass
4.125
0.051
LFM 40B MoE
defender ethnicity
Ethnic Minority
Han
4.263
0.056
LFM 40B MoE
defender household registration
Not Local
Local
3.757
0.099
LFM 40B MoE
defender political background
CCP
Mass
4.829
0.024
LFM 40B MoE
prosecurate gender
Gender Non-Binary
Male
4.401
0.056
LFM 40B MoE
prosecurate sexual orientation
Bisexual
Heterosexual
-5.495
0.016
LFM 40B MoE
prosecurate religion
Buddhism
Atheism
-3.914
0.063
LFM 40B MoE
prosecurate wealth
Penniless
A Million Saving
3.877
0.088
LFM 40B MoE
judge wealth
Penniless
A Million Saving
5.105
0.026
LFM 40B MoE
defender type
Appointed
Privately Attained
-5.075
0.021
LFM 40B MoE
open trial
Open Trial
Not Open Trial
5.121
0.025
LFM 40B MoE
court level
High Court
Primary Court
7.202
0.002
LFM 40B MoE
compulsory measure
Compulsory Measure
No Compulsory Measure
4.346
0.049
Table A40: List of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy analysis (III).
67

--- Page 68 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Impact
on
Sentence
Prediction
(Months)
P-Value
Nova Lite 1.0
defendant ethnicity
Ethnic Minority
Han
-3.246
0.001
Nova Lite 1.0
defendant age
Age
Age
1.771
0.075
Nova Lite 1.0
defendant occupation
Unemployed
Worker
-1.04
0.093
Nova Lite 1.0
defendant political background
CCP
Mass
2.387
0.0
Nova Lite 1.0
defendant wealth
Penniless
A Million Saving
-2.59
0.0
Nova Lite 1.0
defendant sexual orientation
Bisexual
Heterosexual
-1.819
0.001
Nova Lite 1.0
victim religion
Islam
Atheism
1.165
0.043
Nova Lite 1.0
victim ethnicity
Ethnic Minority
Han
1.296
0.015
Nova Lite 1.0
crime date
Summer
Spring
0.881
0.097
Nova Lite 1.0
crime date
Winter
Spring
1.455
0.004
Nova Lite 1.0
defender household registration
Not Local
Local
1.061
0.046
Nova Lite 1.0
prosecurate age
Age
Age
2.4
0.022
Nova Lite 1.0
prosecurate political background
CCP
Mass
0.88
0.06
Nova Lite 1.0
judge age
Age
Age
-2.013
0.092
Nova Lite 1.0
judge gender
Gender Non-Binary
Male
2.149
0.002
Nova Lite 1.0
judge ethnicity
Ethnic Minority
Han
2.226
0.0
Nova Lite 1.0
judge household registration
Not Local
Local
-1.346
0.036
Nova Lite 1.0
judge religion
Buddhism
Atheism
2.474
0.0
Nova Lite 1.0
judge religion
Christianity
Atheism
1.418
0.021
Nova Lite 1.0
judge political background
CCP
Mass
2.51
0.001
Nova Lite 1.0
collegial panel
Collegial Panel
Single
1.384
0.019
Nova Lite 1.0
assessor
No Preple’s Assessor
With People’s Assessor
1.264
0.019
Nova Lite 1.0
pretrial conference
With Pretrial Conference
No Pretrial Conference
-0.883
0.099
Nova Lite 1.0
court level
Intermediate Court
Primary Court
1.366
0.006
Nova Lite 1.0
court level
High Court
Primary Court
1.661
0.002
Nova Micro 1.0
defendant ethnicity
Ethnic Minority
Han
2.228
0.084
Nova Micro 1.0
defendant occupation
Unemployed
Worker
-2.331
0.044
Nova Micro 1.0
defendant nationality
Foreigner
Chinese
-2.236
0.041
Nova Micro 1.0
defendant wealth
Penniless
A Million Saving
-3.819
0.0
Nova Micro 1.0
victim religion
Buddhism
Atheism
2.69
0.009
Nova Micro 1.0
victim occupation
Unemployed
Worker
1.569
0.079
Nova Micro 1.0
victim nationality
Foreigner
Chinese
-1.966
0.045
Nova Micro 1.0
defender gender
Gender Non-Binary
Male
-2.773
0.004
Nova Micro 1.0
defender political background
Other Party
Mass
-1.577
0.08
Nova Micro 1.0
prosecurate household registration
Not Local
Local
1.578
0.069
Nova Micro 1.0
judge age
Age
Age
4.635
0.063
Nova Micro 1.0
judge gender
Gender Non-Binary
Male
-11.831
0.0
Nova Micro 1.0
judge household registration
Not Local
Local
3.299
0.008
Nova Micro 1.0
judge sexual orientation
Homosexual
Heterosexual
6.69
0.0
Nova Micro 1.0
judge religion
Islamic
Atheism
-7.694
0.0
Nova Micro 1.0
judge religion
Christianity
Atheism
3.742
0.004
Nova Micro 1.0
judge political background
CCP
Mass
-3.98
0.001
Nova Micro 1.0
judge political background
Other Party
Mass
-10.281
0.0
Nova Micro 1.0
judge wealth
Penniless
A Million Saving
-4.19
0.001
Nova Micro 1.0
collegial panel
Collegial Panel
Single
1.601
0.084
Nova Micro 1.0
pretrial conference
With Pretrial Conference
No Pretrial Conference
-1.672
0.065
Nova Micro 1.0
judicial committee
With Judicial Committee
No Judicial Committee
2.501
0.005
Nova Micro 1.0
online broadcast
Online Broadcast
No Online Broadcast
2.914
0.001
Nova Micro 1.0
compulsory measure
Compulsory Measure
No Compulsory Measure
2.306
0.054
Nova Micro 1.0
recusal applied
Recusal Applied
Recusal Applied
1.906
0.093
Llama 3.1 8B Instruct
defendant nationality
Foreigner
Chinese
1.68
0.094
Llama 3.1 8B Instruct
defendant sexual orientation
Homosexua
Heterosexual
2.305
0.03
Llama 3.1 8B Instruct
defendant sexual orientation
Bisexual
Heterosexual
3.133
0.001
Llama 3.1 8B Instruct
victim sexual orientation
Bisexual
Heterosexual
1.978
0.065
Llama 3.1 8B Instruct
victim education
Below High School
High School or Above
-3.196
0.003
Llama 3.1 8B Instruct
victim occupation
Farmer
Worker
1.774
0.071
Llama 3.1 8B Instruct
victim political background
CCP
Mass
2.256
0.011
Llama 3.1 8B Instruct
defender gender
Gender Non-Binary
Male
-4.181
0.021
Llama 3.1 8B Instruct
defender education
Below High School
High School or Above
-2.543
0.078
Llama 3.1 8B Instruct
defender occupation
Farmer
Worker
4.387
0.003
Llama 3.1 8B Instruct
defender nationality
Foreigner
Chinese
2.927
0.059
Llama 3.1 8B Instruct
defender religion
Islamic
Atheism
2.909
0.002
Llama 3.1 8B Instruct
defender religion
Buddhism
Atheism
2.752
0.002
Llama 3.1 8B Instruct
defender religion
Christianity
Atheism
4.162
0.0
Llama 3.1 8B Instruct
defender wealth
Penniless
A Million Saving
-7.235
0.0
Llama 3.1 8B Instruct
prosecurate gender
Gender Non-Binary
Male
-1.868
0.073
Llama 3.1 8B Instruct
prosecurate age
Age
Age
9.225
0.003
Llama 3.1 8B Instruct
prosecurate household registration
Not Local
Local
3.46
0.007
Llama 3.1 8B Instruct
prosecurate religion
Islamic
Atheism
3.116
0.073
Llama 3.1 8B Instruct
prosecurate religion
Buddhism
Atheism
3.275
0.052
Llama 3.1 8B Instruct
prosecurate religion
Christianity
Atheism
3.653
0.018
Table A41: List of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy analysis (IV).
68

--- Page 69 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Impact
on
Sentence
Prediction
(Months)
P-Value
Llama 3.1 8B Instruct
prosecurate wealth
Penniless
A Million Saving
-4.117
0.045
Llama 3.1 8B Instruct
judge gender
Female
Male
-2.063
0.031
Llama 3.1 8B Instruct
judge religion
Islamic
Atheism
-2.104
0.07
Llama 3.1 8B Instruct
assessor
No preple’s assessor
Has people’s assessor
-1.909
0.086
Llama 3.1 8B Instruct
pretrial conference
Has Pretrial Conference
No Pretrial Conference
3.193
0.008
Phi 4
defendant gender
Female
Male
-1.282
0.006
Phi 4
defendant household registration
Not Local
Local
1.004
0.022
Phi 4
defendant nationality
Foreigner
Chinese
1.314
0.016
Phi 4
defendant political background
CCP
Mass
0.994
0.092
Phi 4
defendant wealth
Penniless
A Million Saving
-2.319
0.006
Phi 4
defendant sexual orientation
Homosexua
Heterosexual
1.24
0.033
Phi 4
victim sexual orientation
Homosexual
Heterosexual
1.128
0.074
Phi 4
victim age
Age
Age
2.05
0.021
Phi 4
victim nationality
Foreigner
Chinese
1.493
0.011
Phi 4
victim wealth
Penniless
A Million Saving
-2.703
0.001
Phi 4
crime location
Rural
Urban
1.2
0.077
Phi 4
crime date
Summer
Spring
1.056
0.057
Phi 4
crime date
Winter
Spring
1.25
0.013
Phi 4
defender education
Below High School
High School or Above
1.097
0.014
Phi 4
defender occupation
Farmer
Worker
1.516
0.012
Phi 4
defender nationality
Foreigner
Chinese
1.324
0.056
Phi 4
prosecurate wealth
Penniless
A Million Saving
-1.681
0.044
Phi 4
judge age
Age
Age
3.303
0.0
Phi 4
judge gender
Female
Male
-1.049
0.077
Phi 4
judge gender
Gender Non-Binary
Male
-1.399
0.069
Phi 4
judge religion
Buddhism
Atheism
1.279
0.032
Phi 4
judge religion
Christianity
Atheism
-1.017
0.04
Phi 4
judge wealth
Penniless
A Million Saving
4.258
0.0
Phi 4
defender type
Appointed
Privately Attained
1.371
0.038
Phi 4
online broadcast
Online Broadcast
No Online Broadcast
-1.083
0.061
Phi 4
court level
Intermediate Court
Primary Court
1.26
0.013
Phi 4
court level
High Court
Primary Court
2.844
0.0
Phi 4
trial duration
Prolonged Litigation
Short Litigation
1.644
0.01
Phi 4
recusal applied
Recusal Applied
Recusal Applied
2.424
0.003
LFM 7B
defendant ethnicity
Ethnic Minority
Han
2.18
0.054
LFM 7B
defendant household registration
Not Local
Local
-2.104
0.028
LFM 7B
defendant political background
CCP
Mass
-4.883
0.0
LFM 7B
defendant political background
Other Party
Mass
-2.811
0.005
LFM 7B
defendant wealth
Penniless
A Million Saving
5.775
0.0
LFM 7B
defendant religion
Islam
Atheism
-1.989
0.058
LFM 7B
defendant religion
Buddhism
Atheism
-1.654
0.095
LFM 7B
victim religion
Buddhism
Atheism
-2.93
0.004
LFM 7B
victim sexual orientation
Homosexual
Heterosexual
2.569
0.036
LFM 7B
victim sexual orientation
Bisexual
Heterosexual
2.411
0.07
LFM 7B
victim age
Age
Age
-2.738
0.045
LFM 7B
victim occupation
Unemployed
Worker
2.466
0.01
LFM 7B
victim nationality
Foreigner
Chinese
2.595
0.02
LFM 7B
victim wealth
Penniless
A Million Saving
2.853
0.036
LFM 7B
defender gender
Gender Non-Binary
Male
-6.223
0.001
LFM 7B
defender occupation
Unemployed
Worker
-2.597
0.047
LFM 7B
defender religion
Islamic
Atheism
5.368
0.001
LFM 7B
defender religion
Buddhism
Atheism
2.747
0.094
LFM 7B
defender religion
Christianity
Atheism
3.017
0.061
LFM 7B
prosecurate gender
Gender Non-Binary
Male
-2.164
0.081
LFM 7B
prosecurate gender
Female
Male
-5.214
0.007
LFM 7B
prosecurate ethnicity
Ethnic Minority
Han
-3.876
0.005
LFM 7B
prosecurate sexual orientation
Bisexual
Heterosexual
-4.234
0.034
LFM 7B
prosecurate wealth
Penniless
A Million Saving
2.694
0.057
LFM 7B
judge age
Age
Age
-5.917
0.021
LFM 7B
judge household registration
Not Local
Local
1.788
0.078
LFM 7B
judge religion
Buddhism
Atheism
3.151
0.004
LFM 7B
judge political background
Other Party
Mass
-2.983
0.004
LFM 7B
judge wealth
Penniless
A Million Saving
-17.72
0.0
LFM 7B
pretrial conference
With Pretrial Conference
No Pretrial Conference
-1.819
0.092
LFM 7B
court location
Court Rural
Court Urban
-3.166
0.003
Table A42: List of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy Analysis (V).
69

--- Page 70 ---

Working Paper
Model Name
Label Name
Label Value
Reference
Impact
on
Sentence
Prediction
(Months)
P-Value
Mistral Small 3
defendant household registration
Not Local
Local
-0.021
0.058
Mistral Small 3
defendant wealth
Penniless
A Million Saving
-0.047
0.001
Mistral Small 3
victim gender
Gender Non-Binary
Male
-0.022
0.056
Mistral Small 3
victim ethnicity
Ethnic Minority
Han
0.038
0.002
Mistral Small 3
victim wealth
Penniless
A Million Saving
-0.031
0.005
Mistral Small 3
defender religion
Islamic
Atheism
0.03
0.03
Mistral Small 3
prosecurate age
Age
Age
0.032
0.071
Mistral Small 3
prosecurate religion
Christianity
Atheism
0.02
0.07
Mistral Small 3
prosecurate wealth
Penniless
A Million Saving
-0.027
0.069
Mistral Small 3
judge age
Age
Age
0.124
0.0
Mistral Small 3
judge gender
Gender Non-Binary
Male
-0.07
0.0
Mistral Small 3
judge ethnicity
Ethnic Minority
Han
0.034
0.003
Mistral Small 3
judge household registration
Not Local
Local
-0.023
0.032
Mistral Small 3
judge sexual orientation
Homosexual
Heterosexual
0.027
0.06
Mistral Small 3
judge sexual orientation
Bisexual
Heterosexual
0.03
0.017
Mistral Small 3
judge religion
Islamic
Atheism
0.089
0.0
Mistral Small 3
judge religion
Buddhism
Atheism
0.059
0.0
Mistral Small 3
judge religion
Christianity
Atheism
0.05
0.0
Mistral Small 3
judge political background
CCP
Mass
0.1
0.0
Mistral Small 3
judge political background
Other Party
Mass
0.054
0.0
Mistral Small 3
court level
High Court
Primary Court
0.016
0.066
Mistral Small 3
compulsory measure
Compulsory Measure
No Compulsory Measure
0.021
0.1
Mistral Small 3
trial duration
Prolonged Litigation
Short Litigation
0.02
Mistral NeMo
defendant gender
Female
Male
5.233
0.0
Mistral NeMo
defendant ethnicity
Ethnic Minority
Han
-6.208
0.0
Mistral NeMo
defendant wealth
Penniless
A Million Saving
-2.862
0.001
Mistral NeMo
defendant sexual orientation
Homosexua
Heterosexual
0.896
0.08
Mistral NeMo
defendant sexual orientation
Bisexual
Heterosexual
1.028
0.049
Mistral NeMo
victim occupation
Farmer
Worker
-1.226
0.038
Mistral NeMo
victim occupation
Unemployed
Worker
-1.059
0.043
Mistral NeMo
victim wealth
Penniless
A Million Saving
-1.715
0.01
Mistral NeMo
crime date
Summer
Spring
-0.651
0.063
Mistral NeMo
crime time
Afternoon
Morning
-1.353
0.001
Mistral NeMo
defender gender
Female
Male
0.843
0.038
Mistral NeMo
defender political background
CCP
Mass
0.689
0.092
Mistral NeMo
defender sexual orientation
Homosexual
Heterosexual
-0.893
0.05
Mistral NeMo
prosecurate wealth
Penniless
A Million Saving
1.334
0.047
Mistral NeMo
judge gender
Gender Non-Binary
Male
-1.598
0.023
Mistral NeMo
judge sexual orientation
Bisexual
Heterosexual
1.343
0.043
Mistral NeMo
judge political background
CCP
Mass
0.965
0.071
Mistral NeMo
judge wealth
Penniless
A Million Saving
2.015
0.005
Mistral NeMo
collegial panel
Collegial Panel
Single
1.02
0.069
Mistral NeMo
open trial
Open Trial
Not Open Trial
1.624
0.001
Mistral NeMo
court level
Intermediate Court
Primary Court
2.145
0.0
Mistral NeMo
court level
High Court
Primary Court
2.848
0.0
Mistral NeMo
compulsory measure
Compulsory Measure
No Compulsory Measure
4.061
0.0
DeepSeek R1 32B
defendant gender
Female
Male
4.323
0.0
DeepSeek R1 32B
defendant ethnicity
Ethnic Minority
Han
-7.208
0.0
DeepSeek R1 32B
defendant education
Below High School
High School or Above
2.18
0.042
DeepSeek R1 32B
defendant political background
CCP
Mass
2.921
0.008
DeepSeek R1 32B
victim gender
Female
Male
2.111
0.087
DeepSeek R1 32B
defender age
Age
Age
4.054
0.039
DeepSeek R1 32B
judge sexual orientation
Homosexual
Heterosexual
-2.067
0.04
DeepSeek R1 32B
judicial committee
With Judicial Committee
No Judicial Committee
1.962
0.075
DeepSeek R1 32B
court level
High Court
Primary Court
3.806
0.001
Table A43: List of labels with statistically significant results (p −value < 0.1) in imbalanced
inaccuracy analysis (VI).
70

--- Page 71 ---

Working Paper
G
CORRELATION ANALYSIS
G.1
CORRELATIONS AMONG EVALUATION METRICS
Figure A8 consists of four scatter plots that illustrate the relationships among key evaluation metrics
of LLMs when the temperature is set to 0. Each scatter plot includes a regression line (in red) to
indicate the trend, as well as an annotation of the p-value representing the statistical significance of
the correlation. The p-value annotated in each panel quantifies the probability of observing such a
correlation by random chance. A p-value lower than 0.1 or 0.05 indicates statistical significance,
suggesting that the observed correlation is unlikely to be due to random variation. For simplicity,
we only use the results from models with a temperature of 0.
Top-left panel (Inconsistency vs. Bias Number): The x-axis represents the Bias Number, which
quantifies the total number of label values exhibiting significant bias. The y-axis represents Incon-
sistency, which measures the variability of model outputs when only the label value changes. The
plot shows a negative correlation (p-value = 0.013), suggesting that as the number of biased labels
increases, the model’s inconsistency decreases.
Top-right panel (Unfair Inaccuracy Number vs. Bias Number): The x-axis represents the Bias
Number, and the y-axis represents the Unfair Inaccuracy Number. A positive correlation (p-value =
0.018) is observed, suggesting that models with more biases are also more likely to exhibit unfair
prediction inaccuracies across certain label groups.
Figure A8: Correlations among evaluation metrics. The temperature is set to 0.
Bottom-left panel (Weighted Average MAE vs. Bias Number): The x-axis represents the Bias
Number, while the y-axis represents the Weighted Average Mean Absolute Error (MAE). There
is a clear negative correlation (p-value = 0.004), indicating that models with more biases tend to
have lower overall prediction errors, as measured by MAE. This could imply that biased models
are potentially more accurate in their predictions, though not necessarily more fair. This “accuracy-
equity trade-off” is in line with the finding in prior studies (Desiere & Struyven, 2021).
Bottom-right panel (Weighted Average MAPE vs. Bias Number): This figure is similar to the
Bottom-left panel. Y-axis here represents the Weighted Average Mean Absolute Percentage Error
71

--- Page 72 ---

Working Paper
(MAPE). A strong negative correlation (p-value = 0.006) is also detected, corroborating the results
in the Bottom-left panel.
Figure A9: Correlations between model temperature and fairness metrics.
G.2
CORRELATIONS BETWEEN TEMPERATURE AND EVALUATION METRICS
Figure A9 contains three scatter plots that illustrate the relationship between model temperature (0
vs. 1) and key fairness-related metrics: inconsistency, bias number, and unfair inaccuracy number.
There are 12 data points in each panel, corresponding to the 12 models that were evaluated under
both temperature settings. The corresponding p-value for each regression is annotated within the
panel to indicate statistical significance.
Top-left panel (Inconsistency vs. Temperature): It shows that increasing temperature significantly
increases model inconsistency (p < 0.001), reflecting greater variability in predictions when only a
single label value is changed.
Top-right panel (Bias Number vs. Temperature): It reveals a significant negative correlation be-
tween temperature and the number of biased labels (p < 0.001), suggesting that higher temperature
reduces the number of statistically significant biases.
Bottom-left panel (Unfair Inaccuracy Number vs. Temperature): It shows that higher tem-
perature is associated with fewer instances of unfair inaccuracy, i.e., unbalanced prediction error
across label groups (p < 0.001). These results confirm that although a higher temperature amplifies
inconsistency, it concurrently attenuates measurable bias and unfairness in model outputs.
G.3
CORRELATIONS BETWEEN MODEL RELEASE DATE AND EVALUATION METRICS
Figure A10 presents the correlation between model release timing and fairness metrics across three
dimensions: consistency, bias, and imbalanced inaccuracy. All results are based on evaluations
conducted at temperature 0 for comparability.
Top-left panel (Days from Release vs. Inconsistency): The x-axis denotes the number of days
since model release, using January 31, 2025, as the cutoff. The y-axis represents each model’s aver-
72

--- Page 73 ---

Working Paper
age inconsistency rate across all labels. While a downward trend is visually observable—suggesting
newer models may exhibit slightly lower inconsistency—the correlation is not statistically signifi-
cant (p = 0.239). This indicates weak and inconclusive evidence that newer models are more stable
in their predictions.
Top-right panel (Days from Release vs. Bias Number): This panel uses the same x-axis, with the
y-axis indicating the number of labels showing statistically significant bias. The p-value of 0.659
shows no meaningful correlation between release date and bias. This suggests that recent models do
not consistently perform better in terms of reducing systemic bias.
Bottom-left panel (Days from Release vs. Imbalanced Inaccuracy): Here, the y-axis displays the
number of labels where the model produces significantly different prediction errors across groups.
The correlation is again statistically insignificant. In sum, model release date does not strongly
predict performance in any of the three fairness dimensions.
G.4
CORRELATIONS BETWEEN MODEL SIZE AND EVALUATION METRICS
Figure A10: Correlations among days since release and fairness metrics. The temperature is set to
0.
Figure A11 analyzes the relationship between model parameter size (in log scale) and each of the
three fairness metrics.
Top-left panel (Parameter Size vs. Inconsistency): The x-axis represents parameter size in log
scale, and the y-axis shows the inconsistency rate. A significant positive trend (p = 0.084) is
observed, suggesting that larger models tend to produce more inconsistent predictions. However,
the p-value is not lower than 0.5, indicating suggestive but inconclusive evidence. Future research
could examine this issue more deeply and comprehensively.
Top-right panel (Parameter Size vs. Bias Number): The y-axis here is the number of signifi-
cantly biased labels. Again, the lack of statistical significance indicates that larger models are not
consistently better (or worse) at mitigating bias.
73

--- Page 74 ---

Working Paper
Bottom-left panel (Parameter Size vs. Imbalanced Inaccuracy): For imbalanced inaccuracy,
the pattern remains similar. Across all three metrics, model size does not appear to be a reliable
predictor of fairness performance.
G.5
CORRELATIONS BETWEEN A MODEL’S COUNTRY OF ORIGIN AND EVALUATION
METRICS
Figure A12 investigates whether the country in which a model was developed has any association
with its fairness characteristics.
Top-left panel (Developer Country vs. Inconsistency): The inconsistency rate shows no signifi-
cant difference across models developed in different countries.
Top-right panel (Developer Country vs. Bias Number): Similarly, the number of biased labels is
not meaningfully associated with the developer’s national origin.
Bottom-left panel (Developer Country vs. Imbalanced Inaccuracy): No significant pattern is
observed for imbalanced inaccuracy either. Taken together, these findings suggest that fairness per-
formance does not systematically differ by model origin, at least within the scope of models included
in our analysis.
Figure A11: Correlations between model parameter size and fairness metrics. The temperature is
set to 0.
74

--- Page 75 ---

Working Paper
Figure A12: Correlations between country of origin and fairness metrics. The temperature is set to
0.
75

```
