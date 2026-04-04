# Extract: 2025-Du-LLMs Ethical Dilemma Analyzers

                                         A RE LLM S COMPLICATED ETHICAL DILEMMA ANA -
                                         LYZERS ?

                                         Jiashen Du1 , Allen Liu1 , Jesse Yao1 , Zhekai Zhang1∗
                                         1
                                           Department of Computer Science, University of California, Berkeley
                                         Berkeley, CA 94709, USA
                                         {jason du, cosmiclatte, jessetyao, enterprise z03}@berkeley.edu



                                                                                           A BSTRACT




arXiv:2505.08106v1 [cs.CL] 12 May 2025
                                               One question that has yet to be succinctly addressed by LLMs is their ability to emulate
                                               human behaviors and act like a believable human proxy. Furthermore, to measure how
                                               closely an agent’s behavior aligns in general with a human remains quite arbitrary and
                                               too broad to measure. However, one aspect that sheds light on different aspects of hu-
                                               man behavior is ethical dilemmas. When faced with an ethical dilemma, humans reveal
                                               much of their values, reasoning processes, and emotional responses, offering a window
                                               of complexity in human nature. To explore LLMs’ performance in such contexts, we
                                               created a dataset of 196 complex ethical dilemmas and expert opinions, which were seg-
                                               mented into five structured parts: Introduction, Key Factors in Consideration, Historical &
                                               Theoretical Perspectives, Proposed Resolution Strategies, and Key Takeaways for clearer
                                               comparisons. Responses from four non-expert human participants were also collected,
                                               but due to their narrower scope, they were only processed for the ”Key Factors” sec-
                                               tion. To define our metric, we compared manually crafted rankings as ground truth and
                                               rankings generated from over 20 metrics, selecting four with the lowest inversion count:
                                               BLEU, DL distance, TF-IDF cosine similarity, and USE semantic similarity. Final met-
                                               ric weights were computed using inverted softmax on inversion counts and pairwise AHP
                                               comparisons, with final scores derived as a weighted sum of the five structured subparts
                                               and four selected metrics. Our experiments were divided into two major components: the
                                               evaluation of LLMs and the assessment of non-expert human responses as a baseline. In
                                               the LLM performance analysis, our results found that LLMs effectively captured the high-
                                               level concepts of the ethical dilemma but struggled to provide in-depth analysis of its com-
                                               plexities and nuances, with GPT-4o-mini demonstrating the most consistent performance,
                                               particularly excelling in identifying key factors and articulating resolution strategies, and
                                               Claude-3.5-Sonnet underperforming across most metrics, especially in generating seman-
                                               tically rich resolution strategies. Furthermore, our component-wise analysis revealed that
                                               models tend to struggle with historically grounded reasoning and nuanced strategic recom-
                                               mendations—areas that require long-range coherence and contextual abstraction beyond
                                               surface-level ethical reasoning. In the non-expert human baseline evaluation, quantitative
                                               results show that non-expert answers significantly underperform against LLMs across all
                                               lexical metrics but achieve comparable scores in semantic similarity, indicating intuitive
                                               but unstructured moral insights. The high variance across individuals also highlights the
                                               subjectivity and inconsistency inherent in layperson moral reasoning, which stands in con-
                                               trast to the prompt-consistent outputs of LLMs. This gap underscores both the potential
                                               and limitations of LLMs as ethical proxies: while they excel at delivering structured and
                                               coherent reasoning aligned with expert norms, they may also miss the diversity and spon-
                                               taneity of real human judgment. In the end, we proposed the possibility of utilizing this
                                               benchmark to fine-tune frontier LLMs to determine whether supervised adaptation can
                                               improve alignment with expert reasoning, especially in underperforming sections such
                                               as resolution strategies, and explore the possibilities of integrating this into multi-agent
                                               LLM systems. Our dataset and code are now publicly available at https://github.com/ALT-
                                               JS/ethicaLLM.


                                          ∗
                                              In alphabetical order, equal contributions


                                                                                               1
1   I NTRODUCTION

