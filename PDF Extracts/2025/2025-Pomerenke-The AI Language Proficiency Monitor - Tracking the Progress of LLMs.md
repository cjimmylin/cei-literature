---
title: "2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs - PDF Extract"
source_pdf: "2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs.pdf"
pages: 10
extracted_at: "2026-02-13T13:14:01.066269"
---

# PDF Extract: 2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs

**Source PDF:** 2025-Pomerenke-The AI Language Proficiency Monitor - Tracking the Progress of LLMs.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

The AI Language Proficiency Monitor – Tracking the Progress of LLMs on
Multilingual Benchmarks
David Pomerenke1
Jonas Nothnagel2
Simon Ostermann3
1Bundesministerium für wirtschaftliche Zusammenarbeit und Entwicklung (BMZ)
2Gesellschaft für Internationale Zusammenarbeit (GIZ)
3Deutsches Forschungszentrum für Künstliche Intelligenz (DFKI)
david.pomerenke@bmz.bund.de jonas.nothnagel@giz.de simon.ostermann@dfki.de
Abstract
To ensure equitable access to the benefits of
large language models (LLMs), it is essential
to evaluate their capabilities across the world’s
languages. We introduce the AI Language
Proficiency
Monitor,
a
comprehensive
multilingual benchmark that systematically
assesses LLM performance across up to
200 languages, with a particular focus on
low-resource languages.
Our benchmark
aggregates diverse tasks including translation,
question answering, math, and reasoning,
using datasets such as FLORES+, MMLU,
GSM8K, TruthfulQA, and ARC. We provide
an open-source, auto-updating leaderboard
and dashboard that supports researchers,
developers, and policymakers in identifying
strengths and gaps in model performance.
In addition to ranking models, the platform
offers descriptive insights such as a global
proficiency map and trends over time.
By
complementing and extending prior multi-
lingual benchmarks, our work aims to foster
transparency, inclusivity, and progress in multi-
lingual AI. The system is available at https:
//huggingface.co/spaces/fair-forward/
evals-for-every-language.
1
Introduction
To make the benefits of large language models
(LLMs) available to everyone, LLMs must speak
and understand everyone’s language. While a grow-
ing range of multilingual LLMs exist, mainstream
LLM development still predominantly focuses on
English. In contrast to this, a majority – close to
80% – of the world’s population does not speak
English (Eberhard et al., 2025). In response to
this disparity, a significant number of multilingual
resources for evaluation and training have been de-
veloped for many languages, both for pretraining
(Mayer and Cysouw, 2014; Conneau et al., 2020a;
Abadji et al., 2022; Weber et al., 2024) and finetun-
ing LLMs (Fu et al., 2022; Chiang et al., 2023; Asai
Figure 1: The map view of the language proficiency
monitor.
et al., 2024). With this work, we present the AI Lan-
guage Proficiency Monitor, an attempt to compile
a number of such multilingual evaluation datasets
into a comprehensive benchmark for evaluating the
performance of current AI models on every lan-
guage that has available benchmarking data. We
specifically focus on low-resource languages.
The benchmark is accompanied by an open-
source dashboard and is designed to support three
primary use cases:
• Researchers and model developers can bench-
mark their systems using the “AI Language
Proficiency Score,” a multi-task multilingual
performance metric;
• Practitioners can identify the most suitable
models for specific languages and tasks;
• Policymakers and donor agencies can identify
languages where capacity-building is most ur-
gent.
With this design, we aim to provide impact beyond
academia by supporting both private- and public-
sector decision-making, with a particular emphasis
on underserved communities.
1
arXiv:2507.08538v1  [cs.CL]  11 Jul 2025

--- Page 2 ---

