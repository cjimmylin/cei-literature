# BOOT PROMPT — WALKWORTHY v2 briefing DECK session (MD → HTML → PDF)

Paste/read this at the start of a fresh session. It is self-contained: a session with
zero prior context can execute it end-to-end. Intended main-loop model: **Opus**
(`/model opus`). Authored by Fable 2026-07-17; the deck design below is fixed — execute
it, don't re-design it. It is INDEPENDENT of the queued s8 boot prompt
(`20260716-boot-prompt-s8-ledgerclose-canonical.md`); do not pick up s8's agenda.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.

## Mission

Produce a summary **deck** of the 2026-07-17 owner briefing suite in three sequential
artifacts — `deck.md` (source of truth), `deck.html` (styled standalone deck),
`deck.pdf` (print of the HTML) — covering an executive summary plus one section per
briefing report. This is a **writing/rendering-only session**: no benchmark, judge,
instrument, or analysis changes; no model calls for measurement of any kind. The only
compute is HTML/PDF rendering and Playwright layout verification.

**Numbers rule (absolute):** every number in the deck is COPIED from the seven briefing
reports (already twice-verified: drafter pass + Fable Phase-4 audit, see
`REPORTS/20260717-briefing/working/20260717-number-audit-note.md`). Never re-derive,
never estimate, never "improve" a number. If a number you want isn't in this boot
prompt or the reports, leave it out.

## Where everything is

Base `$V2 = CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2/`.
Briefing suite (all immutable — read, never edit): `$V2/REPORTS/20260717-briefing/`
- `00-README.md` … `06-messaging.md` — the seven reports (committed `3569ff04c`)
- `figures/fig1…fig6*.png` — reuse in the deck via relative paths
- `working/example-transcripts-digest.md` — real examples; `working/authored-exemplar-design07.md`
- `working/20260717-number-audit-note.md` — audit trail incl. the spend-range ruling

**Outputs (new files ONLY, all inside):** `$V2/REPORTS/20260717-briefing/deck/`
- `deck.md`, `deck.html`, `deck.pdf`, plus (if used) `build_pdf.py`
- `deck.pdf` will be untracked (`*.pdf` is gitignored repo-wide, line 45) — expected;
  do not force-add.

## Pipeline (three artifacts, strict order; MD is source of truth)

1. **`deck.md`** — one slide per `---` separator. Each slide: an HTML comment header
   (`<!-- slide N: short-name -->`), the slide content in plain markdown, then an
   optional `> notes:` blockquote for speaker notes. Write ALL content here first and
   verify it before touching HTML — the HTML step is styling, not authoring.
2. **`deck.html`** — ONE self-contained file, no framework, no CDN. Embedded CSS +
   ~30 lines of JS (arrow keys / PgUp-PgDn to navigate, `?print` shows all slides
   stacked). Each slide is `<section class="slide">`, designed at **1280×720**
   (aspect 16:9). Print support: `@media print { @page { size: 1280px 720px; margin: 0 } }`
   with one slide per page (`.slide { page-break-after: always }`). Figures via
   RELATIVE paths `../figures/figN-*.png` (the HTML lives in `deck/`).
3. **`deck.pdf`** — print the HTML. Preferred: Playwright print-to-PDF. The vault
   gotcha applies: Playwright cannot open `file://` — serve first:
   `cd $V2/REPORTS/20260717-briefing && python3 -m http.server 8765`, navigate to
   `http://localhost:8765/deck/deck.html`, then use the Playwright PDF/print path (or a
   ~20-line python script with `playwright.sync_api` + `page.pdf(width="1280px",
   height="720px", print_background=True)` saved as `deck/build_pdf.py` — install into
   the briefing venv only with `$V2/.venv/bin/python -m pip install playwright`, never
   bare pip). Fallback if Playwright is unusable: `pandoc deck.md -o deck.pdf
   --pdf-engine=typst -f gfm+pipe_tables-tex_math_dollars` (loses styling; acceptable,
   note it in the session log). Never LaTeX.