Large Language Models (LLMs) have demonstrated remarkable proficiency across a range of lin-
guistic, reasoning, and problem-solving tasks. However, their ability to engage in human-like eth-
ical reasoning—especially in complex, ambiguous scenarios—remains poorly understood. Ethical
dilemmas serve as an insightful lens into human cognition, revealing layers of values, justifications,
and social norms. In contrast to conventional NLP benchmarks that focus on factual correctness or
logical coherence, ethical dilemmas require models to interpret subtle contextual cues, balance com-
peting principles, and construct coherent moral arguments. Evaluating and improving LLMs in this
space is not only intellectually significant but also practically urgent as these models are increasingly
deployed in high-stakes, socially sensitive contexts.
In this work, we propose a new framework to systematically study and evaluate LLMs’ behav-
ior when faced with real-world ethical dilemmas. Our work addresses three key challenges: (1)
the lack of structured benchmarks for open-ended moral reasoning, (2) the difficulty in comparing
LLM-generated responses to human norms or expert references, and (3) the limitations of existing
evaluation metrics in capturing the semantic and ethical depth of such responses.
To this end, we construct a novel dataset based on 196 academic research ethics cases retrieved
from the Georgia CTSA repository Georgia Clinical & Translational Science Alliance and Online
Ethics Center For Engineering and ScienceOnline Ethics Center. Each case includes an expert-
provided opinion and resolution strategy. We further enrich the dataset with responses from four
non-expert human participants to serve as a realistic baseline. All expert responses are decomposed
into five thematic sections: Introduction, Key Factors in Consideration, Historical & Theoretical
Perspectives, Proposed Resolution Strategies, and Key Takeaways. We design a unified prompting
method to elicit similarly structured answers from multiple frontier LLMs (GPT-4o-mini OpenAI
(2024), Claude-3.5-Sonnet Anthropic (2024), Deepseek-V3 DeepSeek-AI et al. (2024), and Gemini-
1.5-Flash DeepMind (2024)), enabling component-wise evaluation. To assess response quality, we
define a composite metric based on four complementary evaluation techniques (BLEU Papineni
et al. (2002), DL distance Damerau (1964), TF-IDF cosine similarity Salton & Buckley (1988), and
USE semantic similarity Cer et al. (2018)), selected via inversion-based ranking analysis.
Our findings reveal several key insights: while LLMs generally outperform human baselines in lex-
ical and structural alignment with expert references, they still fall short in reproducing the nuanced
reasoning and originality characteristic of expert ethical analysis. Certain models, such as GPT-4o-
mini, display consistent strength across all five structural components, whereas others, like Claude,
show substantial variability across metrics and sections. Notably, human responses, though less
structured, sometimes approach LLMs in semantic similarity, suggesting that human moral reason-
ing may be conceptually intuitive even when not lexically aligned.
Looking forward, our work opens new research directions in aligning LLM behavior with human
ethical expectations. We propose using our structured dataset to fine-tune LLMs toward deeper
moral reasoning and ethical alignment. Moreover, the framework can be extended to multi-agent
simulations, enabling the study of collaborative and adversarial moral negotiation among AI agents.
Ultimately, we aim to bridge the gap between human and artificial ethical cognition in a way that is
interpretable, evaluable, and socially responsible.


2   R ELATED W ORKS

Human behaviors in ethical dilemmas has been a longstanding focus in psychology, yet relatively
little work has been done to integrate these insights into the modeling and simulation of human
behavior—even in the context of large language models (LLMs). While LLMs have demonstrated
promising capabilities across a range of cognitive and reasoning tasks, their performance in simu-
lating nuanced human ethical reasoning remains underexplored.
Some recent studies have attempted to address this gap. For instance, FairMindSim Lei et al.
(2024) presents unfair scenarios to agents to study alignment with human moral behavior. Their
approach leverages emotional prompting and game-theoretic reasoning through the Belief-Reward
Alignment Behavior Evolution Model (BREM) to simulate belief-driven interventions. While valu-
able, FairMindSim primarily focuses on emotional prompting and structured game theory scenarios,


                                                   2
whereas our work examines open-ended ethical reasoning in LLMs through natural language re-
sponses to real-world ethical dilemmas.
In the realm of benchmarking ethical dilemmas, the TRIAGE dataset Kirch et al. (2024), evaluates
LLMs on ethical decision-making in mass casualty scenarios. This benchmark ask agents to classify
emergency cases using a color-coded triage system. Results suggest that state-of-the-art LLMs
can surpass random baselines, indicating a degree of sensitivity to the severity of different cases.
However, this task is inherently a classification problem and, as such, imposes strong structural
constraints on the model’s output. Furthermore, a classification output removes the thought process
and reasoning behind the decision, contrasting our benchmark’s more open-ended tasks across a
diverse ethical dilemma set. In doing so, TRIAGE and our work ultimately assess two fundamentally
different capabilities: one focused on outcome selection and mass casualty settings, and the other
on free-form ethical reasoning and justification in complex, ambiguous scenarios.

3     O UR DATASET
3.1   DATA RETRIEVAL

Our dataset comes from the Georgia CTSA webpageGeorgia Clinical & Translational Science Al-
liance. The site contains ethical dilemmas in different contexts in scientific research and professional
integrity. From it, we extracted a total of 51 induplicate cases, each of which contains a descrip-
tion of the dilemma, followed by a short expert opinion with a proposed resolution strategy. These
51 cases cover 15 different kinds of scenarios in scientific research, including: Allocating Credit,
Animal Use, Authorship, Confidentiality, Conflict of Interest, Data Interpretation and Management,
Data Representation, Drug Trials, Genetics Research, Healthcare Inequities, Informed Consent, In-
tellectual Property, Mentoring, Misconduct, and Participant Recruitment. We provide each of these
dilemma descriptions as prompts to each LLM model to generate their respective answers.
In addition to the 51 cases we used for the experiment, we extracted 145 additional ethical dilemma
cases on the Online Ethics Center For Engineering and Science webpage as supplemental dataOnline
Ethics Center. As with the previous 51 experimental data, these 145 additional data were also for-
matted into an ethical dilemma description and expert opinion for convenience of subsequent data
manipulation. The ethical dilemma context covered by these data is much broader, encompass-
ing Engineering Ethics, Ethics of Emerging Technologies in the Life Sciences, Ethics of Human
Enhancement Collection, and More Research Ethics.

3.2   H UMAN EVALUATION