For benchmarking we rely on FLORES+ (Goyal
et al. (2022), translation, classification) and mul-
tilingual versions of MMLU (Hendrycks et al.
(2020), multi-domain question answering), ARC
(Clark et al. (2018), advanced question answer-
ing), GSM8K (Cobbe et al. (2021b), math prob-
lems), and TruthfulQA (Lin et al. (2022), fac-
tuality).
Depending on the task, 100-200 lan-
guages are evaluated; these cover 80-95% of the
world’s speakers, and include many low-resource
languages. The monitor evaluates state-of-the-art
models from commercial AI providers, as well
as relevant open-weights models. The presented
pipeline auto-evaluates daily, always including the
latest relevant models.
In addition to an interactive scoreboard, we
present descriptive analyses: A global map of
country-level scores of AI language proficiency;
progress over time for high-resource vs.
low-
resource languages; and the impact of a language’s
number of speakers, GDP, and data availability on
AI language proficiency. Our goal is to also address
non-academic users, who often struggle to use and
interpret academic benchmarks (Ethayarajh and
Jurafsky, 2020).
In comparison to existing research and systems,
we make the following contributions: While com-
prehensive multilingual benchmarks such as FLO-
RES+ have already been used for evaluating mod-
els at singular points in time, our system contin-
ually applies them to the evolving landscape of
LLMs. This is similar to the OpenLLM leader-
board1 and the underlying EleutherAI LM Evalu-
ation Harness (Gao et al., 2024), but with a focus
on systematic multilingual evaluation. Regional
leaderboards for African and European languages
pursue the same focus (see section 2) and also
leverage machine translation to achieve comprehen-
siveness across the languages they cover; our sys-
tem takes inspiration from them, while scaling to a
global level, including more and up-to-date mod-
els, and providing a user-friendly interface with
language-specific leaderboards and visuals.
While our analysis already covers the most pop-
ular models and the largest languages, it is far from
comprehensive. We thus hope that our initiative
sparks the interest of regional AI developers to sub-
mit their own finetuned AI models, and to integrate
datasets for further tasks and languages.
1https://huggingface.co/spaces/
open-llm-leaderboard/open_llm_leaderboard
2
Background and Related Work
2.1
Multilingual Evaluation Benchmarks
A number of multilingual LLM benchmark ex-
ists. Notably, all of these benchmarks either come
with a very specific regional focus, or a low cov-
erage of low-resource languages. A first example
is the European LLM Leaderboard2 (Thellmann
et al., 2024b). It is based on the OpenGPT-X LM-
evaluation-harness3 and include NLU and machine
translation evaluations in 21 European languages
(Irish, Maltese, Croatian are missing); on publicly
available data sets such as MMLU (Hendrycks
et al., 2020), HellaSwag (Zellers et al., 2019), and
GSM8K(Cobbe et al., 2021a). Notably, only Euro-
pean languages are covered.
Another example is the Multilingual LLM Eval-
uation4 benchmark collection by Cohere.AI. The
benchmark includes a collection of datasets like
Global-MMLU or aya-redteaming. While being
an exhaustive collection of multilingual evaluation
datasets, the benchmark doesn’t provide a unified
evaluation interface or visualizations.
MEGA (Multilingual Evaluation of Generative
AI) (Ahuja et al., 2023) is a collection of standard
NLP benchmarks, covering 16 NLP datasets across
70 typologically diverse languages. MEGAVERSE
(Ahuja et al., 2024) extends this to 22 datasets cov-
ering 83 languages, as well as some multimodal
benchmarks. Both benchmarks are most similar
to ours in terms of coverage, but still lack behind
a more holistic evaluation of languages (with our
benchmark comprising more than twice the amount
of languages), and they come without an explicit
leader board or visualizations, restricting their use-
fulness for non-technical practitioners.
A prominent example for a more local and re-
gional benchmark is AfroBench (Ojo et al., 2025).5
the benchmark encompasses data from 64 African
languages for nine natural language understanding
datasets, six text generation datasets, six knowl-
edge and question answering tasks, and one math-
ematical reasoning task. Naturally, it focuses on
African languages only.
2https://huggingface.co/spaces/Eurolingua/
european-llm-leaderboard
3https://github.com/OpenGPTX/
lm-evaluation-harness
4https://huggingface.co/
collections/CohereLabs/
multilingual-llm-evaluation-674ebf8e49e5af2efe021c8d
5https://mcgill-nlp.github.io/AfroBench/
leaderboard.html
2

--- Page 3 ---

