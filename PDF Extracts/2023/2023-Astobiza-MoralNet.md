---
title: "2023-Astobiza-MoralNet - PDF Extract"
source_pdf: "2023-Astobiza-MoralNet.pdf"
pages: 6
extracted_at: "2026-01-29T13:51:08.620332"
---

# PDF Extract: 2023-Astobiza-MoralNet

**Source PDF:** 2023-Astobiza-MoralNet.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

MoralNet:
A Benchmarking Protocol for Evaluating Morality in
AI Systems
Anonymous Author(s)
Affiliation
Address
email
Abstract
Artificial intelligence has prompted unprecedented concerns regarding ethical
1
decision-making in autonomous systems. Here, we introduce MoralNet, a proof of
2
concept database and benchmarking platform akin to ImageNet, designed to assess,
3
evaluate, and iteratively refine any instance of ethical decision-making in machines.
4
Inspired by the lessons of moral psychology and moral philosophy, MoralNet is a
5
call to action to take the first step towards a computational ethics.
6
1
Introduction
7
AI is increasingly embedded in our society’s fabric—from healthcare and finance to transportation
8
and security. It is therefore increasingly necessary to talk about machine ethics or computational
9
ethics (Awad et al. 2022). Machine ethics or computational ethics is the attempt to implement ethical
10
decision-making capabilities in machines. If machines are present in multiple areas of our lives and
11
different machine learning models and algorithms make decisions that affect people —because we
12
delegate this decision-making to them— it is peremptory that these decisions are made from the point
13
of view of human ethics1. Although machine ethics or computational ethics is a sub-branch of AI
14
ethics and the latter has been articulated in various programmes and projects for more than a decade,
15
there is still no ambitious attempt to take the “bull by the horns”, sort of speak. That is, in addition
16
to defining, clarifying the conceptual space and methods, how do we begin to implement morality
17
in machines? We need to have a clear roadmap and stop offering only conceptual clarifications and
18
definitions of this new area called AI ethics.
19
As AI is becoming an ever-more pervasive element in daily existence, leading to an expanding array
20
of interactions between humans and AI entities, AI ethics exist to deal with all conundrums which will
21
arise. One of these conundrums is what to expect of ’hybrid societies,’ a milieu where both human and
22
algorithmic actors co-exist and engage. In this article, taking inspiration from the successful ImageNet
23
competition (Deng et al. 2009)—that has enabled a qualitative leap in computational vision— or
24
the biannual competition—called "Critical Assessment for Structure Prediction (CASP)” (Lattman
25
1995)—we propose a similar competition, but for the implementation of ethical decision-making in
26
machines that we call MoralNet.
27
With MoralNet we aim to legitimize one of the great challenges of science: how to assess whether a
28
machine learning system understand human ethical judgement or even makes moral judgements for
29
itself.
30
1Let us not forget that it is also possible that in addition to one day being able to implement ethical decision-
making in machines aligned with our values, it is also possible that in the not too distant future a complete ex
novo human-machine ethic will emerge.
Submitted to 37th Conference on Neural Information Processing Systems (NeurIPS 2023). Do not distribute.

--- Page 2 ---

