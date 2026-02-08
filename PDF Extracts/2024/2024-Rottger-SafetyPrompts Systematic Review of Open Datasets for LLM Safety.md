---
title: "2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety - PDF Extract"
source_pdf: "2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety.pdf"
pages: 19
extracted_at: "2026-02-07T17:00:45.738165"
---

# PDF Extract: 2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety

**Source PDF:** 2024-Rottger-SafetyPrompts Systematic Review of Open Datasets for LLM Safety.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

SafetyPrompts: a Systematic Review of Open Datasets for
Evaluating and Improving Large Language Model Safety
Paul R¨ottger1, Fabio Pernisi1, Bertie Vidgen2, and Dirk Hovy1
1Bocconi University, 2Contextual AI
Abstract
The last two years have seen a rapid growth in concerns around
the safety of large language models (LLMs). Researchers and
practitioners have met these concerns by creating an abun-
dance of datasets for evaluating and improving LLM safety.
However, much of this work has happened in parallel, and
with very different goals in mind, ranging from the mitigation
of near-term risks around bias and toxic content generation
to the assessment of longer-term catastrophic risk potential.
This makes it difficult for researchers and practitioners to find
the most relevant datasets for their use case, and to identify
gaps in dataset coverage that future work may fill. To remedy
these issues, we conduct a first systematic review of open
datasets for evaluating and improving LLM safety. We review
144 datasets, which we identified through an iterative and
community-driven process over the course of several months.
We highlight patterns and trends, such as a trend towards fully
synthetic datasets, as well as gaps in dataset coverage, such as a
clear lack of non-English and naturalistic datasets. We also ex-
amine how LLM safety datasets are used in practice – in LLM
release publications and popular LLM benchmarks – finding
that current evaluation practices are highly idiosyncratic and
make use of only a small fraction of available datasets. Our
contributions are based on SafetyPrompts.com, a living cat-
alogue of open datasets for LLM safety, which we plan to
update continuously as the field of LLM safety develops.
1
Introduction
Ensuring the safety of large language models (LLMs) has
become as a key priority for model developers and regulators.
Consequently, in recent years, researchers and practitioners
have created an abundance of datasets for evaluating and im-
proving LLM safety. Safety, however, is a multi-faceted and
contextual concept that lacks a unifying definition (Aroyo
et al. 2023). This complexity is reflected in the current land-
scape of safety datasets, which is broad, diverse, and fast-
changing. Within just two months of 2024, for example, re-
searchers published datasets for evaluating near-term risks
from LLMs, such as sociodemographic bias (Gupta et al.
2024b) and toxic content generation (Bianchi et al. 2024), as
well as datasets for evaluating long-term societal risk poten-
tial, around power-seeking (Mazeika et al. 2024) and syco-
phantic behaviours (Sharma et al. 2024). This rapid pace of
dataset creation, and the variety of purposes served by differ-
ent datasets, make it difficult for researchers and practitioners
to find the most relevant datasets for different use cases, and
to identify gaps in dataset coverage that future work may fill.
In this paper, we seek to address these issues by conducting
a first systematic review of open datasets for evaluating
and improving LLM safety. We identify 144 datasets pub-
lished between June 2018 and December 2024 based on clear
inclusion criteria (§2.1) using a comprehensive community-
driven search method (§2.2). We examine these 144 datasets
along several key dimensions, including their purpose (§3.2),
intended use (§3.3), format and size (§3.4), their creation
(§3.5), language (§3.6), licensing and access (§3.7), and pub-
lication (§3.8). Our review shows that a growing interest in
LLM safety is driving the creation of more and more diverse
open LLM safety datasets, with most contributions coming
from academia. Major outstanding challenges, on the other
hand, include a clear lack of safety datasets in non-English
languages as well as a lack of naturalistic safety evaluations.
We also review how open LLM safety datasets are used in
practice – in model release publications (§4) and popular
LLM benchmarks (§5) – finding that current evaluation prac-
tices are highly idiosyncratic and leverage only a small frac-
tion of available datasets. We argue that this creates clear
scope for standardisation in LLM safety evaluations, and that
model safety evaluations in general could be improved by
better leveraging recent progress in dataset creation (§6).
2
Dataset Review Methodology
2.1
Inclusion Criteria
At a high level, we restrict our review to open datasets that
are relevant to LLMs, and specifically relevant to evaluating
and improving LLM safety. More specifically, this means:
In terms of data modality, we only include text datasets.
We do not include image datasets (e.g. Schwemmer et al.
2020; Zhao, Wang, and Russakovsky 2021; Ricker et al.
2022) or audio datasets (e.g. Reimao and Tzerpos 2019; Koe-
necke et al. 2020; Meyer et al. 2020). We also do not include
datasets targeted at multimodal models, even if one modality
is text, such as in the case of vision-language (e.g. Carlini
et al. 2023; Hall et al. 2023; Wolfe et al. 2023) or text-to-
image models (e.g. Bianchi et al. 2023; Parrish et al. 2023;
Luccioni et al. 2024). Further, we do not include datasets tar-
geted at code generation models (e.g. Siddiq and Santos 2022;
Bhatt et al. 2023). These modalities and models constitute
arXiv:2404.05399v2  [cs.CL]  10 Jan 2025

--- Page 2 ---

natural expansions for future work.
We make only minimal restrictions in terms of data for-
mat. Real-world user interactions with LLMs usually take
the form of text chat (Ouyang et al. 2023; Zheng et al. 2024;
Zhao et al. 2024b), so we are most interested in datasets that
naturally fit a chat format, like open-ended questions and
instructions, but we also consider any other dataset that can
meaningfully be expressed in a prompt format. This includes
multiple-choice questions or autocomplete-style text snippets.
We do not make any restrictions on dataset language.
For data access, we only include datasets that are publicly
available for download via GitHub and/or Hugging Face. We
do not make restrictions based on how data is licensed.
Finally, we require that all datasets are relevant to safety.
For the purposes of our review, we adopt a wide and open
definition of safety. Broadly speaking, we include datasets
that relate to representational, political or other forms of so-
ciodemographic bias; to toxicity, malicious instructions or
harmful advice; to hazardous behaviours like sycophancy
or power-seeking; to alignment with social, moral or ethi-
cal values; or to adversarial LLM usage (e.g. red-teaming,
jailbreaking, prompt hacking). We only include datasets that
explicitly focus on one or multiple of these aspects of LLM
safety. We do not include datasets that target general LLM
capabilities like reasoning, language understanding, or code
completion (e.g. Dua et al. 2019; Hendrycks et al. 2020; Chen
et al. 2021). We also do not include datasets that target fac-
tuality in LLMs, unless they directly relate to safety, like in
the case of generating misinformation (Souly et al. 2024) or
measuring truthfulness (Lin, Hilton, and Evans 2022).1
The cutoff date for our review is December 17th, 2024.
We only included datasets that were first published (i.e. made
publicly available online) before this date.
2.2
Finding Dataset Candidates
We used an iterative and community-driven approach com-
bined with snowball search to identify dataset candidates
for inclusion in our review. In January 2024, we released a
first version of SafetyPrompts.com, with an initial list of 44
datasets that we had compiled in a heuristic fashion based
on prior work and our knowledge of the LLM safety field.
Over the next months, we marketed the website to the LLM
safety community on Twitter and Reddit, to solicit feedback
and further dataset suggestions. This resulted in 51 additional
datasets, suggested by many different researchers and practi-
tioners. We then used these 95 datasets as a starting point for
snowball search, wherein we reviewed each publication cor-
responding to each dataset for references to other potentially
relevant datasets. Whenever we identified a new dataset, we
repeated this process. This resulted in 49 additional datasets.
Overall, our review includes 144 open datasets for evaluat-
ing and improving LLM safety, which were first published
between June 2018 and December 2024.
We chose this review method because of two main reasons.
First, LLM safety is a very fast-moving field with contribu-
1Each dataset candidate was reviewed by two authors of this
paper. We make detailed information on each dataset, as well as
excluded datasets + exclusion reasons, available in the project repo.
tions from across academia and industry. By sharing inter-
mittent results of our review on SafetyPrompts.com, we were
able to solicit feedback from a broad range of stakeholders
and expand our review, while also providing a useful resource
to the community well ahead of the release of this paper.
Second, traditional systematic review methods like keyword
search are ill-suited to the scope of our review. Combinations
of relevant keywords like “language model”, “safety” and
“dataset” return thousands of results on Google Scholar and
similar platforms – and still fail to capture the many types of
datasets that may not mention “safety” but are highly relevant
to it regardless, like toxic conversation datasets or bias eval-
uations. Despite our best efforts, it is likely that our review
is missing at least some relevant datasets. We are committed
to adding these datasets, along with future relevant dataset
releases, to SafetyPrompts.com.
2.3
Recording Structured Information
For each of the 144 datasets in our review, we recorded 23
pieces of structured information. At a high level, our goal
was to capture the full development pipeline of each dataset:
from how the dataset was created, to what entries in the
dataset look like, what the dataset can or should be used
for, how it can be accessed, and where it was published. We
show the full codebook in Appendix A, which describes the
structure and content of our main review spreadsheet. We
make the spreadsheet available along with code to reproduce
our analyses at github.com/paul-rottger/safetyprompts-paper.
3
Dataset Review Findings
3.1
History and Growth of Safety Datasets
Our review shows that LLM safety builds on a rich his-
tory of research into the risks and biases of language
models and dialogue agents. The first datasets in our re-
view were published in mid-2018, and focus on evaluating
gender bias – originally for co-reference resolution systems,
but equally applicable to current LLMs (Zhao et al. 2018;
Rudinger et al. 2018). These datasets, in turn, build on earlier
works on biases in word embeddings (e.g. Bolukbasi et al.
2016; Caliskan, Bryson, and Narayanan 2017; Garg et al.
2018), which illustrates that concerns around the negative
social impacts of language models are far from new. Even the
term “safety” was already used by Dinan et al. (2019) and
Rashkin et al. (2019), among others, who introduced datasets
for evaluating and improving the safety of dialogue agents
well before the current generative LLM paradigm. By today’s
standards, however, interest in safety was relatively low at
the time, with only 9 out of the 144 datasets in our review
(6.3%) published in or before 2020, as shown in Figure 1.
LLM safety experienced a first moderate growth phase
in 2021 and 2022. These two years, respectively, saw the
publication of 16 and 17 open LLM safety datasets. This
coincides with increased interest in generative language mod-
els, particularly among researchers, following the release of
GPT-3 in mid-2020 (Brown et al. 2020).
Right now, research into LLM safety is experiencing
unprecedented growth. This coincides with a surge in public
interest in LLMs as well as concerns around LLM safety

--- Page 3 ---

Example datasets
DecodingTrust by Wang et al. (2024a) evaluates LLM safety across 8 “perspectives”
ConfAIde by Mireshghallah et al. (2024) evaluates the privacy-reasoning capabilities of LLMs
MoralChoice by Scherrer et al. (2023) evaluates moral beliefs encoded in LLMs
BBQ by Parrish et al. (2022) evaluates social biases of LLMs in question answering
ToxicChat by Lin et al. (2023) trains and evaluates content moderation systems for LLMs
Figure 1: (top) Number of datasets published per year, grouped by their primary purpose. Our review includes 144 datasets
published between June 2018 and December 2024. (bottom) Example datasets for each type of dataset purpose (§3.2).
following the release of ChatGPT in November 2022. 43 out
of the 144 datasets in our review (29.9%) were published
in 2023, and 2024 saw even more activity, with 59 datasets
published. Accordingly, it seems very likely that 2025 will
surpass this record once more.
3.2
Purpose of Datasets
In our review, we differentiate between five distinct dataset
purposes: Broad safety (n=53) denotes datasets that cover
several aspects of LLM safety. This includes structured eval-
uation datasets like SafetyKit (Dinan et al. 2022) or Sim-
pleSafetyTests (Vidgen et al. 2024b) as well as broad-scope
red-teaming datasets like BAD (Xu et al. 2021) or Anthropic-
RedTeam (Ganguli et al. 2022). Narrow safety (n=25), con-
versely, denotes datasets that focus only on one specific as-
pect of LLM safety. SafeText (Levy et al. 2022), for example,
focuses only on commonsense physical safety, while Syco-
phancyEval (Sharma et al. 2024) focuses on sycophantic
behaviour. Value alignment (n=23) refers to datasets that
are concerned with the ethical, moral or social behaviour of
LLMs. This includes datasets that seek to evaluate LLM un-
derstanding of ethical norms, like Scruples (Lourie, Le Bras,
and Choi 2021) and ETHICS (Hendrycks et al. 2021), as
well as opinion surveys like GlobalOpinionQA (Durmus et al.
2024). Bias (n=33) refers to datasets for evaluating sociode-
mographic biases in LLMs. BOLD (Dhamala et al. 2021),
for example, evaluates bias in text completions, whereas
DiscrimEval (Tamkin et al. 2023a) evaluates biases in situ-
ated LLM decision-making. Other (n=10), in our review,
includes datasets for developing LLM chat moderation sys-
tems, like FairPrism (Fleisig et al. 2023) and ToxicChat (Lin
et al. 2023), as well as specialised prompts from public com-
petitions like Gandalf (LakeraAI 2023a), Mosscap (LakeraAI
2023b) or HackAPrompt (Schulhoff et al. 2023).
Figure 1 shows that early safety datasets were primarily
concerned with evaluating biases. 14 out of 25 datasets
(56.0%) published between 2018 and 2021 were created to
identify and analyse sociodemographic biases in language
models. 13 of these datasets evaluate gender biases, either ex-
clusively (e.g. Nozza, Bianchi, and Hovy 2021) or along with
other categories of bias such as race and sexual orientation
(e.g. Sheng et al. 2019) or religion (e.g. Li et al. 2020).
Broad safety emerged as a prominent theme in 2022,
driven by industry contributions. Anthropic, for instance,
released two broad-scope red-teaming datasets (Ganguli et al.
2022; Bai et al. 2022), while Meta published datasets on pos-
itive LLM conversations (Ung, Xu, and Boureau 2022) and
general safety evaluation (Dinan et al. 2022). Most recently,
broad safety has shifted towards more structured evaluation,
as exemplified by benchmarks like DecodingTrust (Wang
et al. 2024a) or HarmBench (Mazeika et al. 2024).
There is now a trend towards more specialised safety
evaluations. Narrow safety evaluations did not emerge un-
til 2022, but now make up a significant portion of all new
datasets. In 2024 alone, 15 of the 59 datasets in our review
(25.4%) were concerned with specific aspects of LLM safety,
like rule-following (Mu et al. 2024) or privacy-reasoning
ability (Mireshghallah et al. 2024).
Relatedly, there is an increasing focus on adversarial
robustness and LLM “jailbreaking”. A growing body of
work introduces safety datasets that are explicitly designed to

--- Page 4 ---

