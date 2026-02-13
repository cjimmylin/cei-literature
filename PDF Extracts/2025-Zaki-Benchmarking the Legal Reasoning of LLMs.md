---
title: "2025-Zaki-Benchmarking the Legal Reasoning of LLMs - PDF Extract"
source_pdf: "2025-Zaki-Benchmarking the Legal Reasoning of LLMs.pdf"
pages: 6
extracted_at: "2026-02-13T09:15:43.764095"
---

# PDF Extract: 2025-Zaki-Benchmarking the Legal Reasoning of LLMs

**Source PDF:** 2025-Zaki-Benchmarking the Legal Reasoning of LLMs.pdf
**Total Pages:** 6

---

## Content

```
--- Page 1 ---

Benchmarking the Legal Reasoning of LLMs in Arabic Islamic Inheritance
Cases
Nouar AlDahoul
Computer Science Department
New York University
Abu Dhabi, UAE
nouar.aldahoul@nyu.edu
Yasir Zaki
Computer Science Department
New York University
Abu Dhabi, UAE
yasir.zaki@nyu.edu
Abstract
Islamic inheritance domain holds significant
importance for Muslims to ensure fair distri-
bution of shares between heirs. Manual calcu-
lation of shares under numerous scenarios is
complex, time-consuming, and error-prone. Re-
cent advancements in Large Language Models
(LLMs) have sparked interest in their potential
to assist with complex legal reasoning tasks.
This study evaluates the reasoning capabilities
of state-of-the-art LLMs to interpret and ap-
ply Islamic inheritance laws. We utilized the
dataset proposed in the ArabicNLP QIAS 2025
challenge, which includes inheritance case sce-
narios given in Arabic and derived from Islamic
legal sources. Various base and fine-tuned mod-
els, are assessed on their ability to accurately
identify heirs, compute shares, and justify their
reasoning in alignment with Islamic legal prin-
ciples. Our analysis reveals that the proposed
majority voting solution, leveraging three base
models (Gemini Flash 2.5, Gemini Pro 2.5, and
GPT o3), outperforms all other models that we
utilized across every difficulty level. It achieves
up to 92.7% accuracy and secures third place
overall in the challenge (Tas).
1
Introduction
Islamic inheritance, which is known as “Ilm al-
Maw¯ar¯ıth” in Arabic, is an area of jurisprudence
that is highly structured, rule-based, and sensitive
to context (Abbasi, 2025; qia, 2025). The Qur’an
introduced various rights and restrictions related to
inheritance, marking significant improvements in
the treatment of women and family relations for its
time (Isl). It also aimed to establish clear and fixed
inheritance laws, contributing to the formation of a
comprehensive legal system.
Islamic inheritance jurisprudence aims to pre-
vent disputes by clearly defining the shares of each
heir (Services, 2025). It ensures fair and equitable
distribution, though Qur’anic verses assign differ-
ent shares to specific relatives. Inheritance domain
holds significant importance for Muslims, as it de-
termines the rightful heirs, the individuals to be
inherited from, and the specific shares allocated
to each heir (Zouaoui and Rezeg, 2021). Upon a
person’s death, a matter of particular concern is the
management of all the property left behind. Man-
ual calculation is a complex, time-consuming, and
error-prone task that can be extremely difficult and
costly. Automation of this calculation is convenient
to save time, effort, and cost (Zouaoui and Rezeg,
2021).
Our analyses and experiments center around the
following research questions: RQ1: Do current
Arabic open-source LLMs perform well in Islamic
inheritance reasoning? RQ2: To what extent do
state-of-the-art proprietary base LLMs excel in Is-
lamic inheritance reasoning? and RQ3: Can fine-
tuning LLMs for the inheritance reasoning task
improve performance?
We address RQ1 by running several open-source
Arabic LLMs. To answer RQ2, we utilized APIs
of state-of-the-art proprietary LLMs. Additionally,
to answer RQ3, we fine-tuned several LLMs with
the inheritance multiple-choice questions dataset.
2
Related Work
LLMs have shown impressive performance in a va-
riety of natural language understanding tasks (Al-
Dahoul et al., 2024a,b; Kuo et al., 2025). When
it comes to representing Islam, it is essential to
ensure that its beliefs and teachings are portrayed
accurately and faithfully, grounded in the Quran
and Sunnah (Patel et al., 2023). Additionally, it is
important to prevent hallucination in Islamic fatwa
generation (Mohammed et al., 2025).
Several studies have focused on automating the
inheritance calculation. (Jimoh et al., 2014) used an
expert system to calculate shares based on Islamic
law. Despite the growing development of auto-
mated knowledge retrieval systems, few leverage
semantic web technologies for Islamic knowledge,
arXiv:2508.15796v1  [cs.CL]  13 Aug 2025

--- Page 2 ---

particularly in Arabic. (Zouaoui and Rezeg, 2021)
introduced AraFamOnto, an Arabic ontology-based
system designed to automate Islamic inheritance
calculations by efficiently modeling family rela-
tionships and reducing manual effort.
(Abbasi, 2025) examined the capabilities of gen-
erative AI models, such as ChatGPT-4 (OpenAI,
2024), Gemini (Team et al., 2023), Co-Pilot (Copi-
lot, 2025), and DeepSeek (DeepSeek, 2024), in
applying the principles of Islamic inheritance law.
In their experiment, although ChatGPT-4 surpasses
other models in performance, it continues to exhibit
notable limitations, including fabricated references
and legal inaccuracies. There is an ongoing effort
to transform Islamic studies through generative AI
as part of the 2024–2027 project (Research Center
for Islamic Legislation and Ethics (CILE), 2025).
This initiative focuses on building AI tools to en-
gage with classical and contemporary Islamic texts.
However, previous efforts to automate inheri-
tance problem solving using generative models
remain limited, both in the number of models
explored and due to the absence of large-scale
datasets encompassing diverse scenarios and dif-
ficulty levels. This study addresses these gaps by
utilizing a comprehensive dataset (Bouchekif et al.,
2025; Bouchekif et al.) of inheritance cases to
evaluate the performance of state-of-the-art LLMs.
3
Materials and Methods
3.1
Dataset Overview
The QIAS (Question-and-Answer in Islamic Stud-
ies Assessment Shared Task) 2025 (qia, 2025;
Bouchekif et al., 2025; Bouchekif et al.) dataset
for Islamic inheritance reasoning contains multiple-
choice questions (MCQs) categorized into three
difficulty levels: beginner, intermediate, and ad-
vanced. The primary goal is to evaluate the rea-
soning abilities of LLMs within the domain of Is-
lamic knowledge. Each question has exactly one
correct answer and presents six answer choices,
labeled A through F, each accompanied by a cor-
responding textual explanation. The dataset is an-
notated using one of six distinct symbols. The
questions are sourced from a corpus of 32,000 fat-
was from IslamWeb and have been validated by
a qualified expert in Islamic inheritance law. The
dataset is divided into 9,446 labeled examples for
training, 1,000 labeled examples for validation, and
1,000 unlabeled examples for testing in the final
test phase. Figure 1, Figure 2, and Figure 3 show
Figure 1: Example 1
Figure 2: Example 2
few examples of this dataset.
3.2
Methods
We have evaluated several methods, including base
and fine-tuned LLMs, to find the best solution for
Islamic inheritance reasoning.
In the first experiment, base open-source Ara-
bic models such as Falcon3 (Team, 2024; Tech-
nology Innovation Institute (TII) UAE, 2024)
(“tiiuae/Falcon3-7B-Instruct”), Fanar (QCRI, 2025;
Team et al.) (“QCRI/Fanar-1-9B-Instruct”), and
Allam (ALLaM-AI, 2025; Bari et al., 2024)
(“ALLaM-AI/ALLaM-7B-Instruct-preview”) were
assessed. Additionally, we utilized “Allam think-
ing” (Research, 2025) (“almaghrabima/ALLaM-
Thinking”) (Bari et al., 2024), an advanced Arabic
LLM, which was fine-tuned and optimized specifi-
cally for reasoning and math. It was also prompted

--- Page 3 ---

Figure 3: Example 3
to think step-by-step.
Additionally, proprietary models such as Gemini
Flash 2.5, Gemini Pro 2.5 (Team et al., 2023; Koray
Kavukcuoglu, 2025), GPT-4o (OpenAI, 2024), and
GPT o3 (OpenAI, 2025), were evaluated for the
Islamic inheritance reasoning task using the APIs
of their base models. All previous LLMs were
assessed in inference mode using Prompt 2 with
temperature set to 0 and top_p set to 1.
To improve the performance of the base LLM in
reasoning and increase the rate of correct answers
to inheritance questions, we fine-tuned several
open-source and proprietary LLMs such as GPT-
4o, Gemini Flash 2.5, and Llama 4 Scout (Meta AI,
2025b,a) (“meta-llama/Llama-4-Scout-17B-16E-
Instruct”). All LLMs were fine-tuned in a super-
vised learning setting using the dataset mentioned
above, with a training set of 7,000 examples and a
validation set of 2,446 examples used during train-
ing. The results of the comparison between all
LLMs, including the base and fine-tuned, are re-
ported using the 1,000 examples in the separate
validation set.
Llama 4 was fine-tuned utilizing two prompts:
Prompt 1 and Prompt 2. The fine-tuning was done
using Low-Rank Adaptation (LoRA) (Hu et al.,
2022) as the Parameter-Efficient Fine-Tuning
(PEFT) method. The training was carried out for
seven epochs with a learning rate of 0.0002. Both
the training and evaluation batch sizes were set
to 1 per device, and the gradient accumulation
steps were set to 1.
The optimizer used was
paged_adamw_32bit. Additionally, 10 warmup
steps were used to stabilize the initial training
phase. We loaded the model using 4-bit quan-
tization for memory efficiency. The fine-tuned
models have been uploaded to Hugging Face:
https://huggingface.co/NYUAD-ComNets/
NYUAD_Llama4_Inheritance_Solver,
and
https://huggingface.co/NYUAD-ComNets/
NYUAD_Llama4_Inheritance_Solver2.
Prompt 1: Islamic inheritance reasoning
Answer the following question using a single
word only from this list: A, B, C, D, E, F.
Final Answer:
GPT-4o was fine-tuned in two scenarios: without
a system prompt and with system Prompt 2. The
fine-tuning was done on the OpenAI platform for 5
epochs, with a learning rate multiplier of 2 and au-
tomatically selected batch size. Similarly, Gemini
Flash 2 and 2.5 were fine-tuned with system Prompt
2. The fine-tuning was done on the Google AI Ver-
tex platform. The hyper-parameters used for fine-
tuning are 3 epochs and a learning_rate_multiplier

--- Page 4 ---

of 5. Flash 2.5 used an adapter size of 1, while
Flash 2 used an adapter size of 8 to train more
parameters. In the inference phase, the threshold
in safety_settings is set to off, while thinking was
enabled.
3.3
Results and Discussion
Table 1 shows the accuracy of base LLMs for
several open-source Arabic LLMs and proprietary
state-of-the-art LLMs. Among the open models,
Allam demonstrates relatively better performance
(38.8%), indicating it may be more effectively
tuned for this specific task or domain. In contrast,
Falcon3 and Fanar perform worse, likely due to
limited domain understanding. Although “Allam
Thinking” was optimized for reasoning and math,
its accuracy declined compared to the base Allam
model. This set of experiments indicates a lack
of domain knowledge and reasoning in the base
open-source Arabic LLMs, which addresses RQ1.
Additionally, both GPT o3 (92.3%) and Gemini
Flash 2.5 (91.5%) demonstrate the strongest per-
formance, highlighting their advanced capability
in understanding and reasoning about Islamic in-
heritance, which answers RQ2. The small gap in
accuracy may be due to the results being based on
a single run. Therefore, for future work, we should
run each model multiple times and compute the
average and variance. This process can provide a
clearer comparison between the two.
LLM
Accuracy (%)
Falcon3
24.2
Fanar
31.7
Allam
38.8
Allam think
29.2
Gemini Flash 2.5
91.5
GPT-4o
70.1
GPT O3
92.3
Table 1: Accuracy of different Base LLMs.
Table 2 shows the prompt sensitivity of each
LLM using a simple prompt such as Prompt 1 and
a Chain of Thought (CoT) prompt such as Prompt 2.
The GPT-4o model demonstrates a notable sensitiv-
ity to prompt design. When evaluated with Prompt
1, its accuracy is relatively low at 57.5%. How-
ever, a shift to Prompt 2 significantly enhances the
performance to 70.1%, thereby. Allam also shows
the same trend. On the other hand, Gemini Flash
2.5 exhibits high accuracy regardless of prompt
content, suggesting strong internal reasoning and
understanding.
LLM
Prompt
Accuracy (%)
Allam think
Prompt 1
28.8
Allam think
Prompt 2
29.2
Allam
Prompt 1
30.4
Allam
Prompt 2
38.8
Fanar
Prompt 1
28.7
Fanar
Prompt 2
31.7
Falcon
Prompt 1
24.2
Falcon
Prompt 2
22.8
Gemini Flash 2.5
Prompt 1
90.7
Gemini Flash 2.5
Prompt 2
91.5
GPT-4o
Prompt 1
57.5
GPT-4o
Prompt 2
70.1
Table 2: Prompt sensitivity: Accuracy of LLMs
using two different Prompts.
When GPT-4o was fine-tuned for reasoning us-
ing the training set, its accuracy improved signif-
icantly, reaching over 84% as shown in Table 3.
On the other hand, when no system prompt is used
for tuning, the accuracy reaches 84.7%. When
we added “Prompt 2” as a system prompt, the ac-
curacy improved to 86.6%. On the contrary, the
performance of Gemini Flash 2.5 dropped after
fine-tuning (91.5% –> 74.6%) on this task. This
disparity in the fine-tuning results between GPT-4o
and Gemini Flash 2.5 gives an answer to RQ3.
The reason behind this disparity in performance
after fine-tuning is that GPT-4o is a highly gener-
alist model, not specialized for reasoning. This
makes it more adaptable to niche domains like
Islamic inheritance when given domain-specific
data. Furthermore, GPT-4o may have moderate
prior knowledge about Islamic inheritance laws,
so fine-tuning filled a knowledge gap rather than
conflicting with existing knowledge.
On the other hand, we observed performance
degradation in fine-tuning Gemini Flash 2.5 with
the adapter size set to 1 (tuning fewer parameters).
To confirm our observation, we may consider fine-
tuning the same model with larger adapter sizes.
The reason for degradation may stem from the fact
that Flash 2.5 is optimized for CoT reasoning. If the
fine-tuning dataset has only final labels and lacks
detailed reasoning chains, the model may lose its
reasoning structure. This results in misalignment
between what it’s trained to do and what it’s fine-
tuned to.

--- Page 5 ---

Fine-tuning Flash 2 with an adapter size of 8
resulted in degraded performance on this task. This
may be due to the relatively limited size of the
fine-tuning dataset, which was insufficient to train
a larger adapter. As a result, the model likely failed
to generalize well. To validate our observation,
we may consider fine-tuning the same model with
smaller adapter sizes or using the base model.
As shown in Table 3, fine-tuning GPT-4o with
Prompt 2 resulted in a better performance, which
contrasts with the behavior of Llama 4 Scout.
LLM
Prompt
Accu. (%)
Fine-tuned Llama4
Scout
Prompt 1
84.3
Fine-tuned Llama4
Scout
Prompt 2
82.4
Fine-tuned Gemini
Flash 2
Prompt 2
64.6
Fine-tuned Gemini
Flash 2.5
Prompt 2
74.6
Fine-tuned GPT-4o
No system
Prompt
84.7
Fine-tuned GPT-4o
Prompt 2
86.6
Table 3: Accuracy of fine-tuned LLMs.
Finally, we ran an experiment to assess the best-
performing base LLMs with the testing set released
in the test phase and included an unlabeled set
of 1000 MCQs. We ran three base models in the
inference mode. The accuracies of GPT-o3, Gemini
Flash 2.5, and Gemini Pro 2.5 on the testing data
were 88.4%, 88.1%, and 87.9%, respectively. We
later applied a majority voting technique using the
predictions from these three LLMs, resulting in a
final accuracy of 92.7%, which secured third place
overall in the challenge.
Limitations
The limitation of this work is that LLMs often lack
comprehensive knowledge of all inheritance sce-
narios, which leads even the best reasoning mod-
els to occasionally select incorrect answers. Fine-
tuning can help address this issue. However, a
new problem arises: in the original dataset, answer
choices were labeled without detailed reasoning
for each option, which complicated the fine-tuning
of reasoning-based models. To solve this, a sec-
ond version of the dataset was released recently,
including the reasoning behind each selected an-
swer (Bouchekif et al., 2025; Bouchekif et al.).
This may show potential for increasing the accu-
racy.
References
Islamic inheritance jurisprudence.
https://en.
wikipedia.org/wiki/Islamic_inheritance_
jurisprudence#cite_note-EI2-1. Accessed July
13, 2025.
Task 1 leaderboard - qias2025.
https://sites.
google.com/view/qias2025/leaderboards?
authuser=0. Accessed: 2025-07-27.
2025. Qias 2025 shared task. Accessed July 13, 2025.
Zubair Abbasi. 2025. Augmented learning: Genera-
tive artificial intelligence and islamic inheritance law.
Accessed July 13, 2025.
Nouar AlDahoul, Talal Rahwan, and Yasir Zaki. 2024a.
Polytc: a novel bert-based classifier to detect polit-
ical leaning of youtube videos based on their titles.
Journal of Big Data, 11(1):80.
Nouar AlDahoul, Myles Joshua Toledo Tan, Har-
ishwar Reddy Kasireddy, and Yasir Zaki. 2024b.
Advancing content moderation: Evaluating large
language models for detecting sensitive content
across text, images, and videos.
arXiv preprint
arXiv:2411.17123.
ALLaM-AI.
2025.
Allam-7b-instruct-preview.
https://huggingface.co/ALLaM-AI/
ALLaM-7B-Instruct-preview.
Accessed: 2025-
07-13.
M Saiful Bari, Yazeed Alnumay, Norah A Alzahrani,
Nouf M Alotaibi, Hisham A Alyahya, Sultan Al-
Rashed, Faisal A Mirza, Shaykhah Z Alsubaie, Has-
san A Alahmed, Ghadah Alabduljabbar, et al. 2024.
Allam: Large language models for arabic and english.
arXiv preprint arXiv:2407.15390.
Abdessalam Bouchekif, Samer Rashwani, Emad Mo-
hamed, Mutez Al-Khatib, Heba Sbahi, Shahd Gaben,
Wajdi Zaghouani, Aiman Erbad, and Mohammed
Ghaly. 2025. Qias 2025: Overview of the shared
task on islamic inheritance reasoning and knowledge
assessment. In Proceedings of The Third Arabic Nat-
ural Language Processing Conference, ArabicNLP
2025, Suzhou, China, November 5–9, 2025. Associa-
tion for Computational Linguistics.
Abdessalam Bouchekif, Samer Rashwani, Heba Sbahi,
Shahd Gaben, Mutez Al-Khatib, and Mohammed
Ghaly. Assessing large language models on islamic
legal reasoning: Evidence from inheritance law eval-
uation. CoRR.
Microsoft Copilot. 2025. Copilot ai companion. https:
//copilot.microsoft.com.
Accessed: July 13,
2025.

--- Page 6 ---

DeepSeek. 2024.
Deepseek chat.
https://www.
deepseek.com. Accessed: July 13, 2025.
Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan
Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang,
Weizhu Chen, et al. 2022. Lora: Low-rank adap-
tation of large language models. ICLR, 1(2):3.
RG Jimoh, IR Adebayo, AO Ameen, and HO Ahmad.
2014. Design of an expert system to calculate inher-
itance shares based on islamic law. IEEE-African
Journal of Computing & ICTs, 7(2):151–156.
Koray
Kavukcuoglu.
2025.
Gemini
2.5:
Our
most
intelligent
ai
model.
https:
//blog.google/technology/google-deepmind/
gemini-model-thinking-updates-march-2025/
#gemini-2-5-thinking.
Chen Wei Kuo, Kevin Chu, Nouar AlDahoul, Hazem
Ibrahim, Talal Rahwan, and Yasir Zaki. 2025. Neu-
tralizing the narrative: Ai-powered debiasing of on-
line news articles. arXiv preprint arXiv:2504.03520.
Meta
AI.
2025a.
The
llama
4
herd:
The
beginning
of
a
new
era
of
natively
multi-
modal
ai.
https://ai.meta.com/blog/
llama-4-multimodal-intelligence/.
Ac-
cessed:
2025-07-13; announces Scout & Mav-
erick (17B active, MoE, 10 M & 1 M context)
with
native text+image support
:contentRefer-
ence[oaicite:2]index=2.
Meta AI. 2025b.
Llama-4-scout-17b-16e-instruct.
https://huggingface.co/meta-llama/
Llama-4-Scout-17B-16E-Instruct.
Released
April 5, 2025 under the Llama 4 Community License;
multimodal MoE model with 17 B active parameters
and 16 experts, 10M token context, supports 12
languages.
Marryam Yahya Mohammed,
Sama Ayman Ali,
Salma Khaled Ali, Ayad Abdul Majeed, and En-
saf Hussein Mohamed. 2025.
Aftina: enhancing
stability and preventing hallucination in ai-based is-
lamic fatwa generation using llms and rag. Neural
Computing and Applications, pages 1–26.
OpenAI. 2024. Gpt-4o.
OpenAI.
2025.
Introducing
o3
and
o4-
mini.
https://openai.com/index/
introducing-o3-and-o4-mini/.
Accessed:
2025-07-13.
S Patel, H Kane, and R Patel. 2023. Building domain-
specific llms faithful to the islamic worldview: Mi-
rage or technical possibility?. arxiv.
QCRI.
2025.
Fanar-1-9b-instruct.
https:
//huggingface.co/QCRI/Fanar-1-9B-Instruct.
Accessed: 2025-07-13.
Mohammed Al-Maghrabi Research. 2025.
Allam-
thinking: Arabic large language model with enhanced
reasoning capabilities. https://huggingface.co/
almaghrabima/ALLaM-Thinking.
Research Center for Islamic Legislation and Ethics
(CILE). 2025.
Transforming islamic studies in
the age of generative artificial intelligence (ai):
Developing
ai-empowered
“islamgpt
1.0”
for
arabic sources.
https://www.cilecenter.org/
research-publications/funded-projects/
transforming-islamic-studies-age-generative-artificial.
Islamic Will & Trust Services. 2025.
Islamic
law
of
inheritance
according
to
quran
and
sunnah.
https://islamicwillstrust.com/
islamic-law-of-inheritance/.
Accessed July
2025.
Fanar Team, Ummar Abbas, Mohammad Shahmeer Ah-
mad, Firoj Alam, Enes Altinisik, Ehsannedin Asgari,
Yazan Boshmaf, Sabri Boughorbel, Sanjay Chawla,
Shammur Chowdhury, Fahim Dalvi, Kareem Dar-
wish, Nadir Durrani, Mohamed Elfeky, Ahmed El-
magarmid, Mohamed Eltabakh, Masoomali Fatehkia,
Anastasios Fragkopoulos, Maram Hasanain, Majd
Hawasly, Mus’ab Husaini, Soon-Gyo Jung, Ji Kim
Lucas, Walid Magdy, Safa Messaoud, Abubakr Mo-
hamed, Tasnim Mohiuddin, Basel Mousi, Hamdy
Mubarak, Ahmad Musleh, Zan Naeem, Mourad Ouz-
zani, Dorde Popovic, Amin Sadeghi, Husrev Taha
Sencar, Mohammed Shinoy, Omar Sinan, Yifan
Zhang, Ahmed Ali, Yassine El Kheir, Xiaosong Ma,
and Chaoyi Ruan. Fanar: An arabic-centric multi-
modal generative ai platform.
Gemini Team, Rohan Anil, Sebastian Borgeaud,
Yonghui Wu, Jean-Baptiste Alayrac, Jiahui Yu,
Radu Soricut, Johan Schalkwyk, Andrew M Dai,
Anja Hauth, et al. 2023.
Gemini: a family of
highly capable multimodal models. arXiv preprint
arXiv:2312.11805.
TII Team. 2024. The falcon 3 family of open models.
Technology Innovation Institute (TII) UAE. 2024.
Falcon3-7b-instruct.
https://huggingface.co/
tiiuae/Falcon3-7B-Instruct.
Samia Zouaoui and Khaled Rezeg. 2021. Islamic in-
heritance calculation system based on arabic ontol-
ogy (arafamonto). Journal of King Saud University-
Computer and Information Sciences, 33(1):68–76.

```
