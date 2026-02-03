---
title: "Value Profiles for Encoding Human Variation - PDF Extract"
source_pdf: "2025-Sorensen-Value Profiles for Encoding Human Variation.pdf"
pages: 49
extracted_at: "2026-01-24T16:38:36.493842"
---

# PDF Extract: Value Profiles for Encoding Human Variation

**Source PDF:** 2025-Sorensen-Value Profiles for Encoding Human Variation.pdf
**Total Pages:** 49

---

## Content

```
--- Page 1 ---

Value Profiles for Encoding Human Variation
Taylor Sorensen1†, Pushkar Mishra2, Roma Patel2, Michael Henry Tessler2,
Michiel Bakker2, Georgina Evans2, Iason Gabriel2, Noah Goodman2, Verena Rieser2
1Department of Computer Science, University of Washington, Seattle, WA, USA
2Google DeepMind, London, UK
†Work done during an internship at Google DeepMind.
tsor13@cs.washington.edu, verenarieser@deepmind.com
Abstract
Modelling human variation in rating tasks is
crucial for personalization, pluralistic model
alignment, and computational social science.
We propose representing individuals using nat-
ural language value profiles – descriptions of
underlying values compressed from in-context
demonstrations – along with a steerable de-
coder model that estimates individual ratings
from a rater representation. To measure the
predictive information in a rater representation,
we introduce an information-theoretic method-
ology and find that demonstrations contain the
most information, followed by value profiles,
then demographics. However, value profiles ef-
fectively compress the useful information from
demonstrations (>70% information preserva-
tion) and offer advantages in terms of scrutabil-
ity, interpretability, and steerability. Further-
more, clustering value profiles to identify simi-
larly behaving individuals better explains rater
variation than the most predictive demographic
groupings. Going beyond test set performance,
we show that the decoder predictions change in
line with semantic profile differences, are well-
calibrated, and can help explain instance-level
disagreement by simulating an annotator pop-
ulation. These results demonstrate that value
profiles offer novel, predictive ways to describe
individual variation beyond demographics or
group information.
1
Introduction
Machine learning systems are traditionally trained
to approximate a single “ground truth" label, treat-
ing annotator disagreement as noise. However,
many important tasks such as chat preferences,
hate speech, and toxicity detection can have legiti-
mate disagreement (Aroyo and Welty, 2015; Plank,
2022). Modelling this heterogeneity is important
for pluralistic model alignment (Sorensen et al.,
2024b), unbiased model safety, content modera-
tion, personalization, and more.
We characterize three approaches to variation
modelling: (1) Distributional Population Mod-
elling, which directly models the distribution of la-
bels for a given rater population (Zhang et al., 2024;
Siththaranjan et al., 2024). This approach accounts
for variance and valid disagreements between an-
notators but requires many raters labeling the same
instances and doesn’t model which raters disagree
or why. (2) Grouping by Characteristics such
as demographics or annotation similarity. While
grouping approaches can lead to higher agreement
than the broader rater population, they still do not
account for intra-group disagreement (Hwang et al.,
2023; Prabhakaran et al., 2024), potentially lead-
ing to flattening variance or stereotyping. To cap-
ture intra-group variation, distributional learning is
needed (Meister et al., 2024). Grouping by annota-
tion similarity also requires significant overlap in
labeled instances (Li et al., 2024). (3) Individual
Modelling. At the individual level (Gordon et al.,
2022; Jiang et al., 2024), the target is a single "cor-
rect" answer instead of a distribution,1 allowing for
standard supervised methods. Additionally, we can
obtain group or population distributions through
marginalization. Individual modeling also removes
the requirement for raters to have any instance over-
lap. Because of these advantages, we argue for and
focus on improving individual modeling in order to
better model human variation (for more, see App.
B, Fig. A1). However, this raises the question -
how should we represent an individual?
In this work, we propose to model rater variation
using individual, free-text value profiles – inter-
pretable natural language descriptions of human
values that explain observed rating variation (§2).
In §3, we introduce a methodology to measure
the information content of possible rater represen-
tations. We carry out a series of experiments to
1At least, to the degree that people are self-consistent
(Abercrombie et al., 2023).
arXiv:2503.15484v2  [cs.CL]  30 Sep 2025

--- Page 2 ---

pro-car; ﬁscal 
conservatism; 
preference for 
existing 
systems …
social justice, 
equality; pro-
immigration 
stance; pro-
european…
…
…
 Strong yes
Neutral
Encoder Q compresses rater 
representation as values
Decoder P uses value representation to 
predict ratings conditioned on values
…
Is high immigration 
good for the UK?
 Should we ban cars 
in city centers?
Age: 40 
Gender: Female 
… 
Income: £70k
 Demographics 
Age: 40 
Gender: Female 
… 
Income: £70k
 Demographics 
 Should we ban cars 
in city centers?
No
Yes
va
Generated Value 
Proﬁle for Rater A
vb
Generated Value 
Proﬁle for Rater B
Fit dataset  
of n in-context 
ratings (      )
B
bBU0lEqseiCB4r2g9oQ9lsN+3SzSbsToQS+hO8eFDEq7/Im/GbZuDVh8MPN6bYWZekEh0HW/nMLK6tr6RnGztLW9s7tX3j9omTjVjDdZLGPdCajhUijeRIGSdxLNaRI3g7G1zO/ci1EbF6wEnC/YgOlQgFo2il+5
u+6pcrbtWdg/wlXk4qkKPRL3/2BjFLI6QSWpM13MT9DOqUTDJp6VeanhC2ZgOedSRSNu/Gx+6pScWGVAwljbUkjm6s+JjEbGTKLAdkYUR2bZm4n/ed0Uw0s/EypJkSu2WBSmkmBMZn+TgdCcoZxYQpkW9lbCRlRTh
jadkg3BW375L2mdVb1atXZ3Xqlf5XEU4QiO4RQ8uIA63EIDmsBgCE/wAq+OdJ6dN+d90Vpw8plD+AXn4xseBI21</latexit>En
Held-out eval 
questions
q
h69LBbBU0lEqseiF48V7Ae0oWy2k3bpZhN3J0IJ/RNePCji1b/jzX/jts1BWx8MPN6bYWZekEh0HW/ncLa+sbmVnG7tLO7t39QPjxqmTjVHJo8lrHuBMyAFAqaKFBCJ9HAokBCOxjfzvz2E2gjYvWAkw
T8iA2VCAVnaKVOo9/DESDrlytu1Z2DrhIvJxWSo9Evf/UGMU8jUMglM6bruQn6GdMouIRpqZcaSBgfsyF0LVUsAuNn83un9MwqAxrG2pZCOld/T2QsMmYSBbYzYjgy95M/M/rphe+5lQSYqg+GJRmEq
KMZ09TwdCA0c5sYRxLeytlI+YZhxtRCUbgrf8ipXVS9WrV2f1mp3+RxFMkJOSXnxCNXpE7uSIM0CSeSPJNX8uY8Oi/Ou/OxaC04+cwx+QPn8wf/HI/2</latexit>Pω
Qω
Strong No
Neutral
Strong Yes
0
10
20
30
40
Strong No
Neutral
Strong Yes
0
10
20
30
40
Is high immigration 
good for the UK?
Is high immigration 
good for the UK?
Should we ban cars 
in city centres?
Should we ban cars 
in city centres?
}
}
 Strong yes
 Strong yes
 Yes
Yes
 Strong yes
 Neutral
Yes
 Strong yes
 No
Value 
Encoder
Steerable 
Decoder
Should we be in favour of 
universal basic income?
Should we be in favour of 
universal basic income?
xj
x1
y
ZbaDUDwnc6QA7kM=">AB6nicdVDJSgNBEK2JW4xb1KOXxiB4CjNBoseAF48RzQLJEH
o6PUmTnp6hu0YMQz7BiwdFvPpF3vwbOxu4Pih4vFdFVb0gkcKg634uZXVtfWN/GZha3
tnd6+4f9A0caoZb7BYxrodUMOlULyBAiVvJ5rTKJC8FYwup37rjmsjYnWL4T7ER0oEQ
pG0Uo39z2vVyx5ZXcG8j8pwQL1XvG9249ZGnGFTFJjOp6boJ9RjYJPil0U8MTykZ0wD
uWKhpx42ezUyfkxCp9EsbalkIyU79OZDQyZhwFtjOiODQ/van4l9dJMbzwM6GSFLli80
VhKgnGZPo36QvNGcqxJZRpYW8lbEg1ZWjTKdgQ3OXLv8kyhGal7FXL1euzUq2yiCMPR
3AMp+DBOdTgCurQAYDeIAneHak8+i8OK/z1pyzmDmEb3DePgENgY2b</latexit>x1
xk
xi
B
EK2JW4xb1KOXxiB4CjNBoseAF48RzQLJEHo6PUmTnp6hu0YMQz7BiwdFvPpF3vwbOxu4Pih4vFdFVb0gkcKg634uZXVtfWN/GZha3tnd6+4f9A0caoZb7BYxrodUMOlULyBAiVv
J5rTKJC8FYwup37rjmsjYnWL4T7ER0oEQpG0Uo39z3RK5a8sjsD+Z+UYIF6r/je7csjbhCJqkxHc9N0M+oRsEknxS6qeEJZSM64B1LFY248bPZqRNyYpU+CWNtSyGZqV8nMhoZ
M4C2xlRHJqf3lT8y+ukGF74mVBJilyx+aIwlQRjMv2b9IXmDOXYEsq0sLcSNqSaMrTpFGwI7vLl32QZQrNS9qrl6vVZqVZxJGHIziGU/DgHGpwBXVoAIMBPMATPDvSeXRenNd
5a85ZzBzCNzhvn2JhjdM=</latexit>xi
B
EK2JW4xb1KOXxiB4CjNBoseAF48RzQLJEHo6NUmTnp6huycQhnyCFw+KePWLvPk3djZwfVDweK+KqnpBIrg2rvh5NbWNza38tuFnd29/YPi4VFTx6li2GCxiFU7oBoFl9gw3Ahs
JwpFAhsBaPrmd8ao9I8lvdmkqAf0YHkIWfUWOlu3At6xZJXducg/5MSLFHvFd+7/ZilEUrDBNW647mJ8TOqDGcCp4VuqjGhbEQH2LFU0gi1n81PnZIzq/RJGCtb0pC5+nUio5HW
kyiwnRE1Q/3Tm4l/eZ3UhFd+xmWSGpRsShMBTExmf1N+lwhM2JiCWK21sJG1JFmbHpFGwI7url32QVQrNS9qrl6u1FqVZxpGHEziFc/DgEmpwA3VoAIMBPMATPDvCeXRenNd
Fa85ZzhzDNzhvn1S5jco=</latexit>vb
vb
qyk7q4oTU5LyAk=">AB6nicbVBNS8NAEJ34WetX1aOXxSJ4KkmR6rHgxWNF+wFtKJ
Ptpl262YTdTaGE/gQvHhTx6i/y5r9x2+agrQ8GHu/NMDMvSATXxnW/nY3Nre2d3cJecf
/g8Oi4dHLa0nGqKGvSWMSqE6BmgkvWNwI1kUwygQrB2M7+Z+e8KU5rF8MtOE+REOJQ
85RWOlx0kf+6WyW3EXIOvEy0kZcjT6pa/eIKZpxKShArXuem5i/AyV4VSwWbGXapYgHe
OQdS2VGDHtZ4tTZ+TSKgMSxsqWNGSh/p7IMNJ6GgW2M0Iz0qveXPzP6YmvPUzLpPUME
mXi8JUEBOT+d9kwBWjRkwtQaq4vZXQESqkxqZTtCF4qy+vk1a14tUqtYfrcr2ax1GAc
7iAK/DgBupwDw1oAoUhPMrvDnCeXHenY9l64aTz5zBHzifP1Amjck=</latexit>va
va
u
SOY3Cufv5HNg7Wo=">AB7XicbVBNS8NAEJ3Ur1q/qh69LBbBU0mKVI8FLx4r2A9oQ9
lsN+3azW7Y3Qgh9D948aCIV/+PN/+N2zQHbX0w8Hhvhpl5QcyZNq7ZQ2Nre2d8q7lb
39g8Oj6vFJV8tEdohkvVD7CmnAnaMcxw2o8VxVHAaS+Y3S783hNVmknxYNKY+hGeCB
Yygo2Vuko8/B8VK25dTcHWideQWpQoD2qfg3HkiQRFYZwrPXAc2PjZ1gZRjidV4aJpj
EmMzyhA0sFjqj2s/zaObqwyhiFUtkSBuXq74kMR1qnUWA7I2ymetVbiP95g8SEN37GRJ
wYKshyUZhwZCRavI7GTFieGoJorZWxGZYoWJsQFVbAje6svrpNuoe8168/6q1moUc
ZThDM7hEjy4hbcQRs6QOARnuEV3hzpvDjvzseyteQUM6fwB87nD4p0jxM=</latexit
>y1a
y1b
yja
ykb
Dﬁt
Da
Db
Rater A
Rater B
U
lQ=">ACAnicbVDLSgNBEJyNrxhfq57Ey2IQPIXdINFjQA8eI5gHJGuYnXSIbMPZnqDYQle/BUvHhTx6ld482+cTfa
giQUNRVU3V1eJLhC2/42ciura+sb+c3C1vbO7p65f9BQYSwZ1FkoQtnyqALBA6gjRwGtSAL1PQFNb3SV+s0xSMXD4A4
nEbg+HQS8zxlFLXNo45PcioSK6n9x2EB5R+AmMqpl2zaJfsGaxl4mSkSDLUuZXpxey2IcAmaBKtR07QjehEjkTMC1
0YgURZSM6gLamAfVBucnshal1qpWe1Q+lrgCtmfp7IqG+UhPf053pwWrRS8X/vHaM/Us34UEUIwRsvqgfCwtDK83D6nE
JDMVE8ok17dabEglZahTK+gQnMWXl0mjXHIqpcrtebFazuLIk2NyQs6IQy5IldyQGqkTRh7JM3klb8aT8WK8Gx/z1py
RzRySPzA+fwBsy5gQ</latexit>
Deval
Pω(yia|xi, va)
Pω(yib|xi, vb)
Predicted rating 
distribution given 
value proﬁles
Figure 1: The value profile autoencoder setup. Decoder outputs are from trained profile decoder while demographics
are illustrative to preserve privacy. The encoder extracts/compresses value information from rater examples, and the
decoder changes predictions on held-out questions according to the value profile.
evaluate our value profile system and other rater
representations (§4, 5). In §6, we introduce a rater
clustering algorithm that uncovers better groupings
than the most predictive demographics, while loos-
ening the typical requirement of annotators labeling
overlapping instances. In other experiments, we
find that our value profile system is interpretable,
well-calibrated, and helps explain rater disagree-
ment (§7). We conclude by discussing related work
(§8), directions for future work (§9), and ethical
advantages (and risks) of our approach (§11).
2
Modelling Human Annotator Variation
2.1
Rater Representations
Let R = {r1, r2, . . . , rNR} be the raters who we
wish to model, X = {x1, x2, . . . , xNX} be the
space of instances, and Y = {y1, y2, . . . , yNY } be
the space of potential responses/ratings. We would
like to model Y | X, R. However, because we
don’t have sufficient information to represent (or
observe) the rater r, we compare different potential
representations for r:
• ∅: No information about r.
In this case,
P(Y | X, ∅(r)) = P
r′∈R P(Y | X, r′) =
P(Y | X), or the label distribution for the
input marginalized over all raters.
• D: Demographic information about r. P(Y |
X, D(r)). 2
2In the case that many demographics are provided, this
is sometimes called a “persona" (Cheng et al., 2023). We
also refer to this as “demographics (all)" or “intersectional
demographics". This is in contrast to trying to model an entire
• En: n in-context ratings as demonstrations
from rater r. P(Y | X, En(r)).
• V : A value profile natural language descrip-
tion of the rater’s values which are relevant
for the task. P(Y | X, V (r)).
A value profile might be elicited directly from a
rater r through a survey/value elicitation process.
In absence of this data, we propose to infer V from
observed example ratings En through an autoen-
coder setup.
2.2
Autoencoding Rater Values
Let ri be a particular rater i drawn from the pop-
ulation of n raters, xj be a particular instance j,
and yij be the rating that rater i gave to instance
j. Let Di = {yi1, yi2, . . . , yiNi} be the set of Ni
ratings we have for rater i. We can build a lan-
guage model encoder Qϕ which estimates a value
profile for each rater ri from a set of (fit) demon-
strations drawn from Di, with corresponding prob-
ability distribution qϕ : En →V . Similarly, a
decoder Pθ can estimate the label probability distri-
bution P(Y|X, V (R)) ≈pθ : X, V →Y. Given
this, the entire autoencoder system can be eval-
uated by sampling a value profile from the en-
coder vi ∼qϕ(En(ri)) and calculating the (cross-
entropy) loss on unseen examples.
We randomly partition the instances into Dfit
i for
fitting a value profile and Deval
i
to train the decoder
to generalize to held-out ratings. The setup may be
seen as a way to “compress” predictive information
demographic group at a time.

--- Page 3 ---

The following is a UK opinion 
survey. 
 
Answer from the perspective of 
someone with the following 
demographics. 
 
Demographics: Age: 40, Gender: 
Female, ..., Party: Labour, 
Income: £50k 
 
Question: Should we be in favor 
of UBI? 
Answer: <get logit distribution>
The 
following is 
a UK opinion 
survey. 
 
Question: 
Should we be 
in favor of 
UBI? 
Answer: <get 
logit 
distribution
>
The following is a UK opinion 
survey. 
 
Answer from the perspective of 
someone with the value profile. 
 
Value profile: Compassion and 
empathy, Social justice and 
equality... 
 
Question: Should we be in favor 
of UBI? 
Answer: <get logit distribution>
The following is a UK opinion survey. 
 
Question: Should we ban cars in city 
centers? 
Answer: Strong yes 
 
Question: Is high immigration overall 
good for the UK? 
Answer: Yes 
... 
 
Question: Should we be in favor of UBI? 
Answer: <get logit distribution>
En : In-context examples
V : Value proﬁle
D : Demographic information
→: No info
Figure 2: Rater representations and example corresponding decoder prompts (∅, D, V , En). The decoder predicts
the rater’s annotation given the rater representation.
about a rater’s labeling process from their examples
En(ri) to a natural language value profile vi.
In practice, we initialize the encoder and decoder
parameters ϕ and θ as prompted language models
(prompts in Figs. A9/A10). For the experiments
in the paper, we freeze the encoder parameters and
optimize the decoder directly with supervised fine-
tuning. We choose to do this 1) as prompted lan-
guage models performed quite well at encoding,
preserving > 70% of usable information. (cf. Eq.
3, Fig. 5), 2) in order to regularize the encoder to
remain human understandable/interpretable, and 3)
to preserve generalizability across datasets.
We compare against the alternative rater repre-
sentations of no information ∅, demographics D,
and examples En, by similarly fitting a decoder
Dθ to estimate pθ(Y|X, ·). All parameters are ini-
tialized with a prompted language model. To en-
sure comparable results, we use Dfit demonstra-
tions for the in-context demonstrations En and in-
ferring value profiles in training and testing and
the Deval demonstrations as held-out targets for all
rater representations.
3
Estimating Usable Rater Information
We wish to compare the usable information for
each rater representation. To do this, we extend
Xu et al. (2020)’s concept of V-information, which
was created to analogize the concept of mutual
information between random variables A, B to
constrained computational families. We extend
V-information to the case where we have a third
random variable, C, with computational family
V ⊆{f : A ∪{∅}, C →P(B)}:
HV(B | A, C) = inf
f∈V Ea,b,c∼A,B,C[−log f[a, c](b)]
(1)
IV(A →B | C) = HV(B | ∅, C)−HV(B | A, C)
(2)
We can then measure predictive information
from each rater representation (∅, D, En, V ) to
ratings Y, given instances X. I.e., we can estimate
how much more we know about how a rater will
respond given particular information about them,
as compared to knowing nothing about the rater.
As Ethayarajh et al. (2022) show in a similar
extension of V-information, assuming we have an
i.i.d. dataset of observations, we can get an unbi-
ased estimate of this quantity for a computational
family by training a model in each informational
setting and comparing the held-out test losses to
a trained model with no information. For more
details, see Algorithm 1 (inspired by Ethayarajh
et al. 2022). To contextualize the algorithm with
an example loss plot, see Figure A2.
Algorithm 1 Computing Predictive V-Information
Input:
• Training data Dtrain = {(ri, xj, yij)} = {(ri, xj, yij) :
(xj, yij) ∈Rtest
i , ri ∈train raters Rtrain}
• Test data Dtest for held-out raters Rtest, Rtrain ∩Rtest = ∅
• Initialized decoder d, a prompted, pretrained LM
• Natural language rater representation g : R →NL
dg
←finetune d on {(g(ri), xj, yij)|(ri, xj, yij)
∈
Dtrain}
▷Train w/ rater information
d∅←finetune d on {(∅, xj, yij)|(ri, xj, yij) ∈Dtrain} ▷
Train w/out rater information
HV (Y|X), HV (Y|X, g(R)) ←0, 0
for (ri, xj, yij) ∈Dtest do ▷Accumulate average held-out
test losses
HV (Y|X) ←HV (Y|X) −
1
|Dtest| log d∅(xj, ∅)(yij)
HV (Y|X, g(R))
←
HV (Y|X, g(R))
−
1
|Dtest| log dg(xj, g(ri))(yij)
end for
ˆIV (g(R) →Y|X) ←HV (Y|X) −HV (Y|X, g(R))
▷
Predictive information is drop in test loss when including
rater information
4
Experimental Methodology
Training details
We split raters into 50/50
train/test splits and report results for training/test

--- Page 4 ---

Dataset
Task
Choices
Dem.
Inst.
Raters
Ratings
OpinionQA W27 (OQA)
Opinions (US)
2-6
11
77
10k
731k
Hatespeech-Kumar (HK)
Hate Speech
2
18
19k
864
37k
DICES (DIC)
Toxicity
3
5
990
160
65k
ValuePrism (VP)
Moral Judgments
3
-
31k
4.5k
199k
Habermas-Likert (HL)∗
Opinions (UK)
7
9
1.1k
259
3.1k∗
Prism (PR)∗
Chat Preference
2
20
8.0k
1.4k
8.0k∗
Table 1: Dataset statistics including task information, number of multiple choice options (Ch.), demographic
variables (Dem), unique instances (#I), unique raters (#R), and total ratings (#Rat). Datasets: OQA (Santurkar et al.,
2023), HK (Kumar et al., 2021), DIC (Aroyo et al., 2023), VP (Sorensen et al., 2024a), HL (Tessler et al., 2024),
and PR (Kirk et al., 2024b). Numbers may be smaller than in original datasets due to preprocessing/sampling (see
§A). ∗Results are noisier for datasets with <10k ratings due to underfit models/small test sets.
runs on five random splits.
We draw |Dfit
i | ∼
U({2, . . . , |Di| −2}) to ensure that we have
variable-sized fit/eval splits with at least two in-
stances each. We train the decoder (gemma2-9b-pt,
Gemma Team et al. 2024) for a single epoch (impor-
tant for maintaining calibration, Ji et al. 2021). For
encoders, we use gemma2-9b-it, gemma2-27b-it
(Gemma Team et al., 2024), and Gemini-1.5 Pro
(Team et al., 2024). See App. A for details.
Datasets We utilize six datasets intended for
research (Table 1) spanning tasks relevant to model
alignment, content moderation, and computational
social science. These datasets feature forced choice
selection tasks and were selected to contain 1) some
rater variation due to their subjective nature, 2) an-
notator IDs to link annotations from the same rater,
and 3) ideally, some demographic information. Pre-
processing information in §A.
5
Performance Across Rater
Representation Settings
Detailed results for held-out test losses across rater
representations can be found in Figure 3. Accura-
cies can be found in App. A3, but results mirror the
loss results, which we will focus on. Detailed re-
sults for held-out test losses and accuracies across
rater representations can be found in Figures 3 and
A3 respectively.
We note that error bars are much larger for 2
datasets, HL and PR. We believe that this is mainly
because the datasets are smaller (<10k ratings),
which means that 1) the trained model may be un-
derfit and 2) there is a smaller sample size for each
test split. We include results for all datasets for
maximal inclusion, but focus our attention on the
large datasets (>30k ratings: OQA, HK, DIC, VP)
for which we can make higher confidence compar-
isons across settings.
Now, we compare decoder performance across
rater representation settings (see Figs. 3, 4, A3).
Our main findings are:
In-context examples improve predictions.
Across all four large datasets, providing the decoder
with in-context examples of the rater’s previous an-
notations significantly improved the prediction of
their ratings on held-out test data in both accuracy
and test loss (p < .001). We observe a similar,
but less significant, drop in loss/increase in accu-
racy on the two small datasets. This shows that
rater demonstrations offer useful information for
disentangling human variation.
Value profiles are highly predictive. Value pro-
files generated by Gemini (version: 1.5-pro) con-
sistently provided a significant performance boost
across all four large datasets, suggesting value pro-
files contain useful information for modeling vari-
ation. Gemma2-9b and 27b value profiles also of-
fered a significant boost for three of the four large
datasets (VP, OQA, and HK), but not for DICES. In
other words, as one might expect, value profiles im-
prove with scale. As a result, we will focus the re-
mainder of our experiments on the top-performing
value profiles from Gemini.
Value profiles effectively compress rater in-
formation. Since the value profiles are encoded
from the same in-context examples used in the max-
imal example setting, we can exactly calculate the
amount of decoder-usable information preserved
(see Figure 5):
IV(V (En(R)) →Y | X)
IV(EN(R) →Y | X)
(3)
Value profiles effectively compressed the relevant
information from in-context examples, preserving
>70% of the usable information for the four large
datasets. This indicates that value profiles are an
efficient way to represent human variation.
Demographics have limited predictive power.
Intersectional demographics generally offered a

--- Page 5 ---

no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)1 ex2 ex4 ex8 ex
16 ex
32 ex
0.8
1
1.2
OpinionQA
dataset entropy
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)1 ex2 ex4 ex8 ex
16 ex
32 ex
0.5
0.6
Hatespeech-Kumar
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
16 ex
0.5
0.6
0.7
DICES
no info
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)1 ex2 ex4 ex8 ex
16 ex
32 ex
prof. (ground truth)
0.4
0.6
0.8
1
ValuePrism
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
1.8
1.85
1.9
Habermas
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
0.64
0.66
0.68
Prism
Test Loss or HV(Y|X , ·)
Test Loss or HV(Y|X , ·)
Test Loss or HV(Y|X , ·)
Test Loss or HV(Y|X , ·)
Test Loss or HV(Y|X , ·)
Test Loss or HV(Y|X , ·)
Figure 3: Test losses across rater representation settings. Dashed line: label entropy H(Y); no info: ∅; profile*:
value profiles V generated by gemma2-{9/27}b / Gemini-1.5-Pro; dem (all): D; N ex: EN, up to N examples
from Dfit
i . ValuePrism does not have demographics, but does have a ground truth value profile. Each dot
corresponds to a run with a differently seeded train/test split, with 95% CI reported. Generally, in-context examples
are more performant than value profiles, which are more performant than demographics.
OQA
HK
DIC
VP
HL
PR
0.0
0.1
0.2
0.3
0.4
Usable Rater Information (nats)
demog. (all)
prof. (gemini)
max ex
prof. (ground truth)
Figure 4: Usable rater information across datasets and
rater representations (95% CI).
small and insignificant information boost, except
for OpinionQA, where political affiliation was
highly predictive.3 Interestingly enough, however,
the gains from demographic variables for other
datasets were minimal. Additionally, value profiles
contain more usable predictive information than
demographics in all five datasets with demograph-
ics except OpinionQA (cf. Fig. 4). This suggests
that demographics alone may not be sufficient to
capture the full spectrum of human variation.
We also experiment with providing one demo-
graphic variable at a time (i.e., grouping by de-
mographic) and providing value profiles and de-
mographics together (cf. App. C/Fig. A5). As
expected, single demographics provide less infor-
mation than including all demographics. Also, de-
mographics and value profiles can contain com-
plementary information, with the best performing
representation generally being demographics and
value profiles together.
3It makes sense that demographic variables offer a boost
for OQA as political affiliation (included in demographics)
can be highly predictive for a political opinion survey.
no info
gemma2-9b
gemma2-27b
cluster 2 - gemini
cluster 4 - gemini
cluster 8 - gemini
gemini
max ex
OQA
HK
DIC
VP
0
43
76
56
69
77
74
100
0
18
33
-5
37
46
76
100
0
-14
-36
60
88
93
71
100
0
72
78
-0
20
23
94
100
Usable Information Preserved (%)
Figure 5: Info. preserved w.r.t. to using all examples.
Results shown on the four large, low-variance datasets.
Gemini profiles preserve >70% of usable information.
6
Value Profile Clustering for Grouping
Raters
To identify common modes of (dis)agreement,
avoid over-personalization (Kirk et al., 2024a) and
alleviate potential privacy concerns associated with
inferring individual value profiles, we introduce a
novel value profile-based rater clustering algorithm.
Compared to traditional clustering methods, some
advantages to our clustering method are that it: 1)
does not require any overlap in instances seen by
annotators; 2) is able to leverage semantic infor-
mation between instances; 3) enables qualitative
analyses through resulting cluster descriptions.
We assign the train raters to clusters using Al-
gorithm 2 (cf. Figure 6), where each cluster corre-
sponds to a single value profile description.4 We
4While we focus on value profiles as cluster candidates,
one could also use cluster candidates such as in-context exam-
ples or preset groups. We focus on value profiles due to their
interpretability.

--- Page 6 ---

       Find      (# clusters) value  
       proﬁles such that overall loss is 
minimized when assigning each 
rater to one of the proﬁle clusters
Calculate output probabilities from decoder 
conditioned on value proﬁles
{Yes: .9, 
No: .1}
{Yes: .6, 
No: .4}
{Yes: .2, 
No: .8}
{Yes: .7, 
No: .3}
{Yes: .8, 
No: .2}
…
{Yes: .3, 
No: .7}
{Yes: .6, 
No: .4}
{Yes: .7, 
No: .3}
{Yes: .1, 
No: .9}
…
{Yes: .7, 
No: .3}
{Yes: .9, 
No: .1}
{Yes: .2, 
No: .8}
Minimum wage?
Too many tourists?
Tax unhealthy food?
Ban animal testing?
x1
x2
x3
v1
Government 
intervention…
v2
0
HTn0=">AB7nicbVBNS8NAEJ34WetX1aOXxSJ4KolI9Vj04kq2A9oQ9hst+3SzSbsTgol9Ed48aCIV3+PN/+N2
zYHbX0w8Hhvhpl5YSKFQdf9dtbWNza3tgs7xd29/YPD0tFx08SpZrzBYhnrdkgNl0LxBgqUvJ1oTqNQ8lY4upv5rT
HXRsTqCScJ9yM6UKIvGEUrtcZB9hA0p0Gp7FbcOcgq8XJShz1oPTV7cUsjbhCJqkxHc9N0M+oRsEknxa7qeEJZS
M64B1LFY248bP5uVNybpUe6cfalkIyV39PZDQyZhKFtjOiODTL3kz8z+uk2L/xM6GSFLli0X9VBKMyex30hOaM5Q
TSyjTwt5K2JBqytAmVLQheMsvr5LmZcWrVqPV+XabR5HAU7hDC7Ag2uowT3UoQEMRvAMr/DmJM6L8+58LFrXnHz
mBP7A+fwBXWPmw=</latexit>vNV
xNX
Environmentally 
conscious…
Individual 
liberty…
p(Y|X, V )
s
TnBwsfv5lhdj4/kUKjbd9bQ8Mjo2PjE5OFqemZ2bni/EJdx6niUOxjNWZzRIEUENBUo4SxSw0Jdw6l/t9eqn16C0iKMT7CbQDNlJALBGRrkFev7XuXCReigCrNAYE53qJutdjxnX7ic9D52jo1sPIfzBw7/+KHcb7m5l6xZJftvuhf4wxMiQx05BXv3FbM0xAi5Jp3XDsBJsZUyi4hLzgphoSxq/YJTSMjVgIupn178/piEtGsTKvAhpn36fyFiodTf0TWfIsK1/
13rwv1ojxWC7mYkoSREi/rEoSCXFmPbCpC2hgKPsGsO4EuavlLeZYhxN5AUTgvP75L+mXik7m+XN41SdXcQxwRZIstklThki1TJATkiNcLJDXkgT+TZurUerRfr9aN1yBrMLJIfst7eAQ4CrmQ=</latexit>
Dﬁt
2 = {(x1, Yes), (x2, Yes), (x10, No)}
Z
ntx/a2Nb046b05tBQSaEuO1qSKkhFS/FCikKjlmxYZieTODi7s8ycFcM2f6k/pnf9N06yK7WxPTDwznueMx/nJLmSFsPwt+fu/g4dLyo8bK4ydPV5vPnp9YXRguelwrbc4SZoWSmeih
RCXOciNYmihxmlzsz/Knl8JYqbNvOMnFIGXjTI4kZ+isuPnzsG3ijfdwGdN3sLYD65HSY8jbEYorNGn5Xdgp/ICrmNbMf4GbQ6KosbYIfdUVc7On4fQWvVPhYbAF61DL7h+5WUFAg043br
bCIJwH3BW0Fi1Sx1Hc/BUNS9SkSFXzNo+DXMclMyg5EpMG1FhRc74BRuLvpMZS4UdlPO+TuGtc4Yw0satDGHu3q4oWrtJE0cmTI8t4u5mfmvXL/A0cdBKbO8QJHx6qJRoQA1zIYEQ2k
ERzVxgnEj3VuBnzPDOLpRNlwT6OKX74qTjYB2gs7xh9buXt2OZfKavCFtQkmX7JIDckR6hHsvW1v3/vsv/I/+V/8gwr1vbrmBfkr/ONrTHS/Mg=</latexit>L(r2, v1) = →log p(Yes|x1, v1) →log p(Yes|x2, v1)
→log p(No|x10, v1)
= →log 0.9 →log 0.7 →log 0.3
= 1.67
e.g., Get “ﬁt” ratings for rater 2
Calculate loss of assigning rater 2 to value proﬁle 1
Repeat for all rater / value proﬁle combinations
Repeat for all rater / value proﬁle combinations
2.11
0.92
2.45
1.67
3.04
…
4.22
0.84
6.32
3.23
…
3.81
2.43
1.34
s
eiF48V7Qe0oWy2k3bpZhN2N0IJ/QlePCji1V/kzX/jts1BWx8MPN6bYWZekAiujet+O4W19Y3NreJ2aWd3b/+gfHjU0nGqGDZLGLVCahGwSU2DTcCO4lCGgUC28H4dua3n1BpHstHM0nQj+hQ8pAzaqz0oPpev1xq+4cZJV4OalAjka/N
UbxCyNUBomqNZdz02Mn1FlOBM4LfVSjQlYzrErqWSRqj9bH7qlJxZUDCWNmShszV3xMZjbSeRIHtjKgZ6WVvJv7ndVMTXvsZl0lqULFojAVxMRk9jcZcIXMiIklClubyVsRBVlxqZTsiF4y+vktZF1atVa/eXlfpNHkcRTuAUzsGDK
6jDHTSgCQyG8Ayv8OYI58V5dz4WrQUnzmGP3A+fwAGHo2l</latexit>r1
r2
rNr
v1
v2
vNV
arg min
ˆVc→P(V ):| ˆVc|=C
!
i→[1,NR]
min
˜v→ˆVc
L(ri, ˜v)
e.g., w/ 2 clusters
2.11
0.92
2.45
1.67
3.04
…
4.22
0.84
6.32
3.23
…
3.81
2.43
1.34
v1
d
GpgwO7uZmSUhGz7BiweN8eoXefNvHGAPClbSaWqO91dQSy4Nq7eQ2Nre2d/K7hb39g8Oj4vFJU0eJYthgkYhUO6AaBZfYMNwIbMcKaRgIbAXju7nfmqDSPJPZhqjH9Kh5APOqLHS46RX6RVLbtldgKwTLyMlyFDvFb+6/YglIUrDBNW647mx8VOqDGcCZ4VuojGmbEyH2L
FU0hC1ny5OnZELq/TJIFK2pCEL9fdESkOtp2FgO0NqRnrVm4v/eZ3EDG78lMs4MSjZctEgEcREZP436XOFzIipJZQpbm8lbEQVZcamU7AheKsvr5NmpexVy9WHq1LtNosjD2dwDpfgwTXU4B7q0AGQ3iGV3hzhPivDsfy9ack82cwh84nz8Nuo2q</latexit>v2
vNV
r1
r2
rNr
C
Fu/BU3LhRx61+482+ctlo64ELh3Pu5d57/JgzqSzr2yisrK6tbxQ3S1vbO7t75v5BS0aJILRJIh6Jjo8l5SykTcUp51YUBz4nLb90e3Ub4+pkCwKH9Qkpm6AByHrM4KVljzyBlilbYyj6Br5KRjz5HY6/qZJ5ZtirWDGiZ2DkpQ46GZ345vYgkAQ0V4VjKrm3Fyk2xUIxwmpWcRNIYkxEe0K6mIQ6odNPZBxk61
UoP9SOhK1Ropv6eSHEg5STwdWeA1VAuelPxP6+bqP6Vm7IwThQNyXxRP+FIRWgaB+oxQYniE0wEUzfisgQC0yUDq2kQ7AX14mrWrFrlVq9xfl+k0eRxGO4QTOwIZLqMdNKAJB7hGV7hzXgyXox342PeWjDymUP4A+PzB8m2ldU=</latexit>ˆVc = {v1, v2}
!
i→[1,NR]
min
˜v→{v1,v2}
= .92 + 1.67 + ... + 2.43
Run each instance through the decoder conditioning on 
each value proﬁle, save the probabilities to a table
1
Calculate cross-entropy loss for assigning 
each rater to each value proﬁle
2
3
O
7uZmTUhG7AiweN8eonefNvHGAPClbSaWqO91dQSy4Nq7eQ2Nre2d/K7hb39g8Oj4vFJS0eJYthkYhUJ6AaBZfYNwI7MQKaRgIbAeT2txvP6HSPJIPZhqjH9KR5EPOqLFSo9YvltyuwBZJ15GSpCh3i9+9QYRS0KUhgmqdzY+OnVBnOBM4KvURjTNmEjrBrqaQhaj9dHDojF1YZkG
kbElDFurviZSGWk/DwHaG1Iz1qjcX/O6iRne+imXcWJQsuWiYSKIicj8azLgCpkRU0soU9zeStiYKsqMzaZgQ/BWX14nrauyVylXGtel6l0WRx7O4BwuwYMbqMI91KEJDBCe4RXenEfnxXl3PpatOSebOYU/cD5/AJl3jNI=</latexit>C
Assign new raters to cluster 
with value proﬁle that 
minimizes loss
4
Steerable 
Decoder
X →V
Figure 6: Clustering algorithm represented pictorially (also see Algorithm 2). 1) The decoder predicts label
distributions for each instance and value profile combination; 2) calculate the loss for predicting each rater’s "fit"
ratings with each value profile; 3) find C (# clusters) value profiles s.t. when each rater is assigned to a cluster,
overall loss is minimized; 4) assign new raters to cluster with smallest loss on rater’s train ratings.
train a decoder to predict train rater annotations
based on assigned cluster, and evaluate on held-out
test raters. For all datasets, we use 100 randomly
sampled value profiles as the cluster candidates.
Results can be found in Figs. 5/7 and the corre-
sponding clusters can be found in Appendix H.
Clustering is effective and is suggestive of un-
derlying modes of disagreement. Across all four
large datasets, we observe a few common trends: 1)
clustering into eight profile groups gives significant
predictive improvement over no information, and
2) predictivity improves as we increase the number
of clusters. Beyond this, we see some divergences.
For DIC and OQA, clustering is highly effective -
using just two clusters preserves the majority of the
usable rater information (60%/51% respectively),
and using eight clusters roughly matches the perfor-
mance of giving each rater their own profile. This
suggests that perhaps most raters fall into one of
very few “modes" of agreement for these datasets,
and that clustering based on value profiles is highly
effective at finding these groupings. For the other
two large datasets, HK and VP, clustering preserves
a significant amount of information (≥20%) but
is not as predictive. This implies either a failure to
find the best clusters or that the underlying variation
is inherently more difficult to categorize. Interest-
ingly, this dataset divide coheres with our intuitions:
e.g., for OpinionQA, ideology is highly explana-
tory and mostly centered around a few clusters,
whereas ValuePrism includes a diverse set of 4k
unique values which resist categorization. While
it is epistemically difficult to totally disentangle a
failure of our method to find correct groupings vs.
a true difference in dimensionality of disagreement,
we do find these results suggestive of profile cluster-
ing being able to tell us something interesting about
the true underlying reasons for rater variation.
Algorithm 2 Value Profile Clustering
Input:
• Decoder model d : X, V →P(Y)
• Candidate value profiles V
• Rater annotations for rater i: Rfit
i = {(xj, yij)}
• Target number of clusters Ncluster
• Initial clusters C = [V1, V2, . . . , VNcluster]
• Maximum iterations Miter
Nx ←|{xj s.t. ∃i, (xj, ·) ∈Rfit
i }|
▷# unique inst.
Initialize P ∈RNx×Nv×|Y| ▷Fill in output probabilities
conditioned on each value profile
for j ∈[1, . . . , Nx] do
▷For each instance
for k ∈[1, . . . , Nv] do
▷For each value profile
P[j, k] = d(xj, vk)
▷Prob. dist. over Y from d
conditioned on instance xj and profile vk
end for
end for
L(ri, vk) ←P
(xj,yij)∈Rfit
i −log P[j, k, yij] ▷Total loss
from assigning rater ri to profile vk
converged ←False; iter ←0; Clast ←C
while iter < Miter & not converged do
for c ∈[1, . . . , Ncluster] do ▷Fixing all profiles except
c, greedily find best profile to replace c
C[c] ←
▷New cluster that minimizes loss
arg min
ˆvc∈V
P
i∈[1,NR]
min
˜v∈(C/{ˆvc}∪{˜vc})L(ri, ˜v)
end for
converged ←C = Clast; Clast ←C
end while
Output: Clusters C, assignments arg min
˜v∈C
L(ri, ˜v)
Profile clusters are more predictive than the
best demographic groupings.
Next, we com-
pare with the best performing demographic clusters,
grouping people who gave the same demographic
response to a categorical demographic question
(e.g., people in the same country for DIC or same

--- Page 7 ---

55
60
Test Accuracy
OpinionQA
70
75
Hatespeech-Kumar
70
75
DICES
60
70
80
ValuePrism
25
30
Habermas
50
60
Prism
no info
ideology (5)
2 prof. clust.
4 prof. clust.
8 prof. clust.
prof. (no clust.)
max ex
0.9
1
Test Loss
no info
rel. import. (5)
2 prof. clust.
4 prof. clust.
8 prof. clust.
prof. (no clust.)
max ex
0.5
0.55
no info
locale (2)
2 prof. clust.
4 prof. clust.
8 prof. clust.
prof. (no clust.)
max ex
0.6
0.7
no info
2 prof. clust.
4 prof. clust.
8 prof. clust.
prof. (no clust.)
max ex
0.6
0.8
no info
2 prof. clust.
4 prof. clust.
8 prof. clust.
prof. (no clust.)
max ex
1.8
1.85
no info
locale (33)
2 prof. clust.
4 prof. clust.
8 prof. clust.
prof. (no clust.)
max ex
0.66
0.68
Figure 7: Performance after clustering raters into 2/4/8 profile clusters alongside the best performing categorical
demographic grouping, with the # of groups in parentheses. Value profile clustering is highly effective, outper-
forming the best demographic grouping of comparable size.
Very conservative
Conservative
Moderate
Liberal
Very liberal
Refused
0
1000
2000
3000
Count
Ideological makeup of clusters
Profile Cluster 0
Profile Cluster 1
Profile Cluster 2
Profile Cluster 3
Figure 8: Ideological makeup of the raters sorted into
each value profile cluster for OpinionQA. The clusters
recover strong ideological trends.
political ideology for OQA). We compare specifi-
cally across the three large datasets w/ demograph-
ics: for DIC, the two profile clusters is more predic-
tive than grouping based on country; for HK/OQA,
the four profile clusters outperform grouping by
religiosity/ideology respectively. In other words,
clustering by value profiles is able to outperform
the most performant demographic clusters when
using the same or fewer number of groupings.
Where predictive, demographic groupings
closely match profile clusters. Focusing in on the
two datasets where clustering was most effective,
OQA and DIC, we see if there are any demographic
trends related with clustering. As you can see from
Figure 8, there are strong demographic trends in
the OQA clusters - cluster two consists almost ex-
clusively of self-described conservative individuals,
while cluster one consists of mostly self-described
liberal individuals. In other words, despite not
having access to demographics, the value profiles
are able to largely reconstruct the most explana-
tory demographic groupings. Meanwhile, for the
DIC four-profile clusters, the clusters cut across al-
most uniformly across all demographic groupings
(Figure A4). This suggests that for DIC, the most
important dimensions of variation are not found in
the demographic groupings.
Cluster descriptions qualitatively describe
modes of disagreement.. The profile clustering
algorithm returns not only clustering assignments,
but also a single corresponding value profile for
each cluster (see App. H). For DICES, even two
clusters were quite predictive. The correspond-
ing value clusters relate to overall sensitivity to
toxicity (e.g., profile 1: "High tolerance for of-
fensive language"; "Narrow definition of toxicity"
vs. profile 2: "Strong reaction to overt negativity,
"Sensitivity to potential harm"). Meanwhile, when
going to four clusters, more nuance enters in (e.g.,
"Context and intent matter"). In other words, it
seems that 1) overall sensitivity to toxicity is an
important dimension in explaining variation, and 2)
there are clusters of people who hold more nuanced
views. For OpinionQA, descriptors that have to do
with politics are often used (e.g., "Economically
Conservative, but Populist on Trade"). For HK,
which required more clusters to effectively predict,
there are many specific phrases about what kinds of
things the rater may or may not find offensive (e.g.,
"Profanity tolerance"; "Discomfort with stereotyp-
ing"; etc.). Meanwhile, for PR the clusters center
around potentially conflicting chatbot preferences
(e.g., "Appreciates simplicity" vs. "Appreciates
nuanced and comprehensive answers"). Because
value profiles are interpretable (see §7) and can
recover demographic groupings where predictive,
we have reason to believe that these qualitative
differences map to important dimensions of dis-
agreement for a dataset.
7
Extrinsic Evaluation
In the previous sections, we have established that
value profiles are predictive of individual rater an-
notations for a wide variety of relevant tasks, based

--- Page 8 ---

on intrinsic performance metrics. We are now as-
sessing value profiles within the context of wider
real-world applications. We show that value pro-
files are interpretable – which is important for en-
abling control by the end-user; their predictions
are steerable and well-calibrated – which enables
pluralistic AI alignment; and they are reliable for
extrinsic tasks in the context of computational so-
cial science, such as simulating a rater population.
Value profiles are interpretable. We first ex-
plore interpretability – i.e., do the value descrip-
tions change the decoder outputs in a common-
sense manner? Because the encoder is prompted
and only the decoder is trained (cf. Section 2.2), we
believe that this serves as a strong regularization so
that the value profiles correlate with held-out rat-
ings only by the natural language values described.
To ensure that this is the case, we test the inter-
pretability of the autoencoder as follows: 1. For
each instance and 100 value profiles, we get the
estimated output distribution for the decoder. 2.
We select the value profiles that have the largest
Jensen-Shannon divergence. 3. We create a bi-
nary classification task: given an instance and two
value profiles, which profile corresponds to which
estimated output distribution? If the change in dis-
tribution is not correlated with common sense, we
would expect 50% accuracy, while performance
would approach 100% if an observer is always able
to match value profiles to corresponding distribu-
tions.
Data
Accuracy (%)
OQA
94.8 (±2.5)
HK
96.3 (±.6)
DIC
95.5 (±.7)
VP
91.7 (±.9)
HL
89.8 (±.9)
PR
80.0 (±.3)
Chance
50
Table 2:
Profiles are
semantically
inter-
pretable (95% CI).
As an example of the
task,
here is a short-
ened example from VP:
Is it moral,
immoral,
or
morally
dependent
on context to do this:
“Choosing not to get a vac-
cine." Profile 1: Prioriti-
zation of collective good
over
individual
needs.
Profile 2: Strong belief in
individual liberty and au-
tonomy. X probabilities: Moral: 92%, Context-
dependent: 7%, Immoral: 2%. Y probabilities:
Immoral: 94%, Context-dependent: 3%, Moral:
3%. Which profile goes with the X probabilities?
Correct answer in footnote. 5
We report accuracies for a zero-shot prompted
Gemini in Table 2. Accuracies range from 80-96%
5Profile two is the correct answer.
0
1
0
1
P(correct)
ECE: 0.001
OpinionQA
0
1
0
1
ECE: 0.008
Hatespeech-Kumar
0
1
0
1
ECE: 0.006
DICES
0
1
Model Conﬁdence
0
1
P(correct)
ECE: 0.003
ValuePrism
0
1
Model Conﬁdence
0
1
ECE: 0.007
Habermas
0
1
Model Conﬁdence
0
1
ECE: 0.048
Prism
Figure 9: Calibration plots for value profile decoders.
(Perfect calibration = dotted line). The decoders are
very well-calibrated.
0.0 0.2 0.4 0.6 0.8 1.0
Estimated P(agree)
0
0.2
0.4
0.6
0.8
1
Observed P(agree)
R² = 0.06
p = 0.068
Habermas
0.0 0.2 0.4 0.6 0.8 1.0
Estimated P(agree)
0
0.2
0.4
0.6
0.8
1
R² = 0.19
p = 5.9e-09
Hatespeech-Kumar
0.0 0.2 0.4 0.6 0.8 1.0
Estimated P(agree)
0
0.2
0.4
0.6
0.8
1
R² = 0.02
p = 0.0091
ValuePrism
Figure 10: Instance-level observed vs. estimated inter-
annotator agreement (as the probability that two raters
agree). The predicted simulated agreement correlates
with the observed agreement.
across all datasets, demonstrating that variation in
outputs from value profiles are explainable by their
plain natural language (p<.001).
Decoders are well-calibrated. Decoder calibra-
tion is important for two principal reasons. Firstly,
an appropriately calibrated decoder allows us to
trust the model confidence w.r.t. error rate. Sec-
ondly, even raters with shared values may have var-
ied outputs - a well-trained decoder would model
this distribution appropriately. Calibration plots for
the value profile decoders can be found in Figure
9. The trained decoders are quite well-calibrated,
suggesting that we can generally trust the decoder’s
output confidence.
Simulating an annotator population with
value profiles. Given a trained decoder and a set of
value profiles, one can simulate a Given a trained
decoder and a set of value profiles, one can simu-
late a population – or “jury" (Gordon et al., 2022) –
of annotators on novel instances. While one can do
many things with such a simulated population (Park
et al., 2023; Gordon et al., 2022), one experiment is
to predict which instances raters would have higher
or lower inter-annotator agreement (IAA).
In order to calculate out-of-distribution IAA, we
first eliminate the datasets where annotators have
no overlap (PR) and for which all raters annotated
the same instances (DIC, OQA). For each instance,
we then sample 100 value profiles that were not

--- Page 9 ---

fit on that instance, and calculate the estimated
probability of agreement between those annotators
(assuming each rater annotates at random from the
decoder’s output distribution). We also filter to in-
stances that were labeled by a minimum number of
annotators (See §A for details). We then compare
to the actual observed probability that two raters
agree on the instance (see Figure 10). For all three
datasets, there is a positive correlation between the
estimated and observed IAA, and this correlation
is significant (p < .001) for HK and VP. While not
much variance is explained (R2 < .2), the observed
P(agree) is a high variance estimate with few (∼5)
raters per instance. In summary, a simulated popu-
lation with value profiles provides some explana-
tory power at predicting inter-annotator agreement,
but is not yet a high precision tool.
8
Related Work
Clustering and demographics While aligning to
groups can increase agreement (Chen et al., 2024),
it also has been shown to flatten intra-group vari-
ation (Orlikowski et al., 2023; Wang et al., 2025)
lead to stereotyping (Cheng et al., 2023), or sim-
ply not be correlated with subjective NLP tasks
Orlikowski et al. (2025).
Prior work explores
embedding-based methods for clustering individ-
uals by responses (Vitsakis et al., 2024; Li et al.,
2024) and similarly finds that clusters cut across
demographic groups. Beyond predictivity, demo-
graphics can still be important to collect for eval-
uating group fairness (Aguirre et al., 2023; Kirk
et al., 2024b).
Steering to individuals Prompted large lan-
guage models (LLMs) have been used to simu-
late human judgments, e.g.: NLP task annotators
(Bavaresco et al., 2024), political survey respon-
dents (Argyle et al., 2023), fact-checking labels
(De et al., 2024), or human attitudes and behav-
ior (Park et al., 2024). Textual user profiles have
also been proposed for personalizing chats (Zhang
et al., 2018). Hu and Collier (2024) similarly use
textual demographic descriptions and find that they
provide small, but statistically significant, gains in
explaining human variation. Many works focus
merely on prompting an existing LLM, while our
work explicitly trains an LLM to better match var-
ied perspectives (as in Gordon et al. 2022; Jiang
et al. 2024). Encoding individual information from
demonstrations is also analogous to behavioral
user modeling for recommender systems (Radlin-
ski et al., 2022; Ramos et al., 2024). Poddar et al.
(2024) also use an autoencoder to model human
variation, but focus on preference data and use a
vector-valued latent space instead of natural lan-
guage.
Values and alignment Similarly to natural lan-
guage value profiles, Bai et al. (2022)’s "constitu-
tional AI" train models to follow textual principles,
although they focus on a single set of principles.
Findeis et al. (2024) propose to learn preference
principles directly from preference data (similar to
our encoder setup). Values have also been norma-
tively proposed as an alignment target (Gabriel,
2020; Klingefjord et al., 2024), and pluralistic
alignment (Sorensen et al., 2024b) seeks to align
AI systems to diverse values.
9
Conclusion
In conclusion, we proposed modeling human vari-
ation via natural language value profiles. We also
proposed a methodology to compare the usable
information in various rater representations, and
found that value profiles contain more information
than demographics. Prompted LLMs serve as effec-
tive value encoders, retaining ≥70% of the useful
rater information from demonstrations. In addition,
we introduced a profile clustering algorithm which
is able to find more explanatory clusters of raters
than grouping by the most predictive demographics.
Finally, we showed that value profiles are extrin-
sically useful for interpretability, steerability, and
for simulating diverse populations, hence offering
new ways to describe individual variation beyond
demographics.
Some promising avenues for future work include:
1) qualitative analyses extracting values from data;
2) fairness analysis of who can (or cannot) be well-
represented by value profiles; 3) study on sensi-
tivity of value profiles to choice of and number
of ratings; 4) extensions to additional models and
datasets; 5) how decoders handle conflicting value
information in a profile; 6) optimization of the en-
coder (e.g. via ELBO); and 7) human evaluations
to see how well represented people feel by value
profiles.
Acknowledgements
We would like to thank Lora Aroyo, Laura Wei-
dinger and Ahmad Beirami for helpful discussions.
We would also like to thank Charvi Rastogi and
Jared Moore for useful draft feedback.

--- Page 10 ---

10
Limitations
We have tried to test for generalization across six
tasks and datasets and more than twenty demo-
graphic distributions, However, all of the experi-
ments use the Gemma-2 (Gemma Team et al., 2024)
and Gemini (Team et al., 2024) families of mod-
els. This is due in part due to the TPU hardware
available to us and because of the expense of the
experiments (more than 650 training runs). We
have no reason to think that our results are due to
anything particular about these families of models
though, and prior work doing similar experiments
on demographics with other models has reached
similar results (Orlikowski et al., 2023; Hwang
et al., 2023). That being said, future work could
benefit from experiments on more model families.
11
Ethical Considerations
We seek to improve AI systems’ ability to model
diverse values out of a hope that the systems can
be more inclusive, better represent a range of view-
points, and better serve a wider population. Here,
we explore benefits and risks of modelling variation
with value profiles.
Profiling risks One of the potential ethical
risks of the value profile through an autoencoder
paradigm is in the name: “profile." Value profiles
are, inherently, guesses about the underlying values
that people may hold that lead them to annotate in
the way that they do. There are potential privacy
concerns here - people may not wish to have their
underlying values exposed (Tomasev et al., 2021).
It may be better if people had agency to create
their own value profiles through some voluntary
elicitation process (Park et al., 2024).
False generalization On the one hand, value
profiles are an attempt to reduce the (often false)
generalization inherent when grouping e.g. by de-
mographic groups (Dev et al., 2022), improving
on widely used current techniques. On the other
hand, generalization risks remain. For example,
there may be multiple possible underlying values
that could support a set of rater annotations. In
the absence of additional information, the value
encoder may arbitrarily assign a guess to the un-
derlying values. Also, our experiments focus on
English-language value profiles, so generalization
to other languages is unknown. Additionally, there
is always a risk of misrepresentation when using
simulated human ratings in place of actual ratings
at all (Agnew et al., 2024).
Interpretability, understandability, and user
agency However, there are also several positive
attributes to value profiles. First of all, they are
interpretable - and therefore, potentially more un-
derstandable to a user. While people interact with
many technologies today that are trying to model
their behavior and preferences, most such systems
do not break down their user representation into
a format that as as easy to understand as a textual
description. Additionally, this makes value pro-
files intervenable - people could change how they
choose to be represented (Balog et al., 2019; Lazar
et al., 2024). Relatedly, value profiles serve as a
step towards explainable AI (Arrieta et al., 2019;
Koh et al., 2020) for human variation.
Enabling value reflection Learning values from
data, while allowing users to modify the values,
is loosely related to John Rawls’ concept of re-
flective equilibrium (Rawls, 2005; Knight, 2025):
ratings are akin to judgments, and value profiles
are an attempt to draw general “principles" out of
the judgments in a bottom-up manner. Meanwhile,
a user can then edit the value profile, applying top-
down reflection on whether the values/principles
are ones that the person would endorse. In this
light, perhaps “value profiles" could help a person
to explore their own value system, both in the val-
ues that their decisions may imply and considering
which values they would reflexively endorse.
"Chosenness" of values Many works modeling
diversity focus on socio-demographics. However,
many demographics are not a result of a person’s
agency, but rather a product of unchosen life fac-
tors - for example, the country in which one is born,
or the economic opportunities available to them.
Meanwhile, while the values that one holds can
certainly be affected by unchosen factors (Nguyen,
2024), values can also be chosen for oneself. Thus,
in the spirit of luck egalitarianism (Dworkin, 2002)
it may be more justifiable to represent someone us-
ing values that they reflexively endorse, as opposed
to boxing them in to the characteristics of a group
they may not have chosen.
Importance of demographics for fairness Also,
while demographics may not be the most ideal rater
representation in many cases for the above reasons,
it can still be important to collect demographic
information for other worthwhile goals, such as
fairness/evaluating group disparities, ensuring rep-
resentation, etc.

--- Page 11 ---

References
Gavin Abercrombie, Verena Rieser, and Dirk Hovy.
2023.
Consistency is key: Disentangling label
variation in natural language processing with intra-
annotator agreement. Preprint, arXiv:2301.10684.
William Agnew, A. Stevie Bergman, Jennifer Chien,
Mark Díaz, Seliem El-Sayed, Jaylen Pittman, Shakir
Mohamed, and Kevin R. McKee. 2024. The illusion
of artificial inclusion. In Proceedings of the 2024
CHI Conference on Human Factors in Computing
Systems, CHI ’24, New York, NY, USA. Association
for Computing Machinery.
Carlos Aguirre, Kuleen Sasse, Isabel Cachola, and Mark
Dredze. 2023. Selecting shots for demographic fair-
ness in few-shot learning with large language models.
Preprint, arXiv:2311.08472.
Lisa P. Argyle, Ethan C. Busby, Nancy Fulda, Joshua R.
Gubler, Christopher Rytting, and David Wingate.
2023. Out of one, many: Using language models
to simulate human samples. Political Analysis, page
1–15.
Lora Aroyo, Alex S. Taylor, Mark Diaz, Christopher M.
Homan, Alicia Parrish, Greg Serapio-Garcia, Vinod-
kumar Prabhakaran, and Ding Wang. 2023. Dices
dataset: Diversity in conversational ai evaluation for
safety. Preprint, arXiv:2306.11247.
Lora Aroyo and Chris Welty. 2015. Truth is a lie: Crowd
truth and the seven myths of human annotation. AI
Magazine, 36(1):15–24.
Alejandro Barredo Arrieta, Natalia Díaz-Rodríguez,
Javier Del Ser, Adrien Bennetot, Siham Tabik, Al-
berto Barbado, Salvador García, Sergio Gil-López,
Daniel Molina, Richard Benjamins, Raja Chatila, and
Francisco Herrera. 2019. Explainable artificial in-
telligence (xai): Concepts, taxonomies, opportuni-
ties and challenges toward responsible ai. Preprint,
arXiv:1910.10045.
Yuntao Bai,
Saurav Kadavath,
Sandipan Kundu,
Amanda Askell, Jackson Kernion, Andy Jones, Anna
Chen, Anna Goldie, Azalia Mirhoseini, Cameron
McKinnon, Carol Chen, Catherine Olsson, Christo-
pher Olah, Danny Hernandez, Dawn Drain, Deep
Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez,
and 32 others. 2022. Constitutional ai: Harmlessness
from ai feedback. Preprint, arXiv:2212.08073.
Krisztian
Balog,
Filip
Radlinski,
and
Shushan
Arakelyan. 2019. Transparent, scrutable and explain-
able user models for personalized recommendation.
In Proceedings of the 42nd International ACM SIGIR
Conference on Research and Development in Infor-
mation Retrieval, SIGIR’19, page 265–274, New
York, NY, USA. Association for Computing Machin-
ery.
Anna Bavaresco, Raffaella Bernardi, Leonardo Berto-
lazzi, Desmond Elliott, Raquel Fernández, Albert
Gatt, Esam Ghaleb, Mario Giulianelli, Michael
Hanna, Alexander Koller, André F. T. Martins,
Philipp Mondorf, Vera Neplenbroek, Sandro Pezzelle,
Barbara Plank, David Schlangen, Alessandro Sug-
lia, Aditya K. Surikuchi, Ece Takmaz, and Alberto
Testoni. 2024. Llms instead of human judges? a
large scale empirical study across 20 nlp evaluation
tasks. CoRR, abs/2406.18403.
Quan Ze Chen, K. J. Kevin Feng, Chan Young Park,
and Amy X. Zhang. 2024. Spica: Retrieving sce-
narios for pluralistic in-context alignment. Preprint,
arXiv:2411.10912.
Myra Cheng, Esin Durmus, and Dan Jurafsky. 2023.
Marked personas: Using natural language prompts to
measure stereotypes in language models. In Proceed-
ings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 1504–1532, Toronto, Canada. Association for
Computational Linguistics.
Soham De, Michiel A Bakker, Jay Baxter, and Mar-
tin Saveski. 2024.
Supernotes: Driving consen-
sus in crowd-sourced fact-checking. arXiv preprint
arXiv:2411.06116.
Sunipa Dev, Emily Sheng, Jieyu Zhao, Aubrie Amstutz,
Jiao Sun, Yu Hou, Mattie Sanseverino, Jiin Kim, Ak-
ihiro Nishi, Nanyun Peng, and Kai-Wei Chang. 2022.
On measures of biases and harms in NLP. In Find-
ings of the Association for Computational Linguis-
tics: AACL-IJCNLP 2022, pages 246–267, Online
only. Association for Computational Linguistics.
R. M. Dworkin. 2002. Sovereign virtue: The theory
and practice of equality. Philosophical Quarterly,
52(208):377–389.
Kawin
Ethayarajh,
Yejin
Choi,
and
Swabha
Swayamdipta.
2022.
Understanding
dataset
difficulty with V-usable information.
Preprint,
arXiv:2110.08420.
Arduin Findeis, Timo Kaufmann, Eyke Hüllermeier,
Samuel Albanie, and Robert Mullins. 2024. Inverse
constitutional ai: Compressing preferences into prin-
ciples. Preprint, arXiv:2406.06560.
Iason Gabriel. 2020. Artificial intelligence, values, and
alignment. Minds and Machines, 30(3):411–437.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, Johan Ferret, Peter Liu,
Pouya Tafti, Abe Friesen, Michelle Casbon, Sabela
Ramos, Ravin Kumar, Charline Le Lan, Sammy
Jerome, and 179 others. 2024. Gemma 2: Improving
open language models at a practical size. Preprint,
arXiv:2408.00118.
Mitchell L. Gordon, Michelle S. Lam, Joon Sung Park,
Kayur Patel, Jeff Hancock, Tatsunori Hashimoto, and
Michael S. Bernstein. 2022. Jury learning: Integrat-
ing dissenting voices into machine learning models.
In CHI Conference on Human Factors in Computing
Systems, CHI ’22, page 1–19. ACM.

--- Page 12 ---

Tiancheng Hu and Nigel Collier. 2024. Quantifying
the persona effect in llm simulations.
Preprint,
arXiv:2402.10811.
EunJeong Hwang, Bodhisattwa Prasad Majumder, and
Niket Tandon. 2023. Aligning language models to
user opinions. Preprint, arXiv:2305.14929.
Ziwei Ji, Justin D. Li, and Matus Telgarsky. 2021. Early-
stopped neural networks are consistent. Preprint,
arXiv:2106.05932.
Liwei Jiang, Taylor Sorensen, Sydney Levine, and Yejin
Choi. 2024. Can language models reason about indi-
vidualistic human values and preferences? Preprint,
arXiv:2410.03868.
Hannah Rose Kirk, Bertie Vidgen, Paul Röttger, and
Scott A Hale. 2024a. The benefits, risks and bounds
of personalizing the alignment of large language
models to individuals. Nature Machine Intelligence,
pages 1–10.
Hannah Rose Kirk, Alexander Whitefield, Paul Röttger,
Andrew Bean, Katerina Margatina, Juan Ciro, Rafael
Mosquera, Max Bartolo, Adina Williams, He He,
Bertie Vidgen, and Scott A. Hale. 2024b. The prism
alignment dataset: What participatory, representa-
tive and individualised human feedback reveals about
the subjective and multicultural alignment of large
language models. Preprint, arXiv:2404.16019.
Oliver Klingefjord, Ryan Lowe, and Joe Edelman. 2024.
What are human values, and how do we align ai to
them? Preprint, arXiv:2404.10636.
Carl Knight. 2025.
Reflective Equilibrium.
In Ed-
ward N. Zalta and Uri Nodelman, editors, The Stan-
ford Encyclopedia of Philosophy, Spring 2025 edi-
tion. Metaphysics Research Lab, Stanford University.
Pang Wei Koh, Thao Nguyen, Yew Siang Tang, Stephen
Mussmann, Emma Pierson, Been Kim, and Percy
Liang. 2020. Concept bottleneck models. Preprint,
arXiv:2007.04612.
Deepak Kumar, Patrick Gage Kelley, Sunny Consolvo,
Joshua Mason, Elie Bursztein, Zakir Durumeric, Kurt
Thomas, and Michael Bailey. 2021. Designing toxic
content classification for a diversity of perspectives.
Preprint, arXiv:2106.04511.
Seth Lazar, Luke Thorburn, Tian Jin, and Luca
Belli. 2024.
The moral case for using lan-
guage model agents for recommendation. Preprint,
arXiv:2410.12123.
Junyi Li, Charith Peris, Ninareh Mehrabi, Palash Goyal,
Kai-Wei Chang, Aram Galstyan, Richard Zemel, and
Rahul Gupta. 2024. The steerability of large lan-
guage models toward data-driven personas. In Pro-
ceedings of the 2024 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume
1: Long Papers), pages 7290–7305, Mexico City,
Mexico. Association for Computational Linguistics.
Nicole Meister,
Carlos Guestrin,
and Tatsunori
Hashimoto. 2024.
Benchmarking distributional
alignment of large language models.
Preprint,
arXiv:2411.05403.
Christopher Nguyen. 2024. Value capture. Journal of
Ethics and Social Philosophy, 27(3).
Matthias Orlikowski, Jiaxin Pei, Paul Röttger, Philipp
Cimiano, David Jurgens, and Dirk Hovy. 2025. Be-
yond demographics: Fine-tuning large language mod-
els to predict individuals’ subjective text perceptions.
Preprint, arXiv:2502.20897.
Matthias Orlikowski, Paul Röttger, Philipp Cimiano,
and Dirk Hovy. 2023. The ecological fallacy in anno-
tation: Modeling human label variation goes beyond
sociodemographics. In Proceedings of the 61st An-
nual Meeting of the Association for Computational
Linguistics (Volume 2: Short Papers), pages 1017–
1029, Toronto, Canada. Association for Computa-
tional Linguistics.
Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai,
Meredith Ringel Morris, Percy Liang, and Michael S.
Bernstein. 2023.
Generative agents:
Interac-
tive simulacra of human behavior.
Preprint,
arXiv:2304.03442.
Joon Sung Park, Carolyn Q. Zou, Aaron Shaw, Ben-
jamin Mako Hill, Carrie Cai, Meredith Ringel Morris,
Robb Willer, Percy Liang, and Michael S. Bernstein.
2024. Generative agent simulations of 1,000 people.
Preprint, arXiv:2411.10109.
Barbara Plank. 2022. The “problem” of human label
variation: On ground truth in data, modeling and
evaluation. In Proceedings of the 2022 Conference
on Empirical Methods in Natural Language Process-
ing, pages 10671–10682, Abu Dhabi, United Arab
Emirates. Association for Computational Linguistics.
Sriyash Poddar, Yanming Wan, Hamish Ivison, Ab-
hishek Gupta, and Natasha Jaques. 2024. Person-
alizing reinforcement learning from human feedback
with variational preference learning. In Advances in
Neural Information Processing Systems, volume 37,
pages 52516–52544. Curran Associates, Inc.
Vinodkumar Prabhakaran, Christopher Homan, Lora
Aroyo, Aida Mostafazadeh Davani, Alicia Parrish,
Alex Taylor, Mark Diaz, Ding Wang, and Gregory
Serapio-García. 2024. GRASP: A disagreement anal-
ysis framework to assess group associations in per-
spectives. In Proceedings of the 2024 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), pages 3473–3492,
Mexico City, Mexico. Association for Computational
Linguistics.
Filip Radlinski, Krisztian Balog, Fernando Diaz, Lucas
Dixon, and Ben Wedin. 2022. On natural language
user profiles for transparent and scrutable recommen-
dation. In Proceedings of the 45th International ACM
SIGIR Conference on Research and Development in

--- Page 13 ---

Information Retrieval, SIGIR ’22, page 2863–2874,
New York, NY, USA. Association for Computing
Machinery.
Jerome Ramos, Hossein A. Rahmani, Xi Wang, Xiao Fu,
and Aldo Lipani. 2024. Transparent and scrutable
recommendations using natural language user pro-
files. In Proceedings of the 62nd Annual Meeting of
the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 13971–13984, Bangkok,
Thailand. Association for Computational Linguistics.
John Rawls. 2005. Political Liberalism, expanded edi-
tion edition. Columbia University Press, New York.
Shibani Santurkar, Esin Durmus, Faisal Ladhak,
Cinoo Lee, Percy Liang, and Tatsunori Hashimoto.
2023. Whose opinions do language models reflect?
Preprint, arXiv:2303.17548.
Anand Siththaranjan, Cassidy Laidlaw, and Dylan
Hadfield-Menell. 2024. Distributional preference
learning: Understanding and accounting for hidden
context in rlhf. Preprint, arXiv:2312.08358.
Taylor Sorensen, Liwei Jiang, Jena D. Hwang, Syd-
ney Levine, Valentina Pyatkin, Peter West, Nouha
Dziri, Ximing Lu, Kavel Rao, Chandra Bhagavat-
ula, Maarten Sap, John Tasioulas, and Yejin Choi.
2024a. Value kaleidoscope: Engaging ai with plural-
istic human values, rights, and duties. Proceedings
of the AAAI Conference on Artificial Intelligence,
38(18):19937–19947.
Taylor
Sorensen,
Jared
Moore,
Jillian
Fisher,
Mitchell Gordon, Niloofar Mireshghallah, Christo-
pher Michael Rytting, Andre Ye, Liwei Jiang,
Ximing Lu, Nouha Dziri, Tim Althoff, and Yejin
Choi. 2024b. A roadmap to pluralistic alignment.
Preprint, arXiv:2402.05070.
Gemini Team, Petko Georgiev, Ving Ian Lei, Ryan
Burnell, Libin Bai, Anmol Gulati, Garrett Tanzer,
Damien Vincent, Zhufeng Pan, Shibo Wang, Soroosh
Mariooryad, Yifan Ding, Xinyang Geng, Fred Al-
cober, Roy Frostig, Mark Omernick, Lexi Walker,
Cosmin Paduraru, Christina Sorokin, and 1118 oth-
ers. 2024. Gemini 1.5: Unlocking multimodal un-
derstanding across millions of tokens of context.
Preprint, arXiv:2403.05530.
Michael Henry Tessler, Michiel A. Bakker, Daniel Jar-
rett, Hannah Sheahan, Martin J. Chadwick, Raphael
Koster, Georgina Evans, Lucy Campbell-Gillingham,
Tantum Collins, David C. Parkes, Matthew Botvinick,
and Christopher Summerfield. 2024. Ai can help hu-
mans find common ground in democratic deliberation.
Science, 386(6719):eadq2852.
Nenad Tomasev, Kevin R. McKee, Jackie Kay, and
Shakir Mohamed. 2021. Fairness for unobserved
characteristics: Insights from technological impacts
on queer communities. In Proceedings of the 2021
AAAI/ACM Conference on AI, Ethics, and Society,
AIES ’21, page 254–265, New York, NY, USA. As-
sociation for Computing Machinery.
Nikolas Vitsakis, Amit Parekh, and Ioannis Konstas.
2024. Voices in a crowd: Searching for clusters of
unique perspectives. Preprint, arXiv:2407.14259.
Angelina Wang, Jamie Morgenstern, and John P. Dick-
erson. 2025. Large language models that replace
human participants can harmfully misportray and
flatten identity groups. Nature Machine Intelligence.
Mitchell Wortsman, Gabriel Ilharco, Samir Yitzhak
Gadre, Rebecca Roelofs, Raphael Gontijo-Lopes,
Ari S. Morcos, Hongseok Namkoong, Ali Farhadi,
Yair Carmon, Simon Kornblith, and Ludwig Schmidt.
2022. Model soups: averaging weights of multiple
fine-tuned models improves accuracy without increas-
ing inference time. Preprint, arXiv:2203.05482.
Yilun Xu, Shengjia Zhao, Jiaming Song, Russell Stew-
art, and Stefano Ermon. 2020. A theory of usable in-
formation under computational constraints. Preprint,
arXiv:2002.10689.
Michael JQ Zhang, Zhilin Wang, Jena D. Hwang,
Yi Dong, Olivier Delalleau, Yejin Choi, Eunsol Choi,
Xiang Ren, and Valentina Pyatkin. 2024. Diverging
preferences: When do annotators disagree and do
models know? Preprint, arXiv:2410.14632.
Saizheng Zhang, Emily Dinan, Jack Urbanek, Arthur
Szlam, Douwe Kiela, and Jason Weston. 2018. Per-
sonalizing dialogue agents: I have a dog, do you
have pets too? In Proceedings of the 56th Annual
Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), pages 2204–2213,
Melbourne, Australia. Association for Computational
Linguistics.

--- Page 14 ---

Appendix - Table of contents
• Appendix A: Reproducibility details
• Appendix B: More on approaches to mod-
elling variation.
• Appendix C: Additional experiments.
• Appendix D: Discussion of potential applica-
tions and extensions
• Appendix E: The prompts used for the en-
coders and decoders.
• Appendix F: Preprocessing and demographic
information for all datasets.
• Appendix G: Full results for all experiments
across all rater representations.
• Appendix H: The profile clusters found and
used in the profile cluster experiments.
• Appendix I: Ten random value profiles
for each dataset and model (gemma2-9b,
gemma2-27b, gemini).
A
Reproducibility Details
Here, we include additional experimental details to
aid reproducibility.
Dataset Preprocessing We carried out the fol-
lowing preprocessing steps for the datasets - DIC:
used the larger subset (990); HL: selected raters
with at least nine responses; HK: randomly selected
5k raters and binarized annotations; OQA: ran-
domly selected a wave for experiments (Wave 27);
PR: select annotations from first conversation turn
and compared the chosen response to the next high-
est rated response; VP: Treat each value, right, or
duty as a unique annotator. Finally, for all datasets
we filtered to annotators that had at least four re-
sponses.
Decoder
hyperparameters:
model:
gemma2-9b-pt (Gemma Team et al., 2024),
batch size: 4, learning rate: 1e-7, gradient clipping:
50.
fp32 unembedding layer: Gemma 2 (Gemma
Team et al., 2024) natively uses bf16. However, we
found that this caused heavy quantization among
high-probability logits (e.g., the valid responses).
As such, we cast the embedding/unembedding pa-
rameters to fp32 before training, which allowed
for higher precision distributions, important for cal-
ibration and expressivity.
Fit/eval partition details: For each rater ri,
we draw |Dfit
i | ∼U({2, . . . , |Di| −2}) and set
|Deval
i
| = |Di| −|Dfit
i | to ensure that we have
variable-sized fit/eval splits with at least two in-
stances each. Value profile encoders use all Dfit
i
instances and the decoders with in-context informa-
tion En use the first min(n, |Dfit
i |) examples from
|Dfit
i |. This means that value profiles are fit with a
variable number of ratings.
Simulating an annotator population instance
selection: We selected the minimum number of
instances per dataset as roughly the median number
of annotations per instance: 3 for HL, 5 for HK,
and 5 for VP. This was selected to try to ensure 1)
that we had as many instances as possible and 2)
that we had enough raters to have a high-precision
estimate of actual rater agreement.
B
More on Approaches to Modelling
Variation
In Figure A1, we flesh out more of the comparisons
between various modelling approaches character-
ized in §1.
C
Additional Experiments and Results
C.1
Predictive Power of Demographic Groups
In addition to presenting the decoder with all rater
demographic variables at once (i.e., intersectional
demographics), we also train a decoder for each
demographic dimension individually. This allows
us 1) to see the extent to which grouping individu-
als based on demographic dimensions is predictive,
and 2) which demographic dimensions contain the
most usable information for any given dataset. We
also train a decoder using all demographic infor-
mation plus the value profiles. See Figure A5 for
results. Some main findings include:
Grouping by demographics does not add sig-
nificant predictive power. Grouping individuals
based on individual demographic dimensions did
not significantly improve predictive power, except
for OQA, where political ideology/party and reli-
gious affiliation/attendance were most informative.
Value profiles and demographics can be com-
plementary. Combining value profiles and de-
mographics resulted in performance as good as
or better than either one individually. This sug-
gests that the decoder can leverage both types of
information when relevant, e.g. ignore irrelevant
information when it is not useful (cf. demographics

--- Page 15 ---

Standard modeling
Distributional 
population modeling
Group modeling 
(single answer)
Group modeling 
(distributional)
Individual modeling
Description
Assumes single correct answer, 
any variance is noise ❌
Model the distribution of 
responses ✅
Model a group’s answer 
(assuming each group 
has one answer)
Model a group’s 
distribution of answers ✅
Model an individual’s 
answers ✅
Target
Single response 
(interpersonal variation is noise 
❌)
Distribution of responses 
(variation is signal ✅)
Single group response 
(inter-group variation is 
signal ✅, 
intra-group variation is  
noise ❌);
 
Group’s distribution of 
responses ✅
Single response 
(interpersonal variation is 
signal ✅)
Overlap 
requirement
No instance overlap required 
✅
Many annotators label 
same instance ❌
Many annotators from 
each group label same 
instance ❌
Many annotators from 
each group label same 
instance ❌
No instance overlap 
required ✅
Stereotyping 
risk
High ❌
Lower ✅
High (no allowed in-
group variation) ❌
Lower ✅
Lower ✅
Know who 
disagrees or 
why?
No ❌
No ❌
Between groups, yes ✅ 
Within groups, no ❌
Between groups, yes ✅ 
Within groups, no ❌
Yes ✅
Flexibility of 
population 
modeling
No ❌
 Low, only on population 
distribution trained on ✅
Medium, on arbitrary 
group mixtures ✅ ✅
Medium, on arbitrary 
group mixtures ✅ ✅
High, for arbitrary 
population via 
aggregation ✅ ✅ ✅
Figure A1: Comparisons of various modelling approaches and their tradeoffs with respect to modelling variation
No info (;)
Demographics (D) Value Proﬁle (V )
Examples (En)
0.55
0.60
0.65
Test loss, or H(Y |X, ·)
Fictional Dataset Results
H(Y)
IV(V →Y|X)
HV(Y|X, V )
HV(Y|X, En)
IV(En →Y|X)
IV(D →Y|X)
HV(Y|X, D)
HV(Y|X, →)
w
sFhWoLFHShlC2CpaORaIX1EaR47qtVeci20GqQt6AhVdhYQAhVlY23gb3QgUIfsnSp/+cI5/zexGjQhrGh7awuLS8spZy65vbG5t53Z2GyKMOSZ1HLKQtzwkCKMBqUsqGWlFnCDfY6TpDS/G9eYN4YKGwZU
cRcTxUT+gPYqRVJabO6q6HR/JAUYsaSFOV+nt3NupcduLm/oZtEul06goZfKVqloKbAt27DOoKkbE+XBTDU397phj2SAxQ0K0TSOSToK4pJiRNuJBYkQHqI+aSsMkE+Ek0zuSeGhcrqwF3L1Agkn7ve
JBPlCjHxPdY53FL9rY/OvWjuWvbKT0CKJQnw9KNezKAM4Tgc2KWcYMlGChDmVO0K8QBxhKWKMKtC+LoU/g+Nom7aun1p5SvnszgyYB8cgAIwSmogCqogTrA4A48gCfwrN1rj9qL9jptXdBmM3vgh7S3T1J
2nYU=</latexit>HV(Y|X)
.05 nats
.08 nats
.11 nats
Figure A2: An illustrative plot on fictional data for
measuring V-info.
in DIC/HK) and combine complementary informa-
tion when useful (cf. OQA/HL).
C.2
How does the method generalize to
free-form text?
For all experiments in the paper, rater annotations
were categorical/ordinal responses to a small, fi-
nite number of options. This decision was made
largely because of a lack of adequate datasets with
more complex annotations. However, the question
remains - how does the method generalize to free-
form text outputs?
One (and only one) of our datasets, Habermas
(Tessler et al., 2024), has free-form rater outputs:
the justification that people gave for why they gave
the likert response that they did. These descrip-
tions are usually a few sentences long, and contain
interesting value information. To get a data point
of how our method generalizes to free-form text,
we also train a decoder designed to output textual
justifications on this dataset (results in Figure A6).
Similar to the categorical results, including more
examples does indeed help test perplexity over the
no information setting. However, demographics
and profiles are not able to help significantly. We
have two theories as to why this is the case. Firstly,
text contains not only value information, but also
stylistic and syntactic information - for example,
some raters begin every justification with the same
phrase, and others write short vs. long justifica-
tions. Thus, in-context examples communicate
both value-relevant information and syntactic infor-
mation, and it is difficult to tell which is causing the
decrease in perplexity. Secondly, Habermas was
our smallest dataset, making conclusions difficult
to decisively draw for even the discrete likert-scale
setting. Thus, it is possible that this negative result
is in part due to the decoder being underfit, and that
value profiles would be able to provide predictive
information with additional training. As these re-
sults are only on one (small) dataset, we believe
that testing generality of the method to free-form
text is a promising avenue for future work.
C.3
Zero-shot decoder performance
For all experiments in the main paper, we train a
decoder (using SFT) on a set of train raters and
evaluate them on held out test raters. While this is
necessary for estimating rater information, we are
also curious to know: how well can a value profile

--- Page 16 ---

no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
16 ex
32 ex
40
50
60
Test Accuracy (%)
OpinionQA
majority class acc
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
16 ex
32 ex
60
70
Hatespeech-Kumar
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
16 ex
70
75
DICES
no info
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
16 ex
32 ex
prof. (ground truth)
50
60
70
80
Test Accuracy (%)
ValuePrism
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
20
22
25
28
30
Habermas
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
50
55
60
65
Prism
Test Accuracy
Figure A3: Held-out accuracies across rater representations. Accuracies are reported for the same training runs as
Figure 3, with very similar takeaways/results.
Man
Nonbin
Self-d
Woman
0
10
20
30
40
50
60
70
80
rater_gender
Profile Cluster 0
Profile Cluster 1
Profile Cluster 2
Profile Cluster 3
India
United
0
10
20
30
40
50
60
70
80
rater_locale
Americ
Asian
Black 
East o
Indian
LatinX
Latino
Middle
Mixed
Native
Other
Prefer
White
nan
0
5
10
15
20
25
30
35
40
rater_race_raw
Gen x+
Gen z
Millen
0
20
40
60
80
rater_age
Colleg
High s
0
20
40
60
80
100
120
140
rater_education
Figure A4: For DICES, the four profile clusters cut across demographic groups along all dimensions.
decoder perform without dataset-specific training?
Specifically, we evaluate on the following settings:
• Pretrained/base model: Prompted base model
gemma2-9b-pt.
• Instruction-tuned
model:
Prompted
instruction-tuned model gemma2-9b-it.
• Souped model (Wortsman et al., 2022): Av-
erage the model weights from the trained de-
coders on all datasets except for the evaluation
dataset.
• Trained model: For comparison, we also show
results for the trained model.
Performance and calibration results are reported in
Figure A7.
Some results include:
• As expected, the trained models both offer the
best performance and calibration.
• Instruction-tuned models generally get higher
accuracy than base models (5/6 datasets), but
base models generally get lower loss (4/6
datasets) due to better calibration.
• The souped models (finetuned from pretrained
model) get the same or lower loss as the base
models on all datasets, showing some ability
to generalize to novel datasets.
All in all, training seems important for learning
calibration, and there is some demonstrated ability
to generalize from one dataset to another via soup-
ing. Additional work exploring how to maintain
calibration and performance on out-of-distribution
dataset settings is an interesting avenue for future
work.
D
Applications and Extensions
Given a set of value profiles and well-calibrated,
trained decoders, there are many possible exciting

--- Page 17 ---

55
60
Test Accuracy
OpinionQA
70
72.5
75
Hatespeech-Kumar
70
75
DICES
25
27.5
30
Habermas
50
55
60
65
Prism
no info
RELIGATTEND
RELIG
POLPARTY
POLIDEOLOGY
demog. (all)
prof. (gemini)
demog. (all) + prof. (gemini)
32 ex
0.85
0.9
0.95
1
Test Loss
no info
is parent
uses media forums
uses media video
religion important
demog. (all)
prof. (gemini)
demog. (all) + prof. (gemini)
32 ex
0.5
0.55
0.6
no info
rater age
rater gender
rater race raw
rater locale
demog. (all)
prof. (gemini)
demog. (all) + prof. (gemini)
16 ex
0.6
0.7
no info
income
region
gender id
party id
demog. (all)
prof. (gemini)
demog. (all) + prof. (gemini)
8 ex
1.77
1.8
1.82
1.85
no info
study locale
order lm usecases
system string
order stated prefs
demog. (all)
prof. (gemini)
demog. (all) + prof. (gemini)
8 ex
0.66
0.68
Figure A5: Performance using one demographic at a time, all demographics, value profiles, and all demograph-
ics with the value profile. No information and the max examples settings are also reported as baselines. The four
most predictive demographics (as measured by test loss) are reported for each dataset, results for the remaining
demographics can be found in Appendix G.
no info
demog. (all)
prof. (gemma 9b)
prof. (gemma 27b)
prof. (gemini)
1 ex
2 ex
4 ex
8 ex
1.85
1.9
1.95
Test Loss or HV(Y|X , ·)
Habermas Text
Figure A6: Results when testing our method on predict-
ing textual rater justifications.
applications. We list a few here.
D.1
Disentangling (Value)-Epistemic and
Aleatoric Uncertainty
In the context of modeling human variation, un-
certainty can arise from two distinct sources: epis-
temic uncertainty (reducible through rater informa-
tion) and aleatoric uncertainty (irreducible random
variation). With value profiles, we can further look
at value-epistemic uncertainty, or uncertainty that
can be reduced by better understanding a rater’s
values.
Specifically, given a set of instances, raters, and
their annotations, we can measure the proportion
of total uncertainty that can be attributed to value
differences versus inherent randomness:
• Total Uncertainty: The entropy of ratings
given just the instance, HV (Y |X)
• Value-Epistemic Uncertainty: The infor-
mation gained by knowing value profiles,
IV (V (R)
→
Y |X)
=
HV (Y |X) −
HV (Y |X, V (R))
• Aleatoric Uncertainty: The remaining uncer-
tainty after conditioning on both instance and
value profiles, HV (Y |X, V (R))
The ratio IV (V (R) →Y |X)/HV (Y |X) rep-
resents the fraction of uncertainty that is value-
epistemic (reducible by knowing values), while
HV (Y |X, V (R))/HV (Y |X) represents the frac-
tion that is aleatoric (irreducible even with value
knowledge).
Instance-level uncertainty can similarly be mea-
sured by looking at HV (Y |x), IV (V (R) →Y |x),
and HV (Y |x, V (R)). Similar definitions also exist
for any other rater representation.
We plot instance-level value-epistemic vs.
aleatoric uncertainty for all instances in each
dataset in Figure A8.
Such analyses and information may be useful for
determining which instances have higher or lower
disagreement and whether that disagreement is due
to value-relevant factors or other factors.

--- Page 18 ---

0.0
0.2
0.4
0.6
0.8
1.0
trained
Acc: 76%
NLL: 0.59
DICES
0.0
0.2
0.4
0.6
0.8
1.0
pretrained
Acc: 41%
NLL: 1.01
0.0
0.2
0.4
0.6
0.8
1.0
instruction-tuned
Acc: 72%
NLL: 0.81
0.0 0.2 0.4 0.6 0.8 1.0
0.0
0.2
0.4
0.6
0.8
1.0
soup (all minus dataset)
Acc: 72%
NLL: 0.79
Acc: 26%
NLL: 1.82
Habermas
Acc: 20%
NLL: 1.91
Acc: 17%
NLL: 3.67
0.0 0.2 0.4 0.6 0.8 1.0
Acc: 21%
NLL: 1.91
Acc: 75%
NLL: 0.51
Hatespeech-Kumar
Acc: 53%
NLL: 0.70
Acc: 71%
NLL: 0.81
0.0 0.2 0.4 0.6 0.8 1.0
Acc: 59%
NLL: 0.69
Acc: 60%
NLL: 0.87
OpinionQA W27
Acc: 49%
NLL: 1.09
Acc: 50%
NLL: 1.97
0.0 0.2 0.4 0.6 0.8 1.0
Acc: 50%
NLL: 1.09
Acc: 77%
NLL: 0.57
ValuePrism
Acc: 60%
NLL: 0.93
Acc: 69%
NLL: 0.90
0.0 0.2 0.4 0.6 0.8 1.0
Acc: 65%
NLL: 0.83
Acc: 60%
NLL: 0.66
Prism
Acc: 57%
NLL: 0.68
Acc: 59%
NLL: 0.92
0.0 0.2 0.4 0.6 0.8 1.0
Acc: 58%
NLL: 0.67
Figure A7: Results and calibration plot for zero-shot results for pretrained/base models, instruction-tuned models,
and souped models on all but the dataset to evaluate. Results are compared to the decoder trained on the dataset.
D.2
Identifying instance-specific value
information
Each instance may have particular values which are
more or less relevant for the instance as well. Using
value decoders, one can estimate the relevance of
a value for an instance with IV (v →Y |x). This
could be useful in cases such as if one wants to
know what values to survey raters for for a particu-
lar instance.
D.3
Rater difficulty
Some raters may more easily be modeled by value
profiles (or profile clusters) than others. For ex-
ample, given a set of candidate value profiles (or,
value profile clusters), one could measure the test
loss for a rater given the optimal assignment. The
lower the test loss, the more easily modeled they
are by the value profile, the higher the test loss, the
more they may not be easily explained by a value
profile. In this way, one could find raters that either
a) are not easily modeled by a value profile in the
current system or b) may be providing low-quality
(or random) judgements.
D.4
Other applications
Other potential applications include:
• Designing an active learning system to select
instances for a rater to annotate that are most
likely to provide value-relevant information;
• Exploring which groups are best or worst rep-
resented with value profiles;
• Building a system to help someone explore
their own values (see §11);
or more.
E
Prompts
See Figure A9 for the encoder prompt and Figure
A10 for the decoder prompt used for all experi-
ments.
F
Data
F.1
Dataset Preprocessing Details
We carried out the following preprocessing steps
for the datasets - DIC: used the larger subset (990);
HL: selected raters with at least nine responses;
HK: randomly selected 5k raters and binarized an-
notations; OQA: randomly selected a wave for ex-
periments (Wave 27); PR: select annotations from
first conversation turn and compared the chosen
response to the next highest rated response; VP:
Treat each value, right, or duty as a unique annota-
tor. Finally, for all datasets we filtered to annotators
that had at least four responses.

--- Page 19 ---

0.25
0.50
0.75
0.00
0.05
0.10
0.15
Information Gain (Profile)
DICES
 Not
 Toxic
1.6
1.8
0.025
0.050
0.075
0.100
Habermas
1
6
7
0.2
0.4
0.6
0.05
0.10
0.15
Hatespeech-Kumar
 Toxic
 Not Toxic
0.5
1.0
1.5
Irreducible Entropy
0.0
0.1
0.2
0.3
Information Gain (Profile)
OpinionQA W27
 C
 A
 B
 D
 E
0.50
0.75
1.00
Irreducible Entropy
0.1
0.2
0.3
ValuePrism
 Moral
 It
 Imm
0.625
0.650
0.675
Irreducible Entropy
0.00
0.01
0.02
0.03
Prism
 B
 A
Figure A8: Value-Epistemic Uncertainty (a.k.a., Information Gain from Value Profile) vs. the Irreducible Entropy
(or Aleatoric Uncertainty) for each instance in each dataset, colored by label.
F.2
All Dataset Demographic Variables
Refer to Table 3 to see all demographic variables
contained in each dataset.
G
Detailed Results
The full results for each dataset can be found in:
1. OpinionQA: Table 4
2. Hatespeech-Kumar: Table 5
3. DICES: Table 6
4. ValuePrism: Table 7
5. Habermas-Likert: Table 8
6. Prism: Table 9

--- Page 20 ---

Dataset
Demographics
OpinionQA (W27)
CREGION, SEX, EDUCATION, CITIZEN, MARITAL, INCOME, RACE, RELIG, RELIGAT-
TEND, POLPARTY, POLIDEOLOGY
Habermas-Likert
party_id, religion, age, education, ethnicity, gender_id, immigration_status, income, region
DICES
rater_gender, rater_locale, rater_race_raw, rater_age, rater_education
Hatespeech-Kumar
gender, gender_other, race, identify_as_transgender, lgbtq_status, education, age_range,
political_affilation, is_parent, religion_important, technology_impact, uses_media_social,
uses_media_news, uses_media_video, uses_media_forums, personally_seen_toxic_content, per-
sonally_been_target, toxic_comments_problem
ValuePrism
None, but has "ground truth" value profiles of the original value / right / duty.
Prism
lm_familiarity,
lm_indirect_use,
lm_direct_use,
lm_frequency_use,
lm_usecases,
self_description, system_string, religion, stated_prefs, order_lm_usecases, order_stated_prefs,
age, gender, employment_status, education, marital_status, english_proficiency, study_locale,
location, ethnicity
Table 3: Dataset demographic variables
You will be given a response or set of 
responses from a rater. Given this, output a 
bulleted list of values or beliefs that the 
rater may have. It is okay to be speculative as 
long as you are exhaustive. They should be 
general beliefs that could apply to other 
situations as well, instead of hyper-specific 
to the particulars of this question. 
 
{rater fit ratings} 
Rater values and beliefs: 
-
  
Input variable: 
- {rater fit ratings}: textual representation 
of the annotator’s fit ratings
PMXS3z0YkHEolv1W/8CLc=">AB7XicbVDLSgNBEOz1GeMr6tHLY
BA8hV2R6DHoxWMC5gHJEmYns8mYeSwzs0JY8g9ePCji1f/x5t84Sfa
giQUNRVU3V1Rwpmxv/tra1vbG5tF3aKu3v7B4elo+OWUakmtEkUV
7oTYUM5k7RpmeW0k2iKRcRpOxrfzfz2E9WGKflgJwkNBR5KFjOCrZN
ajX4vGbF+qexX/DnQKglyUoYc9X7pqzdQJBVUWsKxMd3AT2yYW0Z4
XRa7KWGJpiM8ZB2HZVYUBNm82un6NwpAxQr7UpaNFd/T2RYGDMRkes
U2I7MsjcT/O6qY1vwozJLVUksWiOXIKjR7HQ2YpsTyiSOYaOZu
RWSENSbWBVR0IQTL6+S1mUlqFaqjaty7TaPowCncAYXEMA1OAe6t
AEAo/wDK/w5invxXv3Phata14+cwJ/4H3+AG7Qjw4=</latexit>Qω
En(ri) →Dﬁt
i
vi →Qω(En(ri))
Output:
Encoder Prompt
Figure A9: Encoder prompt
H
Profile Clusters
H.1
DICES
H.1.1
2 clusters (DICES)
Cluster Profile 1: High tolerance for offensive lan-
guage and behavior; Focus on intent rather than
impact; Narrow definition of toxicity; Prioritization
of conversation flow over emotional safety; Belief
in personal responsibility for emotional reactions;
Discomfort with addressing conflict or negativity;
Lack of awareness of subtle forms of toxicity; Poten-
tial bias towards certain topics or demographics;
General optimism or positivity
Cluster Profile 2: Strong reaction to overt nega-
tivity or hate speech; Sensitivity to potential harm,
even if unintentional; Prioritizes intention over im-
pact; Tolerance for bluntness and disagreement;
Focus on explicit language rather than subtle cues;
Possible political bias; Inconsistency in application
of criteria
H.1.2
4 clusters (DICES)
Cluster Profile 1: Strong reaction to overt nega-
tivity or hate speech; Sensitivity to potential harm,
even if unintentional; Prioritizes intention over im-
pact; Tolerance for bluntness and disagreement;
Focus on explicit language rather than subtle cues;
Possible political bias; Inconsistency in application
of criteria
Cluster Profile 2: High tolerance for offensive
language and controversial topics; Focus on intent
over impact; Emphasis on personal responsibil-
ity and resilience; Broad definition of acceptable
discourse; Potential desensitization to online inter-
actions; Possible lack of understanding of subtle
forms of toxicity; Potential bias towards certain
viewpoints; Belief in the importance of context
Cluster Profile 3: Direct insults and aggressive
language are toxic; Simple greetings and neutral
topics are not toxic; Humor and playful banter are
not necessarily toxic; The presence of controver-
sial opinions does not automatically equal toxicity;
Context and intent matter, but are difficult to fully
assess; Statements suggesting or promoting illegal
or harmful activities are toxic; The rater may have
a relatively high tolerance for differing viewpoints
Cluster Profile 4: High tolerance for offensive
language and behavior; Focus on intent rather than
impact; Narrow definition of toxicity; Prioritization
of conversation flow over emotional safety; Belief
in personal responsibility for emotional reactions;
Discomfort with addressing conflict or negativity;
Lack of awareness of subtle forms of toxicity; Poten-
tial bias towards certain topics or demographics;
General optimism or positivity

--- Page 21 ---

Answer the questions from the perspective 
of someone with the following 
demographics and value profile. 
 
Value profile: {value profile} 
Demographics: {demographics}
Input: {input1} 
Output: {rating1} 
 
… 
 
Input: {input n} 
Output: {rating n}
  
Input variables: 
- {dataset task description}: Description of the 
task that the raters were given 
- {instance}: The instance to label 
- {value profile} (optional): Value profile for the  
rater 
- {demographics} (optional): Textual description 
of the rater’s demographics 
- {rater fit ratings} (optional): textual representation of 
the annotator’s fit ratings 
{dataset task description} 
 
{rater description} 
 
{in-context rater examples} 
 
Input: {instance} 
Output:
if {value profile} and not {demographics}:
Answer the questions from the perspective 
of someone with the value profile. 
 
Value profile: {value profile}
if {demographics} and not {value profile}:
Answer the questions from the perspective 
of someone with the following 
demographics. 
 
Demographics: {demographics}
if {demographics} and {value profile}:
if not {demographics} and not {value profile}:
{empty string}
if {rater fit ratings}:
if not {rater fit ratings}:
{empty string}
{rater description}
{in-context rater examples}
Decoder Prompt Pω
K
OXRmKCF7JrDHokevGIiSwksCHd0oVKt920XROy4T948aAxXv0/3vw3FtiDgi+Z5OW9mczMCxPOtHdb6ewtr6xuVXcLu3s7u0flA+PfC1TRWiLSC5VJ8SaciZoyzDaSdRFMchp+1wfDvz209UaSbFg5k
NIjxULCIEWys5PtV1Wfn/XLFrblzoFXi5aQCOZr98ldvIEkaU2EIx1p3PTcxQYaVYTamXapgMsZD2rVU4JjqIJtfO0VnVhmgSCpbwqC5+nsiw7HWkzi0nTE2I73szcT/vG5qousgYyJDRVksShKOTI
SzV5HA6YoMXxiCSaK2VsRGWGFibEBlWwI3vLq8S/qHn1Wv3+stK4yeMowgmcQhU8uIG3ETWkDgEZ7hFd4c6bw4787HorXg5DPH8AfO5w/Kb46i</latexit>V (ri)
D(ri)
E
O1xjXGLevTSGIR4CTMi0WNwAY8RzAKZOPR0ekyT7p6hu0YMQ37Bi7/ixYMiXr1582/sLAc1Pih4vFdFVb0wEdyA6345c/MLi0vLuZX86tr6xmZha7th4lRTVqexiHUrJIYJrlgdOAj
WSjQjMhSsGfbPRn7zjmnDY3UNg4R1JLlVPOKUgJWCQukiUCUd8APsGy6xLwn0KBHZ+TDgNz6we9AyizgMg0LRLbtj4FniTUkRTVELCp9+N6apZAqoIMa0PTeBTkY0cCrYMO+nhiWE9
skta1uqiGSmk40/GuJ9q3RxFGtbCvBY/TmREWnMQIa2c3Sx+euNxP+8dgrRSfjKkmBKTpZFKUCQ4xH8eAu14yCGFhCqOb2Vkx7RBMKNsS8DcH7+/IsaRyWvUq5cnVUrJ5O48ihXb
SHSshDx6iKLlEN1RFD+gJvaBX59F5dt6c90nrnDOd2UG/4Hx8A6hynZs=</latexit>
En(ri) →Dﬁt
i
e
64="3rE2qTCEDezK9k3dF5/nYOTIY5w=">
AB6nicbVDLTgJBEOzF+IL9ehlIjHxRH
aNQY9ELx4xyiMBQmaHXhiZnd3MzBrJhk/w
4kFjvPpF3vwbB9iDgpV0UqnqTneXHwuje
t+O7mV1bX1jfxmYWt7Z3evuH/Q0FGiGNZJ
CLV8qlGwSXWDTcCW7FCGvoCm/7oeuo3H1F
pHsl7M46xG9KB5AFn1Fjp7qn30CuW3LI7A
1kmXkZKkKHWK351+hFLQpSGCap123Nj02
pMpwJnBQ6icaYshEdYNtSUPU3XR26oScWK
VPgkjZkobM1N8TKQ21Hoe+7QypGepFbyr+
57UTE1x2Uy7jxKBk80VBIoiJyPRv0ucKmR
FjSyhT3N5K2JAqyoxNp2BD8BZfXiaNs7JX
KVduz0vVqyOPBzBMZyCBxdQhRuoQR0YDO
AZXuHNEc6L8+58zFtzTjZzCH/gfP4AZaN5
A=</latexit>xj
ˆyij
Output:
V (ri)
D(ri)
x1
yi1
yn1
xn
Figure A10: Decoder prompt
H.1.3
8 clusters (DICES)
Cluster Profile 1: Strong reaction to overt nega-
tivity or hate speech; Sensitivity to potential harm,
even if unintentional; Prioritizes intention over im-
pact; Tolerance for bluntness and disagreement;
Focus on explicit language rather than subtle cues;
Possible political bias; Inconsistency in application
of criteria
Cluster Profile 2: Direct insults and aggressive
language are toxic; Simple greetings and neutral
topics are not toxic; Humor and playful banter are
not necessarily toxic; The presence of controver-
sial opinions does not automatically equal toxicity;
Context and intent matter, but are difficult to fully
assess; Statements suggesting or promoting illegal
or harmful activities are toxic; The rater may have
a relatively high tolerance for differing viewpoints
Cluster Profile 3: Strong reaction to discussions
of self-harm and suicide; Sensitivity to discussions
about race and sexual orientation; Discomfort with
overtly sexual conversations or innuendo; Low tol-
erance for aggressive or rude language; A broad
definition of "toxic"; Uncertainty around certain
topics; A belief that context matters; Prioritizes
safety and well-being
Cluster Profile 4: High tolerance for offensive
language and behavior; Focus on intent rather than
impact; Narrow definition of toxicity; Prioritization
of conversation flow over emotional safety; Belief
in personal responsibility for emotional reactions;
Discomfort with addressing conflict or negativity;
Lack of awareness of subtle forms of toxicity; Poten-
tial bias towards certain topics or demographics;
General optimism or positivity
Cluster Profile 5: Emphasis on intent over out-
come; High tolerance for disagreement and differ-
ing opinions; Forgiveness for misunderstandings
and apologies; Political neutrality or apathy; Dis-
comfort with discussions about illegal activities;
Leniency towards casual conversation and humor;
Inconsistency in applying standards; Focus on last
turn in the conversation
Cluster Profile 6: High tolerance for controver-
sial topics and strong opinions; Emphasis on inten-

--- Page 22 ---

Name
Test Accuracy
Test Loss
Usable Info (nats)
Info Preserved
no info
52.0 (±0.14)
0.987 (±0.002)
0.000
(0%)
dem CITIZEN
51.9 (±0.08)
0.987 (±0.002)
0.000
-
dem CREGION
51.9 (±0.12)
0.987 (±0.002)
0.000
-
dem EDUCATION
52.1 (±0.10)
0.985 (±0.002)
0.002
-
dem INCOME
52.0 (±0.13)
0.985 (±0.002)
0.002
-
dem MARITAL
52.4 (±0.07)
0.983 (±0.002)
0.004
-
dem POLIDEOLOGY
59.2 (±0.07)
0.896 (±0.002)
0.091
-
dem POLPARTY
57.1 (±0.17)
0.918 (±0.002)
0.069
-
dem RACE
52.5 (±0.15)
0.983 (±0.002)
0.004
-
dem RELIG
53.7 (±0.13)
0.965 (±0.003)
0.022
-
dem RELIGATTEND
53.5 (±0.08)
0.971 (±0.002)
0.016
-
dem SEX
52.1 (±0.11)
0.985 (±0.001)
0.002
-
dem identity columns
53.3 (±0.32)
0.972 (±0.004)
0.015
-
dem value columns
60.1 (±0.41)
0.881 (±0.008)
0.106
-
dem (all)
61.0 (±0.07)
0.859 (±0.002)
0.128
-
profile cluster-2
59.3 (±0.15)
0.899 (±0.002)
0.088
56%
profile cluster-4
60.1 (±0.22)
0.878 (±0.003)
0.109
69%
profile cluster-8
60.8 (±0.18)
0.866 (±0.003)
0.121
77%
profile 9b
57.5 (±1.10)
0.918 (±0.016)
0.069
43%
profile 27b
61.1 (±0.14)
0.866 (±0.002)
0.120
76%
profile gni
60.3 (±0.13)
0.870 (±0.004)
0.117
74%
dem+profile gni
62.4 (±0.11)
0.829 (±0.002)
0.158
-
1 ex
53.9 (±0.46)
0.964 (±0.005)
0.023
-
2 ex
56.1 (±0.08)
0.937 (±0.002)
0.050
-
4 ex
58.0 (±0.34)
0.906 (±0.005)
0.081
-
8 ex
60.0 (±0.11)
0.870 (±0.003)
0.117
-
16 ex
61.4 (±0.32)
0.843 (±0.005)
0.143
-
32 ex
62.3 (±0.12)
0.829 (±0.003)
0.158
(100%)
majority class acc./dataset entropy
39.7 (±0.00)
1.290 (±0.000)
-
-
Table 4: OpinionQA Performance Metrics (Model: gemma2-9b-pt) Other datasets: Appendix: G
tion over impact; Belief in freedom of expression;
Acceptance of dark humor and sarcasm; Forgive-
ness for immaturity or ignorance; Discomfort with
discussions directly involving their personal ad-
vice on difficult topics; May not be detecting subtle
forms of toxicity; Possibly prioritizing engagement
and entertainment over safety and inclusivity
Cluster Profile 7: Discomfort with sexual top-
ics and exploitation; Sensitivity to personal attacks
and insults; Low tolerance for manipulative or
misleading behavior; Dislike of aggressive or con-
frontational language; High tolerance for sarcasm
and playful banter; Belief that repetitive or non-
sensical conversations are not necessarily toxic;
Uncertainty about the line between persistent ques-
tioning and harassment; Possible leniency towards
conversations that are simply awkward or uncom-
fortable; Emphasis on intent and context; Potential
bias toward focusing on the last statement
Cluster Profile 8: High tolerance for offensive
language and controversial topics; Focus on intent
over impact; Emphasis on personal responsibil-
ity and resilience; Broad definition of acceptable
discourse; Potential desensitization to online inter-
actions; Possible lack of understanding of subtle
forms of toxicity; Potential bias towards certain
viewpoints; Belief in the importance of context
H.2
Habermas-Likert
H.2.1
2 clusters (Habermas-Likert)
Cluster Profile 1: Values religious freedom and
parental rights; Prioritizes family autonomy over
state control; May be religious themselves; Prag-
matic or uncertain about online medicine; Weigh-
ing competing values; Lack of knowledge; Belief in
a mixed approach; Values personal responsibility;
Prioritizes affordability and access to healthcare;
Trusts market forces to some extent
Cluster Profile 2: Strong disapproval of Theresa
May; Public health consciousness; Environmen-
tal concern; Belief in direct democracy; Concern
about overpopulation; Openness to government in-
tervention; Possible leaning towards left-leaning
or liberal politics; Pragmatism and nuanced views;
UK-centric perspective
H.2.2
4 clusters (Habermas-Likert)
Cluster Profile 1: Pro-worker; Value of leisure
and rest; Concern for elderly well-being; Poten-
tial distrust of government or employers; Belief in
social safety nets; Focus on quality of life over eco-
nomic growth; Generational fairness; Compassion

--- Page 23 ---

Name
Test Accuracy
Test Loss
Usable Info (nats)
Info Preserved
no info
70.5 (±0.46)
0.569 (±0.005)
0.000
(0%)
dem (all)
70.7 (±0.40)
0.565 (±0.004)
0.003
-
dem personally been target
70.6 (±0.36)
0.568 (±0.004)
0.000
-
dem personally seen toxic content
70.6 (±0.40)
0.567 (±0.004)
0.001
-
dem age range
70.6 (±0.42)
0.568 (±0.004)
0.001
-
dem uses media social
70.6 (±0.38)
0.568 (±0.004)
0.001
-
dem uses media news
70.7 (±0.35)
0.568 (±0.004)
0.001
-
dem uses media forums
70.6 (±0.65)
0.566 (±0.008)
0.002
-
dem toxic comments problem
70.7 (±0.38)
0.567 (±0.004)
0.001
-
dem technology impact
70.6 (±0.38)
0.569 (±0.004)
0.000
-
dem religion important
71.4 (±0.39)
0.558 (±0.004)
0.010
-
dem race
70.7 (±0.37)
0.568 (±0.004)
0.001
-
dem political affilation
70.7 (±0.41)
0.568 (±0.004)
0.001
-
dem lgbtq status
70.6 (±0.36)
0.569 (±0.004)
0.000
-
dem is parent
70.7 (±0.36)
0.567 (±0.004)
0.002
-
dem identity columns
70.6 (±0.32)
0.568 (±0.004)
0.000
-
dem identify as transgender
70.5 (±0.35)
0.568 (±0.004)
0.000
-
dem gender other
70.6 (±0.40)
0.568 (±0.004)
0.000
-
dem gender
70.6 (±0.34)
0.568 (±0.005)
0.000
-
dem education
70.5 (±0.38)
0.568 (±0.004)
0.001
-
dem uses media video
70.7 (±0.37)
0.566 (±0.004)
0.003
-
dem value columns
71.0 (±0.35)
0.563 (±0.004)
0.005
-
profile cluster-2
70.1 (±0.52)
0.572 (±0.006)
-0.004
-5%
profile cluster-4
72.6 (±0.23)
0.539 (±0.003)
0.029
37%
profile cluster-8
73.1 (±0.26)
0.532 (±0.003)
0.036
46%
profile 9b
71.3 (±0.35)
0.554 (±0.003)
0.014
18%
profile 27b
72.3 (±0.18)
0.543 (±0.002)
0.026
33%
profile gni
74.8 (±0.21)
0.509 (±0.003)
0.060
76%
dem+profile gni
75.0 (±0.15)
0.509 (±0.003)
0.059
-
1 ex
71.6 (±0.31)
0.553 (±0.003)
0.016
-
2 ex
72.5 (±0.21)
0.541 (±0.002)
0.028
-
4 ex
74.1 (±0.22)
0.521 (±0.002)
0.047
-
8 ex
75.5 (±0.21)
0.500 (±0.001)
0.069
-
16 ex
75.5 (±0.40)
0.500 (±0.006)
0.069
-
32 ex
76.3 (±0.33)
0.489 (±0.003)
0.079
(100%)
majority class acc./dataset entropy
55.4 (±0.00)
0.687 (±0.000)
-
-
Table 5: Hatespeech-Kumar Performance Metrics (Model: gemma2-9b-pt) Other datasets: Appendix: G
and empathy for those less fortunate; May hold
specific political or ideological views
Cluster Profile 2: Strong disapproval of Theresa
May; Public health consciousness; Environmen-
tal concern; Belief in direct democracy; Concern
about overpopulation; Openness to government in-
tervention; Possible leaning towards left-leaning
or liberal politics; Pragmatism and nuanced views;
UK-centric perspective
Cluster Profile 3: Altruism and global citizen-
ship; Environmental concern; Collectivism and
public health prioritization; Social welfare and
belief in social safety nets; Potential for utilitarian-
ism; Nuance and pragmatism; Possible support for
animal welfare, but with caveats; Acceptance of
minor moral flexibility; It is important to remember
that these are just inferences based on a limited set
of responses. The rater’s true beliefs and values
may be more complex and nuanced than what can
be determined from this data alone.
Cluster Profile 4: Values religious freedom and
parental rights; Prioritizes family autonomy over
state control; May be religious themselves; Prag-
matic or uncertain about online medicine; Weigh-
ing competing values; Lack of knowledge; Belief in
a mixed approach; Values personal responsibility;
Prioritizes affordability and access to healthcare;
Trusts market forces to some extent
H.2.3
8 clusters (Habermas-Likert)
Cluster Profile 1: Slightly prefers free market prin-
ciples; Concerned about affordability and access;
Cautious about government overreach; Open to
social responsibility and regulation where appro-
priate; Values personal autonomy; Pragmatic and
moderate; Indecisive or uninformed on some top-
ics; Potentially influenced by personal experience;
Open to persuasion
Cluster Profile 2: Pro-worker; Value of leisure
and rest; Concern for elderly well-being; Poten-
tial distrust of government or employers; Belief in
social safety nets; Focus on quality of life over eco-

--- Page 24 ---

Name
Test Accuracy
Test Loss
Usable Info (nats)
Info Preserved
no info
71.8 (±0.92)
0.668 (±0.020)
0.000
(0%)
dem rater age
71.5 (±1.09)
0.671 (±0.020)
-0.002
-
dem rater education
71.1 (±1.21)
0.673 (±0.020)
-0.004
-
dem rater gender
71.7 (±1.13)
0.669 (±0.020)
-0.001
-
dem rater locale
71.6 (±1.20)
0.666 (±0.020)
0.002
-
dem rater race raw
71.6 (±1.10)
0.668 (±0.020)
0.000
-
dem (all)
71.6 (±1.27)
0.667 (±0.021)
0.002
-
profile cluster-2
75.6 (±0.51)
0.605 (±0.012)
0.064
60%
profile cluster-4
76.4 (±0.67)
0.576 (±0.015)
0.093
88%
profile cluster-8
76.9 (±0.69)
0.570 (±0.013)
0.098
93%
profile 9b
71.5 (±0.90)
0.683 (±0.023)
-0.015
-14%
profile 27b
69.9 (±1.04)
0.706 (±0.018)
-0.038
-36%
profile gni
75.7 (±0.50)
0.594 (±0.014)
0.074
71%
dem+profile gni
75.4 (±0.62)
0.598 (±0.015)
0.070
-
1 ex
72.9 (±0.77)
0.644 (±0.016)
0.025
-
2 ex
74.1 (±0.76)
0.625 (±0.014)
0.044
-
4 ex
75.2 (±0.58)
0.602 (±0.012)
0.066
-
8 ex
76.3 (±0.51)
0.580 (±0.013)
0.089
-
16 ex
77.0 (±0.66)
0.563 (±0.014)
0.105
(100%)
majority class acc./dataset entropy
70.4 (±0.00)
0.742 (±0.000)
-
-
Table 6: DICES Performance Metrics (Model: gemma2-9b-pt) Other datasets: Appendix: G
Name
Test Accuracy
Test Loss
Usable Info (nats)
Info Preserved
no info
59.2 (±0.37)
0.852 (±0.005)
0.000
(0%)
profile cluster-2
59.4 (±0.49)
0.853 (±0.005)
-0.001
-0%
profile cluster-4
65.4 (±0.82)
0.792 (±0.013)
0.060
20%
profile cluster-8
65.8 (±1.37)
0.780 (±0.017)
0.071
23%
profile 9b
74.0 (±0.24)
0.632 (±0.006)
0.220
72%
profile 27b
74.6 (±0.39)
0.615 (±0.008)
0.237
78%
profile gni
77.3 (±0.22)
0.566 (±0.006)
0.286
94%
1 ex
68.1 (±0.29)
0.738 (±0.006)
0.114
-
2 ex
70.6 (±0.51)
0.695 (±0.010)
0.157
-
4 ex
73.4 (±0.67)
0.640 (±0.015)
0.212
-
8 ex
75.8 (±0.35)
0.591 (±0.007)
0.261
-
16 ex
76.8 (±0.38)
0.570 (±0.008)
0.282
-
32 ex
77.9 (±0.35)
0.547 (±0.007)
0.305
(100%)
ground truth prof
80.1 (±0.17)
0.493 (±0.006)
0.358
-
ground truth prof+profile gni
80.3 (±0.27)
0.491 (±0.005)
0.361
-
majority class acc./dataset entropy
50.4 (±0.00)
1.004 (±0.000)
-
-
Table 7: ValuePrism Performance Metrics (Model: gemma2-9b-pt) Other datasets: Appendix: G
nomic growth; Generational fairness; Compassion
and empathy for those less fortunate; May hold
specific political or ideological views
Cluster Profile 3: Altruism and global citizen-
ship; Environmental concern; Collectivism and
public health prioritization; Social welfare and
belief in social safety nets; Potential for utilitarian-
ism; Nuance and pragmatism; Possible support for
animal welfare, but with caveats; Acceptance of
minor moral flexibility; It is important to remember
that these are just inferences based on a limited set
of responses. The rater’s true beliefs and values
may be more complex and nuanced than what can
be determined from this data alone.
Cluster Profile 4: Supports government inter-
vention in the economy; Progressive social views;
Prioritizes social welfare; Believes in public infras-
tructure investment; Values education; Potentially
skeptical of inherited power/privilege; May believe
in reducing inequality; Possibly environmentally
conscious; Optimistic about government’s ability
to improve society; Could be influenced by current
events and political discourse in the UK
Cluster Profile 5: Strong disapproval of Theresa
May; Public health consciousness; Environmen-
tal concern; Belief in direct democracy; Concern
about overpopulation; Openness to government in-
tervention; Possible leaning towards left-leaning
or liberal politics; Pragmatism and nuanced views;
UK-centric perspective
Cluster Profile 6: Pro-worker/Pro-labor; En-
vironmentalist/Concerned about climate change;
Socially liberal/Progressive; Emphasis on well-
being/Quality of life; Government intervention; Po-
tentially left-leaning politically; Belief in interna-
tional cooperation; It’s important to remember that

--- Page 25 ---

Name
Test Accuracy
Test Loss
Usable Info (nats)
Info Preserved
no info
24.8 (±0.43)
1.838 (±0.003)
0.000
(0%)
dem demographics.age
23.9 (±1.21)
1.846 (±0.015)
-0.007
-
dem demographics.education
24.1 (±0.69)
1.847 (±0.004)
-0.008
-
dem demographics.ethnicity
24.1 (±0.45)
1.834 (±0.005)
0.004
-
dem demographics.gender id
25.2 (±0.19)
1.830 (±0.005)
0.008
-
dem demographics.immigration status
23.5 (±1.13)
1.838 (±0.009)
0.000
-
dem demographics.income
25.5 (±0.37)
1.834 (±0.007)
0.005
-
dem demographics.party id
24.6 (±0.43)
1.829 (±0.006)
0.009
-
dem demographics.region
24.9 (±0.50)
1.831 (±0.005)
0.008
-
dem demographics.religion
24.7 (±0.67)
1.843 (±0.005)
-0.004
-
dem identity columns
23.9 (±1.27)
1.852 (±0.012)
-0.013
-
dem value columns
23.6 (±1.32)
1.835 (±0.020)
0.003
-
dem (all)
25.3 (±0.49)
1.822 (±0.006)
0.016
-
profile cluster-2
24.3 (±0.54)
1.840 (±0.004)
-0.002
-4%
profile cluster-4
24.6 (±0.56)
1.846 (±0.010)
-0.008
-19%
profile cluster-8
24.6 (±0.45)
1.844 (±0.005)
-0.006
-14%
profile 9b
26.7 (±0.80)
1.819 (±0.004)
0.019
46%
profile 27b
26.2 (±0.52)
1.815 (±0.003)
0.023
56%
profile gni
25.8 (±0.50)
1.817 (±0.006)
0.022
52%
dem+profile gni
27.2 (±0.80)
1.785 (±0.007)
0.053
-
1 ex
25.4 (±0.72)
1.814 (±0.004)
0.025
-
2 ex
27.0 (±0.68)
1.802 (±0.005)
0.036
-
4 ex
27.6 (±0.98)
1.799 (±0.004)
0.039
-
8 ex
27.9 (±0.68)
1.797 (±0.004)
0.042
(100%)
majority class acc./dataset entropy
21.2 (±0.00)
1.906 (±0.000)
-
-
Table 8: Habermas Performance Metrics (Model: gemma2-9b-pt) Other datasets: Appendix: G
these are inferences based on limited data. The
rater’s actual beliefs may be more nuanced and
complex.
Cluster Profile 7: Values religious freedom and
parental rights; Prioritizes family autonomy over
state control; May be religious themselves; Prag-
matic or uncertain about online medicine; Weigh-
ing competing values; Lack of knowledge; Belief in
a mixed approach; Values personal responsibility;
Prioritizes affordability and access to healthcare;
Trusts market forces to some extent
Cluster Profile 8: Strong belief in personal re-
sponsibility and limited government intervention;
Concern for social safety and welfare, but with a
focus on individual choice; Environmental aware-
ness; Generally law-abiding and moralistic, but
with potential for nuance; Potential belief in eco-
nomic fairness and reducing inequality; Value of
personal freedom and autonomy; Pragmatic ap-
proach to complex issues
H.3
Hatespeech-Kumar
H.3.1
2 clusters (Hatespeech-Kumar)
Cluster Profile 1: Profanity Tolerance; Empha-
sis on Intent over Specific Words; Sensitivity to
Identity-Based Attacks; Broad Definition of Toxic-
ity, Including Harmful Stereotypes and Misinforma-
tion; Potential Political Bias; Discomfort with Sex-
ualized Language; Subjectivity and Context Matter;
Acceptance of Strong Opinions; Inconsistency or
evolving understanding of toxicity; Possible cul-
tural or generational influences
Cluster Profile 2: Strong tolerance for offensive
language and controversial topics; Focus on direct
threats and personal attacks as "toxic"; Insensi-
tivity to subtle forms of prejudice; Acceptance of
"locker room talk" or crude humor; Prioritization
of intent over impact; Inconsistency in applying
criteria; It’s important to emphasize that these are
speculative interpretations based on a limited sam-
ple of data. Further analysis and direct questioning
of the rater would be necessary to confirm these
beliefs and values.
H.3.2
4 clusters (Hatespeech-Kumar)
Cluster Profile 1: Strong aversion to negativity
and insults; Sensitivity to discussions of potentially
harmful topics; A broad interpretation of toxic-
ity; Concern with stereotyping and generalizations;
Sensitivity to political and religious discussions;
Emphasis on context and intent; Potential over-
reliance on emotional response
Cluster Profile 2: Strong aversion to profan-
ity and vulgar language; Sensitivity to negativity
and insults; Concern about violence and harmful
actions; Discomfort with stereotypes and gener-
alizations; Sensitivity to discussions of sensitive
topics; Broad interpretation of "toxicity"; Possible
discomfort with intense emotional expressions; In-

--- Page 26 ---

Name
Test Accuracy
Test Loss
Usable Info (nats)
Info Preserved
no info
56.6 (±1.96)
0.684 (±0.004)
0.000
(0%)
dem age
58.9 (±0.92)
0.681 (±0.006)
0.004
-
dem study locale
60.1 (±0.61)
0.674 (±0.005)
0.010
-
dem stated prefs
58.4 (±0.93)
0.680 (±0.007)
0.004
-
dem self description
58.9 (±1.60)
0.678 (±0.004)
0.006
-
dem religion
55.8 (±1.41)
0.686 (±0.002)
-0.001
-
dem order stated prefs
60.4 (±0.60)
0.672 (±0.004)
0.013
-
dem order lm usecases
59.8 (±1.26)
0.674 (±0.007)
0.011
-
dem marital status
59.3 (±1.01)
0.676 (±0.006)
0.009
-
dem location
58.0 (±1.87)
0.676 (±0.007)
0.009
-
dem lm usecases
59.3 (±1.27)
0.675 (±0.006)
0.009
-
dem lm indirect use
55.4 (±1.62)
0.833 (±0.145)
-0.149
-
dem lm frequency use
59.3 (±0.88)
0.680 (±0.006)
0.005
-
dem lm familiarity
55.5 (±2.45)
0.685 (±0.003)
-0.001
-
dem lm direct use
56.5 (±1.60)
0.683 (±0.004)
0.002
-
dem identity columns
60.8 (±0.58)
0.671 (±0.004)
0.013
-
dem gender
57.1 (±1.88)
0.682 (±0.006)
0.002
-
dem ethnicity
57.8 (±1.40)
0.684 (±0.004)
0.000
-
dem english proficiency
57.5 (±1.37)
0.684 (±0.004)
0.000
-
dem employment status
59.6 (±0.75)
0.677 (±0.005)
0.008
-
dem education
59.1 (±0.91)
0.679 (±0.005)
0.005
-
dem system string
59.6 (±0.67)
0.673 (±0.005)
0.011
-
dem value columns
58.6 (±1.83)
0.676 (±0.005)
0.008
-
dem (all)
58.6 (±1.63)
0.679 (±0.006)
0.005
-
profile cluster-2
60.2 (±0.58)
0.673 (±0.005)
0.012
131%
profile cluster-4
58.2 (±2.13)
0.674 (±0.006)
0.010
114%
profile cluster-8
56.2 (±2.09)
0.684 (±0.005)
0.000
5%
profile 9b
60.8 (±1.07)
0.672 (±0.006)
0.013
145%
profile 27b
61.3 (±0.96)
0.667 (±0.008)
0.017
191%
profile gni
60.4 (±1.64)
0.665 (±0.008)
0.020
220%
dem+profile gni
60.8 (±0.55)
0.668 (±0.007)
0.016
-
1 ex
57.6 (±2.30)
0.677 (±0.005)
0.007
-
2 ex
56.0 (±1.91)
0.681 (±0.006)
0.003
-
4 ex
58.0 (±2.26)
0.676 (±0.006)
0.009
-
8 ex
58.0 (±2.42)
0.676 (±0.006)
0.009
(100%)
majority class acc./dataset entropy
50.3 (±0.00)
0.693 (±0.000)
-
-
Table 9: Prism Performance Metrics (Model: gemma2-9b-pt) Other datasets: Appendix: G
consistent application of criteria; Potential cultural
or generational differences
Cluster Profile 3: Strong tolerance for offensive
language and controversial topics; Focus on direct
threats and personal attacks as "toxic"; Insensi-
tivity to subtle forms of prejudice; Acceptance of
"locker room talk" or crude humor; Prioritization
of intent over impact; Inconsistency in applying
criteria; It’s important to emphasize that these are
speculative interpretations based on a limited sam-
ple of data. Further analysis and direct questioning
of the rater would be necessary to confirm these
beliefs and values.
Cluster Profile 4: Profanity Tolerance; Empha-
sis on Intent over Specific Words; Sensitivity to
Identity-Based Attacks; Broad Definition of Toxic-
ity, Including Harmful Stereotypes and Misinforma-
tion; Potential Political Bias; Discomfort with Sex-
ualized Language; Subjectivity and Context Matter;
Acceptance of Strong Opinions; Inconsistency or
evolving understanding of toxicity; Possible cul-
tural or generational influences
H.3.3
8 clusters (Hatespeech-Kumar)
Cluster Profile 1: Strong tolerance for offensive
language and controversial topics; Focus on direct
threats and personal attacks as "toxic"; Insensi-
tivity to subtle forms of prejudice; Acceptance of
"locker room talk" or crude humor; Prioritization
of intent over impact; Inconsistency in applying
criteria; It’s important to emphasize that these are
speculative interpretations based on a limited sam-
ple of data. Further analysis and direct questioning
of the rater would be necessary to confirm these
beliefs and values.
Cluster Profile 2: Profanity Tolerance; Empha-
sis on Intent over Specific Words; Sensitivity to
Identity-Based Attacks; Broad Definition of Toxic-
ity, Including Harmful Stereotypes and Misinforma-
tion; Potential Political Bias; Discomfort with Sex-
ualized Language; Subjectivity and Context Matter;
Acceptance of Strong Opinions; Inconsistency or

--- Page 27 ---

evolving understanding of toxicity; Possible cul-
tural or generational influences
Cluster Profile 3: High tolerance for strong lan-
guage and criticism in certain contexts; Emphasis
on intent and harm over mere presence of nega-
tivity; Acceptance of strong emotional expression,
even negative ones, within reasonable bounds; Po-
litical neutrality or tolerance for diverse political
viewpoints; Context matters; Distinction between
subjective criticism and objective harm; General
permissiveness towards fan-related content and
positive expressions; Focus on individual harm
rather than potential group offense
Cluster Profile 4: High tolerance for profanity
and sexual content; Sensitivity to personal attacks
and insults; A more lenient view of potentially of-
fensive language when used in humor or casual
conversation; Discomfort with stereotyping and
generalizations about groups; Tolerance of strong
opinions and emotional expressions; A possible
bias towards accepting casual, internet-specific
language and trends; Inconsistency in applying
standards; Potential lack of understanding of some
slang or cultural references
Cluster Profile 5: Strong reactions or negativ-
ity alone don’t necessarily constitute toxicity. The
rater marked comments expressing strong dislike
("gross," "wouldn’t touch... with a bargepole") or
frustration ("Who TF cares") as not toxic, suggest-
ing they don’t equate negativity with toxicity. How-
ever, when coupled with aggressive or potentially
harmful sentiments, as in the comment about elec-
tric cars being "political bullshit" that is being
"forced on us", the rating changes to toxic. This im-
plies nuance in their judgment.; Direct or implied
threats and mentions of harm are considered toxic.
The comments referencing "raped," and potentially
violent or inappropriate behavior ("After I nun ate...
he wanna cut up in there") were marked toxic. This
indicates a value for safety and a belief that lan-
guage suggesting harm is unacceptable.; Humor
and informal language are generally acceptable.
The use of slang ("LIT," "TF"), internet abbrevia-
tions, and self-deprecating humor did not trigger a
toxic rating. This suggests a tolerance for casual
online communication styles.; Discussion and dis-
agreement are not inherently toxic. The comment
about "Ariel is black" presents a counter-argument,
yet it’s deemed non-toxic. This implies a belief
that expressing diverse opinions, even on poten-
tially controversial topics, is permissible.; Context
matters. Hashtags and references that could be
considered out of place weren’t considered toxic in
isolation. This suggests the rater is considering the
overall message and intent, rather than focusing
solely on individual words or phrases.; Personal
preferences or strong opinions, if not directed at
individuals or groups, are acceptable. The com-
ment about "gorgeous gay dudes sword fighting"
expresses a specific preference, but is not consid-
ered toxic. This indicates a respect for individual
tastes, as long as they aren’t used to denigrate
others.; The rater may have a higher threshold
for toxicity. Several comments that could be per-
ceived as rude or offensive by some were marked
non-toxic. This suggests the rater focuses on more
severe forms of toxicity, prioritizing clear instances
of harm or aggression.
Cluster Profile 6: High tolerance for offensive
language; Focus on explicit threats or calls for
harm as markers of toxicity; Desensitization to
online negativity; Belief that subjective opinions
are not inherently toxic; Lack of consideration for
the impact of microaggressions; Prioritization of
intent over impact; Possible personal bias
Cluster Profile 7: Strong aversion to profan-
ity and vulgar language; Sensitivity to negativity
and insults; Concern about violence and harmful
actions; Discomfort with stereotypes and gener-
alizations; Sensitivity to discussions of sensitive
topics; Broad interpretation of "toxicity"; Possible
discomfort with intense emotional expressions; In-
consistent application of criteria; Potential cultural
or generational differences
Cluster Profile 8: Strong aversion to negativity
and insults; Sensitivity to discussions of potentially
harmful topics; A broad interpretation of toxic-
ity; Concern with stereotyping and generalizations;
Sensitivity to political and religious discussions;
Emphasis on context and intent; Potential over-
reliance on emotional response
H.4
OpinionQA - Wave 27
H.4.1
2 clusters (OpinionQA - Wave 27)
Cluster Profile 1: Nationalist/Patriotic; Conser-
vative; Law and Order; Pro-Military; Economi-
cally Conservative, but Populist on Trade; Socially
Conservative, but with Libertarian Leanings; Dis-
trustful of Government and Elites; Pragmatic; Pes-
simistic
Cluster Profile 2: Believes in American excep-
tionalism, but acknowledges other great nations;
Values democracy and allies; Supports a strong so-

--- Page 28 ---

cial safety net but believes in personal responsibil-
ity; Pragmatic and values compromise; Optimistic
about social progress; Values traditional family
structures; Concerned about voter fraud, but sup-
ports voting rights; Supports separation of church
and state, but sees value in religious belief; Positive
about technology and globalization; Believes in a
larger government role; Socially moderate; Eco-
nomically progressive; Generally content but sees
areas for improvement; Skeptical of politicians and
the political system; Believes in expert knowledge;
Believes in a strong military and good diplomacy;
Values immigration but with controls; Believes in
personal freedoms but recognizes the need for some
government intervention; Doesn’t feel disrespected
but acknowledges white privilege
H.4.2
4 clusters (OpinionQA - Wave 27)
Cluster Profile 1: Believes in American excep-
tionalism, but acknowledges other great nations;
Values democracy and allies; Supports a strong so-
cial safety net but believes in personal responsibil-
ity; Pragmatic and values compromise; Optimistic
about social progress; Values traditional family
structures; Concerned about voter fraud, but sup-
ports voting rights; Supports separation of church
and state, but sees value in religious belief; Positive
about technology and globalization; Believes in a
larger government role; Socially moderate; Eco-
nomically progressive; Generally content but sees
areas for improvement; Skeptical of politicians and
the political system; Believes in expert knowledge;
Believes in a strong military and good diplomacy;
Values immigration but with controls; Believes in
personal freedoms but recognizes the need for some
government intervention; Doesn’t feel disrespected
but acknowledges white privilege
Cluster Profile 2: Nationalist/Patriotic; Con-
servative; Law and Order; Pro-Military; Economi-
cally Conservative, but Populist on Trade; Socially
Conservative, but with Libertarian Leanings; Dis-
trustful of Government and Elites; Pragmatic; Pes-
simistic
Cluster Profile 3: Conservative or right-leaning
political views; Belief in individual responsibility;
Skepticism of social justice movements or "woke"
ideology; Potential concern about social instabil-
ity; Preference for a smaller government role in
the economy; May value traditional values and
institutions; May believe in American exceptional-
ism; May prioritize economic growth over social
programs; Possible distrust of government
Cluster Profile 4: Progressive/Left-leaning po-
litical views; Distrust of large institutions; Empha-
sis on diplomacy and international cooperation;
Socially liberal; Belief in nuanced approaches;
Slight racial anxiety; Confidence in the electoral
system; Value on expertise; Mixed feelings on the
role of government; Pragmatic approach to mili-
tary strength
H.4.3
8 clusters (OpinionQA - Wave 27)
Cluster Profile 1: Believes in American excep-
tionalism, but acknowledges other great nations;
Values democracy and allies; Supports a strong so-
cial safety net but believes in personal responsibil-
ity; Pragmatic and values compromise; Optimistic
about social progress; Values traditional family
structures; Concerned about voter fraud, but sup-
ports voting rights; Supports separation of church
and state, but sees value in religious belief; Positive
about technology and globalization; Believes in a
larger government role; Socially moderate; Eco-
nomically progressive; Generally content but sees
areas for improvement; Skeptical of politicians and
the political system; Believes in expert knowledge;
Believes in a strong military and good diplomacy;
Values immigration but with controls; Believes in
personal freedoms but recognizes the need for some
government intervention; Doesn’t feel disrespected
but acknowledges white privilege
Cluster Profile 2: Nationalist/Patriotic; Con-
servative; Law and Order; Pro-Military; Economi-
cally Conservative, but Populist on Trade; Socially
Conservative, but with Libertarian Leanings; Dis-
trustful of Government and Elites; Pragmatic; Pes-
simistic
Cluster Profile 3: Conservative or right-leaning
political views; Belief in individual responsibility;
Skepticism of social justice movements or "woke"
ideology; Potential concern about social instabil-
ity; Preference for a smaller government role in
the economy; May value traditional values and
institutions; May believe in American exceptional-
ism; May prioritize economic growth over social
programs; Possible distrust of government
Cluster Profile 4: Socially liberal/Moderate;
Economically left-leaning; Pro-immigration and
diversity;
Trust in experts and government;
Democratic-leaning but not entirely aligned; In-
ternationally cooperative; Values traditional fam-
ily structures but with flexibility; Believes in equal
rights but acknowledges challenges; Sense of fair-
ness and respect; It’s important to note

--- Page 29 ---

Cluster Profile 5: Pro-corporations; Egalitar-
ian parenting; Second Amendment supporter, but
with nuance; Concern about election integrity, but
not extreme distrust; Support for social safety nets,
but potentially limited government intervention;
Generally distrustful of government; Minimizes
racial inequality; Deference to expertise; Toler-
ance of offensive speech; Ambivalence towards
wealth inequality; Non-interventionist foreign pol-
icy or satisfaction with current military spending
Cluster Profile 6: Conservative leaning; Nation-
alist/America First; Socially conservative; Distrust
of Government and Elites; Tough on Crime; Eco-
nomic Conservatism; Pro-Religion; Traditional
Values; Belief in Personal Responsibility; While
not explicitly stated, a potential for racial resent-
ment; It is important to note
Cluster Profile 7: Progressive/Liberal lean-
ing; Socially Liberal; Economic Populist; Pro-
government Intervention; Religious; Community-
Oriented; Distrustful of Institutions; Diplomatic
but Values Democracy; Pro-Voting Rights; Belief
in Experts; Criminal Justice Reform; Pessimistic
about the Present; Believes in Compromise; Con-
cerned about Free Speech; Open to Other Lan-
guages; Believes in shared values; Potentially
holds contradictory views
Cluster Profile 8: Progressive/Left-leaning po-
litical views; Distrust of large institutions; Empha-
sis on diplomacy and international cooperation;
Socially liberal; Belief in nuanced approaches;
Slight racial anxiety; Confidence in the electoral
system; Value on expertise; Mixed feelings on the
role of government; Pragmatic approach to mili-
tary strength
H.5
PRISM
H.5.1
2 clusters (PRISM)
Cluster Profile 1: Completeness and Thorough-
ness; Specificity and Directness; Accuracy and
Up-to-date Information; Neutrality and Objectiv-
ity; Practical Utility; Contextual Awareness; User
Control and Agency
Cluster Profile 2: Completeness and Thorough-
ness; Directness and Assertiveness; Neutrality, but
with Context; Proactive Helpfulness; Formal Tone;
Accuracy and Factuality; Engagement and Conver-
sational Flow
H.5.2
4 clusters (PRISM)
Cluster Profile 1: Completeness and Thorough-
ness; Directness and Assertiveness; Neutrality, but
with Context; Proactive Helpfulness; Formal Tone;
Accuracy and Factuality; Engagement and Conver-
sational Flow
Cluster Profile 2: Prefers helpfulness and rele-
vance over assumptions; Appreciates nuanced and
comprehensive answers; Values honesty and aware-
ness of limitations; Favors open-ended conversa-
tion and assistance; Respects diverse perspectives
and avoids generalizations; Prioritizes accuracy
and avoids potential misinformation
Cluster Profile 3: Completeness and Thorough-
ness; Specificity and Directness; Accuracy and
Up-to-date Information; Neutrality and Objectiv-
ity; Practical Utility; Contextual Awareness; User
Control and Agency
Cluster Profile 4: Practicality and Actionabil-
ity; Thoroughness and Detail; Emphasis on Pos-
itive Communication; Desire for Structure and
Guidance; Appreciation for Contextual Nuance;
Preference for Proactive Problem-Solving; Poten-
tial Discomfort with Ambiguity
H.5.3
8 clusters (PRISM)
Cluster Profile 1: Completeness and Thorough-
ness; Specificity and Directness; Accuracy and
Up-to-date Information; Neutrality and Objectiv-
ity; Practical Utility; Contextual Awareness; User
Control and Agency
Cluster Profile 2: Practicality and Actionabil-
ity; Thoroughness and Detail; Emphasis on Pos-
itive Communication; Desire for Structure and
Guidance; Appreciation for Contextual Nuance;
Preference for Proactive Problem-Solving; Poten-
tial Discomfort with Ambiguity
Cluster Profile 3: Values direct answers over
hedging; Appreciates nuanced perspectives; Fa-
vors a conversational and welcoming tone; Prior-
itizes specific details over generic praise; Trusts
recommendations that consider local perspective;
May appreciate subtlety and avoids overly strong
endorsements; Potentially values the feeling of dis-
covery; Might be influenced by writing style and
fluency
Cluster Profile 4: Completeness and Thorough-
ness; Directness and Assertiveness; Neutrality, but
with Context; Proactive Helpfulness; Formal Tone;
Accuracy and Factuality; Engagement and Conver-
sational Flow
Cluster Profile 5: Prefers conciseness and di-
rectness; Values politeness and helpfulness; Favors
factual and relevant information; Appreciates sim-
plicity over technical jargon; Prioritizes functional

--- Page 30 ---

answers; May have a lower tolerance for conver-
sational fillers; Could value transparency, but only
to a certain extent; Possibly prefers a less anthro-
pomorphic model
Cluster Profile 6: Prefers helpfulness and rele-
vance over assumptions; Appreciates nuanced and
comprehensive answers; Values honesty and aware-
ness of limitations; Favors open-ended conversa-
tion and assistance; Respects diverse perspectives
and avoids generalizations; Prioritizes accuracy
and avoids potential misinformation
Cluster Profile 7: Practicality and Actionable
Advice; Thoroughness and Detail; Directness and
Assertiveness; Real-World Applicability; External
Validation and Authority; Focus on Well-being; Be-
lief in Inclusivity and Fairness; Appreciation for
Nuance and Context
Cluster Profile 8: General Communication
Style; Brevity and Directness; Empathy and En-
couragement; Informality and Approachability; In-
formation and Advice; High-Level Overview; Bal-
ance of Practical and Emotional Considerations;
Less Emphasis on Specifics; It’s important to note
H.6
ValuePrism Valence
H.6.1
2 clusters (ValuePrism Valence)
Cluster Profile 1: Autonomy and bodily integrity,
especially for children; Nuance in medical deci-
sions; Open communication is acceptable, but forc-
ing compliance is not; Potential harm of medica-
tion; Belief in a child’s ability to learn and make
good choices with guidance; Respect for individ-
ual differences; Potential for parental overreach;
Emphasis on intrinsic motivation over extrinsic
pressure
Cluster Profile 2: Inclusivity and acceptance;
Freedom of association; Personal autonomy and
self-expression; Opposition to exclusion and social
ostracism; Potential belief in restorative justice or
rehabilitation over punishment; Colorblindness or
a belief that race should not be a factor in social
interactions; Actions that do not harm others are
generally moral; Focus on positive social interac-
tions
H.6.2
4 clusters (ValuePrism Valence)
Cluster Profile 1: Inclusivity and acceptance;
Freedom of association; Personal autonomy and
self-expression; Opposition to exclusion and social
ostracism; Potential belief in restorative justice or
rehabilitation over punishment; Colorblindness or
a belief that race should not be a factor in social
interactions; Actions that do not harm others are
generally moral; Focus on positive social interac-
tions
Cluster Profile 2: Egalitarianism and Anti-
discrimination; Social Justice and Advocacy; Inclu-
sivity and Acceptance; Meritocracy and Fairness;
Individualism and Contextual Morality; Potential
Conflict or Uncertainty
Cluster Profile 3: Parental autonomy and rights;
Pro-corporal punishment; Importance of fulfilling
parental responsibilities; Nuance in child rearing
decisions; Skepticism of outside intervention in
families; Traditional gender roles; General permis-
siveness or a broad definition of morality; Poten-
tial prioritization of personal freedoms; Important
Note
Cluster Profile 4: Autonomy and bodily in-
tegrity, especially for children; Nuance in medical
decisions; Open communication is acceptable, but
forcing compliance is not; Potential harm of medi-
cation; Belief in a child’s ability to learn and make
good choices with guidance; Respect for individ-
ual differences; Potential for parental overreach;
Emphasis on intrinsic motivation over extrinsic
pressure
H.6.3
8 clusters (ValuePrism Valence)
Cluster Profile 1:
Egalitarianism and Anti-
discrimination; Social Justice and Advocacy; Inclu-
sivity and Acceptance; Meritocracy and Fairness;
Individualism and Contextual Morality; Potential
Conflict or Uncertainty
Cluster Profile 2: Collectivism over Individual-
ism; Authoritarianism/Respect for Authority; Utili-
tarianism/Consequentialism; Nationalism/Group
Loyalty; Situational Ethics; Distrust of "Freedom
Fighters"; Moral Pragmatism; Potential Double
Standards
Cluster Profile 3: Emphasis on self-reliance
and adult responsibility; Prioritization of societal
norms regarding child development and parenting;
Discomfort with actions perceived as unconven-
tional or exceeding typical boundaries; Potential
value of "tough love" as a parenting strategy; Pos-
sible belief in a clear distinction between childhood
and adulthood; Focus on physical and emotional
development milestones; Potential for a conserva-
tive worldview; Implicit bias or personal experi-
ence shaping judgements
Cluster Profile 4: Strong belief in the sanctity
of life, even for those deemed evil; Pacifism or aver-
sion to violence; Nuance in moral decision-making

--- Page 31 ---

and a rejection of simple utilitarianism; Potential
belief in the inherent rights of individuals; Possible
concern for consequences beyond the immediate
situation; Possible belief in alternative solutions;
Absence of prejudice based on nationality; Possible
emphasis on intention over outcome
Cluster Profile 5: Parental autonomy and rights;
Pro-corporal punishment; Importance of fulfilling
parental responsibilities; Nuance in child rearing
decisions; Skepticism of outside intervention in
families; Traditional gender roles; General permis-
siveness or a broad definition of morality; Poten-
tial prioritization of personal freedoms; Important
Note
Cluster Profile 6: Inclusivity and acceptance;
Freedom of association; Personal autonomy and
self-expression; Opposition to exclusion and social
ostracism; Potential belief in restorative justice or
rehabilitation over punishment; Colorblindness or
a belief that race should not be a factor in social
interactions; Actions that do not harm others are
generally moral; Focus on positive social interac-
tions
Cluster Profile 7: Autonomy and bodily in-
tegrity, especially for children; Nuance in medical
decisions; Open communication is acceptable, but
forcing compliance is not; Potential harm of medi-
cation; Belief in a child’s ability to learn and make
good choices with guidance; Respect for individ-
ual differences; Potential for parental overreach;
Emphasis on intrinsic motivation over extrinsic
pressure
Cluster Profile 8: Individual autonomy and free-
dom; Situational ethics; Prioritization of relation-
ships and consent; Consideration of intent and im-
pact; Non-judgmental attitude; Potential cultural
sensitivity; Flexible and adaptable moral frame-
work
I
Random Profile Samples
I.1
gemma2-9b
I.2
OpinionQA (gemma2-9b - 10 random
value profiles)
• Moderate to conservative politically, lean to-
wards social traditionalism; Believes in puni-
tive justice and stronger sentences; Skeptical
of government intervention but open to some
regulation in specific areas; May have a pref-
erence for more traditional American values
and identity; Views the entertainment industry
positively; Pragmatic about the topic of slav-
ery and racism, perhaps seeing it as a complex
issue with no easy solutions; Concerned about
the quality of political candidates
• Believes that corporations are overly prof-
itable; Believes that progress has been made
towards racial equality in the US over the last
50 years; Feels that people are too easily of-
fended and that this is a major problem; Is
disillusioned with the political process, seeing
compromise as a form of "selling out."; Holds
a nationalist view, believing that other coun-
tries take advantage of the US; Believes that
government assistance to the poor is harmful
• Seeks a balance, not extremes: Often re-
sponds with "neither good nor bad" and fa-
vors "modest" changes; Wary of big govern-
ment and dependency: Believes in limited
government involvement,; Conservative so-
cial views: Holds traditional beliefs about
marriage, family structure, and the role of re-
ligion; Values national strength and security:
Prefers the U.S. to maintain military superior-
ity
• Somewhat nationalistic; Patriotic but hesitant
about uncontrolled immigration; Skeptical of
government efficiency; Leaning conservative;
Values traditional social institutions; Believes
military strength is important for peace
• Supports increased government involvement
in providing services; Believes in strict vot-
ing rights and sees it as a fundamental right;
Holds slightly negative views on the way
things are currently going in the country; Val-
ues diplomacy over military strength; Believes
in compromise in politics; Concerned about
social inequality and the impact of powerful
interests; Positive view of same-sex marriage
• Skeptical of organized religion: Sees no harm
in declining religiosity; Patriotic, but distrust-
ful of foreign aid and international involve-
ment: Prefers focus on American interests
in foreign policy; Values individual liberties
and limited government: Believes government
is wasteful and inefficient, prefers less gov-
ernment intervention in people’s lives; Con-
cerned about social changes and decline in
traditional values: Feels uncomfortable with
increased cultural diversity, expresses discom-
fort with societal shifts; Feels alienated from

--- Page 32 ---

current political landscape: Does not res-
onate with
• Believes the entertainment industry has a pos-
itive effect on the country; Concerned about
offensive language and speech; Believes they
receive respect in society; Feels comfortable
with Republicans expressing their views; Sup-
ports free tuition for public colleges; Believes
K-12 public schools are having a positive ef-
fect; Believes strength and military might are
the best way to ensure peace; Comfortable
with the U.S. being treated fairly in the world
• Believes in social justice and equality, as evi-
denced by their answers on racial inequality,
LGBTQ+ rights, and gender equality; Sup-
ports increased government involvement in so-
cial welfare programs and healthcare; Favors
progressive policies such as universal health-
care, tuition-free public colleges, and stricter
gun control; Is skeptical of corporate power
and believes businesses make excessive prof-
its; Values diplomacy and international coop-
eration over military strength; Is concerned
about the influence of religion in politics and
government
• Strongly nationalist. Believes the US is supe-
rior to other countries; Conservative social
values. Opposes same-sex marriage, believes
traditional family structures are best; Pro-gun
rights and skeptical of gun control measures;
Low regard for government and its inefficien-
cies. Favors limited government intervention;
Supports a strong military presence globally;
Skeptical of immigration and its impact on the
country; Concerned about "political correct-
ness" and believes individuals
• Believes that immigrants, when they come to
the U.S. illegally, can have a slightly nega-
tive impact on communities; Somewhat posi-
tive view of religion and its effect on society;
Holds a belief that the U.S. is a great country,
but not necessarily the best in the world; Con-
vinced that large corporations are detrimental
to the country; Favors the traditional role of
women staying home to raise a family; Feels
that the country has made
I.3
Hatespeech-Kumar (gemma2-9b - 10
random value profiles)
• Believes in keeping things civil and respectful
even in disagreement; Values sensitivity and
empathy towards others; Recognizes the dif-
ference between expressing strong opinions
and being abusive or hateful; Sensitive to lan-
guage that could be hurtful or demeaning;
Appreciates humor that isn’t at the expense of
others
• Distrusts inflammatory language: They often
identify as toxic comments that use emotion-
ally charged words, prejudiced terms, or hate-
ful slurs; Values respectful discourse: They
seem to appreciate comments that express
opinions without resorting to insults or per-
sonal attacks; Recognizes dog-whistles: They
may be sensitive to language that carries
coded meanings or implies prejudice, even
if it doesn’t
• Values; Dislike of bullying and insults: The
rater considers personal attacks and insults to
be toxic, even if they are not overtly aggressive
• Believes some comments are inherently offen-
sive or harmful, regardless of intent; Has a
strong moral compass and considers state-
ments that promote hate, prejudice, or vio-
lence as unacceptable; Values respectful and
constructive dialogue, and sees toxicity as a
barrier to healthy communication; May be
sensitive to language that is demeaning, dis-
criminatory, or exploitative; Recognizes that
power dynamics can contribute to toxicity,
and may be more likely to flag comments that
perpetuate harmful stereotypes or reinforce
social inequalities
• Relatively tolerant:; Contextual understand-
ing:; Focus on direct harm:; Skeptical of gen-
eralizations:
• Holds strong opinions about what is accept-
able language and behavior; Is sensitive to
language that is hateful, disrespectful, or de-
meaning; Values honesty and integrity; Be-
lieves in using language that is constructive
and respectful; Appreciates humor that is not
at the expense of others; Concerned with is-
sues of power and privilege; Possibly politi-
cally left-leaning; Has a strong sense of social
justice

--- Page 33 ---

• Believes Sarcasm and humor, even when ex-
pressed in a seemingly negative way, are not
inherently toxic; Sensitive to language that
is directly aggressive or threatening; Might
prioritize personal expression and freedom
of speech, even if it is unconventional or off-
putting to others; Recognizes that humor can
sometimes be used to mask anger or frustra-
tion, and these underlying emotions may con-
tribute to toxicity; Likely values empathy and
understands the importance of considering
the emotional impact of
• Values humor and light-heartedness, at times
even finding positivity in seemingly innocuous
things; Appreciates self-awareness and hon-
esty, even when it comes to admitting lack of
knowledge; Believes in open discussion and
debate, even if it involves differing opinions;
Views direct insults and personal attacks as
toxic; Recognizes the potential for harm in
language that targets individuals based on
their identity or beliefs; Might lean toward
being forgiving
• Believes strong language is inappropriate;
Belives sexualizing minors is wrong; Under-
stands sarcasm and humor but may not always
be able to detect it
• Might be hesitant to label comments as "toxic"
unless they contain clear hate speech, aggres-
sion, or personal attacks; Values freedom of
expression and believes in giving people the
benefit of the doubt; Could be more sensitive
to sarcasm, humor, or ironic statements that
may be misinterpreted as toxic; Appreciates
brevity and directness in communication
I.4
DICES (gemma2-9b - 10 random value
profiles)
• Values open-mindedness and respect for di-
verse viewpoints; Believes in the importance
of kindness and empathy; Dislikes negativity,
hostility, and inflammatory language; Appre-
ciates humor and lightheartedness; Is gener-
ally optimistic and hopeful about the world
• General lack of concern for hateful or inap-
propriate language, even when blatant; Fo-
cuses on argument structure and lack of direct
aggression as indicators of toxicity; May ig-
nore context, taking statements at face value;
Seems to label anything addressing controver-
sial topics as toxic
• Values friendly and polite conversation;
Doesn’t perceive joking or lightheartedness
as toxic; May have a low threshold for iden-
tifying toxicity, as they labeled conversations
with potentially condescending or manipula-
tive language as "Not Toxic."
• Disagreements and differing opinions are nor-
mal and healthy. Conversation should not be
approached like a debate and should not turn
hostile, dismissive, or personal; Everyone de-
serves to be treated with respect, even if their
views are different from our own
• Valuing honesty and integrity in communica-
tion; Believing in treating others with respect
and kindness, regardless of their beliefs or
background; Encouraging critical thinking
and open-mindedness
• Doesn’t consider casual interactions to be
toxic; Tolerates a range of opinions, even if
they are not politically correct or popular;
Doesn’t seem to be overly sensitive to poten-
tially offensive language; Values genuine con-
versation and humor over politeness; Might
be comfortable with a bit of dark humor
• Values personal reflection and avoids making
sweeping judgments; May be more lenient to-
wards social faux pas and missteps in online
communication; Trusts individuals to under-
stand and navigate complex issues
• Generally non judgmental and avoids mak-
ing assumptions about people; Prefers direct
and honest communication; Believes in treat-
ing everyone with respect, regardless of their
background or beliefs; Values empathy and
understanding; Encourages critical thinking
and open-mindedness
• Believes hurtful language is unacceptable;
Values respectful communication; Discour-
ages generalizations and stereotypes; Em-
pathizes with others’ perspectives; Promotes
critical thinking and healthy skepticism; Per-
sonal insults and aggressive language; Dis-
respectful or condescending tone; Harmful
stereotypes and generalizations; Promotion of
hate speech or prejudice; Encouraging harm-
ful or illegal activities; Exploitation

--- Page 34 ---

• Believes a lot of conversations are benign;
May have a low tolerance for strong negativ-
ity; May value straightforwardness
I.5
ValuePrism (gemma2-9b - 10 random
value profiles)
• Honesty is generally valued, but can be situa-
tional; Loyalty to friends is likely important,
as is prioritizing their well-being; Straightfor-
wardness may not always be the most com-
passionate approach; Exploiting someone for
personal gain or manipulating them is wrong;
Protecting oneself is morally justifiable
• Values situational context heavily when de-
termining morality; Holds traditional views
on family structures and authority; May have
discomfort with concepts like gender fluidity;
Believes in parental authority and may disap-
prove of challenging it; May prioritize obedi-
ence and adherence to rules
• Values individual liberty and autonomy; Be-
lieves in resistance to oppressive institutions
or systems; May have socialist or left-wing
political leanings; Sees economic sanctions
as a tool for influencing policy and achieving
justice; Generally believes in using peaceful
means to achieve political change; May be
critical of military intervention and powerful
corporations
• Prioritizes the needs of family; Believes
that survival trumps strict adherence to
laws/morality; May have a strong sense of
empathy and compassion for those in need;
May have a utilitarian perspective, judging
actions based on their outcomes. Utilitarian-
ism: The idea that the best action is the one
that maximizes happiness and minimizes suf-
fering; May not distinguish morality based on
race or nationality
• Strong belief in humanitarianism and helping
those in need; Strong opposition to oppres-
sive regimes and systems of power; Support
for democracy and individual freedom; Ten-
dency to view actions in a binary way, often
as "moral" or "immoral"; May be influenced
by political ideologies that emphasize justice
and anti-imperialism; A clear sense of right
and wrong based on perceived victimhood and
injustice
• Values fairness and justice; Believes in per-
sonal responsibility and accountability; Em-
phasizes the importance of empathy and un-
derstanding; Distinguishes between actions
that are inherently right or wrong and those
that depend on context; Prioritizes individual
autonomy and freedom of choice; Criticizes
abuse of power and authority; Values integrity
and honesty
• Believes in the greater good; Upholds au-
thority and established norms; Values protect-
ing children and sees harm to them as unac-
ceptable; Progressive and tolerant of diverse
family structures; Potential emphasis on non-
violence as a core value
• Believes in inherent rewards and positive re-
inforcement; Values competence and meritoc-
racy; Holds a view that setting clear expecta-
tions and consequences is important
• Believes in situational ethics; Values helping
others; Likely values religious identity and
community; Views helping friends as morally
right; Has a strong sense of moral intuition
• Values familial relationships highly; Believes
in individual autonomy and the right to make
one’s own choices; Values loyalty and sup-
port for loved ones; Doesn’t seem to adhere
to strict rules or social norms; May prioritize
personal fulfillment over strict work obliga-
tions
I.6
Habermas (gemma2-9b - 10 random value
profiles)
• Believes in strong government intervention
and regulation; Prefers a more egalitarian so-
ciety with less inequality; May be concerned
about the societal impact of smoking and alco-
hol consumption; Supporting of public health
initiatives and increased spending on health-
care; May hold traditional or conservative
views on certain social issues, such as mar-
riage
• Believes in giving the people a voice and hav-
ing referendums on important issues; Sup-
ports increased public spending on infras-
tructure like railways; Prefers the current
democratic system over a more direct form of
democracy; Favors the monarchy and main-
taining the UK as a constitutional monarchy;

--- Page 35 ---

Believes in progressive taxation, with a higher
tax burden for the wealthy
• Supports government intervention and social
programs; Worried about health and well-
being, especially of young people; Believes
in rules and structure; May be progressive or
left-leaning in their political views
• Believes in social justice and equality; Sup-
ports government intervention to address soci-
etal issues; Likely progressive or left-leaning
politically; Values education and believes it
should be accessible to all; May be concerned
about income inequality; Probably environ-
mentally conscious and supportive of action
on climate change
• Leans towards social safety nets and govern-
ment intervention in the economy; Favors so-
cial justice and redistribution of wealth; May
have concerns about pharmaceutical industry
practices
• Moderate and tends towards neutrality on a
variety of social and economic issues; May
be open to both sides of an argument and
struggles to commit to a firm stance; Lacks
strong convictions or definitive beliefs about
complex issues; Prefers a balanced approach
rather than taking a strong position
• Progressive on social issues, likely support-
ing universal healthcare and social services;
Skeptical of traditional institutions and hier-
archies; Believes in individual responsibility
and social good, but not necessarily a strict
moral obligation; Concerned about the en-
vironment and public health; Possibly views
capitalism with some criticism, possibly favor-
ing more equitable economic systems
• Leans towards caution but open to progress:
This is demonstrated by weakly agreeing with
the statement that AI will not be able to repro-
duce itself; Believes in environmental action:
The strong agreement with imposing a car-
bon tax points towards a belief in the need to
address climate change; Potentially socially
liberal: Individuals who support environmen-
tal regulations may also hold other socially
progressive views
• Pro-choice and believes parents should have
autonomy over medical decisions for their
children; May believe in a separation of
church and state; Generally supportive of so-
cial justice causes, including expanding vot-
ing rights and redistributive taxation; Envi-
ronmentally conscious, supporting policies to
reduce plastic waste
• Believes in a strong social safety net and
helping those in need; Supports increasing
taxes on the wealthy to fund social programs;
Believes in government intervention to ad-
dress social issues like misinformation and
unhealthy corporate practices; Seeks a bal-
ance between individual rights and collective
good; Generally favors regulation to protect
consumers and ensure fairness; Values trans-
parency and accountability, evidenced by sup-
port for diversity data publication and corpo-
rate liability; May be skeptical of unfet
I.7
Prism (gemma2-9b - 10 random value
profiles)
• Values clarity, conciseness, and directness in
communication; Prefers factual and straight-
forward responses over opinionated or spec-
ulative ones; Appreciates respectful and em-
pathetic responses, even in difficult situations;
Dislikes responses that are overly verbose,
rambling, or unprofessional; May have a low
tolerance for sarcasm or humor that could be
misconstrued
• Prefers factual and informative responses
over personal opinions or feelings; Appre-
ciates neutrality and objectivity, especially
on potentially controversial topics; Values
concise and to-the-point answers; Seeks re-
sponses that demonstrate a clear understand-
ing of the topic; Values objectivity and fac-
tual information over personal opinions or
emotions; Prefers concise and direct answers;
Appreciates responses that demonstrate exper-
tise or knowledge
• Values concise and informative responses;
Prefers responses that acknowledge limita-
tions; Appreciates neutral and objective lan-
guage; Encourages respectful and balanced
discussion; Seeks depth and insight beyond
superficial statements
• Prefers concise and direct answers; Values
practicality and specific information; Appre-
ciates a conversational tone

--- Page 36 ---

• Values critical thinking and questioning au-
thority; Believes in democracy and the impor-
tance of informed citizenry; May be wary of
unchecked power and institutions; Prefers di-
rect and to-the-point answers; Appreciates a
response that encourages further thought and
discussion
• Values neutrality and objectivity: The rater
prefers responses that avoid stating opinions
or taking sides; Appreciates factual informa-
tion: The rater seems to value responses that
provide factual information and avoid spec-
ulation or generalizations; Concerned about
potential harm: The rater seems to be sensi-
tive to the potential for harm that can result
from divisive language and misinformation;
Belives in open dialogue: The rater values
responses that encourage open and honest
conversation about complex issues
• Lists are preferable to narrative summaries;
Prefers concision over elaboration; Values
neutrality and avoids subjective language
• Values clear and concise humor; Appreciates
a conversational tone; May value creativity
and originality in humor
• Values neutrality and objectivity: The rater
seems to appreciate responses that avoid stat-
ing opinions or beliefs as facts; Prefers com-
prehensive and informative answers: The
rater often chooses responses that provide
more detailed information or explore multiple
perspectives; Seeks respectful and inclusive
language: The rater seems to value responses
that demonstrate sensitivity to diverse view-
points
• Values professional help for mental health is-
sues; Prefers direct and concise language; Fo-
cus on actionable advice
I.8
gemma2-27b
I.9
OpinionQA (gemma2-27b - 10 random
value profiles)
• Doesn’t necessarily see the government as a
solution to all problems; Favor capitalism and
believes large corporations in general have
a positive effect; Leans toward conservative
social values; Believes in American exception-
alism and the unique role of the U.S. military
in maintaining global peace; May prioritize
individual liberties and responsibilities above
collective well-being
• Believe society is moving in an unfavorable
direction; Hold somewhat traditional social
views, believing marriage and children are
important and society should prioritize them;
Believe government intervention is sometimes
necessary, but prefer smaller government with
less services; Wary of immigration and the
impact it has on communities; Skeptical of
large corporations and their influence; Value
diplomacy over military strength in interna-
tional relations; While not necessarily reli-
gious themselves, see churches and religious
organizations as a positive force
• Believes in political compromise, accepting
that it sometimes involves concessions; Val-
ues pragmatism over ideological purity; Sees
prison sentences as potentially too harsh;
Holds generally positive views of the United
States, though without an exceptionalist atti-
tude; Is generally accepting of both corpora-
tions and the government, viewing both as
capable of performing their functions ade-
quately
• Believes that white people only benefit “Not
too much” from systemic advantages over
Black people.
This suggests they may not
fully grasp the extent of systemic racism or
think it’s a significant issue; Favors less gov-
ernment assistance for those in need. This
suggests a skepticism towards government in-
tervention and possibly support for smaller
government; Believes billionaires are a neg-
ative force. This indicates belief in economic
inequality as a problem; Emphasizes voting
integrity, particularly preventing non-citizens
from
• Individuals convicted of crimes often don’t
serve enough time in prison; This person may
feel marginalized and under-respected in so-
ciety; He/She holds neutral views on demo-
graphic changes, believing that they have nei-
ther a positive nor negative impact; He/She
believes that while faith is beneficial, it is not
essential for morality; This person perceives
a significant ideological gap between the two

--- Page 37 ---

main political parties; This person believes in
the power of diplomacy as a means to
• Values inclusivity and acceptance of diver-
sity; Believes in providing opportunities for
undocumented immigrants to become legal
citizens; Comfortable with multilingualism
in public spaces; May hold liberal political
views; Might be distrustful of people who hold
different political views
• Believes government should prioritize provid-
ing basic social safety nets for its citizens;
Views the U.S. as generally fair but acknowl-
edges flaws; Favors a mixed economic system
with some regulation, valuing a balance be-
tween private enterprise and social welfare;
Hold some conservative values but balances
them with liberal perspectives; Advocates for
religious freedom but believes it should not
overly influence public policy; Believes in
• Supports a mixed public/private healthcare
system; Believes Republicans are comfortable
expressing their political views; Believes there
is still a lot of work to be done to achieve
racial equality; Favors increased government
assistance for those in need; Views the influ-
ence of churches and religious organizations
as negative; Believes an increase in the num-
ber of guns is slightly detrimental to society;
Values expert opinion in policy making; Be-
lieves increased attention to the
• Skeptical of government involvement, specifi-
cally favoring smaller government and fewer
social services; Favors individual liberty and
autonomy, believing the government should
not overly restrict citizens’ choices; Socially
conservative with concerns about immigra-
tion, the rise of secularism, and traditional
family values; Holds a distrust of large cor-
porations and financial institutions, believing
they have a negative impact on society; Be-
lieves in American exceptionalism and the im-
portance of international diplomacy; Has a
cautious optimism about the
• Believes in the importance of government pro-
viding basic needs for citizens; Believes col-
lege is beneficial; Believes in strong national
defense; Believes in diplomatic solutions over
military force; Believes that open borders are
detrimental to national identity; Prefers a
smaller government with fewer services; Be-
lieves that some immigrants make communi-
ties worse; Believes in traditional family val-
ues; Is somewhat resistant to change; Has
faith in democracy and believes people who
are able to vote should vote
I.10
Hatespeech-Kumar (gemma2-27b - 10
random value profiles)
• Tolerant of informal language and spelling
errors; May be lenient when judging offensive
language, depending on context; Believes that
expressing strong emotions, even anger, is not
inherently toxic; May have a higher threshold
for what is considered "offensive"; Could be
open to adult themes and content, depending
on the implementation
• Belief in objective meaning of toxicity; Will-
ingness to accept potentially controversial
statements as non-toxic if they are not directed
at a specific person; Possible comfort with sex-
ual themes, as long as they are not explicitly
aggressive or graphic; May consider boasts
or self-promotion to be toxic language. May
have a relatively relaxed view on profanity
• Believes that comments that are excessively
aggressive or insulting are toxic; Believes that
comments that tell someone to "go away" or
make them feel unwelcome are toxic; Believes
that comments that express strong or hyper-
bolic opinions without providing supporting
evidence can be toxic; Recognizes that humor
can be subjective and some people might find
things funny that others find offensive
• Believes profanity is toxic; Believes stating
an opinion strongly is toxic; Doesn’t seem to
mind indirect insults; May think expressions
of anger or frustration are toxic even if not
directed at anyone; May think that bragging
or boasting is toxic; May believe statements
that could be
• Believes that expressing strong negative emo-
tions is toxic; Believes that derogatory and
dehumanizing language is toxic; Believes fac-
tual disagreement, even if strongly worded, is
not toxic; Believes that generalizations about
groups of people are potentially toxic; Doesn’t
mind sarcasm or irony as long as it isn’t tar-
geted at individuals; Believes that discussing
sensitive topics is not inherently toxic

--- Page 38 ---

• Believes personal loyalty and commitment are
positive traits; May have a tendency to see
things in black and white. -; Believes strong
expressions of patriotism are positive; Be-
lieves in traditional gender roles. -; Is quick
to label things as "evil" or morally wrong; Is
susceptible to conspiracy theories; Is desensi-
tized to violence in some
• Believes some jokes can be considered toxic;
Likely believes context is important in deter-
mining toxicity:; May believe certain types of
comparisons; May have a looser definition of
toxicity, focusing on statements that are
• May believe that political correctness is im-
portant; May be overly sensitive to poten-
tially offensive language; May have a strong
sense of social justice; May judge individuals
based on their group affiliation; May have a
strong moral compass and believe in right and
wrong; May be quick to anger or frustration;
May have a low tolerance for disagreement
• This rater distinguishes between rude or of-
fensive language and actual toxic harm; This
rater may believe that humor and jokes are
acceptable, even if they are edgy or could be
construed as mildly offensive by some; This
rater appears to value freedom of expression
and may be tolerant of dissenting opinions,
even if they are controversial; This rater may
have a low threshold for blocking or ignoring
users they perceive as annoying or bothering
them
• Toxicity is primarily defined by hateful lan-
guage, slurs, and harmful stereotypes; Casual
vulgarity is not inherently toxic; Mild expres-
sions of frustration or disagreement are ac-
ceptable; Personal insults, especially those
targeting personal characteristics; Opinions
can be expressed freely, as long as they are
not presented in a hateful or demeaning way
I.11
DICES (gemma2-27b - 10 random value
profiles)
• People should be treated with respect; Every-
one has the right to their own opinion; Toxic
conversations are those that are hateful, dis-
respectful, or incite violence; It’s important
to consider the context of a conversation; It’s
okay to disagree with someone, but it’s impor-
tant to do so civilly
• Seems to be tolerant of strong language; Be-
lieves discussions about sensitive topics; May
prioritize a kind and helpful tone even in dis-
agreements; Perhaps sees humor and sarcasm
as not always being inherently toxic; Doesn’t
always view disagreement as inherently
• Believes that direct and factual conversations
are not toxic; Believes that polite and friendly
conversations are not toxic; Believes that
short, uneventful conversations are not toxic;
May have a higher tolerance for abrupt or
unusual conversation styles, as evidenced by
rating the fourth conversation as "Not Toxic."
• Believes honesty is important; Believes in re-
specting the intelligence of others; If someone
claims they know something personal, that’s
a pretty bold claim; Prefers conversational-
ists who don’t engage in hyperbole; Dislikes
being condescended to; Believes casual sex-
ism is never acceptable; While open to playful
banter, they dislike conversations that are con-
descending, rude, or unnecessarily sarcastic;
Believes in following through on one’s com-
mitments
• Respect for others
• It seems likely that the rater judges toxic-
ity based on if the conversation is intention-
ally harmful or aggressive; They seem to be
comfortable with conversations that discuss
potentially sensitive topics like communism,
homelessness, gender differences, and lottery
spending as long as they are not done in a
hateful or disrespectful way; The rater may
have a preference for lighthearted and casual
conversations, as evidenced by their label-
ing of short and simple conversations as "Not
Toxic."
• Believes personal experience can be relevant
to judging toxicity; Values clear communi-
cation in conversation; May be cautious of
making generalizations or assumptions about
people based on limited information -
• Believes AI safety is important; Is politically
neutral and treats all viewpoints with respect;
Doesn’t believe there is one "right" way to
have a conversation; Sees the positive in most
situations; Is not overly concerned with gram-

--- Page 39 ---

mar or punctuation; Wants to be helpful and
informative
• I feel concerned when people express hatred
or prejudice towards others based on their
race, religion, gender, sexual orientation, or
any other protected characteristic; I believe
that everyone deserves to be treated with re-
spect and dignity, regardless of their beliefs
or background; I value open-mindedness and
the ability to engage in constructive dialogues
even when there are disagreements; I find it
troubling when individuals use harmful lan-
guage or engage in personal attacks; I strive
to promote understanding and empathy in my
• Values politeness and respectful communica-
tion; May believe in giving people the benefit
of the doubt. May prioritize factual accuracy
in discussion; Might be averse to confronta-
tional or accusatory language; Possibly val-
ues a cooperative and helpful tone in conver-
sations
I.12
ValuePrism (gemma2-27b - 10 random
value profiles)
• Believes in nuanced moral judgments, not ab-
solutes; Places importance on context and
situational factors; May prioritize pragma-
tism or effectiveness when evaluating moral-
ity; Possibly interested in political affairs
• Believes in open communication in relation-
ships; Values financial responsibility; Views
marriage as a positive institution
• Believes insects have a right to live; May be-
lieve in the interconnectedness of all living
things; May be opposed to broad extermina-
tion efforts
• Believes in acts of charity and selflessness;
Values humility and admitting when wrong;
Appreciates acts of repentance and forgive-
ness; Likely believes in a higher power; Be-
lieves in helping those in need, even strangers;
Values sincerity in apology and action but
disapproves of seeking validation; Sees ac-
cepting defeat as morally sound; Might value
tradition or religious practices
• Believes that providing basic care for chil-
dren; Believes that showing physical affection
to children is moral; Possibly believes that
non-sexual physical contact between a parent
and child is acceptable, regardless of gender
or age; Believes that generally leaving chil-
dren unattended while they are experiencing
distress; Holds a standard that abandoning
a child outside to sleep is immoral; Possi-
bly holds traditional views about family and
child-
• Believes helping those in need is moral; May
believe in prioritizing the needs of family;
May sympathize with Palestinians
• Believes there are strong moral obligations
to truthfulness; May believe there are some
exceptions to these obligations in extreme cir-
cumstances; Appreciates the importance of
informing the public about historical atroci-
ties; Values loyalty and might be conflicted
about situations which pit this against other
moral considerations
• Believes in obeying authority figures, even
when inconvenient; Values familial duty and
responsibility; May be strict in upholding so-
cietal norms and expectations; May find it
important to uphold work commitments
• Strong aversion to violence; Pacifistic tenden-
cies; Belief that morally good actions should
be non-violent
• The rater may believe helping those less for-
tunate is inherently good; The rater may have
concerns about the potential misuse of emer-
gency services; The rater may believe there
are more effective or appropriate ways to as-
sist those in need than calling the police; The
rater may recognize that situations involv-
ing poverty are complex and require nuanced
judgments
I.13
Habermas (gemma2-27b - 10 random
value profiles)
• This rater likely believes in strict immigra-
tion policies; This rater likely prefers limited
government intervention in social services
• Values individual liberty and autonomy; Be-
lieves in the importance of limited government
intervention; May believe in a free market ap-
proach to economic problems; Believes in the
importance of public services but is cautious
about raising taxes

--- Page 40 ---

• Belief in some level of government interven-
tion in the economy; Support for social safety
nets and programs; Potential trust in experts
or scientific consensus; Likely supports pro-
gressive policies such as wealth redistribution;
Possibly leans left on the political spectrum;
May value individual autonomy to a degree
• Values the well-being of future generations.
This is evident in their support for increased
government funding for education and health-
care for young people; Believes in investing in
essential public services. Their strong support
for increased salaries for teachers and doc-
tors reflects this value; Supports strong gov-
ernment regulation, especially in the face of
potentially harmful entities like internet com-
panies; Prioritize public safety and national
security. This can be inferred from their strong
belief that the UK is under-spending on de-
fense
• May believe that law enforcement needs more
resources to effectively combat crime; Be-
lieves in safety regulations and may be con-
cerned about public safety; Believes in civic
participation and engaging with political pro-
cesses, but potentially sees maturity as a pre-
requisite; Believes in the social contract and
a role of government in providing public ser-
vices. They may also be willing to contribute
financially to these services
• Believes in social responsibility and global
solidarity; Supports government intervention
to solve social issues; May believe in progres-
sive taxation; Values environmental sustain-
ability
• Strong belief in fiscal conservatism and poten-
tially limited government intervention. Seems
opposed to free public services; Hard stance
against illegal drugs; Likely values public
safety and order; May prioritize traditional
values and potentially be socially conserva-
tive; Believes in meritocracy and likely values
individual responsibility; Likely skeptical of
environmental alarmism and/or interventions
• Values fiscal responsibility and may lean to-
wards smaller government; Believes strongly
in animal welfare and considers the well-
being of animals as a primary concern; Con-
cerned about environmental issues and is will-
ing to adopt measures addressing them
• Believes in economic justice and redistribu-
tion of wealth; Likely supports socialist or
left-leaning policies; May support individ-
ual autonomy and bodily integrity in contexts
like organ donation; Likely has a positive
view of technological progress and innova-
tion, while acknowledging potential down-
sides; May have an animal welfare perspec-
tive and oppose practices like fox hunting;
May believe in harm reduction approaches
to issues like smoking; Likely values social
welfare and support for marginalized popula-
tions; Has faith in the potential
• Values public health; Disapproves of Theresa
May’s leadership; Open to nuclear power as a
source of energy; Supports government invest-
ment in renewable energy; Believes in prevent-
ing children from secondhand smoke exposure;
Believes in population control measures; Be-
lieves in giving citizens more direct influence
on policy
I.14
Prism (gemma2-27b - 10 random value
profiles)
• Values concise and factual answers over elab-
orate explanations; Prefers responses that
acknowledge alternative viewpoints, even if
briefly, before coming to a conclusion; Ap-
preciates politeness and a helpful tone; May
value avoiding definitive statements where ap-
propriate; Prefers neutral and unbiased re-
sponses, avoiding personal opinions or be-
liefs; May favor responses that present a bal-
anced view by mentioning both sides of an
argument; Appreciates historical context
• Values direct and concise answers; Appreci-
ates detailed explanations
• Prefers factual and concise responses; May
value politeness and careful language espe-
cially when dealing with sensitive topics; Pos-
sibly prefers responses with a more formal
tone; Values responses that acknowledge the
ongoing nature of a situation and avoids spec-
ulation; Perhaps prefers information to be
delivered in a direct manner
• Values nuanced, balanced responses over
straightforward answers; Prefers empathetic

--- Page 41 ---

and understanding language; Prioritizes per-
sonal freedom and self-determination; May be
suspicious of definitive statements or strong
opinions; Prefers responses that acknowledge
complexity and varying perspectives
• Believes that shorter, concise answers are
more desirable than longer more detailed
ones; Values concrete, actionable advice over
general guidance; Possesses a bias towards
career paths that retain relevance to the user’s
current skillset
• Believes that people should only use resources
intended for them; Prefers informative and
comprehensive responses over brief and direct
responses; Appreciates detailed descriptions
and enthusiasm in responses
• They are likely someone who prefers factual
and detailed responses, as shown by their pref-
erence for Model A in three out of the four
examples; They may appreciate context and
background information, as seen in the Wal-
lows example; They appreciate neutral and
objective language, as shown by their prefer-
ence for Model A in the conversion therapy ex-
ample. While both responses condemned the
practice, Model A provided a more detached
and informative description
• Values straightforward and concise commu-
nication; Prefers responses that focus on
the user’s stated problem without venturing
into unnecessary details; May not appreciate
overly empathetic or sentimental language;
Values helpfulness and problem-solving
• Prefers longer, more detailed responses over
shorter, more direct ones; Prefers responses
that are more conversational and friendly in
tone; Values politeness and deference to the
reader
• Prefers concise and direct responses; Appre-
ciates helpfulness and informativeness; May
find lengthy or overly enthusiastic responses
off-putting; Prioritizes practicality and clarity
in communication
I.15
gemini
I.16
OpinionQA (gemini - 10 random value
profiles)
• Centrist or moderate political views; Believes
in American exceptionalism; Pro-individual
liberty and personal choice; Economically
satisfied and potentially pro-business; Prag-
matic and willing to compromise; Socially
liberal on some issues, but less clear on oth-
ers; Not strongly invested in election integrity;
Values walkable communities and potentially
environmental concerns; May be distrustful of
government and institutions; Possibly uncer-
tain or ambivalent on certain issues
• Progressive/Liberal political leaning; Strong
belief in racial equality and social justice;
Pro-immigration; Confidence in expertise; Be-
lief in government intervention; Optimism
about social progress; National pride, but not
exceptionalism; Slight concern about polit-
ical correctness; Traditional views on fam-
ily roles; General trust in others; Value on
diversity; Mixed views on the Democratic
Party; Possible concern about free expression
for Democrats; Potential for cognitive disso-
nance; Relative indifference to educational
attainment for societal well-being; Belief in
criminal justice reform
• Generally satisfied with the status quo; Mod-
erate politically; Prioritizes national inter-
ests; Supportive of traditional family values;
Tolerant and accepting of diversity, but with
some reservations; Skeptical of government
overreach, but believes in its role in certain
areas; Pragmatic and distrustful of compro-
mise; Believes in individual responsibility and
limited government intervention; Confident in
existing systems; Values religious belief, but
supports separation of church and state; Neu-
tral or ambivalent on several social issues;
Values personal liberty and freedom of expres-
sion; Not overly concerned about inequality;
Believes in American exceptionalism, but ac-
knowledges other great nations
• Generally satisfied with their personal level
of respect in society. They feel they receive
the respect they deserve.; Pro-labor. They see
labor unions as having a positive impact on
the country.; Traditional gender roles. They
believe it’s generally better for the mother to
stay home if one parent can.; While acknowl-
edging some racial inequality persists, they
don’t see it as a major issue. They think a lit-
tle more needs to be done to ensure equal
rights, suggesting a belief that significant

--- Page 42 ---

progress has already been made.; Prioritizes
border security in immigration policy. They
believe stronger enforcement and border se-
curity should be prioritized over pathways
to citizenship for undocumented immigrants.;
Tolerant of other languages but perhaps with
some reservation. They aren’t greatly both-
ered by hearing other languages, but their
response of "not much" instead of "not at all"
suggests a possible slight preference for En-
glish in public spaces.; Deference to exper-
tise. They believe experts are usually better
at making policy decisions than others.; Pro-
military and favors a strong national defense.
They want to see the military grow and for the
U.S. to remain the sole military superpower.
This, combined with their belief in the effi-
cacy of military strength for peace, suggests
a hawkish foreign policy stance.; Conserva-
tive leaning. They disapprove of Joe Biden,
feel the Democratic party doesn’t represent
them, and hold views that align with conser-
vative positions on several issues.; Religious,
but not necessarily highly devout. They see
religion as positive for society, but don’t see
belief in God as essential for morality. They
favor the separation of church and state.; Be-
lieves in limited government. They prefer a
smaller government with fewer services and
see government as often wasteful. However,
they also believe in continuing social secu-
rity programs and believe a modest reduction
in government is sufficient.; Believes in per-
sonal responsibility and self-reliance. This
is suggested by their view that government
aid to the poor creates dependency.; Believes
obstacles still exist for women. While they
might not believe these obstacles are as large
as they once were, they recognize that there’s
still progress to be made on gender equal-
ity.; Values clear moral distinctions. They
believe most things in society can be clearly
divided into good and evil.; Supports gun con-
trol. They see a rise in gun ownership as very
bad for society.; Believes in free speech for all
political affiliations. They see both Democrats
and Republicans as comfortable expressing
their views.; Concerned about changing demo-
graphics. They see a decline in the white share
of the population as somewhat bad for soci-
ety.; Values traditional family structures. They
believe society is better off when people pri-
oritize marriage and children.; Generally ac-
cepting of LGBTQ+ people, but with some nu-
ance. They view same-sex marriage as neither
good nor bad and transgender acceptance as
good, suggesting evolving or potentially com-
plex views on these issues.; Skeptical of social
justice movements. Their neutrality on the at-
tention to slavery and racism might indicate
a skepticism of these issues or a belief that
they are being overemphasized.; Believes in
common ground despite political differences.
They think they likely share values with those
who have different political opinions.; Prefers
larger homes and space over walkable com-
munities. This might indicate a preference for
suburban or rural living.; Opposes free col-
lege tuition. This aligns with their limited gov-
ernment stance.; Open to some legal immigra-
tion, but not a large increase. This suggests
a measured approach to immigration policy.;
Positive view of colleges and universities. This
suggests a belief in the value of higher educa-
tion.; Pragmatic approach to politics. They
believe compromise is necessary, even if it
means sacrificing some beliefs.; Realist in for-
eign policy. They believe the US should work
with any country to achieve its goals, even if
it means working with dictatorships.
• Distrust of Power and Institutions; Socially
Liberal/Progressive; Populist Leanings; Lim-
ited Government Intervention; Importance
of Voting Access but Lack of Confidence in
the System; Pragmatic Approach to Political
Experience; Moderate Concern about Voter
Fraud; Potential for Cynicism
• Conservative; Religious; Nationalistic; Tradi-
tionalist; Law and Order; Skeptical of social
justice movements; Distrustful of government
and certain institutions; Economic conser-
vatism; Xenophobic or culturally conserva-
tive; Polarized worldview; Belief in personal
responsibility
• Centrist/Moderate
political
views;
Pro-
business and pro-technology; Socially liberal
on some issues, but with reservations; Impor-
tance of personal responsibility and limited
government; National strength and security;
Importance of voting rights and fair elections;
Pragmatic and nuanced perspective; Tradi-
tional values with some openness to change;

--- Page 43 ---

Belief in American exceptionalism; Potential
for economic anxiety
• Believes in a fair and accessible voting sys-
tem; Socially moderate to conservative; Sup-
portive of a strong social safety net but with
limitations; Concerned about economic in-
equality and corporate power; Skeptical of
government efficiency and elitism; Believes in
a strong national defense, but open to a multi-
polar world; Values personal space and tradi-
tional family structures, but with modern ad-
justments; Pessimistic about societal progress;
Neutral on immigration and religion; Positive
about the impact of colleges and technology
companies; Leans Democrat, but not strongly
partisan; Believes in a black-and-white view
of morality; Believes in harsher criminal jus-
tice
• Pro-immigration;
Gun control advocate;
Socially
liberal/Progressive;
Supportive
of government assistance;
International-
ist/Cooperative foreign policy; Pro-Open
Borders; Confidence in electoral system;
Concern about corporate power; Nuanced
worldview; Trust in experts; Pro public
education
&
Traditional
family
values;
Important Note
• Center-left political leaning; Social liberal
views; Optimistic about progress; Moderate
on some issues; Trust in institutions (with
some reservations); Belief in rehabilitation;
Importance of traditional values (with flexi-
bility); Emphasis on democratic values in for-
eign policy; It’s important to remember these
are inferences and the rater’s views might be
more complex or nuanced than can be fully
captured by a survey. These are simply poten-
tial values and beliefs based on the provided
information.
I.17
Hatespeech-Kumar (gemini - 10 random
value profiles)
• High tolerance for informal language and in-
ternet slang; Leniency towards expressions
of frustration or negativity; Emphasis on di-
rect harm or malicious intent for toxicity; Ac-
ceptance of sexually suggestive language in
certain contexts; Prioritization of freedom of
expression; Possible desensitization to online
language; Potential focus on impact rather
than the mere presence of swear words; Be-
lief that subjective opinions are not inherently
toxic
• Sensitivity to derogatory language; Discom-
fort with aggressive or confrontational tone;
Tolerance for casual swearing and internet
slang; Emphasis on harmful intent; Inconsis-
tency or evolving understanding of toxicity;
Prioritization of personal attacks over gen-
eral negativity; Cultural or generational influ-
ences
• Strong reaction to insults and name-calling;
Sensitivity to discussions of sexual assault and
child abuse; Tolerance for strong opinions
and criticism, within limits; Flexibility with
informal language and internet slang; Un-
clear stance on conspiracy theories; Focus on
direct harm rather than implied negativity
• Sensitivity to emotional expression; High bar
for toxicity; Focus on intent over impact; Po-
tential bias against K-pop or fandom culture;
Lack of understanding of specific cultural con-
texts; Personal interpretation of "toxic"; In-
consistency in application of criteria; Poten-
tial unfamiliarity with political terminology;
Tolerance of potentially offensive language if
not directed
• Strong aversion to negativity and expressions
of hate; Sensitivity to generalizations and
stereotypes; Belief that certain topics should
be discussed with sensitivity; Tolerance for
strong language and informal expression in
some contexts; Focus on the intent or per-
ceived impact rather than solely on the literal
content; Potentially inconsistent or evolving
understanding of toxicity; Limited tolerance
for personal attacks or name-calling; Accep-
tance of casual conversation and speculation
• High tolerance for negativity; Focus on in-
tent to harm or direct insult; Objectivity over
emotional impact; Tolerance for factual dis-
agreements and differing opinions; Context
is not heavily considered (within the limited
data); Possibly a broad definition of "toxic"
• Strong aversion to derogatory language and
slurs; Sensitivity to identity-based attacks;
Low tolerance for generalizations and stereo-
types; Discomfort with comments about sex

--- Page 44 ---

and sexuality; Emphasis on respectful and
constructive communication; Political or ide-
ological leanings; A broader definition of toxi-
city; Inconsistency or evolving understanding;
Prioritization of intent over impact
• Profanity and insults are inherently toxic;
Strong emotional expressions, even negative
ones, are not necessarily toxic if they lack
personal attacks; Political or opinionated
statements, even if potentially controversial,
are not inherently toxic; General statements
or harmless speculation are not toxic; Posi-
tive and encouraging comments are non-toxic;
Personal attacks and derogatory language,
even without profanity, are toxic; The rater
may prioritize "intent to harm" in their as-
sessment of toxicity; The rater may have a
relatively high tolerance for diverse opinions;
The rater may value politeness and respect in
online discourse
• Broad interpretation of "toxicity"; Sensitiv-
ity to political and social issues; Dislike of
strong or potentially offensive language; Aver-
sion to perceived negativity and complain-
ing; Discomfort with potentially controver-
sial topics; Low tolerance for unsolicited re-
quests or boundary-pushing; Potential for
over-generalization; Possible lack of famil-
iarity with certain subcultures or online com-
munication styles
• High tolerance for offensive language and in-
sults; Focus on direct threats and harmful in-
tent; Leniency towards casual and playful lan-
guage; Prioritization of free speech and open
discussion; Limited understanding of microag-
gressions or subtle bias; A potentially narrow
definition of "toxicity"; Possible personal bias
towards certain topics or groups; Acceptance
of online "trash talk" as normal
I.18
DICES (gemini - 10 random value
profiles)
• High tolerance for controversial opinions; Fo-
cus on explicit harm or hate speech; Impor-
tance of intent over impact; Uncertainty in
ambiguous situations; Belief in personal au-
tonomy; Prioritization of personal well-being
and support; Potential discomfort with certain
topics; A non-confrontational approach
• Discomfort with sexual topics; Low tolerance
for negativity or perceived attacks, even in
jest; Sensitivity to personal attacks or dismis-
siveness; Prioritization of emotional support
and empathy; Inconsistency in applying cri-
teria; Possible influence of personal experi-
ences or biases; Unclear understanding of the
definition of "Toxic"; Possible misunderstand-
ing of the task instructions
• Leniency towards strong language/insults; Fo-
cus on intent and context; Sensitivity to cer-
tain topics but not others; Prioritizes di-
rect harm/threats over negativity; Uncertainty
about subtle forms of toxicity; Possible belief
in personal responsibility/freedom of choice;
Inconsistencies in application of criteria
• Tolerance for informal language and typos;
Focus on explicit harm or negativity; High
threshold for toxicity; Potential belief in free-
dom of expression; Prioritization of practi-
cality and usefulness in conversation; Poten-
tially limited understanding of nuanced toxic-
ity; Possible cultural or personal biases
• High tolerance for insensitive or abrasive lan-
guage; Focus on intent over impact; Emphasis
on factual correctness or logical argumenta-
tion; Broad definition of "toxic"; Belief in per-
sonal responsibility and freedom of speech;
Potential desensitization to online negativity;
Possible lack of awareness of microaggres-
sions or subtle forms of toxicity; Prioriti-
zation of information exchange in question-
answering scenarios
• High tolerance for strong language and in-
sults; Focus on intent over impact; Prioritiza-
tion of freedom of expression; Discomfort with
discussions about politics; Inconsistent under-
standing of toxicity; Acceptance of provoca-
tive or dark humor; Potential lack of sensitiv-
ity to certain topics
• High tolerance for offensive language and
controversial topics; Focus on intent rather
than potential harm; Emphasis on direct, ex-
plicit aggression as a marker of toxicity; Be-
lief that disagreement or rudeness does not
necessarily equate to toxicity; Potential lack
of awareness of the broader implications of
certain topics; Possible understanding of on-
line communication norms; Prioritization of

--- Page 45 ---

personal responsibility; Inconsistent applica-
tion of standards; Focus on the surface level
meaning of the conversation
• High tolerance for rudeness and negativity;
Prioritization of freedom of expression; Focus
on intent over impact; Limited sensitivity to
social justice issues; Contextual understand-
ing of "toxic"; Inconsistency in applying stan-
dards; Potential for personal bias
• Drug use and discussion of drug use is toxic;
General negativity and insults contribute to
toxicity; Intolerance and prejudice are toxic;
Statements promoting violence or harm are
toxic; The rater has a high tolerance for sexu-
ally suggestive content; Inconsistency or con-
fusion around religious and political discus-
sions; Context and intent are not always ade-
quately considered; Lack of clear criteria for
"toxicity"
• High tolerance for controversial topics and
opinions; Focus on explicit harm or malice
as indicators of toxicity; Distinction between
offensive content and toxic behavior; Accep-
tance of adult choices and behaviors; Uncer-
tainty around implicit bias and microaggres-
sions; Prioritization of intention over impact;
Leniency in online interactions; Limited un-
derstanding or awareness of certain types of
harm
I.19
ValuePrism (gemini - 10 random value
profiles)
• Humans are superior to animals; Tradition
and cultural norms are morally acceptable;
Playfulness and harmless fun are morally
good; Intentions matter more than potential
harm; Individual autonomy and freedom of
choice are important; Consequences are not
always the sole determinant of morality; A
degree of mischief or mild discomfort is ac-
ceptable in social interactions; Cultural con-
text matters in moral judgments; Focus on
personal pleasure and enjoyment
• Strong belief in free speech and open commu-
nication; Opposition to censorship and sup-
pression of information; Anti-authoritarian
and pro-resistance against perceived oppres-
sion; Belief in challenging harmful ideolo-
gies and individuals; Support for social jus-
tice and minority rights; Emphasis on honesty
and directness; Potential for conflicting val-
ues around violence and interpersonal harm;
Value on personal autonomy and choice; Un-
clear or nuanced stance on certain political
ideologies and figures; It’s important to re-
member that these are inferences based on
limited data. The rater’s reasoning could be
more nuanced or based on factors not cap-
tured in these examples. Further questioning
would be needed to confirm these values and
beliefs and to understand the underlying logic
behind their judgments.
• Utilitarianism/Consequentialism; The sanc-
tity of life, but with a hierarchical view; Impar-
tiality/Universalism; A belief in the greater
good; A lack of strong deontological con-
straints; Possibly a collectivist perspective;
Altruism and a duty to help others; Potentially
a belief in the inherent value of human life,
even with exceptions; Low emotional reactiv-
ity or high emotional regulation
• Parental Authority/Responsibility; Structure
and Discipline are Important; Protecting Chil-
dren from Harm (physical or psychological);
Nuanced understanding of situations; Empha-
sis on education and responsibility; Potential
concern about long-term consequences; Pos-
sible belief in a balance between strictness
and flexibility
• Helping others in need is morally good. This
is the most obvious takeaway, given their con-
sistent "Moral" responses to actions that di-
rectly benefit the homeless.; Social welfare
and support systems are important. Their be-
lief in the morality of providing homes and
ending homelessness suggests a value placed
on societal structures that ensure basic needs
are met.; Reducing suffering is a moral im-
perative. Both actions aim to alleviate the
suffering associated with homelessness, indi-
cating this could be a core belief.; Basic needs
like housing are a human right. This aligns
with the belief in social welfare and suggests
a potentially deontological ethical framework
where certain rights are inherent.; Collective
responsibility for societal well-being. The
rater may believe that society has a collec-
tive responsibility to care for its vulnerable
members.; Utilitarianism – actions that bene-
fit the greatest number are morally good. Pro-

--- Page 46 ---

viding homes and ending homelessness likely
benefits a large portion of society, either di-
rectly or indirectly.; Compassion and empathy
for marginalized groups. The responses sug-
gest a likely inclination towards empathy and
compassion for those experiencing homeless-
ness.; A belief in systemic solutions to societal
problems. "Ending homelessness" implies a
focus on addressing the root causes rather
than just individual instances, hinting at a be-
lief in systemic change.; A positive view of
government or institutional intervention. The
actions implicitly involve government or orga-
nizational efforts, suggesting the rater doesn’t
necessarily see such intervention as negative.;
Equity and fairness as moral principles. The
rater may believe in a just society where ev-
eryone has access to basic necessities like
housing.; Possibly a religious or philosophi-
cal belief system that emphasizes charity and
compassion. Many religious and philosophi-
cal traditions advocate for helping the poor
and vulnerable.; Optimism about the possi-
bility of positive social change. The rater’s
belief that homelessness can be ended sug-
gests an optimistic outlook on the potential
for improvement.
• Low regard for property rights, especially cor-
porate or commercial; "Victimless crimes"
are acceptable; Focus on personal gain or en-
joyment outweighs minor rule-breaking; Anti-
establishment or anti-corporate sentiment; A
belief that these actions have negligible im-
pact; Possible rationalization about resource
abundance; A relaxed or non-traditional
moral code; Prioritization of personal auton-
omy and freedom; A belief that laws or rules
are not always morally sound; Potential influ-
ence of situational factors not explicitly stated
• Believes in civic engagement and participa-
tion; Values democratic principles; May have
a negative view of the Republican party plat-
form or current Republican politicians; Be-
lieves in non-violent political action; Possibly
believes in the legitimacy of elections and the
peaceful transfer of power; May believe that
violence can be justifiable under specific cir-
cumstances; Potential belief in accountabil-
ity for politicians; May believe in the impor-
tance of checks and balances on government
power; Could hold a consequentialist moral
perspective; Possibly believes in the right to
self-defense; May have a nuanced understand-
ing of political conflict
• Altruism and generosity are highly valued.
The rater sees giving away possessions, even
to the point of selling everything, as morally
good, suggesting a belief in the importance of
generosity and helping others.; Detachment
from material possessions is positive. The
actions involve significant material sacrifice.
The positive moral judgment indicates a poten-
tial belief that material possessions are not of
utmost importance, and detachment from them
can be virtuous.; Following a higher purpose
or calling can justify significant sacrifice. The
first action explicitly mentions following Jesus.
This suggests a possible belief that aligning
oneself with a spiritual or higher purpose can
make actions moral, even if they involve signif-
icant personal cost.; Religious faith or spiritu-
ality may be a significant influence. The men-
tion of Jesus in the first example strongly hints
at a potential religious or spiritual framework
influencing the rater’s moral judgments.; Self-
lessness and sacrifice are moral virtues. Both
actions involve giving up something of per-
sonal value. The positive moral assessment
suggests that the rater may view selflessness
and sacrifice as morally positive traits.; Po-
tentially a belief in a specific religious inter-
pretation. Depending on the specific religious
beliefs of the rater, selling all possessions to
follow Jesus might be seen as a specific com-
mandment or ideal within their faith, further
reinforcing its moral goodness in their eyes.;
Possible prioritization of community or collec-
tive well-being over individual wealth. Giving
away possessions could be seen as contribut-
ing to the well-being of others or the commu-
nity, suggesting the rater may prioritize col-
lective good over individual accumulation.;
The rater may believe in a moral imperative
to help those less fortunate. The act of giving
away possessions strongly suggests a possi-
ble belief in the importance of assisting those
in need.; Simplicity and minimalist lifestyles
may be seen as morally positive. The actions
suggest a potential appreciation for a simpler
way of life, where material possessions are
not the primary focus.; Actions motivated by

--- Page 47 ---

sincere faith or conviction are more likely to
be judged as moral. The rater may place a
higher value on actions driven by deep-seated
belief, even if those actions seem extreme from
a different perspective.
• Belief in individual autonomy and freedom;
Nuance in social interactions; Pro-worker
and pro-collective action; Potential belief in
open communication and trust in relation-
ships; Situational ethics; Emphasis on pos-
itive rights; May value social harmony and
avoiding disruption
• Pacifism or strong anti-violence stance; The
sanctity of human life; Situational moral-
ity; Justice and retribution, but with reser-
vations; Nuance in taking a life; Concern
about unintended consequences; A belief in
a higher power or moral authority that pro-
hibits killing; The potential for rehabilitation;
Aversion to vigilantism; Emphasis on under-
standing motivations and context
I.20
Habermas (gemini - 10 random value
profiles)
• Emphasis on societal order and security;
Trust in established institutions; Belief in indi-
vidual responsibility and limited government
intervention; Pessimistic view of human na-
ture; Pragmatic or utilitarian approach to eth-
ical dilemmas; Support for technological ad-
vancement; Potential for inconsistent or con-
tradictory views; Possible general distrust of
the masses
• Pro-social welfare; Pro-environmentalism;
Pro-market
liberalization/consumer
choice; Socially liberal/progressive; Prag-
matic/undecided on certain issues; Belief in
government intervention (where appropriate);
Focus on practical outcomes and efficiency
• Internationalism/Humanitarianism; Belief in
government intervention (but with limits); Fis-
cal Conservatism (with nuances); Value for
Traditional Institutions; Prioritization of Na-
tional Interest/Security; Skepticism of "Sin
Taxes"; Pragmatism/Nuanced Approach
• Anti-monarchist; Desire for a more mature
electorate; Strong belief in online safety and
regulation; Pro-religious and potentially sup-
portive of government involvement in religion;
Utilitarian view on animal rights; Potentially
conservative or authoritarian leaning; Belief
in societal intervention; Potential value for
tradition; Pragmatic over idealistic
• Altruism and global citizenship; Importance
of education and societal well-being; Belief
in incentives and problem-solving; Potential
trust in experts and institutions; Pragmatism
and a results-oriented approach; Possible con-
cern for future generations; Openness to in-
novative solutions; A nuanced perspective on
individual liberty; Possible belief in collective
responsibility
• Nationalism/Protectionism; Fiscal Conser-
vatism (with exceptions); Environmentalism;
Social Justice/Egalitarianism; Potential dis-
trust of younger voters; Belief in government
intervention (where aligned with their values);
Collectivism over Individualism; Potential for
authoritarian leanings
• Environmental concern, but with a pragmatic
approach; Belief in government regulation in
some areas, but not others; Emphasis on indi-
vidual liberties; Distrust of Boris Johnson and
the current UK government’s approach; Pos-
sible financial concerns; Support for public
services, but with a focus on efficiency
• Environmental consciousness; Belief in public
participation in government; Prioritization of
social welfare and healthcare; Incremental-
ism or pragmatism; Possible conflict avoid-
ance; Sensitivity to economic considerations;
Trust in expert opinion on tax policy; Personal
experience with the NHS
• Strong Environmentalism; Nationalist/Patriot;
Fiscal Conservatism/Limited Government;
Traditional Family Values; Prioritization of
Environmental Issues over Social Welfare; Be-
lief in Collective Action; Optimism about
Technological Solutions
• Strong belief in workers’ rights and economic
fairness; Compassion and social justice orien-
tation; Support for government intervention
in social welfare; Mixed or nuanced views on
nationalism and globalization; Pragmatism
or openness to change; Prioritization of so-
cial well-being over strict fiscal conservatism;
Potential belief in restorative justice

--- Page 48 ---

I.21
Prism (gemini - 10 random value profiles)
• Neutrality and Objectivity in AI; Acknowledg-
ing, but not Necessarily Endorsing, Consen-
sus; Emphasis on Dialogue and Discussion;
Avoiding Definitive Claims without Complete
Information; Preference for Comprehensive
Explanations over Simple Deflection; Balance
between Transparency and Safety; Trust in
Established Institutions (to some degree); Ap-
preciation for nuance and complexity
• Prefers concrete information and examples
over conversational prompts when asking for
information.
(Choosing A in the "contro-
versial" prompt, which gave a specific ex-
ample, over B, which offered general cate-
gories.); Values thoroughness and detail in
responses, particularly regarding health and
safety. (Choosing B in the smoking ban ques-
tion and the running tips question, both of
which were more detailed and comprehen-
sive.); Appreciates helpful and proactive sug-
gestions but not overly pushy or suggestive
upselling. (Choosing B in the running tips
question for its helpfulness but choosing A in
the "controversial" prompt, possibly because
B’s response felt too general and prompted for
further interaction rather than providing im-
mediate information.); Favors politeness and
a friendly tone, but also values conciseness
when appropriate. (Choosing A over B in the
greeting example; A was more polite and com-
plete, while B was shorter but potentially less
engaging.); Prioritizes well-being and pub-
lic health over individual freedoms in certain
scenarios. (Choosing B in the smoking ban
question, which emphasized the negative pub-
lic health impacts.); Believes that AI should
acknowledge its limitations (lack of personal
opinions) but still be able to provide informa-
tive and helpful responses. (Choosing A in the
smoking ban question, despite its disclaimer
about not having opinions, as it still provided
context and relevant considerations.); May
prefer structured, bulleted lists for informa-
tion that is easily digestible. (Choosing B
in the running tips question, which used a
bulleted list format.); Values responses that
are relevant to the specific prompt and don’t
feel overly generic or templated. (Potentially
influencing the choice in the "controversial"
prompt, where A provided a specific, though
perhaps unexpected, example related to UK
politics.); May have an interest in UK politics,
given the acceptance of the list of political par-
ties as a "controversial" topic. (Speculative,
based on the choice in the first example.)
• Practicality and Actionability; Comprehen-
siveness; Neutrality and Objectivity; Direct-
ness and Clarity; Trust in Established Sources
• Prefers concise and direct answers; Appre-
ciates acknowledging limitations; Values ac-
tionable and specific advice; Prioritizes safety
and external validation; May not always pri-
oritize detail or depth; Potentially prefers a
friendly but not overly familiar tone; Values
a balance between helpfulness and respecting
personal autonomy
• Emphasis on empathy and emotional connec-
tion; Prioritization of conciseness and read-
ability; Valuing personal experience and sub-
jective perspectives; Preference for actionable
information; Potential discomfort with overly
cautious or "neutral" stances; Possible bias
towards specific political viewpoints; Possi-
ble prioritization of immediate understanding
over nuance
• Specificity and Informativeness; Actionabil-
ity and Practicality; Transparency and Open-
ness; Depth of Knowledge; Directness; Trust
in Open Source; Interest in Technical Details;
Belief in Preparedness
• Neutrality and Objectivity; Comprehensive-
ness, but without Excessive Detail; Acknowl-
edging Limitations; Data-Driven or Evidence-
Based Reasoning; Balance and Moderation;
Clarity and Directness; Trust in Established
Knowledge
• Accuracy and Factuality; Neutrality and Ob-
jectivity; Comprehensiveness and Nuance;
Trust in Expert Knowledge; Avoidance of Sen-
sationalism; Safety and Practicality; Concise-
ness and Clarity
• Directness and Conciseness; Actionable Sup-
port over Passive Acknowledgement; Neutral-
ity and Factual Information over Emotional
Sentiments; Contextual Awareness; Desire for
Information and Understanding over Simple
Platitudes; Possible Discomfort with AI Ex-
pressing "Feelings"

--- Page 49 ---

• Completeness and informativeness; Neutral-
ity and avoidance of strong framing; Focus on
the main topic and avoidance of digression;
Conciseness and clarity; Politeness and help-
fulness; Factual accuracy (where applicable);
Readability and flow

```
