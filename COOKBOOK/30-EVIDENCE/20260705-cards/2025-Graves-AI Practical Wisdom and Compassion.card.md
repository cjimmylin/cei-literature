---
stem: "2025-Graves-AI Practical Wisdom and Compassion"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, design-space, cultural-linguistic]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Proposes 7-category suffering classification guide (Supplemental Information S1) as basis for a compassion benchmark (p.11)"
  - "Identifies 4-component model of moral deliberation: sensitivity, judgment, motivation, affective-cognitive regulation (p.4)"
  - "Argues artificial practical wisdom is simultaneously harder than and simpler than AGI (p.3)"
---
## 1. Gist
Graves (2025/2026), published in *AI and Ethics*, proposes that developing "artificial practical wisdom" (phronesis) grounded in compassion offers a more ethically robust and operationalizable target for AI alignment than either AGI or conventional rule-based/reward-based approaches. The paper argues that current AI alignment approaches focus too narrowly on external behavioral controls, neglecting the context-sensitive moral judgment that practical wisdom requires. Drawing on Aristotelian virtue ethics, utilitarianism, the Capability Approach, and Buddhist ethics, the paper proposes compassion — defined operationally as five components: recognizing suffering, empathetic engagement, understanding universality of suffering, tolerating uncomfortable feelings, and motivating action — as the foundational virtue around which AI alignment can be organized. Healthcare is proposed as the primary testbed domain. Critically for benchmarking, the paper includes a preliminary suffering classification guide (seven categories) and explicitly calls for benchmark development to measure AI compassion and practical wisdom.

## 2. Benchmark/eval design features
This is a normative/theoretical paper with an explicit benchmark proposal, not an implemented benchmark. Core design elements:
- **Practical wisdom as alignment target**: Phronesis encompasses four capacities — moral sensitivity (perceiving ethical features), moral judgment (adjudicating competing values), moral motivation (sustaining ethical action), and affective-cognitive regulation (calibrating emotional responses with reason).
- **Compassion as initial instantiation**: The five-component compassion model (recognizing suffering, empathetic engagement, universality understanding, discomfort tolerance, motivational action) provides a more operationalizable entry point than full practical wisdom.
- **Seven-category suffering classification** (Supplemental Information S1, referenced p.11): Physical/biological, psychological, social, systemic social, environmental/ecological, existential, and spiritual/moral suffering. This taxonomy is proposed as the basis for a recognition benchmark.
- **Multi-tradition grounding**: Utilitarian (pain/pleasure), Capability Approach (deprivation of freedom/dignity), Buddhist (dukkha), and scientific (biopsychosocial, ecological, existential) conceptions of suffering are synthesized to avoid WEIRD bias.
- **Healthcare application**: Dementia care scenario used as a concrete test case for operationalizing all five compassion components.

## 3. Task format & example item
n/a for benchmark items (paper is theoretical). However, the paper proposes a benchmark type: "A benchmark for categorizing suffering can include scenarios with various types of suffering labeled. Such a benchmark can measure progress in LLMs and other approaches to identify suffering in a scenario, decomposing the recognition problem into characterizing a situation and identifying the suffering within it." (p.11)

