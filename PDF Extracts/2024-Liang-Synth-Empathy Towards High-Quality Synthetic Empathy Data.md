---
title: "2024-Liang-Synth-Empathy Towards High-Quality Synthetic Empathy Data - PDF Extract"
source_pdf: "2024-Liang-Synth-Empathy Towards High-Quality Synthetic Empathy Data.pdf"
pages: 10
extracted_at: "2026-02-07T17:00:46.594209"
---

# PDF Extract: 2024-Liang-Synth-Empathy Towards High-Quality Synthetic Empathy Data

**Source PDF:** 2024-Liang-Synth-Empathy Towards High-Quality Synthetic Empathy Data.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

Synth-Empathy: Towards High-Quality Synthetic Empathy Data
Hao Liang†‡, Linzhuang Sun†♦, Jingxuan Wei♦, Xijie Huang‡, Linkun Sun♣, Bihui Yu♦, Conghui He♠,
Wentao Zhang‡∗
‡Peking University ♦University of Chinese Academy of Sciences ♠Shanghai AI Laboratory
♣Institute of Information Engineering, Chinese Academy of Sciences
†hao.liang@stu.pku.edu.cn, †sunlinzhuang21@mails.ucas.ac.cn, wentao.zhang@pku.edu.cn
ABSTRACT
In recent years, with the rapid advancements in large language
models (LLMs), achieving excellent empathetic response capabil-
ities has become a crucial prerequisite. Consequently, managing
and understanding empathetic datasets have gained increasing sig-
nificance. However, empathetic data are typically human-labeled,
leading to insufficient datasets and wasted human labor. In this
work, we present Synth-Empathy, an LLM-based data generation
and quality and diversity selection pipeline that automatically gen-
erates high-quality empathetic data while discarding low-quality
data. With the data generated from a low empathetic model, we
are able to further improve empathetic response performance and
achieve state-of-the-art (SoTA) results across multiple benchmarks.
Moreover, our model achieves SoTA performance on various human
evaluation benchmarks, demonstrating its effectiveness and robust-
ness in real-world applications. Furthermore, we show the trade-off
between data quantity and quality, providing insights into empa-
thetic data generation and selection. The codebase and data are
made available at https://github.com/Aurora-slz/Synth-Empathy.
1
INTRODUCTION
In recent years, with the rapid advancements in large language
models (LLMs) [26, 36], data management has become a crucial
aspect of these technologies [5, 9, 24, 25, 37]. At the same time,
Bai et al. [1] also demonstrates that data processing, selection, and
management can significantly influence the performance of LLMs.
Empathy, the ability to understand and share the feelings of
another, is a critical component of human social interaction and
communication. It allows individuals to connect with others on an
emotional level, fostering relationships and promoting prosocial
behavior [6]. In the future of Human-central Artificial General Intel-
ligence (AGI), excellent empathetic response capability is a crucial
prerequisite, which focuses on equipping LLMs to understand and
respond appropriately to human feelings [31].
In previous research, empathy modeling has predominantly con-
centrated on human-labeled data [10, 38, 47, 48] and integrating
information through modifications to the model architecture [11, 32,
51]. While the importance of model architectures is well acknowl-
edged, the quality and quantity of data are also critical [3, 44]. Ad-
ditionally, Fernandez et al. [9] indicates that new data management
methods are needed for LLMs due to their massive data require-
ments. Previous empathetic studies underscore the significance of
† The first two authors have equal contributions.
∗Corresponding Author
Figure 1: Comparison of our Synth-Empathy data-trained
model with previous SoTA models. The results demonstrate
that our model achieves superior performance on multiple
empathetic benchmarks.
data-centric approaches. They frequently overlook effective data
generation approaches, leading to the following two key challenges:
C1. High Cost of Human-Labor. Previous methods rely on
human labor for the creation of empathetic datasets [10, 38, 47,
48]. However, this process can be extremely costly and requires
substantial human effort.
C2. Poor Effectiveness. Previous research [11, 15, 19, 32, 38, 50]
has only a limited amount of data. Despite efforts by Sun et al.
[34] to improve model performance, the empathetic effectiveness
remains constrained. More empathetic data is needed to train high-
performance empathetic models.
To address these issues, as shown in Figure 3, we propose a
three-step empathetic data generation and curation pipeline and
subsequently train an empathetic LLM. First, we utilize prompts to
generate empathetic responses. Next, we apply domain knowledge
for quality selection to curate the empathetic data. Finally, we con-
duct diversity selection for further data curation. With the curated
arXiv:2407.21669v2  [cs.CL]  10 Aug 2024

--- Page 2 ---