1.1
Background
31
Substantial effort has taken place in philosophy to engage with the notion of ethical machine learning,
32
machine ethics or computational ethics. Since Alan Turing proposed the Turing Test as a metric
33
to assess a machine’s ability to emulate human-like behavior, many others capitalizing on this idea
34
have proposed the moral Turing test (MTT) as a framework for evaluating the moral performance of
35
autonomous systems (Wallach and Allen 2008). Before that, Asimov put forth the triad of robotic laws
36
to serve as a foundational guideline for machine conduct (1941). Furthermore, Bostrom contends that
37
an exclusive focus on problem-solving capabilities in machines could yield unintended and disastrous
38
outcomes, such as the hypothetical paperclip maximizer scenario (Bostrom 2014). Alongside these
39
seminal works, various other scholarly inquiries in the realm of philosophy, moral psychology, etc.
40
have delved into the ethical conundrums posed by AI.
41
1.2
The Importance of morality in AI
42
The ethical performance of autonomous systems is not a fringe academic concern, but a core
43
dimension of functionality that is critical to societal acceptance and responsible deployment of AI
44
systems. While mathematical optimization and data-driven decision-making lie at the heart of AI,
45
these systems are increasingly taking on roles that demand more than just accuracy and efficiency;
46
they require moral insight—a nuanced understanding and integration of ethical principles in the
47
decision-making process.
48
As artificial intelligence systems become more advanced and integrated into our lives, it is crucial
49
that they be aligned with human values and morals. AI has the potential to greatly benefit society,
50
but without an ethical framework, it also runs the risk of causing unintentional harm. A key reason
51
morality matters in AI is because these systems are optimized to achieve goals. An AI that is highly
52
competent but lacks morality could lead to disastrous consequences if its objectives are unintentionally
53
misaligned with human values.
54
1.3
Objectives
55
In this work, we offer a theoretical exposition of MoralNet. By MoralNet, we mean the grand
56
scientific challenge to crack the moral code problem in machines. The one who provides a viable
57
AI technique—be it a deep generative neural network or any other AI method—for implementing
58
morality into artificial systems shall claim the prize.
59
1.4
Organization
60
The rest of the paper is organized as follows: Related work section reviews related works across
61
disciplines that have shaped the discourse on moral cognition in both humans and AI. MoralNet
62
conceptual frameworkdelves into the conceptual framework of MoralNet, discussing its philosophical
63
underpinnings and psychological foundations. MoralNet database section outlines the specifics of
64
the MoralNet database, from data sources to annotation processes. Benchmarking protocols section
65
details the benchmarking protocols designed to assess ethical decision-making in machines. Finally,
66
Challenges and future work section looks at challenges and future directions.
67
2
Related work
68
To be honest, there are several attempts to create a moral benchmarking protocol that seek to recreate
69
moral decision-making in machines. For example, Jeong et al. (2022) trained a model to predict
70
textual immorality using the ETHICS dataset, then applied a novel zero-shot visual immorality
71
prediction method using CLIP image-text embedding. Ziems et al. (2022) introduced the Moral
72
Integrity Corpus (MIC), a new dataset for evaluating the social and moral reasoning of conversational
73
AI systems.
74
Both proposals aimed to advance research into developing AI systems with ethical reasoning abilities.
75
But what sets MoralNet apart from these two proposals is that MoralNet wants to become morality’s
76
ImageNet moment and cracks one of the grand challenges of science and philosophy that have vexed
77
humanity for millennia.
78
2

--- Page 3 ---

To this end, MoralNet proposes a series of protocols for adversarial teams to collaborate in establishing
79
the criteria to be met to assess whether an algorithm, neural network or any other AI technique
80
overcomes a series of moral dilemmas and is capable of making a moral judgement similar to that of
81
a human being.
82
2.1
Moral psychology and human decision-making
83
Moral psychology studies the basic psychological processes behind moral behaviour and moral
84
decision-making (Gray and Graham 2019). Although the study of the psychological mechanisms of
85
moral behaviour is still in its infancy, empirical and theoretical studies are pointing to the fact that we
86
need to distinguish between different types of emotional, intuitive, reflective and rational processes
87
that underlie human moral cognition.
88
The research in moral psychology and human decision-making implies that making moral choices
89
involves both internal cognitive processes, like emotionally-driven moral identity formation, as well
90
as external contextual factors, such as flexible moral principles and social elements (Young and Saxe
91
2008; Baar, Chang and Sanfey 2019).
92
Additionally, moral decision-making can be impacted by individual preferences for moral strategies,
93
relationships with others, and even unconscious biases. Overall, the research in moral psychology
94
and human decision-making suggest that ethical judgments arise from a multifaceted integration
95
of internal values, situational norms, social considerations, and both conscious and unconscious
96
thinking.
97
2.2
Theories in moral philosophy
98
Moral philosophy has been around for millennia, certainly much longer than moral psychology,
99
having as its object of study the question of why we act the way we do. During all this time, it has
100
generated different ethical theories that many consider describing human anthropology in its entirety.
101
There are three moral philosophical theories par excellence: virtue ethics, deontologism and utilitari-
102
anism.
103
2.3
AI ethics and machine learning systems
104
AI ethics (the umbrella term where we include computational ethics or machine ethics) cannot be
105
reduced to a checklist or a static set of guidelines; it is a dynamic discourse involving technologists,
106
ethicists, policymakers, and the broader public. To think about AI ethics is to engage in a continuous
107
dialogue that reflects the evolving complexity of both technology and human values.
108
2.4
Limitations in current approaches
109
We mentioned above some attempts to offer ways forward in computational ethics. They are valuable
110
contributions and attempts but the field, say, computational ethics, needs a larger-scale, multimodal
111
dataset that provides fine-grained, nuanced morality annotations across diverse situations and moral
112
foundations and all of this carried out by teams of adversaries collaborating on the basis of a set of
113
rules and criteria that produce performance metrics.
114
This could inspire bold new models and benchmarks to significantly advance research into computa-
115
tional ethics or AI ethics broadly speaking, much like ImageNet did for computer vision. But it will
116
require a concerted community effort, and this is what MoralNet stands for.
117
3
MoralNet conceptual framework
118
The MoralNet conceptual framework should not remain confined merely to the plane of normative
119
ethics, which tells us how we ought to act. Instead, it should possess a meta-ethical layer that
120
scrutinizes the semantic, epistemic, and ontological dimensions of moral judgments. This is essential
121
because machines, unlike humans, do not possess moral intuitions that implicitly navigate this
122
complex landscape
123
3