2.2
Multilingual and non-English Language
Models
Multilingual large language models (MLLMs) are
able to process and generate text across multiple
languages, enabling cross-lingual applications such
as translation, retrieval, and reasoning. Early ex-
amples of multilingual language models include
mBERT (Devlin et al., 2019) and XLM-R (Con-
neau et al., 2020a), encoder-based models that
are small by modern standards. There also ex-
ist some embedding-based works, especially for
low-resource languages (Gurgurov et al., 2025).
For LLMs, the most famous examples include the
LLama 3 model family (Grattafiori et al., 2024)
and Gemma 3 (Team et al., 2025), two types of
open-weights models.
Qin et al. (2025) introduce a comprehensive tax-
onomy of MLLMs based different techniques to
bridge language gaps. These include (1) shared
vocabulary/token alignment, where subword to-
kenizers like SentencePiece are used across lan-
guages, which sometimes results in tokenization
biases that disadvantage low-resource languages
(Rust et al., 2021); (2) architecture-level alignment,
where model parameters are shared across lan-
guages and sometimes augmented with language-
specific adapters to balance efficiency and special-
ization (Pfeiffer et al., 2020); (3) representation-
level alignment, where multilingual embeddings
are directly aligned using training objectives such
as contrastive or parallel-data losses (Artetxe and
Schwenk, 2018); and (4) post-hoc alignment, in
which independently trained monolingual models
are projected into a shared embedding space, show-
ing emergent alignment even without explicit mul-
tilingual training (Conneau et al., 2020b). Each
method involves trade-offs between scalability, fair-
ness, and computational cost.
3
System Design and Implementation
3.1
Dataset Collection and Translation
We collect multilingual benchmark datasets for
common NLP tasks comprising translation, text
classification, question answering, and maths. We
focus on datasets with parallel data for as many
languages as possible, so that meaningful compar-
isons of results across languages are possible. The
selected datasets are listed in Table 1. The table
also gives information about how the translation
was done (by humans vs. machine-translated).
The most comprehensive of the integrated
datasets is FLORES+ with 200 languages, along
with the derived SIB-200 dataset, where the same
sentences are classified into topic categories. For
question answering and mathematics, benchmark
datasets that were originally published in English
have been translated into additional languages, ei-
ther by humans or by translation software, as speci-
fied in Table 1. When multiple versions of the data
sets cover the same language, we prefer those that
are human-translated. When a dataset is present
in multiple scripts for the same language, we re-
trieve script user population data for the relevant
language from Unicode CLDR6 and only incorpo-
rate the version with the more common script (the
less common script is typically a transliteration
from the original script). The Masakhane datasets
(AfriMMLU, AfriMGSM, Uhura ARC Easy) only
cover a subset of the respective original English
datasets; therefore, we restrict all corresponding
datasets to exactly the same rows as the Masakhane
datasets to ensure that our combined dataset is par-
allel.
We retrieve the 100 most spoken languages in the
world from CLDR and complement all languages
that are not covered by the existing benchmark
datasets by using machine translation. While ma-
chine translation is inferior to human translation
for the purpose of benchmarking, it is a viable al-
ternative for languages without benchmark data,
and has been used before by GlobalMMLU (Singh
et al., 2025), Okapi (Lai et al., 2023), and EU-20
(Thellmann et al., 2024a). We select Google Neural
Machine Translation (Google Cloud Translate v2),
which performs better than any general-purpose
LLM in our FLORES+ translation evaluation, and
use it to translate benchmark questions and answers
into all missing languages.
3.2
Task Implementation and Evaluation
All model evaluations in the leaderboard are con-
ducted in a few-shot manner. Translated prompt in-
structions are not provided by the selected datasets,
and human translations at such large scale are out
of scope for our project. Machine-translating the
prompt into different languages would have been
an alternative, but potential translation errors would
have an overproporionate impact on performance.
Thus, we instead use minimal language-agnostic
prompts along with few-shot prompting, to demon-
strate rather than explain the tasks to the prompted
6https://cldr.unicode.org/
3

--- Page 4 ---

#Languages
Translation
Authors
Translation
FLORES+
200
g
Costa-jussà et al. (2024)
Classification
SIB-200
200
g
Adelani et al. (2024)
Q&A: Multitask Language Understanding
MMLU (Original)
1
–
Hendrycks et al.
MMMLU
14
g
OpenAI
GlobalMMLU
42
g2
Singh et al. (2025)
AfriMMLU
17
g
Adelani et al. (2025)
OkapiMMLU
26
2
Lai et al. (2023)
MMLU Auto-Translated
61
2
–
Q&A: ARC Challenge
ARC (Original)
1
–
Clark et al.
Uhura ARC Easy
6
g
(Bayes et al.)
Okapi ARC Challenge
31
2
Lai et al. (2023)
ARC-X
20
2
Thellmann et al. (2024a)
ARC Auto-Translated
94
2
–
Truthfulness
TruthfulQA
1
–
Lin et al. (2022)
Uhura TruthfulQA
6
g
(Bayes et al.)
Okapi TruthfulQA
31
2
Lai et al. (2023)
TruthfulQA-X
94
2
Thellmann et al. (2024a)
Grade School Math
GSM8K (Original)
1
–
Cobbe et al.
MGSM
10
–
Shi et al. (2022)
AfriMGSM
18
g
Adelani et al. (2025)
GSM8K-X
20
2
Thellmann et al. (2024a)
MGSM Auto-Translated
73
2
–
Table 1: Benchmark datasets by task. The table cover the number of covered languages and information on whether
the translations between languages were done by humans (g) or automatically (2).
models. For the mathematics task, we specify a
response format "<reasoning> #### <number>" in
the prompt to give all models a reasoning scratch-
pad. Examples of few-shot prompts are provided
on Github.7
All classification and question answering tasks
are given in a multiple choice format with one cor-
rect answer, and they are evaluated using accuracy.
The math tasks are evaluated using the accuracy
of the final number. For translation, evaluation is
less straightforward: The often-used BLEU met-
ric (Papineni et al., 2002) may be biased towards
giving worse scores to languages with coarser to-
kenization; BertScore (Zhang et al., 2019) and its
multilingual versions may be biased towards giv-
ing a higher score towards languages seen during
training. We therefore use the SpBLEU metric
(Goyal et al., 2022), which relies on a Sentence-
Piece classifier for tokenization, which has been
7https://github.com/datenlabor-bmz/
evals-for-every-language/blob/main/notes/
prompt-examples.md
equally trained on all languages contained in the
FLORES+ dataset. Moreover, we distinguish be-
tween the task of translating from a language of
interest to a set of other languages (which is sam-
pled representative of speaker populations) and the
task of translating from a representative set of lan-
guages to a language of interest. While the latter is
potentially sensitive to language-specific biases of
the evaluation metric, the former task (translating
from a given language) is more comparable, since
the output sentences on which the evaluation metric
operates are stable across evaluated languages.
3.3
Models and Inference
To make the leaderboard as useful as possible, it
should always include up-to-date models, focus on
those that are also most relevant to the community
of practitioners, and include open-weights as well
as API-only models. We use OpenRouter both for
retrieving information on historically and currently
popular models, and for performing inference. Our
pipeline updates daily via Github Actions to re-
4

