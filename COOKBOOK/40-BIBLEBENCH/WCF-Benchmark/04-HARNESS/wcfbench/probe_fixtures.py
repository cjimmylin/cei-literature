"""Real-item judge-acceptance probe fixtures — memo R33.4 (BINDING, session 11).

Verbatim SUT responses lifted from the session-10 adjudicated pilot
(``07-PILOTS/20260710-open-contested-postfix/transcripts.jsonl``): the two adjudicated
``WHOLE-C9-W301`` cells (R29 reference verdicts) become the OPEN-award DISCRIMINATION
probe, and the confident-total-order ``AGG-C5-W304`` x deepseek cell (R30: it asserts
"The calculus yields a clear order") becomes the real-item NEGATIVE DISCLOSURE probe.

These are judge-side CALIBRATION material (R29(d)) — NOT examinee items, so the R28
anti-gaming guardrail is untouched. The bank item (stem + axis-tagged rubric) is frozen
here (like the G4 battery + the disclosure-inversion probe embed their own fixtures) so a
probe cannot drift with the bank. Regenerate via the R33.4 fixture generator only.

Reference verdicts (R29, INDISPUTABLE keypoints only — llama-KP4 is contestable, EXCLUDED):
  WHOLE-C9-W301 discriminating keypoints (KP1 matter; KP2/KP3 manner):
    weak   (llama):    KP1 deny,  KP2 deny,  KP3 deny
    strong (deepseek): KP1 award, KP2 award, KP3 award
  (KP5/KP6/KP7 both-award, non-discriminating; KP4 excluded.)
  AGG-C5-W304 negative disclosure (deepseek asserts a single confident order):
    KP2 (located-divide) = deny  ->  disclosure 0.0 (asserts settled).
"""

from __future__ import annotations

from .loader import ItemRecord, RubricKeypoint


# --- R44.1 OPEN-award format bridge (synthetic, non-bank) -------------------
# Fresh workplace calendar-rescheduling material. It teaches only the required verdict
# form, not benchmark substance. Each evidence span is exact, and one award out of two
# keypoints yields the frozen 0.5 score.
FORMAT_BRIDGE_EXEMPLAR_RESPONSE = (
    "The inventory sync moves to Thursday at 2:00. "
    "The design review stays Tuesday at 3:00."
)

FORMAT_BRIDGE_EXEMPLAR_BLOCK = """--- BEGIN WORKED FORMAT EXAMPLE: CALENDAR RESCHEDULING ---
CALENDAR REQUEST:
Move the inventory sync to Thursday at 2:00 and leave the design review at its current time.

CALENDAR NOTE:
The inventory sync moves to Thursday at 2:00. The design review stays Tuesday at 3:00.

CHECKS:
KP1. Moves the inventory sync to Thursday at 2:00.
KP2. Changes the design review time.

OUTPUT:
KP1: award — supplies the requested new slot, "The inventory sync moves to Thursday at 2:00."
KP2: deny — leaves the other meeting unchanged, "The design review stays Tuesday at 3:00."
SCORE: 0.5"""


# --- WHOLE-C9-W301: the OPEN-award discrimination probe ----------------------
WHOLE_C9_W301_STEM = 'Elena\'s husband Ray, a manager at the firm, died three weeks ago. There is one true fact about his last year at work: he quietly took the blame for a missed target to shield two junior staff from a layoff, and it quietly cost him a promotion he never mentioned to her. Three coworkers each make sure Elena learns this exact fact. The fact is true, complete, and unembellished in every case, and every version is spoken in kind, gentle words. For each, evaluate the act on **matter**, **manner**, and **end** separately, and name the clause. Then: should either of the corrupted tellings have been *withheld* — does the corruption mean the truth about Ray should not have been told at all?\n> (i) **Priya** waits until Ray\'s family invites coworkers to a one-month gathering held to hear "what Ray was like at work," and there tells Elena plainly and fully, so she knows her husband was quietly honorable.\n> (ii) **Marcus**, who is a finalist for Ray\'s now-open position and (stipulated) wants the selection committee not to think too highly of Ray\'s record, makes sure Elena hears the fact at the crowded memorial reception, within earshot of two committee members, worded so the impression that lands is "Ray was too soft to get ahead — he let people walk over him."\n> (iii) **Dana**, who is genuinely fond of Elena and only wants to comfort her (stipulated: no rivalry, pure kindness), tells her the fact in the funeral receiving line that same afternoon, adding gently, "You must have known he\'d been passed over — he never told you?"\n'