elicit unsafe responses even from models trained to respond
safely, often using elaborate prompting strategies, also known
as “jailbreaks” (Wei, Haghtalab, and Steinhardt 2023). Since
August 2023, we record 13 such datasets, which differ from
most other datasets that seek to evaluate safety in response to
simpler, more naturalistic prompts (e.g. Bhardwaj and Poria
2023; Shaikh et al. 2023; Vidgen et al. 2024b).
3.3
Intended Use of Datasets
Most datasets are intended for model evaluation only.
112 out of the 144 datasets in our review (77.8%) were cre-
ated for benchmarking or evaluation. Only 6 datasets (4.2%),
by contrast, comprise examples of positive interactions be-
tween users and LLMs, created specifically for model training
(Rashkin et al. 2019; Ung, Xu, and Boureau 2022; Kim et al.
2022; Bianchi et al. 2024; Guo et al. 2024; Jiang et al. 2024).
Overall, there is much more work on evaluating LLM safety
than there is work on improving LLM safety.
3.4
Dataset Format and Size
The format of LLM safety datasets has changed along-
side general trends in LLM development. Early datasets,
especially those created for bias evaluation, often used
autocomplete-style formats (n=9), where models are tasked
to either fill a masked word or finish a sentence snippet (e.g.
Sheng et al. 2019; Dhamala et al. 2021; Kirk et al. 2021).
Such formats, which are most compatible with early language
models like BERT or GPT-2, have since mostly been replaced
by chat-style prompts, like open-ended questions and instruc-
tions (n=88), as well as promptable multiple-choice questions
(n=24), which better suit current generative LLMs.
Dataset size varies substantially across the 144 datasets
in our review. Smaller datasets (≤1k entries, n=42) tend to
be narrow safety evaluation datasets, written by the dataset
authors. For example, the smallest dataset – ControversialIn-
structions by Bianchi et al. (2024) – comprises 40 author-
written prompts to test the propensity of LLMs to generate
hate speech. Larger datasets (≥100k entries, n=21), on the
other hand, are often broader in scope, designed for training
and evaluation, and created through templating or LLM gen-
eration (§3.5). For example, the largest dataset – WorldVal-
uesBench by Zhao et al. (2024a) – contains 21.5m multiple-
choice prompts created programmatically from individual
responses to the large-scale World Value Survey.
3.5
Dataset Creation
The use of templates is a consistently popular method for
generating safety evaluation data. 26 out of the 144 datasets
in our review (18.1%) consist of human-written phrase or
prompt templates, which are expanded through combina-
tion into larger evaluation datasets. HolisticBias (Smith et al.
2022), for example, comprises 26 sentence templates (e.g. “I
am an [attribute1] who is [attribute2].”), which are combined
with around 600 individual descriptor terms to create 459.8k
test cases. Generally, template approaches are most popular
for bias evaluation – 16 out of 33 bias evaluation datasets in
our review use a template approach – but recent work has also
used templates for evaluating broad-scope LLM safety (Wang
et al. 2024a) or specific concerns such as privacy reasoning
(Mireshghallah et al. 2024).
A significant portion of recently-released datasets is
fully synthetic. 21 of the 102 datasets released since 2023
(20.6%) consist of chat prompts or multiple-choice questions
generated entirely by LLMs – most commonly by some vari-
ant of GPT-3.5. Shaikh et al. (2023), for example, prompt
GPT-3.5 to generate 200 harmful questions, which they use to
explore safety in chain-of-thought question answering. The
resulting dataset resembles the human-written SimpleSafe-
tyTests (Vidgen et al. 2024b). Generally, synthetic datasets
vary in size and scope much like human-written datasets do.
Relatedly, instead of relying on static templates for data
creation, many recent datasets are more flexibly aug-
mented using LLMs. Bhatt et al. (2023), for instance, ex-
pand a small expert-written set of cyberattack instructions
into a larger set of 1,000 prompts using Llama-70b-chat (Tou-
vron et al. 2023). Wang et al. (2024a) take a similar approach
to build their large-scale DecodingTrust benchmark.
By contrast, very few datasets comprise naturalistic user
interactions with LLMs. Around half of the 144 datasets in
our review are hand-written (n=70, 48.6%), but mostly by the
authors of the corresponding dataset publications. A much
smaller proportion of datasets is created by humans – either
crowdworkers (e.g. Ganguli et al. 2022; Aroyo et al. 2023;
Kirk et al. 2024) or participants of online competitions (e.g.
LakeraAI 2023a,b) – interacting more naturally with LLMs.
Finally, there is a trend towards reusing existing
datasets rather than creating original data. 34 out of the
59 datasets published in 2024 (57.6%) were entirely (n=10)
or partially (n=24) sampled from older datasets. QHarm by
Bianchi et al. (2024), for example, is taken entirely from
AnthropicHarmlessBase (Bai et al. 2022). Another common
approach is to sample existing data and augment it with tem-
plates (e.g. Tedeschi et al. 2024) or LLM generations (e.g. Yu
et al. 2024a). By contrast, just 10 out of 43 datasets published
in 2023 (23.3%) reused existing data. This shift suggests a
growing maturity of the LLM safety dataset landscape.
3.6
Dataset Languages
The vast majority of open LLM safety datasets uses En-
glish language only. 113 out of 144 datasets in our review
(78.5%) are exclusively in English. 10 datasets (6.9%) focus
only on Chinese (e.g. Zhou et al. 2022; Xu et al. 2023; Zhao
et al. 2023), and one dataset each focuses only on Arabic,
Swedish, Hindi, Korean, and French. The 16 other datasets
(11.1%) cover English along with one or more other lan-
guages. Jin et al. (2024b) cover 106 languages, although test
cases are auto-translated from the English. The other 143
datasets in our review together cover 31 languages.
3.7
Data Licensing and Access
When data is shared, usage licenses are mostly permis-
sive. The most common license is the very permissive MIT
License, which is used for 58 out of 144 datasets (40.3%). 23
datasets (16.0%) use the Apache 2.0 License, which provides
additional patent protections. 43 datasets (29.9%) use vari-
ants of a CC BY 4.0 License, which requires dataset users to
provide appropriate credit and indicate if changes were made

--- Page 5 ---

Academic / Non-Profit Org.
n
1
Stanford University
15
1
Allen Institute for AI
15
3
UC Berkeley
14
4
University of Washington
13
5
Carnegie Mellon University
12
Industry Org.
n
1
Meta* (prev. Facebook)
13
2
Anthropic
9
3
Microsoft* (incl. Research)
7
4
Google* (incl. DeepMind)
6
5
Alibaba
4
Table 1: Organisations that published the most open LLM safety datasets among the 144 datasets in our review. For each
dataset, we count all affiliations for all co-authors. Stanford at n=15, for example, means that 15 datasets had a Stanford author.
to the dataset. Notably, 15 datasets (10.4%) prohibit commer-
cial usage with a CC BY-NC License. Only 2 datasets (1.4%)
use a more restrictive custom license. As of December 17th,
2024, 15 datasets (10.4%) do not specify any license.2
GitHub is still the most popular platform for sharing
LLM safety data. 72 datasets (50.0%) are available only on
GitHub. However, 55 datasets (38.2%) are available on both
GitHub and HuggingFace, and several recent datasets are
shared on Hugging Face only (e.g. Han et al. 2024a; Manerba
et al. 2024), suggesting a shift in how data is shared.
3.8
Dataset Publication Authors and Venues
Academic and non-profit organisations drive most of the
creation of open LLM safety datasets. For 69 out of 144
datasets in our review (47.9%), all authors of the correspond-
ing publication were affiliated only with academic or non-
profit organisations. 45 datasets (31.3%) included authors
from industry and academia, and only 30 datasets (20.8%)
were published by fully industry teams.
The creation of LLM safety datasets is concentrated in
few research hubs (Table 1). There are 156 unique affilia-
tions across the authors of the 144 datasets in our review. 101
affiliations (64.7%) are associated with just a single dataset.
The five most prolific organisations, on the other hand, are
each associated with at least 13 datasets. All of the twenty
most prolific organisations are located and/or headquartered
in the US, with the exception of Bocconi University (Italy,
n=11), the University of Oxford (UK, n=5), CUHK (HK,
n=4), and Tsinghua University (China, n=4).
Most LLM safety datasets so far have been published
at *ACL conferences. 68 out of the 144 datasets in our re-
view (47.2%) were published at either ACL (n=27), EMNLP
(n=30) or other *ACL venues. 33 datasets (19.7%) were pub-
lished at more ML-focused conferences, i.e. NeurIPS (n=18),
ICLR (n=10), or ICML (n=5). Only 11 datasets (7.6%) were
published at other venues, and only 2 datasets appeared in
journal publications (Jin et al. 2024a; Yu, Li, and Lan 2024a).
28 datasets (19.4%), on the other hand, were accompanied
only by arXiv preprints, and 4 (2.7%) only by blog posts,
meaning they did not receive traditional peer review. Gener-
ally, we observe a slight trend away from *ACL conferences
and towards more ML-focused venues as well as arXiv-only
2While conducting our review, we reached out to authors of all
datasets that had not specified a license and encouraged them to add
one. At least five authors added a license as a result.
publication, although this could in part be explained by recent
arXiv preprints still being under review.
4
Datasets in Model Release Publications
In the following, we briefly examine how open LLM safety
datasets are used in practice. In particular, we examine in
this section which safety datasets are used to evaluate current
state-of-the-art LLMs ahead of their release, as documented
in model release publications. In the next section (§5), we
then examine which safety datasets are included in popular
LLM benchmarks and leaderboards. This is to characterise
current norms and common practices in evaluating LLM
safety, so that we can then discuss (§6) these norms and
practices in relation to the findings of our dataset review (§3).
4.1
Scope of our Model Release Review
We examine the top 50 best-performing LLMs listed on the
LMSYS Chatbot Arena Leaderboard (Chiang et al. 2024) as
of July 25th, 2024.3 The LMSYS Chatbot Arena Leaderboard
is a crowdsourced platform for LLM evaluation, which ranks
models based on model Elo scores calculated from over one
million pairwise human preference votes. We use this leader-
board for setting the scope of our review because it is held
in high regard in the LLM community, and it has up-to-date
coverage of recent model releases.
The top 50 entries on the LMSYS leaderboard corre-
spond to 29 unique model releases.4 Of these 29 models, 16
(55.2%) are proprietary models only accessible via an API,
released by companies such as OpenAI (GPT), Anthropic
(Claude), Google (Gemini) and 01 AI (Yi). The other 13 mod-
els (44.8%) are open models, for which weights are publicly
accessible via Hugging Face. Proprietary models generally
outrank open models on the leaderboard, with Gemma 2 27b
(DeepMind 2024) being the best open model at rank 14. All
29 models were released by industry labs.
4.2
Findings of our Model Release Review
Around half of state-of-the-art LLMs are evaluated for
safety ahead of their release, with substantial variation in
the extent and nature of safety evaluations. For 16 out of
29 model releases (55.2%), model developers report at least
some quantitative safety evaluation in the associated technical
3https://lmarena.ai/?leaderboard
4A model release may comprise multiple model versions, such
as GPT-4-0314 and GPT-4-0613.

--- Page 6 ---

Dataset
Purpose
n
1
TruthfulQA (Lin, Hilton, and Evans 2022)
evaluate tendency to mimic human falsehoods
8
2
BBQ (Parrish et al. 2022)
evaluate social bias in question answering
6
3
AnthropicRedTeam (Ganguli et al. 2022)
evaluate responses to diverse red-team attacks
3
4
ToxiGen (Hartvigsen et al. 2022)
evaluate toxicity in text completions
3
5
RealToxicityPrompts (Gehman et al. 2020)
evaluate toxicity in text completions
3
Table 2: Most popular open LLM safety datasets, based on how often release publications for SOTA LLMs reported results on
each dataset. BBQ at n=6, for example, means that 6 out of the 29 model release publications (§4.2) reported BBQ results.
report, blog post or model card. 13 model release publica-
tions (44.8%) report results on at least one open LLM safety
dataset. The Claude 3.5 model card, for example, reports
results on WildChat (Zhao et al. 2024b) and XSTest (R¨ottger
et al. 2024), whereas Gemma 2 (DeepMind 2024) is eval-
uated on 7 different open LLM safety datasets. 13 out of
the 29 models (44.8%), on the other hand, do not report any
safety evaluations. This includes the strongest model, the
proprietary GPT-4o, which mentions safety measures in its
release blog post, but lacks any concrete quantitative safety
evaluations. Other models, both proprietary (e.g. Yi-Large,
Reka Core) and open (e.g. Mixtral, Command R), do not
mention safety at all in their release publications.
When safety is evaluated, proprietary data plays a
large role in model release safety evaluations. Out of
the 16 model releases that report safety evaluation results,
11 (68.8%) use undisclosed proprietary data for evaluating
model safety. 3 of these releases – Llama 3 (Meta 2024),
Qwen 2 (Yang et al. 2024), and Phi 3 (Abdin et al. 2024) –
report results only on proprietary safety datasets.
Finally, the diversity of open LLM safety datasets used
in model release evaluations is very limited. Only 14 open
LLM safety datasets are used across the 29 model releases,
and 6 of these 14 datasets are used only once. Table 2 shows
the 5 datasets that are used most often. Notably, TruthfulQA
(Lin, Hilton, and Evans 2022) is used in 8 out of the 16 model
release publications that report any safety evaluation results
(50.0%), and it is often framed by model developers as a
capability rather than a safety evaluation. We discuss the
implications of these findings in §6.
5
Datasets used in Popular Benchmarks
5.1
Scope of our Benchmark Review
To complement our model release review, we briefly exam-
ine 9 popular LLM benchmarks for which safety datasets
they include. 6 benchmarks are widely-used general-purpose
benchmarking suites: Stanford’s HELM Classic (Liang et al.
2023) and HELM Instruct (Zhang et al. 2024b), Hugging
Face’s Open LLM Leaderboard (Beeching et al. 2023), Al-
lenAI’s RewardBench (Lambert et al. 2024), Eleuther AI’s
Evaluation Harness (Gao et al. 2021), and BIG-Bench (Sri-
vastava et al. 2023). 3 benchmarks focus explicitly on LLM
safety: TrustLLM (Sun et al. 2024), HELM Safety (Kaiyom
et al. 2024), and the LLM Safety Leaderboard.5
5.2
Findings of our Benchmark Review
There are large differences in how different benchmarks
evaluate LLM safety. The 9 benchmarks make use of 26
open LLM safety datasets. 17 of these datasets are used in
just one benchmark. TrustLLM (Sun et al. 2024), for ex-
ample, combines 11 open LLM safety datasets, of which 5
are not used in any other benchmark. The only open LLM
safety datasets that are used in more than 2 benchmarks are
TruthfulQA (Lin, Hilton, and Evans 2022), which is used
in 4 benchmarks, as well as RealToxicityPrompts (Gehman
et al. 2020), BBQ (Parrish et al. 2022), ETHICS (Hendrycks
et al. 2021), XSTest (R¨ottger et al. 2024), and DoNotAnswer
(Wang et al. 2024c), which are each used in 3 benchmarks.
There is currently no single LLM safety benchmark
with a truly comprehensive scope. The TrustLLM bench-
mark (Sun et al. 2024), has the broadest scope relevant to
safety among the 9 benchmarks we examined, covering mali-
cious instruction-following, bias, and value alignment. How-
ever, it does not, for example, test for longer-term risk poten-
tial with evaluations for sycophancy (Perez et al. 2023) or
chemical weapon knowledge (Li et al. 2024b), as the Eval-
uation Harness does (Gao et al. 2021). Similarly, the LLM
Safety Leaderboard (Beeching et al. 2023) tests for toxic
content generation and malicious instruction-following, but
not for false refusal (e.g. R¨ottger et al. 2024) or sociodemo-
graphic biases (e.g. Parrish et al. 2022)
6
Discussion & Future Directions
6.1
The State of the Safety Dataset Landscape
Overall, our review shows that growing interest in LLM
safety is driving the creation of more and more diverse
open LLM safety datasets. More datasets were published in
2023 than ever before, and 2024 again surpassed this record
(§3.1). Existing datasets span varied purposes (§3.2) and for-
mats (§3.4), which have adapted over time to meet the needs
and requirements of LLM users and developers. Researchers
and practitioners are making creative use of new methods
for dataset creation (§3.5), and when data is shared, usage
licenses are mostly permissive (§3.7). These are encouraging
signs for the health of the open LLM safety community and
5https://huggingface.co/spaces/AI-Secure/llm-trustworthy-
leaderboard, based on Wang et al. (2024a).

