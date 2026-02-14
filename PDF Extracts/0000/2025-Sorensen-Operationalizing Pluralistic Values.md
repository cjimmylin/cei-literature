---\ntitle: "2025-Sorensen-Operationalizing Pluralistic Values - PDF Extract"\nsource_pdf: "Utilitarian Ethics/Borderline/2025-Sorensen-Operationalizing Pluralistic Values.pdf"\npages: 21\nextracted_at: "2026-02-14T02:17:43.443755"\n---\n\n# PDF Extract: 2025-Sorensen-Operationalizing Pluralistic Values\n\n**Source PDF:** Utilitarian Ethics/Borderline/2025-Sorensen-Operationalizing Pluralistic Values.pdf\n**Total Pages:** 21\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nOperationalizing Pluralistic Values in Large Language Model Alignment
Reveals Trade-offs in Safety, Inclusivity, and Model Behavior
Dalia Ali1, Dora Zhao2, Allison Koenecke3, Orestis Papakyriakopoulos1
1Technical University of Munich, Germany
2Stanford University, USA
3Cornell University, USA
dalia.ali@tum.de, dorothyz@stanford.edu, koenecke@cornell.edu, orestis.p@tum.de
Abstract
Although large language models (LLMs) are increasingly
trained using human feedback for safety and alignment with
human values, alignment decisions often overlook human so-
cial diversity. This study examines how incorporating plu-
ralistic values affects LLM behavior by systematically eval-
uating demographic variation and design parameters in the
alignment pipeline. We collect alignment data from US and
German participants (N = 1,095 participants, 27,375 ratings)
who rated LLM responses across five dimensions: Toxicity,
Emotional Awareness (EA), Sensitivity, Stereotypical Bias,
and Helpfulness. We fine-tuned multiple Large Language
Models and Large Reasoning Models using preferences from
different social groups while varying rating scales, disagree-
ment handling methods, and optimization techniques. The
results revealed systematic demographic effects: male par-
ticipants rated responses 18% less toxic than female partic-
ipants; conservative and Black participants rated responses
27.9% and 44% higher on EA than liberal and White par-
ticipants, respectively. Models fine-tuned on group-specific
preferences exhibited distinct behaviors. Technical design
choices showed strong effects: the preservation of rater dis-
agreement achieved roughly 53% greater toxicity reduction
than majority voting, and 5-point scales yielded about 22%
more reduction than binary formats; and, Direct Preference
Optimization (DPO) consistently outperformed Group Rel-
ative Policy Optimization (GRPO) in multi-value optimiza-
tion. These findings represent a preliminary step in answer-
ing a critical question: How should alignment balance expert-
driven and user-driven signals to ensure both safety and fair
representation?
Codes and Data: github.com/DALIAALISIDDIG/AlignCure
Introduction
As Large Language Models (LLMs) are deployed across
real-world applications, aligning them with human values
has become a core technical and ethical challenge (Wang
et al. 2023; Liu et al. 2024b; Ouyang et al. 2022). Yet human
values are not monolithic; they reflect diverse and often con-
flicting beliefs shaped by culture, politics, and lived expe-
rience (Chen, Zahidi, and Lespinet-Najib 2022; Khamassi,
Nahon, and Chatila 2024; Hadar-Shoval et al. 2024). It is no
longer realistic to assume that a single alignment objective
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
can represent everyone (Gabriel and Keeling 2025; Sorensen
et al. 2024), particularly given concerns about whose voices
shape AI safety research (Lazar and Nelson 2023). Despite
the recognition of value pluralism, alignment norms are of-
ten defined by small groups of developers, which risks ex-
cluding underrepresented worldviews (Kirk et al. 2024a).
This is particularly evident in methods such as Constitu-
tional AI, which bypass human disagreement by specify-
ing fixed normative principles in advance (Bai et al. 2022b).
While such approaches aim for consistency, they risk enforc-
ing narrow value sets that overlook alternative perspectives.
As Gabriel (2020) argues, the central challenge is not sim-
ply deciding what values AI should align with, but identify-
ing fair processes for deciding whose values matter in plu-
ralistic societies. Recent work has begun to address this the-
oretically: Kasirzadeh (2024) distinguishes between first-
order choices (how values like fairness are defined) and
second-order questions (who defines them), while Sorensen
et al. (2024) proposes formal strategies for integrating plu-
ralism through group-specific fine-tuning.
However, a key empirical gap remains; recent studies
show that current LLMs display far less preference varia-
tion than humans across cultural and political lines (Zhang
et al. 2025), reinforcing an “algorithmic monoculture” that
overlooks human value diversity (Kleinberg and Raghavan
2021). Modeling individual annotators, by contrast, helps re-
cover minority viewpoints lost under majority voting (Gor-
don et al. 2022). Yet no work has examined how demo-
graphic diversity in feedback interacts with technical design
choices to shape alignment outcomes. Building on advances
in demographic and cultural alignment, we move from anal-
ysis to intervention.
Prior studies have compared GPT-4’s safety annotations
with human ratings across groups (Movva, Koh, and Pier-
son 2024), investigated cultural alignment via cross-lingual
prompting and data mixtures (AlKhamissi et al. 2024), and
introduced DICES (Aroyo et al. 2023), which frames dis-
agreement as a signal for safety evaluation. Extending this
work, we examine how demographic differences in feed-
back and design choices shape the collapse of pluralistic hu-
man values into a single model behavior during fine-tuning.
Rather than implementing pluralistic alignment systems as
proposed by Sorensen et al. (2024), we study how stan-
dard training homogenizes value variation and determines
arXiv:2511.14476v2  [cs.AI]  25 Nov 2025

--- Page 2 ---\n\nwhich group’s preferences dominate. Specifically, we ask:
(1) How do models behave when aligned using feedback
from different social groups? (2) How do technical choices
such as rating scales, disagreement aggregation, and opti-
mization methods affect learned values?
Our Contributions. We present a systematic empirical
study of LLM alignment that jointly varies demographic
composition and technical design using real human feed-
back (27,375 ratings from 1,095 participants). Models fine-
tuned on feedback from Liberal, White, and Female par-
ticipants show improvements of 5.0, 4.7, and 3.4 percent-
age points (relative to Conservative, Black, and Male base-
lines), across emotional awareness and toxicity. Technical
choices yield even stronger effects: preserving disagreement
improves toxicity reduction by 53% relative to majority vot-
ing, 5-point scales outperform binary formats by 22%, and
DPO outperforms GRPO by about 8× on toxicity and 3×
on emotional awareness. Together, these results demonstrate
how demographic and design parameters jointly determine
alignment behavior, advancing a framework for technically
robust and socially inclusive alignment.
Related Work
Value Pluralism in AI Alignment
Value pluralism
presents a fundamental challenge for AI alignment. It holds
that multiple and potentially conflicting moral values can
each be valid without a single universal hierarchy, rejecting
the idea of a final, universally agreed-upon solution to moral
questions (Berlin 1969). This has prompted researchers to
question alignment strategies built on assumptions of uni-
versal consensus. Sorensen et al. (2024) propose technical
strategies to support pluralistic alignment, including steer-
able models that can be conditioned on specific perspectives
at inference time, approaches for matching models to target
population distributions, and methods for generating mul-
tiple reasonable responses. However, these frameworks re-
main largely theoretical, leaving open questions about how
they perform when applied with real-world data and de-
sign constraints. Our work addresses this gap by empiri-
cally testing how demographic-specific feedback, rating for-
mats, disagreement strategies, and optimization methods in-
fluence which value perspectives are amplified, suppressed,
or erased in model behavior. This provides the first empirical
grounding of value pluralism collapse in applied alignment
design.
Limitations of Current Human Feedback Pipelines for
Alignment
Recent alignment pipelines have enhanced
model safety by incorporating human preferences through
norms such as helpfulness, honesty, and harmlessness
(HHH) (Askell et al. 2021; Bai et al. 2022a; Ouyang
et al. 2022). Datasets such as BeaverTails (Jin et al. 2023),
PRISM (Kirk et al. 2024b), and OASST1 (K¨opf et al. 2024)
utilize crowd-sourced feedback to capture alignment sig-
nals, whereas benchmarks like BBQ (Parrish et al. 2021)
and pipelines like GenderAlign (Zhang et al. 2024) focus
on addressing fairness and stereotyping.
Reinforcement
Learning
from
Human
Feedback
(RLHF) (Ouyang et al. 2022) trains a reward model
from human preference comparisons and uses it to optimize
the model via reinforcement learning. However, most RLHF
paradigms assume homogeneous preferences encodable
by a single reward model (Park et al. 2024). This leads
to implicit averaging that prioritizes majority preferences
while neglecting minorities (Chakraborty et al. 2024). In
extreme cases, this leads to preference collapse, where mi-
nority preferences are disregarded (Xiao et al. 2024). These
pipelines overlook how different social groups interpret
alignment concepts like harm or respect based on cultural
or political context (Kovaˇc et al. 2023; Sorensen et al. 2024;
Pang et al. 2023; Lyu et al. 2025; Pan et al. 2025).
Recent findings on algorithmic monoculture highlight
challenges in capturing human value diversity. Zhang et al.
(2025) show that 21 state-of-the-art LLMs produce signif-
icantly less preference variation than humans across five
countries (N=15,000), limiting the diversity expressible in
current preference datasets. While their work proposes sam-
pling methods to diversify model outputs, our study ad-
dresses the complementary problem of how evaluation de-
sign, including demographic variation, rating scale format,
and disagreement handling, can preserve or suppress plural-
istic values within constrained response spaces.
Rating Scales and Disagreement Handling
The choice
of rating scale, whether Likert (e.g., a 5-point scale
from “strongly disagree” to “strongly agree”), binary (e.g.,
“agree” or “disagree”), or pairwise (e.g., choosing a pre-
ferred response between two options), influences both rater
behavior and model outcomes. Survey research shows that
scale format affects response biases, including net accep-
tance, extreme responding, and misinterpretation of reverse-
coded items (Weijters, Cabooter, and Schillewaert 2010).
Likert scales are especially prone to central tendency bias,
where respondents tend to avoid the endpoints and favor the
midpoints (Douven and Schupbach 2018). In LLM align-
ment, recent studies increasingly use pairwise comparisons
for training and evaluation (Zheng et al. 2023). Despite
the widespread use of various formats in human feedback
pipelines, little is known about how these choices impact
model behavior. Our work fills this gap through a systematic
comparison of rating formats.
Disagreement between raters is often resolved using ma-
jority voting or averaging, which can erase minority perspec-
tives and obscure subjective variation (Gordon et al. 2022;
Davani, D´ıaz, and Prabhakaran 2022). Recent work pro-
poses alternatives such as soft-label representations that re-
tain disagreement distributions, and multi-annotator models
that predict individual judgments (Davani, D´ıaz, and Prab-
hakaran 2022; Aroyo and Welty 2015). Kraus and Kroll
(2025) offers a framework for distinguishing noise from
meaningful signal, arguing that tasks involving personal val-
ues should preserve disagreement rather than aggregate it.
Our work builds on this literature by systematically com-
paring how different aggregation methods, from consensus-
based to disagreement-preserving, shape the downstream
behavior of aligned models.

