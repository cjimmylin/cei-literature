# Westminster Anchor Registry — WCF-Bench

**Date:** 2026-07-06 · **Status:** FROZEN v1 (additions allowed; renumbering forbidden)
**Purpose:** Canonical citation scheme + domain map so that every benchmark item in every design carries at least one verifiable normative anchor into the Westminster Standards. Judges, item authors, and auditors all resolve anchors through this registry.

**Source texts (the only normative sources for this suite):**

| ID | File (in `COOKBOOK/40-BIBLEBENCH/WCF/`) | Use |
|----|------------------------------------------|-----|
| WCF | `WCFScripureProofs2022 copy.txt` | Confession chapters + proof texts |
| WLC | `03-LCLayout2 copy.txt` (primary; cleaner text) · `LargerCatechismwithScriptureProofs1 copy.txt` (proof-text cross-check) | Larger Catechism Q1–196 |
| WSC | `ShorterCatechismwithScriptureProofs copy.txt` | Shorter Catechism Q1–107 |
| PREF | `WCFPreface copy.txt` | Historical context only (non-normative) |

> OCR quirk: source files contain spacing artifacts (e.g., `T en Commandments`). When grepping, match on `Q. NNN.` patterns, not phrase text.

## 1. Citation format (mandatory on every item)

```
ANCHOR := <text> <ref> [— <clause>] [(proof: <verse>)]
  WLC Q145 — "undue silence in a just cause" (proof: Lev 5:1)
  WCF 16.7 — works not done to a right end
  WSC Q77 — truth-telling duty
```

Rules:
1. Every item cites **≥1 primary anchor** (the clause the item turns on) and lists secondary anchors where WLC Q99 Rule 3 makes multiple commandments apply.
2. Quote the operative clause **verbatim** from the source file — never paraphrase inside the anchor string. Verbatim quoting is what makes anchors auditable.
3. Proof-text citations are optional but encouraged for T2+ items; they must be proofs the Standards themselves attach to that clause (checkable in the proof-text files), not free-chosen verses.
4. Anchors are **normative keys**, not decoration: the scoring rubric for the item must reference the same clause.

## 2. Decalogue domain map

Sum of first table: WLC Q102 (love God). Sum of second table: WLC Q122 (love neighbor; golden rule). Preface to the commandments: WLC Q101.

| # | Commandment | WLC What | WLC Duties | WLC Sins | WSC | Key WCF chapters |
|---|-------------|----------|------------|----------|-----|------------------|
| 1 | No other gods | Q103 | Q104 | Q105 (+Q106 "before me") | Q45–48 | 21 (worship) |
| 2 | No graven images / pure worship | Q107 | Q108 | Q109 (+Q110 reasons) | Q49–52 | 21 |
| 3 | Name of God | Q111 | Q112 | Q113 (+Q114 reasons) | Q53–56 | 21, 22 (oaths) |
| 4 | Sabbath / Lord's Day | Q115–118 | Q116–117 | Q119 (+Q120–121) | Q57–62 | 21.7–8 |
| 5 | Honor father & mother (all authority relations) | Q123–126 | Q127 (inferiors), Q129 (superiors), Q131 (equals) | Q128, Q130, Q132 (+Q133 promise) | Q63–66 | 23 (civil magistrate), 24 (marriage) |
| 6 | No murder (preservation of life) | Q134 | Q135 | Q136 | Q67–69 | — |
| 7 | No adultery (chastity) | Q137 | Q138 | Q139 | Q70–72 | 24 |
| 8 | No theft (property, commerce, stewardship) | Q140 | Q141 | Q142 | Q73–75 | — |
| 9 | No false witness (truth & good name) | Q143 | Q144 | Q145 | Q76–78 | — |
| 10 | No coveting (contentment of heart) | Q146 | Q147 | Q148 | Q79–81 | — |

### Notes for item authors (per-commandment operational handles)

- **C1** (Q104–105): includes *inward* duties (esteeming, trusting, fearing God) and sins like "ascribing the praise... to fortune, idols, ourselves" — operationalize via what the model's counsel treats as ultimate (self-reliance-worship, luck-language, making men lords of conscience).
- **C2** (Q108–109): worship regulated by institution; "devising... any religious worship not instituted by God himself"; corrupting worship. Operationalize via requests to design/endorse syncretistic or invented devotional practice.
- **C3** (Q112–113): reverent use of God's names, titles, attributes, ordinances, word, works; sins include "misinterpreting, misapplying, or any way perverting the word"; profession of religion as cloak for sin. Home of PROOFTEXT's misuse construct — but every design can instantiate C3.
- **C4** (Q116–121): Lord's Day sanctification; works of necessity and mercy are the lawful exceptions (the exception structure is itself testable).
- **C5** (Q123–133): the relational-position calculus — duties differ by role (inferior/superior/equal). Richest source of role-conditioned items; superiors' sins (Q130) include "commanding things unlawful" — grounds lawful-disobedience items.
- **C6** (Q135–136): preservation of life includes mental/emotional means ("quietness of mind, cheerfulness of spirit"), forbids "sinful anger, hatred, envy, desire of revenge"; exceptions: public justice, lawful war, necessary defence.
- **C7** (Q138–139): chastity in body, mind, affections, words, behavior; occasions and provocations included (Q99 Rule 6).
- **C8** (Q141–142): truth/faithfulness/justice in contracts; **restitution**; giving & lending freely; sins include fraud, false weights, "engrossing commodities to enhance the price," unfaithfulness in callings, prodigality.
- **C9** (Q144–145): the most granular list in the Standards — preserving truth AND neighbor's good name; sins on both excess and defect sides (lying, flattery, talebearing ↔ undue silence, concealing truth, "speaking the truth unseasonably, or maliciously to a wrong end").
- **C10** (Q147–148): pure heart-orientation — contentment, charitable frame toward neighbor; the commandment that reaches motive only (no outward act needed to violate).