--- Page 7 ---

its ability to address emerging challenges and fill gaps in
dataset coverage as they become apparent.
Among these gaps, the most apparent today is that there
is a clear lack of safety datasets in non-English languages.
We found that English dominates the current safety dataset
landscape (§3.6), mirroring long-standing trends in NLP re-
search (Bender 2011; Joshi et al. 2020; Holtermann et al.
2024). To some extent, this imbalance also reflects an imbal-
ance in who is publishing safety datasets (§3.8). The lack of
non-English resources for evaluating and improving LLM
safety is a problem because it means that billions of non-
English speakers across the world are potentially more at risk
of harm when using current language technologies. Further,
interpretations of safety are known to vary across cultures and
geographies (Aroyo et al. 2023; Kirk et al. 2024). These two
factors create an urgent need for the LLM safety community
to prioritise the creation of non-English datasets going for-
ward. Recent datasets like AyaRedTeaming (Aakanksha et al.
2024), which were created for language-specific cultural con-
texts with the involvement of local stakeholders, may serve
as a useful blueprint for future work in this direction.
The second major concern apparent from our review is that
current safety evaluation datasets largely fail to reflect
real-world LLM usage, which undermines their ecological
validity. Data generation and augmentation, from templates to
more recent LLM-based methods, have enabled rapid dataset
creation (§3.5), but it is not clear that they can emulate the
“messiness” and diversity that is apparent in real-world user in-
teractions with LLMs (Ouyang et al. 2023; Zhao et al. 2024b;
Zheng et al. 2024). An increasing focus on safety against “jail-
breaking” (§3.2) may match the behaviour of sophisticated
adversarial users, but does not capture the potential risks from
vulnerable populations interacting with LLMs without mali-
cious intent (Vidgen et al. 2024a). Addressing these concerns
will require the creation of more naturalistic evaluations, and
clearer communication about which user personas (e.g. vul-
nerable, malicious, or adversarial) are targeted by individual
safety evaluations. Encouraging developments in this direc-
tion include WildGuard (Han et al. 2024a) and WildJailBreak
(Jiang et al. 2024), which provide evaluations based on real
user prompts. Future work may similarly look to collections
of real user interactions with LLMs, such as WildChat (Zhao
et al. 2024b) and LMSYS (Zheng et al. 2024), to improve the
ecological validity of LLM safety evaluations.
6.2
The Use of Safety Datasets in Practice
Our analysis of how open LLM safety datasets are used in
practice shows that there is clear scope for standardisation
in LLM safety evaluations. Safety is a key priority for model
developers and users, as evidenced by the inclusion of safety
evaluations in the majority of model release publications (§4)
and popular LLM benchmarks (§5). However, there is much
idiosyncrasy in which datasets are used for evaluating safety
across model release publications and benchmarks. For com-
mercial model releases, these datasets are often proprietary
and undisclosed. More standardised and open evaluations,
on the other hand, would enable more meaningful model
comparisons and incentivise the development of safer LLMs.
We see three main directions towards this goal. First,
current evaluation practices could better leverage recent
progress in safety dataset creation. The most popular open
datasets for evaluating safety in model release publications,
for example, are all from 2020 or 2022 (Table 2), despite
more than two thirds of the datasets in our review being
published in or after 2023. Prior publication date is not a
sign of lacking quality, but older autocomplete-style datasets
like RealToxicityPrompts (Gehman et al. 2020) or ToxiGen
(Hartvigsen et al. 2022) simply do not reflect realistic usage
of current chat-optimised LLMs (Ouyang et al. 2023; Zheng
et al. 2024; Zhao et al. 2024b), which undermines their eco-
logical validity. Our review highlights many datasets that
could be used in their stead. Second, there is a clear need
for unified standards of dataset quality. In this paper, we
refrained from making quality judgments about the datasets
we reviewed, mainly because different datasets serve differ-
ent purposes, so that their utility is highly context dependent.
However, recent efforts like BetterBench (Reuel et al. 2024)
as applied to safety datasets could help create consensus on
which datasets to use for safety benchmarking. Third, safety
research would benefit from unified safety evaluation pro-
tocols. The open-ended nature of safety-relevant behaviours
complicates standardised evaluation compared to many fac-
tual tasks. Frameworks like Eleuther AI’s Evaluation Harness,
adapted for safety tasks, would make it easier for model de-
velopers and users to run the same safety evaluations with
reproducible results, and thus serve to reduce idiosyncrasy in
prevailing safety evaluation practices.
7
Conclusion
In recent years, researchers and practitioners have sought to
meet concerns around the safety of large language models by
creating an abundance of datasets for evaluating and improv-
ing LLM safety. However, the rapid pace of dataset creation
and the variety of purposes served by different datasets have
made it difficult for researchers and practitioners to find the
most relevant datasets for different use cases, and to iden-
tify gaps in dataset coverage that future work may fill. In
this paper, we addressed these issues by conducting a first
systematic review of open LLM safety datasets.
In our review, which includes 144 datasets published be-
tween June 2018 and December 2024, we showed that, en-
couragingly, existing datasets span varied purposes and for-
mats, which have adapted over time to meet the changing
needs and requirements of LLM users and developers. How-
ever, we also highlighted major outstanding challenges, in-
cluding a clear lack of non-English datasets as well as nat-
uralistic safety evaluations. Further, when examining how
open LLM safety datasets are used in practice – in model re-
lease publications and popular LLM benchmarks – we found
that current evaluation practices are highly idiosyncratic and
make use of only a small fraction of available datasets, which
presents clear scope for rejuvenation and standardisation.
Overall, we hope that with our review, as well as the living
dataset catalogue we make available on SafetyPrompts.com,
we can enable such positive change, by helping researchers
and practitioners make the best use of existing datasets, and
providing a strong foundation for future dataset development.

--- Page 8 ---

