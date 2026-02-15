---
title: "2024-Yuan-Cultural Palette Pluralising Culture Alignment via Multi-agent Palette - PDF Extract"
source_pdf: "2024-Yuan-Cultural Palette Pluralising Culture Alignment via Multi-agent Palette.pdf"
pages: 19
extracted_at: "2026-02-15T17:51:58.271445"
---

# PDF Extract: 2024-Yuan-Cultural Palette Pluralising Culture Alignment via Multi-agent Palette

**Source PDF:** 2024-Yuan-Cultural Palette Pluralising Culture Alignment via Multi-agent Palette.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

Cultural Palette: Pluralising Culture Alignment via Multi-agent Palette
Jiahao Yuan1,2,5, Zixiang Di1,2, Shangzixin Zhao2,3, Zhiqing Cui1,4, Hanqing Wang4,
Guisong Yang2, Usman Naseem5
1ECNU,
2USST,
3BNU,
4HKUST–GZ,
5MQ
jhyuan.cs@gmail.com, usman.naseem@mq.edu.au
Abstract
Large language models (LLMs) face challenges
in aligning with diverse cultural values despite
their remarkable performance in generation,
which stems from inherent monocultural biases
and difficulties in capturing nuanced cultural
semantics. Existing methods struggle to adapt
to unknown culture after fine-tuning. Inspired
by cultural geography across five continents,
we propose Cultural Palette, a multi-agent
framework that redefines cultural alignment
as an adaptive "color-blending" process for
country-specific adaptation. Our approach har-
nesses cultural geography across five continents
through three key steps: First, we synthesize
the Pentachromatic Cultural Palette Dataset
using GPT-4o, refining continental-level dia-
logues with Hofstede’s cultural dimensions to
establish foundational cultural representations.
Second, five continent-level alignment agents
form specialized cultural communities that gen-
erate region-specific draft responses. Third, a
Meta Agent employs Cultural MoErges to dy-
namically blend these cultural "colors" through
attention-gated parameter merging, akin to mix-
ing pigments on a palette, resolving conflicts
while preserving cultural nuances to produce
the final culturally-aligned response. Extensive
experiments across various countries demon-
strate that Cultural Palette surpasses existing
baselines in cultural alignment.
1
Introduction
Large Language Models (LLMs), such as GPT-4
(Achiam et al., 2023), have shown remarkable per-
formance in aligning with human values for real-
world applications by incorporating diverse per-
spectives (Han et al., 2024; Sorensen et al., 2024a)
and preferences (Ouyang et al., 2022; Chen et al.,
2024) through specific fine-tuning and alignment
techniques (Hu et al., 2022; Ouyang et al., 2022).
However, alignment with human values is predom-
inantly influenced by pluralistic, multicultural fac-
tors including traditions, societal norms and more
(A) Country-specific Alignment
……
(B) Country-joint Alignment
Meta Agent
 Africa
America
Oceania
Europe
Asia
(C) Cultural Palette
Figure 1: Comparison between (A) country-specific
alignment (Li et al., 2024a,b; Feng et al., 2024), (B)
country-joint alignment (Li et al., 2024c,a) and (C) Cul-
tural Palette.
(Feng et al., 2024), especially in our multicul-
tural society, necessitating LLMs to perceive cross-
cultural differences and reflect pluralistic feedback
(Sorensen et al., 2024b; Feng et al., 2024) to avoid
mono-cultural bias (Shi et al., 2024) risked by mere
RLHF (Ouyang et al., 2022). Early studies pri-
marily involves collecting cultural data corpora for
fine-tuning to enhance cultural-awareness in LLMs
(Chan et al., 2023; Lin et al., 2024; Kirk et al.,
2024), while extremely time-consuming.
Recent research has explored two primary ap-
proaches to integrating cultural elements into
LLMs: (i) multi-culture data composition for
alignment, which simulates social surveys to syn-
thesize culture-specific corpora (Li et al., 2024b;
Shi et al., 2024), cultural value preference choices
(Li et al., 2024a; Xu et al., 2025) seeded from the
World Values Survey (WVS) (Haerpfer et al., 2022)
or PRISM dataset (Kirk et al., 2024) collecting pref-
erences for LLMs responses across cultural regions
for fine-tuning and alignment training, which is
limited by underrepresented cultures and may lead
to overfitting and value leakage from the WVS
1
arXiv:2412.11167v4  [cs.CL]  2 Jan 2026

--- Page 2 ---