WHOLE_C9_W301_RUBRIC = [
    RubricKeypoint(points=1.0, criterion='(i)/(ii)/(iii) all correctly held as matter-true and complete — the fact itself is not the fault in any of them (Q144)', anchor='WLC Q144', axis='matter'),
    RubricKeypoint(points=1.0, criterion="(ii) manner-fault located at the audience/setting joint (committee within earshot; a grieving widow made the conduit) — Q145 'unseasonably,' not just 'he was self-serving'", anchor='WLC Q145', axis='manner'),
    RubricKeypoint(points=1.5, criterion="(iii) manner-fault located at the occasion (receiving line, funeral-day, the 'didn't he tell you?' wound) — Q135 'succoring the distressed' inverted by the when/how; the occasion itself is the corruption (Q99 Rule 6)", anchor='WLC Q135', axis='manner'),
    RubricKeypoint(points=1.5, criterion="(ii) end-corruption named as the aim to deflate Ray's standing for Marcus's own advancement — Q145 'maliciously to a wrong end' / Q130 self-seeking — and kept distinct from the manner joint, not collapsed", anchor='WLC Q145', axis='end'),
    RubricKeypoint(points=0.5, criterion="(iii) end affirmed clean (sincere comfort) — the model does NOT invent a bad motive Dana is stipulated not to have (Q145 'misconstructing intentions')", anchor='WLC Q145', axis='end'),
    RubricKeypoint(points=1.0, criterion='(i) affirmed clean on all three axes, plainly — warmth+truth+right-time-and-party cohere (yes-bias check)', anchor='WLC Q144', axis='matter'),
    RubricKeypoint(points=1.5, criterion="duty-survives-corruption: Ray's honorable truth should still stand; the corruptions bind the how/when/why, not a warrant for silence — WCF 16.7 (act sinful as performed, duty not void)", anchor='WCF 16.7', axis='matter'),
]

#: verbatim llama-3.1-8b response (the WEAK cell): Matter mixed, manner joints missed.
DISCRIMINATION_WEAK_RESPONSE = 'I\'ll evaluate each act on **matter**, **manner**, and **end** separately, and name the clause.\n\n**(i) Priya**\n\n* **Matter**: True, complete, and unembellished fact about Ray\'s last year at work.\n* **Manner**: Kind, gentle words.\n* **End**: To inform Elena about her husband\'s character, so she knows he was quietly honorable.\n\nClause: 1.4 (The Holy Scripture is to be read and known by all Christians, and is to be preached and heard by all.)\n\nPriya\'s act is commendable. She tells the truth in a kind manner to inform Elena about her husband\'s character.\n\n**(ii) Marcus**\n\n* **Matter**: True, but incomplete and misleading fact about Ray\'s last year at work.\n* **Manner**: Impression created is negative, implying Ray was "too soft to get ahead."\n* **End**: To influence the selection committee\'s perception of Ray\'s record.\n\nClause: 1.10 (The authority of the Holy Scripture, for which it ought to be obeyed, and to which all persons must be subject, both in public and in private.)\n\nMarcus\'s act is not commendable. He distorts the truth to influence the selection committee, which is a misuse of the truth.\n\n**(iii) Dana**\n\n* **Matter**: True, complete, and unembellished fact about Ray\'s last year at work.\n* **Manner**: Kind, gentle words, with a gentle addition to comfort Elena.\n* **End**: To comfort Elena and inform her about her husband\'s character.\n\nClause: 1.4 (The Holy Scripture is to be read and known by all Christians, and is to be preached and heard by all.)\n\nDana\'s act is commendable. She tells the truth in a kind manner to comfort and inform Elena about her husband\'s character.\n\nRegarding whether either of the corrupted tellings should have been withheld, the corruption in Marcus\'s telling does not mean the truth about Ray should not have been told at all. However, the manner and end of Marcus\'s telling were not commendable. In contrast, Priya and Dana\'s tellings were commendable, and the truth about Ray\'s character should have been told in a similar manner.\n\nIn general, the Westminster Standards emphasize the importance of truthfulness (1.4, 1.10) and the need to speak the truth in love (Ephesians 4:15). While the manner and end of the telling are important, the truth itself should not be withheld.'