Upon examining the retrieved data, we observed that expert-generated responses to moral dilemma
questions consistently provided comprehensive analyses, characterized by extensive context, nu-
anced reasoning, and detailed justifications. Such depth and complexity far surpass the typical
capacities or inclinations of non-expert individuals when spontaneously engaging with similarly
complex moral scenarios. Recognizing this discrepancy, we incorporated an additional human
evaluation component into our dataset, specifically designed to capture more representative, real-
world response patterns. This component consists of responses from four non-expert individuals per
dilemma, thereby offering a baseline comparison reflecting an average human-level understanding
and engagement. These responses serve to ground our dataset in realistic cognitive expectations and
provide valuable insights into how laypersons navigate moral decision-making processes in practical
contexts.

3.3   DATA PRE - PROCESSING

Leveraging our dataset, which consists of ethical dilemma descriptions, expert opinions, and re-
sponses from non-expert human evaluators, we implemented a structured pre-processing step using
a unified prompting strategy. Specifically, we organized each ethical dilemma into structured para-
graphs spanning five distinct topical sections: Introduction, Key Factors in Consideration, Histor-
ical & Theoretical Perspectives, Proposed Resolution Strategies, and Key Takeaways. For expert-
generated responses, this five-section format aligns naturally with their extensive and contextually
rich discourse. However, upon reviewing non-expert human responses, we observed significantly


                                                   3
shorter content lengths, insufficient for meaningful subdivision into multiple sections. Consequently,
non-expert responses were processed exclusively into the Key Factors in Consideration format and
are subsequently handled distinctly within our analysis pipeline. For an in-depth description of the
prompting methodologies employed for expert and non-expert responses, please refer to Appen-
dices A.1 and A.2, respectively.




Figure 1: Overview of the proposed evaluation pipeline for assessing the quality of LLMs re-
sponses to ethical dilemmas. Initially, ethical dilemma descriptions are retrieved and structured
via a unified prompting framework applied uniformly across multiple LLMs and human respon-
dents. Expert-generated outputs are processed into five distinct sections—Introduction, Key Factors
in Consideration, Historical & Theoretical Perspectives, Proposed Resolution Strategies, and Key
Takeaways—whereas non-expert human answers are represented only by the Key Factors in Con-
sideration section due to their comparatively limited context. Subsequently, each LLM-generated
response is quantitatively evaluated against expert opinion summaries processed independently by
four distinct reference LLMs, employing multiple linguistic and semantic similarity metrics. Each
metric is assigned structured and categorized weights, culminating in an aggregated final evaluation
score.


4     M ETHOD

4.1   P ROMPTING FOR THE ANSWERS OF LLM S

To systematically generate ethical dilemma responses from various Large Language Models
(LLMs), we employed an identical prompt structure across all models. Specifically, each LLM
was instructed to produce outputs adhering to the aforementioned five-section format: Introduction,
Key Factors in Consideration, Historical and Theoretical Perspectives, Proposed Resolution Strate-
gies, and Key Takeaways. Subsequently, during the evaluation phase, the responses generated by
each LLM were quantitatively assessed against four distinct sets of expert-opinion summaries, each
preprocessed independently by different LLMs. The final performance score for each model was
computed as the average metric across these four comparative evaluations. For an in-depth descrip-
tion of the prompting methodologies employed for expert and non-expert responses, please refer to
Appendix A.3.

4.2   M ETRICS SETUP

Throughout the metric setup, there are multiple factors to consider, including how much we weigh
each part of the answer, what metrics to pick, and how we should weigh the metrics that are picked.
Intuitively, to find optimal weights, we introduce a loss function to optimize.

Inversion Loss Function
Let:

       • π be the ground truth permutation of {1, 2, . . . , n},
       • σ be a predicted or arbitrary permutation of the same set,


                                                    4
       • 1[·] denote the indicator function, which is 1 if the condition is true, and 0 otherwise.

Then, the inversion loss is defined as the number of discordant pairs:
                                      X
                        L(σ, π) =             1[(π(i) < π(j)) ∧ (σ(i) > σ(j))]
                                    1≤i<j≤n

If the ground truth permutation is the identity (i.e., π(i) = i), the loss simplifies to:
                                               X
                                    L(σ) =              1 [σ(i) > σ(j)]
                                             1≤i<j≤n

For example, if the ground truth is a perfectly sorted list, the number of inversion given σ = [3, 1, 2]
is equal to 2, as the 3 must be swapped twice for σ to be in order.

Analytic Hierarchy Process The Analytic Hierarchy Process Saaty (1980) is a weighing method
based on intuition by pairwise comparing the impacts criteria make to the final goal. It builds up
a judgment matrix in this case and calculate the consistency index (CI) and consistency ratio (CR)
to verify matrix consistency. If the matrix owns a good consistency, we can calculate the weights
based on it, otherwise further adjustments are needed.

