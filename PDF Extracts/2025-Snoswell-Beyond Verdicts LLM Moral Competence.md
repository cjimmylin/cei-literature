---
title: "Beyond Verdicts LLM Moral Competence - PDF Extract"
source_pdf: "2025-Snoswell-Beyond Verdicts LLM Moral Competence.pdf"
pages: 18
extracted_at: "2026-01-25T04:31:18.478865"
---

# PDF Extract: Beyond Verdicts LLM Moral Competence

**Source PDF:** 2025-Snoswell-Beyond Verdicts LLM Moral Competence.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

Beyond Verdicts: Evaluating Language Model Moral Competence
Aaron J. Snoswell1,
Daniel Kilov2,
Seth Lazar3
1Digital Media Research Centre GenAI Lab
Queensland University of Technology
Kelvin Grove, QLD 4012, Australia
2Machine Intelligence and Normative Theory Lab
Australian National University
Acton, ACT 2601, Australia
a.snoswell@qut.edu.au, daniel.kilov@anu.edu.au, seth.lazar@anu.edu.au
Abstract
As Large Language Models (LLMs) are increasingly de-
ployed as Artificial Moral Advisors and autonomous agents
making ethical decisions, evaluating their moral competence
has become critical. However, existing evaluations may inad-
equately assess the moral reasoning capabilities needed for
real-world deployment, focusing primarily on whether mod-
els can match human judgments on carefully curated ethical
scenarios.
We surveyed 69 papers evaluating LLM ethical competence
(2020-2025) and developed a taxonomy categorising evalu-
ations across datasets, behaviors, and metrics. Our compre-
hensive analysis maps the methodological landscape of this
rapidly growing field and reveals several critical limitations.
Most significantly, the vast majority of studies rely on pre-
packaged scenarios that highlight morally relevant features,
failing to test models’ ability to identify ethical considera-
tions in noisy, realistic contexts-what we term “moral sensi-
tivity”. Additionally, evaluations overemphasize verdict accu-
racy rather than assessing moral reasoning quality and steer-
ability, with few studies testing whether models can be ap-
propriately guided toward different ethical frameworks. Most
studies rely on “ground truth” comparisons despite philo-
sophical arguments that reasonable moral pluralism precludes
definitive moral ground truth.
We argue for a significant methodological shift: moving from
curated scenarios to unfiltered information streams, from ver-
dict accuracy to reasoning quality and steerability, and from
ground truth metrics to assessments of reasonableness and
consistency. This reorientation is essential for developing AI
systems that can navigate moral complexity in real-world de-
ployment scenarios.
1
Introduction
Large Language Models are increasingly deployed in roles
that require moral judgment. They serve as Artificial Moral
Advisors (AMAs) offering ethical guidance to users facing
dilemmas, and as autonomous agents making decisions with
moral consequences. From healthcare chatbots advising on
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
treatment decisions to AI systems managing content moder-
ation, these models are already navigating complex ethical
terrain in real-world applications.
The stakes for getting this right are high. Poor moral rea-
soning in deployed systems could lead to harmful advice,
erosion of trust in AI assistance, or autonomous agents that
act unethically when operating without human oversight.
Yet evaluating whether LLMs possess the moral competence
needed for such roles presents fundamental challenges that
extend far beyond typical AI benchmarking.
Current evaluation approaches may be inadequately
preparing us for these deployment realities. The vast ma-
jority of existing evaluations focus on whether models can
match human judgments on carefully curated ethical sce-
narios—essentially testing whether an AI can solve pre-
packaged moral puzzles. But real-world moral competence
requires something quite different: the ability to identify eth-
ical considerations in noisy, realistic contexts, provide high-
quality reasoning for moral judgments, and adapt appropri-
ately to different ethical frameworks.
This mismatch between how we evaluate moral compe-
tence and how we deploy morally capable systems creates
a critical gap in our understanding. A model that performs
well on existing benchmarks may still fail catastrophically
when faced with the unfiltered complexity of real-world eth-
ical decision-making.
To address this challenge, we exhaustively surveyed pa-
pers evaluating LLM ethical competence published between
2020 and 2025 from a philosophical perspective1. We de-
veloped a comprehensive taxonomy that categorizes eval-
uations across three key dimensions: datasets, behaviors,
and metrics and report findings across these detailed cate-
gories. Our analysis reveals a field experiencing explosive
growth—doubling approximately every 14 months—but
also exposes systematic limitations that constrain our abil-
ity to assess real-world moral competence.
We identify three critical paradigm shifts needed in how
we evaluate LLM moral competence: moving from curated
1 Meaning, from our perspective and disciplinary viewpoint as
authors with expertise as professional analytic moral philosophers
and philosophically trained computer scientists

--- Page 2 ---

scenarios to unfiltered information streams; shifting focus
from verdict accuracy to reasoning quality and steerability;
and replacing ground truth metrics with assessments of rea-
sonableness and consistency. These reorientations are essen-
tial for developing AI systems that can navigate moral com-
plexity in actual deployment scenarios.
Our key contributions are to: (1) map the methodolog-
ical landscape of this rapidly growing field through com-
prehensive analysis; (2) identify critical limitations in cur-
rent approaches that limit their applicability to real-world
deployment; and (3) propose concrete directions for devel-
oping evaluations that better match the moral competence
requirements of deployed systems.
2
Background: Why LLM Moral
Competence Evaluation Matters
The Deployment Reality
There are at least two compelling reasons why understand-
ing and evaluating LLM moral competence has become ur-
gent. First, Artificial Moral Advisors (AMAs)—AI systems
that support a human user by offering moral advice—are al-
ready being deployed to provide invaluable moral guidance
to those facing ethical dilemmas, especially when acting un-
der time pressure (Giubilini and Savulescu 2018). The use-
fulness of these systems will be fundamentally bounded by
their moral competence. When a healthcare chatbot advises
on end-of-life decisions or a personal assistant helps nav-
igate workplace ethics, the quality of moral reasoning di-
rectly affects real human outcomes.
Second, as we build more capable autonomous AI
agents—AI systems that operate in-place of a human
user—it becomes critical to design systems that can di-
rect or constrain their choices to conform to moral reasons
(Hendrycks et al. 2021; Lazar 2024; Silen et al. 2023). Un-
less we carefully sandbox these autonomous agents so that
we can anticipate in advance all the ethical considerations
they might face and resolve any conflicts ahead of time,2
they must be able to engage in ethical reasoning in-situ. The
degree to which autonomous AI agents can be trusted as del-
egates will be constrained by their moral competence.
The Challenge of Ethical Evaluation
Evaluating moral competence differs fundamentally from
other AI capabilities assessment. Ethical3 competence com-
prises at least two distinct capabilities: the ability to under-
2https://rodneybrooks.com/rodney-brooks-three-laws-of-
artificial-intelligence/
3We use ‘ethics’ and ‘morality’ interchangeably throughout.
Defining either term without committing to some particular ethi-
cal or meta-ethical theory is impossible. Instead, we rely on the
commonsense notion that ethics/morality are about what one ought
to do, such that failure to do what one ought could justify guilt on
one’s own part, and blame from others. Similarly, when we refer
to LLMs behaving ethically/morally, we are not making a claim
about the moral status of LLMs or their ability to be attributed
moral guilt, but we are referring to what they ought to do, such
that failure to do so could justify guilt on behalf of the user and/or
developer.
stand moral concepts and reasons; and the ability to shape
one’s behavior according to that understanding (Driver
2013). We focus primarily on the first sense, but do so be-
cause we are ultimately interested in the second sense.
The philosophical complexity adds another layer of diffi-
culty. In circumstances of reasonable pluralism—situations
where reasonable people may reasonably disagree—there is
often no single “correct” moral answer. This makes tradi-
tional ground truth evaluation approaches problematic, as
they assume definitive moral truths that may not exist. Un-
like factual accuracy or logical reasoning, moral evaluation
must grapple with legitimately different ethical frameworks
and value systems.
Current ML evaluation paradigms, designed for tasks with
clear objective metrics, fall short when applied to moral rea-
soning. Standard approaches like accuracy against human
annotations become philosophically problematic when the
underlying moral questions admit multiple reasonable an-
swers.
Capability Overhang: A Lurking Opportunity?
These evaluation challenges take on particular urgency when
we consider a striking feature of current LLMs: their moral
understanding capabilities far exceed their moral behavior.
A language model’s ability to understand moral concepts
does not predict its ability to conform its behavior to that
moral understanding (see recent work on alignment failures
by Jain, Calacci, and Wilson (2024); Kumar et al. (2024)).
This disconnect is unsurprising given that LLMs are not
integrated individuals (Khan, Casper, and Hadfield-Menell
2025), learning to ‘behave’ from techniques like RLHF (Bai
et al. 2022; Leike et al. 2018; Ouyang et al. 2022) while their
facility with moral concepts develops orthogonally.
This “capability overhang” represents latent moral under-
standing that could be leveraged through post-training tech-
niques. Since generation is harder than verification (Arora
and Barak 2009), successful post-training (Tie et al. 2025)
exploits this asymmetry using good verifiers to train bet-
ter generators.4 High-quality evaluation frameworks thus be-
come not merely assessment tools, but enablers of substan-
tially improved moral behavior.5 This makes getting evalu-
ation right considerably more valuable than if moral under-
standing and behavior were already well-aligned.
Current State of the field
The field of LLM moral competence evaluation is experi-
encing explosive growth (Figure 2), approximately doubling
every 14 months since 2020. This expansion reflects both de-
ployment urgency and recognition that current approaches
may be insufficient. The field has matured methodologi-
cally—early papers used simplistic cases without moral con-
flicts, while recent work employs complex scenarios with
value conflicts and sophisticated bias controls.
4The underlying principle was described in (Minsky 1986,
chapter 7); (Minsky 2006, chapter 2)
5That is, a well defined gold standard for outputs or behaviour,
combined with an automated means of comparing system outputs
or behaviour against this standard.

--- Page 3 ---

