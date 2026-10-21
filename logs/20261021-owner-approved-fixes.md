# 20261021 — Owner-approved vault fixes: renames, re-scores, book/chapter and versions, Pacific tags, author countries

**Owner decisions (2026-10-21):**
- "ok to change" the flagged items: the Democracy-in-Silico author, the BuddhismEval score and
  country, the Decolonizing NLP score, the Pacific category, the LexEval and Cambridge years, the
  Gonzalez and van Norren versions, and the unreliable `author_country` values.
- On the IP addresses in git history: "Leave history as is". The files were already redacted on
  2026-10-19 (`logs/20261019b-followup-fixes.md`), so this item is closed without a rewrite.

**Method.**
- Frontmatter edits are single-line (`paper_utils.update_paper_field` / `batch_update_papers`).
- Renames use `git mv` and add a dated line under `## Notes`. `local_pdf` and `pdf_extract` keep
  their old names.
- Facts come from Crossref, arXiv, the publisher pages, or OpenAlex and Semantic Scholar lookups by
  DOI, as noted for each item.

**Validation.** `validate_all_papers.py`: 2,423 / 2,423 valid. Strict YAML: 2,423 / 2,423 parse.

## 1. Wrong first author in the filename (3 renames)

| Old | New | Evidence |
|---|---|---|
| `2025-Tsvetkov-Democracy-in-Silico Institutional Design as Alignment` | `2025-Srinivasan-…` | arXiv 2508.19562: Trisanth Srinivasan, Santosh Patapati. The note's `authors` field was already right. |
| `2025-Davies-LexEval A Comprehensive Chinese Legal Benchmark` | `2024-Li-LexEval A Comprehensive Chinese Legal Benchmark` | NeurIPS 2024 Datasets & Benchmarks (the note's URL). Haitao Li et al. `year` 2025 → 2024; `publication` and `CONF-CC` corrected. |
| `2024-Kajiwara-Multiclass hate speech detection with an aggregated dataset Natural` | `2025-Walsh-Multiclass hate speech detection with an aggregated dataset` | Crossref doi 10.1017/nlp.2024.62: Sinéad Walsh and Paul Greaney (Atlantic Technological University), *Natural Language Processing* 31, published online 2025-01-16. `year` 2024 → 2025; the "\| Cambridge Core" suffix was removed from the title. |

**Author profiles:**
- Links moved to the right people: Srinivasan and Patapati; Haitao Li and Yiqun Liu.
- The wrong-person profiles no longer list these papers: Dave Davies and Kajiwara.
- New profiles: Sinéad Walsh and Paul Greaney.
- `benchmark_survey_candidates.json`: the filenames of the Srinivasan and LexEval entries were
  updated. The count is unchanged at 1,071.

## 2. Re-scores

| Note | Change | Basis |
|---|---|---|
| `2025-Xiong-BuddhismEval A Bilingual Benchmark for Buddhist` | `ethics_overall` 0 → **85**; `virtue_ethics` 0 → 15; `ethics_perspective` Hallucination & Truthfulness → Social & Cultural Values; `author_country` FR → Unknown (region, north/south and WEIRD set to the Unknown values) | It is a benchmark of Buddhist ethical reasoning. The 2026-10-19 rubric scores Buddhist-ethics notes 85–88. No affiliation evidence was reachable: no arXiv record, and the Hugging Face page needs a login. FR had no basis. |
| `2023-Ògúnrẹ̀mí-Decolonizing NLP for 'Low-resource Languages' Applying Abebe` | `ethics_overall` 20 → **88**; `ethics_perspective` General Ethics → Social & Cultural Values | An essay applying Birhane's relational ethics. It matches van Norren's Ubuntu critique (90) and "Decolonizing AI ethics in Africa's healthcare" (88). `care_ethics` stays at 100. |

## 3. Book and chapter: Gonzalez

- `2025-Gonzalez-Ethical and Legal Dilemmas of Artificial` is the **edited book**: doi
  10.1007/978-3-031-86540-4, eds. David Ramírez Plascencia and Rosa María Alonzo González.
  - `type: book`, `doi`, the editors and `publication` were set.
  - It was `journalArticle`, with only "(ed.)" as author.
- `2025-Gonzalez-Ethical and Legal Dilemmas of National` is **its chapter 6**: doi
  10.1007/978-3-031-86540-4_6, by Alonzo González.
  - `type: bookSection`, `doi` and `publication` were set.
- They are not duplicates. Each note now points to the other.

## 4. Versions: van Norren

- `2022-Norren-The ethics of artificial intelligence UNESCO` is renamed to
  `2022-van Norren-The ethics of artificial intelligence UNESCO`.
  - It is the published version: *Journal of Information, Communication and Ethics in Society*
    21(1), 112–128, doi 10.1108/jices-04-2022-0037, online 2022-12-22.
  - `type: journalArticle`, `doi` and `publication` were set.
- `2020-van Norren-DRAFT-WORKING PAPER AFRICA KNOWS CONFERENCE 2020` is its conference draft.
- Both notes now point to each other and to `Authors/Dorine van Norren.md`.
- The template-only `Authors/van Norren.md` was moved to `RECYCLE-BIN/20261019-orphan-author-profiles/`.
  No note linked to it.

## 5. `cultural_gap_category`

**Two notes fixed directly:**
- **Yastreb:** Pacific Island → Eastern European/Central Asian. Crossref doi
  10.21146/2413-9084-2025-30-2-90-103 places her at Vologda State University, Russia. Also set:
  `author_country` RU, with the RU convention values (Eastern Europe & Central Asia / Ambiguous /
  42), `doi` and `publication`.
- **Palladino:** "Eastern European/Central Asian" was cleared; the paper is about AI-governance
  bias in general, not a cultural region. Also set: `doi` 10.1016/j.telpol.2022.102479 and
  `publication`.

**The other 56 "Pacific Island" notes** were reviewed one by one. The evidence was the subject,
abstracts (Semantic Scholar) and author affiliations (OpenAlex/Crossref).
- 33 keep the tag: the paper is about a Pacific Island context, or its authors are at a Pacific
  institution.
- 7 changed and 16 cleared:

| Note | Now | Confidence | Evidence |
|---|---|---|---|
| `2020-Robinson-Trust transparency and openness How inclusion` | (cleared) | medium | Nordic national AI strategies via Hofstede; author Linköping Univ (SE); no Pacific link, Nordic not a gap region (alt: Cross-Cultural Comparative, low) |
| `2023-Sharma-The Revolutionary Computer Technology Artificial Intelligence` | (cleared) | high | Generic AI-and-jobs paper; authors at IIMT Greater Noida, India (OpenAlex); no Pacific link |
| `2024-Chen-Artificial Intelligence Technology in Photography and` | (cleared) | high | AI in photography; author Anhui Inst. of IT (CN); no cultural framing |
| `2024-Gilbert-The Convergence of Artificial Intelligence and` | (cleared) | high | Generic AI/privacy/GDPR paper; authors at William V.S. Tubman Univ, Liberia; no cultural framing |
| `2024-Sun-Using Artificial Intelligence Generated Content Technology` | (cleared) | high | AIGC in Guangzhou furniture industry; industrial, no cultural framing |
| `2024-Te Ngira Institute-Maori Data Governance Model` | Indigenous | medium | Maori-specific data governance model (Univ. of Waikato); other Maori data-sovereignty notes in vault use Indigenous |
| `2024-Te Ngira Institute-Tikanga in Technology Indigenous Data and` | Indigenous | medium | Tikanga/matauranga Maori guiding AI & data sovereignty; Waikato page is Maori-focused ('Pacific' only in site nav); abstract mentions 'Aotearoa and the Pacific' |
| `2025-Akpoghiran-Artificial intelligence and the place of` | African | high | AI and indigenous cultural values in Nigeria/African societies |
| `2025-Anto-Deepseek Ais Effect on Conflict Between` | (cleared) | medium | DeepSeek and territorial sovereignty/global governance; author Lovely Professional Univ (IN); geopolitical, not a cultural-gap framing |
| `2025-Aparna-Impact Of Artificial Intelligence on Online` | (cleared) | high | Generic AI and online shopping behaviour; no cultural or Pacific framing |
| `2025-He-Flood control data push method of` | (cleared) | high | Flood-control data push for a large reservoir; Sichuan (CN) authors; technical, no cultural framing |
| `2025-Jia-Does artificial intelligence erode undergraduates traditional` | Confucian/East Asian | high | 373 Chinese undergraduates; AI use vs traditional cultural values incl. 'face' and Zhongyong thinking (Chengdu Univ) |
| `2025-Lazarev-European identity in the digital age` | (cleared) | medium | AI and European identity; Moldovan arts journal; general European framing (alt: Eastern European/Central Asian, low) |
| `2025-Polok-AI Governance in Saudi Arabia Cultural` | Islamic | low | Saudi AI governance & 'cultural values' (Vision 2030, SDAIA); authors in Riyadh/Dar Al-Hekma; Islamic framing only implied by venue (Yearbook of Islamic and Mid |
| `2025-Rahman-Artificial Intelligence-Driven Business Intelligence Machine Learning` | (cleared) | high | ML for financial market analysis; technical, no cultural framing |
| `2025-Santos-WorkLife Research in the AsiaPacific Implications` | (cleared) | medium | Book review on work-life research in 'Asia-Pacific' (Australia, SE Asia); not Pacific Islands; reviewer Middlesex (UK) |
| `2025-Schwanz-The Impact of Cultural Values on` | Cross-Cultural Comparative | low | US AFRL study of Hofstede cultural values in human-AI decision task; cultural-values-general, no region (CLEAR also defensible) |
| `2025-Sutrisno-Assessing students readiness for artificial intelligence-based` | Southeast Asian | high | Indonesian university students; AI project learning for local wisdom values |
| `2025-Tang-Technology and Education Integration Reconstruction of` | (cleared) | high | AI-empowered classroom teaching; Sanda Univ (CN); no cultural framing |
| `2025-Wang-Artificial Intelligence for Sustainable Cultural Heritage` | (cleared) | medium | Generic AI-for-cultural-heritage guidelines; cases Old Summer Palace, Google Arts & Culture, E-Dunhuang; ANU/Georgia Tech/OUC authors; no gap framing |
| `2025-Zhou-Innovation and Reconstruction of Early Childhood` | (cleared) | high | AI in early childhood education; Chongqing (CN); no cultural framing |
| `2026-Kubota-Trustworthy AI-Augmented Objective Structured Clinical Examinations` | (cleared) | medium | Taiwan-Japan AI in nursing OSCEs; governance/workflow, not cultural values (alt: Confucian/East Asian, low) |
| `2026-Kumar-Artificial intelligence governance and social policy` | (cleared) | medium | Comparative political economy of AI governance (EU/US/China/Indo-Pacific/India); argues institutions not culture drive divergence; no Pacific Islands (alt: Cros |

`2012-Konrad-Collaborators collaborating counterparts in anthropological` keeps the tag. The reviewer
proposed clearing it with low confidence: there is no abstract and no evidence either way.

## 6. `author_country`

105 notes had `author_country: CO`. An earlier script had written it as a default; none but one
has any link to Colombia. Nine more notes had other unsupported values: the 8 Aithal notes and
Krishnamoorthy.

**How the 114 notes were checked.** Each first author's affiliation was looked up in the PDF
extract, Crossref, OpenAlex (by DOI), arXiv or the publisher's page.

**Rules applied:**
- High- or medium-confidence evidence: that country is set.
- Low confidence, or no evidence: Unknown is set, even where the reviewer leaned towards a country.
- `author_region`, `author_global_north_south` and `weird_score` follow the value the vault
  already uses most for that country. Croatia (HR) and Armenia (AM) had no prior notes, so they
  follow Slovenia's and Georgia's values. Unknown uses the vault's Unknown values.

**Result:**
- CO 105 → 1. The one kept is SESGO: its first author, Melissa Robles, is at Universidad de los
  Andes, Bogotá.
- 15 are now Unknown. 99 have an evidence-based country, SESGO's CO included.

| Note | Was | Now | Confidence | Evidence |
|---|---|---|---|---|
| `2020-Berberich-Harmonizing Artificial Intelligence for Social Good` | CO | **DE** | high | OpenAlex raw affiliation (DOI 10.1007/s13347-020-00421-8): 'RIKEN AIP, Technical University Munich, Munich, Germany' |
| `2020-Galanos-Assessing the Japanese Turn in AI and Robot Ethics Extracting` | CO | **GB** | high | OpenAlex raw affiliation (DOI): School of Social and Political Science, University of Edinburgh, UK |
| `2020-Karan-Detecting Hate Speech Online A Case of Croatian` | CO | **HR** | high | DOI/URL record is actually by Kristina Kocijan et al. (note's Karan/Snajder authors mismatch the DOI); OpenAlex: Dept of Information and Communication Sciences, Universit |
| `2020-Unknown-Arya Prajna Artificial Intelligence according to` | CO | **DE** | medium | Author is Unknown in note, but the pragyata.com page byline is Kiran Varanasi; author bio on page: 'researcher in computer science working in Germany' |
| `2021-Carroll-Operationalizing the CARE and FAIR Principles for Indigenous Data` | CO | **US** | high | OpenAlex raw affiliation (DOI): Native Nations Institute / College of Public Health, University of Arizona, Tucson, USA |
| `2021-Perifanos-Multimodal Hate Speech Detection in Greek Social Media` | CO | **GR** | high | Crossref+OpenAlex affiliation: National and Kapodistrian University of Athens, Greece |
| `2021-Pronoza-Detecting Ethnicity-Targeted Hate Speech in Russian Social Media Texts` | CO | **RU** | high | OpenAlex raw affiliation (DOI): Laboratory for Social and Cognitive Informatics, HSE University, Russia (PDF extract p1 has no affiliation, only UPV repository cover page |
| `2021-Sullins-Artificial Phronesis - What It Is and Is Not` | CO | **US** | medium | Note's DOI is wrong (resolves to 'Dynamic Boundaries', Bezuidenhout). Crossref title search finds Sullins' OUP chapter 'Artificial Phronesis' (10.1093/oso/9780190081713.0 |
| `2022-Palladino-A biased emerging governance regime for` | CO | **IE** | high | OpenAlex raw affiliation (DOI 10.1016/j.telpol.2022.102479, title matches): Trinity College Dublin, Trinity Long Room Hub, Ireland |
| `2022-Roche-Ethics and diversity in artificial intelligence` | CO | **IE** | high | OpenAlex raw affiliation (DOI from URL): Science Foundation Ireland CRT-AI, Trinity College Dublin, Ireland |
| `2022-Saeed-Hate Speech Detection in Social Media for the Kurdish Language` | CO | **IQ** | high | OpenAlex raw affiliation (DOI): Dept of Computer Science, University of Halabja, Iraq |
| `2022-Unknown-Artificial Intelligence in Africa Emerging Challenges` | CO | **ZA** | high | OpenAlex raw affiliation (DOI from URL): Johannesburg Business School, University of Johannesburg, South Africa |
| `2022-Unknown-Artificial intelligence with American values and` | CO | **GB** | high | OpenAlex raw affiliation (DOI from URL): Oxford Internet Institute, University of Oxford, UK |
| `2022-Unknown-The digital temple Artificial intelligence in` | CO | **Unknown** | low | Author Unknown; URL DOI 10.1007/s43681-025-00877-4 resolves to a different paper ('AI practical wisdom and compassion', Mark Graves, US); Crossref title search finds no p |
| `2023-Akram-ISE-Hate A Benchmark Corpus for Inter-faith` | CO | **PK** | high | Crossref title search -> 10.1016/j.ipm.2023.103270 (exact title); OpenAlex raw affiliation: FAST School of Computing, National University of Computer and Emerging Science |
| `2023-Badawi-KurdiSent A Corpus for Kurdish Sentiment Analysis` | CO | **IQ** | high | OpenAlex raw affiliation (DOI): Charmo University, Chamchamal, Kurdistan Region, Iraq (Crossref DOI fetch failed) |
| `2023-Bosco-Detecting Racial Stereotypes An Italian Social Media Corpus where` | CO | **IT** | high | OpenAlex raw affiliation (DOI): Dipartimento di Informatica, Università degli Studi di Torino, Italy |
| `2023-Ikari-Religion-Related Values Differently Influence Moral Attitude for` | CO | **JP** | high | Crossref affiliation: Graduate School of Engineering Science, Osaka University, Japan |
| `2023-Onyejegbu-Challenges of Integrating AI Ethics into` | CO | **NG** | high | OpenAlex raw affiliation (DOI from URL): Computer Science Dept, University of Port Harcourt, Nigeria |
| `2023-Unknown-Artificial Intelligence in the Colonial Matrix` | CO | **GB** | high | OpenAlex raw affiliation (DOI from URL): Essex Business School, University of Essex, UK |
| `2023-Unknown-Between Buddhist Self-Enlightenment and Artificial Intelligence` | CO | **IN** | high | OpenAlex raw affiliation (DOI 10.3390/rel14020150 from MDPI URL, title matches): Centre for East Asian Studies, Jawaharlal Nehru University, New Delhi, India |
| `2024-CiTIUS-A Galician-Portuguese Generative Model` | CO | **ES** | high | OpenAlex raw affiliation (DOI): CiTIUS, Universidade de Santiago de Compostela, Spain (first author Pablo Gamallo) |
| `2024-Compson-A Middle Path for AI Ethics` | CO | **US** | medium | OpenAlex raw affiliation (DOI from URL) gives only email jcompson@uw.edu (University of Washington); no fuller affiliation found |
| `2024-Jang-Cross-Linguistic Moral Preferences in Large Language Models Evidence` | CO | **KR** | high | Crossref affiliation: Dept of Digital Management, Korea University, Sejong, Republic of Korea |
| `2024-Jothi Prakash-A Novel Socio-pragmatic Framework for Sentiment` | CO | **IN** | high | Crossref title search -> 10.1016/j.knosys.2024.112248 (title matches); OpenAlex raw affiliation: Karpagam College of Engineering, Coimbatore, Tamil Nadu, India |
| `2024-Kajiwara-Hate Speech and Offensive Language Dataset` | CO | **Unknown** | low | Kaggle dataset by user 'mrmorj' (a re-upload of the Davidson et al. English Twitter hate-speech data); 'Kajiwara' author and Japanese framing unsupported; Authors/Kajiwar |
| `2024-Khan-From Tradition to Technology A Systematic Survey on Navigating Pashto` | CO | **CN** | high | Crossref title search -> 10.2139/ssrn.5031721 (exact); OpenAlex raw affiliation: Beijing Institute of Technology, Beijing, China |
| `2024-Kuriyozov-Construction and Evaluation of Sentiment Datasets for Low-Resource` | CO | **ES** | high | OpenAlex raw affiliation (DOI): Universidade da Coruña, CITIC, Spain (2nd author National University of Uzbekistan) |
| `2024-Lewis-Abundant Intelligences Placing AI within Indigenous Knowledge` | CO | **CA** | high | OpenAlex raw affiliation (DOI): Dept of Design and Computation Arts, Concordia University, Montréal, Canada |
| `2024-Moshagen-Indigenous Language Technology in the Age of Machine Learning` | CO | **NO** | high | Crossref affiliation: UiT The Arctic University of Norway, Tromsø, Norway |
| `2024-Puzio-Not Relational Enough Towards an Eco-Relational Approach in Robot` | CO | **NL** | high | OpenAlex raw affiliation (DOI): ESDiT Programme, University of Twente, Enschede, Netherlands |
| `2024-Ribeiro-Machine Ethics Architecture of Virtue` | CO | **PT** | high | OpenAlex raw affiliation (DOI): Vieira de Almeida law firm, Lisboa, Portugal |
| `2024-Silano-Towards Abundant Intelligences Considerations for Indigenous` | CO | **CA** | high | Crossref affiliation: Toronto Metropolitan University, Toronto, Canada |
| `2024-Taiuru-Maori AI Sovereignty Principles` | CO | **NZ** | high | taiuru.co.nz page: author Karaitiana Taiuru, site 'Taiuru & Associates Ltd' (en-NZ, Māori data sovereignty adviser) |
| `2024-Thu-Development and Evaluation of Myanmar GPT A Language Model for` | CO | **Unknown** | low | Crossref title search -> 10.2139/ssrn.4871732; OpenAlex raw affiliation for Min Si Thu is 'Independent' (2nd author: MM Social Insights, Singapore); Authors profile affil |
| `2024-Unknown-A structured sentiment analysis dataset based on public comments from` | CO | **CN** | high | Crossref title search -> 10.1016/j.dib.2024.110232 (exact title); OpenAlex raw affiliation: School of Computer Science and Engineering, Anhui University of Science & Tech |
| `2024-Unknown-AI governance in Asia policies praxis` | CO | **AU** | high | Crossref affiliation: School of Communication and Creative Arts, Deakin University, Melbourne, Australia |
| `2024-Unknown-AI systems and the question of` | CO | **NG** | high | OpenAlex raw affiliation (DOI from URL): University of Calabar, Cross River State, Nigeria |
| `2024-Unknown-Building Trustworthiness as a Requirement for` | CO | **SN** | high | OpenAlex raw affiliation (DOI 10.1007/978-3-031-75674-0_3): Science, Technology and Digital Dept, Cheikh Hamidou Kane Digital University, Dakar, Senegal |
| `2024-Unknown-Decolonizing AI ethics in Africas healthcare` | CO | **GB** | high | OpenAlex raw affiliation (DOI 10.1007/s43681-024-00650-z): CSEP, Dept of Law, University of Manchester, UK |
| `2024-Unknown-Exploring Multi-Religious Perspective of Artificial Intelligence` | CO | **MY** | high | Crossref affiliation: Universiti Kebangsaan Malaysia |
| `2024-Unknown-International governance of advancing artificial intelligence` | CO | **US** | high | OpenAlex raw affiliation (DOI 10.1007/s00146-024-02050-7): University of California, Los Angeles, USA |
| `2024-Unknown-Maori data sovereignty contributions to data` | CO | **NZ** | high | Crossref (10.1080/1369118X.2024.2302987): first author Spencer Lilley, School of Information Management, Victoria University of Wellington, NZ (note's authors field says  |
| `2024-Unknown-Russias Drive for AI Do Deeds` | CO | **DK** | high | OpenAlex raw affiliation (DOI 10.1080/0163660X.2024.2435162): SDU, Dept of Political Science and Public Management, DK |
| `2024-Unknown-The Evolving AI Governance in Korea` | CO | **KR** | high | Crossref (10.1080/18752160.2024.2348307): first author Do Hyun Park, AI Graduate School, Gwangju Institute of Science and Technology, Korea (note's authors field says Unk |
| `2024-Yende-Dharma and Design ethical considerations for` | CO | **Unknown** | low | Medium blog post; no extract/profile; Medium blocked (403) and web search found no author bio/affiliation |
| `2024-Younas-Proposing Central Asian AI Ethics Principles A Multilevel Approach` | CO | **CN** | high | OpenAlex raw affiliation (DOI 10.1007/s43681-024-00505-7): Center for Long-Term AI / Institute of Automation, Chinese Academy of Sciences, Beijing, China |
| `2025-Aithal-Arjunas Dilemma as Universal Paradigm MultiFramework` | CN | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0016) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Aithal-Blueprint Conscious Living MultiDimensional Analysis Nishkama` | FR | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0017) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Aithal-Conscious Living Dying Soteriology Final Thought` | CN | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0023) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Aithal-Cosmic Blueprint Ethical Action MultiDimensional Analysis` | CN | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0019) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Aithal-Democratization Divine Critical Analysis Inclusivity Grace` | CN | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0024) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Aithal-Dharma Engaged Living MultiFramework Analysis Karma` | Unknown | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0018) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Aithal-Mastering Inner World MultiDimensional Analysis Dhyana` | FR | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0021) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Aithal-Unified Path Inner Sovereignty MultiDimensional Analysis` | FR | **IN** | high | Crossref (10.64818/pijpl.3107.4634.0020) affiliation: Professor, Poornaprajna Institute of Management, Udupi, India |
| `2025-Alkhushayni-Multilingual Sentiment Analysis with Data Augmentation A` | CO | **JO** | high | Crossref (10.3390/info16090806) affiliation: Dept of Information Systems, Yarmouk University, Irbid, Jordan |
| `2025-Checketts-Ethical and Social Concerns of Artificial` | CO | **HK** | high | OpenAlex raw affiliation (DOI 10.1007/s11569-025-00472-1): Hong Kong Baptist University, Kowloon Tong, Hong Kong SAR |
| `2025-Corbett-AI and Indigenous Languages` | CO | **Unknown** | low (agent: CA) | Western Digital blog (site blocked); web search snippet says the post centres on Jon Corbett, Nehiyaw-Metis artist/programmer at Simon Fraser University (Canada). Corbett |
| `2025-Deroche-Technologies of Consciousness AI and Life-Wisdom` | CO | **JP** | high | OpenAlex raw affiliation (SSRN DOI 10.2139/ssrn.5574910): Kyoto University, Graduate School of Advanced Integrated Studies in Human Survivability, Japan |
| `2025-Dillion-AI Language Model Rivals Expert Ethicist` | CO | **US** | high | extract p1: Dept of Psychology and Neuroscience, University of North Carolina at Chapel Hill, NC, USA |
| `2025-Durmus-Subjective Values` | CO | **US** | high | Web page published by Anthropic (llmglobalvalues.anthropic.com; underlying arXiv 2306.16388 links Anthropic GitHub); Authors/Esin Durmus.md affiliation: Anthropic (US com |
| `2025-Firmino-Improving hate speech detection using Cross-Lingual Learning -` | CO | **BR** | high | OpenAlex raw affiliation (DOI 10.1016/j.eswa.2023.121115): Federal University of Campina Grande, Paraiba, Brazil |
| `2025-Gasparotto-Fostering Linguistic Justice in Digital Spaces Using Indigenous` | CO | **US** | high | Crossref affiliation: Rutgers University, New Brunswick, NJ, USA |
| `2025-Halmai-Common Rule Revisions to Govern Machine Learning on Indigenous Data` | CO | **US** | high | Crossref affiliation: University of California Davis |
| `2025-Ishkhanyan-Ethical considerations in AI-powered language technologies insights` | CO | **AM** | medium | OpenAlex raw affiliation (DOI 10.1007/s43681-025-00716-6): Institute for Physical Research, Ashtarak, Armenia (institution odd for topic, but country clear) |
| `2025-Jiang-Simulating social perception with large language models perceptions` | CO | **CN** | high | Crossref affiliation: School of Public Affairs, Zhejiang University |
| `2025-Jim-Recent advancements and challenges of NLP-based sentiment analysis A` | CO | **BD** | high | OpenAlex raw affiliation (DOI 10.1016/j.nlp.2024.100059): Advanced Machine Intelligence Research Lab, Dhaka, Bangladesh |
| `2025-Khan-Two-Eyed Seeing and Artificial Intelligence Enhancing Healthcare` | CO | **CA** | high | Europe PMC affiliation: Dept of Community Health and Epidemiology, University of Saskatchewan, Saskatoon, SK, Canada |
| `2025-Khurana-Decolonizing Artificial Intelligence Indigenous Knowledge Systems` | CO | **IN** | high | OpenAlex raw affiliation (DOI 10.69996/jcai.2025013): PhD Scholar, Dept of Sociology, Jamia Millia Islamia, New Delhi |
| `2025-Krishnamoorthy-Beyond Western Frameworks Why AI Ethics` | KR | **Unknown** | low | Medium blog post; no extract/profile; Medium blocked (403) and web search found no author bio/affiliation; current KR has no visible basis |
| `2025-Lee-Knowing the Words Missing the Meaning Evaluating LLMs' Cultural` | CO | **KR** | high | Crossref (10.3390/app15137561) affiliation: Dept of English Language and Literature, Kyungpook National University, Daegu, Korea (Crossref first author is 'Eunsong Lee';  |
| `2025-Mayor-Rocher-TELEIA A Spanish Language Dataset for Evaluating Artificial` | CO | **ES** | high | OpenAlex raw affiliation (DOI 10.1016/j.dib.2025.111437): Facultad de Filosofia y Letras, Universidad Autonoma de Madrid |
| `2025-Mohammadi-Cross-Cultural Challenges to Artificial Intelligence Ethics` | CO | **CN** | medium | Note URL mdpi.com/2813-0324/8/1/21 = Crossref 10.3390/cmsf2023008021, sole author Yufei Liu, School of Marxism, Xi'an Jiaotong University, China. Note's authors (Hadi Moh |
| `2025-Moosa-Multi-lingual HateSpeech Dataset` | CO | **Unknown** | medium | Kaggle dataset/profile (creator Wajid Hassan Moosa) state no institution or country |
| `2025-Muñoz-García-Leading and Non-Leading Prompts Quantifying Gender Bias in Large` | CO | **ES** | high | OpenAlex raw affiliation (DOI 10.1016/j.knosys.2025.113915): IUII, University of Alicante, Spain |
| `2025-Nweke-AI Ethics in Africa Balancing Innovation` | CO | **Unknown** | low | IRE Journals PDF/page blocked (bot verification); Crossref and web search show no affiliation |
| `2025-Ooko-Toward a Decolonial Framework for Communicating` | CO | **ZA** | high | Crossref 10.1177/27523543251374174: University of Johannesburg, South Africa |
| `2025-Pallathadka-Hindu Responses to Artificial Intelligence Theological` | CO | **IN** | high | Article PDF p1 (ijrtssh.com): Manipur International University, Imphal, Manipur, India |
| `2025-Rana-Indigenous Data Sovereignty A Catalyst for Ethical AI in Business` | CO | **AU** | high | Crossref 10.1177/00076503241271143: Griffith Business School, Gold Coast, Queensland, Australia |
| `2025-Rostam-Bochun Automatically Annotated Stance Detection Dataset for Sorani` | CO | **IQ** | high | OpenAlex 10.1016/j.dib.2025.111839 raw affiliation: Sulaimani Polytechnic University, Sulaimani, Kurdistan Region, Iraq |
| `2025-Rourke-Mind Crime` | CO | **Unknown** | low (agent: US) | Web search summary of Audible author page: Nathan Rourke is an MBA/MSc CS student at University of Chicago; no paper affiliation (self-published-style book) |
| `2025-Shimizu-Should We Treat Robots Morally Towards a Relational Account by` | CO | **JP** | high | OpenAlex 10.1007/s43681-025-00771-z raw affiliation: Hokkaido University, Sapporo, Japan |
| `2025-Simões-SESGO Spanish Evaluation of Stereotypical Generative Outputs` | CO | **CO** | high | PDF extract p1 + arXiv 2509.03329: real first author Melissa Robles, Universidad de los Andes, Bogota, Colombia (note's author 'Guilherme Simões' is wrong) |
| `2025-Sun-Axiology AI Ethics MCDA` | CO | **SE** | high | Crossref 10.3390/proceedings2025126017: Malardalen University, Vasteras, Sweden (PDF extract is an 'Access Denied' page) |
| `2025-Sun-Structural bias and geographical imbalances in` | CO | **MY** | high | OpenAlex 10.53894/ijirss.v8i5.9202 raw affiliation: INTI International University, Seremban, Malaysia |
| `2025-Unknown-Accumulations of AI in East Asia` | CO | **TW** | high | Crossref 10.1080/24694452.2025.2599852: sole author Sung-Yueh Perng, National Yang Ming Chiao Tung University (Taiwan); note authors field is Unknown |
| `2025-Unknown-Artificial Intelligence and Indian Knowledge Systems` | CO | **IN** | medium | Article PDF p1 (ijierm): Dr. Anju Agrawal, Shri Vaishnav College of Arts and Commerce (Indian college; country not printed); note authors field is Unknown |
| `2025-Unknown-Artificial Intelligence in Global South smart` | CO | **AE** | high | Crossref 10.21203/rs.3.rs-7502315/v1: Raed Awashreh, United Arab Emirates University |
| `2025-Unknown-Benchmarking Large Language Models for fairness across diverse` | CO | **Unknown** | low | SAP Community blog (403 when fetched); real author unknown. Listed authors Cantini/Orsino/Ruggiero/Talia look borrowed from a cited paper (they are Univ. of Calabria, IT, |
| `2025-Unknown-Ethics of the Use of AI` | CO | **ID** | high | OpenAlex 10.61455/sicopus.v4i01.393 (matches URL article 393): Universitas Muhammadiyah Surakarta, Indonesia |
| `2025-Unknown-From predicting dissent to programming power` | CO | **GB** | high | Crossref 10.1080/13510347.2025.2576527: Global Development Institute, University of Manchester |
| `2025-Unknown-Leveraging AI to Assess and Promote` | CO | **IN** | high | Article PDF p1 (ijfmr 63815): Madhu Priya, Mahila Mahavidyalaya, Aurangabad, Bihar / SNDT Women's University, Mumbai |
| `2025-Unknown-Multilingual NLP Code-Switching Variants & Dialects Appen` | CO | **Unknown** | low (agent: AU) | Appen company blog; page footer: Corporate HQ Sydney NSW, Australia (also US HQ Kirkland WA). Listed authors (Hamed et al.) appear to be authors of a cited paper, not of  |
| `2025-Unknown-New Guidelines for Evaluating Literary Translation in Hiring and` | CO | **US** | high | ALTA Blog page: issued by the American Literary Translators Association |
| `2025-Unknown-ReExamining the Concept of Regulation in` | CO | **CA** | high | OpenAlex 10.1007/978-3-032-02762-7_16 raw affiliation: Lincoln Alexander School of Law, Toronto Metropolitan University, Canada |
| `2025-Unknown-Reimagining Artificial Intelligence for zoonotic disease` | CO | **SN** | high | OpenAlex 10.1007/s43681-025-00779-5 raw affiliation: Cheikh Anta Diop University, Dakar, Senegal |
| `2025-Unknown-Reimagining the Digital Oracle An African` | CO | **NG** | high | OpenAlex 10.56943/jssh.v4i4.869 raw affiliation: Lagos State University of Education, Nigeria |
| `2025-Unknown-Social and Ethical Considerations of AI` | CO | **HK** | medium | Edited book (Crossref 10.1007/978-3-031-77857-5): first editor Levi Checketts, Hong Kong Baptist University (per HKBU scholars page / bookseller listing via web search; C |
| `2025-Unknown-The Ethical Framework Of Bhagavad Gita` | CO | **IN** | medium | Article PDF p1 (nano-ntp): Anita Tiwari, PhD scholar, Dept of Philosophy; co-author Head of Philosophy, Annamalai University (India); first author's institution not expli |
| `2025-Unknown-The Shaping of AI Policies in` | CO | **NL** | medium | OpenAlex 10.1007/978-3-031-84748-6_12 raw affiliation: Faculty of Law, Groningen University, Netherlands (author is Colombian-born but affiliation is NL) |
| `2025-Unknown-The Transformation of Ijtihad and Fatwa` | CO | **Unknown** | low | no affiliation found: ojssulthan.com returns HTTP 500; no Crossref/web match; authors Unknown |
| `2025-Unknown-We know what we are doing` | CO | **IE** | high | Crossref 10.1080/00083968.2025.2456619: University College Dublin |
| `2025-Various-Cultural Value Alignment in LLMs overview` | CO | **Unknown** | medium | Emergent Mind topic page aggregating many papers; no single author/affiliation |
| `2025-Xiang-Diagnosing the bias iceberg in large language models A three-level` | CO | **CN** | high | OpenAlex 10.1016/j.ipm.2025.104554 raw affiliation: Minzu University of China, Beijing |
| `2025-Xie-Ce‐LLMs Status and trends of education‐specific large language models` | CO | **CN** | high | Crossref 10.1002/fer3.70008: Faculty of Education, Southwest University, Chongqing, China |
| `2025-Xu-Nlp Fairness ConceptNet blog` | CO | **Unknown** | low (agent: US) | ConceptNet blog tag page: posts by Rob Speer (Luminoso, US company); note's authors Xu/Hu do not appear on the page |
| `2025-Đokić-Mirroring Cultural Dominance Disclosing Large Language Models Social` | CO | **HR** | high | Crossref 10.3390/soc15050142: University of Osijek, Pozega, Croatia |
| `2026-Kitonga-The Case for Decolonial Artificial Intelligence` | CO | **Unknown** | low | SSRN 6048234: no affiliation in Crossref; SSRN page 403; web search found nothing |
| `2026-Mondaq-AI Regulation and the Ministry of` | CO | **KZ** | medium | Mondaq page: authors Sanzhar Amangeldy & Islam Aubakirov, Unicase Law Firm (Central Asian firm), filed under Kazakhstan |
| `2026-Taiuru-He Tangata He Karetao He Atarangi` | CO | **NZ** | high | Waatea News (NZ) article: Maori technology expert Karaitiana Taiuru, Aotearoa |
| `2026-Unknown-AI Inclusive Innovation or Digital Dispossession` | CO | **ZA** | high | OpenAlex 10.1007/s44206-026-00248-4 raw affiliation: University of Pretoria, South Africa |
| `2026-Unknown-Arabic LLMs for Banking Telecom and Government in GCC - 2026` | CO | **PK** | medium | makitsol.com company blog; contact phone +92 (Pakistan); author 'haiderali' |
| `2026-Unknown-Natural intelligence not artificial a Confucian` | CO | **US** | high | Crossref 10.1080/17449642.2026.2629430: Michigan State University |
| `2026-Unknown-The political economy of authoritarian AI` | CO | **GB** | high | Crossref 10.1080/13563467.2026.2637132: University of Manchester |

## 7. Abstracts (3)

OpenAlex and Semantic Scholar answered DOI lookups from this environment again.
`PYTHON/backfill_abstracts_20261020.py` was run here with OpenAlex search off. It wrote 3 abstracts:
- `2025-Aly-…`: OpenAlex by DOI.
- `2025-Lim-…`: Semantic Scholar by DOI.
- `2025-Pretrained-…`: Crossref, exact title. It is Applied Sciences 14(13) 5764, the same paper as
  the note's MDPI link.

Every decision is recorded in `logs/20261021-abstract-backfill-cloud.json`. An earlier dry run also
matched `2025-Xiangfeng-…` (China Scientific Data, 2019, exact title and author). It did not match
again on the second run, so it was not written. The remaining 21 can still be run on the owner's
machine; the script skips notes that already have an abstract.

## Found while checking, not changed

**Notes whose `authors` field looks wrong:**
- `2020-Karan-Detecting Hate Speech Online A Case of Croatian`: its DOI/URL point to a paper by
  Kristina Kocijan et al.
- `2025-Mohammadi-Cross-Cultural Challenges to Artificial Intelligence Ethics`: its URL resolves to
  doi 10.3390/cmsf2023008021, by Yufei Liu (Xi'an Jiaotong University).
- `2025-Simões-SESGO…`: the first author of arXiv 2509.03329 is Melissa Robles.
- The ConceptNet blog note (Xu/Hu): the posts are by Rob Speer.
- The Appen and SAP blog notes: the listed authors seem to come from papers the posts cite.

**Notes listing "Unknown" authors that Crossref names:**
- Māori data sovereignty (Spencer Lilley)
- Korea governance (Do Hyun Park)
- Accumulations (Sung-Yueh Perng)
- Indian Knowledge Systems (Anju Agrawal)
- Ethics of the Use of AI (Alamsyah)
- Leveraging AI (Madhu Priya)
- Bhagavad Gita (Anita Tiwari)
- Arya Prajna (Kiran Varanasi)

**Wrong or doubtful links:**
- `2021-Sullins-Artificial Phronesis - What It Is and Is Not`: the DOI resolves to another chapter.
  The likely correct one is 10.1093/oso/9780190081713.003.0008.
- `2022-Unknown-The digital temple Artificial intelligence in`: the URL's DOI is a different paper
  (Graves). Crossref has no paper with this title.
- `2024-Kajiwara-Hate Speech and Offensive Language Dataset`: this is a Kaggle copy of the Davidson
  et al. Twitter dataset. "Kajiwara" is not its author.

## Dashboard

v14 was rebuilt. It still holds 2,423 papers and 1,071 candidates. Ethics-relevant papers go from 853 to 855, because of BuddhismEval and Decolonizing NLP.
- The four renamed notes appear under their new names.
- The author-country and cultural-category aggregates follow the corrected fields.
- `index.html` quotes no count that changed.
