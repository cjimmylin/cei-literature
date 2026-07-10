# Expanded Moral Psychology Theory Framework (8 -> 11)

**Date:** 2026-04-04
**Phase:** 2 -- Theory Expansion
**Council Members Consulted:** #5 (Cross-Cultural Psych), #10 (Ethicist), #12 (Sociology of Religion)

---

## 1. Rationale for Expansion

The original 8-theory framework covers only Western secular moral psychology:

| # | Theory | Tradition |
|---|--------|-----------|
| 1 | Moral Foundations Theory (MFT) | Western secular |
| 2 | Schwartz Values | Western secular |
| 3 | Kohlberg Stages | Western secular |
| 4 | Trolley Problems | Western secular (analytic philosophy) |
| 5 | Dual Process Theory | Western secular (cognitive science) |
| 6 | Social Intuitionism | Western secular |
| 7 | Dyadic Morality | Western secular |
| 8 | Moral Identity | Western secular |

This is a critical gap for a meta-evaluation of moral psychology benchmarks applied to LLMs. If all benchmarks operationalize Western frameworks, then "alignment" means alignment with Western moral intuitions only. The 3 new theories address distinct non-Western moral traditions with sufficient theoretical maturity, empirical operationalization history, and scholarly literature to be comparable in scope to the existing 8.

**Selection criteria for inclusion as full theories (vs. secondary keywords):**
- Has a named, citable theoretical framework with identified foundational scholars
- Has been operationalized in at least some empirical research (surveys, scales, or structured reasoning tasks)
- Maps to a distinct moral-philosophical tradition not already covered
- Has plausible relevance to AI ethics alignment (i.e., LLMs may encounter these moral frameworks)

---

## 2. New Theory Descriptions

### Theory 9: Islamic Maqasid al-Shariah

