---
title: "A Statistical Case Against Empirical Human-AI - PDF Extract"
source_pdf: "2025-Rodemann-A Statistical Case Against Empirical Human-AI.pdf"
pages: 26
extracted_at: "2026-01-24T16:38:33.504373"
---

# PDF Extract: A Statistical Case Against Empirical Human-AI

**Source PDF:** 2025-Rodemann-A Statistical Case Against Empirical Human-AI.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

A Statistical Case Against Empirical Human–AI Alignment
Julian Rodemann 1 Esteban Garcés Arias 1 2 Christoph Luther 3 4 Christoph Jansen 5 Thomas Augustin 1
Abstract
Empirical human–AI alignment aims to
make AI systems act in line with observed
human behavior. While noble in its goals,
we argue that empirical alignment can in-
advertently introduce statistical biases that
warrant caution. This position paper thus
advocates against naive empirical align-
ment, offering prescriptive alignment and
a posteriori empirical alignment as alterna-
tives. We substantiate our principled ar-
gument by tangible examples like human-
centric decoding of language models.
1. Introduction
"If we use, to achieve our purposes, a mechanical
agency with whose operation we cannot interfere
effectively, [...] we had better be quite sure that
the purpose put into the machine is the purpose
which we really desire and not merely a colorful
imitation of it."
– Wiener (1960), In: Science, 131(3410),
page 1355.
Aligning artificial intelligence (AI) with human goals
has shifted from abstract ethics to urgent policy agen-
das. Regulators see safety and harm prevention as
prerequisites for AI’s widespread deployment, not
optional virtues, see e.g., Chatila & Havens (2019).
Against this background, it comes as no surprise that
1Department of Statistics, LMU Munich, Germany
2Munich Center for Machine Learning (MCML), Germany
3Research Group Neuroinformatics, Faculty of Computer
Science, University of Vienna, Vienna, Austria 4Doctoral
School Computer Science, Faculty of Computer Science,
University of Vienna, Vienna, Austria 5School of Comput-
ing & Communications, Lancaster University Leipzig, Ger-
many. Correspondence to: Julian Rodemann <mail@julian-
rodemann.de>.
Preprint. Copyright by the authors. May 2025.
the challenges of human–AI alignment have sparked
a lot of interest in the machine learning (ML) research
community. In 2024 alone, more than 1500 papers
with alignment-related keywords were uploaded to
arxiv, see Fig. 1. Analyses of github and Hugging
Face uploads show similar trends. An alignment
benchmark study (Kirk et al., 2024) won a best paper
award at the 38th Conference on Neural Information
Processing Systems (NeurIPS).
The position paper track at last year’s 41st Inter-
national Conference on Machine Learning (ICML)
alone saw at least four papers (Sorensen et al., 2024;
Lindauer et al., 2024; Conitzer et al., 2024; Yang et al.,
2024) explicitly calling for more, better, or more nu-
anced human–AI alignment. Lindauer et al. (2024)
advocate for a more human-centered approach to au-
tomating ML pipelines. Both Sorensen et al. (2024);
Conitzer et al. (2024) emphasize the need to align
AI systems with diverse and potentially conflicting
human interests.
Yang et al. (2024) move beyond a mere human-
centered perspective: They recognize the need to
adapt AI to environments and self-constraints in ad-
dition to human intentions. For instance, agents have
to be aligned with environmental dynamics in or-
der to understand whether the next actions could
violate human preferences learned in the first place.
Exclusively aligning with human intentions seems
too strong of a restriction even for adhering to the
very same intentions in the real world.
Partly inspired by Yang et al. (2024), this interdisci-
plinary position paper argues that empirical align-
ment’s nobility of purpose can disguise statistical
flaws.
We are convinced that the pursuit of aligning AI with
human preferences through observing the latter may
inadvertently introduce biases and limitations into
these systems. Unlike Yang et al. (2024), we specif-
ically focus on forward (a priori) alignment of ML
systems in an empirical way. That is, we make the
1
arXiv:2502.14581v2  [cs.AI]  12 May 2025

--- Page 2 ---

Figure 1. Number of arxiv paper uploads per year with alignment-related keywords (2019-2024).
case against aligning AI through observing human
preferences before deployment, see definitions 2.1
through 2.3 and Section 3. Constructively, we offer
three alternatives: Empirical backward (rather than
forward) alignment (Section 5) as well as prescrip-
tive (rather than empirical) alignment, both forward
(Section 4) and backward (Section 6), see Table 1.
Our stance relies on a statistical perspective, as em-
pirical alignment hinges on a myriad of (implicit
and often ignored) statistical assumptions like repre-
sentative samples, absence of confounders and well-
defined populations. We identify several statistical
biases as empirical alignment’s Achilles heel, see Sec-
tion 3.3. Effectively, they skew the alignment goals
away from the “purpose which we really desire” to a
“colorful imitation of it” (Wiener (1960), page 1355,
see above).
Unlike backward empirical alignment, which aligns
AI after deployment, forward empirical alignment
directly leads to these alignment-caused biases be-
ing encoded in the AI models. This makes it hard to
disentangle them from the originally trained model.
Thus, we contend that AI should be – wherever pos-
sible – explained and altered a posteriori rather than
empirically aligned a priori. Section 5 compares the
merits of backward empirical alignment to the perils
of forward empirical alignment in greater detail.
Empirical-alignment-induced biases are not only
counterproductive for solving novel tasks in non-
human-centered environments (Yang et al., 2024).
More dramatically, these biases restrict an AI sys-
tem’s potential for scientific discovery by confining
them to human-centric perspectives. They hinder the
understanding of broader and potentially more im-
portant phenomena that lie beyond human interests
and perception.
Such anthropocentric biases are not unique to AI
alignment. In Section 3.1, we draw parallels to the
rich literature on anthropocentrism, eventually re-
lating alignment-induced biases to the observation
selection effect in physics, see Section 3.2. We learn
that AI systems will miss crucial parts of the universe
if empirically aligned with those that are perceived as
useful for humans or, more generally, that are perceiv-
able by humans at all. This implies that such biases
are unresolvable within an observational, i.e., purely
empirical framework. In this way, we expose empiri-
cal alignment as susceptible to the positivist “myth
of that which is the case” (Horkheimer & Adorno,
2002, page vii), credulously relying on observations
to accurately represent alignment goals.1 Indeed, fol-
lowing Popper (2002/1959, page 93-94),“[t]he empir-
ical basis” does not provide “a solid bedrock,” rather,
“[...] science rises [...] above a swamp.”
These insights motivate our call for prescriptive align-
ment, which aligns AI systems with transparent
axioms rather than human observations. Roughly
1Beyond alignment, such mindless adherence to obser-
vations without questioning their origin and relation to the
world has led to non-replicability in ML, see the position
paper of Herrmann et al. (2024).
2

--- Page 3 ---

speaking, our perspective hinges on the insight that
humans are reasonably good at defining rational ax-
ioms, but rather bad at acting according to them, see
Tversky & Kahneman (1974); Birnbaum et al. (2016);
Balagopalan et al. (2023) and Section 4. Recent work
by Kirk et al. (2024) serves as a motivating exam-
ple: They find that preferences of humans exposed
in conversations with large language models (LLMs)
depart from preferences pre-stated in a survey. In
Section 6, we showcase the advantages of prescriptive
over empirical alignment in a case study on decoding
of large language models.
In summary, this position paper cautions against
biases arising from forward empirical human–AI
alignment. We advocate for prescriptive instead
of empirical alignment and contend that, where
possible, AI should be a posteriori explained and
modified rather than a priori aligned.
2. Human–AI Alignment: A Taxonomy
We do not argue against human–AI alignment per se,
but rather focus on what we perceive as a popular
(see Fig. 1) yet often unquestioned approach to align-
ment in the ML community: forward and empirical
human–AI alignment. We approach this notion by
first defining alignment generally.
Definition 2.1 (Human–AI Alignment). Consider
any ML model identified with parameters ˆθ ∈Θ.
Denote by ω ∈Ωan alignment goal. Define human–
AI alignment as any process involving changes of
ˆθ that considers a function of the form Θ × Ω→
A; (ˆθ, ω) 7→||f(ˆθ) −g(ω)||, where f : Θ →A and
g : Ω→A map to some alignment space A equipped
with some notion of distance || · ||. For instance, this
process can be minˆθ∈Θ ||f(ˆθ) −g(ω)|| for fixed ω.2
We distinguish between forward and backward human–
AI alignment, somewhat reminiscent of Ji et al. (2023,
Section 1.2). Forward alignment refers to harmoniz-
ing AI systems with human values already during the
training phase and before deployment. In other words,
ˆθ is altered informed by (ˆθ, ω) 7→||f(ˆθ) −g(ω)|| be-
fore the test phase. The approach is more proactive,
embedding alignment into learning itself.
2Observe this definition’s similarity to model misspec-
ification in statistics (White, 1982), serving as additional
motivation for examining alignment through a statistical
prism, see Section 3.3.
Table 1. Fourfold distinction of forward vs. backward and
empirical vs. prescriptive human–AI alignment and our
positions.
Empirical
Prescriptive
Alignment
Alignment
Forward
Contra (Section 3)
Pro (Section 4)
Backward
Pro (Section 5)
Pro (Section 6)
Backward human–AI alignment, in contrast, changes
the parameters ˆθ of a trained model during or after de-
ployment. It includes safety evaluations, governance
frameworks, and interpretability methods, see Sec-
tion 5. This approach is rather reactive, focusing on
monitoring, adjusting, and managing AI behavior as
new risks or misalignments emerge during deploy-
ment.
An attentive reader might already have detected the
statistical nuance in this distinction: Our temporal
cut-off point to distinguish forward from backward is
when the model makes inferential statements about
the unobserved population for the first time.
In
other words, we differentiate between AI systems in
a purely descriptive state (capable only of making de-
terministic statements about the observed “training”
sample) and in an inferential state (making uncertain
statements about the unknown population or unseen
“test” sample thereof).
The motivation for backward alignment in this
distinction is straightforward: Before deployment,
changes to ˆθ are driven by training, i.e., by minimiz-
ing a loss Θ × Θ →R. After deployment, it is rea-
sonable to assume that the so-found ˆθ is “sufficiently”
(Bayes-)optimal w.r.t. this training objective. Subse-
quent changes to ˆθ are then motivated by alignment
– i.e., adaptation to human alignment goals ω beyond
mere learning of θ. In contrast, forward alignment
directly encodes ω in Θ while training.
In addition to the forward-backward distinction, we
define prescriptive human–AI alignment and empiri-
cal alignment as follows, giving rise to our fourfold
distinction in Table 1.
Definition 2.2 (Prescriptive Human–AI Alignment).
If Ω∋ω = ˜ω(A) are set according to pre-defined ax-
ioms ˜ω, the process in definition 2.1 shall be called
prescriptive human–AI alignment.
3

--- Page 4 ---