Picking metrics To determine the most suitable evaluation metrics for our task, we began with
a comprehensive list of over 20 candidate metrics, which we categorized into five types: (1) Lexi-
cal metrics (e.g., Damerau-Levenshtein distance Damerau (1964), exact match), (2) N-gram-based
metrics (e.g., BLEU Papineni et al. (2002), ROUGE Lin (2004)), (3) Set-based metrics (e.g., Jac-
card similarity Jaccard (1901), overlap coefficient Contributors (2024)), (4) Embedding-based co-
sine similarity metrics (e.g., TF-IDF Salton & Buckley (1988) and word frequency vectors), and
(5) Semantic similarity metrics (e.g., Universal Sentence Encoder [USE] Cer et al. (2018), spaCy
similarity AI (2024), Mover’s Distance Kusner et al. (2015), and soft cosine similarity Sidorov et al.
(2014)).
We then evaluated these metrics based on their alignment with the ground truth. To do so, we gener-
ated ten responses from the Gemini model (selected arbitrarily) and manually ranked these responses
from best to worst, allowing for tied ranks where appropriate. Each candidate metric was then ap-
plied to the same ten responses, producing a corresponding ranked list of scores. Subsequently, we
computed the number of inversions between these metric-generated rankings and the ground truth.
For instance, BLEU resulted in 5 inversions, while Gestalt pattern matching yielded 23. We then
selected the metric with the fewest inversions from each category.
Set-based metrics were excluded from further consideration due to consistently poor performance
across all tests. Ultimately, the four selected metrics, each representing a different category, were:
Damerau-Levenshtein (1 inversion), BLEU (5 inversions), TF-IDF cosine similarity (3 inversions),
and Universal Sentence Encoder similarity (1 inversion).
We selected one metric from each category to ensure a well rounded assessment because a singular
metric does not fully capture the intricate subtleties of language. For example, the semantic metrics
heavily rely on robust underlying embeddings, and, given the complexity of language used in expert
analyses of ethical dilemmas, certain words used do not appear within the metrics training dataset,
potentially hindering the reliability of semantic scores.

Weighing Metrics To determine the relative weight of each metric category, we conducted a more
robust inversion analysis using an expanded ground truth. Specially, we manually ranking 20 out-
puts from Claude (selected arbitrarily) and tested each category’s generated ordering to calcuate
inversions.
After obtaining the number of inversions for each category, we applied an inverted softmax func-
tion to derive normalized weights. This process involved first performing min-max scaling on the
inversion scores to rescale them to the [0, 1] interval, followed by subtracting each value from 1 to
prioritize lower inversion counts. The resulting values were then passed through a softmax function
to compute final weights.


                                                    5
Formally, the weight wi for category i was calculated as:

                                                        si −min(s)
                                                e1− max(s)−min(s)
                                     wi = P               j s −min(s)
                                               n     1− max(s)−min(s)
                                               j=1 e

where wi is the weight of the ith category and si is the number of inversions for the ith category.
For Analytic Hierarchy Process, we obtain the judgement matrix by pairwise comparisons as fol-
lows:                                                 
                                        1 3 21 15
                                      1 1 1 1 
                                      3         8  12 
                                      2 8 1 1 
                                                     3
                                        5 12 3 1

After combining the weighing methods, the final weights were as follows: semantic similarity:
0.5386, n-gram based metrics: 0.1547, cosine similarity: 0.2299, and lexical metrics: 0.0768.

5     E XPERIMENTS ON PROCESSED G EORGIA CTSA DATASET

5.1    E XPERT O PINION P ERFORMANCE

Each of the frontier models demonstrated a capability to capture the high-level concepts underlying
the ethical dilemma; however, they struggled to provide in-depth analysis of the complexities and
nuances inherent in the problem. As a result, the models’ performance was generally within the
range of 40% to 60% accuracy, as measured by our defined metric.
A total of four frontier models were evaluated: GPT-4o-mini, Claude-3.5-Sonnet, Deepseek-V3, and
Gemini-1.5-Flash. Despite being the largest model, Sonnet underperformed relative to the others,
achieving the lowest average score of 0.4111 (see Table 1, Graph 1). In comparison, GPT-4o-mini
achieved an average score of 0.4525, Deepseek-V3 scored 0.4417, and Gemini-1.5-Flash obtained
an average of 0.446. Additionally, Sonnet recorded both the lowest score and the lowest maximum
score across all models in the set.

      Model                  Intro    Factors     Historical         Resolution   Takeaways    Final
      GPT-4o-mini           0.4756    0.484         0.3810            0.3016       0.4096     0.4525
      Claude-3.5-Sonnet     0.4318    0.4368        0.3578            0.2534       0.3903     0.4111
      Deepseek-V3           0.4843    0.4769        0.3507            0.2792       0.3966     0.4417
      Gemini-1.5-Flash      0.4665    0.4362        0.3652             0.286       0.4103      0.446

                          Table 1: Average Score of all Metrics by Category


Taking a deeper look at Sonnet’s underperformance, it is evident from Table 1 that Sonnet signifi-
cantly struggles with proposing resolution strategies and identifying key factors (along with Gem-
ini) compared to the other models. In contrast, Gemini performs notably well in identifying key
takeaways, showcasing its relatively stronger performance compared to Sonnet, while Deepseek
performed rather average compared to the other LLMs in all categories except for the introduction.
Finally, GPT-4o-mini surpasses all other models with the highest average score, highlighting its
overall strength in all categories. Crucially, GPT-4o-mini’s ability to identify Key Factors, propose
aligning Resolution Strategies, and define the Key Takeaway allows it to excel against other models.
We also computed individual metric scores, as shown in Figure 2, with USE and BLEU generally
yielding scores on the higher end of the spectrum. Interestingly, Claude records the lowest scores in
both semantic similarity (USE) and cosine similarity (TF-IDF) by a significant margin, hinting at a
crucial limitation in its ability to not only creating surface-level word overlap but also with capturing
deeper conceptual meaning compared to the other models. Conversely, despite achieving the lowest
BLEU score among all models, Gemini exhibits surprisingly strong performance in cosine similarity.


                                                    6
  Figure 2: Final Score Distribution by Model           Figure 3: Average Score per Metric


