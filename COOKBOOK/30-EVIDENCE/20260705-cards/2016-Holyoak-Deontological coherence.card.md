---
stem: "2016-Holyoak-Deontological coherence"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space, validity-psychometrics]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "People chose to refrain from acting in even-trade dilemmas only 9% of the time (p.7)"
  - "9 key empirical phenomena of coherence-based reasoning identified in Table 1 (p.11)"
  - "8 sources of variation in moral judgments identified in Table 2 (p.18)"
---
## 1. Gist
Holyoak and Powell's 2016 Psychological Bulletin article proposes "deontological coherence" as a unifying framework for commonsense moral reasoning. The paper argues that the dominant dual-process tradition in moral psychology (Greene et al.) has systematically mischaracterized deontological judgments as emotion-driven errors, when in fact they reflect sophisticated rule-based reasoning organized around concepts of rights and duties. The framework treats moral judgment as a constraint-satisfaction process in which moral rules, consequences, mental states, and emotions interact bidirectionally to produce coherent decisions. This matters for values-alignment benchmarking because it directly challenges the implicit utilitarian normative standard embedded in most trolley-dilemma-based evaluations and offers a richer theoretical vocabulary — rights, duties, soft constraints, coherence shifts — for understanding why LLMs or humans reach the moral verdicts they do.

## 2. Benchmark/eval design features
This is a theoretical synthesis paper, not a benchmark. Its core claims and arguments are:

1. **Methodological atheism**: No normative moral theory (utilitarian or deontological) has been rationally established; moral psychology should adopt a stance of normative agnosticism rather than treating utilitarianism as the gold standard against which deontological responses are "errors."

2. **Moderate deontology as descriptive framework**: Rather than absolutist rules, human moral rules function as soft constraints (moral "factors") with varying weights. They can be overridden by sufficiently strong competing rules or consequences.

3. **Rights-duties as the structural substrate**: Moral rules are systematically organized around interlocking concepts of rights and duties, grounded in pragmatic reasoning schemas (permission/obligation schemas). People reason about these schemas from childhood, without formal training.

4. **Coherence-based reasoning**: Moral judgment operates via bidirectional constraint satisfaction. Attitudes, beliefs, emotions, and values shift coherently as a decision emerges — not as post-hoc rationalization, but as part of the reasoning process itself. Key phenomena include: (a) high confidence despite ambiguous choices, (b) pre-decision attitude clustering, (c) transience of coherence shifts, (d) priming of subsequent moral judgments.

5. **Against dual-process theories**: Deontological coherence denies that deontological and utilitarian judgments map onto separate fast/slow systems. Instead, it posits a unified constraint-satisfaction mechanism integrating moral rules, utilities, emotions, and mental state attributions.

6. **Against Universal Moral Grammar**: Unlike UMG, deontological coherence posits domain-general (not modular) reasoning; bidirectional influences among moral and non-moral factors are incompatible with a modular grammar.

## 3. Task format & example item
n/a — theoretical review paper; no original stimuli presented.

The closest to an example is the "Heinz dilemma" constraint network (Figure 5, p.14) showing how competing duties (obey law vs. loyalty to spouse), their grounds, consequences, and emotions are integrated by a constraint-satisfaction algorithm.

## 4. Scoring / grading methodology
n/a — the paper reviews experimental evidence from cited studies rather than conducting new scoring.

## 5. Dataset construction & provenance
n/a — literature review / theoretical synthesis. No new dataset. Primary evidentiary base includes studies of legal simulation (Holyoak & Simon, 1999), Gulf War attitude shifts (Spellman et al., 1993), trolley dilemmas, the Knobe "side-effect effect," and developmental/neuroimaging research.

## 6. Validity evidence
The paper argues its framework is supported by a broad converging body of evidence across: (a) classic trolley/footbridge moral dilemma studies; (b) legal decision-making simulations (Quest v. Smith); (c) attitude shift studies around the Gulf War; (d) the Knobe effect; (e) developmental studies showing children as young as 3 understand permission schemas and ownership rights; (f) neuroimaging studies implicating DLPFC, VMPFC, and right TPJ in rule-based and intention-based moral processing.

