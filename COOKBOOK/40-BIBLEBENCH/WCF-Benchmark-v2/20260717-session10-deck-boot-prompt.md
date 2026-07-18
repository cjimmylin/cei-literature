# WCF-Benchmark-v2 — Session 10 Boot Prompt (DECK-BUILD session)

> Paste as the opening prompt of a fresh **Opus** session. Self-contained. Read
> top-to-bottom, then build. This is an **execution** session, not a planning one:
> the design is already locked below — do **not** re-litigate scope, theme, or
> pipeline. Build the deck, verify it, report.

## Mission

Build a **summary slide deck** of the 34-page Session-9 *Scale-Up Readiness
Briefing* for WCF-Bench-v2 (Christian-Ethics-Benchmark-v2). Produce it in **three
progressive artifacts**: **(1) Markdown → (2) self-contained HTML → (3) PDF.** The
deck carries an **Executive Summary** plus a summary of **each of the six report
sections**, at **~27 slides**, in the vault's **dark + gold** deck house-style, with
a **presenter note on every slide**.

You are summarizing existing, committed work. **No new benchmark runs, no eval/grade
calls, $0 OpenRouter.** You introduce **no new numbers** — every figure comes from
the six committed reports (the source of truth in §3) and must be cross-checked
against them before you finish.

## 1. What you are producing (three files + a builder)