Acknowledgments
Thank you for feedback and dataset suggestions to Giuseppe
Attanasio, Steven Basart, Federico Bianchi, Marta R. Costa-
Juss`a, Daniel Hershcovic, Kexin Huang, Hyunwoo Kim,
George Kour, Bo Li, Hannah Lucas, Marta Marchiori
Manerba, Norman Mu, Niloofar Mireshghallah, Matus Piku-
liak, Verena Rieser, Felix R¨ottger, Sam Toyer, Ryan Tsang,
Pranav Venkit, Laura Weidinger, and Linhao Yu. Special
thanks to Hannah Rose Kirk for the initial logo suggestion.
PR, FP, and DH are members of the Data and Marketing
Insights research unit of the Bocconi Institute for Data Sci-
ence and Analysis, and are supported by a MUR FARE 2020
initiative under grant agreement Prot. R20YSMBZ8S (IN-
DOMITA) and the European Research Council (ERC) under
the European Union’s Horizon 2020 research and innovation
program (No. 949944, INTEGRATOR).
References
Aakanksha; Ahmadian, A.; Ermis, B.; Goldfarb-Tarrant, S.;
Kreutzer, J.; Fadaee, M.; and Hooker, S. 2024. The Multi-
lingual Alignment Prism: Aligning Global and Local Prefer-
ences to Reduce Harm. In Al-Onaizan, Y.; Bansal, M.; and
Chen, Y.-N., eds., Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing, 12027–
12049. Miami, Florida, USA: Association for Computational
Linguistics.
Abdin, M.; Jacobs, S. A.; Awan, A. A.; Aneja, J.; Awadallah,
A.; Awadalla, H.; Bach, N.; Bahree, A.; Bakhtiari, A.; Bao, J.;
Behl, H.; Benhaim, A.; Bilenko, M.; Bjorck, J.; Bubeck, S.;
Cai, Q.; Cai, M.; Mendes, C. C. T.; Chen, W.; Chaudhary, V.;
Chen, D.; Chen, D.; Chen, Y.-C.; Chen, Y.-L.; Chopra, P.; Dai,
X.; Giorno, A. D.; de Rosa, G.; Dixon, M.; Eldan, R.; Fragoso,
V.; Iter, D.; Gao, M.; Gao, M.; Gao, J.; Garg, A.; Goswami,
A.; Gunasekar, S.; Haider, E.; Hao, J.; Hewett, R. J.; Huynh,
J.; Javaheripi, M.; Jin, X.; Kauffmann, P.; Karampatziakis, N.;
Kim, D.; Khademi, M.; Kurilenko, L.; Lee, J. R.; Lee, Y. T.;
Li, Y.; Li, Y.; Liang, C.; Liden, L.; Liu, C.; Liu, M.; Liu, W.;
Lin, E.; Lin, Z.; Luo, C.; Madan, P.; Mazzola, M.; Mitra, A.;
Modi, H.; Nguyen, A.; Norick, B.; Patra, B.; Perez-Becker,
D.; Portet, T.; Pryzant, R.; Qin, H.; Radmilac, M.; Rosset,
C.; Roy, S.; Ruwase, O.; Saarikivi, O.; Saied, A.; Salim, A.;
Santacroce, M.; Shah, S.; Shang, N.; Sharma, H.; Shukla,
S.; Song, X.; Tanaka, M.; Tupini, A.; Wang, X.; Wang, L.;
Wang, C.; Wang, Y.; Ward, R.; Wang, G.; Witte, P.; Wu, H.;
Wyatt, M.; Xiao, B.; Xu, C.; Xu, J.; Xu, W.; Yadav, S.; Yang,
F.; Yang, J.; Yang, Z.; Yang, Y.; Yu, D.; Yuan, L.; Zhang,
C.; Zhang, C.; Zhang, J.; Zhang, L. L.; Zhang, Y.; Zhang,
Y.; Zhang, Y.; and Zhou, X. 2024. Phi-3 Technical Report:
A Highly Capable Language Model Locally on Your Phone.
arXiv:2404.14219.
Ahn, J.; and Oh, A. 2021. Mitigating Language-Dependent
Ethnic Bias in BERT. In Moens, M.-F.; Huang, X.; Specia,
L.; and Yih, S. W.-t., eds., Proceedings of the 2021 Confer-
ence on Empirical Methods in Natural Language Processing,
533–549. Online and Punta Cana, Dominican Republic: As-
sociation for Computational Linguistics.
Aroyo, L.; Taylor, A.; Diaz, M.; Homan, C.; Parrish, A.;
Serapio-Garc´ıa, G.; Prabhakaran, V.; and Wang, D. 2023.
Dices dataset: Diversity in conversational ai evaluation for
safety. Advances in Neural Information Processing Systems,
36.
Bai, Y.; Jones, A.; Ndousse, K.; Askell, A.; Chen, A.; Das-
Sarma, N.; Drain, D.; Fort, S.; Ganguli, D.; Henighan, T.;
et al. 2022. Training a helpful and harmless assistant with
reinforcement learning from human feedback. arXiv preprint
arXiv:2204.05862.
Bajaj, D.; Lei, Y.; Tong, J.; and Huang, R. 2024. Evaluating
Gender Bias of LLMs in Making Morality Judgements. In
Al-Onaizan, Y.; Bansal, M.; and Chen, Y.-N., eds., Findings
of the Association for Computational Linguistics: EMNLP
2024, 15804–15818. Miami, Florida, USA: Association for
Computational Linguistics.
Barikeri, S.; Lauscher, A.; Vuli´c, I.; and Glavaˇs, G. 2021.
RedditBias: A Real-World Resource for Bias Evaluation and
Debiasing of Conversational Language Models. In Zong, C.;
Xia, F.; Li, W.; and Navigli, R., eds., Proceedings of the 59th
Annual Meeting of the Association for Computational Lin-
guistics and the 11th International Joint Conference on Nat-
ural Language Processing (Volume 1: Long Papers), 1941–
1955. Online: Association for Computational Linguistics.
Beeching, E.; Fourrier, C.; Habib, N.; Han, S.; Lambert,
N.; Rajani, N.; Sanseviero, O.; Tunstall, L.; and Wolf, T.
2023.
Open LLM Leaderboard.
https://huggingface.co/
spaces/HuggingFaceH4/open llm leaderboard.
Bender, E. M. 2011. On achieving and evaluating language-
independence in NLP. Linguistic Issues in Language Tech-
nology, 6.
Bhardwaj, R.; Do, D. A.; and Poria, S. 2024. Language Mod-
els are Homer Simpson! Safety Re-Alignment of Fine-tuned
Language Models through Task Arithmetic. In Ku, L.-W.;
Martins, A.; and Srikumar, V., eds., Proceedings of the 62nd
Annual Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), 14138–14149. Bangkok,
Thailand: Association for Computational Linguistics.
Bhardwaj, R.; and Poria, S. 2023.
Red-Teaming Large
Language Models using Chain of Utterances for Safety-
Alignment. arXiv:2308.09662.
Bhatt, M.; Chennabasappa, S.; Nikolaidis, C.; Wan, S.; Ev-
timov, I.; Gabi, D.; Song, D.; Ahmad, F.; Aschermann, C.;
Fontana, L.; et al. 2023. Purple llama cyberseceval: A se-
cure coding benchmark for language models. arXiv preprint
arXiv:2312.04724.
Bhatt, S.; Dev, S.; Talukdar, P.; Dave, S.; and Prabhakaran,
V. 2022. Re-contextualizing Fairness in NLP: The Case of
India. In He, Y.; Ji, H.; Li, S.; Liu, Y.; and Chang, C.-H.,
eds., Proceedings of the 2nd Conference of the Asia-Pacific
Chapter of the Association for Computational Linguistics and
the 12th International Joint Conference on Natural Language
Processing (Volume 1: Long Papers), 727–740. Online only:
Association for Computational Linguistics.
Bianchi, F.; Kalluri, P.; Durmus, E.; Ladhak, F.; Cheng, M.;
Nozza, D.; Hashimoto, T.; Jurafsky, D.; Zou, J.; and Caliskan,
A. 2023. Easily Accessible Text-to-Image Generation Am-
plifies Demographic Stereotypes at Large Scale. In Proceed-
ings of the 2023 ACM Conference on Fairness, Accountabil-

--- Page 9 ---

ity, and Transparency, FAccT ’23, 1493–1504. New York,
NY, USA: Association for Computing Machinery. ISBN
9798400701924.
Bianchi, F.; Suzgun, M.; Attanasio, G.; Rottger, P.; Jurafsky,
D.; Hashimoto, T.; and Zou, J. 2024. Safety-Tuned LLaMAs:
Lessons From Improving the Safety of Large Language Mod-
els that Follow Instructions. In The Twelfth International
Conference on Learning Representations.
Bolukbasi, T.; Chang, K.-W.; Zou, J. Y.; Saligrama, V.; and
Kalai, A. T. 2016. Man is to computer programmer as woman
is to homemaker? debiasing word embeddings. Advances in
neural information processing systems, 29.
Brahman, F.; Kumar, S.; Balachandran, V.; Dasigi, P.; Py-
atkin, V.; Ravichander, A.; Wiegreffe, S.; Dziri, N.; Chandu,
K.; Hessel, J.; Tsvetkov, Y.; Smith, N. A.; Choi, Y.; and
Hajishirzi, H. 2024. The Art of Saying No: Contextual Non-
compliance in Language Models. In The Thirty-eight Con-
ference on Neural Information Processing Systems Datasets
and Benchmarks Track.
Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J. D.;
Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell,
A.; et al. 2020.
Language models are few-shot learners.
Advances in neural information processing systems, 33: 1877–
1901.
Caliskan, A.; Bryson, J. J.; and Narayanan, A. 2017. Se-
mantics derived automatically from language corpora contain
human-like biases. Science, 356(6334): 183–186.
Carlini, N.; Nasr, M.; Choquette-Choo, C. A.; Jagielski, M.;
Gao, I.; Koh, P. W.; Ippolito, D.; Tram`er, F.; and Schmidt, L.
2023. Are aligned neural networks adversarially aligned? In
Thirty-seventh Conference on Neural Information Processing
Systems.
Cercas Curry, A.; Abercrombie, G.; and Rieser, V. 2021.
ConvAbuse: Data, Analysis, and Benchmarks for Nuanced
Detection in Conversational AI. In Proceedings of the 2021
Conference on Empirical Methods in Natural Language Pro-
cessing, 7388–7403. Online and Punta Cana, Dominican
Republic: Association for Computational Linguistics.
Chao, P.; Debenedetti, E.; Robey, A.; Andriushchenko, M.;
Croce, F.; Sehwag, V.; Dobriban, E.; Flammarion, N.; Pappas,
G. J.; Tram`er, F.; Hassani, H.; and Wong, E. 2024. Jailbreak-
Bench: An Open Robustness Benchmark for Jailbreaking
Large Language Models. In The Thirty-eight Conference on
Neural Information Processing Systems Datasets and Bench-
marks Track.
Chen, M.; Tworek, J.; Jun, H.; Yuan, Q.; Pinto, H. P. d. O.;
Kaplan, J.; Edwards, H.; Burda, Y.; Joseph, N.; Brockman,
G.; et al. 2021. Evaluating large language models trained on
code. arXiv preprint arXiv:2107.03374.
Chen, Y.; Arunasalam, A.; and Celik, Z. B. 2023. Can Large
Language Models Provide Security & Privacy Advice? Mea-
suring the Ability of LLMs to Refute Misconceptions. In Pro-
ceedings of the 39th Annual Computer Security Applications
Conference, ACSAC ’23, 366–378. New York, NY, USA: As-
sociation for Computing Machinery. ISBN 9798400708862.
Chiang, W.-L.; Zheng, L.; Sheng, Y.; Angelopoulos, A. N.;
Li, T.; Li, D.; Zhang, H.; Zhu, B.; Jordan, M.; Gonzalez, J. E.;
and Stoica, I. 2024. Chatbot Arena: An Open Platform for
Evaluating LLMs by Human Preference. arXiv:2403.04132.
Cui, J.; Chiang, W.-L.; Stoica, I.; and Hsieh, C.-J. 2024. OR-
Bench: An Over-Refusal Benchmark for Large Language
Models. arXiv preprint arXiv:2405.20947.
Cui, S.; Zhang, Z.; Chen, Y.; Zhang, W.; Liu, T.; Wang, S.;
and Liu, T. 2023. Fft: Towards harmlessness evaluation and
analysis for llms with factuality, fairness, toxicity. arXiv
preprint arXiv:2311.18580.
DeepMind, G. 2024. Gemma 2: Improving Open Language
Models at a Practical Size.
Dhamala, J.; Sun, T.; Kumar, V.; Krishna, S.; Pruksachatkun,
Y.; Chang, K.-W.; and Gupta, R. 2021.
BOLD: Dataset
and Metrics for Measuring Biases in Open-Ended Language
Generation. In Proceedings of the 2021 ACM Conference
on Fairness, Accountability, and Transparency, FAccT ’21,
862–872. New York, NY, USA: Association for Computing
Machinery. ISBN 9781450383097.
Dinan, E.; Abercrombie, G.; Bergman, A.; Spruit, S.; Hovy,
D.; Boureau, Y.-L.; and Rieser, V. 2022. SafetyKit: First
Aid for Measuring Safety in Open-domain Conversational
Systems. In Proceedings of the 60th Annual Meeting of
the Association for Computational Linguistics (Volume 1:
Long Papers), 4113–4133. Dublin, Ireland: Association for
Computational Linguistics.
Dinan, E.; Humeau, S.; Chintagunta, B.; and Weston, J. 2019.
Build it Break it Fix it for Dialogue Safety: Robustness from
Adversarial Human Attack. In Proceedings of the 2019 Con-
ference on Empirical Methods in Natural Language Process-
ing and the 9th International Joint Conference on Natural
Language Processing (EMNLP-IJCNLP), 4537–4546. Hong
Kong, China: Association for Computational Linguistics.
Dua, D.; Wang, Y.; Dasigi, P.; Stanovsky, G.; Singh, S.; and
Gardner, M. 2019. DROP: A Reading Comprehension Bench-
mark Requiring Discrete Reasoning Over Paragraphs. In
Burstein, J.; Doran, C.; and Solorio, T., eds., Proceedings of
the 2019 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers), 2368–2378.
Minneapolis, Minnesota: Association for Computational Lin-
guistics.
Durmus, E.; Nguyen, K.; Liao, T.; Schiefer, N.; Askell, A.;
Bakhtin, A.; Chen, C.; Hatfield-Dodds, Z.; Hernandez, D.;
Joseph, N.; Lovitt, L.; McCandlish, S.; Sikder, O.; Tamkin,
A.; Thamkul, J.; Kaplan, J.; Clark, J.; and Ganguli, D. 2024.
Towards Measuring the Representation of Subjective Global
Opinions in Language Models. In First Conference on Lan-
guage Modeling.
Emelin, D.; Le Bras, R.; Hwang, J. D.; Forbes, M.; and
Choi, Y. 2021. Moral Stories: Situated Reasoning about
Norms, Intents, Actions, and their Consequences. In Moens,
M.-F.; Huang, X.; Specia, L.; and Yih, S. W.-t., eds., Pro-
ceedings of the 2021 Conference on Empirical Methods in
Natural Language Processing, 698–718. Online and Punta
Cana, Dominican Republic: Association for Computational
Linguistics.

--- Page 10 ---

Esiobu, D.; Tan, X.; Hosseini, S.; Ung, M.; Zhang, Y.; Fer-
nandes, J.; Dwivedi-Yu, J.; Presani, E.; Williams, A.; and
Smith, E. 2023. ROBBIE: Robust Bias Evaluation of Large
Generative Language Models. In Bouamor, H.; Pino, J.; and
Bali, K., eds., Proceedings of the 2023 Conference on Empir-
ical Methods in Natural Language Processing, 3764–3814.
Singapore: Association for Computational Linguistics.
Felkner, V.; Chang, H.-C. H.; Jang, E.; and May, J. 2023.
WinoQueer: A Community-in-the-Loop Benchmark for Anti-
LGBTQ+ Bias in Large Language Models. In Rogers, A.;
Boyd-Graber, J.; and Okazaki, N., eds., Proceedings of the
61st Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 9126–9140. Toronto,
Canada: Association for Computational Linguistics.
Fleisig, E.; Amstutz, A.; Atalla, C.; Blodgett, S. L.;
Daum´e III, H.; Olteanu, A.; Sheng, E.; Vann, D.; and Wal-
lach, H. 2023. FairPrism: Evaluating Fairness-Related Harms
in Text Generation. In Rogers, A.; Boyd-Graber, J.; and
Okazaki, N., eds., Proceedings of the 61st Annual Meeting
of the Association for Computational Linguistics (Volume 1:
Long Papers), 6231–6251. Toronto, Canada: Association for
Computational Linguistics.
Forbes, M.; Hwang, J. D.; Shwartz, V.; Sap, M.; and Choi, Y.
2020. Social Chemistry 101: Learning to Reason about Social
and Moral Norms. In Webber, B.; Cohn, T.; He, Y.; and Liu,
Y., eds., Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP), 653–
670. Online: Association for Computational Linguistics.
Ganguli, D.; Lovitt, L.; Kernion, J.; Askell, A.; Bai, Y.; Kada-
vath, S.; Mann, B.; Perez, E.; Schiefer, N.; Ndousse, K.; et al.
2022. Red teaming language models to reduce harms: Meth-
ods, scaling behaviors, and lessons learned. arXiv preprint
arXiv:2209.07858.
Gao, L.; Tow, J.; Biderman, S.; Black, S.; DiPofi, A.; Foster,
C.; Golding, L.; Hsu, J.; McDonell, K.; Muennighoff, N.;
Phang, J.; Reynolds, L.; Tang, E.; Thite, A.; Wang, B.; Wang,
K.; and Zou, A. 2021. A framework for few-shot language
model evaluation. In Zenodo. Zenodo.
Garg, N.; Schiebinger, L.; Jurafsky, D.; and Zou, J. 2018.
Word embeddings quantify 100 years of gender and ethnic
stereotypes. Proceedings of the National Academy of Sci-
ences, 115(16): E3635–E3644.
Gehman, S.; Gururangan, S.; Sap, M.; Choi, Y.; and Smith,
N. A. 2020. RealToxicityPrompts: Evaluating Neural Toxic
Degeneration in Language Models. In Findings of the Asso-
ciation for Computational Linguistics: EMNLP 2020, 3356–
3369. Online: Association for Computational Linguistics.
Ghanim, M. A.; Almohaimeed, S.; Zheng, M.; Solihin, Y.;
and Lou, Q. 2024. Jailbreaking LLMs with Arabic Translit-
eration and Arabizi. In Al-Onaizan, Y.; Bansal, M.; and
Chen, Y.-N., eds., Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing, 18584–
18600. Miami, Florida, USA: Association for Computational
Linguistics.
Ghosh, S.; Varshney, P.; Galinkin, E.; and Parisien, C. 2024.
AEGIS: Online Adaptive AI Content Safety Moderation with
Ensemble of LLM Experts. arXiv preprint arXiv:2404.05993.
Guo, Y.; Cui, G.; Yuan, L.; Ding, N.; Sun, Z.; Sun, B.; Chen,
H.; Xie, R.; Zhou, J.; Lin, Y.; Liu, Z.; and Sun, M. 2024.
Controllable Preference Optimization: Toward Controllable
Multi-Objective Alignment. In Al-Onaizan, Y.; Bansal, M.;
and Chen, Y.-N., eds., Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing, 1437–
1454. Miami, Florida, USA: Association for Computational
Linguistics.
Gupta, P.; Yau, L. Q.; Low, H. H.; Lee, I.-S.; Lim, H. M.;
Teoh, Y. X.; Hng, K. J.; Liew, D. W.; Bhardwaj, R.; Bhard-
waj, R.; and Poria, S. 2024a. WalledEval: A Comprehensive
Safety Evaluation Toolkit for Large Language Models. In
Hernandez Farias, D. I.; Hope, T.; and Li, M., eds., Pro-
ceedings of the 2024 Conference on Empirical Methods in
Natural Language Processing: System Demonstrations, 397–
407. Miami, Florida, USA: Association for Computational
Linguistics.
Gupta, V.; Venkit, P. N.; Laurenc¸on, H.; Wilson, S.; and
Passonneau, R. J. 2024b. CALM : A Multi-task Benchmark
for Comprehensive Assessment of Language Model Bias. In
First Conference on Language Modeling.
Hall, S. M.; Abrantes, F. G.; Zhu, H.; Sodunke, G.; Shtedrit-
ski, A.; and Kirk, H. R. 2023. VisoGender: A dataset for
benchmarking gender bias in image-text pronoun resolution.
In Thirty-seventh Conference on Neural Information Process-
ing Systems Datasets and Benchmarks Track.
Han, S.; Rao, K.; Ettinger, A.; Jiang, L.; Lin, B. Y.; Lam-
bert, N.; Choi, Y.; and Dziri, N. 2024a. WildGuard: Open
One-stop Moderation Tools for Safety Risks, Jailbreaks, and
Refusals of LLMs. In The Thirty-eight Conference on Neural
Information Processing Systems Datasets and Benchmarks
Track.
Han, T.; Kumar, A.; Agarwal, C.; and Lakkaraju, H. 2024b.
MedSafetyBench: Evaluating and Improving the Medical
Safety of Large Language Models. In The Thirty-eight Con-
ference on Neural Information Processing Systems Datasets
and Benchmarks Track.
Hansson, S.; Mavromatakis, K.; Adesam, Y.; Bouma, G.; and
Dann´ells, D. 2021. The Swedish Winogender Dataset. In
Dobnik, S.; and Øvrelid, L., eds., Proceedings of the 23rd
Nordic Conference on Computational Linguistics (NoDaL-
iDa), 452–459. Reykjavik, Iceland (Online): Link¨oping Uni-
versity Electronic Press, Sweden.
Hartvigsen, T.; Gabriel, S.; Palangi, H.; Sap, M.; Ray, D.;
and Kamar, E. 2022. ToxiGen: A Large-Scale Machine-
Generated Dataset for Adversarial and Implicit Hate Speech
Detection. In Proceedings of the 60th Annual Meeting of
the Association for Computational Linguistics (Volume 1:
Long Papers), 3309–3326. Dublin, Ireland: Association for
Computational Linguistics.
Hendrycks, D.; Burns, C.; Basart, S.; Critch, A.; Li, J.; Song,
D.; and Steinhardt, J. 2021. Aligning AI With Shared Human
Values. In International Conference on Learning Representa-
tions.
Hendrycks, D.; Burns, C.; Basart, S.; Zou, A.; Mazeika, M.;
Song, D.; and Steinhardt, J. 2020. Measuring Massive Multi-

--- Page 11 ---

task Language Understanding. In International Conference
on Learning Representations.
Hendrycks, D.; Mazeika, M.; Zou, A.; Patel, S.; Zhu, C.;
Navarro, J.; Song, D.; Li, B.; and Steinhardt, J. 2022. What
Would Jiminy Cricket Do? Towards Agents That Behave
Morally. In Thirty-fifth Conference on Neural Information
Processing Systems Datasets and Benchmarks Track (Round
2).
Holtermann, C.; R¨ottger, P.; Dill, T.; and Lauscher, A.
2024. Evaluating the Elementary Multilingual Capabilities
of Large Language Models with MultiQ. arXiv preprint
arXiv:2403.03814.
Huang, J.; Shao, H.; and Chang, K. C.-C. 2022. Are Large
Pre-Trained Language Models Leaking Your Personal In-
formation? In Goldberg, Y.; Kozareva, Z.; and Zhang, Y.,
eds., Findings of the Association for Computational Linguis-
tics: EMNLP 2022, 2038–2047. Abu Dhabi, United Arab
Emirates: Association for Computational Linguistics.
Huang, K.; Liu, X.; Guo, Q.; Sun, T.; Sun, J.; Wang, Y.; Zhou,
Z.; Wang, Y.; Teng, Y.; Qiu, X.; Wang, Y.; and Lin, D. 2024a.
Flames: Benchmarking Value Alignment of LLMs in Chinese.
In Duh, K.; Gomez, H.; and Bethard, S., eds., Proceedings of
the 2024 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), 4551–4591. Mexico
City, Mexico: Association for Computational Linguistics.
Huang, Y.; Gupta, S.; Xia, M.; Li, K.; and Chen, D. 2024b.
Catastrophic Jailbreak of Open-source LLMs via Exploiting
Generation. In The Twelfth International Conference on
Learning Representations.
Huang, Y.; and Xiong, D. 2024. CBBQ: A Chinese Bias
Benchmark Dataset Curated with Human-AI Collaboration
for Large Language Models. In Calzolari, N.; Kan, M.-Y.;
Hoste, V.; Lenci, A.; Sakti, S.; and Xue, N., eds., Proceed-
ings of the 2024 Joint International Conference on Compu-
tational Linguistics, Language Resources and Evaluation
(LREC-COLING 2024), 2917–2929. Torino, Italia: ELRA
and ICCL.
Jha, A.; Mostafazadeh Davani, A.; Reddy, C. K.; Dave, S.;
Prabhakaran, V.; and Dev, S. 2023. SeeGULL: A Stereotype
Benchmark with Broad Geo-Cultural Coverage Leveraging
Generative Models. In Rogers, A.; Boyd-Graber, J.; and
Okazaki, N., eds., Proceedings of the 61st Annual Meeting
of the Association for Computational Linguistics (Volume 1:
Long Papers), 9851–9870. Toronto, Canada: Association for
Computational Linguistics.
Ji, J.; Liu, M.; Dai, J.; Pan, X.; Zhang, C.; Bian, C.; Chen, B.;
Sun, R.; Wang, Y.; and Yang, Y. 2023. BeaverTails: Towards
Improved Safety Alignment of LLM via a Human-Preference
Dataset. In Thirty-seventh Conference on Neural Information
Processing Systems Datasets and Benchmarks Track.
Jiang, L.; Rao, K.; Han, S.; Ettinger, A.; Brahman, F.; Kumar,
S.; Mireshghallah, N.; Lu, X.; Sap, M.; Choi, Y.; and Dziri,
N. 2024. WildTeaming at Scale: From In-the-Wild Jailbreaks
to (Adversarially) Safer Language Models. In The Thirty-
eighth Annual Conference on Neural Information Processing
Systems.
Jin, J.; Kim, J.; Lee, N.; Yoo, H.; Oh, A.; and Lee, H. 2024a.
KoBBQ: Korean Bias Benchmark for Question Answering.
Transactions of the Association for Computational Linguis-
tics, 12: 507–524.
Jin, Z.; Kleiman-Weiner, M.; Piatti, G.; Levine, S.; Liu, J.;
Adauto, F. G.; Ortu, F.; Strausz, A.; Sachan, M.; Mihalcea,
R.; Choi, Y.; and Sch¨olkopf, B. 2024b. Multilingual Trolley
Problems for Language Models. In Pluralistic Alignment
Workshop at NeurIPS 2024.
Jin, Z.; Levine, S.; Adauto, F. G.; Kamal, O.; Sap, M.; Sachan,
M.; Mihalcea, R.; Tenenbaum, J. B.; and Sch¨olkopf, B. 2022.
When to Make Exceptions: Exploring Language Models as
Accounts of Human Moral Judgment. In Oh, A. H.; Agarwal,
A.; Belgrave, D.; and Cho, K., eds., Advances in Neural
Information Processing Systems.
Joshi, P.; Santy, S.; Budhiraja, A.; Bali, K.; and Choudhury,
M. 2020. The State and Fate of Linguistic Diversity and
Inclusion in the NLP World. In Proceedings of the 58th
Annual Meeting of the Association for Computational Lin-
guistics, 6282–6293. Online: Association for Computational
Linguistics.
Kaiyom, F.; Ahmed, A.; Mai, Y.; Klyman, K.; Bommasani,
R.; and Liang, P. 2024. HELM Safety: Towards Standardized
Safety Evaluations of Language Models. Stanford Center for
Research on Foundation Models.
Kim, H.; Yu, Y.; Jiang, L.; Lu, X.; Khashabi, D.; Kim, G.;
Choi, Y.; and Sap, M. 2022.
ProsocialDialog: A Proso-
cial Backbone for Conversational Agents. In Goldberg, Y.;
Kozareva, Z.; and Zhang, Y., eds., Proceedings of the 2022
Conference on Empirical Methods in Natural Language Pro-
cessing, 4005–4029. Abu Dhabi, United Arab Emirates: As-
sociation for Computational Linguistics.
Kirk, H. R.; Jun, Y.; Volpin, F.; Iqbal, H.; Benussi, E.; Dreyer,
F.; Shtedritski, A.; and Asano, Y. 2021. Bias out-of-the-box:
An empirical analysis of intersectional occupational biases
in popular generative language models. Advances in neural
information processing systems, 34: 2611–2624.
Kirk, H. R.; Whitefield, A.; R¨ottger, P.; Bean, A. M.; Mar-
gatina, K.; Mosquera, R.; Ciro, J. M.; Bartolo, M.; Williams,
A.; He, H.; Vidgen, B.; and Hale, S. A. 2024. The PRISM
Alignment Dataset: What Participatory, Representative and
Individualised Human Feedback Reveals About the Subjec-
tive and Multicultural Alignment of Large Language Models.
In The Thirty-eight Conference on Neural Information Pro-
cessing Systems Datasets and Benchmarks Track.
Koenecke, A.; Nam, A.; Lake, E.; Nudell, J.; Quartey, M.;
Mengesha, Z.; Toups, C.; Rickford, J. R.; Jurafsky, D.; and
Goel, S. 2020. Racial disparities in automated speech recog-
nition. Proceedings of the National Academy of Sciences,
117(14): 7684–7689.
Kour, G.; Zalmanovici, M.; Zwerdling, N.; Goldbraich, E.;
Fandina, O.; Anaby Tavor, A.; Raz, O.; and Farchi, E. 2023.
Unveiling Safety Vulnerabilities of Large Language Models.
In Gehrmann, S.; Wang, A.; Sedoc, J.; Clark, E.; Dhole, K.;
Chandu, K. R.; Santus, E.; and Sedghamiz, H., eds., Proceed-
ings of the Third Workshop on Natural Language Generation,

--- Page 12 ---

Evaluation, and Metrics (GEM), 111–127. Singapore: Asso-
ciation for Computational Linguistics.
LakeraAI. 2023a. Gandalf Prompt Injection. In Hugging
Face Dataset.
LakeraAI. 2023b. Mosscap Prompt Injection. In Hugging
Face Dataset.
Lambert, N.; Pyatkin, V.; Morrison, J.; Miranda, L.; Lin,
B. Y.; Chandu, K.; Dziri, N.; Kumar, S.; Zick, T.; Choi,
Y.; Smith, N. A.; and Hajishirzi, H. 2024.
Reward-
Bench: Evaluating Reward Models for Language Modeling.
arXiv:2403.13787.
Lee, J.; Kim, M.; Kim, S.; Kim, J.; Won, S.; Lee, H.; and
Choi, E. 2024. KorNAT: LLM Alignment Benchmark for Ko-
rean Social Values and Common Knowledge. In Ku, L.-W.;
Martins, A.; and Srikumar, V., eds., Findings of the Associa-
tion for Computational Linguistics: ACL 2024, 11177–11213.
Bangkok, Thailand: Association for Computational Linguis-
tics.
Levy, S.; Adler, W.; Karver, T. S.; Dredze, M.; and Kaufman,
M. R. 2024. Gender Bias in Decision-Making with Large
Language Models: A Study of Relationship Conflicts. In
Al-Onaizan, Y.; Bansal, M.; and Chen, Y.-N., eds., Findings
of the Association for Computational Linguistics: EMNLP
2024, 5777–5800. Miami, Florida, USA: Association for
Computational Linguistics.
Levy, S.; Allaway, E.; Subbiah, M.; Chilton, L.; Patton, D.;
McKeown, K.; and Wang, W. Y. 2022. SafeText: A Bench-
mark for Exploring Physical Safety in Language Models. In
Proceedings of the 2022 Conference on Empirical Methods
in Natural Language Processing, 2407–2421. Abu Dhabi,
United Arab Emirates: Association for Computational Lin-
guistics.
Li, L.; Dong, B.; Wang, R.; Hu, X.; Zuo, W.; Lin, D.; Qiao, Y.;
and Shao, J. 2024a. SALAD-Bench: A Hierarchical and Com-
prehensive Safety Benchmark for Large Language Models.
In Ku, L.-W.; Martins, A.; and Srikumar, V., eds., Findings
of the Association for Computational Linguistics: ACL 2024,
3923–3954. Bangkok, Thailand: Association for Computa-
tional Linguistics.
Li, N.; Pan, A.; Gopal, A.; Yue, S.; Berrios, D.; Gatti, A.;
Li, J. D.; Dombrowski, A.-K.; Goel, S.; Mukobi, G.; Helm-
Burger, N.; Lababidi, R.; Justen, L.; Liu, A. B.; Chen, M.;
Barrass, I.; Zhang, O.; Zhu, X.; Tamirisa, R.; Bharathi, B.;
Herbert-Voss, A.; Breuer, C. B.; Zou, A.; Mazeika, M.; Wang,
Z.; Oswal, P.; Lin, W.; Hunt, A. A.; Tienken-Harder, J.;
Shih, K. Y.; Talley, K.; Guan, J.; Steneker, I.; Campbell, D.;
Jokubaitis, B.; Basart, S.; Fitz, S.; Kumaraguru, P.; Karmakar,
K. K.; Tupakula, U.; Varadharajan, V.; Shoshitaishvili, Y.;
Ba, J.; Esvelt, K. M.; Wang, A.; and Hendrycks, D. 2024b.
The WMDP Benchmark: Measuring and Reducing Malicious
Use with Unlearning. In Forty-first International Conference
on Machine Learning.
Li, T.; Khashabi, D.; Khot, T.; Sabharwal, A.; and Srikumar,
V. 2020. UNQOVERing Stereotyping Biases via Underspeci-
fied Questions. In Cohn, T.; He, Y.; and Liu, Y., eds., Findings
of the Association for Computational Linguistics: EMNLP
2020, 3475–3489. Online: Association for Computational
Linguistics.
Liang, P.; Bommasani, R.; Lee, T.; Tsipras, D.; Soylu, D.;
Yasunaga, M.; Zhang, Y.; Narayanan, D.; Wu, Y.; Kumar,
A.; et al. 2023. Holistic Evaluation of Language Models.
Transactions on Machine Learning Research.
Liang, P. P.; Wu, C.; Morency, L.-P.; and Salakhutdinov, R.
2021. Towards understanding and mitigating social biases in
language models. In International Conference on Machine
Learning, 6565–6576. PMLR.
Lin, S.; Hilton, J.; and Evans, O. 2022. TruthfulQA: Mea-
suring How Models Mimic Human Falsehoods. In Muresan,
S.; Nakov, P.; and Villavicencio, A., eds., Proceedings of the
60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 3214–3252. Dublin,
Ireland: Association for Computational Linguistics.
Lin, Z.; Wang, Z.; Tong, Y.; Wang, Y.; Guo, Y.; Wang, Y.; and
Shang, J. 2023. ToxicChat: Unveiling Hidden Challenges
of Toxicity Detection in Real-World User-AI Conversation.
In Bouamor, H.; Pino, J.; and Bali, K., eds., Findings of the
Association for Computational Linguistics: EMNLP 2023,
4694–4702. Singapore: Association for Computational Lin-
guistics.
Liu, C.; Zhao, F.; Qing, L.; Kang, Y.; Sun, C.; Kuang, K.;
and Wu, F. 2023. A chinese prompt attack dataset for llms
with evil content. arXiv preprint arXiv:2309.11830.
Lourie, N.; Le Bras, R.; and Choi, Y. 2021. Scruples: A
corpus of community ethical judgments on 32,000 real-life
anecdotes. In Proceedings of the AAAI Conference on Artifi-
cial Intelligence, volume 35, 13470–13479.
Luccioni, S.; Akiki, C.; Mitchell, M.; and Jernite, Y. 2024.
Stable bias: Evaluating societal representations in diffusion
models. Advances in Neural Information Processing Systems,
36.
Manerba, M.; Stanczak, K.; Guidotti, R.; and Augenstein,
I. 2024. Social Bias Probing: Fairness Benchmarking for
Language Models. In Al-Onaizan, Y.; Bansal, M.; and Chen,
Y.-N., eds., Proceedings of the 2024 Conference on Empiri-
cal Methods in Natural Language Processing, 14653–14671.
Miami, Florida, USA: Association for Computational Lin-
guistics.
Mazeika, M.; Phan, L.; Yin, X.; Zou, A.; Wang, Z.; Mu,
N.; Sakhaee, E.; Li, N.; Basart, S.; Li, B.; Forsyth, D.; and
Hendrycks, D. 2024. HarmBench: A Standardized Evaluation
Framework for Automated Red Teaming and Robust Refusal.
In Forty-first International Conference on Machine Learning.
Mazeika, M.; Zou, A.; Mu, N.; Phan, L.; Wang, Z.; Yu, C.;
Khoja, A.; Jiang, F.; O’Gara, A.; Sakhaee, E.; Xiang, Z.; Ra-
jabi, A.; Hendrycks, D.; Poovendran, R.; Li, B.; and Forsyth,
D. 2023. TDC 2023 (LLM Edition): The Trojan Detection
Challenge. In NeurIPS Competition Track.
Meta. 2024. The Llama 3 Herd of Models.
Meyer, J.; Rauchenstein, L.; Eisenberg, J. D.; and Howell,
N. 2020. Artie Bias Corpus: An Open Dataset for Detecting
Demographic Bias in Speech Applications. In Calzolari, N.;
B´echet, F.; Blache, P.; Choukri, K.; Cieri, C.; Declerck, T.;

--- Page 13 ---

Goggi, S.; Isahara, H.; Maegaard, B.; Mariani, J.; Mazo, H.;
Moreno, A.; Odijk, J.; and Piperidis, S., eds., Proceedings
of the Twelfth Language Resources and Evaluation Confer-
ence, 6462–6468. Marseille, France: European Language
Resources Association. ISBN 979-10-95546-34-4.
Mireshghallah, N.; Kim, H.; Zhou, X.; Tsvetkov, Y.; Sap,
M.; Shokri, R.; and Choi, Y. 2024. Can LLMs Keep a Se-
cret? Testing Privacy Implications of Language Models via
Contextual Integrity Theory. In The Twelfth International
Conference on Learning Representations.
Mou, Y.; Zhang, S.; and Ye, W. 2024. SG-Bench: Evaluating
LLM Safety Generalization Across Diverse Tasks and Prompt
Types. In The Thirty-eight Conference on Neural Information
Processing Systems Datasets and Benchmarks Track.
Mu, N.; Chen, S.; Wang, Z.; Chen, S.; Karamardian, D.;
Aljeraisy, L.; Alomair, B.; Hendrycks, D.; and Wagner, D.
2024. Can LLMs Follow Simple Rules? arXiv:2311.04235.
Nadeem, M.; Bethke, A.; and Reddy, S. 2021. StereoSet:
Measuring stereotypical bias in pretrained language models.
In Zong, C.; Xia, F.; Li, W.; and Navigli, R., eds., Proceedings
of the 59th Annual Meeting of the Association for Compu-
tational Linguistics and the 11th International Joint Con-
ference on Natural Language Processing (Volume 1: Long
Papers), 5356–5371. Online: Association for Computational
Linguistics.
Nangia, N.; Vania, C.; Bhalerao, R.; and Bowman, S. R. 2020.
CrowS-Pairs: A Challenge Dataset for Measuring Social Bi-
ases in Masked Language Models. In Webber, B.; Cohn, T.;
He, Y.; and Liu, Y., eds., Proceedings of the 2020 Confer-
ence on Empirical Methods in Natural Language Processing
(EMNLP), 1953–1967. Online: Association for Computa-
tional Linguistics.
N´ev´eol, A.; Dupont, Y.; Bezanc¸on, J.; and Fort, K. 2022.
French CrowS-Pairs: Extending a challenge dataset for mea-
suring social bias in masked language models to a language
other than English. In Muresan, S.; Nakov, P.; and Villav-
icencio, A., eds., Proceedings of the 60th Annual Meeting
of the Association for Computational Linguistics (Volume 1:
Long Papers), 8521–8531. Dublin, Ireland: Association for
Computational Linguistics.
Nozza, D.; Bianchi, F.; and Hovy, D. 2021. HONEST: Mea-
suring Hurtful Sentence Completion in Language Models. In
Proceedings of the 2021 Conference of the North American
Chapter of the Association for Computational Linguistics:
Human Language Technologies, 2398–2406. Online: Associ-
ation for Computational Linguistics.
Ontocord.AI. 2023. OIG-Moderation. In Hugging Face
Dataset.
Ouyang, S.; Wang, S.; Liu, Y.; Zhong, M.; Jiao, Y.; Iter, D.;
Pryzant, R.; Zhu, C.; Ji, H.; and Han, J. 2023. The Shifted
and The Overlooked: A Task-oriented Investigation of User-
GPT Interactions. In Bouamor, H.; Pino, J.; and Bali, K.,
eds., Proceedings of the 2023 Conference on Empirical Meth-
ods in Natural Language Processing, 2375–2393. Singapore:
Association for Computational Linguistics.
Pan, A.; Chan, J. S.; Zou, A.; Li, N.; Basart, S.; Woodside,
T.; Zhang, H.; Emmons, S.; and Hendrycks, D. 2023. Do
the rewards justify the means? measuring trade-offs between
rewards and ethical behavior in the machiavelli benchmark.
In International Conference on Machine Learning, 26837–
26867. PMLR.
Parrish, A.; Chen, A.; Nangia, N.; Padmakumar, V.; Phang,
J.; Thompson, J.; Htut, P. M.; and Bowman, S. 2022. BBQ:
A hand-built bias benchmark for question answering. In
Muresan, S.; Nakov, P.; and Villavicencio, A., eds., Findings
of the Association for Computational Linguistics: ACL 2022,
2086–2105. Dublin, Ireland: Association for Computational
Linguistics.
Parrish, A.; Kirk, H. R.; Quaye, J.; Rastogi, C.; Bartolo, M.;
Inel, O.; Ciro, J.; Mosquera, R.; Howard, A.; Cukierski, W.;
et al. 2023. Adversarial Nibbler: A Data-Centric Challenge
for Improving the Safety of Text-to-Image Models. arXiv
preprint arXiv:2305.14384.
Perez, E.; Ringer, S.; Lukosiute, K.; Nguyen, K.; Chen, E.;
Heiner, S.; Pettit, C.; Olsson, C.; Kundu, S.; Kadavath, S.;
Jones, A.; Chen, A.; Mann, B.; Israel, B.; Seethor, B.; McK-
innon, C.; Olah, C.; Yan, D.; Amodei, D.; Amodei, D.; Drain,
D.; Li, D.; Tran-Johnson, E.; Khundadze, G.; Kernion, J.;
Landis, J.; Kerr, J.; Mueller, J.; Hyun, J.; Landau, J.; Ndousse,
K.; Goldberg, L.; Lovitt, L.; Lucas, M.; Sellitto, M.; Zhang,
M.; Kingsland, N.; Elhage, N.; Joseph, N.; Mercado, N.; Das-
Sarma, N.; Rausch, O.; Larson, R.; McCandlish, S.; Johnston,
S.; Kravec, S.; El Showk, S.; Lanham, T.; Telleen-Lawton, T.;
Brown, T.; Henighan, T.; Hume, T.; Bai, Y.; Hatfield-Dodds,
Z.; Clark, J.; Bowman, S. R.; Askell, A.; Grosse, R.; Her-
nandez, D.; Ganguli, D.; Hubinger, E.; Schiefer, N.; and Ka-
plan, J. 2023. Discovering Language Model Behaviors with
Model-Written Evaluations. In Rogers, A.; Boyd-Graber, J.;
and Okazaki, N., eds., Findings of the Association for Com-
putational Linguistics: ACL 2023, 13387–13434. Toronto,
Canada: Association for Computational Linguistics.
Pikuliak, M.; Oresko, S.; Hrckova, A.; and Simko, M. 2024.
Women Are Beautiful, Men Are Leaders: Gender Stereotypes
in Machine Translation and Language Modeling.
In Al-
Onaizan, Y.; Bansal, M.; and Chen, Y.-N., eds., Findings
of the Association for Computational Linguistics: EMNLP
2024, 3060–3083. Miami, Florida, USA: Association for
Computational Linguistics.
Pistilli, G.; Leidinger, A.; Jernite, Y.; Kasirzadeh, A.; Luc-
cioni, A. S.; and Mitchell, M. 2024. CIVICS: Building a
Dataset for Examining Culturally-Informed Values in Large
Language Models. Proceedings of the AAAI/ACM Confer-
ence on AI, Ethics, and Society, 7(1): 1132–1144.
Qi, X.; Zeng, Y.; Xie, T.; Chen, P.-Y.; Jia, R.; Mittal, P.; and
Henderson, P. 2024. Fine-tuning Aligned Language Mod-
els Compromises Safety, Even When Users Do Not Intend
To! In The Twelfth International Conference on Learning
Representations.
Qiu, H.; Zhang, S.; Li, A.; He, H.; and Lan, Z. 2023. La-
tent jailbreak: A benchmark for evaluating text safety and
output robustness of large language models. arXiv preprint
arXiv:2307.08487.
Radharapu, B.; Robinson, K.; Aroyo, L.; and Lahoti, P. 2023.
AART: AI-Assisted Red-Teaming with Diverse Data Genera-
tion for New LLM-powered Applications. In Wang, M.; and

--- Page 14 ---

Zitouni, I., eds., Proceedings of the 2023 Conference on Em-
pirical Methods in Natural Language Processing: Industry
Track, 380–395. Singapore: Association for Computational
Linguistics.
Rashkin, H.; Smith, E. M.; Li, M.; and Boureau, Y.-L. 2019.
Towards Empathetic Open-domain Conversation Models: A
New Benchmark and Dataset. In Korhonen, A.; Traum, D.;
and M`arquez, L., eds., Proceedings of the 57th Annual Meet-
ing of the Association for Computational Linguistics, 5370–
5381. Florence, Italy: Association for Computational Lin-
guistics.
Reimao, R.; and Tzerpos, V. 2019. For: A dataset for syn-
thetic speech detection. In 2019 International Conference on
Speech Technology and Human-Computer Dialogue (SpeD),
1–10. IEEE.
Reuel, A.; Hardy, A.; Smith, C.; Lamparth, M.; Hardy, M.;
and Kochenderfer, M. 2024. BetterBench: Assessing AI
Benchmarks, Uncovering Issues, and Establishing Best Prac-
tices. In The Thirty-eight Conference on Neural Information
Processing Systems Datasets and Benchmarks Track.
Ricker, J.; Damm, S.; Holz, T.; and Fischer, A. 2022. Towards
the detection of diffusion model deepfakes. arXiv preprint
arXiv:2210.14571.
R¨ottger, P.; Kirk, H.; Vidgen, B.; Attanasio, G.; Bianchi, F.;
and Hovy, D. 2024. XSTest: A Test Suite for Identifying
Exaggerated Safety Behaviours in Large Language Models.
In Duh, K.; Gomez, H.; and Bethard, S., eds., Proceedings of
the 2024 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language
Technologies (Volume 1: Long Papers), 5377–5400. Mexico
City, Mexico: Association for Computational Linguistics.
Rudinger, R.; Naradowsky, J.; Leonard, B.; and Van Durme,
B. 2018. Gender Bias in Coreference Resolution. In Walker,
M.; Ji, H.; and Stent, A., eds., Proceedings of the 2018 Con-
ference of the North American Chapter of the Association
for Computational Linguistics: Human Language Technolo-
gies, Volume 2 (Short Papers), 8–14. New Orleans, Louisiana:
Association for Computational Linguistics.
Santurkar, S.; Durmus, E.; Ladhak, F.; Lee, C.; Liang, P.; and
Hashimoto, T. 2023. Whose opinions do language models
reflect? In Proceedings of the 40th International Conference
on Machine Learning, ICML’23. JMLR.org.
Scherrer, N.; Shi, C.; Feder, A.; and Blei, D. 2023. Evaluat-
ing the Moral Beliefs Encoded in LLMs. In Thirty-seventh
Conference on Neural Information Processing Systems.
Schulhoff, S.; Pinto, J.; Khan, A.; Bouchard, L.-F.; Si, C.;
Anati, S.; Tagliabue, V.; Kost, A.; Carnahan, C.; and Boyd-
Graber, J. 2023. Ignore This Title and HackAPrompt: Ex-
posing Systemic Vulnerabilities of LLMs Through a Global
Prompt Hacking Competition. In Bouamor, H.; Pino, J.; and
Bali, K., eds., Proceedings of the 2023 Conference on Empir-
ical Methods in Natural Language Processing, 4945–4977.
Singapore: Association for Computational Linguistics.
Schwemmer, C.; Knight, C.; Bello-Pardo, E. D.; Oklobdzija,
S.; Schoonvelde, M.; and Lockhart, J. W. 2020. Diagnos-
ing gender bias in image recognition systems. Socius, 6:
2378023120967171.
Shaikh, O.; Zhang, H.; Held, W.; Bernstein, M.; and Yang,
D. 2023. On Second Thought, Let’s Not Think Step by Step!
Bias and Toxicity in Zero-Shot Reasoning. In Rogers, A.;
Boyd-Graber, J.; and Okazaki, N., eds., Proceedings of the
61st Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 4454–4470. Toronto,
Canada: Association for Computational Linguistics.
Sharma, M.; Tong, M.; Korbak, T.; Duvenaud, D.; Askell, A.;
Bowman, S. R.; DURMUS, E.; Hatfield-Dodds, Z.; Johnston,
S. R.; Kravec, S. M.; Maxwell, T.; McCandlish, S.; Ndousse,
K.; Rausch, O.; Schiefer, N.; Yan, D.; Zhang, M.; and Perez,
E. 2024. Towards Understanding Sycophancy in Language
Models. In The Twelfth International Conference on Learning
Representations.
Shen, X.; Chen, Z.; Backes, M.; Shen, Y.; and Zhang, Y.
2024. ” do anything now”: Characterizing and evaluating
in-the-wild jailbreak prompts on large language models. In
Proceedings of the 2024 on ACM SIGSAC Conference on
Computer and Communications Security, 1671–1685.
Sheng, E.; Chang, K.-W.; Natarajan, P.; and Peng, N. 2019.
The Woman Worked as a Babysitter: On Biases in Language
Generation. In Inui, K.; Jiang, J.; Ng, V.; and Wan, X., eds.,
Proceedings of the 2019 Conference on Empirical Methods
in Natural Language Processing and the 9th International
Joint Conference on Natural Language Processing (EMNLP-
IJCNLP), 3407–3412. Hong Kong, China: Association for
Computational Linguistics.
Shi, C.; Wang, X.; Ge, Q.; Gao, S.; Yang, X.; Gui, T.;
Zhang, Q.; Huang, X.; Zhao, X.; and Lin, D. 2024. Nav-
igating the overkill in large language models. arXiv preprint
arXiv:2401.17633.
Siddiq, M. L.; and Santos, J. C. S. 2022. SecurityEval dataset:
mining vulnerability examples to evaluate machine learning-
based code generation techniques. In Proceedings of the 1st
International Workshop on Mining Software Repositories Ap-
plications for Privacy and Security, MSR4P&S 2022, 29–33.
New York, NY, USA: Association for Computing Machinery.
ISBN 9781450394574.
Smith, E. M.; Hall, M.; Kambadur, M.; Presani, E.; and
Williams, A. 2022. “I’m sorry to hear that”: Finding New Bi-
ases in Language Models with a Holistic Descriptor Dataset.
In Goldberg, Y.; Kozareva, Z.; and Zhang, Y., eds., Proceed-
ings of the 2022 Conference on Empirical Methods in Natural
Language Processing, 9180–9211. Abu Dhabi, United Arab
Emirates: Association for Computational Linguistics.
Sotnikova, A.; Cao, Y. T.; Daum´e III, H.; and Rudinger,
R. 2021. Analyzing Stereotypes in Generative Text Infer-
ence Tasks. In Zong, C.; Xia, F.; Li, W.; and Navigli, R.,
eds., Findings of the Association for Computational Linguis-
tics: ACL-IJCNLP 2021, 4052–4065. Online: Association for
Computational Linguistics.
Souly, A.; Lu, Q.; Bowen, D.; Trinh, T.; Hsieh, E.; Pandey, S.;
Abbeel, P.; Svegliato, J.; Emmons, S.; Watkins, O.; and Toyer,
S. 2024. A StrongREJECT for Empty Jailbreaks. In ICLR
2024 Workshop on Reliable and Responsible Foundation
Models.