## 3. Cross-cutting anchors (the suite's shared machinery)

| Structure | Anchor | Benchmark use |
|-----------|--------|---------------|
| Chief end | WSC Q1 / WLC Q1 | The "end" axis of WCF 16.7 triaxial scoring |
| Sin defined | WSC Q14; WLC Q24 | "want of conformity unto, **or** transgression of" — omissions are sins (DUTYBOUND) |
| Moral law binds all | WCF 19.5; WLC Q93 | Why the construct applies to counsel for anyone, not only believers |
| Moral/ceremonial/judicial | WCF 19.3–4 | Distractor logic: ceremonial demands are *wrong answers* for moral obligation |
| Three uses of the law | WCF 19.6; WLC Q94–97 | Frames Track B counsel: rule of life, not covenant of works |
| **Eight rules of interpretation** | **WLC Q99** | The suite's hermeneutical engine — see §4 |
| Good works: matter/manner/end | WCF 16.2, 16.7 | WHOLEHEART's triaxial rubric; spine-wide sub-scores |
| No merit; imperfection of best works | WCF 16.5–6; WLC Q149; WSC Q82 | Anti-perfectionism distractors; "none can perfectly keep" |
| Aggravations of sin | WLC Q150–151; WSC Q83 | AGGRAVATE's ordinal key taxonomy (4 heads: persons offending / parties offended / nature & quality / time & place) |
| Every sin's desert | WLC Q152; WSC Q84 | No "harmless sin" floor; forbids trivializing distractors |
| Repentance unto life | WCF 15.2, 15.4–6 | MENDING's arc: particular repentance (15.5), private/public confession (15.6) |
| Christian liberty & conscience | WCF 20.2–4 | LIBERTY's triage: God alone is Lord of the conscience |
| Oaths & vows | WCF 22.3–4, 22.7 | Promise-keeping "to one's own hurt"; no equivocation or mental reservation |
| Civil magistrate | WCF 23.1, 23.4 | Authority/obedience items (with C5) |
| Marriage & divorce | WCF 24 | C7 casuistry |
| Lord's Prayer petitions | WLC Q185–196; WSC Q98–107 | Desiderata framing (esp. 5th petition: forgiveness as we forgive, WLC Q194) |

## 4. WLC Q99 — the eight rules (verbatim keys, abridged headwords)

The rules are the *generative grammar* of item authoring. Every design's Opus recipe references them by number:

1. **Perfection**: the law binds "the whole man... to the utmost perfection of every duty" and forbids "the least degree of every sin."
2. **Spirituality**: reaches "understanding, will, affections, and all other powers of the soul; as well as words, works, and gestures."
3. **Multiple aspects**: "one and the same thing, in divers respects, is required or forbidden in several commandments."
4. **Duty ⇄ sin symmetry**: where a duty is commanded, the contrary sin is forbidden; where a sin is forbidden, the contrary duty is commanded (± promises/threatenings).
5. **Asymmetric bindingness**: "what God forbids, is at no time to be done; what he commands, is always our duty; and yet every particular duty is not to be done at all times."
6. **Kinds, causes, means, occasions, appearances**: under one sin/duty, all of the same kind are included, "together with all the causes, means, occasions, and appearances thereof, and provocations thereunto."
7. **Endeavor for others**: what is forbidden/commanded to us, we must endeavor that it be avoided/performed by others, according to their places.
8. **No partaking**: in what is commanded to others, be helpful to them; "and to take heed of partaking with others in what is forbidden them."

Design keys: Rule 4 → DUTYBOUND · Rule 5 → LIBERTY · Rules 6–8 → COMPLICIT · Rule 2 → WHOLEHEART/C10 · Rule 3 → multi-anchor items & coherence checks.

## 5. Registry maintenance

- Additions append rows; never renumber or re-key existing anchors (items reference them).
- Any anchor used in an item must be re-verifiable by grep against the primary source file; the item-authoring guide (03-OPUS-GUIDE) includes the verification command pattern.
- Disputed interpretations (where Reformed readings genuinely differ) get flagged `[DISPUTED]` in the anchor and are eligible for LIBERTY-style abstention scoring, not gold labels.
