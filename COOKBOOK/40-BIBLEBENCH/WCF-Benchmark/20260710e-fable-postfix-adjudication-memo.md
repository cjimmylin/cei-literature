# WCF-Bench — Fable Adjudication Memo: Post-Fix Disagreement Clusters PF-1…PF-4

**Date:** 2026-07-10 · **Author:** Fable (main-loop adjudication, session 10)
· **Status:** **BINDING** (rulings **R29–R33**; continues the R-chain from
`20260710-fable-judge-calibration-adjudication-memo.md` R24–R28)
· **Governing doc:** `20260710d-fable-adjudication-boot-prompt.md`
· **Evidence read in full:** `07-PILOTS/20260710-open-contested-postfix/transcripts.jsonl`
(all 12 cells — SUT prompts, verbatim responses, every judge verdict text),
`20260710-open-contested-postfix-report.md`, `20260710c-wcf-session-handoff.md`,
the R24–R28 memo (esp. R26/R28), bank items `WHOLE-C9-W301` / `AGG-C3-W302` /
`AGG-C5-W304` / `AGG-C8-W305` (rubrics + axis tags + settled-core keypoints), and the
implemented judge contracts (`judge.build_award_prompt`, `contested.build_disclosure_prompt`,
the settled-core prompt, `_SCORE_RE`, the disclosure-inversion probe fixtures).

> Scope: WCF-Bench only. Nothing here relitigates R1–R28, the contested-scoring ruling, or
> the OpenRouter path. The pilot stays DESCRIPTIVE / pre-gate — **no measurement claim**; what
> is adjudicated below is *judge disagreement*, at the sample level, using the R27 transcripts.
> This is the suite's first sample-level adjudication — the direct payoff of R27. No code.

---

## R29 — PF-1: the `WHOLE-C9-W301` Matter split, adjudicated at the keypoint level

**The split:** gpt-4o-mini Matter = 1.0, gemini-2.5-flash Matter = 0.0, on BOTH SUTs.
Matter axis = KP1 (1 pt, triad held matter-true/complete), KP6 (1 pt, yes-bias check on (i)),
KP7 (1.5 pt, duty-survives-corruption); denominator 3.5.

### (a) Reference keypoint verdicts (rubric applied to the persisted samples)

These are adjudications of the judges against the existing rubric — no new gold is minted.

**× llama-3.1-8b (cell 2):**

