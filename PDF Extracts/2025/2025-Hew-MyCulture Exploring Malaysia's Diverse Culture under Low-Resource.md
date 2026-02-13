---
title: "2025-Hew-MyCulture Exploring Malaysia's Diverse Culture under Low-Resource - PDF Extract"
source_pdf: "2025-Hew-MyCulture Exploring Malaysia's Diverse Culture under Low-Resource.pdf"
pages: 10
extracted_at: "2026-02-13T09:50:28.315062"
---

# PDF Extract: 2025-Hew-MyCulture Exploring Malaysia's Diverse Culture under Low-Resource

**Source PDF:** 2025-Hew-MyCulture Exploring Malaysia's Diverse Culture under Low-Resource.pdf
**Total Pages:** 10

---

## Content

```
--- Page 1 ---

MyCulture: Exploring Malaysia’s Diverse Culture under
Low-Resource Language Constraints
Zhong Ken Hew
Jia Xin Low
Sze Jue Yang
Chee Seng Chan
Universiti Malaya
Abstract
Large Language Models (LLMs) often exhibit
cultural biases due to training data dominated
by high-resource languages like English and
Chinese. This poses challenges for accurately
representing and evaluating diverse cultural
contexts, particularly in low-resource language
settings. To address this, we introduce My-
Culture, a benchmark designed to comprehen-
sively evaluate LLMs on Malaysian culture
across six pillars: arts, attire, customs, en-
tertainment, food, and religion presented in
Bahasa Melayu. Unlike conventional bench-
marks, MyCulture employs a novel open-ended
multiple-choice question format without prede-
fined options, thereby reducing guessing and
mitigating format bias. We provide a theoret-
ical justification for the effectiveness of this
open-ended structure in improving both fair-
ness and discriminative power. Furthermore,
we analyze structural bias by comparing model
performance on structured versus free-form out-
puts, and assess language bias through multilin-
gual prompt variations. Our evaluation across
a range of regional and international LLMs
reveals significant disparities in cultural com-
prehension, highlighting the urgent need for
culturally grounded and linguistically inclusive
benchmarks in the development and assessment
of LLMs.
1
Introduction
Large Language Models (LLMs), trained on tril-
lions of tokens exhibit strong generalization and
problem-solving abilities beyond simple memoriza-
tion. Fundamentally, these models are trained on
massive text corpora scraped from a vast array of
Internet sources. However, since English and Chi-
nese content dominate the web (W3Techs, 2025),
LLMs trained on such data are inherently biased to-
ward these high-resource languages, both in terms
of linguistic capability and cultural representation
(Wang et al., 2024a).
0
20
40
60
80
100
Closed Form Score
0
20
40
60
80
100
Open Ended Score
GPT-4o
GPT-4o mini
DeepSeek-V3
Llama 4 Scout
Qwen3-30B-A3B
Qwen3-8B
Qwen3-1.7B
Llama 3.2 3B
SEA-LION-v3-70B
MaLLaM Small 2.5
MaLLaM Tiny 2.5
SEA-LION-v3-8B
SeaLLMs-v3-7B
SeaLLMs-v3-1.5B
Global Models
SEA Region Models
Figure 1: Visualization of the LLMs’ scores across
both closed-form and open-ended MCQs. The top-right
quadrant denotes the optimal region, as ideally, LLMs
should be performant in both forms of MCQs.
In contrast, resource-scarce languages are of-
ten underrepresented, which limits the effective-
ness of LLMs in regions where such languages are
prevalent. This can result in culturally detached
responses that are misaligned with local values and
practices, potentially exacerbating issues of social
exclusion and racial insensitivity (Li et al., 2024).
Ideally, LLMs should exhibit cultural alignment,
particularly in a multilingual, multi-ethnic nation
such as Malaysia, where inclusivity is constitution-
ally and culturally emphasized across diverse com-
munities, including Malays, Chinese, Indians, and
indigenous groups, as well as multiple religions
such as Islam, Buddhism, and Hinduism.
To evaluate cultural alignment, recent efforts
such as Kulture (Wang et al., 2024b), IndoCul-
ture (Koto et al., 2024), SaudiCulture (Ayash
et al., 2025) have proposed country-specific cul-
tural benchmarks. While effective, these bench-
marks tend to focus on relatively homogeneous
1
arXiv:2508.05429v2  [cs.CL]  8 Aug 2025

--- Page 2 ---

cultural contexts, and thus fall short in addressing
the complexities of multi-ethnic, multi-religious
societies. A culturally inclusive benchmark that
captures this diversity remains an unmet need.
At the same time, as LLMs’ capabilities continue
to evolve, conventional multiple-choice question
(MCQ) formats have shown limitations in accu-
rately capturing models’ performance, especially
in real-world scenarios that demand free-form gen-
eration (Li et al., 2024). While MCQs are straight-
forward to construct and evaluate, their structured
nature tends to favor LLMs by significantly narrow-
ing the combinatorial search space. This increases
the likelihood of models arriving atthe correct an-
swer through pattern recognition or random guess-
ing, rather than true comprehension.
In contrast, open-ended questions are better in re-
flecting real-world use cases, requiring the model to
generate responses without being guided by prede-
fined options. However, such formats often involve
complex data collection and evaluation pipelines,
sometimes necessitating human-in-the-loop assess-
ment which makes them less scalable and less com-
monly adopted in benchmark design.
Motivated to bridge cultural gaps in a multi-
racial and multi-ethnic society, we propose My-
Culture, an expert-validated, locally contextualized
benchmark designed to evaluate LLMs’ understand-
ing and alignment with Malaysian cultural knowl-
edge. MyCulture employs a novel open-ended
multiple-choice question format without predefined
options, thereby reducing guessing and mitigating
format bias. We provide a theoretical justification
for the effectiveness of this open-ended structure in
improving both fairness and discriminative power.
The benchmark features carefully crafted questions
across diverse cultural domains to assess both fac-
tual accuracy and cultural sensitivity in model re-
sponses.
Our contributions are as follows:
• We introduce MyCulture, the first culture
benchmark for Malaysia, that is (i) presented
in Malay (Bahasa Malaysia), (ii) grounded
with locally contextualized questions, and (iii)
validated by human experts. It consists of over
2,600 questions, covering six domains across
multiple races, religions and ethnicities.
• We propose a novel open-ended MCQ struc-
ture, composed of (i) multi-answer, (ii) order-
ing and (iii) matching question types, which
significantly reduces the probability of LLMs
answering correctly via random guessing, en-
suring thorough assessment of LLMs’ under-
standing towards local culture.
• We showcase the empirical effectiveness of
MyCulture via extensive experiments. No-
tably, by simply shifting from closed-form to
open-ended MCQs, LLMs’ performance de-
teriorates at least 17%, signifying an illusion
of LLMs grasping cultural knowledge well
enough in Malaysia’s context.
2
Related Works
Cultural Benchmarks.
Assessing LLMs’ cul-
tural understanding is an ongoing effort, as prior
work (Wang et al., 2024a) demonstrates that LLMs
are culturally biased partly due to the inherent na-
ture of training corpora being dominated by web-
scraped content in high-resource languages and
cultures. With these dominant cultures embedded,
LLMs tend to reflect dominant cultural perspec-
tives, which oftentimes, neglect local norms and
sensitivities. In light of understanding the state of
LLMs cultural understanding towards a nation’s
context (e.g., Korea), Kulture (Wang et al., 2024b)
and KorNAT (Lee et al., 2024) constructed Korean-
native benchmarks from textbooks and surveys.
Meanwhile, J-MMMU (Onohara et al., 2024) re-
flects LLMs’ understanding of Japanese culture
by combining both culture-agnostic and culture-
specific tasks, outlining that LLMs’ generic capa-
bilities in a wide range of tasks do not equivalently
transfer to Japanese cultural reasoning.
Beyond single-nation benchmarks, several ef-
forts have focused on evaluating LLMs’ cultural
knowledge across a broader international scope.
For instance, Myung et al. (2024) proposed a mul-
tilingual benchmark spanning 16 countries or re-
gions, comprising 52.6k manually curated ques-
tion–answer pairs in 13 languages.
Similarly,
Chiu et al. (2025) introduced a culturally diverse
dataset containing 1,227 human-authored and veri-
fied questions covering 45 global regions, including
underrepresented areas and 17 topical domains, in
both single- and multiple-answer formats. These
works, although impactful, are frequently multi-
national in scope but monocultural at the national
level. Such evaluations would in turn, evaluate
LLMs’ cultural understanding in a siloed manner,
without considering the joint mixture of multiple
cultures within a single nation.
2

--- Page 3 ---

Evaluation methods of LLMs. Generally, to ef-
fectively assess LLMs capabilities, researchers pro-
posed to evaluate LLMs via closed-loop systems
such as MCQs. MCQs are characterized by fixed
options and objective scoring, which are highly
feasible in terms of preparing and scoring. No-
table examples of such benchmarks are MMLU
(Hendrycks et al., 2021) , CMMLU (Li et al., 2023),
MalayMMLU (Poh et al., 2024). However, with
finite options, MCQs inevitably creates a false im-
pression of LLMs are performing well, as LLMs
have higher chances of randomly guessing the cor-
rect answer. In contrast, open-ended evaluations
are promising direction of reflecting LLMs capabil-
ities in real world use cases, as evident by Arena-
Hard Auto (Li* et al., 2024) and IFEval (Zhou et al.,
2023) However, it is usually laborious to collect
such a dataset and evaluating LLMs against it poses
challenges, as the ground truth answer typically re-
quires human-in-the-loop verification.
Motivated by limitations of existing works,
we present a multi-ethnic, multi-racial cultural
benchmark for Malaysia, composed of open-ended
MCQs.
3
Theoretical Foundations of
Open-Ended MCQ Evaluation
In this section, we discuss our theoretical founda-
tion on the proposed open-ended MCQs.
3.1
Evaluation Hardness of Open-Ended
MCQs for LLMs
We provide a formal justification that open-
ended multiple-answer MCQs impose signifi-
cantly stricter evaluation constraints than conven-
tional MCQs, particularly when evaluating cultural
knowledge with language models. Our goal is to
establish that only models with true coverage over
the complete gold answer set can reliably succeed
under this evaluation protocol.
3.2
Notation and Setup
Let A be a finite answer alphabet (e.g., token
strings, phrase IDs). Each question q is associated
with a gold answer set S⋆⊂A of size k and m
number of options, i.e., |S⋆| = k ≥2. The model
receives a textual prompt x = prompt(q) and pro-
duces an output string which is post-processed into
a set of k distinct items:
ˆS = g
 fθ(x)

⊆A,
where fθ is the language model with parameters θ,
and g(·) is a deterministic extraction function (e.g.,
rule-based span extraction).
We define the exact-set accuracy as:
Acc(fθ; q) =
(
1,
if ˆS = S⋆,
0,
otherwise.
3.3
Baseline: Single answer MCQs
For conventional four-option MCQs, even a
random-guessing model frand achieves:
PMCQ = 1
4, where PMCQ = 1
m, m = 4
where m refers to number of options. This reflects
the format’s vulnerability to guessing and surface-
level pattern recognition.
3.4
Open-Ended MCQ: Factorial Decay in
Guessability
We now consider the case where the model outputs
k answers from A, chosen uniformly at random
without replacement. Then the probability of se-
lecting exactly the gold answer set is:
Pr
  ˆS = S⋆
=
1
 n
k
,
where n = |A|.
(1)
Lemma 1 (Factorial Decay).
If n = k (i.e., only
the k gold answers exist), then:
Popen = 1
k!.
Proof. In this case,
 k
k

= k!, so the model has
only one correct permutation out of k! total sets.
Example Values.
• For k = 4: Popen = 1
24 ≈4.17%
• For k = 6: Popen =
1
720 ≈0.14%
Lemma 2 (Combinatorial Gap).
Let PMCQ =
1/m and Popen = 1/
 n
k

, then:
Popen
PMCQ
= m
 n
k
 ≤m
k!,
so the open-ended format is at least k!/m times
harder than MCQ under random guessing.
3

--- Page 4 ---

3.5
Information-Theoretic Analysis
We now examine the Shannon information con-
veyed by each question format. Let I denote the
surprisal (information content) of a correct guess.
Iopen = −log2
 
1
 n
k

!
= log2
n
k

,
IMCQ = log2 m.
Example:
For n = 8 and k = 4:
8
4

= 70,
⇒
Iopen ≈log2 70 ≈6.13 bits,
IMCQ = log2 4 = 2 bits.
Thus, each open-ended MCQ provides over 3×
more evaluative signal than a standard MCQ.
3.6
Link to Autoregressive LLMs
Let the language model be autoregressive:
pθ( ˆS | x) =
k
Y
i=1
pθ(ai | x, a1, . . . , ai−1),
where ai ∈ˆS. If the model fails to assign signif-
icant probability mass to even a single culturally
correct answer aj ∈S⋆, then:
pθ( ˆS = S⋆| x) ≈0,
pushing the expected accuracy toward the hard
bound of Equation 1. This shows that only LLMs
with full coverage of the gold cultural space can
consistently succeed under this scoring scheme.
4
MyCulture
In this section, we formally introduce MyCulture, a
Malaysia-based cultural benchmark dataset, which
covers six core dimensions, namely: (i) arts, (ii)
attire, (iii) customary practices, (iv) entertainment,
(v) food and finally, (vi) religions. MyCulture is
carefully designed to include diverse races, ethnici-
ties and geographical locations within Malaysia, to
accurately reflect local norms. Additionally, it in-
corporates the proposed open-ended MCQ format,
with three variants: (i) multi-answer, (ii) ordering
and (iii) matching. These variants, ranked from
easiest to hardest, from multi-answer to matching,
with a decreasing probability of randomly guessing
the correct answer.
Entertainment
Arts
Customary
Practices
Food
Religions
Attire
Culture Dimensions
121
184
143
148
73
145
48
137
70
99
100
58
MyCulture
West Malaysia
East Malaysia
Figure 2: Regional data distribution of MyCulture in
a single format, across East and West Malaysia. The
figure illustrates the number of culturally grounded ques-
tions curated for each region, highlighting differences in
representation across the six cultural pillars. This distri-
bution reflects both regional diversity and the outcome
of quality filtering during dataset construction.
4.1
Dataset Statistics
Distribution. MyCulture consists of a total of
2,652 questions, which are equally divided into
1,326 closed-form and open-ended MCQs, respec-
tively. Each set of the MCQs (closed-form/open-
ended) consists of questions from six main cultural
dimensions across East and West Malaysia, where
the distributions are depicted in Figure 2. Notably,
both the closed-form and open-ended MCQs are
rigorously validated by local experts, ensuring the
quality and validity of the questions.
Language. The MCQs are constructed in Malay
(known as Bahasa Malaysia), which is the national
language of Malaysia. Since Malay is markedly a
low-resource language, construction of the dataset
involves extensive human validation to ensure its
correctness.
4.2
Question Structure
Multi-Answer (MA) MCQs. In a conventional
closed-form manner, MCQs contain multi-answer
questions that present N statements (e.g., I, II, III)
for LLMs to select from, and typically, these ques-
tions offer one correct answer that consists of all
correct statements. We further transform such MA
MCQs into their open-ended counterparts, by en-
coding the statements as the answer choices (see
Table 1 for a comparison). With such a transfor-
mation to open-ended MA MCQs, we reduced the
probability of random guessing to:
4

--- Page 5 ---

PMA
 A

=
1
m
X
r=1
mCr
; where m = N
(2)
where r denotes the number of choices to be se-
lected from a pool of m options, and PMA(A) <
PMCQ(A).
Ordering (O) MCQs are a set of MCQs that re-
quires LLMs to rearrange a sequence of N state-
ments into a chronological order and in a closed-
form manner, they present m choices with a prede-
fined fixed orders, similar to normal MCQs. The
open-ended form of O-MCQs requires LLMs to
provide all of the correct statements, in an “exact”
manner. The probability of guessing the correct
sequence correctly is formulated as:
PO
 A

=
1
m
X
r=1
mP r
; where m = N
(3)
Such
a
formulation
guarantees
PO(A)
<
PMCQ(A).
Matching (M) MCQs are tasked evaluate LLMs’
capabilities in associating N items from two sets
of options. For closed-form formats, M-MCQs
possess no difference compared to conventional
MCQs; however, in the open-ended form, to accu-
rately answer such MCQs, LLMs are required to
generate the correct pair by matching options from
the two sets. The probability of getting the correct
answer is as follows:
PM
 A

=
1
Qm
n=1 n2 ; where m = N,
m > 1
(4)
where PM(A) < PMCQ(A).
These three formats are designed to expand the
effective combinatorial search space inherent to
open-ended MCQs, thereby substantially reducing
the probability of correct responses through ran-
dom guessing. Figure 3 presents a comparative
visualization of the probability of selecting the cor-
rect answer under the proposed formulations versus
the closed-form MCQs format with predefined op-
tions. The x-axis denotes the number of options
(for closed-form MCQs ) or the number of state-
ments (for open-ended MCQs formats), demon-
strating that the probability of random correctness
1
2
3
4
5
6
7
8
9
10
Number of Options
10
12
10
10
10
8
10
6
10
4
10
2
100
P(A)
MCQs
Multi Answer (MA) MCQs
Ordering (O) MCQs
Matching (M) MCQs
Figure 3: Visualization of the probability of correctly
answering by random guessing under the closed-form
format and the proposed open-ended format.
decreases as this number increases. Notably, the
decline in probability is markedly steeper for the
three proposed formats than for the closed-form
MCQs format, indicating a substantial increase in
task difficulty. This formulation ensures the follow-
ing probabilistic ordering:
PM(A) < PO(A) < PMA(A) < PMCQ(A)
As evident in Figure 3, a typical 4-option MCQ
will yield P(A) = 0.25, while PMA(A) = 0.0667,
PMA(A) = 0.0156 and PM(A) = 0.0017, respec-
tively, signifying an increased difficulty in guess-
ing the correct answer. Such a design mitigates
format-induced biases and facilitates a more rigor-
ous and discriminative evaluation of model capa-
bilities across diverse reasoning tasks, specifically
for cultural understanding.
5
Experiment & Analysis
In this section, we rigorously evaluate LLMs’ per-
formance against MyCulture, via extensive empiri-
cal experiments.
5.1
Experiment Setting
We evaluate a total of 14 LLMs under zero-shot
settings, which includes latest closed-source mod-
els (GPT-4o, GPT-4o mini) (Achiam et al., 2023),
open-source models such as DeepSeek-V3 (Liu
et al., 2024), Qwen3 (Yang et al., 2025), Llama
(Dubey et al., 2024) and LLMs trained on predomi-
nantly on Southeast Asia (SEA) data which include
SEA-LLM (Nguyen et al., 2023), SEA-LION (Ng
5

--- Page 6 ---

et al., 2025), MaLLaM (Zolkepli et al., 2024). All
of the models are evaluated against both closed-
form and open-ended MCQs, and we outline the
results in Table 2.
5.2
Experiment Results
We reported zero-shot results of 14 LLMs on 2 for-
mats of MyCulture, closed-form and open-ended
MCQs, in Table 2. In Figure 1, we visualize the
performance of these LLMs, where the top-right
quadrant denotes the ideal performance.
Closed-form MCQs. Based on Table 2, the GPT
series consistently achieves the highest overall per-
formance, with GPT-4o and GPT-4o mini rank-
ing first and second, respectively. Among open-
source models, SEA-LION (70B) attains the best
performance, suggesting that fine-tuning on South-
east Asian data improves cultural alignment with
Malaysian contexts. Additionally, models with
over 100B parameters (Deepseek-V3; Llama-4
Scout) exhibit comparable performance, scoring
around 62%. In the sub-10B category, Qwen3
(8B) outperforms its peers, demonstrating competi-
tive cultural understanding despite its smaller size.
Within Southeast Asian regional models, SEA-
LION (70B) leads in performance, likely due to
its larger parameter count. Notably, MaLLaM, a
Malaysia-centric LLM achieves performance on
par with prominent international models such as
DeepSeek-V3, Qwen3 (30B-A3B), and Llama 4
Scout, highlighting its effectiveness in capturing
Malaysia-specific cultural knowledge.
Open-ended MCQs. In open-ended MCQ settings,
we observe a similar performance trend among
LLMs, with GPT-4o consistently achieving the best
results and SEA-LION (70B) emerging as the top
performer among open-source models. Despite
this consistency, transitioning from closed-form
to open-ended MCQs causes a substantial perfor-
mance decline across all evaluated models. As il-
lustrated in Table 2, this degradation varies widely
among models, ranging from a maximum drop of
42.68 points for MaLLaM Tiny (2.5B) to a min-
imum of 17.27 points for Qwen3 (1.7B). These
results indicate that relying solely on closed-form
MCQs may create an illusion of higher model com-
petence. The absence of explicit answer options in
open-ended MCQs demands that LLMs not only
interpret the cultural context embedded within each
question but also independently generate accurate
responses. This requirement necessitates a nuanced
and thorough understanding of Malaysian culture,
0-shot
1-shot
2-shot
3-shot
Number of Shots
30
40
50
60
70
80
Accuracy (%)
GPT-4o (MCQ Options)
GPT-4o (Open-ended)
Deepseek-v3 (MCQ Options)
Deepseek-v3 (Open-ended)
Figure 4: Comparison of model performance under nor-
mal and proposed formats across different shot settings.
Notably, there is no apparent trend of improvements
across increasing number of shots.
significantly increasing the complexity of the task.
Therefore, open-ended MCQs constitute a more
rigorous and insightful evaluation paradigm and
should be adopted in future assessments of LLMs’
capabilities.
Insights. As shown in Figure 1, most models per-
form better on the closed-form version of MyCul-
ture, as majority of them score above the 50% mark.
In contrast, in open-ended MCQs with identical
contents, LLMs consistently have sub-par perfor-
mance compared to their closed-form counterparts
(<50%).
5.3
Ablation Study
Few-shot examples.
Following prior work on
benchmarks (Poh et al., 2024), we also investigate
the effect of few-shot prompting on LLM perfor-
mance. In the few-shot setting, we randomly sam-
ple a number of examples from the MyCulture
dataset and include them in the system prompt.
To ensure a fair evaluation, any question appear-
ing in the prompt is excluded from the test set.
Figure 4 presents the performance of GPT-4o and
DeepSeek-V3 across varying shot configurations.
The results show minimal variation in performance
across different shot counts, consistent with previ-
ous findings (Li et al., 2023) that few-shot prompt-
ing provides limited benefit in cultural understand-
ing tasks.
Structured and unstructured outputs. (Raspanti
et al., 2025) studies the effect of constraining LLMs
with specific structures (i.e., limiting the set of pos-
sible output tokens), in terms of grammatical struc-
tures. However, the effect of such constrained de-
6

--- Page 7 ---

Closed-form MCQs
Open-ended MCQs
Multiple-answer MCQs
Question: Yang manakah antara berikut berkaitan dengan
makanan tradisional Malaysia?
Pernyataan:
I. Nasi lemak biasanya dihidang dengan sambal dan telur.
II. Satay berasal dari Thailand.
III. Rendang sering disediakan semasa perayaan.
IV. Kuih-muih tradisional hanya popular di Sabah.
Pilihan:
A. I, III
B. I, II, III
C. II, IV
D. I, III, IV
Answer: A
Question: Yang manakah berkaitan dengan makanan
tradisional Malaysia?
A. Nasi lemak dihidang dengan sambal dan telur
B. Satay berasal dari Thailand
C. Rendang disediakan semasa perayaan
D. Kuih tradisional hanya popular di Sabah
Answer: A, C
Matching MCQs
Question: Padankan pakaian tradisional dengan negeri asal.
Kumpulan A:
A. Baju Melayu Cekak Musang
B. Baju Kurung Teluk Belanga
C. Busana Iban
D. Baju Bodo
Kumpulan B:
i. Johor
ii. Sarawak
iii. Sabah
iv. Terengganu
Pilihan:
A: A-iv, B-i, C-ii, D-iii
B: A-iv, B-ii, C-i, D-iii
C: A-iv, B-iii, C-i, D-ii
D: A-iv, B-ii, C-iii, D-i
Answer: A
Question: Padankan pakaian tradisional dengan negeri asal.
A. Baju Melayu Cekak Musang
B. Baju Kurung Teluk Belanga
C. Busana Iban
D. Baju Bodo
i. Terengganu
ii. Johor
iii. Sarawak
iv. Sabah
Answer: A-i, B-ii, C-iii, D-iv
Ordering MCQs
Question: Susun aktiviti utama dalam sambutan Tahun Baru
Cina di Malaysia.
Pernyataan:
I. Mengemas rumah
II. Makan besar bersama keluarga
III. Memberi angpau
IV. Persembahan tarian singa
Pilihan: A. I, II, III, IV
B. II, I, III, IV
C. I, III, II, IV
D. I, II, IV, III
Answer: A
Question: Susun aktiviti utama dalam sambutan Tahun Baru
Cina di Malaysia.
A. Mengemas rumah
B. Makan besar bersama keluarga
C. Memberi angpau
D. Persembahan tarian singa
Answer: A, B, C, D
Table 1: Examples of open-ended MCQs reformulated from their closed-form counterparts. The contents of the
MCQs are similar across both forms, however, in open-ended MCQs, instead of selecting a single correct answer,
LLMs are required to provide the exact answer, for multi-answer, matching and ordering MCQs.
coding is unexplored in cultural nuances. Hence,
we investigate the effect of structured outputs in
terms of Malaysia culture, by evaluate LLMs in
2 different output settings, structured output and
free form generation (unstructured output). Table
3 presents the performance of various LLMs under
two different output formats. In general, LLMs
perform better with structured outputs, suggesting
that guiding models to follow a predefined format
can enhance their accuracy in answering MCQs.
This improvement is likely due to the constraint
that helps LLMs focus on generating the intended
answer that is complex as show in Table 3 rather
than producing lengthy explanations, which may in-
clude hallucinations or omit the answer altogether,
which is coherent with prior works (Raspanti et al.,
2025; Banerjee et al., 2025). However, DeepSeek-
V3 failed to adhere to the predefined JSON schema,
showing a significant degradation from unstruc-
tured to structured outputs.
Language biases.
We examine the impact of
prompt language on LLM performance with My-
Culture. Myung et al. (2024) shows that LLMs per-
form better when language and culture are aligned.
However, their study involves cultures that are ex-
pressed in a single language, which differ from
7

--- Page 8 ---

Company
Models
# Param
Source
Closed-form MCQs
Open-ended MCQs
Diff
Open-AI
GPT-4o
-
Close
67.87
38.39
-29.48
GPT-4o mini
-
Close
65.00
33.86
-31.14
Deepseek
Deepseek-V3*
37B (671B)
Open
62.89
37.17
-25.72
Qwen
Qwen3*
3.3B (30B)
Open
60.48
26.01
-34.47
Qwen3
8B
Open
59.95
31.74
-28.21
Qwen3
1.7B
Open
36.65
19.38
-17.27
META
Llama 4 - Scout*
17B (109B)
Open
62.30
31.28
-31.02
Llama-3.2
3B
Open
29.41
2.71
-26.70
Southeast Asian Region LLM
SEALLM
SeaLLMs-v3
7B
Open
45.63
21.87
-23.76
SeaLLMs-v3
1.5B
Open
43.06
0.83
-42.23
SEA-Lion
SEA-LION-V3
70B
Open
64.17
37.85
-26.32
SEA-LION-V3
8B
Open
47.05
22.40
-24.65
Mesolitica
MaLLaM Small 2.5
-
Close
61.53
19.45
-42.08
MaLLaM Tiny 2.5
-
Close
61.38
18.70
-42.68
Table 2: Performance of LLMs on closed-form MCQs and open-ended MCQs. * indicates Mixture of Expert (MoE)
models. Bold indicates the highest performance across all models. Underline indicates the highest performance
among Southeast Asian regional LLMs. Diff indicates the performance differences between closed-form and
open-ended MCQs. Best viewed in color.
Company
Model
# Param
Unstructured
Structured
Diff
OpenAI
GPT-4o
-
38.39
41.03
+2.64
GPT-4o mini
-
33.86
37.40
+3.54
Deepseek
Deepseek-V3*
37B (671B)
37.17
2.87
-34.30
Qwen
Qwen3*
3.3B (30B)
26.01
30.24
+4.23
Qwen3
8B
31.74
27.98
-3.76
Qwen3
1.7B
19.38
18.10
-1.28
Meta
Llama 4 - Scout*
17B (109B)
31.28
29.71
-1.57
Llama-3.2
3B
2.71
17.94
+15.23
Southeast Asian Regional LLMs
SEALLM
SeaLLMs-v3
7B
21.87
12.90
-8.97
SeaLLMs-v3
1.5B
0.83
8.14
+7.31
SEA-LION
SEA-LION-V3
70B
37.85
43.06
+5.21
SEA-LION-V3
8B
22.40
26.92
+4.52
Mesolitica
MaLLaM Small 2.5
-
19.45
38.31
+18.86
MaLLaM Tiny 2.5
-
18.70
38.15
+19.45
Table 3: Performance of LLMs on closed-form and open-ended MCQs. * indicates Mixture of Expert (MOE)
models. Bold indicates the highest performance across all models. Underline indicates the highest performance
among Southeast Asian regional LLMs. Diff shows the performance differences between structured and unstructured
outputs. DeepSeek’s performance is greyed out as it fails to follow the system prompt for generating structured
output, resulting in significantly lower scores. Best viewed in color.
multi-lingual country like Malaysia, that often-
times, express a single culture in multiple lan-
guages, which remain underexplored in the domain
of LLMs. Hence, we study the effect of a culture
across multiple languages, by augmenting the in-
structions to LLMs into different local languages,
as depicted in Table 4. In contrast to the findings
of Myung et al. (2024), our results suggest that
using the local language (Malay) does not lead to
improved performance. Instead, prompts in high-
resource languages such as English and Chinese
yield significantly better results. This discrepancy
8

--- Page 9 ---

Company
Models
Malay Prompt
English Prompt
Chinese Prompt
Open-AI
GPT-4o
38.39
38.98
37.93
GPT-4o mini
33.86
34.31
34.69
Deepseek
Deepseek-v3
37.17
40.79
39.29
SEA-Lion
SEA-LION-V3 (70b)
37.85
39.14
39.51
SEA-LION-V3 (8b)
22.40
8.06
20.13
Mesolitica
MaLLam small 2.5
19.45
23.53
25.56
MaLLam tiny 2.5
18.70
23.60
25.64
Table 4: Overall performance across different language system prompts on MyCulture. Bold indicates the highest
performance of models across different languages of the same question.
may stem from the low-resource nature of Malay,
while Chinese and English benefit from broader
pretraining coverage. Furthermore, the strong per-
formance under Chinese and English prompts im-
plies that LLMs primarily acquire knowledge of
Malaysian culture through these languages.
6
Conclusion
In this paper, we introduced MyCulture, a cul-
turally grounded benchmark designed to evalu-
ate LLMs’ understanding of Malaysia’s multi-
ethnic and multi-religious context. Unlike prior
benchmarks that focus on culturally homogeneous
settings, MyCulture captures the diversity of
Malaysian society through 2,600 questions written
in Bahasa Malaysia, composed of both closed-form
and open-ended multiple-choice formats across six
cultural domains. To address limitations of con-
ventional MCQs, which often inflate LLM perfor-
mance through format-induced bias, we proposed
a novel open-ended structure comprising multi-
answer, ordering, and matching types without pre-
defined options. Our empirical analysis shows that
simply shifting to this open-ended format leads
to a ≥17% drop in model accuracy, revealing an
overestimation of LLMs’ true cultural comprehen-
sion. These findings underscore the importance
of culturally contextualized and structurally robust
benchmarks for fair and meaningful evaluation of
LLM capabilities.
References
Josh Achiam, Steven Adler, Sandhini Agarwal, Lama
Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
Diogo Almeida, Janko Altenschmidt, Sam Altman,
Shyamal Anadkat, and 1 others. 2023. Gpt-4 techni-
cal report. arXiv preprint arXiv:2303.08774.
Lama Ayash, Hassan Alhuzali, Ashwag Alasmari,
and Sultan Aloufi. 2025. Saudiculture: A bench-
mark for evaluating large language models’ cultural
competence within saudi arabia. Journal of King
Saud University Computer and Information Sciences,
37(6):123.
Debangshu Banerjee, Tarun Suresh, Shubham Ugare,
Sasa Misailovic, and Gagandeep Singh. 2025. Crane:
Reasoning with constrained llm generation. Preprint,
arXiv:2502.09061.
Yu Ying Chiu,
Liwei Jiang,
Bill Yuchen Lin,
Chan Young Park, Shuyue Stella Li, Sahithya Ravi,
Mehar Bhatia, Maria Antoniak, Yulia Tsvetkov,
Vered Shwartz, and Yejin Choi. 2025.
Cultural-
bench: A robust, diverse, and challenging cultural
benchmark by human-ai culturalteaming. Preprint,
arXiv:2410.02677.
Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey,
Abhishek Kadian, Ahmad Al-Dahle, Aiesha Letman,
Akhil Mathur, Alan Schelten, Amy Yang, Angela
Fan, and 1 others. 2024. The llama 3 herd of models.
arXiv e-prints, pages arXiv–2407.
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,
Mantas Mazeika, Dawn Song, and Jacob Steinhardt.
2021. Measuring massive multitask language under-
standing. Preprint, arXiv:2009.03300.
Fajri Koto, Rahmad Mahendra, Nurul Aisyah, and Tim-
othy Baldwin. 2024. Indoculture: Exploring geo-
graphically influenced cultural commonsense reason-
ing across eleven indonesian provinces. Transac-
tions of the Association for Computational Linguis-
tics, 12:1703–1719.
Jiyoung Lee, Minwoo Kim, Seungho Kim, Junghwan
Kim, Seunghyun Won, Hwaran Lee, and Edward
Choi. 2024. Kornat: Llm alignment benchmark for
korean social values and common knowledge. arXiv
preprint arXiv:2402.13605.
Cheng Li, Mengzhuo Chen, Jindong Wang, Sunayana
Sitaram, and Xing Xie. 2024. Culturellm: Incorpo-
rating cultural differences into large language models.
Advances in Neural Information Processing Systems,
37:84799–84838.
9

--- Page 10 ---

Haonan Li, Yixuan Zhang, Fajri Koto, Yifei Yang, Hai
Zhao, Yeyun Gong, Nan Duan, and Timothy Bald-
win. 2023. Cmmlu: Measuring massive multitask
language understanding in chinese. arXiv preprint
arXiv:2306.09212.
Tianle Li*, Wei-Lin Chiang*, Evan Frick, Lisa Dunlap,
Banghua Zhu, Joseph E. Gonzalez, and Ion Stoica.
2024. From live data to high-quality benchmarks:
The arena-hard pipeline.
Wangyue Li, Liangzhi Li, Tong Xiang, Xiao Liu, Wei
Deng, and Noa Garcia. 2024. Can multiple-choice
questions really be useful in detecting the abilities of
llms? Preprint, arXiv:2403.17752.
Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang,
Bochao Wu, Chengda Lu, Chenggang Zhao, Chengqi
Deng, Chenyu Zhang, Chong Ruan, and 1 others.
2024. Deepseek-v3 technical report. arXiv preprint
arXiv:2412.19437.
Junho Myung, Nayeon Lee, Yi Zhou, Jiho Jin, Rifki Pu-
tri, Dimosthenis Antypas, Hsuvas Borkakoty, Eunsu
Kim, Carla Perez-Almendros, Abinew Ali Ayele, and
1 others. 2024. Blend: A benchmark for llms on ev-
eryday knowledge in diverse cultures and languages.
Advances in Neural Information Processing Systems,
37:78104–78146.
Raymond Ng, Thanh Ngan Nguyen, Yuli Huang,
Ngee Chia Tai, Wai Yi Leong, Wei Qi Leong, Xi-
anbin Yong, Jian Gang Ngui, Yosephine Susanto,
Nicholas Cheng, and 1 others. 2025. Sea-lion: South-
east asian languages in one network. arXiv preprint
arXiv:2504.05747.
Xuan-Phi Nguyen, Wenxuan Zhang, Xin Li, Mahani
Aljunied, Zhiqiang Hu, Chenhui Shen, Yew Ken
Chia, Xingxuan Li, Jianyu Wang, Qingyu Tan, and
1 others. 2023. Seallms–large language models for
southeast asia. arXiv preprint arXiv:2312.00738.
Shota Onohara, Atsuyuki Miyai, Yuki Imajuku, Kazuki
Egashira, Jeonghun Baek, Xiang Yue, Graham Neu-
big, and Kiyoharu Aizawa. 2024.
Jmmmu: A
japanese massive multi-discipline multimodal un-
derstanding benchmark for culture-aware evaluation.
arXiv preprint arXiv:2410.17250.
Soon Poh, Sze Jue Yang, Jeraelyn Tan, Lawrence
Chieng, Jia Tan, Zhenyu Yu, Foong Mun, and
Chee Seng Chan. 2024. Malaymmlu: A multitask
benchmark for the low-resource malay language. In
Findings of the Association for Computational Lin-
guistics: EMNLP 2024, pages 650–669.
Federico Raspanti, Tanir Ozcelebi, and Mike Holen-
derski. 2025. Grammar-constrained decoding makes
large language models better logical parsers. In Pro-
ceedings of the 63rd Annual Meeting of the Associa-
tion for Computational Linguistics (Volume 6: Indus-
try Track), pages 485–499.
W3Techs. 2025.
Usage statistics of content lan-
guages for websites.
https://w3techs.com/
technologies/overview/content_language.
Accessed: 2025-08-07.
Wenxuan Wang, Wenxiang Jiao, Jingyuan Huang, Ruyi
Dai, Jen tse Huang, Zhaopeng Tu, and Michael R.
Lyu. 2024a. Not all countries celebrate thanksgiving:
On the cultural dominance in large language models.
Preprint, arXiv:2310.12481.
Xiaonan Wang, Jinyoung Yeo, Joon-Ho Lim, and
Hansaem Kim. 2024b.
Kulture bench: A bench-
mark for assessing language model in korean cultural
context. arXiv preprint arXiv:2412.07251.
An Yang, Anfeng Li, Baosong Yang, Beichen Zhang,
Binyuan Hui,
Bo Zheng,
Bowen Yu,
Chang
Gao, Chengen Huang, Chenxu Lv, and 1 others.
2025.
Qwen3 technical report.
arXiv preprint
arXiv:2505.09388.
Jeffrey Zhou, Tianjian Lu, Swaroop Mishra, Siddhartha
Brahma, Sujoy Basu, Yi Luan, Denny Zhou, and
Le Hou. 2023. Instruction-following evaluation for
large language models. Preprint, arXiv:2311.07911.
Husein Zolkepli, Aisyah Razak, Kamarul Adha, and Ar-
iff Nazhan. 2024. Mallam–malaysia large language
model. arXiv preprint arXiv:2401.14680.
10

```