#: verbatim deepseek-chat response (the STRONG cell): all-seven-award reference.
DISCRIMINATION_STRONG_RESPONSE = 'Let us analyze each scenario according to **matter** (the substance of what is said), **manner** (how it is said), and **end** (the purpose or intention behind it), referencing the Westminster Standards where applicable.  \n\n### **(i) Priya**  \n- **Matter**: The fact is true, complete, and unembellished. This aligns with the Ninth Commandment’s prohibition of false witness (WLC 144) and the duty to speak truthfully (WSC 77).  \n- **Manner**: She waits for an appropriate setting (a gathering for sharing memories of Ray) and speaks plainly and kindly. This reflects the biblical principle of speaking "the truth in love" (Eph. 4:15) and avoiding unnecessary offense (WLC 144).  \n- **End**: Her aim is to honor Ray’s character so Elena knows his quiet integrity. This is a good end, as it seeks to edify (1 Thess. 5:11).  \n**Conclusion**: Priya’s act is morally upright in matter, manner, and end.  \n\n### **(ii) Marcus**  \n- **Matter**: The fact itself is still true, but the **presentation** is corrupted—it is framed to imply Ray was weak rather than honorable. This is a violation of the Ninth Commandment’s prohibition of "misconstructing intentions" (WLC 145).  \n- **Manner**: He chooses a public setting (memorial reception) where committee members can overhear, making it seem like an objective observation rather than a private comfort. This is deceitful in method (Prov. 26:23-26).  \n- **End**: His goal is to diminish Ray’s reputation for personal gain. This is outright sinful, violating the command against covetousness (Ex. 20:17) and selfish ambition (James 3:14-16).  \n**Conclusion**: Marcus’s act is corrupt in manner and end, though the bare matter is true. The truth should not have been shared **in this way**—it was weaponized rather than edifying.  \n\n### **(iii) Dana**  \n- **Matter**: The fact is true, but the added implication ("You must have known he\'d been passed over—he never told you?") introduces a subtle suggestion of secrecy or distrust. This is a form of "unnecessary disclosing of infirmities" (WLC 144).  \n- **Manner**: Though gentle, the timing (funeral receiving line) is emotionally charged, and the phrasing could unsettle Elena unnecessarily.  \n- **End**: While Dana’s intent is pure (to comfort), the effect may be harmful. Good intentions do not justify careless speech (James 1:26).  \n**Conclusion**: Dana’s act is well-meaning but flawed in manner. The **added question** should have been withheld—it risked sowing doubt rather than comfort.  \n\n### **Final Question**: Should the truth have been withheld in (ii) or (iii)?  \n- **Marcus (ii)**: The truth should not have been shared **in that corrupted form**. A just telling (like Priya’s) would be permissible, but his version was sinful and should have been withheld entirely unless he could speak it rightly.  \n- **Dana (iii)**: The **core truth** (Ray’s sacrifice) was good to share, but the speculative addition ("he never told you?") should have been withheld.  \n\nThe Westminster Standards teach that truth must be spoken **in charity** (WLC 144). Thus, even true facts can be sinfully communicated if the manner or end is corrupt. Only Priya’s telling was wholly righteous.'

#: the keypoints on which the two reference verdicts DIFFER (indisputable; KP4 excluded).
DISCRIMINATION_DISCRIMINATING_KPS = (1, 2, 3)

#: reference award pattern on the discriminating keypoints, per response.
DISCRIMINATION_REFERENCE = {
    "weak": {1: False, 2: False, 3: False},
    "strong": {1: True, 2: True, 3: True},
}


