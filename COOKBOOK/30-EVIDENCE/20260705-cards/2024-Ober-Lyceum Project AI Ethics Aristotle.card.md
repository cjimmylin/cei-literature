---
stem: "2024-Ober-Lyceum Project AI Ethics Aristotle"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, ai-lab-practices, moral-psychology]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This 69-page white paper by Stanford political scientist Josiah Ober and legal philosopher John Tasioulas (from Oxford/King's College) argues that Aristotelian virtue ethics provides the most compelling normative framework for addressing the challenges of contemporary AI. Published by the Lyceum Project in June 2024, the paper is divided into three parts: (I) the Aristotelian framework of human nature, ethics, and political community; (II) a vision of AI systems as "intelligent tools" for human flourishing rather than AGI competitors; and (III) regulatory sign-posts derived from the framework. Its significance for values-alignment benchmarking lies in articulating a rich, multi-dimensional account of human values that explicitly rejects both preference-utilitarian and rights-only frameworks — the very frameworks implicitly operative in most current RLHF and benchmark designs. The paper provides a philosophical vocabulary for thinking about what alignment should even mean.

## 2. Benchmark/eval design features
Not a benchmark paper. Core theoretical claims relevant to values-alignment work:

1. **Human nature as the anchor for ethics**: Aristotle grounds ethics in the fact that humans are rational, communicative, and social animals. An alignment framework that ignores this risks optimising for preference satisfaction (utilitarian) or rule-compliance (rights-based) rather than genuine flourishing.

2. **Rejection of preference-utilitarianism as the foundation for values**: The paper mounts a sustained critique of Benthamite utilitarianism as "hollowed out" — preferences can be ill-informed, manipulated, or oppressive; aggregate welfare maximization sacrifices individuals; moral quantities are not commensurable on a single scale.

3. **Practical reason (phronesis) is uncodifiable**: Algorithmic rule-following cannot substitute for the context-sensitive judgment that ethics requires. This is a direct challenge to benchmark paradigms that reduce moral competence to pattern matching.

4. **Value pluralism without relativism**: Ethics pursues objective truths, but often there is a "bounded range of equally acceptable answers" rather than a single optimum. This frames pluralism as a feature, not a defect, of moral reasoning.

5. **AI as "intelligent tool," not moral agent**: Current and foreseeable AI systems lack the human nature that grounds virtue; they can simulate virtuous behaviour but cannot genuinely possess virtues. Anthropomorphising AI as a moral peer is a category error with dangerous consequences (the "natural slaves" analogy from Aristotle's Politics is developed as a cautionary tale).

6. **Regulatory implications**: Safety-only frameworks are too narrow; the Aristotelian framework demands attention to human flourishing across domains of work, democratic participation, and global governance.

## 3. Task format & example item
n/a — no empirical items or tasks.

## 4. Scoring / grading methodology
n/a.

## 5. Dataset construction & provenance
n/a — philosophical argument drawing on Aristotle's *Nicomachean Ethics*, *Politics*, and a wide secondary literature including Nussbaum, Russell, Acemoglu & Johnson, Shadbolt & Hampson, and others.

## 6. Validity evidence
Not applicable in the empirical sense. The paper's internal validity rests on its philosophical argumentation; it explicitly acknowledges Aristotle's own errors (on slavery and women) as cautionary illustrations, not as invalidating the general framework (p.7).

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- Paper is 69 pages (frontmatter states 69 pages total).
- Aristotle's framework dates to 4th century BC; invoked as 2,400 years of accumulated refinement (p.7).
- Oxford study (pre-2024 AI advances) estimated 47% of US occupations could be "computerised" in 10–20 years (p.37, citing Frey & Osborne 2017).
- McKinsey 2018: ~5% of occupations fully automatable, but ~30% of work tasks in 60% of occupations could be automated (p.38).
- Acemoglu (2024): AI-driven GDP gains projected at 0.93–1.16% over ten years absent fundamental reorientation (p.38 footnote).
- International study: 42% of 18–35 year-olds find authoritarian government preferable to democracy (p.22 footnote).

## 10. Pitfalls & limitations
- The paper is a policy white paper, not peer-reviewed research; empirical claims (automation statistics, energy estimates) are cited from secondary sources without independent scrutiny.
- The paper explicitly rejects Aristotle's views on slavery, women, and population control, but the general claim that his framework is the "most compelling" for AI ethics is asserted rather than argued comparatively against Buddhism, Confucianism, Ubuntu, or Indigenous ethics traditions.
- The regulatory proposals in Part III are sketched rather than operationalised; the novel "right to a human decision" (p.9) lacks a worked-out institutional form.
- The AI capabilities claims (e.g., that LLMs "lack genuine belief, understanding, and communicative intent") rely on philosophical interpretation rather than interpretability research.
- No engagement with the growing empirical literature on moral psychology that complicates Aristotle's rationalist picture of virtue.

## 11. Novel ideas worth stealing
1. **Flourishing-based evaluation criterion**: Instead of benchmarking AI on preference satisfaction or rule compliance, ask whether the AI's outputs enable or impede the "free exercise of core human capacities" — reason, sociability, communication. This is a richer target construct for values-alignment benchmarks.

2. **Virtue-simulation vs. virtue-possession distinction**: Benchmark items could test whether a model correctly identifies the *difference* between an agent that does the right thing for the right reasons vs. one that merely produces the right output. This is a meaningful discriminant for alignment.

3. **Value pluralism without single-optimum**: Benchmark design should accommodate the fact that multiple responses may be equally valid; scoring rubrics that force a single correct answer may systematically penalise Aristotelian-style practical wisdom. Consider range-of-acceptable-answers scoring.

4. **Practical-wisdom items**: Design scenarios where rigid rule application yields bad outcomes, specifically testing whether models can recognise when the rules should yield to context-sensitive judgment — Aristotle's point about equity (epieikeia, NE V.10, p.20).

5. **Anti-techno-determinist framing for consent items**: When eliciting values in surveys or annotations, ask explicitly whether respondents feel they *have a choice* about AI adoption — the paper argues that the rhetoric of inevitability suppresses moral agency and thus distorts values elicitation.

6. **The "intelligent tool" framing as a benchmark category**: Distinct from "moral agent" and "assistant," the "intelligent tool" category (AI augments human capacity without replacing human judgment) is an under-benchmarked use-case that has distinct ethical requirements.

## 12. Notable quotes
- "The idea that we start from an ethical blank slate in addressing the challenges and opportunities of this transformative technology is a fallacy." (p.2)
- "Even the best rules we can devise, says Aristotle, will encounter unforeseen circumstances in which their rigid application would lead to bad or even disastrous consequences (NE V.10). We therefore need to understand that there is an ineliminable role of judgement, and an ineliminable imprecision, in ethical matters." (p.20)
- "[I]n principle any virtue, expressed in language or explicit decisions, can be simulated. Although at present these simulations are only partly convincing, that will change reasonably soon. AIs today can also effectively be deputies for us in situations that call for those virtues. What will not change in the foreseeable future is an AI's inability to truly possess a virtue." (p.33–34, quoting Shadbolt & Hampson)
- "Neither well-being nor morality reduces to one master value that is to be optimised. Instead, there is an irreducible diversity of goods that can feature in a life of well-being, such as knowledge, friendship, achievement, pleasure and so on." (p.15)

## 13. UNKNOWN / not in extract
- Full text of Part III on regulatory sign-posts was not fully read (extract was truncated at p.41 of 69); specific regulatory proposals beyond the "right to a human decision" could not be summarised from the extract.
- Appendices or bibliographic details beyond what appears in footnotes are not visible.
- No information on publication status (journal, book chapter, or standalone report) beyond the Lyceum Project branding and June 2024 date.
