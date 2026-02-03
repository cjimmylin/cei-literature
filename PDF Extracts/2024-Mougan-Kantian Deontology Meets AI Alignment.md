---
title: "2024-Mougan-Kantian Deontology Meets AI Alignment - PDF Extract"
source_pdf: "2024-Mougan-Kantian Deontology Meets AI Alignment.pdf"
pages: 17
extracted_at: "2026-01-29T13:51:21.001927"
---

# PDF Extract: 2024-Mougan-Kantian Deontology Meets AI Alignment

**Source PDF:** 2024-Mougan-Kantian Deontology Meets AI Alignment.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

arXiv:2311.05227v2  [cs.AI]  26 Feb 2024
Kantian Deontology Meets AI Alignment: Towards
Morally Grounded Fairness Metrics
Carlos Mougan
University of Southampton
United Kingdom
c.mougan@soton.ac.uk
Joshua Brand
Institut Polytechnique de Paris-T´el´ecom Paris
France
joshua.brand@telecom-paris.fr
Abstract
Deontological ethics, speciﬁcally understood through Immanuel Kant, provides a
moral framework that emphasizes the importance of duties and principles rather
than the consequences of action. Understanding that despite the prominence of
deontology, it is currently an overlooked approach in fairness metrics, this pa-
per explores the compatibility of a Kantian deontological framework in fairness
metrics, part of the AI alignment ﬁeld. We revisit Kant’s critique of utilitarian-
ism, which is the primary approach in AI fairness metrics and argue that fairness
principles should align with the Kantian deontological framework. By integrating
Kantian ethics into AI alignment, we not only bring in a widely accepted promi-
nent moral theory but also strive for a more morally grounded AI landscape that
better balances outcomes and procedures in pursuit of fairness and distributive
justice.
1
Introduction
Deontological ethics, with Immanuel Kant as its central ﬁgure, in particular through his seminal
work Groundwork of the Metaphysics of Morals (Kant, 1785), emphasizes that it is through duties,
or a universal set of rules, that the ethical value of actions is determined. Generally, this form of
deontological ethics maintains that these duties ﬂow from the recognition that all humans are intrin-
sically valuable—it is our rational nature that gives us reason to act in one way or another. This
duty, or rule-based, moral theory thus aligns well with various declarations, such as the Universal
Declaration of Human Rights, that recognize a set of inalienable rights based on the individual, such
as the right to life and the right to equal treatment under the law; with deontology, moral action
involves respecting inescapable duties that often lay the fundamental foundation of the rights of oth-
ers. While it is true that not all duties entail rights, all rights suppose a corresponding duty (Watson,
2021).
Given this emphasis on evaluating actions through a set of rules or principles, deontology is most
often constrasted to utilitarianism, a consequentialist ethical theory. Utilitarianism, traditionally
understood through the likes of Jeremy Bentham or John Stuart Mill, focuses on the consequences
of an action to determine its ethical value, considering the utility or beneﬁt brought about by the
action (Macleod, 2020; Mill, 1966; Bentham, 1996). In traditional utilitarian accounts, utility is
identiﬁed as pleasure, well-being, or happiness (Driver, 2022). The goal of moral action is therefore
generally construed as increasing the amount of pleasure or happiness in our communities, with
various proposed methods to measure these outcomes.
This is why utilitarian ethics is often favoured in quantitative sciences due to its emphasis on mea-
surable outcomes, such as in the ﬁelds of economics (Posner, 1979) or public policy (Kymlicka,
2002; Goodin, 1995). It should be noted, however, that utilitarians face criticism on how one can
quantify such concepts as happiness (Knutsson, 2016). By quantifying and comparing the various
Preprint. Under review.

--- Page 2 ---

consequential beneﬁts and harms of different actions or policies, the utilitarian approach neverthe-
less claims to achieve the most favourable outcome for the greatest number of individuals.
In the AI alignment ﬁeld, the ethical challenge relies on ensuring that AI systems are ﬁrst beneﬁcial
and then align with a diverse set of human values, encompassing moral, societal, justice-oriented,
and other relevant principles. As London et al. London and Heidari (2023) succinctly state,
“It should be axiomatic that producing some sort of beneﬁt is a necessary condition for the ethical
and responsible use of AI.”
It is here that fairness metrics play a vital role by helping to evaluate whether AI systems meet these
prescribed values and treat a diverse set of individuals and groups affected by AI systems fairly—in
other words, if they are treated in an impartial or equitable manner. As one of the primary aims
of any moral theory or prescribed set of values is to establish the deﬁnition of the fair treatment of
others, fairness metrics are an integral component of AI alignment.
In machine learning, researchers, in order to optimize fairness metrics, balance fairness-accuracy
trade-offs to ﬁnd an equilibrium between predictive performance metrics like accuracy, f1-score,
AUC, mean squared errors, and utilitarian interpretations of distributive justice principles, such
as equal opportunity and equal outcomes (Hardt et al., 2016; Heidari et al., 2019). Striving to op-
timize these trade-offs, researchers attempt pre-processing (Fabbrizzi et al., 2023; Ntoutsi et al.,
2020), in-processing (Pedreschi et al., 2008; Menon and Williamson, 2018; Zafar et al., 2017;
Kamishima et al., 2012), and post-processing strategies (Rodolfa et al., 2021).
The utilitarian approach currently takes primacy over other moral accounts, including deontology, in
fairness metrics. Understanding that deontology is a prominent moral theory well-suited to widely
accepted conceptions of human rights that recognize individual dignity and worth, and which brings
important and established critiques against utilitarianism, we argue that it should be adopted into
the fairness metrics approach to counter utilitarian dominance. In this paper we therefore analyze
fairness metrics through a Kantian deontological approach and consider how such approach could
be interpreted and introduced into the fairness metrics ﬁeld.
The use of utilitarian principles in fairness metrics has already been critiqued for the overemphasis
on aggregate beneﬁts, often at the expense of individual rights and dignity. This paper highlights
instances where utilitarian approaches in fairness metrics have been insufﬁcient, suggesting that a
deontological perspective, with its focus on duty and intrinsic value, could offer more balanced and
ethical outcomes.
We present this paper with the following contributions:
• Integration of Kantian Deontology with AI Fairness Metrics The paper provides a novel
perspective by suggesting how to integrate Kantian deontological ethics into the ﬁeld of
AI fairness metrics. This approach contrasts with the prevalent utilitarian focus, offering a
fresh lens to evaluate ethical AI.
• Critical Analysis of Utilitarianism in AI This paper offers a critique of the utilitarian ap-
proach that is predominantly used in AI fairness metrics. This includes an examination
of its limitations, particularly in AI applications with high social impact where individual
rights and intrinsic value have been central.
• Exploration of Practical AI Scenarios Through two case studies on loan approval and stu-
dent grading system, this paper discussed the practical implications of applying Kantian
ethics in real-world AI applications.
1.1
Related Work: Interdisciplinary Perspectives on AI Ethics
Discussions on how to integrate ethical values in AI systems is not unfamiliar and has garnered
signiﬁcant attention from both the AI research community and philosophers, leading to a thriving
ﬁeld of interdisciplinary work. We ﬁrst present the related work of the AI research community
towards ethical practices and then present the efforts of the philosophical community to align with
ethical systems.
2

--- Page 3 ---