--- Page 3 ---\n\nData Collection
Prompt Selection and Response Generation
To exam-
ine how social group differences and technical choices af-
fect model alignment, we develop a bilingual alignment
pipeline (English-German) with a focus on gender-related
scenarios. Crucially, all participants, regardless of their
own demographics, view the same set of gender-related
prompt-response pairs, isolating the effects of rater de-
mographics and design choices without confounding topic
variation. The prompts are drawn from red-teaming, gen-
der bias, and alignment (BeaverTails) benchmarks (Gan-
guli et al. 2022; Parrish et al. 2021; Ji et al. 2023), us-
ing gender-related keyword filters. Responses are gener-
ated using Wizard-Vicuna-7B-Uncensored-GPTQ
(TheBloke 2023), selected because (1) its lack of safety
filtering ensures exposure to a broad range of potentially
problematic outputs, and (2) it is a stable open-source base
model ensuring reproducibility. This yields 37,884 prompt-
response pairs, from which we select 1,761 unique pairs for
human evaluation. The pairs are translated into German us-
ing DeepL (2024) and checked for semantic equivalence by
a native speaker (see Supplementary A.1 and A.2).
Rating Dimensions and Scale Design
Participants rate
model outputs along five alignment dimensions: Toxicity,
Emotional Awareness, Sensitivity & Openness, Helpfulness,
and Stereotypical Bias (see Supplementary A.3 for defini-
tions provided to participants). Following recent sociotech-
nical alignment frameworks (Kirk et al. 2023), these dimen-
sions capture how AI responses affect users, balancing ethi-
cal concerns (toxicity and stereotypical bias) with social di-
mensions (sensitivity, openness, and helpfulness) (Liu et al.
2024a; Bilquise, Ibrahim, and Shaalan 2022; Yin, Goh, and
Hu 2024; Lissak et al. 2024; Ji et al. 2023). This multi-
dimensional approach expands beyond traditional helpful-
ness and harmfulness prompt–response pairs, yielding a to-
tal of 27,375 evaluations. Each dimension addresses aspects
of human-AI interaction that different social groups may pri-
oritize differently, making them relevant for studying value
pluralism in alignment. Each dimension is rated using a 5-
point Likert scale (from “Strongly Disagree” to “Strongly
Agree”), allowing participants to express the intensity of
their judgments rather than making binary classifications.
Participants received clear definitions for each dimension
(see supplementary A.3) before rating, ensuring consistent
interpretation across cultural contexts.
Participant Recruitment and Demographics
We obtain
ethics approval from Technical University of Munich review
board prior to data collection. We recruit 1,095 participants
from the United States and Germany via Prolific (2025),
targeting balanced distribution across gender, political spec-
trum, age, ethnicity, and country of residence (see Supple-
mentary Table 3 for participant demographics). Each partic-
ipant rates five prompt–response pairs. Participants are com-
pensated and informed that their responses will help train fu-
ture LLMs. We include attention checks to ensure data qual-
ity and collect demographic details (gender, age, ethnicity,
political orientation) to support subgroup analysis (Supple-
mentary A.4).
Data Analyses Informing Experiment
Pervasive Disagreement Across All Dimensions
Analy-
sis of unique 1,761 prompt–response pairs evaluated by mul-
tiple participants (mean: 3.1 raters per pair, all pairs with
≥2 raters) reveals systematic disagreement across all align-
ment dimensions. Disagreement, defined as variation in 5-
point Likert ratings within the same prompt–response pair,
occurred in 85.3% of cases, ranging from 84.5% for sensi-
tivity to 86.2% for helpfulness. This analysis of 5,475 in-
dividual ratings from 1,095 participants demonstrates that
conflicting human preferences are fundamental characteris-
tics of alignment evaluation, not isolated incidents.
Cross-Dimensional Rating Complexity
Participants fre-
quently assign seemingly contradictory ratings to the same
response across different alignment dimensions. By exam-
ining how often responses rated positively for one dimen-
sion were also rated positively for another, we found that
among responses rated as emotionally aware, 20.8% were
also rated as toxic, and 33.5% were also rated as stereotypi-
cally biased. This pattern shows that participants can simul-
taneously perceive both positive and negative qualities in the
same AI response, suggesting that alignment evaluation in-
volves complex trade-offs rather than straightforward cate-
gorization (Figure 1). This aligns with evidence that users
hold diverse, sometimes conflicting preferences rather than
a single aggregated signal (G¨olz, Haghtalab, and Yang 2025;
Fleisig, Fazelpour et al. 2025).
Figure 1: Conditional probabilities between alignment di-
mensions. Each cell shows the probability of a positive rat-
ing in the column given a positive rating in the row.
Ordinal Regression Results
We conduct a cumulative link mixed model (CLMM) anal-
ysis (Christensen 2023) to identify demographic factors that
significantly influence alignment ratings across the five di-

--- Page 4 ---\n\nmensions. Our model specification is:
CLMM(Alignment Ratingi ∼Countryi + Genderi+
Agei +
Political Spectrumi + Ethnicityi+
(1 | Participant IDi) + (1 | Contexti))
(1)
The reference group is defined as White, US-based, Lib-
eral, aged 18–30, and identifying as she/her/hers. Our anal-
ysis reveals several statistically significant demographic ef-
fects (see Table 1). Male participants rate responses as 18%
less toxic and 20.9% less stereotypically biased compared
to female participants. Conservative participants perceive re-
sponses as 27.9% more sensitive and 27% more emotionally
aware than Liberals. Black or African American participants
rate responses as 58% more sensitive and 44% more emo-
tionally aware than White participants, a pattern consistent
with work showing that Black Americans often attend more
closely to emotional nuance and cultural sensitivity in AI in-
teractions (Sandoval et al. 2025; Basoah et al. 2025). Addi-
tionally, participants aged 51-60 find responses 40.6% less
helpful compared to younger participants (see Supplemen-
tary A.6).
Table 1: Demographic Predictors of Participant Ratings. Ar-
rows show direction relative to baseline (↑higher, ↓lower);
M = Male, C = Conservative, B = Black or African Amer-
ican (baselines: White, US-based, Liberal, aged 18–30, and
female). *p < .05, **p < .01, ***p < .001.
Dimension
Gender
Age
Political
Ethnicity
Toxicity
Yes** (M ↓)
No
No
No
Helpfulness
No
Yes*** (51-60 ↓)
No
No
Sensitivity
No
No
Yes** (C ↑)
Yes*** (B ↑)
Stereotypical Bias
Yes*** (M ↓)
No
No
No
Emotional Awareness
No
No
Yes* (C ↑)
Yes*** (B ↑)
Experiment Setup
Fine-tuning Experiments
We conduct four fine-tuning experiments to examine how
demographic variation and technical design choices affect
model alignment. Experiments 1–3 rely on Direct Pref-
erence Optimization (DPO) (Rafailov et al. 2023), which
learns from pairwise response comparisons. We use DPO
for Experiments 1–3 because Experiment 4 shows it outper-
forms GRPO. Experiment 4 then contrasts DPO with Group-
Relative Policy Optimization (GRPO) (Shao et al. 2024),
an on-policy method that optimizes scalar rewards across
multiple sampled completions using group-normalized ad-
vantages. Each method requires distinct data formatting,
and we construct datasets accordingly. All experiments fo-
cus on toxicity and emotional awareness; these two dimen-
sions are chosen to capture complementary safety concerns
of harm avoidance and social understanding, where demo-
graphic and cultural backgrounds shape perceptions. Across
the dataset, we obtain 5,475 ratings per dimension from
1,095 raters, applied to 1,761 unique prompt–response pairs,
some of which receive multiple independent ratings (see
Supplementary B.1, B.2 and B.3). All experiments are repli-
cated across seven model architectures to ensure robustness
(see Supplementary Table 9 for model overviews).
Experiment 1: Data Stratification by Demographic
Groups
We fine-tune models on balanced subsets of hu-
man feedback to examine how demographic composition
influences alignment outcomes. Three contrasts are tested:
gender (female vs. male), political orientation (liberal vs.
conservative), and ethnicity (White vs. Black).1 Each sub-
group contributed an equal number of ratings to control
for the size of the data set and distributional effects. Inter-
annotator reliability, measured using Krippendorff’s α for
toxicity annotations, was α=0.35 (White) and α=0.44
(Black) for ethnicity, α=0.39 (Liberal) and α=0.33 (Con-
servative) for political orientation, and α=0.38 for both fe-
male and male raters, consistent with prior work (Ross et al.
2016; Bui, von der Wense, and Lauscher 2025); these val-
ues indicate substantial within-group variation rather than
consensus. For each subgroup, a separate model is fine-
tuned using DPO while preserving all five-point Likert rat-
ings. The resulting models are evaluated on two alignment
dimensions: Toxicity and Emotional Awareness, and com-
pared against a baseline trained on feedback from conser-
vative, male, and Black participants. Following Table 1, we
focus on emotional awareness for the political spectrum and
ethnicity, and on toxicity for gender, with complementary
robustness checks (Supplementary B.6). This design enables
systematic analysis of both within and cross-dimension ef-
fects.
Experiment 2: Rating Scale Granularity
We investigate
how rating scale granularity influences alignment outcomes
by creating three versions of the toxicity dataset: (1) a 5-
point Likert scale (Strongly Disagree to Strongly Agree), (2)
a 3-point scale (Disagree, Neutral, Agree), and (3) a binary
scale (excluding Neutral responses). For each scale version,
we retain all participant ratings and fine-tune separate mod-
els using DPO on toxicity feedback. This setup enables us to
assess how the level of granularity impacts the model’s abil-
ity to learn alignment preferences. We focus on Likert scale
ratings rather than pairwise comparisons to capture the full
spectrum of participant sentiment and enable analysis across
multiple granularity levels.
Experiment 3: Disagreement Handling Strategies
To
examine the effects of inter-annotator disagreement han-
dling, we create five training datasets using different aggre-
gation methods: (1) all data without aggregation, (2) major-
ity vote, (3) full consensus (complete rater agreement only),
(4) random selection (first rater’s rating), and (5) averaged
ratings (mean of numeric-coded responses rounded to near-
est category). We fine-tune separate DPO models on each
dataset to assess how disagreement resolution strategies im-
pact alignment performance. All models are trained using
the 5-point Likert scale and evaluated on the Toxicity di-
mension.
1Age affects helpfulness only; it shows no consistent effects for
toxicity or emotional awareness, so we do not use it as a contrast.

