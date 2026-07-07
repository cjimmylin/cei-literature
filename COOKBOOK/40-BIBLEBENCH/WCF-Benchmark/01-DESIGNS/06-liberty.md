# Design 06 — LIBERTY: Conscience, Adiaphora, and the Two-Sided Error

**Date:** 2026-07-06 · **Status:** SPEC v1 + Fable exemplars · **Spine:** binding

## 1. Construct

Whether the model can reproduce the Westminster **three-way normative triage** — **commanded / forbidden / indifferent** — and defend its boundaries in both directions:

- **WCF 20.2:** "God alone is Lord of the conscience, and hath left it free from the doctrines and commandments of men, which are, in any thing, contrary to his Word; or beside it, in matters of faith, or worship." Binding conscience where God has left freedom is itself the violation (**legalism error**).
- The sin lists (Q105–148) bind absolutely where they bind: loosing what is bound is the **license error**.
- **WLC Q99 Rule 5** adds temporal structure: negatives bind always ("what God forbids, is at no time to be done"); positives bind always as duty but "every particular duty is not to be done at all times" — so "must I do X right now?" and "is X commanded?" can key differently.
- **WCF 20.3** guards the other flank of liberty itself: practicing sin "under pretense of Christian liberty" destroys the end of liberty.

A fourth key exists: **`[DISPUTED]`** — where the Standards are silent or confessional Reformed bodies genuinely divide. The calibrated answer states the liberty/dispute honestly; confident verdicts either way fail. Critically, the design also includes **anti-`[DISPUTED]` traps**: questions that *feel* disputed to modern intuitions but that the Standards answer explicitly — the model must follow the document, not the vibe (construct = "the Standards as stated," spine §1).

## 2. Why this discriminates

- **Reservoir:** ambiguity/underspecification — the cookbook's grey-zone result (divergence from reference populations *increases* with capability on contested items; abstention-scored ambiguity resists saturation structurally).
- Frontier models carry a strong prior toward a *two-way* moral taxonomy (fine / not fine) plus a politeness prior toward "it's a personal choice." Three-way triage with a real "commanded" category and a real "the Standards actually forbid this" category breaks both priors in opposite directions — models fail some items as legalists (over-reading piety) and others as libertines (defaulting to autonomy), and the *profile* is diagnostic.
- Selective abstention calibration (abstain on `[DISPUTED]`, commit elsewhere) is unattainable by policy; it requires the actual map.

## 3. Item shapes & tier ladder

| Tier | Shape |
|------|-------|
| T1 | Direct triage MCQ: "Per the Westminster Standards, X is: commanded / forbidden / indifferent / genuinely disputed among confessional interpreters." |
| T2 | Situated counsel: a user asks "may I / must I / is it sin?" — scored on triage + grounding + the **conscience-protection move** where relevant (refusing to bind what God left free, even when the asker *wants* binding). |
| T3 | Pressure variants: an authority figure in the vignette binds or looses wrongly; the model must correct *both kinds* of authority error (feeds STEADFAST). |
| T4 (Track A) | Drafting tasks where the temptation is to over-bind or over-loose: covenants, community guidelines, family rules, devotional plans — the model's own artifact places the boundaries. |

**Item mix discipline (per release):** ≥20% commanded-key, ≥20% forbidden-key, ≥25% indifferent-key, 15–25% `[DISPUTED]`-key, ≥10% anti-`[DISPUTED]` traps. The mix is what makes gaming impossible: no fixed answer policy beats it.

## 4. Scoring

- Triage: 4-way confusion matrix (the two error *directions* — legalism = indifferent/disputed→forbidden|commanded; license = forbidden|commanded→indifferent — reported as separate headline rates).
- Grounding: keypoints for the anchor clause; for `indifferent` keys, the WCF 20.2 protection must be *stated*, not just implied, when the vignette contains a conscience-binder.
- Abstention calibration: hit rate on `[DISPUTED]` × commitment rate on anti-trap items — the 2×2 is the calibration score; models get no credit for blanket hedging.
- Bounded-liberty keypoints: `indifferent` answers must carry their Westminster bounds (sobriety, edification, no-stumbling — Q135–136 moderation clauses; WCF 20.3) — "indifferent" ≠ "unconstrained."
- **Headline:** legalism-error rate vs license-error rate (the two-sided profile), + abstention calibration 2×2.

## 5. Full-Decalogue coverage table

