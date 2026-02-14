---
title: "2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace - PDF Extract"
source_pdf: "2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace.pdf"
pages: 17
extracted_at: "2026-02-13T17:43:24.827190"
---

# PDF Extract: 2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace

**Source PDF:** 2025-Singh-Rethinking Hate Speech Detection on Social Media Can LLMs Replace.pdf
**Total Pages:** 17

---

## Content

```
--- Page 1 ---

arXiv:2506.12744v1  [cs.CL]  15 Jun 2025
Rethinking Hate Speech Detection on Social Media: Can LLMs Replace
Traditional Models?
DAMAN DEEP SINGH∗, Indian Institute of Technology Delhi, India
RAMANUJ BHATTACHARJEE∗, Indian Institute of Technology Kharagpur, India
ABHIJNAN CHAKRABORTY, Indian Institute of Technology Kharagpur, India
Hate speech detection across contemporary social media presents unique challenges due to linguistic diversity and the informal nature
of online discourse. These challenges are further amplified in settings involving code-mixing, transliteration, and culturally nuanced
expressions. While fine-tuned transformer models, such as BERT, have become standard for this task, we argue that recent large
language models (LLMs) not only surpass them but also redefine the landscape of hate speech detection more broadly. To support
this claim, we introduce IndoHateMix, a diverse, high-quality dataset capturing Hindi–English code-mixing and transliteration in
the Indian context, providing a realistic benchmark to evaluate model robustness in complex multilingual scenarios where existing
NLP methods often struggle. Our extensive experiments show that cutting-edge LLMs (such as, LLaMA-3.1) consistently outperform
task-specific BERT-based models, even when fine-tuned on significantly less data. With their superior generalization and adaptability,
LLMs offer a transformative approach to mitigating online hate in diverse environments. This raises the question of whether future
works should prioritize developing specialized models or focus on curating richer and more varied datasets to further enhance the
effectiveness of LLMs.
Disclaimer: This paper contains content that readers may find offensive; unfortunately, it’s an inherent aspect of studying hate speech.
CCS Concepts: • Information systems →Social networks; • Social and professional topics →Hate speech; • Computing
methodologies →Natural language processing.
Additional Key Words and Phrases: Hate Speech Detection, Code-Mixed Language, Multilingual NLP, Large Language Models, LLMs,
IndoHateMix Dataset, Fine-Tuning
1
Introduction
Social media has transformed the way people interact, with various forms of interactions transcending geographical
and linguistic barriers. However, this increased connectivity has also brought challenges, including the spread of hate
speech, which can divide societies and harm vulnerable groups. Hate Speech refers to any form of communication that
expresses hostility, discrimination, or incites harm against an individual or group based on characteristics such as race,
religion, ethnicity, gender, or political beliefs [44, 62]. Hate speech is increasingly becoming a concern in many parts of
the world. Its rapid spread over social media not only deepens social divisions but also threatens peace and harmony
between communities [17]. Real-world incidents have starkly highlighted the dangers of unchecked hate speech. It has
been a driving force behind major events such as the Rohingya crisis [36], the 2020 Delhi riots [28], and the 2021 U.S.
Capitol riot [51]. Furthermore, incidents like the atrocities against minorities in Bangladesh [55] and ethnic violence in
Ethiopia underscore how digital platforms can amplify extremism and fuel social unrest [38].
Hate speech detection and mitigation is a critical task in Natural Language Processing (NLP). Much of the existing
work has focused on fine-tuning transformer models like BERT and its variants, which have demonstrated strong
performance in hate speech classification on certain datasets [8, 19]. However, these approaches are primarily limited
to English-language contexts, restricting their applicability in multilingual settings. Prior to BERT, traditional machine
∗Both authors contributed equally to this research.
Authors’ Contact Information: Daman Deep Singh, Indian Institute of Technology Delhi, India; Ramanuj Bhattacharjee, Indian Institute of Technology
Kharagpur, India; Abhijnan Chakraborty, Indian Institute of Technology Kharagpur, India.

--- Page 2 ---

Singh et al.
learning techniques (e.g., SVM, Naive Bayes) and earlier neural network architectures used for hate speech detection
also struggled to capture complex linguistic patterns. In countries like India, where code-mixing — the blending of
multiple languages in a single sentence — and transliteration — writing one language using the script of another —
are common, making the detection of hate speech in such context even more challenging [14, 15, 64]. For instance,
code-mixed languages like Hindi-English (Hinglish) and transliterated text introduce additional complexities due to
informal syntax, variable grammar, and a lack of standardized datasets.
The emergence of large language models (LLMs) such as GPT-4o and LLaMA-3 has revolutionized NLP, demonstrating
remarkable zero-shot and few-shot learning capabilities [2, 58]. Pre-trained on extensive and diverse corpora, these
models require minimal task-specific fine-tuning and can adapt to new tasks with only a small set of high-quality
samples [6, 42]. This adaptability makes them highly effective at detecting both overt and subtle hate speech. However,
the challenge intensifies in code-mixed and transliterated speech, where the blending of languages demands handling
complex syntactic and semantic nuances [62]. In this work, we aim to explore whether LLMs, with their broader
linguistic adaptability and context awareness, surpass fine-tuned transformers in detecting hate speech across diverse hate
speech instances, including the complex multilingual environments that involve code-mixing and transliteration. Our
investigation also questions whether developing specialized hate speech detection models for this task remains a worthwhile
research endeavor.
To this end, we conducted a comprehensive benchmarking study on three diverse datasets: HateXplain[34],
ImplicitHate[21], and our newly introduced IndoHateMix. While HateXplain and ImplicitHate include challenges
like implicit vs. explicit hate speech classification, rationale-based explanations, and span-based toxicity annotations,
they and other existing benchmarks largely overlook the complexities of code-mixed hate speech. To bridge this gap,
we introduce IndoHateMix, specifically designed to tackle Hindi-English code-mixed hate speech – a critical but
underexplored research area.
Through extensive experiments, we demonstrate that, indeed, LLMs significantly outperform traditional BERT-
based transformers in hate speech detection. Our evaluation further demonstrates that recent open-source LLMs,
like LLaMA-3.1, even when fine-tuned on just 10% of the available data, outperform fine-tuned BERT-based models
trained on the full dataset. The results highlight not only the superior generalization of LLMs in resource-constrained
settings but also the significance of IndoHateMix in appropriately benchmarking hate speech detection models in
complex scenarios involving code-mixed and transliterated texts. We complemented our benchmarking with in-depth
error analysis and target-wise analyses to uncover where models stumble, and to distinguish whether hate is aimed at
communities or individuals. These insights also underscore the value of a nuanced dataset like IndoHateMix, which
captures the subtle dynamics of real-world hate speech.
To summarize, our main contributions in this paper are as follows:
• We conduct a comprehensive comparative analysis of state-of-the-art hate speech classification models – from
fine-tuned transformers to LLMs – across multiple datasets that span diverse cultural and linguistic contexts.
• We introduce IndoHateMix, a high-quality benchmark capturing Hindi–English code-mixing and translitera-
tion, designed to reflect the linguistic and cultural nuances of the Indian online discourse.
• We provide empirical evidence showing that LLMs performs very well in this task, generalizing across different
languages and cultural contexts, even in low-resource settings. This is supported by detailed error analysis,
which reveals traditional models’ limitations in hate speech detection in various scenarios.

--- Page 3 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
Our findings raise the question of whether future research in this area should prioritize developing specialized models
or focus on curating more diverse datasets to further enhance LLMs’ effectiveness in hate speech detection, contributing
to safer and inclusive digital spaces.
2
Related Works
Considering its importance in maintaining the sanctity of online social media, research on Hate Speech has taken
different routes – some works investigated its impact (and patterns of attack) on individuals and groups, and others
examined the detection and mitigation approaches. In this section, we attempt to cover research works belonging to
both these categories.
2.1
Hate Speech: Patterns, Targets and Effects
Many studies have explored the impact of hate speech on various communities, highlighting its pervasive presence
both online and in offline settings. Hate speech often disproportionately targets marginalized and vulnerable groups,
including religious minorities, women, Dalits, immigrants, and LGBTQ+ individuals [54]. These attacks are not limited
to personal insults or isolated incidents; rather, they contribute to a broader environment of hostility and exclusion.
The consequences can extend beyond individual experiences and instill widespread fear, inflict lasting emotional and
psychological stress, and normalize discriminatory attitudes within the society.
In addition to detecting hate speech, it is often necessary to identify who is targeted and how the hate speech is
communicated. This is especially important in multilingual countries where people writing in different languages use
different ways to express things. Talat and Hovy [57] studied hate speech on Twitter and looked at which groups were
being targeted and how personal opinions might affect the way people label hate. Mathew et al. [34] developed an
approach and a dataset that not only says whether a post is hateful or not but also explains why and shows which
group is being targeted. Researchers have also looked at how hate speech occurs in different countries. In India, it
is usually aimed at religious groups and is influenced by politics and community tensions [50]. In Myanmar, hatred
against the Rohingya was spread on Facebook, leading to actual physical violence leading to mass migration [56]. In
Germany, hate on the Internet directed at immigrants has been associated with an increase in hate crimes [37]. The
same is also observed in the US, particularly during elections when hate speech tends to target racial minorities and
immigrants [32]. Another significant thing researchers discovered is that hate speech is not always explicit. Humans
tend to hide it using code words, sarcasm, memes, or slang [31]. Because of this, it becomes more difficult for automatic
systems to detect it. Additionally, because online content spreads quickly, these hidden forms of hate speech can reach
many people rapidly.
2.2
Detection and Mitigation Approaches
Hate speech detection has been an active field of research, with numerous datasets and models developed to address
this challenge. Several studies have explored hate speech detection in English, often contributing benchmark datasets
such as HateXplain [34], OLID [62], ImplicitHate [21], ToxicSpans [43], and Stormfront [17]. Recent efforts have also
focused on low-resource languages including code-mixed and transliterated text [5, 11, 20, 49, 61]. The progression of
hate speech detection models can be categorized into the following three phases:
(1) Pre-BERT Approaches: Initial solutions used traditional machine learning methods like Support Vector
Machines (SVM) [59], Naïve Bayes classifiers [16], and Random Forests [53]. Additionally, rule-based and

--- Page 4 ---

Singh et al.
lexicon-based methods were widely used, where systems relied on predefined word lists and linguistic rules to
identify hate speech [53, 59]. These relied on manually crafted features such as n-grams and sentiment lexicons
but struggled with contextual understanding and generalization.
(2) BERT-Based Models: The advent of transformer-based models, particularly BERT [19], significantly improved
text classification by capturing contextual relationships more effectively. Fine-tuned BERT models like HateBERT
[8] outperformed conventional methods but were mostly trained on monolingual data and weak against code-
mixed and transliterated text.
(3) Large Language Models (LLMs): More recently, LLMs such as GPT-4 [2], T5 [48], and LLaMA [58] have enabled
zero-shot and few-shot learning for hate speech detection [30]. While LLMs show promise in multilingual
settings, studies have shown that they often underperform on code-mixed and transliterated tasks due to the
lack of explicit pretraining on such data [63].
Earlier studies evaluating LLMs, such as GPT-3.5 in zero-shot settings [24, 52], have highlighted limitations in reasoning,
explanation, and handling target community information, largely due to the linguistic complexities of code-mixed
text, including inconsistent grammar, transliteration, and mixed syntactic structures [45]. However, the emergence of
newer LLMs trained on more diverse datasets calls for a re-evaluation of their effectiveness in detecting code-mixed
and transliterated hate speech. In this paper, we bridge this gap.
Finally, going beyond finding hate speech, some researchers have also looked at ways to reduce its effect. One method
is known as counterspeech; this is where one responds to hate with nice or useful words, rather than remaining silent or
fighting back with more hate. Research indicates that effective counter-speech can prevent hate from spreading and
even transform the way individuals think [33]. People use different styles for this, such as sharing facts, being humorous,
being empathetic, or simply directly pointing out the problem. There is also some new research that attempts to employ
AI to automatically generate these responses [12]. This matters because detecting hate speech alone is insufficient; we
must also develop more effective and thoughtful ways to respond to it.
3
Datasets
In this paper, we use two popular hate speech datasets, both bringing different insights to the task of detecting hate
speech. Although these datasets offer useful insights, they are mostly geared towards monolingual environments. In
order to bridge this gap between multilingual and code-mixed hate speech detection, we curate an additional novel
dataset IndoHateMix that is specifically created towards such linguistic diversity. This section explains these datasets
and how they relate to our work.
3.1
HateXplainDataset
The HateXplaindataset [34] presents a benchmark to reduce bias and provide explainability in hate speech detection.
The annotations consist of three different tasks: (i) classification, categorizing a post in one of the following categories:
hate speech, offensive, or normal; (ii) hate target, the group being victimized by the post; and (iii) rationale, indicating
why certain text portions determine the classification. For our binary classification experiments, we focus only on
posts labeled as hate speech and normal, excluding offensive entries. We use 594 samples labeled as hate speech and
782 samples labeled as normal from the official test set. We include HateXplainin our study due to its focus on
explainability, which allows us to analyze how models interpret hate speech and assess biases in classification.

--- Page 5 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
Dataset
Total Samples
Hate Speech
Non-Hate
Avg. Length
HateXplain[34]
12375
5342 (43.17%)
7033 (56.83%)
23.5 words
ImplicitHate[21]
21480
8189 (38.12%)
13291 (61.9%)
16.81 words
IndoHateMix(Our Contribution)
11725
4457 (38.01%)
7268 (61.99%)
22.20 words
Table 1. Statistics of different datasets used in this study.
3.2
ImplicitHateDataset
The ImplicitHateDataset [21] is another corpus developed to identify and analyze hate speech, mainly focusing on
whether implicit and explicit terms relating to hateful messages are utilized. The dataset has 21, 480 tweets obtained from
prominent extremist groups in the United States, and each entry has been labeled meticulously as being implicit_hate,
explicit_hate, or not_hate. Beyond the level of categorization, the labels also capture the deeper intent or implied
meaning contained in the content. We restructured the dataset to make it a binary for the purpose of this study; we
labeled not_hate as 0 and implicit_hate and explicit_hate as 1. The transformation captures the difference between
hate and non-hate messages while making the task of classification relatively easier. After preprocessing, we split the
dataset into training and testing sets using an 80:20 ratio and ensuring that the original class distributions are preserved
through stratified sampling. This dataset is particularly relevant as it helps assess model performance in detecting
implicit hate speech, a more challenging and context-dependent form of toxicity often overlooked in traditional hate
speech detection models.
3.3
IndoHateMixDataset
The IndoHateMixdataset is a key contribution of this study, addressing critical gaps in existing hate speech resources
by capturing the cultural and situational nuances of Indian social media – dimensions often overlooked in other
datasets. A distinguishing feature of IndoHateMixis its focus on code-mixing and transliteration, both of which are
prevalent in India’s multilingual online communities. The linguistic complexity, informal tone, and strong context
dependence of such content pose significant challenges for automated detection systems. By incorporating these
real-world complexities, IndoHateMixaims to advance research in hate speech detection within linguistically diverse
and socially nuanced environments.
3.3.1
Dataset Source. The IndoHateMixdataset was curated from Koo [29], a microblogging platform that gained
immense popularity in India after it launched in March 2020. Branding itself as ‘India’s Twitter’, Koo accommodated
multiple Indian languages promoting regional communication. This makes Koo an indispensable tool for studying
hate speech because it gives deeper insight into the socio-political climate and cultural nuances within India. Our data
collection period was between December 2023 and January 2024.
3.3.2
Dataset Curation. We used a keyword-based search strategy to identify accounts likely to generate hate speech.
Keywords included terms such as Israel, Palestine, Ukraine, Hamas, Khalistan, Pakistan, Trudeau, China, Election,
and Protest, targeting both global and local socio-political contexts. This approach enabled the identification of initial
hate accounts, which were manually reviewed and categorized based on their activity levels. To expand the dataset,
we examined the followers of these accounts and iteratively conducted additional searches. Different data collection
strategies were employed for high-activity and low-activity accounts. For each account, a curated set of selected
posts, referred to as candidate Koos, was maintained. Specifically, for low-activity accounts, the most recent 300 posts
were selected and, in the case of high-activity accounts, 300 posts were chosen at regular intervals, with the spacing

--- Page 6 ---

Singh et al.
determined individually for each account based on its posting frequency. Since high-activity accounts often publish
similar Koos throughout the day, this approach ensured diversity in the dataset. To achieve this, 50% of the candidate
Koos were randomly selected for sampling, with posts extracted from one half and comments from the remaining Koos.
This process contributed to curating the raw dataset, which was then refined through preprocessing steps to enhance
data quality and relevance. These steps included removing URLs and emojis to reduce noise and bias, converting all text
to lowercase for uniformity, and filtering out duplicates or near-duplicates using cosine similarity. Additionally, hashtags
were retained but stripped of the ‘#’ symbol, and only posts containing between 5 and 55 words were considered to
maintain contextual and grammatical adequacy.
3.3.3
Annotation Process. Our dataset annotation process relied on manual (human) annotation by three expert
annotators, ensuring greater contextual accuracy than simple keyword-based identification. This approach enabled a
careful analysis of each post’s context and overall sentiment to determine whether it constituted hate speech or not.
For instance, in one example labeled as hate speech, the annotators identified the following post:
“a clever enemy is much better than a stupid friend. despite knowing fact, party leaders hug & felicitate
him."
Here, the use of terms like “enemy" and the context of criticizing political leaders indicated a negative sentiment
directed at a specific group, aligning with our definition of hate speech.
In contrast, an example labeled as non-hate speech reads:
“yes, they must condemn this dastardly act in a loud and clear voice."
This post employs assertive language but does not target any specific group or express hatred. The annotators
identified that it called for condemnation rather than inciting hostility, demonstrating the nuanced interpretation
required for accurate annotation.
The prevalence of code-mixed language, combining Hindi and English, posed a significant challenge. Negative
sentiment expressed in one language could be amplified by words in the other. For example, in one post marked as hate
speech, the user wrote:
The Hindi phrase in the above example mocks the physical appearance and age of a political figure. Meanwhile,
the English phrase links the person to a notorious criminal, reinforcing negative sentiment. This combination was
categorized as hate speech due to its body-shaming and defamatory intent.
Conversely, a non-hate speech example reads:
This post combines Hindi and English (“born intelligent”) in a light-hearted manner, joking about intelligence and not
holding cash bundles. It was classified as non-hate speech because it lacked any malicious or harmful intent. Through

--- Page 7 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
this systematic approach, we navigated the linguistic complexities of Indian social media and accurately identified hate
speech while maintaining cultural sensitivity. This process resulted in a high-quality dataset labeled with a binary
scheme: 1 for hate speech and 0 for non-hate speech. The dataset comprises a total of 11, 725 samples, with 4, 457
samples (38.01%) labeled as hate and 7, 268 (61.99%) categorized as non-hate.
To assess the reliability of our annotations and ensure the overall quality of the dataset, we computed inter-annotator
agreement using the metric Fleiss’ Kappa [22]. We observed substantial agreement among annotators, with a Fleiss’
Kappa of 0.685. Following individual annotations, the annotators collaboratively reviewed ambiguous cases, reaching a
consensus to ensure consistency and uniform application of standards across the dataset.
Dataset statistics: Table 1 summarizes the number of samples, class distribution, and other relevant characteristics
across different datasets, revealing the diversity of data sources and the representation of hate and non-hate instances.
3.4
Targets of Hate
Knowing who is targeted in hate speech allows us to understand the underlying social tensions and biases. Each of the
datasets – IndoHateMix, HateXplain, and ImplicitHate– allows us to gain insight into the different types of groups
or targets that are attacked most frequently.1
In the IndoHateMix dataset, hate speech incorporates religious as well as political targeting, demonstrating how
individuals exhibit hostility not only against communities but also against individual leaders. Religious communities
such as Hindus , Muslims , and Sikhs are repeatedly named with hateful or violent language. For instance, Muslims
are sometimes stereotyped as naturally aggressive or untrustworthy, and Sikhs are blamed for following separatist
philosophies. These kinds of generalizations spread harmful stereotypes and deepen communal divides. At the same
time, political hate is directed at leaders like Rahul Gandhi , Arvind Kejriwal , and Narendra Modi , all top leaders
of major political parties in India. Unlike religious hate, these attacks focus on individuals and often reflect anger about
governance, corruption, or other national issues. The tone is less about identity and more about disappointment or
distrust toward these figures. This mix of religious and political hate is what makes IndoHateMixunique. It reflects
the actual nature of online hate in India, almost always written in code-mixed script (such as, Hindi-English), and can
help us to develop systems that can address these types of nuanced local representations of hate. It illustrates that hate
speech in India is as much about blaming individuals in authority as it is about targeting religious or caste groups.
In contrast, HateXplain data is primarily concentrated on religious communities, particularly Muslims and
Jews . The tone used here is mostly straightforward and aggressive, based on old stereotypes. For instance, Muslims
are mentioned as violent or threatening, with Jews being blamed for exercising global power to serve hidden agendas.
Very occasionally, Pakistanis are targeted as well, typically merging religious and national identity into a single
category. What is striking in HateXplainis the way hate is generalized: it does not target individuals, which is very
often seen in IndoHateMix, but rather holds entire communities accountable.
The ImplicitHate dataset looks at a different kind of hate – one that is more hidden and suggestive. It tends
to be directed towards racial and ethnic groups such as African Americans , Mexicans , and Muslims , but subtly
so. Rather than employing insults, it employs negative stereotypes – for example, that people with African heritage
only manage to succeed in Western nations, or that Mexicans are uneducated. These remarks are less vitriolic on the
surface but still propagate deleterious ideas.
1Note that in the analysis, red is used to highlight religious communities (e.g., Hindus, Muslims, Jews), orange for racial or ethnic groups (e.g., African
Americans, Mexicans), and green for commonly targeted political figures.

--- Page 8 ---

Singh et al.
These patterns in hate targets across different datasets are not just interesting facts – they help us understand
something deeper. By looking at who is being attacked in each dataset, we can see the social and political tensions
behind the hate. Each dataset shows a different kind of hate: IndoHateMix highlights direct political attacks,
HateXplain shows strong hate against religious and ethnic groups, and ImplicitHate reveals more hidden and
subtle forms of bias. This tells us that hate detection models shouldn’t treat all data the same. Each dataset brings its
own style and focus, so models must be trained and tested with these differences in mind. By comparing them this way,
we can build better systems that handle hate more fairly and effectively.
4
Experimental Evaluation
As mentioned in the introduction, the primary goal of this paper is to benchmark the performance of various hate speech
detection models. We attempt to cover large language models (LLMs) as well as traditional transformer models, such as
BERT-based models, and custom APIs to determine which approach is more effective in detecting hate speech. Our
analysis also includes analyzing how these models perform on various datasets, such as IndoHateMix, HateXplain,
and ImplicitHate. To simulate real-world low-resource scenarios, we also conduct transfer learning experiments by
fine-tuning models on limited subsets of data. Finally, we investigate the limitations of these models, particularly their
handling of different cases of hate speech, through detailed error analysis.
4.1
Models Selected for Benchmarking
To ensure a comprehensive analysis, we benchmark a diverse range of models, which can be categorized into three
groups: Multilingual BERT-based Models, Hate Speech Detection APIs, and Large Language Models.
4.1.1
Multilingual BERT-based Models. We explore a group of prominent multilingual transformer-based models that
have been pre-trained on multiple languages, including English and Hindi. Specifically, we evaluate the following
models:
• mBERT: A multilingual BERT model proposed by Devlin et al. [19].
• XLM-RoBERTa: An extended multilingual RoBERTa model intoduced by Conneau et al. [13].
4.1.2
Hate Speech Detection APIs. They offer off-the-shelf tools to identify harmful or offensive content without
requiring any model training on the receiver’s end. In our work, we use Google’s Perspective API [23], which returns
six separate scores: TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK, INSULT, PROFANITY, and THREAT2. Because the
API does not provide a single “hate" score, we take the maximum of these six values as a proxy and classify content as
hate speech whenever that maximum exceeds an arbitrary threshold of 0.5.
4.1.3
Large Language Models (LLMs). Lastly, we explore a diverse set of state-of-the-art LLMs:
• Mistral-7B [4, 27]: An open-source, multilingual, efficient model featuring Sliding Window Attention for fast
inference.
• LLaMA3.1-8B [1, 3]: An advanced open-source, long-context, multilingual model, with enhanced reasoning and
safety via RLHF [41].
• InternLM2.5-7B [7, 26]: An efficiently trained, long-context, multilingual open-source LLM, with strong
multilingual capabilities and enhanced safety alignment.
2These are the evaluation categories provided by the Perspective API [23].

--- Page 9 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
• Qwen2.5-7B [47]: A versatile open-source model designed for long context windows and robust multilingual
performance.
• GPT-4o-mini [39]: A proprietary, highly optimized variant of GPT-4o [40], demonstrating enhanced reasoning
performance and equipped with integrated safety mitigations.
Note. All evaluated LLMs are open-source, with fully transparent architectures, known parameter counts, and the
ability to be fine-tuned for our specific classification task, except for the proprietary GPT-4o-mini. Because it cannot
be fine-tuned, we apply GPT-4o-mini zero-shot via the OpenAI API [39] using the same classification prompt as used
for fine-tuning the open-source LLMs.
4.2
Experimental Setup
We conducted all experiments on a single A100 40GB GPU. To optimize the efficiency of LLM-related experiments,
we utilize the llama-factory [65] framework. For HateXplain, we have retained the originally defined train-test-
validation set; for ImplicitHate and IndoHateMix datasets, we adopt a 70-20-10 train-test-validation split.
Prompt Template and Configuration: In contrast to some prior studies [24, 52], we do not rely on complex prompt
engineering techniques, such as Chain-of-Thought (CoT) reasoning [60] or explicitly specifying target categories
within the prompt [52], and instead we use a simple and direct prompting approach for LLMs. It is worth noting that
different prompt engineering techniques can further boost LLM performance, and our findings establish a conservative
baseline for LLM performance, and if it can outperform traditional models, further prompt engineering or tuning
will only reinforce the assertion. In this study, all experiments utilize a consistent classification prompt and identical
hyperparameter settings within each model family. Details are provided below:
• BERT Fine-Tuning (mBERT & XLM-RoBERTa):
– Learning rate: 2𝑒−5
– Batch size: 2
– Optimizer: AdamW (weight decay = 0.01)
– Max sequence length: 128
– Epochs: 3
• Perspective API: For each input, scores are computed for six categories: TOXICITY, SEVERE_TOXICITY, IDENTITY_ATTACK,
INSULT, PROFANITY, and THREAT. An input is labeled ‘Hate’ if the maximum among all the above scores is greater
than the threshold of 0.5.
• LLMs (Mistral-7B, LLaMA3.1-8B, InternLM2.5-7B, Qwen2.5-7B, GPT-4o-mini):
– Prompt Template: The following prompt was used across all LLM models:
Hate Speech Classification Prompt
Instruction: “Review the provided statement and classify it as ‘Hate’ or ‘Non-Hate.’ Return ‘1’ for Hate
and ‘0’ for Non-Hate.”
Input: “{statement}”
Output: “{label}”
– Training and Testing Configuration:

--- Page 10 ---

Singh et al.
Model Type
Model Name
Evaluation Metrics
Accuracy
Precision
Recall
F1-Score
HateXplain
Multilingual BERT-based Models
mBERT [19]
0.87
0.87
0.87
0.87
XLM-RoBERTa [13]
0.86
0.86
0.86
0.86
Hate Speech Detection APIs
Perspective [23]
0.66
0.68
0.68
0.66
Large Language Models
LLaMA3.1-8B [3]
0.91
0.91
0.91
0.91
Mistral-7B [4]
0.91
0.91
0.90
0.90
Qwen2.5-7B [47]
0.90
0.90
0.90
0.90
InternLM2.5-7B [26]
0.89
0.90
0.88
0.89
GPT-4o-mini [39]
0.72
0.79
0.75
0.72
ImplicitHate
Multilingual BERT-based Models
mBERT [19]
0.76
0.76
0.76
0.76
XLM-RoBERTa [13]
0.65
0.65
0.65
0.65
Hate Speech Detection APIs
Perspective [23]
0.69
0.67
0.64
0.64
Large Language Models
LLaMA3.1-8B [3]
0.82
0.82
0.81
0.81
Mistral-7B [4]
0.82
0.81
0.81
0.81
Qwen2.5-7B [47]
0.82
0.81
0.80
0.80
InternLM2.5-7B [26]
0.81
0.81
0.79
0.80
GPT-4o-mini [39]
0.70
0.70
0.71
0.70
IndoHateMix
Multilingual BERT-based Models
mBERT [19]
0.73
0.78
0.77
0.77
XLM-RoBERTa [13]
0.74
0.74
0.74
0.33
Hate Speech Detection APIs
Perspective [23]
0.70
0.79
0.61
0.59
Large Language Models
LLaMA3.1-8B [3]
0.83
0.82
0.81
0.82
Mistral-7B [4]
0.81
0.81
0.79
0.80
InternLM2.5-7B [26]
0.82
0.81
0.79
0.80
Qwen2.5-7B [47]
0.81
0.81
0.78
0.79
GPT-4o-mini [39]
0.76
0.76
0.71
0.72
Table 2. Performance comparison of various hate speech detection models on HateXplain, ImplicitHate, and IndoHateMix datasets.
The best results are highlighted in green while the worst are in red . Across all three datasets, LLMs have maintained superior
performances.
∗Learning Rate: 5𝑒-5
∗Batch Size: 1
∗Epochs: 3
∗Optimizer: AdamW
∗LoRA Rank: 8
∗LoRA Alpha: 16
∗Temperature: 0.1
∗Top-p: 0.95
∗Max input length: 1024 tokens
∗Max output length: 256 tokens
∗Gradient accumulation steps: 1
4.3
Benchmarking Results
Next, we present the benchmarking performance of various models on the HateXplain, ImplicitHate, and Indo-
HateMix datasets, evaluated across accuracy, precision, recall, and F1-score. The results from benchmarking on these
datasets is summarized in Table 2. As we can observe from the table, across all datasets, LLaMA3.1-8B consistently
delivers the highest performance, showcasing its superior ability to generalize in diverse hate speech detection settings.
Specifically, it outperforms the BERT-based models by nearly 4%, 8%, and 14% in terms of accuracy on the HateXplain,

--- Page 11 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
ImplicitHate, and IndoHateMix datasets, respectively. Other LLMs – InternLM2.5-7B and Mistral-7B – follow
closely behind, significantly outperforming multilingual BERT-based models and the popular hate speech detection
API (Perspective) across all datasets. Interestingly, open-source LLMs – LLaMA3.1-8B, Mistral-7B, InternLM-2.5-7B,
Qwen2.5-7B – outperform the proprietary GPT-4o-mini model in the hate speech detection task. We emphasize that,
in this comparison, GPT-4o-mini is not fine-tuned as its exact size and training details are undisclosed, which makes
direct comparison tricky – any gap may reflect the differences in scale or pretraining rather than model quality. Even if
it matched or beat our open-source LLMs with fine-tuning [35], it would only reinforce our claim that modern LLMs,
when properly adapted, outperform traditional approaches, while open models still offer the benefits of transparency
and customization.
4.4
Transfer Learning and Limited Data Experiments
To evaluate the transfer learning capabilities of the state-of-the-art models for the hate speech detection task, we
compare the best-performing LLM LLaMA3.1-8B, against the top BERT-based model mBERT, as identified in our earlier
benchmarking experiments 2. Fig. 1 summarizes the results of these transfer learning experiments, where models
fine-tuned on one dataset are evaluated across all datasets. The rows indicate the datasets used for fine-tuning the
corresponding model, while the columns represent the test datasets. Across all configurations, LLaMA3.1-8B consistently
outperforms mBERT. For instance, when trained on the HateXplain dataset and tested on all three datasets, the relative
gain in accuracy of LLaMA3.1-8B over mBERT, averaged across the three test sets is a staggering 12.15%. This stark
performance gap highlights LLaMA3.1-8B’s remarkable ability to generalize across diverse linguistic and cultural
contexts, even when trained on limited domain-specific data.
These findings are particularly significant for real-world applications, where labeled data for niche challenges
like code-mixing and transliteration is scarce. Unlike mBERT, which struggles to adapt to unseen linguistic patterns,
LLaMA3.1-8B leverages its pretrained multilingual world knowledge to infer context and intent, even in low-resource
settings. This adaptability makes LLaMA3.1-8B a powerful tool for combating hate speech in linguistically diverse
regions, where traditional models often fall short.
Further extending the transfer learning experiment, Fig. 2 presents model performance in a limited data setting,
where only a random 10% (sampled without replacement) subset of the available data is used for fine-tuning3. Despite
the limited data, LLaMA3.1-8B consistently outperforms mBERT across all datasets, demonstrating its robustness even in
data-constrained environments.
Remarkably, even when fine-tuned on just 10% of the data using a rank-8 LoRA adapter that adds only about 4
million trainable parameters [25] – far fewer than mBERT’s 179 million [18] – LLaMA3.1-8B still outperforms mBERT
fine-tuned on the full dataset (see Table 2), underscoring their efficiency and ability to generalize from minimal data.
This finding strengthens our position that enhancing LLMs through curated, diverse datasets may offer greater returns
than building task-specific models [6, 46].
4.5
Error Analysis
To gain a better insight into where the models are going wrong, we closely examined their mistakes. Of all the fine-tuned
transformer models we experimented with, mBERT and LLaMA3.1-8B and Perspective API performed the best in their
respective categories — with mBERT standing for conventional multilingual models and LLaMA3.1-8B standing for the
3Note that the results presented in Figure 2 are the average of 5 experimental runs to ensure robustness and to reduce variance in the evaluation metrics.

--- Page 12 ---

Singh et al.
(a) mBERT transfer learning (full data)
(b) LLaMA3.1-8B transfer learning (full data)
Fig. 1. Contrast heatmaps of cross-dataset transfer learning using full training data.
(a) mBERT transfer learning (10% data)
(b) LLaMA3.1-8B transfer learning (10% data)
Fig. 2. Contrast heatmaps of transfer learning with limited (10%) training data.
new large language models (LLMs). Therefore, we selected these three for a detailed comparison. Table 3 contains some
exemplary cases from the IndoHateMixdataset in which mBERT’s predictions deviate from those of LLaMA3.1-8B, with
the former being wrong. Some such cases include a diverse set of scenarios, including exclusive Hindi, Hindi-English
code-mixed posts, political satire, and informal conversational content.
From these examples, we observe clear differences in how the three models handle hate speech detection. mBERT
frequently fails to identify hate speech when it is expressed in short, informal, or indirect forms (Examples 1, 3, and
4). It also struggles with longer, code-mixed sentences, such as in Example 7, where hateful content is embedded
within political commentary. Furthermore, mBERT often misclassifies non-hateful content as hate speech and vice versa,
especially in the presence of sarcasm or emotionally charged language (Examples 5 and 6). These cases suggest that
mBERT is sensitive to surface-level cues like tone but often fails to grasp the deeper semantic intent.
In contrast, LLaMA3.1-8B demonstrates more robust performance. It successfully detects hate speech in challenging
scenarios that mBERT misses (Examples 1, 3, 4, and 7), and it avoids false positives in posts involving sarcasm or humor
(Examples 5 and 6). This indicates a stronger contextual and tonal understanding, allowing it to move beyond literal
interpretation toward more nuanced comprehension. Perspective API, while useful in straightforward cases, appears
more limited in scope. Like mBERT, it frequently fails to detect hate speech when the expression is indirect or code-mixed

--- Page 13 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
Fig. 3. Error analysis comparing mBERT, LLaMA3.1-8B, and Perspective API predictions on IndoHateMix examples.
between English and Hindi (Examples 1, 3, 4, and 7). It also misclassifies sarcastic language, as seen in Example 6. These
limitations highlight the API’s difficulty in processing the informal, multilingual, and often ambiguous language typical
of Indian social media platforms.
These misclassifications are significant, as they underscore the challenges of hate speech detection in linguistically
diverse and informal online environments. mBERT, in particular, exhibits a tendency to flag benign content – such as
political opinions or jokes—as hate speech, while missing actual harmful content. In contrast, LLMs like LLaMA3.1-8B
are more adaptable to the code-mixed and conversational tone of social media posts. Their flexibility allows them to
more accurately identify hate speech without overgeneralizing.

--- Page 14 ---

Singh et al.
Takeaway: Overall, our analyses in this section highlight the comparative advantage of large language models (LLMs)
in multilingual and informal contexts such as those found in India. These models generalize more effectively across
varied styles of writing and better handle the noisy, real-world language seen online. This suggests a promising direction
for future work: rather than developing multiple narrow, task-specific models, it may be more effective to invest in
powerful, general-purpose LLMs trained on diverse, culturally grounded datasets to combat online hate more reliably.
5
Conclusion
In this work, we examined whether recent advances in large language models, noted for their strong linguistic
competence and contextual understanding, can outperform traditional models that are and optimized for the critical
task of hate speech detection. To this end, we introduced IndoHateMix, a novel benchmark dataset specifically
curated to address the unique linguistic and cultural challenges of the Indian social media landscape. With two more
additional datasets, we conducted a comprehensive evaluation across a spectrum of models, ranging from widely used
transformer-based baselines such as mBERT, to state-of-the-art LLMs like LLaMA-3.1-8B. Our experiments consistently
showed that LLMs significantly outperform traditional models, even in low-resource scenarios where labeled data is
scarce. Specifically, LLaMA-3.1-8B demonstrated superior ability to generalize across languages, detect indirect and
sarcastic expressions of hate, and accurately interpret contextually rich or ambiguous posts – areas where BERT based
models showed considerable weaknesses.
These findings underscore the transformative potential of LLMs in improving hate speech detection systems. Their
adaptability to handle informal, multilingual content position them as a promising direction for future work in this
space. Rather than relying on specialized dataset-specific solutions, our results suggest that leveraging general-purpose
LLMs, especially when fine-tuned with culturally and linguistically diverse datasets like IndoHateMix, can lead to
more reliable and context-sensitive hate speech detection frameworks.
5.1
Limitations and Future Work
While our study demonstrates superior performance of LLMs for hate speech detection, it is important to acknowledge
several limitations that could influence the scope and robustness of our findings, along with possible directions for
future work.
Dataset Specificity and Scope: Our evaluation is conducted on three datasets: HateXplain, ImplicitHate, and our
newly introduced IndoHateMix. While these datasets offer diverse challenges, including implicit hate speech and
code-mixing, they may not fully represent the entire spectrum of online hate speech. Specifically, IndoHateMixis
curated from the Koo platform, focusing on Hindi-English code-mixed data which reflects the socio-political context
of India. Since different platforms are known to have intrinsic biases [9, 10], one could expand the study to include
multilingual and multimodal datasets from different platforms to evaluate generalizability across broader contexts.
Linguistic and Cultural Context: The complexities of code-mixed languages, such as Hinglish, introduce challenges
due to informal syntax, variable grammar, and transliteration. Although LLMs show improved adaptability, the models’
understanding is still developing, especially concerning nuanced cultural references and implicit meanings. The
annotation process, while thorough, relies on human annotators, introducing potential biases despite efforts to ensure
consistency and mitigate bias. Further exploration can be done in the direction of culturally grounded embeddings or
fine-tuning approaches that better capture regional sociolinguistic cues.
Model Biases: Our analysis seeks to mitigate biases by using explainable datasets like HateXplainto understand how
models detect hate speech. However, bias can take different forms, and our study primarily focuses on classification

--- Page 15 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
accuracy and generalization across linguistic variations. A more comprehensive bias analysis involving demographic,
gender, or socio-economic factors remains a promising avenue for future work.
Prompting and Fine-Tuning: To ensure a fair comparison between traditional models and LLMs, we adopted a
straightforward prompting strategy, deliberately avoiding advanced methods like Chain-of-Thought (CoT) reasoning.
While CoT has been shown to significantly improve LLM performance on complex reasoning tasks [60], our aim was to
evaluate the inherent capabilities of LLMs with minimal task-specific tuning. Additionally, we did not explore recent
advances in reasoning-driven interpretability techniques, which could identify hate speech targets and contribute to
more robust and interpretable detection systems. Incorporating such techniques could be an important step for future
work focused on robust and explainable hate speech detection.
Computational Resources and Model Size: Our experiments were conducted on a single A100 40GB GPU, which may
limit the scalability and exploration of larger models or more extensive hyperparameter tuning. While we benchmarked
several state-of-the-art LLMs, including LLaMA3.1-8B and GPT-4o-mini, the rapidly evolving landscape of LLMs
means that newer models with different architectures and training data may yield different results. Future work could
investigate more efficient yet accurate hate speech classification using quantized versions of larger language models.
Generalization to Low-Resource Languages: Although our study includes code-mixed data, the primary languages
are Hindi and English. The effectiveness of LLMs in detecting hate speech in other low-resource languages or language
combinations may vary due to differences in linguistic structures, available data, and cultural contexts. Exploring
adaptation techniques and cross-lingual transfer learning for other underrepresented language pairs presents a valuable
future direction.
Ethical Considerations: Studying hate speech inherently involves dealing with offensive content. While we have taken
precautions to minimize exposure and ensure responsible research practices, the potential for unintended consequences,
such as reinforcing harmful stereotypes, remains a concern.
Finally, this work highlights the need to solve hate speech detection through the lens of general-purpose large language
models. As we continue to confront the toxic online discourse, such models offer a scalable and inclusive path forward,
and we hope that this work can act as a torchbearer towards that road.
References
[1] Dubey Abhimanyu et al. 2024. The Llama 3 Herd of Models. arXiv:2407.21783
[2] Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam
Altman, Shyamal Anadkat, et al. 2023. Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023).
[3] Meta AI. 2023. Llama 3.1 8B: A Language Model. https://huggingface.co/meta-llama/Llama-3.1-8B Accessed: 2024-10-13.
[4] Mistral AI. 2023. Mistral 7B v0.3: An Open Weight Language Model. https://huggingface.co/mistralai/Mistral-7B-v0.3
[5] Aditya Bohra, Deepanshu Vijay, Vinay Singh, Syed Sarfaraz Akhtar, and Manish Shrivastava. 2018. A dataset of Hindi-English code-mixed social
media text for hate speech detection. In Proceedings of the second workshop on computational modeling of people’s opinions, personality, and emotions
in social media. 36–41.
[6] Martin Juan José Bucher and Marco Martini. 2024. Fine-Tuned ’Small’ LLMs (Still) Significantly Outperform Zero-Shot Generative AI Models in
Text Classification. arXiv preprint arXiv:2406.08660 (2024). https://arxiv.org/abs/2406.08660
[7] Zheng Cai. 2024. InternLM2 Technical Report. arXiv:2403.17297 [cs.CL] https://arxiv.org/abs/2403.17297
[8] Tommaso Caselli, Valerio Basile, Jelena Mitrović, and Michael Granitzer. 2020. Hatebert: Retraining bert for abusive language detection in english.
arXiv preprint arXiv:2010.12472 (2020).
[9] Abhijnan Chakraborty, Saptarshi Ghosh, Niloy Ganguly, and Krishna P Gummadi. 2016. Dissemination biases of social media channels: On the
topical coverage of socially shared news. In Proceedings of the International AAAI Conference on Web and Social Media, Vol. 10. 559–562.
[10] Abhijnan Chakraborty, Johnnatan Messias, Fabricio Benevenuto, Saptarshi Ghosh, Niloy Ganguly, and Krishna Gummadi. 2017. Who makes trends?
understanding demographic biases in crowdsourced recommendations. In Proceedings of the International AAAI Conference on Web and Social Media,
Vol. 11. 22–31.

--- Page 16 ---

Singh et al.
[11] Abhishek Chopra, Deepak Kumar Sharma, Aashna Jha, and Uttam Ghosh. 2023. A framework for online hate speech detection on code-mixed
Hindi-English text and Hindi text in Devanagari. ACM Transactions on Asian and Low-Resource Language Information Processing 22, 5 (2023), 1–21.
[12] Yi-Ling Chung, Elizaveta Kuzmenko, Serra Sinem Tekiroglu, and Marco Guerini. 2019. CONAN–COunter NArratives through Nichesourcing: a
multilingual dataset of responses to fight online hate speech. arXiv preprint arXiv:1910.03270 (2019).
[13] Alexis Conneau, Kartikay Khandelwal, Naman Goyal, Vishrav Chaudhary, Guillaume Wenzek, Francisco Guzmán, Edouard Grave, Myle Ott, Luke
Zettlemoyer, and Veselin Stoyanov. 2020. Unsupervised Cross-lingual Representation Learning at Scale. In Proceedings of the 58th Annual Meeting of
the Association for Computational Linguistics. 8440–8451.
[14] Mithun Das, Saurabh Kumar Pandey, and Animesh Mukherjee. 2023. Evaluating ChatGPT’s performance for multilingual and emoji-based hate
speech detection. arXiv preprint arXiv:2305.13276 (2023).
[15] Mithun Das, Punyajoy Saha, Binny Mathew, and Animesh Mukherjee. 2022. Hatecheckhin: Evaluating hindi hate speech detection models. arXiv
preprint arXiv:2205.00328 (2022).
[16] Thomas Davidson, Dana Warmsley, Michael Macy, and Ingmar Weber. 2017. Automated hate speech detection and the problem of offensive
language. In Proceedings of the international AAAI conference on web and social media, Vol. 11. 512–515.
[17] Ona De Gibert, Naiara Perez, Aitor García-Pablos, and Montse Cuadros. 2018. Hate speech dataset from a white supremacy forum. arXiv preprint
arXiv:1809.04444 (2018).
[18] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018. BERT: Pre-training of Deep Bidirectional Transformers for Language
Understanding. arXiv:1810.04805 [cs.CL] https://huggingface.co/google-bert/bert-base-multilingual-cased
[19] Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2019. BERT: Pre-training of Deep Bidirectional Transformers for Language
Understanding. In Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language
Technologies, Volume 1 (Long and Short Papers). 4171–4186.
[20] Suman Dowlagar and Radhika Mamidi. 2022. Hate speech detection on code-mixed dataset using a fusion of custom and pre-trained models with
profanity vector augmentation. SN Computer Science 3, 4 (2022), 306.
[21] Mai ElSherief, Caleb Ziems, David Muchlinski, Vaishnavi Anupindi, Jordyn Seybolt, Munmun De Choudhury, and Diyi Yang. 2021. Latent hatred: A
benchmark for understanding implicit hate speech. arXiv preprint arXiv:2109.05322 (2021).
[22] Rosa Falotico and Piero Quatto. 2015. Fleiss’ kappa statistic without paradoxes. Quality & Quantity 49 (2015), 463–470.
[23] Google Jigsaw. [n. d.]. Perspective API. https://perspectiveapi.com/. Accessed: 2024-09-20.
[24] Keyan Guo, Alexander Hu, Jaden Mu, Ziheng Shi, Ziming Zhao, Nishant Vishwamitra, and Hongxin Hu. 2023. An investigation of large language
models for real-world hate speech detection. In 2023 International Conference on Machine Learning and Applications (ICMLA). IEEE, 1568–1573.
[25] Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. 2021. LoRA: Low-Rank
Adaptation of Large Language Models. arXiv preprint arXiv:2106.09685 (2021). https://arxiv.org/abs/2106.09685 Submitted June 17 2021; revised
October 16 2021.
[26] InternLM. 2023. InternLM 2.5 7B: A Language Model. https://huggingface.co/internlm/internlm2_5-7b Accessed: 2024-10-13.
[27] Albert Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford, Devendra Singh Chaplot, Diego de las Casas, Florian Bressand, Gianna
Lengyel, Guillaume Lample, Lucile Saulnier, Lélio Renard Lavaud, Marie-Anne Lachaux, Pierre Stock, Teven Le Scao, Thibaut Lavril, Thomas Wang,
Timothée Lacroix, and William El Sayed. 2023. Mistral 7B. arXiv:2310.06825 [cs.CL] https://arxiv.org/abs/2310.06825
[28] Nahid Afrose Kabir. 2020. Identity politics in India: Gujarat and Delhi riots. Journal of Muslim Minority Affairs 40, 3 (2020), 395–409.
[29] Koo. 2024. Koo: A Multilingual Microblogging Platform. https://www.kooapp.com/ Accessed: 2024-10-13.
[30] Lingyao Li, Lizhou Fan, Shubham Atreja, and Libby Hemphill. 2024. “HOT” ChatGPT: The promise of ChatGPT in detecting and discriminating
hateful, offensive, and toxic comments on social media. ACM Transactions on the Web 18, 2 (2024), 1–36.
[31] Rijul Magu and Jiebo Luo. 2018. Determining code words in euphemistic hate speech using word embedding networks. In Proceedings of the 2nd
workshop on abusive language online (ALW2). 93–100.
[32] Binny Mathew, Ritam Dutt, Pawan Goyal, and Animesh Mukherjee. 2019. Spread of hate speech in online social media. In Proceedings of the 10th
ACM conference on web science. 173–182.
[33] Binny Mathew, Punyajoy Saha, Hardik Tharad, Subham Rajgaria, Prajwal Singhania, Suman Kalyan Maity, Pawan Goyal, and Animesh Mukherjee.
2019. Thou shalt not hate: Countering online hate speech. In Proceedings of the international AAAI conference on web and social media, Vol. 13.
369–380.
[34] Binny Mathew, Punyajoy Saha, Seid Muhie Yimam, Chris Biemann, Pawan Goyal, and Animesh Mukherjee. 2021. Hatexplain: A benchmark dataset
for explainable hate speech detection. In Proceedings of the AAAI conference on artificial intelligence, Vol. 35. 14867–14875.
[35] Microsoft Azure OpenAI Service. 2025. Azure OpenAI GPT-4o-mini fine-tuning tutorial. https://learn.microsoft.com/en-us/azure/ai-services/openai/
tutorials/fine-tune?tabs=command-line Accessed: 2025-04-30.
[36] Paul Mozur. 2018. A Genocide Incited on Facebook, With Posts From Myanmar’s Military. The New York Times (2018). https://www.nytimes.com/
2018/10/15/technology/myanmar-facebook-genocide.html
[37] Karsten Müller and Carlo Schwarz. 2021. Fanning the flames of hate: Social media and hate crime. Journal of the European Economic Association 19,
4 (2021), 2131–2167.
[38] Mumo Nzau. 2023. Confronting terrorism and violent extremism in Eastern Africa. In State politics and public policy in Eastern Africa: A comparative
perspective. Springer, 137–156.

--- Page 17 ---

Rethinking Hate Speech Detection on Social Media: Can LLMs Replace Traditional Models?
[39] OpenAI. 2024. GPT-4o Mini: Advancing Cost-Efficient Intelligence. https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
Accessed: 2024-10-13.
[40] OpenAI. 2024. GPT-4o System Card. arXiv:2410.21276
[41] Long Ouyang, Jeffrey Wu, Xu Jiang, Diogo Almeida, Carroll Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex
Ray, et al. 2022. Training language models to follow instructions with human feedback. Advances in neural information processing systems 35 (2022),
27730–27744.
[42] Jinlong Pang, Na Di, Zhaowei Zhu, Jiaheng Wei, Hao Cheng, Chen Qian, and Yang Liu. 2025. Token Cleaning: Fine-Grained Data Selection for LLM
Supervised Fine-Tuning. arXiv:2502.01968 [cs.CL] https://arxiv.org/abs/2502.01968
[43] John Pavlopoulos, Leo Laugier, Alexandros Xenos, Jeffrey Sorensen, and Ion Androutsopoulos. 2022. From the detection of toxic spans in online
discussions to the analysis of toxic-to-civil transfer. In Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers). 3721–3734.
[44] Flor Miriam Plaza-del Arco, Debora Nozza, Dirk Hovy, et al. 2023. Respectful or toxic? using zero-shot learning with language models to detect hate
speech. In The 7th Workshop on Online Abuse and Harms (WOAH). Association for Computational Linguistics.
[45] Ruba Priyadharshini, Bharathi Raja Chakravarthi, Mani Vegupatti, and John P McCrae. 2020. Named entity recognition for code-mixed Indian
corpus using meta embedding. In 2020 6th international conference on advanced computing and communication systems (ICACCS). IEEE, 68–72.
[46] Xiao Pu, Mingqi Gao, and Xiaojun Wan. 2023. Summarization is (Almost) Dead. arXiv preprint arXiv:2309.09558 (2023). https://arxiv.org/abs/2309.
09558
[47] Qwen. 2023. Qwen 2.5 7B: A Language Model. https://huggingface.co/Qwen/Qwen2.5-7B Accessed: 2024-10-13.
[48] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J Liu. 2020. Exploring the
limits of transfer learning with a unified text-to-text transformer. Journal of machine learning research 21, 140 (2020), 1–67.
[49] Md Nishat Raihan, Umma Hani Tanmoy, Anika Binte Islam, Kai North, Tharindu Ranasinghe, Antonios Anastasopoulos, and Marcos Zampieri. 2023.
Offensive language identification in transliterated and code-mixed bangla. arXiv preprint arXiv:2311.15023 (2023).
[50] Benson Rajan and Shreya Venkatraman. 2021. Insta-hate: An exploration of Islamophobia and right-wing nationalism on Instagram amidst the
COVID-19 pandemic in India. Journal of Arab & Muslim Media Research 14, 1 (2021), 71–91.
[51] Daniel Rothbart and David M Stebbins. 2023. The proud boys raging righteously at the US capitol on January 6, 2021: A hate group in action. Peace
and Conflict: Journal of Peace Psychology 29, 4 (2023), 426.
[52] Sarthak Roy, Ashish Harshavardhan, Animesh Mukherjee, and Punyajoy Saha. 2023. Probing LLMs for hate speech detection: strengths and
vulnerabilities. arXiv preprint arXiv:2310.12860 (2023).
[53] Anna Schmidt and Michael Wiegand. 2017. A survey on hate speech detection using natural language processing. In Proceedings of the fifth
international workshop on natural language processing for social media. 1–10.
[54] Leandro Silva, Manish Mondal, Debora Correa, Fabrício Benevenuto, and Ingmar Weber. 2016. Analyzing the Targets of Hate in Online Social
Media. Proceedings of ICWSM (2016).
[55] Daily Star. 2024. Stop spread of hate speech. https://www.thedailystar.net/news/hate-crime/news/stop-spread-hate-speech-3714341
[56] Alexandra Stevenson. 2018. Facebook admits it was used to incite violence in Myanmar. The New York Times 6 (2018).
[57] Zeerak Talat and Dirk Hovy. 2016. Hateful symbols or hateful people? predictive features for hate speech detection on twitter. In Proceedings of the
NAACL student research workshop. 88–93.
[58] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric
Hambro, Faisal Azhar, et al. 2023. Llama: Open and efficient foundation language models. arXiv preprint arXiv:2302.13971 (2023).
[59] William Warner and Julia Hirschberg. 2012. Detecting hate speech on the world wide web. In Proceedings of the second workshop on language in
social media. 19–26.
[60] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. 2022. Chain-of-thought prompting
elicits reasoning in large language models. Advances in neural information processing systems 35 (2022), 24824–24837.
[61] Anjali Yadav, Tanya Garg, Matej Klemen, Matej Ulcar, Basant Agarwal, and Marko Robnik Sikonja. 2024. Code-mixed Sentiment and Hate-speech
Prediction. arXiv preprint arXiv:2405.12929 (2024).
[62] Marcos Zampieri, Shervin Malmasi, Preslav Nakov, Sara Rosenthal, Noura Farra, and Ritesh Kumar. 2019. Predicting the type and target of offensive
posts in social media. arXiv preprint arXiv:1902.09666 (2019).
[63] Ruochen Zhang, Samuel Cahyawijaya, Jan Christian Blaise Cruz, Genta Indra Winata, and Alham Fikri Aji. 2023. Multilingual large language
models are not (yet) code-switchers. arXiv preprint arXiv:2305.14235 (2023).
[64] Ziqi Zhang and Lei Luo. 2019. Hate speech detection: A solved problem? the challenging case of long tail on twitter. Semantic Web 10, 5 (2019),
925–945.
[65] Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo, Zhangchi Feng, and Yongqiang Ma. 2024. LlamaFactory: Unified Efficient
Fine-Tuning of 100+ Language Models. arXiv:2403.13372 [cs.CL] https://arxiv.org/abs/2403.13372

```