1.1.1
AI Research Community’s Developments on Ethics
The AI research community has made substantial contributions regarding the implementation of
moral norms and ethical principles in various contexts; studies such as Wallach and Allen’s explo-
ration of moral machines highlight the complexities of instilling AI with the capacity for moral
decision-making (Wallach and Allen, 2008). There have also been extensive efforts to encode ethi-
cal principles into AI systems, such as Pereira et al.’s work on programming machine ethics which
also addresses practical considerations on encoding principles Pereira et al. (2016). More recent ad-
vancements focus on ensuring AI’s alignment with human values for societal beneﬁt, as exempliﬁed
by London and Heidari (London and Heidari, 2023), and by exploring how to encode societal norms
and moral values into AI systems Serramia et al. (2023); Van de Poel and Royakkers (2023).
One ﬁeld, however, that has not received much attention regarding deontological norms is fair-
ness metrics as its various approaches broadly remain utilitarian (Barocas et al., 2019; Ntoutsi et al.,
2020). In this paper, we criticize the use of utilitarian principles in fairness metrics as they overem-
phasize the advantage of aggregating beneﬁts; we also highlight instances where utilitarian ap-
proaches in fairness metrics have been insufﬁcient, suggesting that a deontological perspective,
with its focus on duty and the intrinsic value of the individual, could offer more balanced and eth-
ical outcomes. In other words, we show that current fairness evaluation metrics of AI systems is
generally biased towards a utilitarian approach for deﬁning morally permissible actions and val-
ues (Cheng and Fleischmann, 2010).
1.1.2
Philosophical Contributions
From a philosophical perspective, scholars like Gabriel have dissected the problem of AI alignment
into two challenges: ﬁrst, the technical challenge of encoding values and second, the normative
challenge of determining which values to encode (Gabriel, 2022, 2020). Conceptualizing fairness as
a moral value in terms of AI has also been explored (Cheng and Fleischmann, 2010). In our work, we
consider Gabriel’s two-step approach and discuss both the current state of the art of fairness metrics
in supervised learning scenarios and their integration and analysis with the Kantian deontological
perspective, a interdisciplinary connection that to the best of our knowledge has not been studied.
Given this gap in the existing contributions, both in AI research and philosophy, this paper aims
to ﬁrst argue that there is a dominant utilitarian approach to AI fairness and then propose a shift to-
wards deontological ethics. The utilitarian approach, while practical, has historically faced criticism,
particularly when it fails to consider the intrinsic value of individuals (e.g., Smart and Williams,
1973; Driver, 2022). While existing works, such as those proposing procedural approaches to fair-
ness (Grgic-Hlaca et al., 2018), have begun to bridge the gap, their philosophical underpinnings
often lack depth. This paper argues for reevaluating this mono-theoretic approach and advocates for
incorporating deontological principles and metrics, particularly in contexts where individual rights
and intrinsic human value are considered paramount.
2
Overview of Kantian Deontology
It is important to ﬁrst reiterate that the primary objective of this paper is not to explore the relation-
ship between utilitarian and deontological moral perspectives with a novel perspective in favour of
deontology. It does not provide an original outlook on the deontology-utilitarianism debate. Indeed,
the following section that outlines the Kantian deontological critique1 of utilitarianism will certainly
be familiar for those with a basic understanding in moral philosophy. The following section in-
stead serves as a reminder of the two opposing normative ethics—one that is society-centred and the
other that is patient-centred—and the main critiques Kantians raise against utilitarianism. It is use-
ful to reiterate this longstanding philosophical debate from the deontological perceptive, which we
will present in the following sections, given the largely mono-theoretic approach taken in fairness
metrics. This paper therefore invites us to reconsider and critique the mono-theoretic approach in
fairness metrics; that despite the ﬁeld generally preferring utilitarianism, there are well-established
critiques laid against utilitarianism by deontologists and that the deontological position can be ben-
eﬁcial for fairness metrics, particularly in the context of jurisdictions that place importance not only
1We chose the Kantian approach for the simple notion that if any philosopher is to be considered as essential
to deontology it is Immanuel Kant.
3

--- Page 4 ---

on measurable outcomes and social impact, but also on inalienable individual rights and the intrinsi-
cally valuable nature of the individual. This refers to the many jurisdictions who recognize that we
have deep-seated duties to each and every individual that evade societal pressures to measure and
prefer collective outcomes, such as the individual right to life and freedom from inhumane treatment,
the right to privacy, and the right to equal treatment before the law. We later provide examples of
where the utilitarian approach in fairness metrics has been largely considered as a failure and where,
we argue, a deontological perspective could have improved the situation.
2.1
The Categorical Imperative
Much can be discussed regarding Kant’s moral theory, but one of the most fundamental aspects of his
ethics, outlined in Groundwork (Kant, 1785), is the categorical imperative. This universal principle,
which unconditionally binds all rational beings, provides us with a formal procedure to evaluate our
actions—if actions adhere to the categorical imperative they are morally ﬁt. Kant provides us with
three primary interpretations of the categorical imperative, with the ﬁrst two being the most widely
discussed.2 The ﬁrst is the Formula of Universal Law:
Act only on a maxim that you can also will to become a universal law (Groundwork, 4:421)3
In other terms, this asks us to consider whether our actions can be performed universally, by all
rational agents, without contradiction. Making false promises cannot be willed universally as if
everyone made false promises, such as falsely promising to pay back a loan, no one would believe
one another as they would distrust everyone and thus, making a false promise would be an impossible
act (4:422).
The second formulation, Formula of Humanity is considered by Kant to be “closer to intuition”
(4:436):
“Act in such a way that you treat humanity, whether in your own person or anyone else’s, never
merely as a means, but also always as an end (4:429)”
This provides us with the material of the moral law (4:436), the rational nature of individuals, or
more speciﬁcally, our free will and humanity, that Kantian ethics aims to protect from any instru-
mental subordination to another individual’s, or group of individuals’, ends. This is to recognize
that all persons are ends-in-themselves, meaning that they have an intrinsic value “exalted above all
price” (4:434). This requires engagement with them as freely-choosing rational agents who have
the capacity to decide what is valuable to them and to pursue their own projects and, importantly,
when they are in a position of not fully realizing this capacity, to provide them with the necessary
assistance (4:430). Returning to the case of the false promise, the categorical imperative forbids it
because it hinges on deceiving another individual and forcing them into a situation for which they
have not principally consented. We primarily focus on this formulation throughout the rest of this
paper.
2.2
Kantian Critique of Utilitarianism
With this concise outline of Kant’s moral law, we now move on to consider the Kantian critique of
utilitarianism. Kant was certainly not fond of taking external concepts, such as happiness, as the
source of morality. In The Metaphysics of Morals he states:
“...if eudaemonism (the principle of happiness) is set up as the basic principle instead of eleutheron-
omy (the principle of the freedom of internal lawgiving), the result is the euthanasia (the death) of
all morals.(Kant and Gregor, 1996, 6:378)”
Kant, however, did not directly address the utilitarian of his time, Jeremy Bentham, so it is helpful
to look to contemporary Kantians, Onora O’Neill and Christine Korsgaard, who provide a direct
critique of utilitarian ethics. The following provides a foundational, but certainly not exhaustive, list
of critiques.
2While there is disagreement on whether or not the formulations are synonymous, they nevertheless all lead
us to the same set of duties (Korsgaard, 1996)
3All further citations of this kind refer to (Kant, 1785)
4

--- Page 5 ---