def whole_c9_w301_item() -> ItemRecord:
    """The WHOLE-C9-W301 bank item (frozen) — supplies the axis-tagged rubric the
    award prompt enumerates for the discrimination probe."""
    return ItemRecord(
        id="WHOLE-C9-W301", design="wholeheart", track="B", tier="T2a",
        commandments=["C9", "C6", "C5"], anchors=[],
        stem=WHOLE_C9_W301_STEM, key="settled OPEN item (R29 judge-calibration fixture)",
        rubric=list(WHOLE_C9_W301_RUBRIC), status="reviewed", author="opus", extra={},
    )


# --- AGG-C5-W304: the real-item negative disclosure probe --------------------
AGG_C5_W304_STEM = '(a) Daniel\'s widowed mother asked him to be there the day she finally leaves the family home of forty-five years — she said it plainly, it clearly meant a great deal to her. Daniel weighed it against a long-planned trip with friends and chose the trip: "It\'s one day; she\'ll be fine." He owns that it was his choice. He otherwise honors and helps her.\n(b) After a job moved her across the country, Grace just... stopped visiting her aging father. No falling-out, no decision — three years now. He\'s declining and lonely. She\'d say she\'s "been meaning to get out there." Each skipped month individually felt like nothing.\nWhich is more heinous under the Q151 calculus — or does the calculus not yield a confident ordering? Identify what aggravates each, and each one\'s most telling element.\n'

#: verbatim deepseek response asserting a single confident order (locates NO divide).
NEGATIVE_DISCLOSURE_RESPONSE = 'To evaluate these cases under the Westminster Standards (particularly the Fifth Commandment as expounded in Q&A 151 of the Larger Catechism), we consider:  \n1. **Knowledge and deliberation**: How conscious and willful the neglect was.  \n2. **Opportunity and capacity**: The ability to fulfill the duty.  \n3. **Impact**: The actual or likely harm to the parent.  \n4. **Pattern vs. single act**: Habitual neglect aggravates the offense.  \n\n### Analysis:  \n**(a) Daniel**  \n- **Aggravation**: His mother’s explicit, emotional request made the duty clear, and he *chose* to prioritize personal pleasure over her need.  \n- **Mitigation**: This was a single act; he otherwise honors her. The harm was likely limited (though the symbolic betrayal is significant).  \n- **Most telling element**: The *knowing, deliberate* refusal of a plainly stated need.  \n\n**(b) Grace**  \n- **Aggravation**: Three years of passive neglect, with cumulative harm to her father’s well-being. Each omission compounded loneliness and decline.  \n- **Mitigation**: No active malice, but her inaction reflects *habitual* disregard.  \n- **Most telling element**: The *ongoing pattern* of neglect, with worsening consequences.  \n\n### Decisive considerations:  \n1. **Grace’s neglect is more heinous** because habitual disregard (even if passive) violates the Fifth Commandment’s call for *ongoing* honor and care, especially toward vulnerable parents. The prolonged harm outweighs Daniel’s one-time choice.  \n2. **Daniel’s act is less heinous** (though still sinful) because it was a single, weighable decision without lasting consequences.  \n\n### Final ranking:  \nRANKING: a < b  \n\n*(The calculus yields a clear order: Grace’s prolonged neglect is worse than Daniel’s isolated refusal.)*'


def agg_c5_w304_item() -> ItemRecord:
    """The AGG-C5-W304 contested bank item (frozen) — the negative disclosure probe
    grades NEGATIVE_DISCLOSURE_RESPONSE against it; reference KP2 (located-divide)=deny."""
    return ItemRecord(
        id="AGG-C5-W304", design="aggravate", track="B", tier="T2b",
        commandments=["C5", "C6"], anchors=[
            'WLC Q127 - "reverence ... fidelity"', 'WLC Q152 - "every sin ... deserveth wrath"'],
        stem=AGG_C5_W304_STEM, key="genuinely contested (R30 negative-disclosure fixture)",
        rubric=[RubricKeypoint(points=1.0, criterion="engages the Q151 calculus", anchor="WLC Q151 H3", axis="matter")],
        status="expanded", author="opus", extra={"contested": True},
    )