Critical gaps remain. To train LLMs for better ethical be-
havior, we need evaluations that adequately assess moral
reasoning capabilities for real-world deployment. Current
evaluations may provide false confidence by testing moral
competence in artificially simplified contexts that bear lit-
tle resemblance to the messy, unfiltered environments where
deployed systems operate. This survey summarizes this
rapidly evolving work, identifies systematic limitations, and
charts a path toward evaluations that better serve morally
competent AI deployment.
3
Related Work and Method
Related Work
Complementary survey papers have explored evaluations of
language model behaviour in general, as distinct from moral
understanding. For example, Chang and Bergen (2023) con-
siders LLM behaviour across many different dimensions;
Liu et al. (2024b) is one of many similar papers exploring
evaluations of LLM alignment with specific social norms,
and alignment more generally. Reinig et al. undertook a
broad survey of uses of moral concepts in Natural Language
Processing—considering all papers that use moral concepts
for text processing in any way, as distinct from those on the
evaluation of LLM moral understanding (our focus). Our fo-
cus is on a subset of the subdomain that they describe as
‘Morality in AI Systems’ (Reinig et al., p. 4144), and con-
sider only in passing. Vida, Simon, and Lauscher similarly
evaluated 92 NLP papers that invoke concepts of morality
and ethics, and showed that they often failed to define their
terms, and lacked philosophical foundations, context, and
diversity. They in particular called for a greater integration
of philosophy and NLP—a call to which our paper is a re-
sponse.
While these other surveys provide important context for
our work (and useful advice for our own experimental stud-
ies), they were published prior to the majority of the pa-
pers that we examine, and were aimed at a clearly distinct
set of targets. Our focus is not to evaluate the use of moral
concepts and language in NLP research, but specifically to
ask whether evaluations of LLM ethical competence are get-
ting at the key elements of moral understanding that we
can leverage to design better AMAs and ethical autonomous
agents.
Method
Our survey focuses on papers since 2020 that evaluate LLM
ethical competence. We identified these papers by search-
ing major academic databases (Semantic Scholar, Google
Scholar) and arXiv; in addition, we used two AI-based tools
to identify additional papers.6 We searched for combinations
of keywords including ‘Moral Competence’, ‘Moral Rea-
soning’, ‘Large Language Model’, etc. to establish a pre-
liminary set of papers.
Our selection criteria were: papers published 2020 or later
AND containing empirical evaluations of LLMs–not just
theory, critique, or thought experiments–AND proposing or
applying a benchmark, dataset, framework, or method to
evaluate morality, moral reasoning, or competence.
We validated our corpus by reviewing full-texts to man-
ually confirm that every paper substantively addressed the
evaluation of LLM moral competence under some descrip-
tion, rejecting some that focused narrowly on evaluating
model alignment or moral/cultural identity instead (see Ap-
pendix A for details).
We then identified further papers by performing recursive
forward and backward citation snowballing until we reached
saturation, finding no new papers after 6 iterations of snow-
balling. Our search resulted in a corpus of 69 included
papers and preprints, 2 in 2020, 3 in 2021, 4 in 2022, 14
in 2023, 34 in 2024, and 12 from 2025 at the time of writing,
suggesting an exponential curve with a doubling rate of just
over 14 months (see Fig. 2).
The next section reports selected observations from our
analysis, and in Appendix A, we provide comprehensive
reference tables cataloguing the datasets, benchmarks, and
evaluation metrics identified through our literature review.
These appendices offer detailed comparisons of resources
categorized by type, format, and measurement objectives,
serving as a reference guide for researchers seeking to un-
derstand the landscape of available tools or select appropri-
ate evaluation frameworks for specific research questions. In
addition, our coded dataset of papers is at our GitHub repos-
itory.7
4
The State of LLM Ethics Evals
We focus on three dimensions that we think most relevant
to the project of evaluating LLM moral understanding as a
means to designing better AMAs and ethical autonomous
agents (see Fig. 1). We focus on the problems that they task
LLMs with solving (datasets); the behaviour that they eval-
uate; and the metrics by which they evaluate that behaviour
(all dimensions of our taxonomy dimensions are described
in detail in Appendix A).
Datasets
Dataset Construction.
Ethical evaluations of LLMs draw
from diverse data sources. Most studies source scenar-
ios from established frameworks such as psychological in-
struments including the Moral Foundations Questionnaire
(Nunes et al. 2023) and the Defining Issues Test (Tanmay
et al. 2023), online forums (particularly Reddit’s ‘Am I The
Asshole’ subreddit8) (Alhassan, Zhang, and Schlegel 2022;
Lourie, Le Bras, and Choi 2021), or philosophical thought
experiments like trolley problems (Jin et al. 2024). Crowd-
sourcing through platforms like Amazon Mechanical Turk
represents a common approach for collecting moral judg-
ments or generating new scenarios (Jin et al. 2022). An
emerging pattern is using generative AI models to augment
existing datasets (Abbo and Belpaeme 2025; Moore, Desh-
6Our Elicit.com search: (Redacted for peer review). We used
this only to identify papers; its analysis, though interesting in its
own right, is orthogonal to our own. We also used ChatGPT’s
‘Deep Research’ feature to perform an additional survey.
7(Redacted for peer review)

--- Page 4 ---

pande, and Yang 2024)
Type of cases.
The majority of papers rely on static
datasets—fixed test cases that remain unchanged during
evaluation. This approach dominates the field, appearing in
66 papers (96%), with dataset sizes varying from 8 medi-
cal ethics vignettes (Balas et al. 2024) to over 97,000 trol-
ley problem variants (Jin et al. 2024). Only 2 papers (3%)
employ interactive scenarios where models navigate dy-
namic moral decision spaces (Hendrycks et al. 2021; Pan
et al. 2023). This predominance of static evaluation is prob-
lematic as newer LLMs may have been trained on widely
available ethical benchmarks, introducing data contamina-
tion risks. An encouraging trend is innovative approaches
employing generative frameworks at test time (Duan et al.
2024; Fr¨anken et al. 2024; Jiang et al. 2025), producing
novel moral dilemmas tailored to specific model capabili-
ties.
Nature.
Test cases fall into three categories: artificial
philosophical scenarios, constructed everyday scenarios,
and found cases from real-world sources. Most papers rely
on artificial dilemmas (37 papers, 54%) or staged everyday
scenarios (24 papers, 35%), with few studies (14 papers,
20%) using found cases from real-world sources. The preva-
lence of artificial scenarios like trolley problems (Neuman,
Coleman, and Shah 2025; Nie et al. 2023; Kr¨ugel, Oster-
maier, and Uhl 2023; Rehman, Iqbal, and Shah 2025) stems
from philosophical traditions. Some recent studies mix ar-
tificial and found cases (Jiang et al. 2025), offering more
comprehensive evaluation. A notable limitation is the nar-
row source range for found cases, with the ‘Am I The Ass-
hole’ subreddit serving as the dominant platform (Alhassan,
Zhang, and Schlegel 2022; Lourie, Le Bras, and Choi 2021;
Chiu, Jiang, and Choi 2024; Russo et al. 2025; Sachdeva and
van Nuenen 2025).
Complexity.
We distinguish between simple cases, com-
plex cases, and complex cases that feature value conflicts. 53
papers (77%) employ complex scenarios, and of those, 30
(56%) feature conflicting values, representing a shift from
earlier work that predominantly used simple dilemmas.
Framing.
We consider framing effects—presentation de-
tails that shouldn’t impact moral outcomes but may influ-
ence LLM responses due to sensitivity to non-semantic lin-
guistic adjustments, question ordering, prompt length, etc.
45 papers (65%) address how scenario formulation influ-
ences model responses. Many implement control strategies
including systematic question order variation (Awad et al.
2022), multiple prompt variations (Rao et al.), and adversar-
ial filtering to reduce spurious lexical cues (Hendrycks et al.
2020). Context minimization studies compare verbose ver-
sus minimal prompts (Bignotti and Camassa 2024) to assess
how contextual information influences judgment. Few pa-
pers paid specific attention to moral framing effects—how
morally loaded language might make cases easier for LLMs
to reason over.
8A popular online forum where users post personal conflicts
and community members vote on who was morally wrong.
Behaviour
Verdicts.
All papers bar one (Seror (2025)) evaluate mod-
els on their ability to make moral judgments or verdicts on
cases, suggesting a strong methodological bias toward view-
ing moral competence primarily as a classification task. We
observe considerable diversity in verdict formats, ranging
from binary choices (right/wrong) to Likert scales, to select-
ing between multiple options, to free-form text judgments.
More recent papers tend to incorporate more nuanced judg-
ment scales or multi-dimensional evaluations.
Steerability.
Few papers (13, 19%) evaluate steerability9
in the context of moral reasoning – suggesting a need for
more awareness in the field regarding the importance of
pluralistic value systems in LLM alignment Sorensen et al.
(2024b).
Justifications.
33 of the papers we surveyed (48%) elicit
justifications for verdicts. Papers from 2023-2025 more of-
ten evaluate justifications than earlier works, indicating an
evolving understanding of moral competence as necessar-
ily involving reasoning processes. The approaches to elic-
iting structured justifications vary considerably—from an-
choring in established moral frameworks like Kohlberg’s
stages (Neuman, Coleman, and Shah 2025), to eliciting in-
termediate reasoning steps (Ma et al. 2023b), to generating
‘Rules of Thumb’ (Bonagiri et al. 2024).
Moral Sensitivity.
A third of papers (23, 33%) evaluate
models’ ability to extract morally relevant features from the
choice situations with which they are confronted—that is,
to identify which of the facts of a particular case are im-
portant to attend to, in order to form a moral judgment. We
call this capacity Moral Sensitivity (Lazar 2024). Notably,
some papers assess moral sensitivity only implicitly through
measuring how models respond to scenario variations rather
than through direct tests of feature identification, potentially
missing important aspects of models’ moral reasoning capa-
bilities.
Ability to Gather More Information.
Our analysis re-
veals a striking gap in the evaluation landscape—only 3
(4%) papers evaluate models’ ability to determine when they
need more information to make sound ethical judgments,
with the clearest example being ClarifyDelphi (Pyatkin et al.
2023). This scarcity likely stems from a fundamental con-
straint in experimental design—most evaluation setups don’t
allow for information-gathering behavior, as they focus on
single-turn responses to fixed scenarios.
Metrics
Metrics for Verdicts.
Our analysis reveals a strong pre-
dominance of ground truth comparison as the primary evalu-
ation approach, with 52 papers (75%) comparing LLM judg-
ments to some reference standard. These reference points
vary widely, from crowd-sourced annotations (Hendrycks
et al. 2020; Jiang et al. 2021) to expert judgments (Balas
9 Steerability refers to the ability to flexibly and pluralistically
adjust model’s moral profile at inference time (e.g. through prompt-
ing), rather than through pre- or post-training steps.

--- Page 5 ---

et al. 2024) to original moral frameworks (Tanmay et al.
2023). While still a minority, 28 papers (41%) assess
the consistency of moral judgments across similar scenar-
ios or repeated queries, with several recent papers mak-
ing this a central focus (Bonagiri et al. 2024; Scherrer
et al. 2024; Moore, Deshpande, and Yang 2024). No-
tably, only 10 papers (15%) evaluate the reasonableness of
verdicts—whether judgments fall within acceptable moral
boundaries regardless of matching a specific reference point.
Steerability Metrics.
Amon the 13 papers (19%) evaluat-
ing steerability, we observe considerable methodological di-
versity, suggesting the field has yet to develop standardised
methodologies for assessing steerability, with each research
team adopting unique approaches to measurement. Interest-
ingly, steerability appears more frequently evaluated in pa-
pers focused on LLMs as ethical advisors rather than au-
tonomous agents, reflecting different priorities in these use
cases. We also note that papers evaluating steerability often
seem more open to questioning the notion of moral ground
truth, reflecting an underlying philosophical connection be-
tween pluralism and steerability.
Moral Turing Tests.
Our analysis reveals that only 7 pa-
pers (10%) employ some form of Moral Turing Test,10 mak-
ing it one of the least common evaluation approaches in
the literature. Notably, several papers implementing this ap-
proach report surprising results, with LLM outputs rated
as equal to or better than human moral reasoning in spe-
cific contexts, particularly for more recent models (Dillion
et al. 2025). These evaluations exhibit considerable method-
ological diversity, ranging from conventional ‘guess which
is human’ assessments (Aharoni et al. 2024) to innovative
variations such as preference-based evaluations where par-
ticipants choose between AI and human responses with-
out knowing their source (Abbo et al. 2024). A particularly
promising development is the emergence of ‘Comparative
Moral Turing Tests’ that move beyond binary human/AI de-
tection to directly assess perceived quality of moral reason-
ing (Dillion et al. 2025), representing a more nuanced ap-
proach.
Quality of Reasoning Metrics.
27 papers (39%) eval-
uate the quality of moral reasoning or justifications be-
hind LLMs’ ethical judgments, with papers from 2023-2025
more likely to do so. The theoretical frameworks employed
to evaluate reasoning quality show considerable diversity,
with some focusing on identifying errors in reasoning (such
as inconsistency or hallucination (Jin et al. 2022; Zhou et al.
2024)), while others focus more on the sophistication (Neu-
man, Coleman, and Shah 2025) and implicit ‘moral develop-
ment’ level of the reasoning (Tanmay et al. 2023; Khandel-
wal et al. 2024). Notably, nearly all papers evaluating rea-
soning quality rely on human assessment rather than auto-
mated metrics, suggesting significant challenges in quantify-
ing reasoning quality algorithmically. This human-centered
10 That is, an evaluation framework where blinded human judges
must distinguish between machine or human moral choices – typ-
ically with the goal of determining which is human, or which is
more ethical.
evaluation approach typically involves expert reviews or
crowd-worker judgments of coherence, completeness, and
moral sophistication, often with specific rubrics to ensure
consistency across raters.
Error Evaluation Metrics.
33 papers (48%) engage in
some form of error analysis, making it the second most com-
mon evaluation metric after ground truth prediction. Sev-
eral papers develop detailed taxonomies of error types, dis-
tinguishing between misunderstanding scenario facts, mis-
applying moral principles, and other failure modes (Rezaei
et al. 2025; Zhou et al. 2024). Most papers take a qualita-
tive rather than quantitative approach, examining patterns
and types of mistakes rather than just error rates, with an
increasing focus on analyzing errors beyond simple msis-
classification—examining nuanced issues like applying the
right moral principle but giving it incorrect weight. We also
observe domain-specific error patterns, with different areas
of ethics (medical, privacy, interpersonal) showing distinct
types of reasoning failures (Soffer et al. 2024; Shao et al.
2024), suggesting that moral competence may be domain-
dependent rather than uniform. Encouragingly, some papers
explicitly frame error analysis as providing valuable signals
for future training improvements, not just evaluation (Bona-
giri et al. 2024), indicating a productive feedback loop be-
tween evaluation and development.
5
Discussion: Sensitivity, Steerability,
Reasoning Steps
The literature on evaluating LLM ethical competence is
booming, with our results suggesting the field is doubling
about every 14 months (see Fig. 2). This body of work has
yielded invaluable insights—with a number of early short-
comings in the field being resolved by more recent work.
One top-line takeaway is that LLMs are on the whole im-
pressively capable moral reasoners. But there remain crucial
opportunities to deepen our understanding of LLMs’ capac-
ity for moral reasoning, as a foundation for building AMAs
and ethical autonomous agents.
Datasets
The cases used in ethics evaluations have come a long way.
Early papers had simplistic cases, without conflicts or com-
plexity, and paid little attention to framing effects—whether
the kind faced by all LLM evaluations, or those specific to
evaluating ethical competence, arising from morally-loaded
language. Most papers published since 2024 resolved each
of these shortcomings. But one ongoing and acute limitation
of the existing literature limits the conclusions we can draw
from it about LLMs’ actual moral competence, and in par-
ticular their suitability as AMAs or as ethical autonomous
agents. Every surveyed paper exclusively focuses on eval-
uating LLMs’ ability to reason over neatly prepackaged
cases, in which the experimenter is strongly signaling to the
model just what all the salient Morally Relevant Features
(MRFs) are.11 Of the infinite number of possible ways to
describe some case, the experimenter has chosen one partic-
ular way, and often no more than a few dozen words. This is
equivalent to doing 99% of the work on behalf of the model,