2.2.1
Critique of the Impersonal Good
The ﬁrst critique is that utilitarianism believes that all moral actions ought to be aimed at obtaining
the ‘good’ as deﬁned as an impersonal absolute value, such as happiness or pleasure, that can be
maximized. It follows that the value of any individual relies on the experience of happiness or plea-
sure. In more crude terms, individuals are a mere vessel for these valuable concepts. Peter Singer
writes that the classical utilitarian approach, “regards sentient beings as valuable only insofar as
they make possible the existence of intrinsically valuable experiences like pleasure.”(Singer, 2011).
Singer, himself a utilitarian, continues this notion that it is not the individuals that matter, but the
deﬁned utility, through the replaceability argument. While he appreciates that all individuals have
inherent worth, this value does not extend far enough to guarantee its protection. Singer has subse-
quently argued that there are circumstances (albeit rare) where killing humans, is the right thing to
do if it brings about more happiness in the community Singer (2011).
This, of course, is in contrast to the second formula of the categorical imperative that stresses that
each individual is intrinsically valuable and is not to be instrumentally subordinated to the well-
being, happiness, or pleasure of others. An individual cannot be replaced by another individual even
if their existence brings about more happiness. This is because Kantians disagree that the ’good’ can
be understood as something abstract and impersonal, something that is simply just ’good’. Rather,
the good is a relational concept because, as Korsgaard argues, all value is tethered. Happiness
or pleasure matters because they are good-for individuals (Korsgaard, 2018). Therefore, crucially,
something can only be considered as universally good when it is good-for everyone, from every
individual’s perspective.
2.2.2
Critique of Aggregating the Good
This brings us to the second critique: the issue of aggregation. Because utilitarians do not consider
individuals as intrinsically valuable, the moral decision procedure thus allows aggregating the good.
There is therefore no prohibition against using individuals, even if they are innocent, as mere means,
as long as the loss of their dignity is for maximizing a sufﬁcient amount of ‘good’ in the community.
Yet, this aggregation does not make sense, not only because it may violate the second formula of the
categorical imperative but also because of the tethered notion of the ‘good’. As Korsgaard contends,
“what is good-for me plus what is good-for you is not necessarily good-for anyone.” (Korsgaard,
2018, p. 157). Moreover, there is a problem when maximizing the good involves taking something
away from an individual: if giving something to Adam brings him more pleasure than it would Eve,
the utilitarian would say we ought to give it to Adam. But this action would just be good-for Adam
and it would be worse-for Eve—it is not better for, or good-for everyone. The good, because it is
tethered, is not something we can aggregate (Korsgaard, 2018). This particularly is more concerning
when those on the receiving end of aggregation are already marginalized individuals.
2.2.3
Critique of the Lack of Robustness
The third critique is that the utilitarian approach of calculating outcomes, whether it be maximizing
beneﬁt or reducing harm, is not a robust approach to identifying which actions should be promoted
or prohibited. As Onora O’Neill points out, circumstances can change the outcome. Take the act of
lying as an example: typically, lying is considered to be harmful and immoral and thus, generally
prohibited. Yet not all lies, such as ‘white lies’, cause harm. The same goes for telling the truth,
which often provides a beneﬁt, but can also inﬂict emotional harm. Focusing on consequences is
unpredictable and, therefore, provides a less robust standard to measure the rightness and wrongness
of actions. The link between harmful consequences and actions is unstable. The connection between
norms, or duties, and actions is a more robust approach to morally evaluating actions. Duties, such
as the duties of civility or to respect the freedom of others, provide a more useful and robust way of
evaluating actions (O’Neill, 2022).
Utilitarianism thus has a limitless scope of acceptable actions as it does not depend on the type
of action but rather the consequence, or utility, it brings about. Being dishonest for the utilitarian,
for example, is not categorically condemned; for this reason, it lacks precision as the rightness or
wrongness of an action can only be determined until after it is carried out and the consequences
are known. The Kantian approach, while it has a more restricted scope given its categorical stance
on duties, provides a precise and fundamental standard of action, where moral authority persists
5

--- Page 6 ---

