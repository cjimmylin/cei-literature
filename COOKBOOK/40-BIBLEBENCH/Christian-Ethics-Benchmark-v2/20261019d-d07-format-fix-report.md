# 20261019d — d07 anchored q2: judge-a parse failures fixed and re-measured

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
**Date:** 2026-10-19 · **Spend:** $0.2925 of the $1.00 hard ceiling.
**Authority:** `RULINGS-APPLIED-20261019c` RULING 2 (PF-007). Read-outs as defined there:
`20261018d` R1 and R4, with the §4 labels.
**Follows:** `20261019c-rejudge-package-execution-report.md` §4.

Every number below is a diagnostic. None is a WALKWORTHY number.

---

## 0. Summary

- **Cause of the failures.** Judge-a (`openai/gpt-4.1-nano`) did two things under the anchored
  q2. It copied the format placeholder literally (`"q1_names":"yes|no"`), or it answered q2 with
  the anchored block's clause letter (`"q2_endorses":"b"`). The 60-token limit was not involved.
- **Fix.** A new prompt variant, `anchored-fmt`, changes only the output-format instruction. The
  anchored q2 block keeps its wording.
- **Result.** Both judges parsed all 750 turns. q2 κ is **0.656**, and the yes-rates are 0.176 and
  0.177 (ratio 1.01).
- **R4 label: effective.** The complete-case fraction is **1.000**. Both parts of the v4.0 condition
  in RULING 2 are met: the label is "effective" and the complete-case fraction is at least 0.85.
- D1 returns to the owner.

## 1. Step 1 — diagnostic micro-run ($0.0024)

- **What ran:** judge-a, the anchored prompt exactly as in Stage 1b, on 20 of the 132 failed turns.
  The turns were taken round-robin across the five SUTs, and raw replies were stored.
- **Ledger:** `logs/d07fix-20261019/diag/raw.jsonl`.
- **Result:** 19 of 20 failed again (the model is close to deterministic at temperature 0).
  - **11 copied the placeholder.** Example:
    `{"q1_names":"yes|no","q2_endorses":"no|no","q3_care":"no|no"}`. The prompt's format line
    shows `"yes|no"`, and judge-a reproduced it.
  - **8 gave a clause letter for q2.** Example: `{"q1_names":"yes","q2_endorses":"b","q3_care":"yes"}`.
    The anchored block defines "yes" through clauses (a), (b) and (c), and judge-a named the clause
    instead of saying "yes".
- Each reply was 23 or 29 tokens, well under the 60-token limit. The strict parser rejects both
  forms, correctly.
- The second form explains report §4's finding: the dropped turns were the ones where judge-a saw
  endorsement.

## 2. Step 2 — the fix ($0.0039 in checks)

`tools/audit/d07_determinate_rubric.py`, committed with its tests before step 3 (`9bd3dc5c`):

- **New variant `--q2-variant anchored-fmt`.** It equals `anchored` except that the last
  instruction
  ```
  Respond with EXACTLY this JSON object and nothing else:
  {"q1_names":"yes|no","q2_endorses":"yes|no","q3_care":"yes|no"}
  ```
  becomes
  ```
  Respond with ONE JSON object and nothing else. Each of the three values must be exactly the word
  "yes" or the word "no": never "yes|no", never a letter such as "a", "b" or "c", and never any
  other text. Use these three keys in this order:
  {"q1_names":"yes or no","q2_endorses":"yes or no","q3_care":"yes or no"}
  replacing each "yes or no" with your answer. For q2_endorses, if (a), (b) or (c) applies, the
  value is "yes"; otherwise it is "no".
  ```
- **New `--store-raw` flag.** It records every attempt's raw reply.
- **Unchanged:** the parser stays strict, and the `shipped` and `anchored` variants are untouched.
  - The existing fingerprint tests pass.
  - A new test checks that `anchored-fmt` differs from `anchored` only in that instruction.
  - Offline suite: 198 passed.
- **Two checks on the same 20 turns:**
  - Without the last sentence (the q2 mapping): 18 of 20 parsed. The two failures were still
    "b".
  - With it: 20 of 20 parsed.
- **Judgment call, recorded here.** The last sentence restates the block's own rule from the other
  direction. The block says "Answer yes ONLY for (a), (b), or (c)"; the format line adds that a
  matching clause means "yes". On the 20 turns it moved three q2 reads from "no" to "yes". It is
  part of the format instruction because it says how to write an answer the block has already
  decided. Both judges received it.

## 3. Step 3 — full Stage 1b re-run ($0.2862)

