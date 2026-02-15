---
title: "2025-Almheiri-Cross-Cultural Transfer of Commonsense Reasoning in LLMs Evidence - PDF Extract"
source_pdf: "2025-Almheiri-Cross-Cultural Transfer of Commonsense Reasoning in LLMs Evidence.pdf"
pages: 22
extracted_at: "2026-02-15T17:51:58.545531"
---

# PDF Extract: 2025-Almheiri-Cross-Cultural Transfer of Commonsense Reasoning in LLMs Evidence

**Source PDF:** 2025-Almheiri-Cross-Cultural Transfer of Commonsense Reasoning in LLMs Evidence.pdf
**Total Pages:** 22

---

## Content

```
--- Page 1 ---

Cross-Cultural Transfer of Commonsense Reasoning in LLMs:
Evidence from the Arab World
Saeed Almheiri∗
Rania Hossam∗
Mena Attia
Chenxi Wang
Preslav Nakov
Timothy Baldwin
Fajri Koto
Mohamed bin Zayed University of Artificial Intelligence
{saeed.y, rania.elbadry, mena.attia, chenxi.wang}@mbzuai.ac.ae
Abstract
Large language models (LLMs) often reflect
Western-centric biases, limiting their effective-
ness in diverse cultural contexts. Although
some work has explored cultural alignment,
the potential for cross-cultural transfer, using
alignment in one culture to improve perfor-
mance in others, remains underexplored. This
paper investigates cross-cultural transfer of
commonsense reasoning in the Arab world,
where linguistic and historical similarities co-
exist with local cultural differences. Using a
culturally grounded commonsense reasoning
dataset covering 13 Arab countries, we eval-
uate lightweight alignment methods such as
in-context learning and demonstration-based re-
inforcement (DITTO), alongside baselines like
supervised fine-tuning and direct preference
optimization. Our results show that merely
12 culture-specific examples from one coun-
try can improve performance in others by 10%
on average, within multilingual models. In
addition, we demonstrate that out-of-culture
demonstrations from Indonesia and US con-
texts can match or surpass in-culture align-
ment for MCQ reasoning, highlighting cultural
commonsense transferability beyond the Arab
world. These findings demonstrate that effi-
cient cross-cultural alignment is possible and
offer a promising approach to adapt LLMs to
low-resource cultural settings.
1
Introduction
Large language models (LLMs) are increasingly
being deployed across diverse cultural contexts, yet
they often reflect a Western-centric worldview, mis-
aligning with local customs, values, and norms of
non-Western cultures (Naous et al., 2024; Sadallah
et al., 2025; Wang et al., 2024). Prior studies have
explored broad East–West cultural misalignments
in LLMs (Naous et al., 2024), but little is known
∗Equal contribution
Before
After
Abeer prepares fesikh for lunch.
A. Abeer serves feskih with rice.
B. Abeer serves fesikh with bread.
C. Abeer serves fesikh with
couscous.
Egypt
UAE
culturally align
LLM using only
Egyptian data
Bakhita performed Al-Na'eesh at her wedding.
A. Al-Na'eesh is a traditional women's dance involving
dancing with sticks.
B. Al-Na'eesh is a traditional women's dance involving
coordinated leg movements.
C. Al-Na'eesh is a traditional women's dance involving
coordinated hair movements.
Abeer prepares fesikh for lunch.
A. Abeer serves feskih with rice.
B. Abeer serves fesikh with bread.
C. Abeer serves fesikh with
couscous.
Egypt
UAE
Bakhita performed Al-Na'eesh at her wedding.
A. Al-Na'eesh is a traditional women's dance involving
dancing with sticks.
B. Al-Na'eesh is a traditional women's dance involving
coordinated leg movements.
C. Al-Na'eesh is a traditional women's dance involving
coordinated hair movements.
Figure 1: An illustration of cross-cultural transfer: if
aligning an LLM with Egyptian data improves its per-
formance on UAE culture, cultural knowledge has been
transferred.
about how these models handle intra-regional cul-
tural variation, such as that found across the 22
Arab countries. For example, despite sharing lin-
guistic ties, Emirati culture differs significantly
from Egyptian or Syrian traditions in food, festivals,
and gender roles. However, most Arabic LLMs
are trained on translated English data or regionally-
aggregated corpora (Sengupta et al., 2023; Sadallah
et al., 2025), potentially flattening these cultural
distinctions.
A key challenge in aligning LLMs with country-
specific cultural knowledge is the uneven avail-
ability of data. High-population countries such
as Egypt provide vastly more online content than
arXiv:2509.19265v1  [cs.AI]  23 Sep 2025

--- Page 2 ---

Models
Arabic
Multilingual
Sampling Methods
Topic Stratified
Sampling
Single Topic
Compare different
experiments
Probing methods
Attention analysis
Impact of geographical
distance
Correlation
analysis
ArabCulture Dataset
In-Context
Learing
DITTO
1.train/test splits
2.set up different
configs for
training data
Evaluation
Alignment Methods
Experiments
Figure 2: This figure illustrates an overview of our alignment and evaluation pipeline. The ArabCulture dataset is
split into train/test subsets, aligned via either In-Context Learning or DITTO on different models with different
sampling methods, then evaluated and probed (stimulus, attention, correlation) to quantify cross-cultural transfer.
smaller ones like the UAE (114M vs. 1.3M popu-
lation) (Insight, 2025; United Nations Population
Fund, 2025), resulting in cultural underrepresenta-
tion. This disparity motivates a central question:
Can cultural knowledge from one country be trans-
ferred to benefit another with limited resources?
In this paper, we investigate the feasibility of
cross-cultural commonsense transfer within the
Arab world (see Figure 1). We focus on this region
because it combines a shared linguistic foundation
with rich cultural diversity, and because most ex-
isting Arabic LLMs are trained on aggregated or
translated data that risk obscuring local distinc-
tions. Specifically, we evaluate whether aligning
an LLM to the culture of one Arab country can
enhance its performance on others through two
lightweight alignment strategies: In-Context Learn-
ing (ICL) and Demonstration-based Iterative Task
Tuning Optimization (DITTO) (Shaikh et al., 2025)
(see Figure 2). While ICL is a strong few-shot base-
line, DITTO offers a reinforcement learning alter-
native that requires only a handful of high-quality
demonstrations, making it particularly suitable for
low-resource cultural domains.
We conduct experiments on the ArabCulture
dataset (Sadallah et al., 2025), covering 13 coun-
tries and 3.2k examples across domains such as
food, rituals, relationships, and social norms. Us-
ing only 12 culture-specific demonstrations per
source country, we evaluate transfer to unseen tar-
get cultures across four LLMs (Qwen2.5, Gemma-
2, ALLaM, and SILMA) (Team, 2024; Team et al.,
2024; Bari et al., 2025; Silma-AI, 2024). Beyond
performance, we examine whether cross-cultural
gains can be predicted from geographic proximity
or cross-country data similarity, and whether align-
ment reshapes latent cultural representations within
the models.
Our contributions are:
• We pioneer the use of DITTO for cultural
alignment, achieving up to 34% accuracy
gains in Arab commonsense reasoning MCQ
with only 12 demonstrations per country.
• We show that cross-cultural transfer is feasi-
ble: cultural knowledge from high-resource
countries improves LLM performance on cul-
turally distinct, low-resource ones.
• We perform probing and correlation analyses
to explain improvements with factors such
as geographic proximity and cultural similar-
ity modeling, and that targeted alignment en-
hances the linear separability of specific cul-
tures in the model’s latent space.
2
Related Work
2.1
Cultural Reasoning
While language models encode cultural knowledge,
they often overrepresent high-resource languages
and cultures (Shen et al., 2024; Wang et al., 2024;
Naous et al., 2024). To evaluate such biases, sev-
eral benchmarks have been introduced, including
cultural reasoning tasks for Indonesian (Koto et al.,

--- Page 3 ---

2024) and Arabic (Sadallah et al., 2025; Huang
et al., 2024; Mousi et al., 2025). These studies
show that LLMs struggle with cultural reasoning
compared to general commonsense reasoning in
English (Roemmele et al., 2011). For Arabic, avail-
able resources include ACVA (Huang et al., 2024),
which provides general true/false statements about
Arab culture as a whole, and AraDiCE (Mousi
et al., 2025), which covers cultural questions from
six Arab countries.
In this work, we rely on
ArabCulture (Sadallah et al., 2025), as it offers
the most comprehensive dataset in terms of scale
and country-level coverage.
Much of the prior work on Arabic cultural align-
ment has focused on evaluation benchmarks or
on large-scale pretraining approaches such as in-
struction fine-tuning (Sengupta et al., 2023; Bari
et al., 2025). However, none of these studies ex-
amine whether adapting an LLM to one culture
can improve—or potentially degrade—its perfor-
mance on another. This question is particularly
important in the Arab world, where countries share
linguistic and historical ties but maintain distinct
cultural practices. To explore this, we leverage
the ArabCulture dataset (Sadallah et al., 2025),
which provides fine-grained, country-level cultural
knowledge across 13 Arab countries, enabling us to
systematically study cross-cultural transfer within
the region.
2.2
Cultural Alignment Approaches
Recent work has explored improving the cultural
awareness of language models through alignment
techniques such as fine-tuning (Li et al., 2024) and
in-context learning via few-shot prompting (Wang
et al., 2024; AlKhamissi et al., 2024). Fine-tuning
can effectively adapt models to cultural data, but it
often requires substantial resources and risks catas-
trophic forgetting of prior knowledge (Choenni
et al., 2024; AlKhamissi et al., 2024). Reinforce-
ment learning provides an alternative by leverag-
ing feedback from a reward model to guide LLMs
with only a small set of demonstrations. Recent
preference-alignment methods such as Direct Pref-
erence Optimization (DPO: Rafailov et al. (2023))
and its extension DITTO (Shaikh et al., 2025)
demonstrate that iterative feedback can align mod-
els efficiently without large-scale data. Although
DITTO was originally developed for stylistic adap-
tation, we adopt it here for the novel task of cul-
tural alignment. Building on these approaches, we
30
40
50
60
70
Score (%)
Qwen2.5 7B-Instruct Performance
2
4
6
8
10
12
Number of Samples
40
50
60
70
Score (%)
ALLaM 7B-Instruct-preview Performance
ICL MCQ
ICL Completion
SFT MCQ
SFT Completion
DPO MCQ
DPO Completion
DITTO MCQ
DITTO Completion
Base MCQ (Model Specific)
Base Completion (Model Specific)
Figure 3: Sample efficiency of different alignment meth-
ods for cultural alignment, evaluated on multiple-choice
questions (MCQ) and completions using cultural demon-
strations from the UAE.
study how LLMs can be aligned with regional cul-
tural nuances while maintaining broader common-
sense reasoning, with a particular focus on the Arab
world. Specifically, we examine whether adapting
to the cultural knowledge of one country improves
or harms performance in others, and how factors
such as geographical distance or cultural similarity
influence cross-cultural generalization.
3
Methodology
We describe the data, alignment procedures (ICL
and DITTO), sampling strategies, and the evalua-
tion protocol for measuring cross-cultural transfer
(Figure 2). We emphasize ICL and DITTO be-
cause pilot experiments (Figure 3) showed they
surpassed instruction fine-tuning and vanilla DPO
on our tasks, warranting deeper exploration.
3.1
Arabic Culture Dataset
We use the ArabCulture dataset (Sadallah et al.,
2025), which consists of approximately 3,200 hand-
crafted cultural statements and the corresponding
multiple choice options (one correct, two incorrect).
The dataset spans 12 topics and 40+ subtopics from
13 countries grouped into 4 regions of the Arab
world (North Africa, Gulf region, Nile Valley, and
Levant). Each country subset consists of roughly
250 pairs of statements and choices. For each coun-
try, we split these 10% for training/alignment ex-
amples and 90% held-out for evaluation.

--- Page 4 ---

Country
Qwen2.5 7B-Inst
Gemma-2 9B-it
ALLaM 7B-Inst
SILMA 9B-Inst
Avg.
DITTO
ICL
DITTO
ICL
DITTO
ICL
DITTO
ICL
Comp. MCQ Comp. MCQ Comp. MCQ Comp.
MCQ Comp.
MCQ Comp.
MCQ Comp.
MCQ Comp.
MCQ
Algeria
0.19
16.74
2.80
18.50
−0.22
25.26
3.86
4.52
−0.31
1.57
3.99 −10.49
−0.88
2.14
1.82
0.79 4.39
Egypt
−0.09
17.56
2.39
19.67
−1.61
28.34
1.72
0.66
−2.77
−1.10
3.61 −25.32
−0.97 −1.22
0.03 −0.66 2.52
Jordan
−0.31
18.91
2.77
17.09
1.47
33.93
4.80
11.21
−4.84 −12.82
3.86
−4.84
1.13
1.57
2.07
3.11 4.94
KSA
−0.06
17.84
3.24
19.92
3.30
27.46
3.42
6.00
0.78
−1.91
3.14 −16.27
0.22
0.66
1.26
1.39 4.40
Lebanon
0.91
18.38
3.52
18.66
1.28
7.19
3.52 −0.03
0.34
3.71
3.99 −14.92
0.88 −3.01
0.63 −1.54 2.72
Libya
−0.12
15.11
3.27
16.71
0.37
33.55
2.38 −0.06
−2.07
−0.28
2.64 −13.22
0.82 −0.34
1.35 −6.97 3.32
Morocco
1.64
17.25
3.33
18.79
−0.41
13.70
3.77
6.91
−0.09
3.14
3.93 −11.72
1.13
2.71
1.89
3.49 4.34
Palestine
−0.03
17.97
1.45
18.03
0.31
24.94
3.42
0.47
−3.33
0.82
2.80 −19.76
0.38
2.05
1.54
0.00 3.19
Sudan
1.07
18.98
3.21
16.15
1.44
15.11
3.26
14.32
−1.67
1.73
3.20 −22.87
1.70
2.74
1.85
1.10 3.83
Syria
0.98
17.00
3.30
19.04
0.15
31.82
2.60
0.44
−1.45
2.55
4.21
−5.90
−0.28
1.95
0.57
3.40 5.02
Tunisia
−0.81
17.18
2.01
18.13
1.35
20.58
2.29
0.60
0.22
1.35
4.33 −18.60
0.28
2.33
0.38
0.35 3.25
UAE
1.07
16.84
3.99
16.81
2.38
28.15
3.55
1.57
−2.07
3.58
3.36 −11.84
1.70
2.20
2.04
2.27 4.73
Yemen
−0.91
18.57
2.14
12.00
−0.35
5.72
2.67
0.22
0.53
−0.50
2.86 −17.65
−0.12
0.44
0.63 −0.75 1.59
Avg.
0.27
17.56
2.88
17.65
0.73
22.75
3.17
3.60
−1.29
0.14
3.53 −14.88
0.46
1.09
1.24
0.46
Accuracy Baselines (Comp.%/MCQ%): Qwen2.5 (32.89/51.65), Gemma-2 (32.52/34.56), ALLaM (36.35/69.9), SILMA (32.39/70.81)
Table 1: Overall accuracy improvements for Arab cultural commonsense reasoning when training on country-specific
knowledge across different models with topic-based sampling. Results show performance on Completion and MCQ
tasks using DITTO and ICL methods. Green-colored values represent the top two improvements in each model
across MCQ and Completion.
3.2
Alignment Methods
We use two alignment methods for country-specific
cultural examples: in-context learning (ICL) and
DITTO, a lightweight DPO variant that itera-
tively prefers curated demonstrations (Rafailov
et al., 2023; Shaikh et al., 2025). DITTO is data-
efficient relative to SFT and full RLHF (Bai et al.,
2022), enabling alignment from few examples (Fig-
ure 3). In preliminary comparisons with SFT and
vanilla DPO, DITTO led on MCQ, while ICL was
stronger on completion tasks across Qwen-2.5-7B
and ALLaM-7B (Figure 3). We therefore study ICL
and DITTO in depth for cultural commonsense rea-
soning.
We evaluate four instruction-tuned baselines:
two multilingual models (Qwen-2.5-7B-Instruct
(Team, 2024), Gemma-2-9B-It (Team et al.,
2024)), and two Arabic-centric models (ALLaM-
7B-Instruct-preview (Bari et al., 2025) and SILMA-
9B-Instruct (Silma-AI, 2024)), enabling direct com-
parison between general multilingual pretraining
and Arabic-oriented models.
3.3
Demonstration Sampling
We adopt two in-context selection schemes for both
ICL and DITTO: topic-stratified (k = 12 per coun-
try, one per main topic) and food-focused (k = 12
from the food topic spanning its subtopics). In both
settings, the model conditions on the demonstra-
tions and selects the culturally appropriate comple-
tion for a held-out statement–choice pair. Demon-
strations are curated for coverage and cultural rele-
vance.
3.4
Evaluation
We quantify cultural alignment as the country-level
accuracy gain (aligned −baseline) for both MCQ
and completion using lm-eval framework (Gao
et al., 2024). For completion, accuracy is computed
from the log-likelihood of the gold continuation.
We then test whether gains track geography and
culture by computing Pearson correlations between
gains and (i) geographical distance, and (ii) cosine-
based cultural similarity. Finally, we report topic-
level breakouts.
4
Results
Our experiments reveal key findings across the four
language models, as evident from Table 1 and Ta-
ble 2, highlighting accuracy improvements when
training on data from one country and evaluating
across others. Each cell shows absolute percentage-
point gains relative to the respective baseline mod-
els.
Strong Cross-Cultural Transfer.
Training on
small demonstration sets from a single Arab coun-
try consistently improves model performance on
other Arab countries, that is, cross-cultural, aver-
aging 2–5% gains in MCQ and completion tasks
across models and methods. Interestingly, Syria
as a source country (“teacher”) results in the high-
est average improvement (5.02%) across all mod-
els and methods, followed by Jordan (4.94%) and
the UAE (4.73%). Furthermore, Jordan-trained

--- Page 5 ---

Country
Gemma-2 9B-it
SILMA 9B-Inst
Avg.
DITTO
ICL
DITTO
ICL
Comp. MCQ Comp. MCQ Comp. MCQ Comp. MCQ
Algeria
0.44 28.71
3.92
0.00 −0.03
1.86
1.54 −2.73
4.21
Egypt
−0.66 37.51
2.35
5.50 −0.03
2.27
0.00
2.49
6.18
Jordan
1.10 22.78
3.58 11.37
0.63
1.98
1.19
2.20
5.60
KSA
−1.26 30.88
1.54
4.46 −0.19
0.98
0.69
0.26
4.67
Lebanon
0.97 32.01
3.52
3.27
1.13
2.61
1.32
3.81
6.08
Libya
−0.85 20.77
2.23
2.45
0.10
2.36
1.19
1.79
3.76
Morocco
1.19 20.45
1.76
3.45 −1.10
3.46
0.69
1.89
3.97
Palestine
0.84 28.53
2.92
0.25 −0.34
2.55
1.13
1.64
4.69
Sudan
0.75 31.45
3.14
8.36 −0.28
1.73
1.19
3.08
6.18
Syria
0.00 37.38
2.82
8.20
0.72
0.69
0.85
2.61
6.66
Tunisia
−1.42 21.58
2.86
1.16
0.22
1.54
0.66
2.61
3.65
UAE
0.50 29.06
2.42 17.97 −0.34
3.24
0.10
2.45
6.93
Yemen
−0.91 18.66
2.26
4.59 −1.10 −0.18
0.28
1.86
3.18
Avg.
0.05 27.67
2.72
5.46 −0.05
1.93
0.83
1.84
Baselines: Gemma-2 (32.52/34.56), SILMA (32.39/70.81)
Table 2: Overall accuracy improvements in Arab cul-
tural commonsense reasoning when training on food-
based country-specific knowledge across different mod-
els. Results show performance on Completion and MCQ
tasks using DITTO and ICL methods. Bold and green
cells indicate top two MCQ and Completion values for
each model. Underlined marks second best.
Gemma-2 exhibits strong cross-cultural improve-
ments, yielding a 4.8% completion gain with ICL
and a 33.9% MCQ gain with DITTO. This cultural
transfer occurs despite the geographical and cul-
tural differences between countries, suggesting that
cultural knowledge effectively transfers across the
Arab region regardless of model architecture. Con-
sistent cross-cultural improvements suggest that
these models develop broader Arab cultural un-
derstanding rather than just memorizing country-
specific features.
Multilingual vs. Arabic-centric.
Table 1 shows
distinct patterns between multilingual models
(Qwen-2.5-7B-Instruct (Team, 2024), Gemma-2-
9B-It (Team et al., 2024)) and Arabic-centric
models (ALLaM-7B-Instruct (Bari et al., 2025),
SILMA-9B-Instruct (Silma-AI, 2024)). Given their
lower baselines, multilingual models—especially
Gemma-2—yield the largest MCQ gains (Gemma-
2: baseline 34.56; +22.75 pp with DITTO), surpass-
ing Qwen-2.5 (baseline 51.65; +17.56 pp) and both
Arabic-centric models. By contrast, ALLaM shows
the strongest improvement on completion (+3.53
pp with ICL) despite its higher baseline (36.35).
These results suggest that multilingual models
adapt more on culturally grounded MCQ with
demonstration-based alignment, whereas Arabic-
centric models obtain larger generative gains. No-
tably, Jordan’s data produces exceptional MCQ
gains for Gemma-2 (+33.93 pp), while Syria
yields the highest cross-model average improve-
ment (5.02 pp). The pattern persists under food-
based sampling (Table 2), though completion gaps
narrow; SILMA shows more balanced cross-task
gains, indicating that Arabic-centric models benefit
from fine-grained domain knowledge.
Performance Comparison of DITTO and ICL.
ICL yields small but consistent gains with few neg-
ative transfers, whereas DITTO reaches higher ceil-
ings—especially on MCQ—at the cost of greater
variance. On MCQ, DITTO is strongest with multi-
lingual models (e.g., Gemma-2: +22.75 pp overall;
+33.93 pp with Jordan), but occasional negative
transfers appear in Arabic-centric settings (e.g.,
SILMA-Lebanon: −3.01 pp), and ICL can also
hurt in some cases (ALLaM MCQ: −14.88 pp). For
completion, ICL consistently outperforms DITTO
across models (e.g., ALLaM: +3.53 pp with ICL
vs. −1.29 pp with DITTO). Overall, DITTO is
preferable for MCQ on multilingual models, while
ICL is the safer choice for completion; both are
sensitive to small demonstration sets.
This asymmetry suggests that DITTO’s iterative
preference updates better suit discriminative MCQ
settings in multilingual models, whereas in-context
demonstrations more effectively enhance gener-
ative completion, particularly for Arabic-centric
models. The gap narrows under food-based sam-
pling (Table 2), indicating that domain-specific ex-
amples reduce method-dependent variance. Abla-
tions (Appendix F) show that increasing the num-
ber of demonstrations lowers DITTO’s MCQ vari-
ance and mitigates negative transfer. In practice,
choose by task and model: use DITTO to maximize
MCQ gains, use ICL for more stable completion,
and increase demo counts to stabilize DITTO.
Transferability with Fine-Grained Sampling.
When alignment data is restricted to a single do-
main (food), cross-cultural effects remain strong
across methods as demonstrated in Table 2. Train-
ing on country-specific food-related examples can
yield notable accuracy improvements, with Syria
and the UAE showing the highest overall average
gains (6.66% and 6.93% respectively). The re-
sults demonstrate asymmetry in knowledge trans-
fer effectiveness. Lebanon consistently performs

--- Page 6 ---

Figure 4: Radar charts comparing topic-level improvements for ICL (left) and DITTO (right) methods across 12
cultural domains. Values represent average improvement in percentage points, with DITTO showing superior
performance in most topics, particularly structured social domains like Family Relationships and Agriculture.
well as a source of transfer learning, appearing in
the top performers for both Gemma-2 and SILMA
completion tasks.
Notably, MCQ tasks show
higher variability, with Gemma-2’s DITTO method
achieving remarkably strong improvements (aver-
aging 27.67% across countries), particularly when
trained on Syrian and Lebanese examples (37.38%
and 32.01%, respectively). For completion tasks,
Gemma-2 with ICL yields the strongest average im-
provement (2.72%), while SILMA benefits more
modestly but consistently across methods. These
findings indicate that the selection of fine-grained
demonstrations fosters robust cross-cultural adap-
tation, but the degree of reciprocity in knowledge
transfer varies substantially by country, model ar-
chitecture, and assessment method.
5
Analysis
5.1
Topic-wise Transfer
Cross-cultural transfer exhibits significant method-
ological and domain-specific variation,
with
DITTO achieving superior performance relative
to ICL (5.3% vs. 2.3% average improvement;
Figure 4). Cosine similarity analysis across 13
Arab countries reveals uniformly low within-topic
similarity scores, providing empirical evidence
of highly localized cultural knowledge structures
where idioms demonstrate maximum divergence
(0.04 average similarity) while agriculture and
family relationships exhibit comparatively greater
cross-cultural consistency (0.08 and 0.07 respec-
tively; Table 7). The relationship between cul-
tural diversity and transfer effectiveness reveals
unexpected complexity: domains with intuitively
high variability do not uniformly yield diminished
performance gains, as evidenced by death-related
cultural knowledge achieving substantial improve-
ments (+5.7% DITTO, +2.8% ICL) and family
relationships demonstrating robust transferability
(+6.0% DITTO, +3.1% ICL), while topics with low-
est similarity scores such as idioms (+3.0% DITTO,
+1.6% ICL) and food practices (+4.2% DITTO,
+1.3% ICL) produce the most limited gains across
both methods. Model architecture fundamentally
shapes transfer dynamics: multilingual models
(Qwen-2.5, Gemma-2) consistently generate posi-
tive improvements across all cultural domains with
performance peaks reaching +15.5% (Qwen-2.5
ICL in family relationships) and +14.4% (Gemma-
2 DITTO in death-related topics), whereas Arabic-
centric architectures exhibit pronounced asymmet-
ric responses with ALLaM demonstrating substan-
tial negative ICL sensitivity (ranging from −9.5%
in wedding topics to +4.5% in agriculture) while
maintaining consistently positive DITTO perfor-
mance across all domains, and SILMA achiev-
ing modest but stable cross-method improvements,
thereby establishing DITTO’s superiority for multi-
lingual frameworks and ICL’s preferential applica-
bility to Arabic-specialized models when avoiding
highly contextual domains.
5.2
Impact of Geographical Distance on
Cross-Cultural Transfer
Considering that Arab culture is often perceived
as homogeneous or grouped geographically into
regions (e.g. Gulf, Levant, North Africa, Nile Val-

--- Page 7 ---

ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
-0.17
-0.01
0.10
-0.09
-0.08
-0.28
-0.03
0.15
-0.19
0.09
-0.25
0.36
-0.50
-0.10
-0.16
0.40
-0.25
-0.10
-0.04
0.37
-0.11
-0.48
0.24
0.18
-0.21
-0.19
0.03
-0.02
-0.33
-0.05
0.02
0.18
-0.31
0.04
0.16
0.10
-0.24
-0.23
0.28
0.09
-0.08
-0.38
-0.17
-0.20
-0.44
0.26
-0.22
-0.02
-0.35
0.21
0.00
0.15
ALLaM 7B-Instruct
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
0.13
0.27
0.28
0.63
0.04
0.06
-0.00
0.08
-0.27
-0.44
-0.04
0.15
-0.09
-0.31
-0.25
-0.22
0.05
0.07
-0.20
-0.07
0.19
0.35
0.40
0.36
0.24
-0.04
-0.28
0.32
-0.20
0.16
-0.20
-0.30
-0.61
-0.38
0.06
-0.14
-0.06
0.12
-0.39
-0.34
-0.10
-0.17
0.34
0.25
-0.18
-0.43
-0.42
-0.36
0.03
-0.12
-0.17
0.05
SILMA 9B-Instruct
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
0.12
-0.31
-0.22
-0.12
-0.51
0.03
0.07
0.16
-0.27
0.18
-0.09
0.02
-0.61
0.07
0.07
0.17
-0.10
-0.51
0.08
0.09
0.17
-0.04
-0.16
-0.18
0.05
0.13
-0.32
-0.25
-0.17
-0.05
0.07
0.11
-0.49
-0.09
0.24
0.19
-0.26
0.03
0.06
0.15
0.00
-0.05
-0.18
-0.11
-0.38
0.09
-0.21
0.16
-0.52
0.15
-0.16
0.28
Qwen2.5B 7B-Instruct
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
0.52
0.65
-0.12
-0.09
-0.29
-0.05
-0.42
0.15
-0.32
-0.32
0.10
0.09
-0.31
-0.32
-0.28
0.05
-0.31
-0.28
0.23
0.25
0.32
0.24
0.32
0.04
0.50
0.53
0.14
-0.13
-0.26
-0.20
-0.24
0.19
-0.51
-0.54
0.33
0.09
-0.45
-0.29
-0.35
0.05
0.25
0.44
0.55
-0.19
-0.80
-0.50
-0.48
0.12
-0.49
-0.21
-0.49
0.12
Gemma-2 9B-Tt
0.4
0.3
0.2
0.1
0.0
0.1
0.2
0.3
0.6
0.4
0.2
0.0
0.2
0.4
0.6
0.6
0.5
0.4
0.3
0.2
0.1
0.0
0.1
0.2
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Figure 5: Pearson correlation between geographical distance from the training country and country-level accuracy
gain, across four train/eval settings (topic-based sampling).
ley), we used the geographical distances between
the capitals of each country shown in Table 5 in
Appendix A.2 and the accuracy improvements per
country over the baseline to calculate the Pearson
correlation between distance and accuracy improve-
ment for each country to measure the impact of ge-
ographical distance on cross-cultural transfer. The
average correlation coefficients across all countries
and training methods are shown in Table 8 (Ap-
pendix D) and a more detailed breakdown of the
results for all the models is shown in Figure 5.
The results reveal high variation in how the four
models perform across the 13 countries using dif-
ferent evaluation methods. The data shows that
performance varies not only by country but also
by testing approach, with ICL Completion gener-
ally producing the most varied results and DITTO
MCQ typically showing more positive correlation,
as shown in Table 8. Notable patterns include
the UAE consistently showing negative correlation
across most models, while Morocco tends toward
positive correlation, particularly with Gemma-2.
The Gemma-2 model exhibits the most extreme cor-
relation values, with correlation coefficients rang-
ing from −0.8 to 0.65. These disparities likely
reflect differences in cultural contexts, and poten-
tially imbalanced training data representation from
these regions, highlighting the challenges in devel-
oping language models that perform consistently
across diverse Arabic-speaking populations.
5.3
Cultural Similarity
We modeled cultural similarity using the 12 broad
topics (e.g., food, weddings, holiday activities) de-
fined in the Arab Culture dataset. For each country,
we obtain a single country-level embedding that
represents all country’s cultural data, then using
cosine similarity between these embeddings, we
quantify cultural similarity between the countries
as represented in Table 6 alongside details in the
Appendix A.3. We then calculated the Pearson cor-
relation between cosine similarity and accuracy im-
provement for each country for the different mod-
els. The detailed results are shown in Figure 14

--- Page 8 ---

Model
DITTO
ICL
Completion
MCQ
Completion
MCQ
ALLaM-7B-Inst
−0.191
−0.066
−0.014
−0.188
Qwen-2.5-7B-Inst
0.026
0.283
0.184
0.236
SILMA-9B-Inst
−0.084
−0.272
0.171
−0.052
Gemma-2-9B-It
−0.206
0.326
0.062
0.070
Table 3: Mean Pearson correlation across countries
between cosine similarity and accuracy improvement
across models for Completion and MCQ tasks.
in Appendix E. The consistently high similarities
(ranging between 0.72–0.89, averaging 0.85) sug-
gest high cultural overlap and help explain transfer-
ability between Arab countries. The multilingual
models exhibit positive average Pearson correla-
tion on MCQ tasks, as shown in Table 3. This
means that higher cosine similarity scores gener-
ally correlated with higher accuracy improvements
and thus, higher transferability. However, the Ara-
bic models displayed negative Pearson correlation,
which might be explained by the chosen sentence
embedding model, detailed in Appendix A.3, being
multilingual, therefore embeddings used to calcu-
late cosine similarity could be more aligned to the
multilingual LLMs’ embeddings than the Arabic-
centric LLMs.
5.4
Cross-Cultural Transfer Beyond Arab
Culture
Expanding upon exploring the effect of cross-
cultural transfer, we examined the use of cultural
demonstrations beyond the Arab world. We curated
12 demonstrations representing each of the two In-
donesian contexts (ID, Aceh & Papua) curated from
the IndoCulture dataset (Koto et al., 2024) and
additional handcrafted demonstrations represent-
ing US cultural contexts to evaluate training on
cultures beyond the Arab world. We aligned Qwen-
2.5-7B and Allam-7B using ICL and DITTO on
cultural contexts and evaluated on Arab cultural
commonsense reasoning to measure cross-cultural
transfer effect. The performance of Indonesian and
US demonstrations compared to Arab counterparts
is demonstrated in Table 4.
For Qwen-2.5-7B, MCQ accuracy jumps from
52% to 69–71% with ICL and 67–70% with
DITTO, averaging 69% and matching the aver-
age performance obtained by training on Arab con-
texts. Completion increases modestly, ID averages
1% lower than average Arab demonstrations while
US scores above in similar magnitude. ALLaM-
MCQ Scores (%)
Completion Scores (%)
Context
Base
ICL DiTTO
Base
ICL
DiTTO
Qwen-2.5-7B-Instruct
Arab LB
51.65
63.65
66.76
32.89
34.34
31.98
Papua (ID)
71.13
67.17
34.49
32.14
Arab AVG
69.30
69.21
35.77
33.16
Aceh (ID)
69.09
67.17
34.15
32.14
US
68.71
69.94
35.03
34.46
Arab UB
71.57
70.63
36.88
34.53
ALLaM-7B-Instruct-preview
Arab LB
69.90
44.58
57.08
36.35
38.99
31.51
Papua (ID)
71.22
71.88
37.76
36.44
Arab AVG
55.02
70.04
39.88
35.06
Aceh (ID)
65.63
72.60
38.14
37.29
US
65.63
73.28
38.71
38.91
Arab UB
65.06
73.61
40.68
37.13
Note: Base scores are constant across contexts.
LB & UB = Lower & Upper bound. ID contexts
(Aceh, Papua) are beyond arab cultures (ID =
Indonesian), while Arab contexts represent cultur-
ally proximate testing.
Table 4: Performance comparison between Qwen-2.5-
7B and ALLaM-7B Models trained on Indonesian and
US contexts and evaluated on Arab culture.
7B showed similar trends, with improvement in
MCQ achieved only using DITTO with non-Arab
contexts. However, in completion, non-Arab con-
texts exceeded Arab demonstrations using DITTO
whereas ICL performed better with in-culture con-
texts and delivered the highest completion gain
(+4.3%).
These results demonstrate that mini-
mal out-of-culture examples can rival in-culture
alignment for MCQ reasoning, though completion
generation still benefits the most from culturally
proximate demonstrations, underscoring that cul-
tural similarity is helpful but not a prerequisite for
valuable transfer. Further investigation of out-of-
culture demonstrations can be found in Appendix I.
5.5
Cultural Representation in Model Latent
Space
To understand how different Arab cultures are inter-
nally represented within the model, we conducted
a probing analysis across all layers of the Qwen
model, using both one-vs-all and multiclass lin-
ear classifiers to assess the linear separability of
cultural knowledge. The results are illustrated in
Figure 6.
In this part, our goal is to assess whether differ-
ent cultural representations are distinguishable in
the model’s latent space. To this end, we adopt
layer-wise probing, which enables a direct evalua-
tion of the linear separability of cultural represen-
tations across layers. This approach provides clear
insights into how cultural knowledge is internally

--- Page 9 ---

0
4
8
12
16
20
24
28
Layer
0.50
0.55
0.60
0.65
0.70
0.75
0.80
F1 Score (One-vs-All)
Sudan (One-vs-All)
Jordan (One-vs-All)
Palestine (One-vs-All)
Syria (One-vs-All)
UAE (One-vs-All)
Sudan (Multiclass)
Jordan (Multiclass)
Palestine (Multiclass)
Syria (Multiclass)
UAE (Multiclass)
0.0
0.1
0.2
0.3
0.4
F1 Score (Multiclass)
Cultural Uniqueness in Qwen-2.5-7B
Figure 6: F1 scores across model layers for different
countries using one-vs-all and multiclass classifiers.
encoded. Details of the probing experiments can
be found in Appendix H.
Our probing analysis shown in Figures 6 and 7
reveals that Qwen-2.5-7B encodes Arab cultures
with varying distinctness, showing high linear sep-
arability for Sudan and Jordan but much lower for
Palestine and Syria. Multiclass probing confirms
the difficulty of jointly distinguishing multiple cul-
tures, though Sudan and Jordan remain relatively
more separable. The results of other models can be
found in Appendix G, and they show similar dis-
tinctness. In other models, the separability for Jor-
dan, Sudan, and the UAE is relatively high, which
may originate from their adopting a lapped pre-
training corpus having more knowledge of these
countries. After UAE-specific alignment, only the
UAE showed improved cultural encoding, while
other countries remained largely unchanged, yet
reasoning performance improved across all coun-
tries. This suggests that targeted cultural alignment
can enhance specific representations while indi-
rectly benefiting generalization, offering a viable
path toward culturally adaptive NLP systems.
As to why the inference effects vary greatly be-
tween countries, one factor is the imbalance in
the LLM’s pretraining corpus, where countries
with larger populations and greater digital pres-
ence are more likely to be represented extensively
in pretraining data (Dunn et al., 2024). The layer-
wise probing results indicate that even before align-
ment, each country already exhibits a degree of cul-
tural representation in the model’s internal layers
as demonstrated in Figure 6. The alignment pro-
cess then shifts or reinforces these representations,
which we observe as changes in cultural separa-
bility across layers showcased in Figure 7. These
findings suggest that prior representation strength,
driven by pretraining exposure, affects a country’s
ability to serve as an effective source.
0
4
8
12
16
20
24
28
Layer
0.50
0.55
0.60
0.65
0.70
0.75
0.80
F1 Score
Cultural Uniqueness Before & After DiTTO
Sudan (Before)
Sudan (After)
UAE (Before)
UAE (After)
Syria (Before)
Syria (After)
Palestine (Before)
Palestine (After)
Figure 7: F1 scores across model layers for Sudan, UAE,
Syria, and Palestine before and after UAE-specific align-
ment on Qwen-2.5-7B.
6
Conclusion
Our study demonstrates that LLMs can effectively
achieve cross-cultural adaptation using lightweight
alignment methods such as ICL and DITTO, pro-
ducing consistent gains in Arab countries—even
with limited and culturally specific data.The results
of our experiments indicate strong cross-cultural
transfer, where training on one country’s dataset
can significantly improve accuracy in other coun-
tries, with gains often exceeding 15–20% across
multilingual models. Some country pairs show
modest gains even at large distances, while others
see minimal improvement despite close proximity,
suggesting that cultural proximity is not strictly
tied to geographic location. In contrast, we ob-
served an overall positive correlation between cul-
tural similarity and accuracy improvement across
multilingual models, suggesting greater transfer-
ability between countries that are more culturally
similar. Probing analyses further show that targeted
alignment enhances cultural encoding (e.g., for the
UAE) without harming overall performance, high-
lighting the feasibility and benefits of culturally
adaptive NLP in multilingual settings.
In general, our results highlight that lightweight
alignment methods can effectively align on the cul-
tural commonsense reasoning task by incorporating
region-specific cultural demonstrations. Whether
through ICL or DITTO, LLMs can learn robust
cultural representations that transfer to new coun-
tries. Therefore, this work reinforces the notion
that cross-cultural adaptation is feasible and bene-
ficial in multilingual NLP settings, particularly in
the Arab world.
7
Limitations
While our findings illuminate promising insights
into pathways of cross-cultural transfer, several

--- Page 10 ---

critical limitations constrain the scope of our con-
clusions.
Task Diversity.
Our primary focus was on the
evaluation of cultural multiple choice questions
and a completion task. The realm of open-ended
tasks (e.g., dialogue, narrative generation) intro-
duces additional layers of complexity for cross-
cultural alignment, underscoring the necessity for
a deeper investigation into how cultural knowledge
extrapolates across open-ended text generation.
Country Coverage
While there are 22 countries
that are members of the Arab League, the data set
we use only represents 13 of them, which although
more representative than other datasets, still does
not completely represent the Arab world. This fur-
ther underscores the point we bring up in the intro-
duction about the discrepancies in data availability
by country, and emphasizes the importance of in-
vestigating cross-cultural transfer in low-resource
settings.
Fine-Grained Cultural Nuances.
Our analysis
highlights performance variations even within topic
categories, such as family relationships and idioms.
In practice, cultural norms can be more nuanced
and context-dependent than captured by any small
demonstration set. A larger set of demonstrations
and supervised fine-tuning may be required to mas-
tering the intricacy of cultural knowledge that re-
quired memorization.
Despite these constraints, our work demonstrates
that meticulously chosen examples, irrespective of
being derived from broad topics or targeted do-
mains, can improve performance in varied cultural
settings. These findings pave the way for future
work that refines cross-cultural alignment strategies
and investigates the interplay between linguistic
diversity, cultural distance and similarity in multi-
lingual NLP.
References
Badr AlKhamissi,
Muhammad ElNokrashy,
Mai
Alkhamissi, and Mona Diab. 2024. Investigating
cultural alignment of large language models. In Pro-
ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 12404–12422, Bangkok, Thailand.
Association for Computational Linguistics.
Yuntao Bai, Andy Jones, Kamal Ndousse, Amanda
Askell, Anna Chen, Nova DasSarma, Dawn Drain,
Stanislav Fort, Deep Ganguli, Tom Henighan,
Nicholas Joseph, Saurav Kadavath, Jackson Kernion,
Tom Conerly, Sheer El-Showk, Nelson Elhage, Zac
Hatfield-Dodds, Danny Hernandez, Tristan Hume,
and 12 others. 2022. Training a helpful and harmless
assistant with reinforcement learning from human
feedback. Preprint, arXiv:2204.05862.
M Saiful Bari, Yazeed Alnumay, Norah A Alzahrani,
Nouf M Alotaibi, Hisham Abdullah Alyahya, Sultan
AlRashed, Faisal Abdulrahman Mirza, Shaykhah Z
Alsubaie, Hassan A Alahmed, Ghadah Alabduljab-
bar, and 1 others. 2025. ALLaM: Large language
models for Arabic and English. In Proceedings of
the Thirteenth International Conference on Learning
Representations, ICLR ’25, Singapore.
Rochelle Choenni, Anne Lauscher, and Ekaterina
Shutova. 2024. The echoes of multilinguality: Trac-
ing cultural value shifts during language model fine-
tuning. In Proceedings of the 62nd Annual Meeting
of the Association for Computational Linguistics (Vol-
ume 1: Long Papers), pages 15042–15058, Bangkok,
Thailand. Association for Computational Linguistics.
Jonathan Dunn, Benjamin Adams, and Harish Tay-
yar Madabushi. 2024. Pre-trained language mod-
els represent some geographic populations better
than others. In Proceedings of the 2024 Joint In-
ternational Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 12966–12976, Torino, Italia.
ELRA and ICCL.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Bider-
man, Sid Black, Anthony DiPofi, Charles Foster,
Laurence Golding, Jeffrey Hsu, Alain Le Noac’h,
Haonan Li, Kyle McDonell, Niklas Muennighoff,
Chris Ociepa, Jason Phang, Laria Reynolds, Hai-
ley Schoelkopf, Aviya Skowron, Lintang Sutawika,
and 5 others. 2024.
The language model evalua-
tion harness. https://github.com/EleutherAI/
lm-evaluation-harness/tree/v0.4.3.
Huang Huang, Fei Yu, Jianqing Zhu, Xuening Sun,
Hao Cheng, Song Dingjie, Zhihong Chen, Mosen
Alharthi, Bang An, Juncai He, Ziche Liu, Juny-
ing Chen, Jianquan Li, Benyou Wang, Lian Zhang,
Ruoyu Sun, Xiang Wan, Haizhou Li, and Jinchao Xu.
2024. AceGPT, Localizing large language models
in Arabic. In Proceedings of the 2024 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies (Volume 1: Long Papers), pages 8139–8163,
Mexico City, Mexico. Association for Computational
Linguistics.
Global
Media
Insight.
2025.
United
Arab
Emirates
(UAE)
Population
Statistics
2025.
https://www.globalmediainsight.com/
blog/uae-population-statistics/#UAE_
Population_by_Nationality_2025.
Accessed:
2025-05-20.
Fajri Koto, Rahmad Mahendra, Nurul Aisyah, and Tim-
othy Baldwin. 2024. IndoCulture: Exploring geo-

--- Page 11 ---

graphically influenced cultural commonsense reason-
ing across eleven Indonesian provinces. Transac-
tions of the Association for Computational Linguis-
tics, 12:1703–1719.
Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana
Sitaram, and Xing Xie. 2024. CultureLLM: Incorpo-
rating cultural differences into large language mod-
els. In Advances in Neural Information Processing
Systems, volume 37, pages 84799–84838. Curran As-
sociates, Inc.
Basel Mousi, Nadir Durrani, Fatema Ahmad, Md. Arid
Hasan, Maram Hasanain, Tameem Kabbani, Fahim
Dalvi, Shammur Absar Chowdhury, and Firoj Alam.
2025. AraDiCE: Benchmarks for dialectal and cul-
tural capabilities in LLMs. In Proceedings of the
31st International Conference on Computational Lin-
guistics, pages 4186–4218, Abu Dhabi, UAE. Asso-
ciation for Computational Linguistics.
Tarek Naous, Michael J Ryan, Alan Ritter, and Wei Xu.
2024. Having beer after prayer? Measuring cultural
bias in large language models. In Proceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 1: Long Papers), pages
16366–16393, Bangkok, Thailand. Association for
Computational Linguistics.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christo-
pher D Manning, Stefano Ermon, and Chelsea Finn.
2023. Direct preference optimization: Your language
model is secretly a reward model. In Proceedings of
the Thirty-seventh Conference on Neural Information
Processing Systems, NeurIPS ’23, New Orleans, LA,
USA.
Melissa Roemmele, Cosmin Adrian Bejan, and An-
drew S Gordon. 2011. Choice of plausible alterna-
tives: An evaluation of commonsense causal reason-
ing. In Proceedings of the AAAI Spring Symposium:
Logical Formalizations of Commonsense Reasoning,
pages 90–95, Stanford, CA, USA.
Abdelrahman Sadallah, Junior Cedric Tonga, Khalid
Almubarak, Saeed Almheiri, Farah Atif, Chatrine
Qwaider, Karima Kadaoui, Sara Shatnawi, Yaser
Alesh, and Fajri Koto. 2025.
Commonsense rea-
soning in Arab culture. In Proceedings of the 63rd
Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), pages 7695–
7710, Vienna, Austria. Association for Computa-
tional Linguistics.
Neha Sengupta, Sunil Kumar Sahu, Bokang Jia,
Satheesh Katipomu, Haonan Li, Fajri Koto, William
Marshall, Gurpreet Gosal, Cynthia Liu, Zhim-
ing Chen, Osama Mohammed Afzal, Samta Kam-
boj, Onkar Pandit, Rahul Pal, Lalit Pradhan,
Zain Muhammad Mujahid, Massa Baali, Xudong
Han, Sondos Mahmoud Bsharat, and 13 others. 2023.
Jais and Jais-chat: Arabic-centric foundation and
instruction-tuned open generative large language
models. Preprint, arXiv:2308.16149.
Omar Shaikh, Michelle S. Lam, Joey Hejna, Yijia Shao,
Hyundong Justin Cho, Michael S. Bernstein, and
Diyi Yang. 2025. Aligning language models with
demonstrated feedback. In Proceedings of the Thir-
teenth International Conference on Learning Repre-
sentations, ICLR ’25, Singapore.
Siqi Shen, Lajanugen Logeswaran, Moontae Lee,
Honglak Lee, Soujanya Poria, and Rada Mihalcea.
2024. Understanding the capabilities and limitations
of large language models for cultural commonsense.
In Proceedings of the 2024 Conference of the North
American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies
(Volume 1: Long Papers), pages 5668–5680, Mexico
City, Mexico. Association for Computational Lin-
guistics.
Silma-AI.
2024.
SILMA
9B
Instruct
v1.0.
https://huggingface.co/silma-ai/
SILMA-9B-Instruct-v1.0.
Gemma Team, Morgane Riviere, Shreya Pathak,
Pier Giuseppe Sessa, Cassidy Hardin, Surya Bhupati-
raju, Léonard Hussenot, Thomas Mesnard, Bobak
Shahriari, Alexandre Ramé, Johan Ferret, Peter Liu,
Pouya Tafti, Abe Friesen, Michelle Casbon, Sabela
Ramos, Ravin Kumar, Charline Le Lan, Sammy
Jerome, and 179 others. 2024. Gemma 2: Improving
open language models at a practical size. Preprint,
arXiv:2408.00118.
Qwen Team. 2024.
Qwen2.5: A party of founda-
tion models. https://qwenlm.github.io/blog/
qwen2.5/.
United Nations Population Fund. 2025. Egypt - world
population dashboard. https://www.unfpa.org/
data/world-population/EG. Accessed: 2025-05-
20.
Wenxuan Wang, Wenxiang Jiao, Jingyuan Huang, Ruyi
Dai, Jen-tse Huang, Zhaopeng Tu, and Michael Lyu.
2024. Not all countries celebrate Thanksgiving: On
the cultural dominance in large language models. In
Proceedings of the 62nd Annual Meeting of the As-
sociation for Computational Linguistics (Volume 1:
Long Papers), pages 6349–6384, Bangkok, Thailand.
Association for Computational Linguistics.
A
Technical Implementation Details
A.1
DITTO Configuration
We followed the standard DITTO implementation
provided in the original paper (Shaikh et al., 2025),
with these default hyperparameters now explicitly
listed for transparency: LoRA (rank 32, α=64);
SFT (batch 4, LR 3 × 10−5); DPO (batch 24 via
8×3 rescale, LR 1×10−6, β=0.05, 40 grad steps);
DITTO-specific (10 negatives, resample every 10
steps at temp 1.0; comparison sampling: 0.7 ex-
pert/0.2 replay/0.1 inter-model). This clarification

--- Page 12 ---

does not affect our methodological setup or con-
clusions, as our reported improvements rely on the
adaptation approach itself, not optimization varia-
tions.
A.2
Geographical Distance Matrix
Table 5 shows the approximate distances (in kilo-
meters) between the capitals of the 13 Arab coun-
tries used in our correlation analysis (Section 5.3).
These distances were calculated using the Haver-
sine formula based on geographical coordinates of
each capital city.
A.3
Cultural Similarity
Table
6
presents
the
cosine
similar-
ity
matrix
between
countries
based
on
cultural
embeddings
computed
using
paraphrase-multilingual-MiniLM-L12-v2.
These similarities were calculated by averaging
topic-level embeddings across the 12 cultural
domains for each country. Specifically, for each
country, we first obtained the sentence-level
embeddings for each cultural sample and found the
average embedding per topic. We then averaged
across all topics to get a single average embedding
per country. Then calculated the cosine similarity
for each country with the other countries to
represent cultural similarity between countries and
average across them as presented in the country
columns and last column of Table 6, respectively.
The high similarity values (0.72–0.89, averaging
0.85) indicate substantial cultural overlap across
Arab countries, supporting the feasibility of cross-
cultural transfer. Notably, Lebanon shows the low-
est average similarity (0.72), while Palestine and
Algeria show the highest (0.89), though these differ-
ences do not strongly predict transfer effectiveness
as discussed in Section 5.3.
B
Topic-Level Cultural Similarity
Analysis
Referenced in the main discussion (Section 5), we
hypothesized that topics like idioms and food are
inherently diverse and context-dependent, making
them harder to transfer across cultures compared
to more structured domains like family relation-
ships or agriculture, which we validated through
a comprehensive cosine similarity analysis exam-
ining within-topic cultural consistency across all
13 Arab countries in our dataset. For each cultural
topic, we computed pairwise cosine similarities be-
tween training examples from different countries
within the same topical domain by embedding each
cultural statement using a multilingual sentence
transformer and calculating the average cosine sim-
ilarity between all country pairs for each topic,
where lower similarity scores indicate greater cross-
cultural diversity within that topic while higher
scores suggest more consistent cultural patterns
across the Arab region. Our quantitative analysis,
presented in Table 7, provides strong empirical sup-
port for our theoretical framework, demonstrating
a clear hierarchy of cultural consistency where id-
ioms exhibit the lowest average similarity (0.04),
followed by food practices (0.06), while family
relationships (0.07) and agriculture (0.08) demon-
strate higher internal consistency across countries,
with this pattern holding remarkably stable across
all 13 countries and idioms showing the most re-
stricted similarity range (0.03-0.06) while agricul-
ture displays the greatest variability (0.06-0.13)
yet maintains the highest average. These findings
provide quantitative evidence that topics involv-
ing richer cultural nuances and linguistic speci-
ficity (idioms, food) require more extensive mem-
orization and contextual grounding, making them
less amenable to lightweight alignment approaches,
while more structured domains with clearer cross-
cultural regularities (family relationships, agricul-
ture) demonstrate greater transferability potential,
aligning with our observed performance patterns in
the main results.
C
Detailed Topic-Level Performance
Analysis
This section provides comprehensive performance
breakdowns for both DITTO and ICL alignment
methods across all 12 cultural topics and 4 lan-
guage models, supporting the topic-wise transfer
analysis presented in Section 5 and corresponding
to the radar chart visualizations in Figure 4, where
performance improvements were calculated as per-
centage point differences between aligned model
accuracy and baseline model accuracy for each cul-
tural topic using country-specific demonstrations
from the ArabCulture dataset. The detailed re-
sults reveal several critical patterns: DITTO demon-
strates superior average performance (+5.3%) com-
pared to ICL (+2.3%) while exhibiting lower vari-
ance and fewer negative transfers, with multilingual
models consistently outperforming Arabic-centric
models across both alignment methods where

--- Page 13 ---

From/To
Morocco
Algeria
Tunisia
Libya
Egypt
Sudan
Palestine
Jordan
Syria
Lebanon
KSA
UAE
Yemen
Morocco
0
948
1,569
1,859
3,596
4,435
3,913
3,968
3,958
3,876
5,234
5,946
5,493
Algeria
948
0
630
1,016
2,706
3,755
2,996
3,048
3,027
2,944
4,340
5,032
4,695
Tunisia
1,569
630
0
518
2,090
3,245
2,368
2,419
2,397
2,314
3,717
4,403
4,117
Libya
1,859
1,016
518
0
1,739
2,753
2,077
2,135
2,148
2,071
3,377
4,098
3,680
Egypt
3,596
2,706
2,090
1,739
0
1,596
432
494
613
485
1,639
2,363
2,104
Sudan
4,435
3,755
3,245
2,753
1,596
0
1,794
1,821
1,997
2,027
1,738
2,426
1,201
Palestine
3,913
2,996
2,368
2,077
432
1,794
0
63
213
234
1,369
2,036
2,039
Jordan
3,968
3,048
2,419
2,135
494
1,821
63
0
177
219
1,328
1,984
2,027
Syria
3,958
3,027
2,397
2,148
613
1,997
213
177
0
86
1,408
2,019
2,170
Lebanon
3,876
2,944
2,314
2,071
485
2,027
234
219
86
0
1,494
2,107
2,240
KSA
5,234
4,340
3,717
3,377
1,638
1,738
1,369
1,328
1,408
1,494
0
773
1,070
UAE
5,946
5,032
4,403
4,098
2,363
2,426
2,036
1,984
2,019
2,107
773
0
1,467
Yemen
5,493
4,695
4,117
3,680
2,104
1,201
2,039
2,027
2,170
2,240
1,070
1,467
0
Table 5: Geographical distances (km) between Arab country capitals used for correlation analysis with cross-cultural
transfer performance.
Morocco
Algeria
Tunisia
Libya
Egypt
Sudan
Palestine
Jordan
Syria
Lebanon
KSA
UAE
Yemen
Avg.*
Morocco
1.00
0.89
0.84
0.92
0.87
0.95
0.92
0.76
0.83
0.81
0.85
0.84
0.79
0.86
Algeria
0.89
1.00
0.77
0.91
0.92
0.92
0.94
0.91
0.94
0.71
0.95
0.91
0.94
0.89
Tunisia
0.84
0.77
1.00
0.83
0.76
0.84
0.82
0.70
0.74
0.85
0.71
0.76
0.68
0.77
Libya
0.92
0.91
0.83
1.00
0.85
0.93
0.95
0.85
0.88
0.73
0.88
0.86
0.86
0.87
Egypt
0.87
0.92
0.76
0.85
1.00
0.89
0.90
0.89
0.89
0.72
0.93
0.93
0.91
0.87
Sudan
0.95
0.92
0.84
0.93
0.89
1.00
0.93
0.79
0.86
0.79
0.87
0.86
0.85
0.87
Palestine
0.92
0.94
0.82
0.95
0.90
0.93
1.00
0.88
0.89
0.77
0.92
0.91
0.88
0.89
Jordan
0.76
0.91
0.70
0.85
0.89
0.79
0.88
1.00
0.92
0.62
0.94
0.90
0.94
0.84
Syria
0.83
0.94
0.74
0.88
0.89
0.86
0.89
0.92
1.00
0.64
0.92
0.87
0.93
0.86
Lebanon
0.81
0.71
0.85
0.73
0.72
0.79
0.77
0.62
0.64
1.00
0.66
0.73
0.61
0.72
KSA
0.85
0.95
0.71
0.88
0.93
0.87
0.92
0.94
0.92
0.66
1.00
0.92
0.96
0.88
UAE
0.84
0.91
0.76
0.86
0.93
0.86
0.91
0.90
0.87
0.73
0.92
1.00
0.91
0.87
Yemen
0.79
0.94
0.68
0.86
0.91
0.85
0.88
0.94
0.93
0.61
0.96
0.91
1.00
0.85
Table 6: Cosine similarity matrix between countries based on cultural embeddings. Higher values indicate greater
cultural similarity. *Diagonal values (1.0) excluded from average calculation.
Qwen-2.5 and Gemma-2 show complementary
strengths, particularly with Gemma-2 achieving the
highest individual improvements in death-related
topics (+14.4%) and family relationships (+13.6%)
under DITTO, while Qwen-2.5 demonstrates ex-
ceptional ICL performance reaching +15.5% in
family relationships, whereas Arabic-centric mod-
els show pronounced variability with ALLaM ex-
hibiting consistent negative transfers across most
ICL topics (ranging from -2.1% to -9.5%) while
maintaining positive DITTO performance, and
SILMA achieving modest but stable improvements
across both methods. Topic-specific effects are pro-
nounced across both alignment approaches, with
family relationships and parenting showing the
highest transferability, death-related topics demon-
strating substantial improvements despite cultural
variation, while idioms and food practices exhibit
the most limited improvements, and model archi-
tecture significantly influences alignment method
effectiveness, suggesting that Arabic-centric mod-
els may require different optimization strategies for
cultural alignment tasks compared to multilingual
architectures that demonstrate robust cross-topic
adaptability.
D
Correlation between Geographical
Distance and Accuracy Improvement
Table 8 and Table 9 show the overall means and me-
dian correlation scores across models and settings.
Figures 8, 9, 10, and 11 show the correlation scores
for the 4 models (Qwen-2.5-7B-Instruct, ALLaM-
7B-Instruct, SILMA-9B-Instruct, and Gemma-2-
9B-It), which are also displayed in heatmaps in Fig-
ure 5. To demonstrate what the correlation looks
like, Figure 12 shows the accuracy improvement vs.
distance graph for the strongest correlation, while
Figure 13 is for the weakest correlation.

--- Page 14 ---

Country
Agriculture
Family
Food
Idioms
Algeria
0.09
0.08
0.05
0.05
Egypt
0.09
0.07
0.07
0.04
Jordan
0.13
0.06
0.07
0.03
KSA
0.10
0.05
0.08
0.04
Lebanon
0.07
0.08
0.06
0.04
Libya
0.08
0.09
0.08
0.04
Morocco
0.09
0.05
0.05
0.03
Palestine
0.09
0.04
0.05
0.03
Sudan
0.07
0.10
0.05
0.06
Syria
0.06
0.05
0.08
0.03
Tunisia
0.06
0.08
0.05
0.04
UAE
0.07
0.09
0.05
0.05
Yemen
0.07
0.08
0.06
0.04
Average
0.08
0.07
0.06
0.04
Table 7: Within-topic cosine similarity scores across
13 Arab countries for selected cultural domains. Lower
scores indicate greater cross-cultural diversity within
the topic.
Model
DITTO
ICL
Completion
MCQ
Completion
MCQ
ALLaM-7B-Inst
−0.094
0.128
−0.251
−0.002
Qwen-2.5-7B-Inst
−0.029
0.052
−0.228
−0.056
SILMA-9B-Inst
−0.067
0.032
−0.064
−0.069
Gemma-2-9B-it
−0.065
0.056
−0.166
−0.054
Table 8: Mean Pearson correlation across countries be-
tween distance and accuracy improvement across mod-
els for Completion and MCQ tasks.
E
Correlation between Cultural
Similarity and Accuracy Improvement
Table 10 shows the overall median correlation
scores across models and settings to supplement the
means in Table 3. Figure 14 shows the correlation
scores for all the models across all the countries.
Model
DITTO
ICL
Completion
MCQ
Completion
MCQ
ALLaM-7B-Inst
-0.2825
-0.0152
0.0262
-0.1653
Qwen-2.5-7B-Inst
0.0158
0.2304
0.1951
0.1963
SILMA-9B-Inst
-0.1067
-0.3007
0.1964
0.0191
Gemma-2-9B-It
-0.2711
0.3135
-0.0042
0.0547
Table 10: Median Pearson correlation between distance
and accuracy improvement across models for Comple-
tion and MCQ tasks.
F
Negative Transfer Effects
Due to the nature of ditto iterative alignment, es-
pecially with small demonstration sets, can result
in sensitivity to intermediate model outputs and
the initial demonstrations selected, causing vari-
able transfer effects. To investigate this, we con-
Model
DITTO
ICL
Completion
MCQ
Completion
MCQ
ALLaM-7B-Inst
−0.099
0.149
−0.242
0.003
Qwen-2.5-7B-Inst
0.031
0.115
−0.264
−0.086
SILMA-9B-Inst
−0.042
0.048
−0.055
−0.174
Gemma-2-9B-It
−0.212
0.087
−0.310
−0.118
Table 9: Median Pearson correlation between distance
and accuracy improvement across models for Comple-
tion and MCQ tasks.
0.6
0.4
0.2
0.0
0.2
Pearson Correlation
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Pearson Correlation between Distance and 
Accuracy Improvement (Qwen2.5B 7B-Instruct)
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Figure 8: Pearson correlation coefficient between dis-
tance from training country and evaluation accuracy im-
provement for four different train/eval methods (Qwen-
2.5-7B-Instruct base model).
ducted an additional targeted experiment increas-
ing demonstrations from 12 (topic-based) to 100
(randomly sampled), summarized in Table 11.
We find that increasing demonstrations reduces
MCQ transfer variability (1.13→0.48) and main-
tains the same low variability in completion tasks
(0.62→0.66), confirming our hypothesis that larger
demonstration sets improve robustness. However,
our primary motivation remains data-efficient align-
ment and potential mitigation strategies (e.g., care-
ful curation or slightly increasing samples) can help
control variability and negative transfer. Detailed
scores breakdown are listed in Table 12.
G
Cultural Representation in Models
0
4
8
12
16
20
24
28
32
Layer
0.5
0.6
0.7
0.8
0.9
F1 Score (One­vs­All)
Sudan (One­vs­All)
Jordan (One­vs­All)
Palestine (One­vs­All)
Syria (One­vs­All)
UAE (One­vs­All)
Sudan (Multiclass)
Jordan (Multiclass)
Palestine (Multiclass)
Syria (Multiclass)
UAE (Multiclass)
0.0
0.2
0.4
0.6
0.8
1.0
F1 Score (Multiclass)
Cultural Uniqueness in ALLaM­7B­Instruct­preview
Figure 15: F1 scores across model layers for different
countries using one-vs-all and multiclass classifiers.

--- Page 15 ---

0.4
0.2
0.0
0.2
0.4
Pearson Correlation
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Pearson Correlation between Distance and 
Accuracy Improvement (ALLaM 7B-Instruct-preview)
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Figure 9:
Pearson correlation coefficient between
distance from training country and evaluation accu-
racy improvement for four different train/eval methods
(ALLaM-7B-Instruct-preview base model).
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Pearson Correlation
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Pearson Correlation between Distance and 
Accuracy Improvement (SILMA 9B-Instruct)
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Figure 10: Pearson correlation coefficient between dis-
tance from training country and evaluation accuracy im-
provement for four different train/eval methods (SiLMA-
9B-Instruct base model).
0
4
8
12
16
20
24
28
32
36
40
Layer
0.5
0.6
0.7
0.8
0.9
F1 Score (One­vs­All)
Sudan (One­vs­All)
Jordan (One­vs­All)
Palestine (One­vs­All)
Syria (One­vs­All)
UAE (One­vs­All)
Sudan (Multiclass)
Jordan (Multiclass)
Palestine (Multiclass)
Syria (Multiclass)
UAE (Multiclass)
0.0
0.1
0.2
0.3
0.4
F1 Score (Multiclass)
Cultural Uniqueness in gemma­2­9b­it
Figure 16: F1 scores across model layers for different
countries using one-vs-all and multiclass classifiers.
0.8
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Pearson Correlation
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Pearson Correlation between Distance and 
Accuracy Improvement (gemma-2 9b-it)
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Figure 11: Pearson correlation coefficient between
distance from training country and evaluation accu-
racy improvement for four different train/eval methods
(Gemma-2-9B-It base model).
0
1000
2000
3000
4000
5000
6000
Distance from UAE (km)
0
2
4
6
Accuracy Improvement (%)
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Accuracy Improvement vs Distance
(Trained on UAE)
Figure 12: Evaluation accuracy improvement vs. dis-
tance for ICL topic-based training on samples from
the UAE with Completion evaluation (Gemma-2-9B-It).
Pearson correlation = −0.797.
0
4
8
12
16
20
24
28
32
36
40
Layer
0.50
0.55
0.60
0.65
0.70
0.75
0.80
0.85
F1 Score (One­vs­All)
Sudan (One­vs­All)
Jordan (One­vs­All)
Palestine (One­vs­All)
Syria (One­vs­All)
UAE (One­vs­All)
Sudan (Multiclass)
Jordan (Multiclass)
Palestine (Multiclass)
Syria (Multiclass)
UAE (Multiclass)
0.0
0.1
0.2
0.3
0.4
F1 Score (Multiclass)
Cultural Uniqueness in SILMA­9B­Instruct­v1.0
Figure 17: F1 scores across model layers for different
countries using one-vs-all and multiclass classifiers.
H
Probing Experiment Details
In our probing experiments, the input to the model
is a task-specific prompt constructed for each exam-
ple, including the cultural statement and candidate
responses.
For each layer, we extract the hidden state of
the final token in the prompt, which corresponds

--- Page 16 ---

0
1000
2000
3000
4000
5000
Distance from Yemen (km)
22.5
20.0
17.5
15.0
12.5
10.0
7.5
Accuracy Improvement (%)
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Accuracy Improvement vs Distance
(Trained on Yemen)
Figure 13: Evaluation accuracy improvement vs. Dis-
tance for ICL topic-based training on samples from
Yemen with MCQ Evaluation (ALLaM-7B-Instruct-
preview). Pearson correlation = 0.003.
Setup
MCQ
Completion
12 topic-based demos
1.13
0.62
100 random demos
0.48
0.66
Table 11: Variance comparison between topic-based and
random demonstration setups for MCQ and Completion
tasks using Ditto on Qwen-2.5-7B-Instruct.
to the last token of the full input sequence. This
token’s hidden state serves as the representation of
the model’s internal encoding for that input. We
will include this experimental detail in the camera-
ready version of the paper.
To better understand this, we provide a example
that illustrates the probing process step by step,
from input text to cultural classification:
This raw input is formatted into the following
prompt (as used in our experiments):
You are tasked with selecting the most culturally appropriate
option based on the context provided below.
Location: None
Statement: When there is a success or a happy occasion, the
mother is keen to cook a dessert as a good omen.
Consider the cultural nuances of the specified location and
choose the most suitable response from the options pro-
vided.
Options:
A: The mother prepares date cookies.
B: The mother prepares beverages.
C: The mother kneads khfaf.
Typically, the pipeline is as follows:
1. LLM Encoding: We feed this prompt into
a large language model, which produces high-
dimensional hidden representations (tensors) for
each token across all layers.
2. Representation Extraction: From each layer,
we extract the hidden state of the final token in the
prompt, resulting in a fixed-size vector (typically
of shape d × 1).
3. Probing Classifier: This vector is passed into
a logistic classifier trained to map the internal rep-
resentation to a cultural class label. In this example,
the correct label is Algeria.
I
Cross-Cultural Transfer Beyond Arab
cultures
Data & Training.
For Indonesian contexts, we
selected Aceh & Papua provinces based on geo-
graphical location/distance, since Aceh represents
the westernmost province and Papua the western-
most. Data are curated from the Indoculture dataset
(Koto et al., 2024) with 12 demonstrations selected
representing one per topic. For US culture, we cu-
rated 12 human-written cultural samples (one per
topic) to represent the US cultural context. These
samples were used to fine-tune the model, which
was then evaluated on Arab cultural tasks.
US Culture.
As represented in Section 5.4, US
contexts achieve the highest observed performance
gains compared to other non-arab contexts. This
shows that training with US cultural samples is
transferred positively to Arab cultural tasks across
both models. For Qwen-2.5-7B, the US achieved
a MCQ accuracy of 68.71% with ICL and 69.94%
with DiTTO, comparable to the average and lower
bound of the Arab contexts. Similarly, for ALLaM-
7B, the US reached 65.63% (ICL) and 73.28%
(DiTTO), closely matching the Arab Upper Bound.
The US context outperformed other non-Arab
cultures, such as Indonesian contexts, indicating
that cultural transfer can be observed in west-
ern contexts. For completion tasks, the improve-
ments were more modest. Qwen-2.5-7B, the US
achieved 35.03% with ICL, similar to the Arab
Lower Bound, while DiTTO (34.46%) was able to
match the Arab Upper Bound. In ALLaM-7B, the
US achieved 38.71% (ICL) and 38.91% (DiTTO),
which are slightly below the Arab Upper Bound.
This suggests that while US cultural samples trans-
fer well in MCQ tasks, their impact on completion
tasks is more limited.
To understand why US cultural contexts trans-
fer effectively, we assessed the curated samples,
where 7 of 12 samples are non-conflicting with
Arab culture values or country-specific to the US,
suggesting that compatibility and relevance of cer-
tain US cultural elements with Arab cultural values

--- Page 17 ---

ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
-0.34
-0.28
-0.04
-0.02
-0.20
-0.35
-0.48
-0.42
0.06
-0.53
0.46
-0.41
0.06
-0.11
-0.04
0.19
-0.33
0.23
-0.25
-0.14
-0.02
0.09
-0.25
-0.02
0.06
-0.36
-0.58
-0.28
-0.05
-0.41
-0.61
-0.11
0.03
0.03
-0.71
0.01
0.13
-0.11
0.15
-0.01
0.20
0.21
0.16
0.13
0.00
-0.49
-0.08
0.07
0.22
-0.40
-0.17
0.15
ALLaM 7B-Instruct
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
0.32
-0.15
-0.23
-0.21
0.03
-0.19
-0.53
-0.59
0.48
0.22
0.03
-0.12
0.50
-0.25
0.25
-0.31
-0.51
-0.13
0.51
0.11
0.47
0.07
-0.45
-0.30
0.01
0.03
0.30
-0.31
0.20
-0.11
-0.09
-0.40
0.26
0.01
0.06
-0.35
0.40
-0.08
-0.07
0.02
-0.09
-0.20
0.02
-0.30
0.19
0.08
0.08
-0.18
-0.04
-0.38
-0.55
-0.60
SILMA 9B-Instruct
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
0.20
-0.14
0.10
0.21
0.53
0.14
0.27
0.34
0.12
-0.03
0.20
0.04
0.20
0.19
0.26
0.18
-0.03
-0.09
-0.03
0.23
0.16
-0.11
0.54
0.44
0.04
0.07
0.60
0.59
0.28
0.02
0.47
0.65
-0.01
0.27
0.14
0.54
-0.02
0.02
0.06
0.03
0.33
0.14
-0.08
0.14
0.38
-0.06
0.41
0.26
0.20
-0.07
0.12
0.03
Qwen2.5B 7B-Instruct
ICL Completion
DITTO Completion
ICL MCQ
DITTO MCQ
Algeria
Egypt
Jordan
KSA
Lebanon
Libya
Morocco
Palestine
Sudan
Syria
Tunisia
UAE
Yemen
Country
-0.00
-0.18
0.28
0.61
-0.01
-0.31
0.24
0.22
0.26
-0.09
-0.00
0.40
0.04
-0.27
0.23
0.27
-0.07
0.11
-0.23
-0.15
-0.06
-0.29
-0.08
0.69
-0.17
-0.39
-0.01
0.31
0.14
-0.40
0.05
0.64
-0.09
-0.28
0.21
0.54
-0.06
-0.32
0.12
0.52
0.14
-0.27
-0.21
-0.12
0.47
0.07
-0.06
0.26
0.21
-0.07
0.36
0.04
Gemma-2 9B-Tt
0.6
0.4
0.2
0.0
0.2
0.4
0.6
0.4
0.2
0.0
0.2
0.4
0.1
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Figure 14: Pearson correlation between cosine-based cultural similarity to the training country and country-level
accuracy gain across four train/eval settings (topic-based sampling).
may contribute to the effective transfer across these
contexts.
Indonesian Contexts
(Out-of-Culture)
Arabic Contexts
(In-Culture)
0
20
40
60
80
MCQ Score (%)
Multiple-Choice QA Tasks
Indonesian Contexts
(Out-of-Culture)
Arabic Contexts
(In-Culture)
0
10
20
30
40
Completion Score (%)
Completion Tasks
Qwen2.5 7B-Instruct
Base
ICL
DiTTO
ALLaM 7B-Instruct-preview
Base
ICL
DiTTO
Cross-Cultural Transfer through Training on Out-of-Culture (Indonesian)
Figure 18: Performance comparison between Qwen-
2.5-7B and ALLaM-7B Models trained on Indonesian
contexts and evaluated on Arab culture.
J
Detailed Results

--- Page 18 ---

Trained on (country)
MCQ (Topic, n=12)
Completion (Topic)
MCQ (100 Random)
Completion (100 Random)
Base (No training)
51.65
32.89
51.42
32.36
Algeria
68.39
33.08
71.13
30.52
Egypt
69.21
32.80
69.89
31.39
Jordan
70.56
32.58
70.76
32.58
KSA
69.49
32.83
71.45
32.95
Lebanon
70.03
33.80
71.04
30.75
Libya
66.76
32.77
70.62
32.31
Morocco
68.90
34.53
70.67
32.08
Palestine
69.62
32.86
70.99
31.81
Sudan
70.63
33.96
70.49
33.27
Syria
68.65
33.87
71.40
31.62
Tunisia
68.83
32.08
71.36
31.39
UAE
68.49
33.96
68.93
31.81
Yemen
70.22
31.98
70.44
31.16
Average
69.21
33.16
70.70
31.82
Variance
1.13
0.62
0.48
0.66
Table 12: Effect of sample count on performance variability on Qwen-2.5-7B-Instruct using DITTO, comparing
topic-based (12 samples) vs random (100 samples). Note: Performance scores are listed for variance calculation.
Comparing scores between sampling methods is not equivalent due to differing unseen evaluation sets.
Topic
ALLaM
Qwen
Gemma
SILMA
Agriculture
+4.2
+3.4
+12.9
+1.8
Art
+1.4
+3.0
+11.6
+1.8
Daily Activities
+0.5
+10.7
+10.9
+0.2
Death
−1.4
+10.2
+14.4
−0.5
Family Relations
−3.4
+13.5
+13.6
+0.3
Food
−2.2
+7.7
+10.5
+0.8
Habits
−1.6
+10.0
+13.7
+1.1
Holiday Activities
−1.8
+9.6
+13.7
+1.4
Idioms
+1.7
+5.3
+4.4
+0.5
Parenting
+4.5
+9.4
+9.7
+0.1
Traditional Games
+1.4
+9.7
+10.9
+0.3
Wedding
−1.9
+10.1
+11.4
+1.1
Average
+0.1
+9.4
+11.9
+0.7
Table 13: DITTO performance improvements (%).
Topic
ALLaM
Qwen
Gemma
SILMA
Agriculture
−2.2
+3.0
+3.4
−1.4
Art
−3.8
+4.3
+1.6
−1.2
Daily Activities
−5.5
+12.2
+3.1
+1.1
Death
−6.1
+12.2
+4.5
+0.8
Family Relations
−5.9
+15.5
+3.8
−1.1
Food
−6.2
+7.6
+2.8
+1.2
Habits
−5.7
+11.4
+5.1
+0.5
Holiday Activities
−6.1
+12.6
+5.3
+2.6
Idioms
+0.4
+4.8
−0.5
+1.7
Parenting
−2.1
+14.1
+3.2
+2.0
Traditional Games
−6.3
+10.6
+2.7
−0.7
Wedding
−9.5
+11.3
+2.5
+0.6
Average
−4.9
+10.0
+3.2
+0.4
Table 14: ICL performance improvements (%).

--- Page 19 ---

Method
Trained
On
∆MCQ vs. Base
∆Completion vs. Base
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
ICL
Algeria
18.1 20.7 15.7 19.3 17.2 28.2 21.7 24.8 15.9 16.4 13.9 25.0
4.4
0.4 6.2
7.9
2.1 -0.4 1.9
3.2
3.2
8.6
0.8
1.3
1.9 -0.8
Egypt
22.2 22.3 16.5 22.3 15.1 29.6 24.5 27.2 15.0 17.2 13.4 25.4
5.6
-0.4 8.7
6.4
2.5 -1.7 -1.4 0.8
4.0
7.3
2.4
1.3
0.8
0.0
Jordan
15.3 18.2 17.2 15.1 13.4 23.6 17.8 22.8 15.0 16.8 13.0 24.6
9.2
-2.8 3.7 13.9 0.0
0.0
1.9
3.5
0.4 12.9 3.5
0.4
0.8 -2.8
KSA
18.6 22.3 18.0 19.3 15.1 27.8 22.9 27.2 17.2 19.5 13.9 27.3 10.0 -1.6 6.2
6.4
3.4
1.7
0.5
1.2
3.6
7.7
3.1
2.1
4.2
3.2
Lebanon 21.4 18.6 16.1 19.8 15.5 29.2 21.0 23.2 12.9 18.4 12.2 26.2
8.8
-1.2 7.0 12.4 -0.8 1.7
1.9
4.7
1.6 13.7 -0.8 0.8
2.7
1.6
Libya
15.3 19.8 15.7 16.8 11.6 26.9 15.8 22.4 12.9 16.4 11.3 24.6
8.0
-1.2 6.6
9.0
0.4 -0.4 2.3
1.2
5.6
8.2
2.0
2.1
5.0
1.2
Morocco 19.8 16.9 13.9 20.2 15.5 28.7 24.5 24.0 15.9 18.0 15.5 26.2
6.0
-0.8 6.2 10.9 0.0
1.7
1.4
3.2
4.4 10.3 2.7
2.9 -0.4 0.4
Palestine 19.3 17.4 16.9 19.8 16.8 30.1 20.2 21.6 13.7 16.0 11.8 25.8
6.0
-2.8 2.5
4.5
1.3 -0.4 0.0
4.0
3.6
6.4
-0.4 0.0
0.0
0.0
Sudan
16.9 15.3 14.2 19.3 16.4 25.0 16.2 19.6 10.7 16.4
8.4
21.5 10.4
0.0 5.4 13.5 2.1
2.2
0.5
0.8
2.8 11.2 1.2
2.1
1.5 -2.0
Syria
18.9 20.2 16.5 16.0 17.2 32.9 22.1 22.8 16.3 18.8 11.8 27.7
7.2
-1.6 6.2
9.7
4.2
1.3
1.9
3.2
3.2 10.3 1.2
2.9
2.3 -2.0
Tunisia
20.6 17.8 16.1 19.8 13.8 30.1 21.4 22.0 14.2 18.8 10.1 23.8
8.0
0.8 6.2
1.1
0.8
1.7
0.5
0.0
4.0
6.0
1.2
2.9
2.7 -1.6
UAE
13.7 14.0 15.7 19.8 13.4 25.5 16.6 20.4 13.7 16.8 13.4 24.6 11.2
0.8 7.9
7.9
4.2
1.3
1.4
2.8
3.6 11.6 2.7
0.4
6.2
0.8
Yemen
6.4
12.4 12.7 16.8
8.6
18.0
9.5
16.4 15.4 11.7
8.4
17.3
2.8
-1.2 3.7
5.6
0.4
1.7
2.8
1.2
1.2
4.7
1.2
0.4
1.9
4.0
Ditto
Algeria
18.6 16.5 14.6 14.7 16.4 21.3 21.7 22.8 15.0 13.3
9.7
23.5
9.6
0.8 2.9
3.0
0.0
1.3
1.9 -2.8 -0.4
2.6
-0.8 1.3 -5.0 -1.6
Egypt
23.0 18.6 16.9 16.0 15.1 24.5 22.9 21.6 15.4 15.6
7.6
23.1
8.0
-1.2 1.2
1.5
0.0 -0.4 -0.9 1.2
1.6
2.6
-5.5 -0.4 1.2 -2.0
Jordan
19.4 20.7 15.4 18.9 19.0 25.5 24.5 24.0 17.2 19.5
8.8
23.5 10.0 -1.6 6.2 -0.7 -0.4 -2.6 1.4
2.4 -1.6
2.2
-3.5 -1.3 -2.3 -1.6
KSA
18.9 19.4 16.1 16.8 18.1 23.6 23.3 24.8 15.4 16.4
8.4
21.2
9.6
1.2 3.3
2.6
0.8 -1.3 0.0
0.0 -3.6
4.3
-4.7 -1.3 -2.7 0.8
Lebanon 21.0 17.4 16.5 16.4 18.5 23.2 22.5 24.4 16.3 16.4 12.6 24.2
9.6
1.6 3.7
3.0
2.1
0.9 -0.5 -3.6 2.0
2.6
-0.8 1.7 -0.8 0.0
Libya
17.3 13.2 15.0 15.6 13.8 19.9 19.0 18.8 14.6 16.4
9.7
20.8
2.4
-1.2 3.3
0.0
2.1 -0.9 0.0 -5.5 1.2
0.9
-2.7 2.5 -1.5 0.8
Morocco 20.6 16.1 15.7 17.6 13.8 24.5 23.7 21.2 15.4 14.5
8.4
23.8
8.8
0.8 3.3
6.0
1.3
1.3 -0.9 2.0 -0.4
9.0
-2.3 0.0 -1.2 2.4
Palestine 18.6 21.9 16.1 17.6 15.1 25.9 22.9 22.8 18.0 13.7 10.1 21.9
9.6
-0.4 6.2
0.0
2.5 -1.3 0.5 -1.6 -1.6
2.6
-3.9 2.1 -1.5 -3.2
Sudan
19.4 22.7 16.5 19.3 16.0 24.5 24.1 22.8 18.4 18.4
9.7
23.1 12.0
2.4 2.5
6.0
1.3 -0.4 0.0
3.6 -2.0
6.9
-2.0 1.7 -3.8 -2.0
Syria
16.9 17.8 15.4 16.4 16.4 22.7 23.3 21.2 16.3 14.1
8.8
22.3
9.6
2.8 4.1
3.8
0.0 -1.3 1.9 -1.2 1.2
5.2
-3.1 2.1 -1.2 -1.2
Tunisia
16.9 17.4 15.7 15.1 17.7 23.6 21.0 22.0 17.2 13.7 11.8 21.9 10.0
2.0 2.1 -5.2
1.7 -0.4 0.0 -2.0 -1.2
1.3
-5.1 -0.8 -1.5 -0.4
UAE
18.1 15.7 16.9 17.6 16.0 24.5 22.1 20.8 18.4 12.1
8.8
21.2
7.2
1.6 4.1
3.4
0.8 -0.4 0.5 -1.2 2.0
6.9
-1.2 1.3 -3.5 0.0
Yemen
18.6 19.8 15.7 17.6 16.8 23.6 23.3 24.8 19.3 16.0 11.8 23.5 10.8
0.8 2.9 -3.0
0.4 -1.7 -2.3 0.4 -0.4
1.7
-4.7 0.0 -4.6 -0.8
Table 15: Cross-country evaluation results for Qwen2.5 7B-Instruct. Models are evaluated on different countries
(columns) after being trained on specific countries (rows). Values represent score difference from the base model.

--- Page 20 ---

Method
Trained
On
∆MCQ vs. Base
∆Completion vs. Base
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
ICL
Algeria
6.5
4.5
0.7
3.8
3.5
2.3
5.9
8.4
1.7 10.6 2.1
5.8
0.4
-0.4 2.9
9.4 8.0 3.5 -0.5 2.8
5.2
8.6
2.0
2.9
3.1
2.4
Egypt
-0.4
0.8
0.7
1.3
0.0
0.0
0.4
1.2
0.9
1.6
0.8
0.8
0.0
-2.8 3.7
3.8 3.8 1.7 -1.4 2.4
3.6
5.6 -1.6 3.4 -0.4 0.8
Jordan
14.5 6.6
1.1 12.6 6.9 13.0 12.6 16.4 4.7 20.7 10.9 15.0 0.4
-2.4 3.3 17.6 6.3 3.0 -0.9 4.7
2.8 10.7 2.7
3.4
3.9
6.0
KSA
7.3
5.8
0.4
8.0
4.8
3.7
2.4 10.4 4.3 16.8 3.8
6.5
2.8
-2.4 1.2
8.6 4.2 3.5
0.9
5.9
4.8
6.9
0.0
1.7
3.1
5.6
Lebanon
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
-0.4
0.4
-0.4
2.0
-3.6 4.5
8.2 9.7 4.7
0.0
4.0
0.8
6.4
2.7
2.5
3.1
2.4
Libya
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
0.0
-0.4
0.0
-0.4
2.8
-4.0 2.1
7.5 4.2 0.0 -0.9 3.6
5.2
3.9
0.4
4.2
1.9
2.4
Morocco
6.9
6.6
0.7
8.4
4.8
4.6
5.5 10.4 2.1 17.6 6.3 10.0 4.4
-3.2 5.0 10.1 8.0 1.7
0.0
3.6
3.6
8.6
1.2
2.5
3.5
4.0
Palestine
0.0
0.8
0.4
1.3
0.0
0.0
0.4
0.0
0.9
1.6
0.4
0.4
-1.2 -2.0 1.2
9.7 7.2 -0.9 0.5
0.4
4.4 10.3 1.6
3.8
3.9
4.0
Sudan
16.1 12.0 3.0 16.0 6.0 12.5 14.6 28.4 3.0 24.6 10.9 21.5 0.0
-2.8 0.8 10.9 4.2 4.3 -2.3 4.7
0.8 11.6 1.2
2.5
1.9
4.0
Syria
0.0
0.8
0.0
0.4
0.9
0.0
0.4
0.0
0.9
1.6
0.0
0.4
0.8
-6.5 2.1
6.0 4.6 3.9 -1.9 4.4
5.6
7.3
3.9
0.0
1.2
2.8
Tunisia
0.0
0.8
0.0
0.4
0.4
0.0
0.4
1.2
1.3
1.6
0.4
0.8
1.6
-4.0 3.7
5.6 4.6 1.7 -1.4 2.4
5.2
3.4
0.4
5.0
1.9
0.8
UAE
0.8
0.4
0.4
2.5
3.0
0.5
0.8
2.8
0.9
4.7
1.3
2.3
2.0
-1.2 4.5
5.6 5.0 3.0
0.5
1.2
4.8
7.3
1.6
0.0
6.9
6.4
Yemen
-0.4
0.8
0.0
0.8
0.0
0.0
0.4
0.0
0.4
0.8
0.0
-0.4
1.2
-0.8 2.9
4.5 5.5 0.4
0.9
1.6
6.4
3.9 -1.2 3.8
1.5
5.2
Ditto
Algeria
25.4 16.1 33.0 26.9 10.4 32.4 32.8 28.8 25.8 29.3 18.5 26.2 21.6 -4.0 -1.2 -1.9 1.7 2.2 -1.9 -4.4 1.6
4.7 -0.8 -0.4 -1.2 3.2
Egypt
24.6 18.6 43.8 26.5 15.5 35.2 41.5 31.2 39.5 30.1 15.1 30.0 15.2 -4.8 1.2 -6.0 0.0 3.5 -3.7 -3.2 -5.2 1.7 -4.7 1.7 -1.5 1.2
Jordan
31.9 23.1 49.4 32.8 20.3 40.7 44.7 38.4 41.2 35.2 21.8 33.5 26.4 -5.2 2.1
5.6 2.1 1.7 -0.9 0.0
0.0
7.7
0.0
2.9
1.5
1.6
KSA
18.2 20.2 44.6 23.9 13.4 32.4 37.6 25.6 40.8 30.9 18.9 31.9 16.8 -1.6 7.4
6.4 2.1 6.5
1.9
0.8
0.0
9.5
1.6
3.8
0.4
4.8
Lebanon
7.3
1.2
2.2
3.8
1.7 15.3 15.0 11.2 9.0 15.2 0.0
6.9
4.8
-5.6 3.3
4.5 3.0 4.3
0.9 -1.2 -4.4 7.7
0.8
2.1
0.4
1.6
Libya
32.3 21.1 49.8 32.4 16.0 40.7 41.1 40.0 43.3 36.3 20.2 30.4 30.8 -2.4 4.1
0.8 5.5 3.0 -1.9 -4.7 -0.8 6.9 -3.5 0.8 -1.9 0.0
Morocco
8.5
9.9 30.3 8.4
4.3 14.8 23.7 14.4 26.2 12.1 6.3 11.5 6.0
-6.5 -2.1 4.1 3.0 1.3 -1.9 -2.0 -5.2 4.3 -3.1 0.0
0.4
2.4
Palestine 22.6 18.6 30.3 23.5 13.4 34.7 33.2 26.8 29.2 30.1 17.2 23.5 20.8 -2.8 2.9
0.8 0.0 0.4
2.3 -4.0 -2.4 1.7 -0.8 3.4 -0.8 4.0
Sudan
14.1 10.7 21.3 13.0 5.2 17.1 23.3 18.0 20.6 17.6 10.1 14.2 10.0 -4.4 0.4
3.0 2.5 2.2 -0.9 0.4
3.2
3.0 -1.2 2.9
2.7
4.8
Syria
29.0 24.8 42.7 32.4 18.1 40.3 40.7 37.2 36.9 35.9 19.3 32.7 22.4 -5.6 3.7
4.1 0.9 3.9
0.9 -2.0 -4.8 6.9 -2.3 -0.4 -1.9 -0.4
Tunisia
21.0 14.9 23.6 18.9 12.1 28.7 27.7 22.4 21.9 25.8 14.7 20.0 15.6 -1.2 2.5
5.6 3.8 2.6 -1.4 -2.0 -1.2 7.3 -3.1 0.4 -1.5 6.0
UAE
24.2 17.8 43.8 24.8 17.2 37.0 37.9 30.4 34.3 28.9 17.2 30.8 20.0 -2.4 5.0
6.4 3.8 2.6
1.9
0.0
1.6
4.3
0.8
1.3
0.4
5.6
Yemen
2.8
2.9 12.7 2.5
0.4
6.9 12.2 4.0 18.0 4.3
2.5
3.5
1.2
1.2
2.5
3.4 0.0 2.2 -2.3 -2.4 -5.2 3.9 -7.4 0.0 -1.9 2.0
Table 16: Cross-country evaluation results for Gemma-2 9B-it. Models are evaluated on different countries (columns)
after being trained on specific countries (rows). Values represent score difference from the base model.

--- Page 21 ---

Method
Trained
On
∆MCQ vs. Base
∆Completion vs. Base
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
ICL
Algeria
-9.7 -15.7
0.0
-11.8 -11.2 -14.4 -11.9 -14.4 -9.0 -10.2 -9.2
-9.6 -10.8 -0.4 2.1
11.2
4.2
3.0
3.7
5.1
3.6
3.4 4.7 8.8 0.8
1.2
Egypt
-25.4 -26.0 -17.2 -26.9 -20.7 -23.6 -28.9 -34.8 -22.3 -31.3 -17.6 -29.2 -24.4 -1.6 0.4
10.5
5.0
1.3
2.3
3.6
4.0
4.7 2.0 7.6 2.7
4.0
Jordan
-3.2
-8.3
-0.4
-5.5
-5.2
-6.9
-7.9
-4.0
-3.9
-5.9
-6.7
-2.7
-3.2
0.0
0.8
13.5
3.4
2.6
1.4
5.1
3.2
9.0 2.3 5.0 1.2
2.0
KSA
-16.9 -19.4 -6.7 -18.1 -16.4 -18.1 -19.4 -23.2 -16.7 -17.6 -13.4 -13.5 -13.2 -4.0 2.1
9.4
5.5
2.2
1.4
2.4
3.6
4.7 5.1 3.8 1.5
2.8
Lebanon -14.5 -17.4 -2.3 -16.4 -15.5 -14.8 -15.8 -21.6 -12.0 -17.2 -15.5 -16.5 -15.2 -0.8 1.2
10.9
5.0
1.3
5.6
2.8
4.0
4.7 4.3 5.9 3.5
3.2
Libya
-14.5 -16.5 -6.0 -13.5 -13.4 -13.4 -16.6 -15.6 -13.3 -13.7 -13.0 -11.5 -11.6 -2.8 0.8
9.0
3.8
2.6
4.2
2.0
2.8
3.4 3.9 3.8 -0.8 1.6
Morocco
-9.3 -13.6 -6.4 -13.9 -13.4 -13.0 -15.0 -14.0 -13.3 -12.5 -8.0
-8.9 -12.0 0.0
1.7
11.2
3.4
2.2
3.7
8.7
3.2
5.2 2.3 4.6 2.3
2.0
Palestine -19.8 -21.9 -12.7 -18.1 -19.0 -22.7 -20.6 -24.8 -22.3 -21.5 -14.3 -21.2 -18.8 0.0
0.8
9.7
4.2
0.9
4.2
1.6
4.0
0.4 2.3 5.0 -0.4 3.2
Sudan
-21.8 -25.6 -21.7 -23.5 -18.5 -21.3 -27.7 -27.2 -26.6 -23.4 -17.2 -21.5 -20.8 -2.4 0.4
9.4
2.1
1.3
1.9
4.8
3.6
8.6 2.0 5.9 1.9
2.0
Syria
-2.4 -13.2 -1.1
-8.4
-6.9
-5.1
-5.5
-8.8
-6.4
-5.1
-5.5
-4.2
-4.8
-1.2 0.8
10.1
5.0
0.9
4.2
5.1
6.0
5.6 6.6 7.1 1.9
2.0
Tunisia
-19.4 -22.7 -7.1 -23.1 -15.1 -17.1 -24.5 -26.4 -15.9 -22.7 -11.3 -20.0 -16.4 -0.4 0.0
8.6
2.9
3.0
5.6
5.9
5.2
4.7 6.3 6.7 3.5
4.0
UAE
-12.1 -16.5 -6.0 -11.8 -10.8 -11.6 -14.2 -18.0 -10.7 -11.7 -10.9 -9.6 -10.4 -2.0 0.0
8.2
3.8
1.3
4.2 -0.8 5.2
6.9 5.5 5.0 3.5
2.8
Yemen
-17.7 -24.0 -7.1 -17.7 -13.8 -16.7 -19.8 -22.8 -21.9 -23.0 -13.9 -16.2 -15.6 0.0 -0.8
6.0
2.5
0.9
5.6
0.4
2.8
3.9 4.3 4.2 1.5
6.0
Ditto
Algeria
-2.8
-5.0
3.0
4.6
-1.7
9.3
3.2
0.0
0.4
4.3
3.8
3.5
-1.6
-5.2 0.8
-5.2 -2.5 -0.9 0.0
0.4
1.6
2.2 3.1 3.8 -2.7 1.2
Egypt
-4.8
-6.2
0.0
0.8
-2.2
-0.9
-1.6
2.0
0.9
-4.3
4.2
-0.4
-1.6
-6.1 1.7
-9.0 -6.3 0.4
0.0 -4.4 -2.4 -4.7 0.4 2.1 -5.4 -1.2
Jordan
-10.5 -13.2 -20.6 -13.9 -9.9
-8.3 -13.8 -18.0 -16.3 -10.2 -7.1 -13.9 -9.6
-6.5 -2.1 -12.4 -7.6 -3.0 -0.9 -4.4 -6.8 -6.4 1.2 1.7 -6.9 -7.6
KSA
-1.2
-4.5
-0.8
-0.4
-7.3
0.0
-0.4
-4.0
-3.0
-0.8
2.1
-1.9
-2.8
-4.0 4.1
-0.4
1.3 -0.4 3.2
0.4
1.6
0.0 1.6 3.4 -1.9 2.0
Lebanon
2.8
0.0
3.0
6.7
1.7
8.8
5.1
3.6
1.3
3.5
5.1
3.8
3.2
-0.4 2.9
0.0
-8.0 0.4
2.8 -1.2 2.8
0.9 0.4 5.5 -3.5 2.4
Libya
-0.4
-6.6
2.2
-0.4
-0.4
-0.5
-1.2
-0.4
0.0
0.8
0.8
0.0
2.0
-4.4 1.2
-7.5 -6.7 -3.0 0.9 -1.2 -0.8 -4.7 1.6 2.9 -3.5 -1.2
Morocco
2.0
-2.5
5.6
2.9
-0.9
7.0
2.4
2.8
-0.4
6.6
5.5
4.2
5.2
-3.6 3.3
4.9
-2.5 2.2 -0.9 0.0 -0.8 -2.1 1.6 2.9 -5.4 -0.8
Palestine
2.8
-5.0
1.9
0.4
0.9
5.1
-2.4
0.8
-2.6
-0.4
4.2
1.5
3.6
-6.5 -0.8 -10.5 -7.6 -0.4 0.0 -5.9 -4.8 -6.0 2.0 2.9 -6.9 2.4
Sudan
-2.4
-2.9
2.6
2.5
-2.2
5.1
3.2
0.0
2.1
2.7
6.3
1.9
3.6
-3.2 2.1
-4.9 -3.4 -0.9 -2.8 -2.0 1.2 -2.6 0.8 2.5 -5.0 -3.2
Syria
2.0
-2.5
0.8
2.1
0.9
7.9
-0.4
4.8
0.4
3.9
8.0
1.5
4.4
-4.0 2.1
-5.6 -5.0 -0.4 0.0 -2.0 -0.4 -3.0 4.3 2.9 -6.5 -0.4
Tunisia
-0.4
-0.8
-0.8
1.7
1.3
7.4
3.2
0.0
-1.3
0.4
2.1
1.5
4.0
-2.4 3.3
2.6
-0.8 2.2
0.0
0.8
0.0 -3.0 0.0 2.9 -3.1 0.4
UAE
0.0
-2.9
5.6
5.9
-1.7
8.3
4.0
4.8
1.7
5.9
5.5
2.7
6.8
-5.7 -0.4 -8.6 -3.4 -1.7 -0.9 -1.2 -1.6 -3.0 0.0 5.5 -3.5 -1.6
Yemen
-2.4
-3.3
0.4
-1.7
-5.6
6.0
-1.2
0.0
-2.2
-0.4
3.4
-0.8
1.6
-3.2 4.6
0.0
-4.2 1.7
1.4
0.8
2.4 -3.9 2.7 5.9 -2.3 1.2
Table 17: Cross-country evaluation results for ALLaM 7B-Instruct-preview. Models are evaluated on different
countries (columns) after being trained on specific countries (rows). Values represent score difference from the base
model.

--- Page 22 ---

Method
Trained
On
∆MCQ vs. Base
∆Completion vs. Base
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
Alg
Egy
Jor
KSA
Leb
Lib
Mor
Pal
Sud
Syr
Tun
UAE
Yem
ICL
Algeria
-1.2
-2.5 -1.5 1.7
3.5
-1.9
3.6
2.8 -0.9 2.0 -0.4 7.3
-2.8
0.4
0.0
6.0
1.7 -1.7 1.9
2.4
1.2
7.3
2.0
0.8 -0.4 2.0
Egypt
-6.5
-4.1 -3.4 0.0
6.0
-3.7
2.4
2.4
0.4 -2.0 0.4
2.7
-3.2
-2.4 -1.2 1.9
1.7 -2.6 1.9
0.8
0.0
1.7 -0.4 0.4 -3.8 2.8
Jordan
2.0
1.7
1.1
4.6
3.0
1.4
5.9
6.4
3.0
4.7
0.0
5.0
1.2
0.4
1.2
8.2
5.0 -0.4 2.8
2.4
3.2
3.9
1.2 -1.3 -3.1 3.2
KSA
1.2
2.1
-2.6 4.6
0.9
-0.5
2.0
4.0 -2.1 0.8
0.8
4.6
2.0
0.8
0.0
5.6
4.6 -1.7 2.8
2.0
0.8
2.1 -1.6 -0.8 -2.3 4.0
Lebanon
-6.1
-4.1 -2.6 -1.3 3.0
-8.3
0.4 -0.8 0.9
0.8
0.4
2.7
-5.6
-3.2 -1.2 1.9
3.8 -2.6 1.4
2.0
0.8
2.1
2.0 -0.4 -0.8 2.4
Libya
-13.7 -12.0 -3.7 -5.5 -1.3 -14.8 -7.9 -4.4 -2.1 -9.8 -3.0 -0.8 -12.4 0.0
1.2
2.6
3.4 -0.9 1.9
3.2
2.8
2.1 -0.8 -0.4 -0.8 3.2
Morocco
4.0
2.5
0.0
2.9
5.2
0.5
6.7
6.0
1.3
7.0
4.2
4.2
0.4
-1.6 2.9
6.0
4.6
0.0
2.8
2.8
1.6
3.9
0.8 -0.8 -0.4 2.0
Palestine
-3.6
-3.7 -1.1 2.5
2.6
-4.2
1.2
2.4
1.3
2.0 -0.4 4.2
-3.6
-2.4 0.8
4.9
5.0 -0.9 2.3
2.0
1.6
3.9
1.2
0.8 -1.2 2.0
Sudan
-1.6
0.0
-1.1 4.6
2.2
-0.9
3.2
1.6
1.7
0.0
2.1
3.8
-1.2
-1.6 1.2
6.4
4.6
0.4
2.3
2.0
0.8
9.0
0.4 -1.3 -2.3 2.4
Syria
2.8
1.7
0.8
4.2
6.5
2.3
3.6
6.4
3.0
6.6
0.4
5.0
0.8
-1.6 -1.2 3.0
1.7 -1.7 1.9
0.8
0.8
4.3
1.2 -1.7 -3.1 3.2
Tunisia
-0.8
1.2
-3.4 1.7
5.2
-5.1
1.6
2.8 -1.3 2.4 -1.3 2.7
-1.6
-0.8 2.1
0.8
1.3 -1.7 1.4
0.0
0.4
0.9 -0.4 1.3 -2.3 2.4
UAE
-1.2
1.2
-1.5 5.9
3.5
-1.4
4.0
4.4
1.3
4.3
2.1
5.4
1.2
-0.4 2.1
3.4
2.9
0.0
2.8
2.4
2.8
5.2
2.3 -0.4 -0.4 4.0
Yemen
-4.8
-5.4 -2.6 0.4
3.9
-5.1
0.8
0.0 -0.4 -0.4 2.1
1.9
-0.4
-0.4 2.1
2.6
2.1
0.9
1.4
2.0 -2.4 0.9 -0.8 1.7 -4.6 3.2
Ditto
Algeria
0.0
-1.7
0.0
4.2
5.6
-1.9
1.2
2.0
1.7
5.5
0.8
6.5
3.2
-2.8 -5.4 -3.0 -2.5 3.0
0.0 -0.8 -2.0 1.7
3.5 -3.8 -2.7 3.6
Egypt
-3.2
-4.1 -3.0 0.4
1.3
-0.5 -2.4 -0.4 0.0 -2.7 0.8
0.8
-2.4
-2.4 0.0 -4.1 -3.0 0.9 -2.8 -0.4 -3.2 -0.4 1.2
0.0 -1.9 3.6
Jordan
0.4
-2.1 -0.4 3.4
2.2
1.4
2.8
0.4
0.9
5.1
1.7
3.1
1.6
-3.2 -0.4 4.9
4.6
0.9
0.0
0.0
0.8
3.9
3.1
0.4 -3.1 2.8
KSA
0.0
-1.2
0.4
0.8
2.6
2.3
-0.8 0.8
0.9
2.4
0.4 -0.4
0.8
-2.0 0.4
1.1 -1.7 1.3 -0.5 -0.8 0.0
1.7
1.6
0.4 -1.2 2.4
Lebanon
-6.9
-9.1 -4.1 -3.8 0.0
-3.2 -3.2 -3.6 -1.3 0.0 -5.5 2.3
-1.2
-3.6 -2.9 0.4
3.4
0.4
1.4
4.4
1.6
2.1
3.1 -1.3 -0.4 2.8
Libya
0.0
-6.2 -0.8 -0.8 3.5
-3.2 -1.2 -0.8 1.3
4.3 -2.1 -0.8
2.0
-2.0 -2.9 2.2
2.5
2.2
1.9 -2.8 1.6
4.3
4.3 -2.9 -1.5 4.0
Morocco
1.2
-2.1
0.8
3.8
6.5
0.0
3.2
3.2
0.4
5.9
2.5
5.0
4.4
-0.4 -1.2 3.4
2.5
0.0
0.9
4.0
0.0
2.6
2.7 -0.8 -3.5 4.4
Palestine
-1.2
-2.5
0.4
5.0
6.5
0.5
1.6
2.4
0.0
7.0
1.7
1.2
4.0
-2.0 -4.6 -2.6 -1.7 0.9
0.9
0.4
1.6
2.6
2.7
2.5
0.8 3.6
Sudan
2.4
-1.7
1.1
5.5
6.0
1.9
0.4
4.8
0.9
6.3
1.7
2.3
4.0
-0.4 -3.7 6.0
3.8 -1.3 1.4
0.0
4.0
4.7
2.0
2.9 -0.8 3.2
Syria
-1.6
-1.2 -0.8 2.9
4.7
0.5
0.8
2.4
1.7
6.6 -0.4 5.0
4.4
-3.2 -6.6 -3.0 -0.4 2.6
1.4
1.2 -1.6 2.1
2.3 -2.1 -1.9 6.0
Tunisia
2.8
-2.5
0.8
2.1
2.6
2.3
0.0
3.6 -0.9 7.0
1.7
3.5
6.8
2.0 -1.7 1.9
0.8
0.9
0.9 -0.8 -0.8 1.3
0.8
0.0 -4.2 2.8
UAE
1.2
-2.1
1.1
3.4
5.6
1.9
0.4
1.2
0.9
7.4
0.0
1.5
6.0
-1.6 -1.2 3.0
5.0
0.9
0.0
0.4
3.6
1.7
4.7 -0.4 -1.5 7.2
Yemen
-1.2
-2.9 -1.5 -0.8 6.9
3.2
-3.2 -0.8 -2.6 2.4
4.6
3.5
-1.2
-2.0 -1.2 -3.0 0.4
2.6 -1.4 0.8 -1.6 1.3
0.0
2.9 -4.2 4.4
Table 18: Cross-country evaluation results for SILMA 9B-Instruct. Models are evaluated on different countries
(columns) after being trained on specific countries (rows). Values represent score difference from the base model.

```