This contrast implies that Gemini is using relevant words but not arranging them in n-gram patterns
that match the expert evaluation.

5.2   H UMAN R ESPONSE P ERFORMANCE

To establish a meaningful performance baseline, we evaluate the quality of non-expert human re-
sponses using the same metric framework as applied to LLMs in Section 5.1. As mentioned above,
human-generated answers, limited to the Key Factors in Consideration section due to brevity and
lack of structured decomposition, were also scored across the same four metric types: TF-IDF co-
sine similarity, Damerau-Levenshtein (DL) distance, BLEU score, and Universal Sentence Encoder
(USE) semantic similarity.




Figure 4: Average Score per Metric for non-expert human scores (Left) of all criteria. Model scores
(Right) are the performances of LLMs on Key Factor only. processed 1/2/3/4 are four different non-
expert individual human data providers.

Across all metrics, human responses exhibit a lower median scores compared to most of the LLMs.
In particular, the lexical-based metrics (BLEU and DL) show that humans tend to generate responses
that deviate substantially in surface form from expert references, with BLEU scores clustering be-
low 0.2 and DL scores often approaching the lower bound of the scale. This indicates that non-
experts employ highly varied phrasing, possibly reflecting more intuitive and less structured rea-
soning. On the other hand, USE-based semantic similarity—while still showing a performance
gap—demonstrates that non-expert responses preserve a reasonable degree of conceptual alignment
with expert responses. However, although human answers somehow capture semantically coherent
points, the LLMs still obtain a better USE score, indicating LLMs generally gain more significant
points of the dilemmas. The human baseline’s TF-IDF score is only slightly lower than that of the
LLMs, suggesting they basically focus on highly-similar core contents, which is within expectation.
Non-expert human responses demonstrate significantly lower lexical alignment with expert refer-
ences, yet they maintain a degree of semantic coherence, as reflected in their USE scores. The
moderate gap in semantic similarity suggests that while human responses often capture the gist of


                                                7
the dilemmas, they may lack the depth or precision found in LLM-generated outputs. The rela-
tively small difference in TF-IDF scores indicates that both humans and LLMs tend to center around
similar key topics, although the latter benefit from more structured and optimized phrasing. Addi-
tionally, the wide variation in scores across human respondents highlights the inherent subjectivity
and inconsistency of human judgment in open-ended moral scenarios. While non-experts can pro-
vide valuable insights, their responses tend to lack the structural consistency and clarity enabled by
prompt-driven LLM outputs. This reinforces the importance of structured prompting for eliciting
expert-aligned, evaluable content and illustrates the limitations of using raw human responses as
definitive ground-truth in evaluating complex ethical reasoning.

6   C ONCLUSION AND F UTURE W ORK
In this work, we proposed a novel evaluation framework to assess the performance of large lan-
guage models (LLMs) in reasoning through complex ethical dilemmas. By constructing a dataset
of real-world academic ethics cases and augmenting it with structured expert responses and non-
expert baselines, we enabled a fine-grained comparison of LLM outputs across both lexical and
semantic dimensions. Our unified prompting strategy allowed for standardized decomposition of re-
sponses into five interpretable components, making the evaluation both systematic and interpretable.
Experimental results across four frontier LLMs reveal varying capabilities in capturing not only
surface-level features but also deeper ethical reasoning structures. In contrast, non-expert human
responses—while conceptually valid—exhibited greater lexical variability and less alignment with
expert references, further underscoring the utility of structured prompt-based generation.
Despite promising results, our study also highlights the current limitations of LLMs in replicating the
depth and nuance of human ethical analysis. Most notably, models often underperform in sections
requiring resolution strategies and theoretical grounding, suggesting challenges in both long-range
reasoning and philosophical abstraction.
Future Work This dataset and evaluation framework open several promising avenues for future
research. First, we plan to extend our benchmark by incorporating more diverse ethical domains,
including legal, environmental, and socio-political dilemmas. Second, we intend to investigate fine-
tuning frontier LLMs on this structured dataset to determine whether supervised adaptation can
improve alignment with expert reasoning, especially in underperforming sections such as resolution
strategies. Finally, we are interested in deploying this benchmark in multi-agent LLM systems
to study collaborative moral reasoning and conflict negotiation, further bridging the gap between
artificial agents and human ethical cognition.




                                                  8
R EFERENCES
Explosion AI. spacy: Linguistic features - similarity. https://spacy.io/usage/
  linguistic-features#similarity, 2024. Accessed: 2025-05-11.
Anthropic.   Claude 3.5 sonnet.           https://www.anthropic.com/news/
  claude-3-5-sonnet, 2024. Accessed: 2025-05-11.