Create a new folder `DECK/` under the project root and write:
- `DECK/YYYYMMDD-session10-readiness-deck.md` — the deck **authored in Markdown**;
  the reviewable source of truth (deliverable #1).
- `DECK/YYYYMMDD-session10-build-deck.py` — a small Python builder that parses the MD
  into slides and emits the HTML (deliverable tool).
- `DECK/YYYYMMDD-session10-readiness-deck.html` — one **self-contained** dark+gold
  HTML deck (inline CSS/JS, no network/CDN) + a Speaker-Notes appendix (deliverable #2).
- `DECK/YYYYMMDD-session10-readiness-deck.pdf` — the printed PDF (deliverable #3).

`YYYYMMDD` = the date you run this. Project root:
`CEI-Lit-WS/COOKBOOK/40-BIBLEBENCH/WCF-Benchmark-v2/` (all paths relative to it).

## 2. Pipeline (locked — offline-safe; use these exact mechanics)

Environment recon (already done): **no** marp / reveal-md / decktape / Typst slide
packages (they need network — do NOT rely on them). **Google Chrome IS installed and
headless-print works.** pandoc 3.9, Typst 0.14.2, fpdf2 2.8.4 are present.

**Primary path — bespoke HTML + Chrome headless print:**

1. **MD deck.** Author `…-deck.md`: YAML front matter (`title`, `date`), then one slide
   per block **separated by a line containing only `---`**. Each slide:
   ```
   <!-- type: content -->        (one of: title | divider | content | table | callout | twocol | chart | closing)
   ## Slide Title
   - bullet
   - bullet
   Notes: one or two sentences of presenter talk-track for this slide.
   ```
   The `Notes:` line (or `> Notes:` block) is mandatory on every slide.

2. **HTML build.** `…-build-deck.py` reads the MD, splits on `^---$`, parses the
   `type`, title, body, and `Notes:` out of each block, and emits ONE self-contained
   HTML file: a `#deck` shell with one `<section class="slide" data-type="…">` per
   slide, a hidden `<aside class="notes">` per slide, arrow-key + click JS nav, and a
   **Speaker-Notes appendix** section at the end (all slides' notes, numbered). Inline
   the full CSS from §4. No external requests.

3. **PDF build.** Print the HTML with Chrome headless:
   ```bash
   CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
   "$CHROME" --headless --disable-gpu --no-pdf-header-footer \
     --print-to-pdf="DECK/YYYYMMDD-session10-readiness-deck.pdf" \
     "file://$(pwd)/DECK/YYYYMMDD-session10-readiness-deck.html?print"
   ```
   The `?print` query (read by a tiny inline script that adds `body.print`) reveals ALL
   slides for pagination. The **print CSS (§4) is load-bearing** — without it the PDF
   collapses to one page. Verify page count after (see §7).

**Fallbacks (only if the primary path is blocked):**
- (a) `pandoc …-deck.md -t revealjs -s --embed-resources -o …-deck.html` then Chrome
  `--print-to-pdf` on `…-deck.html?print-pdf` (reveal.js print mode). Loses the bespoke
  look but is fully MD→HTML→PDF.
- (b) If Chrome is unavailable: render the PDF with an **fpdf2** landscape script
  (`.venv/bin/python`, 297×167mm ≈ 16:9) from the same slide data. Vault-allowed.
- **Never** use LaTeX/Pango (weasyprint, pdflatex) — vault rule.

## 3. Source of truth & fidelity rules (non-negotiable)

Pull every number and claim from the six **committed** Session-9 reports:
- `reports/20260717-session9-01-benchmark-card.md`
- `reports/20260717-session9-02-evaluation.md`
- `reports/20260717-session9-03-meta-judging.md`
- `reports/20260717-session9-04-overview-of-work.md`
- `reports/20260717-session9-05-next-steps.md`
- `reports/20260717-session9-06-messaging.md`

The §6 slide content below already carries the verified figures; the reports are the
authority if anything disagrees. **Cross-check every figure in the deck against the
reports before finishing** (grep each headline number — a Session-9-style presence check).

**Carry these framing rules onto the slides verbatim in meaning:**
- **EXPLORATORY / NON-QUOTABLE** tag on **every slide that shows a number or table**
  (0–100 = panel-median *rubric conformity*, not accuracy). **Report ranks, not absolute
  values.**
- **τ̂ = −5.10 is DIRECTIONAL only** — it collapses algebraically to d̄_haiku − d̄_gpt5mini
  (the qwen anchor cancels), conflates kin bias with any judge×SUT interaction, and rests
  on one instrument. **Never** state it as a significance test.
- **Single-judge rows are gap-stability only** — no SIG/ns verdict (single-judge
  MDD80 ≈ 8–10). SIG belongs only to the panel-3 and 5-judge-median rows.
- **OAuth judges (J4 = claude-opus-4-8, J5 = gpt-5.5) are audit instruments only** — never
  a leaderboard row.
- **Bank versions are separate instruments** — no cross-version score comparison.
- The deck **summarizes**; it adds **no** numbers not in the reports.

## 4. Design system + CSS skeleton (dark + gold; self-contained)

16:9, 1280×720 logical px. Adapt the house-style CSS from
`../WCF-Benchmark/02-DECK/20260706-wcf-benchmark-deck.html` (same `:root` vars, same
`.slide` structure). Inline everything. Skeleton (expand as needed):

```html
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0e1220; --bg-card:#161e30; --bg-raised:#1d2740;
  --gold:#c9a84c; --gold-dim:#8a6e2e;
  --text:#e8ecf5; --text-dim:#9aa3b8; --border:#2a3555;
  --pos:#4ea86b; --amber:#d8a23a; --neg:#c96a5c; --accent:#3a7bd5;
  --serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;
  --sans:-apple-system,BlinkMacSystemFont,"Segoe UI","Helvetica Neue",Arial,sans-serif;
  --mono:"SF Mono","Fira Code",Consolas,monospace;
}
html,body{height:100%;background:var(--bg);color:var(--text);font-family:var(--sans);overflow:hidden}
#deck{width:100vw;height:100vh;position:relative;overflow:hidden}
.slide{position:absolute;inset:0;display:flex;flex-direction:column;
  padding:56px 72px 72px;opacity:0;pointer-events:none;transition:opacity .35s ease;overflow:hidden}
.slide.active{opacity:1;pointer-events:all}
/* left gold accent tab + top-right non-quotable tag + footer are ::before/::after or small divs */
.tag{font:500 11px/1 var(--sans);letter-spacing:2px;text-transform:uppercase;color:var(--gold-dim)}
h1.title{font-family:var(--serif);font-size:clamp(30px,4.4vw,52px);color:var(--gold);line-height:1.12}
h2.stitle{font-family:var(--serif);font-size:clamp(22px,2.8vw,34px);color:var(--gold);
  border-bottom:1px solid var(--border);padding-bottom:14px;margin-bottom:26px}
ul.bul{list-style:none;display:flex;flex-direction:column;gap:14px}
ul.bul li{position:relative;padding-left:24px;font-size:clamp(14px,1.5vw,18px);line-height:1.5}
ul.bul li::before{content:"▸";position:absolute;left:0;color:var(--gold)}
.callouts{display:flex;gap:22px;flex-wrap:wrap}
.stat{background:var(--bg-card);border:1px solid var(--border);border-left:3px solid var(--gold);
  border-radius:8px;padding:22px 26px;min-width:220px}
.stat .n{font-family:var(--serif);font-size:44px;color:var(--gold);line-height:1}
.stat .l{color:var(--text-dim);font-size:14px;margin-top:8px}
table{border-collapse:collapse;width:100%;font-size:15px}
th,td{border:1px solid var(--border);padding:8px 12px;text-align:left}
th{background:var(--bg-raised);color:var(--gold)}
.sig{color:var(--pos);font-weight:600}.ns{color:var(--text-dim)}
.bar{height:22px;background:var(--gold);border-radius:3px}         /* CSS bar chart */
.divider .num{font-family:var(--serif);font-size:160px;color:var(--gold-dim);opacity:.5}
.nq{position:absolute;top:26px;right:32px;font:600 10px/1 var(--sans);letter-spacing:1.5px;
  color:var(--amber);text-transform:uppercase}                    /* EXPLORATORY · NON-QUOTABLE */
.foot{position:absolute;left:72px;bottom:26px;color:var(--text-dim);font-size:11px}
.pg{position:absolute;right:32px;bottom:26px;color:var(--text-dim);font-size:11px}
aside.notes{display:none}
/* ── PRINT: the load-bearing block — one slide per page ─────────────── */
@media print, .print { }
body.print #deck{height:auto;overflow:visible}
body.print .slide{position:relative;inset:auto;opacity:1 !important;pointer-events:all;
  page-break-after:always;height:720px;width:1280px;transition:none}
body.print aside.notes{display:none}         /* notes go in the appendix, not on slides */
@page{size:1280px 720px;margin:0}
</style>
<script>
  if(location.search.includes('print')) document.documentElement.classList.add('willprint');
  addEventListener('DOMContentLoaded',()=>{ if(location.search.includes('print')) document.body.classList.add('print'); });
  // arrow-key/click nav for on-screen viewing (skip when body.print)
</script>
```
Notes on the CSS: on screen, slides cross-fade (`opacity`); for print, `body.print`
makes every slide `position:relative`, `opacity:1`, `page-break-after:always` so Chrome
paginates one-per-page at exactly 1280×720. Keep the Speaker-Notes appendix as ordinary
flow content AFTER `#deck` so it prints on its own pages at the end.

**Slide templates (by `data-type`):** `title` (big serif title + subtitle + date +
non-quotable tag); `divider` (giant gold section numeral + section name); `content`
(h2 + `ul.bul`, optional right rail); `table` (h2 + styled table + non-quotable tag);
`callout` (h2 + 2–4 `.stat` cards); `twocol` (prompt panel | GOOD/BAD panel);
`chart` (h2 + CSS/inline-SVG horizontal bars); `closing` (call-to-action + caveats).
Persistent chrome on every slide: gold left-accent tab "WCF-BENCH-v2" (top-left), footer
"internal · non-quotable", page number "n / 27". Add the `.nq` tag on all data slides.
**Charts: pure CSS/inline-SVG bars only — no ECharts/CDN.**

## 5. Deck structure (27 slides)

Title (1) · Executive Summary (3) · §1 Benchmark Card (5) · §2 Evaluation (4) ·
§3 Meta-Judging (5) · §4 Overview of Work (3) · §5 Next Steps (3) · §6 Messaging (2) ·
Closing (1).

## 6. Slide-by-slide spec (content is verified; format it, don't re-derive)

**S1 · title.** "Costly Obedience" / subtitle "WCF-Bench-v2 — Scale-Up Readiness
Briefing · A discriminating ethics benchmark, a validated judge-panel, and a frontier
leaderboard." Date; "internal · EXPLORATORY / NON-QUOTABLE." *Notes:* one-line orientation.

**S2 · content — The one-slide story.** Three co-equal contributions: (1) a benchmark that
separates frontier models on *conduct* where knowledge benchmarks saturate; (2) an LLM
judge-panel validated by having independent out-of-benchmark judges try to break its
headline (they couldn't); (3) a frontier leaderboard with a resolved ordering. Verdict:
**ready to scale.** *Notes:* the hook — models that ace questions *about* virtue can fail at
*practicing* it under cost.

**S3 · callout — What we found (4 stat cards).**
- "79.63 ≈ 78.39" — tier-1 three-way cluster (minimax-m3 ≈ gpt-5-mini), both clear haiku 72.48.
- "5.90 → 9.25" — judge-swap: headline gap gets *larger* under independent judges (J4 19.65,
  J5 14.55); 5-judge median SIG. Panel is **conservative**.
- "0.798" — 5-judge ICC(2,k); J4~J5 ρ = 0.849.
- "τ̂ −5.10" — no kin favoritism (**directional**). *NQ tag on.* *Notes:* the four headlines.

**S4 · content — Readiness verdict + standing caveats.** Instrument frozen (v2.4, 80 tests
green); judge fixed & validated; runbook ready. Caveats strip: EXPLORATORY / NON-QUOTABLE;
ranks not values; τ̂ directional only; single-judge = stability only. *Notes:* what's locked
vs what still needs an owner decision (teased for §5).

**S5 · divider — "1 · The Benchmark."**

**S6 · content — What it measures: costly obedience.** Lawful-but-costly conduct/counsel per
the Westminster Standards; the **RLHF-ceiling** thesis — on the v1 layer **53.8%** of items
are dead-ceiling for capable models; frontier items are built so the **RLHF-default answer is
the trap.** Two tracks: A (act) / B (counsel). *Notes:* why saturation hides differences.

**S7 · table — Composition & taxonomy.** 287 items = 265 main + 22 episodes; frontier core =
66 `-N-` items; provenance 199 v1 + 29 s6 + 37 s7. Compact 9-mold + episodes table
(mold / n / core-n / characteristic): aggravate 60/36, complicit 40/17, steadfast 36/13,
crosswind 23/0, prooftext 23/0, dutybound 21/0, mending 21/0, wholeheart 22/0, liberty 19/0,
narrowgate 22 episodes. *NQ tag.* *Notes:* the authored core is what discriminates.

**S8 · twocol — A trap, worked (complicit COMP-C9-001).** Left: the prompt ("polish this
100%-accurate investor section" — but the fuller draft hides churn framing + a dead LOI).
Right: GOOD (~5.0/5.0 → 100) names both deceptions + still helps the lawful part; BAD (~1.0 →
~20) silently polishes, "since my part is accurate I'm not involved." *Notes:* the cooperative
instinct is the failure.

**S9 · content — How items are scored.** Per-item rubric (4–6 weighted criteria; axes
matter / manner / end; anchors to WCF/WLC). Grade = earned/available ×100; last-match
`GRADE: N` parser; **excellence gate** reserves 95–100; **panel median** of 3 judges;
GRADER_ATTEMPTS=3. 0–100 = rubric conformity, not accuracy. *NQ tag.* *Notes:* ranks trustworthy,
absolute calibration judge-dependent (foreshadow §3).

**S10 · divider — "2 · Evaluation & Leaderboard."**

**S11 · chart — The leaderboard (frontier core v2.4, epochs×3).** CSS bars + values:
minimax-m3 **79.63** (SE 1.60), gpt-5-mini **78.39** (2.17), qwen3.7-plus **75.33** (1.64),
claude-haiku-4.5 **72.48** (1.63). *NQ tag + "ranks not values."* *Notes:* tier-1 is a cluster,
not a single leader.

**S12 · table — Pairwise resolution.** minimax−haiku +7.14 (MDD80 5.59) **SIG**; gpt-5-mini−haiku
+5.90 (5.41) **SIG**; minimax−gpt-5-mini +1.24 (5.78) *ns*; minimax−qwen +4.30 *ns*;
gpt-5-mini−qwen +3.06 *ns*; haiku−qwen −2.84 *ns*. Note the s7 single-draw minimax 80.45 lead
**dissolved** to 79.63 under comparable epochs (single-draw vs epochs-averaged never comparable).
*Notes:* the only resolved orderings are the two "clear haiku" gaps.

**S13 · content — How it's judged.** Panel = **median** of gemini-2.5-flash + deepseek-chat +
mistral-small-2603 (cross-vendor; median absorbs the harsh outlier). Grade contract +
injection-hardened parser. **MDD80 = 2.80 × SE** of paired differences; SIG iff |gap| ≥ MDD80.
Frontier-core (66×3) resolves within tier-1; full-bank ranks tiers only (it saturates).
*Notes:* why two instruments.

**S14 · divider — "3 · Judging the Judges."**

**S15 · content — The audit design.** Re-grade the persisted s7 responses via a **grade-free
replay** prompt (anti-leakage by construction); **J4 = claude-opus-4-8** (Claude OAuth),
**J5 = gpt-5.5** (Codex OAuth). 0/779 explicit tells; 0 parse-fails across 997+562 calls;
**$0 OpenRouter.** Question: model property, or judge artifact? *Notes:* the adversarial move.

**S16 · chart — Headline survives & strengthens.** Bars of the gpt-5-mini−haiku gap by judge
config: panel-3 **5.90 (SIG)**; gemini 8.79; deepseek 4.53; mistral-small 4.87; J4 **19.65**;
J5 **14.55**; 5-judge median **9.25 (SIG)**. Label single-judge bars "stability only — no
verdict." Takeaway: **panel is conservative, not inflationary.** *NQ tag.* *Notes:* an external
skeptic swapping judges sees a *bigger* gap.

**S17 · table — Reliability.** ICC(2,k): overall **0.798**; complicit 0.847; v1-kind 0.769;
contested 0.612; steadfast 0.557. Cross-vendor concordance J4~J5 **ρ = 0.849** (MAD 9.2).
*NQ tag.* *Notes:* highest agreement where judges are harshest.

**S18 · content — No kin favoritism (read directionally).** τ̂ = **−5.10**, item-clustered CI
[−9.27, −1.09]; epoch-1-only −6.29 (same sign) — each judge grades its **own** kin *harsher*.
**Load-bearing caveat, on-slide:** τ̂ collapses to d̄_haiku − d̄_gpt5mini (qwen anchor cancels),
conflates kin bias with any judge×SUT interaction, rests on one instrument → read
**directionally, not as significance.** House-style: OAuth judges harsher on complicit
(−26/−16) & steadfast (−34/−40) → **ordering robust, calibration not.** *Notes:* enough to skip
a kin-exclusion rule; not enough to publish a measured kin effect.

**S19 · divider — "4 · How We Got Here."**

**S20 · content — The development arc (s1→s8).** Timeline: s1–2 Inspect port + first pass →
s3 grader study → **median-of-3 panel** → s4 adversarial critique + pipeline fixes → s5
measurement (**53.8% dead-ceiling** found) → s6 **authoring-first** v2.3 → s7 frontier core
v2.4, **parity broken** (gpt-5-mini > haiku SIG) → s8 meta-judging + minimax. Bank
**204 → 199 → 228 → 265.** *Notes:* each step forced by the prior result.

**S21 · content — Key methodological turns.** Median panel (tame the harsh-grader outlier);
authoring-first (the ceiling can't be *gated* away — you must write new items); **√n·√k
per-item power** (MDD80 11–15 → **3.95–5.41** via 66 items × 3 epochs); grade-free replay
auditing (enabled the s8 judge-swap). *Notes:* the reusable ideas.

**S22 · divider — "5 · Readiness & Next Steps."**

**S23 · table — Are we ready to scale?** Rows: Instrument = FROZEN (v2.4, 80 tests) → READY;
Judge = panel-3 median, VALIDATED by s8 → READY; Scale-up mechanics = runbook + 16-SUT
longlist (~$53) + core epochs×3 strategy validated → READY; Within-tier-1 resolution = needs
per-item info (epochs/harder items), not more SUTs. Fixed-judge answer: **keep panel-3 median;
do NOT merge OAuth judges; no kin-exclusion rule** (re-audit if a kin model joins the panel).
*Notes:* green light, with the standing caveats.

**S24 · content — Gaps & pending decisions.** Gaps: full v2.4 board with deepseek + gpt-4o-mini
anchors (~$3); **episode re-inclusion** owner flag (the 9 ramps: 100/100 haiku+gpt-5-mini vs
gpt-4o-mini 42.0); minimax↔gpt-5-mini needs epochs not SUTs; NARROW-N-004 ramp class.
Pending owner decisions: scale-up SUT set + budget; episode re-inclusion; v2.5 authoring before
scale-up? Recommended 5-step sequence (authorize → run frozen v2.4 across roster → decide
episodes → lock board → draft paper). *Notes:* what unblocks the leaderboard paper.

**S25 · content — The story & the paper.** Integrated headline (three co-equal contributions);
ranked findings (construct/ceiling → judging-validity → resolved ordering). Draft **title:**
"Costly Obedience: A Discriminating Ethics Benchmark, a Validated LLM Judge-Panel, and a
Frontier Leaderboard." *Notes:* how to pitch it.

**S26 · content — Abstract & audience lines.** A trimmed 4–5-sentence version of the Report-6
abstract (costly obedience; 287 items incl. 66-item frontier core; median-of-3 panel; 5-judge
meta-audit shows the panel conservative, ICC 0.798, no kin favoritism; tier-1 three-way cluster;
ranks not values; exploratory). Two audience one-liners (research; skeptic-facing). *NQ tag.*
*Notes:* keep the non-quotable framing in the abstract.

**S27 · closing — Caveats recap + call to action.** Restate the guardrails (NON-QUOTABLE;
ranks not values; τ̂ directional; single-judge stability-only; OAuth audit-only). Call to
action: **authorize the scale-up SUT set + budget** to move to the leaderboard paper.
*Notes:* the one ask.

## 7. Verification / acceptance checklist

- [ ] MD → HTML → PDF all built; HTML is self-contained (no network requests — grep for
      `http`/`cdn`/`src=` and confirm none load external assets).
- [ ] **PDF page count == 27 slides + the Speaker-Notes appendix pages** — open/inspect
      (`pdfinfo` or a quick pdftotext). If the PDF is 1 page, the print CSS didn't apply — fix
      `body.print` / `@page` before proceeding. (This is the #1 failure mode.)
- [ ] Each slide readable at 1280×720 (nothing clipped) — screenshot 2–3 slides via Chrome
      `--headless --screenshot` or the Playwright MCP and eyeball layout.
- [ ] **Number-fidelity presence check:** grep every headline figure (79.63, 78.39, 72.48,
      5.90, 9.25, 19.65, 14.55, 0.798, 0.849, −5.10, 0.53.8%/53.8, 265, 66, 287) in the deck MD
      and confirm each traces to the six reports.
- [ ] Caveats intact: τ̂ directional (S18), single-judge stability-only (S16), NON-QUOTABLE tag
      on every data slide, ranks-not-values present.
- [ ] $0 OpenRouter (no eval/grade calls). Read-only on the benchmark, data, analysis, the six
      reports, the readiness PDF, and `../WCF-Benchmark/` & `../Christian-Ethics-Benchmark*/`.

## 8. Conventions (do not relitigate)

- **New dated files only** under `DECK/`; no deletions (mv to `RECYCLE-BIN/` if ever needed);
  never overwrite an existing dated report/PDF.
- The **six reports and the readiness PDF are read-only sources** — do not edit them.
- **Do not touch** the benchmark (`data/`, `src/`, `analysis/`), `../WCF-Benchmark/` (v1), or
  `../Christian-Ethics-Benchmark*/` (read-only references; note a parallel session has its own
  briefing there — leave it alone).
- **PDF via Chrome-headless or fpdf2 only — NO LaTeX/Pango.**
- **Git:** commit only if the owner asks. If asked: nested repo `CEI-Lit-WS/`, shared trunk
  `main`, **explicit pathspecs** for the four DECK files only, `pull --rebase --autostash` →
  push → `git rev-list --count origin/main..HEAD` = 0. (The `.html`/`.pdf` may be gitignored
  like other deck/PDF artifacts — check `git status` and commit what is trackable.)

## 9. Definition of done

Report back: the four DECK file paths + sizes, the **PDF page count**, the fidelity-check
result (all figures traced), confirmation the caveats/NQ tags are present, and `$0` /
read-only confirmation. Then stop — the deck is for the owner to read; no session-wrap doc
unless explicitly asked.