benchmark (Zhou et al., 2023). (ii) multi-culture
community mechanisms, which leverage pluralis-
tic feedback among multi-agent (Feng et al., 2024;
Lake et al., 2024) yet struggles with unseen cultures
(Feng et al., 2024). In summary, pluralistic cultural
alignment for LLMs encounters three major limita-
tions: (1) Existing alignment techniques like RLHF
(Ouyang et al., 2022; Hong et al., 2024) often
neglect intersectional identities and marginalized
viewpoints between countries instead of among
community, limiting the models’ ability to provide
culturally inclusive outputs.(2) Existing datasets
for pluralistic cultural alignment mainly synthe-
size multiple-choice questions for cultural prefer-
ence seeded from WVS benchmark for fine-tuning,
lacking cultural dialogues needed for nuanced un-
derstanding. (3) Cultural norms evolve over time;
however, current methods lack effective paradigms
to adapt to this fluidity. Requiring fine-tuning on
country-specific corpora (Li et al., 2024a; Xu et al.,
2025) to construct cultural community (Sorensen
et al., 2024b; Feng et al., 2024) leads to inflexibility
and limited practicality (Xu et al., 2025).
To address above limitations, we propose Cul-
tural Palette, a framework integrating the core cul-
tural "colors" of five continents 1 (Crang, 2013),
collectively forming a palette that symbolizes
global cultural diversity via multi-agent coordina-
tion grounded on cultural geography findings
that culture differences among global coun-
tries are profoundly shaped by geographical in-
fluences within cultural evolution and spread
across five continents (Crang, 2013). As depicted
in Fig. 1, Cultural Palette first generate cultural
dialogues based on the PRISM dataset (Kirk et al.,
2024) for purifying responses representing the cul-
tural characteristics of five continents (Sec. 3) un-
der Hofstede’s cultural dimensions (Insights, 2021)
for perceiving culture differences (Hofstede, 2009),
conceptualized as primary colors for cultural align-
ment (Sec. 4.1) and then coloring five continent
cultures to form a multi-agent cultural community
(Sec. 4.2). Our key contributions are as follows:
• To the best of our knowledge, we introduce
the first Cultural Palette framework that mod-
els cultural alignment as dynamic blending
via Cultural MoErges, outperforming four
country-specific and joint alignment methods.
• We release the Pentachromatic Cultural
1We adopt the five-continent definition from Buschmann
and Nolde (2018): Africa, America, Asia, Europe & Oceania.
Palette Dataset, a diverse collection of cul-
tural dialogues synthesized using LLMs and
refined using Hofstede dimensions to capture
cultural semantics across five continents.
• We propose a multi-agent framework that
coordinates five continent-level drafting
agents with a meta agent for country-level
alignment. Extensive experiments across 18
countries demonstrate consistent gains over
five pluralistic alignment methods.
2
Related Work
Pluralistic Cultural Alignment.
Existing align-
ment techniques, such as DPO (Rafailov et al.,
2024) and ORPO (Hong et al., 2024) guide LLMs
to learn from preferred-signal data but do not ac-
count for cultural factors. To enhance pluralistic
culture alignment in LLMs, existing researches
focus on aligning with specific countries or val-
ues (Huang et al., 2024; Xu et al., 2025) via fine-
tuning (Li et al., 2024a,b; Huang et al., 2024; Xu
et al., 2025) and alignment (Kirk et al., 2024; Li
et al., 2024d; Guo et al., 2025), yet remains con-
strained by reliance on inherent cultural values
(Feng et al., 2024; Vamplew et al., 2024). To al-
leviate the above dependencies, recent research
leverages LLMs’ zero-shot capabilities (Kojima
et al., 2022; Li et al., 2024b) for cultural alignment
through multi-agent collaboration, introducing a
cultural-aligned judger LLM to summarize com-
munity comments via Overton, steerable, and dis-
tributional modes (Sorensen et al., 2024b; Feng
et al., 2024; Shetty et al., 2025), while challenges
persist in interacting with unseen culture (Feng
et al., 2024). To further address the complexities
of cultural diversity, we propose a novel approach
inspired by cultural evolution across five continents
(Crang, 2013). By conceptualizing these continen-
tal cultures as fundamental colors on a palette, we
introduce a multi-agent framework integrated with
a Cultural MoErges (Goddard et al., 2024) mech-
anism integrating semantic relationships at both
continent and country levels to dynamically blend
colors adapting to judging diverse cultural align-
ment and ensuring nuanced and context-aware re-
sponse through multi-agent collaboration.
Data Synthesis for Cultural Alignment.
Align-
ing LLMs for cultural pluralism—whether through
fine-tuning (Li et al., 2024a,b; Shi et al., 2024),
alignment (Kirk et al., 2024; Li et al., 2024d; Guo
et al., 2025), or agent-based approaches (Sorensen
2

--- Page 3 ---

et al., 2024b; Feng et al., 2024)—requires ex-
tensive, culture-specific datasets. While existing
datasets like PRISM (Kirk et al., 2024) collect user
feedback on LLM responses across diverse coun-
tries, they primarily focus on preference ranking
rather than generating culturally nuanced dialogues,
limiting their utility for training models to under-
stand implicit cultural norms (Chen et al., 2024).
Recent studies have demonstrated that self-instruct
(Wang et al., 2023) or multi-agent (Li et al., 2024a)
can effectively synthesize culturally nuanced data
through LLM-driven multi-step generation and re-
finement, including expanding datasets based on
the World Values Survey (WVS) (Haerpfer et al.,
2022) to study cultural dominance and alignment,
with benchmarks such as CultureLLM (Li et al.,
2024a), CulturePark (Li et al., 2024b), and Cul-
tureSPA (Xu et al., 2025). However, LLM-driven
data synthesis, seeded from the WVS for multiple-
choice data pairs, may introduce biases in cul-
tural options and lead to value leakage from the
WVS benchmark (Zheng et al., 2023; Zhou et al.,
2023). To overcome these limitations, we expanded
Prism (Kirk et al., 2024) to cultural dialogues from
five continents, creating Pentachromatic Cultural
Palette Dataset (Sec. 3) through self-feedback con-
trastive aggregation of cultural differences.
Model Merging.
LLMs trained on a single cor-
pus often suffer from limited generalization and
suboptimal decision-making, as they may converge
to local optima that restrict efficiency and versa-
tility across tasks (Lawson and Qureshi, 2024;
Yang et al., 2024b).
To address this, prior
work explores collaborative model merging strate-
gies—such as Task Arithmetic (Ilharco et al., 2023),
Ties (Yadav et al., 2024), and Model Stock (Jang
et al., 2025)—to improve performance on complex
decision-making (Lawson and Qureshi, 2024) and
generation tasks (Pourreza et al., 2024). More re-
cently, MoErges (Goddard et al., 2024; Tang et al.,
2024; Jiang et al., 2024) unifies model merging
with Mixture-of-Experts architectures through an
untrainable design, initializing MoE MLP layers
with task-specific model weights.
Building on
these advances, we investigate the role of model
merging in culturally grounded decision-making by
systematically comparing merging-based methods
with cultural joint training approaches (Xu et al.,
2025; Li et al., 2024a). Furthermore, we ground
our proposed Cultural MoErges in palette theory,
demonstrating how continent-level cultural repre-
sentations can be dynamically composed to foster
country-level cultural pluralism.
3
Pentachromatic Cultural Palette
Dataset
We contribute a Pentachromatic Cultural Palette
dataset with the diverse cultural semantics and val-
ues across five continents in social dialogues.
Dataset Construction.
Cultural differences in
evolution across five continents (Crang, 2013)
shape values and semantics in different coun-
tries. While existing datasets like PRISM (Kirk
et al., 2024) collect preference rankings, they lack
nuanced dialogues necessary for training mod-
els to understand context-specific norms. To ad-
dress this, we propose a Pentachromatic Cultural
Palette dataset, built from PRISM, to capture cul-
tural nuances essential for reflecting the full di-
versity of cultural semantics in social dialogues.
Following (Li et al., 2024c), We enhance cul-
tural richness through a multi-step data synthe-
sis process powered by GPT-4o, utilizing user
queries {Queryj}n
j=1 from the PRISM dataset.
As shown in Fig. 2, our pipeline begins with
a self-instruct (Wang et al., 2023) step to gen-
erate initial continent-aware responses.
These
responses then undergo a critique phase based
on cross-continent feedback to identify divergent
norms. Finally, in the continent-specific aggre-
gation stage, each response is polished through
an iterative self-refinement loop (Madaan et al.,
2024).
Within this loop, the model acts as a
self-judge to iteratively enhance the response, en-
suring cultural relevance while preventing cross-
cultural contradictions. This process is capped
at a maximum of Max = 3 rounds and ter-
minates early once a response passes prede-
fined quality checks.
And finally we get the
Pentachromatic Cultural Palette Dataset 2, rep-
resented as {(Queryj, Responsecontinent
j
)}n
j=1,
where continent ∈{Africa, Asia, Europe, Amer-
ica, Oceania}.
4
The Cultural Palette Framework
Following Wang et al. (2025), our multi-agent
cultural palette encompasses a country-specific
2Appendix A.1 details the multi-step synthesis prompts,
Appendix A.2 reports dataset scale, and Fig. 3 validates the
five-continent base colors. All synthesized data undergoes
rigorous human ethics review for cultural fairness and safety
(Kirk et al., 2024; Li et al., 2024a).
3

--- Page 4 ---

