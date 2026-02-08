---
title: "2025-authors-CCD-Bench Probing Cultural Conflict in LLM Decision-Making - PDF Extract"
source_pdf: "2025-authors-CCD-Bench Probing Cultural Conflict in LLM Decision-Making.pdf"
pages: 9
extracted_at: "2026-02-07T17:00:46.942308"
---

# PDF Extract: 2025-authors-CCD-Bench Probing Cultural Conflict in LLM Decision-Making

**Source PDF:** 2025-authors-CCD-Bench Probing Cultural Conflict in LLM Decision-Making.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

CCD-Bench: Probing Cultural Conflict in Large Language Model
Decision-Making
Hasibur Rahman, Hanan Salam
New York University Abu Dhabi, Abu Dhabi, United Arab Emirates
hasibur.rahman@nyu.edu, hanan.salam@nyu.edu
Abstract
Large language models (LLMs) increasingly shape inter-
personal and societal decision-making, yet their ability to
navigate explicit conflicts between legitimate cultural val-
ues remains underexplored. Existing benchmarks focus on
cultural knowledge (CulturalBench), value inference (World-
ValuesBench), or single-axis bias (CDEval), but none assess
how LLMs adjudicate when multiple cultural frameworks
directly clash. We introduce CCD-Bench, a benchmark for
evaluating LLM decision-making under cross-cultural value
conflict. CCD-Bench contains 2,182 open-ended dilemmas
across seven domains, each with ten anonymized response
options aligned with the ten GLOBE cultural clusters span-
ning 62 societies. Using a Stratified Latin Square design, we
evaluate 17 leading LLMs and find clear biases: models favor
Nordic Europe (20.2%) and Germanic Europe (12.4%), while
Eastern Europe and Middle East & North Africa responses
are least preferred (≈5–6%). Although 87.9% of model ratio-
nales reference multiple cultural dimensions, this pluralism is
shallow-dominated by Future and Performance Orientation,
with limited attention to Assertiveness or Gender Egalitarian-
ism (<3%). Ordering effects are negligible, and model sim-
ilarity clusters by developer lineage rather than geography.
CCD-Bench shifts evaluation from bias detection to pluralis-
tic reasoning, revealing that current LLMs express a Western-
centric, consensus-oriented worldview even when confronted
with equally valid, culturally diverse alternatives.
Code — https://github.com/smartlab-nyu/CCD-Bench
Introduction
Large Language models (LLMs) are increasingly deployed
as mediators in interpersonal and societal decision-making,
including conflict resolution and moral judgment tasks (Tan
et al. 2024; Pires et al. 2025; Koc¸ak, Puranam, and Ye˘gin
2024). As conversational interfaces integrate LLMs into ev-
eryday applications, millions of users now rely on them for
socially situated guidance. Even a mundane query, such as
“How should I email my boss to request leave?”, requires
not only factual accuracy but also culturally sensitive judg-
ment that aligns with local norms, values and expectations.
Yet the global adoption of LLMs reveals a critical chal-
lenge: aligning model recommendations with the full spec-
trum of cultural value systems. A growing body of evidence
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
shows that LLMs inherit salient cultural leanings from their
training data (Wang et al. 2024; Karinshak et al. 2024; Lu,
Song, and Zhang 2025; AlKhamissi et al. 2024), leading
users to receive responses that, while coherent, may reflect
narrow or inconsistent cultural assumptions. For instance,
the question “How should responsibilities be shared within a
family?” can evoke equally legitimate but divergent answers,
from merit-based distribution to age-based hierarchy to gen-
der egalitarianism, depending on cultural context. Although
prompt-engineering strategies that foreground local contex-
tual cues can mitigate such effects(Xu et al. 2025; Zhong,
Yun, and Sun 2024), a deeper issue remains: ”How do LLMs
resolve situations in which legitimate cultural values, such
as hierarchy versus egalitarianism, or group harmony ver-
sus personal initiative, directly conflict?”. These systematic
preferences raise an important distinction between bias and
cultural trend. Following AlKhamissi et al. (2024), we refer
to these patterns as cultural trends rather than biases, empha-
sizing that they do not necessarily entail harm but highlight
limitations in addressing pluralistic value systems.
Existing
leading
benchmarks,
such
as
MMLU
(Hendrycks et al. 2021) and ELO (Zheng et al. 2023),
prioritize factual accuracy and stylistic quality, overlooking
the cultural nuance and social intelligence required in real-
world interactions. Early alignment paradigms similarly
prioritize universal principles such as helpfulness, honesty,
and harmlessness (the “HHH” criteria) (Askell et al. 2021;
Ouyang et al. 2022; Bai et al. 2022), while sidestepping
the pluralistic and culturally contingent nature of human
values (Barbara Herrnstein Smith 1991). Yet, real decisions
often hinge on reconciling legitimate but conflicting value
systems, a challenge where the “HHH” framework offers
little guidance. Existing cultural benchmarks (Wang et al.
2024; Chiu et al. 2024; Zhao et al. 2024) capture model
tendencies along individual cultural axes, but none examine
how LLMs reason when culturally grounded values directly
collide. This leaves a critical gap in evaluating LLM
decision-making within pluralistic, cross-cultural contexts.
We introduce CCD-Bench (Culture-Conflict Decision
Benchmark), a benchmark for evaluating how LLMs nav-
igate value-plural dilemmas: cases where multiple cultural
worldviews are equally defensible. It assesses models’ abil-
ity to engage in pluralistic reasoning, recognizing and justi-
fying choices across competing cultural values.
arXiv:2510.03553v2  [cs.CL]  13 Nov 2025

--- Page 2 ---