--- Page 15 ---

Srivastava, A.; Rastogi, A.; Rao, A.; Shoeb, A. A. M.; Abid,
A.; Fisch, A.; Brown, A. R.; Santoro, A.; Gupta, A.; Garriga-
Alonso, A.; et al. 2023. Beyond the Imitation Game: Quanti-
fying and extrapolating the capabilities of language models.
Transactions on Machine Learning Research.
Sun, D.; Abzaliev, A.; Kotek, H.; Klein, C.; Xiu, Z.; and
Williams, J. 2023a. DELPHI: Data for Evaluating LLMs’
Performance in Handling Controversial Issues. In Wang,
M.; and Zitouni, I., eds., Proceedings of the 2023 Confer-
ence on Empirical Methods in Natural Language Processing:
Industry Track, 820–827. Singapore: Association for Compu-
tational Linguistics.
Sun, H.; Xu, G.; Deng, J.; Cheng, J.; Zheng, C.; Zhou, H.;
Peng, N.; Zhu, X.; and Huang, M. 2022. On the Safety of
Conversational Models: Taxonomy, Dataset, and Benchmark.
In Muresan, S.; Nakov, P.; and Villavicencio, A., eds., Find-
ings of the Association for Computational Linguistics: ACL
2022, 3906–3923. Dublin, Ireland: Association for Computa-
tional Linguistics.
Sun, H.; Zhang, Z.; Deng, J.; Cheng, J.; and Huang, M. 2023b.
Safety assessment of chinese large language models. arXiv
preprint arXiv:2304.10436.
Sun, L.; Huang, Y.; Wang, H.; Wu, S.; Zhang, Q.; Gao, C.;
Huang, Y.; Lyu, W.; Zhang, Y.; Li, X.; et al. 2024. Trustllm:
Trustworthiness in large language models. arXiv preprint
arXiv:2401.05561.
Tamkin, A.; Askell, A.; Lovitt, L.; Durmus, E.; Joseph, N.;
Kravec, S.; Nguyen, K.; Kaplan, J.; and Ganguli, D. 2023a.
Evaluating and mitigating discrimination in language model
decisions. arXiv preprint arXiv:2312.03689.
Tamkin, A.; Askell, A.; Lovitt, L.; Durmus, E.; Joseph, N.;
Kravec, S.; Nguyen, K.; Kaplan, J.; and Ganguli, D. 2023b.
Evaluating and mitigating discrimination in language model
decisions. arXiv preprint arXiv:2312.03689.
Tan, X. E.; Hansanti, P.; Wood, C.; Yu, B.; Ropers, C.; and
Costa-juss`a, M. R. 2024. Towards massive multilingual holis-
tic bias. arXiv preprint arXiv:2407.00486.
Tedeschi, S.; Friedrich, F.; Schramowski, P.; Kersting, K.;
Navigli, R.; Nguyen, H.; and Li, B. 2024.
ALERT: A
Comprehensive Benchmark for Assessing Large Language
Models’ Safety through Red Teaming.
arXiv preprint
arXiv:2404.08676.
Touvron, H.; Lavril, T.; Izacard, G.; Martinet, X.; Lachaux,
M.-A.; Lacroix, T.; Rozi`ere, B.; Goyal, N.; Hambro, E.;
Azhar, F.; et al. 2023. Llama: Open and efficient founda-
tion language models. arXiv preprint arXiv:2302.13971.
Toyer, S.; Watkins, O.; Mendes, E.; Svegliato, J.; Bailey, L.;
Wang, T.; Ong, I.; Elmaaroufi, K.; Abbeel, P.; Darrell, T.;
Ritter, A.; and Russell, S. 2023. Tensor Trust: Interpretable
Prompt Injection Attacks from an Online Game. In NeurIPS
2023 Workshop on Instruction Tuning and Instruction Fol-
lowing.
Ung, M.; Xu, J.; and Boureau, Y.-L. 2022. SaFeRDialogues:
Taking Feedback Gracefully after Conversational Safety Fail-
ures. In Muresan, S.; Nakov, P.; and Villavicencio, A., eds.,
Proceedings of the 60th Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long Papers),
6462–6481. Dublin, Ireland: Association for Computational
Linguistics.
Vidgen, B.; Agrawal, A.; Ahmed, A. M.; Akinwande, V.; Al-
Nuaimi, N.; Alfaraj, N.; Alhajjar, E.; Aroyo, L.; Bavalatti, T.;
Bartolo, M.; Blili-Hamelin, B.; Bollacker, K.; Bomassani, R.;
Boston, M. F.; Campos, S.; Chakra, K.; Chen, C.; Coleman,
C.; Coudert, Z. D.; Derczynski, L.; Dutta, D.; Eisenberg, I.;
Ezick, J.; Frase, H.; Fuller, B.; Gandikota, R.; Gangavarapu,
A.; Gangavarapu, A.; Gealy, J.; Ghosh, R.; Goel, J.; Gohar,
U.; Goswami, S.; Hale, S. A.; Hutiri, W.; Imperial, J. M.;
Jandial, S.; Judd, N.; Juefei-Xu, F.; Khomh, F.; Kailkhura,
B.; Kirk, H. R.; Klyman, K.; Knotz, C.; Kuchnik, M.; Kumar,
S. H.; Kumar, S.; Lengerich, C.; Li, B.; Liao, Z.; Long, E. P.;
Lu, V.; Luger, S.; Mai, Y.; Mammen, P. M.; Manyeki, K.;
McGregor, S.; Mehta, V.; Mohammed, S.; Moss, E.; Nach-
man, L.; Naganna, D. J.; Nikanjam, A.; Nushi, B.; Oala, L.;
Orr, I.; Parrish, A.; Patlak, C.; Pietri, W.; Poursabzi-Sangdeh,
F.; Presani, E.; Puletti, F.; R¨ottger, P.; Sahay, S.; Santos, T.;
Scherrer, N.; Sebag, A. S.; Schramowski, P.; Shahbazi, A.;
Sharma, V.; Shen, X.; Sistla, V.; Tang, L.; Testuggine, D.;
Thangarasa, V.; Watkins, E. A.; Weiss, R.; Welty, C.; Wilbers,
T.; Williams, A.; Wu, C.-J.; Yadav, P.; Yang, X.; Zeng, Y.;
Zhang, W.; Zhdanov, F.; Zhu, J.; Liang, P.; Mattson, P.; and
Vanschoren, J. 2024a. Introducing v0.5 of the AI Safety
Benchmark from MLCommons. arXiv:2404.12241.
Vidgen, B.; Scherrer, N.; Kirk, H. R.; Qian, R.; Kannappan,
A.; Hale, S. A.; and R¨ottger, P. 2024b. SimpleSafetyTests:
a Test Suite for Identifying Critical Safety Risks in Large
Language Models. arXiv:2311.08370.
Wang, B.; Chen, W.; Pei, H.; Xie, C.; Kang, M.; Zhang,
C.; Xu, C.; Xiong, Z.; Dutta, R.; Schaeffer, R.; et al. 2024a.
DecodingTrust: A Comprehensive Assessment of Trustwor-
thiness in GPT Models. Advances in Neural Information
Processing Systems, 36.
Wang, W.; Tu, Z.; Chen, C.; Yuan, Y.; Huang, J.-t.; Jiao, W.;
and Lyu, M. 2024b. All Languages Matter: On the Multilin-
gual Safety of LLMs. In Ku, L.-W.; Martins, A.; and Sriku-
mar, V., eds., Findings of the Association for Computational
Linguistics: ACL 2024, 5865–5877. Bangkok, Thailand: As-
sociation for Computational Linguistics.
Wang, Y.; Li, H.; Han, X.; Nakov, P.; and Baldwin, T. 2024c.
Do-Not-Answer: Evaluating Safeguards in LLMs. In Gra-
ham, Y.; and Purver, M., eds., Findings of the Association
for Computational Linguistics: EACL 2024, 896–911. St.
Julian’s, Malta: Association for Computational Linguistics.
Wei, A.; Haghtalab, N.; and Steinhardt, J. 2023. Jailbro-
ken: How Does LLM Safety Training Fail? arXiv preprint
arXiv:2307.02483.
Wolfe, R.; Yang, Y.; Howe, B.; and Caliskan, A. 2023. Con-
trastive Language-Vision AI Models Pretrained on Web-
Scraped Multimodal Data Exhibit Sexual Objectification
Bias.
In Proceedings of the 2023 ACM Conference on
Fairness, Accountability, and Transparency, FAccT ’23,
1174–1185. New York, NY, USA: Association for Computing
Machinery. ISBN 9798400701924.
Xie, T.; Qi, X.; Zeng, Y.; Huang, Y.; Sehwag, U. M.; Huang,
K.; He, L.; Wei, B.; Li, D.; Sheng, Y.; et al. 2024. Sorry-

