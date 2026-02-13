---
title: "2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented - PDF Extract"
source_pdf: "2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented.pdf"
pages: 26
extracted_at: "2026-02-13T09:15:43.481344"
---

# PDF Extract: 2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented

**Source PDF:** 2024-Mandikal-Ancient Wisdom Modern Tools Exploring Retrieval-Augmented.pdf
**Total Pages:** 26

---

## Content

```
--- Page 1 ---

Ancient Wisdom, Modern Tools: Exploring Retrieval-Augmented
LLMs for Ancient Indian Philosophy
Priyanka Mandikal
Department of Computer Science, UT Austin
mandikal@utexas.edu
Oral teachings
LLMs
Computers and 
the Internet
Printing press
Hand-written 
manuscripts
Time
Knowledge distribution & proliferation
Technological advancements
Figure 1: The dissemination of knowledge through the ages. Over time, methods of storing and transmitting knowledge
have evolved from oral teachings to computers and the internet, signiﬁcantly increasing the distribution and proliferation of
human knowledge. The emerging LLM technology represents a new paradigm shift in this process.
Abstract
LLMs have revolutionized the landscape of
information retrieval and knowledge dissem-
ination.
However, their application in spe-
cialized areas is often hindered by factual in-
accuracies and hallucinations, especially in
long-tail knowledge distributions. We explore
the potential of retrieval-augmented generation
(RAG) models for long-form question answer-
ing (LFQA) in a specialized knowledge domain.
We present VedantaNY-10M, a dataset curated
from extensive public discourses on the ancient
Indian philosophy of Advaita Vedanta. We de-
velop and benchmark a RAG model against
a standard, non-RAG LLM, focusing on tran-
scription, retrieval, and generation performance.
Human evaluations by computational linguists
and domain experts show that the RAG model
signiﬁcantly outperforms the standard model
in producing factual and comprehensive re-
sponses having fewer hallucinations. In ad-
dition, a keyword-based hybrid retriever that
emphasizes unique low-frequency terms further
improves results. Our study provides insights
into effectively integrating modern large lan-
guage models with ancient knowledge systems.
Proceedings of the 1st Machine Learning for Ancient Lan-
guages Workshop, Association for Computational Linguistics
(ACL) 2024. Dataset, code, and evaluation is available at:
https://sites.google.com/view/vedantany-10m
ॐकेनेषितंपततिप्रेषितंमनः|| 1.1 ||
यन्मनसानमनुतेयेनाहुर्मनोमतम्।तदेवब्रह्मत्वंविद्धिनेदं
यदिदमुपासते|| 1.6 ||
"By whom willed and directed, does the mind alight
upon its objects?"
"What one cannot comprehend with the mind, but by
which they say the mind comprehends, know that alone
to be Brahman, not this which people worship here."
– Kena Upanishad, >3000 B.C.E.
1
Introduction
Answer-seeking has been at the heart of human
civilization. Humans have climbed mountains and
crossed oceans in search of answers to the greatest
questions concerning their own existence. Over
time, ancient wisdom has travelled from the silent
solitude of mountain caves and forest hermitages
into the busy cities and plains of the world. Tech-
nology has played a major role in this transmission,
signiﬁcantly increasing the distribution and prolif-
eration of human knowledge. In recent times, large
language models (LLMs) trained on large swathes
of the internet have emerged as de-facto question-
answering machines. Recent studies on the societal
impact of LLMs (Malhotra, 2021; Yiu et al., 2023)
highlight their growing signiﬁcance as cultural tech-
nologies. Analogous to earlier technologies like
writing, print, and the internet, the power of LLMs
can be harnessed meaningfully to preserve and dis-
seminate human knowledge (Fig. 1).

--- Page 2 ---

Generic LLMs have proven to be highly effective
for broad knowledge domains. However, they often
struggle in niche and less popular areas, encounter-
ing issues such as factual inaccuracies and halluci-
nations in long-tail knowledge distributions (Kand-
pal et al., 2023; Mallen et al., 2023). Moreover,
their inability to verify responses against authen-
tic sources is particularly problematic in these do-
mains, where LLMs can generate highly inaccu-
rate answers with unwarranted conﬁdence (Kand-
pal et al., 2023; Menick et al., 2022). In response
to these limitations, there has been growing inter-
est in retrieval-augmented generation (RAG) mod-
els (Karpukhin et al., 2020; Lewis et al., 2020b;
Izacard et al., 2022; Ram et al., 2023). These mod-
els integrate external datastores to retrieve relevant
knowledge and incorporate it into LLMs, demon-
strating higher factual accuracy and reduced hallu-
cinations compared to conventional LLMs (Shuster
et al., 2021; Borgeaud et al., 2022). Updating these
external datastores with new information is also
more efﬁcient and cost-effective than retraining
LLMs. In this vein, we argue that RAG models
show immense potential for enhancing study in un-
conventional, niche knowledge domains that are
often underrepresented in pre-training data. Their
ability to provide veriﬁed, authentic sources when
answering questions is particularly advantageous
for end-users.
In this work, we develop and evaluate a RAG-
based language model specialized in the ancient
Indian philosophy of Advaita Vedanta (Upan-
ishads, >3000 B.C.E.; Bhagavad Gita, 3000 B.C.E.;
Shankaracharya, 700 C.E.). To ensure that the
LLM has not been previously exposed to the source
material, we construct VedantaNY-10M, a custom
philosophy dataset comprising transcripts of over
750 hours of public discourses on YouTube from
Vedanta Society of New York. We evaluate stan-
dard non-RAG and RAG models on this domain
and ﬁnd that RAG models perform signiﬁcantly
better. However, they still encounter issues such as
irrelevant retrievals, sub-optimal retrieval passage
length, and retrieval-induced hallucinations. In
early attempts to mitigate some of these issues, we
ﬁnd that traditional sparse retrievers have a unique
advantage over dense retrievers in niche domains
having speciﬁc terminology—Sanskrit terms in our
case. Consequently, we propose a keyword-based
hybrid retriever that effectively combines sparse
and dense embeddings to upsample low-frequency
or domain-speciﬁc terms.
We conduct an extensive evaluation comprising
both automatic metrics and human evaluation by
computational linguists and domain experts. The
models are evaluated along three dimensions: tran-
scription, retrieval, and generation. Our ﬁndings
are twofold. First, RAG LLMs signiﬁcantly out-
perform standard non-RAG LLMs along all axes,
offering more factual, comprehensive, and speciﬁc
responses while minimizing hallucinations, with an
81% preference rate. Second, the keyword-based
hybrid RAG model further outperforms the stan-
dard deep-embedding based RAG model in both au-
tomatic and human evaluations. Our study also in-
cludes detailed long-form responses from the eval-
uators, with domain experts speciﬁcally indicating
the likelihood of using such LLMs to supplement
their daily studies. Our work contributes to the
broader understanding of how emerging technolo-
gies can continue the legacy of knowledge preser-
vation and dissemination in the digital age.
2
Related Work
Language models for ancient texts
Sommer-
schield et al. (2023) recently conducted a thorough
survey of machine learning techniques applied to
the study and restoration of ancient texts. Span-
ning digitization (Narang et al., 2019; Moustafa
et al., 2022), restoration (Assael et al., 2022), attri-
bution (Bogacz and Mara, 2020; Paparigopoulou
et al., 2022) and representation learning (Bamman
and Burns, 2020), a wide range of use cases have
beneﬁtted from the application of machine learning
to study ancient texts. Recently, Lugli et al. (2022)
released a digital corpus of romanized Buddhist
Sanskrit texts, training and evaluating embedding
models such as BERT and GPT-2. However, the
use of LLMs as a question-answering tool to en-
hance understanding of ancient esoteric knowledge
systems has not yet been systematically studied. To
the best of our knowledge, ours is the ﬁrst work
that studies the effects of RAG models in the niche
knowledge domain of ancient Indian philosophy.
Retrieval-Augmented LMs.
In current LLM
research, retrieval augmented generation models
(RAGs) are gaining popularity (Izacard et al.,
2022; Ram et al., 2023; Khandelwal et al., 2020;
Borgeaud et al., 2022; Menick et al., 2022). A
key area of development in RAGs has been their
architecture. Early approaches involved ﬁnetun-
ing the language model on open-domain question-
answering before deployment. MLM approaches

--- Page 3 ---

such as REALM (Guu et al., 2020) introduced a
two-stage process combining retrieval and read-
ing, while DPR (Karpukhin et al., 2020) fo-
cused on pipeline training for question answer-
ing. RAG (Lewis et al., 2020b) used a genera-
tive approach with no explicit language modeling.
Very recently, in-context RALM (Ram et al., 2023)
showed that retrieved passages can be used to aug-
ment the input to the LLM in-context without any
ﬁne-tuning like prior work. In this work, we adopt
the in-context retrieval augmented methodology
similar to (Ram et al., 2023), where neither the
retriever nor the generator is ﬁne-tuned. This also
enables us to use any combination of retrieval and
generation models that best suits our application.
Applications of RAGs. The applications of RAGs
are diverse and evolving. ATLAS (Izacard et al.,
2022) and GopherCite (Menick et al., 2022) have
shown how ﬁne-tuning and reinforcement learning
from human feedback can enhance RAGs’ ability
to generate veriﬁable answers from reliable sources.
Prompting techniques have also seen innovation.
kNNPrompt (Shi et al., 2022) extended kNN-LM
for zero or few-shot classiﬁcation tasks, and re-
trieval in-context approaches (Ram et al., 2023; Shi
et al., 2023) have proven effective in utilizing re-
trieval at the input stage. Retrieval-LMs have been
shown to be particularly valuable for handling long-
tail or less frequent entities (Kandpal et al., 2023;
Mallen et al., 2023), updating knowledge (Izac-
ard et al., 2022), improving parameter efﬁciency
(Izacard et al., 2022; Mallen et al., 2023), and en-
hancing veriﬁability (Bohnet et al., 2022), making
them increasingly relevant in a wide range of appli-
cations. In our work, we examine the application
of RAGs for long-tail knowledge, conducting an
extensive study on a niche knowledge domain of
ancient Indian philosophy.
Evaluation of LFQA
The ﬁeld of long-form
question answering (LFQA) is an emerging area
of active research (Krishna et al., 2021; Nakano
et al., 2021; Xu et al., 2023). Recently, Xu et al.
(2023) conducted a thorough examination of vari-
ous LFQA metrics, encompassing both human and
automatic evaluation methods, and found that ex-
isting automatic metrics don’t always align with
human preferences. On their suggestion, we place
special emphasis on conducting an extensive hu-
man evaluation utilizing the expertise of experi-
enced computational linguists and domain experts.
Figure 2: Sanskrit terms in VedantaNY-10M. Fre-
quently occurring Sanskrit terms in the corpus.
3
The VedantaNY-10M Dataset
We ﬁrst describe our niche domain dataset creation
process. The custom dataset for our study needs
to satisfy the following requirements: (1) Niche:
Must be a specialized niche knowledge domain
within the LLM’s long-tail distribution. (2) Novel:
The LLM must not have previously encountered the
source material. (3) Authentic: The dataset should
be authentic and representative of the knowledge
domain. (4) Domain experts: should be available
to evaluate the model’s effectiveness and utility.
Knowledge domain. To satisfy the ﬁrst require-
ment, we choose our domain to be the niche knowl-
edge system of Advaita Vedanta, a 1300-year-old
Indian school of philosophy (Shankaracharya, 700
C.E.) based on the Upanishads (>3000 B.C.E.),
Bhagavad Gita (3000 B.C.E.) and Brahmasutras
(3000 B.C.E.)1. It is a contemplative knowledge
tradition that employs a host of diverse tools and
techniques including analytical reasoning, logic,
linguistic paradoxes, metaphors and analogies to
enable the seeker to enquire into their real nature.
Although a niche domain, this knowledge system
has been continuously studied and rigorously devel-
oped over millenia, offering a rich and structured
niche for the purposes of our study. Being a living
tradition, it offers the additional advantage of pro-
viding experienced domain experts to evaluate the
language models in this work.
Composition of the dataset.
Considering the
outlined criteria, we introduce VedantaNY-10M,
a curated philosophy dataset of public discourses.
1Currently there exists no consensus on accurately dating
these ancient scriptures. The Upanishads (which are a part of
the Vedas) have been passed on orally for millennia and are
traditionally not given a historic date. However, they seem to
have been compiled and systematically organized sometime
around 3000 B.C.E. by Vyasa. Likewise, the time period
of Adi Shankaracharya also varies and he is usually placed
between 450 B.C.E to 700 C.E.

--- Page 4 ---

To maintain authenticity while ensuring that the
LLM hasn’t previously been exposed to the source
material, we curate our dataset from a collection of
YouTube videos on Advaita Vedanta, sourced from
the Vedanta Society of New York. It contains 10M
tokens and encompasses over 750 hours of philo-
sophical discourses by Swami Sarvapriyananda, a
learned monk of the Ramakrishna Order. These
discourses provide a rich and comprehensive expo-
sition of the principles of Advaita Vedanta, making
them an invaluable resource for our research.
Languages and scripts.
The dataset primarily
features content in English, accounting for approx-
imately 97% of the total material. Sanskrit, the
classical language of Indian philosophical litera-
ture, constitutes around 3% of the dataset. The
Sanskrit terms are transliterated into the Roman
script. To accommodate the linguistic diversity
and the speciﬁc needs of the study, the dataset in-
cludes words in both English and Sanskrit, without
substituting the Sanskrit terms with any English
translations. Translating ancient Sanskrit techni-
cal terms having considerably nuanced deﬁnitions
into English is a non-trivial problem (Malhotra and
Babaji, 2020). Hence, our dual-language approach
ensures that the Sanskrit terms and concepts are
accurately represented and accessible, thereby en-
hancing the authenticity of our research material.
Frequently occurring Sanskrit terms in the corpus
are shown in Fig. 2. For excerpts from passages,
please refer to Appendix Table 2.
4
In-context RAG for niche domains
We now discuss the methodology adopted to build
an in-context retrieval augmented chatbot from the
custom dataset described above.
We ﬁrst deﬁne a generic chatbot Cg that does
not use retrieval as follows: Cg : q →ag where q
is the user query and ag is the answer generated by
the chatbot. Now, let Dt represent the textual data
corpus from our knowledge domain and R be the
retriever. Our goal is to build a retrieval-augmented
generation chatbot Cr : q × R(Dt, q) →ar that
will generate answer ar for the query by retrieving
relevant context from Dt using R. An overview of
our approach is illustrated in Fig. 3. We ﬁrst build
Dt from 765 hours of public discourses on Advaita
Vedanta introduced in Sec. 3. When deployed, the
system processes q by ﬁrst using retriever R to
identify the top-k most relevant passages P from
Dt using a similarity metric. Subsequently, a large
language model (LLM) is prompted with both the
query and the retrieved passages in-context, follow-
ing Ram et al. (2023), to generate a contextually
relevant response.
We now describe each of the components in de-
tail. We follow a four-stage process as follows:
Transcription. We ﬁrst need to create a dense tex-
tual corpus targeted at our niche domain. Since our
dataset consists of YouTube videos, we ﬁrst employ
a transcription model to transcribe the audio into
text. Our video corpus Dv consists of 612 videos to-
taling 765 hours of content, with an average length
of 1.25 hours per video. We extract audio content
from Dv and transcribe it using OpenAI’s Whisper
large-v2 model (Radford et al., 2023). This step
converts the spoken discourses into a transcribed
textual corpus Dt consisting of 10M tokens in total.
Since Whisper is a multi-lingual model, it has the
capacity to support the dual-language nature of our
dataset. We evaluate the transcription quality of
Whisper in Sec. C.1.
Datastore creation.
The transcribed text in Dt
is then segmented into shorter chunks called pas-
sages P, consisting of 1500 characters each. These
chunks are then processed by a deep embedder to
produce deep embedding vectors zdense. These em-
bedded chunks are stored in a vector database Dz.
Ultimately, we store approximately 25,000 passage
embeddings z ∈Dz, each representing a discrete
chunk of the philosophical discourse in Dt.
Retrieval. To perform retrieval-augmented gen-
eration, we ﬁrst need to build a retrieval system
R : Dz × q →P that retrieves contextually rel-
evant textual passages P from Dt given Dz and
q.
The retriever performs the following opera-
tion: P = Dt[argTop-kz∈Dzsim(q, z)], where
we use cosine similarity as the similarity met-
ric. Standard RAG models employ state-of-the-
art deep embedders to encode documents and re-
trieve them during inference. However, these se-
mantic embeddings can struggle to disambiguate
between speciﬁc niche terminology in custom do-
mains (Mandikal and Mooney, 2024). This can be
particularly problematic in datasets having long-tail
distributions such as ours. In addition, retrieved
ﬁxed-length passages are sub-optimal. Short in-
complete contexts can be particularly damaging for
LFQA, while longer contexts can contain unnec-
essary information that can confuse the generation
model. To mitigate these two issues, we experi-
ment with two key changes: (1) a keyword-based

--- Page 5 ---

Query
Answer
Hybrid 
Retrieval:
Deep + Sparse
Datastore 
Prompt
Passage 1
Passage 2
Passage k
Retriever
Chatbot
LLM
Keyword 
extraction
Context
Refiner
Figure 3: Overview of the RAG model. We present VedantaNY-10M, a dataset derived from over 750 hours of
public discourses on the ancient Indian philosophy of Advaita Vedanta, and build a retrieval-augmented generation
(RAG) chatbot for this knowledge domain. At deployment, given a query q, the retriever R ﬁrst retrieves the top-k
most relevant passages P from the datastore using a hybrid keyword-based retriever. It then reﬁnes this retrieved
context using a keyword-based context reshaper to adjust the passage length. Finally, an LLM is prompted with the
query and the reﬁned passages in-context. We conduct an extensive evaluation with computational linguists and
domain experts to assess the model’s real-world utility and identify challenges.
hybrid retriever to focus on unique low-frequency
words, and (2) a context-reﬁner to meaningfully
shorten or expand retrieved context.
1. Keyword-based retrieval. To emphasize the
importance of key terminology, we ﬁrst employ
keyword extraction and named-entity recogni-
tion techniques on the query q to extract im-
portant keywords κ. During retrieval, we advo-
cate for a hybrid model combining both deep
embeddings as well as sparse vector space em-
beddings. We encode the full query in the deep
embedder and assign a higher importance to
keyphrases in the sparse embedder. The idea
is to have the sparse model retrieve domain-
speciﬁc specialized terms that might otherwise
be missed by the deep model. Our hybrid
model uses a simple weighted combination of
the query-document similarities in the sparse
and dense embedding spaces. Speciﬁcally, we
score a document D for query q and keywords
κ using the ranking function:
Shybrid(D, q) =λ Sim
 zd(D), zd(q)

+
(1 −λ) Sim
 zs(D), zs(κ)

(1)
where zd and zs denotes the dense and sparse
embedding functions and Sim is cosine simi-
larity measuring the angle between such vec-
tor embedddings. In our experiments, we set
λ = 0.2. Amongst the top-n retrieved pas-
sages, we choose k passages containing the
maximum number of unique keywords.
2. Keyword-based context reﬁnement.
Fur-
thermore, we reﬁne our retrieved passages
by leveraging the extracted keywords using
a heuristic-based reﬁnement operation to pro-
duce P ′ = Ref(P, κ). For extension, we ex-
pand the selected passage to include one pre-
ceding and one succeeding passage, and ﬁnd
the ﬁrst and last occurrence of the extracted
keywords. Next, we trim the expanded context
from the ﬁrst occurrence to the last. This can
either expand or shorten the original passage
depending on the placement of keywords. This
ensures that retrieved context contains relevant
information for the generation model.
Generation. For answer generation, we construct
prompt p from the query q and the retrieved pas-
sages (P ′
1, P ′
2, ..., P ′
k) ∈P in context. Finally, we
invoke the chatbot Cr to synthesize an answer ar
from the constructed prompt. For an example of
the constructed RAG bot prompt, please refer to
Fig. 5. This four-stage process produces a retrieval-

--- Page 6 ---

augmented chatbot that can generate contextually
relevant responses for queries in our niche domain.
Implementation Details. For embedding and gen-
eration, we experiment with both closed and open
source language models. For RAG vs non-RAG
comparison, we use OpenAI’s text-embedding-
ada-002 model (Brown et al.) as the embedder
and GPT-4-turbo (OpenAI, 2023) as the LLM for
both Cr and Cg. For comparing RAG model vari-
ants, we use the open source nomic-embed-text-
v1 (Nussbaum et al., 2024) as our deep embedder
and Mixtral-8x7B-Instruct-v0.1 (Jiang et al., 2024)
as our generation model. For keyword extraction,
we use an ensemble of different models including
OpenKP (Xiong et al., 2019), KeyBERT (Groo-
tendorst, 2020) and SpanMarker (Aarsen, 2020).
We experimented with using language models such
as ChatGPT for keyword extraction, but the re-
sults were very poor as also corroborated in Song
et al. (2024).
For further implementation de-
tails of the eval metrics, see Appendix Sec. A.
The VedantaNY-10M dataset, code and evalua-
tion is publicly available at https://github.com/
priyankamandikal/vedantany-10m.
5
Evaluation
We now evaluate the model along two axes: auto-
matic evaluation metrics and a human evaluation
survey. To ensure a broad and comprehensive eval-
uation, we categorize the questions into ﬁve distinct
types, each designed to test different aspects of the
model’s capabilities:
1. Anecdotal: Generate responses based on sto-
ries and anecdotes narrated by the speaker in
the discourses.
2. Comparative: Analyze and compare differ-
ent concepts, philosophies, or texts. This cate-
gory tests the model’s analytical skills and its
ability to draw parallels and distinctions.
3. Reasoning Require logical reasoning, critical
thinking, and the application of principles to
new scenarios.
4. Scriptural: Test the model’s ability to ref-
erence, interpret, and explain passages from
religious or philosophical texts.
5. Terminology: Probe the model’s understand-
ing of speciﬁc technical terms and concepts.
For a sample set of questions across the above
ﬁve categories, please refer to Appendix Table 4.
5.1
Automatic Evaluation
Inspired by Xu et al. (2023), we conduct an exten-
sive automatic evaluation of the two RAG models
on our evaluation set. We describe each metric
type below and provide implementation details in
Appendix Sec. A. Due to the lack of gold answers,
we are unable to report reference-based metrics.
Answer-only metrics:
We assess features like
ﬂuency and coherence by analyzing responses with
speciﬁc metrics: (1) Self-BLEU (Zhu et al., 2018)
for text diversity, where higher scores suggest less
diversity, applied in open-ended text generation; (2)
GPT-2 perplexity for textual ﬂuency, used in prior
studies on constrained generation. We also consider
(3) Word and (4) Sentence counts as length-based
metrics, owing to their signiﬁcant inﬂuence on hu-
man preferences (Sun et al., 2019; Liu et al., 2022;
Xu et al., 2023).
(Question, answer) metric: To ensure answers
are relevant to the posed questions, we model
p(q|a) for ranking responses with RankGen (Kr-
ishna et al., 2022). Leveraging the T5-XXL ar-
chitecture, this encoder is specially trained via
contrastive learning to evaluate model generations
based on their relevance to a given preﬁx, in this
context, the question. A higher RankGen score in-
dicates a stronger alignment between the question
and the answer, serving as a measure of relevance.
(Answer, evidence) metric: A key challenge in
LFQA is assessing answer correctness without ded-
icated factuality metrics, akin to summarization’s
faithfulness. We apply QAFactEval (Fabbri et al.,
2022), originally for summarization, to LFQA by
considering the answer as a summary and evidence
documents as the source. Answers deviating from
source content, through hallucinations or external
knowledge, will score lower on this metric.
5.2
Human Evaluation
We have three experienced domain experts eval-
uate the models across the ﬁve categories. Each
of these experts is closely associated with Vedanta
Society of New York, and has extensively studied
the philosophy in question for up to a decade on
average, being well-versed with domain-speciﬁc
terminology and conceptual analysis. We conduct
the human survey along two dimensions: retrieval
and generation. For retrieval, we evaluate relevance
and completeness, and for generation we evaluate
factual correctness and completeness. In addition,
we ask the reviewers to provide free-form justiﬁ-

--- Page 7 ---

Generation
Transcription
Retrieval
Hallucinations
Outside Knowledge
Figure 4: Human evaluation: RAG vs non-RAG. Both transcription and retrieval performance receive high
scores from the evaluators. For generation, the RAG model outperforms the generic model across various metrics,
particularly in factuality, completeness and speciﬁcity, while being marginally lower in ease of understanding.
cation for their choices, which proves to be very
useful in analyzing the two models.
Relevance:
Deﬁned as the relevance of the re-
trieved passages to the user query, this metric is
scored on a scale from 1 to 5 (1 = Not at all rele-
vant, 5 = Extremely relevant).
Correctness:
Factual accuracy of the generated
answer (1 = Inaccurate, 5 = No inaccuracies)
Completeness:
Measures if the retrieved passage
and generated answer comprehensively cover all
parts of the query (1 = Not at all comprehensive -
misses crucial points, 5 = Very comprehensive).
5.3
Results: RAG vs Non-RAG
We ﬁrst conduct a human evaluation survey with 5
computational linguists and 3 domain experts on
RAG vs non-RAG models. In the evaluation of the
generation capabilities of our models, we consider
ﬁve metrics: factuality, completeness, speciﬁcity,
ease of understanding, and faithfulness. The per-
formance of the RAG model is compared against a
baseline non-RAG model across these dimensions
in Fig. 4. The RAG model substantially outper-
forms the non-RAG model across various metrics,
particularly in factuality, completeness and speci-
ﬁcity, while being marginally lower in ease of un-
derstanding. Sample responses in Figs. 7-11.
5.4
Results: Standard RAG vs
Keyword-based RAG
We report results in Table 1. The keyword based
RAG model shows strong improvement across all
automatic metrics while signiﬁcantly outperform-
ing the standard model in the human evaluation.
Amongst the answer-only metrics, the model tends
to produce longer, more comprehensive answers
(indicated by longer length), which are more co-
herent (lower perplexity). The question-answer
RankGen metric (Krishna et al., 2022) evaluates
the probability of the answer given the question. A
higher score for the model suggests more relevant
answers to the question. Most notably, the keyword
model does very well on QAFactEval (Fabbri et al.,
2022), which evaluates faithfulness by comparing
answers from the summary (in our case, the an-
swer) and the evidence (retrievals). A higher score
indicates greater faithfulness of the answer to re-
trieved passages, indicating fewer hallucinations
and reliance on outside knowledge.
For the human evaluation in Table 1, we report
scores normalized between 0 to 1. A relevance
rating of 0.82 for keyword-based RAG vs 0.59
for standard RAG indicates a strong alignment be-
tween the retrieved content and the users’ queries
for our model, demonstrating the efﬁcacy of the
retrieval process. Conversely, the standard model

--- Page 8 ---

Category
Mean
Anecdotal
Comparative
Reasoning
Scriptural
Terminology
RAG Model
M1/M2
M1/M2
M1/M2
M1/M2
M1/M2
M1/M2
Automatic metrics
Answer-only
GPT2-PPL ↓
16.6/15.3
16.6/16.6
16.9/15.7
13.9/11.9
14.2/14.7
21.5/17.7
Self-bleu ↓
0.12/0.13
0.11/0.05
0.10/0.06
0.15/0.27
0.13/0.16
0.09/0.14
# Words ↑
196/227
189/189
174/206
218/282
225/243
216/261
# Sentences ↑
9.0/10.1
8.2/7.6
7.8/9.4
9.6/11.8
10.0/10.6
9.4/11.0
(Question, answer)
RankGen ↑
0.46/0.48
0.42/0.52
0.44/0.47
0.41/0.43
0.51/0.52
0.52/0.46
(Answer, retrievals)
QAFactEval ↑
1.36/1.60
1.01/1.14
1.53/1.94
1.18/1.61
1.52/1.36
1.56/1.95
Human evaluation
Retrieval
Relevance ↑
0.59/0.82
0.41/0.88
0.79/0.85
0.73/0.83
0.48/0.73
0.55/0.81
Completeness ↑
0.52/0.79
0.41/0.86
0.72/0.79
0.57/0.83
0.37/0.68
0.52/0.79
Answer
Correctness ↑
0.61/0.86
0.40/0.89
0.81/0.88
0.71/0.85
0.52/0.81
0.63/0.89
Completeness ↑
0.58/0.85
0.42/0.92
0.80/0.85
0.72/0.81
0.49/0.77
0.63/0.91
Table 1: Automatic and human evaluation: standard RAG (M1) vs keyword-based RAG (M2). We report both
automatic and human evaluation metrics calculated on 25 triplets of {question, answer, retrievals} across 5 different
question categories. The key-word based RAG model shows strong improvement across all automatic metrics while
signiﬁcantly outperforming the standard model in the human evaluation.
sometimes fails to disambiguate unique terminol-
ogy and retrieves incorrect passages (see Fig. 12).
In assessing the accuracy of the generated an-
swer, the keyword-based RAG model signiﬁcantly
outperforms the standard model, indicating better
alignment with veriﬁable facts. Fig. 13 shows a fac-
tually inaccurate response from the generic model.
The keyword model achieves higher completeness
scores for both the retrieval and generation. Sample
responses are shown in Figs. 12-16.
6
Challenges
The evaluation in Sec. 5 shows that the RAG model
provides responses that are not only more aligned
with the source material but are also more compre-
hensive, speciﬁc, and user-friendly compared to the
responses generated by the generic language model.
In this section, we discuss the challenges we en-
countered while building the retrieval-augmented
chatbot for the niche knowledge domain of ancient
Indian philosophy introduced in this work.
Transcription. Our requirement of using a niche
data domain having long-tail knowledge precludes
the use of source material that the LLM has previ-
ously been exposed to. To ensure this, we construct
a textual corpus that is derived from automated tran-
scripts of YouTube discourses. These transcripts
can sometimes contain errors such as missing punc-
tuations, incorrect transcriptions, and translitera-
tions of Sanskrit terms. A sample of such errors is
shown in Appendix Table 3. A proofreading mech-
anism and/or improved transcription models can
help alleviate these issues to a large extent.
Spoken vs written language.
Unlike tradi-
tional textual corpora that are compiled from writ-
ten sources, our dataset is derived from spoken
discourses. Spoken language is often more ver-
bose and less structured than written text, with
the speaker frequently jumping between concepts
mid-sentence. This unstructured nature of the text
can be unfamiliar for a language model trained ex-
tensively on written text. A peculiar failure case
arising from this issue is shown in Appendix Fig. 6.
This can be addressed by converting the spoken
text into a more structured prose format with the
help of well-crafted prompts to LLMs, followed by
human proofreading.
Context length.
The passages retrieved in the
standard model are of a ﬁxed length and can some-
times be too short for many queries, especially for
long-form answering. For instance, the retrieved
passage may include a snippet from the middle of
the full context, leading to incomplete or incoherent
chatbot responses (Fig. 11). This prompted us to
employ a keyword-based context-expansion mech-
anism to provide a more complete context. While

--- Page 9 ---

this results in much better answer generation, the
retrieved passage may contain too much informa-
tion, making it difﬁcult for the generator to reason
effectively. Moreover, the increase in the number
of tokens increases processing time. Future work
can explore more advanced retrieval models capa-
ble of handling longer contexts and summarizing
them effectively before input to the LLM.
Retrieval-induced hallucinations.
There are
scenarios when the RAG model latches onto a par-
ticular word or phrase in the retrieved passage and
hallucinates a response that is not only irrelevant
but also factually incorrect. A sample of such a
hallucination is in Fig. 10. This is a more challeng-
ing problem to address. However, retrieval models
that can extract the full context, summarize it and
remove irrelevant information should be capable of
mitigating this issue to a reasonable extent.
7
Conclusion
In this work, we integrate modern retrieval-
augmented large language models with the ancient
Indian philosophy of Advaita Vedanta. Toward this
end, we present VedantaNY-10M, a large dataset
curated from automatic transcriptions of extensive
philosophical discourses on YouTube. Validating
these models along various axes using both auto-
matic and human evaluation provides two key in-
sights. First, RAG models signiﬁcantly outperform
non-RAG models, with domain experts express-
ing a strong preference for using such RAG mod-
els to supplement their daily studies. Second, the
keyword-based hybrid RAG model underscores the
merits of integrating classical and contemporary
deep learning techniques for retrieval in niche and
specialized domains. While there is much work
to be done, our study underscores the potential of
integrating modern machine learning techniques to
unravel ancient knowledge systems.
Limitations and Future Work
While our study demonstrates the utility of integrat-
ing retrieval-augmented LLMs with ancient knowl-
edge systems, there are limitations and scope for
future work. First, this study focuses on a single
niche domain of Advaita Vedanta as taught by one
teacher. Expanding this study to include other an-
cient philosophical systems, such as the Vedantic
schools of Vishishtadvaita and Dvaita, as well as
various Buddhist and Jain traditions, would be a
valuable extension. Second, incorporating primary
scriptural sources, in addition to spoken discourses,
would enhance the authenticity of the RAG model’s
outputs. Third, while we only experiment with
RAG models in this study, ﬁnetuning the language
models themselves on philosophy datasets is an
interesting future direction. Fourth, the context
reﬁner is currently heuristic-based and may not
generalize well to all scenarios. Replacing it with a
trained reﬁner using abstractive or extractive sum-
marization techniques would considerably improve
its utility and efﬁciency. Fifth, expanding the eval-
uation set and involving more subjects for evalua-
tion and will considerably strengthen the study’s
robustness. Finally, while the language models in
this work are primarily in English and Latin script,
building native LLMs capable of functioning in the
original Sanskrit language of the scriptures using
Devanagari script is essential future work.
Acknowledgments
The author would like to thank Prof. Kyle Ma-
howald for his insightful course on form and func-
tionality in LLMs, which guided the evaluation
of the language models presented in this paper.
Fangyuan Xu provided valuable information on au-
tomatic metrics for LFQA evaluation. The author
extends their gratitude to all the human evaluators
who took the survey and provided valuable feed-
back, with special thanks to Dr. Anandhi who coor-
dinated the effort among domain experts. Finally,
the author expresses deep gratitude to the Vedanta
Society of New York and Swami Sarvapriyananda
for the 750+ hours of public lectures that served as
the dataset for this project.
Ethics Statement
All data used in this project has been acquired from
public lectures on YouTube delivered by Swami
Sarvapriyananda of the Vedanta Society of New
York. While our study explores integrating ancient
knowledge systems with modern machine learning
techniques, we recognize their inherent limitations.
These knowledge traditions have always empha-
sized the importance of the teacher in transmitting
knowledge. We do not see LLMs as replacements
for monks and teachers of these ancient traditions,
but only as tools to supplement analysis and study.
Moreover, users of these tools need to be made well
aware that these models can and do make errors,
and should therefore seek guidance from qualiﬁed
teachers to carefully progress on the path.

--- Page 10 ---

References
Tom Aarsen. 2020.
SpanMarker for Named Entity
Recognition.
Yannis Assael, Thea Sommerschield, Brendan Shilling-
ford, Mahyar Bordbar, John Pavlopoulos, Marita
Chatzipanagiotou, Ion Androutsopoulos, Jonathan
Prag, and Nando de Freitas. 2022. Restoring and
attributing ancient texts using deep neural networks.
Nature, 603.
David Bamman and Patrick J Burns. 2020. Latin bert:
A contextual language model for classical philology.
arXiv preprint arXiv:2009.10053.
Bhagavad Gita. 3000 B.C.E. The Bhagavad Gita.
Bartosz Bogacz and Hubert Mara. 2020. Period classiﬁ-
cation of 3d cuneiform tablets with geometric neural
networks. In ICFHR.
Bernd Bohnet, Vinh Q Tran, Pat Verga, Roee Aharoni,
Daniel Andor, Livio Baldini Soares, Jacob Eisenstein,
Kuzman Ganchev, Jonathan Herzig, Kai Hui, et al.
2022. Attributed question answering: Evaluation and
modeling for attributed large language models. arXiv
preprint arXiv:2212.08037.
Sebastian Borgeaud, Arthur Mensch, Jordan Hoff-
mann, Trevor Cai, Eliza Rutherford, Katie Milli-
can, George Bm Van Den Driessche, Jean-Baptiste
Lespiau, Bogdan Damoc, Aidan Clark, et al. 2022.
Improving language models by retrieving from tril-
lions of tokens. In ICML.
The Brahmasutras. 3000 B.C.E. The Brahmasutras.
Tom Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared D Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, et al. Language models are few-shot learners.
Anthony Chen, Gabriel Stanovsky, Sameer Singh, and
Matt Gardner. 2020. MOCHA: A dataset for train-
ing and evaluating generative reading comprehension
metrics. In EMNLP.
Kevin Clark, Minh-Thang Luong, Quoc V. Le, and
Christopher D. Manning. 2020. ELECTRA: Pre-
training text encoders as discriminators rather than
generators. In ICLR.
Alexander Fabbri, Chien-Sheng Wu, Wenhao Liu, and
Caiming Xiong. 2022. QAFactEval: Improved QA-
based factual consistency evaluation for summariza-
tion. In NAACL.
Maarten Grootendorst. 2020. Keybert: Minimal key-
word extraction with bert.
Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasu-
pat, and Mingwei Chang. 2020. Realm: Retrieval
augmented language model pre-training. In ICML.
Matthew Honnibal, Ines Montani, Soﬁe Van Lan-
deghem, and Adriane Boyd. 2020. spaCy: Industrial-
strength Natural Language Processing in Python.
Gautier Izacard, Patrick Lewis, Maria Lomeli, Lucas
Hosseini, Fabio Petroni, Timo Schick, Jane Dwivedi-
Yu, Armand Joulin, Sebastian Riedel, and Edouard
Grave. 2022. Atlas: Few-shot learning with retrieval
augmented language models. JMLR.
Albert Q. Jiang, Alexandre Sablayrolles, Antoine
Roux, Arthur Mensch, Blanche Savary, Chris
Bamford, Devendra Singh Chaplot, Diego de las
Casas, Emma Bou Hanna, Florian Bressand, Gi-
anna Lengyel, Guillaume Bour, Guillaume Lam-
ple, Lélio Renard Lavaud, Lucile Saulnier, Marie-
Anne Lachaux, Pierre Stock, Sandeep Subramanian,
Sophia Yang, Szymon Antoniak, Teven Le Scao,
Théophile Gervet, Thibaut Lavril, Thomas Wang,
Timothée Lacroix, and William El Sayed. 2024. Mix-
tral of experts. Preprint, arXiv:2401.04088.
Nikhil Kandpal, Haikang Deng, Adam Roberts, Eric
Wallace, and Colin Raffel. 2023. Large language
models struggle to learn long-tail knowledge. In
ICML.
Vladimir Karpukhin, Barlas O˘guz, Sewon Min, Patrick
Lewis, Ledell Wu, Sergey Edunov, Danqi Chen, and
Wen-tau Yih. 2020. Dense passage retrieval for open-
domain question answering. EMNLP.
Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke
Zettlemoyer, and Mike Lewis. 2020. Generalization
through memorization: Nearest neighbor language
models. ICLR.
Kalpesh Krishna, Yapei Chang, John Wieting, and Mo-
hit Iyyer. 2022. Rankgen: Improving text generation
with large ranking models. arXiv:2205.09726.
Kalpesh Krishna, Aurko Roy, and Mohit Iyyer. 2021.
Hurdles to progress in long-form question answering.
In NAACL.
Philippe Laban, Tobias Schnabel, Paul N. Bennett, and
Marti A. Hearst. 2022. Summac: Re-visiting nli-
based models for inconsistency detection in summa-
rization. TACL.
Mike Lewis, Yinhan Liu, Naman Goyal, Marjan
Ghazvininejad, Abdelrahman Mohamed, Omer Levy,
Veselin Stoyanov, and Luke Zettlemoyer. 2020a.
BART: Denoising sequence-to-sequence pre-training
for natural language generation, translation, and com-
prehension. In ACL.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio
Petroni, Vladimir Karpukhin, Naman Goyal, Hein-
rich Küttler, Mike Lewis, Wen-tau Yih, Tim Rock-
täschel, et al. 2020b. Retrieval-augmented generation
for knowledge-intensive nlp tasks. NeurIPS.
Yixin Liu, Alexander R. Fabbri, Pengfei Liu, Yilun
Zhao, Linyong Nan, Ruilin Han, Simeng Han,
Shaﬁq R. Joty, Chien-Sheng Wu, Caiming Xiong,
and Dragomir R. Radev. 2022. Revisiting the gold
standard: Grounding summarization evaluation with
robust human evaluation. ArXiv, abs/2212.07981.

--- Page 11 ---

Ligeia Lugli, Matej Martinc, Andraž Pelicon, and Senja
Pollak. 2022. Embeddings models for buddhist San-
skrit. In LREC.
Rajiv Malhotra. 2021. Artiﬁcial Intelligence and the Fu-
ture of Power: 5 Battlegrounds. Rupa Publications.
Rajiv Malhotra and Satyanarayana Dasa Babaji. 2020.
Sanskrit Non-Translatables: The Importance of San-
skritizing English. Amaryllis.
Alex Mallen, Akari Asai, Victor Zhong, Rajarshi Das,
Hannaneh Hajishirzi, and Daniel Khashabi. 2023.
When not to trust language models: Investigating
effectiveness and limitations of parametric and non-
parametric memories. ACL.
Priyanka Mandikal and Raymond Mooney. 2024.
Sparse meets dense: A hybrid approach to enhance
scientiﬁc document retrieval. In The 4th CEUR Work-
shop on Scientiﬁc Document Understanding, AAAI.
Joshua Maynez, Shashi Narayan, Bernd Bohnet, and
Ryan McDonald. 2020. On faithfulness and factual-
ity in abstractive summarization. In ACL.
Jacob Menick, Maja Trebacz, Vladimir Mikulik,
John Aslanides, Francis Song, Martin Chadwick,
Mia Glaese, Susannah Young, Lucy Campbell-
Gillingham, Geoffrey Irving, et al. 2022. Teaching
language models to support answers with veriﬁed
quotes. arXiv preprint arXiv:2203.11147.
Ragaa Moustafa, Farida Hesham, Samiha Hussein, Badr
Amr, Samira Refaat, Nada Shorim, and Taraggy M
Ghanim. 2022. Hieroglyphs language translator us-
ing deep learning techniques (scriba). In Interna-
tional Mobile, Intelligent, and Ubiquitous Computing
Conference (MIUCC).
Reiichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu,
Long Ouyang, Christina Kim, Christopher Hesse,
Shantanu Jain, Vineet Kosaraju, William Saunders,
et al. 2021.
Webgpt: Browser-assisted question-
answering with human feedback.
arXiv preprint
arXiv:2112.09332.
Sonika Narang, MK Jindal, and Munish Kumar. 2019.
Devanagari ancient documents recognition using sta-
tistical feature extraction techniques. S¯adhan¯a, 44.
Zach Nussbaum, John X. Morris, Brandon Duderstadt,
and Andriy Mulyar. 2024. Nomic embed: Training a
reproducible long context text embedder. Preprint,
arXiv:2402.01613.
OpenAI. 2023. Gpt-4 technical report.
Asimina Paparigopoulou, John Pavlopoulos, and Maria
Konstantinidou. 2022. Dating greek papyri images
with machine learning. In ICDAR Workshop on Com-
putational Paleography, https://doi. org/10.21203/rs.
Alec Radford, Jong Wook Kim, Tao Xu, Greg Brock-
man, Christine McLeavey, and Ilya Sutskever. 2023.
Robust speech recognition via large-scale weak su-
pervision. In ICML.
Ori Ram, Yoav Levine, Itay Dalmedigos, Dor Muhlgay,
Amnon Shashua, Kevin Leyton-Brown, and Yoav
Shoham. 2023. In-context retrieval-augmented lan-
guage models. arXiv preprint arXiv:2302.00083.
Ramakrishna Order. Belur math.
Adi Shankaracharya. 700 C.E. Commentary on the
Upanishads.
Weijia Shi, Julian Michael, Suchin Gururangan, and
Luke Zettlemoyer. 2022. Nearest neighbor zero-shot
inference. In Proceedings of the 2022 Conference on
Empirical Methods in Natural Language Processing.
Weijia Shi, Sewon Min, Michihiro Yasunaga, Min-
joon Seo, Rich James, Mike Lewis, Luke Zettle-
moyer, and Wen-tau Yih. 2023. Replug: Retrieval-
augmented black-box language models.
arXiv
preprint arXiv:2301.12652.
Kurt Shuster, Spencer Poff, Moya Chen, Douwe Kiela,
and Jason Weston. 2021. Retrieval augmentation
reduces hallucination in conversation. ACL.
Thea Sommerschield, Yannis Assael, John Pavlopou-
los, Vanessa Stefanak, Andrew Senior, Chris Dyer,
John Bodel, Jonathan Prag, Ion Androutsopoulos,
and Nando de Freitas. 2023. Machine Learning for
Ancient Languages: A Survey. Computational Lin-
guistics.
Mingyang Song, Xuelian Geng, Songfang Yao, Shilong
Lu, Yi Feng, and Liping Jing. 2024. Large language
models as zero-shot keyphrase extractors: A prelimi-
nary empirical study. Preprint, arXiv:2312.15156.
Simeng Sun, Ori Shapira, Ido Dagan, and Ani Nenkova.
2019. How to compare summarizers without target
length? pitfalls, solutions and re-examination of the
neural summarization literature. Workshop on Meth-
ods for Optimizing and Evaluating Neural Language
Generation.
Upanishads. >3000 B.C.E. The Upanishads.
Vedanta
Society
of
New
York.
Swami
Sar-
vapriyananda’s Vedanta discourses.
Lee Xiong, Chuan Hu, Chenyan Xiong, Daniel Cam-
pos, and Arnold Overwijk. 2019.
Open domain
web keyphrase extraction beyond language modeling.
arXiv preprint arXiv:1911.02671.
Fangyuan Xu, Yixiao Song, Mohit Iyyer, and Eunsol
Choi. 2023. A critical evaluation of evaluations for
long-form question answering. In ACL.
Eunice Yiu, Eliza Kosoy, and Alison Gopnik. 2023.
Imitation versus innovation: What children can do
that large language and language-and-vision models
cannot (yet)? ArXiv, abs/2305.07666.
Yaoming Zhu, Sidi Lu, Lei Zheng, Jiaxian Guo, Weinan
Zhang, Jun Wang, and Yong Yu. 2018. Texygen: A
benchmarking platform for text generation models.
In The 41st International ACM SIGIR Conference on
Research & Development in Information Retrieval.

--- Page 12 ---

A
Implementation Details
A.1
Automatic Metrics
Following Xu et al. (2023), we implement a num-
ber of automatic evaluation metrics for LFQA as
described below.
Length
We use the Spacy package (Honnibal
et al., 2020) for word tokenization.
Self-BLEU
We calculate Self-BLEU by regard-
ing one sentence as hypothesis and all others in the
same answer paragraph as reference. We report
self-BLEU-5 as a measure of coherence.
RankGen
For a given question q and a model-
generated answer a, we ﬁrst transform them into
ﬁxed-size vectors (q, a) using the RankGen en-
coder (Krishna et al., 2022). To assess their rel-
evance, we compute the dot product q · a. We
utilize the T5-XXL (11B) encoder, which has been
trained using both in-book negative instances and
generative negatives.
QAFactEval
QAFactEval is a QA-based metric
recently introduced by Fabbri et al. (2022). It has
demonstrated exceptional performance across mul-
tiple factuality benchmarks for summarization (La-
ban et al., 2022; Maynez et al., 2020). The pipeline
includes four key components: (1) Noun Phrase
(NP) extraction from sentence S represented as
Ans(S), (2) BART-large (Lewis et al., 2020a) for
question generation denoted as QG, (3) Electra-
large (Clark et al., 2020) for question answering la-
beled as QA, and (4) learned metrics LERC (Chen
et al., 2020), to measure similarity as Sim(pi, si).
An additional answerability classiﬁcation module
is incorporated to assess whether a question can
be answered with the information provided in doc-
ument D. Following Xu et al. (2023), we report
LERC, which uses the learned metrics to compare
AnsS and AnsD(a).
A.2
Chat Prompt
For an example of the constructed RAG bot prompt,
please refer to Fig. 5. In this scenario, the RAG
bot Cr is presented with the top-k retrieved pas-
sages alongside the query for generating a response,
whereas a generic bot Cg would only receive the
query without additional context.
B
Sample Sanskrit terms
Table 2 contains excerpts from passages containing
Sanskrit terms. The Sanskrit terms are italicized
RAG Bot
You are a helpful assistant that accurately 
answers queries using Swami Sarvapriyananda's 
YouTube talks. Use the following passages to 
provide a detailed answer to the query: {query}
Passages:
{Passage 1}
{Passage 2}
...
{Passage k}
Generic Bot
You are a helpful assistant that accurately 
answers queries using Swami Sarvapriyananda's 
YouTube talks. Provide a detailed answer to the 
query: {query}
RAG Bot
Generic Bot
Figure 5: Prompts for the RAG and generic chatbots.
RAG Bot receives the top-k retrieved relevant passages
in the prompt along with the query, while the generic
bot only receives the query.
and underlined. Notice that the passages contain
detailed English explanations of these terms. To
retain linguistic diversity, authenticity and compre-
hensiveness of the source material, we retain these
Sanskrit terms as is in our passages as described in
Sec. 3. Note that these are direct Whisper (Radford
et al., 2023) transcriptions with no further post-
processing or proofreading. Transcriptions may
not always be accurate.
C
Transcription
We asses the transcript quality and list out some
common errors.
C.1
Transcript Evaluation
Transcription quality is scored on a scale from 1 to
5 (where 1 = Poor, 5 = Perfect). On 10 randomly
sampled transcripts, evaluators assign a high av-
erage score of 4.48 suggesting that the transcrip-
tion of YouTube audio into text is highly accurate
and clear, indicating that our constructed custom
dataset Dt is of high quality.
C.2
Transcript Errors
Table 3 contains a few sample transcription errors.
The transcriptions are largely good for English
words and sentences. However, errors often arise
from incorrectly transcribing Sanskrit terms and
verses. Other less common errors include missing

--- Page 13 ---

Sl. No.
Excerpts from passages
Notes
1.
Om Bhadram Karne Bhishrinu Yamadevaha Bhadram
Pashyam Akshabhirya Jatraaha Sthirai Rangai Stushta
Vagam Sasthanubhi Vyase Madevahitaiyadayoh Swasthina
Indro Vriddha Shravaha Swasthina Phusa Vishwa Vedaaha
Swasthina Starksho Arishta Nemi Swasthino Brihas Patir
Dadhatu Om Shanti Shanti Shanti.
This is a Sanskrit chant which
is directly Romanized and pro-
cessed. The automatic tran-
scriptions often contain errors
in word segmentation for San-
skrit verses.
2.
Samsara is our present situation, the trouble that we are
caught in, the mess that we are caught in. Samsara is this.
In Sanskrit, normally when you use the word samsara, it
really means this world of our life, you know, being born
and struggling in life and afﬂicted by suffering and death
and hopelessness and meaninglessness.
Samsara is a Sanskrit term.
The excerpt contains an expla-
nation of the concept in En-
glish.
3.
The problem being ignorance, solution is knowledge and the
method is Jnana Yoga, the path of knowledge. So what is
mentioned here, Shravana Manana Nididhyasana, hearing,
reﬂection, meditation, that is Jnana Yoga. So that’s at the
highest level of practice, way of knowledge.
The excerpt contains an expla-
nation of Jnana Yoga, the path
of knowledge.
4.
In Sanskrit, ajnana and adhyasa, ignorance and superim-
position. Now if you compare the four aspects of the self,
the three appearances and the one reality, three appearances,
waker, dreamer, deep sleeper, the one reality, turiyam, if
you compare them with respect to ignorance and error, you
will ﬁnd the waker, that’s us right now. We have both igno-
rance and error.
Ajnana, adhyasa and turiyam
are Sanskrit terms. Notice that
the passage implicitly contains
rough English translations of
these terms in the context of
the overall discourse. For in-
stance, ajnana is translated
as ignorance and adhyasa is
translated as superimposition.
5.
Mandukya investigates this and points out there is an un-
derlying reality, the Atman, pure consciousness, which has
certain characteristics. This is causality, it is beyond causal-
ity. It is neither a cause nor an effect. The Atman is not
produced like this, nor is it a producer of this. It is be-
yond change. No change is there in the Atman, nirvikara.
And third, it is not dual, it is non-dual, advaitam. This is
kadyakarana in Sanskrit, this is kadyakarana vilakshana
Atma. In Sanskrit this is savikara, this is nirvikara Atma.
This is dvaita, this is advaita Atma. So this is samsara and
this is moksha, freedom.
The excerpt contains an ex-
planation of different Sanskrit
technical terms.
Table 2: Excerpts from passages containing Sanskrit terms. These excerpts contain detailed English descriptions
of technical terms in Sanskrit (italicized and underlined). To retain authenticity to the source material, we retain
these Sanskrit terms as is in our passages. Note that these are direct Whisper (Radford et al., 2023) transcriptions
with no further post-processing or proofreading, so transcriptions may not always be accurate. For more details,
refer to Sec. B.

--- Page 14 ---

RAG Bot
Was Alan Watts' associated with Vedanta?
Figure 6: Subject confusion: Aldous Huxley vs Alan Watts. In the retrieved passage, the speaker jumps between
speaking about Aldous Huxley and Alan Watts. Moreover, the transcription has poor punctuation. As a result, the
RAG bot incorrectly attributes information about Huxley to Watts in the response. Due to the unstructured nature of
the spoken text, such errors can occur. This can be addressed by converting the spoken text into a more structured
prose format with the help of well-crafted prompts to LLMs, followed by human proofreading (see Sec. D).
or incorrect punctuation. Human proofreading will
remove these errors to a large extent.
D
Spoken vs written language
Unlike traditional textual corpora that are compiled
from written sources, our dataset is derived from
spoken discourses. Spoken language is often more
verbose and less structured than written text, with
the speaker frequently jumping between concepts
mid-sentence. This unstructured nature of the text
can be unfamiliar for a language model trained ex-
tensively on written text, which expects a more
coherent and structured input. Fig. 7 shows a pecu-
liar failure case arising from this issue. The speaker
jumps between speaking about Aldous Huxley and
Alan Watts. As a result, the RAG bot incorrectly
attributes information about Huxley to Watts while
answering the query. Due to the unstructured na-
ture of the spoken text, such errors can occur. This
can be addressed by converting the spoken text into
a more structured prose format with the help of
well-crafted prompts to LLMs, followed by human
proofreading.
E
Question Categories
To ensure a broad and comprehensive evalua-
tion, we categorize the questions into ﬁve distinct
types—anecdotal, teminology, scriptural, compara-
tive and reasoning. Questions from each of these
categories is provided in Tab. 4. Each category is
designed to test different aspects of the model’s
capabilities. For details, refer to Sec. 5.
F
Sample Responses: RAG vs Non-RAG
In Figs. 7-11, we present the sample queries and
responses from the RAG and generic chatbots for
ﬁve sample queries. The query is highlighted in
yellow, RAG response is in the green box. Non-
RAG response is in the red box. We use GPT-4-
turbo (OpenAI, 2023) as the large language model
for both of them.
G
Sample Responses: Standard RAG vs
Keyword-based Hybrid RAG
In Figs. 12-16, we present the sample queries and
responses from the standard RAG and keyword-
based hybrid RAG model for one query each
from ﬁve categories. We additionally also show
the human-annotated and model generated key-
words. Keyword-RAG response is in the green
box. Standard-RAG response is in the red box. We
use Mixtral-8x7B-Instruct-v0.1 (Jiang et al., 2024)
as the large language model for both of them.

--- Page 15 ---

Sl. No.
Transcription errors
Notes
1.
That’s what Sam Altman, Chachjipiti, some-
body asked him.
Should be ChatGPT
2.
Last year, you studied extensively with Profes-
sor Garﬁeld, I believe, studying Vajamaka and
the teachings of the Garjuna.
Should be Madhyamaka
and Nagarjuna,
respec-
tively
3.
From attachment comes desire, raga, I want
it and if that desire is satisﬁed then there is no
end to it, greed, lobha. But if it is somehow
thwarted, then anger, kama krodho vijayate.
Should be bhijayate
4.
In fact, one of the terms which is used
in
Mandukya
Upanishad,
Brahman
is
abhyavaharyam.
Should be avyavaharam
5.
So, one of them was the Brahmo Samad,
which was quite popular in Calcutta in those
days.
Should be Samaj
6.
I am awareness I’m eternal consciousness Al-
dous Huxley Christopher Isherwood Gerald
Hurd all of them were very close to Swami
Prabhavananda in Southern California in Hol-
lywood and look at the product of that Ish-
erwood wrote that one of the most amazing
biographies
The transcripts sometimes
miss punctuation marks,
making the passage dif-
ﬁcult to comprehend for
both humans and language
models
Table 3: Sample transcription errors. For constructing our text corpus, we directly use the transcripts obtained
from Whisper (Radford et al., 2023) with no further post-processing or proofreading. The transcriptions are largely
good (with a score of 4.5/5 from human evaluators). However, errors arise from incorrectly transcribing Sanskrit
terms, missing punctuations, etc. Human proofreading will remove these errors to a large extent.

--- Page 16 ---

Category
Description
Questions
Anecdotal
Stories and
anecdotes
narrated by the
speaker in the
discourses
• Does Swami speak about Wittgenstein’s thesis defense?
• Does Swami narrate any incident surrounding Shivaratri?
• Does Swami speak about The Matrix movie?
• Does Swami speak about Vachaspati Mishra? Does he narrate
how Bhamati came to be written?
• What was Christopher Isherwood’s contribution to Vedanta?
Terminology
Probe the
model’s
understanding
of speciﬁc terms
and concepts
• What is Adhyaropa Apavada?
• What is Vikshepa Shakti?
• What is the signiﬁcance of the word ‘Shraddha’?
• What is Upadana Karana?
• What constitutes Sadhana Chatushtaya?
Scriptural
Reference,
interpret, and
explain
passages from
religious or
philosophical
texts
• In Mandukya Upanishad, what is the signiﬁcance of the word
‘Om’?
• In the Gospel, what parable does Sri Ramakrishna use to portray
intense longing for God?
• In the Mundaka Upanishad, how do we interpret the parable of
the two birds?
• How is Phala Vyapti and Vritti Vyapti deﬁned in Vedantasara?
• In the Gospel of Sri Ramakrishna, how do we understand the
analogy of the salt doll that Thakur provides?
Comparative
Analyze and
compare
different
concepts,
philosophies, or
texts
• As mentioned in the Yoga Sutras, is Samadhi necessary to attain
enlightenment according to Advaita Vedanta?
• Would Sri Ramakrishna’s teachings be considered purely Ad-
vaitic?
• In Kashmir Shaivism, Chit is both Prakasha and Vimarsha i.e. it
is both self-lumious and self-reﬂective. Would Advaita Vedanta
agree with this?
• How does Sankhya differ from Advaita Vedanta?
• What is the main difference between Buddhist Shunyavada and
Advaita Vedanta?
Reasoning
Require logical
reasoning,
critical thinking,
and the
application of
principles to
new scenarios
• Can AI ever become conscious?
• Is the waking state similar to a dream or absolutely indistinguish-
able from the dream state?
• Do our senses report reality to us?
• Dis-identifying myself from the body-mind seems to require a
lot of effort. Did the reverse process of identiﬁcation also involve
as much effort?
• If Brahman as Existence-Consciousness-Bliss is the eternal sub-
ject that cannot be objectiﬁed, yet eternally reveals itself to give
rise to apparent objects through the principle of Maya, can we
infer that Brahman is Existence-Consciousness-Bliss-Maya? That
is, is Brahman inseparable from Maya?
Table 4: Question categories. To ensure a broad and comprehensive evaluation, we categorize the questions into
ﬁve distinct types, each designed to test different aspects of the model’s capabilities. For details, refer to Sec. 5.

--- Page 17 ---

Generic Non-RAG Bot
RAG Bot
Sam Altman says that he believes in the absolute equivalence of 
Brahman and Atman. What does it mean?
Figure 7: RAG vs Non-RAG: Sam Altman on Atman and Brahman. The retrieved passages are very good at
capturing the context of the query. The ﬁrst passage references the monk speaking about Sam Altman and his
views on Atman and Brahman. The second passage contains a brief explanation of Atman and Brahman that is
helpful to answer the query. The generic bot also generates a reasonable answer. However, it has a sentence stating
that, “Atman is a part of Brahman”. This is incorrect in the context of Advaita Vedanta as it is not the same as
equivalence—this point was highlighted by the domain experts in the survey.

--- Page 18 ---

Generic Non-RAG Bot
RAG Bot
Does Swamiji speak about Wittgenstein’s dissertation defense?
Figure 8: RAG vs Non-RAG: Wittgenstein’s thesis defense. The retrieved passage is about the monk narrating a
story about Wittgenstein’s thesis defense, which is highly relevant to the query. The generated RAG bot response
makes use of this passage to answer the query. However, the latter half of the response is not relevant to the query
and is purely hallucinated. The generic bot response, on the other hand, is completely fabricated and references a
non-existent YouTube talk.

--- Page 19 ---

Generic Non-RAG Bot
RAG Bot
Can AI ever become conscious?
Figure 9: RAG vs Non-RAG: AI and Consciousness. The retrieved passages are again highly relevant to the
query and the generated answer is coherent. However, it does contain a statement about “a mirror reﬂecting a face”
which is not present in the passages. This was pointed out by the experts as a relevant statement possibly drawn
from outside knowledge. The generic bot’s response is highly general and does not represent the monk’s views on
the topic.

--- Page 20 ---

Generic Non-RAG Bot
RAG Bot
Do our senses report reality to us?
Figure 10: RAG vs Non-RAG: Senses and reality. In this scenario, the retrieved passages provide only partial
context needed to answer the query, with additional irrelevant information. For example, one passage mentions
cognitive scientist Donald Hoffman, inadvertently inﬂuencing the LLM to generate a response linking the Swami’s
views to Hoffman’s concept of the world as a virtual reality. This is an instance where the LLM diverges from the
query, using incomplete information from the passage. To mitigate this, implementing retrieval models capable of
processing longer contexts and summarizing them effectively before input to the LLM could be beneﬁcial. Despite
this, the rest of the response aligns reasonably well with Advaita Vedanta philosophy, similar to the generic bot’s
response, which is also congruent with the philosophical context.

--- Page 21 ---

Generic Non-RAG Bot
RAG Bot
Dreams feel absolutely real while dreaming. What is the guarantee that 
I am not fast asleep in my bed and dreaming right now?
Figure 11: RAG vs Non-RAG: Waking and dreaming. The passages retrieved for the query are relevant but only
offer a segment from a broader context. As stated earlier, this can be mitigated by using more advanced retrieval
models that summarize longer contexts before input to the LLM. The RAG bot’s response, while relevant, is lengthy
and complex, making it challenging to comprehend. The generic bot’s response although more concise and coherent,
is completely general and has no relation to the Advaita Vedanta philosophy.

--- Page 22 ---

Standard RAG
Keyword-based RAG
Keywords
Human-annotated: Shivaratri 
Model ensemble: 
Shivaratri
Category: Anecdotal
Query: Does Swami narrate any incident surrounding Shivaratri?
Figure 12: Keyword-RAG vs Standard-RAG: Anecdotal. The keyword-based retriever accurately retrieves the
correct snippet, while the dense retriever confuses “Shivaratri” with “Shivamayananda”, possibly owing to similar
embeddings and completely misses the context. As a result, the generated standard RAG answer is meaningless
and lacks substance. The keyword-RAG model identiﬁes the two key incidents relating to Shivaratri correctly and
effectively summarizes them.

--- Page 23 ---

Standard RAG
Keyword-based RAG
Keywords
Human-annotated: Shraddha 
Model ensemble: 
Shraddha, significance
Figure 13: Keyword-RAG vs Standard-RAG: Terminology. The keyword-RAG model retrieves a comprehensive
exposition on the concept of Shraddha, loosely translated as conviction, in the context of qualiﬁcations for the study
of Advaita Vedanta. The standard RAG although retrieves a passage containing the word, it is however not directly
related to what the questioner intends. This seems to be an unfortunate case of false positive for standard RAG due
to inadequate or implied meaning in the query.

--- Page 24 ---

Standard RAG
Keyword-based RAG
Figure 14: Keyword-RAG vs Standard-RAG: Comparative. This is a case where both models retrieve meaningful
passages, with the keyword-based model providing greater context due to retrieval expansion. The standard model
also seems to be using outside knowledge not mentioned in the passage.

--- Page 25 ---

Standard RAG
Keyword-based RAG
Keywords
Human-annotated: Om significance, Mandukya 
Model ensemble: 
Om, Mandukya Upanishad
Figure 15: Keyword-RAG vs Standard-RAG: Scriptural.
Both models retrieve from the correct scripture.
However, while the retrieved passage in keyword-RAG is very comprehensive and accurately captures the context
of the question, the standard RAG misses the point of the question and gives a generic answer.

--- Page 26 ---

Standard RAG
Keyword-based RAG
Figure 16: Keyword-RAG vs Standard-RAG: Reasoning. The retrieved passage in keyword-RAG is technical
and comprehensive and the generated answer effectively summarizes the main points. The standard model is also
good, although the explanation is not as effective owing to the quality of retrieval.

```
