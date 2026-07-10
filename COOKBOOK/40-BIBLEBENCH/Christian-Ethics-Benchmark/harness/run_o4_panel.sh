#!/usr/bin/env bash
# WALKWORTHY O4 full panel launcher — one resumable process PER SUT (per-SUT
# parallelism, F-1). Full split (344 runnable items), frozen judges (§E), default
# frontier state classifier (pinned command leaves --classifier-model unset).
# Re-run to RESUME (each per-SUT scored_items.jsonl is the checkpoint).
set -u
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
cd "$(dirname "$0")" || exit 1
LOGDIR=/tmp/ww-o4-panel-logs
mkdir -p "$LOGDIR"

JUDGE1=openai/gpt-4.1-mini
JUDGE2=google/gemini-2.5-flash

# SUT slug -> short dir suffix
declare -a SUTS=(
  "openai/gpt-4.1|gpt41"
  "google/gemini-2.5-pro|gemini25pro"
  "anthropic/claude-sonnet-4|claude-sonnet4"
  "deepseek/deepseek-chat|deepseek"
  "mistralai/mistral-large-2512|mistral-large"
  "meta-llama/llama-3.3-70b-instruct|llama33"
)

pids=()
for entry in "${SUTS[@]}"; do
  slug="${entry%%|*}"; short="${entry##*|}"
  panel="20260711-o4-${short}"
  log="${LOGDIR}/${short}.log"
  echo "[launch] ${slug} -> runs/${panel}  (log ${log})"
  PYTHONUNBUFFERED=1 "$PY" -m walkworthy.panel \
    --items-per-design 0 \
    --sut-models "${slug}" \
    --judge1-model "${JUDGE1}" \
    --judge2-model "${JUDGE2}" \
    --panel "${panel}" \
    --kind o4-panel \
    --date 20260711 \
    > "${log}" 2>&1 &
  pids+=($!)
done

echo "[launch] ${#pids[@]} per-SUT processes started: ${pids[*]}"
fail=0
for pid in "${pids[@]}"; do
  wait "$pid" || fail=$((fail+1))
done
echo "[done] all per-SUT processes exited; failures=${fail}"
exit "$fail"