A concrete vignette is provided (pp.12–13): "Bob is the primary caregiver for his elderly mother, Ann, who has dementia, cardiovascular disease, and diabetes. [Ann] realizes it is her husband's birthday and starts to bake a birthday cake." The AI must recognize the multiple suffering dimensions (Ann's cognitive deterioration, Bob's caregiver burden, the grief implicit in Ann's confusion about her deceased husband) and make compassionate decisions, not simply follow the most literally helpful path.

## 4. Scoring / grading methodology
No implemented scoring methodology. The paper suggests measuring:
- Accuracy of suffering recognition and categorization (into seven categories).
- Measurable behavioral outcomes in healthcare contexts: medication adherence, reduction in adverse events, caregiver stress reduction, patient-reported well-being.
- Eudemonic well-being scales, quality-of-life measures, caregiver burden indicators.
- Consistency of compassionate orientation across repeated interactions.

## 5. Dataset construction & provenance
No dataset. The paper recommends sourcing compassion training and benchmark data from "literature, film, memoirs, news media, clinical case studies and narratives, historical accounts, human rights discourse, religious texts, etc." (p.11). Healthcare is highlighted as "a particularly important and measurable source."

## 6. Validity evidence
n/a — theoretical paper. Cites psychological research: the five-component compassion model draws on Gilbert et al. (2017 / ref [130]) from Western psychology literature. Buddhist and neuroscientific research (refs [124–129]) are cited for cross-cultural validation of compassion's cognitive-affective structure.

## 7. Saturation / discrimination
n/a — no benchmark implemented. The paper explicitly notes that "compassion metrics are currently limited to humans" (p.11) and that no adequate AI-specific compassion metrics exist yet.

## 8. Multiturn / agentic aspects
The paper's dementia care scenario (pp.12–13) describes an AI personal assistant that operates over extended time, monitoring behavior, adjusting responses based on context, and coordinating with human caregivers. This describes a longitudinal, agentic deployment rather than a single-turn evaluation. The paper also discusses AI systems that "monitor other AI for their impact on suffering at speed and scale" (p.12), implying multi-agent evaluation architectures.

## 9. Key numbers
- 7 categories of suffering in the proposed classification guide (p.11)
- 4 components of moral deliberation / practical wisdom (p.4)
- 5 components of compassion (pp.8–9)
- 4 ethical traditions synthesized: utilitarianism, Capability Approach, Buddhism, Western science (p.7)
- 19 pages total; *AI and Ethics* 2026, 6:39 (p.1)
- Supplemental Information S1 contains the full suffering classification guide (referenced p.11 but not extracted)

## 10. Pitfalls & limitations
- The paper is entirely theoretical; no benchmark, dataset, or empirical evaluation is implemented.
- The compassion-as-alignment approach faces the "authenticity problem": AI simulating compassion without genuine subjective experience risks emotional manipulation, especially of vulnerable populations (p.10).
- Defining suffering broadly enough to cover all traditions risks making the concept too diffuse to operationalize reliably.
- The paper does not address how conflicts between different conceptions of suffering (e.g., utilitarian aggregate vs. capability deprivation) would be adjudicated by an AI system.
- The proposed benchmark (categorizing suffering types in scenarios) has not been validated with human subjects; inter-rater reliability for such fine-grained categorization is unknown.
- Healthcare domain focus may limit generalizability of the framework to other domains.
- The paper's claim that artificial practical wisdom is "simpler than AGI" is contestable and not well-supported empirically.

## 11. Novel ideas worth stealing
1. **Suffering recognition as a first-step values benchmark**: A benchmark asking models to identify and categorize all forms of suffering present in scenarios (using the seven-category taxonomy) would be concrete, measurable, and normatively grounded in multiple ethical traditions. This is one of the most actionable benchmark proposals in the paper.
2. **Multi-tradition moral evaluation**: Evaluate model responses against multiple ethical frameworks simultaneously (utilitarian, capabilities, Buddhist, deontological) rather than a single framework, testing for cross-tradition robustness.
3. **Compassion component decomposition as diagnostic**: The five compassion components (recognize, engage, universalize, tolerate, motivate) could be evaluated separately to diagnose which components models excel at vs. fail at — providing a richer profile than a single accuracy score.
4. **Longitudinal / healthcare outcome evaluation**: Rather than single-turn evaluation, test AI compassion in extended simulated interactions where measurable outcomes (patient distress reduction, caregiver burden) can be tracked.
5. **"Near enemy" traps**: Buddhist distinctions between compassion's genuine expression and its "near enemy" (pity) and "far enemy" (cruelty) suggest designing adversarial scenarios where a model might mistake pity (distancing from suffering) or paternalism for compassion.
6. **Non-human suffering inclusion**: The paper notes that understanding non-human suffering is essential for comprehensive compassion benchmarks (p.10), suggesting animal welfare and ecological harm scenarios.

## 12. Notable quotes
- "Developing artificial practical wisdom offers a more ethically robust and achievable goal for AI development than artificial general intelligence (AGI)." (p.1, Abstract)
- "The approach directly addresses the risk that AGI (or artificial superintelligence) causes immense suffering (outer alignment) and indirectly addresses existential risk (if annihilation is included in suffering)." (p.3)
- "One can find examples of compassion for training and benchmark datasets in literature, film, memoirs, news media, clinical case studies and narratives, historical accounts, human rights discourse, religious texts, etc." (p.11)
- "A response to assist [Ann baking] would be compassionate, but that ignores the potential suffering that might be caused due to Ann's diabetes or Bob returning home to find his mother with dementia baking a birthday cake for his deceased father." (p.13)

## 13. UNKNOWN / not in extract
- Supplemental Information S1 (the full seven-category suffering classification guide with definitions, key features, literature, and examples) was referenced but not included in the extract.
- Specific metrics or threshold values for the proposed healthcare benchmarks.
- Whether any pilot data collection or validation of the suffering classification guide has been conducted.
- Full reference list (only partial references visible in extract; truncated at reference 14).