Definition 2.3 (Empirical Human–AI Alignment). If
Ω∋ω = ˆω(X) are set according to estimators ˆω(X)
of ω from observed human behaviors X, the process
in definition 2.1 shall be called empirical human–AI
alignment. Here, X denotes a multivariate random
variable X : S →Rq, q ∈N, describing the data
obtained from humans, where S is a sample space.
This paper’s main argumnet hinges on the simple yet
far-reaching insight that empirical alignment entails
statistical inference: Alignment goals are statistics
of observed human behavior, see definition 2.3. The
subsequent alignment thus hinges on their statistical
properties – in the words of Wiener (see above) they
should resemble “what we really desire and not a
colorful imitation of it”. Statistical biases can render
ω such a colorful imitation. We will discuss a myriad
of such biases in section 3.3 with respect to how these
affect the statistical properties of ˆω(X).
We emphasize the abstract nature of this fourfold dis-
tinction. In practice, the stylized separation between
forward and backward alignment is often less strict.
Consider, e.g., continual learning (Shin et al., 2017;
Kirkpatrick et al., 2017; Parisi et al., 2019; Lopez-Paz
& Ranzato, 2017). Here, dynamic environments re-
quire sequential training and hence also sequential
alignment.
The bulk of recent human–AI alignment research re-
volves around empirical alignment, see right chart
in Fig. 1. Examples of forward empirical comprise re-
inforcement learning from human feedback (RLHF)
(Christiano et al., 2023; Stiennon et al., 2020; Nakano
et al., 2021; Ouyang et al., 2022a; Bai et al., 2022a;
Glaese et al., 2022) or direct preference optimization
(DPO) (Rafailov et al., 2023; Richardson et al., 2024;
Tang & Xu, 2024; Afzali & Khodabandeh, 2024; Wang
et al., 2024a; Gupta et al., 2024; Yin & Leong, 2024; Li
et al., 2024).
In backward empirical alignment, post-deployment
fine-tuning, interpretability methods, and safety
checks allow the system to be continually refined
based on new data (Sun et al., 2019; Kairouz et al.,
2021).
Forward prescriptive alignment has its origins in
rule-based AI and expert systems (Giarratano & Ri-
ley, 1998). It goes beyond mere training on human
preferences and instead introduces explicit principles,
guidelines, or “constitutions” that prescribe what the
AI model should or should not do. Note that these
pre-defined axioms can harness observational infor-
mation, too. They can be functions of potential obser-
vations. For instance, rule-based rewards by Mu et al.
(2024) increase sample efficiency of RLHF through
rule-based alignment.
Albeit its origins laying in the last century, prescrip-
tive approaches to AI alignment are still popular
in state-of-the art models like DeepSeek-R1 (Guo
et al., 2025), which was trained on rule-based re-
wards for reasoning. Bai et al. (2022b;a); Kyrychenko
et al. (2025); Findeis et al. (2024) propose codify-
ing guidelines for harmlessness and helpfulness via
“Constitutional AI”, while Glaese et al. (2022) inte-
grate targeted human feedback to produce safer dia-
logue agents. Normative frameworks like Delphi and
Social Chemistry 101 collect large knowledge bases of
social and moral rules (Jiang et al., 2021; Forbes et al.,
2020). Meanwhile, Hendrycks et al. (2020) under-
score the importance of embedding shared human
values into model alignment protocols.
Lastly, backward prescriptive alignment involves en-
forcing explicit rule sets once the AI system is already
deployed, for instance, via real-time policy-based gov-
ernance (Ge, 2024; Bayne & Paul, 2005; Wang et al.,
2021; Miao et al., 2021) or via decoding of language
models, see Section 6.
3. Contra Forward Empirical Alignment
As this paper cautions against anthropocentric biases
arising from forward empirical alignment, we turn
to this kind of alignment in more detail. We first
emphasize the philosophical underpinnings of our
argument in Section 3.1, and then – motivated by the
anthropic principle in physics (Section 3.2) – discuss
concrete statistical biases in Section 3.3.
3.1. The Anthropocentric Bias
Anthropocentric thinking, which places humans at
the center of the universe, has deep roots in West-
ern thought. In the Judaeo–Christian tradition, the
anthropocentric perspective originates from the cre-
ation narrative, where humans are depicted as the
pinnacle of creation (Genesis 1:27). Historically, this
has heavily influenced science.
However, the anthropocentric interpretation of Gene-
sis 1:27 faced staunch opposition already from within
the Jewish tradition itself. One notable critic was
Moses Maimonides, a preeminent Torah scholar of
4

--- Page 5 ---

the twelfth century AD (Lamm, 1965; Shapiro, 2003).
In his seminal work, The Guide for the Perplexed, Mai-
monides emphasized the vastness and complexity of
the universe, which, in his view, diminished the cen-
trality of humans. He famously referred to humans
as "just a drop in the bucket," evoking Isaiah (40:15),
see Dan (1989). Notably, Maimonides’ opposition to
anthropocentrism was a theological one. He believed
that attributing undue importance to humanity was
arrogant and a misinterpretation of divine intent. For
Maimonides, recognizing the humility of human ex-
istence was essential for a proper understanding of
God and the natural order.
It was more than three centuries later when Nico-
laus Copernicus, Galileo Galilei, and Isaac Newton
established a new heliocentric model of the universe,
literally shifting the center of the universe away from
humans. This paradigm shift (Kuhn, 1997) paved
the way for the scientific revolution in the 16th and
17th centuries.
Yet, anthropocentric biases still persist in science to
this day. The argument is plain and simple: By fo-
cusing on explaining phenomena that are useful for
humans, we inadvertently miss structures that are not
perceived as useful according to current societal val-
ues, which are strongly limited in time and generality.
In the words of Peters (2012), "Nature has much more
structure than what is useful for humans." Strong po-
sitions within evolutionary epistemology even argue
we cannot perceive anything that is not useful, since
our cognitive apparatus is a product of evolution,
thus overfitted to useful elements of nature (Lorenz,
1977; Wuketits, 1990).
The example of Maimonides shows that even within
an overarching anthropocentric dogma, there is room
for critical reflection and nuanced positions. This mo-
tivates our stance on AI alignment. We are well aware
of the pressing need to align AI with human safety
constraints in the wake of ever more powerful models
and in anticipation of Artificial General Intelligence
(AGI), see also Section 7. However, we assert that
empirical alignment is the wrong path towards that
goal. Just like the Torah scholar Maimonides, who
firmly believed in the dogma of his times, we do not
oppose the paradigm of alignment generally. Quite
the contrary, for alignment to work sustainably, we
argue, it has to be freed from anthropocentric biases.
Figure 2. Limits of the human-observable universe: The
Hubble eXtreme Deep Field, showing roughly 5500
galaxies. Source: https://esahubble.org/images/
heic1214a/ (acc. 04/15/25)
3.2. The Anthropic Principle in Physics
Modern-day physics is aware of such anthropocentric
biases and – going even further – the more general
anthropic principle, also referred to as "observation
selection effect" (Bostrom, 2000; 2002; Carter, 1983).
It states that all possible observations of the universe
are limited by the fact that they can only be made in
a universe capable of developing intelligent life, and
is commonly attributed to Robert Dicke (Dicke, 1961;
1957), building on work by Paul Dirac. For example,
constants of nature like the electron charge appear
fine-tuned for life because, if they were not, we would
not be around to observe them.
Accepting this natural restriction to human reason-
ing, Bostrom (2002) postulates the self-sampling as-
sumption, which we can directly relate to empirical
alignment. It states: “One should reason as if one
were a random sample from the set of all observers
in one’s reference class” (Bostrom (2000), page 57).
The self-sampling assumption reveals an unresolv-
able dilemma of empirical alignment. If we define
the reference class broad enough to capture all envi-
ronments relevant to AI deployment, empirical align-
ment will violate the self-sampling assumption, since
the sample is biased towards humans. On the other
hand, if the reference class is narrowly restricted to
human-related objects, the model can hardly gen-
eralize beyond these objectives, see e.g.,Yang et al.
(2024).
Indeed, it was recognized by Schmidhuber (2000;
2002) that the anthropic principle provides little in-
5

--- Page 6 ---

sight when the thought experiment is restricted to
only one universe. A meaningful theory requires
informative priors or alternative universes, see ap-
proaches by Schmidhuber (2000; 2002); Bostrom
(2002). These are all pre-defined axioms, correspond-
ing to a prescriptive approach.
Transferred to empirical human–AI alignment, this
insight implies that we have to at least enrich em-
pirical alignment by axiomatic assumptions on the
alignment procedure. In Popper’s image of empirical
science rising “above a swamp”, see Section 1, these
assumptions are the “piles [...] driven down from
above into the swamp” (Popper, 2002/1959, page 93-
94). Blindly relying on a sample without additional
assumptions on the population where it is drawn
from will always lead to biased conclusions about
non-human entities. The heart of the matter is that
making no population-related assumptions implic-
itly corresponds to making the strongest assump-
tion of all – the sample being fully sufficient for the
alignment goal.
The anthropic literature teaches us that we have to
explicitly take sample selection probabilities into ac-
count, requiring a statistical perspective. We thus
need to consult the statistical literature on causal and
selective inference as well as sampling theory. The
following Section does the job.
3.3. The Statistical Perspective
The limits of empirical alignment can be best under-
stood from a statistical perspective: Empirical align-
ment intends to harmonize AI with the intentions of
some population of (potential) human agents, consti-
tuting Ωin Definition 2.1. This is commonly done by
means of a self-selected, thus – as we learned from
the anthropic principle in physics – distorted sample
thereof. This distortion can become manifest in a myr-
iad of statistical biases, which particularly have been
discussed in the social and survey statistics literature.
A sole focus on empirical evidence denies the prob-
lem of adequation (Menges, 1982; Grohmann, 2000),
which is concerned with the – eo ipso insufficient –
fit between what is, in principle, observable, describ-
able, and analyzable within the framework of our for-
malization process, and the “world-in-itself”. Recall
from Definition 2.3 that empirical alignment relies
on estimators ˆω(X) from data X : S →Rq obtained
from humans, where S is a sample space. The ade-
quation problem tells us that we implicitely aim for
some latent X∗: S∗→Rq, but only have access to its
observable counterpart X.
Groves & Lyberg (2010) concretise some major biases
arising from this discrepancy by their TSE-(Total
Survey Error) concept. They distinguish between
what we call population representation biases and
structural representation biases. The first one com-
prises, e.g., biases in the selection frame. That is, the
population from which the sample is taken differs
from the population of interest. That is, S∗̸= S. One
can distinguish over-coverage (S∗⊂S) and under-
coverage (S ⊂S∗). In practice, survey designers
often face a mixture of both.
Other instances of the population representation bi-
ases are the classical sampling error arising from a
random selection of the sample from the underlying
population and the unit-nonresponses arising when
certain units refuse, or are incapable of, participat-
ing in the survey. The latter can distort conclusions
because non-respondents’ characteristics often differ
systematically from those who participate, biasing S
away from S∗.
The structural representation biases refer to the
content-related part of the analysis and the result-
ing incomplete reflection of the complex relation-
ships between X and X∗. This includes the item-
nonresponse bias, arising when individuals ready
to participate in principle refuse to answer certain
sensitive questions. Response biases refer to biased
data obtained from those that do respond, comprising
acquiescence bias (a tendency to agree) or primacy
and recency effects (a preference for selecting the
first or last item in a sequence), see Kaufmann et al.
(2023). A concrete example of primacy bias in empir-
ical alignment arises in RLHF when presenting more
than two options to the human, see e.g. Early et al.
(2022). As was early recognized in the psychology
literature, fatigue and distraction can make humans
ignore the later (earlier) options and only select from
the ones on the top (the bottom) of the user interface
(Crano, 1977).
A further source of structural representation bias,
not explicitly elaborated in the TSE framework by
Groves & Lyberg (2010), is the omitted variable bias.
It refers to situations when decisive influence factors
(like hidden personal characteristics or genetic dis-
positions) are not accessible to the researcher, for ex-
ample, for reasons of privacy preservation. This can
spuriously enlarge the effect of global variables like
6

--- Page 7 ---

