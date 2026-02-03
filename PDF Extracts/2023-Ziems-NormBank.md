---
title: "NormBank - PDF Extract"
source_pdf: "2023-Ziems-NormBank.pdf"
pages: 20
extracted_at: "2026-01-24T17:05:26.281933"
---

# PDF Extract: NormBank

**Source PDF:** 2023-Ziems-NormBank.pdf
**Total Pages:** 20

---

## Content

```
--- Page 1 ---

NORMBANK: A Knowledge Bank of Situational Social Norms
Caleb Ziems
Jane Dwivedi-Yu
Yi-Chia Wang
Alon Y. Halevy
Diyi Yang
Stanford University,
Meta AI
{cziems, diyiy}@stanford.edu, {janeyu, yichiaw, ayh}@fb.com
Abstract
We present NORMBANK, a knowledge bank
of 155k situational norms. This resource is
designed to ground flexible normative reason-
ing for interactive, assistive, and collabora-
tive AI systems. Unlike prior commonsense
resources, NORMBANK grounds each infer-
ence within a multivalent sociocultural frame,
which includes the setting (e.g., restaurant),
the agents’ contingent roles (waiter, customer),
their attributes (age, gender), and other phys-
ical, social, and cultural constraints (e.g., the
temperature or the country of operation). In
total, NORMBANK contains 63k unique con-
straints from a taxonomy that we introduce
and iteratively refine here. Constraints then
apply in different combinations to frame so-
cial norms. Under these manipulations, norms
are non-monotonic — one can cancel an in-
ference by updating its frame even slightly.
Still, we find evidence that neural models can
help reliably extend the scope and coverage
of NORMBANK. We further demonstrate the
utility of this resource with a series of transfer
experiments. For data and code, see https:
//github.com/SALT-NLP/normbank
1
Introduction
As AI systems continually evolve for human as-
sistance and collaboration, they will increasingly
operate within cultural and social spaces, and re-
quire increasingly robust and flexible knowledge
of social norms (Carlucci et al., 2015). From dia-
logue systems (Molnár and Szüts, 2018; Vaidyam
et al., 2019; Bavaresco et al., 2020; Grossman et al.,
2019) to socially interactive robots (Fong et al.,
2003; Deng et al., 2019) and augmented or mixed
reality technologies (Anderson and Rainie, 2022),
each could benefit from understanding how humans
effectively communicate, make decisions, engage
with requests, and broadly interact with others (Sun-
stein, 1996; Sherif and Sherif, 1953).
Work done at Meta AI Research
Figure 1: What is special about NORMBANK? Norms
are grounded by situational constraints—environmental
and personal attributes, as well as roles and other behav-
iors. In this example, drinking coffee is an encouraged
activity in its prototypical context, for a customer in a
cafe, but it is counternormative for a working barista to
do so in the same cafe, or for a child-age student do so
in a classroom. These represent only some of the non-
monotonic normative inferences that are represented in
NORMBANK.
arXiv:2305.17008v2  [cs.CL]  24 Jul 2023

--- Page 2 ---

Natural language is flexible and highly expres-
sive; thus it is a promising medium for encoding
knowledge of social norms (Sap et al., 2019a). The
goal of this work is to construct NORMBANK, a nat-
ural language bank of social norms that will allow
AI systems to reason about social situations under
complex constraints. NORMBANK encodes 155k
norms via scalable human annotation, bootstrapped
with implicit knowledge from large pre-trained lan-
guage models (LLMs).
NORMBANK factors in two important consider-
ations that have been previously overlooked. First:
norms are not rigid truths; they are flexibly as-
sumed standards that may be updated with new
information from the social context (Blass and Hor-
swill, 2015). Second: this social context is not
a flat list of facts but a matrix of hierarchical de-
pendencies (Hovy and Yang, 2021). These two
considerations have important design implications
for norm representations and reasoning in AI, in-
spiring two objectives for this work.
Objective 1 is to support non-monotonic reason-
ing (Reiter, 1981) over defeasible (Pollock, 1987)
norms. This means inferences that hold under most
cases can be updated or even retracted based on
new information. For example, dancing is a posi-
tive behavior that is generally permitted in many
casual settings and in many cultures.
We can
still strengthen or cancel this inference. On the
one hand, dancing is expected from a professional
dancer. But in an Islamic cultural context, indi-
viduals are forbidden from publicly dancing with
members of the opposite sex. In a hospital setting,
a young child is allowed to dance in the waiting
room, but this behavior would not be expected from
an adult visiting a dying relative. For more exam-
ples, see Figure 1. This kind of reasoning will not
always follow straightforward compositional logic
(Klimczyk, 2021), and we expect it to be a chal-
lenge for AI systems.1 NORMBANK is the first
data resource to support non-monotonic normative
reasoning by encoding contrasting situations un-
der which the same behavior could alternatively be
expected or considered taboo (see §4).
There is a combinatorially explosive space of
situational contexts, each with non-compositional
and thus unpredictable norms. Enumerating the set
of all possible constraints is intractable. To effi-
1Typically, it’s okay to drink soda while actively work-
ing and it’s okay for a waiter to drink soda; yet the inter-
section of these conditions is not typical. It is NOT okay for
a waiter to drink soda while actively working.
ciently learn norms in this space, models can rely
on the regularizing effects of hierarchical organi-
zation and social theory. NORMBANK introduces
hierarchical organization (Objective 2) by means
of a rich taxonomy over the relevant contextual
signals that inform behaviors.
Our new SCENE taxonomy is the first to use
Goffman’s (1959) dramaturgical theory of social
life. We operationalize the theory with settings that
have additional environmental constraints. In each
setting, there are agents with different roles and
attributes, who then perform behaviors. Norms ap-
ply to behaviors in certain situations. For example,
in Figure 1, norms around drinking hot coffee differ
for agents with different roles (e.g., barista, cus-
tomer) and attributes (e.g., adult, child), in different
settings (e.g., cafe, classroom).
Having addressed the objectives above, we train
neural models to expand NORMBANK with auto-
matic knowledge completion. Experiments show
promising results: these models can extrapolate
social commonsense to new behaviors in new sit-
uations, leveraging similarities in analogous roles
across different situations. Finally, we demonstrate
how to transfer knowledge via sequential finetun-
ing from NORMBANK to social reasoning tasks.
Together, knowledge completion and transfer learn-
ing suggest that our dataset will serve as a use-
ful resource for advancing neural models toward
situationally-grounded social reasoning.
2
Related Work
Commonsense knowledge bases
(CSKBs) are
sets of structured knowledge about everyday life.
They capture broad taxonomic relationships (Liu
and Singh, 2004; Speer et al., 2017; Elsahar et al.,
2018), logical relations (Lenat, 1995; Zhang et al.,
2018), and universal laws of causality and phys-
ical mechanics (Talmor et al., 2019; Bisk et al.,
2020). More recent datasets encode social mechan-
ics, like broad human values (Ziems et al., 2022;
Hendrycks et al., 2021), norms (Forbes et al., 2020;
Fung et al., 2022), and typical rules of social behav-
ior and motivation (Sap et al., 2019a; Huang et al.,
2019). NormBank specifically centers social norms
around dramaturgical settings (i.e., places of wor-
ship, commerce, and recreation). Just as ATOMIC
(Sap et al., 2019a) seeded Social IQa (Sap et al.,
2019b) and δ-NLI (Rudinger et al., 2020), we antic-
ipate that NormBank can be converted into bench-
marking tasks, plus injected into language models

--- Page 3 ---

for downstream applications (Chang et al., 2020;
Mitra et al., 2019; Ji et al., 2020a,b).
Norm discovery
is an emerging method in-
spired by automatic knowledge base construction
(Mitchell et al., 2015; Weston et al., 2013; Craven
et al., 2000) and extracting social knowledge from
LLMs via prompting (Trinh and Le, 2018; Petroni
et al., 2019; Wang et al., 2019; Sakaguchi et al.,
2020). In concurrent work, Fung et al. (2022)
propose NORMSAGE, which automatically dis-
covers mandated or conventional behaviors from
dialogues. Their prompts resemble our bootstrap-
ping efforts in §3, with the added step of automatic
self-verification. NORMBANK differs from NORM-
SAGE in that we rely on human annotation to col-
lect more creatively non-prototypical situations to
challenge and expand normative reasoning models.
Normative reasoning
systems like Delphi (Jiang
et al., 2021), and UNICORN (Lourie et al., 2021a)
are pre-trained on existing social knowledge bases
(Forbes et al., 2020; Emelin et al., 2021; Hendrycks
et al., 2021; Lourie et al., 2021b; Sap et al., 2020),
which contain more conventional social behaviors
from narrative contexts. Until Pyatkin et al. (2022),
in work concurrent to our own, descriptive social
reasoning systems have been framed as universal
oracles with forced-choice judgments about human
behaviors (Talat et al., 2022). These models lack
the capacity for defeasible reasoning (Madaan et al.,
2021; Rudinger et al., 2020). Oracles instead tend
to assume the most prototypical contexts (Boratko
et al., 2020). Many of these predictions will appear
reasonable if we pragmatically infer a conventional
narrative, but for systems to achieve robust social
intelligence, they must account for the long tail of
the distribution. We can easily find unconventional
contexts in which the correct inference contained in
NORMBANK is misunderstood by current models.2
3
SCENE: A Dramaturgical Framework
The self... is a dramatic effect arising
diffusely from a SCENE.
— Erving Goffman (1959)
To help models efficiently learn non-monotonic
normative reasoning over a seemingly unbounded
2For example, Delphi believes yelling and clenching your
fists, breathing heavily, or asking someone personal ques-
tions about their sex life are all conventionally inappropriate.
NORMBANK gives acceptable contexts for each: guests riding
a roller coaster, athletes running track, and doctors perform-
ing routine checkups, respectively.
set of possible contexts, and to test this understand-
ing in LLMs, we will need to establish a more
tractable set of elements to represent this social ma-
trix. For this purpose, we construct a hierarchical
taxonomy of constraints, which we call Situational
Constraints for social Expectations, Norms, and
Etiquette (SCENE for short). SCENE follows Goff-
man’s (1959) dramaturgical model of social life.
According to this model, people are like actors try-
ing to maintain a social performance in front of an
audience. Each actor performs a particular role as
if in a scene from a movie. The scene is grounded
in a particular setting, which includes aspects of
the environment that inform the performance. Each
scene also has a script (Schank and Abelson, 1977),
which tells the actor what kinds of behaviors will
be perceived as in-character or out-of-character.
Additionally, the actor will embody socially mean-
ingful attributes like age, gender, status, etc. These
attributes may be relevant to the scene and the ac-
tors place in it. In Figure 2, the example setting is
a restaurant where the environment is uncrowded
and the hour is night. There are two primary roles
of customer and server, and for norm formation,
some relevant attributes include their respective
genders, sexualities, and ages, which parameterize
the behaviors that are appropriate for this dinner,
such as dating and drinking alcohol.
Settings
(e.g., banks, classrooms, homes, hos-
pitals) are the loci of scripted social interactions
(Schank and Abelson, 1977), and they frame all
subsequent elements of NORMBANK, so we begin
here with 129 distinct settings like amusement park,
bus, and elevator. Settings derive from two popular
knowledge resources. First, there are 80 settings
from from ConceptNet (Speer et al., 2017), a broad
knowledge base of the words and phrases that peo-
ple commonly use.3 There are another 255 settings
from the “movie scene” label in the MovieGraphs
(Vicol et al., 2018) resource—a collection of social
situations that were depicted in movie clips.
The Environment
contains signals that can
trigger associative priming of social norms (e.g.,
the noise level of a study space; Aarts and Dijk-
sterhuis). This portion of the taxonomy is designed
to be broad and general-purpose, with a set of at-
tributes that can refine any setting. Our taxonomy
is based on a broad review of the literature on norm
3Settings were defined by head-entities with an IsA rela-
tionship to some tail in {place, location, area}. Man-
ual inspection proved the usefulness of this heuristic.

--- Page 4 ---

Figure 2: An example of the SCENE Dramaturgical Framework used to constrain NORMBANK. The restaurant
setting is specified by the attendance (not crowded) and time of day (night) in the environment. The two agent
roles, customer and server; the latter is specified by the age bracket (adult) and gender (male) attributes. The
former are engaged in the behaviors drinking alcohol and going on a date. Note: Graphics are for illustration.
NORMBANK is a text dataset and does not contain any images.
formation and its relevant factors (van Rijswijk
and Haans, 2018; Janicik and Bartel, 2003; Boyce
et al., 2000; Russell and Ward, 1982; Durkheim,
1915). Importantly, the taxonomy is further refined
through crowdsourced feedback (§4). Ultimately,
our taxonomy grows to contain 404 environmental
constraints. An extensive overview of the environ-
mental constraints is given in Appendix B.1, but
we summarize them here.
In the environment, there are important taxo-
nomic subclasses of factors that inform norms. One
subclass is time constraints, like seasonality (Jani-
cik and Bartel, 2003), holidays and special custom-
ary observances (Durkheim, 1915), and another is
the country of operation, which serves as a proxy
for regional cultural differences (Meyer, 2014). We
also include factors from environmental psychol-
ogy (Bell et al., 2001) that involve the agent’s com-
fort and ease in the environment (e.g., noise level,
privacy, and cleanliness). Additionally, physical
conditions include factors like weather, which im-
pact visibility, coordination, safety, and comfort
(Boyce et al., 2000; van Rijswijk and Haans, 2018;
Cunningham, 1979). In addition to the imposed
taxonomy, annotator feedback (§4) lead us to add
a subclass called restrictions that formally limit
attendance, participation, and behavior, due to no-
tions of formality, religiosity, or exclusiveness.
Roles
may be ubiquitous, but it is chal-
lenging to collect reliable, setting-specific roles
with high coverage.
Our solution is to use
the powerful associative knowledge of LLMs
to automatically enumerate roles for each set-
ting via prompting,
inspired by Trinh and
Le (2018), Petroni et al. (2019), and others
(Wang et al., 2019; Sakaguchi et al., 2020).
Specifically, we prompt GPT-3 (Brown et al.,
2020) text-davinci-002 in a zero-shot man-
ner with the phrase “Some roles <preposition>
<determiner> <setting>:”
where the preposi-
tion and determiner are manually configured to
match the setting (for example, “some roles at
a casino:” or “some roles on the beach:”).
On average, we generate 5.5 roles per setting, with
a total of 928 unique roles.
Attributes
are properties of individual agents
that determine their social norms. Here again, the
goal is to derive a general purpose taxonomy from
the literature.
Some attributes are basic demo-
graphic categories like the person’s age bracket,
gender, race, religion, and sexuality (Thomp-
son Jr and Pleck, 1986; Dempsey and De Vaus,
2004; Helgeson, 2016). Related demographic cate-
gories include education level, employment, and
marital status. Since food is a focal point for cul-
ture and morality, we include diet. We also include
material constraints like medical condition and so-
cial class. Finally, we increase the coverage of this
set by including generic descriptors of two types:
condition or state adjectives, which describe a tem-
porary condition (e.g., dizzy), and characteristic
adjectives that describe more permanent attributes
(e.g., blonde). In total, our taxonomy defines 578
attribute constraints.
Behaviors
are the primary target of analysis
for social norms. As with roles, we co-opt GPT-3
to enumerate behaviors for each setting and
role, but the approach here is augmented in two
ways. First, we include a norm expectation in the
prompt. By querying for unexpected behaviors,
we can begin to shift the distribution of behaviors
away from the prototypical. Second, we increase
the diversity of generations by conditioning on

--- Page 5 ---

the agent’s attribute.
This further reduces the
number of conventional behaviors in our set. The
prompt
is
“Some things you would (never)
do <preposition> <determiner> <setting>
(if you were <attribute>):” where elements
in parentheses are optional elements. In this way,
we generated an average of 776.5 behaviors per
setting, which was filtered down to 112.6 behaviors
per setting, via programmatic methods described
in Appendix B.2.
4
Building NORMBANK
Section 3 gave us a high-recall set of constraint
variables for explaining situational social norms.
Our end goal is to build a resource that contains
reliable norms to ground, train, and test automatic
normative reasoning systems. We want these norms
to describe challenging, non-prototypical exam-
ples, and to depend on subtly contrasting situa-
tions that, when shifted, change the norm label
non-monotonically. This motivates us to use hu-
man annotation over the rich SCENE taxonomy.
Our process is essentially the reverse of the cur-
rent paradigm established by prior work, which
starts with a basic narrative context and subse-
quently extracts (Fung et al., 2022) or annotates
(Forbes et al., 2020) the expected behaviors. In-
stead, we start with behaviors and ask annotators
to provide us with different dramaturgical contexts
(SCENE constraints) under which that behavior
could be variously seen as expected, okay, or unex-
pected. Thus we obtain richer and less prototypical
instances—examples not mentioned in standard di-
alogue, which will significantly challenge models.
The approach is inspired by contrast sets (Gard-
ner et al., 2020) and counterfactual augmentation
(Kaushik et al., 2020) as means of reducing spuri-
ous correlations in model inferences.
4.1
Annotation Task
For the annotation task, we recruit experienced
English-speaking Mechanical Turk annotators who
have ≥98% acceptance with ≥100 HITs and are lo-
cated in the United States. The task requires human
creativity over a large combinatorial space. For a
given setting s and a behavior b, an annotator will
tell us distinct situational contexts under which b
is alternatively expected (required by duty or an-
ticipated with high probability), okay (permitted
or anticipated with moderate probability), or unex-
pected (forbidden, stigmatized, taboo, or otherwise
anticipated with very low probability).
These expected, okay, and unexpected cate-
gories are called “norm labels.”
The language
of expectation is useful for describing behavioral
regularities—the focus of this work—rather than
enumerating top-down or bottom-up judgements
of ethical or moral behavior, as in prior datasets
(Ziems et al., 2022; Emelin et al., 2021; Lourie
et al., 2021b). Importantly, we do not impose any
ethical philosophy or framework as in Hendrycks
et al. (2021), but instead, encourage annotators to
find norms that merely describe observable social
life (Cialdini et al., 1991).
The annotator fully specifies the appropriate
situational context by means of disjunctions
and conjunctions of constraints.
For example,
“spit at a dentist’s office” can be unexpected
when
(PERSON’s role is ‘dentist’)
or
when
((PERSON’s role is ‘patient’) AND
(PERSON’s behavior is ‘checking in’)).
Annotators select SCENE constraints using drop
down menus that follow the hierarchy of §3 (for
details on the HIT interface, see Appendix C.2).
They are also free to insert their own custom
constraints into the hierarchy. In this way, we
iteratively expand the taxonomy.
4.2
Dataset Quality
Quality Control.
Manual inspection of over 2.5k
data points reveals that the open-ended and cre-
ative aspects of the task are natural incentives for
high-quality work (Chandler et al., 2015; Sheehan,
2018). To further ensure the quality of NORM-
BANK, we trained annotators with careful instruc-
tion, a qualification test, a staging round, personal-
ized feedback, programmatic filtering, and finally, a
series of random audits (Litman et al., 2015; Shee-
han, 2018). The instructions included at least 3
fully-worked examples for each norm label, plus
suggestions and explanations for a total of 24 con-
straints. We administered a six-question qualifier,
which tested workers’ knowledge of the taxonomy,
definitions, free text response, and how to properly
indicate constraint conjunctions and disjunctions
through the task interface. If the worker passed at
least five questions correctly on the first try, she
would gain access to the staging round – a small-
scale version of the task in which each submission
would receive detailed and personalized feedback.
We invested a significant amount of time to feed-
back, offering 75 to 200 words of review for each

--- Page 6 ---

Constraints
Norms
Situations
Constr. / Norm
Taxonomic Constr.
Pre-populated Constr.
train
328,045
124,920
57,417
2.63
93.5%
69.3%
dev
37,761
15,008
8,573
2.52
92.8%
66.8%
test
42,601
15,495
8,674
2.75
94.6%
70.9%
NORMBANK
408,407
155,423
70,215
2.63
93.6%
69.2%
Table 1: Summary statistics show the immense scale of NORMBANK (§4) and the broad coverage of our SCENE
framework (§3). There are 155k total annotated norms, comprised of 70k unique situations, and each situation is
drawn from a conjunction of some subset of the 408k annotated constraints. Of these annotated constraints, 94% of
them use the structure of our SCENE taxonomy, and 69% use a pre-populated constraint value from one of our
taxonomic dropdown menus.
of 2, 502 staging HITs. Once a worker submitted 3
high-quality HITs in the staging round, he or she
could move to the full task. To identify poor work
here, we programmatically flagged workers with
extremely low variation in their annotations. Fi-
nally, we periodically performed a total of three
random audits, sampling 250 annotations in each
audit, to confirm the quality of the annotations.
Workers were paid a base rate, plus an additional
itemized bonus for every additional constraint they
added, which incentivized workers to be more ex-
pressive and creative. Annotators received a me-
dian of $30 per hour for this task.
Quality Metrics.
The above methods all proved
remarkably successful in generating a creative and
high-quality resource. Because our task is creative
and subjective, data quality is not easily measured
by inter-annotator agreement. We instead report
human evaluations over the Gold NORMBANK data
in the bottom row of Table 3 (alongside model
generations from §5.1). Annotations are considered
sensible (82.5%), relevant (82.17%), and normative
(72.9%). Still, it is important to note that around
half of gold annotations are marked by third-party
evaluators as fully correct by majority vote.
With regard to the correctness metric, annotator
disagreements can be traced to differences in the
annotators’ models of the world, which likely stem
from their own personal differences, including age,
profession, and worldview. For example, an annota-
tor likely familiar with the Cambodian tradition of
“Pithi Srang Preah” marked that “honoring your an-
cestors” is normal for Cambodians on Cambodian
New Year, while an annotator unfamiliar with this
practice marked it as unexpected. Furthermore, we
administered political leaning and the moral foun-
dations surveys to all annotators, which we release
alongside NORMBANK to help explain how these
age bracket
condition or 
state
characteristic
religion
medical
gender
other
customer
cashier
other
flirt with 
someone
argue with 
someone
yell
take a break
cry
go on a date
act in a movie 
scene
clean up after 
hours
talk loudly
slipping a little 
tongue
drink alcohol
dance
have sex
laugh
listen to music
pray
time
country
operational 
factors
physical 
conditions
spec. observances
other
behav. 
(16%)
role (26%)
attribute (36%)
envmnt.
(16%)
Figure 3: Distribution of NORMBANK constraints
where the area of each cell is proportional to the distri-
bution. Constraints are dominated most by the agent’s
attributes and roles, with a smaller and even split be-
tween behaviors and the environment.
personal differences informed the probabilities they
assigned to events. This resource will be of interest
to computer scientists and social scientists, since
NORMBANK contains not only commonsense facts,
but also culturally-conditioned distributions over
behavior and expectations about behavior.
4.3
Dataset Summary
Summary Statistics.
Table 1 gives the summary
statistics for the annotated dataset. NORMBANK
contains a total of 408k constraints, applied to 155k
norms, for an average of 2.63 constraints per norm.
The SCENE taxonomy broadly captures the kinds
of constraints annotators were looking for 94% of

--- Page 7 ---

Norm Classification Results
Model
P
R
F
Acc
ALBERT
68.0
66.6
67.1
71.0
BERT
72.1
70.7
71.3
74.6
RoBERTa
73.3
71.4
72.1
75.4
Table 2: Classification Results for {expected, okay, or
unexpected} show that standard transformer models can
learn to make normative inferences with an accuracy
that is adequate for expanding NORMBANK.
the time, and they were able to find their exact con-
straint value from a pre-populated list in 69% cases.
For concurrent behavior and attribute constraints,
annotators had to input their own values in 59% and
33% of cases respectively, followed by 27% and
9% of cases for the environment and roles. Overall,
this indicates that our GPT-3 prompting method
achieved high recall, especially for roles, and least
so for behaviors, which is unsurprising, given the
almost unbounded space of viable human behavior.
Figure 3 gives the distribution of constraints in
NORMBANK. Constraints are dominated most by
the agent’s attributes and roles. Age, condition,
and characteristic are the most popular attributes,
while roles vary. There is an even split between
behaviors and the environment. In the environment,
there is a notable focus on time constraints, and
slightly lesser but more even attention towards the
remaining subcategories.
Links to Existing Knowledge.
NORMBANK’s
SCENE taxonomy has close links to existing
knowledge resources. ConceptNet directly seeded
80 settings in SCENE. Beyond this, we success-
fully link over 90% of taxonomic items from the
setting, environment, roles, and attributes directly
with concepts in ConceptNet. These taxonomic
items cover 93.6% of all constraint categories and
70.0% of all constraint values. ConceptNet is fur-
ther linked to WordNet, DBPedia, Umbel, Cyc, and
Wiktionary, so by extension, NORMBANK can be
coupled to these resources.
5
Experiments: How to use NORMBANK
NORMBANK is not designed for any particular
narrow task; it is designed as a general-purpose
knowledge resource that can ground social reason-
ing through downstream tasks (compare ATOMIC
(Sap et al., 2019a) and ConceptNet (Liu and Singh,
2004)). Towards this end, NORMBANK should con-
tain richly organized knowledge that can be learned
by neural models and applied for non-monotonic
reasoning in new settings. In this way, it should be
possible to automatically expand the NORMBANK
resource. The knowledge contained here should
also be applicable across a range of social reason-
ing tasks. Thus our experiments aim to demon-
strate two things: (§5.1) that we can automatically
expand NORMBANK using neural methods, and
(§5.2) that NORMBANK is a useful resource with
relevant knowledge for downstream applications.
For all experiments in the following subsections,
we use an 80%-10%-10% train-dev-test split in
which <setting, behavior> tuples in one set are
never seen in another.
5.1
Automatic Knowledge Completion
How can we expand NORMBANK? We considered
two different methods of knowledge bank com-
pletion (Weston et al., 2013; Craven et al., 2000),
which rely on different assumptions. Results from
both methods indicate that NORMBANK is rich
enough to support its own automatic expansion.
Classification is the simpler case, where we as-
sume a closed world (Bordes et al., 2013; Lin et al.,
2015b,a; Socher et al., 2013), while generation as-
sumes an open world (Shi and Weninger, 2018)
with a modifiable set of constraints.
Classification.
Here, our known constraints and
behaviors (§3) will remain fixed (Shi and Weninger,
2018), but we can discover new relationships by
classifying unseen behavior and constraint combi-
nations as expected, okay, or unexpected. The ad-
vantage of this approach is that it is straightforward,
and the disadvantage is that evaluating classifiers
over the power set of the entire constraint space
would be intractable; thus more efficient search
methods will be needed.
For all norm classification tasks, we fine-tune
three popular transformer models: BERT-base-
uncased (Devlin et al., 2019), RoBERTa-base (Liu
et al., 2019), and ALBERT-base-v2 (Lan et al.,
2020), with hyperparameters in Appendix A. Re-
sults in Table 2 appear promising. Given the scope
and scale of NORMBANK, models are capable of
learning non-monotonic inferences, achieving F1
scores as high as 72.1% on the test set. This shows
that classification is a reliable method for NORM-
BANK knowledge expansion.

--- Page 8 ---

Model
Decoding
ROUGE-L
BLEU
Avg. # Constr.
Tax. Constr.
Pre-pop. Constr.
SensibleS
CorrectS
NormC
RelevantC
BART
greedy
75.7
23.1
1.62
93.8
40.7
100.0
46.0
94.3
94.3
beam
77.1
23.5
1.70
98.8
48.2
98.0
36.0
92.5
94.9
p=0.9
75.8
23.1
1.62
87.7
42.0
100.0
46.0
91.9
97.0
GPT-2
greedy
57.4
12.5
1.78
70.8
36.0
86.0
34.0
86.1
89.6
beam
70.0
16.5
1.26
95.2
47.6
94.0
34.0
88.3
94.3
p=0.9
60.2
13.2
1.46
90.4
43.8
84.0
34.0
93.0
94.0
T-5
greedy
45.0
10.3
2.70
67.2
28.4
60.0
22.0
78.8
78.9
beam
68.3
13.7
1.02
100.0
64.7
86.0
40.0
89.5
96.3
p=0.9
48.4
10.9
2.26
72.7
30.0
76.0
42.0
83.0
79.1
GPT-3 davinci-002
44.2
23.2
5.31
85.4
33.0
87.3
49.0
90.5
83.5
GPT-3 davinci-003
51.7
28.6
2.34
84.6
33.2
95.0
61.1
91.8
87.8
Gold NORMBANK
-
-
2.68
93.6
70.0
82.5
55.0
72.9
81.7
Table 3: Constraint generation results. (Left) Automatic evaluation suggests that BART has the advantage over
other generative models. (Middle) Generated constraints fall into the SCENE taxonomy 67.2-100% [Tax. Constr.]
and use a pre-populated constraint 30-64% of the time [Pre-pop. Constr.], depending on the decoding strategy.
(Right) Human eval shows encouraging results: a NORMBANK-trained BART can generate sensible, correct,
normative, and relevant constraints for use in automatically expanding NORMBANK. Here, the best fine-tuned
model results are highlighted, while the best overall model results are bolded.
Generation.
The model is trained with a forward
language modeling objective over the string g:
g = {[SETTING], s1, s2, ..., sn,
[BEHAVIOR], b1, b2, ..., bm,
[NORM], label,
[CONSTRAINTS]c1
1, c1
2, ..., c1
ℓ1
[AND]c2
1, c2
2, ..., c2
ℓ2...
[AND]ck
1, ck
2, ..., ck
ℓk<EOS>}
At inference time, the model generates the list
of constraints c1, ..., ck that will make the norm
label true as it is conditioned on the setting s
and behavior b. For this purpose, it is sufficient to
use BART (Lewis et al., 2020), GPT-2 (Radford
et al., 2019), and T5 (Raffel et al., 2020), three pow-
erful language models used widely for generative
inference. We also prompted GPT-3 davinci-002
and davinci-003 in a few-shot manner via the Ope-
nAI API (see the prompts in Appendix A).
Evaluation comes from both automatic and hu-
man metrics.
Humans evaluate 300 <setting,
behavior> data points for each of the 11 Model
× Decoding combinations, plus gold standard ex-
amples from NORMBANK. For constraints, they
provide us the % NormC (proportion that helps
represent a human rule or expectation for behav-
ior) and % RelevantC (proportion that relates to
the norm without redundancy or tautology). They
also give us situation4 evals: are they % CorrectS
(they produce an accurate norm label) and mutu-
ally % SensibleS (all constraints can be true at
the same time).
4Situations are defined as the intersection of constraints
Table 3 gives the generation results for the three
fine-tuned models: BART, GPT-2, and T-5. Ac-
cording to human judgment, all models produce
text that successfully constrains human expecta-
tions for behavior (NormC ∼90%). BART + nu-
cleus sampling (p = 0.9) gives the most SensibleS
(100%) and CorrectS situations (46%) with the
most RelevantC constraints (97%). This is clearly
a challenging task: situations are deemed correct
only 46% of the time. Yet they closely approach
the scores of human gold-standard data (55%).
Notably, generated constraints are highly relevant
to the norm label and entirely mutually-sensible.
Given the challenging nature of the task, the re-
sults are quite encouraging, suggesting that NORM-
BANK can facilitate its own expansion via natural
language generation.
Prompting
Results in Table 3 show that few-shot
GPT-3 models fail to match our best performing
BART model’s ability to generate Sensible situa-
tions (95 vs. 100%) with high %Norm (91.8 vs
94.3%) and %Relevant constraints (87.8 vs 97%).
Still, annotators are more likely to find GPT-3 out-
put to be Correct overall (61.1 vs 46%). Automatic
metrics show that GPT-3 achieves higher precision
(28.6 vs 23.1 BLEU) at the expense of recall (51.7
vs 77.1 ROUGE-L), suggesting that GPT-3’s gen-
erations, while often correct, may be more proto-
typical. Qualitative analysis confirms this.
Sometimes the conventional answer leads GPT-
3 astray, as when it uses a series of faulty lexical
associations to explain that ‘drinking milk’ is unex-
pected on an ‘athletic field’ for individuals who are
not the coach and for those whose behavior is not

--- Page 9 ---

‘hydrate’ while the temperature is ‘warm.’ BART,
however, correctly discerns that it’s unexpected for
athletes whose behavior is ‘playing sports.’ In gen-
eral, GPT-3 appears more likely to underspecify the
situation. For example, GPT-3 responds that it’s
expected for a homeowner to ‘leave the gate open’
in the ‘backyard,’ and BART agrees, but BART
further specifies that the owner might be ‘working
outside’ to justify the expectation.
Both quantitative and qualitative analyses indi-
cate that prompting methods can certainly comple-
ment, but may not fully replace, fine-tuned gener-
ation approaches to NORMBANK expansion. A
mixed approach may be most desirable due to
coverage and correctness, while generation errors
may be fixed using self-correction via classification
(above) or further prompting (Fung et al., 2022).
Finally, the middle pane of Table 3 shows the
proportion of generated constraints that fall into
our taxonomy (Tax. Constr.) and the proportion
contained in NORMBANK (Pre-pop. Constr.). The
former shows that our taxonomy broadly captures
the relevant axes (80-90% of our best models’ gen-
erations are taxonomic). The latter shows that be-
tween one third and one half of generations ‘link’
prior constraints to new situations; the rest of gen-
erated constraints are brand new.
5.2
Transfer Learning for Downstream Tasks
Finally, we conduct transfer learning experiments
to demonstrate the utility of the data for down-
stream applications, further indicating the scope
and power of NORMBANK as a general-purpose re-
source for social reasoning. Concretely, we follow
the sequential training paradigm (Pratt et al., 1991),
which has proven better than multitask training
and fine-tuning on a broad range of commonsense
tasks (Lourie et al., 2021a). Specifically, we ini-
tialize a RoBERTa model with weights from our
best-performing norm classifier from Section 5.1
and fine-tune on the target set for 7 epochs.
We evaluate on two specifically moral reason-
ing tasks, Anecdotes and Dilemmas, both from the
SCRUPLES benchmark (Lourie et al., 2021b). We
also consider two multiple-choice commonsense
QA datasets. Social IQa (Sap et al., 2019b) is de-
signed to test social intelligence (e.g., inferring mo-
tivations, emotional reactions), while CosmosQA
(Huang et al., 2019) tests cause and effect and coun-
terfactual reasoning in everyday situations.
All results in Table 4 are averaged over five sepa-
Eval
Base
w/ Transfer Learning from
Task
Model
CQA
SIQA
NORMBANK
ANEC DOT ES
68.3
68.3‡
68.0
68.7⋆‡
DILE MMA S
64.3
67.4
70.9⋆
71.1⋆
SOC IALIQA
59.9
64.1
59.9
64.2
COS MOSQA
59.8
59.8
63.5⋆†
61.2
Table 4: Transfer Learning Accuracies demonstrate
the utility of NORMBANK. By sequential finetuning
on NORMBANK, we improve performance over base-
line on all tasks, and transfer performance from NORM-
BANK exceeds transfer performance from CosmosQA
and from SocialIQa in three cases. Best performance is
bolded. Star⋆results indicate significant improvements
over the Base Model, while † marks significance over
CQA, and ‡ marks significance over SIQA.
rate train-test runs, and significance is given by the
paired bootstrap test. NORMBANK’s utility is seen
by comparing the accuracy of models with trans-
fer learning from NORMBANK against those with
task-only fine-tuning (Base Model). Results show
that NORMBANK improves situational moral clas-
sification (Anecdotes; +0.4%) and forced choice
binary moral judgments (Dilemmas +6.8%) with
significance. Also consider NORMBANK utility
as compared to transfer learning from either Cos-
mosQA (CQA) or SocialIQa (SIQA). The only
task on which transfer from NORMBANK does not
achieve the best performance is on CosmosQA eval-
uation. Here, we find that transfer from the more
structurally related Social IQa task is preferred. We
conclude that NORMBANK is a useful resource for
a range of downstream applications in moral, social,
and emotional reasoning in context.
6
Conclusion
Social norms are the foundation of culture and soci-
ety (McDonald and Crandall, 2015; Hogg and Reid,
2006), and an understanding of these norms is cru-
cial for assistive and collaborative AI. In this work,
we introduced SCENE a new scheme for hierarchi-
cally organizing the seemingly unbounded space
of situational contexts that determine social norms.
With this framework, we built NORMBANK, the
first social knowledge bank to leverage such con-
textual information for contrast sets of richly con-
ditioned defeasible social norms. We found that
NORMBANK supports its own automatic expan-
sion via classification, generation, and prompting
methods. Finally, we demonstrated the utility of
NORMBANK for situational social reasoning tasks.

--- Page 10 ---

7
Limitations
At its core, NORMBANK is a collection of logical
operations on unique constraints. Consequently,
one practical limitation stems from the issue that
some situations cannot be reasonably expressed as
a set of constraints. While theoretically all logic
can be decomposed into AND and OR operations,
the logic may be too challenging for an individual
to formulate, or the set of constraints themselves
might be too large and unwieldy. The latter is
problematic, because language models have a finite
input token capacity, and for the set of constraints
to be digestible, they must fit within that capacity.
Relatedly, if the logic to encode constraints become
more sophisticated, ensuring that logic is not unnec-
essarily duplicated will pose a greater challenge.
Additionally, certain properties of NORMBANK
like the role and behaviors may be challenging to
succinctly describe. Further work will be needed to
ascertain how these can be incorporated or to more
clearly define situations that are out of scope.
Due to limitations on time and computational
resources, we have not exhaustively evaluated all
downstream applications of NORMBANK, and in
future work, we will test additional transfer tasks
beyond the moral and social classification tasks
considered in this work. Since NORMBANK is the
first to encode non-monotonic situational norms,
there was no other available benchmark that is di-
rectly analogous to ours. Instead, our primary evi-
dence for NormBank’s utility is in Table 3, where
human evaluators confirm that models trained on
NORMBANK can reliably learn to make new infer-
ences about non-monotonic situational norms.
Other follow up studies should consider training
larger normative reasoning models, and/or engi-
neering better prompts for expanding NORMBANK.
Relatedly, we have no data to speculate about the
long-term evolution of real-world norms relative to
this resource, nor the rate of decay in the reliability
of NORMBANK. Future work should also expand
this resource with perspectives from cultures other
than our available annotator pool. The pool was
not representative of all cultures and people groups,
as we discuss further in the Ethics section.
8
Ethics
Ethical Assumptions. First, to set proper bound-
aries on this resource and the tasks it can facilitate,
we will outline the ethical assumptions of this work
and address some potential misconceptions. We
want to stress that NORMBANK represents a col-
lection of situational norms that we do not treat as
prescriptive, but rather descriptive. Unlike prior
moral / ethics datasets (Ziems et al., 2022; Emelin
et al., 2021; Lourie et al., 2021b; Forbes et al., 2020;
Sap et al., 2020), we use the neutral language of
expected, okay, and unexpected behaviors to focus
on empirically observed patterns and avoid an over-
emphasis on the ethical grey area of what ought to
be done. Unlike tricky moral dilemmas, the situa-
tional social norms of NORMBANK have an answer
that a majority can agree is descriptively observable
as the expectation under the respective conditions
and/or cultural context. Nevertheless, normative
judgments can vary between individuals in differ-
ent social groups and time periods (Haidt et al.,
1993; Shweder, 1990; Bicchieri, 2005; Culley and
Madhavan, 2013; Amaya et al., 2021). NORM-
BANK can and should be expanded via automatic
or manual methods that can incorporate these axes
of variation. Our annotator pool was limited to
English-speaking individuals living in the United
States in the year 2022. Future expansion efforts
could be crowdsourced from other cultures and
geographic regions and in future decades.
We reiterate that the norms in NORMBANK
should not be used for prescriptive advice or per-
sonal guidance in any way. Our work intends to
unlock future work in the capacity to imbue lan-
guage models with situational commonsense and
enable them to jointly reason with the situational
contexts. Language models which ignore situa-
tional contexts altogether may be just as hazardous,
if not more.
Finally, there are likely biases towards certain
roles and values in NORMBANK. We have taken
steps to mitigate some forms, such as gender bias,
by neutralizing constraints (e.g., [PERSON]’s role
is ‘cowboy or cowgirl’ and [PERSON]’s role is
‘ball boy or girl’). Our SCENE taxonomy, with
the standardized structure of its role and attribute
constraints, will allow practitioners to further ana-
lyze specific axes of prejudice and thus implement
targeted mitigation strategies. Specific identity at-
tributes like gender, ethnicity, and religion are rep-
resented in 24% of norms.5 Stakeholders can invest
a smaller but more concerted effort towards mit-
igating bias in these constraints. We encourage
5There are 40k norms (out of 169k total norms; 24%)
which cover attributes in the following set: {‘country’, ‘age
bracket’, ‘education’, ‘gender’, ‘race or ethnicity’, ‘religion’,
‘sexuality’, ‘social class’}

--- Page 11 ---

stakeholders to give auditing control over a given
norm to those who are affected by it. Previous
norm-datasets encode norms in free-text annota-
tions which lack a hierarchical taxonomy of con-
texts, but our taxonomy can be used to interpret, di-
agnose, and mitigate prejudice, and to return power
to those affected by these prejudices.
Risks in deployment.
Before starting any an-
notation, the resources and findings presented in
this work were thoroughly reviewed and approved
by an internal review board. Prior to being put
into production, the method would also need to
be re-evaluated when applied to a new domain to
ensure reliable performance in order to prevent un-
intended consequences. To help mitigate risks in
deployment from misunderstandings about the ethi-
cal assumptions above, we require users of this data
to complete a Data Use Agreement. The user will
check that they understand the ethical assumptions
above: especially that NORMBANK is not to be
taken for advice. Practitioners will also agree not
to use NORMBANK for malicious purposes “includ-
ing (but not limited to): mockery, discrimination,
and hate speech.”
Acknowledgements
We are thankful to Julia Kruk, William Held, Al-
bert Lu, Camille Harris, and the anonymous ACL
reviewers for their helpful feedback. Caleb Ziems
is supported by the NSF Graduate Research Fel-
lowship under Grant No. DGE-2039655.
References
2022. Permanent missions to the united nations, no.
310. Permanent Missions to the United Nations.
Henk Aarts and Ap Dijksterhuis. 2003. The silence
of the library: environment, situational norm, and
social behavior. Journal of personality and social
psychology, 84(1):18.
Irwin Altman. 1975. The environment and social behav-
ior: privacy, personal space, territory, and crowding.
Ashley Amaya, Ruben Bach, Florian Keusch, and
Frauke Kreuter. 2021. New data sources in social
science research: things to know before working
with reddit data. Social science computer review,
39(5):943–960.
Janna Anderson and Lee Rainie. 2022. The metaverse
in 2040. Pew Research Center.
Rodrigo Bavaresco, Diórgenes Silveira, Eduardo Reis,
Jorge Barbosa, Rodrigo Righi, Cristiano Costa,
Rodolfo Antunes, Marcio Gomes, Clauter Gatti, Mar-
iangela Vanzin, et al. 2020. Conversational agents
in business: A systematic literature review and fu-
ture research directions. Computer Science Review,
36:100239.
Paul A Bell, T Green, Jeffrey D Fisher, and Andrew
Baum. 2001. Environmental psychology. New Jer-
sey.
Cristina Bicchieri. 2005. The grammar of society: The
nature and dynamics of social norms. Cambridge
University Press.
Yonatan Bisk, Rowan Zellers, Ronan LeBras, Jianfeng
Gao, and Yejin Choi. 2020. PIQA: reasoning about
physical commonsense in natural language. In The
Thirty-Fourth AAAI Conference on Artificial Intelli-
gence, AAAI 2020, The Thirty-Second Innovative Ap-
plications of Artificial Intelligence Conference, IAAI
2020, The Tenth AAAI Symposium on Educational
Advances in Artificial Intelligence, EAAI 2020, New
York, NY, USA, February 7-12, 2020, pages 7432–
7439. AAAI Press.
Joseph A Blass and Ian D Horswill. 2015. Implement-
ing injunctive social norms using defeasible reason-
ing. In Eleventh Artificial Intelligence and Interac-
tive Digital Entertainment Conference.
Michael Boratko, Xiang Li, Tim O’Gorman, Rajarshi
Das, Dan Le, and Andrew McCallum. 2020. Pro-
toQA: A question answering dataset for prototypi-
cal common-sense reasoning. In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 1122–1136,
Online. Association for Computational Linguistics.
Antoine Bordes, Nicolas Usunier, Alberto García-
Durán, Jason Weston, and Oksana Yakhnenko.
2013. Translating embeddings for modeling multi-
relational data. In Advances in Neural Information
Processing Systems 26: 27th Annual Conference on
Neural Information Processing Systems 2013. Pro-
ceedings of a meeting held December 5-8, 2013, Lake
Tahoe, Nevada, United States, pages 2787–2795.
Peter R Boyce, Neil H Eklund, Barbara J Hamilton, and
Lisa D Bruno. 2000. Perceptions of safety at night in
different lighting conditions. International Journal
of Lighting Research and Technology, 32(2):79–91.
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language models are few-shot learners. In Ad-
vances in Neural Information Processing Systems 33:

--- Page 12 ---

Annual Conference on Neural Information Process-
ing Systems 2020, NeurIPS 2020, December 6-12,
2020, virtual.
Fabio Maria Carlucci, Lorenzo Nardi, Luca Iocchi, and
Daniele Nardi. 2015. Explicit representation of social
norms for social robots. In 2015 IEEE/RSJ Interna-
tional Conference on Intelligent Robots and Systems
(IROS), pages 4191–4196. IEEE.
Jesse Chandler, Gabriele Paolacci, Eyal Peer, Pam
Mueller, and Kate A Ratliff. 2015. Using nonnaive
participants can reduce effect sizes. Psychological
science, 26(7):1131–1139.
Ting-Yun Chang, Yang Liu, Karthik Gopalakrishnan,
Behnam Hedayatnia, Pei Zhou, and Dilek Hakkani-
Tur. 2020. Incorporating commonsense knowledge
graph in pretrained models for social commonsense
tasks. In Proceedings of Deep Learning Inside Out
(DeeLIO): The First Workshop on Knowledge Extrac-
tion and Integration for Deep Learning Architectures,
pages 74–79, Online. Association for Computational
Linguistics.
Robert B Cialdini, Carl A Kallgren, and Raymond R
Reno. 1991. A focus theory of normative conduct:
A theoretical refinement and reevaluation of the role
of norms in human behavior. In Advances in experi-
mental social psychology, volume 24, pages 201–234.
Elsevier.
Robert B Cialdini, Raymond R Reno, and Carl A Kall-
gren. 1990. A focus theory of normative conduct:
Recycling the concept of norms to reduce littering
in public places. Journal of personality and social
psychology, 58(6):1015.
Mark Craven, Dan DiPasquo, Dayne Freitag, Andrew
McCallum, Tom Mitchell, Kamal Nigam, and Seán
Slattery. 2000.
Learning to construct knowledge
bases from the world wide web. Artificial intelli-
gence, 118(1-2):69–113.
Kimberly E Culley and Poornima Madhavan. 2013. A
note of caution regarding anthropomorphism in hci
agents. Computers in Human Behavior, 29(3):577–
579.
Michael R Cunningham. 1979. Weather, mood, and
helping behavior: Quasi experiments with the sun-
shine samaritan. Journal of personality and social
psychology, 37(11):1947.
Ken Dempsey and David De Vaus. 2004. Who cohabits
in 2001? the significance of age, gender, religion and
ethnicity. Journal of Sociology, 40(2):157–178.
Eric Deng, Bilge Mutlu, Maja J Mataric, et al. 2019.
Embodiment in socially interactive robots. Founda-
tions and Trends® in Robotics, 7(4):251–356.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
E Durkheim. 1915. The elementary forms of the reli-
gious life: A study in religious sociology.
Hady Elsahar, Pavlos Vougiouklis, Arslen Remaci,
Christophe Gravier, Jonathon Hare, Frederique Lafor-
est, and Elena Simperl. 2018. T-REx: A large scale
alignment of natural language with knowledge base
triples. In Proceedings of the Eleventh International
Conference on Language Resources and Evaluation
(LREC 2018), Miyazaki, Japan. European Language
Resources Association (ELRA).
Denis Emelin, Ronan Le Bras, Jena D Hwang, Maxwell
Forbes, and Yejin Choi. 2021. Moral stories: Sit-
uated reasoning about norms, intents, actions, and
their consequences. In Proceedings of the 2021 Con-
ference on Empirical Methods in Natural Language
Processing, pages 698–718.
Terrence Fong, Illah Nourbakhsh, and Kerstin Dauten-
hahn. 2003. A survey of socially interactive robots.
Robotics and autonomous systems, 42(3-4):143–166.
Maxwell Forbes, Jena D. Hwang, Vered Shwartz,
Maarten Sap, and Yejin Choi. 2020. Social chem-
istry 101: Learning to reason about social and moral
norms. In Proceedings of the 2020 Conference on
Empirical Methods in Natural Language Processing
(EMNLP), pages 653–670, Online. Association for
Computational Linguistics.
Yi R Fung, Tuhin Chakraborty, Hao Guo, Owen
Rambow, Smaranda Muresan, and Heng Ji. 2022.
Normsage: Multi-lingual multi-cultural norm discov-
ery from conversations on-the-fly. ArXiv preprint,
abs/2210.08604.
Matt Gardner, Yoav Artzi, Victoria Basmov, Jonathan
Berant, Ben Bogin, Sihao Chen, Pradeep Dasigi,
Dheeru Dua, Yanai Elazar, Ananth Gottumukkala,
Nitish Gupta, Hannaneh Hajishirzi, Gabriel Ilharco,
Daniel Khashabi, Kevin Lin, Jiangming Liu, Nel-
son F. Liu, Phoebe Mulcaire, Qiang Ning, Sameer
Singh, Noah A. Smith, Sanjay Subramanian, Reut
Tsarfaty, Eric Wallace, Ally Zhang, and Ben Zhou.
2020. Evaluating models’ local decision boundaries
via contrast sets.
In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
1307–1323, Online. Association for Computational
Linguistics.
Ervin Goffman. 1959. The presentation of self in every-
day life. Doubleday Anchor Books.
Joshua Grossman, Zhiyuan Lin, Hao Sheng, Johnny
Tian-Zheng Wei, Joseph J Williams, and Sharad Goel.
2019. Mathbot: Transforming online resources for
learning math into conversational interactions. AAAI
2019 Story-Enabled Intelligence.

--- Page 13 ---

Jonathan Haidt, Silvia Helena Koller, and Maria G Dias.
1993. Affect, culture, and morality, or is it wrong
to eat your dog? Journal of personality and social
psychology, 65(4):613.
Vicki S Helgeson. 2016. Psychology of gender. Rout-
ledge.
Dan Hendrycks, Collin Burns, Steven Basart, An-
drew Critch Critch, Jerry Li Li, Dawn Song, and
Jacob Steinhardt. 2021. Aligning ai with shared hu-
man values. In International Conference on Learning
Representations.
Michael A Hogg and Scott A Reid. 2006. Social iden-
tity, self-categorization, and the communication of
group norms. Communication theory, 16(1):7–30.
Dirk Hovy and Diyi Yang. 2021. The importance of
modeling social factors of language: Theory and
practice. In Proceedings of the 2021 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, pages 588–602, Online. Association
for Computational Linguistics.
Lifu Huang, Ronan Le Bras, Chandra Bhagavatula, and
Yejin Choi. 2019. Cosmos QA: Machine reading
comprehension with contextual commonsense rea-
soning. In Proceedings of the 2019 Conference on
Empirical Methods in Natural Language Processing
and the 9th International Joint Conference on Natu-
ral Language Processing (EMNLP-IJCNLP), pages
2391–2401, Hong Kong, China. Association for Com-
putational Linguistics.
Gregory A Janicik and Caroline A Bartel. 2003. Talking
about time: Effects of temporal planning and time
awareness norms on group coordination and perfor-
mance. Group Dynamics: Theory, Research, and
Practice, 7(2):122.
Haozhe Ji, Pei Ke, Shaohan Huang, Furu Wei, and Min-
lie Huang. 2020a. Generating commonsense expla-
nation by extracting bridge concepts from reasoning
paths. In Proceedings of the 1st Conference of the
Asia-Pacific Chapter of the Association for Compu-
tational Linguistics and the 10th International Joint
Conference on Natural Language Processing, pages
248–257, Suzhou, China. Association for Computa-
tional Linguistics.
Haozhe Ji, Pei Ke, Shaohan Huang, Furu Wei, Xiaoyan
Zhu, and Minlie Huang. 2020b. Language generation
with multi-hop reasoning on commonsense knowl-
edge graph. In Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Process-
ing (EMNLP), pages 725–736, Online. Association
for Computational Linguistics.
Liwei Jiang, Jena D Hwang, Chandra Bhagavatula, Ro-
nan Le Bras, Maxwell Forbes, Jon Borchardt, Jenny
Liang, Oren Etzioni, Maarten Sap, and Yejin Choi.
2021. Delphi: Towards machine ethics and norms.
ArXiv preprint, abs/2110.07574.
Divyansh Kaushik, Eduard H. Hovy, and Zachary Chase
Lipton. 2020. Learning the difference that makes A
difference with counterfactually-augmented data. In
8th International Conference on Learning Represen-
tations, ICLR 2020, Addis Ababa, Ethiopia, April
26-30, 2020. OpenReview.net.
Joanna Klimczyk. 2021. Compositional semantics and
normative ‘ought’. Axiomathes, 31(3):381–399.
Zhenzhong Lan, Mingda Chen, Sebastian Goodman,
Kevin Gimpel, Piyush Sharma, and Radu Soricut.
2020. ALBERT: A lite BERT for self-supervised
learning of language representations. In 8th Inter-
national Conference on Learning Representations,
ICLR 2020, Addis Ababa, Ethiopia, April 26-30,
2020. OpenReview.net.
Douglas B Lenat. 1995. Cyc: A large-scale investment
in knowledge infrastructure. Communications of the
ACM, 38(11):33–38.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan
Ghazvininejad, Abdelrahman Mohamed, Omer Levy,
Veselin Stoyanov, and Luke Zettlemoyer. 2020.
BART: Denoising sequence-to-sequence pre-training
for natural language generation, translation, and com-
prehension. In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics,
pages 7871–7880, Online. Association for Computa-
tional Linguistics.
Yankai Lin, Zhiyuan Liu, Huanbo Luan, Maosong Sun,
Siwei Rao, and Song Liu. 2015a. Modeling relation
paths for representation learning of knowledge bases.
In Proceedings of the 2015 Conference on Empirical
Methods in Natural Language Processing, pages 705–
714, Lisbon, Portugal. Association for Computational
Linguistics.
Yankai Lin, Zhiyuan Liu, Maosong Sun, Yang Liu, and
Xuan Zhu. 2015b. Learning entity and relation em-
beddings for knowledge graph completion. In Pro-
ceedings of the Twenty-Ninth AAAI Conference on
Artificial Intelligence, January 25-30, 2015, Austin,
Texas, USA, pages 2181–2187. AAAI Press.
Leib Litman, Jonathan Robinson, and Cheskie Rosen-
zweig. 2015. The relationship between motivation,
monetary compensation, and data quality among us-
and india-based workers on mechanical turk. Behav-
ior research methods, 47(2):519–528.
Hugo Liu and Push Singh. 2004. Conceptnet—a practi-
cal commonsense reasoning tool-kit. BT technology
journal, 22(4):211–226.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
Roberta: A robustly optimized bert pretraining ap-
proach. ArXiv preprint, abs/1907.11692.
Ilya Loshchilov and Frank Hutter. 2019. Decoupled
weight decay regularization. In 7th International
Conference on Learning Representations, ICLR 2019,

--- Page 14 ---

New Orleans, LA, USA, May 6-9, 2019. OpenRe-
view.net.
Nicholas Lourie, Ronan Le Bras, Chandra Bhagavatula,
and Yejin Choi. 2021a. Unicorn on rainbow: A uni-
versal commonsense reasoning model on a new mul-
titask benchmark. In Proceedings of the AAAI Con-
ference on Artificial Intelligence, volume 35, pages
13480–13488.
Nicholas Lourie, Ronan Le Bras, and Yejin Choi. 2021b.
Scruples: A corpus of community ethical judgments
on 32, 000 real-life anecdotes. In Proceedings of
the AAAI Conference on Artificial Intelligence, vol-
ume 35, pages 13470–13479.
Aman Madaan, Dheeraj Rajagopal, Niket Tandon, Yim-
ing Yang, and Eduard Hovy. 2021. Could you give
me a hint ? generating inference graphs for defeasible
reasoning. In Findings of the Association for Com-
putational Linguistics: ACL-IJCNLP 2021, pages
5138–5147, Online. Association for Computational
Linguistics.
Kenneth E Mathews and Lance Kirkpatrick Canon.
1975. Environmental noise level as a determinant
of helping behavior. Journal of Personality and So-
cial Psychology, 32(4):571.
Rachel I McDonald and Christian S Crandall. 2015.
Social norms and social influence. Current Opinion
in Behavioral Sciences, 3:147–151.
Erin Meyer. 2014. The culture map: Breaking through
the invisible boundaries of global business. Public
Affairs.
Tom M. Mitchell, William W. Cohen, Estevam R. Hr-
uschka Jr., Partha Pratim Talukdar, Justin Betteridge,
Andrew Carlson, Bhavana Dalvi Mishra, Matthew
Gardner, Bryan Kisiel, Jayant Krishnamurthy, Ni Lao,
Kathryn Mazaitis, Thahir Mohamed, Ndapandula
Nakashole, Emmanouil A. Platanios, Alan Ritter,
Mehdi Samadi, Burr Settles, Richard C. Wang,
Derry Wijaya, Abhinav Gupta, Xinlei Chen, Abul-
hair Saparov, Malcolm Greaves, and Joel Welling.
2015. Never-ending learning. In Proceedings of the
Twenty-Ninth AAAI Conference on Artificial Intel-
ligence, January 25-30, 2015, Austin, Texas, USA,
pages 2302–2310. AAAI Press.
Arindam Mitra, Pratyay Banerjee, Kuntal Kumar Pal,
Swaroop Mishra, and Chitta Baral. 2019. How ad-
ditional knowledge can improve natural language
commonsense question answering? ArXiv preprint,
abs/1909.08855.
György Molnár and Zoltán Szüts. 2018. The role of
chatbots in formal education. In 2018 IEEE 16th
International Symposium on Intelligent Systems and
Informatics (SISY), pages 000197–000202. IEEE.
Fabio Petroni, Tim Rocktäschel, Sebastian Riedel,
Patrick Lewis, Anton Bakhtin, Yuxiang Wu, and
Alexander Miller. 2019. Language models as knowl-
edge bases?
In Proceedings of the 2019 Confer-
ence on Empirical Methods in Natural Language Pro-
cessing and the 9th International Joint Conference
on Natural Language Processing (EMNLP-IJCNLP),
pages 2463–2473, Hong Kong, China. Association
for Computational Linguistics.
John L Pollock. 1987. Defeasible reasoning. Cognitive
science, 11(4):481–518.
Lorien Y Pratt, Jack Mostow, Candace A Kamm, Ace A
Kamm, et al. 1991. Direct transfer of learned infor-
mation among neural networks. In Aaai, volume 91,
pages 584–589.
Valentina Pyatkin, Jena D Hwang, Vivek Srikumar,
Ximing Lu, Liwei Jiang, Yejin Choi, and Chandra
Bhagavatula. 2022. Reinforced clarification ques-
tion generation with defeasibility rewards for disam-
biguating social and moral situations. ArXiv preprint,
abs/2212.10409.
Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Dario Amodei, and Ilya Sutskever. 2019. Language
models are unsupervised multitask learners. OpenAI
blog, 1(8):9.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J Liu. 2020. Exploring the lim-
its of transfer learning with a unified text-to-text
transformer. Journal of Machine Learning Research,
21(140):1–67.
Raymond Reiter. 1981. On closed world data bases.
In Readings in artificial intelligence, pages 119–140.
Elsevier.
Rachel Rudinger, Vered Shwartz, Jena D. Hwang, Chan-
dra Bhagavatula, Maxwell Forbes, Ronan Le Bras,
Noah A. Smith, and Yejin Choi. 2020. Thinking like
a skeptic: Defeasible inference in natural language.
In Findings of the Association for Computational Lin-
guistics: EMNLP 2020, pages 4661–4675, Online.
Association for Computational Linguistics.
James A Russell and Lawrence M Ward. 1982. Envi-
ronmental psychology. Annual review of psychology,
33(1):651–689.
Keisuke Sakaguchi, Ronan Le Bras, Chandra Bhaga-
vatula, and Yejin Choi. 2020. Winogrande: An ad-
versarial winograd schema challenge at scale. In
Proceedings of the AAAI Conference on Artificial
Intelligence, volume 34, pages 8732–8740.
Maarten Sap, Ronan Le Bras, Emily Allaway, Chan-
dra Bhagavatula, Nicholas Lourie, Hannah Rashkin,
Brendan Roof, Noah A. Smith, and Yejin Choi.
2019a. ATOMIC: an atlas of machine commonsense
for if-then reasoning. In The Thirty-Third AAAI Con-
ference on Artificial Intelligence, AAAI 2019, The
Thirty-First Innovative Applications of Artificial In-
telligence Conference, IAAI 2019, The Ninth AAAI
Symposium on Educational Advances in Artificial

--- Page 15 ---

Intelligence, EAAI 2019, Honolulu, Hawaii, USA,
January 27 - February 1, 2019, pages 3027–3035.
AAAI Press.
Maarten Sap, Saadia Gabriel, Lianhui Qin, Dan Juraf-
sky, Noah A. Smith, and Yejin Choi. 2020. Social
bias frames: Reasoning about social and power im-
plications of language. In Proceedings of the 58th
Annual Meeting of the Association for Computational
Linguistics, pages 5477–5490, Online. Association
for Computational Linguistics.
Maarten Sap, Hannah Rashkin, Derek Chen, Ronan
Le Bras, and Yejin Choi. 2019b. Social IQa: Com-
monsense reasoning about social interactions. In
Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the
9th International Joint Conference on Natural Lan-
guage Processing (EMNLP-IJCNLP), pages 4463–
4473, Hong Kong, China. Association for Computa-
tional Linguistics.
R. C. Schank and R. P. Abelson. 1977. Scripts, plans,
goals, and understanding: An enquiry into human
knowledge structures. Erlbaum.
Alister Scott, Alana Gilbert, and Ayele Gelan. 2007.
The urban-rural divide: Myth or reality? Macaulay
Institute Aberdeen.
Kim Bartel Sheehan. 2018. Crowdsourcing research:
data collection with amazon’s mechanical turk. Com-
munication Monographs, 85(1):140–156.
Muzafer Sherif and Carolyn W Sherif. 1953. Groups
in harmony and tension; an integration of studies of
intergroup relations.
Baoxu Shi and Tim Weninger. 2018. Open-world knowl-
edge graph completion. In Proceedings of the Thirty-
Second AAAI Conference on Artificial Intelligence,
(AAAI-18), the 30th innovative Applications of Arti-
ficial Intelligence (IAAI-18), and the 8th AAAI Sym-
posium on Educational Advances in Artificial Intel-
ligence (EAAI-18), New Orleans, Louisiana, USA,
February 2-7, 2018, pages 1957–1964. AAAI Press.
Richard A Shweder. 1990.
In defense of moral re-
alism: Reply to gabennesch. Child Development,
61(6):2060–2067.
Richard Socher, Danqi Chen, Christopher D. Manning,
and Andrew Y. Ng. 2013. Reasoning with neural
tensor networks for knowledge base completion. In
Advances in Neural Information Processing Systems
26: 27th Annual Conference on Neural Information
Processing Systems 2013. Proceedings of a meet-
ing held December 5-8, 2013, Lake Tahoe, Nevada,
United States, pages 926–934.
Robyn Speer, Joshua Chin, and Catherine Havasi. 2017.
Conceptnet 5.5: An open multilingual graph of gen-
eral knowledge. In Proceedings of the Thirty-First
AAAI Conference on Artificial Intelligence, February
4-9, 2017, San Francisco, California, USA, pages
4444–4451. AAAI Press.
Cass R Sunstein. 1996. Social norms and social roles.
Colum. L. Rev., 96:903.
Zeerak Talat, Hagen Blix, Josef Valvoda, Maya Indira
Ganesh, Ryan Cotterell, and Adina Williams. 2022.
On the machine learning of ethical judgments from
natural language. In Proceedings of the 2022 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies, pages 769–779, Seattle, United
States. Association for Computational Linguistics.
Alon Talmor, Jonathan Herzig, Nicholas Lourie, and
Jonathan Berant. 2019. CommonsenseQA: A ques-
tion answering challenge targeting commonsense
knowledge. In Proceedings of the 2019 Conference
of the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4149–4158, Minneapolis, Minnesota. Association for
Computational Linguistics.
Edward H Thompson Jr and Joseph H Pleck. 1986. The
structure of male role norms. American Behavioral
Scientist, 29(5):531–543.
Trieu H Trinh and Quoc V Le. 2018.
A simple
method for commonsense reasoning. ArXiv preprint,
abs/1806.02847.
Aditya Nrusimha Vaidyam,
Hannah Wisniewski,
John David Halamka, Matcheri S Kashavan, and
John Blake Torous. 2019. Chatbots and conversa-
tional agents in mental health: a review of the psychi-
atric landscape. The Canadian Journal of Psychiatry,
64(7):456–464.
Leon van Rijswijk and Antal Haans. 2018. Illuminating
for safety: Investigating the role of lighting appraisals
on the perception of safety in the urban environment.
Environment and behavior, 50(8):889–912.
Paul Vicol, Makarand Tapaswi, Lluís Castrejón, and
Sanja Fidler. 2018. Moviegraphs: Towards under-
standing human-centric situations from videos. In
2018 IEEE Conference on Computer Vision and Pat-
tern Recognition, CVPR 2018, Salt Lake City, UT,
USA, June 18-22, 2018, pages 8581–8590. IEEE
Computer Society.
Iris Vilnai-Yavetz and Shaked Gilboa. 2010. The effect
of servicescape cleanliness on customer reactions.
Services Marketing Quarterly, 31(2):213–234.
Cunxiang Wang, Shuailong Liang, Yue Zhang, Xiaonan
Li, and Tian Gao. 2019. Does it make sense? and
why? a pilot study for sense making and explana-
tion. In Proceedings of the 57th Annual Meeting of
the Association for Computational Linguistics, pages
4020–4026, Florence, Italy. Association for Compu-
tational Linguistics.
Jason Weston, Antoine Bordes, Oksana Yakhnenko, and
Nicolas Usunier. 2013. Connecting language and
knowledge bases with embedding models for relation
extraction. In Proceedings of the 2013 Conference

--- Page 16 ---

on Empirical Methods in Natural Language Process-
ing, pages 1366–1371, Seattle, Washington, USA.
Association for Computational Linguistics.
Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng
Gao, Kevin Duh, and Benjamin Van Durme. 2018.
Record: Bridging the gap between human and ma-
chine commonsense reading comprehension.
Caleb Ziems, Jane A. Yu, Yi-Chia Wang, Alon Y.
Halevy, and Diyi Yang. 2022. The moral integrity
corpus: A benchmark for ethical dialogue systems.
In Proceedings of the 60th Annual Meeting of the
Association for Computational Linguistics and the
12th International Joint Conference on Natural Lan-
guage Processing, Dublin, Ireland. Association for
Computational Linguistics.

--- Page 17 ---

A
Models & Hyperparameters
Classification.
We use the base versions of BERT
(Devlin et al.; 768-hidden, 12-heads, 110M param-
eters), RoBERTa (Liu et al.; 768-hidden, 12-heads,
125M parameters), and ALBERT-v2 (Lan et al.;
768-hidden, 12-heads, 11M parameters). For each
model, we fine-tune using AdamW (Loshchilov
and Hutter, 2019) for 7 epochs with a batch size of
16 and a learning rate of 1e−5. These hyperparam-
eters were chosen by hyperparameter search on the
dev set over {1e −5, 2e −5, 3e −5, 5e −5} and
the number of epochs in {1..8}, with ϵ = 1e −8
and the batch size set to 16.
Generation.
We trained BART-large (406M pa-
rameters), GPT-2 (768-hidden, 12-heads, 117M
parameters), and T5-small (512-hidden, 8 heads,
60M parameters) for 1 epoch using a batch size of
8 and a learning rate of 3e −5. We also prompted
GPT-3 Davinci-002 and Davinci-003 in a few-shot
manner via the OpenAI API, using the following
prompt, which contains seven representative data-
points from the NORMBANK train set:
It is UNEXPECTED to "talk about sex" at an "cafe" when:
+ PERSON’s role is ’barista’
It is OKAY to "listen to music" in an "arcade" when all of
,→the following are true:
+ PERSON’s role is not ’cook’
+ PERSON’s role is not ’maintenance worker’
+ PERSON’s behavior is ’wear headphones’
It is EXPECTED to "hang film to dry" at the "darkroom" when
,→all of the following are true:
+ PERSON’s role is ’darkroom technician’
+ PERSON’s behavior is ’performing routine tasks’
It is OKAY to "smoke a cigar" in a "limousine" when all of
,→the following are true:
+ OTHER’s age bracket is not ’gradeschooler or younger’
+ OTHER’s attitude towards smoking is not ’bothered by smoke’
,→
+ PERSON’s age bracket is ’adult’
+ limousine rules is not ’forbids smoking’
It is EXPECTED to "maintain the store appearance" at the "
,→clothing store" when all of the following are true:
+ PERSON’s role is ’store owner’
It is OKAY to "talk to yourself" on an "airplane" when all
,→of the following are true:
+ PERSON’s role is ’passenger’
+ PERSON’s behavior is ’pray’
It is UNEXPECTED to "grow tomatoes" in a "garden" when all
,→of the following are true:
+ PERSON’s behavior is not ’use a greenhouse’
+ temperature is ’freezing’
It is {norm} to "{behavior}" {prep} {det} "{setting}" when
,→all of the following are true:
+
B
Additional Details on Constructing
SCENE
B.1
The Environment
Country of Operation
is seeded with the 195
countries from the UN (2022) list of member or
non-member observer states.
Operational Factors
is a broad category of con-
straints from environmental psychology (Bell et al.,
2001) involving one’s comfort and ease of oper-
ation in an environment. Such factors influence
descriptive norms. Operational behaviors can be
influenced by the degree of sensory stimulation,
as well as by privacy and proxemics, or the local
density and organization of persons and objects
(Russell and Ward, 1982). These inform the follow-
ing subcategories: attendance {empty, there are
people around, crowded} (Altman, 1975); clean-
liness {dirty, clean} (Vilnai-Yavetz and Gilboa,
2010; Cialdini et al., 1990); noise {quiet, mod-
erate, loud} (Mathews and Canon, 1975); pop-
ulation density {urban, suburban, rural} (Scott
et al., 2007); and privacy {private, public} (Alt-
man, 1975).
Physical Conditions
in the environment can in-
fluence behavior mechanically as well as psycho-
logically. Specifically, the lighting {bright, moder-
ate, dim, dark}, weather {blizzard, clear, cloudy,
...}, and temperature {freezing, cold, temperate,
hot} can directly impact visibility, coordination,
and the perception of safety (Boyce et al., 2000;
van Rijswijk and Haans, 2018), as well as comfort,
confidence, and altruism (Cunningham, 1979).
Restrictions
formally limit attendance, participa-
tion, and behavior. The environment can be one
of exclusion {adults only, men only, women only},
formality {formal, informal} or religiosity {sa-
cred, secular}. These categories are not part of our
original theoretical taxonomy but were introduced
through annotator feedback (See Section 4).
Special Observances
include cultural obser-
vances like holidays {Advent, Holi, Lunar New
Year} as well other special events {bat mitzvah,
housewarming, quinceañera}, which evoke distinct
rituals, customs and norms (Durkheim, 1915).
Time
constraints include day of the week, sea-
son, time of day, and time period. Like special
observances, much of human activity adheres to a
set of temporal constraints and cues (Janicik and
Bartel, 2003).
B.2
Behaviors
Since the average string length of behaviors was
greater and thus more prone to error, we applied
a suite of programmatic cleaning and filtering
techniques, followed by a manual filtering round
that reduced the average to 112.6 clean and non-

--- Page 18 ---

redundant behaviors per setting. The filtering tech-
niques are as follows:
1. Remove any conditional form “if you were...”
as well as any mention of the role or the setting
in the behavior itself
2. Remove elaborations on behaviors “<behav-
ior> because ... <elaboration>”
3. Normalize the logical form by removing
words that negate behaviors (do not, never,
not, forget to, refuse to, fail to, anything, some-
thing, anyone, someone, in any way, any)
4. Remove biased terms like properly, should,
would, try to, be able to, and see someone.
5. Remove any bullet points or stray characters
6. Require that the behavior has an active (not
passive) verb in it and that the verb does not
have an explicit subject and that there is no
dependent clause (as indicated by the marker
[mark] dependency).
C
Annotation Task Details
C.1
Qualification Task
To qualify for the HIT, workers were required to
pass the following qualifying test, answering at
least 5 out of 6 questions correctly.
1. True or False: you are allowed to add your
own Constraints by typing them directly into
the box. [Answer: True]
2. True or False: “carry a gun” can be an “Ex-
pected” behavior on an Airplane. [Answer:
True]
3. True or False: “read a book” is an “Expected”
behavior for a passenger on an Airplane. [An-
swer: False]
4. True or False: it is possible for a BEHAVIOR
to be both “Expected” and “Okay” under the
same Constraints. [Answer: False]
5. Let’s say you are adding some Constraints for
when “eating shrimp” is “Unexpected” in the
SETTING: restaurant. You know that shellfish
are disallowed in both Hinduism and Judaism,
as well as by the vegan and vegetarian diets.
You are thinking of adding these in the follow-
ing Constraint table. Is this correct? [Answer:
Incorrect]
(PERSON’s religion is Judaism)
AND (PERSON’s religion is Hin-
duism) AND (PERSON’s diet is ve-
gan) AND (PERSON’s diet is vege-
tarian)
6. Let’s say you are adding some Constraints for
when "eating shrimp" is "Okay" in the SET-
TING: restaurant. You know that shellfish are
disallowed in both Hinduism and Judaism, as
well as by the vegan and vegetarian diets. You
are thinking of adding these in the following
Constraint table. Is this correct? [Answer:
Correct]
(PERSON’s religion is NOT Ju-
daism) AND (PERSON’s religion is
NOT Hinduism) AND (PERSON’s
diet is NOT vegan) AND (PER-
SON’s diet is NOT vegetarian)
C.2
HIT Interface
For each HIT, the annotator is presented with a
setting s ∈S and a behavior b ∈B that we gen-
erated for the given s. The annotator helps us de-
scribe when this behavior would be expected; then
describes when it is merely okay; and finally un-
expected. Annotators describe each norm with the
conjunction and disjunction of SCENE constraints.
The annotator appends each constraint to its con-
junction as a 4-tuple consisting of a (1) category,
(2) name, (3) relation, and (4) value. These are
shown with examples in the HIT Instructions (4)
and HIT Interface (Figure 5) screenshots. The cate-
gory helps annotators search for constraints and or-
ganize their thoughts. The category is a high-level
designation of where the constraint is organized:
according to the environment, role, attribute, or be-
havior. The name, relation and value constitute a
standard semantic triple. The name designates the
subject of the constraint, and it a specification of
the category, like the “temperature of the environ-
ment.” The relation is a logical type that includes
equality and inequality. The value designates the
predicate of the constraint (e.g., “freezing”).
Annotators can build constraint 4-tuples from
drop-down menus that enumerate our hierarchi-
cal taxonomy (Section 3). Annotators can also
freely edit the above fields and contribute novel con-
straints. Finally, annotators compose constraints
into disjunctive normal form (DNF), the OR of
ANDs, to describe when behaviors are expected,
okay, or unexpected in a given setting.

--- Page 19 ---

Figure 4: HIT Instructions.

--- Page 20 ---

Figure 5: HIT Interface

```