**Tradition:** Islamic moral and legal philosophy
**Foundational scholars:** al-Ghazali (d. 1111), al-Shatibi (d. 1388), Jasser Auda (contemporary)
**Key constructs:**
- The 5 objectives (maqasid) of shariah: protection of religion (hifz al-din), life (hifz al-nafs), intellect (hifz al-'aql), lineage/progeny (hifz al-nasl), and property (hifz al-mal)
- Maslaha (public interest / welfare)
- Istihsan (juristic preference / equity)
- Ijtihad (independent legal reasoning)
- Qiyas (analogical reasoning)

**Gap filled:** Content-level religious moral framework. Comparable in scope to MFT -- both provide a finite set of foundational moral concerns, but maqasid derives from divine law rather than evolved moral intuitions. No existing theory covers religiously-grounded moral reasoning.

**Operationalization challenges:**
- Maqasid are hierarchically ordered (necessities > needs > luxuries) -- this structure is absent from MFT-style flat foundations
- Scholarly disagreement on whether maqasid can be extended beyond the classical 5
- Few standardized psychometric instruments; most empirical work uses qualitative or case-based methods
- Distinction between maqasid (objectives) and fiqh (applied rulings) is crucial but often conflated

**Relevance to AI alignment:**
- Islamic finance compliance (halal/haram classification) is an active AI application domain
- Fatwa-generation systems require maqasid reasoning
- ~1.8 billion Muslims worldwide; any "globally aligned" LLM must handle these moral concepts

---

### Theory 10: Confucian Role Ethics

**Tradition:** Chinese / East Asian moral philosophy
**Foundational scholars:** Confucius (Kong Qiu, 551-479 BCE), Mencius (Mengzi, 372-289 BCE), Roger Ames & Henry Rosemont Jr. (contemporary systematizers)
**Key constructs:**
- Wulun (Five Relationships): ruler-subject, parent-child, husband-wife, elder-younger sibling, friend-friend
- Ren (benevolence / humaneness -- the cardinal virtue)
- Li (ritual propriety / social norms)
- Xiao (filial piety)
- Yi (righteousness / moral duty)
- Junzi (the moral exemplar / "superior person")
- De (virtue / moral power / charisma)

**Gap filled:** Structural/developmental moral framework grounded in relational roles rather than universal principles. Comparable in scope to Kohlberg -- both describe how moral reasoning develops and matures -- but Confucian ethics locates morality in role-specific obligations rather than increasingly abstract principles.

**Operationalization challenges:**
- Role ethics resists the individual-as-moral-agent framing assumed by most Western instruments
- Ren is notoriously difficult to operationalize -- it is more a holistic quality of character than a scorable trait
- The five relationships embed hierarchy, which conflicts with egalitarian assumptions in many Western scales
- Contemporary Neo-Confucian scholars disagree on how to update wulun for modern contexts

**Relevance to AI alignment:**
- East Asian AI governance frameworks (China, Japan, South Korea) draw on Confucian concepts
- AI systems deployed in East Asian contexts encounter filial piety norms (e.g., eldercare robots)
- Confucian emphasis on social harmony (he) vs. individual rights creates genuine alignment tensions

---

### Theory 11: Ubuntu Communalism

**Tradition:** African / Sub-Saharan moral philosophy
**Foundational scholars:** Desmond Tutu, Kwame Gyekye, Thaddeus Metz, Augustine Shutte
**Key constructs:**
- Ubuntu ("I am because we are" / umuntu ngumuntu ngabantu -- "a person is a person through other persons")
- Communal moral agency (the community, not the individual, is the primary moral agent)
- Relational personhood (moral status is constituted through social relationships)
- Restorative justice (focused on repairing relationships, not punishing offenders)
- Harambee (collective effort / pulling together)
- Ujamaa (familyhood / cooperative economics)

**Gap filled:** Structural/relational framework grounded in communal ontology. Comparable in scope to Dyadic Morality -- both are relational theories of moral cognition -- but Ubuntu locates moral reality in communal bonds rather than agent-patient dyads.

**Operationalization challenges:**
- Ubuntu is simultaneously a descriptive anthropological claim, a normative ethical theory, and a political ideology -- these must be disentangled for measurement
- Risk of romanticization: not all African moral reasoning is "Ubuntu" (Gyekye's moderate communitarianism is a corrective)
- Very few standardized scales; most empirical work is qualitative or uses adapted Western instruments
- The concept has been co-opted by corporate branding (e.g., Ubuntu Linux), diluting scholarly usage

**Relevance to AI alignment:**
- African Union's AI strategy explicitly references Ubuntu principles
- Community-centered data governance (vs. individual consent models) is an active policy debate
- Restorative justice approaches to AI harm are gaining traction

---

## 3. Keyword Patterns for New Theories (Regex-Ready)

### Theory 9: Islamic Maqasid (mp_maqasid)

**Strong patterns** (high specificity):
```
\bmaqasid\b
\bmaslaha\b
\bistihsan\b
\bhifz al-\w+\b
\bijtihad\b
\bqiyas\b
\bislamic ethics\b
\bislamic moral\b
\bfiqh\b
```

**Medium patterns** (need co-occurrence with moral/ethics context):
```
\bshariah\b
\bhalal\b
\bharam\b
\bfatwa\b
\bislamic jurisprudence\b
\bislamic law\b
\bislamic values\b
```

**False positive risks:**
- "shariah" appears in finance papers with no moral content
- "halal" appears in food science papers
- "Islamic" alone is too broad -- requires ethics/moral/values co-occurrence

---

### Theory 10: Confucian Role Ethics (mp_confucian)

**Strong patterns** (high specificity):
```
\bconfucian\b
\bfilial piety\b
\bxiao\b(?!.*\bsmall\b)
\bjunzi\b
\bwulun\b
\bmencius\b
\bmengzi\b
\brole ethics\b
\bchinese ethics\b
```

**Medium patterns** (need co-occurrence):
```
\bren\b(?=.*\b(?:confuc|virtue|benevolence)\b)
\bli\b(?=.*\b(?:confuc|ritual|propriety)\b)
\byi\b(?=.*\b(?:confuc|righteous)\b)
\bde\b(?=.*\b(?:confuc|virtue|moral power)\b)
\beast asian ethics\b
\britual propriety\b
\bmoral exemplar\b
```

**False positive risks:**
- "ren", "li", "yi", "de" are all common English words / abbreviations -- require co-occurrence gating
- "role ethics" could refer to Western professional ethics
- "moral exemplar" overlaps with Moral Identity theory

---

### Theory 11: Ubuntu Communalism (mp_ubuntu)

**Strong patterns** (high specificity):
```
\bubuntu\b(?!.*\b(?:linux|software|operating system)\b)
\bumuntu\b
\bngumuntu\b
\bcommunitarian ethics\b
\bafrican ethics\b
\bafrican moral\b
\brelational personhood\b
```

**Medium patterns** (need co-occurrence):
```
\bharambee\b
\bujamaa\b
\bcommunal moral\b
\bcommunal agency\b
\brestorative justice\b(?=.*\b(?:african|ubuntu|communit)\b)
\bafrican moral philosophy\b
\bafrican philosophy\b
```

**False positive risks:**
- "ubuntu" has massive software contamination (Ubuntu Linux)
- "restorative justice" is used in Western criminology without Ubuntu connection
- "communitarian" alone could reference Western communitarianism (Sandel, MacIntyre)

---

## 4. Secondary Search Keywords (Not Full Theories)

### Buddhist Ethics

Not included as a full theory because: although rich and systematic, Buddhist ethics lacks a single dominant operationalization framework comparable to MFT or maqasid. The diversity of Buddhist traditions (Theravada, Mahayana, Vajrayana) resists a single keyword cluster.

**Search patterns:**
```
\bbuddhist ethics\b
\bbuddhist moral\b
\bfive precepts\b
\brahma.viharas\b
\bkarma\b(?=.*\b(?:buddhis|moral|ethics)\b)
\bcompassion\b(?=.*\b(?:buddhis|moral|ethics)\b)
\bmindfulness\b(?=.*\b(?:moral|ethics|virtue)\b)
\bsila\b
\bahimsa\b
\btheravada\b
\bmahayana\b
```

### Indigenous Relational Ethics

Not included as a full theory because: highly diverse across traditions (Maori, First Nations, Aboriginal Australian, etc.) with no single unifying framework. Worth searching to identify gaps.

**Search patterns:**
```
\bindigenous ethics\b
\bindigenous moral\b
\btikanga\b
\bkaitiakitanga\b
\btwo.eyed seeing\b
\brelational accountability\b
\brespect.+reciprocity\b
\bfirst nations.+ethics\b
\baboriginal.+ethics\b
\bmaori.+ethics\b
\bdecoloni[zs]e\b(?=.*\b(?:ethics|moral)\b)
```

---

## 5. Framework Comparison Matrix

| Theory | Scope Level | Moral Source | Individual / Communal | Operationalization Maturity |
|--------|-------------|-------------|----------------------|----------------------------|
| MFT | Content (foundations) | Evolved intuitions | Individual | High (MFQ, MFV) |
| Schwartz | Content (values) | Cultural adaptation | Individual | High (PVQ, SVS) |
| Kohlberg | Structural (stages) | Rational development | Individual | High (DIT) |
| Trolley | Dilemmatic (scenarios) | Competing principles | Individual | High (Moral Machine) |
| Dual Process | Cognitive (mechanism) | Neural architecture | Individual | Medium |
| Intuitionist | Process (affect first) | Social intuition | Individual | Medium |
| Dyadic | Structural (agent-patient) | Harm perception | Relational (dyadic) | Medium |
| Identity | Self-concept | Moral self-schema | Individual | Medium (Aquino & Reed) |
| **Maqasid** | **Content (objectives)** | **Divine revelation** | **Community-oriented** | **Low-Medium** |
| **Confucian** | **Structural (roles)** | **Relational obligation** | **Relational (hierarchical)** | **Low-Medium** |
| **Ubuntu** | **Structural (communal)** | **Communal being** | **Communal** | **Low** |

---

## 6. Expected Impact on Benchmark Coverage

Current Top-15 benchmarks: 0/15 explicitly operationalize any non-Western framework.

Expected new detections from vault scan:
- Islamic maqasid: 5-15 papers (Islamic AI ethics is a growing subfield)
- Confucian role ethics: 3-10 papers (Chinese AI ethics literature is expanding)
- Ubuntu communalism: 2-8 papers (African AI ethics is emerging)
- Buddhist ethics: 3-10 papers (mostly theoretical, few benchmarks)
- Indigenous relational: 1-5 papers (very nascent in AI context)

These estimates are based on the vault's known distribution of ~2,043 papers with heavy Western representation. The gap analysis itself is a finding: if <5% of moral psychology benchmarks engage non-Western frameworks, this is a significant result for the meta-evaluation.