sex or age in a merely empirical data-based analysis.
Note that all the biases listed here are big data biases
in the sense that they do not vanish with increasing
sample size. The only exception is the usual statistical
uncertainty induced by the sample error.
Beyond the TSE, there is a bulk of statistical literature
on what Benjamini (2020) calls “the silent killer of
replicability”: Selective inference. It occurs when
hypotheses, models, or features are selected based
on the observed data. Such post-selection inference
biases arise in numerous scenarios, like variable selec-
tion in regression models, multiple hypothesis test-
ing, and adaptive stopping rules in ML (Benjamini
& Hochberg, 1995; Wasserman, 2009; Fithian et al.,
2014; Tibshirani & Taylor, 2016; Lee et al., 2016).
Empirical alignment is prone to suffer from selective
inference, if the alignment targets ω are functions
of the same observations X being used for finding
ˆθ ∈Θ through empirical risk minimization, see def-
inition 2.1, as is often the case. If data is sampled
anew from a different population for alignment, such
trouble can be avoided. In that case, however, the
procedure becomes very data hungry. This can pose
practical challenges, as human samples are typically
burdensome and expensive to acquire (Shinn et al.,
2024). For an illustrative example of selective infer-
ence that arises when empirically aligning language
models, we refer the interested reader to experimen-
tal results in Appendix C.
Reflexivity constitutes an even more fundamental
problem in empirical alignment. In addition to the
observation selection effect – which persists in any
empirical science, see Section 3.2 –, empirical human-
AI alignment suffers from a fundamental problem
in the social sciences: The observant entity (human)
coincides with the observing entity (also human).
Unlike for celestial bodies (natural sciences), we can
expect humans (social sciences) to react to conclu-
sions (in our case, AI alignment) being drawn from
observing them, thereby compromising the validity
of those conclusions.
This “reflexivity problem” (Soros, 2015) dates back
to early work of Morgenstern (1928) and has recently
seen some revival in the ML community, recogniz-
ing the fact that today’s predictions can change to-
morrow’s population (Perdomo et al., 2020; Hardt
& Mendler-Dünner, 2023; Mendler-Dünner et al.,
2020; Miller et al., 2021). Examples range from self-
negating traffic route predictions to self-fulfilling
credits scores. In empirical alignment, this translates
to estimated ˆω affecting X, from which ˆω is learned in
the first place. In iterative learning setups, reflexive
effects between parameters and data can even occur
within the sample (Rodemann et al., 2025; Rodemann
& Bailie, 2025).
To make reflexivity more tangible, consider the pop-
ular example of fine-tuning LLMs by RLHF, which
implicitly relies on the “unrealistic” (Carroll et al.,
2024) assumption that human preferences regarding
LLM answer quality is static. To say the least, it is cer-
tainly plausible that previous LLM answers affect our
judgments through, e.g., anchor effects (Lieder et al.,
2018). Very recently, Carroll et al. (2024) took steps
to address such feedback loops by drafting AI align-
ment as a dynamic Markov Decision Process (MDP),
taking into account that our preferences can change
by interacting with changing AI systems. Mitelut
et al. (2023) go further and argue entirely against
alignment to human intent, since AI systems can re-
shape the latter, see also Gabriel (2020).
Causal misrepresentation refers to misleading as-
sociations that do not reflect causal connection be-
tween variables. Such correlations occur in observa-
tional data, on which empirical alignment mostly still
hinges on – with the notable exception of experimen-
tal methods in the assurance literature, see Ji et al.
(2023, §4.3).
In our setup, let X = (Y, Z) with Y : SY →Rq and
Z : SZ →Rq random variables denoting such exper-
imental data. Further, assume our alignment goal ω
consists of the causal effect of Z on Y , e.g., answer
length (Z) on answer quality rated by humans (Y)
for LLM replies. We do not know the actual (true)
causal effect ω, but we observe human ratings of the
quality Y and LLM answer lengths Z and can com-
pute an estimator ˆω(Y, Z), e.g. the Bravais-Pearson
correlation coefficient:
ˆρ(Y, Z) =
Cov(Y, Z)
Var(Y ) Var(Z).
Causal misrepresentation bias implies there is an ad-
ditional variable C, e.g. educational background,
that affects both Z and Y. For instance, people with
college degrees might tend to prefer longer responses
(effect of C on Y ). At the same time, college-educated
prompters might ask more complicated questions
triggering longer replies (effect of C on Z). This im-
plies a spurious correlation between Y and Z. Our
7

--- Page 8 ---

estimator ˆω is thus biased away from the true ω. It
falsely captures the relation between answer length
and quality, while the actual cause of both (educa-
tional background) is not taken into account.
Statistical science offers sound remedies for many of
the above mentioned biases, see Nalenz et al. (2024);
Rodemann et al. (2022) for instance. They typically
involve additional assumptions about the popula-
tion like “absence of unobserved confounders.” Es-
sentially, these assumptions are prescriptive elements,
which we advocate for. Even if they are self-evident
as in the case of confounders, we strongly encourage
making them explicit.
This increases transparency not only for humans but
also for AI, thus addressing potential unintended mis-
alignments due to miscommunication. If AI systems
fail to understand that the actual goal is population-
alignment rather than sample-alignment, conse-
quences can be dire, see Bostrom (2014, pages 122-
125) and Harari (2024, Chapter 8). For instance, spu-
rious correlation between race and occupation status
in alignment samples might lead to discrimination
through aligned AI Systems.
While these statistical remedies address known epis-
temic uncertainties (Hüllermeier & Waegeman, 2021)
(“known unknowns”) about the population, there
are potentially many more unaddressed sources of
uncertainty (“unknown unknowns”), see e.g., Rode-
mann & Augustin (2021; 2022; 2024). This especially
holds for statistical representation of preference data,
essential to measuring human intentions, as we detail
in the next Section.
4. Pro Forward Prescriptive Alignment
The theory of preference(s) (relations) originates in
modeling rational agents within the foundations of
decision theory. It finds ever broader areas of appli-
cation in modern ML (e.g., Fürnkranz & Hüllermeier
(2003); Jansen et al. (2023a;c); Bengs et al. (2021);
Jansen et al. (2024); Rodemann et al. (2023a;b; 2025);
Dietrich et al. (2024); Kim & Oh (2024)). In partic-
ular, the subfields of preference elicitation (e.g., Ha
& Haddaway (1999); Baarslag & Gerding (2015);
Mukherjee et al. (2024)) and preference aggregation
(e.g., Eugster et al. (2012); Jansen et al. (2018); Zhang
& Hardt (2024)) play decisive roles here. In what
follows, we support our case pro forward prescriptive
alignment by findings from these two subfields.
The term preference elicitation refers to the systematic
retrieval of initially unknown (human) preferences,
often achieved by successively (and adaptively) pre-
senting queries to the agent under consideration.
It is an excellent illustration of the superiority of a
prescriptive understanding of alignment (using pre-
defined axioms ˜ω as alignment targets ω ∈Ω, see Def-
inition 2.2) over a purely empirical understanding
of alignment (Definition 2.3): It is easy to find pre-
defined axioms on the nature of preference structures
modeling rational behavior that meet broad social
consensus. – and it is precisely these supposedly
rational axioms that are often violated in empirical
studies.
These violations, however, are often due to lacking
oversight rather than being conscious and intended
choices of the agent. At the same time, integrating ra-
tionality axioms in elicitation strategies is an instance
of forward prescriptive alignment: The axioms are
agreed upon before the model is deployed.
Probably the most prominent example of a rational-
ity axiom in the context of preference elicitation is
that of transitivity: If an agent prefers a over b and b
over c, then the preference of a over c should follow.
While there is strong theoretical support of transitiv-
ity via money-pump arguments (e.g., Aldred (2003)),
numerous studies (e.g., Birnbaum et al. (1999; 2016);
Birnbaum & Schmidt (2008); Bikhchandani & Segal
(2021); Guadalupe-Lanas et al. (2020)) show that
agents often behave intransitively or even cyclic, al-
though they fully agree with transitivity as a ratio-
nality axiom.
This happens in particular when the choice situation
is dynamic and a large number of different options for
action are available. The intransitivity of the agent’s
behavior in such cases is rather an expression of their
limited comprehension than an ideal of action to be
elevated to a principle. Consequently, the naive de-
mand for a purely empirical alignment here would
translate to an AI that only imitates the agent’s lack
of oversight instead of pursuing and supporting their
actual interests.
A simple prescriptive alignment strategy that prevents
the occurrence of intransitive preference patterns by
construction was proposed by Jansen et al. (2022):
Instead of asking the agent about all possible pair-
wise comparisons step by step, the transitive hull of
the elicited preferences is formed after each query.
The next pair to be presented is then selected from
8

--- Page 9 ---

