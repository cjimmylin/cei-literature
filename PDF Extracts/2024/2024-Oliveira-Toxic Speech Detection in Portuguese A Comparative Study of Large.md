---
title: "2024-Oliveira-Toxic Speech Detection in Portuguese A Comparative Study of Large - PDF Extract"
source_pdf: "2024-Oliveira-Toxic Speech Detection in Portuguese A Comparative Study of Large.pdf"
pages: 9
extracted_at: "2026-02-13T22:00:45.612146"
---

# PDF Extract: 2024-Oliveira-Toxic Speech Detection in Portuguese A Comparative Study of Large

**Source PDF:** 2024-Oliveira-Toxic Speech Detection in Portuguese A Comparative Study of Large.pdf
**Total Pages:** 9

---

## Content

```
--- Page 1 ---

Toxic Speech Detection in Portuguese:
A Comparative Study of Large Language Models
Amanda S. Oliveira and João P. R. Alvarenga
Graduate Program in Computer Science
Federal University of Ouro Preto
35.400-000 – Ouro Preto – MG – Brazil
amanda.oliveira2,joao.alvarenga@aluno.ufop.edu.br
Thiago C. Cecote and Vander L. S. Freitas and Eduardo J. S. Luz
Department of Computing
Federal University of Ouro Preto
35.400-000 – Ouro Preto – MG – Brazil
thiago.cecote@aluno.ufop.edu.br
vander.freitas,eduluz@ufop.edu.br
Abstract
This research addresses the automatic detec-
tion of toxic speech in Portuguese. Utilizing
the ToLD-Br dataset, which includes 21,000 an-
notated tweets, we examine the performance of
Large Language Models (LLMs) such as Ope-
nAI’s ChatGPT and the monolingual MariTalk
from Maritaca AI. The study focuses on their
effectiveness in identifying Toxic speech, the
influence of few-shot learning, and the intrica-
cies of annotating datasets, particularly regard-
ing vulgar language (swear words). Our ex-
periments reveal that MariTalk (Sabiá) demon-
strates a nuanced understanding of colloquial
Portuguese. Meanwhile, ChatGPT, especially
when augmented with few-shot learning, shows
robustness comparable to baseline methods.
This investigation underscores the value of
both monolingual and lower-capacity models
in the nuanced field of language-specific Toxic
speech detection, offering insights into their
competitive edge against models like ChatGPT.
1
Introduction
In 2023, X (formerly Twitter) updated its documen-
tation on hateful conduct (Twitter, 2023), clearly
defining what they consider a violation of this pol-
icy. This includes explicit prohibitions against mes-
sages that promote fear and discrimination against
specific groups. Additionally, the policy considers
the repeated use of insults, degrading stereotypes,
or images that dehumanize a particular group as
violations. In light of these updated policies, de-
veloping effective automatic hate and toxic speech
detection strategies becomes increasingly crucial.
Automated toxic speech detection strategies typ-
ically involve linguistic feature analysis, lexicon-
based approaches, and supervised machine learning
algorithms trained on labeled datasets (Schmidt and
Wiegand, 2017; Vargas et al., 2022b). Advanced
techniques, including natural language processing
and deep learning methods, seek to comprehend
the semantics and context of textual content (Leite
et al., 2020; Vargas et al., 2022a). Yet, substantial
challenges persist due to the complexity of human
language, the fast evolution of toxic speech, and
the balance needed between free speech and the
fight against harmful content.
Moreover, while research has predominantly fo-
cused on English, there has been notable progress
in detecting toxic speech in Portuguese. For in-
stance, the ToLD-Br dataset (Leite et al., 2020),
containing 21,000 annotated tweets, allows for new
advancements. Despite BERT-based models reach-
ing macro-F1 scores between 70% and 80% on this
dataset, room for improvement exists.
The use of Large Language Models (LLMs)
has gained significant notoriety due to the success
of OpenAI’s ChatGPT. Today, impressive results
are being achieved using LLMs for various nat-
ural language tasks (Koco´n et al., 2023), includ-
ing for Portuguese, such as answering questions
from the Brazilian National High School Exam
(Silveira and Mauá, 2018; Nunes et al., 2023), text
reading and comprehension (FaQuAD) (Sayama
et al., 2019), and social network sentiment anal-
ysis (Brum and Nunes, 2017), prediction of de-
pressive disorder (dos Santos and Paraboni, 2023),
among others. A comprehensive study by Koco´n
et al. (2023) demonstrated how ChatGPT, via Ope-
nAI’s API, can be competitive for various NLP
tasks, including hate speech.
In Oliveira et al.

--- Page 2 ---

(2023), authors showed the efficacy of ChatGPT-
3.5 Turbo, using a zero-shot approach, for detect-
ing toxic speech in Portuguese. The same study
indicated that other supervised learning methods
struggle with test data from different distributions,
whereas ChatGPT is more resilient in this regard.
However, OpenAI’s ChatGPT is a model with a
large number of parameters and, consequently,
high computational cost. This study centers its
investigation on the analysis of toxicity and hate
speech in Portuguese texts. Thus, this work aims to
explore smaller, Portuguese-specialized language
models, such as Sabiá from Maritaca AI 1. Sabiá
is a monolingual language model trained for Por-
tuguese (Pires et al., 2023) and available via a free
API (MariTalk API) as a chatbot. Unlike Oliveira
et al. (2023), we also investigate the few-shot ap-
proach for ChatGPT 3.5 and the Maritalk here. Ad-
ditionally, we deeply analyze the ToLD-Br dataset,
considering the annotation challenges discussed in
Poletto et al. (2021), focusing on texts containing
vulgar language. In this work, we concentrate on
three research questions:
• Q1: How does the performance of a monolin-
gual Large Language Model (LLM) for Por-
tuguese (MariTalk-Sabiá) compare to a mul-
tilingual counterpart (ChatGPT) in the detec-
tion of toxic speech?
• Q2: What is the efficacy of a few-shot learn-
ing approach in enhancing the performance of
LLMs for hate/toxic speech detection?
• Q3: What are the challenges associated with
dataset annotation for toxic speech detec-
tion, and how does including vulgar and ob-
scene language (swear words) affect the per-
formance of these models?
Through four experiments, the study analyzed
models’ proficiency in processing Portuguese for
toxic text detection. MariTalk-Sabiá demonstrated
notable efficacy, especially when enhanced by the
few-shot approach, and showed a more sophisti-
cated understanding of colloquial Portuguese. Even
with lower capacity, monolingual models can be
a promising way to solve the problem addressed
here.
1API MariTalk: https://www.maritaca.ai/
2
Detection of Hate Speech and Toxicity
in Portuguese
The effective detection of hate speech and toxic-
ity in Portuguese texts presents unique challenges
due to the diverse speakers across various coun-
tries. While each region and social group exhibits
distinct cultural differences, they contribute to the
complexity of hate speech detection in Portuguese.
Comprehensive and representative datasets are es-
sential to address this challenge effectively. How-
ever, there is a relative scarcity of labeled data
in Portuguese compared to English, which signifi-
cantly impedes the development of robust detection
systems. In this context, analyzing existing datasets
becomes critical to identifying representative con-
tent that captures the multifaceted nature of hate
speech in Portuguese across diverse cultural and
regional contexts. The lack of a common taxon-
omy connecting various concepts related to toxic
or hateful speech also poses a challenge, leading
to possible biases and misclassification issues in
detection models (Poletto et al., 2021). Below, we
highlight four datasets and works of interest.
2.1
OffcomBr
The dataset proposed in de Pelle and Moreira
(2017) collects comments from a news site (G12).
A total of 1,250 comments were manually anno-
tated by three different annotators, using the Fless
Kappa measure to gauge the level of agreement
among them.
The authors provided two different sets, named
OFFCOMBR-2 and OFFCOMBR-3. The differ-
ence between them is that OFFCOMBR-2 includes
comments considered offensive by at least two an-
notators, while OFFCOMBR-3 consists of com-
ments on which all three annotators agreed. Be-
sides, the dataset was also classified among racism,
sexism, homophobia, xenophobia, religious intol-
erance, and insults. The most frequent class is
“insults”. The authors established a baseline using
n-grams and infoGain as features and used Naive
Bayes and Support Vector Machine (SVM) clas-
sifiers. The SVM-based models performed better
than others, achieving a weighted F-score in the
range of 77-82.
2.2
HLPHSD
The HLPHSD dataset, detailed in Fortuna et al.
(2019), is a corpus of 5,668 tweets from 1,156 users
2https://g1.globo.com/

--- Page 3 ---

collected between January and March 2017. An-
notation started with non-specialist volunteers who
categorized tweets as hate or non-hate, followed by
experts assigning nuanced labels to create an 81-
category hierarchical taxonomy. Cohen’s Kappa
coefficient ensured consistency among annotators.
The dataset’s inclusion of Brazilian and European
users captures the nuances of the Portuguese lan-
guage, with 31.5% of tweets classified under hate
speech.
The authors of the dataset employed pre-
trained embeddings and Long Short-Term Memory
(LSTM) networks to establish a baseline. This eval-
uation resulted in an F1-score of 78%.
2.3
Hate-Br
The Hate-Br database, introduced in Vargas et al.
(2022a), comprises 7,000 Instagram comments in
Brazilian Portuguese, annotated by three expert an-
notators. The annotation was structured in three lay-
ers: binary (offensive vs. non-offensive), level of
offensiveness (highly, moderately, and slightly of-
fensive), and specific hate speech categories (xeno-
phobia, racism, homophobia, sexism, religious in-
tolerance, partisanship, apology to the dictatorship,
anti-Semitism, and fatphobia).
For baseline establishment in Vargas et al.
(2022a), the authors utilized n-grams and bag-of-
n-grams with TFIDF preprocessing for data repre-
sentation, applying Naive Bayes, SVM, Multilayer
Perceptron, and Logistic Regression for classifica-
tion. The dataset was split into 80% for training,
10% for testing, and 10% for validation. The study
achieved an F-score of 85% in hate speech detec-
tion and 78% in offensive speech detection.
2.4
ToLD-Br
The ToLD-Br dataset, introduced in Leite et al.
(2020), serves as a specialized corpus for detecting
toxic language within Brazilian Portuguese on Twit-
ter/X. This dataset was collected over the months of
July and August 2019, employing a dual-strategy
approach to maximize the inclusion of potentially
toxic content. The first strategy targeted tweets
containing predefined terms associated with toxic-
ity, while the second strategy broadened the scope
by capturing tweets directed at influential figures,
likely to attract abusive responses. The resultant
dataset is comprehensive, encompassing 21,000
tweets that were anonymized and then rigorously
annotated by three independent volunteers to en-
sure a diverse and representative compilation of var-
ious forms of toxic language, including LGBTpho-
bia, racism, misogyny, and xenophobia. The final
corpus, with 60% of posts derived from keyword-
focused strategies and the remainder from threads
involving public figures, was partitioned with an
80% allocation for training and a stratified 20%
reserved for testing.
Research conducted in Leite et al. (2020) show-
cased the efficacy of BERT-based models on this
dataset, yielding a macro-F1 score of 76% in hate
speech detection. This underscores the significance
of expansive monolingual datasets in enhancing
computational model precision. Meanwhile, the
study in da Rocha Junqueira et al. (2023) revealed
the superiority of BERTimbau for toxic speech de-
tection within ToLD-Br, substantiating the selec-
tion of BERTimbau as the baseline model for the
present research.
Further exploration in Oliveira et al. (2023) fo-
cused on ChatGPT in zero-shot mode for detecting
toxic speech in the ToLD-Br test partition. Though
ChatGPT 3.5 Turbo did not surpass established
baseline models, it showed comparable outcomes.
The study also highlighted the significant effect
of data distribution variations in baseline methods.
While ChatGPT demonstrated resilience to these
variations, it has constraints related to high finan-
cial costs, limited accessibility, and undisclosed
details about the Reinforcement Learning from Hu-
man Feedback (RLHF) phase. This paves the way
for a shift in focus toward investigating an open
architecture model, such as the Llama-based model
tailored for Portuguese with 65 billion parameters
called Sabiá (Pires et al., 2023). Although an in-
stance of it cannot be accessed directly, it can be
accessed via a free API.
3
Experimental Methodology
This study employs the GPT 3.5 models from Ope-
nAI via a paid API3 and also utilizes the MariTalk
from Maritaca AI, accessible through a free API4.
The models evaluated include gpt-3.5-turbo-0613
and an instance of Sabiá-65B Architecture. A zero-
temperature setting is used for all language models,
meaning more deterministic inferences. As a base-
line, a BERT-based model trained for Portuguese
is used.
3https://platform.openai.com/
4https://github.com/maritaca-ai/maritalk-api

--- Page 4 ---

Figure 1: Methodological flow for evaluating LLMs APIs.
3.1
Evaluation with LLMs via APIs
In evaluating prompts with LLM chatbots using
APIs, two models, ChatGPT and MariTalk, were
assessed according to the methodology outlined in
Figure 1.
ChatGPT, a significant progression in the GPT
series based on the Transformer architecture, show-
cased notable advancements from its predecessor
models. The initial GPT version utilized the Trans-
former decoder stack with unidirectional attention,
expanding its capabilities to tasks like translation,
summarization, and question answering (Radford
et al., 2018). GPT-2 further extended these func-
tions by doubling the input context length, increas-
ing parameters, and enhancing training data vol-
ume for better task-specific learning. The subse-
quent model, GPT-3, with its 175 billion parame-
ters and training on vast textual data, excelled in
zero-shot and few-shot scenarios, demonstrating
substantial improvements (Brown et al., 2020). The
most recent innovation, InstructGPT, refined the
model to better cope with human needs, leveraging
Reinforcement Learning from Human Feedback
(RLHF) (Ouyang et al., 2022). This evolution re-
flects the ongoing commitment to align language
models, such as ChatGPT, with real user needs
(Radford et al., 2018; Ouyang et al., 2022).
In contrast, MariTalk employs the same archi-
tecture as Sabiá-65B; although trained on an undis-
closed set of data, the model capacity is known.
The instance of Sabiá-65B presented in Pires et al.
(2023), based on the Llama 65B language model,
was evaluated on several tasks from the Poeta
benchmark, including text classification, gap fill-
ing, and translation. Sabiá outperformed English-
centric and multilingual language models in many
of these tasks, setting new benchmarks for perfor-
mance in Portuguese natural language processing
tasks. Although Pires et al. (2023) provides details
about the LLM, it is still not open to the public.
Also, other processes behind the MariTalk API,
such as the use of reinforcement learning from hu-
man feedback or fine-tuning processes for instruc-
tion, remain undisclosed.
3.1.1
Prompt Design
The prompts used in this study were adapted from
the work of Oliveira et al. (2023) for comparative
purposes. In our approach, two types of prompts
were explored for few-shot and zero-shot, and a
third prompt, proposed in this work, was employed
for a zero-shot analysis. Prompts 1 and 2 were used
to assess the ability of MariTalk and ChatGPT 3.5
Turbo models to identify toxic texts. It is notewor-
thy that while ChatGPT 3.5 Turbo uses the concept
of a “system” message, in the case of MariTalk, this
message was directly incorporated into the prompt.
Prompt 3 was used exclusively with MariTalk.
The prompts, along with the dataset instances
sourced from Portuguese-speaking users, were
translated and thoughtfully adapted into English
for the manuscript readers, but the models received
input texts in Portuguese.
Prompt #1
For the zero-shot method, the prompt is struc-
tured as follows:
“You are conducting text analysis. The following
text was used in a social media context. Tell me,
with a yes or no, if you consider this text toxic:
[text].”
For the few-shot method, with n instances per
class, the dialogue is structured as follows:
User: “You are conducting text analysis. The
following text was used in a social media context.
Respond only with ’yes’ or ’no’ if the text below
contains hate speech, offense, aggression, or other
forms of toxicity: [example text].”
Assistant: “Yes, it is toxic.” (or “No, it is not
toxic.”)
The “example text” here means an input from
the training set.
Prompt #2
For the zero-shot method, the prompt is struc-
tured as follows:

--- Page 5 ---

“You are conducting text analysis. The following
text was used in a social media context. Respond
only with ’yes’ or ’no’ if the text below contains
hate speech, offense, aggression, or other forms
of toxicity: [text]”
For the few-shot method, with n instances per
class, the dialogue is structured as follows:
User: “You are conducting text analysis. The
following text was used in a social media context.
Respond only with ’yes’ or ’no’ if the text below
contains hate speech, offense, aggression, or other
forms of toxicity: [example text].”
Assistant: “Yes, it is toxic.” (or “No, it is not
toxic.”)
The “example text” here means an input from
the training set.
Prompt #3
Deriving from the prompts presented in Oliveira
et al. (2023), we introduce here a version of the
prompt with explicit commands, instructing the
model to classify it as toxic if the text already con-
tains obscene and aggressive texts. The prompt is
structured as follows:
“You are conducting text analysis. The following
text was used in a social media context. Respond
only with ’yes’ or ’no’ if the text below contains
hate speech, offense, aggression, or other forms
of toxicity. If the text includes swear words, low-
level language, or obscene words, classify it as
offensive, therefore toxic: [text].”
3.1.2
Dataset Selection and Preprocessing
In this stage, a dataset comprising a series of tweets
is chosen for evaluation (ToLD-Br). Each tweet
underwent individual processing and anonymiza-
tion; specifically, mentions of users were uniformly
replaced with “@user”. Furthermore, all embed-
ded links within these tweets were systematically
removed.
3.1.3
Constructing the Prompt and Querying
the Models
During this phase, each tweet is carefully tailored
to fit the designated prompt (specified in the [text]
field) before initiating a query to either the Mar-
iTalk or ChatGPT API. To efficiently manage po-
tential network disruptions, a strategy of retries
with exponential backoff was implemented.
3.1.4
Processing the Raw Response
Responses to each tweet were diligently recorded
and subsequently refined to align with the output
format of the baseline model for comparison. In
this process, responses explicitly stating “yes” were
converted to a numerical value of 1.0, while those
indicating “No” were translated to 0.0. It’s note-
worthy that responses from large language models
can sometimes deviate from expected patterns, as
demonstrated in the following examples:
Query: “You are conducting text analysis. The
following text was used in a social media context.
Respond only with ’yes’ or ’no’, if you consider
this text toxic: ridiculous the attitude of both,
mercy on such people”
ChatGPT answer: “No.”
Query: “You are conducting text analysis. The
following text was used in a social media context.
Respond only with ’yes’ or ’no’, if you consider
this text toxic: rt @user wrote, didn’t read, the
stick hit.”
ChatGPT answer: “Yes, it is toxic.”
Thus, regular expressions (regex) are used here
to check if a given text contains the words “yes” or
“no” as whole and independent words within the
sentences.
3.1.5
Metrics
The evaluation encompasses a range of metrics,
notably the class-specific F1-score, precision, and
recall, as well as their macro and weighted counter-
parts. The macro variant of these metrics computes
the metric separately for each class before aver-
aging them, thereby ensuring equal representation
for all classes. Conversely, the weighted variant
also calculates these metrics individually for each
class but applies a weighting in the averaging pro-
cess proportional to the class’s prevalence. These
metrics are defined as follows:
Precision =
TP
TP + FP ,
(1)
Recall =
TP
TP + FN ,
(2)
F1-score = 2 × Precision × Recall
Precision + Recall,
(3)
Macro F1-score = 1
N
N
X
i=1
F1-scorei,
(4)
Weighted F1-score =
N
X
i=1
wi × F1-scorei,
(5)
where TP, FP, and FN correspond to true positives,
false positives, and false negatives, respectively; N
is the number of classes, and wi is the proportion
of the total sample size that class i represents.

--- Page 6 ---

3.2
Baseline Methods
For the baseline model, we followed the method-
ology proposed in Leite et al. (2020) and Oliveira
et al. (2023), also employing a BERT-based model.
We used the simpletransformers library 5 with de-
fault arguments for reproducibility. The pre-trained
model was BERTimbau (Souza et al., 2020)6.
3.3
Methodology for Analysis and Verification
of Dataset Annotations
To better understand the nuances of our results, we
conducted a detailed review of the dataset annota-
tions (test set). We explored the hypothesis that the
presence of swear words might influence text clas-
sification as hate speech or toxic discourse, which
could reflect common challenges in annotation con-
sistency.
To conduct this investigation, we first compiled
a list encompassing various categories of swear
words, totaling 60 terms and expressions, includ-
ing spelling errors and internet neologisms. Sub-
sequently, we used this list to identify sentences
containing such terms in the test data, resulting in
1,010 instances in the test data. These instances
were then re-annotated by a specialist, who fol-
lowed a specific guide covering all contexts of
swear word usage in Brazilian Portuguese.
It
is worth noting that, in the Portuguese language,
words commonly considered obscene can function
as adjectives, interjections, or intensity adverbs, as
exemplified in (Original source follow in italics for
further reference):
• Fucking delicious cake. “Bolo gostoso pra caralho.”
(intensity adverb)
• Blessed be the mute, damn it! “Bendito seja o mute,
caralho!” (interjection)
• Bahia is so fucking awesome, giants. “O bahia é foda
demais pqp, gigantes.”(adjective/interjection)
To refine our understanding of the dataset’s nu-
ances, we conducted a thorough review of the an-
notations within the test set. During this process,
we identified 380 instances where the presence of
swear words, often used as interjections or inten-
sifiers, may have led to their initial categorization
as toxic content. We carefully reassessed these
instances. After a considered re-evaluation, we
updated the labels where necessary, resulting in
5https://simpletransformers.ai/
6https://huggingface.co/neuralmind/bert-large-
portuguese-cased
a revised test set that we believe reflects a more
colloquial interpretation of the language used.
4
Results and Discussion
For the experiments involving ChatGPT and Mar-
iTalk, the official APIs were utilized.
In total,
24,984 prompts were sent to the MariTalk API and
16,656 to the OpenAI API. Post-processing of each
prompt’s response was conducted following the
query, with necessary adjustments made for com-
parison against the baseline model, BERTimbau.
Regarding the baseline, the BERTimbau model
was locally trained on a machine equipped with
an NVIDIA 3090 GPU with 24GB, an Intel(R)
Core(TM) i9-10900 CPU @ 2.80GHz, and 128GB
of RAM. Four experiments were conducted to ad-
dress the three research questions posed in this
study. The source code for reproducing the ex-
periments is available at https://github.com/
ufopcsilab/ToxicSpeech-Propor2024.
4.1
EXP 1: Assessing the Impact of a
Portuguese-Specific Language Model:
MariTalk
To evaluate a monolingual model’s performance for
the task, we compared the results obtained from the
MariTalk API against the top outcomes reported
in Oliveira et al. (2023). For this purpose, both the
experiments with BERTimbau and the ChatGPT
3.5 Turbo API were re-implemented and tested un-
der the same setup. The radar chart of Figure 2
compares the performance of three models, with
axes representing precision, recall, and F1 scores
for toxic and non-toxic categories. The chart indi-
cates that the MariTalk model is particularly pre-
cise at identifying non-toxic texts, meaning it has
a lower rate of falsely labeling non-toxic texts as
toxic. However, its ability to recognize toxic texts
(recall for toxic) and its overall accuracy and bal-
ance between precision and recall (F1 scores for
both toxic and non-toxic) might not be as strong as
some of the other models represented on the chart.
4.2
EXP 2: Examining the Impact of the
Few-Shot Approach
Experiment 2 aimed to address research question
Q2, specifically investigating the impact of em-
ploying a few-shot approach on the models un-
der study. For this experiment, instances from the
training dataset were randomly selected from both
classes in a balanced manner and used to compose

--- Page 7 ---

Model
Prompt
Precision
F-score
BERTimbau
—-
0.76
0.75
ChatGPT 3.5-turbo zeroshot
prompt 2
0.74
0.74
ChatGPT 3.5-turbo + 10 fewshots
prompt 1
0.74
0.56
ChatGPT 3.5-turbo + 10 fewshots
prompt 2
0.75
0.72
Maritaca zeroshot
prompt 1
0.70
0.50
Maritaca zeroshot
prompt 2
0.73
0.69
Maritaca + 10 fewshots
prompt 2
0.73
0.73
Maritaca + 20 fewshots
prompt 2
0.74
0.72
Bertimbau#
—-
0.72
0.73
ChatGPT 3.5-turbo zeroshot#
prompt 2
0.72
0.72
Maritaca zeroshot#
prompt 1
0.70
0.55
Maritaca zeroshot#
prompt 2
0.68
0.67
Table 1: Summary of results on ToLD-Br test set. Methods marked with # were evaluated on a re-annotated ToLD-Br
test set.
Figure 2: Zero-shot experiments for Q1.
the prompts. We experimented with 10 and 20 in-
stances per class. Figure 3 displays a comparison
of the best results achieved, and Table 1 shows a
more complete panorama. It’s important to note
that BERTimbau is included for comparison pur-
poses, as it remained unchanged between tests.
Figure 3: Few-shot experiments for Q2.
In the zero-shot modeling context, we observed
that certain popular words and expressions, often
categorized as slang or vulgar language, were not
automatically classified as toxic, aggressive, or
hateful language. The following phrases, extracted
from the ToLD-Br test partition, were initially clas-
sified as non-toxic by MariTalk in zero-shot mode
but were reclassified when the few-shot approach
was employed:
• “get out of this, they’ve already done a lot but now some
super badass girls are coming and they’re playing like
hell.”
• “but in the end I understood all the shit and I got along
with the guys... I loved it, everyone was fucking awe-
some yesterday.”
• “I dreamed that I was dating?? Fuck, the guy was hot
for me.”
• “mami calling me a bitch lol lol so good.”
• “bro, I’m fucking mad at this network!!!!”
In our opinion, these phrases highlight MariTalk-
zero-shot’s ability to discern between collo-
quial language and potentially offensive language,
demonstrating an advanced understanding of the
usage of words and slang in different contexts.
With the few-shot approach, MariTalk began to
classify these instances correctly, or rather, align
them with the dataset ToLD-Br’s labels.
4.3
EXP 3: Investigating a Third Prompt:
Focus on Aggressive and Obscene Words
Two experiments were conducted to address re-
search question Q3, experiments 3 and 4. Experi-
ment 3 aimed to understand the impact of incorpo-
rating specific commands into the prompt to force
the classification of instances as toxic whenever
an aggressive or obscene word appeared. Figure 4
shows the effect of prompt 3 on MariTalk’s classi-
fication.

--- Page 8 ---

Figure 4: Few-shot experiments for Q3.
4.4
EXP 4: Analyzing Annotations from the
ToLD-Br Test Partition
To perform a comparative performance analysis be-
tween the models, taking into account the reannota-
tion of the test data according to our methodology,
we proceeded with experiments using the new test
set. The results demonstrated a small discrepancy,
as can be seen in Table 1. In this case, we are in-
terested in the response of the models without any
interference, that is, zero-shot.
MariTalk, while achieving satisfactory outcomes
in the initial experiment, experienced a notable de-
cline in F-score and precision when the reannotated
test set was applied with prompt 2. We believe that
prompt 2 instructs the model to become more sen-
sitive. ChatGPT also presents a decline in terms
of F-score and precision for prompt 2. We would
like to highlight that the MariTalk model improved
precision for the case of the first prompt.
4.5
Discussion
The four experiments conducted provided valu-
able insights into the performance and utility of
the models in processing Portuguese text. Exper-
iment 1, focusing on the monolingual MariTalk
chatbot, demonstrated its effectiveness in handling
Portuguese language tasks, as evidenced by its
comparison with top results from previous stud-
ies. The introduction of the few-shot approach in
Experiment 2 marked a significant improvement in
MariTalk’s ability to correctly classify instances,
particularly those involving colloquial and slang
expressions, highlighting the model’s improved un-
derstanding and contextual interpretation with ad-
ditional examples.
Experiments 3 and 4 further explored the sub-
tleties of language model performance. Experi-
ment 3 examined the impact of a prompt specifi-
cally designed to identify aggressive and obscene
words, showing the model’s sensitivity to prompt
design and its influence on classification accuracy.
In Experiment 4, the analysis of reannotated test
data from the ToLD-Br dataset indicated a slight
discrepancy in the performance of ChatGPT and
MariTalk. MariTalk exhibited increased precision,
supporting the hypothesis that it better understands
the nuances of colloquial Portuguese.
5
Conclusion
The experiments conducted provided insights into
the performance and adaptability of both ChatGPT
and MariTalk in processing Portuguese for toxic
text detection. Both models demonstrated com-
petitive performances, yet neither managed to out-
perform the BERTimbau model when applied to
the ToLD-Br dataset. Notably, MariTalk, being a
monolingual model with an open Llama architec-
ture, showed particular promise. The study also
revealed that employing a few-shot approach, even
with as few as ten example instances per class, sig-
nificantly influenced the results. However, it is
crucial to recognize the limitations of our study,
particularly the lack of in-depth access to the mod-
els, which might have impacted our findings. Mov-
ing forward, a valuable path for research could in-
volve direct interaction with Large Language Mod-
els (LLMs), bypassing the constraints of API-based
access.
Acknowledgments
We would like to express our sincere thanks to the
company Blip, whose generous support and invalu-
able assistance were crucial for the presence of two
authors at this event. The authors would also like
to thank the Coordenação de Aperfeiçoamento de
Pessoal de Nível Superior - Brazil (CAPES) - Fi-
nance Code 001, Fundacão de Amparo à Pesquisa
do Estado de Minas Gerais (FAPEMIG, grants
APQ-01518-21), Conselho Nacional de Desen-
volvimento Científico e Tecnológico (CNPq, grants
308400/2022-4), and Universidade Federal de Ouro
Preto (PROPPI/UFOP) for supporting the develop-
ment of this study.
References
T. Brown, B. Mann, N. Ryder, M. Subbiah, J.D. Kaplan,
P. Dhariwal, A. Neelakantan, P. Shyam, G. Sastry,

--- Page 9 ---

A. Askell, et al. 2020. Language models are few-
shot learners. In Advances in neural information
processing systems, volume 33, pages 1877–1901.
Henrico Bertini Brum and Maria das Graças Volpe
Nunes. 2017.
Building a sentiment corpus of
tweets in brazilian portuguese.
arXiv preprint
arXiv:1712.08917.
Júlia da Rocha Junqueira, Claudio Luis Junior, Félix
Leonel V Silva, Ulisses Brisolara Côrrea, and
Larissa A de Freitas. 2023.
Albertina in action:
An investigation of its abilities in aspect extraction,
hate speech detection, irony detection, and question-
answering. In Anais do XIV Simpósio Brasileiro de
Tecnologia da Informação e da Linguagem Humana,
pages 146–155. SBC.
Rafael P de Pelle and Viviane P Moreira. 2017. Offen-
sive comments in the brazilian web: a dataset and
baseline results. In Anais do VI Brazilian Workshop
on Social Network Analysis and Mining. SBC.
Wesley Ramos dos Santos and Ivandré Paraboni. 2023.
Predição de transtorno depressivo em redes sociais:
Bert supervisionado ou chatgpt zero-shot? In Anais
do XIV Simpósio Brasileiro de Tecnologia da Infor-
mação e da Linguagem Humana, pages 11–21. SBC.
Paula Fortuna, João Ricardo da Silva, Leo Wanner, and
Samuel Nunes. 2019. A hierarchically-labeled por-
tuguese hate speech dataset. In Proceedings of the
third workshop on abusive language online, pages
94–104.
Jan Koco´n, Igor Cichecki, Oliwier Kaszyca, Mateusz
Kochanek, Dominika Szydło, Joanna Baran, Julita
Bielaniewicz, Marcin Gruza, Arkadiusz Janz, Kamil
Kanclerz, et al. 2023. Chatgpt: Jack of all trades,
master of none. Information Fusion, page 101861.
João Antônio Leite, Diego Silva, Kalina Bontcheva, and
Carolina Scarton. 2020. Toxic language detection in
social media for brazilian portuguese: New dataset
and multilingual analysis. In Proceedings of the 1st
Conference of the Asia-Pacific Chapter of the Asso-
ciation for Computational Linguistics and the 10th
International Joint Conference on Natural Language
Processing, pages 914–924.
Desnes Nunes, Ricardo Primi, Ramon Pires, Roberto
Lotufo, and Rodrigo Nogueira. 2023. Evaluating
gpt-3.5 and gpt-4 models on brazilian university ad-
mission exams. arXiv preprint arXiv:2303.17003.
Amanda S Oliveira, Thiago C Cecote, Pedro HL Silva,
Jadson C Gertrudes, Vander LS Freitas, and Ed-
uardo JS Luz. 2023. How good is chatgpt for de-
tecting hate speech in portuguese? In Anais do XIV
Simpósio Brasileiro de Tecnologia da Informação e
da Linguagem Humana, pages 94–103. SBC.
Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida,
Carroll Wainwright, Pamela Mishkin, Chong Zhang,
Sandhini Agarwal, Katarina Slama, Alex Ray, et al.
2022. Training language models to follow instruc-
tions with human feedback.
Advances in Neural
Information Processing Systems, 35:27730–27744.
Ramon Pires, Hugo Abonizio, Thales Sales Almeida,
and Rodrigo Nogueira. 2023.
Sabiá: Portuguese
large language models. In Intelligent Systems, pages
226–240, Cham. Springer Nature Switzerland.
Fabrício Poletto, Valerio Basile, and Manuela San-
guinetti. 2021. Resources and benchmark corpora
for hate speech detection: a systematic review. Lan-
guage Resources & Evaluation, 55(2):477–523.
Alec Radford, Karthik Narasimhan, Tim Salimans, Ilya
Sutskever, et al. 2018. Improving language under-
standing by generative pre-training.
Hélio Fonseca Sayama, Anderson Viçoso Araujo, and
Eraldo Rezende Fernandes. 2019. Faquad: Reading
comprehension dataset in the domain of brazilian
higher education. In 2019 8th Brazilian Conference
on Intelligent Systems (BRACIS), pages 443–448.
IEEE.
Anna Schmidt and Michael Wiegand. 2017.
A sur-
vey on hate speech detection using natural language
processing. In Proceedings of the Fifth International
Workshop on Natural Language Processing for Social
Media, pages 1–10. Association for Computational
Linguistics.
Igor Cataneo Silveira and Denis Deratani Mauá. 2018.
Advances in automatically solving the enem.
In
2018 7th Brazilian Conference on Intelligent Systems
(BRACIS), pages 43–48. IEEE.
Fabricio Souza, Rodrigo Nogueira, and Roberto Lotufo.
2020. Bertimbau: pretrained bert models for brazil-
ian portuguese. In Intelligent Systems: 9th Brazilian
Conference, BRACIS 2020, Rio Grande, Brazil, Octo-
ber 20–23, 2020, Proceedings, Part I, pages 403–417.
Springer.
Twitter. 2023.
Hateful conduct policy.
https:
//help.twitter.com/en/rules-and-policies/
hateful-conduct-policy.
Felipe Vargas, Isabela Carvalho, Felipe R de Góes, Thi-
ago Pardo, and Fabrício Benevenuto. 2022a. Hatebr:
A large expert annotated corpus of brazilian insta-
gram comments for offensive language and hate
speech detection. In Proceedings of the Thirteenth
Language Resources and Evaluation Conference,
pages 7174–7183.
Francielle Vargas, Fabiana Rodrigues de Góes, Isabelle
Carvalho, Fabrício Benevenuto, and Thiago Alexan-
dre Salgueiro Pardo. 2022b. Contextual-lexicon ap-
proach for abusive language detection.

```