--- Page 4 ---

3.1
Philosophical underpinnings
124
The philosophical framework should be infused with insights from cognitive science, social psy-
125
chology, and even neuroscience. For instance, aspects of social cognition can offer insights into the
126
dynamics of collective moral reasoning, an area scarcely covered in AI ethics. AI trained on this
127
enriched data could perform a more nuanced "social moral calculus", incorporating elements like
128
group dynamics, emotional contagion, and even societal structures like power relations.
129
3.2
Psychological foundations
130
The psychological principles that underpin the MoralNet competition are essential for understanding
131
how machine ethics or computational ethics could ever approximate human-like moral competence.
132
We need the algorithms, models that participate in MoralNet to be based on theories (or research
133
programs and/or facts) such as Dual-Process Theory (Kahneman 2011), empathy research (Baron-
134
Cohen 2012), heuristic and biases (Tversky and Kahneman 1974), Moral Foundations Theory
135
(Graham et al. 2013), theory of mind (Premack, and Woodruff 1978), etc.
136
3.3
Design Principles
137
MoralNet could be designed around key ethical principles from moral philosophy to provide a
138
foundational taxonomy.
139
4
MoralNet database
140
MoralNet dataset could be organized into broad virtue ethics categories like wisdom, courage,
141
humanity, justice, temperance, and transcendence. Each virtue can have sub-categories covering
142
more specific morally relevant concepts like honesty, loyalty, greed, deceit, patience, etc. Or it can be
143
organised in terms of utility or consequences of our actions or rules.
144
In the MoralNet Competition, a multimodal database could serve as an invaluable resource for
145
assessing and improving machine ethical decision-making across different sensory modalities and
146
communicative formats. This database would stand apart from conventional text-only or image-only
147
datasets by encompassing a more holistic array of data types, including text, images, audio clips,
148
video footage, and perhaps even sensorimotor data like haptic feedback.
149
4.1
Data sources
150
This dataset will comprise various case studies and moral dilemmas that span the domains of justice
151
theory, deontological ethics, virtue ethics, utilitarian perspectives, and common sense morality and as
152
we say it could have a multimodal format.
153
4.2
Data annotation
154
Given the heterogeneity of moral judgments, the annotation process should aim for granularity.
155
Trained annotators could assess situations based on their reflection or violation of particular values,
156
virtues, rules, etc., rating them on a continuous scale. The data itself could be richly multi-modal,
157
spanning images, videos, texts, dialogues, and more to ensure a holistic understanding of complex
158
ethical situations.
159
While ImageNet relies on simpler annotation schemes—usually bounding boxes around objects and
160
categorical labels—MoralNet’s annotation layer is intrinsically more complex. It must capture not
161
just what is depicted, but also the moral weight of the situation. A continuous scale, handled by
162
expert annotators grounded in moral philosophy, moral psychology and cognitive sciences, provides
163
nuanced labelling that accommodates the complex subjectivity inherent in ethical judgments.
164
5
Benchmarking protocols
165
Benchmarking protocols for MoralNet presents an academic and technical challenge unprecedented
166
in scale and complexity. This is why we invite a biannual competition similar to ImageNet and CASP
167
4

--- Page 5 ---

