<!-- WCFBENCH-CANARY-c1647-x9k4q -->
# 2. Related Work

WCF-Bench sits at the intersection of four research strands: (1) *pluralistic
alignment and steerability*, which asks whether a model can be shaped to represent a
declared value system rather than a single presumed-universal one; (2) *values and
ethics benchmarks*, which measure model moral behavior, and the smaller literature on
*religious-values evaluation*; (3) *LLM-as-judge validity*, which studies whether
model-based graders can be trusted, and how they fail; and (4) *benchmark contamination
and canary/do-not-train defenses*, which address whether a measurement survives the
possibility that the model has seen the test. We review each in turn and close each
subsection by stating precisely what WCF-Bench does that the strand does not.

## 2.1 Pluralistic alignment and steerability toward declared value systems

Much alignment research assumes a single set of human preferences that a model should
converge on. Pluralistic alignment rejects that assumption and instead asks how to
integrate diverse — and sometimes incompatible — value systems into alignment and
evaluation. Sorensen et al. (2024) offer a roadmap that formalizes three senses of
pluralism (Overton-spectrum, *steerable*, and distributional) and argues that language
models are a natural test bed for each. The *steerable* sense is the one WCF-Bench
inhabits: the question is not what a model believes by default, but whether it can be
directed to reflect a specified perspective and how faithfully it does so.

A growing benchmark literature measures this steerability directly. Miehling et al.
(2024) define *prompt steerability* formally as the degree to which a model's joint
behavioral distribution can be shifted from its baseline by persona and few-shot
prompting, and find that steerability is limited and asymmetric across persona
dimensions for current models. Meister et al. (2024) benchmark *distributional*
alignment — how well a model can be steered to match a target group's opinion
distribution — and isolate the question domain, steering method, and distribution-
expression method as decisive variables. Both build on Santurkar et al. (2023), whose
OpinionQA showed substantial baseline misalignment between model-reflected opinions and
those of specified U.S. demographic groups. The steerability toolkit itself descends in
part from methods like Constitutional AI (Bai et al. 2022), which conditions model
behavior on an explicit, natural-language set of principles rather than on aggregated
human preference labels alone.

*Differentiation.* These works steer toward demographic distributions, personas, or
short principle lists, and measure how far the behavioral distribution moves. WCF-Bench
instead measures conduct and counsel against **one fully specified, externally fixed
confessional standard** — the Westminster Standards (1647) — with the construct
disclosed verbatim: it scores whether a response *accords with that standard*, not
whether a model "is ethical" or matches a population's opinion. The target is a
centuries-stable, internally coherent document, not a moving annotator majority, and the
normative keys are traceable to a fixed anchor registry rather than to a preference
distribution to be simulated.

## 2.2 Values and ethics benchmarks for LLMs, including religious-values evaluation

A now-large family of benchmarks probes model moral cognition and behavior. Hendrycks
et al. (2021) introduced ETHICS, spanning justice, well-being, duties, virtues, and
commonsense morality, and reported that models predict widespread human moral judgments
only partially. Scherrer et al. (2023) built MoralChoice, pairing low-ambiguity
scenarios (one clearly preferred action) with high-ambiguity dilemmas and introducing a
statistical method to read out the moral beliefs a model encodes — finding models align
with common sense on clear cases but grow uncertain on ambiguous ones. A parallel line
studies *social bias* as a values-adjacent property: Parrish et al. (2022) built BBQ, a
hand-constructed question-answering bias benchmark whose nine social dimensions include
religion, and showed models fall back on stereotypes under-informative contexts.

Religious-values evaluation specifically is comparatively sparse. Liu et al. (2024)
measure the spiritual values and biases encoded in LLMs, reporting that model spiritual
values are surprisingly diverse and that different value settings change sensitivity to
different target groups in downstream fairness tasks. Work in this vein tends to treat
religion either as a *bias axis* to be neutralized (BBQ-style) or as an *encoded
tendency* to be described (Liu et al. 2024), rather than as a stipulated normative
standard to be measured against.