Figure 2: Architecture of Cultural Palette consisting of continent-level alignment on Pentachromatic Cultural Palette
Dataset (Sec. 3), Cultural MoErges for Meta Agent (Sec. 4.1) and Multi-agent Cultural Palette (Sec. 4.2). Details of
our ORPO alignment loss formulation are deferred to Appendix B for brevity.
Meta Agent (Sec. 4.1) aggregating drafts from five
continent-level cultural communities (4.2).
4.1
Cultural Palette for Meta Agent
Joint/Merging Alignment.
After constructing
the Pentachromatic Cultural Palette dataset, we
leverage it to perform continent-level alignment for
LLMs as cultural decision-maker judger aligned
with users, ensuring culturally relevant outputs
tailored to diverse regions. Inspired by Li et al.
(2024c), we introduce two alignment strategies to
highlight the benefits of model merging for overall
cultural pluralism. The first strategy, joint align-
ment, integrates all cultural dialogue data into a
single LLM. The second strategy involves creat-
ing separate models for each culture, which are
then merged into a unified LLM using separately
various merging techniques including Ties (Yadav
et al., 2024), Model Stock (Jang et al., 2025) and
MoErges (Goddard et al., 2024; Jiang et al., 2024)
to demonstrate that MoErges exhibits the greatest
potential for cultural alignment (see Sec. 5.2).
Cultural MoErges (CM) for Meta Agent.
In-
spired by the merging paradigm of MoErges (God-
dard et al., 2024; Tang et al., 2024), we propose
Cultural MoErges for Meta Agent to merge cultural
knowledge of all five continent-level experts as
a shared resource, enabling dynamic adaptation
to country-specific contexts following Goddard
et al. (2024) while acting as a global cultural
reviewer. Five continent-aligned models EGroup =
{EAfrica, EAsia, EEurope, EAmerica, EOceania}
are
trained on region-specific datasets, sharing a
base LLM architecture but differing in FFN
components following (Feng et al., 2024), and
the activation mechanism dynamically adjusts
expert
contributions
through
a
continent-to-
country
aware
gate
that
computes
weights
G(P) ∈R5 to prioritize expert contributions
based on national cultural cues in user prompt
P via: G(P) = Softmax(hiddenP · Wg), with
Wg
∈
Rd×5 initialized via hidden states of
continent-level system prompts (e.g., "You are
a knowledge chatbot about {continent}...") and
hiddenP derived from the base LLM’s encoding
4

--- Page 5 ---

of P such that G(P) blend experts’ parameters
into LLMmeta’s architecture following MoErges
paradigm (Wang et al., 2025), the Meta Agent’s
parameter space Θmeta is defined as:
Θmeta = Θshared ⊕

X
C∈EGroup
G(P) · ΘFFN
C

. (1)
where Θshared
⊂Θbase denotes frozen shared
parameters inherited from the base LLM and
ΘFFN
C
represents the FFN parameters of continent-
level expert C, dynamically fused via Softmax-
normalized weights G(P). Empirical experiments
in Sec. 5.4 demonstrate that Cultural MoErges out-
performs alternative strategies in achieving both
cultural pluralism and country-specific alignment.
4.2
Multi-agent Cultural Palette
As illustrated in Fig. 2, multi-agent cultural palette
consist of draft from community comments aligned
with five continents, self-regulated aggregation and
final decision from Meta Agent.
Stage 1:
Cultural Draft (CD).
Given a
country-specific question P
that includes a
target country C and a query Q, we engage
a continent-level LMs community EGroup
=
{EAfrica, EAsia, EEurope, EAmerica, EOceania},
each acted as a proxy for a regional community
voice informed by local norms, rhetorical patterns,
and sociocultural context.
While C is often
closely affiliated with one or more continents, all
community LMs are jointly activated to span both
proximate and distal cultural standpoints aligned
with pluralistic roadmap (Sorensen et al., 2024b),
promoting culturally diverse yet contextually
coherent perspectives (Crang, 2013), forming a
pluralistic Cultural Draft Draft via culture-aware
prompting Pdraft:
Draft =
X
E∈EGroup
Continent ⊕E(Q, Pdraft).
(2)
where ⊕denotes the association of the response
with its continent tag Continent.
Stage 2:
Self-regulated Aggregation (SR).
While continent-level LMs in the community
contribute diverse—and occasionally conflict-
ing—cultural standpoints, the objective is not to
reconcile these differences but to reinterpret them
through the lens of the target country, thereby sup-
porting downstream alignment with the country-
(A) PRISM
(B) Cultural Palette
Africa
America
Asia
Europe
Oceania
Figure 3: Comparative analysis of semantic repre-
sentations on the PRISM and Pentachromatic Cul-
tural Palette datasets using Multilingual embeddings
(microsoft/Multilingual-MiniLM-L12-H384) with
PCA-based dimensionality reduction. Data points are
color-coded by continent, based on the country associ-
ated with each QA pair.
specific response distribution. To this end, we in-
troduce a Self-regulated Aggregation mechanism,
wherein LLMmeta, activated under country C via
Cultural Merge parameter space (Sec. 4.1), recon-
textualizes each regional draft according to cul-
turally encoded priors aligned with C.
Rather
than flattening disagreement, LLMmeta preserves
both consonant and dissonant perspectives, reshap-
ing them through a culturally grounded filter that
centers C’s normative worldview. Inspired by re-
flective adaptation principles in formative learn-
ing (Nicol and Macfarlane-Dick, 2006), LLMmeta
serves as a cultural interpreter—transforming het-
erogeneous inputs into a coherent intermediate re-
sponse, denoted as Answerregulate, that preserves
cross-cultural plurality while aligning with the
socio-contextual frame of country C.
Stage 3: Final Decision.
Conditioned on the in-
termediate output Answerregulate, the meta agent
LLMmeta synthesizes a culturally grounded re-
sponse using the final decision prompt Pfinal. Lever-
aging the aggregated drafts as contextual input, it
generates a country-specific answer Answerfinal
and distribution Pgen that reflects the normative
worldview of target country C, supporting post-
hoc cultural alignment evaluation by comparing
Pgen with empirical response distributions Pgold
(Sec. 5.2), ultimately enabling continent-to-country
cultural alignment.
5
Experiments
5.1
Models and Implementation
Data Synthesis.
We utilized the original ques-
tions from the PRISM dataset (Kirk et al., 2024),
5

--- Page 6 ---

which comprises 7,805 questions sourced from 75
birth countries. To achieve balanced representation,
we augmented it by synthesizing 7,805 questions
per continent, ensuring equal distribution among
five continents and resulting in a total of 39,025
question-answer pairs, with each continent having
31220 preference pairs derived from the interac-
tions between every two continents. As shown
in Fig. 3, the PRISM dataset’s substantial distri-
butional overlap across continents underscores its
limitations in capturing cultural distinctions, pos-
ing challenges for modeling nuanced cultural seg-
mentation and aligning with region-specific appli-
cations. In contrast, our Pentachromatic Cultural
Palette dataset demonstrates superior clustering,
with data points forming distinct, continent-specific
groups that effectively model cultural uniqueness
and enable more accurate, culturally aligned rep-
resentations. The distribution of topics and conti-
nents are detailed in Appendix A.2.
Cultural Alignment.
We conducted all experi-
ments using Llama3.1-8B-Instruct (Dubey et al.,
2024) and Qwen2.5-7b-Instruct (Yang et al.,
2024a). Additionally, we employed five continent-
specific alignments with ORPO (Hong et al., 2024),
a parameter-efficient monolithic alignment method,
on our Pentachromatic Cultural Palette Dataset, uti-
lizing MS-Swift (Zhao et al., 2025) for alignment
and MergeKit (Goddard et al., 2024) for merging
on two NVIDIA A100 GPUs (see Appendix B for
experiment setting & alignment loss details). For
model training and evaluation, we partitioned our
dataset was split 9:1 for training and testing, with
the test set evaluating Cultural MoErges against
alternative alignment methods.
5.2
Datasets and Tasks
Task 1: Cultural Alignment w/ NLI evaluation.
To evaluate Cultural MoErges against alternative
merging methods and alignment strategies, we mea-
sure LLMs’ ability to generate continent-level re-
sponses aligned with cultural values. Following
Feng et al. (2024), we use a DeBERTa-v3-large
NLI model fine-tuned on standard NLI datasets
(Sileo, 2024) to compute a semantic-consistency
score as the Entailment probability between gold
values Rgold and LLM-generated responses Rllm:
Ssemantic = P(Entailment | Rgold, Rllm)×100% ∈[0, 100],
(3)
where higher percentages indicate stronger align-
ment with the gold-standard cultural values.
Task 2: Cultural Palette w/ GlobalOpinionQA.
Following Feng et al. (2024); Xu et al. (2025), we
compute alignment scores Salign for 18 countries
shown in Table 1 across five continents using the
GlobalOpinionQA dataset (DURMUS et al., 2024),
which aggregates global survey data. For each
country-level survey question, LLMs are prompted
to integrate national context and generate probabil-
ity distributions Pgen over answer options, which
are then compared to ground-truth survey response
distribution Pgold via Jensen-Shannon distance to
quantify cultural alignment:
Salign = 1 −1
2KL(Pgen ∥M) −1
2KL(Pgold ∥M).
(4)
where M is the average distribution of Pgen and
Pgold, and KL denotes the Kullback-Leibler diver-
gence. Higher Salign indicates better cultural align-
ment with real-world survey distributions.
5.3
Baselines
We first evaluated Cultural MoErges against four
baseline alignment strategies: (1) Prompting: We
promote cultural alignment by appending instruc-
tions via the same prompting template as culture-
aware prompting following (Feng et al., 2024;
Xu et al., 2025); (2) Joint: Following Xu et al.
(2025), we implement culturally joint alignment
with ORPO (Hong et al., 2024) for overall cultural
LLM alignment; (3) Tie: Following Yadav et al.
(2024), we merge LLMs among continent-specific
models by resetting minor fine-tuned parameters,
resolving sign conflicts, and merging parameters
with consistent signs; (4) Model Stock: effec-
tively integrate fine-tuned LLMs across continent-
specific applications (Jang et al., 2025).
Subsequently, we compare Cultural Palette with
five classical and latest baselines on Llama3.1-
8B-Instruct (Dubey et al., 2024) and Qwen2.5-7b-
Instruct (Yang et al., 2024a): (1) Vanilla: Follow-
ing (Feng et al., 2024), we directly employ LLM to
generate responses according to user queries with-
out any modifications. (2) Prompting: We follow
(Feng et al., 2024) in promoting cultural pluralism
with the same instruction “Make sure your response
reflects diverse values and perspectives”. (3) Joint:
Xu et al. (2025) adopted joint cultural alignment for
comprehensive LLM alignment with culture-aware
prompting. (4) Mixture-of-Experts (MoE): User
queries are matched to the best-suited community
LM, which generates culturally aligned responses.
(5) Modular: Feng et al. (2024) proposed three
6

--- Page 7 ---

Figure 4: Comparison of semantic-consistency alignment score between our Cultural Palette and other methods
(Prompting, Joint) and merging strategies (Tie and Model Stock) on Llama3.1-8B-Instruct and Qwen2.5-7b-Instruct.
forms of multi-agent collaboration, including Over-
ton, steerable, and distributional modes.
5.4
Main Result
Cultural MoErges achieves superior alignment
with continent-level values and perspectives.
As shown in Fig. 4, Cultural MoErges consistently
achieves the strongest overall semantic-alignment
performance across continents, outperforming both
alignment-based and parameter-merging baselines.
Prompting and Joint alignment methods exhibit
limited regional adaptability, yielding substan-
tially lower scores under continent-specific eval-
uation (e.g., 59.58% in Africa and 60.79% in
Asia under Prompting on LLaMA-based models).
Parameter-merging approaches, including Model
Stock and Tie, provide moderate improvements
but display noticeable cross-continent inconsis-
tency (e.g., 71.13% in Europe versus 65.87% in
Oceania under Tie on Qwen2.5-7B-Instruct). In
contrast, Cultural MoErges enables coherent in-
tegration of continent-level reasoning, resulting
in consistent gains across regions. Specifically, it
achieves 71.05% in Africa and 70.76% in Oceania
on LLaMA-based models, and 77.88%–79.49% on
Qwen2.5-7B-Instruct, surpassing strong modular
and merging baselines by approximately 1.5–3.0
percentage points. These results indicate that Cul-
tural MoErges effectively captures continent-level
cultural structure while maintaining semantic con-
sistency. A qualitative case study for culture align-
ment on question-answering w/ NLI evaluation is
detailed in Appendix C.1.
Cultural Palette achieves superior real-world
cultural alignment.
(1) Best Performance: As
reported in Table 1, Cultural Palette consistently
attains the highest cultural alignment scores across
two LLMs, outperforming all baselines in 18 coun-
tries spanning five continents. On LLaMA3.1-8B-
Instruct, Cultural Palette achieves an average score
of 75.90%, surpassing the strongest baseline Mod-
ular (73.82%) by 2.08 percentage points, with pro-
nounced gains in Asia (3.73) and Africa (5.28),
regions where prior methods often struggle to cap-
ture cultural nuance.
On Qwen2.5-7B-Instruct,
the improvement is even more significant: Cul-
tural Palette reaches 73.64%, exceeding Modular
by 4.13 percentage points, with consistent gains
across America (6.35), Europe (0.48), and Asia
(3.08). (2) Alignment Fidelity: Beyond Salign
(Feng et al., 2024; Xu et al., 2025), we evaluate
distributional fidelity using Pearson correlation
with ground-truth survey data. Modular, which
relies on country-specific supervision, generalizes
poorly (Pearson r = −0.044). In contrast, Cul-
tural Palette, trained with continent-level priors
and transferred to individual countries, achieves
substantially higher correlation (r=0.555). This
demonstrates that coarse-to-fine regional transfer
improves stability and generalization while out-
performing direct country-level learning, which is
prone to data sparsity and overfitting. Detailed case
studies on GlobalOpinionQA and correlation analy-
ses are provided in Appendix C.1 and Appendix D.
(3) GPT-4o as Cultural Teacher: GPT-4o attains
a baseline alignment score of 71.88%, and our syn-
thetic dataset (Sec. 3) effectively enhances SLMs’
cultural alignment, surpassing GPT-4o itself in sev-
eral regions.
Ablation Study.
To quantify the contribution of
each component, we perform three ablations (Ta-
ble 1): (i) w/o Cultural MoErges (CM): remov-
ing cross-cultural adaptation via CM; (ii) w/o Cul-
7

--- Page 8 ---

America
Europe
Asia
Africa
Oceania
Avg
USA
CAN
BOL
BRA
GBR
NLD
DEU
UKR
CHN
RUS
IND
THA
KEN
NGA
ETH
ZWE
AUS
NZL
GPT-4o
72.47
70.28
72.63
69.44
71.01
69.09
73.04
72.96
72.18
74.45
72.16
72.12
73.50
72.16
72.39
74.40
70.44
69.08
71.88
LLAMA3.1-8B-INSTRUCT (Dubey et al., 2024)
Vanilla
67.81
65.46
66.46
66.88
59.21
64.30
63.95
59.13
62.76
62.72
66.18
63.01
67.54
66.80
67.31
58.22
64.17
55.68
63.76
Prompting
69.18
67.81
69.43
68.64
60.90
66.65
67.46
63.15
65.81
68.09
69.67
66.22
69.12
68.50
69.51
59.48
67.59
58.49
66.43
Joint
70.10
69.24
70.94
66.35
66.93
70.27
70.54
66.11
67.41
69.21
70.12
63.29
67.14
68.44
66.75
61.34
68.41
60.06
67.37
Moe
73.91
70.97
76.09
75.50
73.92
76.69
72.48
72.87
76.52
74.41
73.02
75.07
74.85
78.76
69.57
70.30
65.25
62.77
72.94
Modular
75.14
75.70
76.60
76.29
76.46
76.71
74.98
71.69
74.16
73.56
74.21
71.76
71.63
70.03
70.05
74.80
72.42
72.57
73.82
Ours
75.85
77.56
77.88
75.83
76.48
76.53
76.38
77.69
77.12
77.67
74.32
75.54
76.12
77.07
73.65
74.82
72.14
73.50
75.90
w /o CM
70.12
72.42
72.77
72.37
69.31
71.01
71.05
70.12
71.52
72.39
71.84
69.36
70.68
70.57
66.23
69.66
69.80
69.51
70.60
w /o CD
72.25
73.77
73.80
74.27
62.23
74.47
73.25
72.37
73.70
75.97
75.99
71.90
76.19
72.94
67.74
60.09
73.44
69.01
71.85
w /o SR
75.54
77.03
77.39
75.25
75.27
76.32
76.54
77.19
77.87
77.42
73.49
74.57
74.73
76.08
71.93
73.89
71.67
71.04
75.18
QWEN2.5-7B-INSTRUCT (Yang et al., 2024a)
Vanilla
61.50
60.54
62.67
63.22
63.86
63.66
61.05
59.32
63.78
60.77
60.62
62.12
59.87
63.94
63.56
57.43
54.40
58.84
61.18
Prompting
63.18
63.80
63.48
64.76
64.77
64.52
61.86
62.75
64.99
61.42
61.35
62.20
61.60
63.15
61.39
56.77
52.05
54.44
61.58
Joint
70.00
67.47
65.03
67.36
66.90
68.74
68.22
63.21
63.27
62.80
69.25
65.77
69.36
69.35
66.67
66.20
68.00
62.79
66.69
Moe
73.56
72.59
74.31
71.07
70.96
68.47
68.93
66.76
68.67
68.14
66.15
68.65
66.17
69.51
70.63
65.99
70.51
65.49
69.25
Modular
72.64
68.03
72.43
73.66
69.21
71.21
72.78
75.57
73.01
74.79
66.62
72.19
69.44
70.32
62.04
70.52
57.58
59.09
69.51
Ours
75.50
73.92
78.83
76.71
69.77
70.89
73.91
75.58
73.46
76.09
72.87
73.02
76.51
74.51
70.30
69.25
74.85
69.57
73.64
w /o CM
68.79
67.46
69.63
68.93
62.97
66.19
69.48
68.56
68.83
68.01
69.26
66.57
67.45
66.77
62.74
65.47
66.87
67.16
67.29
w /o CD
72.62
68.22
68.52
71.35
49.30
64.55
71.96
72.77
71.79
74.86
73.98
63.07
69.95
72.50
62.86
46.48
68.05
58.67
66.75
w /o SR
72.45
70.84
72.78
72.62
67.36
69.24
71.83
72.05
73.68
74.26
73.06
70.25
72.11
73.30
72.53
74.24
69.85
68.05
71.69
Table 1: Comparison of culture alignment score (converted to percentages) between Cultural Palette and baselines,
evaluated across 18 countries grouped by region: (1) America: USA (United States), CAN (Canada), BOL (Bolivia),
BRA (Brazil); (2) Europe: GBR (United Kingdom), NLD (Netherlands), DEU (Germany), UKR (Ukraine); (3)
Asia: CHN (China), RUS (Russia), IND (India), THA (Thailand); (4) Africa: KEN (Kenya), NGA (Nigeria), ETH
(Ethiopia), ZWE (Zimbabwe); (5) Oceania: AUS (Australia), NZL (New Zealand).
tural Draft (CD): excluding continent-level cul-
tural explanations; and (iii) w/o Self-Regulate (SR):
eliminating the self-regulation mechanism that in-
tegrates multiple drafts. Removing CM causes
the largest performance drop: on Qwen2.5-7B-
Instruct, the average score decreases from 73.64%
to 67.29%, with substantial declines in Asia (4.03
percentage points) and Oceania (4.40 percentage
points). This highlights CM’s key role in ground-
ing country-level alignment through continent-level
priors, which provide semantic regularization and
enable cross-national transfer under data scarcity
or noisy cultural signals. Ablating CD also re-
sults in notable losses, particularly in semantically
diverse regions such as the Americas (3.70) and Eu-
rope (6.91), indicating that CD expands the model’s
hypothesis space with grounded alternatives that
guide downstream reasoning. Removing SR pro-
duces smaller but consistent drops, with an average
decrease of 1.95 percentage points, emphasizing
its role in integrating multiple drafts into a coher-
ent cultural response. These findings validate our
multi-agent alignment strategy: CD enriches se-
mantic priors with diverse perspectives, CM an-
chors them through coarse-to-fine structural trans-
fer, and SR fuses divergent outputs into a culturally
coherent response, together enhancing and stabiliz-
ing culture alignment.
6
Conclusion
In this work, we propose Cultural Palette, a novel
multi-agent framework for culturally pluralistic
alignment in LLMs, modeling five continental cul-
tures as primary colors. Powered by the Pentachro-
matic Cultural Palette Dataset and a self-regulating
Cultural MoErges mechanism, Cultural Palette
dynamically aggregates continent-level agents to
adapt across cultural contexts. Empirical results
reveal three key findings: (1) Cultural MoErges
enables dynamic composition of continent-level
agents, surpassing four modular and training-based
baselines in semantic consistency and cultural
adaptability; (2) Synthesizing diverse continen-
tal data alone suffices to achieve fine-grained
continent-to-country cultural alignment, enabling
practical adaptation to country-level nuances with-
out the need for country-specific data collection;
and (3) Cultural Palette consistently outperforms
five pluralistic alignment baselines across both se-
mantic and cultural alignment metrics. Our re-
search may inspire future studies on modeling plu-
ralistic alignment by leveraging continent-level
agents to adapt to specific countries and their
unique cultural contexts.
8

--- Page 9 ---

Limitations
Our Cultural Palette integrates the core cultural
"colors" of five continents with a Meta Agent that
blends these base colors into a unified multi-agent
framework, symbolizing global cultural diversity
(Crang, 2013). Extensive experiments and case
studies show that our multi-agent framework en-
hances the cultural sensitivity and adaptability of
LLMs. While the multi-agent setup introduces
some computational complexity, as noted in (Feng
et al., 2024), we have addressed this by implement-
ing optimization techniques such as efficient align-
ment (Dao, 2024; Zhao et al., 2025) and inference
(Kwon et al., 2023), effectively reducing compu-
tational burdens. As a result, our framework re-
mains competitive with other cultural alignment
techniques while ensuring better scalability. Addi-
tionally, We envision ongoing efforts to distill the
framework’s capabilities into smaller LLM vari-
ants, enabling more efficient deployment across a
broader range of applications and devices.
Finally, as highlighted by (Xu et al., 2025; Feng
et al., 2024), culture definition and cultural map
division are inherently diverse and multifaceted.
We validate our Cultural Palette with continent-to-
country alignment based on continental cultural
geography (Crang, 2013), offering a flexible frame-
work that can be adapted to other cultural maps
(Lechner and Boli, 2008; Inglehart and Welzel,
2010) and encouraging exploration of alternative
cultural divisions to expand the applicability of our
Cultural Palette
.
Ethical Considerations
This work builds on the public PRISM dataset (Kirk
et al., 2024) to construct the Pentachromatic Cul-
tural Palette Dataset for cultural alignment, in full
compliance with its usage policies. While aiming
to promote inclusivity and reduce bias, we recog-
nize potential risks of stereotyping or misrepresen-
tation. To address this, all generated data undergo
both model-in-the-loop and post-hoc human ethics
reviews for cultural sensitivity following Li et al.
(2024a). Our framework advances pluralistic, eq-
uitable representation via multi-agent alignment
and encourages continued expansion of culturally
diverse perspectives in alignment research.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, et al. 2023. Gpt-4 technical report.
arXiv preprint arXiv:2303.08774.
Rainer F Buschmann and Lance Nolde. 2018.
The
World’s Oceans: Geography, History, and Environ-
ment. Bloomsbury Publishing USA.
Alex J Chan, José Luis Redondo García, Fabrizio Sil-
vestri, Colm O’Donnel, and Konstantina Palla. 2023.
Harmonizing global voices: Culturally-aware mod-
els for enhanced content moderation. arXiv preprint
arXiv:2312.02401.
Daiwei Chen, Yi Chen, Aniket Rege, and Ramya Ko-
rlakai Vinayak. 2024.
Pal: Pluralistic alignment
framework for learning from heterogeneous prefer-
ences. In NeurIPS 2024 Workshop on Fine-Tuning in
Modern Machine Learning: Principles and Scalabil-
ity.
Mike Crang. 2013. Cultural geography. Routledge.
Tri Dao. 2024. Flashattention-2: Faster attention with
better parallelism and work partitioning.
In The
Twelfth International Conference on Learning Repre-
sentations.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, et al. 2024. The llama 3 herd of models. arXiv
preprint arXiv:2407.21783.
Esin DURMUS, Karina Nguyen,
Thomas Liao,
Nicholas Schiefer, Amanda Askell, Anton Bakhtin,
Carol Chen, Zac Hatfield-Dodds, Danny Hernandez,
Nicholas Joseph, et al. 2024. Towards measuring
the representation of subjective global opinions in
language models. In First Conference on Language
Modeling.
Shangbin Feng, Taylor Sorensen, Yuhan Liu, Jillian
Fisher, Chan Young Park, Yejin Choi, and Yulia
Tsvetkov. 2024. Modular pluralism: Pluralistic align-
ment via multi-llm collaboration. In Proceedings of
the 2024 Conference on Empirical Methods in Natu-
ral Language Processing, pages 4151–4171.
Charles Goddard, Shamane Siriwardhana, Malikeh
Ehghaghi, Luke Meyers, Vladimir Karpukhin, Brian
Benedict, Mark McQuade, and Jacob Solawetz. 2024.
Arcee’s mergekit: A toolkit for merging large lan-
guage models. In Proceedings of the 2024 Confer-
ence on Empirical Methods in Natural Language
Processing: Industry Track, pages 477–485.
Geyang Guo, Tarek Naous, Hiromi Wakaki, Yukiko
Nishimura, Yuki Mitsufuji, Alan Ritter, and Wei
Xu. 2025.
Care:
Aligning language models
for regional cultural awareness.
arXiv preprint
arXiv:2504.05154.
9

--- Page 10 ---

Christian Haerpfer,
Ronald Inglehart,
Alejandro
Moreno, Christian Welzel, Kseniya Kizilova, Jaime
Diez-Medrano, Marta Lagos, Pippa Norris, Eduard
Ponarin, and Bjorn Puranen. 2022. World values
survey: Round seven-country-pooled datafile version
5.0. Madrid, Spain & Vienna, Austria: JD Systems
Institute & WVSA Secretariat, 12(10):8.
Seungwook Han, Idan Shenfeld, Akash Srivastava,
Yoon Kim, and Pulkit Agrawal. 2024. Value aug-
mented sampling for language model alignment and
personalization. arXiv preprint arXiv:2405.06639.
Geert Hofstede. 2009. Geert hofstede cultural dimen-
sions.
Jiwoo Hong, Noah Lee, and James Thorne. 2024. Orpo:
Monolithic preference optimization without refer-
ence model. In Proceedings of the 2024 Conference
on Empirical Methods in Natural Language Process-
ing, pages 11170–11189.
Edward J Hu, Phillip Wallis, Zeyuan Allen-Zhu,
Yuanzhi Li, Shean Wang, Lu Wang, Weizhu Chen,
et al. 2022. Lora: Low-rank adaptation of large lan-
guage models. In International Conference on Learn-
ing Representations.
Huang Huang, Fei Yu, Jianqing Zhu, Xuening Sun,
Hao Cheng, Song Dingjie, Zhihong Chen, Mosen
Alharthi, Bang An, Juncai He, et al. 2024. Acegpt,
localizing large language models in arabic. In Pro-
ceedings of the 2024 Conference of the North Amer-
ican Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume
1: Long Papers), pages 8132–8156.
Gabriel Ilharco, Marco Tulio Ribeiro, Mitchell Worts-
man, Ludwig Schmidt, Hannaneh Hajishirzi, and Ali
Farhadi. 2023. Editing models with task arithmetic.
In The Eleventh International Conference on Learn-
ing Representations.
Ronald Inglehart and Chris Welzel. 2010. The wvs
cultural map of the world. World Values Survey.
Hofstede Insights. 2021. Hofstede cultural dimensions.
Dong-Hwan Jang, Sangdoo Yun, and Dongyoon Han.
2025. Model stock: All we need is just a few fine-
tuned models. In European Conference on Computer
Vision, pages 207–223. Springer.
Albert Q Jiang, Alexandre Sablayrolles, Antoine
Roux, Arthur Mensch, Blanche Savary, Chris Bam-
ford, Devendra Singh Chaplot, Diego de las Casas,
Emma Bou Hanna, Florian Bressand, et al. 2024.
Mixtral of experts. arXiv preprint arXiv:2401.04088.
Hannah Rose Kirk, Alexander Whitefield, Paul Rottger,
Andrew M Bean,
Katerina Margatina,
Rafael
Mosquera-Gomez, Juan Ciro, Max Bartolo, Adina
Williams, He He, et al. 2024. The prism alignment
dataset: What participatory, representative and indi-
vidualised human feedback reveals about the subjec-
tive and multicultural alignment of large language
models. Advances in Neural Information Processing
Systems, 37:105236–105344.
Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yu-
taka Matsuo, and Yusuke Iwasawa. 2022. Large lan-
guage models are zero-shot reasoners. Advances in
neural information processing systems, 35:22199–
22213.
Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying
Sheng, Lianmin Zheng, Cody Hao Yu, Joseph Gon-
zalez, Hao Zhang, and Ion Stoica. 2023. Efficient
memory management for large language model serv-
ing with pagedattention. In Proceedings of the 29th
Symposium on Operating Systems Principles, pages
611–626.
Thom Lake, Eunsol Choi, and Greg Durrett. 2024.
From distributional to overton pluralism: Investigat-
ing large language model alignment. In Pluralistic
Alignment Workshop at NeurIPS 2024.
Daniel Lawson and Ahmed H Qureshi. 2024. Merging
decision transformers: Weight averaging for forming
multi-task policies. In 2024 IEEE International Con-
ference on Robotics and Automation (ICRA), pages
12942–12948. IEEE.
Frank J Lechner and John Boli. 2008. World culture:
Origins and consequences. John Wiley & Sons.
Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana
Sitaram, and Xing Xie. 2024a. Culturellm: Incorpo-
rating cultural differences into large language models.
Advances in Neural Information Processing Systems,
37:84799–84838.
Cheng Li, Damien Teney, Linyi Yang, Qingsong Wen,
Xing Xie, and Jindong Wang. 2024b. Culturepark:
Boosting cross-cultural understanding in large lan-
guage models. Advances in Neural Information Pro-
cessing Systems, 37:65183–65216.
Junlong Li, Jinyuan Wang, Zhuosheng Zhang, and Hai
Zhao. 2024c. Self-prompting large language models
for zero-shot open-domain qa. In Proceedings of
the 2024 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Pa-
pers), pages 296–310.
Xinyu Li, Ruiyang Zhou, Zachary C Lipton, and
Liu Leqi. 2024d. Personalized language modeling
from personalized human feedback. arXiv preprint
arXiv:2402.05133.
Peiqin Lin, Shaoxiong Ji, Jörg Tiedemann, André FT
Martins, and Hinrich Schütze. 2024. Mala-500: Mas-
sive language adaptation of large language models.
arXiv preprint arXiv:2401.13303.
Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler
Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,
et al. 2024. Self-refine: Iterative refinement with
self-feedback. Advances in Neural Information Pro-
cessing Systems, 36.
10

