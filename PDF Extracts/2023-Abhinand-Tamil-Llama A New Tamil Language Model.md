---
title: "2023-Abhinand-Tamil-Llama A New Tamil Language Model - PDF Extract"
source_pdf: "2023-Abhinand-Tamil-Llama A New Tamil Language Model.pdf"
pages: 19
extracted_at: "2026-02-13T09:15:43.314367"
---

# PDF Extract: 2023-Abhinand-Tamil-Llama A New Tamil Language Model

**Source PDF:** 2023-Abhinand-Tamil-Llama A New Tamil Language Model.pdf
**Total Pages:** 19

---

## Content

```
--- Page 1 ---

TAMIL-LLAMA: A NEW TAMIL LANGUAGE MODEL BASED ON
LLAMA 2
Abhinand Balachandran
abhinandb.ml@gmail.com
ABSTRACT
Language modeling has witnessed remarkable advancements in recent years, with Large Language
Models (LLMs) like ChatGPT setting unparalleled benchmarks in human-like text generation. How-
ever, a prevailing limitation is the underrepresentation of languages like Tamil in these cutting-edge
models, leading to suboptimal performance in diverse linguistic contexts. This paper addresses this
lacuna, enhancing the open-source LLaMA model with an addition of 16,000 Tamil tokens, aiming to
achieve superior text generation and comprehension in the Tamil language. We strategically employ
the LoRA methodology for efficient model training on a comprehensive Tamil corpus, ensuring com-
putational feasibility and model robustness. Moreover, we introduce a Tamil-translated version of the
Alpaca dataset and a subset of the OpenOrca dataset tailored for instruction fine-tuning. Our results
showcase significant performance improvements in Tamil text generation, with potential implications
for the broader landscape of LLMs in Indian languages. We further underscore our commitment
to open research by making our models, datasets, and code1 publicly accessible, fostering further
innovations in language modeling.
1
Introduction
The past few years have been transformative for language modeling, with groundbreaking advances and monumental
achievements. At the forefront of this revolution was OpenAI’s ChatGPT (OpenAI, 2022), which not only raised the
bar in language modeling performance but also underscored the immense societal implications of such technologies.
Alongside ChatGPT, various Large Language Models (LLMs) have consistently demonstrated exceptional prowess in
natural language understanding and generation, heralding a new era in computational linguistics.
Central to the functionality of these modern LLMs is the Transformer architecture, a cornerstone concept brought to
the limelight by "Attention is All You Need" (Vaswani et al., 2017). This innovation transformed our approach to
sequence-based tasks, catalyzing pivotal models like BERT (Devlin et al., 2019) and redefining best practices in Natural
Language Processing (NLP).
Subsequent developments, particularly the Generative Pre-trained Transformer (GPT) (Radford et al., 2018), showcased
the profound potential of unsupervised pre-training on vast datasets. Models like GPT-3 and its successor, GPT-4
(OpenAI, 2023), have redefined benchmarks and fueled a renaissance in natural language understanding and generation.
Beyond their technical prowess, they have prompted a renewed vigor in exploring the limits of Artificial General
Intelligence (AGI). These advancements, paired with exemplary performance in numerous applications, have galvanized
the NLP community, sparking widespread application and research from sentiment analysis to machine translation.
However, progress is not without its pitfalls. The elite LLMs, despite their remarkable capabilities, grapple with
challenges—primarily, their proprietary nature, which constricts open research. Furthermore, an English-centric
bias and the enormous computational requirements for training such behemoths further accentuate the call for more
accessible and diverse solutions.
In response, the open-source community has championed the creation of models like LLaMA (Touvron et al., 2023a)
and Mistral (Jiang et al., 2023). Such models, despite their compact nature, challenge the hegemony of giants like
ChatGPT in select benchmarks, heralding a promising direction for future research.
1GitHub Repository: https://github.com/abhinand5/tamil-llama
arXiv:2311.05845v1  [cs.CL]  10 Nov 2023

--- Page 2 ---

However, as robust as these models, like LLaMA and Mistral, might be, their proficiency in generating coherent text in
Tamil and several other Indian languages remains noticeably deficient. A fundamental limitation lies in their minimal
vocabulary of Tamil characters, which is essential for effective text encoding and generation. This paper aims to bridge
this gap by augmenting the existing LLaMA models’ vocabulary with an additional 16,000 Tamil tokens, markedly
enhancing their capability in processing and producing Tamil content. This method draws inspiration from a parallel
endeavor in the Chinese adaptation of LLaMA, as documented in Cui et al. (2023). To ensure efficient pre-training
and fine-tuning while maintaining computational feasibility, we leverage the LoRA (Hu et al., 2021) methodology. We
aspire that this initiative catalyzes further research endeavors, refining LLaMA and other open-source models tailored
for Indian languages. A succinct overview of the principal contributions of this paper is as follows:
• We bolster the LLaMA model’s encoding and decoding proficiencies for Tamil by incorporating an additional
16,000 Tamil tokens, thereby expanding its vocabulary.
• Through the LoRA methodology, the augmented model undergoes training on an extensive Tamil corpus,
resulting in a marked enhancement of its text generation capabilities relative to its predecessor models.
• We present a Tamil-translated version of the original Alpaca dataset (Taori et al., 2023), paired with a subset of
the OpenOrca (Lian et al., 2023) dataset, both curated for instruction fine-tuning in Tamil.
• Our newly trained instruction and chat models, built upon the Alpaca and OpenOrca datasets, demonstrate
notable advancements in performance for the Tamil language compared to other open-source language models.
• To stimulate continuous innovation and broader adaptability, we grant public access to the models, datasets,
and associated code, inviting further exploration and encouraging the refinement of LLaMA models for diverse
languages.
2
Related Work
Within the broad field of Natural Language Processing (NLP), the advent of Large Language Models (LLMs) marks a
transformative moment. These models have heralded new capabilities in understanding, generating, and processing
various human languages, underpinning innovations from automated content creation to nuanced sentiment analysis.
While their proficiency in mainstream languages like English is widely recognized and leveraged, a disparity exists in
their performance and availability for numerous non-European languages.
Tamil, a language with ancient roots and spoken by a substantial global population, epitomizes this disparity. Despite
its linguistic depth and cultural significance, dedicated pre-trained LLMs for Tamil are conspicuously underrepresented.
Most current offerings are generic, multipurpose LLMs, which do not cater specifically to the unique attributes of the
Tamil language.
A survey of the existing literature reveals that many attempts to cater to the Tamil language through LLMs rely heavily
on multilingual models. Works such as Scao et al. (2022), Shliazhko et al. (2022), and Lin et al. (2022) have all ventured
into this domain. However, it is crucial to note that, except "GPT-2 Tamil" by Mahendiran (2021), all these models
are not exclusive to Tamil. While they can process Tamil to a certain extent, their capabilities are inherently limited.
This limitation arises because the training data for these models often comprise a low fraction of Tamil content relative
to other languages. Consequently, the nuances and intricacies specific to Tamil are often lost, leading to suboptimal
performance.
The effort by Mahendiran (2021) represents a notable deviation from this trend. Here, the GPT-2 base model, equipped
with 117 million parameters as outlined in Radford et al. (2019), was fine-tuned with a focus on Tamil, using both the
Oscar dataset (Caswell et al., 2020) and The IndicNLP (Kunchukuttan, 2020) dataset. This approach signifies a targeted
attempt to adapt LLM capabilities for the Tamil language specifically.
However, the broader landscape of Tamil-specific LLM research remains relatively uncharted. This context underscores
the motivation for our present research. We endeavor to delve deeper into this space, addressing existing shortcomings
and advancing the capabilities of LLMs tailored for Tamil.
3
Tamil LLaMA
3.1
Datasets Used
The development of Tamil-LLaMA involved using several different datasets, each chosen for specific parts of the
training and fine-tuning process. This approach was vital to ensure the model’s effectiveness across various tasks.
2

--- Page 3 ---

3.1.1
Datasets used for Pre-Training
For the initial pre-training phase of LLaMA 2 (Touvron et al., 2023a), we mainly used the CulturaX dataset (Nguyen
et al., 2023). This dataset is a combination of many popular datasets, including the Oscar dataset (Caswell et al., 2020).
Out of the 4.72 million documents in CulturaX, we selected 600k documents (12 GB) for training. This choice was
made to manage training costs while aiming for high performance. Our approach was successful, as the model showed
strong results in text completion tasks even with this smaller dataset.
3.1.2
Datasets used for Instruction Tuning
The "Instruction Tuning" phase was a pivotal stage in refining LLaMA’s proficiency in precisely adhering to textual
instructions. For this enhancement, we incorporated a translated version of the Stanford Alpaca dataset (Taori et al.,
2023), comprising 52,000 instructions. Concurrently, we integrated a specialized no-code section from the OpenOrca
dataset (Lian et al., 2023), which consists of around 93,000 instructions. The deliberate focus on no-code instructions
was to streamline the training process, eliminating the intricacies presented by coding instructions during translation.
To ensure translation uniformity and accuracy across the datasets, the Google Translation API service was our tool of
choice. We meticulously translated the entirety of the Alpaca dataset while also applying a similar methodology to the
OpenOrca subset.
We believe that leveraging diverse datasets has bolstered LLaMA’s enhanced capability to discern and generate
contextually pertinent responses across a spectrum of prompts.
3.2
Background on the LLaMA Models
Introduced by Touvron et al. (2023a), LLaMA has emerged as an essential milestone in the world of open-source
large language models (LLMs), with the renowned Transformer architecture (Vaswani et al., 2017) as its foundation.
While it draws inspiration from models like GPT for its basic structure—comprising an embedding layer and multiple
transformer blocks—LLaMA has its unique features. LLaMA has brought forward several innovative techniques such
as pre-normalization (Zhang and Sennrich, 2019), SwiGLU activation (Shazeer, 2020), and rotary embeddings (Su
et al., 2022). Offered in sizes ranging from 7B (7 Billion) to 65B (65 Billion) parameters, LLaMA has been trained
on a rich mixture of content sources, including web pages, books, and academic papers. Its strong performance on
benchmarks, especially given its relatively compact size compared to other models, has made it a noteworthy contender
in the LLM landscape, drawing considerable attention in the AI research community.
Building upon its predecessor’s foundation, LLaMA 2 (Touvron et al., 2023b) introduces monumental enhancements to
the LLaMA lineage. With a dataset expanded by 40% relative to LLaMA 1, the models under LLaMA 2 exhibit an
enriched comprehension of diverse content, leading to improved text generation. An extended context length of 4,096
tokens empowers LLaMA 2 to process and understand more extensive textual segments, significantly benefiting tasks
such as translation and intricate question answering. Another pivotal innovation in LLaMA 2 is adopting the grouped-
query attention mechanism (Ainslie et al., 2023), facilitating faster inference despite its expanded size compared to
LLaMA 1.
In the course of our research, we made a conscious choice to employ LLaMA 2 as our primary language model. Several
factors influenced this decision. Firstly, LLaMA 2 is a recent addition to the lineage of Large Language Models, which
implies that it benefits from the latest advancements in model training and architectural innovations. This recent launch
incorporates the most up-to-date techniques and methodologies. Secondly, compared with its predecessor, LLaMA
1, the enhancements in LLaMA 2 are undeniably compelling. These improvements are not just incremental; they
represent substantial strides in areas such as data exposure, context length, and attention mechanisms. The evolution
from LLaMA 1 to LLaMA 2 is emblematic of the rapid advancements in the field, and by leveraging the latter, we
aimed to ensure our research was grounded in the most cutting-edge tools available.
3.3
Expansion of Tamil Vocabulary
LLaMA 2, as outlined in the seminal work of Touvron et al. (2023b), is backed by an expansive pre-training corpus of 2
Trillion tokens. A detailed linguistic analysis of this vast corpus reveals a striking imbalance in language representation.
An overwhelming 89.7% of the tokens are sourced from English, with other European languages collectively contributing
to nearly 10% of the dataset. In stark contrast, diverse languages such as Tamil and Hindi represent a meager presence,
with their combined token count along with other under-represented languages accounting for less than 0.21%.
This skewed distribution raises concerns about the genuine multilingual and cross-lingual capabilities of LLaMA 2.
While it is evident that the model is proficient in several European languages, its ability to comprehend and generate
3

--- Page 4 ---

content in languages like Tamil needs to be improved substantially. Our preliminary experiments further underscored
this limitation. When presented with tasks in Tamil, LLaMA 2 exhibited a remarkable lack of coherence in its responses.
In fact, its performance was notably inferior to smaller models, underscoring a noticeable shortcoming in LLaMA 2’s
coverage of worldwide languages. There is a clear need for the open-source community to focus on languages like
Tamil, spoken by millions globally across multiple countries.
To bolster the text generation and understanding abilities of LLaMA 2 in Tamil, we advocate extending its pre-training
phase with an expansive Tamil corpus, as recommended by Cui et al. (2023). However, this alone is not sufficient. A
limitation arises from LLaMA’s existing vocabulary, which has a tiny number of Tamil characters. Although LLaMA
can bypass this by encoding unknown tokens, this process considerably lengthens the sequences, leading to substantial
delays during encoding and decoding. Typically, a single Tamil character is translated into 3-4 byte tokens. Moreover,
these byte tokens are not uniquely purposed for Tamil characters but represent UTF-8 tokens from various languages.
This dual role complicates the task for transformer encoders and byte-tokens to understand and capture the nuanced
semantics of Tamil characters proficiently.
To overcome these problems and to enhance the text generation capabilities in Tamil, we propose the incorporation of
an additional 16,000 Tamil tokens to the pre-existing vocabulary of the LLAMA 2 model. This methodology echoes the
strategies employed in developing Chinese LLaMA (Cui et al., 2023). The subsequent steps explain the process of
vocabulary extension:
1. Employ SentencePiece (Kudo and Richardson, 2018) to train a Tamil Tokenizer on an extensive corpus
of contemporary Tamil text, capturing the essence of modern linguistic nuances necessary for coherent
communication.
2. Integrate the original tokenizer of the LLaMA 2 model with the vocabulary derived from the newly trained
SentencePiece tokenizer. This amalgamation culminates in an augmented tokenizer encompassing an additional
16,000 Tamil tokens, leading to an aggregated vocabulary size of 48,000 (32,000 original + 16,000 new).
3. Drawing parallels from Cui et al. (2023), the LLaMA model is then tailored to accommodate the Tamil LLaMA
tokenizer. This modification necessitates resizing the word embeddings and the language model head from
a matrix shape V × H to V’ × H. Herein, V represents the original vocabulary size of 32,000, whereas V’
signifies the extended size of 48,000. Importantly, this adjustment ensures the preservation of the embeddings
associated with the original vocabulary by appending the new rows to the concluding segments of the initial
embedding matrices.
In Figure 1, we can see that the Tamil LLaMA tokenizer needs only 20% to 25% of the tokens that the original LLaMA
model uses to encode Tamil text. This makes the Tamil LLaMA much more efficient. With this crucial update, the
model can handle over three times more information and works three times faster. In conclusion, our modifications to
LLaMA 2 significantly bolster its capabilities in understanding and generating Tamil content. By adding 16,000 Tamil
tokens, we ensure a more efficient and nuanced representation. The new Tamil LLaMA tokenizer drastically reduces
the required tokens, making encoding more efficient.
Figure 1: Tokenizer comparisons between original LLaMA and Tamil LLaMA.
4

--- Page 5 ---

3.4
Pre-Training Phase
In order to harness the full potential of the expanded vocabulary of Tamil LLaMA, a robust pre-training phase is
implemented using a comprehensive Tamil text corpus. The datasets utilized during this training phase are detailed in
3.1.1.
Causal Language Modelling Approach
The central mechanism for this pre-training is Causal Language Modelling
(CLM). This method specializes in predicting a given token xt relying entirely on its preceding tokens. Formally, the
objective during this training phase is to maximize the likelihood of the entire sequence, as represented by:
P(x1, x2, . . . , xT ) =
T
Y
t=1
P(xt|x1, x2, . . . , xt−1)
(1)
Breaking down the elements of this equation:
• x1, x2, . . . , xT : The individual tokens that constitute the sequence.
• P(xt|x1, x2, . . . , xt−1): Represents the conditional probability of the token xt, which depends on the preced-
ing tokens in the sequence.
Significance of the CLM in Language Adaptation
The CLM stage is integral to enhancing LLaMA’s capability in
Tamil and other languages. It facilitates the model in learning the intricate syntactic patterns, semantic subtleties, and
unique linguistic features of Tamil. Due to its autoregressive characteristics, the CLM mimics the human approach to
comprehending and generating language, which is primarily shaped by the previous context. Hence, at the end of this
initial training period, LLaMA becomes capable of interpreting and creating Tamil text that is pertinent to the given
context. This sets a strong foundation for further fine-tuning and specific task-based training sessions.
3.5
Fine-Tuning Phase
Following the foundational pre-training phase, the fine-tuning phase emerges as a crucial step, especially for modern
Large Language Models (LLMs) deployed in real-world scenarios. A broad understanding of language structure and
semantics, while essential, does not suffice for such applications. This gap is addressed by instruction fine-tuning, a
tailored process enabling LLMs to interpret and execute task-oriented instructions conveyed in natural language. Rather
than the traditional approach of adapting to specific datasets, instruction fine-tuning focuses on a wide array of tasks
articulated through language, ensuring the LLM’s adaptability without task-specific alterations. The datasets employed
in this phase are elaborated in Section 3.1.2.
Instruction fine-tuning’s transformative essence lies in its ability to enhance an LLM’s dynamism and responsiveness.
While pre-training equips the model with general linguistic proficiency, instruction fine-tuning refines it to interact
seamlessly with users through natural language, bridging the gap between overarching language mastery and nuanced,
task-specific agility.
The instruction format employed closely resembles the one described in the original Alpaca dataset (Taori et al., 2023).
Both prompt templates suggested by Alpaca have been utilized: one that includes an input field within the instruction
and another that does not. The prompt templates used during training are given in Figure 2.
It is essential to clarify that in both templates, the first line signifies the system prompts. For the Alpaca dataset (Taori
et al., 2023), we utilize the two system prompts as mentioned in Figure 2. However, for the OpenOrca subset (Lian
et al., 2023), a distinct approach is taken: given that this subset already includes a dedicated field for the system prompt
within its dataset, we utilize that specific prompt.
3.6
Experimental Setup and Training Details
3.6.1
LoRA Approach for Pre-Training and Fine-Tuning
LoRA (Low-Rank Adapters) is a technique that offers an efficient pathway to fine-tuning large language models, as
introduced by Hu et al. (2021). This approach is especially beneficial for its computational efficiency, enabling the
fine-tuning of language models without the need for extensive GPU resources. We employed the LoRA method to
moderate training expenses while also accelerating the training timeline. Training the complete set of parameters
for models like LLaMA can be exceedingly expensive and resource-intensive, which is often beyond the budget of
individual research teams or small organizations.
5

--- Page 6 ---

Figure 2: Prompt Template for Instruction Tasks
1. Prompt Template Without Input
ஒருபணிையஎவ்வாறுநிைறேவற்றேவண
்
டும்என்றுகூறும்அறB-
வுைரகீேழஉள்ளது. ேவண
்
டுேகாைளப்ெபாருத்தமாகநிைறவுெசய்-
கின்றபதில்ஒன்ைறஎழுதுக.
### Instruction:
{instruction}
### Response:
{output}
2. Prompt Template With Input
ஒருபணிையஎவ்வாறுநிைறேவற்றேவண
்
டும்என்றுகூறும்அறB-
வுைரகீேழஉள்ளது. ேமலும்விரிவானபின்னணிையவழங்கும்ஓர்
உள்ளீடும்ெகாடுக்கப்பட்டுள்ளது. ேவண
்
டுேகாைளப்ெபாருத்தமாக
நிைறவுெசய்கின்றபதில்ஒன்ைறஎழுதுக.
### Instruction:
{instruction}
### Input:
{input}
### Response:
{output}
3.6.2
Experimental Setups for Pre-Training
The foundational models of Tamil LLaMA are initiated with the original LLaMA weights and undergo pre-training
using the fp16 precision setting for both the 7B2 and 13B3 parameter versions. We utilize 12GB of Tamil text sourced
from Nguyen et al. (2023) during this pre-training phase. Further insights on the dataset can be found in section 3.1.1.
Our pre-training strategy incorporates the LoRA method Hu et al. (2021), where we integrate LoRA adapters into the
attention vectors and subsequently train the embeddings, LM heads, and the newly incorporated LoRA parameters. A
noteworthy deviation from the methodology of the Chinese LLaMA (Cui et al., 2023) in our approach is the elimination
of the initial exclusive training of embeddings. Instead of following it with a two-stage LoRA training of attention
blocks, embeddings, and LM heads, we’ve opted for a streamlined approach to curb costs.
For the training infrastructure, we harnessed an Nvidia A100 GPU with 80GB of VRAM. The models were trained for
1 epoch on the entire dataset, and the training time spanned 48 hours for 7B model and 60 hours for the 13B model on
Microsoft Azure’s Standard NC24adsA100v4 instance.
The detailed hyperparameters used for training are listed in Table 1.
3.6.3
Experimental Setups for Instruction Fine-Tuning
The 7B4 and 13B5 models, once pre-trained, undergo fine-tuning in alignment with the procedures outlined in Section
3.5. The datasets employed for this phase are elaborated upon in Section 3.1.2. We persist with the LoRA methodology
for fine-tuning, executing it under the fp16 precision setting for both models. Our datasets comprise translated variants
of Alpaca (Taori et al., 2023) and a select subset from OpenOrca (Lian et al., 2023).
2Tamil LLaMA 7B Pretrained: https://huggingface.co/abhinand/tamil-llama-7b-base-v0.1
3Tamil LLaMA 13B Pretrained: https://huggingface.co/abhinand/tamil-llama-13b-base-v0.1
4Tamil LLaMA 7B Instruct: https://huggingface.co/abhinand/tamil-llama-7b-instruct-v0.1
5Tamil LLaMA 13B Instruct: https://huggingface.co/abhinand/tamil-llama-13b-instruct-v0.1
6

--- Page 7 ---

Table 1: Pre-Training Hyperparameters
Configurations
7B
13B
Training Data
12GB
4GB
Epochs
1
1
Batch Size
64
64
Initial Learning Rate
2e-4
2e-4
Max Sequence Length
512
512
LoRA Rank
64
64
LoRA Alpha
128
128
LoRA Target Modules
QKVO, MLP
QKVO, MLP
Training Precision
FP16
FP16
In a bid to augment the models’ proficiency with Tamil-centric literature, cultural nuances, and historical contexts, we
leverage a tailored dataset sourced from Wikipedia. Additionally, to extract instructions from this text, we utilize the
Self-Instruct method, as highlighted in Wang et al. (2023). This approach involves the GPT-4 (OpenAI, 2023) APIs
from OpenAI to generate the new instruction dataset. It is crucial to note that the system prompts, referenced in Section
3.1.2, remain consistent during this supplemental fine-tuning phase. For the hardware, the same A100 GPU with 80GB
of VRAM was utilized.
In summary, our fine-tuning approach employs a new translated dataset consisting of roughly 145,000 instructions. A
detailed account of the hyperparameters used for fine-tuning can be found in the Table 2.
Table 2: Fine-tuning Hyperparameters
Configurations
7B
13B
Training Data
145k
145k
Epochs
2
1
Batch Size
64
64
Dropout Rate
0.1
0.1
Initial Learning Rate
2e-4
2e-4
Max Sequence Length
512
512
LoRA Rank
64
64
LoRA Alpha
128
128
LoRA Target Modules
QKVO, MLP
QKVO, MLP
Training Precision
FP16
FP16
4
Results on Instruction Following Tasks
4.1
Task Design and Evaluation Method
Evaluating the outcomes of text generation tasks is intricate due to their multifaceted formats, distinguishing them
from typical Natural Language Understanding (NLU) tasks. Drawing inspiration from previous studies that employed
GPT-4 (OpenAI, 2023) for scoring, we similarly engage GPT-4 to assign a grade on a 10-point scale to each instance.
This approach is more efficient than human evaluations. However, understanding the potential inaccuracies of GPT-4’s
evaluations, we supplement its scores with manual reviews, adjusting them as necessary. Such hands-on inspections
affirm the consistency and authenticity of the scores, ensuring they genuinely mirror the efficacy of the models under
review.
With the GPT-4-based scoring and manual verifications, we have established a robust evaluation framework for our
Tamil LLaMA. Our assessment suite is diligently designed to provide a basic evaluation of Tamil LLaMA. This suite
comprises over 120 diverse examples, covering areas such as Question Answering, Reasoning, Literature, Entertainment,
Translation, Programming, and Ethics, among others. The overall score for a specific task is computed by summing
the scores from its constituent samples and normalizing it to a 100-point scale. Such an approach ensures a holistic
reflection of the models’ capabilities across varying tasks, yielding a well-rounded measure of their overall performance.
7

--- Page 8 ---

4.2
Generation Parameters
The choice of generation parameters during inference greatly affects the caliber of the results in tasks involving text
generation. Additionally, the degree of quantization can also affect performance. Below are the generation parameters
we adopted for model evaluations:
• Quantization Config: The model is loaded in 8 −bit, with the torch data type specified as bfloat16.
• Context Size: The context size is maintained at the model’s default of 4096 tokens.
• Temperature: We assign a temperature value of 0.2 to guide the randomness during sampling. A lower
temperature prompts the model to produce more deterministic outputs, whereas a higher value boosts diversity,
potentially compromising coherence. For creative instructions, we adjust the temperature to 0.7 to encourage
varied outputs.
• Top-k Sampling: With k set to 50, the model selects its succeeding token from the 50 most probable candidates,
introducing a level of unpredictability and variety to the resulting text.
• Top-p Sampling: Complementing Top-k sampling, we employ Top-p sampling with a threshold of 0.90. This
ensures the model weighs a fluid set of tokens, which, combined, represent 90
• Maximum Sequence Length: To keep the output concise and pertinent, we cap the generated sequence at 512
tokens.
• Repetition Penalty: A repetition penalty of 1.1 is applied to deter the model from producing redundant text,
disincentivizing previously chosen tokens.
For these evaluations, we utilized a Google Colab notebook powered by a T4 GPU.
4.3
Results from Instruction Tasks
The evaluation scores of the Tamil LLaMA models, as rated by GPT-4, are presented in Table 3. A noteworthy
observation during our evaluation is the superior performance of our models compared to gpt-3.5-turbo in manual
assessments, which is further reinforced by the commendable scores in GPT-4’s evaluations. However, it is essential to
consider that GPT-4 might inherently favor responses from other GPT model lineages. Even though our model excels in
numerous tasks, there are areas of exception, such as ethics, and this was anticipated, given that we did not undertake
any alignment efforts. Challenges in literature/entertainment and other areas can be attributed to data limitations during
the pre-training phase, primarily due to cost constraints. Despite these nuances, our models establish a robust foundation
for subsequent enhancements and progress in large language models tailored to Tamil.
Table 3: GPT-4 rated performance scores for different models on Tamil instructions
Task Type
Tamil-LLaMA-7B
Tamil-LLaMA-13B
gpt-3.5-turbo
Question Answering
77.00
75.33
54.33
Open-ended QA
84.47
85.26
58.68
Reasoning
47.50
64.25
63.50
Literature
45.50
40.00
71.00
Entertainment
43.33
50.00
60.00
Creative Writing
92.50
95.62
59.69
Translation
60.56
66.67
92.78
Coding
63.57
76.07
57.14
Ethics
23.75
57.50
40.00
Overall
63.83
71.17
61.33
By observing Table 3, several intriguing outcomes emerge. Notably, the gpt-3.5-turbo, despite its prowess in numerous
languages, appears to be eclipsed by the Tamil LLaMA models in multiple domains. A standout observation was
the Ethics category, where the gpt-3.5-turbo model demonstrated a propensity to respond to potentially dangerous
queries in Tamil. Additionally, in the Coding section, the gpt-3.5-turbo’s responses either seemed to exhibit a lack of
comprehension or overlooked critical details, leading to a subdued score. While gpt-3.5-turbo excels in tasks related to
English and other languages, its performance in the context of Tamil reveals areas for weaknesses.
8

--- Page 9 ---

4.3.1
Reasoning:
In reasoning tasks, the models demonstrate commendable performance. While minor discrepancies occasionally arise in
areas such as dates, quantities, and formulas, they predominantly excel in reasoning exercises. According to our manual
evaluations, even our smaller Tamil-LLaMA 7B model surpasses the performance of the much larger LLaMA 2 70B in
Tamil text generation. In comparison, even gpt-3.5-turbo (OpenAI, 2022) often falters in several reasoning instructions,
producing outputs that miss the mark in relevance, clarity, fluency, and accuracy. This inadequacy in performance is
also observed in LLaMA 2 70B, rendering their generated Tamil text less beneficial. Examples of responses related to
reasoning tasks are given in the Figure 5.
We conducted our comparisons with LLaMA 2 70B using the model hosted by Perplexity Labs.
4.3.2
Translation:
For translation tasks, our models exhibit satisfactory performance, particularly when translating from a foreign language
to Tamil. However, the accuracy diminishes when translating from Tamil to other languages—a shortcoming we aim to
address in future iterations. Based on our manual evaluations, our models outperform the original LLaMA 2 70B in
Tamil text translations. However, their efficacy is roughly on par with gpt-3.5-turbo. Examples of outputs for translation
tasks are given in Figure 6.
4.3.3
Code Generation:
Our models exhibit impressive performance in code generation tasks despite the limited code instructions present
in the training dataset. They capably provide coherent explanations in Tamil for the generated code. Based on our
hands-on evaluations, our models markedly surpass the performance of the more sizable LLaMA 2 70B model, which
when instructed in Tamil, often either misconstrues the task or produces erroneous answers in English. However, it is
important to highlight that our model is not tailored for coding tasks. While it handles more straightforward problems
adeptly, it encounters challenges with more intricate ones. Example responses from our models for Code Generation
tasks can be found in Figure 7.
4.3.4
Open Question Answering
In open question answering tasks, much like in reasoning, the model displays a commendable performance. Despite
occasional inaccuracies in areas like dates and other factual information, its proficiency often exceeded our expectations,
delivering surprising results on multiple instances. Example responses from our models for Open Question Answering
tasks can be found in Figure 8.
4.3.5
Creative Writing / Text Generation
Text generation is a foundational capability for Large Language Models (LLMs), with creative text generation—such as
crafting letters or applications—being a particularly notable use case. In general, larger models have an edge in this
domain, often outshining their smaller counterparts. The quality and quantity of training data play pivotal roles in this
context. While the sheer volume of data can improve performance, the richness and quality of the data are equally vital.
With abundant high-quality training data, even smaller models can sometimes surpass the performance of larger ones.
In our experiments, our models showed decent performance in standard tasks. However, they faced challenges when
assigned with more complicated tasks. Example responses from our models for Creative Writing tasks can be found in
Figure 9.
4.3.6
Mathematical reasoning
Mathematical reasoning presents a significant challenge for our models. Like many Large Language Models (LLMs),
they don’t excel in handling mathematical tasks. From our hands-on experiments, we observed that the performance of
our models, mainly when dealing with Tamil, lagged behind that of the original English LLaMA models. Recognizing
this as an area of improvement, we intend to prioritize and enhance the model’s capabilities in subsequent iterations.
Examples of outputs for mathematical reasoning tasks are given in Figure 10.
4.4
Results from Natural Language Understanding (NLU) tasks
Understanding natural language (NLU) is a vital element within the field of natural language processing (NLP) that
enables computers to comprehend and interpret human language. NLU focuses on comprehending and extracting
9

--- Page 10 ---

meaning from text, whereas text generation is concerned with generating human-like text based on a given input, often
without any specific understanding of the text’s meaning.
To ascertain the prowess of a model, its performance in Natural Language Understanding (NLU) tasks is paramount.
However, the availability of standard benchmarks for Tamil in this domain remains sparse. Notable exceptions include
the IndicNLP (Kunchukuttan, 2020), IndicNLP Corpus (Kunchukuttan et al., 2020), and IndicSentiment (AI4Bharat,
2023) datasets. We opted to assess our models utilizing the test set from the IndicSentiment dataset (AI4Bharat, 2023),
and a text classification dataset sourced from the IndicNLP Corpus (Kunchukuttan et al., 2020).
The test set of the IndicSentiment dataset encompasses 1,000 sentiment samples in Tamil. It is important to note that
our evaluation was concentrated solely on this Tamil subset.
Figure 3: Performance comparison on the IndicSentiment-7B dataset
From Figure 3, it is evident that our Tamil LLaMA model remarkably surpasses the original LLaMA in this specific
NLU task. The latter’s performance mirrors that of random guessing, registering an accuracy of 50.5%. In stark contrast,
our model impressively scores an accuracy of 81.3%. This enhanced NLU capability underscores the efficacy of our
methodologies—such as vocabulary expansion and retraining in facilitating the model to comprehend a new language
like Tamil with heightened proficiency.
We further extended our evaluation to the iNLTK Headline Classification subset within the IndicNLP suite (Kakwani
et al., 2020). It is essential to highlight that our analysis was focused strictly on the Tamil language subset of this dataset.
The outcomes of this evaluation are graphically depicted in Figure 4.
Insight from Figure 4 reveals that the original LLaMA model’s performance aligns closely with random predictions.
In contrast, our Tamil LLaMA model showcases a compelling lead, achieving an accuracy rate of 80.12%, further
affirming its superior capability in natural language understanding.
5
Limitations
The Tamil LLaMA suite of models we introduce in this paper heralds several advancements in Tamil language processing.
However, in the spirit of rigorous research, it is imperative to discuss the inherent limitations accompanying these
models.
10

--- Page 11 ---

Figure 4: Performance comparison on the IndicGLUE Text Classification dataset
• Constrained Knowledge Base: Due to computational and cost constraints, our models were trained on a
relatively limited Tamil dataset. This translates to gaps in the models’ knowledge, especially regarding nuances
and specifics native to Tamil culture and literature. While the current version lays the foundation, the true
potential can be unlocked with access to a broader data spectrum, enriching its contextual understanding.
• Ethical Concerns: Detoxification procedures were not implemented in our training process, making these
models prone to generating potentially harmful or offensive content. Their uncensored nature necessitates
caution during deployment.
• Lack of Robustness: Our models may, at times, produce outputs that veer off-topic or deviate substantially
from anticipated responses. This vulnerability is more pronounced under adversarial conditions or tricky
prompts.
• Reasoning and Mathematical Challenges: While our models showcase competence in specific reasoning
scenarios, they falter in many others, underscoring the repercussions of not having a comprehensive training
set.
• Over-Generation Tendencies: On occasions, the models tend to generate verbose content, extending beyond
logical termination points, leading to potential redundancy.
• Evaluation Hurdles: Assessment of LLMs is a crucial yet challenging endeavor. The scarcity of standardized
benchmarks, particularly for languages like Tamil, which are outside the European linguistic group, complicates
comparative evaluations. Although we propose an evaluative approach tailored for Tamil within this paper, it
is not exhaustive enough to gauge models’ efficacy across diverse domains.
• Translation Loss: Given that the instructional prompts used for fine-tuning the Tamil LLaMA base models are
derived from English datasets translated into Tamil, there is a potential for nuanced inaccuracies—commonly
referred to as translation loss. This can potentially affect the models’ abilities in both text generation and
comprehension due to subtle shifts in meaning that can occur during the translation process.
While some of these challenges are addressable in subsequent iterations, we envision this work serving as an anchor,
inspiring the research community to propel advancements in LLMs for Indian languages.
11

--- Page 12 ---

6
Conclusion
In this research endeavor, we have not only filled a critical void in the domain of Tamil text generation but have also
elevated the status of this venerable language within the realm of large language models with the advent of our Tamil
LLaMA.To assess the performance of our models, we curated an evaluation dataset consisting of 120 Tamil instructions
covering a wide range of topics. We then employed GPT-4 to assess and rate the responses generated by our model. The
7B variant of our model has surpassed the performance of OpenAI’s gpt-3.5-turbo in tasks involving Tamil instructions
within our evaluation methodology. Even more impressively, the 13B iteration has outperformed its counterparts,
demonstrating an almost 10% higher proficiency in these tasks.
The significance of our findings is accentuated by the efficiency of our models in generating Tamil text. Equipped with
a refined tokenizer, the 7B and 13B variants demonstrate exceptional proficiency, eclipsing the original LLaMA models
in processing speed without sacrificing textual quality. This stride is not just a modest step forward but a major leap in
the models’ ability to process and generate Tamil language content, thus forging a new avenue for practical applications
that necessitate precision and promptness.
Nevertheless, our exploration in this field continues. We acknowledge the triumphs and yet remain mindful of the
impending obstacles. The possibility of generating unintended or adverse content, the financial limitations associated
with model training, and the need for comprehensive evaluation benchmarks tailored for Tamil are challenges we are
committed to surmounting.
As we chart our path forward, we acknowledge the value of continuous learning and adaptation. We aspire to delve
deeper into strategies to mitigate the limitations observed, perhaps even leveraging advancements like Reinforcement
Learning With Human Feedback (RLHF) and more advanced quantization techniques. The horizon looks promising,
and we remain committed to elevating the capabilities of LLaMA for Tamil and other Indian languages.
Appendix
Example Outputs
Figure 5: Example Output for Reasoning Tasks
Prompt
ேமைஜயில்
4 ஆப்பிள்கள்
இருந்தன. குமார்ஒன்ைறச்
சாப்பிட்டான், ராம்
எடுத்துச்
ெசன்றான்
2.
மீதிஎத்-
தைனஆப்பிள்கள்
உள்ளன?
7B Model
முதலில், நாம்4 - 1 = 3 ஆப்பிள்கைளஎடுத்துக்ெகாள்-
ளலாம், ஏெனனில்குமார்ஒன்றுசாப்பிட்டார். அடுத்து,
ராம்2 ஆப்பிள்கைளஎடுத்துச்ெசன்றார், எனேவமீத-
முள்ளஆப்பிள்களின்
எண
்
ணிக்ைக3 - 2 = 1 ஆகும்.
எனேவ, மீதமுள்ளஆப்பிள்
1 உள்ளது.
13B Model
இப்ேபாது, இந்தக்
ேகள்விக்குபதிலளிக்க, நாம்
சூத்தி-
ரத்ைதப்பயன்படுத்தலாம்:
ெமாத்தஆப்பிள்கள்= ஆரம்பஆப்பிள்கள்- சாப்பிட்ட
ஆப்பிள்கள்
- எடுத்துச்ெசன்றஆப்பிள்கள்
ஆரம்பஆப்பிள்கள்
= 4
சாப்பிட்டஆப்பிள்கள்
= 1
எடுக்கப்பட்டஆப்பிள்கள்
= 2
இப்ேபாதுஇந்தமதிப்புகைளசூத்திரத்தில்ெசருகலாம்:
ெமாத்தஆப்பிள்கள்
= 4 - 1 - 2 = 1
எனேவ, ேமைஜயில்1 ஆப்பிள்
உள்ளது.
12

--- Page 13 ---

Figure 6: Example Outputs for Translation Tasks
Example 1
Prompt
தயவுெசய்துபின்வரும்வாக்கியத்ைததமBழBல்
ெமாழB-
ெபயர்க்கவும்:
”We’ve trained a model called ChatGPT which interacts in
a conversational way. The dialogue format makes it possible
for ChatGPT to answer followup questions, admit its mis-
takes, challenge incorrect premises, and reject inappropriate
requests.”
7B Model
நாங்கள்
சாட்ேபாட்
என்றெபயரில்
பயிற்சியளிக்கப்-
பட்டமாதிரிையக்
ெகாண
்
டுள்ேளாம், இதுஉைரயாட-
லில்ேபசுவதுேபால்ெசயல்படுகிறது. உைரயாடல்வடி-
வைமப்பின்
மூலம், ேகள்விகளுக்குபதிலளிக்கும்
தி-
றன்
மற்றும்தவறானஅறBக்ைககைளமறுக்கும்திறன்
ேபான்றபலவிஷயங்கைளச்ெசய்யசாட்ேபாட்அனு-
மதிக்கிறது.
கூடுதலாக, சாட்ேபாட்
சிலேநரங்களில்
அதன்
தவறுகளில்
ஒப்புக்ெகாள்கிறார்
மற்றும்
ெபா-
ருத்தமற்றேகாரிக்ைககைளக்கூடநிராகரிக்கிறார்.
13B Model
நாங்கள்”ChatGPT” என்றமாதிரிையபயிற்றுவித்துள்-
ேளாம், இதுஉைரயாடல்
முைறயில்
ெதாடர்புெகாள்-
கிறது. இந்தேபச்சுவழக்குவடிவமானது, பின்ெதாடர்-
தல்
ேகள்விகளுக்குபதிலளிக்கவும், தவறுகைளச்சரி-
பார்க்கவும், தவறானமுன்ெமாழBவுகைளசவால்ெசய்-
யவும்மற்றும்ெபாருத்தமற்றேகாரிக்ைககள்
மீதுநிரா-
கரிக்கவும்ChatGPT ஐஅனுமதிக்கிறது.
Example 2
Prompt
தயவுெசய்துபின்வரும்வாக்கியத்ைததமBழBல்
ெமாழB-
ெபயர்க்கவும்:
”Estoy pensando en viajar a Inglaterra para ver el partido
entre Inglaterra y España de este fin de semana. ¡Va a ser
emocionante!”
7B Model
நான்
இந்தவாரஇறுதியில்
இங்கிலாந்தில்
கால்பந்து
விைளயாட்ைடப்பார்க்கவிரும்புகிேறன், இதுமBகவும்
சுவாரஸ்யமாகஇருக்கும்!
13B Model
நான்
இந்தவாரஇறுதியில்
இங்கிலாந்துமற்றும்
ஸ்-
ெபயின்
இைடேயயானகால்பந்துவிைளயாட்ைடப்
பார்க்க
இங்கிலாந்ைதச்
ெசல்லத்
திட்டமBடுகிேறன்!
இதுமBகவும்உற்சாகமாகஇருக்கும்!
13

--- Page 14 ---

Figure 7: Example Output for Coding Tasks
Prompt: ைபத்தானில்”Quick Sort” அல்காரிதத்ைதெசயல்ப-
டுத்தவும்.
7B Model:
நிச்சயம்! ைபதான்
குறBயீடுதுணுக்குஇேதா, இதுQuickSort அல்-
காரிதத்ைதப்பயன்படுத்திவரிைசப்படுத்தப்பட்டபட்டியைல
உருவாக்கப்பயன்படும்:
def quick_sort(arr):
if len(arr) <= 1:
return arr
pivot = arr[0]
less = [x for x in arr[1:] if x < pivot]
greater = [x for x in arr[1:] if x > pivot]
return quick_sort(less) + [pivot] + quick_sort
(greater)
my_list = [5, 3, 7, 2, 9, 4]
result = quick_sort(my_list)
print(result) # Output: [2, 3, 5, 4, 7, 9]
குறBயீட்டின்
ெவளியீடு, வரிைசப்படுத்தப்பட்டபட்டியலில்உள்ள
உறுப்புகளின்
மறுசீரைமக்கப்பட்டவரிைசையவழங்குகிறது.
இதுஉதவும்என்றுநான்
நம்புகிேறன்! உங்களுக்குஏேதனும்
ேகள்விகள்
இருந்தால்எனக்குெதரியப்படுத்தவும்.
13B Model:
ைபத்தானில்QuickSort அல்காரிதம்ெசயல்படுத்துவதற்கான
எடுத்துக்காட்டுஇங்ேக:
def quick_sort(arr):
if len(arr) <= 1:
return arr
pivot = arr[0]
left, right = [], []
for i in range(1, len(arr)):
if arr[i] < pivot:
left.append(arr[i])
else:
right.append(arr[i])
return quick_sort(left) + [pivot] + quick_sort
(right)
arr = [2, 3, 5, 7, 9, 10, 11]
result = quick_sort(arr)
print("The sorted array is:", result)
14

--- Page 15 ---

Figure 8: Example Output for Open Question Answering Tasks
Prompt: நான்
ெபரியபணக்காரன்
இல்ைல, சமீபத்தியiPhone
15'க்குநிைறயபணம்ெசலவழBக்கேவண
்
டுமா?
7B Model:
AI ஆக, எனக்குதனிப்பட்டவிருப்பங்கள்அல்லதுநிதிஇலக்-
குகள்இல்ைல. இருப்பினும், உங்கள்ேதைவகளுக்குஏற்றெதா-
ைலேபசிையத்ேதர்ந்ெதடுப்பதுமற்றும்உங்கள்பட்ெஜட்ைடக்
கருத்தில்ெகாள்வதுமுக்கியம். சமீபத்தியஐேபான்களில்வி-
ைலகள்
அதிகமாகஇருக்கலாம், ஆனால்
நீங்கள்
விரும்பிய
அம்சங்கைளவழங்குவதில்அைவஇன்னும்சிறந்தைவ. உங்-
கள்
ேதைவகைளப்
பூர்த்திெசய்யும்
ஒன்ைறத்ேதர்வுெசய்ய-
வும், ேமலும்கூடுதல்ெசலவுகைளச்ேசமBக்கஉதவும்வைகயில்,
தள்ளுபடிகள்
அல்லதுஒப்பந்தங்கைளப்பார்க்கவும்.
உங்கள்பட்ெஜட்டுக்குள்இருக்கமுயற்சிப்பதும்முக்கியம். உங்-
கள்
ெசலவினங்கைளக்கண
்
காணித்து, உங்கள்
ெசலவினங்-
களுக்குமுன்னுரிைமஅளிக்கவும். இதுேதைவயற்றெசலவு-
கைளத்தவிர்க்கவும், உங்கள்பணத்ைதச்ேசமBப்பதற்கானவழB-
கைளக்கண
்
டறBயவும்உதவும்.
இறுதியில், உங்கள்ேதைவகள்மற்றும்பட்ெஜட்டிற்குஏற்றெதா-
ைலேபசிையத்ேதர்ந்ெதடுப்பதுமுக்கியம். உங்கள்
பட்ெஜட்-
டில்ஒட்டிக்ெகாண
்
டு, உங்களுக்குத்ேதைவயானஅம்சங்கைளத்
ேதடுங்கள்.
இருப்பினும், சமீபத்தியஐேபான்களில்ஒன்றுநிச்சயமாகஅதிக
விைலயில்இருக்கும்என்பைதநிைனவில்ெகாள்ளுங்கள்.
15

--- Page 16 ---

Figure 9: Example Output for Creative Writing Tasks
Example:
Prompt: ஐபிஎல்
ெதாடைரெசன்ைனசூப்பர்கிங்ஸ்
(சிஎஸ்-
ேக) ெவன்றதுஎன்றதைலப்பில்
ஒருசிறுெசய்திக்கட்டுைர-
ையஎழுதுங்கள்.
7B Model:
ெசன்ைனசூப்பர்கிங்ஸ்
(சிஎஸ்ேக) 2021 இந்தியன்
பிரீமBயர்
லீக்கில்(ஐபிஎல்) இறுதிப்ேபாட்டிையெவன்றது, அவர்களின்
மூன்றாவதுஐபிஎல்
பட்டத்ைதஉறுதிெசய்தது. இந்தெவற்-
றBயின்
மூலம், சிஎஸ்ேகஅணிக்காகவிைளயாடியேகப்டன்
ேதானிதைலைமயிலானஇளம்மற்றும்திறைமயானவீரர்க-
ளின்
குழுவிற்குஇதுஒருகுறBப்பிடத்தக்கசாதைனயாகும்.
சமீபத்தியசீசன்
முழுவதும், சிஎஸ்ேகஅணிபலசவால்கைள
எதிர்ெகாண
்
டது, ஆனால்
அவர்கள்
ெதாடர்ந்துதங்கள்
திற-
ைமகைளயும்நம்பிக்ைகையயும்ெவளிப்படுத்தினர். அணி-
யின்
ேவகப்பந்துவீச்சு, ேபட்டிங்
மற்றும்ஃபீல்டிங்
ஆகியவற்-
றBன்
வலுவானகலைவயானதுஅவர்களின்
ேபாட்டியாளர்-
களின்
பலேமாசமானஆட்டங்களுக்குவழBவகுத்தது, ேமலும்
அவர்கள்இறுதிப்ேபாட்டியில்அவர்களின்
ெசாந்தவிைளயாட்-
டுகளில்ஆதிக்கம்ெசலுத்தமுடிந்தது.
இந்தெவற்றBயின்
மூலம், சிஎஸ்ேகஅணிமூன்றுஐபிஎல்சாம்-
பியன்ஷCப்கைளெவன்றுள்ளது, ேமலும்அவர்களின்
ரசிகர்-
கள்மகிழ்ச்சியில்மூழ்கிஉள்ளனர். ேதானியும்அவரதுஅணி-
யும்
பலஆண
்
டுகளாகஇந்தியகிரிக்ெகட்அரங்கில்
முக்கிய
நபராகஇருந்துவருகின்றனர், ேமலும்இந்தெவற்றB அவர்க-
ளின்
பாரம்பரியத்ைதேமலும்உயர்த்துகிறது.
ஒட்டுெமாத்தமாக, சிஎஸ்ேகஅணிஇந்தசீசனின்
ஐபிஎல்ெதா-
டர்இறுதிப்ேபாட்டிக்குமுன்ேனறBயதில்ஒருெபரியசாதைன-
ையக்ெகாண
்
டிருந்தது, ேமலும்அவர்களின்
ரசிகர்கள்இப்ேபா-
துஒருவருடம்கழBத்துதங்கள்அணிக்குஉற்சாகத்ைதயும்ஆத-
ரைவயும்காட்டஎதிர்பார்க்கிறார்கள்.
16

--- Page 17 ---

Figure 10: Example Outputs for Mathematical Reasoning Tasks
Example 1
Prompt
7! என்றால்என்னஎன்பைதக்கணக்கிடுங்கள்
7B Model
7! என்பது7 x 6 x 5 x 4 x 3 x 2 x 1 என்றெபருக்கல்
ெவளிப்பாட்ைடக்
குறBக்கிறது, இதுேதாராயமாக870
ஆகும்.
எனேவ, 7! = 870
13B Model
7! என்பது7 இன்
காரணிகளின்
எண
்
ணிக்ைக, அதா-
வது1 x 2 x 3 x 4 x 5 x 6 x 7 ஆகும். எனேவ, 7! = 5040
ஆகும்.
Example 2
Prompt
3x+1=10 என்றால், x எதற்குசமம்?
7B Model
ெகாடுக்கப்பட்டசமன்பாடு3x + 1 = 10 எனில், x க்குதீர்-
வுகாண, நாம்பின்வரும்படிகைளப்பின்பற்றலாம்:
படி1: சமன்பாட்டின்
இருபக்கங்களிலிருந்தும்
1 ஐக்
கழBக்கவும். இதுநமக்குஅளிக்கிறது:
3x + 1 −1 = 10 −1
3x = 9
படி2:
இப்ேபாதுஎங்களிடம்
4x இன்
மதிப்புஇருப்ப-
தால், அைதஅசல்சமன்பாட்டில்மாற்றலாம்: 3x+1 = 10
3(9) + 1 = 10
29 + 1 = 10
30 = 10
எனேவ, x க்கானதீர்வு30 ஆகும்.
இருப்பினும், ெகாடுக்கப்பட்டசமன்பாட்டிற்கானசரி-
யானதீர்ைவநீங்கள்ேதடுகிறீர்களானால், x இன்
மதிப்-
ைபப்ெபற, இருபக்கங்கைளயும்3 ஆல்வகுக்கேவண
்
-
டும்.
x = (30/3)
x = 10
எனேவ, x என்பது10க்குசமம்.
13B Model
3x + 1
=
10 சமன்பாட்டில்
x க்குதீர்வுகாணும்ேபா-
து, சமன்பாட்டின்
ஒருபக்கத்தில்
மாறBையதனிைமப்-
படுத்தேவண
்
டும்.
முதலில், சமன்பாட்டின்
இருபக்கங்களிலிருந்தும்1 ஐக்
கழBப்பதன்
மூலம்ெதாடங்கலாம்:
3x + 1 −1 = 10 −1
இதுஎளிதாக்குகிறது:
3x = 9
அடுத்து, சமன்பாட்டின்
இருபக்கங்கைளயும்
3 ஆல்
வகுப்பதன்
மூலம்x ஐதனிைமப்படுத்துேவாம்:
(3x)/3 = (9)/3
இதுஎளிதாக்குகிறது:
x = 3
எனேவ, 3x + 1 = 10 சமன்பாட்டிற்கானதீர்வுx = 3
ஆகும்.
17

--- Page 18 ---

Acknowledgments
We gratefully acknowledge the assistance of OpenAI’s GPT-4 in the preparation of this manuscript. The AI’s advanced
language understanding and generation capabilities were invaluable in refining the structure, clarity, and overall
coherence of the original draft.
References
AI4Bharat.
Indic sentiment dataset by ai4bharat.
https://huggingface.co/datasets/ai4bharat/
IndicSentiment, 2023.
J. Ainslie, J. Lee-Thorp, M. de Jong, Y. Zemlyanskiy, F. Lebrón, and S. Sanghai. Gqa: Training generalized multi-query
transformer models from multi-head checkpoints, 2023.
I. Caswell, T. Breiner, D. van Esch, and A. Bapna. Language id in the wild: Unexpected challenges on the path to a
thousand-language web text corpus, 2020.
Y. Cui, Z. Yang, and X. Yao. Efficient and effective text encoding for chinese llama and alpaca, 2023.
J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova. Bert: Pre-training of deep bidirectional transformers for language
understanding, 2019.
E. J. Hu, Y. Shen, P. Wallis, Z. Allen-Zhu, Y. Li, S. Wang, L. Wang, and W. Chen. Lora: Low-rank adaptation of large
language models, 2021.
A. Q. Jiang, A. Sablayrolles, A. Mensch, C. Bamford, D. S. Chaplot, D. de las Casas, F. Bressand, G. Lengyel,
G. Lample, L. Saulnier, L. R. Lavaud, M.-A. Lachaux, P. Stock, T. L. Scao, T. Lavril, T. Wang, T. Lacroix, and W. E.
Sayed. Mistral 7b, 2023.
D. Kakwani, A. Kunchukuttan, S. Golla, G. N.C., A. Bhattacharyya, M. M. Khapra, and P. Kumar. IndicNLPSuite:
Monolingual corpora, evaluation benchmarks and pre-trained multilingual language models for Indian languages.
In Findings of the Association for Computational Linguistics: EMNLP 2020, pages 4948–4961, Online, Nov.
2020. Association for Computational Linguistics. doi: 10.18653/v1/2020.findings-emnlp.445. URL https://
aclanthology.org/2020.findings-emnlp.445.
T. Kudo and J. Richardson. Sentencepiece: A simple and language independent subword tokenizer and detokenizer for
neural text processing, 2018.
A. Kunchukuttan. The IndicNLP Library. https://github.com/anoopkunchukuttan/indic_nlp_library/
blob/master/docs/indicnlp.pdf, 2020.
A. Kunchukuttan, D. Kakwani, S. Golla, G. N.C., A. Bhattacharyya, M. M. Khapra, and P. Kumar. Ai4bharat-indicnlp
corpus: Monolingual corpora and word embeddings for indic languages. arXiv preprint arXiv:2005.00085, 2020.
W. Lian, B. Goodson, E. Pentland, A. Cook, C. Vong, and "Teknium". Openorca: An open dataset of gpt augmented
flan reasoning traces. https://https://huggingface.co/Open-Orca/OpenOrca, 2023.
X. V. Lin, T. Mihaylov, M. Artetxe, T. Wang, S. Chen, D. Simig, M. Ott, N. Goyal, S. Bhosale, J. Du, R. Pasunuru,
S. Shleifer, P. S. Koura, V. Chaudhary, B. O’Horo, J. Wang, L. Zettlemoyer, Z. Kozareva, M. Diab, V. Stoyanov, and
X. Li. Few-shot learning with multilingual language models, 2022.
A. Mahendiran. abinayam/gpt-2-tamil. https://huggingface.co/abinayam/gpt-2-tamil, 2021.
T. Nguyen, C. V. Nguyen, V. D. Lai, H. Man, N. T. Ngo, F. Dernoncourt, R. A. Rossi, and T. H. Nguyen. Culturax: A
cleaned, enormous, and multilingual dataset for large language models in 167 languages, 2023.
OpenAI. Introducing chatgpt. https://openai.com/blog/chatgpt, 2022.
OpenAI. Gpt-4 technical report, 2023.
A. Radford,
K. Narasimhan,
T. Salimans,
and I. Sutskever.
Improving language understanding by
generative pre-training.
https://s3-us-west-2.amazonaws.com/openai-assets/research-covers/
language-unsupervised/language_understanding_paper.pdf, 2018.
A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever. Language models are unsupervised mul-
titask learners. https://d4mucfpksywv.cloudfront.net/better-language-models/language_models_
are_unsupervised_multitask_learners.pdf, 2019.
T. L. Scao, A. Fan, C. Akiki, E. Pavlick, S. Ili´c, D. Hesslow, R. Castagné, A. S. Luccioni, F. Yvon, M. Gallé, et al.
Bloom: A 176b-parameter open-access multilingual language model. arXiv preprint arXiv:2211.05100, 2022.
N. Shazeer. Glu variants improve transformer, 2020.
18

--- Page 19 ---

O. Shliazhko, A. Fenogenova, M. Tikhonova, V. Mikhailov, A. Kozlova, and T. Shavrina. mgpt: Few-shot learners go
multilingual, 2022. URL https://arxiv.org/abs/2204.07580.
J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu. Roformer: Enhanced transformer with rotary position embedding,
2022.
R. Taori, I. Gulrajani, T. Zhang, Y. Dubois, X. Li, C. Guestrin, P. Liang, and T. B. Hashimoto. Stanford alpaca: An
instruction-following llama model. https://github.com/tatsu-lab/stanford_alpaca, 2023.
H. Touvron, T. Lavril, G. Izacard, X. Martinet, M.-A. Lachaux, T. Lacroix, B. Rozière, N. Goyal, E. Hambro, F. Azhar,
A. Rodriguez, A. Joulin, E. Grave, and G. Lample. Llama: Open and efficient foundation language models, 2023a.
H. Touvron, L. Martin, K. Stone, P. Albert, A. Almahairi, Y. Babaei, N. Bashlykov, S. Batra, P. Bhargava, S. Bhosale,
D. Bikel, L. Blecher, C. C. Ferrer, M. Chen, G. Cucurull, D. Esiobu, J. Fernandes, J. Fu, W. Fu, B. Fuller, C. Gao,
V. Goswami, N. Goyal, A. Hartshorn, S. Hosseini, R. Hou, H. Inan, M. Kardas, V. Kerkez, M. Khabsa, I. Kloumann,
A. Korenev, P. S. Koura, M.-A. Lachaux, T. Lavril, J. Lee, D. Liskovich, Y. Lu, Y. Mao, X. Martinet, T. Mihaylov,
P. Mishra, I. Molybog, Y. Nie, A. Poulton, J. Reizenstein, R. Rungta, K. Saladi, A. Schelten, R. Silva, E. M. Smith,
R. Subramanian, X. E. Tan, B. Tang, R. Taylor, A. Williams, J. X. Kuan, P. Xu, Z. Yan, I. Zarov, Y. Zhang, A. Fan,
M. Kambadur, S. Narang, A. Rodriguez, R. Stojnic, S. Edunov, and T. Scialom. Llama 2: Open foundation and
fine-tuned chat models, 2023b.
A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, Ł. Kaiser, and I. Polosukhin. Attention is all
you need. Advances in neural information processing systems, 30, 2017.
Y. Wang, Y. Kordi, S. Mishra, A. Liu, N. A. Smith, D. Khashabi, and H. Hajishirzi. Self-instruct: Aligning language
models with self-generated instructions, 2023.
B. Zhang and R. Sennrich. Root mean square layer normalization, 2019.
19

```