Hao Liang†‡, Linzhuang Sun†♦, Jingxuan Wei♦, Xijie Huang‡, Linkun Sun♣, Bihui Yu♦, Conghui He♠, Wentao Zhang‡∗
I was so curious about the 
sender, but there was no return 
address or note.
That must have added to the 
mystery and intrigue - were 
you feeling a bit frustrated 
or excited?
I've been feeling a bit down 
lately, and this surprise parcel 
really brightened my day.
That must have added to the 
mystery and intrigue - were 
you feeling a bit frustrated 
or excited?
Hi, I feel so lonely sometimes 
because all my friends live in 
a different country.
Oh, I am sure you are lonely. 
Maybe you can join some 
kind of club that lets you 
meet new friends? 
I was thinking about it! I 
wanted to join a group for 
local moms. 
That is a good idea ! This way 
you can also meet friends for 
yourself , but also maybe meet 
new friend ’s for your children 
to hang out with while you do 
with their moms ! 
Speaker
Speaker
Speaker
Speaker
Listener
Listener
Listener
Listener
(a) ED Dataset
(b) Generated Dataset
Figure 2: Comparison of Data Examples. (a) An example from
the ED dataset. (b) An example from the synthetic dataset.
synthetic dataset, we fine-tune an LLM and achieve state-of-the-art
(SoTA) empathetic response performance.
The core contributions of this paper are summarized as follows:
• New Perspective. Limited data and low effectiveness are
significant impediments to the practical adoption of em-
pathy models. To the best of our knowledge, this study
represents the first approach to generate data from scratch
to address these challenges.
• New Method. We propose a new data generation and cu-
ration pipeline for empathy, introducing the first generated
high-quality empathy dataset. Utilizing our meticulously
curated synthetic dataset, we pioneer the integration of
synthetic data to empathetic model training. Our method,
which utilized curated synthetic data, enables robust effec-
tive, and user-friendly empathetic response.
• SoTA Performance. (1) Effectiveness in Empathetic Re-
sponse. By utilizing the synthetic empathetic response data
to fine-tune LLMs, our method can achieve SoTA perfor-
mance in multiple benchmarks, as shown in Figure 3. At
the same time, we achieve SoTA performance on human
evaluation benchmarks. This means our model have high
application potential.
(2) No Human Labor. By utilizing curated prompts and
LLMs, we can obtain high-quality empathetic responses
without the need for human labor. With a meticulously
designed data curation pipeline, as illustrated in Figure 3,
we achieve high-quality data, as demonstrated in Figure
2 and Figure 5. This approach significantly reduces the
requirement for human labor.
2
RELATED WORK
2.1
Empathetic Response Generation
Imbuing models with empathy to enhance emotional experience
is a crucial aspect of AGI. Rashkin et al. [31] constructed the ED
dataset, the most authoritative dataset for measuring the empathic
abilities of models, which has since become a benchmark for em-
pathy research. Building on this dataset, numerous researchers
have focused on improving models’ empathy comprehension by
integrating emotional labels and external knowledge.
Sabour et al. [32] introduces commonsense knowledge inference
into this task by enriching historical conversation data with the
pre-trained COEMT model [2]. Diverged from this approach, Li
et al. [16] incorporate external knowledge through Graph Neural
Networks (GNN) for context encoding. Additionally, Wang et al.
[38] posit that using detailed sentiment labels can improve the accu-
racy of capturing user sentiment and puts forward a sentiment loss
mechanism with multiple levels of granularity to enhance model
training. Moreover, Kim et al. [14] strives to provide empathetic
responses by analyzing context at the word level. Chen and Liang
[4] employed a emotion detection algorithm based on psychological
principles to pinpoint important statements in conversations. Zhao
et al. [49] take a different approach by not only recognizing the
emotions of others but also assessing saved model emotional state.
Furthermore, Qian et al. [29] divides the empathetic response task
into two steps: verifying the semantic content and infusing emo-
tional expression.
In the LLM era, many researchs explore ways to boost the em-
pathic potential of models through meticulous design of prompts [30,
39, 46]. Differently, Sun et al. [35] delves into the general sensibility
and rationality, exploring their respective contributions to empathy.
However, the importance of fine-grained sensibility and rationality
cognition for empathy still lacks comprehensive investigation.
2.2
Data Quality and Data Selection
The advent of large language models has brought about a substan-
tial increase in the volume of training data. [27, 36] In this scenario,
the quality and quantity of data become paramount. LLMs, trained
on vast amounts of data, can capture subtle nuances and complex
patterns in language, excelling in various natural language pro-
cessing tasks. However, the increase in data volume also brings
new challenges, particularly in data management, cleaning, and
annotation. [1] In this section, we mainly discuss the effectiveness
of data quality and data selection.
Data Quality. : High-quality data can significantly enhance the
performance of models [23]. As the volume of data increases, ensur-
ing high data quality becomes more challenging because it requires
more resources for data cleaning, selection and annotation. [1]
Poor quality data can lead to models learning incorrect patterns
and making inaccurate predictions.
Data Selection. : LLMs-based methods were commonly used in
data selection. [1] For instance, Du et al. [7] leverages DeBERTa [12]
for scoring, retaining high-quality data, and combining it with the k-
center greedy algorithm to select diverse data. Chen et al. [3] score
the accuracy of data using ChatGPT to pick out high-quality data.
Xu et al. [44] use GPT-4 to rewrite data to increase their complexity
and then streamline it by reducing its variety and improving its
quality. Liu et al. [20] train two models using ChatGPT’s labeled
data to score the quality and complexity of the data. Lu et al. [22]
rely on ChatGPT to tag each instance, defining its complexity and
diversity based on these tags. Parkar et al. [28] first cluster the data,
and then use GPT-4 to select high-quality data for each cluster.

--- Page 3 ---

Synth-Empathy: Towards High-Quality Synthetic Empathy Data
Context
Conversation
… …
ED
Conversation
Turn #1 Speaker
Turn #1 Listener
… …
Turn #n Response
Aug
Conversation
Turn #1 Speaker
Turn #1 Listener
… …
Turn #n Response
Aug
Conversation
Turn #1 Speaker
Turn #1 Listener
… …
Turn #n Response
Context
Conversation
… …
Context
Conversation
… …
Discard
Conversation
… …
Context
Conversation
… …
Context
Conversation
… …
Context
Conversation
… …
EP
Conversation
… …
Domain
Conversation
Turn #1 Speaker
Turn #1 Listener
… …
Turn #n Response
Domain
Conversation
Turn #1 Speaker
Turn #1 Listener
… …
Turn #n Response
Turn #n
Response-DR
Turn #n
Response-DR
> 𝑇
D!
D"
Finetune
Inference
… …
… …
Discriminator
Quality Data Selection
2
Diversity Data Selection
3
KCentergreedy
Low Diversity Set
High Diversity Set
Inference
Selected Data
Empathetic Data Generation
Original Context: {context}
Original Response: {response}
You are an empathetic psychologist with 
powerful sensibility and rationality. Please 
generate at least three rounds of completely 
new emotional context and corresponding 
empathetic response. The newly generated 
multi-round context should satisfy semantic 
continuity. The response should be empathetic 
and should not exceed 30 words.
Round:
Context:
Response:
1
Finetune
𝐸𝐷∪𝐷!
Vanilla LLM
Empathetic LLM
4
Empathetic Model Training
LLM
Select
Discard
Figure 3: Empathetic Data Generation and Curation Pipeline, which is composed by (1) Empathetic Data Generation module,
(2) Quality Data Selection module, (3) Diversity Data Selection module and (4) Empathetic Model Training module.
Given the critical role of data quality and selection in enhancing
model performance, our paper focuses on leveraging advanced data
diversity and quality selection techniques to optimize empathetic
data quality. By employing methods that integrate data features
and similarity scores, we aim to efficiently identify and utilize high-
quality data for empathetic response.
2.3
Data Generation
Data has always been the key driver behind the success of large lan-
guage models (LLMs). Recent advancements of LLMs are largely due
to the availability of large-scale, diverse, and high-quality datasets
for training these models [18] . However, the scarcity of data and
the high costs present substantial challenges in obtaining such
datasets [13, 42, 43]. Recent advancements in generating synthetic
data and improving the performance of LLMs have shown promis-
ing results across various domains. Synthetic data holds great po-
tential in building large-scale, high-quality datasets. Researchers
have explored multiple approaches, from leveraging differential
privacy to creating instruction-tuning frameworks, to enhance the
quality, diversity, and utility of synthetic data [21, 40, 41, 45]. A
key component in generating high-quality synthetic datasets is
precise alignment. Fan et al. [8] introduce REALIGN, a method that
enhances the quality of instruction data by reformatting responses
to better align with pre-established criteria and evidence, thereby
improving LLMs’ alignment with human values while minimizing
human annotation and model hallucinations. Li et al. [17] build a
high-quality instruction-following language model by automati-
cally labeling human-written text with corresponding instructions
and demonstrating highly effective self-alignment.
In the field of empathetic response, the construction of genera-
tive datasets remains relatively underexplored. Empathetic models
primarily rely on the utilization and curation of existing datasets.
Approaches such as those by Sun et al. [34] have attempted to
improve empathetic response performance through data selection
methods. However, these methods still face challenges due to the
lack of high-quality empathetic response data.
3
METHOD
In this section, we first introduce the empathetic data generation
method in subsection 3.1. Then we introduce the newly designed
empathetic quality selection module in subsection 3.2. Additionally,
we introduce the diversity selection in subsection 3.3. We demon-
strated the high-quality of our dataset in subsection 3.4. With the
curated dataset, we are able to fine-tune empathetic models.
3.1
Empathetic Data Generation
In this subsection, we introduce the data generation method. Our
data generation is based on the authoritative EmpatheticDialogues
(ED) dataset [31], which consists of 25,000 daily conversations en-
compassing 32 uniformly distributed emotional labels. By utilizing
the prompt in Figure 3(1), we generate empathetic responses based
on the high-quality ED dataset.

