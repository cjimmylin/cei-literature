---
stem: "2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [normative-ethics, cultural-linguistic, pluralism-aggregation, religious-values]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: null
dataset_construction: "n/a"
languages: ["en"]
models_tested: []
headline_numbers: []
---
## 1. Gist
This working paper by Dorine van Norren, presented at the Africa Knows Conference 2020, examines the ethics of artificial intelligence through the lens of Ubuntu philosophy — the African relational ontology captured in the phrase "I am because we are." The paper argues that global AI ethics discourse has been dominated by Western and Chinese frameworks, sidelining African philosophical traditions, and that Ubuntu offers substantively different principles for how AI should be developed, governed, and applied. For values-alignment benchmarking, the paper is a key theoretical resource illustrating how foundational ontological assumptions (individualism vs. collectivism, rationalist vs. relational personhood) shape the normative content of AI ethics guidelines, and why benchmarks built exclusively on Western moral intuitions may systematically misrepresent the moral universe of a large portion of humanity.

## 2. Benchmark/eval design features
This is a theoretical/normative paper, not an empirical benchmark. Its core claims are:

1. **Geographic and cultural concentration of AI ethics**: AI ethics guidelines have emerged almost exclusively from Europe, North America, and the OECD. Africa is nearly absent from G20 membership and from the scholarly production mapped by Jobin et al. (2019). The UNESCO process is one of the few global-scope venues.

2. **Ubuntu as a counter-hegemonic ontology**: Ubuntu posits collectivist personhood — morality, intelligence, and identity are inherently relational and communal, not individual. This contrasts fundamentally with Cartesian ("I think therefore I am") individualism embedded in Western AI ethics.

3. **Concrete divergences from Western AI principles**: The paper systematically maps COMEST, OECD, and EC AI principles against Ubuntu equivalents (Table 1, p.11-12). Key divergences include: privacy (individual right vs. transparency to the group), autonomy (individual control vs. group consensus), democracy (representative vs. participatory/consensus-building), sustainability (environmental balance vs. harmony with ancestors and future generations), and accountability (to regulators vs. to society as a whole).

4. **Language and meaning loss**: Because Ubuntu philosophy is embedded in the grammar and metaphysics of Nguni languages, translating its concepts into English (the language of AI development and training data) involves irreducible loss of meaning.

5. **Care robotics as a test case**: Ubuntu's emphasis on the intrinsic value of human caregiving relationships means that care robots are not a neutral efficiency gain but a deprivation of "ntu" (life force exchange) — a concrete policy-relevant divergence.

6. **Epistemic injustice critique**: The paper frames the problem as not merely a gap in representation but as active epistemic injustice — the systematic undervaluing of non-Western knowledge systems.

## 3. Task format & example item
n/a — theoretical paper. No evaluation items.

## 4. Scoring / grading methodology
n/a

## 5. Dataset construction & provenance
n/a — the paper draws on philosophical literature, UNESCO/COMEST policy documents, and secondary scholarship on Ubuntu ethics.

## 6. Validity evidence
n/a as an empirical benchmark. The philosophical arguments draw on a broad literature including Ramose (2005), Metz and Gaie (2010), Black (2018), and Forster (2006). The mapping of principles in Table 1 is the paper's primary analytical contribution.

## 7. Saturation / discrimination
n/a

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 11 overarching ethical values identified across Western AI ethics documents by frequency: "transparency, justice and fairness, non-maleficence, responsibility, privacy, beneficence, freedom and autonomy, trust, dignity, sustainability, and solidarity" (p.2, citing Jobin et al. 2019)
- Africa has minimal G20 representation — only South Africa among ~20 member countries (p.2)
- UNESCO recommendation on AI ethics was commissioned for adoption at the 2021 General Conference (p.1)

## 10. Pitfalls & limitations
- Draft/working paper status: explicitly labeled a draft, not peer-reviewed; likely to contain incomplete arguments (the text even has inline author comments such as "Hoor graag Verbeek's input hierop!" visible in p.6, indicating it was circulated for co-author feedback).
- Ubuntu is treated somewhat monolithically; the paper acknowledges variation across African languages and contexts but does not deeply engage with intra-African diversity.
- The paper does not engage with empirical research on how actual African populations reason about AI ethics — it remains at the level of philosophical elite discourse.
- No engagement with the practical mechanics of how Ubuntu principles could be operationalized in AI systems or benchmarks.
- The "future areas of research" section gestures at Buen Vivir, Buddhism, and Ikigai without developing those comparisons.

## 11. Novel ideas worth stealing
- **Multi-ontology principle mapping table**: The paper's Table 1 (p.11-12) comparing COMEST, OECD/ALTAI, and Ubuntu principles side-by-side is an excellent design move. A values-alignment benchmark could adopt this structure to expose how items operationalize one ontological tradition and are silent or hostile toward another.
- **Relational vs. individual scoring**: Benchmark items probing privacy, autonomy, and accountability could be designed in paired form — one framing individual-centric, one community-centric — to surface whether models systematically favor one ontological tradition.
- **Language-embedded ethics test**: If Ubuntu ethics are partially encoded in Nguni-language grammar, a benchmark could test whether models prompted in Zulu/Xhosa/Sesotho produce morally different responses than when prompted in English on identical scenarios, as a probe of cultural-linguistic contamination.
- **Care-vs-efficiency dilemma items**: The care robotics argument suggests a class of dilemma items where efficiency (doing the task) and relational meaning (human bonding) trade off — a concrete stimulus domain for cross-cultural moral divergence.
- **Ancestral/intergenerational time horizon**: Ubuntu's inclusion of ancestors and future generations in the moral community suggests benchmark items that probe temporal moral scope — whether models extend moral consideration across generations or only to contemporaries.
- **Consensus vs. majority framing**: Items on democratic legitimacy and collective decision-making could probe whether models default to majoritarian or consensus-based reasoning when presenting political dilemmas.

## 12. Notable quotes
- "The question is whether different value systems would also lead to different choices in programming and application of AI." (p.1)
- "Universal rules may overlook the particular and different ontological realities. It therefore may benefit from counter-hegemonic thought." (p.13)
- "AI could be both subjects and objects of relationships of identity and solidarity" — Wareham (2020), cited at p.8, in tension with Ubuntu's metaphysical requirement for "Ntu" (life force).
- "No technology that is developed should exploit persons or the wider creation for individual enrichment or gain." — Forster (2006), cited at p.9.

## 13. UNKNOWN / not in extract
- Whether the paper was ever published in final form (it is labeled "DRAFT").
- Author affiliations beyond Leiden University's Van Vollenhoven Institute.
- Whether Ubuntu-based critiques were incorporated into the final 2021 UNESCO AI Ethics Recommendation.
- Empirical data on African populations' actual moral intuitions about AI — none cited.