the remaining pairs, excluding those pairs that would
follow anyway due to transitivity, ensuring the final
result to be transitive.
Beyond elicitation procedures, another problem of
purely relying on empirical alignment arises in the
context of preference aggregation. This term refers to
the problem of defining procedures that aggregate
arbitrary profiles (fixed-size tuples) of preference re-
lations to one collective preference, in a way that is
conceived fair. For instance, preference aggregation
plays a crucial role in benchmarking problems un-
der multiple evaluations (e.g., Eugster et al. (2012);
Mersmann et al. (2015); Rodemann & Blocher (2024);
Zhang & Hardt (2024)), where one aims to aggregate
several rankings of ML algorithms, e.g., obtained by
domain experts.
Infamously, the attempt to define (full-domain) ag-
gregation procedures for preference profiles is gen-
erally doomed to failure already under very weak
axiomatic conditions. This follows from Arrow’s im-
possibility theorem (Arrow, 1950), which was dis-
cussed in Conitzer et al. (2024) as a major challenge
in aligning AI with diverse human feedback.
A common way to get around this impossibility is to
retreat to the Pareto front of the aggregation problem,
i.e. to base analyses on the (undominated elements
of the) partial preference order arising as the intersec-
tion of the preference orders in the respective profile.
However, this strategy, too, has serious disadvan-
tages: Retreating to the Pareto front – given some of
the preference orders in the profiles originate from
some (latent) real-valued score – results in signifi-
cant information loss and thus inefficiency, see. e.g.,
Jansen et al. (2023b); Farrow & Goldstein (2009).
Both challenges just sketched – aggregation and
Pareto-analysis – essentially originate from an im-
plicit assumption of purely empirical forward align-
ment.
Accordingly, both challenges can potentially be
avoided by a prescriptive approach: In the context
of aggregation, this would imply that the aggregate
does not have to correspond directly to a function of
the preference orders of the individual agents. In-
stead, external factors could also be taken into ac-
count in the aggregation, allowing the rigid frame-
work of the impossibility theorem to be left behind.
In the light of the second problem, the inefficiency
of the Pareto front can also be remedied: As demon-
strated in e.g., Kreuter (2013); Jansen et al. (2022), in
the process of eliciting preferences, paradata about
preference intensity (i.e., latent cardinal information)
can be implicitly collected, allowing the full available
information to be included. Under a prescriptive
alignment paradigm, this data – not directly related
to targeted human behavior – could be used to ob-
tain significantly more information-efficient improve-
ments on the Pareto front.
5. Pro Backward Empirical Alignment
Another argument versus forward empirical align-
ment stems from the pursuit of transparency. While
most ML models are powerful predictors their deci-
sion making process typically is not human intelligi-
ble – with the exception of intrinsically interpretable
models. Transparency, however, is desired to un-
derstand model decisions especially in high-stakes
environments – let alone legal requirements like the
EU AI Act.
We argue that forward empirical alignment adds to
the opacity of models. In RLHF, for example, the
reward function is typically approximated by a deep
neural network trained on observed human behavior
(Christiano et al., 2023), and hence the (often non-
transparent) policy is optimized using feedback from
a nontransparent reward model. More importantly,
though, any forward empirical alignment encodes
biases into the model that cannot be disentangled
from dependencies in the training data as discussed
in Section 3.3, which further impedes model under-
standing.
Thus, we argue for more transparent alignment. Pre-
scriptive alignment techniques check this box by ex-
plicitly stating the axioms a model shall be aligned to.
If the latter is impractical, however, we offer changes
of an ML model’s parameters ˆθ ∈Θ informed by
interpretable ML (IML) as potential strategy. We call
this backward alignment. Modifications to the model
architecture, by contrast, are another valid option but
per definition not part of the alignment process of
the original model.
There is a vast literature on IML methods for classical
ML (e.g., Molnar (2022); Ribeiro et al. (2016); Lund-
berg & Lee (2017); Greenwell et al. (2018); Covert
et al. (2020)) as well as those dedicated to explain
decision making in RL (e.g., Puiutta & Veith (2020);
Milani et al. (2022); Madumal et al. (2019); Topin
9

--- Page 10 ---

Table 2. Empirical vs. prescriptive alignment of language models: Decoding strategies Contrastive Search (CS) and DoubleExp
are compared across three datasets using two alignment metrics: QText (prescriptive) and MAUVE (empirical) for Automatic
Evaluation. Human Evaluation results indicate the percentage of evaluators favoring each strategy based on perceived
semantic coherence and fluency. Human selections align with QText (prescriptive), see Garcés Arias et al. (2024b). All results
are reported as percentages.
Automatic Evaluation
Human Evaluation
Dataset
QText (prescriptive) ↑
MAUVE (empirical) ↑
Semantic coherence ↑
Fluency ↑
CS
DoubleExp
CS
DoubleExp
CS
DoubleExp
CS
DoubleExp
Wikinews
91.95
82.79
84.14
90.65
73.00
27.00
61.00
39.00
Wikitext
87.64
81.50
77.97
84.07
57.00
43.00
60.50
39.50
BookCorpus
88.71
82.12
84.74
85.66
64.50
35.50
61.00
39.00
All
89.68
82.22
82.82
87.16
66.00
34.00
59.00
41.00
& Veloso (2019); Olson et al. (2021); Huang et al.
(2018)).
Such methods typically provide explanations of ML
models during or after deployment that are subse-
quently inspected by human observers. Upon in-
spection, model explanations can a posteriori assure
that the model works as intended. On the contrary,
the observer can infer that the model behaves against
their intentions and imply changes on the parameters
ˆθ ∈Θ without ever explicitly stating their preferences
and while never providing universally applicable ax-
ioms. Thus, we merely observe human preferences
implicitly and call the latter scenario empirical back-
ward alignment.
Note that – while inherently prescriptive – the choice
of the (I)ML method is not yet part of the alignment
process. As we argue for transparent alignment, we
contend that such a posteriori informed backward
alignment achieves this due to the more explicit na-
ture of the performed changes unlike forward empir-
ical alignment. Moreover, the strategy comprises a
rather static choice situation which can mitigate the
issue of irrational behavior in empirical alignment
raised in Section 4.
As a tangible example of backward empirical align-
ment, assume a model was trained to classify images
into “husky” and “wolf”. While highly predictive,
in the example from Ribeiro et al. (2016), the model
explanation shows white pixels (i.e., snow) to be an
influential feature. Hence, you find the model to
be unaligned with prior knowledge, as snow is not
the crucial difference between both classes, and you
would not trust the model to generalize well. Based
on this insight, you may want to change ˆθ by retrain-
ing the model on more diverse training data. Note
that any subsequent model change will always be in-
formed by model behavior after the first deployment,
and hence — once this knowledge was introduced —
the process shall be considered backward.
6. Pro Backward Prescriptive Alignment
An illustrative example of backward alignment in
language models emerges in the choice of decoding
strategies for autoregressive text generation. These
strategies specify how each subsequent token is se-
lected from the model’s probability distribution over
tokens at every inference step, thereby exerting a crit-
ical influence on the quality of the generated text.
Various automatic metrics have been introduced to
evaluate text generated by different decoding strate-
gies. Among them are several prescriptive ones like co-
herence, diversity or QText (harmonic mean of these
latter), and empirical ones such as MAUVE (Pillutla
et al., 2021). For a detailed overview and technical
description, we refer to Appendix A.1 and A.2. While
coherence assesses how likely the generated text is
given the prompt, diversity measures lexical repeti-
tion rates (Su & Xu, 2022). In contrast, MAUVE mea-
sures how closely machine-generated text aligns with
empirical samples of human-written text by com-
paring their distributional “fingerprints” in a latent
representation space. Technically, it calculates the
Kullback–Leibler divergence between the two distri-
butions. Higher MAUVE scores correspond to lower
divergence, indicating greater similarity to human-
produced text.
10

--- Page 11 ---

Choosing a decoding strategy to align the model out-
put with human-generated text is an obvious exam-
ple of backward alignment: Decoding strategies are
chosen after the language model has been trained,
allowing for fine-tuning towards human preferences.
Relying exclusively on MAUVE to select or evalu-
ate decoding strategies constitutes backward empirical
alignment: the quality of a strategy is evaluated based
on how well its text generations align with observed
human-written text samples. This methodology has
notable limitations, as our illustrative case study re-
veals: Based on experimental results in Garcés Arias
et al. (2024b; 2025), we compare the quality (assessed
by human evaluators) of text generated by the same
model (GPT2-XL (Radford et al., 2019)) using two
different decoding strategies, namely CS (contrastive
search, Su & Xu (2022); Su & Collier (2023)) and
DoubleExp (Garcés Arias et al., 2024b). In one sce-
nario, the decoding strategy is empirically aligned
via MAUVE. In the other scenario, we use QText, a
prescriptive metric, to choose the decoding method.
Table 2 highlights discrepancies between high
MAUVE scores and human judgments of final text
quality. In other words, if we choose a decoding strat-
egy empirically through MAUVE, the output is judged
to be of lower quality than the one generated by a
prescriptively chosen decoding strategy. While Dou-
bleExp consistently achieves higher MAUVE scores
than CS, it is rejected by human evaluators, which
prefer CS for its perceived semantic coherence and
fluency.
In a nutshell, these findings suggest that humans
favor text from a model that was not aligned to em-
pirically observed human-generated text but to a pre-
scriptive metric. For further results, we refer to Tables
3 and 4 in Appendix B. Conclusively, we emphasize
that these findings are not limited to specific decod-
ing methods like CS, see comprehensive studies in
Su & Xu (2022); Garcés Arias et al. (2024b;a; 2025);
Ding et al. (2025).
7. Alternative Views
In this Section, we present three alternative views –
pro forward empirical alignment, contra prescriptive
alignment, and contra alignment altogether.
7.1. Pro Forward Empirical Alignment
While statistical caution is appropriate, there might
be other – potentially superior – reasons to do align AI
with human preferences in a forward empirical way.
Often, ML’s main and only goal is good prediction.
Strong cases for empirical alignment are especially
concerned with such "performance" goals (see Ibarz
et al. (2018)).
A prime example is InstructGPT (Ouyang et al.,
2022b), an LLM trained with a "technique [that]
can align to a specific human reference group for
a specific application" (p. 18). The authors name
improved performance and cost-effectiveness over
larger models as key benefits of their approach. Sti-
ennon et al. (2020) report similar benefits of smaller,
empirically forward aligned models for the clearly
defined task of text summarization. Potentially re-
duced model size while maintaining predictive per-
formance is further desirable for the widespread de-
ployment of ML models on less powerful hardware.
We refer to Appendix D for a similar argument in de-
fense of forward empirical alignment from a bench-
marking perspective.
7.2. Contra Prescriptive Alignment
In this paper, we argue that prescriptive alignment
should be favored over empirical alignment, since the
latter suffers from serious statistical shortcomings;
nevertheless, prescriptive alignment is not without
its own limitations. How to agree on predefined ax-
ioms ω that govern prescriptive alignment, is highly
relevant and non-trivial. People often disagree with
each other on which principles are normatively de-
sirable. Prescriptive alignment is only valuable if one
accepts the principles that have been agreed upon in
the first place.
Nevertheless, there are two clear advantages over
a naive empirical alignment process. Firstly, align-
ment becomes more transparent and thus more ob-
jective through a prescriptive approach: If you agree
with the pre-defined normative principles, you can
check whether the AI acts in accordance with these
principles and, if in doubt, intervene. This seems
hardly possible for empirical alignment, where we
cannot distinguish whether the AI breaks the rules or
the human is just inconsistently violating principles
they would accept in theory. Secondly, prescriptive
alignment offers the possibility of AI systems acting
according to normative principles controlled by hu-
11

--- Page 12 ---

mans, which humans themselves may not be able to
implement in their concrete behavior.
7.3. A Case Against Alignment Altogether
With the very same principled arguments from Sec-
tion 3, one might as well arrive at the reasonable po-
sition of giving up alignment entirely. Our offered al-
ternatives (backward and/or prescriptive alignment)
increase transparency and decrease negative effects
of statistical biases. Yet, they cannot resolve the fun-
damental dilemma of the observation selection effect:
As detailed in Section 3.1, any alignment to humans
will necessarily bias the AI away from other entities
in nature. Fundamentally opposing alignment might
thus be particularly justified if the AI’s goal is scien-
tific inference, e.g., by means of IML.
While we considered explicit changes to a model
informed by IML as backward alignment, the use of
IML can end at the stage of model explanation as a
tool for scientific inference (Freiesleben et al., 2024;
Ewald et al., 2024; Molnar et al., 2023; König et al.,
2024) – typically about the data generating distribu-
tion. From a statistician’s perspective, we deem such
inference as valuable in itself and further argue that
principled explanations aid in understanding model
decisions. Covert et al. (2020) introduce SAGE val-
ues for so called global feature importance that – under
certain conditions – represent mutual information
between inputs and output or conditional output
variance, König et al. (2024) extend similar insights
to feature dependencies and Freiesleben et al. (2024)
define a general framework to design and use IML
methods for scientific inference grounded in statisti-
cal learning theory.
We contend that a bias from any form of alignment
encoded in the ML model can confound the rela-
tions between the model variables and as a result
diminish the potential for scientific discovery. This
argument is further underlined by findings from RL.
Silver et al. (2017) show that the famous AlphaGo
model trained from observations of human play is
inferior to AlphaGo Zero trained without human knowl-
edge. Moreover, Schut et al. (2023) use concept-based
explanations to extract sequences of actions in chess
from an AI trained without human oversight that go
beyond human skill level.
It thus can be argued that not only forward empiri-
cal, but any kind of alignment – in the language of
Schut et al. (2023) – biases the machine representational
space towards the human representational space. It in-
troduces or exacerbates an anthropocentric bias that
can substantially reduce AI’s ability to learn concepts
beyond human knowledge.
8. Conclusion
AI alignment is a double-edged sword. Done well,
it makes AI safer. Done poorly, it biases models and
limits their potential for discovery. This paper devel-
oped a nuanced statistical perspective on this trade-
off. It cautioned against forward empirical alignment
unless strictly necessary.
We emphasized the statistical caveats of common
empirical alignment practices (Section 3) and scru-
tinized (in)consistencies of observed human pref-
erences (Section 4). We showed that forward em-
pirical alignment is especially prone to “locking in”
statistical biases during training. What is more, we
constructively discussed alternatives like prescriptive
(Section 4 and 6) and backward (Section 5 and 6) align-
ment. We further provided practical guidance by
concrete examples like decoding of language models
(Section 6).
Along the way, we discovered a fourfold taxonomy
– distinguishing forward vs. backward, empirical
vs. prescriptive (Table 1) – of alignment methods
that might be of independent interest. Our hope is
that this taxonomy and the accompanying arguments
guide the ML community towards (more) statisti-
cally informed alignment. We wish to stimulate a
constructive debate on the trade-offs between these
different approaches to alignment, see also the con-
trasting opinions in Section 7.
To invoke Norbert Wiener, whose famous quote on
the alignment problem (see Section 1) motivated this
whole paper, once again:
“Moreover, if we move in the direction of making
machines which learn and whose behavior is
modified by experience, we must face the fact
that every degree of independence we give the
machine is a degree of possible defiance of our
wishes.”
– Norbert Wiener, 1949, Markoff (2013, acc.
01/15/25)
As AI grows more autonomous, “who aligns whom?”
will become a central ethical question. Our position
12