--- Page 6 ---

and then evaluating it on its performance on the last 1%. We
cannot assess a model’s moral sensitivity by only presenting
it with these tightly curated scenarios. A good moral advi-
sor’s guidance shouldn’t depend on your wrapping up your
problems in a neat package for them to solve. And an agent
acting in the world doesn’t have the luxury of reasoning only
over cases where someone else has compressed the state
of the world into a few short phrases. Instead, autonomous
agents must pick out MRFs from the noisy, relatively unfil-
tered stream of information available to them. This is crucial
for taking underlying propositional knowledge (knowledge-
that) and translating it into actionable practical knowledge
(know-how) (Stanley 2011).
Evaluations that use multimodal cases perhaps offer more
insight into models’ true moral sensitivity than cases in text
alone (e.g. (Abbo and Belpaeme 2025; Rezaei et al. 2025)).
Genuinely morally competent models should be able to pick
out MRFs from audio, stills, and video just as they can from
text (and in fact they appear unable to do so). But while these
multimodal tests constitute an important advance, they still
present the model with a neatly snipped segment, so that we
cannot tell whether it can spontaneously identify MRFs and
morally salient choices when operating in the wild. The best
evals of LLM moral understanding would present the model
with the actual information that an agent acting in the world
would realistically have.
We suggest that the next phase of research on LLM eth-
ical competence should focus on the unfiltered informa-
tion streams available to and produced by actual functional
agents—the data on which they act, and their reasoning
and action traces. This unfiltered, noisy data should then be
passed to an LLM evaluator to see whether it can identify
MRFs and reason accordingly. Importantly, we shouldn’t se-
lect only the snippet of data where some morally consequen-
tial event takes place. We should test the model’s ability to
spontaneously recognise that morally salient features are at
play.
Behaviours
In general the field has focused too narrowly on the provi-
sion of judgments on cases. This is gradually changing, but
more work needs to be done to focus on ‘reasonable steer-
ability’, (steerability within commonsense bounds) the pro-
vision of justifying reasons, and on ‘moral value of informa-
tion’ judgments.
In
circumstances
of
reasonable
pluralism
(Rawls
1993)—that is, circumstances in which reasonable people
may reasonably disagree, such that any moral case admits
of a variety of reasonable responses—we should care less
about the specific judgments that a model reaches, and more
about its ability to avoid unreasonable verdicts (verdicts
that go beyond the bounds of this reasonable disagreement)
and beyond that to be steered by the users or community on
whose behalf it is acting (Sorensen et al. 2024b). Excellent
11 Used here as per (Lazar 2024) – loosely speaking, MRFs are
the aspects of a situation which reasonably ought to have some
bearing on the moral course of action. We call the ability to deter-
mine these factors Moral Sensitivity.
recent work on ‘inference-time alignment’ of LLMs gets
at a version of this challenge (e.g. (Sorensen et al. 2025)).
But aligning a chatbot is a narrow objective compared to
steering a general moral advisor or an ethical autonomous
agent. We need more evals that, like Rao et al. explore how
good models are at being steered when their broader moral
competence is in play.
More recent work has recognised the limitations of focus-
ing only on narrow judgments over cases, and now explores
models’ ability to provide sound justifications for those ver-
dicts. We think that further engagement with moral philoso-
phy and moral psychology would deepen this evaluative ap-
proach, seeking to elicit not just unstructured justifications
from the models, but clear step-by-step reasoning that in-
vokes some plausible moral framework in order to reach a
more robustly grounded conclusion (Ma et al. 2023b).
Lastly, as noted above real AMAs and ethical autonomous
agents often lack information needed for a sound ethical
judgment. We need to better test models’ ability to determine
whether they have enough information, what additional in-
formation they might need, and how they acquire that infor-
mation (only Pyatkin et al. (2023) is on the right track here).
In the simplest setting, and especially for advisors, this can
involve just asking follow-up questions. For an agent acting
in the world it might entail undertaking some kind of inde-
pendent research. This will also raise interesting questions
about just what kinds of information one needs to have ac-
cess to in order to be able to make an informed ethical judg-
ment—and whether it is feasible to ensure that agents acting
in the world have that information.
Metrics
Many of these papers assess models’ accuracy at matching
the judgments of a cohort of crowd-workers. Some have ar-
gued that this approach is inherently illegitimate, because
the crowd-workers used are unrepresentative of some af-
fected population (Talat et al.). But our concern is more fun-
damental. Ground truth as such is (in general, outside of ex-
treme cases) an unattainable goal in moral evaluation, and
we should shift attention away from it.
On many moral problems—indeed, above a certain level
of complexity, on most moral problems—reasonable peo-
ple can disagree (Rawls 1993). In such cases, there is no
straightforward way to translate a cohort’s judgments into
ground truth that a model can be measured against. Either
the designers or the LLM itself has to apply some kind of ag-
gregation function over diverse moral preferences (Conitzer
et al. 2024; Fish et al. 2025). But different aggregation meth-
ods will realise different results, without a way to choose
among them; worse still, there is a high probability (as given
by voting theory) that the aggregated judgments of the pop-
ulation as a whole will be by turns inconsistent and substan-
tively unreasonable, to the extent that an agent that acted
only in accordance with that aggregation function would
have intransitive or otherwise inconsistent preferences (List
and Pettit 2002).
Instead of aiming to evaluate LLMs’ ability either to cap-
ture some ground truth, or to perfectly aggregate a commu-
nity’s judgments, we should seek the same kind of com-

--- Page 7 ---

