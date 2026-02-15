---
title: "2025-Pan-Banzhida Advancing Large Language Models for Tibetan with Curated - PDF Extract"
source_pdf: "2025-Pan-Banzhida Advancing Large Language Models for Tibetan with Curated.pdf"
pages: 13
extracted_at: "2026-02-15T17:54:27.932201"
---

# PDF Extract: 2025-Pan-Banzhida Advancing Large Language Models for Tibetan with Curated

**Source PDF:** 2025-Pan-Banzhida Advancing Large Language Models for Tibetan with Curated.pdf
**Total Pages:** 13

---

## Content

```
--- Page 1 ---

Advancing Large Language Models for Tibetan with Curated Data and
Continual Pre-Training
Leiyu Pan1, Bojian Xiong1, Lei Yang1, Renren Jin1,2, Shaowei Zhang1
Yue Chen1, Ling Shi1, Jiang Zhou1, Junru Wu1, Zhen Wang1, Jianxiang Peng1
Juesi Xiao1, Tianyu Dong1, Zhuowen Han1, Zhuo Chen1, Yuqi Ren1,2, Deyi Xiong1,2*†
1TJUNLP Lab, Tianjin University 2Yuanhui AI Lab
Abstract
Large language models have achieved remark-
able progress across many languages. However,
Tibetan, as a representative low-resource lan-
guage, is particularly underrepresented in exist-
ing models due to the scarcity of high-quality
training corpora. To address this gap, we cu-
rate the largest Tibetan pre-training corpus to
date, aggregating data from diverse sources and
applying a dedicated data cleaning and pro-
cessing pipeline tailored for Tibetan. With the
curated data, we continue pre/post-training a
multilingual base model to enhance its gen-
erative capabilities in Tibetan.
To evaluate
the Tibetan capabilities of the model, we cre-
ate new high-quality Tibetan benchmarks, and
complement them with existing public bench-
marks. Experimental results demonstrate that
our model consistently and significantly out-
performs both open-source models of similar
scale and Tibetan-tailored models across a wide
range of tasks.
1
Introduction
In recent years, large language models (LLMs)
have achieved remarkable progress, demonstrating
exceptional performance across a wide range of nat-
ural language processing tasks (Yang et al., 2025;
Liu et al., 2024; Grattafiori et al., 2024), largely
due to access to massive, high-quality training data
(Kaplan et al., 2020; Wettig et al., 2024). How-
ever, the pre-training corpora of mainstream LLMs
are predominantly composed of high-resource lan-
guages such as English and Chinese (Touvron et al.,
2023; Grattafiori et al., 2024). This imbalance in
data distribution has led to a strong performance
bias toward high-resource languages, while support
for low-resource languages remains significantly
limited (Zhu et al., 2024b; Sun et al., 2024).
*Corresponding author.
†Project Lead.
The root causes of this disparity lie in the inher-
ent scarcity of accessible data for low-resource lan-
guages, as well as the considerable challenges in-
volved in data collection, cleaning, and standardiza-
tion (Kudugunta et al., 2023; Penedo et al., 2024a).
These limitations hinder the development and effec-
tiveness of LLMs for underrepresented languages,
thereby preventing speakers of those languages
from benefiting equally from the latest advances in
artificial intelligence (Nguyen et al., 2024b; Dou
et al., 2024). Moreover, this technological imbal-
ance risks further concentrating linguistic resources
and innovation around dominant languages, pos-
ing a serious threat to global linguistic diversity
(Üstün et al., 2024) and cultural preservation (Xu
et al., 2024; Li et al., 2024). Therefore, advancing
research on LLMs for low-resource languages is
not only a matter of technological development but
also a critical step toward promoting AI equity and
safeguarding cultural diversity (Shen et al., 2024).
Tibetan, as a representative low-resource lan-
guage, is one of China’s minority languages and
is spoken by millions of native speakers. It serves
as a vital vehicle for the preservation of Tibetan
culture and historical heritage (Liang et al., 2024;
Huang et al., 2025). Despite its significant pop-
ulation base and cultural value, Tibetan remains
severely underrepresented in terms of digitized lin-
guistic resources and has long been categorized
as a low-resource language (Liu et al., 2022; Liu
and Best, 2025). In recent years, the development
of multilingual LLMs has led to gradual improve-
ments in support for Tibetan (Liu et al., 2024; Lv
et al., 2025). However, due to the dominance of
high-resource languages in training corpora and
the limited scale, quality, and standardization of Ti-
betan data, existing models still struggle with tasks
involving Tibetan understanding and generation
(Wenhao et al., 2024).
In light of the aforementioned challenges, we
create a multilingual LLM supporting Tibetan, Chi-
arXiv:2507.09205v4  [cs.CL]  28 Jul 2025

--- Page 2 ---

nese, and English. We present a comprehensive
pipeline for building a Tibetan-capable LLM, cov-
ering data curation, pre-training, post-training, and
evaluation.
To curate pre-training data for Tibetan, we build
our Tibetan pre-training corpus from four primary
sources: (1) publicly available datasets, (2) large-
scale web crawling, (3) synthetic data generation,
(4) proprietary data. To ensure high data quality, we
also develop a customized data cleaning pipeline
tailored for Tibetan. In total, we have collected
72 GB of cleaned Tibetan text, which, to the best
of our knowledge, constitutes the largest Tibetan
corpus ever constructed for LLM pre-training.
To build our model, we continue to pre-train
Qwen2.5-7B-base model (Qwen et al., 2025), a
strong open-source multilingual LLM, to extend
its capabilities to Tibetan. To facilitate effective
cross-lingual transfer and accelerate the model’s
adaptation, we incorporate both Chinese and En-
glish data alongside the curated Tibetan data during
this continual pre-training phase. Following pre-
training, we perform instruction tuning using mul-
tilingual instruction-following datasets collected
from open-source repositories in Tibetan, Chinese
and English, further enhancing ability of the model
to handle diverse downstream tasks across the three
languages.
For evaluation, given the limited availability of
standardized Tibetan benchmarks for large lan-
guage models, we construct multiple new Tibetan
evaluation datasets by automatically translating ex-
isting benchmarks into Tibetan. All translations
are rigorously proofread by native Tibetan speak-
ers. The translated benchmarks are supplemented
with existing public Tibetan benchmarks to pro-
vide a more comprehensive evaluation framework.
Results show that both our base and chat models
consistently outperform other models of similar
scale across a variety of tasks, and in some cases,
achieve performance comparable to significantly
larger LLMs. Additionally, by extending the model
vocabulary to include frequent Tibetan character
combinations, we further enhance both generation
quality and decoding efficiency, enabling faster in-
ference under identical runtime conditions.
Our main contributions can be summarized as
follows:
• We enhance the foundation for Tibetan natural
language processing by constructing a high-
quality Tibetan pre-training corpus (the largest
Tibetan dataset to date) and developing several
evaluation benchmarks specifically designed
for Tibetan LLMs.
• With the curated data, we build a multilingual
LLM with strong capabilities in Tibetan.
• Extensive evaluations show that our model
achieves strong improvements in accuracy
compared to other open-source models and
Tibetan-tailored models of similar scale across
various benchmarks.
2
Related Work
In recent years, multilingual LLMs have made sig-
nificant progress, gradually evolving from support-
ing a limited number of high-resource languages
to covering a broader range of low- and medium-
resource languages (Yang et al., 2025). This im-
provement is largely driven by the continued ex-
pansion of multilingual corpora, both in terms of
the number of supported languages and the amount
of data available for each language (Penedo et al.,
2024b). As a result, the multilingual capabilities
of LLMs have seen steady improvements (Üstün
et al., 2024; Ji et al., 2024). However, despite this
progress, current multilingual models still provide
insufficient support for Tibetan (Qwen et al., 2025).
Existing open-source multilingual corpora include
very limited Tibetan data in terms of both scale and
diversity, which significantly hampers model per-
formance on Tibetan language understanding and
generation (Kudugunta et al., 2023; Nguyen et al.,
2024a). To address this gap, we focus on build-
ing a large-scale, high-quality Tibetan pre-training
corpus and training a dedicated language model
with enhanced support for Tibetan, thus improving
performance in downstream Tibetan tasks.
To efficiently leverage language-specific data for
building models tailored to a particular language,
a straightforward approach is to combine the col-
lected data with multilingual corpora and train a
new model from scratch (Ji et al., 2024). How-
ever, this method is computationally expensive. As
a result, prior research has proposed several low-
cost alternatives to enhance existing models’ per-
formance on specific languages. One line of work
explores in-context learning techniques (Cahyaw-
ijaya et al., 2024). While these methods are rela-
tively efficient, they do not fundamentally improve
the model’s inherent capabilities in the target lan-
guage and typically assume that the base model

--- Page 3 ---

already has a reasonable degree of support for that
language. This limitation makes such methods less
effective for truly low-resource languages like Ti-
betan, where existing models perform poorly to
begin with. Another line of work adopts continued
pre-training to adapt pre-trained models to under-
represented languages. Notable examples include
Sailor (Dou et al., 2024) and LLaMaTurk (Toraman,
2024), which demonstrate that extending multilin-
gual models with targeted continual pre-training
can effectively enhance their capabilities in specific
languages. Inspired by this approach, we employ
a continued pre-training approach to enhance the
Tibetan language support of the Qwen2.5 model.
Several large language models with support
for Tibetan understanding and generation have
been proposed recently , e.g., TiLamb (Wen-
hao et al., 2024), Sunshine (Huang et al., 2025),
and T-LLaMa (Lv et al., 2025). Some of these
models adopt parameter-efficient fine-tuning tech-
niques like LoRA for continued pre-training (Hu
et al., 2022). In contrast, our approach uses full-
parameter fine-tuning, offering greater flexibility
and potential for adaptation. Moreover, compared
to the aforementioned models, our Tibetan training
corpus is larger in scale, richer in source diversity,
and covers a wider range of linguistic scenarios.
As a result, the model we trained on this corpus
achieves superior performance on both our curated
Tibetan benchmarks and existing public evaluation
datasets.
3
Pre-training Data Curation
During the pre-training data curation phase, we
collect Tibetan data from a wide range of sources.
In addition to gathering all available open-source
Tibetan corpora, we also include web-scraped con-
tent, synthetically generated data, and a portion of
proprietary resources. To ensure high data qual-
ity, we design and apply a dedicated data cleaning
pipeline specifically for Tibetan, which is used to
process the entire dataset.
3.1
Data Collection
Our data collection covers four main sources: open-
source data collection, web data crawling, synthetic
data generation, and private data usage. The com-
position of these sources is detailed in Appendix A.
Open-Source Data Collection
We extensively
collect Tibetan data from various open-source mul-
tilingual datasets, as well as from monolingual
Tibetan dataset. Detailed information about the
collected datasets is provided in Appendix B. The
majority of the data originates from web sources,
but it also includes content from other domains
such as news, books, and Wikipedia, contributing
to the overall diversity of the corpus.
Web Data Crawling
Although the open-source
data we have collected includes a wealth of web-
based content, it suffers from limited timeliness,
with many recent materials not reflected in exist-
ing datasets. To address this limitation, we utilize
the crawl4ai tool1 to collect data from 55 Tibetan-
language websites, resulting in a total of 204,125
webpages. The crawled data spans a wide range
of domains, which are primarily on news, but also
include content from books, Wikipedia, and other
categories, contributing to the diversity of our Ti-
betan corpus. Detailed information of web data
crawling is given in Appendix C.
Synthetic Data Generation
Synthetic data is
often used to compensate for the lack of real-
world data in low-resource settings, and it has been
shown to effectively improve the performance of
LLMs (Abdin et al., 2024). Since Tibetan is a low-
resource language with limited high-quality data,
we employ automatic data synthesis to supplement
our Tibetan corpus. Given that existed LLMs ex-
hibit limited ability in Tibetan monolingual genera-
tion, we choose to generate Tibetan data via trans-
lation. To further promote cross-lingual transfer,
we construct parallel corpora using both source lan-
guage sentences and their Tibetan translations for
training. Specifically, we sample a portion of the
FineWeb-Edu (Penedo et al., 2024a) and Cosmo-
pedia (Ben Allal et al., 2024) pre-training datasets,
translate them into Tibetan using the Google Trans-
late API, and organize the resulting parallel data
using the instruction templates introduced by Zhu
et al. (2024a).
Private Data Usage
In addition to publicly avail-
able data, we also utilize a set of private Tibetan-
language digital resources, primarily consisting of
books and classical materials. These resources are
obtained from non-public but legally accessible
sources, such as internal digital archives and insti-
tutional collaborations. All data used in this cate-
gory contain no personally identifiable information
or user-generated content, and are solely used for
research and model training purposes.
1https://github.com/unclecode/crawl4ai

--- Page 4 ---

3.2
Data Cleaning and Deduplication
After collecting the Tibetan corpus, we perform
a comprehensive data cleaning process to ensure
high data quality suitable for LLM training. Due to
the unique characteristics of Tibetan script, we de-
velop a customized data cleaning pipeline tailored
to Tibetan, inspired by the FineWeb data process-
ing workflow (Penedo et al., 2024a). Our cleaning
pipeline consists of two main stages: language fil-
tering and quality filtering. For language filtering,
we use the FastText language classifier (Grave et al.,
2018) to identify Tibetan text, removing any docu-
ments with a Tibetan confidence score below 0.5.
For quality filtering, we apply a combination of
five filtering strategies: Gopher duplicate filtering,
Gopher quality filtering (Rae et al., 2021), C4 qual-
ity filtering (Raffel et al., 2020), FineWeb quality
filtering and sensitive content filtering. Some of
the heuristic rules in these procedures are slightly
modified to better accommodate the characteristics
of Tibetan text. Detailed descriptions of quality
filtering are provided in Appendix D.
After completing the data cleaning process, we
apply MinHash-based deduplication using the Data-
Trove tool2 to remove highly redundant text seg-
ments. This step helps enhance the diversity and
effectiveness of the pretraining data.
3.3
Data Composition
After cleaning and deduplicating the Tibetan data,
we further enhance the model’s Tibetan capabili-
ties by incorporating high-quality, multi-domain
Chinese and English data (Chen et al., 2024) into
the continued pre-training process. This approach
leverages cross-lingual generalization to transfer
the model’s existing strengths in Chinese and En-
glish to Tibetan. Additionally, it functions as a
data replay strategy, helping to prevent catastrophic
forgetting of general knowledge that could arise
if the model were trained exclusively on Tibetan
data. Additionally, we adopt a balanced multilin-
gual data ratio, aiming to maximize the model’s Ti-
betan performance by mitigating interference from
high-resource languages while still benefiting from
cross-lingual generalization. The data volumes
used for continued pre-training in each language
are summarized in Table 1.
2https://github.com/huggingface/datatrove
Language
Category
Volume
Token
English
Books
9.8 G
2.77 B
Code
9.7 G
4.42 B
Encyclopedia
3 G
0.77 B
Mathematical Corpora
4.6 G
1.27 B
Academic Papers
5.8 G
1.47 B
QA Forums
2.7 G
0.90 B
Web Pages
13.9 G
3.35 B
Chinese
Books
8.5 G
2.72 B
Encyclopedia
3.3 G
1.00 B
QA Forums
3 G
0.88 B
Web Pages
35.1 G
10.23 B
Tibetan
Books
7.5 G
0.88 B
Web Pages
64.8 G
7.61 B
Table 1: Pre-training data volume for three languages.
4
Continual Pre-training
We select Qwen2.5-7B-base (Qwen et al., 2025)
as our foundation model due to its strong multi-
lingual capabilities, which provides a solid foun-
dation for cross-lingual transfer to low-resource
languages such as Tibetan. To enhance its ability to
process Tibetan text, we first expand the vocabulary
to include commonly used Tibetan character com-
binations, enabling more efficient and accurate tok-
enization. We then adopt a two-stage continued pre-
training strategy: a language-balanced pre-training
stage with a short context window to transfer Chi-
nese and English knowledge to Tibetan, followed
by a long-context pre-training stage to extend the
model’s context length. In future work, we plan to
adopt the recently released Qwen3-8B-base model
(Yang et al., 2025) as our new foundation model,
leveraging its improved multilingual performance
to further enhance Tibetan language modeling.
4.1
Vocabulary Expansion
The original Qwen2.5 tokenizer tends to over-
segment Tibetan characters, resulting in higher
computational costs and reduced generation con-
trollability. To address this, we extend its vocabu-
lary by training a 15K Byte-level BPE tokenizer on
a representative Tibetan corpus and merging it with
the original vocabulary, removing duplicates. The
final vocabulary contains 165,428 tokens, enabling
more efficient and accurate Tibetan tokenization.
4.2
Stage 1: Language Balanced Pre-training
The first stage of continued pre-training aims to
build foundational Tibetan capabilities by lever-
aging both Tibetan monolingual data and cross-
lingual transfer from high-resource languages. To

--- Page 5 ---

ensure knowledge retention and avoid catastrophic
forgetting, we use a balanced mix of Chinese, En-
glish, and Tibetan data during training.
After tokenization using our extended tokenizer,
the training dataset comprises approximately 15B
Chinese tokens, 15B English tokens, and 8.5B Ti-
betan tokens. It is worth noting that although the
raw volume of Tibetan data is substantial, the final
token count is lower due to the higher compression
efficiency of our tokenizer, which is specifically
adapted for Tibetan.
In this stage, we perform continual pre-training
starting from the Qwen2.5-7B-base model, preserv-
ing its original configuration. To improve training
efficiency, we use a relatively short context win-
dow of 4K tokens. Additional training details are
provided in Appendix E.
4.3
Stage 2: Long Context Pre-training
To enhance the model’s capability for processing
long inputs, we conduct long context pre-training
based on the first stage model to extend the context
window to 32K tokens. Since Qwen2.5-7B-base ex-
tensively pre-training on 32K long contexts (Qwen
et al., 2025), only a minimal amount of training is
required to achieve our objective.
The training data consist of trilingual mixed text
in Chinese (0.56B), English (2.5B), and Tibetan
(1.5B, which is not utilized in the first stage), total-
ing 4.56B tokens. This contributes to improving the
model’s generalization capability for Tibetan long
contexts. Regarding training parameters, we main-
tain consistency with Qwen2.5-7B-base and the
first stage pre-training. Specific data distribution
and training parameters are detailed in Appendix
F.
We evaluate the model’s performance in
long context comprehension through needle-in-a-
haystack evaluation using Claude as the evaluator.
Due to the scarcity of Tibetan data, we construct a
needle-in-a-haystack dataset for Tibetan text and
employ recent news articles as needles to avoid the
influence of the model’s inherent knowledge on the
evaluation. Experimental results demonstrate that
the model after long context pre-training signifi-
cantly outperforms the model that completed only
the first stage pre-training. Detailed experiments
are provided in Appendix F.
5
Post Training
After continual pre-training, the model has ac-
quired foundational capabilities in Tibetan. To
further enhance its ability to follow instructions,
we perform instruction tuning using a diverse and
richly curated set of instruction data. In terms
of domain coverage, the open-source instruction
data we have collected spans a wide range of ar-
eas, including instruction following, multi-turn dia-
logue, subject-specific knowledge, logical reason-
ing, translation, summarization and etc. This di-
verse coverage is designed to comprehensively en-
hance the model’s alignment capabilities across
different tasks. From a linguistic perspective, to
facilitate the transfer of instruction-following capa-
bilities from Chinese and English to Tibetan, we
construct a multilingual instruction dataset that cov-
ers three languages. Detailed information on the
post-training data and process is provided in Ap-
pendix G.
6
Experiments
Due to the current lack of standardized Tibetan
benchmarks for LLMs, we constructed four bench-
marks to evaluate general Tibetan capabilities.
Combined with two existing benchmarks for tra-
ditional Tibetan NLP tasks, this enables a compre-
hensive evaluation of model performance. Experi-
mental results demonstrate that our model outper-
forms both open-source models of similar scale and
Tibetan-tailored models across all evaluated tasks.
6.1
General Tibetan Benchmark Construction
Existing benchmarks for evaluating LLMs are pre-
dominantly designed for high-resource languages,
with limited resources available for Tibetan. To
facilitate systematic evaluation of Tibetan LLMs
across a wide range of tasks, we constructed
general-purpose Tibetan benchmarks based on the
translation of several well-established English eval-
uation benchmarks, including HellaSwag (Zellers
et al., 2019), ARC (Clark et al., 2018), Xcopa
(Ponti et al., 2020), and XStoryCloze (Lin et al.,
2021).
We leveraged the Claude-Sonnet-3.7 model,
which demonstrates strong Tibetan generation ca-
pabilities, to translate the original datasets into Ti-
betan. To ensure the quality and reliability of the
translated data, we performed a rigorous multi-
stage review process covering semantic consis-
tency, grammatical correctness, cultural appropri-

--- Page 6 ---

Model
Hellaswag-bo
ARC-bo
Xcope-bo
Xstorycloze-bo
TibetanQA
(acc)
(acc_norm)
(acc)
(acc)
(acc)
(EM)
(F1)
Ours-Base
30.30
36.20
44.32
59.80
60.80
49.43
66.15
Ours-Base-32k
30.09
36.58
44.62
58.60
60.60
38.42
55.52
Ours-SFT
30.64
36.71
48.39
57.80
61.86
46.15
63.15
Qwen3-8B
27.07
30.56
29.16
50.40
50.37
17.80
30.22
LLaMA3.1-8B-Instruct
27.28
32.00
29.31
51.60
51.69
36.09
53.04
Qwen2.5-7B-base
26.69
31.57
29.60
51.80
49.97
19.31
32.38
Qwen2.5-7B-Instruct
26.46
31.03
28.47
51.60
50.43
10.15
18.42
DeepSeek-R1-Distill-Llama-8B
25.96
30.67
30.38
50.40
48.50
9.88
17.99
Table 2: Performance comparison between our models and open-source models on different tasks.
Model
Hellaswag-bo
Arc-bo
Xcope-bo
Xstorycloze-bo
TibetanQA
Flores-200
(acc)
(acc_norm)
(acc)
(acc)
(acc)
(EM)
(F1)
zh-bo
en-bo
Ours-Base
30.30
36.20
44.32
59.80
60.80
49.43
66.15
13.81
9.20
Ours-Base-32k
30.09
36.58
44.62
58.60
60.60
38.42
55.52
20.86
13.56
Ours-SFT
30.64
36.71
48.39
57.80
61.86
46.15
63.15
21.56
11.42
Yak_Llama2_7B
24.67
26.40
25.64
53.00
48.37
0.12
0.24
11.81
11.10
Tibetan-Alpaca-7B
25.95
28.23
27.94
51.20
49.97
2.47
4.81
4.87
5.69
Tibetan-Llama2-7B
26.09
27.58
27.54
50.60
49.37
1.20
2.38
11.81
11.10
Table 3: Performance of our models compared to other Tibetan models on different benchmarks.
ateness, and content safety. Detailed translation
and quality review procedures are provided in Ap-
pendix H. Ultimately, we constructed four bench-
marks: HellaSwag-bo, ARC-bo, Xcopa-bo, and
XStoryCloze-bo.
6.2
Evaluation Benchmarks
We evaluated our model on a diverse set of Ti-
betan benchmarks, including our constructed tasks
(HellaSwag-bo, ARC-bo, Xcopa-bo, XStoryCloze-
bo) for reasoning and knowledge assessment, Ti-
betanQA (Sun et al., 2021) for reading comprehen-
sion, and FLORES-200 (nll, 2024) for multilingual
translation. Detailed benchmark descriptions are
provided in Appendix I.
6.3
Comparison against Open-Source Models
We conducted a comparative evaluation of three
versions of our model: Ours-Base, which is trained
with one stage of continual pretraining; Ours-
Base-32k, which undergoes two stages of con-
tinual pretraining; and Ours-SFT, which is fur-
ther instruction-tuned. These models are evaluated
against leading general-purpose open-source mod-
els on both standard reasoning and Tibetan-specific
benchmarks.
On multiple-choice reasoning tasks such as
Hellaswag-bo and ARC-bo, our models consis-
tently outperform the baselines in accuracy scores.
The advantage is even more pronounced on Ti-
betanQA, where our models outperform general-
purpose models by a large margin in both EM and
F1 scores. These results underscore the effective-
ness of our continued pretraining strategy, instruc-
tion tuning, and data construction pipeline in im-
proving performance for low-resource languages
like Tibetan.
6.4
Comparison against Existing
Tibetan-Tailored Models
We further compared our models with several
instruction-tuned models specifically designed for
Tibetan. As shown in Table 3, our model con-
sistently outperform existing Tibetan instruction-
tuned models across all tasks. In particular, Ours-
SFT achieves the strongest overall performance,
showing substantial improvements in reading com-
prehension and question answering, where other
models fall significantly behind.
Moreover, in
both zh-bo and en-bo translation tasks, our mod-
els achieve the highest BLEU scores among all
evaluated models, demonstrating strong multilin-
gual alignment and effective cross-lingual gener-
alization. It is worth noting that our comparison
only includes open-source Tibetan-tailored models.
Models such as Sun-Shine (Huang et al., 2025),
which are not publicly available, are not included
in this evaluation.

--- Page 7 ---

7
Conclusion
To address the limited support for Tibetan in exist-
ing models, we construct a high-quality, large-scale
Tibetan pre-training corpus. With the curated cor-
pus, we perform continual pretraining to develop
a multilingual large language model supporting
Tibetan, Chinese, and English. Our model demon-
strates superior performance compared to both
general-purpose open-source models and Tibetan-
tailored models of similar scale on our constructed
Tibetan benchmark as well as traditional Tibetan
NLP tasks.
Limitations
Due to budget constraints, our current Tibetan
pre-training corpus does not include data obtained
through OCR of PDF documents. We are actively
collecting Tibetan book PDFs to support future
research in this direction. Additionally, limited
computational resources have restricted our contin-
ued pre-training experiments to the 7B model scale.
Exploring larger model scales will be left for future
work.
References
2024. Scaling neural machine translation to 200 lan-
guages. Nature, 630(8018):841–846.
Marah Abdin, Jyoti Aneja, Harkirat Behl, Sébastien
Bubeck, Ronen Eldan, Suriya Gunasekar, Michael
Harrison, Russell J Hewett, Mojan Javaheripi, Piero
Kauffmann, and 1 others. 2024. Phi-4 technical re-
port. arXiv preprint arXiv:2412.08905.
Loubna Ben Allal, Anton Lozhkov, Guilherme Penedo,
Thomas Wolf, and Leandro von Werra. 2024. Cos-
mopedia.
Samuel Cahyawijaya, Holy Lovenia, and Pascale Fung.
2024. Llms are few-shot in-context low-resource
language learners. In Proceedings of the 2024 Con-
ference of the North American Chapter of the Asso-
ciation for Computational Linguistics: Human Lan-
guage Technologies (Volume 1: Long Papers), pages
405–433.
Jie Chen, Zhipeng Chen, Jiapeng Wang, Kun Zhou, Yu-
tao Zhu, Jinhao Jiang, Yingqian Min, Wayne Xin
Zhao, Zhicheng Dou, Jiaxin Mao, and 1 others.
2024. Towards effective and efficient continual pre-
training of large language models. arXiv preprint
arXiv:2407.18743.
Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot,
Ashish Sabharwal, Carissa Schoenick, and Oyvind
Tafjord. 2018. Think you have solved question an-
swering? try arc, the ai2 reasoning challenge. arXiv
preprint arXiv:1803.05457.
Longxu Dou, Qian Liu, Guangtao Zeng, Jia Guo, Ji-
ahui Zhou, Xinnian Mao, Ziqi Jin, Wei Lu, and Min
Lin. 2024. Sailor: Open language models for south-
east asia. In Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing:
System Demonstrations, pages 424–435.
Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri,
Abhinav Pandey, Abhishek Kadian, Ahmad Al-
Dahle, Aiesha Letman, Akhil Mathur, Alan Schelten,
Alex Vaughan, and 1 others. 2024. The llama 3 herd
of models. arXiv preprint arXiv:2407.21783.
Édouard Grave, Piotr Bojanowski, Prakhar Gupta, Ar-
mand Joulin, and Tomáš Mikolov. 2018. Learning
word vectors for 157 languages. In Proceedings of
the Eleventh International Conference on Language
Resources and Evaluation (LREC 2018).
Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and
Weizhu Chen. 2022. Lora: Low-rank adaptation of
large language models. In The Tenth International
Conference on Learning Representations, ICLR 2022,
Virtual Event, April 25-29, 2022. OpenReview.net.
Cheng Huang, Fan Gao, Nyima Tashi, Yutong Liu, Xi-
angxiang Wang, Thupten Tsering, Ban Ma-bao, Ren-
zeg Duojie, Gadeng Luosang, Rinchen Dongrub, and
1 others. 2025. Sun-shine: A large language model
for tibetan culture. arXiv preprint arXiv:2503.18288.
Shaoxiong Ji, Zihao Li, Indraneil Paul, Jaakko Paavola,
Peiqin Lin, Pinzhen Chen, Dayyán O’Brien, Hengyu
Luo, Hinrich Schütze, Jörg Tiedemann, and 1 others.
2024. Emma-500: Enhancing massively multilingual
adaptation of large language models. arXiv preprint
arXiv:2409.17892.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B
Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models.
arXiv
preprint arXiv:2001.08361.
Sneha Kudugunta, Isaac Caswell, Biao Zhang, Xavier
Garcia, Derrick Xin, Aditya Kusupati, Romi Stella,
Ankur Bapna, and Orhan Firat. 2023. Madlad-400:
A multilingual and document-level large audited
dataset. Advances in Neural Information Process-
ing Systems, 36:67284–67296.
Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana
Sitaram, and Xing Xie. 2024. Culturellm: Incorpo-
rating cultural differences into large language models.
Advances in Neural Information Processing Systems,
37:84799–84838.
Yatao Liang, Hui Lv, Yan Li, La Duo, Chuanyi Liu, and
Qingguo Zhou. 2024. Tibetan-bert-wwm: a tibetan
pretrained model with whole word masking for text
classification. IEEE Transactions on Computational
Social Systems.

--- Page 8 ---

Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu
Wang, Shuohui Chen, Daniel Simig, Myle Ott, Na-
man Goyal, Shruti Bhosale, Jingfei Du, and 1 others.
2021. Few-shot learning with multilingual language
models. arXiv preprint arXiv:2112.10668.
Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang,
Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi
Deng, Chenyu Zhang, Chong Ruan, and 1 others.
2024. Deepseek-v3 technical report. arXiv preprint
arXiv:2412.19437.
Shuheng Liu and Michael Best. 2025. A survey of nlp
progress in sino-tibetan low-resource languages. In
Proceedings of the 2025 Conference of the Nations of
the Americas Chapter of the Association for Compu-
tational Linguistics: Human Language Technologies
(Volume 1: Long Papers), pages 7804–7825.
Sisi Liu, Junjie Deng, Yuan Sun, and Xiaobing Zhao.
2022. Tibert: Tibetan pre-trained language model.
In 2022 IEEE International Conference on Systems,
Man, and Cybernetics (SMC), pages 2956–2961.
IEEE.
Ilya Loshchilov and Frank Hutter. 2017.
Decou-
pled weight decay regularization.
arXiv preprint
arXiv:1711.05101.
Hui Lv, Chi Pu, La Duo, Yan Li, Qingguo Zhou, and Jun
Shen. 2025. T-llama: a tibetan large language model
based on llama2. Complex & Intelligent Systems,
11(1):72.
Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu
Man, Nghia Trung Ngo, Franck Dernoncourt, Ryan A
Rossi, and Thien Huu Nguyen. 2024a. Culturax: A
cleaned, enormous, and multilingual dataset for large
language models in 167 languages. In Proceedings of
the 2024 Joint International Conference on Compu-
tational Linguistics, Language Resources and Evalu-
ation (LREC-COLING 2024), pages 4226–4237.
Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani
Aljunied, Zhiqiang Hu, Chenhui Shen, Yew Ken
Chia, Xingxuan Li, Jianyu Wang, Qingyu Tan, and
1 others. 2024b. Seallms-large language models for
southeast asia. In Proceedings of the 62nd Annual
Meeting of the Association for Computational Lin-
guistics (Volume 3: System Demonstrations), pages
294–304.
Guilherme Penedo, Hynek Kydlíˇcek, Anton Lozhkov,
Margaret Mitchell,
Colin A Raffel,
Leandro
Von Werra, Thomas Wolf, and 1 others. 2024a. The
fineweb datasets: Decanting the web for the finest
text data at scale. Advances in Neural Information
Processing Systems, 37:30811–30849.
Guilherme Penedo, Hynek Kydlíˇcek, Vinko Sabolˇcec,
Bettina Messmer, Negar Foroutan, Martin Jaggi,
Leandro von Werra, and Thomas Wolf. 2024b.
Fineweb2: A sparkling update with 1000s of lan-
guages.
Edoardo Maria Ponti, Goran Glavaš, Olga Majewska,
Qianchu Liu, Ivan Vuli´c, and Anna Korhonen. 2020.
Xcopa: A multilingual dataset for causal common-
sense reasoning. arXiv preprint arXiv:2005.00333.
Qwen, :, An Yang, Baosong Yang, Beichen Zhang,
Binyuan Hui, Bo Zheng, Bowen Yu, Chengyuan
Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan
Lin, Jian Yang, Jianhong Tu, Jianwei Zhang, Jianxin
Yang, Jiaxi Yang, Jingren Zhou, and 25 oth-
ers. 2025.
Qwen2.5 technical report.
Preprint,
arXiv:2412.15115.
Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie
Millican, Jordan Hoffmann, Francis Song, John
Aslanides, Sarah Henderson, Roman Ring, Susan-
nah Young, and 1 others. 2021. Scaling language
models: Methods, analysis & insights from training
gopher. arXiv preprint arXiv:2112.11446.
Colin Raffel, Noam Shazeer, Adam Roberts, Katherine
Lee, Sharan Narang, Michael Matena, Yanqi Zhou,
Wei Li, and Peter J Liu. 2020. Exploring the lim-
its of transfer learning with a unified text-to-text
transformer. Journal of machine learning research,
21(140):1–67.
Samyam Rajbhandari, Jeff Rasley, Olatunji Ruwase,
and Yuxiong He. 2020. Zero: Memory optimizations
toward training trillion parameter models. In SC20:
International Conference for High Performance Com-
puting, Networking, Storage and Analysis, pages 1–
16. IEEE.
Lingfeng Shen, Weiting Tan, Sihao Chen, Yunmo Chen,
Jingyu Zhang, Haoran Xu, Boyuan Zheng, Philipp
Koehn, and Daniel Khashabi. 2024. The language
barrier: Dissecting safety challenges of llms in multi-
lingual contexts. In Findings of the Association for
Computational Linguistics ACL 2024, pages 2668–
2680.
Haoran Sun, Renren Jin, Shaoyang Xu, Leiyu Pan, Men-
glong Cui, Jiangcun Du, Yikun Lei, Lei Yang, Ling
Shi, Juesi Xiao, and 1 others. 2024. Fuxitranyu: A
multilingual large language model trained with bal-
anced data. In Proceedings of the 2024 Conference
on Empirical Methods in Natural Language Process-
ing: Industry Track, pages 1499–1522.
Y Sun, S Liu, C Chen, Z Dan, and X Zhao. 2021. Con-
struction of high-quality tibetan dataset for machine
reading comprehension. In Proceedings of the 20th
Chinese National Conference on Computational Lin-
guistics, pages 208–218.
Cagri Toraman. 2024.
Llamaturk: Adapting open-
source generative large language models for low-
resource language. arXiv preprint arXiv:2405.07745.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, and 1 others. 2023. Llama 2: Open foun-
dation and fine-tuned chat models. arXiv preprint
arXiv:2307.09288.

--- Page 9 ---

Ahmet Üstün, Viraat Aryabumi, Zheng Yong, Wei-Yin
Ko, Daniel D’souza, Gbemileke Onilude, Neel Bhan-
dari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid, and
1 others. 2024. Aya model: An instruction finetuned
open-access multilingual language model. In Pro-
ceedings of the 62nd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 1: Long
Papers), pages 15894–15939.
Zhuang Wenhao, Sun Yuan, and Zhao Xiaobing. 2024.
Tilamb: A tibetan large language model based on
incremental pre-training. In Proceedings of the 23rd
Chinese National Conference on Computational Lin-
guistics (Volume 1: Main Conference), pages 254–
267.
Alexander Wettig, Aatmik Gupta, Saumya Malik, and
Danqi Chen. 2024. Qurating: Selecting high-quality
data for training language models. In International
Conference on Machine Learning, pages 52915–
52971. PMLR.
Shaoyang Xu, Yongqi Leng, Linhao Yu, and Deyi Xiong.
2024. Self-pluralising culture alignment for large
language models. arXiv preprint arXiv:2410.12971.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui,
Bo Zheng,
Bowen Yu,
Chang
Gao, Chengen Huang, Chenxu Lv, and 1 others.
2025.
Qwen3 technical report.
arXiv preprint
arXiv:2505.09388.
Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali
Farhadi, and Yejin Choi. 2019. Hellaswag: Can a
machine really finish your sentence? arXiv preprint
arXiv:1905.07830.
Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan
Ye, Zheyan Luo, Zhangchi Feng, and Yongqiang Ma.
2024. Llamafactory: Unified efficient fine-tuning
of 100+ language models. In Proceedings of the
62nd Annual Meeting of the Association for Compu-
tational Linguistics (Volume 3: System Demonstra-
tions), Bangkok, Thailand. Association for Computa-
tional Linguistics.
Dawei Zhu, Sony Trenous, Xiaoyu Shen, Dietrich
Klakow, Bill Byrne, and Eva Hasler. 2024a.
A
preference-driven paradigm for enhanced translation
with large language models. In Proceedings of the
2024 Conference of the North American Chapter of
the Association for Computational Linguistics: Hu-
man Language Technologies (Volume 1: Long Pa-
pers), pages 3385–3403.
Shaolin Zhu, Shaoyang Xu, Haoran Sun, Leiyu Pan,
Menglong Cui, Jiangcun Du, Renren Jin, António
Branco, Deyi Xiong, and 1 others. 2024b. Multi-
lingual large language models: A systematic survey.
arXiv preprint arXiv:2411.11072.

--- Page 10 ---

Data Source
Language
Size (After Filter)
Open-source data
Tibetan
9.53 G
Web data crawling
Tibetan
4.18 G
Synthetic data
Tibetan, Chinese, English
17.46 G
Private data
Tibetan
41.13 G
Table 4: Overview of the four main sources of Tibetan training data.
A
Tibetan Data Composition
To support large-scale Tibetan language modeling,
we collect a diverse and high-quality training cor-
pus from four major sources: open-source datasets,
web data crawling, synthetic data generation, and
private data. These data sources vary in style, do-
main coverage, and linguistic features, and together
form a comprehensive Tibetan pre-training corpus.
Table 4 summarizes the detail information of each
data component.
B
Open-Source Data Collection
The open-source Tibetan corpus we collected pri-
marily comes from two sources: (1) the Tibetan
portions of multilingual open-source datasets, and
(2) dedicated monolingual Tibetan datasets. These
corpora cover a wide range of domains. However,
we observe that a portion of the web-based data
originates from different snapshots of Common
Crawl, which may introduce redundancy. To ad-
dress this, we appliy deduplication to remove du-
plicate content across time.
C
Web Data Crawling
We manually collected 45 Tibetan-language web-
sites and extracted textual data from them. Most
of these sites are news-oriented, and our primary
goal is to obtain up-to-date Tibetan text. During
the web crawling process, we extracted hyperlinks
from each page and determined whether the linked
page belongs to the same root domain. If so, and
the page has not been previously visited, we recur-
sively crawl the subpage.
D
Quality Filtering
Gopher Duplicate Filtering
This method re-
moves both documents with a large number of
short, repeated segments and those with low du-
plication but excessively long content. We measure
duplication at both the sentence and paragraph level
by computing the proportion of duplicated content
and the proportion of characters within duplicated
segments.
• Character proportion in repeated n-grams:
For 2-gram, 3-gram, and 4-gram patterns, we
compute the proportion of characters con-
tained in the most frequent repeated n-gram
relative to the total number of characters in the
document, with filtering thresholds set at 0.20,
0.18, and 0.16, respectively. In contrast, for
n-grams ranging from 5 to 10, we calculate
the proportion of characters contained in all
repeated n-grams relative to the total character
count. The corresponding thresholds decrease
gradually from 0.15 for 5-grams to 0.10 for
10-grams.
• Character proportion in duplicated sen-
tences: Documents in which duplicated sen-
tences contain more than 20% of the total char-
acters are filtered out.
• Duplication ratio: Documents are filtered out
if more than 30% of their sentences or 30% of
their paragraphs are exact duplicates.
Gopher Quality Filtering
This stage filters out
any documents that violate the quality heuristics
defined in the Gopher data pipeline. Specifically, a
document is removed if it meets any of the follow-
ing conditions:
• The document contains fewer than 50 words
or more than 10,000 words.
• The document has an average word length less
than 2 or greater than 10.
• The document is with a symbol-to-word ratio
greater than 0.1.
• Fewer than 80% of words in the document
contain at least one alphabetic character.
• More than 90% of sentences in the document
begin with bullet points.

--- Page 11 ---

• More than 30% of sentences in the document
end with ellipses.
To better handle Tibetan text, we replaced the
default NLTK tokenizer3 with a custom tokenizer
designed specifically for Tibetan. This allows for
more accurate tokenization and filtering tailored to
the unique linguistic features of Tibetan.
C4 Quality Filtering
The following filtering
rules are applied to ensure data cleanliness, in line
with the C4 dataset preprocessing strategy:
• Only lines containing at least three words are
retained.
• Any page containing words from a predefined
list of offensive, profane, obscene, or other-
wise inappropriate terms is discarded.
• All lines containing the word "Javascript" are
removed.
• Any page containing the phrase "lorem ipsum"
is discarded.
• Any page containing curly braces is removed.
• Since some crawled pages originated from
Wikipedia and included citation markers, all
pages containing such citation patterns are
excluded.
• To eliminate templated or boilerplate legal
content, we remove any line that contains
phrases such as “terms of use”, “privacy pol-
icy”, “cookie policy”, “uses cookies”, “use of
cookie”, or “use cookie”.
FineWeb Quality Filtering
Documents that vi-
olate the FineWeb quality heuristics are removed.
Specifically, a document is filtered out if it meets
any of the following conditions:
• More than 67% of its sentences have a length
less than or equal to 30 characters.
• After removing empty lines, the proportion of
repeated characters exceeds 1% of the total
character count.
• The ratio of newline characters to total word
count exceeds 0.3.
3https://github.com/nltk/nltk
Sensitive Content Filtering
To eliminate sensi-
tive content from the collected data, we manually
curated a list of sensitive terms. Any document con-
taining one or more terms from this list is filtered
out.
E
Continual Pre-training
To improve training efficiency, we adopted a pack-
ing strategy (Raffel et al., 2020) to preprocess the
data. This involves concatenating and truncating
the data to ensure that each training sample is ex-
actly 4096 tokens in length. Given the large volume
of training data, we also applied a pre-tokenization
strategy, where the tokenized and packed datasets
are preprocessed and saved in advance to stream-
line the subsequent training process.
For the training framework, we used the LLaMA-
Factory library (Zheng et al., 2024) in combination
with DeepSpeed, enabling the ZeRO Stage 2 opti-
mization strategy (Rajbhandari et al., 2020). Train-
ing was conducted using 32 A800 GPUs with bf16
precision. Regarding optimization, we used the
standard AdamW optimizer (Loshchilov and Hut-
ter, 2017) with a maximum gradient norm of 1.0.
The learning rate was set to 5e-5, with a warmup
ratio of 0.1, and we adopted a cosine learning rate
scheduler.
F
Long Context Pre-training
Data Distribution. To fully account for the distri-
butional characteristics of the training data in the
first stage and further enhance the model’s long con-
text processing capabilities in Tibetan, we added
long mixed-language texts (Chinese, English, and
Tibetan) as training corpora in the second training
stage.We sampled 0.56B tokens of Chinese data,
2.5B tokens of English data, and 1.5B tokens of
Tibetan data (unused in the first stage) from long
context sources in each respective language, result-
ing in a trilingual long context training set totaling
4.56B tokens.
Training Parameters.
For training config-
urations, we maintained consistency with the
Qwen2.5-7B-base model by setting the RoPE θ
parameter to 1,000,000. The global batch size was
set to 128 to ensure consistency in the number of
tokens per batch with the first stage pre-training.
Additionally, the learning rate was reduced from 5e-
5 to 1e-5, while all other hyperparameters remained
unchanged. This stage of training was conducted
using DeepSpeed ZeRO-3 Offload strategy for a

--- Page 12 ---

4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(a) 4K_base/en
4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(b) 4K_base/bo
4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(c) 4K_SFT/en
4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(d) 4K_SFT/bo
4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(e) 32K_base/en
4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(f) 32K_base/bo
4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(g) 32K_SFT/en
4K
8K
12K
16K
20K
24K
28K
32K
Token Limit
0.0
11.0
22.0
33.0
44.0
56.0
67.0
78.0
89.0
100.0
Depth Percent
0
2
4
6
8
10
Score
(h) 32K_SFT/bo
Figure 1: Performance of the first stage 4K context window base and SFT models, and the second stage long context
training 32K context window base and SFT models on the English (en) and Tibetan (bo) needle-in-a-haystack task.
total of 1,000 steps.
Experimental Results. We evaluated the per-
formance of four model variants on the needle-in-
a-haystack task: the base and SFT models from
the first stage, and the base and SFT models after
long context training in the second stage. Evalua-
tions were conducted using bilingual long context
samples in English and Tibetan. As illustrated in
Figure 1, experiment results demonstrate that long
context training successfully extend the model’s
context window to 32K tokens and significantly
improve its multilingual capabilities.
G
Post Training Details
Training Data
We extensively collected open-
source instruction datasets in Chinese, English,
and Tibetan. Upon analysis, we find that most
existing Tibetan instruction datasets are generated
by translating open-source Chinese and English
instruction data using Google Translate. While
this approach is simple and convenient, it often
results in low-quality Tibetan instructions due to
the current limitations of Google’s Tibetan trans-
lation capabilities. Additionally, such translations
may introduce unintended biases. To address these
issues, we collaborated with native Tibetan speak-
ers to produce additional high-quality translation
and summarization data. These samples are orga-
nized using instruction-style templates to further
enhance the model’s instruction-following abilities
in Tibetan, particularly in the areas of translation
and summarization.
Training Setting
We used a packing strategy
to process the instruction data and adopted the
standard supervised fine-tuning loss computation
method. Specifically, the loss was calculated only
on assistant tokens, while system prompt and user
tokens were excluded. The learning rate was set to
1e-5 while the maximum gradient norm 1.0. The
model was trained for three epochs.
H
General Tibetan Benchmark
Construction
To construct general-purpose Tibetan benchmarks
for evaluating LLMs, we translated several widely
used English evaluation datasets (e.g., HellaSwag,
ARC, XCOPA, and XStoryCloze) into Tibetan.
These datasets span a range of reasoning, common-
sense, and knowledge-intensive tasks, making them
suitable for comprehensive capability assessment.
Translation
We used the Claude-Sonnet-3.7
model to perform English-to-Tibetan translation.
This model is equipped with advanced capabili-
ties for Tibetan generation, enabled by large-scale
cross-lingual pre-training.

--- Page 13 ---

Quality Review
To ensure translation quality,
we performed a structured manual review process
guided by our internal Data Review Guidelines.
The review procedure consists of three main stages:
• Semantic and Terminological Accuracy:
Reviewers compare the source and translated
texts to identify semantic deviations, includ-
ing incorrect interpretation of core concepts,
logical inconsistencies, or mistranslation of
technical terms.
• Content Compliance: All translated content
is checked for potentially harmful material,
such as violent or discriminatory language.
Additionally, reviewers filter out content that
may conflict with Tibetan cultural norms.
• Linguistic and Formatting Correctness: Re-
viewers examine grammatical structures (e.g.,
use of case particles, honorifics), fluency, and
formatting consistency, including punctuation,
line breaks, and symbol pairing.
Translations exhibiting conspicuous machine
translation artifacts or unnatural expressions shall
be rejected under the “Low-Quality Machine Trans-
lation” category to ensure that our training data
align with Tibetan linguistic conventions. During
review, annotators must maintain objective assess-
ment, comprehensively label rejection categories
for multi-issue samples with specific problem de-
scriptions, thereby constructing a high-quality Ti-
betan evaluation benchmarks.
I
Evaluation Benchmarks
We used six key benchmarks, each designed to
assess a specific capability of models within the
Tibetan language setting:
• HellaSwag-bo: Evaluates commonsense rea-
soning about event progression using multiple-
choice questions.
Accuracy is measured
against adversarial distractors to test the
model’s ability to make logically coherent pre-
dictions across diverse scenarios.
• Xcopa-bo: Focuses on causal reasoning by re-
quiring the model to choose the correct cause
or effect of a given event.
• XstoryCloze-bo: Assesses zero-shot narrative
understanding by requiring a model to choose
the most plausible story ending. It evaluates
both temporal consistency and semantic co-
herence in Tibetan.
• ARC-bo: Benchmarks factual knowledge by
evaluating middle-school level science ques-
tions that require basic recall. Accuracy re-
flects the ability of a model to retrieve simple
facts in Tibetan.
• TibetanQA: A large-scale machine reading
comprehension dataset containing 20,000 QA
pairs across 12 domains and four difficulty
levels: word matching, synonym substitu-
tion, multi-sentence reasoning, and ambigu-
ous questions. It tests fine-grained Tibetan
text understanding.
• FLORES-200 (Tibetan subset): Used to eval-
uate translation quality among Chinese, En-
glish, and Tibetan. The dataset consists of
professionally verified parallel sentences and
measures character handling, grammatical cor-
rectness, and translation fidelity.
J
Tokenizer Compression Ratio
Evaluation
In the tokenizer compression ratio evaluation, our
Tibetan model demonstrates exceptional perfor-
mance, achieving a compression ratio of 3.9644.
This far surpasses those of mainstream models de-
veloped in the industry, e.g., Qwen3-8B’s 0.7315
and Llama3-8B’s 0.4885, highlighting a signifi-
cant advantage in compression capability. A high
compression ratio indicates that when processing
Tibetan texts of the same length, a model requires
fewer tokens, which effectively reduces computa-
tional load and memory usage, thereby significantly
accelerating the inference process. This feature
not only enhances the operational efficiency of the
model but also provides strong support for the ap-
plication of Tibetan natural language processing
tasks in real-time response scenarios and resource-
constrained environments, underscoring the promi-
nent value of our method in optimizing inference
speed and reducing computational cost.

```