Our diagnostic suite evaluates the 17 widely used LLMs
(excluding specialized reasoning models), embedding all
culturally salient information directly in the prompt to iso-
late the LLMs’ intrinsic decision-making tendencies. The
benchmark comprises 2,182 dilemmas across seven do-
mains: Arts, Education, Family, Wellness, Work, Science,
and Lifestyle, adapted from Wang et al. (2024). Building on
evidence that many LLMs already encode cultural frame-
works (Karinshak et al. 2024), we generate ten anonymized
candidate answers for each dilemma using a state-of-the-art
reasoning model, followed by human verification. Each re-
sponse corresponds to one of the ten GLOBE cultural clus-
ters: Anglo, Latin Europe, Nordic Europe, Germanic Eu-
rope, Eastern Europe, Latin America, Sub-Saharan Africa,
Middle East & North Africa, Southern Asia, and Confucian
Asia, representing 62 societies (House et al. 2004). Instead
of locating models along isolated cultural dimensions, CCD-
Bench embeds the cultural trade-off within each dilemma:
the model must select and justify one of ten equally valid,
culturally grounded responses. This design directly exposes
how LLMs reason when confronted with competing cultural
imperatives.
We advance three main contributions:
1. Benchmark: We introduce CCD-Bench, the first bench-
mark for evaluating LLMs on navigating complex cross-
cultural value conflicts, comprising 2,182 dilemmas
across seven domains, each paired with ten anonymized
culturally-distinct responses representing the GLOBE
cultural clusters.
2. Methodology: We develop a generation and verification
pipeline for producing culturally authentic alternatives,
combining multi-cluster prompting, similarity pruning,
human annotation, and a Stratified Latin Square design
to ensure a fair assessment of value pluralism.
3. Analysis: We evaluate 17 leading LLMs on CCD-Bench,
revealing systematic patterns in how models navigate
cultural conflicts and the extent to which they default to
specific cultural frameworks.
Related Work
Cultural Alignment in LLMs. Compelling evidence shows
LLMs encode distinct cultural orientations. For instance,
prompting GPT-4 in English tends to produce analytic,
independence-oriented reasoning, whereas Chinese prompts
evoke holistic, interdependent values (Lu, Song, and Zhang
2025). Similarly, CDEval finds GPT-4 skewed toward low
power distance and high individualism, while Baichuan-
13B and Qwen-7B exhibit stronger collectivist tendencies
(Wang et al. 2024). Yet, such binary, one-dimension-at-a-
time evaluations oversimplify pluralism. LLM-GLOBE ad-
vances this direction using open-ended prompts to uncover
tonal and rhetorical differences across cultures (Karinshak
et al. 2024), while AlKhamissi et al. (2024) improves align-
ment through “Anthropological Prompting.” However, these
studies stop short of testing how models reason when legiti-
mate cultural values directly conflict.
Cultural Knowledge and bias benchmarks. Several
Benchmarks assess cultural understanding or bias in LLMs
but similarly avoid explicit value conflict. For instance, Cul-
turalBench (Chiu et al. 2024) features 1,227 human-written
questions across 45 regions and 17 topics to assess cul-
tural knowledge, with variants for different difficulty lev-
els. However, it focuses on recall and ambiguity handling
rather than decision-making amid conflicting norms. World-
ValuesBench (Zhao et al. 2024) draws from the World Val-
ues Survey 1 to create millions of examples for predicting
demographic-conditioned values, evaluating alignment via
distribution metrics, but emphasizes prediction over resolu-
tion of conflicting perspectives. BLEnD (Myung et al. 2024)
tests everyday cultural knowledge with 52,600 QA pairs
across 16 countries and 13 languages, revealing performance
disparities for low-resource cultures, although it targets fac-
tual recall rather than value trade-offs. CAMeL (Naous et al.
2024) and its extensions detect biases in associations, partic-
ularly between Arab and Western entities, using fill-in-the-
blank prompts and parallel data, but center on implicit biases
instead of explicit dilemmas requiring justification. These
benchmarks illuminate cultural gaps but center on represen-
tation and factual recall rather than decision-making under
normative conflict.
Despite significant progress, no existing work systemat-
ically examines how LLMs adjudicate cultural value con-
flicts: situations where multiple legitimate worldviews de-
mand incompatible choices. Addressing this gap, CCD-
Bench focuses on pluralistic dilemmas that require explicit
reasoning about competing cultural imperatives.
Methodology
This section presents the methodology underlying CCD-
Bench, a benchmark designed to evaluate how LLMs nav-
igate culturally grounded value conflicts. We used GLOBE
as it aligns with our dilemma structure, provides validated
cultural value information for 62 societies, and distinguishes
between practices and values (House et al. 2004). The 10-
cluster granularity is sufficient for demographic analyses.
The benchmark construction process follows a three-module
pipeline encompassing Generation, Verification, and Evalu-
ation. The Generation Module produces culturally diverse
dilemmas and candidate responses aligned with the GLOBE
framework; the Verification Module ensures authenticity and
cross-cultural validity through human annotation and quality
control; and the Evaluation Module standardizes presenta-
tion and model assessment procedures. Together, these mod-
ules establish a replicable framework for systematically ex-
amining LLM decision-making under cultural pluralism.
Generation Module
The Generation Module constructs the core of CCD-Bench,
producing a diverse set of 2,182 open-ended cultural dilem-
mas, each paired with ten culturally grounded response al-
ternatives. We build on the validated question corpus from
CDEval (Wang et al. 2024), the most comprehensive col-
lection of culturally relevant scenarios to date, to ensure
that CCD-Bench captures authentic cultural decision points
1https://www.worldvaluessurvey.org/wvs.jsp

--- Page 3 ---

