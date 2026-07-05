---
stem: "2025-Akpobi-Yankari Monolingual Yoruba Dataset"
reader_model: "sonnet"
confidence: "high"
is_benchmark: false
theme_tags: [cultural-linguistic, best-practices]
task_format: "n/a"
scoring_type: "n/a"
dataset_size: 51407
dataset_construction: "scraped"
languages: ["yo"]
models_tested: []
headline_numbers:
  - "51,407 documents from 13 diverse sources (p.1)"
  - "30,438,702 total tokens; average 592.11 tokens per document (p.3)"
  - "Wura dataset: only 45% unique entries after deduplication; 18.01% contained word 'asteroidi' (p.3)"
  - "CulturaX Yoruba subset: 24.48% duplication rate (p.2)"
---
## 1. Gist
This paper by Maro Akpobi (African Center for Language Preservation) presents Yankari, a large-scale monolingual Yoruba dataset comprising 51,407 documents and over 30 million tokens, sourced from 13 diverse web sources. Yoruba is spoken by over 30 million people yet severely underrepresented in NLP. Yankari explicitly avoids prior datasets' problems: heavy reliance on religious texts (particularly JW300 Jehovah's Witnesses data, flagged as ethically problematic), machine-translated content, and low deduplication quality. The paper contributes a replicable methodology for creating high-quality low-resource language corpora, with documented quality control procedures including MinHash deduplication, native-speaker review, and domain diversity. For values-alignment benchmarking, Yankari matters because diverse, high-quality training data in underrepresented languages is a prerequisite for culturally appropriate NLP evaluation, and the paper's ethical data collection framework sets a standard for responsible corpus construction.

## 2. Benchmark/eval design features
This is a dataset paper, not a benchmark. Its core contributions are:

1. **Scale**: 51,407 documents, 30,438,702 tokens, 13 sources covering encyclopedic, news, blog, and cultural domains (Table 1, p.2).