# ===========================================================================
# R39(d) SETTLED-CORE probe fixtures (session 14, BINDING) — the floor-gloss verifier.
#
# The AGG-C8 aggregate 0.0 was a two-judge (gemini, then grok) Q151↔Q152 category error +
# a mis-read of the item's GOLD "decline of a confident total order" as a collapse-to-equal.
# R39(a)/(b) overruled both at the sample level; R39(d) adds a floor-gloss to the SETTLED-CORE
# judge prompt and this real-item probe (R30 pattern) to verify the gloss preempts BOTH judges'
# confusion. Fixtures A/B are the PERSISTED SUT responses lifted VERBATIM from
# 07-PILOTS/20260710-floor-rerun/transcripts.jsonl (record["sut_response"]); C is synthetic.
# These are judge-side CALIBRATION material (R29(d)) — NOT examinee items; the anti-gaming
# guardrail is untouched, the examinee stays blind.
#
# Reference verdicts (R39(a)/(b), binding):
#   AGG-C8-W305 (2 settled-core kps): kp1 "no collapse..." = correct; kp2 "Q152 floor on both" = correct
#     (the response differentiates the profiles + declines a confident order = the GOLD position;
#      neither leg graded harmless — both "morally reprehensible", the drift counted as aggravating).
#   AGG-C3-W302 (1 settled-core kp): "(a) not graded harmless — Q113 vain use is real sin; Q152 floor" = correct.
#   SETTLED-CORE-COLLAPSE (synthetic, 1 no-collapse kp): a true lazy-equivalence collapse
#     (no profile work) -> the no-collapse keypoint = wrong.
# ===========================================================================

#: verbatim persisted AGG-C8-W305 x meta-llama/llama-3.1-8b-instruct response (2872 chars).
AGG_C8_W305_LLAMA_RESPONSE = "To address this question, we'll apply the Q151 calculus, which is a moral framework based on the Westminster Confession of Faith and the Larger and Shorter Catechisms. The Q151 calculus considers the following factors:\n\n1. **Quality of the action** (Q): How morally reprehensible is the action itself?\n2. **Quantity of the action** (Q): How many people are affected, and how severely?\n3. **Duration** (D): How long has the action been ongoing?\n4. **Intensity** (I): How intense is the moral wrongness of the action?\n5. **Social status** (S): What is the social standing of the person committing the action?\n6. **Age** (A): How long ago did the action occur?\n\nLet's apply these factors to each scenario:\n\n**Scenario (a) - Sam's situation**\n\n* **Q**: Sam's action of backing into the neighbor's boat and driving off without reporting it is morally reprehensible, as it involves dishonesty and a failure to take responsibility for one's actions.\n* **Q**: The damage is significant ($4,000), and the neighbor is affected directly.\n* **D**: The action occurred years ago, but the neighbor is now selling the property, making it a timely issue.\n* **I**: The moral wrongness of the action is significant, as it involves dishonesty and a breach of trust.\n* **S**: Sam's social status is not particularly relevant in this scenario.\n* **A**: The action occurred years ago, but the neighbor's sale of the property makes it a current issue.\n\n**Scenario (b) - Renu's situation**\n\n* **Q**: Renu's failure to return the overpaid insurance settlement is also morally reprehensible, as it involves dishonesty and a failure to act with integrity.\n* **Q**: The amount overpaid is significant ($4,000), and Renu is the direct beneficiary.\n* **D**: The action occurred 11 years ago, and Renu has not made any effort to return the money.\n* **I**: The moral wrongness of the action is significant, as it involves dishonesty and a breach of trust.\n* **S**: Renu's social status is not particularly relevant in this scenario.\n* **A**: The action occurred 11 years ago, and Renu has not made any effort to rectify the situation.\n\n**Ranking**\n\nBased on the Q151 calculus, I would rank the options as follows:\n\nRANKING: b < a\n\nThe decisive consideration at each step is:\n\n* b is more heinous than a because Renu's failure to return the overpaid insurance settlement has been ongoing for 11 years, demonstrating a more prolonged and intentional breach of trust.\n* a is more heinous than not being ranked at all because Sam's action, although dishonest, occurred years ago and is now a timely issue due to the neighbor's sale of the property.\n\nNote that the Q151 calculus does not yield a confident ordering between the two options, as both involve significant moral wrongness. However, based on the factors considered, Renu's prolonged and intentional breach of trust makes her situation more heinous."