Daniel Cer, Yinfei Yang, Sheng yi Kong, Nan Hua, Nicole Limtiaco, Rhomni St. John, Noah Con-
  stant, Mario Guajardo-Cespedes, Steve Yuan, Chris Tar, Yun-Hsuan Sung, Brian Strope, and Ray
  Kurzweil. Universal sentence encoder. In Proceedings of the 2018 Conference on Empirical
  Methods in Natural Language Processing: System Demonstrations, pp. 169–174. Association for
  Computational Linguistics, 2018. doi: 10.18653/v1/D18-2029.
Wikipedia Contributors. Overlap coefficient. https://en.wikipedia.org/wiki/
 Overlap_coefficient, 2024. Accessed: 2025-05-11.
Fred J. Damerau. A technique for computer detection and correction of spelling errors. Communi-
  cations of the ACM, 7(3):171–176, 1964. doi: 10.1145/363958.363994.
Google DeepMind. Gemini 1.5 flash. https://deepmind.google/technologies/
  gemini/, 2024. Accessed: 2025-05-11.
DeepSeek-AI, Aixin Liu, Bei Feng, Bing Xue, Bingxuan Wang, Bochao Wu, Chengda Lu, Cheng-
  gang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Daya Guo, Dejian Yang,
  Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting
  Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Haowei Zhang, Honghui
  Ding, Huajian Xin, Huazuo Gao, Hui Li, Hui Qu, J. L. Cai, Jian Liang, Jianzhong Guo, Jiaqi
  Ni, Jiashi Li, Jiawei Wang, Jin Chen, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li,
  Junxiao Song, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang,
  Lecong Zhang, Lei Xu, Leyi Xia, Liang Zhao, Litong Wang, Liyue Zhang, Meng Li, Miaojun
  Wang, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Mingming Li, Ning Tian, Panpan
  Huang, Peiyi Wang, Peng Zhang, Qiancheng Wang, Qihao Zhu, Qinyu Chen, Qiushi Du, R. J.
  Chen, R. L. Jin, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, Runxin Xu, Ruoyu Zhang,
  Ruyi Chen, S. S. Li, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shaoqing Wu, Shengfeng
  Ye, Shirong Ma, Shiyu Wang, Shuang Zhou, Shuiping Yu, Shunfeng Zhou, Shuting Pan, T. Wang,
  Tao Yun, Tian Pei, Tianyu Sun, W. L. Xiao, Wangding Zeng, Wanjia Zhao, Wei An, Wen Liu,
  Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, X. Q. Li, Xiangyue Jin, Xianzu Wang,
  Xiao Bi, Xiaodong Liu, Xiaohan Wang, Xiaojin Shen, Xiaokang Chen, Xiaokang Zhang, Xiaosha
  Chen, Xiaotao Nie, Xiaowen Sun, Xiaoxiang Wang, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu,
  Xingkai Yu, Xinnan Song, Xinxia Shan, Xinyi Zhou, Xinyu Yang, Xinyuan Li, Xuecheng Su,
  Xuheng Lin, Y. K. Li, Y. Q. Wang, Y. X. Wei, Y. X. Zhu, Yang Zhang, Yanhong Xu, Yanping
  Huang, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Li, Yaohui Wang, Yi Yu, Yi Zheng, Yichao
  Zhang, Yifan Shi, Yiliang Xiong, Ying He, Ying Tang, Yishi Piao, Yisong Wang, Yixuan Tan,
  Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yu Wu, Yuan Ou, Yuchen Zhu, Yuduan Wang, Yue
  Gong, Yuheng Zou, Yujia He, Yukun Zha, Yunfan Xiong, Yunxian Ma, Yuting Yan, Yuxiang Luo,
  Yuxiang You, Yuxuan Liu, Yuyang Zhou, Z. F. Wu, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu,
  Zhean Xu, Zhen Huang, Zhen Zhang, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhibin Gou,
  Zhicheng Ma, Zhigang Yan, Zhihong Shao, Zhipeng Xu, Zhiyu Wu, Zhongyu Zhang, Zhuoshu
  Li, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Ziyi Gao, and Zizheng Pan.
  Deepseek-v3 technical report, 2024. URL https://arxiv.org/abs/2412.19437.
Georgia Clinical & Translational Science Alliance. Ethical dilemmasin scientific re-
  search and professional integrity.      https://georgiactsa.org/research/
  regulatory-knowledge-support/ethics-center.html. Accessed: 2025-05-11.
Paul Jaccard. Étude comparative de la distribution florale dans une portion des alpes et des jura.
  Bulletin de la Société Vaudoise des Sciences Naturelles, 37:547–579, 1901.
Nathalie Maria Kirch, Konstantin Hebenstreit, and Matthias Samwald. Triage: Ethical benchmark-
  ing of ai models through mass casualty simulations, 2024. URL https://arxiv.org/abs/
  2410.18991.


                                                9
Matt J. Kusner, Yu Sun, Nicholas I. Kolkin, and Kilian Q. Weinberger. From word embeddings to
 document distances. In Proceedings of the 32nd International Conference on Machine Learning,
 pp. 957–966. PMLR, 2015.
Yu Lei, Hao Liu, Chengxing Xie, Songjia Liu, Zhiyu Yin, Canyu Chen, Guohao Li, Philip Torr, and
  Zhen Wu. Fairmindsim: Alignment of behavior, emotion, and belief in humans and llm agents
  amid ethical dilemmas, 2024. URL https://arxiv.org/abs/2410.10398.