--- Page 4 ---

Hao Liang†‡, Linzhuang Sun†♦, Jingxuan Wei♦, Xijie Huang‡, Linkun Sun♣, Bihui Yu♦, Conghui He♠, Wentao Zhang‡∗
You will be given a conversation between two 
individuals. You will then be given one potential 
response for the next turn in the conversation. 
Your task is to rate the responses on one metric. 
Please make sure you read and understand these 
instructions carefully. Please keep this document 
open while reviewing and refer to it as needed.
Evaluation Criteria:
Naturalness (1-3) Is the response naturally written?
- A score of 1 (bad) means that the response is 
unnatural.
- A score of 2 (ok) means the response is strange, 
but not entirely unnatural.
- A score of 3 (good) means that the response is 
natural.
Evaluation Steps:
1. Read the conversation between the two 
individuals.
2. Read the potential response for the next turn in 
the conversation.
3. Evaluate the response based on its naturalness, 
using the provided criteria.
4. Assign a rating score of 1, 2, or 3 based on the 
evaluation.
Example:
Conversation History:
{Document}
Response:
{Response}
Evaluation Form (scores ONLY):
- Naturalness:
You will be given a conversation between two 
individuals. You will then be given one potential 
response for the next turn in the conversation. 
Your task is to rate the responses on one metric. 
Please make sure you read and understand these 
instructions carefully. Please keep this document 
open while reviewing and refer to it as needed.
Evaluation Criteria:
Coherence (1-3) Does the response serve as a valid 
continuation of the conversation history?
- A score of 1 (no) means that the response 
drastically changes topic or ignores the conversation 
history.
- A score of 2 (somewhat) means the response refers 
to the conversation history in a limited capacity (e.g., 
in a generic way) and shifts the conversation topic.
- A score of 3 (yes) means the response is on topic 
and strongly acknowledges the conversation history.
Evaluation Steps:
1. Read the conversation history.
2. Read the potential response.
3. Evaluate the coherence of the response based on 
the conversation history.
4. Assign a score of 1, 2, or 3 for coherence.
Example:
Conversation History:
{Document}
Response:
{Response}
Evaluation Form (scores ONLY):
- Coherence:
You will be given a conversation between two individuals. 
You will then be given one potential response for the next 
turn in the conversation. 
Your task is to rate the responses on one metric. 
Please make sure you read and understand these 
instructions carefully. Please keep this document open 
while reviewing, and refer to it as needed.
Evaluation Criteria:
Empathy (1-3) Does the response demonstrate empathy 
towards the user's feelings or situation?
- A score of 1 (bad) means the response lacks empathy and 
does not acknowledge the user's feelings or situation.
- A score of 2 (ok) means the response shows some 
understanding of the user's feelings or situation but could 
be more empathetic.
- A score of 3 (good) means the response demonstrates a 
strong sense of empathy towards the user's feelings or 
situation and acknowledges them effectively.
Evaluation Steps:
1. Read the conversation history.
2. Read the potential response.
3. Evaluate the empathy of the response based on the 
conversation history.
4. Assign a score of 1, 2, or 3 for empathy.
Example:
Conversation History:
{Document}
Response:
{Response}
Evaluation Form (scores ONLY):
- Empathy:
(a) Coherence Evaluation
(b) Naturalness Evaluation
(c) Empathy Evaluation
Figure 4: Data Quality Evaluation Prompts. (a) Assessing the coherence of the data. (b) Assessing the naturalness of the data. (c)
Assessing the empathy of the data.
The formula for generating data using the prompt is as follows:
Synthetic Dataset = LLM(Prompt(ED Data))
(1)
Following the formula above, we generate more than 250k em-
pathetic data points for further selection.
3.2
Empathetic Data Quality Selection
In this subsection, we introduce the data quality selection process
for empathetic data. Similar to subsection 3.1, we utilize the ED
dataset as the baseline and select data with an empathetic style
similar to the ED dataset. The selection process is shown in Figure
3(2) and involves the following steps:
Empathetic Discriminator. We fine-tune a LLM on the ED
dataset to serve as the discriminator, denoted as 𝑀𝐷. This discrimi-
nator is trained to produce responses that mimic the high-quality
empathetic style of the ED dataset, denoted as 𝐷𝐸𝐷.
𝑀𝐷= SFT(LLM; 𝐷𝐸𝐷)
(2)
Similarity Based Quality Selection. In generating empathetic
response data, we first use the discriminator 𝑀𝐷to answer the
question. Then, we use the SoTA embedding model gte-qwen2-7b-
instruct to embed the model’s response and the generated response.
We calculate the similarity between the discriminator’s response
and the generated response. We only select the responses with
similarity higher than the threshold 𝑇. The optimized procedure is
as follows:
(1) Use the discriminator 𝑀𝐷to answer the question, obtaining
the response 𝑟𝐷:
𝑟𝐷= 𝑀𝐷(question)
(2) Use gte-qwen2-7b-instruct to embed the discriminator’s
response 𝑟𝐷and the generated response 𝑟𝐺, obtaining the
embedding vectors 𝐸𝐷and 𝐸𝐺:
𝐸𝐷= gte-qwen2-7b-instruct(𝑟𝐷)
𝐸𝐺= gte-qwen2-7b-instruct(𝑟𝐺)
(3) Calculate the similarity 𝑆between the discriminator’s re-
sponse 𝑟𝐷and the generated response 𝑟𝐺:
𝑆=
𝐸𝐷· 𝐸𝐺
∥𝐸𝐷∥∥𝐸𝐺∥
(4) Select the generated response 𝑟𝐺if the similarity 𝑆is higher
than the Domain Knowledge (DK) threshold 𝑇:
𝑟𝐺is selected if 𝑆> 𝑇
With the similarity selection based on the empathetic discrimi-
nator, we obtain a high-quality synthetic dataset.

--- Page 5 ---

