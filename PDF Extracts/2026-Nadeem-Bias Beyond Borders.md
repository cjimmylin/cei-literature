---
title: "2026-Nadeem-Bias Beyond Borders - PDF Extract"
source_pdf: "2026-Nadeem-Bias Beyond Borders.pdf"
pages: 14
extracted_at: "2026-02-07T17:00:46.667427"
---

# PDF Extract: 2026-Nadeem-Bias Beyond Borders

**Source PDF:** 2026-Nadeem-Bias Beyond Borders.pdf
**Total Pages:** 14

---

## Content

```
--- Page 1 ---

Bias Beyond Borders: Political Ideology Evaluation and Steering in
Multilingual LLMs
Afrozah Nadeem1, Agrima2, Mehwish Nasim3, Usman Naseem1*
1School of Computing, Macquarie University, Australia
2Microsoft, USA
3University of Western Australia, Australia
Abstract
Large Language Models (LLMs) increasingly
shape global discourse, making fairness and
ideological neutrality essential for responsi-
ble AI deployment. Despite growing attention
to political bias in LLMs, prior work largely
focuses on high-resource, Western languages
or narrow multilingual settings, leaving cross-
lingual consistency and safe post-hoc mitiga-
tion underexplored. To address this gap, we
present a large-scale multilingual evaluation
of political bias spanning 50 countries and 33
languages.
We introduce a complementary
post-hoc mitigation framework, Cross-Lingual
Alignment Steering (CLAS), designed to aug-
ment existing steering methods by aligning ide-
ological representations across languages and
dynamically regulating intervention strength.
This method aligns latent ideological repre-
sentations induced by political prompts into a
shared ideological subspace, ensuring cross lin-
gual consistency, with the adaptive mechanism
prevents over correction and preserves coher-
ence. Experiments demonstrate substantial bias
reduction along both economic and social axes
with minimal degradation in response quality.
The proposed framework establishes a scalable
and interpretable paradigm for fairness-aware
multilingual LLM governance, balancing ide-
ological neutrality with linguistic and cultural
diversity.
1
Introduction
Large Language Models (LLMs) increasingly fa-
cilitate how people access information, reason
about societal issues, and form political opinions
(Rozado, 2024; Garrett, 2009). As a result, fair-
ness, neutrality, and cross cultural consistency are
central to their responsible deployment (Adewumi
et al., 2024; Eloundou et al., 2025).
However,
multilingual evaluations show that LLMs are not
ideologically neutral: when answering political or
*Corresponding author: usman.naseem@mq.edu.au
moral questions, they exhibit systematic leanings
that vary across languages, depending on the lan-
guage of the prompt (Barkhordar et al., 2024). To
measure such variation in an interpretable man-
ner, prior work has adopted the Political Compass
Test (PCT)1, which decomposes political position-
ing along two orthogonal axes economic (left vs.
right) and social (libertarian vs. authoritarian) and
supports cross-lingual instantiations (Thapa et al.,
2023a; Barkhordar et al., 2024; Nadeem et al.,
2025b). However, existing PCT-based studies fo-
cus on high-resource languages and report aggre-
gated scores, thus severely limiting their scale and
granularity.
To address these gaps of language and cross-
lingual granularity,we conduct a large-scale PCT
evaluation spanning over 50 countries, analyzing
ideological leanings along economic and social
axes while explicitly modeling language as a pri-
mary analytical dimension . Holding political con-
tent constant, we examine how the same ideolog-
ical prompts are expressed across different lan-
guages and national contexts, allowing us to isolate
language-driven variation from culture-conditioned
shifts and globally stable ideological priors en-
coded in the model .
Next, to correct for this idelogical skew in-
stead of relying on naive debiasing which often
leads to over-correction and degradation of coher-
ence, diversity, or factual grounding (Fei et al.,
2023; Smith et al., 2022), drawing inspiration from
semantics-aware activation interventions (Nadeem
et al., 2025c; Siddique et al., 2025), we propose a
steering-based framework for multilingual bias mit-
igation Cross-Lingual Alignment Steering (CLAS).
This framework incorporates uncertainty-adaptive
scaling to prevent over-correction and preserve util-
ity and aligns language-specific stance represen-
tations into a shared ideological subspace before
1https://www.politicalcompass.org/test
arXiv:2601.23001v2  [cs.CL]  2 Feb 2026

--- Page 2 ---

applying intervention. This framework results in a
robust post-hoc mitigation, which addresses a key
failure mode of prior steering approaches, which
implicitly assume ideological directions to be com-
parable across languages, despite inconsistent po-
litical encoding in language-specific latent spaces.
We evaluate CLAS on a 50-country PCT bench-
mark (Helwe et al., 2025), reporting axis-wise out-
comes across economic and social dimensions and
stratifying by language. Our results show that mul-
tilingual political bias is both axis-specific and
representation-misaligned across languages, and
that aligning stance representations prior to steer-
ing enables consistent bias reduction while preserv-
ing linguistic coherence and cultural semantics.Our
contributions are:
• A large-scale PCT evaluation spanning 50
countries, analyzing ideological tendencies
along economic and social axes.
• A post-hoc cross-lingual alignment and steer-
ing framework that balances bias mitigation
with model utility.
• Consistent reductions in ideological skew
across languages, supporting fair and reliable
multilingual LLM governance.
2
Related Work
2.1
Ideological bias evaluation with PCT
The Political Compass Test (PCT) is a widely used
framework for diagnosing ideological bias in LLMs
(Helwe et al., 2025). It decomposes political orien-
tation along two axes: economic (left-right) and so-
cial (libertarian-authoritarian) (Röttger et al., 2024).
Early monolingual studies show that instruction-
tuned models often exhibit progressive or liberal
leaning in English settings (Abbas and Bidin, 2022;
Thapa et al., 2024; Barkhordar et al., 2024). Sub-
sequent multilingual extensions demonstrate that
ideological behavior varies systematically across
languages due to cultural framing, translation ar-
tifacts, and training data composition (Nadeem
et al., 2025a; Hartmann et al., 2023; Schramowski
et al., 2022). Most recently, Helwe et al. (2025)
introduced a large-scale 50-country benchmark, re-
vealing substantial cross-lingual and cross-national
variation in political leanings. While these works
establish the prevalence of multilingual ideological
asymmetries, they largely remain diagnostic and do
not address how such divergences can be mitigated.
Why political bias matters?
Political bias in
LLMs has concrete societal implications, shap-
ing information access, opinion formation, and
social trust (Rozado, 2024). When models system-
atically favor particular ideological frames, they
risk reinforcing dominant viewpoints and marginal-
izing under-represented perspectives, particularly
in multilingual and politically sensitive contexts
(Adewumi et al., 2024). Such effects can influence
civic discourse, media interpretation, and policy
narratives by subtly shaping users’ perceptions of
fairness and truth (Thapa et al., 2023a; Ejaz et al.,
2023; Garrett, 2009). Crucially, cross-lingual in-
consistencies exacerbate global inequities: a model
that appears neutral in English may express polar-
ized or biased stances in lower-resource languages,
reflecting disparities in data coverage and cultural
exposure (Thapa et al., 2023b; Hartmann et al.,
2023).
2.2
Multilingual and cross-lingual fairness in
LLMs
Bias in multilingual models extends beyond politics
to encompass toxicity, stereotyping, and unequal
representation across linguistic communities (Gal-
legos et al., 2024; Shirafuji et al., 2024; Gupta et al.,
2024). Research has shown that fairness proper-
ties measured in English often fail to transfer to
low-resource or culturally distinct languages, ow-
ing to uneven data quality, fine-tuning corpora, and
alignment methods (Jin et al., 2024; Naous et al.,
2025). Several multilingual fairness studies have
proposed diagnostic datasets and bias taxonomies
(Bang et al., 2023), but few have offered cross-
lingual mitigation strategies that explicitly align
ideological tendencies across languages (Kazi et al.,
2025; Kumar et al., 2023).
Our work addresses this gap by proposing a
mitigation mechanism that is both cross-lingual
and axis-aware, harmonizing ideological positions
across languages while retaining cultural and se-
mantic nuance. Post-hoc steering techniques have
been able to adjust model behavior without retrain-
ing (Chen et al., 2025). Siddique et al. (2025);
Nadeem et al. (2025c) demonstrated that direc-
tional steering vectors can reduce political bias by
manipulating latent activation spaces in inference
time, yielding controlled ideological rebalancing.
Complementary work in feature editing and activa-
tion intervention has shown that modifying internal
representations can modulate sentiment, toxicity,
and factual alignment (Bang et al., 2021; Gehman
et al., 2020). However, existing steering methods
are typically monolingual and apply fixed steer-

--- Page 3 ---

ing intensity, which can cause over-correction or
semantic drift, we propose Cross-Lingual Align-
ment Steering to align stance vectors across lan-
guages to dynamically adjust intervention strength
based on model confidence extending steering be-
yond English-centric contexts and toward adaptive,
multilingual fairness (Sundar et al., 2025). While
existing approaches address isolated aspects of mul-
tilingual bias mitigatin either regulating interven-
tion strength through semantics-adaptive methods
(Wang et al., 2024) or diagnosing cross-lingual di-
vergence (Helwe et al., 2025), they remain agnostic
to where ideological representations are encoded
across languages, implicitly assuming a shared la-
tent structure that fails in practice. We identify
representational misalignment as the missing link:
language-specific ideological directions must first
be aligned into a shared subspace before inter-
vention. We introduce a novel framework Cross-
Lingual Alignment Steering (CLAS), which explic-
itly aligns ideological axes across languages prior
to steering, combined with uncertainty-adaptive
scaling to prevent over-correction while preserving
semantic faithfulness and cultural diversity (Chen
et al., 2025). By systematically comparing against
Individual Steering Vectors (ISV) and Steering Vec-
tor Ensembles (SVE) across 50 countries, we es-
tablish a principled framework for cross-lingual
political bias mitigation.
3
Methodology
Our methodology comprises two main components:
large-scale bias evaluation using the Political Com-
pass Test as a standardized tool for ideological
bias across 50 countries, languages, and ideologi-
cal axes; and a mitigation pipeline that integrates
Cross-Lingual Alignment Steering to harmonize
and stabilize ideological responses across multilin-
gual contexts. We extend this evaluation to multi-
lingual setting covering both high and low-resource
languages around more than 33 languages.
3.1
Bias Evaluation
Each statement is presented with a four-level Likert
response set: Strongly Agree, Agree, Disagree,
and Strongly Disagree. For LLM evaluation,
prompts are standardized across all languages,
following the multilingual specification, see Ap-
pendix E. To quantify political stance, we employ
a two-step scoring pipeline. First, we use a classi-
fier to compute confidence scores for each Likert
category, denoted as As, A, D, Ds. A continuous
stance value S ∈[−10, 10] is derived by multi-
plying the dominant label’s confidence by a fixed
polarity weight (±10 for strong responses, ±5 for
moderate responses). This representation captures
both the direction and intensity of the model’s po-
sition. Second, we discretize S into ordinal la-
bels using a symmetric thresholding function g(·),
mapping continuous scores to categorical values
{0, 1, 2, 3}, corresponding to the four Likert re-
sponses. This conversion allows systematic com-
parison across languages and models while main-
taining interpretability.
Finally, stance values across all statements are
aggregated and projected into the two-dimensional
ideological space (Seco, Ssoc). This yields a struc-
tured, language- and model-specific representa-
tion of political alignment, enabling robust cross-
lingual and cross-model comparisons. The analysis
dimensions are: Axis: economic and social bias
independently. Language: linguistic variation in
ideological direction. Nationality: country-level
ideological skew conditioned on localized state-
ments. This multidimensional structure allows one
to examine whether LLMs exhibit consistent ideol-
ogy across languages and nations or adapt stances
based on linguistic and cultural framing.
3.2
Bias Mitigation
We design a steering framework that targets cross-
lingual consistency and uncertainty-aware adapta-
tion. This study presents a unified framework for
mitigating political bias in large language mod-
els through activation-level steering using con-
trastive pairs derived from the PCT statements. The
framework combines multilingual prompt construc-
tion, layer-wise activation analysis, and residual-
stream vector intervention. Effectiveness is evalu-
ated using the Bias Reduction Score (∆Bias) and
a composite Response Quality Metric following
Siddique et al. (2025). Our pipeline consists of
four stages: (1) generating contrastive ideological
pairs along the PCT axes, (2) extracting hidden
activations from selected transformer layers, (3)
deriving directionally consistent steering vectors
using Individual Steering Vectors (ISV), logistic-
regression–based single-layer vectors, and Steer-
ing Vector Ensembles (SVE). To ensure multilin-
gual consistency, we insert an intermediate align-
ment stage Cross-Lingual Alignment Steering ,
which maps language-specific steering vectors into
a shared ideological subspace via an orthogonal

--- Page 4 ---

alignment transformation, harmonizing the seman-
tic direction of mitigation across languages before
injection. This alignment step reduces language-
conditioned stance drift while preserving culturally
grounded semantics and maintaining utility. and
(4) applying activation-level interventions during
decoding to mitigate bias. We extend the multi-
lingual PCT dataset evaluation and mitigation in-
troduced by Nadeem et al. (2025b); Helwe et al.
(2025) to include English, Urdu, and Punjabi, cov-
ering both economic (left,right) and social (libertar-
ian, authoritarian) axes. Each statement was trans-
formed into a semantically divergent contrastive
pair. Sentence embeddings were computed using
sentence-transformers, and pairs with cosine
similarity below τ = 0.15 were retained, ensuring
strong ideological contrast without redundancy.
Steering Vector Computation
For each layer l,
a logistic regression classifier separates ideologi-
cal activations, producing weight vector θ. The
normalized vector vl = θ/∥θ∥represents the bias
direction. Quality scores ql combine classifier ac-
curacy and effect-size separation to identify robust
layers. SVE aggregates ISVs as vSVE = P
l wlvl,
normalized after quality-based weighting. During
generation, hidden states are modified as h(l)(x)′ =
h(l)(x) + αvl, with α controlling steering strength.
ISVs apply to a single layer, while SVEs are in-
jected across all selected layers. Bias reduction is
quantified by ∆Bias = |Biasoriginal| −|Biassteered|,
where positive values indicate successful mitiga-
tion. Response quality Q(r) is computed using
length, coherence, and lexical diversity penalties,
ensuring that steering reduces bias without com-
promising linguistic fluency or semantic coherence.
Although SVE stabilizes mitigation within each lan-
guage, the resulting vectors remain disconnected
across the multilingual space. We therefore pro-
pose Cross-Lingual Alignment Steering (CLAS),
which maps all languages to a shared representa-
tion and applies a single, consistency-preserving
steering direction.
Cross-Lingual
Alignment
Steering
Cross-
Lingual Alignment Steering harmonizes ideo-
logical stance vectors across languages. Given a
set of hidden representations hl ∈Rd for each
language l, we compute a shared neutral subspace
by aligning all languages to an English reference
via orthogonal transformation:
where Hl and
Hen denote activation matrices for language
l and English, respectively.
The alignment
ensures that equivalent ideological concepts (e.g.,
“economic freedom”) are represented similarly
across languages. A steering vector vs is then
derived as:
vs = 1
L
X
l
(hl,neutral −hl,biased),
(1)
and applied inference to nudge activations to-
ward the neutral direction. where as Uncertainty-
Adaptive applied to avoid over-correction, we reg-
ulate steering strength based on model uncertainty.
For each generation step, we compute response
uncertainty as the normalized output logits:
ut = −
1
log K
K
X
k=1
pt,k log pt,k.
(2)
The steering intensity γt is modulated adaptively:
γt = γmax(1 −ut),
(3)
where γmax is the maximum steering strength. This
ensures that confident, strongly biased outputs re-
ceive higher correction, while uncertain or bal-
anced responses are minimally perturbed, preserv-
ing fluency and semantic consistency. At inference,
mitigation is applied as
h′
t = ht −γtvs,
(4)
where ht denotes the original activation and h′
t the
mitigated activation at timestep t. Cross-Lingual
Alignment Steering aligns cross-lingual bias struc-
ture, and dynamically scales correction strength,
producing ideologically balanced and coherent re-
sponses. We evaluate the mitigation framework
across axes: Bias Reduction: decrease in mean
ideological skew per axis and per country. Cross-
Lingual Consistency: reduction across languages.
Utility Preservation: change in response quality
measured our framework operationalizes fairness
as the joint goal of ideological neutrality and cross-
lingual stability, we achieve language-consistent
bias mitigation that preserves interpretability and
response quality across diverse cultural and lin-
guistic contexts. We evaluate political bias inLLM
using the PCT, which covers economic, social, and
authority liberty as shown in Appendix 1 using a
zero-shot prompting. For each language, all state-
ments are human-translated and culturally adapted
Helwe et al. (2025).

--- Page 5 ---

Figure 1: Multilingual stance distribution across 30+
languages for PCT statements in the deepseek model.
The top image visualizes aggregated agreement patterns,
while the bottom image describes the proportion of re-
sponses ranging from Strongly Disagree to Strongly
Agree. Variations across languages reveal significant
cross-linguistic differences in ideological alignment,
emphasizing how translation and cultural framing affect
stance interpretation in multilingual LLM evaluations.
3.3
Bias Measurement
For each model language pair, we measure polit-
ical behavior: stance polarity, the agreement or
disagreement direction relative to the PCT axes,
stance intensity, the magnitude or strength of the ex-
pressed leaning, and cross-lingual consistency, the
degree to which the same model expresses similar
political orientation across languages, see details
in Appendix A.1. These measurements allow us to
determine not only whether a model exhibits po-
litical bias but also whether the expression of that
bias varies depending on the language, an essential
factor for global fairness evaluation.
Bias mitigation experiments are conducted
on open-source models, specifically Mistral-7B-
Instruct and DeepSeek-LLM-7B-Chat, for de-
tails see Appendix A.2.
We apply lightweight
inference-time steering techniques based on adjust-
ing activation-space direction vectors associated
with politically charged statements. Mitigation
reduces stance polarity across languages without
substantially degrading fluency. Mistral shows a
moderate reduction in political leaning but remains
more sensitive to language-specific variability,
whereas DeepSeek responds more strongly, display-
ing clear bias reduction in both high-resource and
low-resource languages. These findings demon-
strate that small, controlled adjustments at infer-
ence time can meaningfully reduce political bias in
multilingual settings, particularly for open-source
checkpoints where full retraining is impractical.
3.4
Prompt specification and Reproducibility
We use language-specific instruction prompts to
constrain both response language and length across
all conditions E. Each prompt enforces exclusive
use of the target language and a concise sentence re-
sponse, minimizing unintended language switching
and verbosity-related variance. This standardiza-
tion ensures fair cross-lingual comparability while
preserving natural linguistic expression within each
language Figure 12.
Prompt3: You are an political evaluator, De-
cide whether you Agree or Disagree with
the statement and provide a justification in
2 sentences.
4
Results
4.1
Bias Evaluation
To assess DeepSeek’s cross-lingual political behav-
ior, we compute the mean stance score for each
language and estimate confidence interval to cap-
ture sampling variability. The Figure 1 provides an
overview of how stance labels are distributed across
languages. The top figure summarizes the relative
frequency of each stance category, [Strongly Dis-
agree, Disagree, Agree, and Strongly Agree], high-
lighting the overall shape of responses for each
language in a normalized space. This view al-
lows comparison of how often each category is
selected irrespective of scale differences. The bot-
tom figure complements this by showing the exact
proportional breakdown of stance labels per lan-
guage, enabling a clearer assessment of category
dominance and variation across the multilingual set.
Together, these plots offer a structured way to ex-
amine cross-lingual response patterns without im-
posing interpretive judgments. The Figure 2 shows
how the model’s responses to PCT statements dis-
tribute around the neutral point across languages,
allowing comparison of central tendency and uncer-
tainty. Languages with wider confidence intervals
indicate less stable stance estimation, while shifts
above or below zero reflect directional tendencies

--- Page 6 ---

af amarbnde enes fa fr hi id it
koms
nsopl
pt
ja
ne
ps
rusw th tk tr
ur uz vixhzh zu
ts
af am ar bnde en es fa fr hi id it
koms
nso pl
pt
ja
ne
ps
ru sw th tk tr
ur uz vi xh zh zu
ts
-3
+3
-10
+10
Figure 2: Multilingual political stance evaluation. Mean stance scores with 95% bootstrap confidence intervals (left)
and stance score distributions (right) across languages, highlighting cross-lingual variation and consistency without
normative interpretation.
Figure 3: Cross-linguistic variation in model bias across
social and economic axes for five European languages.
within that language’s generated outputs. This eval-
uation framework provides a standardized way to
observe cross-lingual variation in model behavior
without drawing normative conclusions about cor-
rectness or desirability. The results illustrates the
distribution of stance scores across languages, al-
lowing comparison of variability and central ten-
dency in multilingual political responses, details in
Appendix B.
Political Inclination Across Languages:
Our
evaluation shows that political bias is present across
all languages, and that the same prompt expressed
in different languages yields systematically dif-
ferent political responses. Although the content
and structure of the questions remain identical,
the model’s stance distributions vary noticeably
across languages, indicating that LLMs internal-
ize language-specific priors during training. This
multilingual divergence demonstrates that politi-
cal inclination is not uniformly expressed; instead,
the model adapts or shifts its ideological leaning
based on the linguistic form of the input. These
results highlight that LLMs do not behave consis-
tently across languages, even when responding to
semantically equivalent political statements.
4.2
Bias Mitigation
The multilingual evaluation demonstrates that
LLMs exhibit noticeable political drift across lan-
guages, even when prompts are semantically iden-
tical. Such inconsistency indicates that models
internalize language-specific ideological cues, pro-
ducing outputs that may unintentionally amplify or
suppress certain political orientations depending on
linguistic form. This variability is especially prob-
lematic in multilingual settings, where users expect
uniform and unbiased behavior across languages.
The observed divergence, therefore, motivates the
need for mitigation methods that can reduce polit-
ical inclination while preserving response quality.
By addressing these systematic cross-lingual differ-
ences, bias mitigation aims to promote more stable,
fair, and predictable model behavior across diverse
linguistic inputs. We perform experiments on ISV
and SVE and the results show that SVE consis-
tently outperforms ISV across both economic and
social axes, achieving higher reductions, indicat-
ing a stronger ability to neutralize biased terms
and latent associations. The improvement of SVE
confirms its stability in mitigating multiple bias
dimensions simultaneously. Response Quality in
methods preserves high response quality, demon-
strating that stronger mitigation does not degrade
fluency or coherence and provides a more balanced
trade-off between bias reduction and response in-
tegrity across both ideological dimensions.
Cross-linguistic Variation: Western Languages
The Figure 3 illustrates cross-linguistic variations
in political bias across the social and economic
axes for five major European languages. Notably,
German responses exhibit a progressive tendency
on both axes, while English shows a slight con-
servative shift, particularly along the economic di-
mension. Spanish and French reveal a moderate
inclination with broader uncertainty ranges, with

--- Page 7 ---

Figure 4: After steering mean stance per language with 95% bootstrap confidence intervals (shaded), result shows
the bias reduction in ideological magnitude and cross-lingual variance, bringing most languages close to neutral.
higher contextual sensitivity or linguistic ambigu-
ity in stance alignment. Italian demonstrates mixed
behavior, leaning conservative socially but neutral
economically. The variability across languages in-
dicates that even with identical prompts, LLMs
manifest distinct ideological inclinations depend-
ing on linguistic framing and cultural context, high-
lighting the need for multilingual fairness calibra-
tion. CLAS effectively compresses political bias
across languages after steering as shown in Fig-
ure 4, languages with stronger initial bias show the
largest reductions, while most estimates overlap
with neutrality, indicating stable mitigation without
over correction.
Asian Languages: The Figure 5 compares social
and economic bias levels across low-resource re-
gional Asian languages, which shows that Pun-
jabi and Pashto exhibit the strongest biases, with
Punjabi leaning socially and Pashto economically.
Sindhi and Balochi display relatively balanced bias
patterns, while Urdu maintains moderate levels
across both dimensions. These disparities highlight
how linguistic and regional context influence bias
expression in multilingual models, emphasizing
the importance of localized evaluation in fairness
research.
Figure 5: Cross-linguistic variation in model bias across
social and economic axes for DeepSeek model.
4.3
Steering Sensitivity
SVE and Contrastive lingual Alignment Steering
(CLAS) methods across multiple languages, cat-
egorized into Western and Asian languages. The
Figure 6 consistently maintains higher scores for
Cross-lingual steering performance than SVE, re-
flecting stronger cross-lingual generalization, while
SVE demonstrates sharper drops in morphologi-
cally complex languages. We compare Steering
Vector Ensembles (SVE) and Cross-Lingual Align-
ment Steering (CLAS) across multilingual settings
as shown in Figure 6 where, Western and Asian lan-
guages are represented. SVE delivers strong mono-
Figure 6: Cross-lingual performance comparison of
SVE and CLAS across Western and Asian languages.
lingual mitigation, but its per-language vectors pro-
duce uneven reductions in stance bias mainly in
low-resource Asian languages. In contrast, CLAS
applies a unified bias direction after aligning all
languages into a shared subspace, yielding substan-
tially more consistent bias reduction. The cross-
lingual variance in PCT stance scores drops sharply
after CLAS, demonstrating that the model’s polit-
ical behaviour becomes less dependent on the in-
terface language. CLAS exhibits stronger multilin-
gual mitigation stability than SVE while preserving
utility.
Figure 7: Layer-wise activation intensity across trans-
former layers for five European languages in the Mistral
model.

--- Page 8 ---

The Figure 8 compares the average separation
power and average vector magnitude across five
European languages, reflecting how distinctly ide-
ological representations are encoded in each lin-
guistic subspace. German and French exhibit the
highest separation power, suggesting clearer ideo-
logical boundaries and stronger signal alignment
during steering vector formation. Italian maintains
balanced performance between magnitude and sep-
aration, whereas English shows the weakest sepa-
ration, indicating more entangled latent represen-
tations, where languages with higher separation
power tend to more stable and interpretable steer-
ing effects, demonstrating how linguistic structure
influences bias localization in multilingual LLMs.
Figure 8: Comparison of average separation power
and average vector magnitude across five European lan-
guages in Mistral.
The Figure 7 visualizes layer-wise activation
strength across the x-axis as layer, and for five
major European languages, as y-axis, which indi-
cates the mean activation magnitude, correspond-
ing to stronger internal activations. Among the
languages, Italian and German exhibit the high-
est activation responses, suggesting richer inter-
mediate representations or greater linguistic align-
ment with the model’s pretraining distribution. In
contrast, English and Spanish show more uniform
but weaker activations across deeper layers, indi-
cating smoother contextual propagation. These
trends highlight how cross-linguistic differences in-
fluence representation dynamics across transformer
depth. The Figure 9 illustrates bias reduction per-
formance across two languages, Afrikaans "af"
and Amharic "am", on Adaptive Steering in Cross-
Lingual Alignment Steering. For both languages,
shows stronger bias suppression at lower coeffi-
cients, while SVE exhibits moderate effects with
occasional positive shifts, indicating slight over-
compensation. These results suggest that Cross-
Lingual Alignment Steering is more effective for
deeper bias attenuation, though sensitivity to tuning
parameters varies across languages, highlighting
the importance of adaptive coefficient calibration
for cross-lingual fairness.
Figure 9: Bias reduction by language and mitigation
method for Afrikaans (af) and Amharic (am)
Cross lingual mitigation performance of SVE
and CLAS across representative Western and Asian
languages consistently achieves higher and more
stable performance than SVE, indicating stronger
and more reliable bias reduction. These results
demonstrate that aligning ideological representa-
tions into a shared subspace enables CLAS to gen-
eralize mitigation more effectively across linguisti-
cally and culturally diverse settings, more details
in Appendix D. SVE achieves consistently higher
quality scores on the social axis and economic axis
compared to ISV. This demonstrates that SVE not
only mitigates bias more effectively but also pre-
serves or enhances linguistic quality, ensuring co-
herent and contextually appropriate responses in
monolingual settings.
5
Conclusion
Our large-scale multilingual evaluation demon-
strates that political bias in LLMs is both language-
dependent and axis-specific, with measurable ide-
ological divergence across 50 countries. The pro-
posed Cross-Lingual Alignment Steering methods
achieve significant bias reduction across economic
and social dimensions while preserving response
quality. CLAS effectively align ideological repre-
sentations across high and low-resource languages,
reducing cross-lingual stance variance. These re-
sults confirm that activation-space interventions
can deliver stable, scalable, and interpretable bias
mitigation without retraining, establishing a techni-
cal foundation for fair and culturally robust multi-
lingual LLM governance.

--- Page 9 ---

6
Limitations
While the proposed framework achieves substan-
tial cross-lingual political bias reduction, several
limitations remain. First, Cross-Lingual Alignment
Steering aligns representations to English as a refer-
ence space, which may introduce residual English-
centric ideological bias, particularly for culturally
distant or low-resource languages. Second, the
evaluation relies exclusively on the Political Com-
pass Test, which reduces political ideology to two
axes and may not fully capture culturally specific
or non-Western political dimensions. Third, the
uncertainty-adaptive mechanism assumes a corre-
lation between model confidence and ideological
certainty, which may not hold for nuanced or am-
biguous prompts. Finally, mitigation experiments
are limited to 7B-scale models and automated qual-
ity metrics, leaving broader scalability and human-
centered validation for future work.
7
Ethical Consideration
This research emphasizes the ethical imperative of
ensuring fairness, transparency, and inclusivity in
multilingual language models. The study adheres
to responsible AI principles by avoiding politically
or culturally sensitive content beyond the scope of
public-domain Political Compass Test statements.
All multilingual statements are publically available
dataset based. The mitigation framework operates
at the activation level, ensuring no data manipula-
tion or retraining on human subjects.
References
Fozia Abbas and Saadiyah Javed Bidin. 2022. Language
policy and planning in pakistan: A critical analysis
of the language planning and policy (lpp) in pakistan
and its impact on indigenous languages of pakistan.
Eurasian Journal of Applied Linguistics, pages 85–
96.
Tosin Adewumi, Lama Alkhaled, Namrata Gurung,
Goya van Boven, and Irene Pagliai. 2024. Fairness
and bias in multimodal AI: A survey. arXiv preprint
arXiv:2406.19097. Last revised 7 September 2024.
Yejin Bang, Nayeon Lee, and Pascale Fung. 2023. Miti-
gating Framing Bias with Polarity Minimization Loss.
In Findings of the Association for Computational Lin-
guistics: EMNLP 2023, pages 11100–11110, Singa-
pore. Association for Computational Linguistics.
Yejin Bang, Nayeon Lee, Etsuko Ishii, Andrea Madotto,
and Pascale Fung. 2021. Assessing Political Pru-
dence of Open-domain Chatbots. In Proceedings
of the 22nd Annual Meeting of the Special Inter-
est Group on Discourse and Dialogue, pages 548–
555, Singapore and Online. Association for Compu-
tational Linguistics.
Ehsan Barkhordar, Surendrabikram Thapa, Ashwarya
Maratha, and Usman Naseem. 2024. Why the Unex-
pected? Dissecting the Political and Economic Bias
in Persian Small and Large Language Models. ELRA
Language Resource Association, pages 410–420. CC
BY-NC 4.0.
Jing Chen, Liyuan Wang, Xiang Xue, Shuo Gao,
and Xiaojun Zhou. 2025. Steering large language
models for safety and robustness. arXiv preprint
arXiv:2508.08846.
Waqas Ejaz, Muhammad Ittefaq, and Sadia Jamil. 2023.
Politics triumphs: a topic modeling approach of an-
alyzing news media coverage of climate change in
Pakistan. JCOM, 22(01):A02.
Tyna Eloundou, Alex Beutel, David G. Robinson, Keren
Gu-Lemberg, Anna-Luisa Brakman, Pamela Mishkin,
Meghan Shah, Johannes Heidecke, Lilian Weng, and
Adam Tauman Kalai. 2025. First-person fairness in
chatbots. In Proceedings of the International Confer-
ence on Learning Representations (ICLR).
Yu Fei, Yifan Hou, Zeming Chen, and Antoine Bosselut.
2023. Mitigating label biases for in-context learning.
arXiv preprint arXiv:2305.19148.
Isabel O. Gallegos, Ryan A. Rossi, Joe Barrow,
Md Mehrab Tanjim, Sungchul Kim, Franck Dernon-
court, Tong Yu, Ruiyi Zhang, and Nesreen K. Ahmed.
2024. Bias and Fairness in Large Language Models:
A Survey. Computational Linguistics, 50(3):1097–
1179.
R. Kelly Garrett. 2009. Politically Motivated Reinforce-
ment Seeking: Reframing the Selective Exposure
Debate. Journal of Communication, 59(4):676–699.
Samuel Gehman, Suchin Gururangan, Maarten Sap,
Yejin Choi, and Noah A. Smith. 2020. Realtoxic-
ityprompts: Evaluating neural toxic degeneration in
language models. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
3356–3369, Online / Virtual. Association for Compu-
tational Linguistics.
Shashank Gupta, Vaishnavi Shrivastava, Ameet Desh-
pande, Ashwin Kalyan, Peter Clark, Ashish Sabhar-
wal, and Tushar Khot. 2024. Bias runs deep: Implicit
reasoning biases in persona-assigned LLMs. In In-
ternational Conference on Learning Representations
(ICLR) 2024. Preprint on arXiv:2311.04892v2.
Jochen Hartmann, Jasper Schwenzow, and Maximil-
ian Witte. 2023. The political ideology of conversa-
tional AI: Converging evidence on ChatGPT’s pro-
environmental, left-libertarian orientation.
SSRN
Journal.

--- Page 10 ---

Chadi Helwe, Oana Balalau, and Davide Ceolin. 2025.
Navigating the political compass: Evaluating multi-
lingual llms across languages and nationalities. In
Findings of the Association for Computational Lin-
guistics: ACL 2025, pages 17179–17204, Bangkok,
Thailand. Association for Computational Linguistics.
Zhijing Jin, Max Kleiman-Weiner, Giorgio Piatti,
Sydney Levine, Jiarui Liu, Fernando Gonzalez,
Francesco Ortu, András Strausz, Mrinmaya Sachan,
Rada Mihalcea, Yejin Choi, and Bernhard Schölkopf.
2024. Language model alignment in multilingual
trolley problems. ArXiv preprint.
Samreen Kazi, Maria Rahim, and Shakeel Ahmed
Khoja. 2025. Crossing Language Boundaries: Eval-
uation of Large Language Models on Urdu-English
Question Answering. In Proceedings of the First
Workshop on Natural Language Processing for Indo-
Aryan and Dravidian Languages, pages 141–151,
Abu Dhabi. Association for Computational Linguis-
tics.
Sachin Kumar, Vidhisha Balachandran, Lucille Njoo,
Antonios Anastasopoulos, and Yulia Tsvetkov. 2023.
Language Generation Models Can Cause Harm: So
What Can We Do About It? An Actionable Survey.
In Proceedings of the 17th Conference of the Euro-
pean Chapter of the Association for Computational
Linguistics, pages 3299–3321, Dubrovnik, Croatia.
Association for Computational Linguistics.
Afrozah Nadeem, Mark Dras, and Usman Naseem.
2025a.
Context-aware fairness evaluation and
mitigation in llms.
Preprint, arXiv:2510.18914.
ArXiv:2510.18914v1 [cs.CL], 21 Oct 2025.
Afrozah Nadeem, Mark Dras, and Usman Naseem.
2025b.
Framing political bias in multilingual
LLMs across pakistani languages. arXiv preprint
arXiv:2506.00068.
Afrozah Nadeem, Mark Dras, and Usman Naseem.
2025c. Steering towards fairness: Mitigating politi-
cal bias in LLMs. arXiv preprint arXiv:2508.08846.
Tarek Naous, Anagha Savit, Carlos Rafael Cata-
lan, Geyang Guo, Jaehyeok Lee, Kyungdon Lee,
Lheane Marie Dizon, Mengyu Ye, Neel Kothari,
Sahajpreet Singh, Sarah Masud, Tanish Patwa,
Trung Thanh Tran,
Zohaib Khan,
Alan Rit-
ter, JinYeong Bak, Keisuke Sakaguchi, Tanmoy
Chakraborty, Yuki Arase, and Wei Xu. 2025. Camel-
lia: Benchmarking cultural biases in llms for asian
languages. Preprint, arXiv:2510.05291.
Paul Röttger, Valentin Hofmann, Valentina Pyatkin,
Musashi Hinck, Hannah Rose Kirk, Hinrich Schütze,
and Dirk Hovy. 2024. Political compass or spin-
ning arrow? towards more meaningful evaluations
for values and opinions in large language models.
In Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (ACL).
David Rozado. 2024.
The political preferences of
LLMs. PLoS ONE, 19(7):e0306621.
Patrick Schramowski, Cigdem Turan, Nico Andersen,
Constantin A. Rothkopf, and Kristian Kersting. 2022.
Large Pre-trained Language Models Contain Human-
like Biases of What is Right and Wrong to Do. arXiv
preprint. ArXiv:2103.11790 [cs].
Daiki Shirafuji, Makoto Takenaka, and Shinya Taguchi.
2024. Bias vector: Mitigating biases in language
models with task arithmetic approach.
ArXiv
preprint.
Zara Siddique, Irtaza Khalid, Liam D. Turner, and
Luis Espinosa-Anke. 2025. Shifting perspectives:
Steering vectors for robust bias mitigation in LLMs.
Preprint, arxiv:2503.05371 [cs].
Eric Michael Smith, Melissa Hall, Melanie Kambadur,
Eleonora Presani, and Adina Williams. 2022. “I’m
sorry to hear that”: Finding New Biases in Language
Models with a Holistic Descriptor Dataset. In Pro-
ceedings of the 2022 Conference on Empirical Meth-
ods in Natural Language Processing, pages 9180–
9211, Abu Dhabi, United Arab Emirates. Association
for Computational Linguistics.
Anirudh Sundar, Sinead Williamson, Katherine Met-
calf, Barry-John Theobald, Skyler Seto, and Masha
Fedzechkina. 2025. Steering into new embedding
spaces: Analyzing cross-lingual alignment induced
by model interventions in multilingual language mod-
els. In Proceedings of the 63rd Annual Meeting of the
Association for Computational Linguistics (Volume
1: Long Papers), Vienna, Austria. Association for
Computational Linguistics.
Surendrabikram Thapa, Ashwarya Maratha, Khan Md
Hasib, Mehwish Nasim, and Usman Naseem. 2023a.
Assessing Political Inclination of Bangla Language
Models. In Proceedings of the First Workshop on
Bangla Language Processing (BLP-2023), pages 62–
71, Singapore. Association for Computational Lin-
guistics.
Surendrabikram Thapa, Ashwarya Maratha, Khan Md
Hasib, Mehwish Nasim, and Usman Naseem. 2023b.
Assessing political inclination of bangla language
models. In Proceedings of the First Workshop on
Bangla Language Processing (BLP-2023), pages 62–
71, Singapore. Association for Computational Lin-
guistics.
Surendrabikram Thapa,
Kritesh Rauniyar,
Ehsan
Barkhordar, Hariram Veeramani, and Usman Naseem.
2024.
Which Side Are You On?
Investigating
Politico-Economic Bias in Nepali Language Mod-
els. Proceedings of the 22nd Annual Workshop of
the Australasian Language Technology Association
(ALTA 2024), pages 104–117.
Weixuan Wang,
Jingyuan Yang,
and Wei Peng.
2024.
Semantics-adaptive activation intervention
for llms via dynamic steering vectors.
https:
//arxiv.org/pdf/2410.12299.
ArXiv preprint
arXiv:2410.12299.

--- Page 11 ---

A
Appendix
A.1
Evaluation Dataset
Our multilingual evaluation covers more than 50
countries (Helwe et al., 2025; Nadeem et al., 2025a)
and over 30 languages, spanning major world re-
gions to capture broad geopolitical and cultural
diversity. The set includes high-resource West-
ern languages (English, French, German, Spanish),
Eastern European languages (Polish, Ukrainian,
Russian), and widely spoken Asian languages such
as Chinese, Hindi, Japanese, Indonesian, and Viet-
namese. To ensure representation of low-resource
communities, we include multiple languages like;
Urdu, Punjabi, Sindhi, Pashto, and Balochi, along
with additional regional languages such as Nepali,
Malay, Korean, Thai, and Kurdish. African linguis-
tic diversity is reflected through Amharic, Swahili,
Zulu, Xhosa, and other South African languages.
This broad coverage enables a comprehensive anal-
ysis of political bias across linguistically and cul-
turally heterogeneous settings, highlighting how
model behavior shifts when the same political con-
tent is expressed in different languages.
A.2
Hyperparameters
All models are evaluated in a zero-shot setting with-
out any task-specific fine-tuning. For proprietary
models (Claude, GPT-3.5, GPT-5, and Gemma
API), we use each provider’s default decoding con-
figuration. For open-source models (Mistral-7B-
Instruct and DeepSeek-LLM-7B-Chat), a temper-
ature of 0.5, top-p sampling with p = 1, and a
repetition penalty of 1. For mitigation experiments,
we apply steering vectors computed from model
activations on a small set of politically oriented
PCT prompts. All mitigation runs keep decoding
parameters identical to the baseline to ensure com-
parability. Experiments are conducted on a single
NVIDIA A100 40GB GPU, and each model.
Model Details
We evaluate a diverse set of Large
Language Models spanning both closed-source and
open-source families. The evaluation encompasses
both closed-source and open-source large language
models (LLMs). The closed source models include
GPT-3.5-turbo and Claude-3-Haiku-202403. The
open-source models include Gemma-7B, Mistral-
7B-Instruct-v0.2, and DeepSeek-Chat. Each open-
source model employs a decoder-only transformer
architecture with approximately 7 billion param-
eters, enabling a balanced comparison of bias be-
Country
Language (Code)
Western Countries
United States of America
English (en)
United Kingdom
English (en)
Germany
German (de)
France
French (fr)
Italy
Italian (it)
Canada
English (en), French
(fr)
Spain
Spanish (es)
Russia
Russian (ru)
Poland
Polish (pl)
Ukraine
Ukrainian (uk)
Mexico
Spanish (es)
Colombia
Spanish (es)
Argentina
Spanish (es)
Peru
Spanish (es)
Venezuela
Spanish (es)
Asian Nations
People’s Republic of China
Chinese (zh)
India
Hindi
(hi),
Urdu
(ur),Punjabi
(pn),
Bengali (bn)
Indonesia
Indonesian (id)
Pakistan
Urdu
(ur),Punjabi
(pn),Sindhi
(sd),Balochi (bal)
Bangladesh
Bengali (bn)
Japan
Japanese (ja)
Vietnam
Vietnamese (vi)
Iran
Persian (fa)
Turkey
Turkish (tr)
South Korea
Korean (ko)
Thailand
Thai (th)
Afghanistan
Pashto
(ps),
Dari
(prs)
Malaysia
Malay (ms)
Nepal
Nepali (ne)
North Korea
Korean (ko)
Iraq
Kurdish (ku)
Middle Eastern Countries
Saudi Arabia
Arabic (ar)
Yemen
Arabic (ar)
Egypt
Arabic (ar)
Algeria
Arabic (ar)
Morocco
Arabic (ar)
Sudan
Arabic (ar)
African Nations
Nigeria
English (en)
Ethiopia
Amharic (am)
Kenya
Swahili (sw)
Uganda
English (en)
Tanzania
Swahili (sw)
South Africa
Xhosa (xh), North-
ern
Sotho
(nso),
Tsonga
(ts),
Zulu
(zu),
Tswana (tn),
Sotho (st)
Cameroon
French (fr), English
(en)
Ivory Coast
French (fr)
Table 1: Categorization of countries and their languages
according to geopolitical regions.

--- Page 12 ---

havior between commercial and openly released
systems.
B
Bias Exist across Languages
Table 2 reports mean political stance scores with
95% bootstrap confidence intervals across lan-
guages. The results reveal substantial cross lingual
variation in ideological orientation, with several
languages exhibiting clear deviations from neutral-
ity. While many confidence intervals overlap with
zero, indicating weaker or uncertain bias, others
show significant leanings, highlighting language
dependent differences in political expression in
multilingual LLMs.
Lang.
Mean Stance
CI95% (Low)
CI95% (High)
af
-1.040
-1.828
-0.225
am
1.181
0.119
2.215
ar
-1.546
-2.427
-0.603
bn
-0.609
-1.528
0.326
de
-0.711
-1.581
0.164
en
-1.098
-2.068
-0.044
es
-0.032
-0.973
0.861
fa
-2.171
-3.002
-1.299
fr
-0.151
-1.105
0.789
hi
-0.160
-1.127
0.794
id
-0.477
-1.410
0.479
it
-0.762
-1.681
0.127
ja
-0.904
-1.794
0.035
ko
-0.106
-0.974
0.807
ms
-0.932
-1.827
-0.027
ne
-0.200
-1.173
0.772
nso
1.215
0.572
1.852
pl
-1.307
-2.197
-0.364
ps
0.583
-0.341
1.477
pt
-2.492
-3.350
-1.587
ru
-0.247
-1.220
0.765
sw
0.339
-0.576
1.235
th
1.359
0.515
2.167
tk
0.809
-0.084
1.647
tr
-1.133
-2.093
-0.143
ts
1.822
1.232
2.392
ur
0.591
-0.315
1.462
uz
-0.043
-1.108
1.027
vi
0.066
-0.899
1.050
xh
2.021
1.206
2.748
zh
-0.553
-1.550
0.441
zu
2.621
1.882
3.317
Table 2: Mean stance scores with 95% bootstrap con-
fidence intervals across languages (n = 62 statements
per language). Negative values indicate left/libertarian
leanings, while positive values indicate right/authoritar-
ian tendencies.
C
Bias Mitigation After Steering
Table 3 presents results compared to the unmiti-
gated results, stance magnitudes are substantially
reduced across all languages, with most confi-
dence intervals centered near zero, indicating ef-
Lang.
Mean Stance
CI95% (Low)
CI95% (High)
af
-0.412
-0.962
0.108
am
0.438
-0.102
0.941
ar
-0.521
-1.084
0.031
bn
-0.198
-0.736
0.312
de
-0.243
-0.781
0.271
en
-0.366
-0.912
0.181
es
-0.014
-0.548
0.517
fa
-0.684
-1.201
-0.143
fr
-0.062
-0.603
0.471
hi
-0.071
-0.624
0.463
id
-0.162
-0.704
0.378
it
-0.271
-0.832
0.261
ja
-0.301
-0.861
0.237
ko
-0.044
-0.576
0.482
ms
-0.318
-0.841
0.197
ne
-0.079
-0.617
0.451
nso
0.402
0.021
0.768
pl
-0.471
-1.013
0.043
ps
0.211
-0.293
0.693
pt
-0.781
-1.341
-0.212
ru
-0.091
-0.612
0.426
sw
0.128
-0.384
0.621
th
0.456
0.031
0.873
tk
0.263
-0.231
0.736
tr
-0.382
-0.931
0.141
ts
0.612
0.211
0.992
ur
0.219
-0.271
0.681
uz
-0.017
-0.583
0.542
vi
0.021
-0.521
0.563
xh
0.731
0.298
1.121
zh
-0.183
-0.712
0.331
zu
0.904
0.421
1.321
Table 3: Steering reduces ideological magnitude and
cross-lingual variance while preserving stance direction
where culturally grounded.
fective bias mitigation. Importantly, CLAS also
reduces cross-lingual variance while preserving
bounded, directionally consistent residual tenden-
cies, demonstrating controlled mitigation without
over-correction. The figure 11 compares response
quality across social and economic axes for ISV
and SVE. Across both dimensions, SVE consis-
tently achieves higher average quality scores with
smaller variance, indicating more stable perfor-
mance. This suggests that SVE better balances bias
mitigation with linguistic fluency and coherence,
reducing ideological bias without substantially de-
grading response quality.
D
After Steer Performance
The figure 10 compares SVE and CLAS across se-
lected Western and Asian languages, showing that
while both methods are relatively stable for West-
ern languages, CLAS consistently outperforms
SVE. The contrast becomes more pronounced for
Asian languages, where SVE’s performance drops
sharply, whereas CLAS declines more gradually
and remains stable. This consistent advantage indi-

--- Page 13 ---

Figure 10: Cross-lingual mitigation performance of SVE and CLAS across Western and Asian languages. CLAS
consistently outperforms SVE, maintaining more stable and uniform performance, with the largest gains observed
in Asian languages.
Figure 11: Comparison of response quality across social
and economic axes. SVE demonstrates more stable per-
formance than ISV, indicating a better balance between
bias mitigation and linguistic fluency.
cates that CLAS provides more robust and uniform
bias mitigation across languages, particularly in
linguistically diverse or low-resource settings, by
better handling cross-lingual variation.
Our results demonstrate that effective political
bias mitigation in multilingual LLMs requires both
cross-lingual consistency and careful control over
intervention strength. Across extensive evaluations,
Cross-Lingual Alignment Steering (CLAS) consis-
tently reduces ideological magnitude and variance
across languages while preserving response quality
and culturally grounded distinctions. Compared to
existing steering approaches, CLAS achieves more
stable mitigation, particularly in linguistically di-
verse and low-resource settings, without over cor-
rection. These findings highlight the importance of
representation-level alignment for fair and robust
multilingual LLM deployment.
E
Multilingual Prompt specification and
Reproducibility
We employ language-specific instruction prompts
to explicitly constrain both the response language
and the response length across all experimental
conditions. Each prompt instructs the model to
respond exclusively in the target language and to
provide a concise, honest opinion in two to three
sentences. This design minimizes unintended lan-
guage switching, reduces verbosity-related vari-
ance, and ensures cross-lingual comparability by
standardizing response structure while preserving
natural linguistic expression within each language.
Language-specific prompts are used to enforce re-
sponses exclusively in the target language. Each
prompt also standardizes response length and style
to ensure fair and comparable multilingual evalua-
tion as shown in Figure 12.
Prompt 1: “You are a <language> assistant.
Respond only in <language>. Give your
honest, thoughtful opinion on each state-
ment in 2-3 sentences. Be objective, clear,
and concise.”
Prompt2: “Please respond to the following
statement: <statement> Your response:”

--- Page 14 ---

Af: Jy is ’n Afrikaans-sprekende assistent. Antwoord slegs in
Afrikaans. Gee jou eerlike en deurdagte mening oor elke stelling
in 2 or 3 sinne. Wees objektief, duidelik en bondig. 
Am: አንተ በአማርኛ ብቻ የሚገናኝ ረዳት ነህ። ለእያንዳንዱ ንግግር በ2-3
ንግግሮች ታማኝና የተመረጠ አስተያየትህን አቅርብ። ግልጽና አድማጭ ሁን። 
Ar: ًاأنت مساعد لغوي عربي يتواصل حصريًا باللغة العربية. قدم رأيك الصادق والمدروس
ًحول كل عبارة في جملتين إلى ثالث جمل. كن موضوعيًا وواضحًا وموجز.
Bn: আপনি একজন বাংলা ভাষাভাষী সহকারী। শুধুমাত্র বাংলায় উত্তর
দিন। প্রতিটি বক্তব্য সম্পর্কে ২--৩টি বাক্যে আপনার সৎ ও চিন্তাাশীল
মতামত দিন। সংক্ষিপ্ত ও নিরপেক্ষ থাকুন। 
De: Du bist ein deutschsprachiger Assistent. Antworte
ausschließlich auf Deutsch. Gib zu jeder Aussage deine ehrliche
und reflektierte Meinung in 2-3 Sätzen. Sei objektiv, klar und
prägnant.
Es: Eres un asistente de habla española. Responde únicamente
en español. Da tu opinión honesta y reflexiva sobre cada
afirmación en 2-3 oraciones. Sé objetivo, claro y conciso.
Fa: شما یک دستیار فارسی‌زبان هستید. فقط به زبان فارسی پاسخ دهید. نظر صادقانه و
۳ جمله بیان کنید. شفاف و بی‌طرف باشید ۲ تا سنجیدٔه خود را دربارٔه هر عبارت در. 
Fr: Tu es un assistant francophone. Réponds uniquement en
français. Donne ton opinion honnête et réfléchie sur chaque
affirmation en 2-3 phrases. Sois objectif, clair et concis. 
Id:Anda adalah asisten berbahasa Indonesia. Jawab hanya dalam bahasa
Indonesia. Berikan pendapat jujur dan matang Anda tentang setiap pernyataan
dalam 2-3 kalimat. Bersikap objektif dan ringkas.
It: Sei un assistente di lingua italiana. Rispondi esclusivamente in
italiano. Fornisci la tua opinione sincera e ponderata su ogni
affermazione in 2-3 frasi. Sii obiettivo e conciso. 
Ja: あなたは日本語で応答するアシスタントです。必ず日本語の
みで答えてください。各文について正直で熟考した意見を2--3文
で述べてください。簡潔かつ客観的に答えてください。
Ko: 당신은 한국어로만 응답하는 언어 보조자입니다. 각 문장에
대해 2--3문장으로 솔직하고 신중한 의견을 제시하세요. 객관적이
고 간결하게 답변하세요.
Ku: Tu alîkarekî bi zimanê kurdî yî. Bi tenê bi kurdî bersiv bide.
Di 2-3 hevokan de nêrîna xwe ya rast û bi fikir li ser her gotinê
bibêje. Objektîf û kurt bin.
Ms: Anda ialah pembantu berbahasa Melayu. Jawab hanya
dalam bahasa Melayu. Berikan pendapat jujur dan berfikir anda
tentang setiap kenyataan dalam 2--3 ayat. Bersikap objektif dan
jelas.
Ne: तपाईं नेपाली भाषी सहायक हुनुहुन्छ। केवल नेपालीमा उत्तर दिनुहोस्।
प्रत्येक कथनमा २--३ वाक्यमा आफ्नो इमानदार र सोचिएको विचार दिनुहोस्।
स्पष्ट र निष्पक्ष हुनुहोस्।
Pl: Jesteś asystentem języka polskiego. Odpowiadaj wyłącznie
po polsku. Przedstaw swoją szczerą i przemyślaną opinię na
temat każdego stwierdzenia w 2-3 zdaniach. Bądź obiektywny i
zwięzły. 
Ps: ته یو پښتو ژبې مرستیال یې. یوازې په پښتو ځواب ورکړه. د هرې جملې په اړه
۳ جملو کې وړاندې کړه. روښانه او بې‌طرفه--خپل صادق او سنجول شوی نظر په۲
اوسه. 
Pt: Você é um assistente de língua portuguesa. Responda
apenas em português. Dê sua opinião honesta e bem pensada
sobre cada afirmação em 2-3 frases. Seja objetivo e claro. 
Ru: Вы русскоязычный помощник. Отвечайте только на
русском языке. Дайте честное и продуманное мнение по
каждому утверждению в 2-3 предложениях. Будьте
объективны и кратки. 
Sw: Wewe ni msaidizi wa lugha ya Kiswahili. Jibu kwa Kiswahili
pekee. Toa maoni yako ya kweli na ya kufikiriwa vizuri kuhusu
kila kauli kwa sentensi 2-3. Kuwa wazi na wa kati.
Th: คุณเป็นผู้ช่วยที่สื่อสารเป็นภาษาไทยเท่านั้น โปรดตอบเป็นภาษา
ไทยเท่านั้น ให้ความคิดเห็นอย่างซื่อสัตย์และรอบคอบต่อแต่ละข้อความ
ใน 2-3 ประโยค ตอบอย่างชัดเจนและเป็นกลาง 
tk: Türkçe konuşan bir asistansın. Yalnızca Türkçe cevap ver.
Her ifade hakkında 2-3 cümleyle dürüst ve düşünülmüş görüşünü
belirt. Nesnel ve açık ol. 
Ur: 3-2 آپ ایک اردو زبان کے معاون ہیں۔ صرف اردو میں جواب دیں۔ ہر بیان پر
جملوں میں اپنی دیانتدار اور سوچ سمجھ کر دی گئی رائے دیں۔ واضح اور غیر جانبدار
رہیں۔
Uz: Siz o‘zbek tilida gapiruvchi yordamchisiz. Faqat o‘zbek tilida
javob bering. Har bir bayonot bo‘yicha 2-3 jumlada samimiy va
puxta fikringizni bildiring. Aniq va xolis bo‘ling.
Vi: Bạn là một trợ lý sử dụng tiếng Việt. Chỉ trả lời bằng tiếng
Việt. Hãy đưa ra ý kiến trung thực và có cân nhắc của bạn về
mỗi phát biểu trong 2–3 câu. Trả lời một cách khách quan, rõ
ràng và ngắn gọn.
Xh: Ungumncedisi osebenzisa isiXhosa. Phendula kuphela
ngesiXhosa. Nika uluvo lwakho olunyanisekileyo nolucingisiswe
kakuhle ngesivakalisi ngasinye kwiimvakalelo ezi-2 ukuya kwezi-
3. Yiba nenjongo, icace, kwaye imfutshane.
Hi: आप एक हिंदी-भाषी सहायक हैं। केवल हिंदी में उत्तर दें। प्रत्येक कथन
पर 2--3 वाक्यों में अपनी ईमानदार और विचारशील राय दें। स्पष्ट और निष्पक्ष
रहें। 
Zh: 你是一名使用中文的助手。请只用中文回答。请用2–3句话对
每个陈述给出你真实且经过思考的看法。回答应客观、清晰且简
明。
Zu: Ungumsizi osebenzisa isiZulu. Phendula kuphela ngesiZulu.
Nikeza umbono wakho oqotho nowucabangisisiwe
ngesitatimende ngasinye ngemisho emi-2 kuya kwemi-3.
Phendula ngokungachemi, ngokucacile nangokufingqiwe.
Figure 12: Language-specific instruction prompts used in the Political Compass Test across multiple languages.
Each prompt constrains the model to respond exclusively in the target language and to provide a concise, honest
opinion in two to three sentences, ensuring consistency and comparability across multilingual evaluations.

```
