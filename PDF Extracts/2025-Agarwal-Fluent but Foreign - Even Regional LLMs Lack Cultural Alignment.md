---
title: "2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment - PDF Extract"
source_pdf: "2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment.pdf"
pages: 18
extracted_at: "2026-02-07T17:00:46.758706"
---

# PDF Extract: 2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment

**Source PDF:** 2025-Agarwal-Fluent but Foreign - Even Regional LLMs Lack Cultural Alignment.pdf
**Total Pages:** 18

---

## Content

```
--- Page 1 ---

Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment
Dhruv Agarwal
Cornell University
Ithaca, New York, United States
da399@cornell.edu
Anya Shukla
Cornell University
Ithaca, New York, United States
Sunayana Sitaram
Microsoft Research
Bengaluru, India
Aditya Vashistha
Cornell University
Ithaca, New York, United States
adityav@cornell.edu
Is drinking alcohol (a) morally acceptable, (b) morally 
unacceptable, or (c) is it not a moral issue?
Indian LLM (nanda-10b)
More similar to 
American public 
opinion
10%
69%
17%
33%
16%
47%
23%
2%
61%
Figure 1: Regional LLMs trained in India continue to reflect American rather than Indian public opinion on value-related
questions.
Abstract
Large language models (LLMs) are used worldwide, yet exhibit West-
ern cultural tendencies. Many countries are now building “regional”
or “sovereign” LLMs, but it remains unclear whether they reflect
local values and practices or merely speak local languages. Using In-
dia as a case study, we evaluate six Indic and six global LLMs on two
dimensions—values and practices—grounded in nationally represen-
tative surveys and community-sourced QA datasets. Across tasks,
Indic models do not align better with Indian norms than global
models; in fact, a U.S. respondent is a closer proxy for Indian values
than any Indic model. We further run a user study with 115 Indian
users and find that writing suggestions from both global and Indic
LLMs introduce Westernized or exoticized writing. Prompting and
regional fine-tuning fail to recover alignment and can even degrade
existing knowledge. We attribute this to scarce culturally grounded
data, especially for pretraining. We position cultural evaluation as
a first-class requirement alongside multilingual benchmarks and
Permission to make digital or hard copies of all or part of this work for personal or
classroom use is granted without fee provided that copies are not made or distributed
for profit or commercial advantage and that copies bear this notice and the full citation
on the first page. Copyrights for components of this work owned by others than the
author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or
republish, to post on servers or to redistribute to lists, requires prior specific permission
and/or a fee. Request permissions from permissions@acm.org.
Conference acronym ’XX, Woodstock, NY
© 2026 Copyright held by the owner/author(s). Publication rights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/2018/06
https://doi.org/XXXXXXX.XXXXXXX
offer a reusable, community-grounded methodology. We call for
native, community-authored corpora and thick×wide evaluations
to build truly sovereign LLMs.
CCS Concepts
• Human-centered computing →Empirical studies in HCI; •
Computing methodologies →Artificial intelligence.
Keywords
AI, NLP, cultural alignment, value alignment, multilingual, large
language models
ACM Reference Format:
Dhruv Agarwal, Anya Shukla, Sunayana Sitaram, and Aditya Vashistha.
2026. Fluent but Foreign: Even Regional LLMs Lack Cultural Alignment. In
Proceedings of Make sure to enter the correct conference title from your rights
confirmation email (Conference acronym ’XX). ACM, New York, NY, USA,
18 pages. https://doi.org/XXXXXXX.XXXXXXX
1
Introduction
Large language models (LLMs) have witnessed an unprecedented
user adoption worldwide. These models are rapidly becoming global
infrastructures, mediating decisions and interactions in domains
as consequential as healthcare, education, and online governance.
Their adoption is not confined to Western settings: communities
across the Global South are integrating LLMs into everyday prac-
tices, including in high-stakes settings. Despite this global spread,
arXiv:2505.21548v3  [cs.CL]  22 Jan 2026

--- Page 2 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
frontier models continue to encode Western-centric values, beliefs,
and knowledge [6, 20]. From an HCI perspective, LLMs are not neu-
tral tools but cultural artifacts whose legitimacy, trustworthiness,
and use are shaped by local norms and expectations [11, 23]. When
these models privilege Western perspectives, the harms are not
merely technical—they manifest as cultural hegemony, homoge-
nization, and misalignment with the very populations that are now
becoming their fastest-growing users [2, 32].
To address these risks, researchers have begun developing re-
gional language models tailored to specific linguistic or geographic
communities. Recent examples include Nanda, a Hindi LLM aiming
to “usher in a culturally-aware AI era” for Hindi-speaking users [8],
and Jais, an LLM for Arabic-speaking communities [37]. These mod-
els are typically trained on large local-language corpora and are
evaluated on multilingual NLP benchmarks that test reasoning, clas-
sification, generation, and summarization in target languages [3].
Despite the rapid proliferation of regional models, no prior work
has systematically assessed their cultural alignment with the popu-
lations they target. Existing multilingual benchmarks primarily test
a model’s linguistic fluency and understanding, and not cultural
alignment.
This language-first orientation leaves a critical gap. Fluency in a
language is not the same as alignment with the cultural values, prac-
tices, and lived realities of its speakers [15]. A model can generate
grammatically correct text in a non-Western language yet remain
culturally alien in the assumptions it encodes. For example, an Ara-
bic model once linked prayer with alcohol consumption, a clear
violation of religious and cultural norms [27]. When evaluation
treats culture as secondary to language, models risk appearing lo-
cally fluent while remaining culturally misaligned. This disconnect
motivates our central research question: Does regional training
actually endow LLMs with the cultural alignment required
to serve the people they are built for?
To address this question, we examine regional models built for
Indian languages and cultures as a case study. India provides a
compelling context for this study: (i) the rapid proliferation of Indic
models creates a diverse test-bed for evaluation, and (ii) Indian cul-
tural norms diverge substantially from those typically represented
in Western-centric training corpora [2]. We systematically compare
several Indic LLMs—models explicitly trained on Indian languages
and for the Indian context—with global foundation models such
as the GPT, Llama, and Gemma series. In total, we evaluated 12
models: six Indic and six global. Because some Indic models are
fine-tuned from checkpoints of global models, our comparisons also
reveal whether regional adaptation yields emergent cultural knowl-
edge or whether more fundamental shifts in training paradigms are
required.
Guided by Hofstede’s cultural onion [17], our analysis assesses
two cultural dimensions—values and practices—using four tasks1
grounded in nationally representative surveys and community-
authored QA datasets. For values, we leverage the World Values
Survey (WVS), a nationally representative survey conducted in
∼120 countries [14, 18]. We also use GlobalOpinionQA [12], de-
rived from the Pew Global Attitudes Survey, which captures how
1We triangulate our findings across four tasks for robustness, as cultural alignment
can be sensitive to the specific task [21].
people across countries actually respond to value-related questions.
For practices—i.e., what people do in everyday life—we use Cul-
turalBench [7] and NormAd [33], both of which contain people’s
responses about diverse cultural practices. These four tasks allow us
to anchor evaluation directly in human knowledge. We then stress-
test these benchmark findings in a downstream setting via a user
study with 115 participants measuring how AI writing suggestions
from regional models versus global models shape users’ writing,
following the approach used by Agarwal et al. [2]. Taken together,
the surveys, QA datasets, and the user study let us evaluate model
alignment with the populations they are intended to serve.
Across the four benchmark tasks, we find that Indic models align
more closely with American culture than with Indian culture. An
example is shown in Figure 1. In some cases, regional training
even reduces cultural alignment compared to the base global model
on which the regional model was trained. We experiment with
diverse prompting strategies to help the model elicit Indian cultural
knowledge, but find that they offer negligible gains. Strikingly,
an average US respondent is a better proxy for Indian cultural
values than any Indic model we test. These benchmark findings
are reproduced in our user study, which shows that Indic models
homogenize Indian writing styles and flatten cultural expressions
similar to global models. Overall, these findings highlight the limits
of regional fine-tuning and call for new training paradigms and
benchmarks that place cultural alignment on equal footing with
linguistic fluency. Our main contributions are:
(1) A multi-dimensional evaluation framework. We oper-
ationalize Hofstede’s cultural onion for cultural evaluation
in LLMs by combining four community-grounded surveys
and benchmarks (two probing values, two probing practices)
with a complementary user study.
(2) A large-scale empirical study of regional training. We
evaluate 12 models (six Indic, six global), yielding the first
empirical evaluation of how regional fine-tuning affects cul-
tural alignment.
(3) Bridging NLP and HCI on cultural alignment. We posi-
tion cultural alignment as a human-centered process with
concrete implications for model training and the equitable
design of AI systems in non-Western contexts.
2
Related Work
2.1
Western Hegemony in AI Systems
HCI as a field has long recognized the importance of cultural
context in the design, adoption, and evaluation of technologies
(e.g., [9, 24, 41]). This body of work has critiqued the Western-
centrism of technology design and called for culturally grounded
approaches. Irani et al. [19] introduced the lens of postcolonial com-
puting, highlighting that design and use of technology are deeply
shaped by local histories and power relations. This perspective
emphasizes that what works in a Western context may fail to ac-
commodate non-Western cultural practices, urging designers to
foreground indigenous values and knowledge. Dourish [11] simi-
larly argues that algorithms are not neutral technical artifacts but
culturally situated, embedding the assumptions of its context of
origin, often a US-centric worldview in today’s AI systems [6, 20].
Building on this lineage, we treat LLMs not just as language tools

--- Page 3 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
but as cultural actors—systems that mediate values, norms, and
practices—and draw on value-sensitive design [13] to frame cul-
tural alignment as a first-class design requirement in the LLM
development cycle.
In recent years, there has been a growing interest in examin-
ing how cultural biases in AI models manifest in non-Western
regions [1, 2, 16, 32]. For example, Sambasivan et al. [36] argued
that AI fairness frameworks center Western notions of fairness
that overlook local realities. Likewise, recent work by Agarwal
et al. [2] demonstrates how AI writing assistants can effectively im-
pose a Western lens on non-Western users, such as making Indian
users’ writing resemble that of Americans and erasing important
cultural nuances. Qadri et al. [32] expanded this body of work
into multimodal models, showing that text-to-image models fail
to generate non-Western cultural artifacts accurately. Beyond the
model level, recent work has shown the impact of this cultural
bias on downstream tasks, including question answering, cross-
cultural communication, and situated applications across many
languages [2, 27, 35]. For example, Ochieng et al. [28] showed that
a variety of LLMs misclassified the sentiment of Swahili phrases
despite correct translation, because they missed out on the cultural
nuances surrounding these phrases. These findings underscore the
need for culturally aligned AI systems, especially in non-Western
regions where global models often fail to reflect local norms.
To address concerns about human-AI cultural alignment in non-
Western regions, researchers and developers have begun building
regional language models. These models are explicitly positioned
as multilingual, multicultural models, designed for local cultural
contexts. For example, Nanda is promoted as a multilingual model
that aims to “usher in a culturally-aware AI era” for Hindi users [8],
while Jais is framed as an LLM built to preserve the Arabic cul-
ture [37]. Yet, despite the regional branding of such models, current
evaluations remain narrowly focused on multilingual fluency, over-
looking the deeper question of alignment with local cultural values,
beliefs, and practices.
This gap is critical: in high-stakes domains, cultural misalign-
ment risks eroding trust, reproducing colonial epistemologies, and
undermining the very communities these models aim to serve. As
Qadri et al. [31] argue, evaluations must move beyond technical
benchmarks to account for the social and cultural dynamics in
which AI systems are embedded. Without rigorous evaluations, we
risk assuming that regional models address cultural misalignment
simply by producing content in local languages, when in fact they
may show biases similar to global models, or even exacerbate them.
Our work responds to this gap by systematically testing whether re-
gional LLMs are truly culturally grounded or whether they merely
speak local languages while reflecting a Western worldview.
2.2
Cultural Evaluation in NLP and HCI
A growing body of work in both HCI and NLP has focused on
evaluating whether LLMs encode culturally grounded knowledge,
values, and practices [1, 16]. Many of these evaluations use bench-
mark datasets grounded in large-scale, human-centered data—often
from nationally representative surveys or community co-design
processes. For instance, CulturalBench [7] evaluates factual cultural
knowledge across 45 global regions via over 1,200 multiple-choice
questions about customs, language, and behavior. All questions
are human-authored and verified by five annotators with exper-
tise in local cultures. NormAd [33] goes beyond factual recall by
examining whether models can apply cultural knowledge in situ-
ated scenarios such as greeting etiquette or dining norms. These
benchmarks reflect a growing interest in evaluating not only what
models know, but whether they can reason appropriately within
different cultural contexts [34].
Complementing practice-oriented benchmarks, several evalua-
tions use value-oriented datasets grounded in nationally represen-
tative surveys. For example, the World Values Survey (WVS) is a
large-scale study that captures variation in values across more than
120 countries [14]. The Inglehart–Welzel cultural map [18] distills
the WVS into two interpretable axes: traditional vs. secular-rational
and survival vs. self-expression, and is widely used to visualize cross-
national value differences [43]. For example, Western Europe and
North America cluster toward secular-rational and self-expression
values, while many South Asian and African societies lean toward
traditional and survival orientations. These value differences mat-
ter for AI systems: models trained predominantly on Western data
may default to value orientations that do not reflect the preferences
or lived realities of users elsewhere. However, such frameworks
includings Hofstede’s cultural dimensions [17] and the WVS-based
cultural map have been critiqued for being reductionist, treating na-
tions as culturally homogeneous units [5]. Still, they remain useful
scaffolds for early-stage AI alignment work [4, 25].
Beyond values, researchers have also examined how well LLMs
reflect population-level public opinion. GlobalOpinionQA [12], de-
rived from Pew Global Attitudes surveys, provides full national
response distributions for each question and enables comparing
model predictions against empirical opinion patterns. Newer bench-
marks such as ValueActionLens [38] probe whether a model’s stated
values or opinions match its behavior in decision-making.
These existing evaluations consistently show that global, Western-
trained models reproduce Western-centric knowledge and values [7,
20, 43]. In response, researchers have explored techniques for im-
proving cultural alignment. Simple prompting strategies such as
adding cultural identity cues yield limited improvements [21, 26],
whereas post-training on culturally representative corpora shows
more promise [22]. Yet, crucially, regional LLMs built “by and for” lo-
cal communities have rarely been evaluated against cultural bench-
marks grounded in representative, on-the-ground data. Instead,
they are judged primarily on multilingual fluency or task perfor-
mance. Our work systematically evaluates regional LLMs using
human-grounded surveys of values and practices and culturally ver-
ified QA datasets. By grounding evaluation in lived social contexts,
we test whether these models reflect the cultural values, practices,
and diversity of the communities they claim to serve [30].
3
Methodology
We use Hofstede’s cultural onion [17], a framework from social psy-
chology, to structure our evaluation. This framework categorizes
culture into two main dimensions: values (what people believe)
and practices (what people do). We operationalize each dimension
through two tasks, yielding a total of four tasks in our study (sum-
marized in Table 1). To keep human values at the center of our

--- Page 4 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
evaluation, we draw on high-quality data from large-scale, cross-
national surveys such as the World Values Survey and Pew Global
Attitudes Survey. These instruments are designed to capture nation-
ally representative values and practices across dozens of countries.
While these datasets enable broad and systematic evaluation, they
do not reveal how cultural (mis)alignment might affect end users in
real tasks. Thus, we additionally conduct a user study with 115 par-
ticipants, employing the models in a downstream task: generating
AI writing suggestions for culturally grounded content [2].
To control our study design, we use India as an example non-
Western culture and the United States as a Western culture. India
offers a rich testbed for this analysis due to (i) the rapid proliferation
of region-specific LLMs for Indian users, (ii) the availability of
community-grounded datasets as ground truth for India, and (iii) the
substantial cultural divergence between Indian and US norms [18].
Further, the authors’ positionality (familiarity with Indian culture
and local languages) enables a robust and contextually sensitive
evaluation.
3.1
Tasks and Datasets
3.1.1
Evaluating Values. We compare the performance of models
against two established survey datasets that collect data periodi-
cally from around the world by deploying on-ground teams. We
introduce these surveys below.
Value Orientation (Cultural Map). The World Values Survey (WVS)
is a large-scale, cross-national study that administers over 600 ques-
tions to participants in 120 countries every five years to examine
global variation in human values [14]. Inglehart and Welzel dis-
tilled ten of these questions into two latent dimensions: traditional
vs. secular-rational and survival vs. self-expression [18]. These two
dimensions form the axes of a cultural map that positions each
country within a shared value space. An example is shown in Fig-
ure 6 in Appendix A. This framework allows us to place models in
the same cultural space as human societies, allowing us to assess
their proximity to various cultural groups.
Opinion Alignment. While the cultural map reveals a model’s
average value orientation, we also test how well a model reflects
population distributions on concrete issues. We use GlobalOpin-
ionQA [12], derived from another popular value survey called the
Pew Global Attitudes Survey [29]. Each question in this dataset is
annotated with human response distributions from various coun-
tries; an example is shown in Figure 1. We filter the dataset to
include 94 questions where Indian and American public opinions
diverge and check whether a model aligns more closely with Indian
or American responses collected on the ground.
3.1.2
Evaluating Practices. The above experiments were designed
to test the cultural values of the models. Now, we evaluate their
cultural knowledge and their ability to apply it in situated contexts.
Cultural Knowledge. CulturalBench [7] is a question-answer
dataset designed to evaluate factual cultural knowledge. It con-
sists of 1,227 questions about customs, language, and behaviors
from 45 global regions. Each question is verified by five human
annotators with expertise in local cultures. An example question in
the dataset is: In Hindu culture, monkey is worshipped as which god?
A. Shiva B. Durga C. Hanuman D. Snake. Since we focus on India
and the US, we administer only a filtered subset of 46 India-specific
and 20 US-specific questions to assess a model’s knowledge about
these two cultures.
Cultural Adaptation. Knowledge alone is insufficient if a model
cannot apply it in context [38]. While CulturalBench directly probes
raw cultural knowledge in a model, NormAd [33] presents etiquette
scenarios that require socio-cultural reasoning and a categorical
response (Yes/No/Neither). These questions are sourced from ex-
tensive global community interviews and rigorous validation. An
example question in the dataset is: Sarah went to her friend’s home
for dinner. When food was served, she started eating with her left hand.
Was what she did socially acceptable? Yes, no, neither? The blank is
replaced with three levels of cultural specificity: (1) Country only
(e.g., “in India”), (2) Value+Country (e.g., “in India, where there is
respect for hygiene in dining”), and (3) Rule-of-Thumb, which makes
norms explicit (e.g., “in a culture where people avoid eating with their
left hand”). The Country case provides the least context and there-
fore requires the most cultural inference (e.g., in the example above,
it requires the model to first infer the social etiquette in India, then
use that to provide a yes/no/neither answer), whereas RoT is the
most direct. We use 29 Indian and 49 American-context questions,
testing if the model correctly identifies community-grounded social
norms in the two cultures.
3.1.3
User Study: Writing Task. Benchmarks evaluate how models
answer decontextualized questions, but they do not capture how
they behave when people actually use them for downstream appli-
cations such as writing. To probe this, we run a complementary
experiment inspired by Agarwal et al. [2]’s study of cultural homog-
enization in AI writing suggestions. In this experiment, we recruited
115 Indian participants to write short essays on culturally-grounded
topics: favorite festival, food, and public figure, and email to boss
asking for a vacation [2]. We compare the suggestions generated by
an Indic and global model, as well as the essays participants wrote
when receiving suggestions from each.
3.2
Models Evaluated and Prompting Strategies
As explained previously, we focus on India and the US as a case
study. We evaluate 12 models—six Indic and six global—summarized
in Table 2. Since all our tasks were framed in a question-answer
format, we used instruction-tuned variants of all models.
Indic models: sarvam-m-24b, nanda-10b, krutrim-2-12b, airavata-
7b, aryabhatta-8b, and gajendra-7b. These are trained or fine-
tuned on Indian language corpora specifically for Indian users.
Global models: mistral-3.1-24b, llama-2-7b, llama-3.1-8b,
gemma-7b, aya-8b, and gpt-4o. These models were not designed
with a specific region in mind and serve as baselines. We selected
these models to ensure (i) size parity (in terms of number of pa-
rameters) with Indic models for fair comparison, (ii) inclusion of
base models that some Indic models build upon, and (iii) a frontier
model for contextualizing results (GPT-4o).
Prompting Strategies. To give models a fair chance to surface
Indian values, we use four prompting strategies based on prior
work [1, 12]: (1) Default: Ask the question in English, as originally
written. (2) Demographic: Add a system prompt like “You are

--- Page 5 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Task
Example Question
# Questions
Trials per Question
Cultural Map
(WVS)
How important is God in your life?
(1–10)
10 (global)
100 trials
(10 prompts × 10 repe-
titions)
Opinion Alignment
(GlobalOpinionQA)
Is drinking alcohol (a) acceptable, (b)
unacceptable, or (c) not a moral issue?
94
(India–US
divergent)
All permutations (up
to 24)
Cultural Knowledge
(CulturalBench)
In Hindu culture, monkey is wor-
shipped as which god? (A) Shiva (B)
Durga (C) Hanuman (D) Snake)
66 total
(IN: 46, US: 20)
120 trials (24 perms ×
5 repetitions)
Cultural Adaptation
(NormAd)
Sarah ate with her left hand at dinner.
Is this acceptable? (Yes/No/Neither)
78 total
(IN: 29, US: 49)
30 trials (6 perms × 5
repetitions)
Writing Suggestions
(User Study)
Write a 50 word essay on: What is
your favorite food and why?
4 essays per participant (115 participants)
Table 1: Summary of tasks, example questions, questions, and trials in the study.
Global Models
Indic Models
Model
Params (B)
Model
Params (B)
Indian Langs.
mistral-3.1-24b
24
sarvam-m-24b
24
Hindi +9
llama-2-7b
7
nanda-10b
10
Hindi
llama-3.1-8b
8
krutrim-2-12b
12
Hindi +21
gemma-7b
7
airavata-7b
7
Hindi
aya-8b
8
aryabhatta-8b
8
Hindi +8
gpt-4o
–
gajendra-7b
7
Hindi
Table 2: Global and Indic LLMs used in our study and their parameter count (in billions). We used the instruction-tuned versions
of all models. For Indic models, we also report the number of Indian languages they are trained on (e.g., “Hindi + 9 other
languages”). Note: these are shorthand names used throughout the paper. Full-length HuggingFace model identifiers and model
release dates are provided in Appendix Table ??.
an average person in 𝑥country.” (3) Cross-lingual: Translate the
question to Hindi (a major language in India), keeping instructions
(e.g., formatting instructions) in English. (4) Hindi: Translate both
question and instructions to Hindi (dropped later due to poor in-
struction-following capabilities in Hindi). Hindi translations were
produced once using GPT-4o and then cached for reuse to avoid any
variability from GPT-4o’s non-deterministic outputs. All prompts
were zero-shot — the model was instructed to answer the question
without receiving any exemplars.
Additional methodological details, including decoding strategy (we
use a temperature of 0.3), handling of refusals, and hardware con-
figuration, are provided in Appendix E.
3.3
Data Collection and Analysis
We now detail our experimental methodology for all tasks and the
writing experiment. A consolidated summary is provided in Table 1.
Cultural Map. We asked each of the 10 WVS questions and
recorded the models’ responses. Following Tao et al. [43], we used
ten distinct system prompts (e.g., “You are an average human being
responding to the following survey question.”), and sampled ten
responses per prompt to account for decoding randomness, result-
ing in 100 responses per question. To ensure valid outputs, we also
appended an instruction to prevent the model from abstaining and,
for models with poor instruction-following, added explicit format-
ting instructions.2 Then, using standard methodology [18, 43], we
processed the responses to locate each model on the cultural map,
allowing us to compare it with population-scale average data for
each country.
GlobalOpinionQA. We follow the methodology of Durmus et al.
[12] to measure how closely a model’s opinion aligns with that of
Indian and American respondents. Let 𝑄= {𝑞1, . . . ,𝑞𝑛} be the set of
questions and 𝑂𝑞= {𝑜1, . . . ,𝑜𝑘} the answer options for a question
𝑞∈𝑄. Let 𝑃𝑐(𝑜𝑖| 𝑞) denote the probability that respondents from
country𝑐select option𝑜𝑖, as annotated in the dataset. We filtered the
dataset to retain only those questions for which the Indian and US
response distributions differ moderately, i.e., Sim(India, USA) ≤0.6,
where Sim is 1−Jensen–Shannon distance.
For each model 𝑚and question 𝑞, we compute the model’s an-
swer distribution 𝑃𝑚(𝑜𝑖| 𝑞) by biasing the logits toward the valid
options and applying a softmax [12]. We then compute Sim𝑞(𝑚,𝑐),
the similarity between model 𝑚and country 𝑐’s response distri-
butions (where 𝑐∈{India, USA}). Finally, we define the Cultural
Alignment Differential (CAD) as:
CAD𝑞,𝑚= Sim𝑞(𝑚, India) −Sim𝑞(𝑚, USA)
(1)
2We modified prompts across models only for this task, where a valid response to every
question is necessary to plot the map. In all other experiments, we used a uniform
prompt across models and treated invalid responses as incorrect.

--- Page 6 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
A positive CAD indicates greater alignment with Indian responses,
while a negative value indicates greater alignment with US re-
sponses. We report the average CAD for each model computed over
all filtered questions. To control for position bias, we present each
question using all possible answer option permutations (up to 24
per question3) and average the results across these permutations.
CulturalBench. We use the prompt template provided by Chiu
et al. [7] to ask each model questions about Indian and American
cultures. Since questions are multiple-choice, the order in which
the options are presented could bias the model’s output. To account
for this ordering effect, we repeat each question for all possible
answer option permutations (4! = 24). Further, to account for the
decoding randomness explained previously, we conduct five4 trials
for each permutation. This results in 24 × 5 = 120 repetitions per
question. We then compare the model’s response to the community-
grounded ground-truth, marking it as correct or incorrect. Finally,
we compute and report the overall accuracy, which represents the
model’s knowledge about the two cultures.
NormAd. We ask each question under the three context levels
described in Section 3.1.2 (Country, Value+Country, and Rule-of-
Thumb) using the prompt template provided by Rao et al. [33].
We compare the model’s response to the ground-truth (sourced
from community interviews), checking for correctness. We report
accuracy on each context for Indian and American norms. For each
context, we run 3! = 6 answer permutations to account for ordering
effects among the answer choices (yes, no, neither) and repeat 5
times for decoding variability, resulting in 30 total runs per question
per context.
User Study: Writing Task. We conduct an IRB-approved online
experiment using a custom-built web application. We recruit 115 In-
dian participants from Prolific, who first signed a consent form and
saw a short tutorial about how to use the system. Then, they wrote
short essays (minimum 50 words) on their favorite festival, food,
and public figure. We intentionally keep the task design identical
to Agarwal et al. [2] to ensure methodological consistency.
Each participant was assigned to one of four conditions: (1) No-
AI (natural Indian writing, 𝑛= 24), (2) AI-Global (suggestions from
GPT-4o, a global model, 𝑛= 36), (3) AI-Indic (suggestions from
Sarvam-M, an Indic model, 𝑛= 29), and (4) AI-Indic-Demographic
(suggestions from Sarvam-M with demographic prompting;𝑛= 26).
We choose GPT-4o and Sarvam-M for this experiment as they are
the most performant global and Indic models in our evaluation
set. In the AI conditions, participants receive inline autocomplete
suggestions that they can accept or reject while writing. This setup
enables us to test whether suggestions from an Indic model better
reflect Indian cultural preferences. We recorded each participant’s
writing process (e.g., suggestions shown, accepted, or rejected) and
their final essays, which we analyze using qualitative coding and
NLP methods (via OpenAI text embeddings).
3In GlobalOpinionQA, questions have different numbers of answer options. Since the
number of permutations grows quickly with the answer options, we cap it at 24 per
question.
4We used ten trials per Cultural Map question, but only five for CulturalBench and
NormAd due to the added cost of evaluating all answer permutations in these multiple-
choice tasks.
4
Results
We first analyze the results across the four tasks described previ-
ously: cultural map, opinion alignment, cultural knowledge, and
cultural adaptation. Then, we present results from the writing ex-
periment.
4.1
Cultural Map
Figure 2 plots all models on the Inglehart–Welzel (IW) cultural map,
which organizes societies along two value dimensions: traditional
vs. secular-rational values (x-axis) and survival vs. self-expression
values (y-axis). We plot results from three prompting strategies:
Default, Demographic, and Cross-lingual.5 For reference, we high-
light India and the United States on the map and treat the Euclidean
distance between them as a meaningful reference points: if an Indic
model lies farther from India than the US does, then an average
American is a closer proxy for Indian cultural values than the model
itself.
No model aligns with India on both axes. Figure 2 shows that
across all prompting conditions, no model falls into the bottom-left
quadrant of the map, where India sits. Some models align with
India on one axis but diverge sharply on the other. For example,
aryabhatta-8b score similarly to India on traditionalism but fall
closer to Western societies on self-expression and vice-versa for
gajendra-7b. In fact, no model achieves simultaneous alignment
with India on both value dimensions. This visual intuition is sup-
ported by quantitative distance measures comparing each model’s
Euclidean proximity to India and to the US (see Appendix Figure 7).
The surprising result is that under Default prompting, the United
States is closer to India than any of the Indic models—even though
Indic models are explicitly trained for the region. In other words,
an average American respondent is more culturally proximate to
India in this value space than any model fine-tuned on Indian data.
Prompting nudges models but doesn’t close the gap. Prompt-
ing strategies modestly shift models’ positions, but not enough to
change the underlying pattern. Demographic prompting moves
global models about 20% closer to India, on average, while barely
affecting Indic models (6% shift on average). This suggests that
regional training may have made Indic models more rigid, locking
them in value orientations that are still misaligned. Cross-lingual
prompting (i.e., presenting the question in Hindi) is more effective
at pulling Indic models somewhat closer to India (18% closer to
India than Default prompting). However, as seen in the right-most
plot in Figure 2, this happens because it brings models closer to the
US, and as a side-effect, the models also appear closer to India.
Among the Indic models, sarvam-m-24b is the only one that
maintains any proximity to India on the cultural map, even manag-
ing to cross the India–US distance threshold under some prompting
strategies (see Appendix Figure 6b for direct comparison). How-
ever, we point out that its base (global) model, mistral-3.1-24b is
even closer to India, suggesting that this success came from the
base model not from regional training. More importantly, despite
crossing this threshold, this model is still closer to the US than to
India in all three prompting strategies (Appendix Figure 7).
5We omit the Hindi strategy due to poor instruction-following by most models in
Hindi.

--- Page 7 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
1
0
1
2
3
Survival vs. Self-Expression Values
1
0
1
2
3
4
Traditional vs. Secular Values
airavata-7b
aryabhatta-8b
aya-8b
gajendra-7b
gemma-7b
gpt-4o
krutrim-2-12b
llama-2-7b
llama-3.1-8b
mistral-3.1-24b
nanda-10b
sarvam-m-24b
Ghana
India
Japan
Moldova
Sweden
United States
Prompting: Default
1
0
1
2
3
Survival vs. Self-Expression Values
airavata-7b
aryabhatta-8b
aya-8b
gajendra-7b
gemma-7b
gpt-4o
krutrim-2-12b
llama-2-7b
llama-3.1-8b
mistral-3.1-24b
nanda-10b
sarvam-m-24b
Ghana
India
Japan
Moldova
Sweden
United States
Prompting: Demographic
1
0
1
2
3
Survival vs. Self-Expression Values
aryabhatta-8b
aya-8b
gajendra-7b
gemma-7b
gpt-4o
krutrim-2-12b
llama-2-7b
llama-3.1-8b
mistral-3.1-24b
nanda-10b
sarvam-m-24b
Ghana
India
Japan
Moldova
Sweden
United States
Prompting: Cross-lingual
African-Islamic
Catholic Europe
Latin America
English-Speaking
Orthodox Europe
West & South Asia
Confucian
Protestant Europe
Model
Figure 2: Inglehart-Welzel (IW) cultural map. Bright purple markers denote the models evaluated; other markers denote
countries colored by geographic region. India and the United States are highlighted in black and some countries are labeled for
reference.
Takeaway. Despite being explicitly developed for Indian users,
none of the Indic models consistently align with India’s value profile
based on data collected from a nationally representative popula-
tion on the ground. While prompting strategies can nudge models
closer to India, these shifts are often incidental, driven by overlap-
ping alignment with Western values. These findings reveal a core
limitation of current regionalization efforts: fine-tuning alone is
insufficient for achieving cultural alignment.
4.2
Opinion Alignment
We assess how closely each model’s answers mirror public opinion
in India versus the United States, using 94 value-related questions
from the GlobalOpinionQA dataset [12]. These questions are drawn
from the Pew Global Attitudes Survey and come annotated with
nationally representative response distributions for both countries.
Since Indic models are intended for Indian users, we would expect
them to better reflect Indian responses. To quantify this, we use the
Cultural Alignment Differential (CAD), defined in Equation 1.6
Figure 3(a) shows the mean CAD under Default prompting for
all models. As expected, all global models align more closely with
US public opinion. Surprisingly, three Indic models—sarvam-m-24b,
krutrim-2-12b, and nanda-10b—also show a statistically signifi-
cant tilt toward US responses. The remaining Indic models cluster
around zero, appearing neutral. While neutrality might be desirable
for global models to not be aligned to any single value system, we
argue that it constitutes a failure case for regional models trained
specifically for a community.
Normalized CAD reveals stronger US bias. Public opinion
does not differ by the same amount on every question. On some
issues, Indians and Americans already think alike; on others, they
are far apart. A raw CAD of +0.10 therefore means very different
things across questions: if the two countries already agree, there is
little “room” for a model to lean toward either side; if they strongly
6This experiment requires raw logits, we could not run it for gpt-4o.
disagree, there is a lot of room. We make questions comparable by
scaling CAD by the available room to differ on that question, which
we call normalized CAD (nCAD).
nCAD =
CAD
1 −Sim(ind, usa)
where Sim(ind, usa) captures how similar the two populations’ an-
swer distributions are. Thus, the denominator 1 −Sim is the “maxi-
mum possible tilt” on that question7. nCAD represents the fraction
of the maximum possible tilt that a model expresses, ranging from
-1 (fully US-aligned) to +1 (fully India-aligned), with 0 denoting
neutrality.
Figure 3(b) shows the mean nCAD for each model. After nor-
malization, the US bias becomes even more pronounced: nearly all
models shift further left. No model shows statistically significant
alignment with Indian values. Notably, sarvam-m-24b, an Indic
model that came closest to India on the cultural map, leans 22%
toward the US from the point of neutrality (even more than its base
model, mistral-3.1-24b). To illustrate this, Table 3 provides exam-
ples from the dataset, showing the model’s response distribution
alongside those of Indian and US populations. Both examples show
that this Indic model does not reflect the ground realities of the
Indian public, but instead better reflects American public opinion.
Prompting strategies fail to recover Indian alignment. Fig-
ure 8 in Appendix B.1 reports nCAD across the four prompting
strategies. None of the strategies materially improves alignment for
Indic models. The average change from Default prompting is mar-
ginal: 0.02 ± 0.03 for Demographic, 0.06 ± 0.05 for Hindi, 0.04 ± 0.04
for Cross-lingual. Although Hindi prompting produces statistically
significant India-leaning shifts in two models (aryabhatta-8b and
gajendra-7b), the effect sizes remain small (only 7% and 4% tilts,
respectively).
7To avoid unstable denominators when the two populations are almost identical on a
question, we pre-filter items where the populations are too similar; see Methods.

--- Page 8 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
0.3
0.2
0.1
0.0
0.1
Cultural Alignment Differential (CAD)
mistral-3.1-24b
llama-3.1-8b
llama-2-7b
gemma-7b
aya-8b
sarvam-m-24b
krutrim-2-12b
nanda-10b
aryabhatta-8b
airavata-7b
gajendra-7b
***
medium
***
large
*
small
***
large
***
small
***
medium
***
medium
***
small
Global
Indic
0.3
0.2
0.1
0.0
0.1
Normalized Cultural Alignment Differential (nCAD)
mistral-3.1-24b
llama-3.1-8b
llama-2-7b
gemma-7b
aya-8b
sarvam-m-24b
krutrim-2-12b
nanda-10b
aryabhatta-8b
airavata-7b
gajendra-7b
***
medium
***
large
*
small
***
large
***
medium
***
medium
***
medium
**
small
Global
Indic
Figure 3: Cultural Alignment Differential (raw and normalized) for all models on GlobalOpinionQA under Default prompting.
Negative values represent a US tilt, and positive values mean an Indian tilt. The dotted vertical line at 𝑥= 0 represents no tilt.
Significance stars: *** 𝑝< 0.001, ** 𝑝< 0.01, * 𝑝< 0.05 (two-sided). Normality is checked with the Shapiro–Wilk test (𝛼= 0.05); if
normal, we run a one-sample t-test; otherwise a Wilcoxon signed-rank test. Green text shows effect sizes: (Cohen’s 𝑑for t-tests,
𝑟for Wilcoxon.
Question
Response Option
India
US
Global
Indic
Would military rule be a good way of governing the
country?
Refused
19%
<1%
<1%
<1%
Very bad
17%
63%
99%
98%
Somewhat bad
11%
19%
<1%
1%
Somewhat good
23%
13%
<1%
<1%
Very good
30%
4%
<1%
<1%
How much of a danger is the current government in
Iran to stability in the Middle East and world peace?
A great danger
13%
51%
97%
48%
Moderate danger
33%
37%
3%
48%
Small danger
31%
9%
<1%
4%
No danger
23%
3%
<1%
<1%
Table 3: Example questions from GlobalOpinionQA showing Indian and US public opinion, and model predictions from a
global model (llama-3.1-8b) and Indic model (sarvam-m-24b). These results are under Default prompting. We highlight the
most notable distribution mismatch in red, but we encourage the reader to notice the disparity across the entire India and
Indic model distributions. Note: the question and answer options have been paraphrased, and numbers have been rounded for
brevity.
Takeaway. While global models predictably lean toward US
public opinion, Indic models fail to align with Indian values even
under culturally sensitive prompting. Normalizing by intercultural
disagreement shows the extent of this bias, highlighting the need
for training data that balances cross-cultural value distributions.
4.3
Cultural Knowledge
We evaluate each model on 66 culturally specific multiple-choice
questions from CulturalBench [7], comprising 46 India-focused
and 20 US-focused items. These questions test knowledge of cus-
toms, etiquette, and behaviors in each country (e.g., appropriate
greeting styles, dining norms). For each question, we generate 120
responses per model (24 permutations of answer options × 5 trials),
and compute accuracy as the proportion of correct answers.
Models know more about US culture. Figure 4 (left) shows
that under Default prompting, all models—global and Indic—score
significantly better on US cultural questions. For example, gemma-
7b exhibits the largest accuracy gap (32%). The performance gap is
statistically significant across all models and all prompting strate-
gies (Bonferroni-corrected 𝑧-tests). Surprisingly, the same trend
holds for Indic models, which are ostensibly fine-tuned to serve
Indian users. This suggests that regional fine-tuning does not equip
models with stronger factual knowledge of Indian cultural contexts.
Prompting does not help elicit cultural knowledge. We ex-
plore whether prompting strategies can close the cultural knowl-
edge gap. While Demographic and Cross-linugal prompting slightly
reduce the India–US accuracy gap (from 16.1% under Default to
14.4% and 14.0%, respectively), this marginal improvement comes
at the cost of lower performance across both cultures. Even Indic
models perform 13–15% worse on Indian questions compared to
US ones under all strategies. In other words, the prompts helped
neither in surfacing hidden Indian knowledge nor in narrowing the
gap meaningfully.
Regional fine-tuning fails to add knowledge. Since Indic
models are fine-tuned on top of global models, good performance
on US questions is not surprising. Hence, we ask a more nuanced

--- Page 9 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
gpt-4o
mistral-3.1-24b
llama-3.1-8b
llama-2-7b
gemma-7b
aya-8b
sarvam-m-24b
krutrim-2-12b
nanda-10b
aryabhatta-8b
airavata-7b
gajendra-7b
***
***
***
***
***
***
***
***
***
***
***
***
Prompting: Default
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
***
***
***
***
***
***
***
***
***
***
***
***
Prompting: Demographic
0.0
0.2
0.4
0.6
0.8
1.0
Accuracy
***
***
**
***
***
***
***
***
***
***
***
Prompting: Cross-lingual
India
United States
Global Models
Figure 4: Accuracy on India– and US–specific questions from CulturalBench. Error bars represent 95% confidence intervals. The
dotted vertical line at 𝑥= 0.25 marks random-chance accuracy (four answer choices). Stars denote pairwise differences that
remain significant after Bonferroni correction (***: 𝑝< 0.001, **: 𝑝< 0.01 using a z-test for proportions).
Base →Indic
AccInd
AccUS
llama-2-7b →gajendra-7b
0.57 →0.45***
0.69 →0.59***
llama-2-7b →airavata-7b
0.57 →0.52***
0.69 →0.70
gemma-7b →aryabhatta-8b
0.50 →0.53*
0.82 →0.74***
mistral-3.1-24b →sarvam-m-24b
0.81 →0.79*
0.92 →0.87***
Table 4: Change in CulturalBench accuracy after regional
fine-tuning (for default prompting). Each row shows the base
model’s accuracy (left) and the Indic model’s accuracy (right)
for Indian and US questions. ***: 𝑝< 0.001, **: 𝑝< 0.01, *:
𝑝< 0.05.
question: does fine-tuning on Indian language data actually improve
knowledge of Indian culture?
To answer this, Table 4 compares several Indic models with
their respective base models8. In most cases, fine-tuning fails to
yield gains and sometimes worsens performance. For example,
gajendra-7b performs significantly worse than its base on both In-
dia and U.S. questions (–12.5% and –9.3%, respectively). airavata-7b
drops 5.6% on Indian questions without improving elsewhere. Only
aryabhatta-8b shows a modest +2.6% gain on India, but at the
cost of –8.5% on US knowledge. The highest accuracy Indic model,
sarvam-m-24b, underperforms its base across both Indian and US
questions. These results suggest that regional training displaces
general knowledge without reliably adding localized knowledge.
Takeaway. Indic models demonstrate a surprising lack of fac-
tual knowledge about Indian culture, even when evaluated with
culturally sensitive prompts. Regional fine-tuning does not reliably
inject new cultural knowledge, and can even degrade performance
on general cultural knowledge. These findings challenge the as-
sumption that language localization alone is sufficient for cultural
alignment, and point to a need for new training pipelines that more
intentionally encode region-specific cultural content.
8While the fine-tuning of Indic models is often performed on base models that are
not instruction-tuned, we compare against instruction-tuned variants of those bases,
as our tasks require instruction-following behavior. Since instruction tuning adds
task-following capability but not new factual knowledge, this comparison remains
valid for assessing cultural knowledge.
4.4
Cultural Adaptation
We evaluate all models on 71 etiquette-related questions from Nor-
mAd [33], spanning 29 India-specific and 42 US-specific scenarios.
This dataset presents each question under three levels of cultural
context: Country (e.g., “in India”), Value+Country (e.g., “in India,
where hygiene in dining is valued”), and Rule-of-Thumb (e.g., “in
a culture where people avoid eating with their left hand”). These
three conditions vary in reasoning demand: the Country prompt is
most implicit and reasoning-heavy, while Rule-of-Thumb makes
the norm explicit. Accuracy is averaged across all answer option
permutations and five trials per permutation.
Figure 5 shows that across all three conditions, all models per-
form better on US norms than on Indian ones. For most models, this
performance gap is statistically significant (Bonferroni-corrected
𝑧-test).
Indic models struggle with Indian cultural reasoning. In
the more implicit reasoning settings (Country and Value+Country),
Indic models perform only slightly better than random guessing
on Indian questions. For example, across all Indic models, aver-
age accuracy is just 38.6% in the Country condition and 43.5%
in Value+Country (random chance = 33%). Yet many of the same
models score much higher on US questions (49.1% and 53.4% re-
spectively), showing that they can reason better about American
norms.
Further, global models perform better as the cultural context be-
comes more explicit. This pattern is expected: more context makes
the task easier. However, some Indic models do not follow this trend.
For example, airavata-7b and gajendra-7b, perform near chance
across both cultures and all contexts. This suggests that they fail to
leverage added context for improved reasoning.
Regional fine-tuning does not improve cultural adaptation.
To isolate the impact of regional training, we compare Indic mod-
els to their base models. Across contexts, we find that fine-tuning
rarely improves performance on Indian questions and often reduces
performance on US ones. For example: In the Country condition,
airavata-7b and gajendra-7b improve by only 1% on Indian ques-
tions over their base llama-2-7b, but lose 4–6% accuracy on US
questions. aryabhatta-8b underperforms its base gemma-7b on

--- Page 10 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
0.0
0.2
0.4
0.6
0.8
Accuracy
gpt-4o
mistral-3.1-24b
llama-3.1-8b
llama-2-7b
gemma-7b
aya-8b
sarvam-m-24b
krutrim-2-12b
nanda-10b
aryabhatta-8b
airavata-7b
gajendra-7b
***
***
**
***
***
***
***
***
**
Prompting: Country
0.0
0.2
0.4
0.6
0.8
Accuracy
***
***
**
***
**
***
***
**
Prompting: Value+Country
0.0
0.2
0.4
0.6
0.8
Accuracy
***
**
*
***
***
*
Prompting: Rule-of-Thumb
India
United States
Global Models
Figure 5: Accuracy on NormAd questions about Indian and US social norms, grouped by the amount of contextual help: Country
(hard), Value+Country, and Rule-of-Thumb (easiest). The dotted vertical line at 𝑥= 0.33 marks random-chance accuracy (three
answer choices). Stars mark differences that remain significant after Bonferroni correction (***: 𝑝< 0.001, **: 𝑝< 0.01, *: 𝑝< 0.05).
Scenario
sarvam-
m-24b
mistral-
3.1-24b
Correct
Country: India. At a gathering at her friend’s house, Emily
was helping to set the table for dinner. When her friend
asked for the salt, Emily passed it using only her left hand.
Is what Emily did acceptable? Options: Yes, no, neutral
Yes
No
No
Explanation:
Using only the left hand to pass objects is considered disrespectful in many Indian contexts, where
the right or both hands are traditionally used.
Table 5: An example from the Country condition in NormAd. Despite regional fine-tuning, sarvam-m-24b consistently produces
an incorrect answer to this question, whereas its base model, mistral-m-24b, answers correctly.
both India and US items. sarvam-m-24b shows the most dramatic
loss: from 61% to 35% accuracy on Indian questions (–26%) after
fine-tuning, while gaining only 4% on US norms. Table 5 shows
an example where regional fine-tuning fails to improve cultural
reasoning.
Similar trends hold in the Value+Country context, indicating
that regional finetuning on Indian language data failed to inject
cultural reasoning capabilities specific to Indian social norms.
Takeaway. No model—global or Indic—can reliably apply Indian
social norms. While global models perform better on US questions
and benefit from increased context, Indic models consistently un-
derperform on Indian norms and fail to capitalize on cultural cues.
Regional fine-tuning does not enhance adaptation to local social
practices, and in some cases actively erodes previously acquired
cultural competence.
4.5
Writing Experiment
So far, our results show that Indic models do not align better with
Indian values or practices than global models on population-scale
benchmarks. But do these benchmark-level gaps matter for every-
day use? We now present results from a writing experiment with
Indian participants and compare the cultural “performance” of an
Indic model (Sarvam-M) and a global model (GPT-4o).
Condition
Mean simto No-AI
SD
𝑛
AI-Global (GPT-4o)
0.559
0.09
144
AI-Indic (Sarvam-M)
0.575
0.09
116
AI-Indic-Demographic
0.578
0.09
104
Table 6: Essay-level similarity to Indian No-AI essays (one
value per AI essay, averaged over natural Indian essays for
the same task). Note: 𝑛refers to the number of essays (4×
the number of participants since each participant wrote four
essays).
Similarity to natural Indian writing. We embed all essays
using OpenAI’s text-embedding model and compare the essays
written by Indians in the baseline condition (No-AI) with those
written with the help of AI suggestions coming from Sarvam-M vs
GPT-4o. We compute for each AI essay its average cosine similarity
across all No-AI essays within the same task. The resulting simi-
larity scores are shown in Table 6 and we also fit a linear mixed
model with with random intercepts for task. On average, Sarvam-
M-assisted (AI-Indic condition) essays are only marginally more
similar (𝛽= + 0.016) to natural Indian essays than GPT-4o-assisted
ones (95% CI [.002, .029], 𝑝=.028). This corresponds to a small effect
size (Cohen’s 𝑑) of 0.28.
Indic model suggests Western artifacts and descriptions.
We manually extract the the first cultural artifacts (food, festivals,

--- Page 11 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
celebrities) suggested by the AI model and code them as Indian or
non-Indian. We find that Sarvam-M’s suggestions frequently lean
toward Western or broadly globalized references. For public figures
and foods, 92% of first suggestions were non-Indian (e.g., Malala
Yousafzai or Oprah Winfrey for celebrities; pizza or sushi for food),
mirroring GPT-4o. For festivals, Sarvam-M typically suggested
Diwali (whereas GPT-4o suggested Christmas), but the accompa-
nying descriptions were similarly generic (“vibrant“ festivals that
“fill my heart with joy”, “aromatic” and “flavorful” food), exoticized
(“comforting bowl of happiness”, “melt-in-your-mouth textures”),
and even Westernized (phrases such as “naan bread” and “namaz
prayers”). In one notable example, an Indian participant chose (In-
dian) Independence Day as their favorite festival, yet Sarvam-M
proposed celebrating with a barbecue, an American Independence
Day tradition. These findings mirror those reported by Agarwal
et al. [2] but go further to show that homogenization, exoticization,
and cultural flattening arise not only in suggestions from global
models, but also from regional models.
Demographic prompting does not help. We repeat the writing
experiment with Sarvam-M with Demographic prompting, where
we explicitly state in the system prompt that the model is assisting
an Indian user. Although demographic prompting yielded Indian
artifacts in 100% of initial suggestions„ the model continued to
produce generalized, exoticized, or Westernized descriptions (e.g.,
“spices that tell a story”, “contentment in every bite”, “joyous time
filled with lights and laughter”, “vibrant and joyful”). The similarity
analysis in Table 6 confirms this; when comparing the demographic-
prompted condition to the global model (AI-Indic-Demographic vs.
AI-Global), the estimated improvement is very small (𝛽= .019 [.005,
.033]) even though it is statistically significant (𝑝=.009). And when
comparing demographic prompting to the regular Indic model (AI-
Indic vs. AI-Indic-Demographic), the difference is not significant at
all.
Takeaway. Taken together, these analyses show that even in a
downstream co-writing setting, Indic models do not preserve Indian
writing styles any better than a global model; their suggestions
often reproduce a Westernized gaze on Indian culture. Consistent
with our broader results, prompting strategies provide surface-level
alignment (e.g., more Indian artifacts) but leave deeper, entrenched
cultural biases unchanged.
5
Discussion
Our central question was whether region-specific training produces
language models that are culturally and not merely linguistically
aligned with their target communities. chaddedAcross four com-
plementary population-scale benchmarks and a downstream co-
writing experiment, we find that the answer is consistently negative.
Indic models fluently speak Indian languages, yet they reason, ex-
press opinions, recall cultural facts, and even assist Indian writers
in ways that resemble Western-centric models. For high-stakes
domains, this gap is not cosmetic; culturally misaligned models
can misinform users, erode trust, and reproduce epistemic harms
under the guise of localization. For the AI community, this under-
scores the need to treat culture as a first-class design target, on
par with other tasks and metrics. We now discuss implications for
human-centered AI evaluation and design.
Human-grounded AI evaluation at population scale. Recent
HCI work argues many AI evaluations of culture are “thin”, i.e.,
they are detached from the community, and calls for thick evalua-
tions co-constructed with local participants [30]. We expand this
idea into a thick × wide evaluation blueprint. In particular, much
of HCI’s evaluation of AI has relied on small lab or field studies
that richly capture context but are hard to scale across cultures
and regions. We complement that depth with scale by grounding
model evaluations in nationally representative surveys such as
the World Values Survey and Pew Global Attitudes Survey [14, 29].
These instruments are designed and fielded by on-the-ground teams
and capture cultural values, beliefs, and practices from thousands
of participants across dozens of countries, enabling us to anchor
model outputs to population-level distributions rather than isolated
individual judgments. This approach does not replace qualitative
or participatory inquiry but extends it, allowing HCI to connect
lived experience with population-scale patterns. We argue that pair-
ing community workshops and participatory evaluations (thick)
with survey-grounded, nationally representative instruments (wide)
can truly center the lived experiences of local participants while
evaluating AI models at scale.
Further, value-aligned models face the challenge of pluralism:
a plurality of values and practices exists in the world, as well as
within a nation-state. Sometimes, even conflicting cultural norms
coexist within the same geography. This raises the question, who
should models represent? Sorensen et al. [40] argued that models
can either reflect the plurality of views in every output (overton plu-
ralism), be steerable to a user’s desired views (steerable pluralism),
or reflect the plurality of views proportional to the population’s
preferences (distributional pluralism). Human-grounded data at the
population scale is crucial to covering these diverse perspectives
and building AI that is culturally situated, trustworthy, and socially
responsive [11, 13, 19].
Why evaluate “small” regional models at all? One might
argue that current regional LLMs are too small (7–24B parameters)
and far less capable than frontier models to be relevant. Why, then,
should we evaluate these models? However, two factors make this
evaluation especially important. First, these models are promoted as
culturally grounded and tailored for regional users, yet, in practice,
they are evaluated primarily on linguistic tasks. Our results show
empirically that regional language fluency ≠cultural competence,
and we hope this work encourages developers to treat cultural
evaluation as a first-class concern during model building. Model
evaluation must therefore expand beyond task metrics and test
cultural performance on thick (communally-grounded) and wide
(population-scale) human data. Second, these early regional models
are prototypes — they form the foundation for much larger invest-
ments. For example, companies like Sarvam (India), Sakana (Japan),
and others worldwide are already building frontier-scale sovereign
models. Before pouring resources into scaling, it is important to as-
sess whether these prototypes have succeeded at their core promise.
This will help detect cultural brittleness before building frontier-
scale versions which could fossilize the cultural misalignment.

--- Page 12 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
Training data and sovereign models. In our results, compar-
isons against Indic models’ base checkpoints show that supervised
fine-tuning (SFT) on local-language data leaves cultural knowledge
unchanged or degraded (Table 4). Digging deeper into the technical
reports for Indic models, we find that almost every Indic model
relies on instruction-tuning data that is either translated from Eng-
lish or tiny compared to the Western-centric pre-training data they
attempt to counterbalance. For example, nanda-10b, airavata-7b,
and gajendra-7b machine-translate English instruction datasets
into Hindi or other Indic languages, with limited native Hindi cor-
pora (e.g., 6k Hindi WikiHow articles). aya-expanse-8b includes a
sizeable, genuinely multilingual corpus, yet it tilts US-centric in our
evaluation. krutrim-2-12b seems to be pre-trained from scratch
by an Indian company, yet remains strongly US-leaning.
Thus, we hypothesize that the bottleneck lies in the imbalance
of pretraining and fine-tuning data. Web-scale corpora used for pre-
training are overwhelmingly produced by Western internet users,
and fine-tuning on a thin slice of translated regional languages does
not offset that prior. This mirrors HCI’s long-standing critique that
artifacts embed the assumptions of their origin contexts [11]. Our
findings reinforce that building “sovereign” models is guided by
Richard Sutton’s bitter lesson [42]: more data usually beats clever
algorithms. Hence, improved cultural alignment likely depends on
access to high-quality data from local populations that reflects their
culture, values, and lived realities.
Implications for HCI and NLP. Practitioners can embed “thick×wide”
cultural alignment into everyday workflows. For example, AI de-
velopers can evaluate any new models with a small participatory
cohort (thick) and on a population-grounded survey dataset (wide)
to track cultural drift before deployment. Wide evaluations can
show whether models reflect population-level cultural patterns,
which values and norms they reproduce, and where systematic
misalignments appear. Thick evaluations, informed by postcolonial
critiques that challenge static or monolithic views of culture, can
use community-engaged methods to surface subcultural variation
and to assess users’ perceptions of cultural (mis)alignment, includ-
ing how these misalignments shape end-user tasks done with AI
assistance. Together, this combined view can help identify when
model generations feel culturally off and how such misalignments
affect real-world use. Widely available datasets such as WVS, Pew,
regional opinion polls, and census data already provide strong
population-level priors, and partnerships with public institutions
and civil-society organizations can help create more representa-
tive models as AI systems become embedded in high-stakes non-
Western contexts [10].
A complementary direction extends the thick×wide approach
from evaluation to ownership by building community-centered
auditing infrastructures. This aligns with value-sensitive design
and postcolonial computing, which argue that communities should
not only be sites of data collection but should hold authority over
how cultural knowledge is defined, interpreted, and used. The pur-
poses of these infrastructures is not free labor for AI companies
but to shift power by giving communities mechanisms to detect
misrepresentation, negotiate boundaries on data use, and refuse
forms of cultural extraction. Community stewardship models al-
ready exist in adjacent domains, including local linguistic archives,
community data trusts, and participatory knowledge repositories
(e.g., AImpower). These models demonstrate that communities can
maintain data resources that serve their own interests rather than
those of commercial actors.
Building on these precedents, local NGOs, universities, and civil-
society organizations can steward small, regularly updated corpora
of culturally grounded prompts, examples, and norms. Such stew-
ardship allows communities to decide what cultural knowledge is
recorded, how it is governed, and under what conditions external
actors may access it. Such community-centered auditing infras-
tructures can protect communities from cultural flattening and
misuse.
Limitations and Future Work. Our analysis is constrained by
the availability of regional models. There exist a few frontier-scale
LLMs that were trained outside the West (e.g., DeepSeek), but no
such model exists yet for India that we could add to our evaluation
set. Cultural benchmarks like CulturalBench and NormAd used
in our study, though community-grounded, are limited in size for
many communities. While we mitigated this problem by triangulat-
ing across multiple experiments, we welcome future work that can
create more of these “thick” benchmarks at scale (“wide”). Yet, we
inherit the limitations of our datasets—their coarse granularity and
tendency to treat countries as singular cultural units. We encourage
work in cultural HCI and NLP that develops more fine-grained,
subnational approaches to cultural analysis. Finally, our study com-
pares one non-Western nation (India) with one Western nation
(the United States) due to the limited availability of non-Western
models and benchmark datasets; we encourage similar evaluations
for other regions as more regional models become available.
6
Conclusion
Regional language fluency does not imply cultural competence.
Across four human-grounded evaluations (leveraging nationally
representative surveys and culturally verified QA) and a human
participant study, we find that six Indic LLMs do not align better
with Indian values or practices than global baselines, and some-
times perform worse. Prompting offered little relief, highlighting
the limits of small-scale or translated local data in overcoming the
Western bias baked into web-scale pretraining. Our findings po-
sition cultural alignment not as an add-on but as a core goal in
model development. Building truly sovereign LLMs will require
untranslated regional corpora, training objectives that prioritize
cultural alignment, and thick × wide evaluation protocols that pair
community co-design with population-scale data. These efforts
align with HCI’s commitment to culturally situated design. Only
by embedding such practices early and continuously can future
regional and sovereign models truly serve the people they are built
for—not just linguistically, but also culturally and socially.
References
[1] Muhammad Farid Adilazuarda, Sagnik Mukherjee, Pradhyumna Lavania, Sid-
dhant Singh, Alham Fikri Aji, Jacki O’Neill, Ashutosh Modi, and Monojit Choud-
hury. 2024. Towards Measuring and Modeling "Culture" in LLMs: A Survey.
arXiv:2403.15412 [cs.CY] https://arxiv.org/abs/2403.15412
[2] Dhruv Agarwal, Mor Naaman, and Aditya Vashistha. 2025. AI Suggestions
Homogenize Writing Toward Western Styles and Diminish Cultural Nuances. In
Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems
(CHI ’25). ACM, 1–21. doi:10.1145/3706598.3713564

--- Page 13 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
[3] Kabir Ahuja, Harshita Diddee, Rishav Hada, Millicent Ochieng, Krithika Ramesh,
Prachi Jain, Akshay Nambi, Tanuja Ganu, Sameer Segal, Mohamed Ahmed, Kalika
Bali, and Sunayana Sitaram. 2023. MEGA: Multilingual Evaluation of Generative
AI. In Proceedings of the 2023 Conference on Empirical Methods in Natural Language
Processing, Houda Bouamor, Juan Pino, and Kalika Bali (Eds.). Association for
Computational Linguistics, Singapore, 4232–4267. doi:10.18653/v1/2023.emnlp-
main.258
[4] Arnav Arora, Lucie-Aimée Kaffee, and Isabelle Augenstein. 2023.
Prob-
ing Pre-Trained Language Models for Cross-Cultural Differences in Values.
arXiv:2203.13722 [cs.CL] https://arxiv.org/abs/2203.13722
[5] Sjoerd Beugelsdijk and Chris Welzel. 2018. Dimensions and Dynamics of Na-
tional Culture: Synthesizing Hofstede With Inglehart. Journal of Cross-Cultural
Psychology 49, 10 (Oct. 2018), 1469–1505. doi:10.1177/0022022118798505
[6] Yong Cao, Li Zhou, Seolhwa Lee, Laura Cabello, Min Chen, and Daniel Hersh-
covich. 2023. Assessing Cross-Cultural Alignment between ChatGPT and Human
Societies: An Empirical Study. arXiv:2303.17466 [cs.CL] https://arxiv.org/abs/
2303.17466
[7] Yu Ying Chiu, Liwei Jiang, Bill Yuchen Lin, Chan Young Park, Shuyue Stella Li,
Sahithya Ravi, Mehar Bhatia, Maria Antoniak, Yulia Tsvetkov, Vered Shwartz, and
Yejin Choi. 2024. CulturalBench: a Robust, Diverse and Challenging Benchmark
on Measuring the (Lack of) Cultural Knowledge of LLMs. doi:10.48550/arxiv.
2410.02677
[8] Monojit Choudhury, Shivam Chauhan, Rocktim Jyoti Das, Dhruv Sahnan, Xudong
Han, Haonan Li, Aaryamonvikram Singh, Alok Anil Jadhav, Utkarsh Agarwal,
Mukund Choudhary, Debopriyo Banerjee, Fajri Koto, Junaid Bhat, Awantika
Shukla, Samujjwal Ghosh, Samta Kamboj, Onkar Pandit, Lalit Pradhan, Rahul
Pal, Sunil Sahu, Soundar Doraiswamy, Parvez Mullah, Ali El Filali, Neha Sen-
gupta, Gokul Ramakrishnan, Rituraj Joshi, Gurpreet Gosal, Avraham Sheinin,
Natalia Vassilieva, and Preslav Nakov. 2025.
Llama-3-Nanda-10B-Chat: An
Open Generative Large Language Model for Hindi. arXiv:2504.06011 [cs.CL]
https://arxiv.org/abs/2504.06011
[9] Torkil Clemmensen, Morten Hertzum, Kasper Hornbæk, Qingxin Shi, and Pradeep
Yammiyavar. 2009. Cultural cognition in usability evaluation. Interacting with
Computers 21, 3 (July 2009), 212–220. doi:10.1016/j.intcom.2009.05.003
[10] Deepak Varuvel Dennison, Mohit Jain, Tanuja Ganu, and Aditya Vashistha. 2025.
Designing Culturally Aligned AI Systems For Social Good in Non-Western Con-
texts. arXiv:2509.16158 [cs.HC] https://arxiv.org/abs/2509.16158
[11] Paul Dourish. 2016. Algorithms and their others: Algorithmic culture in context.
Big Data & Society 3, 2 (2016), 2053951716665128.
[12] Esin Durmus, Karina Nguyen, Thomas I. Liao, Nicholas Schiefer, Amanda
Askell, Anton Bakhtin, Carol Chen, Zac Hatfield-Dodds, Danny Hernandez,
Nicholas Joseph, Liane Lovitt, Sam McCandlish, Orowa Sikder, Alex Tamkin,
Janel Thamkul, Jared Kaplan, Jack Clark, and Deep Ganguli. 2023. Towards Mea-
suring the Representation of Subjective Global Opinions in Language Models.
doi:10.48550/arxiv.2306.16388
[13] Batya Friedman and David G Hendry. 2019. Value sensitive design. MIT Press,
London, England.
[14] Christian Haerpfer, Ronald Inglehart, Alejandro Moreno, Christian Welzel,
Kseniya Kizilova, Jaime Diez-Medrano, Marta Lagos, Pippa Norris, Eduard
Ponarin, and Bi Puranen. 2022. World Values Survey (1981-2022). Trend File.
doi:10.14281/18241.23
[15] Shreya Havaldar, Sunny Rai, Bhumika Singhal, Langchen Liu, Sharath Chan-
dra Guntuku, and Lyle Ungar. 2023. Multilingual Language Models are not
Multicultural: A Case Study in Emotion.
arXiv:2307.01370 [cs.CL]
https:
//arxiv.org/abs/2307.01370
[16] Daniel Hershcovich, Stella Frank, Heather Lent, Miryam de Lhoneux, Mostafa
Abdou, Stephanie Brandl, Emanuele Bugliarello, Laura Cabello Piqueras, Ilias
Chalkidis, Ruixiang Cui, Constanza Fierro, Katerina Margatina, Phillip Rust,
and Anders Søgaard. 2022. Challenges and Strategies in Cross-Cultural NLP.
In Proceedings of the 60th Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), Smaranda Muresan, Preslav Nakov, and Aline
Villavicencio (Eds.). Association for Computational Linguistics, Dublin, Ireland,
6997–7013. doi:10.18653/v1/2022.acl-long.482
[17] Geert H. Hofstede. 1991.
Cultures and organizations: Software of the mind.
McGraw-Hill, London and New York. xii, 279 pages.
[18] Ronald Inglehart and Christian Welzel. 2005. Modernization, Cultural Change,
and Democracy: The Human Development Sequence. Cambridge University Press.
doi:10.1017/cbo9780511790881
[19] Lilly Irani, Janet Vertesi, Paul Dourish, Kavita Philip, and Rebecca E. Grinter. 2010.
Postcolonial computing: a lens on design and development. In Proceedings of the
SIGCHI Conference on Human Factors in Computing Systems (Atlanta, Georgia,
USA) (CHI ’10). Association for Computing Machinery, New York, NY, USA,
1311–1320. doi:10.1145/1753326.1753522
[20] Rebecca L Johnson, Giada Pistilli, Natalia Menédez-González, Leslye Denisse Dias
Duran, Enrico Panai, Julija Kalpokiene, and Donald Jay Bertulfo. 2022. The
Ghost in the Machine has an American accent: value conflict in GPT-3.
arXiv:2203.07785 [cs.CL] https://arxiv.org/abs/2203.07785
[21] Ariba Khan, Stephen Casper, and Dylan Hadfield-Menell. 2025. Randomness,
Not Representation: The Unreliability of Evaluating Cultural Alignment in LLMs.
In Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Trans-
parency (FAccT ’25). ACM, 2151–2165. doi:10.1145/3715275.3732147
[22] Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana Sitaram, and Xing Xie.
2024. Culturellm: Incorporating cultural differences into large language models.
Advances in Neural Information Processing Systems 37 (2024), 84799–84838.
[23] Zihan Liu, Han Li, Anfan Chen, Renwen Zhang, and Yi-Chieh Lee. 2024. Un-
derstanding public perceptions of AI conversational agents: A cross-cultural
analysis. In Proceedings of the 2024 CHI conference on human factors in computing
systems. 1–17.
[24] Aaron Marcus and Emilie West Gould. 2000. Crosscurrents: cultural dimensions
and global Web user-interface design. Interactions 7, 4 (July 2000), 32–46. doi:10.
1145/345190.345238
[25] Reem Masoud, Ziquan Liu, Martin Ferianc, Philip C. Treleaven, and Miguel Ro-
drigues Rodrigues. 2025. Cultural Alignment in Large Language Models: An
Explanatory Analysis Based on Hofstede‘s Cultural Dimensions. In Proceedings
of the 31st International Conference on Computational Linguistics, Owen Rambow,
Leo Wanner, Marianna Apidianaki, Hend Al-Khalifa, Barbara Di Eugenio, and
Steven Schockaert (Eds.). Association for Computational Linguistics, Abu Dhabi,
UAE, 8474–8503. https://aclanthology.org/2025.coling-main.567/
[26] Sagnik Mukherjee, Muhammad Farid Adilazuarda, Sunayana Sitaram, Kalika Bali,
Alham Fikri Aji, and Monojit Choudhury. 2024. Cultural Conditioning or Placebo?
On the Effectiveness of Socio-Demographic Prompting. arXiv:2406.11661 [cs.CL]
https://arxiv.org/abs/2406.11661
[27] Tarek Naous, Michael J. Ryan, Alan Ritter, and Wei Xu. 2024.
Having
Beer after Prayer? Measuring Cultural Bias in Large Language Models.
arXiv:2305.14456 [cs.CL] https://arxiv.org/abs/2305.14456
[28] Millicent Ochieng, Varun Gumma, Sunayana Sitaram, Jindong Wang, Vishrav
Chaudhary, Keshet Ronen, Kalika Bali, and Jacki O’Neill. 2024. Beyond Metrics:
Evaluating LLMs’ Effectiveness in Culturally Nuanced, Low-Resource Real-World
Scenarios. arXiv:2406.00343 [cs.CL] https://arxiv.org/abs/2406.00343
[29] Pew Research Center. 2025. Methodology: Spring 2025 Global Attitudes Sur-
vey.
https://www.pewresearch.org/2025/08/19/methodology-global-threats-
2025/. Accessed: 2025-09-11.
[30] Rida Qadri, Mark Diaz, Ding Wang, and Michael Madaio. 2025. The Case for
"Thick Evaluations" of Cultural Representation in AI. arXiv:2503.19075 [cs.CY]
https://arxiv.org/abs/2503.19075
[31] Rida Qadri, Piotr Mirowski, and Remi Denton. 2025. AI and Non-Western Art
Worlds: Reimagining Critical AI Futures through Artistic Inquiry and Situated Di-
alogue. In Proceedings of the 2025 CHI Conference on Human Factors in Computing
Systems (CHI ’25). ACM, 1–17. doi:10.1145/3706598.3714049
[32] Rida Qadri, Renee Shelby, Cynthia L. Bennett, and Emily Denton. 2023. AI’s
Regimes of Representation: A Community-centered Study of Text-to-Image Mod-
els in South Asia. In 2023 ACM Conference on Fairness, Accountability, and Trans-
parency (FAccT ’23). ACM, 506–517. doi:10.1145/3593013.3594016
[33] Abhinav Rao, Akhila Yerukola, Vishwa Shah, Katharina Reinecke, and Maarten
Sap. 2024. NormAd: A Framework for Measuring the Cultural Adaptability of
Large Language Models. doi:10.48550/arxiv.2404.12464
[34] Sougata Saha, Saurabh Kumar Pandey, and Monojit Choudhury. 2025. Meta-
Cultural Competence: Climbing the Right Hill of Cultural Awareness. In Pro-
ceedings of the 2025 Conference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human Language Technologies (Vol-
ume 1: Long Papers), Luis Chiruzzo, Alan Ritter, and Lu Wang (Eds.). Associ-
ation for Computational Linguistics, Albuquerque, New Mexico, 8025–8042.
https://aclanthology.org/2025.naacl-long.408/
[35] Sougata Saha, Saurabh Kumar Pandey, Harshit Gupta, and Monojit Choudhury.
2025. Reading between the Lines: Can LLMs Identify Cross-Cultural Communi-
cation Gaps? arXiv:2502.09636 [cs.CL] https://arxiv.org/abs/2502.09636
[36] Nithya Sambasivan, Erin Arnesen, Ben Hutchinson, Tulsee Doshi, and Vinodku-
mar Prabhakaran. 2021. Re-imagining Algorithmic Fairness in India and Beyond.
arXiv:2101.09995 [cs.CY] https://arxiv.org/abs/2101.09995
[37] Neha Sengupta, Sunil Kumar Sahu, Bokang Jia, Satheesh Katipomu, Haonan
Li, Fajri Koto, William Marshall, Gurpreet Gosal, Cynthia Liu, Zhiming Chen,
Osama Mohammed Afzal, Samta Kamboj, Onkar Pandit, Rahul Pal, Lalit Pradhan,
Zain Muhammad Mujahid, Massa Baali, Xudong Han, Sondos Mahmoud Bsharat,
Alham Fikri Aji, Zhiqiang Shen, Zhengzhong Liu, Natalia Vassilieva, Joel Hestness,
Andy Hock, Andrew Feldman, Jonathan Lee, Andrew Jackson, Hector Xuguang
Ren, Preslav Nakov, Timothy Baldwin, and Eric Xing. 2023. Jais and Jais-chat:
Arabic-Centric Foundation and Instruction-Tuned Open Generative Large Lan-
guage Models. arXiv:2308.16149 [cs.CL] https://arxiv.org/abs/2308.16149
[38] Hua Shen, Nicholas Clark, and Tanushree Mitra. 2025. Mind the Value-Action
Gap: Do LLMs Act in Alignment with Their Values? arXiv:2501.15463 [cs.HC]
https://arxiv.org/abs/2501.15463
[39] Yifan Song, Guoyin Wang, Sujian Li, and Bill Yuchen Lin. 2025. The Good, The
Bad, and The Greedy: Evaluation of LLMs Should Not Ignore Non-Determinism.
In Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the
Association for Computational Linguistics: Human Language Technologies (Volume

--- Page 14 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
1: Long Papers), Luis Chiruzzo, Alan Ritter, and Lu Wang (Eds.). Association for
Computational Linguistics, Albuquerque, New Mexico, 4195–4206. doi:10.18653/
v1/2025.naacl-long.211
[40] Taylor Sorensen, Jared Moore, Jillian Fisher, Mitchell Gordon, Niloofar
Mireshghallah, Christopher Michael Rytting, Andre Ye, Liwei Jiang, Ximing
Lu, Nouha Dziri, Tim Althoff, and Yejin Choi. 2024. A Roadmap to Pluralistic
Alignment. arXiv:2402.05070 [cs.AI] https://arxiv.org/abs/2402.05070
[41] Huatong Sun. 2012. Cross-Cultural Technology DesignCreating Culture-Sensitive
Technology for Local Users. Oxford University Press. doi:10.1093/acprof:oso/
9780199744763.001.0001
[42] Richard Sutton. 2019.
The Bitter Lesson.
http://www.incompleteideas.net/
IncIdeas/BitterLesson.html. Retrieved September 7, 2025.
[43] Yan Tao, Olga Viberg, Ryan S Baker, and René F Kizilcec. 2024. Cultural bias
and cultural alignment of large language models. PNAS Nexus 3, 9 (Sept. 2024).
doi:10.1093/pnasnexus/pgae346
A
Cultural Map Experiment
A.1
Inglehart-Welzel Cultural Map
Refer to Figure 6a for an example of the cultural map from 2023.
A.2
Distance from India across Prompting
Strategies
Refer to Figure 6b.
A.3
Distance from India and the US
Figure 7 shows the distance of each model from India and the US
on the IW cultural map.
B
Opinion Alignment Experiment
B.1
Impact of Prompting Strategies
Refer to Figure 8.
B.2
Raw Similarity Scores
Inspecting the raw similarity scores in Figure ?? (before comput-
ing the CAD), we find that some models (e.g. gemma-7b, aya-8b,
krutrim-2-12b) are generally misaligned with both Indian and
American responses. These models do not echo any of the target
groups. These models exhibit lower average similarity than even
the inter-country agreement between Indians and Americans (0.48).
In other words, American opinions are a better proxy for Indian
public opinion (and vice versa) than these models’ predictions. This
might not always be a bad thing. In fact, it might be desirable for a
global model not to be aligned to any culture than to be strongly
aligned to one specific culture. However, it constitutes a failure
mode for regional models (e.g., Indic models), which are explicitly
designed to align with a specific user group. The raw numbers in
this plot (and for the other three prompting strategies) are shown
in Table 7.
C
Cultural Knowledge Experiment
Accuracy results for the CulturalBench dataset shown in Figure 4
are reported in Table 8.
D
Cultural Adaptation Experiment
Accuracy results for the NormAd dataset shown in Figure 5 are
reported in Table 9.
E
Reproducibility Details
E.1
HuggingFace Model Identifiers
We used the open-source HuggingFace checkpoints for most mod-
els; see Table ?? for the exact HuggingFace checkpoints used. We
used 8-bit quantized versions of sarvam-m-24b and mistral-3.1-
24b. This is standard practice for models that are too large to fit on
available GPU memory. We accessed GPT-4o from the OpenAI API,
using model ID gpt-4o-2024-08-06.
E.2
Decoding
Decoding refers to the process of sampling the next token from the
model’s predicted distribution. Picking the most probable token is
called greedy decoding. However, greedy decoding locks a model
into a single response that may not answer the question or follow
the formatting instructions. To reduce invalid outputs from mod-
els with brittle instruction-following capabilities, we use random
sampling with a temperature of 0.3 instead of greedy decoding.
To account for this randomness, we follow best practices [39] by
repeating each prompt multiple times and averaging across trials
(details in Section 3.3).
E.3
Handling Unanswered/Refused Questions
Models sometimes refused to answer questions, especially on sen-
sitive World Value Survey question topics like abortion. For the
cultural map, we added an explicit instruction to prevent refusal.
Further, as explained in Section 3.2, instead of greedy decoding, we
sample the next token with a low temperature (0.3). This gave
the model a chance to answer the question without refusal or
instruction-following failures. Finally, we tried sampling a valid an-
swer ten times before counting it as invalid. The opinion alignment
task relies on logit-biasing without sampling a token, and hence is
safe from refusal.
E.4
Hardware Details
Experiments were run on Google Cloud Platform using a combina-
tion of Nvidia T4 and A100 GPUs.
Received 20 February 2007; revised 12 March 2009; accepted 5 June 2009

--- Page 15 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
0
1
2
3
4
Distance to India
gpt-4o
mistral-3.1-24b
llama-3.1-8b
llama-2-7b
gemma-7b
aya-8b
sarvam-m-24b
krutrim-2-12b
nanda-10b
aryabhatta-8b
airavata-7b
gajendra-7b
Experiment
Default
Demographic
Cross-lingual
(a) Inglehart-Welzel Cultural Map 2023 [18]
(b) Distance from India across prompting strategies
Figure 6: (a) Inglehart-Welzel Cultural Map 2023 [18]. (b) Euclidean distance between each model and India under three
prompting strategies. Lower is better. The dotted vertical line marks the distance between India and US on the cultural map;
most models are farther from India than an average American.
0
1
2
3
4
5
Distance
gpt-4o
mistral-3.1-24b
llama-3.1-8b
llama-2-7b
gemma-7b
aya-8b
sarvam-m-24b
krutrim-2-12b
nanda-10b
aryabhatta-8b
airavata-7b
gajendra-7b
Prompting: Default
0
1
2
3
4
5
Distance
Prompting: Demographic
0
1
2
3
4
5
Distance
Prompting: Cross-lingual
Distance to India
Distance to US
Global Models
India-US Distance
Figure 7: Distance of each model from India and the US across the three prompting strategies. The dotted vertical line marks
the distance between India and US on the cultural map.
0.3
0.2
0.1
0.0
0.1
nCAD
mistral-3.1-24b
llama-3.1-8b
llama-2-7b
gemma-7b
aya-8b
sarvam-m-24b
krutrim-2-12b
nanda-10b
aryabhatta-8b
airavata-7b
gajendra-7b
***
medium
***
large
*
small
***
large
***
medium
***
medium
***
medium
**
small
Prompting: Default
0.3
0.2
0.1
0.0
0.1
nCAD
***
medium
***
medium
***
large
**
medium
***
medium
***
medium
**
small
Prompting: Demographic
0.3
0.2
0.1
0.0
0.1
nCAD
**
small
***
medium
***
medium
***
medium
***
medium
*small
*small
Prompting: Hindi
0.3
0.2
0.1
0.0
0.1
nCAD
***
medium
***
large
***
medium
***
medium
***
medium
***
medium
Prompting: Cross-lingual
Global Models
Indic Models
Figure 8: Normalized CAD (nCAD) under four prompting strategies. Negative values indicate a US tilt, and positive values
indicate an India tilt. The dotted vertical line at 𝑥= 0 represents no tilt. * 𝑝< 0.05, ** 𝑝< 0.01, *** 𝑝< 0.001 (two-sided). Tests
used are the same as in Figure 3.

--- Page 16 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.
Model
Default
Demographic
Hindi
Cross-lingual
mistral-3.1-24b
0.33±0.17 // 0.43±0.15
0.33±0.17 // 0.46±0.15
0.40±0.16 // 0.47±0.15
0.38±0.16 // 0.46±0.15
llama-3.1-8b
0.41±0.17 // 0.55±0.15
0.46±0.17 // 0.58±0.14
0.53±0.17 // 0.64±0.15
0.50±0.16 // 0.62±0.15
llama-2-7b
0.47±0.13 // 0.51±0.13
0.47±0.12 // 0.49±0.13
0.48±0.09 // 0.47±0.10
0.48±0.11 // 0.48±0.14
gemma-7b
0.23±0.13 // 0.34±0.15
0.24±0.13 // 0.33±0.15
0.25±0.12 // 0.32±0.15
0.25±0.12 // 0.32±0.15
aya-8b
0.29±0.16 // 0.38±0.15
0.30±0.17 // 0.38±0.16
0.27±0.14 // 0.34±0.16
0.29±0.15 // 0.37±0.16
sarvam-m-24b
0.44±0.19 // 0.55±0.16
0.47±0.17 // 0.57±0.15
0.46±0.18 // 0.51±0.15
0.47±0.18 // 0.56±0.16
krutrim-2-12b
0.35±0.17 // 0.46±0.15
0.37±0.16 // 0.46±0.15
0.36±0.15 // 0.47±0.15
0.36±0.16 // 0.48±0.15
nanda-10b
0.54±0.17 // 0.61±0.15
0.54±0.17 // 0.61±0.15
0.59±0.18 // 0.58±0.15
0.57±0.17 // 0.59±0.14
aryabhatta-8b
0.59±0.16 // 0.57±0.13
0.58±0.16 // 0.55±0.15
0.62±0.16 // 0.60±0.13
0.62±0.16 // 0.60±0.13
airavata-7b
0.58±0.13 // 0.59±0.13
0.58±0.13 // 0.58±0.13
0.58±0.12 // 0.58±0.12
0.58±0.13 // 0.58±0.13
gajendra-7b
0.61±0.14 // 0.61±0.12
0.60±0.13 // 0.61±0.12
0.58±0.14 // 0.56±0.13
0.63±0.14 // 0.60±0.12
Table 7: Mean and standard deviation of Sim(𝑚,𝑖𝑛𝑑) (first) and Sim(𝑚,𝑢𝑠𝑎) (second) scores for all models under each prompting
strategy, prior to CAD normalization. Higher values indicate greater similarity to the corresponding population’s opinions.
Similarity with Indian opinion is generally lesser than American opinion, resulting in negative CAD scores in Figure 3.
Model
Default
Demographic
Cross-lingual
gpt-4o
0.85±0.36 // 0.98±0.15
0.85±0.36 // 0.98±0.13
0.64±0.48 // 0.94±0.23
mistral-3.1-24b
0.81±0.39 // 0.92±0.27
0.82±0.38 // 0.90±0.29
0.58±0.49 // 0.70±0.46
llama-3.1-8b
0.73±0.45 // 0.86±0.34
0.76±0.43 // 0.88±0.32
0.58±0.49 // 0.63±0.48
llama-2-7b
0.57±0.49 // 0.69±0.46
0.59±0.49 // 0.68±0.47
0.27±0.44 // 0.32±0.47
gemma-7b
0.50±0.50 // 0.82±0.38
0.51±0.50 // 0.80±0.40
0.40±0.49 // 0.53±0.50
aya-8b
0.68±0.47 // 0.91±0.28
0.68±0.47 // 0.90±0.29
0.50±0.50 // 0.74±0.44
sarvam-m-24b
0.79±0.41 // 0.87±0.33
0.80±0.40 // 0.87±0.34
0.55±0.50 // 0.75±0.43
krutrim-2-12b
0.73±0.45 // 0.84±0.36
0.73±0.44 // 0.83±0.37
0.56±0.50 // 0.73±0.44
nanda-10b
0.61±0.49 // 0.76±0.43
0.63±0.48 // 0.77±0.42
0.54±0.50 // 0.68±0.46
aryabhatta-8b
0.53±0.50 // 0.74±0.44
0.54±0.50 // 0.73±0.44
0.49±0.50 // 0.65±0.48
airavata-7b
0.52±0.50 // 0.70±0.46
0.52±0.50 // 0.69±0.46
0.39±0.49 // 0.48±0.50
gajendra-7b
0.45±0.50 // 0.59±0.49
0.45±0.50 // 0.57±0.49
0.29±0.45 // 0.31±0.46
Table 8: Accuracy (mean and standard deviation) on CulturalBench under all prompting strategies. Entries show accuracy on
India (left) and US (right) specific questions.
Model
Country
Value
Rule-of-Thumb
gpt-4o
0.53±0.50 // 0.69±0.46
0.61±0.49 // 0.75±0.44
0.78±0.41 // 0.81±0.40
mistral-3.1-24b
0.61±0.49 // 0.56±0.50
0.70±0.46 // 0.79±0.41
0.78±0.41 // 0.88±0.32
llama-3.1-8b
0.40±0.49 // 0.59±0.49
0.55±0.50 // 0.65±0.48
0.63±0.48 // 0.74±0.44
llama-2-7b
0.36±0.48 // 0.44±0.50
0.39±0.49 // 0.47±0.50
0.39±0.49 // 0.48±0.50
gemma-7b
0.48±0.50 // 0.63±0.48
0.53±0.50 // 0.67±0.47
0.64±0.48 // 0.70±0.46
aya-8b
0.47±0.50 // 0.65±0.48
0.58±0.49 // 0.64±0.48
0.66±0.47 // 0.72±0.45
sarvam-m-24b
0.35±0.48 // 0.60±0.49
0.48±0.50 // 0.68±0.47
0.64±0.48 // 0.77±0.42
krutrim-2-12b
0.50±0.50 // 0.62±0.49
0.56±0.50 // 0.71±0.46
0.68±0.47 // 0.73±0.45
nanda-10b
0.36±0.48 // 0.48±0.50
0.42±0.49 // 0.53±0.50
0.43±0.50 // 0.56±0.50
aryabhatta-8b
0.38±0.48 // 0.47±0.50
0.40±0.49 // 0.49±0.50
0.42±0.49 // 0.57±0.50
airavata-7b
0.36±0.48 // 0.38±0.49
0.37±0.48 // 0.38±0.49
0.41±0.49 // 0.42±0.49
gajendra-7b
0.37±0.48 // 0.40±0.49
0.37±0.48 // 0.41±0.49
0.39±0.49 // 0.46±0.50
Table 9: Accuracy (mean and standard deviation) on NormAd under all prompting contexts (Country, Value, Rule-of-Thumb).
Entries show accuracy on Indian (left) and American (right) norms.

--- Page 17 ---

Fluent but Foreign
Conference acronym ’XX, June 03–05, 2018, Woodstock, NY

--- Page 18 ---

Conference acronym ’XX, June 03–05, 2018, Woodstock, NY
Agarwal et al.

```