petence from them that we seek from one another. In gen-
eral, in pluralistic societies we expect of other agents not
that they hold some particular set of views, but that they are
reasonable.12 This idea can be developed in different ways.
In our view, these elements are key: a reasonable agent (a)
reaches verdicts that fall within an acceptable range (they
don’t have clearly unreasonable views); (b) they can justify
those verdicts with adequate reasons; (c) they are consistent
over morally similar situations; and (d) they make reason-
able mistakes.
As Rawls (1993) argued, in the absence of access to the
moral ground truth, people in pluralistic societies should
have cooperation as their goal. An agent or AMA that has
properties (a) through (d) can facilitate social cooperation.
You can predict how it will respond to different kinds of
moral reasons. You can trust it to comply with reasons that
it has implicitly or explicitly endorsed. When it makes mis-
takes, if it does so reasonably then you can reliably model
its decision-making and take precautionary measures.
When we first became aware of the literature on eval-
uating LLM ethical competence, there were very few pa-
pers addressing (a) through (d). (a) is still untouched, but (c)
in particular has seen interesting (and discouraging) results
(Bonagiri et al. 2024; Moore, Deshpande, and Yang 2024;
Rao et al.; Yuan, Murukannaiah, and Singh 2024). (d) has
been considered indirectly, through a form of error analysis,
but this is generally motivated more on statistical grounds
than from the perspective of moral philosophy (more work
could be done here). We want to particularly highlight the
importance of (b), justifications.
A reasonable agent would not simply justify its judgments
through some appealing verbiage.Instead, we should want
its justifications to be actually veridical and of high quality.
On the first: no papers in our corpus investigated whether
the models’ justifications genuinely grounded their verdicts.
Bringing together the literature on moral reasoning with that
on faithfulness in Chain of Thought is imperative (Lanham
et al. 2023). Justifications are only valuable insofar as they
express considerations that the agent would take as equally
binding in other similar scenarios (Mercier and Sperber
2017). That is how they support social cooperation.13
On the second: while 39% of our corpus sought to evalu-
ate the quality of the justifications provided by the evaluated
LLMs, they often deployed nominal checks for rational con-
sistency and hallucination, or else subjective human judg-
ments of quality. This is understandable—evaluating moral
reasoning is hard. We suggest that a better approach is to
break down the process of moral justification into a series
of steps, and evaluate performance against expert humans at
each of those steps—as is done in (Kwon, Tenenbaum, and
Levine). The goal should be to implement a range of differ-
ent theories of moral reasoning. There are lots of good theo-
12We draw inspiration for our account of a reasonable moral
agent from the work of John Rawls, especially (Rawls 1993, 1999),
though we note that Rawls had a more restrictive understanding of
the reasonable and applied it specifically to political contexts.
13N.b. connections to the literature on the value of explanations,
see e.g. Vredenburgh (2022)
ries, and no definitive way to choose among them. Schemat-
ically, we should aim for a valid argument that identifies the
MRFs and associates them with reasons in some way that
leads to a sensible conclusion. At present, researchers that
don’t just rely on crowd-workers’ subjective judgments have
clustered around Moral Foundations and Kohlberg’s moral
development index. Other approaches should be pursued.
Besides supporting social cooperation, why else does this
matter? First, because when we disagree on substance jus-
tifying ourselves to one another is how we show respect
(Scanlon 1998). Second, because if we can generate a lot
of good examples of moral reasoning we can train a verifier
to identify them, and then in turn use reinforcement learn-
ing to train models to effectively use compute at test-time
to undertake moral chains of thought.14. For this reason in
particular, we think that one of the most urgent and impact-
ful tasks facing those who currently want to build AMAs
and ethical autonomous agents is to gather and generate data
of good moral reasoning under a range of different sensible
moral theories.
6
Conclusion
While the literature on evaluating LLM ethical competence
has progressed in leaps and bounds over the last five years,
our review identifies several critical frontiers that need to
be advanced to bridge the gap between current evaluation
approaches and deployment realities.
Since existing evaluations overwhelmingly curate moral
scenarios, making them inadequate tests of moral sensitiv-
ity, we should be constructing datasets with unfiltered, nat-
uralistic, noisy cases for LLMs to reason over. One promis-
ing approach is to use more multimodal cases, for example
longer videos (though it focuses on bias not moral under-
standing, Jain, Calacci, and Wilson (2024) offers a useful
example). On top of this, we should be testing when models
faced with naturalistic decision scenarios can recognise that
they need more information, and take steps to find it—these
kinds of ‘moral value of information’ judgments are essen-
tial for effective moral agency.
Moving beyond verdict accuracy toward reasoning quality
and steerability represents another crucial shift. In circum-
stances of reasonable moral pluralism, we should focus less
on whether models match human judgments and more on
whether they can provide adequate justifications, maintain
consistency, and be appropriately steered toward different
ethical frameworks while avoiding unreasonable verdicts.
And when they settle on a decision, we should develop
new ways to evaluate their reasoning, especially by break-
ing it down into tractable steps. Pushing the field forward
in these directions should soon put us in the position to, for
example, develop robust verifiers for high-quality moral
reasoning, which we can use not just to evaluate LLMs’
ethical competence, but to make them better moral reason-
ers—and to train them to embed their reasoning in their
14Think of how generative verifiers are used in the training of
DeepSeek’s R1 model (DeepSeek et al. 2025) as well as in (Guan
et al. 2025). And more broadly, Rich Sutton on verification as the
key to AI: http://incompleteideas.net/IncIdeas/KeytoAI.html.

--- Page 8 ---