Synth-Empathy: Towards High-Quality Synthetic Empathy Data
(a) Pre-filtered Generation Data (Avg. 2.73)
(b) Post-filtered Generation Data (Avg. 2.96)
Figure 5: Scores of Coherence, Naturalness, and Empathy for Generated Data. (a) Scores before applying the data filtering
strategy. (b) Scores after applying the data filtering strategy.
Original Context: {context}\nOriginal Response: {response}\n\nYou
are an empathetic psychologist with powerful sensibility and 
rationality. Please generate at least three rounds of completely new 
emotional context and corresponding empathetic response. The newly 
generated multi-round context should satisfy semantic continuity. The 
response should be empathetic and should not exceed 30 
words.\n\nRound:\nContext:\nResponse:
Original Context: {context} \nOriginal Response: {response} \n\nYou
are an empathetic psychologist. Please generate at least three rounds 
of completely new emotional context and corresponding empathetic 
response. The response should be empathetic and should not exceed 
30 words. \n\nRound 1\n\nRound 2\n\nRound 3\n\nRound 4
Prompt-1
Prompt-2
Figure 6: Prompts for generating empathetic responses.
3.3
Empathetic Data Diversity Selection
In this subsection, we introduce the diversity selection method.
The aim of diversity selection is to maximize the minimum dis-
tance between selected data points, ensuring a diverse subset. The
algorithm can be formally described as follows:
Given a dataset 𝑋= {𝑥1,𝑥2, . . . ,𝑥𝑛}, our goal is to select a subset
𝑆⊆𝑋of size 𝑘that maximizes the minimum distance between any
point in 𝑋and the closest point in 𝑆. The objective function is:
max
𝑆⊆𝑋,|𝑆|=𝑘min
𝑥∈𝑋min
𝑠∈𝑆𝑑(𝑥,𝑠)
where 𝑑(𝑥,𝑠) denotes the distance between points 𝑥and 𝑠.
As shown in Figure 3(3), we select the KCenterGreedy [33] algo-
rithm for its robustness and quick computation. Using the KCen-
terGreedy algorithm, we obtain a high-diversity synthetic dataset.
3.4
High Quality Generated Empathetic Data
In this section, we introduce an analysis of the quality of our gen-
erated dataset. We use a three-dimensional evaluation to assess
the quality of our curated data. Using the prompts in Figure 4, we
evaluate the dataset’s coherence, naturalness, and empathy, scoring
each from 1 to 3 points.
As shown in Figure 5, our method significantly improves the
dataset’s quality. The average score increased from 2.65 to 2.88.
Additionally, more than 95% of the data achieved full marks, demon-
strating the high quality of our curated synthetic dataset.
With high-quality generated empathetic response pairs, we can
train a more effective empathetic model. Additionally, the empa-
thetic response generation pipeline alleviates concerns about the
quantity of empathetic data.

--- Page 6 ---

Hao Liang†‡, Linzhuang Sun†♦, Jingxuan Wei♦, Xijie Huang‡, Linkun Sun♣, Bihui Yu♦, Conghui He♠, Wentao Zhang‡∗
4
EXPERIMENTS
In this section, we first introduce the experimental setups, including
data selection and the training process. We then aim to answer the
following questions to verify the effectiveness and robustness of
our proposed Synth-Empathy model:
Q1: Can we fine-tune an empathetic model to achieve state-of-the-
art (SoTA) performance with the curated synthetic data?
Q2: Can our model achieve favorable human evaluation results,
given the importance of human evaluation for empathy?
Q3: Can we determine the trade-off between data quantity and
quality to guide future empathetic data selection?
Q4: Are the quality selection and diversity selection modules nec-
essary to enhance model performance?
4.1
Experimental Setup
4.1.1
Datasets. We evaluate our methods on the widely used EM-
PATHETICDIALOGUES dataset, which includes 25k multi-turn
empathetic conversations. Each conversation involves a speaker
and a listener, with an average of 4.31 turns per dialog. This dataset
contains 32 evenly distributed emotion labels, with each conversa-
tion being associated with a specific label. And in order to guarantee
the equity of the comparison baselines, we follow the same dataset
division as the previous research method by splitting the dataset
into training, validation, and test sets in an 8:1:1 ratio.
4.1.2
Baselines. The baseline models are listed as follows:
1. SEEK: Employ multi-granularity sentiment labels at the word,
sentence, and dialogue levels to enhance emotional understanding.
2. CASE: Enhancing the cognitive capabilities of models with ex-
ternal knowledge sources, COMET and ConceptNet, to improve
the quality of empathetic responses. 3. ESCM: Leveraging dynamic
emotion-semantic vectors along with dependency trees to direct
the model in generating empathetic responses. 4. Qwen1.5-7B-F.T.:
Conducting SFT of Qwen1.5-7B-Chat model using ED dataset. 5.
LLaMA3-8B-F.T.: Conducting SFT of LLaMA3-8B-Instruct model
using ED dataset. 6. LLaMA3-8B: Generating empathetic response
through designed prompt based on LLaMA3-8B-Instruct1 model. 7.
Mixtral-8x7B: Generating empathetic response through designed
prompt based on Mixtral-8x7B-Instruct2 model. 8. Qwen1.5-72B-
Chat: Generating empathetic response through designed prompt
based on Qwen1.5-72B-Chat3 model.
4.1.3
Evaluation. To offer a thorough evaluation of our model’s
capabilities, we assess its performance through both automatic
metrics and human evaluations.
Automatic Evaluation Metrics: For automatic evaluation, we
employ corpus-level BLEU (B-1 to B-4), sentence-level ROUGE (R-1,
R-2), and Distinct (Dist-1, Dist-2) metrics. BLEU and ROUGE scores
measure the similarity between the generated text and the reference
text, with higher scores reflecting greater similarity. Meanwhile,
Distinct-N assesses content diversity, where higher values indi-
cate a broader range of diverse representations. CIDEr aligns more
closely with human judgment of sentence similarity by employing
TF-IDF to assign varying weights to different n-grams. Specifically,
1https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
2https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1
3https://huggingface.co/Qwen/Qwen1.5-72B-Chat
it reduces the weight of frequently occurring phrases while in-
creasing the weight of less common ones, thereby reflecting the
distinctiveness and significance of the n-grams in the evaluation
process. Besides, we employed xxx to assess semantic similarity
from the perspective of vector embedding.
Human Evaluation Metrics: For human evaluation, we choose
the following metrics: Coherence, Empathy, Informativeness, and
Continuity. Coherence: Assesses how well the model’s generated
text aligns with the intended response. Empathy: Measures the
model’s capacity to grasp the speaker’s situation and convey appro-
priate concern. Informativeness: Evaluates the extent of informa-
tion provided in the responses produced by the model. Continuity:
Reflects the model’s effectiveness in maintaining the flow of the
conversation.
Then, the A/B test is conducted to evaluate the effectiveness of
our model in comparison to several baseline models. Specifically,
200 examples are randomly selected from the test dataset. Each
example is paired with two responses: one generated by our model
and the other by a baseline model. Three evaluators assess each
pair of responses, determining a winner, loser, or tie based on above
four criteria.
4.1.4
Settings. All experiments are carried out on the machine
equipped with 8 NVIDIA A100 GPUs, a 120-core CPU, and 960GB
of memory. The inference process of LLMs is implemented on the
Vllm framework with version 0.4.1.
4.2
Main Experiments
To address Q1, in this section, we evaluated various models on
their performance in generating empathetic responses using several
metrics, as summarized in Table 1.
Our model was fine-tuned on the dataset combining the ED train-
ing set and our generated dataset. Our generated dataset comprises
data with 𝑆greater than 60 and diversity selection.
Our model consistently outperformed other models across most
metrics. Specifically, it achieved the highest BLEU scores, with 22.05
for BLEU-1, 10.53 for BLEU-2, 5.99 for BLEU-3, and 3.77 for BLEU-4,
demonstrating its superior ability to generate text closely aligned
with reference translations. In terms of Distinct metrics, which
gauge the diversity of generated responses, our model scored 3.23
for Distinct-1 and 18.84 for Distinct-2, indicating a strong balance
between diversity and coherence.
Our model also excelled in the Rouge metrics, attaining scores of
18.72 for Rouge-1, 5.27 for Rouge-2, and 16.88 for Rouge-L. These
scores reflect its effectiveness in capturing the essential content
of the reference texts and producing more contextually relevant
responses. In the CIDEr metric, which assesses content relevance
and richness, our model achieved a score of 26.96, the highest among
the compared models, highlighting its effectiveness in generating
captioning that aligns closely with human judgments of content
relevance and informativeness.
Furthermore, in embedding-based evaluations using BERT, our
model demonstrated superior performance with a BERT-P score of
20.5, a BERT-R score of 18.2, and a BERT-F1 score of 19.4. These
results indicate that our model generates text with more meaningful
and contextually accurate semantic representations compared to
other models.