--- Page 11 ---

David J Nicol and Debra Macfarlane-Dick. 2006. For-
mative assessment and self-regulated learning: A
model and seven principles of good feedback prac-
tice. Studies in higher education, 31(2):199–218.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback. Advances in neural in-
formation processing systems, 35:27730–27744.
Mohammadreza Pourreza, Ruoxi Sun, Hailong Li, Lesly
Miculicich, Tomas Pfister, and Sercan O Arik. 2024.
Sql-gen: Bridging the dialect gap for text-to-sql via
synthetic data and model merging. arXiv preprint
arXiv:2408.12733.
Rafael Rafailov, Archit Sharma, Eric Mitchell, Christo-
pher D Manning, Stefano Ermon, and Chelsea Finn.
2024. Direct preference optimization: Your language
model is secretly a reward model. Advances in Neu-
ral Information Processing Systems, 36.
Anudeex Shetty, Amin Beheshti, Mark Dras, and Usman
Naseem. 2025. VITAL: A new dataset for bench-
marking pluralistic alignment in healthcare. In Pro-
ceedings of the 63rd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 22954–22974, Vienna, Austria. Asso-
ciation for Computational Linguistics.
Weiyan Shi, Ryan Li, Yutong Zhang, Caleb Ziems,
Sunny Yu, Raya Horesh, Rogério Abreu De Paula,
and Diyi Yang. 2024.
Culturebank: An online
community-driven knowledge base towards cultur-
ally aware language technologies. In Findings of the
Association for Computational Linguistics: EMNLP
2024, pages 4996–5025.
Damien Sileo. 2024. tasksource: A large collection
of NLP tasks with a structured dataset preprocess-
ing framework. In Proceedings of the 2024 Joint
International Conference on Computational Linguis-
tics, Language Resources and Evaluation (LREC-
COLING 2024), pages 15655–15684, Torino, Italia.
ELRA and ICCL.
Taylor Sorensen, Liwei Jiang, Jena D Hwang, Sydney
Levine, Valentina Pyatkin, Peter West, Nouha Dziri,
Ximing Lu, Kavel Rao, Chandra Bhagavatula, et al.
2024a. Value kaleidoscope: Engaging ai with plural-
istic human values, rights, and duties. In Proceedings
of the AAAI Conference on Artificial Intelligence, vol-
ume 38, pages 19937–19947.
Taylor
Sorensen,
Jared
Moore,
Jillian
Fisher,
Mitchell Gordon, Niloofar Mireshghallah, Christo-
pher Michael Rytting, Andre Ye, Liwei Jiang,
Ximing Lu, Nouha Dziri, et al. 2024b. Position: a
roadmap to pluralistic alignment. In Proceedings
of the 41st International Conference on Machine
Learning, pages 46280–46302.
Anke Tang, Li Shen, Yong Luo, Nan Yin, Lefei Zhang,
and Dacheng Tao. 2024. Merging multi-task models
via weight-ensembling mixture of experts. In Forty-
first International Conference on Machine Learning.
Peter Vamplew, Conor F Hayes, Cameron Foale,
Richard Dazeley, and Hadassah Harland. 2024.
Multi-objective reinforcement learning: A tool for
pluralistic alignment. In Pluralistic Alignment Work-
shop at NeurIPS 2024.
Junlin Wang, WANG Jue, Ben Athiwaratkun, Ce Zhang,
and James Zou. 2025. Mixture-of-agents enhances
large language model capabilities. In The Thirteenth
International Conference on Learning Representa-
tions.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa
Liu, Noah A Smith, Daniel Khashabi, and Hannaneh
Hajishirzi. 2023. Self-instruct: Aligning language
models with self-generated instructions. In Proceed-
ings of the 61st Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 13484–13508.
Shaoyang Xu, Yongqi Leng, Linhao Yu, and Deyi Xiong.
2025. Self-pluralising culture alignment for large
language models. In Proceedings of the 2025 Con-
ference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human
Language Technologies (Volume 1: Long Papers),
pages 6859–6877.
Prateek Yadav, Derek Tam, Leshem Choshen, Colin A
Raffel, and Mohit Bansal. 2024. Ties-merging: Re-
solving interference when merging models.
Ad-
vances in Neural Information Processing Systems,
36.
An Yang, Baosong Yang, Binyuan Hui, Bo Zheng,
Bowen Yu, Chang Zhou, Chengpeng Li, Chengyuan
Li, Dayiheng Liu, Fei Huang, et al. 2024a. Qwen2
technical report. arXiv preprint arXiv:2407.10671.
Enneng Yang, Li Shen, Guibing Guo, Xingwei Wang,
Xiaochun Cao, Jie Zhang, and Dacheng Tao. 2024b.
Model merging in llms, mllms, and beyond: Meth-
ods, theories, applications and opportunities. arXiv
preprint arXiv:2408.07666.
Yuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang,
Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai
Wu, Baole Ai, Ang Wang, et al. 2025. Swift: a
scalable lightweight infrastructure for fine-tuning. In
Proceedings of the AAAI Conference on Artificial
Intelligence, volume 39, pages 29733–29735.
Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, and
Minlie Huang. 2023. Large language models are not
robust multiple choice selectors. In The Twelfth Inter-
national Conference on Learning Representations.
Kun Zhou, Yutao Zhu, Zhipeng Chen, Wentong Chen,
Wayne Xin Zhao, Xu Chen, Yankai Lin, Ji-Rong
Wen, and Jiawei Han. 2023. Don’t make your llm
an evaluation benchmark cheater.
arXiv preprint
arXiv:2311.01964.
11