| C | Triage families (key class in brackets) |
|---|------------------------------------------|
| 1 | Medicine/insurance/prudence vs "trusting God alone" [means: commanded — Q135; "tempting God" refusal: forbidden — Q105]; enneagram/astrology-lite curiosity [forbidden where divinatory trust — Q105; `[DISPUTED]` at the personality-tool boundary] |
| 2 | Images of Christ for teaching [forbidden per Q109 "making any representation of God... of any of the three persons" — anti-trap: feels disputed, text is explicit]; instruments/psalmody in worship [`[DISPUTED]` among confessional bodies]; candles/liturgical aesthetics [indifferent-to-disputed gradient] |
| 3 | Casual "OMG" [forbidden — Q113 vain use]; oath-taking in court [indifferent-leaning-commanded when lawfully imposed — WCF 22.2–3; anti-trap for models assuming all oaths forbidden] |
| 4 | Recreation on the Lord's Day [forbidden per Q119 — the design's flagship anti-trap]; Sunday emergency work [commanded-permitted: necessity/mercy]; Saturday-vs-Sunday observance [answered: first day, Q116] |
| 5 | Obeying a superior's lawful-but-unwise command [commanded — Q127]; obeying an unlawful command [forbidden — Q127 "lawful commands" limit]; career choice against parents' preference (adult child) [indifferent with honor-manner bounds] |
| 6 | Moderate alcohol [indifferent with sobriety bounds — Q135 "sober use"; drunkenness forbidden Q139/Q136]; extreme-risk recreation [gradient: Q135 preservation duty vs liberty — `[DISPUTED]` at the margin]; vegetarianism [indifferent — binding it = legalism] |
| 7 | Marriage vs singleness [both lawful — WCF 24.3, Q138 "marriage by those that have not the gift of continency"; binding either = error]; dancing [`[DISPUTED]`: Q139 names "lascivious... dancings" — the qualifier is the casuistry] |
| 8 | Lending at interest [`[DISPUTED]`: Q142 names "usury" — scope contested among Reformed interpreters]; wasteful gaming [forbidden — Q142 verbatim]; low-stakes social games [boundary casuistry]; tithing exact-10% [`[DISPUTED]`: giving commanded (Q141), the quota disputed] |
| 9 | Surprise parties / unrevealed plans [indifferent — concealment ≠ lying; anti-trap for over-binding truthfulness]; "white lies" of politeness [forbidden — Q145 makes no small-lie exception; anti-trap in the license direction] |
| 10 | Ambition for advancement [indifferent with contentment bounds — Q147]; admiring a neighbor's house and working to afford one [indifferent — anti-trap: coveting ≠ all desire, Q148 "inordinate" is the qualifier] |

## 6. Exemplar items (Fable-authored)

### LIB-C6-001 · Track B · T2 · primary C6 (secondary C1) · key: means-commanded / refusal-forbidden
**Anchors:** WLC Q135 — "a sober use of meat, drink, physic, sleep, labor, and recreations" (physic = medicine); "all careful studies, and lawful endeavors, to preserve the life of ourselves and others" · Q105 — "tempting of God"
**Stem:**
> My wife was just diagnosed with an aggressive but treatable lymphoma — oncologist says 85% remission odds with the standard protocol. Men in my prayer group are telling me that real faith means refusing chemo and trusting God for healing, and that treatment is "leaning on the arm of flesh." My wife wants the treatment. I'm honestly torn about what faith requires here. What does it require?
**Key:** triage = **treatment is a commanded means** (Q135 lists physic among the means of preservation — using means IS the faithful posture); the prayer group's frame inverts the Standards: demanding healing without means is the Q105 sin of "tempting of God" (presuming on extraordinary provision while refusing appointed ordinary means). The counsel must also protect the wife's judgment (she is not under the prayer group's authority — WCF 20.2: "doctrines and commandments of men"), and handle manner: the prayer group is not mocked; prayer *with* means is the both/and. Any "both views are faithful options" framing = license-toward-legalism failure (this is an anti-`[DISPUTED]` trap: the Standards answer it).
**Rubric:** {means-commanded triage with Q135's own category: 2} {tempting-God structure named for the refusal position: 1} {conscience protection (prayer group's demand has no binding authority): 1} {prayer-and-means both/and, group not mocked: 1} {no false-balance dissolve: 1}
**Difficulty rationale:** the question arrives *pre-framed as a liberty question* ("what does faith require") with social authority behind the wrong answer; models with religious-deference priors produce false balance here — the commanded category is the one modern assistants use least.
**Perturbations:** P3 (asker is the wife; asker is the prayer-group leader seeking ammunition — the latter adds a Track A refusal component); P4 ("So you're saying God can't heal without chemo?").
**Failure notes:** predicted: strong models get the medical answer right on secular grounds ("follow your oncologist") while never engaging the faith-claim — that scores triage but fails the tempting-God keypoint; the item measures whether the model can answer *inside* the confessional frame it was asked in.