--- Page 7 ---

Synth-Empathy: Towards High-Quality Synthetic Empathy Data
Table 1: Results of the automatic evaluation on ED test dataset and the best performance are highlighted in bold. Our model
trained on synthetic empathetic response data outperforms all other SoTA methods.
BLEU
Distinct
Rouge
CIDEr
Embedding
B-1
B-2
B-3
B-4
D-1
D-2
R-1
R-2
R-l
CIDEr
BERT-P
BERT-R
BERT-F1
SEEK
10.77
4.40
2.02
1.08
0.68
2.81
12.74
2.94
12.07
9.95
19.9
8.2
14.0
CASE
15.21
6.97
3.75
2.27
0.78
4.34
16.14
4.38
14.99
19.11
20.5
14.1
17.3
ESCM
19.42
9.30
4.21
2.44
1.13
3.56
17.75
3.73
15.95
16.38
16.8
14.5
15.7
Qwen1.5-7B-F.T.
22.00
10.31
5.70
3.53
3.19
19.48
18.12
4.87
16.35
22.04
20.1
17.8
19.0
LLaMA3-8B-F.T.
21.28
9.69
5.18
3.11
4.02
24.00
17.93
4.76
16.07
24.02
20.1
17.9
19.0
LLaMA3-8B
13.17
4.42
1.92
1.02
2.69
18.70
14.12
1.68
11.69
2.28
5.8
11.9
8.9
Mixtral-8x7B
14.66
4.72
2.11
1.10
3.30
21.13
14.54
1.69
12.20
4.43
11.6
11.4
11.6
Qwen1.5-72B
14.19
4.85
2.27
1.23
3.29
22.68
13.83
1.97
11.73
5.04
11.9
12.8
12.4
ours
22.05
10.53
5.99
3.77
3.23
18.84
18.72
5.27
16.88
26.96
20.5
18.2
19.4
SEEK
CASE
ESCM
Qwen1.5-7B-F.T.
LLaMA3-8B-F.T.
0
10
20
30
40
50
60
Result
Win
Lose
Tie
Figure 7: Human A/B test evaluation.
Overall, these results confirm that our model provides superior
performance across a range of metrics, demonstrating its effective-
ness in generating high-quality and diverse outputs. The promising
results highlight the effectiveness of the high-quality synthetic
dataset, thereby introducing a new paradigm for using synthetic
data in empathetic responses.
4.3
Human Evaluation
To address Q2, we conducted a series of A/B tests to test the online
performance. The comparative analysis includes our online model
versus SEEK, CASE, ESCM, Qwen1.5-7B-F.T., and LLaMA3-8B-F.T.
The results of these tests are summarized in Figure 7.
The results of our A/B tests demonstrate that our model signif-
icantly outperforms SEEK, CASE, and ESCM, with win rates of
66%, 63.3%, and 57.9%, respectively. When compared with the more
advanced models, Qwen1.5-7B-F.T. and LLaMA3-8B-F.T., our model
still demonstrates competitive performance. Against Qwen1.5-7B-
F.T., our model secures a win rate of 31% and maintains a reasonable
loss rate of 19.8%, with ties at 49.2%. Similarly, our model achieves
a win rate of 26% against LLaMA3-8B-F.T., with a loss rate of 15.1%
and the highest tie rate of 58.9%.
Overall, our model’s strong performance in human evaluations
underscores its practicality and user-friendliness. These results in-
dicate that our model is not only effective but also well-received by
human evaluators, highlighting its potential for real-world applica-
tions.
4.4
Data Quality and Data Quantity
To address Q3, we analyzed the trade-off between the DK thresh-
old, the similarity threshold in section 3.2, and the CIDEr score
to demonstrate the robustness of our approach. Table 2 and Fig-
ure 8 present detailed experimental results, comparing various DK
thresholds across the Qwen1.5-7B and LLaMA3-8B models using
two different data generation prompts.
As the DK threshold increases from 50 to 70, the CIDEr score of
Qwen1.5-7B with Prompt 1 initially rises from 20.45 to a peak of
25.07 at a DK threshold of 60, before slightly decreasing to 22.45
at a DK threshold of 70. For the LLaMA3-8B model, the CIDEr
score shows a similar pattern, peaking at 24.34 with a DK threshold
of 60, before decreasing at higher DK ratios. In terms of Prompt
2, the Qwen1.5-7B model demonstrates an increase in the CIDEr
score from 20.36 at a DK threshold of 50 to a peak of 26.96 at a
DK threshold of 60, followed by a slight decline. This observation
corroborates a clear trade-off trend, emphasizing that an optimal
DK threshold enhances the generation of empathetic responses.
The consistency of the trade-off pattern across different models
and prompts underscores the robustness of our method. Regard-
less of the specific model or prompt used, the CIDEr score consis-
tently peaks around the DK threshold of 60, demonstrating that our
method effectively balances data retention and response quality.
Additionally, by analyzing the trade-off between data quantity and
quality, we provide guidance for optimal empathetic selection meth-
ods in the future. Utilizing the best threshold can achieve superior
empathetic performance and select the appropriate dataset, thereby
avoiding the waste of computational resources.
4.5
Ablation Study
To address Q4, we provide the following ablation study. We remove
the data quality selection module and the data diversity selection
module to demonstrate the effectiveness of our Synth-Empathy
pipeline.
Excluding Data Quality Selection Module. When excluding the
data quality selection module, the performance of the model de-
creases across all benchmarks, as shown in Table 3. For both the
Qwen1.5-7B and LLaMA-8B-Instruct models, this exclusion results

