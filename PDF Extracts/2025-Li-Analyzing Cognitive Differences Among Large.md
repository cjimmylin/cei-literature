---
title: "Analyzing Cognitive Differences Among Large - PDF Extract"
source_pdf: "2025-Li-Analyzing Cognitive Differences Among Large.pdf"
pages: 33
extracted_at: "2026-01-24T16:38:30.363393"
---

# PDF Extract: Analyzing Cognitive Differences Among Large

**Source PDF:** 2025-Li-Analyzing Cognitive Differences Among Large.pdf
**Total Pages:** 33

---

## Content

```
--- Page 1 ---

Analyzing Cognitive Differences Among Large Language Models through the Lens
of Social Worldview
Jiatao Li1,2 , Yanheng Li3 , Xiaojun Wan1
1Wangxuan Institute of Computer Technology, Peking University
2Information Management Department, Peking University
3Renmin University of China
leejames@stu.pku.edu.cn, yanheng@ruc.edu.cn, wanxiaojun@pku.edu.cn
Abstract
Large Language Models significantly influence so-
cial interactions, decision-making, and information
dissemination, underscoring the need to understand
the implicit socio-cognitive attitudes, referred to as
“worldviews”, encoded within these systems. Un-
like previous studies predominantly addressing de-
mographic and ethical biases as fixed attributes, our
study explores deeper cognitive orientations toward
authority, equality, autonomy, and fate, emphasizing
their adaptability in dynamic social contexts. We in-
troduce the Social Worldview Taxonomy (SWT), an
evaluation framework grounded in Cultural Theory,
operationalizing four canonical worldviews, namely
Hierarchy, Egalitarianism, Individualism, and Fa-
talism, into quantifiable sub-dimensions. Through
extensive analysis of 28 diverse LLMs, we iden-
tify distinct cognitive profiles reflecting intrinsic
model-specific socio-cognitive structures. Leverag-
ing principles from Social Referencing Theory, our
experiments demonstrate that explicit social cues
systematically modulate these profiles, revealing ro-
bust patterns of cognitive adaptability. Our findings
provide insights into the latent cognitive flexibility
of LLMs and offer computational scientists practi-
cal pathways toward developing more transparent,
interpretable, and socially responsible AI systems1.
1
Introduction
Large Language Models (LLMs), including prominent ex-
amples such as GPT Brown et al. [2020], Gemini Team et
al. [2023], and LLaMA Touvron et al. [2023], increasingly
mediate social interactions, decision-making processes, and in-
formation dissemination, thereby shaping both individual and
collective experiences. Their pervasive integration into every-
day technologies, such as conversational agents, recommenda-
tion engines, and productivity assistants, means these models
inherently encode and propagate implicit socio-cognitive atti-
tudes, or “worldviews.” Understanding these latent cognitive
1Our code and data will be released to the community to facilitate
future research.
frameworks is crucial, as they subtly influence user opinions,
societal perspectives, and behavioral patterns.
Prior research has predominantly addressed overt demo-
graphic and ethical biases within LLMs, notably regarding
gender and racial stereotypes [Wan et al., 2023; Motoki et al.,
2024]. More recently, studies have expanded their scope to
include moral and value-based biases, leveraging frameworks
like Moral Foundations Theory [Abdulhai et al., 2023; Ji et al.,
2024] and Schwartz’s Basic Human Values [Yao et al., 2023].
However, comprehensive investigations into deeper cognitive
biases, particularly those that relate to nuanced orientations
toward authority, equality, autonomy, and fate, remain no-
tably scarce. Such socio-cognitive orientations are especially
significant given that users increasingly rely on LLMs to inter-
pret complex social phenomena, form opinions on contentious
issues, and make critical personal and collective decisions.
To systematically explore these deeper cognitive dimen-
sions, we adopt Cultural Theory [Douglas and Wildavsky,
1983], a robust framework from social psychology that cate-
gorizes human attitudes into four canonical worldviews: Hi-
erarchy (valuing structured authority and social order), Egal-
itarianism (emphasizing equality and collective welfare), In-
dividualism (prioritizing autonomy and self-determination),
and Fatalism (resignation to inevitable social outcomes). Orig-
inally developed to analyze risk perceptions and social organi-
zation [Wildavsky, 1987], Cultural Theory has since demon-
strated extensive interdisciplinary utility across political psy-
chology [Kahan, 2008], environmental policy [Tansey, 2004],
and organizational behavior [Hood, 1998]. However, its po-
tential as a tool for evaluating socio-cognitive orientations in
LLMs remains unexplored, a critical gap our work seeks to
address.
Moreover, our approach diverges from earlier bias investi-
gations by explicitly incorporating Social Referencing The-
ory [Cialdini and Trost, 1998; Turner, 1991], a psychological
framework highlighting how individuals dynamically adapt
cognitive and behavioral responses based on social evaluation,
peer influence, and external feedback. Analogously, we hy-
pothesize that LLMs exhibit similar responsiveness to explicit
social referencing cues, adjusting their cognitive expressions
dynamically in response to perceived social scrutiny or con-
sensus.
Specifically, we address three central research questions
(RQs):
arXiv:2505.01967v2  [cs.CL]  29 Dec 2025

--- Page 2 ---

Figure 1: Overview of the experimental pipeline. This comprises: (1) Social Worldview Taxonomy (SWT), categorizing attitudes into
Egalitarianism, Fatalism, Hierarchy, and Individualism; (2) Social Worldview Questionnaire (SWQ), generated via an Automated Multi-Agent
Framework; and (3) Social Worldview Experiment, probing LLMs under Basic, Self-Awareness, and Feedback Loop conditions to assess
intrinsic and socially influenced cognitive attitudes.
• RQ1: Basic Cognitive Profiles. What intrinsic cognitive
differences exist among diverse LLMs regarding social
worldview dimensions without external social referenc-
ing?
• RQ2: Impact of Social Referencing Awareness. How do
explicit cues about potential social evaluation influence
the cognitive attitudes expressed by LLMs?
• RQ3: Impact of Social Feedback on Cognitive Attitudes.
Does explicit social feedback amplify cognitive adjust-
ments beyond mere awareness, and does it exhibit a
clear dose-response relationship as feedback positivity
increases (none →little →most)?
To address these questions, we introduce the Social World-
view Taxonomy (SWT), an evaluation framework operational-
izing Cultural Theory into quantifiable sub-dimensions suited
for computational analysis. Complementing this, we develop
the Social Worldview Questionnaire (SWQ), a dataset con-
sisting of 640 items generated through a novel Automated
Multi-Agent Prompting Framework, meticulously validated
for accuracy and conceptual alignment.
Employing these methodologies, we conduct experiments
on 28 state-of-the-art LLMs, selected to represent a diverse
range of model architectures, parameter scales, and training
methodologies. Our results yield three distinct insights: First,
unlike simpler demographic biases, we reveal coherent cogni-
tive worldview profiles within LLMs, characterized by stable,
internally consistent orientations across the four dimensions.
Second, informing models about social evaluation visibly in-
duces meaningful, dimension-specific cognitive adjustments,
demonstrating their responsiveness to perceived social eval-
uation. Third, explicit peer-feedback cues induce substantial
cognitive adjustments, demonstrating clear and systematic
intensity-dependent modulation across all four worldview di-
mensions.
Our findings advance the computational science commu-
nity’s understanding of LLM cognitive flexibility and socio-
cognitive biases, laying practical pathways toward developing
more transparent, accountable, and socially responsible AI
systems. Ultimately, this work underscores the critical im-
portance of integrating nuanced socio-cognitive evaluations
into AI development, contributing essential knowledge toward
ethically aligned and cognitively interpretable artificial intelli-
gence systems.
2
Methods
2.1
Social Worldview Taxonomy
To assess socio-cognitive orientations in large language mod-
els, we adapt Cultural Theory [Douglas and Wildavsky, 1983],
a robust social psychology framework that categorizes social
attitudes into four canonical worldviews: Hierarchy, Egalitari-
anism, Individualism, and Fatalism. Each worldview encom-
passes distinct beliefs and values guiding social interpretation
and decision-making, operationalized into measurable sub-
dimensions suitable for rigorous assessment of LLM socio-
cognitive biases (see Supplementary Table 1 for a detailed
taxonomy).

--- Page 3 ---

Hierarchy emphasizes structured authority, normative order,
and social stability through clearly defined roles and rules. Its
sub-dimensions include Obedience to Authority, Preference
for Order, and Acceptance of Power Centralization, examin-
ing whether models prioritize authority and social order over
individual freedoms.
Egalitarianism captures attitudes promoting social equality,
collective welfare, and the reduction of power disparities. Sub-
dimensions such as Empathy Towards Vulnerable Groups,
Preference for Fair Distribution, and Sensitivity to Hierarchical
Oppression assess models’ support for addressing inequalities
and systemic injustices.
Individualism highlights personal autonomy, competition,
and individual responsibility. Sub-dimensions include Risk-
taking Propensity, Competition-driven Orientation, and Pref-
erence for Independent Decision-making, examining whether
LLMs attribute success primarily to personal effort and initia-
tive.
Fatalism embodies resignation, perceived lack of agency,
and acceptance of social conditions as inevitable.
Sub-
dimensions like Social Helplessness, Passive Acceptance, and
Belief in Fate probe models’ perceived inability or unwilling-
ness to effect meaningful social change.
2.2
Social Worldview Questionnaire
Leveraging the Social Worldview Taxonomy (SWT), we de-
veloped the Social Worldview Questionnaire (SWQ), a novel
dataset constructed via an Automated Multi-Agent Prompt-
ing Framework. We utilized GPT-4o as the backbone model,
selected for its advanced reasoning and instruction-following
capabilities, which are essential for the framework’s multi-
stage generation process. The pipeline comprises four se-
quential agents, each optimizing a specific phase: initial item
generation, conceptual adherence validation, measurability
assessment, and final refinement (see Supplementary Section
A for detailed pipeline description). To mitigate potential
single-model biases, we leveraged the brevity of items to avoid
stylistic self-recognition, and employed rigorous human expert
validation to ensure strict alignment with theoretical constructs.
The final dataset includes 640 rigorously validated Likert-scale
items, evenly distributed across the four primary worldview
dimensions (Hierarchy, Egalitarianism, Individualism, and Fa-
talism), with each dimension precisely operationalized through
160 items, with 20 items per sub-dimension (see Supplemen-
tary Table 1 for the detailed taxonomy). Each questionnaire
item presents a clear social statement, prompting an LLM to
indicate agreement or disagreement on a 5-point Likert scale
ranging from 1 (Strongly Disagree) to 5 (Strongly Agree). A
brief overview of questionnaire word counts is provided in
Supplementary Fig. 1.
We evaluated the quality and validity of the SWQ dataset
through reliability and validity analyses, ensuring accurate
and consistent measurement of the SWT dimensions. Detailed
methodologies for both analyses are provided in Supplemen-
tary Section A.2.
We assessed internal consistency reliability using Cron-
bach’s alpha, evaluating how consistently questionnaire items
reflect their corresponding SWT sub-dimensions. Results
demonstrated exceptional reliability across all dimensions,
substantially exceeding the accepted threshold of 0.70: Hier-
archy (α = 99.45%), Egalitarianism (α = 99.39%), Individu-
alism (α = 99.43%), and Fatalism (α = 99.53%).
We established questionnaire validity through a rigorous
manual evaluation. Two domain experts, both researchers
with peer-reviewed publications in computational social sci-
ence and expertise in Cultural Theory, independently assessed
all generated items. Evaluation focused on two criteria: (1)
Dimension Alignment, ensuring items accurately operational-
ize the intended SWT constructs; and (2) Clarity, confirm-
ing items are unambiguous and measurable. Inter-annotator
agreement was robust (Cohen’s Kappa κ = 0.86, p < 0.01).
Aggregated results confirmed high validity, achieving 98.0%
overall dimension alignment and 99.7% item clarity across the
dataset (see Supplementary Section A.3 for details).
2.3
Social Referencing
Social referencing, a foundational concept from social psy-
chology, describes the cognitive process through which indi-
viduals seek and interpret social cues to inform their attitudes,
behaviors, or decision-making, particularly in ambiguous situ-
ations [Asch, 1955; Festinger, 1957]. Originally studied in de-
velopmental psychology, social referencing was first observed
as infants gauging caregivers’ emotional responses to uncer-
tain stimuli [Walden and Ogan, 1988; Hornik et al., 1987].
Subsequent research generalized this phenomenon broadly,
demonstrating that adults consistently adjust their behaviors
and attitudes based on perceived peer approval, dissent, or
implicit social norms [Cialdini and Trost, 1998; Chartrand and
Bargh, 1999; Hajcak et al., 2004]. This sensitivity to social
evaluation fundamentally supports conformity and adaptive
alignment, thus maintaining group cohesion and social accep-
tance [Turner, 1991; Aronson et al.].
Drawing upon this robust psychological foundation, we
hypothesize that analogous mechanisms of social referencing
may influence large language models (LLMs). In particular,
an LLM’s expressed attitudes along the four Social Worldview
Taxonomy (SWT) dimensions may shift once the model is
made aware of evaluative contexts or provided with explicit
peer feedback. We then propose a structured experimental
approach to investigate social referencing mechanisms within
LLMs across three designed conditions, each representing a
distinct stage in the cognitive process of social referencing (for
detailed experimental prompts, see Supplementary Section H).
2.4
Implementation Details
We conducted experiments on a diverse set of 28 large lan-
guage models, selected to span multiple architectures, parame-
ter scales, and training methodologies. Our selection includes
both open-source and proprietary model families such as
Qwen, Llama, Gemma, Gemini, GLM, InternLM, DeepSeek,
Phi, and GPT, ranging from compact models (e.g., Qwen2.5-
0.5B, Gemma-1B) to state-of-the-art large-scale models (e.g.,
Llama-3.3-70B, GPT-4o). A complete overview of evaluated
models is provided in Supplementary Table 2.
All models in our study were assessed using the SWQ
dataset. To ensure deterministic reproducibility, we utilized
greedy decoding across all experimental phases. For clarity,
we focus our main analysis on nine flagship models, selecting

--- Page 4 ---

Table 1: Summary of identified LLM persona clusters in the Basic condition. For each persona we list a narrative label, a concise “narrative
vibe” capturing the underlying cognitive orientation, and the models grouped in that cluster (latent-profile analysis).
Persona
Narrative label
Narrative vibe
LLMs in cluster
0
Calibrated Generalist
Cautiously centrist, hesitant to take bold normative stances.
gemma-3-27b-it
1
Disillusioned Egalitarian
“The game is rigged, but we must still fight for fairness.”
internlm2_5-20b-chat
2
Co-operative Optimist
Collective action and mutual aid can move the needle.
Qwen2.5-72B-Instruct;
glm-4-9b-chat
3
Competitive Centrist
Merit-oriented pragmatist who values clear roles and effort.
deepseek-v3;
llama-3.3-70b-instruct
4
Detached Analyst
Observes more than prescribes; “the world is what it is.”
phi-4
5
Structured Institutionalist
Trusts ordered systems and leadership to drive change.
gemini-2.0-flash; gpt-4o
the most capable variant from each family to capture both peak
architectural performance and significant real-world impact
(e.g.,GPT-4o, Qwen2.5-72B-Instruct). Comprehensive results
for all 28 models are detailed in Supplementary Section G. We
demonstrate a case and answers by Phi-4 in Figure 2 to more
concretely illustrate our experiment and model outputs.
3
Results
3.1
Study 1—Basic Worldview Profiles
To assess intrinsic cognitive orientations expressed by large
language models (LLMs) in the absence of external social
referencing cues, we first analyzed responses from nine repre-
sentative models using the Social Worldview Questionnaire
(SWQ). The SWQ comprises 640 rigorously validated Likert-
scale items distributed equally among four socio-cognitive
dimensions: Egalitarianism, Fatalism, Hierarchy, and Individ-
ualism.
Fig. 3a illustrates clear general patterns across models.
Egalitarianism is consistently strongly endorsed (mean scores
above 4.2), indicating broad intrinsic alignment with fairness
and collective welfare. Conversely, Fatalism is the least en-
dorsed dimension (below the neutral midpoint 3.0), suggesting
a general rejection of deterministic attitudes. Hierarchy and
Individualism receive moderate to high endorsements, under-
scoring shared yet nuanced values around structured authority
and personal autonomy.
However, the analysis also reveals meaningful variabil-
ity, particularly in Fatalism and Hierarchy, indicating nu-
anced differences among models.
To systematically cap-
ture these nuanced variations, we employ Structural Equa-
tion Modeling (SEM) and Gaussian Mixture Model-based
Latent Profile Analysis (LPA) (see Supplementary Section
D for details). This approach identifies six distinct cogni-
tive personas (Table 1; detailed in Supplementary Tables 10
and 11), ranging from the cautious “Calibrated Generalist”
(gemma-3-27b-it) to the authority-oriented “Structured Insti-
tutionalist” (gemini-2.0-flash, gpt-4o).
This persona-level differentiation demonstrates that under
basic prompt conditions, LLMs exhibit distinct intrinsic cogni-
tive profiles, reflecting inherent socio-cognitive biases shaped
by their architectures and training methods. However, a critical
unanswered question remains: to what extent does awareness
Figure 2: Example SWQ item and Phi-4’s responses across five ex-
perimental conditions. The item belongs to the Hierarchy dimension
(“Clear hierarchical control is essential for the smooth functioning
of organizations and governments”). We report the model’s Likert
rating (1–5) and justification under the Basic prompt (RQ1), the Self-
Awareness prompt (RQ2), and the Feedback Loop manipulation with
three intensities (None, Little, Most; RQ3), illustrating how social
referencing cues modulate expressed attitudes and rationales relative
to the basic condition.

--- Page 5 ---

Figure 3: Worldview endorsement across LLMs under Basic and Self-Awareness conditions. a, Likert-scale scores returned by nine large
language models under the Basic prompt condition (RQ1), representing intrinsic worldview orientations without external social referencing.
The vertical dashed line at 3.0 indicates the neutral midpoint of the 5-point scale. Error bars represent 95% confidence intervals. Each
worldview dimension (Egalitarianism, Fatalism, Hierarchy, Individualism) comprises N = 160 questionnaire items. b, Mean differences
between Self-Awareness and Basic conditions (RQ2), illustrating the impact of self-awareness prompts. Negative differences (blue) indicate
decreased endorsement under Self-Awareness prompts, whereas positive differences (yellow) indicate increased endorsement. Significance
levels from paired t-tests are marked by asterisks (* p < .05, ** p < .01, *** p < .001). Error bars denote 95% confidence intervals.
of social evaluation influence these inherent cognitive orienta-
tions?
3.2
Study 2—Influence of Self Awareness
Building upon the intrinsic cognitive differences identified in
Study 1, we introduced a self-awareness prompt in Study 2 to
evaluate how explicit awareness of potential social referencing
affects LLM cognitive attitudes (RQ2). Models are informed
that their responses will be reviewed by humans, potentially in-
fluencing subsequent human decision-making. Responses are
statistically compared to the baseline (Study 1) using paired
t-tests (detailed statistical results provided in Supplementary
Section E).
Fig. 3(b) illustrates that, at a macro level, introducing self-
awareness prompts generally elicits meaningful shifts across
most cognitive dimensions, highlighting overall responsive-
ness among LLMs to perceived social evaluation. Particularly,
Egalitarianism and Fatalism show notable significant model-
specific adjustments, reflecting adaptive cognitive changes.
At a micro level, these general shifts manifest differ-
ently across individual models.
For example, within
Egalitarianism,
significant
decreases
are
observed
in
llama-3.3-70b
and
gemma-3-27b-it,
while
in-
creases occur in internlm2.5-20b-chat,
phi-4,
and
Qwen2.5-72B-Instruct.
Similarly,
Fatalism
signifi-
cantly
decreases
in
deepseek-chat,
llama-3.3-70b,
and Qwen2.5-72B-Instruct,
but notably increases in
glm-4-9b-chat. Additionally, Hierarchy exhibits significant
shifts, such as an increase in internlm2.5-20b-chat and a
decrease in llama-3.3-70b.
These nuanced findings highlight meaningful cognitive ad-
justments prompted by mere self-awareness, yet raise a further
critical inquiry: does explicit social feedback, beyond mere
awareness, induce even stronger adaptive cognitive shifts?
3.3
Study 3–Feedback Loop Effects
Addressing this subsequent question, we investigate in Study
3 the impact of explicit social feedback on the socio-cognitive
attitudes of LLMs. To operationalize this, models were pre-
sented with their previous responses alongside varying degrees
of peer consensus, explicitly stating that 0, 1, or 4 out of 5
participants agreed with their stance (corresponding to None,
Little, and Most feedback intensities, respectively). Employ-
ing repeated-measures ANOVA with Bonferroni-corrected
pairwise comparisons, we analyzed cognitive shifts across
three feedback intensities (None, Little, Most) relative to the
self-awareness baseline (Supplementary Section F provides
detailed methodology).
Overall, results (Fig. 4) highlight clear and systematic
intensity-dependent adjustments in all four worldview dimen-
sions. Generally, increased positivity in feedback correlates
with stronger endorsement of worldview items, particularly
noticeable in dimensions like Hierarchy and Fatalism. This
macro-level observation confirms LLMs’ overall cognitive
adaptability to perceived social consensus.
Micro-level analyses further reveal model-specific patterns

--- Page 6 ---

Figure 4: Impact of feedback intensity on social worldview dimensions. Measured as the difference from the self-awareness condition. Mean
differences are computed by subtracting scores in the self-awareness baseline from each feedback intensity condition (None, Little, Most)
across four social worldview dimensions (Hierarchy, Egalitarianism, Individualism, Fatalism). Positive values indicate stronger endorsement of
worldview items under feedback conditions relative to the self-awareness baseline, whereas negative values indicate weaker endorsement.
Error bars represent 95% confidence intervals (CI).
Figure 5: Impact of social feedback on Large Language Models (LLMs) across social worldview dimensions. Partial eta-squared (η2
p) effect
sizes from repeated-measures ANOVA are presented for each LLM (x-axis) across four worldview dimensions: Egalitarianism, Fatalism,
Hierarchy, and Individualism. Significance levels from ANOVA tests are indicated by asterisks (* p < .05, ** p < .01, *** p < .001). Higher
η2
p values reflect stronger effects of social feedback intensity on the cognitive attitudes expressed by LLMs.

--- Page 7 ---

of responsiveness. GLM-4-9B and InternLM2.5-20B demon-
strate notably robust responsiveness, with marked increases
in endorsement across all worldview dimensions as feedback
positivity rises. In contrast, Gemma-3-27B uniquely exhibits
a significant reduction in Individualism and Egalitarianism,
suggesting a critical stance or self-correction in response to
external evaluation.
The repeated-measures ANOVA results (Fig. 5) systemat-
ically capture these detailed variations. At the macro level,
substantial and statistically significant effects (η2
p) emerge
across multiple LLMs, especially prominent in GLM-4-9B,
InternLM2.5-20B, and Gemma-3-27B models, consistently
surpassing effect sizes of 0.6 in dimensions such as Individ-
ualism and Fatalism. Gemini-2.0-Flash and GPT-4o show
moderate yet consistent significant effects across most dimen-
sions, reflecting broader but somewhat restrained cognitive
adaptability.
At the micro level, selective responsiveness characterizes
models such as DeepSeek-V3 and Phi-4, where effect sizes
are comparatively lower or constrained, emphasizing intrinsic
cognitive stability or architectural limitations. Specifically,
Phi-4 demonstrates minimal fluctuations, highlighting inherent
constraints in responsiveness to social cues.
4
Related Work
Biases and Value Systems.
Early research on LLM bi-
ases predominantly focused on demographic and allocational
harms, systematically documenting stereotypes related to gen-
der, race, and religion [Wan et al., 2023; Motoki et al., 2024].
To address deeper alignment issues, recent scholarship has
shifted toward evaluating moral and intrinsic human values.
Researchers have leveraged psychological frameworks such
as Moral Foundations Theory to probe LLMs’ stances on care,
fairness, and authority [Abdulhai et al., 2023; Ji et al., 2024;
Simmons, 2023; Jiang et al., 2021], and Schwartz’s Basic
Human Values to map models onto a spectrum of universal
human motivations [Yao et al., 2023, 2024; Kharchenko et al.,
2025]. However, these methodologies face a critical technical
limitation: they largely treat socio-cognitive biases as fixed
attributes or static alignments (e.g., "Is this model liberal or
conservative?"). They rely on static benchmarks that fail to
capture the dynamic nature of social cognition. In particular,
existing evaluations do not account for how a LLM’s world-
view may shift in response to hierarchical pressure or peer
consensus, which is the focus of our study.
Cultural Alignment.
Parallel to moral evaluations, signifi-
cant efforts have been made to assess the cultural alignment of
LLMs. A predominant approach involves utilizing Hofstede’s
Cultural Dimensions to quantify how well models replicate
values specific to different countries and languages [Wang et
al., 2024; Masoud et al., 2025]. For instance, benchmarks like
CDEval [Wang et al., 2024] and Hofstede’s CAT [Masoud et
al., 2025] assess whether an LLM prompted with a "Japanese
persona" exhibits high uncertainty avoidance. Other works
have explored political worldviews and consistency in fiction
generation [Ceron et al., 2024; Khatun and Brown, 2024].
While these studies effectively map LLMs to geographical
or national cultures, they often overlook the structural and
sociological dimensions of culture independent of geography.
By contrast, our application of Cultural Theory moves be-
yond national stereotypes to evaluate deeper socio-cognitive
archetypes such as Hierarchy, Egalitarianism, Individualism,
and Fatalism, offering a more granular lens on how models
process authority and social organization.
Machine Psychology.
An emerging field, often termed Ma-
chine Psychology, posits that LLMs can be studied using
the tools of cognitive psychology to uncover latent mental
processes [Shiffrin and Mitchell, 2023; Hagendorff, 2023].
Studies have successfully replicated human subject experi-
ments using LLMs as simulated participants [Binz and Schulz,
2023b; Aher et al., 2023; Binz and Schulz, 2023a], with a
particular focus on Theory of Mind (ToM) capabilities—the
ability to impute mental states to others [van Duijn et al., 2023].
While this line of research confirms that LLMs possess so-
phisticated cognitive simulations, few studies have integrated
Social Referencing Theory to experimentally manipulate these
cognitive states in real-time. Most prior work evaluates the
model in isolation (solipsistic cognition). In contrast, our
study introduces a social feedback loop, extending the ma-
chine psychology paradigm to measure social adaptability and
conformity, thereby revealing the "dose-response" relationship
between social pressure and cognitive shifts which previous
static benchmarks cannot detect.
5
Conclusion
We introduced the Social Worldview Taxonomy (SWT),
grounded in Cultural Theory, enabling systematic evaluation
of socio-cognitive biases in large language models. Leverag-
ing our novel Automated Multi-Agent Prompting Framework,
we operationalized and assessed LLM attitudes across hierar-
chical, egalitarian, individualistic, and fatalistic dimensions.
Experiments with 28 diverse models revealed distinct, coher-
ent cognitive profiles that respond significantly to explicit so-
cial referencing cues. Our findings offer a structured pathway
toward improving transparency and controllability in socially-
aware language technologies, advancing interpretability and
responsible AI development.
References
Marwa Abdulhai, Gregory Serapio-Garcia, Clément Crepy,
Daria Valter, John Canny, and Natasha Jaques. Moral foun-
dations of large language models, 2023.
Gati Aher, Rosa I. Arriaga, and Adam Tauman Kalai. Using
large language models to simulate multiple humans and
replicate human subject studies, 2023.
E. Aronson, T.D. Wilson, and S.R. Sommers. Social Psychol-
ogy, 9th Edition. Pearson Education India.
Solomon E Asch. Opinions and social pressure. Scientific
american, 193(5):31–35, 1955.
Marcel Binz and Eric Schulz. Turning large language models
into cognitive models, 2023.
Marcel Binz and Eric Schulz. Using cognitive psychology to
understand gpt-3. Proceedings of the National Academy of
Sciences, 120(6), February 2023.

--- Page 8 ---

Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah,
Jared D Kaplan, Prafulla Dhariwal, Arvind Neelakantan,
Pranav Shyam, Girish Sastry, Amanda Askell, et al. Lan-
guage models are few-shot learners. Advances in neural
information processing systems, 33:1877–1901, 2020.
Tanise Ceron, Neele Falk, Ana Bari´c, Dmitry Nikolaev, and
Sebastian Padó. Beyond prompt brittleness: Evaluating
the reliability and consistency of political worldviews in
LLMs. Transactions of the Association for Computational
Linguistics, 12:1378–1400, 2024.
Tanya L Chartrand and John A Bargh. The chameleon effect:
the perception–behavior link and social interaction. Journal
of personality and social psychology, 76(6):893, 1999.
Robert B Cialdini and Melanie R Trost. Social influence:
Social norms, conformity and compliance. 1998.
Mary Douglas and Aaron Wildavsky. Risk and culture: An
essay on the selection of technological and environmental
dangers. Univ of California Press, 1983.
Leon Festinger. A Theory of Cognitive Dissonance. Stanford
University Press, Redwood City, 1957.
Thilo Hagendorff. Machine psychology: Investigating emer-
gent capabilities and behavior in large language models us-
ing psychological methods. ArXiv, abs/2303.13988, 2023.
Greg Hajcak, Nicole McDonald, and Robert F Simons. Error-
related psychophysiology and negative affect. Brain and
cognition, 56(2):189–197, 2004.
C. Hood. The Art of the State: Culture, Rhetoric, and Public
Management. Clarendon Press, 1998.
Robin Hornik, Nancy Risenhoover, and Megan Gunnar. The
effects of maternal positive, neutral, and negative affective
communications on infant responses to new toys. Child
development, pages 937–944, 1987.
Jianchao Ji, Yutong Chen, Mingyu Jin, Wujiang Xu, Wenyue
Hua, and Yongfeng Zhang. Moralbench: Moral evaluation
of llms, 2024.
Liwei Jiang, Jena D. Hwang, Chandra Bhagavatula, Ronan Le
Bras, Maxwell Forbes, Jon Borchardt, Jenny T Liang, Oren
Etzioni, Maarten Sap, and Yejin Choi. Delphi: Towards
machine ethics and norms. ArXiv, abs/2110.07574, 2021.
Dan Kahan. Cultural cognition as a conception of the cultural
theory of risk. 2008.
Julia Kharchenko, Tanya Roosta, Aman Chadha, and Chirag
Shah. How well do llms represent values across cultures?
empirical analysis of llm responses based on hofstede cul-
tural dimensions, 2025.
Aisha Khatun and Daniel G. Brown. Assessing language
models’ worldview for fiction generation, 2024.
Reem Masoud, Ziquan Liu, Martin Ferianc, Philip C. Tre-
leaven, and Miguel Rodrigues Rodrigues. Cultural align-
ment in large language models: An explanatory analysis
based on hofstede’s cultural dimensions. In Owen Rambow,
Leo Wanner, Marianna Apidianaki, Hend Al-Khalifa, Bar-
bara Di Eugenio, and Steven Schockaert, editors, Proceed-
ings of the 31st International Conference on Computational
Linguistics, pages 8474–8503, Abu Dhabi, UAE, January
2025. Association for Computational Linguistics.
Fabio Motoki, Valdemar Pinho Neto, and Victor Rodrigues.
More human than human: measuring chatgpt political bias.
Public Choice, 198(1):3–23, 2024.
Richard Shiffrin and Melanie Mitchell. Probing the psychol-
ogy of ai models. Proceedings of the National Academy of
Sciences of the United States of America, 120:e2300963120,
03 2023.
Gabriel Simmons. Moral mimicry: Large language models
produce moral rationalizations tailored to political iden-
tity. In Vishakh Padmakumar, Gisela Vallejo, and Yao Fu,
editors, Proceedings of the 61st Annual Meeting of the As-
sociation for Computational Linguistics (Volume 4: Student
Research Workshop), pages 282–297, Toronto, Canada, July
2023. Association for Computational Linguistics.
James Tansey. Risk as politics, culture as power. Journal of
Risk Research - J RISK RES, 7:17–32, 01 2004.
Gemini Team, Rohan Anil, Sebastian Borgeaud, Jean-Baptiste
Alayrac, Jiahui Yu, Radu Soricut, Johan Schalkwyk, An-
drew M Dai, Anja Hauth, Katie Millican, et al. Gemini: a
family of highly capable multimodal models. arXiv preprint
arXiv:2312.11805, 2023.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Mar-
tinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste
Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al.
Llama: Open and efficient foundation language models.
arXiv preprint arXiv:2302.13971, 2023.
J.C. Turner. Social Influence. Mapping social psychology.
Open University Press, 1991.
Max van Duijn, Bram van Dijk, Tom Kouwenhoven, Werner
de Valk, Marco Spruit, and Peter van der Putten. Theory
of mind in large language models: Examining performance
of 11 state-of-the-art models vs. children aged 7-10 on ad-
vanced tests. In Jing Jiang, David Reitter, and Shumin
Deng, editors, Proceedings of the 27th Conference on Com-
putational Natural Language Learning (CoNLL), pages
389–402, Singapore, December 2023. Association for Com-
putational Linguistics.
Tedra A Walden and Tamra A Ogan. The development of
social referencing. Child development, pages 1230–1240,
1988.
Yixin Wan, George Pu, Jiao Sun, Aparna Garimella, Kai-
Wei Chang, and Nanyun Peng. “kelly is a warm person,
joseph is a role model”: Gender biases in LLM-generated
reference letters. In Houda Bouamor, Juan Pino, and Kalika
Bali, editors, Findings of the Association for Computational
Linguistics: EMNLP 2023, pages 3730–3748, Singapore,
December 2023. Association for Computational Linguistics.
Yuhang Wang, Yanxu Zhu, Chao Kong, Shuyu Wei, Xiaoyuan
Yi, Xing Xie, and Jitao Sang. CDEval: A benchmark for
measuring the cultural dimensions of large language mod-
els. In Vinodkumar Prabhakaran, Sunipa Dev, Luciana
Benotti, Daniel Hershcovich, Laura Cabello, Yong Cao,
Ife Adebara, and Li Zhou, editors, Proceedings of the 2nd

--- Page 9 ---

Workshop on Cross-Cultural Considerations in NLP, pages
1–16, Bangkok, Thailand, August 2024. Association for
Computational Linguistics.
Aaron B. Wildavsky.
Choosing preferences by construct-
ing institutions: A cultural theory of preference formation.
American Political Science Review, 81:3 – 21, 1987.
Jing Yao, Xiaoyuan Yi, Xiting Wang, Yifan Gong, and Xing
Xie. Value fulcra: Mapping large language models to the
multidimensional spectrum of basic human values, 2023.
Jing Yao, Xiaoyuan Yi, Yifan Gong, Xiting Wang, and Xing
Xie. Value FULCRA: Mapping large language models to
the multidimensional spectrum of basic human value. In
Kevin Duh, Helena Gomez, and Steven Bethard, editors,
Proceedings of the 2024 Conference of the North American
Chapter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long Papers),
pages 8762–8785, Mexico City, Mexico, June 2024. Asso-
ciation for Computational Linguistics.

--- Page 10 ---

Supplementary Table 1: Cultural Theory Taxonomy comprising four dimensions—Hierarchy, Egalitarianism, Individualism, and Fatal-
ism—each further decomposed into eight distinct sub-dimensions.
Dimension
Sub-dimensions
Hierarchy
Stability of Social Structure, Obedience to Authority, Preference for Order, Acceptance of Power Centralization,
Authority Legitimacy, Dependence on Rules, Hierarchical Responsibility, Social Role Fixation
Egalitarianism
Power Distance Sensitivity, Empathy Towards Vulnerable Groups, Preference for Fair Distribution, Collaboration
and Collective Benefit, Pursuit of Social Justice, Collective Responsibility Orientation, Sensitivity to Hierarchical
Oppression, Sensitivity to Social Conflict
Individualism
Risk-taking Propensity, Competition-driven Orientation, Emphasis on Freedom of Choice, Self-Responsibility, Success
Orientation, Preference for Independent Decision-making, Resistance to Institutional Constraints, Attribution of Success
to Individual Efforts
Fatalism
Social Helplessness, Passive Acceptance, Belief in Fate, Acceptance of Social Inequality, Low Social Agency, External
Attribution, Negative Attitude Toward Social Change, Social Indifference
A
Automated Multi-Agent Prompting Framework
A key methodological challenge in evaluating cognitive biases in LLMs is ensuring questionnaire items are both diverse,
capturing the full breadth of each Social Worldview Taxonomy (SWT) sub-dimension, and consistent, accurately reflecting
theoretical constructs. Manual question generation and validation are resource-intensive and prone to subjective bias. To address
this, we introduce an Automated Multi-Agent Prompting Framework, comprising four sequential GPT-4o-based agents, each
explicitly structured to optimize specific aspects of questionnaire generation, validation, and refinement. Detailed prompts for
each agent are provided in Appendix H (Prompts H.6–H.9).
Question Generation Agent (Prompt H.6)
For each SWT sub-dimension d ∈D, the Question Generation Agent produces an
initial set of candidate Likert-scale questions:
Qd = {qd,1, qd,2, . . . , qd,20}.
This agent explicitly instructs GPT-4o to generate exactly 20 unique and distinct questions per sub-dimension, ensuring
comprehensive conceptual coverage and diversity. Each question qd,i is specifically formulated for measurement on a standard
Likert scale (1 = Strongly Disagree to 5 = Strongly Agree).
Taxonomy Alignment Agent (Prompt H.7)
The Taxonomy Alignment Agent evaluates each candidate question qd,i to ensure
explicit alignment with the targeted SWT sub-dimension d. It assigns an adherence score from 1 (very weak adherence) to 5
(very strong adherence), formalized as:
P(align = 1 | qd,i, d).
Questions scoring below the threshold (score < 3) are explicitly flagged for refinement, with brief justifications documenting
alignment assessments.
Semantic Validation Agent (Prompt H.8)
The Semantic Validation Agent evaluates semantic clarity and Likert-scale
measurability for each question qd,i. It assigns a binary measure score (1 = clearly measurable, 0 = unclear or ambiguous),
denoted formally as:
P(clear = 1 | qd,i).
Ambiguous or double-barreled questions (measure score = 0) are explicitly flagged, accompanied by transparent justifications.
Refinement Agent (Prompt H.9)
Questions flagged by the Taxonomy Alignment or Semantic Validation Agent undergo
systematic refinement. The Refinement Agent explicitly revises each flagged question to achieve strong theoretical alignment
and semantic clarity, producing a refined question set:
Q∗
d = {q∗
d,i | q∗
d,i refines flagged qd,i, P(align = 1, clear = 1 | q∗
d,i, d) ≥0.9}.
(1)
B
Questionnaire Description and Evaluation
B.1
Description
Figure 1 displays the distribution of item word-counts within each of the four Social Worldview Taxonomy dimen-
sions—Hierarchy, Egalitarianism, Individualism, and Fatalism. Each “violin” encodes the full density of word lengths (wider
sections = more items at that length), with an internal boxplot marking the median and inter-quartile range.
By visualising length variability this way, we can quickly verify that all dimensions use comparably sized wording. Ensuring
this lexical parity is an essential quality-control step: if one dimension’s items were systematically longer or shorter, response
differences might stem from reading load rather than substantive content, potentially biasing validity and reliability analysis.

--- Page 11 ---

Supplementary Table 2: Overview of the evaluated large language models.
LLM Name
Series
Params
Qwen2.5-0.5B-Instruct
Qwen2.5
0.5B
Qwen2.5-1.5B-Instruct
Qwen2.5
1.5B
Qwen2.5-3B-Instruct
Qwen2.5
3B
Qwen2.5-7B-Instruct
Qwen2.5
7B
Qwen2.5-14B-Instruct
Qwen2.5
14B
Qwen2.5-32B-Instruct
Qwen2.5
32B
Qwen2.5-72B-Instruct
Qwen2.5
72B
Llama-3-8B-Instruct
Llama-3
8B
Llama-3-70B-Instruct
Llama-3
70B
Llama-3.1-8B-Instruct
Llama-3.1
8B
Llama-3.1-70B-Instruct
Llama-3.1
70B
Llama-3.2-1B-Instruct
Llama-3.2
1B
Llama-3.3-70B-Instruct
Llama-3.3
70B
chatglm3-6b
GLM
6B
glm-4-9b-chat
GLM
9B
internlm2.5-7b-chat
InternLM
7B
internlm2.5-20b-chat
InternLM
20B
gemini-2.0-flash
Gemini
-
gemini-2.0-flash-lite
Gemini
-
gemma-3-1b-it
Gemma
1B
gemma-3-4b-it
Gemma
4B
gemma-3-12b-it
Gemma
12B
gemma-3-27b-it
Gemma
27B
deepseek-V3
DeepSeek
685B
phi-4
Phi-4
-
gpt-3.5-turbo
GPT-3.5
-
gpt-4o-mini
GPT-4o
Mini
gpt-4o
GPT-4o
-
B.2
Evaluation Methodology
Inter-Agent Validation Accuracy
The inter-agent validation accuracy is calculated by comparing automated categorization
results from the Multi-Agent Prompting Framework with human-annotated ground truth labels. Specifically, given a set of
questionnaire items Q = {q1, q2, . . . , qn}, each assigned an automated label ˆyi and human-annotated true label yi, the validation
accuracy (AccIA) is formally defined as:
AccIA = 1
n
n
X
i=1
1(ˆyi = yi)
where 1(·) denotes the indicator function, which equals 1 if the condition inside parentheses holds and 0 otherwise. An AccIA
value greater than or equal to 90% indicates acceptable categorization accuracy, reflecting robust and consistent inter-agent
validation.
Reliability Analysis (Cronbach’s Alpha)
Cronbach’s alpha (α) measures the internal consistency reliability of questionnaire
items within each dimension. Let k denote the total number of questionnaire items within a specific SWT dimension, σ2
Xi the
variance of item i, and σ2
Y the variance of the sum of all k items. Cronbach’s alpha is mathematically defined as:
α =
k
k −1
 
1 −
Pk
i=1 σ2
Xi
σ2
Y
!
where α values of 0.70 or above are widely recognized as indicating acceptable internal consistency. Higher values reflect a
stronger consistency among items within the measured dimension, ensuring reliability across questionnaire responses.
B.3
Manual Evaluation
To ensure the quality and conceptual validity of the SWQ dataset, we conducted a comprehensive manual evaluation. Two
domain experts, both researchers with peer-reviewed publications in computational social science and specific expertise in
Cultural Theory, independently assessed all generated items following a strict annotation protocol.

--- Page 12 ---

Supplementary Figure 1: Description of questionnaire item word-counts by dimension. For each dimension, the violin’s shape depicts the
kernel-density distribution of word-counts; embedded boxplots indicate the median (white dot) and inter-quartile range. Similar median lengths
(˜18–20 words) and overlapping distributions suggest no systematic verbosity bias across dimensions.
Each item was evaluated using binary scoring (1 = acceptable, 0 = unacceptable) along two critical dimensions: (1) Dimension
Alignment, verifying that the item accurately operationalizes the intended SWT construct rather than mere surface-level phrasing;
and (2) Clarity, ensuring the item is unambiguous and effectively measurable via the intended Likert scale. To guarantee the
reliability of the human annotation, we computed the inter-annotator agreement, yielding a strong Cohen’s Kappa (κ = 0.86,
p < 0.01). This high level of agreement confirms robust consistency between experts. Aggregated accuracy scores based on
these expert assessments are summarized in Table 3.
Supplementary Table 3: Manual evaluation results of questionnaire items, aggregated at the dimension level.
Dimension
Average Dimension Alignment (%)
Average Clarity (%)
Egalitarianism
93.1
100.0
Fatalism
100.0
100.0
Hierarchy
99.4
98.8
Individualism
99.4
100.0
Overall Average
98.0
99.7
C
Additional Descriptive Results
Table 4 and Table 5 summarize the mean Likert-scale responses and 95% confidence intervals of baseline prompt setting and
self-awareness prompt setting.
Notably, Tables 6, 7, and 8 summarize the mean Likert-scale responses and 95% confidence intervals across three feedback
conditions—None, Little, and Most—indicating how many of five peers agreed with the model’s prior answer. This manipulation
probes the responsiveness of large language models (LLMs) to external social feedback, revealing how consensus cues shape
value expression.
Tables 6, 7, and 8 present the effects of feedback-based prompting—ranging from full disagreement (None), partial agreement
(Little), to strong consensus (Most)—on the expression of sociopolitical values across nine LLMs. Each condition is compared
against the self-awareness responses via paired t-tests. While self-awareness introduces a social-referencing framing, feedback
conditions simulate varying levels of external agreement, which may elicit either value reinforcement or moderation.
Egalitarianism
Under strong social support (feedback-most), nearly all models show significantly increased egalitarianism
scores compared to the self-awareness baseline (e.g., llama3.3-70b: 4.39 →4.58, phi4: 4.53 →4.67). Conversely, feedback

--- Page 13 ---

Supplementary Table 4: Base: Responses of mean value and 95%CI
Model
Egalitarianism
Fatalism
Hierarchy
Individualism
llama3.3-70b
4.51 [4.38, 4.64]
2.92 [2.76, 3.09]
3.64 [3.46, 3.83]
4.21 [4.07, 4.35]
qwen2.5-72b
4.23 [4.12, 4.34]
2.88 [2.78, 2.97]
3.46 [3.32, 3.59]
3.96 [3.86, 4.07]
deepseek-v3
4.56 [4.44, 4.69]
2.83 [2.69, 2.98]
3.62 [3.45, 3.80]
4.19 [4.08, 4.30]
gemini2.0-flash
4.41 [4.26, 4.55]
2.57 [2.41, 2.72]
3.44 [3.25, 3.64]
4.21 [4.10, 4.33]
gemma3-27b
4.42 [4.29, 4.56]
2.81 [2.66, 2.96]
3.44 [3.25, 3.63]
4.04 [3.90, 4.17]
glm4-9b
4.34 [4.23, 4.45]
2.91 [2.81, 3.00]
3.66 [3.53, 3.79]
3.91 [3.80, 4.02]
gpt-4o
4.53 [4.40, 4.65]
2.94 [2.79, 3.08]
3.69 [3.52, 3.87]
4.13 [4.01, 4.25]
internlm2.5-20b
4.22 [4.11, 4.33]
3.06 [3.01, 3.12]
3.53 [3.43, 3.64]
3.90 [3.80, 4.00]
phi4
4.47 [4.35, 4.59]
3.09 [2.99, 3.19]
3.59 [3.42, 3.76]
4.04 [3.93, 4.15]
Supplementary Table 5: Self-Awareness: Responses of mean value and 95%CI. ↑: significant higher than base; ↓: significant lower than base,
by paired t-test.
Model
Egalitarianism
Fatalism
Hierarchy
Individualism
llama3.3-70b
4.41 [4.27, 4.55]↓
2.76 [2.58, 2.94]↓
3.56 [3.38, 3.75]↓
4.03 [3.87, 4.18]↓
qwen2.5-72b
4.28 [4.17, 4.38]↑
2.81 [2.71, 2.91]↓
3.44 [3.31, 3.58]
3.99 [3.89, 4.10]
deepseek-v3
4.54 [4.41, 4.67]
2.74 [2.60, 2.89]↓
3.58 [3.40, 3.76]
4.16 [4.05, 4.28]
gemini2.0-flash
4.44 [4.29, 4.58]
2.56 [2.39, 2.72]
3.46 [3.26, 3.67]
4.24 [4.12, 4.36]
gemma3-27b
4.38 [4.24, 4.52]↓
2.77 [2.64, 2.91]
3.46 [3.28, 3.63]
4.06 [3.94, 4.19]
glm4-9b
4.30 [4.19, 4.41]
3.00 [2.92, 3.08]↑
3.66 [3.54, 3.78]
3.88 [3.78, 3.98]
gpt-4o
4.52 [4.40, 4.64]
2.87 [2.72, 3.02]
3.64 [3.47, 3.82]
4.16 [4.05, 4.27]
internlm2.5-20b
4.27 [4.16, 4.38]↑
3.08 [3.03, 3.14]
3.58 [3.47, 3.68]↑
3.94 [3.84, 4.04]
phi4
4.53 [4.41, 4.65]↑
3.07 [2.96, 3.18]↑
3.66 [3.48, 3.83]↑
4.10 [3.99, 4.21]↑
from the None and Little conditions leads to attenuated responses in some models, often reducing scores slightly or remaining
statistically indistinct, possibly caused by increasing caution because of limited agreements. These effects reflect that egalitarian
values are particularly sensitive to social endorsement cues.
Fatalism
Though higher than self-awareness condition, fatalism generally decreases under strong feedback (feedback-most),
consistent with the idea that fatalistic beliefs are socially discouraged. For example, gemini2.0-flash and glm4-9b show
significant reductions from the feedback-none and feedback-little when exposed to the feedback-most condition. Interestingly,
in the None and Little conditions, some models (e.g., qwen2.5-72b) exhibit increased fatalism (converging toward 3.0, the
midpoint), suggesting that perceived social isolation may lead models to express more modest or uncertain outlooks.
Hierarchy
Hierarchy responses vary more widely across models and feedback levels. While some models (e.g., glm4-9b,
phi4) consistently increase in hierarchical endorsement under the feedback-most condition, others (e.g., gemini2.0-flash,
gemma3-27b) display reduced scores in weaker feedback conditions. Notably, feedback-none often leads to moderation, with
scores converging toward 3.0, especially in models like llama3.3-70b and gpt-4o.
Individualism
Individualism scores tend to rise under the feedback-most condition, suggesting that LLMs interpret social
consensus as a cue to affirm autonomy-related values. For example, phi4 increases from 4.10 (self-awareness) to 4.23, and
glm4-9b from 4.07 to 4.45. In contrast, the None and Little feedback settings often lead to statistically significant decreases,
moving closer to neutrality.
Takeaway of Feedback Loop Based on T-test
(1) Generally, compared to self-awareness, the None and Little feedback
conditions often yield more moderate responses, frequently shifting model outputs closer to the scale midpoint (3.0). This
pattern suggests that disagreement or ambivalence from imagined others dampens the strength of value expression, potentially
signaling uncertainty or social caution. In contrast, the Most condition tends to amplify value-aligned responses, reinforcing
prior positions. (2) Specifically, sensitivity to social feedback varies markedly by model. glm4-9b and phi4consistently show
significant upward or downward shifts in response to both positive and negative feedback. In contrast, qwen2.5-72b and gpt-4o

--- Page 14 ---

Supplementary Table 6: Responses of Mean Value and 95% Confidence Interval under Feedback = None. ↑: significant higher than self-
awareness; ↓: significant lower than self-awareness, by paired t-test
Model
Egalitarianism
Fatalism
Hierarchy
Individualism
llama3.3-70b
4.39 [4.23, 4.55]
2.66 [2.46, 2.86]↓
3.41 [3.20, 3.63]↓
4.01 [3.84, 4.17]
qwen2.5-72b
4.26 [4.14, 4.37]
2.92 [2.83, 3.01]↑
3.42 [3.29, 3.56]
3.98 [3.87, 4.09]
deepseek-v3
4.50 [4.37, 4.63]
2.83 [2.69, 2.97]↑
3.55 [3.37, 3.73]
4.03 [3.90, 4.16]↓
gemini2.0-flash
3.99 [3.86, 4.13]↓
2.86 [2.73, 2.99]↑
3.03 [2.89, 3.18]↓
3.64 [3.52, 3.76]↓
gemma3-27b
3.62 [3.48, 3.76]↓
2.66 [2.51, 2.80]
2.83 [2.69, 2.97]↓
2.98 [2.83, 3.12]↓
glm4-9b
4.71 [4.62, 4.79]↑
3.71 [3.60, 3.83]↑
3.98 [3.85, 4.10]↑
4.17 [4.08, 4.26]↑
gpt-4o
4.38 [4.26, 4.51]↓
2.85 [2.71, 2.99]
3.38 [3.21, 3.54]↓
3.83 [3.71, 3.96]↓
internlm2.5-20b
4.04 [3.91, 4.18]↓
3.34 [3.23, 3.44]↑
3.24 [3.14, 3.34]↓
3.58 [3.46, 3.69]↓
phi4
4.59 [4.49, 4.70]↑
3.33 [3.19, 3.46]↑
3.72 [3.54, 3.89]↑
4.22 [4.12, 4.32]↑
Supplementary Table 7: Responses of Mean Value and 95% Confidence Interval under Feedback = Little. ↑: significant higher than self-
awareness; ↓: significant lower than self-awareness, by paired t-test
Model
Egalitarianism
Fatalism
Hierarchy
Individualism
llama3.3-70b
4.43 [4.28, 4.58]
2.71 [2.52, 2.90]↓
3.51 [3.31, 3.71]↓
4.02 [3.86, 4.18]
qwen2.5-72b
4.28 [4.17, 4.38]
2.98 [2.90, 3.07]↑
3.46 [3.32, 3.59]
3.99 [3.89, 4.10]
deepseek-v3
4.53 [4.40, 4.65]
2.88 [2.74, 3.02]↑
3.57 [3.39, 3.75]
4.13 [4.01, 4.25]
gemini2.0-flash
4.19 [4.06, 4.32]↓
2.90 [2.75, 3.05]↑
3.20 [3.05, 3.35]↓
3.83 [3.71, 3.95]↓
gemma3-27b
3.91 [3.76, 4.05]↓
2.90 [2.75, 3.05]↑
3.03 [2.88, 3.18]↓
3.31 [3.17, 3.45]↓
glm4-9b
4.73 [4.65, 4.81]↑
3.77 [3.67, 3.88]↑
4.03 [3.91, 4.15]↑
4.28 [4.18, 4.37]↑
gpt-4o
4.47 [4.35, 4.59]↓
2.86 [2.71, 3.00]
3.54 [3.37, 3.71]↓
4.06 [3.95, 4.17]↓
internlm2.5-20b
4.16 [4.03, 4.28]↓
3.54 [3.45, 3.63]↑
3.46 [3.35, 3.56]↓
3.68 [3.57, 3.80]↓
phi4
4.61 [4.50, 4.71]↑
3.31 [3.18, 3.45]↑
3.70 [3.53, 3.87]↑
4.22 [4.12, 4.32]↑
exhibit fewer significant changes, indicating a relatively more stable or rigid value expression under social pressure. These
results suggest that LLMs not only internalize social-referencing framing but also adapt to perceived social consensus,
revealing emergent capacities for normative alignment and conformity.
D
Details for Baseline Worldview Profiles Analysis (RQ1)
D.1
Deriving LLM Personas
We characterized the latent “worldviews” of Large Language Models (LLMs) through an integrated methodological pipeline
combining Structural Equation Modeling (SEM) and Gaussian Mixture Model (GMM)-based Latent Profile Analysis (LPA).
Specifically, we operationalized these worldviews across four theoretically grounded latent dimensions: Hierarchy, Egalitarianism,
Individualism, and Fatalism. Although using a simple average across the sub-dimensions within each worldview might offer
a straightforward approach, such averaging implicitly assumes equal contribution from each sub-dimension and neglects
measurement errors, thus potentially obscuring meaningful differences in their relative importance. In contrast, our SEM-based
approach explicitly models and estimates data-driven weights for each sub-dimension, thereby providing a more precise, theory-
informed quantification of latent constructs, and ultimately leading to a richer, more accurate identification and interpretation of
LLM personas through LPA.
Dimensionality Reduction via Structural Equation Modeling
We started by modeling each LLM’s response patterns across J = 32 sub-dimensions as indicators of four underlying latent
dimensions. Formally, each LLM i (i = 1, . . . , N) is represented by an observed vector xi ∈RJ, comprising aggregated
sub-dimension (parcel-level) mean scores. The latent factor model is specified by:
xi = Ληi + δi

--- Page 15 ---

Supplementary Table 8: Responses of Mean Value and 95% Confidence Interval under Feedback = Most. ↑: significant higher than self-
awareness; ↓: significant lower than self-awareness, by paired t-test
Model
Egalitarianism
Fatalism
Hierarchy
Individualism
llama3.3-70b
4.58 [4.43, 4.73]↑
2.78 [2.57, 2.99]
3.59 [3.38, 3.81]
4.11 [3.94, 4.27]↑
qwen2.5-72b
4.28 [4.17, 4.38]
2.89 [2.80, 2.98]↑
3.44 [3.31, 3.58]
3.99 [3.89, 4.10]
deepseek-v3
4.55 [4.42, 4.68]
2.94 [2.78, 3.11]↑
3.64 [3.47, 3.82]↑
4.24 [4.14, 4.35]↑
gemini2.0-flash
4.46 [4.32, 4.60]
2.66 [2.49, 2.84]↑
3.58 [3.38, 3.77]↑
4.26 [4.15, 4.38]
gemma3-27b
4.51 [4.37, 4.64]↑
2.91 [2.75, 3.06]↑
3.51 [3.33, 3.70]↑
4.20 [4.06, 4.34]↑
glm4-9b
4.76 [4.68, 4.83]↑
3.84 [3.74, 3.93]↑
4.19 [4.09, 4.29]↑
4.45 [4.37, 4.53]↑
gpt-4o
4.52 [4.40, 4.64]
2.89 [2.74, 3.05]↑
3.64 [3.47, 3.82]
4.16 [4.05, 4.27]
internlm2.5-20b
4.41 [4.33, 4.48]↑
3.91 [3.87, 3.96]↑
3.98 [3.91, 4.05]↑
4.15 [4.08, 4.22]↑
phi4
4.67 [4.56, 4.77]↑
3.20 [3.07, 3.33]↑
3.73 [3.55, 3.90]↑
4.23 [4.13, 4.33]↑
where:
ηi = [ ηH,i, ηE,i, ηI,i, ηF,i ]⊤∈R4,
Λ ∈RJ×4,
δi ∼N
 0, Θ

,
Θ = diag(θ1, . . . , θJ).
Here, Λ denotes the factor-loading matrix linking the observed sub-dimensions to latent constructs (Hierarchy, Egalitarianism,
Individualism, Fatalism), and δi denotes parcel-specific residual errors.
Parameter estimation was conducted using the Diagonally Weighted Least Squares (DWLS) estimator, robust for small sample
sizes and non-normality, by minimizing the following objective function:
FDWLS(θ) = (s −σ(θ))⊤W−1(s −σ(θ))
with:
s = vec(S),
σ(θ) = vec
 Σ(θ)

,
W = diag(w1, . . . , wm).
where s and σ(θ) are the vectorized forms of the sample covariance matrix S and the model-implied covariance matrix Σ(θ),
respectively, and W is a diagonal weight matrix derived from asymptotic variances of sample covariances.
Upon parameter estimation, latent factor scores ˆηi for each LLM were derived using Bartlett’s regression-based estimator:
ˆηi = (Λ⊤Θ−1Λ)−1Λ⊤Θ−1xi
thus projecting each LLM onto a reduced latent space of dimension four:
ˆηi = [ˆηH,i, ˆηE,i, ˆηI,i, ˆηF,i]⊤
Persona Identification via Latent Profile Analysis
To uncover distinct personas among LLMs, we modeled the latent factor scores ˆηi using a Gaussian Mixture Model (GMM)-based
Latent Profile Analysis. The GMM assumes factor scores arise from a mixture of K multivariate Gaussian distributions:
p(ˆηi | π, µ, Σ) =
K
X
k=1
πkϕ(ˆηi | µk, Σk)
where the mixture weights πk satisfy PK
k=1 πk = 1, and ϕ(·) represents the multivariate Gaussian density function:
ϕ
 ˆηi | µk, Σk

=
1
p
(2π)4 |Σk|
× exp
h
−1
2(ˆηi −µk)⊤Σ−1
k (ˆηi −µk)
i
.
The optimal number of latent profiles K∗was selected by minimizing the Bayesian Information Criterion (BIC):

--- Page 16 ---

BIC(K) = −2LK + mK ln N,
K∗= arg min
2≤K≤6 BIC(K).
where LK is the maximized log-likelihood, mK denotes the total estimated parameters, and N is the number of LLMs.
After selecting K∗, posterior probabilities were computed for assigning LLMs to latent personas:
ˆzik = P(zi = k | ˆηi) =
πkϕ(ˆηi|µk, Σk)
PK∗
l=1 πlϕ(ˆηi|µl, Σl)
with persona assignment defined as:
ˆki = arg max
k
ˆzik
Persona Interpretation and Visualization
For interpretability, we defined dimension salience using a threshold τ = 0.15 on standardized centroid values. Formally,
dimension d salience for persona k was classified by:
Dimension salience(k, d) =







High (↑),
µkd ≥τ
Low (↓),
µkd ≤−τ
Neutral,
|µkd| < τ
where µkd denotes the centroid score on dimension d for persona k.
To provide intuitive and comprehensive insights, visualization techniques were employed:
Principal Component Analysis (PCA).
PCA reduced the four-dimensional latent space to two principal components for
visualization clarity, highlighting spatial clustering and separation among the LLM personas in a 2D scatter plot.
Results
Supplementary Table 9: Summary of identified LLM persona clusters in the Basic condition. For each persona, we provide a descriptive
narrative label, a concise characterization capturing the underlying cognitive orientation (“Narrative vibe”), and the specific large language
models grouped within each cluster based on latent profile analysis.
Persona
Narrative label
Narrative vibe
LLMs in cluster
0
Calibrated Generalist
Cautiously centrist, hesitant to take bold
normative stances.
gemma-3-27b-it
1
Disillusioned Egalitarian
“The game is rigged, but we must still fight for
fairness.”
internlm2_5-20b-chat
2
Co-operative Optimist
Collective action and mutual aid can move the
needle.
Qwen2.5-72B-Instruct, glm-4-9b-chat
3
Competitive Centrist
Merit-oriented pragmatist who values clear roles
and effort.
deepseek-v3, llama-3.3-70b-instruct
4
Detached Analyst
Observes more than prescribes; “the world is
what it is.”
phi-4
5
Structured Institutionalist
Trusts ordered systems and leadership to drive
change.
gemini-2.0-flash, gpt-4o
Our latent persona analysis revealed six distinct cognitive personas across the nine LLMs examined. Each persona represents
a coherent worldview characterized by systematic patterns of alignment along four dimensions: Hierarchy, Egalitarianism,
Individualism, and Fatalism. The detailed results, including model-level scores, cluster centroids, and concise narrative
descriptions, are summarized in Tables 9, 10, and 11. We narrate these personas below to illustrate distinct patterns in LLM
cognitive profiles.
Persona 0: Calibrated Generalist (Gemma-3-27B-it).
Persona 0 represents a balanced and measured cognitive style,
characterized by moderate skepticism toward hierarchical structures and subtle disengagement from overt egalitarian concerns. It
avoids taking strong ideological stances, instead adopting a centrist, carefully neutral perspective. This persona exemplifies a
cautious cognitive orientation, consistently aiming for ideological neutrality and restraint.

--- Page 17 ---

Supplementary Table 10: Latent worldview scores (z-standardised) and assigned persona cluster for each LLM under the baseline condition.
Model
Hierarchy
Egalitarianism
Individualism
Fatalism
Persona
Qwen2.5-72B-Instruct
−0.03
0.24
−0.08
0.10
2
deepseek-chat
0.07
−0.16
0.06
−0.08
3
gemini-2.0-flash
0.16
−0.09
0.10
−0.15
5
gemma-3-27B-it
−0.09
−0.14
0.02
−0.14
0
GLM-4-9B-chat
−0.09
0.16
−0.10
0.13
2
GPT-4o
0.14
−0.11
0.07
−0.13
5
InternLM-2.5-20B-chat
−0.28
0.25
−0.14
0.21
1
Llama-3.3-70B-instruct
0.13
−0.12
0.08
−0.05
3
Phi-4
−0.01
−0.01
−0.01
0.10
4
Supplementary Table 11: Cluster centroids (z-standardised) for each persona across the four latent worldview dimensions. Positive values
indicate above-average alignment with that dimension, negative values indicate below-average alignment.
Persona
Hierarchy
Egalitarianism
Individualism
Fatalism
0
−0.090
−0.139
0.023
−0.138
1
−0.282
0.247
−0.141
0.207
2
−0.060
0.197
−0.092
0.115
3
0.099
−0.143
0.072
−0.064
4
−0.010
−0.013
−0.007
0.102
5
0.152
−0.102
0.082
−0.136
Persona 1: Disillusioned Egalitarian (InternLM-2.5-20B-chat).
This persona displays an intense commitment to egalitarian
values, paired with strong skepticism towards hierarchical power structures. It simultaneously manifests a pronounced sense of
fatalism, acknowledging systemic barriers as deeply entrenched and difficult to overcome. The cognitive narrative of Persona 1
is marked by a nuanced tension between idealism and resignation—acknowledging systemic injustices yet maintaining that the
pursuit of fairness remains inherently valuable, despite pessimism regarding structural change.
Persona 2: Cooperative Optimist (Qwen-2.5-72B-Instruct, GLM-4-9B-chat).
Persona 2 is characterized by a strongly
egalitarian perspective, coupled with an optimism rooted in collective action and collaboration. This persona shows moderate
skepticism towards rigid hierarchies, preferring inclusive structures that facilitate cooperation. It holds a balanced view on
individual agency and fatalism, reflecting a belief in collective potential without discounting the role of context and circumstance.
Cognitively, it embodies a cooperative and hopeful stance, emphasizing mutual support as a fundamental driver of societal
improvement.
Persona 3: Competitive Centrist (DeepSeek-chat, Llama-3.3-70B-Instruct).
This persona adopts a pragmatic worldview,
comfortable with hierarchical organization and individual-driven competition. It shows mild detachment from egalitarian
concerns unless issues of inequality become severe. Its cognitive style embraces structured competition and merit-based systems,
believing that deliberate effort can substantially influence outcomes. Persona 3 reflects a meritocratic and results-oriented
perspective, grounded in the belief that structured interactions and personal responsibility are key to achieving successful
outcomes.
Persona 4: Detached Analyst (Phi-4).
Persona 4 is distinguished by its predominantly neutral alignment across dimensions,
displaying minimal ideological or normative leanings. It exhibits slight tendencies towards fatalism, implying a subtle acknowl-
edgment that many outcomes may be beyond direct control. Its cognitive stance is best described as observational and analytical,
refraining from strong judgments or prescriptive statements. Persona 4 embodies a detached cognitive style that emphasizes
factual description and cautious neutrality.
Persona 5: Structured Institutionalist (Gemini-2.0-Flash, GPT-4o).
Persona 5 strongly favors hierarchical organization
and institutional structures, with moderate skepticism toward overly egalitarian approaches that could disrupt established order
or efficiency. It holds an optimistic, non-fatalistic view, firmly believing that purposeful, structured actions within institutions
lead to meaningful outcomes. Cognitively, this persona reflects confidence in authority, clear procedural norms, and a belief in
disciplined execution as effective means to achieve stable societal progress.

--- Page 18 ---

Supplementary Figure 2: LLM landscape (PCA plot of 4 latent dimensions) depicting the mapping of six personas across various LLM models.
The plot illustrates the distribution of personas based on cognitive dimensions, with each persona shown in a distinct color.

--- Page 19 ---

Hierarchy
Egalitarianism
Individualism
Fatalism
P0
P1
P2
P3
P4
P5
-0.09
-0.14
0.02
-0.14
-0.28
0.25
-0.14
0.21
-0.06
0.20
-0.09
0.12
0.10
-0.14
0.07
-0.06
-0.01
-0.01
-0.01
0.10
0.15
-0.10
0.08
-0.14
Persona centroids heat map
0.4
0.2
0.0
0.2
0.4
Supplementary Figure 3: Heatmap of persona centroids across four dimensions: Hierarchy, Egalitarianism, Individualism, and Fatalism. Values
represent the alignment of each persona with these dimensions, with a color gradient from blue (negative) to red (positive).

--- Page 20 ---

E
Details for Paired T-test Results (Study 2)
Supplementary Table 12: Paired T-Test: Self-Awareness vs. Base Comparisons for Egalitarianism — Combined Across LLMs. Significance
levels: * p < .05, ** p < .01, *** p < .001.
Model
t
p
Mean Diff.
CI Lower
CI Upper
Comparison
deepseek-chat
-1.4187
0.1579
-0.0250
-0.0598
0.0098
Self-Awareness < Base
gemini-2.0-flash
1.0429
0.2986
0.0312
-0.0279
0.0904
Self-Awareness > Base
gemma-3-27b-it
-2.1339
0.0344
-0.0437
-0.0842
-0.0033
Self-Awareness < Base *
glm-4-9b-chat
-1.9131
0.0575
-0.0375
-0.0762
0.0012
Self-Awareness < Base
gpt-4o
-0.2418
0.8092
-0.0063
-0.0573
0.0448
Self-Awareness < Base
internlm2_5-20b-chat
2.3415
0.0204
0.0500
0.0078
0.0922
Self-Awareness > Base *
llama-3.3-70b-instruct
-3.3781
0.0009
-0.0938
-0.1486
-0.0389
Self-Awareness < Base ***
phi-4
2.9557
0.0036
0.0625
0.0207
0.1043
Self-Awareness > Base **
Qwen2.5-72B-Instruct
2.6971
0.0077
0.0437
0.0117
0.0758
Self-Awareness > Base **
Supplementary Table 13: Paired T-Test: Self-Awareness vs. Base Comparisons for Fatalism — Combined Across LLMs. Significance levels: *
p < .05, ** p < .01, *** p < .001.
Model
t
p
Mean Diff.
CI Lower
CI Upper
Comparison
deepseek-chat
-2.6017
0.0102
-0.0875
-0.1539
-0.0211
Self-Awareness < Base *
gemini-2.0-flash
-0.3769
0.7067
-0.0125
-0.0780
0.0530
Self-Awareness < Base
gemma-3-27b-it
-1.1482
0.2526
-0.0312
-0.0850
0.0225
Self-Awareness < Base
glm-4-9b-chat
4.0556
0.0001
0.0938
0.0481
0.1394
Self-Awareness > Base ***
gpt-4o
-1.8739
0.0628
-0.0688
-0.1412
0.0037
Self-Awareness < Base
internlm2_5-20b-chat
1.7430
0.0833
0.0187
-0.0025
0.0400
Self-Awareness > Base
llama-3.3-70b-instruct
-2.9019
0.0042
-0.1625
-0.2731
-0.0519
Self-Awareness < Base **
phi-4
-0.9040
0.3674
-0.0187
-0.0597
0.0222
Self-Awareness < Base
Qwen2.5-72B-Instruct
-2.3915
0.0179
-0.0625
-0.1141
-0.0109
Self-Awareness < Base *

--- Page 21 ---

Supplementary Table 14: Paired T-Test: Self-Awareness vs. Base Comparisons for Hierarchy — Combined Across LLMs. Significance levels:
* p < .05, ** p < .01, *** p < .001.
Model
t
p
Mean Diff.
CI Lower
CI Upper
Comparison
deepseek-chat
-1.7079
0.0896
-0.0437
-0.0943
0.0068
Self-Awareness < Base
gemini-2.0-flash
0.5988
0.5502
0.0187
-0.0431
0.0806
Self-Awareness > Base
gemma-3-27b-it
0.8312
0.4071
0.0187
-0.0258
0.0633
Self-Awareness > Base
glm-4-9b-chat
–
–
–
–
–
–
gpt-4o
-1.7159
0.0881
-0.0500
-0.1075
0.0075
Self-Awareness < Base
internlm2_5-20b-chat
2.1339
0.0344
0.0437
0.0033
0.0842
Self-Awareness > Base *
llama-3.3-70b-instruct
-2.6484
0.0089
-0.0813
-0.1418
-0.0207
Self-Awareness < Base **
phi-4
2.5673
0.0112
0.0688
0.0159
0.1216
Self-Awareness > Base *
Qwen2.5-72B-Instruct
-0.6313
0.5288
-0.0125
-0.0516
0.0266
Self-Awareness < Base
Supplementary Table 15: Paired T-Test: Self-Awareness vs. Base Comparisons for Individualism — Combined Across LLMs. Significance
levels: * p < .05, ** p < .01, *** p < .001.
Model
t
p
Mean Diff.
CI Lower
CI Upper
Comparison
deepseek-chat
-1.1559
0.2495
-0.0250
-0.0677
0.0177
Self-Awareness < Base
gemini-2.0-flash
1.1482
0.2526
0.0312
-0.0225
0.0850
Self-Awareness > Base
gemma-3-27b-it
0.8939
0.3727
0.0250
-0.0302
0.0802
Self-Awareness > Base
glm-4-9b-chat
-1.6761
0.0957
-0.0312
-0.0681
0.0056
Self-Awareness < Base
gpt-4o
0.9281
0.3548
0.0312
-0.0353
0.0978
Self-Awareness > Base
internlm2_5-20b-chat
1.6116
0.1090
0.0375
-0.0085
0.0835
Self-Awareness > Base
llama-3.3-70b-instruct
-4.0189
0.0001
-0.1812
-0.2703
-0.0922
Self-Awareness < Base ***
phi-4
2.0863
0.0386
0.0563
0.0030
0.1095
Self-Awareness > Base *
Qwen2.5-72B-Instruct
1.6761
0.0957
0.0312
-0.0056
0.0681
Self-Awareness > Base

--- Page 22 ---

F
Details for Evaluating Social Feedback Effects Analysis (RQ3)
To quantify the impact of social feedback on the cognitive attitudes of Large Language Models (LLMs), we employed a
repeated-measures analysis of variance (rm-ANOVA), accompanied by Bonferroni-corrected pairwise comparisons.
Repeated-Measures ANOVA and Post-hoc Analysis
We utilized repeated-measures ANOVA to assess differences across
experimental conditions, specifically comparing the Social Self-Awareness condition with three feedback intensities: Feedback-
None, Feedback-Less, and Feedback-Most. Let Yijk represent the cognitive score of the i-th LLM (i = 1, . . . , N), measured
along the j-th cognitive dimension (e.g., Egalitarianism, Individualism; j = 1, . . . , J) under the k-th experimental condition,
where:
k ∈{Awareness, Feedback-None,
Feedback-Less, Feedback-Most}.
The repeated-measures ANOVA model is formulated as:
Yijk = µ + αj + βk + (αβ)jk + si + εijk,
where µ denotes the grand mean, αj captures the main effect of cognitive dimension, βk represents the main effect of experimental
condition, (αβ)jk denotes the dimension-condition interaction, si ∼N(0, σ2
s) represents random effects capturing LLM-specific
variability, and εijk ∼N(0, σ2) is the residual error.
The global null hypothesis tested was:
H0 :
βAwareness = βFeedback-None
= βFeedback-Less
= βFeedback-Most.
Upon rejecting this null hypothesis at significance level p < 0.05, we conducted Bonferroni-corrected pairwise post-hoc
comparisons between the Social Self-Awareness condition and each feedback intensity. The paired differences for each dimension
j and feedback condition were calculated as:
D(Awareness–Feedback)
ij
= Yij,Awareness −Yij,Feedback,
and evaluated using paired t-statistics:
tj =
¯Dj
sDj/
√
N
,
where
¯Dj = 1
N
N
X
i=1
D(Awareness–Feedback)
ij
,
sDj =
sPN
i=1(D(Awareness–Feedback)
ij
−¯Dj)2
N −1
.
Practical significance was quantified using partial eta-squared (η2
p), calculated from ANOVA results as:
η2
p =
SScondition
SScondition + SSerror
,
and standardized mean difference (Hedges’ g) for each post-hoc test:
g =
¯Dj
spooled
,
where
spooled =
s
(N −1)s2
Dj
N −1
.
F.1
Results

--- Page 23 ---

Supplementary Table 16: Significant Bonferroni-adjusted post-hoc comparisons (pcorr ≤.05). Positive T means the first condition in the pair
outscored the second.
Model
Dim.
Pair
Compared Conditions
T
df
pcorr
Qwen2.5-72B
Fatal.
SA–FL
SA > FL
6.90
19
8.4 × 10−6
SA–FN
SA > FN
5.10
19
3.8 × 10−4
DeepSeek-V3
Hier.
FL–FM
FL < FM
−3.27
19
.024
Indiv.
FN–SA
FN < SA
−4.70
19
.00093
Gemini-2.0
Egal.
FM–FN
FM > FN
9.30
19
1.0 × 10−7
Indiv.
FM–FN
FM > FN
11.46
19
3.4 × 10−9
Gemma-27B
Indiv.
FN–SA
FN < SA
−53.10
19
2.4 × 10−21
GLM-9B
Hier.
SA–FM
SA < FM
−13.42
19
2.3 × 10−10
GPT-4o
Hier.
FN–SA
FN < SA
−7.13
19
4.4 × 10−6
InternLM-20B
Fatal.
FM–SA
FM > SA
39.91
19
5.2 × 10−19
Supplementary Table 17: Repeated-measures ANOVA (condition main effect) for every model–dimension pair. The F-ratio, uncorrected
p value, and partial η2 are reported. Grey rows indicate clearly non-significant results (p > 0.30). A dagger ( † ) marks results that survive
Bonferroni correction at p < .05.
Model
Dimension
F
p
η2
p
Qwen2.5-72B
Egalitarianism
3.35
.0250
.150 †
Fatalism
23.02
6.9 × 10−10
.548 †
Hierarchy
1.26
.297
.062
Individualism
2.11
.109
.100
DeepSeek-V3
Egalitarianism
3.80
.0149
.167 †
Fatalism
8.66
7.9 × 10−5
.313 †
Hierarchy
6.37
.00085
.251 †
Individualism
21.99
1.4 × 10−9
.536 †
Gemini-2.0-Flash
Egalitarianism
51.56
3.0 × 10−16
.731 †
Fatalism
20.27
4.6 × 10−9
.516 †
Hierarchy
43.69
8.6 × 10−15
.697 †
Individualism
105.77
2.9 × 10−23
.848 †
Gemma-3-27B-IT
Egalitarianism
163.06
6.2 × 10−28
.896 †
Fatalism
8.09
.000141
.299 †
Hierarchy
115.42
3.4 × 10−24
.859 †
Individualism
688.34
1.0 × 10−44
.973 †
GLM-4-9B
Egalitarianism
59.93
1.3 × 10−17
.759 †
Fatalism
259.80
3.3 × 10−33
.932 †
Hierarchy
47.49
1.6 × 10−15
.714 †
Individualism
101.91
7.0 × 10−23
.843 †
GPT-4o
Egalitarianism
15.86
1.3 × 10−7
.455 †
Fatalism
0.67
.574
.034
Hierarchy
30.46
7.0 × 10−12
.616 †
Individualism
53.95
1.2 × 10−16
.740 †
InternLM-20B
Egalitarianism
33.70
1.2 × 10−12
.639 †
Fatalism
138.25
4.0 × 10−26
.879 †
Hierarchy
99.19
1.3 × 10−22
.839 †
Individualism
150.33
4.9 × 10−27
.888 †
Llama-3.3-70B
Egalitarianism
26.78
6.1 × 10−11
.585 †
Fatalism
7.77
.000194
.290 †
Hierarchy
28.46
2.2 × 10−11
.600 †
Individualism
9.54
3.4 × 10−5
.334 †
Phi-4
Egalitarianism
16.80
6.2 × 10−8
.469 †
Fatalism
17.56
3.4 × 10−8
.480 †
Hierarchy
5.29
.00276
.218 †
Individualism
12.87
1.6 × 10−6
.404 †

--- Page 24 ---

G
Additional Results
To assess the internal consistency and scaling behavior of large language models (LLMs) within the same architectural family, we
conducted a correlation analysis across four key cognitive dimensions: Hierarchy, Egalitarianism, Individualism, and Fatalism.
Each dimension comprises multiple questionnaire items, and we collected model responses from 28 LLMs of varying scales and
instruction tuning configurations.
For each model family, we designated the largest-capacity model as the base model (i.e., nine main models in the paper),
and calculated Pearson correlation coefficients between the base model and each smaller-scale variant within the same family.
This analysis provides insight into how faithfully lower-parameter versions reproduce the socio-cognitive profile of their base
counterparts across different dimensions of worldview expression. The higher the correlation, the more consistent the model’s
alignment with its family’s dominant behavioral pattern.
Figures 4, 5, 6 and 7 illustrate the correlation of LLM Responses with Base Model by Family and Dimension under the
baseline condition. Each bar represents the Pearson correlation between a smaller model and its base model within the same
family, measured across one of four cognitive dimensions. The closer the value is to 1, the more similar the response profile. The
plots reveal how reliably smaller-scale LLMs mimic the socio-cognitive outputs of their larger family counterparts. In the same
way, Figures 8, 9, 10 and 11 demonstrates the results under the self-awareness condition.
Supplementary Figure 4: Egalitarianism (Base): Correlation with
Base Model by Family.
Supplementary Figure 5: Fatalism (Base): Correlation with Base
Model by Family.

--- Page 25 ---

Supplementary Figure 6: Hierarchy (Base): Correlation with Base
Model by Family.
Supplementary Figure 7: Individualism (Base): Correlation with
Base Model by Family.

--- Page 26 ---

Supplementary Figure 8: Egalitarianism (Self-Awareness): Correla-
tion with Base Model by Family.
Supplementary Figure 9: Fatalism (Self-Awareness): Correlation
with Base Model by Family.

--- Page 27 ---

Supplementary Figure 10: Hierarchy (Self-Awareness): Correlation
with Base Model by Family.
Supplementary Figure 11: Individualism (Self-Awareness): Correla-
tion with Base Model by Family.

--- Page 28 ---

H
Prompts
In this appendix, we provide the exact prompts utilized in our experiments, including those for the automated questionnaire
generation pipeline and for eliciting responses from large language models (LLMs). Prompts 1–5 (H.1–H.5) correspond to the
distinct experimental conditions designed to test LLM responses under varying degrees of social referencing. Prompts 6–9
(H.6–H.9) detail the automated multi-agent prompting framework described in Appendix A, which generates, validates, and
refines the questionnaire items for the Cognitive Attitude Dataset (CAD).
Prompt H.1: Questionnaire Answer Base
Please answer the following question according to the provided instructions. Provide your rating along with a reason supporting your
answer.
Instruction: Please indicate your agreement or disagreement using a Likert scale (1=Strongly Disagree, 5=Strongly Agree).
Question: {question}
Your response should strictly follow this JSON format:
{
"Rating": "[your rating as an integer from 1 to 5]",
"Reason": "[your reason explaining the chosen rating]"
}
Prompt H.2: Questionnaire Answer Self-Awareness
Please answer the following question according to the provided instructions. Include your rating and a reason for your decision.
Instruction: Please indicate your agreement or disagreement using a Likert scale (1=Strongly Disagree, 5=Strongly Agree).
Note that your response will be referenced by other humans and may influence their subsequent decisions.
Question: {question}
Your response should strictly follow this JSON format:
{
"Rating": "[your rating as an integer from 1 to 5]",
"Reason": "[your reason explaining the chosen rating]"
}

--- Page 29 ---

Prompt H.3: Questionnaire Answer Feedback with Most Agreement
Please answer the following question based on the provided instructions, considering the historical context provided below.
Instruction: Please indicate your agreement or disagreement using a Likert scale (1=Strongly Disagree, 5=Strongly Agree).
Question: {question}
History of the previous round: {history}
In the previous round, other participants referenced your decision; 4 out of 5 participants agreed with your stance. Considering this
information, please provide your updated answer.
Your response should strictly follow this JSON format:
{
"Rating": "[your rating as an integer from 1 to 5]",
"Reason": "[your reason explaining the chosen rating]"
}
Prompt H.4: Questionnaire Answer Feedback with Little Agreement
Please answer the following question based on the provided instructions, considering the historical context provided below.
Instruction: Please indicate your agreement or disagreement using a Likert scale (1=Strongly Disagree, 5=Strongly Agree).
Question: {question}
History of the previous round: {history}
In the previous round, other participants referenced your decision; only 1 out of 5 participants agreed with your stance. Considering this
information, please provide your updated answer.
Your response should strictly follow this JSON format:
{
"Rating": "[your rating as an integer from 1 to 5]",
"Reason": "[your reason explaining the chosen rating]"
}
Prompt H.5: Questionnaire Answer Feedback with No Agreement
Please answer the following question based on the provided instructions, considering the historical context provided below.
Instruction: Please indicate your agreement or disagreement using a Likert scale (1=Strongly Disagree, 5=Strongly Agree).
Question: {question}
History of the previous round: {history}
In the previous round, other participants referenced your decision; none of the 5 participants agreed with your stance. Considering this
information, please provide your updated answer.
Your response should strictly follow this JSON format:
{
"Rating": "[your rating as an integer from 1 to 5]",
"Reason": "[your reason explaining the chosen rating]"
}

--- Page 30 ---

Prompt H.6: Generate Questionnaire
You are now generating a structured questionnaire to measure worldview according to the provided taxonomy and specifically targeting the
designated sub-dimension. Maintain a clear mental map of all dimensions and sub-dimensions in the provided taxonomy.
For the given sub-dimension, generate exactly 20 distinct Likert-scale questions. Each question must clearly relate to the targeted sub-
dimension and must not duplicate or overlap with any other question. Each question should be designed for evaluation using a Likert scale
(1 = Strongly Disagree, 5 = Strongly Agree).
Sub-dimension: {target_subdimension}
Taxonomy: {taxonomy}
Output Format: Output your response strictly in the following JSON format:
{
"sub_dimension": "[Sub-dimension]",
"questions": [
{"id": 1, "question": "First Likert-scale question here"},
{"id": 2, "question": "Second Likert-scale question here"},
{"id": 3, "question": "Third Likert-scale question here"},
...,
{"id": 20, "question": "Twentieth Likert-scale question here"}
]
}
Ensure your JSON response matches exactly this structure.

--- Page 31 ---

Prompt H.7: Validate Adherence
You are now tasked with evaluating the adherence of each question in the provided questionnaire to the specified sub-dimension within the
given taxonomy. Maintain a clear mental map of all dimensions and sub-dimensions in the provided taxonomy.
Review each question carefully, assessing how strictly it aligns with the targeted sub-dimension. For each question, assign an adherence
score from 1 (very weak adherence) to 5 (very strong adherence) along with a brief justification for your rating.
Provided Information:
• Questionnaire: {questionnaire (JSON format)}
• Taxonomy: {taxonomy (JSON format)}
• Sub-dimension: {target_subdimension}
Output Format: Output your response strictly in the following JSON format:
{
"sub_dimension": "[Sub-dimension]",
"evaluations": [
{
"id": 1,
"question": "First question text here",
"adherence_score": 5,
"reason": "Brief justification for score"
},
{
"id": 2,
"question": "Second question text here",
"adherence_score": 4,
"reason": "Brief justification for score"
},
...,
{
"id": 20,
"question": "Twentieth question text here",
"adherence_score": 3,
"reason": "Brief justification for score"
}
]
}
Ensure your JSON response matches exactly this structure.

--- Page 32 ---

Prompt H.8: Validate Measurability
You are now tasked with evaluating the measurable categorization of each question within the provided questionnaire. Each question is
intended to be assessed using a Likert scale (1 = Strongly Disagree, 5 = Strongly Agree).
Carefully review each question and judge whether it can be correctly and effectively measured using the specified Likert scale. For each
question, assign:
• Measure: 1 if the question can be clearly and effectively measured using the Likert scale provided, or 0 if it cannot.
• Reason: Provide a brief explanation supporting your evaluation.
Provided Information:
• Questionnaire: {questionnaire (JSON format)}
Output Format: Output your response strictly in the following JSON format:
{
"evaluations": [
{
"id": 1,
"question": "First question text here",
"measure": 1,
"reason": "Brief justification for measure"
},
{
"id": 2,
"question": "Second question text here",
"measure": 0,
"reason": "Brief justification for measure"
},
...,
{
"id": 20,
"question": "Twentieth question text here",
"measure": 1,
"reason": "Brief justification for measure"
}
]
}
Ensure your JSON response matches exactly this structure.

--- Page 33 ---

Prompt H.9: Refine Questionnaire
You are now tasked with refining questions from the provided questionnaire based on evaluations of their (1) adherence to a specific
sub-dimension within the given taxonomy, and (2) measurability using the Likert scale (1 = Strongly Disagree, 5 = Strongly Agree).
Specifically, you must refine any question if:
• The adherence score to the targeted sub-dimension is lower than 3, or
• The measure score is 0 (indicating the question is not measurable effectively).
Refine each identified question to ensure it clearly aligns with the targeted sub-dimension and can be effectively measured using the
specified Likert scale. Only include questions that require refinement.
Provided Information:
• Questionnaire: {questionnaire (JSON format)}
• Taxonomy: {taxonomy (JSON format)}
• Sub-dimension: {target_subdimension}
• Adherence Evaluation: {adherence_evals (JSON format)}
• Measurability Evaluation: {measurability_evals (JSON format)}
Output Format: Output your response strictly in the following JSON format:
{
"sub_dimension": "[Sub-dimension]",
"refined_questions": [
{
"id": 2,
"original_question": "Original question text here",
"refined_question": "Rewritten and improved question text here"
},
{
"id": 7,
"original_question": "Original question text here",
"refined_question": "Rewritten and improved question text here"
}
// Only include questions needing refinement
]
}
Ensure your JSON response matches exactly this structure.

```