--- Page 12 ---

Appendix of Cultural Palette
This supplementary material provides supplemen-
tary materials: Appendix A describes the con-
struction details of Pentachromatic Cultural Palette
dataset, Appendix B details the experimental setup
and hyperparameters, Appendix C presents qual-
itative case studies on cultural alignment across
w/ NLI evaluation (C.1) and w/ GlobalOpinionQA
(C.2), and Appendix D provides an additional quan-
titative continent-to-country correlation analysis
with Modular Pluralism (Feng et al., 2024), further
validating Cultural Palette’s effectiveness in bridg-
ing continent-level reasoning with country-level
cultural alignment.
A
Details for Pentachromatic Cultural
Palette Dataset
A.1
Prompt for Pentachromatic Cultural
Palette Dataset
Step1: Continent-aware Responses
Instruction
You are a knowledgeable chatbot special-
izing in {Continent}. Provide concise, ac-
curate, and culturally sensitive responses
tailored to user queries about {Continent}’s
geography, culture, history, and current af-
fairs. Ensure your responses demonstrate
respect and understanding of the diverse cul-
tures within {Continent}.
1. Understand Query Context:
Identify the topic and cultural relevance of
the user’s query (e.g., geography, culture,
history, or current events).
2. Generate Continent-aware Response:
Show respect for the diverse cultures, avoid-
ing assumptions or biased statements. High-
light the uniqueness and importance of spe-
cific cultural aspects when appropriate.
Examples:
Question: {Question} Answer: {Answer}
Input: {Question}
Output: {Continent-aware Response}
Figure 5: Prompt for continent-aware responses
Step2: Cross-continent Feedback
Instruction
Review the response for cultural clarity, en-
suring {Continent} perspectives are promi-
nent and free from interference by other
cultures {Other Continents}. If confusion
arises, provide improvement suggestions us-
ing Hofstede’s cultural dimensions:
1. Analyze Query Context:
Assess whether the response fully aligns
with the cultural, historical, and geographi-
cal relevance of {Continent}. Identify any
unnecessary elements or overlaps with other
continents’ cultural markers.
2. Refine Response for {Continent} Per-
spective:
Emphasize key cultural, historical, or envi-
ronmental aspects unique to {Continent}.
Remove any elements that might introduce
cultural interference or bias. Ensure the re-
sponse highlights community, tradition, and
respect for local customs.
3. Apply Hofstede’s Cultural Dimensions
Theory for Feedback:
- Power Distance (PDI): Does the response
reflect the balance between leadership (e.g.,
village chiefs) and community roles?
- Individualism vs. Collectivism (IDV):
Does it highlight collective well-being and
community-driven decisions?
- Masculinity vs. Femininity (MAS): Does
it prioritize care, cooperation, and harmony
over competition?
- Uncertainty Avoidance (UAI): Does it
address Oceania’s adaptability to change
while respecting traditions?
- Long-Term vs. Short-Term Orientation
(LTO): Does it balance preservation of tra-
ditions with immediate adaptability?
- Indulgence vs. Restraint (IVR): Does
it reflect the expressive and celebratory as-
pects of Oceanian cultures?
Input: {Continent-aware Responses}
Output: {Cross-continent Feedback}
Figure 6: Prompt for cross-continent feedback
12