--- Page 13 ---

is clear: Alignment should be governed by principles,
not just by unreflected mirroring of observations.
9. Statement on Societal Impact
This paper warns against the uncritical and naive
use of forward empirical alignment, arguing that
such alignment introduces statistical biases and an-
thropocentric constraints. We propose alternatives:
prescriptive alignment and backward adjustments.
These latter ensure transparency and prevent AI from
merely imitating (potentially irrational and inconsis-
tent) human behavior at the cost of better reasoning.
Misalignment can lead to significant societal risks, as
touched upon in Section 3.3.
Future AI policy should thus consider the biases dis-
cussed in this position paper. Regulation should not
blindly enforce empirical alignment, but instead, de-
mand transparency in how models are aligned. This
means documenting alignment assumptions, ensur-
ing explainability, and regularly auditing statistical
biases in training data.
The ethical stakes are high. If AI is aligned to flawed
human preferences, it may amplify societal biases
rather than correct them.
At worst, it could reinforce harmful power struc-
tures, see the example of racial biases in Section 3.3.
Conversely, dismissing empirical alignment entirely
might create models that fail to serve human needs.
We advocate a middle ground: rigorous, principle-
based alignment that minimizes bias while allowing
AI to generalize beyond human-imposed limits.
Particularly, by pushing for a middle ground, we ob-
ject to the misinterpretation of this paper’s arguments
as a call against alignment altogether. We discussed
this as an alternative view in Section 7. Abandoning
alignment entirely poses the severe and existential
risk of loosing human control over AI systems, po-
tentially giving rise to several “doom” scenarios, see
also Section 3.1.
13

--- Page 14 ---

A. Metrics for Evaluating Decoding of Language Models
In what follows, we discuss the prescriptive and empirical metrics used for language model alignment via
decoding strategy selection in Section 6.
A.1. Prescriptive Metrics
Coherence.
Proposed by Su & Xu (2022), the coherence metric is defined as the averaged log-likelihood of the
generated text conditioned on the prefix text as
Coherence(ˆx, x) = 1
|ˆx|
|ˆx|
X
i=1
log pM (ˆxi | [x : ˆx<i])
where x and ˆx are the prefix text and the generated text, respectively; [:] is the concatenation operation and M
is an external language model, namely OPT (2.7B) (Zhang et al., 2022).
Diversity.
Proposed by Su & Xu (2022), the diversity metric aggregates n-gram repetition rates:
DIV =
4
Y
n=2
| unique n-grams (xcont ) |
| total n-grams (xcont ) |
A low diversity score suggests the model suffers from repetition, and a high diversity score means the model-
generated text is lexically diverse.
QText.
QText (Garcés Arias et al., 2025) is given by the harmonic mean of rescaled coherence and diversity:
QText =
2
1
COH +
1
DIV
∗100,
where
COH =
Coherence −min(Coherence) + 1
max(Coherence) −min(Coherence) + 1.
QText values close to 100 indicate high-quality text generation, while values approaching zero reflect low-quality
outcomes.
A.2. Empirical Metrics
MAUVE.
MAUVE (Pillutla et al., 2021) is a metric designed to quantify how closely a model distribution Q
matches a target distribution P of human texts. Two main types of error contribute to any discrepancy between
Q and P:
• Type I Error: Q assigns high probability to text that is unlikely under P.
• Type II Error: Q fails to generate text that is plausible under P.
These errors can be formalized using the Kullback–Leibler (KL) divergences KL(Q ∥P) and KL(P ∥Q). If P
and Q do not share the same support, at least one of these KL divergences will be infinite. To address this issue,
Pillutla et al. (2021) propose measuring errors through a mixture distribution
Rλ = λP + (1 −λ) Q
with λ ∈(0, 1).
14

--- Page 15 ---

Table 3. Automatic evaluation results: Comparison of Contrastive Search (CS) and DoubleExp across Wikinews, Wikitext, and
BookCorpus using two automatic metrics: QText and MAUVE. DoubleExp outperforms CS in terms of MAUVE, while CS
outperforms DoubleExp in terms of QText across all three datasets.
Dataset
QText (prescriptive) ↑
MAUVE (empirical) ↑
CS
DoubleExp
CS
DoubleExp
Wikinews
91.95
82.79
84.14
90.65
Wikitext
87.64
81.50
77.97
84.07
BookCorpus
88.71
82.12
84.74
85.66
All
89.68
82.22
82.82
87.16
Table 4. Human evaluation results: Human ratings of Contrastive Search (CS) and DoubleExp across Wikinews, Wikitext, and
BookCorpus, focusing on perceived semantic coherence and fluency of the generated text. DoubleExp is consistently rejected
by human evaluators.
Dataset
Semantic coherence
Fluency
CS is better
CS and DoubleExp are similar
DoubleExp is better
CS is better
CS and DoubleExp are similar
DoubleExp is better
Wikinews
56%
34%
10%
32%
58%
10%
Wikitext
34%
46%
20%
29%
63%
8%
BookCorpus
49%
31%
20%
32%
58%
10%
All
48%
36%
16%
28%
62%
10%
This leads to redefined Type I and Type II errors given by
KL
 Q∥Rλ

and
KL
 P ∥Rλ

,
respectively.
By varying λ and computing these two errors, one obtains a divergence curve
C(P, Q) =
 exp
 −c KL(Q∥Rλ)

, exp
 −c KL(P ∥Rλ)

: Rλ = λP + (1 −λ)Q, λ ∈(0, 1)
	
,
where c > 0 is a hyperparameter that controls the scaling.
Finally, MAUVE(P, Q) is defined as the area under the divergence curve C(P, Q). Its value lies between 0 and
100, with higher values indicating that Q is more similar to P.
B. Further Results on Decoding Alignment of Language Models
We provide additional details on the experimental results presented in Section 6, see also Garcés Arias et al.
(2024b; 2025). Tables 3 and 4 provide a more granular breakdown of the empirical versus prescriptive alignment
methods evaluated in Table 2 in the main paper. Table 3 presents quantitative comparisons across various datasets
and evaluation metrics, highlighting the alignment discrepancies when relying on empirical metrics like MAUVE
versus prescriptive metrics such as QText. Table 4 provides a more detailed breakdown of the human evaluation
results reported in Table 2 in the main paper. The latter summarized the human preferences by reporting the
share of text generations that was preferred, while Table 4 additionally shows indifference votes. The results
reinforce the finding that empirical alignment methods may not necessarily correspond to human-perceived text
quality. This further substantiates our argument for a more principle-driven approach to AI alignment. To reflect
the share of human raters favoring each decoding strategy, as depicted in Table 2 in the main paper, we apply the
following scoring approach:
Score CS =
#(CS is better ) + 0.5 × #( tie )
#(CS is better ) + #( tie ) + #( DoubleExp is better )
Score DoubleExp = 100 −Score CS.
15

--- Page 16 ---

C. Selective Inference in Decoding Alignment of Language Models
Dataset
Truncation
# Examples
MAUVE(%)↑
Preferred
length
CS
ACS
CS
ACS
∆
Method
Wikinews
64
1939
2000
87.42
85.79
-1.63
CS
96
1920
2000
81.11
88.13
7.02
ACS
128
1859
1977
84.14
85.39
1.25
ACS
160
1684
1824
84.86
85.78
0.92
ACS
192
1447
1617
85.23
87.10
1.87
ACS
Wikitext
64
1296
1314
82.78
86.83
4.05
ACS
96
1280
1314
81.46
85.67
4.21
ACS
128
1250
1301
77.97
79.82
1.85
ACS
160
845
889
69.66
80.53
10.87
ACS
192
529
564
81.50
75.45
-6.05
CS
BookCorpus
64
1907
1947
84.22
87.04
2.82
ACS
96
1873
1947
87.82
83.66
-4.16
CS
128
1657
1749
84.74
85.49
0.75
ACS
160
863
922
83.59
83.68
0.09
ACS
192
476
518
79.43
83.38
3.95
ACS
Table 5. Illustration of selective inference in aligning decoding strategies for language models. MAUVE scores are computed
on both machine- and human-written text. In order to compute the KL-divergence, see Appendix A.2, MAUVE typically
considers samples based on the minimal token lengths observed in human-reference texts (already seen during model
training). Texts exceeding this length are truncated, while texts that do not achieve this length are excluded from the sample.
Results are reported across three different datasets. This can be seen in the varying numbers of examples (column 3). Positive
∆-values indicate that the decoding method ACS (Garcés Arias et al., 2024b) outperforms the baseline CS (Su & Collier,
2023). All computations were performed using the gpt2-xl model (Radford et al., 2019). For CS (Su & Collier, 2023),
hyperparameters k = 5 and α = 0.6 were selected.
In this section, we discuss a tangible and concrete example of selective inference (Section 3.3) arising in empirical
alignment of decoding methods in language models.
When empirically aligning decoding methods via MAUVE, see also section 6, only machine-generated samples
that match the distributional length constraints of human-written texts are considered. Any generated text that
exceeds these bounds is often truncated or outright discarded (Pillutla et al., 2021; Garcés Arias et al., 2024b). This
leads to a biased evaluation where only text that “fits” pre-existing norms is measured, disregarding potentially
superior but unconventional outputs. More precisely, MAUVE is typically computed over samples based on
the minimal token lengths observed in human-reference texts (already seen during model training), in order
to compute the Kullback-Leibler-divergence between their respective distributions, see Appendix A.2. Texts
exceeding this length are truncated, while texts that do not achieve this length are excluded from the sample.
Through a statistical lens, any inference from a so-aligned model is doomed to suffer from post-selection bias – as
discussed in Section 3.3. Only considering samples of a certain length corresponds to reducing the domain of
the sample, i.e, setting some parameters ˆθ to zero, thus shrinking the model’s effective parameter space Θ. All
subsequent probabilistic inference guarantees are then hampered, because they fail to condition on the events
(that is, sample realizations) that led to the changes of Θ. Correction methods (e.g., Berk et al. (2013); Benjamini
& Hochberg (1995); Wasserman (2009); Fithian et al. (2014); Tibshirani & Taylor (2016); Lee et al. (2016)) can
render post-selection inference valid again. These prescriptive elements, however, are not considered in many
empirical alignment use cases like decoding alignment through MAUVE (Pillutla et al., 2021).
This highlights a general pattern: Forward empirical alignment, if driven by selective inference, may optimize
for artifacts of the training data rather than the intended alignment objective. A naïve adherence to empirical
alignment thus risks codifying and amplifying these biases in AI behavior rather than mitigating them. By
16

--- Page 17 ---

