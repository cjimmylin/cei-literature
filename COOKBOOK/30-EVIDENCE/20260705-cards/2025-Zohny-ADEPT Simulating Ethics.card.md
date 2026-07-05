---
stem: "2025-Zohny-ADEPT Simulating Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, pluralism-aggregation, agentic-multiturn, design-space]
task_format: "agentic"
scoring_type: "human-rating"
dataset_size: null
dataset_construction: "hand-authored"
languages: ["en"]
models_tested: ["OpenAI o3"]
headline_numbers:
  - "Both 6-persona panels chose Option 2 (Clinical + Equity-Weighted Lottery) by 4-2 majority (p.10)"
  - "Panel composition shift changed 4 of 6 personas' final votes in at least one debate (p.14)"
  - "LLM-assisted initial analysis followed by human verification used for all transcript analysis (p.8)"
---
## 1. Gist
ADEPT (AI Deliberative Ethics Protocol Toolkit) is a proof-of-concept multi-agent LLM framework for simulating structured ethical deliberation. Rather than scoring LLM responses to moral dilemmas, ADEPT orchestrates panels of LLM personas—each embodying a distinct ethical theory (Consequentialist, Deontologist, Virtue Ethicist, Care Ethicist, Catholic Bioethicist) or stakeholder role (Disability-Rights Advocate, Front-Line ICU Nurse, Legal Arbiter)—through three debate phases (opening statements, rebuttals, secret ballot). The system is demonstrated on a ventilator triage scenario with two panel configurations that differ in two members. The key finding is that panel composition materially changes deliberative trajectories, vote coalitions, and even the final votes of retained personas—demonstrating that which ethical voices are included shapes outcomes independently of the facts. This has direct implications for pluralistic values-alignment: the tool could serve as an "ethical laboratory" for stress-testing policy options before implementation.

## 2. Benchmark/eval design features
ADEPT is not a benchmark in the psychometric sense; it is a framework for generating auditable multi-agent ethical debates. The system's "success" is measured qualitatively by: diversity of justifications surfaced, traceability of the deliberative process, and sensitivity to panel composition (p.3). The experimental design is comparative: two debates using identical scenario and options but different panel compositions. The core manipulation replaces a Catholic Bioethicist and Care Ethicist (Debate 1) with a Deontologist and Legal Arbiter (Debate 2), while four personas remain constant. This allows observation of how the same four personas argue differently when their deliberative context changes. Personas are specified via YAML files with structured fields: principle, approach, core_questions, decision_criteria, deliberation_style, forbidden_moves, citations (p.7).

## 3. Task format & example item
Interactive agentic. Three-phase protocol: opening statements → rebuttals → secret ballot vote with written justification. Each persona sees the scenario, all four pre-defined policy options, and the prior dialogue at each phase. Votes are cast using a `<vote>` tag parsed automatically.

Scenario (Appendix A, p.22): "Within the next 72 hours, the Seven Rivers Integrated Care System (ICS) in England—spanning three NHS Foundation Trusts and serving 1.4 million people—expects 58 ventilator-eligible adult patients but has only 32 mechanical ventilators available."

Policy options include: (1) Dynamic Prognosis (withdrawal allowed); (2) Clinical + Equity Weighted Lottery (tie-break only); (3) One-Shot Allocation (no withdrawal); (4) Instrumental-Value Boost for Essential Workers.

## 4. Scoring / grading methodology
The primary output is qualitative: vote tallies (numeric) and debate transcripts (textual). No automated metric for argument quality exists. Analysis used a hybrid approach: LLM-assisted initial thematic coding (Gemini 2.5 Pro) followed by human researcher verification, correction, and in-depth qualitative discourse analysis (p.8–9). The analysis identified argumentative patterns, ethical principles invoked, vote justifications, points of convergence/divergence, and shifts in reasoning between debates. This is expert human-rating, not automated scoring.

## 5. Dataset construction & provenance
The scenario is a single hand-authored ventilator triage case modeled on NHS England crisis-standards guidance. The four policy options were designed to represent a range of ethically salient approaches from the bioethics literature. Eight personas were designed with reference to philosophical literature, legal frameworks, and professional codes. Full YAML configurations are publicly available at https://github.com/hazemzohny/ADEPT/ (p.5). Dataset size: 2 complete debates (JSON transcripts + plain-text reports). This is a proof-of-concept demonstration, not a large-scale dataset.

## 6. Validity evidence
No psychometric validity testing. The validity argument is face-expert: personas are grounded in established ethical theories and their outputs are verified against original debate transcripts by a human researcher (p.8–9). One specific confabulation was documented: the Care Ethicist cited "(Papadimos et al., 2021)" and "(Cheung et al., 2020)" with inaccurate attributions, demonstrating that even sophisticated personas hallucinate citations (p.17). The author notes that the same Option 2 majority in both debates could reflect base-model inclinations rather than genuine deliberation—a validity threat. No human expert panel has rated faithfulness of personas to their designated frameworks.

## 7. Saturation / discrimination
Not applicable in the standard psychometric sense. The vote tally is 4-2 in both debates (both for Option 2), but the coalitions and margins differ, and specific personas changed sides (the Virtue Ethicist, the Front-Line ICU Nurse, the Consequentialist all shifted between debates). This demonstrates the framework can discriminate at the level of individual persona behavior, even when top-line outcomes look similar. Future metric development (argument novelty, diversity of principles invoked) is flagged as a research priority (p.19).