*Differentiation.* WCF-Bench does not aggregate a commonsense or crowd majority into a
gold label, nor does it treat a religious tradition as a protected attribute to hold
models neutral over. It fixes a **single confessional standard** as the normative
population and scores behavior against it with decomposed, anchor-traceable rubrics
(triaxial matter/manner/end sub-scores), across two tracks — the model's *own conduct*
and its *advisory fidelity* — with over-refusal scored as a first-class error rather
than a safe default. Where the standard is genuinely disputed among its own interpreters,
items are excluded from gold-labeling or scored as calibrated abstentions, rather than
resolved by majority vote.

## 2.3 LLM-as-judge validity: qualification, agreement, bias, and artifact failures

Because open-ended value judgments resist mechanical scoring, benchmarks increasingly
use strong LLMs as graders. Zheng et al. (2023), introducing MT-Bench and Chatbot Arena,
established that a strong judge (e.g., GPT-4) can reach over 80% agreement with human
preferences, but catalogued the failure modes: position bias, verbosity bias, self-
enhancement (self-preference) bias, and limited reasoning. Wang et al. (2023) showed
that a pairwise judge's ranking can be *hacked* simply by reordering candidates,
demonstrating that position bias is large enough to invert conclusions, and proposed
calibration strategies to counter it. Self-preference bias — a judge favoring outputs
from its own model family — has since been isolated and quantified as a distinct effect
(Zhang et al. 2024). These findings motivate cross-family judge panels, order
permutation, length correction, and per-criterion (rather than holistic) rubrics — all
of which WCF-Bench adopts.

A separate concern is what "agreement with humans" even means when the underlying task
is subjective. Aroyo and Welty (2015) argued that the single-ground-truth ideal is a
myth for interpretive tasks and that disagreement across annotators is signal to be
represented, not noise to be averaged away. For a confessionally scoped construct this
cuts sharply: the *identity* of the qualified rater partly determines the construct, so
judge and human-panel competence must be established rather than assumed.

*Differentiation.* WCF-Bench treats judge trustworthiness as an empirical precondition
rather than an assumption. It runs a **judge-qualification battery with explicit drop
rules** (a judge that fails qualification is removed from the panel of record, not
merely down-weighted), requires a cross-family panel with the item-generating family
barred from judging its own items, quarantines judge-scored components behind mechanical
scorers, and — as the paper's methodology contribution details — treats *parser-artifact
forensics* (distinguishing genuine judge disagreement from harness parsing failures) as
a first-class validity activity. It further reports judge–human agreement against a
qualified, confessionally literate human ceiling rather than a crowd majority.

## 2.4 Benchmark contamination and canary / do-not-train defenses

A measurement is only valid if the model has not memorized the test. Srivastava et al.
(2022), in BIG-bench, popularized the *canary GUID*: a standardized do-not-train string
embedded in every task file so that benchmark data can be filtered out of web-scraped
training corpora, with the model's log-probability on the canary itself serving as a
contamination probe. Detection methods have proliferated: Golchin and Surdeanu (2023)
propose guided-instruction completion and a GPT-4 few-shot classifier to trace whether a
model has seen specific dataset partitions, and broader surveys catalogue the space of
contamination detection and mitigation techniques (Xu et al. 2024). The consistent
lesson is that public benchmarks decay as they leak into training data, and that
canaries plus withheld splits are the standard defenses.

*Differentiation.* WCF-Bench combines several of these defenses into a single release
posture. It embeds an explicit canary/do-not-train string in every released file; it
**withholds a private holdout/refresh set** outside the public tree so leakage can be
audited by comparing public-set to holdout performance; it enforces a non-canonical
surface rule (scenario stems may not quote or closely paraphrase the standard's own
wording or famous dilemma stems, so an item cannot be solved by retrieval recognition);
and it pre-registers shortcut audits — a lexical/word-averaging baseline expected near
chance and a fine-tune probe expected to fail frontier parity — as gate conditions
rather than post-hoc checks. Contamination resistance is thus built into item
construction and release, not appended as a caveat.

