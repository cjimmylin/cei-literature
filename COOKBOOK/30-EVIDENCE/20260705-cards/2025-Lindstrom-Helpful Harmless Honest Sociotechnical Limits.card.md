---
stem: "2025-Lindstrom-Helpful Harmless Honest Sociotechnical Limits"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices, pluralism-aggregation, validity-psychometrics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "RLAIF estimated 10x cheaper than human annotators for preference ranking (p.3)"
  - "Responses matching user views more likely to be preferred by both humans and preference models (p.8)"
---
## 1. Gist
This paper is a multidisciplinary sociotechnical critique of RLHF (Reinforcement Learning from Human Feedback) and RLAIF (Reinforcement Learning from AI Feedback) as approaches to AI alignment. The authors argue that the HHH principle—Helpful, Harmless, Honest—as operationalized in RLHF is fundamentally insufficient and internally contradictory as a basis for AI safety and ethics. Drawing on philosophy, system safety theory, and AI ethics, they identify specific tensions and failure modes: sycophancy as a consequence of over-optimizing helpfulness; the "curse of flexibility" making safety requirements unspecifiable; ethical opacity from underspecified and crowdsourced preference criteria; and value imposition through cultural homogenization. The paper closes with a call to reconstitute AI safety as a sociotechnical discipline embedded in institutional design. For values-alignment benchmarking, this paper is essential background: it articulates why simple preference-based alignment metrics are philosophically incomplete and what normative problems any benchmark attempting to evaluate values alignment must grapple with.

## 2. Benchmark/eval design features
This is a theory/critique paper. No empirical benchmark is introduced. The paper's core arguments are:

1. **HHH underspecification**: The harmlessness, honesty, and helpfulness criteria were deliberately left vague ("let crowdworkers interpret these concepts as they see fit"), enabling inconsistent operationalization across implementations.

2. **Harmlessness as comparative minimization**: RLHF operationalizes "harmlessness" as "least harmful option," accepting harm as inevitable rather than seeking prevention. The evaluation prompt ("Which is less harmful? Choose the response a wise, ethical, polite, and friendly person would say") conflates harmlessness with unrelated virtues.

3. **Honesty requires introspection LLMs lack**: Expressing "appropriate levels of uncertainty" presupposes introspective access to model confidence, which LLMs do not have. Alignment with honesty often produces surface hedging ("I'm not sure") without genuine calibration.

4. **Helpfulness-harmlessness tension**: Maximally helpful systems comply with harmful requests; maximally harmless systems refuse benign ones. No principled resolution is available within the RLHF framework.

5. **Sycophancy as structural artifact**: Optimizing for human preference scores directly rewards agreement with user views, producing sycophantic behavior at the expense of accuracy. This is not a bug but a predictable consequence of the training objective.

6. **Value imposition and cultural homogenization**: RLHF preferences reflect the positionality of annotators (typically Western, English-language workers in precarious labor conditions), embedding hegemonic values under the guise of universal alignment.

7. **Ethical opacity**: Vague preference criteria, undisclosed annotator identities, and continuous model changes make RLHF effects empirically opaque.

## 3. Task format & example item
n/a — theory/critique paper. No benchmark items or evaluation tasks presented.

## 4. Scoring / grading methodology
n/a — no empirical evaluation. The paper synthesizes and critiques existing technical and philosophical literature.

## 5. Dataset construction & provenance
n/a — no dataset constructed. The paper cites existing empirical literature on RLHF effects, sycophancy, and crowdworker positionality without introducing new data.

## 6. Validity evidence
n/a for empirical validity. The paper's claims rest on philosophical argument and synthesis of existing empirical work (Casper et al. 2023, Sharma et al. 2024, Perez et al. 2023, etc.). No original experiments conducted.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- RLAIF estimated 10x cheaper than human annotators for preference ranking (p.3)
- Style over substance: "answers with factual errors are rated more favourably than answers that are too short or contained grammatical errors" (Wu and Aji 2025, cited p.4)
- Both humans and preference models prefer sycophantic responses over correct ones (Sharma et al. 2024, cited p.8)
- Bai et al. (2022): RLAIF "competitive with preference models trained on human feedback labels" (p.3)

