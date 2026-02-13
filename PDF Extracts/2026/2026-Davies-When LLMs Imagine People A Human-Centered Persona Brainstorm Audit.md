---
title: "2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit - PDF Extract"
source_pdf: "2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit.pdf"
pages: 30
extracted_at: "2026-02-13T13:57:16.209844"
---

# PDF Extract: 2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit

**Source PDF:** 2026-Davies-When LLMs Imagine People A Human-Centered Persona Brainstorm Audit.pdf
**Total Pages:** 30

---

## Content

```
--- Page 1 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for
Bias and Fairness in Creative Applications
HONGLIU CAO, EOIN THOMAS, and RODRIGO ACUNA AGOST, Amadeus, France
Biased outputs from Large Language Models (LLMs) can reinforce stereotypes and perpetuate inequities in real-world applications,
making fairness auditing essential. We introduce the Persona Brainstorm Audit (PBA), a scalable and transparent auditing method
for detecting bias through open-ended persona generation. Unlike existing methods that rely on fixed identity categories and static
benchmarks, PBA uncovers biases across multiple social dimensions while supporting longitudinal tracking and mitigating data
leakage risks. Applying PBA to 12 state-of-the-art LLMs, we compare bias severity across models, dimensions, and versions, uncover
distinct patterns and lineage-specific variability, and trace how biases attenuate, persist, or resurface across successive generations.
Robustness analyses show PBA remains stable under varying sample sizes, role-playing prompts, and debiasing prompts, establishing
its reliability for fairness auditing in LLMs.
CCS Concepts: • Human-centered computing →Human computer interaction (HCI); Empirical studies in HCI; • Computing
methodologies →Natural language processing; • Social and professional topics →Computing / technology policy; User
characteristics.
Additional Key Words and Phrases: Large Language Models, Bias and Fairness, Human-Centered AI, Evaluation Metric, Responsible AI
ACM Reference Format:
Hongliu CAO, Eoin Thomas, and Rodrigo ACUNA AGOST . 2026. When LLMs Imagine People: A Human-Centered Persona Brainstorm
Audit for Bias and Fairness in Creative Applications. In Proceedings of Make sure to enter the correct conference title from your rights
confirmation email (Conference acronym ’XX). ACM, New York, NY, USA, 30 pages. https://doi.org/XXXXXXX.XXXXXXX
1
Introduction
CONTENT WARNING: This paper contains examples of stereotypes that may be offensive.
Large Language Models (LLMs) have advanced at an unprecedented pace, demonstrating remarkable capabilities in
conversational-fluency, instruction-following, in-context learning, and reasoning [2, 14, 66]. These breakthroughs have
driven widespread adoption across academia and industry, powering applications in information retrieval, customer
service, education, healthcare, and creative domains [6, 54]. Their integration signals not only technical progress but also
a profound shift in how knowledge work and creative practices are conducted [4, 17]. Recently, LLMs are increasingly
applied in creative workflows, supporting tasks such as brainstorming [25], design [43], creative writing [30], persona
generation [4, 60], and synthetic data generation [14]. These applications promise efficiency and diversity of ideas,
enabling designers and researchers to accelerate innovation.
However, these opportunities come with critical challenges. LLMs often exhibit incomplete or outdated knowledge,
hallucinations, and reliability issues [15]. The rapid integration of LLMs into real-world applications can amplify existing
bias and fairness challenges [27], undermining the reliability and robustness of Artificial Intelligence (AI) systems and
Authors’ Contact Information: Hongliu CAO, caohongliu@gmail.com; Eoin Thomas; Rodrigo ACUNA AGOST, Amadeus, Nice, France.
Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not
made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components
of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on
servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
Manuscript submitted to ACM
Manuscript submitted to ACM
1
arXiv:2602.00044v1  [cs.CY]  19 Jan 2026

--- Page 2 ---

2
Trovato et al.
exacerbating societal inequities. In creative contexts, these risks extend beyond factual accuracy: representational
harms, stereotype reinforcement, and cultural homogenization can shape design outcomes and user experiences in
subtle but consequential ways [4, 33].
There is a rich body of research on bias detection in the area of Natural Language Processing (NLP) and language
models. Early work examined bias in static word embeddings, using association tests such as the Word Embedding
Association Test (WEAT) and its variants to quantify stereotypical associations [10, 12]. To extend these measures to
contextualized embeddings, the Sentence Encoder Association Test (SEAT) was introduced to generate embeddings from
semantically bleached and template-based sentences [44]. While these approaches have been influential for probing
internal representations, prior work shows that they have weak and inconsistent correlations with biases in downstream
tasks and offer limited applicability to LLMs [11, 20, 27]. Subsequent work introduced masked token methods, which
estimate token probabilities by masking words in a sentence and prompting a language model to predict the missing
token. Although effective for examining contextual associations, these methods depend on rigid templates with limited
semantic diversity and a narrow set of target words, which constrains their generalizability and robustness [27].
Recent work has shifted toward LLM-specific bias detection, using metrics on generated text for tasks such as
sentence completion [22] and question answering [55]. These approaches leverage prompt-based probing and generative
benchmarks to assess stereotypes and fairness in generated outputs. However, they rely on user-defined datasets that
suffer from ambiguity, limited coverage, and scalability issues [19, 27]. Moreover, these evaluations rarely reflect
real-world usage, leaving creative downstream tasks such as persona generation and brainstorming largely unexamined.
Unlike factual Question-Answering (QA), creative outputs influence downstream design decisions, making unexamined
biases particularly consequential for inclusivity and fairness in real-world products. Prior work has examined bias
and fairness in persona generation, including narrative style descriptive personas conditioned on specific domains or
meta personas, through manual expert assessments and quantitative comparisons against ground truth profiles [39, 56].
These studies reveal persistent risks of stereotype propagation in creative applications. Despite these efforts, existing
approaches remain fragmented and narrow in scope. Systematic, holistic, and scalable methods for examining bias and
fairness in creative LLM outputs are still scarce, leaving practitioners without robust metrics to evaluate or mitigate
these risks.
To address this gap, we introduce the Persona Brainstorm Audit (PBA), a scalable and interpretable auditing method
for creative LLM use in persona generation. Our work is driven by a simple but pressing question: when LLMs imagine
people, what patterns of bias emerge and how do they change over time? To unpack this, we explore three dimensions
of inquiry. First, we ask whether leading LLMs differ in the severity and extent of bias when examined through PBA.
Next, we investigate the shape of these biases by answering how do different LLMs exhibit distinct patterns of bias
across identity dimensions. Finally, we examine how these patterns evolve across successive model releases, probing
whether fairness improves, stagnates, or even regresses. The main contributions of this work are:
• A novel auditing method: PBA is able to detect biases in LLM-generated personas without relying on fixed
identity categories or static benchmarks.
• A robust bias metric: We adapt and normalize Cramér’s V for multi-cardinality, multi-dimensional identity
attributes, enabling fair and interpretable comparisons of bias strength across models and dimensions.
• A longitudinal, multi-model Analysis: We apply PBA to 12 state-of-the-art LLMs, uncovering nonlinear bias tra-
jectories and domain-specific allocation patterns that challenge assumptions of monotonic fairness improvement.
Manuscript submitted to ACM

--- Page 3 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
3
• Robustness and sensitivity Analysis: Empirical validation of PBA’s stability under variations in sample size,
prompt design, and debiasing strategies, ensuring reliability for longitudinal audits.
• Actionable Implications: Design and governance recommendations for bias-aware creative AI, including continu-
ous auditing, transparency practices, and sustainability considerations.
2
Related works
In recent years, LLMs have emerged as a powerful tool in various industrial applications, sparking widespread concerns
related to bias and fairness in LLM based applications. This led to a significant surge in research works on bias
identification and measurement in LLMs.
Bias types: Bias in Large Language Models LLMs can be categorized as intrinsic or extrinsic bias. Intrinsic bias
originates during pre-training, reflecting patterns and assumptions embedded in large-scale training data and model
architecture [63]. In contrast, extrinsic bias arises during fine-tuning or task-specific deployment, often influencing
outputs in specific tasks such as automated decision-making systems [32]. Differentiating these sources is essential
for tracing bias origins and informing mitigation strategies [20, 27]. Beyond intrinsic and extrinsic distinctions, biases
in LLM can also be categorized along sociodemographic axes [27], including gender [47], race [5], age [16], sexual
orientation [24], religion [1], socioeconomic status [7], disability [31], etc. These biases contribute to representational
harms (e.g., stereotyping, misrepresentation) and allocational harms (e.g., unequal access to resources), reinforcing the
need for systematic auditing [27]. A keyword-based analysis of the ACL Anthology [19] shows that among 4,140 papers
related to bias and stereotypes, gender bias dominates (54.1%), followed by racial bias (25.8%), while other identities such
as sexual orientation, nationality, and profession receive limited attention. This imbalance highlights the importance of
scalable frameworks capable of surfacing underrepresented forms of bias.
Bias Identification methods & Metrics: Bias evaluation in LLMs typically follows three paradigms: into embedding-
based, probability-based, and generation-based (or prompt-based) approaches [17, 27, 68]. Among these, generation-
based methods are particularly relevant for auditing both proprietary and open-source models, as they directly assess
outputs under prompting. These methods involve conditioning the model on a predefined prompt, often designed to elicit
biased or toxic responses, and then analyzing the generated continuations for evidence of bias [27]. Generation-based
approaches can be further divided into two primary paradigms: sentence completion, where the model completes partial
sentences, and Question-Answering (QA), where responses to structured queries are evaluated for fairness and bias. For
example, RealToxicityPrompts [29] provides 100,000 web-derived sentence prefixes with toxicity scores annotated by
Perspective API, allowing measurement of toxicity in generation texts. BOLD [22] offers 23,679 prompts to assess bias
across dimensions such as profession, gender, race, religion, and political ideology by scraping English Wikipedia pages
that mention a group in the bias domain. HONEST [49] includes 420 prompts for detecting negative gender stereotypes
in six languages (English, Italian, French, Portuguese, Spanish, and Romanian), while TrustGPT [35] offers prompts to
evaluate toxicity and performance disparities across social groups. These methods typically measure bias by analyzing
sentiment or toxicity inconsistencies across demographic groups or by counting harmful completions. QA benchmarks
adopt a similar principle. UnQover [40] employs underspecified questions to expose stereotyping in gender, nationality,
ethnicity, and religion, where unbiased models should treat all answers as equally likely. BBQ [55] requires models
to select the correct answer from multiple options, using ambiguous and disambiguated contexts to reveal models’
reliance on stereotypes. Together, these tools provide a foundation for systematic bias auditing in generative AI.
Gaps in Current Approaches: Despite significant progress, existing methods for bias evaluation exhibit several
critical limitations. First, coverage of bias types remains narrow. Most research focuses on gender and race, often
Manuscript submitted to ACM

--- Page 4 ---

4
Trovato et al.
constrained by binary gender constructs [21] and Western racial histories [57], while other identity axes such as
sexual orientation or socioeconomic status remain underrepresented [19]. Many benchmarks reduce bias to binary
group comparisons or pronoun resolution, which fail to capture complex social relationships and do not reflect how
models generate biased content in open-ended contexts [27]. Second, evaluation metrics introduce methodological
challenges. Distribution-based metrics rely on word associations that poorly reflect downstream harms [11], while
classifier-based metrics inherit biases from toxicity and sentiment models, disproportionately flagging dialects like
African-American English [48, 58] and misclassifying content related to marginalized groups [46]. Third, benchmark
design limits generalizability. Many datasets originate from Western contexts and use template-based prompts lacking
linguistic and cultural diversity [19]. Widely used resources such as Winogender, WinoBias, and StereoSet contain
ambiguities regarding stereotype definitions, raising concerns about validity [3, 9]. Moreover, bias is dynamic, yet most
benchmarks treat it as static, ignoring temporal shifts [28]. Finally, existing bias evaluation methods remain largely
disconnected from real-world applications, as assessments are primarily conducted at model checkpoints rather than
within downstream tasks or daily use cases [19, 61]. Tasks such as selecting between pronouns or predefined answer
options fail to capture how a model would independently generate biased content, limiting the practical relevance of
these benchmarks [27].
3
Proposed Method
Recently, LLMs are increasingly integrated into creative workflows such as brainstorming and persona generation
[4, 25, 54], while automated and systematic bias evaluation in these contexts remains underexplored. Most existing
bias detection methods focus on constrained tasks like question answering or sentence completion using predefined
templates, which fail to capture how bias emerges in open-ended, creative generations. This gap poses a critical challenge
for assessing fairness in real-world creative applications.
3.1
Persona Brainstorm Audit
To address these limitations mentioned above, we introduce the Persona Brainstorm Audit (PBA), a scalable and
transparent auditing method for systematic bias detection within structured domains. Rather than relying on predefined
protected attributes (e.g., male, female) or stereotype templates, PBA prompts LLMs to generate large-scale persona
profiles across diverse dimensions such as race/ethnicity, gender, sexual orientation, education, occupation, social class,
etc. This open-ended design enables the detection of diverse biases without constraining outputs to fixed categories. PBA
is extensible to additional dimensions, supporting broader bias detection and enhancing applicability across domains.
By analyzing systematic associations within generated profiles, PBA surfaces patterns of diverse forms of bias. These
patterns are quantified using interpretable metrics (detailed below), offering a robust approach to fairness auditing in
creative AI applications.
3.2
Proposed metric
To systematically quantify bias in LLM-generated personas, we employ Cramér’s V [18], a well-established and
interpretable measure of association between categorical variables. Cramér’s V is particularly suited to the proposed
PBA as it accommodates variables with differing cardinalities and yields a score between 0 and 1, facilitating intuitive
Manuscript submitted to ACM

--- Page 5 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
5
comparisons across identity dimensions. Cramér’s V is derived from the chi-squared statistic and is defined as:
𝑉=
√︄
𝜒2
𝑛· min(𝑘−1,𝑟−1)
(1)
Where:
• 𝜒2 is the chi-squared statistic from the contingency table. For example, to assess whether gender is associated
with occupation in LLM-generated personas, we construct a table where rows represent gender categories
(e.g., male, female, nonbinary) and columns represent occupation categories (e.g., engineer, teacher, artist,
caregiver, executive). The 𝜒2 statistic captures the deviation between observed and expected frequencies under
the assumption of independence.
• 𝑛is the total number of observations. In the context of PBA, 𝑛corresponds to the total number of generated
personas included in the audit.
• 𝑘and 𝑟denote the number of categories in each variable. For instance, if the gender dimension includes 3
categories and the occupation dimension includes 5 categories, then 𝑘= 5 and 𝑟= 3. The term min(𝑘−1,𝑟−1)
ensures normalization based on the smaller degree of freedom, allowing Cramér’s V to remain bounded between
0 and 1.
Table 1. Comparison of PBA with existing bias evaluation methods
Dimension
Existing Benchmarks
Persona Brainstorm Audit (PBA)
Bias Type Coverage
Narrow focus on binary gender and Western
racial categories; limited inclusion of other
identity axes
Broad and extensible coverage including
race, gender, sexual orientation, class, dis-
ability, etc.
Intersectionality
Not supported; evaluates attributes in isola-
tion
Supports intersectional analysis across mul-
tiple identity dimensions
Evaluation Task
Constrained tasks (e.g., pronoun resolution,
sentence completion)
Open-ended persona generation reflecting
real-world creative workflows
Metric Design
Classifier-based or word-association met-
rics; often opaque and error-prone
Interpretable metrics based on attribute as-
sociations in generated content
Cultural Generalizabil-
ity
Western-centric prompts and datasets; lim-
ited linguistic and cultural diversity
Prompt design adaptable to diverse cultural
and linguistic contexts
Temporal Sensitivity
Static benchmarks; do not account for evolv-
ing stereotypes or social norms
Supports longitudinal audits to track bias
evolution over time
Scalability
Hard to increase in terms of sample size and
bias dimensions
Scales easily to new bias dimensions and
larger sample sizes
Transparency & Repro-
ducibility
Often opaque scoring and ambiguous
stereotype definitions
Transparent audit protocol with repro-
ducible outputs and human-readable met-
rics
Data Leakage Risk
High; fixed datasets and known answers are
easily memorized by models
Low; open-ended generation avoids fixed
answers and reduces leakage risk
A Cramér’s V score of 0 indicates no association (e.g., gender is independent of social class in model outputs), while a
score of 1 reflects maximal association (e.g., race is strongly correlated with occupation). Because statistical significance
alone does not convey the magnitude of an effect, we report effect sizes to characterize the strength of observed
associations. Following interpretive guidelines from [37], we classify bias strength based on Cramér’s V thresholds
Manuscript submitted to ACM

--- Page 6 ---

6
Trovato et al.
(e.g., values below 0.06 indicate low bias, while values above 0.29 suggest very high bias for degrees of freedom equal
to 3). However, because different bias dimensions yield contingency tables with varying degrees of freedom, direct
comparison of raw Cramér’s V scores can be misleading. For example, name x occupation may have a much higher
degree of freedom than gender x education, simply due to the number of unique names or occupations. To address
this, we apply a degree-of-freedom-aware normalization. Each raw score is scaled relative to established thresholds for
small, medium, and large effects [37]. Normalized scores are mapped to the following scale:
• 0–0.33 indicates a small bias,
• 0.33–0.66 indicates a medium bias,
• 0.66–1.0 indicates a high bias,
• values >1.0 reflect very high bias beyond the large-effect threshold.
This normalization preserves interpretability while accounting for structural differences in category granularity. It
enables equitable comparison of bias levels across models and identity dimensions, supporting scalable and meaningful
fairness evaluations in generative AI. To validate whether higher bias severity indicated by normalized Cramér’s V
scores corresponds to greater potential harm, we conducted a preliminary human validation study. This study is found
in Appendix B.6 and showcases that a single step on the scale (from high bias to very high bias) can be identified by all
human validators.
The proposed PBA and its evaluation metric address key limitations in existing bias evaluation approaches. Unlike
benchmarks that focus narrowly on binary gender or Western racial categories, PBA supports broad and extensible
coverage across identity dimensions. It enables intersectional analysis by generating personas that reflect multiple,
overlapping identity attributes, rather than evaluating them in isolation. Where traditional methods rely on constrained
tasks such as pronoun resolution or sentence completion, PBA situates bias evaluation within open-ended persona
generation to align with real-world creative workflows. This shift enhances ecological validity and reflects how LLMs
are used in practice. PBA also improves cultural generalizability through adaptable prompt design, moving beyond
Western-centric datasets. It supports longitudinal audits to track bias evolution over time, addressing the static nature of
most benchmarks. Unlike classifier-dependent metrics, PBA emphasizes transparency by analyzing raw model outputs
with interpretable, human-readable metrics. Finally, its open-ended generation reduces data leakage risks associated
with fixed-answer benchmarks, enabling scalable and reproducible audits. A summarized comparison of PBA with
existing bias evaluation methods can be found in Table 1.
4
Empirical Findings from PBA across LLMs
To demonstrate the practical utility of the proposed PBA, this section presents an empirical evaluation of bias in
persona generation across widely used LLMs. Unlike prior work, this study aims to expand the scope of bias analysis
by examining identity dimensions that remain underrepresented in existing benchmarks. Specifically, we investigate
how attributes such as name, gender, ethnicity, and sexual orientation are associated with social class, education
level, occupation, and personal interests in LLM-generated personas. This instantiation of PBA enables a systematic
audit of representational bias across multiple identity axes, revealing complex patterns in open-ended generative
contexts. Through this analysis, we seek to advance fairness auditing methodologies and contribute to a more inclusive
understanding of bias in creative AI applications.
Manuscript submitted to ACM

--- Page 7 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
7
4.1
Experimental protocol
Prompt design: In order to instantiate the proposed PBA to investigate associations between identity attributes and
social-economical roles, we designed a structured prompting protocol that supports scalable and interpretable analysis.
Unlike prior bias evaluation methods that rely on predefined protected categories (e.g., binary gender labels such as
“male” and “female”), our approach leverages open-ended persona generation. To address practical constraints such as
output token limits and formatting inconsistencies in LLM responses, we adopt a standardized prompt that requests
structured output in JSON format. The prompt is as follows:
“Brainstorm 20 diverse user profiles with the following information in JSON format: name, gender, ethnicity, sexual
orientation, social class, education level, occupation, and top personal interest. Return only the generated profiles with
STRICTLY no other text.”
This format ensures that each generated persona contains a complete and comparable set of attributes, facilitating
downstream parsing and statistical analysis. By avoiding rigid templates and predefined categories, this protocol enables
the detection of nuanced biases that may not be captured by conventional benchmarks, while maintaining consistency
and reproducibility across model evaluations.
LLM models & parameters: The work includes models developed by OpenAI (based in the United States), such as
GPT-3.5, GPT-4, GPT-4o, GPT-4.1, GPT-4.1 mini, GPT-4.1 nano, GPT-5, GPT-5 mini, and GPT-5 nano, as well as models
from Mistral (based in Europe), including Ministral-3B (ministral-3b-2410), Mistral-small (mistral-small-2501), and
Mistral-medium (mistral-medium-2505). This selection reflects a range of model sizes, release periods, and regional
development contexts, allowing us to examine whether bias patterns vary across different design philosophies, model
complexity and deployment ecosystems. All models were prompted using a temperature setting of 1. This choice is
grounded in prior work on bias detection in generative tasks [62], and is further supported by two practical considerations:
(1) creative tasks such as persona generation benefit from higher temperature settings, which promote diversity and
reduce deterministic outputs; and (2) GPT-5 models currently support only temperature = 1, ensuring consistency across
all evaluations. We generate 10,000 persona profiles (without duplicates) for each LLM, providing a robust sample size
for statistical analysis and enabling the detection of both frequent and subtle patterns of representational bias across
model families.
Data processing: To operationalize the proposed PBA for large-scale analysis, we implement a structured normal-
ization pipeline designed to balance comparability, scalability, and interpretability.
First, generated persona profiles in JSON format are parsed into tabular structures using Pandas. Attributes are
normalized (lowercasing, stemming), and profiles are concatenated across iterations. Duplicate entries are removed
to mitigate skew introduced by uneven duplication rates across models. Deduplication statistics and inter-model
comparisons are reported in Table 7 in the Appendix.
Second, raw attribute cardinalities exhibit substantial variability across models. To enable meaningful comparison,
we consolidate diverse generated terms into commonly accepted minimal non-redundant categories using GPT-5,
followed by human validation. For example, variants such as “high school,” “secondary school,” “higher secondary” were
normalized to “high school”. Cardinalities before and after data processing are documented in the Appendix (Table 6).
This abstraction ensures comparability across models, statistical robustness, and scalability for benchmarking, while
preserving links to original terms for drill-down (zoom in) analysis (e.g., Healthcare →nurse, doctor, etc.).
Finally, contingency matrices are constructed for each bias dimension based on the normalized categories, then
normalized Cramer’s V scores are computed, adjusting for degrees of freedom to ensure comparability across models
Manuscript submitted to ACM

--- Page 8 ---

8
Trovato et al.
with differing category distributions. All generated profiles, normalization mappings, and processing code will be
released upon publication to support transparency and reproducibility.
This pipeline reflects our broader philosophy that fairness is not a fixed endpoint but a bar that must be raised
continuously. Group fairness itself is inherently multi-scalar: definitions of “group” vary in granularity, size, and level of
abstraction, and these definitions evolve across cultural, regional, and temporal contexts. Our approach accommodates
this variability through semantic consolidation (zooming out) and drill-down capability (zooming in), enabling fairness
evaluation at multiple levels. Key advantages include: (1) comparability across models by reducing lexical variability
and cardinality differences; (2) statistical robustness through consolidation of sparse categories; (3) flexibility and
sustainability, as researchers can easily adapt to evolving group definitions or introduce finer granularity by modifying
the mapping file without altering the pipeline; and (4) transparency and interpretability, as mappings preserve links to
original terms for both macro-level benchmarking and micro-level bias analysis. Together, these properties position
PBA as a scalable and future-proof auditing method for fairness research.
4.2
RQ1: How do leading LLMs differ in the extent and severity of bias when examined through PBA?
Following the experimental protocol described in the previous section, we generated 10,000 personas from each of 12
state-of-the-art LLMs, resulting in a total of 120,000 open-ended persona profiles. These generated profiles are analyzed
across 16 bias dimensions, constructed by crossing four identity axes (name, gender, ethnicity, sexual orientation) with
four social dimensions (social class, education, occupation, interest). Normalized Cramér’s V score is calculated for each
bias dimension of each LLM.
Figure 6 presents radar charts comparing bias levels across 16 dimensions for 12 LLMs (the corresponding numerical
results are provided in Table 2). The models are grouped into four subplots for readability: GPT-3.5, GPT-4, and GPT-
4o (top-left); GPT-4.1 series (top-right); GPT-5 series (bottom-left); and Mistral models (bottom-right). Each subplot
visualizes bias scores for three models, with each axis representing a distinct identity-social dimension pair. Bias severity
is color-coded using a perceptually accessible palette: low (gray), medium (amber), high (red), and very high (dark red).
To support colorblind accessibility, models are further distinguished using unique line styles and markers. The average
bias scores of each model series are shown in the title of each subplot.
LLMs with more compact polygonal profiles exhibit lower overall bias. From Figure 6, it can be seen that GPT-4o
exhibits the most compact profile, followed by Ministral-3B and GPT-4. GPT-4.1 mini and GPT-5 display broader,
irregular polygons with pronounced spikes, indicating higher bias and greater cross-dimension variability. Severity
levels show clear regimes. GPT-4o has 1 very high, 8 high, 5 medium, and 2 low bias dimensions. GPT-5 has 9 very high
and no low bias dimensions. The middle group includes GPT-4.1, GPT-4.1 nano, Mistral Small, and Mistral Medium.
Each has 5 to 8 very high bias dimensions.
Table 2 presents normalized Cramér’s V scores for 16 bias dimensions across 12 LLMs. Scores are color-coded by
severity thresholds: green = small (0–0.33), yellow = medium (0.33–0.66), orange = high (0.66–1.0), and red = very
high (>1.0). From the average bias scores across all dimensions, it can be observed that the least biased models are
GPT-4o, followed by Ministral-3B, GPT-4, and GPT-5 nano. In contrast, the most biased models are GPT-4.1 mini, GPT-5,
GPT-5 mini and Mistral-medium. Severity levels show clear regimes. For example, GPT-4o has 1 very high, 8 high, 5
medium, and 2 low bias dimensions, whereas GPT-5 exhibits 9 very high and no low bias dimensions.
Analysis by model family shows distinct patterns of bias across generations of LLMs. OpenAI early frontier models
(including GPT-3.5, GPT-4, and GPT-4o) have the lowest average bias scores. The Mistral series shows slightly higher
averages. In contrast, the most recent OpenAI series, GPT-4.1 series and GPT-5 series, have the highest average bias
Manuscript submitted to ACM

--- Page 9 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
9
Fig. 1. Radar chart comparing bias levels across 16 bias dimensions for 12 LLMs, including GPT-3.5, GPT-4, GPT-4o (top-left subplot),
GPT-4.1 series (top-right subplot), GPT-5 series (bottom-left subplot), and Mistral models (bottom-right subplot). Each subplot
displays three models, with bias measured across intersections of identity axes (name, gender, ethnicity, sexual orientation) and
social dimensions (social class, education, occupation, interest). The average bias scores of each model series are shown in the title of
each subplot. Bias severity is color-coded: low (gray), medium (amber), high (red), and very high (dark red). Line styles and markers
distinguish models for accessibility.
scores. Within the GPT-4.1 series, the largest model GPT-4.1 has the lowest bias score. However, within the GPT-5
series, the smallest model GPT-5 nano has the lowest bias score. The Mistral family shows a similar pattern as GPT-5
series: the smallest model Ministral-3B has the lowest bias score. These findings reveal that bias trajectories in LLMs are
neither linear nor uniform: lineage and scale interact in complex ways, producing structurally heterogeneous profiles
where the magnitude and concentration of biases vary sharply across dimensions. This underscores that mitigating bias
requires model-specific strategies rather than assumptions of steady progress across generations or model sizes. For
readers who prefer a visual summary, radar plots illustrating shape-based variability are provided in Appendix (Figure
6).
To examine whether bias profiles differ significantly between models, we conduct the pairwise significance tests
(t-test) across 16 bias dimensions and visualize the results in an upper-triangular heatmap (Figure 2), with models
Manuscript submitted to ACM

--- Page 10 ---

10
Trovato et al.
Name
Gender
Ethnicity
Sexual Orientation
Mean
Model
Soc.Cls
Educ.
Occup.
Interest
Soc.Cls
Educ.
Occup.
Interest
Soc.Cls
Educ.
Occup.
Interest
Soc.Cls
Educ.
Occup.
Interest
GPT-3.5
0.981
1.128
1.036
0.928
0.493
0.443
0.995
0.832
0.811
0.881
1.132
0.815
0.372
0.353
0.891
0.755
0.803
GPT-4
0.830
0.997
1.036
1.005
0.358
0.344
0.803
0.862
0.573
0.528
1.064
0.902
0.278
0.333
0.745
0.653
0.707
GPT-4o
0.791
0.813
0.943
0.909
0.542
0.377
0.939
1.006
0.568
0.554
0.796
0.785
0.311
0.205
0.667
0.640
0.678
GPT-4.1 nano
0.930
1.212
1.250
1.205
0.542
0.563
1.006
0.968
0.709
0.816
1.291
1.005
0.377
0.353
0.762
0.687
0.855
GPT-4.1 mini
1.046
1.372
1.350
1.573
0.601
0.528
1.066
1.254
0.721
0.864
1.227
1.155
0.471
0.525
0.946
0.806
0.969
GPT-4.1
1.077
1.092
1.141
1.145
0.497
0.493
0.998
1.049
0.667
0.694
1.095
0.913
0.415
0.432
0.976
0.728
0.838
GPT-5 nano
0.735
0.963
1.073
0.974
0.391
0.344
0.779
0.862
0.563
0.640
1.036
0.709
0.453
0.475
0.653
0.663
0.707
GPT-5 mini
1.029
1.424
1.359
0.962
0.467
0.415
1.134
1.077
0.665
0.796
1.250
0.913
0.476
0.578
1.252
0.922
0.920
GPT-5
1.097
1.364
1.245
1.336
0.398
0.401
1.066
1.074
0.716
0.905
1.368
1.232
0.417
0.495
1.160
0.932
0.950
Ministral-3B
0.704
1.000
1.177
1.027
0.332
0.358
0.910
0.934
0.526
0.561
0.758
0.642
0.337
0.485
0.776
0.663
0.699
Mistral-small
1.200
1.404
1.441
1.300
0.540
0.346
0.998
1.111
0.675
0.714
0.962
0.702
0.471
0.459
0.796
0.691
0.863
Mistral-medium
1.097
1.096
1.291
1.350
0.578
0.476
1.020
1.129
0.777
0.748
1.114
1.055
0.481
0.475
0.844
0.752
0.893
Table 2. Normalized Cramér’s V bias scores across intersections of identity axes (name, gender, ethnicity, sexual orientation) and
social dimensions (social class, education, occupation, interest) with color-coded thresholds: green = small (0–0.33), yellow = medium
(0.33–0.66), orange = high (0.66–1.0), red = very high (>1.0).
arranged from least biased (top-left) to most biased (bottom-right). Each cell displays the raw p-value for a comparison,
with black indicating significance after Benjamini–Hochberg False Discovery Rate (BH-FDR) correction [8] at q <
0.05 and white indicating non-significance. GPT-4o and Ministral-3B, the least biased models, are not significantly
better than GPT-4 or GPT-5 nano (p > 0.35), indicating comparable fairness profiles. In contrast, these 4 models are
significantly better than all remaining models (p < 0.001). The mid-bias cluster comprises GPT-3.5, GPT-4.1, GPT-4.1
nano and Mistral-small: while internal differences are less pronounced, comparisons with the low-bias group remain
significant. The high-bias cluster, including Mistral-medium, GPT-5 mini, GPT-5, and GPT-4.1 mini, shows statistically
significant differences from both low- and mid-bias clusters. These models demonstrate broad and systematic disparities
across multiple dimensions (each has 7-9 very high severity bias dimensions).
4.3
RQ2: How do different LLMs exhibit distinct patterns of bias across identity dimensions?
While RQ1 establishes that overall bias severity varies widely across models, aggregate scores alone obscure where
bias concentrates and what forms it takes. For creative applications, this granularity matters: potential harms often
arise not from global averages but from localized spikes on attributes that shape persona generation. Understanding
these patterns enables practitioners to estimate downstream risks and target mitigation where it matters most. To
address this, we conduct a two-part analysis: (1) dimension-wise comparison to identify which identity–attribute pairs
consistently exhibit the strongest associations; and (2) Deep dive into a focal dimension to examine how stereotypes
manifest across different models.
Dimension-wise comparison:
• Name-based associations are the strongest across all models (with the mean bias score of 1.113), with Name X
Occupation (mean: 1.195), Name X Education (mean: 1.155), and Name X Interest (mean: 1.143) topping the list.
These patterns indicate that names act as powerful socio-cultural signals, shaping downstream attributes in
ways that can reinforce stereotypes.
• Occupation and interest act as strong bias attractors. Across all identity dimensions (e.g., Name, Gender, Sexual
Orientation, Ethnicity), the identity X Occupation and identity X Interest consistently exhibit high or very high
levels of bias. For example, Ethnicity X Occupation averages 1.091, and Gender X Interest averages 1.013. These
attributes, often considered neutral in creative workflows, emerge as critical leverage points for mitigation.
Manuscript submitted to ACM

--- Page 11 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
11
Fig. 2. Upper-triangular heatmap of pairwise significance tests for model bias comparisons across 16 dimensions. Each cell shows
the raw p-value for a comparison between two models, formatted in compact notation. Black cells indicate significance after
Benjamini–Hochberg False Discovery Rate (BH-FDR) correction (q < 0.05), while white cells indicate non-significance. Models are
ordered from least biased (top-left) to most biased (bottom-right).
• Ethnicity and sexual orientation trends: Ethnicity strongly correlates with occupational outcomes, while sexual
orientation primarily influences occupations and interests rather than status markers like education or social
class.
• Asymmetric gender patterns. Gender bias is not uniform: Gender X Education and Gender X Social Class remain
low–medium, while Gender X Occupation and Gender X Interest spike into high tiers, reflecting persistent role
and taste stereotypes.
4.3.1
How stereotypes manifest across models? To examine how stereotypes manifest across models, we focus on
a high-impact dimension following analysis above: Sexual Orientation X Occupation. This pairing also reflects an
understudied dimension in the literature. We visualize in Figure 3 the Sexual Orientation X Occupation distributions
for 12 LLMs using heatmaps, with each subplot representing one model. To enable meaningful comparison while
emphasizing high-frequency roles, we visualize only the top 10 occupations per sexual orientation for each model in
Figure 3. Each cell indicates the percentage of a given sexual orientation assigned to an occupation (columns sum to
100% per sexual orientation within each model).
Manuscript submitted to ACM

--- Page 12 ---

12
Trovato et al.
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Professor
Hospitality & Retail
Social Impact & Nonprofit
Creative & Design
Teacher
Business & Finance
Skilled Worker
Science & Research
Engineering
Student
Media & Publishing
6 7 6 6 4
10 4 3 9 4
7 11 8 10 7
4 8 6 8 3
21 5 12 6 8
3 5 3 2 6
182721 11 25
6 1 1 2 3
3 1 4 14 3
7 0 2 11 1
3 9 7 5 8
2 0 1 6 2
4 1216 4 14
5 8 9 5 11
GPT-3.5
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Professor
Hospitality & Retail
Social Impact & Nonprofit
Creative & Design
Business & Finance
Skilled Worker
Science & Research
Engineering
Student
Media & Publishing
2 6 4 6 2
8 4 11 12 7
7 11 10 7 7
9 6 5 7 4
11 7 6 5 6
1 5 2 3 4
2423221023
4 5 5 10 4
4 0 1 5 1
8 131010 9
4 2 2 10 3
141313 8 25
5 6 7 6 5
GPT-4
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Hospitality & Retail
Professor
Teacher
Creative & Design
Business & Finance
Skilled Worker
Science & Research
Engineering
Student
Media & Publishing
3 8 7 10 3
10 4 9 7 9
7 10 9 4 5
13 6 7 6 8
10 6 6 6 6
3 5 5 6 2
223123 11 33
7 2 2 11 3
4 0 2 6 1
6 9 10 9 9
3 2 2 9 1
4 5 8 6 10
8 1310 9 9
GPT-4o
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Professor
Hospitality & Retail
Social Impact & Nonprofit
Creative & Design
Teacher
Business & Finance
Skilled Worker
Science & Research
Legal & Public Safety
Engineering
Student
Media & Publishing
0 5 3 5 2
9 2 5 12 9
2 5 5 2 3
9 3 5 8 5
20 6 6 7 5
0 6 4 2 4
1827181222
4 3 5 4 3
6 2 2 10 3
8 0 1 4 1
101218 9 11
2 3 3 5 1
1 0 1 5 1
2 1314 6 20
9 11 1210 9
GPT-4.1 nano
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Hospitality & Retail
Professor
Social Impact & Nonprofit
Creative & Design
Teacher
Business & Finance
Skilled Worker
Science & Research
Legal & Public Safety
Engineering
Student
Media & Publishing
1 5 4 8 2
6 3 1510 8
9 8 6 3 10
14 4 8 7 6
7 8 6 6 1
1 6 3 3 7
2423151020
8 1 2 4 0
6 1 2 10 1
1 0 2 7 0
3 1414 6 8
1 4 2 3 1
1 0 1 8 1
9 7 11 6 26
1016 11 8 10
GPT-4.1 mini
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Hospitality & Retail
Professor
Social Impact & Nonprofit
Creative & Design
Teacher
Business & Finance
Science & Research
Driver
Engineering
Student
Media & Publishing
2 8 3 8 1
14 5 6 11 10
6 5 5 3 3
15 8 13 8 13
16 8 7 6 2
1 7 3 2 4
1627221022
9 3 2 4 0
2 5 2 13 1
4 7 7 7 5
2 0 1 8 0
1 2 2 10 1
8 8 17 6 28
6 9 10 5 9
GPT-4.1
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Professor
Hospitality & Retail
Teacher
Creative & Design
Business & Finance
Science & Research
Engineering
Student
Media & Publishing
1 9 4 3 3
24 7 252322
4 6 7 3 3
2 4 3 12 4
15 7 5 7 8
3 6 5 6 3
3035241324
2 2 3 5 2
3 13 6 7 9
5 4 3 8 2
6 2 9 9 13
4 6 6 2 5
GPT-5 nano
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Hospitality & Retail
Professor
Social Impact & Nonprofit
Creative & Design
Teacher
Business & Finance
Skilled Worker
Science & Research
Legal & Public Safety
Engineering
Driver
Student
Media & Publishing
1 5 1 13 1
2715261336
15 3 11 5 4
3 5 2 4 1
1 13 9 8 7
172920 8 23
19 2 4 4 1
2 1 1 3 0
1 1 4 11 1
2 8 5 6 4
1 7 3 4 2
2 3 3 13 1
1 0 3 5 0
3 1 3 2 14
4 8 6 3 6
GPT-5 mini
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Hospitality & Retail
Professor
Teacher
Creative & Design
Social Impact & Nonprofit
Business & Finance
Skilled Worker
Science & Research
Driver
Engineering
Student
Media & Publishing
5 5 2 7 1
1622271434
2 1 3 2 2
19 6 10 5 9
5 4 1 3 1
7 3 1 4 0
242920 9 20
4 8 8 2 12
1 1 1 11 1
3 2 5 14 2
5 8 2 3 4
1 0 1 4 0
3 5 5 17 2
1 1 3 1 8
4 5 11 3 5
GPT-5
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Professor
Hospitality & Retail
Teacher
Creative & Design
Skilled Worker
Science & Research
Legal & Public Safety
Engineering
Student
7 242013 5
6 4 7 12 7
2 10 11 6 9
14 8 6 7 5
7 3 4 5 6
121515 11 12
141413 6 21
16 0 3 9 1
6 9 4 6 4
3 4 3 6 1
9 4 9 16 3
4 6 4 3 24
Ministral-3B
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Professor
Hospitality & Retail
Teacher
Creative & Design
Social Impact & Nonprofit
Business & Finance
Skilled Worker
Science & Research
Legal & Public Safety
Engineering
Student
Media & Publishing
3 21 9 15 6
5 3 8 9 14
5 7 7 6 7
5 8 9 6 3
10 5 6 5 4
19 6 4 5 2
2418221321
0 3 2 1 9
6 1 3 9 2
5 0 3 3 1
3 6 8 4 7
5 6 3 6 2
4 2 2 8 2
2 5 4 3 7
4 9 8 6 14
Mistral-small
Gay
Lesbian
Bisexual
Heterosexual
Other
Healthcare
IT & Software
Marketing & HR
Hospitality & Retail
Professor
Social Impact & Nonprofit
Creative & Design
Teacher
Business & Finance
Science & Research
Legal & Public Safety
Engineering
Student
Media & Publishing
8 5 7 11 1
1 0 1 4 4
131612 6 9
8 3 4 8 11
7 2 5 6 9
5 7 9 3 5
1633201241
9 3 4 4 3
2 0 0 13 0
1 4 8 10 0
8 7 0 7 4
0 0 0 7 0
10 4 25 4 10
11 15 5 5 2
 Mistral-medium
0
5
10
15
20
25
0
5
10
15
20
25
0
5
10
15
20
25
30
0
5
10
15
20
25
0
5
10
15
20
25
0
5
10
15
20
25
5
10
15
20
25
30
35
0
5
10
15
20
25
30
35
0
5
10
15
20
25
30
0
5
10
15
20
0
5
10
15
20
0
5
10
15
20
25
30
35
40
Fig. 3. Heatmaps of Sexual Orientation–Occupation distributions for 12 LLMs. Each subplot corresponds to one model. To facilitate
the comparison while focusing on high-mass roles, only top 10 most popular occupations of each sexual orientation are selected for
each LLM. Each cell is the percentage of that sexual orientation assigned to a given occupation (columns sum = 100% per sexual
orientation, within model).
Visual inspection of the heatmaps reveals systematic disparities in how LLMs associate sexual orientations to
occupational roles. Across all twelve models, non-heterosexual personas (Gay, Lesbian, Bisexual, Other) exhibit strong
clustering in a narrow set of occupations rather than balanced diversity compared to heterosexual personas. In Creative
& Design, high-intensity cells for lesbian, bisexual and gay categories recur across nearly all models, signaling a
persistent association between creative work and queer identities. This concentration is not confined to a single group;
it spans multiple non-heterosexual categories, producing a non-uniform yet distributed pattern. Conversely, lesbian,
bisexual, and gay categories exhibit very low intensity in Engineering across most models compared to heterosexuals,
suggesting a consistent heteronormative bias in technical domains. Overall, these patterns suggest that differentiation
by sexual orientation is driven less by hierarchical status (e.g., Sexual Orientation × Social Class remains low–medium
bias in Table 2) and more by domain-specific associations.
Different model families show distinct occupational patterns. In Healthcare, GPT models remain relatively flat, with
all sexual-orientation groups low and no strong peaks. In contrast, Mistral models assign a much higher share of
healthcare roles. More specifically, lesbian representation in Healthcare rises sharply: 24% in Ministral-3B and 21%
in Mistral-small, while Mistral-medium partly reverses this trend, lowering lesbian dominance. On the other hand,
Manuscript submitted to ACM

--- Page 13 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
13
GPT-5 series show a sharp rise in IT & Software compared to earlier GPT variants. Across GPT-3.5 and GPT-4.x, IT
allocations are modest (Gay 9.5%, Lesbian 3.7%, Bisexual 8.2%, Heterosexual 10.2% on average). GPT-5 series lift these
averages substantially (Gay 22.3%, Lesbian 14.7%, Bisexual 26.0%, Heterosexual 16.7%), signaling a strong family-level
shift toward IT domains, especially for non-heterosexual profiles. However, internal heterogeneity persists: GPT-5
nano peaks for Gay (24%) and Bisexual (25%), GPT-5 mini pushes Gay to 27% and Bisexual to 26%, while GPT-5 reverses
leadership with Lesbian at 22%, surpassing Gay (16%). A notable insight is the role of Lesbian profiles: historically
underrepresented in IT across GPT models, they surge in GPT-5 (22%), signaling a late-stage correction or instability
rather than a consistent trend. These patterns reveal that bias is architecture-dependent and variant-sensitive. GPT-5
series amplify IT associations broadly across non-heterosexual identities, while Mistral reinforces healthcare stereotypes
for lesbian profiles. The variability within GPT-5 series highlights that bias is dynamic, effective mitigation strategies
must therefore be variant-aware, monitor evolving patterns, and address multi-group fairness rather than assuming
stability.
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
31
51
34
22
36
15
34
32
27
43
34
47
35
17
38
36
30
38
GPT-3.5
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
19
21
22
16
16
15
36
35
29
39
41
40
45
44
50
46
43
45
GPT-4
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
17
24
17
11
14
7
43
46
42
60
63
65
41
30
41
29
23
28
GPT-4o
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
28
33
23
28
29
20
27
23
27
44
37
51
45
45
50
28
34
29
GPT-4.1 nano
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
19
43
35
9
13
15
55
42
35
64
63
60
25
15
31
27
24
25
GPT-4.1 mini
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
27
59
43
21
32
26
35
27
30
47
42
48
38
14
27
32
26
26
GPT-4.1
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
45
34
26
33
40
28
29
25
23
25
30
32
26
41
51
42
30
40
GPT-5 nano
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
37
58
54
15
34
39
36
27
23
46
44
39
27
15
24
39
22
22
GPT-5 mini
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
30
51
42
20
31
32
40
34
37
49
49
46
30
15
22
31
20
22
GPT-5
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
41
29
28
27
30
26
15
19
21
25
29
27
44
52
52
47
41
47
Ministral-3B
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
29
32
15
17
15
11
28
21
18
38
34
41
43
47
67
45
51
49
Mistral-small
male X Gay
male X Bisexual
male X Heterosexual
female X Lesbian
female X Bisexual
female X Heterosexual
lower
middle
upper
13
44
17
2
18
6
55
55
33
72
59
57
32
2
50
26
22
38
 Mistral-medium
25
50
25
50
25
50
25
50
25
50
25
50
25
50
25
50
25
50
25
50
25
50
25
50
Fig. 4. Heatmaps of Gender X Sexual Orientation intersection - Social Class distributions for 12 LLMs. Each subplot corresponds to
one model. Each cell is the percentage of that Gender X Sexual Orientation intersection assigned to a given Social Class (columns
sum = 100% per Gender X Sexual Orientation intersection, within model).
4.3.2
Intersectional analysis. A key strength of the proposed PBA lies in its ability to enable intersectional analysis
across identity dimensions. Fairness cannot be meaningfully evaluated through only single-axis perspectives, as
overlapping identities often surface disparities that remain hidden otherwise. Intersectional analysis embodies our
broader philosophy that fairness is not a fixed endpoint but a dynamic standard, evolving alongside shifting definitions
of “group”.
To illustrate this capability, we examine the intersection of Gender × Sexual Orientation and its relationship to Social
Class. Figure 4 displays heatmaps for these intersections across 12 LLMs, with each subplot representing one model.
For clarity, we focus on high-frequency identities: male × Gay, male × Bisexual, male × Heterosexual, female × Lesbian,
Manuscript submitted to ACM

--- Page 14 ---

14
Trovato et al.
female × Bisexual, and female × Heterosexual, associated to lower, middle, and upper social classes. Each cell shows the
percentage of an intersectional identity assigned to a social class, with columns summing to 100% within each model.
Several global trends can be observed from Figure 4:
• Sexual orientation disparities within the same gender are pronounced. For male identities, GPT-3.5, GPT-4.1 mini,
GPT-4.1, GPT-5 mini, GPT-5, and Mistral-medium consistently associate bisexual men with lower-class roles at
high rates, while gay and heterosexual men show more balanced distribution. Similarly, for female identities,
bisexual women dominate middle-class representation in most models, whereas heterosexual women and lesbian
often cluster toward upper-class associations (especially in GPT-3.5, GPT-4.1, GPT-5 series and Mistral-medium).
• Gender gaps within each sexual orientation category are also apparent. For gay versus lesbian identities, several
models (GPT-4o, GPT-4.1 nano, GPT-4.1, and Mistral-medium) consistently associate lesbian identities with
middle-class roles, whereas gay identities lean toward upper-class occupations. Interestingly, this trend reverses
in GPT-5 nano and GPT-5 mini, highlighting model-specific variability. For bisexual identities, a persistent bias
appears across GPT-3.5, GPT-4.1 variants, GPT-5 series, and Mistral-medium: female intersections dominate
middle-class representation, while male intersections exhibit greater variability across social classes, suggesting
uneven treatment within the same orientation. Finally, for heterosexual identities, most models (GPT-4, GPT-4o,
GPT-4.1 series, GPT-5 nano and Mistral series) have higher upper-class associations for male intersections
compared to their female counterparts.
These findings underscore that intersectional analysis is essential for complementing single-axis metrics, as it reveals
disparities that remain invisible when identities are examined in isolation. Disparities emerge both within gender and
within sexual orientation, amplifying bias in nuanced ways. Larger or newer models do not eliminate these patterns; in
some cases, they intensify them, underscoring the need for intersectional auditing in real-world deployments.
4.4
RQ3: How do biases emerge, attenuate, or resurface across successive LLM versions?
Bias in LLMs is dynamic rather than fixed. As models evolve through new releases, fine-tuned variants, and fairness
interventions, their bias profiles shift in complex ways. Prior work shows that mitigation often follows non-linear
trajectories, where biases attenuate in one dimension but resurface in another due to changes in training data, opti-
mization objectives, or alignment strategies [33]. Understanding how stereotypes emerge, diminish, or reappear across
versions is therefore critical to assess whether fairness gains are systemic or incidental.
To study how bias envolves across model updates, we focus on five OpenAI models: GPT-3.5, GPT-4, GPT-4o, GPT-4.1,
and GPT-5, because they represent a clear evolutionary path, offering a natural lens for studying longitudinal bias
dynamics. These models span major architectural and training shifts. GPT-4 introduced multimodal input and achieved
human-level performance on benchmarks, far surpassing GPT-3.5 [50]. GPT-4o enabled real-time multimodal interaction
across text, audio, image, and video [51], while GPT-4.1 improved coding, instruction following, and long-context
understanding [52]. The most recent GPT-5 unifies fast and deep reasoning, reduces hallucinations, and enhances
performance across key domains [53].
Figure 5 visualizes how normalized Cramér’s V scores shift across five model generations for four identity axes. Each
subplot corresponds to one identity axis and plots normalized Cramér’s V scores for four social dimensions (Social
Class, Education, Occupation, and Interest) alongside their average. Figure 5 reveals that bias trajectories across GPT
generations are neither linear nor uniformly improving, challenging the common expectation that newer models are
inherently fairer. Some biases intensify as models gain capabilities. For example, name and ethnicity-based biases remain
Manuscript submitted to ACM

--- Page 15 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
15
GPT-3.5
GPT-4
GPT-4o
GPT-4.1
GPT-5
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Normalized Cramér's V
Name
GPT-3.5
GPT-4
GPT-4o
GPT-4.1
GPT-5
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Normalized Cramér's V
Gender
GPT-3.5
GPT-4
GPT-4o
GPT-4.1
GPT-5
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Normalized Cramér's V
Ethnicity
GPT-3.5
GPT-4
GPT-4o
GPT-4.1
GPT-5
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
Normalized Cramér's V
Sexual Orientation
Soc.Cls
Educ.
Occup.
Interest
Average
Fig. 5. The bias evolution across five model generations (GPT-3.5 →GPT-4 →GPT-4o →GPT-4.1 →GPT-5) for four identity axes:
Name, Gender, Ethnicity, and Sexual Orientation. Each subplot corresponds to one identity axis and plots normalized Cramér’s V
scores for four social dimensions (Social Class, Education, Occupation, and Interest) alongside their average (black line). Shaded
bands indicate interpretive thresholds: small (<0.33), medium (0.33–0.66), high (0.66–1.0), and very high (>1.0).
high throughout and peak in GPT-5 most of the times, suggesting that the recent improvement abilities on GPT-5
amplify biases rather than eliminate them. Among most bias dimensions (e.g., name, ethnicity and sexual orientation),
there is a clear bias reduction from GPT-3.5 to GPT-4 to GPT-4o. Bias often rebounds in later versions as seen in GPT-4.1
and GPT-5. These patterns indicate that fairness improvements are not guaranteed by scale, alignment, or new-release
alone. For practitioners and users, this underscores the need for longitudinal audits and transparency across releases.
5
Robustness and Sensitivity Analysis of PBA
Ensuring the robustness of auditing method is essential for their practical adoption and scientific validity. While the
proposed PBA offers a scalable and interpretable approach to bias detection, its reliability under varying conditions must
be rigorously evaluated. In this section, we conduct a series of sensitivity analyses to examine how PBA performs when
key factors change, including sample size, prompt framing through role-playing, and explicit debiasing instructions.
These analyses address two critical questions: (1) Do observed bias patterns remain stable across different data scales
Manuscript submitted to ACM

--- Page 16 ---

16
Trovato et al.
and prompt variations; (2) Can prompt-level interventions meaningfully alter fairness outcomes? By systematically
examining these factors, we assess the robustness of PBA’s metrics for deploying scalable and trustworthy bias audits
in real-world creative AI applications.
5.1
Impact of sample size
In the previous analysis, each LLM was prompted to generate 10,000 personas as the basis for bias and fairness evaluation.
To examine the robustness of PBA under varying data scales, we conducted a sensitivity analysis across four sample
sizes: 5,000, 10,000, 15,000, and 20,000 personas. To ensure sustainability and real-world relevance, we evaluate only
the latest models (three from the GPT-5 family and three from the Mistral series) reflecting current state-of-the-art
deployments. This comparison allows us to assess whether observed bias patterns remain stable as the number of
generated personas increases. To quantify the robustness of PBA across different sample sizes, we compute the following
metrics for each bias dimension:
• Intraclass Correlation Coefficient (ICC) [45]: ICC is employed to assess the consistency of normalized Cramér’s
V scores across conditions. We report two forms computed across all sizes: ICC(C,1) for quantifying the degree
of consistency among measurements and ICC(A,1) for quantifying the degree of absolute agreement [42].
• Rank stability: Spearman and Kendall rank correlation coefficient are calculated [36, 59]. Spearman’s 𝜌captures
overall monotonic agreement, while Kendall’s 𝜏_𝑏assesses pairwise order consistency and explicitly accounts
for ties. Used together, they provide complementary views of rank agreement.
• Severity Difference (SD): For ordinal severity levels (e.g., low, medium, high, very high shown in the previous
section), we measure the mean absolute difference among different sample sizes.
Table 3 reports agreement metrics for varying sample sizes. For ICC(C,1), ICC(A,1), Spearman, and Kendall, higher
values indicate stronger consistency, whereas for Severity Difference, lower values indicate better agreement. Overall,
most bias dimensions exhibit very high stability across sample sizes, reinforcing the robustness of PBA to data scale
variations. Notably, Severity Difference remains unchanged for the majority of dimensions (10 out of 16), suggesting
that severity assessments are largely insensitive to sample size. Robustness to sampling variation is critical: it ensures
that PBA delivers reliable and comparable audits under practical constraints and enables consistent longitudinal bias
tracking without requiring fixed or unsustainable large sample sizes.
5.2
Impact of role playing
Role-playing has emerged as a structured prompt-engineering strategy that instructs the model to “act as” a specific
persona, such as a teacher or domain expert, to influence reasoning patterns and output characteristics [64]. Recent work
demonstrates its effectiveness for improving alignment and task performance [34, 38, 65]. However, its implications for
bias and fairness remain underexplored. Hence, we propose to study if expert roles such as a UX researcher have an
impact on the proposed PBA, which is essential for designing robust auditing methods.
To systematically examine the effect of role-playing on bias auditing, we compare persona generation under two
conditions: a baseline prompt with no roles specified and a role-conditioned prompt where the LLM is instructed to act
as an expert UX researcher. Beyond the robustness metrics reported in the previous section, we report paired t-test
p-values to assess whether role-playing as an expert UX researcher leads to a statistically significant reduction in bias
compared to the original prompt (the paired samples are normalized Cramér’s V scores for each bias dimension under
Manuscript submitted to ACM

--- Page 17 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
17
Table 3. Robustness of PBA across different sample sizes (5k, 10k, 15k, 20k) with multiple metrics. For ICC(C,1), ICC(A,1), Spearman,
Kendall, larger values indicate stronger agreement. For Severity Difference, lower values indicate stronger agreement.
ICC(C,1) (↑)
ICC(A,1) (↑)
Spearman (↑)
Kendall (↑)
SD (↓)
Name x Social Class
0.974
0.974
0.905
0.778
0.000
Name x Education
0.929
0.934
0.928
0.852
0.111
Name x Occupation
0.828
0.746
0.833
0.674
0.000
Name x Interest
0.960
0.927
0.943
0.867
0.000
Gender x Social Class
0.980
0.980
0.981
0.956
0.056
Gender x Education
0.930
0.933
0.842
0.763
0.000
Gender x Occupation
0.993
0.992
1.000
1.000
0.000
Gender x Interest
0.978
0.979
0.899
0.828
0.000
Ethnicity
x
Social
Class
0.975
0.974
0.943
0.867
0.111
Ethnicity
x
Educa-
tion
0.983
0.978
0.947
0.898
0.000
Ethnicity x Occupa-
tion
0.996
0.988
1.000
1.000
0.000
Ethnicity x Interest
0.986
0.986
0.981
0.956
0.056
Sexual Orientation x
Social Class
0.969
0.963
0.851
0.763
0.000
Sexual Orientation x
Education
0.874
0.853
0.714
0.689
0.000
Sexual Orientation x
Occupation
0.998
0.998
1.000
1.000
0.056
Sexual Orientation x
Interest
0.938
0.938
0.924
0.867
0.167
two conditions: original prompt versus modified prompt across all models). A low p-value (e.g., p <0.05) suggests that
role-playing produces a significant improvement in bias scores.
Table 4 summarizes the results. Agreement metrics suggest that most bias dimensions maintain high stability when
prompts are adapted for role-playing, indicating that the underlying bias patterns are largely preserved. The only
exception is the Sexual Orientation X Education dimension, which shows reduced agreement. However, its Severity
Difference is 0, implying that while the distribution of bias scores may shift slightly, the severity of biased outcomes
remains unchanged. Moreover, the t-test results reveal no statistically significant differences between the original and
role-playing prompts across all bias dimensions. This finding indicates that role-playing as a prompt variation strategy,
does not significantly affect PBA outcomes or bias severity.
5.3
Impact of debiasing prompt
Prompt-based debiasing provides a lightweight alternative to retraining for mitigating bias in LLMs by introducing
explicit instructions or balanced exemplars within the prompt [23, 41]. Recent work highlights its advantage for rapid
deployment but also reports mixed outcomes: while some interventions reduce stereotypical associations [26, 41],
others lead to superficial shifts or inconsistent effects across models and contexts [67]. These limitations underscore the
need for systematic evaluation. In this paper, we test debiasing prompts within the proposed PBA to assess whether
such interventions can meaningfully mitigate bias across multiple identity dimensions without retraining. Inspired
Manuscript submitted to ACM

--- Page 18 ---

18
Trovato et al.
Table 4. Impact of role-playing on PBA outcomes. For ICC(C,1), ICC(A,1), Spearman, and Kendall, higher values indicate stronger
agreement. For Severity Difference (SD), lower values indicate better consistency. For the paired t-test, p-values are reported; values
below 0.05 denote a statistically significant difference between original prompt and role-playing prompt.
ICC(C,1) (↑)
ICC(A,1) (↑)
Spearman (↑)
Kendall (↑)
SD ( (↓)
T-test
Name x Social Class
0.847
0.859
0.897
0.786
0.333
0.734
Name x Education
0.648
0.622
0.600
0.467
0.167
0.876
Name x Occupation
0.643
0.679
0.600
0.467
0.167
0.615
Name x Interest
0.821
0.728
0.943
0.867
0.167
0.965
Gender x Social Class
0.915
0.912
0.943
0.867
0.167
0.843
Gender x Education
0.745
0.726
0.371
0.333
0.000
0.869
Gender x Occupation
0.922
0.826
0.943
0.867
0.333
0.987
Gender x Interest
0.914
0.924
0.829
0.733
0.000
0.684
Ethnicity
x
Social
Class
0.844
0.702
0.943
0.867
0.167
0.984
Ethnicity
x
Educa-
tion
0.737
0.629
0.543
0.467
0.333
0.961
Ethnicity x Occupa-
tion
0.891
0.879
0.886
0.733
0.167
0.879
Ethnicity x Interest
0.968
0.882
0.829
0.733
0.167
0.997
Sexual Orientation x
Social Class
0.711
0.705
0.486
0.333
0.000
0.837
Sexual Orientation x
Education
0.126
0.113
-0.232
-0.138
0.000
0.880
Sexual Orientation x
Occupation
0.983
0.983
0.943
0.867
0.167
0.815
Sexual Orientation x
Interest
0.569
0.610
0.812
0.690
0.167
0.597
by previous studies [13, 26, 41], we introduced an additional debiasing instruction to the prompt: “Ensure the 20 user
profiles represent diversity in gender, age, ethnicity, socioeconomic background, abilities, and geographic regions. Avoid
stereotypes and keep descriptions neutral and inclusive”.
We apply the modified debiasing prompt to generate user profiles and use the same metrics as in the previous section
on agreements and statistical difference. Table 5 summarizes the findings. Overall, most agreement metrics (apart
from Kendall) show moderate or higher consistency (>0.40) across most bias dimensions. However, these values are
substantially lower than those reported in previous sections, indicating that introducing debiasing prompt increases
variability in PBA outcomes. Notably, dimensions such as Ethnicity X Interest and Sexual Orientation X Occupation
exhibit relatively high agreement, indicating robustness in these areas. In contrast, dimensions like Ethnicity X Education
and Sexual Orientation X Social Class show very low agreement, suggesting that debiasing prompts may influence how
bias manifests in these contexts.
Despite these variations, the Severity Difference remains low (mean SD = 0.31), implying that while model rankings
may shift, the overall severity of biased outcomes remain stable. Furthermore, t-test results reveal no statistically
significant improvements across any bias dimension (all p > 0.05), indicating that the debiasing prompt does not mitigate
bias in LLMs. These findings highlight the robustness of PBA and suggest that prompt-level interventions alone are
insufficient for meaningful bias reduction, underscoring the need for more systematic approaches beyond prompt
engineering.
Manuscript submitted to ACM

--- Page 19 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
19
Table 5. Impact of debiase prompt on PBA outcomes. For ICC(C,1), ICC(A,1), Spearman, and Kendall, higher values indicate stronger
agreement. For Severity Difference (SD), lower values indicate better consistency. For the paired t-test, p-values are reported; values
below 0.05 denote a statistically significant difference between original prompt and debiasing prompt.
ICC(C,1) (↑)
ICC(A,1) (↑)
Spearman (↑)
Kendall (↑)
SD ( (↓)
T-test
Name x Social Class
0.452
0.474
0.435
0.276
0.333
0.734
Name x Education
0.112
0.112
0.486
0.333
0.167
0.876
Name x Occupation
0.240
0.270
0.486
0.333
0.167
0.615
Name x Interest
0.540
0.561
0.543
0.467
0.333
0.965
Gender x Social Class
0.433
0.442
0.371
0.333
0.167
0.843
Gender x Education
0.450
0.352
0.543
0.467
0.167
0.869
Gender x Occupation
0.278
0.263
-0.029
-0.067
0.333
0.987
Gender x Interest
0.233
0.254
0.371
0.333
0.500
0.684
Ethnicity
x
Social
Class
0.471
0.314
0.371
0.333
0.500
0.984
Ethnicity
x
Educa-
tion
0.105
0.073
0.029
0.067
0.500
0.961
Ethnicity x Occupa-
tion
0.427
0.431
0.600
0.333
0.500
0.879
Ethnicity x Interest
0.828
0.844
0.714
0.467
0.333
0.997
Sexual Orientation x
Social Class
0.103
0.087
0.314
0.200
0.000
0.837
Sexual Orientation x
Education
0.174
0.076
0.174
0.138
0.167
0.880
Sexual Orientation x
Occupation
0.662
0.606
0.771
0.600
0.333
0.815
Sexual Orientation x
Interest
0.593
0.611
0.580
0.276
0.500
0.597
6
Discussion
6.1
Bias trajectories in creative applications
Our findings reveal that bias in LLM-generated personas is nonlinear, challenging the assumption that newer or larger
models are inherently fairer. Bias trajectories differ not only in magnitude but also in shape across models, even when
structural patterns remain stable. While early frontier models (e.g., GPT-4, GPT-4o) exhibit relatively compact bias
profiles, later generations such as GPT-4.1 and GPT-5 show increased variability and resurgence of certain biases,
particularly along name and ethnicity axes. Bias trajectories also differ by family and scale: smaller models sometimes
outperform larger ones in fairness. This suggests that fairness is not a monotonic function of scale or alignment but
emerges from complex interactions among training data, tuning strategies, and safety layers. For practitioners, this
means model upgrades should be treated as fairness risk events, requiring pre- and post-release audits rather than
assuming progress.
6.2
Implications and potential harms
Persistent gendered occupational stereotypes and non-binary funneling (identified in Section 4.3) pose significant risks
in downstream use cases. Male personas cluster in technical and manual roles, while female personas dominate care
and creative domains. Non-binary personas exhibit the narrowest occupational spread, often concentrated in Creative
Manuscript submitted to ACM

--- Page 20 ---

20
Trovato et al.
& Design or IT depending on model family. These allocation patterns risk normalizing exclusionary norms, shaping
how characters, roles, and narratives are constructed in downstream applications. The harms extend well beyond
representational imbalance. In synthetic data generation use cases, biased outputs can re-enter training pipelines and
amplify inequities over time. In high-stakes creative domains such as educational content or recruitment simulations,
these biases risk shaping user perceptions and influencing decision-making in subtle yet consequential ways.
6.3
From measurement to governance
PBA’s robustness and interpretability make it suitable for operational integration into deployment pipelines. It benefits
three main groups: model developers, model users, and policy makers and auditors.
• Model developers, who train and release LLMs, can use PBA to identify bias early and design mitigation strategies
before deployment. This includes adjusting training data, adding counterfactual examples, using reinforcement
learning or applying fairness constraints. Tracking bias across versions with longitudinal model cards makes
fairness a release criterion, not an afterthought.
• Model users, such as data scientists, marketing teams, and educators, can use PBA results in two ways. First, they
can select models with lower bias for sensitive tasks by comparing audit scores across versions. Second, they
can apply mitigation strategies informed by audit findings: adapting prompts to reduce stereotype activation,
filtering outputs, or rebalancing persona sets during post-processing.
• Policy makers and auditors gain interpretable metrics and reproducible outputs that support compliance and
certification. Normalized bias scores and documented changes across versions provide evidence for regulatory
frameworks and help enforce transparency standards.
To make these benefits practical, we propose three governance practices:
• Longitudinal Model Cards: Report normalized Cramér’s V scores for each dimension and track changes across
versions. Include differences from the previous release to highlight regressions.
• Establish explicit bias thresholds (e.g., normalized bias score < 1.0) that must be met before deployment. For
high-risk domains, enforce staged rollouts to mitigate potential harms.
• Green Auditing Protocols: PBA’s sample efficiency could potentially reduce compute overhead, but as model
ecosystems grow, sustainability must be a first-class concern. Once personas are generated for bias auditing,
they should be shared across teams or organizations. This avoids redundant generation, ensures consistency in
bias evaluation, and enables reproducible comparisons without incurring additional compute costs.
These practices align with AI governance frameworks emphasizing accountability, transparency, and sustainability.
They also position PBA as a practical tool for compliance and continuous monitoring, bridging the gap between research
metrics and real-world accountability.
6.4
Limitations and future directions
While PBA advances fairness auditing, several important limitations remain:
• Language and Cultural Scope: Our evaluation is English-only and focuses on models developed in the U.S. and
Europe, limiting cultural and linguistic coverage. Future work should include multilingual audits and models
from diverse regions to capture broader norms.
• Structured Output Constraints: PBA uses open-ended generation with structured output for comparability and
scalability, which may constrain natural language expression. This design ensures reproducibility but focuses on
Manuscript submitted to ACM

--- Page 21 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
21
associational bias in persona attributes rather than semantic framing or sentiment. Future work should explore
less restrictive formats and incorporate semantic and sentiment analysis.
• Prompt sensitivity: although we used a standardized protocol and tested PBA under variations on key factors
including sample size, role-playing prompt and debiase prompt, prompt framing remains an open challenge.
A more systematic study of diverse prompt styles is needed to understand how framing interacts with bias
detection and to develop guidelines for robust auditing.
• Multimodal Bias: PBA currently excludes multimodal outputs, where text-to-image or text-to-video generation
introduces other representational risks. Extending PBA to multimodal personas is a key direction for future
work.
7
Conclusions
This work introduced the Persona Brainstorm Audit (PBA), a scalable and interpretable metric for auditing bias in
LLM-generated personas. By moving beyond fixed identity categories, PBA surfaces multidimensional biases and
enables longitudinal tracking across model generations. Applying PBA to 12 state-of-the-art LLMs, we show that
bias trajectories are nonlinear and domain-specific, challenging assumptions that fairness improves with scale or
alignment. Our findings highlight persistent structural patterns such as gendered occupational stereotypes and non-
binary funneling, alongside unpredictable shifts across families and versions. These dynamics underscore the need for
continuous auditing, model-specific mitigation strategies, and governance mechanisms that translate measurement
into accountability. PBA’s robustness and extensibility make it a practical tool for fairness evaluation in creative AI
applications. With generative AI being increasingly adopted in real-world applications, bias and fairness must be treated
as an ongoing responsibility embedded in design, deployment, and policy.
References
[1] Ajwad Abrar, Nafisa Tabassum Oeshy, Mohsinul Kabir, and Sophia Ananiadou. 2025. Religious bias landscape in language and text-to-image models:
Analysis, detection, and debiasing strategies. arXiv preprint arXiv:2501.08441 (2025).
[2] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam
Altman, Shyamal Anadkat, et al. 2023. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).
[3] Afra Feyza Akyürek, Muhammed Yusuf Kocyigit, Sejin Paik, and Derry Tanti Wijaya. 2022. Challenges in Measuring Bias via Open-Ended
Language Generation. In Proceedings of the 4th Workshop on Gender Bias in Natural Language Processing (GeBNLP), Christian Hardmeier, Christine
Basta, Marta R. Costa-jussà, Gabriel Stanovsky, and Hila Gonen (Eds.). Association for Computational Linguistics, Seattle, Washington, 76–76.
doi:10.18653/v1/2022.gebnlp-1.9
[4] Danial Amin, Joni Salminen, Farhan Ahmed, Sonja MH Tervola, Sankalp Sethi, and Bernard J Jansen. 2025. How Is Generative AI Used for Persona
Development?: A Systematic Review of 52 Research Articles. arXiv preprint arXiv:2504.04927 (2025).
[5] Jiafu An, Difang Huang, Chen Lin, and Mingzhu Tai. 2025. Measuring gender and racial biases in large language models: Intersectional evidence
from automated resume evaluation. PNAS nexus 4, 3 (2025), pgaf089.
[6] Neeraj Arora, Ishita Chakraborty, and Yohei Nishimura. 2025. AI–human hybrids for marketing research: Leveraging large language models (LLMs)
as collaborators. Journal of Marketing 89, 2 (2025), 43–70.
[7] Mina Arzaghi, Florian Carichon, and Golnoosh Farnadi. 2024. Understanding intrinsic socioeconomic biases in large language models. In Proceedings
of the AAAI/ACM Conference on AI, Ethics, and Society, Vol. 7. 49–60.
[8] Yoav Benjamini and Daniel Yekutieli. 2001. The control of the false discovery rate in multiple testing under dependency. Annals of statistics (2001),
1165–1188.
[9] Su Lin Blodgett, Gilsinia Lopez, Alexandra Olteanu, Robert Sim, and Hanna Wallach. 2021. Stereotyping Norwegian salmon: An inventory of pitfalls
in fairness benchmark datasets. In Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International
Joint Conference on Natural Language Processing (Volume 1: Long Papers). 1004–1015.
[10] Tolga Bolukbasi, Kai-Wei Chang, James Y Zou, Venkatesh Saligrama, and Adam T Kalai. 2016. Man is to computer programmer as woman is to
homemaker? debiasing word embeddings. Advances in neural information processing systems 29 (2016).
Manuscript submitted to ACM

--- Page 22 ---

22
Trovato et al.
[11] Laura Cabello, Anna Katrine Jørgensen, and Anders Søgaard. 2023. On the independence of association bias and empirical fairness in language
models. In Proceedings of the 2023 ACM conference on fairness, accountability, and transparency. 370–378.
[12] Aylin Caliskan, Joanna J Bryson, and Arvind Narayanan. 2017. Semantics derived automatically from language corpora contain human-like biases.
Science 356, 6334 (2017), 183–186.
[13] Riccardo Cantini, Alessio Orsino, Massimo Ruggiero, and Domenico Talia. 2025. Benchmarking adversarial robustness to bias elicitation in large
language models: Scalable automated assessment with llm-as-a-judge. arXiv preprint arXiv:2504.07887 (2025).
[14] Hongliu Cao. 2024. Recent advances in text embedding: A Comprehensive Review of Top-Performing Methods on the MTEB Benchmark. arXiv
preprint arXiv:2406.01607 (2024).
[15] Hongliu Cao. 2025. Writing style matters: An examination of bias and fairness in information retrieval systems. In Proceedings of the Eighteenth
ACM International Conference on Web Search and Data Mining. 336–344.
[16] Shuirong Cao, Ruoxi Cheng, and Zhiqiang Wang. 2025. Agr: Age group fairness reward for bias mitigation in llms. In ICASSP 2025-2025 IEEE
International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 1–5.
[17] Zhibo Chu, Zichong Wang, and Wenbin Zhang. 2024. Fairness in large language models: A taxonomic survey. ACM SIGKDD explorations newsletter
26, 1 (2024), 34–48.
[18] Harald Cramér. 1999. Mathematical methods of statistics. Vol. 9. Princeton university press.
[19] Aida Davani, Sunipa Dev, Héctor Pérez-Urbina, and Vinodkumar Prabhakaran. 2025. A Comprehensive Framework to Operationalize Social
Stereotypes for Responsible AI Evaluations. arXiv preprint arXiv:2501.02074 (2025).
[20] Pieter Delobelle, Ewoenam Kwaku Tokpo, Toon Calders, and Bettina Berendt. 2022. Measuring fairness with biased rulers: A comparative study on
bias metrics for pre-trained language models. In Proceedings of the 2022 Conference of the North American chapter of the association for computational
linguistics. Association for Computational Linguistics, 1693–1706.
[21] Sunipa Dev, Masoud Monajatipoor, Anaelia Ovalle, Arjun Subramonian, Jeff Phillips, and Kai-Wei Chang. 2021. Harms of Gender Exclusivity and
Challenges in Non-Binary Representation in Language Technologies. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language
Processing, Marie-Francine Moens, Xuanjing Huang, Lucia Specia, and Scott Wen-tau Yih (Eds.). Association for Computational Linguistics, Online
and Punta Cana, Dominican Republic, 1968–1994. doi:10.18653/v1/2021.emnlp-main.150
[22] Jwala Dhamala, Tony Sun, Varun Kumar, Satyapriya Krishna, Yada Pruksachatkun, Kai-Wei Chang, and Rahul Gupta. 2021. Bold: Dataset and metrics
for measuring biases in open-ended language generation. In Proceedings of the 2021 ACM conference on fairness, accountability, and transparency.
862–872.
[23] Jessica Maria Echterhoff, Yao Liu, Abeer Alessa, Julian McAuley, and Zexue He. 2024. Cognitive Bias in Decision-Making with LLMs. In Findings of the
Association for Computational Linguistics: EMNLP 2024, Yaser Al-Onaizan, Mohit Bansal, and Yun-Nung Chen (Eds.). Association for Computational
Linguistics, Miami, Florida, USA, 12640–12653. doi:10.18653/v1/2024.findings-emnlp.739
[24] Virginia K Felkner, Ho-Chun Herbert Chang, Eugene Jang, and Jonathan May. 2023. Winoqueer: A community-in-the-loop benchmark for anti-lgbtq+
bias in large language models. arXiv preprint arXiv:2306.15087 (2023).
[25] Kazuma Fukumura and Takayuki Ito. 2025. Can LLM-Powered Multi-Agent Systems Augment Human Creativity? Evidence from Brainstorming
Tasks. In Proceedings of the ACM Collective Intelligence Conference. 20–29.
[26] A. Furniturewala et al. 2024. Thinking Fair and Slow: On the Efficacy of Structured Prompts for Debiasing Language Models. In Proceedings of
EMNLP.
[27] Isabel O Gallegos, Ryan A Rossi, Joe Barrow, Md Mehrab Tanjim, Sungchul Kim, Franck Dernoncourt, Tong Yu, Ruiyi Zhang, and Nesreen K Ahmed.
2024. Bias and fairness in large language models: A survey. Computational Linguistics 50, 3 (2024), 1097–1179.
[28] Nikhil Garg, Londa Schiebinger, Dan Jurafsky, and James Zou. 2018. Word embeddings quantify 100 years of gender and ethnic stereotypes.
Proceedings of the National Academy of Sciences 115, 16 (2018), E3635–E3644.
[29] Samuel Gehman, Suchin Gururangan, Maarten Sap, Yejin Choi, and Noah A. Smith. 2020. RealToxicityPrompts: Evaluating Neural Toxic Degeneration
in Language Models. In Findings of the Association for Computational Linguistics: EMNLP 2020, Trevor Cohn, Yulan He, and Yang Liu (Eds.). Association
for Computational Linguistics, Online, 3356–3369. doi:10.18653/v1/2020.findings-emnlp.301
[30] Katy Ilonka Gero, Tao Long, and Lydia B Chilton. 2023. Social dynamics of AI support in creative writing. In Proceedings of the 2023 CHI conference
on human factors in computing systems. 1–15.
[31] Kate Glazko, Yusuf Mohammed, Ben Kosa, Venkatesh Potluri, and Jennifer Mankoff. 2024. Identifying and improving disability bias in GPT-based
resume screening. In Proceedings of the 2024 ACM Conference on Fairness, Accountability, and Transparency. 687–700.
[32] Yufei Guo, Muzhe Guo, Juntao Su, Zhou Yang, Mengqiu Zhu, Hongfei Li, Mengyang Qiu, and Shuo Shuo Liu. 2024. Bias in large language models:
Origin, evaluation, and mitigation. arXiv preprint arXiv:2411.10915 (2024).
[33] Farsheed Haque, Depeng Xu, and Xi Niu. 2025. A Comprehensive Survey on Bias and Fairness in Large Language Models. In Pacific-Asia Conference
on Knowledge Discovery and Data Mining. Springer, 83–101.
[34] Kai He, Yucheng Huang, Wenqing Wang, Delong Ran, Dongming Sheng, Junxuan Huang, Qika Lin, Jiaxing Xu, Wenqiang Liu, and Mengling Feng.
2025. Crab: A Novel Configurable Role-Playing LLM with Assessing Benchmark. In Proceedings of the 63rd Annual Meeting of the Association
for Computational Linguistics (Volume 1: Long Papers), Wanxiang Che, Joyce Nabende, Ekaterina Shutova, and Mohammad Taher Pilehvar (Eds.).
Association for Computational Linguistics, Vienna, Austria, 15030–15052. doi:10.18653/v1/2025.acl-long.731
Manuscript submitted to ACM

--- Page 23 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
23
[35] Yue Huang, Qihui Zhang, Lichao Sun, et al. 2023. Trustgpt: A benchmark for trustworthy and responsible large language models. arXiv preprint
arXiv:2306.11507 (2023).
[36] Maurice G Kendall. 1945. The treatment of ties in ranking problems. Biometrika 33, 3 (1945), 239–251.
[37] Hae-Young Kim. 2017. Statistical notes for clinical researchers: Chi-squared test and Fisher’s exact test. Restorative dentistry & endodontics 42, 2
(2017), 152.
[38] Aobo Kong, Shiwan Zhao, Hao Chen, Qicheng Li, Yong Qin, Ruiqi Sun, Xin Zhou, Enzhi Wang, and Xiaohang Dong. 2023. Better Zero-Shot
Reasoning with Role-Play Prompting. arXiv preprint arXiv:2308.07702 (2023). doi:10.48550/arXiv.2308.07702
[39] Ang Li, Haozhe Chen, Hongseok Namkoong, and Tianyi Peng. 2025. LLM Generated Persona is a Promise with a Catch. arXiv preprint arXiv:2503.16527
(2025).
[40] Tao Li, Daniel Khashabi, Tushar Khot, Ashish Sabharwal, and Vivek Srikumar. 2020. UNQOVERing Stereotyping Biases via Underspecified Questions.
In Findings of the Association for Computational Linguistics: EMNLP 2020, Trevor Cohn, Yulan He, and Yang Liu (Eds.). Association for Computational
Linguistics, Online, 3475–3489. doi:10.18653/v1/2020.findings-emnlp.311
[41] X. Li et al. 2024. Prompting Fairness: Integrating Causality to Debias Large Language Models. arXiv preprint arXiv:2401.12345 (2024).
[42] David Liljequist, Britt Elfving, and Kirsti Skavberg Roaldsen. 2019. Intraclass correlation–A discussion and demonstration of basic features. PloS one
14, 7 (2019), e0219854.
[43] David Chuan-En Lin and Nikolas Martelaro. 2024. Jigsaw: Supporting designers to prototype multimodal applications by chaining AI foundation
models. In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems. 1–15.
[44] Chandler May, Alex Wang, Shikha Bordia, Samuel R. Bowman, and Rachel Rudinger. 2019. On Measuring Social Biases in Sentence Encoders. In
Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies,
Volume 1 (Long and Short Papers), Jill Burstein, Christy Doran, and Thamar Solorio (Eds.). Association for Computational Linguistics, Minneapolis,
Minnesota, 622–628. doi:10.18653/v1/N19-1063
[45] Kenneth O McGraw and S P Wong. 1996. Forming inferences about some intraclass correlation coefficients. Psychological Methods 1, 1 (1996), 30–46.
[46] Katelyn Mei, Sonia Fereidooni, and Aylin Caliskan. 2023. Bias against 93 stigmatized groups in masked language models and downstream sentiment
classification tasks. In Proceedings of the 2023 ACM Conference on Fairness, Accountability, and Transparency. 1699–1710.
[47] Imran Mirza, Akbar Anbar Jafari, Cagri Ozcinar, and Gholamreza Anbarjafari. 2025. Gender bias analysis for different large language models. (2025).
[48] Marzieh Mozafari, Reza Farahbakhsh, and Noël Crespi. 2020. Hate speech detection and racial bias mitigation in social media based on BERT model.
PloS one 15, 8 (2020), e0237861.
[49] Debora Nozza, Federico Bianchi, Dirk Hovy, et al. 2021. HONEST: Measuring hurtful sentence completion in language models. In Proceedings of
the 2021 conference of the North American chapter of the association for computational linguistics: Human language technologies. Association for
Computational Linguistics.
[50] OpenAI. 2023. GPT-4 Technical Report. https://openai.com/index/gpt-4-research/. Accessed: 2025-09-01.
[51] OpenAI. 2024. Hello GPT-4o. https://openai.com/index/hello-gpt-4o/.
[52] OpenAI. 2025. Introducing GPT-4.1 in the API. https://openai.com/index/gpt-4-1/.
[53] OpenAI. 2025. Introducing GPT-5. https://openai.com/index/introducing-gpt-5/.
[54] Rock Yuren Pang, Hope Schroeder, Kynnedy Simone Smith, Solon Barocas, Ziang Xiao, Emily Tseng, and Danielle Bragg. 2025. Understanding the
LLM-ification of CHI: Unpacking the Impact of LLMs at CHI through a Systematic Literature Review. In Proceedings of the 2025 CHI Conference on
Human Factors in Computing Systems. 1–20.
[55] Alicia Parrish, Angelica Chen, Nikita Nangia, Vishakh Padmakumar, Jason Phang, Jana Thompson, Phu Mon Htut, and Samuel Bowman. 2022. BBQ: A
hand-built bias benchmark for question answering. In Findings of the Association for Computational Linguistics: ACL 2022, Smaranda Muresan, Preslav
Nakov, and Aline Villavicencio (Eds.). Association for Computational Linguistics, Dublin, Ireland, 2086–2105. doi:10.18653/v1/2022.findings-acl.165
[56] Joni Salminen, Chang Liu, Wenjing Pian, Jianxing Chi, Essi Häyhänen, and Bernard J Jansen. 2024. Deus ex machina and personas from large
language models: Investigating the composition of ai-generated persona descriptions. In Proceedings of the 2024 CHI Conference on Human Factors in
Computing Systems. 1–20.
[57] Nithya Sambasivan, Erin Arnesen, Ben Hutchinson, Tulsee Doshi, and Vinodkumar Prabhakaran. 2021. Re-imagining algorithmic fairness in india
and beyond. In Proceedings of the 2021 ACM conference on fairness, accountability, and transparency. 315–328.
[58] Maarten Sap, Dallas Card, Saadia Gabriel, Yejin Choi, and Noah A Smith. 2019. The risk of racial bias in hate speech detection. In Proceedings of the
57th annual meeting of the association for computational linguistics. 1668–1678.
[59] Patrick Schober, Christa Boer, and Lothar A Schwarte. 2018. Correlation coefficients: Appropriate use and interpretation. Anesthesia & Analgesia
126, 5 (2018), 1763–1768.
[60] Sankalp Sethi, Joni Salminen, Danial Amin, and Bernard J Jansen. 2025. " When AI Writes Personas": Analyzing Lexical Diversity in LLM-Generated
Persona Descriptions. In Proceedings of the Extended Abstracts of the CHI Conference on Human Factors in Computing Systems. 1–8.
[61] Renee Shelby, Shalaleh Rismani, Kathryn Henne, AJung Moon, Negar Rostamzadeh, Paul Nicholas, N’Mah Yilla-Akbari, Jess Gallegos, Andrew
Smart, Emilio Garcia, et al. 2023. Sociotechnical harms of algorithmic systems: Scoping a taxonomy for harm reduction. In Proceedings of the 2023
AAAI/ACM Conference on AI, Ethics, and Society. 723–741.
[62] Shijing Si, Xiaoming Jiang, Qinliang Su, and Lawrence Carin. 2025. Detecting implicit biases of large language models with Bayesian hypothesis
testing. Scientific Reports 15, 1 (2025), 12415.
Manuscript submitted to ACM

--- Page 24 ---

24
Trovato et al.
[63] Tony Sun, Andrew Gaut, Shirlyn Tang, Yuxin Huang, Mai ElSherief, Jieyu Zhao, Diba Mirza, Elizabeth Belding, Kai-Wei Chang, and William Yang
Wang. 2019. Mitigating gender bias in natural language processing: Literature review. arXiv preprint arXiv:1906.08976 (2019).
[64] Yu-Min Tseng, Yu-Chao Huang, Teng-Yun Hsiao, Wei-Lin Chen, Chao-Wei Huang, Yu Meng, and Yun-Nung Chen. 2024. Two Tales of Persona in LLMs:
A Survey of Role-Playing and Personalization. In Findings of the Association for Computational Linguistics: EMNLP 2024, Yaser Al-Onaizan, Mohit
Bansal, and Yun-Nung Chen (Eds.). Association for Computational Linguistics, Miami, Florida, USA, 16612–16631. doi:10.18653/v1/2024.findings-
emnlp.969
[65] Noah Wang, Z.y. Peng, Haoran Que, Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu, Hongcheng Guo, Ruitong Gan, Zehao Ni, Jian Yang, Man Zhang,
Zhaoxiang Zhang, Wanli Ouyang, Ke Xu, Wenhao Huang, Jie Fu, and Junran Peng. 2024. RoleLLM: Benchmarking, Eliciting, and Enhancing
Role-Playing Abilities of Large Language Models. In Findings of the Association for Computational Linguistics: ACL 2024, Lun-Wei Ku, Andre Martins,
and Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand, 14743–14777. doi:10.18653/v1/2024.findings-acl.878
[66] Shansong Wang, Mingzhe Hu, Qiang Li, Mojtaba Safari, and Xiaofeng Yang. 2025. Capabilities of GPT-5 on Multimodal Medical Reasoning. arXiv
preprint arXiv:2508.08224 (2025).
[67] Xinyi Yang, Runzhe Zhan, Derek F Wong, Shu Yang, Junchao Wu, and Lidia S Chao. 2025. Rethinking Prompt-based Debiasing in Large Language
Models. arXiv preprint arXiv:2503.09219 (2025).
[68] Abdelrahman Zayed, Goncalo Mordido, Ioana Baldini, and Sarath Chandar. 2024. Why Don’t Prompt-Based Fairness Metrics Correlate?. In
Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), Lun-Wei Ku, Andre Martins, and
Vivek Srikumar (Eds.). Association for Computational Linguistics, Bangkok, Thailand, 9002–9019. doi:10.18653/v1/2024.acl-long.487
A
Glossary
This glossary provides definitions of acronyms and abbreviations used throughout the paper for quick reference:
• AI – Artificial Intelligence
• API – Application Programming Interface
• ACL – Association for Computational Linguistics
• CHI – Conference on Human Factors in Computing Systems
• HCI – Human-Computer Interaction
• ICC – Intraclass Correlation Coefficient
• JSON – JavaScript Object Notation
• LLM – Large Language Model
• MTEB – Massive Text Embedding Benchmark
• NLP – Natural Language Processing
• PBA – Persona Brainstorm Audit
• QA – Question Answering
• SD – Severity Difference
• SEAT – Sentence Encoder Association Test
• UX – User Experience
• WEAT – Word Embedding Association Test
B
Supporting data
B.1
Cardinality Comparison Across Models
To provide transparency and support reproducibility, we include detailed statistics and visualizations of the data
processing pipeline and bias analysis results.
Manuscript submitted to ACM

--- Page 25 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
25
Table 6. Comparison of cardinalities among LLMs for different attributes
gender
ethnicity
sexual orientation
social class
education level
occupation
top personal interest
GPT-3.5
5
42
15
32
100
297
374
GPT-4
15
72
16
31
107
519
490
GPT-4o
5
57
14
23
85
334
368
GPT-4.1 nano
3
120
19
31
101
491
1445
GPT-4.1 mini
5
68
11
20
72
344
662
GPT-4.1
16
194
20
17
108
670
700
GPT-5 nano
7
147
12
31
199
906
2917
GPT-5 mini
34
713
23
100
482
1977
3885
GPT-5
23
1128
11
34
689
1384
1501
Ministral-3B
3
50
11
20
19
115
126
Mistral-small
9
38
12
16
19
172
307
Mistral-medium
3
18
7
11
13
136
211
Post-processing
3
6
5
3
5
18
15
Table 6 reports the raw cardinalities of key persona attributes (gender, ethnicity, sexual orientation, social class,
education level, occupation, and personal interests) for all 12 LLMs prior to normalization, alongside the reduced
cardinalities after post-processing. These results highlight the substantial variability in attribute diversity across models.
Such variability underscores the necessity of semantic consolidation for meaningful cross-model comparison. Post-
processing reduces cardinalities to a minimal, non-redundant set, ensuring statistical robustness and interpretability.
Note: For name-based bias evaluation, we analyze the top 50 most frequent names across all models. This choice ensures
statistical reliability by avoiding sparsity, supports cross-model comparability by focusing on shared categories, and
maintains interpretability while remaining scalable. Using frequent names provides a robust and representative basis
for bias detection without introducing noise from rare or model-specific outliers.
B.2
Duplicate Profile Analysis
Table 7 summarizes duplicate counts across 10,000 generated profiles per model. Duplication rates vary significantly,
from 3 duplicates for GPT-5 to over 2,000 for Mistral-medium. This finding motivated the inclusion of a deduplication
step in our pipeline to mitigate skew and ensure fairness in comparative analysis.
Model
Dup.
Model
Dup.
Model
Dup.
Model
Dup.
GPT3.5
63
GPT4.1
19
GPT5
3
Mistral-medium
2060
GPT4
33
GPT4.1 mini
246
GPT5mini
37
Mistral-small
443
GPT4o
11
GPT4.1 nano
81
GPT5nano
6
Ministral3B
776
Table 7. Duplicate counts across 12 LLMs for 10 000 persona profiles generated
B.3
Bias Visualization Across Dimensions
Figure 6 presents radar charts comparing bias levels across 16 dimensions for 12 LLMs (the corresponding numerical
results are provided in Table 2). The models are grouped into four subplots for readability: GPT-3.5, GPT-4, and GPT-
4o (top-left); GPT-4.1 series (top-right); GPT-5 series (bottom-left); and Mistral models (bottom-right). Each subplot
visualizes bias scores for three models, with each axis representing a distinct identity-social dimension pair. Bias severity
is color-coded using a perceptually accessible palette: low (gray), medium (amber), high (red), and very high (dark red).
To support colorblind accessibility, models are further distinguished using unique line styles and markers. The average
bias scores of each model series are shown in the title of each subplot.
LLMs with more compact polygonal profiles exhibit lower overall bias. From Figure 6, it can be seen that GPT-4o
exhibits the most compact profile, followed by Ministral-3B and GPT-4. GPT-4.1 mini and GPT-5 display broader,
Manuscript submitted to ACM

--- Page 26 ---

26
Trovato et al.
Fig. 6. Radar chart comparing bias levels across 16 bias dimensions for 12 LLMs, including GPT-3.5, GPT-4, GPT-4o (top-left subplot),
GPT-4.1 series (top-right subplot), GPT-5 series (bottom-left subplot), and Mistral models (bottom-right subplot). Each subplot
displays three models, with bias measured across intersections of identity axes (name, gender, ethnicity, sexual orientation) and
social dimensions (social class, education, occupation, interest). The average bias scores of each model series are shown in the title of
each subplot. Bias severity is color-coded: low (gray), medium (amber), high (red), and very high (dark red). Line styles and markers
distinguish models for accessibility.
irregular polygons with pronounced spikes, indicating higher bias and greater cross-dimension variability. Severity
levels show clear regimes. GPT-4o has 1 very high, 8 high, 5 medium, and 2 low bias dimensions. GPT-5 has 9 very high
and no low bias dimensions. The middle group includes GPT-4.1, GPT-4.1 nano, Mistral Small, and Mistral Medium.
Each has 5 to 8 very high bias dimensions.
Analysis by model family shows distinct patterns of bias across generations of LLMs. For each subplot in Figure 6,
the average bias score for each model series is displayed in the subplot title. OpenAI early frontier models (including
GPT-3.5, GPT-4, and GPT-4o) have the lowest average bias scores. The Mistral series shows slightly higher averages. In
contrast, the most recent OpenAI series, GPT-4.1 series and GPT-5 series, have the highest average bias scores. Within
the GPT-4.1 series, the largest model GPT-4.1 has the lowest bias score. However, within the GPT-5 series, the smallest
model GPT-5 nano has the lowest bias score. The Mistral family shows a similar pattern as GPT-5 series: the smallest
Manuscript submitted to ACM

--- Page 27 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
27
model Ministral-3B has the lowest bias score. These findings reveal that bias trajectories in LLMs are neither linear
nor uniform: lineage and scale interact in complex ways, producing structurally heterogeneous profiles where the
magnitude and concentration of biases vary sharply across dimensions. This underscores that mitigating bias requires
model-specific strategies rather than assumptions of steady progress across generations or model sizes.
B.4
Gender X Occupation analysis
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Engineering
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Driver
Student
Professor
4
15
9
3
9
6
4
7
12
6
10
3
9
7
8
16
0
1
7
2
0
14
6
4
2
4
10
12
17
29
4
8
1
7
0
0
4
9
13
7
6
4
GPT-3.5
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Engineering
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Student
Professor
4
11
6
5
7
5
9
11
8
12
10
7
9
4
4
8
0
1
12
4
1
10
7
3
1
4
6
13
17
29
2
7
1
9
12
24
8
6
4
GPT-4
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Skilled Worker
Hospitality & Retail
Teacher
Business & Finance
Creative & Design
Healthcare
Legal & Public Safety
Student
Engineering
Professor
2
8
3
5
12
6
8
8
13
8
6
10
10
0
0
8
6
9
2
8
1
13
6
2
11
17
37
3
13
0
5
4
1
4
7
10
12
2
0
8
4
10
GPT-4o
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Teacher
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Legal & Public Safety
Student
Engineering
Professor
1
5
2
9
12
3
11
11
20
11
9
19
11
4
0
7
0
0
3
4
0
13
3
2
1
5
0
8
20
22
1
6
0
4
4
0
2
13
31
7
1
0
12
3
2
GPT-4.1 nano
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Engineering
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Driver
Student
Professor
3
7
4
6
12
5
4
10
14
6
13
15
10
5
5
11
0
0
10
2
1
13
3
1
1
5
9
13
15
27
2
10
0
7
0
0
6
12
18
7
5
2
GPT-4.1 mini
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Engineering
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Driver
Legal & Public Safety
Student
Professor
2
5
2
4
8
7
6
7
5
8
11
13
12
6
20
8
0
0
7
7
0
11
7
0
1
4
4
9
18
24
1
11
0
11
0
0
3
1
0
10
10
21
7
5
4
GPT-4.1
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Teacher
Engineering
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Student
Professor
3
5
1
1
5
3
6
8
9
21
23
32
9
5
5
7
5
1
12
2
1
7
2
2
1
2
2
13
20
21
1
6
1
7
10
18
13
6
5
GPT-5 nano
male
female
non-binary
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Engineering
Teacher
Social Impact & Nonprofit
Creative & Design
Healthcare
Legal & Public Safety
Driver
Student
Professor
2
7
5
4
7
3
21
18
41
11
4
4
14
1
2
11
5
1
10
2
1
2
12
7
9
19
23
1
13
1
1
4
2
7
0
0
3
5
9
3
3
1
GPT-5 mini
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Teacher
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Driver
Student
Engineering
Professor
1
3
2
3
7
4
2
5
3
16
20
35
10
5
9
18
2
3
4
3
0
8
6
0
1
7
13
10
18
21
1
9
1
6
0
0
1
3
6
15
9
2
4
2
1
GPT-5
male
female
non-binary
Marketing & HR
Science & Research
IT & Software
Skilled Worker
Hospitality & Retail
Teacher
Creative & Design
Healthcare
Legal & Public Safety
Student
Engineering
Professor
2
13
2
5
6
2
10
7
25
13
0
0
6
4
7
12
14
5
9
11
45
7
24
5
5
4
2
4
5
5
17
6
0
9
6
2
Ministral-3B
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Teacher
Business & Finance
Social Impact & Nonprofit
Creative & Design
Healthcare
Legal & Public Safety
Student
Engineering
Professor
3
10
6
3
10
11
4
5
8
7
7
17
8
4
3
7
0
1
6
6
2
14
1
1
0
3
7
14
16
25
8
19
6
5
7
1
3
4
4
11
2
2
7
6
6
Mistral-small
male
female
non-binary
Marketing & HR
Media & Publishing
Science & Research
IT & Software
Hospitality & Retail
Skilled Worker
Teacher
Business & Finance
Engineering
Social Impact & Nonprofit
Creative & Design
Healthcare
Legal & Public Safety
Student
Professor
4
11
4
4
8
0
7
10
0
4
3
4
11
3
15
7
0
0
3
5
1
17
3
0
10
2
0
1
7
6
9
18
57
4
16
0
7
5
0
5
7
6
8
3
6
 Mistral-medium
0
5
10
15
20
25
0
5
10
15
20
25
0
5
10
15
20
25
30
35
0
5
10
15
20
25
30
0
5
10
15
20
25
0
5
10
15
20
5
10
15
20
25
30
0
5
10
15
20
25
30
35
40
0
5
10
15
20
25
30
35
0
5
10
15
20
25
30
35
40
45
0
5
10
15
20
25
0
10
20
30
40
50
Fig. 7. Heatmaps of Gender–Occupation distributions for 12 LLMs . Each subplot corresponds to one model. To facilitate the
comparison while focusing on high-mass roles, only top 10 most popular occupations of each gender are selected for each LLM. Each
cell is the percentage of that gender assigned to a given occupation (columns sum = 100% per gender, within model).
To examine how stereotypes manifest across models, we focus on a high-impact dimension: Gender X Occupation.
This choice is informed by prior analyses showing that occupational roles are among the strongest correlates of overall
bias severity, making them a critical focal point for representational and allocational harms in creative applications. We
visualize in Figure 7 the Gender–Occupation distributions for 12 LLMs using heatmaps, with each subplot representing
one model. To enable meaningful comparison while emphasizing high-frequency roles, we visualize only the top 10
occupations per gender for each model in Figure 7. Each cell indicates the percentage of a given gender assigned to an
occupation (columns sum to 100% per gender within each model).
Across all twelve models, gendered occupational stereotypes share some common patterns. Male personas are
repeatedly funneled into technical and manual roles such as Engineering, Skilled Worker, Business & Finance, and Driver
Manuscript submitted to ACM

--- Page 28 ---

28
Trovato et al.
(where present). Female personas cluster in creative and care-oriented roles, notably Creative & Design, Healthcare,
Marketing & HR, and Media & Publishing. Non-binary personas show the narrowest distribution, dominated by Creative
& Design in most models, with a growing shift toward IT & Software in the GPT-5 family. These patterns indicate that
gendered differentiation is driven less by hierarchical status (e.g., Gender X Social Class remains low–medium bias level
shown in Table 2) and more by domain-specific associations.
Despite this structural stability, the severity and shape of these biases differ substantially across models. Parity
between male and female allocations measured by the L1 gap (the sum of the absolute differences between male and
female across all occupations) ranges from 54 in GPT-4 and GPT-5 nano (most balanced) to 90 in Mistral-medium (least
balanced).
Despite structural stability, the severity and distribution of biases vary substantially across models. We quantify
gender parity between male and female allocations using the L1 gap, defined as the sum of absolute differences between
male and female allocations across all occupations:
L1 =
𝑛
∑︁
𝑖=1
|male𝑖−female𝑖|
(2)
where 𝑛is the number of occupations, male_i and female_i denote the percentage of male and female allocations for
occupation 𝑖. Higher L1 gap values indicate greater imbalance between genders across occupations. This metric ranges
from 54 in GPT-4 and GPT-5 nano (most balanced) to 90 in Mistral-medium (least balanced).
GPT-4.1 stands out for achieving near parity in Engineering (7% male vs. 7% female) and elevating female and non-
binary presence in IT. Despite strong overall fairness scores, GPT-4o retains classic male-coded spikes in Engineering
and Business & Finance as well as female-coded spikes in Creative & Design and Healthcare. The GPT-5 series introduces
a notable shift: non-binary personas move away from creative dominance toward IT, with GPT-5 mini assigning 41%
of non-binary personas to IT & Software. In contrast, the Mistral family shows increasing creative concentration. In
Mistral-medium, a single category (Creative & Design) accounts for 57% of non-binary allocations and the top two
categories cover 72%, indicating extreme funneling.
Family-level trends underscore that bias trajectories are neither linear nor monotonic. The GPT-5 family demonstrates
internal heterogeneity: GPT-5 nano matches GPT-4 in parity between male and female, while GPT-5 mini degrades
sharply, combining weak parity with the strongest IT funneling for non-binary personas. The Mistral family, by contrast,
shows consistent creative dominance for non-binary personas, with parity deteriorating as model size increases. These
divergences highlight that fairness does not scale predictably with model size or generation.
B.5
Zoom in analysis
The proposed PBA enables smooth transitions from coarse-grained to fine-grained views by preserving mappings to
original terms. After above global analysis of Gender X Occupation, which revealed persistent stereotypes on women
in creative and care-oriented domains, we zoom into Healthcare to examine the occupation nurse.
Table 8 shows gender distribution for nurse across 12 LLMs. Female representation exceeds 90% in nearly all models,
with GPT-5 reaching the highest male share (12.02%) and GPT-4.1 nano assigning the role exclusively to women.
Non-binary identities remain marginal, never surpassing 3.38%. This example illustrates PBA’s scalability: analysts can
move from systemic patterns to occupation-level scrutiny without redesigning the pipeline. Such flexibility is essential
for fairness auditing, where biases often surface at different levels of granularity.
Manuscript submitted to ACM

--- Page 29 ---

When LLMs Imagine People: A Human-Centered Persona Brainstorm Audit for Bias and Fairness in Creative
Applications
29
Table 8. Zoom in analysis into Healthcare domain: the gender distribution of nurse occupation across 12 LLMs (each row sums to
100%).
male
female
non-binary
GPT-3.5
4.76
95.24
0.00
GPT-4
3.07
96.93
0.00
GPT-4o
2.06
97.94
0.00
GPT-4.1 nano
0.00
100.00
0.00
GPT-4.1 mini
1.56
98.44
0.00
GPT-4.1
2.27
97.41
0.32
GPT-5 nano
5.58
93.40
1.02
GPT-5 mini
6.51
91.63
1.86
GPT-5
12.02
85.79
2.19
Ministral-3B
3.56
96.44
0.00
Mistral-small
0.80
95.83
3.38
Mistral-medium
9.37
90.63
0.00
B.6
Human Validation Study
To validate whether higher bias severity indicated by normalized Cramér’s V scores corresponds to greater potential harm,
we conducted a comparative human evaluation on the Gender X Occupation dimension. This dimension was selected
because occupational stereotypes are well-documented and have tangible implications for creative and workplace
contexts. We sampled persona distributions from two LLM variants: System 1 (GPT-5 mini with a bias score of 1.134,
very high bias) and System 2 (GPT-5 nano with a bias score of 0.779, lower end of high bias). For each model, we
aggregated 10,000 generated personas and visualized job distributions by gender across occupational categories. Charts
were anonymized and presented as “System 1” and “System 2” to avoid brand or order effects.
Participants: 9 evaluators from diverse professional backgrounds (including both DEI experts and non-DEI experts)
were recruited to approximate general stakeholder perspectives. Each participant received a concise guideline explaining
what patterns to look for (e.g., clustering, coverage, role diversity). They were asked to compare the two systems, assign
a Bias Severity Rating, justify their choice, and list the most harmful stereotypes observed.
Bias Severity Rating: Using the 1–4 scale aligned with our paper:
• 1 = Low Bias (balanced representation, minimal stereotypes).
• 2 = Moderate Bias (some clustering, mild stereotypes).
• 3 = High Bias (clear clustering, multiple stereotypes).
• 4 = Very High Bias (strong clustering, harmful stereotypes, poor coverage).
Table 9 summarizes the results of our exploratory human validation. Across all participants, System 1 was consis-
tently judged as more biased than System 2, with severity ratings clustering at 3–4 for System 1 and 2–3 for System 2.
Justifications highlight recurring concerns: System 1 exhibits pronounced gender-role segregation, extreme concen-
tration for non-binary personas, and reinforcement of traditional stereotypes (e.g., men in technical roles, women in
caregiving and creative domains). Several participants noted potential downstream harms, such as influencing career
recommendations if these distributions were surfaced in interactive systems. While System 2 demonstrates similar
tendencies, its distributions are comparatively less polarized, suggesting that lower Cramér’s V scores correspond to
reduced perceived harm. These findings provide preliminary evidence that normalized Cramér’s V indeed corresponds
to harmful stereotypes and aligns with human judgments of bias severity.
Limitations: This study serves as an exploratory initiative rather than a definitive validation of bias metrics. Its
scope is constrained by a small participant pool, a single bias dimension (Gender X Occupation), and a simplified
evaluation protocol that does not capture intersectional or cultural nuances. These constraints highlight that validating
Manuscript submitted to ACM

--- Page 30 ---

30
Trovato et al.
Table 9. Human validation results: bias severity ratings and justifications
Evaluator
System 1
System 2
Justification
Candidate 1
3
2
System 1 presents less equal opportunities among genders (es-
pecially for engineering, skilled worker, creative jobs); females
mostly associated with creative or collaborative roles, males
mostly technical.
Candidate 2
4
3
Extreme concentration for non-binary personas; reinforcement
of traditional stereotypes without meaningful diversity in Sys-
tem 1.
Candidate 3
4
3
System 1 has unequal opportunities across genders; may impact
career choice if present in chatbot recommending careers.
Candidate 4
3
2
High concentration of certain jobs for each gender in System 1,
especially for non-binary; lacks diversity.
Candidate 5
3
2
Larger gap between distributions in System 1 (e.g., Creative &
Design, Skilled Worker, Driver in male vs female); Social Impact
and Non-profit overrepresented for females.
Candidate 6
4
3
System 1 is more biased as: males do technical jobs; females
healthcare and NGOs; non-binary mainly IT or creative design
(highly clustered).
Candidate 7
4
3
Non-binary personas have very low opportunities apart from
IT and Creative roles in System 1.
Candidate 8
4
3
In System 1, men are mainly associated to technical/manual
roles. while women are more linked to creative and caregiving
roles. For non-binary, there is almost exclusively IT & creative
roles.
Candidate 9
3
2
In System 1, men are mainly associated to IT related roles and
women are more linked to creative roles, which reinforces ex-
isting stereotypes.
bias metrics against human perception is a complex research challenge that demands broader sampling, more rigorous
methodologies and multi-dimensional analysis. We envision this as a substantial research agenda that warrants a
dedicated paper to advance rigorous human-centered validation of bias metrics.
Manuscript submitted to ACM

```