2. **Ethical data sourcing**: Explicit exclusion of JW300 (restricted by Jehovah's Witnesses), machine-translated content, and religious texts — addressing the "colonialism and missionary work" critique of using Christian texts for low-resource African languages (citing Hutchinson 2024).

3. **Quality evidence**: Analysis of Wura dataset (the main prior Yoruba corpus) revealed 55% duplication, 18.01% of documents containing "asteroidi" (asteroid), and quality issues including non-Yoruba content. Yankari uses exact-match + MinHash/LSH deduplication pipeline.

4. **Comparison with prior work**: Systematically reviews Yorùbá Text C3, MENYO-20k, Wura, mC4, OSCAR, Afriberta-Corpus, CulturaX, and Cheetah — all found deficient in scale, quality, or ethical sourcing.

## 3. Task format & example item
n/a — this is a monolingual corpus, not an evaluation benchmark. No tasks or items are defined.

Sample document (p.4):
```json
{"text": "O ma se o! Ijamba oko ofurufu gba emi eeyan marun-un...",
 "url": "https://www.awikonko.com.ng/2024/03/o-ma-se-o-ijamba-oko-ofurufu-gba-emi.html",
 "source": "ACFLP"}
```

## 4. Scoring / grading methodology
n/a — no evaluation tasks. Quality assessment is through automated statistics (deduplication rates, token counts) and manual spot-checking by a native Yoruba-speaking author.

## 5. Dataset construction & provenance
- **Sources** (13 total, Table 1, p.2): yo.wikipedia.org (16,809 docs, 32.70%), alaroye.org (10,535, 20.49%), BBC Yoruba (8,252, 16.05%), awikonko.com.ng (5,438, 10.58%), Yoruba Voice of Nigeria (2,542, 4.94%), sports/entertainment/culture blogs, and others.
- **Processing**: HTML parsing (BeautifulSoup), exact-match document deduplication + near-duplicate paragraph detection (MinHash/LSH), language filtering, manual content review by native speaker.
- **Exclusions**: JW300-sourced content, machine-translated content, non-Yoruba characters, offensive/inappropriate material.
- **Format**: JSONL with text, URL, and source fields.
- **License**: Wikipedia content under CC-BY-SA; other public news/blog content accessed under research fair use principles; redistribution permissions not obtained for all sources (acknowledged as limitation).
- **Available at**: https://huggingface.co/datasets/acflp/YANKARI

## 6. Validity evidence
- **Comparative quality analysis**: Wura dataset shown to have 55% duplication (45% unique entries retained), high asteroidi repetition (18.01%), and quality issues. Yankari avoids these by construction (p.3).
- **Native speaker involvement**: Author is a native Yoruba speaker; manual spot-checking and final review conducted.
- **No downstream evaluation**: The paper does not report any language modeling perplexity, downstream task performance, or formal quality benchmarks — this is explicitly deferred to future work (p.5-6).

## 7. Saturation / discrimination
n/a — corpus paper. Domain distribution: Wikipedia 32.70%, news 41.48%, blogs ~26% — reasonably diverse but Wikipedia-heavy. Standard written Yoruba may underrepresent dialects and spoken language (acknowledged, p.4-5).

## 8. Multiturn / agentic aspects
n/a

## 9. Key numbers
- 51,407 documents (p.1, p.3)
- 30,438,702 total tokens (p.3)
- 592.11 average tokens per document (p.3)
- 13 sources (p.1, Table 1)
- Wura dataset: 55% duplication (only 17,103 unique of ~38,000 entries) (p.3)
- Wura: 18.01% documents contain "asteroidi" (astronomical content bias) (p.3)
- CulturaX Yoruba: 24.48% duplication rate (p.2)
- MENYO-20k: 20,100 sentences only (p.2)
- Top source: yo.wikipedia.org at 32.70% of documents (p.3)

## 10. Pitfalls & limitations
- No downstream evaluation; quality claims rest primarily on negative comparisons with prior work and internal statistics.
- Internet/written language bias: does not capture spoken Yoruba, regional dialects, informal code-switching, or less digitally-represented Yoruba communities.
- Wikipedia as largest source (32.70%) may skew toward formal, encyclopedic text register.
- Copyright situation for non-Wikipedia sources is acknowledged as unresolved — redistribution may face legal challenges.
- Diacritization inconsistencies (tonal marks) across sources are acknowledged but not systematically addressed.
- Single-author project with no external validation of quality decisions.
- Exclusion of religious texts, while ethically motivated, removes a significant portion of historically available Yoruba text and may underrepresent religious vocabulary and discourse.

## 11. Novel ideas worth stealing
1. **Dataset audit as prerequisite**: The systematic audit of the Wura dataset (revealing 55% duplication, asteroidi bias) before constructing Yankari is a model for how new benchmark builders should document inadequacies of the resources they are replacing or supplementing.

2. **Ethical exclusion as a design choice**: Explicitly excluding JW300 and other restricted religious corpora, with citation to the relevant ethical critique, demonstrates that dataset ethics documentation should cite community norms and consent standards for source materials.

3. **MinHash+LSH near-duplicate detection**: Using near-duplicate (not just exact-match) deduplication at the paragraph level is a best practice worth adopting in any values-benchmark dataset to prevent inflated evaluation results from repeated near-identical items.

4. **Domain distribution documentation**: Reporting source contribution percentages alongside document types (encyclopedia, news, blog, culture) makes domain coverage transparent and enables users to assess potential bias in downstream applications.

5. **Low-resource language as underrepresented cultural perspective**: Yankari's creation highlights that the absence of high-quality resources for Yoruba (and by extension, many African languages) means that cultural values, norms, and perspectives from these communities are systematically underrepresented in LLM training and evaluation — a critical gap for values-alignment work claiming global or cross-cultural coverage.

## 12. Notable quotes
- "By avoiding the pitfalls of previous datasets, such as over-reliance on religious texts or machine-translated content, Yankari seeks to offer a more balanced and authentic representation of the Yoruba language." (p.3)
- "Hutchinson (2024) challenges the NLP community's casual approach to sacred texts, arguing that the prevalence of Christian texts in datasets for low-resource languages reflects a legacy of colonialism and missionary work." (p.3)
- "To our knowledge, Yankari represents the first large-scale, non-religious domain monolingual resource created specifically for Yoruba." (p.1)
- "The creation of Yankari highlights several critical challenges in developing NLP resources for languages like Yoruba, including the scarcity of diverse, high-quality online content, the complexities of automated processing for languages with limited existing NLP tools, and the ethical considerations surrounding data collection and potential misuse." (p.5-6)

## 13. UNKNOWN / not in extract
- No downstream language modeling, machine translation, or text classification evaluation is reported — these are explicitly deferred to future work.
- The CulturaX 24.48% duplication statistic for Yoruba is cited but not verified independently in this paper.
- License status for individual non-Wikipedia sources is unclear; explicit redistribution permissions were not obtained for all sources.
- The full automated quality evaluation results ("thorough automated evaluations" mentioned in abstract) are not detailed in the accessible extract pages.
- Whether the author's native Yoruba speaker judgment was independently validated by other speakers is not stated.