--- Page 5 ---

Figure 2: Language proficiency scores by different mod-
els over time. The line shows the highest achieved score
by any model at a given date.
trieve the latest models and run evaluations on them
automatically. OpenRouter has a central function-
ality to only use endpoints where providers are
not allowed to train on user data, which is crucial
for avoiding data contamination when performing
benchmarking via APIs.
For non-commercial, open-source models - of-
ten of particular relevance to local communities
due to their task- or language-specific design and
lower operational costs - we rely on HuggingFace’s
inference API. This approach also provides a sim-
ple and inclusive mechanism for users to submit
and benchmark their own models, as anyone can
publish endpoints on HuggingFace. At present, we
ask users to submit a request via an online form
and share their model endpoint to be included in
the automated evaluation runs. Future versions
of the leaderboard will support a fully automated
submission and integration process.
3.4
The Language Proficiency Score
For our leaderboard we normalize the scores of all
tasks using min-max-normalization, so that scores
are more comparable across tasks.
We define an aggregate metric, the Language
Proficiency Score, as the mean of the individual
task metrics. This metric provides an overall rating
of an AI models understanding of a given language,
and is intended for reporting on multilingual abil-
ities of new AI models. On our leader board, we
report aggregate Language Proficiency Scores both
for each AI model (averaging over all languages)
and for each language (averaging over all models).
Figure 3: Language Proficiency Score by language.
3.5
Web Application
Our web application is hosted on Huggingface,
where it is linked to existing models and datasets.
The web app consists of four parts:
• Model leaderboard. This table ranks LLMs
by their language proficiency and provides the
Language Proficiency Score as well as scores
for each task. The table can be filtered by
open-weights vs API-only models, by cost per
output tokens, and for the open models also by
parameter size; this metadata is retrieved from
OpenRouter and Huggingface. By default, the
leaderboard shows scores that are aggregated
across all evaluated languages. The leader-
board picker allows users to switch instead to
leaderboards for a specific language of inter-
est.
• Language scoreboard. This table shows in-
formation on languages and how proficient
AI models are in them. Languages are sorted
by overall number of speakers, and may be
filtered by language family. The language
Proficiency Score and task-specific scores are
displayed. The user may select one or multi-
ple languages, and the model leaderboard will
focus on the selected languages.
• Dataset infoboard. This table presents data
on the benchmark datasets that the system
uses for evaluation, and they can be filtered
by task, number of languages, and human- vs
machine-translated datasets.
• Visuals board. This view provides interactive
plots, including a map, trends over time, and
a cost-effectiveness comparison (see Figure 1,
Figure 3, Figure 2).
5

--- Page 6 ---