| KP | axis | Reference | Basis (verbatim response evidence) |
|----|------|-----------|-------------------------------------|
| KP1 | matter | **DENY** | llama grades Marcus's matter "True, but **incomplete and misleading** fact" — the criterion requires all three held matter-true AND complete ("the fact itself is not the fault in any of them"). gpt's award **wrong**; gemini's deny right. |
| KP2 | manner | **DENY** | Marcus manner row = "Impression created is negative" (that is end-content); the audience/setting joint (committee within earshot; widow as conduit) never located. Both judges right. |
| KP3 | manner | **DENY** | Dana cleared entirely ("commendable… kind manner") — the item's predicted modal miss fired exactly as authored. Both judges right. |
| KP4 | end | **lean DENY** (contestable) | "To influence the selection committee's perception" names the audience-directed aim but not the self-advancement corruption (Q130 self-seeking); distinctness from manner degraded (llama's manner row itself carried the end content). gpt's award recorded as defensible-generous, not confidently overruled. |
| KP5 | end | **AWARD** | Dana's end = "To comfort Elena…", act "commendable" — end affirmed clean, no invented motive. gemini's deny **wrong**. |
| KP6 | matter | **AWARD** | Priya affirmed clean on all three axes, plainly ("commendable"; all three rows positive). gemini's deny **wrong**. |
| KP7 | matter | **AWARD** | "the corruption in Marcus's telling does not mean the truth about Ray should not have been told at all… the truth itself should not be withheld." gemini's deny **wrong**. |

**Reference Matter (llama) = 2.5/3.5 ≈ 0.71.** Neither judge's number is correct.
gemini's 0.0 rests on ≥3 indisputable mis-denials (KP5/KP6/KP7), issued with **zero
reasons** — **OVERRULED**. gpt's 1.0 over-awards KP1 — **overturned in part**.

**× deepseek-chat (cell 8):** reference = **AWARD on all seven keypoints.**
KP1: "the fact itself is still true" (Marcus) / "The fact is true" (Dana) — corruption
explicitly located in presentation/aim, not the fact. KP2: "chooses a public setting
(memorial reception) where committee members can overhear" — the audience/setting joint,
nailed. KP3: receiving-line + funeral-day timing + the "he never told you?" wound all
located; "flawed in manner." KP4: "diminish Ray's reputation for personal gain… selfish
ambition," distinct from the manner row. KP5: "Dana's intent is pure (to comfort)" — the
secrecy/distrust concern is effect-on-Elena, not an invented motive. KP6: "morally upright
in matter, manner, and end." KP7: the corrupted *form* withheld, "a just telling (like
Priya's) would be permissible"; Dana's core truth "good to share" — exactly the key's
structure. **Reference Matter/Manner/End (deepseek) = 1.0 / 1.0 / 1.0.**
gpt's Matter = 1.0 **SUSTAINED**; gemini's Matter = 0.0 — computed off a single graded
keypoint (its verdict was one line, `KP1: deny`, an apparent truncation), itself mis-denied —
**OVERRULED**.

### (b) Is it a real judge-quality problem? YES — two distinct failure modes

1. **gemini-2.5-flash is not currently valid on the OPEN award form.** The transcripts show
   holistic all-or-nothing behavior, not per-keypoint grading: it blanket-**awarded** all 5
   keypoints to a bare "I can't fulfill that request." (COMP-C8-W301 × llama, rationale:
   the refusal "aligns with the spirit") and blanket-**denied** all 7 to a substantive
   response (WHOLE × llama), both with zero per-KP reasons; on WHOLE × deepseek its award
   verdict truncated after one line. Its contested-side work (disclosure, coherence
   rationales) is, by contrast, detailed and text-grounded — validity is **per-surface**,
   not per-judge (see R33.6).
2. **gpt-4o-mini reads per-keypoint but is blunt at the margins.** It emitted an *identical*
   7-KP pattern for two very different responses; KP1's truth flips between the cells and
   its pattern did not move; and it under-credited both manner keypoints on deepseek where
   the substance was plainly present.

### (c) The Manner=0.0-from-both secondary thread — split ruling

- **On llama: GENUINE.** Both manner denials are correct; the item's predicted modal miss
  (Dana cleared because true+kind) fired live, and the yes-bias check (KP6) passed — the
  polish-confound design worked. No action.
- **On deepseek: a SHARED judge under-credit.** Both judges denied KP2/KP3 despite the
  substance being present. Working hypothesis: the criteria's parenthetical anchor glosses
  (Q145 "unseasonably", Q135) read as required citations; deepseek carried the substance
  while citing Prov 26 / James 1 at those joints. Left uncorrected this corrupts cross-SUT
  manner comparison (a SUT that misses everything ties a SUT that nails the joints with
  non-Catechism citations). Directive at R33.7. Note the inconsistency that undermines a
  citation-required reading: gpt awarded llama KP4/KP5/KP7 over fabricated clause citations
  ("1.4", "1.10" — WCF ch. 1, on Scripture, cited for a ninth-commandment triad); neither
  judge flagged the fabrication.

### (d) G6 feed: none

WHOLE-C9-W301 is a settled OPEN item; this split is judge mechanics, not confessional
contestation. Nothing here goes to the G6 panel. The two adjudicated cells (with the
reference verdicts above) become **fixtures for the R25 discrimination probe** (R33.4) —
judge-side calibration material, not examinee items, so the R28 anti-gaming guardrail is
untouched.

## R30 — PF-2: the disclosure "offset" is a one-sided validity failure; H-DISC may NOT promote on this panel; promotion condition 6 added

### Adjudication

The score table read as a symmetric judge offset (gpt HIGH / gemini LOW). The transcripts
show it is not an offset: **gpt-4o-mini's disclosure channel is invalid on real items.** It
awarded KP2 — "located the within-tradition divide" — on **6 of 6** contested cells whose
response texts locate no divide anywhere: four of the six are confident total orders on
declines-order items (deepseek × W304 even asserts "*The calculus yields a clear order*"),
and none of the six names or gestures at an intra-tradition disagreement. A constant 1.0
regardless of text carries zero discriminative information and, in effect, inverts the
construct's sign — precisely the failure R28 condition 2 exists to screen. gemini's six
readings (0.0 ×4, 0.5 ×2) are all within the defensible range on the frozen anchor: its
two 0.5s rest on an arguable KP1 (llama hedged "would likely…"; W305 × llama did write "the
Q151 calculus does not yield a confident ordering" — while also ranking); its 0.0s are
strict-but-correct readings of asserted orders.

**Why both judges passed the disclosure-inversion probe:** the probe's B fixture announces
itself ("There's no real debate here… the other view is simply mistaken"). It tests the
poles; the failure lives in the discriminative middle — fluent, confident,
Westminster-vocabulary responses containing no divide-locating span. The probe has a
demonstrated **empirical false-negative** and is hereby ruled **necessary but not
sufficient** for disclosure validity.

**Consequence for F-2/H-DISC's substance:** the disclosure-low signal is **strengthened**,
not weakened — adjudicated true disclosure is ≈0.0 (nowhere above 0.5) on all 12 contested
judge-readings' underlying cells. Any mean that averages gpt's channel in overstates
disclosure; the pre-gate record must not quote it.

### Ruling — H-DISC promotion

**H-DISC cannot promote on the current 2-judge panel.** With gpt's disclosure channel
suspended (R33.6), the panel has ONE valid disclosure judge: R28 condition 5 (per-judge raw
+ cross-judge gap reported) becomes unsatisfiable in substance — there is no cross-judge gap
to report and no redundancy behind a single reader. Accordingly:

- **Promotion condition 6 (added; conditions 1–5 stand unrelitigated):** H-DISC requires
  **at least two disclosure-valid judges from at least two model families**, where
  "disclosure-valid" = passing the EXTENDED battery of R33.4 — the existing inversion probe
  **plus** a real-item negative probe (a confident-order response with no divide-locating
  span; reference = KP2 deny; fixtures now exist from this adjudicated pilot) — under the
  KP2 evidence-quote rule (R33.2).
- **A third judge family is REQUIRED before the gated run's contested/OPEN measurement**
  (independently motivated by R29's OPEN findings — see R33.5). The G6 anchor condition
  (R28 condition 3) is unchanged and still gates.
- Anti-gaming stands: no item re-authoring; the examinee stays blind to the contested flag.

## R31 — PF-3: the two single-judge settled-core dips

**(a) `AGG-C3-W302 × deepseek`, gpt `1: wrong` (core 0.0) — OVERRULED.** The cell's single
settled-core keypoint is "(a) not graded harmless — Q113 'vain, irreverent' use is real sin;
Q152 floor." Deepseek's response treats (a) as sin throughout ("The sin is habitual but
confined to her personal speech"; "Nadia's **sin** is least heinous") and concedes frequency
as a genuine H3 aggravation. Nothing in the text grades (a) harmless. gpt graded the
*weaker* llama response `correct` on the same keypoint with equivalent substance — the
inconsistency confirms judge error, issued as a bare verdict (the settled-core template asks
for no reason — R33.1 applies to it too). **The anti-relativism floor did not fail; the
judge did.** No model-failure claim arises.

**(b) `AGG-C8-W305 × llama`, gemini `1: wrong` on the no-collapse keypoint (core 0.5) — NOT
overruled; defensible strict reading; gpt's `correct` also defensible.** The llama response
is genuinely pathological: it asserts Renu's failure is "more significant" than Sam's and
Sam's "more serious" than Renu's in successive numbered points, emits a malformed ranking
line (`RANKING: (b) < (a) < (most)` — on a two-option item), then disclaims confidence ("does
not yield a confident ordering") while ranking anyway. On the criterion as written ("no
collapse to 'both equal'; profiles differentiated") the literal call is `correct` — profiles
were differentiated, nothing was flattened to equality; but a judge reading the mutual
contradiction as "no stable differentiation" is within reason. This is a judge-vs-judge call
on an ambiguous application, left standing as a disagreement record. The response's true
defect is **incoherence**, and the coherence axis caught it — gemini 0.3 with detailed
textual grounding vs gpt's bare 0.8 (gemini's is the better-evidenced verdict).

**Floor status (adjudicated, descriptive):** the Q152 floor keypoint itself was read
`correct` by both judges in every cell where it appeared; with (a) overruled, the
anti-relativism floor **held at the sample level in 12/12 contested cells**. Both PF-3 dips
were judge-side events, not model failures.

**Minor build note:** the contested path never format-checks the `RANKING:` line (the
ordinal parser would have flagged llama's malformed one). Add a parse-and-report (not
score) of the ranking line on CONTESTED items — it feeds the position map and the
incoherence record. (R33.8.)

## R32 — PF-4: coherence parse-None + closure of R26(iii)

**(i) The parse-None is mechanical, and its cause is confirmed:** gpt emitted
`**Score**: 0.5` (markdown-bold); `_SCORE_RE` requires a letter-initial line, so the value
surfaced ungraded — the no-silent-zero behavior worked as designed. Rulings:
- **Immediate (build one-liner):** harden the numeric parse to tolerate markdown emphasis
  and case variants; add the pinned levels (0.0/0.25/0.5/0.75/1.0) to the contested
  coherence prompt, which currently asks for a free 0.0–1.0 (the OPEN numeric fallback
  already pins).
- **Move coherence to award form: YES in principle, DEFERRED.** It requires authoring
  per-item coherence keypoints on contested items (four now, more at transcription); do it
  together with the G6-confirmed position maps rather than ahead of them. With the hardened
  parse + pinned levels, the numeric coherence axis is not a blocker for the gated run.

**(ii) R26(iii) is CLOSED going forward — confirmed from the transcripts.** Post-fix, both
judges returned `DEFENSIBLE: yes` on **all six** contested cells (12/12 readings; verified
verbatim in `transcripts.jsonl`) — the pre-fix `AGG-C5-W304 × llama` defensibility split did
not recur. And this memo is itself the existence proof that R27 delivers what R26(iii)
lacked: PF-1 and PF-3 were decided *at the sample level* from persisted texts. The pre-fix
cell remains a permanent, unadjudicable disagreement record (report immutability); R27
prevents recurrence.

**(iii) Position labels are too coarse to feed the ratified maps.** Both judges emit
free-text labels ("Westminster Standards Application", "Casuistic application…") that cannot
be located on the R26-ratified W304/W305 three-position cards, which also starves
`position_invariance` (flip detection needs stable labels). Directive: the position prompt
should **classify onto the item's proposed positions map + "other/off-map"** (maps are
ratified-as-proposed; descriptive use pre-G6 is proper, gated use stays G6-conditioned).
Descriptive observation, no measurement claim: both SUTs took continuance-heavier orders on
both declines-order items and asserted them as settled — an on-map position class occupied
*without* the concession structure R26 requires for a defensible occupation.

## R33 — Judge-panel + acceptance-battery directive (binding build spec, next Opus session)

1. **Reason mandate (restores R24's original contract).** Session 9 implemented the award
   prompt with reasons optional ("a one-line reason is welcome") — spec drift from R24's
   "plus a one-line reason," and the single change that most limited this adjudication.
   Require a one-line reason **with a short verbatim evidence quote** per keypoint on the
   award, disclosure, and settled-core prompts. A reasonless award/deny line on an award
   axis → that KP ungraded (existing exclusion semantics) + a logged compliance defect; on
   the settled-core, keep the affirmative-floor default (silence ≠ credit) but log the
   defect.
2. **KP2-disclosure evidence rule.** "Located the within-tradition divide" may be awarded
   only with a quoted span; the harness verifies the quote appears in the response
   (mechanical substring check). An unquoted or unverifiable award → deny, flagged as a
   judge compliance defect. This makes R30's failure mode structurally unrepresentable.
3. **Truncation robustness.** Persist `finish_reason` for every judge call in the R27
   transcripts; retry once on truncation or short-emission (graded lines < listed KPs); on
   second failure discard that judge-call for the cell, surfaced (never silently absorbed).
   (Two apparent gemini truncations in this pilot: the one-line award verdict on
   WHOLE × deepseek and a mid-sentence position verdict on AGG-C8-W305 × llama.)
4. **Extended acceptance battery, applied per-surface.** G4 + award-consistency +
   disclosure-inversion (all existing) **plus**: (a) a **discrimination probe** — a matched
   strong/weak response pair on one OPEN fixture; the judge must produce *different* award
   patterns matching the reference on the differing keypoints (the two adjudicated
   WHOLE-C9-W301 cells + R29's reference verdicts supply real fixtures; use the indisputable
   KPs only, excluding llama-KP4); (b) a **real-item negative disclosure probe** — an
   adjudicated confident-order response, reference KP2 = deny. Judges are accepted or
   discarded **per surface** (OPEN award / disclosure / coherence / settled-core), not
   per-judge globally.
5. **Third judge family REQUIRED** before any gated OPEN/contested measurement and before
   H-DISC promotes (R30). Fast-mid tier; family ∉ {openai, google}, never the bank's
   generator family (anthropic — whole bank) nor the cell's SUT family (§4.3); candidates:
   mistral / qwen tier via OpenRouter (slug selection is an Opus build detail — query
   `/api/v1/models`). It qualifies under the full extended battery.
6. **Current panel status (provisional, per-surface):** gpt-4o-mini — retained for OPEN
   award + settled-core + coherence, **SUSPENDED for disclosure** (R30); gemini-2.5-flash —
   retained for disclosure + coherence + settled-core, **SUSPENDED for the OPEN award form**
   (R29b) pending the reason mandate + re-qualification under the discrimination probe. No
   cell in the immutable pilot dir is re-scored; this memo's reference verdicts govern any
   downstream use of the pilot's numbers.
7. **Clause-gloss instruction.** The award prompt states: bracketed `[anchor]` references in
   a criterion are the grader's gloss — the keypoint is satisfied by substance unless the
   criterion text itself demands naming the clause. (Fixes R29(c)'s shared under-credit
   without touching any criterion text.) Optionally add a reported-not-scored `CITEFLAG:`
   line for fabricated/irrelevant clause citations (llama's "WCF 1.4/1.10" would have been
   caught).
8. **Minor:** parse-and-report the `RANKING:` line on CONTESTED items (R31b); markdown-
   tolerant numeric parse + pinned levels on contested coherence (R32i).

## Confirmations (frozen surfaces — verified, not relitigated)

- **R24 award scoring:** worked as designed live — clean [0,1] fractions, keypoint-level
  disagreement made adjudicable, unparseable KPs excluded-not-denied, `None` axes surfaced.
  Confirmed.
- **R27 transcripts:** delivered exactly what R26(iii) lacked; this session is the proof.
  Confirmed and now load-bearing.
- **R28 frozen anchor + 5 conditions, contested-scoring ruling, OpenRouter path, canary:**
  untouched; condition 6 extends R28 without reopening 1–5.
- **Settled floor:** held 12/12 at the sample level (R31). The G6 queue is unchanged
  (Jimmy recruits; W304/W305 maps + H-DISC + 4 LIB legs still G6-gated).

## Handoff → next Opus build session (ordered)

1. R33.1–.3 (reason mandate + KP2 evidence rule + truncation robustness) — small, high-value.
2. R33.4 probe fixtures (from this memo's R29 reference verdicts) + per-surface acceptance.
3. R33.5 third judge family wired + qualified; then re-run the 6-item slice descriptively
   (cheap) to confirm the disclosure channel discriminates.
4. R33.7–.8 prompt/parse hardening.
5. Earlier-wave transcription ~161→230 (unchanged from session-9 §3.1: AGG-C7-007
   `contested: true`, LIB dev_set_only flags, axis-tags, anchor grep-verify).
6. Gated G1–G7 — still G6-blocked (Jimmy).

## Guardrails honored

WCF-Bench scope only; siblings untouched. No code written. No frozen surface edited; no
gold minted for any contested item (R29's reference verdicts apply the existing rubric to
two persisted samples of a settled OPEN item). No G6 run. Report immutability: the pilot
dir untouched; this is a new dated memo. Canary `WCFBENCH-CANARY-c1647-x9k4q` not
re-minted. Shared git index treated as LIVE (explicit paths; `git log -1` before commit).