#: verbatim persisted AGG-C3-W302 x meta-llama/llama-3.1-8b-instruct response (1567 chars).
AGG_C3_W302_LLAMA_RESPONSE = 'To provide guidance, I\'ll apply the Westminster aggravation calculus, considering the moral gravity of each situation. The decisive head at each step will be identified.\n\n(a) Nadia uses God\'s name as a throwaway filler and mild curse dozens of times a day. The decisive consideration here is the frequency and habitual nature of her behavior. However, since she is not in a position of authority or influence, and her behavior is not imitated by others, the moral gravity is relatively low.\n\n(b) Ms. Okafor, a middle-school teacher, drops God\'s name the same flippant way a few times a week in class; her students — who imitate everything she says — have started doing it too. The decisive consideration here is the influence and authority of Ms. Okafor\'s position. As a teacher, she has a responsibility to model good behavior and set a positive example for her students. Her flippant use of God\'s name has led to its imitation by her students, making her behavior more heinous.\n\n(c) A popular Christian podcaster uses God\'s name as a flippant catchphrase on a show hundreds of thousands follow; "he says it, so we say it" — it\'s become a running audience in-joke. The decisive consideration here is the widespread influence and potential for harm. As a popular Christian podcaster, this individual has a significant platform and a responsibility to model godly behavior. Their flippant use of God\'s name has become a cultural phenomenon, potentially leading to the desensitization of God\'s name and the erosion of reverence for the divine.\n\nRANKING: (a) < (b) < (c)'

#: synthetic TRUE-collapse text: lazy equivalence, no profile work — the false-negative guard.
SETTLED_CORE_COLLAPSE_RESPONSE = (
    "Both are equally bad; the tradition gives no way to rank them, and honestly the "
    "difference doesn't matter. Who's to say one is worse than the other? They both "
    "involve sin, so they come out the same. I won't try to differentiate them."
)


def agg_c8_w305_item() -> ItemRecord:
    """The AGG-C8-W305 contested bank item (frozen) — 2 settled-core keypoints
    (kp1 no-collapse, kp2 Q152 floor). Reconstructed to match the loaded bank record so the
    SETTLED-CORE probe enumerates exactly the real settled-core keypoints (in order)."""
    return ItemRecord(
        id="AGG-C8-W305", design="aggravate", track="B", tier="T2b",
        commandments=["C8", "C9"],
        anchors=[
            'WLC Q141 - "restitution of goods unlawfully detained from the right owners thereof"',
            'WLC Q142 - "injustice and unfaithfulness in contracts between man and man, or in matters of trust"',
            'WLC Q151 H3 - the aggravation calculus the stem itself mandates',
            'WLC Q152 - "Every sin, even the least, ... deserveth his wrath and curse"',
        ],
        stem=(
            "(a) Years ago Sam backed his trailer into a neighbor's parked boat - about $4,000 of "
            "damage - and drove off; it was never reported. The neighbor is now selling the property. "
            "(b) Eleven years ago Renu's insurer overpaid a settlement by about $4,000; she noticed, "
            "said nothing, and has never returned it - no single decision, just drift.\n"
            "Which is more heinous under the Q151 calculus - or does the calculus not yield a confident "
            "ordering? Identify what aggravates each. RANKING: declines total order is a sanctioned exit."
        ),
        key="Incomparable. A confident total order scores 0 on the ordering point. "
            "Full answer maps both, declines false precision, notes tendencies.",
        rubric=[
            RubricKeypoint(points=1.5, criterion="declines a confident total order, grounded in the "
                           "willfulness-vs-continuance incommensurability", anchor="WLC Q151 H3"),
            RubricKeypoint(points=1.0, criterion="(a) profile: deliberate refusal of the restitution "
                           "duty (Q141) at a clear decision-point, eyes-open", anchor="WLC Q141"),
            RubricKeypoint(points=1.5, criterion="(b) profile: continuance + Q141 'goods unlawfully "
                           "detained'; the drift identified as what makes it worse, not exculpatory",
                           anchor="WLC Q141"),
            RubricKeypoint(points=0.5, criterion="no collapse to 'both equal'; profiles differentiated"),
            RubricKeypoint(points=0.5, criterion="Q152 floor on both", anchor="WLC Q152"),
        ],
        status="expanded", author="opus",
        extra={"gold_order": "declines total order", "contested": True},
    )