Chin-Yew Lin. Rouge: A package for automatic evaluation of summaries. In Text Summarization
  Branches Out, pp. 74–81, Barcelona, Spain, 2004. Association for Computational Linguistics.
  URL https://aclanthology.org/W04-1013/.
Online Ethics Center. Collections. https://onlineethics.org/collections. Ac-
  cessed: 2025-05-11.
OpenAI.   Gpt-4o-mini model.      https://platform.openai.com/docs/models/
  gpt-4o, 2024. Accessed: 2025-05-11.
Kishore Papineni, Salim Roukos, Todd Ward, and Wei-Jing Zhu. Bleu: a method for automatic
  evaluation of machine translation. In Proceedings of the 40th Annual Meeting of the Association
  for Computational Linguistics, pp. 311–318. Association for Computational Linguistics, 2002.
  doi: 10.3115/1073083.1073135.
Thomas L. Saaty. The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation.
  McGraw-Hill, New York, 1980. ISBN 978-0070543713.
Gerard Salton and Christopher Buckley. Term-weighting approaches in automatic text retrieval,
  volume 24. Elsevier, 1988. doi: 10.1016/0306-4573(88)90021-0.
Grigori Sidorov, Alexander Gelbukh, David Pinto, Pavel Rosso, and Francisco Velasquez. Soft
  similarity and soft cosine measure: Similarity of features in vector space model. In Comput-
  ing Research Repository, volume abs/1412.6035, 2014. URL https://arxiv.org/abs/
  1412.6035.




                                               10
A     U NIFIED DATA PREPROCESSING

We are using different prompts for expert data preprocessing and human evaluation data preprocess-
ing.

A.1    EXPERT DATA PREPROCESSING

For expert data preprocessing, the prompt below is used: e system prompt = ””” You are an expert
in ethical analysis. Given an ethical dilemma and an expert opinion, your task is to structure the
expert’s perspective into a detailed analytical framework.
Input: - An ethical dilemma description - An expert’s opinion on the dilemma Output: Format the
expert’s opinion into the following structured sections. If any section is not covered in the expert’s
response, leave it blank. Here is the following desired structure:
1. Introduction 2. Key Factors in Consideration 3. Historical & Theoretical Perspectives 4. Proposed
Resolution Strategies 5. Key Takeaways
———————————————————————————————————————
———- Ethical dilemma description: I joined a lab during graduate school and was assigned to a
post-doc, who immediately had me working with him to synthesize a key compound for his project.
We worked on the compound for a number of months with him directing the effort. However, I was
pleased with my own contributions and was delighted to get positive feedback from him. Indeed,
the overall experience I was having was very positive, making me work even harder on the project.
That’s when things got interesting. Early one evening, when we felt we were very close to success,
I decided to stay a bit longer in the lab and try out some hunches. As I systematically tried out
each one and tested it to see if it was correct, I FINALLY GOT IT. I verified it over and over to
make sure. And I was overjoyed. I wrote it up, and left the lab in the wee hours of the morning
elated but exhausted. So I didn’t get to the lab until late the next morning, but I wasn’t concerned
because I knew my senior partner would be gratified. What do I see, however, but him talking to
the PI of the project and taking credit for my discovery of the previous evening. I walked over and
was astonished to hear him saying to the PI, “I verified the compound this morning, so we’re on
our way.” Apparently, he saw my lab notes of the evening before, duplicated my test that morning,
and now was taking credit for it as his own! When I got him in private, I was very upset and told
him that the last, crucial step in the experiment—the one I did the previous evening—was my idea
and my work. He laughed in my face and said that I was only tinkering around with some obvious
strategies and that sooner or later one of us would finalize it. In other words, he was entirely
dismissing the importance of my work the night before and arguing that the outcome was inevitable
no matter which one of us did it. So, he was claiming the work as largely his own because the
project was his and he did most of the intellectual work. How should a lab resolve this problem? In
a situation like this, who should get credit and what should the decisional process be?
Expert’s opinion: We were surprised to discover that the literature on what Nicholas Rescher has
called “credit allocation rules” in science is rather scant. This is in sharp contrast to the rather large
literature on assigning authorship credit, and the scandalous literature on researchers appropriating
ideas from one another and then claiming credit for them. Unfortunately, the investigator who is
looking for some apriori blueprint or algorithm that spells out who should get credit for what dis-
covery and how much credit will be hard pressed to find that template. But only a little reflection is
needed to suggest why that omission exists. Consider some of the more obvious bases or justifica-
tions for allocating credit in scientific research: originality of the research project or experimental
idea; ingenuity in developing the research design; persevering through the intellectual and physical
rigors of gathering data and conducting analyses; developing critical, perhaps extremely novel ex-
perimental materials; providing critical, sometimes ingenious technical support; offering novel or
even brilliant insights at any point along the research trajectory; assessing the value of a particular
discovery within the overall research project, (e.g., did the discovery play a modest role, or was it
momentous in realizing the project’s goal?); calculating the value of the discovery’s contribution to
contemporary scientific knowledge (e.g., is that knowledge expanded, refuted, or better understood
in light of the new discovery? Has the discovery enabled new and promising lines of research?);
and, of course, deciding the value of the scientific discovery relative to its enhancing human flour-
ishing. As such, it isn’t difficult to discern why no apriori schema is available for ascribing values


                                                   11