recognizing selective inference as a fundamental issue in empirical AI alignment, we advocate for more prescriptive
and transparent approaches that explicitly account for sample selection biases and ensure alignment is guided by
rationally defined objectives rather than self-reinforcing observational artifacts.
D. Additional Alternative View: Empirical Alignment as a Necessary Benchmarking Tool
We have argued against forward empirical alignment as a primary strategy. An alternative perspective holds that
empirical methods are not just unavoidable but necessary for benchmarking and validation. According to this view,
even if prescriptive alignment is theoretically preferable, it ultimately requires empirical validation to ensure it
functions as intended in real-world settings. Without empirical feedback, alignment objectives risk becoming too
abstract or detached from practical deployment concerns (Gao et al., 2022; Ding & Zou, 2021).
However, this argument presumes that empirical validation provides a neutral or reliable ground truth for
alignment, rather than a reflection of existing biases. In practice, empirical benchmarks often reinforce anthro-
pocentric limitations, locking models into human-like behaviors that may not generalize to more robust or
scalable alignment strategies, see section 3.3 and also Gabriel (2020); Perdomo et al. (2020); Wang et al. (2024b).
Instead of treating empirical evaluation as a fundamental necessity, an alternative approach would prioritize
validation through formal guarantees, logical consistency, and predictive stability, reducing dependence on
imperfect human-labeled data. This perspective suggests to walk a tightrope, balancing empirical and prescriptive
benchmarking: Rather than outright rejecting empirical methods, alignment research should redefine their role.
One can treat them as a secondary check on prescriptive models rather than as the primary mechanism for
defining alignment itself.
In this framing, the burden of proof is reversed: Instead of requiring prescriptive methods to justify themselves
empirically, empirical methods should justify their necessity in cases where prescriptive approaches provide
clear, rule-based guarantees. This would allow empirical tools to serve as a complement rather than a crutch,
making sure alignment strategies are both rigorous and adaptable.
17

--- Page 18 ---

References
Afzali, A. and Khodabandeh, B. Aligning visual contrastive learning models via preference optimization. arXiv
preprint arXiv:2411.08923, 2024. URL https://arxiv.org/pdf/2411.08923.
Aldred, J. The money pump revisited. Risk, Decision and Policy, 8(1):59–76, 2003.
Arrow, K. A difficulty in the concept of social welfare. Journal of Political Economy, 58:328–346, 1950.
Baarslag, T. and Gerding, E. H. Optimal incremental preference elicitation during negotiation. In Proceedings of
the 24th International Conference on Artificial Intelligence, IJCAI’15, pp. 3–9. AAAI Press, 2015.
Bai, Y., Jones, A., Ndousse, K., Askell, A., Chen, A., Muratore, P., Perry, J., Lin, Q., Sorensen, A., Knight, M.,
Conerly, T., et al. Training a helpful and harmless assistant with reinforcement learning from human feedback.
arXiv preprint arXiv:2204.05862, 2022a. URL https://arxiv.org/abs/2204.05862.
Bai, Y., Kadavath, S., Kundu, S., Askell, A., Kernion, J., Jones, A., Chen, A., Goldie, A., Mirhoseini, A., McKinnon,
C., et al. Constitutional ai: Harmlessness from ai feedback. arXiv preprint arXiv:2212.08073, 2022b.
Balagopalan, A., Madras, D., Yang, D. H., Hadfield-Menell, D., Hadfield, G. K., and Ghassemi, M. Judging facts,
judging norms: Training machine learning models to judge humans requires a modified approach to labeling
data. Science advances, 9(19):eabq0701, 2023.
Bayne, J. and Paul, R. Policy-based command and control. In 10th International Command and Control Research
Technology Symposium, 2005. URL http://dodccrp.org/events/10th_ICCRTS/CD/papers/360.pdf.
Bengs, V., Busa-Fekete, R., Mesaoudi-Paul, A. E., and Hüllermeier, E. Preference-based online learning with
dueling bandits: A survey. Journal of Machine Learning Research, 22(7):1–108, 2021. URL http://jmlr.org/
papers/v22/18-546.html.
Benjamini, Y. Selective Inference: The Silent Killer of Replicability. Harvard Data Science Review, 2(4), dec 16 2020.
https://hdsr.mitpress.mit.edu/pub/l39rpgyc.
Benjamini, Y. and Hochberg, Y. Controlling the false discovery rate: a practical and powerful approach to multiple
testing. Journal of the Royal Statistical Society: Series B (Methodological), 57(1):289–300, 1995.
Berk, R., Brown, L., Buja, A., Zhang, K., and Zhao, L. Valid post-selection inference. The Annals of Statistics, pp.
802–837, 2013.
Bikhchandani, S. and Segal, U. Intransitivity in the small and in the large. Journal of Risk and Uncertainty, 63(3):
257–273, 2021.
Birnbaum, M. H. and Schmidt, U. An experimental investigation of violations of transitivity in choice under
uncertainty. Journal of Risk and Uncertainty, 37:77–91, 2008.
Birnbaum, M. H., Patton, J. N., and Lott, M. K. Evidence against rank-dependent utility theories: Tests of
cumulative independence, interval independence, stochastic dominance, and transitivity. Organizational
Behavior and human decision Processes, 77(1):44–83, 1999.
Birnbaum, M. H., Navarro-Martinez, D., Ungemach, C., Stewart, N., and Quispe-Torreblanca, E. G. Risky decision
making: Testing for violations of transitivity predicted by an editing mechanism. Judgment and Decision Making,
11(1):75–91, 2016.
Bostrom, N. Observational Selection Effects in Science and Philosophy. PhD thesis, London School of Economics,
2000.
Bostrom, N. Anthropic Bias: Observation Selection Effects in Science and Philosophy. Routledge, New York, USA, 2002.
18

--- Page 19 ---

Bostrom, N. Superintelligence: Paths, strategies, dangers. Oxford University Press, Oxford, UK, 2014.
Carroll, M., Foote, D., Siththaranjan, A., Russell, S., and Dragan, A. Ai alignment with changing and influenceable
reward functions. arXiv preprint arXiv:2405.17713, 2024.
Carter, B. The anthropic principle and its implications for biological evolution. Philosophical Transactions of the
Royal Society of London. Series A, Mathematical and Physical Sciences, 310(1512):347–363, 1983.
Chatila, R. and Havens, J. C. The IEEE global initiative on ethics of autonomous and intelligent systems. Robotics
and well-being, pp. 11–16, 2019.
Christiano, P., Leike, J., Brown, T. B., Martic, M., Legg, S., and Amodei, D. Deep reinforcement learning from
human preferences, 2023. URL https://arxiv.org/abs/1706.03741.
Conitzer, V., Freedman, R., Heitzig, J., Holliday, W. H., Jacobs, B. M., Lambert, N., Mossé, M., Pacuit, E., Russell,
S., Schoelkopf, H., et al. Position: Social choice should guide ai alignment in dealing with diverse human
feedback. In Forty-first International Conference on Machine Learning, 2024.
Covert, I., Lundberg, S. M., and Lee, S.-I. Understanding global feature contributions with additive importance
measures. In Larochelle, H., Ranzato, M., Hadsell, R., Balcan, M., and Lin, H. (eds.), Advances in Neural
Information Processing Systems, volume 33, pp. 17212–17223. Curran Associates, Inc., 2020.
Crano, W. D. Primacy versus recency in retention of information and opinion change. The Journal of Social
Psychology, 101(1):87–96, 1977.
Dan, Y. Studies in Jewish thought. Praeger, 1989.
Dicke, R. H. Gravitation without a principle of equivalence. Reviews of Modern Physics, 29(3):363, 1957.
Dicke, R. H. Dirac’s cosmology and mach’s principle. Nature, 192(4801):440–441, 1961.
Dietrich, S., Rodemann, J., and Jansen, C. Semi-supervised learning guided by the generalized bayes rule under
soft revision. In International Conference on Soft Methods in Probability and Statistics, pp. 110–117. Springer, 2024.
Ding, X. and Zou, J. On the biases of standard machine learning evaluation metrics. In NeurIPS 2021, 2021.
Ding, Y., Arias, E. G., Li, M., Rodemann, J., Aßenmacher, M., Chen, D., Fan, G., Heumann, C., and Zhang, C.
Guard: Glocal uncertainty-aware robust decoding for efficient hyperparameter-free text generation. arXiv,
2025.
Early, J., Bewley, T., Evers, C., and Ramchurn, S. Non-markovian reward modelling from trajectory labels via
interpretable multiple instance learning. Advances in Neural Information Processing Systems, 35:27652–27663,
2022.
Eugster, M., Hothorn, T., and Leisch, F. Domain-based benchmark experiments: Exploratory and inferential
analysis. Austrian Journal of Statistics, 41(1):5–26, 2012.
Ewald, F. K., Bothmann, L., Wright, M. N., Bischl, B., Casalicchio, G., and König, G. A guide to feature importance
methods for scientific inference. In Longo, L., Lapuschkin, S., and Seifert, C. (eds.), Explainable Artificial
Intelligence, pp. 440–464, Cham, 2024. Springer Nature Switzerland.
Farrow, M. and Goldstein, M. Almost-pareto decision sets in imprecise utility hierarchies. Journal of Statistical
Theory and Practice, 3:137–155, 2009.
Findeis, A., Kaufmann, T., Hüllermeier, E., Albanie, S., and Mullins, R. Inverse constitutional ai: Compressing
preferences into principles. arXiv preprint arXiv:2406.06560, 2024.
Fithian, W., Sun, D., and Taylor, J. Optimal inference after model selection. arXiv preprint arXiv:1410.2597, 2014.
19

--- Page 20 ---

Forbes, M., Sap, M., Seering, J., Kim, S., Choi, Y., et al. Social chemistry 101: Learning to reason about social and
moral norms. In Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing (EMNLP),
pp. 653–670, 2020. URL https://arxiv.org/abs/2010.00672.
Freiesleben, T., König, G., Molnar, C., and Tejero-Cantero, A. Scientific inference with interpretable machine
learning: Analyzing models to learn about real-world phenomena. Minds and Machines, 34(3), July 2024. URL
http://dx.doi.org/10.1007/s11023-024-09691-z.
Fürnkranz, J. and Hüllermeier, E. Pairwise preference learning and ranking. In Lavrač, N., Gamberger, D.,
Blockeel, H., and Todorovski, L. (eds.), Machine Learning: ECML 2003, pp. 145–156. Springer, 2003.
Gabriel, I. Artificial intelligence, values, and alignment. Minds and machines, 30(3):411–437, 2020.
Gao, J. P., Durmus, E., Cho, K., and Mielke, S. J. Aligning language models to follow instructions. arXiv preprint
arXiv:2210.01264, 2022.
Garcés Arias, E., Blocher, H., Rodemann, J., Li, M., Heumann, C., and Aßenmacher, M. Towards better open-ended
text generation: A multicriteria evaluation framework. arXiv preprint arXiv:2410.18653, 2024a.
Garcés Arias, E., Rodemann, J., Li, M., Heumann, C., and Aßenmacher, M.
Adaptive contrastive search:
Uncertainty-guided decoding for open-ended text generation. In Al-Onaizan, Y., Bansal, M., and Chen,
Y.-N. (eds.), Findings of the Association for Computational Linguistics: EMNLP 2024, pp. 15060–15080, Miami,
Florida, USA, November 2024b. Association for Computational Linguistics. URL https://aclanthology.
org/2024.findings-emnlp.885/.
Garcés Arias, E., Li, M., Heumann, C., and Assenmacher, M. Decoding decoded: Understanding hyperparameter
effects in open-ended text generation. In Rambow, O., Wanner, L., Apidianaki, M., Al-Khalifa, H., Eugenio,
B. D., and Schockaert, S. (eds.), Proceedings of the 31st International Conference on Computational Linguistics,
pp. 9992–10020, Abu Dhabi, UAE, January 2025. Association for Computational Linguistics. URL https:
//aclanthology.org/2025.coling-main.668/.
Ge, Y.
The symbiosis of trust and ai: Scientific foundations for strategic network security, autonomous
resilience, and prescriptive governance, 2024.
URL https://search.proquest.com/openview/
7ff78946fb5901d4f6064a861fd598ff/1.
Giarratano, J. C. and Riley, G. Expert systems. PWS Publishing Co., 1998.
Glaese, A., McAleese, N., Laroche, J., Irving, G., Humphreys, O., Leike, J., Rauh, M., Bohg, J., Hooker, S.,
Christiano, P. F., Amodei, D., Legassick, A., Downey, C., Simonyan, K., Suleyman, M., and Hassabis, D.
Improving alignment of dialogue agents via targeted human judgements. arXiv preprint arXiv:2209.14375, 2022.
URL https://arxiv.org/abs/2209.14375.
Greenwell, B. M., Boehmke, B. C., and McCarthy, A. J. A simple and effective model-based variable importance
measure, 2018. URL https://arxiv.org/abs/1805.04755.
Grohmann, H. Statistik als Instrument der empirischen Wirtschafts- und Sozialforschung: Eine methodologische
Betrachtung aus der Sicht der Frankfurter Schule der sozialwissenschaftlichen Statistik [Statistics as an instru-
ment of empirical research in economy and society: A methodological reflection in the view of the Frankfurt
School of Statistics]. Jahrbücher für Nationalökonomie und Statistik, 220:669–688, 2000.
Groves, R. M. and Lyberg, L. Total survey error – past, presence and future. Public Opinion Quarterly, 7:849–879,
2010.
Guadalupe-Lanas, J., Cruz-Cárdenas, J., Artola-Jarrín, V., and Palacio-Fierro, A. Empirical evidence for intransi-
tivity in consumer preferences. Heliyon, 6:1–8, 2020.
20