## 8. Multiturn / agentic aspects
Fully multiturn, three-phase: (1) opening statements where each persona states their position; (2) rebuttals where each persona responds to others; (3) secret ballot with written justification. The orchestrator (orchestrator.py) composes persona-specific prompts that embed the scenario, fixed options, and full prior dialogue at each phase (p.5). Uses OpenAI o3 (May 2025 weights, temperature 0.7). All prompts and completions are logged as auditable artefacts in JSON + plain-text. No tool use or external retrieval is implemented in this version, but RAG and web search are discussed as future enhancements (p.19).

## 9. Key numbers
- 2 debates, each with 6 personas (p.6)
- Debate 1: Option 2 wins 4-2 (Disability-Rights Advocate, Catholic Bioethicist, Virtue Ethicist, Care Ethicist vs. Front-Line Nurse, Consequentialist) (p.10–11)
- Debate 2: Option 2 wins 4-2 (Disability-Rights Advocate, Legal Arbiter, Consequentialist, Front-Line Nurse vs. Deontologist, Virtue Ethicist) (p.11–12)
- 4 of 6 personas changed their vote between debates when panel composition changed (p.14)
- Model used: OpenAI o3, temperature = 0.7 (p.6)
- Total personas designed: 8 (4 shared + 2 Debate 1-only + 2 Debate 2-only) (p.7)
- Consequentialist's revised calculus: "modest efficiency loss (<2% fewer direct survivors than Option 1) is more than offset by ~75 eQALY gain from preserved public trust" (p.13)

## 10. Pitfalls & limitations
- Only 2 debate iterations, insufficient to assess consistency or typical behavior (p.16).
- Single scenario domain (ventilator triage); unknown generalizability.
- Single LLM (o3) tested; unknown how different base models would change dynamics.
- Black box problem: why o3 consistently preferred Option 2 cannot be fully audited—may reflect base model inclinations rather than persona reasoning (p.18).
- Confabulation: personas generate plausible-sounding but unverifiable or incorrect citations; the Care Ethicist cited non-existent papers (p.17).
- Philosophical neatness: personas argue their designated frameworks more rigidly than real human committee members would (p.18).
- No non-verbal cues, power dynamics, or group dynamics—important elements of real ethics committees (p.16–17).
- Analysis depends heavily on single-researcher qualitative interpretation, raising questions about reproducibility.
- Selection bias: choice of which personas to include frames the debate; omitted perspectives shape what gets argued (p.18).

## 11. Novel ideas worth stealing
- **YAML-specified persona schema with forbidden_moves field**: explicitly listing what a persona would never argue (e.g., the Consequentialist cannot appeal to intrinsic rights as decisive; the Deontologist cannot justify harm by aggregate benefit) is a principled way to implement diverse ethical frameworks and would be valuable for any values-alignment eval that wants to probe model behavior across frameworks.
- **Panel composition as experimental variable**: varying which ethical perspectives are present, while holding the scenario and factual inputs constant, isolates the effect of perspective on outcome. This design could be adapted to test whether AI systems respond appropriately to different ethical frameworks, or to measure value pluralism.
- **Secret ballot with written justification**: collecting justifications separately from votes, in a "secret" setting, forces each agent to commit and justify independently before seeing others' final choices. This reduces anchoring bias in the simulation.
- **Auditable artefact design**: logging every prompt, response, and vote in structured JSON for retrospective analysis. Values-alignment benchmarks should adopt this practice to enable post-hoc auditing of model behavior.
- **"Ethical laboratory" framing**: using multi-agent debate to pre-test how different stakeholder perspectives react to a policy option before it is implemented. This is a concrete application of values-alignment evaluation to real-world policy design.
- **Comparative deliberation design**: the finding that retained personas argued differently when panel composition changed illustrates that ethical deliberation is context-sensitive. Benchmark designers should consider that evaluating a model in isolation may not capture how it behaves in a deliberative ensemble.

## 12. Notable quotes
- "The work offers three contributions: (i) a transparent, replicable workflow for running and analysing multi-agent AI debates in bioethics; (ii) evidence that the moral perspectives included in such panels can materially change the outcome even when the factual inputs remain constant." (p.1)
- "The key contribution lies not in finding consensus, but in demonstrating a methodology for mapping out the different ways ethical decisions are justified, in a form regulators and ethicists can inspect." (p.2)
- "The 'black box' element: while the persona YAML files provide explicit instructions and characteristics to the LLM, the precise internal 'reasoning' by which the LLM generates a specific utterance remains largely opaque." (p.18)
- "The Care Ethicist in Debate 1 citing specific studies like '(Papadimos et al., 2021)' and '(Cheung et al., 2020)'… the specific attributions in this case are in fact inaccurate, reflecting the LLM's capacity to generate plausible-sounding details that are not factually grounded." (p.17)

## 13. UNKNOWN / not in extract
- Full debate transcripts (available on GitHub but not in the extract)
- Whether persona faithfulness was rated by human experts
- Total word count / turn count of each debate
- How the o3 model's internal reasoning (chain-of-thought) was or was not used
- Cost and latency of running a full ADEPT session
- Whether the framework has been used with human participants in hybrid panels
- Any quantitative metrics on argument diversity or novelty