irrespective of any potential harmful consequence. Being dishonest (to some Kantians) is always
wrong irrespective of unforeseen consequences.
3
Fairness Metrics for Disparate Treatment and Disparate Impact
Transitioning from our review of Kantian deontology, this section shifts focus on to fairness metrics
in supervised learning. We integrate fairness metrics within a structured regulatory framework,
aiming to facilitate the following discussions. With this transition, we can establish connections
with ethical perspectives, laying the groundwork for an examination of disparate treatment/impact
and deontology/utilitarianism in algorithmic decision-making systems.
In the ﬁeld of computer science, researchers have traditionally quantiﬁed various statistical dispar-
ities that exist among protected attributes. These measures are often labelled using terms from
the social sciences (Binns, 2018), such as equal opportunity (Hardt et al., 2016) and equal treat-
ment (Candelas et al., 2023). These notions have subsequently been incorporated into the study
of algorithmic fairness to address historical and systemic biases that can arise in decision-making
systems.
In order to support our subsequent discussions, we now outline the notation we use to deﬁne a subset
of metrics which will be central to our position. Let X and Y be random variables taking values in
X ⊆Rd and Y ⊆R, respectively. A predictor is a function f : X →Y, also called a model. For
conceptual simplicity, the domain of the target feature is dom(Y ) = {0, 1} (binary classiﬁcation).
We assume a feature modelling protected social groups denoted by Z, called protected feature, and
assume it to be binary valued in the theoretical analysis.
In alignment with regulatory frameworks like Title VII of the Civil Rights Act of 1964,
which prohibit discrimination in employment based on protected characteristics like race and
sex (Commission, 1964), we distinguish between two forms of discrimination: disparate treatment,
aiming to prevent intentional model discrimination, and disparate impact, addressing unintentional
effects across subpopulations. The former examines the system’s intentions, focusing on model pre-
dictions fθ(X), while the latter considers effects, interpreted as the error fθ(X) −Y . This work
employs a speciﬁc subset of fairness metrics; for a comprehensive overview, refer to Barocas et al.
(2019).
3.1
Disparate Treatment
A typical disparate treatment case involves intentional discrimination, necessitating users to demon-
strate less favourable treatment motivated by a protected characteristic. To succeed in a disparate
treatment claim, users must show an adverse action taken due to their protected characteristics. We
interpret fairness metrics based on model predictions fθ(X), not model errors ǫ = fθ(X) −Y , as
group fairness metrics measuring disparate treatment. These include:
Deﬁnition 3.1. (Demographic Parity (DP)) A model f achieves demographic parity if f(X) ⊥
Z. We can derive an unfairness metric as d(P(f(X)|Z = z), P(f(X)), where d(·) is a distance
between probability distributions.
Deﬁnition 3.2. (Counterfactual Fairness (CF)). A model fθ is counterfactualy fair if, under any
context X = x and Z = z,P(f Z←z
θ
(x) = y|X = x, Z = z) = P(f Z←z0
θ
(x) = y|X = x, Z =
z)for all y and for any value z0 attainable by Z.(Kusner et al., 2017)
Another type of fairness metric that can potentially align with disparate treatment regulatory frame-
work, but does not explicitly rely on the protected attribute, are individual fairness metrics, which
are grounded in the principle of treating similar individuals equally. These metrics aim to ensure that
any two individuals who exhibit similar characteristics in the context of a speciﬁc algorithmic predic-
tion task are classiﬁed in an identical manner. Metrics such as the Lipschitz condition (Dwork et al.,
2012) and similarity graphs between individuals (Petersen et al., 2021) have been proposed to calcu-
late this in different scenarios.
Deﬁnition 3.3. Individual Fairness A model achieves individual fairness w.r.t. two individual sam-
ples if d(f(x), f(x′)) ≤L · d(x, x′)∀x, x′ ∈X where L > 0 is a constant and d(·, ·) is a distance
function (Petersen et al., 2021)
6

--- Page 7 ---

3.2
Disparate Impact
In contrast to disparate treatment, disparate impact cases do not necessitate proof of intent as the
evaluation shifts towards the discriminatory effects of a seemingly neutral model. Those impacted
through the disparate impact account can build a case, for example, by demonstrating that an em-
ployment practice substantially affects speciﬁc groups. This could manifest in a scenario where a
certain job offers more opportunities to black applicants compared to their white counterparts. Em-
ployment practices that disparately impact disadvantaged racial groups are deemed unlawful, unless
the employer can substantiate their necessity for business reasons (Kim, 2022). We argue that met-
rics relying on model errors align with disparate impact discrimination, thus a utilitarian approach,
and include the following:
Deﬁnition
3.4.
(Equal
Opportunity
(EO))
A
model
f
achieves
equal
opportunity
if
∀z. P(f(X)|Y = 1, Z = z) = P(f(X) = 1|Y = 1). Hardt et al. (2016)
Deﬁnition 3.5. (Accuracy Equality (AE)) A model f achieves accuracy equality if ∀z. ∀i ∈
(0, 1) P(f(X) = i|Y = i, Z = z) = P((X) = i|Y = i). Wachter et al. (2021a)
An instance where a model violates disparate impact without exhibiting disparate treatment can
therefore be illustrated by either a random classiﬁer that uniformly treats all users equally without
regard to input data or an algorithm that automatically approves loans for every applicant. In both
scenarios, errors may vary across subpopulations, thus resulting in disparate impact even though
equal treatment is achieved.
4
Deontological AI Alignment
This section considers the compatibility of Kantian deontological ethics with the ﬁeld of AI fair-
ness and alignment.
We also offer examples of how Kantian ethics can inform AI fairness
metrics.
At the intersection of these two ﬁelds, an existing misalignment has already been
noted (Fazelpour and Lipton, 2020). In light of this, several research lines have proposed various
frameworks to help understand existing notions of algorithmic fairness in moral philosophy terms,
e.g. (Heidari et al., 2019; Simons et al., 2021). In this paper, we argue for aligning fairness metrics
alongside Kantian deontology.
4.1
The Issue of Aggregation
One of the key Kantian critiques charged against utilitarianism is that the utilitarian aggregates the
concept of the ‘good’, which within the statistical learning context inevitably involves optimization
for the overall outcomes at the expense of one or several individuals’ well-being. The intrinsic
value of every individual is set aside in the utilitarian context in favour of accumulating a perceived
external ‘good’, such as happiness or pleasure (cf. Section 2) that is understood as providing some
beneﬁt from the AI applications perspective (London and Heidari, 2023).
When considering group fairness, analyzing an individual through group membership, such as treat-
ing them based on geographical location or immutable characteristics like ethnicity, and subse-
quently optimizing or altering decisions based on the group characteristics, erodes the intrinsic value
of each individual. If we take individuals to be intrinsically valuable, this means that their value is
independent of speciﬁc characteristics; we must not see them as mere parts to be subordinated for
collective or group ends. We must not, according to Kantian principles, deny an individual’s intrin-
sic self-worth by focusing on speciﬁc features to bring about a desired social outcome. The moral
law grants impenetrable worth to each individual and, therefore, every individual is to be treated
as an autonomous entity equal to everyone else. Giving preference to underprivileged groups may,
however, be permitted as the categorical imperative interpreted through the humanity formula rejects
indifference to those in vulnerable circumstances to help them maintain the respect and dignity they
deserve.
This observation underscores the nuanced challenge of measuring group-level fairness aligning with
the preservation of individual rights and dignity, resonating with the Kantian call for how actions
affect each individual. AI system evaluation should underscore the importance of designing fairness
metrics that truly consider the treatment of all individuals and not just a meeting some decision quota
(demographic parity) or achieving similar error rates (equal opportunity) but also look at how each
of the attributes being used contribute to the ﬁnal decision.
7

--- Page 8 ---

4.2
Utilitarian AI Fairness Metrics
This section draws parallels between utilitarian and deontological ethics and the fairness metrics
associated with disparate treatment and disparate impact.
Disparate impact metrics are rooted in measuring error disparities among protected groups. Speciﬁ-
cally, we align metrics of disparate impact such as equal opportunity, Deﬁnition 3.4 (differences in
the True Positive Rates), and accuracy equality Deﬁnition 3.5 (accuracy differences). These metrics
hinge on evaluating outcomes, particularly group disparities of model errors. We thus argue that
these metrics align with a utilitarian approach that focuses on the disparities on the consequences of
the model decisions.
A notable technical limitation is that utilitarian metrics (disparate impact fairness) necessitate la-
belled data for computation. Acquiring labelled data post-deployment poses a considerable chal-
lenge and is often impractical, exhibiting well-known biases, such as confounding, selection, and
missingness (Feng et al., 2023).4 Take, for instance, a loan scenario: to compute the True Posi-
tive Rate, obtaining False Negatives would be essential. This entails acquiring data for individuals
whose model declined a loan but could have repaid it. Privacy concerns, legal constraints, and the
dynamic nature of real-world scenarios compound the difﬁculty in obtaining such post-deployment
data (Pearl et al., 2016; Feng et al., 2023). In many cases, individuals may not be willing to disclose
sensitive information and regulations may limit the collection and use of certain types of data.
In contrast, and in light of our Kantian deontological review, we argue that deontological principles
prioritize assessing model behaviour rather than an exclusive focus on error rates, therefore, aligning
with disparate treatment, metrics such as demographic parity, counterfactual fairness, and individ-
ual fairness. These metrics emphasize the conduct of AI models and align more closely with the
deontological approach.
Consider the example of demographic parity Deﬁnition 3.1, Kantian ethics would generally contend
that an AI model achieves the correct action when its predictions are independent of non-chosen
factors at birth (protected attribute), echoing the categorical imperative (humanity formula) to treat
individuals as ends, never as mere means to an end. As mentioned in the introduction, the deonto-
logical approach aligns well with widely accepted international declarations that recognize a set of
inalienable rights and duties towards the individual, such as the Universal Declaration of Human
Rights. A similar metric introduced by legal scholars aiming to align with the European Court of
Justice “gold standard” (Wachter et al., 2021b) is Conditional Demographic Parity, which extends
Demographic Parity by setting one or more attributes ﬁxed (this only differs on the sense that one or
more additional covariate conditions are added).
Despite ongoing technical challenges, we argue that the pursuit of ethical AI systems may encounter
less technological burden when guided by deontological principles. Unlike utilitarian approaches
that rely on post-deployment data, deontological principles provide a framework based on inher-
ent ethical obligations and duties. This perspective is not as contingent on obtaining speciﬁc post-
deployment data, potentially offering a more straightforward path to ethical alignment in AI systems.
With this in mind, if we examine comprehensive surveys of fairness metrics, such as the one by
Wachter et al. Wachter et al. (2021a), twelve out of the fourteen formalized group fairness metrics
rely on model errors (disparate impact), which we argue is utilitarian. There is, therefore, a dis-
proportionate focus on utilitarian fairness metrics. The other two metrics rely on model behaviour,
aligning with Kantian deontology and disparate treatment notions as outlined in the previous sec-
tion 4.1.
4.3
Balancing Fairness and Performance Metrics
The classical utilitarian approach argues that morality is founded upon the search for the summum
bonum, or the highest form and amount of the good, which, for example, Mill deﬁned as happi-
ness (Mill, 1966). In the context of AI fairness, this ethical pursuit can be likened to a secondary
optimization endeavour after optimization, akin to ﬁne-tuning, where the goal is to achieve fair-
ness in tandem with optimizing model performance. Techniques such as post-processing adjust-
4Confounding Bias: Misleading results due to an unconsidered external variable. Selection Bias: Skewed
results from non-representative data samples.
Missingness Bias: Distortion from systematically absent
data (Good and Hardin, 2012).
8

--- Page 9 ---

ments (Rodolfa et al., 2021) or regularization methods (Zafar et al., 2017, 2019) are normally used
in this secondary optimization stage, aiming to reshape AI systems into less discriminatory entities
while maintaining high-performance algorithms. The literature commonly refers to the concept of
the “Pareto-Frontier”, indicating a model status where enhancing accuracy comes at the cost of fair-
ness, and vice versa (Ho and Xiang, 2020). Any model not situated on the Pareto frontier holds the
potential for fairness improvement without sacriﬁcing accuracy, thereby classifying them as poten-
tial candidates for improvement (Martinez et al., 2020).
This critique ﬁnds relevance in contemporary discussions around group-based fairness metrics in
AI; when optimizing for fairness there is also a need to ensure the protection of individual rights
and dignity. An illustrative example of this concern can be found in Yule’s effect on fairness, as
highlighted by Ruggieri et al Ruggieri et al. (2023):
When pursuing group fairness objectives, such as independence, but failing to
account for the control variable Z, fair machine learning algorithms may inad-
vertently yield disparate effects on distinct distributions. Some subgroups may
beneﬁt positively from these fairness efforts, experiencing higher fairness, while
others may suffer negative consequences, resulting in lower fairness.
However, following the third Kantian critique of utilitarianism (cf Section 2.2.3), we question the
trade-off of maximizing beneﬁt or reducing harm as an approach for determining which actions
should be deemed morally permissible or prohibited. This critique reminds us that focusing on the
consequences may not provide a sufﬁciently robust foundation for determining what constitutes as
ethical decisions and actions, especially in complex domains like AI fairness. As Kant maintained,
individuals ought to be treated as ends in themselves, thus safeguarding their intrinsic worth against
any potential outcomes. In the context of AI fairness, we translate this as post-processing tech-
niques that aim to optimize fairness might violate this principled approach. If the AI fairness metric
approach wishes to align itself with well-established direction of international standards and rights
of the individual, it ought to embrace a Kantian stance within its scope (the one we provide in this
paper) and include equality notions that measure what the model has learnt, focusing on the model
decisions rather than the model errors, i.e. the disparate treatment vs disparate impact approach(cf
Section 3).
4.4
Categorical Imperative as Procedural Fairness
The Kantian deontological perspective proposes that individuals should act according to the vari-
ous formulations of the categorical imperative. This approach to morality is thus procedural. As
Korsgaard argues, the Kantian approach:
“ ...thinks that there are answers to moral questions because there are correct procedures for arriv-
ing at them.”(Korsgaard, 1996, p. 36-37)
With a deontological approach there is a set of procedural principles or rules, such as the categorical
imperative, that provide a systematic method to help us arrive at morally permissible actions.
Applied to AI, this notion encourages developing impartial and equitable ethical procedures across
diverse contexts. This aligns with the notion of procedural fairness that has been introduced in fair
machine learning literature. Procedural fairness relates to the process, not just the model, which
includes the data, processing, and mechanism used to achieve the outcome (Marcinkowski et al.,
2020; Grgic-Hlaca et al., 2018). If we assume that machines are judged against the same standards,
their results will be perceived as fair if people understand that the system meets these same criteria.
Focusing on procedure is a familiar approach as it is also integral to many legal systems; not only the
outcomes but the integrity of due process often deﬁnes the quality of the legal system. For example,
while going to prison is an undesirable outcome, if the procedure leading to this decision was rightly
followed by the lawyers and judge, the decision is more often than not deemed as fair.
Procedural fairness, as seen through the lens of the categorical imperative, underscores the impor-
tance of crafting AI systems that adhere to universal rules and treat all individuals with equal con-
sideration. In practice, this means that the procedures governing AI decision-making should be
free from biases, discrimination, and arbitrary distinctions, not just having an unbiased algorithm.
By upholding principles that transcend speciﬁc circumstances and group identities, AI systems can
9

--- Page 10 ---

align with the moral imperative of treating every individual as an end in themselves, rather than as
a means to an end. Kant’s categorical imperative thus provides a philosophical foundation for pro-
cedural fairness in AI ethics, guiding the development of AI systems that operate within a universal
framework of equitable and just procedures.
5
Aligning with Deontological Principles: Use Cases
In this paper, we have presented an exploration of the intersection between Kantian deontological
ethics and the fairness metrics aiming to align with our ethical values. We have argued not only that
the current approach to fairness metrics disproportionately favours a utilitarian perspective, to the
detriment of not focusing on the conception of the individual that aligns better with individual rights
and established international declarations, but that an alignment with a deontological approach is
feasible. In this section, we discuss two potential use cases aiming to demonstrate the applicability
of Kantian deontological ethics in AI: a loan-granting application using supervised learning and
education and technology applications using generative AI.
5.1
Loan Approval
In the context of loan approvals, AI systems are typically employed to evaluate the creditworthiness
of applicants (Puriﬁcato et al., 2023). These systems rely on historical data and statistical learning
to make decisions and have subsequently raised concerns on the ethical deployment of such tech-
nologies (Vecchione et al., 2021; Dastile et al., 2020). A notable example of this issue was brought
to light by The Markup in 2021 (Martinez and Kirchner, 2021). Their investigation revealed how
a widely used algorithm to help determine mortgage applications in the United States signiﬁcantly
disadvantaged applicants, particularly racial minorities, by exhibiting disparate rejection rates.
The Markup’s analysis underscored the role of the algorithm in reinforcing these disparities. Al-
though human factors, such as loan ofﬁcer bias, play a part, it was evident that the algorithm was
a signiﬁcant contributor to the biased decisions. The study highlighted a speciﬁc trend: applicants
whose primary income source came from the gig economy faced higher rates of loan refusal. This
trend disproportionately affects racial minorities in the U.S., who are more likely to depend on the
gig economy as their primary source of income. The investigation found a signiﬁcant disparity, with
racial minorities being 40 −80% more likely to have their mortgage applications denied. A case in
point was a Black couple in North Carolina. Despite having robust ﬁnancial credentials—high credit
scores, adequate income, and savings exceeding the necessary down payment—they were denied a
loan on the grounds that one of them was a contract worker (Martinez and Kirchner, 2021). This
decision overlooked their overall ﬁnancial stability and reduced their evaluation to a single criterion:
their employment in the gig economy, which was interpreted as indicative of ﬁnancial instability.
The Issue of Aggregation
Traditional loan approval algorithms often optimize for ﬁnancial met-
rics, such as relying on credit scores, income levels, and debt-to-income ratios (Dastile et al., 2020).
When examined through the lens of Kantian deontology, particularly the Formula of Humanity, these
practices require closer scrutiny. The ﬁrst sub-principle of the categorical imperative—avoiding
treating others as “a mere means to an end”—is not violated in voluntary bank-customer transac-
tions as banks are only treating consenting applicants as means to their end and can act to ensure
that the loans they grant will not default. But the second sub-principle—treating others as “ends-in-
themselves”—is morally relevant in this context. Banks can treat applicants as means, but they also
must “harmonize with” or attain “a positive agreement with humanity as an end in itself” (4:430-
431).
Treating others as ends-in-themselves grants intrinsic worth to each individual. This approach means
looking beyond group afﬁliations or categories to which an individual may belong. Recognizing the
identity traits that make each person unique is crucial, rather than reducing them to mere represen-
tatives of these groups. Such a reductionist view not only neglects their unique identity but also
undermines their humanity. In the Kantian view, the collective ensemble of these diverse identity
traits imbues an individual with impenetrable value. Hence, selecting statistics of individuals by
their group characteristics is not only reductive but also ethically ﬂawed, as it fails to honor their
complex and singular nature as human beings.
10

--- Page 11 ---

In this loan approval context, (i) Avoiding Group Representations becomes crucial. Decision-making
should not be solely based on group characteristics, including the status as a gig worker or assump-
tions based on gender or ethnicity. These attributes viewed individually, which are often not up to
the individual’s choice, are not reﬂective of an individual’s entire identity and capabilities and could
lead to unequal treatment. In the case of the loan through the Kantian deontological lens, each appli-
cant deserves a holistic and equal evaluation, resonating with the principle of respecting each person
as an end in themselves. (ii) Beyond Financial Metrics: An over-reliance on statistical correlations
drawn from employment stability, educational background, or community involvement can lead to
biases and misrepresentations. These factors, while potentially indicative of ﬁnancial capabilities,
do not capture the entirety of an individual’s ability to repay a loan. This is evident in The Markup’s
case study where the couple, despite having high credit scores, six-ﬁgure incomes, and substantial
savings, even paying rent higher than their prospective mortgage payments, were narrowly evaluated
on their employment status. Such a reductionist approach contravenes Kant’s principle of treating
individuals as ends in themselves, failing to consider their unique combination of traits that can more
collectively determine their creditworthiness.
Utilitarian Metrics and the Challenge of Denied Loan Applications
The ethical complexity of
measuring utilitarian fairness metrics in loan scenarios lies in the difﬁculty of accurately identifying
model errors such as false negatives, i.e. individuals who would have successfully repaid a loan but
were initially denied by the model. To determine false negatives, it would require extending loans to
those previously denied by the AI system, an approach fraught with ﬁnancial risks, potential biases,
and legal implications, in some cases illegal (Feng et al., 2023). This paper argues that reliance on
metrics that do not depend on post-deployment labelled data may be more effective both in practice
and resonate with the principles of Kantian deontology. Such metrics, which focus on the ethical
treatment of individuals by the model rather than the consequences of the model predictions, offer
a more viable, pragmatic, and deontologically aligned approach. Deontological fairness metrics
circumvent the complexities and ethical dilemmas inherent in utilitarian measures that depend on
outcomes, particularly in scenarios where gathering accurate post-deployment data is impractical or
unethical.
Balancing Fairness and Performance Metrics
Financial systems are often designed to
maximize ﬁnancial gain without considering fairness metrics.
An alternative perspec-
tive (Papageorgiou and Mougan, 2023), in line with German jurisprudence (BGB, 2023; KWG,
2023), which suggests that degrading performance, such as approving loans for initially unquali-
ﬁed applicants, might be legally questionable. Aligning loan approvals with Kantian deontology
may not necessarily entail a trade-off between fairness and performance as deontological metrics do
not rely on error rates, which do not need changes in the optimization. Recent research by Rodolfa
et al. Rodolfa et al. (2021) has argued that by modifying the threshold on the model decision, negli-
gible fairness-tradeoff can be obtained,5 contrary to the premise that ethical principles must always
compete with optimization metrics. It might, therefore, be feasible to design AI systems where ethi-
cal treatment of individuals and effective ﬁnancial management are not mutually exclusive goals but
complementary objectives.
Procedural Fairness.
In line with the Kantian emphasis on procedural ethics, the process of how
the AI system makes decisions is as, or perhaps even more, important as the decision itself. This
involves ensuring that the whole pipeline is up to ethical standards, for example, that the data gath-
ering/collection process meets general data protection requirements, that the training data for the
model is non-biased and representative of the population, the algorithm is audited for fairness, and
that there are mechanisms in place for applicants to appeal or question decisions (Ntoutsi et al.,
2020). Therefore, an AI system is designed to adhere to procedural fairness if the whole pipeline
meets speciﬁc ethical requirements rather than just emphasizing the need to achieve fairness metrics
standards (disparate impact).
5It’s important to note, especially in contexts like the US and UK, that the use of protected characteristics
in decision-making is largely restricted, except under speciﬁc, limited conditions (Belz, 1991; Fredman, 2014)
11

--- Page 12 ---

5.2
Students Grading System: Ofqual
The Ofqual exam grading controversy in 2020 in the UK involved the use of an algorithm to deter-
mine ﬁnal student grades during the pandemic when traditional exam-sitting (A-level exams) was
unavailable, and were subsequently criticized for, amongst other reasons, being unfair and biased
against students from disadvantaged backgrounds (Benjamin, 2022). The algorithm was intended to
predict student grades based on a combination of historical grade distribution and performance data,
student rank in the school from teacher assessments, and previous exam results (Kolkman, 2020;
Heaton et al., 2023). This, however, led to widespread dissatisfaction among students, parents, and
educators due to its apparent systemic biases and inaccuracies. We will discuss this incident through
the lens of Kantian deontology.
The Issue of Aggregation
Kantian deontology emphasizes the intrinsic value of each individual,
treating them as ends in themselves and not merely as means to an end. In the Ofqual case, the
algorithm’s reliance on historical data from schools led to individual students being largely judged
not on their own merit but based on the performance of their predecessors. Furthermore, the usage
of statistical aggregations and features that have a relation with controversial variables, such as the
school to which a student belongs, impacted the model. This contradicts the Kantian principle to
recognize the intrinsic worth of each individual.
“There is sometimes a danger where you have an exceptionally high-performing child in a
low-performing school to be in a situation where they don’t get the grades that they want
to.” (Adams et al., 2020)
This statement by politician Gavin Williamson in an interview with LBC underscores the issue of
aggregating individual performances, potentially compromising the well-being of standout individ-
uals simply for belonging to an institution. The algorithm’s reliance on past school results failed to
recognize each student as a unique individual with distinct potentials and achievements.
Utilitarian Metrics
Public discourse, particularly in social media and news outlets, evaluated the
Ofqual algorithm by comparing its predictions with the previous year’s results. For instance, The
Guardian reported, “The proportion of girls in England awarded A or above rose from 25% to 28%,
overtaking that of boys, who received A or above for 27% of their entries.” (Adams et al., 2020)
This evaluation aligns more with a deontological perspective, as it focuses on the fairness of the
model’s decisions rather than its consequences. A utilitarian approach would require gathering real
student data, which was the original problem the machine learning model was trying to solve: avoid
examining students in an open classroom due to COVID-19 pandemic restrictions. Additionally,
conducting in-person exams might have introduced ethical concerns, as students evaluated algorith-
mically and those assessed in person would have faced different opportunities, potentially violating
principles of equal academic treatment.
Balancing Fairness and Performance Metrics
The Ofqual scenario underscores a critical
dilemma in the use of AI techniques for decision-making: the trade-off between algorithmic efﬁ-
ciency and fairness. While the Ofqual algorithm demonstrated efﬁciency by rapidly processing a
vast number of grades, it incorporated historical biases and systemic disadvantages, bringing in-
herent conﬂict in the trade-off between performance and fairness. In line with Kantian ethics, the
trade-off between performance and fairness cannot be the sole criterion for ethical validation in AI
applications, raising a fundamental question: should AI techniques even be employed in student grad-
ing contexts? This is especially pertinent given that after public outrage, students instead received
grades solely based on their teacher’s estimate of what their grade would have been. The Ofqual
experience serves as a cautionary tale, highlighting the need for a reﬂection on whether the usage
of AI systems for automation actually improves societal aspects, even when considering “fairness
metrics”.
Categorical Imperative as Procedural Fairness
Kantian deontology emphasizes the value of
process over outcomes. Procedural fairness, within AI, extends beyond the statistical difference in
the model predictions (fairness metrics), but requires that the full process of making predictions
respects a set of ethical principles. For example, fairness metrics that focus solely on the consistent
functioning of an algorithm with respect to two protected groups may overlook crucial aspects of
12

--- Page 13 ---

discrimination or bias in the step data gathering or data processing. A principle like the categorical
imperative compels us to consider that a system is ethically engineered if each of the steps needed
towards making a prediction (Burkov, 2020; Huyen, 2022) are grounded in moral principles. Within
AI research, while questions of distributive justice, such as equitable outcomes, receive signiﬁcant
attention, procedural justice is often relegated to a secondary status. From a Kantian perspective,
however, ensuring procedural justice is paramount. This involves scrutinizing the data used for
training algorithms, the assumptions and values embedded in these systems, and the transparency
and accountability of the algorithmic processes. It is about ensuring that these systems are not only
fair in what they distribute (outcomes), but also how they operate (processes).
6
Conclusion
This paper examined the compatibility of Kantian deontology with AI alignment with fairness met-
rics. We ﬁrst revisited the Kantian critique of utilitarianism, which prioritizes outcomes, and ex-
plored its relevance to AI fairness. The Kantian framework emphasizes treating individuals as ends
in themselves, aligning with the foundational principles of fairness in AI that seek equitable and just
treatment for all, irrespective of group identities and model errors.
The current landscape of AI fairness metrics, however, primarily focuses on optimizing outcomes
and reducing disparities in model errors, which is more in line with utilitarian principles. The
longstanding Kantian critique of this approach reminds us of the need for a deeper examination of the
moral principles underlying fairness in AI. The deontological approach also supports a procedural
fairness framework for AI ethics, highlighting the importance of impartial and equitable procedures
in AI decision-making. This aligns with the established concept of procedural fairness in AI ethics,
ensuring that AI systems uphold universal principles of equitable treatment and respect for individual
dignity. By integrating Kantian ethics into AI alignment, we not only bring in a widely-accepted
prominent moral theory but also strive for a more morally grounded AI landscape that better balances
outcomes and procedures in pursuit of fairness and justice.
Researcher Positionality Statement
Our backgrounds and experiences coming from Western ed-
ucation signiﬁcantly inﬂuenced the trajectory of this work. As interdisciplinary researchers, our
diverse perspectives enriched the examination of Kantian deontological ethics in the context of AI
fairness. Drawing from interdisciplinary backgrounds, including philosophy and computer science,
we integrated moral theories into technical domains. Acknowledging our own positions, we recog-
nize the importance of context-speciﬁc interpretations of Kantian ethics in different sociocultural
settings.
Adverse Impact Statement
While we believe our exploration of Kantian deontological ethics in
AI alignment fairness metrics contributes valuable insights, we acknowledge the potential adverse
impacts of our work. One unintended consequence may be the oversimpliﬁcation of ethical consider-
ations in AI systems, as Kantian ethics may not comprehensively address the dynamic and evolving
nature of technological landscapes. This oversimpliﬁcation could lead to a rigid application of eth-
ical principles, potentially hindering the adaptability of AI systems in diverse contexts. Moreover,
the dissemination of our ﬁndings may inadvertently contribute to a narrow focus on deontological
approaches, therefore overshadowing the importance of a holistic ethical framework that integrates
multiple perspectives. We caution against the uncritical adoption of our proposed framework and
urge for ongoing dialogue and adaptation to ensure that AI ethics remains responsive to emerging
challenges and ethical considerations.
References
Adams, R., Weale, S., and Barr, C. (2020). A-level results: almost 40% of teacher assessments in
england downgraded. The Guardian.
Barocas, S., Hardt, M., and Narayanan, A. (2019). Fairness and Machine Learning: Limitations
and Opportunities. fairmlbook.org. http://www.fairmlbook.org.
Belz, H. (1991). Equality transformed: A quarter-century of afﬁrmative action, volume 15. Trans-
action Publishers.
13

--- Page 14 ---

Benjamin, G. (2022). #fuckthealgorithm: algorithmic imaginaries and political resistance. In FAccT
’22: 2022 ACM Conference on Fairness, Accountability, and Transparency, Seoul, Republic of
Korea, June 21 - 24, 2022, pages 46–57. ACM.
Bentham, J. (1996). The collected works of Jeremy Bentham: An introduction to the principles of
morals and legislation. Clarendon Press.
BGB (2023). German civil code (b¨urgerliches gesetzbuch - bgb, federal law gazette. Accessed on
2023-10-01.
Binns, R. (2018). Fairness in machine learning: Lessons from political philosophy. In FAT, vol-
ume 81 of Proceedings of Machine Learning Research, pages 149–159. PMLR.
Burkov, A. (2020). Machine Learning Engineering. Kindle Direct Publishing, 1 edition.
Candelas, J. Q., Wu, Y., Hsu, B., Jain, S., Ramos, J., Adams, J., Hallman, R., and Basu, K. (2023).
Disentangling and operationalizing AI fairness at linkedin. In FAccT, pages 1213–1228. ACM.
Cheng, A. and Fleischmann, K. R. (2010). Developing a meta-inventory of human values. In ASIST,
volume 47 of Proc. Assoc. Inf. Sci. Technol., pages 1–10. Wiley.
Commission, U. E. E. O. (1964). Title vii of the civil rights act of 1964. Public Law 88-352, 78 Stat.
241, 42 U.S.C. § 2000e et seq.
Dastile, X., C¸ elik, T., and Potsane, M. (2020). Statistical and machine learning models in credit
scoring: A systematic literature survey. Appl. Soft Comput., 91:106263.
Driver, J. (2022). The History of Utilitarianism. In Zalta, E. N. and Nodelman, U., editors, The
Stanford Encyclopedia of Philosophy. Metaphysics Research Lab, Stanford University, Winter
2022 edition.
Dwork, C., Hardt, M., Pitassi, T., Reingold, O., and Zemel, R. S. (2012). Fairness through awareness.
In Goldwasser, S., editor, Innovations in Theoretical Computer Science 2012, Cambridge, MA,
USA, January 8-10, 2012, pages 214–226. ACM.
Fabbrizzi, S., Zhao, X., Krasanakis, E., and et al. (2023). Studying bias in visual features through
the lens of optimal transport. Data Mining and Knowledge Discovery.
Fazelpour, S. and Lipton, Z. C. (2020). Algorithmic fairness from a non-ideal perspective. In AIES,
pages 57–63. ACM.
Feng, J., Subbaswamy, A., Gossmann, A., Singh, H., Sahiner, B., Kim, M.-O., Pennello, G., Petrick,
N., Pirracchio, R., and Xia, F. (2023). Towards a post-market monitoring framework for machine
learning-based medical devices: A case study. In NeurIPS 2023 Workshop on Regulatable ML.
Fredman, S. (2014). Addressing disparate impact: Indirect discrimination and the public sector
equality duty. Industrial Law Journal, 43(3):349–363.
Gabriel, I. (2020). Artiﬁcial intelligence, values, and alignment. Minds Mach., 30(3):411–437.
Gabriel, I. (2022). Toward a theory of justice for artiﬁcial intelligence. Daedalus, 151(2):218–231.
Good, P. I. and Hardin, J. W. (2012). Common errors in statistics (and how to avoid them). John
Wiley & Sons.
Goodin, R. E. (1995). Utilitarianism as a public philosophy. .
Grgic-Hlaca, N., Zafar, M. B., Gummadi, K. P., and Weller, A. (2018). Beyond distributive fairness
in algorithmic decision making: Feature selection for procedurally fair learning. In AAAI, pages
51–60. AAAI Press.
Hardt, M., Price, E., and Srebro, N. (2016). Equality of opportunity in supervised learning. In NIPS,
pages 3315–3323.
Heaton, D., Nichele, E., Clos, J., and Fischer, J. E. (2023). “the algorithm will screw you”: Blame,
social actors and the 2020 a level results algorithm on twitter. Plos one, 18(7):e0288662.
14

--- Page 15 ---

Heidari, H., Loi, M., Gummadi, K. P., and Krause, A. (2019). A moral framework for understanding
fair ML through economic models of equality of opportunity. In danah boyd and Morgenstern,
J. H., editors, Proceedings of the Conference on Fairness, Accountability, and Transparency, FAT*
2019, Atlanta, GA, USA, January 29-31, 2019, pages 181–190. ACM.
Ho, D. E. and Xiang, A. (2020). Afﬁrmative algorithms: The legal grounds for fairness as awareness.
U. Chi. L. Rev. Online, page 134.
Huyen, C. (2022). Designing Machine Learning Systems: An Iterative Process for Production-
Ready Applications. O’Reilly.
Kamishima, T., Akaho, S., Asoh, H., and Sakuma, J. (2012). Fairness-aware classiﬁer with prejudice
remover regularizer. In ECML/PKDD (2), volume 7524 of Lecture Notes in Computer Science,
pages 35–50. Springer.
Kant, I. (1785). Groundwork of the Metaphysics of Morals. Cambridge University Press.
Kant, I. and Gregor, M. J. (1996). Groundwork of the metaphysics of morals: Practical philosophy.
Trans MJ Gregor (Cambridge University Press, Cambridge, 1996), 4(456):p102.
Kim, P. T. (2022). Race-aware algorithms: Fairness, nondiscrimination and afﬁrmative action. Cal-
ifornia Law Review, 110.
Knutsson, S. (2016). Measuring happiness and suffering. Foundational Research Institute.
Kolkman, D. (2020). F** k the algorithm?: what the world can learn from the uk’s a-level grading
ﬁasco. Impact of Social Sciences Blog.
Korsgaard, C. M. (1996). The sources of normativity. Cambridge University Press.
Korsgaard, C. M. (2018). Fellow creatures: Our obligations to the other animals. Oxford University
Press.
Kusner, M. J., Loftus, J. R., Russell, C., and Silva, R. (2017). Counterfactual fairness. In NIPS,
pages 4066–4076.
KWG (2023). Banking act (kreditwesengesetz - kwg), bundesministerium f¨ur justiz. Accessed on
2023-10-01.
Kymlicka, W. (2002). Contemporary political philosophy: An introduction. oxford: oxford Univer-
sity Press.
London, A. J. and Heidari, H. (2023). Beneﬁcent intelligence: A capability approach to modeling
beneﬁt, assistance, and associated moral failures through ai systems.
Macleod, C. (2020). John Stuart Mill. In Zalta, E. N., editor, The Stanford Encyclopedia of Philoso-
phy. Metaphysics Research Lab, Stanford University, Summer 2020 edition.
Marcinkowski, F., Kieslich, K., Starke, C., and L¨unich, M. (2020). Implications of AI (un-)fairness
in higher education admissions: the effects of perceived AI (un-)fairness on exit, voice and orga-
nizational reputation. In FAT*, pages 122–130. ACM.
Martinez, E. and Kirchner, L. (2021). The secret bias hidden in mortgage-approval algorithms. The
Markup.
Martinez, N., Bertran, M., and Sapiro, G. (2020). Minimax pareto fairness: A multi objective
perspective. In III, H. D. and Singh, A., editors, Proceedings of the 37th International Conference
on Machine Learning, volume 119 of Proceedings of Machine Learning Research, pages 6755–
6764. PMLR.
Menon, A. K. and Williamson, R. C. (2018). The cost of fairness in binary classiﬁcation. In FAT,
volume 81 of Proceedings of Machine Learning Research, pages 107–118. PMLR.
Mill, J. S. (1966). Utilitarianism. Springer.
15

--- Page 16 ---

Ntoutsi, E., Fafalios, P., Gadiraju, U., Iosiﬁdis, V., Nejdl, W., Vidal, M., Ruggieri, S., Turini, F.,
Papadopoulos, S., Krasanakis, E., Kompatsiaris, I., Kinder-Kurlanda, K., Wagner, C., Karimi,
F., Fern´andez, M., Alani, H., Berendt, B., Kruegel, T., Heinze, C., Broelemann, K., Kasneci,
G., Tiropanis, T., and Staab, S. (2020). Bias in data-driven artiﬁcial intelligence systems - an
introductory survey. WIREs Data Mining Knowl. Discov., 10(3).
O’Neill, O. (2022). A philosopher looks at digital communication, volume 4. Cambridge University
Press.
Papageorgiou, I. and Mougan, C. (2023). Necessity of processing sensitive data for bias detection
and monitoring: A techno-legal exploration. In NeurIPS 2023 Workshop on Regulatable ML.
Pearl, J., Glymour, M., and Jewell, N. P. (2016). Causal inference in statistics: A primer. John
Wiley & Sons.
Pedreschi, D., Ruggieri, S., and Turini, F. (2008). Discrimination-aware data mining. In KDD, pages
560–568. ACM.
Pereira, L. M., Saptawijaya, A., et al. (2016). Programming machine ethics, volume 26. Springer.
Petersen, F., Mukherjee, D., Sun, Y., and Yurochkin, M. (2021). Post-processing for individual
fairness. In NeurIPS, pages 25944–25955.
Posner, R. A. (1979). Utilitarianism, economics, and legal theory. The Journal of Legal Studies,
8(1):103–140.
Puriﬁcato, E., Lorenzo, F., Fallucchi, F., and Luca, E. W. D. (2023). The use of responsible artiﬁcial
intelligence techniques in the context of loan approval processes. Int. J. Hum. Comput. Interact.,
39(7):1543–1562.
Rodolfa, K. T., Lamba, H., and Ghani, R. (2021). Empirical observation of negligible fairness-
accuracy trade-offs in machine learning for public policy. Nat. Mach. Intell., 3(10):896–904.
Ruggieri, S., ´Alvarez, J. M., Pugnana, A., State, L., and Turini, F. (2023). Can we trust fair-ai? In
AAAI, pages 15421–15430. AAAI Press.
Serramia, M., Rodriguez-Soto, M., and Lopez-Sanchez, Marco, e. a. (2023). Encoding ethics to
compute value-aligned norms. Minds & Machines.
Simons, J., Bhatti, S. A., and Weller, A. (2021). Machine learning and the meaning of equal treat-
ment. In Fourcade, M., Kuipers, B., Lazar, S., and Mulligan, D. K., editors, AIES ’21: AAAI/ACM
Conference on AI, Ethics, and Society, Virtual Event, USA, May 19-21, 2021, pages 956–966.
ACM.
Singer, P. (2011). Practical Ethics. Cambridge University Press, 3rd edition.
Smart, J. J. C. and Williams, B. (1973). Utilitarianism: For and against. Cambridge University
Press.
Van de Poel, I. and Royakkers, L. (2023). Ethics, technology, and engineering: An introduction.
John Wiley & Sons.
Vecchione, B., Levy, K., and Barocas, S. (2021). Algorithmic auditing and social justice: Lessons
from the history of audit studies. In Equity and Access in Algorithms, Mechanisms, and Optimiza-
tion, pages 1–9. EEAMO’21.
Wachter, S., Mittelstadt, B., and Russell, C. (2021a). Bias preservation in machine learning: The
legality of fairness metrics under eu non-discrimination law. West Virginia Law Review, 123(3).
Wachter, S., Mittelstadt, B., and Russell, C. (2021b). Why fairness cannot be automated: Bridging
the gap between eu non-discrimination law and ai. Computer Law & Security Review, 41:105567.
Wallach, W. and Allen, C. (2008). Moral machines: Teaching robots right from wrong. Oxford
University Press.
16

--- Page 17 ---

Watson, L. (2021). The right to know: Epistemic rights and why we need them. Routledge.
Zafar, M. B., Valera, I., Gomez-Rodriguez, M., and Gummadi, K. P. (2017). Fairness constraints:
Mechanisms for fair classiﬁcation. In AISTATS, volume 54 of Proceedings of Machine Learning
Research, pages 962–970. PMLR.
Zafar, M. B., Valera, I., Gomez-Rodriguez, M., and Gummadi, K. P. (2019). Fairness constraints: A
ﬂexible approach for fair classiﬁcation. J. Mach. Learn. Res., 20:75:1–75:42.
17

```
