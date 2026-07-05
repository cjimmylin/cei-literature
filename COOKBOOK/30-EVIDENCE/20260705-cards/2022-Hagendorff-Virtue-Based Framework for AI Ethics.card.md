---
stem: "2022-Hagendorff-Virtue-Based Framework for AI Ethics"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, moral-psychology, ai-lab-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Ethics professors do not act more ethically than non-ethicists (p.4, citing Schwitzgebel 2009)"
  - "Ethical principles have no significant influence on technology developers' decision making (p.4, citing McNamara et al. 2018)"
  - "People rate themselves >50/100 on ethicality even though the true average must be exactly 50 (p.12, citing Epley & Dunning 2000)"
  - "Four basic AI virtues distilled from meta-studies: justice, honesty, responsibility, care (p.5)"
  - "Two second-order AI virtues: prudence and fortitude (p.9)"
---
## 1. Gist
Hagendorff proposes a virtue-ethics complement to the dominant principle-based approach in AI ethics. The central thesis is that principled codes of ethics fail in practice not because the principles are wrong, but because moral psychology shows that explicit ethical knowledge does not reliably translate into ethical behavior. Drawing on "bounded ethicality" research (Bazerman & Tenbrunsel), the paper defines four "basic AI virtues" (justice, honesty, responsibility, care) derived by clustering all recurring principles in AI ethics meta-studies, and two "second-order AI virtues" (prudence and fortitude) that help practitioners overcome bounded ethicality. The paper then enumerates individual and organizational training measures to cultivate these virtues. For values-alignment benchmarking, this paper provides a theoretical grounding for why character-based evaluations of AI practitioners may matter as much as capability-based evaluations of AI systems, and articulates a vocabulary of bounded ethicality pitfalls that benchmark designers should account for.

## 2. Benchmark/eval design features
Not a benchmark paper. The paper's conceptual contribution consists of:
1. A **critique of principlism**: AI ethics codes lack enforcement mechanisms, don't account for moral psychology, and are subject to ethics-washing.
2. A **taxonomy of basic AI virtues** (Table 1): each virtue maps to a cluster of AI ethics principles:
   - Justice → algorithmic fairness, non-discrimination, bias mitigation, inclusion, equality, diversity
   - Honesty → organizational transparency, explainability, open-source, acknowledging errors
   - Responsibility → accountability, liability, legality, accuracy, considering long-term consequences
   - Care → non-maleficence, harm, safety, privacy, beneficence, sustainability, autonomy, solidarity
3. A **taxonomy of bounded ethicality factors** (Table 2):
   - Prudence addresses: system 1 thinking, implicit biases, in-group favoritism, self-serving biases, value-action gaps, moral disengagement
   - Fortitude addresses: situational forces, peer influences, authorities
4. **Individual training measures** (Table 3): knowledge about virtues; knowledge about action strategies; locus of control; public commitment; audits and discussion groups.
5. **Systemic/organizational measures** (Table 4): leader influences; ethical climate and culture; increasing proportion of women; decreasing stress and pressure; openness for critique.

## 3. Task format & example item
n/a — No benchmark tasks or example items. Theory paper.

## 4. Scoring / grading methodology
n/a.

## 5. Dataset construction & provenance
n/a. The framework is derived from three AI ethics meta-studies (Fjeld et al. 2020, Hagendorff 2020, Jobin et al. 2019) that mapped recurring principles across dozens of AI ethics guidelines globally.