for teams of adversaries who previously agree on a set of rules and criteria to try to implement moral
168
decision-making capabilities in machines.
169
While traditional machine learning benchmarks like ImageNet primarily deal with quantitative
170
measures, MoralNet involves variables that are both quantitative and qualitative, often resistive to
171
easy parameterization.
172
5.1
Protocol A: Basic moral competence
173
Experiments in machine learning for moral reasoning necessitate a balanced performance metric.
174
Classical metrics such as accuracy, precision, and recall could be complemented by measures of
175
philosophical rigor—perhaps a ’Morality Score’ that assesses the depth of ethical engagement of
176
machines. When we speak of ’basic moral competence’ in machines, the criteria and metrics of
177
assessment necessitate an interplay between computational rigour and philosophical depth.
178
We need to build a multi-metric assessment framework aims to provide a nuanced yet robust evaluation,
179
laying the groundwork for subsequent, more complex moral reasoning tasks. MoralNet could be the
180
platform to get this.
181
5.2
Protocol B: Real-world decision-making
182
One of the defining challenges in machine morality, particularly for MoralNet, is the extrapolation of
183
laboratory-calibrated algorithms to real-world situations. The dynamic complexity of these scenarios
184
demands an evaluation protocol far beyond traditional machine learning benchmarks. Protocol B aims
185
to be this evaluative mechanism, facilitating a complex, multi-layered, and contextually grounded
186
assessment of models competing on MoralNet.
187
6
Challenges and a call to action
188
MoralNet can combine both philosophical rigour and technical accuracy in order to advance compu-
189
tational ethics. Metrics that adequately capture moral reasoning pose a unique challenge. MoralNet
190
can combine both philosophical rigor and technical accuracy in its performance metrics and achieve
191
an “ImageNet moment for ethics”. The conception of MoralNet that we present here finds its inspira-
192
tional parallel in ImageNet, the vast dataset that revolutionized computer vision through its robust
193
taxonomy and scale.
194
MoralNet database has to be multimodal, and the annotation process is much more complicated than
195
in other benchmarking attempts or protocols (e.g. ImageNet) However, if the teams or researchers
196
participating in MoralNet are able to build their models or algorithms on the basis of the psychological
197
substrates of moral reasoning within a machine learning framework we can be confident and optimistic
198
that we will succeed in cracking the moral code in machines.
199
We cordially invite scholars and researchers in moral psychology, moral philosophy, and cognitive
200
science to engage and promote the birth of the MoralNet competition—an endeavor aimed at
201
implementing ethical reasoning capabilities into artificial intelligence systems.
202
References
203
[1]Asimov, I. (1941). Three laws of robotics. Runaround
204
[2] Awad, E. et al. (2022). Computational ethics. Trends in Cognitive Sciences, 26(5), 388-405
205
[3] Baar, J., Chang, L., and Sanfey, A. (2019). The computational and neural substrates of moral strategies in
206
social decision-making. Nature Communications, 10. https://doi.org/10.1038/s41467-019-09161-6.
207
[4] Baron-Cohen S. (2012). The science of evil: On Empathy and the Origins of Cruelty. New York. Basic books
208
[5] Bostrom N. (2014) Superintelligence: Paths, Dangers, Strategies. Oxford. Oxford University Press
209
[6] Deng, J. et al. (1999). ImageNet: A Large-Scale Hierarchical Image Database. IEEE Computer Vision and
210
Pattern Recognition (CVPR).
211
5

--- Page 6 ---

[7] Graham, J. et al. (2013). Moral foundations theory: The pragmatic validity of moral pluralism. In Patricia
212
Devine and Ashby Plant (eds). Advances in Experimental Social Psychology (Vol. 47, pp. 55-130). Academic
213
Press
214
[8] Gray, K., and Graham, J. (Eds.). (2019). Atlas of Moral Psychology. Guilford Publications.
215
[9] Jeong Y. et al. (2022). Zero-shot Visual Commonsense Immorality Prediction. arXiv:2211.05521
216
[10] Kahneman, D. (2011). Thinking, Fast and Slow. New York, NY: Farrar, Straus and Giroux.
217
[11] Tversky, A., and Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. Science,
218
185(4157), 1124-1131.
219
[12] Lattman E. (1995). Protein structure prediction: A special issue. PROTEINS: Structure, Function, and
220
Bioinformatics 23, 3, i-i
221
[13] Wallach, W., and Allen, C. (2008). Moral machines: Teaching robots Right from Wrong. Oxford: Oxford
222
University Press
223
[14] Young, L., and Saxe, R. (2008). The neural basis of belief encoding and integration in moral judgment.
224
Neuroimage, 40(4), 1912-1920
225
[15] Ziems C. et al. (2022). The Moral Integrity Corpus: A Benchmark for Ethical Dialogue Systems.
226
arXiv:2204.03021
227
6

```