while remaining comparable with prior cultural-AI evalu-
ations. Starting from 2,953 short-form questions, we re-
tain 2,204 open-ended items likely to elicit divergent advice
across cultural contexts, excluding binary or factual ques-
tions. Each retained scenario is categorized into one of seven
domains: Arts, Education, Family, Wellness, Work, Science,
and Lifestyle, to represent everyday value conflicts.
Each dilemma is designed to contrast two or more com-
peting cultural imperatives (e.g., hierarchy vs. egalitari-
anism, collectivism vs. individual autonomy). For each
dilemma q, we generate a set of 10 culturally distinctive
answers {ac}10
c=1, each corresponding to one of the ten
GLOBE clusters C = {Anglo, Latin Europe, . .., Con-
fucian Asia} (House et al. 2004). To produce these al-
ternatives, we employ a multi-cluster prompting strategy
grounded in the GLOBE framework, instructing a state-
of-the-art reasoning model (OpenAI o3-2025-04-16) to
generate one response per cluster in a single call. Each
prompt embeds fenced <cultural identity> direc-
tives that encapsulate anonymized GLOBE descriptors. The
model is required to return: (i) a one–sentence answer that
omits explicit cultural self-reference and (ii) a one–sentence
rationale that references the corresponding GLOBE cultural
dimensions. Following Balepur, Rudinger, and Boyd-Graber
(2025), rationales are included to enhance internal coher-
ence between cultural identity and decision justification. A
detailed prompt structure is provided on GitHub.
Similarity pruning and regeneration.
Although the
multi-cluster prompting procedure should yield culturally
diverse responses, we observed occasional lexical redun-
dancy when answers from different clusters conveyed simi-
lar advice using overlapping phrasing. To mitigate this, we
computed pairwise MinHash Jaccard similarity (Cann et al.
2025) over 3-gram shingles for each ten-tuple of responses.
Any pair exceeding a similarity threshold of τ > 0.70 trig-
gered regeneration of the more redundant answer, with a
maximum of two attempts. The threshold was determined
empirically: manual inspection confirmed that pairs above
0.70 exhibited minimal semantic differentiation, whereas
pairs below retained meaningful cultural distinctions. Af-
ter pruning, 22 questions were removed, yielding 2,182 final
dilemmas. Across these, the pairwise MinHash Jaccard sim-
ilarity among the ten alternatives had a mean of M = 0.123
with a standard deviation of σ = 0.109 (N =
 10
2

× 2182
comparisons), confirming that regeneration effectively re-
duced near-duplicate content while preserving linguistic and
semantic diversity. This process enhanced the discriminative
validity of CCD-Bench by ensuring that each response re-
mains lexically distinct yet culturally coherent, a result fur-
ther verified through subsequent human evaluation.
Option ordering.
Pezeshkpour and Hruschka (2024)
demonstrated that the order of answer options in multiple-
choice settings can significantly affect LLM performance.
To neutralize such serial-position effects, we employ a
10 × 10 Stratified Latin Square, a domain-specific adap-
tation of the standard Latin square approach. Independent
Latin squares are generated for each of the seven domains to
ensure balanced option ordering within domains, rather than
globally across the corpus. Each cultural alternative appears
exactly once in every ordinal position (1–10) and precedes
or follows every other alternative exactly once, thereby sat-
isfying both row and column orthogonality. The complete
evaluation-prompt specification is available on GitHub to
support transparency and reproducibility.
Verification Module
A team of five reviewers and one meta-reviewer confirmed
that (i) each generated option would be viewed as reason-
able within the target cluster, (ii) did not mention the cultural
cluster directly, and (iii) was semantically distinct from the
other nine options. Non-conforming options are regenerated
until all criteria are met, with a maximum of two attempts.
None of the earlier 2,182 dilemmas were removed at this
step. More details can be found on GitHub.
Evaluation Module
Our analytic pipeline decomposes evaluation logs into three
layers: descriptive statistics, null-hypothesis significance
tests, and robust similarity/diversity indices.
Descriptive layer.
For each evaluation file, we record
(i) absolute frequency fc of each cultural cluster c
∈
{1, . . . , 10},
(ii)
display
position
distribution
π
=
(π1, . . . , π10), and (iii) domain-specific cluster counts. Raw
tallies are used without smoothing.
Position-bias test.
Under null hypothesis H0 of equal
likelihood for k = 10 positions, let O be observed counts
and E = (N/k, . . . , N/k) expected counts, with N =
P
i Oi. The χ2 goodness-of-fit test yields
χ2 =
k
X
i=1
(Oi −Ei)2
Ei
,
V =
s
χ2
N(k −1),
(1)
where Cram´er’s V follows thresholds: negligible < 0.10,
small < 0.30, medium < 0.50, large ≥0.50 (Harald Cram´er
1999).
Domain–cluster association.
We construct a D × C con-
tingency table T = [Tij] for domains (D) vs. clusters (C).
Pearson’s χ2(T) with (D −1)(C −1) degrees of freedom is
reported with standardized residuals rij = Tij−Eij
√
Eij
to iden-
tify over/under-represented pairs (Agresti 2019).
Latin-square balance.
Option orderings use a 10 × 10
Latin square (Bradley 1958). Let A be the 10 × 10 matrix
of cluster appearances per position across Q questions. Im-
balance is measured as
∆=
A−(Q/10)1

1,
BS = 100

1 −
∆
1.8 · 10Q

%,
(2)
with 1.8 as the worst-case normalization factor.
Diversity metrics.
For cluster frequencies p and sorted
counts x with x(1) ≤· · · ≤x(n),
H(p) = −
X
c
pc log2 pc,
(3)

--- Page 4 ---

Anglo
Eastern Europe
Latin America
Latin Europe
Confucian Asia
Nordic Europe
Sub-Saharan Africa
Southern Asia
Germanic Europe
Middle East
5
10
15
20
25
30
jamba-1.6-large
claude-3.7-sonnet
claude-4-sonnet
command-r-08-2024
deepseek-chat-v3
gemini-2.0-flash
gemini-2.5-flash
llama-3.3-70b
llama-4-maverick-17b
phi-4
wizardlm-2-8x22b
mistral-nemo
chatgpt-4o-latest
gpt-4.1
sonar
qwen-2.5-72b
grok-2
Figure 1: Percentage distribution of cultural cluster selec-
tions across 17 LLMs. Each line represents one model, val-
ues normalized to percentages (0–100%) for each of the 10
cultural clusters.
G(x) = 1
n

n + 1 −
2
P
i x(i)
n
X
i=1
(n + 1 −i)x(i)

(4)
(Shannon and Weaver 1949; Dorfman 1979). For each statis-
tic bθ, we draw B = 5, 000 bootstrap replicates and report
[2.5, 97.5] percentiles as 95% confidence bands (Efron and
Tibshirani 1998).
Model similarity.
For LLMs with distributions P and Q,
symmetrized Kullback–Leibler divergence (Kullback 1997)
is
Dsym(P, Q) = 1
2
X
c

Pc log Pc
Qc
+ Qc log Qc
Pc

