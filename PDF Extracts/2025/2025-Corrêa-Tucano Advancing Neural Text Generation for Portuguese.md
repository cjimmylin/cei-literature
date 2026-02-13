---
title: "2025-Corrêa-Tucano Advancing Neural Text Generation for Portuguese - PDF Extract"
source_pdf: "2025-Corrêa-Tucano Advancing Neural Text Generation for Portuguese.pdf"
pages: 34
extracted_at: "2026-02-13T09:50:31.832431"
---

# PDF Extract: 2025-Corrêa-Tucano Advancing Neural Text Generation for Portuguese

**Source PDF:** 2025-Corrêa-Tucano Advancing Neural Text Generation for Portuguese.pdf
**Total Pages:** 34

---

## Content

```
--- Page 1 ---

Tucano: Advancing Neural Text Generation for
Portuguese
Nicholas Kluge Corrêa
Aniket Sen
Sophia Falk
Shiza Fatimah
Rhenish Friedrich Wilhelm University of Bonn
Abstract
Significant advances have been made in natural language processing in recent
years. However, our current deep learning approach to language modeling requires
substantial resources in terms of data and computation. One of the side effects of
this data-hungry paradigm is the current schism between languages, separating
those considered high-resource, where most of the development happens and re-
sources are available, and the low-resource ones, which struggle to attain the same
level of performance and autonomy. This study aims to introduce a new set of re-
sources to stimulate the future development of neural text generation in Portuguese.
In this work, we document the development of GigaVerbo, a concatenation of
deduplicated Portuguese text corpora amounting to 200 billion tokens. Via this
corpus, we trained a series of decoder-transformers named Tucano. Our models
perform equal or superior to other Portuguese and multilingual language models
of similar size in several Portuguese benchmarks. The evaluation of our models
also reveals that model performance on many currently available benchmarks used
by the Portuguese NLP community has little to no correlation with the scaling of
token ingestion during training, highlighting the limitations of such evaluations
when it comes to the assessment of Portuguese generative language models. All
derivatives of our study are openly released on GitHub1 and Hugging Face2.
1
github.com/Nkluge-correa/Tucano
2
huggingface.co/TucanoBR
Preprint, work in progress.
arXiv:2411.07854v1  [cs.CL]  12 Nov 2024

--- Page 2 ---

1
Introduction
Over almost a decade, the deep learning paradigm has been the de facto mode of operation for many
of the sub-fields involved in artificial intelligence research [91, 71]. Natural Language Processing
(NLP) is a canonical depiction of the success story of deep learning [112, 46, 118], where neural
network approaches to machine learning have become the engine that powers many aspects of our
current age of intelligent automation, with breakthroughs like word embeddings [107, 106] and the
transformer neural architecture [164] being at the heart of this revolution.
Another aspect of this developmental movement is using the self-supervised learning approach as
an intermediate step to many language modeling tasks [68]. In essence, self-supervised learning is
a training methodology for machine learning systems, where we leverage the vastness of available
unlabeled data at our disposition to create pretraining tasks where labeling can happen on the fly.
This results in systems with useful and downstream-applicable representations tied to the domain
they were trained on [75, 108, 68]. This training approach has been responsible for some of the early
breakthroughs of the field [13, 106, 157, 11], which have now morphed into our standard training
recipe for foundation models [17].
Nonetheless, while the statement "leverage the vastness of available unlabeled data at our disposition
to create pretraining tasks" can be true for languages like English or Chinese, where datasets can
reach the 1013 tokens mark [150, 178, 27, 125], and models are trained way past what scaling laws
prescribe as compute-optimal [181, 122, 176], the same cannot be said about the crushing majority
of more than 7000 languages spoken around the world today [136, 101, 33]. Hence, the prospect
of training language models at the scale required to match what is done in such high-resource
languages (even when compared to the state-of-the-art from 5 years ago)3 is a far-fetched goal for
most low-resource languages [60, 2, 40, 111, 38].
To overcome this linguistic shortcoming, one of the approaches found in the literature is the develop-
ment of multilingual models and datasets [149, 183, 10, 153]. In these models, the self-supervised
pretraining stage is conducted with various languages. Models like mBERT [48], mT5 [177], XLM-
RoBERTa [35], mGPT [146], XGLM [98], BLOOM [174], PolyLM [171], Aya [183], and Llama 3
[50] are examples of this approach. On the other hand, the development of monolingual language
models has also been explored and, at many times, shown to be a more successful approach to the
multilingual one, like in the case of Finish [166], French [105], Catalan [8], Chinese [156], and
Portuguese [152, 136, 38]. Besides, as already pointed out by other works [38], if based on raw
pretraining instead of a fine-tuning approach, the monolingual approach can help developers escape
the computational (i.e., models that are too expensive to run) and legal constraints (i.e., models that
are restricted in terms of their licensing) of working with an already established foundation.
However, advances in developing low-resource monolingual language models, such as those for
Portuguese, remain limited, small in scale, undocumented, lacking standardization, and often reliant
on repurposing models trained behind closed doors,4 as will be discussed in the next section. These
deficits also make it challenging to compare language models and evaluation benchmarks. At the
same time, the effectiveness of the currently available benchmarks for Portuguese is also untested.
In this work, we aim to address these challenges and build on existing studies to improve the status
of generative language modeling research and development for Portuguese. In summary, our study
offers the following advancements to the Portuguese NLP community:
1. The concatenation of a larger and more high-quality dataset for Portuguese language model-
ing (GigaVerbo).
2. The development of learned filters and datasets to improve text pre-processing for Por-
tuguese.
3. Pushing self-supervised pretraining beyond the 500B tokens mark for Portuguese monolin-
gual models.
4. The development of new, low-resource, efficient, and effective open-source foundation
models for Portuguese (Tucano).
3Models like GPT-3 (2020) [19] were trained only on 300B tokens, which is still something not reproduced
in a monolingual setting for most low-resource languages.
4This is particularly true for the European and Brazilian variants, with other variants (e.g., Angolan Por-
tuguese) even less represented or entirely absent.
2

--- Page 3 ---

5. A critical assessment and comparison of currently available benchmarks for Portuguese
language models.
In Section 2, we review the current status of Portuguese Large Language Model (LLM) research and
development, documenting the trends and deficits in the field. Section 3 describes the pretraining
corpus used in this work. Section 4 and 5 contain the definition of our chosen tokenizer and the
parameter space of different models we trained. In Section 6, we discuss the training and evaluation
of our models. We also employ a simple alignment strategy to our more capable models, as will
be discussed in Section 7. In Section 8, we present the results of our evaluation harness. Finally,
Sections 9 and 10 provide an outlook for future studies and conclusion of our work.
2
An Anthology of Portuguese LLM Development
A historical timeline of Portuguese LLM research and development can help to understand how
our work should be contextualized. This landscape consists of many pre-trained and fine-tuned
transformer networks. However, before doing so, we would like to differentiate between two terms
(fine-tuning and pretraining) that are used loosely and interchangeably in the literature, making it
sometimes difficult to distinguish between them.
First, we will use the definition of fine-tuning as "the process of updating the weights of a pre-trained
model on new data" [71, 129]. Hence, all models that adopt a training methodology in which already
trained weights are repurposed and updated are byproducts of a fine-tuning approach, done at full or
low ranks [80], with or without adaptations (e.g., changing the tokenizer vocabulary and re-initializing
the embedding matrix and language modeling head). Secondly, pretraining can be defined as "the act
of training a neural network initialized with random weights". The distinction between pretraining
and training is merely contextual or terminological, given that a foundation model is usually trained
to be later "trained again" (i.e., fine-tuned) for a more specific task, hence the "pre", as "before we
train on the tasks and applications we care about". Although intuitive, this distinction is sometimes
presented in an unclear fashion, even though the difference between both approaches is evident and
can severely affect the performance models can achieve.5
In summary, distinguishing between these two developmental approaches is essential to interpret
evaluation results and model capabilities, as we will explore in upcoming sections. Now, with these
definitions in mind, let us review some of the developments achieved in recent years (Fig. 1):
• GPorTuguese-2 (July 18, 2020) [72]: The first publicly available large language model
tailored for Brazilian Portuguese. GPorTuguese-2 is a byproduct of fine-tuning OpenAI’s
smallest version of GPT-2 [130] on the Portuguese portion of Wikipedia [173]. This
model also has adaptations, like its own byte-pair encoding (BPE) tokenizer with a custom
vocabulary that repurposes the joint embeddings from the original English vocabulary.
GPorTuguese-2 was fine-tuned on ≈1.2 GB of text, and it is available under an MIT License.
• PTT5 (August 20, 2020) [26]: An encoder-decoder model developed as a foundation
for Text-to-Text tasks in Brazilian Portuguese. PTT5 is an adapted version of another
foundation model (Google’s multilingual T5 [133]), having a custom vocabulary and
embeddings that were reinitialized and trained from scratch. PTT5 model was trained on the
BrWaC corpus [168] (≈2.68 billion tokens) and is available under an MIT License.
• BERTimbau (October 20, 2020) [152]: A fine-tuning version of the base and large
versions of mBERT and English BERT [48], respectively. BERTimbau has a custom
vocabulary, embeddings, and attention heads that were reinitialized and trained from scratch.
5For example, the fine-tuning of a foundation like Llama 2 [161], even on a small dataset of monolingual
text, usually results in a model that, besides presenting performant language modeling skills in the language
chosen, inherits from the pervasive training the original foundation was put through. However, this approach
can make results hard to trace depending on the context in which we find ourselves. For example, how much
of performance x can be attributed to 1013 tokens of pretraining compared to the 109 tokens of fine-tuning in
benchmark y? Such a question becomes even harder to answer when models are based on foundations developed
in a private setting.
3

--- Page 4 ---

Figure 1: This timeline illustrates several Portuguese language model releases from 2020 to October 2024. The
models are color-coded to indicate their respective Portuguese language variants, e.g., green for South America
and blue for Europe. The timeline also distinguishes pre-trained models from fine-tuned derivatives of other
foundations. We limited the models displayed in this timeline to those we could find tied to publication reports,
unpublished manuscripts, peer-reviewed papers, and popular repositories.
Both versions of BERTimbau were trained on BrWaC [168], and are available under an MIT
License.
• BioBERTpt (November 19, 2020) [139]:
A fine-tuned version of mBERT [48].
BioBERTpt was created to support named-entity recognition (NER) in clinical and
biomedical applications, being trained on a corpus of 44.1 M tokens of clinical narratives
and biomedical-scientific papers in Brazilian Portuguese. While mBERT is licensed under
an MIT License, BioBERTpt does not specify any licensing regime. However, the model is
openly accessible via the Hugging Face platform.
• BERTaú (January 28, 2021) [57]:
A pre-trained BERT-based LLM for Brazilian
Portuguese. BERTaú was pre-trained using customer-service conversations from a Brazilian
financial services company (Itaú), with 5GB of text, following a similar training protocol to
the one described in the original BERT paper [48]. As far as we could investigate, BERTaú
is not open to the public, being proprietary software from Itaú.
• GPT2-Bio-Pt (June 1, 2021) [143]: A fine-tuned version of the GPorTuguese-2 [72],
trained on 48M tokens of clinical and biomedical literature. While GPorTuguese-2 is
licensed under an MIT License, GPT2-Bio-Pt does not specify any licensing regime.
However, the model is accessible via the Hugging Face platform.
• BERTikal (October 5, 2021) [128]: A BERT model tailored for the Brazilian Portuguese
legal domain. BERTikal is a fine-tuned version of BERTimbau-base [152]. For training, the
authors used 2.6 GB of text composed of legal documents from several Brazilian courts
dated from 2019 to 2020. BERTikal is currently available under an MIT License.
• PetroBERT (March 16, 2022) [137]: A BERT-based model adapted to the oil and gas
exploration domain in Portuguese. PetroBERT has two versions, each fine-tuned over a
different foundation: mBERT [48] and BERTimbau [152]. No model is currently available
4

--- Page 5 ---

for public use.
• Sabiá (April 16, 2023) [127]: A series of fine-tuned models that used GPT-J [169] and
Llama [160] as a foundation. The outcomes of this fine-tuning process are Sabiá-7b, 65B
(both derivatives of Llama), and Sabiá-J (using GPT-J as a base). The Sabiá series was
trained on ≈7.8 billion tokens from a filtered portion of the ClueWeb 2022 dataset [120].
Sabiá-65B and Sabiá-J are unavailable to the public, while Sabiá-7B is available under the
Llama 2 license.
• Albertina (May 11, 2023) [136]: A family of encoder-only transformers that use DeBERTa
[77] as a foundation. Albertina models come for Brazilian and European Portuguese,
having been trained on over 2.2B tokens of text. Currently, the Albertina series scales
from 100 million to 1.5 billion parameters, and all models are available under an MIT license.
• JurisBERT (July 30, 2023) [165]: A series of BERT-based models developed for the
Brazilian legal domain. In this series, we find models either pre-trained from scratch or
adapted from BERTimbau-base [152]. We also find adapted versions from these models that
were later fine-tuned to work as Sentence Transformers [135]. Even though no license is
tied to these models, all are available for use in the Hugging Face platform.
• Cabrita (August 23, 2023) [89]: A fine-tuned version of OpenLLaMA 3B [69], with
an adapted tokenizer and extended embeddings. Cabrita was trained on 7 billion tokens
extracted from the Portuguese subset of the mC4 dataset [177]. Cabrita is available under an
Apache 2.0 license.
• BERTabaporu (September 4, 2023) [39]: Two BERT models, base and large, pre-trained
on Brazilian Portuguese Twitter data. These models were trained on 2.9B tokens, following
a similar training recipe as the original BERT paper [48]. BERTabaporu is available under
an MIT license.
• DeBERTinha (September 28, 2023) [23]: An adapted version of DeBERTaV3 [76],
fine-tuned to be performant in Brazilian Portuguese. DeBERTinha has a custom vocabulary
and embeddings trained from scratch while repurposing the other weights from the original
DeBERTaV3. For training, the authors used a combination of the BrWaC [168] and Carolina
[58] datasets, which amounted to 33GB of text (≈3.4 billion tokens). DeBERTinha is
available under an MIT license.
• LegalBert-pt (October 12, 2023) [148]: Both a pre-trained BERT and a fine-tuned
BERTimbau [152]. The training dataset contained 1.5 million samples of legal texts (12
million sentences) and was used to pre-train/fine-tune both versions of LegalBert-pt. Both
versions of LegalBert-pt are available under the OpenRAIL license.
• Bode (January 5, 2024) [66]: Both a low-rank adaptation and full fine-tuned version of
Llama 2 [161]. These models were trained on a translated version of the Alpaca dataset
[159] (i.e., 52,000 instruction-following demonstrations generated by text-davinci-003).
Bode is available in two sizes, 7B and 13B, under the Llama 2 license.6
• TeenyTinyLlama (January 30, 2024) [38]: A pair of language models pre-trained in
Brazilian Portuguese. TeenyTinyLlama (TTL) models are based on the Llama architecture
[161], downsized to a 160 and 460 million parameter version. These were trained on a
concatenation of publicly available Portuguese datasets called Portuguese-Corpus Instruct
(6.2B tokens). Models, datasets, and source code for training/evaluation are available under
an Apache 2.0 license.
6Similar models (e.g., Caramelo [21] and Harpia [22]) can also be found using Falcon 7B as a foundation [4].
5

--- Page 6 ---

• Glória (February 20, 2024) [101]: A pair of language models pre-trained in European
Portuguese. Glória models are based on the GPTNeo architecture [16], scaled to 1.3B and
2.7B parameters. Its training dataset comprises a concatenation of European Portuguese
datasets amounting to 35.5 billion tokens. Glória’s usage is restricted to research-only
purposes, subject to the ClueWeb22 Dataset license.
• Gervásio (February 29, 2024) [141]: A fined-tuned version of Llama 2 7B [161]. It comes
in a European and Brazilian variant, each trained on distinct datasets designed to induce
instruction-following behavior. Even though Gervásio is a derivative of Llama 2,7 Gervásio
is currently available under an MIT license.
• RoBERTaLexPT (March 12, 2024) [64]: A pair of encoder-only LLM based on the
RoBERTa-base implementation [100], tailored for general Brazilian Portuguese language
modeling and applications in the legal domain. While RoBERTaCrawlPT was pre-trained
from scratch on the CrawlPT corpora (i.e., a deduplicated concatenation of BrWaC [168],
Common Crawl [172, 34], and Oscar [117, 116, 1]), RoBERTaLexPT was pre-trained
from scratch from a combination of CrawlPT and LegalPT (i.e., a concatenation of six
different Brazilian Portuguese legal text corpora [115, 136, 151, 18]). RoBERTaCrawlPT
and RoBERTaLexPT are available under a Creative Commons license (CC BY 4.0).
• Sabiá-2 (March 14, 2024) [5]: Not much information is known about Sabiá-2, and its report
only brings evaluation scores of internally held benchmarking on two models of unknown
sizes, referred to by the authors as "small" and "medium". Sabiá-2 is only available to the
public via a commercial API.
• Juru (March 26, 2024) [84]:
A fine-tuned version of Sabiá-2 small.
Juru was
trained on 5.88 billion tokens from academic studies and other high-quality sources tied to
the Brazilian legal domain. Juru and the dataset used to train it are not available to the public.
• PTT5-v2 (June 16, 2024) [126]: Similar to the first iteration of PTT5, PTT5-v2 is a series
of fine-tuned models, up to 3 billion parameters, based on Google’s multilingual T5 [133].
PTT5-v2 was trained on approximately 524 GB of uncompressed text for 1.7 million
optimization steps (115 billion tokens), following a training regime similar to the original
T5 paper. Even though no license is tied to these models, all are available for use in the
Hugging Face platform.
• Sabiá-3 (October 15, 2024): Not much information is known about Sabiá-3, and its report
only brings evaluation scores of internally held benchmarking on one model of unknown
size. Sabiá-3 is only available to the public via a commercial API.8
Reviewing these past works reveals a few crucial insights about Portuguese NLP research’s current
state and direction. Firstly, language adaptation, i.e., repurposing the language modeling capabilities
of a model for another language, is a popular approach, especially when the foundation used is
already performant and multilingual. The great majority of the work mentioned in the above list
presents research revolving around fine-tuning and adaptation of already pre-trained models rather
than developing native Portuguese foundations [152, 136, 89, 5].
Moreover, the fine-tuning over pretraining choice can be attributed to factors characteristic of low-
resource languages (e.g., not enough tokens) and conditions of low-resource development (e.g., not
enough computing). For example, until 2024, almost all studies were limited to datasets with less
than 10 billion tokens, with most fine-tuning models using much less than this. Although justifiable in
terms of model size and scaling laws [78], this makes the training of larger models infeasible unless
we promote a severe repetition of our dataset [89], which, however, does not contribute to improved
model performance [111]. Hence, most of the community relies heavily on leveraging the capabilities
7Hence, supposedly should be restricted by the Llama 2 Community License Agreement.
8The "Sabiá-3 Technical Report" is available via the maritaca.ai website.
6

--- Page 7 ---

of established models, which have been extensively pre-trained on large and diverse datasets in other
languages.
Another interesting point is that while encoder-only models like BERT have dominated the landscape
for some time [152, 128, 137, 136, 39, 148, 23, 64], there has been a recent shift towards training
decoder-only models [127, 38, 101]. However, a significant challenge with these models is the need
for more standardization in evaluation protocols. Each study tends to develop its own benchmarks and
evaluation metrics, which complicates direct comparisons and makes it difficult to ascertain the actual
performance of these models. Furthermore, many of the current Portuguese benchmarks available
for the evaluations of few-shot capabilities of generative models are either repurposed datasets
initially created for downstream development or assessment of BERT-style models [134, 163, 20] or
translated versions of English benchmarks [88], which raises questions regarding their effectiveness
in evaluating the capabilities of generative language models. Meanwhile, model comparisons are still
very limited among Portuguese language models, given that only a few available models allow cheap
and accessible benchmarking for cross-study comparisons.
Regarding dataset creation, there is a notable trend towards concatenating and deduplicating various
text corpora to form more extensive and scalable datasets. In 2024, we see several studies imple-
menting this approach, giving birth to some of the first large datasets (> 10B tokens) for Portuguese
language modeling [101, 64]. However, data filtering and preprocessing methods remain primarily
heuristic (e.g., hash-similarity-based deduplication, HTML removal, and mojibake correction) in
most studies [101, 64]. At the same time, works that pioneer the filtering and creation of high-quality
text datasets do not make these available for the community [84, 126]. Meanwhile, we currently do
not see the documented use of more sophisticated approaches (e.g., "LLM-as-a-Judge" or learned
filters [73]) to ensure data quality in the creation of these corpora.
It is also worth noting that several recent works have demonstrated the advantages of pretraining
models from scratch over fine-tuning/adapting existing ones [39, 38, 101, 64], especially in circum-
stances where training data is sufficient. Nonetheless, the top-performing models in the literature
often rely on fine-tuning foundations whose pretraining data is not disclosed [127, 5]. This opacity
raises questions about the factors driving their performance and the limits of how far we can push
Portuguese pretraining natively. This brings us to another crucial insight: a significant need for more
openness regarding datasets and code implementations across many works. Without it, machine
learning research becomes vulnerable to several criticisms, aggravating its current reproducibility
crisis [85], while also fueling the "deep learning is alchemy" critique [83].
Finally, another idea worth expressing regarding the pretraining versus fine-tuning choice is that, while
building on top of ready-made foundations has its merits (e.g., simplifying the LLM development
process to a transfer learning/fine-tuning problem), it is also responsible for masking or diverging
attention from severe issues many NLP researchers face. For example, if we agree that LLMs
are valuable tools, should communities of low-resource languages be forever bound to "wait and
recycle" the outputs of research often done behind closed doors and with no prospect of accurate
reproducibility? Suppose "yes" is the answer. In that case, there is an argument to be made that many
communities involved in NLP research find themselves bound in a form of technological colonialism.9
On the contrary, if technological sovereignty should be sought as something that "ought", research
focused on creating foundations instead of repurposing them should be more stimulated.
In this work, we seek to aid in improving some of these critical points and participate in the open
development of some trends seen thus far. In the following sections, we present novel tools, datasets,
and models for the Portuguese NLP community to expand upon. Although our efforts are mainly
concerned with Brazilian Portuguese, we believe they can be repurposed, built upon, and adapted to
other variants of Portuguese. In the following sections, we document the creation of our datasets,
filtering methods, models, pretraining protocol, and evaluation procedures.
3
Pretraining Data
9Technological colonialism refers to the dominance of a small number of entities, typically large corporations
or specific geographic regions, in controlling and shaping the development, deployment, and norms of advanced
technological systems [9].
7

--- Page 8 ---

3.1
Concatenating GigaVerbo
Datasets like the ones created by Lopes et al. [101] (35.5B tokens) and Garcia et al. [64] (≈90B
tokens) are filtered concatenations of several datasets used in previous studies or made accessible
by crawling initiatives like Common Crawl and Oscar, much like the Pile [61], and MassiveText
[131], which are also collections of large text datasets from multiple sources, but with a focus on
English. We applied the same methodology to create our dataset’s initial version, concatenating
several portions of openly available datasets for Portuguese and deduplicating their summation with
an exact hash deduplication filter [110].
Our pretraining corpus, which we will refer to as GigaVerbo, contains over 145 million documents,
amounting to 780 GB of text. More details of its composition can be found in Table 1.
3.2
Filtering GigaVerbo
As recent studies have suggested, several gains in performance can be achieved by enhancing dataset
quality instead of merely scaling data ingestion and model size [113, 73, 96, 125, 170, 94, 158, 50].
However, what defines a text as "high-quality" is a nontrivial question. While heuristic-based filters
can help us parse samples that are, for example, too short or ill-formatted, it is hard to differentiate
high-quality text (e.g., articles, poems, tutorials) from plain text scrapped from the web (e.g., product
information scrapped from e-commerce platforms) using only heuristic-based filters. Given that
human annotation can be tedious and expensive [52], and current learned filters are either ill-suited
for Portuguese or too expansive to run at scale, we decided to employ the same strategy used by
Gunasekar et al. [73] and train our own filtering system.
For this, we randomly selected 110,000 samples from 9 Subsets of GigaVerbo (i.e., specifically
those not synthetic).10 With these samples, we created a text-quality dataset using GPT-4o as a
judge. Similar to the study of Gunasekar et al., [73], we prompted GPT-4o to score every text sample
regarding its quality to create a high-quality text dataset for the Portuguese language (Fig. 2).11
As a first attempt, we sought to emulate Gunasekar et al. [73] by converting the text samples of our
classification dataset into embedding representations via a sentence-BERT [135]. After evaluating
several available multilingual sBERTs, we selected LaBSE (Language-agnostic BERT Sentence
Embedding) [56], which generates 768-dimensional embedding vectors. Then, we trained a shallow
classifier based on XgBoost [28]. To convert Real numbered scores into labels, we binarized our
data by defining as "high" all samples with a score >= 0.8 and "low" all those with a score <= 0.6.
However, we were not satisfied with the results of this initial approach, and we hypothesize that
the embedding representations of LaBSE were not performant enough for Portuguese. Hence, we
decided to use BERTimbau [152] as the foundation for a text classification model. Results for both
approaches can be found in Table 2.
In the end, we chose to use our fine-tuned version of BERTimbau-base to filter GigaVerbo, given that
it had achieved good performance and was faster than both our XGBoost classifiers and BERTimbau-
large. After parsing GigaVerbo with our learned filter, from 145 million samples, our classifier
assigned low-quality to approximately 50 million samples, leaving 65% of GigaVerbo with a high-
quality ranking according to our filter. However, for this study, we adopted a filtering approach
where we only removed the low-quality samples if the confidence of our classifier was above 95%
for the low-quality class. We expect that this would minimize token waste due to low-confidence
false negatives. This approach leaves us with ≈70% of GigaVerbo to work with. The available
GigaVerbo version on Hugging Face has the class and confidence score assigned by our filter for each
text sample, allowing other users to replicate our training mixture or adapt the filtering process to
their liking.
10These Subsets are monoHPLT-PT, CrawlPT, Wikipedia, CulturaX, Common Crawl, ROOTS, XL-Sum,
Corpus Carolina, and LegalPT.
11Example system prompt (translated): "You are required to act as a text classifier. Rate the quality of the text
provided with a score between 0.0 and 1.0, considering how reasonable, valuable, and informative this text is
for training a language model in Portuguese. Return the score to two decimal places without further comments".
8

--- Page 9 ---

Subset
Nº of Samples
%
Description
monoHPLT-PT
58,244,012
40.09%
The clean and deduplicated Portuguese portion
of the High-Performance Language Technologies
resources dataset [44].
CrawlPT
43,846,974
30.17%
A deduplicated Portuguese corpus extracted from
various web pages, concatenated from CC-100,
Oscar, and BrWaC [64, 35, 117, 116, 1, 168].
Multilingual-C4
16,092,571
11.07%
The Brazilian Portuguese cleaned portion of the
m-C4 dataset [133].
Common Crawl
12,470,998
8.58%
A clean and deduplicated snapshot of the Common
Crawl dataset (CC-MAIN-2023-23) [172, 34].
BlogSet-BR
4,321,181
2.97%
A collection of blog posts written in Brazilian Por-
tuguese [140].
Instruct-PTBR
2,962,856
2.04%
A mix of multiple instruction datasets for various
tasks, machine-translated from English to Brazil-
ian Portuguese [25].
Corpus Carolina
2,075,395
1.43%
An open corpus with varied typology in contempo-
rary Brazilian Portuguese [58].
UltrachatBR
1,255,091
0.86%
A Portuguese version (machine-translated) of the
Ultrachat dataset [65].
Wikipedia
1,101,475
0.76%
Cleaned Portuguese articles built from the
Wikipedia dumps [173].
CulturaX
999,994
0.69%
The Portuguese portion of CulturaX, a multilingual
dataset with 167 languages [114].
LegalPT
925,522
0.64%
A concatenation of publicly available legal data
in Portuguese, including legislation, jurisprudence,
and legal articles [151, 18, 115, 136, 64].
Gpt4All
808,803
0.56%
A Portuguese (machine-translated) version of the
Gpt4All dataset [7].
Bactrian-X
66,994
< 0.1%
The Portuguese portion of Bactrian-X, a collection
of instruction-response pairs in 52 languages [93].
XL-Sum
64,577
< 0.1%
A Portuguese (machine-translated) version of XL-
Sum, a diverse dataset for abstractive summariza-
tion [74].
Dolly 15K
28,401
< 0.1%
A Portuguese (machine-translated) version of
Dolly 15K, an open-source dataset of instruction-
following records generated by human annotators
[36].
CosmosQA
25,260
< 0.1%
A Portuguese (machine-translated) version of the
CosmosQA dataset for commonsense-based read-
ing comprehension [81].
ROOTS
10,740
< 0.1%
The Portuguese portion of the ROOTS corpus, a
dataset spanning 59 languages [90].
Table 1: Description of the different datasets comprising GigaVerbo. GigaVerbo is currently hosted
on Hugging Face. More information can be found in its dataset card.
3.3
Scaling GigaVerbo
According to the work of Muennighoff et al. [111], training with up to 4 epochs of repeated data
in data-constrained scenarios yields minor changes to loss compared to unique data, while further
9

--- Page 10 ---

Figure 2: This graph shows the distribution of scores for 4 Subsets of GigaVerbo. We determined that the text
would have a "high" quality if the GPT-4o scores were >= 0.8 and "low" when <= 0.6, thus keeping our dataset
with a more balanced proportion of labels for our classifiers. Above, we see that datasets like monoHPLT and
Corpus Carolina have some of the lowest-quality samples. Also, given that GPT-4o is extremely sensitive to
toxic and harmful content, samples containing toxic, dangerous, or NSFW content end up being scored very low
(< 0.1), given as a way to account for the toxicity in our dataset. Analyzing samples from the Wikipedia portion
scored by GPT-4o, we found that the model consistently gives low scores (< 0.5) to ill-formatted, incomplete, or
excessively short documents (< 20 words). This classification/regression dataset is available on Hugging Face.
Class
Precision
Recall
F1-score
LaBSE + XGBoost
Low
0.89
0.81
0.85
High
0.92
0.96
0.94
BERTimbau
Low
0.99
0.97
0.98
High
0.99
0.99
0.99
Table 2: The table above shows the evaluation scores for both our LaBSE + XGBoost and
BERTimbau-based classifiers. These scores were obtained by evaluating both models on a test
set of 11,000 samples. For the XGBoost, we used a learning rate of 0.1, a maximum tree depth of
10, and 100 estimators. For fine-tuning BERTimbau, we used a learning rate of 4 × 10−5, a weight
decay of 0.01 for regularization, and a batch size of 128 for 3 epochs on our entire dataset. We also
experimented with training a LaBSE + XGBoost regression algorithm, which achieved a root mean
squared error of 0.16 on our evaluation, and the fine-tuning of BERTimbau-large, which achieved
very similar results to its base version. All these models are available on Hugging Face.
repetition yields less performance, eventually (for > 10 epochs) decaying to zero. Hence, to enlarge
our pretraining corpus, when training the smaller versions of our series (i.e., 160m, 630m, and 1b1),
10

--- Page 11 ---

we repeated specific GigaVerbo subsets based on the overall quality assigned by our learned filter.
The contents of one epoch of GigaVerbo are shown in Table 3. To train our largest model (2b4), we
repeated the entire filtered dataset for four epochs.
Subset
Original Size
Filtered Size
%
Repeat Factor
Token Count
monoHPLT-PT
58,244,012
37,291,607
64.03%
1
84,708,988,928
CrawlPT
43,846,974
29,427,715
67.11%
1
14,023,256,064
Multilingual-C4
16,092,571
13,849,412
87.10%
2
8,083,937,280
Common Crawl
12,470,998
10,527,584
84.42%
2
14,421,852,160
BlogSet-BR
4,321,181
2,411,590
55.81%
1
1,561,569,280
Instruct-PTBR
2,962,856
2,570,829
86.77%
4
1,141,768,192
Corpus Carolina
2,075,395
1,170,905
56.42%
1
1,018,951,680
UltrachatBR
1,255,091
1,2477,14
99.41%
4
1,652,916,224
Wikipedia
1,101,475
921,137
83.63%
4
551,403,520
CulturaX
999,994
883,550
88.36%
4
565,768,192
LegalPT
925,522
891,891
97.62%
4
1,313,269,760
Gpt4All
808,803
725,195
89.66%
4
381,650,944
Bactrian-X
66,994
55,685
83.012%
4
9,517,056
XL-SUM
64,577
64,467
99.83%
4
52,072,448
Dolly 15K
28,401
21,016
74.00%
2
3,698,688
CosmosQA
25,260
14,702
58.20%
1
2,074,624
ROOTS
10,740
5,448
50.72%
1
11,456,512
Total
145,300,844
102,080,447
70.25%
129 Billion
Table 3: In the table above, we present the number of documents present in every subset of GigaVerbo
(i.e., its original size), its size after filtering, and the repetition factor used for creating the data mixture
used to train the 160m, 630m, and 1b1 versions of the Tucano series, which generates a dataset
with 169 billion tokens. The token count column provides raw values, i.e., the token count without
accounting for the repetition factor of the filtered portion of GigaVerbo (129 billion tokens). Without
filtering, GigaVerbo contains ≈200 billion tokens. To train our biggest model (Tucano-2b4), we
repeated the entire filtered dataset for four epochs, amounting to ≈515 billion tokens.
4
Tokenization
As already pointed out by previous studies [57, 41, 89, 38], the success of a tokenization scheme
in compressing a given language has a subsequent impact on the efficiency of the language model
in question. While the precise effect on the overall language modeling capability remains unclear
[142], the tokenization scheme certainly plays a significant role in this process [70]. In terms of
compression, one can significantly improve tokenizer efficiency (i.e., how many tokens are required
to encode a given piece of text) when using a vocabulary custom-made for a given domain [89, 38].
This allows us to better utilize limited resources, like context, when working with transformer-based
models.
To better assess and compare tokenizer efficiency across our revised anthology of Portuguese language
models, we replicated the test evaluation performed by both Larcher et al. [89] and Corrêa et al. [38]
on several available tokenizers tied to Portuguese LLMs. For this, we used a text sample containing
11

--- Page 12 ---

Figure 3: The figure above lets us understand specific relationships between vocabulary size and the respective
tokenizer’s capabilities regarding compression. For example, models that use the Llama 2 tokenizer (e.g., Sabiá),
primarily focused on English, do not encode Portuguese very efficiently. On a similar note, Sabiá-2 has the
worst performance across all tokenizers, even though it has double the vocab size of its predecessor. Meanwhile,
multilingual models, like mBERT, PolyLM, Llama 3, mT5, and mGPT, improve their compression efficiency
by having significantly enlarged vocabularies, with Bloom, XGLM, and XLM being close to the top of this
comparison, all using massive multilingual vocabularies with > 250,000 tokens. As a middle ground between
efficiency and resource consumption (i.e., larger vocabularies imply larger embedding matrices, which then imply
more computational requirements for inference or training), we have tokenizers with vocabularies tailored for
the Portuguese domain (e.g., BERTabaporu, TeenyTinyLlama, BERTimbau). In summary, while multilingual (or
larger) vocabularies generally offer improved compression, small, domain-specific tokenizers balance efficiency
and computational resource consumption. The code for replicating this test is available in GitHub.
≈14,000 words from Portuguese poems extracted from authors like Fernando Pessoa and Ronald de
Carvalho, among others. Our results are displayed in Fig. 3.
According to our experiments, the tokenizer trained by Corrêa et al. [38] presents both an efficient
compression capability and a slim vocabulary size for improved efficiency during input and output
embedding matrices computations. The TeenyTinyLlama tokenizer (from now on referred to as the
Tucano tokenizer) is a Sentencepiece tokenizer [86], which implements both sub-word and unigram
tokenization. Finally, we utilized this tokenizer to encode our pretraining dataset, separating each
document with an end-of-text token (</s>).
5
Architecture
Like many other studies [127, 89, 38, 66, 5], we used a decoder-only Transformer based on the
Llama architecture [160, 161, 50] as the basis for our models. In terms of code implementation,
we used the implementation provided by Hugging Face so that our models can be easily shared
and used by the community. Like the standard Llama architecture, our models use both root mean
square layer normalization [180] and RoPE embeddings [155], with Silu activation’s [53] instead of
the SwiGLU [145] described in the original Llama papers. All models were trained using a causal
language modeling objective and cross-entropy as its loss. The dimensions of our models, which we
named Tucano, are documented in Table 4.
12

--- Page 13 ---

nparam
nlayers
dmodel
dmlp
nheads
nKV −heads
dhead
clength
162,417,408
12
768
3,072
12
12
64
2048
630,253,568
14
2,048
4,096
16
4
128
2048
1,100,048,384
22
2,048
5,632
32
4
64
2048
2,444,618,240
24
2,560
10,240
16
4
160
4096
Table 4: Each model is based on a decoder-only Llama architecture, with a vocabulary size of 32,000.
Tucano-160m, 630m, and 1b1 were trained with a context window of 2048 tokens, while the largest
model (2b4) was trained with sequences of length 4096. All models were trained using a causal
language modeling objective and cross-entropy loss. The parameters were explicitly tuned to fit
these models (and respective optimizers and batches) on A100-SXM4-80GB GPUs. Unlike previous
studies [38, 49], we trained all models beyond what the Chinchilla scaling laws prescribed [78].
Group-query attention [3], with 4 key-value heads per decoder block, was used to reduce attention
computations’ memory footprint, helping us to maximize token throughput during training without
significantly impacting model convergence when training Tucano-630m, 1b1, and 2b4.
6
Training and Evaluation
6.1
Hyperparameters and Performance
Our training code base was primarily built with a PyTorch-based deep learning stack [123]. As a
training framework, given that our model sizes could all fit inside the memory of our GPUs, we
utilized a simple Distributed Data-Parallel approach [95]. For support, we used specific libraries
tied to the Hugging Face ecosystem, like Tokenizers [82] for fast tokenization and Datasets [92]
for handling our pretraining corpus. We also used FlashAttention [43, 42] for optimized IO-aware
attention computation and the Liger Triton kernels [79] to reduce memory footprint and improve
token throughput during training. We used 8 NVIDIA A100-SXM4-80GB GPUs to train both smaller
versions of Tucano (160m and 630m) and 16 of these for our two largest models (1b1 and 2b4). Lastly,
we utilized CodeCarbon [32] to track the resource consumption of our experiments and training runs.
To assess the efficiency of our deep learning stack, we utilized the method proposed by Chowdhery et
al. [30] to estimate the model FLOPs utilization (MFU) we were able to achieve during our training
runs, which can be understood as the ratio of the observed throughput (actual performance) to the
theoretical maximum throughput that a given hardware offers. Regarding speed comparison, our
code implementation is on par with other documented developments in the literature. For example,
for our Tucano-1b1, we were able to achieve a training throughput of 24,180 tokens per second per
A100-SXM4-80GB, which is similar to that achieved in the development of TinyLlama [181], and
superior to those documented in the development of the Pythia suite [15]. In Table 5, we document
the hyper-settings used to train our models and the efficiency we achieved.
6.2
Batch Size and Gradient Accumulation
According to the literature, transformer-based networks can benefit from larger batch sizes during
training [144]. By larger, we mean up to millions of tokens per batch. For example, in the first
iteration of GPT-3, the series was trained on batches from 524K to 3.2 million tokens [19], with batch
sizes increasing with model size. Meanwhile, all Llama 2 models were trained with 4 million tokens
per batch [161], while Llama 3 405B used a massive amount of 16 million tokens per batch [50]. In
Biderman et al. [15] development of the Pythia suite, all models were trained with a batch size of 2
million. Currently, for language model training at the sub 2 billion parameters mark, most studies
maintain a batch size between 1 to 2 million tokens per batch [73, 181, 101, 158].
Given that achieving this batch size range requires that our hardware have a significant amount of
available memory for batch processing, a common approach documented in the literature is using
gradient accumulation strategies when limited by available VRAM. In essence, gradient accumulation
is used during training to simulate larger batch sizes than our hardware’s memory typically allows.
In this approach, instead of updating the model parameters after each mini-batch, the gradients are
13

--- Page 14 ---

160m
630m
1b1
2b4
Total Optimization Steps
320K
400K
480K
1.9M
Batch Size (in tokens)
524K
524K
524K
262K
Epochs
1
1.25
1.5
4
Total Tokens
169B
211B
250B
515B
Total Time (days)
1.8
6.9
7.2
30
Tokens/parameter
1,050
335
225
210
Max Learning Rate
1 × 10−3
6 × 10−4
4 × 10−4
2 × 10−4
Min Learning Rate
1 × 10−4
6 × 10−5
4 × 10−5
2 × 10−5
GPU Count (A100)
8
8
16
16
MFU
43%
54%
53%
55%
Tokens/seconds
1,066,000
346,000
387,000
180,200
% Memory Footprint
43.75%
92.5%
95%
95%
Table 5: All models used AdamW [102], with the following configuration: ε = 1 × 10−8, β1 = 0.9,
and β2 = 0.95. We applied a weight decay factor of 0.1 and a gradient clipping threshold of 1.0 to
regularize gradient values. Regarding optimizer scheduling, all models had 1,000 warm-up steps,
where the learning rate was linearly increased up to the max learning rate. After that, during 90% of
the training, we used a cosine learning rate decay from its maximum value to a minimum learning rate
(10% of the maximum learning rate). For the last 10% of the training, the minimum learning rate is
sustained as a constant. All models were trained using BF16 mixed precision, TF32 mode enabled for
matrix multiplication operations, and FlashAttention 2, in addition to the Liger Triton kernels. Many
of these configurations were estimated via experiments (i.e., short runs of ≈10,000 steps) or directly
imported from the documentation of other LLMs of similar size [19, 182, 174, 15, 73, 96, 181, 158].
computed and stored in several gradient accumulation steps. Still, the model weights are not updated
immediately. Instead, the gradients are accumulated and normalized over multiple mini-batches,
and only after a specified number of iterations (the accumulation steps) are the model’s parameters
updated. This method effectively allows training with larger equivalent batch sizes without increasing
memory requirements. Hence, several studies document the use of this approach to simulate large,
million-size batch ranges [73, 89, 101].
Aware of this trend, our initial experiments used gradient accumulation steps to increase our models’
batch size artificially. However, we documented a significant decrease in convergence speed when
applying gradient accumulation steps, where the more gradient accumulation steps performed (e.g., 2,
4), the slower the convergence of our models became. To investigate this issue further, we promoted
a series of small test runs on our smallest model to track how the rate of change in loss (dloss) was
influenced by the amount of gradient accumulation steps performed. Our results are depicted in Fig.
4.
Given these results, we conclude that a better performance can be achieved without the use any
form of gradient accumulation. Although we could have lowered our memory footprint by using
gradient checkpointing [29], and hence, increased our batches without the need for accumulation
steps, we decided to prioritize training speed and efficient hardware utilization. It is puzzling why
other works that employed the gradient accumulation approach on Llama models did not report such
a phenomenon [89]. For the moment, we hypothesize that the root means squared normalization
used in the Llama architecture, which already averages batch-dependent activations, suffered from an
introduction of extra noise when we adopted smaller batches combined with gradient accumulation
averaging of the loss. However, more extensive experimentation is required to truly understand the
causes of this phenomenon and determine how practitioners can use gradient accumulation strategies
without severely impacting the training performance of this type of neural architecture.
6.3
Evaluation Protocol
While training our base models, we saved several checkpoints for each model at intervals of ap-
proximately 10.5 billion tokens. For every checkpoint, in addition to running a small evaluation
dataset (i.e., 60,000 samples randomly selected and excluded from GigaVerbo) to track the model’s
14

--- Page 15 ---

Figure 4: We tested several batch sizes on our 160 million parameter model, from 1 million (512) to 65 thousand
tokens (32), while also trying to reproduce a 0.5 million batch (256) via different levels of gradient accumulation
(i.e., 2, 4, and 8 accumulation steps). We maintained the learning rate and the β values of the AdamW constant
for all these tests, together with a linear warm-up of 1,000 steps. As expected, the 1 million tokens batch, with
no gradient accumulation steps (i.e., step of 1), produced the best loss curve with faster convergence at the
earliest stages of training, followed by all other batch sizes (i.e., 256, 128, 64, and 32) that did not have gradient
accumulation steps. At the same time, the more gradient steps are applied to achieve a desired batch size, the
slower the convergence rate, up to the point that training with a global batch size of 32 and a global batch of
512 achieved via 2 gradient accumulation steps yield the same results in terms of convergence speed. While the
plot on the left shows the shape of the loss curve for several different batch sizes and gradient accumulation
configurations, the plot on the right shows the rate of change in loss (dloss) for the first 200 million tokens.
While this rate of change tends to converge to the same value for all experimented batch sizes (i.e., with time, all
lines converge at the same rate), the initial values differ significantly in the early stages of training, with bigger
"natural" batches presenting a higher rate of change. Although not through extensive exploration, we observed
the same behavior for our other model sizes, independent of tweaks to the learning rate hyper-settings or changes
in the number of warm-up steps.
perplexity as training progressed, we employed a comprehensive evaluation harness. This harness was
modeled after the work of Corrêa et al. [38], with additional benchmarks included. The benchmarks
in our evaluation harness can generally be categorized into two types: native evaluations, specifically
developed in Portuguese, and translated ones, consisting of English benchmarks machine-translated
into Portuguese.
Although native benchmarks are ideal for assessing linguistic and cultural nuance, using translated
datasets was necessary due to the limited availability of Portuguese-specific evaluation benchmarks.
This approach allows us to determine our model’s generalization capabilities across various domains
and ensure that critical evaluation categories, often well-represented in English datasets, are dutifully
assessed. Table 6 lists all the evaluations used in our custom harness.
In total, this evaluation harness comprises 14 benchmarks, ten of which are native to Portuguese, and
four are machine-translated from English datasets. The native benchmarks include ENEM [147],
BLUEX [6], OAB [45], ASSIN2 RTE [134], ASSIN2 STS [134], FAQUAD NLI [138], HateBR
[163], PT Hate Speech [59], and TweetSentBR [20], all tied to a natively Brazilian Portuguese
implementation of the Language Model Evaluation Harness [62], made available by Garcia [63]. In
the assessment of CALAME-PT, we had to create a custom evaluation protocol based on the work
of Lopes et al. [101], i.e., all generations are performed deterministically without sampling in a
zero-shot manner, with only exact matches being counted as a successful inference.
The remaining four benchmarks, ARC-Challenge [31], HellaSwag [179], and TruthfulQA [97] are
all evaluations tied to a machine-translated version of the original (English) datasets, made available
by a multilingual implementation of the Language Model Evaluation Harness (Lai et al. [88]). All
few-shot settings for assessment remain the same as the one set for standard leaderboard comparisons.
For LAMBADA-PT, a machine-translated version of the original test set of LAMBADA [121], we
used the same evaluation protocol as the one used in CALAME-PT, given that both benchmarks
involve the same primary task (i.e., predict the final word of a given sentence).
Finally, to evaluate the "Instruct" versions (see Section 7 for more details) of our base models, we
developed a Portuguese chat evaluation dataset, comprised of 805 completion samples extracted from
a machine-translated version of the original Alpaca dataset [159]12. In this evaluation, our model’s
12This dataset is available on Hugging Face.
15

--- Page 16 ---

Benchmark
n-shot
Origin
Type
Metric
ENEM
3-shot
Native
Q&A
acc
BLUEX
3-shot
Native
Q&A
acc
OAB Exams
3-shot
Native
Q&A
acc
ASSIN2 RTE
15-shot
Native
Entailment
f1 macro
ASSIN2 STS
10-shot
Native
Similarity
pearson
FAQUAD NLI
15-shot
Native
Entailment
f1 macro
HateBR
25-shot
Native
Classification
f1 macro
PT Hate Speech
25-shot
Native
Classification
f1 macro
TweetSentBR
25-shot
Native
Classification
f1 macro
CALAME-PT
0-shot
Native
Next Word Prediction
acc
ARC-Challenge
25-shot
Translated
Q&A
acc norm
HellaSwag
10-shot
Translated
Q&A
acc norm
TruthfulQA
0-shot
Translated
Q&A
bleurt
LAMBADA
0-shot
Translated
Next Word Prediction
acc
Table 6: A description of the evaluation harness used in our work. To learn how to replicate our
usage of this harness, please visit the evaluation section of our GitHub repository.
outputs are compared to a reference standard13 and later judged by an automated annotator (GPT-4
Turbo) to determine their relevance, coherence, and adherence to the instruction prompts. In line with
the evaluation methodology proposed by Dubois et al. [51], we use length-controlled win rates as our
evaluation metric, given that these are highly correlated with human preferences and evaluations of
pair-wise comparisons.
7
Alignment
To offer a more easy-to-use version of our more capable models (i.e., 1b1 and 2b4), we implemented a
fine-tuning process divided into two stages: supervised fine-tuning (SFT) [119] and direct preference
optimization (DPO) [132].
For the supervised fine-tuning step, we synthesized a small dataset containing over 600K samples
of user-assistant interactions generated by other models that went through an alignment process.14.
A description of this dataset can be found in Table 7. These fine-tuned models have special chat-
delimiting tokens (i.e., <instruction> and </instruction>) added to their tokenizers and were
trained by starting from the latest checkpoint of their respective model (e.g., Tucano-1b1, step
480,000). Regarding hyper-settings, fine-tuning jobs performed another learning rate decay to 10%
of the original minimal value achieved during training, with no warm-up steps and all other hyper-
parameters unchanged. Both models were trained on a batch size of 262K tokens per optimizer step
for four epochs.
Finally, for the DPO step, we used the preference modeling dataset developed by Corrêa [37],
which consists of 35K triplets comprising a user prompt, a preferred response, and a less preferred
alternative. We design our DPO fine-tuning implementation on top of the Transformer Reinforcement
Learning (TRL) library [167]. We trained both models using their respective SFT versions as initial
checkpoints. Regarding hyper-settings, for both models, we used a cosine learning rate scheduler
13In our case, we use the original text-davinci-003 completions from the Alpaca dataset.
14In general terms, we can define an alignment process as a process in which we seek to improve a system’s
capability to follow human instructions and intentions while minimizing the possible harm it can cause [37].
16

--- Page 17 ---

Subset
Nº of Samples
%
Description
GPT4-500k-PTBR
565,536
83%
A machine-translated version of conversa-
tions with GPT-4 [24].
Orca-Math-PT
64,073
9.5%
A machine-translated version of Orca-math
dataset [109].
Instruct-Aira v.3
50,000
7.5%
A collection of multi-turn conversations gen-
erated by user interactions with conversa-
tional LLMs [37].
Table 7: A description of the datasets used in the alignment of the trained models. This dataset is
currently hosted on Hugging Face. More information can be found in its dataset card.
with a learning rate of 1 × 10−6 and a weight decay of 0.1. We set beta to 0.5, applied sigmoid as
the loss function and used zero label smoothing. We repeated the dataset for three epochs, with a
global batch size of 16 for the 1b1 model and 8 for the 2b4 model. This two-step alignment approach
outputs the "Instruct" version of our models: Tucano-1b1-Instruct and Tucano-2b4-Instruct.
8
Results
Figure 5 depicts the logged training loss and validation perplexity curves for all four base models
we trained. As expected, larger models exhibit a more significant reduction in loss and perplexity as
training progresses, even though this difference would be made more pronounced if we could train
our bigger models with larger batches. In short, our logs reaffirm that as the model size and data
ingestion are increased, the performance of the language model also increases.
Figure 5: All logs from our training runs recorded loss, evaluation loss, the current value of the learning rate,
and the gradient norm for that specific optimization step. These logs are available in our GitHub repository.
8.1
Benchmark Evaluations
As mentioned, for every 10.5 billion tokens processed during training, we saved a checkpoint for
each model and ran our evaluation harness on it. This approach allowed us to systematically track
and represent model performance as a function of time and token ingestion, enabling us to observe
how model performance, across several benchmarks, is related to token ingestion on a plain causal
language modeling regime without intentionally seeking to overfit a specific training (or evaluation)
distribution.
If we assume that "the more a model is trained on new tokens, the more capable it becomes",
as demonstrated by several works examining the scaling behavior of LLMs [131, 78, 15, 175,
181], we would expect to observe this phenomenon when evaluating our models with the custom
evaluation harness we developed (which contains most of the evaluations used by the Portuguese
NLP community). To test this hypothesis, we calculated the Pearson product-moment correlation
17

--- Page 18 ---

coefficients between our evaluation results and the number of tokens processed at each checkpoint. A
positive correlation between token ingestion and benchmark performance would suggest a relationship
between these variables, implying that performance improves as the model ingests more tokens.
However, this anticipated pattern was only observed across some benchmarks, as seen in Table 8.
Benchmark
r160m
r630m
r1b1
r2b4
ENEM
0.10
-0.45
0.41
0.48
BLUEX
-0.06
0.21
0.52
0.00
OAB Exams
0.34
0.21
0.28
0.24
ASSIN2 RTE
-0.30
0.78
0.74
0.34
ASSIN2 STS
0.58
0.22
0.81
-0.50
FAQUAD NLI
-0.31
0.00
0.00
0.17
HateBR
-0.56
0.65
0.48
-0.36
PT Hate Speech
-0.75
-0.15
0.31
0.49
TweetSentBR
0.17
0.50
0.33
0.88
CALAME-PT
0.92
0.96
0.94
0.86
ARC-Challenge
0.76
0.69
0.82
0.61
HellaSwag
0.93
0.94
0.90
0.89
TruthfulQA
-0.16
0.66
-0.05
-0.30
LAMBADA
0.89
0.90
0.91
0.86
Table 8: The table shows all correlation scores for each benchmark against the different models.
The highlighted scores correspond to a Pearson product-moment correlation value above 0.6, while
the highlighted benchmarks are those where a positive correlation above 0.6 was found for all
models, irrespective of size. To replicate these results, you can use the evaluation logs and code
implementation available in our GitHub repository.
Even when considering the possibility that specific in-context capabilities only emerge once models
reach a particular scale, our results do not consistently show this pattern across benchmarks of the
same type, such as multiple-choice Q&A evaluations. For instance, benchmarks like ENEM and
BLUEX show a moderate positive correlation only for the 1b1 model. Meanwhile, for the OAB
Exams (Brazilian Bar Exam), performance appears entirely uncorrelated with the number of tokens
processed, despite over 4 billion tokens from our dataset originating from the legal domain, regardless
of model size. We initially hypothesized that model performance might only exceed random chance
for benchmarks like ENEM, BLUEX, and OAB Exams once the models surpass a certain parameter
threshold (e.g., 7 billion), which would explain the poor performance of smaller models. However,
this does not account for why performance correlates significantly with training volume on similar
benchmarks, such as ARC-Challenge and HellaSwag, which follow a multiple-choice Q&A format.
At the same time, for all sub-billion parameter models, we find instances where "training hinders
benchmark performance", i.e., inverse scaling. This is especially true for our 160 million parameter
model, where, for several benchmarks, its performance worsens as the model advances its training.
Also, for evaluations like HateBR and ASSIN2 STS, we again see this phenomenon afflicting our 2b4
model, where training causes the models to become worse than a random guesser. At the same time,
performance on benchmarks like the Portuguese native FAQUAD NLI seems completely uncorrelated
with token ingestion.
These results prompt us to question the validity of these evaluations and help explain other results
presented in the literature[101]. Regardless of the number of tokens in which models were trained,
language modeling capabilities did not translate to performance in numerous evaluations used by
the community. Hence, we hypothesize that results showing good performance on such benchmarks
(i.e., above what a random guesser would achieve) might indicate not language modeling pretraining
but overfitting to the style of evaluation these benchmarks bring (e.g., multiple choice Q&A of
18

--- Page 19 ---

(a) CALAME-PT
(b) HellaSwag
(c) ARC-Challenge
(d) LAMBADA
Figure 6: The images above show instances where benchmark performance increases as models are trained on
more tokens. The same analysis for all benchmarks used in this study can be found in our GitHub repository.
OAB exams or ENEM tests), or simple luck15. However, given that many studies do not share the
foundations of their work, like pretraining/fine-tuning datasets, it becomes hard to explain, on an
empirical level, the performance documented by such developments [127, 5, 141].
Despite these findings, we observed several evaluations where the extent of language modeling
pretraining shows an above-average (> 60%) positive correlation with benchmark performance across
the entire series (Fig. 6). Benchmarks such as CALAME-PT (6a), LAMBADA(6d), HellaSwag(6b),
and the ARC-Challenge(6c) consistently showed improvement as causal language modeling pre-
training scales. These benchmarks, therefore, seem to serve as the most reliable indicators of model
performance and capabilities when training native Portuguese LLMs with plain common crawl data.
These insights could assist other practitioners in selecting benchmarks for evaluating smaller LLMs
and determining which benchmarks might be better suited for models specifically trained or fine-tuned
for particular domains (e.g., OAB test exams).
Focusing only on the benchmarks that showed a significant correlation between language modeling
pretraining and performance, we obtained the results in Table 9. According to our evaluation protocol,
our largest models outperformed several multilingual and natively pre-trained LLMs across nearly
all benchmarks, including the recently released Llama-3.2-1b, trained on a far larger dataset than
GigaVerbo. Our models also outperformed larger multilingual models, such as Bloom-1b7, in
benchmarks like CALAME-PT and LAMBADA. Considering all benchmarks in our evaluation suite,
our series outperforms all models listed in Table 9, except the models coming from the Llama-3.2
series 16.
It is also noteworthy that the fine-tuning/alignment process has the potential to degrade the per-
formance of the foundational model on specific benchmarks. For instance, while our alignment
process improved the controllability of our models for users, it reduced their performance in particular
15On benchmarks like ASSIN2 RTE, performance fluctuates drastically from checkpoint to checkpoint.
16Additionally, we noticed that Llama-based models like Sabiá-7b, Gervásio-7b, and Llama-2-7b significantly
outperform other models on benchmarks where we observed a low correlation between language modeling
pretraining and evaluation performance (e.g., ENEM, BLUEX, OAB Exams, FAQUAD NLI). Since we do
not have access to the training data for these models (particularly the pretraining corpus of the Llama series),
we suspect this performance discrepancy may be due to overfitting on specific evaluation styles, which, we
speculate, could require particular types of data or domain knowledge to achieve the documented results.
19

--- Page 20 ---

Average
Calame-PT
Lambada-PT
ARC-PT
HellaSwag-PT
Llama-3.2-3B
52.00
58.43
49.1
43.25
57.2
Tucano-2b4
43.58
59.06
37.67
30.43
47.17
Llama-3.2-1B
42.95
51.83
41.02
33.5
45.44
Tucano-1b1
41.55
58.24
34.7
30.43
42.84
Gemma-2b
40.38
51.16
39.88
37.95
32.53
Bloom-1b7
40.37
55.64
31.98
30.34
43.52
Tucano-630m
39.5
56.55
33.13
28.89
39.41
Gemma-2-2b
39.21
56.7
47.1
24.19
28.85
Bloom-1b1
38.18
52.94
30.22
29.83
39.74
GlórIA-1b3
36.05
52.79
27.71
26.67
37.04
Tucano-160m
35.14
52.31
28.16
27.01
33.07
XGLM-564m
34.55
50.58
27.42
25.56
34.64
Bloom-560m
34.32
49.95
25.44
24.74
37.15
TTL-460m
33.78
49.42
23.29
29.4
33.00
mGPT-1b3
31.81
47.14
29.92
23.81
26.37
TTL-160m
30.78
46.72
20.98
26.15
29.29
Lola-v1
30.19
26.4
18.32
30.42
45.61
GPorTuguese
28.92
40.61
22.98
22.48
29.62
Table 9: Evaluation benchmark scores for our models compared with models of similar size. For this
table, we use only the benchmarks that demonstrated a positive correlation (> 60%) between bench-
mark performance and token ingestion across the entire series. All evaluations for all benchmarks
that form our custom harness are available on our GitHub repository.
benchmarks17. However, when looking at our Instruct models via our custom AlpacaEval benchmark,
a more appropriate benchmark for evaluating chat models, we see promising results (Table 10), where
Tucano-Instruct models can outperform much larger models (e.g., Sabiá-7b and Gervásio-7b), and
approximate models like the ones from the Llama-3.2 series.
Avg. Length
Wins
Base Wins
LC Win Rate (%)
Std. Error
Llama-3.2-3B-Instruct
1609
257
548
21.06
0.075
Tucano-2b4-Instruct
1843
151
654
13.00
0.071
Tucano-1b1-Instruct
1667
124
681
8.80
0.083
Llama-3.2-1B-Instruct
1429
99
706
7.15
0.057
TeenyTinyLlama-460m-Chat
1333
28
777
2.84
0.059
Sabiá-7b
5011
1
804
0.076
0.0043
Gervásio-7b
5740
1
804
0.026
0.0016
Table 10: Length-controlled win rates and standard errors for different models evaluated with the
Alpaca-Eval-PT. All models were evaluated on 805 prompts. To replicate our evaluation, visit our
GitHub repository.
8.2
Qualitative Demonstration
To complement our evaluations, Table 11 presents a qualitative demonstration of Tucano’s text
generation capabilities by prompting our largest models on diverse topics related to Brazilian and
Portuguese culture.
According to our initial explorations, Tucano models demonstrate a firm grasp of culturally relevant
subjects tied to the Lusophone world and can generate coherent and contextually appropriate text
regarding many subjects. However, like all LLMs, our models have strong tendencies towards generat-
ing hallucinations, i.e., text that is grammatically correct but factually erroneous or incomprehensible,
17The same applies to Gervásio-7b, which performs considerably worse than its raw base (Llama-2-7b) across
nearly all evaluations.
20

--- Page 21 ---

A floresta da Amazônia é conhecida por sua biodi-
versidade e diversidade de espécies vegetais e ani-
mais. No entanto, a exploração madeireira ilegal e
o desmatamento continuam a ameaçar esta impor-
tante área natural. A extração ilegal de madeira na
Amazônia tem sido um problema significativo. Um
estudo realizado pelo World Wildlife Fund (WWF)
em 2019 descobriu que mais de 80% das árvores
derrubadas na região foram ilegalmente extraídas.
O desmatamento, juntamente com as mudanças
climáticas, está causando uma perda significativa
de habitat para muitas espécies, incluindo pás-
saros, mamíferos e insetos. (...)
O Carnaval do Rio de Janeiro é um dos mais
famosos e tradicionais do mundo. A festa acon-
tece durante os dias que antecedem a Quarta-Feira
de Cinzas, o primeiro dia da Quaresma. Durante
cinco dias, os foliões saem às ruas em busca de
diversão e adoram celebrar até o amanhecer nas
festas de rua e nos desfiles das escolas de samba.
A cidade do Rio de Janeiro, conhecida mundial-
mente por suas belezas naturais, também tem seu
carnaval. As pessoas se reúnem para curtir as
marchinhas e sambas-enredo das escolas de samba
e os blocos de rua (...)
<instruction>Qual é a capital do Estado do Rio
Grande do Sul?</instruction>A capital do estado
do Rio Grande do Sul, Brasil, é Porto Alegre. É um
importante centro cultural, econômico e político
no sul do Brasil. A cidade tem uma população de
cerca de 1,4 milhão de habitantes e está localizada
na região metropolitana de Porto Alegre, que inclui
cidades vizinhas como Canoas, Gravataí e Viamão
(...)
"<instruction>Quem
foi
Fernando
Pes-
soa?</instruction>"Fernando
Pessoa
foi
um
poeta, escritor e tradutor português nascido em 13
de junho de 1888, em Lisboa. Ele é amplamente
considerado como o maior poeta da língua
portuguesa e uma figura cultural significativa do
século XX. Aqui estão alguns detalhes sobre sua
vida e obra: (...)
A culinária Portuguesa é famosa por pratos como
o bacalhau, a alheira, os pastéis de nata e as
sardinhas. Além disso, os vinhos portugueses são
conhecidos mundialmente pela sua qualidade e
sabor único. Se você está planejando uma vi-
agem para Portugal, não deixe de experimentar
esses pratos deliciosos e desfrutar da cultura gas-
tronômica única do país (...)
Um fator comun entre países como o Brasil, An-
gola e Moçambique é que todos foram coloniza-
dos por Portugal e, portanto, têm uma história
comum de colonização. O Brasil foi colônia por-
tuguesa até 1822, quando a independência do país
foi proclamada (...)
Table 11: These text samples (prompts and generations) were generated by Tucano-2b4 (and
2b4-Instruct) using beam search decoding with the following sampling configuration: top-p = 1.0,
temperature = 0.3, top-k = 100.
besides other limitations tied to the fact that a significant portion of our pretraining corpus contains
machine-translated samples of English text.
8.3
Energy Consumption and Carbon Emissions
Following the example of past works [154, 67, 103, 87, 47, 104], and with the knowledge of the
side effects deep learning practices can have when scaled at the level required by large foundation
models [162, 124, 54, 55], we tracked our energy use during training, experiments, and evaluation.
We measured the energy consumption and estimated carbon emissions for every checkpoint created
during our training runs and experiments. All estimations were made using the 2023 estimations
of the carbon intensity of Germany’s energy grid (0.37 KgCO2eq/KWh)18, which, according to
Lottick et al. [103] methodology, can be used to infer carbon emissions (CO2eq) by multiplying the
carbon intensity of the energy grid by the total energy consumption of a given experiment. Table 12
summarizes the energy and carbon footprint related to our work.
Deep learning research is fundamentally driven by experimentation and heuristic approaches. Al-
though many studies attempt to document training procedures [182, 14, 49, 182], offering valuable
guidelines for configuring models and their training environments, these published (or documented)
procedures rarely provide universal solutions. Hence, the heuristic challenges and the current deficien-
18Available in CodeCarbon’s source [32].
21

--- Page 22 ---

Model
Duration (hours)
Training (kWh)
Exp. (kWh)
Emissions (KgCO2eq)
160m
44
235
200
160
630m
170
920
125
387
1b1
194
2,600
335
1,085
2b4
860
11,860
400
4,536
Total
1,268
15,615
1,060
6,168 KgCO2eq
Table 12: The table above shows, for each model, the duration of its training run, the energy
consumption related to that run, the energy consumption regarding experimentation and evaluations,
and the total estimated carbon emissions regarding the development of that model size. The training of
the instruct versions is also accounted for in each respective model. To minimize energy consumption,
we performed almost all of our experiments using the smaller version of our models. According to
our logs, we utilized around 5,900 GPU hours across training, translating to an estimated cost of
approximately 5,990 USD, assuming a rate of 1.1 USD per hour per A100 GPU. From the total of
16,675 kWh used, a significant portion (≈6%) was used to run experiments and evaluations, totaling
6.1 tCO2eq in emissions.
cies in training documentation force researchers to expend resources and energy that could have been
avoided when developing new models. Meanwhile, several factors shape the carbon footprint of deep
learning, including the unique characteristics of each experiment and the infrastructure supporting
it. In our experience, we frequently needed to fine-tune hyperparameters, adjust preprocessing
strategies, and conduct exploratory experiments to achieve good results. However, this reliance on
experimentation has significant environmental implications. To address this issue, we performed
most experiments using our smaller models, as experimenting with the larger models (e.g., 2b4)
would have led to a much higher increase in CO2 emissions, which we aimed to avoid. In short,
LLM development is computationally demanding, with a substantial portion of energy consumption
occurring outside the training runs.
9
Future Works
The Tucano series significantly contributes to the Portuguese NLP community in several ways. First,
we ensure that the entire series is open-source and highly reproducible. Additionally, the language
models we present are trained on the largest documented dataset of native Portuguese text. To the best
of our knowledge, the scale of monolingual Portuguese pretraining in this study is unprecedented in
the literature. All models, along with intermediary checkpoints, datasets, code implementations, and
logs, are freely accessible through the repositories associated with this study. Table 13 summarizes
the availability of the artifacts mentioned earlier in the context of the Portuguese LLMs reviewed in
Section 2, with a comparison to our own work.
Nevertheless, numerous milestones remain to be achieved before Portuguese can be considered a
high-resource language. Some of the prospects for future studies are:
1. Expanding GigaVerbo by creating larger concatenation of Portuguese datasets. Future
studies should seek to enrich our pretraining corpus with more high-quality tokens, like
academic papers, books, and other forms of high-quality text. Ambitiously, we should aim to
reach the trillion-token range. At the same time, it would be interesting to conduct ablation
studies on GigaVerbo to determine the impact of different dataset components and identify
which subsets contribute most effectively to model performance.
2. Further enhancing GigaVerbo by incorporating synthetically generated data. While
this approach was not explored in our current study, synthetic data augmentation has been
proven in other works to bolster model performance in many specific domains (e.g., coding
and storytelling) [73]. In the future, augmenting GigaVerbo with this type of data could
22

--- Page 23 ---

improve its representative power in domains where, in its current state, it is found to be
lacking.
3. Explore the downstream applicability of the Tucano series: Future studies can use the models
from the Tucano series as foundations for future developments, like multimodal Portuguese
LLaVas [99], Portuguese embedding models [12], or more capable filters and guardrails.
4. Increasing model scale to larger architectures, such as 3B, 7B, and 13B parameters.
Scaling up to larger model sizes would enable us to understand better how benchmark
performance changes with model size and to determine whether certain benchmarks correlate
more strongly with language modeling pretraining only when models exceed a certain size
threshold.
5. Developing new and more comprehensive benchmarks for Portuguese. Our results
indicate that Portuguese evaluation benchmarks for generative language models require
improvement. Future research to advance Portuguese NLP should focus on either developing
more effective benchmarks or refining existing ones to better capture the impact of pre-
training and provide a more precise correlation between pretraining depth and performance
across various language tasks.
Model
Data
Code
Logs
#models
#ckpts
Tucano
✓
✓
✓
✓
6
111
TeenyTinyLlama
✓
✓
✓
✓
3
70
GPorTuguese
✓
✓
✓
✓
1
1
PTT5
✓
✓
✓
✗
6
1
RoBERTaLexPT
✓
✓
✗
✗
2
3
Albertina
✓
✓
✗
✗
8
1
BERTimbau
✓
✓
✗
✗
2
1
DeBERTinha
✓
✓
✗
✗
1
1
Gervásio
✓
✓
✗
✗
2
1
PTT5-v2
✓
✗
✗
✗
4
1
BERTabaporu
✓
✗
✗
✗
2
1
Glória
✓
✗
✗
✗
1
1
Sabiá
✓
✗
✗
✗
1
1
Sabiá-2
✗
✗
✗
✗
2
None
Sabiá-3
✗
✗
✗
✗
1
None
Table 13: The above table compares Portuguese language models regarding the open-source avail-
ability of models, datasets, code, logs, the total number of models (#models), and the number of
checkpoints (#ckpts). In terms of open (and reproducible) development, many aspects of past stud-
ies are indeed closed. Saved for rare exceptions [72, 26, 38], many studies only make available
"end-products" devoid of logs, datasets, or code implementations, making the reproduction of LLM
development a task that requires constant rediscovering. Given the level of computing needed to
practice deep learning at such scales, a lack of reusable code and materials can seriously slow down
the Portuguese NLP community’s progress while hindering its sustainability.
10
Conclusion
In this study, we introduced the Tucano series, a collection of open-source large language models
designed to advance natural language processing for Portuguese. Our work covered the entire de-
velopment pipeline, from dataset creation and filtration to hyperparameter tuning and evaluation,
emphasizing openness and reproducibility. These efforts contribute capable models, large datasets,
and tools to the Portuguese NLP community to set a standard for transparent and replicable research
practices. Moreover, our critical assessment of the field highlighted ongoing challenges, particularly
around evaluation methodologies and result interpretability, which will only be solved if the commu-
nity shifts toward a more rigorous and reproducible developmental framework. Finally, we hope our
contributions will help spur this shift, providing essential resources to guide future studies. Ultimately,
23

--- Page 24 ---

we hope the work initiated here will be extended to other low-resource languages, fostering a more
equitable and sustainable NLP ecosystem globally.
Acknowledgments
The authors gratefully acknowledge the granted access to the Marvin cluster hosted by the University
of Bonn along with the support provided by its High Performance Computing & Analytics Lab.
Authors would also like to acknowledge their own personal funding agencies. Nicholas Kluge
Corrêa is funded by the Ministerium für Wirtschaft, Industrie, Klimaschutz und Energie des Landes
Nordrhein-Westfalen (Ministry for Economic Affairs, Industry, Climate Action and Energy of
the State of North Rhine- Westphalia), as part of the KI.NRW-flagship project "Zertifizierte KI"
(Certified AI). Aniket Sen is funded by the Deutsche Forschungsgemeinschaft (DFG, German
Research Foundation) as part of the CRC 1639 NuMeriQS – project no. 511713970.
Author’s Information
The corresponding author is Nicholas Kluge Corrêa. He is a postdoctoral researcher at the Center
for Science and Thought at the University of Bonn (Bonn, NRW, Germany). His contact email is
kluge@uni-bonn.de.
Aniket Sen is a postdoctoral researcher at the High Performance Computing and Analytics Lab and
the Helmholtz-Institut für Strahlen- und Kernphysik at the University of Bonn. His contact email is
sen@hiskp.uni-bonn.de.
Sophia Falk is a PhD researcher at the Bonn Sustainable AI Lab, Institute for Science and Ethics,
University of Bonn. Her contact email is falk@iwe.uni-bonn.de.
Shiza Fatimah is a master’s student at the Institute for Computer Science at the University of Bonn.
Her contact email is s39sfati@uni-bonn.de.
References
[1] Julien Abadji, Pedro Ortiz Suarez, Laurent Romary, and Benoît Sagot. Towards a cleaner
document-oriented multilingual crawled corpus. arXiv preprint arXiv:2201.06642, 2022.
[2] Oliver Adams, Adam Makarucha, Graham Neubig, Steven Bird, and Trevor Cohn. Cross-
lingual word embeddings for low-resource language modeling. In Proceedings of the 15th
Conference of the European Chapter of the Association for Computational Linguistics: Volume
1, Long Papers, pages 937–947, 2017.
[3] Joshua Ainslie, James Lee-Thorp, Michiel de Jong, Yury Zemlyanskiy, Federico Lebrón, and
Sumit Sanghai. Gqa: Training generalized multi-query transformer models from multi-head
checkpoints. arXiv preprint arXiv:2305.13245, 2023.
[4] Ebtesam Almazrouei, Hamza Alobeidli, Abdulaziz Alshamsi, Alessandro Cappelli, Ruxandra
Cojocaru, Mérouane Debbah, Étienne Goffinet, Daniel Hesslow, Julien Launay, Quentin
Malartic, et al. The falcon series of open language models. arXiv preprint arXiv:2311.16867,
2023.
[5] Thales Sales Almeida, Hugo Abonizio, Rodrigo Nogueira, and Ramon Pires. Sabi\’a-2: A
new generation of portuguese large language models. arXiv preprint arXiv:2403.09887, 2024.
[6] Thales Sales Almeida, Thiago Laitz, Giovana K. Bonás, and Rodrigo Nogueira. Bluex: A
benchmark based on brazilian leading universities entrance exams, 2023.
[7] Yuvanesh Anand, Zach Nussbaum, Brandon Duderstadt, Benjamin Schmidt, and Andriy
Mulyar. Gpt4all: Training an assistant-style chatbot with large scale data distillation from
gpt-3.5-turbo. GitHub (2023), 2023.
24

--- Page 25 ---

[8] Jordi Armengol-Estapé, Casimiro Pio Carrino, Carlos Rodriguez-Penagos, Ona de Gibert
Bonet, Carme Armentano-Oller, Aitor Gonzalez-Agirre, Maite Melero, and Marta Villegas.
Are multilingual models the best choice for moderately under-resourced languages? a compre-
hensive assessment for catalan. arXiv preprint arXiv:2107.07903, 2021.
[9] David Arnold. Europe, technology, and colonialism in the 20th century. History and Technol-
ogy, 21(1):85–106, 2005.
[10] Viraat Aryabumi, John Dang, Dwarak Talupuru, Saurabh Dash, David Cairuz, Hangyu Lin,
Bharat Venkitesh, Madeline Smith, Kelly Marchisio, Sebastian Ruder, et al. Aya 23: Open
weight releases to further multilingual progress. arXiv preprint arXiv:2405.15032, 2024.
[11] Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. Neural machine translation by
jointly learning to align and translate. arXiv preprint arXiv:1409.0473, 2014.
[12] Parishad BehnamGhader, Vaibhav Adlakha, Marius Mosbach, Dzmitry Bahdanau, Nicolas
Chapados, and Siva Reddy. Llm2vec: Large language models are secretly powerful text
encoders. arXiv preprint arXiv:2404.05961, 2024.
[13] Yoshua Bengio, Réjean Ducharme, and Pascal Vincent. A neural probabilistic language model.
Advances in neural information processing systems, 13, 2000.
[14] Stella Biderman, Hailey Schoelkopf, Quentin Anthony, Herbie Bradley, Kyle O’Brien, Eric
Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward Raff,
Aviya Skowron, Lintang Sutawika, and Oskar van der Wal. Pythia: A suite for analyzing large
language models across training and scaling, 2023.
[15] Stella Biderman, Hailey Schoelkopf, Quentin Gregory Anthony, Herbie Bradley, Kyle O’Brien,
Eric Hallahan, Mohammad Aflah Khan, Shivanshu Purohit, USVSN Sai Prashanth, Edward
Raff, et al. Pythia: A suite for analyzing large language models across training and scaling. In
International Conference on Machine Learning, pages 2397–2430. PMLR, 2023.
[16] Sid Black, Stella Biderman, Eric Hallahan, Quentin Anthony, Leo Gao, Laurence Golding,
Horace He, Connor Leahy, Kyle McDonell, Jason Phang, et al. Gpt-neox-20b: An open-source
autoregressive language model. arXiv preprint arXiv:2204.06745, 2022.
[17] Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von
Arx, Michael S Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. On the
opportunities and risks of foundation models. arXiv preprint arXiv:2108.07258, 2021.
[18] Luiz Henrique Bonifacio, Paulo Arantes Vilela, Gustavo Rocha Lobato, and Eraldo Rezende
Fernandes. A study on the impact of intradomain finetuning of deep language models for
legal named entity recognition in portuguese. In Intelligent Systems: 9th Brazilian Conference,
BRACIS 2020, Rio Grande, Brazil, October 20–23, 2020, Proceedings, Part I 9, pages 648–662.
Springer, 2020.
[19] Tom Brown, Benjamin Mann, Nick Ryder, Melanie Subbiah, Jared D Kaplan, Prafulla Dhari-
wal, Arvind Neelakantan, Pranav Shyam, Girish Sastry, Amanda Askell, et al. Language
models are few-shot learners. Advances in neural information processing systems, 33:1877–
1901, 2020.
[20] Henrico Bertini Brum and Maria das Graças Volpe Nunes. Building a sentiment corpus of
tweets in brazilian portuguese. arXiv preprint arXiv:1712.08917, 2017.
[21] Bruno Henrique. Caramelo 7b. https://huggingface.co/Bruno/Caramelo_7B, 2023.
[22] Bruno
Henrique.
Harpia-7b-guanacolora.
https://huggingface.co/Bruno/
Harpia-7b-guanacoLora, 2023.
[23] Israel Campiotti, Matheus Rodrigues, Yuri Albuquerque, Rafael Azevedo, and Alyson Andrade.
Debertinha: A multistep approach to adapt debertav3 xsmall for brazilian portuguese natural
language processing task, 2023.
[24] Carlo Moro. Gpt4-500k-augmented-ptbr-clean. https://huggingface.co/datasets/
cnmoro/GPT4-500k-Augmented-PTBR-Clean, 2024.
[25] Carlo Moro.
Instruct-ptbr-enus-11m.
https://huggingface.co/datasets/cnmoro/
Instruct-PTBR-ENUS-11M, 2024.
[26] Diedre Carmo, Marcos Piau, Israel Campiotti, Rodrigo Nogueira, and Roberto Lotufo.
Ptt5: Pretraining and validating the t5 model on brazilian portuguese data. arXiv preprint
arXiv:2008.09144, 2020.
25

--- Page 26 ---

[27] Jianghao Chen, Pu Jian, Tengxiao Xi, Dongyi Yi, Qianlong Du, Chenglin Ding, Guibo Zhu,
Chengqing Zong, Jinqiao Wang, and Jiajun Zhang. Chinesewebtext: Large-scale high-quality
chinese web text extracted with effective evaluation model, 2023.
[28] Tianqi Chen and Carlos Guestrin. Xgboost: A scalable tree boosting system. In Proceedings
of the 22nd acm sigkdd international conference on knowledge discovery and data mining,
pages 785–794, 2016.
[29] Tianqi Chen, Bing Xu, Chiyuan Zhang, and Carlos Guestrin. Training deep nets with sublinear
memory cost. arXiv preprint arXiv:1604.06174, 2016.
[30] Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, Gaurav Mishra, Adam
Roberts, Paul Barham, Hyung Won Chung, Charles Sutton, Sebastian Gehrmann, et al. Palm:
Scaling language modeling with pathways. arxiv 2022. arXiv preprint arXiv:2204.02311, 10,
2022.
[31] Peter Clark, Isaac Cowhey, Oren Etzioni, Tushar Khot, Ashish Sabharwal, Carissa Schoenick,
and Oyvind Tafjord. Think you have solved question answering? try arc, the ai2 reasoning
challenge. arXiv preprint arXiv:1803.05457, 2018.
[32] CodeCarbon. Codecarbon: Track emissions from compute and recommend ways to reduce
their impact on the environment. https://github.com/mlco2/codecarbon, 2019.
[33] Cohere For AI team. Policy primer - the ai language gap. https://cohere.com/research/
papers/policy-primer-the-ai-language-gap-2024-06-27, 2024.
[34] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek,
Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov.
Unsupervised cross-lingual representation learning at scale. In Proceedings of the 58th Annual
Meeting of the Association for Computational Linguistics, pages 8440–8451, Online, July
2020. Association for Computational Linguistics.
[35] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek,
Francisco Guzmán, Edouard Grave, Myle Ott, Luke Zettlemoyer, and Veselin Stoyanov.
Unsupervised cross-lingual representation learning at scale, 2020.
[36] Mike Conover, Matt Hayes, Ankit Mathur, Jianwei Xie, Jun Wan, Sam Shah, Ali Ghodsi,
Patrick Wendell, Matei Zaharia, and Reynold Xin. Free dolly: Introducing the world’s first
truly open instruction-tuned llm, 2023.
[37] Nicholas Kluge Corrêa. Dynamic normativity: Necessary and sufficient conditions for value
alignment. arXiv preprint arXiv:2406.11039, 2024.
[38] Nicholas Kluge Corrêa, Sophia Falk, Shiza Fatimah, Aniket Sen, and Nythamar De Oliveira.
Teenytinyllama: open-source tiny language models trained in brazilian portuguese. Machine
Learning with Applications, 16:100558, 2024.
[39] Pablo Botton Costa, Matheus Camasmie Pavan, Wesley Ramos Santos, Samuel Caetano Silva,
and Ivandré Paraboni. Bertabaporu: assessing a genre-specific language model for portuguese
nlp. In Proceedings of the 14th International Conference on Recent Advances in Natural
Language Processing, pages 217–223, 2023.
[40] Jan Christian Blaise Cruz and Charibeth Cheng. Evaluating language model finetuning
techniques for low-resource languages. arXiv preprint arXiv:1907.00409, 2019.
[41] Yiming Cui, Ziqing Yang, and Xin Yao. Efficient and effective text encoding for chinese llama
and alpaca. arXiv preprint arXiv:2304.08177, 2023.
[42] Tri Dao. FlashAttention-2: Faster attention with better parallelism and work partitioning. In
International Conference on Learning Representations (ICLR), 2024.
[43] Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré. FlashAttention: Fast
and memory-efficient exact attention with IO-awareness. In Advances in Neural Information
Processing Systems (NeurIPS), 2022.
[44] Ona De Gibert, Graeme Nail, Nikolay Arefyev, Marta Bañón, Jelmer Van Der Linde, Shaoxiong
Ji, Jaume Zaragoza-Bernabeu, Mikko Aulamo, Gema Ramírez-Sánchez, Andrey Kutuzov,
et al. A new massive multilingual dataset for high-performance language technologies. arXiv
preprint arXiv:2403.14009, 2024.
26

--- Page 27 ---

[45] Pedro Delfino, Bruno Cuconato, Edward Hermann Haeusler, and Alexandre Rademaker.
Passing the brazilian oab exam: data preparation and some experiments. arXiv preprint
arXiv:1712.05128, 2017.
[46] Li Deng and Yang Liu. Deep learning in natural language processing. Springer, 2018.
[47] Radosvet Desislavov, Fernando Martínez-Plumed, and José Hernández-Orallo. Compute and
energy consumption trends in deep learning inference. arXiv preprint arXiv:2109.05472, 2021.
[48] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. Bert: Pre-training of
deep bidirectional transformers for language understanding. arXiv preprint arXiv:1810.04805,
2018.
[49] Nolan Dey, Gurpreet Gosal, Hemant Khachane, William Marshall, Ribhu Pathria, Marvin
Tom, Joel Hestness, et al. Cerebras-gpt: Open compute-optimal language models trained on
the cerebras wafer-scale cluster. arXiv preprint arXiv:2304.03208, 2023.
[50] Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek Kadian, Ahmad Al-Dahle,
Aiesha Letman, Akhil Mathur, Alan Schelten, Amy Yang, Angela Fan, et al. The llama 3 herd
of models. arXiv preprint arXiv:2407.21783, 2024.
[51] Yann Dubois, Balázs Galambosi, Percy Liang, and Tatsunori B Hashimoto. Length-controlled
alpacaeval: A simple way to debias automatic evaluators. arXiv preprint arXiv:2404.04475,
2024.
[52] Yann Dubois, Chen Xuechen Li, Rohan Taori, Tianyi Zhang, Ishaan Gulrajani, Jimmy Ba,
Carlos Guestrin, Percy S Liang, and Tatsunori B Hashimoto. Alpacafarm: A simulation
framework for methods that learn from human feedback. Advances in Neural Information
Processing Systems, 36, 2024.
[53] Stefan Elfwing, Eiji Uchibe, and Kenji Doya. Sigmoid-weighted linear units for neural network
function approximation in reinforcement learning. Neural networks, 107:3–11, 2018.
[54] Sophia Falk and Aimee van Wynsberghe. Challenging ai for sustainability: what ought it
mean? AI and Ethics, pages 1–11, 2023.
[55] Sophia Falk, Aimee van Wynsberghe, and Lisa Biber-Freudenberger. The attribution problem
of a seemingly intangible industry. Environmental Challenges, page 101003, 2024.
[56] Fangxiaoyu Feng, Yinfei Yang, Daniel Cer, Naveen Arivazhagan, and Wei Wang. Language-
agnostic bert sentence embedding. arXiv preprint arXiv:2007.01852, 2020.
[57] Paulo Finardi, José Dié Viegas, Gustavo T Ferreira, Alex F Mansano, and Vinicius F Caridá.
Berta\’u: Ita\’u bert for digital customer service. arXiv preprint arXiv:2101.12015, 2021.
[58] Marcelo Finger, Maria Clara Paixão de Sousa, Cristiane Namiuti, Vanessa Martins do Monte,
Aline Silva Costa, Felipe Ribas Serras, Mariana Lourenço Sturzeneker, Raquel de Paula
Guets, Renata Morais Mesquita, Guilherme Lamartine de Mello, Maria Clara Ramos Morales
Crespo, Maria Lina de Souza Jeannine Rocha, Patrícia Brasil, Mariana Marques da Silva, and
Mayara Feliciano Palma. Carolina: The open corpus for linguistics and artificial intelligence.
https://sites.usp.br/corpuscarolina/corpus, 2022. Version 1.1 (Ada).
[59] Paula Fortuna, Joao Rocha da Silva, Leo Wanner, Sérgio Nunes, et al. A hierarchically-labeled
portuguese hate speech dataset. In Proceedings of the third workshop on abusive language
online, pages 94–104, 2019.
[60] Ankur Gandhe, Florian Metze, and Ian Lane. Neural network language models for low resource
languages. In Fifteenth Annual Conference of the International Speech Communication
Association, 2014.
[61] Leo Gao, Stella Biderman, Sid Black, Laurence Golding, Travis Hoppe, Charles Foster, Jason
Phang, Horace He, Anish Thite, Noa Nabeshima, et al. The pile: An 800gb dataset of diverse
text for language modeling. arXiv preprint arXiv:2101.00027, 2020.
[62] Leo Gao, Jonathan Tow, Stella Biderman, Sid Black, Anthony DiPofi, Charles Foster, Laurence
Golding, Jeffrey Hsu, Kyle McDonell, Niklas Muennighoff, et al. A framework for few-shot
language model evaluation. Version v0. 0.1. Sept, 2021.
[63] Eduardo A. S. Garcia. Open portuguese llm leaderboard. https://huggingface.co/
spaces/eduagarcia/open_pt_llm_leaderboard, 2024.
27

--- Page 28 ---

[64] Eduardo AS Garcia, Nadia FF Silva, Felipe Siqueira, Hidelberg O Albuquerque, Juliana RS
Gomes, Ellen Souza, and Eliomar A Lima. Robertalexpt: A legal roberta model pretrained
with deduplication for portuguese. In Proceedings of the 16th International Conference on
Computational Processing of Portuguese, pages 374–383, 2024.
[65] Gabriel Lino Garcia, Pedro Henrique Paiola, João Otávio Frediani, Luis Henrique Morelli,
João Vitor Mariano Correia, Danilo Samuel Jodas, Arnaldo Candido Junior, Bruno Elias
Penteado, Ivan Rizzo Guilherme, and João Paulo Papa. Ultrachatbr: Um dataset em português
baseado no ultrachat, 2023.
[66] Gabriel Lino Garcia, Pedro Henrique Paiola, Luis Henrique Morelli, Giovani Candido, Ar-
naldo Cândido Júnior, Danilo Samuel Jodas, Luis C. S. Afonso, Ivan Rizzo Guilherme,
Bruno Elias Penteado, and João Paulo Papa. Introducing bode: A fine-tuned large language
model for portuguese prompt-based task, 2024.
[67] Eva García-Martín, Crefeda Faviola Rodrigues, Graham Riley, and Håkan Grahn. Estimation
of energy consumption in machine learning. Journal of Parallel and Distributed Computing,
134:75–88, 2019.
[68] Jonas Geiping, Quentin Garrido, Pierre Fernandez, Amir Bar, Hamed Pirsiavash, Yann
LeCun, and Micah Goldblum. A cookbook of self-supervised learning. arXiv preprint
arXiv:2304.12210, 2023.
[69] Xinyang Geng and Hao Liu. Openllama: An open reproduction of llama. https://github.
com/openlm-research/open_llama, May 2023.
[70] Omer Goldman, Avi Caciularu, Matan Eyal, Kris Cao, Idan Szpektor, and Reut Tsarfaty. Un-
packing tokenization: Evaluating text compression and its correlation with model performance.
arXiv preprint arXiv:2403.06265, 2024.
[71] Ian Goodfellow, Yoshua Bengio, and Aaron Courville. Deep learning. MIT press, 2016.
[72] Pierre Guillou. Gportuguese-2 (portuguese gpt-2 small): a language model for portuguese
text generation (and more nlp tasks...).
https://huggingface.co/pierreguillou/
gpt2-small-portuguese, 2020.
[73] Suriya Gunasekar, Yi Zhang, Jyoti Aneja, Caio César Teodoro Mendes, Allie Del Giorno,
Sivakanth Gopi, Mojan Javaheripi, Piero Kauffmann, Gustavo de Rosa, Olli Saarikivi, et al.
Textbooks are all you need. arXiv preprint arXiv:2306.11644, 2023.
[74] Tahmid Hasan, Abhik Bhattacharjee, Md. Saiful Islam, Kazi Mubasshir, Yuan-Fang Li, Yong-
Bin Kang, M. Sohel Rahman, and Rifat Shahriyar. XL-sum: Large-scale multilingual ab-
stractive summarization for 44 languages. In Findings of the Association for Computational
Linguistics: ACL-IJCNLP 2021, pages 4693–4703, Online, August 2021. Association for
Computational Linguistics.
[75] Trevor Hastie, Robert Tibshirani, Jerome Friedman, Trevor Hastie, Robert Tibshirani, and
Jerome Friedman. Overview of supervised learning. The elements of statistical learning: Data
mining, inference, and prediction, pages 9–41, 2009.
[76] Pengcheng He, Jianfeng Gao, and Weizhu Chen.
Debertav3: Improving deberta using
electra-style pre-training with gradient-disentangled embedding sharing.
arXiv preprint
arXiv:2111.09543, 2021.
[77] Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. Deberta: Decoding-enhanced
bert with disentangled attention. arXiv preprint arXiv:2006.03654, 2020.
[78] Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza
Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al.
Training compute-optimal large language models. arXiv preprint arXiv:2203.15556, 2022.
[79] Pin-Lun Hsu, Yun Dai, Vignesh Kothapalli, Qingquan Song, Shao Tang, and Siyu Zhu. Liger-
kernel: Efficient triton kernels for llm training, 2024.
[80] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang,
Lu Wang, and Weizhu Chen. Lora: Low-rank adaptation of large language models. arXiv
preprint arXiv:2106.09685, 2021.
[81] Lifu Huang, Ronan Le Bras, Chandra Bhagavatula, and Yejin Choi. Cosmos QA: Machine
reading comprehension with contextual commonsense reasoning. In Proceedings of the 2019
28

--- Page 29 ---

Conference on Empirical Methods in Natural Language Processing and the 9th International
Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 2391–2401,
Hong Kong, China, November 2019. Association for Computational Linguistics.
[82] HuggingFace. Tokenizers: Fast state-of-the-art tokenizers optimized for research and produc-
tion. https://github.com/huggingface/tokenizers, 2019.
[83] Matthew Hutson. Has artificial intelligence become alchemy?, 2018.
[84] Roseval Malaquias Junior, Ramon Pires, Roseli Romero, and Rodrigo Nogueira. Juru: Legal
brazilian large language model from reputable sources. arXiv preprint arXiv:2403.18140,
2024.
[85] Sayash Kapoor and Arvind Narayanan. Leakage and the reproducibility crisis in ml-based
science. arXiv preprint arXiv:2207.07048, 2022.
[86] Taku Kudo and John Richardson. Sentencepiece: A simple and language independent subword
tokenizer and detokenizer for neural text processing. arXiv preprint arXiv:1808.06226, 2018.
[87] Alexandre Lacoste, Alexandra Luccioni, Victor Schmidt, and Thomas Dandres. Quantifying
the carbon emissions of machine learning. arXiv preprint arXiv:1910.09700, 2019.
[88] Viet Dac Lai, Chien Van Nguyen, Nghia Trung Ngo, Thuat Nguyen, Franck Dernoncourt,
Ryan A Rossi, and Thien Huu Nguyen. Okapi: Instruction-tuned large language models
in multiple languages with reinforcement learning from human feedback. arXiv preprint
arXiv:2307.16039, 2023.
[89] Celio Larcher, Marcos Piau, Paulo Finardi, Pedro Gengo, Piero Esposito, and Vinicius Caridá.
Cabrita: closing the gap for foreign languages. arXiv preprint arXiv:2308.11878, 2023.
[90] Hugo Laurençon, Lucile Saulnier, Thomas Wang, Christopher Akiki, Albert Villanova del
Moral, Teven Le Scao, Leandro Von Werra, Chenghao Mou, Eduardo González Ponferrada,
Huu Nguyen, et al. The bigscience roots corpus: A 1.6 tb composite multilingual dataset.
Advances in Neural Information Processing Systems, 35:31809–31826, 2022.
[91] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. nature, 521(7553):436–444,
2015.
[92] Quentin Lhoest, Albert Villanova del Moral, Yacine Jernite, Abhishek Thakur, Patrick von
Platen, Suraj Patil, Julien Chaumond, Mariama Drame, Julien Plu, Lewis Tunstall, Joe Davison,
Mario Šaško, Gunjan Chhablani, Bhavitvya Malik, Simon Brandeis, Teven Le Scao, Victor
Sanh, Canwen Xu, Nicolas Patry, Angelina McMillan-Major, Philipp Schmid, Sylvain Gugger,
Clément Delangue, Théo Matussière, Lysandre Debut, Stas Bekman, Pierric Cistac, Thibault
Goehringer, Victor Mustar, François Lagunas, Alexander Rush, and Thomas Wolf. Datasets: A
community library for natural language processing. In Proceedings of the 2021 Conference on
Empirical Methods in Natural Language Processing: System Demonstrations, pages 175–184,
Online and Punta Cana, Dominican Republic, November 2021. Association for Computational
Linguistics.
[93] Haonan Li, Fajri Koto, Minghao Wu, Alham Fikri Aji, and Timothy Baldwin. Bactrian-x : A
multilingual replicable instruction-following model with low-rank adaptation, 2023.
[94] Jeffrey Li, Alex Fang, Georgios Smyrnis, Maor Ivgi, Matt Jordan, Samir Gadre, Hritik
Bansal, Etash Guha, Sedrick Keh, Kushal Arora, Saurabh Garg, Rui Xin, Niklas Muennighoff,
Reinhard Heckel, Jean Mercat, Mayee Chen, Suchin Gururangan, Mitchell Wortsman, Alon
Albalak, Yonatan Bitton, Marianna Nezhurina, Amro Abbas, Cheng-Yu Hsieh, Dhruba Ghosh,
Josh Gardner, Maciej Kilian, Hanlin Zhang, Rulin Shao, Sarah Pratt, Sunny Sanyal, Gabriel
Ilharco, Giannis Daras, Kalyani Marathe, Aaron Gokaslan, Jieyu Zhang, Khyathi Chandu,
Thao Nguyen, Igor Vasiljevic, Sham Kakade, Shuran Song, Sujay Sanghavi, Fartash Faghri,
Sewoong Oh, Luke Zettlemoyer, Kyle Lo, Alaaeldin El-Nouby, Hadi Pouransari, Alexander
Toshev, Stephanie Wang, Dirk Groeneveld, Luca Soldaini, Pang Wei Koh, Jenia Jitsev, Thomas
Kollar, Alexandros G. Dimakis, Yair Carmon, Achal Dave, Ludwig Schmidt, and Vaishaal
Shankar. Datacomp-lm: In search of the next generation of training sets for language models,
2024.
[95] Shen Li, Yanli Zhao, Rohan Varma, Omkar Salpekar, Pieter Noordhuis, Teng Li, Adam Paszke,
Jeff Smith, Brian Vaughan, Pritam Damania, et al. Pytorch distributed: Experiences on
accelerating data parallel training. arXiv preprint arXiv:2006.15704, 2020.
29

--- Page 30 ---

[96] Yuanzhi Li, Sébastien Bubeck, Ronen Eldan, Allie Del Giorno, Suriya Gunasekar, and Yin Tat
Lee. Textbooks are all you need ii: phi-1.5 technical report. arXiv preprint arXiv:2309.05463,
2023.
[97] Stephanie Lin, Jacob Hilton, and Owain Evans. Truthfulqa: Measuring how models mimic
human falsehoods. arXiv preprint arXiv:2109.07958, 2021.
[98] Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu Wang, Shuohui Chen, Daniel Simig,
Myle Ott, Naman Goyal, Shruti Bhosale, Jingfei Du, et al. Few-shot learning with multilingual
language models. arXiv preprint arXiv:2112.10668, 2021.
[99] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning, 2023.
[100] Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy,
Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. Roberta: A robustly optimized bert
pretraining approach. arXiv preprint arXiv:1907.11692, 2019.
[101] Ricardo Lopes, João Magalhães, and David Semedo. Gl\’oria-a generative and open large
language model for portuguese. arXiv preprint arXiv:2402.12969, 2024.
[102] I Loshchilov. Decoupled weight decay regularization. arXiv preprint arXiv:1711.05101, 2017.
[103] Kadan Lottick, Silvia Susai, Sorelle A Friedler, and Jonathan P Wilson.
Energy usage
reports: Environmental awareness as part of algorithmic accountability.
arXiv preprint
arXiv:1911.08354, 2019.
[104] AS Luccioni, S Viguier, and AL Ligozat. Estimating the carbon footprint of bloom, a 176b
parameter language model, doi: 10.48550. arXiv preprint ARXIV.2211.02001, 2022.
[105] Louis Martin, Benjamin Muller, Pedro Javier Ortiz Suárez, Yoann Dupont, Laurent Romary,
Éric de la Clergerie, Djamé Seddah, and Benoît Sagot. CamemBERT: a tasty French language
model. In Proceedings of the 58th Annual Meeting of the Association for Computational
Linguistics, pages 7203–7219, Online, July 2020. Association for Computational Linguistics.
[106] Tomas Mikolov, Kai Chen, Greg Corrado, and Jeffrey Dean. Efficient estimation of word
representations in vector space. arXiv preprint arXiv:1301.3781, 2013.
[107] Tomáš Mikolov, Wen-tau Yih, and Geoffrey Zweig. Linguistic regularities in continuous space
word representations. In Proceedings of the 2013 conference of the north american chapter of
the association for computational linguistics: Human language technologies, pages 746–751,
2013.
[108] Ishan Misra and Laurens van der Maaten.
Self-supervised learning of pretext-invariant
representations. In Proceedings of the IEEE/CVF conference on computer vision and pattern
recognition, pages 6707–6717, 2020.
[109] Arindam Mitra, Hamed Khanpour, Corby Rosset, and Ahmed Awadallah. Orca-math: Unlock-
ing the potential of slms in grade school math. arXiv preprint arXiv:2402.14830, 2024.
[110] Chenghao Mou, Chris Ha, Kenneth Enevoldsen, and Peiyuan Liu. Chenghaomou/text-dedup:
Reference snapshot, September 2023.
[111] Niklas Muennighoff, Alexander M Rush, Boaz Barak, Teven Le Scao, Aleksandra Piktus,
Nouamane Tazi, Sampo Pyysalo, Thomas Wolf, and Colin Raffel. Scaling data-constrained
language models. arXiv preprint arXiv:2305.16264, 2023.
[112] Prakash M Nadkarni, Lucila Ohno-Machado, and Wendy W Chapman. Natural language
processing: an introduction.
Journal of the American Medical Informatics Association,
18(5):544–551, 2011.
[113] Thao Nguyen, Gabriel Ilharco, Mitchell Wortsman, Sewoong Oh, and Ludwig Schmidt. Quality
not quantity: On the interaction between dataset design and robustness of clip. Advances in
Neural Information Processing Systems, 35:21455–21469, 2022.
[114] Thuat Nguyen, Chien Van Nguyen, Viet Dac Lai, Hieu Man, Nghia Trung Ngo, Franck
Dernoncourt, Ryan A. Rossi, and Thien Huu Nguyen. Culturax: A cleaned, enormous, and
multilingual dataset for large language models in 167 languages, 2023.
[115] Joel Niklaus, Veton Matoshi, Matthias Stürmer, Ilias Chalkidis, and Daniel E Ho. Multile-
galpile: A 689gb multilingual legal corpus. arXiv preprint arXiv:2306.02069, 2023.
30

--- Page 31 ---

[116] Pedro Javier Ortiz Su’arez, Laurent Romary, and Benoit Sagot. A monolingual approach
to contextualized word embeddings for mid-resource languages. In Proceedings of the 58th
Annual Meeting of the Association for Computational Linguistics, pages 1703–1714, Online,
July 2020. Association for Computational Linguistics.
[117] Pedro Javier Ortiz Su’arez, Benoit Sagot, and Laurent Romary. Asynchronous pipelines
for processing huge corpora on medium to low resource infrastructures. Proceedings of the
Workshop on Challenges in the Management of Large Corpora (CMLC-7) 2019. Cardiff, 22nd
July 2019, pages 9 – 16, Mannheim, 2019. Leibniz-Institut f"ur Deutsche Sprache.
[118] Daniel W Otter, Julian R Medina, and Jugal K Kalita. A survey of the usages of deep learning
for natural language processing. IEEE transactions on neural networks and learning systems,
32(2):604–624, 2020.
[119] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin,
Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. Training language models
to follow instructions with human feedback. Advances in neural information processing
systems, 35:27730–27744, 2022.
[120] Arnold Overwijk, Chenyan Xiong, and Jamie Callan. Clueweb22: 10 billion web documents
with rich information. In Proceedings of the 45th International ACM SIGIR Conference on
Research and Development in Information Retrieval, pages 3360–3362, 2022.
[121] Denis Paperno, Germán Kruszewski, Angeliki Lazaridou, Quan Ngoc Pham, Raffaella
Bernardi, Sandro Pezzelle, Marco Baroni, Gemma Boleda, and Raquel Fernández. The
lambada dataset: Word prediction requiring a broad discourse context.
arXiv preprint
arXiv:1606.06031, 2016.
[122] Jupinder Parmar, Shrimai Prabhumoye, Joseph Jennings, Mostofa Patwary, Sandeep Subrama-
nian, Dan Su, Chen Zhu, Deepak Narayanan, Aastha Jhunjhunwala, Ayush Dattagupta, et al.
Nemotron-4 15b technical report. arXiv preprint arXiv:2402.16819, 2024.
[123] Adam Paszke, Sam Gross, Francisco Massa, Adam Lerer, James Bradbury, Gregory Chanan,
Trevor Killeen, Zeming Lin, Natalia Gimelshein, Luca Antiga, et al. Pytorch: An imperative
style, high-performance deep learning library. Advances in neural information processing
systems, 32, 2019.
[124] David Patterson, Joseph Gonzalez, Urs Hölzle, Quoc Le, Chen Liang, Lluis-Miquel Munguia,
Daniel Rothchild, David R So, Maud Texier, and Jeff Dean. The carbon footprint of machine
learning training will plateau, then shrink. Computer, 55(7):18–28, 2022.
[125] Guilherme Penedo, Hynek Kydlíˇcek, Loubna Ben allal, Anton Lozhkov, Margaret Mitchell,
Colin Raffel, Leandro Von Werra, and Thomas Wolf. The fineweb datasets: Decanting the
web for the finest text data at scale, 2024.
[126] Marcos Piau, Roberto Lotufo, and Rodrigo Nogueira. ptt5-v2: A closer look at continued
pretraining of t5 models for the portuguese language. arXiv preprint arXiv:2406.10806, 2024.
[127] Ramon Pires, Hugo Abonizio, Thales Rogério, and Rodrigo Nogueira. Sabi\’a: Portuguese
large language models. arXiv preprint arXiv:2304.07880, 2023.
[128] Felipe Maia Polo, Gabriel Caiaffa Floriano Mendonça, Kauê Capellato J Parreira, Lucka
Gianvechio, Peterson Cordeiro, Jonathan Batista Ferreira, Leticia Maria Paz de Lima, Antônio
Carlos do Amaral Maia, and Renato Vicente. Legalnlp–natural language processing methods
for the brazilian legal language. arXiv preprint arXiv:2110.15709, 2021.
[129] Simon JD Prince. Understanding deep learning. MIT press, 2023.
[130] Alec Radford, Jeffrey Wu, Rewon Child, David Luan, Dario Amodei, Ilya Sutskever, et al.
Language models are unsupervised multitask learners. OpenAI blog, 1(8):9, 2019.
[131] Jack W Rae, Sebastian Borgeaud, Trevor Cai, Katie Millican, Jordan Hoffmann, Francis Song,
John Aslanides, Sarah Henderson, Roman Ring, Susannah Young, et al. Scaling language
models: Methods, analysis & insights from training gopher. arXiv preprint arXiv:2112.11446,
2021.
[132] Rafael Rafailov, Archit Sharma, Eric Mitchell, Christopher D Manning, Stefano Ermon, and
Chelsea Finn. Direct preference optimization: Your language model is secretly a reward model.
Advances in Neural Information Processing Systems, 36, 2024.
31

--- Page 32 ---

[133] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena,
Yanqi Zhou, Wei Li, and Peter J Liu. Exploring the limits of transfer learning with a unified
text-to-text transformer. Journal of machine learning research, 21(140):1–67, 2020.
[134] Livy Real, Erick Fonseca, and Hugo Goncalo Oliveira. The assin 2 shared task: a quick
overview.
In International Conference on Computational Processing of the Portuguese
Language, pages 406–412. Springer, 2020.
[135] Nils Reimers and Iryna Gurevych. Sentence-bert: Sentence embeddings using siamese bert-
networks. arXiv preprint arXiv:1908.10084, 2019.
[136] João Rodrigues, Luís Gomes, João Silva, António Branco, Rodrigo Santos, Henrique Lopes
Cardoso, and Tomás Osório. Advancing neural encoding of portuguese with transformer
albertina pt. arXiv preprint arXiv:2305.06721, 2023.
[137] Rafael BM Rodrigues, Pedro IM Privatto, Gustavo José de Sousa, Rafael P Murari, Luis CS
Afonso, João P Papa, Daniel CG Pedronette, Ivan R Guilherme, Stephan R Perrout, and
Aliel F Riente. Petrobert: a domain adaptation language model for oil and gas applications
in portuguese. In International Conference on Computational Processing of the Portuguese
Language, pages 101–109. Springer, 2022.
[138] Ruan Chaves Rodrigues. Faquad-nli. https://huggingface.co/datasets/ruanchaves/
faquad-nli, 2024.
[139] Elisa Terumi Rubel Schneider, João Vitor Andrioli de Souza, Julien Knafou, Lucas ES
Oliveira, Yohan B Gumiel, Lucas FA de Oliveira, Douglas Teodoro, Emerson Cabrera Paraiso,
Claudia Moro, et al. Biobertpt: a portuguese neural language model for clinical named entity
recognition. In Proceedings of the 3rd Clinical Natural Language Processing Workshop. 19
November 2020, 2020.
[140] Henrique Santos, Vinicius Woloszyn, and Renata Vieira. Blogset-br: A brazilian portuguese
blog corpus. In Proceedings of the Eleventh International Conference on Language Resources
and Evaluation (LREC 2018), 2018.
[141] Rodrigo Santos, João Silva, Luís Gomes, João Rodrigues, and António Branco. Advancing
generative ai for portuguese with open decoder gerv\’asio pt. arXiv preprint arXiv:2402.18766,
2024.
[142] Craig W Schmidt, Varshini Reddy, Haoran Zhang, Alec Alameddine, Omri Uzan, Yuval Pinter,
and Chris Tanner. Tokenization is more than compression. arXiv preprint arXiv:2402.18376,
2024.
[143] Elisa Terumi Rubel Schneider, Joao Vitor Andrioli de Souza, Yohan Bonescki Gumiel, Clau-
dia Moro, and Emerson Cabrera Paraiso. A gpt-2 language model for biomedical texts in
portuguese. In 2021 IEEE 34th international symposium on computer-based medical systems
(CBMS), pages 474–479. IEEE, 2021.
[144] Christopher J Shallue, Jaehoon Lee, Joseph Antognini, Jascha Sohl-Dickstein, Roy Frostig,
and George E Dahl. Measuring the effects of data parallelism on neural network training.
Journal of Machine Learning Research, 20(112):1–49, 2019.
[145] Noam Shazeer. Glu variants improve transformer. arXiv preprint arXiv:2002.05202, 2020.
[146] Oleh Shliazhko, Alena Fenogenova, Maria Tikhonova, Vladislav Mikhailov, Anastasia Ko-
zlova, and Tatiana Shavrina.
mgpt: Few-shot learners go multilingual.
arXiv preprint
arXiv:2204.07580, 2022.
[147] Igor Cataneo Silveira and Denis Deratani Mauá. University entrance exam as a guiding test for
artificial intelligence. In Proceedings of the 6th Brazilian Conference on Intelligent Systems,
BRACIS, pages 426–431, 2017.
[148] Raquel Silveira, Caio Ponte, Vitor Almeida, Vládia Pinheiro, and Vasco Furtado. Legalbert-
pt: A pretrained language model for the brazilian portuguese legal domain. In Brazilian
Conference on Intelligent Systems, pages 268–282. Springer, 2023.
[149] Shivalika Singh, Freddie Vargus, Daniel Dsouza, Börje F. Karlsson, Abinaya Mahendiran,
Wei-Yin Ko, Herumb Shandilya, Jay Patel, Deividas Mataciunas, Laura OMahony, Mike
Zhang, Ramith Hettiarachchi, Joseph Wilson, Marina Machado, Luisa Souza Moura, Dominik
Krzemi´nski, Hakimeh Fadaei, Irem Ergün, Ifeoma Okoh, Aisha Alaagib, Oshan Mudannayake,
Zaid Alyafeai, Vu Minh Chien, Sebastian Ruder, Surya Guthikonda, Emad A. Alghamdi,
32

--- Page 33 ---

Sebastian Gehrmann, Niklas Muennighoff, Max Bartolo, Julia Kreutzer, Ahmet Üstün, Marzieh
Fadaee, and Sara Hooker. Aya dataset: An open-access collection for multilingual instruction
tuning, 2024.
[150] Luca Soldaini, Rodney Kinney, Akshita Bhagia, Dustin Schwenk, David Atkinson, Russell
Authur, Ben Bogin, Khyathi Chandu, Jennifer Dumas, Yanai Elazar, Valentin Hofmann,
Ananya Harsh Jha, Sachin Kumar, Li Lucy, Xinxi Lyu, Nathan Lambert, Ian Magnusson, Jacob
Morrison, Niklas Muennighoff, Aakanksha Naik, Crystal Nam, Matthew E. Peters, Abhilasha
Ravichander, Kyle Richardson, Zejiang Shen, Emma Strubell, Nishant Subramani, Oyvind
Tafjord, Pete Walsh, Luke Zettlemoyer, Noah A. Smith, Hannaneh Hajishirzi, Iz Beltagy, Dirk
Groeneveld, Jesse Dodge, and Kyle Lo. Dolma: an Open Corpus of Three Trillion Tokens for
Language Model Pretraining Research. arXiv preprint, 2024.
[151] A Willian Sousa and Marcos Didonet Del Fabro. Iudicium textum dataset uma base de textos
jurıdicos para nlp. In XXXIV Simpósio Brasileiro de Banco de Dados: Dataset Showcase
Workshop, SBBD, pages 1–11, 2019.
[152] Fábio Souza, Rodrigo Nogueira, and Roberto Lotufo. Bertimbau: pretrained bert models for
brazilian portuguese. In Intelligent Systems: 9th Brazilian Conference, BRACIS 2020, Rio
Grande, Brazil, October 20–23, 2020, Proceedings, Part I 9, pages 403–417. Springer, 2020.
[153] Nikit Srivastava, Denis Kuchelev, Tatiana Moteu Ngoli, Kshitij Shetty, Michael Roeder, Diego
Moussallem, Hamada Zahera, and Axel-Cyrille Ngonga Ngomo. Lola – an open-source
massively multilingual large language model, 2024.
[154] Emma Strubell, Ananya Ganesh, and Andrew McCallum. Energy and policy considerations
for deep learning in nlp. arXiv preprint arXiv:1906.02243, 2019.
[155] Jianlin Su, Yu Lu, Shengfeng Pan, Bo Wen, and Yunfeng Liu. Roformer: Enhanced transformer
with rotary position embedding. corr abs/2104.09864 (2021). arXiv preprint arXiv:2104.09864,
2021.
[156] Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu,
Xuyi Chen, Yanbin Zhao, Yuxiang Lu, et al. Ernie 3.0: Large-scale knowledge enhanced
pre-training for language understanding and generation. arXiv preprint arXiv:2107.02137,
2021.
[157] Ilya Sutskever, Oriol Vinyals, and Quoc V Le. Sequence to sequence learning with neural
networks. Advances in neural information processing systems, 27, 2014.
[158] Calvin Tan and Jerome Wang. 1.5-pints technical report: Pretraining in days, not months–your
language model thrives on quality data. arXiv preprint arXiv:2408.03506, 2024.
[159] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos Guestrin,
Percy Liang, and Tatsunori B Hashimoto.
Alpaca:
A strong, replicable instruction-
following model. Stanford Center for Research on Foundation Models. https://crfm. stanford.
edu/2023/03/13/alpaca. html, 3(6):7, 2023.
[160] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timo-
thée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. Llama: Open
and efficient foundation language models. arXiv preprint arXiv:2302.13971, 2023.
[161] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei,
Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open
foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.
[162] Aimee Van Wynsberghe. Sustainable ai: Ai for sustainability and the sustainability of ai. AI
and Ethics, 1(3):213–218, 2021.
[163] Francielle Vargas, Isabelle Carvalho, Fabiana Rodrigues de Góes, Thiago Pardo, and Fabrício
Benevenuto. Hatebr: A large expert annotated corpus of brazilian instagram comments for
offensive language and hate speech detection. In Proceedings of the Thirteenth Language
Resources and Evaluation Conference, pages 7174–7183, 2022.
[164] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N Gomez,
Łukasz Kaiser, and Illia Polosukhin. Attention is all you need. Advances in neural information
processing systems, 30, 2017.
33

--- Page 34 ---

[165] Charles FO Viegas, Bruno C Costa, and Renato P Ishii. Jurisbert: a new approach that converts
a classification corpus into an sts one. In International Conference on Computational Science
and Its Applications, pages 349–365. Springer, 2023.
[166] Antti Virtanen, Jenna Kanerva, Rami Ilo, Jouni Luoma, Juhani Luotolahti, Tapio Salakoski,
Filip Ginter, and Sampo Pyysalo. Multilingual is not enough: Bert for finnish. arXiv preprint
arXiv:1912.07076, 2019.
[167] Leandro von Werra, Younes Belkada, Lewis Tunstall, Edward Beeching, Tristan Thrush,
Nathan Lambert, Shengyi Huang, Kashif Rasul, and Quentin Gallouédec. Trl: Transformer
reinforcement learning. https://github.com/huggingface/trl, 2020.
[168] Jorge A Wagner Filho, Rodrigo Wilkens, Marco Idiart, and Aline Villavicencio. The brwac
corpus: A new open resource for brazilian portuguese. In Proceedings of the Eleventh
International Conference on Language Resources and Evaluation (LREC 2018), 2018.
[169] Ben Wang and Aran Komatsuzaki. GPT-J-6B: A 6 Billion Parameter Autoregressive Language
Model. https://github.com/kingoflolz/mesh-transformer-jax, 2021.
[170] Weizhi Wang, Khalil Mrini, Linjie Yang, Sateesh Kumar, Yu Tian, Xifeng Yan, and Heng
Wang. Finetuned multimodal language models are high-quality image-text data filters. arXiv
preprint arXiv:2403.02677, 2024.
[171] Xiangpeng Wei, Haoran Wei, Huan Lin, Tianhao Li, Pei Zhang, Xingzhang Ren, Mei Li,
Yu Wan, Zhiwei Cao, Binbin Xie, et al. Polylm: An open source polyglot large language
model. arXiv preprint arXiv:2307.06018, 2023.
[172] Guillaume Wenzek, Marie-Anne Lachaux, Alexis Conneau, Vishrav Chaudhary, Francisco
Guzmán, Armand Joulin, and Edouard Grave. CCNet: Extracting high quality monolingual
datasets from web crawl data. In Proceedings of the 12th Language Resources and Evaluation
Conference, pages 4003–4012, Marseille, France, May 2020. European Language Resources
Association.
[173] Wikimedia Foundation. Wikimedia Downloads. https://dumps.wikimedia.org, 2024.
[174] BigScience Workshop, Teven Le Scao, Angela Fan, Christopher Akiki, Ellie Pavlick, Suzana
Ili´c, Daniel Hesslow, Roman Castagné, Alexandra Sasha Luccioni, François Yvon, et al. Bloom:
A 176b-parameter open-access multilingual language model. arXiv preprint arXiv:2211.05100,
2022.
[175] Fuzhao Xue, Yao Fu, Wangchunshu Zhou, Zangwei Zheng, and Yang You. To repeat or not to
repeat: Insights from scaling llm under token-crisis. arXiv preprint arXiv:2305.13230, 2023.
[176] Fuzhao Xue, Zian Zheng, Yao Fu, Jinjie Ni, Zangwei Zheng, Wangchunshu Zhou, and Yang
You. Openmoe: An early effort on open mixture-of-experts language models. arXiv preprint
arXiv:2402.01739, 2024.
[177] Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya Siddhant,
Aditya Barua, and Colin Raffel. mt5: A massively multilingual pre-trained text-to-text
transformer. arXiv preprint arXiv:2010.11934, 2020.
[178] Alex Young, Bei Chen, Chao Li, Chengen Huang, Ge Zhang, Guanwei Zhang, Heng Li,
Jiangcheng Zhu, Jianqun Chen, Jing Chang, et al. Yi: Open foundation models by 01. ai. arXiv
preprint arXiv:2403.04652, 2024.
[179] Rowan Zellers, Ari Holtzman, Yonatan Bisk, Ali Farhadi, and Yejin Choi. Hellaswag: Can a
machine really finish your sentence? arXiv preprint arXiv:1905.07830, 2019.
[180] Biao Zhang and Rico Sennrich. Root mean square layer normalization. Advances in Neural
Information Processing Systems, 32, 2019.
[181] Peiyuan Zhang, Guangtao Zeng, Tianduo Wang, and Wei Lu. Tinyllama: An open-source
small language model. arXiv preprint arXiv:2401.02385, 2024.
[182] Susan Zhang, Stephen Roller, Naman Goyal, Mikel Artetxe, Moya Chen, Shuohui Chen,
Christopher Dewan, Mona Diab, Xian Li, Xi Victoria Lin, et al. Opt: Open pre-trained
transformer language models. arXiv preprint arXiv:2205.01068, 2022.
[183] Ahmet Üstün, Viraat Aryabumi, Zheng-Xin Yong, Wei-Yin Ko, Daniel D’souza, Gbemileke
Onilude, Neel Bhandari, Shivalika Singh, Hui-Lee Ooi, Amr Kayid, Freddie Vargus, Phil
Blunsom, Shayne Longpre, Niklas Muennighoff, Marzieh Fadaee, Julia Kreutzer, and Sara
Hooker. Aya model: An instruction finetuned open-access multilingual language model, 2024.
34

```