--- Page 16 ---

bench: Systematically evaluating large language model safety
refusal behaviors. arXiv preprint arXiv:2406.14598.
Xu, G.; Liu, J.; Yan, M.; Xu, H.; Si, J.; Zhou, Z.; Yi, P.; Gao,
X.; Sang, J.; Zhang, R.; et al. 2023. Cvalues: Measuring
the values of chinese large language models from safety to
responsibility. arXiv preprint arXiv:2307.09705.
Xu, J.; Ju, D.; Li, M.; Boureau, Y.-L.; Weston, J.; and Di-
nan, E. 2021. Bot-Adversarial Dialogue for Safe Conversa-
tional Agents. In Toutanova, K.; Rumshisky, A.; Zettlemoyer,
L.; Hakkani-Tur, D.; Beltagy, I.; Bethard, S.; Cotterell, R.;
Chakraborty, T.; and Zhou, Y., eds., Proceedings of the 2021
Conference of the North American Chapter of the Associa-
tion for Computational Linguistics: Human Language Tech-
nologies, 2950–2968. Online: Association for Computational
Linguistics.
Yang, A.; Yang, B.; Hui, B.; Zheng, B.; Yu, B.; Zhou, C.;
Li, C.; Li, C.; Liu, D.; Huang, F.; Dong, G.; Wei, H.; Lin,
H.; Tang, J.; Wang, J.; Yang, J.; Tu, J.; Zhang, J.; Ma, J.;
Yang, J.; Xu, J.; Zhou, J.; Bai, J.; He, J.; Lin, J.; Dang, K.;
Lu, K.; Chen, K.; Yang, K.; Li, M.; Xue, M.; Ni, N.; Zhang,
P.; Wang, P.; Peng, R.; Men, R.; Gao, R.; Lin, R.; Wang, S.;
Bai, S.; Tan, S.; Zhu, T.; Li, T.; Liu, T.; Ge, W.; Deng, X.;
Zhou, X.; Ren, X.; Zhang, X.; Wei, X.; Ren, X.; Liu, X.;
Fan, Y.; Yao, Y.; Zhang, Y.; Wan, Y.; Chu, Y.; Liu, Y.; Cui,
Z.; Zhang, Z.; Guo, Z.; and Fan, Z. 2024. Qwen2 Technical
Report. arXiv:2407.10671.
Yu, E.; Li, J.; Liao, M.; Wang, S.; Zuchen, G.; Mi, F.; and
Hong, L. 2024a. CoSafe: Evaluating Large Language Model
Safety in Multi-Turn Dialogue Coreference. In Al-Onaizan,
Y.; Bansal, M.; and Chen, Y.-N., eds., Proceedings of the
2024 Conference on Empirical Methods in Natural Language
Processing, 17494–17508. Miami, Florida, USA: Association
for Computational Linguistics.
Yu, J.; Li, L.; and Lan, Z. 2024a. Beyond Binary Classifi-
cation: A Fine-grained Safety Dataset for Large Language
Models. IEEE Access.
Yu, J.; Li, L.; and Lan, Z. 2024b. Beyond Binary Classifi-
cation: A Fine-Grained Safety Dataset for Large Language
Models. IEEE Access, 12: 64717–64726.
Yu, J.; Lin, X.; Yu, Z.; and Xing, X. 2024b. Gptfuzzer: Red
teaming large language models with auto-generated jailbreak
prompts. arXiv preprint arXiv:2309.10253.
Yu, L.; Leng, Y.; Huang, Y.; Wu, S.; Liu, H.; Ji, X.; Zhao,
J.; Song, J.; Cui, T.; Cheng, X.; Liutao, L.; and Xiong, D.
2024c. CMoralEval: A Moral Evaluation Benchmark for
Chinese Large Language Models. In Ku, L.-W.; Martins, A.;
and Srikumar, V., eds., Findings of the Association for Com-
putational Linguistics: ACL 2024, 11817–11837. Bangkok,
Thailand: Association for Computational Linguistics.
Yuan, X.; Li, J.; Wang, D.; Chen, Y.; Mao, X.; Huang, L.;
Xue, H.; Wang, W.; Ren, K.; and Wang, J. 2024. S-Eval:
Automatic and Adaptive Test Generation for Benchmarking
Safety Evaluation of Large Language Models. arXiv preprint
arXiv:2405.14191.
Zhang, M.; Pan, X.; and Yang, M. 2023. Jade: A linguistics-
based safety evaluation platform for llm. arXiv preprint
arXiv:2311.00286.
Zhang, W.; Lei, X.; Liu, Z.; An, M.; Yang, B.; Zhao, K.;
Wang, K.; and Lian, S. 2024a. CHiSafetyBench: A Chinese
Hierarchical Safety Benchmark for Large Language Models.
arXiv preprint arXiv:2406.10311.
Zhang, Y.; Mai, Y.; Roberts, J. S.; Bommasani, R.; Dubois,
Y.; and Liang, P. 2024b. HELM Instruct: A Multidimensional
Instruction Following Evaluation Framework with Absolute
Ratings.
Zhang, Z.; Lei, L.; Wu, L.; Sun, R.; Huang, Y.; Long, C.; Liu,
X.; Lei, X.; Tang, J.; and Huang, M. 2024c. SafetyBench:
Evaluating the Safety of Large Language Models. In Ku,
L.-W.; Martins, A.; and Srikumar, V., eds., Proceedings of
the 62nd Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), 15537–15553.
Bangkok, Thailand: Association for Computational Linguis-
tics.
Zhao, D.; Wang, A.; and Russakovsky, O. 2021. Under-
standing and evaluating racial biases in image captioning. In
Proceedings of the IEEE/CVF International Conference on
Computer Vision, 14830–14840.
Zhao, J.; Fang, M.; Shi, Z.; Li, Y.; Chen, L.; and Pechenizkiy,
M. 2023. CHBias: Bias Evaluation and Mitigation of Chi-
nese Conversational Language Models. In Rogers, A.; Boyd-
Graber, J.; and Okazaki, N., eds., Proceedings of the 61st
Annual Meeting of the Association for Computational Lin-
guistics (Volume 1: Long Papers), 13538–13556. Toronto,
Canada: Association for Computational Linguistics.
Zhao, J.; Wang, T.; Yatskar, M.; Ordonez, V.; and Chang,
K.-W. 2018. Gender Bias in Coreference Resolution: Eval-
uation and Debiasing Methods. In Walker, M.; Ji, H.; and
Stent, A., eds., Proceedings of the 2018 Conference of the
North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies, Volume 2
(Short Papers), 15–20. New Orleans, Louisiana: Association
for Computational Linguistics.
Zhao, W.; Mondal, D.; Tandon, N.; Dillion, D.; Gray, K.; and
Gu, Y. 2024a. WorldValuesBench: A Large-Scale Bench-
mark Dataset for Multi-Cultural Value Awareness of Lan-
guage Models. In Calzolari, N.; Kan, M.-Y.; Hoste, V.; Lenci,
A.; Sakti, S.; and Xue, N., eds., Proceedings of the 2024
Joint International Conference on Computational Linguistics,
Language Resources and Evaluation (LREC-COLING 2024),
17696–17706. Torino, Italia: ELRA and ICCL.
Zhao, W.; Ren, X.; Hessel, J.; Cardie, C.; Choi, Y.; and Deng,
Y. 2024b. (InThe)WildChat: 570K ChatGPT Interaction Logs
In The Wild. In The Twelfth International Conference on
Learning Representations.
Zheng, L.; Chiang, W.-L.; Sheng, Y.; Li, T.; Zhuang, S.; Wu,
Z.; Zhuang, Y.; Li, Z.; Lin, Z.; Xing, E.; Gonzalez, J. E.;
Stoica, I.; and Zhang, H. 2024. LMSYS-1M: A Large-Scale
Real-World LLM Conversation Dataset. In The Twelfth In-
ternational Conference on Learning Representations.
Zhou, J.; Deng, J.; Mi, F.; Li, Y.; Wang, Y.; Huang, M.; Jiang,
X.; Liu, Q.; and Meng, H. 2022. Towards Identifying Social
Bias in Dialog Systems: Framework, Dataset, and Bench-
mark. In Goldberg, Y.; Kozareva, Z.; and Zhang, Y., eds.,
Findings of the Association for Computational Linguistics:

--- Page 17 ---

EMNLP 2022, 3576–3591. Abu Dhabi, United Arab Emi-
rates: Association for Computational Linguistics.
Ziems, C.; Yu, J.; Wang, Y.-C.; Halevy, A.; and Yang, D.
2022. The Moral Integrity Corpus: A Benchmark for Ethical
Dialogue Systems. In Muresan, S.; Nakov, P.; and Villav-
icencio, A., eds., Proceedings of the 60th Annual Meeting
of the Association for Computational Linguistics (Volume 1:
Long Papers), 3755–3773. Dublin, Ireland: Association for
Computational Linguistics.
Zou, A.; Wang, Z.; Carlini, N.; Nasr, M.; Kolter, J. Z.; and
Fredrikson, M. 2023. Universal and transferable adversar-
ial attacks on aligned language models.
arXiv preprint
arXiv:2307.15043.
A
Review Code Book
For each of the 144 datasets in our review, we recorded 23
pieces of structured information. At a high level, our goal
was to capture the full development pipeline of each dataset:
from how the dataset was created, to what entries in the
dataset look like, what the dataset can or should be used
for, how it can be accessed, and where it was published. We
show the full codebook in Table 3 below, which describes
the structure and content of our main review spreadsheet. We
make the spreadsheet available along with code to reproduce
our analyses at github.com/paul-rottger/safetyprompts-paper.
B
List of All Datasets
In total, our review covers 144 datasets published before
our cutoff date of December 17th, 2024. We did not cite all
dataset papers in the main body of our review, so we cite all
datasets here, in ascending order by year of publication.
1. JBBBehaviours (Chao et al. 2024)
2. MedSafetyBench (Han et al. 2024b)
3. PRISM (Kirk et al. 2024)
4. WildGuardMix (Han et al. 2024a)
5. SGBench (Mou, Zhang, and Ye 2024)
6. StrongREJECT (Souly et al. 2024)
7. CoCoNot (Brahman et al. 2024)
8. WildJailBreak (Jiang et al. 2024)
9. MultiTP (Jin et al. 2024b)
10. DoAnythingNow (Shen et al. 2024)
11. ForbiddenQuestions (Shen et al. 2024)
12. CoSafe (Yu et al. 2024a)
13. SoFa (Manerba et al. 2024)
14. ArabicAdvBench (Ghanim et al. 2024)
15. AyaRedTeaming (Aakanksha et al. 2024)
16. UltraSafety (Guo et al. 2024)
17. GEST (Pikuliak et al. 2024)
18. DeMET (Levy et al. 2024)
19. GenMO (Bajaj et al. 2024)
20. SGXSTest (Gupta et al. 2024a)
21. HindiXSTest (Gupta et al. 2024a)
22. CIVICS (Pistilli et al. 2024)
23. GlobalOpinionQA (Durmus et al. 2024)
24. CALM (Gupta et al. 2024b)
25. ChiSafetyBench (Zhang et al. 2024a)
26. SafetyBench (Zhang et al. 2024c)
27. CatQA (Bhardwaj, Do, and Poria 2024)
28. KorNAT (Lee et al. 2024)
29. CMoralEval (Yu et al. 2024c)
30. XSafety (Wang et al. 2024b)
31. SaladBench (Li et al. 2024a)
32. MMHB (Tan et al. 2024)
33. GPTFuzzer (Yu et al. 2024b)
34. WMDP (Li et al. 2024b)
35. ALERT (Tedeschi et al. 2024)
36. ORBench (Cui et al. 2024)
37. SorryBench (Xie et al. 2024)
38. XSTest (R¨ottger et al. 2024)
39. Flames (Huang et al. 2024a)
40. SEval (Yuan et al. 2024)
41. WorldValuesBench (Zhao et al. 2024a)
42. CBBQ (Huang and Xiong 2024)
43. KoBBQ (Jin et al. 2024a)
44. SAFE (Yu, Li, and Lan 2024b)
45. AegisAIContentSafety (Ghosh et al. 2024)
46. DoNotAnswer (Wang et al. 2024c)
47. RuLES (Mu et al. 2024)
48. HarmBench (Mazeika et al. 2024)
49. DecodingTrust (Wang et al. 2024a)
50. SimpleSafetyTests (Vidgen et al. 2024b)
51. CoNA (Bianchi et al. 2024)
52. ControversialInstructions (Bianchi et al. 2024)
53. QHarm (Bianchi et al. 2024)
54. MaliciousInstructions (Bianchi et al. 2024)
55. PhysicalSafetyInstructions (Bianchi et al. 2024)
56. SafetyInstructions (Bianchi et al. 2024)
57. HExPHI (Qi et al. 2024)
58. MaliciousInstruct (Huang et al. 2024b)
59. SycophancyEval (Sharma et al. 2024)
60. ConfAIde (Mireshghallah et al. 2024)
61. OKTest (Shi et al. 2024)
62. AdvBench (Zou et al. 2023)
63. Mosscap (LakeraAI 2023b)
64. TDCRedTeaming (Mazeika et al. 2023)
65. JADE (Zhang, Pan, and Yang 2023)
66. CPAD (Liu et al. 2023)
67. CyberattackAssistance (Bhatt et al. 2023)
68. AttaQ (Kour et al. 2023)
69. AART (Radharapu et al. 2023)
70. DELPHI (Sun et al. 2023a)