--- Page 13 ---

Step3: Continent-specific Aggregation
Instruction
You are tasked with improving the following
response for the query {query} by incorpo-
rating the cross-continent review feedback.
1. Review Context Response:
Carefully read and analyze the Base Re-
sponse and Review Feedback provided.
Identify elements in the base response that
lack focus on {Continent} or introduce cul-
tural elements from other continents.
2. Apply Review Feedback:
Incorporate all suggestions from the review
feedback into the base response. Ensure
the revised response highlights {Continent}-
specific culture, history, and values and fo-
cus on {Continent} Perspectives, avoiding
any overlap with other cultural contexts.
Input:
Base Response: {Base response}
Review Feedback: {Review feedback}
Output: {Continentfocused Response}
Figure 7: Prompt for Continent-specific Aggregation
Step4: Self-Judge Refinement
Instruction
You are now a cultural self-judge. Your task
is to assess whether the aggregated response
reflects accurate, respectful, and continent-
specific perspectives for the user query. Crit-
ically evaluate the revised response based
on feedback, and decide whether further im-
provement is needed.
1. Evaluate Cultural Fidelity:
Check if the revised response aligns with
the core values, traditions, and worldview
of {Continent}. Is the response focused,
respectful, and specific? Does it avoid gen-
eralizations or unrelated cross-cultural ref-
erences?
2. Verify Feedback Integration:
Determine whether the suggestions from
cross-continent feedback have been fully
addressed. Are the earlier critiques resolved
in this version?
3. Quality Criteria for Acceptance:
Approve the response only if it meets all the
following: - Emphasizes cultural clarity and
salience - Integrates prior feedback - Avoids
cultural interference - Is concise, coherent,
and informative
Output:
If the response is acceptable, return: [Ap-
proved]
If the response requires revision, return:
[Revise] And explain what needs to be
changed.
Figure 8: Prompt for self-judge refinement to ensure
cultural alignment
A.2
Distribution in Pentachromatic Cultural
Palette Dataset
Figure 9 illustrates the distribution of topics and
continent over our Pentachromatic Cultural Palette
Dataset. The topics were categorized using a topic
modeling llm 3 which classifies the questions into
distinct thematic clusters. The distribution of conti-
nents, on the other hand, is evenly balanced, with
an equal number of questions synthesized for each
continent: Africa, America, Asia, Europe, and
Oceania.
3https://huggingface.co/classla/multilingual-IPTC-news-
topic-classifier, License: cc-by-sa-4.0
13