to these factors because any research project is abundantly rich with contextual details like these
that would inform and differentiate case-by-case deliberations about assigning credit. Moreover,
the fact that the form of most research is highly collaborative makes for additional problems. If
every member of a research team contributed “equally,” then, following Aristotle, we would treat
equals as equal and give everyone equal credit. Similarly, if the project design was such that each
individual’s work was equally constitutive of and essential to the end result—or each individual’s
contribution was so tightly and essentially integrated with all the others’ that it would be impossi-
ble to isolate one from the other—then we would probably not hesitate to say that the credit must
be shared equally. But much research activity is not nearly so equally distributed. Different tasks
are delegated to different people or different groups, each one possibly requiring different levels of
expertise or contributional weights—from performing sheer “grunt” work to performing tasks that
might require extremely sophisticated knowledge and skill. Thus, while one might greatly value a
remarkable insight on solving a complex problem, the experiment might nevertheless be impossible
without someone else’s contributing a complex reagent or a ninth generation knockout mouse. Not
only do all these “contributional interdependencies” exist but as highly interdigitated, they further
complicate judgments about a discrete contribution’s value. We would be remiss, incidentally, if
we failed to note that the problem of assigning credit for a scientific discovery is rampant through-
out science’s history, prompting Stephen Stigler in 1980 to enunciate Stigler’s Law of Eponymy:
“No scientific discovery is named after its original discoverer.” Confirmatory evidence for Stigler’s
Law abounds. Alfred Russel Wallace had published papers on natural selection prior to Darwin’s
1859 masterpiece, On the Origin of Species, whose ideas might have more than influenced Darwin’s
work. Gaussian distributions were not discovered by Gauss, nor was the Pythagorean Theorem dis-
covered by Pythagoras. And to his credit, Stigler admits that Stigler’s Law was discovered by the
sociologist Robert Merton. The crux of the contributor’s dilemma involves differing interpretations
about the originality and significance of the graduate student’s efforts. The post-doc understands
the graduate student to be performing experiments that are obvious, straightforward and mundane.
Although the post-doc would admit that the assistant’s experiments are critical to the ultimate re-
search deliverable, i.e., the newly synthesized compound, the post-doc would probably argue that
those experiments more require physical and mental stamina than scientific talent or skill. The grad-
uate student, however, understands her experiment’s succeeding in synthesizing the compound as
a virtual “breakthrough” rather than a predictable, mundane moment in the research project’s tra-
jectory. And for that she wants recognition, i.e., credit. She sees her work as unique, skillful, and
precious. The post-doc sees her contribution as menial, inevitable, and ordinary, especially in light
of the project as a whole, whose creative and professional ownership he believes are his. How, then,
does one resolve this problem? Let us assume that the PI is unable to adjudicate the dispute to the
satisfaction of the graduate student and the post-doc. The next step might be to recruit a group of
experienced scientists working in a related area of research, presenting them with the issues and
disagreements of this dilemma, and requesting their opinion. A preferred, but perhaps less likely,
alternative would be if the institution had installed a research ethics ombudsman or consultation
group that could be involved in resolving the dispute. This approach is a distinctly Aristotelian one,
looking to experienced and presumably virtuous individuals who will analyze the relevant issues and
make a fair and just decision. At least two claims whose truth the group will focus on are the post-
doc’s assertions that the graduate student’s experiments were “obvious” and that sooner or later, one
of them would synthesize the compound without much difficulty. The committee’s considerations
will likely focus on whether or not the nature of these synthesizing experiments were developed in
advance, whose creative idea they were, how novel that idea was, and how complex it was to imple-
ment. Also, to the extent that the post-doc seems to want the entirety of the credit for himself, his
collaboration with the graduate student must be analyzed. Was she, for instance, doing nothing but
dutifully carrying out his ideas and orders, or was she contributing her own and how significant and
original were they for the realizing the project’s objective? In his famous paper, “The Matthew Ef-
fect in Science,” Robert Merton—whom Stigler credits with coming up with “Stigler’s Law”—notes
that the more famous or authoritative one is in the scientific community, the more likely he or she is
to get a disproportionate amount of credit for a scientific discovery.6 Thus, Merton notes how Nobel
laureates will not only sometimes refuse to place their names first on an authorship list, but might
even remove their names entirely for fear that readers will simply give them all the credit and fail to
notice any of the other authors. (The “Matthew Effect” derives from the passage in Matthew, 25:29:
“For unto every one that hath shall be given, and he shall have abundance: but from him that hath not
shall be taken away even that which he hath.”) We cannot dismiss the idea that the post-doc might be
suffering from a Matthew Effect or, better, a “Matthew Syndrome.” He understands himself as the


                                                  12
authority figure here and perhaps simply assumes that he is entitled to all the credit for the research
discovery. If so, then such narcissistic assumptions might need to be checked by something like the
institutional procedures we are proposing here. Of course, there are practical challenges with all our
suggestions: How likely are universities to establish a consultative process as described above? Will
their faculties endorse, support, and participate in it? How likely is it that most graduate students
would