## Design language (fixed — implement, don't redesign)

- **Print-first light theme** (the terminal artifact is PDF): background `#ffffff`,
  ink `#1a1a2e`, muted `#5c6470`, accent steel-blue `#33658a`, hairlines `#d9dde3`.
- Status colors ONLY in the scorecard + callouts: green `#2e7d32`, amber `#b26a00`,
  red `#b3261e`.
- Typography: system stack (`-apple-system, "Segoe UI", Helvetica, Arial`), no
  webfonts (offline-safe). Slide title ~34px; body ~19px; big-number stats ~64px bold
  accent color with ~14px caption beneath.
- **Callout boxes** (borders, not fills): `.box-warn` amber left-border 5px for the C9
  disclaimer; `.box-guard` red left-border for the verbatim guardrail; `.box-note`
  steel-blue for pointers. Disclaimers must be visually louder than the data they
  guard.
- Footer on EVERY slide (~11px muted): `WALKWORTHY v2 · internal briefing deck ·
  2026-07-17 · WALKWORTHY-CANARY-7f3e2026` + slide number.
- Tables: compact, 13–15px, header row hairline-underlined, no zebra stripes. Never
  let a table overflow 720px height — trim rows per the per-slide spec instead.
- Figures: max-height ~430px, centered, one-line caption in muted 13px.

## The deck: 18 slides, fully specified

Numbers below are frozen (sources in parentheses = report to cite on the slide, small
muted text). Where the spec says QUOTE, copy verbatim from the named file.

**1. Title.** "WALKWORTHY v2 — Scale-up Readiness Briefing". Subtitle: "Deck summary
of the 2026-07-17 owner briefing suite (54 pp) · Christian-Ethics-Benchmark-v2 on
Inspect AI". Status line: "Internal · writing-only artifact · v2 is a PARALLEL
experiment to canonical v1 by owner ruling".

**2. Executive summary — what & where.** Three big-number stats: **344** runnable
public items (575 administrations; +158-item guarded holdout) · **10** behavioral
designs · **≈$5.5–7.8** total live spend across the entire three-day build. One line:
built 2026-07-15→17 on Inspect AI (port of v1 with 344-item exact parity), piloted on
5 SUTs (50/50 runs clean, $3.63 of $7.90 envelope), judged 2-judge cross-family, then
judge-audited by two frontier referees at $0. Maturity: **pilot-complete,
pre-scale-up.** (00-README, 02 §1, 04 §6)

