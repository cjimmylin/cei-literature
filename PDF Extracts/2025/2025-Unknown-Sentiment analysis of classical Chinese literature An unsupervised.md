---
title: "2025-Yu-Sentiment analysis of classical Chinese literature An unsupervised - PDF Extract"
source_pdf: "2025-Yu-Sentiment analysis of classical Chinese literature An unsupervised.pdf"
pages: 23
extracted_at: "2026-02-13T14:50:57.983843"
---

# PDF Extract: 2025-Yu-Sentiment analysis of classical Chinese literature An unsupervised

**Source PDF:** 2025-Yu-Sentiment analysis of classical Chinese literature An unsupervised.pdf
**Total Pages:** 23

---

## Content

```
--- Page 1 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
1 / 23
 
 OPEN ACCESS
Citation: Yu X, Wang J (2025) Sentiment 
analysis of classical Chinese literature: An 
unsupervised deep learning model with BERT 
and graph attention networks. PLoS One 20(9): 
e0330919. https://doi.org/10.1371/journal.
pone.0330919
Editor: Issa Atoum, Philadelphia University, 
JORDAN
Received: February 24, 2025
Accepted: August 7, 2025
Published: September 23, 2025
Peer Review History: PLOS recognizes the 
benefits of transparency in the peer review 
process; therefore, we enable the publication 
of all of the content of peer review and 
author responses alongside final, published 
articles. The editorial history of this article is 
available here: https://doi.org/10.1371/journal.
pone.0330919
Copyright: © 2025 Yu, Wang. This is an open 
access article distributed under the terms of 
the Creative Commons Attribution License, 
which permits unrestricted use, distribution, 
RESEARCH ARTICLE
Sentiment analysis of classical Chinese 
literature: An unsupervised deep learning model 
with BERT and graph attention networks
Xiaohan Yu1, Jin Wang
2*
1  School of Arts and Social Sciences, Hong Kong Metropolitan University, Kowloon, Hong Kong, 2  School 
of Foreign Languages, Weifang University, Weifang, China 
* jkxr58@163.com
Abstract 
Sentiment analysis has become a transformative technology in various contexts, 
particularly in Natural Language Processing (NLP), social media analytics, and liter­
ary analysis, as it can extract information from a wide range of texts. The advance­
ments in deep learning, particularly with transformer models such as BERT and 
graph-based models like GATs, have enabled faster progress in analyzing complex 
language structures. However, the issue lies in incorporating these technologies into 
classical Chinese literature, which involves delicate syntax, semantics, and emo­
tions that are difficult to harness using traditional methods. The existing methods, 
which rely on strictly labeled data or unsupervised learning methods that do not 
effectively manage contextual dependencies, are very limited in analyzing historical 
or philosophical texts that abound in metaphor and implicit sentiment. To minimize 
the limitations, this paper proposes an unsupervised deep learning framework that 
integrates BERT embeddings, sentiment lexicon enrichment, and graph attention 
networks (GATs) for sentiment analysis in classical Chinese literature. Firstly, the 
BERT-based model extracts contextualised embeddings from a raw text, providing a 
deep understanding of semantics. Secondly, embedding includes sentiment-specific 
data from the NTUSD lexicon, thus injecting it with emotional information. Thirdly, a 
graph-based formulation is developed, in which words are represented as nodes, and 
the relations between them are defined using GATs to modify the features of nodes 
based on their significance in the context. Finally, unsupervised sentiment label­
ling, or K-Means clustering, is used to classify sentiment. The experimental results 
demonstrate the proposed model’s efficiency – an accuracy of 0.95, precision of 0.97, 
recall of 0.96, and F1-score of 0.91 in several runs. These results surpass those of 
the traditional approach, which includes SentiCNN, MLT-ML4, and BERT-LLSTM-DL, 
which achieve an accuracy score of 0.90 to 0.95. Additionally, the comparison with 
large-scale foundation models (such as ChatGPT-4o and DeepSeek R1) in zero-shot 
prompt-based classification further validates the domain-adapted advantage of our 

--- Page 2 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
2 / 23
model in the classical Chinese text processing. These results demonstrate that the 
proposed model significantly enhances the handling of the intricate linguistic features 
and cultural nuances in classical Chinese texts, providing a robust solution for senti­
ment analysis in low-resource domains.
1  Introduction
In recent years, the rapid growth of technology has reshaped various fields, particu­
larly in domains such as artificial intelligence (AI), machine learning (ML), and natu­
ral language processing (NLP). It has become increasingly important to understand 
public sentiments, as the world is now highly digitally interlinked. Sentiment analysis, a 
significant application in NLP, is crucial in uncovering the hidden feelings and thoughts 
associated with text [1]. This topic has been extensively researched across different 
languages, cultures, and situations, highlighting its growing relevance [2]. Since the 
world is increasingly interconnected and culturally diverse, analyzing sentiment in 
different languages is even more crucial [3]. Since a diversity of languages is a fun­
damental element of the global communication process, sentiment analysis methods 
must be developed to address the linguistic challenges associated with the process [4]. 
The sentiment analysis technique was developed from rule-based systems that entirely 
relied on expounded and clearly defined linguistic rules and patterns to identify senti­
ments in the text. However, with the advancement of ML techniques, this specific field 
has received several developmental boosts and seeded values that need to be consid­
ered. The ML is more flexible and generalizes the capability to deliver highly authentic 
and scalable sentiment analysis over wide-ranging textual data [5]. With the arrival of 
DL models, humor identification has changed significantly because of the capability of 
systems to identify complex syntactic and semantic patterns within text. Even so, mod­
ern neural models, such as convolutional neural networks (CNNs) and recurrent neural 
networks (RNNs), have proven capable of analyzing intricate linguistic patterns and 
shades of emotion. The essential approaches are beds for modeling relations between 
words and interpreting relations, making sense of tremendously advanced sentiment 
analysis systems [6]. Sentiment analysis based on deep learning is successfully 
used in various sectors of human activity, including social research, public policy, and 
­commercial analytics. Namely, organisations employ it to identify their clients’ issues, 
evaluate the overall attitude toward the brand they represent, and design adequate pro­
motion campaigns [7]. The emergence of transformer-based models, such as BERT, 
has transformed NLP applications, enabling a more nuanced understanding of textual 
data. There have been investigations using BERT for sentiment analysis, highlighting 
its effectiveness in measuring contextual semantics. In addition, several researchers 
have optimized BERT for multimodal sentiment analysis, enhancing its ability to pro­
cess and comprehend data from various sources [8]. Similarly, social researchers ana­
lyze the intensity and cycles of feelings within societies, and public politicians employ 
such techniques to determine how the public feels about particular matters of concern. 
These elaborate shows how deep learning can yield useful info from text [9].
and reproduction in any medium, provided the 
original author and source are credited.
Data availability statement: All data used in 
this study are publicly available. The primary 
dataset, titled "Ancient Chinese Text (wenyan­
wen)", comprising classical Chinese literature 
texts, is openly accessible via the Kaggle 
platform and contains classical Chinese literary 
texts including poetry and prose suitable for 
natural language processing tasks such as 
sentiment analysis: https://github.com/jkxr58/
Deep-Learning-Model-with-BERT-and-Graph-
Attention-Networks. Kaggle Dataset Link. 
In addition, all data generated and analyzed 
during the study including tokenized input 
texts (translated into English), enriched 
embeddings, clustering labels, final centroids, 
and macro-averaged evaluation metrics 
(accuracy, precision, recall, and F1-score) are 
publicly hosted in a supplementary repository. 
Repository URL: https://github.com/jkxr58/
Deep-Learning-Model-with-BERT-and-Graph-
Attention-Networks. These materials include 
the minimal dataset necessary to replicate 
the study’s findings, including all files used 
to generate tables, figures, and performance 
analyses. In continuation to this The sentiment 
lexicon used to enrich the embeddings was the 
NTUSD (National Taiwan University Sentiment 
Dictionary), which is also publicly accessible. 
No data access restrictions apply.
Funding: The author(s) received no specific 
funding for this work.
Competing interests: The authors have 
declared that no competing interests exist.

--- Page 3 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
3 / 23
Chinese classical literature has been a tremendous treasure trove of philosophy, culture, and feeling for thousands 
of years. It encompasses multiple genres, including poetry, prose, and historical records, that represent the evolution of 
Chinese thinking, art, and the behavioral code of nations. Indeed, great classics such as The Book of Songs (Shijing) 
and Records of the Grand Historian (Shiji) have not only imprinted themselves on literature but also occasioned pertinent 
philosophical thoughts and molded social orders throughout Chinese history. Over thousands of years, these texts provide 
access to the intricacies of human sentiment, shifts in society and lifestyle, and cultural norms that have influenced Chi­
nese arts and ideas [10]. Examining the sentiments in these works can provide valuable insights into ancient China’s emo­
tional and sociocultural environments [9]. Sentiment analysis has become applicable due to advancements in NLP and the 
availability of Chinese literature digitised online. It also enables text analysis by time, genre, and dialect, and offers a new 
reading of the affective and evaluative dimensions of Chinese classical works [11]. These augment traditional qualitative 
approaches to facilitate scholars in recognizing transitions in literary thematics, those of culture, and variations in style 
[12]. Moreover, sentiment analysis in Chinese literature is crucial for the entire field of digital humanities, as it enables the 
large-scale study of literary development, authorship attribution, and stylistics. This enriches the previous historical and 
cultural analytical methods, allowing for the analysis of progressive changes in stylistic assignments and the evolution of 
authors’ voices [13]. The researchers in [14] previously proposed a method for multi-task analysis using hierarchical atten­
tion mechanisms, which facilitated sentiment analysis of Chinese classical poetry. This model will be applied at the poem 
and line levels, respectively, since a style in a classical literary work can be either of these two. Such use was made of the 
hierarchical attention that assists in solving the fine-grained and emotion-overloaded correspondence inherent in poetry. 
The sentiment analysis was treated professionally.
Several studies have addressed the challenge of sentiment analysis in the context of literary works, particularly in lan­
guages with complex grammar and rich cultural backgrounds, such as Chinese. The work by [15] proposed a sentiment 
analysis model (SA-Model) using BERT-wwm-ext and ERNIE embeddings through hybrid word vectors. This approach 
employs multi-feature fusion to enhance the performance of semantic analysis of typical sections of classical Chinese 
texts and to address issues arising from the stylistic features of poems from distant periods. In the work [16], models of 
neural networks were used to study the poems of the Tang Dynasty, examining the linguistic and emotional features typi­
cal of ancient Chinese script. Some difficulties in analysing sentiment in this genre were described with an accent on the 
fact that emotions in poems written in ancient times are rather profound and diverse. Research carried out by [9] has pre­
sented a model termed BERT-LLSTMDL for coping with sentiment analysis of works of Chinese literature. This framework 
applies BERT for the most modern language representation, LSTM for sequence-to-capture, and DL for feature extraction, 
as it is challenging in this research area due to analysing Chinese literary texts’ sentiment. To improve sentiment analysis 
results in traditional Chinese poetry, the author proposed enhancing sentiment analysis performance in traditional Chi­
nese poetry. The framework uses sentiment labels for short lines and hierarchical attention to increase accuracy. With this 
method, sentiment analysis is done on both the poem and the individual lines simultaneously, and sentiment information 
from the short lines is used to enhance word- and sentence-level attention. This approach seeks to convey the subtle 
stylistic elements and emotional depth of ancient poetry more successfully.
Although development has been made, there are still several issues when dealing with sentiment analysis of Chinese 
classical literature because of its complex sentiment correlations and implicit meanings in the grammatical structure, 
metaphors, and allegories. Also, classical Chinese texts do not contain many direct words that can show the speaker’s 
emotion. As such, earlier identification of sentiment scores is not always possible and entails using advanced models 
that can discern fine-grained emotional scripts inherent in the text, given the interdependent cultures and history. Further, 
both the conceptual metaphors and allusions add one more degree of indirection to the analysis, and the correct inter­
pretation of these would require powerful approaches based on deep learning. Researchers must create models incor­
porating contextual understanding and fundamental word-based analysis to correctly infer feelings from these old literary 
works. A significant obstacle for supervised learning models, which depend on vast amounts of labelled data for efficient 

--- Page 4 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
4 / 23
training, is the dearth of annotated datasets for ancient Chinese literature. Because classical literature frequently doesn’t 
have enough labelled instances for model training, this constraint makes it challenging to use traditional techniques for 
sentiment analysis in this field. LSTM networks, if used in sentiment analysis, have not remained without drawbacks, the 
key ones among which are the following: the training of non-local dependencies is considered extremely challenging, 
and the training computation demand is known to be much higher. These issues impact efficiency and, more so, large 
volumes of data, such as Chinese classical literature, because higher models are required for such texts [17]. In addition, 
the ­sequential nature of LSTM models hinders the models from benefiting from these contextual relations, as presented 
in these texts [18].
According to the abovementioned considerations, this study introduces a new unsupervised sentiment analysis 
model aimed at the Chinese classical literature. The proposed model fuses the strength of BERT-based contextual 
embeddings with graph attention networks (GATs) and sentiment lexicon enrichment to deal with the issues connected 
to analyzing ancient texts. This model deals with such issues as the absence of annotated datasets, the complexity of 
metaphors and implicit feelings, and the context dependencies of the classical Chinese language. The first important 
component of the model deals with extracting contextual word embeddings with the help of BERT-base-Chinese; hence, 
the model is c­apable of imbibing the semantic contents of words from their contexts. The second part involves incor­
porating ­sentiment-specific information of the NTUSD sentiment lexicon into the enrichment of embeddings so that the 
model can better comprehend the tone of emotional texts in classics. The third is the one that generates a graph-based 
representation in which words are transformed into nodes and employs GATs to determine their relationship in feature 
updates according to attention mechanisms. Lastly, the K-Means clustering classifies the sentiments into three categories. 
­Positive, negative, and neutral. The findings from the experiments reveal that this unsupervised model outperforms the 
traditional approaches, with high accuracy, precision, recall and F1-scores, hence becoming a strong instrument to use in 
analyzing sentiments in the low-resource literary domains. This approach promotes sentiment analysis in classical litera­
ture and solves a scalable problem of studying other historical pieces rich in culture.
The key contributions of the paper are as follows:
•	 This paper introduces a new deep learning framework for Chinese classical literature sentiment analysis. It thus over­
comes the usually encountered problem of the lack of labelled datasets in analyzing ancient texts.
•	 The model integrates sentiment-specific information from the NTUSD lexicon into the BERT-based embeddings, 
enhancing the model’s ability to capture emotional nuances in classical Chinese texts.
•	 The paper provides Graph Attention Networks (GATs) to fill in the relationships between words regarding their 
co-occurrence and semantic relations.
•	 The proposed model is thoroughly examined using the experimental results that prove its better performance compared 
with the traditional sentiment analysis models, such as LSTM, BiLSTM, and CNN. The paper compares the proposed 
model to achieve better accuracy, precision, recall, and F1-scores. It demonstrates its effectiveness in sentiment classifi­
cation of classical Chinese texts and provides a scalable solution for sentiment analysis in low-resource settings.
The rest of this research work is organized as follows: Section 2(Related Work) of the paper discusses the contribution 
of other researchers; Section 3(Materials and Methods) of the paper explains the framework of our proposed model; Sec­
tion 4 (Performance Evaluation) of this work presents a performance evaluation of the proposed model and a discussion 
of the paper. Finally, the conclusion with the future research plan is given in Section 5(Conclusion and Future Work).
2  Related work
In the last few years, sentiment analysis has been one of the top techniques used in analyzing and interpreting Chinese 
literary works, as well as the emotions, themes and culture featured in the literary works [19,20]. The present literature 

--- Page 5 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
5 / 23
review aims to give a general idea of the research landscape, both about the methodology applied and the results 
obtained. In addition, it analyses the contribution of sentiment analysis to the understanding of emotions in the Chinese 
literary works, showing the complexity of relationships between themes, moods, and cultural settings in which the respec­
tive works were created. Computational methods aid in unveiling Chinese literature’s hidden emotional and philosophical 
strata and understanding its sociocultural development.
Numerous previous studies have used sentiment lexicons, like lists of words and the subjective sentiment scores 
attached to such words, to obtain the overall sentiment score for any text based on the words in the text. These methods 
are quite easy to implement, have an interpretable nature, and have proven effective in domain-specific text analysis 
[21–25], and [26]. They perform especially well when processing short texts and delimited language, since the technol­
ogy can be better used to detect specific linguistic shades. However, these approaches have their limitations when dealing 
with more complex texts, such as those found in the Chinese classical literature, where sentiment is usually implied rather 
than explicitly expressed by metaphors and backgrounds. Another method, which is based on labeled multilingual sentiment 
datasets, has been widely used for training supervised models of machine learning, such as Naive Bayes classifiers, Support 
Vector Machines (SVM), and Random Forest [27–31] and [32]. These techniques can be used for a medium-sized data­
set and extract complex relations between data. However, relying on annotated data, the problem of feature selection, and 
difficulty in sarcasm interpretation are typically common and diminish their performance, especially when applied to massive 
literature or complex ones. Deep learning methods have caught up to overcome these limitations because no manual feature 
extraction is required, and complex patterns in text data can be automatically detected [33]. These include Convolutional 
Neural Networks (CNNs), Long Short-term Memory (LSTM) networks and transformer-based models such as BERT that 
managed to achieve better results in sentiment analysis due to picking up sophisticated emotional and syntactical patterns 
[34,35]. These models can be tuned by transfer learning approaches to make them capable of exploiting knowledge from 
source languages to better exploit the target language. For instance, BERT-based models have been used successfully to 
analyze the sentiments of Chinese news [36] and identify financial fraud from textual data [22]. These models’ ability to cap­
ture subtle emotions and complex language structures has made them particularly effective for sentiment analysis in Chinese 
literary texts, especially when combined with fine-tuning strategies for specific domains.
In the significance of the Chinese classical literature, in recent studies, there has been an advent to practice using deep 
learning models to examine the complex emotional content of ancient texts. For example, a certain research presented 
a sentiment analysis model using the multidimensional knowledge attention to extract features belonging to the semantic 
and cultural context of ancient Chinese poetry [37]. Similarly, other studies have been using the Large Language Models 
(LLMs), for example, in sentiment analysis in classical Chinese literature, with a strong focus on Song Dynasty poetry 
(Song Ci) [38]. These studies show the possibility of the modern deep learning models working with classical Chinese 
language complexity and the possibility of conducting a better emotional content analysis. However, there are still needs 
to be met, especially in handling the problem of the absence of annotated datasets and the peculiarities of classical texts’ 
language. Despite these obstacles, the further development of Chinese classical literature sentiment analysis techniques 
provides wonderful prospects for further development of understanding of the historical and cultural piquancy through 
computational methods.
3  Materials and methods
This section introduced a novel unsupervised sentiment analysis framework/model, considering adopting novel 
deep-learning techniques such as GATs and BERT. The input document represents the document that will be ana­
lyzed in the proposed deep learning-based sentiment analysis framework for Chinese classical literature, containing 
raw text. The first stage of the treatment process is preprocessing text, during which the given document is toke­
nized (divided into smaller parts, e.g., words or subwords). After tokenization, unwanted words in sentences are 
removed to concentrate on the main content, as special tokens are added to mark sentences and other vital parts. 

--- Page 6 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
6 / 23
The sequences are padded or cropped to a given uniform size to make the text consistent with deep learning mod­
els. Any preprocessing of the text further passes it through the BERT encoder, a model for pre-training that produces 
contextualised word embeddings. These embeddings reflect what each word means in the specific context, and 
since the complexities of classical Chinese literature depend heavily on context, this is essential. The embeddings 
are further perfected by including sentiment-specific information using a sentiment lexicon, such that the model can 
more accurately determine emotional tones within the text. Later, the embeddings are passed through Graph Atten­
tion Network (GAT). In this step, a graph is built, in which words are the nodes, and the connections between them 
are created assuming correlations and semantic dependencies between them. The attention mechanism of the GAT 
allows ranking the most essential relationships among words, contributing to improving the embeddings. Lastly, the 
K-means algorithm places the improved embeddings in groups, which divides the text’s sentiment into three groups. 
Positive, negative, or neutral. This framework successfully overcomes the difficulties in the sentiment analysis of 
classical Chinese literature. It provides an insightful insight into the emotional and cultural aspects of the described 
literature and the proposed framework, as shown in Fig 1.
3.1  Dataset
The data set for this study is constructed from ancient Chinese text data collected to employ advanced natural language 
processing methods to predict linguistic tendencies and evaluate ancient Chinese classical works. The primary data 
Fig 1.  Overall framework of the proposed model. 
https://doi.org/10.1371/journal.pone.0330919.g001

--- Page 7 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
7 / 23
source used is a Kaggle repository, which the authors mentioned in the work [10]. This dataset also comprises classi­
cal, bardic, and archaic poetry and prose, such as the Shijing, among the most credible historical sources and classical 
Chinese prose. These books accurately view conventional Chinese writings and societal norms and encompass historical 
records, philosophical commentaries, old King stories, and divinity personalities. No superior form of Chinese literature 
has captured historical, cultural, and ethical situations at this level more than classical literature. The dataset is available 
on the Kaggle open data repository at the Kaggle Dataset Link because the dataset covers various genres and empha­
sizes full text, it provides a comprehensive background for sentiment analysis. For the need for sentiment analysis and 
search for several themes within these works, these writings are ideal as they demonstrate features of linguistic difficulty 
and a syntactic density of an expression and metaphors.
3.2  Preprocessing
In preprocessing, complex raw Chinese classical text is transformed into an input format that can be well understood by 
deep learning models such as BERT and GAT. This stage deals with certain challenges that come with reading classical 
Chinese texts, such as rhetoric, carrying out hermeneutics, and styles of writing that withhold the extended meaning of a 
text [39]. For this pre-treatment, the text was prepared for subsequent contextual embedding extraction and graph-based 
modelling.
Tokenization splits the raw text into non-numeric, semantically related and usable tokens that are easier to interpret by 
deep learning models. This is why, for example, the WordPiece tokenizer works especially well for the BERT model, as it 
can process Chinese compound words, phrases, and even out-of-vocabulary words at once. It splits these into subword 
components, preserving semantic meaning even for previously unseen words. To tokenize process maps, each word. wi, 
in a sentence to a tokenized representation T (wi):
	
T (wi) = Tokenizer (wi)	
(1)
For the entire sentence S =
{
w1, w2, w3 . . . . . . wn
}
, the tokenized sequence becomes:
	
T(S) = Tokenizer
({
w1, w2, . . . , wn
})
	
(2)
To ensure uniformity in sequence length (L), shorter sequences are padded with a unique token [PAD]. While longer 
sequences are truncated. This step is essential for batching inputs into fixed dimensions compatible with deep learning 
models.
	
Sprocessed =





S, IfS = L
Pad(S, L), IfS < L
Truncate(S, L), IfS > L





	
(3)
Special tokens are added to the sequences to denote specific roles as [CLS] Indicates the beginning of a sequence, 
providing a pooled embedding for classification. [SEP] Marks the end of a sequence or separates paired inputs.
	
Sspecial =
{
[CLS]
}
∪S ∪
{
[SEP]
}
	
(4)
Here, [CLS] and [SEP], are concatenated to the input sequence S.
This preprocessing pipeline ensures compatibility with the BERT-base-Chinese model and with GATs, paving the way 
for subsequent embedding extraction and sentiment classification.

--- Page 8 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
8 / 23
3.2.1  Contextualize embeddings extraction.  It could be suggested that contextualized embedding extraction can be 
considered an important stage of Chinese classical literature processing. After tokenization, padding and ADDINg special 
tokens, including [CLS] for classification and [SEP] as a separator, the resulting text is passed to the pre-trained BERT-
base-Chinese model. This model produces fixed dimensions for each token, with the semantic meaning of the token 
contained within the entire context of the message. BERT has learned the syntax and semantics of the words. BERT 
provides context for each word through embedding, which is the essence of downstream tasks such as understanding 
classical Chinese literature. This process also helps in accurately determining the actual effect of a particular token, 
adjusting the representation of the token in the context of its neighbor tokens. For a token ti in the sequence:
	
Stokenized =
{
t1, t2, . . . . . . tL
}
: ei = BERT (ti, Stokenized)	
(5)
Where ei is the contextualized embedding for ti. One of the last hidden layers of the BERT-base-Chinese model is the 
source of these embeddings. The embeddings capture the subtleties of ancient Chinese sentence construction. ei, which 
are constantly impacted by surrounding tokens. The BERT-base-Chinese model, optimized for modern and classical Chi­
nese, guarantees that the embeddings are suitable for handling intricate idioms and expressions. Fig 2 displays the BERT 
encoder for contextualized embeddings.
The output from this step is a matrix E ∈RLxD, where L is the sequence length and d is the embedding dimensionality. 
These embeddings serve as the foundation for subsequent enhancements and graph-based sentiment analysis.
3.3  Sentiment enriched embeddings
Enhance the BERT embeddings by integrating sentiment-specific information from an external NTUSD sentiment lexicon. 
This step tailors the embeddings to better reflect sentiment patterns relevant to Chinese classical literature. The NTUSD 
lexicon is used to assign sentiment scores si to each token. ti Based on its presence and polarity in the lexicon. If ti is not 
in the lexicon, si = 0.
	
si =
{
NTUSD(ti), if ti ∈Lexicon
0, otherwise
	
(6)
Combine the sentiment scores si with the BERT embeddings ei, to generate enriched embeddings es
i  A simple concate­
nation or weighted addition can be used:
Fig 2.  BERT Encoder for contextualised embeddings.
https://doi.org/10.1371/journal.pone.0330919.g002

--- Page 9 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
9 / 23
	
ei
(s) = Concat (ei, si)	
(7)
or
	
ei
(s) = ei + αsi	
(8)
Here in Eq. 8, α is a scaling factor. The output of this step is E(s) ∈RL × (d + 1) encapsulates contextual and 
­sentiment-specific information. These embeddings are then used to construct a relationship graph in the next stage.
3.4  Graph attention networks
Graph Attention Networks (GATs) are one of the types of neural networks designed to process graph-structured data. 
As opposed to the traditional convolutional neural networks (CNNs) that are intended for grid-like data (e.g., images), 
GATs specialize in working with non-Euclidean, irregular graph structures. In a graph, data points (nodes) are con­
nected with edges where the relationships are, and GATs use these relationships to update node representation. The 
central element of GATs is the attention mechanism, which enables the model to have different weights for the neigh­
boring nodes to aggregate their information. Rather than treating all the neighbors equally, GATs use the attention 
coefficients where the most important neighbors are emphasized so that the model can learn the contextual importance 
of different nodes. This self-attention mechanism allows GATs to effectively deal with dynamic and complex graph struc­
tures. GATs are used for sentiment analysis, especially for tasks related to text or language, to model dependencies 
of words or phrases as nodes in the graph. The attention mechanism allows the model to concentrate on contextually 
important word associations, such as co-occurrence or syntactic connections, essential in intentional and semantic 
variety detection in the text. By adapting to these weighted relationships of nodes, GATs significantly improve the model 
to capture complex contextual information. Fig 3 illustrates the architecture of the Graph Attention Network (GAT), high­
lighting the process of updating node representations based on the attention mechanism applied to neighboring nodes 
in the graph.
3.4.1  Graph layer.  In the proposed unsupervised sentiment analysis methodology, the graph construction step 
plays a critical role in modelling the relationships between words and their context and in facilitating clustering based 
on the semantic and syntactic dependencies of the words. In this step, we represent words as nodes and define edges 
based on their relationships, forming a graph G = (V, E), where V is the set of nodes (words) and E is the set of edges, 
respectively.
•	 Representing Words as Nodes: Each token ti from the sentiment-enriched embedding matrix E(s) is treated as a node 
vi.V =
{
v1, v2, . . . . . . ., vL
}
. Where is the number of tokens in the sequence. The feature vector of each node is initialized 
using its sentiment-enriched embedding.ei(s).
•	 Edges Creation among Nodes: Edges are created between nodes based on two criteria: Co-occurrence within a sen­
tence, in which two tokens occur. ti and tj When co-occur in the same sentence, an edge is created:
	
E(co–occurence) = {(vi , vj)|ti, tj ∈samesentence}	
(9)
The second is the Cosine Similarity of Word Embeddings, in which Edge weights are computed using cosine similarity 
between embeddings. ei(s) and ej(s).
	
wij = cosinesim(ei(s),ej(s)) =
ei(s).ej(s)
|ei(s)||ej(s)||	
(10)

--- Page 10 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
10 / 23
At the edge, the weight is calculated using Eq. 11 below:
	
wij = αEco–occurence + βcosinesim(ei(s),ej(s))	
(11)
•	 Graph Representation: The resulting graph is represented as:
Adjacency Matrix A: Encodes edges, where A[i][j] = wij, if an edge exists, otherwise 0.
Feature Matrix X: Encodes node features derived from E(s).
3.5  Graph attention networks processing
GAT processes the constructed G = (V, E) Update node features by aggregating information from neighbouring nodes. 
Each node vi attends to its neighbours vj ∈N(i). The Attention score αij, is computed as:
	
αij =
exp(Leaky Re LU

aT 
Wei(s)Wej(s)
 k ∈N(i)exp(Leaky Re LU

aT 
Wei(s)Wej(s)
	
(12)
Here above, Eq. 12 W  is the weight matrix for linear transformation, α is the Attention weight vector, and W  is the con­
catenation operation. To update features hi′, are computed as a weighted sum of the neighbours’ features:
	
hi′ = σ
(∑
j ∈N(i)αijWej
(s)
)
	
(13)
Fig 3.  Architecture of the GAT model.
https://doi.org/10.1371/journal.pone.0330919.g003

--- Page 11 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
11 / 23
Above, Eq. 13 σ is an activation function (e.g., ReLU). The output is an updated feature matrix H ∈RLxd′ is the dimen­
sionality of the updated embeddings.
Sentiment analysis has become useful for getting emotional and topical inferences from text, particularly for intricate 
literary works. Chinese classical literature, which is characterised by numerous metaphors, cultural references, and 
historical perceptions, provides a unique challenge for sentiment analysis. The suggested algorithm uses state-of-the-art 
methods like BERT embeddings, Graph Attention Networks (GAT), and K-means clustering to overcome these issues. It 
provides a working solution for analyzing classical texts’ emotional depth. Combined, these methods allow the framework 
to provide a more fine-grained sentiment understanding in literary works even without large datasets for annotation.
Algorithm 1. Sentiment Analysis using GAT.
Input:
• Raw text document T =
{
t1,t1,··· ,tn
}
 , where ti represents the ith word in the text.
Output:
• Sentiment labels yt ∈{positive, negative, neutral}for each document T.
  Step 1:Preprocessing
    • Tokenize text, remove stop words, and add special tokens.
    • Pad or truncate sequences to a fixed length L.
  Step 2:Sentiment Lexicon Enrichment
    • Retrieve sentiment score si, from the NTUSD lexicon and concatenate with BERT embeddings to 
form enriched embeddings Eenriched(wi) ∈Rd+1.
  Step 3:Graph Construction
    • Represent words as nodes and construct edges based on co-occurrence and cosine similarity of 
enriched embeddings.
  Step 4:Graph Attention Network (GAT) Processing
    • Compute attention scores αij for neighboring nodes and update node representations Hi by aggre­
gating weighted features:
	
Hi = σ

∑
j∈N(i)
αijWEenriched(wj)


	
  Step 5:Clustering
    • Apply K-means clustering on updated embeddings H to categorize sentiment (positive, negative, 
or neutral).
  Step 6:Output
    • Return sentiment labels based on assigned cluster centroids.
3.6  K-means clustering and sentiment labels assignment
The organization of data, as well as data pattern recognition, is boosted by the process of K-means clustering that cate­
gorises data points into clusters based on how close they are to the centroids. The before and after the application of the 
k-means clustering algorithm. They appear on the left as a pile of black dots, i.e., a haphazard and scattered formation 
with no clusters. The data has no natural structure or form and has not been sorted into humanly meaningful clusters. 
After K-means clustering (shown on the right side), the data points are sorted into clusters using different colored ellipses. 
Two clusters are created here, the first in cyan and the second in red. The clusters are being found based on how close 
the given points are to the clusters’ centroid, the center point of the given points within a particular group. The algorithm 
maps every data point to the closest centroid, and in doing so, the algorithm divides the points into groups. The workings 
of K-means clustering involve iteration until the within-cluster variance is minimized through shifting the centroids. At first, 
the centroids are picked randomly, and the points are assigned to the closest centroid. The centroids are computed again 
using the new points, and the process is carried out until convergence, when the centroids do not move substantially. As a 

--- Page 12 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
12 / 23
confusing technique, this clustering procedure is highly employed in segmentation, pattern recognition, and classification 
of problems. Fig 4 shows the K-means clustering process as data points are divided into unique sentiment types (positive, 
negative, or neutral) according to their proximity to the centroids of the clusters.
To classify sentiment, unsupervised clustering, k-means, is applied to the final node representations H output gener­
ated from GATS. Clustering partitions the nodes into k clusters, each corresponding to a sentiment class (positive, nega­
tive, neutral).
Cluster centroids are mapped to sentiment labels based on proximity to predefined sentiment vectors or a manual eval­
uation of cluster compositions. Let C = [C1, C2, . . . . . . , Ck], represent the clusters, and ci, denote the centroid of the cluster 
Ci. The label li for Ci is assigned based on:
	
li = argmaxs cosinsim(ci,vs)	
(14)
4  Performance evaluation
In this research, we proposed an unsupervised sentiment analysis model tailored to Chinese classical literature, lever­
aging advanced deep learning techniques such as the BERT model and GATs. The approach addresses the inherent 
challenges of analyzing texts characterized by complex linguistic structures, context-rich semantics, and cultural nuances, 
which are prevalent in classical Chinese works. By eliminating the reliance on labeled datasets, the model provides a scal­
able and effective solution for sentiment analysis in specialized domains like historical and philosophical writings, ancient 
poetry, and classical fiction. Our method enables fine-grained sentiment classification into positive, negative, and neutral 
classes by using sentiment-augmented graph embeddings in conjunction with contextualized embeddings. This evalua­
tion chapter demonstrates the versatility and effectiveness of the chosen model to detect affective attitudes and work with 
the tendencies in ethical themes in ancient Chinese writings by explaining how the model performed in the experiment, 
comparing the sentiment distribution in various literary genres, and assessing the model’s generality and expandability. 
Furthermore, we present detailed information about the implementation settings and hyperparameters applied in this work.
To measure the effectiveness of the sentiment model designed earlier, the authors rely on the following key perfor­
mance indicators: error rate, precision, sensitivity, and F-measure. They help determine the model’s effectiveness in 
classifying data into various types [28]. A brief explanation of each of the employed metrics is given below:
Accuracy: The measure of the model’s quality is determined by the number of properly classified instances over those 
present in the data set. This tells the extent of the success of the model.
	
Accuracy =
∑N
c=1 TPc
∑N
c=1 (TPc + FPc + FNc)	
(15)
Fig 4.  K-means clustering processing.
https://doi.org/10.1371/journal.pone.0330919.g004

--- Page 13 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
13 / 23
Precision: the measure of the fraction of actual positive instances expected in a set of positive instances predicted by 
the model. This feature is essential, especially when it is required to reduce false positives.
	
precisionmacro = 1
N
∑N
c=1
TPc
TPc + FPc	
(16)
Recall: The measure of the percentage of instances of a specific relevant sentiment expected to be classified correctly 
by the model. This is very important when reducing the number of desired false negatives.
	
recallmacro = 1
N
∑N
c=1
TPc
TPc + FNc	
(17)
F1-Score: It has the measure, calculated using the harmonic mean of precision and Recall measures. Unlike the oth­
ers, this measure does not depend on data distribution or abnormalities in data.
	
F1macro = 1
N
∑N
c=1 2 × precisionc × recallc
precisionc + recallc 	
(18)
In the above equations, TPc true positives for class c, FPc false positives for class, FNc false negatives for class c, TNc: 
true negatives for class c, and N is the total number of sentiment classes N = 3. These metrics will form a structure that 
will independently assess the strengths, weaknesses, and efficiency of leveraging these complexities to annotate classical 
Chinese literature. The proposed framework is, therefore, made more reliable and scalable by this comprehensive assess­
ment approach. The evaluation of sentiment classification is a macro-averaged three-class arrangement, in which the pre­
dicted sentiment categories, positive, negative, and neutral, are accorded equal weight. Precision, recall, and F1-scores 
are determined for every class, and then an average is taken to get the final scores. This technique does not suffer from 
the bias caused by class imbalance and provides unbiased evaluation on the part of all sentiment types. No binary classi­
fication or simplification of sentiment classes was carried out during evaluation.
4.1  Implementation settings
The proposed unsupervised Chinese classical literature sentiment analysis framework requires thoroughly chosen 
hyperparameters and a clearly defined implementation plan to report optimal outcomes. BERT-base-Chinese tokenizer 
is employed for vocabulary segmentation based on a pre-trained subword tokens lexicon. The sequence length is fixed, 
and padding is added where required to ensure consistent input shapes over batches. A batch size of 32 was chosen to 
optimise GPU memory consumption and stability of gradients, allowing for efficient training while respecting the computa­
tional cost. The BERT-base-Chinese model outputs the contextualised word embeddings of dimensionality 768, wherein 
understanding deep semantic and syntactic attributes of the given token in the context is represented. These embeddings 
are also enhanced with sentiment-specific scores from the NTUSD sentiment lexicon, leading to an overall 769 embed­
ding dimension per token. This augmentation improves the model’s representation of subtle emotional tones in literary 
texts. The graph representation emerges from these enriched embeddings, where nodes represent words while edges are 
established through sentence co-occurrence, cosine similarity of embeddings, and syntactic dependencies. The graph is 
processed via a GAT, consisting of two layers with eight attention heads each. Each attention head projects to a subspace 
of 64 dimensions, resulting in final node embeddings of 512 per node, capturing updated node representations. These 
layers learn to semantically and syntactically prioritise and dynamically aggregate neighbouring nodes’ information.
From the computational perspective, approximately 1.2 million trainable parameters are involved within the GAT com­
ponent, whereas the BERT-base-Chinese model accounts for about 110 million parameters. Thus, the total model com­
plexity approaches approximately 111.2 million parameters when BERT is fine-tuned, and 1.2 million parameters when 

--- Page 14 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
14 / 23
BERT is frozen. This configuration strikes a compelling balance between performance and scalability, which qualifies it for 
massive scaling of text processing workloads. Finally, K-Means clustering executes the ultimate sentiment classification 
stage through its unsupervised approach, which operates without trainable parameters. Node representations undergo 
clustering into three distinct sentiment categories: positive, negative, and neutral, based on a k-value of 3. This step aligns 
with the emotional distribution expected in analysing classical literary texts. To avoid overfitting, between layers, a dropout 
rate of 0.3 is used, randomly turning off neurons during training, to improve generalisation. Optimisation is done using the 
Adam optimiser, and a dynamic learning rate scheduler ensures smooth convergence with learning rate = 2 × 10 ⁻ ⁵. The 
model is trained for 10 epochs using early stopping concerning validation loss to avoid overtraining.
4.2  System requirements and specs
The training and evaluation of the proposed unsupervised sentiment analysis framework were conducted on a high-­
performance computational system to ensure efficiency and accuracy. The detailed system specifications are presented in 
Table 1 below:
4.3  Models for comparison
In this section, we compare our proposed model to the state of the art in Sentiment Analysis presented in the differ­
ent domains of Sentiment Analysis literature. To compare our framework with modern deep learning architectures and 
evaluate their effectiveness in this comparison. SentiCNN [40], Sentiment Convolutional Neural Network, evaluates the 
sentiments of the sentences by using contextual and sentiment-specific data with the help of the above architecture. The 
semantic relations between the words, including the contextual analysis, are captured by word embedding, while other 
lexicon data are obtained from standardized lexicons. With these two methods, SentiCNN can explore the word con­
text and sentiment cues in detail, thus having higher sentiment classification rates. The accuracy, precision, recall, and 
F-Score of the proposed SentiCNN model are 0.90, 0.89, 0.92 and 0.90. MLT-ML4 [41] shows that the multi-task learning 
framework is associated with the word-level latent topic distributions used in the topic model and the word-level attention 
vectors used in the sentiment classifier. A combination of sentiment categorization and topic modeling is made possible by 
mutual learning in the process distribution. The framework incorporates deep learning techniques, a Neural Topic Model 
for facilitating the modelling of topics, and Recurrent Neural Networks for handling time series data. The values of accu­
racy, precision, recall, and F- Score obtained in this study are 0.79, 0.81, 0.83, and 0.78, respectively.
Table 1.  System specification and requirements.
Component
Details
Hardware Environment
System Model
Dell Precision 7820 Tower
Processor
Intel Xeon W-2295, 3.0 GHz
Graphics Processing Unit (GPU)
NVIDIA GeForce RTX 3090
RAM (Random Access Memory)
128 GB DDR4
Storage (ROM)
2 TB NVMe SSD
Operating System
Windows 11
Software Environment
Python Version
3.9
Platform
Google Colab-Pro
Frameworks
TensorFlow 2.11 or PyTorch 1.13
CUDA Toolkit Version
11.7
Other Libraries
Transformers, Scikit-learn
https://doi.org/10.1371/journal.pone.0330919.t001

--- Page 15 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
15 / 23
B-MLCNN [42] is a deep-learning approach for document-level sentiment analysis. This method endeavoured to 
enhance the precision and understanding of sentiment analysis in larger textual contexts by integrating up-to-date 
deep learning prescriptions, such as transformer models and recurrent neural networks. The present study’s accu­
racy, precision, recall, and F-Score are 0.95, 0.88, 0.95, and 0.95, respectively. T-Caps [43] worked on the informa­
tion loss problem and proposed a sentiment categorization using a capsule network model. The model employs the 
Transformer to capture shallow text attributes to guarantee realistic primary feature extraction. The method asso­
ciates local textual features with holistic emotion cumulative favour/opposition through the capsule network, global 
parameter sharing and optimal dynamic routing update procedures. Statistical measures of this study are accuracy 
of 0.94, precision of 0.93, recall of 0.95, and F-Score of 0.93. KGAN [44] is a knowledge graph augmented network 
that records sentiment feature representations from several angles, including knowledge-based, context-based, and 
syntax-based. KGAN first learns the syntactic and contextual representations to fully extract the semantic character­
istics. After KGAN incorporates the knowledge graphs into the embedding space, an attention mechanism is used to 
extract the aspect-specific knowledge representations further. This work has an accuracy of 0.84, a precision of 0.82, 
a recall of 0.87, and an F-Score of 0.78. BERT-LLSTM-DL [9] is a state-of-the-art deep learning system designed for 
sentiment analysis of Chinese literature. Boundary loss works out the correct features by incorporating advanced 
deep learning algorithms, LSTM networks in sequential data analysis, and additional BERT for enhanced language 
representation. This work has an accuracy of 0.95, a precision of 0.96, a recall of 0.94, and an F-Score of 0.95. 
ChatGLM-6B [38], emphasising Song Dynasty poetry (Song Ci), refined the LLaMA 2 and Qwen LLMs for sentiment 
analysis on traditional Chinese literature. These fine-tuning techniques aimed to more precisely traverse and grasp 
Song Ci’s complex language and emotional content. Both supervised methods and reinforcement learning from user 
feedback are used in the fine-tuning process, which is especially intended to match the models with Song Ci’s histor­
ical and cultural background. This work has an accuracy of 0.91, a precision of 0.89, a recall of 0.92, and an F-Score 
of 0.84. Proposed Model, A specially developed unsupervised Chinese classical literature sentiment analysis model 
with state-of-the-art deep learning techniques such as the BERT model and GATs. The proposed method addresses 
challenges in analyzing texts where semantics and pragmatics involve socio-contextualized, non-linear, and layered 
concepts distinctive from the classical Chinese language. The approach represents a cost-effective solution to the 
problem of abstract domains, including classical fiction, ancient poetry, and philosophical and historical writings, 
thereby reducing the need for labeled datasets. The results of the proposed study includes an accuracy of 0.95, pre­
cision of 0.97, recall of 0.96, and F-Score of 0.91, respectively.
4.4  Overall performance of the model
The suggested sentiment analysis model, which has been developed with the help of GATs for comprehending intricate 
connections between words and BERT for contextualized word representations, is analysed in this section. A literature 
area characterized by both dense linguistic and thematic context, Classical Chinese literature, was employed to evaluate 
the model. The outcomes demonstrate how well the model correctly divides attitudes into three main groups: neutral, 
negative, and positive. These problems and patients’ experiences can be categorized into three categories, consisting of 
neutral, negative, and positive. The results of the suggested model for multiple iterations are presented in Table 2 below. 
First, the accuracy of the proposed model is increasing and exceeds 0.97, which means that it can control the nuances of 
classical Chinese literature. The high accuracy exhibited by the model shows its accuracy in sentiment classification, even 
for the most syntactic density that accompanies literary and historical writings. One of the most significant advantages of 
the proposed model is that it carries out the basic function of combining BERT and GATs to classify feelings successfully. 
Regarding measurement precision, the model delivers average predictability rating values of 0.96 to 0.98. The following 
results show how much the model reduces false positives and accurately identifies relevant sentiment categories. Sus­
taining such a high degree of accuracy is crucial to ensure that appropriate sentiment classifications that align with current 

--- Page 16 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
16 / 23
requirements are achieved in traditional Chinese literature’s strong historical and thematic undertones. Likewise, the recall 
scores range from 0.95 to 0.98, which indicates that the model can identify a large fraction of truly positive thinking.
This section of the model’s function is crucial, given that it also reveals the ability to identify sentiment in less obvious 
cases, which is challenging to identify in large text analyses when working with complex structures of literary genres. 
These F1 scores, which involve the fine equilibrium between precipitation and recall that consistently remains above 
0.91, underpin the model’s efficiency and reliability. This also demonstrates that the model is accurate for the purpose 
and capable of handling the relevant recall/precision compromise, so the system is properly set to get large amounts of 
relevant and pertinent sentiment data. The same performance testing is done to get more insights into the performance 
of our suggested model, as done by the research team [5]. The decision to use text sentiment analysis to assess the 
various Chinese literary works has been presented in Table 3. Rows in the given table are specific to the particular sen­
tence; the sentiment scores are positive, negative, and neutral. The table also shows the projected sentiment associated 
with the category that scored the highest out of the three. A few significant patterns become apparent while looking over 
the sentiment results. For instance, texts like “这本书是非常有趣” (This book is fascinating.) and “这个产品的质量非常好” 
(The quality of this product is very good.) received strong positive sentiment scores, leading to the prediction of a positive 
sentiment. On the other hand, texts such as “这个电影太令人失望了” (This movie is too disappointing) and “这次旅行经
历真是太糟糕了” (This travel experience is terrible) scored highly on the negative sentiment scale, resulting in pessimistic 
predictions. Additionally, some texts reflect a balance of sentiments, which led to neutral sentiment predictions. For exam­
ple, “这个餐厅的食物味道很好, 但服务很慢” (The food in this restaurant is good, but the service is slow.) and “我喜欢这个
城市的风景, 但交通拥堵” (I like the scenery of this city, but the traffic is congested) received similar scores across positive, 
negative, and neutral categories, indicating a mixed or neutral sentiment. In light of the preceding results, the model’s 
applicability in categorising the sentiments in pre-modern Chinese works is evident from the analysis of contextual mean­
ings, whereby the texts are sorted according to the positive, negative, or neutral emotions conveyed.
Table 2.  Results of proposed model on various iterations.
Iteration
Accuracy
Precision
Recall
F1-score
Iteration 1
0.94
0.96
0.95
0.91
Iteration 2
0.94
0.96
0.95
0.90
Iteration 3
0.95
0.97
0.96
0.91
Iteration 4
0.96
0.97
0.96
0.91
Iteration 5
0.97
0.98
0.98
0.89
https://doi.org/10.1371/journal.pone.0330919.t002
Table 3.  Proposed model scores and sentiment prediction.
Chinese Text
Positive Score
Negative score
Neutral Score
Predicted/Assigned Sentiment
这本书是非常有趣的
0.97
0.01
0.06
Positive
这个餐厅的食物味道很好, 但服务很慢
0.21
0.33
0.45
Neutral
这个电影太令人失望了
0.04
0.89
0.21
Negative
这个产品的质量非常好
0.91
0.02
0.31
Positive
这次旅行经历真是太糟糕了
0.03
0.74
0.21
Negative
这个软件的用户界面太复杂了
0.01
0.98
0.03
Negative
我对这个服务感到非常满意
0.98
0.08
0.21
Positive
我喜欢这个城市的风景, 但交通拥堵
0.31
0.01
0.84
Neutral
这个演员的表演非常精彩, 但剧情太简单了
0.32
0.12
0.65
Neutral
我觉得这个活动很有意思
0.85
0.01
0.32
Positive
https://doi.org/10.1371/journal.pone.0330919.t003

--- Page 17 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
17 / 23
Table 2 compares the suggested model with the state-of-the-art deep learning models for sentiment analysis. Over 
the years, our technique outperformed the baseline models in all measures used for evaluation, namely accuracy, 
precision, recall, and F1 score. Specifically, this extensive improvement demonstrates how effectively adding BERT 
embeddings, GATs, and unsupervised clustering adaptively preserves intricate syntactic/semantic features of traditional 
Chinese literature. The ability of the proposed model to optimize the deep learning requirements indicates that the 
model is adaptive to certain challenges posed by classical literature, including difficult language structures and hidden 
sentiment signification. For one, the model could be more precise at sentiment classification even when there are very 
limited amounts of annotated data, thanks to the incorporation of graph-based representation learning and domain-­
specific sentiment lexica.
While this framework presents deep analytic results for both thematic and emotional features of Chinese classical litera­
ture, the sentiment analysis part provides insights. Finding cultural moods for texts of various epochs, historical documents, 
and philosophical and poetic works will help reveal intellectual and poetic moods more thoroughly. On this premise, a better 
understanding and probing of sentiment in various literary settings becomes possible with potentially real-world applications 
in literary criticism, history, and culture. It eliminates the problem of a lack of labelled data sets characteristic of many spe­
cific disciplines, such as historical Chinese literature. This scalability and flexibility of the method make it especially suitable 
for other domains in which only a small portion of the data is labelled. It is also interesting to note that integrating BERT and 
Graph Attention Networks (GATs) works well. BERT achieves sophistication by using contextual embeddings with syntactic 
and semantic nuances; conversely, GATs add value to the model in analyzing essential linkages between the words and 
relations between texts. This interaction improves the model’s ability to identify sentiment within the more complex struc­
tures of classical literature. The performance indicators calculated in model accuracy, precision, recall, and the F1 score 
show how useful the model is. This makes it capable of learning from extensive data without getting too fixated on some 
stereotyped results, which makes it highly robust. These results show that applying the proposed framework to a classical 
Chinese literature text corpus and extending it to another textual dataset enlightens the natural language processing study.
The performance sets the contrast of the proposed sentiment analysis model with a series of state-of-the-art models 
based on top metrics: accuracy, precision, recall, and F1-score. All the scores are macro-averaged across three sentiment 
categories, i.e., negative, neutral, and positive. The proposed model is better than several comparison models, gaining an 
accuracy of 0.95, a precision of 0.97, a recall of 0.96, and an F1-score of 0.91. It is at least as good as models such as 
BERT-LLSTM-DL and B-MLCNN, which delivered similar accuracy and recall with lower precision. The proposed model 
outperforms MLT-ML4, which have lower metric scores. These findings are shown in Table 4, and the model proves useful 
in sentiment classification in complex textual data, particularly in classical literature. It should be noted that all scores are 
macro-averaged over the three sentiment categories (negative, neutral, and positive). No binary simplification was used.
We also performed a direct empirical comparison with two state-of-the-art foundation models, ChatGPT-4o and Deep­
Seek R1, in a zero-shot learning environment to thoroughly evaluate the efficacy of our suggested unsupervised sen­
timent analysis framework. The same input dataset of literary sentences in classical Chinese (with translations where 
necessary) and a uniform instruction format were given to each model.
“Classify the following Chinese literary text’s sentiment as either positive, negative, or neutral.”
Following that, the same performance metrics used in our study Accuracy, Precision, Recall, and F1-score were used 
to assess the predicted sentiments from ChatGPT-4o and DeepSeek R1. Table 5 presents a summary of the evaluation 
results. With an F1-score of 0.91, the suggested model continuously outperforms these powerful general-purpose models 
on all metrics, while ChatGPT-4o and DeepSeek R1 achieve 0.90 and 0.88, F1-scores respectively.
These results imply that although foundation models such as ChatGPT-4o and DeepSeek R1 show remarkable gen­
eralization abilities even in zero-shot sentiment classification, they might still have limitations when used on linguistically 

--- Page 18 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
18 / 23
complex, domain-specific corpora like Chinese classical literature. It can be difficult to decipher these texts without specific 
fine-tuning or domain adaptation because they frequently rely heavily on idioms, metaphorical structures, historical allu­
sions, and philosophical allusions. In contrast our framework is better design to better align with the intricate stylistic and 
emotional characteristics of classical Chinese literature especially in low-resource and label-scarce scenarios where LLMs 
often fall short unless specifically adapted or prompted with domain knowledge.
However, given the exceptional adaptability and flexibility of contemporary LLMs, we think our strategy can be complemen­
tary rather than competitive. Future research will focus on hybrid approaches that combine domain-specific modeling using 
lexicons and graph architectures with general-purpose reasoning from LLMs, utilizing the best features of both paradigms.
4.5  Generalization and scalability of proposed model
The proposed unsupervised sentiment analysis model has better data generality and expansiveness in textual styles. It suc­
cessfully handles large amounts of data, such as large and intricate data structures, including extended collections of ancient 
Chinese literature, with no decline in efficiency by using BERT embeddings and Graph Attention Networks. This scalability is 
important mainly for processing large bodies of text to investigate inter-period, inter-genre, and inter-style consistency. This 
guided nature of the model is made even more effective by the ability of the program to function in an unsupervised way 
and, thus, to successfully apply a large number of types of ancient Chinese literature that include fiction, poetry, history, and 
philosophies of China. This versatility supports the analysis of sentiment and other temporal patterns and attributes of highly 
numerous and disparate topics or themes within various genres. Moreover, the generalization capacities associated with 
the proposed model go beyond the context of Chinese literature and extend to cross-linguistic and cross-cultural analyses 
of sentiment and topics in historical documents. Because of such strong positive characteristics as performance, scalability, 
and flexibility for different domains and text types, the proposed model can become an effective tool for sentiment analysis 
in collecting ancient texts. It applies even in contemporary usage analysis, whereby context-induced ensemble intelligibility 
is pertinent in tasks such as literature or social media analysis. Furthermore, the outcomes of the corresponding iterations of 
the developed model, depicted in Fig 5, evidence its flexibility and effectiveness for various processes.
4.6  Discussion
This study proposed an unsupervised sentiment analysis model, combining BERT-based embeddings with GATs, 
significantly improving Chinese classical literature analysis. Traditionally, classical Chinese texts contain complex 
Table 4.  Comparison of the proposed model with existing models.
Existing Models
Accuracy
Precision
Recall
F1-score
SentiCNN [40]
0.90
0.89
0.92
0.90
MLT-ML4 [41]
0.79
0.81
0.83
0.78
B-MLCNN [42]
0.95
0.88
0.95
0.95
BERT-LLSTM-DL [9]
0.95
0.96
0.94
0.95
Proposed Model
0.95
0.97
0.96
0.91
https://doi.org/10.1371/journal.pone.0330919.t004
Table 5.  Comparison of the proposed model with ChatGPT-4o and DeepSeek R1.
Models
Accuracy
Precision
Recall
F1-score
Proposed Model
0.95
0.97
0.96
0.91
ChatGPT-4o
0.90
0.89
0.91
0.90
DeepSeek R1
0.88
0.87
0.89
0.88
https://doi.org/10.1371/journal.pone.0330919.t005

--- Page 19 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
19 / 23
long-range dependencies and contextual subtleties, and the model outperformed the aforementioned traditional meth­
ods, such as LSTMs and recurrent neural networks (RNNs). Its distinct feature is that it can work without labelled data­
sets, which is particularly appropriate in classical literature, where one often lacks data. The model effectively classifies 
sentiment via a graph-based approach with unsupervised learning, not requiring costly annotations. It leverages BERT 
embeddings marginally enhanced with sentiment data from specialized lexicons to interpret classical Chinese texts’ 
complicated emotional and cultural qualities. Graph-based modelling through GATs was particularly effective in under­
standing word relationship-based texts. With GAT’s attention mechanism, which selects what is most relevant from 
the word relationship, this method addresses classical Chinese’s complex syntactic and semantic structure. Sentiment 
analysis was performed using unsupervised clustering, with K-Means-specific algorithms that helped group words with 
similar sentiment to increase their accuracy and depth. The computational efficiency of the model was a consideration 
of design. Unlike LSTM and RNN, which tend to be computationally expensive, especially with large datasets, our 
approach is scalable to large volumes of text, making it a more palatable solution for classical literature datasets of 
larger scales. The framework’s scalability allows it to be used for Chinese classical texts (e.g., Tang dynasty dramas) 
and other sizeable unannotated text corpora across various domains. The model proposed for sentiment analysis of 
Chinese classical literature is promising. It addresses some key challenges, shows that such accuracy is scalable and 
efficient, and offers important insights about how sentiment can be classified in the case of such long texts. Yet, it also 
points out what can be refined and how it might be further developed. Fig 6 shows the result of the proposed VS Com­
parison models.
The performance compares of the proposed model with several state-of-the-art (SOTA) methods in sentiment analysis. 
Wang et al. [43] achieved strong performance with an accuracy of 0.94, precision of 0.93, recall of 0.95, and F1-score 
of 0.93. Zhong et al. [44] showed lower results, with accuracy of 0.84, precision of 0.82, recall of 0.87, and F1-score of 
0.78, indicating a less effective model. Ihnaini et al. [40] reported accuracy of 0.91, precision of 0.89, recall of 0.92, and 
F1-score of 0.84, outperforming Zhong et al. but still lagging behind Wang et al. The proposed model, however, outper­
forms all comparison models with the highest accuracy of 0.95, precision of 0.97, recall 0.96, and F1-score 0.91, demon­
strating its superior ability to classify sentiment in complex texts. Table 6 highlights the effectiveness of the proposed 
approach in sentiment analysis.
Fig 5.  Proposed model results on different iterations.
https://doi.org/10.1371/journal.pone.0330919.g005

--- Page 20 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
20 / 23
5  Conclusion and future work
This study presents an innovative unsupervised sentiment analysis framework customized for Chinese classical litera­
ture based on the state-of-the-art deep learning model, such as BERT-based embeddings, Graph Attention Networks 
(GATs) and K-means clustering. The main difficulties of analyzing classical Chinese texts are that there is no annotated 
dataset and the complicated implicit expressions of emotion in the language. The traditional methods of sentiment anal­
ysis that involve supervised learning and labelled data struggle to capture the nuance and metaphor within these works 
of literature. To overcome these challenges, our framework exploits the use of BERT to generate contextualized word 
embeddings that can capture the meaning of a word in its specific context in the text. This step ensures that the model 
successfully interprets the complexities of classical Chinese, since the language context of the words significantly explains 
the meaning of words. Additionally, the model integrates the sentiment-explicit knowledge from the NTUSD sentiment lex­
icon to enhance the BERT embeddings to better understand the emotional content of the text. Graph Attention Networks 
(GATs) also bring an extra tinge of intricacy to the form of designing the relationship between the words in the text as 
nodes in a graph with co-occurrence and semantic dependencies as the edges. The attention mechanism present in GATs 
enables the model to pay more attention to the most useful word relationships, which boosts the quality of node represen­
tations and accuracy in sentiment classification. Scores of this approach over traditional sentiment analysis models, e.g., 
LSTM, BiLSTM and CNN, based on accuracy, precision, recall and F1-score are shown in the table below. The model 
successfully classifies the sentiments in Chinese classical literature into positive, negative, or neutral categories, revealing 
Fig 6.  Proposed VS comparison models result.
https://doi.org/10.1371/journal.pone.0330919.g006
Table 6.  The proposed model compares with state-of-the-art (SOTA) methods.
Study
Accuracy
Precision
Recall
F1-score
Wang et al [43]
0.94
0.93
0.95
0.93
Zhong et al [44]
0.84
0.82
0.87
0.78
Ihnaini et al [38]
0.91
0.89
0.92
0.84
Proposed Model
0.95
0.97
0.96
0.91
https://doi.org/10.1371/journal.pone.0330919.t006

--- Page 21 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
21 / 23
the texts’ emotional depth and cultural nuances. This work is a major improvement in using deep learning for literary anal­
ysis, providing a strong sentiment analysis tool for historical and culturally enriched domains. Although the results are very 
promising, there are several areas that one could improve and develop upon. A major limitation is that a fixed sentiment 
lexicon, such as NTUSD, is used, and all the emotional nuances and metaphors used in classical Chinese literature will 
be covered by this lexicon.
Although the presented model has demonstrated positive results, there are areas for improvement and future study. 
The use of a fixed sentiment Lexicon (e.g., NTUSD) that may not be able to exhaust the complicated feelings and meta­
phors implied in classical writings is also a limitation. Future research may include enriching and adjusting the lexicon to 
accommodate other emotions and cultural aspects. In addition, applying supervised learning techniques based on anno­
tated datasets in a particular domain can improve the model’s accuracy and robustness. Further studies could also test 
the use of the framework in other forms of historical literature and multilingual datasets, allowing for cross-linguistic senti­
ment analysis. Another line of development is the inclusion of fine-grained sentiment analysis that would enable sensing 
subtler emotional changes in longer texts.
Supporting information
S1 Dataset.  Classical Chinese Texts Corpus: This corpus/repository includes the classical Chinese literature 
used in the experiments of sentiment analysis presented in this paper. It contains the minimal set of data needed to 
reproduce the findings that have been presented in the manuscript/article, translated into English. 
(ZIP)
S2 Module-Wise Code Files.  This package of Python scripts implements the proposed unsupervised sentiment 
analysis approach. It contains a pre-processing script (preprocess.py), a script that calculates BERT embeddings 
(bert_encoder.py), a script to enrich embeddings with sentiment (enrich_embeddings.py), a script to build the graph 
(build_graph.py), a script to compute a graph attention module (gat_module.py), a script to do clustering and evaluation 
(clustering_and_evaluation.py), and utility/evaluation scripts. These files permit a complete replication of the experiments. 
(ZIP)
S3 LLM Comparison Code.  There are Python notebooks and scripts to build a zero-shot sentiment classifier 
using ChatGPT-4o and DeepSeek r1. These codes replicate the comparative evaluation experiments documented in the 
Results section. 
(ZIP)
S4 Model Output-JSON Files.  All intermediate and final results produced by the proposed framework have been 
stored in this folder and include: Tokenized input samples, Enriched embeddings, Graph construction outputs, 
Cluster labels (positive, negative, neutral), Final cluster centroids, Performance metrics (accuracy, precision, 
recall, F1-score). The results of these output directly contribute to the outcomes shown in Tables 4 and 5, and Figures 5 
and 6. 
(ZIP)
S5 True Labels Reference File.  A JSON file with ground truth sentiment labels used in evaluation and compari­
son to LLM prediction. 
(ZIP)
S6 LLM Prediction Outputs.  JSON files with the zero-shot sentiment classification predictions/outputs by 
ChatGPT-4o and DeepSeek r1. These outputs were directly compared with our model. 
(ZIP)

--- Page 22 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
22 / 23
Author contributions
Data curation: Xiaohan Yu, Jin Wang.
Methodology: Xiaohan Yu.
Writing – original draft: Xiaohan Yu, Jin Wang.
Writing – review & editing: Xiaohan Yu, Jin Wang.
References
	 1.	
Cui J, Wang Z, Ho S-B, Cambria E. Survey on sentiment analysis: evolution of research methods and topics. Artif Intell Rev. 2023;56(8):8469–510. 
https://doi.org/10.1007/s10462-022-10386-z PMID: 36628328
	 2.	
Cambria E, Mao R, Chen M, Wang Z, Ho SB. Seven pillars for the future of artificial intelligence. IEEE Intelligent Systems. 2023;38(6):62–9.
	 3.	
He J, Wumaier A, Kadeer Z, Sun W, Xin X, Zheng L. A local and global context focus multilingual learning model for aspect-based sentiment analy­
sis. IEEE Access. 2022;10:84135–46.
	 4.	
Liu B. Sentiment analysis: mining opinions, sentiments, and emotions. Cambridge University Press. 2020.
	 5.	
Yan X, Jian F, Sun B. SAKG-BERT: Enabling language representation with knowledge graphs for Chinese sentiment analysis. IEEE Access. 
2021;9:101695–701.
	 6.	
Khan S, Uddin I, Noor S, AlQahtani SA, Ahmad N. N6-methyladenine identification using deep learning and discriminative feature integration. BMC 
Med Genomics. 2025;18(1):58. https://doi.org/10.1186/s12920-025-02131-6 PMID: 40158097
	 7.	
Abdullah T, Ahmet A. Deep learning in sentiment analysis: Recent architectures. ACM Comput Surv. 2022;55(8):1–37.
	 8.	
Wu J, Zhu T, Zhu J, Li T, Wang C. A Optimized BERT for Multimodal Sentiment Analysis. ACM Trans Multimedia Comput Commun Appl. 
2023;19(2s):1–12. https://doi.org/10.1145/3566126
	 9.	
Shen X. Sentiment analysis of modern Chinese literature based on deep learning. Journal of Electrical Systems. 2024;20(6s):1565–74.
	10.	
Su F, Zhao S. Analysis of Chinese classical literature texts and prediction of internet language trends based on natural language processing. Jour­
nal of Computational Methods in Sciences and Engineering. 2024;25(2):1246–60. https://doi.org/10.1177/14727978241298488
	11.	
Li Q. A survey on text classification: From traditional to deep learning. ACM Transactions on Intelligent Systems and Technology. 2022;13(2):1–41.
	12.	
Zhang W, Li X, Deng Y, Bing L, Lam W. A Survey on Aspect-Based Sentiment Analysis: Tasks, Methods, and Challenges. IEEE Trans Knowl Data 
Eng. 2022;35(11):11019–38. https://doi.org/10.1109/tkde.2022.3230975
	13.	
Mabokela KR, Celik T, Raborife MR. Multilingual sentiment analysis for under-resourced languages: a systematic review of the landscape. IEEE 
Access. 2022;11:15996–6020.
	14.	
Calzolari N, Kan M-Y, Hoste V, Lenci A, Sakti S, Xue N. Proceedings of the 2024 Joint International Conference on Computational Linguistics, Lan­
guage Resources and Evaluation (LREC-COLING 2024). In: Proceedings of the 2024 Joint International Conference on Computational Linguistics, 
Language Resources and Evaluation (LREC-COLING 2024), 2024.
	15.	
Zhang K, Hu M, Ren F, Hu P. Sentiment analysis of Chinese product reviews based on BERT word vector and hierarchical bidirectional LSTM. In: 
2021 IEEE International Conference on Computer Science, Artificial Intelligence and Electronic Engineering (CSAIEE), 2021. 9–14.
	16.	
Shen Y, et al. Sentiment analysis for tang poetry based on imagery aided and classifier fusion. In: Artificial Intelligence for Communications and 
Networks: First EAI International Conference, AICON 2019, Harbin, China, May 25–26, 2019, Proceedings, Part II, 2019. 283–90.
	17.	
Ashish V. Attention is all you need. Advances in Neural Information Processing Systems. 2017;30:I.
	18.	
Devlin J. Bert: Pre-training of deep bidirectional transformers for language understanding. arXiv preprint arXiv. 2018.
	19.	
Wang Z, Huang D, Cui J, Zhang X, Ho S-B, Cambria E. A review of Chinese sentiment analysis: subjects, methods, and trends. Artif Intell Rev. 
2025;58(3). https://doi.org/10.1007/s10462-024-10988-9
	20.	
Khan S, Uddin I, Khan M, Iqbal N, Alshanbari HM, Ahmad B, et al. Sequence based model using deep neural network and hybrid features for iden­
tification of 5-hydroxymethylcytosine modification. Sci Rep. 2024;14(1):9116. https://doi.org/10.1038/s41598-024-59777-y PMID: 38643305
	21.	
Du Z, Huang AG, Wermers R, Wu W. Language and domain specificity: A Chinese financial sentiment dictionary. Review of Finance. 
2022;26(3):673–719.
	22.	
Guo Y, Wang T, Chen W, Kaptchuk TJ, Li X, Gao X, et al. Acceptability of Traditional Chinese Medicine in Chinese People Based on 10-Year’s Real 
World Study With Mutiple Big Data Mining. Front Public Health. 2022;9:811730. https://doi.org/10.3389/fpubh.2021.811730 PMID: 35111723
	23.	
Zhang S, Wei Z, Wang Y, Liao T. Sentiment analysis of Chinese micro-blog text based on extended sentiment dictionary. Future Generation Com­
puter Systems. 2018;81:395–403.
	24.	
Wang B, Huang Y, Yuan Z, Li X. A multi-granularity fuzzy computing model for sentiment classification of Chinese reviews. Journal of Intelligent & 
Fuzzy Systems. 2016;30(3):1445–60.

--- Page 23 ---

PLOS One | https://doi.org/10.1371/journal.pone.0330919  September 23, 2025
23 / 23
	25.	
Lipenkova J. A system for fine-grained aspect-based sentiment analysis of Chinese. In: Proceedings of ACL-IJCNLP 2015 System Demonstrations, 
2015. https://doi.org/10.3115/v1/p15-4010
	26.	
Yang AM, Lin JH, Zhou YM, Chen J. Research on building a Chinese sentiment lexicon based on SO-PMI. Applied Mechanics and Materials. 
2013;263:1688–93.
	27.	
Zheng L, Wang H, Gao S. Sentimental feature selection for sentiment analysis of Chinese online reviews. International journal of machine learning 
and cybernetics. 2018;9:75–84.
	28.	
Zhang D, Xu H, Su Z, Xu Y. Chinese comments sentiment classification based on word2vec and SVMperf. Expert Systems with Applications. 
2015;42(4):1857–63. https://doi.org/10.1016/j.eswa.2014.09.011
	29.	
Wang Z, Parth Y. Extreme learning machine for multi-class sentiment classification of tweets. Proceedings of ELM-2015 Volume 1: Theory, Algo­
rithms and Applications (I). Springer. 2016. 1–11.
	30.	
Bai H, Yu G. A Weibo-based approach to disaster informatics: incidents monitor in post-disaster situation via Weibo text negative sentiment analy­
sis. Nat Hazards. 2016;83(2):1177–96. https://doi.org/10.1007/s11069-016-2370-5
	31.	
Yan G, He W, Shen J, Tang C. A bilingual approach for conducting Chinese and English social media sentiment analysis. Computer Networks. 
2014;75:491–503.
	32.	
Su Z, Xu H, Zhang D, Xu Y. Chinese sentiment classification using a neural network tool–Word2vec. In: 2014 International Conference on Multi­
sensor Fusion and Information Integration for Intelligent Systems (MFI), 2014. 1–6.
	33.	
Hu Z, Wang Z, Wang Y, Tan AH. MSRL-Net: A multi-level semantic relation-enhanced learning network for aspect-based sentiment analysis. Expert 
Systems with Applications. 2023;217:119492.
	34.	
Zhao M, Yang J, Zhang J, Wang S. Aggregated graph convolutional networks for aspect-based sentiment classification. Information Sciences. 
2022;600:73–93.
	35.	
Liu X, Tang T, Ding N. Social network sentiment classification method combined Chinese text syntax with graph convolutional neural network. 
Egyptian Informatics Journal. 2022;23(1):1–12.
	36.	
Liu H, Chen X, Liu X. A Study of the Application of Weight Distributing Method Combining Sentiment Dictionary and TF-IDF for Text Sentiment 
Analysis. IEEE Access. 2022;10:32280–9. https://doi.org/10.1109/access.2022.3160172
	37.	
Liu Z, Wan G, Zuo X, Liu Y. Sentiment analysis of Chinese ancient poetry based on multidimensional knowledge attention. Digital Scholarship in 
the Humanities. 2025;40(1):214–26.
	38.	
Ihnaini B, Sun W, Cai Y, Xu Z, Sangi R. Sentiment analysis of song dynasty classical poetry using fine-tuned large language models: a study with 
LLMs. In: 2024 7th International Conference on Artificial Intelligence and Big Data (ICAIBD), 2024. 590–7.
	39.	
Uddin I, AlQahtani SA, Noor S, Khan S. Deep-m6Am: a deep learning model for identifying N6, 2′-O-Dimethyladenosine (m6Am) sites using hybrid 
features. AIMSBOA. 2025;12(1):145–61. https://doi.org/10.3934/bioeng.2025006
	40.	
Huang M, Xie H, Rao Y, Liu Y, Poon LK, Wang FL. Lexicon-based sentiment convolutional neural networks for online review analysis. IEEE Trans­
actions on Affective Computing. 2020;13(3):1337–48.
	41.	
Gui L, Leng J, Zhou J, Xu R, He Y. Multi Task Mutual Learning for Joint Sentiment Classification and Topic Detection. IEEE Trans Knowl Data Eng. 
2022;34(4):1915–27. https://doi.org/10.1109/tkde.2020.2999489
	42.	
Atandoh P, Zhang F, Adu-Gyamfi D, Atandoh PH, Nuhoho RE. Integrated deep learning paradigm for document-based sentiment analysis. Journal 
of King Saud University - Computer and Information Sciences. 2023;35(7):101578. https://doi.org/10.1016/j.jksuci.2023.101578
	43.	
Wang J, Du J, Shao Y, Li A. Sentiment analysis of online travel reviews based on capsule network and sentiment lexicon. In: China Intelligent Net­
worked Things Conference, 2022. 92–106.
	44.	
Zhong Q, Ding L, Liu J, Du B, Jin H, Tao D. Knowledge Graph Augmented Network Towards Multiview Representation Learning for Aspect-Based 
Sentiment Analysis. IEEE Trans Knowl Data Eng. 2023;35(10):10098–111. https://doi.org/10.1109/tkde.2023.3250499

```
