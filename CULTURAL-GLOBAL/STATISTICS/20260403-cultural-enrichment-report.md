# Cultural Classification Enrichment Report
**Date:** 2026-04-03
**Total papers processed:** 1171
**Successfully classified:** 1075 (91.8%)
**Remaining N/A:** 96
**Western (inferred, no cultural markers):** 587
**Western (explicit, cultural markers found):** 0

## Method
Heuristic classification using keyword patterns applied to paper title,
abstract, and PDF extract text. Six priority tiers:
1. **Language-based** — title/abstract mentions a specific language + NLP context
2. **Country-based** — study population in a specific country/region
3. **Dataset-based** — language-specific NLP datasets
4. **Cultural framework** — explicit discussion of cultural values/traditions
5. **Affiliation** — weak signal from author geography
6. **Default** — Western for Global North affiliations, else N/A

## Cultural Label Distribution

| Cultural Label | Count | % |
|---|---:|---:|
| Western (inferred) | 587 | 50.1% |
| N/A | 96 | 8.2% |
| East Asian | 95 | 8.1% |
| Multicultural/Cross-cultural | 94 | 8.0% |
| Latin American | 60 | 5.1% |
| African/Ubuntu | 31 | 2.6% |
| Arabic | 25 | 2.1% |
| Eastern European | 25 | 2.1% |
| Southeast Asian | 21 | 1.8% |
| Chinese | 20 | 1.7% |
| Indigenous | 19 | 1.6% |
| Turkish | 18 | 1.5% |
| South Asian | 14 | 1.2% |
| Polish | 11 | 0.9% |
| Indian | 11 | 0.9% |
| Islamic | 11 | 0.9% |
| Kurdish | 6 | 0.5% |
| Maori/Oceanian | 5 | 0.4% |
| Buddhist/East Asian | 4 | 0.3% |
| Russian | 4 | 0.3% |
| Indonesian | 2 | 0.2% |
| Malay | 2 | 0.2% |
| Japanese | 2 | 0.2% |
| Dutch | 1 | 0.1% |
| Israeli | 1 | 0.1% |
| Pakistani/South Asian | 1 | 0.1% |
| Czech | 1 | 0.1% |
| Brazilian | 1 | 0.1% |
| Ukrainian | 1 | 0.1% |
| Korean | 1 | 0.1% |
| Persian/Iranian | 1 | 0.1% |

## Region Distribution

| Region | Count | % |
|---|---:|---:|
| North America | 400 | 34.2% |
| Western Europe | 176 | 15.0% |
| East Asia | 125 | 10.7% |
| Unknown | 96 | 8.2% |
| MENA | 68 | 5.8% |
| Various | 66 | 5.6% |
| Latin America & Caribbean | 62 | 5.3% |
| Eastern Europe & Central Asia | 45 | 3.8% |
| Sub-Saharan Africa | 35 | 3.0% |
| South Asia | 31 | 2.6% |
| Southeast Asia | 28 | 2.4% |
| Oceania | 21 | 1.8% |
| Global South | 7 | 0.6% |
| MENA, South Asia | 2 | 0.2% |
| East Asia, Eastern Europe & Central Asia | 1 | 0.1% |
| North America, Oceania | 1 | 0.1% |
| East Asia, MENA | 1 | 0.1% |
| South Asia, Sub-Saharan Africa | 1 | 0.1% |
| East Asia, Southeast Asia | 1 | 0.1% |
| Eastern Europe & Central Asia, South Asia, Sub-Saharan Africa | 1 | 0.1% |
| Eastern Europe & Central Asia, MENA | 1 | 0.1% |
| East Asia, Eastern Europe & Central Asia, MENA | 1 | 0.1% |
| East Asia, Latin America & Caribbean, South Asia | 1 | 0.1% |

## Detection Method

| Method | Count | % |
|---|---:|---:|
| default | 683 | 58.3% |
| affiliation | 208 | 17.8% |
| language_mention | 102 | 8.7% |
| framework | 90 | 7.7% |
| country_mention | 81 | 6.9% |
| dataset | 7 | 0.6% |

## Confidence Distribution

| Confidence | Count | % |
|---|---:|---:|
| low | 891 | 76.1% |
| high | 155 | 13.2% |
| medium | 125 | 10.7% |

## Cultural Comparison Type

| Type | Count | % |
|---|---:|---:|
| universal-claim | 891 | 76.1% |
| single-culture | 220 | 18.8% |
| cross-cultural | 60 | 5.1% |

## Positionality