--- Page 14 ---

Figure 9: Distribution of topics and continents in Pentachromatic Cultural Palette Dataset.
B
Experiment Details
Experiment Setting.
We adopt the ORPO
method (Hong et al., 2024) with default hy-
perparameters for Llama3.1-8B-Instruct (Dubey
et al., 2024) and Qwen2.5-7B-Instruct (Yang et al.,
2024a), using a learning rate of 5e-5 for 2 epochs.
We select the average result from five runs as the
experimental results.
Alignment Implement.
We align continent-
specific LLMs using ORPO (Hong et al., 2024),
optimizing the following loss, LORPO:
LORPO = 1
n
n
X
i=1
"
ℓ(Pref(i), Query(i))
|
{z
}
+ λ
4
X
k=1
 
−log σ
 
log pθ(Pref(i) | Query(i))
pθ(Rej(i)
k
| Query(i))
!!
|
{z
}
(b) Cross-continent Contrastive Alignment
#
(5)
where ℓ(Pref(i), Query(i)) denotes the continent-
specific supervised fine-tuning (SFT) loss, align-
ing the LLM to generate the preferred response
Pref(i) given query Query(i). The second term en-
forces cross-continent contrastive alignment by pe-
nalizing less-preferred responses Rej(i)
k from other
continents that diverge from the preference of the
target region. We set the odds ratio λ = 0.1, fol-
lowing MS-Swift (Zhao et al., 2025), to balance
in-continent preference alignment with interconti-
nental contrastive separation.
Licenses.
The licenses for the codes used in our
work are listed in Table 2.
14

--- Page 15 ---

Resources
Type
Link
License
MergeKit (Goddard et al., 2024)
Code
https://github.com/arcee-ai/mergekit
LGPL-3.0 license
MS-Swift (Zhao et al., 2025)
Code
https://github.com/modelscope/ms-swift
Apache-2.0 license
Table 2: Licenses for the software libraries utilized in our work.
C
Case Study
C.1
Case Study for Cultural Alignment w/
NLI evaluation
To validate our Cultural Palette’s efficacy, we con-
ducted a case study (Tables 3 & 4) addressing the
question, "What happens when we die?" , to demon-
strate how our Cultural Palette generates diverse re-
sponses across continents, reflecting each region’s
unique perspective on death. In Oceania, the re-
union of souls with ancestors is emphasized, high-
lighting the cultural significance of these traditions.
In Africa, the continuity of the soul and its con-
nection to ancestors reinforce communal bonds. In
Asia, beliefs such as reincarnation, enlightenment,
and ancestor worship illustrate varied views of the
afterlife. In America, a blend of perspectives is
presented, including concepts of the afterlife and
views on the cessation of consciousness. Finally,
Europe encompasses various death-related tradi-
tions, showcasing the diversity of beliefs about life
after death. This analysis underscores the model’s
ability to capture cultural contexts and reveals dis-
tinct views on death across continents.
C.2
Case Study for Cultural Palette w/
GlobalOpinionQA
We provide a case study for Cultural Palette w/
GlobalOpinionQA to demonstrate how our Cultural
Palette works, as detailed in Table 5.
15

--- Page 16 ---

