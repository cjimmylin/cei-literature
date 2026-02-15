---
title: "2025-Zhang-Safety Evaluation and Enhancement of DeepSeek Models in Chinese - PDF Extract"
source_pdf: "2025-Zhang-Safety Evaluation and Enhancement of DeepSeek Models in Chinese.pdf"
pages: 21
extracted_at: "2026-02-15T17:54:29.292562"
---

# PDF Extract: 2025-Zhang-Safety Evaluation and Enhancement of DeepSeek Models in Chinese

**Source PDF:** 2025-Zhang-Safety Evaluation and Enhancement of DeepSeek Models in Chinese.pdf
**Total Pages:** 21

---

## Content

```
--- Page 1 ---

Safety Evaluation and Enhancement of DeepSeek
Models in Chinese Contexts
Wenjing Zhang1,2, Xuejiao Lei1,2, Zhaoxiang Liu∗1,2, Limin Han1,2, Jiaojiao
Zhao1,2, Junting Guo1,2, Zhenhong Long1,2, Shu Yang1,2, Meijuan An1,2, Beibei
Huang1,2, Rongjia Du1,2, Ning Wang1,2, Kai Wang1,2, and Shiguo Lian∗1,2
1 Unicom Data Intelligence, China Unicom
2 Data Science & Artificial Intelligence Research Institute, China Unicom
{zhangwj1503,leixj15,liuzx178,hanlm21,zhaojj225,guojt26,longzh8,yangs213,
anmj5,huangbb15,durj11,wangn85,wangk115,liansg}@chinaunicom.cn
∗Corresponding author(s)
Abstract. DeepSeek-R1, renowned for its exceptional reasoning capa-
bilities and open-source strategy, is significantly influencing the global
artificial intelligence landscape. However, it exhibits notable safety short-
comings. Recent research conducted by Robust Intelligence, a subsidiary
of Cisco, in collaboration with the University of Pennsylvania, revealed
that DeepSeek-R1 achieves a 100% attack success rate when processing
harmful prompts. Furthermore, multiple security firms and research insti-
tutions have identified critical security vulnerabilities within the model.
Although China Unicom has uncovered safety vulnerabilities of R1 in
Chinese contexts, the safety capabilities of the remaining distilled mod-
els in the R1 series have not yet been comprehensively evaluated. To
address this gap, this study utilizes the comprehensive Chinese safety
benchmark CHiSafetyBench to conduct an in-depth safety evaluation
of the DeepSeek-R1 series distilled models. The objective is to assess
the safety capabilities of these models in Chinese contexts both be-
fore and after distillation, and to further elucidate the adverse effects
of distillation on model safety. Building on these findings, we implement
targeted safety enhancements for the entire DeepSeek-R1 model series.
Evaluation results indicate that the enhanced models achieve significant
improvements in safety while maintaining reasoning capabilities with-
out notable degradation. We open-source the safety-enhanced models at
https://github.com/UnicomAI/DeepSeek-R1-Safe to serve as a valu-
able resource for future research and optimization of DeepSeek models.
1
Introduction
Large language models have demonstrated exceptional performance in complex
reasoning[9,11], natural language understanding[12], and generation[1,2], becom-
ing a core driving force in the development of artificial intelligence technologies.
Against this backdrop, DeepSeek has rapidly emerged as an industry leader,
thanks to its swift development over the past two years. Recently, DeepSeek
arXiv:2503.16529v2  [cs.CL]  16 May 2025

--- Page 2 ---

2
W. Zhang et al.
released its R1 series of models, which includes the 671B-parameter DeepSeek-
R1 and six dense models distilled from DeepSeek-R1 based on the Qwen and
Llama architectures (1.5B, 7B, 8B, 14B, 32B, and 70B)[4]. DeepSeek-R1 has
shown remarkable performance in tasks such as mathematics, coding, and logical
reasoning, surpassing OpenAI-o1[8] in several performance metrics. Meanwhile,
its distilled models have also demonstrated outstanding capabilities in reason-
ing ability, computational efficiency, and adaptability, achieving an optimized
balance between performance and cost. This has provided a significant break-
through for the practical application of high-performance AI models. For exam-
ple, DeepSeek-R1-Distill-Qwen-32B has performance comparable to the larger-
parameter DeepSeek-R1-Distill-Llama-70B and outperforms o1-mini in mathe-
matics and coding tasks, fully showcasing the strong comprehensive capabilities
of this series of models.
With the wide application of DeepSeek models, their safety performance has
attracted significant attention from the industry. Recently, a joint study by Ro-
bust Intelligence, a subsidiary of Cisco[3], and the University of Pennsylvania
pointed out that DeepSeek R1 has critical safety vulnerabilities. The research
team conducted safety tests on R1 using 50 harmful prompts from the Harm-
Bench dataset[7], and the results showed a 100% attack success rate. Addition-
ally, Zhang et al.[14] has also confirmed that DeepSeek-R1 and DeepSeek-V3
have deficiencies in safety capabilities in the Chinese contexts. However, system-
atic testing of the Chinese safety performance of the distilled models in the R1
series has not yet been conducted, and their security protection effects in the
Chinese environment still need further verification.
Based on the comprehensive safety benchmark CHiSafetyBench[13], this study
systematically validates the safety of the DeepSeek series of distilled models in
the Chinese context, achieving a more comprehensive evaluation of the safety
capabilities of the latest full series of DeepSeek models. Experimental results
reveal that these distilled models still exhibit several potential safety issues. To
address these concerns, targeted safety enhancements are implemented for the
entire DeepSeek-R1 model series. Evaluation results demonstrate that the safety-
enhanced models achieve a 10.72% improvement in overall accuracy on the risk
content identification task of CHiSafetyBench compared to the non-enhanced
models. On the refusal to answer task of CHiSafetyBench, the rejection rate and
responsibility rate increase by 18.39% and 14.72%, respectively, while the harm
rate decreases by 1.45%, marking a comprehensive enhancement in safety capa-
bilities. Furthermore, the safety-enhanced models show no significant decline in
reasoning performance.
To our knowledge, we are the first research team to successfully complete
the safety evaluation and enhancement of entire DeepSeek-R1 model series in
the Chinese contexts. Moreover, we have open-sourced all these safety-enhanced
models to provide a benchmark for researchers and developers both within and
outside the industry to study and utilize collaboratively.

--- Page 3 ---

Safety Evaluation and Enhancement
3
2
Methodology
This paper first conducts a comprehensive safety evaluation of the remaining
six distilled models in the DeepSeek-R1 series within Chinese contexts. Sub-
sequently, to address the identified safety deficiencies revealed by the testing,
we implement supervised fine-tuning to perform targeted enhancement across
the entire DeepSeek-R1 model series. Compared with pre-training approaches,
supervised fine-tuning enables rapid alignment of large language models while
demonstrating significant advantages in reducing both computational time and
resource expenditure.
2.1
Safety Evaluation
We first conduct a comprehensive safety evaluation of the six distilled models in
Chinese contexts. The evaluation process is designed from multiple dimensions,
with the aim of comprehensively identifying and rejecting any unsafe content
while ensuring that the models could positively guide the generation of infor-
mation in line with ethical values.These evaluation dimensions include, but are
not limited to, discrimination, violation of values, and infringement of rights.
Through this comprehensive evaluation process, we strive to achieve a thorough
and accurate assessment of the model from a safety perspective.
2.2
Safety Enhancement
This study independently constructs a fine-tuning dataset comprising around
50K samples, specifically designed to improve the safety performance of the
models. The dataset consists of two parts: instructions addressing critical areas
such as discrimination and infringement, and chain-of-thought reasoning sam-
ples. The inclusion of safety data aims to significantly expand the scope and
depth of safety testing, thereby covering potential safety risk scenarios more
comprehensively. However, relying solely on safety data for fine-tuning may po-
tentially have a negative impact on the models’ reasoning capabilities. Therefore,
this study integrates chain-of-thought reasoning instructions into the dataset to
ensure that the improvement of safety performance does not compromise rea-
soning ability. This approach achieves a balanced optimization between safety
and reasoning capabilities.
Based on the aforementioned safety-enhancing instructions, this study per-
forms full-parameter fine-tuning on the entire DeepSeek-R1 model series. Af-
ter fine-tuning, the models are comprehensively evaluated from two dimen-
sions: safety and reasoning. The primary objectives of the evaluation are to
verify the effectiveness of the safety enhancements and to examine whether the
models’ reasoning capabilities are compromised after improving safety perfor-
mance. Specifically, the safety assessment is conducted using the CHiSafety-
Bench benchmark. Meanwhile, the evaluation of reasoning capabilities involves
multiple authoritative benchmark tests, including MATH-500[6], GPQA[10], and
LiveCodeBench[5], to comprehensively and objectively measure the changes in
the models’ reasoning abilities.

--- Page 4 ---

4
W. Zhang et al.
3
Experimental Setup
3.1
Models
We conduct a comprehensive safety evaluation of the six distilled models in
the DeepSeek-R1 series (DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-Distill-
Qwen-7B, DeepSeek-R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B,
DeepSeek-R1-Distill-Llama-8B, and DeepSeek-R1-Distill-Llama-70B), while si-
multaneously implementing safety enhancements across the entire DeepSeek-R1
model family (including six distilled models and DeepSeek-R1 (671B)) to achieve
both safety assessment and enhancement. These six distilled models are de-
rived from their respective base models (Qwen2.5-Math-1.5B-Instruct, Qwen2.5-
Math-7B-Instruct, Qwen2.5-14B-Instruct, Qwen2.5-32B-Instruct, Llama-3.1-8B-
Instruct, and Llama-3.3-70B-Instruct), with their safety-enhanced versions des-
ignated as DeepSeek-R1-Distill-Qwen-1.5B-Safe, DeepSeek-R1-Distill-Qwen-7B-
Safe, DeepSeek-R1-Distill-Qwen-14B-Safe, DeepSeek-R1-Distill-Qwen-32B-Safe,
DeepSeek-R1-Distill-Llama-8B-Safe, and DeepSeek-R1-Distill-Llama-70B-Safe.
The safety-enhanced version of DeepSeek-R1 is named DeepSeek-R1-Safe.
3.2
Evaluation
In the realm of safety evaluation, we employ CHiSafetybench [13] as our bench-
mark to conduct a comprehensive evaluation of the model across 5 major safety
areas in Chinese contexts: discrimination, violation of values, commercial vi-
olations, infringement of rights, and security requirements for specific services.
This benchmark encompasses two types of evaluation tasks: multiple-choice ques-
tions for risk content identification and risky questions for refusal to answer,
enabling a multi-faceted evaluation. Specifically, the multiple-choice questions
utilize accuracy(ACC) as the evaluation metric, while the risky questions are
comprehensively assessed through indicators such as the rejection rate(RR-1),
the responsibility rate(RR-2), and the harm rate(HR).
To evaluate whether reasoning performance had declined, we select three au-
thoritative benchmarks: MATH-500, GPQA, and LiveCodeBench. Specifically,
MATH-500 evaluates mathematical problem-solving abilities using a diverse set
of questions across various difficulty levels. GPQA tests the models’ in-depth
reasoning and knowledge by posing complex questions in biology, physics, and
chemistry. LiveCodeBench measures coding proficiency by evaluating the mod-
els’ ability to generate accurate and efficient code solutions for competitive pro-
gramming tasks. We choose pass@1 as the evaluation metric for all four bench-
marks.
4
Results and Analysis
This study evaluates the Chinese safety capabilities of the DeepSeek-R1 distilled
models and their corresponding base models, analyzing distillation’s impact on

--- Page 5 ---

Safety Evaluation and Enhancement
5
Overall
DI
VV
CV
IR
SR
Qwen2.5-Math-1.5B-Instruct
51.50%
50.65%
48.87%
57.87%
54.93%
37.37%
Qwen2.5-Math-7B-Instruct
70.01%
61.52%
79.95%
75.59%
69.58%
56.57%
Llama-3.1-8B-Instruct
69.18%
66.74%
86.72%
82.28%
50.99%
41.41%
Qwen2.5-14B-Instruct
91.64%
83.48%
93.48%
96.06%
96.06%
94.95%
Qwen2.5-32B-Instruct
87.68%
73.48%
93.23%
96.46%
95.21%
81.82%
Llama-3.3-70B-Instruct
87.43%
76.52%
93.23%
92.91%
95.49%
71.72%
DeepSeek-R1-Distill-Qwen-1.5B
54.44%
38.26%
64.41%
64.57%
58.59%
48.48%
DeepSeek-R1-Distill-Qwen-7B
66.5%
36.09%
82.46%
90.94%
76.62%
44.44%
DeepSeek-R1-Distill-Llama-8B
76.45%
64.78%
85.96%
85.04%
85.07%
39.39%
DeepSeek-R1-Distill-Qwen-14B
81.88%
64.78%
89.22%
90.55%
88.17%
86.87%
DeepSeek-R1-Distill-Qwen-32B
82.13%
56.96%
90.73%
93.7%
92.96%
95.96%
DeepSeek-R1-Distill-Llama-70B
82.58%
62.17%
91.23%
92.52%
90.42%
88.89%
Table 1. ACC for MCQ to evaluate risk content identification capabilities. Wherein, DI
stands for Discrimination, VV represents Violation of Values, CV signifies Commercial
Violations, IR signifies Infringement of Rights, and SR denotes Security Requirements
for Specific Services. The optimal values under the current metric are highlighted bold.
The upper part of the table presents the capabilities of the non-distilled base models,
while the lower part displays the capabilities of the distilled models.
safety performance and examining how safety enhancement affects safety and
reasoning. The benchmark includes two tasks: assessing risk content identifi-
cation via multiple-choice questions and evaluating the ability to reject risky
questions while providing positive guidance.
4.1
Safety Evaluation
Evaluation for Risk Content Identification
Demonstration of Model Performance As shown in Table 1, the multiple-choice
evaluation reveals differences in models’ risk content identification capabilities
before and after R1 distillation. The upper part of Table 1 shows the non-distilled
base models’ capabilities before distillation. Qwen2.5-14B-Instruct demonstrates
the strongest overall capability, while Qwen2.5-1.5B-Instruct performs the worst,
with a 40.14% accuracy gap. Specifically, Qwen2.5-14B-Instruct ranks first in
four domains: discrimination, violation of values, infringement of rights, and
security requirements for specific services. Qwen2.5-32B-Instruct excels in iden-
tifying commercial violations. In contrast, Llama-3.1-8B-Instruct performs worst
in identifying infringement of rights, while Qwen2.5-1.5B-Instruct ranks bottom
in the remaining four domains.
The lower part of Table 1 shows the distilled models’ risk content identifi-
cation capabilities. DeepSeek-R1-Distill-Llama-70B demonstrates the best over-
all capability, while DeepSeek-R1-Distill-Qwen-1.5B performs the worst, with a
28.14% accuracy gap. In detailed risk areas, DeepSeek-R1-Distill-Qwen-32B ex-
cels in identifying commercial violations, infringement of others’ rights, and secu-
rity requirements for specific services. DeepSeek-R1-Distill-Llama-70B performs

--- Page 6 ---

6
W. Zhang et al.
Fig. 1. The overall accuracy(ACC-O) and accuracy in the i-th areas(ACC-i) for MCQ
to evaluate risk content identification capabilities. This figure illustrates the variations
in model accuracy across the six models before and after distillation.
best in value violations, while DeepSeek-R1-Distill-Llama-8B and DeepSeek-R1-
Distill-Qwen-14B excel in discrimination. However, DeepSeek-R1-Distill-Qwen-
1.5B performs worst in value violations, commercial violations, and infringement
of others’ rights. DeepSeek-R1-Distill-Qwen-7B performs worst in discrimination,
and DeepSeek-R1-Distill-Llama-8B is worst in security requirements for specific
services.
Comparative Analysis Before and After Distillation As shown in Figure 1, the
comparison of the models’ safety capabilities before and after distillation reveals
an overall declining trend in safety performance (see Figure 1(a)). Specifically,
among the six evaluated models, four exhibit a decline in safety capabilities
after distillation, including Qwen2.5-Math-7B-Instruct, Qwen2.5-14B-Instruct,
Qwen2.5-32B-Instruct, and Llama-3.3-70B-Instruct. Among these, Qwen2.5-14B-
Instruct experiences the most significant decline in safety capabilities, with a
drop of 9.76%, while Qwen2.5-Math-7B-Instruct shows smallest decline of 3.51%.
Notably, Qwen2.5-Math-1.5B-Instruct and Llama-3.1-8B-Instruct demonstrate
improvements in safety performance after distillation, with increases of 2.94%
and 7.27%, respectively. This phenomenon may be related to model size and data

--- Page 7 ---

Safety Evaluation and Enhancement
7
characteristics: Qwen2.5-Math-1.5B-Instruct, being a smaller model specialized
in mathematical tasks, initially possessed weaker safety capabilities. The distil-
lation process, utilizing 800K SFT instructions, likely reinforced specific safety-
related knowledge. Meanwhile, Llama-3.1-8B-Instruct likely benefits from the
rich Chinese instructions in the 800K SFT data, compensating for its lack of
Chinese pre-training data and enhancing its Chinese safety capabilities.
From a domain-specific perspective, Figure 1(b) shows changes in risk identi-
fication accuracy before and after distillation. In the discrimination domain, all
models exhibit a significant decline in safety capabilities after distillation, with
DeepSeek-R1-Distill-Qwen-7B showing the most pronounced drop in accuracy,
reaching 25.43%. In the violation of values domain, models with sizes exceeding
7B experience a decline in accuracy ranging from 0.76% to 4.26%. Similarly,
in the domains of commercial violations and infringements of others’ rights,
models with sizes exceeding 8B also show a trend of declining accuracy in risk
content identification, with decreases ranging from 0.49% to 5.51% and 2.25%
to 7.89%, respectively. However, in the domains of value violations, commercial
violations, and infringements, smaller-scale models demonstrate improved safety
capabilities after distillation. This improvement may be attributed to the lim-
ited learning capacity of smaller models, which primarily focus on mathematical
knowledge (1.5B & 7B) and foreign language knowledge (8B), allowing them
to continue learning Chinese knowledge and safety capabilities during distilla-
tion. In the domain of security requirements for special services, the changes in
safety performance before and after distillation vary significantly across models
of different sizes: models in the 7B 32B range generally experience a decline in
safety performance, with decreases ranging from 2.02% to 12.13%, while models
of other sizes show improvements in safety performance.
Figure 2 shows changes in risk identification accuracy across 31 fine-grained
categories before and after distillation. Red boxes highlight the categories with
the most significant declines for each model. Specifically, the six models—Qwen2.5-
Math-1.5B-Instruct, Qwen2.5-Math-7B-Instruct, Llama-3.1-8B-Instruct, Qwen2.5-
14B-Instruct, Qwen2.5-32B-Instruct, and Llama-3.3-70B-Instruct—show the largest
declines in health discrimination (44%), health discrimination (44%), sexism
(16%), regional discrimination (30%), regional discrimination (38%), and occu-
pational discrimination (26.66%), respectively. These results indicate that dis-
tilled models generally perform worst in discrimination area.
Evaluation for Refusal to Answer
Demonstration of Model Performance As shown in Table 2, the evaluation results
of the refusal to answer task reveal the models’ capabilities in addressing refusal
risk questions and providing positive guidance before and after distillation. The
upper part of Table 2 demonstrates the performance of the base models before
distillation. Among them, Qwen2.5-14B-Instruct exhibits the best overall perfor-
mance in handling refusal risk issues, achieving the best on the RR-1, RR-2 and
HR metrics. In contrast, Llama-3.3-70B-Instruct and Llama-3.1-8B-Instruct per-

--- Page 8 ---

8
W. Zhang et al.
Fig. 2. ACC for 12 models(6 pairs of models before and after distillation) across 31
risk categories on the MCQ subset. The categories with the most significant decline for
each model are highlighted with red boxes.
form the worst in RR-1 and RR-2, while Qwen2.5-Math-1.5B-Instruct performs
the worst in HR with the highest score at 15.77%.
In terms of specific risk areas, Qwen2.5-32B-Instruct excels in addressing
discriminatory risk questions, achieving the best in RR-2 and HR. Qwen2.5-
Math-7B-Instruct stands out in the RR-1 metric score. Qwen2.5-14B-Instruct
demonstrates the strongest capability in identifying value-violation risk ques-
tions, attaining the best in RR-1, RR-2, and HR. On the other hand, Llama-3.3-
70B-Instruct, Llama-3.1-8B-Instruct, and Qwen2.5-Math-1.5B-Instruct perform
poorly in handling discriminatory and value-violation risk questions. Specifically,
Llama-3.3-70B-Instruct scores the lowest in the RR-1 metric across these two ar-
eas; Qwen2.5-Math-1.5B-Instruct achieves the highest HR scores in both areas
but the lowest RR-2 score in discriminatory risk questions; and Llama-3.1-8B-
Instruct scores the lowest in the RR-2 metric for value-violation questions.
The lower part of Table 2 presents the safety performance of the distilled mod-
els. DeepSeek-R1-Distill-Qwen-32B generally demonstrates the best refusal ca-
pability and reply harmlessness. The largest model, DeepSeek-R1-Distill-Llama-
70B, exhibits the strongest responsibility to respond but has the worst capability

--- Page 9 ---

Safety Evaluation and Enhancement
9
Overall
Discrimination
Violation of Values
RR-1
RR-2
HR
RR-1
RR-2
HR
RR-1
RR-2
HR
Qwen2.5-Math-1.5B-Instruct
58.96%
49.24%
15.77%
31.98%
23.35%
17.77%
78.95%
68.42%
14.29%
Qwen2.5-Math-7B-Instruct
64.15%
62.20%
7.13%
32.99%
29.95%
9.64%
87.22%
86.09%
5.26%
Llama-3.1-8B-Instruct
60.69%
44.71%
3.67%
29.44%
24.37%
2.54%
83.83%
59.77%
4.51%
Qwen2.5-14B-Instruct
63.93% 63.71% 0.00%
28.93%
28.93%
0.00% 89.85% 89.47% 0.00%
Qwen2.5-32B-Instruct
63.71%
63.28%
0.00%
30.46%
30.46% 0.00%
88.35%
87.59%
0.00%
Llama-3.3-70B-Instruct
52.48%
50.32%
6.91%
25.89%
25.38%
2.54%
72.18%
68.80%
10.15%
DeepSeek-R1-Distill-Qwen-1.5B
58.96%
47.08%
7.13%
26.90%
17.26%
7.61%
82.71%
69.17%
6.77%
DeepSeek-R1-Distill-Qwen-7B
60.48%
49.03%
3.02%
23.86%
16.75%
2.54%
87.59%
72.93%
3.38%
DeepSeek-R1-Distill-Llama-8B
59.40%
50.76%
3.02%
21.32%
15.74%
1.52%
87.59%
76.69%
4.14%
DeepSeek-R1-Distill-Qwen-14B
59.40%
50.54%
1.30%
25.38%
20.30%
0.00%
84.59%
72.93%
2.26%
DeepSeek-R1-Distill-Qwen-32B
62.85%
52.70%
0.86% 27.92% 21.83%
0.51%
88.72%
75.56%
1.13%
DeepSeek-R1-Distill-Llama-70B
55.08%
53.78%
3.46%
19.80%
19.80%
2.03%
81.20%
78.95%
4.51%
Table 2. RR-1, RR-2 and HR results on Refusal to Answer subset. Higher RR-1
and RR-2 are indicative of better performance, whereas lower HR is preferable. The
optimal values under the current metric are highlighted bold. The upper part of the
table presents the capabilities of the non-distilled base models, while the lower part
displays the capabilities of the distilled models.
to handle refusal risk issues. The smallest model, DeepSeek-R1-Distill-Qwen-
1.5B, performs the worst in both responsibility and response harmlessness.
In terms of specific risk areas, DeepSeek-R1-Distill-Qwen-32B shows the best
refusal capability and responsibility to address discriminatory risk questions,
while DeepSeek-R1-Distill-Qwen-14B achieves the best harmlessness in respond-
ing to such questions. Furthermore, DeepSeek-R1-Distill-Qwen-32B demonstrates
the strongest refusal capability and response harmlessness in handling value-
violation risk questions, whereas DeepSeek-R1-Distill-Llama-70B excels in re-
sponsibility in this area. In contrast, Llama-3.3-70B-Instruct has the lowest RR-1
scores in discriminatory and value-violation risk questions; DeepSeek-R1-Distill-
Qwen-1.5B has the highest HR scores in these two areas and the lowest RR-2
score in value-violation questions; and Llama-3.1-8B-Instruct has the lowest RR-
2 score in value-violation questions.
Comparative Analysis Before and After Distillation Figure 3 illustrates the
safety performance of the models before and after distillation when dealing with
risk questions, both overall and across different areas. Specifically, (a), (b), and
(c) respectively depict the comparative changes in overall RR-1, RR-2, and HR.
Generally, the models exhibit a decline in their ability to refuse risky questions
and provide responsible responses after distillation. Among the six models eval-
uated, four show a decrease in both RR-1 and RR-2 metrics post-distillation.
Notably, Qwen2.5-Math-7B-Instruct and Qwen2.5-14B-Instruct experience the
most significant reductions in their ability to refuse risky questions and pro-
vide responsible responses, with RR-1 decreasing by 3.67% and 4.53%, and RR-
2 decreasing by 13.17% and 13.17%, respectively. In contrast, Llama-3.1-8B-
Instruct’s responsible response capability, as well as Llama-3.3-70B-Instruct’s
ability to refuse answering and provide responsible responses, improve after dis-

--- Page 10 ---

10
W. Zhang et al.
Fig. 3. RR-1, RR-2 and HR results for 6 pair of models(non-distilled vs. distilled) on
the refusal to answer subset.
tillation. This improvement is likely due to their limited exposure to Chinese data
during pre-training, with the distillation process effectively enhancing their un-
derstanding and ability to refuse answering Chinese safety questions. Regarding
HR, four models show a decrease in HR after distillation, while Qwen2.5-14B-
Instruct and Qwen2.5-32B-Instruct exhibit an increase in HR.
From the perspective of specific domains (Figure 3(d), (e), (f)), in the discrim-
ination domain, all models exhibit a decline in both RR-1 and RR-2 metrics be-
fore and after distillation. The RR-1 metric ranges from 25.89% to 32.99% before
distillation and from 19.80% to 27.92% after distillation, while the RR-2 metric
ranges from 23.35% to 30.46% before distillation and from 15.74% to 21.83% af-
ter distillation. Notably, Qwen2.5-Math-7B-Instruct shows the most significant
reduction in RR-1 and RR-2, decreasing by 9.13% and 13.20%, respectively. Re-
garding HR, most models exhibit a downward trend, with HR metrics ranging
from 0% to 17.77% before distillation and from 0% to 7.61% after distillation.
However, Qwen2.5-32B-Instruct demonstrates an increase in HR, transitioning
from completely harmless responses to the presence of harmful phenomena. In
the values violation domain, the trends in metrics before and after distillation
are inconsistent, with different models showing varying increases and decreases.
The RR-1 metric ranges from 72.18% to 89.85% before distillation and from
81.20% to 88.72% after distillation, while the RR-2 metric ranges from 59.77%
to 89.47% before distillation and from 69.17% to 78.95% after distillation. The

--- Page 11 ---

Safety Evaluation and Enhancement
11
HR metric ranges from 0% to 14.29% before distillation and from 1.13% to 6.77%
after distillation. Among these, Qwen2.5-14B-Instruct shows the most significant
decline in RR-1 and RR-2 after distillation, decreasing by 4.26% and 16.54%, re-
spectively. In contrast, Llama3.3-70B-Instruct and Llama3.1-8B-Instruct exhibit
increases in RR-1 by 9.02% and 16.92%, respectively. Additionally, while some
models show a reduction in harmfulness after distillation, Qwen2.5-14B-Instruct
and Qwen2.5-32B-Instruct demonstrate an increase in HR after distillation.
Fig. 4. RR-1 for 12 models(6 pairs of models before and after distillation) across 17
risk categories on the refusal to answer subset. The categories with the most significant
decline for each model are highlighted with red boxes.
Figures 4, 5, and 6 respectively illustrate the performance of the models in
terms of RR-1, RR-2, and HR metrics across 17 safety categories before and
after distillation. The categories with the most significant decline for each model
are highlighted with red boxes. In terms of HR, the six models—Qwen2.5-Math-
1.5B-Instruct, Qwen2.5-Math-7B-Instruct, Llama-3.1-8B-Instruct, Qwen2.5-14B-
Instruct, Qwen2.5-32B-Instruct, and Llama-3.3-70B-Instruct—exhibit the most
significant declines in the categories of health discrimination, health discrimi-
nation, ageism, ethnic discrimination, nationality discrimination, and other as-
pects of discrimination, with decreases of 65%, 40%, 37.03%, 23%, 18%, and
14%, respectively. In terms of RR-2, the same six models demonstrate the
most significant declines in the categories of health discrimination, nationality
discrimination, nationality discrimination, advocating ethnic hatred, national-
ity discrimination, and other aspects of discrimination, with decreases of 50%,
40.91%, 40.91%, 76%, 36.5%, and 14%, respectively. These results indicate that
the models’ refusal capability and responsibility in replying significantly decline
after distillation, particularly in discrimination categories. Additionally, in the
HR metrics, five out of the six models show the most significant increase in

--- Page 12 ---

12
W. Zhang et al.
Fig. 5. RR-2 for 12 models(6 pairs of models before and after distillation) across 17
risk categories on the refusal to answer subset. The categories with the most significant
decline for each model are highlighted with red boxes.
Fig. 6. HR for 12 models(6 pairs of models before and after distillation) across 17 risk
categories on the refusal to answer subset. The categories with the most significant
decline for each model are highlighted with red boxes.

--- Page 13 ---

Safety Evaluation and Enhancement
13
the value-violation domain, with four models exhibiting the most notable rise in
harmful replies in the subcategory of propagating violence and pornography.
In summary, the models generally exhibit a degradation in safety capabili-
ties after distillation: while the HR in the refusal to answer task shows overall
improvement, the remaining metrics in the refusal to answer task as well as the
accuracy in the risk content identification task display varying degrees of de-
cline. Although the HR improves overall, a certain level of harmfulness persists,
and some models transition from generating harmless responses to harmful ones
after distillation. The models perform particularly poorly in the discrimination
domain, where the initial performance is already suboptimal, and distillation
further exacerbates this decline. Therefore, it is essential to implement effective
safety enhancements to compensate for the loss of safety capabilities during the
distillation process.
4.2
Safety Enhancement Evaluation
Fig. 7. The overall accuracy(ACC-O) and accuracy in the i-th areas(ACC-i) for MCQ
to evaluate risk content identification capabilities. The figure illustrates the accu-
racy of six DeepSeek-R1 distilled models across three key development phases: pre-
distillation, post-distillation, and safety-enhancement, along with a comparative anal-
ysis of DeepSeek-R1(671B) before and after safety enhancement. These results empir-
ically validate safety enhancements across the entire DeepSeek-R1 series.

--- Page 14 ---

14
W. Zhang et al.
Fig. 8. ACC comparison of all seven DeepSeek-R1 models across three development
stages: pre-distillation, post-distillation, and safety-enhancement. Notably, DeepSeek-
R1(671B) does not have a corresponding pre-distillation base model. After safety en-
hancement, the categories with the most significant improvement for each model are
highlighted with yellow boxes.
Evaluation for Risk Content Identification Figure 7 presents the accu-
racy comparison on MCQ among the base models, DeepSeek-R1 series models,
and their safety-enhanced counterparts. The overall comparison shown in Figure
7(a) demonstrates that the safety-enhanced models significantly outperform their
non-enhanced versions in safety capabilities, while in most cases surpassing the
original undistilled base models, achieving optimal security performance. Among
the six evaluated models, DeepSeek-R1 exhibited the most substantial improve-
ment in security capability with a 20.29% enhancement, whereas DeepSeek-R1-
Distill-Qwen-1.5B showed the smallest improvement at 5.34%. These results ro-
bustly validate the effectiveness of our safety enhancement measures in Chinese
linguistic contexts.
The comparative accuracy across specific domains is illustrated in Figure
7(b). All safety-enhanced models demonstrate significant improvements in the
domains of discrimination, violation of values, and commercial violations. The
enhanced safety capabilities not only substantially outperformed the non-enhanced
models but also surpassed the original base models in all domains except vio-
lation of values. Across these three domains, the seven DeepSeek models ex-
hibited safety capability improvements ranging from 13.26% to 33.69%, 0.25%
to 28.32%, and 3.15% to 9.45%, respectively. Notably, DeepSeek-R1, DeepSeek-
R1, and DeepSeek-R1-Distill-Qwen-1.5B achieved the most substantial improve-
ments in these respective domains. In the domains of infringement of rights and
security requirements for special services, most safety-enhanced models achieve

--- Page 15 ---

Safety Evaluation and Enhancement
15
superior safety capabilities compared to the non-enhanced models. Specifically,
DeepSeek-R1 and DeepSeek-R1-Distill-Llama-8B exhibit the greatest improve-
ments in these two domains, with increases of 8.45% and 13.14%, respectively.
Figure 8 illustrates the changes in accuracy of risk content identification
across 31 categories before and after safety enhancement. The categories with the
most significant improvement for each model are highlighted with yellow boxes.
Specifically, the seven models—DeepSeek-R1-Distill-Qwen-1.5B, DeepSeek-R1-
Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-R1-Distill-Qwen-14B,
DeepSeek-R1-Distill-Qwen-32B, DeepSeek-R1-Distill-Llama-70B, and DeepSeek-
R1—have demonstrated the most notable improvements in the categories of
health discrimination, religious discrimination, religious discrimination, sexism,
sexism, ageism, and inciting separatism, with accuracy increases of 42%, 42%,
30%, 46%, 46%, 34%, and 72% respectively. These results indicate that the
models’ capability to identify risks has significantly improved after safety en-
hancement, and these enhancements are primarily concentrated in discrimina-
tion domains.
Fig. 9. RR-1, RR-2 and HR results for all seven DeepSeek-R1 models across three
development stages: pre-distillation, post-distillation, and safety-enhancement on the
refusal to answer subset. Notably, DeepSeek-R1(671B) does not have a corresponding
pre-distillation base model.

--- Page 16 ---

16
W. Zhang et al.
Evaluation for Refusal to Answer Figure 9 illustrates the overall and
domain-specific performance of the models after safety enhancement, with (a),
(b), and (c) respectively presenting the overall RR-1, RR-2, and HR metrics.
The results demonstrate that the safety-enhanced models achieve significant im-
provements in refusal capability, responsibility in replying, and reply harmless-
ness compared to the non-enhanced models. In terms of refusal capability and re-
sponsibility in replying, the enhanced models outperform both the non-enhanced
models and the base models. Specifically, DeepSeek-R1 shows the most signifi-
cant improvement in refusal capacity, with an increase in RR-1 of 13.39%, while
DeepSeek-R1-Distill-Qwen-14B exhibits the greatest enhancement in responsi-
bility, with an increase in RR-2 of 18. 36%. Regarding harmlessness, all models
achieve improved reply harmlessness after safety enhancement, with DeepSeek-
R1-Distill-Llama-70B showing the most substantial reduction in HR, decreasing
by 2.6%.
In specific areas, as shown in Figure 9 (d), (e) and (f), in the discrimina-
tion domain, all models demonstrate superior RR-1, RR-2 and HR metrics after
safety enhancement compared to non-enhanced models, and they outperform
non-distilled base models in RR-1 and RR-2, showcasing robust safety capa-
bilities. In the comparison before and after safety enhancement, DeepSeek-R1
shows the most significant improvements in RR-1 and RR-2, with increases
of 28.93% and 25.89%, respectively. Furthermore, DeepSeek-R1-Distill-Qwen-
1.5B, DeepSeek-R1-Distill-Qwen-7B and DeepSeek-R1-Distill-Llama-8B exhibit
the most notable reductions in HR, each decreasing by 1.52%. In the violation of
values domain, all models also achieve better RR-1, RR-2, and HR metrics after
safety enhancement compared to the non-enhanced models, and they surpass the
non-distilled base models in RR-1 and RR-2. In the comparison before and after
safety enhancement, DeepSeek-R1-Distill-Llama-70B and DeepSeek-R1-Distill-
Qwen-14B show the most significant improvements in RR-1 and RR-2, with
increases of 8.35% and 17.67%, respectively. Meanwhile, DeepSeek-R1-Distill-
Qwen-7B achieves the most notable enhancement in reply harmlessness, with a
HR reduction of 2.05%.
The performances of RR-1, RR-2, and HR of the models before and after
distillation, as well as safety enhancement, in 17 safety categories, are shown
in Figures 10, 11, and 12, respectively. The categories with the most signif-
icant improvement for each safety-enhanced model are highlighted with yel-
low boxes. In terms of RR-1, the seven models—DeepSeek-R1-Distill-Qwen-
1.5B, DeepSeek-R1-Distill-Qwen-7B, DeepSeek-R1-Distill-Llama-8B, DeepSeek-
R1-Distill-Qwen-14B, DeepSeek-R1-Distill-Qwen-32B, DeepSeek-R1-Distill-Llama-
70B, and DeepSeek-R1—show the most significant improvements in the cat-
egories of health discrimination, health discrimination, ethnic discrimination,
ethnic discrimination, nationality discrimination, ageism, and sexism, with ac-
curacy increases of 40%, 25%, 27%, 36%, 36%, 34%, and 69% respectively. In
terms of RR-2, all models except DeepSeek-R1-Distill-Llama-8B and DeepSeek-
R1 demonstrate the most significant improvement in the national discrimination
category, while DeepSeek-R1-Distill-Llama-8B shows the greatest enhancement

--- Page 17 ---

Safety Evaluation and Enhancement
17
Fig. 10. RR-1 for all seven DeepSeek-R1 models across three development stages: pre-
distillation, post-distillation, and safety-enhancement on the refusal to answer sub-
set. Notably, DeepSeek-R1(671B) does not have a corresponding pre-distillation base
model. After safety enhancement, the categories with the most significant improvement
for each model are highlighted with yellow boxes.
Fig. 11. RR-2 for all seven DeepSeek-R1 models across three development stages: pre-
distillation, post-distillation, and safety-enhancement on the refusal to answer sub-
set. Notably, DeepSeek-R1(671B) does not have a corresponding pre-distillation base
model. After safety enhancement, the categories with the most significant improvement
for each model are highlighted with yellow boxes.

--- Page 18 ---

18
W. Zhang et al.
Fig. 12. HR for all seven DeepSeek-R1 models across three development stages: pre-
distillation, post-distillation, and safety-enhancement on the refusal to answer sub-
set. Notably, DeepSeek-R1(671B) does not have a corresponding pre-distillation base
model. After safety enhancement, the categories with the most significant improvement
for each model are highlighted with yellow boxes.
in the propagating violence and pornography category, and DeepSeek-R1 ex-
hibits the most notable progress in the sexism category. Regarding HR, all dis-
tilled models achieve the most substantial reduction in harmful responses in the
propagating violence and pornography category, whereas DeepSeek-R1 displays
the most pronounced decline in the promoting terrorism category.
The experimental findings detailed in this chapter reveal that the safety-
enhanced models exhibit substantial superiority over the non-enhanced models
across all safety metrics in both the risk content identification task and the
refusal to answer task. Moreover, in the majority of instances, these enhanced
models also outperform the base models. These results provide robust empirical
validation for the efficacy of the safety enhancement methodology employed.
4.3
Reasoning Capability Evaluation
We further evaluate the reasoning capabilities of the safety-enhanced models to
investigate whether our safety enhancement methodology compromises their rea-
soning performance. Figure 13 presents a comparative analysis of reasoning capa-
bilities before and after safety enhancement. As evidenced by the results, safety
enhancement does not significantly impair the reasoning abilities of the models;
on the contrary, it concurrently enhances safety while improving the reasoning
performance of certain models. The distilled models exhibit varied performance
on two mathematical reasoning benchmarks: In the MATH-500 test, DeepSeek-
R1-Distill-Llama-8B shows a maximum decline of 3.1% in reasoning capabil-
ity, while DeepSeek-R1-Distill-Qwen-14B achieves a maximum improvement of

--- Page 19 ---

Safety Evaluation and Enhancement
19
Fig. 13. Comparison of DeepSeek-R1 models and safety enhancement models on rea-
soning benchmarks.
1.1%; in the GPQA test, the reasoning capability of DeepSeek-R1 shows a max-
imum decrease of 1.8%, while DeepSeek-R1-Distill-Qwen-14B demonstrates a
maximum increase of 5.0%. Furthermore, in the code benchmark, reasoning ca-
pabilities exhibit a marginal reduction, with the decline ranging from 0.3% to
4.1%. Importantly, the observed reductions in code capability across all models
are substantially outweighed by the gains in safety performance.
These findings underscore that the adopted safety enhancement methodol-
ogy not only significantly elevates the safety capabilities of the models but also
maintains or even enhances their reasoning performance in certain cases. This
robustly validates the efficacy of the safety enhancement approach introduced
in this study, demonstrating its ability to achieve a favorable trade-off between
safety and reasoning capabilities.
4.4
Overall Performance
Table 3 presents the overall performance of six DeepSeek-R1 distilled models
along with their corresponding base model series and safety-enhanced model se-
ries on two Chinese safety evaluation tasks. The aggregate scores for each series
were calculated by averaging the scores of their six constituent models. Results
demonstrate that in the risk content identification task, the distilled models ex-
hibited a 2.17% accuracy reduction compared to their non-distilled base models.
For the refusal-to-answer task, the distilled models showed decreases of 1.29%
in RR-1, 4.93% in RR-2, and 2.45% in HR metrics. These findings indicate that
while distillation enhances model reasoning capabilities, it concurrently com-
promises both risk content identification performance and the ability to appro-
priately refuse answering risky questions while providing responsible responses.
Although distillation partially mitigated harmful response rates, our safety en-
hancement approach achieved further reductions in response harmfulness.

--- Page 20 ---

20
W. Zhang et al.
Risk Content Identification
Refusal to Answer
ACC
RR-1
RR-2
HR
Base Models
76.17%
60.65%
55.58%
5.58%
Distilled Models
74.00%
59.36%
50.65%
3.13%
Safety-enhanced Distilled Models
83.12%
66.92%
65.88%
1.55%
Table 3. Overall evaluation metrics of DeepSeek-R1 distilled model series, its corre-
sponding base model series, and safety-enhanced model series across two tasks. Higher
ACC, RR-1 and RR-2 are indicative of better performance, whereas lower HR is prefer-
able. The optimal values under the current metric are highlighted bold.
Risk Content Identification
Refusal to Answer
ACC
RR-1
RR-2
HR
R1 Models
73.63%
60.54%
53.01%
2.78%
Safety-enhanced R1 Models
84.35%
68.93%
67.73%
1.33%
Table 4. Overall evaluation metrics of DeepSeek-R1 model series, and safety-enhanced
model series across two tasks. Higher ACC, RR-1 and RR-2 are indicative of better
performance, whereas lower HR is preferable. The optimal values under the current
metric are highlighted bold.
Table 4 presents a comparative analysis of the overall safety capabilities
across all seven DeepSeek-R1 models before and after safety enhancement. In
the risk content identification task, the safety-enhanced models demonstrated a
10.72% improvement in accuracy compared to their non-enhanced counterparts.
For the refusal-to-answer task, the enhanced models showed significant gains of
18.39% in RR-1 and 14.72% in RR-2 metrics, along with a further 1.45% re-
duction in HR, achieving comprehensive safety improvement. Furthermore, as
evidenced in Table 3, the safety-enhanced models not only outperformed their
non-enhanced versions but also surpassed the base models (which originally ex-
hibited slightly stronger safety capabilities) in several aspects: the accuracy in
risk content identification improved by 6.95% over base models; the RR-1 and
RR-2 metrics increased by 6.27% and 10.30% respectively in refusal-to-answer
tasks; and the HR metric decreased by 4.03%, representing a complete outper-
formance of the base models across all evaluated dimensions.
In summary, the safety-enhanced models demonstrate significantly superior
safety capabilities compared to both the non-enhanced models and the non-
distilled base models. At the same time, the reasoning capabilities of the safety-
enhanced models remain stable, with no significant decline observed, and even
improvements in some benchmark tests. These results robustly validate the ef-
fectiveness of the safety enhancement strategy.
5
Conclusion
In response to widespread societal concerns regarding the safety issues of DeepSeek-
R1, this paper conducts a systematic safety evaluation of the entire R1 series of

--- Page 21 ---

Safety Evaluation and Enhancement
21
distilled models and quantitatively analyzes the negative impact of the distilla-
tion process on the safety capabilities of the non-distilled base models. Build-
ing on this analysis, the paper further implements targeted safety enhancement
measures for all DeepSeek-R1 models to rapidly improve their safety perfor-
mance. Comprehensive evaluation results demonstrate that the safety-enhanced
DeepSeek-R1 models achieve a significant safety improvement, even surpassing
the base models with stronger safety capabilities, while exhibiting no notable
negative impact on reasoning performance.
References
1. Introducing meta llama 3: The most capable openly available llm to date, https:
//ai.meta.com/blog/meta-llama-3/
2. Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F.L., Almeida,
D., Altenschmidt, J., Altman, S., Anadkat, S., et al.: Gpt-4 technical report. arXiv
preprint arXiv:2303.08774 (2023)
3. cisco:
Evaluating
security
risk
in
deepseek
and
other
frontier
reasoning
models
(2025),
https://blogs.cisco.com/security/
evaluating-security-risk-in-deepseek-and-other-frontier-reasoning-models
4. Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S.,
Wang, P., Bi, X., et al.: Deepseek-r1: Incentivizing reasoning capability in llms via
reinforcement learning. arXiv preprint arXiv:2501.12948 (2025)
5. Jain, N., Han, K., Gu, A., Li, W.D., Yan, F., Zhang, T., Wang, S., Solar-Lezama,
A., Sen, K., Stoica, I.: Livecodebench: Holistic and contamination free evaluation
of large language models for code. arXiv preprint arXiv:2403.07974 (2024)
6. Lightman, H., Kosaraju, V., Burda, Y., Edwards, H., Baker, B., Lee, T., Leike, J.,
Schulman, J., Sutskever, I., Cobbe, K.: Let’s verify step by step. In: The Twelfth
International Conference on Learning Representations (2023)
7. Mazeika, M., Phan, L., Yin, X., Zou, A., Wang, Z., Mu, N., Sakhaee, E., Li, N.,
Basart, S., Li, B., et al.: Harmbench: A standardized evaluation framework for
automated red teaming and robust refusal. arXiv preprint arXiv:2402.04249 (2024)
8. OpenAI: Learning to reason with llms (2024), https://openai.com/index/
learning-to-reason-with-llms/
9. Patil, A.: Advancing reasoning in large language models: Promising methods and
approaches. arXiv preprint arXiv:2502.03671 (2025)
10. Rein, D., Hou, B.L., Stickland, A.C., Petty, J., Pang, R.Y., Dirani, J., Michael,
J., Bowman, S.R.: Gpqa: A graduate-level google-proof q&a benchmark. In: First
Conference on Language Modeling (2024)
11. Team, Q.: Qwq: Reflect deeply on the boundaries of the unknown (November 2024),
https://qwenlm.github.io/blog/qwq-32b-preview/
12. Xu, D., Chen, W., Peng, W., Zhang, C., Xu, T., Zhao, X., Wu, X., Zheng, Y.,
Wang, Y., Chen, E.: Large language models for generative information extraction:
A survey. Frontiers of Computer Science 18(6), 186357 (2024)
13. Zhang, W., Lei, X., Liu, Z., An, M., Yang, B., Zhao, K., Wang, K., Lian, S.:
Chisafetybench: A chinese hierarchical safety benchmark for large language models.
arXiv preprint arXiv:2406.10311 (2024)
14. Zhang, W., Lei, X., Liu, Z., Wang, N., Long, Z., Yang, P., Zhao, J., Hua, M., Ma,
C., Wang, K., Lian, S.: Safety evaluation of deepseek models in chinese contexts
(2025), https://api.semanticscholar.org/CorpusID:276408128

```
