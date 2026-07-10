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