A screenshot of the system is included in Ap-
pendix A. Code and evaluation pipeline are re-
leased under the MIT License.8 All code and docu-
mentation are available at https://github.com/
datenlabor-bmz/evals-for-every-language.
4
Evaluation
4.1
Model and Language Performance
Figure 3 shows the language proficiency scores by
language. The size of the dots and the position-
ing on the x axis indicates the number of speakers
of the respective language. The graph confirms
already known trends: English as the language
with most resources employs the highest language
proficiency scores. Large European Languages
like French, Spanish, Portuguese, or German show
high scores in spite of comparably fewer speak-
ers. Larger low to mid resource languages like
Swahili show comparably bad scores in spite of
many speakers. Figure 2 shows language profi-
ciency scores by different models over time, show-
casing that Google models currently perform best.
4.2
Qualitative Stakeholder Feedback
In order to get an idea about the usefulness of our
tool for the relevant stakeholder, we conducted
a small qualitative survey comparing our bench-
mark along other freely available benchmarks
(AfroBench, European LLM Leaderboard, Multi-
lingual MMLU Benchmark Leaderboard, Multilin-
gual Reasoning Leaderboard) with one stakeholder
each from Industry, SME, Public Sector, and NGO.
In comparison, the stakeholders liked the simplic-
ity of the AI monitor use and the focus on non-
European languages, while they criticized that still
only academic benchmarks were used, the perfor-
mance on which doesn’t necessarily correlate with
downstream application performance in a language.
While they liked the language coverage and ease of
use of the dashboard, they still lacked cross-lingual
trends and would have expected an even larger cov-
erage of tasks - which we will account for in future
versions of the dashboard.
5
Conclusion
5.1
Limitations
A key limitation of our work arises from the in-
herent challenges of using benchmarks to evaluate
8https://opensource.org/licenses/MIT. Copyright
© 2025 Datenlabor BMZ, GIZ, and DFKI.
large language models. As widely discussed in re-
cent literature, for example (Raji et al., 2021) (Asai
et al., 2024), benchmarks often offer only a very
specific snapshot of capabilities and may not re-
flect real-world utility, particularly across diverse,
low-resource contexts and use-cases. Our monitor
naturally inherits these limitations, as it consoli-
dates and standardizes many existing benchmarks
into a unified leaderboard.
In addition, both resource constraints and the
prototype nature of our system currently limit the
scope of our benchmarking runs. Evaluating all
models across the full benchmark—spanning up
to 200 languages and multiple tasks—would re-
quire substantial compute. At this stage, our goal
is to demonstrate the feasibility of the approach be-
fore exhaustively benchmarking every model. As
a result, our automated runs currently sample 10
instances per combination of model, task, and lan-
guage. We plan to scale up coverage in future it-
erations through additional compute resources and
community contributions.
5.2
Future Directions
While our monitor aims to offer a broad, inclusive
view of multilingual LLM performance, particu-
larly for low-resource languages, its current cov-
erage can still be extended. More localized mod-
els, benchmarks, and underrepresented languages
could still be added to provide a more complete
and impactful overview. To address this, we plan to
leverage our open-source framework to iteratively
include these together with regional communities
and researchers.
5.3
Summary
We introduced the AI Language Proficiency Moni-
tor, a comprehensive, continually updated bench-
mark that tracks the multilingual capabilities of
large language models across up to 200 languages.
By combining diverse evaluation datasets and pre-
senting results through an accessible and open-
source dashboard, our system enables develop-
ers, researchers, and policymakers to identify per-
formance disparities and support equitable lan-
guage representation. Our approach provides a
scalable foundation for inclusive, transparent, and
actionable multilingual AI evaluation. We invite
the broader community to contribute new mod-
els, tasks, and languages to further strengthen this
shared resource.
6

--- Page 7 ---

