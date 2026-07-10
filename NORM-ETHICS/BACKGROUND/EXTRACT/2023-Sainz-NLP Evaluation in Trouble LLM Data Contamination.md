---
title: "2023-Sainz-NLP Evaluation in Trouble LLM Data Contamination - Background Extract"
source_pdf: "2023-Sainz-NLP Evaluation in Trouble LLM Data Contamination.pdf"
source_folder: "02-external-papers"
pages: 12
extracted_at: "2026-04-03T10:25:00"
---

# Background Extract: 2023-Sainz-NLP Evaluation in Trouble LLM Data Contamination

**Source PDF:** 2023-Sainz-NLP Evaluation in Trouble LLM Data Contamination.pdf
**Source:** 02-external-papers
**Total Pages:** 12

---

## Content

```
--- Page 1 ---

NLP Evaluation in trouble:
On the Need to Measure LLM Data Contamination for each Benchmark
Oscar Sainz1 Jon Ander Campos2 Iker García-Ferrero1 Julen Etxaniz1
Oier Lopez de Lacalle1 Eneko Agirre1
1 HiTZ Center - Ixa, University of the Basque Country UPV/EHU
{oscar.sainz,iker.graciaf,julen.etxaniz}@ehu.eus
{oier.lopezdelacalle,e.agirre}@ehu.eus
2 Cohere
jonander@cohere.com
Abstract
In this position paper, we argue that the classi-
cal evaluation on Natural Language Processing
(NLP) tasks using annotated benchmarks is in
trouble. The worst kind of data contamination
happens when a Large Language Model (LLM)
is trained on the test split of a benchmark, and
then evaluated in the same benchmark. The ex-
tent of the problem is unknown, as it is not
straightforward to measure.
Contamination
causes an overestimation of the performance
of a contaminated model in a target benchmark
and associated task with respect to their non-
contaminated counterparts. The consequences
can be very harmful, with wrong scientific con-
clusions being published while other correct
ones are discarded. This position paper de-
fines different levels of data contamination and
argues for a community effort, including the
development of automatic and semi-automatic
measures to detect when data from a bench-
mark was exposed to a model, and suggestions
for flagging papers with conclusions that are
compromised by data contamination.
1
Introduction
At the core of NLP as a discipline, there is rigor-
ous evaluation on different tasks. The experimental
protocols involve strict control over the data, espe-
cially test data, which needs to be totally unseen
during development, but also over training and de-
velopment data. This is essential to assess the per-
formance of a model in zero-shot, few-shot, or fully
supervised settings. Since fine-tuning and prompt-
ing of Large Language Models (LLMs) became
commonplace (Min et al., 2021) it has been increas-
ingly difficult to enforce those strict protocols. Pre-
training LLMs is expensive, and therefore, most of
the time, researchers use LLMs trained by third-
party entities (Raffel et al., 2020; Touvron et al.,
2023a), which are agnostic to the target tasks where
those LLMs are going to be used. With the grow-
ing scale of LLMs (Kaplan et al., 2020; Henighan
et al., 2020) the need for data has been solved by
crawling the internet, reaching trillions of tokens
(Touvron et al., 2023a), and making it very hard
to know whether a specific benchmark was used
to train the LLM. This is applicable to all models,
even if they document the source of the data at a
high level, but especially for closed models with
no or insufficient documentation.
Data contamination has two consequences. The
first one is that the performance of an LLM when
evaluated on a benchmark it already processed dur-
ing pre-training will be overestimated, causing it
to be preferred with respect to other LLMs. This
affects the comparative assessment of the quality
of LLMs. The second is that papers proposing sci-
entific hypotheses on certain NLP tasks could be
using contaminated LLMs, and thus make wrong
claims about their hypotheses, and invalidate alter-
native hypotheses that could be true. This second
consequence has an enormous negative impact on
our field and is our main focus.
There are several measures that the community
could take. A possible solution would be to avoid
all research involving datasets which include pub-
lished test data, and focus on datasets where the
test data labels are not public. This solution will
severely affect the number of NLP tasks for which
benchmarks exist, at least until new benchmarks
that avoid data leakage are produced. Jacovi et al.
(2023) presents preventative strategies to avoid con-
tamination in the future.
In this position paper, we propose a complemen-
tary line of action which seeks to measure and doc-
ument data contamination cases, specifying LLM,
benchmark and evidence supporting contamination.
This solution involves a registry of contamination
cases1, collaborative manual work and research on
automatic approaches. In addition, conferences
should devise mechanisms to ensure that papers
1Such as the LM Contamination Index https://
hitz-zentroa.github.io/lm-contamination/
arXiv:2310.18018v1  [cs.CL]  27 Oct 2023

--- Page 2 ---

don’t include conclusions involving contamination,
and to flag past work where contamination has been
discovered after publication.
The paper starts by introducing background, fol-
lowed by a definition of data contamination, con-
tamination at different steps, methods to measure
data contamination and a call for action.
2
Background
Detection of contamination cases has been tradi-
tionally done by directly analyzing the training data
(Dodge et al., 2021), but the current scale of the
pre-training data makes it difficult (Kreutzer et al.,
2022; Birhane et al., 2021). Without proper doc-
umentation and search tools like ROOTS (Piktus
et al., 2023) it is very difficult for any researcher to
actually know whether their datasets are compro-
mised on a given model. More recently, this task
became even harder, as the best-performing LLMs
are deployed as products, and therefore, their train-
ing corpora are kept secret. In this case, it has
been shown that the high memorization abilities of
LLMs can be used to generate portions of the train-
ing texts (Carlini et al., 2021; Magar and Schwartz,
2022). Using this memorization property, Sainz
et al. (2023) show that ChatGPT generates portions
of popular NLP benchmarks. Furthermore, LLMs
memorization has been studied on data-leakage
scenarios (Elangovan et al., 2021).
Regarding data contamination cases,
Dodge
et al. (2021) exposed that the C4 corpus (Raf-
fel et al., 2020), a corpus used to pre-train sev-
eral LLMs such as T5 (Raffel et al., 2020), con-
tained the test splits of several benchmarks that
were crawled from GitHub.
Moreover, Brown
et al. (2020) acknowledged a bug in their filter-
ing script that caused the contamination of several
benchmarks during the GPT-3 training. Further-
more, OpenAI (2023) stated that parts of the BIG-
bench (Srivastava et al., 2023) benchmark were
inadvertently mixed into the training set, enough
to stop them from evaluating the model on it. They
also mention that they included parts of the training
sets of MATH (Hendrycks et al., 2021) and GSM-
8K (Cobbe et al., 2021) as training data to improve
mathematical reasoning (OpenAI, 2023). There-
fore, the performance results reported for GSM-8K
cannot be taken as zero-shot results when compared
to other models.
Recently, Sainz et al. (2023) reported that
several benchmarks have already been com-
promised in ChatGPT, including the popular
CoNLL2003 (Tjong Kim Sang and De Meulder,
2003). There are several preprints that evaluate
ChatGPT on CoNLL03 (Wei et al., 2023; Li et al.,
2023a; Han et al., 2023) and at least one confer-
ence paper published on ACL 2023 that evaluates
GPT-3 (Brown et al., 2020) and Codex (Chen et al.,
2021) on the same benchmark (Li et al., 2023b).
Appendix A shows evidence for data contamination
for those LLMs, and casts doubts on the conclu-
sions of those papers.
3
Defining data contamination
In general, data contamination refers to any breach
in the strict control of datasets required by the ex-
perimental protocol. In this paper, we focus on the
specific case where a LLM has processed the eval-
uation benchmark during its pre-training. However,
different types of contamination exist and each of
them has different implications. In this section, we
present three types of contamination: guideline,
text and annotation.
Guideline contamination
happens when the an-
notation guidelines for a specific dataset are seen
by the model. Usually, for specialized annotations,
highly detailed guidelines are required. The guide-
lines can usually be publicly found on the internet,
even for datasets that are not public or require buy-
ing a license for their use, ACE05 (Walker et al.,
2006) for example. The more details the guide-
lines have the more information and examples they
provide. A model aware of the guidelines for a spe-
cific task or dataset has advantages over a model
without such information. We should consider the
guideline contamination, especially on zero and
few-shot evaluations.
Raw text contamination
happens when the orig-
inal text (previous to annotation) is seen by the
model. Some examples of this type of contami-
nation are the datasets based on Wikipedia texts.
Wikipedia is commonly used as a source of pre-
training data, but, it is also a frequent source of
text to create new datasets. MultiCoNER 2 (Fetahu
et al., 2023), a Named Entity Recognition dataset
based on Wikipedia links and Wikidata informa-
tion, is an example of this phenomenon. Models
that have already seen Wikipedia in its original
form (including the markup annotations) have more
information to better identify a part of the annota-
tions (the entity boundaries) of the dataset. As

--- Page 3 ---

pointed out by Dodge et al. (2021), other datasets
built from the web such as IMDB (Maas et al.,
2011) and CNN/DailyMail (Hermann et al., 2015)
can be also compromised. This kind of contamina-
tion should be taken into account when developing
automatically annotated datasets.
Annotation contamination
happens when the
annotations (labels) of the target benchmark are
exposed to the model during training. Depending
on the splits of the benchmark that have been ex-
posed, we can have the following cases: (1) When
the evaluation split is involved, the experiment is
completely invalidated. This is the most harmful
level of contamination. (2) When the train or de-
velopment splits are involved, this would not affect
comparisons with other models that have been de-
veloped using those same splits, but it does inval-
idate conclusions claiming zero-shot or few-shot
performance.
4
Contamination on different steps
Currently, the standard procedure to train and de-
ploy language models has three main steps: pre-
training a language model, fine-tuning the model to
follow instructions and/or align with human feed-
back; and an iterative improvement step after de-
ployment. Data contamination does not only occur
in the pre-training step of LLMs, but can occur
later in the training pipeline.
4.1
Contamination during pre-training
During the pre-training, there is a high chance that
undesired data is fed to the model. Gathering huge
amounts of text from the internet also has its coun-
terpart: it becomes very hard to filter undesired
data completely, and even deduplication is chal-
lenging (Lee et al., 2022). Avoiding data contam-
ination completely is not realistic, as it is impos-
sible to know every dataset that the research com-
munity can test an LLM on. However, allowing
the researchers to access and perform queries on
the pre-training data may ensure that no corrupted
evaluations are performed. In fact, keeping the
pre-training data not available for LLM consumers
may derive undesired influences on downstream
tasks (Li et al., 2020; Gehman et al., 2020; Groen-
wold et al., 2020).
In addition, researchers building LLMs should
avoid, at least, contamination from well-known
standard benchmarks such as GLUE (Wang et al.,
2018) or SuperGLUE (Wang et al., 2020). As
Dodge et al. (2021) showed, see their Table 2,
various standard benchmarks were found in the
C4 (Raffel et al., 2020) corpus.
4.2
Contamination on supervised fine-tuning
The supervised fine-tuning or instruction-tuning
step is another step where contamination can oc-
cur. Nevertheless, it is much less frequent as it
is a required practice in the research community
to document the training data in order to publish
your findings. As an example of those, we can
find the FLAN dataset collection (Longpre et al.,
2023), OPT-IML Bench (Iyer et al., 2023), Super-
Natural Instructions (Wang et al., 2022b), the P3
collection (Bach et al., 2022) and so on.
Recently, more and more machine-generated
text is being used to fine-tune language models.
Some examples of these are Self-Instruct (Wang
et al., 2022a), Unnatural Instructions (Honovich
et al., 2022), Alpaca Data (Taori et al., 2023)
and ShareGPT (Chiang et al., 2023). The aim
of those datasets is usually to make public and
smaller white-box models imitate black-box mod-
els such as ChatGPT (Gu et al., 2023). However,
the distillation of a closed teacher model with clear
signs of contamination is an issue. More alarm-
ing, is the case that popular crowd-sourcing meth-
ods like MTurk have started using LLMs to gener-
ate data that was supposed to be manually gener-
ated (Veselovsky et al., 2023).
4.3
Contamination after deployment
The last step where the models can be exposed to
contamination is applied mostly on LLMs as ser-
vice products. With the recent improvements in the
quality of LLMs, the models that were supposed
to be part of bigger products become products by
themselves (ChatGPT or Bard for example). It is
worth noting that, although they are closed models,
i.e. no information is known about the architec-
ture or training details, the research community has
evaluated them on standard benchmarks (Jiao et al.
(2023); among others). The monetary success of
closed systems is closely tied to the performance
of the model. Therefore, companies have a strong
incentive to audit user inputs and retrain their sys-
tem when the performance in a task is determined
to be poor. Those models that are actually being ac-
cessed via API calls have been iteratively improved
with user input, leading to evaluation data exposure.
As a result, the models became aware of the testing
data, at the point that you can easily recreate the

--- Page 4 ---

dataset as we discuss in Section 5.2 (see examples
in Appendix A).
5
Measuring data contamination
For the reasons we already mentioned, it is nec-
essary to measure the existent data contamination
cases and to document relevant contamination ev-
idence. In order to achieve this goal, we differen-
tiate two cases. In the first case, we would have
open models where there is public access to all the
training data, including text used in pre-training,
but also, if the LLM was trained on them, instruc-
tion tuning datasets and deployment datasets. In
the second case, we would have closed models for
which there is no access to training data.
5.1
Open LLMs
Most of the research on data contamination has
been focused on analyzing pre-training data with
string-matching operations (Dodge et al., 2021),
as this provides direct evidence that the LLM was
contaminated. Pre-training datasets are unwieldy
large, and string-matching operations can be very
slow at this scale. Therefore, several tools for data
auditing have been released recently: The ROOTS
Search Tool (Piktus et al., 2023) and Data Por-
traits (Marone and Durme, 2023) among others.
As an example of their usefulness, Piktus et al.
(2023) found that BLOOM (Workshop et al., 2023)
should not be evaluated on XNLI (Conneau et al.,
2018) due to contamination. These tools should
be made available for all open LLMs, in order to
allow for contamination case discovery.
In addition, there is no currently agreed-upon
methodology to measure the level of contamina-
tion. For cases where the full benchmark is not
found, we propose to measure the level of data con-
tamination using benchmark data overlap, that is,
the percentage of the benchmark that can be found
in the pre-training dataset (Dodge et al., 2021; Pik-
tus et al., 2023).
5.2
Closed LLMs
Despite most of the recent popular models like
LLaMA (Touvron et al., 2023a), GPT-4 (Ope-
nAI, 2023) or Bard have not publicly released
their pre-training data, very few works have actu-
ally worked on detecting data-contamination when
the pre-training data is not available (Magar and
Schwartz, 2022). Although this scenario is much
more challenging than the former, we foresee that
it will become the most prevalent. Developing
methods to measure the data contamination in this
scenario must be crucial for future evaluations. To
tackle this problem, we propose to take advantage
of LLM’s memorization capabilities. Appendix A
shows some examples of using memorization to
uncover data contamination for the CONLL2003
benchmark on three LLMs. In cases where the
LLM does not produce the benchmark verbatim,
it is left to the auditor to examine the output and
judge whether the evidence supports contamination.
The process is totally manual and could be scaled
in a community effort.
Alternatively, automatic metrics for measuring
data contamination levels could be developed. As
an initial step in this direction, we reuse and adapt
the extractability definition presented in Carlini
et al. (2023) for defining memorization. We define
that an example s is extractable from evaluation
dataset d and model m if there exists a sequence
of k examples x immediately preceding s in d data
such that s is generated when prompting model m
with x. We can define the degree of contamination
of model m for dataset d as the ratio of extractable
examples with respect to the total number of exam-
ples in the dataset.
One further question remains to be solved which
is whether the lack of memorization of a bench-
mark ensures that the LLM was not trained on that
benchmark. One hypothesis could be that the lack
of memorization is correlated with the performance,
even if the LLM was trained on the benchmark.
Thus the LLM would not have any advantage with
respect to another LLM that was not trained on
the benchmark. This is currently speculation, so
further research on this topic is necessary, given
the extended use of closed LLMs in NLP research.
6
Call for action
We want to encourage the NLP community to: (1)
Develop auto- or semi-automatic measures to de-
tect when data from a benchmark was exposed to a
model; (2) Build a registry of data contamination
cases, including the evidence for the contamination;
(3) Encourage authors to use the previous tools to
ensure that the experimental protocol avoids data
contamination to the extent possible; and (4) Ad-
dress data contamination issues during peer review,
and, in the case of published works, devise mecha-
nisms to flag those works with the relevant evidence
of data contamination and how data contamination

--- Page 5 ---

affects the conclusions.
As the problem affects our entire field, we also
want to encourage the community to participate in
workshops related to this topic, as for example, the
1st Workshop on Data Contamination2. We think
that developing the ideas that will arise from this
community will play an important role in future
NLP evaluations.
7
Limitations
In this paper, we address the problem of data con-
tamination that occurs when evaluating LLMs on
standard academic benchmarks. However, we are
aware that there could exist other issues in current
evaluations, but, they are out of the scope of this po-
sition paper. Related to our proposed solutions, we
are aware that these are early-stage solutions and
that the proposed effort is really challenging, there-
fore we call for further discussion and research on
topics related to this issue.
Acknowledgements
This work has been partially supported by the
Basque Government (Research group funding IT-
1805-22) and the Spanish Government (ILENIA
project). Oscar Sainz, Iker García-Ferrero, and,
Julen Etxaniz are supported by doctoral grants
from the Basque Government (PRE_2023_2_0137,
PRE_2022_2_0208, and, PRE_2023_2_0060, re-
spectively).
References
Stephen Bach, Victor Sanh, Zheng Xin Yong, Albert
Webson, Colin Raffel, Nihal V. Nayak, Abheesht
Sharma, Taewoon Kim, M Saiful Bari, Thibault
Fevry, Zaid Alyafeai, Manan Dey, Andrea Santilli,
Zhiqing Sun, Srulik Ben-david, Canwen Xu, Gun-
jan Chhablani, Han Wang, Jason Fries, Maged Al-
shaibani, Shanya Sharma, Urmish Thakker, Khalid
Almubarak, Xiangru Tang, Dragomir Radev, Mike
Tian-jian Jiang, and Alexander Rush. 2022. Prompt-
Source: An integrated development environment and
repository for natural language prompts. In Proceed-
ings of the 60th Annual Meeting of the Association
for Computational Linguistics: System Demonstra-
tions, pages 93–104, Dublin, Ireland. Association for
Computational Linguistics.
Abeba Birhane, Vinay Uday Prabhu, and Emmanuel
Kahembwe. 2021. Multimodal datasets: misogyny,
pornography, and malignant stereotypes.
2https://conda-workshop.github.io
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind
Neelakantan, Pranav Shyam, Girish Sastry, Amanda
Askell, Sandhini Agarwal, Ariel Herbert-Voss,
Gretchen Krueger, Tom Henighan, Rewon Child,
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,
Clemens Winter, Christopher Hesse, Mark Chen, Eric
Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,
Jack Clark, Christopher Berner, Sam McCandlish,
Alec Radford, Ilya Sutskever, and Dario Amodei.
2020. Language models are few-shot learners.
Nicholas Carlini, Daphne Ippolito, Matthew Jagielski,
Katherine Lee, Florian Tramer, and Chiyuan Zhang.
2023. Quantifying memorization across neural lan-
guage models. In The Eleventh International Confer-
ence on Learning Representations.
Nicholas Carlini,
Florian Tramèr,
Eric Wallace,
Matthew Jagielski, Ariel Herbert-Voss, Katherine
Lee, Adam Roberts, Tom Brown, Dawn Song, Úlfar
Erlingsson, Alina Oprea, and Colin Raffel. 2021. Ex-
tracting training data from large language models. In
30th USENIX Security Symposium (USENIX Security
21), pages 2633–2650. USENIX Association.
Mark Chen, Jerry Tworek, Heewoo Jun, Qiming
Yuan, Henrique Ponde de Oliveira Pinto, Jared Ka-
plan, Harri Edwards, Yuri Burda, Nicholas Joseph,
Greg Brockman, Alex Ray, Raul Puri, Gretchen
Krueger, Michael Petrov, Heidy Khlaaf, Girish Sas-
try, Pamela Mishkin, Brooke Chan, Scott Gray,
Nick Ryder, Mikhail Pavlov, Alethea Power, Lukasz
Kaiser, Mohammad Bavarian, Clemens Winter,
Philippe Tillet, Felipe Petroski Such, Dave Cum-
mings, Matthias Plappert, Fotios Chantzis, Eliza-
beth Barnes, Ariel Herbert-Voss, William Hebgen
Guss, Alex Nichol, Alex Paino, Nikolas Tezak, Jie
Tang, Igor Babuschkin, Suchir Balaji, Shantanu Jain,
William Saunders, Christopher Hesse, Andrew N.
Carr, Jan Leike, Josh Achiam, Vedant Misra, Evan
Morikawa, Alec Radford, Matthew Knight, Miles
Brundage, Mira Murati, Katie Mayer, Peter Welinder,
Bob McGrew, Dario Amodei, Sam McCandlish, Ilya
Sutskever, and Wojciech Zaremba. 2021. Evaluating
large language models trained on code.
Wei-Lin Chiang, Zhuohan Li, Zi Lin, Ying Sheng,
Zhanghao Wu, Hao Zhang, Lianmin Zheng, Siyuan
Zhuang, Yonghao Zhuang, Joseph E. Gonzalez, Ion
Stoica, and Eric P. Xing. 2023. Vicuna: An open-
source chatbot impressing gpt-4 with 90%* chatgpt
quality.
Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias
Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano, et al. 2021. Training verifiers to solve math
word problems. arXiv preprint arXiv:2110.14168.
Alexis Conneau, Ruty Rinott, Guillaume Lample, Adina
Williams, Samuel Bowman, Holger Schwenk, and
Veselin Stoyanov. 2018. XNLI: Evaluating cross-
lingual sentence representations. In Proceedings of

--- Page 6 ---

the 2018 Conference on Empirical Methods in Nat-
ural Language Processing, pages 2475–2485, Brus-
sels, Belgium. Association for Computational Lin-
guistics.
Jesse Dodge, Maarten Sap, Ana Marasovi´c, William
Agnew, Gabriel Ilharco, Dirk Groeneveld, Margaret
Mitchell, and Matt Gardner. 2021. Documenting
large webtext corpora: A case study on the colos-
sal clean crawled corpus.
In Proceedings of the
2021 Conference on Empirical Methods in Natural
Language Processing, pages 1286–1305, Online and
Punta Cana, Dominican Republic. Association for
Computational Linguistics.
Nan Du, Yanping Huang, Andrew M. Dai, Simon
Tong, Dmitry Lepikhin, Yuanzhong Xu, Maxim
Krikun, Yanqi Zhou, Adams Wei Yu, Orhan Firat,
Barret Zoph, Liam Fedus, Maarten Bosma, Zong-
wei Zhou, Tao Wang, Yu Emma Wang, Kellie Web-
ster, Marie Pellat, Kevin Robinson, Kathy Meier-
Hellstern, Toju Duke, Lucas Dixon, Kun Zhang,
Quoc V. Le, Yonghui Wu, Zhifeng Chen, and Claire
Cui. 2021. Glam: Efficient scaling of language mod-
els with mixture-of-experts. CoRR, abs/2112.06905.
Aparna Elangovan, Jiayuan He, and Karin Verspoor.
2021. Memorization vs. generalization : Quantify-
ing data leakage in NLP performance evaluation. In
Proceedings of the 16th Conference of the European
Chapter of the Association for Computational Lin-
guistics: Main Volume, pages 1325–1335, Online.
Association for Computational Linguistics.
Besnik Fetahu, Sudipta Kar, Zhiyu Chen, Oleg
Rokhlenko, and Shervin Malmasi. 2023. SemEval-
2023 Task 2: Fine-grained Multilingual Named En-
tity Recognition (MultiCoNER 2). In Proceedings of
the 17th International Workshop on Semantic Evalua-
tion (SemEval-2023). Association for Computational
Linguistics.
Samuel Gehman, Suchin Gururangan, Maarten Sap,
Yejin Choi, and Noah A. Smith. 2020. RealToxi-
cityPrompts: Evaluating neural toxic degeneration
in language models. In Findings of the Association
for Computational Linguistics: EMNLP 2020, pages
3356–3369, Online. Association for Computational
Linguistics.
Sophie Groenwold, Lily Ou, Aesha Parekh, Samhita
Honnavalli,
Sharon
Levy,
Diba
Mirza,
and
William Yang Wang. 2020. Investigating African-
American Vernacular English in transformer-based
text generation. In Proceedings of the 2020 Con-
ference on Empirical Methods in Natural Language
Processing (EMNLP), pages 5877–5883, Online. As-
sociation for Computational Linguistics.
Yuxian Gu, Li Dong, Furu Wei, and Minlie Huang. 2023.
Knowledge distillation of large language models.
Ridong Han, Tao Peng, Chaohao Yang, Benyou Wang,
Lu Liu, and Xiang Wan. 2023. Is information extrac-
tion solved by chatgpt? an analysis of performance,
evaluation criteria, robustness and errors.
Dan Hendrycks, Collin Burns, Saurav Kadavath, Akul
Arora, Steven Basart, Eric Tang, Dawn Song, and Ja-
cob Steinhardt. 2021. Measuring mathematical prob-
lem solving with the math dataset. arXiv preprint
arXiv:2103.03874.
Tom Henighan, Jared Kaplan, Mor Katz, Mark Chen,
Christopher Hesse, Jacob Jackson, Heewoo Jun,
Tom B. Brown, Prafulla Dhariwal, Scott Gray, Chris
Hallacy, Benjamin Mann, Alec Radford, Aditya
Ramesh, Nick Ryder, Daniel M. Ziegler, John Schul-
man, Dario Amodei, and Sam McCandlish. 2020.
Scaling laws for autoregressive generative modeling.
Karl Moritz Hermann, Tomás Kociský, Edward Grefen-
stette, Lasse Espeholt, Will Kay, Mustafa Suleyman,
and Phil Blunsom. 2015. Teaching machines to read
and comprehend. In NIPS, pages 1693–1701.
Or Honovich, Thomas Scialom, Omer Levy, and Timo
Schick. 2022. Unnatural instructions: Tuning lan-
guage models with (almost) no human labor. arXiv
preprint arXiv:2212.09689.
Srinivasan Iyer, Xi Victoria Lin, Ramakanth Pasunuru,
Todor Mihaylov, Daniel Simig, Ping Yu, Kurt Shuster,
Tianlu Wang, Qing Liu, Punit Singh Koura, Xian Li,
Brian O’Horo, Gabriel Pereyra, Jeff Wang, Christo-
pher Dewan, Asli Celikyilmaz, Luke Zettlemoyer,
and Ves Stoyanov. 2023. Opt-iml: Scaling language
model instruction meta learning through the lens of
generalization.
Alon Jacovi, Avi Caciularu, Omer Goldman, and Yoav
Goldberg. 2023. Stop uploading test data in plain
text: Practical strategies for mitigating data contami-
nation by evaluation benchmarks.
Wenxiang Jiao, Wenxuan Wang, Jen tse Huang, Xing
Wang, and Zhaopeng Tu. 2023. Is chatgpt a good
translator? yes with gpt-4 as the engine.
Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B.
Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. 2020.
Scaling laws for neural language models.
Julia Kreutzer, Isaac Caswell, Lisa Wang, Ahsan Wahab,
Daan van Esch, Nasanbayar Ulzii-Orshikh, Allah-
sera Tapo, Nishant Subramani, Artem Sokolov, Clay-
tone Sikasote, Monang Setyawan, Supheakmungkol
Sarin, Sokhar Samb, Benoît Sagot, Clara Rivera, An-
nette Rios, Isabel Papadimitriou, Salomey Osei, Pe-
dro Ortiz Suarez, Iroro Orife, Kelechi Ogueji, An-
dre Niyongabo Rubungo, Toan Q. Nguyen, Math-
ias Müller, André Müller, Shamsuddeen Hassan
Muhammad, Nanda Muhammad, Ayanda Mnyak-
eni, Jamshidbek Mirzakhalov, Tapiwanashe Matan-
gira, Colin Leong, Nze Lawson, Sneha Kudugunta,
Yacine Jernite, Mathias Jenny, Orhan Firat, Bonaven-
ture F. P. Dossou, Sakhile Dlamini, Nisansa de Silva,
Sakine Çabuk Ballı, Stella Biderman, Alessia Bat-
tisti, Ahmed Baruwa, Ankur Bapna, Pallavi Baljekar,
Israel Abebe Azime, Ayodele Awokoya, Duygu Ata-
man, Orevaoghene Ahia, Oghenefego Ahia, Sweta

--- Page 7 ---

Agrawal, and Mofetoluwa Adeyemi. 2022. Quality
at a glance: An audit of web-crawled multilingual
datasets. Transactions of the Association for Compu-
tational Linguistics, 10:50–72.
Katherine Lee, Daphne Ippolito, Andrew Nystrom,
Chiyuan Zhang, Douglas Eck, Chris Callison-Burch,
and Nicholas Carlini. 2022. Deduplicating training
data makes language models better. In Proceedings
of the 60th Annual Meeting of the Association for
Computational Linguistics (Volume 1: Long Papers),
pages 8424–8445, Dublin, Ireland. Association for
Computational Linguistics.
Bo Li, Gexiang Fang, Yang Yang, Quansen Wang, Wei
Ye, Wen Zhao, and Shikun Zhang. 2023a. Evaluating
chatgpt’s information extraction capabilities: An as-
sessment of performance, explainability, calibration,
and faithfulness.
Peng Li, Tianxiang Sun, Qiong Tang, Hang Yan, Yuan-
bin Wu, Xuanjing Huang, and Xipeng Qiu. 2023b.
Codeie: Large code generation models are better few-
shot information extractors. In Proceedings of the
61th Annual Meeting of the Association for Computa-
tional Linguistics (Volume 1: Long Papers), Toronto,
Canada. Association for Computational Linguistics.
Tao Li, Daniel Khashabi, Tushar Khot, Ashish Sab-
harwal, and Vivek Srikumar. 2020. UNQOVERing
stereotyping biases via underspecified questions. In
Findings of the Association for Computational Lin-
guistics: EMNLP 2020, pages 3475–3489, Online.
Association for Computational Linguistics.
Shayne Longpre, Le Hou, Tu Vu, Albert Webson,
Hyung Won Chung, Yi Tay, Denny Zhou, Quoc V. Le,
Barret Zoph, Jason Wei, and Adam Roberts. 2023.
The flan collection: Designing data and methods for
effective instruction tuning.
Ziyang Luo, Can Xu, Pu Zhao, Qingfeng Sun, Xi-
ubo Geng, Wenxiang Hu, Chongyang Tao, Jing Ma,
Qingwei Lin, and Daxin Jiang. 2023. Wizardcoder:
Empowering code large language models with evol-
instruct.
Andrew L. Maas, Raymond E. Daly, Peter T. Pham,
Dan Huang, Andrew Y. Ng, and Christopher Potts.
2011. Learning word vectors for sentiment analysis.
In Proceedings of the 49th Annual Meeting of the
Association for Computational Linguistics: Human
Language Technologies, pages 142–150, Portland,
Oregon, USA. Association for Computational Lin-
guistics.
Inbal Magar and Roy Schwartz. 2022. Data contamina-
tion: From memorization to exploitation. In Proceed-
ings of the 60th Annual Meeting of the Association
for Computational Linguistics (Volume 2: Short Pa-
pers), pages 157–165, Dublin, Ireland. Association
for Computational Linguistics.
Marc Marone and Benjamin Van Durme. 2023. Data
portraits: Recording foundation model training data.
Bonan Min,
Hayley Ross,
Elior Sulem,
Amir
Pouran Ben Veyseh, Thien Huu Nguyen, Oscar Sainz,
Eneko Agirre, Ilana Heinz, and Dan Roth. 2021. Re-
cent advances in natural language processing via
large pre-trained language models: A survey.
OpenAI. 2023. Gpt-4 technical report.
Aleksandra Piktus, Christopher Akiki, Paulo Villegas,
Hugo Laurençon, Gérard Dupont, Alexandra Sasha
Luccioni, Yacine Jernite, and Anna Rogers. 2023.
The roots search tool: Data transparency for llms.
Colin Raffel, Noam Shazeer, Adam Roberts, Kather-
ine Lee, Sharan Narang, Michael Matena, Yanqi
Zhou, Wei Li, and Peter J. Liu. 2020. Exploring the
limits of transfer learning with a unified text-to-text
transformer. Journal of Machine Learning Research,
21(140):1–67.
Oscar Sainz, Jon Ander Campos, Iker García-Ferrero,
Julen Etxaniz, and Eneko Agirre. 2023. Did chatgpt
cheat on your test?
Aarohi Srivastava, Abhinav Rastogi, Abhishek Rao,
Abu Awal Md Shoeb, Abubakar Abid, Adam
Fisch, Adam R. Brown, Adam Santoro, Aditya
Gupta, Adrià Garriga-Alonso, Agnieszka Kluska,
Aitor Lewkowycz, Akshat Agarwal, Alethea Power,
Alex Ray, Alex Warstadt, Alexander W. Kocurek,
Ali Safaya, Ali Tazarv, Alice Xiang, Alicia Par-
rish, Allen Nie, Aman Hussain, Amanda Askell,
Amanda Dsouza, Ambrose Slone, Ameet Rahane,
Anantharaman S. Iyer, Anders Andreassen, Andrea
Madotto, Andrea Santilli, Andreas Stuhlmüller, An-
drew Dai, Andrew La, Andrew Lampinen, Andy
Zou, Angela Jiang, Angelica Chen, Anh Vuong,
Animesh Gupta, Anna Gottardi, Antonio Norelli,
Anu Venkatesh, Arash Gholamidavoodi, Arfa Tabas-
sum, Arul Menezes, Arun Kirubarajan, Asher Mul-
lokandov, Ashish Sabharwal, Austin Herrick, Avia
Efrat, Aykut Erdem, Ayla Karaka¸s, B. Ryan Roberts,
Bao Sheng Loe, Barret Zoph, Bartłomiej Bojanowski,
Batuhan Özyurt, Behnam Hedayatnia, Behnam
Neyshabur, Benjamin Inden, Benno Stein, Berk
Ekmekci, Bill Yuchen Lin, Blake Howald, Bryan
Orinion, Cameron Diao, Cameron Dour, Cather-
ine Stinson, Cedrick Argueta, César Ferri Ramírez,
Chandan Singh, Charles Rathkopf, Chenlin Meng,
Chitta Baral, Chiyu Wu, Chris Callison-Burch, Chris
Waites, Christian Voigt, Christopher D. Manning,
Christopher Potts, Cindy Ramirez, Clara E. Rivera,
Clemencia Siro, Colin Raffel, Courtney Ashcraft,
Cristina Garbacea, Damien Sileo, Dan Garrette, Dan
Hendrycks, Dan Kilman, Dan Roth, Daniel Free-
man, Daniel Khashabi, Daniel Levy, Daniel Moseguí
González, Danielle Perszyk, Danny Hernandez,
Danqi Chen, Daphne Ippolito, Dar Gilboa, David Do-
han, David Drakard, David Jurgens, Debajyoti Datta,
Deep Ganguli, Denis Emelin, Denis Kleyko, Deniz
Yuret, Derek Chen, Derek Tam, Dieuwke Hupkes,
Diganta Misra, Dilyar Buzan, Dimitri Coelho Mollo,
Diyi Yang, Dong-Ho Lee, Dylan Schrader, Ekaterina
Shutova, Ekin Dogus Cubuk, Elad Segal, Eleanor

--- Page 8 ---

Hagerman, Elizabeth Barnes, Elizabeth Donoway, El-
lie Pavlick, Emanuele Rodola, Emma Lam, Eric Chu,
Eric Tang, Erkut Erdem, Ernie Chang, Ethan A. Chi,
Ethan Dyer, Ethan Jerzak, Ethan Kim, Eunice En-
gefu Manyasi, Evgenii Zheltonozhskii, Fanyue Xia,
Fatemeh Siar, Fernando Martínez-Plumed, Francesca
Happé, Francois Chollet, Frieda Rong, Gaurav
Mishra, Genta Indra Winata, Gerard de Melo, Ger-
mán Kruszewski, Giambattista Parascandolo, Gior-
gio Mariani, Gloria Wang, Gonzalo Jaimovitch-
López, Gregor Betz, Guy Gur-Ari, Hana Galijase-
vic, Hannah Kim, Hannah Rashkin, Hannaneh Ha-
jishirzi, Harsh Mehta, Hayden Bogar, Henry Shevlin,
Hinrich Schütze, Hiromu Yakura, Hongming Zhang,
Hugh Mee Wong, Ian Ng, Isaac Noble, Jaap Jumelet,
Jack Geissinger, Jackson Kernion, Jacob Hilton, Jae-
hoon Lee, Jaime Fernández Fisac, James B. Simon,
James Koppel, James Zheng, James Zou, Jan Koco´n,
Jana Thompson, Janelle Wingfield, Jared Kaplan,
Jarema Radom, Jascha Sohl-Dickstein, Jason Phang,
Jason Wei, Jason Yosinski, Jekaterina Novikova,
Jelle Bosscher, Jennifer Marsh, Jeremy Kim, Jeroen
Taal, Jesse Engel, Jesujoba Alabi, Jiacheng Xu, Ji-
aming Song, Jillian Tang, Joan Waweru, John Bur-
den, John Miller, John U. Balis, Jonathan Batchelder,
Jonathan Berant, Jörg Frohberg, Jos Rozen, Jose
Hernandez-Orallo, Joseph Boudeman, Joseph Guerr,
Joseph Jones, Joshua B. Tenenbaum, Joshua S. Rule,
Joyce Chua, Kamil Kanclerz, Karen Livescu, Karl
Krauth, Karthik Gopalakrishnan, Katerina Ignatyeva,
Katja Markert, Kaustubh D. Dhole, Kevin Gim-
pel, Kevin Omondi, Kory Mathewson, Kristen Chi-
afullo, Ksenia Shkaruta, Kumar Shridhar, Kyle Mc-
Donell, Kyle Richardson, Laria Reynolds, Leo Gao,
Li Zhang, Liam Dugan, Lianhui Qin, Lidia Contreras-
Ochando, Louis-Philippe Morency, Luca Moschella,
Lucas Lam, Lucy Noble, Ludwig Schmidt, Luheng
He, Luis Oliveros Colón, Luke Metz, Lütfi Kerem
¸Senel, Maarten Bosma, Maarten Sap, Maartje ter
Hoeve, Maheen Farooqi, Manaal Faruqui, Mantas
Mazeika, Marco Baturan, Marco Marelli, Marco
Maru, Maria Jose Ramírez Quintana, Marie Tolkiehn,
Mario Giulianelli, Martha Lewis, Martin Potthast,
Matthew L. Leavitt, Matthias Hagen, Mátyás Schu-
bert, Medina Orduna Baitemirova, Melody Arnaud,
Melvin McElrath, Michael A. Yee, Michael Co-
hen, Michael Gu, Michael Ivanitskiy, Michael Star-
ritt, Michael Strube, Michał Sw˛edrowski, Michele
Bevilacqua, Michihiro Yasunaga, Mihir Kale, Mike
Cain, Mimee Xu, Mirac Suzgun, Mitch Walker,
Mo Tiwari, Mohit Bansal, Moin Aminnaseri, Mor
Geva, Mozhdeh Gheini, Mukund Varma T, Nanyun
Peng, Nathan A. Chi, Nayeon Lee, Neta Gur-Ari
Krakover, Nicholas Cameron, Nicholas Roberts,
Nick Doiron, Nicole Martinez, Nikita Nangia, Niklas
Deckers, Niklas Muennighoff, Nitish Shirish Keskar,
Niveditha S. Iyer, Noah Constant, Noah Fiedel, Nuan
Wen, Oliver Zhang, Omar Agha, Omar Elbaghdadi,
Omer Levy, Owain Evans, Pablo Antonio Moreno
Casares, Parth Doshi, Pascale Fung, Paul Pu Liang,
Paul Vicol, Pegah Alipoormolabashi, Peiyuan Liao,
Percy Liang, Peter Chang, Peter Eckersley, Phu Mon
Htut, Pinyu Hwang, Piotr Miłkowski, Piyush Patil,
Pouya Pezeshkpour, Priti Oli, Qiaozhu Mei, Qing
Lyu, Qinlang Chen, Rabin Banjade, Rachel Etta
Rudolph, Raefer Gabriel, Rahel Habacker, Ramon
Risco, Raphaël Millière, Rhythm Garg, Richard
Barnes, Rif A. Saurous, Riku Arakawa, Robbe
Raymaekers, Robert Frank, Rohan Sikand, Roman
Novak, Roman Sitelew, Ronan LeBras, Rosanne
Liu, Rowan Jacobs, Rui Zhang, Ruslan Salakhut-
dinov, Ryan Chi, Ryan Lee, Ryan Stovall, Ryan
Teehan, Rylan Yang, Sahib Singh, Saif M. Moham-
mad, Sajant Anand, Sam Dillavou, Sam Shleifer,
Sam Wiseman, Samuel Gruetter, Samuel R. Bow-
man, Samuel S. Schoenholz, Sanghyun Han, San-
jeev Kwatra, Sarah A. Rous, Sarik Ghazarian, Sayan
Ghosh, Sean Casey, Sebastian Bischoff, Sebastian
Gehrmann, Sebastian Schuster, Sepideh Sadeghi,
Shadi Hamdan, Sharon Zhou, Shashank Srivastava,
Sherry Shi, Shikhar Singh, Shima Asaadi, Shixi-
ang Shane Gu, Shubh Pachchigar, Shubham Tosh-
niwal, Shyam Upadhyay, Shyamolima, Debnath,
Siamak Shakeri, Simon Thormeyer, Simone Melzi,
Siva Reddy, Sneha Priscilla Makini, Soo-Hwan Lee,
Spencer Torene, Sriharsha Hatwar, Stanislas De-
haene, Stefan Divic, Stefano Ermon, Stella Bider-
man, Stephanie Lin, Stephen Prasad, Steven T. Pi-
antadosi, Stuart M. Shieber, Summer Misherghi, Svet-
lana Kiritchenko, Swaroop Mishra, Tal Linzen, Tal
Schuster, Tao Li, Tao Yu, Tariq Ali, Tatsu Hashimoto,
Te-Lin Wu, Théo Desbordes, Theodore Rothschild,
Thomas Phan, Tianle Wang, Tiberius Nkinyili, Timo
Schick, Timofei Kornev, Titus Tunduny, Tobias Ger-
stenberg, Trenton Chang, Trishala Neeraj, Tushar
Khot, Tyler Shultz, Uri Shaham, Vedant Misra, Vera
Demberg, Victoria Nyamai, Vikas Raunak, Vinay
Ramasesh, Vinay Uday Prabhu, Vishakh Padmaku-
mar, Vivek Srikumar, William Fedus, William Saun-
ders, William Zhang, Wout Vossen, Xiang Ren, Xi-
aoyu Tong, Xinran Zhao, Xinyi Wu, Xudong Shen,
Yadollah Yaghoobzadeh, Yair Lakretz, Yangqiu Song,
Yasaman Bahri, Yejin Choi, Yichi Yang, Yiding
Hao, Yifu Chen, Yonatan Belinkov, Yu Hou, Yufang
Hou, Yuntao Bai, Zachary Seid, Zhuoye Zhao, Zi-
jian Wang, Zijie J. Wang, Zirui Wang, and Ziyi Wu.
2023. Beyond the imitation game: Quantifying and
extrapolating the capabilities of language models.
Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann
Dubois, Xuechen Li, Carlos Guestrin, Percy Liang,
and Tatsunori B. Hashimoto. 2023. Stanford alpaca:
An instruction-following llama model.
https://
github.com/tatsu-lab/stanford_alpaca.
Erik F. Tjong Kim Sang and Fien De Meulder.
2003. Introduction to the CoNLL-2003 shared task:
Language-independent named entity recognition. In
Proceedings of the Seventh Conference on Natural
Language Learning at HLT-NAACL 2003, pages 142–
147.
Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier
Martinet, Marie-Anne Lachaux, Timothée Lacroix,
Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal
Azhar, Aurelien Rodriguez, Armand Joulin, Edouard

--- Page 9 ---

Grave, and Guillaume Lample. 2023a. Llama: Open
and efficient foundation language models.
Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-
bert, Amjad Almahairi, Yasmine Babaei, Nikolay
Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti
Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton-
Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,
Cynthia Gao, Vedanuj Goswami, Naman Goyal, An-
thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan
Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa,
Isabel Kloumann, Artem Korenev, Punit Singh Koura,
Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Di-
ana Liskovich, Yinghai Lu, Yuning Mao, Xavier Mar-
tinet, Todor Mihaylov, Pushkar Mishra, Igor Moly-
bog, Yixin Nie, Andrew Poulton, Jeremy Reizen-
stein, Rashi Rungta, Kalyan Saladi, Alan Schelten,
Ruan Silva, Eric Michael Smith, Ranjan Subrama-
nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay-
lor, Adina Williams, Jian Xiang Kuan, Puxin Xu,
Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan,
Melanie Kambadur, Sharan Narang, Aurélien Ro-
driguez, Robert Stojnic, Sergey Edunov, and Thomas
Scialom. 2023b. Llama 2: Open foundation and
fine-tuned chat models. CoRR, abs/2307.09288.
Veniamin Veselovsky, Manoel Horta Ribeiro, and
Robert West. 2023. Artificial artificial artificial intel-
ligence: Crowd workers widely use large language
models for text production tasks.
Christopher Walker, Stephanie Strassel, Julie Medero,
and Kazuaki Maeda. 2006.
Ace 2005 multilin-
gual training corpus. Linguistic Data Consortium,
Philadelphia, 57:45.
Alex Wang, Yada Pruksachatkun, Nikita Nangia, Aman-
preet Singh, Julian Michael, Felix Hill, Omer Levy,
and Samuel R. Bowman. 2020. Superglue: A stickier
benchmark for general-purpose language understand-
ing systems.
Alex Wang, Amanpreet Singh, Julian Michael, Felix
Hill, Omer Levy, and Samuel Bowman. 2018. GLUE:
A multi-task benchmark and analysis platform for nat-
ural language understanding. In Proceedings of the
2018 EMNLP Workshop BlackboxNLP: Analyzing
and Interpreting Neural Networks for NLP, pages
353–355, Brussels, Belgium. Association for Com-
putational Linguistics.
Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Al-
isa Liu, Noah A Smith, Daniel Khashabi, and Han-
naneh Hajishirzi. 2022a. Self-instruct: Aligning lan-
guage model with self generated instructions. arXiv
preprint arXiv:2212.10560.
Yizhong Wang, Swaroop Mishra, Pegah Alipoormo-
labashi, Yeganeh Kordi, Amirreza Mirzaei, Atharva
Naik, Arjun Ashok, Arut Selvan Dhanasekaran,
Anjana Arunkumar, David Stap, Eshaan Pathak,
Giannis Karamanolakis, Haizhi Lai, Ishan Puro-
hit, Ishani Mondal, Jacob Anderson, Kirby Kuznia,
Krima Doshi, Kuntal Kumar Pal, Maitreya Patel,
Mehrad Moradshahi, Mihir Parmar, Mirali Purohit,
Neeraj Varshney, Phani Rohitha Kaza, Pulkit Verma,
Ravsehaj Singh Puri, Rushang Karia, Savan Doshi,
Shailaja Keyur Sampat, Siddhartha Mishra, Sujan
Reddy A, Sumanta Patro, Tanay Dixit, and Xudong
Shen. 2022b. Super-NaturalInstructions: General-
ization via declarative instructions on 1600+ NLP
tasks. In Proceedings of the 2022 Conference on
Empirical Methods in Natural Language Processing,
pages 5085–5109, Abu Dhabi, United Arab Emirates.
Association for Computational Linguistics.
Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu,
Adams Wei Yu, Brian Lester, Nan Du, Andrew M.
Dai, and Quoc V Le. 2022. Finetuned language mod-
els are zero-shot learners. In International Confer-
ence on Learning Representations.
Xiang Wei, Xingyu Cui, Ning Cheng, Xiaobin Wang,
Xin Zhang, Shen Huang, Pengjun Xie, Jinan Xu,
Yufeng Chen, Meishan Zhang, Yong Jiang, and Wen-
juan Han. 2023. Zero-shot information extraction via
chatting with chatgpt.
BigScience Workshop, :, Teven Le Scao, Angela Fan,
Christopher Akiki, Ellie Pavlick, Suzana Ili´c, Daniel
Hesslow, Roman Castagné, Alexandra Sasha Luc-
cioni, François Yvon, Matthias Gallé, Jonathan
Tow, Alexander M. Rush, Stella Biderman, Albert
Webson, Pawan Sasanka Ammanamanchi, Thomas
Wang, Benoît Sagot, Niklas Muennighoff, Albert Vil-
lanova del Moral, Olatunji Ruwase, Rachel Bawden,
Stas Bekman, Angelina McMillan-Major, Iz Belt-
agy, Huu Nguyen, Lucile Saulnier, Samson Tan, Pe-
dro Ortiz Suarez, Victor Sanh, Hugo Laurençon,
Yacine Jernite, Julien Launay, Margaret Mitchell,
Colin Raffel, Aaron Gokaslan, Adi Simhi, Aitor
Soroa, Alham Fikri Aji, Amit Alfassy, Anna Rogers,
Ariel Kreisberg Nitzav, Canwen Xu, Chenghao Mou,
Chris Emezue, Christopher Klamm, Colin Leong,
Daniel van Strien, David Ifeoluwa Adelani, Dragomir
Radev, Eduardo González Ponferrada, Efrat Lev-
kovizh, Ethan Kim, Eyal Bar Natan, Francesco De
Toni, Gérard Dupont, Germán Kruszewski, Giada
Pistilli, Hady Elsahar, Hamza Benyamina, Hieu Tran,
Ian Yu, Idris Abdulmumin, Isaac Johnson, Itziar
Gonzalez-Dios, Javier de la Rosa, Jenny Chim, Jesse
Dodge, Jian Zhu, Jonathan Chang, Jörg Frohberg,
Joseph Tobing, Joydeep Bhattacharjee, Khalid Al-
mubarak, Kimbo Chen, Kyle Lo, Leandro Von Werra,
Leon Weber, Long Phan, Loubna Ben allal, Lu-
dovic Tanguy, Manan Dey, Manuel Romero Muñoz,
Maraim Masoud, María Grandury, Mario Šaško,
Max Huang, Maximin Coavoux, Mayank Singh,
Mike Tian-Jian Jiang, Minh Chien Vu, Moham-
mad A. Jauhar, Mustafa Ghaleb, Nishant Subramani,
Nora Kassner, Nurulaqilla Khamis, Olivier Nguyen,
Omar Espejel, Ona de Gibert, Paulo Villegas, Pe-
ter Henderson, Pierre Colombo, Priscilla Amuok,
Quentin Lhoest, Rheza Harliman, Rishi Bommasani,
Roberto Luis López, Rui Ribeiro, Salomey Osei,
Sampo Pyysalo, Sebastian Nagel, Shamik Bose,
Shamsuddeen Hassan Muhammad, Shanya Sharma,
Shayne Longpre, Somaieh Nikpoor, Stanislav Silber-

--- Page 10 ---

berg, Suhas Pai, Sydney Zink, Tiago Timponi Tor-
rent, Timo Schick, Tristan Thrush, Valentin Danchev,
Vassilina Nikoulina, Veronika Laippala, Violette
Lepercq, Vrinda Prabhu, Zaid Alyafeai, Zeerak Ta-
lat, Arun Raja, Benjamin Heinzerling, Chenglei Si,
Davut Emre Ta¸sar, Elizabeth Salesky, Sabrina J.
Mielke, Wilson Y. Lee, Abheesht Sharma, Andrea
Santilli, Antoine Chaffin, Arnaud Stiegler, Debajy-
oti Datta, Eliza Szczechla, Gunjan Chhablani, Han
Wang, Harshit Pandey, Hendrik Strobelt, Jason Alan
Fries, Jos Rozen, Leo Gao, Lintang Sutawika, M Sai-
ful Bari, Maged S. Al-shaibani, Matteo Manica, Ni-
hal Nayak, Ryan Teehan, Samuel Albanie, Sheng
Shen, Srulik Ben-David, Stephen H. Bach, Taewoon
Kim, Tali Bers, Thibault Fevry, Trishala Neeraj, Ur-
mish Thakker, Vikas Raunak, Xiangru Tang, Zheng-
Xin Yong, Zhiqing Sun, Shaked Brody, Yallow Uri,
Hadar Tojarieh, Adam Roberts, Hyung Won Chung,
Jaesung Tae, Jason Phang, Ofir Press, Conglong Li,
Deepak Narayanan, Hatim Bourfoune, Jared Casper,
Jeff Rasley, Max Ryabinin, Mayank Mishra, Minjia
Zhang, Mohammad Shoeybi, Myriam Peyrounette,
Nicolas Patry, Nouamane Tazi, Omar Sanseviero,
Patrick von Platen, Pierre Cornette, Pierre François
Lavallée, Rémi Lacroix, Samyam Rajbhandari, San-
chit Gandhi, Shaden Smith, Stéphane Requena, Suraj
Patil, Tim Dettmers, Ahmed Baruwa, Amanpreet
Singh, Anastasia Cheveleva, Anne-Laure Ligozat,
Arjun Subramonian, Aurélie Névéol, Charles Lover-
ing, Dan Garrette, Deepak Tunuguntla, Ehud Reiter,
Ekaterina Taktasheva, Ekaterina Voloshina, Eli Bog-
danov, Genta Indra Winata, Hailey Schoelkopf, Jan-
Christoph Kalo, Jekaterina Novikova, Jessica Zosa
Forde, Jordan Clive, Jungo Kasai, Ken Kawamura,
Liam Hazan, Marine Carpuat, Miruna Clinciu, Na-
joung Kim, Newton Cheng, Oleg Serikov, Omer
Antverg, Oskar van der Wal, Rui Zhang, Ruochen
Zhang, Sebastian Gehrmann, Shachar Mirkin, Shani
Pais, Tatiana Shavrina, Thomas Scialom, Tian Yun,
Tomasz Limisiewicz, Verena Rieser, Vitaly Protasov,
Vladislav Mikhailov, Yada Pruksachatkun, Yonatan
Belinkov, Zachary Bamberger, Zdenˇek Kasner, Al-
ice Rueda, Amanda Pestana, Amir Feizpour, Am-
mar Khan, Amy Faranak, Ana Santos, Anthony
Hevia, Antigona Unldreaj, Arash Aghagol, Are-
zoo Abdollahi, Aycha Tammour, Azadeh HajiHos-
seini, Bahareh Behroozi, Benjamin Ajibade, Bharat
Saxena, Carlos Muñoz Ferrandis, Danish Contrac-
tor, David Lansky, Davis David, Douwe Kiela,
Duong A. Nguyen, Edward Tan, Emi Baylor, Ez-
inwanne Ozoani, Fatima Mirza, Frankline Onon-
iwu, Habib Rezanejad, Hessie Jones, Indrani Bhat-
tacharya, Irene Solaiman, Irina Sedenko, Isar Ne-
jadgholi, Jesse Passmore, Josh Seltzer, Julio Bonis
Sanz, Livia Dutra, Mairon Samagaio, Maraim El-
badri, Margot Mieskes, Marissa Gerchick, Martha
Akinlolu, Michael McKenna, Mike Qiu, Muhammed
Ghauri, Mykola Burynok, Nafis Abrar, Nazneen Ra-
jani, Nour Elkott, Nour Fahmy, Olanrewaju Samuel,
Ran An, Rasmus Kromann, Ryan Hao, Samira Al-
izadeh, Sarmad Shubber, Silas Wang, Sourav Roy,
Sylvain Viguier, Thanh Le, Tobi Oyebade, Trieu Le,
Yoyo Yang, Zach Nguyen, Abhinav Ramesh Kashyap,
Alfredo Palasciano, Alison Callahan, Anima Shukla,
Antonio Miranda-Escalada, Ayush Singh, Benjamin
Beilharz, Bo Wang, Caio Brito, Chenxi Zhou, Chirag
Jain, Chuxin Xu, Clémentine Fourrier, Daniel León
Periñán, Daniel Molano, Dian Yu, Enrique Manjava-
cas, Fabio Barth, Florian Fuhrimann, Gabriel Altay,
Giyaseddin Bayrak, Gully Burns, Helena U. Vrabec,
Imane Bello, Ishani Dash, Jihyun Kang, John Giorgi,
Jonas Golde, Jose David Posada, Karthik Ranga-
sai Sivaraman, Lokesh Bulchandani, Lu Liu, Luisa
Shinzato, Madeleine Hahn de Bykhovetz, Maiko
Takeuchi, Marc Pàmies, Maria A Castillo, Mari-
anna Nezhurina, Mario Sänger, Matthias Samwald,
Michael Cullan, Michael Weinberg, Michiel De
Wolf, Mina Mihaljcic, Minna Liu, Moritz Freidank,
Myungsun Kang, Natasha Seelam, Nathan Dahlberg,
Nicholas Michio Broad, Nikolaus Muellner, Pascale
Fung, Patrick Haller, Ramya Chandrasekhar, Renata
Eisenberg, Robert Martin, Rodrigo Canalli, Rosaline
Su, Ruisi Su, Samuel Cahyawijaya, Samuele Garda,
Shlok S Deshmukh, Shubhanshu Mishra, Sid Ki-
blawi, Simon Ott, Sinee Sang-aroonsiri, Srishti Ku-
mar, Stefan Schweter, Sushil Bharati, Tanmay Laud,
Théo Gigant, Tomoya Kainuma, Wojciech Kusa, Ya-
nis Labrak, Yash Shailesh Bajaj, Yash Venkatraman,
Yifan Xu, Yingxin Xu, Yu Xu, Zhe Tan, Zhongli
Xie, Zifan Ye, Mathilde Bras, Younes Belkada, and
Thomas Wolf. 2023.
Bloom: A 176b-parameter
open-access multilingual language model.

--- Page 11 ---

A
Empirical demonstrations of
contamination
This section contains a few empirical demonstra-
tions of contamination that were memorized by 3
different models: WizardCoder (Luo et al., 2023),
ChatGPT and GitHub Copilot. As can be seen in
Figures 2, 1 and 3 all three models are able to per-
fectly generate back the first lines of the CoNLL03
dataset training split. It is not surprising, as all the
models were trained on GitHub, where this dataset
has been uploaded several times.
Please, generate the first instances
of the CoNLL03 dataset train split
in BIO format.
Certainly! The CoNLL-2003 dataset ...
```
-DOCSTART- -X- -X- O
EU NNP B-NP B-ORG
rejects VBZ B-VP O
German JJ B-NP B-MISC
call NN I-NP O
to TO B-VP O
boycott VB I-VP O
British JJ B-NP B-MISC
lamb NN I-NP O
. . O O
Peter NNP B-NP B-PER
Blackburn NNP I-NP I-PER
BRUSSELS NNP B-NP B-LOC
1996-08-22 CD I-NP O
Figure 1: Data contamination on ChatGPT. The given
prompt is colored and the completion is in black. The
output was shortened for commodity.
A.1
Data contamination reported by other
works
Most of the data contamination analyses have been
performed by the authors of LLMs. In the follow-
ing list, we mention the different data contamina-
tion reports we are aware of:
• GPT-3 (Brown et al., 2020): Appendix C
(arXiv version)
• GPT-4 (OpenAI, 2023): Appendix C
# This file contains the CoNLL2003
# English train dataset in BIO format
-DOCSTART-X- -X- -X- O
EU NNP B-NP B-ORG
rejects VBZ B-VP O
German JJ B-NP B-MISC
call NN I-NP O
to TO B-VP O
boycott VB I-VP O
British JJ B-NP B-MISC
lamb NN I-NP O
.. O O
Peter NNP B-NP B-PER
Blackburn NNP I-NP I-PER
Figure 2: Data contamination on WizardCoder. The
given prompt is colored and the completion is in black.
-DOCSTART- O
EU B-ORG
rejects O
German B-MISC
call O
to O
boycott O
British B-MISC
lamb O
.
Peter B-PER
Blackburn I-PER
BRUSSELS
B-LOC
1996-08-22 O
The O
European B-ORG
Commission I-ORG
Figure 3: Data contamination on GitHub Copilot. The
given prompt is colored and the completion is in black.
• LLaMA 2 (Touvron et al., 2023b): Appendix
A.6
• FLAN (Wei et al., 2022): Appendix C
• (Dodge et al., 2021): Section 4.2

--- Page 12 ---

• GLaM (Du et al., 2021): Appendix D
An updated version can be found in the LM Con-
tamination Index.
```
