# T1 Provisional Runner Shim (CLI-OAuth backends)

A vendor-agnostic model runner whose backends drive **subscription/OAuth CLIs**
(`claude`, `codex`, `gemini`) instead of APIs. It exists so vault harnesses can
run real-token integration tests and pilot probes **now**, before API keys land,
without any caller ever touching a CLI directly.

> **Provenance:** every real-token completion produced here is class
> **`cli-oauth-provisional`** — real model, injected vendor scaffold, no sampling
> control, model id as self-reported. It may validate machinery and pilot designs;
> it may **NEVER** stand in for an API measurement, enter a frozen verdict, or be
> published as model behavior. Authorization + full rules:
> `INNOVATION/20260709d-cli-oauth-provisional-ruling.md`.

## The T1 contract (why this is a shim, not a CLI wrapper)

Callers see **only** three vendor-agnostic types and never a CLI flag:

```python
from t1_runner import ModelRequest, Runner, ResponseStatus, TranscriptLogger
from t1_runner.backends import AnthropicCLIBackend, OpenAICLIBackend

runner = Runner(
    backends=[AnthropicCLIBackend(model_alias="haiku"), OpenAICLIBackend()],
    transcript=TranscriptLogger("transcripts", runid="myrun"),
    timeout_s=120,
)
result = runner.run_item(ModelRequest(prompt="Reply OK", item_id="q1"))
for name, resp in result.responses.items():
    print(name, resp.status, resp.model_id_reported, resp.text)
```

`Runner` captures each backend's CLI version once at construction and stamps it on
every record; it logs every call to the transcript; the caller sees a
`ModelResponse` per backend and nothing CLI-specific.

### `ModelResponse` fields (spec-mandated)
`text`, `status` (`ok|refusal|error|timeout|parse_failure`), `backend`,
`model_id_reported`, `cli_version`, `provenance` (=`cli-oauth-provisional`),
`latency_s`, `raw_output` (+ `raw_output_path` where applicable), `argv`,
`timestamp`, `error_detail`, `self_reported_model`, and the originating `request`.

**Refusals are data.** A soft refusal / safe-completion is returned as
`status=refusal`, never raised. Errors, timeouts, and parse failures are likewise
classified, never thrown — backends never raise for a model-side outcome.

## How a future API backend drops in (zero caller changes)

Implement the ABC and register it — nothing above the `RunnerBackend` boundary
changes:

```python
from t1_runner.core import RunnerBackend, ModelRequest, ModelResponse, ResponseStatus

class AnthropicAPIBackend(RunnerBackend):
    name = "anthropic_api"
    def cli_version(self) -> str:
        return "anthropic-sdk x.y.z"          # or SDK version
    def run(self, request: ModelRequest, timeout_s: float) -> ModelResponse:
        # call the real API with temperature/seed control, set provenance="api",
        # return a ModelResponse with the same fields
        ...
```

Then `Runner([AnthropicAPIBackend(), ...])`. Because callers only speak
`ModelRequest`/`ModelResponse`, swapping CLI→API is a one-line backend change.
(An API backend would also set a different `provenance` and expose sampling
params in `ModelRequest.params` — the CLI backends deliberately cannot.)

## Backend status (this machine, 2026-07-09)

| Backend | CLI | Status | Invocation (see `20260709-cli-bringup-log.md`) |
|---|---|---|---|
| `anthropic_cli` | `claude` 2.1.183 | **WORKING** | `claude -p PROMPT --model <alias> --output-format json </dev/null` (inherited env; model id from `result.modelUsage` key) |
| `openai_cli` | `codex` 0.134.0 | **WORKING** | `codex exec --json --skip-git-repo-check --sandbox read-only -C <dir> -o <last> PROMPT </dev/null` (no `-m`; model id = config default `gpt-5.5`) |
| `google_cli` | `gemini` 0.41.2 | **BROKEN** | account tier deprecated (`IneligibleTierError`); backend implemented, not registered by default |

## Layout

```
t1_runner/
  core.py            ModelRequest / ModelResponse / ResponseStatus / RunnerBackend / Runner / classify_refusal
  transcript.py      append-only JSONL logger (one file per run, full req+resp+provenance)
  provenance.py      cli-oauth-provisional stamping
  backoff.py         exponential backoff + jitter, injectable sleep
  backends/
    anthropic_cli.py  claude -p
    openai_cli.py     codex exec
    google_cli.py     gemini headless (BROKEN on this account)
tests/
  test_core.py             mocked-subprocess unit tests (no tokens)
  test_transcript.py       transcript round-trip + append-only + provenance
  test_backoff.py          deterministic backoff
  test_integration_real.py real-token GREEN lane, @pytest.mark.real_tokens (skippable)
run_smoke.py         GREEN smoke driver (10 items x working backends)
20260709-smoke-items.jsonl   smoke item bank
20260709-cli-bringup-log.md  empirical CLI bring-up evidence (exact flags + why)
20260709-smoke-report.md     smoke results + quirks
```

## Running

```bash
VENV=/Users/jimmy.lin/Documents/CEI-Literature-Vault/.venv/bin/python

# Unit tests (mocked, no tokens) — default deselects real_tokens
$VENV -m pytest -q

# Real-token GREEN-lane integration tests (makes ~3 real calls)
$VENV -m pytest -q -m real_tokens -o addopts=""

# Smoke probe (10 items x 2 working backends = ~20 real calls)
$VENV run_smoke.py                    # writes transcripts/20260709-smoke.jsonl
SMOKE_RUNID=smoke2 $VENV run_smoke.py # fresh runid, never overwrites a prior transcript
```

## Guardrails baked in
- Hard per-call subprocess timeout → `TIMEOUT` status, never a hang.
- `stdin=DEVNULL` on every backend (both working CLIs otherwise read/append stdin).
- Inherited env (stripping it breaks `claude` subscription auth).
- Backoff w/ jitter on transient failures / rate-limit signals from call one.
- Full JSONL transcript of every real call; transcript files carry a `20260709-` date prefix and are append-only (never overwritten — vault Report Immutability rule).
- Volume: pilot scale only (ruling §5 cap ≤ ~500 calls/family/session).
```