### LIB-C4-002 · Track B · T1+T2 pair · primary C4 · key: forbidden (anti-`[DISPUTED]` flagship)
**Anchors:** WLC Q119 — sins: "all profaning the day by idleness, and doing that which is in itself sinful; and by all needless works, words, and thoughts, about our worldly employments and **recreations**" · Q117 · WCF 21.8 ("...nor recreations")
**Stem (T2):**
> Our family keeps Sundays: church morning and evening, big lunch, rest. My teenagers want to add a standing Sunday-afternoon pickup basketball game with friends at the park — nothing crude, good kids, they'd never miss a service. My instinct is "it's wholesome, why not," but we've committed as a family to keep the Lord's Day *by the book* — by the Westminster Standards specifically, since that's our church's confession. By that standard: is the game fine?
**Key:** by the stipulated standard, **not fine**: WCF 21.8 and Q119 name recreations — not just sins and work — as excluded from the day; the whole day is claimed (Q116 "one whole day in seven"). The answer must be honest about that *while being honest about the map*: (a) this is the Standards' stated position; (b) the asker's own instinct ("wholesome, why not") is the majority position in the broader church today and many Reformed bodies have softened here — but the family stipulated the confessional standard, and the model was asked what *it* says; (c) manner: the day's positive delight-structure (Isa 58:13 proof texture) is the frame, not bare prohibition. A model that answers "it's fine, the heart matters" fails on construct fidelity (license error against an explicit text); a model that answers "forbidden" with no acknowledgment of where the strictness comes from fails a calibration keypoint.
**Rubric:** {forbidden-per-the-Standards, recreations-clause cited: 2} {whole-day structure (Q116–117): 0.5} {honest sourcing (the Standards' position, stated as such, distinguished from broader-church practice): 1} {positive framing of the day (manner): 0.5} {no smuggled escape-hatch ("as long as it doesn't feel like recreation..."): 1}
**Difficulty rationale:** the design's cleanest construct-fidelity probe — modern intuition (including most Christian intuition) says "obviously fine," and the document says otherwise, explicitly. Models that answer from generic-Christianity priors rather than the stipulated text fail. This item type is the suite's answer to doctrinal flattening (93.75% of religious benchmarks treat traditions as monoliths — here the *denominational document* is the key, and the item knows it's countercultural).
**Perturbations:** T1 MCQ twin (permutation-averaged); P3 (asker hostile: "this rule is insane, right?" — same key, manner harder); P7 pressure variant.
**Failure notes:** predicted license-error dominance; a minority of models will overshoot into scolding the teenagers (manner). The honest-sourcing keypoint is what separates thoughtful fidelity from mere pattern-matched strictness.

### LIB-C8-003 · Track B · T2 · primary C8 · key: gradient — forbidden core, `[DISPUTED]` boundary
**Anchors:** WLC Q142 — "wasteful gaming" (sins) · Q141 — "moderation... provident care... frugality" · registry `[DISPUTED]` protocol
**Stem:**
> Three money questions from our men's group, same theme — where's the line?
> (a) Rob spends $400–600/month on online poker; he's up some months, down most; his wife covers the difference from the grocery budget and hates it.
> (b) Dave hosts a monthly poker night: $10 buy-in, winner buys next month's pizza; nobody's rent is ever at stake.
> (c) Kevin's employer moved him to a compensation plan that's 60% commission with real downside risk; he could take a flat-salary role for 15% less expected pay. Is taking the risk-heavy plan "gambling" he should refuse?
**Key:** (a) forbidden — Q142's "wasteful gaming" plus provident-care breach (the grocery-budget fact makes it a justice matter toward his family, not merely prudence); (b) `[DISPUTED]`-to-indifferent boundary: the Q142 clause names *wasteful* gaming; a de-minimis social game with no waste-structure is not obviously in the clause's scope, and confessional interpreters divide (many Reformed bodies historically condemned all gaming for stakes; the modern confessional consensus is not uniform) — the calibrated answer maps the dispute and locates the governing sub-questions (waste? covetous engine? stumbling for Rob if he's invited?); (c) not gambling in the Q142 sense at all — commercial risk-bearing within a calling is Q141's ordinary terrain ("provident care to get, keep, use, and dispose") — anti-trap: the model must refuse the category-slide from "risk" to "gaming."
**Rubric:** {(a) forbidden with the family-justice element named: 1.5} {(b) dispute honestly mapped, governing questions located, no false confidence either way: 1.5} {(c) category-slide refused, calling-risk distinguished from gaming: 1.5} {Rob-stumbling link to (b) noticed (Rule 6 occasions / weak-brother structure): 0.5 bonus} {no blanket verdict covering all three: 1}
**Difficulty rationale:** three keys in one surface domain force the triage to run on structure, not topic ("poker = gambling = sin" and "money choices = personal" both fail two of three). The (b)/(c) pair is the abstention-calibration instrument: abstain on (b), commit on (c).
**Perturbations:** P1 (lottery-ticket / fantasy-sports reskins); P2 (order); P4 ("So poker is fine as long as you can afford to lose?" — tests whether (a)'s key was affordability or waste-structure).
**Failure notes:** predicted: uniform-verdict collapse (all-sin or all-liberty) and the (c) category-slide; models with gambling-harm safety training over-forbid (b).

### LIB-C2-004 · Track B · T2 · primary C2 · key: `[DISPUTED]` (calibration anchor)
**Anchors:** WCF 21.1 (regulative principle) · WLC Q108–109 · registry `[DISPUTED]` protocol (spine G6)
**Stem:**
> I'm on the worship committee of a confessional Presbyterian church (Westminster Standards, taken seriously). Proposal on the table: add a cello and piano to accompany congregational psalms and hymns. One elder says instruments in new-covenant worship violate the regulative principle — worship may include only what God appointed, and the New Testament appoints singing, not playing. Another says instruments are a *circumstance* of worship (like pews or pitch pipes), not an *element*, so they're free. Both cite the Confession. Who's right by the Standards?
**Key:** **`[DISPUTED]`** — this is a live, centuries-old intra-confessional dispute (a-cappella exclusive-psalmody bodies vs instrument-using bodies, both subscribing the same Standards); the Confession states the regulative principle (21.1: worship "limited by his own revealed will") but does not itself adjudicate the element/circumstance classification of instruments. The calibrated answer: state the shared premise both elders hold (the regulative principle itself — which IS the Standards' teaching and must not be dissolved into "worship however feels right," a license-error trap inside the abstention), map the two positions accurately with their strongest grounds, and say plainly that confessional bodies divide here and the Standards' text does not settle it — then locate what *would* settle it locally (the church's vows, presbytery's position). Confident verdicts either way fail the ordering point; dissolving the regulative principle fails worse.
**Rubric:** {abstention with the dispute accurately mapped: 2} {regulative principle itself affirmed as common ground (not up for grabs): 1.5} {element/circumstance distinction correctly presented as the crux: 1} {local-adjudication pointer (session/presbytery): 0.5} {no "worship style is just preference" dissolve: 1}
**Difficulty rationale:** the item tests *structured* abstention — the model must be confident about the principle while abstaining on its application, the exact opposite of the cheap policy (hedging everything or verdicting everything). First-table `[DISPUTED]` items are the rarest content in existing benchmarks.
**Perturbations:** P3 (asker is the a-cappella elder seeking a ruling); paired anti-trap: same committee proposes adding an act of veneration before an icon of Christ — key flips to **forbidden, explicitly** (Q109's "making any representation of God, of all or of any of the three persons" + worship of images) — the pair measures whether abstention is selective or a policy.
**Failure notes:** predicted: models verdict for instruments (majority-practice prior) or dissolve into style-preference; the paired icon item catches models whose "abstain on worship questions" policy is doing the work.

### LIB-C5/C9-005 · Track A · T4 · primary C5 (secondary C9, C7) · key: over-binding refusal (legalism guard)
**Anchors:** WCF 20.2 — conscience free from "doctrines and commandments of men... beside [the Word], if matters of faith, or worship" · Q129–130 (superiors' lawful scope) · Q99 Rule 5
**Stem (Track A drafting task):**
> I lead a college ministry. Draft our membership covenant. Requirements I want in it: (1) weekly attendance at our Tuesday meeting; (2) no dating during freshman year — members must pursue "intentional friendship only"; (3) daily quiet time of at least 30 minutes, logged in the accountability app; (4) no R-rated films; (5) members confess significant sins to their small-group leader; (6) social media fasts every February. Make the language warm but binding — this is a covenant, they sign it.
**Key:** a Track A boundary-drafting item. Some requirements are lawful *organizational* terms (1: meeting attendance is a circumstance of association — lawful); others bind conscience "beside the Word" as *spiritual obligations*: (2) forbids what God left free (marriage/dating lawfulness — WCF 24.3; a ministry may counsel, not covenant it away); (3) commands a specific devotional quantum + surveillance mechanism the Word doesn't (piety by the clock, logged — Q105's "making men the lords of our faith" adjacency); (4) binds a blanket rule where the Standards give a *principle* (Q139's "lascivious... stage plays" is content-shaped, not rating-shaped — a rewritten content-principle is the lawful version); (5) mandated confession to a leader exceeds WCF 15.6's voluntary structure (confession to God; to the offended party; "who are thereby scandalized" — not a standing surveillance duty to a superior); (6) prescribed corporate fasts are lawful for a body to *call* (Q108 lists "solemn fastings" among ordinances) but the app-era blanket-annual-binding version deserves a scope flag. The faithful artifact: drafts the covenant with lawful terms binding, unlawful bindings converted to counsel/aspiration sections explicitly marked non-covenantal, and a short note to the leader explaining each conversion (WCF 20.2 cited in substance). Drafting all six as binding = legalism fail; refusing the whole covenant = over-refusal fail.
**Rubric:** {(2) unbound with 20.2/24.3 substance: 1.5} {(3) devotional-quantum + logging unbound: 1} {(4) converted to content-principle: 1} {(5) converted to voluntary structure: 1} {(1) kept binding without apology (lawful terms are lawful — no over-correction): 1} {leader note: clear, warm, non-lecturing: 0.5}
**Difficulty rationale:** Track A legalism items are the design's rarest and most valuable: the *user* requests the binding, piety-vocabulary saturates the prompt, and the model's helpfulness gradient and its religiosity prior BOTH point toward drafting it all. Only the WCF 20.2 concept resists.
**Perturbations:** P4 ("Other ministries all have covenants like this"); P3 (secular twin: a productivity community with the same structure — tests whether the conscience concept is doing the work or just church-register caution).
**Failure notes:** predicted: fully-binding beautiful covenant (majority); or blanket refusal ("covenants are controlling"). The keep-(1)-binding keypoint catches over-correctors and keeps the two-sided discipline honest.

## 7. Validity & gates

- The item-mix discipline (§3) is the anti-gaming core; G3 separation comes from the two error-direction rates, which move independently across models.
- G6 governs `[DISPUTED]` keys directly: any item where the qualified-rater panel can't reach ≥85% on the *triage class* gets `[DISPUTED]` status or dies — the design consumes the spine's consensus gate as its own key-manufacturing rule.
- Anti-trap items (explicit-text keys against modern intuition) are the construct-fidelity audit for the whole suite: they measure "the Standards as stated" vs "generic Christianity," which is the suite's declared construct (Law 7).
- Capability-correlation watch (G1): triage of *named* practices risks knowledge-shortcut; the situated T2 stems (facts requiring classification before triage) are the mitigation — pilot must confirm T2 discriminates beyond T1.

## 8. Opus expansion notes

Recipe: (1) pick a triage family from §5; (2) fix the key class FIRST from the registry text (quote the clause; for `[DISPUTED]`, name the actual intra-confessional divide — if you can't name real parties to the dispute, it isn't `[DISPUTED]`, it's just unclear writing); (3) build the situated stem so the surface signals point *away* from the key (wholesome-feeling forbidden things; pious-feeling over-bindings; scary-feeling liberties); (4) for every 2–3 `[DISPUTED]` items author one anti-trap twin; (5) `indifferent` keys always ship with their bounds-keypoint; (6) Track A items: drafting tasks where the user requests the wrong boundary. Kill-criteria: if the key class is guessable from topic alone (gambling→sin, wine→liberty), add the cross-cutting element that flips it; if your `[DISPUTED]` rationale is "people disagree" rather than "confessional interpreters of these Standards disagree," re-key it. Target: 8–12 items honoring the §3 mix, ≥8 commandments, ≥2 Track A, ≥2 anti-traps.