References
Julien Abadji, Pedro Ortiz Suarez, Laurent Romary, and
Benoît Sagot. 2022. Towards a cleaner document-
oriented multilingual crawled corpus. In Proceedings
of the Thirteenth Language Resources and Evalua-
tion Conference, pages 4344–4355, Marseille, France.
European Language Resources Association.
David Ifeoluwa Adelani, Hannah Liu, Xiaoyu Shen,
Nikita Vassilyev, Jesujoba O. Alabi, Yanke Mao, Hao-
nan Gao, and Annie En-Shiun Lee. 2024. SIB-200:
A Simple, Inclusive, and Big Evaluation Dataset for
Topic Classification in 200+ Languages and Dialects.
Preprint, arXiv:2309.07445.
David Ifeoluwa Adelani, Jessica Ojo, Israel Abebe Az-
ime, Jian Yun Zhuang, Jesujoba O. Alabi, Xuanli He,
Millicent Ochieng, Sara Hooker, Andiswa Bukula,
En-Shiun Annie Lee, Chiamaka Chukwuneke, Happy
Buzaaba, Blessing Sibanda, Godson Kalipe, Jonathan
Mukiibi, Salomon Kabongo, Foutse Yuehgoh, Mma-
sibidi Setaka, Lolwethu Ndolela, and 8 others. 2025.
IrokoBench: A New Benchmark for African Lan-
guages in the Age of Large Language Models.
Preprint, arXiv:2406.03368.
Kabir Ahuja, Harshita Diddee, Rishav Hada, Milli-
cent Ochieng, Krithika Ramesh, Prachi Jain, Ak-
shay Nambi, Tanuja Ganu, Sameer Segal, Mohamed
Ahmed, Kalika Bali, and Sunayana Sitaram. 2023.
MEGA: Multilingual evaluation of generative AI.
In Proceedings of the 2023 Conference on Empir-
ical Methods in Natural Language Processing, pages
4232–4267, Singapore. Association for Computa-
tional Linguistics.
Sanchit Ahuja, Divyanshu Aggarwal, Varun Gumma,
Ishaan Watts, Ashutosh Sathe, Millicent Ochieng,
Rishav Hada, Prachi Jain, Mohamed Ahmed, Kalika
Bali, and Sunayana Sitaram. 2024. MEGAVERSE:
Benchmarking large language models across lan-
guages, modalities, models and tasks. In Proceed-
ings of the 2024 Conference of the North American
Chapter of the Association for Computational Lin-
guistics: Human Language Technologies (Volume
1: Long Papers), pages 2598–2637, Mexico City,
Mexico. Association for Computational Linguistics.
Mikel Artetxe and Holger Schwenk. 2018.
Mas-
sively multilingual sentence embeddings for zero-
shot cross-lingual transfer and beyond. In Proceed-
ings of the 2018 Conference on Empirical Methods
in Natural Language Processing, pages 4971–4980.
Akari Asai, Sneha Kudugunta, Xinyan Yu, Terra
Blevins, Hila Gonen, Machel Reid, Yulia Tsvetkov,
Sebastian Ruder, and Hannaneh Hajishirzi. 2024.
BUFFET: Benchmarking large language models for
few-shot cross-lingual transfer. In Proceedings of
the 2024 Conference of the North American Chap-
ter of the Association for Computational Linguistics:
Human Language Technologies (Volume 1: Long
Papers), pages 1771–1800, Mexico City, Mexico. As-
sociation for Computational Linguistics.
Edward Bayes, Israel Abebe Azime, Jesujoba O. Al-
abi, Jonas Kgomo, Tyna Eloundou, Elizabeth Proehl,
Kai Chen, Imaan Khadir, Naome A. Etori, Sham-
suddeen Hassan Muhammad, Choice Mpanza, Igne-
ciah Pocia Thete, Dietrich Klakow, and David Ife-
oluwa Adelani. Uhura: A Benchmark for Evalu-
ating Scientific Question Answering and Truthful-
ness in Low-Resource African Languages. Preprint,
arXiv:2412.00948.
Wei-Lin Chiang, Zhuohan Li, Ziqing Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan
Zhuang, Yonghao Zhuang, Joseph E Gonzalez, and
1 others. 2023. Vicuna: An open-source chatbot
impressing gpt-4 with 90%* chatgpt quality. See
https://vicuna. lmsys. org (accessed 14 April 2023),
2(3):6.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord.
Think you have Solved Question An-
swering? Try ARC, the AI2 Reasoning Challenge.
Preprint, arXiv:1803.05457.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018. Think you have solved question an-
swering? try arc, the ai2 reasoning challenge. arXiv
preprint arXiv:1803.05457.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
Training Verifiers to Solve Math Word Problems.
Preprint, arXiv:2110.14168.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, Christopher Hesse, and John Schulman.
2021a. Training verifiers to solve math word prob-
lems. Preprint, arXiv:2110.14168.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, and 1 others. 2021b.
Training verifiers
to solve math word problems.
arXiv preprint
arXiv:2110.14168.
Alexis Conneau, Kartikay Khandelwal, Naman Goyal,
Vishrav Chaudhary, Guillaume Wenzek, Francisco
Guzmán, Edouard Grave, Myle Ott, Luke Zettle-
moyer, and Veselin Stoyanov. 2020a. Unsupervised
cross-lingual representation learning at scale. In Pro-
ceedings of the 58th Annual Meeting of the Asso-
ciation for Computational Linguistics, pages 8440–
8451, Online. Association for Computational Lin-
guistics.
Alexis Conneau, Shijie Wu, Haoran Li, Luke Zettle-
moyer, and Veselin Stoyanov. 2020b.
Emerging
cross-lingual structure in pretrained language mod-
els. In Proceedings of the 58th Annual Meeting of
7

--- Page 8 ---