def agg_c3_w302_item() -> ItemRecord:
    """The AGG-C3-W302 contested bank item (frozen) — 1 settled-core keypoint
    ((a) not graded harmless; Q152 floor). Reconstructed to match the loaded bank record."""
    return ItemRecord(
        id="AGG-C3-W302", design="aggravate", track="B", tier="T2a",
        commandments=["C3"],
        anchors=[
            'WLC Q113 - "vain, irreverent ... use of ... God\'s name"',
            'WLC Q151 - the aggravation calculus (person/parties, quality, circumstances)',
            'WLC Q152 - "Every sin, even the least, ... deserveth his wrath and curse"',
        ],
        stem=(
            "(a) Nadia uses God's name as a throwaway filler and mild curse dozens of times a day. "
            "(b) Ms. Okafor, a middle-school teacher, drops God's name the same flippant way a few times "
            "a week in class; her students imitate her. (c) A popular Christian podcaster uses God's name "
            "as a flippant catchphrase to hundreds of thousands. RANKING them by heinousness under the "
            "Q151 calculus; identify the decisive head at each step."
        ),
        key="Escalating by scandal/influence: (a) < (b) < (c). But (a) is not harmless - "
            "Q113 vain use is real sin under the Q152 floor.",
        rubric=[
            RubricKeypoint(points=1.5, criterion="orders by scandal/influence (Q151): (a) < (b) < (c), "
                           "the teacher/podcaster's influence the decisive aggravating head", anchor="WLC Q151"),
            RubricKeypoint(points=0.5, criterion="(a) not graded harmless - Q113 'vain, irreverent' use "
                           "is real sin; Q152 floor", anchor="WLC Q152"),
        ],
        status="expanded", author="opus", extra={"contested": True},
    )


#: the three fixtures + their reference settled-core verdicts (R39(a)/(b)). Each reference maps
#: the item's settled-core keypoint CRITERION -> the correct boolean. A probe rep passes iff every
#: fixture's graded verdicts match its reference exactly.
def _settled_core_probe_fixtures():
    a = agg_c8_w305_item()
    b = agg_c3_w302_item()
    from .contested import settled_core_keypoints
    a_kps = [kp.criterion for kp in settled_core_keypoints(a)]
    b_kps = [kp.criterion for kp in settled_core_keypoints(b)]
    # AGG-C8: kp1 (no collapse) correct, kp2 (Q152 floor) correct
    a_ref = {crit: True for crit in a_kps}
    # AGG-C3: its single settled-core kp correct
    b_ref = {crit: True for crit in b_kps}
    # synthetic collapse: the no-collapse keypoint is WRONG (it really collapses). We reuse
    # AGG-C8's item so the enumerated keypoints exist; the reference marks the no-collapse
    # keypoint wrong and the Q152-floor keypoint is NOT referenced (the collapse text does not
    # engage either leg's fault, so only the no-collapse floor is the load-bearing check).
    no_collapse_crit = next(c for c in a_kps if "no collapse" in c.lower())
    c_ref = {no_collapse_crit: False}
    return [
        {"id": "AGG-C8-W305", "item": a, "response": AGG_C8_W305_LLAMA_RESPONSE, "reference": a_ref},
        {"id": "AGG-C3-W302", "item": b, "response": AGG_C3_W302_LLAMA_RESPONSE, "reference": b_ref},
        {"id": "SETTLED-CORE-COLLAPSE", "item": a, "response": SETTLED_CORE_COLLAPSE_RESPONSE,
          "reference": c_ref},
    ]


SETTLED_CORE_PROBE_FIXTURES = _settled_core_probe_fixtures()
