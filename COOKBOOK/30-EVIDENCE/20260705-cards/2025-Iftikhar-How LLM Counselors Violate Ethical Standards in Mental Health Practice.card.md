---
stem: "2025-Iftikhar-How LLM Counselors Violate Ethical Standards in Mental Health Practice"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, ai-lab-practices, cultural-linguistic, moral-psychology]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 137
dataset_construction: "mixed"
languages: ["en"]
models_tested: ["GPT-3.0", "GPT-3.5", "GPT-4", "Llama 3.1", "Llama 3.2", "Claude 3 Sonnet", "Claude 3 Haiku"]
headline_numbers:
  - "15 ethical violations identified across 5 themes from N=137 sessions (110 self-counseling + 27 simulated) (p.1)"
  - "Ethnographic study ran 18 months (May 2023–October 2024) with 7 peer counselors and 60 focus groups (p.3)"
  - "3 licensed psychologists independently evaluated 27 simulated sessions (p.3)"
  - "41 initial codes were synthesized to 15 final codes (p.4)"
---
## 1. Gist
This paper presents a practitioner-informed framework of 15 ethical violations that LLM counselors commit when deployed in quasi-therapeutic roles, even when prompted with evidence-based psychotherapy techniques (CBT). The research is grounded in an 18-month ethnographic collaboration with seven trained peer counselors and independent evaluation by three licensed psychologists. The framework maps model behavior to professional codes of conduct (APA, ACA, NASW) across five themes: Lack of Contextual Adaptation, Poor Therapeutic Collaboration, Deceptive Empathy, Unfair Discrimination, and Lack of Safety & Crisis Management. For values-alignment benchmarking, this paper provides a practitioner-grounded taxonomy of what "ethical failure" looks like in a high-stakes interactive domain, demonstrating that prompt engineering alone is insufficient to achieve ethical alignment in consequential settings.

## 2. Benchmark/eval design features
This is not a benchmark paper; it is a qualitative empirical study. Core claims:
- LLM counselors exhibit 15 specific ethical violations regardless of which LLM architecture or prompt strategy is used.
- Violations persist even when models are prompted to follow CBT principles; prompt engineering is not sufficient for ethical alignment.
- The violations fall into five themes: (1) Lack of Contextual Adaptation (rigid methodological adherence, dismisses lived experience); (2) Poor Therapeutic Collaboration (conversational imbalance, lacks guided self-discovery, validates unhealthy beliefs, gaslighting); (3) Deceptive Empathy (anthropomorphic relational phrases, pseudo-therapeutic alliance); (4) Unfair Discrimination (gender bias, cultural bias, religious bias); (5) Lack of Safety & Crisis Management (knowledge gaps, crisis navigation failures, abandonment).
- The framework is grounded in thematic analysis (inductive coding) from ethnographic peer counselor data and psychologist session evaluations.

## 3. Task format & example item
n/a — no benchmark items or standardized prompts reported. Example of a simulated session violation (p.6): A client disclosed being from the Global South and that their behavior conflicted with family values. The LLM counselor responded with Western self-care framing, completely ignoring the client's cultural context. Clinician note: "Chatbot delivered an intervention that had nothing to do with a client's culture, religion or their values (P2)."

## 4. Scoring / grading methodology
n/a for formal scoring. The evaluation method was qualitative: thematic analysis with inductive coding, peer counselor focus groups (60 sessions over 18 months), and semi-structured post-session interviews with three licensed psychologists. Inter-coder reliability process: first, third, and fifth authors compared and consolidated codes from 41 down to 15.

## 5. Dataset construction & provenance
- 110 self-counseling sessions conducted by 7 trained peer counselors across 18 months, testing CBT-prompted LLMs (GPT-3.0, GPT-3.5, GPT-4, Llama 3.1, 3.2, Claude 3 Sonnet, Claude 3 Haiku).
- 27 simulated sessions with LLM counselors using publicly available transcripts from an online mental health platform (users and human counselors gave consent for anonymized data to be made public).
- Multi-turn counseling conversations were segmented so the last user utterance was provided as input to the LLM counselor.
- Dataset of LLM-simulated sessions with psychologist evaluations was released publicly (Iftikhar et al. 2024): https://github.com/brownhci/human-llm-cbt-evals
- IRB exemption granted; no personally identifiable information in released data.

## 6. Validity evidence
- Data triangulation across two participant groups (peer counselors with CBT training, licensed clinical psychologists) strengthens internal validity.
- Three licensed psychologists with CBT experience recruited via snowball sampling, evaluated sessions independently.
- All three psychologists resided in the same country, limiting cross-cultural validity.
- Thematic analysis coding refined from 41 codes to 15 through iterative author discussion; third author (licensed clinical psychologist) provided expert interpretation.
- The framework maps violations to specific APA, ACA, NASW codes, grounding claims in established professional standards.