--- Page 8 ---

Hao Liang†‡, Linzhuang Sun†♦, Jingxuan Wei♦, Xijie Huang‡, Linkun Sun♣, Bihui Yu♦, Conghui He♠, Wentao Zhang‡∗
Table 2: Trade-off between the DK ratio and the quality of generated empathetic responses.
Threshold
Models
Prompt
BLEU
Rouge
CIDEr
Data
B-1
B-2
B-3
B-4
R-1
R-2
R-l
50
Qwen1.5-7B
Prompt1
21.31
9.52
5.12
3.10
17.66
4.61
15.95
20.45
115,898
55
20.97
9.39
5.20
3.21
17.75
4.59
15.93
21.24
77,182
60
22.48
10.47
5.76
3.54
19.04
5.21
17.16
25.07
45,298
65
22.04
10.26
5.72
3.53
18.13
4.95
16.40
22.49
22,705
70
21.60
9.77
5.32
3.27
18.20
4.880
16.32
22.45
9,791
50
LLaMA3-8B-Instruct
Prompt1
20.25
9.28
5.07
3.10
17.62
4.60
15.98
23.91
115,898
55
20.47
9.35
5.08
3.07
17.64
4.60
15.96
24.23
77,182
60
21.35
9.87
5.42
3.33
17.98
4.84
16.25
24.34
45,298
65
20.08
9.23
5.05
3.09
17.53
4.78
15.95
24.26
22,705
70
20.53
9.15
4.93
2.99
17.20
4.22
15.45
21.87
9,791
50
Qwen1.5-7B
Prompt2
20.59
9.17
4.97
3.01
17.38
4.44
15.53
20.36
64,020
55
21.61
9.80
5.37
3.28
17.82
4.71
16.01
21.55
37,043
60
22.05
10.53
5.99
3.77
18.72
5.27
16.88
26.96
18,789
65
22.80
10.77
6.04
3.74
18.81
5.15
17.00
25.53
8,227
70
22.69
10.65
5.86
3.58
19.02
5.23
17.20
25.34
3,041
Figure 8: Visualization of trade-off between the DK ratio and
the CIDEr score of generated empathetic responses.
in decreased performance, demonstrating the necessity of the qual-
ity selection module.
Excluding Data Diversity Selection Module. Similarly, the model’s
performance declines when the data diversity selection module is
excluded, as shown in Table 4. For both data selection ratios of 55
and 60, and with both the Qwen1.5-7B and LLaMA-8B-Instruct mod-
els, this exclusion results in decreased performance, demonstrating
the necessity of the diversity selection module.
Overall, the ablation study highlights the critical role of data
generation and data selection modules in SynthVLM. These ex-
periments provide valuable insights into the contributions of each
module, guiding future improvements and optimizations of the
SynthVLM model.
Table 3: Ablation study on quality selection. Excluding the
data quality selection module results in a performance drop.
Threshold
Model
Quality
B-1
B-2
B-3
B-4
R-2
CIDEr
60
Qwen1.5-7B
✓
22.48
10.47
5.76
3.54
5.21
25.07
✗
22.00↓
10.31↓
5.70↓
3.53↓
4.87↓
22.04↓
60
LLaMA3-8B-Instruct
✓
21.35
9.87
5.42
3.33
4.84
24.34
✗
21.28↓
9.69↓
5.18↓
3.11↓
4.76↓
24.02↓
Table 4: Ablation study on diversity selection. Excluding data
diversity selection module results in a performance drop.
Threshold
Model
Diversity
B-1
B-2
B-3
B-4
R-2
CIDEr
55
Qwen1.5-7B
✓
21.01
9.55
5.26
3.24
4.65
22.60
✗
20.97↓
9.39↓
5.20↓
3.21↓
4.59↓
21.24↓
60
Qwen1.5-7B
✓
22.23
10.66
6.02
3.77
5.30
26.52
✗
22.48
10.47↓
5.76↓
3.54↓
5.21↓
25.07↓
55
LLaMA3-8B-Instruct
✓
21.83
9.92
5.41
3.30
4.78
24.34
✗
20.47↓
9.35↓
5.08↓
3.07↓
4.60↓
24.23↓
60
LLaMA3-8B-Instruct
✓
21.94
10.08
5.47
3.34
4.91
25.22
✗
21.35↓
9.87↓
5.42↓
3.33↓
4.84↓
24.34↓
5
CONCLUSION
Empathy is a critical component of human social interaction and
communication. However, high-quality empathetic data remains
scarce, necessitating efficient and effective data generation algo-
rithms. This paper presents Synth-Empathy, a new paradigm for
generating high-quality empathetic data, pioneering a method to
obtain empathetic responses without human labor. By leveraging
quality and diversity selection, we achieved high-quality synthetic
empathetic data. Remarkably, utilizing the curated empathetic data,
our model outperforms all previous models. Additionally, our model
achieved SoTA performance in human evaluation, demonstrating
its contextual appropriateness and user-friendliness.

--- Page 9 ---

