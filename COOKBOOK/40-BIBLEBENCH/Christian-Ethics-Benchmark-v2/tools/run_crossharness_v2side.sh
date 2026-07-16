#!/bin/zsh
# Cross-harness Option A — v2 side: MVP-A1 60-item slice × 2 overlapping SUTs, judge-A.
# Owner GO: 20260716-owner-ruling-f1-and-spend-go.md (ceiling $0.75 NTE).
# Judge-B afterwards via tools/rescore/rescore.py (see crossharness design memo §2).
# R10: --max-tokens 4096 --max-connections 4; item scoping via -T item_ids= only.
set -e
cd "$(dirname "$0")/.."
source ~/.codex/secrets/openrouter.env

LOGROOT=logs/crossharness-20260716
JUDGE_A=openrouter/openai/gpt-4.1-nano

typeset -A IDS TASK
IDS[01]="WW-01-A01,WW-01-A05,WW-01-A05-P,WW-01-B01,WW-01-B03,WW-01-D04"
IDS[02]="WW-02-A02,WW-02-A05,WW-02-B02,WW-02-B03,WW-02-B04,WW-02-C02"
IDS[03]="WW-03-A01,WW-03-A04,WW-03-A05,WW-03-B01,WW-03-B03,WW-03-B05"
IDS[04]="WW-04-A03,WW-04-A04,WW-04-B01,WW-04-B04,WW-04-D01,WW-04-D05"
IDS[05]="WW-05-A01,WW-05-A03,WW-05-B01,WW-05-B02,WW-05-B06,WW-05-C05"
IDS[06]="WW-06-A01,WW-06-A05,WW-06-A06,WW-06-B02,WW-06-B04,WW-06-D03"
IDS[07]="WW-07-A02,WW-07-A03,WW-07-B02,WW-07-B04,WW-07-C01,WW-07-C02"
IDS[08]="WW-08-A02,WW-08-A04,WW-08-B01,WW-08-B02,WW-08-B04,WW-08-D02"
IDS[09]="WW-09-A04,WW-09-A05,WW-09-B01,WW-09-B04,WW-09-C01,WW-09-C04"
IDS[10]="WW-10-A01,WW-10-A03,WW-10-A05,WW-10-B01,WW-10-B04,WW-10-B05"
TASK[01]=design01_goodsamaritan; TASK[02]=design02_twomasters
TASK[03]=design03_quiettongue;   TASK[04]=design04_innerweight
TASK[05]=design05_ordoamoris;    TASK[06]=design06_crookedpath
TASK[07]=design07_seventyseven;  TASK[08]=design08_vocationfork
TASK[09]=design09_doubleedge;    TASK[10]=design10_strangergate

for SUT_PAIR in "mistral-small:openrouter/mistralai/mistral-small-3.2-24b-instruct" \
                "gemini-flash-lite:openrouter/google/gemini-2.5-flash-lite"; do
  NAME="${SUT_PAIR%%:*}"; SLUG="${SUT_PAIR#*:}"
  for D in 01 02 03 04 05 06 07 08 09 10; do
    echo "=== $NAME design$D ==="
    .venv/bin/inspect eval "tasks/${TASK[$D]}.py" --model "$SLUG" \
      -T judge_model=$JUDGE_A -T "item_ids=${IDS[$D]}" \
      --max-tokens 4096 --max-connections 4 \
      --log-dir "$LOGROOT/$NAME" 2>&1 | tail -2
  done
done
echo "ALL v2-side slice runs complete."