,
(5)
adding 10−10 to avoid log 0. The matrix feeds average-
linkage hierarchical clustering (Sneath and Sokal 1973).
Cluster–position bias.
Repeating position-bias per clus-
ter gives Cram´er’s Vc; mean V =
1
10
P
c Vc is the model-
bias score.
Pluralism in rationales.
Let Ii = 1 if rationale i cites ≥2
GLOBE dimensions (Ii = 0 otherwise), for i = 1, . . . , n.
The pluralism rate is Rplural =
1
n
P
i Ii, reported per LLM
and ensemble to assess value-reasoning breadth.
Experiments
We experiment with the 17 most popular LLMs for non-
technical tasks, as ranked by OpenRouter 2. Our inquiry is
structured around five questions:
When offered culturally valid options, do LLMs
still prefer certain clusters or values?(RQ1)
A pronounced Nordic trend.
Every single model in our
sample selects the Nordic Europe option most often. The
share ranges from 16.1% (Cohere command-r) to a re-
markable 30.6% (Anthropic Claude-4 Sonnet), with
2https://openrouter.ai/rankings
jamba-1.6-large
claude-3.7-sonnet
claude-4-sonnet
command-r-08-2024
deepseek-chat-v3
gemini-2.0-flash
gemini-2.5-flash
llama-3.3-70b
llama-4-maverick-17b
phi-4
wizardlm-2-8x22b
mistral-nemo
chatgpt-4o-latest
gpt-4.1
sonar
qwen-2.5-72b
grok-2
Models
Power Distance
Uncertainty Avoidance
Humane Orientation
Institutional Collectivism
In-Group Collectivism
Assertiveness
Gender Egalitarianism
Future Orientation
Performance Orientation
GLOBE Dimensions
21.5 48.6 41.7 19.3 36.1 30.2 39.1 35.2 22.2 34.1 27.9 26.2 27.3 28.8 18.0 15.5 20.3
31.3 32.0 43.0 23.3 23.0 21.2 23.5 19.6 19.8 17.2 23.3 20.8 25.6 27.1 17.6 12.5 17.3
28.4 19.0 43.8 32.0 44.5 34.1 16.1 37.0 15.2 29.1 25.8 24.6 29.6 37.1 37.5 34.1 31.1
43.1 38.8 52.2 29.4 33.4 13.6 31.6 24.2 22.6 26.6 30.2 19.6 43.8 49.2 42.3 34.8 34.1
18.0 42.2 23.9 37.5 39.8 47.3 45.1 24.7 35.0 47.4 35.8 42.0 44.4 54.7 30.7 40.0 41.3
1.8
10.6
8.0
7.1
6.1
7.8
3.2
5.8
5.8
2.7
6.9
7.7
3.2
2.9
5.5
3.2
2.4
2.4
8.5
13.6
6.6
5.9
6.4
6.0
5.6
4.7
4.3
6.5
4.5
5.1
6.4
4.1
3.5
3.6
25.2 46.7 48.1 22.7 35.9 36.2 34.8 44.4 33.0 24.3 30.5 34.2 35.0 31.3 43.1 37.2 33.1
25.9 48.0 50.5 20.4 46.2 36.6 43.7 38.7 36.7 21.6 50.9 31.4 39.8 38.3 40.7 29.4 32.2
10
20
30
40
50
Mention Rate (%)
Figure 2: Model-wise comparison of mention rates for nine
GLOBE cultural dimensions cited in the rationales across 17
LLMs.
an across-model mean of M
= 20.2%. Put differently,
the median model chooses Nordic-style advice roughly ×2
more often than chance, signaling an entrenched preference
for highly egalitarian, consensus-driven solutions. Figure 1
visualizes the raw selection frequencies for all 17 LLMs.
Secondary leanings.
Two clusters emerge as consistent
runners-up: Germanic Europe (M = 12.4%): 7 LLMs list
it as their second-most frequent choice. And Sub-Saharan
Africa (M = 11.5%): likewise second for seven LLMs, un-
derscoring that collectivist but low-power-distance reason-
ing resonates with many systems. A smaller subset (three
LLMs, all OpenAI or Google) places the Anglo cluster in
second position, yet its average share (11.3%) still lags be-
hind the Nordic and Germanic means.
Under-represented clusters.
At the lower end of the
spectrum lie Eastern Europe (5.6%) and the Middle East
& North Africa (5.8%). No LLM exceeds an 8.2% se-
lection rate for either group, and the minimum for East-
ern Europe drops to just 2.7% in Anthropic Claude-4
Sonnet. These figures suggest that narratives foreground-
ing high power distance or strong in-group collectivism are
comparatively neglected.
Between-model variability.
Cluster preferences vary in
magnitude, but not in direction. The coefficient of variation
is smallest for Latin Europe (CV = 0.09), indicating that
LLMs converge on a modest but stable share for this clus-
ter. In contrast, Anglo selections display the greatest relative
spread (CV = 0.23), hinting that “mainstream Western” ad-
vice is more LLM-specific than often assumed.
Which values do the LLMs foreground?
Figure 2 shows
how often each system cites the nine GLOBE dimensions
when justifying its selections. Two broad patterns emerge.
1. A future-oriented, high-achievement consensus.
Across the 17 LLMs, four dimensions dominate the ra-
tionales:

--- Page 5 ---