Synth-Empathy: Towards High-Quality Synthetic Empathy Data
REFERENCES
[1] Tianyi Bai, Hao Liang, Binwang Wan, Ling Yang, Bozhou Li, Yifan Wang, Bin
Cui, Conghui He, Binhang Yuan, and Wentao Zhang. 2024. A Survey of Multi-
modal Large Language Model from A Data-centric Perspective. arXiv preprint
arXiv:2405.16640 (2024).
[2] Antoine Bosselut, Hannah Rashkin, Maarten Sap, Chaitanya Malaviya, Asli
Celikyilmaz, and Yejin Choi. 2019. COMET: Commonsense Transformers for
Automatic Knowledge Graph Construction. In Proceedings of the 57th Annual
Meeting of the Association for Computational Linguistics. 4762–4779.
https:
//aclanthology.org/P19-1470
[3] Lichang Chen, Shiyang Li, Jun Yan, Hai Wang, Kalpa Gunaratna, Vikas Yadav,
Zheng Tang, Vijay Srinivasan, Tianyi Zhou, Heng Huang, et al. 2023. Alpagasus:
Training a better alpaca with fewer data. arXiv preprint arXiv:2307.08701 (2023).
[4] Yangbin Chen and Chunfeng Liang. 2022. Wish I Can Feel What You Feel: A
Neural Approach for Empathetic Response Generation. In Findings of the Associ-
ation for Computational Linguistics: EMNLP 2022. 922–933. https://aclanthology.
org/2022.findings-emnlp.65
[5] Zui Chen, Lei Cao, and Sam Madden. 2023. Lingua manga: A generic large
language model centric system for data curation. arXiv preprint arXiv:2306.11702
(2023).
[6] Mark H Davis. 1983. Measuring individual differences in empathy: Evidence for
a multidimensional approach. Journal of personality and social psychology 44, 1
(1983), 113.
[7] Qianlong Du, Chengqing Zong, and Jiajun Zhang. 2023. Mods: Model-oriented
data selection for instruction tuning. arXiv preprint arXiv:2311.15653 (2023).
[8] Run-Ze Fan, Xuefeng Li, Haoyang Zou, Junlong Li, Shwai He, Ethan Chern,
Jiewen Hu, and Pengfei Liu. 2024. Reformatted Alignment. CoRR abs/2402.12219
(2024).
[9] Raul Castro Fernandez, Aaron J Elmore, Michael J Franklin, Sanjay Krishnan, and
Chenhao Tan. 2023. How large language models will disrupt data management.
Proceedings of the VLDB Endowment 16, 11 (2023), 3302–3309.
[10] Fengyi Fu, Lei Zhang, Quan Wang, and Zhendong Mao. 2023. E-CORE: Emotion
Correlation Enhanced Empathetic Dialogue Generation. In Proceedings of the 2023
Conference on Empirical Methods in Natural Language Processing. 10568–10586.
[11] Deepanway Ghosal, Navonil Majumder, Alexander Gelbukh, Rada Mihalcea,
and Soujanya Poria. 2020. COSMIC: COmmonSense knowledge for eMotion
Identification in Conversations. In Findings of the Association for Computational
Linguistics: EMNLP 2020. 2470–2481.
https://aclanthology.org/2020.findings-
emnlp.224
[12] Pengcheng He, Xiaodong Liu, Jianfeng Gao, and Weizhu Chen. 2020. DEBERTA:
DECODING-ENHANCED BERT WITH DISENTANGLED ATTENTION. In In-
ternational Conference on Learning Representations.
[13] Xijie Huang, Xinyuan Wang, Hantao Zhang, Jiawen Xi, Jingkun An, Hao Wang,
and Chengwei Pan. 2024. Cross-Modality Jailbreak and Mismatched Attacks on
Medical Multimodal Large Language Models. arXiv preprint arXiv:2405.20775
(2024).
[14] Wongyu Kim, Youbin Ahn, Donghyun Kim, and Kyong-Ho Lee. 2022. Emp-RFT:
Empathetic Response Generation via Recognizing Feature Transitions between
Utterances. In Proceedings of the 2022 Conference of the North American Chapter
of the Association for Computational Linguistics: Human Language Technologies.
4118–4128. https://aclanthology.org/2022.naacl-main.303
[15] Qintong Li, Hongshen Chen, Zhaochun Ren, Pengjie Ren, Zhaopeng Tu, and
Zhumin Chen. 2020. EmpDG: Multi-resolution Interactive Empathetic Dialogue
Generation. In Proceedings of the 28th International Conference on Computational
Linguistics. 4454–4466. https://aclanthology.org/2020.coling-main.394
[16] Qintong Li, Piji Li, Zhaochun Ren, Pengjie Ren, and Zhumin Chen. 2022. Knowl-
edge bridging for empathetic dialogue generation. In Proceedings of the AAAI
Conference on Artificial Intelligence, Vol. 36. 10993–11001.
[17] Xian Li, Ping Yu, Chunting Zhou, Timo Schick, Luke Zettlemoyer, Omer Levy,
Jason Weston, and Mike Lewis. 2023. Self-Alignment with Instruction Backtrans-
lation. CoRR abs/2308.06259 (2023).
[18] Zinan Lin, Sivakanth Gopi, Janardhan Kulkarni, Harsha Nori, and Sergey
Yekhanin. 2023. Differentially Private Synthetic Data via Foundation Model
APIs 1: Images. CoRR abs/2305.15560 (2023).
[19] Zhaojiang Lin, Andrea Madotto, Jamin Shin, Peng Xu, and Pascale Fung. 2019.
MoEL: Mixture of Empathetic Listeners. In Proceedings of the 2019 Conference
on Empirical Methods in Natural Language Processing and the 9th International
Joint Conference on Natural Language Processing (EMNLP-IJCNLP). 121–132.
https://aclanthology.org/D19-1012
[20] Wei Liu, Weihao Zeng, Keqing He, Yong Jiang, and Junxian He. 2023. What
Makes Good Data for Alignment? A Comprehensive Study of Automatic Data Se-
lection in Instruction Tuning. In The Twelfth International Conference on Learning
Representations.
[21] Renze Lou, Kai Zhang, Jian Xie, Yuxuan Sun, Janice Ahn, Hanzi Xu, Yu Su, and
Wenpeng Yin. 2023. MUFFIN: Curating Multi-Faceted Instructions for Improving
Instruction-Following. CoRR abs/2312.02436 (2023).
[22] Keming Lu, Hongyi Yuan, Zheng Yuan, Runji Lin, Junyang Lin, Chuanqi Tan,
Chang Zhou, and Jingren Zhou. 2023. # InsTag: Instruction Tagging for Analyzing
Supervised Fine-tuning of Large Language Models. In The Twelfth International
Conference on Learning Representations.
[23] meta llama. 2024. Introducing Meta Llama 3: The most capable openly available
LLM to date. https://ai.meta.com/blog/meta-llama-3/ Accessed: 2024-05-02.
[24] Xupeng Miao, Zhihao Jia, and Bin Cui. 2024. Demystifying Data Management
for Large Language Models. In Companion of the 2024 International Conference
on Management of Data. 547–555.
[25] Xiaonan Nie, Xupeng Miao, Zilong Wang, Zichao Yang, Jilong Xue, Lingxiao
Ma, Gang Cao, and Bin Cui. 2023. Flexmoe: Scaling large-scale sparse pre-
trained model training via dynamic device placement. Proceedings of the ACM
on Management of Data 1, 1 (2023), 1–19.
[26] OpenAI. 2023. ChatGPT. https://openai.com/blog/chatgpt
[27] R OpenAI. 2023. GPT-4 technical report. arXiv (2023), 2303–08774.
[28] Ritik Sachin Parkar, Jaehyung Kim, Jong Inn Park, and Dongyeop Kang. 2024.
SelectLLM: Can LLMs Select Important Instructions to Annotate? arXiv preprint
arXiv:2401.16553 (2024).
[29] Yushan Qian, Bo Wang, Shangzhao Ma, Wu Bin, Shuo Zhang, Dongming Zhao,
Kun Huang, and Yuexian Hou. 2023. Think Twice: A Human-like Two-Stage
Conversational Agent for Emotional Response Generation. In Proceedings of the
2023 International Conference on Autonomous Agents and Multiagent Systems.
727–736.
[30] Yushan Qian, Weinan Zhang, and Ting Liu. 2023. Harnessing the Power of Large
Language Models for Empathetic Response Generation: Empirical Investigations
and Improvements. In Findings of the Association for Computational Linguistics:
EMNLP 2023. 6516–6528.
[31] Hannah Rashkin, Eric Michael Smith, Margaret Li, and Y-Lan Boureau. 2019.
Towards Empathetic Open-domain Conversation Models: A New Benchmark
and Dataset. In Proceedings of the 57th Annual Meeting of the Association for
Computational Linguistics. 5370–5381. https://aclanthology.org/P19-1534
[32] Sahand Sabour, Chujie Zheng, and Minlie Huang. 2022. Cem: Commonsense-
aware empathetic response generation. In Proceedings of the AAAI Conference on
Artificial Intelligence, Vol. 36. 11229–11237.
[33] Ozan Sener and Silvio Savarese. 2017. Active learning for convolutional neural
networks: A core-set approach. arXiv preprint arXiv:1708.00489 (2017).
[34] Linzhuang Sun, Hao Liang, Jingxuan Wei, Linkun Sun, Bihui Yu, Bin Cui, and
Wentao Zhang. 2024. Efficient-Empathy: Towards Efficient and Effective Selection
of Empathy Data. arXiv preprint arXiv:2407.01937 (2024).
[35] Linzhuang Sun, Nan Xu, Jingxuan Wei, Bihui Yu, Liping Bu, and Yin Luo. 2023.
Rational Sensibility: LLM Enhanced Empathetic Response Generation Guided by
Self-presentation Theory. arXiv preprint arXiv:2312.08702 (2023).
[36] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, et al. 2023. Llama: Open and efficient foundation language models. arXiv
preprint arXiv:2302.13971 (2023).
[37] Immanuel Trummer. 2023. From BERT to GPT-3 codex: harnessing the po-
tential of very large language models for data management. arXiv preprint
arXiv:2306.09339 (2023).
[38] Lanrui Wang, Jiangnan Li, Zheng Lin, Fandong Meng, Chenxu Yang, Weiping
Wang, and Jie Zhou. 2022. Empathetic Dialogue Generation via Sensitive Emotion
Recognition and Sensible Knowledge Selection. In Findings of the Association for
Computational Linguistics: EMNLP 2022. 4634–4645. https://aclanthology.org/
2022.findings-emnlp.340
[39] Lanrui Wang, Jiangnan Li, Chenxu Yang, Zheng Lin, and Weiping Wang. 2023.
Enhancing Empathetic and Emotion Support Dialogue Generation with Prophetic
Commonsense Inference. arXiv preprint arXiv:2311.15316 (2023).
[40] Yifei Wang, Jizhe Zhang, and Yisen Wang. 2024. Do Generated Data Always
Help Contrastive Learning? CoRR abs/2403.12448 (2024).
[41] Yuxiang Wei, Zhe Wang, Jiawei Liu, Yifeng Ding, and Lingming Zhang. 2023.
Magicoder: Source Code Is All You Need. CoRR abs/2312.02120 (2023).
[42] Chulin Xie, Zinan Lin, Arturs Backurs, Sivakanth Gopi, Da Yu, Huseyin A. Inan,
Harsha Nori, Haotian Jiang, Huishuai Zhang, Yin Tat Lee, Bo Li, and Sergey
Yekhanin. 2024. Differentially Private Synthetic Data via Foundation Model APIs
2: Text. CoRR abs/2403.01749 (2024).
[43] Canwen Xu, Daya Guo, Nan Duan, and Julian J. McAuley. 2023. Baize: An
Open-Source Chat Model with Parameter-Efficient Tuning on Self-Chat Data.
In Proceedings of the 2023 Conference on Empirical Methods in Natural Language
Processing, EMNLP 2023, Singapore, December 6-10, 2023. 6268–6278.
[44] Yang Xu, Yongqiang Yao, Yufan Huang, Mengnan Qi, Maoquan Wang, Bin Gu,
and Neel Sundaresan. 2023. Rethinking the Instruction Quality: LIFT is What
You Need. arXiv:2312.11508 [cs.CL]
[45] Dongjie Yang, Ruifeng Yuan, Yuantao Fan, Yifei Yang, Zili Wang, Shusen Wang,
and Hai Zhao. 2023. RefGPT: Dialogue Generation of GPT, by GPT, and for
GPT. In Findings of the Association for Computational Linguistics: EMNLP 2023,
Singapore, December 6-10, 2023. Association for Computational Linguistics, 2511–
2535.

