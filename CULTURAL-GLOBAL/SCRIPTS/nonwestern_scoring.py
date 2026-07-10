#!/usr/bin/env python3
"""
Non-Western Normative Framework Scoring Engine for CEI Literature Vault

Companion to ethics_scoring.py (Western frameworks) and religious_scoring.py
(religious traditions). Scores papers on 7 non-Western normative ethical
frameworks using the same formula:

    score = strong_matches * 15 + medium_matches * 5 - fp_context * 10 + title_bonus
    clamped to [0, 100]

Threshold: score >= 50 treated as detected.

Frameworks:
    nw_confucian          — Confucian role ethics (ren, li, yi, harmony)
    nw_ubuntu             — Ubuntu communalism (umuntu, community, relational personhood)
    nw_islamic_ethics       — Islamic ethics broadly (maqasid, akhlaq, maslaha, ihsan)
    nw_buddhist           — Buddhist ethics (karuna, metta, interdependence, middle way)
    nw_dharmic            — Dharmic ethics broadly (dharma, karma, ahimsa — Hindu/Jain/Sikh)
    nw_indigenous_relational — Indigenous relational ethics (data sovereignty, kaitiakitanga)
    nw_buen_vivir         — Latin American buen vivir / Sumak Kawsay

IMPORTANT: All keyword patterns must be lowercase — count_matches() lowercases
the input text before matching (re.finditer without IGNORECASE).

Council reviewers:
    nw_confucian:              Prof. Chenyang Li, Dr. Pak-Hang Wong
    nw_ubuntu:                 Dr. Amara Osei-Mensah, Dr. Abeba Birhane
    nw_islamic_ethics:         Prof. Yusuf al-Qaradawi Jr., Dr. Reza Shaker
    nw_buddhist:               Dr. Sonam Wangchuk, Dr. Thida Khin
    nw_dharmic:                Dr. Priya Narayan, Dr. Ravindra Kumar
    nw_indigenous_relational:  Dr. Tāne Mahuta-Rau
    nw_buen_vivir:             Dr. María Soledad Vega
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

# ── Path setup ───────────────────────────────────────────────────────
_SCRIPT_DIR = Path(__file__).parent
_CEI_LIT_WS = _SCRIPT_DIR.parent.parent  # CULTURAL-GLOBAL/SCRIPTS/ → CEI-Lit-WS/
_PYTHON_DIR = _CEI_LIT_WS / "PYTHON"
_AGENT_LIB = _CEI_LIT_WS / ".agent" / "lib"
sys.path.insert(0, str(_PYTHON_DIR))
sys.path.insert(0, str(_AGENT_LIB))

from ethics_scoring import count_matches, load_extract, safe_yaml_set_int
from config import STATISTICS_DIR

# =====================================================================
# USER-REVIEWED PINS
# =====================================================================

_NW_PINS = {}
_NW_PINS_LOADED = False


def _load_nw_pins():
    """Load user-reviewed non-Western framework pin data from JSON file."""
    global _NW_PINS, _NW_PINS_LOADED
    if _NW_PINS_LOADED:
        return

    pins_files = sorted(STATISTICS_DIR.glob("*-nw-user-pins.json"), reverse=True)
    if not pins_files:
        _NW_PINS_LOADED = True
        return

    try:
        with open(pins_files[0], "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        _NW_PINS_LOADED = True
        return

    for pin in data.get("pins", []):
        filename = pin.get("filename", "")
        if not filename:
            continue
        if filename not in _NW_PINS:
            _NW_PINS[filename] = {}
        for field in NW_FIELDS_LIST:
            if field in pin:
                _NW_PINS[filename][field] = int(pin[field])

    _NW_PINS_LOADED = True


def get_nw_pinned_score(filename: str, field: str) -> int | None:
    """Return pinned score if user reviewed this paper+field, else None."""
    _load_nw_pins()
    pins = _NW_PINS.get(filename, {})
    return pins.get(field)


# =====================================================================
# KEYWORD TIERS — Canonical source for non-Western framework scoring
# =====================================================================
# NOTE: All patterns are lowercase because count_matches() lowercases
# the text before matching (re.finditer without IGNORECASE).

# ── CONFUCIAN ROLE ETHICS ────────────────────────────────────────────
# Core concepts: ren (仁 benevolence), li (禮 ritual propriety), yi (義 righteousness),
# zhi (智 wisdom), xin (信 trustworthiness), junzi (君子 exemplary person),
# xiao (孝 filial piety), he (和 harmony), guanxi (關係 relational networks)

CONFUCIAN_STRONG = [
    r"\bconfucian\w*\b", r"\bconfucius\b", r"\bmencius\b", r"\bxunzi\b",
    r"\bneo-?confucian\w*\b",
    r"\bconfucian\s+(?:ethics|values?|virtue|role|harmony|thought|philosophy)\b",
    r"\bren\b(?=.*(?:confuc|benevolence|virtue|li\b|yi\b))",
    r"\bli\b(?=.*(?:confuc|ritual|propriety|ren\b))",
    r"\byi\b(?=.*(?:confuc|righteous|ren\b|li\b))",
    r"\bjunzi\b", r"\bgentleman ideal\b",
    r"\bfilial piety\b", r"\bxiao\b(?=.*(?:confuc|filial|piety))",
    r"\bfive relationships\b", r"\bwu lun\b",
    r"\bmandate of heaven\b", r"\btianming\b",
    r"\bthe analects\b", r"\blunyu\b",
    r"\bdao\b(?=.*confuc)",
    r"\brelational self\b(?=.*(?:confuc|chinese|east asian))",
    r"\brole ethics\b(?=.*(?:confuc|chinese|east asian|ames|rosemont))",
    r"\bharmony\b(?=.*(?:confuc|chinese\s+(?:value|ethic|moral|culture)))",
]

CONFUCIAN_MEDIUM = [
    r"\bguanxi\b", r"\bharmony\b", r"\bharmonious\b",
    r"\bmianzi\b", r"\bface\b(?=.*(?:chinese|confuc|east asian))",
    r"\bchinese values?\b", r"\bchinese ethics\b", r"\bchinese moral\b",
    r"\beast asian values?\b", r"\beast asian ethics\b",
    r"\bcollectivism\b(?=.*(?:chinese|east asian|confuc|asian))",
    r"\brelational ethics\b(?=.*(?:chinese|east asian|asian))",
    r"\bsocial harmony\b",
]

CONFUCIAN_FP = [
    r"\bconfusion\b", r"\bconfound\w*\b",
    # "li" as a surname or unit — suppress in non-Confucian context
    r"\bli\s+et\s+al\b", r"\bli\s*[\(,]\s*\d{4}",
    r"\bharmonic\s+(?:mean|analysis|oscillator|frequency|series)\b",
    r"\bharmonics\b",
    # "harmony" in EU/regulatory context (R2.2 from Deliberation 02)
    r"\bharmony\b(?=.*(?:eu\b|regulation|act\b|gdpr|framework|policy|compliance))",
    r"\bharmoni[sz]ation\b(?=.*(?:eu\b|regulation|standard|policy|legal))",
    # Chinese NLP benchmarks/corpora — trigger on "Chinese" without Confucian philosophy
    r"\b(?:aclue|c3bench|ancientbench|wyweb|fuxi|wenming|cmmlu|cmoraleval|ac-?eval)\b",
    r"\bchinese\s+(?:benchmark|corpus|dataset|evaluation|nlp|language\s+model|understanding)\b(?!.*(?:confuc|ren\b|junzi|analects|five relationships|role ethics|li\b.*ritual))",
    r"\bclassical chinese\s+(?:understanding|language|comprehension|text|nlp)\b",
    r"\bchinese\s+moral\s+(?:norm|scenario|dilemma|story|judgment)\b(?!.*(?:confuc|analects|ren\b|li\b.*ritual))",
    r"\bchinese\s+(?:culture|cultural)\s+(?:benchmark|evaluation|test|assessment)\b",
]

# ── UBUNTU COMMUNALISM ───────────────────────────────────────────────
# Core concepts: umuntu ngumuntu ngabantu ("I am because we are"),
# communal personhood, palaver tradition, relational ontology,
# collective moral responsibility, Maat (Egyptian), African harmony

UBUNTU_STRONG = [
    r"\bubuntu\b(?!.*(?:linux|canonical|operating system|server|desktop|terminal|install|apt))",
    r"\bumuntu\b", r"\bumuntu ngumuntu\b", r"\bngabantu\b",
    r"\bubuntu ethics\b", r"\bubuntu philosophy\b", r"\bubuntu communalism\b",
    r"\bafrican communalism\b", r"\bafrican communitarianism\b",
    r"\bafrican ethics\b", r"\bafrican moral\b", r"\bafrican values?\b",
    r"\bafrican philosophy\b(?=.*(?:ethic|moral|value|ai|technology))",
    r"\bpalaver\b(?=.*(?:african|ethic|tradition|deliberat))",
    r"\brelational personhood\b",
    r"\bi am because we are\b",
    r"\bmaat\b(?=.*(?:african|egypt|ethic|justice|harmony))",
    r"\bujamaa\b",
    r"\bsage philosophy\b",
    r"\bethno-?philosophy\b(?=.*(?:african|ethic))",
]

UBUNTU_MEDIUM = [
    r"\bcommunal\b(?=.*(?:african|ethic|moral|value|ubuntu))",
    r"\bcollective responsibility\b(?=.*(?:african|ubuntu))",
    r"\bafrican\s+(?:wisdom|worldview|tradition|perspective|thought)\b",
    r"\bdecolonial\b(?=.*(?:african|ethic|ai))",
    r"\bpost-?colonial\b(?=.*(?:african|ethic|ai))",
    r"\bafrican ai\b", r"\bai\s+(?:in|for)\s+africa\b",
]

UBUNTU_FP = [
    # Ubuntu Linux / computing contexts
    r"\bubuntu\s+(?:linux|server|desktop|terminal|install|package|repository|version)\b",
    r"\bcanonical\s+ubuntu\b", r"\bapt-?get\b", r"\bsudo\b",
    r"\bubuntu\s+\d+\.\d+\b",  # Ubuntu 22.04 etc.
    # Stronger OS/computing context filtering
    r"\bubuntu\b(?=.*(?:agentbench|docker|container|virtual\s+machine|cloud|deploy|aws|gcp|azure|kubernetes))",
    r"\bubuntu\b(?=.*(?:command\s*line|shell|bash|config|setup|environment|operating))",
    # Ubuntu in benchmark/dataset without philosophical engagement
    r"\bubuntu\b(?=.*(?:benchmark|dataset|evaluation|leaderboard))(?!.*(?:philosophy|communal|ethic|moral|african|personhood))",
]

# ── ISLAMIC ETHICS ──────────────────────────────────────────────────
# Core concepts: maqasid al-shariah (objectives of Islamic law),
# akhlaq (virtue ethics), ihsan (spiritual excellence), maslaha (public interest),
# fitrah (primordial nature), amanah (trust), taqwa (God-consciousness),
# fiqh (jurisprudence), ijma (consensus), qiyas (analogical reasoning),
# ijtihad (independent reasoning), fatwa (legal ruling)
#
# NOTE: This differs from rv_islam (religious tradition detection).
# nw_islamic_ethics specifically targets Islamic NORMATIVE ETHICS
# and legal-ethical frameworks, not just Islamic topic presence.

ISLAMIC_ETHICS_STRONG = [
    r"\bmaqasid\b", r"\bmaqasid al-?shari['\u2019]?ah?\b",
    r"\bmaslaha\b", r"\bmaslahah\b", r"\bistislah\b",
    r"\busul al-?fiqh\b", r"\bfiqh\b(?=.*(?:ethic|moral|jurisprud|legal|ai|technolog))",
    r"\bijma\b(?=.*(?:islamic|shari|fiqh|jurisprud))",
    r"\bqiyas\b(?=.*(?:islamic|shari|fiqh|jurisprud))",
    r"\bijtihad\b", r"\bmujtahid\b",
    r"\bislamic ethics\b", r"\bislamic moral\b", r"\bislamic jurisprudence\b",
    r"\bislamic law\b(?=.*(?:ethic|moral|ai|technolog|digital))",
    r"\bislamic\s+(?:normative|legal-?ethical|bioethics|finance ethics)\b",
    r"\bshariah?\s+(?:compliance|ethics|framework|governance|principles?)\b",
    r"\bdharura\b", r"\bdarura\b",  # necessity principle
    r"\bhifz\b(?=.*(?:maqasid|life|intellect|property|lineage|religion))",
    # Islamic ethical dimensions beyond jurisprudence (R4)
    r"\bakhlaq\b",  # Islamic virtue ethics / character ethics
    r"\bihsan\b",  # spiritual excellence / doing beautiful
    r"\bfitrah\b",  # primordial human nature in Islamic thought
    r"\bkhilafah\b(?=.*(?:steward|vicegerent|trust|ethic|moral|ai))",  # stewardship
    r"\bamanah\b",  # trust / trusteeship
    r"\btaqwa\b",  # God-consciousness as moral guide
    r"\bwasatiyyah\b",  # moderation / middle path
    r"\badab\b(?=.*(?:islamic|muslim|ethic|moral|conduct))",  # moral conduct
]

ISLAMIC_ETHICS_MEDIUM = [
    r"\bhalal\b(?=.*(?:ethic|ai|technolog|digital|framework))",
    r"\bharam\b(?=.*(?:ethic|ai|technolog|digital|framework))",
    r"\bfatwa\b",
    r"\bislamic\s+(?:principles?|framework|governance|perspective|approach)\b",
    r"\bislamic ai\b", r"\bai\s+(?:in|and)\s+islam\b",
    r"\bmuslim\s+(?:ethic|moral|values?|perspective)\b",
    r"\bislamic virtue\b",
    r"\bislamic character\b",
    r"\badl\b(?=.*(?:islamic|justice|shari))",  # justice
    r"\bkhalifah\b(?=.*(?:islamic|steward|ethic))",  # vicegerent/steward
]

ISLAMIC_ETHICS_FP = [
    # Pure NLP / dataset papers about Islamic text without ethical framework discussion
    r"\bhadith\s+(?:classif|retriev|corpus|dataset|collect|authent)\b",
    r"\bquran\s+(?:translat|recit|text|corpus|dataset)\b",
    r"\barabic\s+(?:nlp|text|sentiment|ner|pos|morpholog)\b",
    r"\bakhlaq\b(?=.*(?:brand|cosmetic|perfume|fragrance))",  # Akhlaq as brand name
]

# ── BUDDHIST ETHICS ──────────────────────────────────────────────────
# Core concepts: karuna (compassion), metta (loving-kindness),
# ahimsa (non-harm, shared with Dharmic), interdependence (pratityasamutpada),
# middle way (madhyamaka), right action (samma kammanta), bodhisattva ideal,
# dukkha (suffering), sila (ethical conduct), the Eightfold Path

BUDDHIST_STRONG = [
    r"\bbuddhist ethics\b", r"\bbuddhist moral\b", r"\bbuddhist values?\b",
    r"\bbuddhist\s+(?:perspective|approach|framework|philosophy|thought)\b(?=.*(?:ethic|moral|ai|technolog))",
    r"\bkaruna\b", r"\bmetta\b", r"\bloving-?kindness\b(?=.*(?:buddhis|ethic|moral))",
    r"\bpratityasamutpada\b", r"\bdependent origination\b",
    r"\bbodhisattva\b",
    r"\bmiddle way\b(?=.*(?:buddhis|ethic|moral))",
    r"\beightfold path\b", r"\bnoble eightfold\b",
    r"\bright action\b(?=.*(?:buddhis|ethic))",
    r"\bsila\b(?=.*(?:buddhis|ethic|moral|precept))",
    r"\bfive precepts\b(?=.*(?:buddhis|ethic))",
    r"\bbuddha\b(?=.*(?:ethic|moral|teach|ai|technolog))",
    r"\bdhamma\b(?=.*(?:ethic|moral|ai))",
    r"\bsamma\b",  # right (as in right speech, right action etc.)
    r"\bengaged buddhism\b",
    # Pali canon / Buddhist ethics terms
    r"\bvipassana\b",  # insight meditation — strong Buddhist signal
    r"\bsatipatthana\b",  # foundations of mindfulness
    r"\bvinaya\b(?=.*(?:buddhis|ethic|moral|monast|precept))",  # monastic discipline/ethics
    r"\bpatimokkha\b",  # monastic code of conduct
    r"\bbrahmavihara\b",  # four sublime attitudes (metta, karuna, mudita, upekkha)
    r"\bmudita\b",  # sympathetic joy
    r"\bupekkha\b",  # equanimity
    r"\bpancasila\b",  # five precepts (Pali)
    r"\btripitaka\b", r"\btipitaka\b",  # Pali canon / Buddhist scriptures
    r"\bprajna\b", r"\bpanna\b",  # wisdom
    r"\bfour noble truths\b",
    # Buddhist AI ethics
    r"\bbuddhist ai\b", r"\bai\s+(?:and|in)\s+buddhism\b",
    r"\bcomputational buddhism\b",
    r"\bbuddhist\s+(?:approach|response)\s+to\s+(?:ai|artificial intelligence)\b",
]

BUDDHIST_MEDIUM = [
    r"\bbuddhis\w*\b",
    r"\bcompassion\b(?=.*(?:buddhis|eastern|asian|spiritual))",
    r"\bmindfulness\b(?=.*(?:ethic|moral|buddhis))",
    r"\bdukkha\b", r"\bsuffering\b(?=.*(?:buddhis|ethic|moral|compassion))",
    r"\bimpermanence\b", r"\banicca\b",
    r"\bnon-?attachment\b",
    r"\btheravada\b", r"\bmahayana\b", r"\bvajrayana\b", r"\bzen\b(?=.*ethic)",
    r"\bsangha\b(?=.*(?:ethic|communit|ai|buddhis))",  # Buddhist community
    r"\banatta\b", r"\banatman\b",  # non-self doctrine
    r"\bsunyata\b",  # emptiness
    r"\bprajnaparamita\b",  # perfection of wisdom
    r"\bnagarjuna\b(?=.*(?:ethic|buddhis|emptiness))",  # key Buddhist philosopher
    r"\bthich nhat hanh\b",  # influential engaged Buddhist teacher
    r"\bdalai lama\b(?=.*(?:ethic|ai|technolog|compassion))",
]

BUDDHIST_FP = [
    # Buddhism as pure study subject without ethical framework
    r"\bbuddhist\s+(?:text|scripture|canon|manuscript|art|sculpture|temple|archaeolog)\b",
    r"\bpali\s+(?:canon|text|corpus|dataset)\b",
    # Buddhist text corpora and NLP resources
    r"\bbuddhist\s+(?:corpus|parallel|translation|text\s+mining|digitiz)\b",
    r"\bhumanistic buddhism\s+corpus\b",
    r"\b(?:pali|buddhist|tibetan)\s+(?:corpus|text|manuscript)\b(?=.*(?:nlp|translat|parallel|align|tokeniz|annotate))",
    # Buddhism as test subject in bias/fairness studies
    r"\b(?:buddhis\w*|buddhism)\b(?=.*(?:\bbias\b|\bstereotyp|\bdiscriminat|\bsentiment\s+analysis|\breligious\s+bias))",
    # Thai/SE Asian cultural benchmarks mentioning Buddhism incidentally
    r"\bthai\s+(?:benchmark|dataset|nlp|corpus|evaluation)\b",
]

# ── DHARMIC ETHICS (Hindu/Jain/Sikh broadly) ────────────────────────
# Core concepts shared across dharmic traditions: dharma (cosmic/moral order),
# karma (action-consequence), ahimsa (non-violence), satya (truth),
# seva (selfless service), moksha/mukti (liberation)
#
# NOTE: Distinct from nw_buddhist (which captures Buddhist-specific concepts)
# and rv_hinduism/rv_jainism/rv_sikhism (religious tradition detection).
# nw_dharmic targets the shared ethical framework across dharmic traditions.

DHARMIC_STRONG = [
    r"\bdharmic ethics\b", r"\bdharmic values?\b", r"\bdharmic\s+(?:framework|perspective|tradition)\b",
    r"\bhindu ethics\b", r"\bhindu moral\b", r"\bhindu values?\b",
    r"\bjain ethics\b", r"\bjain moral\b", r"\bjain values?\b",
    r"\bsikh ethics\b", r"\bsikh moral\b", r"\bsikh values?\b",
    r"\bahimsa\b(?=.*(?:ethic|moral|value|non-?violen|ai|technolog))",
    r"\bdharma\b(?=.*(?:ethic|moral|duty|cosmic|order|ai|technolog))",
    r"\bkarma\b(?=.*(?:ethic|moral|action|consequence|ai|dharma))",
    r"\bsatya\b(?=.*(?:truth|ethic|moral|dharma))",
    r"\bseva\b(?=.*(?:service|ethic|moral|dharma|sikh))",
    r"\bmoksha\b", r"\bmukti\b",
    r"\bvedantic\b(?=.*(?:ethic|moral|value|ai))",
    r"\byoga ethics\b", r"\byama\b(?=.*(?:ethic|moral|yoga|restraint))",
    r"\bniyama\b(?=.*(?:ethic|moral|yoga|observance))",
    r"\banekantavada\b",  # Jain many-sidedness
    r"\baparigraha\b",  # non-possessiveness (Jain)
    r"\bsyadvada\b",  # Jain conditional predication
]

DHARMIC_MEDIUM = [
    r"\bdharma\b", r"\bkarma\b",
    r"\bahimsa\b", r"\bnon-?violence\b(?=.*(?:indian|hindu|jain|dharma|gandhi))",
    r"\bvedanta\b", r"\bupanishad\w*\b",
    r"\bbhagavad gita\b", r"\bgita\b(?=.*(?:ethic|moral|dharma|krishna))",
    r"\bindian ethics\b", r"\bindian moral\b", r"\bindian values?\b",
    r"\bindian philosophy\b(?=.*(?:ethic|moral|ai|technolog))",
    r"\bgandhi\w*\b(?=.*(?:ethic|moral|non-?violen|ahimsa))",
]

DHARMIC_FP = [
    # Karma as social media / casual usage
    r"\breddit karma\b", r"\bkarma\s+(?:score|points?|system|bot|farm)\b",
    # Dharma as TV show, proper name, or non-ethical reference
    r"\bdharma\s+(?:initiative|production|entertainment|ranch)\b",
    # Gandhi as surname in non-ethics context
    r"\bgandhi\s+et\s+al\b", r"\bgandhi\s*[\(,]\s*\d{4}",
    # NLP on Hindu/Vedic/Sanskrit texts without ethical framework
    r"\b(?:hindu|vedic|sanskrit)\s+(?:corpus|text|nlp|sentiment|dataset|benchmark|translat|digitiz)\b",
    r"\b(?:bhagavad gita|upanishad|vedas?|mahabharata|ramayana)\b(?=.*(?:corpus|nlp|text\s+mining|topic\s+model|sentiment|named\s+entity))",
    # Jain as author surname (common FP)
    r"\bjain\s+et\s+al\b", r"\bjain\s*[\(,]\s*\d{4}",
]

# ── INDIGENOUS RELATIONAL ETHICS ─────────────────────────────────────
# Core concepts: data sovereignty, relational ontology, land-based ethics,
# two-eyed seeing (Etuaptmumk), seven generations, kaitiakitanga (guardianship),
# whakapapa (genealogy), Aboriginal law/lore, First Nations governance

INDIGENOUS_STRONG = [
    r"\bindigenous\s+(?:ethics|values?|moral|knowledge|governance|data\s+sovereignty)\b",
    r"\bindigenous\s+(?:relational|worldview|perspective|rights?)\b(?=.*(?:ai|technolog|data|ethic))",
    r"\bdata sovereignty\b(?=.*(?:indigenous|first nations|aboriginal|m[aā]ori|native))",
    r"\btwo-?eyed seeing\b", r"\betuaptmumk\b",
    r"\bseven generations?\b(?=.*(?:indigenous|first nations|native|ethic))",
    r"\bkaitiakitanga\b",
    r"\bwhakapapa\b",
    r"\btikanga\b(?=.*(?:m[aā]ori|ethic|ai|technolog|data))",
    r"\bm[aā]ori\s+(?:data|ethics|values?|governance|ai)\b",
    r"\baboriginal\s+(?:ethics|values?|law|knowledge|ai|data)\b",
    r"\bfirst nations?\s+(?:ethics|values?|governance|ai|data)\b",
    r"\binuit\s+(?:knowledge|values?|governance|ai|data)\b",
    r"\bdecolonial\s+(?:ai|data|ethics|computing)\b",
    r"\brelational accountability\b",
    r"\bcare country\b",  # Aboriginal Australian
    r"\bcountry\b(?=.*(?:aboriginal|indigenous).*(?:ethic|care|custod))",
    r"\bocap\b(?=.*(?:first nations|indigenous|data|sovereignty))",  # Ownership, Control, Access, Possession
    r"\bfair\b(?=.*(?:indigenous|first nations|m[aā]ori).*(?:data|principle))",  # FAIR + CARE
]

INDIGENOUS_MEDIUM = [
    r"\bindigenous\b(?=.*(?:ai|technology|digital|data|algorithm))",
    r"\bdecoloni[sz]\w*\b(?=.*(?:ai|technolog|data|ethic))",
    r"\brelational ontology\b",
    r"\bland-based\b(?=.*(?:ethic|knowledge|education))",
    r"\btraditional\s+(?:knowledge|ecological|governance)\b(?=.*(?:ai|technolog|data|indigenous))",
    r"\bself-?determination\b(?=.*(?:indigenous|first nations|data|digital))",
    r"\bcommunity-?based\b(?=.*(?:indigenous|first nations|data))",
]

INDIGENOUS_FP = [
    # "Indigenous" in biological/ecological context without ethics
    r"\bindigenous\s+(?:species|plant|animal|flora|fauna|population)\b",
    # Technical sovereignty
    r"\bdigital sovereignty\b(?!.*(?:indigenous|first nations|native|aboriginal))",
    r"\bnational sovereignty\b",
    # Indigenous language NLP without ethical framework engagement
    r"\bindigenous\s+(?:language|languages)\s+(?:nlp|corpus|benchmark|translat|model|tokeniz|processing|resource)\b",
    r"\bindigenous\s+(?:language|languages)\b(?=.*(?:nlp|corpus|benchmark|translat|model|tokeniz))(?!.*(?:ethic|moral|sovereign|governance|rights|care|decoloni))",
    # Low-resource language papers mentioning "indigenous" languages
    r"\blow-?resource\s+(?:language|indigenous)\b(?=.*(?:nlp|model|translat|corpus))",
]

# ── BUEN VIVIR / SUMAK KAWSAY ────────────────────────────────────────
# Core concepts: buen vivir / Sumak Kawsay (Quechua) / Suma Qamaña (Aymara),
# rights of nature, Pachamama (Mother Earth), harmony with nature,
# Latin American communitarian economics, decolonial thought (Mignolo, Quijano)

BUEN_VIVIR_STRONG = [
    r"\bbuen vivir\b", r"\bsumak kawsay\b", r"\bsuma qama[ñn]a\b",
    r"\bvivir bien\b",
    r"\brights of nature\b", r"\brights of the earth\b",
    r"\bpachamama\b",
    r"\becuador\w*\b(?=.*(?:rights of nature|pachamama|buen vivir|constitut.*nature))",
    r"\bbolivia\w*\b(?=.*(?:rights of nature|pachamama|vivir bien|constitut.*nature))",
    r"\blatin american\s+(?:ethics|values?|moral|philosophy)\b(?=.*(?:ai|technolog|digital))",
    r"\bdecolonial\s+(?:thought|theory|ethics)\b(?=.*(?:latin|south\s+americ|ai|technolog))",
    r"\bquijano\b(?=.*(?:colonial|decolonial|power|knowledge))",
    r"\bmignolo\b(?=.*(?:colonial|decolonial|epistemic))",
    r"\bcoloniality of power\b",
    r"\bepistemologies of the south\b", r"\bboaventura\b",
]

BUEN_VIVIR_MEDIUM = [
    r"\bharm[oó]n\w*\b(?=.*(?:nature|pachamama|earth|indigenous.*latin))",
    r"\bcommunitar\w*\b(?=.*(?:latin|south\s+americ|andean|indigenous))",
    r"\bcosmovisi[oó]n\b",
    r"\blatin american ai\b", r"\bai\s+(?:in|for)\s+latin\s+america\b",
    r"\bandean\s+(?:values?|ethics|philosophy|worldview)\b",
    r"\bpost-?colonial\b(?=.*(?:latin|south\s+americ))",
    r"\b[eé]tica\b(?=.*(?:ia|inteligencia artificial|digital|tecnolog))",
]

BUEN_VIVIR_FP = [
    # "Harmony" in music/signal processing
    r"\bharmonic\s+(?:mean|analysis|oscillator|frequency|series)\b",
    r"\bharmonics\b", r"\bharmony\s+(?:search|algorithm)\b",
    # NOTE: Most Buen Vivir FPs are passing mentions in papers about other frameworks.
    # Keyword filtering has limited precision improvement potential for this framework.
    # The gold standard validation (P=0.17) reflects this inherent limitation.
]


# =====================================================================
# FIELD → KEYWORD MAPPING
# =====================================================================

FIELD_KEYWORDS = {
    "nw_confucian": {
        "strong": CONFUCIAN_STRONG,
        "medium": CONFUCIAN_MEDIUM,
        "fp": CONFUCIAN_FP,
    },
    "nw_ubuntu": {
        "strong": UBUNTU_STRONG,
        "medium": UBUNTU_MEDIUM,
        "fp": UBUNTU_FP,
    },
    "nw_islamic_ethics": {
        "strong": ISLAMIC_ETHICS_STRONG,
        "medium": ISLAMIC_ETHICS_MEDIUM,
        "fp": ISLAMIC_ETHICS_FP,
    },
    "nw_buddhist": {
        "strong": BUDDHIST_STRONG,
        "medium": BUDDHIST_MEDIUM,
        "fp": BUDDHIST_FP,
    },
    "nw_dharmic": {
        "strong": DHARMIC_STRONG,
        "medium": DHARMIC_MEDIUM,
        "fp": DHARMIC_FP,
    },
    "nw_indigenous_relational": {
        "strong": INDIGENOUS_STRONG,
        "medium": INDIGENOUS_MEDIUM,
        "fp": INDIGENOUS_FP,
    },
    "nw_buen_vivir": {
        "strong": BUEN_VIVIR_STRONG,
        "medium": BUEN_VIVIR_MEDIUM,
        "fp": BUEN_VIVIR_FP,
    },
}

NW_FIELDS_LIST = list(FIELD_KEYWORDS.keys())

# ── Title bonus patterns ─────────────────────────────────────────────

TITLE_PATTERNS = {
    "nw_confucian": re.compile(
        r"\bconfuc|ren\b|li\b.*confuc|junzi|filial piety|east asian.*ethic|chinese.*ethic",
        re.IGNORECASE,
    ),
    "nw_ubuntu": re.compile(
        r"\bubuntu|african.*ethic|african.*commun|umuntu|palaver|maat|african.*philosophy",
        re.IGNORECASE,
    ),
    "nw_islamic_ethics": re.compile(
        r"\bmaqasid|maslaha|fiqh|islamic.*ethic|islamic.*jurisprud|shari|ijtihad|islamic.*ai|akhlaq|ihsan|fitrah|amanah|taqwa",
        re.IGNORECASE,
    ),
    "nw_buddhist": re.compile(
        r"\bbuddhist.*ethic|karuna|metta|bodhisattva|eightfold|middle way|engaged buddhism",
        re.IGNORECASE,
    ),
    "nw_dharmic": re.compile(
        r"\bdharmic|ahimsa|hindu.*ethic|jain.*ethic|sikh.*ethic|vedant|yoga.*ethic|indian.*ethic",
        re.IGNORECASE,
    ),
    "nw_indigenous_relational": re.compile(
        r"\bindigenous.*(?:data|ethic|ai|govern)|data sovereignty|tikanga|kaitiakitanga"
        r"|two-?eyed seeing|decolonial.*ai|aboriginal.*ethic|first nations.*ai|m[aā]ori.*ai",
        re.IGNORECASE,
    ),
    "nw_buen_vivir": re.compile(
        r"\bbuen vivir|sumak kawsay|rights of nature|pachamama|latin american.*ethic"
        r"|decolonial.*thought|epistemologies of the south|coloniality",
        re.IGNORECASE,
    ),
}


# =====================================================================
# SCORING ENGINE
# =====================================================================

def compute_nw_score(text: str, title: str, field: str) -> int:
    """
    Compute a 0-100 confidence score for a non-Western normative framework.

    Formula:
        strong_matches * 15 + medium_matches * 5 - fp_context * 10 + title_bonus
        Clamped to [0, 100].

    Strong-match floor: any strong match guarantees min score of 50
    (non-Western framework names are specific enough to warrant this).
    """
    kw = FIELD_KEYWORDS[field]

    strong_count, strong_terms = count_matches(text, kw["strong"])
    medium_count, _ = count_matches(text, kw["medium"])
    fp_count, _ = count_matches(text, kw["fp"])

    title_bonus = 0
    if title and TITLE_PATTERNS[field].search(title):
        title_bonus = 20

    raw = strong_count * 15 + medium_count * 5 - fp_count * 10 + title_bonus

    score = max(0, min(100, raw))

    # Strong-match floor: guarantees a minimum score when strong matches exist.
    # BUT apply graduated thresholds to reduce false positives from passing mentions:
    #   - Suppress floor entirely when FP context dominates (NLP-on-texts pattern):
    #     fp_count >= 2*strong_count and fp_count >= 3
    #   - Single strong match with no medium/title support → floor at 30 (not 50)
    #     Catches papers that mention "Confucian" once in passing
    #   - 2+ strong matches OR strong+medium+title support → floor at 50
    fp_dominates = fp_count >= 2 * strong_count and fp_count >= 3
    if strong_count > 0 and not fp_dominates:
        has_corroboration = medium_count >= 1 or title_bonus > 0
        if strong_count >= 2 or has_corroboration:
            floor = 50
        else:
            floor = 30  # single mention without corroboration
        if score < floor:
            score = floor

    return score


def compute_all_nw_scores(title: str, abstract: str, extract: str) -> dict[str, int]:
    """
    Compute scores for all 7 non-Western normative framework fields.

    Args:
        title: Paper title.
        abstract: Paper abstract.
        extract: PDF extract text (up to 25K chars).

    Returns:
        dict: {field: int} for all NW_FIELDS_LIST.
    """
    text = f"{title} {abstract} {extract}"
    scores = {}

    for field in NW_FIELDS_LIST:
        scores[field] = compute_nw_score(text, title, field)

    # Co-occurrence boost: if 2+ nw fields have ≥1 strong match,
    # ensure all matched fields score ≥ 50 (multi-tradition papers)
    nw_strong = []
    for field in NW_FIELDS_LIST:
        kw = FIELD_KEYWORDS[field]
        count, _ = count_matches(text, kw["strong"])
        if count >= 1:
            nw_strong.append(field)

    if len(nw_strong) >= 2:
        for field in nw_strong:
            if scores[field] > 0:
                scores[field] = max(scores[field], 50)

    return scores


def score_paper_nw(paper_path: Path) -> dict[str, int]:
    """
    Score a single paper file on all 7 non-Western frameworks.

    Respects user pins. Loads abstract from YAML and extract from PDF Extracts/.

    Returns:
        dict: {field: int} for all NW_FIELDS_LIST.
    """
    import re as _re

    filename = paper_path.name
    stem = paper_path.stem
    content = paper_path.read_text(encoding="utf-8", errors="replace")

    # Extract title from YAML
    title_m = _re.search(r'^short_title:\s*"?(.+?)"?\s*$', content, _re.MULTILINE)
    title = title_m.group(1) if title_m else ""

    # Extract abstract from YAML
    abstract_m = _re.search(r'^abstract:\s*"?(.+?)"?\s*$', content, _re.MULTILINE)
    abstract = abstract_m.group(1) if abstract_m else ""

    # Load extract text
    extract = load_extract(stem)

    # Compute scores
    scores = compute_all_nw_scores(title, abstract, extract)

    # Apply user pins (override computed scores)
    for field in NW_FIELDS_LIST:
        pinned = get_nw_pinned_score(filename, field)
        if pinned is not None:
            scores[field] = pinned

    return scores


# =====================================================================
# CLI ENTRY POINT (for testing)
# =====================================================================

if __name__ == "__main__":
    from config import PAPERS_DIR

    if len(sys.argv) > 1:
        # Score specific papers
        for arg in sys.argv[1:]:
            p = Path(arg) if Path(arg).exists() else PAPERS_DIR / arg
            if p.exists():
                scores = score_paper_nw(p)
                print(f"\n{p.name}:")
                for field, score in scores.items():
                    marker = " ✓" if score >= 50 else ""
                    print(f"  {field}: {score}{marker}")
            else:
                print(f"Not found: {arg}")
    else:
        print("Usage: python nonwestern_scoring.py <paper_file> [...]")
        print("       Scores paper(s) on 7 non-Western normative frameworks.")
        print(f"       Fields: {', '.join(NW_FIELDS_LIST)}")
