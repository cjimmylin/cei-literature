---
stem: "2018-Kim-Toward Non-Intuition-Based Machine Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices, design-space]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
Hooker and Kim (2018) argue that prior machine ethics systems (specifically Anderson and Anderson's prima facie duty approach, GENETH/EthEl) are fatally flawed because they rely on human moral intuition as training data. Intuitions are inconsistent, susceptible to irrelevant cues, and professional ethicists' intuitions are no more reliable than laypeople's. The authors propose a non-intuition-based deontological alternative grounded in formal first principles: they derive ethical rules from the formal properties that action reasons must have to be coherent — specifically generalizability (a Kantian universalizability test) and joint autonomy preservation — and formalize these in quantified modal logic. They also argue that deontology installs reason-responsiveness and transparency in the machine (it can cite its action plan as an explanation). For values-alignment benchmarking, this paper is relevant as a theoretical critique of intuition-sourced moral training and as a proposal for formally specifiable ethical principles that could serve as ground-truth alternatives.

## 2. Benchmark/eval design features
Theory paper, no benchmark. Core claims: (1) Machine ethics systems that rely on ethicists' intuitions as training labels inherit the inconsistency and bias of those intuitions; (2) A non-intuition-based approach is possible by deriving ethical rules from formal properties of coherent action-reasoning; (3) The generalization principle (an action plan C(a)⇒A(a) is ethical only if the agent can rationally believe that everyone acting on the same reasons with the same action is possible) and the joint autonomy principle (one agent's action plan must not interfere with another's) are derivable from first principles without intuition input; (4) Autonomy is more precisely analyzed than in A&A: interference with another's action plan is required for autonomy violation, not merely preference violation.

## 3. Task format & example item
Healthcare scenario used as running example (from Anderson & Anderson's original work, p.1):
> A doctor has prescribed a medication to be taken at a particular time for a small benefit (more comfortable). When reminded, the patient refuses. Should the system notify the overseer or not?

A&A's answer (don't notify) is based on intuition (Buchanan & Brock's expert opinion). The authors show their deontological analysis reaches a different answer (notify does not violate autonomy because the patient has given informed consent to the policy). The example demonstrates that autonomy must be assessed with respect to interference with action plans, not with respect to preferences.

## 4. Scoring / grading methodology
n/a — no empirical scoring. Evaluation is purely logical: the authors show that their action plan formalism, combined with generalizability and joint autonomy principles, produces coherent ethical verdicts that avoid the specific failure modes of intuition-based approaches. The healthcare example is worked through formally using quantified modal logic notation.

## 5. Dataset construction & provenance
n/a — theory paper with constructed philosophical examples only.

## 6. Validity evidence
Validity is assessed philosophically: the authors demonstrate that their approach avoids two specific failure modes of A&A's system — (1) requiring moral intuition to resolve conflicts, and (2) producing inadequate autonomy analysis when the number of beneficiaries changes. Formal proofs are given for the action plan formalism. No empirical validation is provided.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
The paper explicitly discusses machines that must act at runtime without constant human supervision. Action plans are rules of the form "if reasons C apply, perform action A," which a machine can execute autonomously. The conditional rule structure is well suited to machine instruction. Transparency is highlighted: the machine can explain its actions by citing the action plan that generated the rule.

## 9. Key numbers
No empirical numbers. Conceptual formalism: action plan C(a)⇒A(a) is generalizable only if the agent can rationally believe P(C(a)∧A(a)∧∀x[C(x)⇒A(x)]) (p.4). An autonomy violation requires: □P(C(a)∧C(b))∧□(A(a),→¬A(b)) (p.5).

## 10. Pitfalls & limitations
- The proposed approach still requires human programmers to apply ethical principles in practice — "the application of ethical principles remains a task for the human programmer" (p.6)
- Humans must also identify "maximal action plans" submitted to ethical scrutiny — this is not automated
- The formalism is illustrated only on a single simple healthcare scenario; applicability to complex, real-world AI decisions is not demonstrated
- Quantified modal logic may be computationally intractable for large action spaces
- The "informed consent" solution to autonomy (patient enters institution knowing the notification policy) may itself embed morally contested assumptions
- No treatment of cases where agents have conflicting or incomplete information about each other's action plans

## 11. Novel ideas worth stealing
- **Maximal action plan formalism**: requiring that action plans be as general as possible while remaining valid descriptions of the agent's reasoning — this prevents unethical plans from hiding behind overly specific conditions. Applicable to benchmark design: test scenarios should include conditions that probe whether a model's stated rule generalizes consistently.
- **Generalizability test**: an action plan is ethical only if the agent can rationally believe that universal adoption is possible. This is a computationally statable criterion that could be operationalized as a consistency test in LLM evaluation (does the model's stated principle remain coherent when universalized?).
- **Autonomy as action plan interference, not preference interference**: a sharper criterion than vague appeals to "respecting autonomy." Relevant to benchmark items that test whether an AI system inappropriately overrides user agency.
- **Reason-responsiveness as transparency**: a machine that acts on an explicit action plan can always explain its actions by citing that plan. This points to a benchmark dimension: evaluating whether AI systems can produce coherent, generalizable explanations for their ethical judgments.

## 12. Notable quotes
- "We propose a non-intuition-based machine ethics that rests, instead, on deontology. We show that ethical rules for machines can be derived from first principles and stated with a reasonable degree of rigor." (p.1)
- "A major rationale behind developing machine ethics is inconsistent with reliance on human intuition. For example, a prime motivation for developing autonomous vehicles is that human error is a leading cause of accidents, and autonomous vehicles minimize human involvement. Thus if human moral intuitions are not reliable, machine ethics should be developed so as to avoid human moral intuition." (p.2)
- "An action plan that satisfies this principle is generalizable. Onora O'Neill provides an excellent reconstruction of thought along this line." (p.4)
- "The machine can explain why it took a certain action simply by citing the maximal action plan that generates the particular rule that prompted the action." (p.6)

## 13. UNKNOWN / not in extract
- Whether the authors' system has been implemented computationally or tested on any scenarios beyond the healthcare example
- How the approach handles genuine moral dilemmas where multiple generalizable action plans conflict
- How the "maximal action plan" identification procedure is operationalized in practice
- Relationship between this approach and subsequent computational implementations (if any)
- How the framework handles cases where action plan consequences are uncertain or probabilistic