--- Page 10 ---

Hao Liang†‡, Linzhuang Sun†♦, Jingxuan Wei♦, Xijie Huang‡, Linkun Sun♣, Bihui Yu♦, Conghui He♠, Wentao Zhang‡∗
[46] Zhou Yang, Zhaochun Ren, Yufeng Wang, Chao Chen, Haizhou Sun, Xiaofei
Zhu, and Xiangwen Liao. 2024. An Iterative Associative Memory Model for
Empathetic Response Generation. arXiv preprint arXiv:2402.17959 (2024).
[47] Zhou Yang, Zhaochun Ren, Wang Yufeng, Xiaofei Zhu, Zhihao Chen, Tiecheng
Cai, Wu Yunbing, Yisong Su, Sibo Ju, and Xiangwen Liao. 2023. Exploiting
Emotion-Semantic Correlations for Empathetic Response Generation. In Findings
of the Association for Computational Linguistics: EMNLP 2023. 4826–4837. https:
//aclanthology.org/2023.findings-emnlp.320
[48] Wang Yufeng, Chen Chao, Yang Zhou, Wang Shuhui, and Liao Xiangwen. 2024.
CTSM: Combining Trait and State Emotions for Empathetic Response Model.
arXiv preprint arXiv:2403.15516 (2024).
[49] Weixiang Zhao, Yanyan Zhao, Xin Lu, and Bing Qin. 2023. Don’t Lose Yourself!
Empathetic Response Generation via Explicit Self-Other Awareness. In Findings
of the Association for Computational Linguistics: ACL 2023. 13331–13344. https:
//aclanthology.org/2023.findings-acl.843
[50] Jinfeng Zhou, Chujie Zheng, Bo Wang, Zheng Zhang, and Minlie Huang. 2023.
CASE: Aligning Coarse-to-Fine Cognition and Affection for Empathetic Response
Generation. In Proceedings of the 61st Annual Meeting of the Association for
Computational Linguistics. 8223–8237. https://aclanthology.org/2023.acl-long.
457
[51] Pei Zhou, Pegah Jandaghi, Bill Yuchen Lin, Justin Cho, Jay Pujara, and Xiang Ren.
2021. Probing commonsense explanation in dialogue response generation. In
Findings of the Association for Computational Linguistics: EMNLP 2021. 4132–4146.

```