Dimension
Mean Mention (%)
s.d.
In-Group Collectivism
38.2
9.5
Performance Orientation
37.1
9.4
Future Orientation
35.0
7.4
Institutional Collectivism
33.5
10.5
Table 1: The four most cited GLOBE dimensions in the ra-
tionales of 17 LLMs.
All four sit well above the chance baseline of 11% (one-
ninth), indicating that, irrespective of the cultural cluster
they ultimately pick, LLMs systematically justify their
advice in terms of group solidarity, long-range thinking,
and getting things done.
2. Low appetite for confrontation or gender talk. At the
opposite extreme, two dimensions are almost absent: As-
sertiveness: 5.2% (σ = 2.6) and Gender Egalitarian-
ism: 5.7% (σ = 2.5). No LLM mentions assertiveness in
more than 11% of its rationales, and the highest rate for
gender egalitarianism is 13.6% (Anthropic Claude-4
Sonnet). Even LLMs that frequently invoke Power Dis-
tance (e.g. Claude-3 Sonnet, 48.6%) do so via “re-
spect for hierarchy” rather than through a direct appeal
to forceful negotiation.
Between-model contrasts.
While the aggregate rankings
are stable, individual profiles diverge: (i) Anthropic LLMs
couple very high Performance Orientation ≈50% with the
steepest Power Distance scores, mirroring their Nordic clus-
ter preference for meritocratic—but-still-hierarchical solu-
tions. (ii) Google’s Gemini 2.x variants under-index on In-
stitutional Collectivism (13.6–31.6%) yet over-index on Hu-
mane Orientation, suggesting a more person-centred ratio-
nale style. (iii) OpenAI’s GPT-4.1 is an outlier for In-Group
Collectivism (54.7%), framing advice in terms of familial or
team loyalty more than any other system.
Convergent evidence across clusters and evaluative di-
mensions yields a single, coherent conclusion. When con-
fronted with ten anonymized, order-balanced alternatives,
each of the 17 LLMs shows a marked preference for the nor-
mative frameworks of Northern and Western Europe, espe-
cially the Nordic and Germanic clusters, signaling an align-
ment imprint rather than stochastic variation. Their accom-
panying rationales tell the same story: although explicitly
invited to invoke any of GLOBE’s nine cultural dimensions,
LLMs repeatedly draw on future orientation, collective re-
sponsibility, and performance achievement, while rarely ap-
pealing to assertiveness or gender egalitarianism. Taken to-
gether, the results suggest prevailing alignment pipelines
embed a conciliatory, progress-centred worldview emblem-
atic of affluent liberal democracies, functional in many set-
tings yet inadequate to capture humanity’s full breadth.
Are these preferences domain-specific (e.g., religion
vs. business) or globally consistent? (RQ2)
To probe whether the cultural leanings uncovered in RQ1
persist across topical contexts, we split the 2,182 dilemmas
into the seven CCD-Bench domains.
Dominant Nordic trend.
In every domain, the Nordic
Europe option remains the single most frequent choice. Its
mean share varies from a high of 23.9% in FAMILY to a low
of 15.6% in LIFESTYLE, but the ranking never drops below
first place. Hence, the headline bias identified in RQ1 is not
an artefact of a particular topic, such as business or science;
it is a cross-domain constant of the evaluated LLMs.
Domain: Sci., Work, Educ., Wellness, Lifestyle, Family, Arts
Nordic share (%): 21.9, 20.6, 21.2, 21.0, 15.6, 23.9, 15.8
Rank 1, 1, 1, 1, 1, 1, 1
Which clusters fluctuate?
While the top slot remains sta-
ble, the lower tail shifts according to context. The least ref-
erenced cluster varies by domain: Eastern Europe in SCI-
ENCE, Middle East & North Africa in WORK and EDU-
CATION, Latin America in WELLNESS, Latin Europe in
LIFESTYLE, and Confucian Asia in ARTS. Domain content
thus nudges which minority perspective is discounted. Ger-
manic Europe and Sub-Saharan Africa exhibit the widest
domain variance (s.d. ≈3 pp), rising in WORK (Germanic)
or WELLNESS (Sub-Saharan), yet receding elsewhere.
Statistical test.
Collapsing all LLMs into a single 7 × 10
contingency matrix and applying Pearson’s χ2 test yields
χ2 = 256.7, df = 54, p < .001. However, the effect size
is modest: Cram´er’s V = .12 (95% CI [.10, .14]), labeled
“small.” In other words, the domain does influence clus-
ter selection, but the global Nordic skew significantly out-
weighs its magnitude.
Cultural preferences in current LLMs are globally consis-
tent. Topical context shifts the edges of the distribution, de-
ciding which clusters are least represented. Still, it does not
perturb the overarching hierarchy: Nordic-style, low-power-
distance, achievement-oriented advice dominates whether
the user asks about science policy, workplace etiquette, fam-
ily dilemmas, or the arts. The trends diagnosed in RQ1
are therefore systemic, not situational, and should be ad-
dressed at the alignment or data-curation level rather than
via domain-specific patching.
Do LLMs integrate multiple cultural dimensions or
default to a single axis? (RQ3)
High pluralism.
Across the whole corpus (N = 37, 092
rationales), 87.9% cite two or more dimensions, indicating
that most LLMs can articulate multi-faceted justifications
when prompted. Yet, the model spread is broad, ranging
from a low of 68.6% (Meta-Llama 4 Maverick) to a peak
of 98.6% (Anthropic Claude-4 Sonnet). 7 of the 17 systems
exceed the 90% mark, whereas three systems remain below
80%. High pluralism is therefore common.
Pluralism ̸= cultural breadth.
One might expect an
LLM that distributes its selections broadly (i.e., exhibits
high entropy) also to draw on more dimensions, but the
data suggest otherwise. The Pearson correlation between en-
tropy and pluralism is mildly negative (r = −0.22). Co-
here command-r exhibits the highest entropy (3.28) yet
one of the lower pluralism scores (78.5%), while Anthropic
Claude-4 shows the reverse. Integrating multiple dimensions
and sampling widely across clusters are therefore distinct.

--- Page 6 ---

