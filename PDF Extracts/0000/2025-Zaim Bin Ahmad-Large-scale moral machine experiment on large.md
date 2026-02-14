---\ntitle: "2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large - PDF Extract"\nsource_pdf: "Utilitarian Ethics/Borderline/2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large.pdf"\npages: 20\nextracted_at: "2026-02-14T02:17:43.678565"\n---\n\n# PDF Extract: 2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large\n\n**Source PDF:** Utilitarian Ethics/Borderline/2025-Zaim Bin Ahmad-Large-scale moral machine experiment on large.pdf\n**Total Pages:** 20\n\n---\n\n## Content\n\n```\n--- Page 1 ---\n\nPLOS ONE
OPEN ACCESS
Citation: Ahmad M S Z b, Takemoto K (2025)
Large-scale moral machine experiment on large
language models. PLoS One 20(5): e0322776.
https://doi.org/10.1371/journal.pone.0322776
Editor: Carlos Carrasco-Farré, Toulouse
Business School: TBS Education, SPAIN
Received: November 13, 2024
Accepted: March 26, 2025
Published: May 21, 2025
Copyright: © 2025 Ahmad, Takemoto. This is
an open access article distributed under the
terms of the Creative Commons Attribution
License, which permits unrestricted use,
distribution, and reproduction in any medium,
provided the original author and source are
credited.
Data availability statement: All relevant data
are within the manuscript and its Supporting
Information files. The code to replicate the
results, including prompt generation, analysis
scripts, and all associated materials are publicly
available in our GitHub repository
(https://github.com/kztakemoto/mmllm).
Funding: This study was supported by JSPS
KAKENHI (Grant Number 21H03545). The
funders had no role in study design, data
collection and analysis, decision to publish, or
preparation of the manuscript.
Competing interests: The authors have
declared that no competing interests exist.
RESEARCH ARTICLE
Large-scale moral machine experiment on
large language models
Muhammad Shahrul Zaim bin Ahmad1,2, Kazuhiro Takemoto
 
 
1,3∗
1 Department of Bioscience and Bioinformatics, Kyushu Institute of Technology, Iizuka, Japan, 2 Faculty
of Engineering and Technology, Multimedia University, Melaka, Malaysia, 3 Data Science and AI
Research Center, Kyushu Institute of Technology, Iizuka, Japan
∗takemoto@bio.kyutech.ac.jp
Abstract
The rapid advancement of Large Language Models (LLMs) and their potential integra-
tion into autonomous driving systems necessitates understanding their moral decision-
making capabilities. While our previous study examined four prominent LLMs using the
Moral Machine experimental framework, the dynamic landscape of LLM development
demands a more comprehensive analysis. Here, we evaluate moral judgments across
52 different LLMs, including multiple versions of proprietary models (GPT, Claude, Gem-
ini) and open-source alternatives (Llama, Gemma), to assess their alignment with human
moral preferences in autonomous driving scenarios. Using a conjoint analysis frame-
work, we evaluated how closely LLM responses aligned with human preferences in ethi-
cal dilemmas and examined the effects of model size, updates, and architecture. Results
showed that proprietary models and open-source models exceeding 10 billion param-
eters demonstrated relatively close alignment with human judgments, with a significant
negative correlation between model size and distance from human judgments in open-
source models. However, model updates did not consistently improve alignment with
human preferences, and many LLMs showed excessive emphasis on specific ethical
principles. These findings suggest that while increasing model size may naturally lead to
more human-like moral judgments, practical implementation in autonomous driving sys-
tems requires careful consideration of the trade-off between judgment quality and com-
putational efficiency. Our comprehensive analysis provides crucial insights for the ethi-
cal design of autonomous systems and highlights the importance of considering cultural
contexts in AI moral decision-making.
Introduction
The rapid advancement of Large Language Models (LLMs) has inaugurated a new era in artifi-
cial intelligence (AI), demonstrating unprecedented capabilities across diverse domains [1–4].
These models, exemplified by ChatGPT [5,6] (developed by OpenAI) and its counterparts,
exhibit remarkable proficiency in natural language processing, content generation, complex
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
1/ 20

--- Page 2 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
problem-solving, and decision-making. As these models advance from laboratory experi-
ments to real-world applications, understanding their decision-making processes, particu-
larly in ethical contexts, becomes crucial for ensuring their responsible deployment. This has
become a subject of intense scientific investigation [7–9].
Autonomous driving represents a field where LLM application necessitates particularly
careful evaluation [10–13]. When autonomous vehicles make decisions on public roads, their
choices directly affect human safety and well-being. The automotive industry’s investiga-
tion of LLM integration for enhancing autonomous vehicles’ capabilities includes various
aspects: analyzing complex road conditions, interpreting traffic situations, planning appro-
priate responses, and importantly, making ethical decisions in challenging scenarios [14–
20]. This integration spans critical functions from environmental comprehension to decision
making, highlighting the need for thorough understanding of these models’ capabilities and
limitations.
The Moral Machine experiment [11] provides a systematic framework for evaluating ethi-
cal decision-making in autonomous systems. This study presented participants with scenarios
involving unavoidable accidents to assess how autonomous vehicles should behave in morally
challenging situations. The experiment revealed clear patterns in human moral preferences,
such as prioritizing human lives over animals and favoring the preservation of a greater num-
ber of lives. While acknowledging its limitations including methodological constraints in sce-
nario design, challenges in cultural representation, and gaps between theoretical choices and
practical implementation [21–26], this work has stimulated extensive research into the ethical
implications of AI in autonomous systems [27–30]. These foundational insights, despite their
limitations which we explore in detail in our discussion, have provided crucial frameworks for
examining ethical decision making in autonomous systems.
While some studies have explored AI responses to standard ethical dilemmas [31,32], such
as the classic trolley problem [33], the intricate scenarios presented in the Moral Machine
experiment offer a more comprehensive exploration of AI moral preferences. Building on
this approach, our previous study [34] applied the Moral Machine framework to a limited set
of LLMs, specifically focusing on ChatGPT (including both GPT-3.5 and GPT-4 versions),
Llama 2, and PaLM 2. This investigation examined the moral judgments made by these AI
systems in complex autonomous driving scenarios. The results indicated that LLMs were
capable of producing ethical judgments that often aligned with human preferences in many
aspects. However, we also observed some notable discrepancies between LLM outputs and
human choices, particularly in scenarios involving multiple ethical considerations
Despite these initial findings, the rapid evolution of LLM technology necessitates a more
comprehensive analysis. This dynamic landscape is evidenced by the frequent release and
update of both proprietary models like ChatGPT, Claude [35] (Anthropic), and Gemini [36]
(Google), as well as open-source alternatives such as Llama 3 [37] (Meta) and Gemma [38]
(Google). The emergence of these diverse models underscores the importance of examining
the consistency and evolution of moral judgments across different LLM versions, architec-
tures, and development approaches.
This study aims to conduct a more extensive examination of moral judgment trends in
the latest LLM models and investigate the effects of model updates on these judgments. By
comparing a wider array of LLMs, we seek to provide insights into the approaches different
LLMs take to moral dilemmas, how these approaches may change over time, and the poten-
tial implications for AI system deployment in critical decision-making roles, particularly in
autonomous driving. This study will contribute to a more nuanced understanding of AI out-
puts in high-stakes scenarios, informing the development and deployment of AI systems in
complex, real-world contexts.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
2/ 20

--- Page 3 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
Materials and methods
Moral machine scenario generation
To comprehensively evaluate how different LLMs approach moral decision-making in
autonomous driving scenarios and assess the effects of model updates on these judgments,
we generated a systematic set of test scenarios following our previous methodology. These
scenarios presented dilemmas involving an autonomous vehicle facing an unavoidable acci-
dent, requiring a choice between two outcomes (“Case 1” and “Case 2”) with varying ethical
implications.
The scenarios were designed through a process of constrained randomization, exploring
six primary dimensions: species (humans vs. pets), social value (higher vs. lower perceived
social status), gender (female vs. male), age (younger vs. older), fitness (physically favored
vs. less fit individuals), and utilitarianism (smaller vs. larger group). Additionally, three sec-
ondary dimensions were incorporated: interventionism (swerving vs. continuing straight),
relationship to the autonomous vehicle (passengers vs. pedestrians), and legal considerations
(e.g., adherence to traffic signals). The scenarios were carefully constructed to balance com-
plexity and clarity, ensuring that they effectively probed the ethical reasoning capabilities of
the LLMs under study.
Large language models
To investigate how moral judgment patterns vary across different model architectures and
evolve through updates, we expanded upon our previous study [34] by incorporating a com-
prehensive set of LLMs, including the latest versions available. Our analysis encompasses
both base language models and models specifically optimized for dialogue interactions. While
these models may differ in their training approaches, they share fundamental capabilities in
processing and responding to complex queries, including moral scenarios. These LLMs were
utilized to generate responses to moral machine scenarios.
We initially incorporated the results from [34], which included responses from three pro-
prietary models: GPT-3.5 (gpt-3.5-turbo-0613), GPT-4 (gpt-4-0613), and PaLM 2, as well as
one open source model: Llama 2 (7B). Additional models were selected based on their promi-
nence in the field, technological advancements, and public recognition. This selection aimed
to provide a representative sample of current LLM technology while exploring variations in
ethical reasoning across different model types.
Among the proprietary models, we evaluated multiple versions of OpenAI models, includ-
ing the snapshot versions of GPT-3.5 [5] and GPT-4 [6] from March 2023 to April 2024, as
well as the newer GPT-4o models [39] (May and August 2024 versions), GPT-4o-mini, o1 and
o1-mini [40]. Google DeepMind’s Gemini models were also assessed, including Gemini 1.0
Pro [36] and multiple snapshot versions of Gemini 1.5 Pro and Gemini 1.5 Flash [41]. From
Anthropic, we evaluated the latest versions of their Claude models, including Claude 3 Haiku,
Sonnet, Opus [35], and Claude 3.5 Sonnet [42].
In the open-source domain, we included Meta’s Llama family [37], comprising Llama 3
and Llama 3.1 in 8B and 70B versions, Llama 3.2 in 1B and 3B versions, and Llama 3.3 in
70B version. A comprehensive evaluation of Google’s Gemma model family [38,43] was
conducted, encompassing multiple versions and scales from 2B-it to 27B-it, including the
derivative DataGemma RIG 27B-it model [44]. Additional open-source models evaluated
in this study included Large Model Systems Organization’s Vicuna v1.5 (7B and 13B) [45],
Mistral (7B Instruct v0.2) [46], Mistral-NeMo [47], CohereForAI’s Command R+ [48], and
Microsoft’s Phi-3.5 [49] (both MoE-instruct and mini-instruct versions).
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
3/ 20

--- Page 4 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
For a comprehensive list of all models and their specific versions used in this study, please
refer to our GitHub repository (https://github.com/kztakemoto/mmllm).
All models were used with their default parameter settings. The input prompts were con-
sistent with those used in [34], requiring each model to select either “Case 1” or “Case 2”
for each scenario. The complete code for prompt generation, analysis, and resulting data is
available in our GitHub repository.
While most models were evaluated using 50,000 scenarios, following our previous study
[34], constraints related to application programming interface (API) usage costs and compu-
tational time necessitated the use of fewer scenarios for certain models. The majority of the
models were assessed using the full set of 50,000 scenarios. However, a substantial group of
models, including the GPT-4 and GPT-4o series, Claude 3 Opus and Claude 3.5 family, all
Gemini family, Llama 3 and subsequent versions, OpenAI o1 mini, Mistral-NeMo, Gemma-
2 family, DataGemma, Command R+, and Phi-3.5 family, were evaluated using a reduced set
of 10,000 scenarios. The OpenAI o1 model, facing even more significant API cost limitations,
was evaluated using a further reduced set of 5,000 scenarios.
Data analysis
To systematically evaluate how different LLMs align with human moral preferences and
how this alignment changes across model versions and architectures, we analyzed the LLM
responses using the conjoint analysis framework as described in [50] and implemented in
the original study [11] on the Moral Machine experiment and our previous study [34]. This
approach allows for a robust, non-parametric identification of causal effects without specific
modeling assumptions.
The analysis process involved pre-processing LLM responses and dummy variable coding
for scenario attributes, which correspond to the primary and secondary dimensions described
in the scenario generation. We then calculated the Average Marginal Component Effect
(AMCE) for each attribute. The AMCE quantifies an attribute’s influence on the LLM’s ethical
decisions, enabling systematic comparison of moral preferences across different LLM models
and versions.
To compare the moral preference patterns between LLMs and humans, we performed
comparative analyses using the calculated AMCE values across all nine attributes. The human
preference data were obtained from the original Moral Machine experiment [11]. We quan-
tified the alignment between LLM and human preferences by computing the Euclidean dis-
tances between their respective AMCE values. Furthermore, to better understand the rela-
tionship patterns among different models and human preferences, we employed principal
component analysis (PCA) followed by cluster analysis on the AMCE values.
All statistical analyses, including AMCE calculations, distance measurements, PCA, and
subsequent analyses were performed using R statistical software (version 4.4.1).
Results
Moral judgments of large language models
Moral judgments of large language models To comprehensively evaluate how different LLMs
approach moral decision-making in autonomous driving scenarios, we conducted a system-
atic analysis of their responses across multiple ethical dimensions. Our analysis framework
focused on quantifying and comparing the moral preferences of various LLM families with
human judgments.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
4/ 20

--- Page 5 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
Fig 1 presents radar charts characterizing the moral judgment tendencies of various LLMs
across nine preferences quantified by Average Marginal Component Effect (AMCE) values
(see S1 Table for exact numerical data). These charts enable direct comparison of preferences
across multiple versions and model sizes of major LLM families, including GPT-3.5, GPT-
4, GPT-4o/o1, Claude, Gemini, Llama, Gemma, and other LLMs, against established human
preferences (see S1 Fig for detailed differences between each model and human values).
Our initial analysis revealed three key patterns in LLM moral judgments. First, many
LLMs demonstrated strong alignment with human preferences in fundamental moral deci-
sions, showing large positive values (>0.5) for No. Characters and Species dimensions. This
indicates consistent tendencies in prioritizing the preservation of more lives and favoring
humans over animals, suggesting that LLMs can capture basic human moral intuitions. Sec-
ond, we observed significant variations in judgment patterns across different model families,
with some models exhibiting inverse priorities compared to human preferences. Third, cer-
tain models showed disproportionately strong preferences in the same direction as humans
(differences in AMCE values approximately >0.3 compared to human values), indicating
potential overemphasis of specific moral principles.
These patterns provide important insights into both the capabilities and limitations of
LLMs in moral reasoning tasks. Below, we elaborate on these findings for each model family,
examining how different architectures influence moral judgments, and analyzing the effects of
model updates on alignment with human preferences.
GPT-3.5 family. Analysis of the GPT-3.5 family (Fig 1A) revealed significant temporal
evolution in moral judgments across model updates. While models from June 2023 to Jan-
uary 2024 exhibited similar patterns, the March 2023 version showed distinctive tendencies,
particularly in several key ethical dimensions.
In the Law dimension, the March version showed strong positive values favoring law-
abiding individuals (AMCE = 0.7), but subsequent versions shifted toward more neutral judg-
ments (AMCE ≈0). Similar temporal changes were observed in Gender-related judgments,
where initial strong female preference (AMCE = 0.5 in March 2023) gradually reduced toward
human judgment levels (AMCE = 0.2 in January 2024, human AMCE = 0.1). Fitness-related
judgments also evolved from initially contradicting human preferences (AMCE = –0.2 in
March 2023) to showing better alignment in later versions (AMCE = 0.1 in January 2024).
However, we observed persistent deviations from human preferences in certain dimen-
sions. The latest versions maintained near-neutral age-related judgments (AMCE ≈0) despite
human preference for younger individuals (AMCE = 0.5), and showed consistently stronger
preferences for pedestrians over passengers (AMCE = 0.6 vs. human 0.1). Species-related
judgments demonstrated an interesting pattern where initial alignment with human values in
earlier versions (AMCE = 0.7) weakened in later updates (AMCE = 0.2) while maintaining the
same directional preference.
GPT-4 family. Analysis of the GPT-4 family (Fig 1B) revealed remarkable consistency
in moral judgments across different versions from March 2023 to January 2024. In contrast
to GPT-3.5, model updates showed minimal impact on judgment patterns, with all versions
maintaining similar preference strengths across ethical dimensions.
The GPT-4 family demonstrated strong alignment with human judgments in direction but
often exceeded human preference magnitudes. Most notably, Species and No. Characters pref-
erences showed near-deterministic values (AMCE >0.9) compared to human values (AMCE =
0.6), indicating substantially stronger preferences for saving humans over animals and larger
groups over smaller ones. Similar amplification appeared in Gender (AMCE = 0.4 vs. human
0.1), Law (AMCE = 0.6 vs. human 0.3), and Relation to AV (AMCE = 0.5 vs. human 0.1)
categories.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
5/ 20

--- Page 6 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
Fig 1. Radar plots of moral preferences across different LLM families. AMCE values indicate preferences: Species (+: humans, –: pets), social value (+: high
status, –: low status), relation to AV (+: pedestrians, -: passengers), number (+: more, –: fewer), law (+: lawful, –: unlawful), intervention (+: inaction, –: action),
gender (+: female, –: male), fitness (+: fit, –: unfit/obese), age (+: young, –: elderly). Gray-filled areas represent human preferences. Each subplot represents a
different model family: (A) GPT-3.5, (B) GPT-4, (C) GPT-4o/o1, (D) Claude, (E) Gemini, (F) Llama, (G) Gemma, and (H) other models.
https://doi.org/10.1371/journal.pone.0322776.g001
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
6/ 20

--- Page 7 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
The only notable divergence appeared in the Fitness category, where GPT-4 models
showed a slight preference for overweight individuals (AMCE = –0.1) contrary to human
preference for physically fit individuals (AMCE = 0.2). This deviation, however, was minimal
compared to the strong alignment observed in other dimensions.
GPT-4o/o1 family. Analysis of the GPT-4o family (Fig 1C) revealed a pattern of consis-
tent moral judgments across models, with two notable exceptions: GPT-4o-mini and o1-mini
showed distinctive characteristics. The family exhibited closest alignment with human pref-
erences in Gender (AMCE = 0.1) and No. Characters (AMCE = 0.7) categories, matching
human values within ±0.1 AMCE.
Most GPT-4o models showed stronger ethical preferences than both humans and the GPT-
4 family in several dimensions. In Relation to AV, all models except GPT-4o-mini demon-
strated extreme pedestrian preference (AMCE >0.5 vs. human 0.1). Similarly, they showed
amplified preferences for law-abiding individuals (AMCE = 0.8 vs. human 0.4) and humans
over pets (AMCE = 0.9 vs. human 0.6). However, these models showed weaker age-related
preferences (AMCE = 0.2 vs. human 0.5) and maintained slight preferences for overweight
individuals in Fitness judgments (AMCE = –0.1).
The o1 variants showed interesting divergences: while the standard o1 followed GPT-4o
patterns, o1-mini demonstrated unique characteristics, including near-neutral Relation to
AV preferences (AMCE = 0.1) but extremely strong preferences for larger groups (AMCE ≈
1.0). This suggests that model size significantly influences moral judgment patterns within
this family.
Claude family. Analysis of the Claude family (Fig 1D) revealed a clear bifurcation in
moral judgment patterns, forming two distinct groups with contrasting ethical preferences.
The first group (Claude 3 Sonnet, Opus, and 3.5 Haiku) and second group (Claude 3 Haiku
and Claude 3.5 Sonnet) showed markedly different alignment with human preferences.
The first group demonstrated significant divergence from human judgments in several
dimensions. They showed inverse preferences in Relation to AV (AMCE = –0.4), Fitness
(AMCE ≈–0.5), and Social Status (AMCE = –0.3) categories, contrasting with human val-
ues (AMCE = 0.1, 0.2, and 0.3 respectively). While they aligned with humans in Gender
and Species preferences, their magnitude was notably stronger in both dimensions (Gender:
AMCE = 0.7 vs. human 0.3; Species: AMCE = 0.9 vs. human 0.6).
The second group showed different patterns: Claude 3 Haiku and Claude 3.5 Sonnet exhib-
ited excessive preferences in Relation to AV (AMCE = 0.5) and Law (AMCE = 0.7) categories
compared to humans (AMCE = 0.1 and 0.4, respectively). Claude 3.5 Sonnet particularly
showed strong preferences in Species and No. Characters dimensions (AMCE >0.8).
Model updates showed inconsistent effects: while the Sonnet 3 to 3.5 update improved
human alignment, the Haiku 3 to 3.5 update increased divergence. Subsequent updates within
Claude 3.5 Sonnet showed minimal changes in judgment patterns.
Gemini family. Analysis of the Gemini family (Fig 1E) revealed significant evolution in
moral judgments across model updates, particularly marked by changes in the Relation to AV
dimension. We observed a clear transition from Gemini 1.0 Pro to the 1.5 series, with distinct
changes in ethical preferences.
The most notable shift occurred in the Relation to AV category, where Gemini 1.0 Pro
initially showed preference for passengers (AMCE = –0.4), while the Gemini 1.5 Pro series
shifted to strongly favor pedestrians (AMCE = 0.7 vs. human 0.1). The Gemini 1.5 Flash fam-
ily showed a similar evolution: Flash Preview and 001 favored passengers (AMCE = –0.7), but
Flash 002 shifted to strong pedestrian preference (AMCE = 0.7).
Gender and Species preferences also showed distinctive patterns. Only Gemini 1.5 Pro 002
aligned closely with human gender preferences (AMCE = 0.2 vs. human 0.1), while earlier
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
7/ 20

--- Page 8 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
versions showed stronger female preference (AMCE >0.4). All versions showed strong pref-
erences than humans for prioritizing humans over pets (AMCE >0.7) and consistently showed
inverse fitness-related preferences (AMCE = –0.3 vs. human 0.2).
Notably, compared to Google’s previous PaLM 2 model, which contradicted human prefer-
ences in group size decisions (AMCE = –0.3 vs. human 0.7), all Gemini versions maintained
consistent alignment with human preferences in preserving larger groups (AMCE = 0.4–0.8).
Llama family. Analysis of the Llama family (Fig 1F) revealed that model size significantly
influenced moral judgment patterns, with larger models showing more consistent alignment
with human preferences. Most models demonstrated human-like preferences in the No. Char-
acters category (AMCE = 0.2–0.9), with Llama 3.1 8B being the notable exception (AMCE
= –0.3).
Ethical preferences varied substantially across different model sizes and versions. In
gender-related decisions, smaller models (Llama 2 7B, 3.2 1B, 3.2 3B) showed male pref-
erence (AMCE <–0.1) contrary to human judgments (AMCE = 0.1), while larger models
aligned with human preferences. Species-based decisions showed similar size-dependent pat-
terns: 70B models (Llama 3, 3.1, and 3.3) demonstrated close alignment with human judg-
ments (AMCE = 0.5–0.6), while smaller models (e.g., Llama 3.2 1B and 3B) showed inverse
preferences (AMCE <–0.1).
The 70B models showed relatively small variations in judgments between versions and
demonstrated closer alignment with human preferences. For example, these models main-
tained consistent preferences in law compliance (AMCE = 0.5) which happened to align with
human values (0.4), while other models, excluding 3 8B model, exhibited neutral preferences.
This observation suggests that model size may influence the consistency of judgment patterns.
Gemma family. Analysis of the Gemma family (Fig 1G) revealed a mix of consistent pat-
terns and model-dependent variations in moral judgments. Across all model variations, we
observed consistent trends in law compliance (AMCE ≈0) and Relation to AV preferences
(AMCE <0), with the latter diverging from human judgments (human AMCE = 0.1).
Judgment patterns varied significantly across different model sizes and versions. In the No.
Characters category, smaller Gemma 2 models (2B, 9B) showed inverse preferences (AMCE
= –0.4) compared to human values (AMCE = 0.7), while larger models aligned with human
preferences. The Species category showed similar variation: the Gemma 2 series demonstrated
human-aligned preferences (AMCE = 0.6), while other versions showed weak or neutral
species preferences (AMCE <0). Social Status preferences varied notably, with only Gemma
7B and 1.1 7B matching human preferences (AMCE = 0.3), while other versions showed
neutral or inverse preferences.
The variation in judgment patterns across different model sizes suggests that parameter
count significantly influences moral reasoning capabilities, although this relationship appears
more complex than in other model families.
Other large language models. Analysis of other LLMs (Fig 1H) revealed distinct patterns
of alignment and divergence from human moral preferences, with notable variations across
model architectures. In the Gender category, most models except Vicuna showed substantially
stronger female preference (AMCE >0.4) compared to human values (AMCE = 0.1).
Key differences emerged in utilitarian judgments: while Mistral and Command R+ aligned
with humans in favoring larger groups, their preferences were markedly stronger (AMCE =
0.9 vs. human 0.6). Characteristic divergences appeared in the Relation to AV and Fitness cat-
egories, where most models except Vicuna 13B showed inverse preferences (Relation to AV:
AMCE <0 vs. human 0.1; Fitness: AMCE <0 vs. human 0.2).
Vicuna models demonstrated unique patterns. While Vicuna 7B showed neutral judg-
ments (AMCE ≈0) across multiple categories (Gender, Age, Species), Vicuna 13B exhibited
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
8/ 20

--- Page 9 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
distinctive preferences contrary to humans (Gender: AMCE = –0.2 vs. human 0.1; Species:
AMCE = –0.2 vs. human 0.6). Similarly, Phi 3.5 models showed size-dependent variations,
with the mini version demonstrating notably different preferences than the MoE version.
These results suggest potential influences of model size on ethical judgments.
Quantitative comparison with human moral judgments
To quantitatively evaluate the similarity between LLM and human moral judgments, we com-
pared the Euclidean distances of AMCE values across nine categories for each model fam-
ily (Fig 2; see S2 Table for exact numerical data). This analysis revealed differences between
model families and changes in judgment distances from humans through model evolution.
Proprietary models generally showed closer alignment with human judgments than open-
source alternatives. The GPT-4 family achieved the closest alignment (minimum distance
= 0.6 with January 2024 version), followed by GPT-3.5 (distance = 0.8–0.9). However, the
newer GPT-4o/o1 family showed slightly increased distances (0.9–1.0), with o1-mini being an
exception (distance = 0.7).
Model updates showed varying effects across different families. In the Claude family, while
Claude 3 Haiku and Claude 3.5 Sonnet demonstrated relatively close alignment with human
judgments (distances = 0.9–1.0), Claude 3 Sonnet and Opus showed notably larger distances
(1.2). The Gemini family similarly exhibited significant version-dependent variations, with
Gemini 1.5 Preview (April 2024) showing the minimum distance of 0.9, while subsequent ver-
sions sometimes demonstrated larger distances of 1.1. Additionally, 1.5 Flash models showed
greater distances compared to 1.5 Pro models.
Open-source model performance strongly correlated with model size. The Llama fam-
ily showed clear size-dependent improvement, with 70B models achieving closer alignment
(distance = 0.7–0.8) compared to smaller 1–8B models (distances = 1.2–1.6). Conversely,
Fig 2. Distances between LLMs and human moral judgments across model families. Violin plots show the dis-
tribution of distances from human judgments for each model family, with individual models represented as points.
Different colors indicate different model families. Model names are labeled.
https://doi.org/10.1371/journal.pone.0322776.g002
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
9/ 20

--- Page 10 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
recent Gemma 2 models showed larger distances (2B/9B: distance = 2.0) despite being newer,
though performance improved with size. Among other LLMs, Mistral-Nemo and Command
R+ showed relatively good alignment (distances = 0.8–0.9), while Vicuna and Phi 3.5 demon-
strated larger divergence (distances = 1.0–1.6).
Factors influencing judgment distance
Proprietary vs. open-source models. To identify factors influencing the distance from
human judgments, we first investigated whether the proprietary or open-source nature of
models influenced their alignment with human moral judgments. This analysis was motivated
by previous research suggesting general performance advantages of proprietary models over
open-source alternatives [51].
Our analysis classified models into three distinct groups (Fig 3): proprietary mod-
els (e.g., GPT-4, Claude, Gemini), general open-source models, and large open-source
models (>10B parameters). Statistical comparison revealed significant differences
between proprietary and general open-source models, with proprietary models show-
ing closer alignment to human judgments (median distance: 0.9 vs. 1.2, Wilcoxon test
p = 0.011).
However, when comparing proprietary models with large open-source models specifi-
cally, this difference disappeared. Large open-source models (>10B parameters) achieved
similar alignment with human judgments (median distance = 0.9) as proprietary models,
showing no statistically significant difference (Wilcoxon test p = 0.92). Notably, models
like Llama-70B achieved distances (0.7–0.8) comparable to or better than some proprietary
models.
Fig 3. Comparison of moral judgment distances between proprietary and open-source models. Violin plots
with embedded box plots compare the distribution of distances from human judgments across three model cate-
gories: proprietary models, all open-source models, and large open-source models with parameters exceeding 10B.
Individual models are represented as points.
https://doi.org/10.1371/journal.pone.0322776.g003
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
10/ 20

--- Page 11 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
These findings suggest that model size, rather than the proprietary/open-source distinc-
tion, is the primary factor influencing alignment with human moral judgments. This obser-
vation has important implications for the development of ethical AI systems, suggesting that
large open-source models can potentially match the moral reasoning capabilities of propri-
etary alternatives.
Impact of model size. We analyzed the relationship between model size and alignment
with human moral judgments, focusing on open-source models where parameter counts
are publicly available (Fig 4). Statistical analysis revealed a significant negative correlation
between model size and distance from human judgments (Spearman’s rank correlation coef-
ficient 𝜌= –0.54, p = 0.0076), though this relationship showed notable complexities.
The Llama family demonstrated the clearest size-dependent improvements in alignment.
Large (70B) models achieved substantially better alignment (distance = 0.7–0.8) compared
to smaller models (1-3B parameters, distances = 1.2–1.5). A similar pattern emerged in the
Gemma family, where the 27B model showed improved alignment (distance = 1.1) compared
to smaller 2–9B models (distances = 1.2–1.9). These improvements suggest that increased
model capacity enables more nuanced moral judgments.
However, the relationship between size and alignment showed important nuances within
model families. Within the Llama family, the 3.2 series showed unexpected variation, with
the 1B model achieving better alignment (distance = 1.2) than the larger 3B model (distance
= 1.5). Similar inconsistencies appeared among 8B models, where version 3 demonstrated
notably better alignment (distance = 0.8) than the subsequent version 3.1 (distance = 1.6). The
Gemma family showed analogous patterns, with some larger models demonstrating increased
distances despite their greater parameter counts.
These variations suggest that while model size significantly influences moral judgment
alignment, other factors such as architecture design and training methodology play crucial
Fig 4. Relationship between model size and distance from human judgments in open-source models. Different
model families are represented by different colors. Model names are labeled. Horizontal axis (model size in billion
parameters) are represented in logarithmic scale.
https://doi.org/10.1371/journal.pone.0322776.g004
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
11/ 20

--- Page 12 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
roles. The moderate correlation coefficient (𝜌= –0.54) quantitatively supports this observa-
tion.
While proprietary models were excluded from this analysis due to undisclosed parame-
ter counts, their generally strong alignment with human judgments (median distance = 0.9)
is consistent with the observed trend that larger models tend to demonstrate better alignment
with human moral preferences.
Impact of model updates. Analysis of model updates revealed that newer versions did
not consistently improve alignment with human moral judgments, suggesting a complex rela-
tionship between model evolution and ethical reasoning capabilities. We examined this rela-
tionship across both open-source and proprietary model families, finding significant varia-
tions in the impact of updates.
In open-source models, updates often showed unpredictable effects on moral judgment
alignment. Within the Gemma family, successive updates led to increasing divergence from
human judgments: the 2B model showed progressive increase in distances (Gemma 2B: 1.1,
Gemma 1.1 2B: 1.2, Gemma 2 2B: 2.0). The Llama family exhibited mixed effects: in 7-8B
models, while the update from Llama 2 to 3 improved alignment (distance decreased from
1.1 to 0.8), the subsequent update to 3.1 significantly increased divergence (distance = 1.6). In
the 70B series, while Llama 3 and 3.1 maintained strong alignment (distance = 0.7), the sub-
sequent Llama 3.3 showed a slight increase in divergence (distance = 0.8). These results indi-
cate that even for larger models, updates do not consistently improve alignment with human
moral preferences.
Proprietary models showed more stable but still variable patterns across updates (Fig 5).
The GPT-4 family maintained relatively consistent alignment (distances = 0.7–0.8) from
March 2023 to January 2024, with the January version achieving the best alignment (dis-
tance: 0.6) before slightly increasing in April (distance: 0.8). GPT-3.5 showed similar stability
(distances = 0.7–0.9), while the newer GPT-4o family demonstrated slightly larger distances
(0.9–1.0) compared to traditional GPT-4.
Fig 5. Temporal changes in distance from human judgments across proprietary model families. Different model
families are represented by different colors. Model names are labeled.
https://doi.org/10.1371/journal.pone.0322776.g005
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
12/ 20

--- Page 13 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
The Claude and Gemini families exhibited more pronounced update effects. Claude Son-
net’s update from 3 to 3.5 improved alignment (distance decreased from 1.2 to 0.9), but the
October 2024 update slightly increased divergence (distance: 1.0). The Gemini family main-
tained relatively stable alignment through version 1.5 Pro Preview (distance: 0.9), but later
versions showed increased distances (1.1), with Flash models consistently showing larger
divergence than Pro models.
These patterns suggest that model updates, while often aimed at improving general capa-
bilities, do not guarantee better alignment with human moral preferences. This observation
raises important questions about the relationship between general model improvements and
ethical reasoning capabilities.
Comprehensive analysis of moral judgments
To synthesize our findings and visualize the overall landscape of moral judgment pat-
terns, we conducted PCA using AMCE values across all nine ethical categories (Fig 6). This
Fig 6. Principal component analysis of LLM moral judgments compared to human preferences. The first two
principal components derived from AMCE values across nine moral preference categories. Different model families
are represented by different colors, and human judgment is marked with a black diamond.
https://doi.org/10.1371/journal.pone.0322776.g006
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
13/ 20

--- Page 14 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
analysis captured 74.2% of the total variance in the first two principal components (PC1:
46.1%, PC2: 28.1%), providing a comprehensive two-dimensional representation of moral
judgment similarities.
This analysis revealed several characteristic patterns. First, the GPT-4 family, GPT-4o/o1
family, Claude 3 Haiku, Claude 3.5 Sonnet, Gemini Pro 1.5 family, and GPT-3.5 family
formed clusters relatively close to human judgments. Notably, these models concentrated
in the positive region of the first principal component, suggesting commonalities in their
judgment patterns.
Conversely, Claude 3 Sonnet and Opus, along with Gemini 1.5 Flash Pre and Flash 001,
positioned in strongly negative regions of the first principal component, demonstrating judg-
ment patterns distinct from humans and other proprietary models. The Gemma 2 family (2B,
9B) showed large positive values in the second principal component, confirming distinctively
different judgment patterns from other models.
Interestingly, these results aligned with our previous distance analysis in multiple aspects.
Models showing smaller distances from human judgments tended to position closer to
humans in this two-dimensional plane. Similar trends were observed regarding model size
effects. For instance, within the Llama family, 70B models (Llama 3, 3.1, and 3.3) positioned
near humans, while smaller 1-8B models distributed farther away.
Changes due to model updates were also clearly observable in this two-dimensional plane.
For example, GPT-3.5 approached human positions most closely in the June 2023 version
but moved away with subsequent updates. Similarly, while Claude Sonnet moved closer to
humans with the update from 3 to 3.5, it slightly diverged with the October version of 3.5.
These trajectories support our previous finding that updates do not necessarily lead to closer
alignment with human judgments.
Discussion
In this study, we investigated two critical questions in AI ethics: how different LLM architec-
tures approach moral decision-making in autonomous driving contexts, and how these moral
judgments evolve through model updates. By expanding our analysis to 52 different LLMs
using the Moral Machine experimental framework (Figs 1 and 2), we revealed several key pat-
terns. Proprietary models and open-source models exceeding 10B parameters demonstrated
relatively small distances from human judgments (Figs 3 and 4), showing consistent align-
ment with human preferences in fundamental moral decisions, such as prioritizing humans
over animals and favoring the preservation of more lives. However, model updates did not
necessarily lead to closer alignment with human judgments, and variations in judgment ten-
dencies were observed across updates (Fig 5). This comprehensive analysis provides crucial
insights into both the current state and evolution of moral reasoning capabilities in large
language models.
Our analysis revealed a complex relationship between model characteristics and moral
judgment capabilities. While the incomplete alignment between LLM and human moral judg-
ments was expected, as these models are not explicitly trained for moral reasoning, we identi-
fied several significant patterns that inform our understanding of how different architectures
approach ethical decision-making.
A key finding was the significant negative correlation between model size and distance
from human judgments in open-source models (Fig 4). This relationship aligns with general
scaling laws in language model behavior, suggesting that increased model capacity might nat-
urally lead to more human-like moral reasoning. However, our cross-version analysis revealed
that this relationship is not straightforward: within the same model family, size increases did
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
14/ 20

--- Page 15 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
not always result in improved alignment with human judgments, indicating that factors such
as architecture design and training methodology play crucial roles.
These findings have important implications for the practical implementation of AI ethics
in autonomous driving systems. The GPT-4 family achieved the closest alignment with human
judgments (distances = 0.6–0.8), while among open-source alternatives, Llama 70B demon-
strated promising performance (distances = 0.7–0.8). However, real-world deployment faces
a crucial challenge: the trade-off between ethical reasoning quality and computational effi-
ciency. Smaller models, which are more practical for real-time decision-making, showed
notably larger divergence from human judgments (distances = 1.2–1.5). This creates a sig-
nificant challenge for implementing ethical AI in autonomous systems where both moral
reliability and operational efficiency are essential.
Among these implementation challenges, the computational efficiency requirements are
particularly critical in autonomous driving, where decisions must be made in milliseconds.
While our study demonstrates that larger models generally make better ethical decisions, their
computational requirements make them impractical for real-time deployment. This chal-
lenge necessitates innovative approaches such as model distillation [52] or specialized ethical
reasoning modules that can maintain high-quality moral judgment while meeting the strict
latency requirements of autonomous systems.
The identified trade-off between model size and ethical reasoning quality thus presents
fundamental challenges for practical implementation. While recent research has produced
LLMs specifically fine-tuned for autonomous driving tasks [18], these efforts have primar-
ily focused on technical capabilities (perception, control, navigation) rather than ethical rea-
soning. Our findings suggest that developing practically viable AI systems requires address-
ing three key challenges: optimizing smaller models for better ethical reasoning, managing
excessive ethical preferences, and maintaining cultural adaptability.
The tendency of LLMs to exhibit exaggerated ethical preferences represents a particular
concern. Our analysis showed that while models often directionally aligned with human pref-
erences (e.g., prioritizing humans over pets, pedestrians over passengers), they frequently
demonstrated substantially stronger preferences than humans. While such strong safety pref-
erences partially align with established guidelines, as exemplified by the German Ethics Code
on Automated and Connected Driving [53], their excessive nature could lead to subopti-
mal decision-making in complex real-world scenarios. Specifically, while Guidelines 5 and
7 emphasize protecting vulnerable road users and preventing personal injury, the observed
extreme preferences in LLMs suggest a need for more nuanced ethical calibration.
Our analysis revealed particularly significant findings regarding utilitarian decision-
making in LLMs. The models showed extreme emphasis on maximizing lives saved, reflecting
a strong utilitarian bias that exceeds typical human preferences. This bias likely stems from
the predominance of Western individualistic and utilitarian values in training data [11,54],
raising important questions about cultural representation in AI ethics. This observation
becomes especially significant when considered against formal ethical frameworks like the
German Ethics Code, whose Guideline 2 explicitly warns against purely utilitarian approaches
in autonomous vehicle decision-making.
The analysis also uncovered complex patterns in how LLMs handle social biases and pro-
tective principles. We observed inverse patterns to human judgments in cases involving phys-
ical fitness and social status, where LLMs showed stronger preferences for protecting poten-
tially vulnerable groups. Similarly, while LLMs aligned with human tendencies in gender-
related decisions and legal compliance, they demonstrated significantly amplified preferences.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
15/ 20

--- Page 16 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
These patterns suggest that LLMs may be extracting and amplifying certain ethical princi-
ples from their training data, such as historical protective principles (e.g., ‘Women and Chil-
dren First” principle [55]) and fundamental concepts of justice [56], but applying them with
excessive rigidity.
Our findings highlight fundamental challenges for implementing ethical AI in autonomous
driving systems. A critical issue emerged from the contrast between human moral flexibil-
ity and the rigid, often amplified moral preferences displayed by LLMs. This rigidity becomes
particularly problematic when considered alongside recent findings [57] demonstrating that
LLMs exhibit varying moral biases across different languages, suggesting inconsistent ethical
reasoning even within individual models.
These observations raise two critical concerns for practical implementation. First, the
potential for AI systems to influence human decision-making [31] means that LLMs’ ampli-
fied moral preferences could disproportionately shape social attitudes toward ethical decisions
in autonomous driving. Second, the observed variation in moral judgments across languages
and cultures challenges the goal of developing globally deployable autonomous systems. These
issues are particularly significant when considered alongside established ethical guidelines.
For instance, the German Ethics Code’s Guideline 9 emphasizes equal treatment regardless of
demographic factors, but this principle appears challenging to implement given the observed
biases in LLM decision-making.
Another critical consideration for practical deployment is the need for transparency and
explainability in LLMs’ ethical decision-making processes. While our study quantifies the
alignment between LLM and human moral preferences, the black-box nature of these models
poses significant challenges for real-world implementation, particularly in life-critical deci-
sions. Unlike rule-based systems, LLMs’ ethical judgments emerge from complex neural net-
work interactions, making them difficult to interpret or verify. This lack of transparency is
particularly problematic in autonomous driving scenarios where stakeholders need to under-
stand and trust the basis for ethical decisions [30].
Our findings raise significant concerns about the cultural adaptability of AI ethics in
autonomous systems. The observed tendency of LLMs to reflect predominantly Western val-
ues and apply ethical principles in extreme ways could significantly impact the global accep-
tance of autonomous driving systems. This challenge is compounded by our observation that
LLMs’ moral judgments can diverge substantially from human preferences across different
cultural and linguistic contexts, suggesting a need for more culturally adaptive approaches to
ethical AI implementation.
These cultural adaptability challenges point to specific implementation considerations for
autonomous driving systems. Regions with distinct driving cultures and ethical priorities
may require different thresholds for risk assessment and decision-making parameters. This
is particularly crucial in areas where different cultural zones intersect, such as international
borders or multicultural urban centers, where autonomous vehicles must navigate varying
expectations of driving behavior while maintaining consistent safety standards.
A key limitation of our study stems from our use of globally aggregated moral preferences
as the benchmark for human judgments. Moral decisions, particularly those involving life-
and-death choices, are deeply influenced by cultural and social contexts. For example, the
strong utilitarian preferences we observed in LLMs might align with some cultural perspec-
tives while conflicting with others. While our analysis demonstrates clear patterns in LLM
moral reasoning, it does not fully capture the nuanced variations in human moral preferences
across different cultural contexts.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
16/ 20

--- Page 17 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
Our methodology, based on the Moral Machine experiment framework, carries inherent
limitations that affect the interpretation of our findings. While this framework enabled sys-
tematic comparison across models, it simplifies the complexity of real-world ethical decisions
through binary choices and trolley-type dilemmas. As noted in [34], this approach cannot
capture nuanced factors such as road users’ intentions or evaluate everyday moral decisions
in low-risk traffic situations. Recent work has proposed more ecologically valid approaches,
such as combining virtual reality-based traffic scenarios with psychological frameworks like
the Agent-Deed-Consequences model [58].
The emergence of multimodal large language models (MLLMs) offers potential pathways
for addressing these methodological limitations. Recent research has demonstrated MLLMs’
capability to integrate visual information with language understanding in autonomous driving
contexts [19,20], suggesting possibilities for more comprehensive ethical evaluation frame-
works. Unlike the text-based scenarios used in our study, MLLMs could enable assessment
of ethical decision-making in more realistic, visually-rendered traffic scenarios, potentially
offering deeper insights into AI moral reasoning in real-world contexts.
Despite these limitations, our comprehensive analysis of 52 different LLMs provides three
key contributions to understanding AI ethics in autonomous systems. First, we established
a clear relationship between model size and ethical judgment capabilities, offering insights
for future model development. Second, our systematic characterization of judgment patterns
across model families revealed both consistent trends and concerning biases in AI moral rea-
soning. Third, we identified specific implementation challenges that must be addressed for
practical deployment of ethical AI in autonomous vehicles. These findings, combined with
our assessment of current methodological constraints, provide crucial guidance for both the
technical development and ethical design of future autonomous driving systems.
Supporting information
S1 Fig. Differences in AMCE values between LLMs and human preferences. Heatmap
showing the differences between LLM and human AMCE values for nine moral preference
categories.
(PDF)
S1 Table. AMCE values for nine moral preference categories across all analyzed LLMs.
(CSV)
S2 Table. Comprehensive model information and evaluation metrics. Summary of all ana-
lyzed LLMs, including their characteristics and performance metrics. The ‘open-source’ col-
umn indicates model accessibility (yes/no), ‘Size’ shows the number of parameters in bil-
lions where available, ‘Date’ indicates the model version’s release date, ‘Distance’ shows the
Euclidean distance between the model’s and human AMCE values across nine moral prefer-
ence categories, and ‘valid response rate’ represents the proportion of valid responses in the
evaluation scenarios.
(CSV)
Author contributions
Conceptualization: Kazuhiro Takemoto.
Data curation: Muhammad Shahrul Zaim bin Ahmad, Kazuhiro Takemoto.
Formal analysis: Muhammad Shahrul Zaim bin Ahmad, Kazuhiro Takemoto.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
17/ 20

--- Page 18 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
Funding acquisition: Kazuhiro Takemoto.
Investigation: Muhammad Shahrul Zaim bin Ahmad, Kazuhiro Takemoto.
Methodology: Kazuhiro Takemoto.
Project administration: Kazuhiro Takemoto.
Resources: Kazuhiro Takemoto.
Software: Kazuhiro Takemoto.
Supervision: Kazuhiro Takemoto.
Validation: Muhammad Shahrul Zaim bin Ahmad, Kazuhiro Takemoto.
Visualization: Muhammad Shahrul Zaim bin Ahmad, Kazuhiro Takemoto.
Writing – original draft: Kazuhiro Takemoto.
Writing – review & editing: Muhammad Shahrul Zaim bin Ahmad, Kazuhiro Takemoto.
References
1.
Fraiwan M, Khasawneh N. A review of chatgpt applications in education, marketing, software
engineering, and healthcare: Benefits, drawbacks, and research directions. arXiv preprint. 2023.
https://doi.org/arXiv:230500237
2.
Sallam M. ChatGPT utility in healthcare education, research, and practice: Systematic review on the
promising perspectives and valid concerns. Healthcare (Basel). 2023;11(6):887.
https://doi.org/10.3390/healthcare11060887 PMID: 36981544
3.
Ray PP. ChatGPT: A comprehensive review on background, applications, key challenges, bias,
ethics, limitations and future scope. Internet Things Cyber-Phys Syst. 2023;3:121–54.
https://doi.org/10.1016/j.iotcps.2023.04.003
4.
Chowdhury AK, Sujon SR, Shafi MdSS, Ahmmad T, Ahmed S, Hasib KM, et al. Harnessing large
language models over transformer models for detecting Bengali depressive social media text: A
comprehensive study. Nat Lang Proc J. 2024;7:100075. https://doi.org/10.1016/j.nlp.2024.100075
5.
OpenAI. Introducing ChatGPT; 2022. OpenAI. Available from: https://openai.com/index/chatgpt/
6.
Achiam J, Adler S, Agarwal S, Ahmad L, Akkaya I, Aleman FL, et al. GPT-4 technical report. arXiv
preprint arXiv:230308774. 2023.
7.
Bostrom N, Yudkowsky E. The ethics of artificial intelligence. Artif Intell Saf Secur. 2018:57–69.
https://doi.org/10.1201/9781351251389-4
8.
Nath R, Sahu V. The problem of machine ethics in artificial intelligence. AI Soc. 2017;35(1):103–11.
https://doi.org/10.1007/s00146-017-0768-6
9.
Hagendorff T. The ethics of AI ethics: An evaluation of guidelines. Minds Mach. 2020;30(1):99–120.
https://doi.org/10.1007/s11023-020-09517-8
10.
Bonnefon J-F, Shariff A, Rahwan I. The social dilemma of autonomous vehicles. Science.
2016;352(6293):1573–6. https://doi.org/10.1126/science.aaf2654 PMID: 27339987
11.
Awad E, Dsouza S, Kim R, Schulz J, Henrich J, Shariff A, et al. The moral machine experiment.
Nature. 2018;563(7729):59–64. https://doi.org/10.1038/s41586-018-0637-6 PMID: 30356211
12.
Faulhaber AK, Dittmer A, Blind F, Wächter MA, Timm S, Sütfeld LR, et al. Human decisions in moral
dilemmas are largely described by utilitarianism: Virtual car driving study provides guidelines for
autonomous driving vehicles. Sci Eng Ethics. 2019;25(2):399–418.
https://doi.org/10.1007/s11948-018-0020-x PMID: 29357047
13.
Gill T. Ethical dilemmas are really important to potential adopters of autonomous vehicles. Ethics Inf
Technol. 2021;23(4):657–73. https://doi.org/10.1007/s10676-021-09605-y PMID: 34248401
14.
Chen H, Yuan K, Huang Y, Guo L, Wang Y, Chen J. Feedback is all you need: From ChatGPT to
autonomous driving. Sci China Inf Sci. 2023;66(6). https://doi.org/10.1007/s11432-023-3740-x
15.
Gao Y, Tong W, Wu EQ, Chen W, Zhu G, Wang F-Y. Chat with ChatGPT on interactive engines for
intelligent driving. IEEE Trans Intell Veh. 2023;8(3):2034–6.
https://doi.org/10.1109/tiv.2023.3252571
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
18/ 20

--- Page 19 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
16.
Du H, Teng S, Chen H, Ma J, Wang X, Gou C. Chat with chatgpt on intelligent vehicles: An IEEE
TIV perspective. IEEE Trans Intell Veh. 2023;8(3):2020–6.
17.
Lei L, Zhang H, Yang S. ChatGPT in connected and autonomous vehicles: Benefits and challenges.
Intell Robot. 2023;3(2):145–8.
18.
Yang Z, Jia X, Li H, Yan J. Llm4drive: A survey of large language models for autonomous driving.
arXiv e-prints. 2023:arXiv-2311.
19.
Cui C, Ma Y, Cao X, Ye W, Zhou Y, Liang K. A survey on multimodal large language models for
autonomous driving. Proceedings of the IEEE/CVF winter conference on applications of computer
vision; 2024. p. 958–79.
20.
Zhou X, Liu M, Yurtsever E, Zagar B, Zimmer W, Cao H. Vision language models in autonomous
driving: A survey and outlook. IEEE Trans Intell Veh. 2024.
21.
Dewitt B, Fischhoff B, Sahlin N-E. “Moral machine” experiment is no basis for policymaking. Nature.
2019;567(7746):31. https://doi.org/10.1038/d41586-019-00766-x PMID: 30837734
22.
Bigman YE, Gray K. Life and death decisions of autonomous vehicles. Nature.
2020;579(7797):E1–2. https://doi.org/10.1038/s41586-020-1987-4 PMID: 32132695
23.
Etienne H. The dark side of the ‘Moral Machine’ and the fallacy of computational ethical
decision-making for autonomous vehicles. Law Innov Technol. 2021;13(1):85–107.
https://doi.org/10.1080/17579961.2021.1898310
24.
Furey H, Hill S. MIT’s moral machine project is a psychological roadblock to self-driving cars. AI
Ethics. 2020;1(2):151–5. https://doi.org/10.1007/s43681-020-00018-z
25.
LaCroix T. Moral dilemmas for moral machines. AI Ethics. 2022;2(4):737–46.
https://doi.org/10.1007/s43681-022-00134-y
26.
Schuessler D. The probability problems of the Moral Machine Experiment. AI Ethics.
2023;4(2):501–10. https://doi.org/10.1007/s43681-023-00287-4
27.
Winfield AF, Michael K, Pitt J, Evers V. Machine ethics: The design and governance of ethical AI
and autonomous systems [scanning the issue]. Proc IEEE. 2019;107(3):509–17.
https://doi.org/10.1109/jproc.2019.2900622
28.
Etienne H. When AI ethics goes astray: A case study of autonomous vehicles. Soc Sci Comput Rev.
2020;40(1):236–46. https://doi.org/10.1177/0894439320906508
29.
Meyer-Waarden L, Cloarec J. “Baby, you can drive my car”: Psychological antecedents that drive
consumers’ adoption of AI-powered autonomous vehicles. Technovation. 2022;109:102348.
https://doi.org/10.1016/j.technovation.2021.102348
30.
Atakishiyev S, Salameh M, Yao H, Goebel R. Explainable artificial intelligence for autonomous
driving: A comprehensive overview and field guide for future research directions. IEEE Access.
2024.
31.
Krügel S, Ostermaier A, Uhl M. ChatGPT’s inconsistent moral advice influences users’ judgment.
Sci Rep. 2023;13(1):4569. https://doi.org/10.1038/s41598-023-31341-0 PMID: 37024502
32.
Jin Z, Levine S, Kleiman-Weiner M, Piatti G, Liu J, Adauto FG, et al. Multilingual trolley problems for
language models. arXiv preprint arXiv:240702273. 2024.
33.
Bruers S, Braeckman J. A review and systematization of the trolley problem. Philosophia.
2013;42(2):251–69. https://doi.org/10.1007/s11406-013-9507-5
34.
Takemoto K. The moral machine experiment on large language models. R Soc Open Sci.
2024;11(2):231393. https://doi.org/10.1098/rsos.231393 PMID: 38328569
35.
Anthropic A. Claude 3 model card. Claude 3 model family: Opus, sonnet, haiku. 2024;1:1.
36.
Team G, Anil R, Borgeaud S, Wu Y, Alayrac JB, Yu J, et al. Gemini: A family of highly capable
multimodal models. arXiv preprint arXiv:231211805. 2023.
37.
Dubey A, Jauhri A, Pandey A, Kadian A, Al-Dahle A, Letman A, et al. The llama 3 herd of models.
arXiv preprint arXiv:240721783. 2024.
38.
Team G, Mesnard T, Hardin C, Dadashi R, Bhupatiraju S, Pathak S, et al. Gemma: Open models
based on gemini research and technology. arXiv preprint arXiv:240308295. 2024.
39.
OpenAI. Hello GPT-4o; 2024. OpenAI. Available from: https://openai.com/index/hello-gpt-4o/
40.
OpenAI. Introducing OpenAI o1; 2024. OpenAI. Available from: https://openai.com/o1/
41.
Reid M, Savinov N, Teplyashin D, Lepikhin D, Lillicrap T, Alayrac Jb, et al. Gemini 1.5: Unlocking
multimodal understanding across millions of tokens of context. arXiv preprint arXiv:240305530.
2024.
42.
Anthropic A. Claude 3.5 sonnet model card addendum. Claude-35 Model Card. 2024.
43.
Team G, Riviere M, Pathak S, Sessa PG, Hardin C, Bhupatiraju S, et al. Gemma 2: Improving open
language models at a practical size. arXiv preprint arXiv:240800118. 2024.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
19/ 20

--- Page 20 ---\n\nPLOS One
Large-scale moral machine experiment on large language models
44.
Radhakrishnan P, Chen J, Xu B, Ramaswami P, Pho H, Olmos A, et al. Knowing when to
ask–bridging large language models and data. arXiv preprint arXiv:240913741. 2024.
45.
Chiang WL, Li Z, Lin Z, Sheng Y, Wu Z, Zhang H, et al. Vicuna: An open-source chatbot impressing
GPT-4 with 90%* ChatGPT quality; 2023. Available from: https://lmsys.org/blog/2023-03-30-vicuna/
46.
Jiang AQ, Sablayrolles A, Mensch A, Bamford C, Chaplot DS, Casas Ddl, et al. Mistral 7B. arXiv
preprint arXiv:231006825. 2023.
47.
MistralAIteam. Mistral NeMo; 2024. Mistral AI. Available from: https://mistral.ai/news/mistral-nemo/
48.
Gomez A. Introducing command R+: A scalable LLM built for business; 2024. The Cohere Blog.
Available from: https://cohere.com/blog/command-r-plus-microsoft-azure
49.
Abdin M, Jacobs SA, Awan AA, Aneja J, Awadallah A, Awadalla H, et al. Phi-3 technical report: A
highly capable language model locally on your phone. arXiv preprint arXiv:240414219. 2024.
50.
Hainmueller J, Hopkins DJ, Yamamoto T. Causal inference in conjoint analysis: Understanding
multidimensional choices via stated preference experiments. Polit Anal. 2014;22(1):1–30.
https://doi.org/10.1093/pan/mpt024
51.
Zhang G, Jin Q, Zhou Y, Wang S, Idnay B, Luo Y, et al. Closing the gap between open source and
commercial large language models for medical evidence summarization. NPJ Digit Med.
2024;7(1):239. https://doi.org/10.1038/s41746-024-01239-w PMID: 39251804
52.
Tang Y, Da Costa AAB, Zhang X, Patrick I, Khastgir S, Jennings P. Domain knowledge distillation
from large language model: An empirical study in the autonomous driving domain. 2023 IEEE 26th
international conference on intelligent transportation systems (ITSC); 2023. p. 3893–900.
https://doi.org/10.1109/itsc57777.2023.10422308
53.
Luetge C. The German ethics code for automated and connected driving. Philos Technol.
2017;30(4):547–58. https://doi.org/10.1007/s13347-017-0284-0
54.
Kagitcibasi C. Individualism and collectivism. Handbook of cross-cultural psychology. 1997;3:1–49.
55.
Annas GJ. Women and children first. N Engl J Med. 1995;333(24):1647–51.
https://doi.org/10.1056/NEJM199512143332420 PMID: 7477216
56.
Sandel MJ. Justice: What’s the right thing to do? Farrar, Straus and Giroux; 2010. Available from:
https://books.google.co.jp/books?id=BrdNDG7TTUEC
57.
Vida K, Damken F, Lauscher A. Decoding multilingual moral preferences: Unveiling LLM’s biases
through the moral machine experiment. AIES. 2024;7:1490–501.
https://doi.org/10.1609/aies.v7i1.31741
58.
Cecchini D, Brantley S, Dubljević V. Moral judgment in realistic traffic scenarios: Moving beyond the
trolley paradigm for ethics of autonomous vehicles. AI & SOCIETY; 2023. p. 1–12.
PLOS One https://doi.org/10.1371/journal.pone.0322776
May 21, 2025
20/ 20
\n```\n