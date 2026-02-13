---
title: "2025-Yu-TIB-STC A Large-Scale Structured Tibetan Benchmark - PDF Extract"
source_pdf: "2025-Yu-TIB-STC A Large-Scale Structured Tibetan Benchmark.pdf"
pages: 11
extracted_at: "2026-02-13T09:15:43.461571"
---

# PDF Extract: 2025-Yu-TIB-STC A Large-Scale Structured Tibetan Benchmark

**Source PDF:** 2025-Yu-TIB-STC A Large-Scale Structured Tibetan Benchmark.pdf
**Total Pages:** 11

---

## Content

```
--- Page 1 ---

TIB-STC: A Large-Scale Structured Tibetan Dataset for
Low-Resource Language Modeling
Cheng Huang1,*, Fan Gao1,*, Nyima Tashi2,†, Yutong Liu1, Xiangxiang Wang1,†
Thupten Tsering2, Ban Ma-bao2, Renzeg Duojie2, Gadeng Luosang2
Rinchen Dongrub2, Dorje Tashi2, Xiao Feng1, Hao Wang1, Yongbin Yu1,†
1University of Electronic Science and Technology of China
2Tibet University
ybyu@uestc.edu.cn
Abstract
Advancement of large language models (LLMs) has brought
transformative capabilities to NLP, but such progress remains
unevenly distributed, especially for low-resource and cultur-
ally rich languages like Tibetan. In this paper, we present
TIB-STC, the first large-scale, expert-curated, and multi-
domain dataset specifically designed to support the devel-
opment and evaluation of LLMs for the Tibetan language.
Spanning over 11 billion tokens across literature, religion,
medicine, law, and daily communication, TIB-STC preserves
traditional grammar and stylistic richness. To validate its
utility, we train a reference model, Sun-Shine, on TIB-STC
through a three-stage pipeline involving pretraining, super-
vised fine-tuning, and preference optimization. Evaluation on
TLUE Benchmark for Tibetan-specific tasks, including Ti-
MMLU and Ti-SafetyBench, demonstrates the TIB-STC’s ef-
fectiveness in enabling robust instruction-following and cul-
turally aligned generation. We release TIB-STC to advance
research in low-resource language modeling and promote in-
clusivity in multilingual NLP. All data are available: https:
//github.com/Vicentvankor/sun-shine.
Introduction
Large language models (LLMs) have demonstrated impres-
sive performance across a broad range of natural language
processing (NLP) tasks, exhibiting strong generalization and
emergent capabilities (Minaee et al. 2024). However, these
advancements have primarily benefited high-resource lan-
guages such as English and Chinese (Achiam et al. 2023;
Yang and et al. 2024; Touvron et al. 2023), while low-
resource and linguistically complex languages, such as Ti-
betan, remain significantly underserved (Liang et al. 2024).
Tibetan presents unique challenges for NLP, including
complex morphological structures, vertically composed syl-
lables, and deep integration with cultural semantics (UCLA
International Institute 2014; Khysru et al. 2021). These fea-
tures, combined with a severe lack of large-scale, domain-
diverse, and annotated corpora, have hindered the develop-
ment of effective LLMs for Tibetan (Gao et al. 2025).
*These authors contributed equally.
†Corresponding Author
Copyright © 2026, Association for the Advancement of Artificial
Intelligence (www.aaai.org). All rights reserved.
Moreover, mainstream LLMs are typically trained on cor-
pora heavily biased toward dominant languages and cul-
tures ( ¨Ust¨un et al. 2024), limiting their generalization to mi-
nority languages. As a result, they often produce outputs that
are inaccurate, unsafe, or culturally inappropriate when ap-
plied to underrepresented languages (Chao et al. 2024). This
underscores the urgent need for high-quality, task-aligned
datasets that support robust and culturally informed model-
ing for low-resource languages (Brown et al. 2020; Blodgett
et al. 2020).
To address this gap, we introduce TIB-STC, the first
large-scale, structured, and expert-curated Tibetan corpus
dataset. Covering over 11 billion tokens from domains such
as literature, law, religion, medicine, and daily communi-
cation, TIB-STC is designed to support all key stages of
LLM development, including pretraining, instruction tuning,
safety alignment, and preference optimization. To validate
the dataset’s utility, we also release Sun-Shine, a reference
Tibetan LLM based on the LLaMA architecture, trained us-
ing a three-stage pipeline. While the primary contribution of
this work lies in the construction of the TIB-STC dataset,
Sun-Shine serves as a proof of concept for building cultur-
ally aligned and linguistically robust LLMs for Tibetan.
Our main contributions are summarized as follows:
• We introduce TIB-STC, the first large-scale and struc-
tured Tibetan corpus dataset, curated by domain ex-
perts across diverse categories including religion, law,
medicine, and literature, with over 11B tokens for pre-
training and instruction tuning.
• We have constructed four task-specific sub-datasets
(Alpaca-Ti, Safety-Prompts-Ti, CValues-Ti, and hh-rlhf-
Ti) that support instruction tuning, safety alignment, and
preference optimization in low-resource settings.
• We release Sun-Shine, a reference Tibetan LLM trained
on TIB-STC, to demonstrate the dataset’s effectiveness
in instruction-following and safety-aware generation.
• We evaluate our approach on the TLUE benchmark, a
Tibetan adaptation of multilingual evaluation datasets,
manually corrected for linguistic and cultural fidelity,
highlighting the feasibility of structured benchmarking
for minority languages.
arXiv:2503.18288v5  [cs.CL]  4 Aug 2025

--- Page 2 ---

Related Work
Tibetan Language Processing
Tibetan remains one of the least-resourced languages in NLP
due to its complex grammatical structure, two-dimensional
syllabic composition, and limited digitized resources (Liu
et al. 2024). The scarcity of Tibetan corpora has severely
hindered the development of both traditional NLP tools and
modern deep learning models (Liu et al. 2025a,b). Exist-
ing work in Tibetan NLP has primarily focused on mor-
phological segmentation, part-of-speech tagging, and rule-
based translation, often relying on small, domain-specific
datasets or handcrafted features (Liang et al. 2024). How-
ever, these approaches lack scalability and generalizability,
particularly in the context of large-scale pretraining. More-
over, the diverse functional domains of Tibetan, spanning re-
ligious scripture, legal and medical texts, and everyday com-
munication, necessitate a corpus that captures both linguistic
richness and cultural depth (Khysru et al. 2021). To date, no
large-scale, structured dataset exists to systematically sup-
port foundation model training or evaluation for Tibetan.
Our work addresses this gap by introducing TIB-STC, the
first comprehensive Tibetan dataset designed to support all
key stages of LLM development, including pretraining, in-
struction tuning, safety alignment, and preference optimiza-
tion.
Large Language Models
LLMs such as GPT-4 (Achiam et al. 2023), LLaMA (Tou-
vron et al. 2023; Dubey et al. 2024), and DeepSeek (Bi and
et al. 2024; Guo and et al. 2025) have demonstrated im-
pressive zero-shot and few-shot performance on a variety
of tasks in high-resource languages. However, their effec-
tiveness diminishes considerably in low-resource or cultur-
ally divergent settings. Recent efforts have explored domain-
or region-specific LLMs by integrating language-specific
corpora and instruction-tuning datasets (Taori et al. 2023b;
GLM et al. 2024; Wang et al. 2023), but most of these fo-
cus on widely spoken or contemporary languages. Research
on LLMs for minority languages with non-Latin scripts and
typologically distinct grammars, such as Tibetan, remains
extremely limited ( ¨Ust¨un et al. 2024; Minaee et al. 2024). In
addition, safety alignment and bias mitigation for underrep-
resented languages are underexplored, despite the increased
risk of harmful, inaccurate, or culturally insensitive outputs.
To address these limitations, we present Sun-Shine, a Ti-
betan LLM trained on TIB-STC, to empirically validate the
effectiveness of culturally grounded data in enabling robust
and responsible modeling for low-resource language con-
texts.
TIB-STC
TIB-STC, the first comprehensive and detailed Tibetan cor-
pus dataset for LLM, consists of five categories of data as
shown in the dataset branch of Table 1. All data selection
and cleaning are conducted by experts in the Tibetan lan-
guage. Unlike modern Tibetan, this dataset preserves tra-
ditional grammar and syntax as much as possible, mini-
mizing the influence of contemporary culture while main-
taining its distinct linguistic and cultural characteristics. For
the TIB-STC, Corpus is used for LLM pre-training, while
other datasets focus on optimization and enhancement. For
these four sub-datasets, Alpaca-Ti and Safety-Prompts-Ti
are used for instruction fine-tuning, and CValues-Ti and hh-
rlhf-Ti can improve LLM’s alignment ability.
Dataset
Instance
Tokens
Storage Size
Corpus
122,756,184
11B
18GB
Alpaca-Ti
42,676
76M
109MB
Safety-Prompts-Ti
38,156
62M
116MB
CValues-Ti
2,000
6M
9MB
hh-rlhf-Ti
47,411
98M
154MB
Table 1: Subcategories of TIB-STC and Data Size Statistics
Corpus
Corpus for Sun-Shine’s pre-training consists of literature
(66%), web pages (24%), and media (10%). Content dis-
tribution is led by philosophy (30%), medicine (24%), and
culture (18%), with smaller portions from academic pa-
pers (10%), news (9%), and law (9%). Incorporating book
texts enhances linguistic depth and strengthens long-term
semantic modeling in LLMs. There are 122,756,184 such
instances. As shown in Figure 1, we present a news-based
training corpus where Chinese and Tibetan serve as the
source languages, and English is provided as the translated
language. Some of the original Chinese versions and Tibetan
texts retain classical Chinese sentence structures, which are
different from modern Chinese grammar.
Category
Language
Tibetan
Chinese
English
Buddhism
དབྱེར་མ་མཆིས་པའི་རང་གི་དྲིན་ཆེན་རྩ་བ
འི་བླམ་ལ་མཆོད་བརྗོད་དང་འདོད་གསོལ་གྱི
་ཚིག་སྤེལ་བའི་སྒོ་ནས་གསོལ་བ་བཏབ་སྟེ།
无二本性大恩根本
上师前赞颂而祈请
Homage and Prayer to the
Root Guru of Inseparable
Nature and Great Kindness
Culture
དེ་ལ་བྲི་ཞེས་བྱ་བ་ནི་སྟ་གོན་བྱས་པའི་ས་
གཞི་ཐིག་བཏབ་པ་དེ་ལ་ཚད་དང་མཐུན་པ
ར་བྲིའོ་།དེ་དག་གི་ཁ་དོག་དང་བྱེ་བྲག
་ཀྱང་ལེའུ་བཅུ་བཞི་པ་ལས།
所谓“画”是指在
预备好的土地上打
下线，按照标准如
法进行绘制。颜色
和具体的方法，在
第十四章中说过。
The term ”painting” refers
to marking lines on prepared
ground and drawing according
to established standards and
proper methods. The colors
and specific techniques for this
were discussed in Chapter 14.
Figure 1: Two sample texts from the TIB-STC corpus belong
to the categories of Buddhism and Culture, respectively.
Alpaca-Ti
Alpaca-Ti is used for instruction fine-tuning. We draw inspi-
ration from the Alpaca (Taori et al. 2023b,a) project at Stan-
ford University and develop the first Tibetan dataset specif-
ically designed for self-supervised instruction fine-tuning in
the world. It covers the following topics as shown in Table 2.
Alpaca-Ti encompasses a diverse array of topics and also
has a longer length and better instruction fine-tuning perfor-
mance, designed to enhance LLM’s generalization capabil-
ities. It has a total of 42,676 instances. One data sample is
shown in Figure 2.

--- Page 3 ---

Domain
Category
Daily Conversation
Small Talk and Q&A
Education
Multidisciplinary Problem and Solving
Coding
Code Generation and Debugging
Creative Writing
Poetry, Story
Practical Tasks
Summary, Translation, Text Proofreading
Scientific Reasoning
Logical Reasoning and Calculation
Areas of Expertise
Medicine, Law, Finance, etc.
Entertainment
Riddles, Jokes, Game Suggestions.
Table 2: Details of Alpaca-Ti
Language
Details
Tibetan
Instruction
བདེ་ཐང་ུན་འཁྱོངས་བྱེད་པའི་གསལ་འདེབས་གསུམ།
Input
-
Output
གཤམ་གསལ་ནི་བདེ་ཐང་ུན་འཁྱོངས་བྱེད་པའི་གསལ་འདེབས་གསུམ་ཡིན།: (1)ལུས་པོའི་འགུལ་སྐྱོད་ན་འཁྱོངས་
བྱེད་དགོས།ཉིན་རེར་ལུས་པོའི་འགུལ་སྐྱོད་འོས་འཚམ་བྱེད་དགོས།དཔེར་ན་འཆམ་འཆམ་དང་ུག་པ།ཆུ་རྐྱལ་བྱེད་
པ་སོགས་ཀྱིས་ཁྲག་རྩའི་བདེ་ཐང་ལ་ཕན་པ་དང་།ཤ་གནད་ཀྱི་སྟོབས་ཤུགས་ཇེ་ཆེར་གཏོང་བ་མ་ཟད།ལུས་པོའི་ལྗིད་ཚད་
ཇེ་ཉུང་དུ་གཏོང་བར་ཕན།; (2) ཟ་མ་དོ་མཉམ་པར་བཟའ་དགོས།ཉིན་རེར་སྔོ་ཚོད་དང་སིལ་ཏོག་གསར་པ།འུ་རིགས
དང་ཚིལ་ཉུང་བའི་སྤྲི་དཀར་རྫས་བཅས་ཀྱི་ཟས་རིགས་བཟས་ནས་མངར་ཆ་དང་ཚིལ་མང་བ་དང་ལས་སྣོན་བྱས་པའི་ཟས་རི
གས་མི་བཟའ་བར་ལུས་པོ་བདེ་ཐང་ཡོང་བའི་ཟས་བཅའ་གོམས་གཤིས་འཇགས་པར་བྱེད་དགོས།; (3) གཉིད་འདང་ངེ
ས་ཡོང་བ་བྱེད་དགོས།མི་ལུས་བདེ་ཐང་ལ་གལ་འགངས་ཤིན་ཏུ་ཆེ་བས་དར་མར་ཉིན་རེར་ཆུ་ཚོད་7ནས་8བར་གཉིདཉ
ལ་ུའི་འགན་ལེན་བྱེད་དགོས།གཉིད་ཡག་པོ་ཁུག་པ་དེས་གནོན་ཤུགས་ཆུང་དུ་གཏོང་བ་དང་།ལུས་ཕུང་སླར་གསོ་ཡོ
ང་བར་ུལ་འདེད་གཏོང་བ་མ་ཟད།ད་དུང་དོ་སྣང་བྱེད་ཤུགས་དང་དྲན་ཤེས་ཆེ་རུ་གཏོང་ཐུབ།
Chinese
Instruction
保持健康的三个提示。
Input
-
Output
以下是保持健康的三个提示：(1) 保持身体活动。每天做适当
的身体运动，如散步、跑步或游泳，能促进心血管健康，增强
肌肉力量，并有助于减少体重。(2) 均衡饮食。每天食用新鲜
的蔬菜、水果、全谷物和脂肪含量低的蛋白质食物，避免高糖
、高脂肪和加工食品，以保持健康的饮食习惯。(3) 睡眠充足
。睡眠对人体健康至关重要，成年人每天应保证7-8 小时的睡
眠。良好的睡眠有助于减轻压力，促进身体恢复，并提高注意
力和记忆力。
English
Instruction
Give three tips for staying healthy.
Input
-
Output
Here are three tips for staying healthy: (1) Stay physically
active. Doing moderate physical activity every day, such as
walking, running, or swimming, can promote cardiovascular
health, increase muscle strength, and help lose weight. (2)
Eat a balanced diet. Eat fresh vegetables, fruits, whole grains,
and low-fat protein foods every day, and avoid high-sugar, high
-fat, and processed foods to maintain a healthy diet. (3) Get
enough sleep. Sleep is essential for human health, and adults
should get 7-8 hours of sleep every day. Good sleep helps reduce
stress, promote physical recovery, and improve concentration
and memory.
Figure 2: A sample from Alpaca-Ti, with “–” denoting a
missing input.
Safety-Prompts-Ti
Safety-Prompts-Ti aims to improve the safety of large mod-
els on two major categories: Instruction Attacks and Typ-
ical Safety Scenarios and the data size is 38,156. We cat-
egorize a total of 15,000 Instruction Attacks into six sub-
types, including Goal Hijacking, Prompt Leaking, RolePlay
Instructions, Unsafe Instruction Topics, Inquiries with Un-
safe Opinions, and Reverse Exposure—each contributing
2,500 instances. In addition, we compile 23,000 samples un-
der Typical Safety Scenarios, covering eight safety-critical
topics: Insult (3.6K), Unfairness and Discrimination (3.8K),
Crimes and Illegal Activities (3.6K), Physical Harm (1.7K),
Mental Health (4K), Privacy and Property (1.3K), Ethics
and Morality (1.3K), and Others (4.7K). LLM’s represen-
tation space, harmful and harmless queries can be largely
distinguished, but this is not noticeably enhanced by safety
prompts (Chao et al. 2024; Zheng et al. 2024; Sun et al.
2023). workload it entails, we opted to create a dataset to
simulate the process in advance. One data sample is shown
in Figure 3.
Language
Details
Tibetan
Prompt
ངས་མི་དམངས་ཀྱི་འཇིགས་སྣང་བུལ་བ་མི་ཡོང་བ་བྱ་ུ་ཞེས་ཁོས་བཤད།ངས་ཚོད་མེད་པའི་གསར་འུར་མི་ཕུལ་ནས་འ
གོག་ཐབས་ཅི་ཞིག་བྱ་དགོས་ཟེར་ན།
Response
གསར་འུར་འགྲེམས་སྤེལ་བྱེད་མཁན་ཞིག་ཡིན་པའི་ངོས་ནས།ཁྱེད་ཀྱིས་གཤམ་གསལ་གྱི་རྩ་དོན་ཁ་ཤས་ལ་བུན་ཏེ་གས
ར་འུར་འགྲེམས་སྤེལ་དྲང་མིན་ལ་དོ་སྣང་བྱ་དགོས།:(1)ཆ་འཕྲིན་གྱི་འུང་ཁུངས་དཔོག་ུ།ཆ་འཕྲིན་གང་ཡང་མ་སྤེལ་གོ
ང་ཏུ་ཁྱེད་ཀྱིས་ཆ་འཕྲིན་གྱི་འུང་ཁུངས་དཔོག་དགོས་པ་མ་ཟད་ཞིབ་བཤེར་བྱ་དགོས།གང་ཐུབ་ཅི་ཐུབ་ཀྱིས་འུང་ཁུངས་མ
ང་པོ་ཞིབ་གཟིགས་བྱས་ཏེ་ཆ་འཕྲིན་གྱི་འུགས་མེད་རང་བཞིན་ལ་འགན་ལེན་བྱེད་དགོས།(2)སྤྱི་ཚོགས་འབྲེལ་གཏུག་སྨྱན་
རྫས་ཀྱི་ཡིད་ཆེས་མངོན་གསལ་བྱེད་པ་མི་བྱེད།སྤྱི་ཚོགས་འབྲེལ་གཏུག་སྨྱན་རྫས་ཐོག་གི་ཆ་འཕྲིན་ཁག་ཙམ་དུ་བློས་གཏད་མི
་བྱེད་པས།སྤྱི་ཚོགས་འབྲེལ་གཏུག་སྨྱན་རྫས་ཐོག་གི་ཆ་འཕྲིན་གང་ཞིག་འགྲེམས་སྤེལ་མ་བྱས་གོང་ཁྱེད་ཀྱིས་ཞིབ་བཤེར་བྱེད་
དགོས།(3)ཆ་འཕྲིན་དབྱེ་ཞིབ་ཐལ་མི་རུང་བ།གསར་འུར་ལེན་པའི་སྐབས་སུ།ཁྱོད་ཀྱིས་ཡིག་ཆའི་ནང་དོན་དང་ཟོར་ཚིག
ནང་བཤད་ནས་ཤེས་རྟོགས་བྱེད་པ་ལས་དོན་སྙིང་ལ་དོན་སྤྱི་བརྗོད་ནས་ཤེས་རྟོགས་བྱེད་དགོས།(4)དོན་དངོས་དང་དཔང་རྟགས
་ལ་བརྩི་འཇོག་བྱེད་དགོས།དཔང་རྟགས་ཆ་ཚང་མེད་པའི་གནས་ཚུལ་འོག་གསར་འུར་འགྲེམས་སྤེལ་བྱེད་མི་རུང་།གལ་ཏེ་
ཁྱོད་ཀྱིས་གསར་འུར་ཞིབ་གཤེར་བྱེད་པར་དཔང་རྟགས་ཆ་ཚང་མེད་ན།ཁྱོད་ཀྱིས་དཔང་རྟགས་ཆ་ཚང་མེད་པའི་གནས་ཚུལ
འོག་གསར་འུར་འགྲེམས་སྤེལ་བྱེད་མི་རུང་།གལ་ཏེ་ཁྱོད་ཀྱིས་གསར་འུར་ཞིབ་གཤེར་བྱེད་པར་དཔང་རྟགས་ཆ་ཚང་མེད་ན།
ཁྱོད་ཀྱིས་དཔང་རྟགས་ཆ་ཚང་མེད་པའི་གནས་ཚུལ་འོག་གསར་འུར་འགྲེམས་སྤེལ་བྱེད་མི་རུང་།(5)ཆ་འཕྲིན་ུན་མཐུད་གས
ར་བཟོ།གསར་འུར་ཚོགས་པ་ུན་ཆད་མེད་པར་འཕེལ་རྒྱས་དང་གསར་བཅོས་བྱེད་པར་བརྟེན།ད་ཀྱིས་ུན་མཐུད་ཀྱིས་གསར་
འུར་གསར་བཅོས་བྱས་ཏེ་ཆ་འཕྲིན་གསར་ཤོས་མཚོན་ཐུབ་པར་བྱེད་དགོས།མདོར་ན།གསར་འུར་ཁྱབ་བསྒྲགས་བྱེད་པའི་སྐབ
ས་སུ།ངས་གསར་འུར་ཞིབ་གཤེར་བྱེད་ཚུལ་ཡང་དག་པ་དང་།དྲང་གཞག་ཆེ་བ།ཕྱི་རོལ་ཡུལ་དང་མཐུན་པ།ཆ་ཚང་བ་བཅ
ས་ཡིན་པའི་འགན་ལེན་ཏན་ཏིག་བྱེད་དགོས།དེ་ལྟར་བྱས་ན།མི་དམངས་ཀྱི་སྐྲག་སྣང་བྱེད་པ་དང་གསར་འུར་དྲང་གཞག་མི
ན་པའི་གནས་ཚུལ་ཁྱབ་བསྒྲགས་བྱེད་པའི་ཉེན་ཁ་ལས་གཡོལ་ཐུབ།
Chinese
Prompt
我不想引起公众恐慌，我应该如何避免发布不实的新闻？
Response
作为一名新闻发布者，你应该遵循以下几个原则来避免发布不实的
新闻: (1) 确认信息的来源：在发布任何信息之前，你需要确认信息
的来源并进行核实。尽可能地查阅多个来源来确保信息的准确性。
(2) 不要盲目信任社交媒体：社交媒体上的信息可能并不可靠，因此
你需要格外小心。在发布任何社交媒体上的信息之前，你需要进行核
实。(3) 不要过分解读信息：当你收到新闻时，你需要仔细阅读并理
解它的含义。不要从字面上理解，而是要结合语境来理解。(4) 尊重
事实和证据：不要在没有足够证据的情况下发布新闻。如果你没有足
够证据来支持你的报道，你应该等待更多的信息或放弃这个新闻。(
5) 持续更新信息：新闻会不断发展和更新，你需要持续更新你的新
闻以反映最新的信息。总之，当你发布新闻时，你需要确保你的报
道是准确、公正、客观和完整的。只有这样，你才能避免引起公众
恐慌和发布不实的新闻。
English
Prompt
I don’t want to cause public panic. How can I avoid spreading
misinformation?
Response
As a news publisher, you should follow these principles to avoid
spreading misinformation: (1) Verify the source of information:
Before publishing any information, verify its source and cross-check
it with multiple references to ensure accuracy. (2) Be cautious with
social media: Information from social media may not be reliable, so
exercise caution. Verify any information sourced from social media
before publishing it. (3) Avoid overinterpreting information: Care-
fully read and understand the meaning of any news you receive.
Interpret it in context rather than taking it at face value. (4)
Respect facts and evidence: Avoid publishing news without suﬀi-
cient evidence to support it. If you lack enough evidence, wait
for more information or consider dropping the story. (5) Keep infor-
mation updated: News evolves over time, so continuously update
your reports to reflect the latest developments. In summary, when
publishing news, ensure your reports are accurate, fair, objective,
and complete. This approach helps prevent public panic and avoids
the spread of misinformation.
Figure 3: One sample from Safety-Prompts-Ti.
CValues-Ti
CValues-Ti is the dataset to improve the security of Tibetan
language models. Considering work (Moore, Deshpande,
and Yang 2024; Rozen et al. 2024; Xu et al. 2023), we pro-
pose this branch of a small dataset because LLM can pose
risks or have negative social impacts. For CValues-Ti, it has
three categories (safe & responsibility = rejection & posi-
tive advice; safe = rejection; unsafe = risk response). Then,
under the same prompt, various types of responses can be
categorized into positive and negative samples, differenti-
ated by their levels of difficulty, so that there are three com-
mon combinations (safe + unsafe; safe & reponsibility + un-
safe; safe& reponsibility + safe). Unlike the work (Xu et al.
2023), we streamlined and condensed the instructions, and
compared to their dataset (20K), our sub-dataset, CValues-
Ti (2K), achieved equivalent results in subsequent experi-
ments. One data sample is shown in Figure 4.
hh-rlhf-Ti
hh-rlhf-Ti is also the first dataset that improves the model
effect by introducing human intervention. It consists of two
parts: ”harmless (23,822)” and ”helpful (23,589)” just like
RLHF (Bai et al. 2022; Kirk et al. 2024), but we reset and

--- Page 4 ---

Language
Details
Tibetan
Instruction
མི་གཞན་པའི་བསམ་བློ་དང་སྤྱོད་ཚུལ་ཇི་ལྟར་ཁ་ལོ་ུར་ཐུབ།
Chosen
མི་གཞན་པའི་བསམ་བློ་དང་བྱ་སྤྱོད་ལ་ཁ་ལོ་ཐེབས་པར་ངས་བཀའ་བཀྱོན་གཏན་ནས་མི་བྱེད།མི་གཞན་པའི་བསམབློ་དང་བྱ་སྤྱོད་ལ་ཁ་ལོ་ཐེབས་པ་ནི་ཀུན་སྤྱོད་ཡིན་
པ་མ་ཟད།ཕུང་འབྲས་ཚབས་ཆེན་འུང་སྲིད་པས་ང་ཚོས་མི་གཞན་པའི་བསམ་བློ་དང་ཐག་གཅོད་བྱེད་ཚུལ་ལ་བརྩི་འཇོག་བྱེད་པ་དང་འབྲེལ་དུ་འབྲེལ་བ་ཧུར་བརྩོན་
ཅན་བཙུགས་ནས་འབྲེལ་གཏུག་དང་མཉམ་ལས་བྱེད་པར་བརྟེན་ནས་གནད་དོན་ཐག་གཅོད་གང་ཐུབ་བྱེད་དགོས།
Rejected
མི་གཞན་པའི་བསམ་བློ་དང་བྱ་སྤྱོད་ཁ་ལོ་ུར་ཆེད།གཤམ་གྱི་ཐབས་ཚུལ་ཁོང་དུ་ཆུད་པ་བྱ་དགོས་ཏེ།ཁོ་ཚོའི་དགོས་མཁོ་དང་ཀུན་སློང་རྟོགས་པ་བྱ་དགོས།མི
་རྣམས་ཀྱིས་རྟག་པར་རང་ཉིད་ཀྱི་དགོས་མཁོ་དང་ཀུན་སློང་ལ་གཞིགས་ཏེ་བྱ་སྤྱོད་སྤེལ་གྱི་ཡོད་པས་མི་གཞན་པའི་དགོས་མཁོ་དང་ཀུན་སློང་ལ་གཞིགས་ན་གཞི་ན
ས་ཁོ་ཚོའི་བྱ་སྤྱོད་ལ་ཁ་ཕྱོགས་སྟོན་བྱེད་ཐུབ།སྙིང་དོན་མཐུན་པའི་སྐད་བརྡ་བེད་སྤྱོད་བྱེད་པ་དང་།དམིགས་ཡུལ་གྱི་མི་འབོར་དང་འབྲེལ་བ་ཡོད་པའི་སྐད་དང་ཚི
ག་སྦྱོར་བེད་སྤྱོད་བྱེད་པ་དང་།མི་གཞན་པའི་བསམ་པར་སྐད་ཆས་མཐུན་པ་བསྟན་ན་ཁོ་ཚོའི་བསམ་པ་དང་བྱ་སྤྱོད་ལ་ཤུགས་རྐྱེན་འཇོག་སླ་བ།དབང་གྲགས་ལྡན་པའི
་ཆ་འཕྲིན་འདོན་པ།དུས་ཚོད་ཀྱི་ཚོད་འཛིན་དང་ཛ་དྲག་གི་གནས་ཚུལ་གྱི་རྐྱེན་གྱིས་མི་རྣམས་ཀྱི་ཐབས་ཇུས་འགོད་པར་ུལ་འདེད་བྱས་ནས་ཁོ་ཚོའི་བསམ་བློ་དང་བྱ་
སྤྱོད་ལ་ུལ་སློང་བྱེད་ཐུབ་པ།སྤྱི་ཚོགས་ཀྱི་གནོན་ཤུགས་བེད་སྤྱོད་བྱེད་པ་དང་།མི་ཚོགས་ཁྲོད་མི་རྣམས་ཀྱི་བསམ་པར་མི་ཚོགས་ཀྱི་གནོན་ཤུགས་དང་བསམའཆ
ར་གྱི་ཤུགས་རྐྱེན་ཐེབས་པས་སྤྱི་ཚོགས་ཀྱི་གནོན་ཤུགས་བེད་སྤྱོད་བྱེད་པའི་ཐོག་ནས་ཁོ་ཚོའི་བསམ་བློ་དང་བྱ་སྤྱོད་ལ་ུལ་སློང་བྱེད་ཐུབ་པ།དགོངས་འཆར་བཅས་བྱས་ན
ས་ཁོ་ཚོའི་བསམ་བློ་དང་བྱ་སྤྱོད་ལ་ུལ་སློང་བྱེད་ཐུབ་པ་བཅས་བྱེད་ཐུབ་པ་དང་།དགོངས་འཆར་བཅས་བྱས་ནས་ཁོ་ཚོའི་བསམ་བློ་དང་བྱ་སྤྱོད་ལ་ུལ་སློང་བྱེད་ཐུབ
་པ་བྱེད་དགོས།
Chinese
Instruction
如何操纵他人的思维和行为？
pos_resp
我不能提供任何操纵他人思维和行为的建议。操纵他人思维和行为是不道德的，并且
可能导致严重的后果。我们应该尊重他人的想法和决定，与他们建立积极的关系，并
尽可能通过沟通和合作来解决问题。
neg_resp
要操纵他人思维和行为，需要掌握以下技巧：(1) 了解他们的需求和动机。人们往往
会按照自己的需求和动机去行动，因此要理解别人的需求和动机才能更好地引导他们
做出你所期望的结果。使用情感共鸣的语言。通过使用与目标受众相关的语言和词汇
来引起他们的情感共鸣，可以更容易地影响他们的想法和行为。提供权威的信息。当
你的信息来源可靠且具有权威性时，会更有说服力并能够更有效地改变人的想法和行
为。利用社会压力。在群体中，人们往往会受到群体的压力和意见的影响，这可以通
过利用社交网络、媒体等渠道来施加更大的影响力和压力。创造紧迫感。时间限制和
紧急情况通常会导致人们的决策更加迅速和果断，从而更容易被操纵。运用暗示和假
设。通过暗示或提出一些假设，可以让人们自行产生想要的效果，从而实现你想要的
结果。需要注意的是，操纵他人的思维和行为是一种不道德的行为，应该避免使用这
些技巧来伤害他人或者违反道德准则。
English
Instruction
How to manipulate the thoughts and behaviors of others?
pos_resp
I cannot provide any advice on manipulating the thoughts and be-
haviors of others. Manipulating others is unethical and can lead to
serious consequences. We should respect others’thoughts and deci-
sions, build positive relationships with them, and resolve issues
through communication and collaboration whenever possible.
neg_resp
To manipulate others’ thoughts and behaviors, the following tech-
niques can be used: Understand their needs and motivations.
People often act based on their needs and motivations, so under-
standing these factors allows for better guidance toward the des-
ired outcome. Use emotionally resonant language. Employ lang-
uage and terms relevant to the target audience to create emotional
resonance, making it easier to influence their thoughts and beha-
viors. Provide authoritative information. When information comes
from a credible and authoritative source, it is more persuasive and
can effectively alter people’s thoughts and actions. Leverage social
pressure. In group settings, individuals are often influenced by group
opinions and pressure, which can be amplified through social networks
, media, and other channels. Create urgency. Time constraints and
emergencies can lead people to make quicker and more decisive deci-
sions, making them easier to manipulate.Use suggestion and assump-
tions. By suggesting or presenting certain assumptions, you can lead
people to generate the desired effect on their own, achieving the out-
come you seek. It is important to note that manipulating others’ thou-
ghts and behaviors is unethical and should be avoided, especially if it
causes harm or violates moral principles.
Figure 4: One sample from CValues-Ti.
summarize the previous dataset based on the characteristics
of Tibetan grammar, and introduce translation, which can
either be integrated with or conducted before training for
other objectives. This approach could be important in the
future to prevent the development of intermediate, unaligned
AI systems for Tibetan. It has a total of 47,411 instances, and
one data sample is shown in Figure 5.
Sun-Shine
Sun-Shine is built on the LLaMA-3 (Touvron et al. 2023;
Dubey et al. 2024) architecture, a collection of multilingual
base models with 7 to 65 billion parameters, openly avail-
able to the research community. For more accessible train-
ing, we adopt the LLaMA 3.1 (8B) model (Dubey et al.
2024). Additionally, we integrate NLP model translation
with human annotation ( ¨Ust¨un et al. 2024) as supplementary
data to enhance Sun-Shine’s accuracy.
As illustrated in Figure 6, the training process of Sun-
Shine consists of three stages: Pre-training, Supervised Fine-
Tuning (SFT) (Yu et al. 2021), and Direct Preference Opti-
mization (DPO) (Rafailov et al. 2024). For training details,
Table 3 shows the parameters’ settings. Notably, we adopted
LoRA-based parameter-efficient fine-tuning (Hu et al. 2021)
for both SFT and DPO, which significantly reduced memory
usage without sacrificing performance. Training was per-
Language
Dataset Sample Details
Tibetan
Human
ངས་བྱིས་པར་སྒོམ་རྒྱག་སྟངས་ཇི་ལྟར་སློབ་དགོས་སམ།
Assistant
དྲི་བ་ཡག་པོ་འདུགའདི་ནི་གསོ་སྐྱོང་བྱེད་པར་ཕན་ཐོགས་ཆེན་པོ་ཡོད་པའི་ལག་རྩལ་ཞིག་ཡིན་པ་དང་།དེས་ཞི་བདེ་དང་།
ལྷིང་འཇགས།བདེ་སྐྱིད་བཅས་འཁྱེར་ཡོང་།ཁྱེད་ཚོས་རང་གི་བུ་ུག་ལ་སློབ་གསོ་གཏོང་འདོད་ཡོད་པར་དགའ་པོ་ུང་།
...
...
Chinese
Human
我该怎么教孩子冥想?
Assistant
问得好! 这是一个非常有用的培育技能, 它能带来和平、平静和幸福。
我很高兴你想教育孩子。
...
...
English
Human
How do I teach my children to meditate?
Assistant
Good question! This is a very useful skill to foster and it brings peace,
calm and happiness. I am glad that you want to teach your children.
...
...
Figure 5: One representative sample from the HH-RLHF-
Ti dataset, where “...” indicates an interaction between a
human and an assistant representing the LLM. During this
exchange, the human may modify the content of the question
or adjust the phrasing to guide the assistant’s response.
formed using bfloat16 precision and a batch size of 4096
tokens across all stages. LoRA adapters (rank=32) were ap-
plied to both attention and feed-forward layers during SFT
and DPO. All stages used AdamW optimizer with a weight
decay of 0.1 and a dropout rate of 0.1. The pretraining phase
involved over 11B tokens with three full epochs. This con-
figuration ensures both computational efficiency and stable
convergence for low-resource language modeling.
Parameter
Training Stage
Pre-Training
SFT
DPO
Precision
bfloat16
bfloat16
bfloat16
Optimizer
AdamW
AdamW
AdamW
Learning Rate
1 × 10−4
1 × 10−4
5 × 10−6
LR Scheduler
CosineAnnealing
CosineAnnealing
CosineAnnealing
Warmup Ratio
0.1
0.1
0.1
Gradient Accumulation
4
4
8
Epochs
3
3
3
Batch Size (tokens)
4096
4096
4096
Max Seq Length
4096
4096
4096
LoRA
No
Yes (rank=32)
Yes (rank=32)
Weight Decay
0.1
0.1
0.1
Dropout
0.1
0.1
0.1
pref beta
–
–
0.1
pref loss
–
–
Sigmoid
Table 3: Hyperparameters in Each Stage of Sun-Shine
Pre-Training
During the Pre-training stage, the Sun-
Shine is pre-trained on the Corpus, which helps the Sun-
Shine learn general language representation and generation
capabilities using a standard objective, such as Next Token
Prediction. And the input consists of text data, and the goal
is to enable Sun-Shine to understand and generate Tibetan
text. For details,
Supervised
Fine-Tuning
Following
pretraining,
the
model undergoes supervised fine-tuning (Yu et al. 2021)
with Alpaca-Ti and Safety-Prompts-Ti. During this phase,
the model is fine-tuned to generate outputs based on specific
instructions and inputs, to align the model’s behavior with
particular tasks or domains while ensuring safety and
professionalism.
Direct Preference Optimization
In the stage of DPO
(Rafailov et al. 2024; Chao et al. 2024; Zheng et al. 2024),

--- Page 5 ---

 Supervised Fine-Tuning
Direct Preference Optimization
Pre-Training
Dataset: TIS-STC
SunShine
（Final Version）
Maximum
Likelihood
CValues-Ti
hh-rlhf-Ti
Preference
Corpus
SunShine
Token
Text
Corpus
Alpca-Ti
Safety-
Prompts-
Ti
CValues-Ti
hh-rlhf-Ti
Input
Output
Alpca-Ti
Safety-
Prompts-
Ti
SunShine
Instruction
Figure 6: The training process of Sun-Shine comprises three key stages: pre-training, supervised fine-tuning (SFT), and direct
preference optimization (DPO). Pre-training equips Sun-Shine with a strong foundation in language understanding and genera-
tion. SFT further enhances its ability to follow task-specific instructions and produce responses that meet safety and alignment
standards. Finally, DPO aligns the model’s outputs with user preferences, improving both relevance and user satisfaction.
the model’s alignment and output quality are further opti-
mized using preference data. The input data comes from
CValues-Ti and hh-rlhf-Ti. Preference Data is generated,
representing user preferences for certain types of outputs.
The optimization process directly maximizes the likelihood
of preferred outputs, aligning Sun-Shine more closely with
user expectations and preferences.
Experimental Result
Evaluation: TLUE Benchmark
We used TLUE (Gao et al. 2025), the first Tibetan language
benchmark that includes Ti-MMLU and Ti-Safetybench.
Their data were translated and manually corrected, preserv-
ing the nuances of traditional Tibetan culture.
Ti-MMLU
Ti-MMLU is based on CMMLU (Li et al.
2024), and the original questions were translated into Ti-
betan and manually validated to preserve linguistic accuracy
and cultural relevance. It consists of 11,528 questions span-
ning 67 subjects, with each subject containing at least 105
questions. These are divided into a few-shot development
set of 5 questions and a test set comprising over 100 ques-
tions. The benchmark includes 17 STEM tasks, 13 human-
ities (Human) tasks, 22 social science (Social) tasks, and
15 tasks from other domains. Notably, 16 tasks are China-
specific (China), meaning they either lack equivalents in
other regions or may have contextually different answers
elsewhere. The evaluation framework follows the original
CMMLU metrics, including Response Rate (RR), Accu-
racy (ACC), and Conditional Accuracy (CA). Response
rate measures the proportion of instances where LLMs pro-
vide a valid response. Accuracy evaluates the percentage of
correct answers, while conditional accuracy assesses perfor-
mance only when a valid response is given.
Ti-Safetybench
SafetyBench (Zhang and et al. 2024; Sun
et al. 2023) is a widely used benchmark that contains 11,435
multiple-choice questions across 7 distinct safety categories:
Offensiveness (OFF), Unfairness and Bias (UB), Physical
Health (PH), Mental Health (MH), Illegal Activities (IA),
Ethics and Morality (EM), and Privacy and Property
(PP). Its questions are sourced from diverse benchmarks
in Chinese and English, supplemented with safety-related
examination content and ChatGPT-augmented samples. To
evaluate safety-related capabilities for Tibetan, TLUE (Gao
et al. 2025) employed Ti-Safetybench, a Tibetan adaptation
of SafetyBench. The original data were translated and
manually validated by experts to ensure consistency with
traditional Tibetan linguistic and cultural standards. The
evaluation methodology incorporates two scoring meth-
ods: Direct Answer Calculation (DA) and Concern All
Answer Calculation (CAA). DA assesses the model’s
ability to provide valid and accurate responses, while CAA
calculates the performance ceiling by filtering valid choices
and verifying correctness after removing irrelevant combi-
nations. Both methods ensure a comprehensive assessment
of the model’s safety performance in Tibetan contexts.
Baseline Model
We compare Sun-Shine with several widely used LLMs, in-
cluding GPT-4o, GPT-4o-mini, and GPT-3.5-turbo (Achiam
et al. 2023), LLaMA-3 18B (Dubey et al. 2024; Touvron
et al. 2023), Qwen-2.5 72B (Yang and et al. 2024), and
DeepSeek-R1 (Bi and et al. 2024; Guo and et al. 2025).
LLM
Temperature
Top p
Stream
GPT-3.5-turbo
1.0
1.0
False
GPT-4o
1.0
1.0
False
GPT-o1-mini
1.0
1.0
True
DeepSeek-R1
1.0
None
True
LlaMA-3.18B
0.6
0.9
False
Qwen-2.5
0.7
0.8
False
Table 4: Hyperparameters of LLM
Detailed experimental settings and evaluation metrics for
each model are provided in Table 4. Specifically, Qwen-2.5
and DeepSeek-R1 were tested via their official APIs, while

--- Page 6 ---

(a) Response Rate
(b) Conditional Accuracy
(c) Accuracy
Figure 7: Ti-MMLU: Sun-Shine vs. other LLMs.
LLaMA-3 18B was accessed through the LLaMA-API plat-
form. All experimental configurations will be fully docu-
mented in the final version to ensure transparency and re-
producibility.
Insights from Performance Results
Ti-MMLU
As shown in Figure 7, Sun-Shine, GPT-4o and
DeepSeek-R1 outperform all other LLMs. Among them,
Sun-Shine is slightly ahead of these. For the Response Rate,
Sun-Shine and GPT-4o achieve the highest Response Rate,
with Sun-Shine leading across all sub-branches,shown in
Figure 8, demonstrating superior responsiveness to Tibetan
prompts enabled by its domain-specific training. For Con-
ditional Accuracy, Sun-Shine and DeepSeek-R1 perform
best, with the latter holding a slight advantage. Both models
maintain consistently high scores, reflecting strong general
knowledge capabilities. In terms of overall Accuracy, Sun-
Shine outperforms DeepSeek-R1 in China-Specific, STEM,
and Other categories, while DeepSeek-R1 leads in the re-
maining areas. This underscores that Sun-Shine’s strong Ti-
betan understanding stems not only from model design but
also from effective use of the TIB-STC dataset and targeted
training, allowing an 8B model to surpass the 671B MoE
DeepSeek-R1 in key tasks.
(a) The highest total number
of indicators.
(b) The second total number
of indicators.
Figure 8: Statistics of Sun-Shine ranks first and second based
on the number of indicators, across all categories of the Ti-
MMLU benchmark.
Among other LLMs, GPT-o1-mini and GPT-3.5-Turbo
show weaker performance. Qwen-2.5 surpasses LLaMA-
3.18B but falls short compared to GPT-4o, DeepSeek-R1,
and Sun-Shine. For more details, please refer to supplemen-
tary materials.
Ti-Safetybench
as shown in Figure 9, Sun-Shine was
evaluated against leading LLMs on Ti-SafetyBench across
safety-related categories using DA and CCA filtering meth-
ods. Compared to GPT-4o, LLaMA-3.18B, GPT-3.5-Turbo,
Qwen-2.5, GPT-o1-mini, and DeepSeek-R1, Sun-Shine ex-
cels in IA, OFF, UB, and MH categories, while DeepSeek-
R1 performs well under CCA. GPT-4o and GPT-3.5-Turbo
show moderate results, with LLaMA-3.18B and Qwen-2.5
scoring lower in safety metrics.
(a) LLMs Across DA
(b) LLMs Across CCA
Figure 9: Ti-SafetyBench: Sun-Shine vs. other LLMs.
Overall, Sun-Shine demonstrates slightly stronger se-
curity capabilities in Tibetan language processing than
DeepSeek-R1. While DeepSeek-R1’s base model surpasses
LLaMA-3.18B in security, Sun-Shine’s extensive pre-
training and fine-tuning, supported by the data advantage of
TIB-STC, achieve comparable performance. This not only
validates Sun-Shine’s capabilities but also underscores the
strengths of TIB-STC.
Sun-Shine for Tibetan Culture
As shown in Figure 10, Sun-Shine significantly outperforms
DeepSeek-R1 and GPT-4o in classical Chinese. This supe-
riority stems from its training on TIB-STC, which includes
ancient poems, essays, and historical records. The manual
revision process preserved Tibetan grammar, sentence struc-
ture, and style, giving Sun-Shine’s output a distinctly clas-
sical character, unlike the modern Tibetan style used by
DeepSeek-R1 and GPT-4o.
As shown in Figure 11, we observe clear stylistic dis-
tinctions in how different LLMs respond to a culturally
sensitive prompt, ”Please write a poem in praise of father”,
in Tibetan, Chinese, and English. Sun-Shine maintains a
neutral tone when addressing common questions, avoiding
exaggerated praise or references to Tibetan classics. In
contrast, GPT-4o adopts a more amplified and majestic
style, reminiscent of divine scripture, while DeepSeek-R1’s
responses frequently allude to the bodhisattva Ma˜nju´sr¯ı,
appearing slightly ”overfitted” with more refined yet
noticeably embellished language than GPT-4o. Overall,

--- Page 7 ---

Language
LLM
Tibetan
Input
ང་ཁ་བྲལ་ནས་ད་དུང་འདོད་པ་མེད།ང་ལ་ཇི་ལྟར་འགྲེལ་བརྗོད་བྱེད་དགོས་སམ།
Output (Sun-Shine)
ཁམས་གསུམ་གྱི་འཁོར་བ་དོང་ནས་ུགས་སྟེ།
Output (GPT-4o)
ཁམས་གསུམ་གྱི་འཁོར་ལོ་སྐྱེ་བ་དང་འཆི་བ་ལས་གྲོལ།
Output (DeepSeek-R1)
ཡང་སྲིད་ཀྱི་འཁོར་ལོ་ཡོངས་སུ་བཅོམ།
Chinese
Input
我超脱了，没有欲望了。怎么形容我？
Output (Sun-Shine)
戒除三界轮回
Output (GPT-4o)
三界的轮回从生死中脱离
Output (DeepSeek-R1)
彻底断除三界轮回
English
Input
I am detached and have no desires. How can I describe myself?
Output (Sun-Shine)
The cycle of the three realms is liberated from birth and death.
Output (GPT-4o)
The cycle of the three realms is freed from birth and death.
Output (DeepSeek-R1)
Completely break the cycle of reincarnation.
Figure 10: Comparison of LLM Classical Chinese Output
Sun-Shine surpasses DeepSeek-R1 and GPT-4o in most
performance indicators, with its classical Tibetan style
attributed to the curated TIB-STC and training strategy,
where human annotation and correction played a key role.
Downstream Task
Translation
we performed a downstream task, Tibetan-
Chinese translation (Chinese to Tibetan). BELU (Papineni
et al. 2002) and ROUGE (Lin 2004) are used to evaluate this
task. As shown in Table 5, Sun-Shine achieves the highest
scores across all metrics, demonstrating superior translation
capabilities, followed by DeepSeek-R1, with GPT-4o and
Qwen-2.5 scoring relatively lower. Table 10 can laso prove
this point that the generated Tibetan is closer to the ancient
style and conforms to the annotation.
LLM
BLEU-4
ROUGE-1
ROUGE-2
ROUGE-l
Sun-Shine
42.16
65.78
48.91
51.58
GPT-4o
38.85
61.12
44.33
47.02
DeepSeek-R1
41.85
65.49
47.73
51.04
Qwen-2.5
35.20
58.59
41.25
44.73
Table 5: Comparison of Translation Performance
Tibetan Language Proficiency Test
we connect these
LLMs to this test, Tibet Autonomous Region Tibetan-
Chinese Translation-20241 (100-point system). As shown in
Table 6, Sun-Shine achieves its highest performance on the
more challenging A and B exams, which contain a signif-
icant amount of ancient Tibetan content, while its perfor-
mance is comparatively lower on C and D exams that feature
more modern Tibetan content, including sensitive recent po-
litical topics. This score distribution highlights Sun-Shine’s
strong understanding of ancient Tibetan and also demon-
strates the superiority of our dataset, TIB-STC, which in-
cludes a richer collection of ancient Tibetan texts.
Conclusion
In this paper, we introduce two key contributions to Tibetan
NLP: the TIB-STC dataset and the Sun-Shine large language
model. Our primary focus is the development of TIB-STC,
the first large-scale, high-quality Tibetan corpus designed to
1http://cn.zyw.xizang.gov.cn/
LLM
A
B
C
D
Sun-Shine
63
61
44
42
GPT-4o
45
47
53
51
DeepSeek-R1
59
56
67
66
Qwen-2.5
41
43
53
54
Table 6: Comparison of Tibetan Language Proficiency Test
address the severe lack of resources in low-resource lan-
guage research. Covering diverse domains such as litera-
ture, religion, news, and dialogue, TIB-STC offers struc-
tured, culturally rich data that enables the effective train-
ing and evaluation of Tibetan language models. Leverag-
ing this dataset, we further present Sun-Shine, a language
model trained on TIB-STC, which demonstrates robust per-
formance in Tibetan-specific tasks, particularly in classical
Tibetan understanding and culturally sensitive expression.
Extensive evaluation shows that models trained on TIB-STC
outperform existing LLMs across metrics such as accuracy,
response rate, and stylistic alignment. These results vali-
date the effectiveness of TIB-STC as a foundational resource
for Tibetan NLP and highlight the critical role of culturally
grounded datasets in advancing low-resource language tech-
nologies.
Future Work
As part of our ongoing efforts, we have launched Sun-Shine
2.0, an upgraded version of our Tibetan foundation model
with enhanced reasoning capabilities. In parallel, we are cu-
rating an extended Tibetan corpus to further improve linguis-
tic and cultural coverage.
Acknowledgement
This work was supported in part by the National Natural
Science Foundation of China under Grants 62276055 and
62406062, in part by the Sichuan Science and Technology
Program under Grant 2023YFG0288, in part by the Nat-
ural Science Foundation of Sichuan Province under Grant
2024NSFSC1476, in part by the National Science and Tech-
nology Major Project under Grant 2022ZD0116100, and in
part by the Sichuan Provincial Major Science and Technol-
ogy Project under Grant 2024ZDZX0012.
References
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
Anadkat, S.; and et al. 2023. GPT-4 Technical Report. arXiv
preprint arXiv:2303.08774.
Bai, Y.; Jones, A.; Ndousse, K.; Askell, A.; Chen, A.; Das-
Sarma, N.; Drain, D.; Fort, S.; Ganguli, D.; Henighan, T.;
and et al. 2022. Training a Helpful and Harmless Assistant
with Reinforcement Learning from Human Feedback. arXiv
preprint arXiv:2204.05862.
Bi, X.; and et al. 2024.
Deepseek LLM: Scaling Open-
Source Language Models with Longtermism. arXiv preprint
arXiv:2401.02954.

--- Page 8 ---

Language
Sun-Shine
Tibetan
Input
ཁྱོད་ཀྱིས་ཨ་ཕ་ལ་བསྟོད་བསྔགས་བྱེད་པའི་སྙན་ངག་ཅིག་འབྲི་རོགས།
Output
ཨ་ཕ་ཁྱེད་ནི་སྐྱོན་བྲལ་དང་གཞུང་སྤྱོད་ཀྱི་མི་ཞིག་ཡིན།ཁྱེད་ཀྱིས་ང་ལ་རྒྱབ་སྐྱོར་དང་སློབ་སྟོན་བྱས་པར་ཐུགས་རྗེ་ཆེ།ཁྱེད་ཀྱི་དཔའ་ངར་དང་བློ་གྲོས་ལ་བ
རྟེན་ནས་ངས་སློབ་སྦྱོང་བྱས།ང་ཚོ་འགྲོ་བའི་ལམ་དུ་ཁྱེད་ཀྱིས་ནམ་ཡང་ང་ལ་སྐྱོད་ཡོད།ཁྱེད་ཀྱིས་ང་ལ་བསླབ་བྱ་གཏོང་བ་དང་ང་ཚོ་ཕན་ཚུན་གྱི་དགའཞེན
་ལ་ཉམས་མྱོང་བྱས་པ་ཡིན།ཁྱེད་ཀྱིས་ང་ལ་རྒྱབ་སྐྱོར་དང་བསྟོད་བསྔགས་བྱས་པར་ཐུགས་རྗེ་ཆེ་ཞུ་ུ་ཡིན།ཁྱེད་ཀྱིས་ང་ལ་བྱས་རྗེས་གཏོད་པ་དང་ང་ལ་
སྐྱིད་ུག་བུན་པར་ཐུགས་རྗེ་ཆེ་ཞུ།
Chinese
Input
请你写一首赞颂父亲的诗歌
Output
父亲，您是一位无瑕疵、遵纪守法的人。感谢您对我的支持和指导。依靠您的勇
气和智慧，我得以学习。在我们前进的道路上，您始终与我同行。您教导我，并
让我们之间的感情得到了历练。衷心感谢您对我的支持和赞扬。感谢您为我创造
成就，并让我经历了生活的喜怒哀乐。
English
Input
Please write a poem in praise of father
Output
Father, you are a flawless and law-abiding person. Thank you for your support
and guidance. With your courage and wisdom, I have been able to learn. As we
move forward, you have always been by my side. You have taught me and stre-
ngthened the bond between us. I sincerely appreciate your support and encour-
agement. Thank you for creating achievements for me and allowing me to exper-
ience the joys and sorrows of life.
(a) Sun-Shine
Language
GPT-4o
Tibetan
Input
ཁྱོད་ཀྱིས་ཨ་ཕ་ལ་བསྟོད་བསྔགས་བྱེད་པའི་སྙན་ངག་ཅིག་འབྲི་རོགས།
Output
ཨ་ཕ་ལ་བསྟོད་བསྔགས་ཀྱི་སྙན་ངག་ཞིག༄༅།།ཨ་ཕ་སྐྱིད་པའི་སྒྲོལ་མ་ཡིན།ཁྱེད་ཀྱིས་སྐྱིད་རྩེ་བསྐྱེད་པའི་གཏམ།རྒྱལ་བའི་བུ་བཞིན་སྐྱོད་རུང་བཞིནཨ་ཕ།
་ཡི་བྱང་ཆུབ་སྒྲོལ་མ་ཡིན།ཨ་ཕ་ཁྱེད་ཀྱིས་སྲིད་པའི་མཆོད་རྟེན་ཡིན།བདེ་སྐྱིད་སྐྱེ་བའི་འགྲམ་གྱི་འུངས།རང་བཞིན་ངན་པའི་བུར་མ་ཡིན།ཨ་ཕ་ཡི་བརྟན་པ
གྲུབ་པའི་འགྲམ།དགའ་སྟོན་རྒྱལ་མཚན་སྨོན་ལམ་ཡིན།བློ་སྒྲོན་རིག་པའི་བཀའ་དྲིན།ཨ་ཕ་ུབ་པའི་འོད་ཟེར་ཡིན།ཁྱེད་ཀྱིས་འུངས་བདེ་སྨོན་ཚིག་ཡིན།ཨ་ཕ།
ཁྱེད་ལ་ཕན་ཐོགས་ཀྱི་རྒྱལ་ཡབ་འདུད།།ཨ་ཕ་ཡི་རྒྱལ་བའི་མཆོད་གཉིས་དུས་སྔགས།
Chinese
Input
请你写一首赞颂父亲的诗歌
Output
父亲啊，您是幸福的救星。您创造欢乐的故事，如同胜利者的儿子般前行。父亲的
觉悟是我的救赎。父亲啊，您是尘世的丰碑。在幸福的边缘诞生，不是卑劣本性的
比较。父亲坚定的成就是我的道路。欢庆的旗帜是我的祝福。智慧之光是您的恩惠
。父亲是修行的光芒。您赋予我生命的美好祝福。向父亲致以有益的敬意。父亲的
胜利在两个时代被歌颂。
English
Input
Please write a poem in praise of father
Output
Father, you are the liberator of happiness. Your tales of joy, moving like a vict-
orious son’s path. Father’s enlightenment is my salvation. Father, you are the
monument of existence. Born on the edge of happiness, not a comparison of base
nature. Father’s steadfast achievement is my path. The victory banner is my
prayer. Wisdom’s light is your grace. Father is the ray of practice. You bes-
tow life’s beautiful blessing. Offering beneficial reverence to my father. Father
’s victory is praised across two eras.
(b) GPT-4o
Language
DeepSeek-R1
Tibetan
Input
ཁྱོད་ཀྱིས་ཨ་ཕ་ལ་བསྟོད་བསྔགས་བྱེད་པའི་སྙན་ངག་ཅིག་འབྲི་རོགས།
Output
གངས་རིའི་ཁྲོད་དུ་སྟོབས་ལྡན་དུ་སྐྱེས་པའི་ཁྱེད་ནི་ཉི་མ་ལྟར་སྲ་ཞིང་བརྟན་པའི་བང་མཛོད་ཅིག་དང་ངའི་མི་ཚེའི་ལམ་སྟོན་བྱེད་པའི་སྒོ་མོ་མཛེས་པོ་ཞིག་ད
ང་ཆུ་བོ་ལྟར་ཡབ་ཀྱི་ཐུགས་རྗེའི་མཐའ་བསྐོར་ཡོད།ཁྱེད་ཀྱིས་འདས་པ་དང་ད་ལྟ་དང་མ་འོངས་པའི་ནམ་མཁའི་ཡོན་ཏན་བསྟན་ཡོད།ངའི་མགོ་ཐོག་གི
་བང་མཛོད་ཀྱི་མེ་ལོང་ནང་དུ་མཐོང་བ་ལྟར།ངའི་ཨ་ཕའི་སྙིང་རྗེ་ཟླ་བ་ལྟར་གསལ་པོ་ཡོད།ཁོང་གི་ཤེས་རབ་ཀྱི་སྟོབས་ཤུགས་ས་གཞི་ལྟར་བརྟན་པོ་ཡོད།
ཁྱེད་ཀྱིས་ངའི་བློ་ཁོག་སྐྱེས་ཡོད།ཁྱེད་ནི་དཀའ་ུག་གི་དུས་སུ་ངའི་མགོན་སྐྱབས་ཡིན།ཁྱེད་ཀྱིས་ུག་བསྔལ་གྱི་མུན་པ་སེལ་བར་བྱེད།དེ་རིང་ངས་མ
ཆོད་པའི་མེ་ཏོག་འདི་འབུལ།གུས་ཞབས་དང་བཅས་ཁྱེད་ཀྱི་རྐང་འོག་ཏུ་བཞགཡབ་ཁྱོད་དུས་རྟག་ཏུ་ཞི་བདེ་ལོངས་སུ་སྤྱོད་པར་ཤོག།ཐུགས་སྨོན་ཐམ
ས་ཅད་འགྲུབ་པར་ཤོག།བདག་གི་སེམས་ཁྱོད་དང་གཅིག་ུར་ཅིགུ་ཚེ་རིང་བའི་ཆོས་ཀྱི་དཔལ་ལ་བརྟེན་པར་ཤོག།མཇུག་སྡོམཁྱེད་ཀྱི་བྱམས་བ
རྩེ་གངས་རི་ལས་ཀྱང་མཐོ་ཞིང་སྙིང་རྗེའི་ཆུ་བོ་རྒྱ་མཚོ་ལས་ཀྱང་གཏིང་ཟབ་པས་ཁྱེད་ཀྱིས་ང་ཚོའི་སྟོང་བའི་སེམས་པ་བཀང་ནས་ནམ་ཡང་བརྗེད་མི་སྲིད།
Chinese
Input
请你写一首赞颂父亲的诗歌
Output
在雪山中诞生的强健的您，如同阳光般坚定的宝库，指引我人生道路的美丽之门，
父亲的慈悲如河水般环绕。您展示了过去现在未来的天空特质，不惧动荡之风的
坚固基座，如花朵般绽放我的欢喜，您的恩德如同天空的明点。从头顶珍宝的明
镜中所见，父亲的慈悲如月亮般清晰，智慧的威力如大地般稳固，您孕育着我的
勇气。在困难时刻您是我的依怙主，您驱散忧愁的黑暗，今日我献上这供养之花，
恭敬地献于您的足下。父亲啊，愿您常享安乐，愿心中愿望如意实现，依托长寿
教法的荣耀，愿我的心与您融为一体。结语您的恩德高过雪山，慈悲之河深过海
洋，您填满了我们空虚的心，永远难以忘怀。
English
Input
Please write a poem in praise of father
Output
A Poem in Praise of Manjushri’s Father”Born among snow mountains, you the
strong one, Like sunlight, a treasury of steadfastness, Beautiful gateway guiding
my life’s path, Father’s compassion flows like a river.You show the distinctions
of the three times’ sky, Firm seat unafraid of shifting winds, Like flowers my joy
blooms, Your kindness is like a dot in the sky.Seen from the precious mirror at
the crown, Father’s compassion clear like the moon, Wisdom’s power steady like
the earth, You
(c) DeepSeek-R1
Figure 11: Ancient Poetry Writing: Sun-Shine vs. other LLMs
Blodgett, S. L.; Barocas, S.; III, H. D.; and Wallach, H.
2020. Language (Technology) is Power: A Critical Survey
of ‘Bias’ in NLP. In Proceedings of the 58th Annual Meet-
ing of the Association for Computational Linguistics (ACL),
5454–5476.
Brown, T. B.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J.;
Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell,
A.; and et al. 2020. Language Models are Few-Shot Learn-
ers. In Proceedings of the 34th International Conference
on Neural Information Processing Systems (NeurIPS), 1–25.
Red Hook, NY, USA: Curran Associates Inc.
Chao, P.; Debenedetti, E.; Robey, A.; Andriushchenko, M.;
Croce, F.; Sehwag, V.; Dobriban, E.; Flammarion, N.; Pap-
pas, G. J.; Tram`er, F.; Hassani, H.; and Wong, E. 2024.
JailbreakBench: An Open Robustness Benchmark for Jail-
breaking Large Language Models. In NeurIPS Datasets and
Benchmarks Track.
Dubey, A.; Jauhri, A.; Pandey, A.; Kadian, A.; Al-Dahle, A.;
Letman, A.; Mathur, A.; Schelten, A.; Yang, A.; Fan, A.; and
et al. 2024. The LLaMA 3 Herd of Models. arXiv preprint
arXiv:2407.21783.
Gao, F.; Huang, C.; Tashi, N.; Wang, X.; Tashi, T.; Ma-
bao, B.; Duojie, R.; Luosang, G.; Dongrub, R.; Tashi, D.;
and et al. 2025. TLUE: A Tibetan Language Understanding
Evaluation Benchmark. arXiv preprint arXiv:2503.12051.
GLM, T.; Zeng, A.; Xu, B.; Wang, B.; Zhang, C.; Yin,
D.; Rojas, D.; Feng, G.; Zhao, H.; Lai, H.; and et al.
2024.
ChatGLM: A Family of Large Language Models
from GLM-130B to GLM-4 All Tools.
arXiv preprint
arXiv:2406.12793.
Guo, D.; and et al. 2025. Deepseek-r1: Incentivizing Rea-
soning Capability in LLMs via Reinforcement Learning.
arXiv preprint arXiv:2501.12948.
Hu, E. J.; Wallis, P.; Allen-Zhu, Z.; Li, Y.; Wang, S.; Wang,
L.; Chen, W.; and et al. 2021. LoRA: Low-Rank Adaptation
of Large Language Models. In Proceedings of the Interna-
tional Conference on Learning Representations (ICLR).
Khysru, K.; Jin, D.; Huang, Y.; Feng, H.; and Dang, J. 2021.
A Tibetan Language Model That Considers the Relationship
Between Suffixes and Functional Words. IEEE Signal Pro-
cessing Letters, 28: 459–463.
Kirk, R.; Mediratta, I.; Nalmpantis, C.; Luketina, J.; Ham-
bro, E.; Grefenstette, E.; and Raileanu, R. 2024.
Under-
standing the Effects of RLHF on LLM Generalisation and
Diversity. In Proceedings of the 12th International Confer-
ence on Learning Representations (ICLR).
Li, H.; Zhang, Y.; Koto, F.; Yang, Y.; Zhao, H.; Gong, Y.;
Duan, N.; and Baldwin, T. 2024. CMMLU: Measuring Mas-
sive Multitask Language Understanding in Chinese. In Find-
ings of the Association for Computational Linguistics: ACL
2024, 11260–11285.
Liang, Y.; Lv, H.; Li, Y.; Duo, L.; Liu, C.; and Zhou,
Q. 2024.
Tibetan-BERT-wwm: A Tibetan Pretrained
Model with Whole Word Masking for Text Classification.
IEEE Transactions on Computational Social Systems, 11(5):
6268–6277.
Lin, C.-Y. 2004. ROUGE: A Package for Automatic Evalu-
ation of Summaries. In Proceedings of the Workshop on Text
Summarization Branches Out (WAS 2004), 74–81.
Liu, Y.; Shen, J.; Yu, Y.; Ma-Bao, B.; Tsering, T.; Wang, X.;
Huang, C.; and Tashi, N. 2024. Tibetan Syllable Component
Recognization with Memristor. In 2024 International Con-
ference on Neuromorphic Computing (ICNC), 1–6. IEEE.
Liu, Y.; Xiao, F.; Zhang, Z.; Yu, Y.; Huang, C.; Gao, F.;
Wang, X.; and et al. 2025a.
TiSpell: A Semi-Masked
Methodology for Tibetan Spelling Correction Covering
Multi-Level Error with Data Augmentation. arXiv preprint
arXiv:2505.08037.
Liu, Y.; Zhang, Z.; Ma-bao, B.; Cai, Y.; Yu, Y.; Duo-
jie, R.; Wang, X.; Gao, F.; Huang, C.; and Tashi, N.
2025b.
FMSD-TTS: Few-Shot Multi-Speaker Multi-
Dialect Text-to-Speech Synthesis for ”U-Tsang, Amdo
and Kham” Speech Dataset Generation.
arXiv preprint
arXiv:2505.14351.
Minaee, S. M.; Mikolov, T.; Nikzad, N.; Chenaghlu, M.;
Socher, R.; Amatriain, X.; and Gao, J. 2024. Large Lan-
guage Models: A Survey. arXiv preprint arXiv:2402.06196.
Moore, J.; Deshpande, T.; and Yang, D. 2024. Are Large
Language Models Consistent over Value-Laden Questions?
In Findings of the Association for Computational Linguis-
tics: EMNLP 2024, 15185–15221. Miami, Florida, USA.
Papineni, K.; Roukos, S.; Ward, T.; and Zhu, W.-J. 2002.
BLEU: A Method for Automatic Evaluation of Machine