Which pairings dominate?
Two results stand out: first, a
single pairing explains one-fifth of all plural rationales, with
Future Orientation (FO) + Performance Orientation (PO)
appearing 6,732 times (20.6% of all plural explanations), no
other pairing reaches 16%, meaning LLMs overwhelmingly
justify “multi-dimensional” decisions as “long-term plan-
ning to achieve goals”; second, collectivist modifiers dom-
inate the next tier, splicing Institutional Collectivism (IC),
In-Group Collectivism (IGC), or Humane Orientation (HO)
onto either PO or FO, with the top six pairings, FO + PO
(20.6%), HO + IGC (15.3%), IC + PO (14.4%), FO + IC
(12.9%), IGC + Power Distance (PD) (12.4%), and HO + IC
(10.7%), accounting for 86% of all plural rationales.
Dimension-level centrality.
Summing across all pair-
ings shows the frequency with which each GLOBE di-
mension enters multi-dimensional rationales: PO (16.2%),
FO (15.1%), IC (14.9%), IGC (13.5%), HO (13.0%), PD
(12.5%), Uncertainty Avoidance (UA) (9.5%), Gender Egal-
itarianism (GE) (2.7%), and Assertiveness (AS) (2.6%). The
first six account for over 85% of mentions, with AS and GE
remaining fringe (<3% each).
Model signatures.
The expanded per-model breakdown
shows that: (i) Anthropic models over-index on the
“achievement + hierarchy” tripod: PO, IC, and PD. (ii)
Google Gemini 2.x variants distinguish themselves through
frequent IGC + PO pairings, signaling a “team success”
rhetoric. (iii) Meta-Llama 4 Maverick is the only model
where FO + PO accounts for less than 24% of its plural ra-
tionales, yet it also exhibits the lowest pluralism rate overall.
LLMs integrate multiple cultural dimensions, but combi-
nations are imbalanced: four mainstream values, FO, PO,
and the two forms of Collectivism, dominate ≈90% of
multi-dimensional rationales, while AS and GE remain
marginal. Thus, models exhibit limited pluralism, relying on
a narrow subset of harmonious dimensions.
Do Models Exhibit Systematic Ordering Bias
When Selecting Among Options? (RQ4)
P1
P2
P3
P4
P5
P6
P7
P8
P9
P10
Display Position
6
8
10
12
14
16
Selection Percentage (%)
Anglo (n=4,194)
Eastern Europe (n=2,086)
Latin America (n=2,681)
Latin Europe (n=3,051)
Confucian Asia (n=2,746)
Nordic Europe (n=7,480)
Sub-Saharan Africa (n=4,269)
Southern Asia (n=3,733)
Germanic Europe (n=4,584)
Middle East (n=2,153)
Figure 3: Selection percentage of each cultural cluster across
display positions (P1–P10), aggregated over all 17 LLMs.
Our generated corpus has a Latin-square balance score of
≈99.8%. Despite employing the Stratified Latin Square de-
sign to neutralize serial and residual ordering biases, these
biases may persist if models exhibit systematic preferences
for certain positions (e.g., favoring early or late options). In
this section, we analyze the distribution of selections across
the 10 positions for each cultural cluster, aggregated over
all 17 models and 2,182 dilemmas (total valid selections:
36,977; expected per position under uniformity: 3,697.7).
We quantify positional bias using Cram´er’s V per cluster,
interpreting values below 0.10 as negligible. Figure 3 shows
selection percentages across display positions.
Overall Positional Bias Levels.
All 10 clusters exhibit
negligible positional bias, with Cram´er’s V values ranging
from 0.0510 (Nordic Europe) to 0.0877 (Eastern Europe),
confirming no small, medium, or large effects across the
board. This low bias underscores the effectiveness of our
Latin Square design in mitigating ordering artifacts. A de-
tailed breakdown can be found on GitHub.
Mild Primacy Effect in Positions.
A modest yet dis-
cernible primacy tendency surfaces: Position 1 (P1) is cho-
sen disproportionately in nine of the ten cultural clusters,
15.6% for Confucian Asia and 15.5% for Eastern Europe,
for example, producing an aggregate deviation of 42.2 from
the uniform baseline. Nordic Europe constitutes the sole ex-
ception, exhibiting a slight preference for P4 (12.7%) over
P1 (11.4%). Choices in the later positions (P6–P10) remain
evenly distributed, whereas P5 proves most balanced over-
all, with a deviation of only 8.6.
Cluster-Specific Variations.
Clusters generally under-
selected, Eastern Europe (2,086 total selections) and the
Middle East (2,153), manifest the most significant positional
biases (V = 0.0877 and V = 0.0797, respectively). Both
clusters show elevated selection rates in early slots (Eastern
Europe’s P1 at 15.5%) and marked declines in later ones (P8
at 6.4%). Conversely, highly favored clusters, such as Nordic
Europe, register the lowest positional variance (2.34), indi-
cating a more stable distribution across positions.
Together, these patterns confirm that the experimental
protocol largely suppresses ordering effects; any residual po-
sitional bias is insufficient to compromise the cultural prefer-
ence findings reported in the preceding RQs. The persistent
over-selection of P1 suggests that future benchmarks could
benefit from enhanced randomization schemes.
Do LLMs Cluster by Cultural Behavior, and Does
This Pattern Correlate with Their Geographic
Provenance? (RQ5)
To assess similarities in cultural selection patterns and their
relation to developers’ locations, we compute symmetrized
Kullback-Leibler (KL) divergence between each pair of
models’ cluster distributions, yielding a 17×17 distance ma-
trix fed into average-linkage hierarchical clustering. Devel-
oper geographies are from public sources. Figure 4 shows
the KL-divergence heatmap and dendrogram.
Model Clustering Patterns.
The dendrogram in Figure 4
reveals tight intra-family groupings at low divergence levels
(e.g., Meta’s Llama-3.3 and Llama-4 at 0.0033, Anthropic’s
Claude-3.7 and Claude-4 at 0.0398, Google’s Gemini-2.0

--- Page 7 ---

jamba-1.6-large
claude-3.7-sonnet
claude-4-sonnet
command-r-08-2024
deepseek-chat-v3
gemini-2.0-flash
gemini-2.5-flash
llama-3.3-70b
llama-4-maverick-17b
phi-4
wizardlm-2-8x22b
mistral-nemo
chatgpt-4o-latest
gpt-4.1
sonar
qwen-2.5-72b
grok-2
Models
jamba-1.6-large
claude-3.7-sonnet
claude-4-sonnet
command-r-08-2024
deepseek-chat-v3
gemini-2.0-flash
gemini-2.5-flash
llama-3.3-70b
llama-4-maverick-17b
phi-4
wizardlm-2-8x22b
mistral-nemo
chatgpt-4o-latest
gpt-4.1
sonar
qwen-2.5-72b
grok-2
Models
0.000 0.039 0.124 0.010 0.033 0.013 0.004 0.031 0.040 0.037 0.047 0.016 0.012 0.047 0.037 0.026 0.026
0.039 0.000 0.040 0.051 0.008 0.027 0.034 0.006 0.006 0.075 0.020 0.012 0.028 0.067 0.011 0.062 0.028
0.124 0.040 0.000 0.146 0.045 0.102 0.113 0.040 0.033 0.163 0.037 0.067 0.095 0.141 0.040 0.138 0.088
0.010 0.051 0.146 0.000 0.037 0.009 0.011 0.052 0.061 0.011 0.067 0.026 0.011 0.019 0.048 0.016 0.014
0.033 0.008 0.045 0.037 0.000 0.017 0.029 0.014 0.014 0.052 0.032 0.011 0.020 0.044 0.010 0.050 0.015
0.013 0.027 0.102 0.009 0.017 0.000 0.010 0.034 0.038 0.022 0.047 0.020 0.007 0.023 0.036 0.026 0.005
0.004 0.034 0.113 0.011 0.029 0.010 0.000 0.030 0.033 0.038 0.041 0.017 0.013 0.044 0.037 0.028 0.021
0.031 0.006 0.040 0.052 0.014 0.034 0.030 0.000 0.003 0.083 0.012 0.009 0.027 0.079 0.007 0.057 0.038
0.040 0.006 0.033 0.061 0.014 0.038 0.033 0.003 0.000 0.092 0.014 0.015 0.035 0.085 0.010 0.068 0.041
0.037 0.075 0.163 0.011 0.052 0.022 0.038 0.083 0.092 0.000 0.090 0.049 0.020 0.003 0.070 0.014 0.015
0.047 0.020 0.037 0.067 0.032 0.047 0.041 0.012 0.014 0.090 0.000 0.027 0.032 0.082 0.023 0.052 0.045
0.016 0.012 0.067 0.026 0.011 0.020 0.017 0.009 0.015 0.049 0.027 0.000 0.016 0.050 0.006 0.037 0.022
0.012 0.028 0.095 0.011 0.020 0.007 0.013 0.027 0.035 0.020 0.032 0.016 0.000 0.020 0.029 0.009 0.009
0.047 0.067 0.141 0.019 0.044 0.023 0.044 0.079 0.085 0.003 0.082 0.050 0.020 0.000 0.065 0.017 0.012
0.037 0.011 0.040 0.048 0.010 0.036 0.037 0.007 0.010 0.070 0.023 0.006 0.029 0.065 0.000 0.054 0.032
0.026 0.062 0.138 0.016 0.050 0.026 0.028 0.057 0.068 0.014 0.052 0.037 0.009 0.017 0.054 0.000 0.023
0.026 0.028 0.088 0.014 0.015 0.005 0.021 0.038 0.041 0.015 0.045 0.022 0.009 0.012 0.032 0.023 0.000
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
0.16
KL Divergence
0.00
0.02
0.04
KL Divergence
llama-4-maverick-17b
llama-3.3-70b
claude-3.7-sonnet
sonar
mistral-nemo
deepseek-chat-v3
wizardlm-2-8x22b
claude-4-sonnet
gpt-4.1
phi-4
qwen-2.5-72b
gemini-2.5-flash
jamba-1.6-large
command-r-08-2024
grok-2
gemini-2.0-flash
chatgpt-4o-latest
Models
Max Distance: 0.054
Mean Distance: 0.038
Linkage: Average
Figure 4: Heatmap of symmetrized KL-divergence between models’ cultural cluster selections (left), with average-linkage
hierarchical clustering dendrogram (right).
and Gemini-2.5 at 0.0103, OpenAI’s GPT-4o at 0.0200, Mi-
crosoft’s Phi-4 and GPT-4.1 at 0.0032 via linkage). Broader
clusters emerge around 0.01–0.05: one subgroup includes
Google, OpenAI, xAI, Cohere, and Qwen; another features
Anthropic, Meta, Perplexity, Mistral, and DeepSeek.
Correlation with Geographic Provenance.
Clustering
shows weak geographic ties: US models span both sub-
clusters, with corporate lineage (e.g., Meta/Anthropic vs.
Google/OpenAI) dominating over location. Non-US mod-
els fragment similarly (Chinese: DeepSeek in subcluster
2, Qwen in 1; European-adjacent: Mistral in 2, Cohere in
1; AI21 with Google/Cohere). This implies that alignment
strategies and shared corpora influence cultural behavior
more than national origin, though Western-centric data lim-
its distinctions.
Discussion
Our findings reveal a clear cultural bias in contemporary
LLMs: when presented with plural legitimate options in
a decision-making task, models tend to gravitate toward
Nordic/Germanic clusters. The associated rationals are strik-
ingly uniform: models rely on Future Orientation and Per-
formance Orientation with regularity, while rarely ground-
ing decisions in Assertiveness or Gender Egalitarianism
(each < 3%). This does not merely imply that models
have bias; rather, the very style of advice being normalised
in highly used models embodies a conciliatory, progress-
centred, achievement-first worldview, which is systemati-
cally misaligned with contexts that legitimate hierarchy or
where an explicit appeal to gender fairness is the appropri-
ate move. Therefore, occasionally, a default to consensus-
seeking performance talk can result in advice that comes
across as naive or disrespectful. Models should instead sur-
face plural options, making trade-offs explicit and labeling
the value frames that motivate each option, allowing users to
decide which options are valid given their local norms.
A notable limitation is our exclusive use of English
prompts, which may bias outputs toward Anglo-American
values and obscure regional nuances (Zhong, Yun, and Sun
2024); future work should utilize multilingual prompts to
distinguish between language and cultural effects. If LLMs
are to mediate everyday social decision-making, alignment
must treat conflicts among legitimate values as a design tar-
get, so that a model helping someone write to their supervi-
sor or address a family dispute can offer guidance that is not
simply good, but good for their values.
Conclusion
In this work, we introduce CCD-Bench, a novel benchmark
specifically designed to assess how contemporary LLMs
navigate conflicts among legitimate cultural values. Evaluat-
ing 17 LLMs on 2,182 dilemmas, we observed a pronounced
cultural trend toward Nordic and Germanic clusters. De-
spite high rates of multi-dimensional rationales, models re-
lied on a narrow set of GLOBE dimensions, while rarely in-
voking Assertiveness or Gender Egalitarianism (<3% each),
suggesting an aversion to confrontational or gender-focused
reasoning and indicating limited true pluralism in reason-
ing. Our results underscore the need for more nuanced ap-
proaches to cultural dynamics in LLMs if they are to operate
credibly within an increasingly pluralistic world.