--- Page 21 ---

Guo, D., Yang, D., Zhang, H., Song, J., Zhang, R., Xu, R., Zhu, Q., Ma, S., Wang, P., Bi, X., et al. Deepseek-r1:
Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.
Gupta, T., Shandilya, S., and Ghosh, S. Unveiling context-aware criteria in self-assessing llms. arXiv preprint
arXiv:2410.21545, 2024. URL https://arxiv.org/pdf/2410.21545.
Ha, V. and Haddaway, P. A hybrid approach to reasoning with partially elicited preference models. In Laskey, K.
and Prade, H. (eds.), Proceedings of the Fifteenth Conference on Uncertainty in Artificial Intelligence. 1999.
Harari, Y. N. Nexus: A brief history of information networks from the Stone Age to AI. Signal, 2024.
Hardt, M. and Mendler-Dünner, C. Performative prediction: Past and future. arXiv preprint arXiv:2310.16608,
2023.
Hendrycks, D., Mazeika, M., Burns, C., Basart, S., Critch, A., Song, D., and Steinhardt, J. Aligning ai with shared
human values. arXiv preprint arXiv:2008.02275, 2020. URL https://arxiv.org/abs/2008.02275.
Herrmann, M., Lange, F. J. D., Eggensperger, K., Casalicchio, G., Wever, M., Feurer, M., Rügamer, D., Hüllermeier,
E., Boulesteix, A.-L., and Bischl, B.
Position paper: Rethinking empirical research in machine learning:
Addressing epistemic and methodological challenges of experimentation. International Conference on Machine
Learning, 2024.
Horkheimer, M. and Adorno, T. W. Dialectic of Enlightenment: Philosophical Fragments. Stanford University Press,
Standford, 2002.
Huang, S. H., Bhatia, K., Abbeel, P., and Dragan, A. D. Establishing appropriate trust via critical states. CoRR,
abs/1810.08174, 2018. URL http://arxiv.org/abs/1810.08174.
Hüllermeier, E. and Waegeman, W. Aleatoric and epistemic uncertainty in machine learning: An introduction to
concepts and methods. Machine learning, 110(3):457–506, 2021.
Ibarz, B., Leike, J., Pohlen, T., Irving, G., Legg, S., and Amodei, D. Reward learning from human preferences and
demonstrations in atari. In Bengio, S., Wallach, H., Larochelle, H., Grauman, K., Cesa-Bianchi, N., and Garnett,
R. (eds.), Advances in Neural Information Processing Systems, volume 31. Curran Associates, Inc., 2018.
Jansen, C., Schollmeyer, G., and Augustin, T.
A probabilistic evaluation framework for preference aggre-
gation reflecting group homogeneity.
Mathematical Social Sciences, 96:49–62, 2018.
URL https://www.
sciencedirect.com/science/article/pii/S0165489618300660.
Jansen, C., Blocher, H., Augustin, T., and Schollmeyer, G. Information efficient learning of complexly structured
preferences: Elicitation procedures and their application to decision making under uncertainty. International
Journal of Approximate Reasoning, 144:69–91, 2022.
Jansen, C., Nalenz, M., Schollmeyer, G., and Augustin, T. Statistical comparisons of classifiers by generalized
stochastic dominance. Journal of Machine Learning Research, 24(231):1–37, 2023a. URL http://jmlr.org/
papers/v24/22-0902.html.
Jansen, C., Schollmeyer, G., and Augustin, T. Multi-target decision making under conditions of severe uncertainty.
In Torra, V. and Narukawa, Y. (eds.), Modeling Decisions for Artificial Intelligence, pp. 45–57, Cham, 2023b.
Springer Nature Switzerland.
Jansen, C., Schollmeyer, G., Blocher, H., Rodemann, J., and Augustin, T. Robust statistical comparison of random
variables with locally varying scale of measurement. In Evans, R. J. and Shpitser, I. (eds.), Proceedings of the
Thirty-Ninth Conference on Uncertainty in Artificial Intelligence, volume 216 of Proceedings of Machine Learning
Research, pp. 941–952. PMLR, 2023c.
21

--- Page 22 ---

Jansen, C., Schollmeyer, G., Rodemann, J., Blocher, H., and Augustin, T. Statistical multicriteria benchmarking
via the GSD-front. In The Thirty-eighth Annual Conference on Neural Information Processing Systems, 2024. URL
https://openreview.net/forum?id=jXxvSkb9HD.
Ji, J., Qiu, T., Chen, B., Zhang, B., Lou, H., Wang, K., Duan, Y., He, Z., Zhou, J., Zhang, Z., et al. Ai alignment: A
comprehensive survey. arXiv preprint arXiv:2310.19852, 2023.
Jiang, L. A. H., Sap, M., Choi, Y., et al. Delphi: Towards machine ethics and norms via language models.
https://delphi.allenai.org/, 2021.
Kairouz, P., McMahan, H. B., et al. Advances and open problems in federated learning. Foundations and Trends in
Machine Learning, 14(1–2):1–210, 2021.
Kaufmann, T., Ball, S., Beck, J., Hüllermeier, E., and Kreuter, F. On the challenges and practices of reinforcement
learning from real human feedback. In Joint European Conference on Machine Learning and Knowledge Discovery in
Databases, pp. 276–294. Springer, 2023.
Kim, J. and Oh, M. Queueing matching bandits with preference feedback. In The Thirty-eighth Annual Conference
on Neural Information Processing Systems, 2024. URL https://openreview.net/forum?id=0TUMAAb3of.
Kirk, H. R., Whitefield, A., Röttger, P., Bean, A., Margatina, K., Ciro, J., Mosquera, R., Bartolo, M., Williams, A.,
He, H., et al. The prism alignment project: What participatory, representative and individualised human
feedback reveals about the subjective and multicultural alignment of large language models. arXiv preprint
arXiv:2404.16019, 2024.
Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho,
T., Grabska-Barwinska, A., et al. Overcoming catastrophic forgetting in neural networks. Proceedings of the
National Academy of Sciences, 114(13):3521–3526, 2017.
Kreuter, F. (ed.). Improving surveys with paradata: Analytic uses of process information. John Wiley & Sons, 2013.
Kuhn, T. S. The structure of scientific revolutions, volume 962. University of Chicago press Chicago, 1997.
Kyrychenko, Y., Zhou, K., Bogucka, E., and Quercia, D. C3ai: Crafting and evaluating constitutions for constitu-
tional ai. In Proceedings of the ACM on Web Conference 2025, pp. 3204–3218, 2025.
König, G., Günther, E., and von Luxburg, U. Disentangling interactions and dependencies in feature attribution,
2024. URL https://arxiv.org/abs/2410.23772.
Lamm, N. Man’s position in the universe. a comparative study of the views of saadia gaon and maimonides. The
Jewish Quarterly Review, 55(3):208–234, 1965.
Lee, J. D., Sun, D. L., Sun, Y., and Taylor, J. E. Exact post-selection inference with the lasso. The Annals of Statistics,
44(3):907–927, 2016.
Li, X., Yu, Z., and Xiong, C. Montessori-instruct: Generate influential training data tailored for student learning.
arXiv preprint arXiv:2410.14208, 2024. URL https://arxiv.org/pdf/2410.14208.
Lieder, F., Griffiths, T. L., M. Huys, Q. J., and Goodman, N. D. The anchoring bias reflects rational use of cognitive
resources. Psychonomic bulletin & review, 25:322–349, 2018.
Lindauer, M., Karl, F., Klier, A., Moosbauer, J., Tornede, A., Mueller, A. C., Hutter, F., Feurer, M., and Bischl,
B. Position: A call to action for a human-centered automl paradigm. In Forty-first International Conference on
Machine Learning, 2024.
Lopez-Paz, D. and Ranzato, M. Gradient episodic memory for continual learning. In Advances in Neural Information
Processing Systems, volume 30, 2017.
22

--- Page 23 ---

Lorenz, K. Behind the Mirror. Methuen, London, 1977.
Lundberg, S. M. and Lee, S. A unified approach to interpreting model predictions. CoRR, abs/1705.07874, 2017.
URL http://arxiv.org/abs/1705.07874.
Madumal, P., Miller, T., Sonenberg, L., and Vetere, F. Explainable reinforcement learning through a causal lens.
CoRR, abs/1905.10958, 2019. URL http://arxiv.org/abs/1905.10958.
Markoff, J. In 1949, he imagined an age of robots. New York Times, 2013. URL https://shorturl.at/Zhyss.
Mendler-Dünner, C., Perdomo, J., Zrnic, T., and Hardt, M. Stochastic optimization for performative prediction.
Advances in Neural Information Processing Systems, 33:4929–4939, 2020.
Menges, G.
Die statistische Adäquation [The Statistical Adequation].
Jahrbücher für Nationalökonomie
und Statistik, 197(4):289–308, 1982.
URL http://www.degruyter.com/document/doi/10.1515/
jbnst-1982-0402/html.
Mersmann, O., Preuss, M., Trautmann, H., Bischl, B., and Weihs, C. Analyzing the BBOB results by means of
benchmarking concepts. Evolutionary Computation, 23:161–185, 2015.
Miao, F., Holmes, W., Huang, R., Zhang, H., et al. AI and education: A guidance for policymakers. Unesco Publishing,
2021.
Milani, S., Topin, N., Veloso, M., and Fang, F. A survey of explainable reinforcement learning, 2022. URL
https://arxiv.org/abs/2202.08434.
Miller, J. P., Perdomo, J. C., and Zrnic, T. Outside the echo chamber: Optimizing the performative risk. In
International Conference on Machine Learning, pp. 7710–7720. PMLR, 2021.
Mitelut, C., Smith, B., and Vamplew, P. Intent-aligned ai systems deplete human agency: the need for agency
foundations research in ai safety. arXiv preprint arXiv:2305.19223, 2023.
Molnar, C.
Interpretable Machine Learning.
2 edition, 2022.
URL https://christophm.github.io/
interpretable-ml-book.
Molnar, C., Freiesleben, T., König, G., Herbinger, J., Reisinger, T., Casalicchio, G., Wright, M. N., and Bischl, B.
Relating the partial dependence plot and permutation feature importance to the data generating process. In
Longo, L. (ed.), Explainable Artificial Intelligence, pp. 456–479, Cham, 2023. Springer Nature Switzerland.
Morgenstern, O. Wirtschaftsprognose: Eine untersuchung ihrer voraussetzungen und möglichkeiten [Eco-
nomic forecast: An examination of its assumptions and possibilities]. Wissenschaftstheorie in Ökonomie und
Wirtschaftsinformatik, Deutscher Universitäts-Verlag, Wiesbaden, pp. 171–190, 1928.
Mu, T., Helyar, A., Heidecke, J., and Achiam, J. Rule-based rewards for fine-grained llm safety. In ICML.
OpenReview, 2024.
Mukherjee, S., Lalitha, A., Kalantari, K., Deshmukh, A. A., Liu, G., Ma, Y., and Kveton, B. Optimal design for
human preference elicitation. In The Thirty-eighth Annual Conference on Neural Information Processing Systems,
2024. URL https://openreview.net/forum?id=cCGWj61Ael.
Nakano, R., Hilton, J., Balaji, S., Wu, J., Ouyang, L., Kim, C., Hashemi, M., Jiang, L., Chen, A., Haas, J., Shi, J., Iyer,
S., Goodfellow, I., Butchireddygari, S., and Sucholutsky, I. WebGPT: Browser-assisted question-answering with
human feedback. arXiv preprint arXiv:2112.09332, 2021. URL https://arxiv.org/abs/2112.09332.
Nalenz, M., Rodemann, J., and Augustin, T. Learning de-biased regression trees and forests from complex
samples. Machine Learning, 113(6):3379–3398, 2024.
23