--- Page 5 ---\n\nExperiment 4: DPO vs. GRPO Optimization Method
Comparison
We systematically compare DPO and GRPO
in multi-value optimization using our combined Toxicity
and Emotional Awareness dataset (5-point scale, all data
without aggregation). We format the merged dataset accord-
ing to each method’s requirements and fine-tune separate
models to evaluate their comparative effectiveness in simul-
taneously reducing toxicity and improving emotional aware-
ness in model outputs.
Experimental Design and Statistical Analysis
All ex-
periments use LoRA fine-tuning (Hu et al. 2022), with
deterministic sampling (temperature=0.0) for reproducible
evaluation across seven diverse model architectures (1B-
14B parameters), ensuring consistent comparison of align-
ment effects across demographic groups and technical con-
ditions. After fine-tuning the models on human feedback,
we use GPT–4o–mini to score their toxicity and emotional-
awareness outputs. We validate these LLM-generated scores
against human expert judgements, achieving 85% agree-
ment (see Supplementary B.2 and B.3). We use a DerSi-
monian–Laird random-effects meta-analysis (DerSimonian
and Laird 1986) to pool effects across model architectures,
accounting for both within-model variance and between-
model heterogeneity. Full equations and derivations are pro-
vided in (Supplementary B.5) .
Results
Experiment 1: Demographic Composition Effects
on Model Fine-tuning Outcomes
We assess how subgroup-specific fine-tuning affects align-
ment outcomes across gender, political orientation, and eth-
nicity by comparing models trained on female, liberal, and
White feedback with models trained on male, conservative,
and Black feedback (Figure 2).
Demographic
Feedback
Shapes
Specific
Behaviors.
Models fine-tuned on Liberal and White feedback produced
higher emotional awareness scores than those trained on
Conservative and Black feedback (pooled effects: 0.049,
p = 0.010, and 0.046, p = 0.001, respectively). Similarly,
models fine-tuned on Female feedback showed lower tox-
icity than those trained on Male feedback (pooled effect:
−0.035, p = 0.002). These effects were consistent across
seven model architectures.
Effects Are Dimension-Specific.
To test for general-
ization beyond the target dimensions, each demograph-
ically fine-tuned model was evaluated on both toxicity
and emotional awareness. No statistically significant cross-
dimensional effects were observed. For instance, the model
fine-tuned on Female toxicity feedback did not significantly
alter emotional awareness (p = 0.860), while Liberal and
White emotional-awareness models showed no effect on
toxicity (p = 0.500 and p = 0.880, respectively). These
findings demonstrate that demographic composition pro-
duces measurable yet dimension-specific effects on align-
ment: subgroup value preferences are reliably encoded in
fine-tuned models without introducing unintended behav-
ioral shifts across unrelated alignment dimensions.
Experiment 2: Rating Scale Granularity Effects on
Alignment Training
We examine how the granularity of the rating scale affects
alignment effectiveness by comparing 5-point, 3-point, and
binary scales using data from the toxicity dimension and
DPO fine-tuning. We examine scale granularity with a fo-
cus on toxicity ratings (Figure 3).
Granular Scales Improve Alignment Performance
All
scales produce a reduction in toxicity relative to the con-
trol model (no fine-tuning), but with substantially different
effect sizes. The 5-point scale achieves the largest effect
(−0.242), followed by the 3-point scale (−0.225) and bi-
nary scale (−0.198). Pairwise comparisons reveal that the
5-point scale outperforms the binary scale (p = 0.0141) and
marginally outperforms the 3-point scale (p = 0.0140), indi-
cating that scale granularity has an impact on model training
outcomes. The difference between 3-point and binary scales
is statistically marginal yet directionally consistent, confirm-
ing that finer scales yield stronger alignment effects.
Implications of Scale Granularity for Model Learning
5-point scales are 22% more effective than binary scales at
reducing toxicity (effect sizes: −0.242 vs. −0.198); this pat-
tern is consistent with findings that multi-level cardinal feed-
back (such as 5-point scale) yields more learnable reward
models than pairwise preferences, while maintaining sim-
ilar levels of inter-rater reliability (Kreutzer, Uyheng, and
Riezler 2018). This performance gap reveals that reducing
human feedback to binary choices for individual alignment
tasks systematically under-utilizes available preference in-
formation. While binary formats are widely adopted in pref-
erence learning, our findings show measurable costs to the
effectiveness of alignment.
Experiment 3: Disagreement Handling Strategy
Effects on Alignment Training
We examine how approaches to handling inter-annotator dis-
agreement affect alignment outcomes by comparing five ag-
gregation strategies: preserving all ratings, averaging, ma-
jority vote, random selection, and full consensus (Figure 4).
Complete Rating Preservation Demonstrates Superior
Alignment Performance
All strategies reduce toxicity
relative to the control model, but their effectiveness varies
substantially. Preserving all ratings yields the strongest re-
duction (−0.242), closely followed by averaging ratings
(−0.229). Other approaches perform less effectively: ma-
jority vote (−0.158), random selection (−0.146), and full
consensus (−0.039). Pairwise comparisons confirm that
preserving all ratings consistently outperforms consensus-
based and random selection methods, while the averaged-
rating strategy performs comparably to full preservation.
Preserving all ratings is approximately 53% more effec-
tive than majority vote and nearly 6× more effective than
full consensus in reducing toxicity. The strong performance
of preserving or averaging all ratings shows that disagree-
ment carries meaningful signal. Majority vote and con-
sensus filtering suppress minority perspectives and weaken
alignment. Treating disagreement as information rather than

--- Page 6 ---\n\nFigure 2: Effects of demographic composition on fine-tuning outcomes. Purple circles show model differences between groups
(Liberal, Female, White minus Conservative, Male, Black, respectively) on Emotional Awareness or Toxicity ratings; blue
triangles show survey-estimated differences for the same contrasts. Positive values indicate higher Emotional Awareness for the
first group; negative values indicate lower Toxicity for the first group. Error bars show 95% confidence intervals.
Figure 3: Rating Scale Effects on Toxicity Reduction. (A)
All scales reduce toxicity relative to the control (no fine-
tuning), with the 5-point most effective. (B) 5-point scales
significantly outperform binary. Error bars: 95% CIs. Lower
values indicate reduced toxicity.
noise improves robustness and inclusivity, yielding stronger
alignment across diverse preferences.
Experiment 4: DPO vs GRPO Comparison
DPO outperforms GRPO Training
We systematically
compare DPO and GRPO using a multi-objective loss that
jointly optimizes toxicity and emotional awareness (Fig-
ure 5). When trained on the same-sized dataset, DPO con-
sistently outperforms GRPO across both dimensions. The
DPO-Toxic+EA model achieves substantial toxicity reduc-
tion (−0.159, p < 0.001) and meaningful emotional aware-
ness improvement (0.084), while GRPO-Toxic+EA shows
only marginal effects (−0.020, p = 0.045; 0.029, p =
0.034). These correspond to effect sizes roughly 8× larger
for toxicity and nearly 3× larger for emotional awareness,
demonstrating DPO’s advantage over GRPO for multivalue
alignment. All effects relative to the control (no fine-tuning)
Figure 4: Disagreement Handling Strategy Effects on Align-
ment Training. (A) Strategy performance relative to the con-
trol (no fine-tuning) on toxicity. (B) Pairwise strategy com-
parisons. Error bars show 95% CIs. Lower values indicate
better performance.
are statistically significant (p < 0.05).
Single-Objective DPO Outperforms Multi-Objective
Training
Comparing DPO variants reveals clear trade-
offs between single- and multi-objective training. For toxic-
ity reduction, DPO-Toxic yields the largest effect (−0.243,
p < 0.001), significantly outperforming both DPO-EA (dif-
ference: 0.097, p < 0.001) and the multi-objective DPO-
Toxic+EA model (difference: −0.084, p = 0.022). DPO-
EA and DPO-Toxic+EA exhibit comparable toxicity effects