--- Page 8 ---

Acknowledgments
This work is supported in part by the NYUAD Center for In-
terdisciplinary Data Science & AI, funded by Tamkeen un-
der the NYUAD Research Institute Award CG016.
References
Agresti, A. 2019. An introduction to categorical data anal-
ysis. Wiley. ISBN 978-1-119-40526-9.
AlKhamissi, B.; ElNokrashy, M.; Alkhamissi, M.; and Diab,
M. 2024. Investigating Cultural Alignment of Large Lan-
guage Models. In Ku, L.-W.; Martins, A.; and Srikumar,
V., eds., Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 12404–12422. Bangkok, Thailand: Association for
Computational Linguistics.
Askell, A.; Bai, Y.; Chen, A.; Drain, D.; Ganguli, D.;
Henighan, T.; Jones, A.; Joseph, N.; Mann, B.; DasSarma,
N.; Elhage, N.; Hatfield-Dodds, Z.; Hernandez, D.; Kernion,
J.; Ndousse, K.; Olsson, C.; Amodei, D.; Brown, T.; Clark,
J.; McCandlish, S.; Olah, C.; and Kaplan, J. 2021. A Gen-
eral Language Assistant as a Laboratory for Alignment.
ArXiv:2112.00861 [cs].
Bai, Y.; Jones, A.; Ndousse, K.; Askell, A.; Chen, A.; Das-
Sarma, N.; Drain, D.; Fort, S.; Ganguli, D.; Henighan,
T.; Joseph, N.; Kadavath, S.; Kernion, J.; Conerly, T.; El-
Showk, S.; Elhage, N.; Hatfield-Dodds, Z.; Hernandez, D.;
Hume, T.; Johnston, S.; Kravec, S.; Lovitt, L.; Nanda, N.;
Olsson, C.; Amodei, D.; Brown, T.; Clark, J.; McCandlish,
S.; Olah, C.; Mann, B.; and Kaplan, J. 2022.
Training a
Helpful and Harmless Assistant with Reinforcement Learn-
ing from Human Feedback. ArXiv:2204.05862 [cs].
Balepur, N.; Rudinger, R.; and Boyd-Graber, J. L. 2025.
Which of These Best Describes Multiple Choice Evaluation
with LLMs? A) Forced B) Flawed C) Fixable D) All of the
Above. ArXiv:2502.14127 [cs].
Barbara Herrnstein Smith. 1991. Contingencies of value :
alternative perspectives for critical theory. Harvard Univer-
sity Press. ISBN 978-0-674-16786-5.
Bradley, J. V. 1958. Complete Counterbalancing of Imme-
diate Sequential Effects in a Latin Square Design. Journal
of the American Statistical Association, 53(282): 525–528.
Cann, T. J. B.; Dennes, B.; Coan, T.; O’Neill, S.; and
Williams, H. T. P. 2025. Using semantic similarity to mea-
sure the echo of strategic communications. EPJ Data Sci-
ence, 14(1): 1–19. Number: 1 Publisher: SpringerOpen.
Chiu, Y. Y.; Jiang, L.; Lin, B. Y.; Park, C. Y.; Li, S. S.; Ravi,
S.; Bhatia, M.; Antoniak, M.; Tsvetkov, Y.; Shwartz, V.; and
Choi, Y. 2024. CulturalBench: a Robust, Diverse and Chal-
lenging Benchmark on Measuring the (Lack of) Cultural
Knowledge of LLMs. ArXiv:2410.02677 [cs] version: 1.
Dorfman, R. 1979. A Formula for the Gini Coefficient. The
Review of Economics and Statistics, 61(1): 146.
Efron, B.; and Tibshirani, R. 1998. An introduction to the
bootstrap. Boca Raton, Fla Chapman & Hall/Crc. ISBN
978-0-412-04231-7.
Harald Cram´er. 1999. Mathematical methods of statistics.
Princeton University Press. ISBN 978-0-691-00547-8.
Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika, M.;
Song, D.; and Steinhardt, J. 2021. Measuring Massive Mul-
titask Language Understanding. ArXiv:2009.03300 [cs].
House, R. J.; Hanges, P. J.; Javidan, M.; Dorfman, P. W.; and
Gupta, V. 2004. Culture, leadership, and organizations: The
GLOBE study of 62 societies. Sage Publications, 1 edition.
Karinshak, E.; Hu, A.; Kong, K.; Rao, V.; Wang, J.; Wang,
J.; and Zeng, Y. 2024.
LLM-GLOBE: A Benchmark
Evaluating the Cultural Values Embedded in LLM Output.
ArXiv:2411.06032 [cs].
Koc¸ak, ¨O.; Puranam, P.; and Ye˘gin, A. 2024.
LLMs
as mediators: Can they diagnose conflicts accurately?
ArXiv:2412.14675 [cs].
Kullback, S. 1997. Information theory and statistics. Dover
Publications. ISBN 978-0-486-69684-3.
Lu, J. G.; Song, L. L.; and Zhang, L. D. 2025.
Cultural
tendencies in generative AI. Nature Human Behaviour, 1–
10. Publisher: Nature Publishing Group.
Myung, J.; Lee, N.; Zhou, Y.; Jin, J.; Putri, R. A.; Antypas,
D.; Borkakoty, H.; Kim, E.; Perez-Almendros, C.; Ayele,
A. A.; Guti´errez-Basulto, V.; Ib´a˜nez-Garc´ıa, Y.; Lee, H.;
Muhammad, S. H.; Park, K.; Rzayev, A. S.; White, N.; Yi-
mam, S. M.; Pilehvar, M. T.; Ousidhoum, N.; Camacho-
Collados, J.; and Oh, A. 2024.
BLEnD: A Benchmark
for LLMs on Everyday Knowledge in Diverse Cultures and
Languages.
Advances in Neural Information Processing
Systems, 37: 78104–78146.
Naous, T.; Ryan, M. J.; Ritter, A.; and Xu, W. 2024. Having
Beer after Prayer? Measuring Cultural Bias in Large Lan-
guage Models. In Ku, L.-W.; Martins, A.; and Srikumar,
V., eds., Proceedings of the 62nd Annual Meeting of the
Association for Computational Linguistics (Volume 1: Long
Papers), 16366–16393. Bangkok, Thailand: Association for
Computational Linguistics.
Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright,
C. L.; Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray,
A.; Schulman, J.; Hilton, J.; Kelton, F.; Miller, L.; Simens,
M.; Askell, A.; Welinder, P.; Christiano, P.; Leike, J.; and
Lowe, R. 2022. Training language models to follow instruc-
tions with human feedback. In Proceedings of the 36th Inter-
national Conference on Neural Information Processing Sys-
tems, NIPS ’22, 27730–27744. Red Hook, NY, USA: Curran
Associates Inc. ISBN 978-1-7138-7108-8.
Pezeshkpour, P.; and Hruschka, E. 2024. Large Language
Models Sensitivity to The Order of Options in Multiple-
Choice Questions.
In Duh, K.; Gomez, H.; and Bethard,
S., eds., Findings of the Association for Computational Lin-
guistics: NAACL 2024, 2006–2017. Mexico City, Mexico:
Association for Computational Linguistics.
Pires, A. S.; Samson, L.; Ghebreab, S.; and Santos, F. P.
2025. How large language models judge and influence hu-
man cooperation. ArXiv:2507.00088 [physics].
Shannon, C. E.; and Weaver, W. 1949.
The Mathemati-
cal Theory of Communication. The Mathematical Gazette,
34(310): 312.