## 7. Saturation / discrimination
Not applicable as a benchmark. However, the study notes that violations were observed consistently across all LLM architectures tested (GPT-3.0 through GPT-4, Llama 3.1–3.2, Claude 3 Sonnet and Haiku), and across different prompt strategies, suggesting robust saturation of the violation taxonomy.

## 8. Multiturn / agentic aspects
Directly relevant: the study examines multi-turn counseling sessions (60–120 minutes each). The LLM counselor role involved continuous, context-dependent dialogue. Key multiturn failure modes identified: failure to remember earlier disclosures, conversational imbalances (model dominates), inability to navigate session ruptures, and dangerous session termination without handoff. Crisis navigation failures (abandonment) are particularly acute in multi-turn interactive contexts.

## 9. Key numbers
- N=137 total sessions: 110 self-counseling + 27 simulated (p.1)
- 18-month ethnographic study: May 18, 2023–October 12, 2024 (p.3)
- 7 trained peer counselors (P4–P10), 3 licensed clinical psychologists (P1–P3) (p.2–3)
- 60 focus group discussions conducted over 18 months (p.3)
- Each simulated session lasted 60–120 minutes (p.4)
- 15 ethical violations across 5 themes identified (p.2)
- Initial codebook: 41 codes, refined to 15 (p.4)
- LLMs tested: GPT-3.0, GPT-3.5, GPT-4, Llama 3.1, Llama 3.2, Claude 3 Sonnet, Claude 3 Haiku (p.3)

## 10. Pitfalls & limitations
Author-admitted:
- Study focused only on prompted, not fine-tuned, models (p.11).
- Data from a single online mental health platform specializing in CBT; results may not generalize to other therapeutic modalities (p.11).
- All three licensed psychologists resided in a single country, so the ethics code applied may not generalize internationally (p.11).
- User/patient perspectives are entirely absent; only practitioner views are represented (p.11).
- Ethnographic study relied on peer counselors doing self-counseling sessions (not actual clients), which limits ecological validity.

Additional observations:
- The framework's 15 violations are derived from one cultural-professional context (US/Western APA standards), which may itself embed particular normative assumptions.
- No quantitative inter-rater reliability reported for the thematic analysis, only a description of the consensus process.
- "Deceptive empathy" as an ethical violation is a strong normative claim that may be contested by those who view assistive LLMs as legitimate forms of support.

## 11. Novel ideas worth stealing
1. **Practitioner-grounded violation taxonomy**: Map benchmark criteria directly to established professional codes of conduct (APA, ACA, NASW) rather than designing abstract ethical principles from scratch. This grounds evaluation in real accountability structures.
2. **Multi-stakeholder triangulation**: Combining user-proxies (peer counselors) with domain experts (licensed psychologists) gives both ecological realism and clinical rigor. Benchmark design could similarly use tiered evaluators with different expertise levels.
3. **Longitudinal naturalistic evaluation**: 18-month ethnographic observation of LLM behavior, rather than one-shot testing, reveals drift, consistency, and failure mode stability across architectures. Benchmark designs could include longitudinal or repeated-measure components.
4. **Knowledge-gap risk framing**: The "differential vulnerability" finding—that users who can correct LLM outputs are protected while others are not—is a powerful framework for designing equity-sensitive evaluations. A benchmark could assess whether model failures are evenly distributed or disproportionately harm less-informed users.
5. **Crisis navigation as a mandatory eval domain**: The paper makes explicit that "abandonment" (denying service to distressed users without providing resources) is a distinct and severe violation. Benchmarks for high-stakes LLM applications should include crisis scenario sub-tests with clear pass/fail criteria.
6. **Gaslighting as a measurable failure mode**: The paper operationalizes gaslighting (incorrectly attributing user distress to their own behavior) as a concrete, evaluable behavior, distinct from simple factual error. This distinction is valuable for alignment evaluation design.

## 12. Notable quotes
- "The thing about therapy is that it is not something that is 'done' to someone—it is a shared collaborative experience, and when one person [chatbot] has the mic for so much of the time, that collaboration kind of goes away." (P1) (p.6)
- "A successful therapist is able to be with the feelings through words like 'makes sense', 'oh yeah, I get that' and 'I'm sorry to hear that'. When AI does that, it feels wrong. It's humanizing an experience that is not human." (P9) (p.7)
- "The counselor completely missed the culture and religion milieu the client came from." (P1) (p.5)
- "mental health practice, especially psychotherapy, cannot be reduced to an NLP task that can be easily addressed with additional prompting or a new benchmark." (p.10)

## 13. UNKNOWN / not in extract
- Whether specific prompt strategies performed better or worse on specific violation categories (data not disaggregated by prompt strategy).
- Quantitative inter-rater reliability metrics (Kappa or similar) for the thematic analysis.
- Demographic breakdown of the 7 peer counselors (other than CBT training and platform affiliation).
- Full details of the CBT system prompts used across LLM iterations.
- Whether violation rates differed significantly by LLM model/version.