--- Page 7 ---\n\nFigure 5: DPO and GRPO Optimization Methods Comparison. (A-B) Performance of each DPO and GRPO trained model.
(C-D) Pairwise comparisons between single-objective and multi-objective DPO approaches. Error bars show 95% CIs.
(difference: 0.013, p = 0.743). For emotional awareness,
all three DPO variants perform similarly: DPO-EA achieves
0.083 (p = 0.002), DPO-Toxic achieves 0.068 (p = 0.003),
and DPO-Toxic+EA achieves 0.084 (p = 0.003), with no
significant pairwise differences (all p > 0.13). These find-
ings show that single-objective toxicity fine-tuning max-
imizes performance on its targeted dimension, whereas
emotional-awareness gains remain indistinguishable across
all models optimized with DPO.
Optimization Method and Training Objective Matter
Two findings emerge from our dataset. First, the choice
of optimization method significantly influences alignment
outcomes: DPO yields larger and more reliable gains than
GRPO on the same data. Second, focused single-objective
DPO fine-tuning produces stronger and more interpretable
effects than multi-objective training. Taken together, these
results challenge the assumption that multi-objective align-
ment or newer optimization methods automatically perform
better, highlighting the need for methodological precision in
preference-based fine-tuning.
Discussion and Conclusion
How should alignment processes balance expert-driven and
user-driven signals to ensure both safety and fair represen-
tation? Lazar and Nelson (2023) argue that AI safety is
shaped by a demographic monoculture that lacks legitimacy
and intellectual breadth, while Gyevnar and Kasirzadeh
(2025) call for an epistemically inclusive and pluralistic ap-
proach. Anthis et al. (2025) show that even a single rigorous
fairness criterion becomes intractable for general-purpose
LLMs across diverse contexts, and Kleinberg, Mullainathan,
and Raghavan (2016) formally demonstrate that core group-
fairness conditions cannot be satisfied simultaneously ex-
cept in highly restricted cases. Taken together with our em-
pirical results, this suggests that known pathologies in algo-
rithmic fairness also appear in alignment research, with lim-
ited participation and structural limits jointly produce sys-
tematic distortions in model behavior.
Safety judgments are not universal but reflect specific de-
mographic perspectives. Male and female participants rated
identical responses with an 18% difference in perceived tox-
icity, while Conservative and Black participants reported
27.9% and 44% higher emotional awareness ratings, re-
spectively, compared to Liberal, White participants. Cur-
rent alignment approaches that aggregate these differences
away may systematically exclude safety-relevant perspec-
tives. Preserving disagreement achieved the strongest tox-
icity reduction, outperforming the majority vote by 53%,
and other strategies. This suggests alignment annotators’
“noise” may be an essential safety signal. Technical choices
such as rating scales (5-point exceeding binary by 22%) and
optimization methods (DPO exceeding GRPO) profoundly
impact safety performance. Rather than trading off safety
against inclusivity, we find that inclusive approaches en-
hance safety outcomes.
Our findings reveal systematic demographic effects: mod-
els trained on White, Liberal, and Female feedback achieve
higher emotional awareness and lower toxicity respectively
than those trained on Black, Conservative, and Male feed-
back. These shifts occur because demographic groups dif-
fer fundamentally in how they evaluate harm and emotional
quality. Together, these results show that demographic diver-
sity is not a one-time dataset choice but an ongoing align-
ment requirement. Safety judgments vary across popula-
tions and shift over time, demanding continuous reassess-
ment of whose perspectives are prioritized. Since both train-
ing data and technical design systematically advantage cer-
tain groups over others, robust alignment requires periodic
audits: Which demographic groups dominate our data? How
do our methodological decisions suppress minority voices?
This reflexive practice can help ensure that alignment does
not unintentionally center the values of specific groups.
Rather than relying only on prescriptive value choices
made by researchers or model developers (Kirk et al. 2024a),
expert technical knowledge should serve democratic inclu-
sion rather than replace it. Our findings support systems that
preserve diverse safety perspectives rather than require com-
plete agreement. Robust AI safety requires both expert so-
phistication and comprehensive democratic representation
as complementary requirements for effective alignment.
We conclude with limitations (see more in Supplementary
A.5). Our dataset covers only two WEIRD-dominant coun-
tries and has uneven demographic representation (underrep-
resenting conservatives, gender minorities, and older adults).
Model evaluation used GPT-4o-mini, though its judgments
are in high agreement with human reviewers. Our optimiza-
tion analysis focused on DPO and GRPO, leaving other
methods for future work. These constraints do not affect the
core patterns but highlight the need for more diverse datasets
and broader evaluation of optimization approaches.
Acknowledgements
We thank Mich`ele Wieland, Aysenur Kocak, Cheng Yu,
Furkan Kadıo˘glu, Jana Diesner, Shaghayegh Kolli and
Nafiseh Nikeghbal for their valuable discussions and sup-
port throughout this project.

--- Page 8 ---\n\nReferences
AlKhamissi, B.; ElNokrashy, M.; AlKhamissi, M.; and
Diab, M. 2024. Investigating cultural alignment of large lan-
guage models. arXiv preprint arXiv:2402.13231.
Anthis, J. R.; Lum, K.; Ekstrand, M.; Feller, A.; and Tan, C.
2025. The impossibility of fair LLMs. In Proceedings of the
63rd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 105–120.
Aroyo, L.; Taylor, A.; Diaz, M.; Homan, C.; Parrish, A.;
Serapio-Garc´ıa, G.; Prabhakaran, V.; and Wang, D. 2023.
Dices dataset: Diversity in conversational ai evaluation for
safety. Advances in Neural Information Processing Systems,
36: 53330–53342.
Aroyo, L.; and Welty, C. 2015. Truth is a lie: Crowd truth
and the seven myths of human annotation. AI Magazine,
36(1): 15–24.
Askell, A.; Bai, Y.; Chen, A.; Drain, D.; Ganguli, D.;
Henighan, T.; Jones, A.; Joseph, N.; Mann, B.; DasSarma,
N.; Elhage, N.; Hatfield-Dodds, Z.; Hernandez, D.; Kernion,
J.; Ndousse, K.; Olsson, C.; Amodei, D.; Brown, T.; Clark,
J.; McCandlish, S.; Olah, C.; and Kaplan, J. 2021. A Gen-
eral Language Assistant as a Laboratory for Alignment. Ac-
cessed: 2025-05-29, arXiv:2112.00861.
Bai, Y.; Jones, A.; Ndousse, K.; Askell, A.; Chen, A.; Das-
Sarma, N.; Drain, D.; Fort, S.; Ganguli, D.; Henighan, T.;
et al. 2022a.
Training a helpful and harmless assistant
with reinforcement learning from human feedback. arXiv
preprint arXiv:2204.05862.
Bai, Y.; Kadavath, S.; Kundu, S.; Askell, A.; Kernion, J.;
Jones, A.; Chen, A.; Goldie, A.; Mirhoseini, A.; McKinnon,
C.; et al. 2022b. Constitutional AI: harmlessness from AI
feedback. 2022. arXiv preprint arXiv:2212.08073, 8(3).
Basoah, J.; Cunningham, J. L.; Adams, E.; Bose, A.; Jain,
A.; Yadav, K.; Yang, Z.; Reinecke, K.; and Rosner, D. 2025.
Should AI mimic people? Understanding AI-Supported
writing technology among Black users. Proceedings of the
ACM on Human-Computer Interaction, 9(7): 1–51.
Berlin, I. 1969. Two Concepts of Liberty. In Four Essays on
Liberty, 118–172. Oxford University Press.
Bilquise, G.; Ibrahim, S.; and Shaalan, K. F. 2022. Emotion-
ally Intelligent Chatbots: A Systematic Literature Review.
Human Behavior and Emerging Technologies.
Accessed:
2024-07-21.
Bui, M. D.; von der Wense, K.; and Lauscher, A. 2025.
Multi3Hate: Multimodal, Multilingual, and Multicultural
Hate Speech Detection with Vision–Language Models.
arXiv preprint arXiv:2411.03888.
Chakraborty, S.; Qiu, J.; Yuan, H.; Koppel, A.; Manocha, D.;
Huang, F.; Bedi, A. S.; and Wang, M. 2024. MaxMin-RLHF:
Alignment with Diverse Human Preferences. Proceedings of
the 41st International Conference on Machine Learning.
Chen, L.; Zahidi, K.; and Lespinet-Najib, V. 2022. Aligning
artificial intelligence with human values: reflections from a
phenomenological perspective. AI & Society, 37(3): 1151–
1171.
Christensen, R. H. B. 2023. ordinal—Regression Models for
Ordinal Data. R package version 2023.12-4.1.
Davani, A. M.; D´ıaz, M.; and Prabhakaran, V. 2022. Dealing
with disagreements: Looking beyond the majority vote in
subjective annotations. Transactions of the Association for
Computational Linguistics, 10: 92–110.
DeepL. 2024. DeepL Translator. Accessed: 2024-07-26.
DerSimonian, R.; and Laird, N. 1986. Meta-analysis in clin-
ical trials. Controlled Clinical Trials, 7(3): 177–188.
Douven, I.; and Schupbach, J. N. 2018. A Bayesian per-
spective on Likert scales and central tendency. Psychonomic
Bulletin & Review, 25(3): 1203–1211.
Fleisig, J.; Fazelpour, S.; et al. 2025. Perspectival Homog-
enization: A Normative Framework for Reasoning About
Disagreement in AI Development.
In Proceedings of the
ACM Conference on Fairness, Accountability, and Trans-
parency (FAccT).
Gabriel, I. 2020. Artificial intelligence, values, and align-
ment. Minds and machines, 30(3): 411–437.
Gabriel, I.; and Keeling, G. 2025. A matter of principle?
AI alignment as the fair treatment of claims. Philosophical
Studies.
Ganguli, D.; Lovitt, L.; Kernion, J.; Askell, A.; Bai, Y.; Ka-
davath, S.; Mann, B.; Perez, E.; Schiefer, N.; Ndousse, K.;
et al. 2022. Red teaming language models to reduce harms:
Methods, scaling behaviors, and lessons learned.
arXiv
preprint arXiv:2209.07858.
G¨olz, P.; Haghtalab, N.; and Yang, K. 2025. Distortion of
AI Alignment: Does Preference Optimization Optimize for
Preferences? arXiv preprint arXiv:2502.04564.
Gordon, M. L.; Lam, M. S.; Park, J. S.; Patel, K.; Hancock,
J. T.; Hashimoto, T.; and Bernstein, M. S. 2022. Jury Learn-
ing: Integrating Dissenting Voices into Machine Learning
Models.
In CHI Conference on Human Factors in Com-
puting Systems, CHI ’22, 1–19. New York, NY, USA: ACM.
ISBN 978-1-4503-9157-3/22/04.
Gyevnar, B.; and Kasirzadeh, A. 2025. AI safety for every-
one. Nature Machine Intelligence, 1–12.
Hadar-Shoval, D.; Asraf, K.; Mizrachi, Y.; Haber, Y.; and
Elyoseph, Z. 2024. Assessing the Alignment of Large Lan-
guage Models With Human Values for Mental Health Inte-
gration: Cross-Sectional Study Using Schwartz’s Theory of
Basic Values. JMIR Mental Health, 11: e55988.
Hu, E. J.; Shen, Y.; Wallis, P.; Allen-Zhu, Z.; Li, Y.; Wang,
S.; Wang, L.; Chen, W.; et al. 2022. Lora: Low-rank adapta-
tion of large language models. ICLR, 1(2): 3.
Ji, J.; Liu, M.; Dai, J.; Pan, X.; Zhang, C.; Bian, C.; Chen, B.;
Sun, R.; Wang, Y.; and Yang, Y. 2023. Beavertails: Towards
improved safety alignment of llm via a human-preference
dataset. Advances in Neural Information Processing Sys-
tems, 36: 24678–24704.
Jigsaw; and Google. 2025. Jigsaw’s Perspective API. https:
//perspectiveapi.com/. Accessed: 16 November 2025.
Jin, D.; Mehri, S.; Hazarika, D.; Padmakumar, A.; Lee, S.;
Liu, Y.; and Namazifar, M. 2023. Data-efficient alignment of

--- Page 9 ---\n\nlarge language models with human feedback through natural
language. arXiv preprint arXiv:2311.14543.
Kasirzadeh, A. 2024.
Plurality of value pluralism and ai
value alignment.
In Pluralistic Alignment Workshop at
NeurIPS 2024.
Khamassi, M.; Nahon, M.; and Chatila, R. 2024.
Strong
and weak alignment of large language models with human
values. Scientific Reports, 14(1): 19399.
Kirk, H.; Vidgen, B.; R¨ottger, P.; et al. 2024a. The benefits,
risks and bounds of personalizing the alignment of large lan-
guage models to individuals. Nature Machine Intelligence,
6: 383–392.
Kirk, H. R.; Vidgen, B.; R¨ottger, P.; and Hale, S. A. 2023.
The Empty Signifier Problem: Towards Clearer Paradigms
for Operationalising ”Alignment” in Large Language Mod-
els. Accessed: 2024-08-21, arXiv:2310.02457.
Kirk, H. R.; Whitefield, A.; R¨ottger, P.; Bean, A.; Mar-
gatina, K.; Ciro, J.; Mosquera, R.; Bartolo, M.; Williams,
A.; He, H.; et al. 2024b. The PRISM Alignment Project:
What Participatory, Representative and Individualised Hu-
man Feedback Reveals About the Subjective and Multicul-
tural Alignment of Large Language Models. arXiv preprint
arXiv:2404.16019.
Kleinberg, J.; Mullainathan, S.; and Raghavan, M. 2016.
Inherent trade-offs in the fair determination of risk scores.
arXiv preprint arXiv:1609.05807.
Kleinberg, J.; and Raghavan, M. 2021. Algorithmic mono-
culture and social welfare.
Proceedings of the National
Academy of Sciences, 118(22): e2018340118.
K¨opf, A.; Kilcher, Y.; von R¨utte, D.; Anagnostidis, S.; Tam,
Z. R.; Stevens, K.; Barhoum, A.; Nguyen, D.; Stanley,
O.; Nagyfi, R.; et al. 2024.
Openassistant conversations-
democratizing large language model alignment. Advances
in Neural Information Processing Systems, 36.
Kovaˇc, G.; Sawayama, M.; Portelas, R.; Colas, C.; Dominey,
P. F.; and Oudeyer, P.-Y. 2023.
Large language models
as superpositions of cultural perspectives.
arXiv preprint
arXiv:2307.07870.
Kraus, K.; and Kroll, M. 2025.
Maximizing Signal in
Human-Model Preference Alignment.
In Proceedings of
the AAAI Conference on Artificial Intelligence, volume 39,
27392–27400.
Kreutzer, J.; Uyheng, J.; and Riezler, S. 2018. Reliability
and learnability of human bandit feedback for sequence-
to-sequence
reinforcement
learning.
arXiv
preprint
arXiv:1805.10627.
Lazar, S.; and Nelson, A. 2023. AI safety on whose terms?
Lissak, S.; Calderon, N.; Shenkman, G.; Ophir, Y.; Fruchter,
E.; Klomek, A. B.; and Reichart, R. 2024.
The Colorful
Future of LLMs: Evaluating and Improving LLMs as Emo-
tional Supporters for Queer Youth. Accessed: 2024-06-27,
arXiv:2402.11886.
Liu, Y.; Yao, Y.; Ton, J.-F.; Zhang, X.; Guo, R.; Cheng, H.;
Klochkov, Y.; Taufiq, M. F.; and Li, H. 2024a. Trustwor-
thy LLMs: a Survey and Guideline for Evaluating Large
Language Models’ Alignment.
Accessed: 2024-06-25,
arXiv:2308.05374.
Liu, Y.; Zhou, H.; Guo, Z.; Shareghi, E.; Vuli´c, I.; Korhonen,
A.; and Collier, N. 2024b. Aligning with Human Judgement:
The Role of Pairwise Preference in Large Language Model
Evaluators. In Proceedings of the Conference on Language
Modeling (COLM).
Lyu, H.; Luo, J.; Kang, J.; and Koenecke, A. 2025. Char-
acterizing Bias: Benchmarking Large Language Models in
Simplified versus Traditional Chinese.
In Proceedings of
the 2025 ACM Conference on Fairness, Accountability, and
Transparency, 2815–2846.
Movva, R.; Koh, P. W.; and Pierson, E. 2024. Annotation
alignment: Comparing LLM and human annotations of con-
versational safety. arXiv preprint arXiv:2406.06369.
Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright, C.;
Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.;
et al. 2022. Training language models to follow instructions
with human feedback. Advances in neural information pro-
cessing systems, 35: 27730–27744.
Pan, E.; Choi, A. S. G.; Ter Hoeve, M.; Seto, S.; and
Koenecke, A. 2025.
Analyzing Dialectical Biases in
LLMs for Knowledge and Reasoning Benchmarks.
In
Christodoulopoulos, C.; Chakraborty, T.; Rose, C.; and
Peng, V., eds., Findings of the Association for Computa-
tional Linguistics: EMNLP 2025, 20882–20893. Suzhou,
China: Association for Computational Linguistics.
ISBN
979-8-89176-335-7.
Pang, R. Y.; Cenatempo, J.; Graham, F.; Kuehn, B.;
Whisenant, M.; Botchway, P.; Stone Perez, K.; and Koe-
necke, A. 2023.
Auditing cross-cultural consistency of
human-annotated labels for recommendation systems.
In
Proceedings of the 2023 ACM Conference on Fairness, Ac-
countability, and Transparency, 1531–1552.
Park, C.; Liu, M.; Zhang, K.; and Ozdaglar, A. 2024.
Principled RLHF from Heterogeneous Feedback via Per-
sonalization and Preference Aggregation.
arXiv preprint
arXiv:2405.00254.
Parrish, A.; Chen, A.; Nangia, N.; Padmakumar, V.; Phang,
J.; Thompson, J.; Htut, P. M.; and Bowman, S. R. 2021.
BBQ: A hand-built bias benchmark for question answering.
arXiv preprint arXiv:2110.08193.
Prolific. 2025. Prolific: Online participant recruitment for
surveys and experiments. https://www.prolific.com/. Ac-
cessed: 12 November 2025.
Rafailov, R.; Sharma, A.; Mitchell, E.; Manning, C. D.; Er-
mon, S.; and Finn, C. 2023. Direct preference optimization:
Your language model is secretly a reward model. Advances
in neural information processing systems, 36: 53728–53741.
Ross, B.; Rist, M.; Carbonell, G.; Cabrera, B.; Kurowsky,
N.; and Wojatzki, M. 2016. Measuring the reliability of hate
speech annotations: The case of the European refugee crisis.
arXiv preprint arXiv:1701.08118.
Sandoval, S. C.; Acquaye, C.; Cobbina, K.; Teli, M. N.;
and Daum´e III, H. 2025. My LLM might Mimic AAE–But
When Should it? arXiv preprint arXiv:2502.04564.
Shao, Z.; Wang, P.; Zhu, Q.; Xu, R.; Song, J.; Bi, X.; Zhang,
H.; Zhang, M.; Li, Y.; Wu, Y.; et al. 2024. Deepseekmath:

--- Page 10 ---\n\nPushing the limits of mathematical reasoning in open lan-
guage models. arXiv preprint arXiv:2402.03300.
Sharma, A.; Miner, A. S.; Atkins, D. C.; and Althoff, T.
2020. A Computational Approach to Understanding Em-
pathy Expressed in Text-Based Mental Health Support. In
Proceedings of the 2020 Conference on Empirical Methods
in Natural Language Processing (EMNLP), 5263–5276. As-
sociation for Computational Linguistics.
Sorensen, T.; Moore, J.; Fisher, J.; Gordon, M.; Mireshghal-
lah, N.; Rytting, C. M.; Ye, A.; Jiang, L.; Lu, X.; Dziri, N.;
et al. 2024. A Roadmap to Pluralistic Alignment. arXiv
preprint arXiv:2402.05070.
Tan, X.; Shi, S.; Qiu, X.; Qu, C.; Qi, Z.; Xu, Y.; and Qi,
Y. 2023.
Self-Criticism: Aligning Large Language Mod-
els with their Understanding of Helpfulness, Honesty, and
Harmlessness. In Wang, M.; and Zitouni, I., eds., Proceed-
ings of the 2023 Conference on Empirical Methods in Nat-
ural Language Processing: Industry Track, 650–662. Singa-
pore: Association for Computational Linguistics. Accessed:
2024-07-26.
TheBloke. 2023.
Wizard-Vicuna-7B-Uncensored-GPTQ.
https://huggingface.co/TheBloke/Wizard-Vicuna-7B-
Uncensored-GPTQ.
Wang, Y.; Zhong, W.; Li, L.; Mi, F.; Zeng, X.; Huang, W.;
Shang, L.; Jiang, X.; and Liu, Q. 2023.
Aligning Large
Language Models with Human: A Survey. arXiv preprint
arXiv:2307.12966.
Weijters, B.; Cabooter, E.; and Schillewaert, N. 2010. The
effect of rating scale format on response styles: The number
of response categories and response category labels. Inter-
national Journal of Research in Marketing, 27(3): 236–247.
Xiao, J.; Li, Z.; Xu, M.; Zhang, C.; Wang, M.; and Liu, Z.
2024. On the Algorithmic Bias of Aligning Large Language
Models with RLHF: Preference Collapse and Matching Reg-
ularization. arXiv preprint arXiv:2405.16455.
Yin, J.; Goh, T.-T.; and Hu, Y. 2024. Interactions with ed-
ucational chatbots: the impact of induced emotions and stu-
dents’ learning motivation. International Journal of Educa-
tional Technology in Higher Education, 21(1): 47.
Zhang, L. H.; Milli, S.; Jusko, K.; Smith, J.; Amos, B.;
Bouaziz, W.; Revel, M.; Kussman, J.; Titus, L.; Radharapu,
B.; Yu, J.; Sarma, V.; Rose, K.; and Nickel, M. 2025. Culti-
vating Pluralism In Algorithmic Monoculture: The Commu-
nity Alignment Dataset. arXiv preprint arXiv:2507.09650.
Zhang, T.; Zeng, Z.; Xiao, Y.; Zhuang, H.; Chen, C.; Foulds,
J.; and Pan, S. 2024. GenderAlign: An Alignment Dataset
for Mitigating Gender Bias in Large Language Models.
arXiv preprint arXiv:2406.13925.
Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; Wu, Z.;
Zhuang, Y.; Lin, Z.; Li, Z.; Li, D.; Xing, E.; et al. 2023. Judg-
ing LLM-as-a-Judge with MT-Bench and Chatbot Arena.
Advances in Neural Information Processing Systems, 36:
46595–46623.
Zhihong Shao, Q. Z. R. X. J. S. M. Z. Y. K. L. Y. W. D. G.,
Peiyi Wang. 2024. TRL: Reinforcement Learning for Trans-
former Models – GRPO Trainer.

--- Page 11 ---\n\nSupplementary A
A.1 Model Instructions for Response Generation
We used Wizard-Vicuna-7B-Uncensored-GPTQ
(TheBloke 2023) because it is stable, fully open source, and
straightforward to reproduce. The uncensored version can
generate unsafe and sensitive outputs, which is necessary for
our study because participants must evaluate the responses
as they are, including cases that contain bias, toxicity, or
emotionally inappropriate content. The model’s quantized
format also makes large-scale generation fast and efficient.
These features make it an appropriate choice for produc-
ing the varied responses required for participant evaluation.
Table 2 lists the five instructions (contexts) we provide to
the LLM to obtain different perspectives: “No Instruction”,
“Republican Perspective”, “Belief in Patriarchy”, “Focus on
Empathy”, and “Focus on Equality”. These instructions are
prepended to each original prompt before model generation,
creating responses that reflect different value orientations.
Table 2: Instructions used to generate responses.
Instruction
Text (English / German)
No Instruction
–
Republican Perspective
Answer as someone who
votes for the Republican
party.
Beantworte
als
jemand,
der f¨ur die Republikanische
Partei abstimmt.
Belief in Patriarchy
Answer as someone who
believes in patriarchy.
Beantworte
als
jemand,
der
an
das
Patriarchat
glaubt.
Focus on Empathy
Answer as an empathetic
person.
Beantworte als empathische
Person.
Focus on Equality
Answer with a focus on
promoting equality.
Beantworte
mit
Fokus
auf
die
F¨orderung
der
Gleichstellung.
A.2 Example of Gender-Focused Prompt-Response
Pairs
Figure 6 displays three example gender-related prompts
collected from different datasets and Wizard-Vicuna-7B-
Uncensored-GPTQ responses. The prompt-response pairs
were translated into German using DeepL (2024). We se-
lected gender-related prompts to ensure all participants eval-
uated responses within the same thematic domain, control-
ling for topic variation and isolating differences in individual
judgment rather than content effects.
A.3 Definitions of Alignment Dimensions
The following definitions were shown at the start of the sur-
vey to ensure consistent interpretation of each alignment di-
mension. Participants received the definitions directly in the
survey interface (without additional examples) and were also
provided with links to the source papers that define each di-
mension. To avoid language mixing, we deployed two paral-
lel survey platforms: an English version and a German ver-
sion. Participants were routed automatically based on their
Prolific demographic information, and each participant saw
the entire survey-definitions and instructions—in a single
language only.
Stereotypical Gender Bias
English: Refers to beliefs about a person’s abilities and in-
terests based on their gender (Liu et al. 2024a, p.17).
German:
Bezieht
sich
auf
¨Uberzeugungen
¨uber
die
F¨ahigkeiten und Interessen einer Person basierend auf ihrem
Geschlecht (Liu et al. 2024a, p.17).
Toxicity
English: Refers to language that exhibits rudeness, disre-
spect, threats, or attacks on particular cultural, racial, or gen-
der groups (Liu et al. 2024a, p.25).
German: Bezieht sich auf Sprache, die Unh¨oflichkeit, Re-
spektlosigkeit, Drohungen oder Angriffe auf bestimmte kul-
turelle, rassische oder geschlechtsspezifische Gruppen zeigt
(Liu et al. 2024a, p.25).
Emotional Awareness
English: Refers to the ability of an LLM to correctly identify
and consider the user’s emotions (Liu et al. 2024a; Bilquise,
Ibrahim, and Shaalan 2022; Yin, Goh, and Hu 2024).
German: Bezieht sich auf die F¨ahigkeit eines LLMs,
die Emotionen der Nutzer korrekt zu erkennen und zu
ber¨ucksichtigen (Liu et al. 2024a; Bilquise, Ibrahim, and
Shaalan 2022; Yin, Goh, and Hu 2024).
Sensitivity and Openness
English: Refers to the LLM’s ability to provide thoughtful,
encouraging, and open responses that promote self-growth
and transparent conversations (Lissak et al. 2024, p.22).
German: Bezieht sich auf die F¨ahigkeit des LLM, durch-
dachte, ermutigende und offene Antworten zu geben, die das
eigene Wachstum und transparente Gespr¨ache f¨ordern (Lis-
sak et al. 2024, p.22).
Helpfulness
English: Refers to the clarity, completeness, and relevance
of the LLM’s responses in competently reacting to the
user’s prompt (Tan et al. 2023; Ji et al. 2023). German:
Bezieht sich auf die Klarheit, Vollst¨andigkeit und Relevanz
der Antworten des LLM bei der kompetenten Beantwortung
der Benutzeranfragen (Tan et al. 2023; Ji et al. 2023).

--- Page 12 ---\n\nFigure 6: Gender-related prompt-response examples from Wizard-Vicuna-7B-Uncensored-GPTQ.

--- Page 13 ---\n\nA.4 Detailed Recruitment and Data Quality
Procedures
Participant Screening and Quality Control
We recruit
participants from Prolific, a crowdsourcing platform de-
signed for academic research
(Prolific 2025). Data col-
lection took place between September 2024 and January
2025. Each participant rated 5 randomly drawn prompt-
response pairs from a pool of 1,762. The total cost for par-
ticipant compensation across both countries was approxi-
mately $6,000 USD. We implement multiple quality control
measures to ensure reliable data:
• Pre-screening: Only participants with Prolific approval
ratings above 95% are eligible to participate.
• Attention checks: We embed two attention check ques-
tions throughout the survey. Participants who fail to re-
spond correctly to both attention checks are automati-
cally excluded from the study:
– “The following statement contains important informa-
tion. Please select ‘Neutral’ if you are reading this
carefully.”
– “The following statement contains important informa-
tion. Please select ‘Strongly Agree’ if you are reading
this carefully.”
• Completion time validation: Participants are informed
that the study takes approximately 15 minutes to com-
plete, including time to read the consent form, evaluate
AI responses, review dimension definitions, and provide
demographic information. We set a minimum completion
threshold of 5 minutes; participants completing the study
faster are excluded as this indicates insufficient time to
thoughtfully evaluate the content. Among our final sam-
ple of 1,095 participants, the median completion time
was around 10 minutes.
• Response pattern analysis: After data collection, we
conduct post-hoc validation to identify participants who
may have rushed their responses. This includes detect-
ing uniform response patterns where participants select
the same rating (e.g., “Strongly Agree”) across all five
dimensions, indicating insufficient engagement with the
content rather than genuine evaluation.
Together, these measures ensure that our final dataset
of 1,095 participants reflects thoughtful and engaged re-
sponses; approximately 25% of initially recruited par-
ticipants were removed after failing attention checks,
minimum-time thresholds, or post-hoc quality-control cri-
teria.
Demographic Breakdown of Study Participants
This
section presents the demographic characteristics of the 1,095
participants who complete our study. To ensure ethical data
collection and respect participant privacy, we provide an “I
wish not to declare” option for all demographic questions,
allowing participants to opt out without being forced to pro-
vide false information. The sample includes diverse repre-
sentation across age groups, gender identities, countries of
residence, ethnic backgrounds, and political affiliations, pro-
viding a comprehensive foundation for analyzing responses
to the survey questions.
Table 3: Demographic Breakdown of Study Participants
Category
Subcategory
Count (%)
Total Participants
Total
1095 (100.00%)
Age
18–30
485 (44.29%)
31–40
319 (29.13%)
41–50
148 (13.52%)
51–60
94 (8.58%)
60+
46 (4.20%)
Wish not to declare
3 (0.27%)
Gender
He/Him/His
510 (46.58%)
She/Her/Hers
549 (50.14%)
They/Them/Theirs
18 (1.64%)
Wish not to declare
18 (1.64%)
Country of Residence
Germany
525 (47.95%)
USA
563 (51.42%)
Wish not to declare
7 (0.64%)
Ethnicity
White
748 (68.31%)
Black/African American
138 (12.60%)
Asian
69 (6.30%)
Mixed
51 (4.66%)
Hispanic/Latino
28 (2.56%)
Middle Eastern/N. African
23 (2.10%)
American Indian/Alaska Native
6 (0.55%)
Wish not to declare
32 (2.92%)
Political Spectrum
Rather Liberal
343 (31.32%)
Centre
300 (27.40%)
Liberal
244 (22.28%)
Rather Conservative
110 (10.05%)
Conservative
98 (8.95%)
Political Party
Republicans
193 (17.63%)
Democrats
281 (25.66%)
AfD
28 (2.56%)
Andere
79 (7.21%)
CDU/CSU
56 (5.11%)
FDP
28 (2.56%)
Gr¨une
135 (12.33%)
Linke
65 (5.94%)
Piraten
11 (1.00%)
SPD
66 (6.03%)
Tier
15 (1.37%)
Wish not to declare
138 (12.60%)

--- Page 14 ---\n\nDistribution of Ratings Across Value Dimensions
To
provide an overview of how human raters evaluated the lan-
guage model responses, we visualized the distribution of rat-
ings across the five value dimensions(Figure 7): stereotypi-
cal bias, toxicity, emotional awareness, sensitivity, and help-
fulness. Each dimension was evaluated on a 5-point Likert
scale ranging from strongly disagree to strongly agree.
Figure 7: Distribution of participant ratings across five value
dimensions. Ratings are on a 5-point Likert scale: strongly
disagree, disagree, neutral, agree, and strongly agree.
A.5 Limitations and Future Work
Our dataset includes participants from the US and Ger-
many, limiting cultural scope; we also recognize that both
countries represent predominantly WEIRD (Western, Edu-
cated, Industrialized, Rich, and Democratic) cultures, and
suggest that future work be conducted across a more di-
verse set of countries and cultures. We standardized political
ideology using a five-point scale and harmonized ethnicity
categories across countries, while acknowledging inherent
cross-national differences. To ensure sufficient sample sizes,
we collapsed adjacent ideological groups (e.g., “conserva-
tive” and “rather conservative”) – see Supplementary Table
3 for participant demographics. Still, conservatives, gender
minorities, and older adults remained underrepresented, re-
flecting common online recruitment challenges. Future work
should expand geographic and demographic diversity.
While using GPT-4o-mini for evaluation may miss cul-
tural nuance, we validated its use through two human ex-
perts who independently evaluated 50 responses, achieving
85% agreement across toxicity and emotional awareness di-
mensions. Furthermore, our optimization analysis focused
on DPO versus GRPO, leaving Proximal Policy Optimiza-
tion (PPO) and Constitutional AI for future work.
Scale granularity analysis involved converting 5-point rat-
ings to 3-point and binary formats. Although systematically
applied, this process may not fully preserve semantic mean-
ing. Future studies should directly collect ratings at different
granularities and examine optimal scale designs for captur-
ing value diversity across demographic groups.
A.6 Detailed Regression Results
This appendix presents the complete ordinal regression re-
sults for all five rating dimensions analyzed in our study. For
regression analysis, we collapsed the 5-point Likert scale
into a 3-point scale (Agree, Neutral, Disagree) to improve
model stability by increasing observations per category and
to enhance interpretability of the estimated effects. Each
table reports coefficient estimates, odds ratios, and signifi-
cance levels for demographic predictors. Significance is de-
noted as: ∗p < 0.05, ∗∗p < 0.01, ∗∗∗p < 0.001.
Table 4: CLMM coefficients for Toxicity. Coefficient esti-
mates and significance levels.
Variable
Est.
OR
p-value
Sig
Country: Germany
-0.073
0.93
0.325
Male (he/him)
-0.197
0.821
0.002
*
Gender: Non-binary
-0.099
0.906
0.675
Age: 31-40
-0.071
0.931
0.34
Age: 41-50
-0.049
0.952
0.622
Age: 51-60
-0.095
0.909
0.422
Age: 60+
-0.072
0.93
0.657
Pol: Centre
0.098
1.103
0.183
Pol: Conservative
-0.06
0.941
0.497
Ethnicity:Black/African
American
0.015
1.015
0.884
Ethnicity: Hispanic/Latino
0.231
1.26
0.211
Ethnicity: Asian
-0.01
0.99
0.941
Ethnicity: MENA
0.185
1.203
0.383
Ethnicity: Mixed
-0.146
0.864
0.323
Table 5: CLMM coefficients for Helpfulness. Coefficient
estimates and significance levels.
Variable
Est.
OR
p-value
Sig
Country: Germany
-0.149
0.861
0.073
Male (he/him)
0.069
1.071
0.347
Gender: Non-binary
-0.228
0.796
0.4
Age: 31-40
0.07
1.072
0.409
Age: 41-50
-0.059
0.943
0.603
Age: 51-60
-0.521
0.594
0
*
Age: 60+
-0.095
0.91
0.607
Pol: Centre
-0.049
0.952
0.556
Pol: Conservative
0.004
1.004
0.967
Ethnicity:Black/African
American
0.106
1.112
0.371
Ethnicity: Hispanic/Latino
-0.239
0.788
0.252
Ethnicity: Asian
0.052
1.054
0.73
Ethnicity: MENA
-0.387
0.679
0.11
Ethnicity: Mixed
0.012
1.013
0.94

--- Page 15 ---\n\nTable 6: CLMM coefficients for Sensitivity. Coefficient es-
timates and significance levels.
Variable
Est.
OR
p-value
Sig
Country: Germany
-0.022
0.978
0.766
Male (he/him)
0.069
1.072
0.29
Gender: Non-binary
-0.274
0.76
0.257
Age: 31-40
0.044
1.045
0.558
Age: 41-50
0.01
1.01
0.921
Age: 51-60
-0.071
0.931
0.55
Age: 60+
-0.009
0.991
0.956
Pol: Centre
0.122
1.129
0.101
Pol: Conservative
0.246
1.279
0.006
*
Ethnicity:Black/African
American
0.459
1.582
0
*
Ethnicity: Hispanic/Latino
0.074
1.077
0.689
Ethnicity: Asian
0.166
1.18
0.213
Ethnicity: MENA
0.133
1.143
0.527
Ethnicity: Mixed
0.063
1.066
0.671
Table 7: CLMM coefficients for Stereotypical Bias. Coef-
ficient estimates and significance levels.
Variable
Est.
OR
p-value
Sig
Country: Germany
-0.115
0.892
0.119
Male (he/him)
-0.234
0.791
0
*
Gender: Non-binary
-0.037
0.964
0.878
Age: 31-40
0.051
1.052
0.496
Age: 41-50
0.137
1.146
0.169
Age: 51-60
0.028
1.028
0.814
Age: 60+
-0.056
0.946
0.733
Pol: Centre
0.122
1.13
0.096
Pol: Conservative
0.038
1.039
0.67
Ethnicity:Black/African
American
-0.003
0.997
0.975
Ethnicity: Hispanic/Latino
0.025
1.025
0.893
Ethnicity: Asian
-0.115
0.892
0.379
Ethnicity: MENA
0.06
1.062
0.778
Ethnicity: Mixed
-0.017
0.983
0.909
Table 8: CLMM coefficients for Emotional Awareness.
Coefficient estimates and significance levels.
Variable
Est.
OR
p-value
Sig
Country: Germany
0.075
1.078
0.333
Male (he/him)
0.012
1.012
0.858
Gender: Non-binary
-0.304
0.738
0.237
Age: 31-40
0.035
1.035
0.659
Age: 41-50
-0.08
0.923
0.445
Age: 51-60
-0.103
0.902
0.407
Age: 60+
-0.002
0.998
0.99
Pol: Centre
0.065
1.067
0.4
Pol: Conservative
0.24
1.271
0.01
*
Ethnicity:Black/African
American
0.362
1.436
0.001
*
Ethnicity: Hispanic/Latino
0.249
1.283
0.202
Ethnicity: Asian
0.04
1.041
0.774
Ethnicity: MENA
0.362
1.436
0.1
Ethnicity: Mixed
0.004
1.004
0.979
A.7 Alignment Assumptions and Our Framing
Our work contrasts the standard “one-model-for-all” align-
ment pipeline with a pluralistic alternative. Traditional
alignment assumes that a small set of annotators and a fixed
set of values can speak for everyone, producing a single
model trained on uniform feedback. Our approach instead
varies who provides the feedback and how the feedback is
encoded. By using diverse raters and testing different rating
scales, aggregation methods and optimisation choices, we
show that alignment outcomes change depending on these
social and technical decisions. This demonstrates that align-
ment is not inherently universal and that accounting for vari-
ation leads to models that better reflect diverse perspectives.
Figure 8: Traditional monolithic alignment assumes univer-
sal values of helpfulness, honesty, and harmlessness (left),
whereas our approach varies rater demographics and tech-
nical choices (rating scales, disagreement aggregation, and
optimization methods) to reflect diverse perspectives (right).

--- Page 16 ---\n\nSupplementary B
B.1 Experimental Design Overview
Figure 10 provides a systematic overview of our four fine-
tuning experiments, showing how we systematically vary
key parameters while controlling others. Each experiment
isolates specific factors affecting pluralistic alignment: de-
mographic stratification (Experiment 1), rating scale granu-
larity (Experiment 2), disagreement handling methods (Ex-
periment 3), and optimization algorithms (Experiment 4).
This design allows us to assess the individual and compara-
tive effects of demographic composition, technical choices,
and methodological decisions on model alignment perfor-
mance.
B.2 Complete Model and Experimental
Specifications
All models used in this study were available on Hugging
Face throughout the fine-tuning period (March–September
2025), ensuring stable and reproducible training. The se-
lection captures variation in size, objectives, and safety
properties to support comparative analysis across archi-
tectures. Table 9 lists the models included. Model-level
results, including full breakdowns for every architecture,
are provided in our public repository https://github.com/
DALIAALISIDDIG/AlignCure.
Table 9: Model Architecture Overview. Primary specifica-
tions for all evaluation models.
Model
Params Specialization
Wizard-Vicuna-7B (cognitivecomputations)
7B
Instruction + Uncensored
Llama-3-8B-Lexi (Orenguteng)
8B
General-purpose + Uncen-
sored
Deep-Reasoning-Llama-3.2 (DavidAU)
3B
Reasoning + Uncensored
Qwen3-14B Abliterated (mlabonne)
14B
General-purpose + Abliter-
ated
Guanaco-3B-Uncensored-v2 (Fredithefish)
3B
Instruction-tuned + Uncen-
sored
Llama3.2-1B-Uncensored (xdrshjr)
1B
General-purpose + Uncen-
sored
WizardVicuna-3B (heegyu)
3B
Instruction + Uncensored
B.3 Evaluation Methodology
We evaluate alignment performance using OpenAI’s GPT-
4o-mini API to score model responses on Toxicity (contin-
uous 0.0-1.0 scale) and Emotional Awareness dimensions
(binary 0-1). We use two different scales because toxic-
ity, following the continuous scoring framework of (Jig-
saw and Google 2025), varies by degree, whereas emo-
tional awareness, consistent with Sharma et al. (2020), is
expressed in threshold-like categories and is therefore more
reliably captured as a binary judgement. To validate this
automated approach, we conduct a reliability study where
two independent human experts assess 50 randomly selected
responses using identical criteria. We achieve an average
agreement rate of 0.85 between human evaluators and au-
tomated scores across both dimensions, confirming the re-
liability of our evaluation approach. Our automated evalu-
Figure 9: Evaluation prompt specifications. Standardized
protocols for toxicity assessment (continuous 0.0-1.0 scale)
and emotional awareness evaluation (binary 0-1 scale) using
GPT-4o-mini as evaluator.
ation employs GPT-4o-mini with temperature=0 for consis-
tent scoring. Figure 9 shows the prompts used for each align-
ment dimension.
B.4 Alignment Optimization Methods
This subsection summarizes the optimization procedures
used in our experiments and provides the mathematical for-

--- Page 17 ---\n\nmulations for the preference learning objectives applied in
both DPO and GRPO.
Single-Objective DPO
Classical Direct Preference Opti-
mization (DPO) on a single dimension (e.g., toxicity) mini-
mizes the pairwise logistic loss:
LDPO(θ) = −E(x,y+,y−)[log σ(sθ(y+; x) −sθ(y−; x))].
(2)
where
σ(z) =
1
1 + e−z ,
(3)
sθ(y; x) = log πθ(y | x) −log πref(y | x).
(4)
Group Relative Policy Optimization (GRPO)
For each
prompt q and model-generated output oi, the reward func-
tion R(q, oi) assigns a scalar value ri ∈[0, 1] based on a
Likert-style human rating. We use two distinct mappings
depending on whether the evaluation dimension is nega-
tively or positively oriented. We implement GRPO using the
Hugging Face TRL library’s GRPOTrainer (Zhihong Shao
2024).
Negative-oriented
dimensions.
For
d
∈
{toxicity,
stereotypical bias}, agreement indicates un-
desirable behavior. The reward function is:
R(q, oi) =

















1.0
if rating = strongly disagree,
0.8
if rating = disagree,
0.5
if rating = neutral,
0.2
if rating = agree,
0.0
if rating = strongly agree.
(5)
Positive-oriented
dimensions.
For
d
∈
{sensitivity, helpfulness, emotional awareness}, agreement
indicates desirable behavior. The reward function is:
R(q, oi) =

















0.0
if rating = strongly disagree,
0.2
if rating = disagree,
0.5
if rating = neutral,
0.8
if rating = agree,
1.0
if rating = strongly agree.
(6)
Computing the loss. The GRPO objective maximizes the
advantage while keeping the policy close to the reference
model. The loss is:
(7)
The scalar reward is then used within GRPO by first com-
puting the group-normalized reward
˜ri = ri −mean(r1, . . . , rG)
std(r1, . . . , rG)
,
(8)
which defines the per-token advantage
ˆAi,t = ˜ri,
∀t ∈{1, . . . , Ti}.
(9)
Multi-Objective DPO
To optimize two objectives simul-
taneously (e.g., toxicity and emotional awareness), we pool
all accept/reject pairs—“accept” refers to the response rated
higher by participants on the target dimension, and “reject”
is the lower-rated response—from both dimensions into one
dataset and apply the same loss:
LDPO(θ) = −E(x,y+,y−)[log σ(sθ(y+; x) −sθ(y−; x))].
(10)
where each (y+, y−) may originate from either objec-
tive’s judgments.
DPO with Different Aggregation Strategies
We use the
same DPO loss but vary how we form (y+, y−) from the raw
Likert annotations:
LDPO(θ) = −E(x,y+,y−)[log σ(sθ(y+; x) −sθ(y−; x))].
(11)
We construct five versions of the dataset using different
aggregation strategies to examine how disagreement resolu-
tion affects alignment outcomes:
• All Ratings: Includes all individual rater responses with-
out aggregation. Each accept/reject judgment is used as a
training pair.
• Majority Vote: Assigns the most frequent label across
raters for each prompt-response pair. Ties are broken ran-
domly.
• Full Consensus: Retains only examples where all raters
unanimously agreed on the label. This method empha-
sizes certainty but results in fewer examples.
• Random Selection: Randomly samples one rater’s label
per item. This simulates a lightweight annotation strategy
with minimal aggregation.
• Create Average: Converts Likert ratings to numeric
scores, computes the mean per item, and rounds to the
nearest valid category.
Each strategy encodes a different assumption about how
best to handle disagreement, enabling us to assess the impact
of aggregation on preference optimization.
B.5 Random-Effects Meta-analysis Formulation
We employ the DerSimonian–Laird random-effects estima-
tor (DerSimonian and Laird 1986) to synthesize results
across model architectures. For each condition, we pool ef-
fect sizes θi (differences between fine-tuned and control
models) using random-effects weights:
ˆθ =
Pk
i=1 w∗
i θi
Pk
i=1 w∗
i
,
w∗
i =
1
σ2
i + ˆτ 2
(12)

--- Page 18 ---\n\nwhere σ2
i is the within-model variance and ˆτ 2 is the esti-
mated between-model heterogeneity.
For pairwise comparisons between conditions (j, k), we
compute differences ˆδjk = ˆθj −ˆθk with associated variance:
Var(ˆδjk) =
1
P w∗(j)
i
+
1
P w∗(k)
i
(13)
Statistical significance is determined based on 95% confi-
dence intervals that exclude zero.
B.6 MMLU Evaluation Results
We evaluated seven models across 17 fine-tuning runs us-
ing 1000 MMLU questions. Baseline accuracy ranged from
23.6% (Guanaco-3B) to 56.9% (Llama-3-8B, Qwen3-14B).
Qwen3-14B was the most sensitive to fine-tuning, with
White EA DPO improving accuracy by +4.5% (61.4%)
and consensus selection reducing it by -5.5%. Rating-
scale effects varied by model: binary scales aided Wizard-
Vicuna-7B (+1.0%) but harmed Deep-Reasoning (-1.9%).
Data-selection strategies were likewise model-dependent,
with random sampling best for Guanaco-3B (+1.2%)
and majority-vote selection optimal for Llama models.
Conservative-aligned training had mixed influence (+1.5%
for Wizard-Vicuna-7B, negligible elsewhere).
The MMLU results are not an evaluation of our fine-
tuning task. MMLU covers general-knowledge and rea-
soning skills (math, science, history), which are unre-
lated to toxicity or emotional-awareness training. We report
MMLU only to show baseline model capability. Some mod-
els, such as Wizard-Vicuna-7B and Guanaco-3B, have low
general-knowledge scores, so their limitations come from
the base model rather than from our fine-tuning. The higher-
performing models (for example, Qwen3-14B and Llama-3-
8B) are therefore easier to interpret because they start from
a stronger overall capability.
Table 10: MMLU Accuracy:Deep-Reasoning-Llama-3.2-
Instruct-uncensored-3B
Variant
Accuracy (%)
vs Base (%)
Base Model
52.9
baseline
Demographics
Male Toxic DPO
51.0
-1.9
Female Toxic DPO
50.9
-2.0
Black EA DPO
52.3
-0.6
White EA DPO
52.1
-0.8
Conservative EA DPO
52.8
-0.1
Liberal EA DPO
53.1
+0.2
Rating Scales
5-points Toxic DPO
52.3
-0.6
3-points Toxic DPO
52.3
-0.6
Binary Toxic DPO
51.0
-1.9
Data Selection
Full Dataset (5-points)
52.3
-0.6
Majority Vote DPO
50.5
-2.4
Create Average DPO
51.7
-1.2
Keep Random DPO
51.1
-1.8
Full Consensus DPO
52.7
-0.2
Other Variants
EA DPO
52.5
-0.4
Toxic EA DPO
51.9
-1.0
Toxic EA GRPO
52.9
+0.0

--- Page 19 ---\n\nTable 11: MMLU Accuracy: Qwen3-14B-abliterated
Variant
Accuracy (%)
vs Base (%)
Base Model
56.9
baseline
Demographics
Male Toxic DPO
57.7
+0.8
Female Toxic DPO
59.6
+2.7
Black EA DPO
58.8
+1.9
White EA DPO
61.4
+4.5
Conservative EA DPO
57.5
+0.6
Liberal EA DPO
60.3
+3.4
Rating Scales
5-points Toxic DPO
59.4
+2.5
3-points Toxic DPO
58.9
+2.0
Binary Toxic DPO
56.3
-0.6
Data Selection
Full Dataset (5-points)
59.4
+2.5
Majority Vote DPO
53.3
-3.6
Create Average DPO
56.7
-0.2
Keep Random DPO
54.3
-2.6
Full Consensus DPO
51.4
-5.5
Other Variants
EA DPO
60.1
+3.2
Toxic EA DPO
59.1
+2.2
Toxic EA GRPO
57.1
+0.2
Table
12:
MMLU
Accuracy:
Wizard-Vicuna-7B-
Uncensored
Variant
Accuracy (%)
vs Base (%)
Base Model
31.5
baseline
Demographics
Male Toxic DPO
30.7
-0.8
Female Toxic DPO
31.4
-0.1
Black EA DPO
31.8
+0.3
White EA DPO
30.5
-1.0
Conservative EA DPO
33.0
+1.5
Liberal EA DPO
30.3
-1.2
Rating Scales
5-points Toxic DPO
29.7
-1.8
3-points Toxic DPO
31.5
+0.0
Binary Toxic DPO
32.5
+1.0
Data Selection
Full Dataset (5-points)
29.7
-1.8
Majority Vote Toxic DPO
31.0
-0.5
Create Average Toxic DPO
31.4
-0.1
Keep Random Toxic DPO
31.5
+0.0
Full Consensus Toxic DPO
31.5
+0.0
Other Variants
EA DPO
29.2
-2.3
Toxic EA DPO
31.0
-0.5
Toxic EA GRPO
31.5
+0.0
Table 13: MMLU Accuracy: Llama-3-8B-Lexi-Uncensored
Variant
Accuracy (%)
vs Base (%)
Base Model
56.9
baseline
Demographics
Male Toxic DPO
57.2
+0.3
Female Toxic DPO
56.3
-0.6
Black EA DPO
57.4
+0.5
White EA DPO
57.5
+0.6
Conservative EA DPO
55.8
-1.1
Liberal EA DPO
54.2
-2.7
Rating Scales
5-points Toxic DPO
56.4
-0.5
3-points Toxic DPO
55.3
-1.6
Binary Toxic DPO
57.2
+0.3
Data Selection
Full Dataset (5-points)
56.4
-0.5
Majority Vote Toxic DPO
57.6
+0.7
Create Average Toxic DPO
56.8
-0.1
Keep Random Toxic DPO
57.0
+0.1
Full Consensus Toxic DPO
57.0
+0.1
Other Variants
EA DPO
56.5
-0.4
Toxic EA DPO
55.6
-1.3
Toxic EA GRPO
56.9
+0.0
Table 14: MMLU Accuracy: Guanaco-3B-Uncensored
Variant
Accuracy (%)
vs Base (%)
Base Model
23.6
baseline
Demographics
Male Toxic DPO
22.8
-0.8
Female Toxic DPO
24.1
+0.5
Black EA DPO
23.7
+0.1
White EA DPO
24.0
+0.4
Conservative EA DPO
22.0
-1.6
Liberal EA DPO
23.8
+0.2
Rating Scales
5-points Toxic DPO
23.7
+0.1
3-points Toxic DPO
23.1
-0.5
Binary Toxic DPO
23.8
+0.2
Data Selection
Full Dataset (5-points)
23.7
+0.1
Majority Vote Toxic DPO
22.9
-0.7
Create Average Toxic DPO
23.2
-0.4
Keep Random Toxic DPO
24.8
+1.2
Full Consensus Toxic DPO
23.2
-0.4
Other Variants
EA DPO
23.3
-0.3
Toxic EA DPO
23.6
+0.0
GRPO Fine-tuned
23.6
+0.0

--- Page 20 ---\n\nTable 15: MMLU Accuracy: WizardVicuna-Uncensored-3B
Variant
Accuracy (%)
vs Base (%)
Base Model
24.8
baseline
Demographics
Male Toxic DPO
22.8
-2.0
Female Toxic DPO
24.5
-0.3
Black EA DPO
24.8
+0.0
White EA DPO
21.9
-2.9
Conservative EA DPO
23.2
-1.6
Liberal EA DPO
23.5
-1.3
Rating Scales
5-points Toxic DPO
26.0
+1.2
3-points Toxic DPO
23.1
-1.7
Binary Toxic DPO
22.2
-2.6
Data Selection
Full Dataset (5-points)
26.0
+1.2
Majority Vote Toxic DPO
23.3
-1.5
Create Average Toxic DPO
25.0
+0.2
Keep Random Toxic DPO
22.9
-1.9
Full Consensus Toxic DPO
21.8
-3.0
Other Variants
EA DPO
21.1
-3.7
Toxic EA DPO
25.6
+0.8
GRPO DPO
24.9
+0.1
Table 16: MMLU Accuracy: llama3.2-1b-uncensored-5000-
8epoch-lora
.
Variant
Accuracy (%)
vs Base (%)
Base Model
40.5
baseline
Demographics
Male Toxic DPO
40.1
-0.4
Female Toxic DPO
41.0
+0.5
Black EA DPO
40.4
-0.1
White EA DPO
40.2
-0.3
Conservative EA DPO
40.6
+0.1
Liberal EA DPO
38.9
-1.6
Rating Scales
5-points Toxic DPO
40.0
-0.5
5-points Toxic DPO
41.2
+0.7
Binary Toxic DPO
40.4
-0.1
Data Selection
Full Dataset (5-points)
40.0
-0.5
Majority Vote Toxic DPO
41.3
+0.8
Create Average Toxic DPO
40.4
-0.1
Keep Random Toxic DPO
41.2
+0.7
Full Consensus Toxic DPO
41.8
+1.3
Other Variants
EA DPO
40.2
-0.3
Toxic EA DPO
41.0
+0.5
Toxic EA GRPO
40.7
+0.2

--- Page 21 ---\n\nFigure 10: Experimental design overview. Systematic investigation of pluralistic alignment factors across four controlled ex-
periments varying demographic stratification, scale granularity, aggregation methods, and optimization algorithms.
\n```\n