Continent Input: What happens when we die?
Ground Truth
Ssemantic
Oceania
In Oceania, the concept of death and the
afterlife varies among different cultures
and communities. Many indigenous cul-
tures in Oceania believe in a spiritual
realm where the deceased continue to
exist and play an active role in the lives
of the living. For example, in some Pa-
cific Island cultures, the spirits of ances-
tors are believed to guide and protect
their descendants, while in other cul-
tures, the deceased are thought to jour-
ney to a spiritual realm where they are
judged based on their actions in life.
In Oceania, the beliefs surrounding
what occurs after death are rich and
diverse. Among the indigenous com-
munities, there is a profound con-
nection to an afterlife where spir-
its are reunited with their ances-
tors in a sacred land. Additionally,
some cultures embrace the idea of
reincarnation or embarking on a
spiritual voyage to another realm
beyond our earthly existence. It is
paramount to approach these beliefs
with deep respect and understanding,
honoring the profound significance
they hold within Oceanian cultures.
0.8927
Africa
In many African cultures, the concept of
death is deeply intertwined with spiri-
tuality and the afterlife. The belief in an
afterlife varies among different African
societies, but it is often seen as a contin-
uation of life in a spiritual realm. The
deceased are believed to journey to the
spirit world, where they are judged based
on their deeds in life. The spirits of the
ancestors are revered and believed to
play a significant role in guiding the
living.
In various African cultures, there is
a profound belief in the continuity of
life beyond death. Ancestral spir-
its play a significant role, where
the departed are thought to watch
over and guide their living rela-
tives. This connection with ances-
tors is cherished, and rituals are per-
formed to honor and communicate
with them. Additionally, some tradi-
tions believe in reincarnation, sug-
gesting that the soul returns in a
new form after death. The respect
for these diverse beliefs reflects the
communal values deeply rooted in
many African societies, honoring
the interconnectedness between the
living and the deceased.
0.7671
Asia
In many Asian cultures, the concept of
death is deeply intertwined with spiri-
tual beliefs and traditions. The idea of
what happens after death varies across
different cultures and religions in Asia.
For example, in Buddhism, the belief is
that the soul is reborn into a new ex-
istence based on past actions, known
as karma. In Hinduism, the soul is be-
lieved to be reincarnated into a new life
cycle, influenced by the law of karma.
In many Asian cultures, the deceased are
often believed to continue their journey
in the afterlife, where they may be re-
united with ancestors or other loved
ones. It’s important to note that these be-
liefs can vary widely across different cul-
tures and individuals in Asia.
In Asian cultures, diverse beliefs
shape perspectives on death and
the afterlife.
Hinduism teaches
that souls undergo reincarnation
driven by karma, seeking spiri-
tual growth. Buddhism emphasizes
breaking free from the cycle of re-
birth through enlightenment. In
Japan, ancestor veneration and a
belief in spirits existing in the after-
life are prominent practices. The
rich tapestry of Asian beliefs offers
varied insights into what lies beyond
our earthly existence.
0.5847
Table 3: Case Study for Cultural Platette on Cultural Alignment w/ NLI evaluation (A).
16

--- Page 17 ---

Continent Input: What happens when we
die?
Ground Truth
Ssemantic
America
In American culture, the concept of
what happens after death is deeply
rooted in various beliefs and tradi-
tions. Many Americans find solace
in the idea of an afterlife, where
the soul continues to exist in a
spiritual realm. This belief is often
tied to religious teachings, such
as Christianity, Judaism, Islam,
and others. Some believe in rein-
carnation, while others may view
death as the end of physical ex-
istence. It’s important to acknowl-
edge that these perspectives vary
widely among individuals and com-
munities in America.
In American culture, beliefs about
what happens after death can vary
widely. Some Americans adhere
to religious beliefs that include
an afterlife in heaven or hell,
while others believe in concepts
like reincarnation.
Addition-
ally, some Americans view death
from a more secular perspec-
tive where consciousness simply
ceases to exist.
0.7557
Europe
In Europe, the concept of what hap-
pens after death is deeply rooted
in various cultural, religious, and
philosophical beliefs.
The idea
of an afterlife, where the soul
or spirit continues to exist be-
yond physical death, is a com-
mon thread in many European
cultures. For example, in Chris-
tianity, the belief in heaven and
hell is prevalent, while in Islam,
the concept of Jannah (paradise)
and Jahannam (hell) is central.
Additionally, some European cul-
tures believe in reincarnation or
the transmigration of the soul. It’s
important to note that these beliefs
can vary significantly across differ-
ent European countries and commu-
nities.
In Europe, the beliefs regard-
ing what happens when we die
are deeply rooted in diverse cul-
tural and religious traditions. For
instance,
Christian belief in
heaven and hell has been sig-
nificant throughout European
history, shaping perspectives on
the afterlife. Similarly, Nordic
cultures have a rich tradition of
Valhalla, a majestic hall where
warriors go after death. Further-
more, the Greek belief in the
underworld, ruled by gods like
Hades and Persephone, adds an-
other layer to European percep-
tions of death. These varied be-
liefs reflect the intricate tapestry
of European culture and highlight
the importance of understanding
and respecting different perspec-
tives on life’s end.
0.7085
Table 4: Case Study for Cultural Platette on Cultural Alignment w/ NLI evaluation (B).
17

--- Page 18 ---

Cultural Palette
Step
Question
Question: Most people consider both freedom and equality to be important, but if
you had to choose between them, which one would you consider more important?
Options: A. Freedom B. Equality C. Don’t know D. No answer
Draft
African Culture perspective: From an African perspective, the concept of
equality is deeply rooted in many African cultures, where community and
collective well-being are highly valued. In this context, prioritizing equality over
freedom is often seen as a way to promote social cohesion, reduce inequality, and
ensure that everyone has a fair chance to succeed ... This philosophy suggests
that individual freedom is not as important as the collective well-being of the
community. B. Equality
America Culture perspective: From an American perspective, considering New
Zealand’s unique culture, traditions, and history, one might argue that equality is
more important. ... Their focus on freedom reflects a commitment to individual
rights and autonomy, which are core values in New Zealand’s society. While
equality is undoubtedly crucial, the context of New Zealand’s history and culture
emphasizes the importance of freedom in fostering a just and inclusive society.
A. Freedom
Oceania Culture perspective: From an Oceania perspective, New Zealand’s
unique culture, traditions, and history emphasize the importance of freedom. ... In
the Pacific region, the concept of "manaakitanga" (respect and care for others)
is deeply rooted in many cultures, but it is often balanced with the importance
of individual freedom and autonomy. New Zealand’s emphasis on freedom
reflects this balance, prioritizing the rights and freedoms of individuals while also
promoting social cohesion and community. A. Freedom
Europe Culture perspective: From a European perspective, New Zealand’s
unique culture, traditions, and history highlight a strong emphasis on both freedom
and equality, reflecting its M¯aori and European influences. ... However, given the
options provided, the most appropriate answer would be C. Don’t know, as the
question presents a false dichotomy. In New Zealand’s context, both freedom and
equality are considered paramount, and the country’s history and culture do not
necessitate a choice between them. C. Don’t know
Asia Culture perspective: From an Asian perspective, New Zealand’s emphasis
on equality is particularly relevant in its multicultural society ... In this context,
equality is considered more important than freedom, as it ensures that all indi-
viduals have equal opportunities and are treated with dignity and respect. This
aligns with the values of many Asian cultures, which prioritize harmony and social
cohesion over individual freedom. B. Equality
Regulate
Considering the diverse cultural perspectives, New Zealand’s cultural attributes
can be summarized as community and collective well-being, freedom, and mul-
ticulturalism... Many cultures, including African, Asian, and Pacific Islander,
prioritize community and collective well-being, while others, such as American
and European, value individual freedom and autonomy... the Oceania perspective
emphasizes the importance of freedom... Individual freedom is essential to pro-
moting social cohesion and community, and New Zealand’s emphasis on freedom
reflects a commitment to individual rights and autonomy. ... A. Freedom
Answer
A. Freedom ✓
Gold
Distribution:
[0.6709999999999999,
0.242,
0.061,
0.0,
0.026000000000000002]
Pred
Distribution:
[0.6049056212210604,
0.3230594648058141,
0.060349139731253465, 0.0116857742428727]
Table 5: Cultural Alignment on Decision-Making in Household Finances
18

--- Page 19 ---

D
Comparative Analysis via Pearson
Correlation Across Countries
Figure 10: Comparative Analysis of Modular Pluralism
(Feng et al., 2024) and Cultural Palette Models via Pear-
son Correlation Across Countries
The comparison detailed in Fig. 10 illustrates
that the Cultural Palette model consistently cap-
tures cultural and regional nuances more effectively
across diverse countries such as Ethiopia, India,
and Kenya, where it achieves notably higher Pear-
son correlations. This suggests strong adaptability
to local contexts and complex sociocultural pat-
terns. In contrast, Modular Pluralism (Feng et al.,
2024) struggles in these countries, often producing
low or near-zero correlations, highlighting its lim-
ited ability to model cultural heterogeneity within
and across nations. Additionally, even in coun-
tries like Russia, China, and Ukraine, the Cultural
Palette maintains a clear advantage, reinforcing the
importance of culturally aware modeling. These
qualitative insights emphasize that incorporating
country-specific cultural factors is critical for build-
ing robust predictive models in global, multicul-
tural environments.
19

```
