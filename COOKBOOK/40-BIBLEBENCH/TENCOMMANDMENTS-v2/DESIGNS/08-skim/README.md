# SKIM P1

SKIM P1 currently contains 640 frozen logical records, 640 aligned private-gold
records, and 800 executable runtime requests.  The shared custody runtime lives
at `TENCOMMANDMENTS/harness/custody_stack`; SKIM composes that implementation
and does not maintain a second custody stack.

## Cheap OpenRouter engineering smoke

The frozen engineering smoke executes three requests (primary, clean, and
recognition) against three inexpensive models.  It is explicitly
`eligible_for_empirical_decision=false`; it is a transport, custody, scoring,
and cost-control check, not an official benchmark result.

Run the offline contract first:

```bash
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY -m pytest TENCOMMANDMENTS-v2/DESIGNS/08-skim/tests/test_harness.py -q
```

Then run a paid smoke into a new, absent output directory:

```bash
set -a
source "$HOME/.codex/secrets/openrouter.env"
set +a
PY=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python
$PY TENCOMMANDMENTS-v2/DESIGNS/08-skim/harness/run_openrouter_smoke.py \
  --execute-paid-live \
  --output-dir TENCOMMANDMENTS-v2/DESIGNS/08-skim/pilots/20260711-cheap-openrouter-smoke-rerun-01
```

The runner requires explicit paid opt-in, the exact frozen config hash, the
three configured model/provider pairs, provider fallbacks disabled, complete
parameter support, canonical frozen bank/gold/runtime hashes, and a fresh
output directory.  It estimates the worst-case initial-plus-repair schedule
before transport, enforces the `$0.01` aggregate cap before every call, permits
one neutral syntax repair only, and writes sanitized failure custody if a paid
response is rejected.

The first real smoke completed on 2026-07-11:

- 9 scheduled requests and 9 paid calls;
- 9 valid one-event terminal custody chains;
- 9 mechanically scored episodes;
- providers Novita, DeepInfra, and DekaLLM (three calls each);
- total returned cost `$0.00013118`;
- conservative preflight bound `$0.00154864`;
- zero exact API-key, full-prompt, private-map, or raw-response-value hits.

Artifacts are under `pilots/20260711-cheap-openrouter-smoke/`.  The frozen
configuration is `configs/openrouter-cheap-engineering-smoke.json`, SHA-256
`498361a8322ff4211fae8e156405fb5306738a2418662c861045a026269a6468`.

## Scientific status

The cheap smoke does not satisfy the professional-realism, same-harness human
baseline, real-LLM fine-tune, three-seed, or official multi-vendor gates.  Those
remain separately reported prerequisites; no synthetic or engineering-smoke
artifact may be promoted to official evidence.
