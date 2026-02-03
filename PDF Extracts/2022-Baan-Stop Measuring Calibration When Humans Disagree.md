---
title: "Stop Measuring Calibration When Humans Disagree - PDF Extract"
source_pdf: "2022-Baan-Stop Measuring Calibration When Humans Disagree.pdf"
pages: 24
extracted_at: "2026-01-24T17:05:09.548082"
---

# PDF Extract: Stop Measuring Calibration When Humans Disagree

**Source PDF:** 2022-Baan-Stop Measuring Calibration When Humans Disagree.pdf
**Total Pages:** 24

---

## Content

```
--- Page 1 ---

Stop Measuring Calibration When Humans Disagree
Joris Baan1, Wilker Aziz1, Barbara Plank2,3,4, Raquel Fernández1
1University of Amsterdam, 2IT University of Copenhagen, 3MCML Munich, 4LMU Munich
{j.s.baan,w.aziz,raquel.fernandez}@uva.nl, b.plank@lmu.de
Abstract
Calibration is a popular framework to evalu-
ate whether a classiﬁer knows when it does
not know—i.e., its predictive probabilities are
a good indication of how likely a prediction
is to be correct.
Correctness is commonly
estimated against the human majority class.
Recently, calibration to human majority has
been measured on tasks where humans inher-
ently disagree about which class applies. We
show that measuring calibration to human ma-
jority given inherent disagreements is theo-
retically problematic, demonstrate this empir-
ically on the ChaosNLI dataset, and derive
several instance-level measures of calibration
that capture key statistical properties of human
judgements—class frequency, ranking and en-
tropy.1
1
Introduction
Neural text classiﬁers are becoming more powerful
but increasingly difﬁcult to interpret (Rogers et al.,
2020). In response, the demand for transparency
and trust in their predictions is growing (Yin et al.,
2019; Bansal et al., 2019; Bianchi and Hovy, 2021).
One step towards understanding when to trust pre-
dictions is to evaluate whether models know when
they do not know—i.e., whether predictive proba-
bilities are a good indication of how likely a predic-
tion is to be correct—known as calibration. This is
crucial in user-facing and high-stake applications.
Calibration, and particularly the Expected Cali-
bration Error (ECE; Naeini et al., 2015; Guo et al.,
2017), is widely studied in Machine Learning and
Computer Vision (Mena et al., 2021), and is gaining
increased attention in Natural Language Process-
ing (NLP; Desai and Durrett, 2020; Kong et al.,
2020; Jiang et al., 2021; Dan and Roth, 2021).
An important implicit assumption in the widely
used deﬁnition of perfect calibration proposed by
1Code
available
at
https://github.com/jsbaan/
calibration-on-disagreement-data.
Guo et al. (2017) is that predictions are either right
or wrong—in other words, that the true class dis-
tribution, i.e., human judgement distribution, is
deterministic (one-hot). However, for many prob-
lems, while categories exist, their boundaries are
ﬂuid: there exists inherent disagreement about
labels. This means that gold labels are at best
an idealization—as irreconcilable disagreement is
abundant (Plank et al., 2014; Aroyo and Welty,
2015; Jamison and Gurevych, 2015; Palomaki et al.,
2018; Pavlick and Kwiatkowski, 2019). Evidence
for this can be found in various tasks, including
those which involve linguistic and subjective judge-
ments (Akhtar et al., 2020; Basile et al., 2021).
Surprisingly, however, while limitations of calibra-
tion are studied (§2), this fundamental assumption
is ignored.
In this work, we show that popular calibration
metrics—such as ECE—are not applicable to data
with inherent human disagreement (§3). We pro-
pose an alternative, instance-level notion of cal-
ibration based on human uncertainty, and opera-
tionalize it with several measures that capture key
statistics of the human judgement distribution other
than matching the majority vote (§4). Finally, we
verify our theoretical claims with a case study on
the ChaosNLI dataset, and investigate temperature
scaling—a popular post-hoc calibration method—
through the lens of human uncertainty (§5).
2
Background
Data
We have data D = {(xn, yn)}N
n=1 where
xn is an instance (i.e., text or texts) and yn ∈[C]
is a category. For any instance X = x,2 we as-
sume that human annotators draw their labels in-
dependently from the same Categorical distribu-
2We use capital letters for random variables (e.g., X) and
lowercase letters for their assignments (e.g., X = x), [C] is
short for {1, . . . , C}, [a = b] is the Iverson bracket (i.e., it
evaluates to 1 if the predicate a = b is True, 0 otherwise),
and ∆C−1 ⊂RC is the simplex (i.e., set of C-dimensional
vectors whose coordinates are positive and sum to 1).
arXiv:2210.16133v2  [cs.CL]  30 Nov 2022

--- Page 2 ---

tion with class probabilities π(x) ∈∆C−1. That
is, the probability Pr(Y = c|X = x) that a human
should label x an instance of c ∈[C] is πc(x).
For observed x, an estimate of π(x) can be ob-
tained via maximum likelihood estimation (MLE).
This estimate ¯π(x) is the vector whose coordinate
¯πc(x) =
PN
n=1[xn=x][yn=c]
PN
n=1[xn=x]
is the relative frequency
with which x is labeled as c ∈[C]. Oftentimes,
π(x) is assumed to be one-hot (i.e., the task is un-
ambiguous), in such cases, a single human judge-
ment per instance is sufﬁcient for an exact estimate.
Classiﬁcation
A probabilistic classiﬁer approxi-
mates π(x) with a trained parametric function (e.g.,
BERT; Devlin et al., 2019) that maps an input x
to a vector f(x) of class probabilities. After train-
ing, and given an instance x, we typically map the
model’s output f(x) to a single decision ˆy ∈[C].
More often than not, this is the mode of the model
distribution: ˆy = arg maxc fc(x). The correctness
of ˆy is assessed against the observed human ‘gold
standard’ decision y⋆= arg maxc ¯πc(x).
Calibration
A classiﬁer is multi-class calibrated
(Vaicenavicius et al., 2019; Kull et al., 2019) if,
for all instances mapped to the same vector q, the
relative frequency with which c is correct (assessed
against the gold standard) is qc for every c:
Pr(Y ⋆= c | f(X)=q) = qc
∀c ∈[C]
(1)
Consider a problem with three classes. A model is
multi-class calibrated if, for all instances mapped to
the same vector, e.g., (0.90, 0.07, 0.03)⊤, predict-
ing the ﬁrst class would result in a correct decision
for 90% of these instances, the second class for 7%,
and the third class for 3%. Estimation of the left-
hand side (LHS) of Eq(1) by counting is difﬁcult
as it requires observing multiple instances mapped
to the same probability vector.
A weaker notion of calibration (popular in NLP;
Desai and Durrett, 2020; Jiang et al., 2021) is con-
ﬁdence calibration (Guo et al., 2017):3
Pr

Y ⋆= ˆY | max(f(X)) = p

= p
(2)
A model is conﬁdence calibrated if, for all instances
mapped to a maximum probability value p (e.g.,
0.9), the most probable class under the model is
correct for 90% of these instances.
3The maximum class probability assigned to a ran-
dom text X is itself a random variable, we denote it by
max(f(X)) := maxc∈[C] fc(X). As for any other random
variable, max(f(X)) = p identiﬁes the set of texts for which
the maximum probability predicted by the model is exactly p.
Expected Calibration Error
is most often used
to measure (conﬁdence) calibration in practice.
Naeini et al. (2015) originally proposed ECE for
binary classiﬁcation and Guo et al. (2017) later
adapted it to a multi-class setting:
ECE =
M
X
m=1
|Bm|
N |acc(Bm) −conf(Bm)|
(3)
ECE estimates the conﬁdence calibration error—
absolute difference between the LHS and the RHS
of Eq(2)—in expectation by discretizing the proba-
bility of the model decision into a ﬁxed number M
of intervals (or bins). Each prediction vector f(x) is
assigned to a bin Bm based on its highest probabil-
ity maxc fc(x). The ECE is the weighted average
of the difference between the average conﬁdence
and accuracy per bin. To obtain zero calibration
error, if 90 out of 100 instances that received a
highest probability between 0.8 and 1.0 are cor-
rectly classiﬁed, the average conﬁdence on those
100 instances must be 0.9.
Several recent studies identify and address prob-
lems with ECE—mostly with its binning scheme
and implicit decision rule (e.g., Kumar et al., 2018;
Nixon et al., 2019; Widmann et al., 2019; Gupta
et al., 2021; Si et al., 2022). Instead, in this work
we identify a fundamental problem in the deﬁnition
of perfect calibration when applying it to setups
where there exists no real gold label.
3
Calibration & Disagreement Pathology
It is common practice to handle human disagree-
ment with majority voting or other aggregation
methods (Dawid and Skene, 1979; Artstein and
Poesio, 2008; Paun et al., 2022). Aggregate (gold)
labels are then used to evaluate a classiﬁer’s ac-
curacy. We now illustrate the problem this poses
when measuring calibration.
Desideratum: Any classiﬁer g that, given an in-
stance x, predicts the human judgement distribu-
tion g(x) = π(x) should be perfectly calibrated.
Consider the oracle classiﬁer that has access to the
MLE ¯π(x) of π(x) for any instance x in a valida-
tion set. For each x, the oracle is able to predict
the human labeling uncertainty π(x). This esti-
mate is unbiased and becomes more precise the
more judgements we have access to. By deﬁnition,
when human majority voting is used, this classi-
ﬁer achieves perfect accuracy—its highest conﬁ-
dence prediction always matches the gold standard.

--- Page 3 ---

However, according to ECE, the oracle classiﬁer is
miscalibrated (this is true for other deﬁnitions of
calibration to accuracy, including multi-class and
classwise). Recall that the calibration error is the
absolute difference between accuracy and average
conﬁdence per bin. The accuracy of the oracle clas-
siﬁer is always 1. On data where humans disagree,
the average conﬁdence will be lower than 1.
This mismatch results in high calibration error
(as demonstrated in §5) and exposes a problem with
using ECE to measure calibration on disagreement
data. An important takeaway is that, even if we can
train a classiﬁer that perfectly models the human
judgement distribution, this classiﬁer would still be
severely miscalibrated. To achieve perfect calibra-
tion, its probabilities must drift towards an unfaith-
ful representation of human conﬁdence. Therefore,
we argue that human majority accuracy is a bad
estimate of correctness to calibrate against.
4
Calibration to Human Uncertainty
To get a faithful probabilistic classiﬁer, we expect
it to predict the uncertainty the human population
exhibits on any given x. Notions of calibration to
accuracy (e.g., multi-class, classwise, conﬁdence)
are deﬁned marginally (i.e., for instances grouped
by a property of model predictions such as their
probability). Instead, we argue for a direct assess-
ment of calibration at the instance level. Given x,
perfect calibration to human uncertainty requires:
Pr(Y = c | X = x) = fc(x)
∀c ∈[C]
(4)
This is our desideratum of §3 re-expressed for a
practical classiﬁer f(·). In words, a model is cal-
ibrated for x if it predicts probability fc(x) equal
to the probability Pr(Y = c | X = x) with which
humans label x as c. With multiple human judge-
ments (whether or not they disagree), the LHS can
be estimated by ¯π(x)—the relative frequency of
the observed labels. Assessing the degree to which
Eq(4) holds in expectation across instances gives
us a tool to criticize classiﬁers in terms of their
overall calibration to human uncertainty in a given
task. This is appealing because we can assess the
trustworthiness both globally (overall calibration)
as well as on individual predictions.
Distance Measures
To operationalize our notion
of human calibration, we propose three distance
measures—each capturing a different key statistic.
First, Human Entropy Calibration Error:
EntCE(x) = H(f(x)) −H(¯π(x))
(5)
This captures the alignment between disagreement
among humans and a model’s indecisiveness. It is
sensitive to average confusion, but not to class rank-
ing. Second, Human Ranking Calibration Score:
RankCS = 1
N
N
X
n=1
[argsort(f(xn)) =
argsort(¯π(xn))]
(6)
RankCS is a global measure that can be viewed as
a stricter alternative to majority vote accuracy. It is
sensitive to class ranking but not to magnitude of
probability, complementing entropy calibration.4
Third, Human Distribution Calibration Error—the
strictest and most informative measure of the three:
DistCE(x) = TVD(f(x), ¯π(x))
(7)
We opt for the popular total variation distance
(TVD) between the predictive distribution and the
human judgement distribution.5 One could com-
pare other statistics of interest, and we encourage
the community to do so. For example, a more ﬁne-
grained classwise analysis (see Appendix B).
Advantages
First, unlike ECE, human calibra-
tion naturally handles disagreement data—in fact,
it requires multiple annotations to reliably esti-
mate the human judgement distribution. Second,
DistCE and EntCE measure the calibration of in-
dividual predictions, which is a powerful tool to aid
decision making. Crucially, this avoids the need for
a binning scheme, often criticized in ECE (Nixon
et al., 2019; Gupta et al., 2021). Third, DistCE
ensures full multi-class calibration: there is no im-
plicit decision rule and a classiﬁer’s underlying
statistical model is directly evaluated on its ability
to match the entire human judgement distribution.
Fourth, unlike ECE and its variants, DistCE is a
proper scoring rule, which comes with a range of
desirable properties (Gneiting and Raftery, 2007).
Related Work
Several recent studies on soft
evaluation evaluate or optimize for a quantity simi-
lar to our DistCE. However, we are the ﬁrst to pro-
pose a general notion of calibration in disagreement
4We leave aside specifying a method for handling cases
where two or more classes obtain an equal number of votes,
which makes multiple rankings correct.
5TVD(q, p) = 1/2∥q −p∥1 is convenient for various
reasons: it is a metric (hence, symmetric) and deﬁned for all
discrete distributions (including sparse distributions); being
expressed directly in (absolute difference in) probability, it is
dimensionless (or unitless) and bounded between 0 and 1; it
quantiﬁes the maximum discrepancy in probability across the
event space. For a more technical discussion, see Appendix E.

--- Page 4 ---

(a) DistCE: Vanilla
(b) DistCE: Temp Scaling
(c) ECE: Vanilla
(d) ECE: Temp Scaling
Figure 1: Left: Distribution over instance-level calibration errors (DistCE). While temperature scaling (TS) causes
fewer severely miscalibrated instances—illustrated by the right tail of the distribution retracting from (a) to (b)—
there are also fewer instances that are perfectly calibrated, see drop of ﬁrst bar in (b). Right: Reliability Diagrams
indicate that TS improves ECE enormously, because the bars in (d) move towards the diagonal.
settings. Nie et al. (2020) introduce ChaosNLI
(see §5) and report the Kullback–Leibler (KL) and
Jensen–Shannon (JS) divergences from estimates
of the human judgement distributions. Follow-up
work explores decreasing this divergence. For ex-
ample, by ﬁne-tuning on them directly (Meissner
et al., 2021; Zhang et al., 2021); using Bayesian-
inspired methods (Zhou et al., 2022); methods pop-
ularized to bring down ECE, such as temperature
scaling or label smoothing (Zhang et al., 2021;
Wang et al., 2022); or framing the task as regression
(Chen et al., 2020).
We show that the human majority class is not a
meaningful statistic to calibrate against in disagree-
ment settings. In §5, we empirically demonstrate
that human calibration is more faithful, and a use-
ful tool to gain insights into calibration errors.
5
Case Study
5.1
Experimental Setup
Dataset
We use the ChaosNLI dataset (Nie et al.,
2020) as case study. It contains English natural
language inference instances selected from the de-
velopment sets of SNLI (Bowman et al., 2015),
MNLI (Williams et al., 2018) and AbductiveNLI
(Bhagavatula et al., 2020) for having a borderline
annotator agreement, i.e., at most 3 out of 5 human
votes for the same class. ChaosNLI collects an
additional 100 independent annotations for each of
the roughly 1,500 instances per dataset, resulting
in T = 100 human votes distributed over C = 3
classes per premise-hypothesis pair for a total of
N = 4, 645 instances. The dataset was collected
very carefully and with strict annotation guidelines.
This ensures that disagreement cannot easily be dis-
carded as noise (Pavlick and Kwiatkowski, 2019;
Nie et al., 2020). The task description and exam-
ples can be found in Appendix A.
Method
We ﬁne-tune RoBERTa (Liu et al., 2019)
on SNLI following the standard procedure de-
scribed by Desai and Durrett (2020). We evalu-
ate on the ChaosNLI-SNLI split. To investigate
the value of human calibration, we inspect Wang
et al. (2022)’s claim that ECE is a good alternative
to measuring divergence to the human judgement
distribution—and that temperature scaling (TS;
Guo et al., 2017) is a suitable calibration method
to do so. We discuss temperature scaling and how
we choose a temperature in Appendix C.
5.2
Results
Table 1 shows accuracy, ECE,6 RankCS, and sum-
mary statistics of the instance-level EntCE and
DistCE metrics for RoBERTa, temperature scaled
RoBERTa-TS and the oracle classiﬁer.
Oracle is miscalibrated
Indeed, the oracle clas-
siﬁer is severely miscalibrated according to ECE—
even more so than RoBERTa (0.25 vs 0.14), demon-
strating the problem we highlight in §3. Instead,
on all our human calibration metrics, the oracle is
perfectly calibrated.
Inspecting Error Distributions
Applying TS to
RoBERTa results in a sharp decrease in ECE (from
0.14 to 0.03). The reliability diagrams7 in Fig-
ures 1c and 1d conﬁrm this, suggesting that TS
successfully calibrates probability values.
However, TS only causes a very small change
in mean DistCE (from 0.26 to 0.22). Though the
practical signiﬁcance of this shift might not be im-
mediately obvious (that is also true for other met-
rics, such as ECE), human calibration allows us to
inspect how errors are distributed across instances.
6We observe a similar trend for classwise-ECE, a popular
improvement to standard ECE, in Appendix D.
7A reliability diagram (DeGroot and Fienberg, 1983;
Naeini et al., 2015) visualizes ECE by plotting accuracy
against conﬁdence (intervals). As bars approach the diagonal,
ECE converges to 0.

--- Page 5 ---

RoBERTa
RoBERTa-TS
Oracle
Acc ↑
0.74±0.01
0.74±0.01
1.00
ECE ↓
0.14±0.01
0.03±0.01
0.25
RankCS ↑
0.62±0.01
0.62±0.01
1.00
E[|EntCE|] ↓
0.30±0.02
0.21±0.02
0.00
E[DistCE] ↓
0.26±0.00
0.22±0.00
0.00
Table 1:
Accuracy & ECE versus our RankCS and
summary (mean) of instance-level |EntCE| & DistCE
on ChaosNLI-SNLI. Results shown over 3 random
seeds.
Figure 2: DistCE error distributions for two “as-good-
as-it-realistically-gets”-classiﬁers and two RoBERTas
(vanilla and TS). There are big differences between but
not within groups.
This is an important tool to gain more insight into
the effects of a method such as TS on calibration.
The global DistCE error distributions in Fig-
ure 1a and 1b reveal that perfectly-calibrated in-
stances are sacriﬁced to reduce poorly-calibrated
instances. This corroborates our intuition that TS
artiﬁcially compresses the predicted probability
range, which, arguably is not desirable. For more
extensive and ﬁne-grained analyses, including out-
of-distribution evaluation on the ChaosNLI-MNLI
set, see Appendix B.
How Good is Good?
A naturally arising ques-
tion is how good the shape of a DistCE error
distribution is. To answer this, we need a target:
what does the error distribution of a “as-good-as-
it-realistically-gets”-classiﬁer look like?
To approximate such a classiﬁer, for each
premise-hypothesis pair, we sub-sample 20 votes
and use them to construct a higher-variance MLE of
the underlying human judgement distribution π(x).
We construct two such classiﬁers (H1 and H2) and
plot their DistCE distribution alongside RoBERTa
and RoBERTa-TS in Figure 2. We evaluate the
classiﬁers against the 100 available annotations.
As expected, we barely observe any difference
between the two sub-sampled human classiﬁers.
However, there is a massive difference between
the RoBERTa-based and human-based classiﬁers—
with RoBERTas stretching to much higher instance
level calibration errors (x-axis) than humans—
thereby providing a sense of scale. To quantify
these differences, we compute KL-divergences be-
tween DistCE error distributions. We opt for KL-
divergence because it is asymmetric; weighting
differences in bins that are not probable under the
human model less than those that are. We also
report TVD.
Table 2 shows that KL divergences from
RoBERTa or RoBERTa-TS to an ideal clas-
siﬁer’s error distribution are 150-170x bigger
(0.611 and 0.688) compared to the control group
(one ideal classiﬁer to another; 0.004).
Even
though RoBERTa-TS shows slightly reduced KL-
divergence compared to the vanilla model, it is
nowhere near an ideal classiﬁer, and it is unclear
whether the observed reduction in KL translates to
a meaningful or practical difference, i.e., something
a practitioner would care about.
DistCE error distribution
KL(H1, ·) TVD(H1, ·)
H2
0.004
0.022
RoBERTa
0.688
0.500
RoBERTa-TS
0.611
0.454
Table 2: Quantifying divergence between DistCE error
distributions for human sub-populations (H1 and H2)
and neural classiﬁers (RoBERTa and RoBERTa-TS).
6
Conclusion
We demonstrate a fundamental problem with mea-
suring calibration to the human majority vote in
settings with inherent disagreement in human la-
bels. We propose an alternative, instance-level
notion based on the full human judgement distri-
bution and operationalize this notion with three
metrics. We study temperature scaling RoBERTa
on the ChaosNLI dataset using these metrics and
conclude that they—and crucially, the ability to in-
spect them in distribution—provide a more robust
and faithful lens to analyze classiﬁer calibration in
disagreement settings.
Human uncertainty can be used to evaluate many
other calibration techniques—we only performed a
preliminary analysis for temperature scaling—and
we encourage the community to look into those, in

--- Page 6 ---

addition to exploring other datasets with inherent
disagreements.
Limitations
A reliable estimate of the human judgement dis-
tribution is an important requirement for human
calibration. For the ChaosNLI dataset, the relia-
bility is endorsed by the large number of annota-
tions per instance and strict quality control (Nie
et al., 2020). Most datasets do not provide this. We
believe, however, that the advantages of collect-
ing additional annotation outweigh its cost, since,
without it, datasets are likely to under-represent
human disagreement. We therefore advocate fu-
ture datasets to include multiple annotations per in-
stance (at least for a small test set), as recently also
advocated by, e.g., Prabhakaran et al. (2021), and a
better understanding of how many annotations are
required for good estimates of human uncertainty.
An important challenge is to distinguish inherent
disagreement from noise, for example due to spam-
mers, which negatively affects data quality (Raykar
and Yu, 2012; Aroyo et al., 2019; Klie et al., 2022).
Another limitation is that uncertainty estimates
from one population cannot be said to be univer-
sally correct. The notion that, given an instance,
one unique human distribution governs all anno-
tators is a simpliﬁcation. Even a single collection
of votes from one experiment might contain sub-
populations, in which case the marginal distribution
is not representative of individual components.
Acknowledgements
We thank the anonymous reviewers and meta-
reviewer for their invaluable feedback.
This
project has received funding by the ELLIS Am-
sterdam Unit. BP is supported by the Indepen-
dent Research Fund Denmark (DFF) Sapere Aude
grant 9063-00077B and ERC Consolidator Grant
101043235. RF is supported by ERC Consolidator
Grant 819455.
References
Sohail Akhtar, Valerio Basile, and Viviana Patti. 2020.
Modeling annotator perspective and polarized opin-
ions to improve hate speech detection. Proceedings
of the AAAI Conference on Human Computation and
Crowdsourcing, 8(1):151–154.
Lora Aroyo, Lucas Dixon, Nithum Thain, Olivia Red-
ﬁeld, and Rachel Rosen. 2019. Crowdsourcing sub-
jective tasks: The case study of understanding tox-
icity in online discussions.
In Companion Pro-
ceedings of The 2019 World Wide Web Conference,
WWW ’19, page 1100–1105, New York, NY, USA.
Association for Computing Machinery.
Lora Aroyo and Chris Welty. 2015.
Truth is a lie:
Crowd truth and the seven myths of human annota-
tion. AI Magazine, 36(1):15–24.
Ron Artstein and Massimo Poesio. 2008. Inter-coder
agreement for computational linguistics. Computa-
tional linguistics, 34(4):555–596.
Gagan Bansal, Besmira Nushi, Ece Kamar, Walter S
Lasecki, Daniel S Weld, and Eric Horvitz. 2019.
Beyond accuracy: The role of mental models in
human-ai team performance.
In Proceedings of
the AAAI Conference on Human Computation and
Crowdsourcing, volume 7, pages 2–11.
Valerio Basile, Michael Fell, Tommaso Fornaciari,
Dirk Hovy, Silviu Paun, Barbara Plank, Massimo
Poesio, Alexandra Uma, et al. 2021. We need to con-
sider disagreement in evaluation. In 1st Workshop
on Benchmarking: Past, Present and Future, pages
15–21. Association for Computational Linguistics.
Chandra Bhagavatula, Ronan Le Bras, Chaitanya
Malaviya, Keisuke Sakaguchi, Ari Holtzman, Han-
nah Rashkin, Doug Downey, Wen tau Yih, and Yejin
Choi. 2020. Abductive commonsense reasoning. In
International Conference on Learning Representa-
tions.
Federico Bianchi and Dirk Hovy. 2021. On the gap be-
tween adoption and understanding in NLP. In Find-
ings of the Association for Computational Linguis-
tics: ACL-IJCNLP 2021, pages 3895–3901, Online.
Association for Computational Linguistics.
Samuel R. Bowman, Gabor Angeli, Christopher Potts,
and Christopher D. Manning. 2015. A large anno-
tated corpus for learning natural language inference.
In Proceedings of the 2015 Conference on Empiri-
cal Methods in Natural Language Processing, pages
632–642, Lisbon, Portugal. Association for Compu-
tational Linguistics.
Tongfei Chen, Zhengping Jiang, Adam Poliak, Keisuke
Sakaguchi, and Benjamin Van Durme. 2020.
Un-
certain natural language inference. In Proceedings
of the 58th Annual Meeting of the Association for
Computational Linguistics, pages 8772–8779, On-
line. Association for Computational Linguistics.
Soham Dan and Dan Roth. 2021.
On the effects of
transformer size on in- and out-of-domain calibra-
tion. In Findings of the Association for Computa-
tional Linguistics: EMNLP 2021, pages 2096–2101,
Punta Cana, Dominican Republic. Association for
Computational Linguistics.
Alexander Philip Dawid and Allan M Skene. 1979.
Maximum likelihood estimation of observer error-
rates using the em algorithm. Journal of the Royal
Statistical Society:
Series C (Applied Statistics),
28(1):20–28.

--- Page 7 ---

Morris H. DeGroot and Stephen E. Fienberg. 1983.
The comparison and evaluation of forecasters. Jour-
nal of the Royal Statistical Society. Series D (The
Statistician), 32(1/2):12–22.
Shrey Desai and Greg Durrett. 2020.
Calibration of
pre-trained transformers. In Proceedings of the 2020
Conference on Empirical Methods in Natural Lan-
guage Processing (EMNLP), pages 295–302, Online.
Association for Computational Linguistics.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019.
BERT: Pre-training of
deep bidirectional transformers for language under-
standing.
In Proceedings of the 2019 Conference
of the North American Chapter of the Association
for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers),
pages 4171–4186, Minneapolis, Minnesota. Associ-
ation for Computational Linguistics.
Luc Devroye and Gábor Lugosi. 2001. Combinatorial
methods in density estimation. Springer Science &
Business Media.
Tilmann Gneiting and Adrian E Raftery. 2007. Strictly
proper scoring rules, prediction, and estimation.
Journal of the American statistical Association,
102(477):359–378.
Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q.
Weinberger. 2017.
On calibration of modern neu-
ral networks.
In Proceedings of the 34th Interna-
tional Conference on Machine Learning - Volume 70,
ICML’17, page 1321–1330. JMLR.org.
Kartik Gupta, Amir Rahimi, Thalaiyasingam Ajan-
than, Thomas Mensink, Cristian Sminchisescu, and
Richard Hartley. 2021.
Calibration of neural net-
works using splines. In International Conference on
Learning Representations.
Emily Jamison and Iryna Gurevych. 2015. Noise or ad-
ditional information? Leveraging crowdsource an-
notation item agreement for natural language tasks.
In Proceedings of the 2015 Conference on Empiri-
cal Methods in Natural Language Processing, pages
291–297, Lisbon, Portugal. Association for Compu-
tational Linguistics.
Zhengbao Jiang, Jun Araki, Haibo Ding, and Graham
Neubig. 2021.
How Can We Know When Lan-
guage Models Know? On the Calibration of Lan-
guage Models for Question Answering.
Transac-
tions of the Association for Computational Linguis-
tics, 9:962–977.
Jan-Christoph
Klie,
Bonnie
Webber,
and
Iryna
Gurevych. 2022. Annotation Error Detection: An-
alyzing the Past and Present for a More Coherent
Future. Computational Linguistics, pages 1–42.
Lingkai Kong, Haoming Jiang, Yuchen Zhuang, Jie
Lyu, Tuo Zhao, and Chao Zhang. 2020.
Cali-
brated language model ﬁne-tuning for in- and out-of-
distribution data. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing (EMNLP), pages 1326–1340, Online. As-
sociation for Computational Linguistics.
Meelis Kull, Miquel Perelló-Nieto, Markus Kängsepp,
Telmo de Menezes e Silva Filho, Hao Song, and
Peter A. Flach. 2019.
Beyond temperature scal-
ing: Obtaining well-calibrated multi-class probabil-
ities with dirichlet calibration. In NeurIPS, pages
12295–12305.
Aviral Kumar, Sunita Sarawagi, and Ujjwal Jain. 2018.
Trainable calibration measures for neural networks
from kernel mean embeddings.
In Proceedings
of the 35th International Conference on Machine
Learning, volume 80 of Proceedings of Machine
Learning Research, pages 2805–2814. PMLR.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Man-
dar Joshi, Danqi Chen, Omer Levy, Mike Lewis,
Luke Zettlemoyer, and Veselin Stoyanov. 2019.
RoBERTa: A robustly optimized BERT pretraining
approach. arXiv preprint arXiv:1907.11692.
Johannes Mario Meissner, Napat Thumwanit, Saku
Sugawara, and Akiko Aizawa. 2021.
Embracing
ambiguity: Shifting the training target of NLI mod-
els. In Proceedings of the 59th Annual Meeting of
the Association for Computational Linguistics and
the 11th International Joint Conference on Natu-
ral Language Processing (Volume 2: Short Papers),
pages 862–869, Online. Association for Computa-
tional Linguistics.
José Mena, Oriol Pujol, and Jordi Vitrià. 2021.
A
Survey on Uncertainty Estimation in Deep Learning
Classiﬁcation Systems from a Bayesian Perspective.
ACM Comput. Surv., 54(9).
Mahdi Pakdaman Naeini, Gregory F. Cooper, and Mi-
los Hauskrecht. 2015.
Obtaining Well Calibrated
Probabilities Using Bayesian Binning. In Proceed-
ings of the Twenty-Ninth AAAI Conference on Artiﬁ-
cial Intelligence, AAAI’15, page 2901–2907. AAAI
Press.
Yixin Nie, Xiang Zhou, and Mohit Bansal. 2020. What
can we learn from collective human opinions on nat-
ural language inference data? In Proceedings of the
2020 Conference on Empirical Methods in Natural
Language Processing (EMNLP), pages 9131–9143,
Online. Association for Computational Linguistics.
Jeremy Nixon, Michael W. Dusenberry, Linchuan
Zhang, Ghassen Jerfel, and Dustin Tran. 2019. Mea-
suring calibration in deep learning. In Proceedings
of the IEEE/CVF Conference on Computer Vision
and Pattern Recognition (CVPR) Workshops.
Jennimaria Palomaki, Olivia Rhinehart, and Michael
Tseng. 2018. A case for a range of acceptable anno-
tations. In SAD/CrowdBias@ HCOMP, pages 19–
31.
Silviu Paun, Ron Artstein, and Massimo Poesio. 2022.
Statistical methods for annotation analysis.
Syn-
thesis Lectures on Human Language Technologies,
15(1):1–217.

--- Page 8 ---

Ellie Pavlick and Tom Kwiatkowski. 2019. Inherent
disagreements in human textual inferences. Transac-
tions of the Association for Computational Linguis-
tics, 7:677–694.
Barbara Plank, Dirk Hovy, and Anders Søgaard. 2014.
Linguistically debatable or just plain wrong? In Pro-
ceedings of the 52nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 2: Short
Papers), pages 507–511.
Vinodkumar Prabhakaran, Aida Mostafazadeh Davani,
and Mark Diaz. 2021. On releasing annotator-level
labels and information in datasets. In Proceedings
of The Joint 15th Linguistic Annotation Workshop
(LAW) and 3rd Designing Meaning Representations
(DMR) Workshop, pages 133–138, Punta Cana, Do-
minican Republic. Association for Computational
Linguistics.
Vikas C. Raykar and Shipeng Yu. 2012. Eliminating
spammers and ranking annotators for crowdsourced
labeling tasks. J. Mach. Learn. Res., 13:491–518.
Anna Rogers, Olga Kovaleva, and Anna Rumshisky.
2020.
A primer in BERTology: What we know
about how BERT works. Transactions of the Associ-
ation for Computational Linguistics, 8:842–866.
Chenglei Si, Chen Zhao, Sewon Min, and Jordan Boyd-
Graber. 2022. Revisiting calibration for question an-
swering. arXiv preprint arXiv:2205.12507.
Juozas Vaicenavicius, David Widmann, Carl Ander-
sson, Fredrik Lindsten, Jacob Roll, and Thomas
Schön. 2019. Evaluating model calibration in clas-
siﬁcation.
In The 22nd International Conference
on Artiﬁcial Intelligence and Statistics, pages 3459–
3467. PMLR.
Yuxia Wang, Minghan Wang, Yimeng Chen, Shimin
Tao, Jiaxin Guo, Chang Su, Min Zhang, and Hao
Yang. 2022. Capture human disagreement distribu-
tions by calibrated networks for natural language in-
ference. In Findings of the Association for Compu-
tational Linguistics: ACL 2022, pages 1524–1535,
Dublin, Ireland. Association for Computational Lin-
guistics.
David
Widmann,
Fredrik
Lindsten,
and
Dave
Zachariah. 2019.
Calibration tests in multi-class
classiﬁcation: A unifying framework. Advances in
Neural Information Processing Systems, 32.
Adina Williams, Nikita Nangia, and Samuel Bowman.
2018. A broad-coverage challenge corpus for sen-
tence understanding through inference. In Proceed-
ings of the 2018 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies, Volume
1 (Long Papers), pages 1112–1122. Association for
Computational Linguistics.
Ming Yin, Jennifer Wortman Vaughan, and Hanna Wal-
lach. 2019. Understanding the effect of accuracy on
trust in machine learning models. In Proceedings of
the 2019 CHI conference on human factors in com-
puting systems, pages 1–12.
Shujian Zhang, Chengyue Gong, and Eunsol Choi.
2021. Learning with different amounts of annota-
tion: From zero to many labels. In Proceedings of
the 2021 Conference on Empirical Methods in Natu-
ral Language Processing, pages 7620–7632, Online
and Punta Cana, Dominican Republic. Association
for Computational Linguistics.
Xiang Zhou, Yixin Nie, and Mohit Bansal. 2022. Dis-
tributed NLI: Learning to predict human opinion dis-
tributions for language reasoning.
In Findings of
the Association for Computational Linguistics: ACL
2022, pages 972–987, Dublin, Ireland. Association
for Computational Linguistics.

--- Page 9 ---

Appendix
A
ChaosNLI
Table 3 and Table 4 show examples with very low
or very high agreement. The task description pro-
vided by Nie et al. (2020) is in Figure 3.8
Figure 3: The task description for natural language in-
ference by Nie et al. (2020) used to collect ChaosNLI-
SNLI and ChaosNLI-MNLI.
B
Additional Analyses
This section provides additional analyses and ﬁg-
ures. Each ﬁgure shows a comparison between
model predictions and human predictions using the
measures we propose in §4. We use three different
views to compare statistics of human judgements
to statistics of model predictions.9
The ﬁrst view shows two marginal or dataset-
level histograms: one of a human statistic and one
of a model statistic, e.g., entropy. This view is
useful to compare the global distribution over an
instance-level statistic between human judgements
and model predictions (Figure 4 and 5).
The second view shows one histogram of the
conditional instance-level error between a model
and human statistic, e.g., entropy (Figure 8 and 9).
This is interesting for diagnosing a classiﬁer’s un-
der or over conﬁdence. Instances centered around
zero have zero error, instances in the positive range
exhibit over-conﬁdence, and instances in the nega-
tive range under-conﬁdence.
The third view is similar to the previous, (it is
also conditional, e.g., it compares an instance-level
statistic between humans and a model) but shows
8ChaosNLI can be downloaded at https://www.dropbox.
com/s/h4j7dqszmpt2679/chaosNLI_v1.0.zip.
9Note that these views do not apply to the DistCE (row
3 column 1) and reliability diagrams (row 4), which will not
change across views.
the absolute errors (Figure 6 and 7). This is useful
to spot general miscalibration, regardless of the di-
rection (i.e., under-conﬁdence vs over-conﬁdence).
In each ﬁgure, the top row shows a histogram of
the predicted probability for class 0 (entailment),
1 (neutral) and 2 (contradiction). The second row
shows predicted probability for the kth highest pre-
dicted probability, i.e., the ﬁrst, second and third
guess from either the model or human distribution
(note that the corresponding classes are not neces-
sarily the same for the model and humans—this
row is informative to compare the magnitude of
the probability for the same rank). The third row
shows the histogram of DistCE (TVD) from §5
(left) and the histogram for EntCE (right). The
fourth row shows conventional reliability diagrams
that visualize ECE, and the number of instances per
bin (note that this is not normally shown—though
we ﬁnd it very insightful).
B.1
Beyond DistCE
Figure 4 shows a vanilla RoBERTa on ChaosNLI-
SNLI. We can see that all histograms are very dif-
ferent between humans and model. It is clear that
the model predictions are drawn from a different
distribution than the human predictions. This sig-
nals bad calibration. Figure 5 shows a temperature
scaled RoBERTa. According to all plots, the pre-
dictions still appear drawn from a different distribu-
tion, even though the ECE drops signiﬁcantly. TS
seems to transform the distributions, but they are
not clearly closer to the human distribution. The
entropy ﬁgure seems to indicate that TS overshoots
to the other end of the spectrum (i.e., from over-
conﬁdence to under-conﬁdence). The TS model
is unable to match the extreme left and right end
of the human certainty spectrum for class 0, 1 and
2, which corroborates our intuition that the proba-
bility range is compressed. Another observation is
that the human distribution rarely put much mass
on the third guess (i.e., the predicted class with
the lowest probability). However, after TS models
actually do so—which is undesirable.
We next compare the histogram of (non abso-
lute) instance-level errors in Figure 8 and 9. TS
brings entropy error median and mean from -.26 to
.12. The TS model therefore overshoots also on the
instance-level (recall this plot is the instance-level
error, unlike the previous marginal ﬁgure we dis-
cussed) and becomes more much more uncertain
than humans are. TS causes less class 0 predictions

--- Page 10 ---

Premise
Hypothesis
Label Distribution
A man running a marathon talks
to his friend
There is a man running.
Entailment: 100, Neutral: 0,
Contradiction: 0
A young girl plays with a neon-
colored Slinky in a crowd of
people on a street lined with
ﬂags.
The girl is ﬁve years old.
Entailment: 0, Neutral: 100,
Contradiction: 0
A well built black man stands
in the subway, listening to head-
phones.
A man with headphones on is
standing in a subway.
Entailment: 100, Neutral: 0,
Contradiction: 0
Table 3: High agreement examples from the ChaosNLI dataset.
Premise
Hypothesis
Label Distribution
The important thing is to realize
that it’s way past time to move
it.
It cannot be moved, now or
ever.
Entailment: 34, Neutral: 32,
Contradiction: 34
An elderly woman crafts a de-
sign on a loom.
The woman is sewing.
Entailment: 35, Neutral: 31,
Contradiction: 34
Number 13 kicks a soccer ball
towards the goal during chil-
dren’s soccer game.
A player passing the ball in a
soccer game.
Entailment: 36, Neutral: 33,
Contradiction: 31
Table 4: Low agreement examples from the ChaosNLI dataset.

--- Page 11 ---

to have 0 error (which is bad). It also narrows the
spread slightly for class 1 and increases errors for
class 3.
We next compare the histogram of absolute er-
rors in Figure 6 and 7. We see that TS reduces error
tail of class 0, but also reduces instances with 0 er-
ror (similar trend as discussed in §B about DistCE).
Similarly for class 2 and 3, and entropy: it seem-
ingly reduces the mean and median by cutting off
the tail. Finally, the human rank calibration error
(RCE) shown in the title of each ﬁgure, shoes that
models are not good at matching the human rank
at all—as expected, much worse than matching the
majority vote.
In general, it appears that the median and
mean error on most metrics go down with TS,
mainly by removing instances from the tail (those
are extremely miscalibrated examples).
How-
ever, they seem to sacriﬁce predictions that were
well/perfectly aligned with human judgement prob-
abilities. This illustrated by the mode of the error
distributions moving towards the right (meaning
more predictions with a higher error). Arguably,
this is not desirable—and our metrics provide tools
to expose such behaviors.
B.2
Out of Distribution Evaluation
The OOD setting is interesting to evaluate uncer-
tainty estimates, because it is especially important
to have reliable uncertainty estimates for examples
that are especially difﬁcult (e.g., because the classi-
ﬁer has not seen them during training, and might
not reﬂect the learned distribution). In such cases,
it is desirable that a classiﬁer is more uncertain on
such examples. In fact, OOD detection is often
used to evaluate uncertainty estimates, next to or
instead of calibration. Models are often found to
be more badly miscalibrated for OOD datasets (De-
sai and Durrett, 2020), which is an observation we
conﬁrm.
We observe similar trends as in the in-
distribution analysis. The marginal distributions
from Figure 10 to Figure 11 seem to match the
human marginal slightly better than on the in-
distribution dataset. However, inspecting the error
distributions in Figure 14, 15, 12 and 13, we see
that the distributions are transformed somewhat,
but we do not believe that to be evidence that TS
is a good method to improve calibration. The in-
stances are still obviously drawn from a different
distribution.
C
Temperature Scaling
Temperature scaling is a simple method that uses
a single temperature parameter t to scale the out-
put logits of a classiﬁer (Guo et al., 2017). The
standard way to choose a temperature is to perform
a search on a range of possible values for t on a
development set. However, sometimes, the tem-
perature is tuned directly on the test set. This is
commonly referred to as the oracle temperature.
Indeed, we use this method to obtain our tempera-
ture, because we consider it an (unrealistic) upper
bound on what TS can do. For OOD evaluation,
we use the temperature tuned on the ID evaluation.
In our experiments in §5, we found a temperature
of 2.0 to result in the lowest ECE.
D
Classwise-ECE
Classwise-ECE (Nixon et al., 2019) is based on
the notion of classwise-calibration (Vaicenavicius
et al., 2019; Kull et al., 2019). The main difference
with ECE—based on the notion of conﬁdence cali-
bration (§2)—is that it removes the dependency
on a decision rule on top of the classiﬁer, and
computes the calibration separately for each class.
Classwise-ECE, then, is the average calibration
error over classes:
1
K
K
X
k=1
M
X
m=1
|Bmk|
N
|acc(m, k) −conf(m, k))|
(8)
Table D shows a similar trend for classwise-ECE
as for ECE: the oracle classiﬁer is severely miscali-
brated. This conﬁrms our claims that the general
notion of calibration is not suited for data on which
humans inherently disagree about a class—and is
not restricted to Guo et al. (2017) notion of conﬁ-
dence calibration.
RoBERTa
RoBERTa-TS
Oracle
Classwise-ECE
10
5
16
Table 5: Classwise-ECE on ChaosNLI-SNLI in %.
E
Total Variation Distance
The total variation distance TVD(q, p) between
two Categorical distributions with parameters
q, p ∈∆C−1 is deﬁned as:
max
A∈P([C]) |Q(A) −P(A)|
(9a)

--- Page 12 ---

which can also be expressed as
= 1
2
C
X
c=1
|qc −pc|
|
{z
}
=∥q−p∥1
.
(9b)
where [C] is the sample space, P([C]) is the event
space (for generality, we use the powerset of [C],
the set of all subsets of outcomes in the sample
space), A ∈P([C]) is any event in the event
space, Q and P are the probability measures pre-
scribed by each of the Categorical distributions (i.e.,
Q(A) = P
c∈A qa and P(A) = P
c∈A pa). For a
complete technical results with deﬁnitions, proofs,
and various properties see Devroye and Lugosi
(2001, Chapter 5).
Properties.
TVD is deﬁned for any two probabil-
ity vectors, whether dense or sparse. It is a metric
(hence symmetric and minimised only for identical
distributions) and bounded:
TVD(q, p) = TVD(p, q)
(10a)
TVD(q, p) = 0
iff q = p
(10b)
TVD(q, p) ∈[0, 1] .
(10c)
Interpretations.
The identity in Eq(9b), which
expresses TVD in terms of the L1 norm, gives us
a rather practical (linear-time) algorithm to com-
pute it by summing half the absolute difference in
probability for the outcomes in the sample space
[C] of the random variable. This means that TVD
is expressed in units of absolute difference in prob-
ability. That deﬁnition, Eq(9a), also helps interpre-
tation, it shows that TVD quantiﬁes the maximum
discrepancy in probability between the two mea-
sures over their entire event spaces.

--- Page 13 ---

Figure 4: RoBERTa-0 on the ChaosNLI-SNLI dev+test set. Several ﬁgures comparing human uncertainty to
model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This ﬁgure shows the distribution
over instance-based absolute errors between probabilities for each class (top row) or the model vs human kth guess
(i.e., the highest model probability versus the highest human probability on each instance). See Appendix B for
more information.

--- Page 14 ---

Figure 5: RoBERTa-0 with oracle temperature scaling on the ChaosNLI-SNLI dev+test set. Several ﬁgures com-
paring human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the human and model distribution over the probability, entropy or TVD range. Top row shows dis-
tribution over probability magnitudes for class 0, 1 and 2, while the second row shows the distribution for ﬁrst,
second and third guess for the model vs human kth guess (i.e., the highest model probability versus the highest
human probability on each instance). See Appendix B for more information.

--- Page 15 ---

Figure 6: RoBERTa-0 on the ChaosNLI-SNLI dev+test set. Several ﬁgures comparing human uncertainty to
model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This ﬁgure shows the distribution
over instance-based absolute errors between probabilities for each class (top row) or the model vs human kth guess
(i.e., the highest model probability versus the highest human probability on each instance). See Appendix B for
more information.

--- Page 16 ---

Figure 7: RoBERTa-0 with oracle temperature scaling on the ChaosNLI-SNLI dev+test set. Several ﬁgures com-
paring human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the distribution over instance-based absolute errors between probabilities for each class (top row) or
the model vs human kth guess (i.e., the highest model probability versus the highest human probability on each
instance). See Appendix B for more information.

--- Page 17 ---

Figure 8: RoBERTa-0 on the ChaosNLI-SNLI dev+test set. Several ﬁgures comparing human uncertainty to
model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This ﬁgure shows the distribution
over instance-based absolute errors between probabilities for each class (top row) or the model vs human kth guess
(i.e., the highest model probability versus the highest human probability on each instance). See Appendix B for
more information.

--- Page 18 ---

Figure 9: RoBERTa-0 with oracle temperature scaling on the ChaosNLI-SNLI dev+test set. Several ﬁgures com-
paring human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the distribution over instance-based absolute errors between probabilities for each class (top row) or
the model vs human kth guess (i.e., the highest model probability versus the highest human probability on each
instance). See Appendix B for more information.

--- Page 19 ---

Figure 10: RoBERTa-0 with (ID) temperature scaling on the OOD ChaosNLI-MNLI dev+test set. Several ﬁgures
comparing human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the distribution over instance-based absolute errors between probabilities for each class (top row) or
the model vs human kth guess (i.e., the highest model probability versus the highest human probability on each
instance). See Appendix B for more information.

--- Page 20 ---

Figure 11: RoBERTa-0 with (ID) temperature scaling on the OOD ChaosNLI-MNLI dev+test set. Several ﬁgures
comparing human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the human and model distribution over the probability, entropy or TVD range. Top row shows
distribution over probability magnitudes for class 0, 1 and 2, while the second row shows the distribution for ﬁrst,
second and third guess for the model vs human kth guess (i.e., the highest model probability versus the highest
human probability on each instance). See Appendix B for more information.

--- Page 21 ---

Figure 12: RoBERTa-0 with (ID) temperature scaling on the OOD ChaosNLI-MNLI dev+test set. Several ﬁgures
comparing human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the distribution over instance-based absolute errors between probabilities for each class (top row) or
the model vs human kth guess (i.e., the highest model probability versus the highest human probability on each
instance). See Appendix B for more information.

--- Page 22 ---

Figure 13: RoBERTa-0 with oracle temperature scaling on the ChaosNLI-SNLI dev+test set. Several ﬁgures
comparing human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the distribution over instance-based absolute errors between probabilities for each class (top row) or
the model vs human kth guess (i.e., the highest model probability versus the highest human probability on each
instance). See Appendix B for more information.

--- Page 23 ---

Figure 14: RoBERTa-0 with (ID) temperature scaling on the OOD ChaosNLI-MNLI dev+test set. Several ﬁgures
comparing human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the distribution over instance-based absolute errors between probabilities for each class (top row) or
the model vs human kth guess (i.e., the highest model probability versus the highest human probability on each
instance). See Appendix B for more information.

--- Page 24 ---

Figure 15: RoBERTa-0 with (ID) temperature scaling on the OOD ChaosNLI-MNLI dev+test set. Several ﬁgures
comparing human uncertainty to model uncertainty using TVD, conﬁdence, entropy, and reliability diagrams. This
ﬁgure shows the distribution over instance-based absolute errors between probabilities for each class (top row) or
the model vs human kth guess (i.e., the highest model probability versus the highest human probability on each
instance). See Appendix B for more information.

```