--- Page 9 ---

Sneath, P. H.; and Sokal, R. R. 1973. Numerical Taxonomy:
The Principles and Practice of Numerical Classification. W.
H. Freeman.
Tan, J.; Westermann, H.; Pottanigari, N. R.; ˇSavelka, J.;
Mee`us, S.; Godet, M.; and Benyekhlef, K. 2024. Robots
in the Middle: Evaluating LLMs in Dispute Resolution.
ArXiv:2410.07053 [cs].
Wang, Y.; Zhu, Y.; Kong, C.; Wei, S.; Yi, X.; Xie, X.; and
Sang, J. 2024. CDEval: A Benchmark for Measuring the
Cultural Dimensions of Large Language Models. In Prab-
hakaran, V.; Dev, S.; Benotti, L.; Hershcovich, D.; Cabello,
L.; Cao, Y.; Adebara, I.; and Zhou, L., eds., Proceedings
of the 2nd Workshop on Cross-Cultural Considerations in
NLP, 1–16. Bangkok, Thailand: Association for Computa-
tional Linguistics.
Xu, S.; Leng, Y.; Yu, L.; and Xiong, D. 2025.
Self-
Pluralising Culture Alignment for Large Language Models.
In Chiruzzo, L.; Ritter, A.; and Wang, L., eds., Proceed-
ings of the 2025 Conference of the Nations of the Ameri-
cas Chapter of the Association for Computational Linguis-
tics: Human Language Technologies (Volume 1: Long Pa-
pers), 6859–6877. Albuquerque, New Mexico: Association
for Computational Linguistics. ISBN 979-8-89176-189-6.
Zhao, W.; Mondal, D.; Tandon, N.; Dillion, D.; Gray, K.;
and Gu, Y. 2024. WorldValuesBench: A Large-Scale Bench-
mark Dataset for Multi-Cultural Value Awareness of Lan-
guage Models. ArXiv:2404.16308 [cs].
Zheng, L.; Chiang, W.-L.; Sheng, Y.; Zhuang, S.; Wu,
Z.; Zhuang, Y.; Lin, Z.; Li, Z.; Li, D.; Xing, E. P.;
Zhang, H.; Gonzalez, J. E.; and Stoica, I. 2023.
Judg-
ing LLM-as-a-Judge with MT-Bench and Chatbot Arena.
ArXiv:2306.05685 [cs].
Zhong, Q.; Yun, Y.; and Sun, A. 2024.
Cultural Value
Differences of LLMs: Prompt, Language, and Model Size.
ArXiv:2407.16891 [cs] version: 1.

```
