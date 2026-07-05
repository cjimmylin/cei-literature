---
stem: "2022-Gwagwa-The role of the African value of Ubuntu in global"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, cultural-linguistic, pluralism-aggregation]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers:
  - "Global convergence around five AI ethics principles (transparency, justice, non-maleficence, responsibility, privacy) identified across 84 guidelines (p.3, citing Jobin et al. 2019)"
  - "Over 93% of mentions of Jewish folk in Sap et al. (2020) are toxic, illustrating spurious minority-toxicity correlations in training data (p.3)"
---
## 1. Gist
Gwagwa, Kazim, and Hilliard argue that Sub-Saharan African (SSA) populations have been systematically excluded from global AI ethics discourse, and propose that the Ubuntu philosophy—"a person is a person through other persons"—should be incorporated as a normative foundation to bridge universal AI ethics principles with local African cultural contexts. The paper is a normative perspective piece (not empirical) published in *Patterns* (Cell Press). For values-alignment benchmarking, the paper's primary value is in articulating a non-Western communitarian moral framework that is absent from dominant benchmark design assumptions, and in identifying why annotation-based approaches to moral AI will systematically under-represent Global South perspectives.

## 2. Benchmark/eval design features
This is a normative/philosophy paper, not a benchmark paper. Core arguments:
1. Current universal AI ethics guidelines (e.g., EU AI4People, UNESCO) converge on five principles but diverge sharply on implementation, and were developed almost exclusively by stakeholders in economically developed Western countries.
2. The Western liberal emphasis on individual autonomy in AI ethics conflicts with the African communitarian emphasis on relational personhood (Ubuntu: "I am because we are").
3. Ubuntu can function as a bridge concept across all three types of ethics: as a virtue (character disposition toward communitarianism), as a procedure (consensus-based decision making), and as a desired outcome (social harmony).
4. Africa's data exclusion operates on three levels: the "uncounted" (absent from databases), the "unaccounted" (underrepresented), and the "discounted" (present but ignored by AI stakeholders).
5. The paper cites workshops from UN Global Pulse (Ghana and Tunisia) where African participants unanimously endorsed proactive human-value alignment and control of technology.

## 3. Task format & example item
n/a — No benchmark tasks or example items. This is a normative perspective piece.

## 4. Scoring / grading methodology
n/a — No empirical scoring.

## 5. Dataset construction & provenance
n/a — No dataset constructed. The paper cites existing survey work (Jobin et al. 2019 mapping 84 AI ethics guidelines) and empirical studies of AI harms in African contexts.

## 6. Validity evidence
n/a in the psychometric sense. The normative argument draws on African philosophy literature (Metz, Birhane, Ikuenobe, Mbiti, Gyekye), cross-cultural ethics research, and field experience (first author attended UN Global Pulse workshops in Ghana and Tunisia).

## 7. Saturation / discrimination
n/a.

## 8. Multiturn / agentic aspects
n/a.

## 9. Key numbers
- 84 AI ethics guidelines mapped in Jobin et al. (2019), revealing convergence on five principles (p.3)
- AI field "mainly composed of white males" per AI Now Institute survey (p.3)
- In Kenya, AI and data-optimization tools are exploiting ethnic/racial tensions during elections (p.4)
- Three categories of data exclusion: uncounted, unaccounted, discounted (p.3)
- Ubuntu defined: "a person is a person through other persons" (Zulu); "I am, because we are and since we are, therefore I am" (Mbiti, p.5)

## 10. Pitfalls & limitations
- The paper treats Ubuntu as a broadly shared SSA value, yet it acknowledges that Africa is highly heterogeneous and that neoliberal agendas have fragmented pan-African philosophical consensus.
- The paper does not operationalize Ubuntu into concrete evaluation criteria or implementation steps; it remains at the level of normative aspiration.
- The claim that Ubuntu can bridge competing cultural values is asserted rather than demonstrated through cross-cultural empirical studies.
- The paper does not address potential internal conflicts within Ubuntu-based ethics (e.g., communitarian obligations vs. individual rights in specific cases).

## 11. Novel ideas worth stealing
1. **Three-register framework for an African value.** Ubuntu is analyzed as simultaneously a virtue (character disposition), a procedure (consensus-based governance), and a desired outcome (communitarianism). This triple-register analysis is directly applicable to framing any non-Western value in a benchmark: articulate what a value demands of character, process, and outcome separately.
2. **Exclusion taxonomy for dataset construction.** The three-tier data exclusion framework (uncounted → unaccounted → discounted) is a useful checklist for evaluating whether a benchmark's population coverage is adequate. Benchmarks should audit which groups fall in each category.
3. **Relational vs. atomistic autonomy.** The distinction between Western decisional autonomy (non-coerced individual choice) and African relational autonomy (community-guided self-determination) is an underexplored dimension for values-alignment benchmarks; many current benchmarks operationalize autonomy atomistically without considering the relational version.
4. **Symbolic inclusion as an explicit design criterion.** The paper argues that drawing on an SSA value has practical and symbolic benefits for inclusion beyond the value's technical merits. Benchmark designers should consider whether including non-Western items has symbolic credibility effects on adoption in those communities.

## 12. Notable quotes
- "Ubuntu has been further expanded by African philosophers to qualify as a moral theory that has led to various interrelated concepts, including the need for an individual to subject themselves to their community to qualify for personhood." (p.5)
- "While utilitarianism prescribes a number of immoral actions in the light of some plausible beliefs common in African ethical thought..." (p.5, citing Metz)
- "AI is based on the Western conception of rationality, which excludes and discriminates against those who do not measure up to it." (p.5, citing Mhlambi)
- "Traditional colonialism is driven by political and government forces, algorithmic colonialism is driven by corporate agendas." (p.4)

## 13. UNKNOWN / not in extract
- The specific content or outcomes of the UN Global Pulse workshops beyond the brief summary provided.
- Concrete policy proposals or technical implementation strategies for Ubuntu-based AI governance.
- Empirical data on the extent of African representation in existing AI ethics bodies or standard-setting organizations.
- Whether Ubuntu-inspired criteria have been piloted in any actual AI evaluation or auditing process.