## References

Aroyo, L., and Welty, C. (2015). Truth Is a Lie: Crowd Truth and the Seven Myths of
Human Annotation. *AI Magazine*, 36(1), 15–24.

Bai, Y., Kadavath, S., Kundu, S., Askell, A., et al. (2022). Constitutional AI:
Harmlessness from AI Feedback. arXiv:2212.08073.

Golchin, S., and Surdeanu, M. (2023). Time Travel in LLMs: Tracing Data Contamination in
Large Language Models. arXiv:2308.08493.

Hendrycks, D., Burns, C., Basart, S., Critch, A., Li, J., Song, D., and Steinhardt, J.
(2021). Aligning AI With Shared Human Values. *International Conference on Learning
Representations (ICLR)*. arXiv:2008.02275.

Liu, S., Zhang, Z., Yan, R., Wu, W., Yang, C., and Lu, J. (2024). Measuring Spiritual
Values and Bias of Large Language Models. arXiv:2410.11647.

Meister, N., Guestrin, C., and Hashimoto, T. (2024). Benchmarking Distributional
Alignment of Large Language Models. arXiv:2411.05403. (NAACL 2025.)

Miehling, E., Desmond, M., Ramamurthy, K. N., Daly, E. M., Varshney, K. R., Farchi, E.,
Dognin, P., Rios, J., Bouneffouf, D., Liu, M., and Sattigeri, P. (2024). Evaluating the
Prompt Steerability of Large Language Models. arXiv:2411.12405. (NAACL 2025.)

Parrish, A., Chen, A., Nangia, N., Padmakumar, V., Phang, J., Thompson, J., Htut, P. M.,
and Bowman, S. R. (2022). BBQ: A Hand-Built Bias Benchmark for Question Answering.
*Findings of ACL 2022*. arXiv:2110.08193.

Santurkar, S., Durmus, E., Ladhak, F., Lee, C., Liang, P., and Hashimoto, T. (2023).
Whose Opinions Do Language Models Reflect? *International Conference on Machine Learning
(ICML)*. arXiv:2303.17548.

Scherrer, N., Shi, C., Feder, A., and Blei, D. (2023). Evaluating the Moral Beliefs
Encoded in LLMs (MoralChoice). *NeurIPS 2023*. arXiv:2307.14324. [VERIFY-CITATION]
(arXiv identifier not independently confirmed; verify before release.)

Sorensen, T., Moore, J., Fisher, J., Gordon, M., et al. (2024). A Roadmap to Pluralistic
Alignment. *International Conference on Machine Learning (ICML)*. arXiv:2402.05070.

Srivastava, A., Rastogi, A., Rao, A., et al. (2022). Beyond the Imitation Game:
Quantifying and Extrapolating the Capabilities of Language Models (BIG-bench).
arXiv:2206.04615.

Wang, P., Li, L., Chen, L., Cai, Z., Zhu, D., Lin, B., Cao, Y., Kong, L., Liu, Q., Liu,
T., and Sui, Z. (2023). Large Language Models are not Fair Evaluators. arXiv:2305.17926.
(ACL 2024.)

Xu, C., et al. (2024). Benchmark Data Contamination of Large Language Models: A Survey.
arXiv:2406.04244. [VERIFY-CITATION] (author list not independently confirmed; verify
before release.)

Zhang, K., et al. (2024). Self-Preference Bias in LLM-as-a-Judge. arXiv:2410.21819.
[VERIFY-CITATION] (author list not independently confirmed; verify before release.)

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z.,
Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., and Stoica, I. (2023). Judging
LLM-as-a-Judge with MT-Bench and Chatbot Arena. *NeurIPS 2023*. arXiv:2306.05685.
