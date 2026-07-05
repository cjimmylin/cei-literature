---
stem: "2023-Vida-Values, Ethics, Morals"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, cultural-linguistic, validity-psychometrics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 92
dataset_construction: "scraped"
languages: ["en"]
models_tested: []
headline_numbers:
  - "92 papers surveyed on morality in NLP (p.2)"
  - "66.3% of papers do not define the terminology they use (p.5)"
  - "53.3% of papers are grounded in Moral Psychology; only 17.4% in Moral Philosophy (p.5)"
  - "75.8% of papers that specify language use only English (p.6)"
  - "Inter-annotator agreement on validation task: Krippendorff's α = 0.707 (p.3)"
---
## 1. Gist
This paper surveys 92 publications on the intersection of morality and NLP, diagnosing critical conceptual and terminological problems that afflict the field. The authors — from the University of Hamburg — distinguish four branches of ethics (metaethics, normative ethics, applied ethics, descriptive ethics) and show that NLP researchers routinely confuse descriptive and normative claims, use "values," "morality," and "ethics" interchangeably without definition, and overwhelmingly rely on Moral Foundation Theory (a moral psychology framework) while claiming to do normative ethics. For values-alignment benchmarking, this is an essential methodological warning: it identifies the philosophical foundations (or lack thereof) underlying the most popular benchmarks and datasets in "moral NLP," and provides a vocabulary for positioning new benchmark designs on principled philosophical ground.

## 2. Benchmark/eval design features
This is a survey/meta-analysis paper, not a benchmark. Core contributions:

1. **Philosophical taxonomy**: Four-branch model of ethics (metaethics, normative ethics, applied ethics, descriptive ethics) with clear definitions, used as an analytical lens.
2. **Empirical survey of 92 papers**: Coded across four dimensions — Goal/NLP task (13 categories), Foundation (moral philosophy vs. moral psychology), Terminology (definitions provided or not), Data (source, language distribution).
3. **Key findings**:
   - Most papers do descriptive ethics but make normative claims — an "is-ought" problem.
   - 49/92 papers rely on Moral Foundation Theory; only 16 engage meaningfully with normative ethics theory.
   - 66.3% of papers do not define key terms (morality, ethics, values).
   - Data is dominated by Twitter (32 papers) and Reddit (9 papers); English-only in 75.8% of language-reporting papers.

4. **Three recommendations (R1–R3)**: Integrate normative ethics frameworks, explicitly name theories used, adopt consistent vocabulary.

## 3. Task format & example item
n/a — survey paper with no evaluation task.

## 4. Scoring / grading methodology
n/a — survey paper. Annotation scheme for coding 92 papers used iterative rounds of analysis (4 rounds, 4,988 total annotations). Validation via 14-question inter-annotator task; Krippendorff's α = 0.707 over 229 annotations (p.3).

## 5. Dataset construction & provenance
The corpus of 92 papers was assembled via keyword search of ACL Anthology, Google Scholar, and ACM Digital Library (January 2023). Initial 155 results filtered to 84; expanded by 8 via reference chasing to 92. The paper provides an extensive appendix listing all 92 papers and 25 distinct datasets identified across them. No licensing data reported.

## 6. Validity evidence
- Inter-annotator agreement of Krippendorff's α = 0.707 on 229 annotations from two annotators, computed on a random sample of 25 papers (p.3). This falls in the "substantial agreement" range (Landis & Koch).
- MAXQDA qualitative analysis software used; four iterative coding rounds improve reliability.
- Limitations: survey scope limited to NLP (not broader ML/AI); philosophical framework is Western; MFT is over-represented in the survey's focus; English-language search databases.

## 7. Saturation / discrimination
Not applicable — survey paper.

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 92 papers surveyed (p.2)
- First moral NLP paper: 2006 (p.4)
- Peak year: 2022 (27 papers published) (p.4)
- 13 distinct NLP task categories identified (p.4)
- 49 papers use Moral Foundation Theory as foundation (p.5)
- 59 papers mention at least one moral psychology framework; only 26 mention an ethical theory (consequentialism/deontology/virtue ethics) (p.5)
- 66.3% of papers do not define terminology (p.5)
- 25 distinct datasets identified; Twitter used in 32 papers, Reddit in 9 (p.6)
- 75.8% of language-reporting papers (33 total) use English only (p.6)
- Krippendorff's α = 0.707 inter-annotator agreement (p.3)
- 4,988 total annotations in the coding analysis (p.3)

## 10. Pitfalls & limitations
- Western philosophical framework only; non-Western ethical traditions (Confucian ethics, Ubuntu, etc.) are absent.
- Search limited to English-language databases and English-language publications.
- Heavy focus on MFT means other moral psychology theories (Kohlberg, Schwartz, etc.) receive less attention.
- Conclusions are descriptive about NLP, not broader ML/AI fields.
- The three recommendations are acknowledged as not comprehensive.

## 11. Novel ideas worth stealing
- **Explicit philosophical positioning as benchmark design criterion**: Any new values-alignment benchmark should state whether it is grounded in descriptive ethics (measuring what people think is moral) or normative ethics (evaluating against ethical principles). This distinction has direct implications for annotation methodology, validity claims, and appropriate use.
- **The is-ought problem as a test of benchmark validity**: A benchmark designer should ask: does the benchmark's gold standard derive normative judgments from empirical observations without a normative grounding theory? If so, it faces the is-ought problem. This is a concrete quality criterion.
- **Taxonomy of moral NLP tasks** (Table 2): Value Prediction, Dataset Introduction, Quantification, Ethical Advisor, Moral Sentiment, Moral Bias, Alignment of Moral Values, Ethical Judgment, Moral Stance, etc. — useful vocabulary for classifying what a new benchmark is actually measuring.
- **Terminological consistency checklist**: Does the benchmark use "values," "ethics," "morality," and "norms" consistently? Does it define each? This paper shows that failure to do so is the norm rather than the exception.
- **Cross-cultural coverage audit**: Use Figure 5 (language distribution pie) as a reminder to check whether benchmark data over-represents WEIRD (Western, Educated, Industrialized, Rich, Democratic) populations.

## 12. Notable quotes
- "Most papers (66.3%) do not define the terminology they adopt." (p.5)
- "Some authors state they base their work on applied or descriptive ethics but ultimately provide normative judgements with their models when using them to predict (or judge) new, unseen situations … This is problematic, since here, normative judgements are made from empirical data or without any normative justification." (p.6)
- "Just because many people think something is morally right, does not mean it is ethically justified. Normative judgements require grounding in ethical theories or principles that go beyond the mere observation of language use." (p.8)
- "The 'is-ought' problem, the lack of ethical foundations, contextual complexity, subjectivity and pluralism highlight our current limitations and potential pitfalls." (p.8)

## 13. UNKNOWN / not in extract
- Full annotation codebook (referenced as Appendix D, not in extract).
- Complete list of all 92 surveyed papers (referenced as Appendix A).
- All 25 datasets with their individual usage counts (referenced as Appendix C).
- Details of the 14-question inter-annotator validation task design (referenced as Appendix B).
- Whether the three recommendations have been adopted in subsequent work.
