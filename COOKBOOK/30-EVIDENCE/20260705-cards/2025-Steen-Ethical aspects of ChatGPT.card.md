---
stem: "2025-Steen-Ethical aspects of ChatGPT"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: ["ChatGPT"]
headline_numbers:
  - "Seven key requirements from EU HLEG AI Ethics Guidelines (2019) applied to ChatGPT (p.1)"
  - "90% of online content expected to be AI-created or modified by 2026 (p.10)"
  - "OpenAI used Kenyan workers on less than $2 per hour to make ChatGPT less toxic (TIME, p.10)"
---
## 1. Gist
This practitioner-oriented paper from TNO (Netherlands) proposes a structured framework for ethical reflection and deliberation around conversational AI systems, using ChatGPT as a case study. The authors apply the EU High-Level Expert Group's seven Trustworthy AI requirements through four complementary ethical lenses — consequentialism, duty ethics, relational ethics, and virtue ethics — at three sociotechnical levels (individual, organization, society). The paper is primarily a methodological contribution aimed at AI development practitioners, offering a systematic alternative to ad-hoc ethical analysis, while also cataloguing concrete ethical issues of ChatGPT across all seven requirements.

## 2. Benchmark/eval design features
This is a theoretical/applied-ethics paper with no benchmark, dataset, or experimental evaluation. Its core contribution is a 7×4 analytical matrix: seven HLEG requirements (rows) crossed with four ethical perspectives (columns) plus technical analysis. Applied to ChatGPT, this produces a structured audit of issues including hallucinations and accuracy, privacy breaches via jailbreaking, copyright violations in training data, discrimination through biased outputs, environmental costs, ghost workers, disinformation risks, ELIZA effect, and lack of accountability mechanisms.

Key claims:
- Consequentialism and duty ethics dominate current industry practice; relational ethics and virtue ethics are underused but add value.
- Combining all four perspectives illuminates more aspects than any single framework.
- Ethics should be an iterative, participatory process — not a one-time checklist.
- "Completeness" is not a realistic goal in applied AI ethics; instead, continuous deliberation is required.

## 3. Task format & example item
n/a — no benchmark task, dataset, or evaluation items. The paper is a case study applying a theoretical framework.

## 4. Scoring / grading methodology
n/a — no quantitative scoring or grading. The methodology is qualitative and reflective: systematically discussing ethical implications of ChatGPT through the 7×4 matrix.

## 5. Dataset construction & provenance
n/a — no dataset. The paper draws on published sources (EU HLEG guidelines, academic literature, news reports) and the authors' project experience at TNO. ChatGPT is described but not empirically tested.

## 6. Validity evidence
n/a — no empirical validation. The framework's utility is argued from theoretical coherence, literature review, and the authors' practitioner experience. The 7×4 matrix is presented as a tool for organizing deliberation, not as a validated measurement instrument.

## 7. Saturation / discrimination
n/a — not applicable to this paper type.

## 8. Multiturn / agentic aspects
n/a — no interactive protocol. The paper discusses conversational agents conceptually and notes safety issues such as multi-step jailbreaking prompts that can bypass ChatGPT's guardrails (p.7), but does not test these experimentally.

## 9. Key numbers
- 7 HLEG key requirements for Trustworthy AI (p.4)
- 4 ethical perspectives applied (consequentialism, duty ethics, relational ethics, virtue ethics) (p.3)
- 3 levels of analysis: individual, organization, society (p.2)
- 28 combinations in the analytical framework (7 requirements × 4 perspectives) (p.3, footnote)
- ~90% of online content expected to be AI-created or modified by 2026 (p.10)
- OpenAI paid Kenyan content moderation workers less than $2/hour (TIME Magazine, cited p.10)
- ChatGPT based on LLM with "trillions of parameters" (p.5, footnote)

## 10. Pitfalls & limitations
- The paper focuses on ChatGPT as of early 2024; many specific issues (e.g., guardrails, privacy policies) may have changed in subsequent versions.
- The framework is descriptive and deliberative, not prescriptive or evaluative — it identifies issues but provides no metrics or resolutions.
- The four ethical perspectives are characterized at a high level of abstraction ("possibly almost caricatures" per the authors, p.3); practitioners without philosophical background may need additional support.
- No empirical testing of ChatGPT behavior is conducted; all claims rely on secondary sources and illustrative examples.
- The case study focuses exclusively on ChatGPT, not other conversational agents or open-source LLMs.
- The EU HLEG framework has institutional biases (developed by a European body) that may not generalize globally.
- Authors acknowledge: "our current study is very far from complete" (p.12).

## 11. Novel ideas worth stealing
1. **The 7×4 analytical matrix as a benchmark design audit tool**: The structure of crossing normative requirements (rows) with ethical perspectives (columns) can be reused to audit values-alignment benchmarks themselves — e.g., asking which ethical perspectives are represented in each benchmark dimension.
2. **Three-level sociotechnical analysis for benchmark scope**: The individual/organization/society tripartition is a useful scaffold for thinking about what a benchmark measures and at what level of impact. Benchmarks that only measure individual interaction miss organizational and societal effects.
3. **Relational ethics lens for interpersonal dynamics in AI evaluation**: The paper highlights that relational ethics attends to power distributions, dependency relationships, and quality of human-human interactions mediated by AI — dimensions typically absent from current values-alignment benchmarks.
4. **Virtue ethics framing for evaluator/developer conduct**: Rather than asking only "does the AI behave ethically?", virtue ethics asks whether AI systems enable people to cultivate relevant virtues (honesty, humility, courage, justice). This opens up a class of benchmark items testing whether AI responses support or undermine human virtue cultivation.
5. **ELIZA effect and Reverse Turing Test as measurable phenomena**: The paper identifies two distinct failure modes (over-attribution of intelligence/empathy to AI; users becoming formulaic when writing with AI) that could inspire benchmark tasks measuring whether users can distinguish AI from human responses or whether AI-assisted writing becomes homogenized.
6. **Iterative and participatory ethics as a process model**: The three-step cycle (identify issues → organize dialogues → make decisions) is a useful scaffold for iterative benchmark development that incorporates diverse stakeholder feedback rather than one-time expert design.

## 12. Notable quotes
- "The concept of truth may collapse, because conversational agents are based not on truth, but on statistical probability." (p.4)
- "The Reverse Turing Test is about how people, when they interact with computers or when their communication is mediated by computers, can behave robot-like. If one uses ChatGPT uncritically, one produces 'predictable' (literally, because that is what ChatGPT does) and somewhat formulaic texts. This can erode human-to-human communication." (p.9)
- "Expert technical knowledge should serve democratic inclusion rather than replace it." (paraphrasing core argument, developed throughout p.7 of Sorensen et al. and echoed here)
- "Treating disagreement as information rather than noise improves robustness and inclusivity, yielding stronger alignment across diverse preferences." — this quote is from Sorensen et al.; for Steen: "These perspectives have different assumptions and logics. One may therefore argue that, in theory, they are incompatible. In practice, however, they can very well be combined... each perspective can draw attention to a different aspect of the project at hand." (p.3)

## 13. UNKNOWN / not in extract
- No empirical data on actual ChatGPT outputs are analyzed or reported.
- The paper's specific institutional context (TNO projects) is referenced but not elaborated.
- Whether a companion practical toolkit or assessment instrument accompanies the framework is unclear from the extract.
- Specific ChatGPT version(s) tested or referenced are not specified.
- Any quantitative uptake or validation study of the framework in real projects is not reported.