## 6. Validity evidence
The virtues are derived by a reductionist clustering approach across three meta-studies. No formal validity testing of the virtue taxonomy is conducted. The author acknowledges that authority for selecting these particular four virtues rests on meta-studies that themselves over-represent Western, economically developed countries.

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- Four basic AI virtues derived by clustering all frequently recurring AI ethics principles (p.5-6)
- Two second-order virtues: prudence (counteracts individual psychological biases) and fortitude (counteracts situational/supra-individual forces) (p.9-10)
- Aristotelian concept of prudence (phronesis) as the guiding intellectual virtue (p.9)
- When asked to rate their own ethicality on 0–100 scale, most people score themselves above 50 even though the true average must be 50 (p.12)
- Ethics training must impart tacit knowledge (social perception, emotion) not just explicit principles, to affect behavior (p.15, citing Haidt 2006)
- Ethics codes are proven to have no significant effect on ethical decision making in organizations; ethical climates do (p.17, citing McNamara et al. 2018)

## 10. Pitfalls & limitations
- The virtue selection is driven by meta-studies dominated by Global North perspectives (Jobin et al. 2019), meaning African and South American values are largely absent.
- Virtue ethics is criticized for focusing on "being" not "doing" — virtuous persons can still perform wrong actions.
- The framework lacks technical implementation details; it cannot substitute for domain-specific guidance on, e.g., fairness metrics or explainability tools.
- Virtue ethics' focus on individual dispositions may be less apt for inspiring systemic legal changes than principle-based approaches.
- Unforeseen harmful AI consequences cannot be attributed solely to individual virtue deficits — multifactorial system dynamics matter.
- The framework could have an elitist effect: once AI practitioners become virtuous, who has moral authority over them?

## 11. Novel ideas worth stealing
1. **Bounded ethicality checklist as a benchmark validity audit.** The bounded ethicality taxonomy (implicit biases, self-serving biases, value-action gaps, moral disengagement, situational forces, peer/authority pressures) is directly applicable as a threats-to-validity checklist for benchmark annotation processes. Annotators and benchmark designers are subject to exactly these forces.
2. **Virtue-principle correspondence table.** Hagendorff's Table 1 maps four virtues to their corresponding AI ethics principles. A similar mapping could be used to check whether a benchmark's construct coverage is exhaustive across all major ethical principles.
3. **Value-action gap as a specific failure mode.** The distinction between stating ethical values and actually acting on them (value-action gap) is an under-measured phenomenon in AI ethics evaluations. Benchmarks could probe both self-reported values and revealed behavioral preferences to surface this gap in AI systems.
4. **Moral disengagement taxonomy.** Bandura's moral disengagement techniques (justification, euphemistic relabeling, denial of responsibility, displacement, dehumanization, distorted consequences) provide a vocabulary for labeling specific failure modes in AI-generated moral reasoning.
5. **Future lock-in as a compliance design technique.** Announcing ethics policies with a time delay increases adoption because it eliminates immediate costs and allows preparation. This insight applies to AI evaluation governance: phased adoption of evaluation standards is more effective than immediate mandates.

## 12. Notable quotes
- "Empirical research shows that having plain knowledge on ethical topics or moral dilemmas is likely to have no measurable influence on decision making. Even ethics professionals, meaning ethics professors and other scholars of ethics, typically do not act more ethically than non-ethicists." (p.4)
- "A lot of ongoing AI basic research or very specific, small AI applications have such weak ethical implications that virtues or ethical values have no relevance at all. But AI applications that involve personal data, that are part of human-computer interaction or that are used on a grand scale clearly have ethical implications that can be addressed by virtue ethics." (p.5)
- "Especially the AI sector is often accused of ethics-washing, hence of talking much about ethics, but not acting accordingly." (p.13)
- "The geographic distribution of origin countries of AI ethics guidelines is rather biased towards economically developed countries. Hence, especially African and South-American countries are not represented in the AI ethics discourse." (p.19)

## 13. UNKNOWN / not in extract
- Whether any organizations have piloted the proposed virtue-training program and measured outcomes.
- The full set of principles from the meta-studies before reduction to four virtues (only top-level clustering is described).
- Empirical evidence that virtue-based ethics training outperforms principle-based ethics training in reducing actual ethical violations in AI development settings.
- The specific number of AI ethics guidelines reviewed in each of the three meta-studies used as source material.