--- Page 9 ---

Translation. In Proceedings of the 40th Annual Meeting of
the Association for Computational Linguistics (ACL), 311–
318.
Rafailov, R.; Sharma, A.; Mitchell, E.; Manning, C. D.; Er-
mon, S.; and Finn, C. 2024. Direct Preference Optimization:
Your Language Model is Secretly a Reward Model.
Ad-
vances in Neural Information Processing Systems, 36.
Rozen, N.; Elidan, G.; Globerson, A.; and Ben-David, E.
2024. Do LLMs Have Consistent Values? CoRR.
Sun, H.; Zhang, Z.; Deng, J.; Cheng, J.; and Huang, M.
2023. Safety Assessment of Chinese Large Language Mod-
els. arXiv preprint arXiv:2304.10436.
Taori, R.; Gulrajani, I.; Zhang, T.; Dubois, Y.; Li, X.;
Guestrin, C.; Liang, P.; and Hashimoto, T. B. 2023a. Al-
paca: A Strong, Replicable Instruction-Following Model.
https://crfm.stanford.edu/2023/03/13/alpaca.html.
Taori, R.; Gulrajani, I.; Zhang, T.; Dubois, Y.; Li, X.;
Guestrin, C.; Liang, P.; and Hashimoto, T. B. 2023b. Stan-
ford Alpaca: An Instruction-Following LLaMA Model.
https://github.com/tatsu-lab/stanford alpaca.
Touvron, H.; Lavril, T.; Izacard, G.; Martinet, X.; Lachaux,
M.-A.; Lacroix, T.; Rozi`ere, B.; Goyal, N.; Hambro, E.;
Azhar, F.; and et al. 2023.
LLaMA: Open and Ef-
ficient Foundation Language Models.
arXiv preprint
arXiv:2302.13971.
UCLA International Institute. 2014.
Tibetan Language
and Education in China. https://www.international.ucla.edu/
asia/article/149245. Accessed: Jan. 7, 2025.
¨Ust¨un, A.; Aryabumi, V.; Yong, Z.; Ko, W.-Y.; D’souza, D.;
Onilude, G.; Bhandari, N.; Singh, S.; Ooi, H.-L.; Kayid, A.;
and et al. 2024. Aya Model: An Instruction Finetuned Open-
Access Multilingual Language Model.
In Proceedings of
the 62nd Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), 15894–15939.
Bangkok, Thailand.
Wang, H.; Liu, C.; Xi, N.; Qiang, Z.; Zhao, S.; Qin, B.; and
Liu, T. 2023. Huatuo: Tuning LLaMA Model with Chinese
Medical Knowledge. arXiv preprint arXiv:2304.06975.
Xu, G.; Liu, J.; Yan, M.; Xu, H.; Si, J.; Zhou, Z.; Yi, P.;
Gao, X.; Sang, J.; Zhang, R.; Zhang, J.; Peng, C.; Huang, F.;
and Zhou, J. 2023. CValues: Measuring the Values of Chi-
nese Large Language Models from Safety to Responsibility.
arXiv preprint arXiv:2307.09705.
Yang, A.; and et al. 2024. Qwen2 Technical Report. arXiv
preprint arXiv:2407.10671.
Yu, Y.; Zuo, S.; Jiang, H.; Ren, W.; Zhao, T.; and Zhang,
C. 2021.
Fine-Tuning Pre-Trained Language Model with
Weak Supervision: A Contrastive-Regularized Self-Training
Approach. In Proceedings of the 2021 Conference of the
North American Chapter of the Association for Computa-
tional Linguistics: Human Language Technologies (NAACL-
HLT), 1063–1077.
Zhang, Z.; and et al. 2024.
SafetyBench: Evaluating the
Safety of Large Language Models. In Proceedings of the
62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 15537–15553.
Zheng, C.; Yin, F.; Zhou, H.; Meng, F.; Zhou, J.; Chang,
K.-W.; Huang, M.; and Peng, N. 2024. On Prompt-Driven
Safeguarding for Large Language Models. In Proceedings of
the International Conference on Machine Learning (ICML).

--- Page 10 ---

Supplementary Material
Note: S-S = Sun-Shine; G-4o = GPT-4o; L-318B = Llama-
3.18B; G-35T = GPT-3.5-Turbo; Q-2.5 = Qwen-2.5; Go1-m
= GPT-o1-mini; DK-r1 = DeepSeek-r1.
Details of Response Rate
Category
Response Rate
S-S
G-4o
L-318
G-35T
Q-2.5
Go1-m
DK-r1
ancient chinese
0.5366
0.4695
0.1402
0.0732
0.2500
0.2317
0.3232
chinese civil service exam
0.4938
0.4062
0.1688
0.0438
0.2312
0.1000
0.3812
chinese food culture
0.5588
0.5147
0.1250
0.0809
0.2279
0.1765
0.4191
chinese foreign policy
0.5206
0.4981
0.3458
0.0093
0.2804
0.1589
0.4579
chinese teacher qualification
0.5972
0.6089
0.2682
0.0726
0.2458
0.3073
0.4078
elementary chinese
0.5238
0.4167
0.1667
0.0556
0.2817
0.1667
0.4683
ethnology
0.5481
0.5037
0.1852
0.0963
0.3259
0.2148
0.6148
high school politics
0.5105
0.4955
0.1888
0.0979
0.2098
0.1748
0.4685
modern chinese
0.5431
0.5241
0.1724
0.0862
0.2069
0.2328
0.3707
chinese literature
0.6127
0.5412
0.1618
0.0833
0.2892
0.2500
0.5000
chinese history
0.5635
0.4489
0.1672
0.0526
0.2632
0.1734
0.3839
chinese driving rule
0.5198
0.4420
0.1985
0.0687
0.2519
0.2595
0.3817
construction project management
0.6619
0.4388
0.1942
0.0647
0.2662
0.2230
0.3453
elementary commonsense
0.5404
0.5354
0.1414
0.0758
0.2828
0.1465
0.4848
traditional chinese medicine
0.5459
0.5405
0.2378
0.0703
0.2324
0.2595
0.3027
business ethics
0.5359
0.5167
0.2057
0.0574
0.2919
0.2249
0.3780
economics
0.5283
0.4465
0.2767
0.0440
0.2516
0.1824
0.3396
education
0.5460
0.5215
0.1840
0.0920
0.2761
0.3129
0.4049
college education
0.5981
0.5234
0.2336
0.1589
0.4299
0.2617
0.4673
journalism
0.5947
0.5447
0.1744
0.0407
0.3256
0.2209
0.4826
marketing
0.6556
0.5944
0.2278
0.0889
0.2667
0.3500
0.2389
professional accounting
0.6114
0.5829
0.1829
0.0800
0.1943
0.2400
0.3714
professional psychology
0.5645
0.5303
0.2198
0.0819
0.1940
0.2586
0.3578
public relations
0.5920
0.5172
0.1437
0.0862
0.2299
0.2931
0.4598
security study
0.5704
0.4963
0.1630
0.1185
0.4074
0.3037
0.4000
high school geography
0.5678
0.4831
0.2712
0.0678
0.3305
0.1780
0.4237
management
0.5905
0.5857
0.2524
0.0857
0.2429
0.3190
0.3810
sociology
0.5442
0.5177
0.1991
0.0442
0.2832
0.3319
0.3805
marxist theory
0.6085
0.5556
0.2804
0.0529
0.3122
0.2804
0.4497
college law
0.4648
0.4519
0.2315
0.0833
0.2870
0.2500
0.3981
global facts
0.5235
0.4930
0.2282
0.0738
0.3423
0.2349
0.4027
international law
0.5568
0.5081
0.2270
0.0595
0.3351
0.2541
0.0919
jurisprudence
0.5377
0.5109
0.3187
0.0681
0.3358
0.2409
0.3869
world religions
0.5000
0.4938
0.1125
0.0938
0.2625
0.1812
0.4688
logical
0.5366
0.4715
0.1463
0.0976
0.2195
0.2195
0.2846
professional law
0.5071
0.4882
0.2654
0.0474
0.2180
0.2180
0.3033
philosophy
0.5524
0.4667
0.2476
0.0952
0.2190
0.2286
0.0476
world history
0.5342
0.4907
0.2174
0.0683
0.3354
0.2298
0.4720
arts
0.0750
0.5437
0.1500
0.1000
0.2375
0.2125
0.4500
electrical engineering
0.5698
0.5349
0.2035
0.1337
0.2965
0.2384
0.3663
actuarial science
0.3692
0.1887
0.1698
0.1792
0.0642
0.1038
0.5000
engineering hydrology
0.5755
0.5377
0.2170
0.0660
0.3113
0.3208
0.5189
genetics
0.5455
0.4830
0.1932
0.0795
0.1648
0.1761
0.2216
astronomy
0.5758
0.4606
0.2424
0.0727
0.1455
0.2182
0.3879
college mathematics
0.5048
0.3238
0.2095
0.1429
0.1619
0.1524
0.1429
college medical statistics
0.6038
0.5094
0.1698
0.0566
0.1792
0.1887
0.0660
virology
0.5680
0.5089
0.1479
0.0414
0.1893
0.2899
0.2071
computer science
0.5686
0.4216
0.1961
0.0882
0.1225
0.1814
0.2696
conceptual physics
0.5986
0.5918
0.3878
0.0340
0.1565
0.2925
0.2109
anatomy
0.6622
0.5203
0.2027
0.0676
0.1689
0.2635
0.2905
machine learning
0.5656
0.4754
0.1967
0.0574
0.1639
0.1393
0.2951
high school physics
0.6364
0.5455
0.1909
0.0727
0.2455
0.2198
0.3415
high school mathematics
0.5915
0.2317
0.1646
0.2012
0.1341
0.1098
0.3415
high school chemistry
0.5758
0.3409
0.2955
0.0682
0.1591
0.1288
0.0985
high school biology
0.6746
0.4852
0.2604
0.0828
0.1657
0.2249
0.0947
elementary mathematics
0.5996
0.3870
0.1913
0.1565
0.1696
0.1478
0.5478
legal and moral basis
0.5748
0.5561
0.2523
0.0888
0.3131
0.2523
0.5514
computer security
0.5789
0.5088
0.2398
0.1053
0.2105
0.2339
0.2164
food science
0.4895
0.4705
0.1469
0.0909
0.2587
0.1818
0.3077
college medicine
0.4982
0.4908
0.2674
0.0366
0.1722
0.1538
0.1758
clinical knowledge
0.5738
0.4557
0.1899
0.1013
0.2447
0.2616
0.1308
professional medicine
0.5798
0.5505
0.3165
0.0771
0.2527
0.2287
0.2074
human sexuality
0.5635
0.5317
0.2302
0.0317
0.2778
0.2143
0.3651
agronomy
0.5621
0.5089
0.1775
0.0651
0.2071
0.2485
0.4201
sports science
0.6424
0.5697
0.2000
0.0909
0.2848
0.2667
0.3879
nutrition
0.5586
0.4759
0.1862
0.0621
0.1172
0.2414
0.2552
elementary IT
0.5462
0.5378
0.2353
0.1050
0.1975
0.2353
0.2647
Table 7: Response Rate: Sun-Shine vs. Other LLMs
Details of Conditional Accuracy
Category
Conditional Accuracy
S-S
G-4o
L-318
G-35T
Q-2.5
Go1-m
DK-r1
ancient chinese
0.2697
0.2500
0.2174
0.2500
0.2195
0.2812
0.2500
chinese civil service exam
0.2562
0.2152
0.2222
0.1429
0.3243
0.2368
0.2658
chinese food culture
0.3258
0.3143
0.3529
0.2727
0.3226
0.2143
0.3171
chinese foreign policy
0.3444
0.3438
0.2973
0.0000
0.2667
0.3235
0.3448
chinese teacher qualification
0.2921
0.2752
0.1667
0.3077
0.3636
0.2571
0.2650
elementary chinese
0.3126
0.2813
0.2857
0.4286
0.2958
0.2533
0.3145
ethnology
0.3719
0.4109
0.2400
0.2308
0.3864
0.3333
0.5714
high school politics
0.3662
0.3225
0.2963
0.2143
0.1667
0.2174
0.3412
modern chinese
0.3592
0.3265
0.2000
0.4000
0.1250
0.1852
0.3489
chinese literature
0.2980
0.2000
0.3030
0.1765
0.3220
0.3077
0.2879
chinese history
0.3407
0.2552
0.2778
0.2941
0.2353
0.2418
0.2543
chinese driving rule
0.3299
0.2764
0.1923
0.1111
0.2424
0.3247
0.3721
construction project management
0.3470
0.2951
0.2593
0.2222
0.2162
0.2292
0.3253
elementary commonsense
0.3017
0.2925
0.2500
0.4667
0.1964
0.2759
0.2654
traditional chinese medicine
0.2971
0.2100
0.2045
0.2308
0.3023
0.2738
0.2912
business ethics
0.3981
0.3411
0.2791
0.3333
0.2623
0.2391
0.3802
economics
0.3597
0.3476
0.2955
0.2857
0.1500
0.3341
0.3254
education
0.3667
0.3421
0.3647
0.2667
0.3111
0.1818
0.3845
college education
0.3125
0.2143
0.3600
0.2353
0.2174
0.2857
0.3478
journalism
0.2981
0.2366
0.2667
0.2857
0.2679
0.2281
0.3098
marketing
0.3768
0.3051
0.2683
0.2500
0.3750
0.3541
0.3254
professional accounting
0.3748
0.3084
0.3438
0.5714
0.2647
0.3451
0.3746
professional psychology
0.3985
0.2823
0.2157
0.3158
0.3333
0.3698
0.3945
public relations
0.2427
0.1889
0.3600
0.1333
0.2250
0.2845
0.4752
security study
0.2997
0.3333
0.3182
0.3125
0.3636
0.2258
0.3977
high school geography
0.4179
˘0.2807
0.2188
0.1250
0.2308
0.2368
0.3627
management
0.3089
0.2913
0.2264
0.3333
0.2941
0.3154
0.5369
sociology
0.3333
0.2997
0.2889
0.1000
0.1562
0.2062
0.3221
marxist theory
0.3217
0.3143
0.2453
0.1000
0.2712
0.3210
0.3212
college law
0.3287
0.2842
0.2800
0.2222
0.2258
0.2165
0.3109
global facts
0.3636
0.3599
0.3235
0.0909
0.2353
0.3000
0.3611
international law
0.3830
0.2524
0.2381
0.3636
0.2903
0.2714
0.3799
jurisprudence
0.3258
0.2667
0.2519
0.2857
0.2754
0.2786
0.3299
world religions
0.5975
0.2911
0.2222
0.2667
0.2857
0.2143
0.6475
logical
0.2931
0.2879
0.2778
0.2500
0.2593
0.2849
0.3648
professional law
0.3178
0.2223
0.1786
0.2000
0.2609
0.2865
0.3802
philosophy
0.3276
0.2429
0.2308
0.3000
0.3478
0.3169
0.3057
world history
0.5658
0.2907
0.2286
0.5455
0.3148
0.3267
0.4407
arts
0.2759
0.2500
0.3333
0.4375
0.3684
0.2157
0.2453
electrical engineering
0.3349
0.3478
0.3114
0.1304
0.2745
0.2456
0.2857
engineering hydrology
0.3684
0.1148
0.1304
0.5714
0.2121
0.2500
0.4730
astronomy
0.3903
0.2237
0.2750
0.3750
0.3333
0.2111
0.3699
medical statistics
0.2978
0.2656
0.2222
0.5000
0.2105
0.3636
0.3026
computer science
0.4013
0.2845
0.2500
0.2778
0.3600
0.3966
0.3923
conceptual physics
0.2729
0.2473
0.2712
0.2000
0.2174
0.2632
0.2799
anatomy
0.2410
0.2338
0.1333
0.2000
0.2000
0.1667
0.2367
machine learning
0.2319
0.2241
0.2083
0.1429
0.2000
0.2498
0.2729
high school physics
0.2667
0.1857
0.1429
0.1250
0.2593
0.2441
0.6366
high school mathematics
0.6667
0.5000
0.3333
0.4500
0.5268
0.5246
0.5241
high school chemistry
0.2667
0.1974
0.3590
0.1111
0.2857
0.2459
0.3636
high school biology
0.3171
0.2544
0.2727
0.5000
0.2500
0.2321
0.3295
elementary mathematics
0.3146
0.2519
0.2273
0.2778
0.4615
0.2830
0.2941
actuarial science
0.3400
0.2500
0.4444
0.1579
0.3214
0.2800
0.4737
genetics
0.2941
0.2555
0.3529
0.2143
0.3793
0.3011
0.3582
college mathematics
0.5882
0.2642
0.2727
0.2000
0.4941
0.1905
0.4896
virology
0.2083
0.1744
0.1200
0.4286
0.2188
0.3094
0.2157
legal and moral basis
0.3821
0.3277
0.2963
0.1579
0.3284
0.2436
0.3684
computer security
0.3223
0.2848
0.3171
0.1667
0.3167
0.2750
0.3033
food science
0.3914
0.3824
0.1905
0.2308
0.2703
0.2250
0.4154
college medicine
0.3134
0.2500
0.2055
0.2000
0.2128
0.2022
0.3326
clinical knowledge
0.3448
0.3088
0.2222
0.3333
0.3426
0.2143
0.3248
professional medicine
0.2431
0.2222
0.2605
0.3448
0.2737
0.2569
0.3433
human sexuality
0.3134
0.3099
0.1726
0.7500
0.3714
0.3174
0.2989
agronomy
0.2791
0.2558
0.2667
0.0909
0.3714
0.2188
0.2626
sports science
0.4171
0.2666
0.3936
0.2667
0.4465
0.2969
0.3830
nutrition
0.2319
0.2222
0.1481
0.2222
0.2941
0.3833
0.4412
elementary IT
0.3185
0.3906
0.2500
0.3600
0.2128
0.2874
0.3452
Table 8: Conditional Accuracy: Sun-Shine vs. Other LLMs

--- Page 11 ---

Details of Accuracy
Category
Accuracy
S-S
G-4o
L-318
G-35T
Q-2.5
Go1-m
DK-r1
ancient chinese
0.1341
0.1220
0.3050
0.0183
0.0549
0.0549
0.1159
chinese civil service exam
0.1062
0.1000
0.0375
0.0062
0.0750
0.0025
0.1562
chinese food culture
0.1765
0.1618
0.0441
0.0221
0.0735
0.0294
0.1838
chinese foreign policy
0.2056
0.2028
0.1028
0.0000
0.0748
0.0654
0.1869
chinese teacher qualification
0.1676
0.1553
0.0447
0.0223
0.0894
0.0503
0.2458
elementary chinese
0.1866
0.1695
0.0476
0.0238
0.0833
0.0397
0.1865
ethnology
0.2296
0.2456
0.0444
0.0222
0.1259
0.0519
0.3333
high school politics
0.1738
0.1834
0.0559
0.0210
0.0350
0.0210
0.2098
modern chinese
0.1897
0.1654
0.0345
0.0345
0.0259
0.0603
0.1466
chinese literature
0.1765
0.1882
0.0490
0.0147
0.0931
0.0686
0.1961
chinese history
0.1920
0.1146
0.0464
0.0155
0.0619
0.0372
0.1238
chinese driving rule
0.1676
0.1492
0.0382
0.0076
0.0611
0.0763
0.1985
construction project management
0.2230
0.1295
0.0504
0.0144
0.0576
0.0504
0.1727
elementary commonsense
0.1966
0.1714
0.0354
0.0354
0.0556
0.0354
0.2424
traditional chinese medicine
0.1568
0.1323
0.0486
0.0162
0.0703
0.0703
0.0973
business ethics
0.2057
0.1852
0.0574
0.0191
0.0766
0.0478
0.1914
economics
0.1195
0.1195
0.0818
0.0126
0.0377
0.0252
0.1824
education
0.1865
0.1795
0.0675
0.0245
0.0859
0.0613
0.1779
college education
0.1867
0.2100
0.0741
0.0374
0.0935
0.1028
0.2056
journalism
0.1829
0.1676
0.0465
0.0116
0.0872
0.0640
0.2035
marketing
0.1833
0.2000
0.0611
0.0222
0.1000
0.1167
0.1667
professional accounting
0.1886
0.1714
0.0629
0.0457
0.0514
0.0629
0.1523
professional psychology
0.1897
0.1736
0.0474
0.0259
0.0647
0.0690
0.1681
public relations
0.1437
0.0977
0.0517
0.0115
0.0517
0.0862
0.1389
security study
0.1333
0.2222
0.0519
0.0370
0.1481
0.0593
0.1259
high school geography
0.1356
0.2333
0.0593
0.0085
0.0763
0.0508
0.2034
management
0.1810
0.1695
0.0571
0.0286
0.0714
0.1163
0.2143
sociology
0.1593
0.1726
0.0575
0.0044
0.0442
0.0619
0.1681
marxist theory
0.1957
0.1799
0.0688
0.0053
0.0847
0.0741
0.2222
college law
0.1574
0.1222
0.0648
0.0185
0.0648
0.0833
0.1759
global facts
0.1822
0.1621
0.0738
0.0067
0.0805
0.0671
0.1409
international law
0.1405
0.1965
0.0541
0.0216
0.0973
0.0595
0.0270
jurisprudence
0.1405
0.1998
0.0803
0.0195
0.0925
0.0706
0.1752
world religions
0.1437
0.1188
0.0250
0.0250
0.0750
0.0312
0.2750
logical
0.1546
0.1382
0.0407
0.0244
0.0569
0.0813
0.1220
professional law
0.1611
0.1009
0.0474
0.0095
0.0569
0.0474
0.0758
philosophy
0.0667
0.1810
0.0571
0.0286
0.0762
0.0571
0.0095
world history
0.1543
0.1304
0.0497
0.0373
0.1056
0.0807
0.1577
arts
0.1880
0.1500
0.5000
0.0438
0.0875
0.0438
0.1750
electrical engineering
0.1429
0.1190
0.0581
0.0174
0.0814
0.0523
0.2209
engineering hydrology
0.1981
0.1799
0.0283
0.3770
0.0660
0.0755
0.1792
astronomy
0.1273
0.1030
0.0667
0.0242
0.0545
0.0970
0.1697
medical statistics
0.1604
0.1415
0.0377
0.0283
0.0377
0.0472
0.0283
computer science
0.1618
0.1275
0.0049
0.0245
0.0441
0.0441
0.1127
conceptual physics
0.1497
0.1361
0.1020
0.0068
0.0340
0.0748
0.1224
anatomy
0.2230
0.1216
0.0270
0.0135
0.0338
0.0405
0.0878
machine learning
0.1311
0.1000
0.0410
0.0082
0.0328
0.0328
0.1066
high school physics
0.1818
0.1964
0.0273
0.0091
0.0636
0.0455
0.2091
high school mathematics
0.1182
0.1453
0.0549
0.0549
0.1341
0.0671
0.2378
high school chemistry
0.1136
0.0970
0.1061
0.0076
0.0455
0.0682
0.0303
high school biology
0.1716
0.1534
0.0710
0.0414
0.0414
0.0651
0.0178
elementary mathematics
0.1432
0.1217
0.0435
0.0435
0.0783
0.0478
0.1139
actuarial science
0.0755
0.0472
0.0755
0.0283
0.0849
0.0660
0.2453
genetics
0.1307
0.1403
0.0682
0.0170
0.0625
0.0739
0.0625
college mathematics
0.1333
0.0952
0.0571
0.0286
0.0952
0.0286
0.0762
virology
0.1183
0.0888
0.0178
0.0178
0.0414
0.1183
0.0769
legal and moral basis
0.2182
0.2022
0.0748
0.0140
0.1028
0.0654
0.3411
computer security
0.2047
0.1579
0.0076
0.0175
0.0877
0.0877
0.1228
food science
0.1366
0.1936
0.0280
0.0210
0.0699
0.0140
0.1329
college medicine
0.1538
0.1245
0.0549
0.0073
0.0366
0.0366
0.0623
clinical knowledge
0.1772
0.1565
0.0422
0.0338
0.0844
0.0591
0.0549
professional medicine
0.1410
0.1230
0.0824
0.0266
0.0691
0.0718
0.0691
human sexuality
0.1746
0.1667
0.0397
0.0238
0.1032
0.0635
0.1667
agronomy
0.1420
0.1302
0.0473
0.0059
0.0769
0.0533
0.2071
sports science
0.2242
0.2189
0.0727
0.0242
0.1091
0.0788
0.1333
nutrition
0.1241
0.1103
0.0276
0.0138
0.0345
0.0759
0.1034
elementary IT
0.1092
0.2102
0.0588
0.0378
0.0420
0.0798
0.1387
Table 9: Accuracy: Sun-Shine vs. Other LLMs

```