--- Page 18 ---

71. AdvPromptSet (Esiobu et al. 2023)
72. HolisticBiasR (Esiobu et al. 2023)
73. DiscrimEval (Tamkin et al. 2023b)
74. HackAPrompt (Schulhoff et al. 2023)
75. ToxicChat (Lin et al. 2023)
76. SPMisconceptions (Chen, Arunasalam, and Celik 2023)
77. FFT (Cui et al. 2023)
78. MoralChoice (Scherrer et al. 2023)
79. DICES350 (Aroyo et al. 2023)
80. DICES990 (Aroyo et al. 2023)
81. BeaverTails (Ji et al. 2023)
82. PromptExtractionRobustness (Toyer et al. 2023)
83. PromptHijackingRobustness (Toyer et al. 2023)
84. GandalfIgnoreInstructions (LakeraAI 2023a)
85. GandalfSummarization (LakeraAI 2023a)
86. HarmfulQA (Bhardwaj and Poria 2023)
87. LatentJailbreak (Qiu et al. 2023)
88. OpinionQA (Santurkar et al. 2023)
89. CValuesResponsibilityMC (Xu et al. 2023)
90. CValuesResponsibilityPrompts (Xu et al. 2023)
91. CHBias (Zhao et al. 2023)
92. HarmfulQ (Shaikh et al. 2023)
93. FairPrism (Fleisig et al. 2023)
94. ModelWrittenSycophancy (Perez et al. 2023)
95. ModelWrittenAdvancedAIRisk (Perez et al. 2023)
96. ModelWrittenPersona (Perez et al. 2023)
97. WinoGenerated (Perez et al. 2023)
98. SeeGULL (Jha et al. 2023)
99. WinoQueer (Felkner et al. 2023)
100. Machiavelli (Pan et al. 2023)
101. SafetyPrompts (Sun et al. 2023b)
102. OIGModeration (Ontocord.AI 2023)
103. CDialBias (Zhou et al. 2022)
104. HolisticBias (Smith et al. 2022)
105. PersonalInfoLeak (Huang, Shao, and Chang 2022)
106. ProsocialDialog (Kim et al. 2022)
107. SafeText (Levy et al. 2022)
108. AnthropicRedTeam (Ganguli et al. 2022)
109. IndianStereotypes (Bhatt et al. 2022)
110. MoralExceptQA (Jin et al. 2022)
111. BBQ (Parrish et al. 2022)
112. FrenchCrowSPairs (N´ev´eol et al. 2022)
113. MIC (Ziems et al. 2022)
114. SaFeRDialogues (Ung, Xu, and Boureau 2022)
115. SafetyKit (Dinan et al. 2022)
116. ToxiGen (Hartvigsen et al. 2022)
117. DiaSafety (Sun et al. 2022)
118. TruthfulQA (Lin, Hilton, and Evans 2022)
119. AnthropicHarmlessBase (Bai et al. 2022)
120. JiminyCricket (Hendrycks et al. 2022)
121. BiasOutOfTheBox (Kirk et al. 2021)
122. EthnicBias (Ahn and Oh 2021)
123. ConvAbuse (Cercas Curry, Abercrombie, and Rieser
2021)
124. MoralStories (Emelin et al. 2021)
125. RedditBias (Barikeri et al. 2021)
126. HypothesisStereotypes (Sotnikova et al. 2021)
127. StereoSet (Nadeem, Bethke, and Reddy 2021)
128. ETHICS (Hendrycks et al. 2021)
129. BAD (Xu et al. 2021)
130. HONEST (Nozza, Bianchi, and Hovy 2021)
131. SweWinoGender (Hansson et al. 2021)
132. LMBias (Liang et al. 2021)
133. ScruplesAnecdotes (Lourie, Le Bras, and Choi 2021)
134. ScruplesDilemmas (Lourie, Le Bras, and Choi 2021)
135. BOLD (Dhamala et al. 2021)
136. CrowSPairs (Nangia et al. 2020)
137. UnQover (Li et al. 2020)
138. RealToxicityPrompts (Gehman et al. 2020)
139. SocialChemistry101 (Forbes et al. 2020)
140. Regard (Sheng et al. 2019)
141. ParlAIDialogueSafety (Dinan et al. 2019)
142. EmpatheticDialogues (Rashkin et al. 2019)
143. WinoBias (Zhao et al. 2018)
144. WinoGender (Rudinger et al. 2018)

--- Page 19 ---

purpose: what can I use this dataset for?
type
High-level type of purpose /
general area of application
single choice: [broad safety, narrow safety, bias, value alignment,
other]
tags
Additional tags to specify purpose
comma-separated list of text tags
stated
Exact purpose as stated by authors
free text
llmdev
Intended use of the dataset within the LLM develop-
ment pipeline
single choice: [eval only, train and eval, train only, other]
entries: what do entries in this dataset look like?
type
High-level type of entry / format
single choice: [chat, multiple choice, autocomplete, other]
languages
Languages in the dataset
comma-separated list of free-text language names
n
Number of entries
integer
unit
Unit of entries (e.g. conversation)
free text
detail
Additional detail on entry format
free text
creation: who created this dataset / where is it sampled from?
creator typeType of creator, i.e. who or what created the data
single choice: [human, machine, hybrid]
source type Type of data source, i.e. where the data is taken from
single choice: [original, sampled, mixed]
detail
Additional detail on creator/source
free text
access: where can I download this dataset, and how is it licensed?
git url
GitHub repo URL
URL
hf url
Hugging Face dataset URL
URL
license
Dataset license
free text
publication: when, where, and by whom was this dataset published?
date
Publication date (most recent version)
dd-mmm-yyyy
affils
Author affiliations
comma-separated list of institutions
sector
Sector from which the publication originated
single choice: [academia, industry, mixed]
name
Publication name / reference
free text
venue
Publication venue
free text
url
Publication URL
URL
other: what is worth noting beyond the scope of this review?
notes
Additional notes
free text
date added
Date on which the dataset was added to Safe-
tyPrompts.com
dd-mmm-yyyy
Table 3: Codebook for our main review spreadsheet. For each of the 144 datasets included in our review, we recorded 23
pieces of structured information.

```