--- Page 24 ---

Olson, M. L., Khanna, R., Neal, L., Li, F., and Wong, W.-K. Counterfactual state explanations for reinforcement
learning agents via generative deep learning. Artificial Intelligence, 295:103455, June 2021. URL http://dx.
doi.org/10.1016/j.artint.2021.103455.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., Zhang, C., Agarwal, S., Slama, K., Ray, A.,
et al. Training language models to follow instructions with human feedback. Advances in neural information
processing systems, 35:27730–27744, 2022a.
Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C. L., Mishkin, P., Zhang, C., Agarwal, S., Slama, K.,
Ray, A., Schulman, J., Hilton, J., Kelton, F., Miller, L., Simens, M., Askell, A., Welinder, P., Christiano, P.,
Leike, J., and Lowe, R. Training language models to follow instructions with human feedback, 2022b. URL
https://arxiv.org/abs/2203.02155.
Parisi, G. I., Kemker, R., Part, J. L., Kanan, C., and Wermter, S. Continual lifelong learning with neural networks:
A review. Neural Networks, 113:54–71, 2019.
Perdomo, J., Zrnic, T., Mendler-Dünner, C., and Hardt, M. Performative prediction. In International Conference on
Machine Learning, pp. 7599–7609. PMLR, 2020.
Peters, O. Time for a change: Introducing irreversible time in economics. In Talk at Gresham College, 2012.
Pillutla, K., Swayamdipta, S., Zellers, R., Thickstun, J., Welleck, S., Choi, Y., and Harchaoui, Z. Mauve: Measuring
the gap between neural text and human text using divergence frontiers, 2021. URL https://arxiv.org/
abs/2102.01454.
Popper, K. R. The Logic of Scientific Discovery. Routledge Classics, 2002/1959.
Puiutta, E. and Veith, E. M. S. P. Explainable reinforcement learning: A survey. CoRR, abs/2005.06247, 2020. URL
https://arxiv.org/abs/2005.06247.
Radford, A., Wu, J., Child, R., Luan, D., Amodei, D., and Sutskever, I. Language models are unsupervised mul-
titask learners.
https://cdn.openai.com/better-language-models/language_models_are_
unsupervised_multitask_learners.pdf, 2019. Accessed: 2025-01-27.
Rafailov, R., Sharma, A., and Mitchell, E. Direct preference optimization: Your language model is secretly a
reward model. In Advances in Neural Information Processing Systems, 2023.
Ribeiro, M. T., Singh, S., and Guestrin, C. "why should i trust you?": Explaining the predictions of any classifier,
2016. URL https://arxiv.org/abs/1602.04938.
Richardson, K., Srikumar, V., and Sabharwal, A. Understanding the logic of direct preference alignment. arXiv
preprint arXiv:2412.17696, 2024.
Rodemann, J. and Augustin, T. Accounting for imprecision of model specification in bayesian optimization. In
Poster presented at International Symposium on Imprecise Probabilities (ISIPTA), 2021.
Rodemann, J. and Augustin, T. Accounting for gaussian process imprecision in bayesian optimization. In
International Symposium on Integrated Uncertainty in Knowledge Modelling and Decision Making, pp. 92–104.
Springer, 2022.
Rodemann, J. and Augustin, T. Imprecise bayesian optimization. Knowledge-Based Systems, 300:112186, 2024.
Rodemann, J. and Bailie, J. Generalization bounds and stopping rules for learning with self-selected data. arXiv,
2025.
Rodemann, J. and Blocher, H. Partial rankings of optimizers. In The Second Tiny Papers Track at ICLR 2024, 2024.
24

--- Page 25 ---

Rodemann, J., Fischer, S., Schneider, L., Nalenz, M., and Augustin, T. Not all data are created equal: Lessons from
sampling theory for adaptive machine learning. In Poster presented at International Conference on Statistics and
Data Science (ICSDS), Institute of Mathematical Statistics (IMS), 2022.
Rodemann, J., Goschenhofer, J., Dorigatti, E., Nagler, T., and Augustin, T. Approximately bayes-optimal pseudo-
label selection. In Uncertainty in Artificial Intelligence, pp. 1762–1773. PMLR, 2023a.
Rodemann, J., Jansen, C., Schollmeyer, G., and Augustin, T. In all likelihoods: Robust selection of pseudo-labeled
data. In International Symposium on Imprecise Probability: Theories and Applications, pp. 412–425. PMLR, 2023b.
Rodemann, J., Jansen, C., and Schollmeyer, G. Reciprocal learning. Advances in Neural Information Processing
Systems, 37:1686–1724, 2025.
Schmidhuber, J. Algorithmic theories of everything. arXiv preprint quant-ph/0011122, 2000.
Schmidhuber, J. The speed prior: a new simplicity measure yielding near-optimal computable predictions. In
International conference on computational learning theory, pp. 216–228. Springer, 2002.
Schut, L., Tomasev, N., McGrath, T., Hassabis, D., Paquet, U., and Kim, B. Bridging the human-ai knowledge gap:
Concept discovery and transfer in alphazero, 2023. URL https://arxiv.org/abs/2310.16410.
Shapiro, M. B. The Limits of Orthodox Theology: Maimonides’ Thirteen Principles Reappraised. Liverpool University
Press, 2003.
Shin, H., Lee, J. K., Kim, J., and Kim, J. Continual learning with deep generative replay. In Advances in Neural
Information Processing Systems, volume 30, 2017.
Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K., and Yao, S. Reflexion: Language agents with verbal
reinforcement learning. Advances in Neural Information Processing Systems, 36, 2024.
Silver, D., Schrittwieser, J., Simonyan, K., Antonoglou, I., Huang, A., Guez, A., Hubert, T., Baker, L., Lai, M.,
Bolton, A., Chen, Y., Lillicrap, T., Hui, F., Sifre, L., van den Driessche, G., Graepel, T., and Hassabis, D.
Mastering the game of go without human knowledge. Nature, 550(7676):354–359, Oct 2017. URL https:
//doi.org/10.1038/nature24270.
Sorensen, T., Moore, J., Fisher, J., Gordon, M. L., Mireshghallah, N., Rytting, C. M., Ye, A., Jiang, L., Lu, X., Dziri,
N., et al. Position: A roadmap to pluralistic alignment. In Forty-first International Conference on Machine Learning,
2024.
Soros, G. The alchemy of finance. John Wiley & Sons, 2015.
Stiennon, N., Ouyang, L., Wu, J., Ziegler, D. M., Lowe, R. J., Voss, C., Radford, A., Amodei, D., and Christiano, P. F.
Learning to summarize with human feedback. In Advances in Neural Information Processing Systems (NeurIPS),
volume 33, pp. 3008–3021, 2020. URL https://arxiv.org/abs/2009.01325.
Su, Y. and Collier, N. Contrastive search is what you need for neural text generation, 2023. URL https:
//arxiv.org/abs/2210.14140.
Su, Y. and Xu, J. An empirical study on contrastive search and contrastive decoding for open-ended text generation,
2022. URL https://arxiv.org/abs/2211.10797.
Sun, C., Qiu, X., Xu, Y., and Huang, X. How to fine-tune bert for text classification? In Lecture Notes in Computer
Science, pp. 153–163. Springer, 2019.
Tang, W. and Xu, R. A stochastic analysis approach to conditional diffusion guidance. Columbia University Preprint,
2024. URL http://www.columbia.edu/~wt2319/CDG.pdf.
25

--- Page 26 ---

Tibshirani, R. J. and Taylor, J. Exact post-selection inference for sequential regression procedures. Journal of the
American Statistical Association, 111(514):600–620, 2016.
Topin, N. and Veloso, M. Generation of policy-level explanations for reinforcement learning. CoRR, abs/1905.12044,
2019. URL http://arxiv.org/abs/1905.12044.
Tversky, A. and Kahneman, D. Judgment under uncertainty: Heuristics and biases: Biases in judgments reveal
some heuristics of thinking under uncertainty. Science, 185(4157):1124–1131, 1974.
Wang, S., Qureshi, M. A., and Miralles-Pechuan, L. Applications of explainable ai for 6g: Technical aspects, use
cases, and research challenges. arXiv preprint, 2021. URL https://arxiv.org/pdf/2112.04698.
Wang, S., Zhang, S., Zhang, J., Hu, R., and Zhang, T. Reinforcement learning enhanced llms: A survey. arXiv
preprint arXiv:2412.10400, 2024a. URL https://arxiv.org/pdf/2412.10400.
Wang, X., Chen, Q., and Singh, S. Towards verifiable ai alignment: The case for formal guarantees. arXiv preprint
arXiv:2401.09172, 2024b.
Wasserman, L. All of statistics: a concise course in statistical inference. Springer Science & Business Media, 2009.
White, H. Maximum likelihood estimation of misspecified models. Econometrica: Journal of the econometric society,
pp. 1–25, 1982.
Wiener, N. Some moral and technical consequences of automation: As machines learn they may develop
unforeseen strategies at rates that baffle their programmers. Science, 131(3410):1355–1358, May 1960.
Wuketits, F. Evolutionary Epistemology and Its Implications for Humankind. State University of New York Press,
Albany, 1990.
Yang, Z., Liu, A., Liu, Z., Liu, K., Xiong, F., Wang, Y., Yang, Z., Hu, Q., Chen, X., Zhang, Z., et al. Position: Towards
unified alignment between agents, humans, and environment. In Forty-first International Conference on Machine
Learning, 2024.
Yin, Q. and Leong, C. Direct preference optimization using sparse feature-level constraints. arXiv preprint
arXiv:2411.07618, 2024. URL https://arxiv.org/pdf/2411.07618.
Zhang, G. and Hardt, M. Inherent trade-offs between diversity and stability in multi-task benchmarks. In
Salakhutdinov, R., Kolter, Z., Heller, K., Weller, A., Oliver, N., Scarlett, J., and Berkenkamp, F. (eds.), Proceedings
of the 41st International Conference on Machine Learning, volume 235 of Proceedings of Machine Learning Research,
pp. 58984–59002. PMLR, 2024.
Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., Dewan, C., Diab, M., Li, X., Lin, X. V., Mihaylov,
T., Ott, M., Shleifer, S., Shuster, K., Simig, D., Koura, P. S., Sridhar, A., Wang, T., and Zettlemoyer, L. Opt: Open
pre-trained transformer language models, 2022. URL https://arxiv.org/abs/2205.01068.
26

```