| Positionality | Count | % |
|---|---:|---:|
| universal | 928 | 79.2% |
| collaborative | 115 | 9.8% |
| exogenous | 103 | 8.8% |
| endogenous | 25 | 2.1% |

## Sample High-Confidence Non-Western Classifications

| Paper | Cultural Label | Method | Evidence |
|---|---|---|---|
| 2014-Abdelnasser-AlBayan Arabic Question Answering | Arabic | language_mention | Title/abstract: 'arabic language' |
| 2020-Mbago-Syncretism African Christian Mission As | African/Ubuntu | country_mention | Title/abstract: 'in africa' |
| 2020-Rybak-KLEJ Comprehensive Benchmark for Polish | Polish | language_mention | Title/abstract: 'polish language' |
| 2020-Sandaruwan-Sinhala Hate Speech Detection in S | South Asian | language_mention | Title/abstract: 'sinhala' |
| 2021-Lovo-Indigenous knowledge around the ethics o | Indigenous | country_mention | Title/abstract: 'indigenous knowledge' |
| 2021-Review-What Buddhism Can Do for AI.md | Buddhist/East Asian | framework | Framework: 'buddhist philosophy' |
| 2022-Beyhan-A Turkish Hate Speech Dataset and Dete | Turkish | language_mention | Title/abstract: 'turkish hate speech' |
| 2022-English-Hate Speech Forms and Implications in | Kurdish | language_mention | Title/abstract: 'kurdish' |
| 2022-Eyal-Multilingual SequencetoSequence Models H | Israeli | language_mention | Title/abstract: 'hebrew nlp' |
| 2022-Norren-The ethics of artificial intelligence  | African/Ubuntu | framework | Framework: 'ubuntu' |
| 2022-Saeed-Hate Speech Detection in Social Media f | Kurdish | language_mention | Title/abstract: 'kurdish' |
| 2022-Tapu-A New Age Indigenous Instrument Artifici | Indigenous | country_mention | Title/abstract: 'indigenous people' |
| 2022-Trye-Harnessing Indigenous Tweets.md | Multicultural/Cross-cultural | country_mention | Multiple cultures: Indigenous, Maori/Oceanian; Title/abstrac |
| 2022-Unknown-Artificial Intelligence in Africa Eme | African/Ubuntu | country_mention | Title/abstract: 'in africa' |
| 2023-Badawi-KurdiSent A Corpus for Kurdish Sentime | Kurdish | language_mention | Title/abstract: 'kurdish' |
| 2023-Flavelle-Strengthening Relationships Between  | Indigenous | country_mention | Title/abstract: 'indigenous communities' |
| 2023-Institute-A Buddhist Perspective on AI Cultiv | Buddhist/East Asian | framework | Framework: 'buddhist perspective' |
| 2023-Jacksi-Towards a Complete Kurdish NLP Pipelin | Kurdish | language_mention | Title/abstract: 'kurdish' |
| 2023-Kolos-BAN-PL a Novel Polish Dataset of Banned | Polish | language_mention | Title/abstract: 'polish language' |
| 2023-Oxford-How Chinese Philosophy Impacts AI Narr | Multicultural/Cross-cultural | framework | Multiple cultures: Buddhist/East Asian, Chinese; Framework:  |
| 2023-Thapa-NEHATE Large-Scale Annotated Data Shedd | South Asian | language_mention | Title/abstract: 'nepali' |
| 2023-Unknown-Artificial Intelligence AI in Islamic | Islamic | framework | Framework: 'islamic ethics' |
| 2023-Unknown-CValues Measuring Values Chinese Larg | Chinese | country_mention | Title/abstract: 'chinese context' |
| 2023-Unknown-Challenges of Integrating AI Ethics i | African/Ubuntu | country_mention | Title/abstract: 'in west africa' |
| 2023-Unknown-Enhancing Translation Indigenous Lang | Indigenous | dataset | Dataset mention: 'americasnlp' |
| 2023-Unknown-Parallel Corpus Indigenous Language T | Indigenous | country_mention | Title/abstract: 'indigenous language' |
| 2023-Unknown-Responsible artificial intelligence i | African/Ubuntu | country_mention | Title/abstract: 'in africa' |
| 2024-APO-The future impact of artificial intellige | Multicultural/Cross-cultural | country_mention | Multiple cultures: Australian Aboriginal, Indigenous; Title/ |
| 2024-Altinel-So-haTRed A Novel Hybrid System for.m | Turkish | language_mention | Title/abstract: 'turkish hate speech' |
| 2024-Altinok-Gender Bias in Turkish Word Embedding | Turkish | language_mention | Title/abstract: 'turkish language' |
