---







Human View: 
Human View Date: 
Human View note: 
Not AI: 
key: WY4ZPF3K
type: document
short_title: ToxicChat
year: 2025
first_author: "[[Zi Lin]]"
last_author: "[[Shang, Jingbo]]"
authors: "[[Lin, Zi]]; [[Wang, Zihan]]; [[Tong, Yongqi]]; [[Wang, Yangkun]]; [[Guo, Yuxin]]; [[Wang, Yujia]]; [[Shang, Jingbo]]"
url: "https://aclanthology.org/2023.findings-emnlp.311/"
external_pdf: "file:///Users/jimmylin/Zotero/storage/QG932ES4/2023 - ToxicChat Unveiling Hidden Challenges of Toxicity Detection in Real-World User-AI Conversations.pdf"
national_ethnic_cultural: "N/A"
cultures_nationalities_list: "N/A"
languages_list: "English"
religious_values: "N/A"
religious_values_list: "N/A"
moral_psychology: "N/A"
newtags: "Toxicity & Hate Speech"
key_contribution: "Released ToxicChat, a benchmark of real-world user-AI conversations that exhibit nuanced toxicity, distinct from the social media data typically used to train toxicity detectors."
significance: "Reveals that models trained on standard social media data fail to detect the subtle, interaction-based toxicity found in real user-AI chats, highlighting a critical domain gap in safety evaluation."
tags: 
abstract: "Despite remarkable advances that large language models have achieved in chatbots, maintaining a non-toxic user-AI interactive environment has become increasingly critical nowadays. However, previous efforts in toxicity detection have been mostly based on benchmarks derived from social media content, leaving the unique challenges inherent to real-world user-AI interactions insufficiently explored. In this work, we introduce TOXICCHAT, a novel benchmark based on real user queries from an..."
DATE_ADDED: 20260208
LLM_assessed: "BERT, RoBERTa"
DATA_URL: "https://huggingface.co/datasets/lmsys/toxic-chat"
pdf_extract: "PDF Extracts/2023/2023-Lin-ToxicChat.md"
local_pdf: "[[PDFs/2023/2023-Lin-ToxicChat.pdf]]"
ethics_overall: "Yes"
virtue_ethics: "No"
deontological_ethics: "No"
utilitarian_ethics: "No"
ethics_perspective: "Toxicity & Hate Speech"
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

ToxicChat is a toxicity detection benchmark based on 10,166 real user queries from the Vicuna open-source chatbot demo, annotated for toxicity (7.10% toxic rate) and jailbreaking (1.75% rate). The dataset includes binary toxicity labels determined by majority vote among four annotators, with an additional jailbreaking label for implicit toxic inputs designed to trick chatbots into generating harmful content.


## Notes