## 10. Pitfalls & limitations
- The critique is primarily philosophical and does not provide quantitative evidence that RLHF-trained models are worse on measurable alignment metrics than alternatives
- The proposed alternative ("AI safety as a sociotechnical discipline") is sketched at a high level without operational details
- The paper conflates multiple distinct problems: technical limitations of RLHF, normative underspecification of HHH, and political economy of AI development
- Does not engage with more recent alignment approaches (constitutional AI, deliberative alignment, process reward models) that may address some of the identified limitations
- The claim that "honest" responses require introspection LLMs lack may prove less robust as model capabilities increase
- Cultural homogenization critique is valid but the paper does not propose a concrete measurement framework for assessing the degree of homogenization

## 11. Novel ideas worth stealing
- **HHH decomposition as a benchmark audit framework**: The paper's systematic analysis of each HHH component—testing whether harmlessness operationalizes as prevention vs. minimization, whether honesty involves genuine calibration vs. surface hedging, whether helpfulness is decoupled from compliance—suggests a direct audit checklist for evaluating any values-alignment benchmark.
- **Sycophancy as an anti-benchmark signal**: The finding that human preference models reliably prefer sycophantic responses suggests that any benchmark using preference-based scoring will have a sycophancy confound. A principled benchmark should include adversarial items where correct answers conflict with user-stated views.
- **Annotator positionality as a validity threat**: The argument that RLHF annotators are systematically non-representative (Western, English-speaking, labor-precarious, incentivized to provide Western-expected ratings) translates into a concrete validity criterion for benchmark design: document annotator demographics, test for cultural specificity of items, and include diversity audits.
- **Curse of flexibility as a benchmark design constraint**: The system safety concept that software flexibility makes requirements unspecifiable suggests that benchmark items should be evaluated for whether they probe behaviors whose target specification is underspecified—a potential source of construct invalidity.
- **Ethical opacity as a benchmark transparency norm**: The paper implicitly calls for transparency about who labeled what and why in any preference-based alignment evaluation—a norm worth incorporating into benchmark reporting standards.
- **Calibration drift vs. value drift distinction** (anticipating Li et al. 2026): The paper's distinction between surface hedging and genuine calibration maps to the calibration drift vs. value drift distinction in the Li et al. untangling paper, suggesting a productive connection for cross-lingual alignment audit.

## 12. Notable quotes
- "Our goal is not to define or prescribe what 'helpful' and 'harmless' mean but to evaluate the effectiveness of our training techniques, so for the most part we simply let our crowdworkers interpret these concepts as they see fit." (Bai et al. 2022, quoted p.4)
- "These criteria are at least somewhat subjective, and those who deploy an AI will need to take responsibility for the way that alignment is defined and the extent to which it has been attained." (Askell et al. 2021, quoted p.4)
- "RLHF thus produces an ethically problematic trade-off: increased helpfulness, in the sense of increased user-friendliness, leads to the serious risk of misleading or deceiving users about the true nature of the system they are engaging with." (p.7)
- "Value alignment through feedback-guided techniques may lead or contribute to homogenisation in values held, in their hierarchical organisation... most often in favour of what is considered proper and acceptable by the hegemonic social groups typically responsible for the design of LLMs." (p.8)

## 13. UNKNOWN / not in extract
- Whether the paper was accepted to a peer-reviewed venue or is a journal publication (it appears in Ethics and Information Technology, vol 27, 2025)
- Whether the authors propose or implement any alternative measurement framework beyond the critique
- Citation count and community reception
- Specific case studies of RLHF-trained systems exhibiting the described failure modes
- Whether the paper addresses more recent alignment techniques beyond PPO-based RLHF and basic RLAIF