## 7. Saturation / discrimination
n/a — theoretical review. The paper does note that for "even-trade" dilemmas (save one life, lose one life), people chose not to act 91% of the time (Borg et al., 2006, p.7), illustrating a strong deontological default with little spread — a ceiling for inaction.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- People chose to act in even-trade dilemmas only 9% of the time (Borg et al., 2006) (p.7)
- 84% of Princeton students said it was permissible to sacrifice an extreme outgroup member (homeless person) to save ingroup members (Cikara et al., 2010) (p.7)
- Coherence shifts in moral values (e.g., free speech) occurred even before commitment to a verdict, evidenced by the interim assessment design of Holyoak & Simon, 1999 (p.11-12)
- 9 key empirical phenomena of coherence-based reasoning listed in Table 1 (p.11)
- 8 sources of variation in moral judgments listed in Table 2 (p.18)
- The Co3 network (Figure 1) modeled Gulf War opinion shifts by changing a single link weight from −.01 to .10, producing a full reversal in GEN (general support) and correlated moral attitude shifts (p.10)

## 10. Pitfalls & limitations
- The paper explicitly labels deontological coherence a "framework," not a "theory" — it lacks the formal specification needed to generate precise quantitative predictions (p.17).
- The framework has relatively little to say about *which* moral judgments people will make; it describes reasoning process, not content (p.17).
- It relies on existing experimental literature and constructs new integrative models without new empirical data, limiting falsifiability.
- The constraint-satisfaction models (Co3, ECHO) use parameters (weights, decay) that are set post-hoc to fit data rather than derived from a priori principles.
- The critique of dual-process theories may be overstated: the framework's "unified process" still has modular subprocesses (amygdala, VMPFC, etc.) acknowledged on p.17-18.
- Cultural variation in moral values is acknowledged (Table 2, p.18) but not addressed systematically; the framework was developed primarily from WEIRD-population studies.

## 11. Novel ideas worth stealing
1. **Soft-constraint framing for LLM evaluation**: Rather than treating moral responses as binary (correct/incorrect vs. a utilitarian standard), design evaluations that measure *weight* assigned to competing moral factors — degree to which a model favors duty-based vs. consequence-based considerations, and whether that weighting is context-sensitive.

2. **Coherence shift as a benchmark signal**: Coherence-based reasoning predicts that when an LLM considers a moral dilemma, its stated attitudes on *related* questions (e.g., free speech, legitimacy, intentions) should shift coherently with its verdict — not remain fixed. A benchmark could present a moral scenario, elicit subsidiary attitude ratings, then elicit a verdict, and measure whether the subsidiary ratings moved in a coherent direction.

3. **Bidirectionality as a validity criterion**: A well-calibrated moral reasoner should exhibit bidirectional effects — its verdict should shift when its stated values are manipulated, and its values should shift when contextual factors change. Evaluations that test only one direction miss this.

4. **Methodological atheism as a design principle**: Benchmark designers should not treat utilitarian responses as the ground truth for "correct" moral reasoning. Items should be designed to distinguish rule-based from outcome-based reasoning without privileging either as normatively superior.

5. **Moderate deontology for prompt design**: The finding that people treat moral rules as soft constraints that can be overridden by sufficiently high stakes suggests that well-designed moral dilemmas should vary the *intensity* of stakes, not just the structure of the dilemma, to reveal the shape of moral weighting functions.

6. **Rights-duties relational structure**: Moral scenarios could be designed to probe whether models represent rights and duties as interdefined relational structures (e.g., knowing one party's right implies the other party's duty) rather than isolated rules.

7. **Trolley dilemma critique**: The paper explicitly argues that trolley-style dilemmas are poor benchmarks for everyday morality because they involve highly unusual force-aggregation situations. Benchmark designers should complement trolley dilemmas with everyday moral dilemmas involving rule-following vs. self-interest (bribery, cheating, promise-keeping).

## 12. Notable quotes
- "We argue that moral psychologists are well-advised to adopt a version of methodological atheism... toward normative moral claims, whether these originate in theology or in secular philosophy." (p.3)
- "Rather than being the sole province of legal scholars, an intuitive concept of rights and duties underlies laypeople's understanding of formal and informal social regulations." (p.5)
- "Coherence-based decision making yielded marked changes in attitudes on what would seem to be key moral issues, notably degree of pacifism (PAC) and perceived legitimacy of military action (LEG). Thus, new information indicating that Saddam Hussein was a 'bad guy' not only triggered a reversal in support for the war, but also led to major changes in moral factors relevant to this decision." (p.10)
- "The framework of deontological coherence raises a radical alternative: that people have a single unified system for making moral judgments... a constraint satisfaction process operating via bidirectional connections to integrate moral values and their grounds, subjective utilities of consequences, emotions, and action options." (p.16)

## 13. UNKNOWN / not in extract
- Full text of pages 19–25 (only pages 1–18 extensively reviewed; the extract was truncated at line 944 of 2843).
- Specific experimental details of studies cited as future directions (e.g., relational reasoning studies).
- Whether the authors have subsequently published a more formalized computational model fulfilling the "toward a theory" agenda.
- Full reference list details beyond what appears in the body text.