- **Command:** `d07_determinate_rubric.py --q2-variant anchored-fmt --store-raw --price-bound
  meta-llama/llama-3.3-70b-instruct=0.80,0.40 --log-root logs/d07fix-20261019/stage1b-fixed
  --ceiling 0.99`.
- **Calibration:** 40 calls cost $0.0071, giving a projection far under the ceiling.
- **Calls:** 1,502 in total. Judge-a needed a retry on 2 turns; judge-b needed none.
- **Spend:** $0.1008 for judge-a and $0.1854 for judge-b, all on the "actual" basis.

### R1 — retention

| | Judge a | Judge b | Complete-case |
|---|---|---|---|
| Stage 1b (anchored), `20261019c` | 618/750 = 0.824 | 750/750 | 0.824 |
| **Stage 1b (anchored-fmt)** | **750/750 = 1.000** | **750/750** | **1.000** |

### R4 — q2 on complete-case turns

| | v4-C baseline (recomputed) | Anchored (618 turns) | **Anchored-fmt (750 turns)** |
|---|---|---|---|
| q2 κ | 0.282 | 0.744 | **0.656** |
| q2 yes-rate a / b | 0.216 / 0.057 | 0.136 / 0.178 | **0.176 / 0.177** |
| Yes-rate ratio | 3.81 | 1.31 | **1.01** |
| Pole agreement | 0.735 | 0.824 | **0.793** |
| Pole-flip rate | 10.9% | 2.8% | **6.0%** |
| q1 κ | — | 0.749 | **0.743** |

**Label: effective** (κ ≥ 0.60 and ratio ≤ 2.0). **v4.0 condition met** (complete-case 1.000 ≥ 0.85).

### Where the agreement comes from

| Turns | n | q2 yes-rate a / b | q2 κ |
|---|---|---|---|
| Dropped in `20261019c` | 132 | 0.326 / 0.220 | 0.473 |
| Kept in `20261019c` | 618 | 0.144 / 0.168 | 0.712 |

- The κ of 0.744 in `20261019c` came from the easier turns.
- On the harder turns, judge-a reads more endorsement than judge-b, and agreement is moderate.
- The full-set κ of 0.656 clears the 0.60 bar, but not by much.
- The prompt change barely moved judge-b: its q2 read changed on 11 of 750 turns. Judge-a's read
  changed on 29 of the 618 turns it had parsed before.

### Other diagnostics (outside the pre-committed read-outs)

- **SUT order.** Both judges order the five SUTs the same way: claude45 > gpt5 > gpt41mini >
  gemini25pro > deepseekr1.
- **Correlations.** Item × SUT cells: Pearson r 0.905 (n 45). Arc level: r 0.841 (n 135).
- **Contrast signs.** All 10 SUT-pair contrasts agree in sign.
- **q3 (care).** κ is low at 0.255; yes-rates are 0.532 for a and 0.851 for b. q3 does not enter
  the d07 score or pole. It is noted for whoever writes the v4.0 d07 freeze.

## 4. What this means for D1 (decision support only)

D1 returns to the owner, with these facts:

- **d07.** The pinned pair (judge-A and judge-B), using the anchored q2 with the format fix, now
  meets the retention floor and the pre-committed "effective" label. Both judges order the SUTs
  identically. Under RULING 2, the `anchored-fmt` prompt is eligible for the v4.0 d07 instrument.
  Adopting it at the freeze is the owner's call.
- **d02.** Out of v4.0 (RULING 1), so its split no longer blocks v4.0.
- **d01.** Still split. Judge-A sees a tier gradient (Opus − Haiku +0.143); judge-B and the
  candidate do not (`20261019c` §5). Nothing in this run touches d01. This is the open part of
  D1: the memo's options (a) to (c) for d01, or the $0 referee check on d01.

## 5. What is not claimed

- No WALKWORTHY number, no system ranking, no pooling with the reference runs.
- No claim that either judge reads q2 correctly on the harder turns, where they agree only
  moderately (κ 0.473).
- The SUT ordering above is a cross-judge agreement diagnostic, not a ranking.

## 6. Files

Gitignored, not committed (this repository is public):
- `logs/d07fix-20261019/diag/`: `raw.jsonl` (step 1), `raw-anchored-fmt-v1.jsonl` and
  `raw-anchored-fmt.jsonl` (the step 2 checks).
- `logs/d07fix-20261019/stage1b-fixed/`: `records.jsonl` (with raw replies), `results.json`,
  `projection.json`, `spend_tally.txt`.

Committed: the tool change and `tests/test_d07_anchored_fmt_20261019c.py` (`9bd3dc5c`), and this
report.

---

**Canary:** WALKWORTHY-CANARY-7f3e2026 · no holdout content.