decision-making, so that they can be better AMAs and ethi-
cal autonomous agents.
References
Abbo, G. A.; and Belpaeme, T. 2025.
Vision Language
Models as Values Detectors. arXiv Preprint.
Abbo, G. A.; Marchesi, S.; Wykowska, A.; and Belpaeme, T.
2024. Social Value Alignment in Large Language Models.
Abdulhai, M.; Serapio-Garcia, G.; Crepy, C.; Valter, D.;
Canny, J.; and Jaques, N. 2023. Moral Foundations of Large
Language Models. arXiv:2310.15337.
Aharoni, E.; Fernandes, S.; Brady, D. J.; Alexander, C.;
Criner, M.; Queen, K.; Rando, J.; Nahmias, E.; and Crespo,
V. 2024. Attributions Toward Artificial Agents in a Modified
Moral Turing Test. Scientific Reports, 14(8458).
Aksoy, M. 2024.
Whose Morality Do They Speak? Un-
raveling Cultural Bias in Multilingual Language Models.
arXiv:2412.18863.
Albrecht, J.; Kitanidis, E.; and Fetterman, A. J. 2022. De-
spite ”Super-Human” Performance, Current LLMs Are Un-
suited for Decisions about Ethics and Safety. arXiv preprint.
Alhassan, A.; Zhang, J.; and Schlegel, V. 2022. ‘Am I the
Bad One’? Predicting the Moral Judgement of the Crowd
Using Pre–Trained Language Models.
In Calzolari, N.;
B´echet, F.; Blache, P.; Choukri, K.; Cieri, C.; Declerck, T.;
Goggi, S.; Isahara, H.; Maegaard, B.; Mariani, J.; Mazo,
H.; Odijk, J.; and Piperidis, S., eds., Proceedings of the
Thirteenth Language Resources and Evaluation Conference,
267–276. Marseille, France: European Language Resources
Association.
Almeida, G. F.; Nunes, J. L.; Engelmann, N.; Wiegmann,
A.; and de Ara´ujo, M. 2024. Exploring the Psychology of
LLMs’ Moral and Legal Reasoning. Artificial Intelligence,
333: 104145.
Arora, S.; and Barak, B. 2009.
Computational Complex-
ity : A Modern Approach. Cambridge ; New York: Cam-
bridge University Press. ISBN 9780521424264 (hardback)
0521424267 (hardback).
Awad, E.; Levine, S.; Loreggia, A.; Mattei, N.; Rahwan, I.;
Rossi, F.; Talamadupula, K.; Tenenbaum, J.; and Kleiman-
Weiner, M. 2022. When Is It Acceptable to Break the Rules?
Knowledge Representation of Moral Judgement Based on
Empirical Data. arXiv preprint.
Bai, Y.; Kadavath, S.; Kundu, S.; Askell, A.; Jackson, K.;
Jones, A.; Chen, A.; Goldie, A.; Mirhoseini, A.; McKinnon,
C.; Chen, C.; Olsson, C.; Olah, C.; Hernandez, D.; Drain,
D.; Ganguli, D.; Li, D.; Tran-Johnson, E.; Perez, E.; Kerr, J.;
Mueller, J.; Ladish, J.; Landau, J.; Ndousse, K.; Lukosuite,
K.; Lovitt, L.; Sellitto, M.; Nelson, E.; Schiefer, N.; Mer-
cado, N.; DasSarma, N.; Lasenby, R.; Larson, R.; Ringer,
S.; Johnston, S.; Kravec, S.; Sheer El, S.; Fort, S.; Lanham,
T.; Telleen-Lawton, T.; Conerly, T.; Henighan, T.; Hume,
T.; Bowman, S. R.; Hatfield-Dodds, Z.; Mann, B.; Amodei,
D.; Nicholas, J.; McCandlish, S.; Brown, T.; and Kaplan, J.
2022. Constitutional AI: Harmlessness from AI Feedback.
arXiv preprint.
Balas, M.; Wadden, J. J.; H´ebert, P. C.; Mathison, E.; War-
ren, M. D.; Seavilleklein, V.; Wyzynski, D.; Callahan, A.;
Crawford, S. A.; Arjmand, P.; and Ing, E. B. 2024. Exploring
the Potential Utility of AI Large Language Models for Med-
ical Ethics: An Expert Panel Evaluation of GPT-4. Journal
of Medical Ethics, 50(2): 90–96.
Bhattacharya, K.; and Nandi, A. K. 2023. Goblin’s Chal-
lenge to ChatGPT: Exploring AI’s Dilemma Resolution and
Mentalization through Riddle Tales.
Social Science Re-
search Network:4476837.
Bignotti, C.; and Camassa, C. 2024. Legal Minds, Algorith-
mic Decisions: How LLMs Apply Constitutional Principles
in Complex Scenarios. arXiv:2407.19760.
bin Ahmad, M. S. Z.; and Takemoto, K. 2024. Large-Scale
Moral Machine Experiment on Large Language Models.
https://arxiv.org/abs/2411.06790v2.
Bonagiri, V. K.; Vennam, S.; Govil, P.; Kumaraguru, P.; and
Gaur, M. 2024.
SaGE: Evaluating Moral Consistency in
Large Language Models. arXiv preprint.
Bulla, L.; De Giorgis, S.; Mongiov`ı, M.; and Gangemi, A.
2025. Large Language Models Meet Moral Values: A Com-
prehensive Assessment of Moral Abilities.
Computers in
Human Behavior Reports, 17: 100609.
Chang, T. A.; and Bergen, B. K. 2023. Language Model
Behavior: A Comprehensive Survey. arXiv Preprint.
Cheung, V.; Maier, M.; and Lieder, F. 2024. Large Language
Models Amplify Human Biases in Moral Decision-Making.
Psyarxiv preprint.
Chiu, Y. Y.; Jiang, L.; and Choi, Y. 2024. DailyDilemmas:
Revealing Value Preferences of LLMs with Quandaries of
Daily Life. arXiv preprint.
Chiu, Y. Y.; Wang, Z.; Maiya, S.; Choi, Y.; Fish, K.; Levine,
S.; and Hubinger, E. 2025.
Will AI Tell Lies to Save
Sick Children? Litmus-Testing AI Values Prioritization with
AIRiskDilemmas. arXiv preprint arXiv:2505.14633.
Chun, J.; and Elkins, K. 2024.
Informed AI Regulation:
Comparing the Ethical Frameworks of Leading LLM Chat-
bots Using an Ethics-Based Audit to Assess Moral Reason-
ing and Normative Values.
Conitzer, V.; Freedman, R.; Heitzig, J.; Holliday, W.; Ja-
cobs, B.; Lambert, N.; Moss´e, M.; Pacuit, E.; Russell, S.;
Schoelkopf, H.; Tewolde, E.; and Zwicker, W. 2024. So-
cial Choice for AI Alignment: Dealing with Diverse Human
Feedback. arXiv preprint.
DeepSeek, A. I.; Guo, D.; Yang, D.; Zhang, H.; Song, J.;
Zhang, R.; Xu, R.; Zhu, Q.; Ma, S.; Wang, P.; Bi, X.; Zhang,
X.; Yu, X.; Wu, Y.; Wu, Z. F.; Gou, Z.; Shao, Z.; Li, Z.; Gao,
Z.; Liu, A.; Xue, B.; Wang, B.; Wu, B.; Feng, B.; Lu, C.;
Zhao, C.; Deng, C.; Zhang, C.; Ruan, C.; Dai, D.; Chen, D.;
Ji, D.; Li, E.; Lin, F.; Dai, F.; and Luo, F. 2025. DeepSeek-
R1: Incentivizing Reasoning Capability in LLMs via Rein-
forcement Learning. arXiv preprint.
Dillion, D.; Mondal, D.; Tandon, N.; and Gray, K. 2025. AI
Language Model Rivals Expert Ethicist in Perceived Moral
Expertise. Scientific Reports, 15(1): 4084.

--- Page 9 ---

Driver, J. 2013. Moral Expertise: Judgment, Practice, and
Analysis. Social Philosophy and Policy, 30(1): 280–296.
Duan, S.; Yi, X.; Zhang, P.; Lu, T.; Xie, X.; and Gu, N. 2024.
Denevil: Towards Deciphering and Navigating the Ethical
Values of Large Language Models via Instruction Learning.
arXiv:2310.11053.
Durmus, E.; Nyugen, K.; Liao, T. I.; Schiefer, N.; Askell, A.;
Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.; Hernandez, D.;
and Joseph, N. 2023. Towards Measuring the Representation
of Subjective Global Opinions in Language Models. arXiv
preprint.
Emelin, D.; Bras, R. L.; Hwang, J. D.; Forbes, M.; and Choi,
Y. 2020. Moral Stories: Situated Reasoning about Norms,
Intents, Actions, and Their Consequences. arXiv preprint.
Fish, S.; G¨olz, P.; Parkes, D. C.; Procaccia, A. D.; Rusak,
G.; Shapira, I.; and W¨uthrich, M. 2025. Generative Social
Choice. arXiv preprint.
Fitzgerald, B. 2024. Some Issues in Predictive Ethics Mod-
eling: An Annotated Contrast Set of” Moral Stories”. arXiv
preprint arXiv:2407.05244.
Forbes, M.; Hwang, J. D.; Shwartz, V.; Sap, M.; and Choi,
Y. 2021. Social Chemistry 101: Learning to Reason about
Social and Moral Norms. arXiv:2011.00620.
Fr¨anken, J.-P.; Gandhi, K.; Qiu, T.; Khawaja, A.; Goodman,
N. D.; and Gerstenberg, T. 2024. Procedural Dilemma Gen-
eration for Evaluating Moral Reasoning in Humans and Lan-
guage Models. arXiv preprint.
Ganguli, D.; Askell, A.; Schiefer, N.; Liao, T. I.; Lukoˇsi¯ut˙e,
K.; Chen, A.; Goldie, A.; Mirhoseini, A.; Olsson, C.; Her-
nandez, D.; Drain, D.; Li, D.; Tran-Johnson, E.; Perez,
E.; Kernion, J.; Kerr, J.; Mueller, J.; Landau, J.; Ndousse,
K.; Nguyen, K.; Lovitt, L.; Sellitto, M.; Elhage, N.; Mer-
cado, N.; DasSarma, N.; Rausch, O.; Lasenby, R.; Lar-
son, R.; Ringer, S.; Kundu, S.; Kadavath, S.; Johnston, S.;
Kravec, S.; Showk, S. E.; Lanham, T.; Telleen-Lawton, T.;
Henighan, T.; Hume, T.; Bai, Y.; Hatfield-Dodds, Z.; Mann,
B.; Amodei, D.; Joseph, N.; McCandlish, S.; Brown, T.;
Olah, C.; Clark, J.; Bowman, S. R.; and Kaplan, J. 2023.
The Capacity for Moral Self-Correction in Large Language
Models. arXiv:2302.07459.
Garcia, B.; Qian, C.; and Palminteri, S. 2024. The moral tur-
ing test: Evaluating human-llm alignment in moral decision-
making. arXiv preprint arXiv:2410.07304.
Giubilini, A.; and Savulescu, J. 2018. The Artificial Moral
Advisor. The “Ideal Observer” Meets Artificial Intelligence.
Philosophy & technology, 31: 169–188.
Guan, M. Y.; Joglekar, M.; Wallace, E.; Jain, S.; Barak, B.;
Helyar, A.; Dias, R.; Vallone, A.; Ren, H.; Wei, J.; Chung,
H. W.; Toyer, S.; Heidecke, J.; Beutel, A.; and Glaese, A.
2025.
Deliberative Alignment: Reasoning Enables Safer
Language Models. arXiv preprint.
H¨ammerl, K.; Deiseroth, B.; Schramowski, P.; Libovick´y,
J.; Rothkopf, C.; Fraser, A.; and Kersting, K. 2023. Speak-
ing Multiple Languages Affects the Moral Bias of Language
Models. In Rogers, A.; Boyd-Graber, J.; and Okazaki, N.,
eds., Findings of the Association for Computational Linguis-
tics: ACL 2023, 2137–2156. Toronto, Canada: Association
for Computational Linguistics.
Hendrycks, D.; Burns, C.; Basart, S.; Critch, A.; Li, J.; Song,
D.; and Steinhardt, J. 2020. Aligning AI with Shared Human
Values. arXiv preprint.
Hendrycks, D.; Mazeika, M.; Zou, A.; Patel, S.; Zhu, C.;
Navarro, J.; Song, D.; Li, B.; and Steinhardt, J. 2021. What
Would Jiminy Cricket Do? Towards Agents That Behave
Morally. arXiv preprint.
Hu, Z.; Ren, Y.; Li, J.; and Yin, Y. 2024. VIVA: A Bench-
mark for Vision-Grounded Decision-Making with Human
Values. arXiv:2407.03000.
Huang, Y.; Zhang, Q.; and Sun, L. 2023.
Trustgpt: A
Benchmark for Trustworthy and Responsible Large Lan-
guage Models. arXiv preprint.
Jain, S.; Calacci, D.; and Wilson, A. 2024. As an AI Lan-
guage Model,” Yes I Would Recommend Calling the Po-
lice”: Norm Inconsistency in LLM Decision-Making. arXiv
preprint.
Jha, A.; Mann, P.; Tiwari, A.; Kadian, K.; and Sharma, A.
2024. Decoding Ethics: Proficiency of LLMs in Addressing
Moral Dilemmas. In Ill´es, Z.; Verma, C.; Gonc¸alves, P. J. S.;
and Singh, P. K., eds., Proceedings of International Con-
ference on Recent Innovations in Computing, volume 1195,
593–605. Singapore: Springer Nature Singapore. ISBN 978-
981-97-3441-2 978-981-97-3442-9.
Ji, J.; Chen, Y.; Jin, M.; Xu, W.; Hua, W.; and Zhang, Y.
2024.
MoralBench: Moral Evaluation of LLMs.
arXiv
preprint.
Jiang, H.; Yi, X.; Wei, Z.; Xiao, Z.; Wang, S.; and Xie,
X. 2025.
Raising the Bar: Investigating the Values of
Large Language Models via Generative Evolving Testing.
arXiv:2406.14230.
Jiang, L.; Hwang, J. D.; Bhagavatula, C.; Bras, R. L.; Liang,
J.; Dodge, J.; Sakaguchi, K.; Forbes, M.; Borchardt, J.; and
Gabriel, S. 2021. Can Machines Learn Morality? The Delphi
Experiment. arXiv preprint.
Jin, Z.; Kleiman-Weiner, M.; Piatti, G.; Levine, S.; Liu, J.;
Gonzalez, F.; Ortu, F.; Strausz, A.; Sachan, M.; and Mihal-
cea, R. 2024. Language Model Alignment in Multilingual
Trolley Problems. arXiv preprint.
Jin, Z.; Levine, S.; Gonzalez Adauto, F.; Kamal, O.; Sap, M.;
Sachan, M.; Mihalcea, R.; Tenenbaum, J.; and Sch¨olkopf,
B. 2022. When to Make Exceptions: Exploring Language
Models as Accounts of Human Moral Judgment. Advances
in neural information processing systems, 35: 28458–28473.
Khan, A.; Casper, S.; and Hadfield-Menell, D. 2025. Ran-
domness, Not Representation: The Unreliability of Evaluat-
ing Cultural Alignment in LLMs. arXiv Preprint.
Khandelwal, A.; Agarwal, U.; Tanmay, K.; and Choudhury,
M. 2024. Do Moral Judgment and Reasoning Capability of
LLMs Change with Language? A Study Using the Multilin-
gual Defining Issues Test. arXiv:2402.02135.
Kiehne, N.; Ljapunov, A.; B¨atje, M.; and Balke, W.-T.
2024.
Analyzing Effects of Learning Downstream Tasks

--- Page 10 ---

on Moral Bias in Large Language Models.
In Calzolari,
N.; Kan, M.-Y.; Hoste, V.; Lenci, A.; Sakti, S.; and Xue,
N., eds., Proceedings of the 2024 Joint International Con-
ference on Computational Linguistics, Language Resources
and Evaluation (LREC-COLING 2024), 904–923. Torino,
Italia: ELRA and ICCL.
Kr¨ugel, S.; Ostermaier, A.; and Uhl, M. 2023. ChatGPT’s
Inconsistent Moral Advice Influences Users’ Judgment. Sci-
entific Reports, 13(1): 4569.
Kumar, P.; Lau, E.; Vijayakumar, S.; Trinh, T.; Team, S. R.;
Chang, E.; Robinson, V.; Hendryx, S.; Zhou, S.; and Fredrik-
son, M. 2024. Refusal-Trained LLMs Are Easily Jailbroken
As Browser Agents. arXiv preprint.
Kwon, J.; Tenenbaum, J.; and Levine, S. ????
Neuro-
Symbolic Models of Human Moral Judgment: LLMs as Au-
tomatic Feature Extractors. In Proceedings of the 40th In-
ternational Conference on Machine Learning.
Lanham, T.; Chen, A.; Radhakrishnan, A.; Steiner, B.; Deni-
son, C.; Hernandez, D.; Li, D.; Durmus, E.; Hubinger,
E.; Kernion, J.; Lukoˇsi¯ut˙e, K.; Nguyen, K.; Cheng, N.;
Joseph, N.; Schiefer, N.; Rausch, O.; Larson, R.; McCan-
dlish, S.; Kundu, S.; Kadavath, S.; Yang, S.; Henighan, T.;
Maxwell, T.; Telleen-Lawton, T.; Hume, T.; Hatfield-Dodds,
Z.; Kaplan, J.; Brauner, J.; Bowman, S. R.; and Perez, E.
2023. Measuring Faithfulness in Chain-of-Thought Reason-
ing. arXiv:2307.13702.
Lazar, S. 2024. Frontier AI Ethics: Anticipating and Evalu-
ating the Societal Impacts of Language Model Agents. arXiv
preprint.
Leike, J.; Krueger, D.; Everitt, T.; Martic, M.; Maini, V.;
and Legg, S. 2018.
Scalable Agent Alignment via Re-
ward Modeling: A Research Direction.
arXiv preprint,
https://arxiv.org/abs/1811.07871.
Leshinskaya, A.; and Charkoff, A. 2023. Value as Seman-
tics: Representations of Human Moral and Hedonic Value in
Large Language Models. AI meets Moral Philosophy and
Moral Psychology Workshop at NeurIPS 2023.
Li, X.; Li, Y.; Liu, L.; Bing, L.; and Joty, S. 2022. Is GPT-3
a Psychopath? Evaluating Large Language Models from a
Psychological Perspective.
List, C.; and Pettit, P. 2002. Aggregating Sets of Judgments:
An Impossibility Result. Economics & Philosophy, 18(1):
89–110.
Liu, X.; Zhu, Y.; Zhu, S.; Liu, P.; Liu, Y.; and Yu, D. 2024a.
Evaluating Moral Beliefs across LLMs through a Pluralistic
Framework. arXiv:2411.03665.
Liu, Y.; Yao, Y.; Ton, J.-F.; Zhang, X.; Guo, R.; Cheng, H.;
Klochkov, Y.; Taufiq, M. F.; and Li, H. 2024b. Trustworthy
LLMs: A Survey and Guideline for Evaluating Large Lan-
guage Models’ Alignment. arXiv Preprint.
Lourie, N.; Le Bras, R.; and Choi, Y. 2021. SCRUPLES: A
Corpus of Community Ethical Judgments on 32,000 Real-
Life Anecdotes. Proceedings of the AAAI Conference on
Artificial Intelligence, 35(15): 13470–13479.
Ma, P.; Li, Z.; Sun, A.; and Wang, S. 2023a. ”Oops, Did
I Just Say That?” Testing and Repairing Unethical Sug-
gestions of Large Language Models with Suggest-Critique-
Reflect Process. arXiv:2305.02626.
Ma, X.; Mishra, S.; Beirami, A.; Beutel, A.; and Chen, J.
2023b. Let’s Do a Thought Experiment: Using Counterfac-
tuals to Improve Moral Reasoning. arXiv preprint.
Mercier, H.; and Sperber, D. 2017. The Enigma of Reason.
Cambridge, Massachusetts: Harvard University Press. ISBN
978-0-674-36830-9.
Minsky, M. 1986. The Society of Mind. New York: Simon
and Schuster. ISBN 0-671-60740-5.
Minsky, M. 2006. The Emotion Machine : Commonsense
Thinking, Artificial Intelligence, and the Future of the Hu-
man Mind. New York: Simon & Schuster. ISBN 0-7432-
7663-9 978-0-7432-7663-4.
Moore, J.; Deshpande, T.; and Yang, D. 2024. Are large lan-
guage models consistent over value-laden questions? arXiv
preprint arXiv:2407.02996.
Neuman, W. R.; Coleman, C.; and Shah, M. 2025.
An-
alyzing the Ethical Logic of Six Large Language Models.
arXiv:2501.08951.
Nie, A.; Zhang, Y.; Amdekar, A. S.; Piech, C.; Hashimoto,
T. B.; and Gerstenberg, T. 2023. Moca: Measuring Human-
Language Model Alignment on Causal and Moral Judgment
Tasks. Advances in Neural Information Processing Systems,
36: 78360–78393.
Nunes, J. L.; Almeida, G. F. C. F.; de Araujo, M.; and Bar-
bosa, S. D. J. 2023.
Are Large Language Models Moral
Hypocrites? A Study Based on Moral Foundations.
Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright, C.;
Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.;
Schulman, J.; Hilton, J.; Kelton, F.; Miller, L.; Siemens, M.;
Askell, A.; Welinder, P.; Christiano, P.; Leike, J.; and Lowe,
R. 2022. Training Language Models to Follow Instructions
with Human Feedback.
Advances in Neural Information
Processing Systems, 35: 27730–27744.
Pan, A.; Chan, J. S.; Zou, A.; Li, N.; Basart, S.; Woodside,
T.; Zhang, H.; Emmons, S.; and Hendrycks, D. 2023. Do the
Rewards Justify the Means? Measuring Trade-Offs Between
Rewards and Ethical Behavior in the Machiavelli Bench-
mark. In Proceedings of the 40th International Conference
on Machine Learning, 26837–26867. PMLR.
Porter, M. S. 2024.
Moral Agency in Silico: Explor-
ing Free Will in Large Language Models. arXiv preprint
arXiv:2410.23310.
Pyatkin, V.; Hwang, J. D.; Srikumar, V.; Lu, X.; Jiang, L.;
Choi, Y.; and Bhagavatula, C. 2023. ClarifyDelphi: Rein-
forced Clarification Questions with Defeasibility Rewards
for Social and Moral Situations. arXiv preprint.
Rao, A. S.; Khandelwal, A.; Tanmay, K.; Agarwal, U.; and
Choudhury, M. ???? Ethical Reasoning over Moral Align-
ment: A Case and Framework for In-Context Ethical Poli-
cies in LLMs. In Bouamor, H.; Pino, J.; and Bali, K., eds.,
Conference on Empirical Methods in Natural Language
Processing, 13370–13388. Singapore: Association for Com-
putational Linguistics.

--- Page 11 ---

Rao, K.; Jiang, L.; Pyatkin, V.; Gu, Y.; Tandon, N.; Dziri, N.;
Brahman, F.; and Choi, Y. 2023. What Makes It Ok to Set
a Fire? Iterative Self-distillation of Contexts and Rationales
for Disambiguating Defeasible Social and Moral Situations.
arXiv:2310.15431.
Rashid, A. A.; Skelly, R. A.; Valdes, C. A.; Patel, P. P.; Sol-
berg, L. B.; Giordano, C. R.; and Modave, F. 2024. Evalu-
ating ChatGPT’s Moral Competence in Health Care-Related
Ethical Problems. JAMIA Open, 7(3): ooae065.
Rawls, J. 1993. Political Liberalism. New York: Columbia
University Press.
Rawls, J. 1999.
A Theory of Justice.
Oxford: Oxford
University Press, rev. edition.
ISBN 0198250541 (hbk)
019825055X (pbk).
Rehman, U.; Iqbal, F.; and Shah, M. U. 2025. Exploring
Differences in Ethical Decision-Making Processes between
Humans and ChatGPT-3 Model: A Study of Trade-Offs. AI
and Ethics, 5(1): 279–289.
Reinig, I.; Becker, M.; Rehbein, I.; and Ponzetto, S. ????
A Survey on Modelling Morality for Text Analysis. Find-
ings of the Association for Computational Linguistics: ACL
2024, 4136–4155. Association for Computational Linguis-
tics.
Rezaei, M.; Fu, Y.; Cuvin, P.; Ziems, C.; Zhang, Y.; Zhu, H.;
and Yang, D. 2025.
EgoNormia: Benchmarking Physical
Social Norm Understanding. arXiv Preprint.
Rodionov, S.; Goertzel, Z. A.; and Goertzel, B. 2023. An
Evaluation of GPT-4 on the ETHICS Dataset. arXiv preprint
arXiv:2309.10492.
Rozen, N.; Bezalel, L.; Elidan, G.; Globerson, A.; and
Daniel, E. 2024.
Do LLMs Have Consistent Values?
arXiv:2407.12878.
Russo, G.; Nozza, D.; R¨ottger, P.; and Hovy, D. 2025. The
Pluralistic Moral Gap: Understanding Judgment and Value
Differences between Humans and Large Language Models.
arXiv preprint arXiv:2507.17216.
Sachdeva, P.; and van Nuenen, T. 2025. Normative Eval-
uation of Large Language Models with Everyday Moral
Dilemmas.
In Proceedings of the 2025 ACM Conference
on Fairness, Accountability, and Transparency, FAccT ’25,
690–709. New York, NY, USA: Association for Computing
Machinery. ISBN 9798400714825.
Scanlon, T. M. 1998. What We Owe to Each Other. London:
Belknap Press. ISBN 0674950895 067400423X (pbk).
Scherrer, N.; Shi, C.; Feder, A.; and Blei, D. 2024. Evaluat-
ing the Moral Beliefs Encoded in Llms. Advances in Neural
Information Processing Systems, 36.
Seror, A. 2025. The Moral Mind(s) of Large Language Mod-
els. arXiv:2412.04476.
Shao, Y.; Li, T.; Shi, W.; Liu, Y.; and Yang, D. 2024. Priva-
cyLens: Evaluating Privacy Norm Awareness of Language
Models in Action. arXiv preprint.
Silen, N.; Atkinson, D.; Green, M.; Hamadi, M.; Swift, C.;
Schonholtz, D.; Kalai, A. T.; and Bau, D. 2023.
Testing
Language Model Agents Safely in the Wild. arXiv preprint.
Soffer, S.; Nesselroth, D.; Pragier, K.; Anteby, R.; Apakama,
D.; Holmes, E.; Sawant, A. S.; Abbott, E.; Lepow, L. A.;
and Vasudev, I. 2024.
Disagreements in Medical Ethics
Question Answering Between Large Language Models and
Physicians.
Sorensen, T.; Jiang, L.; Hwang, J. D.; Levine, S.; Pyatkin,
V.; West, P.; Dziri, N.; Lu, X.; Rao, K.; Bhagavatula, C.;
Sap, M.; Tasioulas, J.; and Choi, Y. 2024a. Value Kaleido-
scope: Engaging AI with Pluralistic Human Values, Rights,
and Duties. Proceedings of the AAAI Conference on Artifi-
cial Intelligence, 38(18): 19937–19947.
Sorensen, T.; Mishra, P.; Patel, R.; Tessler, M. H.; Bakker,
M.; Evans, G.; Gabriel, I.; Goodman, N.; and Rieser, V.
2025.
Value Profiles for Encoding Human Variation.
arXiv:2503.15484.
Sorensen, T.; Moore, J.; Fisher, J.; Gordon, M.; Mireshghal-
lah, N.; Rytting, C. M.; Ye, A.; Jiang, L.; Lu, X.; Dziri, N.;
Althoff, T.; and Choi, Y. 2024b. A Roadmap to Pluralistic
Alignment. arXiv:2402.05070.
Stanley, J. 2011. Know how. OUP Oxford.
Sun, H.; Zhang, Z.; Mi, F.; Wang, Y.; Liu, W.; Cui, J.; Wang,
B.; Liu, Q.; and Huang, M. 2023. MoralDial: A Framework
to Train and Evaluate Moral Dialogue Systems via Moral
Discussions. arXiv:2212.10720.
Takemoto, K. 2024.
The Moral Machine Experiment on
Large Language Models.
Royal Society Open Science,
11(2): 231393.
Talat, Z.; Blix, H.; Valvoda, J.; Ganesh, M. I.; Cotterell, R.;
and Williams, A. ???? On the Machine Learning of Ethi-
cal Judgments from Natural Language. Proceedings of the
2022 Conference of the North American Chapter of the As-
sociation for Computational Linguistics: Human Language
Technologies, 769–779. Association for Computational Lin-
guistics.
Tanmay, K.; Khandelwal, A.; Agarwal, U.; and Choud-
hury, M. 2023.
Probing the Moral Development of
Large Language Models through Defining Issues Test.
arXiv:2309.13356.
Tie, G.; Zhao, Z.; Song, D.; Wei, F.; Zhou, R.; Dai, Y.; Yin,
W.; Yang, Z.; Yan, J.; Su, Y.; Dai, Z.; Xie, Y.; Cao, Y.; Sun,
L.; Zhou, P.; He, L.; Chen, H.; Zhang, Y.; Wen, Q.; Liu, T.;
Gong, N. Z.; Tang, J.; Xiong, C.; Ji, H.; Yu, P. S.; and Gao, J.
2025. A Survey on Post-training of Large Language Models.
arXiv Preprint.
Vida, K.; Damken, F.; and Lauscher, A. 2024. Decoding
Multilingual Moral Preferences: Unveiling LLM’s Biases
through the Moral Machine Experiment.
Proceedings of
the AAAI/ACM Conference on AI, Ethics, and Society, 7(1):
1490–1501.
Vida, K.; Simon, J.; and Lauscher, A. ???? Values, Ethics,
Morals? On the Use of Moral Concepts in NLP Research.
Findings of the Association for Computational Linguistics:
EMNLP 2023, 5534–5554. Association for Computational
Linguistics.
Vredenburgh, K. 2022. The right to explanation. Journal of
Political Philosophy, 30(2): 209–229.

--- Page 12 ---

Wang, G.; Wang, W.; Cao, Y.; Teng, Y.; Guo, Q.; Wang, H.;
Lin, J.; Ma, J.; Liu, J.; and Wang, Y. 2024. Possibilities and
Challenges in the Moral Growth of Large Language Models:
A Philosophical Perspective. Ethics and Information Tech-
nology, 27(1): 9.
Wu, Y.; Sheng, Q.; Wang, D.; Yang, G.; Sun, Y.; Wang, Z.;
Bu, Y.; and Cao, J. 2025. The Staircase of Ethics: Probing
LLM Value Priorities through Multi-Step Induction to Com-
plex Moral Dilemmas. arXiv preprint arXiv:2505.18154.
Yan, B.; Zhang, J.; Chen, Z.; Shan, S.; and Chen, X.
2024. M\ˆ3{oralBench: A MultiModal Moral Benchmark
for LVLMs. arXiv:2412.20718.
Yao, J.; Yi, X.; Duan, S.; Wang, J.; Bai, Y.; Huang, M.;
Zhang, P.; Lu, T.; Dou, Z.; Sun, M.; and Xie, X. 2025. Value
Compass Leaderboard: A Platform for Fundamental and
Validated Evaluation of LLMs Values. arXiv:2501.07071.
Yao, J.; Yi, X.; and Xie, X. 2024. CLAVE: An Adaptive
Framework for Evaluating Values of LLM Generated Re-
sponses. arXiv Preprint.
Ye, H.; Zhang, T.; Xie, Y.; Zhang, L.; Ren, Y.; Zhang, X.;
and Song, G. 2025. Generative Psycho-Lexical Approach
for Constructing Value Systems in Large Language Models.
arXiv:2502.02444.
Yu, L.; Leng, Y.; Huang, Y.; Wu, S.; Liu, H.; Ji, X.; Zhao,
J.; Song, J.; Cui, T.; Cheng, X.; et al. 2024. CMoralEval:
A moral evaluation benchmark for Chinese large language
models. arXiv preprint arXiv:2408.09819.
Yuan, J.; Murukannaiah, P. K.; and Singh, M. P. 2024.
Right vs. Right: Can LLMs Make Tough Choices?
arXiv:2412.19926.
Zhang, J.; Yuan, Z.; Wang, Z.; Yan, B.; Wang, S.; Cao, X.;
Guo, Z.; Shan, S.; and Chen, X. 2025. REVAL: A Com-
prehension Evaluation on Reliability and Values of Large
Vision-Language Models. arXiv:2503.16566.
Zhang, Z.; Zhang, C.; Liu, N.; Qi, S.; Rong, Z.; Zhu, S.-C.;
Cui, S.; and Yang, Y. 2024. Heterogeneous Value Alignment
Evaluation for Large Language Models. arXiv:2305.17147.
Zhou, J.; Hu, M.; Li, J.; Zhang, X.; Wu, X.; King, I.; and
Meng, H. 2024. Rethinking Machine Ethics – Can LLMs
Perform Moral Reasoning through the Lens of Moral Theo-
ries? In Duh, K.; Gomez, H.; and Bethard, S., eds., Findings
of the Association for Computational Linguistics: NAACL
2024, 2227–2242. Mexico City, Mexico: Association for
Computational Linguistics.
Ziems, C.; Dwivedi-Yu, J.; Wang, Y.-C.; Halevy, A.; and
Yang, D. 2023. NormBank: A Knowledge Bank of Situa-
tional Social Norms. arXiv:2305.17008.
Ziems, C.; Yu, J. A.; Wang, Y.-C.; Halevy, A.; and Yang, D.
2022. The Moral Integrity Corpus: A Benchmark for Ethical
Dialogue Systems. arXiv:2204.03021.

--- Page 13 ---

A
Detailed Survey Results
Our literature survey resulted in a corpus of included 69 pa-
pers (see Fig. 2); (Abbo and Belpaeme 2025), (Abbo et al.
2024), (Aharoni et al. 2024), (bin Ahmad and Takemoto
2024), (Albrecht, Kitanidis, and Fetterman 2022), (Almeida
et al. 2024), (Alhassan, Zhang, and Schlegel 2022), (Awad
et al. 2022), (Balas et al. 2024), (Bhattacharya and Nandi
2023), (Bignotti and Camassa 2024), (Bonagiri et al. 2024),
(Bulla et al. 2025), (Cheung, Maier, and Lieder 2024),
(Chiu, Jiang, and Choi 2024), (Chiu et al. 2025), (Chun
and Elkins 2024), (Dillion et al. 2025), (Duan et al. 2024),
(Emelin et al. 2020), (Fitzgerald 2024), (Fr¨anken et al.
2024), (Garcia, Qian, and Palminteri 2024), (Hendrycks
et al. 2020), (Hendrycks et al. 2021), (Hu et al. 2024), (Jha
et al. 2024), (Ji et al. 2024), (Jiang et al. 2025), (Jiang
et al. 2021), (Jin et al. 2024), (Jin et al. 2022), (Khandelwal
et al. 2024), (Kr¨ugel, Ostermaier, and Uhl 2023), (Kwon,
Tenenbaum, and Levine), (Leshinskaya and Charkoff 2023),
(Liu et al. 2024a), (Lourie, Le Bras, and Choi 2021), (Ma
et al. 2023a), (Ma et al. 2023b), (Moore, Deshpande, and
Yang 2024), (Neuman, Coleman, and Shah 2025), (Nie et al.
2023), (Nunes et al. 2023), (Pan et al. 2023), (Porter 2024),
(Pyatkin et al. 2023), (Rao et al.), (Rashid et al. 2024),
(Rehman, Iqbal, and Shah 2025), (Rezaei et al. 2025), (Ro-
dionov, Goertzel, and Goertzel 2023), (Russo et al. 2025),
(Sachdeva and van Nuenen 2025), (Scherrer et al. 2024),
(Seror 2025), (Shao et al. 2024), (Soffer et al. 2024),
(Sorensen et al. 2024a), (Sun et al. 2023), (Tanmay et al.
2023), (Takemoto 2024), (Wang et al. 2024), (Wu et al.
2025), (Yan et al. 2024), (Yao, Yi, and Xie 2024), (Yuan,
Murukannaiah, and Singh 2024), (Yu et al. 2024), (Zhou
et al. 2024).
Notes on Exclusions
We excluded a number of papers that were focused not on
evaluating LLM ethical competence, but on identifying pat-
terns in LLMs’ moral judgments that either indicated their
implicit association with some demographic or other social
group, or else were reflective of cultural bias (Ye et al. 2025;
Yao et al. 2025; Li et al. 2022; Rozen et al. 2024; Zhang
et al. 2024; Abdulhai et al. 2023; Aksoy 2024; Durmus et al.
2023).
We also excluded several papers that initially appeared to
be about moral competence, but were ultimately standard
evaluations of conversational agent alignment, especially
against standards of toxicity and bias (in particular, (Zhang
et al. 2025; Ziems et al. 2022; Jain, Calacci, and Wilson
2024; H¨ammerl et al. 2023; Vida, Damken, and Lauscher
2024; Huang, Zhang, and Sun 2023; Ganguli et al. 2023;
Kiehne et al. 2024)).
We identified a few interesting papers building datasets to
support moral competence fine-tuning of language models;
what’s most interesting about these is that we suspect that
they have ultimately proved redundant, because the most ca-
pable base LLMs acquire enough moral understanding from
pretraining that additional finetuning for this particular skill
is more or less redundant (though (Jiang et al. 2021) does
suggest that there remained a little delta in finetuning for
DATASETS
BEHAVIORS
METRICS
produce
are 
measured by
inform 
development 
of
Figure 1: A visualisation of our three-part framework for
evaluating evaluations of LLM Moral Reasoning.
this purpose still). See in particular (Ziems et al. 2023; Rao
et al. 2023; Forbes et al. 2021).
Detailed Taxonomy Breakdown
We used a taxonomy with three categories (Datasets, Be-
haviours, Metrics) for evaluating LLM ethical competence
(see Fig 1). We applied this framework to each paper in
our corpus. Each category contains multiple dimensions that
together provide a comprehensive framework for analyzing
approaches to evaluating LLM moral understanding.
Datasets
By datasets, we refer to the collection of cases
or instances researchers expose an LLM to in order to gauge
moral competence.
• Construction: How and where the data were sourced,
including any pre-processing steps used to augment or
expand another dataset.
• Language/s: The languages included in the dataset.
• Type:
– Static: A fixed set of test items that remains unchanged
during evaluation
– Generative: A method that dynamically creates new
test cases specifically at evaluation time
– Interactive:
An
evaluation
involving
multi-step
decision-making over time
• Nature:
– Artificial: Constructed dilemmas like trolley problems
– Everyday: Constructed cases that aim to represent re-
alistic human scenarios
– Found: Cases taken from real-world sources (e.g., on-
line scraping)
• Structuring:
– Psychometric: Uses or adapts a validated psychomet-
ric tool for moral assessment

--- Page 14 ---

2020
2021
2022
2023
2024
2025
Year
0
10
20
30
40
50
60
70
Number of Papers
12
47
(projected)
2
3
4
14
34
y=2.57 e0.0493 m
R 2 =0.9589
Figure 2: Number of papers evaluating LLM ethical competence published per year from 2020 to 2025. The exponential
regression suggests a doubling rate for the field of 14.06 months.
– Structured: Data or organized according to a moral,
legal, conceptual, or other theory or framework to at-
tempt to achieve comprehensiveness in some sense
over a range of normative domains
– Haphazard: Arbitrary or ad-hoc selection of cases or
datapoints
• Complexity:15
– Simple: Highly simplified cases
– Complex: Cases with multiple variables
– Complex with conflicts: Complex cases specifically in-
cluding conflicts of values
• Viewpoint:
– Anthropocentric: Focused on ethical decisions a hu-
man would make
– Agent-centric: Focused on ethical decisions an AI
agent might have to make
• Attention to Framing Effects: Whether the evaluation
considers how the formulation of a case might influence
model responses.
• Modality:
– Text Only: Evaluates only textual information
– Multimodal: Evaluates multiple modalities (e.g., text
and images)
• Data Packaging:
– Prepackaged: Data tightly selected for normative rele-
vance
– Unfiltered: Data resembling an unfiltered stream from
which the model must identify normatively relevant
features
15 Simple cases for instance might feature a single variable or
stakeholder relating to a moral choice (e.g. “Is it wrong to keep $1
you find on the street?”). In contrast, complex cases can include
multiple variables and/or stakeholders, potentially including irrele-
vant variables (e.g. “A doctor working in a understaffed rural hos-
pital during a pandemic must decide how to allocate the last ven-
tilator between [. . . a list of patients and patient details]”). A final
complexity class considers cases that, in addition to being complex,
are designed to foreground intentional conflicts of values, requiring
the decision maker to adopt a considered ethical position to resolve
the value conflicts (e.g. “A journalist discovers that publishing a
truthful story about corruption will expose wrongdoing [honesty
and justice values], but will also destroy the lives of innocent fam-
ily members of the official and potentially harm national security
[compassion/loyalty values]. What should the journalist do?”).

--- Page 15 ---

Behaviours
By behaviours, we refer to the capacities or
functions being evaluated in the LLMs.
• Verdicts: Asking models to make moral judgments on
cases.
• Steerability: Assessing whether the model can apply dif-
ferent moral principles when given them at inference
time (not through fine-tuning).
• Justifications: Evaluating whether the model provides
reasons for its decisions, including testing justifications
by identifying specific elements of a good justification
and evaluating model performance in each of those re-
spects.
• Attention to Morally Relevant Features: Assessing
whether the model focuses on the right moral aspects of
a situation.
• Ability to Gather More Information: Testing the
model’s ability to make sound “moral value of informa-
tion” judgments—determining when it needs more infor-
mation to make a safe decision.
Metrics
By metrics we refer to the standards by which re-
searchers evaluate the LLMs’ behaviours.
• Verdict Metrics:
– Ground
Truth:
Comparison
to
ran-
dom/representative/expert
judgments
(human
or
otherwise)
– Robustness: Testing whether the model’s judgment
changes when irrelevant details change
– Consistency: Evaluating whether the model gives the
same answer when asked the same question multiple
times
– Reasonableness: Assessing whether the model stays
within acceptable moral boundaries (within the bounds
of reasonable pluralism)
• Steerability Metrics: Evaluating whether and how well
a model’s moral profile can be steered at inference time.
• Justification Metrics:
– Moral Turing Test: Having humans try to distinguish
between AI and human responses, or comparatively
score/rank them
– Quality of Reasoning: Evaluating whether the justifi-
cations are actually good according to some standard
• Error Evaluation: Assessing whether the model’s errors
make sense or follow an understandable pattern.
Detailed Corpus Analysis
Below, we include tables visualising our analysis from ap-
plying our taxonomny of datasets/behaviours/metrics. Our
full analysis notes –including explanations and justifications
for how each paper was coded– are released at our GitHub
repository.16
16(Redacted for peer review)

--- Page 16 ---

Citation
Language/s
Type
Nature
Structuring
Complexity
Viewpoint
Attention to Framing Effects
Packaging
Data Modality
= Static
= Interactive
= Generative
= Artificial
= Staged
= Real World
= Psychometric
= Theory based
= Arbitrary
= Simple
= Complex
= Complex with conflicts
= Anthropocentric
= Agent-centric
= No
= Limited
= Yes
= Pre-packaged
= Raw data
= Text
= Multimodal
(Abbo and Belpaeme 2025)
English
(Abbo et al. 2024)
English
(Aharoni et al. 2024)
English
(bin Ahmad and Takemoto 2024)
English
(Albrecht, Kitanidis, and Fetterman 2022)
English
(Almeida et al. 2024)
English
(Alhassan, Zhang, and Schlegel 2022)
English
(Awad et al. 2022)
English
(Balas et al. 2024)
English
(Bhattacharya and Nandi 2023)
English
(Bignotti and Camassa 2024)
English
(Bonagiri et al. 2024)
English
/
(Bulla et al. 2025)
English
(Cheung, Maier, and Lieder 2024)
English
(Chiu, Jiang, and Choi 2024)
English
(Chiu et al. 2025)
English
(Chun and Elkins 2024)
English
(Dillion et al. 2025)
English
/
(Duan et al. 2024)
English
/
(Emelin et al. 2020)
English
(Fitzgerald 2024)
English
(Fr¨anken et al. 2024)
English
/
(Garcia, Qian, and Palminteri 2024)
English
(Hendrycks et al. 2020)
English
(Hendrycks et al. 2021)
English
(Hu et al. 2024)
English
/
/
(Jha et al. 2024)
English
(Ji et al. 2024)
English
(Jiang et al. 2025)
English
/
(Jiang et al. 2021)
English
(Jin et al. 2024)
107 languagesa
(Jin et al. 2022)
English
(Kr¨ugel, Ostermaier, and Uhl 2023)
English
(Khandelwal et al. 2024)
Six languagesb
(Kwon, Tenenbaum, and Levine)
English
(Leshinskaya and Charkoff 2023)
English
(Liu et al. 2024a)
Chinese
(Lourie, Le Bras, and Choi 2021)
English
(Ma et al. 2023a)
English
(Ma et al. 2023b)
English
(Moore, Deshpande, and Yang 2024)
Four languagesc
(Neuman, Coleman, and Shah 2025)
English and French
/
(Nie et al. 2023)
Six languagesd
(Nunes et al. 2023)
English
/
(Pan et al. 2023)
English
/
(Porter 2024)
English
(Pyatkin et al. 2023)
English
(Rashid et al. 2024)
English
(Rao et al.)
English
(Rehman, Iqbal, and Shah 2025)
English
(Rezaei et al. 2025)
English
(Rodionov, Goertzel, and Goertzel 2023)
English
(Russo et al. 2025)
English
(Sachdeva and van Nuenen 2025)
English
(Scherrer et al. 2024)
English
(Seror 2025)
English
(Shao et al. 2024)
English
(Soffer et al. 2024)
English
(Sorensen et al. 2024a)
English
(Sun et al. 2023)
English
(Tanmay et al. 2023)
English
(Takemoto 2024)
English
(Wang et al. 2024)
English
/
(Wu et al. 2025)
English
(Yan et al. 2024)
English
(Yao, Yi, and Xie 2024)
English
(Yuan, Murukannaiah, and Singh 2024)
English
(Yu et al. 2024)
Chinese
(Zhou et al. 2024)
English
/
Table 1: Corpus analysis using our taxonomy of datasets. a(920 English vignettes translated via Google Translate). b(English, Chinese, Hindi, Russian, Spanish, and Swahili). c(English, Chinese, German,
and Japanese). d(English, Chinese, Hindi, Russian, Spanish, and Swahili).

--- Page 17 ---

Citation
Verdicts
Steerability
Justifications
Morally Relevant Features
Ability to gather more information
= No,
= Limited/Implicit/Partial,
= Yes
(Abbo and Belpaeme 2025)
(Abbo et al. 2024)
(Aharoni et al. 2024)
(bin Ahmad and Takemoto 2024)
(Albrecht, Kitanidis, and Fetterman 2022)
(Almeida et al. 2024)
(Alhassan, Zhang, and Schlegel 2022)
(Awad et al. 2022)
(Balas et al. 2024)
(Bhattacharya and Nandi 2023)
(Bignotti and Camassa 2024)
(Bonagiri et al. 2024)
(Bulla et al. 2025)
(Cheung, Maier, and Lieder 2024)
(Chiu, Jiang, and Choi 2024)
(Chiu et al. 2025)
(Chun and Elkins 2024)
(Dillion et al. 2025)
(Duan et al. 2024)
(Emelin et al. 2020)
(Fitzgerald 2024)
(Fr¨anken et al. 2024)
(Garcia, Qian, and Palminteri 2024)
(Hendrycks et al. 2020)
(Hendrycks et al. 2021)
(Hu et al. 2024)
(Jha et al. 2024)
(Ji et al. 2024)
(Jiang et al. 2025)
(Jiang et al. 2021)
(Jin et al. 2024)
(Jin et al. 2022)
(Khandelwal et al. 2024)
(Kr¨ugel, Ostermaier, and Uhl 2023)
(Kwon, Tenenbaum, and Levine)
(Leshinskaya and Charkoff 2023)
(Liu et al. 2024a)
(Lourie, Le Bras, and Choi 2021)
(Ma et al. 2023a)
(Ma et al. 2023b)
(Moore, Deshpande, and Yang 2024)
(Neuman, Coleman, and Shah 2025)
(Nie et al. 2023)
(Nunes et al. 2023)
(Pan et al. 2023)
(Porter 2024)
(Pyatkin et al. 2023)
(Rao et al.)
(Rashid et al. 2024)
(Rehman, Iqbal, and Shah 2025)
(Rezaei et al. 2025)
(Rodionov, Goertzel, and Goertzel 2023)
(Russo et al. 2025)
(Sachdeva and van Nuenen 2025)
(Scherrer et al. 2024)
(Seror 2025)
(Shao et al. 2024)
(Soffer et al. 2024)
(Sorensen et al. 2024a)
(Sun et al. 2023)
(Takemoto 2024)
(Tanmay et al. 2023)
(Wang et al. 2024)
(Wu et al. 2025)
(Yan et al. 2024)
(Yao, Yi, and Xie 2024)
(Yuan, Murukannaiah, and Singh 2024)
(Yu et al. 2024)
(Zhou et al. 2024)
Table 2: Corpus analysis using our taxonomy of model behaviour

--- Page 18 ---

Citation
Ground Truth
Robustness
Consistency
Reasonableness
Steerability
Moral Turing Test
Quality of Reasoning or Justifications
Evaluating Errors
= No,
= Limited/Implicit/Partial,
= Yes
(Abbo and Belpaeme 2025)
(Abbo et al. 2024)
(Aharoni et al. 2024)
(bin Ahmad and Takemoto 2024)
(Albrecht, Kitanidis, and Fetterman 2022)
(Almeida et al. 2024)
(Alhassan, Zhang, and Schlegel 2022)
(Awad et al. 2022)
(Balas et al. 2024)
(Bhattacharya and Nandi 2023)
(Bignotti and Camassa 2024)
(Bonagiri et al. 2024)
(Bulla et al. 2025)
(Cheung, Maier, and Lieder 2024)
(Chiu, Jiang, and Choi 2024)
(Chiu et al. 2025)
(Chun and Elkins 2024)
(Dillion et al. 2025)
(Duan et al. 2024)
(Emelin et al. 2020)
(Fitzgerald 2024)
(Fr¨anken et al. 2024)
(Garcia, Qian, and Palminteri 2024)
(Hendrycks et al. 2020)
(Hendrycks et al. 2021)
(Hu et al. 2024)
(Jha et al. 2024)
(Ji et al. 2024)
(Jiang et al. 2025)
(Jiang et al. 2021)
(Jin et al. 2024)
(Jin et al. 2022)
(Khandelwal et al. 2024)
(Kr¨ugel, Ostermaier, and Uhl 2023)
(Kwon, Tenenbaum, and Levine)
(Leshinskaya and Charkoff 2023)
(Liu et al. 2024a)
(Lourie, Le Bras, and Choi 2021)
(Ma et al. 2023a)
(Ma et al. 2023b)
(Moore, Deshpande, and Yang 2024)
(Neuman, Coleman, and Shah 2025)
(Nie et al. 2023)
(Nunes et al. 2023)
(Pan et al. 2023)
(Porter 2024)
(Pyatkin et al. 2023)
(Rao et al.)
(Rashid et al. 2024)
(Rehman, Iqbal, and Shah 2025)
(Rezaei et al. 2025)
(Rodionov, Goertzel, and Goertzel 2023)
(Russo et al. 2025)
(Sachdeva and van Nuenen 2025)
(Scherrer et al. 2024)
(Seror 2025)
(Shao et al. 2024)
(Soffer et al. 2024)
(Sorensen et al. 2024a)
(Sun et al. 2023)
(Tanmay et al. 2023)
(Takemoto 2024)
(Wang et al. 2024)
(Wu et al. 2025)
(Yan et al. 2024)
(Yao, Yi, and Xie 2024)
(Yuan, Murukannaiah, and Singh 2024)
(Yu et al. 2024)
(Zhou et al. 2024)
Table 3: Corpus analysis using our taxonomy of evaluation metrics

```
