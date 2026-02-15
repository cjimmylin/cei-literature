---
title: "2025-Yao-Multi-TW Benchmarking Multimodal Models on Traditional Chinese - PDF Extract"
source_pdf: "2025-Yao-Multi-TW Benchmarking Multimodal Models on Traditional Chinese.pdf"
pages: 8
extracted_at: "2026-02-15T17:54:29.020097"
---

# PDF Extract: 2025-Yao-Multi-TW Benchmarking Multimodal Models on Traditional Chinese

**Source PDF:** 2025-Yao-Multi-TW Benchmarking Multimodal Models on Traditional Chinese.pdf
**Total Pages:** 8

---

## Content

```
--- Page 1 ---

Multi-TW: Benchmarking Multimodal Models on Traditional
Chinese Question Answering in Taiwan
Jui-Ming Yao
National Taiwan University of
Science and Technology
Taipei, Taiwan
b11132009@mail.ntust.edu.tw
Bing-Cheng Xie
National Taiwan University of
Science and Technology
Taipei, Taiwan
b11130009@mail.ntust.edu.tw
Sheng-Wei Peng
National Taiwan University of
Science and Technology
Taipei, Taiwan
m11207330@mail.ntust.edu.tw
Hao-Yuan Chen
University of London
London, United Kingdom
hc118@student.london.ac.uk
He-Rong Zheng
National Taiwan University
Taipei, Taiwan
b10302350@ntu.edu.tw
Bing-Jia Tan
National Taiwan University
Taipei, Taiwan
b11115001@mail.ntust.edu.tw
Peter Shaojui Wang
National Taiwan University of
Science and Technology
Taipei, Taiwan
shaojuiwang@mail.ntust.edu.tw
Shun-Feng Su
National Taiwan University of
Science and Technology
Taipei, Taiwan
sfsu@mail.ntust.edu.tw
Abstract
Multimodal Large Language Models (MLLMs) process visual, acous-
tic, and textual inputs, overcoming the limitations of single-modality
LLMs. However, existing benchmarks often neglect tri-modal eval-
uation in Traditional Chinese and overlook inference latency. To
fill this gap, we introduce Multi-TW, the first Traditional Chinese
benchmark for evaluating the performance and latency of any-to-
any multimodal models. Multi-TW comprises 900 multiple-choice
questions (image & text, audio & text pairs) from authentic profi-
ciency tests developed with the Steering Committee for the Test
of Proficiency-Huayu (SC-TOP). We evaluated various any-to-any
models and vision-language models (VLMs) with audio transcrip-
tion. Our findings show closed-source models generally outperform
open-source ones across modalities, though open-source models
can excel in audio tasks. End-to-end any-to-any pipelines demon-
strate significant latency advantages over VLM with separate audio
transcription. Multi-TW offers a holistic view of model capabili-
ties, underscoring the need for Traditional Chinese fine-tuning and
efficient multimodal architectures.
CCS Concepts
• Computing methodologies →Model verification and vali-
dation; Model verification and validation.
Keywords
Benchmark evaluation, Traditional Chinese, Question Answering,
Multimodal Large Language Models, Inference Latency Analysis
1
Introduction
Pre-trained Large Language Models (LLMs), such as LLaMA [29, 30]
and Qwen [3, 21, 35], have demonstrated remarkable success across
a wide range of natural language processing (NLP) tasks. However,
these text-only models remain constrained by their single-modality
input. To address this limitation, recent research has increasingly
focused on Multimodal Large Language Models (MLLMs), which
can jointly process and reason over visual, acoustic, and textual
inputs [15, 36].
In the visual domain, models such as CLIP [22] and Flamingo [1]
have shown that contrastive pretraining and multimodal fusion
architectures enable state-of-the-art zero-shot image classification,
image captioning, and few-shot visual reasoning [9, 14]. Building
upon these breakthroughs, Vision-Language Models (VLMs) like
LLaVA [16] have pushed the frontier further, inspiring fine-tuned
successors such as Vicuna [38] and Alpaca [28], which expand mul-
timodal reasoning capabilities across broader task domains. The
models evaluated in our experiments, such as the LLaVA series,
PaliGemma 2 [25], Idefics2 [11], Llama 3.2-Vision [18], UI-TARS [20]
and Qwen VL [4] series, represent the cutting edge in these devel-
opments.
With the evolution of VLMs, increasing attention has turned
toward audio-language modeling. Audio Language Models (ALMs)
typically employ an audio encoder that transforms raw waveform
signals into token representations that can be processed by a lan-
guage model [10, 19]. For instance, Qwen-Audio [7] and Qwen-
Audio2 [6] utilize the Qwen model series [3, 35] as their language
modeling backbone and incorporate OpenAI’s Whisper [23] for
end-to-end speech recognition. Other architectures, such as Au-
dioPaLM [24], fuse the text-based capabilities of PaLM-2 [2] with
the discrete audio token modeling of AudioLM [5], enabling both
high-quality speech recognition and speech-to-speech translation
in a unified framework.
More recently, research has progressed toward universal any-to-
any multimodal models that support cross-modal input and output
across vision, audio, and text. Prominent examples include NExT-
GPT [32], AnyGPT [37] and Unified-IO 2 [17], all pushing the
limits of unified multimodal intelligence. Later, this trend transfer
into multilingual support, as shown in open-source models like
arXiv:2508.01274v1  [cs.AI]  2 Aug 2025

--- Page 2 ---

Preprint, August, 2025
Yao, et al.
Baichuan-Omni-1.5 [12] and Qwen2.5-Omni [33], as well as closed-
source systems such as gemini, which achieve strong performance
in both Chinese and English understanding.
To rigorously evaluate the capabilities of such models, several
benchmarks have been proposed. However, most evaluations still
assess only two modalities at a time. For instance, NExT-GPT [32]
and AnyGPT [37] focus on pairwise modality evaluations. Recently,
Qwen2.5-Omni [33] and Baichuan-Omni-1.5 [12] have adopted
OmniBench [13], a tri-modal benchmark designed to assess per-
formance across text, image, and audio simultaneously, providing
deeper insight into a model’s unified reasoning ability.
Despite these advances, a critical gap remains in the evaluation of
multimodal models in Traditional Chinese. Existing Traditional
Chinese benchmarks are largely text-based. TMMLU [8] and
its extension TMMLU+ [26] provide comprehensive text-only eval-
uations of LLMs. VisTW [27] moves into the multimodal space by
evaluating VLMs on multiple-choice and dialog-based tasks; how-
ever, no benchmark currently supports comprehensive evaluation
across textual, visual, and acoustic modalities in Traditional Chi-
nese. In addition to this linguistic gap, we observe that most existing
benchmarks prioritize accuracy, often overlooking model infer-
ence time. This approach is insufficient for real-world applications
where both accuracy and efficiency are crucial.
To address this gap, we introduce Multi-TW, the first benchmark
specifically designed for evaluating the performance and latency
of any-to-any multimodal models in Traditional Chinese. Multi-
TW consists of image-text and audio-text pairs, enabling rigorous
evaluations that cover textual, visual, and acoustic modalities. All
datasets are open-sourced and available at: https://drive.google.
com/drive/folders/1IvBOXR1GpMNtst0T3HT6dM59_ASlXdyn.
In summary, our contributions are as follows:
• We propose Multi-TW, the first Traditional Chinese bench-
mark for rigorous evaluation across text, audio, and visual
inputs.
• We collaborated with the Steering Committee for the Test
of Proficiency-Huayu to incorporate authentic, real-world
assessment tasks into our machine evaluation framework.
• We conduct comprehensive experiments on both any-to-any
models and VLMs (the latter using ASR for audio input).
• In addition to accuracy, we evaluate latency to offer a more
holistic view of model performance in real-world settings.
2
Multi-TW Benchmark
In this section, we provide a concise overview of Multi-TW, includ-
ing its construction process, validation procedures, and data format
specifications to support reproducibility. Our dataset is derived
from real-world exams, detailed further in Section 2.2.
2.1
Data Construction
To construct the Multi-TW dataset, we collaborated with the Steer-
ing Committee for the Test of Proficiency-Huayu (SC-TOP), a dedi-
cated agency responsible for developing and promoting Taiwan’s
Mandarin proficiency tests for non-native speakers. These exams,
primarily in a multiple-choice format, underwent rigorous utility
analysis to ensure their practical value and effectiveness.
Image
Audio
Question
Information
Instruction
&
Options
Collect
History
Figure 1: Illustration of data collection interface.
Construction. The construction phase spanned from Septem-
ber 2023 to December 2023, primarily using publicly available data.
All items in Multi-TW underwent a standardized collection and
processing workflow performed by our research team to ensure
consistency and accuracy. We developed an interface to acceler-
ate data collection and automate labeling, as depicted in Figure 1.
Initially, purely textual questions were removed. The remaining
items, which involved various combinations of modalities, were
then curated to form image-text and audio-text pairs. To address
data imbalance and expand the image-text subset, some questions
originally coupling image and audio were adapted by extracting
their ground-truth audio transcripts, which were then paired with
the corresponding image as the textual component. Subsequently,
each image-text and audio-text multiple-choice item was serial-
ized into a unified JSON schema, containing the original question,
response options, instructions, and references to the separately
stored image or audio files. During construction, instructions were
classified into seven categories to prevent excessive fragmentation
of task types. Further details are depicted in Table 1.
Quality Control. To ensure data integrity, each image-text and
audio-text pair was independently reviewed by a second annotator
to verify content consistency and accuracy, ensuring the absence
of syntax errors, missing information, or incorrect answer choices.
Our quality control process involved multiple stages:
(1) Completeness Check: Annotators inspected each question
to confirm the presence of all required components: text
(prompt, options, and solution index), image or audio file, and
associated metadata. Entries with missing or inconsistent
elements (e.g., a mismatched file name) were flagged and
corrected.
(2) File Consistency Check: Each image was viewed to confirm it
was properly formatted (150 dpi PNG), and each audio clip
was played to ensure audible clarity in the specified 128 kbps
MP3 (or other, specify format) setting. Invalid or corrupted
files were replaced or re-processed.
(3) Label Accuracy Verification: Given that the dataset tests lan-
guage proficiency, annotators carefully matched the text con-
tent with the corresponding image or audio. For the image-
text subset, the visual context had to align with the question
stem and options (e.g., an illustration of a given scenario).
For audio-text items, the spoken content was compared with

--- Page 3 ---

Multi-TW: Benchmarking Multimodal Models on Traditional Chinese Question Answering in Taiwan
Preprint, August, 2025
the multiple-choice options to verify that the designated
answer was correct.
(4) Final Confirmation: After all corrections were made, each
question was subjected to a final review to verify that the
files and metadata were correctly updated. Only after passing
this final check was the question approved for inclusion in
the final dataset.
Reproducibility. To ensure reproducibility and facilitate data
management, a system was developed to encode the original source
location of each data item. The following details the significance of
the dataset identifier. Files are organized into directories named by
a five-part identifier, read from left to right as follows:
(1) Volume (1–5): The ’booklet’ number of the data source.
(2) Section (L/R): L for Listening, R for Reading.
(3) Level (N/A/B/C): A difficulty rating where N denotes “Novice”
and A, B, and C correspond to Bands A, B, and C, respectively.
(4) Part (Pn): The part number within the section (e.g., P1, P2).
(5) Question: The index of the question within that part.
This structure facilitates verification and aids researchers in data
retrieval and collection. More detailed information on the data
format is provided in Table 1.
Table 1: Key Fields in the JSON Annotation Format.
Field Name
Description
id
Unique item identifier (e.g., "01-L-A-P1-001").
image
Relative image file path (string or null).
audio
Relative audio file path (string or null).
instruction
Instructions for the question.
question
Textual content of the question.
options
List of options, typically prefixed with (A)–(D)
(e.g., ["(A) Option 1", "(B) Option 2"]).
answer
Correct option identifier: "A", "B", "C", or "D".
2.2
Data Analysis
This section provides a detailed analysis of Multi-TW to facilitate a
comprehensive understanding of its characteristics, including its
size and the distribution of question types and modalities. Through
this analysis, our objective is to concretely characterize our dataset
and highlight its distinctions from existing benchmarks. Finally, we
compare Multi-TW against other established datasets to underscore
its unique characteristics and strengths.
Data Size. Multi-TW comprises 900 multiple-choice questions
curated to assess Traditional Chinese proficiency in a multimodal
context. The dataset is equally divided into 450 image-text items
and 450 audio-text items. In the following sections, we refer to these
as ’vision-based items’ and ’audio-based items,’ respectively. This
balanced design enables direct comparison of model performance
on visual versus auditory modalities paired with Traditional Chi-
nese text and encourages the development of models that handle
both input types proficiently.
Data Distribution. The vision-based subset features 397 distinct
images and includes 407 three-choice items alongside 43 four-choice
items. These images depict contextual illustrations, diagrams, and
real-world scenarios. All audio-based items employ a four-choice
format. Consequently, the 900-item benchmark comprises 407 three-
choice questions and 493 four-choice questions (43 from vision-
based and 450 from audio-based). For the audio-based items, the
average question length is approximately 12 words, and the average
option length is approximately 10 words. The average duration of
the audio is approximately 107.5 seconds, as illustrated in Figure 4.
Task Formulation. Multi-TW evaluates multimodal under-
standing by measuring performance on two primary task types:
vision-based tasks and audio-based tasks. These are structured as
multiple-choice questions (MCQs), namely Vision-based MCQ and
Audio-based MCQ.
• Audio-based MCQ comprises two subtasks:
– Dialogue Comprehension
– Passage Comprehension
• Vision-based MCQ comprises five subtasks:
– Dialogue Comprehension
– Image Comprehension
– Reading Comprehension
– Sentence-to-Image Matching
– Image-to-Sentence Matching
Details of subtask distribution are provided in Figure 3. This diverse
mix of task types ensures that Multi-TW evaluates a broad spectrum
of multimodal understanding capabilities.
Comparison with Existing Benchmarks. Table 2 presents
a comparison of Multi-TW with other notable Traditional Chi-
nese language evaluation datasets. While existing benchmarks like
TMMLU+ [26] focus on text-only LLM capabilities, and VisTW-
MCQ [27] and ALM-Bench [31] incorporate vision and text, Multi-
TW, to the best of our knowledge, is the first benchmark to provide
comprehensive image-text and audio-text evaluation for Traditional
Chinese, thereby covering visual, textual, and auditory modalities.
By unifying these input types within a single benchmark framework
for Traditional Chinese, it fills a critical gap and enables a more
holistic evaluation of multimodal models. Moreover, beyond its rich
modality and linguistic features, Multi-TW’s audio samples average
107.5 seconds in length, substantially longer than the 9.12 seconds
typical of OmniBench [13] (which primarily tests English). This
extended duration enables a more rigorous evaluation of long-form
listening comprehension abilities.
Table 2: Comparison of Multi-TW with other datasets. For
ALM-Bench, we only compare the subset for Traditional Chi-
nese. (A: audio, T: text, V: vision) (Traditional Chinese: zh,
English: en)
Dataset
Modalities
Language
Test size
Subjects
TMMLU+ [26]
T
zh
20,118
66
ALM-Bench [31]
T, V
zh
52
13
VisTW-MCQ [27]
T, V
zh
3,795
21
OmniBench [13]
A, T, V
en
1,142
8
Multi-TW (Ours)
A, T, V
zh
900
7

--- Page 4 ---

Preprint, August, 2025
Yao, et al.
question: (Transfer from audio)
（A）不開了
（B）要離開了
（C）晚一個小時到
（D）晚三十分鐘到
answer: "D"
請聽這一段車站裡的廣播，然後回答下面的問題。
各位旅客，很抱歉！因為大雨的關係，十二點五十分往台北的一一零號火車
會晚半個小時到，要坐一一零號車的旅客請在月台上耐心等候。謝謝！
question: (Transfer from audio)
（A）上午,
（B）中午,
（C）下午,
（D）晚上
answer: "C"
男：我想坐早上九點的火車到高雄去，中午到得了嗎？
女：應該是到不了，到高雄大概要五個小時。
男：早上九點的火車什麼時候到高雄？
Paragraph Comprehension
Instruction：在這個部分，你會聽到幾段話。
每段話結束後，會問幾個問題。
每個問題都有（A）（B）（C）（D）四個選項，這四個選項的內容也會出現在題本上。
Dialogue Comprehension
Instruction：在這個部分，你會聽到幾段兩個人的對話，
每段對話結束後，會問幾個問題。
每個問題都有(接著你會聽到)（A）（B）（C）（D）四個選項，這四個選項的內容也會出現在題本上。
Image-Based Q&A
Instruction：在這個部分，會有一張情境圖片，圖片下面會有句子，請
根據圖片情境，選出最合適的答案。
question: __著眼鏡的小女孩在看書。
（A）穿,
（B）帶,
（C）戴,
answer: "C"
Single Sentence Comprehension
Instruction：在這個部分，你會看到一個句子和（A）（B）（C）三
張圖片。請根據句子的意思，從三張圖片中選出與句子意思相符的
圖片。(在這個部分，每題有一個簡短的文字訊息和（A）（B）（C）
三張圖片。請根據文字訊息，選出正確的圖片。)
question: 那杯牛奶被喝了一半。
（A)
（B）
（C）
answer: "C"
Reading Comprehension
Instruction：在這一部分，請閱讀材料或短文，並根據內容回答幾個
問題。
question: 這個捐血中心的傳單上說了什麼？
（A)服務別人就是幫助別人
（B）捐血地點將透過電話通知
（C）捐血中心需要各種血型的血
（D）目前哪一種血型的血明顯不夠
answer: "D"
Image-Based Interpretation 
Instruction：在這個部分，你會看到一張圖片。
請根據圖片，從（A）（B）（C）三個選項中選出與圖片內容相符的句子。
question: 他們在哪裡？
（A）銀行,
（B）教室,
（C）郵局,
answer: "B"
Question-Answer Comprehension
Instruction：在這個部分，每題有（A）（B）（C）三張圖片，
你會看到一問一答的對話，請根據對話的內容，選出合適的圖片。
question: 男：你覺得桌子放在哪兒比較好呢？\n女：放在窗戶前面吧！那兒比較亮。
（A)
（B）
（C）
answer: "B"
Figure 2: Illustration of samples from the Multi-TW dataset.
....
28.1%
..
21.9%
.......
17.2%
.
14.4%
......
9.1%
...
4.8%
.....
4.4%
Question-Answer 
Comprehension
14.4%
4.4%
9.1%
17.2%
28.1%
4.8%
21.9%
Paragraph 
Comprehension
Reading 
Comprehension
Dialogue 
Comprehension
Image-Based 
Q&A
Single Sentence 
Comprehension
Image-Based 
Interpretation
Figure 3: Distribution of question types in Multi-TW.
3
Experiments
To demonstrate the utility of Multi-TW and establish initial perfor-
mance benchmarks, we conducted experiments using a variety of
publicly available multimodal language models. This section details
our experimental setup, the models evaluated, and the observed
results.
3.1
Experiment Setup
All experiments were conducted on an NVIDIA A100-SXM4 80GB
GPU. All 900 questions in Multi-TW were used for evaluation in a
zero-shot setting. The evaluation metric reported is exact-match
Figure 4: Distribution of audio durations in Multi-TW.
accuracy, reflecting the percentage of correctly answered multiple-
choice questions. We detail our prompting strategy, answer extrac-
tion, and time measurement protocols below.
Prompting Strategy. For all evaluated models, a uniform prompt
was appended to each question. The general prompt template pro-
vided to the models is as follows (in Traditional Chinese):
{question}
僅輸出正確答案的字母，格式必須為’A’, ’B’,
’C’, ’D’，輸出限制為單個字母，無需解釋。
This prompt instructs the model to directly output a single char-
acter representing the chosen option, without any additional expla-
nation or reasoning.

--- Page 5 ---

Multi-TW: Benchmarking Multimodal Models on Traditional Chinese Question Answering in Taiwan
Preprint, August, 2025
Answer Extraction. To extract answers from the model-generated
content, we constrained the model’s output to a single token and
applied a regular expression to capture the first occurrence of ’A’,
’B’, ’C’, or ’D’. If the regular expression failed to retrieve a valid
response, a fallback mechanism was implemented where a ran-
dom option from the available choices was selected. This ensures
consistent answer provision across all evaluations.
Time Measurement. We recorded the elapsed time for four
sequential stages: data loading, data preprocessing, model infer-
ence, and metric computation. Data preprocessing and model in-
ference account for the majority of runtime and utilize identical
code across all open-source models. Therefore, our timing analysis
focuses primarily on the combined duration of these two phases for
open-source models. Closed-source models were omitted from this
specific latency analysis, as their response times are dominated by
external API calls and network transmission, which are not directly
comparable. To eliminate variability from differing output lengths,
we fixed the model’s maximum generation length to one token for
all timed experiments.
3.2
Model Selection
We evaluated several any-to-any models that process text, image,
and audio inputs to generate text output in Traditional Chinese,
as well as several VLMs where audio input was provided via ASR
transcripts. These models, presented in Tables 3 and 4, span both
closed- and open-weight categories and were selected based on
their state-of-the-art performance, availability, architectural diver-
sity, and varying degrees of exposure to Chinese language data. For
closed-source any-to-any models, we selected gemini-2.0-flash and
gemini-1.5-flash from Google. For open-source any-to-any models,
we chose the Qwen2.5-Omni series and Baichuan-Omni-1.5, both
pretrained primarily on Simplified Chinese. Although Simplified
and Traditional Chinese share lexical similarities, they differ sub-
stantially in character forms and orthographic conventions. We
also incorporated UnifiedIO-2, an encoder-decoder Transformer
pretrained from scratch mostly on English data (with a small multi-
lingual fraction from mC4 [34]), making it a useful test for zero-shot
cross-script transfer as it has not been specifically fine-tuned for
either Chinese variant. For VLMs, we employed Whisper-large [23]
to transcribe audio inputs into text for the audio-text tasks. The
selected VLMs include Qwen2.5-VL-7B, Qwen2-VL-7B, Llama-3.2-
11B-Vision, UI-TARS-1.5-7B, Idefics2-8b, the LLaVA series, and
PaliGemma2. This selection reflects the current landscape and pro-
vides a broad overview of VLM capabilities on our benchmark.
4
Results and Analysis
This section offers a summary of performance across all evaluated
models on the 900-item Multi-TW benchmark, comparing accu-
racy on the image-text and audio-text subsets alongside inference
latency.
Performance on Any-to-Any Models. Table 3 illustrates the
results for any-to-any models across overall accuracy, image-text
subset accuracy, audio-text subset accuracy, and inference time. Key
observations include: 1) The Qwen2.5-Omni series and Baichuan-
Omni-1.5, despite being primarily pretrained and fine-tuned on
Simplified Chinese, achieve competitive accuracy on Traditional
Chinese inputs, particularly on audio-text tasks. 2) In contrast,
UnifiedIO-2-XL, with limited exposure to Chinese, often failed to
produce meaningful answers. Manual inspection of its responses
(when constraining output length to 30 tokens) revealed that in 78
cases the model echoed the first option’s Chinese description, and
in 807 cases it consistently selected option “A.” 3) Qwen2.5-Omni-
7B exhibited the longest inference time among the open-source
any-to-any models, approximately 30.8% longer than Baichuan-
Omni-1.5 (11B parameters). This suggests that parameter count is
not the sole determinant of inference speed. 4) The results reveal
a significant performance gap between open-source and closed-
source models, especially in the image-text domain, highlighting
the urgent need for dedicated Traditional Chinese fine-tuning and
more robust vision components in open-source any-to-any models.
Performance on Vision Language Models (with ASR). We
evaluated a range of VLMs using Whisper-large for audio transcrip-
tion. Table 4 reports overall accuracy, image-text accuracy, audio-
transcript-text accuracy, and inference time. Key observations are:
1) Qwen2.5-VL-7B-Instruct and UI-TARS-1.5-7B lead among the
evaluated VLMs. The competitive results from these models, devel-
oped by organizations with a strong focus on Chinese AI, suggest
that extensive pre-training on relevant Chinese-language corpora
is a crucial factor for strong performance. 2) In contrast, models like
Llama-3.2-11B-Vision-Instruct, despite their large parameter counts
or general multimodal capabilities, exhibit notably lower perfor-
mance, potentially due to less exposure to Traditional Chinese data
or specific task alignments.
Performance on Latency. Open-source any-to-any models
completed inference in a range of 467–744 seconds for the entire
900-item benchmark. In comparison, VLMs coupled with an ASR
pipeline (Whisper-large for audio transcription, then VLM for com-
prehension) required 1,187–2,131 seconds, reflecting the overhead
of the two-stage processing for audio-related tasks. In addition,
while closed-source models’ runtimes are not directly comparable
due to API encapsulation, they generally exhibit higher end-to-end
latency in practice for batch processing due to network factors,
though individual query latency might be low.
5
Conclusion and Future Work
To address the gap in evaluating Multimodal Large Language Mod-
els capable of processing visual, acoustic, and textual inputs, par-
ticularly in Traditional Chinese, we introduced Multi-TW, the
first benchmark of its kind. This dataset provides new insights
into current multimodal large language models’ abilities, includ-
ing their performance and latency on Traditional Chinese tasks.
Our evaluation reveals that while closed-source models generally
achieve strong performance across both image and audio modali-
ties, open-source alternatives currently tend to perform better on
audio-text tasks compared to image-text tasks when using any-to-
any architectures. The VLM plus ASR approach can achieve strong
results but incurs higher latency for audio tasks. We also found that
end-to-end any-to-any models offer notable latency advantages
over cascaded VLM plus ASR pipelines for processing audio inputs.
Our findings underscore the need for more appropriate architec-
ture designs and targeted fine-tuning data for robust multimodal
integration, especially for Traditional Chinese.

--- Page 6 ---

Preprint, August, 2025
Yao, et al.
Table 3: Performance of Any-to-Any Multimodal Models on Multi-TW.
Models
Overall Acc.
Image-Text Acc.
Audio-Text Acc.
Inference Time (s)
gemini-2.0-flash
0.8900
0.8800
0.9000
-
gemini-1.5-flash
0.8111
0.7644
0.8578
-
Qwen2.5-Omni-7B
0.6534
0.4156
0.8911
744
Baichuan-Omni-1.5
0.6289
0.4822
0.7756
569
Qwen2.5-Omni-3B
0.5878
0.3377
0.8378
712
UnifiedIO-2-XL
0.2589
0.2600
0.2578
467
Table 4: Performance of Vision-Language Models (VLMs) with ASR (Whisper-large) on Multi-TW.
Models
Overall Acc.
Image-Text Acc.
Audio Transcript-Text Acc.
Inference Time (s)
Qwen2.5-VL-7B-Instruct
0.8423
0.8267
0.8578
1216
Qwen2-VL-7B-Instruct
0.8033
0.7822
0.8244
1187
UI-TARS-1.5-7B
0.7823
0.7378
0.8267
2131
Llama-3.2-11B-Vision-Instruct
0.5578
0.4711
0.6444
1308
idefics2-8b
0.4167
0.5156
0.3178
1228
llava-v1.6-mistral-7b
0.4100
0.4178
0.4022
1305
llava-v1.6-vicuna-7b
0.3345
0.4022
0.2667
1302
llava-v1.5-7b
0.3211
0.3911
0.2511
1201
paligemma2-10b-pt-896
0.2600
0.2800
0.2400
1727
In future work, we will examine how cross-lingual transfer ca-
pabilities influence the performance of Simplified Chinese-trained
models on Traditional Chinese reasoning tasks. We also plan to
evaluate latency under more rigorous, parallelized experimental
conditions and explore alternative settings, such as streaming in-
ference. Furthermore, expanding Multi-TW to include generative
tasks and more complex reasoning scenarios will be a key direction.
Acknowledgments
The authors would like to thank Steering Committee for the Test
Of Proficiency-Huayu for agreeing to release the Test of Chinese
as a Foreign Language data for this study. The responsibility for
errors in fact or judgment is ours. We also extend our gratitude to
Professor Yun-Nung Chen from National Taiwan University for her
invaluable guidance and support.
References
[1] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana
Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman
Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei,
Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, Andrew Brock, Aida
Nematzadeh, Sahand Sharifzadeh, Mikolaj Binkowski, Ricardo Barreira, Oriol
Vinyals, Andrew Zisserman, and Karen Simonyan. 2022. Flamingo: a Visual
Language Model for Few-Shot Learning. arXiv:2204.14198 [cs.CV] https://arxiv.
org/abs/2204.14198
[2] Rohan Anil, Andrew M. Dai, Orhan Firat, Melvin Johnson, Dmitry Lepikhin,
Alexandre Passos, Siamak Shakeri, Emanuel Taropa, Paige Bailey, Zhifeng Chen,
Eric Chu, Jonathan H. Clark, Laurent El Shafey, Yanping Huang, Kathy Meier-
Hellstern, Gaurav Mishra, Erica Moreira, Mark Omernick, Kevin Robinson, Sebas-
tian Ruder, Yi Tay, Kefan Xiao, Yuanzhong Xu, Yujing Zhang, Gustavo Hernandez
Abrego, Junwhan Ahn, Jacob Austin, Paul Barham, Jan Botha, James Bradbury,
Siddhartha Brahma, Kevin Brooks, Michele Catasta, Yong Cheng, Colin Cherry,
Christopher A. Choquette-Choo, Aakanksha Chowdhery, Clément Crepy, Shachi
Dave, Mostafa Dehghani, Sunipa Dev, Jacob Devlin, Mark Díaz, Nan Du, Ethan
Dyer, Vlad Feinberg, Fangxiaoyu Feng, Vlad Fienber, Markus Freitag, Xavier
Garcia, Sebastian Gehrmann, Lucas Gonzalez, Guy Gur-Ari, Steven Hand, Hadi
Hashemi, Le Hou, Joshua Howland, Andrea Hu, Jeffrey Hui, Jeremy Hurwitz,
Michael Isard, Abe Ittycheriah, Matthew Jagielski, Wenhao Jia, Kathleen Kenealy,
Maxim Krikun, Sneha Kudugunta, Chang Lan, Katherine Lee, Benjamin Lee, Eric
Li, Music Li, Wei Li, YaGuang Li, Jian Li, Hyeontaek Lim, Hanzhao Lin, Zhong-
tao Liu, Frederick Liu, Marcello Maggioni, Aroma Mahendru, Joshua Maynez,
Vedant Misra, Maysam Moussalem, Zachary Nado, John Nham, Eric Ni, Andrew
Nystrom, Alicia Parrish, Marie Pellat, Martin Polacek, Alex Polozov, Reiner Pope,
Siyuan Qiao, Emily Reif, Bryan Richter, Parker Riley, Alex Castro Ros, Aurko Roy,
Brennan Saeta, Rajkumar Samuel, Renee Shelby, Ambrose Slone, Daniel Smilkov,
David R. So, Daniel Sohn, Simon Tokumine, Dasha Valter, Vijay Vasudevan,
Kiran Vodrahalli, Xuezhi Wang, Pidong Wang, Zirui Wang, Tao Wang, John Wi-
eting, Yuhuai Wu, Kelvin Xu, Yunhan Xu, Linting Xue, Pengcheng Yin, Jiahui Yu,
Qiao Zhang, Steven Zheng, Ce Zheng, Weikang Zhou, Denny Zhou, Slav Petrov,
and Yonghui Wu. 2023. PaLM 2 Technical Report. arXiv:2305.10403 [cs.CL]
https://arxiv.org/abs/2305.10403
[3] Jinze Bai, Shuai Bai, Yunfei Chu, Zeyu Cui, Kai Dang, Xiaodong Deng, Yang Fan,
Wenbin Ge, Yu Han, Fei Huang, Binyuan Hui, Luo Ji, Mei Li, Junyang Lin, Runji
Lin, Dayiheng Liu, Gao Liu, Chengqiang Lu, Keming Lu, Jianxin Ma, Rui Men,
Xingzhang Ren, Xuancheng Ren, Chuanqi Tan, Sinan Tan, Jianhong Tu, Peng
Wang, Shijie Wang, Wei Wang, Shengguang Wu, Benfeng Xu, Jin Xu, An Yang,
Hao Yang, Jian Yang, Shusheng Yang, Yang Yao, Bowen Yu, Hongyi Yuan, Zheng
Yuan, Jianwei Zhang, Xingxuan Zhang, Yichang Zhang, Zhenru Zhang, Chang
Zhou, Jingren Zhou, Xiaohuan Zhou, and Tianhang Zhu. 2023. Qwen Technical
Report. arXiv:2309.16609 [cs.CL] https://arxiv.org/abs/2309.16609
[4] Shuai Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, Sibo Song, Kai Dang,
Peng Wang, Shijie Wang, Jun Tang, Humen Zhong, Yuanzhi Zhu, Mingkun Yang,
Zhaohai Li, Jianqiang Wan, Pengfei Wang, Wei Ding, Zheren Fu, Yiheng Xu, Jiabo
Ye, Xi Zhang, Tianbao Xie, Zesen Cheng, Hang Zhang, Zhibo Yang, Haiyang Xu,
and Junyang Lin. 2025. Qwen2.5-VL Technical Report. arXiv:2502.13923 [cs.CV]
https://arxiv.org/abs/2502.13923
[5] Zalán Borsos, Raphaël Marinier, Damien Vincent, Eugene Kharitonov, Olivier
Pietquin, Matt Sharifi, Dominik Roblek, Olivier Teboul, David Grangier, Marco
Tagliasacchi, and Neil Zeghidour. 2023. AudioLM: a Language Modeling Approach
to Audio Generation. arXiv:2209.03143 [cs.SD] https://arxiv.org/abs/2209.03143
[6] Yunfei Chu, Jin Xu, Qian Yang, Haojie Wei, Xipin Wei, Zhifang Guo, Yichong
Leng, Yuanjun Lv, Jinzheng He, Junyang Lin, Chang Zhou, and Jingren Zhou.
2024. Qwen2-Audio Technical Report. arXiv:2407.10759 [eess.AS] https://arxiv.
org/abs/2407.10759
[7] Yunfei Chu, Jin Xu, Xiaohuan Zhou, Qian Yang, Shiliang Zhang, Zhijie Yan,
Chang Zhou, and Jingren Zhou. 2023.
Qwen-Audio: Advancing Univer-
sal Audio Understanding via Unified Large-Scale Audio-Language Models.
arXiv:2311.07919 [eess.AS] https://arxiv.org/abs/2311.07919

--- Page 7 ---

Multi-TW: Benchmarking Multimodal Models on Traditional Chinese Question Answering in Taiwan
Preprint, August, 2025
[8] Chan-Jan Hsu, Chang-Le Liu, Feng-Ting Liao, Po-Chun Hsu, Yi-Chang Chen, and
Da shan Shiu. 2023. Advancing the Evaluation of Traditional Chinese Language
Models: Towards a Comprehensive Benchmark Suite. arXiv:2309.08448 [cs.CL]
https://arxiv.org/abs/2309.08448
[9] Ashhadul Islam, Md. Rafiul Biswas, Wajdi Zaghouani, Samir Brahim Belhaouari,
and Zubair Shah. 2023. Pushing Boundaries: Exploring Zero Shot Object Clas-
sification with Large Multimodal Models.
arXiv:2401.00127 [cs.CV] https:
//arxiv.org/abs/2401.00127
[10] Siddique Latif, Moazzam Shoukat, Fahad Shamshad, Muhammad Usama, Yi Ren,
Heriberto Cuayáhuitl, Wenwu Wang, Xulong Zhang, Roberto Togneri, Erik Cam-
bria, and Björn W. Schuller. 2023. Sparks of Large Audio Models: A Survey and
Outlook. arXiv:2308.12792 [cs.SD] https://arxiv.org/abs/2308.12792
[11] Hugo Laurençon, Léo Tronchon, Matthieu Cord, and Victor Sanh. 2024. What
matters when building vision-language models? arXiv:2405.02246 [cs.CV] https:
//arxiv.org/abs/2405.02246
[12] Yadong Li, Jun Liu, Tao Zhang, Tao Zhang, Song Chen, Tianpeng Li, Zehuan
Li, Lijun Liu, Lingfeng Ming, Guosheng Dong, Da Pan, Chong Li, Yuanbo Fang,
Dongdong Kuang, Mingrui Wang, Chenglin Zhu, Youwei Zhang, Hongyu Guo,
Fengyu Zhang, Yuran Wang, Bowen Ding, Wei Song, Xu Li, Yuqi Huo, Zheng
Liang, Shusen Zhang, Xin Wu, Shuai Zhao, Linchu Xiong, Yozhen Wu, Jiahui
Ye, Wenhao Lu, Bowen Li, Yan Zhang, Yaqi Zhou, Xin Chen, Lei Su, Hongda
Zhang, Fuzhong Chen, Xuezhen Dong, Na Nie, Zhiying Wu, Bin Xiao, Ting Li,
Shunya Dang, Ping Zhang, Yijia Sun, Jincheng Wu, Jinjie Yang, Xionghai Lin,
Zhi Ma, Kegeng Wu, Jia li, Aiyuan Yang, Hui Liu, Jianqiang Zhang, Xiaoxi Chen,
Guangwei Ai, Wentao Zhang, Yicong Chen, Xiaoqin Huang, Kun Li, Wenjing Luo,
Yifei Duan, Lingling Zhu, Ran Xiao, Zhe Su, Jiani Pu, Dian Wang, Xu Jia, Tianyu
Zhang, Mengyu Ai, Mang Wang, Yujing Qiao, Lei Zhang, Yanjun Shen, Fan Yang,
Miao Zhen, Yijie Zhou, Mingyang Chen, Fei Li, Chenzheng Zhu, Keer Lu, Yaqi
Zhao, Hao Liang, Youquan Li, Yanzhao Qin, Linzhuang Sun, Jianhua Xu, Haoze
Sun, Mingan Lin, Zenan Zhou, and Weipeng Chen. 2025. Baichuan-Omni-1.5
Technical Report. arXiv:2501.15368 [cs.CL] https://arxiv.org/abs/2501.15368v1
[13] Yizhi Li, Ge Zhang, Yinghao Ma, Ruibin Yuan, Kang Zhu, Hangyu Guo, Yiming
Liang, Jiaheng Liu, Zekun Wang, Jian Yang, Siwei Wu, Xingwei Qu, Jinjie Shi,
Xinyue Zhang, Zhenzhu Yang, Xiangzhou Wang, Zhaoxiang Zhang, Zachary Liu,
Emmanouil Benetos, Wenhao Huang, and Chenghua Lin. 2025. OmniBench: To-
wards The Future of Universal Omni-Language Models. arXiv:2409.15272 [cs.CL]
https://arxiv.org/abs/2409.15272
[14] Zongxia Li, Xiyang Wu, Hongyang Du, Fuxiao Liu, Huy Nghiem, and Guangyao
Shi. 2025. A Survey of State of the Art Large Vision Language Models: Alignment,
Benchmark, Evaluations and Challenges. arXiv:2501.02189 [cs.CV] https://arxiv.
org/abs/2501.02189
[15] Zijing Liang, Yanjie Xu, Yifan Hong, Penghui Shang, Qi Wang, Qiang Fu, and
Ke Liu. 2024. A Survey of Multimodel Large Language Models. In Proceedings of
the 3rd International Conference on Computer, Artificial Intelligence and Control
Engineering (Xi’ an, China) (CAICE ’24). Association for Computing Machinery,
New York, NY, USA, 405–409. doi:10.1145/3672758.3672824
[16] Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. 2024. Improved Baselines
with Visual Instruction Tuning. arXiv:2310.03744 [cs.CV] https://arxiv.org/abs/
2310.03744
[17] Jiasen Lu, Christopher Clark, Sangho Lee, Zichen Zhang, Savya Khosla, Ryan
Marten, Derek Hoiem, and Aniruddha Kembhavi. 2023. Unified-IO 2: Scaling
Autoregressive Multimodal Models with Vision, Language, Audio, and Action.
arXiv:2312.17172 [cs.CV] https://arxiv.org/abs/2312.17172v1
[18] Meta. 2024. Meta Llama 3.2-11B Vision Instruct. https://huggingface.co/meta-
llama/Llama-3.2-11B-Vision-Instruct. Accessed: 2025-05-25.
[19] Jing Peng, Yucheng Wang, Yu Xi, Xu Li, Xizhuo Zhang, and Kai Yu. 2025. A
Survey on Speech Large Language Models. arXiv:2410.18908 [eess.AS] https:
//arxiv.org/abs/2410.18908
[20] Yujia Qin, Yining Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian,
Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, Wanjun Zhong, Kuanye Li, Jiale
Yang, Yu Miao, Woyu Lin, Longxiang Liu, Xu Jiang, Qianli Ma, Jingyu Li, Xiaojun
Xiao, Kai Cai, Chuang Li, Yaowei Zheng, Chaolin Jin, Chen Li, Xiao Zhou, Minchao
Wang, Haoli Chen, Zhaojian Li, Haihua Yang, Haifeng Liu, Feng Lin, Tao Peng,
Xin Liu, and Guang Shi. 2025. UI-TARS: Pioneering Automated GUI Interaction
with Native Agents. arXiv:2501.12326 [cs.AI] https://arxiv.org/abs/2501.12326
[21] Qwen, :, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen
Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang,
Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang
Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue,
Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi Tang, Tingyu Xia,
Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan,
Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. 2025. Qwen2.5 Technical
Report. arXiv:2412.15115 [cs.CL] https://arxiv.org/abs/2412.15115
[22] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh,
Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark,
Gretchen Krueger, and Ilya Sutskever. 2021. Learning Transferable Visual Models
From Natural Language Supervision. arXiv:2103.00020 [cs.CV] https://arxiv.org/
abs/2103.00020
[23] Alec Radford, Jong Wook Kim, Tao Xu, Greg Brockman, Christine McLeavey,
and Ilya Sutskever. 2022. Robust Speech Recognition via Large-Scale Weak
Supervision. arXiv:2212.04356 [eess.AS] https://arxiv.org/abs/2212.04356
[24] Paul K. Rubenstein, Chulayuth Asawaroengchai, Duc Dung Nguyen, Ankur
Bapna, Zalán Borsos, Félix de Chaumont Quitry, Peter Chen, Dalia El Badawy,
Wei Han, Eugene Kharitonov, Hannah Muckenhirn, Dirk Padfield, James Qin,
Danny Rozenberg, Tara Sainath, Johan Schalkwyk, Matt Sharifi, Michelle Tadmor
Ramanovich, Marco Tagliasacchi, Alexandru Tudor, Mihajlo Velimirović, Damien
Vincent, Jiahui Yu, Yongqiang Wang, Vicky Zayats, Neil Zeghidour, Yu Zhang,
Zhishuai Zhang, Lukas Zilka, and Christian Frank. 2023. AudioPaLM: A Large
Language Model That Can Speak and Listen. arXiv:2306.12925 [cs.CL] https:
//arxiv.org/abs/2306.12925
[25] Andreas Steiner, André Susano Pinto, Michael Tschannen, Daniel Keysers, Xiao
Wang, Yonatan Bitton, Alexey Gritsenko, Matthias Minderer, Anthony Sher-
bondy, Shangbang Long, Siyang Qin, Reeve Ingle, Emanuele Bugliarello, Sa-
har Kazemzadeh, Thomas Mesnard, Ibrahim Alabdulmohsin, Lucas Beyer, and
Xiaohua Zhai. 2024. PaliGemma 2: A Family of Versatile VLMs for Transfer.
arXiv:2412.03555 [cs.CV] https://arxiv.org/abs/2412.03555
[26] Zhi-Rui Tam, Ya-Ting Pai, Yen-Wei Lee, Jun-Da Chen, Wei-Min Chu, Sega Cheng,
and Hong-Han Shuai. 2024. An Improved Traditional Chinese Evaluation Suite
for Foundation Model. arXiv:2403.01858 [cs.CL] https://arxiv.org/abs/2403.01858
[27] Zhi Rui Tam, Ya-Ting Pai, Yen-Wei Lee, and Yun-Nung Chen. 2025. VisTW:
Benchmarking Vision-Language Models for Traditional Chinese in Taiwan.
arXiv:2503.10427 [cs.CL] https://arxiv.org/abs/2503.10427v2
[28] Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann Dubois, Xuechen Li, Carlos
Guestrin, Percy Liang, and Tatsunori B. Hashimoto. 2023. Alpaca: A Strong,
Replicable Instruction-Following Model. https://crfm.stanford.edu/2023/03/13/
alpaca.html
[29] Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne
Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro,
Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, and Guil-
laume Lample. 2023. LLaMA: Open and Efficient Foundation Language Models.
arXiv:2302.13971 [cs.CL] https://arxiv.org/abs/2302.13971
[30] Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yas-
mine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhos-
ale, Dan Bikel, Lukas Blecher, Cristian Canton Ferrer, Moya Chen, Guillem Cucu-
rull, David Esiobu, Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller, Cynthia
Gao, Vedanuj Goswami, Naman Goyal, Anthony Hartshorn, Saghar Hosseini,
Rui Hou, Hakan Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa, Isabel
Kloumann, Artem Korenev, Punit Singh Koura, Marie-Anne Lachaux, Thibaut
Lavril, Jenya Lee, Diana Liskovich, Yinghai Lu, Yuning Mao, Xavier Martinet,
Todor Mihaylov, Pushkar Mishra, Igor Molybog, Yixin Nie, Andrew Poulton,
Jeremy Reizenstein, Rashi Rungta, Kalyan Saladi, Alan Schelten, Ruan Silva,
Eric Michael Smith, Ranjan Subramanian, Xiaoqing Ellen Tan, Binh Tang, Ross
Taylor, Adina Williams, Jian Xiang Kuan, Puxin Xu, Zheng Yan, Iliyan Zarov,
Yuchen Zhang, Angela Fan, Melanie Kambadur, Sharan Narang, Aurelien Ro-
driguez, Robert Stojnic, Sergey Edunov, and Thomas Scialom. 2023.
Llama
2: Open Foundation and Fine-Tuned Chat Models. arXiv:2307.09288 [cs.CL]
https://arxiv.org/abs/2307.09288
[31] Ashmal Vayani, Dinura Dissanayake, Hasindri Watawana, Noor Ahsan, Nevasini
Sasikumar, Omkar Thawakar, Henok Biadglign Ademtew, Yahya Hmaiti, Aman-
deep Kumar, Kartik Kuckreja, Mykola Maslych, Wafa Al Ghallabi, Mihail Mi-
haylov, Chao Qin, Abdelrahman M Shaker, Mike Zhang, Mahardika Krisna Ihsani,
Amiel Esplana, Monil Gokani, Shachar Mirkin, Harsh Singh, Ashay Srivastava,
Endre Hamerlik, Fathinah Asma Izzati, Fadillah Adamsyah Maani, Sebastian
Cavada, Jenny Chim, Rohit Gupta, Sanjay Manjunath, Kamila Zhumakhanova,
Feno Heriniaina Rabevohitra, Azril Amirudin, Muhammad Ridzuan, Daniya Ka-
reem, Ketan More, Kunyang Li, Pramesh Shakya, Muhammad Saad, Amirpouya
Ghasemaghaei, Amirbek Djanibekov, Dilshod Azizov, Branislava Jankovic, Na-
man Bhatia, Alvaro Cabrera, Johan Obando-Ceron, Olympiah Otieno, Fabian
Farestam, Muztoba Rabbani, Sanoojan Baliah, Santosh Sanjeev, Abduragim
Shtanchaev, Maheen Fatima, Thao Nguyen, Amrin Kareem, Toluwani Aremu,
Nathan Xavier, Amit Bhatkal, Hawau Toyin, Aman Chadha, Hisham Cholakkal,
Rao Muhammad Anwer, Michael Felsberg, Jorma Laaksonen, Thamar Solorio,
Monojit Choudhury, Ivan Laptev, Mubarak Shah, Salman Khan, and Fahad Khan.
2025. All Languages Matter: Evaluating LMMs on Culturally Diverse 100 Lan-
guages. arXiv:2411.16508 [cs.CV] https://arxiv.org/abs/2411.16508
[32] Shengqiong Wu, Hao Fei, Leigang Qu, Wei Ji, and Tat-Seng Chua. 2024. NExT-
GPT: Any-to-Any Multimodal LLM. arXiv:2309.05519 [cs.AI] https://arxiv.org/
abs/2309.05519
[33] Jin Xu, Zhifang Guo, Jinzheng He, Hangrui Hu, Ting He, Shuai Bai, Keqin Chen,
Jialin Wang, Yang Fan, Kai Dang, Bin Zhang, Xiong Wang, Yunfei Chu, and
Junyang Lin. 2025. Qwen2.5-Omni Technical Report. arXiv:2503.20215 [cs.CL]
https://arxiv.org/abs/2503.20215v1
[34] Linting Xue, Noah Constant, Adam Roberts, Mihir Kale, Rami Al-Rfou, Aditya
Siddhant, Aditya Barua, and Colin Raffel. 2021. mT5: A massively multilingual
pre-trained text-to-text transformer. arXiv:2010.11934 [cs.CL] https://arxiv.org/
abs/2010.11934

--- Page 8 ---

Preprint, August, 2025
Yao, et al.
[35] An Yang, Baosong Yang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Zhou, Cheng-
peng Li, Chengyuan Li, Dayiheng Liu, Fei Huang, Guanting Dong, Haoran Wei,
Huan Lin, Jialong Tang, Jialin Wang, Jian Yang, Jianhong Tu, Jianwei Zhang,
Jianxin Ma, Jianxin Yang, Jin Xu, Jingren Zhou, Jinze Bai, Jinzheng He, Jun-
yang Lin, Kai Dang, Keming Lu, Keqin Chen, Kexin Yang, Mei Li, Mingfeng
Xue, Na Ni, Pei Zhang, Peng Wang, Ru Peng, Rui Men, Ruize Gao, Runji Lin,
Shijie Wang, Shuai Bai, Sinan Tan, Tianhang Zhu, Tianhao Li, Tianyu Liu,
Wenbin Ge, Xiaodong Deng, Xiaohuan Zhou, Xingzhang Ren, Xinyu Zhang,
Xipin Wei, Xuancheng Ren, Xuejing Liu, Yang Fan, Yang Yao, Yichang Zhang,
Yu Wan, Yunfei Chu, Yuqiong Liu, Zeyu Cui, Zhenru Zhang, Zhifang Guo,
and Zhihao Fan. 2024.
Qwen2 Technical Report.
arXiv:2407.10671 [cs.CL]
https://arxiv.org/abs/2407.10671
[36] Shukang Yin, Chaoyou Fu, Sirui Zhao, Ke Li, Xing Sun, Tong Xu, and Enhong
Chen. 2024. A Survey on Multimodal Large Language Models. doi:10.1093/nsr/
nwae403 arXiv:2306.13549 [cs.CV]
[37] Jun Zhan, Junqi Dai, Jiasheng Ye, Yunhua Zhou, Dong Zhang, Zhigeng Liu, Xin
Zhang, Ruibin Yuan, Ge Zhang, Linyang Li, Hang Yan, Jie Fu, Tao Gui, Tianxiang
Sun, Yugang Jiang, and Xipeng Qiu. 2024. AnyGPT: Unified Multimodal LLM
with Discrete Sequence Modeling. arXiv:2402.12226 [cs.CL] https://arxiv.org/
abs/2402.12226
[38] Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu,
Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang,
Joseph E. Gonzalez, and Ion Stoica. 2023. Judging LLM-as-a-Judge with MT-Bench
and Chatbot Arena. arXiv:2306.05685 [cs.CL] https://arxiv.org/abs/2306.05685

```
