---
title: "Ten Hard Problems in Artificial Intelligence We - PDF Extract"
source_pdf: "2024-Leech-Ten Hard Problems in Artificial Intelligence We.pdf"
pages: 94
extracted_at: "2026-01-29T14:01:13.960179"
---

# PDF Extract: Ten Hard Problems in Artificial Intelligence We

**Source PDF:** 2024-Leech-Ten Hard Problems in Artificial Intelligence We.pdf
**Total Pages:** 94

---

## Content

```
--- Page 1 ---

Ten Hard Problems in Artificial Intelligence We Must Get Right
GAVIN LEECH∗, University of Bristol and Arb Research,
SIMSON GARFINKEL∗, BasisTech, LLC,
MISHA YAGUDIN, ALEXANDER BRIAND, and ALEKSANDR ZHURAVLEV, Arb Research,
We explore the AI2050 “hard problems” that block the promise of AI and cause AI risks: (1) developing general capabilities of
the systems; (2) assuring the performance of AI systems and their training processes; (3) aligning system goals with human
goals; (4) enabling great applications of AI in real life; (5) addressing economic disruptions; (6) ensuring the participation of
all; (7) at the same time ensuring socially responsible deployment; (8) addressing any geopolitical disruptions that AI causes;
(9) promoting sound governance of the technology; and (10) managing the philosophical disruptions for humans living in the
age of AI. For each problem, we outline the area, identify signiﬁcant recent work, and suggest ways forward. Note: this paper
reviews literature through January 2023.
CCS Concepts: • Computing methodologies →Artiﬁcial intelligence; • Social and professional topics →Computing
/ technology policy.
Additional Key Words and Phrases: Artiﬁcial Intelligence, AI2050, Hard Problems, Wicked Problems, Schmidt Futures
1
Introduction
Artiﬁcial intelligence has begun to revolutionize science and engineering through the automated discovery of
new drugs, building materials, and even techniques for fusion energy (see HP#4). At the same time, current
generative AI systems can create targeted disinformation and automate the production of hate speech—and these
are only two examples of how the beneﬁts and dangers of AI have progressed from hypotheticals to actual issues
we must address in the near term.
In response to such opportunities and risks, the AI2050 program was initiated, drawing on previous research
and numerous conversations with experts.1 This paper reviews the AI2050 list of hard problems that AI researchers
must “get right” for socially positive outcomes to result by the year 2050 [270]. It attempts to bridge all the ﬁelds
and factions that concern themselves with AI.
This paper explores each of the ten Hard Problems (HPs). We begin with the recent history of AI in Section 2.
Section 3 expands each HP into a research agenda, identiﬁes signiﬁcant work published in it between 2017
and 2022, and identiﬁes the kinds of research that will be needed in coming decades. A similar exercise was
undertaken in Gil and Selman [203]. Calling these problems “hard” might connote that they are unsolvable:
“wicked problems” [479]. We address this question in Section 4, concluding that there is hope for partial solutions
to suitably sharpened versions of the problems. Section 5 concludes with our outlook for the future. The electronic
appendix provides additional resources for each HP and presents our methodology. Throughout this paper, our
analysis is guided by AI2050’s motivating question: “It’s 2050. AI has turned out to be hugely beneﬁcial to society.
What happened? What are the most important problems we solved and the opportunities and possibilities we
realized to ensure this outcome?” Accordingly, the headline text of each section is subjunctive, conditioned on
our collective success in resolving each problem.
∗Corresponding authors. Contribution statement: Simson Garﬁnkel is the author of the introduction, the discussion of wicked problems and
the conclusion. Simson Garﬁnkel and Gavin Leech jointly participated in the historical section. The analysis of each speciﬁc hard problem is
the work of Gavin Leech, Aleksandr Zhuravlev, Misha Yagudin, and Alexander Briand, with editing by Simson Garﬁnkel.
1AI2050 is a $125 million, ﬁve-year commitment by Eric and Wendy Schmidt to “support exceptional people working on key opportunities
and hard problems that are critical to get right for society to beneﬁt from AI.” [497]
Authors’ addresses: Gavin Leech, g.leech@bristol.ac.uk, University of Bristol and Arb Research, Bristol, ; Simson Garﬁnkel, simsong@
basistech.com, BasisTech, LLC, ; Misha Yagudin; Alexander Briand; Aleksandr Zhuravlev, Arb Research, Prague,


--- Page 2 ---

2
•
Leech et al.
2
Background
“Oh emperor, my wishes are simple. I only wish for this. Give me one grain of rice for the ﬁrst
square of the chessboard, two grains for the next square, four for the next, eight for the next and so
on for all 64 squares, with each square having double the number of grains as the square before.”
— The Rice and Chessboard legend [124]
From the coining of the term “artiﬁcial intelligence” onward [375], progress in AI has been coupled to
improvements in computing power and data storage [504]. For decades apparent progress was slow—or even
invisible to those following other areas of computer science, where progress was in line with the optimistic
predictions of Moore’s Law [394] in the 1990s. It appears, to adopt AI pioneer Ray Kurzweil’s metaphor [315],
that we are now in the “second half of the chessboard,” a period in which the acceleration of AI capabilities has
become impossible to ignore. There is a good chance that many of the speciﬁc claims in this paper about AI
limitations will be invalid within one or two years.
Big improvements in AI rely on scaling up compute [46], including (at the top end) by harnessing tens
of thousands of machines and millions of cores towards the same problem, and using distributed storage to
make proportionally more data accessible at speed. This in turn is dependent on breakthroughs in parallelized
training [406, 258, 442], which make it possible to apply thousands of machines to the single problem of tuning
the billions or trillions of weights in a large-scale neural network.
As these constraints eased, the last decade saw qualitative changes in AI capabilities, with progress on some
of the ﬁeld’s earliest, grandest aspirations [176, 363]. Systems display above-human-level perception on some
tasks [304], as well as some multi-task [460, 79, 428, 472] and multi-modal ability [462, 602, 428].2 This capability is
most impressive (and practically usable) in domains involving image, text, or audio data, as well as discrete spaces
like game-playing, biological codes, and mathematics, in which we see human-level capability or beyond [217,
487, 544, 499, 277, 343]. In an unprecedented turn, these same systems often present users with powerful natural
language user interfaces, with passable performance on arbitrary queries [79, 472]. And, most recently, systems
that exhibit human-like creativity have sparked widespread interest, as in the case of diﬀusion models for
generating high-resolution, high-quality custom images and videos from given arbitrary prompts (see DALL-E,
Stable Diﬀusion, and Phenaki) [467, 484, 574].
Shortfalls & costs
But the grandest promises remain unfulﬁlled. Self-driving cars continue to hover around the
bar of practicality after ten years of testing on public roads [522, 166]. Despite IBM’s claims that its Watson system
would revolutionize healthcare [239], AI for healthcare is only slowly penetrating clinical practice—reﬂecting
“issues with reliability, mixed impacts on workﬂows, poor user-friendliness and lack of adeptness with local
contexts”, as well as “limited data availability, trust and evidence of cost-eﬀectiveness” [105], especially in the low
and middle-income countries where AI would have the greatest impact due to the sometimes drastic shortage of
practitioners. Within AI capabilities, most systems completely lack persistence (saved states and coherent output
across sessions), range (long time horizons and hierarchical plans), and continual learning (retaining relevant
past information while updating to include new information) [571].
Further, the beneﬁts of AI are not equally experienced. In recent years it has been widely reported that AI
systems deployed for applications assessing human beings for credit, employment, and release from prison
seem to replicate pre-existing racial biases and stereotypes [402, 463, 475]. Another example is provided by
commercially deployed object recognition systems, which seem to do a better job of recognizing objects in
wealthy households than those in households at the other end of the economic spectrum [575].
2A multi-task system is one which can solve several unrelated tasks with only minimal further learning ‘in-context’ [225]. A multi-modal
system is one that can solve complex tasks using inputs from several ‘senses’ at once.


--- Page 3 ---

Ten Hard Problems in AI
•
3
Finally, the impressive capabilities of the recent AI revolution have come at signiﬁcant cost: as of writing, global
spending on AI research and development (R&D) is now in the hundreds of billions USD per year3, with the cost
of a single model training run sometimes exceeding $10 million of compute alone [506]. In response, the computer
scientist Christopher Manning quipped “you often use the slogan ‘AI is the new electricity’... discussing this trend
of bigger and bigger models, I’ve been turning it around, and saying that electricity is the new AI” [413]. However,
once the model has been trained (and the upfront cost for the inference infrastructure paid), models have a very
low cost per query [145]—and this combination of large upfront capital requirements and economies of scale
could easily lead to AI being dominated by a small number of well-funded organizations, blocking entrants to
research and markets [14].
These trends, if they continue, could signiﬁcantly limit the beneﬁts of AI in the coming decades.
2.1
Deep Learning Lifoﬀ(2010–2016)
Recent successes in AI are largely due to deep learning (DL), belatedly vindicating the old connectionist research
program [370]. In DL, a neural network learns a hierarchical representation of data from examples—including
so-called “unstructured” high-dimensional examples (such as arrays of pixels, audio waveforms, and text docu-
ments)4 [56].
Neural networks ﬁrst appeared in the 1960s [587]; why did they take ﬁfty years to become dominant?
Inputs: compute and data
The reductive answer (which completely abstracts out the role of research) is simply
that it is computationally expensive to train networks, and the cost of relevant computations decreased by a
factor of trillions over this period [265, 264, 507]. At the same time, the internet dramatically reduced the cost of
both data acquisition and labeling for key tasks like image recognition and machine translation [53].
The computer scientist Sara Hooker notes that an idea’s success in the computational sciences is not just
a function of the idea’s quality, but also of the hardware and software that enable the idea to demonstrate a
practical advantage [249]. This angle explains the decades of no progress in deep learning as “due in large part
to incompatible hardware... The inability to parallelize on CPUs meant matrix multiplies quickly exhausted
memory bandwidth, and it simply wasn’t possible to train deep neural networks with multiple layers.” From
this perspective, DL won a “hardware lottery” in the 2010s after billions of R&D dollars were spent developing
graphical processing units (GPUs), which use matrix multiplications to create realistic 3D graphics. It so happened
that GPUs optimized for consumer entertainment also worked for accelerating neural network training [249].
This is obviously an incomplete explanation: Figure 1 describes many other innovations involved in the
2010–2012 computer vision breakthrough that heralded deep learning [108, 310]. That breakthrough, in turn,
stimulated the circa 2016 inﬂux of researchers and capital that has driven subsequent progress [14]. Even so, the
unprecedentedly low cost of computation and data is certainly a key condition of the present paradigm, since
deep learning is so far one of few methods capable of using data and compute at the “warehouse computing”
scale.
Correcting misconceptions
A series of popular errors among researchers constituted another blocker. Over
the decades, the received view was that multilayer networks were too hard to train [58] because of instability
(vanishing or exploding gradients [416]) or local minima [75, 528, 185]. Additionally, a misapplication of statistical
learning theory suggested that overﬁtting was unavoidable for complex models like large neural networks [56,
603], and the ﬁeld thus trapped itself in a local maximum of low-parameter models (the “underparameterized”
regime) [431, 404]. Sociological factors also held back DL, as with the counter-advocacy of the leading AI scientist
3Consider the $95.99bn of world private investment in AI in 2023, plus $11.7bn of public spending from the US alone [index2024].
4The term “unstructured” is an artefact from when most machine learning was applied to tabular data, while images, sounds, and text could
not be analyzed without signiﬁcant preprocessing. In fact these modalities have rich structure, in the form of dependencies in time, space,
and more. Modern deep learning techniques excel because they identify and exploit such structures. [242, 492].


--- Page 4 ---

4
•
Leech et al.
Marvin Minsky [386]. With his collaborator Seymour Papert, Minsky proved that shallow neural networks lacked
the expressiveness for complex tasks, convincing two generations of researchers to largely avoid them [425].
On one occasion, Minsky asked a presenter “How can an intelligent young man like you waste your time with
something like [neural networks]? ... This is an idea with no future.” [378].
The “Common Task Framework”
[154]. ML research is often structured as a competition to perform a ﬁxed
benchmark task, with “held-out” test data (ideally not seen by competitors) used to objectively test whether
systems generalize beyond the data used to train them. For instance, success on the ImageNet visual classiﬁcation
benchmark was a watershed moment for the popularization of deep neural networks [144, 310]. The degree to
which performance on these simple curated datasets generalizes to real-world data is controversial, but it is now
accepted that neural networks can learn generally useful representations from training on simple tasks (rather
than learning only spurious or highly task-speciﬁc features) [139, 56, 79, 344].
Accumulating training tricks
Much of the progress of the last decade is due to engineering optimizations: training
stabilizers, ad-hoc algorithmic speedups, and dozens of tweaks to architectures. Together with improvements in
the availability of computation and data, these produced a qualitative leap in capabilities thanks to an increased
ability to search the vast model space [415]. Figures 1 and 3 describe some of these tricks; other crucial examples
include skip connections [433], batch normalization [266], better weight initializations [206, 232], gradient
clipping [443], and a plethora of data augmentation methods [195].
Which of these were crucial? A concise enumeration for the ImageNet benchmark is given by Arora and
Zhang [28]; taking the best practices of 2011 as background, they give a complete speciﬁcation for training a 95%
accuracy model—including all hyperparameter values—in just 1032 bits. The minimal innovations were batch
normalization, skip connections, and residual blocks.
Representation learning and end-to-end training
Previous ML systems involved a pre-processing pipeline of mod-
ules which transformed the input data into a form suitable for the ﬁnal predictor. This was most intense in natural
language processing (NLP): before 2018, feature pipelines were elaborate, involving sentence segmentation, word
tokenization, lemmatization, stop word removal, part-of-speech tagging, dependency parsing, and constituency
phrasing [548]. Many of these modules had to be hand-coded [178] or trained independently. In end-to-end
training, conversely, one neural network represents the entire target system on its own, taking raw (or nearly
raw) inputs [205]; gradients are backpropagated from the output end all the way to the input end. Not only does
this save huge amounts of researcher time, counterintuitively it also results in better performance when trained
at suitable scale (with more data and parameters) [227, 542, 280]. This is because “credit” for improvements can be
jointly assigned across layers, and so better representations are learned [56]. This loss of modularity is, however,
yet another obstacle to the interpretability of DL systems’ decisions, contravening as it does a key principle of
good engineering [29, 309].
2.2
The Large Scale Era (2016–Present)
We date this second era in deep learning to 2016, following the quantitative analysis in [504] and the wild
post-2017 success of massively scaled Transformer neural networks [570] and the AlphaGo-MuZero lineage of
deep reinforcement learning (RL) systems [516, 499]. Figure 3 lays out some key factors that led to an exemplar
large scale system, GPT-2 [460], and to emergently multitask systems with passable understanding of language
and a broad range of abilities [582]. (Note that it is not possible to produce an equivalent diagram for more recent
systems: AI development has “gone dark” in the intervening three years, with roughly complete papers replaced
by technical notes which omit even basic information like parameter count [428].) Figure 4 presents heavily
idealized diﬀerences between neural networks in each era.
In retrospect, we can view the Liftoﬀera as a search for a scalable “data sponge” architecture [271, 603] and a
way to make use of unlabeled data, i.e. the vast majority of all data. The search succeeded: the dominant training


--- Page 5 ---

Ten Hard Problems in AI
•
5
scheme for cutting-edge models is now unsupervised (or self-supervised) pre-training followed by supervised
ﬁne-tuning, very often using the Transformer [68, 98, 104]. More importantly, this era established that parameter
count is more crucial for performance than network depth and architecture [284, 61], which again foregrounds
the role of hardware and engineering (in this case, breakthroughs in model parallelism which permit the inclusion
of vastly more parameters).
The Transformer and the pending uniﬁcation of ML
In 2012, ML was divided into research communities which
each worked on one type of input, generally using diﬀerent methods and holding separate conferences. Each input
modality involved diﬀerent tradeoﬀs, diﬀerent domain knowledge for hardcoding inductive bias, and diﬀerent
engineering challenges. Each of these communities focused on computer vision, natural language processing,
speech processing, reinforcement learning, or probabilistic methods, and so on. Deep learning became dominant
in computer vision ﬁrst [310, 233], followed by word embeddings [385], reinforcement learning [392], machine
translation [37], and speech processing [227]. After 2017, the worth of massively scaled neural networks was
realized. Here, “scaled” refers to nets with greatly increased parameter count and the associated increases in
training data size and training compute. The architecture most often scaled is the Transformer [570], but other
architectures can reach performance equivalent to the Transformer’s when equivalent dataset sizes and parameter
counts are used [61]. Massively scaled nets enabled unprecedented progress on the input modalities mentioned
above—and, crucially, on multimodal learning (the use and integration of information from several “senses”
or data types at once, as in image captioning or text-to-speech audio generation) [269]. It is vital to tie these
other domains to language because symbols index conceptual space and thus allow searches to be performed.
Suitably scaled Transformers now achieve state-of-the-art performance in several domains: in order of application,
machine translation [570], language modelling [146], computer vision [156], speech [96, 327], and multimodal
combinations of the above [401, 601, 15, 472]. At the logical extreme of this trend are single pretrained models
serving as “foundation models” for a huge array of downstream tasks and modalities [68].
RL comes of age
Another impressive lineage of systems are trained using deep RL, with unprecedented perfor-
mance and generality (including long-awaited success with model-based RL and real-world deployment) [392,
516, 499, 219, 39, 451, 171, 138, 287].
Outlook
New benchmarks and challenging examples are now often beaten within months [435]. However, this
trend relies on exponential increases in inputs [504] and is thus unlikely to continue for long without greater
algorithmic progress [167]. A weakness of the current paradigm is the use of best-case performance as the dominant
publication criterion, sometimes to the total exclusion of eﬃciency, robustness, and theoretical motivation [297].
Generally, no adjustment is made for the amount of optimization performed across methods [518], which means
that impractical methods can be presented as state-of-the-art simply because one research group spent more.
Similarly, it is normal not to report your method’s sensitivity to random seeds [455].
Further, the practice of iterating on previous hyperparameters and selecting methods based on previous
performance on the same task is common, but represents a subtle kind of data leakage (i.e., a violation of the
assumptions of empirical risk minimization). Combined with overparameterization, this can make conventional
DL unﬁt for tasks where overﬁtting or data shortages are a live concern [198, 351]. (For work focusing on
improving the robustness of ML outputs, see Section 3.2.)
3
The Hard Problems
Here we present each of the AI2050 Hard Problems. For each, we present the results of our literature search,
discuss what makes the problem hard, and examine prospects for future work in the area.


--- Page 6 ---

6
•
Leech et al.
3.1
Hard Problem #1: By 2050, we will have solved the scientific and technological limitations in
current AI that are critical to enabling further breakthrough progress and powerful AI capable of
realizing beneficial and exciting possibilities.
Between 2010 and 2020, artiﬁcial neural networks (ANNs) re-emerged as the dominant tool in AI research, under
the branding “deep learning” (DL) [500]. During that period, the publication rate of papers on ANNs increased
thirty-fold [604]; at the same time, systems of unprecedented capability were trained through a ten order-of-
magnitude increase in computational input (Figure 2). Compared with alternative approaches, the triumph of
DL is that it productively enlists vast computational and data resources, and continues to meaningfully increase
in capability as it scales up. The result is that today’s best AI systems are billion- to trillion-parameter neural
networks trained on terabytes of high-quality data using petaﬂop-days of compute [504, 21]. (See Supplement
2 for a more detailed explanation of the DL boom.) Despite remarkable successes in ML perception and the
emergent capabilities of large language models (LLMs), these systems still lack reliability and persistence, and
remain inscrutable owing to their high dimensionality and distributed representation, the black-box optimization
processes used to train them, and the diﬃculty of reverse-engineering the circuits and algorithms they learn [424,
405].
To realize the potential of AI, the ﬁeld will need to develop approaches that can be applied across datasets,
domains, input modalities (e.g. pixels, text, waveforms, and control signals), and forms of cognition (e.g. raw
sensory processing, language understanding [87], symbolic reasoning, physical movement, content creation, and
the ability to learn and perform a wide range of tasks) [9, 371, 568, 582].
To demonstrate progress in a particular capability, machine learning researchers present an implementation
with unprecedented results on some respected performance benchmark. However, when it comes to recent
LLMs (and other “foundation models” [68]), these demonstrations tend to lower-bound the system’s capabilities,
because emergent capabilities that were not part of the training objective are increasingly being discovered as we
increase parameter counts and improve our “prompting” (i.e., sampling) strategies [582, 74]. Recent examples of
emergent skills include “showing your work” (step-by-step informal logical reasoning) [420, 582], high-quality
text summarization [429], competency in basic physics, the ability to identify irony, and the ability to identify
analogies [581]. (It is sometimes argued that this emergence is a mere artefact of the particular evaluation metrics
used [494], but we note that this does not apply to bilingual evaluation understudy or to high-level “in-context
learning” capability (runtime improvement on a huge range of tasks, given only examples and no further training
steps) [79, 357, 582, 595, 225]. Barak further notes that diﬃcult tasks involve the conjunction of many small
tasks—and attaining all clauses of such conjunctions is binary, so capabilities on complex tasks can be legitimately
emergent [42].) The result is a capability overhang, in which we do not know the limits of today’s large models
because it is infeasible to test them exhaustively [467, 427].
Following publication, it can take researchers years before they can explain how their work contributes to
improved system performance (if their contribution is ever explained). The most commonly used explanations
are ablation (the removal of elements of the system while observing the degree of performance degradation [381])
and retrospective theoretical analysis (in which we prove hopefully-relevant theorems about the method’s time
complexity or its equivalence to an ideal inference framework) [191, 247].
Is deep learning enough?
How much can DL continue to improve through increased computation [552], more
and better data, engineering tricks, and patching in other software tools [69, 383]? Do we need a new paradigm?
In their recent study of AI experts, Cremer identiﬁed ﬁve key disagreements about the limits of ANNs [119]:
Abstraction: “Do ANNs form abstract representations eﬀectively?”
Generalization: “Should ANNs’ ability to generalize inspire optimism about deep learning?”
Causal models: “Is it necessary, possible and feasible to construct compressed, causal, explanatory models of
the environment... using deep learning?”


--- Page 7 ---

Ten Hard Problems in AI
•
7
Emergent planning: “Will suﬃciently complex environments be suﬃcient... to develop... long-term reasoning
and planning?”
Intervention : “Will DL support and require learning by intervening in a real environment?”
To this we might add:
Sample eﬃciency: Will DL be able to learn from just a few examples, similar to the human brain? [311].
These are wide-open scientiﬁc questions. While some researchers predict a negative answer to one or more of
these six capability questions [169], we note that, to date, improvements from large-scale DL have not stopped—and
the rate at which new benchmarks are solved may also be increasing [535].
One tool for predicting the future of machine learning involves black-box “scaling laws” [284, 246]. These
empirical curves are ﬁt by varying the dataset size and number of parameters used to train a large model for a
given compute budget, and they allow us to predict loss over diﬀerent levels of input (dataset size, model size,
and amount of training computation). Remarkably, scaling improvements have so far held over eight orders of
magnitude of training computation [284]. The most recent such law [246] implies that a relative lack of training
data is presently the limiting factor, rather than the engineering challenges of increasingly vast models or scarce
computational resources [573, 358]. It thus seems likely that any future improvements in this paradigm will
result from better algorithms, more data, and better data quality, rather than the brute-force scaling of parameter
counts.
Are AI capabilities a virtuous cycle?
A much-discussed milestone in AI research is the point at which systems
begin to contribute to the design of their successor systems—or, more generally, when AI research improves the
eﬃciency of AI research. Such a recursive process would produce an exponential acceleration in capabilities [211,
70, 223]. The emergence of such a virtuous cycle would require success in one or more of these speciﬁc research
components:
ML optimizing ML inputs To date, ML systems have optimized several key inputs to ML R&D by reducing
datacenter energy costs [171], reducing the cost of acquiring training data [24], and improving semi-
conductor designs, including for AI chips [486, 312, 387]. The image data used to train deep learning
systems has also been expanded using deep learning systems [511], possibly addressing concerns around
long-term data quantity and quality [573].
ML aiding ML researchers Similarly, code suggested by ML models has improved programmers’ eﬃciency,
with 3% of new Google code now being auto-suggested [545], and potentially an even larger share of
GitHub repositories beneﬁting from this [152]. It seems likely that this already feeds into the increasing
eﬃciency of ML research (or at least ML deployment).
ML replacing ML research ML systems taking over tasks which were previously performed by hand is some-
times branded “AutoML” [263]. This includes automatic data cleaning and feature engineering, automatic
and symbolic diﬀerentiation [321], meta-learning of network components (like activation functions [12]
and optimizers [379]), and neural architecture searches [606, 165, 345] in which a neural network designs
better neural networks. In addition, steps have been taken towards automating fundamental discoveries,
as with the discovery of a nominally better algorithm for matrix multiplication [175] (though this speciﬁc
algorithm has a highly limited domain).
Direct self-improvement (i.e. models which improve themselves) The most successful example is “self-
play” (in which a system is pitted against a copy of itself, thus producing inﬁnite training data and a
smoothly increasing need for greater capabilities) [515, 224]. Recent work with unclear practical eﬀect
includes “Algorithm Distillation” (which automatically replaces RL algorithms with notably more sample-
eﬃcient versions [327]); and, most strikingly, language models which ﬁne-tune themselves on their own
output, producing reported improvements in programming and reasoning ability [224, 257]. A notable


--- Page 8 ---

8
•
Leech et al.
example is the Self-Taught Optimizer, which chains language model calls to improve a target program’s
programming ability [600].
The practical signiﬁcance of some of these components has been contested [78, 196, 2], but they stand as early
proofs of concept, while other innovations (like data augmentation and code completion) are already having a
measurable eﬀect on the productivity of researchers and engineers [545, 152].
2024 update
Of the Hard Problems, HP#1 moves so quickly that some update on our January 2023 view is
mandatory. Besides a vast outpouring of consumer products (surpassing $1bn in revenue for the ﬁrst time [162]),
open-source initatives [393], and the landmark multimodal GPT-4 and Gemini releases [428, 197], in 2023 some
progress was made on the scientiﬁc questions covered in this HP section. In our view, the “stochastic parrot
hypothesis” (that LLMs only learn superﬁcial correlations and do not have stable representations of the world, or
any “understanding”) is disconﬁrmed [344, 85]. However, we also have a clearer picture of the degree to which
LLM outputs reﬂect “only” compression or memorization of the model’s training data [141]. Recall that the
training data used to create frontier LLMs are usually not public for competitive reasons [45]. As a result, it is
diﬃcult for external researchers to tell whether a given successful LLM output is more a result of reasoning than
of recall. Let the %-memorisation hypothesis be the claim that some proportion of apparent LLM reasoning is
in fact recall of hidden training data. The strong stochastic parrot hypothesis claims 100%-memorization, but
most tasks appear to instead be 20-60% memorization (in the sense that this is the degree to which performance
degrades on problems constructed to be novel, that the model has not been trained on) [591]. Finally, we should
note that compression of training data does not preclude intelligence [141]. We also have a better understanding
of LLMs’ key “in-context learning’ (emergent, few-shot) ability [582, 225]
Summary
An entire industry and a major academic ﬁeld are focused on solving HP#1 (bound up with its cousin
HP#4). Being upstream of applications, capabilities are the root source of all the value and risk associated with
AI. Researcher incentives already lie in the direction of best-case performance, and the marginal attempt to
accelerate capabilities may have less impact than work on the other Hard Problems, which is less well-funded
and well-staﬀed. Worse yet, as many researchers have noted, increasing capabilities decrease the time available
for society to acclimate to current AI systems and prepare for more advanced systems [513, 382, 380, 559, 364,
557]. These preparations include improving system robustness and human oversight (HP#2), preventing harmful
emergent goals (HP#3) and disparate social impacts (HP#6,7), creating stabilizers for international relations
(HP#8), and putting in place social safety nets (HP#5, 9).
3.2
Hard Problem #2: By 2050, we will have solved AI’s continually evolving safety and security,
robustness, performance and output challenges and other shortcomings that may cause
harm or erode the public trust of AI systems, especially in safety-critical applications and uses
where social stakes and risk are high.
While HP#1 concerns mean or best-case performance, HP#2 concerns worst-case performance: how can we
ensure that AI systems will perform safely, and how can we prove this? ML systems have been implemented in
high-stakes, safety-critical domains such as driving [182], medicine [113], and warfare [298]. Many more systems
have been developed but have remained undeployed or been rolled back as a result of regulatory and safety
reasons [471]. Clearly, unsafe systems can result in loss of life, economic damage, and social unrest [407, 10].
Most concerningly, AI systems may be susceptible to so-called “normal accidents” [63], creating cascading errors
that are diﬃcult to prevent merely by maintaining a nominal “human in the loop” [122].
Most advanced ML models perform far below the reliability level customary in engineering ﬁelds [359]—and
because we do not fully understand how cutting-edge systems achieve their results, we cannot yet detect and
prevent dangerous modes of operation [285].


--- Page 9 ---

Ten Hard Problems in AI
•
9
Key approaches for solving HP#2 include systemic safety, monitoring, robustness and alignment. (See Figure 5
for a conceptual illustration.) We discuss the ﬁrst three here, and alignment in HP#3. In addition, the subﬁeld of
formal veriﬁcation of neural networks has begun to make progress on smaller models. These methods produce a
proof that the system meets a speciﬁcation [529]. If successfully scaled (and if applied to safety properties at a
much higher level of abstraction than the usual input-output functions), these methods could help catch unsafe
systems before deployment.
Systemic safety
Traditional software security methods, including formal methods, could help ensure that AI
systems are run in secure environments and constructed using trustworthy software. However, such approaches
are incomplete and unlikely to be perfected even by 2050. This aligns with a key insight of safety-critical
engineering: safety is a social problem as much as a technical one, because systems are always deployed in a
social context which determines their actual performance. Safety thus requires careful design and vigilance on
the part of developers and users [341].
Some researchers argue that HP#2 can be addressed by simplifying ML systems so that they are more amenable
to veriﬁcation and validation. This assertion relies on results showing that, in some domains, simple models can
match or approximate the performance of more complex systems like neural networks [488, 419, 502].
Monitoring
Public trust in AI systems requires that we be able to observe, interpret, and ultimately understand
AI outputs. Approaches for understanding these incredibly complex systems include mechanistic interpretation
(determining exactly what function a subset of a system is executing); concept-based interpretation (e.g. “this
is the collection of neurons which correspond to ‘forking’ when the system analyzes a chess game”, etc.); and
feature-based interpretation (e.g. “this square is critical to the system’s evaluation of the chessboard”, or “these
pixels are critical to the system’s attempt to determine the number of cats”) [377].
An ideal interpretability tool would directly report the internal representation used by the system in a relatively
faithful low-dimensional form [102, 423, 577], but building a system that is fully interpretable (as advocated by e.g.
Räuker et al.[469]) likely requires building interpretability into the training process (by choosing models legible to
humans) or paring down more complex neural networks (as in model distillation or mechanistic interpretability)
[16, 577].
Robustness
Building a system which performs properly or fails gracefully in all conditions requires us to
recognize and avoid areas where our system will fail. To build such a robust system we might drastically perturb
training dataset with various forms of noise [235]; ensure adequate diversity in the training data; and “red-team”
the AI system with adversarial examples generated by humans or by other AIs [450].
Correct model calibration helps ensure safety. However, while modern algorithms have greatly improved
average performance, they are consistently overconﬁdent compared with ground truth and with simpler models—
even on inputs drawn from the same source as their training data [216, 279]. When inputs are no longer suﬃciently
similar to the training data, the system is said to be “out-of-distribution” (OOD). As systems go further OOD, their
performance degrades. All oﬄine AI systems are somewhat OOD, simply because distribution shift is omnipresent
in real-world contexts: systems are trained on past data and deployed in the present. It is increasingly possible to
automatically detect when new data is OOD, allowing systems to acknowledge this fact and so fail safely [359].
Summary
Any solution to HP#2 will require systematic testing. Realizing the potential of AI will thus depend
on our constructing and using strict and credible tests of real-world ML behavior.
To date, most testing of AI systems has used benchmarks which have been criticized as artiﬁcial and easily
gamed [400, 194, 549, 466]. As the computer scientist Boaz Barak puts it: “The history of artiﬁcial intelligence is one
of underestimating future achievements on speciﬁc benchmarks, but... overestimating the broader implications of
those benchmarks.” [43]. More recently, some researchers have focused on system performance “in the wild” (e.g.,
driving through city streets) and through “adversarial testing” by human and ML critics [194, 292]. Meanwhile,


--- Page 10 ---

10
•
Leech et al.
third-party AI testing is emerging as an attempt to check that AI systems do not engage in dangerous actions
(like deception or self-replication) [17] or discrimination against legally protected groups [288].
3.3
Hard Problem #3: By 2050, we will have solved the challenge of safety and control, alignment,
and compatibility with increasingly powerful and capable AI systems and eventually those of
artificial general intelligences (AGI).
How do we ensure AI acts according to our values? Equivalently, how do we prevent poorly-understood AI
systems from advancing goals we do not endorse? Whereas HP#2 concerns the prevention of harm caused by
incompetent systems, HP#3 seeks to align competent AIs with humans, through methods which ensure their
behavior is compatible with the user’s intentions.
Of course, HP#3 is complicated by the lack of agreement among humans about values. Diﬀerent cultures have
diﬀerent approaches to risk tolerance and diﬀerent deﬁnitions of harm, and so diﬀerent regulatory environments
have diﬀerent legal standards for how automated systems should perform when they, for example, encounter
OOD inputs [359]. One goal which is robust to normative variety is intent alignment: producing a system which is
at least trying to do what the user intends it to do [188, 340]. Figure 6 shows one decomposition of the alignment
problem.
Figure 7 depicts the “greater alignment problem” of economic and strategic barriers to the successful use of
alignment methods once we have established them. This can be viewed as a central problem of AI governance:
see HP#9.
For an updated (2024) view of approaches to the alignment problem, see our informal review [332].
Problem: Speciﬁcation gaming
When the US adopted standardized testing to determine the quality of public
schools, educators predictably responded by “teaching to the test”: under-emphasizing any part of the curriculum
that was not included in the exam [273]. Likewise, when the UK National Health Service adopted a stringent
target that all emergency patients would be seen within four hours of entering hospital, the result was columns
of ambulances idling outside hospitals for hours to prevent the target timer starting [62]. These cases can be
described as cheating, because the metric is being optimized at the expense of the underlying purpose.
Similarly, AI systems game speciﬁcations [305]. For example, in 2017 an OpenAI robot trained to grasp a ball
via human feedback from a ﬁxed viewpoint learned that it was easier to pretend to grasp the ball by placing its
hand between the camera and the target object, as this was easier to learn than actually grasping the ball [103].
Researchers may respond to speciﬁcation gaming by adding detail to the speciﬁcation of the desired task (in
the form of a more complicated objective function, or more labeled instances, demonstrations, or advice) [255].
However, it is diﬃcult to specify all the relevant desiderata and conditions, even when using a learned implicit
model of human preferences [22, 491]. Optimized against an incomplete speciﬁcation, a system will ﬁnd loopholes
and may instead perform a spuriously correlated task [549]. Such behavior can be called speciﬁcation gaming or
reward hacking [440, 519, 112], and has now been observed in many AI systems [305, 549].
A natural response is to simply add variables to the speciﬁcation when it is revealed that they are needed—an
interminable process, owing to the sheer number and context-sensitivity of human preferences and the diﬃculty
of specifying them formally [491, 22]. As Russell argues, “It is... perhaps impossible, for mere humans to anticipate
and rule out in advance all the disastrous ways the machine could choose to achieve a speciﬁed objective.” [490]
So one part of a solution to HP#3 is to detect ﬂawed speciﬁcations and cheating, and to ﬁnd ways to specify
robust objectives [260].
Problem: Emergent goals
As well as optimizing a subtly wrong goal, systems can develop harmful instrumental
goals in the service of a given goal—without these emergent goals being speciﬁed in any way [434, 218, 339,
17]. For instance, a theorem in reinforcement learning suggests that optimal and near-optimal policies will seek


--- Page 11 ---

Ten Hard Problems in AI
•
11
power over their environment under fairly general conditions [560]. This power-seeking behavior is plausibly
the worst of these emergent goals [92], and may be an attractor state for highly capable systems, since most
goals can be furthered through gaining resources, self-preservation, preventing goal modiﬁcation, and blocking
adversaries [426, 449]. Presently, power-seeking is not common, because most systems are unable to plan and
understand how actions aﬀect their power in the long term [414].
A further risk is presented by systems that deceive us about their alignment. Current systems can learn to
deceive: for instance, the Cicero system plays a version of the game Diplomacy at human level, employing persua-
sion, deception and betrayal despite being trained for honesty [40]. Perhaps the greatest risk involves deceptive
alignment [91], in which a system learns to detect human monitoring and hides its undesirable properties—simply
because any display of these properties is penalized by the feedback process, while that same feedback is usually
imperfect. (Consider the problem of verifying a translation into a language you do not speak, or of checking a
mathematical proof that is thousands of pages long.) [92, 259]. Rudimentary examples of deceptive alignment
have been observed in current systems [322, 333].
Approaches For a review of current research agendas in AI alignment and control, see our informal work [332].
Currently, the dominant approach to HP#3 involves iterated human feedback: humans reward systems that
output good behavior, and penalize unwanted behavior by making signiﬁcant modiﬁcations to the system. (In
practice this process requires so much feedback that it must be automated by using a proxy model of human
preferences [103, 436, 204, 38, 338].) Again, this feedback method selects for systems that appear safe during
training, and thus leaves open the possibility of unsafe systems which merely appear safe. In particular, if a
system exceeds some threshold of planning ability, seemingly innocuous feedback might simultaneously penalize
misbehavior and incentivize deception [5]. The system could thus pass behavior tests, but still deviate whenever
it could do so without being detected. A naive response is to simply severely penalize even mild forms of such
behavior—but this only delays the problem, since such penalties greatly increase the selection pressure towards
opaque and patient deception [70, 115]. The response also fails to apply to tasks where human scoring of results
is imperfect or impractical (as with any long-range task with slow feedback loops or messy causal inference).
The leader of the alignment team at OpenAI, Jan Leike, has proposed that parts of the alignment problem
be delegated to ML systems, particularly the generation of ideas and the design of scalable systems [335, 334].
Similarly, Christiano has proposed an AI interpreter for AI systems [102]: an advanced, adversarial form of
dimensionality reduction which discovers the target system’s high-level representations. If achieved, this Eliciting
Latent Knowledge (ELK) system could help detect and train out misalignment. Perez et al. use language models to
judge the output of other language models, speeding up the process by more than an order of magnitude [449].
Summary: AI assurance, AI ethics, and AI alignment
Researchers working on the diﬀerent risks posed by AI
overlap in personnel, methods, and goals [267, 121, 238]. Alignment research thus overlaps with assurance (HP#2)
and responsible AI (HP#7): each involves mitigating risks to hard-to-model, high-level features of the human
environment. In particular, the alignment problem can be viewed as a kind of robustness problem: we need to
ensure that systems robustly generalize about the goals we are training them to fulﬁll [323, 238].
Despite this, there is some debate over the proper horizon with regard to harms: should we focus on current
systems and current risks, or look ahead to future risks? [331] This is a false dichotomy: AI risk is better viewed
as a continuum, both ends of which are worthy of concern [458, 94, 538, 48, 189]. Consciousness of one risk does
not appear to trade oﬀagainst consciousness of other risks [214]. Aligning current systems against current and
foreseeable harms plausibly provides us with the best feedback we will get for aligning stronger systems [114, 31,
540].


--- Page 12 ---

12
•
Leech et al.
3.4
Hard Problem #4: By 2050, there will have been game-changing contributions by AI to
humanity’s greatest challenges and opportunities, including in health and life sciences,
climate, foundational science (including the social sciences) and mathematics.
Researchers across disciplines and industries are applying AI to their hardest data analysis and discovery
problems. Many of these, like improvements in energy and healthcare, are crucial for the future of humanity.
These applications include fundamental discoveries, building AI into beneﬁcial applications, and using AI to
accelerate the pace of R&D and technology transfer. Already, automatic diﬀerentiation tools have reduced
mathematical drudgery in science, technology, engineering and mathematics (STEM) ﬁelds, including ML [153,
50]. Some applications are overlooked because they succeed to the point of becoming routine background:
consider “prediction machines” [13] like spam ﬁlters [531], recommender systems [457], the turn to ML pricing
across industries [65, 584], or the ubiquity of serviceable machine translation (including real-time translation
from images and speech) [445]. This section brieﬂy explores progress in select areas; see [464, 133, 49, 474, 26,
136, 325] for more.
Scientiﬁc discovery
ML has led to remarkable scientiﬁc breakthroughs in recent years, including the AlphaFold
system increasing the number of predicted protein structures by two orders of magnitude [230]. One worry is
that these systems give us answers but do not increase our understanding; but Krenn et al. sketch ways in which
systems could aid us in this too [308]. One example of ML assisting discovery is models substituting for exact
simulations, as in Figure 8: exact simulation of quantum systems is incredibly computationally expensive, but
can generate perfectly labeled training data to train machine learning proxies, which can then support much
larger searches and larger quantum systems [256, 307, 530].
Energy & climate
AI applications in clean energy have garnered signiﬁcant attention and investment. Rolnick
et al. list many such applications [483]: optimizing electricity grids, enhancing transportation eﬃciency, reﬁning
energy usage in heating and construction, streamlining industrial supply chains, carbon removal techniques, and
improving climate models. AI has also contributed to fusion research [262, 138]. The interdisciplinary organization
Climate Change AI was founded to focus on this strand of applications [111].
Chemical and materials research
A fundamental challenge in the design of new catalysts, batteries and advanced
materials is the modeling of complex quantum wave equations that might involve hundreds of atoms and
thousands of electrons. Recent ML systems can perform elements of quantum simulation [256] previously thought
to be solely the domain of much-anticipated quantum computers [597, 408]. Meanwhile, quantum computers
may come to depend upon machine learning for error correction [306, 569].
Software development and algorithm design
Language models optimized to output source code [224, 97] are
reportedly now writing 3% of all new code at Google [545], and perhaps an even larger fraction of Github
repositories [152]. Currently, humans remain in the loop, reviewing code completions and ﬁxing the (common)
bugs. Language models continue to show remarkable improvements in programming ability, achieved for instance
by bootstrapping with a compiler or an interpreter as a training signal [224]. The Codex model (a heavily ﬁne-
tuned GPT-3) generated bug-free code 29% of the time on a small benchmark of basic problems, while a baseline
GPT-3 passed 0% of these problems [97]; the AlphaCode system solves diﬃcult competitive programming tasks at
median human level [599]. More interesting still is early work on algorithm design, for instance the use of deep
RL to discover a novel eﬃcient algorithm for matrix multiplication (though over a very limited domain) [174].
Healthcare
High variance in ML performance remains a serious obstacle for high-stakes applications like
healthcare. In 2016, the deep learning pioneer Geoﬀrey Hinton famously claimed that “we should stop train-
ing radiologists. It’s just completely obvious that within ﬁve years, deep learning is going to do better than
radiologists” [20]. The evidence suggests that this prediction was overstated rather than outright false.


--- Page 13 ---

Ten Hard Problems in AI
•
13
As of 2022, around 40% of European radiologists are using AI tools [51]. This is far short of the full automation
implied by Hinton, and does not strictly imply that the tools are clinically useful—but this is still remarkable
penetration in only six years. We found little data on the promised cost savings of ML healthcare; one study found
a 10-19% cost reduction for one procedure [395]. Similarly, the ﬁrst drugs suggested by AI systems predicting
clinical relevance from chemical structure are now entering human trials; there is a good chance this trend will
revolutionize drug discovery [95, 282, 352].
Despite these encouraging signs, uptake remains slow. How can this be explained? One concerning review
shows that bad methodology is rampant in healthcare ML: only 12.5% of diagnostic and prognostic studies
included a test set, and only 10% performed any calibration analysis [23]. Of 232 Covid diagnosis models selected
for relative high quality by Wynants et al [592], all had a “high or unclear" risk of bias, and only two passed
basic performance tests. Roberts et al [482] similarly ﬁnd that “none of the [62 imaging] models identiﬁed are of
potential clinical use due to methodological ﬂaws and/or underlying biases”. These problems are found in other
domains [347, 439], and likely explain a large part of the deployment gap.
Summary
The pattern is that ﬁelds with large amounts of data, strong theory, and relatively stationary distribu-
tions beneﬁt most from ML, just as they beneﬁt most from mathematization and statistical modelling. Similarly,
the AI products which are currently generating revenue are mostly in areas with imprecise speciﬁcations and a
low cost of error—consider art, copywriting, customer service, code completion with a human in the loop, and
conversation bots [554, 432, 593, 545]. The low reliability of most ML methods is a general obstacle to deployment
(see HP#2).
Further, in many of the above cases we have approximately no mechanistic understanding of how our successful
systems succeed [577]. This is an uncomfortable situation for scientists, or anyone concerned with insight, control,
and accountability. Looking ahead, we need applications that actually improve society. This will require progress
on assurance (3.2), alignment (3.3), and responsible AI (3.7). (See Section 3.7 for possible ML applications for
advancing the ‘social good’: e.g. AI countermeasures against poverty, pollution, and human traﬃcking [356].)
3.5
Hard Problem #5: By 2050, we will have met the economic challenges and opportunities
resulting from AI and its related technologies.
Are the robots and generative AIs coming for our jobs—or will AI create new economic opportunities for humans
that we cannot yet imagine? History is an imperfect guide here, given the apparently fundamental diﬀerence
between AI’s impacts in the past and its likely impact over the next 25 years.
At the onset of the Great Depression, John Maynard Keynes famously claimed that, in the long run, humanity’s
major challenge would be deciding what to do with our leisure time—since by 2000 we would work no more
than 15 hours a week; “Thus for the ﬁrst time since his creation man will be faced with his real, his permanent
problem—how to use his freedom from pressing economic cares, how to occupy the leisure, which science and
compound interest will have won for him, to live wisely and agreeably and well.” [290]
Keynes did not foresee AI completing the centuries-long project of labor automation: he simply had faith in
the power of compound interest and steadily increasing levels of productivity.5
The dissenting view was articulated by a US national commission in 1966: “The basic fact is that technology
eliminates jobs, not work” [73]. This belief is often proclaimed by those in favor of automation, as opposed to
those who stand to lose their current jobs. It also assumes a balance between the rate of job creation and job
destruction—a balance that AI may disrupt, as Brynjolfsson and McAfee forecast:
5Keynes also assumed “no important wars and no important increases in population” would detract from the power of compound interest,
and did not account for steadily increasing expectations on the part of consumers. Thus, today we ﬁnd ourselves in a rich but labor-intensive
world: since Keynes was writing, working hours have fallen about 25% rather than the 80% he predicted [202].


--- Page 14 ---

14
•
Leech et al.
Rapid and accelerating digitization is likely to bring economic rather than environmental disrup-
tion, stemming from the fact that as computers get more powerful, companies have less need for
some kinds of workers. Technological progress is going to leave behind some people, perhaps
even a lot of people, as it races ahead. As we’ll demonstrate, there’s never been a better time to
be a worker with special skills or the right education, because these people can use technology
to create and capture value. However, there’s never been a worse time to be a worker with only
‘ordinary’ skills and abilities to oﬀer, because computers, robots, and other digital technologies
are acquiring these skills and abilities at an extraordinary rate. [83]
One famous estimate of automation risk by industry [186] illustrates the diﬃculty of forecasting such risks:
creative professions like “visual artist” were only included in the paper’s appendix, and were given a mere 4%
risk of automation—but today, after a decade of generative AI development, commercial art has turned out to be
at much higher risk. OpenAI researchers project that 80% of the US workforce might ﬁnd 10% of their work tasks
“aﬀected” by OpenAI’s GPT-4 system, and 19% of the workforce may see “at least 50% of their tasks impacted”
[164].
We break this “hard problem” into three: (1) predicting the impact of AI on economic growth; (2) predicting its
impact on the labor market and inequality; (3) possible policies to maximize beneﬁcial outcomes.
Predicting AI’s impact on economic growth
Despite continuing technological progress the key measure of
economic growth, ‘total factor productivity’ growth, has been slowly declining in the developed world for
50 years, down to 1.0% per year in 2016, compared with 1.5% in the 1970s [118]. This reduced acceleration
in developed economies is known as the productivity paradox or Solow paradox. In 1987 Solow himself wrote
that “You can see the computer age everywhere but in the productivity statistics” [526]. Three decades later,
Brynjolfsson, Rock, and Syverson noted that the paradox still held, attributing it to the lagging diﬀusion of AI
technology. Other technologies (e.g. electriﬁcation, semiconductors) averaged 25 years of slow growth before
having profound impacts on productivity, and we might expect AI to follow a similar pattern [84].
There is no consensus about how AI eﬀects should be incorporated into growth theory. One paper ﬁnds
25 distinct modeling choices in the literature [556]. Most models formalize AI as a capital-augmenting factor
[6]—but some models include it as a labor-augmenting factor [60] or a replacement for highly-skilled labor that
simultaneously generates innovation [11]. Starting afresh, Trammell and Korinek [556] examine four ways in
which AI could transform economic growth:
(1) “a decrease to the growth rate, even perhaps rendering it negative”;
(2) “a permanent increase to the growth rate, as the Industrial Revolution increased the global growth rate
from near zero to something over two percent per year”;
(3) “a continuous acceleration in growth, with the growth rate growing unboundedly as time tends to inﬁnity”;
(4) “an acceleration in the growth rate rapid enough to produce inﬁnite output in ﬁnite time.”
The last scenario is physically impossible, of course, but the relevant question is whether the AI transition is
better modeled using this drastic functional form rather than brief periods. According to Trammell and Korinek,
there are no compelling theoretical reasons to dismiss such scenarios [556]; in principle, advances in robotics and
AI allow for super-exponential growth [493].
How will AI aﬀect labor?
Following long-held concerns about automation, the most common AI-related topic
among policymakers and the public regards AI’s threat to jobs. The current evidence is ﬂawed: most empirical
studies of AI-induced unemployment use a deﬁnition of AI (as mundane automation) that covers only a subset of
the potential eﬀects of AI on the labor market. One widely cited paper claims that “up to 35% of all workers in
the United Kingdom, and 47% in the United States, are at risk of being displaced by technology over the next
20 years” [186]. This could result in substantial employment displacement, exacerbating income and wealth


--- Page 15 ---

Ten Hard Problems in AI
•
15
inequalities [303] in the absence of corresponding social programs. The ﬁrst empirical studies on the eﬀects
of LLMs on industries have begun to emerge, showing notable increases in productivity among e.g. median
customer support workers [82]—and also associating wage decreases with automation in general [7].
Acemoglu and Restrepo note four factors that may instead contribute to a positive eﬀect on employment:
(1) The productivity eﬀect, whereby cost savings from automation reduce prices and so increase consumer
demand (in the sector experiencing automation or in other sectors). This could increase the demand for
labor to perform the remaining non-automated tasks.
(2) The capital accumulation eﬀect, whereby automation increases the capital intensity of production, trigger-
ing accumulation of capital, which also raises the demand for labor (in tasks where AI is complementary
to human labor);
(3) The deepening of automation, whereby technological improvements increase the productivity of existing
machines with no additional displacement of labor, boosting the productivity eﬀect and further increasing
the demand for labor; and
(4) New labor-intensive tasks made economically feasible by AI assistance, which could increase the labor
share of income (an eﬀect which could potentially persist in the longer term), which would also counteract
the impact of automation.[8]
Possible interventions
Realization of the beneﬁts of AI requires the mitigation of any negative economic impacts.
It is increasingly plausible that this mitigation will itself involve the use of AI [301].
Economists were early adopters of machine learning methods, with some notable improvements to empirical
methods [64]. One simple example is the Bank of Italy’s use of natural language processing to track inﬂation
expectations by analyzing millions of Twitter feeds [25]; the results are reportedly more accurate than other
sources.
As with other areas, reliability is a serious obstacle. For example, the Polish Ministry of Labor used AI to
automate its unemployment beneﬁt process, assigning individuals to categories (e.g. job placements, vocational
training, apprenticeships, allowances); however, the system had to be dismantled following widespread reports
of inaccuracy [317]. Similarly, well-cited work using Twitter to predict the stock market [67] failed to pan out:
“the hedge fund set up in late 2010 to implement the Twitter mood strategy, Derwent Capital Markets, failed and
closed in early 2012” [319].
AI systems like the experimental “AI Economist,” a multiagent RL system able to set taxation policy in a
simulated economy [605], could help make policy decisions. This particular simulation has not been used in real
policymaking, but successor methods could help vet decisions.
If it becomes necessary to mitigate the downsides of AI through policy, what will we do? Radical changes such
as universal basic income could result in net welfare gains, but uncertainty remains worryingly high [229, 583].
Governments might contrive incentives for companies to hire people (and for workers to get hired) [302]. This
might also help us retain the considerable noneconomic beneﬁts of meaningful work, such as dignity and social
cohesion.
It is important to emphasize the unpredictability of AI capabilities, and therefore of the labor market shocks
associated with them [582]. None of the classic studies of AI automation foresaw 2022’s nascent automation of
commercial visual art [485]—even though the breakthrough followed one study (Nedelkoska and Quintini) by
less than four years [410]. We can say with some conﬁdence that capabilities will increase, that these increases
are likely to be sudden and unexpected, and that few social institutions will be prepared for their eﬀects.


--- Page 16 ---

16
•
Leech et al.
3.6
Hard Problem #6: By 2050, we will have met the challenge of democratizing access,
participation, and agency in the development of AI across countries, organizations, and
segments of society, especially those not presently involved in the development of AI.
Our next problem is the fact that the current AI workforce does not evenly represent world demographics. Men
from the US and China, working in the US, for US corporations, are disproportionately highly represented [402,
157, 170, 534]. Realizing the full promise of AI requires that people throughout the world and from all social
strata are able to use AI and participate in its design and governance. Solving this problem requires addressing
unequal access to AI both within countries and across countries.
3.6.1
Within-country issues: domestic inequality
Demographic diversity of researchers
The AI research establishment inherits patterns of under-representation
that are dominant in most technical ﬁelds. In North America, large parts of professional AI research require
a Ph.D., yet less than 25% of Ph.D. computer scientists are women, and fewer than 2% are Black or African
American [608]. This holds globally and outside the research community: LinkedIn data suggests that only 22%
of AI professionals are women [161]. Since the vast majority of AI practitioners work for private companies,
limited corporate statistics on gender and racial diversity hinder a full understanding of the situation [402], but
those few statistics that exist are not encouraging: only 5% of Google and 7% of Microsoft employees are Black or
African American, with potentially even lower representation at the more senior levels [212, 384].
A report by the European Institute for Gender Equality cites several reasons for gender discrimination in the
speciﬁc ﬁeld of AI, examining barriers to women’s entry to the ﬁeld through education (e.g. gender stereotypes
and educational choices) and the workplace (e.g. sexual harassment, male-dominated teams, and lack of access to
funding) [170].
We should not assume that improving the representation of under-represented groups in the ﬁeld will neces-
sarily improve the ﬁnal product for those groups; some authors warn against “participation washing,” in which
nominal participation provides legitimacy to a project regardless of the actual outcome [521, 520].
Privatization of AI
Over the past two decades, there has been a net migration of AI researchers from academia to
industry [278]: a study of North American publications found that the researchers behind 19% of all AI citations
moved to industry between 2000 and 2018 [210]. Similarly, Ganguli et al. found that the share of ‘large-scale’
AI systems run for academic purposes fell from approximately 70% in 2000 to approximately 15% in 2020 [192].
This trend is likely to be self-reinforcing, as private incentives for non-cooperation and the keeping of trade
secrets, combined with the associated centralization of decisions and beneﬁts, will likely make AI research more
expensive and less rewarding for those who remain in academia [278].
Researchers in deep learning and those with greater research impact are more likely to migrate to industry,
raising concerns about the “privatization of AI knowledge” [278]. Speciﬁcally, if the most sophisticated AI
approaches become proprietary and are used only within private research labs, then it will be impossible for
universities to teach them, let alone contribute to leading research.
One reason for this shift is the intense capital requirements involved in staying at the frontier of research in
the “large scale era” of deep learning (see Section 2). For example, the pretraining cost for Google’s 2020 T5 model
reached $10 million in compute costs alone [506]; we do not know how much more was spent on data annotation,
software engineering, and other factors. If AI increases returns on capital, then it will tend to concentrate power
in fewer hands [283, 35].
Even for those who remain in academia, the inﬂuence of private funding is signiﬁcant. 58% of AI ethicists
at four leading US universities have received ﬁnancial support from major tech ﬁrms [4]. Some researchers
claim that this helps tech companies disproportionately inﬂuence discourse, including decisions about which
technologies get developed and adopted [222, 297].


--- Page 17 ---

Ten Hard Problems in AI
•
17
The hybrid nonproﬁt/corporation OpenAI has released an API which allows those without giant compute
clusters to use the ﬂagship GPT-4 language model [430], and this currently serves as the de facto baseline in
large parts of natural language processing research. However, the API provides no details on the training setup
or speciﬁc model version exposed each time it is used (beyond crude top-level versions like ‘davinci-001’ vs
‘davinci-002’), and these frequently change silently, rendering the original research papers non-replicable [336].
This precludes a scientiﬁc approach to our experiments, since we do not know the exact conditions of our baseline,
cannot reproduce past results, and so cannot resolve disagreements about capabilities.
Against this trend, support for AI access comes from unexpected places. A 2020 report from the US National
Security Commission on Artiﬁcial Intelligence (NSCAI) recommended the creation of public infrastructure to
democratize AI research [496]. Picked up in the subsequent US defense budget, this led to recommendation of
the creation of a National Artiﬁcial Intelligence Research Resource (NAIRR), a public cluster with the goal of
“spurring innovation, increasing the diversity of talent, improving capacity, and advancing trustworthy AI.” [441]
Public participation
Fixing AI workforce demographics helps promote AI access, but is not suﬃcient. Most people
are not AI developers, and even research teams that are balanced by gender, race and other demographic factors
create technologies that do not promote equal access and beneﬁcial use. “Participatory technology assessments”
provide a more structured approach to keeping developers aligned with the goal of equitable access as well as the
impacts of AI on aﬀected groups; such participatory frameworks have been used in ﬁelds such as climate change
futures [248], and have even been trialed for highly technical projects [120, 446]. “Citizen Assemblies,” in which
non-experts are randomly selected and given suﬃcient background information to make substantive decisions
about technical issues, have also been proposed as a way to broaden the governance of AI [181]. However, use of
these frameworks is still in its infancy in AI.
3.6.2
Between-country issues: global inequality There is an even greater divide between the countries currently
leading in AI and those falling behind. While AI is widely considered a national priority, with almost 40% of
countries having created an AI strategy [437], the implementation of these strategies depends on scarce resources,
including trained STEM talent and computing power. These resources are predictably concentrated: 59% of
leading AI researchers currently work in the US, and another 20% in China and Europe [372]. Figure 9 shows
post-college migration among AI researchers who have published at one top conference, as of 2019.
A 2021 survey by the US National Science Foundation found that of the 1334 students graduating from a US
institution with a Ph.D. in computer and information science, only 124 (9%) had plans to leave the country [289];
that same year, the Taulbee Survey found that 69% of computer science PhDs were awarded to graduates in the
“Nonresident Alien” category [608].
Structured access
Open-sourcing ML tools and model weights is a powerful way to allow less wealthy users to
catch up. However, this laudable aim sometimes conﬂicts with other aspects of responsible AI. Generative AI
systems can assemble dossiers on individuals based on leaked personal information, and can produce limitless
amounts of customized hate speech; so too can image generation systems produce synthetic revenge porn or
instructions for the manufacture of weapons, among other harmful material [532]. Some organizations publishing
these models have attempted to limit such uses [79, 477, 525], but other systems (such as the independent
“GPT-4chan,” which was trained on a notably bigoted internet corpus and then open-sourced [314]), intentionally
have no such limitations.
Hosting generative systems and allowing access via a web browser or other API allows users without consider-
able computational resources to use cutting-edge models, and allows nontechnical people to access the models
from any client device [525]. This use of APIs also allows generated material to be examined for dangerous
or undesirable content (e.g. bomb-making instructions) and for such content to be blocked. This “structured


--- Page 18 ---

18
•
Leech et al.
access” model allows controls to be revised after problems come to light [508]. However, such access can also be
terminated for less benign reasons, such as censorship or political sanctions.
3.7
Hard Problem #7: By 2050, we will have solved the challenges and complexities of responsible
research, deployment, and sociotechnical embedding of AI into diﬀerent societies and
subcultures, accounting for diﬀerent cultures, participants, stakes, risks, societal externalities,
and market and other forces.
Many academics, community activists, artists, creative professionals and philosophers have raised ethical and
social concerns regarding advanced AI systems.6 These concerns include the unauthorized use of protected
intellectual property as training data; poor working conditions for human annotators; the tendency of AI systems
to exhibit racial or gender biases [402]; their ability to generate misinformation [143]; and their growing use for
social control in authoritarian states [123]. Improvements in AI capabilities are likely to further exacerbate these
concerns and create new ones [585, 366].
3.7.1
Negative Impacts of AI Use A major role of the current AI ethics movement is to draw attention to
overlooked side-eﬀects, costs, and harms of building and deploying AI systems, particularly as they befall existing
marginalized groups:
• Under-recognized work. Without training data, ML cannot take place. Much of this data comes from paid
clickwork (also called “platform work” [170] or “microwork” [558]), unpaid crowdsourcing, and unpaid
user behavior capture. Clickworkers, mainly in the global south, perform repetitive data-labeling tasks
for use in the training of ML models [558]. The market value of such annotations “is projected to reach
$13.7 billion by 2030” [228] and the annotation industry is widely reported to have little concern for
workers’ rights. Besides welfare and rights, the invisibility of this contribution arguably contributes to a
misunderstanding of AI capabilities.7
• Environmental cost. Large-scale DL systems can produce signiﬁcant carbon emissions as a result of the
computational demands of training runs and inference [539]. While AI has the potential to improve
energy eﬃciency and progress on sustainable energy [116], estimating the trade-oﬀbetween these two
factors is complex and requires life-cycle estimations of carbon emissions, which have only recently
been attempted [362]. Previous estimates focused on emissions from training systems [151, 41]; recent
work has found that the majority of emissions may in fact be due to inference (the actual use of AI
systems) [448]. Estimates are limited by the lack of transparency around the utilization of datacenters and
hardware, and the diﬃculty of retroactively sourcing such data [447]—for instance, in at least one case
external estimates of training emissions were oﬀby two orders of magnitude [539, 447]. Additionally, the
projection of current carbon emissions into the future is unreliable without an ability to model eﬃciency
improvements in AI architectures, algorithms, accelerators, and datacenter usage, as exempliﬁed by the
747-fold reduction in carbon emissions between the Transformer and Primer training setups [448]. Calls
have been made for research papers to explicitly include measurements of carbon emissions [447], and to
treat energy eﬃciency as a core component of competition benchmarks and conference awards [448, 391].
• Discrimination, toxicity, and bias. AI models and the tools that use them may exacerbate unequal access to
employment and services. AI-generated content can promote inequality and harmful stereotypes.
While proponents of AI systems argue that ML has the potential to remove racist biases in hiring or
lending, critics claim that, in practice, these systems contain biases that require special attention from
6This section omits the question of whether suﬃciently advanced AI systems ought to be treated as moral actors. For full-length treatments
of these questions, see [213, 215, 512].
7Note that this is only the most distinctive form of labor in AI; as a high-tech industry, AI also relies on the often hazardous work involved in
procuring raw materials and manufacturing components [286].


--- Page 19 ---

Ten Hard Problems in AI
•
19
their human users [299]. For example, one system used to catch welfare fraud in Michigan had a 93% false
discovery rate (almost all accusations of fraud were found to be mistakes, on review) [1]. The negative
impacts of mistakes can be mitigated if negative decisions can be easily identiﬁed, appealed and rapidly
reviewed; in practice such appeals are frequently impossible, such as when a classiﬁer decides against
showing a submitted resume to a hiring manager. Although there is broad consensus that preexisting
bias in datasets is a signiﬁcant source of undesirable behavior, there is heated disagreement about other
sources of bias in machine learning, which could include sensors [342]; feature selection; and even biases
rooted in gendered human language [374].
• Privacy. Figure 10 shows a strong consensus in favor of respecting privacy. The qualiﬁed success of
data protection laws such as the General Data Protection Regulation (GDPR) [199] and the California
Consumer Privacy Act (CCPA) [88] has made privacy one of the areas of responsible AI subject to
enforceable legislation [389]. Similarly, a growing body of research addresses privacy concerns [510, 396,
346]. Methods such as federated learning [300] and diﬀerential privacy [3] promise to allow ML training
that incorporates tunable privacy protections with respect to training data extraction, but may not provide
for protection of facts that are in the public domain but are scattered, such as those that may be included
in dossiers created using large language models. OpenAI’s GPT-3 was designed to be diﬃcult to extract
personal information from, including for example public ﬁgures’ dates of birth. Even so, malicious uses
of AI continue to encroach on privacy, as exempliﬁed by China’s “Sharp Eye” automated surveillance
system [551] and automated cyberattacks on personal data [354]. A more drastic form of AI-enabled
surveillance could be on the way in the form of nonsurgical decoding of thoughts [54]—a technique which
is reportedly already used by some police forces [398].
• Security There is growing concern that AI-based systems can discover and exploit vulnerabilities in
software or cyberinfrastructure [354].
3.7.2
Principles for Responsible AI Major institutions like governments and international organizations have
responded to ethical problems with AI with a ﬂurry of principles and guidelines: one review found 84 such
documents, mostly published since 2016 [274]. Figure 10 summarizes the themes of these guidelines and identiﬁes
common and neglected themes.
Our analysis ﬁnds that few of these documents cover HP#3 or HP#10, express caution about dangerous
capabilities or weaponization, present a technical research agenda to put principles into practice, or pay attention
to future AI systems. Industry principles explicitly stress the beneﬁts of AI capabilities. Google and DeepMind
explicitly disavow working on AI-enabled weapons and surveillance systems, but most other documents omit
the issue or stop short of prohibition. Principles written by industry entirely omit HP#5 (the future shock to the
labor market), HP#9 (regulating AI systems), and environmental sustainability. Subjects underemphasized by
governments include HP#8, speciﬁcally the impact on geopolitics, international cooperation, and approaches for
avoiding racial conﬂict.
Statements of principle naturally lack detail about speciﬁc problematic technical features of AI systems—but
they also lack speciﬁc mechanisms for ensuring that their principles are respected [220, 537, 598]. As Figure 10
shows, statements of principle are usually orphaned, with no clearly associated technical agenda or policy
proposal to move them towards implementation and impact. Documents generated in industry and government
are an exception. In common with [220, 390], we ﬁnd that these documents systematically overlook certain topics,
particularly future systems and the risks of increased AI capabilities.
We can make clear the limits of statements of principle by comparing their laudable aims to how AI is used
in practice. For instance, the AI principles published by a Chinese state committee read “These norms aim...
to promote fairness, justice, harmony, and security while avoiding such problems as bias, discrimination, and


--- Page 20 ---

20
•
Leech et al.
privacy.” This is in stark contrast to the widespread use of AI in human rights violations in China [397, 578].
Ethics research that distracts from unethical actual uses of AI has been called “ethics-washing” [576, 598].
Funding allocations and research outputs also indicate which ethical constraints are active. Despite publishing
twice as much work on AI as the US [604], Chinese research accounts for 1% of all research into social bias in
AI; the US accounts for 48% [465]. Conversely, Chinese research constitutes 58% of the world’s state-of-the-art
Region-Based Convolutional Neural Network object recognition research, a key input for automated surveillance
(the US share is 11%) [465]. Of course, publication rates alone do not rule out responsible use of this research.
3.7.3
Turning Principles into Action. One concrete product of research on AI ethics is the new norm in corporate AI
products of providing “model cards”: descriptions of the training process, the provenance of the data, performance
limitations, and ethical considerations [388]. Similarly, requirements such as those at the US National Science
Foundation for researchers to document the “broader impacts” of their work encourage researchers to think
about downstream consequences of their work at its inception [409]. Unfortunately, it is diﬃcult to quantify the
eﬀect of these requirements on AI research.
In the West, AI workers play a key role in promoting ethical use [411]. The global talent shortage in the ﬁeld
gives researchers and engineers power over project selection, as demonstrated by the successful walkout over
military applications at Google [505, 411, 52]. Protection for whistleblowers is thus a key way for governments
and industry bodies to promote responsible AI [126]; such protections are simply not available in many countries,
and are not always honored even when they are mandated by law.
As much as AI poses serious risks, there is a precedent for data-driven mechanisms reducing discrimination, and
even greater potential [356]. The original FICO credit score—a pioneering loan approval system based on metrics
rather than bank managers’ judgment—helped expand opportunities Black and African American entrepreneurs
to obtain ﬁnancing in the United States [422]. In an example of future promise, one report concludes that current
ML systems could substantially assist each of the UN Sustainable Development Goals [240].
To make systems perform properly for underrepresented groups, we need predictive data about such groups [438].
Federated learning promises to allow such data to be collected while respecting privacy [281], but more represen-
tative data needs to be identiﬁed.
Much attention has been devoted to AI misinformation [143]. Simultaneously, a line of AI systems have shown
promise in correcting misinformation and catching bad scholarship [456, 454, 143]. This could be a scalable way
to address the rise of generative models. For instance, the Meta AI system Sphere scans citations, looks up the
original sources, and detects cases where the source does not support the claim [456].
3.8
Hard Problem #8: By 2050, we will have solved AI-related risks around its use and misuse,
competition, cooperation, and coordination between countries and other key actors.
AI is likely to transform international security, the broader competitive landscape between states, the power and
roles of states relative to other actors, and the conditions or foundations of global cooperation or coordination.
These geopolitical challenges will be particularly diﬃcult to address: “few eras have faced a strategic and
technological challenge so complex [as AI] and with so little consensus about either the nature of the challenge
or even the vocabulary necessary for discussing it.” [296]. The history of cyberwarfare and drone warfare shows
that it can be diﬃcult to anticipate the impacts of emerging technologies, or even to assess them accurately after
deployment [250]. This lack of consensus about the exact impacts, coupled with the high political stakes around
AI, will likely impede eﬀective coordination. Indeed, one hurdle to managing AI’s geopolitical impacts is that
addressing them is a collective action problem [412] that entails structural risks, such that there is no apparent
entity whose behavior could redress the harm. As a result, adverse impacts of the technology will likely be diﬀuse
and uncertain, and eﬀective responses will be delayed [127].


--- Page 21 ---

Ten Hard Problems in AI
•
21
Figure 11 predicts the eﬀect of geopolitical applications of AI on diﬀerent elements of the international order.
Only the use of AI for information gathering (reducing uncertainty and validating counterparty claims about
capabilities) is thought likely to reduce tension; the authors ﬁnd that other eﬀects are likely to reduce stability,
and to erode the compliance of military operations with humanitarian principles.
3.8.1
Destabilizing military conflicts. AI has the potential to destabilize international relations in the near term.
While militaries face unexpected challenges in procuring AI technologies and adapting them to their operational
needs [33, 572], recent years have seen growing investment in AI by G7 countries [226], with Libya and Ukraine
providing opportunities to demonstrate these systems at work [360, 367]—to much outspoken opposition from
civil society and public stakeholders [52, 36]. The advancement of AI capabilities in the military and intelligence
realm may lead to loss of strategic stability, a disturbance of the foundational tenets of nuclear deterrence [296, 251,
585, 367, 32], and new avenues towards unintended escalation [275]. Oﬀthe battleﬁeld, AI makes cyber-threats
cheaper, more scalable, and potentially more dangerous [80, 172, 276].
The growing availability of AI means that these systems are likely to proliferate to non-state actors. This includes
AI-enabled systems which could facilitate terror attacks and assassinations [59]. Although truly catastrophic
terror attacks using swarms of small drones may encounter practical constraints in the near term [367], it is
increasingly recognized that AI systems for tasks such as image recognition need not perform ﬂawlessly to be
attractive to non-state insurgent groups seeking to level the playing ﬁeld against state militaries [318, 376].
Addressing these risks is complicated by the fact that leading nations have generally shown a lack of interest
in regulating military AI [150, 360]. While conﬁdence-building measures, norm-setting and ultimately treaties
have helped limit the destabilizing impact of chemical, biological and nuclear weapons, AI is rapidly ﬁnding
revenue streams that eluded the nuclear industry, with a speed and magnitude of scaling without precedent in
other industries.
3.8.2
Destabilizing other international interactions. The geopolitical impacts of AI are far broader than military
use. New technologies often signiﬁcantly disrupt trade and other aspects of international relations, altering states’
preferences and interests, redistributing power, and creating new ways to exercise hard and soft power [160].
This is especially true for “general-purpose technologies” like AI [148, 193, 585]. Traditional geopolitical analysis
focusing on state actors may become misleading as private companies play an ever more important role in
signiﬁcant AI. Likewise, established concepts like the “national interest” may be complicated by transnational
networks of ﬁrms and individuals [149].
Another problem lies in managing the growing geopolitical competition over AI. The common description of
these trends as an “arms race” is inaccurate, since only a minority of the capabilities pursued or invested in are
entirely military in nature, and arms, once created, do not lead to increased productivity [495]. The trends can be
more accurately described as a winner-take-most “virtuous circle” with strong network eﬀects. Success in such a
competition depends on access to key AI inputs, such as data, hardware, software and talent [326], as well as
diﬀerent states’ eﬀorts to deny one another such access through strategic decoupling [553] and the maintenance
of “chokepoints” [44] in the global AI value chain.
At present, the US and China lead the AI ﬁeld [index2024]. The technological decoupling between China and
the United States is continuing, with China working towards self-suﬃciency in high-tech products [47]—for
example, in 2022 the Chinese government mandated that all computers used by state organizations must be
produced within China. [326]. China’s pursuit of AI arises not only from domestic regulatory needs, but from the
desire for global agenda-setting power [100]. While leading Chinese private companies such as Alibaba, Huawei,
and Baidu are now considered “national champions” and play some role in agenda-setting, their inﬂuence is
limited compared to their US counterparts.
Strategic competition over AI is driving growing regulatory fragmentation between the US, China, and
Europe [481, 177]. While the US and China lead in terms of technical AI capabilities, the European Union leads


--- Page 22 ---

22
•
Leech et al.
in AI regulation [523, 328, 163, 326]. Diﬀering regulatory regimes are likely to cause conﬂict not just between
military rivals, but between the individual countries that make up the Eastern and Western blocs, as corporations
take advantage of opportunities for regulatory arbitrage.
To date, the US approach to AI governance has been largely hands–oﬀ[326, 482], fostering innovation by
reducing regulatory burdens [561]. While the US has implemented some important initiatives such as the AI
Bill of Rights [66], its overall laissez-faire approach has resulted in less global inﬂuence than the framework
developed by the European Union. Instead, the US has focused on industrial policy, such as the CHIPS and Science
Acts [326, 453, 18], to strengthen its AI supply chain—increasingly to the detriment of its European allies. Lastly,
the international nature of AI ecosystems and digital platforms renders exclusively national regulation expensive
and suboptimal [498].
3.8.3
Navigating AI turbulence. To carry a stable world through to the year 2050, the geopolitical risks associated
with AI will need to be addressed, just as in the last century we found ways to address the risk and instability
created by nuclear weapons.
AI is likely to play a role. Some AI tools, including translation, information aggregation and monitoring tools,
are likely to improve information ﬂow and ultimately decrease conﬂict—especially given their potential to help
smaller actors participate in global dialogue on a more even footing [137, 365].
3.9
Hard Problem #9: By 2050, we will have solved the adaptation, co-evolution and resiliency of
institutions and social infrastructure to keep up with and harness AI progress for the benefit
of society.
“This lack of [AI governance] standards makes it both more challenging to deploy systems,
as developers may need to determine their own policies for deployment, and it also makes
deployments inherently risky, as there’s less shared knowledge about what ’safe’ deployments
look like. We are, in a sense, building the plane as it is taking oﬀ.”
– Ganguli et al. [192]
The pressures placed by AI on social infrastructure (for example governments, universities, corporations,
publishers) are likely to increase as AI capabilities continue to grow, proliferate, and outstrip control. HP#9
focuses on domestic governance: we consider explicit governmental and industry mechanisms for AI assurance,
alignment, social responsibility, and the adaptation of social institutions to the coming disruption.
Stahl [533] divides governance proposals into three main categories: policy-level proposals, organizational
responses, and guidance for individuals. We focus on the ﬁrst two. (Policy-level proposals are also called “hard
law,” while the other two categories fall under “soft law.”)
While AI governance has grown signiﬁcantly in recent years [514, 19]), the ﬁeld is still ﬁnding its place
between public policy, political science, international relations, security studies, jurisprudence, and other existing
structures.
Figure 12 depicts some mechanisms by which AI governance is produced. Such mechanisms cover regulation,
industry standards, ethics principles, and coordination protocols between stakeholders. Although regulations and
standards serve as potent instruments in governing AI, their eﬃcacy in directing AI towards socially advantageous
outcomes may be limited without the integration of ethical considerations and the capacity to apply such ethical
principles, [183, 140], as well as research into risks that are not yet within the “Overton window” of political
concern [127].
In governance papers published in 2010–2022, the most common academic background was computer science
and IT, with 52% of researchers coming from other ﬁelds [19].


--- Page 23 ---

Ten Hard Problems in AI
•
23
Up to 2023, contributions to AI governance focused on on individual problems [537, 478] and attempts to
lay foundations for the ﬁeld through prospective research agendas and advocacy [125, 128, 588]. In 2023, this
work bore fruit in the form of a major international summit [562], Congressional and House hearings [565],
consensus declarations [564], and new, well-resourced government bodies with responsibility for the oversight
and evaluation of AI risks [563, 418].
A major problem with surveying governance research is that the public record is heavily ﬁltered. Jack Clark,
former policy director at OpenAI, notes candidly that “A surprisingly large amount of AI policy is illegible,
because mostly [only] the PR-friendly stuﬀgets published, and many of the smartest people working in AI policy
circulate all their stuﬀprivately” [109].
Some problems with AI regulation are shared with other emerging technologies: consider information asymme-
tries between manufacturers and regulators, policy uncertainty and the political cycle, structural power dynamics,
and policy errors [546]. The resulting “Collingridge dilemma” is the observation that regulators attempting to
prevent harm from new technologies must create norms and laws before it is even possible to fully understand
the potential impact of the technology, or their regulations on it [200, 514]. Regulators face a trade-oﬀbetween
proactive regulation (to minimize risks but hinder innovation) and a more laissez-faire approach (that would
incentivize AI development, but could drastically increase potential risks).
The dilemma is common to many emerging technologies, but the ﬁeld of AI governance is extreme in that its
potential risks include proactive and adversarial dynamics not found in other technologies: AI is a technology
which can misuse itself [126, 125, 92]. In addition to directly catastrophic scenarios such as misaligned power-
seeking AI [92], Dafoe identiﬁes four main sources of risk: (1) robust totalitarianism; (2) preventive, inadvertent,
or runaway nuclear war; (3) powerful AI systems not fully aligned with human values; and (4) systematic value
erosion from competition [127].
Gasser and Almeida categorize approaches to AI governance as a series of layers on top of the technology:
(1) the technical layer, which seeks to understand AI technologies, leading to context-speciﬁc mechanisms
for diﬀerent technologies and diﬀerent levels of intervention (technical, organizational, policy);
(2) the responsibility layer, in which all the societal, ethical, and regulatory impacts of AI are considered. The
aim is to help guide policy by understanding the wider societal, ethical, and legal challenges;
(3) the regulation layer, in which the speciﬁc subjects addressed by AI regulation and coordination are deﬁned;
(4) the public policy layer, including the implementation of hard and soft governance mechanisms (social and
legal norms, regulation and legislation, ethical principles and codes of conduct, as well as practices such
as data management tools, standards, and certiﬁcations); policy implementation should take into account
the various contexts and levels of implementation in the technical layer and involve various forms of
cooperation between diﬀerent actors and stakeholders;
(5) the collaborative layer, in which stakeholder goals and conﬂicting interests are balanced, building trust,
shared values, and motivation among diﬀerent stakeholders [589].
A leading example of a policy which spans these layers is “compute governance”, by which the provenance
of high-end chips is tracked and controlled [291, 295]. Other tools include procurement regulation [155], “soft
law” [369], ethical reviews and impact assessments at conferences [313], research release strategies [509], pre-
publication impact assessments [459], standards-setting organizations (e.g. ISO, IEEE, ESOs, and NIST) [417, 106],
third-party certiﬁcation schemes [107], criminal law [293], human rights law [355], ethics oversight boards (on
the model of the Meta Oversight Board [234]), permit programs [566], cooperative policies between AI labs [30],
software and hardware mechanisms that allow actors to make veriﬁable claims about their AI systems [81],
competition law [231], and perhaps new instruments like private regulatory markets [110].


--- Page 24 ---

24
•
Leech et al.
3.10
Hard Problem #10: By 2050, we will have solved what it means to be human in the age of AI.
AI poses personal and philosophical challenges. Say an AI does your job better than you; setting aside the
economic concerns, what does this mean for you as a moral agent, as a citizen, and as a human being?
Figure 13 presents John Danaher’s list of philosophical and personal problems that would arise if AI and other
software greatly reduced the economic and social importance of human labor and creativity [131].
3.10.1
Does AI mean that humans won’t mater? A common goal in life is to make a diﬀerence, but the conceivable
full automation of human work would prevent this. Danaher calls this the severance problem: automating human
activity severs the connection between human eﬀort and the world improving (counterfactually, such that the
world would be worse if we did not act) [131]. This problem also covers the loss of positional goods, which rely
on us being the “best” at something (perhaps as a species, rather than individually) [77]. Moreover, the problem is
only partially mitigated by limiting machine entry into certain ﬁelds—for example by preventing bipedal robots
from entering into races with humans—since the essence of the problem is that you could be replaced even if you
are not.
The severance problem is related to the worry that AI excellence will inspire passivity in individuals, and
so stagnation in society [421, 132]—a kind of bystander eﬀect for values. This is particularly worrying from
the perspective of political and moral agency. Democratic societies require a certain level of voluntary action,
activism, oversight, and other forms of participation to function in a stable fashion [129]. Similarly, moral progress
usually depends on the actions of the unusual thinkers and ‘moral entrepreneurs’ [134] who start the movements
that lead to shifting attitudes and laws [567].
Language is the major channel of social organization. Tobias Rees argues that language models thus precipitate
a particular crisis because our culture (or ontology) has assumed that humans are the only agents which use
language, and that we are unprepared for a world in which most text is AI-generated [473].
AI could make it drastically harder to understand society and each person’s role in it [131]. For example,
systems collect data on us and make decisions about us—but if these processes are inside a private company
(or a classiﬁed government function), we will struggle to discover and establish an explanation for decisions
made about us [501, 117]. This could greatly intensify the old problem of bureaucracy: diﬀused responsibility,
without possibility of appeal or transparency [268, 361, 373]. Inscrutable systems such as large neural networks
will remove the possibility of understanding how speciﬁc decisions were made, even in the presence of strong
legal protections and compliant organizations [86]. Together, these eﬀects serve to make society’s operations
opaque to a given person, and so make it harder for them to exercise control over their own life. This arguably
also threatens their dignity [131].
Finally, the ongoing spread of AI surveillance could also threaten freedom of association and protest, even in
democracies [547]. AI and automation will make it cheaper to exercise various forms of social control [179, 590].
This can be achieved in a (relatively) liberal fashion through ‘nudging’, subtly altering the choices made most
salient to the user [72]; adapting this to best inﬂuence each user diﬀerently has been called “hypernudging” [324].
Digital policing and omnipresent surveillance is another, much less subtle, way to have your freedom limited—with
its increased scope and scalability allowing for new forms of overreach [179].
If your decisions are covertly or overtly inﬂuenced, making it harder for you to exercise control over your own
life, is this a threat to your dignity [131] and what it means to be human? Or will this simply become the ‘new
normal’, a default which does not often rise to conscious attention?
Besides the potential loss of broader ﬂourishing, we might worry that loss of attention could further reinforce
a fall in social participation, as discussed below.


--- Page 25 ---

Ten Hard Problems in AI
•
25
3.10.2
Will humans choose to value things that don’t mater? Alternatively, humans may chose to retain their
distinctiveness from AI by purposely excluding AI from particular activities, by analogy with a wealthy family
that prefers to cook a meal themselves, rather than have one cooked by a professional chef.
Consider sport, one arena in which human excellence and meaning-making has not suﬀered much from the
existence of superhuman machines [272]. Chess engines have been superhuman for 25 years [89], but human
chess retains an audience many thousands of times larger than machine chess—and by many measures, interest
in chess played by humans is higher than it has ever been [550]. This is some indication that human-human
competition may be both preferable and suﬃcient for meaning.
The drama that grips audiences also seems to stem from human performers [261]: however, whether humans
will prefer live-action humans in pre-recorded video when actors are indistinguishable from artiﬁcial replacements
is an open question. One point in favor is that live performance of all kinds is often regarded as a superior good
to pre-recorded or generated art, even all-time great recordings [543, 320]. Live shows generally command a cost
premium. Further, if the meaningfulness of these activities survives machine excellence then it seems likely that
the goods associated with connoisseurship and participation in the related communities will also survive [368,
142, 555]. Human performance might then still generate some form of the crucial goods of excellence, mattering,
community, and social recognition [201]—even if it is indistinguishable from AI output to most observers.
3.10.3
Meaning afer AI. Is our last paragraph wishful thinking by “meat machines”[541] on our way to being
replaced by superior content creators? Like the current economy, the coming AI economy may default to producing
an unending stream of addictive or distracting entertainment—perhaps with psychological consequences far
beyond current claims about addictive social media [252, 93]. The philosophical problem with addiction (or
extreme distraction) is that it replaces broad life pursuits with one-dimensional behavior which likely misses
much of what others consider to be valuable (the addicted individual having lost the ability to behave as a rational
actor). Highly addictive AI-developed media might prevent us from realizing indirect goods which require delayed
gratiﬁcation and investment, especially social goods [180]. This view presumes pluralism, in that there are many
valuable things, and it is important to achieve a good range of them [547, 184]. (Philosophers often assume that
addiction leads to the total loss of self-control, and so dignity, but this is contested [184].) Another problem is that
automated entertainment will reﬂect “simple engagement metrics rather than a harder-to-measure combination
of societal and consumer well-being” [68]—and thus provide us with unusually shallow kinds of pleasure.
Given this background, it seems odd to suggest that AI could help resolve the subjective and philosophical
problems it causes. One route involves helping us understand ourselves [209]: if the scientiﬁc promise of AI
is met, then we will all gain the good of better understanding the world, society, and the brain. AI might also
provide an unprecedented laboratory for simulating and testing hypotheses about intelligence, creativity, cultural
evolution, and values [473, 31, 27].
4
Are the Hard Problems wicked problems?
Rittel and Webber coined the term wicked problems to describe social problems that by nature cannot be
solved [479]. Wicked problems defy solution due to their entanglement of facts and values; their lack of a
conclusive criterion; their preclusion of any opportunity to learn by trial-and-error; their numerous incompatible
explanations; and to their perverse links to other problems. For example, bringing fresh water to buildings
and removing waste through city-scale plumbing and sewer infrastructures is not a wicked problem, because
approaches for building water delivery and sewage are well understood, and near-optimal approaches can be
readily designed. On the other hand, designing an urban mass-transit system requires weighing many more
choices, with each potential decision having many potentially positive and negative consequences.
The wicked problem framework has been widely used in the decades since it was formulated. As Hou, Li,
and Song write in a review of 800 academic publications that used the wicked problem framework, “Because


--- Page 26 ---

26
•
Leech et al.
fragmented but interconnected social challenges coexist, wicked problems call for cooperation among diﬀerent
disciplines” [253].
Surveying the above research, it may be tempting to conclude that our Hard Problems are wicked problems, and
so move on to some less question—but we claim that suitably realistic and precise versions of the Hard Problems
are not wicked. After forty years of work using the framework, “Most authors hold that wicked problems are made
up of multiple internal characteristics, all of which can be divided on diﬀerent scales from docile to intractable,
as diﬀerences between facts and values [in] combination,” Hou, Li, and Song continue; what makes a problem
wicked, rather than tame, is that it can “cross the boundaries between countries, policy domains, organizations,
and scientiﬁc disciplines” with “a combination of complexity, diversity and uncertainty” [253].
Making progress on a wicked problem requires distinguishing aspects of the problem that are based on facts
from those that are based on values. Problems that are largely about facts should have near-optimal solutions,
given agreement on a loss function for mapping multiple parameters onto some scale. Values are inherently more
complex than facts, both a result of their philosophical foundations and the diﬃculty of quantifying them.
The Hard Problems ﬁt some of the wickedness criteria—for example, there is no ‘stopping rule’ for understanding
or redeﬁning what it means to be human (HP#10). We may not have an answer for what it means to be human in
the age of AI, but we have a working understanding of the more general problem via the history of philosophy.
When overcoming the “scientiﬁc and technological limitations in current AI” (HP#1) or enabling “game-
changing contributions” (HP#4), we do have “conventionalized criteria for objectively deciding whether the
oﬀered solution” [479] does or does not address today’s AI limitations or create new capabilities, violating one of
the criteria for wickedness. These solutions (if they are found) will also be testable, which violates one of the
worst features of a wicked problem.
The Hard Problems that directly invoke human values (e.g., HP#3, HP#6–9) are better candidates for wicked
problems: they lack stopping rules and the purported solutions are not testable. With such problems, solutions are
not judged on technical correctness, but on their ﬁt to values. For instance, a technology that supports responsible
democratic control by an informed electorate will only make progress on HP#9 for users who prefer democracy.
For those who prefer a totalitarian system in which artiﬁcial intelligence surveillance protects a ruling elite
against accountability [90, 607, 147], very diﬀerent breakthroughs will be seen as progress.
By arguing that the Hard Problems are not necessarily wicked, we hold open the possibility that some or all of
the problems might actually be solved—or at least, that we might be closer to solving them in 2050 than today.
5
Outlook
Between 2012 and 2022, the publication rate in technical AI doubled, reaching 240,000 papers per year [index2024],
more than the entire ﬁeld of physics [517]. As a result, the most intensely researched and well-resourced areas in
AI are HP#1 and HP#4—the accelerator pedal.
The broad vision of the AI2050 program is that AI researchers, funding agencies, and society at large can
make decisions now and in the following years that will result in widespread beneﬁcial impact. Finding answers
to the Hard Problems will clearly be a challenge, but we see no other choice if humans are to coexist with our
technologies. For all these problems, one clear condition of a successful 2050 scenario is that we begin work on
them now.
Acknowledgments
This literature review was made possible in part by grant G-22-63887 of the Eric and Wendy Schmidt Fund for
Strategic Innovation, and by the Schelling Residency. We thank Sanjeev Arora, Mike Belinsky, Jan Brauner, Dan
Carey, Connor Coley, Andis Draguns, Owain Evans, Basil Halperin, Jose Hernandez-Orallo, Robert Kirk, James
Lucassen, Matthijs Maas, Sören Mindermann, Hugh Panton, Javier Prieto, Yonadav Shavit, Karina Vold, Sophia


--- Page 27 ---

Ten Hard Problems in AI
•
27
Wisdom, Junfeng Yang, John Zerilli, Huan Zhang, and our many anonymous reviewers for their comments and
suggested improvements to the paper. We thank Calum Leslie for editing work. Marcus Gemzoe-Winding and
Anekdote Studio assisted with our visualizations. Eric Schmidt and James Manyika contributed the original list of
hard problems.
References
[1]
6th Circuit Court. Cahoo v. SAS Analytics Inc., No. 18-1296 (6th Cir. 2019). en. 2019. url: https://law.justia.
com/cases/federal/appellate-courts/ca6/18-1296/18-1296-2019-01-03.html (visited on 12/07/2022).
[2]
Scott Aaronson. Postdocs, matrix multiplication, and WSJ: yet more shorties. 2022. url: https://scottaaronson.
blog/?p=6745.
[3]
Martín Abadi et al. “Deep Learning with Diﬀerential Privacy”. In: Proceedings of the 2016 ACM SIGSAC
Conference on Computer and Communications Security. arXiv:1607.00133 [cs, stat]. Oct. 2016, pp. 308–318.
doi: 10.1145/2976749.2978318. url: http://arxiv.org/abs/1607.00133 (visited on 12/08/2022).
[4]
Mohamed Abdalla and Moustafa Abdalla. “The Grey Hoodie Project: Big tobacco, big tech, and the threat
on academic integrity”. In: Proceedings of the 2021 AAAI/ACM Conference on AI, Ethics, and Society. 2021,
pp. 287–297.
[5]
Josh Abramson et al. Improving Multimodal Interactive Agents with Reinforcement Learning from Human
Feedback. arXiv:2211.11602 [cs]. Nov. 2022. doi: 10.48550/arXiv.2211.11602. url: http://arxiv.org/abs/2211.
11602 (visited on 11/30/2022).
[6]
Laura Abrardi, Carlo Cambini, and Laura Rondi. The Economics of Artiﬁcial Intelligence: A Survey. en.
SSRN Scholarly Paper. Rochester, NY, July 2019. doi: 10.2139/ssrn.3425922. url: https://papers.ssrn.com/
abstract=3425922 (visited on 10/21/2022).
[7]
Daron Acemoglu and Pascual Restrepo. Tasks, Automation, and the Rise in US Wage Inequality. Working
Paper. June 2021. doi: 10.3386/w28920. url: https://www.nber.org/papers/w28920 (visited on 01/08/2024).
[8]
Daron Acemoglu and Pascual Restrepo. “The Race between Man and Machine: Implications of Technology
for Growth, Factor Shares, and Employment”. en. In: American Economic Review 108.6 (June 2018), pp. 1488–
1542. issn: 0002-8282. doi: 10.1257/aer.20160696. url: https://www.aeaweb.org/articles?id=10.1257/aer.
20160696 (visited on 09/15/2022).
[9]
Sam Adams et al. “Mapping the landscape of human-level artiﬁcial general intelligence”. In: AI Magazine
33.1 (2012), pp. 25–42.
[10]
Nuclear Energy Agency. Chernobyl: Assessment of Radiological and Health Impacts. 2002. url: https:
//www.oecd-nea.org/jcms/pl_13598.
[11]
Philippe Aghion, Benjamin F. Jones, and Charles I. Jones. Artiﬁcial Intelligence and Economic Growth.
Working Paper. Oct. 2017. doi: 10.3386/w23928. url: https://www.nber.org/papers/w23928 (visited on
09/15/2022).
[12]
Forest Agostinelli et al. “Learning activation functions to improve deep neural networks”. In: arXiv (2014).
[13]
Ajay Agrawal, Joshua Gans, and Avi Goldfarb. Prediction Machines: The Simple Economics of Artiﬁcial Intel-
ligence. en. Google-Books-ID: 8MBYEAAAQBAJ. Harvard Business Press, Nov. 2022. isbn: 9781647824686.
[14]
Nur Ahmed and Muntasir Wahed. The De-democratization of AI: Deep Learning and the Compute Divide
in Artiﬁcial Intelligence Research. arXiv:2010.15581 [cs]. Oct. 2020. doi: 10.48550/arXiv.2010.15581. url:
http://arxiv.org/abs/2010.15581 (visited on 09/19/2022).
[15]
Hassan Akbari et al. VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio
and Text. tex.copyright: arXiv.org perpetual, non-exclusive license. 2021. doi: 10.48550/ARXIV.2104.11178.
url: https://arxiv.org/abs/2104.11178.


--- Page 28 ---

28
•
Leech et al.
[16]
Ekin Akyürek et al. What learning algorithm is in-context learning? Investigations with linear models.
arXiv:2211.15661 [cs]. Nov. 2022. doi: 10.48550/arXiv.2211.15661. url: http://arxiv.org/abs/2211.15661
(visited on 11/29/2022).
[17]
Alignment Research Center. Update on ARC’s recent eval eﬀorts. Mar. 2023. url: https://evals.alignment.
org/blog/2023-03-18-update-on-recent-evals/ (visited on 04/06/2023).
[18]
Gregory Allen. Choking OﬀChina’s Access to the Future of AI. en. 2022. url: https://www.csis.org/analysis/
choking-chinas-access-future-ai (visited on 12/27/2022).
[19]
Patricia Gomes Rêgo de Almeida, Carlos Denner dos Santos, and Josivania Silva Farias. “Artiﬁcial Intelli-
gence Regulation: A Framework for Governance”. en. In: Ethics and Information Technology 23.3 (Sept.
2021), pp. 505–525. issn: 1572-8439. doi: 10.1007/s10676-021-09593-z. url: https://doi.org/10.1007/s10676-
021-09593-z (visited on 12/06/2022).
[20]
Ramón Alvarado. “Should we replace radiologists with deep learning? Pigeons, error and trust in medical
AI”. In: Bioethics 36.2 (2022). Publisher: Wiley Online Library, pp. 121–133.
[21]
Dario Amodei and Danny Hernandez. AI and Compute. 2018. url: https://openai.com/blog/ai-and-
compute/.
[22]
Dario Amodei et al. Concrete Problems in AI Safety. arXiv:1606.06565 [cs]. July 2016. doi: 10.48550/arXiv.
1606.06565. url: http://arxiv.org/abs/1606.06565 (visited on 09/29/2022).
[23]
Constanza L. Andaur Navarro et al. “Systematic review identiﬁes the design and methodological conduct
of studies on machine learning-based prediction models”. en. In: Journal of Clinical Epidemiology (Nov.
2022). issn: 0895-4356. doi: 10.1016/j.jclinepi.2022.11.015. url: https://www.sciencedirect.com/science/
article/pii/S0895435622003006 (visited on 12/03/2022).
[24]
Mykhaylo Andriluka, Jasper R. R. Uijlings, and Vittorio Ferrari. “Fluid Annotation”. In: Proceedings of the
26th ACM International Conference on Multimedia. ACM, Oct. 2018. doi: 10.1145/3240508.3241916. url:
https://doi.org/10.1145%2F3240508.3241916.
[25]
Cristina Angelico et al. Can We Measure Inﬂation Expectations Using Twitter? en. SSRN Scholarly Paper.
Rochester, NY, Feb. 2021. doi: 10.2139/ssrn.3827489. url: https://papers.ssrn.com/abstract=3827489
(visited on 12/01/2022).
[26]
Christof Angermueller et al. “Deep learning for computational biology”. en. In: Molecular Systems Biology
12.7 (July 2016), p. 878. issn: 1744-4292, 1744-4292. doi: 10.15252/msb.20156651. url: https://onlinelibrary.
wiley.com/doi/10.15252/msb.20156651 (visited on 09/29/2022).
[27]
Lisa P. Argyle et al. “Out of One, Many: Using Language Models to Simulate Human Samples”. In:
arXiv:2209.06899 [cs]. arXiv, 2022, pp. 819–862. doi: 10.18653/v1/2022.acl-long.60. url: http://arxiv.org/
abs/2209.06899 (visited on 12/01/2022).
[28]
Sanjeev Arora and Yi Zhang. Rip van Winkle’s Razor: A Simple Estimate of Overﬁt to Test Data. arXiv:2102.13189
[cs, stat]. Feb. 2021. doi: 10.48550/arXiv.2102.13189. url: http://arxiv.org/abs/2102.13189 (visited on
09/27/2022).
[29]
Anders Arpteg et al. “Software engineering challenges of deep learning”. In: 2018 44th Euromicro Conference
on Software Engineering and Advanced Applications (SEAA). tex.organization: IEEE. IEEE, 2018, pp. 50–59.
[30]
Amanda Askell, Miles Brundage, and Gillian Hadﬁeld. The Role of Cooperation in Responsible AI Develop-
ment. arXiv:1907.04534 [cs]. July 2019. doi: 10.48550/arXiv.1907.04534. url: http://arxiv.org/abs/1907.04534
(visited on 09/29/2022).
[31]
Amanda Askell et al. A General Language Assistant as a Laboratory for Alignment. arXiv:2112.00861 [cs].
Dec. 2021. doi: 10.48550/arXiv.2112.00861. url: http://arxiv.org/abs/2112.00861 (visited on 10/03/2022).
[32]
Shahar Avin and S. M. Amadae. “Autonomy and machine learning at the interface of nuclear weapons,
computers and people”. en. In: The Impact of Artiﬁcial Intelligence on Strategic Stability and Nuclear Risk.


--- Page 29 ---

Ten Hard Problems in AI
•
29
Ed. by V. Boulanin. Stockholm International Peace Research Institute, Oct. 2019. doi: 10.17863/CAM.44758.
url: https://www.repository.cam.ac.uk/handle/1810/297703 (visited on 10/16/2019).
[33]
Kareem Ayoub and Kenneth Payne. “Strategy in the Age of Artiﬁcial Intelligence”. In: Journal of Strategic
Studies 39.5-6 (Sept. 2016), pp. 793–819. issn: 0140-2390. doi: 10.1080/01402390.2015.1088838. url:
https://doi.org/10.1080/01402390.2015.1088838 (visited on 03/08/2018).
[34]
Jimmy Lei Ba, Jamie Ryan Kiros, and Geoﬀrey E. Hinton. Layer Normalization. tex.copyright: arXiv.org
perpetual, non-exclusive license. 2016. doi: 10.48550/ARXIV.1607.06450. url: https://arxiv.org/abs/1607.
06450.
[35]
Tania Babina et al. Artiﬁcial Intelligence, Firm Growth, and Product Innovation. en. SSRN Scholarly Paper.
Rochester, NY, May 2022. doi: 10.2139/ssrn.3651052. url: https://papers.ssrn.com/abstract=3651052
(visited on 12/27/2022).
[36]
Şerif Onur Bahçecik. “Civil Society Responds to the AWS: Growing Activist Networks and Shifting Frames”.
en. In: Global Policy 10.3 (Sept. 2019), pp. 365–369. issn: 1758-5880, 1758-5899. doi: 10.1111/1758-5899.12671.
url: https://onlinelibrary.wiley.com/doi/10.1111/1758-5899.12671 (visited on 01/11/2023).
[37]
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural Machine Translation by Jointly Learning
to Align and Translate. tex.copyright: arXiv.org perpetual, non-exclusive license. 2014. doi: 10.48550/
ARXIV.1409.0473. url: https://arxiv.org/abs/1409.0473.
[38]
Yuntao Bai et al. Training a Helpful and Harmless Assistant with Reinforcement Learning from Human
Feedback. arXiv:2204.05862 [cs]. Apr. 2022. doi: 10.48550/arXiv.2204.05862. url: http://arxiv.org/abs/2204.
05862 (visited on 09/29/2022).
[39]
Bowen Baker et al. “POSTER: Video PreTraining (VPT): Learning to Act by Watching Unlabeled Online
Videos”. In: New Orleans, LA: NeurIPS, Nov. 2022. doi: 10.48550/arXiv.2206.11795. url: https://nips.cc/
virtual/2022/poster/54699 (visited on 11/26/2022).
[40]
Anton Bakhtin et al. “Human-level play in the game of Diplomacy by combining language models with
strategic reasoning”. In: Science (New York, N.Y.) 0.0 (), eade9097. doi: 10.1126/science.ade9097. url:
https://www.science.org/doi/abs/10.1126/science.ade9097.
[41]
Nesrine Bannour et al. “Evaluating the carbon footprint of NLP methods: a survey and analysis of existing
tools”. In: Proceedings of the Second Workshop on Simple and Eﬃcient Natural Language Processing. Virtual:
Association for Computational Linguistics, Nov. 2021, pp. 11–21. doi: 10.18653/v1/2021.sustainlp-1.2. url:
https://aclanthology.org/2021.sustainlp-1.2 (visited on 12/07/2022).
[42]
Boaz Barak. Emergent abilities and grokking: Fundamental, Mirage, or both? en. Dec. 2023. url: https:
//windowsontheory.org/2023/12/22/emergent-abilities-and-grokking-fundamental-mirage-or-both/
(visited on 01/08/2024).
[43]
Boaz Barak. Injecting some numbers into the AGI debate. 2022. url: https://windowsontheory.org/2022/06/
27/injecting-some-numbers-into-the-agi-debate/.
[44]
Andre Barbe and Will Hunt. Preserving the Chokepoints: Reducing the Risks of Oﬀshoring Among U.S.
Semiconductor Manufacturing Equipment Firms. en-US. Tech. rep. Center for Security and Emerging
Technology, May 2022. url: https://cset.georgetown.edu/publication/preserving-the-chokepoints/
(visited on 10/18/2022).
[45]
Kyle Barr. GPT-4 Is a Giant Black Box and Its Training Data Remains a Mystery. en. Mar. 2023. url:
https://gizmodo.com/chatbot-gpt4-open-ai-ai-bing-microsoft-1850229989 (visited on 01/08/2024).
[46]
Luiz Andre Barroso. “Warehouse-scale Computing”. In: Proceedings of the 2010 ACM SIGMOD International
Conference on Management of data. SIGMOD ’10. New York, NY, USA: ACM, July 2010. isbn: 978-1-
4503-0032-2. doi: 10.1145/1807167.1837133. url: https://doi.org/10.1145/1807167.1837133 (visited on
11/04/2022).


--- Page 30 ---

30
•
Leech et al.
[47]
Jon Bateman. U.S.-China Technological “Decoupling”: A Strategy and Policy Framework. en. url: https:
//carnegieendowment.org/2022/04/25/u.s.-china-technological-decoupling-strategy-and-policy-
framework-pub-86897 (visited on 12/11/2022).
[48]
Seth Baum. Reconciliation between Factions Focused on Near-Term and Long-Term Artiﬁcial Intelligence. en.
SSRN Scholarly Paper. Rochester, NY, May 2017. url: https://papers.ssrn.com/abstract=2976444 (visited
on 11/28/2022).
[49]
Zachary J. Baum et al. “Artiﬁcial Intelligence in Chemistry: Current Trends and Future Directions”. en. In:
Journal of Chemical Information and Modeling 61.7 (July 2021), pp. 3197–3212. issn: 1549-9596, 1549-960X.
doi: 10.1021/acs.jcim.1c00619. url: https://pubs.acs.org/doi/10.1021/acs.jcim.1c00619 (visited on
09/22/2022).
[50]
Atilim Gunes Baydin et al. Automatic diﬀerentiation in machine learning: a survey. arXiv:1502.05767 [cs,
stat]. Feb. 2018. doi: 10.48550/arXiv.1502.05767. url: http://arxiv.org/abs/1502.05767 (visited on
09/29/2022).
[51]
Christoph D. Becker et al. “Current practical experience with artiﬁcial intelligence in clinical radiology: a
survey of the European Society of Radiology”. In: Insights into Imaging 13.1 (2022). Publisher: Springer,
p. 107.
[52]
Haydn Belﬁeld. “Activism by the AI Community: Analysing Recent Achievements and Future Prospects”.
en. In: Proceedings of the AAAI/ACM Conference on AI, Ethics, and Society. ZSCC: 0000004. New York
NY USA: ACM, Feb. 2020, pp. 15–21. isbn: 978-1-4503-7110-0. doi: 10.1145/3375627.3375814. url:
https://dl.acm.org/doi/10.1145/3375627.3375814 (visited on 08/24/2020).
[53]
Gordon Bell, Tony Hey, and Alex Szalay. “Beyond the data deluge”. In: Science (New York, N.Y.) 323.5919
(2009). Publisher: American Association for the Advancement of Science, pp. 1297–1298.
[54]
Yohann Benchetrit, Hubert Banville, and Jean-Rémi King. Brain decoding: toward real-time reconstruction
of visual perception. arXiv:2310.19812 [cs, eess, q-bio]. Oct. 2023. doi: 10.48550/arXiv.2310.19812. url:
http://arxiv.org/abs/2310.19812 (visited on 01/08/2024).
[55]
Yoshua Bengio et al. “Learning Deep Architectures for AI”. In: Now Publishers 2.1 (2009). Publisher: Now
Publishers, Inc., pp. 1–127. issn: 1935-8237. doi: 10.1561/2200000006. url: https://doi.org/10.1561/
2200000006.
[56]
Yoshua Bengio, Aaron Courville, and Pascal Vincent. “Representation learning: A review and new per-
spectives”. In: IEEE Transactions on Pattern Analysis and Machine Intelligence 35.8 (2013). Publisher: IEEE,
pp. 1798–1828.
[57]
Yoshua Bengio and Olivier Delalleau. “On the Expressive Power of Deep Architectures”. In: Algorithmic
Learning Theory. Ed. by Jyrki Kivinen et al. Berlin, Heidelberg: Springer Berlin Heidelberg, 2011, pp. 18–36.
isbn: 978-3-642-24412-4.
[58]
Yoshua Bengio et al. “Greedy layer-wise training of deep networks”. In: Advances in Neural Information
Processing Systems 19 (2006).
[59]
Ronen Bergman and Farnaz Fassihi. “The Scientist and the A.I.-Assisted, Remote-Control Killing Machine”.
en-US. In: The New York Times (Sept. 2021). issn: 0362-4331. url: https://www.nytimes.com/2021/09/18/
world/middleeast/iran-nuclear-fakhrizadeh-assassination-israel.html (visited on 12/13/2021).
[60]
James Bessen. AI and Jobs: The role of demand. Tech. rep. National Bureau of Economic Research, 2018.
[61]
James Betker. The “it” in AI models is the dataset. – Non_Interactive – Software & ML. en-US. June 2023.
url: https://nonint.com/2023/06/10/the-it-in-ai-models-is-the-dataset/ (visited on 02/06/2024).
[62]
Gwyn Bevan and Christopher Hood. “Have targets improved performance in the English NHS?” en. In:
BMJ 332.7538 (Feb. 2006), pp. 419–422. issn: 0959-8138, 1468-5833. doi: 10.1136/bmj.332.7538.419. url:
https://www.bmj.com/content/332/7538/419 (visited on 11/30/2022).


--- Page 31 ---

Ten Hard Problems in AI
•
31
[63]
Federico Bianchi, Amanda Cercas Curry, and Dirk Hovy. “Viewpoint: Artiﬁcial Intelligence Accidents
Waiting to Happen?” en. In: Journal of Artiﬁcial Intelligence Research 76 (Jan. 2023), pp. 193–199. issn:
1076-9757. doi: 10.1613/jair.1.14263. url: https://jair.org/index.php/jair/article/view/14263 (visited on
01/10/2023).
[64]
Steve J. Bickley, Ho Fai Chan, and Benno Torgler. “Artiﬁcial intelligence in the ﬁeld of economics”. en. In:
Scientometrics 127.4 (Apr. 2022), pp. 2055–2084. issn: 1588-2861. doi: 10.1007/s11192-022-04294-w. url:
https://doi.org/10.1007/s11192-022-04294-w (visited on 12/01/2022).
[65]
Christopher Blier-Wong et al. “Machine Learning in P&C Insurance: A Review for Pricing and Reserving”.
en. In: Risks 9.1 (Jan. 2021), p. 4. issn: 2227-9091. doi: 10.3390/risks9010004. url: https://www.mdpi.com/
2227-9091/9/1/4 (visited on 12/07/2022).
[66]
Blueprint for an AI Bill of Rights | OSTP. en-US. url: https://www.whitehouse.gov/ostp/ai-bill-of-rights/
(visited on 12/11/2022).
[67]
Johan Bollen, Huina Mao, and Xiaojun Zeng. “Twitter mood predicts the stock market”. en. In: Journal
of Computational Science 2.1 (Mar. 2011), pp. 1–8. issn: 1877-7503. doi: 10.1016/j.jocs.2010.12.007. url:
https://www.sciencedirect.com/science/article/pii/S187775031100007X (visited on 12/08/2022).
[68]
Rishi Bommasani et al. On the Opportunities and Risks of Foundation Models. arXiv:2108.07258 [cs]. July
2022. doi: 10.48550/arXiv.2108.07258. url: http://arxiv.org/abs/2108.07258 (visited on 09/22/2022).
[69]
Sebastian Borgeaud et al. Improving language models by retrieving from trillions of tokens. arXiv:2112.04426
[cs]. Feb. 2022. doi: 10.48550/arXiv.2112.04426. url: http://arxiv.org/abs/2112.04426 (visited on
11/25/2022).
[70]
Nick Bostrom. Superintelligence: Paths, Dangers, Strategies. USA: Oxford University Press, Inc., 2016. isbn:
978-0-19-873983-8.
[71]
Léon Bottou. “Stochastic Gradient Learning in Neural Networks”. In: Proceedings of Neuro-Nîmes 91.
Nimes, France: EC2, 1991. url: http://leon.bottou.org/papers/bottou-91c.
[72]
Luc Bovens. “The Ethics of Nudge”. en. In: Preference Change: Approaches from Philosophy, Economics and
Psychology. Ed. by Till Grüne-Yanoﬀand Sven Ove Hansson. Theory and Decision Library. Dordrecht:
Springer Netherlands, 2009, pp. 207–219. isbn: 9789048125937. doi: 10.1007/978-90-481-2593-7_10. url:
https://doi.org/10.1007/978-90-481-2593-7_10 (visited on 12/06/2022).
[73]
Harold R. Bowen. Report of the National Commission on Technology, Automation, and Economic Progress:
Volume I. Tech. rep. US Government Printing Oﬃce, 1966.
[74]
Samuel R. Bowman. The Dangers of Underclaiming: Reasons for Caution When Reporting How NLP Systems
Fail. arXiv:2110.08300 [cs]. Mar. 2022. doi: 10.48550/arXiv.2110.08300. url: http://arxiv.org/abs/2110.08300
(visited on 12/03/2022).
[75]
M.L. Brady, R. Raghavan, and J. Slawny. “Back propagation fails to separate where perceptrons succeed”.
In: IEEE Transactions on Circuits and Systems 36.5 (May 1989), pp. 665–674. issn: 1558-1276. doi: 10.1109/
31.31314.
[76]
Johann Brehmer et al. “Constraining Eﬀective Field Theories with Machine Learning”. In: Physical Review
Letters 121.11 (Sept. 2018). Number of pages: 5 Publisher: American Physical Society, p. 111801. doi:
10.1103/PhysRevLett.121.111801. url: https://link.aps.org/doi/10.1103/PhysRevLett.121.111801.
[77]
Harry Brighouse and Adam Swift. “Equality, Priority, and Positional Goods”. In: Ethics 116.3 (Apr. 2006),
pp. 471–497. issn: 0014-1704. doi: 10.1086/500524. url: https://www.journals.uchicago.edu/doi/abs/10.
1086/500524 (visited on 12/05/2022).
[78]
Rodney Brooks. “A better lesson”. In: Robots, AI, and other stuﬀ(2019). url: https://rodneybrooks.%20com/
a-better-lesson.
[79]
Tom B. Brown et al. GPT-3 - Language Models are Few-Shot Learners. arXiv:2005.14165 [cs]. July 2020. doi:
10.48550/arXiv.2005.14165. url: http://arxiv.org/abs/2005.14165 (visited on 09/22/2022).


--- Page 32 ---

32
•
Leech et al.
[80]
Miles Brundage et al. The Malicious Use of Artiﬁcial Intelligence: Forecasting, Prevention, and Mitigation.
arXiv:1802.07228 [cs]. Feb. 2018. doi: 10.48550/arXiv.1802.07228. url: http://arxiv.org/abs/1802.07228
(visited on 09/23/2022).
[81]
Miles Brundage et al. Toward Trustworthy AI Development: Mechanisms for Supporting Veriﬁable Claims.
arXiv:2004.07213 [cs]. Apr. 2020. doi: 10.48550/arXiv.2004.07213. url: http://arxiv.org/abs/2004.07213
(visited on 09/23/2022).
[82]
Erik Brynjolfsson, Danielle Li, and Lindsey R. Raymond. Generative AI at Work. Working Paper. Apr. 2023.
doi: 10.3386/w31161. url: https://www.nber.org/papers/w31161 (visited on 01/08/2024).
[83]
Erik Brynjolfsson and Andrew McAfee. The Second Machine Age. en. Norton, 2014. url: https://wwnorton.
com/books/the-second-machine-age/ (visited on 12/08/2022).
[84]
Erik Brynjolfsson, Daniel Rock, and Chad Syverson. “Artiﬁcial intelligence and the modern productivity
paradox: A clash of expectations and statistics”. In: The Economics of Artiﬁcial Intelligence: An agenda.
University of Chicago Press, 2018, pp. 23–57.
[85]
Sébastien Bubeck et al. Sparks of Artiﬁcial General Intelligence: Early experiments with GPT-4. arXiv:2303.12712
[cs]. Mar. 2023. doi: 10.48550/arXiv.2303.12712. url: http://arxiv.org/abs/2303.12712 (visited on 03/23/2023).
[86]
Jenna Burrell. “How the machine ‘thinks’: Understanding opacity in machine learning algorithms”. en.
In: Big Data & Society 3.1 (June 2016), p. 205395171562251. issn: 2053-9517, 2053-9517. doi: 10.1177/
2053951715622512. url: http://journals.sagepub.com/doi/10.1177/2053951715622512 (visited on
11/26/2022).
[87]
Patrick Butlin. “Sharing Our Concepts with Machines”. en. In: Erkenntnis (Nov. 2021). issn: 1572-8420. doi:
10.1007/s10670-021-00491-w. url: https://doi.org/10.1007/s10670-021-00491-w (visited on 12/01/2022).
[88]
California Consumer Privacy Act (CCPA). en. Oct. 2018. url: https://oag.ca.gov/privacy/ccpa (visited on
12/08/2022).
[89]
Murray Campbell, A. Joseph Hoane, and Feng-hsiung Hsu. “Deep Blue”. en. In: Artiﬁcial Intelligence
134.1 (Jan. 2002), pp. 57–83. issn: 0004-3702. doi: 10.1016/S0004-3702(01)00129-1. url: https://www.
sciencedirect.com/science/article/pii/S0004370201001291 (visited on 12/05/2022).
[90]
Bryan Caplan. “The totalitarian threat”. In: Global Catastrophic Risks. 2008. url: https://academic.oup.
com/book/40615/chapter-abstract/348242235?redirectedFrom=fulltext.
[91]
Joe Carlsmith. Scheming AIs: Will AIs fake alignment during training in order to get power? arXiv:2311.08379
[cs]. Nov. 2023. doi: 10.48550/arXiv.2311.08379. url: http://arxiv.org/abs/2311.08379 (visited on
01/08/2024).
[92]
Joseph Carlsmith. Is Power-Seeking AI an Existential Risk? arXiv:2206.13353 [cs]. June 2022. doi: 10.48550/
arXiv.2206.13353. url: http://arxiv.org/abs/2206.13353 (visited on 09/30/2022).
[93]
Nicholas Carr. The Shallows: What the Internet Is Doing to Our Brains. en. W. W. Norton & Company, Mar.
2020. isbn: 9780393358001.
[94]
S. Cave and S. S. ÓhÉigeartaigh. “Bridging near- and long-term concerns about AI”. en. In: Nature Machine
Intelligence (2019). issn: 2522-5839. doi: 10.17863/CAM.40184. url: https://www.repository.cam.ac.uk/
handle/1810/293033 (visited on 11/28/2022).
[95]
Verge Genomics Centre for Human Drug Research. Study to investigate the safety of VRG50635 in healthy
volunteers and patients with motor neuron disease (amyotrophic lateral sclerosis). 2022. url: https://www.
isrctn.com/ISRCTN14792372.
[96]
Lili Chen et al. Decision Transformer: Reinforcement Learning via Sequence Modeling. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2021. doi: 10.48550/ARXIV.2106.01345. url: https://arxiv.org/
abs/2106.01345.
[97]
Mark Chen et al. Evaluating Large Language Models Trained on Code. arXiv:2107.03374 [cs]. July 2021.
doi: 10.48550/arXiv.2107.03374. url: http://arxiv.org/abs/2107.03374 (visited on 09/23/2022).


--- Page 33 ---

Ten Hard Problems in AI
•
33
[98]
Ting Chen et al. A Simple Framework for Contrastive Learning of Visual Representations. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2020. doi: 10.48550/ARXIV.2002.05709. url: https://arxiv.org/
abs/2002.05709.
[99]
Jianpeng Cheng, Li Dong, and Mirella Lapata. “Long short-term memory-networks for machine reading”.
In: arXiv (2016).
[100]
Jing Cheng and Jinghan Zeng. “Shaping AI’s Future? China in Global AI Governance”. In: Journal of
Contemporary China 0.0 (Aug. 2022), pp. 1–17. issn: 1067-0564. doi: 10.1080/10670564.2022.2107391. url:
https://doi.org/10.1080/10670564.2022.2107391 (visited on 09/23/2022).
[101]
Paul Christiano. Current Work in AI Alignment. en. 2019. url: https://www.eﬀectivealtruism.org/articles/
paul-christiano-current-work-in-ai-alignment (visited on 11/28/2022).
[102]
Paul Christiano. Eliciting latent knowledge. en. Feb. 2022. url: https://ai-alignment.com/eliciting-latent-
knowledge-f977478608fc (visited on 11/28/2022).
[103]
Paul Christiano et al. Deep reinforcement learning from human preferences. arXiv:1706.03741 [cs, stat]. July
2017. doi: 10.48550/arXiv.1706.03741. url: http://arxiv.org/abs/1706.03741 (visited on 09/30/2022).
[104]
Ching-Yao Chuang et al. “Debiased Contrastive Learning”. In: arXiv (2020). Publisher: arXiv tex.copyright:
arXiv.org perpetual, non-exclusive license. doi: 10.48550/ARXIV.2007.00224. url: https://arxiv.org/abs/
2007.00224.
[105]
Tadeusz Ciecierski-Holmes et al. “Artiﬁcial intelligence for strengthening healthcare systems in low-
and middle-income countries: a systematic scoping review”. en. In: Nature 5.1 (Oct. 2022). Number: 1
Publisher: Nature Publishing Group, pp. 1–13. issn: 2398-6352. doi: 10.1038/s41746-022-00700-y. url:
https://www.nature.com/articles/s41746-022-00700-y (visited on 11/04/2022).
[106]
Peter Cihon. Standards for AI Governance: International Standards to Enable Global Coordination in AI
Research & Development. Tech. rep. Future of Humanity Institute, 2019. url: http://www.fhi.ox.ac.uk/wp-
content/uploads/Standards_-FHI-Technical-Report.pdf.
[107]
Peter Cihon et al. “AI Certiﬁcation: Advancing Ethical Practice by Reducing Information Asymmetries”.
In: IEEE Transactions on Technology and Society 2.4 (Dec. 2021), pp. 200–209. issn: 2637-6415. doi: 10.1109/
TTS.2021.3077595.
[108]
Dan Claudiu Ciresan et al. “Flexible, high performance convolutional neural networks for image classi-
ﬁcation”. In: Twenty-second International Joint Conference on Artiﬁcial Intelligence. 2011. doi: 10.5555/
2283516.2283603. url: https://people.idsia.ch/~juergen/ijcai2011.pdf.
[109]
Jack Clark. AI policy tweet thread. en-GB. 2022. url: https://twitter.com/jackclarksf/status/1555980661499908096
(visited on 11/28/2022).
[110]
Jack Clark and Gillian K. Hadﬁeld. Regulatory Markets for AI Safety. arXiv:2001.00078 [cs, econ, q-ﬁn].
Dec. 2019. doi: 10.48550/arXiv.2001.00078. url: http://arxiv.org/abs/2001.00078 (visited on 01/11/2023).
[111]
Climate Change AI. en-US. url: https://www.climatechange.ai/ (visited on 04/05/2023).
[112]
Michael K. Cohen, Marcus Hutter, and Michael A. Osborne. “Advanced artiﬁcial agents intervene in the
provision of reward”. en. In: AI Magazine 43.3 (Sept. 2022), pp. 282–293. issn: 0738-4602, 2371-9621. doi:
10.1002/aaai.12064. url: https://onlinelibrary.wiley.com/doi/10.1002/aaai.12064 (visited on 10/03/2022).
[113]
Alistair Connell et al. “Implementation of a Digitally Enabled Care Pathway (Part 2): Qualitative Analysis
of Experiences of Health Care Professionals”. In: Journal of Medical Internet Research 21.7 (July 2019). url:
https://www.jmir.org/2019/7/e13143/PDF.
[114]
Ajeya Cotra. “The case for aligning narrowly superhuman models”. en. In: Ajeya Cotra (2021). url:
https://www.alignmentforum.org/posts/PZtsoaoSLpKjjbMqM/the- case- for- aligning- narrowly-
superhuman-models (visited on 11/28/2022).


--- Page 34 ---

34
•
Leech et al.
[115]
Ajeya Cotra. “Without speciﬁc countermeasures, the easiest path to transformative AI likely leads to AI
takeover”. en. In: Ajeya Cotra (2022). url: https://www.alignmentforum.org/posts/pRkFkzwKZ2zfa3R6H/
without-speciﬁc-countermeasures-the-easiest-path-to (visited on 11/27/2022).
[116]
Josh Cowls et al. “The AI gambit: leveraging artiﬁcial intelligence to combat climate change—opportunities,
challenges, and recommendations”. en. In: AI & Society (Oct. 2021). issn: 1435-5655. doi: 10.1007/s00146-
021-01294-x. url: https://doi.org/10.1007/s00146-021-01294-x (visited on 12/08/2022).
[117]
Diane Coyle. Socializing Data. en. 2022. url: https://www.amacad.org/publication/socializing-data
(visited on 11/25/2022).
[118]
Nicholas Crafts and Terence C Mills. “Predicting Medium-Term TFP Growth in the United States: Econo-
metrics vs ‘Techno-Optimism’”. In: National Institute Economic Review 242.1 (2017). Publisher: Cambridge
University Press, R60–R67. doi: 10.1177/0027950117242001. url: https://journals.sagepub.com/doi/abs/10.
1177/002795011724200115.
[119]
Carla Zoe Cremer. “Deep limitations? Examining expert disagreement over deep learning”. en. In: Progress
in Artiﬁcial Intelligence 10.4 (Dec. 2021), pp. 449–464. issn: 2192-6360. doi: 10.1007/s13748-021-00239-1.
url: https://doi.org/10.1007/s13748-021-00239-1 (visited on 09/22/2022).
[120]
Carla Zoe Cremer and Jess Whittlestone. “Artiﬁcial Canaries: Early Warning Signs for Anticipatory and
Democratic Governance of AI”. In: IJMAI (2021). Publisher: International Journal of Interactive Multimedia
and Artiﬁcial Intelligence.
[121]
Andrew Critch and David Krueger. AI Research Considerations for Human Existential Safety (ARCHES).
arXiv:2006.04948 [cs]. May 2020. doi: 10.48550/arXiv.2006.04948. url: http://arxiv.org/abs/2006.04948
(visited on 11/28/2022).
[122]
Rebecca Crootof, Margot E. Kaminski, and W. Nicholson Price II. Humans in the Loop. en. SSRN Scholarly
Paper ID 4066781. Rochester, NY: Social Science Research Network, Mar. 2022. doi: 10.2139/ssrn.4066781.
url: https://papers.ssrn.com/abstract=4066781 (visited on 04/04/2022).
[123]
Matthew Crosston. “Cyber Colonization: The Dangerous Fusion of Artiﬁcial Intelligence and Authoritarian
Regimes”. In: Cyber, Intelligence, and Security 4.1 (2020). url: https://www.inss.org.il/wp-content/uploads/
2020/04/Cyber4.1ENG_7-151-173.pdf.
[124]
Cuneiform Digital Library Initiative. Cuneiform Tablet P390441. 1900 BCE. url: https://cdli.ucla.edu/
search/search_results.php?SearchMode=Text&ObjectID=P390441.
[125]
Dafoe. “AI Governance: Overview and Theoretical Lenses”. In: Oxford Handbook on AI Governance. Ed. by
YC Chen et al. Oxford University Press, 2023.
[126]
Allan Dafoe. AI Governance: A Research Agenda | GovAI. en. 2018. url: https://www.governance.ai/research-
paper/agenda (visited on 09/23/2022).
[127]
Allan Dafoe. AI Governance: Opportunity and Theory of Impact. en. 2022. url: https://www.governance.ai/
research-paper/ai-governance-opportunity-and-theory-of-impact (visited on 09/23/2022).
[128]
Allan Dafoe et al. “Cooperative AI: machines must learn to ﬁnd common ground”. en. In: Nature 593.7857
(May 2021), pp. 33–36. doi: 10.1038/d41586-021-01170-0. url: https://www.nature.com/articles/d41586-
021-01170-0 (visited on 09/30/2022).
[129]
Robert A. Dahl, Ian Shapiro, and Jose Antonio Cheibub. The Democracy Sourcebook. en. Google-Books-ID:
B8THIuSkiqgC. MIT Press, Aug. 2003. isbn: 9780262541473.
[130]
Andrew M. Dai and Quoc V. Le. Semi-supervised Sequence Learning. arXiv:1511.01432 [cs]. Nov. 2015. doi:
10.48550/arXiv.1511.01432. url: http://arxiv.org/abs/1511.01432 (visited on 09/22/2022).
[131]
John Danaher. Automation and Utopia: Human Flourishing in a World without Work. Harvard University
Press, Sept. 2019. isbn: 978-0-674-24220-3. url: https://www.degruyter.com/document/doi/10.4159/
9780674242203/html (visited on 11/25/2022).


--- Page 35 ---

Ten Hard Problems in AI
•
35
[132]
John Danaher. “The rise of the robots and the crisis of moral patiency”. en. In: AI & Society 34.1 (Mar.
2019), pp. 129–136. issn: 1435-5655. doi: 10.1007/s00146-017-0773-9. url: https://doi.org/10.1007/s00146-
017-0773-9 (visited on 11/26/2022).
[133]
Peter Dauvergne. AI in the Wild: Sustainability in the Age of Artiﬁcial Intelligence. en. Google-Books-ID:
M1X6DwAAQBAJ. MIT Press, Sept. 2020. isbn: 9780262539333.
[134]
Mary De Young. “Moral Entrepreneur”. en. In: The Blackwell Encyclopedia of Sociology. Ed. by George
Ritzer. Oxford, UK: John Wiley & Sons, Ltd, Feb. 2007, wbeosm122. isbn: 978-1-4051-2433-1. doi: 10.1002/
9781405165518.wbeosm122. url: https://onlinelibrary.wiley.com/doi/10.1002/9781405165518.wbeosm122
(visited on 12/06/2022).
[135]
Jeﬀrey Dean et al. “Large scale distributed deep networks”. In: Advances in neural information processing
systems 25 (2012).
[136]
Ashley Deeks. High-Tech International Law. en. SSRN Scholarly Paper. Rochester, NY, Feb. 2020. url:
https://papers.ssrn.com/abstract=3531976 (visited on 09/23/2022).
[137]
Ashley Deeks. “How Will Artiﬁcial Intelligence Aﬀect International Law?” en. In: American Journal of
International Law 114.114 (2020), pp. 138–140. issn: 2398-7723. doi: 10.1017/aju.2020.29. url: https://
www.cambridge.org/core/journals/american-journal-of-international-law/article/introduction-to-the-
symposium-how-will-artiﬁcial-intelligence-aﬀect-international-law/CD26AD55818677B9B28FB59EAD96D4BB
(visited on 01/11/2023).
[138]
Jonas Degrave et al. “Magnetic control of tokamak plasmas through deep reinforcement learning”. en.
In: Nature 602.7897 (Feb. 2022), pp. 414–419. issn: 1476-4687. doi: 10.1038/s41586-021-04301-9. url:
https://www.nature.com/articles/s41586-021-04301-9 (visited on 09/23/2022).
[139]
Mostafa Dehghani et al. The Benchmark Lottery. tex.copyright: arXiv.org perpetual, non-exclusive license.
2021. doi: 10.48550/ARXIV.2107.07002. url: https://arxiv.org/abs/2107.07002.
[140]
Sylvie Delacroix and Ben Wagner. “Constructing a mutually supportive interface between ethics and
regulation”. en. In: Computer Law & Security Review 40 (Apr. 2021), p. 105520. issn: 0267-3649. doi:
10.1016/j.clsr.2020.105520. url: https://www.sciencedirect.com/science/article/pii/S0267364920301254
(visited on 12/09/2022).
[141]
Grégoire Delétang et al. Language Modeling Is Compression. arXiv:2309.10668 [cs, math]. Sept. 2023. doi:
10.48550/arXiv.2309.10668. url: http://arxiv.org/abs/2309.10668 (visited on 01/08/2024).
[142]
Elizabeth B. Delia, Jeﬀrey D. James, and Daniel L. Wann. “Does Being a Sport Fan Provide Meaning in
Life?” en. In: Journal of Sport Management 36.1 (Aug. 2021), pp. 45–55. issn: 0888-4773, 1543-270X. doi:
10.1123/jsm.2020-0267. url: https://journals.humankinetics.com/view/journals/jsm/36/1/article-p45.xml
(visited on 12/05/2022).
[143]
Gianluca Demartini, Stefano Mizzaro, and Damiano Spina. “Human-in-the-loop Artiﬁcial Intelligence for
Fighting Online Misinformation: Challenges and Opportunities”. In: Bulletin of the IEEE Computer Society
Technical Committee on Data Engineering (2020). url: http://sites.computer.org/debull/A20sept/p65.pdf
(visited on 12/02/2022).
[144]
Jia Deng et al. “Imagenet: A large-scale hierarchical image database”. In: Proceedings of the IEEE. tex.organization:
Ieee. IEEE, 2009, pp. 248–255. url: https://ieeexplore.ieee.org/document/5206848.
[145]
Radosvet Desislavov, Fernando Martínez-Plumed, and José Hernández-Orallo. Compute and Energy
Consumption Trends in Deep Learning Inference. arXiv:2109.05472 [cs]. Sept. 2021. doi: 10.48550/arXiv.
2109.05472. url: http://arxiv.org/abs/2109.05472 (visited on 12/03/2022).
[146]
Jacob Devlin et al. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.
arXiv:1810.04805 [cs]. May 2019. doi: 10.48550/arXiv.1810.04805. url: http://arxiv.org/abs/1810.04805
(visited on 09/22/2022).


--- Page 36 ---

36
•
Leech et al.
[147]
Larry Diamond. “The Road to Digital Unfreedom: The Threat of Postmodern Totalitarianism”. en. In:
Journal of Democracy 30.1 (Jan. 2019), pp. 20–24. issn: 1086-3214. doi: 10.1353/jod.2019.0001. url:
https://muse.jhu.edu/article/713719 (visited on 12/09/2022).
[148]
Jeﬀrey Ding and Allan Dafoe. “Engines of Power: Electricity, AI, and General-Purpose Military Trans-
formations”. In: arXiv (June 2021). arXiv: 2106.04338. url: http://arxiv.org/abs/2106.04338 (visited on
06/12/2021).
[149]
Jeﬀrey Ding and Allan Dafoe. “The Logic of Strategic Assets: From Oil to AI”. In: Security Studies 30.2
(Mar. 2021). Publisher: Routledge _eprint: https://doi.org/10.1080/09636412.2021.1915583, pp. 182–212.
issn: 0963-6412. doi: 10.1080/09636412.2021.1915583. url: https://doi.org/10.1080/09636412.2021.1915583
(visited on 12/12/2022).
[150]
Bonnie Docherty. Mind the Gap. en. Tech. rep. Human Rights Watch, Apr. 2015. url: https://www.hrw.
org/report/2015/04/09/mind-gap/lack-accountability-killer-robots (visited on 12/11/2022).
[151]
Jesse Dodge et al. “Measuring the Carbon Intensity of AI in Cloud Instances”. en. In: 2022 ACM Conference
on Fairness, Accountability, and Transparency. Seoul Republic of Korea: ACM, June 2022, pp. 1877–1894.
isbn: 978-1-4503-9352-2. doi: 10.1145/3531146.3533234. url: https://dl.acm.org/doi/10.1145/3531146.
3533234 (visited on 12/07/2022).
[152]
Thomas Dohmke. GitHub Copilot is generally available to all developers. 2022. url: https://github.blog/2022-
06-21-github-copilot-is-generally-available-to-all-developers/.
[153]
Justin Domke. Automatic Diﬀerentiation: The most criminally underused tool in the potential machine
learning toolbox? 2009. url: https://justindomke.wordpress.com/2009/02/17/automatic-diﬀerentiation-
the-most-criminally-underused-tool-in-the-potential-machine-learning-toolbox.
[154]
David Donoho. “50 Years of Data Science”. In: Journal of Computational and Graphical Statistics 26.4 (2017).
Publisher: Taylor & Francis tex.eprint: https://doi.org/10.1080/10618600.2017.1384734, pp. 745–766. doi:
10.1080/10618600.2017.1384734. url: https://doi.org/10.1080/10618600.2017.1384734.
[155]
Lavi M. Ben Dor and Cary Coglianese. “Procurement as AI Governance”. In: IEEE Transactions on Technol-
ogy and Society 2.4 (Dec. 2021), pp. 192–199. issn: 2637-6415. doi: 10.1109/TTS.2021.3111764.
[156]
Alexey Dosovitskiy et al. An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale.
arXiv:2010.11929 [cs]. June 2021. doi: 10.48550/arXiv.2010.11929. url: http://arxiv.org/abs/2010.11929
(visited on 10/13/2022).
[157]
Eleanor Drage and Kerry Mackereth. “Does AI Debias Recruitment? Race, Gender, and AI’s “Eradication
of Diﬀerence””. en. In: Philosophy & Technology 35.4 (Oct. 2022), p. 89. issn: 2210-5441. doi: 10.1007/s13347-
022-00543-1. url: https://doi.org/10.1007/s13347-022-00543-1 (visited on 11/04/2022).
[158]
K. Eric Drexler. Reframing Superintelligence: Comprehensive AI Services as General Intelligence. en-GB.
Tech. rep. Future of Humanity Institute, Jan. 2019. url: https://www.fhi.ox.ac.uk/reframing/ (visited on
11/28/2022).
[159]
Stuart Dreyfus. “The numerical solution of variational problems”. In: Journal of Mathematical Analysis
and Applications 5.1 (1962). Publisher: Academic Press, pp. 30–45.
[160]
Daniel W Drezner. “Technological change and international relations”. en. In: International Relations
33.2 (June 2019), pp. 286–303. issn: 0047-1178, 1741-2862. doi: 10.1177/0047117819834629. url: http:
//journals.sagepub.com/doi/10.1177/0047117819834629 (visited on 01/10/2023).
[161]
Sue Duke. Growing But Not Gaining: Are AI skills holding women back in the workplace? en. 2018. url:
https://economicgraph.linkedin.com/blog/growing-but-not-gaining-are-ai-skills-holding-women-
back-in-the-workplace (visited on 12/09/2022).
[162]
Amir Efrati. OpenAI’s Revenue Crossed $1.3 Billion Annualized Rate, CEO Tells Staﬀ. 2023. url: https:
//www.theinformation.com/articles/openais-revenue-crossed-1-3-billion-annualized-rate-ceo-tells-
staﬀ(visited on 01/08/2024).


--- Page 37 ---

Ten Hard Problems in AI
•
37
[163]
Martin Eifert et al. “Taming the Giants: The DMA/DSA Package”. In: Common Market Law Review 58 (2021),
p. 987. url: https://heinonline.org/HOL/Page?handle=hein.kluwer/cmlr0058&id=995&div=&collection=.
[164]
Tyna Eloundou et al. GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language
Models. arXiv:2303.10130 [cs, econ, q-ﬁn]. Mar. 2023. doi: 10.48550/arXiv.2303.10130. url: http://arxiv.org/
abs/2303.10130 (visited on 03/21/2023).
[165]
Thomas Elsken, Jan Hendrik Metzen, and Frank Hutter. “Neural architecture search: A survey”. In: The
Journal of Machine Learning Research 20.1 (2019). Publisher: JMLR.org, pp. 1997–2017.
[166]
Debbie Encalada. Google Conﬁrms First Ever Driverless Self-Driving Car Ride. 2016. url: https://www.
complex.com/life/2016/12/blind-man-rides-self-driving-google-car-by-himself.
[167]
Ege Erdil and Tamay Besiroglu. Algorithmic progress in computer vision. arXiv:2212.05153 [cs]. Dec. 2022.
doi: 10.48550/arXiv.2212.05153. url: http://arxiv.org/abs/2212.05153 (visited on 01/04/2023).
[168]
Dumitru Erhan et al. “Why Does Unsupervised Pre-training Help Deep Learning?” In: Proceedings of
the Thirteenth International Conference on Artiﬁcial Intelligence and Statistics. Ed. by Yee Whye Teh and
Mike Titterington. Vol. 9. Proceedings of Machine Learning Research. Chia Laguna Resort, Sardinia, Italy:
PMLR, May 2010, pp. 201–208. url: https://proceedings.mlr.press/v9/erhan10a.html.
[169]
John Essington. “How we learn: why brains learn better than any machine ... for now”. In: Educational
Review 74.4 (June 2022), pp. 899–899. issn: 0013-1911. doi: 10.1080/00131911.2021.1930914. url: https:
//doi.org/10.1080/00131911.2021.1930914 (visited on 12/01/2022).
[170]
European Institute for Gender Equality. Artiﬁcial intelligence, platform work and gender equality. en. 2021.
url: https://eige.europa.eu/publications/artiﬁcial-intelligence-platform-work-and-gender-equality
(visited on 11/15/2022).
[171]
Richard Evans and Jim Gao. DeepMind AI Reduces Google Data Centre Cooling Bill by 40%. 2022. url:
https://www.deepmind.com/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-by-40.
[172]
Marina Favaro. Weapons of Mass Distortion: A new approach to emerging technologies, risk reduction, and
the global nuclear order. en. Tech. rep. Centre for Science & Security Studies, King’s College London, June
2021, p. 32. url: https://www.kcl.ac.uk/csss/assets/weapons-of-mass-distortion.pdf.
[173]
Marina Favaro, Neil Renic, and Ulrich Kühn. Negative Multiplicity: Forecasting the Future Impact of Emerging
Technologies on International Stability and Human Security. Tech. rep. 10. University of Hamburg: Institute
for Peace Research and Security Policy, 2022. url: https://doi.org/10.25592/ifsh-research-report-010.
[174]
Alhussein Fawzi et al. “AlphaTensor - Discovering faster matrix multiplication algorithms with reinforce-
ment learning”. en. In: Nature 610.7930 (Oct. 2022), pp. 47–53. issn: 1476-4687. doi: 10.1038/s41586-022-
05172-4. url: https://www.nature.com/articles/s41586-022-05172-4 (visited on 10/06/2022).
[175]
Alhussein Fawzi et al. “Discovering faster matrix multiplication algorithms with reinforcement learning”.
In: Nature 610.7930 (2022). Publisher: Nature Publishing Group, pp. 47–53.
[176]
Edward A Feigenbaum. “Artiﬁcial intelligence research”. In: IEEE Transactions on Information Theory 9.4
(1963), pp. 248–253.
[177]
Claudio Feijóo et al. “Harnessing artiﬁcial intelligence (AI) to increase wellbeing for all: The case for a new
technology diplomacy”. en. In: Telecommunications Policy 44.6 (May 2020), p. 101988. issn: 0308-5961. doi:
10.1016/j.telpol.2020.101988. url: http://www.sciencedirect.com/science/article/pii/S030859612030080X
(visited on 05/11/2020).
[178]
Christiane Fellbaum. “WordNet”. In: Theory and applications of ontology: Computer applications. Springer,
2010, pp. 231–243.
[179]
Filip Bacalu. Digital Policing Tools as Social Control Technologies: Data-driven Predictive Algorithms, Au-
tomated Facial Recognition Surveillance, and Law Enforcement Biometrics. en. 2021. url: https://www.
proquest.com/openview/6749ab16b8e92ea3e0f619e429b9ba96/1?pq-origsite=gscholar&cbl=136104
(visited on 12/06/2022).


--- Page 38 ---

38
•
Leech et al.
[180]
Owen Flanagan. “Addiction Doesn’t Exist, But it is Bad for You”. en. In: Neuroethics 10.1 (Apr. 2017), pp. 91–
98. issn: 1874-5504. doi: 10.1007/s12152-016-9298-z. url: https://doi.org/10.1007/s12152-016-9298-z
(visited on 12/06/2022).
[181]
Bailey Flanigan et al. “Fair algorithms for selecting citizens’ assemblies”. en. In: Nature 596.7873 (Aug. 2021).
Number: 7873 Publisher: Nature Publishing Group, pp. 548–552. issn: 1476-4687. doi: 10.1038/s41586-021-
03788-6. url: https://www.nature.com/articles/s41586-021-03788-6 (visited on 12/09/2022).
[182]
Sean Fleming. Europe’s ﬁrst full-sized self-driving urban electric bus has arrived. 2021. url: https://www.
weforum.org/agenda/2021/03/europe-ﬁrst-autonomous-electric-buses-spain/.
[183]
Luciano Floridi et al. “AI4People—An ethical framework for a good AI society: Opportunities, risks,
principles, and recommendations”. In: Minds and Machines 28.4 (2018). Publisher: Springer, pp. 689–707.
[184]
Bennett Foddy and Julian Savulescu. “A Liberal Account of Addiction”. In: Philosophy, Psychiatry, &
Psychology: PPP 17.1 (Mar. 2010), pp. 1–22. issn: 1071-6076. doi: 10 . 1353 / ppp . 0 . 0282. url: https :
//www.ncbi.nlm.nih.gov/pmc/articles/PMC3959650/ (visited on 12/06/2022).
[185]
Paolo Frasconi, Marco Gori, and Alberto Tesi. “Successes and failures of backpropagation: A theoretical
investigation”. In: Progress in Neural Networks. Vol. 5. Intellect Books, 1993.
[186]
Carl Benedikt Frey and Michael Osborne. “The Future of Employment: How susceptible are jobs to com-
puterisation?. Oxford Martin School”. In: Oxford University Press (2013). url: https://www.oxfordmartin.
ox.ac.uk/publications/the-future-of-employment/ (visited on 11/26/2022).
[187]
Kunihiko Fukushima. “Cognitron: A self-organizing multilayered neural network”. In: Biological Cyber-
netics 20.3 (1975). Publisher: Springer, pp. 121–136.
[188]
Iason Gabriel. “Artiﬁcial Intelligence, Values, and Alignment”. en. In: Minds and Machines 30.3 (Sept. 2020),
pp. 411–437. issn: 0924-6495, 1572-8641. doi: 10.1007/s11023-020-09539-2. url: https://link.springer.com/
10.1007/s11023-020-09539-2 (visited on 09/30/2022).
[189]
Iason Gabriel and Vafa Ghazavi. The Challenge of Value Alignment: from Fairer Algorithms to AI Safety.
arXiv:2101.06060 [cs]. Jan. 2021. doi: 10.48550/arXiv.2101.06060. url: http://arxiv.org/abs/2101.06060
(visited on 11/22/2022).
[190]
Philip Gage. “A new algorithm for data compression”. In: C Users Journal 12.2 (1994). Publisher: McPherson,
KS: R & D Publications, c1987-1994., pp. 23–38.
[191]
Yarin Gal and Zoubin Ghahramani. “Dropout as a Bayesian Approximation: Representing Model Uncer-
tainty in Deep Learning”. en. In: Proceedings of The 33rd International Conference on Machine Learning.
PMLR, June 2016, pp. 1050–1059. url: https://proceedings.mlr.press/v48/gal16.html (visited on 09/27/2022).
[192]
Deep Ganguli et al. “Predictability and Surprise in Large Generative Models”. In: 2022 ACM Conference on
Fairness, Accountability, and Transparency. arXiv:2202.07785 [cs]. ACM, June 2022, pp. 1747–1764. doi:
10.1145/3531146.3533229. url: http://arxiv.org/abs/2202.07785 (visited on 10/12/2022).
[193]
Ben Garﬁnkel. “The Impact of Artiﬁcial Intelligence: A Historical Perspective”. In: The Oxford Handbook
of AI Governance. Ed. by Justin B. Bullock et al. Oxford University Press, 2022. isbn: 978-0-19-757932-9.
doi: 10.1093/oxfordhb/9780197579329.013.5. url: https://doi.org/10.1093/oxfordhb/9780197579329.013.5
(visited on 01/08/2023).
[194]
Timnit Gebru, Judy Hoﬀman, and Li Fei-Fei. Fine-grained Recognition in the Wild: A Multi-Task Domain
Adaptation Approach. tex.copyright: arXiv.org perpetual, non-exclusive license. 2017. doi: 10.48550/
ARXIV.1709.02476. url: https://arxiv.org/abs/1709.02476.
[195]
Jonas Geiping et al. How Much Data Are Augmentations Worth? An Investigation into Scaling Laws,
Invariance, and Implicit Regularization. tex.copyright: arXiv.org perpetual, non-exclusive license. 2022.
doi: 10.48550/ARXIV.2210.06441. url: https://arxiv.org/abs/2210.06441.
[196]
Andrew Gelman. Google’s problems with reproducibility. 2022. url: https://statmodeling.stat.columbia.
edu/2022/05/03/googles-problems-with-reproducibility/.


--- Page 39 ---

Ten Hard Problems in AI
•
39
[197]
Gemini Team et al. Gemini: A Family of Highly Capable Multimodal Models. arXiv:2312.11805 [cs]. Dec.
2023. doi: 10.48550/arXiv.2312.11805. url: http://arxiv.org/abs/2312.11805 (visited on 01/08/2024).
[198]
Oguzhan Gencoglu et al. HARK Side of Deep Learning – From Grad Student Descent to Automated Machine
Learning. arXiv:1904.07633 [cs]. Apr. 2019. doi: 10.48550/arXiv.1904.07633. url: http://arxiv.org/abs/1904.
07633 (visited on 10/25/2022).
[199]
General Data Protection Regulation (GDPR) – Oﬃcial Legal Text. en-US. url: https://gdpr-info.eu/ (visited
on 12/08/2022).
[200]
Audley Genus and Andy Stirling. “Collingridge and the dilemma of control: Towards responsible and
accountable innovation”. en. In: Research Policy 47.1 (Feb. 2018), pp. 61–69. issn: 0048-7333. doi: 10.1016/j.
respol.2017.09.012. url: https://www.sciencedirect.com/science/article/pii/S0048733317301622 (visited on
12/09/2022).
[201]
Anca Gheaus and Lisa Herzog. “The Goods of Work (Other Than Money!): The Goods of Work”. en. In:
Journal of Social Philosophy 47.1 (Mar. 2016), pp. 70–89. issn: 00472786. doi: 10.1111/josp.12140. url:
https://onlinelibrary.wiley.com/doi/10.1111/josp.12140 (visited on 12/05/2022).
[202]
Charlie Giattino, Esteban Ortiz-Ospina, and Max Roser. “Working Hours”. In: Our World in Data (Dec.
2020). url: https://ourworldindata.org/working-hours (visited on 12/01/2022).
[203]
Yolanda Gil and Bart Selman. A 20-Year Community Roadmap for Artiﬁcial Intelligence Research in the US.
arXiv:1908.02624 [cs]. Aug. 2019. doi: 10.48550/arXiv.1908.02624. url: http://arxiv.org/abs/1908.02624
(visited on 12/06/2022).
[204]
Amelia Glaese. “Improving alignment of dialogue agents via targeted human judgements”. In: Google AI
(2022). url: https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/
sparrow-ﬁnal.pdf.
[205]
Tobias Glasmachers. “Limits of end-to-end learning”. In: Asian Conference on Machine Learning. 2017,
pp. 17–32.
[206]
Xavier Glorot and Yoshua Bengio. “Understanding the diﬃculty of training deep feedforward neural
networks”. In: Proceedings of the Thirteenth International Conference on Artiﬁcial Intelligence and Statistics.
tex.organization: JMLR Workshop and Conference Proceedings. 2010, pp. 249–256.
[207]
Xavier Glorot, Antoine Bordes, and Yoshua Bengio. “Deep sparse rectiﬁer neural networks”. In: Proceedings
of the Fourteenth International Conference on Artiﬁcial Intelligence and Statistics. tex.organization: JMLR
Workshop and Conference Proceedings. 2011, pp. 315–323.
[208]
Harshvardhan Gm et al. “A comprehensive survey and analysis of generative models in machine learning”.
en. In: Computer Science Review 38 (Nov. 2020), p. 100285. issn: 1574-0137. doi: 10.1016/j.cosrev.2020.100285.
url: https://www.sciencedirect.com/science/article/pii/S1574013720303853.
[209]
Fernand Gobet and Giovanni Sala. “How Artiﬁcial Intelligence Can Help Us Understand Human Creativity”.
In: Frontiers in Psychology 10 (2019). issn: 1664-1078. url: https://www.frontiersin.org/articles/10.3389/
fpsyg.2019.01401 (visited on 12/01/2022).
[210]
Michael Gofman and Zhao Jin. Artiﬁcial Intelligence, Education, and Entrepreneurship. en. SSRN Scholarly
Paper. Rochester, NY, July 2022. doi: 10.2139/ssrn.3449440. url: https://papers.ssrn.com/abstract=3449440
(visited on 10/27/2022).
[211]
Irving John Good. “Speculations Concerning the First Ultraintelligent Machine”. In: ed. by Franz L. Alt
and Morris Rubinoﬀ. Vol. 6. Advances in Computers. ISSN: 0065-2458. Elsevier, 1966, pp. 31–88. doi:
https://doi.org/10.1016/S0065-2458(08)60418-0. url: https://www.sciencedirect.com/science/article/pii/
S0065245808604180.
[212]
Google Diversity Annual Report 2022. Tech. rep. Google, 2022.


--- Page 40 ---

40
•
Leech et al.
[213]
John-Stewart Gordon and Ausrine Pasvenskiene. “Human rights for robots? A literature review”. In:
AI and Ethics 1.4 (Nov. 2021), pp. 579–591. issn: 2730-5961. doi: 10.1007/s43681-021-00050-7. url:
https://doi.org/10.1007/s43681-021-00050-7 (visited on 09/23/2022).
[214]
Erich Grünewald. Attention on Existential Risk from AI Likely Hasn’t Distracted from Current Harms from
AI. en. Dec. 2023. url: https://www.erichgrunewald.com/posts/attention-on-existential-risk-from-ai-
likely-hasnt-distracted-from-current-harms-from-ai/ (visited on 01/08/2024).
[215]
David J Gunkel. Robot Rights. MIT Press, 2018.
[216]
Chuan Guo et al. On Calibration of Modern Neural Networks. arXiv:1706.04599 [cs]. Aug. 2017. doi:
10.48550/arXiv.1706.04599. url: http://arxiv.org/abs/1706.04599 (visited on 09/29/2022).
[217]
Yanming Guo et al. “Deep learning for visual understanding: A review”. In: Neurocomputing 187 (2016),
pp. 27–48. issn: 0925-2312. doi: https://doi.org/10.1016/j.neucom.2015.09.116. url: https://www.
sciencedirect.com/science/article/pii/S0925231215017634.
[218]
Dylan Hadﬁeld-Menell et al. The Oﬀ-Switch Game. arXiv:1611.08219 [cs]. June 2017. doi: 10.48550/arXiv.
1611.08219. url: http://arxiv.org/abs/1611.08219 (visited on 09/29/2022).
[219]
Danijar Hafner et al. Dream to Control: Learning Behaviors by Latent Imagination. arXiv:1912.01603 [cs].
Mar. 2020. doi: 10.48550/arXiv.1912.01603. url: http://arxiv.org/abs/1912.01603 (visited on 11/26/2022).
[220]
Thilo Hagendorﬀ. “AI ethics and its pitfalls: not living up to its own standards?” en. In: AI and Ethics (May
2022). issn: 2730-5961. doi: 10.1007/s43681-022-00173-5. url: https://doi.org/10.1007/s43681-022-00173-5
(visited on 11/29/2022).
[221]
Thilo Hagendorﬀ. “The Ethics of AI Ethics: An Evaluation of Guidelines”. en. In: Minds and Machines 30.1
(Mar. 2020), pp. 99–120. issn: 1572-8641. doi: 10.1007/s11023-020-09517-8. url: https://doi.org/10.1007/
s11023-020-09517-8 (visited on 09/23/2022).
[222]
Thilo Hagendorﬀand Kristof Meding. “Ethical considerations and statistical analysis of industry involve-
ment in machine learning research”. en. In: AI & Society (Sept. 2021). issn: 1435-5655. doi: 10.1007/s00146-
021-01284-z. url: https://doi.org/10.1007/s00146-021-01284-z (visited on 12/07/2022).
[223]
John Storrs Hall. “Self-improving AI: an Analysis”. In: Minds and Machines 17.3 (Oct. 2007), pp. 249–259.
issn: 1572-8641. doi: 10.1007/s11023-007-9065-3. url: https://doi.org/10.1007/s11023-007-9065-3 (visited
on 11/27/2022).
[224]
Patrick Haluptzok, Matthew Bowers, and Adam Tauman Kalai. Language Models Can Teach Themselves to
Program Better. tex.copyright: arXiv.org perpetual, non-exclusive license. 2022. doi: 10.48550/ARXIV.2207.
14502. url: https://arxiv.org/abs/2207.14502.
[225]
Chi Han et al. Explaining Emergent In-Context Learning as Kernel Regression. arXiv:2305.12766 [cs]. Oct.
2023. doi: 10.48550/arXiv.2305.12766. url: http://arxiv.org/abs/2305.12766 (visited on 01/08/2024).
[226]
Justin Haner and Denise Garcia. “The Artiﬁcial Intelligence Arms Race: Trends and World Leaders in
Autonomous Weapons Development”. en. In: Global Policy 10.3 (2019), pp. 331–337. issn: 1758-5899. doi:
10.1111/1758-5899.12713. url: https://onlinelibrary.wiley.com/doi/abs/10.1111/1758-5899.12713 (visited
on 10/08/2019).
[227]
Awni Hannun et al. Deep Speech: Scaling up end-to-end speech recognition. arXiv:1412.5567 [cs]. Dec. 2014.
doi: 10.48550/arXiv.1412.5567. url: http://arxiv.org/abs/1412.5567 (visited on 12/06/2022).
[228]
Karen Hao and Andrea Paola Hernandez. “How the AI industry proﬁts from catastrophe”. en. In: MIT
Technology Review (Apr. 2022). url: https://www.technologyreview.com/2022/04/20/1050392/ai-industry-
appen-scale-data-labels/ (visited on 03/22/2023).
[229]
Rebecca Hasdell. What We Know About Universal Basic Income. 2020.
[230]
Demis Hassabis. AlphaFold reveals the structure of the protein universe. en. 2022. url: https://www.
deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe (visited on 12/07/2022).


--- Page 41 ---

Ten Hard Problems in AI
•
41
[231]
Haydn Belﬁeld and Shin-Shin Hua. Compute and Antitrust. de-DE. 2022. url: https://verfassungsblog.de/
compute-and-antitrust/ (visited on 01/11/2023).
[232]
Kaiming He et al. Delving Deep into Rectiﬁers: Surpassing Human-Level Performance on ImageNet Classiﬁca-
tion. arXiv:1502.01852 [cs]. Feb. 2015. doi: 10.48550/arXiv.1502.01852. url: http://arxiv.org/abs/1502.01852
(visited on 11/21/2022).
[233]
Kaiming He et al. “ResNet - Deep Residual Learning for Image Recognition”. In: 2016 IEEE Conference
on Computer Vision and Pattern Recognition (CVPR). ISSN: 1063-6919. IEEE, June 2016, pp. 770–778. doi:
10.1109/CVPR.2016.90.
[234]
Laurence R. Helfer and Molly K. Land. The Meta Oversight Board’s Human Rights Future. en. SSRN Scholarly
Paper. Rochester, NY, Aug. 2022. doi: 10.2139/ssrn.4197107. url: https://papers.ssrn.com/abstract=4197107
(visited on 01/11/2023).
[235]
Dan Hendrycks and Thomas Dietterich. Benchmarking Neural Network Robustness to Common Corruptions
and Perturbations. arXiv:1903.12261 [cs, stat]. Mar. 2019. doi: 10.48550/arXiv.1903.12261. url: http:
//arxiv.org/abs/1903.12261 (visited on 11/30/2022).
[236]
Dan Hendrycks and Kevin Gimpel. Gaussian Error Linear Units (GELUs). tex.copyright: arXiv.org perpetual,
non-exclusive license. 2016. doi: 10.48550/ARXIV.1606.08415. url: https://arxiv.org/abs/1606.08415.
[237]
Dan Hendrycks, Mantas Mazeika, and Thomas Dietterich. “Deep anomaly detection with outlier exposure”.
In: arXiv (2018).
[238]
Dan Hendrycks et al. Unsolved Problems in ML Safety. arXiv:2109.13916 [cs]. June 2022. doi: 10.48550/
arXiv.2109.13916. url: http://arxiv.org/abs/2109.13916 (visited on 09/29/2022).
[239]
Daniela Hernandez and Ted Greenwald. IBM Has a Watson Dilemma. 2018. url: https://www.wsj.com/
articles/ibm-bet-billions-that-watson-could-improve-cancer-treatment-it-hasnt-worked-1533961147.
[240]
Ashley van Heteren et al. Applying AI for social good. 2018. url: https://www.mckinsey.com/featured-
insights/artiﬁcial-intelligence/applying-artiﬁcial-intelligence-for-social-good (visited on 12/06/2022).
[241]
Wilbur H Highleyman. “Linear decision functions, with application to pattern recognition”. In: Proceedings
of the IRE 50.6 (1962). Publisher: IEEE, pp. 1501–1514.
[242]
Salah Hihi and Yoshua Bengio. “Hierarchical Recurrent Neural Networks for Long-Term Dependencies”.
In: Advances in Neural Information Processing Systems. Ed. by D. Touretzky, M.C. Mozer, and M. Hasselmo.
Vol. 8. MIT Press, 1995.
[243]
Geoﬀrey E Hinton, Simon Osindero, and Yee-Whye Teh. “A fast learning algorithm for deep belief nets”.
In: MIT Press 18.7 (2006). Publisher: MIT Press One Rogers Street, Cambridge, MA 02142-1209, USA
journals-info ..., pp. 1527–1554.
[244]
Geoﬀrey E. Hinton et al. Improving neural networks by preventing co-adaptation of feature detectors.
tex.copyright: arXiv.org perpetual, non-exclusive license. 2012. doi: 10.48550/ARXIV.1207.0580. url:
https://arxiv.org/abs/1207.0580.
[245]
Torsten Hoeﬂer et al. Sparsity in Deep Learning: Pruning and growth for eﬃcient inference and training in
neural networks. tex.copyright: arXiv.org perpetual, non-exclusive license. 2021. doi: 10.48550/ARXIV.
2102.00554. url: https://arxiv.org/abs/2102.00554.
[246]
Jordan Hoﬀmann et al. Chinchilla - Training Compute-Optimal Large Language Models. arXiv:2203.15556
[cs]. Mar. 2022. doi: 10.48550/arXiv.2203.15556. url: http://arxiv.org/abs/2203.15556 (visited on
09/23/2022).
[247]
Lara Hoﬀmann and Clemens Elster. “Deep ensembles from a Bayesian perspective”. In: arXiv (2021).
eprint: 2105.13283.
[248]
Helena Hollis and Jess Whittlestone. Participatory AI futures: lessons from research in climate change. en.
Aug. 2021. url: https://medium.com/@helena.hollis.14/participatory-ai-futures-lessons-from-research-
in-climate-change-34e3580553f8 (visited on 08/25/2021).


--- Page 42 ---

42
•
Leech et al.
[249]
Sara Hooker. “The hardware lottery”. In: Communications of the ACM 64.12 (2021). Publisher: ACM New
York, NY, USA, pp. 58–65.
[250]
Michael C. Horowitz. “Do Emerging Military Technologies Matter for International Politics?” en. In: Annual
Review of Political Science 23.1 (May 2020), pp. 385–400. issn: 1094-2939, 1545-1577. doi: 10.1146/annurev-
polisci-050718-032725. url: https://www.annualreviews.org/doi/10.1146/annurev-polisci-050718-032725
(visited on 01/06/2023).
[251]
Michael C. Horowitz, Paul Scharre, and Alexander Velez-Green. “A Stable Nuclear Future? The Impact
of Autonomous Systems and Artiﬁcial Intelligence”. In: arXiv (Dec. 2019). arXiv: 1912.05291. url: http:
//arxiv.org/abs/1912.05291 (visited on 12/18/2019).
[252]
Georgia Wells Horwitz Deepa Seetharaman and Jeﬀ. “Is Facebook Bad for You? It Is for About 360
Million Users, Company Surveys Suggest”. en-US. In: Wall Street Journal (Nov. 2021). issn: 0099-9660. url:
https://www.wsj.com/articles/facebook-bad-for-you-360-million-users-say-yes-company-documents-
facebook-ﬁles-11636124681 (visited on 12/06/2022).
[253]
Xiaojing Hou, Ruichang Li, and Zhiping Song. “A Bibliometric Analysis of Wicked Problems: From Single
Discipline to Transdisciplinarity”. en. In: Fudan Journal of the Humanities and Social Sciences 15.3 (Sept.
2022), pp. 299–329. issn: 2198-2600. doi: 10.1007/s40647-022-00346-w. url: https://doi.org/10.1007/s40647-
022-00346-w (visited on 11/16/2022).
[254]
Jeremy Howard and Sebastian Ruder. Universal Language Model Fine-tuning for Text Classiﬁcation.
arXiv:1801.06146 [cs, stat]. May 2018. doi: 10.48550/arXiv.1801.06146. url: http://arxiv.org/abs/1801.06146
(visited on 09/22/2022).
[255]
Zhiting Hu and Eric P. Xing. “Toward a ’Standard Model’ of Machine Learning”. en. In: Harvard Data
Science Review 4.4 (Oct. 2022). issn: 2644-2353, 2688-8513. doi: 10.1162/99608f92.1d34757b. url: https:
//hdsr.mitpress.mit.edu/pub/zkib7xth/release/2 (visited on 11/28/2022).
[256]
Hsin-Yuan Huang et al. “Provably eﬃcient machine learning for quantum many-body problems”. en. In:
Science 377.6613 (Sept. 2022), eabk3333. issn: 0036-8075, 1095-9203. doi: 10.1126/science.abk3333. url:
https://www.science.org/doi/10.1126/science.abk3333 (visited on 10/02/2022).
[257]
Jiaxin Huang et al. Large Language Models Can Self-Improve. tex.copyright: arXiv.org perpetual, non-
exclusive license. 2022. doi: 10.48550/ARXIV.2210.11610. url: https://arxiv.org/abs/2210.11610.
[258]
Yanping Huang et al. “GPipe: Eﬃcient Training of Giant Neural Networks using Pipeline Parallelism”.
In: Advances in Neural Information Processing Systems. Vol. 32. Curran Associates, Inc., 2019. url: https:
//papers.nips.cc/paper/2019/hash/093f65e080a295f8076b1c5722a46aa2- Abstract.html (visited on
11/04/2022).
[259]
Evan Hubinger. How likely is deceptive alignment? en. 2022. url: https://www.alignmentforum.org/posts/
A9NxPTwbw6r6Awuwt/how-likely-is-deceptive-alignment (visited on 12/01/2022).
[260]
Evan Hubinger et al. Risks from Learned Optimization in Advanced Machine Learning Systems. arXiv:1906.01820
[cs]. Dec. 2021. doi: 10.48550/arXiv.1906.01820. url: http://arxiv.org/abs/1906.01820 (visited on 11/28/2022).
[261]
Humberto Maturana Romesin and Pille Bunnell. “Biosphere, homosphere, and robosphere: What has
this to do with business?” In: Society for Organizational Learning Member’s Meeting (1998). url: https:
//reﬂexus.org/wp-content/uploads/Biosphere.pdf.
[262]
David Humphreys et al. “Advancing Fusion with Machine Learning Research Needs Workshop Report”. en.
In: Journal of Fusion Energy 39.4 (Aug. 2020), pp. 123–155. issn: 1572-9591. doi: 10.1007/s10894-020-00258-1.
url: https://doi.org/10.1007/s10894-020-00258-1 (visited on 10/13/2022).
[263]
Frank Hutter and Marius Lindauer. AutoML. 2022. url: https://www.automl.org/.
[264]
AI Impacts. 2017 trend in the cost of computing. 2017. url: https://aiimpacts.org/recent-trend-in-the-cost-
of-computing/.


--- Page 43 ---

Ten Hard Problems in AI
•
43
[265]
AI Impacts. Trends in the cost of computing. 2015. url: https://aiimpacts.org/trends-in-the-cost-of-
computing/.
[266]
Sergey Ioﬀe and Christian Szegedy. “Batch Normalization: Accelerating Deep Network Training by
Reducing Internal Covariate Shift”. en. In: Proceedings of the 32nd International Conference on Machine
Learning. PMLR, June 2015, pp. 448–456. url: https://proceedings.mlr.press/v37/ioﬀe15.html (visited on
09/29/2022).
[267]
Geoﬀrey Irving and Amanda Askell. “AI Safety Needs Social Scientists”. en. In: Distill 4.2 (Feb. 2019), e14.
issn: 2476-0757. doi: 10.23915/distill.00014. url: https://distill.pub/2019/safety-needs-social-scientists
(visited on 11/28/2022).
[268]
Robert Jackall. “Moral Mazes”. en. In: Wiley Encyclopedia of Management. Ed. by Cary L Cooper. Chichester,
UK: John Wiley & Sons, Ltd, Jan. 2015, pp. 1–2. isbn: 978-1-118-78531-7. doi: 10.1002/9781118785317.
weom020150. url: https://onlinelibrary.wiley.com/doi/10.1002/9781118785317.weom020150 (visited on
12/06/2022).
[269]
Andrew Jaegle et al. Perceiver: General Perception with Iterative Attention. tex.copyright: arXiv.org perpetual,
non-exclusive license. 2021. doi: 10.48550/ARXIV.2103.03206. url: https://arxiv.org/abs/2103.03206.
[270]
James Manyika. AI2050’s Hard Problems Working List. url: https://www.schmidtfutures.com/our-
work/ai2050/ai2050-hard-problems-working-list/.
[271]
Eric Jang. Just Ask for Generalization. Oct. 2021. url: https://evjang.com/2021/10/23/generalization.html
(visited on 10/13/2022).
[272]
Francisco Javier Lopez Frias and José Luis Pérez Triviño. “Will robots ever play sports?” en. In: Sport, Ethics
and Philosophy 10.1 (Jan. 2016), pp. 67–82. issn: 1751-1321, 1751-133X. doi: 10.1080/17511321.2016.1166393.
url: https://www.tandfonline.com/doi/full/10.1080/17511321.2016.1166393 (visited on 12/05/2022).
[273]
Jennifer L. Jennings and Jonathan Marc Bearak. ““Teaching to the Test” in the NCLB Era: How Test
Predictability Aﬀects Our Understanding of Student Performance”. en. In: Educational Researcher 43.8
(Nov. 2014). Publisher: American Educational Research Association, pp. 381–389. issn: 0013-189X. doi:
10.3102/0013189X14554449. url: https://doi.org/10.3102/0013189X14554449 (visited on 12/06/2022).
[274]
Anna Jobin, Marcello Ienca, and Eﬀy Vayena. “The global landscape of AI ethics guidelines”. en. In:
Nature 1.9 (Sept. 2019), pp. 389–399. issn: 2522-5839. doi: 10.1038/s42256- 019- 0088- 2. url: https:
//www.nature.com/articles/s42256-019-0088-2 (visited on 12/09/2022).
[275]
James Johnson. “Inadvertent escalation in the age of intelligence machines: A new model for nuclear
risk in the digital age”. en. In: European Journal of International Security (Oct. 2021). Publisher: Cam-
bridge University Press, pp. 1–23. issn: 2057-5637, 2057-5645. doi: 10.1017/eis.2021.23. url: https:
//www.cambridge.org/core/journals/european-journal-of-international-security/article/inadvertent-
escalation-in-the-age-of-intelligence-machines-a-new- model- for- nuclear- risk- in- the- digital-
age/D1F1FC47D12FA4DCB12D1648412B696B (visited on 10/15/2021).
[276]
James Johnson. “The AI-cyber nexus: implications for military escalation, deterrence and strategic sta-
bility”. en. In: Journal of Cyber Policy (Dec. 2019). Publisher: Routledge. issn: 2373-8871. url: https:
//www.tandfonline.com/doi/full/10.1080/23738871.2019.1701693 (visited on 01/03/2022).
[277]
John Jumper et al. “Highly accurate protein structure prediction with AlphaFold”. In: Nature 596.7873
(2021). Publisher: Nature Publishing Group, pp. 583–589.
[278]
Roman Jurowetzki et al. The Privatization of AI Research(-ers): Causes and Potential Consequences – From
university-industry interaction to public research brain-drain? arXiv:2102.01648 [cs]. Feb. 2021. doi: 10.
48550/arXiv.2102.01648. url: http://arxiv.org/abs/2102.01648 (visited on 09/19/2022).
[279]
Saurav Kadavath et al. “Language Models (Mostly) Know What They Know”. en. In: arXiv (July 2022).
doi: 10.48550/arXiv.2207.05221. url: https://arxiv.org/abs/2207.05221v4 (visited on 11/28/2022).


--- Page 44 ---

44
•
Leech et al.
[280]
Jeremy Kahn. Lessons from DeepMind’s breakthrough in protein-folding A.I. 2020. url: https://fortune.com/
2020/12/01/lessons-from-deepminds-a-i-breakthrough-eye-on-ai.
[281]
Peter Kairouz et al. Advances and Open Problems in Federated Learning. arXiv:1912.04977 [cs, stat]. Mar.
2021. doi: 10.48550/arXiv.1912.04977. url: http://arxiv.org/abs/1912.04977 (visited on 12/08/2022).
[282]
Yogesh Kalakoti, Shashank Yadav, and Durai Sundar. “TransDTI: Transformer-Based Language Models
for Estimating DTIs and Building a Drug Recommendation Workﬂow”. en. In: ACS Omega 7.3 (Jan. 2022),
pp. 2706–2717. issn: 2470-1343, 2470-1343. doi: 10.1021/acsomega.1c05203. url: https://pubs.acs.org/doi/
10.1021/acsomega.1c05203 (visited on 11/30/2022).
[283]
Andreas Kaplan and Michael Haenlein. “Rulers of the world, unite! The challenges and opportunities
of artiﬁcial intelligence”. en. In: Business Horizons 63.1 (Jan. 2020), pp. 37–50. issn: 0007-6813. doi:
10.1016/j.bushor.2019.09.003. url: https://www.sciencedirect.com/science/article/pii/S0007681319301260
(visited on 12/27/2022).
[284]
Jared Kaplan et al. Scaling Laws for Neural Language Models. arXiv:2001.08361 [cs, stat]. Jan. 2020. doi:
10.48550/arXiv.2001.08361. url: http://arxiv.org/abs/2001.08361 (visited on 09/27/2022).
[285]
Md. Rezaul Karim et al. Interpreting Black-box Machine Learning Models for High Dimensional Datasets.
tex.copyright: Creative Commons Attribution Non Commercial No Derivatives 4.0 International. 2022.
doi: 10.48550/ARXIV.2208.13405. url: https://arxiv.org/abs/2208.13405.
[286]
Kate Crawford and Vladan Joler. Anatomy of an AI System. en. 2018. url: http://www.anatomyof.ai
(visited on 12/06/2022).
[287]
Elia Kaufmann et al. “Champion-level drone racing using deep reinforcement learning”. en. In: Nature
620.7976 (Aug. 2023), pp. 982–987. issn: 1476-4687. doi: 10.1038/s41586- 023- 06419- 4. url: https:
//www.nature.com/articles/s41586-023-06419-4 (visited on 01/08/2024).
[288]
Keith E. Sonderling, Bradford J. Kelley, and Lance Casimir. “The Promise and The Peril: Artiﬁcial Intelli-
gence and Employment Discrimination”. In: University of Miami Law Review 77.1 (Nov. 2022), p. 88. url:
https://repository.law.miami.edu/cgi/viewcontent.cgi?article=4692&context=umlr.
[289]
Kelly Kang. Doctorate Recipients from U.S. Universities: 2021. Tech. rep. National Science Foundation, 2021.
url: https://ncses.nsf.gov/pubs/nsf23300/data-tables (visited on 12/08/2022).
[290]
John Maynard Keynes. “Economic Possibilities for our Grandchildren (1930)”. In: Essays in Persuasion.
tex.lastaccessed: September 11, 2022. New York: W. W. Norton & Co, 1963, pp. 358–373. url: http:
//www.econ.yale.edu/smith/econ116a/keynes1.pdf.
[291]
Saif Khan. The Semiconductor Supply Chain. en-US. 2021. url: https://cset.georgetown.edu/publication/the-
semiconductor-supply-chain/ (visited on 12/27/2022).
[292]
Douwe Kiela et al. Dynabench: Rethinking Benchmarking in NLP. arXiv:2104.14337 [cs]. Apr. 2021. doi:
10.48550/arXiv.2104.14337. url: http://arxiv.org/abs/2104.14337 (visited on 12/01/2022).
[293]
Thomas C. King et al. “Artiﬁcial Intelligence Crime: An Interdisciplinary Analysis of Foreseeable Threats
and Solutions”. In: Science and Engineering Ethics 26.1 (2020), pp. 89–120. issn: 1353-3452. doi: 10.1007/
s11948- 018- 00081- 0. url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6978427/ (visited on
11/29/2022).
[294]
Diederik P Kingma and Jimmy Ba. “Adam: A method for stochastic optimization”. In: arXiv (2014).
[295]
Jan Hendrik Kirchner. Compute Governance: The Role of Commodity Hardware. Substack newsletter. Mar.
2022. url: https://universalprior.substack.com/p/compute-governance-the-role-of-commodity (visited on
12/27/2022).
[296]
Henry A. Kissinger et al. The Age of AI: And Our Human Future. en. Google-Books-ID: PrEhzgEACAAJ.
Little Brown, 2021. isbn: 978-0-316-27380-0.
[297]
Joel Klinger, Juan Mateos-Garcia, and Konstantinos Stathoulopoulos. A narrowing of AI research? arXiv:2009.10385
[cs]. Jan. 2022. doi: 10.48550/arXiv.2009.10385. url: http://arxiv.org/abs/2009.10385 (visited on 09/19/2022).


--- Page 45 ---

Ten Hard Problems in AI
•
45
[298]
Will Knight. Russia’s Killer Drone in Ukraine Raises Fears About AI in Warfare. 2022. url: https://www.
wired.com/story/ai-drones-russia-ukraine/.
[299]
Alina Köchling and Marius Claus Wehner. “Discriminated by an algorithm: a systematic review of
discrimination and fairness by algorithmic decision-making in the context of HR recruitment and HR
development”. In: Business Research 13.3 (2020). Publisher: Springer, pp. 795–848.
[300]
Jakub Konečný et al. Federated Learning: Strategies for Improving Communication Eﬃciency. arXiv:1610.05492
[cs]. Oct. 2017. doi: 10.48550/arXiv.1610.05492. url: http://arxiv.org/abs/1610.05492 (visited on 12/08/2022).
[301]
Anton Korinek. Language Models and Cognitive Automation for Economic Research. Working Paper. Feb.
2023. doi: 10.3386/w30957. url: https://www.nber.org/papers/w30957 (visited on 01/08/2024).
[302]
Anton Korinek and Megan Juelfs. Preparing for the (non-existent?) future of work. Tech. rep. National
Bureau of Economic Research, 2022.
[303]
Anton Korinek and Joseph E. Stiglitz. Artiﬁcial Intelligence, Globalization, and Strategies for Economic
Development. Working Paper. Feb. 2021. doi: 10.3386/w28453. url: https://www.nber.org/papers/w28453
(visited on 09/15/2022).
[304]
Rick Korzekwa. Time for AI to cross the human performance range in ImageNet image classiﬁcation. Oct.
2020. url: https://aiimpacts.org/time-for-ai-to-cross-the-human-performance-range-in-imagenet-image-
classiﬁcation/.
[305]
Victoria Krakovna et al. Speciﬁcation gaming: the ﬂip side of AI ingenuity. en. 2020. url: https://www.
deepmind.com/blog/speciﬁcation-gaming-the-ﬂip-side-of-ai-ingenuity (visited on 11/28/2022).
[306]
Stefan Krastanov and Liang Jiang. “Deep Neural Network Probabilistic Decoder for Stabilizer Codes”.
en. In: Scientiﬁc Reports 7.1 (Dec. 2017), p. 11003. issn: 2045-2322. doi: 10.1038/s41598-017-11266-1. url:
http://www.nature.com/articles/s41598-017-11266-1 (visited on 10/03/2022).
[307]
Mario Krenn et al. Artiﬁcial Intelligence and Machine Learning for Quantum Technologies. arXiv:2208.03836
[quant-ph]. Aug. 2022. doi: 10.48550/arXiv.2208.03836. url: http://arxiv.org/abs/2208.03836 (visited on
09/23/2022).
[308]
Mario Krenn et al. On scientiﬁc understanding with artiﬁcial intelligence. arXiv:2204.01467 [physics]. Apr.
2022. doi: 10.48550/arXiv.2204.01467. url: http://arxiv.org/abs/2204.01467 (visited on 09/23/2022).
[309]
Peter Kriens and Tim Verbelen. “What Machine Learning Can Learn From Software Modularity”. In:
Computer 55.9 (2022), pp. 35–42. doi: 10.1109/MC.2022.3160276.
[310]
Alex Krizhevsky, Ilya Sutskever, and Geoﬀrey E Hinton. “ImageNet Classiﬁcation with Deep Convolutional
Neural Networks”. In: Advances in Neural Information Processing Systems. Vol. 25. Curran Associates, Inc.,
2012. url: https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
(visited on 09/29/2022).
[311]
Niklas Kühl et al. Human vs. supervised machine learning: Who learns patterns faster? tex.copyright:
Creative Commons Attribution Non Commercial No Derivatives 4.0 International. 2020. doi: 10.48550/
ARXIV.2012.03661. url: https://arxiv.org/abs/2012.03661.
[312]
Aviral Kumar et al. Data-Driven Oﬄine Optimization For Architecting Hardware Accelerators. tex.copyright:
Creative Commons Attribution 4.0 International. 2021. doi: 10.48550/ARXIV.2110.11346. url: https:
//arxiv.org/abs/2110.11346.
[313]
Johnny Kung. A Culture of Ethical AI. en-US. Mar. 2021. url: https://cifar.ca/cifarnews/2021/03/25/a-
culture-of-ethical-ai/ (visited on 01/11/2023).
[314]
Andrey Kurenkov. Lessons from the GPT-4Chan Controversy. en. June 2022. url: https://thegradient.pub/
gpt-4chan-lessons/ (visited on 11/29/2022).
[315]
Ray Kurzweil. Age of Spiritual Machines: When Computers Exceed Human Intelligence. 1st. USA: Penguin
USA, 1999. isbn: 978-0-14-028202-3.


--- Page 46 ---

46
•
Leech et al.
[316]
Ernst Kussul and Tatiana Baidyk. “Improved method of handwritten digit recognition tested on MNIST
database”. In: Image and Vision Computing 22.12 (2004). Publisher: Elsevier, pp. 971–981.
[317]
Maciej Kuziemski and Gianluca Misuraca. “AI governance in the public sector: Three tales from the
frontiers of automated decision-making in democratic settings”. en. In: Telecommunications Policy. Artiﬁ-
cial intelligence, economy and society 44.6 (July 2020), p. 101976. issn: 0308-5961. doi: 10.1016/j.telpol.
2020.101976. url: https://www.sciencedirect.com/science/article/pii/S0308596120300689 (visited on
12/01/2022).
[318]
Jonathan Kwik. “Mitigating the Risk of Autonomous-Weapon Misuse by Insurgent Groups”. en. In: Laws
12.1 (Feb. 2023). Number: 1 Publisher: Multidisciplinary Digital Publishing Institute, p. 5. issn: 2075-471X.
doi: 10.3390/laws12010005. url: https://www.mdpi.com/2075-471X/12/1/5 (visited on 01/08/2023).
[319]
Michael Lachanski and Steven Pav. “Shy of the Character Limit: "Twitter Mood Predicts the Stock Market"
Revisited”. en. In: Econ Journal Watch 14.3 (2017), pp. 302–345. url: https://ideas.repec.org/a/ejw/journl/
v14y2017i3p302-345.html (visited on 12/08/2022).
[320]
Alexandra Lamont. “University students’ strong experiences of music: Pleasure, engagement, and mean-
ing”. en. In: Musicae Scientiae 15.2 (July 2011), pp. 229–249. issn: 1029-8649, 2045-4147. doi: 10.1177/
1029864911403368. url: http://journals.sagepub.com/doi/10.1177/1029864911403368 (visited on
12/05/2022).
[321]
Guillaume Lample and François Charton. Deep Learning for Symbolic Mathematics. tex.copyright: arXiv.org
perpetual, non-exclusive license. 2019. doi: 10.48550/ARXIV.1912.01412. url: https://arxiv.org/abs/1912.
01412.
[322]
Eric D. Langlois and Tom Everitt. “How RL Agents Behave When Their Actions Are Modiﬁed”. en. In:
Proceedings of the AAAI Conference on Artiﬁcial Intelligence 35.13 (May 2021), pp. 11586–11594. issn:
2374-3468. doi: 10.1609/aaai.v35i13.17378. url: https://ojs.aaai.org/index.php/AAAI/article/view/17378
(visited on 12/10/2022).
[323]
Lauro Langosco Di Langosco et al. “Goal Misgeneralization in Deep Reinforcement Learning”. en. In:
Proceedings of the 39th International Conference on Machine Learning. PMLR, June 2022, pp. 12004–12019.
url: https://proceedings.mlr.press/v162/langosco22a.html (visited on 09/30/2022).
[324]
Marjolein Lanzing. ““Strongly Recommended” Revisiting Decisional Privacy to Judge Hypernudging
in Self-Tracking Technologies”. en. In: Philosophy & Technology 32.3 (Sept. 2019), pp. 549–568. issn:
2210-5441. doi: 10.1007/s13347-018-0316-4. url: https://doi.org/10.1007/s13347-018-0316-4 (visited on
11/26/2022).
[325]
Pedro Larrañaga et al. Industrial Applications of Machine Learning. Boca Raton: CRC Press, Dec. 2018.
isbn: 9781351128384. doi: 10.1201/9781351128384.
[326]
Benjamin Cedric Larsen. The geopolitics of AI and the rise of digital sovereignty. en-US. Dec. 2022. url:
https://www.brookings.edu/research/the-geopolitics-of-ai-and-the-rise-of-digital-sovereignty/ (visited
on 12/11/2022).
[327]
Michael Laskin et al. “In-context Reinforcement Learning with Algorithm Distillation”. In: arXiv (2022).
[328]
Johann Laux, Sandra Wachter, and Brent Mittelstadt. “Taming the few: Platform regulation, independent
audits, and the risks of capture created by the DMA and DSA”. en. In: Computer Law & Security Review 43
(Nov. 2021), p. 105613. issn: 0267-3649. doi: 10.1016/j.clsr.2021.105613. url: https://www.sciencedirect.
com/science/article/pii/S0267364921000868 (visited on 12/11/2022).
[329]
Yann LeCun, Yoshua Bengio, and Geoﬀrey Hinton. “Deep learning”. en. In: Nature 521.7553 (May 2015),
pp. 436–444. issn: 0028-0836, 1476-4687. doi: 10.1038/nature14539. url: http://www.nature.com/articles/
nature14539.
[330]
Yann LeCun et al. “Handwritten digit recognition with a back-propagation network”. In: Advances in
Neural Information Processing Systems 2 (1989).


--- Page 47 ---

Ten Hard Problems in AI
•
47
[331]
Gavin Leech. AI ethics for present & future. 2020. url: https://www.gleech.org/ai-ethics.
[332]
Gavin Leech and Stag Lynn. Shallow review of live agendas in alignment & safety. en. Nov. 2023. url:
https://www.alignmentforum.org/posts/zaaGsFBeDTpCsYHef/shallow-review-of-live-agendas-in-
alignment-and-safety (visited on 01/08/2024).
[333]
Joel Lehman et al. The Surprising Creativity of Digital Evolution: A Collection of Anecdotes from the
Evolutionary Computation and Artiﬁcial Life Research Communities. tex.copyright: arXiv.org perpetual,
non-exclusive license. 2018. doi: 10.48550/ARXIV.1803.03453. url: https://arxiv.org/abs/1803.03453.
[334]
Jan Leike. A minimal viable product for alignment. Substack newsletter. Mar. 2022. url: https://aligned.
substack.com/p/alignment-mvp (visited on 11/28/2022).
[335]
Jan Leike. Our approach to alignment research. en. Aug. 2022. url: https://openai.com/blog/our-approach-
to-alignment-research/ (visited on 10/03/2022).
[336]
Jan Leike. Unfortunately trying to improve the API. en-GB. 2022. url: https://twitter.com/janleike/status/
1597785614950141952 (visited on 11/30/2022).
[337]
Jan Leike. What is inner alignment? Substack newsletter. May 2022. url: https://aligned.substack.com/p/
inner-alignment (visited on 12/05/2022).
[338]
Jan Leike. Why I’m excited about AI-assisted human feedback. Substack newsletter. Mar. 2022. url: https:
//aligned.substack.com/p/ai-assisted-human-feedback (visited on 11/28/2022).
[339]
Jan Leike et al. AI Safety Gridworlds. arXiv:1711.09883 [cs]. Nov. 2017. doi: 10.48550/arXiv.1711.09883.
url: http://arxiv.org/abs/1711.09883 (visited on 11/28/2022).
[340]
Jan Leike et al. “Scalable agent alignment via reward modeling: a research direction”. en. In: arXiv (Nov.
2018). doi: 10.48550/arXiv.1811.07871. url: https://arxiv.org/abs/1811.07871v1 (visited on 11/28/2022).
[341]
Nancy G. Leveson. Engineering a Safer World: Systems Thinking Applied to Safety. en. Google-Books-ID:
fA38DwAAQBAJ. MIT Press, Dec. 2016. isbn: 9780262533690.
[342]
Sarah Lewis. “The Racial Bias Built Into Photography”. en-US. In: The New York Times (Apr. 2019). issn:
0362-4331. url: https://www.nytimes.com/2019/04/25/lens/sarah-lewis-racial-bias-photography.html
(visited on 03/22/2023).
[343]
Aitor Lewkowycz et al. Solving Quantitative Reasoning Problems with Language Models. tex.copyright:
Creative Commons Attribution 4.0 International. 2022. doi: 10.48550/ARXIV.2206.14858. url: https:
//arxiv.org/abs/2206.14858.
[344]
Kenneth Li. Do Large Language Models learn world models or just surface statistics? en. Jan. 2023. url:
https://thegradient.pub/othello/ (visited on 03/07/2023).
[345]
Liam Li and Ameet Talwalkar. “Random Search and Reproducibility for Neural Architecture Search”. In:
arXiv (2019). Publisher: arXiv tex.copyright: arXiv.org perpetual, non-exclusive license. doi: 10.48550/
ARXIV.1902.07638. url: https://arxiv.org/abs/1902.07638.
[346]
Qinbin Li et al. “A Survey on Federated Learning Systems: Vision, Hype and Reality for Data Privacy and
Protection”. In: IEEE Transactions on Knowledge and Data Engineering (2021). Conference Name: IEEE
Transactions on Knowledge and Data Engineering, pp. 1–1. issn: 1558-2191. doi: 10.1109/TKDE.2021.
3124599.
[347]
Thomas Liao et al. “Are We Learning Yet? A Meta Review of Evaluation Failures Across Machine Learning”.
en. In: NeurIPS, Jan. 2022. url: https://openreview.net/forum?id=mPducS1MsEK (visited on 12/03/2022).
[348]
Mark Liberman. “Obituary: Fred Jelinek”. In: Computational Linguistics 36.4 (2010), pp. 595–599.
[349]
Tianyang Lin et al. A Survey of Transformers. arXiv:2106.04554 [cs]. June 2021. doi: 10.48550/arXiv.2106.
04554. url: http://arxiv.org/abs/2106.04554 (visited on 09/27/2022).
[350]
Seppo Linnainmaa. “The representation of the cumulative rounding error of an algorithm as a Taylor
expansion of the local rounding errors”. ﬁ. MA thesis. Univ. Helsinki (in Finnish), 1970.


--- Page 48 ---

48
•
Leech et al.
[351]
Zachary C. Lipton and Jacob Steinhardt. Troubling Trends in Machine Learning Scholarship. arXiv:1807.03341
[cs, stat]. July 2018. doi: 10.48550/arXiv.1807.03341. url: http://arxiv.org/abs/1807.03341 (visited on
09/22/2022).
[352]
Gary Liu et al. “Deep learning-guided discovery of an antibiotic targeting Acinetobacter baumannii”. en.
In: Nature Chemical Biology 19.11 (Nov. 2023), pp. 1342–1350. issn: 1552-4469. doi: 10.1038/s41589-023-
01349-8. url: https://www.nature.com/articles/s41589-023-01349-8 (visited on 01/08/2024).
[353]
Peter J Liu et al. “Generating Wikipedia by summarizing long sequences”. In: arXiv (2018).
[354]
Ximeng Liu et al. “Privacy and Security Issues in Deep Learning: A Survey”. In: IEEE Access 9 (2021).
Conference Name: IEEE Access, pp. 4566–4593. issn: 2169-3536. doi: 10.1109/ACCESS.2020.3045078.
[355]
Steven Livingston and Mathias Risse. “The Future Impact of Artiﬁcial Intelligence on Humans and
Human Rights”. en. In: Ethics & International Aﬀairs 33.2 (2019), pp. 141–158. issn: 0892-6794, 1747-
7093. doi: 10.1017/S089267941900011X. url: https://www.cambridge.org/core/journals/ethics-and-
international-aﬀairs/article/abs/future-impact-of-artiﬁcial-intelligence-on-humans-and-human-
rights/2016EDC9A61F68615EBF9AFA8DE91BF8 (visited on 01/11/2023).
[356]
Orly Lobel. The Equality Machine. en-US. Public Aﬀairs, Jan. 2022. isbn: 9781541774735. url: https:
//www.publicaﬀairsbooks.com/titles/orly-lobel/the-equality-machine/9781541774735/ (visited on
12/08/2022).
[357]
Robert L. Logan IV et al. Cutting Down on Prompts and Parameters: Simple Few-Shot Learning with Language
Models. arXiv:2106.13353 [cs]. July 2021. doi: 10.48550/arXiv.2106.13353. url: http://arxiv.org/abs/2106.
13353 (visited on 01/08/2024).
[358]
Andrew Lohn and Micah Musser. “AI and Compute: How Much Longer Can Computing Power Drive
Artiﬁcial Intelligence Progress?” In: Center for Security and Emerging Technology (2022). Publisher: Center
for Security and Emerging Technology. url: https://cset.georgetown.edu/publication/ai-and-compute/.
[359]
Andrew J. Lohn. Estimating the Brittleness of AI: Safety Integrity Levels and the Need for Testing Out-Of-
Distribution Performance. arXiv:2009.00802 [cs, stat]. Sept. 2020. doi: 10.48550/arXiv.2009.00802. url:
http://arxiv.org/abs/2009.00802 (visited on 09/29/2022).
[360]
Shayne Longpre, Marcus Storm, and Rishi Shah. “Lethal autonomous weapons systems & artiﬁcial
intelligence: Trends, challenges, and policies”. en. In: MIT Science Policy Review 3 (Aug. 2022). Ed. by
Kevin McDermott, pp. 47–56. doi: 10.38105/spr.360apm5typ. url: https://sciencepolicyreview.org/2022/
07/mitspr-191618003019/ (visited on 12/11/2022).
[361]
David Luban, Alan Strudler, and David Wasserman. “Moral Responsibility in the Age of Bureaucracy”. In:
Michigan Law Review 90.8 (Aug. 1992), pp. 2348–2392. issn: 0026-2234. url: https://repository.law.umich.
edu/mlr/vol90/iss8/4.
[362]
Alexandra Sasha Luccioni, Sylvain Viguier, and Anne-Laure Ligozat. Estimating the Carbon Footprint of
BLOOM, a 176B Parameter Language Model. arXiv:2211.02001 [cs]. Nov. 2022. url: http://arxiv.org/abs/
2211.02001 (visited on 12/07/2022).
[363]
George F Luger. Artiﬁcial intelligence: structures and strategies for complex problem solving. Pearson
Education, 2005.
[364]
Matthijs Maas. Paths Untaken: The History, Epistemology and Strategy of Technological Restraint, and
lessons for AI. 2022. url: https://verfassungsblog.de/paths-untaken/.
[365]
Matthijs M. Maas. AI, Governance Displacement, and the (De)Fragmentation of International Law. en. SSRN
Scholarly Paper. Rochester, NY, Mar. 2021. doi: 10.2139/ssrn.3806624. url: https://papers.ssrn.com/
abstract=3806624 (visited on 11/28/2022).
[366]
Matthijs M. Maas. “Aligning AI Regulation to Sociotechnical Change”. en. In: The Oxford Handbook of
AI Governance. Ed. by Johannes Himmelreich et al. 1st ed. Oxford University Press, Mar. 2022. isbn:


--- Page 49 ---

Ten Hard Problems in AI
•
49
9780197579329. doi: 10.1093/oxfordhb/9780197579329.013.22. url: https://academic.oup.com/edited-
volume/41989/chapter/355438659 (visited on 09/23/2022).
[367]
Matthijs M. Maas, Kayla Matteucci, and Di Cooke. Military Artiﬁcial Intelligence as Contributor to Global
Catastrophic Risk. en. SSRN Scholarly Paper. Rochester, NY, May 2022. doi: 10.2139/ssrn.4115010. url:
https://papers.ssrn.com/abstract=4115010 (visited on 01/11/2023).
[368]
Terri Mannarini and Angela Fedi. “Multiple senses of community: the experience and meaning of commu-
nity”. en. In: Journal of Community Psychology 37.2 (Mar. 2009), pp. 211–227. issn: 00904392, 15206629. doi:
10.1002/jcop.20289. url: https://onlinelibrary.wiley.com/doi/10.1002/jcop.20289 (visited on 12/05/2022).
[369]
Gary E. Marchant, Lucille Tournas, and Carlos Ignacio Gutierrez. Governing Emerging Technologies
Through Soft Law: Lessons for Artiﬁcial Intelligence. en. SSRN Scholarly Paper. Rochester, NY, Dec. 2020.
url: https://papers.ssrn.com/abstract=3761871 (visited on 01/11/2023).
[370]
Gary Marcus. The Algebraic Mind. en-US. 2003. url: https://mitpress.mit.edu/9780262632683/the-
algebraic-mind/ (visited on 02/06/2024).
[371]
Fernando Martínez-Plumed, Emilia Gómez, and José Hernández-Orallo. “Futures of artiﬁcial intelligence
through technology readiness levels”. In: Telematics and Informatics 58 (2021). Publisher: Elsevier, p. 101525.
[372]
Matt Sheehan and Ishan Banerjee. The Global AI Talent Tracker. en. 2022. url: https://macropolo.org/digital-
projects/the-global-ai-talent-tracker/ (visited on 12/07/2022).
[373]
Matthew M Young et al. “Artiﬁcial Intelligence and Administrative Evil”. In: Perspectives on Public
Management and Governance (2021).
[374]
Abigail Matthews et al. “Gender Bias in Natural Language Processing Across Human Languages”. In:
Proceedings of the First Workshop on Trustworthy Natural Language Processing. Online: Association for
Computational Linguistics, June 2021, pp. 45–54. doi: 10.18653/v1/2021.trustnlp- 1.6. url: https:
//aclanthology.org/2021.trustnlp-1.6 (visited on 03/22/2023).
[375]
J. McCarthy et al. “A proposal for the Dartmouth Summer Research Project on Artiﬁcial Intelligence”. In:
Stanford (1955). url: www-formal.stanford.edu/jmc/history/dartmouth/dartmouth.html.
[376]
Jack McDonald. What if Military AI is a Washout? June 2021. url: https://jackmcdonald.org/book/2021/
06/what-if-military-ai-sucks/.
[377]
Thomas McGrath et al. Acquisition of Chess Knowledge in AlphaZero. arXiv:2111.09259 [cs, stat]. Aug.
2022. doi: 10.48550/arXiv.2111.09259. url: http://arxiv.org/abs/2111.09259 (visited on 09/29/2022).
[378]
Cade Metz. Genius Makers: The Mavericks who Brought AI to Google, Facebook, and the World. Penguin,
2022.
[379]
Luke Metz et al. VeLO: Training Versatile Learned Optimizers by Scaling Up. tex.copyright: arXiv.org
perpetual, non-exclusive license. 2022. doi: 10.48550/ARXIV.2211.09760. url: https://arxiv.org/abs/2211.
09760.
[380]
Thomas Metzinger. “Towards a global artiﬁcial intelligence charter”. In: Should We Fear Artiﬁcial Intelli-
gence (2018). Publisher: EU Parliament Bruxelles, pp. 27–33.
[381]
Richard Meyes et al. “Ablation studies in artiﬁcial neural networks”. In: arXiv (2019).
[382]
El-Mahdi El-Mhamdi et al. “SoK: On the Impossible Security of Very Large Foundation Models”. In: arXiv
(2022).
[383]
Grégoire Mialon et al. Augmented Language Models: a Survey. arXiv:2302.07842 [cs]. Feb. 2023. doi:
10.48550/arXiv.2302.07842. url: http://arxiv.org/abs/2302.07842 (visited on 03/07/2023).
[384]
Microsoft Global Diversity & Inclusion Report 2022. Tech. rep. Microsoft, 2022.
[385]
Tomas Mikolov et al. “Distributed Representations of Words and Phrases and their Compositionality”.
In: Advances in Neural Information Processing Systems. Vol. 26. Curran Associates, Inc., 2013. url: https:
//proceedings.neurips.cc/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html (visited on
12/06/2022).


--- Page 50 ---

50
•
Leech et al.
[386]
Marvin L Minsky and Seymour A Papert. Perceptrons. MIT Press, 1969.
[387]
Azalia Mirhoseini et al. “A graph placement methodology for fast chip design”. In: Nature 594.7862 (2021).
Publisher: Nature Publishing Group, pp. 207–212.
[388]
Margaret Mitchell et al. “Model cards for model reporting”. In: Proceedings of the Conference on Fairness,
Accountability, and Transparency. 2019, pp. 220–229. doi: 10.1145/3287560.3287596. url: http://dx.doi.org/
10.1145/3287560.3287596.
[389]
Lilian Mitrou. Data Protection, Artiﬁcial Intelligence and Cognitive Services: Is the General Data Protection
Regulation (GDPR) ‘Artiﬁcial Intelligence-Proof’? en. SSRN Scholarly Paper. Rochester, NY, Dec. 2018. doi:
10.2139/ssrn.3386914. url: https://papers.ssrn.com/abstract=3386914 (visited on 12/08/2022).
[390]
Brent Mittelstadt. “Principles alone cannot guarantee ethical AI”. en. In: Nature 1.11 (Nov. 2019), pp. 501–
507. issn: 2522-5839. doi: 10.1038/s42256-019-0114-4. url: https://www.nature.com/articles/s42256-019-
0114-4 (visited on 12/07/2022).
[391]
MLPerf Inference v1.0 Results with First Power Measurements. en. url: https://mlcommons.org/ (visited on
12/07/2022).
[392]
Volodymyr Mnih et al. Playing Atari with Deep Reinforcement Learning. arXiv:1312.5602 [cs]. Dec. 2013.
doi: 10.48550/arXiv.1312.5602. url: http://arxiv.org/abs/1312.5602 (visited on 11/10/2022).
[393]
Kimberley Mok. Large Language Models: Open Source LLMs in 2023. en-US. Dec. 2023. url: https://
thenewstack.io/large-language-models-open-source-llms-in-2023/ (visited on 01/08/2024).
[394]
Gordon E. Moore. “Cramming More Components onto Integrated Circuits”. In: Electronicsweek (Apr. 1965),
pp. 114–117.
[395]
Yuichi Mori et al. “Cost savings in colonoscopy with artiﬁcial intelligence-aided polyp diagnosis: an add-on
analysis of a clinical trial (with video)*”. en. In: Gastrointestinal Endoscopy 92.4 (Oct. 2020), 905–911.e1.
issn: 0016-5107. doi: 10.1016/j.gie.2020.03.3759. url: https://www.sciencedirect.com/science/article/pii/
S0016510720340347 (visited on 12/06/2022).
[396]
Viraaji Mothukuri et al. “A survey on security and privacy of federated learning”. en. In: Future Generation
Computer Systems 115 (Feb. 2021), pp. 619–640. issn: 0167-739X. doi: 10.1016/j.future.2020.10.007. url:
https://www.sciencedirect.com/science/article/pii/S0167739X20329848 (visited on 12/07/2022).
[397]
Paul Mozur. “One Month, 500,000 Face Scans: How China Is Using A.I. to Proﬁle a Minority”. en-US. In: The
New York Times (Apr. 2019). issn: 0362-4331. url: https://www.nytimes.com/2019/04/14/technology/china-
surveillance-artiﬁcial-intelligence-racial-proﬁling.html (visited on 12/08/2022).
[398]
Paul Mozur and Adam Satariano. “A.I., Brain Scans and Cameras: The Spread of Police Surveillance Tech”.
en-US. In: The New York Times (Mar. 2023). issn: 0362-4331. url: https://www.nytimes.com/2023/03/30/
technology/police-surveillance-tech-dubai.html (visited on 01/08/2024).
[399]
Luke Muehlhauser. Our AI governance grantmaking so far. 2020. url: https://www.openphilanthropy.org/
blog/ai-governance-grantmaking.
[400]
Kevin Musgrave, Serge Belongie, and Ser-Nam Lim. A Metric Learning Reality Check. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2020. doi: 10.48550/ARXIV.2003.08505. url: https://arxiv.org/
abs/2003.08505.
[401]
Basil Mustafa et al. Multimodal Contrastive Learning with LIMoE: the Language-Image Mixture of Experts.
arXiv:2206.02770 [cs]. June 2022. doi: 10.48550/arXiv.2206.02770. url: http://arxiv.org/abs/2206.02770
(visited on 10/13/2022).
[402]
Sarah Myers West. “Discriminating Systems: Gender, Race and Power in Artiﬁcial Intelligence”. In: Georgia
Tech Library (Feb. 2020). url: https://smartech.gatech.edu/handle/1853/62480 (visited on 09/19/2022).
[403]
Vinod Nair and Geoﬀrey E Hinton. “Rectiﬁed linear units improve restricted Boltzmann machines”. In:
Proceedings of the 27th International Conference on International Conference on Machine Learning. ICML
’10. Omnipress, 2010, pp. 807–814.


--- Page 51 ---

Ten Hard Problems in AI
•
51
[404]
Preetum Nakkiran et al. Deep Double Descent: Where Bigger Models and More Data Hurt. arXiv:1912.02292
[cs, stat]. Dec. 2019. doi: 10.48550/arXiv.1912.02292. url: http://arxiv.org/abs/1912.02292 (visited on
09/27/2022).
[405]
Neel Nanda. A Mechanistic Interpretability Analysis of Grokking. en. 2022. url: https://www.alignmentforum.
org/posts/N6WM6hs7RQMKDhYjB/a-mechanistic-interpretability-analysis-of-grokking (visited on
09/29/2022).
[406]
Deepak Narayanan et al. “PipeDream: generalized pipeline parallelism for DNN training”. In: Proceedings
of the 27th ACM Symposium on Operating Systems Principles. SOSP ’19. New York, NY, USA: ACM, Oct.
2019, pp. 1–15. isbn: 978-1-4503-6873-5. doi: 10.1145/3341301.3359646. url: https://doi.org/10.1145/
3341301.3359646 (visited on 11/04/2022).
[407]
NASA. Preparation for Flight, the Accident, and Investigation. 1967. url: https://www.hq.nasa.gov/oﬃce/
pao/History/SP-4009/v4p1h.htm.
[408]
Engineering National Academies of Sciences. Quantum Computing: Progress and Prospects. en. National
Academies, Dec. 2018. isbn: 978-0-309-47969-1. doi: 10.17226/25196. url: https://nap.nationalacademies.
org/catalog/25196/quantum-computing-progress-and-prospects (visited on 10/13/2022).
[409]
National Science Foundation. Proposal and Award Policies and Procedures Guide. 2021. url: https://www.
nsf.gov/pubs/policydocs/pappg22_1/index.jsp (visited on 12/09/2022).
[410]
Ljubica Nedelkoska and Glenda Quintini. Automation, skills use and training. Tech. rep. Paris: OCDE, Mar.
2018. doi: 10.1787/2e2f4eea-en. url: https://www.oecd-ilibrary.org/fr/employment/automation-skills-
use-and-training_2e2f4eea-en (visited on 11/25/2022).
[411]
Nataliya Nedzhvetskaya and J. S. Tan. The Role of Workers in AI Ethics and Governance. arXiv:2108.07700
[cs]. Aug. 2021. doi: 10.48550/arXiv.2108.07700. url: http://arxiv.org/abs/2108.07700 (visited on
12/08/2022).
[412]
Robert de Neufville and Seth D. Baum. “Collective action on artiﬁcial intelligence: A primer and review”.
en. In: Technology in Society 66 (Aug. 2021), p. 101649. issn: 0160-791X. doi: 10.1016/j.techsoc.2021.101649.
url: https://www.sciencedirect.com/science/article/pii/S0160791X2100124X (visited on 07/15/2021).
[413]
Andrew Ng and Christopher Manning. Heroes of NLP: Chris Manning. en-GB. Youtube, 2020. url: https:
//www.youtube.com/watch?v=H343JRrncfc (visited on 12/09/2022).
[414]
Richard Ngo. The alignment problem from a deep learning perspective. arXiv:2209.00626 [cs]. Aug. 2022.
doi: 10.48550/arXiv.2209.00626. url: http://arxiv.org/abs/2209.00626 (visited on 09/30/2022).
[415]
Michael Nielsen. The role of “explanation” in AI. 2022. url: https://michaelnotebook.com/ongoing/
sporadica.html#role_of_explanation_in_AI.
[416]
Michael A Nielsen. Neural Networks and Deep Learning. Vol. 25. Determination Press San Francisco, CA,
USA, 2015.
[417]
NIST. “AI Risk Management Framework”. en. In: NIST (July 2021). url: https://www.nist.gov/itl/ai-risk-
management-framework (visited on 01/11/2023).
[418]
NIST. “U.S. Artiﬁcial Intelligence Safety Institute”. en. In: NIST (Oct. 2023). url: https://www.nist.gov/
artiﬁcial-intelligence/artiﬁcial-intelligence-safety-institute (visited on 01/08/2024).
[419]
Harsha Nori et al. “InterpretML: A Uniﬁed Framework for Machine Learning Interpretability”. In: arXiv
(2019). url: https://arxiv.org/pdf/1909.09223.pdf.
[420]
Maxwell Nye et al. Show Your Work: Scratchpads for Intermediate Computation with Language Models.
arXiv:2112.00114 [cs]. Nov. 2021. doi: 10.48550/arXiv.2112.00114. url: http://arxiv.org/abs/2112.00114
(visited on 09/23/2022).
[421]
Sven Nyholm. “Attributing Agency to Automated Systems: Reﬂections on Human–Robot Collaborations
and Responsibility-Loci”. en. In: Science and Engineering Ethics 24.4 (Aug. 2018), pp. 1201–1219. issn:


--- Page 52 ---

52
•
Leech et al.
1471-5546. doi: 10.1007/s11948-017-9943-x. url: https://doi.org/10.1007/s11948-017-9943-x (visited on
11/25/2022).
[422]
Cathy O’Neil. Weapons of Math Destruction: How big data increases inequality and threatens democracy.
Crown, 2017.
[423]
Chris Olah. Mechanistic Interpretability, Variables, and the Importance of Interpretable Bases. 2022. url:
https://transformer-circuits.pub/2022/mech-interp-essay/index.html.
[424]
Chris Olah et al. “Zoom In: An Introduction to Circuits”. In: Distill 5.3 (Mar. 2020), 10.23915/distill.00024.001.
issn: 2476-0757. doi: 10.23915/distill.00024.001. url: https://distill.pub/2020/circuits/zoom-in (visited on
09/29/2022).
[425]
Mikel Olazaran. “A Sociological History of the Neural Network Controversy”. In: ed. by Marshall C. Yovits.
Vol. 37. Advances in Computers. ISSN: 0065-2458. Elsevier, 1993, pp. 335–425. doi: https://doi.org/10.1016/
S0065-2458(08)60408-8. url: https://www.sciencedirect.com/science/article/pii/S0065245808604088.
[426]
Stephen M. Omohundro. “The Basic AI Drives”. In: Proceedings of the 2008 Conference on Artiﬁcial General
Intelligence 2008: Proceedings of the First AGI Conference. NLD: IOS Press, June 2008, pp. 483–492. isbn:
9781586038335. (Visited on 09/29/2022).
[427]
OpenAI. GPT Tokenizer. 2020. url: https://beta.openai.com/tokenizer.
[428]
OpenAI. GPT-4 Technical Report. arXiv:2303.08774 [cs]. Mar. 2023. doi: 10.48550/arXiv.2303.08774. url:
http://arxiv.org/abs/2303.08774 (visited on 04/13/2023).
[429]
OpenAI. OpenAI API. en. 2020. url: https://beta.openai.com (visited on 11/28/2022).
[430]
OpenAI API. url: https://openai.com/api.
[431]
Manfred Opper. “Statistical Mechanics of Learning: Generalization”. In: The Handbook of Brain Theory
and Neural Networks (1995). Publisher: MIT Press) (Cambridge, MA, pp. 922–925.
[432]
Oracle. Can Virtual Experiences Replace Reality? Tech. rep. Oracle, 2019.
[433]
A. Emin Orhan and Xaq Pitkow. Skip Connections Eliminate Singularities. tex.copyright: arXiv.org perpetual,
non-exclusive license. 2017. doi: 10.48550/ARXIV.1701.09175. url: https://arxiv.org/abs/1701.09175.
[434]
Laurent Orseau and Stuart Armstrong. Safely Interruptible Agents. en. 2016. url: https://www.deepmind.
com/publications/safely-interruptible-agents (visited on 10/03/2022).
[435]
Simon Ott et al. “Mapping global dynamics of benchmark creation and saturation in artiﬁcial intelligence”.
en. In: Nature Communications 13.1 (Nov. 2022), p. 6793. issn: 2041-1723. doi: 10.1038/s41467-022-34591-0.
url: https://www.nature.com/articles/s41467-022-34591-0 (visited on 02/02/2023).
[436]
Long Ouyang et al. Training language models to follow instructions with human feedback. arXiv:2203.02155
[cs]. Mar. 2022. doi: 10.48550/arXiv.2203.02155. url: http://arxiv.org/abs/2203.02155 (visited on
09/30/2022).
[437]
Pablo Fuentes Nettel and Alejandra Finotto, Sulamaan Rahim and André Petheram. Government AI
Readiness Index 2021. en-GB. 2021. url: https://www.oxfordinsights.com/government-ai-readiness-
index2021 (visited on 12/07/2022).
[438]
PAI. Fairer Algorithmic Decision-Making and Its Consequences: Interrogating the Risks and Beneﬁts of
Demographic Data Collection, Use, and Non-Use. Dec. 2021. url: https://partnershiponai.org/paper/fairer-
algorithmic-decision-making-and-its-consequences/.
[439]
Andrei Paleyes, Raoul-Gabriel Urma, and Neil D. Lawrence. “Challenges in Deploying Machine Learning:
a Survey of Case Studies”. In: ACM Computing Surveys (Apr. 2022). Just Accepted. issn: 0360-0300. doi:
10.1145/3533378. url: https://doi.org/10.1145/3533378 (visited on 12/03/2022).
[440]
Alexander Pan, Kush Bhatia, and Jacob Steinhardt. “The Eﬀects of Reward Misspeciﬁcation: Mapping
and Mitigating Misaligned Models”. en. In: ICLR, Feb. 2022. url: https://openreview.net/forum?id=
JYtwGwIL7ye (visited on 09/30/2022).


--- Page 53 ---

Ten Hard Problems in AI
•
53
[441]
Sethuraman Panchanathan and Arati Prabhakar. Strengthening and Democratizing the U.S. Artiﬁcial
Intelligence Innovation Ecosystem. en-US. Tech. rep. The White House, Jan. 2023. url: https://www.ai.gov/
wp-content/uploads/2023/01/NAIRR-TF-Final-Report-2023.pdf (visited on 03/21/2023).
[442]
Mohit Pandey et al. “The transformational role of GPU computing and deep learning in drug discovery”.
en. In: Nature 4.3 (Mar. 2022). Number: 3 Publisher: Nature Publishing Group, pp. 211–221. issn: 2522-5839.
doi: 10.1038/s42256-022-00463-x. url: https://www.nature.com/articles/s42256-022-00463-x (visited on
11/04/2022).
[443]
Razvan Pascanu, Tomas Mikolov, and Yoshua Bengio. “On the diﬃculty of training recurrent neural
networks”. In: International Conference on Machine Learning. tex.organization: PMLR. 2013, pp. 1310–1318.
[444]
Razvan Pascanu, Guido Montufar, and Yoshua Bengio. “On the number of response regions of deep feed
forward networks with piece-wise linear activations”. In: arXiv (2013). eprint: 1312.6098.
[445]
Rajan Patel. Giving Lens New Reading Capabilities in Google Go. en. 2019. url: https://ai.googleblog.com/
2019/09/giving-lens-new-reading-capabilities-in.html (visited on 12/07/2022).
[446]
Reema Patel. Public deliberation could help address AI’s legitimacy problem in 2019. en-GB. 2019. url: https:
//www.adalovelaceinstitute.org/blog/public-deliberation-help-address-ais-legitimacy-problem-2019/
(visited on 12/07/2022).
[447]
David Patterson et al. Carbon Emissions and Large Neural Network Training. arXiv:2104.10350 [cs]. Apr.
2021. doi: 10.48550/arXiv.2104.10350. url: http://arxiv.org/abs/2104.10350 (visited on 12/07/2022).
[448]
David Patterson et al. The Carbon Footprint of Machine Learning Training Will Plateau, Then Shrink.
arXiv:2204.05149 [cs]. Apr. 2022. url: http://arxiv.org/abs/2204.05149 (visited on 12/07/2022).
[449]
Ethan Perez et al. Discovering Language Model Behaviors with Model-Written Evaluations. Tech. rep.
Anthropic, Dec. 2022. url: https://www.anthropic.com/model-written-evals.pdf.
[450]
Ethan Perez et al. Red Teaming Language Models with Language Models. arXiv:2202.03286 [cs]. Feb. 2022.
doi: 10.48550/arXiv.2202.03286. url: http://arxiv.org/abs/2202.03286 (visited on 09/30/2022).
[451]
Julien Perolat et al. “Mastering the game of Stratego with model-free multiagent reinforcement learning”.
en. In: Science 378.6623 (Dec. 2022), pp. 990–996. issn: 0036-8075, 1095-9203. doi: 10.1126/science.add4679.
url: https://www.science.org/doi/10.1126/science.add4679 (visited on 12/02/2022).
[452]
Matthew E. Peters et al. Deep contextualized word representations. tex.copyright: arXiv.org perpetual,
non-exclusive license. 2018. doi: 10.48550/ARXIV.1802.05365. url: https://arxiv.org/abs/1802.05365.
[453]
Michael A. Peters. “Semiconductors, geopolitics and technological rivalry: the US CHIPS & Science Act,
2022”. en. In: Educational Philosophy and Theory (Sept. 2022), pp. 1–5. issn: 0013-1857, 1469-5812. doi: 10.
1080/00131857.2022.2124914. url: https://www.tandfonline.com/doi/full/10.1080/00131857.2022.2124914
(visited on 12/11/2022).
[454]
Fabio Petroni et al. Improving Wikipedia Veriﬁability with AI. arXiv: 2207.06220 [cs]. July 2022. doi:
10.48550/arXiv.2207.06220. url: http://arxiv.org/abs/2207.06220 (visited on 11/14/2022).
[455]
David Picard. Torch.manual_seed(3407) is all you need: On the inﬂuence of random seeds in deep learning ar-
chitectures for computer vision. tex.copyright: Creative Commons Attribution Share Alike 4.0 International.
2021. doi: 10.48550/ARXIV.2109.08203. url: https://arxiv.org/abs/2109.08203.
[456]
Aleksandra Piktus et al. The Web Is Your Oyster - Knowledge-Intensive NLP against a Very Large Web Corpus.
arXiv:2112.09924 [cs]. May 2022. doi: 10.48550/arXiv.2112.09924. url: http://arxiv.org/abs/2112.09924
(visited on 11/14/2022).
[457]
Ivens Portugal, Paulo Alencar, and Donald Cowan. “The use of machine learning algorithms in recom-
mender systems: A systematic review”. en. In: Expert Systems with Applications 97 (May 2018), pp. 205–227.
issn: 0957-4174. doi: 10.1016/j.eswa.2017.12.020. url: https://www.sciencedirect.com/science/article/pii/
S0957417417308333 (visited on 12/07/2022).


--- Page 54 ---

54
•
Leech et al.
[458]
Carina Prunkl and Jess Whittlestone. “Beyond Near- and Long-Term: Towards a Clearer Account of
Research Priorities in AI Ethics and Society”. In: Proceedings of the AAAI/ACM Conference on AI, Ethics,
and Society. AIES ’20. New York, NY, USA: ACM, Feb. 2020, pp. 138–143. isbn: 978-1-4503-7110-0. doi:
10.1145/3375627.3375803. url: https://doi.org/10.1145/3375627.3375803 (visited on 09/30/2022).
[459]
Carina E. A. Prunkl et al. “Institutionalizing ethics in AI through broader impact requirements”. en.
In: Nature 3.2 (Feb. 2021), pp. 104–110. issn: 2522-5839. doi: 10.1038/s42256-021-00298-y. url: https:
//www.nature.com/articles/s42256-021-00298-y (visited on 01/11/2023).
[460]
Radford. “Language Models are Unsupervised Multitask Learners”. In: PapersWithCode (). url: https:
//d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf.
[461]
Alec Radford et al. “Improving language understanding by generative pre-training”. In: arXiv (2018).
Publisher: OpenAI.
[462]
Alec Radford et al. Learning Transferable Visual Models From Natural Language Supervision. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2021. doi: 10.48550/ARXIV.2103.00020. url: https://arxiv.org/
abs/2103.00020.
[463]
Manish Raghavan et al. “Mitigating Bias in Algorithmic Hiring: Evaluating Claims and Practices”. In:
arXiv:1906.09208 [cs]. arXiv, Jan. 2020, pp. 469–481. doi: 10.1145/3351095.3372828. url: http://arxiv.org/
abs/1906.09208 (visited on 11/28/2022).
[464]
Maithra Raghu and Eric Schmidt. A Survey of Deep Learning for Scientiﬁc Discovery. arXiv:2003.11755
[cs, stat]. Mar. 2020. doi: 10.48550/arXiv.2003.11755. url: http://arxiv.org/abs/2003.11755 (visited on
09/23/2022).
[465]
Ilya Rahkovsky et al. “AI Research Funding Portfolios and Extreme Growth”. In: Frontiers in Research
Metrics and Analytics 6 (2021). issn: 2504-0537. url: https://www.frontiersin.org/articles/10.3389/frma.
2021.630124 (visited on 12/09/2022).
[466]
Inioluwa Deborah Raji et al. AI and the Everything in the Whole Wide World Benchmark. arXiv:2111.15366
[cs]. Nov. 2021. doi: 10.48550/arXiv.2111.15366. url: http://arxiv.org/abs/2111.15366 (visited on
12/07/2022).
[467]
Aditya Ramesh et al. Hierarchical Text-Conditional Image Generation with CLIP Latents. tex.copyright:
Creative Commons Attribution 4.0 International. 2022. doi: 10.48550/ARXIV.2204.06125. url: https:
//arxiv.org/abs/2204.06125.
[468]
Marc’Aurelio Ranzato et al. “Unsupervised learning of invariant feature hierarchies with applications to
object recognition”. In: Proceedings of the IEEE. tex.organization: IEEE. 2007, pp. 1–8.
[469]
Tilman Räuker et al. Toward Transparent AI: A Survey on Interpreting the Inner Structures of Deep Neural
Networks. arXiv:2207.13243 [cs]. Sept. 2022. doi: 10.48550/arXiv.2207.13243. url: http://arxiv.org/abs/2207.
13243 (visited on 09/29/2022).
[470]
Benjamin Recht and Moritz Hardt. The Saga of Highleyman’s Data. Oct. 2021. url: http://www.argmin.
net/2021/10/20/highleyman/.
[471]
Joanna Redden et al. Automating Public Services: Learning from Cancelled Systems. en-US. Tech. rep.
Carnegie UK, 2022. url: https://www.carnegieuktrust.org.uk/publications/automating-public-services-
learning-from-cancelled-systems/ (visited on 10/13/2022).
[472]
Scott Reed et al. Gato - A Generalist Agent. arXiv:2205.06175 [cs]. May 2022. doi: 10.48550/arXiv.2205.06175.
url: http://arxiv.org/abs/2205.06175 (visited on 09/27/2022).
[473]
Tobias Rees. Non-Human Words: On GPT-3 as a Philosophical Laboratory. en. 2022. url: https://www.
amacad.org/publication/non-human-words-gpt-3-philosophical-laboratory (visited on 11/25/2022).
[474]
Lyle Regenwetter, Amin Heyrani Nobari, and Faez Ahmed. Deep Generative Models in Engineering Design:
A Review. arXiv:2110.10863 [cs, stat]. Mar. 2022. doi: 10.48550/arXiv.2110.10863. url: http://arxiv.org/abs/
2110.10863 (visited on 09/23/2022).


--- Page 55 ---

Ten Hard Problems in AI
•
55
[475]
Report on Algorithmic Risk Assessment Tools in the U.S. Criminal Justice System. en-US. url: https://
partnershiponai.org/paper/report-on-machine-learning-in-risk-assessment-tools-in-the-u-s-criminal-
justice-system/ (visited on 11/15/2022).
[476]
Albert Reuther et al. AI and ML Accelerator Survey and Trends. tex.copyright: arXiv.org perpetual, non-
exclusive license. 2022. doi: 10.48550/ARXIV.2210.04055. url: https://arxiv.org/abs/2210.04055.
[477]
Mark Riedl. AI Democratization in the Era of GPT-3. en. Sept. 2020. url: https://thegradient.pub/ai-
democratization-in-the-era-of-gpt-3/ (visited on 09/20/2022).
[478]
Clarissa Rios Rojas, Catherine Richards, and Catherine Rhodes. Pathways to Linking Science and Policy
in the Field of Global Risk. Tech. rep. Cambridge: Centre for the Study of Existential Risk. url: https:
//www.cser.ac.uk/news/new-report-pathways-linking-science-and-policy-ﬁe/ (visited on 11/25/2022).
[479]
Horst W. J. Rittel and Melvin M. Webber. “Dilemmas in a General Theory of Planning”. In: Policy Sciences
4.2 (1973). Publisher: Springer, pp. 155–169. issn: 0032-2687. url: https://www.jstor.org/stable/4531523
(visited on 10/05/2022).
[480]
Herbert Robbins and Sutton Monro. “A stochastic approximation method”. In: The Annals of Mathematical
Statistics (1951). Publisher: JSTOR, pp. 400–407.
[481]
Huw Roberts et al. “Achieving a ‘Good AI Society’: Comparing the Aims and Progress of the EU and the
US”. en. In: Science and Engineering Ethics 27.6 (Nov. 2021), p. 68. issn: 1471-5546. doi: 10.1007/s11948-
021-00340-7. url: https://doi.org/10.1007/s11948-021-00340-7 (visited on 11/16/2021).
[482]
Michael Roberts et al. “Common pitfalls and recommendations for using machine learning to detect and
prognosticate for COVID-19 using chest radiographs and CT scans”. en. In: Nature 3.3 (Mar. 2021), pp. 199–
217. issn: 2522-5839. doi: 10.1038/s42256-021-00307-0. url: https://www.nature.com/articles/s42256-021-
00307-0 (visited on 09/29/2022).
[483]
David Rolnick et al. Tackling Climate Change with Machine Learning. arXiv:1906.05433 [cs, stat]. Nov.
2019. doi: 10.48550/arXiv.1906.05433. url: http://arxiv.org/abs/1906.05433 (visited on 04/05/2023).
[484]
Robin Rombach et al. High-Resolution Image Synthesis with Latent Diﬀusion Models. arXiv:2112.10752 [cs].
Apr. 2022. doi: 10.48550/arXiv.2112.10752. url: http://arxiv.org/abs/2112.10752 (visited on 01/07/2023).
[485]
Kevin Roose. A.I.-Generated Art Is Already Transforming Creative Work. 2022. url: https://www.nytimes.
com/2022/10/21/technology/ai-generated-art-jobs-dall-e-2.html.
[486]
Rajarshi Roy et al. “PreﬁxRL: Optimization of Parallel Preﬁx Circuits using Deep Reinforcement Learning”.
In: 2021 58th ACM/IEEE Design Automation Conference (DAC). IEEE, 2021, pp. 853–858. doi: 10.1109/
DAC18074.2021.9586094.
[487]
Sebastian Ruder. Tracking Progress in Natural Language Processing. 2022. url: https://github.com/
sebastianruder/NLP-progress.
[488]
Cynthia Rudin. Stop Explaining Black Box Machine Learning Models for High Stakes Decisions and Use
Interpretable Models Instead. arXiv:1811.10154 [cs, stat]. Sept. 2019. doi: 10.48550/arXiv.1811.10154. url:
http://arxiv.org/abs/1811.10154 (visited on 09/29/2022).
[489]
David E Rumelhart, Geoﬀrey E Hinton, and Ronald J Williams. “Learning representations by back-
propagating errors”. In: Nature 323.6088 (1986). Publisher: Nature Publishing Group, pp. 533–536.
[490]
Stuart Russell. Human Compatible: Artiﬁcial intelligence and the problem of control. Penguin Random
House, 2020. isbn: 9780525558637.
[491]
Stuart Russell and Peter Norvig. Artiﬁcial Intelligence: A Modern Approach. 4th. Prentice Hall, 2021. isbn:
978-1-292-40113-3.
[492]
Benjamin Sanchez-Lengeling et al. “A gentle introduction to graph neural networks”. In: Distill 6.9 (2021),
e33.


--- Page 56 ---

56
•
Leech et al.
[493]
Anders Sandberg. “An overview of models of technological singularity”. In: The Transhumanist Reader:
Classical and contemporary essays on the science, technology, and philosophy of the human future (2013).
Publisher: Wiley Online Library, pp. 376–394.
[494]
Rylan Schaeﬀer, Brando Miranda, and Sanmi Koyejo. Are Emergent Abilities of Large Language Models a
Mirage? arXiv:2304.15004 [cs]. May 2023. doi: 10.48550/arXiv.2304.15004. url: http://arxiv.org/abs/2304.
15004 (visited on 01/08/2024).
[495]
Paul Scharre. “Debunking the AI Arms Race Theory”. en-US. In: Texas National Security Review 4.3 (June
2021). url: https://tnsr.org/2021/06/debunking-the-ai-arms-race-theory/ (visited on 07/08/2021).
[496]
Eric Schmidt et al. NSCAI 2021 Final Report. en-US. 2021. url: https://www.nscai.gov/2021-ﬁnal-report/
(visited on 11/26/2022).
[497]
Schmidt Futures Launches AI2050 to Protect Our Human Future in the Age of Artiﬁcial Intelligence. Feb. 2022.
url: https://www.schmidtfutures.com/schmidt-futures-launches-ai2050-to-protect-our-human-future-
in-the-age-of-artiﬁcial-intelligence/.
[498]
Lewin Schmitt. “Mapping global AI governance: a nascent regime in a fragmented landscape”. en. In:
AI and Ethics 2.2 (May 2022), pp. 303–314. issn: 2730-5961. doi: 10.1007/s43681-021-00083-y. url:
https://doi.org/10.1007/s43681-021-00083-y (visited on 01/06/2023).
[499]
Julian Schrittwieser et al. “Mastering Atari, Go, Chess and Shogi by planning with a learned model”.
In: Nature 588.7839 (Dec. 2020), pp. 604–609. issn: 1476-4687. doi: 10.1038/s41586-020-03051-4. url:
https://www.nature.com/articles/s41586-020-03051-4 (visited on 11/26/2022).
[500]
Terrence J Sejnowski. The Deep Learning Revolution. MIT press, 2018.
[501]
Andrew Selbst and Julia Powles. ““Meaningful Information” and the Right to Explanation”. en. In: Pro-
ceedings of the 1st Conference on Fairness, Accountability and Transparency. PMLR, Jan. 2018, pp. 48–48.
url: https://proceedings.mlr.press/v81/selbst18a.html (visited on 11/26/2022).
[502]
Lesia Semenova, Cynthia Rudin, and Ronald Parr. “On the Existence of Simpler Machine Learning Models”.
In: arXiv (2022). url: https://arxiv.org/pdf/1908.01755.pdf.
[503]
Rico Sennrich, Barry Haddow, and Alexandra Birch. Neural Machine Translation of Rare Words with
Subword Units. tex.copyright: Creative Commons Attribution 4.0 International. 2015. doi: 10.48550/ARXIV.
1508.07909. url: https://arxiv.org/abs/1508.07909.
[504]
Jaime Sevilla et al. Compute Trends Across Three Eras of Machine Learning. arXiv:2202.05924 [cs]. Mar.
2022. doi: 10.48550/arXiv.2202.05924. url: http://arxiv.org/abs/2202.05924 (visited on 10/14/2022).
[505]
Scott Shane and Daisuke Wakabayashi. “‘The Business of War’: Google Employees Protest Work for the
Pentagon”. en-US. In: The New York Times (Apr. 2018). issn: 0362-4331. url: https://www.nytimes.com/
2018/04/04/technology/google-letter-ceo-pentagon-project.html (visited on 12/08/2022).
[506]
Or Sharir, Barak Peleg, and Yoav Shoham. The Cost of Training NLP Models: A Concise Overview. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2020. doi: 10.48550/ARXIV.2004.08900. url: https://arxiv.org/
abs/2004.08900.
[507]
Cayla Sharp. Peter Norvig – Singularity is in the Eye of the Beholder. 2021. url: https://wandb.ai/wandb_fc/
gradient-dissent/reports/Peter-Norvig-Google-s-Director-of-Research-Singularity-is-in-the-eye-of-
the-beholder--Vmlldzo2MTYwNjk.
[508]
Toby Shevlane. “Structured Access: An Emerging Paradigm for Safe AI Deployment”. en. In: The Oxford
Handbook of AI Governance. Ed. by Justin Bullock et al. 1st ed. Oxford University Press, May 2022. isbn:
9780197579329. doi: 10.1093/oxfordhb/9780197579329.013.39. url: https://academic.oup.com/edited-
volume/41989/chapter/355438814 (visited on 09/23/2022).
[509]
Toby Shevlane. The Artefacts of Intelligence: Governing Scientists’ Contribution to AI Proliferation | GovAI.
en. 2021. url: https://www.governance.ai/research-paper/the-artefacts-of-intelligence-governing-
scientists-contribution-to-ai-proliferation (visited on 01/11/2023).


--- Page 57 ---

Ten Hard Problems in AI
•
57
[510]
Reza Shokri and Vitaly Shmatikov. “Privacy-preserving deep learning”. In: 2015 53rd Annual Allerton
Conference on Communication, Control, and Computing (Allerton). IEEE, Sept. 2015, pp. 909–910. isbn:
978-1-5090-1824-6. doi: 10.1109/ALLERTON.2015.7447103.
[511]
Connor Shorten and Taghi M. Khoshgoftaar. “A survey on Image Data Augmentation for Deep Learning”.
In: Journal of Big Data 6.1 (July 2019), p. 60. issn: 2196-1115. doi: 10.1186/s40537-019-0197-0. url:
https://doi.org/10.1186/s40537-019-0197-0 (visited on 09/29/2022).
[512]
Carl Shulman and Nick Bostrom. “Sharing the World with Digital Minds”. In: Rethinking Moral Status.
tex.eprint: https://academic.oup.com/book/0/chapter/350760172/chapter-pdf/43437637/oso-9780192894076-
chapter-18.pdf. Oxford University Press, Aug. 2021. isbn: 978-0-19-289407-6. doi: 10.1093/oso/9780192894076.
003.0018. url: https://doi.org/10.1093/oso/9780192894076.003.0018.
[513]
Divya Siddarth et al. How AI Fails Us. 2022. url: https://carrcenter.hks.harvard.edu/ﬁles/cchr/ﬁles/
howaifailsus.pdf.
[514]
Anton Sigfrids et al. “How Should Public Administrations Foster the Ethical Development and Use of
Artiﬁcial Intelligence? A Review of Proposals for Developing Governance of AI”. In: Frontiers in Human
Dynamics 4 (2022). issn: 2673-2726. url: https://www.frontiersin.org/articles/10.3389/fhumd.2022.858108
(visited on 12/06/2022).
[515]
David Silver et al. “AlphaGo - Mastering the game of Go with deep neural networks and tree search”.
en. In: Nature 529.7587 (Jan. 2016), pp. 484–489. issn: 1476-4687. doi: 10.1038/nature16961. url: https:
//www.nature.com/articles/nature16961 (visited on 09/29/2022).
[516]
David Silver et al. “Mastering the game of Go without human knowledge”. In: Nature 550.7676 (2017).
Publisher: Nature Publishing Group, pp. 354–359.
[517]
Roberta Sinatra et al. “A century of physics”. In: Nature 11.10 (2015). Publisher: Nature Publishing Group,
pp. 791–796.
[518]
Prabhu Teja Sivaprasad et al. Optimizer Benchmarking Needs to Account for Hyperparameter Tuning.
tex.copyright: arXiv.org perpetual, non-exclusive license. 2019. doi: 10.48550/ARXIV.1910.11758. url:
https://arxiv.org/abs/1910.11758.
[519]
Joar Skalse et al. Deﬁning and Characterizing Reward Hacking. tex.copyright: arXiv.org perpetual, non-
exclusive license. 2022. doi: 10.48550/ARXIV.2209.13085. url: https://arxiv.org/abs/2209.13085.
[520]
Mona Sloane. Participation-washing could be the next dangerous fad in machine learning. en. Aug. 2020.
url: https://www.technologyreview.com/2020/08/25/1007589/participation-washing-ai-trends-opinion-
machine-learning/ (visited on 12/08/2022).
[521]
Mona Sloane et al. “Participation is not a Design Fix for Machine Learning”. In: Equity and Access in
Algorithms, Mechanisms, and Optimization. EAAMO ’22. New York, NY, USA: ACM, Oct. 2022, pp. 1–6.
isbn: 978-1-4503-9477-2. doi: 10.1145/3551624.3555285. url: https://doi.org/10.1145/3551624.3555285
(visited on 12/09/2022).
[522]
Mary Slosson. Google gets ﬁrst self-driven car license in Nevada. 2012. url: https://www.reuters.com/
article/uk-usa-nevada-google-idUSLNE84701320120508.
[523]
Nathalie A. Smuha. From a ’Race to AI’ to a ’Race to AI Regulation’ - Regulatory Competition for Artiﬁcial
Intelligence. en. SSRN Scholarly Paper ID 3501410. Rochester, NY: Social Science Research Network, Nov.
2019. url: https://papers.ssrn.com/abstract=3501410 (visited on 02/17/2020).
[524]
Nate Soares et al. “Corrigibility”. en. In: AAAI, Mar. 2020. url: https://openreview.net/forum?id=
H1bIT1buWH (visited on 09/29/2022).
[525]
Irene Solaiman et al. Release Strategies and the Social Impacts of Language Models. arXiv:1908.09203 [cs].
Nov. 2019. doi: 10.48550/arXiv.1908.09203. url: http://arxiv.org/abs/1908.09203 (visited on 09/29/2022).


--- Page 58 ---

58
•
Leech et al.
[526]
Robert Solow. “Manufacturing Matters: The Myth of the Post-Industrial Economy. Review of The Myth
of the Post-Industrial Economy, by Stephen S. Cohen and John Zysman.” In: The New York Times Book
Review (July 1987), p. 36.
[527]
Haim Sompolinsky. “The theory of neural networks: The Hebb rule and beyond”. In: Heidelberg Colloquium
on Glassy Dynamics. tex.organization: Springer. 1987, pp. 485–527.
[528]
Eduardo D Sontag and Hector J Sussmann. “Backpropagation Can Give Rise to Spurious Local Minima
Even for Networks without Hidden Layers”. In: Complex Systems (1989). url: http://www.sontaglab.org/
FTPDIR/complex_systems.pdf.
[529]
Jean Souyris et al. “Formal veriﬁcation of avionics software products”. In: International Symposium on
Formal Methods. tex.organization: Springer. 2009, pp. 532–546.
[530]
James S. Spencer et al. Better, Faster Fermionic Neural Networks. arXiv:2011.07125 [physics]. Nov. 2020.
doi: 10.48550/arXiv.2011.07125. url: http://arxiv.org/abs/2011.07125 (visited on 09/23/2022).
[531]
Nikita Spirin and Jiawei Han. “Survey on web spam detection: principles and algorithms”. In: ACM
SIGKDD Explorations Newsletter 13.2 (May 2012), pp. 50–64. issn: 1931-0145. doi: 10.1145/2207243.2207252.
url: https://doi.org/10.1145/2207243.2207252 (visited on 12/07/2022).
[532]
Tejas Srinivasan and Yonatan Bisk. Worst of Both Worlds: Biases Compound in Pre-trained Vision-and-
Language Models. arXiv:2104.08666 [cs]. May 2022. doi: 10.48550/arXiv.2104.08666. url: http://arxiv.org/
abs/2104.08666 (visited on 10/13/2022).
[533]
Bernd Carsten Stahl. Artiﬁcial Intelligence for a Better Future: An Ecosystem Perspective on the Ethics of AI
and Emerging Digital Technologies. en. SpringerBriefs in Research and Innovation Governance. Cham:
Springer International Publishing, 2021. isbn: 978-3-030-69977-2. doi: 10.1007/978-3-030-69978-9. url:
http://link.springer.com/10.1007/978-3-030-69978-9 (visited on 12/06/2022).
[534]
Konstantinos Stathoulopoulos and Juan C. Mateos-Garcia. Gender Diversity in AI Research. en. SSRN
Scholarly Paper. Rochester, NY, July 2019. doi: 10.2139/ssrn.3428240. url: https://papers.ssrn.com/
abstract=3428240 (visited on 09/19/2022).
[535]
Jacob Steinhardt. Updates and Lessons from AI Forecasting. 2021. url: https://bounded-regret.ghost.io/ai-
forecasting/.
[536]
Dave Steinkraus, Ian Buck, and PY Simard. “Using GPUs for machine learning algorithms”. In: Eighth
International Conference on Document Analysis and Recognition (ICDAR ’05). tex.organization: IEEE. 2005,
pp. 1115–1120.
[537]
Charlotte Stix. “Actionable Principles for Artiﬁcial Intelligence Policy: Three Pathways”. en. In: Science
and Engineering Ethics 27.1 (Feb. 2021), p. 15. issn: 1471-5546. doi: 10.1007/s11948-020-00277-3. url:
https://doi.org/10.1007/s11948-020-00277-3 (visited on 12/06/2022).
[538]
Charlotte Stix and Matthijs M. Maas. Bridging the Gap: the case for an Incompletely Theorized Agreement
on AI policy. arXiv:2101.06110 [cs]. Jan. 2021. doi: 10.1007/s43681-020-00037-wAIET-D-20-00032. url:
http://arxiv.org/abs/2101.06110 (visited on 11/28/2022).
[539]
Emma Strubell, Ananya Ganesh, and Andrew McCallum. Energy and Policy Considerations for Deep
Learning in NLP. arXiv:1906.02243 [cs]. June 2019. doi: 10.48550/arXiv.1906.02243. url: http://arxiv.org/
abs/1906.02243 (visited on 12/07/2022).
[540]
Andreas Stuhlmüller and Jungwon Byun. Supervise Process, not Outcomes | Ought. en. O. 2022. url:
https://ought.org/updates/2022-04-06-process (visited on 11/28/2022).
[541]
Susan Hassler. “Marvin Minsky and the pursuit of machine understanding - Making machines-and
people-think [Spectral Lines]”. en-US. In: IEEE Spectrum 53.3 (Mar. 2016). url: https://ieeexplore.ieee.org/
document/7420381 (visited on 03/23/2023).
[542]
Richard Sutton. “The bitter lesson”. In: Incomplete Ideas (blog) 13 (2019), p. 12. url: http : / / www.
incompleteideas.net/IncIdeas/BitterLesson.html.


--- Page 59 ---

Ten Hard Problems in AI
•
59
[543]
Dana Swarbrick et al. “How Live Music Moves Us: Head Movement Diﬀerences in Audiences to Live
Versus Recorded Music”. eng. In: Frontiers in Psychology 9 (2018), p. 2682. issn: 1664-1078. doi: 10.3389/
fpsyg.2018.02682.
[544]
Gabriel Synnaeve. WER Are We? An attempt at tracking states of the art(s) and recent results on speech
recognition. 2022. url: https://github.com/syhw/wer_are_we.
[545]
Maxim Tabachnyk and Stoyan Nikolov. ML-Enhanced Code Completion Improves Developer Productivity.
2022. url: https://ai.googleblog.com/2022/07/ml-enhanced-code-completion-improves.html.
[546]
Araz Taeihagh, M Ramesh, and Michael Howlett. “Assessing the regulatory challenges of emerging
disruptive technologies”. en. In: Regulation & Governance 15.4 (Oct. 2021), pp. 1009–1019. issn: 1748-5983,
1748-5991. doi: 10.1111/rego.12392. url: https://onlinelibrary.wiley.com/doi/10.1111/rego.12392 (visited
on 12/06/2022).
[547]
John Tasioulas. Artiﬁcial Intelligence, Humanistic Ethics. en. url: https://www.amacad.org/publication/
artiﬁcial-intelligence-humanistic-ethics (visited on 11/25/2022).
[548]
Ian Tenney, Dipanjan Das, and Ellie Pavlick. “BERT rediscovers the classical NLP pipeline”. In: arXiv
(2019). eprint: 1905.05950.
[549]
Rachel Thomas and David Uminsky. The Problem with Metrics is a Fundamental Problem for AI. arXiv:2002.08512
[cs]. Feb. 2020. doi: 10.48550/arXiv.2002.08512. url: http://arxiv.org/abs/2002.08512 (visited on 11/28/2022).
[550]
Andreas Thome. Record Viewership for Chess as Magnus Carlsen Wins FIDE World Championship | Play
Magnus AS. no. 2021. url: https://kommunikasjon.ntb.no/announcement?publisherId=16823864&
announcementId=1062&lang=en (visited on 12/05/2022).
[551]
Adrienne Thompson. China’s ‘Sharp Eyes’ Program Aims to Surveil 100% of Public Space. en-US. Mar. 2021.
url: https://cset.georgetown.edu/article/chinas-sharp-eyes-program-aims-to-surveil-100-of-public-
space/ (visited on 12/08/2022).
[552]
Neil C. Thompson et al. The Computational Limits of Deep Learning. arXiv:2007.05558 [cs, stat]. July 2022.
doi: 10.48550/arXiv.2007.05558. url: http://arxiv.org/abs/2007.05558 (visited on 12/07/2022).
[553]
Tim Hwang and Emily S. Weinstein. Decoupling in Strategic Technologies. en-US. 2022. url: https://cset.
georgetown.edu/publication/decoupling-in-strategic-technologies/ (visited on 01/11/2023).
[554]
Rob Toews. The Biggest Opportunity In Generative AI Is Language, Not Images. en. 2022. url: https:
//www.forbes.com/sites/robtoews/2022/11/06/the-biggest-opportunity-in-generative-ai-is-language-
not-images/ (visited on 12/02/2022).
[555]
Quintão Ronan Torres and Brito Eliane P. Zamith. “Connoisseurship Taste Ritual”. In: Consumer Culture
Theory. Vol. 17. Research in Consumer Behavior. Emerald Group Publishing Limited, Jan. 2015, pp. 255–273.
isbn: 9781785603235. doi: 10.1108/S0885-211120150000017012. url: https://doi.org/10.1108/S0885-
211120150000017012 (visited on 12/05/2022).
[556]
Philip Trammell and Anton Korinek. Economic growth under transformative AI. 2020.
[557]
Michael Trazzi and Katja Grace. Katja Grace on Slowing Down AI and Surveys. 2022. url: https : / /
theinsideview.ai/katja.
[558]
Paola Tubaro and Antonio A. Casilli. “Micro-work, artiﬁcial intelligence and the automotive industry”.
en. In: Journal of Industrial and Business Economics 46.3 (Sept. 2019), pp. 333–345. issn: 1972-4977. doi:
10.1007/s40812-019-00121-1. url: https://doi.org/10.1007/s40812-019-00121-1 (visited on 12/09/2022).
[559]
Alexey Turchin, David Denkenberger, and Brian Patrick Green. “Global Solutions vs. Local Solutions for
the AI Safety Problem”. In: Big Data and Cognitive Computing 3.1 (2019). tex.article-number: 16. issn:
2504-2289. doi: 10.3390/bdcc3010016. url: https://www.mdpi.com/2504-2289/3/1/16.
[560]
Alexander Matt Turner et al. Optimal Policies Tend to Seek Power. arXiv:1912.01683 [cs]. Dec. 2021. doi:
10.48550/arXiv.1912.01683. url: http://arxiv.org/abs/1912.01683 (visited on 09/30/2022).


--- Page 60 ---

60
•
Leech et al.
[561]
U.S. Leadership in AI: A Plan for Federal Engagement in Developing Technical Standards and Related Tools.
en. url: https://itlaw.fandom.com/wiki/U.S._Leadership_in_AI:_A_Plan_for_Federal_Engagement_in_
Developing_Technical_Standards_and_Related_Tools (visited on 12/11/2022).
[562]
UK Government. About the AI Safety Summit 2023. en. 2023. url: https://www.gov.uk/government/topical-
events/ai-safety-summit-2023/about (visited on 01/08/2024).
[563]
UK Government. AI Safety Institute: overview. en. 2023. url: https://www.gov.uk/government/publications/
ai-safety-institute-overview (visited on 01/08/2024).
[564]
UK Government. The Bletchley Declaration by Countries Attending the AI Safety Summit, 1-2 November
2023. en. 2023. url: https://www.gov.uk/government/publications/ai-safety-summit-2023-the-bletchley-
declaration/the-bletchley-declaration-by-countries-attending-the-ai-safety-summit-1-2-november-
2023 (visited on 01/08/2024).
[565]
US House of Representatives. Full Committee Hearing - Artiﬁcial Intelligence: Advancing Innovation Towards
the National Interest. en. June 2023. url: https://science.house.gov/2023/6/artiﬁcial-intelligence-advancing-
innovation-towards-the-national-interest (visited on 01/08/2024).
[566]
Valerie M. Hudson. “Standing Up a Regulatory Ecosystem for Governing AI Decision-making: Principles
and Components”. In: The Oxford Handbook of AI Governance. Oxford University Press, 2021. url: https:
//academic.oup.com/edited-volume/41989/chapter-abstract/355438188 (visited on 01/11/2023).
[567]
Shannon Vallor. “Moral Deskilling and Upskilling in a New Machine Age: Reﬂections on the Ambiguous
Future of Character”. en. In: Philosophy & Technology 28.1 (Mar. 2015), pp. 107–124. issn: 2210-5441. doi:
10.1007/s13347-014-0156-9. url: https://doi.org/10.1007/s13347-014-0156-9 (visited on 11/26/2022).
[568]
Ivan Vankov and Jeﬀrey Bowers. Training neural networks to encode symbols enables combinatorial gener-
alization. tex.copyright: arXiv.org perpetual, non-exclusive license. 2019. doi: 10.48550/ARXIV.1903.12354.
url: https://arxiv.org/abs/1903.12354.
[569]
Savvas Varsamopoulos, Koen Bertels, and Carmen G. Almudever. “Decoding surface code with a distributed
neural network–based decoder”. en. In: Quantum Machine Intelligence 2.1 (June 2020), p. 3. issn: 2524-4906,
2524-4914. doi: 10.1007/s42484-020-00015-9. url: http://link.springer.com/10.1007/s42484-020-00015-9
(visited on 10/03/2022).
[570]
Ashish Vaswani et al. Attention Is All You Need. arXiv:1706.03762 [cs]. Dec. 2017. doi: 10.48550/arXiv.1706.
03762. url: http://arxiv.org/abs/1706.03762 (visited on 09/13/2022).
[571]
Gido M. van de Ven, Hava T. Siegelmann, and Andreas S. Tolias. “Brain-inspired replay for continual
learning with artiﬁcial neural networks”. In: Nature 11 (Aug. 2020), p. 4069. issn: 2041-1723. doi: 10.
1038/s41467-020-17866-2. url: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7426273/ (visited on
11/30/2022).
[572]
Maaike Verbruggen. AI & Military Procurement: What Computers Still Can’t Do. en-US. May 2020. url:
https://warontherocks.com/2020/05/ai-military-procurement-what-computers-still-cant-do/ (visited on
05/12/2020).
[573]
Pablo Villalobos et al. Will we run out of data? An analysis of the limits of scaling datasets in Machine Learning.
tex.copyright: Creative Commons Attribution 4.0 International. 2022. doi: 10.48550/ARXIV.2211.04325.
url: https://arxiv.org/abs/2211.04325.
[574]
Ruben Villegas et al. Phenaki: Variable Length Video Generation From Open Domain Textual Description.
tex.copyright: arXiv.org perpetual, non-exclusive license. 2022. doi: 10.48550/ARXIV.2210.02399. url:
https://arxiv.org/abs/2210.02399.
[575]
Terrance de Vries et al. “Does Object Recognition Work for Everyone?” In: IEEE, 2019, pp. 52–59. url:
https://openaccess.thecvf.com/content_CVPRW_2019/html/cv4gc/de_Vries_Does_Object_Recognition_
Work_for_Everyone_CVPRW_2019_paper.html (visited on 11/04/2022).


--- Page 61 ---

Ten Hard Problems in AI
•
61
[576]
Ben Wagner. “Ethics As An Escape From Regulation. From “Ethics-Washing” To Ethics-Shopping?” en. In:
Being Proﬁled: Cogitas Ergo Sum. Ed. by Emre Bayamlioglu et al. Amsterdam University Press, Dec. 2018,
pp. 84–89. isbn: 9789048550180. url: https://www.degruyter.com/document/doi/10.1515/9789048550180-
016/html?lang=en (visited on 12/08/2022).
[577]
Kevin Wang et al. Interpretability in the Wild: a Circuit for Indirect Object Identiﬁcation in GPT-2 small.
arXiv:2211.00593 [cs]. Nov. 2022. doi: 10.48550/arXiv.2211.00593. url: http://arxiv.org/abs/2211.00593
(visited on 11/30/2022).
[578]
Maya Wang. The Robots are Watching Us. en. Apr. 2020. url: https://www.hrw.org/news/2020/04/06/robots-
are-watching-us (visited on 12/08/2022).
[579]
Thomas Wang et al. What Language Model Architecture and Pretraining Objective Work Best for Zero-Shot
Generalization? tex.copyright: arXiv.org perpetual, non-exclusive license. 2022. doi: 10.48550/ARXIV.2204.
05832. url: https://arxiv.org/abs/2204.05832.
[580]
Semantic Web. Common Crawl. 2022. url: https://web.archive.org/web/20140701235708/http://
semanticweb.com/common-crawl-to-add-new-data-in-amazon-web-services-bucket_b27341.
[581]
Jason Wei. 137 emergent abilities of large language models. en-US. 2022. url: https://www.jasonwei.net/
blog/emergence (visited on 11/28/2022).
[582]
Jason Wei et al. Emergent Abilities of Large Language Models. arXiv:2206.07682 [cs]. Oct. 2022. doi:
10.48550/arXiv.2206.07682. url: http://arxiv.org/abs/2206.07682 (visited on 01/08/2024).
[583]
David Weisstanner. “COVID-19 and welfare state support: the case of universal basic income”. In: Policy
and Society 41.1 (2022). Publisher: Oxford University Press UK, pp. 96–110.
[584]
Angus Whitley. “AI Knows How Much You’re Willing to Pay for Flights Before You Do”. In: Bloomberg
(2022). url: https://www.bloomberg.com/news/articles/2022-10-20/artiﬁcial-intelligence-helps-airlines-
ﬁnd-the-right-prices-for-ﬂight-tickets.
[585]
Jess Whittlestone and Samuel Clarke. “AI Challenges for Society and Ethics”. en. In: The Oxford Handbook
of AI Governance. Ed. by Justin Bullock et al. Oxford University Press, Apr. 2022. isbn: 978-0-19-757932-9.
doi: 10.1093/oxfordhb/9780197579329.013.3. url: https://oxfordhandbooks.com/view/10.1093/oxfordhb/
9780197579329.001.0001/oxfordhb-9780197579329-e-3 (visited on 06/07/2022).
[586]
Bernard Widrow. “Generalization and information storage in network of adaline ’neurons’”. In: Self-
organizing Systems. Ed. by Marshall Clinton Yovits. Spartan Books, 1962, pp. 435–462.
[587]
Bernard Widrow and Michael A Lehr. “30 years of adaptive neural networks: perceptron, madaline, and
backpropagation”. In: Proceedings of the IEEE 78.9 (1990). Publisher: IEEE, pp. 1415–1442.
[588]
Christoph Winter. The Challenges of Artiﬁcial Judicial Decision-Making for Liberal Democracy. en. SSRN
Scholarly Paper. Rochester, NY, Mar. 2021. url: https://papers.ssrn.com/abstract=3933648 (visited on
11/14/2022).
[589]
Bernd W. Wirtz, Jan C. Weyerer, and Benjamin J. Sturm. “The Dark Sides of Artiﬁcial Intelligence: An
Integrated AI Governance Framework for Public Administration”. en. In: International Journal of Public
Administration 43.9 (July 2020), pp. 818–829. issn: 0190-0692, 1532-4265. doi: 10.1080/01900692.2020.
1749851. url: https://www.tandfonline.com/doi/full/10.1080/01900692.2020.1749851 (visited on
12/09/2022).
[590]
Nicholas Wright. “How Artiﬁcial Intelligence Will Reshape the Global Order”. en-US. In: Foreign Aﬀairs
(Oct. 2022). issn: 0015-7120. url: https://www.foreignaﬀairs.com/articles/world/2018-07-10/how-
artiﬁcial-intelligence-will-reshape-global-order (visited on 12/06/2022).
[591]
Zhaofeng Wu et al. Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models
Through Counterfactual Tasks. arXiv:2307.02477 [cs]. Aug. 2023. doi: 10.48550/arXiv.2307.02477. url:
http://arxiv.org/abs/2307.02477 (visited on 01/08/2024).


--- Page 62 ---

62
•
Leech et al.
[592]
Laure Wynants et al. “Prediction models for diagnosis and prognosis of Covid-19: Systematic review and
critical appraisal”. en. In: BMJ 369 (Apr. 2020), p. m1328. issn: 1756-1833. doi: 10.1136/bmj.m1328. url:
https://www.bmj.com/content/369/bmj.m1328 (visited on 09/29/2022).
[593]
Selina Xu. Microsoft Chatbot SpinoﬀXiaoice Reaches $1 Billion Valuation. 2021. url: https : / / www.
bloomberg.com/news/articles/2021- 07- 14/microsoft- chatbot- spinoﬀ- xiaoice- reaches- 1- billion-
valuation?leadSource=uverify%20wall.
[594]
Kouichi Yamaguchi et al. “A neural network for speaker-independent isolated word recognition.” In:
ICSLP. 1990.
[595]
Chengrun Yang et al. Large Language Models as Optimizers. arXiv:2309.03409 [cs]. Dec. 2023. doi: 10.
48550/arXiv.2309.03409. url: http://arxiv.org/abs/2309.03409 (visited on 01/08/2024).
[596]
Xiangli Yang et al. “A Survey on Deep Semi-supervised Learning”. In: CoRR abs/2103.00550 (2021). url:
https://arxiv.org/abs/2103.00550.
[597]
Norman Yao. “Quantum Simulation: Advances, Platforms, and Applications National Academies of
Sciences, Engineering, and Medicine.” en. In: Frontiers of Engineering: Reports on Leading-Edge Engineering
from the 2018 Symposium. 2018. doi: 10.17226/25333. url: https://www.nap.edu/read/25333/chapter/7
(visited on 10/13/2022).
[598]
Karen Yeung, Andrew Howes, and Ganna Pogrebna. AI Governance by Human Rights-Centred Design,
Deliberation and Oversight: An End to Ethics Washing. en. SSRN Scholarly Paper. Rochester, NY, June 2019.
doi: 10.2139/ssrn.3435011. url: https://papers.ssrn.com/abstract=3435011 (visited on 12/08/2022).
[599]
Yujia Li et al. “Competition-level code generation with AlphaCode”. In: Science 378.6624 (2022). url:
https://www.science.org/doi/10.1126/science.abq1158.
[600]
Eric Zelikman et al. Self-Taught Optimizer (STOP): Recursively Self-Improving Code Generation. en. Oct.
2023. url: https://arxiv.org/abs/2310.02304v1 (visited on 01/08/2024).
[601]
Rowan Zellers et al. MERLOT: Multimodal Neural Script Knowledge Models. tex.copyright: arXiv.org
perpetual, non-exclusive license. 2021. doi: 10.48550/ARXIV.2106.02636. url: https://arxiv.org/abs/2106.
02636.
[602]
Andy Zeng et al. Socratic Models: Composing Zero-Shot Multimodal Reasoning with Language. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2022. doi: 10.48550/ARXIV.2204.00598. url: https://arxiv.org/
abs/2204.00598.
[603]
Chiyuan Zhang et al. Understanding deep learning requires rethinking generalization. arXiv:1611.03530 [cs].
Feb. 2017. doi: 10.48550/arXiv.1611.03530. url: http://arxiv.org/abs/1611.03530 (visited on 10/13/2022).
[604]
Daniel Zhang et al. The AI Index 2022 Annual Report. arXiv:2205.03468 [cs]. May 2022. doi: 10.48550/arXiv.
2205.03468. url: http://arxiv.org/abs/2205.03468 (visited on 11/13/2022).
[605]
Stephan Zheng et al. “The AI Economist: Taxation policy design via two-level deep multiagent reinforce-
ment learning”. en. In: Science Advances 8.18 (May 2022), eabk2607. issn: 2375-2548. doi: 10.1126/sciadv.
abk2607. url: https://www.science.org/doi/10.1126/sciadv.abk2607 (visited on 12/01/2022).
[606]
Barret Zoph and Quoc V. Le. Neural Architecture Search with Reinforcement Learning. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2016. doi: 10.48550/ARXIV.1611.01578. url: https://arxiv.org/
abs/1611.01578.
[607]
Shoshana Zuboﬀ. The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of
Power. 1st. ACM, 2018. isbn: 978-1-61039-569-4.
[608]
Stuart Zweben and Betsy Bizot. 2021 Taulbee Survey. en-US. Tech. rep. Computer Research Association,
May 2022. url: https://cra.org/wp-content/uploads/2022/05/2021-Taulbee-Survey.pdf (visited on
09/19/2022).


--- Page 63 ---

Ten Hard Problems in AI
•
63
FIGURES AND TABLES
Fig. 1. The path to the DL breakthrough in computer vision (2010–2012), using [108, 310] as an exemplar, following [58, 55,
207]. No part of this graph is a necessary condition (besides massively increased computation, here represented by GPUs,
and some stabilizing activation function); see [28] for a very diﬀerent minimal path. The “data deluge” is the internet-driven
availability of data on more or less everything [53]. The “Common Task Framework” is competitive benchmarking: the use of
fixed datasets and objectives, with held-out test data, plus a culture of open competition (Liberman [348] dates it to 1986, but
see also [470]). ImageNet is the most famous example of a common task: for its time, it was an extremely large and diverse
image classification dataset [144]. Empirical risk minimization is the fundamental method of machine learning: creating a
training set and a test set and using training performance as an estimate of true performance [241]. Convolutional neural
networks (CNNs) were the original network architecture employed during the DL lifoﬀ[330]. Max pooling (MaxPool) is an
approach to reducing the state of a convolutional layer ([468], following [594]). Dropout prevents overfiting by randomly
deleting connections between units ([244] following [527]). Stochastic gradient descent is a remarkably eﬀicient general
optimizer ([71], following [480]). The “depth eﬀiciency hypothesis” was the long-standing belief that adding layers should
improve the statistical eﬀiciency of networks, exemplified in [55, 57] and later proven in [444]. Graphical processing units
(GPUs) sped up training by an order of magnitude or more [536]; reuse of this pre-existing hardware represented a lucky
ticket in the “hardware lotery” [249], shifing future hardware investments towards DL operations. Backpropagation is the
reigning method of assigning “credit” to particular weights, enabling gradient-based learning in neural networks ([330, 489]
following pioneering work by [586, 159, 350]. The rectified linear unit (ReLU) is an activation function which avoids the
vanishing/exploding gradient problem ([403], following [187]). “Depth” is the number of layers between input and output in
the network; early systems counted two hidden layers as “deep” [243, 58] while AlexNet had eight—and, ultimately more
importantly, 60 million parameters [310]. (AlexNet was not the first success in computer vision or neural networks; eight
years before AlexNet, Kussul and Baidyk achieved beter than 99% accuracy in handwriting recognition [316].)


--- Page 64 ---

64
•
Leech et al.
Fig. 2. Timeline of computation required (in floating point operations, FLOPs) to train leading machine learning systems
(n=121): note the exponential increase. A “milestone” model is one that has “an explicit learning component, showcases
experimental results, and advances the state-of-the-art and at least one notability criterion” (>1000 citations, retrospective
historical importance, deployed in a notable context) [504]. Where the total compute was not given by the paper, the Epoch
team estimated it using methods from [21]. Using a separate fit for models more than three-quarters of a standard deviation
above that year’s mean compute, they obtain three plausible trends, somewhat robust to the date or size thresholds. (Note the
huge practical significance of a slightly diﬀerent slope on an exponential scale.) The graph depicts three eras with diﬀerent
shading: the pre-deep learning period 1950–2010; the deep learning lifoﬀperiod 2010–2016; and the large-scale period
2016–2022. Each
circle is one milestone system, n=91; triangles denote a separate cluster of anomalously large models,
n=16. The graph shows that the exponential increase in demand for computation per model accelerated around 2010, when
deep learning became popular; it also shows the introduction of anomalously large models in 2016. Adapted with permission
from [504].


--- Page 65 ---

Ten Hard Problems in AI
•
65
Fig. 3. The path to the large scale era in deep learning (2016–present), using GPT-2 as an exemplar. The most important
node in this graph is pre-training, read as a stand-in for massively scaled parameter counts. Adam (afer “adaptive moment
estimation”) is a robust replacement for stochastic gradient descent which maintains and adapts many separate learning
rates [294]. Unsupervised pretraining (preparing a neural network for later tasks by learning generally useful features from
unlabeled data) gained new relevance when used for sequence modelling [130, 146] (rather than its original purpose, stable
network initialization [168]). Large language models depend on web scraping at the scale of the entire internet [580], which
in turn depends on relaxed atitudes to copyright on the internet. ULMFiT and ELMo pioneered unsupervised training that
produced transferable skills and embeddings for NLP [254, 452, 461]. GELU is an activation function with beter implicit
regularization [236]. Atention weights the parts of several input sequences in proportion to their relevance to the decoding
at the current training step [37]; self-atention, o n the other hand, weights parts of a single input sequence, allowing us to
infer dependencies [99]. Byte-pair encoding tokenizes input text into a code suitable for learning subword representations
([503], following [190]). The Transformer is a network built from many layers of atention (“multi-headed atention”), plus a
positional encoding separate from the text (essentially an accumulator indicating word order) [570]. The decoder-only form
of the Transformer simplifies the architecture and improves zero-shot generalization at the cost of being unidirectional [353];
many state-of-the-art models are instances [579]. Layer normalization stabilizes training by using summary statistics of
inputs to an entire layer of the network [34]. Model parallelism splits a model across training machines (ofen by layer) for
enormous model sizes and parallel speedups [135].


--- Page 66 ---

66
•
Leech et al.
1 Supervised learning is the classic statistical task of ﬁtting data labeled with the “ground truth” (output
data which is at least roughly correct) [329]. Self-supervised learning uses entirely unlabeled data, avoiding
expensive labeling; semi-supervised learning expands a labeled dataset with unlabeled data [596].
2 Discriminative models draw a decision boundary in data space, while generative models instead learn the
distribution of the data; this allows them to generate typical examples, as seen in the GPT series [79, 428] &
DALL-E [208].
3 Single-task learning refers to systems being trained on only one task, as opposed to learning representations
useful for multiple tasks.
4 Single modality systems (trained on only one data type) have been followed by multi-modal systems handling
e.g. both text and image data.
5 Relatively domain-speciﬁc architectures like convolutional and recurrent neural networks were followed by
the Transformer’s state-of-the-art results in language, vision, audio, and more [349].
6 In the liftoﬀera models could be trained on a single workstation, but scaling requirements have led to
massively distributed training across thousands of machines.
7 ML hardware largely comprises repurposed consumer-grade GPUs, succeeded (at the top end) by ASIC
“accelerators” specialized for ML operations like matrix multiplication [476].
8 Connectivity refers to the degree of connection between units; “dense” (fully-connected) networks could
eventually give way to more eﬃcient, sparser models [245].
Fig. 4. Comparison of rough tendencies between the two eras in deep learning research, besides the key diﬀerence that
training in the Large Scale Era involves more than a billion times more data and compute [504]. See Figure 2 for definitions
of the eras.


--- Page 67 ---

Ten Hard Problems in AI
•
67
Fig. 5. HP#2: The “Swiss cheese” model of safety engineering as applied to machine learning systems. To reduce the probability
of hazards, we can adopt a “defense in depth” approach: a series of mechanisms that each work against some subset of
hazards. Systematic safety combines a strong safety culture among developers and users with AI systems that detect and
block hazards early. Monitoring involves gaining greater insight into AI systems themselves, for instance through anomaly
detection [237]. Robustness measures increase systems’ ability to perform gracefully in the presence of extreme events and
adversarial action. Alignment—ensuring that the goals of advanced systems reflect human values—is the subject of HP#3.
Adapted with permission from [238].


--- Page 68 ---

68
•
Leech et al.
Fig. 6. HP#3: Alignment approaches and how they relate to diﬀerent alignment milestones. Intent alignment is making a
system try to do what we intend it to. It factors into objective robustness (that the system successfully infers what we intend,
even when operating in very diﬀerent conditions from training) and outer alignment (that the objective given to the system
captures important variables and is not merely correlated with the true goal) [260]. Inner alignment (discussed above under
“emergent goals”) is ensuring that the goal a system ends up acting under is safe [260, 337]. A “corrigible” system is one with
no incentive to prevent shutdown or modification by users [524, 218]. For a more detailed and up-to-date review, see [332].


--- Page 69 ---

Ten Hard Problems in AI
•
69
Fig. 7. HP#3: The greater alignment problem: even if methods of intent alignment succeed, we need them to cover powerful
systems and to be adopted by a huge variety of actors, which requires the method to have litle overhead in training cost or
performance (a low “alignment tax”), as well as strong understanding of the risk among AI researchers (“capability caution”).
Simultaneously, other misaligned systems need to be detected [70], and alignment problems arising from the perverse
interaction of individually-aligned systems solved [158, 121]. Figure inspired by [260, 101].


--- Page 70 ---

70
•
Leech et al.
Fig. 8. HP#4: AI creates game-changing opportunities for scientific exploration. ML systems can be trained on high-fidelity
but computationally intensive physics simulations. The trained model produces a compact approximation of the target
physical system, and can then be used as a proxy for inference. Alternatively, classifiers can be used to characterize actual
data from experimental apparatus. Figure adapted from [76].


--- Page 71 ---

Ten Hard Problems in AI
•
71
Fig. 9. HP#6: National origin and current location of leading AI researchers (using undergraduate institution as a proxy
for origin country, and using publication in the proceedings of one top conference, NeurIPS, as a proxy for top researcher
status), 2019. We see that the US is the largest beneficiary by far, gaining 40% of the world’s top researchers. The ‘Remaining’
countries represent more than half of the world’s population, but only 10% of its AI researchers. Data from the MacroPolo
Global AI Tracker [372].


--- Page 72 ---

72
•
Leech et al.
Fig. 10. HP#7: Topics covered in “AI principles” issued by governments, non-governmental organizations, academics, and
industry. Citations to the principles and to the associated legislation and technical agendas are collected in Table A.7. Figure
inspired by [221].


--- Page 73 ---

Ten Hard Problems in AI
•
73
Fig. 11. HP#8. The eﬀect of AI applications on the international order as expected by researchers at IFSH. “C4ISR” is
Command, Control, Communications, Computers, Intelligence, Surveillance, and Reconnaissance: i.e. the entire military and
national security information chain. Adapted with permission from [173]
.


--- Page 74 ---

74
•
Leech et al.
Fig. 12. HP#9: The production of AI governance: actors and mechanisms. ‘Civil society’ here includes academics, consultants,
and think tanks. Independent AI developers are not to be overlooked, since they develop tools and products outside regulatory
structures, ofen using open-sourced weights from industry and academia. Map inspired by [478, 399].


--- Page 75 ---

Ten Hard Problems in AI
•
75
Fig. 13. Potential humanist problems caused by automation technologies including AI. Adapted with permission from [131].


--- Page 76 ---

Ten Hard Problems in AI
•
1
ELECTRONIC SUPPLEMENT
Note: The entire bibliography is available as a Zotero library at
https://www.zotero.org/groups/4774748/the_hard_problems_bibliography/library.
A
Additional Material for Each Hard Problem
A.1
Additional Citations: HP#1
While deep learning led to an improved theory of learning (particularly of the benign overﬁtting phenomenon
[115, 35, 14]), currently we cannot predict whether a DL system will generalize—that is, actually solve the
task—when provided with out-of-distribution data [110]. However, humans may not be as sample-eﬃcient as they
seem, since each brain is initialized with inductive biases from millions of years of evolutionary experience—our
pretraining [171, 93, 149]. In the meantime, ML methods become incrementally more sample eﬃcient year by
year, with the occasional dramatic improvement [155, 169, 83, 82, 99].
Other researchers skeptical about the prospects of deep learning alone include [95, 111] and [22].
A.2
Additional Citations: HP#2
Many authors have noted that there is a signiﬁcant gap between the average performance of AI systems and the
high level of assurance required for deployment in safety-critical environments [76, 38]. Additional references for
the potential for AI to create “normal accidents” include [109, 167].
Indeed, many ML systems are now so complex that emergent modes of operation and failure are the norm [165,
85].
As Stuart Russell notes: “we are a long way from being able to prove any such theorem [about a behavior being
beneﬁcial for humans] for really intelligent machines operating in the real world” [140]. A scalable approach
might involve learning (approximate) models of safety properties and the invariants we want our systems to
respect.
Technology Readiness Levels[100] are a commonly used scale for describing the maturity of a new technology
with regard to its suitability for deployment.
Human oversight, augmented with AI anomaly detection and calibration warnings, holds promise as a com-
ponent of safety systems [66]. To be viable, such human-in-the-loop systems need to reliably identify cases on
which they can safely operate on their own, and only refer cases to human operators which are both impactful
and uncertain.[10].
However, extracting guarantees that neural networks will perform within bounds is a daunting task: one classic
approach amounts to solving satisﬁability problems with as many variables as the network has parameters (i.e.
millions or more) [9]. Practical approaches sacriﬁce exactness and/or completeness [173], and remain limited to
small-to-medium parameter counts. Recent work considers increasingly realistic networks, including nonlinear
activations and modern architectures [168]. VNN-COMP, a common task competition, ﬁnds that hybrid GPU-
enabled methods can produce impressive results on networks of up to around 100,000 neurons [13, 172].
Figure 14 shows three approaches to handling the variance of ML performance [114]. Panel (i) shows a system
that produces unacceptable performance from time-to-time (as demonstrated by the area to the left of the dashed
red line). One approach (ii) adds a failsafe that detects when an AI system might fail, with the result that not
many situations are accepted in which the AI’s performance is low but acceptable. The approach in panel (iii)
ELECTRONIC SUPPLEMENT


--- Page 77 ---

2
•
Leech et al.
avoids opaque AI systems entirely, replacing them with inherently interpretable (or architecturally transparent)
systems which users can prove to be safe. Another approach is to reduce the variance of AI performance, either
by making the systems themselves more robust, or by improving our understanding of them, as in panel (iv).
This ﬁgure ignores the cost of producing each system.
Redundancy can be used to produce a reliable system from less reliable components [106]: if a self-driving car
has two independent stop-sign detectors, each of which is 99.9% reliable, and the driving system stops when either
detects a stop sign, then the combined system should be 99.9999% reliable. However, failures in ML perception
generally correlate, greatly reducing the eﬀectiveness of this method. Multiple researchers [57, 153] have found
that “a wide variety of models with diﬀerent architectures trained on diﬀerent subsets of the training data
misclassify the same adversarial example” [57].
Another way to improve robustness is to create robust measures of intelligence or generality for AI systems [69,
70], and to use less artiﬁcial metrics and more inclusive methods from the natural sciences when studying AI
systems [136, 15, 102].
Interpretability is especially important when the loss function used to train the system may not fully represent
the interests of the user (or the subject of modeling) [104, 39].
AI for assurance
The Eliciting Latent Knowledge (ELK) agenda attempts to develop AI techniques to deduce what
a system “believes” about its environment; this line of work could be extremely useful for avoiding unexpected
and catastrophic outcomes [24].
AI could be used to detect anomalous inputs, and hence whether the system is operating outside (the training)
distribution to an extent which could jeopardize its performance [66, 68].
Adversarial training synthesizes misleading edge cases for other AI systems during their training, making
failure less likely when the system being trained encounters such cases in production [174, 79].
Security
The above concerns the safety of ML systems: that is, their accident risk. The other major category
of hazard is adversarial attack. The essence of an adversarial situation is that the environment adapts to your
countermeasures: the noise aﬀecting your system can thus be crafted to be maximally perverse [51]. End users,
data subjects or third parties may attempt to manipulate AI systems into making decisions and predictions which
beneﬁt them or harm others [20]. This serves to create a second mode in the performance distribution, with an
unusually high probability of unusually bad outcomes.
One security measure is multi-criteria evaluation: system performance should be assessed with more than
one metric, and a threshold should be met on all metrics [102]. (For instance, a language model may perform
exceptionally well at holding a realistic conversation, while simultaneously leaking the personal information
used to train it to malicious third parties [132] or producing oﬀensive output.)
Interpretability and simplicity make systems easier to attack, even as they improve worst-case outcomes [104,
52]. Simple, deterministic systems are easier for attackers to understand and thus abuse. Tools which help us ﬁnd
(and ﬁx) adversarial examples will also help attackers ﬁnd (and thus exploit) adversarial examples [158, 163]. It is
thus reasonable to assume that such attacks will become more feasible [20], not least through the use of data
poisoning [51] and neural backdoors [56].
In addition to being constructed in the typical way, we can derive “architecturally” [74] interpretable models by
training a complex model and then paring it down. Mechanistic interpretability investigates the circuits created
during training and deduces what they are doing, ideally to the level of the exact algorithm it has learned [123].
For example, recent work has reverse-engineered algorithms developed inside Transformers, including at the
100 million parameter scale [116, 124, 162]. Again ideally, the algorithm discovered could then be executed as a
white-box deterministic program.
ELECTRONIC SUPPLEMENT


--- Page 78 ---

Ten Hard Problems in AI
•
3
Probability
Performance
i)
Probability
Performance
ii)   Add failsafes
Probability
Performance
iii)   Interpretable System
Probability
Performance
iv)   Reduce variance
P (Performance = X)
Minimum safe performance
P (Failsafes not triggered)
Fig. 14. Assurance is the atempt to reduce the probability of critical failure to an acceptable level. Panel (i) depicts an AI
system that broadly performs acceptably, but which has an unacceptable region (to the lef of the doted red line). This might
correspond to an AI radiologist misdiagnosing an extremely diﬀicult mammogram, or a car driving on a slick and winding
road. The approach in panel (ii) detects poor conditions and refuses to operate, which an be achieved by gating AI with
less advanced systems that have well-understood failure modes; panel (iii) depicts a system that has a limited operational
range, but that range can be beter understood; panel (iv) shows a system designed to have reduced variance in performance,
perhaps designed using a system designed to produce “adversarial robustness.” Interventions which reduce variance while
also reducing average performance can be worthwhile, if they reduce the probability of catastrophic failures.
ELECTRONIC SUPPLEMENT


--- Page 79 ---

4
•
Leech et al.
For tabular data, generalized additive models are an inherently interpretable model class (implemented in
the open-source InterpretML library [120]). Similarly, the ﬂedgling subﬁeld of mechanistic interpretability also
recently received a dedicated library which helps open the black box of neural networks [117].
Today we have only rudimentary control over high-level properties of trained models like values and goals [54].8
Many current systems display some form of misaligned behavior [94, 97, 98, 17, 91, 152].
A.3
Additional Citations: HP#3
Approaches
The alignment ﬁeld is under active development, with new perspectives and concepts arising and
with a range of diﬀerent problem decompositions, naming conventions [11] and contested hypotheses [27]. In
their data-driven survey, Kirchner et al. discover ﬁve clusters in the alignment literature [89]:
(1) [Empirical] agent alignment concerns current “agentic” systems, i.e. those trained to perform complex
actions in a simulated or real environment, usually with RL. Representative work includes safe RL and
reward learning [63, 81], assistance games [146, 170], and adversarial training [174].
(2) Foundational work aims to develop strong theoretical frameworks to guide alignment research. Represen-
tative work includes agent foundations (formal theories of agency and decision-making) [150, 36], causal
incentives (analyzing when a system is in practice being trained for) [88], and natural abstractions [166].
(3) Tool alignment concerns nonagentic systems, i.e. classic classiﬁcation, regression, or generative systems.
Representative work includes ML safety [10, 68], the alignment of large language models [128, 86, 67, 87],
adversarial training [79, 174], scalable oversight [18] and interpretability research [73, 122].
(4) AI governance concerns social and political factors in the transition to advanced AI. (See Section 3.9.)
(5) Value alignment, “understanding and extracting human preferences, and designing methods that stop AI
systems from acting against these preferences” [89]. Representative work includes [101, 21, 54, 50, 134].
A.4
Additional Citations: HP#4
A.4.1
AI to promote access One great promise of AI is its potential for greater inclusion, for instance of those
with disabilities or those who do not speak the dominant language.
Access for people with disabilities
People with disabilities have traditionally lacked power in industrialized
societies [55]. As a result, people with disabilities have often been needlessly disenfranchised by technological
progress. Legislation such as the Americans with Disabilities Act of 1990 attempts to address this injustice by legal
mandating accessibility. In so doing, such legislation also supports a market for accessibility devices, allowing
the cost of R&D to be spread over a much larger customer base.
Technology can both empower and disadvantage people with disabilities: the same speech-to-text technology
that powers live captioning of videos on services such as YouTube and Zoom also powers voice assistants—devices
which are almost entirely unusable by people who are deaf. In order for all to beneﬁt from the promise of AI, it is
critical that AI systems be designed with all users in mind. Promising new developments include brain-computer
interfaces to allow people with paralysis to operate computers [121] or, eventually, wheelchairs and powered
prostheses [139, 137]. Too often, developers of technology overlook straightforward modiﬁcations that could
make their systems more accessible. For example, speech-to-text systems have poor accuracy for deaf users
out-of-the-box, but accuracy can be dramatically improved if the systems are explicitly trained on the voices of
deaf individuals [47].
Linguistic access
For more than ﬁfty years, English has been the dominant language of science and technology.
However, the majority of the world’s population do not speak English, and the majority of English speakers are
8This section factors out risks from intentional misuse of AI, and instead asks how to handle the inherent risks of intelligent systems,
particularly advanced systems with broad capabilities. We discuss misuse risk in sections 3.2 and 3.8.
ELECTRONIC SUPPLEMENT


--- Page 80 ---

Ten Hard Problems in AI
•
5
not native speakers. One side eﬀect of this is that “non-English language articles are commonly excluded from
published systematic reviews” [138]—and this is true of the present article.
High-ﬁdelity translation, including the translation of all written text, spoken language, and sign language into
all other languages, is now well within our capabilities and will dramatically ease linguistic barriers worldwide.
Crucially, it will also allow non-English speakers to access large-scale AI systems which use English as the
primary interface. While systems such as GPT-4 can translate between English and non-English languages, their
performance in English is generally better than in non-English languages due to the availability of training data.
The movement to produce language models for non-English languages (along with multilingual models) is thus of
enormous importance, given that the overwhelming majority of people cannot use the English-language models
which are the current focus of innovation [164].
A.5
Additional Citations: HP#5
Economic studies of technological impacts on society have a long history, and the analysis of AI ﬁts into
this tradition well. The economics of AI is an established subﬁeld within growth theory and the economics of
innovation [107, 40], with regular conferences and contributions from top economists [2, 4, 112]. Other approaches
for incorporating AI eﬀects into growth theory include [65, 141, 60].
However, the literature has serious limitations. The operational deﬁnitions of AI used are often vague and even
internally inconsistent. Theoretical studies usually use a broad deﬁnition of AI that encompasses most potential
use cases, but empirical studies tend to use a narrow deﬁnition of AI, often as a synonym for robotics, computer
numerical control, robotic process automation, and traditional automation methods [107].
AI is best thought of as a general purpose technology (GPT)—a “single generic technology, recognizable as
such... [that] comes to be widely used, to have many uses, and to have many spillover eﬀects” [103, 156]. Past
examples of such technologies include electricity, lean production processes, and the internet [103].
However, data on AI tool use are extremely limited. In contrast, data on the use of industrial robots are available
at the national level [3], but even these data are mostly limited to summary statistics: as Seamans and Raj highlight,
we lack data at the level of individual ﬁrms [144]. This precludes in-depth studies on fundamental questions,
such as whether robotics and AI complement or substitute labor while simultaneously clearly eliminating jobs.
Other classic studies on the impact of AI on automation include [127, 119, 12].
Another approach to ameliorating potential eﬀects on human labor involves requiring companies to hire a
certain number of workers per large unit of proﬁt [92].
A natural next step for AI economics is to collect granular data on capabilities and on ﬁrm-level and intra-ﬁrm
utilization. We must also model the labor eﬀects of speciﬁc AI technologies in detail, as in [142].
A.6
Additional Citations: HP#6
Disciplinary diversity
Because the Hard Problems are interdisciplinary and often contain social and political
subproblems, solving them will require insights from across the sciences and humanities [78, 136]. Many ﬁelds
have responded to the rise of AI with a new subﬁeld—the economics of AI, the philosophy of AI, and so on.
ELECTRONIC SUPPLEMENT


--- Page 81 ---

6
•
Leech et al.
A.7
Additional Citations: HP#7
Principal citation
Associated
legislation
Associated
technical agenda
European Commission
[44]
[1]
White House
[16]
[49]
OECD
[154]
UK
[118]
[159]
China
[43]
[157]
AI4People
[7]
UNESCO
[160]
IEEE
[75]
PAI
[129]
[130]
Asilomar
[77]
[6]
AI Now
[28]
NeurIPS
[23]
FAT/ML
[46]
[135]
Montréal
[32]
[113]
OpenAI
[126]
[125]
Meta
[45]
[5]
DeepMind
[33]
[34]
Google
[58]
[59]
Table 1. Citations for Figure 10
A.8
Additional Citations: HP#8
This problem covers foreign policy, the stability of the international order, and potential international governance
mechanisms under current and coming AI shocks. (HP#9 focuses instead on domestic governance.)
AI systems have a range of potential applications in militaries and national security [61, 31, 131].
In the middle of the spectrum, conventional warfare is becoming faster and more unpredictable due to the
use of AI systems to operate remote platforms, interpret sensor information, and accelerate tactical decision-
making, raising the risk of ’ﬂash wars’ [48] caused by loss of control, data poisoning issues [105] or destabilizing
interactions between AI systems.
AI can, and thus may, change how states use targeted cyber operations and coercion against opponents [53].
Conﬁdence-building measures have been used to stabilize expectations and avoid miscommunication around
military technologies, and these measures could play a key role in governing military AI [71, 72].
States have a shared interest in preserving stability, preventing arms races, and preventing proliferation among
malicious actors, and can draw on a long history of arms control agreements [143, 108]. Militaries may increasingly
come to recognize that technological supremacy does not always equate to improved national security, if it drives
one or both sides to play ’technology roulette’ [30] by prematurely adopting unreliable or insecure systems.
A classic case study of how technologies can impact international relations deals with the development of
armored “dreadnought” battleships, which sparked an arms race in the run-up to World War I [161].
Digital technologies of the past enabled non-state civil society actors to take a much more prominent role
participating in and shaping international negotiations [133].
ELECTRONIC SUPPLEMENT


--- Page 82 ---

Ten Hard Problems in AI
•
7
AI may also change the nature of conﬂict, making wars less predictable and more diﬃcult to limit by augmenting
cyber, conventional, and nuclear capabilities [90]. Finally, it may lead to the creation of new players in the
geopolitical arena [37].
The AI eﬀect is largely a structural risk, in the sense used by Dafoe: “When we think about the risks arising
from the combustion engine—such as urban sprawl, blitzkrieg oﬀensive warfare, strategic bombers, and climate
change—we see that it is hard to fault any one individual or group for negligence or malign intent... technology
can produce social harms, or fail to have its beneﬁts realized, because of a host of structural dynamics. The
impacts from technology may be diﬀuse, uncertain, delayed, and hard to contract over. Existing institutions are
often not suited to managing disruption and renegotiating arrangements” [29].
“AI Governance: Overview and Theoretical Lenses” provides an excellent introduction to the current state of
AI governance [29].
Although the EU leads in AI regulation, it is struggling to catch up in actual AI research, as well as other
areas such as the manufacture of semiconductors [64]. The EU typically employs a risk-based approach that
distinguishes between diﬀerent AI applications and proposes distinct regulations for each, and violators are
subject to stiﬀpenalties calculated as percentages of their world-wide revenues. As a result, the EU’s regulatory
capacity and market size also give it signiﬁcant inﬂuence beyond its borders [19], a phenomenon known as
the “Brussels eﬀect” [19, 147]. Seeking to ensure that US tech companies comply with its laws, the EU recently
established an oﬃce in San Francisco [41].
Although the EU’s approach has been praised for its ethical considerations and protection of fundamental
rights, the ultimate impact of this regulation is far from clear.
Global AI regulation is still in its early stages, but is developing rapidly: Organization for Economic Co-
operation and Development (OECD) members and several other states have agreed to a set of AI Principles, and
the G7 has created a Global Partnership on AI. International organizations such as the United Nations Educational,
Scientiﬁc and Cultural Organization (UNESCO), the Council of Europe, and the OECD have also convened
multi-stakeholder groups to draft policy instruments in this area [26]. International standards developed by
organizations such as the International Organization for Standardization (ISO) and the Institute of Electrical and
Electronics Engineers (IEEE) also play a signiﬁcant role in AI regulation [148, 25]. In addition, ethical guides
and codes serve as important tools for cross-border AI governance, providing guidance for companies and other
stakeholders [84, 151].
Some important contributions to the ﬁeld have dealt with ﬁnding consensus on principles and developing
global AI governance proposals. Some scholars have suggested the creation of centralized intergovernmental
agencies [25] to coordinate global policy responses, while others have proposed the establishment of an Interna-
tional Artiﬁcial Intelligence Organization [42] or an international coordinating mechanism under the G20 [80,
26].
A.9
Additional Citations: HP#10
An autonomous driving championship, Roborace, closed after six seasons owing to lack of interest and funding [8].
Perhaps most people lack the technical or legal knowledge to understand their data, data protection law, and
how (or even the fact that) a system is making automated decisions [145].
Landmore provides an example of speculative technologies which could instead enhance democratic participa-
tion in [96].
ELECTRONIC SUPPLEMENT


--- Page 83 ---

8
•
Leech et al.
Fig. 15. The topics of presentations at conference workshops between 2017 and 2023, modelled using BERTopic [62]. The
conferences covered are AAAI, ICLR, NeurIPS, IJCAI, and ICML. Each topic is named afer its three most common words
(‘Topic’), and was also given a name for readability (‘Human label’).
ELECTRONIC SUPPLEMENT


--- Page 84 ---

Ten Hard Problems in AI
•
9
B
Topic modelling of top ML conferences
Investigating our Hard Problems further, we tested a more quantitative approach to surveying AI research as a
whole. Figure 15 shows how research areas cluster together based on word co-occurrences in conference workshop
text. (Clustering is not a well-deﬁned problem, however, and so each dataset aﬀords many solutions [62].) Our
code is available on GitHub here: https://github.com/cufbas/topicModeling; the links used to scrape the text data
can be found here: https://zenodo.org/record/7565722. No hyperparameters were altered—Figure 15 represents
the ﬁrst and only clustering run. The only post-processing was to delete spurious topics (those which were overﬁt
or lacked a real common theme).
What could we learn from this? Two possible aims are 1) validating our list of hard problems as a relatively
natural categorization of AI research; 2) attempting to discover cross-cutting intellectual movements and schools
within AI, which might reveal themselves in the process of naming and organizing workshops (and ultimately
new conferences).
The method oﬀers only weak evidence on (1) as the workshops included largely concern AI in a purely technical
sense, mostly with regard to relatively abstract capabilities. Figure 15 is thus more of an elaboration of HP#1 and
4.
Regarding (2): movements within AI research are often hard to demarcate, as demonstrated by the overlapping
research areas within ‘Trustworthiness’, ‘Interpretability’, ‘Explainability’, ‘AI Safety’, and ‘Algorithmic fairness’.
Nevertheless, we think this clustering exercise oﬀers some insight.
References
[1]
A European approach to artiﬁcial intelligence. en. url: https://digital-strategy.ec.europa.eu/en/policies/
european-approach-artiﬁcial-intelligence (visited on 11/27/2022).
[2]
Daron Acemoglu and Pascual Restrepo. “Automation and New Tasks: How Technology Displaces and
Reinstates Labor”. en. In: Journal of Economic Perspectives 33.2 (May 2019), pp. 3–30. issn: 0895-3309. doi:
10.1257/jep.33.2.3. url: https://www.aeaweb.org/articles?id=10.1257/jep.33.2.3 (visited on 10/20/2022).
[3]
Daron Acemoglu and Pascual Restrepo. “The Race between Man and Machine: Implications of Technology
for Growth, Factor Shares, and Employment”. en. In: American Economic Review 108.6 (June 2018), pp. 1488–
1542. issn: 0002-8282. doi: 10.1257/aer.20160696. url: https://www.aeaweb.org/articles?id=10.1257/aer.
20160696 (visited on 09/15/2022).
[4]
Philippe Aghion, Benjamin F. Jones, and Charles I. Jones. Artiﬁcial Intelligence and Economic Growth.
Working Paper. Oct. 2017. doi: 10.3386/w23928. url: https://www.nber.org/papers/w23928 (visited on
09/15/2022).
[5]
Meta AI. Meta | Building AI That Works Better for Everyone. en-US. Mar. 2021. url: https://about.fb.com/
news/2021/03/building-ai-that-works-better-for-everyone/ (visited on 11/27/2022).
[6]
AI Existential Safety Community. en-US. url: https://futureoﬂife.org/about-us/our-people/ai-existential-
safety-community/ (visited on 11/28/2022).
[7]
AI4People’s Ethical Framework for a Good AI Society | Atomium-EISMD. en-US. url: https://www.eismd.
eu/featured/ai4peoples-ethical-framework-for-a-good-ai-society/ (visited on 11/27/2022).
[8]
aiforgoodstg2. How Roborace could shape the future of driving – and save lives. en-US. Nov. 2019. url:
https://aiforgood.itu.int/how-roborace-could-shape-the-future-of-driving-and-save-lives/ (visited on
12/05/2022).
[9]
Aws Albarghouthi et al. “Introduction to neural network veriﬁcation”. In: Foundations and Trends® in
Programming Languages 7.1–2 (2021). Publisher: Now Publishers, Inc., pp. 1–157.
[10]
Dario Amodei et al. Concrete Problems in AI Safety. arXiv:1606.06565 [cs]. July 2016. doi: 10.48550/arXiv.
1606.06565. url: http://arxiv.org/abs/1606.06565 (visited on 09/29/2022).
ELECTRONIC SUPPLEMENT


--- Page 85 ---

10
•
Leech et al.
[11]
Rauno Arike. Clarifying the Confusion Around Inner Alignment. en-US. June 2022. url: https://rauno.io/
clarifying-the-confusion-around-inner-alignment/ (visited on 11/28/2022).
[12]
Melanie Arntz, Terry Gregory, and Ulrich Zierahn. “Revisiting the risk of automation”. In: Economics
Letters 159 (2017), pp. 157–160. issn: 0165-1765. doi: https://doi.org/10.1016/j.econlet.2017.07.001. url:
https://www.sciencedirect.com/science/article/pii/S0165176517302811.
[13]
Stanley Bak, Changliu Liu, and Taylor Johnson. The Second International Veriﬁcation of Neural Networks
Competition (VNN-COMP 2021): Summary and Results. arXiv:2109.00498 [cs]. Aug. 2021. doi: 10.48550/
arXiv.2109.00498. url: http://arxiv.org/abs/2109.00498 (visited on 11/27/2022).
[14]
Peter L. Bartlett et al. “Benign Overﬁtting in Linear Regression”. In: Proceedings of the National Academy of
Sciences 117.48 (Dec. 2020). arXiv:1906.11300 [cs, math, stat], pp. 30063–30070. issn: 0027-8424, 1091-6490.
doi: 10.1073/pnas.1907378117. url: http://arxiv.org/abs/1906.11300 (visited on 11/27/2022).
[15]
Benjamin Beyret et al. The Animal-AI Environment: Training and Testing Animal-Like Artiﬁcial Cognition.
tex.copyright: arXiv.org perpetual, non-exclusive license. 2019. doi: 10.48550/ARXIV.1909.07483. url:
https://arxiv.org/abs/1909.07483.
[16]
Blueprint for an AI Bill of Rights | OSTP. en-US. url: https://www.whitehouse.gov/ostp/ai-bill-of-rights/
(visited on 11/27/2022).
[17]
Rishi Bommasani et al. On the Opportunities and Risks of Foundation Models. arXiv:2108.07258 [cs]. July
2022. doi: 10.48550/arXiv.2108.07258. url: http://arxiv.org/abs/2108.07258 (visited on 09/22/2022).
[18]
Samuel R. Bowman et al. Measuring Progress on Scalable Oversight for Large Language Models. arXiv:2211.03540
[cs]. Nov. 2022. doi: 10.48550/arXiv.2211.03540. url: http://arxiv.org/abs/2211.03540 (visited on
11/30/2022).
[19]
Anu Bradford. The Brussels eﬀect: How the European Union rules the world. Oxford University Press, USA,
2020.
[20]
Miles Brundage et al. The Malicious Use of Artiﬁcial Intelligence: Forecasting, Prevention, and Mitigation.
arXiv:1802.07228 [cs]. Feb. 2018. doi: 10.48550/arXiv.1802.07228. url: http://arxiv.org/abs/1802.07228
(visited on 09/23/2022).
[21]
Steve Byrnes. Intro to Brain-Like-AGI Safety. en. 2021. url: https : / / www. alignmentforum . org / s /
HzcM2dkCq7fwXBej8 (visited on 11/28/2022).
[22]
Steven Byrnes. Can you get AGI from a Transformer? en. 2020. url: https://www.alignmentforum.org/
posts/SkcM4hwgH3AP6iqjs/can-you-get-agi-from-a-transformer (visited on 12/01/2022).
[23]
Comms Chairs. NeurIPS 2021 Ethics Guidelines – NeurIPS Blog. en-US. url: https://blog.neurips.cc/2021/
08/23/neurips-2021-ethics-guidelines/ (visited on 11/27/2022).
[24]
Paul Christiano. Eliciting latent knowledge. en. Feb. 2022. url: https://ai-alignment.com/eliciting-latent-
knowledge-f977478608fc (visited on 11/28/2022).
[25]
Peter Cihon, Matthijs M. Maas, and Luke Kemp. “Fragmentation and the Future: Investigating Architectures
for International AI Governance”. en. In: Global Policy 11.5 (Nov. 2020), pp. 545–556. issn: 1758-5880, 1758-
5899. doi: 10.1111/1758-5899.12890. url: https://onlinelibrary.wiley.com/doi/10.1111/1758-5899.12890
(visited on 11/28/2022).
[26]
Peter Cihon, Matthijs M. Maas, and Luke Kemp. Should Artiﬁcial Intelligence Governance be Centralised?
Design Lessons from History. arXiv:2001.03573 [cs]. Jan. 2020. doi: 10.48550/arXiv.2001.03573. url:
http://arxiv.org/abs/2001.03573 (visited on 11/28/2022).
[27]
Ben Cottier and Rohin Shah. “Clarifying some key hypotheses in AI alignment”. en. In: Ajeya Cotra (2019).
url: https://www.alignmentforum.org/posts/mJ5oNYnkYrd4sD5uE/clarifying-some-key-hypotheses-
in-ai-alignment (visited on 11/28/2022).
[28]
Kate Crawford et al. “AI now 2019 report”. In: New York, NY: AI Now Institute (2019).
ELECTRONIC SUPPLEMENT


--- Page 86 ---

Ten Hard Problems in AI
•
11
[29]
Dafoe. “AI Governance: Overview and Theoretical Lenses”. In: Oxford Handbook on AI Governance. Ed. by
YC Chen et al. Oxford University Press, 2023.
[30]
Richard Danzig. Technology Roulette: Managing Loss of Control as Many Militaries Pursue Technological
Superiority. en. Tech. rep. Center for a New American Security, June 2018, p. 40. url: https://www.cnas.
org/publications/reports/technology-roulette.
[31]
Stephan De Spiegeleire, Matthijs M. Maas, and Tim Sweijs. Artiﬁcial Intelligence and the Future of Defense:
Strategic Implications for Small- and Medium-Sized Force Providers. The Hague, The Netherlands: The Hague
Centre for Strategic Studies, May 2017. url: http://hcss.nl/report/artiﬁcial-intelligence-and-future-defense
(visited on 05/19/2017).
[32]
Declaration of Montréal for a responsible development of AI. en. url: https://www.montrealdeclaration-
responsibleai.com (visited on 11/26/2022).
[33]
DeepMind | Operating Principles. en. url: https://www.deepmind.com/about/operating-principles (visited
on 11/27/2022).
[34]
DeepMind Safety Research – Medium. url: https://deepmindsafetyresearch.medium.com/ (visited on
11/27/2022).
[35]
Mostafa Dehghani et al. The Benchmark Lottery. tex.copyright: arXiv.org perpetual, non-exclusive license.
2021. doi: 10.48550/ARXIV.2107.07002. url: https://arxiv.org/abs/2107.07002.
[36]
Abram Demski and Scott Garrabrant. “Embedded Agency”. en. In: arXiv (Feb. 2019). doi: 10.48550/arXiv.
1902.09469. url: https://arxiv.org/abs/1902.09469v3 (visited on 11/28/2022).
[37]
Jeﬀrey Ding and Allan Dafoe. “The Logic of Strategic Assets: From Oil to AI”. In: Security Studies 30.2
(Mar. 2021). Publisher: Routledge _eprint: https://doi.org/10.1080/09636412.2021.1915583, pp. 182–212.
issn: 0963-6412. doi: 10.1080/09636412.2021.1915583. url: https://doi.org/10.1080/09636412.2021.1915583
(visited on 12/12/2022).
[38]
Roel I. J. Dobbe. System Safety and Artiﬁcial Intelligence. arXiv:2202.09292 [cs, eess]. Feb. 2022. doi:
10.48550/arXiv.2202.09292. url: http://arxiv.org/abs/2202.09292 (visited on 12/03/2022).
[39]
Finale Doshi-Velez and Been Kim. Towards A Rigorous Science of Interpretable Machine Learning. arXiv:1702.08608
[cs, stat]. Mar. 2017. doi: 10.48550/arXiv.1702.08608. url: http://arxiv.org/abs/1702.08608 (visited on
09/29/2022).
[40]
William Drummond. Economic growth under transformative AI - Philip Trammell (Global Priorities In-
stitute, Oxford University) and Anton Korinek (University of Virginia). en-GB. Sept. 2020. url: https:
/ / globalprioritiesinstitute . org / philip - trammell - and - anton - korinek - economic - growth - under -
transformative-ai/ (visited on 10/21/2022).
[41]
EC. EU opens new oﬃce in San Francisco to reinforce its digital diplomacy | Shaping Europe’s digital future.
en. 2022. url: https://digital-strategy.ec.europa.eu/en/news/eu-opens-new-oﬃce-san-francisco-reinforce-
its-digital-diplomacy (visited on 01/11/2023).
[42]
Olivia J. Erdélyi and Judy Goldsmith. “Regulating artiﬁcial intelligence: Proposal for a global solution”.
en. In: Government Information Quarterly 39.4 (Oct. 2022), p. 101748. issn: 0740-624X. doi: 10.1016/j.giq.
2022.101748. url: https://www.sciencedirect.com/science/article/pii/S0740624X22000843 (visited on
12/11/2022).
[43]
Ethical Norms for New Generation Artiﬁcial Intelligence Released. en-US. url: https://cset.georgetown.edu/
publication/ethical-norms-for-new-generation-artiﬁcial-intelligence-released/ (visited on 11/27/2022).
[44]
European Commission | Ethics guidelines for trustworthy AI | Shaping Europe’s digital future. en. url:
https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai (visited on 11/27/2022).
[45]
Facebook’s ﬁve pillars of Responsible AI. en. url: https://ai.facebook.com/blog/facebooks-ﬁve-pillars-of-
responsible-ai/ (visited on 11/27/2022).
ELECTRONIC SUPPLEMENT


--- Page 87 ---

12
•
Leech et al.
[46]
FAT ML :: Principles for Accountable Algorithms and a Social Impact Statement for Algorithms. url: https:
//www.fatml.org/resources/principles-for-accountable-algorithms (visited on 11/27/2022).
[47]
Raymond Fok et al. “Towards More Robust Speech Interactions for Deaf and Hard of Hearing Users”. In:
Proceedings of the 20th International ACM SIGACCESS Conference on Computers and Accessibility. ASSETS
’18. New York, NY, USA: ACM, Oct. 2018, pp. 57–67. isbn: 978-1-4503-5650-3. doi: 10.1145/3234695.3236343.
url: https://doi.org/10.1145/3234695.3236343 (visited on 12/08/2022).
[48]
Ulrike Esther Franke. Flash Wars: Where could an autonomous weapons revolution lead us? en. Nov. 2018. url:
https://www.ecfr.eu/article/Flash_Wars_Where_could_an_autonomous_weapons_revolution_lead_us
(visited on 06/25/2020).
[49]
FTC. Aiming for truth, fairness, and equity in your company’s use of AI. en. Apr. 2021. url: https://www.
ftc.gov/business-guidance/blog/2021/04/aiming-truth-fairness-equity-your-companys-use-ai (visited on
11/28/2022).
[50]
Iason Gabriel and Vafa Ghazavi. The Challenge of Value Alignment: from Fairer Algorithms to AI Safety.
arXiv:2101.06060 [cs]. Jan. 2021. doi: 10.48550/arXiv.2101.06060. url: http://arxiv.org/abs/2101.06060
(visited on 11/22/2022).
[51]
Jonas Geiping et al. “Witches’ brew: Industrial scale data poisoning via gradient matching”. In: arXiv
(2020).
[52]
Rayid Ghani. You Say You Want Transparency and Interpretability? 2016. url: http://www.rayidghani.
com/2016/04/29/you-say-you-want-transparency-and-interpretability/.
[53]
Amandeep Singh Gill. “Artiﬁcial Intelligence and International Security: The Long View”. en. In: Ethics &
International Aﬀairs 33.2 (2019), pp. 169–179. issn: 0892-6794, 1747-7093. doi: 10.1017/S0892679419000145.
url: https://www.cambridge.org/core/journals/ethics-and-international-aﬀairs/article/artiﬁcial-
intelligence-and-international-security-the-long-view/4AB181EAF648501422257934982A4DD5 (visited
on 06/13/2019).
[54]
Amelia Glaese. “Improving alignment of dialogue agents via targeted human judgements”. In: Google AI
(2022). url: https://storage.googleapis.com/deepmind-media/DeepMind.com/Authors-Notes/sparrow/
sparrow-ﬁnal.pdf.
[55]
Gerard Goggin and Christopher Newell. “The Business of Digital Disability”. en. In: The Information
Society 23.3 (Apr. 2007), pp. 159–168. issn: 0197-2243, 1087-6537. doi: 10.1080/01972240701323572. url:
http://www.tandfonline.com/doi/abs/10.1080/01972240701323572 (visited on 12/08/2022).
[56]
ShaﬁGoldwasser et al. Planting Undetectable Backdoors in Machine Learning Models. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2022. doi: 10.48550/ARXIV.2204.06974. url: https://arxiv.org/
abs/2204.06974.
[57]
Ian J. Goodfellow, Jonathon Shlens, and Christian Szegedy. Explaining and Harnessing Adversarial Examples.
arXiv:1412.6572 [cs, stat]. Mar. 2015. doi: 10.48550/arXiv.1412.6572. url: http://arxiv.org/abs/1412.6572
(visited on 09/29/2022).
[58]
Google AI | Our Principles. en. url: https://ai.google/principles/ (visited on 11/27/2022).
[59]
Google AI | Responsible AI practices. en. url: https://ai.google/responsibilities/responsible-ai-practices/
(visited on 11/27/2022).
[60]
Georg Graetz, Guy Michaels, et al. Robots at work: the impact on productivity and jobs. Tech. rep. Centre
for Economic Performance, LSE, 2015.
[61]
Greg Allen and Taniel Chan. Artiﬁcial Intelligence and National Security. en. 2017. url: https://www.
belfercenter.org/publication/artiﬁcial-intelligence-and-national-security (visited on 01/11/2023).
[62]
Maarten Grootendorst. BERTopic: Neural topic modeling with a class-based TF-IDF procedure. arXiv:2203.05794
[cs]. Mar. 2022. doi: 10.48550/arXiv.2203.05794. url: http://arxiv.org/abs/2203.05794 (visited on 01/11/2023).
ELECTRONIC SUPPLEMENT


--- Page 88 ---

Ten Hard Problems in AI
•
13
[63]
Shangding Gu et al. A Review of Safe Reinforcement Learning: Methods, Theory and Applications. arXiv:2205.10330
[cs]. June 2022. doi: 10.48550/arXiv.2205.10330. url: http://arxiv.org/abs/2205.10330 (visited on 11/28/2022).
[64]
Bob Hancké and Angela Garcia Calvo. “Mister Chips goes to Brussels: On the Pros and Cons of a Semicon-
ductor Policy in the EU”. en. In: Global Policy 13.4 (2022). _eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/1758-
5899.13096, pp. 585–593. issn: 1758-5899. doi: 10.1111/1758-5899.13096. url: https://onlinelibrary.wiley.
com/doi/abs/10.1111/1758-5899.13096 (visited on 10/17/2022).
[65]
David Hémous and Morten Olsen. “The Rise of the Machines: Automation, Horizontal Innovation, and
Income Inequality”. en. In: American Economic Journal: Macroeconomics 14.1 (Jan. 2022), pp. 179–223. issn:
1945-7707. doi: 10.1257/mac.20160164. url: https://www.aeaweb.org/articles?id=10.1257/mac.20160164&
&from=f (visited on 09/15/2022).
[66]
Dan Hendrycks, Mantas Mazeika, and Thomas Dietterich. “Deep anomaly detection with outlier exposure”.
In: arXiv (2018).
[67]
Dan Hendrycks et al. Aligning AI With Shared Human Values. arXiv:2008.02275 [cs]. July 2021. doi:
10.48550/arXiv.2008.02275. url: http://arxiv.org/abs/2008.02275 (visited on 09/30/2022).
[68]
Dan Hendrycks et al. Unsolved Problems in ML Safety. arXiv:2109.13916 [cs]. June 2022. doi: 10.48550/
arXiv.2109.13916. url: http://arxiv.org/abs/2109.13916 (visited on 09/29/2022).
[69]
José Hernández-Orallo. The measure of all minds: evaluating natural and artiﬁcial intelligence. Cambridge
University Press, 2017.
[70]
José Hernández-Orallo et al. “General intelligence disentangled via a generality metric for natural and
artiﬁcial intelligence”. In: Scientiﬁc reports 11.1 (2021). Publisher: Nature Publishing Group, pp. 1–16.
[71]
Michael C. Horowitz and Lauren Kahn. “How Joe Biden can use conﬁdence-building measures for
military uses of AI”. In: Bulletin of the Atomic Scientists 77.1 (Jan. 2021). Publisher: Routledge _eprint:
https://doi.org/10.1080/00963402.2020.1860331, pp. 33–35. issn: 0096-3402. doi: 10.1080/00963402.2020.
1860331. url: https://doi.org/10.1080/00963402.2020.1860331 (visited on 02/01/2021).
[72]
Michael C. Horowitz, Lauren Kahn, and Christian Ruhl, eds. Policy Roundtable: Artiﬁcial Intelligence and
International Security. en-US. June 2020. url: http://tnsr.org/roundtable/policy-roundtable-artiﬁcial-
intelligence-and-international-security/ (visited on 06/03/2020).
[73]
Evan Hubinger. An overview of 11 proposals for building safe advanced AI. arXiv:2012.07532 [cs]. Dec. 2020.
doi: 10.48550/arXiv.2012.07532. url: http://arxiv.org/abs/2012.07532 (visited on 11/30/2022).
[74]
Evan Hubinger. Relaxed adversarial training for inner alignment. 2019. url: https://www.alignmentforum.
org/posts/9Dy5YRaoCxH9zuJqa/relaxed-adversarial-training-for-inner-alignment.
[75]
IEEE Ethics In Action in Autonomous and Intelligent Systems | IEEE SA. en-US. url: https://ethicsinaction.
ieee.org/ (visited on 11/27/2022).
[76]
Inioluwa Deborah Raji and Roel Dobbe. “Concrete Problems in AI Safety, Revisited”. In: Workshop on Ma-
chine Learning In. Real Life (2020). url: https://drive.google.com/ﬁle/d/1Re_yQDNFuejoqjZloTgQpILosDGtt5ei/
view.
[77]
Future of Life Institute. Asilomar Open Letter on AI Principles. 2017. url: https://futureoﬂife.org/open-
letter/ai-principles/.
[78]
Geoﬀrey Irving and Amanda Askell. “AI Safety Needs Social Scientists”. en. In: Distill 4.2 (Feb. 2019), e14.
issn: 2476-0757. doi: 10.23915/distill.00014. url: https://distill.pub/2019/safety-needs-social-scientists
(visited on 11/28/2022).
[79]
Geoﬀrey Irving, Paul Christiano, and Dario Amodei. AI safety via debate. arXiv:1805.00899 [cs, stat]. Oct.
2018. doi: 10.48550/arXiv.1805.00899. url: http://arxiv.org/abs/1805.00899 (visited on 11/30/2022).
[80]
Thorsten Jelinek, Wendell Wallach, and Danil Kerimi. “Policy brief: the creation of a G20 coordinating
committee for the governance of artiﬁcial intelligence”. en. In: AI and Ethics 1.2 (May 2021), pp. 141–150.
ELECTRONIC SUPPLEMENT


--- Page 89 ---

14
•
Leech et al.
issn: 2730-5961. doi: 10.1007/s43681-020-00019-y. url: https://doi.org/10.1007/s43681-020-00019-y
(visited on 11/28/2022).
[81]
Hong Jun Jeon, Smitha Milli, and Anca D. Dragan. “Reward-rational (implicit) choice: A unifying formalism
for reward learning”. en. In: arXiv (Feb. 2020). doi: 10.48550/arXiv.2002.04833. url: https://arxiv.org/abs/
2002.04833v4 (visited on 11/28/2022).
[82]
Yunfan Jiang et al. VIMA: General Robot Manipulation with Multimodal Prompts. tex.copyright: Creative
Commons Attribution 4.0 International. 2022. doi: 10.48550/ARXIV.2210.03094. url: https://arxiv.org/abs/
2210.03094.
[83]
Chi Jin, Qinghua Liu, and Sobhan Miryooseﬁ. “Bellman Eluder Dimension: New Rich Classes of RL
Problems, and Sample-Eﬃcient Algorithms”. In: Advances in Neural Information Processing Systems. Ed. by
M. Ranzato et al. Vol. 34. Curran Associates, Inc., 2021, pp. 13406–13418. url: https://proceedings.neurips.
cc/paper/2021/ﬁle/6f5e4e86a87220e5d361ad82f1ebc335-Paper.pdf.
[84]
Anna Jobin, Marcello Ienca, and Eﬀy Vayena. “The global landscape of AI ethics guidelines”. en. In:
Nature 1.9 (Sept. 2019), pp. 389–399. issn: 2522-5839. doi: 10.1038/s42256- 019- 0088- 2. url: https:
//www.nature.com/articles/s42256-019-0088-2 (visited on 12/09/2022).
[85]
jsteinhardt. Future ML Systems Will Be Qualitatively Diﬀerent. en. 2022. url: https://www.alignmentforum.
org/posts/pZaPhGg2hmmPwByHc/future- ml- systems- will- be- qualitatively- diﬀerent (visited on
11/30/2022).
[86]
Saurav Kadavath et al. “Language Models (Mostly) Know What They Know”. en. In: arXiv (July 2022).
doi: 10.48550/arXiv.2207.05221. url: https://arxiv.org/abs/2207.05221v4 (visited on 11/28/2022).
[87]
Atoosa Kasirzadeh and Iason Gabriel. In conversation with Artiﬁcial Intelligence: aligning language models
with human values. arXiv:2209.00731 [cs]. Sept. 2022. doi: 10.48550/arXiv.2209.00731. url: http://arxiv.
org/abs/2209.00731 (visited on 11/22/2022).
[88]
Zachary Kenton et al. Discovering Agents. arXiv:2208.08345 [cs]. Aug. 2022. doi: 10.48550/arXiv.2208.08345.
url: http://arxiv.org/abs/2208.08345 (visited on 11/28/2022).
[89]
Jan H. Kirchner et al. Researching Alignment Research: Unsupervised Analysis. tex.copyright: Creative
Commons Attribution Non Commercial No Derivatives 4.0 International. 2022. doi: 10.48550/ARXIV.
2206.02841. url: https://arxiv.org/abs/2206.02841.
[90]
Henry A. Kissinger et al. The Age of AI: And Our Human Future. en. Google-Books-ID: PrEhzgEACAAJ.
Little Brown, 2021. isbn: 978-0-316-27380-0.
[91]
W. Bradley Knox et al. Reward (Mis)design for Autonomous Driving. arXiv:2104.13906 [cs]. Mar. 2022. doi:
10.48550/arXiv.2104.13906. url: http://arxiv.org/abs/2104.13906 (visited on 09/30/2022).
[92]
Anton Korinek and Megan Juelfs. Preparing for the (non-existent?) future of work. Tech. rep. National
Bureau of Economic Research, 2022.
[93]
Alexei Koulakov et al. “Encoding innate ability through a genomic bottleneck”. In: bioRxiv (2022). Publisher:
Cold Spring Harbor Laboratory tex.elocation-id: 2021.03.16.435261 tex.eprint: https://www.biorxiv.org/content/early/2022/05/26
doi: 10.1101/2021.03.16.435261. url: https://www.biorxiv.org/content/early/2022/05/26/2021.03.16.435261.
[94]
Victoria Krakovna et al. Speciﬁcation gaming: the ﬂip side of AI ingenuity. en. 2020. url: https://www.
deepmind.com/blog/speciﬁcation-gaming-the-ﬂip-side-of-ai-ingenuity (visited on 11/28/2022).
[95]
Brenden M. Lake et al. Building Machines That Learn and Think Like People. arXiv:1604.00289 [cs, stat].
Nov. 2016. doi: 10.48550/arXiv.1604.00289. url: http://arxiv.org/abs/1604.00289 (visited on 09/29/2022).
[96]
Hélène Landemore. “2. Open Democracy and Digital Technologies”. en. In: 2. Open Democracy and
Digital Technologies. University of Chicago Press, Feb. 2021, pp. 62–89. isbn: 9780226748603. url: https:
//www.degruyter.com/document/doi/10.7208/9780226748603-003/html?lang=en (visited on 12/06/2022).
[97]
Eric D. Langlois and Tom Everitt. “How RL Agents Behave When Their Actions Are Modiﬁed”. en. In:
Proceedings of the AAAI Conference on Artiﬁcial Intelligence 35.13 (May 2021), pp. 11586–11594. issn:
ELECTRONIC SUPPLEMENT


--- Page 90 ---

Ten Hard Problems in AI
•
15
2374-3468. doi: 10.1609/aaai.v35i13.17378. url: https://ojs.aaai.org/index.php/AAAI/article/view/17378
(visited on 12/10/2022).
[98]
Lauro Langosco Di Langosco et al. “Goal Misgeneralization in Deep Reinforcement Learning”. en. In:
Proceedings of the 39th International Conference on Machine Learning. PMLR, June 2022, pp. 12004–12019.
url: https://proceedings.mlr.press/v162/langosco22a.html (visited on 09/30/2022).
[99]
Michael Laskin et al. “In-context Reinforcement Learning with Algorithm Distillation”. In: arXiv (2022).
[100]
Alexander Lavin et al. “Technology readiness levels for machine learning systems”. en. In: Nature 13.1
(Oct. 2022), p. 6039. issn: 2041-1723. doi: 10.1038/s41467-022-33128-9. url: https://www.nature.com/
articles/s41467-022-33128-9 (visited on 12/05/2022).
[101]
Jan Leike et al. “Scalable agent alignment via reward modeling: a research direction”. en. In: arXiv (Nov.
2018). doi: 10.48550/arXiv.1811.07871. url: https://arxiv.org/abs/1811.07871v1 (visited on 11/28/2022).
[102]
Percy Liang et al. Holistic Evaluation of Language Models. arXiv:2211.09110 [cs]. Nov. 2022. doi: 10.48550/
arXiv.2211.09110. url: http://arxiv.org/abs/2211.09110 (visited on 11/30/2022).
[103]
Richard G Lipsey, Kenneth I Carlaw, and Cliﬀord T Bekar. Economic transformations: general purpose
technologies and long-term economic growth. OUP Oxford, 2005.
[104]
Zachary C. Lipton. The Mythos of Model Interpretability. arXiv:1606.03490 [cs, stat]. Mar. 2017. doi:
10.48550/arXiv.1606.03490. url: http://arxiv.org/abs/1606.03490 (visited on 09/29/2022).
[105]
Andrew Lohn. Poison in the Well. en-US. 2021. url: https://cset.georgetown.edu/publication/poison-in-
the-well/ (visited on 01/11/2023).
[106]
Andrew J. Lohn. Estimating the Brittleness of AI: Safety Integrity Levels and the Need for Testing Out-Of-
Distribution Performance. arXiv:2009.00802 [cs, stat]. Sept. 2020. doi: 10.48550/arXiv.2009.00802. url:
http://arxiv.org/abs/2009.00802 (visited on 09/29/2022).
[107]
Yingying Lu and Yixiao Zhou. “A review on the economics of artiﬁcial intelligence”. en. In: Journal of
Economic Surveys 35.4 (Sept. 2021), pp. 1045–1072. issn: 0950-0804, 1467-6419. doi: 10.1111/joes.12422.
url: https://onlinelibrary.wiley.com/doi/10.1111/joes.12422 (visited on 09/14/2022).
[108]
Matthijs M. Maas. “How viable is international arms control for military artiﬁcial intelligence? Three
lessons from nuclear weapons”. In: Contemporary Security Policy 40.3 (Feb. 2019), pp. 285–311. issn:
1352-3260. doi: 10.1080/13523260.2019.1576464. url: https://doi.org/10.1080/13523260.2019.1576464
(visited on 02/07/2019).
[109]
Matthijs M. Maas. “Regulating for ’Normal AI Accidents’: Operational Lessons for the Responsible
Governance of Artiﬁcial Intelligence Deployment”. In: Proceedings of the 2018 AAAI/ACM Conference on AI,
Ethics, and Society. AIES ’18. New York, NY, USA: ACM, Dec. 2018, pp. 223–228. isbn: 978-1-4503-6012-8.
doi: 10.1145/3278721.3278766. url: https://doi.org/10.1145/3278721.3278766 (visited on 09/08/2020).
[110]
Tegan Maharaj. Generalizing in the Real World with Representation Learning. tex.copyright: Creative
Commons Attribution Non Commercial Share Alike 4.0 International. 2022. doi: 10.48550/ARXIV.2210.
09925. url: https://arxiv.org/abs/2210.09925.
[111]
Gary Marcus. Deep Learning: A Critical Appraisal. arXiv:1801.00631 [cs, stat]. Jan. 2018. doi: 10.48550/
arXiv.1801.00631. url: http://arxiv.org/abs/1801.00631 (visited on 10/26/2022).
[112]
Roxana Mihet and Thomas Philippon. “The economics of Big Data and artiﬁcial intelligence”. In: Disruptive
Innovation in Business and Finance in the Digital World. Emerald Publishing Limited, 2019.
[113]
Mila | Biasly. en-US. url: https://mila.quebec/en/project/biasly/ (visited on 11/28/2022).
[114]
Sina Mohseni et al. Taxonomy of Machine Learning Safety: A Survey and Primer. arXiv:2106.04823 [cs].
Mar. 2022. doi: 10.48550/arXiv.2106.04823. url: http://arxiv.org/abs/2106.04823 (visited on 09/29/2022).
[115]
Preetum Nakkiran et al. Deep Double Descent: Where Bigger Models and More Data Hurt. arXiv:1912.02292
[cs, stat]. Dec. 2019. doi: 10.48550/arXiv.1912.02292. url: http://arxiv.org/abs/1912.02292 (visited on
09/27/2022).
ELECTRONIC SUPPLEMENT


--- Page 91 ---

16
•
Leech et al.
[116]
Neel Nanda. A Mechanistic Interpretability Analysis of Grokking. en. 2022. url: https://www.alignmentforum.
org/posts/N6WM6hs7RQMKDhYjB/a-mechanistic-interpretability-analysis-of-grokking (visited on
09/29/2022).
[117]
Neel Nanda. TransformerLens: An implementation of transformers tailored for mechanistic interpretability.
2022. url: https://github.com/neelnanda-io/TransformerLens.
[118]
National AI Strategy - GOV.UK. url: https://www.gov.uk/government/publications/national- ai-
strategy/national-ai-strategy-html-version (visited on 11/27/2022).
[119]
Ljubica Nedelkoska and Glenda Quintini. Automation, skills use and training. Tech. rep. Paris: OCDE, Mar.
2018. doi: 10.1787/2e2f4eea-en. url: https://www.oecd-ilibrary.org/fr/employment/automation-skills-
use-and-training_2e2f4eea-en (visited on 11/25/2022).
[120]
Harsha Nori et al. “InterpretML: A Uniﬁed Framework for Machine Learning Interpretability”. In: arXiv
(2019). url: https://arxiv.org/pdf/1909.09223.pdf.
[121]
Paul Nuyujukian et al. “Cortical control of a tablet computer by people with paralysis”. en. In: PLOS
ONE 13.11 (Nov. 2018), e0204566. issn: 1932-6203. doi: 10.1371/journal.pone.0204566. url: https:
//journals.plos.org/plosone/article?id=10.1371/journal.pone.0204566 (visited on 12/08/2022).
[122]
Chris Olah. Mechanistic Interpretability, Variables, and the Importance of Interpretable Bases. 2022. url:
https://transformer-circuits.pub/2022/mech-interp-essay/index.html.
[123]
Chris Olah et al. “Zoom In: An Introduction to Circuits”. In: Distill 5.3 (Mar. 2020), 10.23915/distill.00024.001.
issn: 2476-0757. doi: 10.23915/distill.00024.001. url: https://distill.pub/2020/circuits/zoom-in (visited on
09/29/2022).
[124]
Catherine Olsson et al. In-context Learning and Induction Heads. arXiv:2209.11895 [cs]. Sept. 2022. doi:
10.48550/arXiv.2209.11895. url: http://arxiv.org/abs/2209.11895 (visited on 11/30/2022).
[125]
OpenAI | Aligning AI systems with human intent. url: https : / / openai . com / alignment/ (visited on
11/27/2022).
[126]
OpenAI Charter. en. url: https://openai.com/charter/ (visited on 11/27/2022).
[127]
Michael Osborne. Automation and the future of work – understanding the numbers. Oxford Martin School.
2013. url: https://www.oxfordmartin.ox.ac.uk/blog/automation-and-the-future-of-work-understanding-
the-numbers/ (visited on 11/25/2022).
[128]
Long Ouyang et al. Training language models to follow instructions with human feedback. arXiv:2203.02155
[cs]. Mar. 2022. doi: 10.48550/arXiv.2203.02155. url: http://arxiv.org/abs/2203.02155 (visited on
09/30/2022).
[129]
Partnership on AI | About Us | Advancing positive outcomes for people and society | Values, Pillars, Tenets.
en-US. url: https://partnershiponai.org/about/ (visited on 11/27/2022).
[130]
Partnership on AI | Resource Library. en-US. url: https://partnershiponai.org/resources/ (visited on
11/27/2022).
[131]
Kenneth Payne. I, Warbot: The Dawn of Artiﬁcially Intelligent Conﬂict. English. S.l.: C Hurst & Co Publishers
Ltd, June 2021. isbn: 978-1-78738-462-0.
[132]
Ethan Perez et al. Red Teaming Language Models with Language Models. arXiv:2202.03286 [cs]. Feb. 2022.
doi: 10.48550/arXiv.2202.03286. url: http://arxiv.org/abs/2202.03286 (visited on 09/30/2022).
[133]
Colin B. Picker. A View from 40,000 Feet: International Law and the Invisible Hand of Technology. en. SSRN
Scholarly Paper. Rochester, NY, May 2007. url: https://papers.ssrn.com/abstract=987524 (visited on
11/28/2022).
[134]
Quintin Pope. The Shard Theory of Human Values. en. 2022. url: https://www.alignmentforum.org/s/
nyEFg3AuJpdAozmoX (visited on 11/28/2022).
[135]
Projects :: FAT ML. url: https://www.fatml.org/resources/relevant-projects (visited on 11/28/2022).
ELECTRONIC SUPPLEMENT


--- Page 92 ---

Ten Hard Problems in AI
•
17
[136]
Iyad Rahwan et al. “Machine behaviour”. In: Nature 568.7753 (2019). Publisher: Nature Publishing Group,
pp. 477–486.
[137]
Siddharth Reddy, Sergey Levine, and Anca D. Dragan. First Contact: Unsupervised Human-Machine Co-
Adaptation via Mutual Information Maximization. arXiv:2205.12381 [cs]. Sept. 2022. doi: 10.48550/arXiv.
2205.12381. url: http://arxiv.org/abs/2205.12381 (visited on 12/12/2022).
[138]
Lauren Rockliﬀe. “Including non-English language articles in systematic reviews: A reﬂection on processes
for identifying low-cost sources of translation support”. en. In: Research Synthesis Methods 13.1 (2022).
_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/jrsm.1508, pp. 2–5. issn: 1759-2887. doi: 10.1002/
jrsm.1508. url: https://onlinelibrary.wiley.com/doi/abs/10.1002/jrsm.1508 (visited on 12/09/2022).
[139]
Elle Rothermich. “Mind Games: How Robots Can Help Regulate Brain-Computer Interfaces”. In: University
of Pennsylvania Journal of Law & Public Aﬀairs 7 (2021), p. 391. url: https://heinonline.org/HOL/Page?
handle=hein.journals/penjuaf7&id=397&div=&collection=.
[140]
Stuart Russell. Human Compatible: Artiﬁcial intelligence and the problem of control. Penguin Random
House, 2020. isbn: 9780525558637.
[141]
Jeﬀrey D Sachs and Laurence J Kotlikoﬀ. Smart machines and long-term misery. Tech. rep. National Bureau
of Economic Research, 2012. url: https://www.nber.org/papers/w18629.
[142]
Sam Manning, Pamela Mishkin, and Tyna Eloundou. Economic Impacts Research at OpenAI. en. Mar. 2022.
url: https://openai.com/blog/economic-impacts/ (visited on 12/07/2022).
[143]
Paul Scharre and Megan Lamberth. Artiﬁcial Intelligence and Arms Control. en. Tech. rep. Center for a
New American Security, Oct. 2022. url: https://www.cnas.org/publications/reports/artiﬁcial-intelligence-
and-arms-control (visited on 10/13/2022).
[144]
Robert Seamans and Manav Raj. AI, Labor, Productivity and the Need for Firm-Level Data. Working Paper.
Jan. 2018. doi: 10.3386/w24239. url: https://www.nber.org/papers/w24239 (visited on 10/20/2022).
[145]
Andrew Selbst and Julia Powles. ““Meaningful Information” and the Right to Explanation”. en. In: Pro-
ceedings of the 1st Conference on Fairness, Accountability and Transparency. PMLR, Jan. 2018, pp. 48–48.
url: https://proceedings.mlr.press/v81/selbst18a.html (visited on 11/26/2022).
[146]
Rohin Shah et al. “Beneﬁts of Assistance over Reward Learning”. en. In: ICLR (Mar. 2021). url: https:
//openreview.net/forum?id=DFIoGDZejIB (visited on 11/30/2022).
[147]
Charlotte Siegmann and Markus Anderljung. The Brussels Eﬀect and Artiﬁcial Intelligence: How EU
regulation will impact the global AI market. en. Tech. rep. Centre for the Governance of AI, Aug. 2022,
p. 97. url: https://www.governance.ai/research-paper/brussels-eﬀect-ai.
[148]
Anton Sigfrids et al. “How Should Public Administrations Foster the Ethical Development and Use of
Artiﬁcial Intelligence? A Review of Proposals for Developing Governance of AI”. In: Frontiers in Human
Dynamics 4 (2022). issn: 2673-2726. url: https://www.frontiersin.org/articles/10.3389/fhumd.2022.858108
(visited on 12/06/2022).
[149]
Fabian H. Sinz et al. “Engineering a Less Artiﬁcial Intelligence”. In: Neuron 103.6 (2019), pp. 967–979. issn:
0896-6273. doi: https://doi.org/10.1016/j.neuron.2019.08.034. url: https://www.sciencedirect.com/science/
article/pii/S0896627319307408.
[150]
Nate Soares et al. “Corrigibility”. en. In: AAAI, Mar. 2020. url: https://openreview.net/forum?id=
H1bIT1buWH (visited on 09/29/2022).
[151]
Charlotte Stix. Foundations for the Future: Institution building for the purpose of Artiﬁcial Intelligence
governance. en. SSRN Scholarly Paper. Rochester, NY, Sept. 2021. doi: 10 . 2139 / ssrn . 3934878. url:
https://papers.ssrn.com/abstract=3934878 (visited on 12/09/2022).
[152]
Jonathan Stray. “Aligning AI Optimization to Community Well-Being”. en. In: International Journal of
Community Well-Being 3.4 (Dec. 2020), pp. 443–463. issn: 2524-5309. doi: 10.1007/s42413-020-00086-3.
url: https://doi.org/10.1007/s42413-020-00086-3 (visited on 09/30/2022).
ELECTRONIC SUPPLEMENT


--- Page 93 ---

18
•
Leech et al.
[153]
Christian Szegedy et al. Intriguing properties of neural networks. arXiv:1312.6199 [cs]. Feb. 2014. doi:
10.48550/arXiv.1312.6199. url: http://arxiv.org/abs/1312.6199 (visited on 09/29/2022).
[154]
The OECD Artiﬁcial Intelligence (AI) Principles. en. url: https://oecd.ai/en/ai-principles (visited on
11/27/2022).
[155]
Hugo Touvron et al. Training data-eﬃcient image transformers & distillation through attention. tex.copyright:
arXiv.org perpetual, non-exclusive license. 2020. doi: 10.48550/ARXIV.2012.12877. url: https://arxiv.org/
abs/2012.12877.
[156]
Manuel Trajtenberg. “AI as the next GPT: a Political-Economy Perspective”. en. In: NBER Working Papers
(Jan. 2018). url: https://ideas.repec.org/p/nbr/nberwo/24245.html (visited on 11/28/2022).
[157]
Translation: Internet Information Service Algorithmic Recommendation Management Provisions – Eﬀective
March 1, 2022. en. url: https://digichina.stanford.edu/work/translation-internet-information-service-
algorithmic-recommendation-management-provisions-eﬀective-march-1-2022/ (visited on 11/28/2022).
[158]
Jonathan Uesato et al. “Adversarial Risk and the Dangers of Evaluating Against Weak Attacks”. en. In:
Proceedings of the 35th International Conference on Machine Learning. PMLR, July 2018, pp. 5025–5034.
url: https://proceedings.mlr.press/v80/uesato18a.html (visited on 11/28/2022).
[159]
UK sets out proposals for new AI rulebook to unleash innovation and boost public trust in the technology. en.
url: https://www.gov.uk/government/news/uk-sets-out-proposals-for-new-ai-rulebook-to-unleash-
innovation-and-boost-public-trust-in-the-technology (visited on 11/28/2022).
[160]
UNESCO - Recommendation on the Ethics of Artiﬁcial Intelligence. url: https://unesdoc.unesco.org/ark:
/48223/pf0000381137 (visited on 11/27/2022).
[161]
William Walters. “The Geography of the European Dreadnought Race: 1884-1919”. en. In: The Geographical
Bulletin 34.1 (1992). url: https://www.proquest.com/openview/41ce2d8af6399ba089475b61417a9c65/1?pq-
origsite=gscholar&cbl=1817294 (visited on 01/11/2023).
[162]
Kevin Wang et al. Interpretability in the Wild: a Circuit for Indirect Object Identiﬁcation in GPT-2 small.
arXiv:2211.00593 [cs]. Nov. 2022. doi: 10.48550/arXiv.2211.00593. url: http://arxiv.org/abs/2211.00593
(visited on 11/30/2022).
[163]
Tony Tong Wang et al. Adversarial Policies Beat Professional-Level Go AIs. arXiv:2211.00241 [cs, stat]. Oct.
2022. doi: 10.48550/arXiv.2211.00241. url: http://arxiv.org/abs/2211.00241 (visited on 11/30/2022).
[164]
Andrew Warner. BigScience launches open-source LLM, BLOOM. 2022. url: https://multilingual.com/bloom-
large-language-model/.
[165]
Jason Wei. 137 emergent abilities of large language models. en-US. 2022. url: https://www.jasonwei.net/
blog/emergence (visited on 11/28/2022).
[166]
John Wentworth. Abstraction 2020. en. 2020. url: https://www.alignmentforum.org/s/ehnG4mseKF6xALmQy
(visited on 11/28/2022).
[167]
Robert Williams and Roman Yampolskiy. “Understanding and Avoiding AI Failures: A Practical Guide”. en.
In: Philosophies 6.3 (Sept. 2021). Number: 3 Publisher: Multidisciplinary Digital Publishing Institute, p. 53.
doi: 10.3390/philosophies6030053. url: https://www.mdpi.com/2409-9287/6/3/53 (visited on 07/05/2021).
[168]
Kaidi Xu et al. “Automatic perturbation analysis for scalable certiﬁed robustness and beyond”. In: Advances
in Neural Information Processing Systems 33 (2020), pp. 1129–1141.
[169]
Denis Yarats et al. “Improving Sample Eﬃciency in Model-Free Reinforcement Learning from Images”.
In: Proceedings of the AAAI Conference on Artiﬁcial Intelligence 35.12 (May 2021), pp. 10674–10681. doi:
10.1609/aaai.v35i12.17276. url: https://ojs.aaai.org/index.php/AAAI/article/view/17276.
[170]
Eliezer Yudkowsky. Problem of fully updated deference. en. 2020. url: https://arbital.com/p/updated_
deference/ (visited on 11/30/2022).
[171]
Anthony M Zador. “A critique of pure learning and what artiﬁcial neural networks can learn from animal
brains”. In: Nature 10.1 (2019). Publisher: Nature Publishing Group, pp. 1–7.
ELECTRONIC SUPPLEMENT


--- Page 94 ---

Ten Hard Problems in AI
•
19
[172]
Huan Zhang et al. $\alpha,\beta$-CROWN. 2022. url: https://github.com/Veriﬁed-Intelligence/alpha-beta-
CROWN.
[173]
Huan Zhang et al. “Eﬃcient neural network robustness certiﬁcation with general activation functions”.
In: Advances in neural information processing systems 31 (2018).
[174]
Daniel M. Ziegler et al. Adversarial Training for High-Stakes Reliability. arXiv:2205.01663 [cs]. Nov. 2022.
doi: 10.48550/arXiv.2205.01663. url: http://arxiv.org/abs/2205.01663 (visited on 11/30/2022).
ELECTRONIC SUPPLEMENT

```