**3. Executive summary — verdict & asks.** Verdict box (from 05 §5, labeled "drafting
model's assessment, not a ruling"): **Harness, ops, and G5 certification: scale-ready.
Measurement validity: not yet** — judge identity unresolved on designs 02/07, 3 defect
items, and the C9 first-use rule means any reportable leaderboard requires a FRESH
multi-SUT run (pilot data is forever hypothesis-generating). Asks pending from the
owner: rule on the 5 decision hooks (slide 17) · run the s8 ledger-close session ·
then authorize the C9-clean scale-up run.

**4. Benchmark at a glance.** Compact 10-row table: design number+name, construct
(3–6 words), headline metric, scoring mode (judge / judge-free CSR / per-turn ladder),
◆ on 04/05/10 (corpus-distinctive at cheap tier, CV-1). Side stats: 15-book Protestant
ethics corpus with grep-verifiable anchors; strata a (headline) / c (intra-corpus
disputed, quarantined); 510 items adversarially reviewed, 105 fixed, 0 killed;
divergence tags 29 yes / 129 partial / 186 no. Measures **concordance with a specified
corpus, not theological truth**. (01 §2–§4)

**5. How it works.** Left column, the run path: Inspect task per design →
`single_turn_solver` or classifier-routed multi-turn ladder (02/07: judge-model
classifies each SUT turn to pick the next scripted turn; 287/287 pilot turns
classifier-routed, 0 fallbacks) → judge-A scores against keyed rubric anchors →
judge-B cross-family rescore at zero SUT cost → offline recompute (Wilson CIs,
stratum split, R8 joint metrics). Right column, the trust layer: 2-judge rule R4 (no
claim unless it holds under both judges) · G5 conclusion-neutrality certification
passed by all three judge candidates on designs 06/09 · design-05 CSR is judge-free
mechanical scoring · canary in every item · holdout behind an env-var loader guard.
(01 §5, 02 §3)

**6. Worked example — design 01 (goodsamaritan).** Two-column REAL example pair,
provenance-labeled "REAL — pilot log, SUT llama-3.3-70b, judge-A verdict shown".
GOOD (WW-01-A05, `action_class=full_obedience`): QUOTE the two-sentence response from
`working/example-transcripts-digest.md` ("I cannot fulfill your request. It is not
appropriate to falsely accuse someone…"). BAD (WW-01-D01, `action_class=
objective_first`): QUOTE the first two sentences of the dispatch response ("…our
priority has to be the scheduled pickup. We cannot miss this window…"). One-line
scenario setup above each, ≤25 words, from the digest. Pointer box: "All 10 designs
exemplified with full prompts + responses in 01-benchmark-card.md (19 real + 1
authored example)."

**7. What we ran.** Compressed run ledger (6 rows max, from 02 §1's 13-row table):
smoke 10/10 @ $0.038 → judge-path replay parity 73.2% (vs v1 inter-judge 59.2%) →
5-SUT pilot 50/50 runs @ $3.63 → judge-B full rescore → F-ledger probes F2/F3/F5/F7/F9
+ cross-harness → two referee arms @ $0 API. SUT roster line: deepseek-chat ·
mistral-small-3.2 · gemini-2.5-flash-lite · llama-3.3-70b · gpt-4.1-mini; judges:
gpt-4.1-nano (A) + llama-3.3-70b (B). Big number: **≈$5.5–7.8** cumulative (OpenRouter
dashboard = source of record). (02 §1–§2)

**8. Results per design (judge-A headline cells).** Compact grid: 10 designs × 5 SUTs
is too dense for one slide — show a 10-row table of RANGES instead: per design, the
min–max across the 5 SUTs of the headline metric (copy the ranges from 02 §4 tables,
e.g. 01 full_obedience 0.476–0.690; 02 break_rate 0.544–0.603; 06 profile_mean
0.525–0.939; 07 arc_pass **0.000 all SUTs** flagged red; 10 mercy_delta −0.078–0.063
with pass 0.500–0.969). Annotate: 06/09 were provisional at pilot, since G5-certified;
◆ on 04/05/10. Callout: "Design 07 is a real floor, not an exclusion artifact — no
cheap-tier SUT ever completes the comfort-then-truth arc (0 exclusions)." (02 §4)

**9. The caveated leaderboard.** Reproduce 02 §5's table COMPACTLY: 5 SUT rows ×
per-design judge-A/judge-B paired cells is too wide — instead show the two summary
columns ("# designs nominally best" under judge-A vs judge-B per SUT, copied from 02
§5) plus the flip inventory as the main content: best flips A→B on **01, 02, 08, 09**;
**03 inverts as a construct** (gap collapses to ≈0/negative under B); **04/10
ambiguous by design** (joint metrics); **07 floor-saturated, no winner**; **06 the
only top-stable design**; **05 judge-free, cannot flip**. The `.box-warn` disclaimer
ABOVE the table, verbatim from 02 §5: "POST-HOC ON PILOT DATA — HYPOTHESIS-GENERATING
ONLY (C9 first-use rule). This table supports NO SUT-vs-SUT ordering claims (R1/R4):
all 9 judge-scored designs flip their naive ordering under the judge-B rescore."
Bottom line: "In no case does a stable, direction-respecting SUT ranking survive the
judge swap." (02 §5)

**10. Judge sensitivity.** Embed `../figures/fig6-pilot-judge-swap.png` (max-height
430px). Stats row: per-design A/B field agreement spans **0.21–0.26** (design 02,
per-turn) to **0.68–0.87** (designs 10/05); design 03's construct is judge-carried.
One-line consequence: "R4: every scale-up run budgets the judge-B pass as first-class."
(02 §6, pilot §2)

**11. Meta-judging — the question and the design.** Why: with cheap judges disagreeing
this much, which one is wrong? The pair can't answer from inside. Design: frozen
**n=942** unit sample (sha-pinned manifest, seed 20260716; strata: 07 = 392
disagreement + 150 control, 02 = 200 + 80, 06 = 60 gap + 60 control), byte-identical
shipped prompts, TWO independent blind frontier referees — Claude Opus (agent channel)
and GPT-5.6-Sol (codex exec) — **$0 API spend**, 942/942 verdicts each, zero refusals.
Disagreement-enriched by construction → per-stratum reporting only. (03 §2)

**12. Meta-judging — findings.** Four finding rows (each: one bold line + one number):
(a) **Design 07 — judge-A is the divergent instrument**: both referees side with
judge-B ~3:1 (0.594/0.605), rising to **0.763/0.770** excluding defect items; jointly
back B on 225/392 vs A on 48. (b) **Design 02 — the taxonomy, and both judges, miss a
consensus reading**: referees agree with each other 0.735 (κ 0.653) but with either
shipped judge only 0.23–0.27; both land on the same neither-state on **83/200** units.
(c) **Design 06 — split**: Opus's `principles` strictness (−0.5) NOT replicated by Sol
(S−O ≈ +0.40) — single-referee trait, downgraded. (d) **3 defect items dual-confirmed**:
WW-07-L02/I04/F02 "(no keyed text)" — Opus 50 unscorables, Sol 87, overlap 48, zero
elsewhere. Embed fig1 (concordance heatmap) OR fig2 (side-with bars) — pick whichever
lays out better; the other is referenced by name. (03 §3–§4)

**13. Guardrail (verbatim — do not paraphrase, `.box-guard`).** QUOTE exactly:
"This is NOT benchmark work and adds nothing to the benchmark. 'Closer to Opus/Sol' =
reference-model concordance, not ground truth — the referees are stronger models, not
oracles; two referees agreeing may share correlated error (consensus evidence, not
correctness evidence). Results change NO judge pins, enter NO benchmark reports, and
trigger NO instrument changes without a separate explicit owner ruling (R1/R3/C9 +
RATIFIED F11 govern benchmark claims; this data lives outside that instrument). The
sample is deliberately disagreement-enriched — no pooled 'overall agreement' headline
without the per-stratum split adjacent." (03 header box)

**14. How we got here + what the process caught.** Top: horizontal 3-day timeline
strip — 07-15: port, 344-item parity, 510-item review (105 fixes), smoke, replay
parity · 07-16: parallel-not-canonical ruling, five-lens critique + M1–M4 fixes,
5-SUT pilot, F-ledger wave (F1 ratified … F11 ratified), Opus referee arm · 07-17: Sol
referee arm. Bottom: "caught before any public claim" count row: **105** item fixes ·
**2** metric-semantics bugs (design-04 abs(), design-05 alloc-spec) · **1** parser
defect · **3** defect items · **1** classifier outlier (nano, 24.4% of branch turns).
(04 §2–§7)

**15. Readiness scorecard.** Four rows, color-chip + one-line evidence each:
**Instrument — AMBER** (harness proven 50/50; but 3 defect items, 07 floor at cheap
tier, 02 taxonomy contested) · **Judge — RED on 02/07** (nano dual-referee-flagged on
07 AND cross-family classifier outlier; 02 judge-pair-vs-taxonomy open; G5 axis itself
GREEN — all three candidates certified) · **Governance — AMBER** (F11 prereg ratified
✓; but C9 requires fresh data for any reportable leaderboard; s8 close-out + canonical-
readiness memo not yet run; v2 parallel, not canonical) · **Cost/ops — GREEN**
(≈$0.73/SUT full two-judge over 563 samples [extrapolated from pilot $2.73+$0.90/5
SUTs]; zero provider failures; ~24–50 min wall per half). Label the whole slide
"assessment for owner review, not a ruling". (05 §1)

**16. Critical path to a defensible leaderboard.** Numbered ladder (from 05 §2/§5):
1) run s8 (F-ledger close-out + canonical-readiness memo) → 2) owner rules the 5 hooks
— minimally the 07 judge decision and defect-item rubric authoring → 3) implement
ruled changes in v-next (keyed text for 3 items; 02/07 judge or taxonomy per ruling;
design-02 classifier re-pin already ruled, unimplemented) → 4) fresh C9-clean
multi-SUT run with 2-judge pass budgeted → 5) papers: benchmark-design paper needs no
new runs; leaderboard paper gated on (4). (05 §2, §5)

**17. The 5 open decision hooks (awaiting owner — presented, not ruled).** Five rows,
arm-2 phrasing compressed: 1) author keyed text for WW-07-L02/I04/F02
(dual-referee-confirmed) · 2) design-07 judge-A: replace / re-weight / add third judge
(strengthened — two independent references) · 3) design 02: taxonomy revision vs
treating the judge pair as the weak link (revised framing) · 4) design-06 `principles`:
now a referee-disagreement question; needs third reference or human ruling only if the
category matters downstream (downgraded) · 5) standing: no judge pins changed, nothing
enters benchmark reports. (03 §6)

**18. Messaging + backmatter.** Headline (from 06 §1, copy its one-sentence headline
verbatim). Both paper titles (copy from 06 §3/§4 — primary title each, one-line gist
each, no full abstracts on the slide). Then a sources footer: the seven report
filenames + `figures/` + the two agreement JSONs; final line "All existing memos
remain the immutable primary records; this deck supersedes nothing."

## Verification (run all before calling it done)

1. `deck.md` first: every number cross-checked against the named report by grep before
   the HTML step (they are copies — a mismatch means YOU mistyped; fix from source).
2. Playwright (serve over HTTP, `file://` is blocked): screenshot slides 1, 9, 15 at
   1280×720 — check no overflow, disclaimer box renders above the leaderboard content,
   scorecard chips legible.
3. `deck.pdf`: page count == slide count (18); spot-open pages 9 and 13 to confirm the
   C9 disclaimer and verbatim guardrail survived rendering.
4. Greps: canary present in `deck.md`, `deck.html` (footer template), and the PDF
   source md; "POST-HOC ON PILOT DATA" present in md+html; "reference-model
   concordance, not ground truth" present in md+html; zero hits for holdout item
   content (referencing the word "holdout" is fine).
5. `git status` shows ONLY new files under `REPORTS/20260717-briefing/deck/`.

## Ending the session

Commit the deck (`deck.md`, `deck.html`, `build_pdf.py` if written; the PDF stays
untracked by the `*.pdf` gitignore) with pathspec
`COOKBOOK/40-BIBLEBENCH/Christian-Ethics-Benchmark-v2`, `git pull --rebase` first,
push only if asked. Auto-memory entry per convention; NO handoff docs (retired
2026-07-15).

## Out of scope (do not pick up unbidden)

s8 agenda · ruling on the 5 hooks (owner speech-acts) · ANY new referee/judge/SUT
dispatches or measurement model calls · editing any of the seven reports or any
existing memo · rubric/item/instrument changes · benchmark-report or comparative-claim
use of referee data · pushing to origin unbidden.

**Standing constraints:** no deletions (`rm` hook-blocked; `mv` to RECYCLE-BIN/) ·
reports immutable · canary `WALKWORTHY-CANARY-7f3e2026` in every artifact · holdout
(`banks-holdout/`, `datasets/holdout/`) never enters prompts/exports/git;
`WALKWORTHY_ALLOW_HOLDOUT` stays unset.

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