the Association for Computational Linguistics, pages
6022–6034, Online. Association for Computational
Linguistics.
Marta R. Costa-jussà, James Cross, Onur Çelebi, Maha
Elbayad, Kenneth Heafield, Kevin Heffernan, Elahe
Kalbassi, Janice Lam, Daniel Licht, Jean Mail-
lard, Anna Sun, Skyler Wang, Guillaume Wen-
zek, Al Youngblood, Bapi Akula, Loic Barrault,
Gabriel Mejia Gonzalez, Prangthip Hansanti, John
Hoffman, and 20 others. 2024.
Scaling neural
machine translation to 200 languages.
Nature,
630(8018):841–846.
Jacob Devlin, Ming-Wei Chang, Kenton Lee, and
Kristina Toutanova. 2019. BERT: Pre-training of
deep bidirectional transformers for language under-
standing. In Proceedings of the 2019 Conference of
the North American Chapter of the Association for
Computational Linguistics: Human Language Tech-
nologies, Volume 1 (Long and Short Papers), pages
4171–4186, Minneapolis, Minnesota. Association for
Computational Linguistics.
David M. Eberhard, Gary F. Simons, and Charles D.
Fennig. 2025. Ethnologue: Languages of the World,
26 edition. SIL International, Dallas, Texas. Ac-
cessed July 3, 2025.
Kawin Ethayarajh and Dan Jurafsky. 2020. Utility is in
the eye of the user: A critique of nlp leaderboards.
In Proceedings of the 2020 Conference on Empirical
Methods in Natural Language Processing (EMNLP),
pages 3356–3363. Association for Computational
Linguistics.
Jinlan Fu, See-Kiong Ng, and Pengfei Liu. 2022. Poly-
glot prompt: Multilingual multitask prompt training.
In Proceedings of the 2022 Conference on Empiri-
cal Methods in Natural Language Processing, pages
9919–9935, Abu Dhabi, United Arab Emirates. As-
sociation for Computational Linguistics.
Leo Gao, Jonathan Tow, Baber Abbasi, Stella Bider-
man, Sid Black, Anthony DiPofi, Charles Foster,
Laurence Golding, Jeffrey Hsu, Alain Le Noac’h,
Haonan Li, Kyle McDonell, Niklas Muennighoff,
Chris Ociepa, Jason Phang, Laria Reynolds, Hailey
Schoelkopf, Aviya Skowron, Lintang Sutawika, and
5 others. 2024. The language model evaluation har-
ness.
Naman Goyal, Cynthia Gao, Vishrav Chaudhary, Peng-
Jen Chen, Guillaume Wenzek, Da Ju, Sanjana Kr-
ishnan, Marc’Aurelio Ranzato, Francisco Guzmán,
and Angela Fan. 2022. The Flores-101 evaluation
benchmark for low-resource and multilingual ma-
chine translation. Transactions of the Association for
Computational Linguistics, 10:522–538.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, and 1 others. 2024. The llama 3 herd
of models. arXiv preprint arXiv:2407.21783.
Daniil Gurgurov, Rishu Kumar, and Simon Ostermann.
2025. GrEmLIn: A repository of green baseline em-
beddings for 87 low-resource languages injected with
multilingual graph knowledge. In Findings of the
Association for Computational Linguistics: NAACL
2025, pages 1204–1221, Albuquerque, New Mexico.
Association for Computational Linguistics.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
Measuring Massive Multitask Language Understand-
ing. Preprint, arXiv:2009.03300.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2020. Measuring massive multitask language under-
standing. arXiv preprint arXiv:2009.03300.
Viet Dac Lai, Chien Van Nguyen, Nghia Trung Ngo,
Thuat Nguyen, Franck Dernoncourt, Ryan A. Rossi,
and Thien Huu Nguyen. 2023. Okapi: Instruction-
tuned Large Language Models in Multiple Languages
with Reinforcement Learning from Human Feedback.
Preprint, arXiv:2307.16039.
Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.
TruthfulQA: Measuring how models mimic human
falsehoods. In Proceedings of the 60th Annual Meet-
ing of the Association for Computational Linguistics
(Volume 1: Long Papers), pages 3214–3252, Dublin,
Ireland. Association for Computational Linguistics.
Thomas Mayer and Michael Cysouw. 2014. Creating
a massively parallel Bible corpus. In Proceedings
of the Ninth International Conference on Language
Resources and Evaluation (LREC‘14), pages 3158–
3163, Reykjavik, Iceland. European Language Re-
sources Association (ELRA).
Jessica Ojo, Odunayo Ogundepo, Akintunde Oladipo,
Kelechi Ogueji, Jimmy Lin, Pontus Stenetorp, and
David Ifeoluwa Adelani. 2025. Afrobench: How
good are large language models on african languages?
Preprint, arXiv:2311.07978.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-
Jing Zhu. 2002. Bleu: a method for automatic evalu-
ation of machine translation. In Proceedings of the
40th Annual Meeting of the Association for Compu-
tational Linguistics, pages 311–318, Philadelphia,
Pennsylvania, USA. Association for Computational
Linguistics.
Jonas Pfeiffer, Aishwarya Kamath, Andreas Rücklé,
Kyunghyun Cho,
and Iryna Gurevych. 2020.
Adapterfusion: Non-destructive task composition for
transfer learning. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing (EMNLP), pages 4876–4883.
Libo Qin, Qiguang Chen, Yuhang Zhou, Zhi Chen,
Yinghui Li, Lizi Liao, Min Li, Wanxiang Che, and
S Yu Philip. 2025. A survey of multilingual large
language models. Patterns, 6(1):101118.
8

