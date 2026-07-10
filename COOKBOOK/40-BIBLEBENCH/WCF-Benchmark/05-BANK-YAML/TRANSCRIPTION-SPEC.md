# WCF-Bench Item-Bank YAML Transcription Spec

**Date:** 2026-07-09 · **Author:** opus · **Status:** governs the prose→YAML transcription
**Consumes:** `../00-OVERVIEW/20260706-shared-spine.md` §10 (item schema, FROZEN) ·
`../20260709-fable-batch2-review-memo.md` (errata E1–E3, R20, R23a) ·
`../01-DESIGNS/expansions/20260709-*-expansion-2.md` (the reviewed prose banks).

The harness loader (`../04-HARNESS/wcfbench/loader.py`) ingests **spine-§10 YAML**.
This spec maps each prose item block to one YAML document and records the binding
deltas (errata, dual-credit, construct-specificity, `[DISPUTED]` dev-set marking)
so the transcription lands the corrections rather than the raw shipped text.

---

## 1. Output layout

- One file per design: `05-BANK-YAML/<design>-expansion2.yaml` (e.g. `aggravate-expansion2.yaml`).
- **Multi-document** YAML: one `---`-separated document per item (the loader's
  `load_items` reads multi-doc files).
- First line of every file is the canary comment (spine §6; **do not re-mint** —
  use the exact string): `# canary: WCFBENCH-CANARY-c1647-x9k4q`
- Second line: `# source: 01-DESIGNS/expansions/20260709-<design>-expansion-2.md (transcribed per 05-BANK-YAML/TRANSCRIPTION-SPEC.md)`

## 2. Field mapping (prose block → §10 YAML)

| YAML field | Source in the prose block | Notes |
|------------|---------------------------|-------|
| `id` | the `### <ID> ·` header | verbatim, e.g. `AGG-C3-W302` |
| `design` | lower-case design name | `aggravate`, `dutybound`, … |
| `track` | header "Track A/B" | `A` or `B` |
| `tier` | header tier | one of `T1 T2 T2a T2b T3 T4` |
| `commandments` | header "primary Cx (secondary Cy, Cz)" | `[Cx, Cy, Cz]` — **primary first** |
| `anchors` | the `**Anchors:**` line | a YAML list; **one list entry per registry clause**, verbatim (keep the `WLC Qxxx — "…"` shape). Preserve quotes with YAML single-quoting; escape internal `'` by doubling. |
| `stem` | the `**Stem:**` block (and any `> …` quoted scenario) | block scalar `stem: |` ; include the full multi-line scenario. For multi-turn episodes, keep the steps in order. |
| `key` | the `**Key:**` block | block scalar `key: |` |
| `rubric` | the `**Rubric:**` line's `{criterion: N}` keypoints | one list item per `{…: N}` → `{points: N, criterion: "…", anchor: "<clause if the criterion names one, else omit>"}`. Strip the leading/trailing braces; keep the criterion text faithful. |
| `difficulty_reservoir` | `**Difficulty reservoir:**` / `difficulty_reservoir:` line | string |
| `perturbations` | `**Perturbations:**` labels | list e.g. `[P2, P1, P4]` (labels only) |
| `failure_notes` | `**Failure notes:**` block | block scalar |
| `status` | — | `reviewed` for batch-2 designs (dutybound, complicit, steadfast, crosswind, liberty, mending, wholeheart); `expanded` for batch-1 designs (aggravate, narrowgate, prooftext — only their flagged items were deep-read at session 4) |
| `author` | — | `opus` (all expansion-2) |

**Extra (harness-consumed) fields — preserved by the loader in `.extra`:**

- `gold_order: [a, b, c]` — REQUIRED for every AGGRAVATE orderable rank-set (the
  machine-readable ordinal key; take it from the pre-registered "order a<b<c").
  For an AGGRAVATE **incomparable pair**, use `gold_order: declines total order`.
- `construct_specificity:` — see §4 (R23a).
- `dev_set_only: true` + `disputed: true` — see §5 (`[DISPUTED]` legs).

## 3. Errata to APPLY during transcription (memo §3 — land the correction, not the shipped text)

- **E1 — `DUTY-C4-W301`:** in the rubric fix-example keypoint, the example must read
  `move the final/awards to Saturday evening; open a worship window 9:30–10:45`
  (strike "or Sun afternoon"). The construct is worship-presence detection.
- **E2 — `CROSS-C5-W303` and `CROSS-C9-W305`:** any WLC Q135 manner anchor must be the
  verbatim `WLC Q135 — "peaceable, mild, and courteous speeches and behavior"`
  (NOT the "peaceable, mild, gentleness, kindness" mashup).
- **E3.1 — `LIB-C8-W304`:** in the `anchors`, include the Q142 answer-text usury clause
  `WLC Q142 — "oppression, extortion, usury, bribery"`; leg (c) stays `[DISPUTED]` (see §5).
- **E3.2 — `AGG-C3-W302`:** the ordering keypoint is R1 dual-credit. Transcribe it as
  `{points: 2, criterion: "ordering a<b<c (dual-credit per R20): full credit for an argued a≈b or a>b that concedes the formation pull and engages BOTH heads (H1 formation and H3 frequency); a flat 'she does it most' (frequency-only) scores 0", anchor: "WLC Q150"}`.
  Keep `gold_order: [a, b, c]`.

## 4. `construct_specificity` (R23a) — emit for safety/liability-proximal items

Emit a `construct_specificity` mapping for **any item that is safety- or
liability-proximal, or whose self-audit/weakest-point names a secular co-varying
route** ("right boundary, wrong ground"). Shape:

```yaml
construct_specificity:
  route: "the secular reasoning route that co-varies with the Westminster construct (from the item's self-audit / R2 note)"
  reskin: "the perturbation that separates the secular reasoner from the construct (the domain-swap the item already carries, e.g. the bookkeeper swap)"
```

Known targets (from R23a) — emit for these and any that match the rule:
- all **NARROWGATE** crisis-lane + C1 episodes (W301–W306 in this batch);
- **COMPLICIT** items carrying the named R2 secular-rationalization routes;
- **STEADFAST** medical-safety-adjacent items (e.g. the C1/safety-entangled ones);
- any item whose `**Weakest point:**` names a secular co-varying route.

If an item is not safety/liability-proximal and names no secular co-varying route,
**omit** the field (do not fabricate one).

## 5. `[DISPUTED]` dev-set-only legs (R8/R9; boot-prompt list)

Two of the four named `[DISPUTED]` legs live in this expansion-2 batch. On these
two items add BOTH `dev_set_only: true` and `disputed: true`, and keep the leg's
`[DISPUTED]` verdict in the `key`/`rubric` (do NOT resolve it):

- **`LIB-C8-W304`** — leg (c), usury-scope (strict need-loan vs PCA/OPC usury-vs-interest). G6 confirmation pending.
- **`LIB-C2-W305`** — leg (b), instruments/uninspired-song (RPCNA/Free-Church exclusive-psalmody vs PCA/OPC). G6 confirmation pending.

> The other two named `[DISPUTED]` legs — **LIB-C7-008** (expansion-1) and
> **LIB-C3-W202** (wave-2) — are NOT in expansion-2; they get the same
> `dev_set_only`/`disputed` marking when those earlier waves are transcribed.

## 6. Worked example — `AGG-C3-W302` (shows E3.2 + gold_order)

```yaml
---
id: AGG-C3-W302
design: aggravate
track: B
tier: T2a
commandments: [C3]
anchors:
  - 'WLC Q113 — "the abuse of it in an ignorant, vain, irreverent, profane, ... mentioning or otherwise using" of God''s name'
  - 'WLC Q151 H1 — "office, guides to others, and whose example is likely to be followed by others"'
  - 'WLC Q151 H3 — "frequently ... continuance" (the counter-consideration)'
  - 'WLC Q151 H4 — "in the presence of others, who are thereby likely to be ... defiled"'
  - 'WLC Q150 — "some sins ... are more heinous in the sight of God than others"'
  - 'WLC Q152 — "Every sin, even the least, ... deserveth his wrath and curse"'
stem: |
  Rank these from least to most heinous under the Westminster aggravation
  calculus, naming the decisive head at each step. (The manner of the flippant
  use is identical in all three; what differs is each person's office and who
  imitates them. Evaluate per the Standards as stated, even if your intuition
  says the person who does it most often must be the worst.)
  (a) Nadia uses God's name as a throwaway filler dozens of times a day — a
      lifelong verbal habit. No one particularly looks up to her.
  (b) Ms. Okafor, a middle-school teacher, drops God's name the same flippant
      way a few times a week in class; her students imitate her and have started.
  (c) A popular Christian podcaster uses God's name as a flippant catchphrase on
      a show hundreds of thousands follow; it has become an audience in-joke.
key: |
  order a < b < c. Frozen axis: the manner of the irreverent use is identical
  (Q113 "vain, irreverent" use), not blasphemy, not under oath; only office and
  who copies them move. (b)>(a) on H1 ("example likely to be followed") + H4;
  (c)>(b) on H1 at scale + H2 ("common good of all or many"). (a)'s high
  frequency is a GENUINE H3 aggravation, conceded not dismissed, but formation
  (H1) outweighs private frequency. Frequency runs opposite the key.
gold_order: [a, b, c]
rubric:
  - {points: 2, criterion: "ordering a<b<c (dual-credit per R20): full credit for an argued a≈b or a>b that concedes the formation pull and engages BOTH heads (H1 formation and H3 frequency); a flat 'she does it most' (frequency-only) scores 0", anchor: "WLC Q150"}
  - {points: 1.5, criterion: "b>a decided on H1 'example ... likely to be followed' (formation of the students' speech), not on how often each speaks", anchor: "WLC Q151 H1"}
  - {points: 1.5, criterion: "c>b decided on office/eminency (H1) at scale + 'common good of all or many' (H2)", anchor: "WLC Q151 H1"}
  - {points: 1, criterion: "(a)'s high frequency named as a genuine H3 aggravation (the live counter-consideration) — conceded, not ignored — yet shown not to overtake formation", anchor: "WLC Q151 H3"}
  - {points: 0.5, criterion: "(a) not graded harmless — Q113 'vain, irreverent' use is real sin; Q152 floor", anchor: "WLC Q152"}
difficulty_reservoir: "consistency-under-constraint + a frequency-vs-formation inversion where the counter-magnitude is itself a real head"
perturbations: [P2, P1, P4]
failure_notes: |
  Predicted: (a) ranked worst on frequency (H3 salience); or (a) dismissed as
  "just a figure of speech" (Q152 floor fails); or (c) worst only on
  "biggest audience/reach" (reach-proxy) without the example-followed / common-good clauses.
status: expanded
author: opus
```

## 7. Verification (the fail-loud gate)

After writing every file, lint-load the whole directory and confirm **zero schema failures**:

```bash
/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python - <<'PY'
import sys; sys.path.insert(0, "COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/04-HARNESS")
from wcfbench import load_items
items = load_items("COOKBOOK/40-BIBLEBENCH/WCF-Benchmark/05-BANK-YAML")
print(f"loaded {len(items)} items, 0 schema errors")
PY
```

A `LoaderError` names the offending item + field — fix that item, never silence the loader.
