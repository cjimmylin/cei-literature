---








































Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: WY4ZPF3K
type: document
short_title: ToxicChat
year: 2023
first_author: "[[Zi Lin]]"
last_author: "[[Shang, Jingbo]]"
authors: "Lin, Zi; Wang, Zihan; Tong, Yongqi; Wang, Yangkun; Guo, Yuxin; Wang, Yujia; Shang, Jingbo"
url: "https://aclanthology.org/2023.findings-emnlp.311/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/QG932ES4/2023 - ToxicChat Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversations.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
rv_islam: 0
rv_christianity: 0
rv_buddhism: 0
rv_judaism: 0
rv_hinduism: 0
rv_sikhism: 0
rv_confucianism: 0
rv_taoism: 0
rv_shinto: 0
rv_jainism: 0
rv_bahai: 0
rv_zoroastrianism: 0
rv_ubuntu: 0
rv_indigenous: 0
religious_values_list: "N/A"
mp_mft: 0
mp_schwartz: 0
mp_trolley: 0
mp_kohlberg: 0
mp_dual_process: 0
mp_intuitionist: 0
mp_dyadic: 0
mp_identity: 0
moral_psychology: "N/A"
newtags: "Toxicity & Hate Speech"
key_contribution: "Released ToxicChat, a benchmark of real-world user-AI conversations that exhibit nuanced toxicity, distinct from the social media data typically used to train toxicity detectors."
significance: "Reveals that models trained on standard social media data fail to detect the subtle, interaction-based toxicity found in real user-AI chats, highlighting a critical domain gap in safety evaluation."
tags: 
abstract: "Despite remarkable advances that large language models have achieved in chatbots, maintaining a non-toxic user-AI interactive environment has become increasingly critical nowadays. However, previous efforts in toxicity detection have been mostly based on benchmarks derived from social media content, leaving the unique challenges inherent to real-world user-AI interactions insufficiently explored. In this work, we introduce TOXICCHAT, a novel benchmark based on real user queries from an..."
CONF-CC: "N/A"
DATE_ADDED: 20260208
LLM_assessed: "RoBERTa"
DATA_URL: "https://huggingface.co/datasets/lmsys/toxic-chat"
pdf_extract: "PDF Extracts/2023/2023-Lin-ToxicChat.md"
local_pdf: "[[Lit-WS-Lit-WS-PDFs/2023/2023-Lin-ToxicChat.pdf]]"
CONFERENCE: "EMNLP 2023"
ethics_overall: 100
virtue_ethics: 0
deontological_ethics: 0
utilitarian_ethics: 0
contractarian_ethics: 0
care_ethics: 0
ethics_perspective: "Toxicity & Hate Speech"
nw_confucian: 0
nw_ubuntu: 0
nw_islamic_ethics: 0
nw_buddhist: 0
nw_dharmic: 0
nw_indigenous_relational: 0
nw_buen_vivir: 0
author_country: "US"
author_region: "North America"
author_global_north_south: "Global North"
weird_score: 78
is_benchmark: "Yes"
is_eval: "Yes"
is_dataset: "Yes"
data_description: "Benchmark dataset for toxicity detection"
data_metrics: "Not specified"
---
# ToxicChat: Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversations

## Authors

[[Zi Lin|Lin, Zi]], [[Zihan Wang|Wang, Zihan]], [[Yongqi Tong|Tong, Yongqi]], [[Yangkun Wang|Wang, Yangkun]], [[Yuxin Guo|Guo, Yuxin]], [[Yujia Wang|Wang, Yujia]], [[Jingbo Shang|Shang, Jingbo]]

## Links

- **ACL Anthology:** https://aclanthology.org/2023.findings-emnlp.311/

## Abstract

Despite remarkable advances that large language models have achieved in chatbots nowadays, maintaining a non-toxic user-AI interactive environment has become increasingly critical nowadays. However, previous efforts in toxicity detection have been mostly based on benchmarks derived from social media contents, leaving the unique challenges inherent to real-world user-AI interactions insufficiently explored. In this work, we introduce ToxicChat, a novel benchmark constructed based on real user queries from an open-source chatbot. This benchmark contains the rich, nuanced phenomena that can be tricky for current toxicity detection models to identify, revealing a significant domain difference when compared to social media contents. Our systematic evaluation of models trained on existing toxicity datasets has shown their shortcomings when applied to this unique domain of ToxicChat. Our work illuminates the potentially overlooked challenges of toxicity detection in real-world user-AI conversations. In the future, ToxicChat can be a valuable resource to drive further advancements toward building a safe and healthy environment for user-AI interactions.

## Data Description

ToxicChat benchmark dataset of 10,166 real user-AI conversation examples with human toxicity annotations and jailbreaking labels, collected from Vicuna chatbot interactions.


## Notes

