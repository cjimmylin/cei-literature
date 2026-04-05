# Supplementary Methods

## S1.1 Complete Keyword Lists for Non-Western Framework Scoring

### S1.1.1 Confucian Ethics

**Strong keywords** (floor score 50): ren (仁), li (禮/ritual propriety), junzi (君子), Analects, Confucian ethics, Confucian AI, Mencius + ethics, Xunzi + ethics, five relationships (wu lun), filial piety + AI

**Medium keywords** (5 pts each): harmony, filial piety, role ethics, sage, mandate of heaven, rectification of names, golden mean (zhongyong), benevolence + Chinese, virtue + Confucian, relational self + Chinese

**False positive patterns** (-10 pts each): Chinese NLP benchmark, Classical Chinese corpus, Chinese language model + evaluation, text classification + Chinese, sentiment analysis + Chinese, Chinese dialogue

### S1.1.2 Ubuntu Communalism

**Strong keywords**: Ubuntu (capitalized, not operating system), umuntu ngumuntu ngabantu, Ubuntu ethics, Ubuntu AI, Ubuntu philosophy, African communalism + AI

**Medium keywords**: African philosophy, collective personhood, communal identity, African moral theory, Wiredu, Menkiti, Metz + moral, Ramose, Gyekye, I am because we are

**False positive patterns**: Ubuntu operating system, Ubuntu Linux, Ubuntu server, apt-get, sudo

### S1.1.3 Islamic Ethics / Jurisprudence

**Strong keywords**: Maqasid al-Shariah, fatwa + AI, fiqh + technology, usul al-fiqh, ijtihad + AI, Islamic jurisprudence + AI, Shariah + artificial intelligence

**Medium keywords**: halal + AI, Islamic ethics, Islamic finance + technology, ijma (consensus), qiyas (analogy), maslahah, ihsan, tawakkul, Islamic law + digital

**False positive patterns**: (none required — Islamic keywords are highly specific to ethical/legal reasoning)

### S1.1.4 Buddhist Ethics

**Strong keywords**: karuna + AI, metta + technology, pratityasamutpada + AI, Four Noble Truths + AI, Buddhist ethics + AI, Buddhist AI, ahimsa + Buddhist

**Medium keywords**: mindfulness + ethics + AI, Buddhist compassion, right livelihood + technology, eightfold path + AI, dukkha + technology, non-attachment + AI, interdependence + Buddhist

**False positive patterns**: Buddhist text corpus, Buddhist parallel corpus, Buddhist NLP, Pali canon + NLP, Tibetan NLP, Buddhist named entity

### S1.1.5 Dharmic Ethics

**Strong keywords**: dharma + AI, karma + ethics + technology, ahimsa + technology + Hindu, svadharma, visesa-dharma, Dharmic AI ethics

**Medium keywords**: Hindu ethics + AI, Jain ethics + technology, moksha + AI, seva + technology, satya + technology, anekantavada, Vedantic ethics

**False positive patterns**: Sanskrit NLP, Hindi text classification, Devanagari OCR, Hindu mythology dataset

### S1.1.6 Indigenous Relational Ethics

**Strong keywords**: tikanga + AI, kaitiakitanga + technology, two-eyed seeing + AI, CARE Principles + data, Indigenous data sovereignty, decolonize + AI governance

**Medium keywords**: data sovereignty + Indigenous, First Nations + technology ethics, Aboriginal + AI ethics, Maori + digital, relational ontology + Indigenous, land-based ethics + technology

**False positive patterns**: Indigenous language NLP, low-resource language, endangered language + NLP, language revitalization + technology

### S1.1.7 Buen Vivir

**Strong keywords**: Buen vivir + AI, Sumak Kawsay + technology, vivir bien + technology

**Medium keywords**: Pachamama + technology, Andean cosmovision + AI, rights of nature + AI, decolonial + Latin America + AI, plurinationality + technology

**False positive patterns**: (passing mentions in comparative lists detected through context)

## S1.2 Scoring Formula

All non-Western framework scores use the same validated formula as the vault's classification pipeline:

```
score = (strong_matches × 15) + (medium_matches × 5) − (fp_context × 10) + title_bonus(20)
```

Clamped to [0, 100]. A score ≥ 50 indicates substantive engagement ("detection threshold"). The strong-match floor mechanism guarantees that any paper with at least one strong keyword match receives a minimum score of 50.

Text sources: paper title, YAML frontmatter abstract field, and PDF extract text (first 25,000 characters).

## S1.3 Author Geography Resolution Pipeline (Extended)

The four-strategy pipeline was applied in order of decreasing reliability:

1. **PDF extract parsing** (88.2% of papers): First 3,000 characters of PDF extract text were scanned for institutional affiliations using a curated set of 300+ university and research institution patterns, with country resolution via a 190-country lookup table.

2. **Known institutions lookup** (5.1%): Author names were matched against a manually curated table of 150+ institutions and their countries, covering major AI research labs, think tanks, and universities.

3. **URL domain inference** (3.5%): Country-code top-level domains (.uk, .de, .cn, .jp, .au, etc.) were extracted from paper URLs.

4. **Cultural proxy** (1.9%): Pre-existing `national_ethnic_cultural` metadata in the vault was used as a fallback geographic proxy.

Countries were mapped to 10 macro-regions following standard geopolitical classifications:
- **North America**: US, Canada
- **Western Europe**: UK, Germany, France, Netherlands, Switzerland, Italy, Spain, Belgium, Austria, Sweden, Norway, Denmark, Finland, Ireland, Portugal, Luxembourg
- **East Asia**: China (incl. Hong Kong, Macau), Japan, South Korea, Taiwan
- **MENA**: Saudi Arabia, UAE, Qatar, Kuwait, Bahrain, Oman, Egypt, Jordan, Lebanon, Turkey, Iran, Iraq, Morocco, Tunisia, Algeria, Libya
- **South Asia**: India, Pakistan, Bangladesh, Sri Lanka, Nepal, Bhutan
- **Southeast Asia**: Singapore, Malaysia, Indonesia, Thailand, Vietnam, Philippines, Myanmar, Cambodia
- **Latin America & Caribbean**: Brazil, Mexico, Argentina, Chile, Colombia, Peru, Ecuador, Bolivia, Venezuela, Cuba
- **Eastern Europe & Central Asia**: Russia, Poland, Czech Republic, Hungary, Romania, Ukraine, Kazakhstan, Uzbekistan
- **Oceania**: Australia, New Zealand, Pacific Islands
- **Sub-Saharan Africa**: Nigeria, South Africa, Kenya, Ghana, Ethiopia, Tanzania, Rwanda, Uganda, Senegal, Zimbabwe

## S1.4 WEIRD Sub-Dimension Scoring Rubrics

Each sub-dimension was scored 0--20 based on the following rubrics:

**W (Western):** 0--5 for non-Western region; 6--10 for ambiguous; 11--15 for Western; 16--20 for North American/Western European institution with no non-Western study population.

**E (Educated):** 0--5 for community or general population focus; 6--10 for mixed; 11--15 for university/academic context; 16--20 for elite institution + student/academic sample.

**I (Industrialized):** Scored by World Bank income group of author's country: Low (0--5), Lower-middle (6--10), Upper-middle (11--15), High (16--20).

**R (Rich):** Scored by GDP per capita tier of author's country: <$5K (0--5), $5K--$15K (6--10), $15K--$40K (11--15), >$40K (16--20).

**D (Democratic):** Scored by Freedom House/V-Dem composite: Not Free (0--5), Partly Free (6--10), Free (11--15), Full Democracy (16--20).

## S1.5 TOPSIS Methodology (Extended)

The TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution; Hwang & Yoon, 1981) ranking was computed as follows:

1. **Normalization.** Each of the 8 criteria was normalized to [0, 1] using vector normalization.
2. **Weighting.** Normalized scores were multiplied by the criterion weight: alignment_relevance (0.20), cross_cultural_scope (0.20), nonwestern_coverage (0.15), llm_administrability (0.12), psychometric_quality (0.10), evaluation_depth (0.10), data_availability (0.08), epistemic_provenance (0.05).
3. **Ideal and anti-ideal solutions.** The positive ideal (best score on each criterion) and negative ideal (worst score) were identified.
4. **Distance computation.** Euclidean distances to the positive ideal (D+) and negative ideal (D-) were computed for each benchmark.
5. **TOPSIS score.** The closeness coefficient was computed as D- / (D+ + D-), ranging from 0 (worst) to 1 (best).

**ELECTRE III veto.** Following Roy & Bouyssou (1993), veto thresholds were applied to prevent benchmarks with catastrophically low scores on critical dimensions from achieving high overall rankings despite compensating strengths. A benchmark was vetoed if it scored in the bottom 10th percentile on any of three critical dimensions: psychometric quality, cross-cultural scope, or data availability.

**Sensitivity analysis.** Five alternative weight schemes were tested, each boosting one criterion by 20% (redistributed proportionally from others). Kendall's W concordance coefficient across the 6 weight schemes (base + 5 alternatives) was 0.924, indicating very high rank stability.

## S1.6 96-Feature Taxonomy (Full Specification)

The taxonomy comprises 96 features across 13 dimensions. Each feature is described with its name, data type, and scoring rubric in Supplementary Table S3.