--- Page 9 ---

Inioluwa Deborah Raji, Andrew Smart, and Rumman
White. 2021. Ai benchmarking: A meta-analysis and
the need for inclusive, dynamic metrics. Proceedings
of the ACM Conference on Fairness, Accountability,
and Transparency (FAccT), page 1104–1114.
Phillip Rust, Jonas Pfeiffer, Ivan Vuli´c, Sebastian Ruder,
and Iryna Gurevych. 2021. How good is your tok-
enizer? on the monolingual performance of multilin-
gual language models. In Proceedings of the 59th
Annual Meeting of the Association for Computational
Linguistics, pages 3118–3135.
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,
Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,
Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan
Das, and Jason Wei. 2022. Language Models are
Multilingual Chain-of-Thought Reasoners. Preprint,
arXiv:2210.03057.
Shivalika Singh, Angelika Romanou, Clémentine Four-
rier, David I. Adelani, Jian Gang Ngui, Daniel
Vila-Suero, Peerat Limkonchotiwat, Kelly Marchi-
sio, Wei Qi Leong, Yosephine Susanto, Raymond
Ng, Shayne Longpre, Wei-Yin Ko, Sebastian Ruder,
Madeline Smith, Antoine Bosselut, Alice Oh, An-
dre F. T. Martins, Leshem Choshen, and 5 others.
2025. Global MMLU: Understanding and Address-
ing Cultural and Linguistic Biases in Multilingual
Evaluation. Preprint, arXiv:2412.03304.
Gemma Team, Aishwarya Kamath, Johan Ferret, Shreya
Pathak, Nino Vieillard, Ramona Merhej, Sarah Perrin,
Tatiana Matejovicova, Alexandre Ramé, Morgane
Rivière, and 1 others. 2025. Gemma 3 technical
report. arXiv preprint arXiv:2503.19786.
Klaudia Thellmann, Bernhard Stadler, Michael Fromm,
Jasper Schulze Buschhoff, Alex Jude, Fabio Barth, Jo-
hannes Leveling, Nicolas Flores-Herr, Joachim Köh-
ler, René Jäkel, and Mehdi Ali. 2024a. Towards Mul-
tilingual LLM Evaluation for European Languages.
Preprint, arXiv:2410.08928.
Klaudia Thellmann, Bernhard Stadler, Michael Fromm,
Jasper Schulze Buschhoff, Alex Jude, Fabio Barth, Jo-
hannes Leveling, Nicolas Flores-Herr, Joachim Köh-
ler, René Jäkel, and Mehdi Ali. 2024b. Towards
multilingual llm evaluation for european languages.
Preprint, arXiv:2410.08928.
Maurice Weber, Dan Fu, Quentin Anthony, Yonatan
Oren, Shane Adams, Anton Alexandrov, Xiaozhong
Lyu, Huu Nguyen, Xiaozhe Yao, Virginia Adams,
and 1 others. 2024. Redpajama: an open dataset for
training large language models. Advances in neural
information processing systems, 37:116462–116492.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can a
machine really finish your sentence? In Proceedings
of the 57th Annual Meeting of the Association for
Computational Linguistics.
Tianyi Zhang, Varsha Kishore, Felix Wu, Kilian Q
Weinberger, and Yoav Artzi. 2019. Bertscore: Eval-
uating text generation with bert.
arXiv preprint
arXiv:1904.09675.
9

--- Page 10 ---

A
Appendix
Screenshot of the model leaderboard, showing aggregate score across languages per model, overall and by
task. The user can filter for specific types of models, or switch to a language-specific leaderboard for any
of the evaluated 200 languages.
10

```
